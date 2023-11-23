
def to_freq(gscn):
    if gscn < 7499:
        Mp = (gscn - 2) % 3 - 1
        M = Mp * 2 + 3
        N = (gscn - Mp) / 3
        return N * 1200000 + M * 50000
    elif gscn < 22256:
        return 3e9 + (gscn - 7499) * 1440e3
    else:
        return 24250080e3 + (gscn - 22256) * 17280e3
        
def from_freq(freq):
    if freq < 3000:
        Mp = freq % 1200000 // 50000 

        if Mp == 1200000 - 50000:
            Mp = -50000

        assert Mp in [-50000, 0, 50000]
        
        freq -= Mp

        assert freq % 1200000 == 0

        N = freq // 12000000

        return 3 * N + Mp

k_PBCH = 120
k_SS = 120

# TS 138 104 Table 5.4.3.3-1
