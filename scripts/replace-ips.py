#!/usr/bin/env python3
from pathlib import Path


def main():
    config_text = Path("client/profile/sfa/test.json").read_text()
    files = {
        "client/profile/sfa/vpn-us.json": "150.136.91.11",
        "client/profile/sfa/vpn-vn.json": "116.111.113.94",
    }
    for file, ip in files.items():
        print(f"[INFO] Copying test.json to {file}...")
        Path(file).write_text(config_text.replace("127.0.0.1", ip))


if __name__ == "__main__":
    main()