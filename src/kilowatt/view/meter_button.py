import gettext

from gi.repository import Gtk

from kilowatt.model.metering import Meter
from kilowatt.util.ui import ui_path

_ = gettext.gettext


@Gtk.Template(filename=ui_path("meter_button.ui"))
class MeterButton(Gtk.Button):
    __gtype_name__ = "MeterButton"

    description_label: Gtk.Label = Gtk.Template.Child("descriptionLabel")
    reading_label: Gtk.Label = Gtk.Template.Child("readingLabel")
    id_label: Gtk.Label = Gtk.Template.Child("idLabel")
    reading_date_label: Gtk.Label = Gtk.Template.Child("readingDateLabel")

    def __init__(self, meter: Meter):
        Gtk.Button.__init__(self)
        self.meter = meter
        self.description_label.set_label(self.meter.description)
        self.id_label.set_label(self.meter.id)
        self.update_reading()

    def update_reading(self):
        if self.meter.measurements:
            last_measurement = self.meter.measurements[-1]
            self.reading_label.set_label(f"{last_measurement.value:.2f} {self.meter.unit}")
            self.reading_date_label.set_label(last_measurement.date.strftime("%x"))
        else:
            self.reading_label.set_label(f"0.00 {self.meter.unit}")
            self.reading_date_label.set_label(_("No reading"))



