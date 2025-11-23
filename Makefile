.PHONY: build flatpak-install flatpak-build flatpak-run flatpak-uninstall build

app_package = kilowatt
app_id = io.github.dlippok.kilowatt

sources = $(shell find src/$(app_package)/ -name "*.py")
ui_sources = $(shell find src/$(app_package)/resources/ui -name "*.blp")

update-translations:
	xgettext \
		$(sources) \
		$(ui_sources) \
		--from-code=UTF-8 \
        --add-comments \
        --keyword=_ \
        --keyword=C_:1c,2 \
		-o data/translations/$(app_id).pot

	msgmerge --update  data/translations/de/$(app_id).po data/translations/$(app_id).pot

build:
	mkdir -p build/dist/share
	cp --recursive data/share/* build/dist/share
	blueprint-compiler batch-compile src/$(app_package)/resources/ui/compiled/ src/$(app_package)/resources/ui src/$(app_package)/resources/ui/*.blp

	mkdir -p build/dist/share/locale/de/LC_MESSAGES
	msgfmt data/translations/de/$(app_id).po \
  		-o build/dist/share/locale/de/LC_MESSAGES/$(app_id).mo


install: build
	pip3 install . --prefix $(INSTALL_TARGET) --no-build-isolation
	cp --recursive build/dist/* $(INSTALL_TARGET)

# Flatpak
flatpak-build: build
	flatpak-builder --force-clean build/flatpak flatpak.yaml

flatpak-install: build
	flatpak-builder --user --install --force-clean build/flatpak flatpak.yaml

flatpak-run: flatpak-install
	flatpak run io.github.dlippok.kilowatt

flatpak-uninstall:
	flatpak uninstall -y io.github.dlippok.kilowatt

clean:
	rm -rf .flatpak-builder
	rm -rf build
	rm -rf src/resources/ui/compiled


