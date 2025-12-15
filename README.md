# Ghost Phisher

## Modernization Covenant

This is a refactored and modernized edition of **Ghost Phisher**, a GUI suite for phishing and penetration attacks.

Key changes:

- ✅ Migration to Python 3
- ✅ Migration to PyQt6
- ✅ Vendored Bottle replaced by the standard Python Bottle package

**Future enhancements:**
* According to the code analysis, the project needs to be more robust because the original one didn't manage some exceptions that cause the application to crash.

### Installation

#### Dependencies

Runtime dependencies:
```
aircrack-ng metasploit python python-bottle python-pyqt6 python-scapy xterm
```

#### From source

```bash
git clone https://github.com/Obsidian-Covenant/ghost-phisher.git
cd ghost-phisher
sudo python ghost.py
```

## README

<hr>
  <h5>Create portable static executables from dynamic executables that will run on every distribution of linux without the need of recompiling, <a target="_blank" href="https://www.elfex-linker.com">Click here</a> for more information</h5>
  <hr>
  
<i><b>Ghost Phisher</b></i> is a Wireless and Ethernet security auditing and attack software program written using the <a href="https://www.python.org/">Python Programming Language</a> and the <a href="https://www.riverbankcomputing.co.uk/software/pyqt/intro">Python Qt GUI library</a>, the program is able to emulate access points and deploy various internal networking servers for networking, penetration testing and phishing attacks.

### Operating Systems Supported
The Software runs on any <i>Linux machine</i> with the programs <a href="#prerequisites">prerequisites</a>, But the program has been tested on the following Linux based operating systems:
<p>1. <a href="https://www.ubuntu.com/">Ubuntu KDE/GNOME</a></p>
<p>2. <a href="https://www.backtrack-linux.org/">BackTrack Linux</a></p>
<p>3. <a href="https://www.backbox.org/">BackBox Linux</a></p>


### Prerequisites
The Program requires the following to run properly:<br>
The following dependencies can be installed using the <i>Debian package installer</i> command on Debian based systems using "apt-get install program" or otherwise downloaded
and installed manually
<p>1. <a href="https://www.aircrack-ng.org/">Aircrack-NG</a></li>
<p>2. <a href="https://www.secdev.org/projects/scapy/">Python-Scapy</a></li>
<p>3. <a href="https://www.riverbankcomputing.co.uk/software/pyqt/intro">Python Qt6</a></li>
<p>4. <a href="https://www.python.org/">Python</a></li>
<p>5. <a href="https://subversion.tigris.org/">Subversion</a></li>
<p>6. <a href="https://invisible-island.net/xterm/">Xterm</a></li>
<p>7. <a href="https://www.metasploit.com/">Metasploit Framework</a> <i>(Optional)</i></li>
<hr>

### Features
<hr>
<i>Ghost Phisher</i> currently supports the following features:

<p>1. <i>HTTP Server</i></li>
<p>2. <i>Inbuilt RFC 1035 DNS Server</i></li>
<p>3. <i>Inbuilt RFC 2131 DHCP Server</i></li>
<p>4. <i>Webpage Hosting and Credential Logger (Phishing)</i></li>
<p>5. <i>Wifi Access point Emulator</i></li>
<p>6. <i>Session Hijacking (Passive and Ethernet Modes)</i></li>
<p>7. <i>ARP Cache Poisoning (MITM and DOS Attacks)</i></li>
<p>8. <i>Penetration using Metasploit Bindings</i></li>
<p>9. <i>Automatic credential logging using SQlite Database</i></li>
<p>10. <i>Update Support</i></li>

<hr>

## Installation

Installation on Debian Package supported systems:
<br><hr>
<code>root@host:~# dpkg -i ghost-phisher_1.5_all.deb</code>
<hr><br>

The <i>source code</i> for the program can be fetched using the following command on terminal
<br><hr>
<code>root@host:~# svn checkout http://ghost-phisher.googlecode.com/svn/Ghost-Phisher/</code>
<hr>


### Other Projects:

https://github.com/savio-code/fern-wifi-cracker

https://github.com/savio-code/hexorbase

<h3><i>Please support Ghost Phisher development</i></h3>
<h3>Bitcoin: &nbsp;&nbsp;  1AoBfNLfwDrw4ofZXZVm9YfeaFCXtG9k9B</h3>
