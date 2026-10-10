#!/usr/bin/env python3
"""
T_{3,5} beta decay — correct braid concatenation + Gröbner--Shirshov reduction.

The T_{3,5} braid is APPENDED to the end of the parent nuclear braid,
then the full word is reduced via Gröbner--Shirshov basis. The ENERGY of the
reduction (Hecke steps only) gives the transition physics.

Correct procedure:
  1. Build parent braid word (concatenation of all crossings)
  2. Append T_{3,5} = (σ₃σ₄)⁵ at the END
  3. Reduce via Gröbner--Shirshov basis, logging every step
  4. Energy of Hecke steps = transition energy

The Gröbner-Shirshov energy theorem:
  - Only Hecke steps (σ² = (q-q⁻¹)σ + 1) change energy
  - Yang-Baxter and far-commutativity are energy-preserving
  - Total energy is path-independent (diamond lemma)

Usage:
    cd computations
    python3 t35-braid-concatenation.py
"""

import json
import math
from datetime import datetime, timezone
from pathlib import Path

from q_parameter import (Q as q, Q_INV as qi, S_SKEIN as s,
                         E_CROSS, HBAR_Q_SQ)
from hecke_division import HeckeDivision, HeckeElement

div = HeckeDivision(q_val=q)

print(f"T_{{3,5}} beta decay — braid concatenation + Gröbner--Shirshov reduction")
print(f"q = {q:.10f}")
print()

# ═══════════════════════════════════════════════════════════════════
# Helper: build braid word as raw concatenation (no intermediate reduction)
# ═══════════════════════════════════════════════════════════════════

def build_raw_braid(quark_types):
    """Build unreduced braid word from quark types.
    Returns HeckeElement with a single term (the full braid word)."""
    n = len(quark_types)
    elem = HeckeElement.identity()
    for i in range(n):
        for j in range(i + 1, n):
            qi, qj = quark_types[i], quark_types[j]
            if qi == 'u' and qj == 'u':
                cx = div.crossing_positive(i)
            elif qi == 'd' and qj == 'd':
                cx = div.crossing_negative(i)
            else:
                cx = div.crossing_mixed(i)
            elem = elem * cx
    return elem

# ═══════════════════════════════════════════════════════════════════
# DECAY 1: Free neutron β⁻ (n → p + e⁻ + ν̄)
# ═══════════════════════════════════════════════════════════════════

print("=" * 70)
print("DECAY 1: Free neutron (3 quark strands)")
print("=" * 70)

# Neutron: B₃(u, d, d) — strands 0, 1, 2
neutron_quarks = ['u', 'd', 'd']
# Proton: B₃(u, u, d)
proton_quarks = ['u', 'u', 'd']

# Build raw braid words
neutron_raw = build_raw_braid(neutron_quarks)
proton_raw = build_raw_braid(proton_quarks)

# Build T_{3,5} = (σ₀σ₁)⁵ on strands 0,1,2
t35_3strand = HeckeElement.identity()
for _ in range(5):
    t35_3strand = t35_3strand * div.crossing_positive(0) * div.crossing_positive(1)

# CORRECT: append T_{3,5} to END of neutron braid
neutron_t35_raw = neutron_raw * t35_3strand

print(f"\nNeutron raw: {neutron_raw.n_terms()} terms, max length {neutron_raw.max_word_length()}")
print(f"T_{{3,5}}: 1 term, length 10")
print(f"Neutron · T_{{3,5}} raw: {neutron_t35_raw.n_terms()} terms, max length {neutron_t35_raw.max_word_length()}")

# Reduce each, logging energy
print(f"\n--- Reducing neutron ---")
neutron_red, neutron_log = div.reduce(neutron_raw)
neutron_summary = div.summarize_log(neutron_log)
neutron_trace = div.markov_trace(neutron_red, 3)
print(f"  {neutron_red.n_terms()} terms, {neutron_summary['hecke_steps']} Hecke steps")
print(f"  Hecke energy: {neutron_summary['hecke_energy_change']:.10f}")
print(f"  Trace: {neutron_trace:.10f}")

