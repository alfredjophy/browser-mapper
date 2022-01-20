PREFIX?=/usr/local
install:
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	cp ubm.py $(DESTDIR)$(PREFIX)/bin/ubm
	cp ubmctl.py $(DESTDIR)$(PREFIX)/bin/ubmctl
	mkdir -p $(DESTDIR)$(PREFIX)/share/applications
	cp UrlBrowserMapper.desktop $(DESTDIR)$(PREFIX)/share/applications/
uninstall:
	rm $(DESTDIR)$(PREFIX)/share/applications/UrlBrowserMapper.desktop
	rm $(DESTDIR)$(PREFIX)/bin/{ubm,ubmctl}


