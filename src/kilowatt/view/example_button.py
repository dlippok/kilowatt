import gettext

from gi.repository import Gtk

from kilowatt.util.ui import ui_path

_ = gettext.gettext


@Gtk.Template(filename=ui_path("example_button.ui"))
class ExampleButton(Gtk.Button):
    __gtype_name__ = "ExampleButton"

    @Gtk.Template.Callback()
    def on_clicked(self, *args):
        print(_("Button Clicked"))
