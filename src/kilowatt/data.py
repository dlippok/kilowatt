from datetime import date

from kilowatt.model.metering import Measurement, Meter


METER_DUMMY = Meter(
    id="000001",
    unit='kWh',
    description="Empty Meter",
    measurements=[]
)

METER_DUMMY_2 = Meter(
    id="000002",
    unit='kWh',
    description="Dummy Meter",
    measurements=[
        Measurement(date=date(2025, 8, 28), value=136021.5),
        Measurement(date=date(2025, 11, 2), value=136056.6),
        Measurement(date=date(2025, 11, 21), value=136067.4)
    ]
)


METERS = [
    METER_DUMMY,
    METER_DUMMY_2
]
