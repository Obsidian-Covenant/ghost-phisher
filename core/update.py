# core/update_ui.py

import os
import re
import shutil
import subprocess
import time
import threading
import urllib.request
import urllib.error

from gui import settings
from gui import update_ui

from PyQt6 import QtCore, QtWidgets


class update_class(QtWidgets.QDialog, update_ui.Ui_Dialog):
    # Qt signals (thread-safe to emit from worker threads)
    download_failed = QtCore.pyqtSignal()
    finished_downloading = QtCore.pyqtSignal()
    file_downloaded = QtCore.pyqtSignal()
    restart_application_signal = QtCore.pyqtSignal()
    new_update_available = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current_version = 2.0

        self.new_version = 0.0
        self.git_failure_message = ""

        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Modern signal connections
        self.upgrade_button.clicked.connect(self.update_installer)

        self.download_failed.connect(self.update_timeout_message)
        self.finished_downloading.connect(self.finished_download)
        self.file_downloaded.connect(self.downloading)
        self.restart_application_signal.connect(self.restart_application)

    def display_update_version(self):
        self.update_display_label.setText(
            f"<font color=blue>Version {self.new_version} Available</font>"
        )

    def percentage(self, current, total):
        if not total:
            return "0%"
        float_point = float(current) / float(total)
        calculation = int(float_point * 100)
        return f"{calculation}%"

    def restart_application(self):
        self.label_2.setText("<font color=red>Please Restart Application</font>")

    def finished_download(self):
        self.label_2.setText("<font color=green>Finished Downloading</font>")

    def downloading(self):
        self.label_2.setText(
            f"<font color=green>{self.percentage(self.files_downloaded, self.file_total)} Complete</font>"
        )

    def update_timeout_message(self):
        self.label_2.setText("<font color=red>Network timeout</font>")

    def update_error(self):
        # Read stderr from git process (bytes -> str)
        try:
            failure = self.git_access.stderr.read()
            if isinstance(failure, (bytes, bytearray)):
                failure = failure.decode("utf-8", errors="replace")
            self.git_failure_message = failure or ""
            if self.git_failure_message:
                self.label_2.setText(
                    "<font color=red>Update Failed:" + self.git_failure_message + "</font>"
                )
        except Exception:
            # keep it quiet; errors will be handled by download_failed signal later
            pass

    def update_installer(self):
        self.label_2.setText("<font color=green>Downloading...</font>")
        t = threading.Thread(target=self.update_launcher, daemon=True)
        t.start()

    def update_launcher(self):
        """Downloads and installs update files."""
        self.file_total = 0
        self.files_downloaded = 0

        forbidden_files = ["Settings", "Ghost-Phisher-Database"]
        update_directory = "/tmp/Ghost-Phisher/"
        git_path = "https://github.com/Obsidian-Covenant/ghost-phisher/tree/master/Ghost-Phisher/"

        try:
            # Fetch update manifest (bytes -> str)
            online_response_check = urllib.request.urlopen(
                "https://raw.githubusercontent.com/Obsidian-Covenant/ghost-phisher/master/Ghost-Phisher/UPDATE"
            )
            online_response = online_response_check.read()
            if isinstance(online_response, (bytes, bytearray)):
                online_response = online_response.decode("utf-8", errors="replace")

            total_files_re = re.compile(r"total_files\s*=\s*(\d+)", re.IGNORECASE)
            for line in online_response.splitlines():
                m = total_files_re.search(line)
                if m:
                    self.file_total = int(m.group(1))
                    break

            if os.path.exists(update_directory):
                shutil.rmtree(update_directory)

            # GIT checkout into /tmp
            self.git_access = subprocess.Popen(
                f"cd /tmp/ \n git checkout {git_path}",
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
                text=False,  # we want bytes from stdout for consistent handling
            )

            threading.Thread(target=self.update_error, daemon=True).start()

            git_update = self.git_access.stdout

            while True:
                response = git_update.readline()
                if not response:
                    # process ended or no output; small sleep avoids tight loop
                    time.sleep(0.05)

                if response:
                    self.files_downloaded += 1
                    self.file_downloaded.emit()

                # detect "revision" in output (bytes -> str)
                resp_text = response.decode("utf-8", errors="replace") if isinstance(response, (bytes, bytearray)) else str(response)

                if "revision" in resp_text.lower():
                    self.finished_downloading.emit()

                    # Remove old files/dirs (excluding forbidden)
                    for old_file in os.listdir(os.getcwd()):
                        full = os.path.join(os.getcwd(), old_file)
                        if os.path.isfile(full) and old_file not in forbidden_files:
                            os.remove(full)

                    for old_directory in os.listdir(os.getcwd()):
                        full = os.path.join(os.getcwd(), old_directory)
                        if os.path.isdir(full) and old_directory not in forbidden_files:
                            shutil.rmtree(full)

                    # Copy in update files
                    for update_file in os.listdir(update_directory):
                        src = os.path.join(update_directory, update_file)
                        dst = os.path.join(os.getcwd(), update_file)

                        if os.path.isfile(src):
                            shutil.copyfile(src, dst)
                            os.chmod(dst, 0o777)
                        else:
                            shutil.copytree(src, dst)
                            # chmod a directory tree carefully (optional; keeping your behavior)
                            for root, dirs, files in os.walk(dst):
                                os.chmod(root, 0o777)
                                for name in files:
                                    os.chmod(os.path.join(root, name), 0o777)

                    time.sleep(5)

                    whats_new = settings.Ghost_settings()
                    whats_new.create_settings("disable whats new window", "True")
                    whats_new.close_setting_file()

                    self.restart_application_signal.emit()
                    break

                if len(self.git_failure_message) > 2:
                    self.download_failed.emit()
                    break

        except (urllib.error.URLError, urllib.error.HTTPError):
            self.download_failed.emit()
        except Exception:
            self.download_failed.emit()

    #
    # Update checker thread
    #
    def update_initializtion_check(self):
        while True:
            try:
                online_response_thread = urllib.request.urlopen(
                    "https://raw.githubusercontent.com/Obsidian-Covenant/ghost-phisher/master/Ghost-Phisher/UPDATE"
                )
                online_response = online_response_thread.read()
                if isinstance(online_response, (bytes, bytearray)):
                    online_response = online_response.decode("utf-8", errors="replace")

                online_version = re.compile(r"version\s*=\s*(\d*?\.\d*)", re.IGNORECASE)
                found = online_version.findall(online_response)
                if not found:
                    break

                update_version_number = float(found[0])

                if float(self.current_version) != update_version_number:
                    self.new_version = update_version_number
                    self.new_update_available.emit()
                    break

                if float(self.current_version) == update_version_number:
                    break

            except Exception:
                time.sleep(9)
