#!/usr/bin/env python3
from pathlib import Path
from base64 import b64encode


def main():
    # SFA
    sfa_base_path = "client/profile/sfa/"
    sn_base_path = "client/profile/sagernet/"
    v2n_base_path = "client/profile/v2rayng/"
    print("[INFO] Copying...")
    sfa_config_text = Path(sfa_base_path + "test.json").read_text()
    sn_config_text = Path(sn_base_path + "test.json").read_text()
    v2n_config_text = Path(v2n_base_path + "test.json").read_text()
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
            "ip": "tretrauit.duckdns.org",
            "name": "Zafkiel / VN",
        },
    }
    v2n_subscription_text = ""
    for file, ip in files.items():
        print(f"[INFO] Copying test.json to {file}...")
        print("[INFO] Copying for SFA...")
        Path(sfa_base_path + file).write_text(
            sfa_config_text.replace("127.0.0.1", ip["ip"])
        )
        print("[INFO] Copying for SagerNet...")
        Path(sn_base_path + file).write_text(
            sn_config_text.replace("127.0.0.1", ip["ip"]).replace("{name}", ip["name"])
        )
        v2n_file_text = v2n_config_text.replace("127.0.0.1", ip["ip"]).replace(
            "{name}", ip["name"]
        )
        print("[INFO] Copying for v2rayNG (JSON)...")
        Path(v2n_base_path + file).write_text(v2n_file_text)
        print("[INFO] Copying for v2rayNG (URL)...")
        v2n_url = f"vmess://{b64encode(v2n_file_text.encode()).decode()}"
        Path(v2n_base_path + file[:-5]).write_text(v2n_url)
        v2n_subscription_text += v2n_url + "\n"
    print("[INFO] Copying for v2rayNG (Subscription)...")
    Path(v2n_base_path + "subscription.txt").write_text(v2n_subscription_text)


if __name__ == "__main__":
    main()
