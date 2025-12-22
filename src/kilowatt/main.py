import os
import sys

import gi
gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from kilowatt.model.metering import Meter
from kilowatt.view.meter_button import MeterButton
from kilowatt.view.meter_page import MeterPage
from kilowatt.view.start_page import StartPage
from kilowatt.data import METERS
from gi.repository import Gtk, Adw, Gdk
from kilowatt.util.locales import init_locale
from kilowatt.util.ui import ui_path

APPLICATION_ID = 'io.github.dlippok.kilowatt'
init_locale(APPLICATION_ID)


class Application(Adw.Application):
    def __init__(self):
        super().__init__(application_id=APPLICATION_ID)
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(os.path.dirname(__file__) + "/resources/style.css")
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.builder = Gtk.Builder()
        self.builder.add_from_file(ui_path("main_window.ui"))
        self.nav: Adw.NavigationView = self.builder.get_object('nav')

        start_page: StartPage = self.builder.get_object("startPage")
        start_page.update_meters(METERS)
        start_page.connect('meter_selected', self.on_meter_selected)

    def open_meter_page(self, meter: Meter):
        page = MeterPage(meter)
        self.nav.push(page)

    def on_meter_selected(self, page: StartPage, button: MeterButton):
        self.open_meter_page(button.meter)

    def do_activate(self):
        window: Adw.ApplicationWindow = self.builder.get_object("main_window")
        window.get_child()
        self.add_window(window)
        window.present()


def run():
    app = Application()
    app.run(sys.argv)