print(f"\n--- Reducing proton ---")
proton_red, proton_log = div.reduce(proton_raw)
proton_summary = div.summarize_log(proton_log)
proton_trace = div.markov_trace(proton_red, 3)
print(f"  {proton_red.n_terms()} terms, {proton_summary['hecke_steps']} Hecke steps")
print(f"  Hecke energy: {proton_summary['hecke_energy_change']:.10f}")
print(f"  Trace: {proton_trace:.10f}")

print(f"\n--- Reducing neutron · T_{{3,5}} ---")
nt35_red, nt35_log = div.reduce(neutron_t35_raw)
nt35_summary = div.summarize_log(nt35_log)
nt35_trace = div.markov_trace(nt35_red, 3)
print(f"  {nt35_red.n_terms()} terms, {nt35_summary['hecke_steps']} Hecke steps")
print(f"  Hecke energy: {nt35_summary['hecke_energy_change']:.10f}")
print(f"  YB steps: {nt35_summary['yang_baxter_steps']}")
print(f"  Far-comm steps: {nt35_summary['far_comm_steps']}")
print(f"  Trace: {nt35_trace:.10f}")

# Energy differences
delta_E_t35 = nt35_summary['hecke_energy_change'] - neutron_summary['hecke_energy_change']
delta_E_decay = nt35_summary['hecke_energy_change'] - proton_summary['hecke_energy_change']

print(f"\n  ΔE(T_{{3,5}} insertion) = E(n·T35) - E(n) = {delta_E_t35:.10f}")
print(f"  ΔE(decay total) = E(n·T35) - E(p) = {delta_E_decay:.10f}")
print(f"  ΔE(n→p without T35) = E(n) - E(p) = {neutron_summary['hecke_energy_change'] - proton_summary['hecke_energy_change']:.10f}")

# Show reduced forms
print(f"\n  Neutron reduced:")
for w, c in sorted(neutron_red.terms.items(), key=lambda x: (len(x[0]), x[0])):
    ws = '·'.join(f'σ{i}' for i in w) if w else '1'
    print(f"    {c:+.10f} · {ws}")

print(f"\n  Proton reduced:")
for w, c in sorted(proton_red.terms.items(), key=lambda x: (len(x[0]), x[0])):
    ws = '·'.join(f'σ{i}' for i in w) if w else '1'
    print(f"    {c:+.10f} · {ws}")

print(f"\n  Neutron · T_{{3,5}} reduced:")
for w, c in sorted(nt35_red.terms.items(), key=lambda x: (len(x[0]), x[0])):
    ws = '·'.join(f'σ{i}' for i in w) if w else '1'
    print(f"    {c:+.10f} · {ws}")


# ═══════════════════════════════════════════════════════════════════
# DECAY 2: Tritium β⁻ (³H → ³He + e⁻ + ν̄)
# Level 1: 9 quark strands
# ═══════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("DECAY 2: Tritium (9 quark strands)")
print("=" * 70)

# ³H quarks: proton(u,u,d) + neutron₁(u,d,d) + neutron₂(u,d,d)
tritium_quarks = ['u','u','d', 'u','d','d', 'u','d','d']
# ³He quarks: proton₁(u,u,d) + proton₂(u,u,d) + neutron(u,d,d)
helium3_quarks = ['u','u','d', 'u','u','d', 'u','d','d']

# T_{3,5} at converting nucleon (strands 3,4,5): (σ₃σ₄)⁵
t35_9strand = HeckeElement.identity()
for _ in range(5):
    t35_9strand = t35_9strand * div.crossing_positive(3) * div.crossing_positive(4)

# Build raw braids
print(f"\nBuilding raw braid words...")
tritium_raw = build_raw_braid(tritium_quarks)
helium3_raw = build_raw_braid(helium3_quarks)
tritium_t35_raw = tritium_raw * t35_9strand

print(f"  ³H raw: {tritium_raw.n_terms()} terms, length {tritium_raw.max_word_length()}")
print(f"  ³He raw: {helium3_raw.n_terms()} terms, length {helium3_raw.max_word_length()}")
print(f"  ³H · T_{{3,5}} raw: {tritium_t35_raw.n_terms()} terms, length {tritium_t35_raw.max_word_length()}")

