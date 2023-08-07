#!/usr/bin/env python3
import json
from pathlib import Path
from base64 import b64encode


def bl_inbound(config: dict | str):
    if isinstance(config, dict):
        if config.get("listen") in ["127.0.0.1", "localhost"]:
            return True
    elif isinstance(config, str):
        if config in ["127.0.0.1", "localhost"]:
            return True
    return False


def loop_replace(
    config: dict,
    ip: str,
    name: str = None,
    local: bool = None,
    ancestor: list[str] = None,
):
    if not ancestor:
        ancestor = []
    # print("Current ancestor:", ancestor)
    new_config = config
    for key, value in config.items():
        if isinstance(value, dict):
            new_config[key] = loop_replace(
                value, ip, name, local, ancestor=ancestor + [key]
            )
        elif isinstance(value, list):
            for index, item in enumerate(value):
                if isinstance(item, dict):
                    new_config[key][index] = loop_replace(
                        item, ip, name, local, ancestor=ancestor + [key]
                    )
        elif isinstance(value, str):
            if bl_inbound(config=config):
                print("[INFO] Skipping inbound")
                continue
            new_config[key] = value.replace("127.0.0.1", ip).replace("localhost", ip)
            if isinstance(name, str):
                new_config[key] = new_config[key].replace("{name}", name)
    return new_config


def replace(string: str, ip: str, name: str = None, local: bool = None):
    new_string = string
    config = json.loads(new_string)
    # print(loop_replace(config=config, ip=ip, name=name, local=local))
    new_string = json.dumps(
        loop_replace(config=config, ip=ip, name=name, local=local), indent=2
    )
    return new_string


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
            replace(sfa_config_text, ip["ip"], local=True)
        )
        print("[INFO] Copying for SagerNet...")
        Path(sn_base_path + file).write_text(
            replace(sn_config_text, ip["ip"], name=ip["name"])
        )
        v2n_file_text = replace(v2n_config_text, ip["ip"], name=ip["name"])
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
