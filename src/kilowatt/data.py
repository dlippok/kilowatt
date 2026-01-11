from datetime import date

from kilowatt.model.metering import Measurement, Meter

METER_STROM_EG = Meter(
    id="226254",
    unit='kWh',
    description="Strom EG",
    measurements=[
        Measurement(date=date(2025, 7, 27), value=136814.8),
        Measurement(date=date(2025, 8, 28), value=136954.8),
        Measurement(date=date(2025, 9, 7), value=137042.8),
        Measurement(date=date(2025, 11, 2), value=137583.0),
        Measurement(date=date(2025, 11, 21), value=137825.4)
    ]
)

METER_GAS_EG =  Meter(
    id="0020963",
    unit='m³',
    description="Gas EG",
    measurements=[
        Measurement(date=date(2025, 8, 28), value=23057.681),
        Measurement(date=date(2025, 9, 7), value=23057.685),
        Measurement(date=date(2025, 11, 2), value=23276.768),
        Measurement(date=date(2025, 11, 21), value=23399.148)
    ]
)

METER_WASSER_EG = Meter(
    id="7099934",
    unit='m³',
    description="Wasser EG",
    measurements=[
        Measurement(date=date(2025, 8, 28), value=159.65),
        Measurement(date=date(2025, 9, 7), value=163.198),
        Measurement(date=date(2025, 11, 2), value=184.93),
        Measurement(date=date(2025, 11, 21), value=192.784)
    ]
)

METER_STROM_OG = Meter(
    id="225875",
    unit='kWh',
    description="Strom OG",
    measurements=[
        Measurement(date=date(2025, 8, 28), value=136021.5),
        Measurement(date=date(2025, 11, 2), value=136056.6),
        Measurement(date=date(2025, 11, 21), value=136067.4)
    ]
)

METER_GAS_OG = Meter(
    id="10036318",
    unit='m³',
    description="Gas OG",
    measurements=[
        Measurement(date=date(2025, 8, 28), value=18676.674),
        Measurement(date=date(2025, 11, 2), value=18712.562),
        Measurement(date=date(2025, 11, 21), value=18786.796)
    ]
)

METER_WASSER_OG = Meter(
    id="7035671",
    unit='m³',
    description="Wasser OG",
    measurements=[
        Measurement(date=date(2025, 8, 28), value=265.5),
        Measurement(date=date(2025, 11, 2), value=265.77),
        Measurement(date=date(2025, 11, 21), value=265.77)
    ]
)

METER_STROM_KELLER = Meter(
    id="1EBZ0100186158",
    unit='kWh',
    description="Strom Keller",
    measurements=[
        Measurement(date=date(2025, 8, 28), value=356),
        Measurement(date=date(2025, 9, 7), value=368),
        Measurement(date=date(2025, 11, 2), value=494),
        Measurement(date=date(2025, 11, 21), value=519)
    ]
)

METERS = [
    METER_STROM_EG,
    METER_GAS_EG,
    METER_WASSER_EG,
    METER_STROM_OG,
    METER_GAS_OG,
    METER_WASSER_OG,
    METER_STROM_KELLER,
]
