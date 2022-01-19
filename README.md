# UrlBrowserMapper

Do you have a couple of browsers/profiles and tens of PWAs installed? 

Are you tired of copy-pasting URLs from one browsers/profile to another?

Are you annoyed because a link opens in the default browsers instead of the PWA?

Fret not, `ubm` is here.

### How does it work ?

You configure ubm (which you will set as your default browser) with ubmctl by mapping urls/domains/url patterns (as regex)
to browsers and corresponding profiles.

Your system will open all urls in ubm which will search through the configuration file and open the url based on the configuration provided.

This is still in beta, so please be patient

### Installation

1. Clone the repos
2. `make install`

* To set ubm as the default browser, `xdg-settings set default-web-browser UrlBrowserMapper.desktop`

1. To remove, `make uninstall`




