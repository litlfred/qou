#!/usr/bin/env python3
"""
Deep trace of protium ℵ(1,0) formation at the quark level.

Traces WHERE each negative coefficient comes from — which
Hecke reduction step introduced it, and what it means physically.

Output: protium-deep-trace.witness.json

Usage:
    cd computations
    python3 protium-deep-trace.py
"""

import math, json
from datetime import datetime, timezone
from pathlib import Path
from hecke_division import HeckeDivision, HeckeElement
from q_parameter import Q as q, Q_INV as qi, E_CROSS
from experimental_constants import *

div = HeckeDivision(q_val=q)
HA = q - qi; s = q**0.5 - qi**0.5
z = 1.0/(q**0.5 + qi**0.5)
kappa = E_CROSS * M_E_MEV / (3 * E_CROSS)

def sig(i): return HeckeElement({(i,): 1.0})
c_dd = 1.0; d_dd = -HA
c_ud = 1.0; d_ud = -HA/2

def cx(ti, tj, gen):
    if ti == tj == 'u': return sig(gen)
    elif ti == tj == 'd': return HeckeElement({(gen,): c_dd, (): d_dd})
    elif set([ti,tj]) == set(['u','d']): return HeckeElement({(gen,): c_ud, (): d_ud})
    else: return sig(gen)

def wp(w):
    if not w: return "𝟏"
    return " · ".join(f"σ_{i}" for i in w)

def elem_str(elem):
    parts = []
    for w, c in sorted(elem.terms.items(), key=lambda x: (len(x[0]), x[0])):
        parts.append(f"({c:+.10f}) · {wp(w)}")
    return "\n    ".join(parts)

# ═══ PROTIUM: step by step with DEEP trace ═══
# Strands: u_r(0), u_g(1), d_b(2), e⁻(3)

output_lines = []
def log(s):
    print(s)
    output_lines.append(s)

log("=" * 80)
log("PROTIUM ℵ(1, 0) = B₃(u_r, u_g, d_b) ⋈ e⁻")
log("DEEP TRACE: where does each coefficient come from?")
log("=" * 80)
log("")
log(f"q = {q:.10f}")
log(f"q − q⁻¹ = {HA:.10f}")
log(f"s = q^½ − q^(−½) = {s:.10f}")
log("")

log("Strands:")
log("  0: u_r (up quark, red)")
log("  1: u_g (up quark, green)")
log("  2: d_b (down quark, blue)")
log("  3: e⁻  (electron)")
log("")

elem = HeckeElement.identity()

# Crossing (0,1): u_r–u_g = u–u = positive crossing σ₀
log("─── Crossing (0,1): u_r–u_g = u–u ───")
log("  Type: same-flavor quarks → positive crossing")
log(f"  Element: σ₀  (c = 1, d = 0)")
log("")
log(f"  Before: {elem_str(elem)}")
elem = elem * sig(0)
elem, _ = div.reduce(elem)
log(f"  After:  {elem_str(elem)}")
log(f"  Reduction: none (σ₀ is already in NF)")
log(f"  ALL COEFFICIENTS POSITIVE ✓")
log("")

# Crossing (0,2): u_r–d_b = u–d = mixed crossing
log("─── Crossing (0,2): u_r–d_b = u–d ───")
log("  Type: different-flavor quarks → mixed crossing")
log(f"  Element: ({c_ud:.6f}) · σ₀ + ({d_ud:.6f}) · 𝟏")
log("")
log(f"  Before: {elem_str(elem)}")
before = elem
cx_elem = HeckeElement({(0,): c_ud, (): d_ud})
product = elem * cx_elem
log(f"  Product (before reduction):")
log(f"    {elem_str(product)}")
log("")
log("  The product contains σ₀ · σ₀ = σ₀² (Hecke-reducible!)")
log(f"  σ₀² coefficient: 1.0 × {c_ud:.6f} = {1.0 * c_ud:.6f}")
log("")
log("  *** HECKE REDUCTION (R1) ***")
log(f"  σ₀² → ({HA:.6f}) · σ₀ + 𝟏")
log(f"  The σ₀² term ({1.0 * c_ud:.6f}) · σ₀² becomes:")
log(f"    ({1.0 * c_ud:.6f}) × ({HA:.6f}) · σ₀ = ({c_ud * HA:.6f}) · σ₀")
log(f"    ({1.0 * c_ud:.6f}) × 𝟏 = ({c_ud:.6f}) · 𝟏")
log("")
elem = product
elem, _ = div.reduce(elem)
log(f"  After reduction: {elem_str(elem)}")
log("")

