#!/usr/bin/sh
# TODO: Build yacd and copy automatically.
echo "Copying files..."
cp -rf ./sing-box/config.json /usr/local/etc/sing-box/config.json
cp -rf ./sing-box/cert.pem /var/lib/sing-box/cert.pem
cp -rf ./sing-box/key.pem /var/lib/sing-box/key.pem
