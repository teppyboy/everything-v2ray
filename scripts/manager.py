#!/usr/bin/env bash
from subprocess import run, PIPE
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="manager",
        description="Manage the application",
        epilog="#KurumiTokisaki",
    )
    subparsers = parser.add_subparsers(required=True)
    vpn = subparsers.add_parser("vpn", help="sing-box related commands")
    parser.parse_args()


if __name__ == "__main__":
    main()