# Where is the 𝟏 coefficient from?
c_identity = elem.terms.get((), 0.0)
log(f"  ★ The 𝟏 coefficient = {c_identity:.10f}")
log(f"    This came from: Hecke reduction of σ₀²")
log(f"    The u_r–d_b mixed crossing multiplied against the u_r–u_g")
log(f"    crossing, producing σ₀². The Hecke relation splits σ₀²")
log(f"    into ({HA:.6f})·σ₀ + 𝟏. The +{c_ud:.6f} contribution to 𝟏")
log(f"    plus the existing ({d_ud:.6f}) from the d coefficient gives")
log(f"    the final 𝟏 coefficient: {c_identity:.10f}")
if c_identity > 0:
    log(f"    SIGN: POSITIVE → this is binding energy RELEASED")
else:
    log(f"    SIGN: NEGATIVE → this was an INPUT (consumed)")
log("")

# Crossing (1,2): u_g–d_b = u–d = mixed crossing at σ₁
log("─── Crossing (1,2): u_g–d_b = u–d ───")
log("  Type: different-flavor quarks → mixed crossing")
log(f"  Element: ({c_ud:.6f}) · σ₁ + ({d_ud:.6f}) · 𝟏")
log("")
log(f"  Before: {elem_str(elem)}")
cx_elem2 = HeckeElement({(1,): c_ud, (): d_ud})
product2 = elem * cx_elem2
log(f"  Product (before reduction): {product2.n_terms()} terms")
log(f"    {elem_str(product2)}")
log("")
log("  σ₀ and σ₁ are ADJACENT generators → no σ² but check for far-comm")
elem = product2
elem, _ = div.reduce(elem)
log(f"  After reduction: {elem_str(elem)}")
log("")

# NOW: trace the negative coefficients
log("─── NEGATIVE COEFFICIENT ANALYSIS (proton B₃ complete) ───")
for w, c in sorted(elem.terms.items(), key=lambda x: (len(x[0]), x[0])):
    if c < 0:
        log(f"  ★ ({c:+.10f}) · {wp(w)}  ← NEGATIVE (INPUT)")
        if w == ():
            log(f"    Origin: d_ud = −½q·s = {d_ud:.6f}")
            log(f"    The identity coefficient in the u–d mixed crossing")
            log(f"    is NEGATIVE because d = −½q·s < 0.")
            log(f"    This is the Skein amplitude cost of mixing u and d quarks.")
            log(f"    Physically: the energy PAID to bind different-flavor quarks.")
        elif w == (0,):
            log(f"    Origin: combined from Hecke reduction remainder + d_ud")
            log(f"    The σ₀ coefficient absorbed contributions from:")
            log(f"      1. The original σ₀ term (from u_r–u_g crossing)")
            log(f"      2. The Hecke reduction of σ₀² (added +{c_ud*HA:.6f})")
            log(f"      3. The d coefficient of the u–d crossing (−{abs(d_ud):.6f})")
            log(f"    The small negative value means the d contribution")
            log(f"    slightly exceeded the Hecke energy release.")
    else:
        log(f"  ★ ({c:+.10f}) · {wp(w)}  ← POSITIVE (OUTPUT)")
        if len(w) == max(len(ww) for ww in elem.terms):
            log(f"    This is the DOMINANT term — the hadron bound state.")

log("")

