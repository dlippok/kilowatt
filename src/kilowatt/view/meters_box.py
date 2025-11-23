import gettext

from gi.repository import Gtk

from kilowatt.util.ui import ui_path

_ = gettext.gettext


@Gtk.Template(filename=ui_path("meters_box.ui"))
class MetersBox(Gtk.FlowBox):
    __gtype_name__ = "MetersBox"

