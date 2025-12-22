import os
import sys

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

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
        start_page: StartPage = self.builder.get_object("startPage")
        start_page.update_meters(METERS)

    def do_activate(self):
        window: Adw.ApplicationWindow = self.builder.get_object("main_window")
        window.get_child()
        self.add_window(window)
        window.present()


def run():
    app = Application()
    app.run(sys.argv)
