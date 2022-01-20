PREFIX?=/usr/local
install:
	cp ubm.py $(DESTDIR)/$(PREFIX)/bin/ubm
	cp ubmctl.py $(DESTDIR)/$(PREFIX)/bin/ubmctl
	cp UrlBrowserMapper.desktop $(DESTDIR)/$(PREFIX)/share/applications/
uninstall:
	rm $(DESTDIR)/$(PREFIX)/share/applications/UrlBrowserMapper.desktop
	rm $(DESTDIR)/$(PREFIX)/bin/{ubm,ubmctl}


