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

#### [Android](https://sing-box.sagernet.org/installation/clients/sfa/) / [Windows](https://github.com/SagerNet/sing-box/releases) / [Linux](https://github.com/SagerNet/sing-box/releases) / [iOS](https://sing-box.sagernet.org/installation/clients/sfi/)

> On Windows/Linux you need to start sing-box with administrator/root privilege.

> Copy the URL in `raw` to the clipboard and paste it into the app.

+ [vpn-us](client/profile/sfa/vpn-us.json) - [raw](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/sfa/vpn-us.json)
+ [vpn-hk-gce](client/profile/sfa/vpn-hk-gce.json) - [raw](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/sfa/vpn-hk-gce.json)
+ [vpn-vn](client/profile/sfa/vpn-vn.json) - [raw](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/sfa/vpn-vn.json)

The one below is for testing only, you need to host the server yourself.

+ [localhost](client/profile/sfa/test.json) - [raw](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/sfa/test.json)

### SagerNet / Matsuri

> Copy the whole content in the `raw` URL to the clipboard and paste it into the app.

+ [vpn-us](client/profile/sagernet/vpn-us.json) - [raw](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/sagernet/vpn-us.json)
+ [vpn-hk-gce](client/profile/sagernet/vpn-hk-gce.json) - [raw](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/sagernet/vpn-hk-gce.json)
+ [vpn-vn](client/profile/sagernet/vpn-vn.json) - [raw](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/sagernet/vpn-vn.json)

The one below is for testing only, you need to host the server yourself.

+ [localhost](client/profile/sagernet/test.json) - [raw](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/sagernet/test.json)

### v2rayNG (and almost all v2ray clients)

> You can use subscription URL in v2rayNG, which is more convenient, by copying the URL in `raw` to the clipboard and paste it into the app.
> Copy the whole content in the `config` URL or `raw` URL to the clipboard and paste it into the app.

+ [vpn-us](client/profile/v2rayng/vpn-us.json) - [config](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/v2rayng/vpn-us) - [raw](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/v2rayng/vpn-us.json)
+ [vpn-hk-gce](client/profile/v2rayng/vpn-hk-gce.json) - [config](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/v2rayng/vpn-hk-gce) - [raw](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/v2rayng/vpn-hk-gce.json)
+ [vpn-vn](client/profile/v2rayng/vpn-vn.json) - [config](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/v2rayng/vpn-vn) - [raw](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/v2rayng/vpn-vn.json)

+ [subscription](client/profile/v2rayng/subscription.txt) - [raw](https://raw.githubusercontent.com/teppyboy/everything-v2ray/master/client/profile/v2rayng/subscription.txt)

## Certificate

They are generated dummy certificate, replace with your own if you wish to pass the TLS check.

## Web UI

New version of sing-box automatically download yacd GUI and use it automatically.

## License

[MIT](LICENSE)
