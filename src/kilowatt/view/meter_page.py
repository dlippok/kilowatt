import gettext

from gi.repository import Gtk, Adw

from kilowatt.model.metering import Meter
from kilowatt.util.ui import ui_path

_ = gettext.gettext


@Gtk.Template(filename=ui_path("meter_page.ui"))
class MeterPage(Adw.NavigationPage):
    __gtype_name__ = "MeterPage"

    id_label: Gtk.Label = Gtk.Template.Child("idLabel")
    reading_label: Gtk.Label = Gtk.Template.Child("readingLabel")
    reading_date_label: Gtk.Label = Gtk.Template.Child("readingDateLabel")

    def __init__(self, meter: Meter):
        Adw.NavigationPage.__init__(self)
        self.meter = meter
        self.refresh_values()

    def refresh_values(self):
        self.set_title(self.meter.description)
        self.id_label.set_label(self.meter.id)

        if self.meter.measurements:
            last_measurement = self.meter.measurements[-1]
            self.reading_label.set_label(f"{last_measurement.value:.2f} {self.meter.unit}")
            self.reading_date_label.set_label(last_measurement.date.strftime("%x"))
        else:
            self.reading_label.set_label(f"0.00 {self.meter.unit}")
            self.reading_date_label.set_label(_("No reading"))
