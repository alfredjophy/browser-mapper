PREFIX?=$(HOME)/.local
install:
	cp ubm/ubm.py $(PREFIX)/bin/ubm
	cp ubm/ubmctl.py $(PREFIX)/bin/ubmctl
	cp UrlBrowserMapper.desktop $(PREFIX)/share/applications/
uninstall:
	rm $(PREFIX)/share/applications/UrlBrowserMapper.desktop
	rm $(PREFIX)/bin/{ubm,ubmctl}