# Reduce all three
print(f"\n--- Reducing ³H ---")
trit_red, trit_log = div.reduce(tritium_raw)
trit_summary = div.summarize_log(trit_log)
trit_trace = div.markov_trace(trit_red, 9)
print(f"  {trit_red.n_terms()} terms, {trit_summary['hecke_steps']} Hecke steps")
print(f"  Hecke energy: {trit_summary['hecke_energy_change']:.10f}")
print(f"  Trace: {trit_trace:.10f}")

print(f"\n--- Reducing ³He ---")
he3_red, he3_log = div.reduce(helium3_raw)
he3_summary = div.summarize_log(he3_log)
he3_trace = div.markov_trace(he3_red, 9)
print(f"  {he3_red.n_terms()} terms, {he3_summary['hecke_steps']} Hecke steps")
print(f"  Hecke energy: {he3_summary['hecke_energy_change']:.10f}")
print(f"  Trace: {he3_trace:.10f}")

print(f"\n--- Reducing ³H · T_{{3,5}} ---")
trit_t35_red, trit_t35_log = div.reduce(tritium_t35_raw)
trit_t35_summary = div.summarize_log(trit_t35_log)
trit_t35_trace = div.markov_trace(trit_t35_red, 9)
print(f"  {trit_t35_red.n_terms()} terms, {trit_t35_summary['hecke_steps']} Hecke steps")
print(f"  Hecke energy: {trit_t35_summary['hecke_energy_change']:.10f}")
print(f"  YB: {trit_t35_summary['yang_baxter_steps']}, far-comm: {trit_t35_summary['far_comm_steps']}")
print(f"  Trace: {trit_t35_trace:.10f}")

# Energy analysis
delta_E_t35_trit = trit_t35_summary['hecke_energy_change'] - trit_summary['hecke_energy_change']
delta_E_trit_he3 = trit_summary['hecke_energy_change'] - he3_summary['hecke_energy_change']
delta_E_full = trit_t35_summary['hecke_energy_change'] - he3_summary['hecke_energy_change']

print(f"\n  ENERGY ANALYSIS (Hecke units):")
print(f"  E(³H)           = {trit_summary['hecke_energy_change']:.10f}")
print(f"  E(³He)          = {he3_summary['hecke_energy_change']:.10f}")
print(f"  E(³H · T_{{3,5}}) = {trit_t35_summary['hecke_energy_change']:.10f}")
print(f"  ΔE(³H → ³He) without T35 = {delta_E_trit_he3:.10f}")
print(f"  ΔE(T_{{3,5}} cost)          = {delta_E_t35_trit:.10f}")
print(f"  ΔE(³H·T35 → ³He) total   = {delta_E_full:.10f}")

# Convert to physical units
mu_0 = 0.51100 / (3 * E_CROSS)  # MeV per Hecke unit
ha = q - qi  # q - q⁻¹
energy_per_hecke = ha  # each Hecke step changes energy by |c|·(q-q⁻¹)

print(f"\n  PHYSICAL UNITS:")
print(f"  q - q⁻¹ = {ha:.10f}")
print(f"  μ₀ = {mu_0:.6f} MeV/Skein")
print(f"  ΔE(³H → ³He) = {delta_E_trit_he3 * mu_0:.6f} MeV")
print(f"  ΔE(T_{{3,5}} cost) = {delta_E_t35_trit * mu_0:.6f} MeV")
print(f"  ΔE(total decay) = {delta_E_full * mu_0:.6f} MeV")

# Trace analysis
print(f"\n  TRACE ANALYSIS:")
print(f"  tr(³H)        = {trit_trace:.10f}")
print(f"  tr(³He)       = {he3_trace:.10f}")
print(f"  tr(³H·T35)    = {trit_t35_trace:.10f}")
print(f"  tr(³He)/tr(³H)      = {he3_trace/trit_trace:.10f}")
print(f"  tr(³H·T35)/tr(³H)   = {trit_t35_trace/trit_trace:.10f}")
print(f"  tr(³H·T35)/tr(³He)  = {trit_t35_trace/he3_trace:.10f}")