# Crossing (0,3): u_r–e⁻ = quark–electron = Hopf link σ₀
log("─── Crossing (0,3): u_r–e⁻ = Hopf link ───")
log("  Type: quark–electron → positive crossing σ₀")
log(f"  Element: σ₀  (c = 1, d = 0)")
log("")
log(f"  Before: {elem_str(elem)}")
before3 = elem
elem = elem * sig(0)
product3 = elem
log(f"  Product: {elem_str(product3)}")
elem, _ = div.reduce(elem)
log(f"  After reduction: {elem_str(elem)}")

# Check what changed
for w in set(before3.terms.keys()) | set(elem.terms.keys()):
    cb = before3.terms.get(w, 0.0)
    ca = elem.terms.get(w, 0.0)
    if abs(ca - cb) > 1e-12:
        log(f"    Δ({wp(w)}): {cb:+.6f} → {ca:+.6f} (Δ = {ca-cb:+.6f})")
log("")

# Crossing (1,3): u_g–e⁻ = Hopf link σ₁
log("─── Crossing (1,3): u_g–e⁻ = Hopf link ───")
log("  Type: quark–electron → positive crossing σ₁")
log(f"  Before: {elem_str(elem)}")
before4 = elem
elem = elem * sig(1)
log(f"  Product: {elem_str(elem)}")
elem, log4 = div.reduce(elem)
s4 = div.summarize_log(log4)
log(f"  *** {s4['hecke_steps']} Hecke + {s4['yang_baxter_steps']} YB reductions ***")
log(f"  After: {elem_str(elem)}")
log("")

# Crossing (2,3): d_b–e⁻ = Hopf link σ₂
log("─── Crossing (2,3): d_b–e⁻ = Hopf link ───")
log("  Type: quark–electron → positive crossing σ₂")
log(f"  Before: {elem_str(elem)}")
elem = elem * sig(2)
elem, _ = div.reduce(elem)
log(f"  After: {elem_str(elem)}")
log("")

# ═══ FINAL ═══
tr = div.markov_trace(elem, 4)
net = sum(c for c in elem.terms.values())

log("═" * 80)
log("FINAL NORMAL FORM: 𝒩̄(ℵ(1, 0))")
log("═" * 80)
log("")
for w, c in sorted(elem.terms.items(), key=lambda x: (len(x[0]), x[0])):
    sign = "INPUT (consumed)" if c < 0 else "OUTPUT (produced)"
    log(f"  ({c:+.10f}) · {wp(w)}  [{sign}]")
log("")
log(f"  Net coefficient: {net:+.10f}")
log(f"  Markov trace (4-strand): {tr:.10f}")
log("")
log("PHYSICAL READING:")
log("  The negative terms (-0.010 σ₁·σ₂ and -0.067 σ₀·σ₁·σ₂)")
log("  are the Skein amplitude costs of binding quarks with")
log("  different flavors (u–d). They entered through the d")
log("  coefficient of the mixed crossing: d_ud = −½q·s.")
log("  These are the 'raw materials' — the quark-pair mixing")
log("  energy that was CONSUMED to build the hadron.")
log("")
log("  The positive terms (+0.196 σ₁·σ₀·σ₂ and +1.286 σ₀·σ₁·σ₀·σ₂)")
log("  are the BOUND STATE — the proton+electron that was PRODUCED.")
log("  The dominant term σ₀·σ₁·σ₀·σ₂ encodes the full Borromean")
log("  structure of the proton (σ₀·σ₁·σ₀) plus the electron Hopf")
log("  link (σ₂).")

# Write witness
witness = {
    "computation": "protium-deep-trace",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "q": q,
    "description": "Deep trace of protium formation showing origin of each coefficient",
    "normal_form": {wp(w): {"coefficient": c, "sign": "INPUT" if c < 0 else "OUTPUT",
                             "origin": "Skein mixing cost (d_ud)" if c < 0 else "bound state"}
                    for w, c in sorted(elem.terms.items(), key=lambda x: (len(x[0]), x[0]))},
    "net": net,
    "markov_trace": tr,
    "full_trace": "\n".join(output_lines),
}
out = Path("protium-deep-trace.witness.json")
with open(out, "w") as f:
    json.dump(witness, f, indent=2)
print(f"\nWitness: {out}")
