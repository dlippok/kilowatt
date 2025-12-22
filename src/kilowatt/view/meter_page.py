import gettext
from typing import List

from gi.repository import Gtk, Adw, GObject

from kilowatt.model.metering import Meter
from kilowatt.util.ui import ui_path
from kilowatt.view.meter_button import MeterButton
from kilowatt.view.meters_box import MetersBox

_ = gettext.gettext


@Gtk.Template(filename=ui_path("meter_page.ui"))
class MeterPage(Adw.NavigationPage):
    __gtype_name__ = "MeterPage"

    meter_label: Gtk.Label = Gtk.Template.Child("meterLabel")

    def __init__(self, meter: Meter):
        Adw.NavigationPage.__init__(self)
        self.meter_label.set_label(meter.id)