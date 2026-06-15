#!/usr/bin/env python3
"""
T_{3,5} weak vertex form factor — witness computation.

Computes the Markov trace of the T_{3,5} braid word (σ₁σ₂)⁵ in H₃(q),
which is the weak vertex form factor W(q) for beta decay.

The T_{3,5} torus knot has 10 crossings and mediates the weak force.
The crossing budget for beta decay:
  3 crossings → electron trefoil T_{2,3}
  0 crossings → neutrino unknot K_{0_1}
  7 crossings → nuclear re-reduction (R2 moves)

Also computes:
  - The single-crossing approximation s² = (q^½ - q^{-½})²
  - The ratio W(q)/s² (correction factor for half-life predictions)
  - The Jones polynomial J(T_{3,5}, q)
  - Reduction log showing how many Hecke steps are needed

Usage:
    cd folio-assistant/computations
    python3 t35-weak-vertex.py

Output:
    t35-weak-vertex.witness.json

No external dependencies beyond Python 3 standard library + hecke_division.py.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import math
from datetime import datetime, timezone
from pathlib import Path

from q_parameter import (Q as q, Q_INV as qi, HBAR_Q as hbar_q,
                         E_CROSS as E_cross, S_SKEIN as s,
                         TWO_Q as two_q)
from hecke_division import HeckeDivision, HeckeElement


# ── Build the T_{3,5} braid word (σ₁σ₂)⁵ ──────────────────────
div = HeckeDivision(q_val=q)

sigma1 = div.crossing_positive(0)  # σ₁ (0-indexed)
sigma2 = div.crossing_positive(1)  # σ₂

# Build (σ₁σ₂)⁵ step by step, reducing at each stage
print("Building T_{3,5} = (σ₁σ₂)⁵ in H₃(q)")
print(f"  q = {q:.10f}")
print()

# Method 1: Build unreduced, then reduce once
braid_word_unreduced = HeckeElement.identity()
for i in range(5):
    braid_word_unreduced = braid_word_unreduced * sigma1 * sigma2

print(f"Unreduced: {braid_word_unreduced.n_terms()} terms, "
      f"max length {braid_word_unreduced.max_word_length()}")

# Reduce via Gröbner--Shirshov basis
reduced, log = div.reduce(braid_word_unreduced)
summary = div.summarize_log(log)

print(f"Reduced: {reduced.n_terms()} terms, "
      f"max length {reduced.max_word_length()}")
print(f"Steps: {summary['total_steps']} "
      f"({summary['hecke_steps']} Hecke, "
      f"{summary['yang_baxter_steps']} YB, "
      f"{summary['far_comm_steps']} far-comm)")
print(f"Energy change: {summary['total_energy_change']:.6f}")
print(f"Word histogram: {reduced.word_histogram()}")
print()

# Show all terms of the reduced element
print("Reduced element terms:")
for word, coeff in sorted(reduced.terms.items(), key=lambda x: (len(x[0]), x[0])):
    w_str = ''.join(f'σ{i+1}' for i in word) if word else '1'
    print(f"  {coeff:+.10f} · {w_str}")
print()

# ── Markov trace ────────────────────────────────────────────────
n_strands = 3  # T_{3,5} lives in B₃
W_q = div.markov_trace(reduced, n_strands)
print(f"Markov trace W(q) = tr_Markov((σ₁σ₂)⁵) = {W_q:.10f}")

# ── Single-crossing approximation ──────────────────────────────
s_squared = s ** 2
print(f"Single-crossing s² = (q^½ - q^{{-½}})² = {s_squared:.10f}")
print(f"Ratio W(q) / s² = {W_q / s_squared:.6f}")
print(f"|W(q)|² = {W_q**2:.10f}")
print(f"|W(q)|² / s⁴ = {W_q**2 / s_squared**2:.6f}")
print()

# ── Also compute for sub-braids (crossing budget verification) ──
# T_{2,3} = (σ₁)³ = σ₁³ in B₂
trefoil_braid = HeckeElement.identity()
for i in range(3):
    trefoil_braid = trefoil_braid * sigma1

trefoil_reduced, _ = div.reduce(trefoil_braid)
W_trefoil = div.markov_trace(trefoil_reduced, 2)
print(f"T_{{2,3}} Markov trace (electron): {W_trefoil:.10f}")

# Unknot has trace 1
W_unknot = 1.0
print(f"K_{{0_1}} Markov trace (neutrino): {W_unknot:.10f}")

# ── Crossing energy from T_{3,5} ───────────────────────────────
# W boson mass: 10 crossings × E_× × μ₀
m_e_MeV = 0.51100
mu_0 = m_e_MeV / (3 * E_cross)
m_W_from_crossings = 10 * E_cross * mu_0
print(f"\nCrossing energy budget:")
print(f"  μ₀ = {mu_0:.4f} MeV/Skein")
print(f"  10 × E_× × μ₀ = {m_W_from_crossings:.4f} MeV (crossing energy of T_{{3,5}})")
print(f"  m_e = 3 × E_× × μ₀ = {3 * E_cross * mu_0:.4f} MeV")
print(f"  Residual: (10-3) × E_× × μ₀ = {7 * E_cross * mu_0:.4f} MeV "
      f"(7 re-reduction crossings)")

# ── Half-life correction factor ─────────────────────────────────
# Current predictions use s² as coupling
# Corrected should use W(q)
# Ratio of decay rates: Γ_corr / Γ_old = |W(q)|² / s⁴
# So half-life ratio: t_corr / t_old = s⁴ / |W(q)|²
rate_correction = W_q**2 / s_squared**2
halflife_correction = 1.0 / rate_correction

print(f"\nHalf-life correction factor:")
print(f"  Rate ratio Γ_new/Γ_old = |W(q)|²/s⁴ = {rate_correction:.6f}")
print(f"  Half-life ratio t_new/t_old = s⁴/|W(q)|² = {halflife_correction:.6f}")
print(f"  This means the corrected half-lives are {halflife_correction:.4f}× the old values")

# ── Apply correction to all 6 nuclei ───────────────────────────
nuclei = [
    {"name": "³H",   "obs_yr": 12.32,  "pred_yr": 13.0,   "corr_yr": 12.4,  "unit": "yr"},
    {"name": "¹⁴C",  "obs_yr": 5730.0, "pred_yr": 6800.0, "corr_yr": 6690.0,"unit": "yr"},
    {"name": "⁶⁰Co", "obs_yr": 5.2714, "pred_yr": 6.2,    "corr_yr": 6.17,  "unit": "yr"},
    {"name": "⁹⁰Sr", "obs_yr": 28.79,  "pred_yr": 32.0,   "corr_yr": 31.9,  "unit": "yr"},
    {"name": "¹³⁷Cs","obs_yr": 30.17,  "pred_yr": 33.0,   "corr_yr": 32.9,  "unit": "yr"},
    {"name": "²¹⁰Bi","obs_yr": 5.012,  "pred_yr": 5.8,    "corr_yr": 5.79,  "unit": "d"},
]

print(f"\nCorrected half-life predictions (with T_{{3,5}} vertex):")
print(f"{'Nucleus':8s} {'Old pred':>10s} {'T35 corr':>10s} {'Obs':>10s} {'Old ratio':>10s} {'New ratio':>10s}")
print("-" * 60)
for nuc in nuclei:
    old_pred = nuc["corr_yr"]  # use the q_eff-corrected values
    new_pred = old_pred * halflife_correction
    old_ratio = old_pred / nuc["obs_yr"]
    new_ratio = new_pred / nuc["obs_yr"]
    u = nuc["unit"]
    nuc["t35_pred"] = new_pred
    nuc["t35_ratio"] = new_ratio
    print(f"{nuc['name']:8s} {old_pred:>8.2f} {u} {new_pred:>8.2f} {u} "
          f"{nuc['obs_yr']:>8.2f} {u} {old_ratio:>10.4f} {new_ratio:>10.4f}")

# ── Assemble witness ─────────────────────────────────────────────
reduced_terms = {}
for word, coeff in sorted(reduced.terms.items(), key=lambda x: (len(x[0]), x[0])):
    w_str = '·'.join(f'σ{i+1}' for i in word) if word else '1'
    reduced_terms[w_str] = coeff

witness = {
    "computation": "t35-weak-vertex",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "description": (
        "T_{3,5} weak vertex form factor W(q) = tr_Markov((σ₁σ₂)⁵) in H₃(q). "
        "The torus knot T_{3,5} with 10 crossings mediates the weak force. "
        "Beta decay inserts T_{3,5} at the converting quark; the 10 crossings "
        "partition into electron (3) + neutrino (0) + re-reduction (7)."
    ),
    "parameters": {
        "q": q,
        "q_inv": qi,
        "s_skein": s,
        "s_squared": s_squared,
        "z_markov": div.z_markov,
        "n_strands": n_strands,
    },
    "t35_braid": {
        "word": "(σ₁σ₂)⁵",
        "crossings": 10,
        "genus": 4,
        "knot_group": "⟨x,y | x³ = y⁵⟩",
    },
    "reduction": {
        "unreduced_terms": braid_word_unreduced.n_terms(),
        "reduced_terms": reduced.n_terms(),
        "max_word_length": reduced.max_word_length(),
        "hecke_steps": summary["hecke_steps"],
        "yang_baxter_steps": summary["yang_baxter_steps"],
        "far_comm_steps": summary["far_comm_steps"],
        "total_energy_change": summary["total_energy_change"],
        "word_histogram": reduced.word_histogram(),
    },
    "reduced_element": reduced_terms,
    "weak_vertex_form_factor": {
        "W_q": W_q,
        "W_q_squared": W_q ** 2,
        "s_squared": s_squared,
        "s_fourth": s_squared ** 2,
        "ratio_W_over_s2": W_q / s_squared,
        "ratio_W2_over_s4": W_q ** 2 / s_squared ** 2,
    },
    "crossing_budget": {
        "total": 10,
        "electron_T23": 3,
        "neutrino_K01": 0,
        "re_reduction": 7,
        "trefoil_markov_trace": W_trefoil,
        "unknot_markov_trace": W_unknot,
    },
    "halflife_correction": {
        "rate_ratio": rate_correction,
        "halflife_ratio": halflife_correction,
        "description": (
            "Half-life correction from replacing s² with W(q) as weak coupling. "
            "t_new = t_old × (s⁴/|W(q)|²)."
        ),
    },
    "corrected_predictions": [
        {
            "name": nuc["name"],
            "old_corr": nuc["corr_yr"],
            "t35_pred": nuc["t35_pred"],
            "observed": nuc["obs_yr"],
            "unit": nuc["unit"],
            "old_ratio": nuc["corr_yr"] / nuc["obs_yr"],
            "new_ratio": nuc["t35_ratio"],
        }
        for nuc in nuclei
    ],
}

# ── Write witness ────────────────────────────────────────────────
out_path = Path(__file__).parent / "t35-weak-vertex.witness.json"
with open(out_path, "w") as f:
    json.dump(witness, f, indent=2)

print(f"\nWitness written to {out_path}")
