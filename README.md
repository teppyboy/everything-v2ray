# sing-box VPN configuration

For my personal usage

# Client

## Configuration

There are currently 2 app configs

+ [Matsuri](client/config/matsuri.json)
+ [SagerNet](client/config/sagernet.json)

## Profile

There are some preconfigured profiles for your convenience.

### sing-box official app

#### [Android](https://sing-box.sagernet.org/installation/clients/sfa/) / [Windows](https://github.com/SagerNet/sing-box/releases) / [Linux](https://github.com/SagerNet/sing-box/releases)

> On Windows/Linux you need to start sing-box with administrator/root privilege.

+ [vpn-us](client/profile/sfa/vpn-us.json) - [raw](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/sfa/vpn-us.json)
+ [vpn-vn](client/profile/sfa/vpn-vn.json) - [raw](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/sfa/vpn-vn.json)

The one below is for testing only, you need to host the server yourself.

+ [localhost](client/profile/sfa/test.json) - [raw](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/sfa/test.json)

#### [iOS](https://sing-box.sagernet.org/installation/clients/sfi/)

Not tested yet, you can try using Android profiles.

## Certificate

They are generated dummy certificate, replace with your own if you wish to pass the TLS check.

## Web UI

New version of sing-box automatically download yacd GUI and use it automatically.

## License

[MIT](LICENSE)
