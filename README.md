# 🔍 Python TCP Port Scanner

## 🎯 Objective
A foundational network reconnaissance script built to identify open TCP ports on target systems. This project demonstrates core Attack Surface Management concepts and fundamental Python network programming using the native socket library.

## 🛠️ Skills & Technologies Demonstrated
*   **Network Protocols:** Application of IPv4 routing, dynamic DNS resolution, and TCP handshakes.
*   **Python Socket Programming:** Direct interaction with the network stack using `socket.AF_INET` and `socket.SOCK_STREAM`.
*   **Defensive Programming:** Implementation of robust `try/except` blocks to gracefully handle DNS resolution failures (`socket.gaierror`), dropped connections, and manual user interruptions (`KeyboardInterrupt`).

## 🚀 Features
*   **Sequential Port Scanning:** Iterates sequentially through standard TCP service ports (1-1024) to verify open entry points.
*   **Automated DNS Resolution:** Translates human-readable hostnames directly into IPv4 addresses prior to initiating the scan.
*   **Zero Dependencies:** Runs entirely on Python's standard library (`socket`, `sys`, `datetime`), requiring no external packages or virtual environments.

## 💻 Installation & Usage

### Prerequisites
*   Python 3.x natively installed on your system.

### Execution
Execute the script via the command line by passing the target IP or hostname as a positional argument:

```bash
python scanner.py <target-ip-or-domain>
