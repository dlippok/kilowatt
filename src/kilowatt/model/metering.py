from dataclasses import field, dataclass
from datetime import date
from typing import List, Optional, Dict, DefaultDict


@dataclass
class Measurement:
    date: date
    value: float


@dataclass
class Meter:
    id: str
    unit: str
    description: str
    measurements: List[Measurement] = field(default_factory=lambda: [])
