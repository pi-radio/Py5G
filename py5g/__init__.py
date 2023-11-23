#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# a_{k, l}^{(p, μ)} - Value of resource element
# β - Amplitude scaling
# c(n) PN sequence
# Δf -- SCS -- subcarrier spacing
# Δf_RA -- SCSRA -- Random Access SCS
# κ -- ratio between T_s and T_c -- 64
# k -- Subcarrier index relative to reference
# l -- OFDM symbol index relative to reference
# μ -- Subcarrier spacing 2^μ * 15 kHz ; μ ∈ {0, 4} 
# M_bit^(q) 
#
# 
#
#

# Δf_max -- 480 kHz N_f = 4096
# Δf_ref -- 15 kHz N_{f,ref} = 2048
#

NormalCP=0
ExtendedCP=1

class ChannelConfig:
    def __init__(self, μ, N_RB, CP=NormalCP):
        self.μ = μ
        self.CP = CP
        self.N_RB = N_RB
        
        if CP == ExtendedCP:
            assert self.μ == 2

    @property
    def k_offset(self):
        return 6 if self.N_RB & 1 else 0

    
    @property
    def slots_per_subframe(self):
        return (1 << self.μ)

    @property
    def slots_per_frame(self):
        return self.slots_per_subframe * 10

    @property
    def symbols_per_subframe(self):
        return self.symbols_per_slot * self.slots_per_subframe
    
    @property
    def symbols_per_slot(self):
        return 14 if self.CP == NormalCP else 12
        
class Frame:
    """ Represents 10ms frame """
    def __init__(self, config):
        self.config = config

class Subframe:
    """ Represents 1ms subframe """
    def __init__(self, config):
        self.config = config

    

class ResourceElement:
    def __init__(self, k, l, p, μ):
        self.k = k
        self.l = l
        self.p = p
        self.μ = μ

        
class PRB:
    def __init__(self, num):
        self.num = num
