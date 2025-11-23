import sys

import gi

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Gtk, Adw
from kilowatt.util.locales import init_locale
from kilowatt.util.ui import ui_path

from kilowatt.view.example_button import ExampleButton

APPLICATION_ID = 'io.github.dlippok.kilowatt'
init_locale(APPLICATION_ID)

class Application(Adw.Application):
    def __init__(self):
        super().__init__(application_id=APPLICATION_ID)
        self.builder = Gtk.Builder()
        self.builder.add_from_file(ui_path("main_window.ui"))

    def do_activate(self):
        window: Adw.ApplicationWindow = self.builder.get_object("main_window")
        window.get_child()
        self.add_window(window)
        window.present()


def run():
    app = Application()
    app.run(sys.argv)
