#!/usr/bin/env python3
from pathlib import Path


def main():
    # SFA
    sfa_base_path = "client/profile/sfa/"
    sn_base_path = "client/profile/sagernet/"
    print("[INFO] Copying for SFA...")
    sfa_config_text = Path(sfa_base_path + "test.json").read_text()
    sn_config_text = Path(sn_base_path + "test.json").read_text()
    files = {
        "vpn-us.json": {
            "ip": "150.136.91.11",
            "name": "Zafkiel / US (Oracle)",
        },
        "vpn-hk-gce.json": {
            "ip": "35.215.183.30",
            "name": "Zafkiel / HK (GCE)",
        },
        "vpn-vn.json": {
            "ip": "116.111.113.94",
            "name": "Zafkiel / VN",
        },
    }
    for file, ip in files.items():
        print(f"[INFO] Copying test.json to {file}...")
        Path(sfa_base_path + file).write_text(
            sfa_config_text.replace("127.0.0.1", ip["ip"])
        )
        print("[INFO] Copying for SagerNet...")
        Path(sn_base_path + file).write_text(
            sn_config_text.replace("127.0.0.1", ip["ip"]).replace("{name}", ip["name"])
        )


if __name__ == "__main__":
    main()
