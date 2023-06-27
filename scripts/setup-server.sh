#!/usr/bin/sh
# TODO: Build yacd and copy automatically.
echo "sing-box server quick setup script."
if ! command -v sing-box &> /dev/null
then
    echo "sing-box not found, please install sing-box first."
    echo "For servers, see https://sing-box.sagernet.org/examples/linux-server-installation/"
    exit
fi
echo "Copying config..."
cp -rf ./sing-box/config.json /usr/local/etc/sing-box/config.json
echo "Copying dummy ceritificate (for Hysteria support)..."
cp -rf ./sing-box/cert.pem /var/lib/sing-box/cert.pem
cp -rf ./sing-box/key.pem /var/lib/sing-box/key.pem
echo "Done."
