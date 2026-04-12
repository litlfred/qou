#!/usr/bin/env python3
"""
Actual Gröbner--Shirshov basis computation for beta decay.

Start with parent normal form, insert T_{3,5} weak vertex,
reduce through ideal I = {Hecke, YB, far-comm}, track energy.

This is NOT the transfer matrix ansatz — it's the full
division algorithm applied to the composed braid word.

Usage:
    python3 groebner-beta-decay.py
"""

import math
from hecke_division import HeckeDivision, HeckeElement
from q_parameter import Q as q, Q_INV as qi, E_CROSS
from experimental_constants import *

div = HeckeDivision(q_val=q)
HA = q - qi
Z_m = 1.0 / (q**0.5 + qi**0.5)
mu_0 = M_E_MEV / (3 * E_CROSS)
kappa = E_CROSS * mu_0

def sigma(i): return HeckeElement({(i,): 1.0})
def sigma_inv(i): return HeckeElement({(i,): 1.0, (): -HA})

# Skein-weighted crossing elements
c_pp, d_pp = 1.0, 0.0
c_nn, d_nn = 1.0, -HA
c_mix, d_mix = 1.0, -HA / 2

def crossing_element(ti, tj, gen):
    """Hecke element for crossing between types ti, tj at generator gen."""
    if ti == 'u' and tj == 'u':
        return sigma(gen)  # positive
    elif ti == 'd' and tj == 'd':
        return HeckeElement({(gen,): c_nn, (): d_nn})  # negative
    else:
        return HeckeElement({(gen,): c_mix, (): d_mix})  # mixed

def build_borromean(quarks):
    """Build Borromean triplet normal form in H_3(q).
    quarks: list of 3 quark flavours, e.g. ['u','u','d'] for proton.
    """
    elem = HeckeElement.identity()
    hecke_total = 0.0

    # Crossing (0,1) at gen 0
    cx01 = crossing_element(quarks[0], quarks[1], 0)
    elem = elem * cx01
    elem, log01 = div.reduce(elem)
    hecke_total += div.summarize_log(log01).get('hecke_energy_change', 0)

    # Crossing (0,2) at gen 0
    cx02 = crossing_element(quarks[0], quarks[2], 0)
    elem = elem * cx02
    elem, log02 = div.reduce(elem)
    hecke_total += div.summarize_log(log02).get('hecke_energy_change', 0)

    # Crossing (1,2) at gen 1
    cx12 = crossing_element(quarks[1], quarks[2], 1)
    elem = elem * cx12
    elem, log12 = div.reduce(elem)
    hecke_total += div.summarize_log(log12).get('hecke_energy_change', 0)

    return elem, hecke_total


# T_{3,5} weak vertex
T35 = HeckeElement.identity()
for _ in range(5):
    T35 = T35 * sigma(0) * sigma(1)
T35, log_T35 = div.reduce(T35)
sum_T35 = div.summarize_log(log_T35)
tr_T35 = div.markov_trace(T35, 3)


# ══════════════════════════════════════════════════════════════
# COMPUTATIONS
# ══════════════════════════════════════════════════════════════

print("=" * 80)
print("GRÖBNER BASIS BETA DECAY COMPUTATION")
print("=" * 80)
print(f"q = {q:.10f}, HA = {HA:.10f}")
print()

# Build particles
neutron, E_neutron = build_borromean(['u', 'd', 'd'])
proton, E_proton = build_borromean(['u', 'u', 'd'])
electron, E_electron = build_borromean(['u', 'u', 'u'])  # electron = trefoil T_{2,3}...
# Actually electron is T_{2,3} = sigma^3 in H_2(q), not a Borromean.
# Let me build it directly:
electron = sigma(0) * sigma(0) * sigma(0)
electron, log_e = div.reduce(electron)
E_electron = div.summarize_log(log_e).get('hecke_energy_change', 0)

tr_neutron = div.markov_trace(neutron, 3)
tr_proton = div.markov_trace(proton, 3)
tr_electron = div.markov_trace(electron, 2)  # 2-strand for T_{2,3}

print("PARTICLE NORMAL FORMS:")
print()
for name, elem, n_strands, E in [
    ("Neutron B_3(u,d,d)", neutron, 3, E_neutron),
    ("Proton B_3(u,u,d)", proton, 3, E_proton),
]:
    tr_val = div.markov_trace(elem, n_strands)
    print(f"  {name}:")
    print(f"    {elem.n_terms()} terms, Hecke energy = {E:.6f}")
    for w, c in sorted(elem.terms.items(), key=lambda x: (len(x[0]), x[0])):
        ws = '.'.join(f's{i}' for i in w) if w else '1'
        print(f"    {c:+.10f} * {ws}")
    print(f"    Markov trace = {tr_val:.10f}")
    print(f"    ln|tr| = {math.log(abs(tr_val)):.10f}")
    print()

print(f"  T_{{3,5}} weak vertex: {T35.n_terms()} terms")
print(f"    {sum_T35['hecke_steps']} Hecke, {sum_T35['yang_baxter_steps']} YB")
print(f"    Markov trace W(q) = {tr_T35:.10f}")
print()

# Beta decay: neutron × T_{3,5}
print("=" * 80)
print("BETA DECAY: neutron × T_{3,5}")
print("=" * 80)
print()

decay = neutron * T35
decay, log_decay = div.reduce(decay)
sum_decay = div.summarize_log(log_decay)
tr_decay = div.markov_trace(decay, 3)

print(f"  N_n × T_{{3,5}} reduced: {decay.n_terms()} terms")
print(f"    {sum_decay['hecke_steps']} Hecke, {sum_decay['yang_baxter_steps']} YB")
print(f"    Hecke energy of reduction: {sum_decay.get('hecke_energy_change', 'N/A')}")
print(f"    Markov trace: {tr_decay:.10f}")
print()

for w, c in sorted(decay.terms.items(), key=lambda x: (len(x[0]), x[0])):
    ws = '.'.join(f's{i}' for i in w) if w else '1'
    print(f"    {c:+.10f} * {ws}")

print()
print("  COMPARISON:")
print(f"    ln|tr(neutron)| = {math.log(abs(tr_neutron)):.10f}")
print(f"    ln|tr(proton)|  = {math.log(abs(tr_proton)):.10f}")
print(f"    ln|tr(T35)|     = {math.log(abs(tr_T35)):.10f}")
print(f"    ln|tr(n×T35)|   = {math.log(abs(tr_decay)):.10f}")
print()
print(f"    ln|tr(n)| - ln|tr(p)| = {math.log(abs(tr_neutron)) - math.log(abs(tr_proton)):.10f}")
print(f"    Q = |diff| × κ = {abs(math.log(abs(tr_neutron)) - math.log(abs(tr_proton))) * kappa:.6f} MeV")
print(f"    Q_exp (free neutron) ≈ 0.782 MeV")
print()

# Also try: T_{3,5} × neutron (other order)
decay2 = T35 * neutron
decay2, log_d2 = div.reduce(decay2)
tr_d2 = div.markov_trace(decay2, 3)
sum_d2 = div.summarize_log(log_d2)
print(f"  T_{{3,5}} × N_n: {decay2.n_terms()} terms, "
      f"{sum_d2['hecke_steps']} Hecke, {sum_d2['yang_baxter_steps']} YB")
print(f"    Markov trace: {tr_d2:.10f}")
print(f"    Hecke energy: {sum_d2.get('hecke_energy_change', 'N/A')}")