# Hecke step breakdown for the T_{3,5} reduction
hecke_steps_t35 = [s for s in trit_t35_log if s.relation == 'hecke']
yb_steps_t35 = [s for s in trit_t35_log if s.relation == 'yang-baxter']
fc_steps_t35 = [s for s in trit_t35_log if s.relation == 'far-comm']

print(f"\n  REDUCTION STEP BREAKDOWN (³H · T_{{3,5}}):")
print(f"  Total steps: {len(trit_t35_log)}")
print(f"  Hecke (energy-changing): {len(hecke_steps_t35)}")
print(f"  Yang-Baxter (energy-preserving): {len(yb_steps_t35)}")
print(f"  Far-commutativity (energy-preserving): {len(fc_steps_t35)}")
if hecke_steps_t35:
    print(f"  Avg energy per Hecke step: {sum(s.energy_change for s in hecke_steps_t35)/len(hecke_steps_t35):.10f}")


# ═══════════════════════════════════════════════════════════════════
# WITNESS
# ═══════════════════════════════════════════════════════════════════

witness = {
    "computation": "t35-braid-concatenation",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "description": (
        "T_{3,5} beta decay via correct braid concatenation + Gröbner--Shirshov reduction. "
        "T_{3,5} appended to END of parent braid, then reduced. Energy of Hecke "
        "steps gives transition physics (Gröbner-Shirshov energy theorem)."
    ),
    "parameters": {"q": q, "s": s, "E_cross": E_CROSS, "mu_0_MeV": mu_0},
    "free_neutron": {
        "neutron": {
            "n_terms": neutron_red.n_terms(),
            "hecke_steps": neutron_summary["hecke_steps"],
            "hecke_energy": neutron_summary["hecke_energy_change"],
            "trace": neutron_trace,
        },
        "proton": {
            "n_terms": proton_red.n_terms(),
            "hecke_steps": proton_summary["hecke_steps"],
            "hecke_energy": proton_summary["hecke_energy_change"],
            "trace": proton_trace,
        },
        "neutron_t35": {
            "n_terms": nt35_red.n_terms(),
            "hecke_steps": nt35_summary["hecke_steps"],
            "yb_steps": nt35_summary["yang_baxter_steps"],
            "fc_steps": nt35_summary["far_comm_steps"],
            "hecke_energy": nt35_summary["hecke_energy_change"],
            "trace": nt35_trace,
        },
        "delta_E_t35": delta_E_t35,
        "delta_E_decay": delta_E_decay,
    },
    "tritium": {
        "parent": {
            "n_terms": trit_red.n_terms(),
            "hecke_steps": trit_summary["hecke_steps"],
            "hecke_energy": trit_summary["hecke_energy_change"],
            "trace": trit_trace,
        },
        "daughter": {
            "n_terms": he3_red.n_terms(),
            "hecke_steps": he3_summary["hecke_steps"],
            "hecke_energy": he3_summary["hecke_energy_change"],
            "trace": he3_trace,
        },
        "parent_t35": {
            "n_terms": trit_t35_red.n_terms(),
            "hecke_steps": trit_t35_summary["hecke_steps"],
            "yb_steps": trit_t35_summary["yang_baxter_steps"],
            "fc_steps": trit_t35_summary["far_comm_steps"],
            "hecke_energy": trit_t35_summary["hecke_energy_change"],
            "trace": trit_t35_trace,
        },
        "energy_analysis": {
            "delta_E_parent_daughter": delta_E_trit_he3,
            "delta_E_t35_cost": delta_E_t35_trit,
            "delta_E_total_decay": delta_E_full,
            "delta_E_parent_daughter_MeV": delta_E_trit_he3 * mu_0,
            "delta_E_t35_cost_MeV": delta_E_t35_trit * mu_0,
            "delta_E_total_MeV": delta_E_full * mu_0,
        },
    },
}

out_path = Path(__file__).parent / "t35-braid-concatenation.witness.json"
with open(out_path, "w") as f:
    json.dump(witness, f, indent=2)

print(f"\nWitness written to {out_path}")
