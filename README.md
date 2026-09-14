<div align="center">

# 🛡️ NetSentry

### Advanced Python Network Port Scanner for Cyber Security Professionals

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**Fast • Lightweight • Multithreaded • Professional Reporting**

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Architecture](#-architecture)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Executable Release](#-executable-release)
- [Reports](#-reports)
- [Testing](#-testing)
- [Security and Responsible Use](#-security-and-responsible-use)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 🚀 Overview

**NetSentry** is a modular Python-based network port scanner designed for cyber security students, penetration testers, and security analysts.

It performs TCP port scanning, checks host availability, identifies common services, grabs service banners, and generates reports in multiple formats. The project uses a clean, modular architecture to support maintainability, testing, and future feature expansion.

> **NetSentry = Network + Sentry**  
> A lightweight network guardian for visibility and security assessment.

---

## ✨ Features

| Feature | Status |
|---|:---:|
| TCP Port Scanning | ✅ |
| Multithreaded Scanning | ✅ |
| Host Discovery | ✅ |
| Service Detection | ✅ |
| HTTP/HTTPS Banner Grabbing | ✅ |
| Generic Banner Grabbing | ✅ |
| Progress Bar | ✅ |
| Colored CLI Output | ✅ |
| Input Validation | ✅ |
| Logging | ✅ |
| Scan History | ✅ |
| JSON Reports | ✅ |
| CSV Reports | ✅ |
| HTML Reports | ✅ |
| PDF Reports | ✅ |
| Unit Tests | ✅ |
| Windows and Linux Support | ✅ |

---

## 📂 Project Structure

```text
NetSentry/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── assets/
│   ├── NetSentry.ico
│   └── NetSentry.png
│
├── scanner/
│   ├── __init__.py
│   ├── config.py
│   ├── validator.py
│   ├── exceptions.py
│   ├── logger.py
│   ├── scanner.py
│   ├── service.py
│   ├── banner.py
│   ├── report.py
│   ├── history.py
│   ├── colors.py
│   ├── host.py
│   └── pdf_report.py
│
├── tests/
│   ├── __init__.py
│   ├── test_banner.py
│   ├── test_history.py
│   ├── test_scanner.py
│   ├── test_service.py
│   └── test_validator.py
│
├── reports/
├── history/
└── logs/
```

---

## 🏗 Architecture

```text
User
  │
  ▼
Command-Line Interface
  │
  ▼
Input Validation
  │
  ▼
Host Discovery
  │
  ▼
Multithreaded TCP Scanner
  │
  ├──► Service Detection
  │
  └──► Banner Grabbing
          │
          ▼
     Report Generator
          │
          ├──► JSON
          ├──► CSV
          ├──► HTML
          └──► PDF
          │
          ▼
     Scan History and Logs
```

---

## 🛠 Technologies Used

- **Python 3.12**
- **Socket Programming**
- **ThreadPoolExecutor**
- **argparse**
- **tqdm**
- **colorama**
- **ReportLab**
- **JSON**
- **CSV**
- **HTML**
- **pytest**

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/megh3905/NetSentry.git
```

### 2. Open the project directory

```bash
cd NetSentry
```

### 3. Create and activate a virtual environment

#### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Usage

### Display the help menu

```bash
python main.py --help
```

### Scan a target using the default configuration

```bash
python main.py scanme.nmap.org
```

### Scan a custom port range

```bash
python main.py scanme.nmap.org --start 1 --end 1000
```

### Scan localhost

```bash
python main.py 127.0.0.1
```

> Only scan systems that you own or have explicit permission to assess.

---

## 📦 Executable Release

A standalone Windows executable is available in the GitHub Releases section.

1. Open the repository's **Releases** page.
2. Open the latest release.
3. Download `NetSentry.exe`.
4. Run the executable from Windows.

The executable includes the NetSentry application and uses the custom NetSentry icon.

---

## 📊 Example Output

```text
Target      : scanme.nmap.org
Host Status : Alive

Scanning: 100% |████████████████████████|

OPEN PORTS
PORT     SERVICE              BANNER
22       SSH                  OpenSSH
80       HTTP                 Apache
443      HTTPS                Open

Reports generated successfully.
Scan completed.
```

---

## 📁 Reports

After a successful scan, NetSentry can generate reports in the following formats:

- **JSON** — structured machine-readable results
- **CSV** — spreadsheet-friendly results
- **HTML** — browser-readable report
- **PDF** — printable professional report

Generated reports are stored in:

```text
reports/
```

Additional runtime data is stored in:

```text
history/
logs/
```

---

## 🧪 Testing

Run the test suite with:

```bash
pytest
```

The tests cover important components such as:

- Input validation
- Port scanning behavior
- Service detection
- Banner grabbing
- Scan history

---

## 🔐 Security and Responsible Use

NetSentry is intended for **authorized security testing, learning, troubleshooting, and network administration**.

Do not scan public systems, networks, or devices without explicit permission. The author is not responsible for misuse of this tool.

---

## 🔮 Future Enhancements

- UDP port scanning
- Operating system fingerprinting
- CVE and vulnerability lookup
- XML report export
- Scheduled scans
- Docker support
- Advanced service fingerprinting
- Optional GUI interface
- Improved stealth and rate-control options

---

## 🤝 Contributing

Contributions, improvements, bug reports, and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Run the test suite.
5. Commit and push your changes.
6. Open a Pull Request.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

### Megh Bhavsar

Bachelor of Engineering in Computer Science and Engineering  
Specialization: Cyber Security

- GitHub: [@megh3905](https://github.com/megh3905)

---

<div align="center">

⭐ If you find NetSentry useful, consider starring the repository.

**Made with ❤️ using Python**

</div>
