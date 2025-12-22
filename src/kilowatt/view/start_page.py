import gettext
from typing import List

from gi.repository import Gtk, Adw

from kilowatt.model.metering import Meter
from kilowatt.util.ui import ui_path
from kilowatt.view.meter_button import MeterButton

_ = gettext.gettext


@Gtk.Template(filename=ui_path("start_page.ui"))
class StartPage(Adw.NavigationPage):
    __gtype_name__ = "StartPage"

    meters_box: Gtk.Label = Gtk.Template.Child("metersBox")

    def __init__(self):
        Adw.NavigationPage.__init__(self)

    def update_meters(self, meters: List[Meter]):
        for meter in meters:
            button = MeterButton(meter)
            self.meters_box.append(button)

