from dataclasses import dataclass
from typing import List


@dataclass
class ShipParams:
    """The vital params of a ship"""
    # Meta params
    tier: int

    # Hull params
    health: int
    concealment: List[float]  # [surface, air]

    speed: float
    turningRadius: float
    rudderShift: float

    # Main battery params
    gunReload: float
    gunTraverse: float
    gunRange: float

    shellAlpha: List[int]  # [HE, AP, SAP]
    shellVelocity: List[float]  # [HE, AP, SAP]

    fireChance: float

    # Torpedoes Params
    torpRange: float
    torpSpeed: float
    torpAlpha: int
    torpTraverse: float
