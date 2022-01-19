# UrlBrowserMapper

Do you have a couple of browsers/profiles and tens of PWAs installed? 

Are you tired of copy-pasting URLs from one browsers/profile to another?

Are you annoyed because a link opens in the default browsers instead of the PWA?

Fret not, `ubm` is here.

### How does it work ?

You configure ubm (which you will set as your default browser) with ubmctl by mapping domains/ips
to browsers and corresponding profiles.

Your system will open all urls in ubm which will search through the configuration file and open the url based on the configuration provided.

This is still in beta, so please be patient

### Installation
1. Clone the repository and cd into it

```
git clone https://github.com/AlfredEVOL/browser-mapper.git
```

2. Install it using make

```
make install
```

To uninstall 
```
make uninstall
```

3. To set ubm as the default browser

```
xdg-settings set default-web-browser UrlBrowserMapper.desktop`
```

4. Once installed, configure the default browser with ubmctl

```
ubmctl --set-default <Browser> <Profile>
```

To find the browser profile see [here](#Browser Profiles)

### Configuration

UrlBrowserMapper comes with the runner `ubm` and the configuration tool `ubmctl`. Run `ubmctl -h` to see all the options.

The configuration file is store in \$HOME/.config/ubm/config.json. If `ubmctl` feels like a lot work, you can directly edit the config file.

### Browser Profiles

Browser Profiles are handled differently by browsers.

#### For firefox and its derivates

* Go to `about:profiles` to see the profiles

#### For Chromium and its derivates

* Go to `chrome://version` and check the Profile Path section
* The last part of the Profile Path will the profile name
* Enclose profile name with single quotes when using ubmctl

#### For FirefoxPWA

* When using ubmctl, use firefoxpwa as the browser name
* Go to \$HOME/.local/share/applications
* The desktop entries of the pwa are there named as FFPWA-{a sequence of numbers and letters}
* Open them to see which app they belong.
* Use the sequence of numbers and letters as the profile name

#### For Epiphany

*UBM should support epiphany profiles though I haven't tested it yet*

#### For PWAs on chromium and chromium-based browser

*no support yet*

