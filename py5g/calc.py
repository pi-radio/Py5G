import py5g.arfcn as arfcn
import py5g.bands as bands
from .freq import Freq

import click

@click.group()
def calc():
    pass

@calc.group("info")
def _info():
    pass

@calc.group("find")
def _find():
    pass

@calc.command("arfcn")
@click.option("--freq", 'direction', flag_value="freq", default=True)
@click.option("--arfcn", 'direction', flag_value="arfcn")
@click.argument("arg")
def _arfcn(direction, arg):
    if direction == "freq":
        arg = Freq(arg)
        print(f"ARFCN: {arfcn.from_freq(arg)}")
    elif direction == "arfcn":
        print(f"Freq: {arfcn.to_freq(int(arg))}")

@_info.command("band")
@click.argument("band", type=int)
def info_band(band):
    if band not in bands.table:
        print(f"Band n{band} not defined")
        return 255

    band = bands.table[band]
    
    print(f"Band Info: n{band.band_no}")
    print(f" Duplex: {band.duplex}")

    if band.ul_low is not None:
        print(f" Uplink {band.ul_low}-{band.ul_high}")

    if band.dl_low is not None:
        print(f" Downlink {band.dl_low}-{band.dl_high}")

@_find.command("band")
@click.argument("freq", type=Freq)
def find_band(freq):
    print(freq)
    found = []
    for b in bands.table.values():
        if b.dl_low is not None and b.dl_low <= freq and freq <= b.dl_high:
            found.append(b.band_no)

    for b in found:
        print(f"n{b}")

    if len(found):
        return
        
    closest = -1
    mindist = Freq(1e12)
        
    for b in bands.table.values():
        if b.dl_low is not None:
            dist = min(abs(freq-b.dl_low),  abs(freq-b.dl_high))
            if dist < mindist:
                closest = b.band_no
                mindist = dist

    print(f"Frequency {freq} not in 5G band.  Closest band: n{closest}")
        
if __name__ == "__main__":
    calc()
