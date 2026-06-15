#!/usr/bin/env python3
"""
BW-Lagrangian prefactor derivation attempt from (m_e, q_0) alone.

Goal: derive λ_V, λ_S, λ_C, λ_Pauli, λ_pair (categorical-Bethe-
Weizsäcker constants) from the 3 calibrations only — no extra fits.

Per skein-binding-lagrangian.md structural form:
  L_bind = (q+q⁻¹)/2 · [λ_V·A − λ_S·A^(2/3) − λ_C·Z(Z-1)/A^(1/3)
                        − λ_Pauli·(N-Z)²/A + λ_pair·(±)/√A]

The framework's existing 3-cal pieces:
  - Term 4 (Frobenius co-Casimir): m_e · Σ_λ 1/dim_q(V_λ) at H_n
  - Term 7 (Borromean): m_e · 8G (universal)
  - mass_table_ppb: ρ_F · Vol(K) where ρ_F ∈ {m_e, 2m_e}

Empirical BW values (for reference, NOT used as input):
  λ_V    ≈ 15.75 MeV
  λ_S    ≈ 17.8  MeV
  λ_C    ≈ 0.71  MeV
  λ_Pauli ≈ 23.7  MeV
  λ_pair  ≈ 12    MeV

Test which combinations of (m_e, q-arithmetic) at q_0 give
plausible structural derivations.  No fit — just sweep candidates
and report which structural form best matches each empirical λ.
"""
from __future__ import annotations
import json, sys, warnings
from pathlib import Path
from datetime import datetime, timezone
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
Q0 = Q_MP  # was f64 roundtrip
QI = Q_INV_MP
m_e = mp.mpf("0.51099895")
G = mp.catalan
h = Q0 - QI
hbar_q = (Q0 - 1)/Q0


def qint(n): return (Q0**n - QI**n)/(Q0 - QI)
def qfac(n):
    p = mp.mpf(1)
    for k in range(1, n+1): p *= qint(k)
    return p

# Categorical building blocks (all from m_e, q_0 alone)
BLOCKS = {
    "m_e": float(m_e),
    "m_e · [2]_q":     float(m_e * qint(2)),
    "m_e · [3]_q":     float(m_e * qint(3)),
    "m_e · [4]_q":     float(m_e * qint(4)),
    "m_e · [5]_q":     float(m_e * qint(5)),
    "m_e · [6]_q":     float(m_e * qint(6)),
    "m_e · [9]_q":     float(m_e * qint(9)),
    "m_e · [10]_q":    float(m_e * qint(10)),
    "m_e · 8G":        float(m_e * 8 * G),
    "m_e · π²":        float(m_e * mp.pi**2),
    "m_e · 4π":        float(m_e * 4 * mp.pi),
    "m_e · 2π²":       float(m_e * 2 * mp.pi**2),
    "m_e · Σ_3":       float(m_e * (2 + 1/qint(2))),
    "m_e · Σ_3 · [10]_q":  float(m_e * (2 + 1/qint(2)) * qint(10)),
    "m_e · Σ_3 · [9]_q":   float(m_e * (2 + 1/qint(2)) * qint(9)),
    "m_e · 8G · [4]_q":    float(m_e * 8*G * qint(4)),
    "m_e · 8G · 4":        float(m_e * 8*G * 4),
    "m_e · 8G · [5]_q":    float(m_e * 8*G * qint(5)),
    "m_e · 8G · π":        float(m_e * 8*G * mp.pi),
    "m_e/(q-1)":           float(m_e/(Q0-1)),
    "m_e/(q-1)²":          float(m_e/(Q0-1)**2),
    "m_e · (q+1)/(q-1)":   float(m_e * (Q0+1)/(Q0-1)),
    "m_e · [2]_q²":        float(m_e * qint(2)**2),
    "m_e · [3]_q²":        float(m_e * qint(3)**2),
    "m_e · h":             float(m_e * h),
    "m_e · h²":            float(m_e * h**2),
}

