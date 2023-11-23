from .freq import MHz

from dataclasses import dataclass

@dataclass
class FrequencyBand:
    band_no: int
    ul_low:  float
    ul_high: float
    dl_low:  float
    dl_high: float
    duplex:  str
    
table = {
    1: FrequencyBand(1, MHz(1920), MHz(1980), MHz(2110), MHz(2170), "FDD"),
    2: FrequencyBand(2, MHz(1850), MHz(1910), MHz(1930), MHz(1990), "FDD"),
    3: FrequencyBand(3, MHz(1710), MHz(1785), MHz(1805), MHz(1880), "FDD"),
    5: FrequencyBand(5, MHz(824), MHz(849), MHz(869), MHz(894), "FDD"),
    7: FrequencyBand(7, MHz(2500), MHz(2570), MHz(2620), MHz(2690), "FDD"),
    8: FrequencyBand(8, MHz(880), MHz(915), MHz(925), MHz(960), "FDD"),
    12: FrequencyBand(12, MHz(699), MHz(716), MHz(729), MHz(746), "FDD"),
    14: FrequencyBand(14, MHz(788), MHz(798), MHz(758), MHz(768), "FDD"),
    18: FrequencyBand(18, MHz(815), MHz(830), MHz(860), MHz(875), "FDD"),
    20: FrequencyBand(20, MHz(832), MHz(862), MHz(791), MHz(821), "FDD"),
    25: FrequencyBand(25, MHz(1850), MHz(1915), MHz(1930), MHz(1995), "FDD"),
    26: FrequencyBand(26, MHz(814), MHz(849), MHz(859), MHz(894), "FDD"),
    28: FrequencyBand(28, MHz(703), MHz(748), MHz(758), MHz(803), "FDD"),
    29: FrequencyBand(29, None, None, MHz(717), MHz(728), "SDL"),
    30: FrequencyBand(30, MHz(2305), MHz(2315), MHz(2350), MHz(2360), "FDD"),
    34: FrequencyBand(34, MHz(2010), MHz(2025), MHz(2010), MHz(2025), "TDD"),
    38: FrequencyBand(38, MHz(2570), MHz(2620), MHz(2570), MHz(2620), "TDD"),
    39: FrequencyBand(39, MHz(1880), MHz(1920), MHz(1880), MHz(1920), "TDD"),
    40: FrequencyBand(40, MHz(2300), MHz(2400), MHz(2300), MHz(2400), "TDD"),
    41: FrequencyBand(41, MHz(2496), MHz(2690), MHz(2496), MHz(2690), "TDD"),
    48: FrequencyBand(48, MHz(3550), MHz(3700), MHz(3550), MHz(3700), "TDD"),
    50: FrequencyBand(50, MHz(1432), MHz(1517), MHz(1432), MHz(1517), "TDD"),
    51: FrequencyBand(51, MHz(1427), MHz(1432), MHz(1427), MHz(1432), "TDD"),
    53: FrequencyBand(53, MHz(2483.5), MHz(2495), MHz(2483.5), MHz(2495), "TDD"),
    65: FrequencyBand(65, MHz(1920), MHz(2010), MHz(2110), MHz(2200), "FDD"),
    66: FrequencyBand(66, MHz(1710), MHz(1780), MHz(2110), MHz(2200), "FDD"),
    70: FrequencyBand(70, MHz(1695), MHz(1710), MHz(1995), MHz(2020), "FDD"),
    71: FrequencyBand(71, MHz(663), MHz(698), MHz(617), MHz(652), "FDD"),
    74: FrequencyBand(74, MHz(1427), MHz(1470), MHz(1475), MHz(1518), "FDD"),
    75: FrequencyBand(75, None, None, MHz(1432), MHz(1517), "SDL"),
    76: FrequencyBand(76, None, None, MHz(1427), MHz(1432), "SDL"),
    77: FrequencyBand(77, MHz(3300), MHz(4200), MHz(3300), MHz(4200), "TDD"),
    78: FrequencyBand(78, MHz(3300), MHz(3800), MHz(3300), MHz(3800), "TDD"),
    79: FrequencyBand(79, MHz(4400), MHz(5000), MHz(4400), MHz(5000), "TDD"),
    80: FrequencyBand(80, MHz(1710), MHz(1785), None, None, "SUL"),
    81: FrequencyBand(81, MHz(880), MHz(915), None, None, "SUL"),
    82: FrequencyBand(82, MHz(832), MHz(862), None, None, "SUL"),
    83: FrequencyBand(83, MHz(703), MHz(748), None, None, "SUL"),
    84: FrequencyBand(84, MHz(1920), MHz(1980), None, None, "SUL"),
    86: FrequencyBand(86, MHz(1710), MHz(1780), None, None, "SUL"),
    89: FrequencyBand(89, MHz(824), MHz(849), None, None, "SUL"),
    90: FrequencyBand(90, MHz(2496), MHz(2690), MHz(2496), MHz(2690), "TDD"),
    91: FrequencyBand(91, MHz(832), MHz(862), MHz(1427), MHz(1432), "FDD2"),
    92: FrequencyBand(92, MHz(832), MHz(862), MHz(1432), MHz(1517), "FDD2"),
    93: FrequencyBand(93, MHz(880), MHz(915), MHz(1427), MHz(1432), "FDD2"),
    94: FrequencyBand(94, MHz(880), MHz(915), MHz(1432), MHz(1517), "FDD2"),
    95: FrequencyBand(95, MHz(2010), MHz(2025), None, None, "SUL"), # China Only
    257: FrequencyBand(257, MHz(26500), MHz(29500), MHz(26500), MHz(29500), "TDD"),
    258: FrequencyBand(258, MHz(24250), MHz(27500), MHz(24250), MHz(27500), "TDD"),
    259: FrequencyBand(259, MHz(39500), MHz(43500), MHz(39500), MHz(43500), "TDD"),
    260: FrequencyBand(260, MHz(37000), MHz(40000), MHz(37000), MHz(40000), "TDD"),
    261: FrequencyBand(261, MHz(27500), MHz(28350), MHz(27500), MHz(28350), "TDD")
    }
