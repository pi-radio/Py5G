from .freq import Freq, Hz, KHz, MHz, GHz
from dataclasses import dataclass

# N_ref_offset, f_ref_offset, delta_f

table = [
    ( 2016667, KHz(24250080), KHz(60) ),
    (  600000, GHz(3),        KHz(15) ),
    (       0, Hz(0),         KHz(5) )
]

def to_freq(arfcn):
    assert arfcn <= 3279165 # Max defined ARFCN
    
    for N_ref, f_ref, delta_f in table:
        if arfcn >= N_ref:
            return f_ref + delta_f * (arfcn - N_ref)
        
def from_freq(f):
    assert f <= GHz(100)

    for N_ref, f_ref, delta_f in table:
        if f >= f_ref:
            return int((f - f_ref) / delta_f)

@dataclass
class BandARFCN:
    band_no: int
    delta_f_raster: int
    ul_arfcn_spacing: int
    ul_Nref_low: int
    ul_Nref_high: int
    dl_arfcn_spacing: int
    dl_Nref_low: int
    dl_Nref_high: int


    
band_list = [
    BandARFCN(1, 100, 20, 384000, 396000, 20, 422000, 434000),
    BandARFCN(2, 100, 20, 370000, 382000, 20, 386000, 398000),
    BandARFCN(3, 100, 20, 342000, 357000, 20, 361000, 376000),
    BandARFCN(5, 100, 20, 164800, 169800, 20, 173800, 178800),
    BandARFCN(7, 100, 20, 500000, 514000, 20, 524000, 538000),
    BandARFCN(8, 100, 20, 176000, 183000, 20, 185000, 192000),
    BandARFCN(12, 100, 20, 139800, 143200, 20, 145800, 149200),
    BandARFCN(14, 100, 20, 157600, 159600, 20, 151600, 153600),
    BandARFCN(18, 100, 20, 163000, 166000, 20, 172000, 175000),
    BandARFCN(20, 100, 20, 166400, 172400, 20, 158200, 164200),
    BandARFCN(25, 100, 20, 370000, 383000, 20, 386000, 399000),
    BandARFCN(26, 100, 20, 162800, 169800, 20, 171800, 178800),
    BandARFCN(28, 100, 20, 140600, 149600, 20, 151600, 160600),
    BandARFCN(29, 100, None, None, None, 20, 143400, 145600),
    BandARFCN(30, 100, 20, 461000, 463000, 20, 470000, 472000),
    BandARFCN(34, 100, 20, 402000, 405000, 20, 402000, 405000),
    BandARFCN(38, 100, 20, 514000, 524000, 20, 514000, 524000),
    BandARFCN(39, 100, 20, 376000, 384000, 20, 376000, 384000),
    BandARFCN(40, 100, 20, 460000, 480000, 20, 460000, 480000),
    BandARFCN(41, 15, 3, 499200, 537999, 3, 499200, 537999),
    BandARFCN(41, 30, 6, 499200, 537996, 6, 499200, 537996),
    BandARFCN(48, 15, 1, 636667, 646666, 1, 636667, 646666),
    BandARFCN(48, 30, 2, 636668, 646666, 2, 636668, 646666),
    BandARFCN(50, 100, 20, 286400, 303400, 20, 286400, 303400),
    BandARFCN(51, 100, 20, 285400, 286400, 20, 285400, 286400),
    BandARFCN(53, 100, 20, 496700, 499000, 20, 496700, 499000),
    BandARFCN(65, 100, 20, 384000, 402000, 20, 422000, 440000),
    BandARFCN(66, 100, 20, 342000, 356000, 20, 422000, 440000),
    BandARFCN(70, 100, 20, 339000, 342000, 20, 399000, 404000),
    BandARFCN(71, 100, 20, 132600, 139600, 20, 123400, 130400),
    BandARFCN(74, 100, 20, 285400, 294000, 20, 295000, 303600),
    BandARFCN(75, 100, None, None, None,  20, 286400, 303400),
    BandARFCN(76, 100, None, None, None,  20, 285400, 286400),
    BandARFCN(77, 15, 1, 620000, 680000, 1, 620000, 680000),
    BandARFCN(77, 30, 2, 620000, 680000, 2, 620000, 680000),
    BandARFCN(78, 15, 1, 620000, 653333, 1, 620000, 653333),
    BandARFCN(78, 30, 2, 620000, 653332, 2, 620000, 653332),
    BandARFCN(79, 15, 1, 693334, 733333, 1, 693334, 733333),
    BandARFCN(79, 30, 2, 693334, 733332, 2, 693334, 733332),
    BandARFCN(80, 100, 20, 342000, 357000, None, None, None),
    BandARFCN(81, 100, 20, 176000, 183000, None, None, None),
    BandARFCN(82, 100, 20, 166400, 172400, None, None, None),
    BandARFCN(83, 100, 20, 140600, 149600, None, None, None),
    BandARFCN(84, 100, 20, 384000, 396000, None, None, None),
    BandARFCN(86, 100, 20, 342000, 356000, None, None, None),
    BandARFCN(89, 100, 20, 164800, 169800, None, None, None),
    BandARFCN(90, 15, 3, 499200, 537999, 3, 499200, 537999),
    BandARFCN(90, 30, 6, 499200, 537996, 6, 499200, 537996),
    BandARFCN(90, 100, 20, 499200, 538000, 20, 499200, 538000),
    BandARFCN(91, 100, 20, 166400, 172400, 20, 285400, 286400),
    BandARFCN(92, 100, 20, 166400, 172400, 20, 286400, 303400),
    BandARFCN(93, 100, 20, 176000, 183000, 20, 285400, 286400),
    BandARFCN(94, 100, 20, 176000, 183000, 20, 286400, 303400),
    BandARFCN(95, 100, 20, 402000, 405000, None, None, None),
    BandARFCN(257, 60, 1, 2054166, 2104165, 1, 2054166, 2104165),
    BandARFCN(257, 120, 2, 2054167, 2104165, 2, 2054167, 2104165),
    BandARFCN(258, 60, 1, 2016667, 2070832, 1, 2016667, 2070832),
    BandARFCN(258, 120, 2, 2016667, 2070831, 2, 2016667, 2070831),
    BandARFCN(259, 60, 1, 2270832, 2337499, 1, 2270832, 2337499),
    BandARFCN(259, 120, 2, 2270832, 2337499, 2, 2270832, 2337499),
    BandARFCN(260, 60, 1, 2229166, 2279165, 1, 2229166, 2279165),
    BandARFCN(260, 120, 2, 2229167, 2279165, 2, 2229167, 2279165),
    BandARFCN(261, 60, 1, 2070833, 2084999, 1, 2070833, 2084999),
    BandARFCN(261, 120, 2, 2070833, 2084999, 2, 2070833, 2084999)
]
    