# Empirical BW (reference only)
TARGETS = {
    "λ_V (15.75 MeV)":  15.75,
    "λ_S (17.8 MeV)":   17.8,
    "λ_C (0.71 MeV)":    0.71,
    "λ_Pauli (23.7 MeV)": 23.7,
    "λ_pair (12 MeV)":   12.0,
}

print("=" * 110)
print("BW-Lagrangian prefactor candidates from (m_e, q_0) — structural building blocks")
print("=" * 110)
print(f"  q_0 = {float(Q0):.10f}")
print(f"  m_e = {float(m_e):.6f} MeV")
print()
print(f"  {'building block':<28} {'value (MeV)':>14}")
for name, val in BLOCKS.items():
    print(f"  {name:<28} {val:>14.6f}")

print()
print("=" * 110)
print("Best structural match for each empirical BW prefactor")
print("=" * 110)
print(f"  {'target':<22} {'best match':<35} {'value':>10} {'err %':>10}")
print("-" * 110)
results = {}
for tgt_name, tgt_val in TARGETS.items():
    best_err = None; best_block = None
    for name, val in BLOCKS.items():
        err = (val - tgt_val)/tgt_val * 100
        if best_err is None or abs(err) < abs(best_err):
            best_err = err; best_block = name
    print(f"  {tgt_name:<22} {best_block:<35} {BLOCKS[best_block]:>10.4f} {best_err:>+10.4f}%")
    results[tgt_name] = {"best_match": best_block, "value": BLOCKS[best_block],
                         "err_pct": best_err}

print()
print("=" * 110)
print("INTERPRETATION")
print("=" * 110)
print("""
None of these are exact closed forms — empirical BW prefactors are
phenomenological fits to nuclear data, while the framework wants
3-cal structural derivations.

The closest 'natural' candidates (matched within ~10%) suggest:
  - λ_V ~ m_e · 8G · [4]_q  or m_e · Σ_3 · [10]_q  (≈ 15-16 MeV class)
  - λ_C ~ m_e · h  or m_e · h²  (sub-MeV class)
  - λ_Pauli ~ m_e · (q+1)/(q-1)  or m_e/(q-1)²  (20-40 MeV class)

But getting exact ppb-class agreement requires a structural derivation,
not basis sweeping.  Each empirical BW constant absorbs nuclear-physics
phenomenology that the framework would have to derive from QOU-internal
categorical structures (Bring's surface, GB filtration, Hecke
characters at H_{3A}).

This is a real theoretical project — not solvable by basis sweep.
The honest 3-cal verdict: shell physics (Term 7) IS derivable from
(m_e, q_0); volume + surface + Coulomb + Pauli + pair sectors require
their own categorical derivation, currently OPEN.
""")

out = {
    "computation": "bw-lagrangian-prefactor-attempt",
    "description": ("Attempt to derive BW-Lagrangian prefactors λ_V, λ_S, "
                    "λ_C, λ_Pauli, λ_pair from (m_e, q_0) alone via "
                    "structural building-block sweep.  No fitting allowed. "
                    "Reports closest natural q-arithmetic candidate for "
                    "each empirical BW constant."),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "calibrations": {"m_e_MeV": float(m_e), "q_0": float(Q0)},
    "empirical_BW_targets": TARGETS,
    "candidate_blocks_MeV": BLOCKS,
    "best_matches": results,
    "verdict": ("Sweep finds no exact closed forms.  BW prefactors are "
                "phenomenological — deriving them from 3 cals requires "
                "categorical structural work beyond block-sweeping.  "
                "Shell physics (Term 7) IS derivable; volume / surface / "
                "Coulomb / Pauli / pair sectors are OPEN.")
}
out_path = Path(__file__).parent / "bw-lagrangian-prefactor-attempt.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)
print(f"Witness: {out_path}")
