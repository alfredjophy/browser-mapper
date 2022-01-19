PREFIX?=$(HOME)/.local
install:
	cp ubm.py $(PREFIX)/bin/ubm
	cp ubmctl.py $(PREFIX)/bin/ubmctl
	cp UrlBrowserMapper.desktop $(PREFIX)/share/applications/
uninstall:
	rm $(PREFIX)/share/applications/UrlBrowserMapper.desktop
	rm $(PREFIX)/bin/{ubm,ubmctl}


