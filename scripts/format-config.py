#!/usr/bin/env python3
from subprocess import run
from pathlib import Path


def main():
    config_files = [
        "server/sing-box/config.json",
    ]
    # Add config from SFA
    for file in Path("client/profile/sfa").glob("*.json"):
        config_files.append(str(file))
    # Execute command
    for file in config_files:
        proc = run(["sing-box", "format", "-c", file], capture_output=True)
        if proc.returncode != 0:
            print(f"[ERROR] Failed to format {file}: {proc.stderr.decode()}")
            continue
        with open(file=file, mode="w") as f:
            f.write(proc.stdout.decode())
        print(f"[INFO] Formatted {file}")


if __name__ == "__main__":
    main()