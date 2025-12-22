import gettext
from typing import List

from gi.repository import Gtk, Adw, GObject

from kilowatt.model.metering import Meter
from kilowatt.util.ui import ui_path
from kilowatt.view.meter_button import MeterButton
from kilowatt.view.meters_box import MetersBox

_ = gettext.gettext


@Gtk.Template(filename=ui_path("start_page.ui"))
class StartPage(Adw.NavigationPage):
    __gtype_name__ = "StartPage"

    meters_box: MetersBox = Gtk.Template.Child("metersBox")

    def __init__(self):
        Adw.NavigationPage.__init__(self)

    @GObject.Signal(arg_types=(MeterButton,))
    def meter_selected(self, button: MeterButton):
        pass

    def update_meters(self, meters: List[Meter]):
        for meter in meters:
            button: MeterButton = MeterButton(meter)
            button.connect('clicked', lambda b: self.emit('meter_selected', b))
            self.meters_box.append(button)

