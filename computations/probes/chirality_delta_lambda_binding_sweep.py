#!/usr/bin/env python3
"""Chirality-Δ_λ binding sweep — wire the PROVED Δ_λ=sgn·dim through the all-A
χ^λ transfer (EXPLORATORY).

Wires together two pieces that were never connected:
  • the PROVED categorical per-block factor (keystone S5SO3FiberAction.lean,
    PR #1305; audit 2026-06-16-delta-lambda-sign-is-icosahedral-chirality.md):
        Δ_λ = sgn(w₀^{S_λ'}) · dim(V_λ)
    — magnitude = Wedderburn dim, sign = icosahedral chirality (−1)^{Σ C(λ'_c,2)};
  • the all-A fine-Bratteli χ^λ transfer (PR #2405, tr_m_atom_via_transfer)
    which gives χ^λ(β_atom) for EVERY isotope at q₀, no p(3A) wall.

The categorical binding (binding_energy_categorical_deuteron.py, PR #1307):
    B(K) = m_e · |Σ_{λ⊢3A} y_λ · χ^λ(β_atom) · Δ_λ|

was only ever evaluated for the DEUTERON (loaded from a precomputed witness;
B(D)=0.380 MeV, −82.9 % vs AME — the Δ_λ gate is OPEN, the deficit is NOT a
derived layer). This script EXTENDS that exact formula to D…⁷Li using the
transfer χ^λ, to see HOW the chirality-Δ_λ binding tracks AME across the chain
(uniform undershoot? does the chirality sign structure do anything?).

DISCIPLINE: derive-or-refute; the formula is the FORMALIZED one (no C_knot fit).
Known to undershoot the deuteron; this quantifies it across A + exposes the
per-λ sign structure. No production rewire, no fit. Cross-check: D ≈ 0.380.
"""
from __future__ import annotations

import sys
from math import factorial
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
for p in (str(ROOT), str(ROOT / "substrate")):
    sys.path.insert(0, p)

mp.mp.dps = 50

from tr_m_atom_via_transfer import tr_m_atom_zn          # noqa: E402  (PR #2405)
from wedderburn_jones_markov import y_lambda_at          # noqa: E402
from q_parameter import Q as q0                          # noqa: E402
from codata_constants import M_E_MEV                     # noqa: E402

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2),
      "6Li": (3, 3), "7Li": (3, 4)}


# ── the PROVED Δ_λ = sgn(w₀^{S_λ'})·dim factor (option_e_delta_lambda_sign_chirality.py) ──
def transpose(lam):
    return tuple(sum(1 for r in lam if r > c) for c in range(lam[0])) if lam else ()


def hook_dim(lam) -> int:
    n = sum(lam)
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = sum(1 for k in range(i + 1, len(lam)) if lam[k] > j)
            prod *= (arm + leg + 1)
    return factorial(n) // prod


def delta_sign(lam) -> int:
    """sgn(w₀^{S_λ'}) = Π_cols (−1)^{C(λ'_c,2)} — transpose-determined chirality."""
    s = 1
    for b in transpose(lam):
        s *= (-1) ** (b * (b - 1) // 2)
    return s


def delta_lambda(lam) -> int:
    return delta_sign(lam) * hook_dim(lam)


def _ame_binding():
    import json
    d = json.loads((ROOT / "data" / "ame2020.json").read_text())
    entries = d["entries"] if isinstance(d, dict) and "entries" in d else d
    rows = entries.values() if isinstance(entries, dict) else entries
    out = {}
    for r in rows:
        b = r.get("binding_energy_total_keV")
        if b is not None:
            out[(r["Z"], r["A"])] = b / 1000.0
    return out


def main() -> int:
    m_e = mp.mpf(M_E_MEV)
    ame = _ame_binding()
    print("=" * 96)
    print(" Chirality-Δ_λ binding sweep:  B(K) = m_e·|Σ_λ y_λ χ^λ(β_atom) sgn(w₀^{S_λ'}) dim(V_λ)|")
    print(" (the PROVED Δ_λ=sgn·dim factor × the all-A χ^λ transfer; EXPLORATORY, no fit)")
    print("=" * 96)
    print(f" m_e={float(m_e):.6f} MeV, q₀={float(q0):.10f}\n")
    print(f"  {'iso':<5}{'A':>3}{'n':>4}{'#λ':>5}{'Σ_λ yχΔ':>16}{'B_pred':>11}"
          f"{'B_AME':>10}{'ratio':>8}{'#sgn+':>7}{'#sgn-':>7}")
    print("  " + "-" * 92)
    rows = []
    for atom, (Z, N) in ZN.items():
        n = 3 * (Z + N)
        tA, tF, chi_atom, wall = tr_m_atom_zn(Z, N)
        y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q0).items()}
        terms = []
        npos = nneg = 0
        for lam in chi_atom:
            dl = delta_lambda(lam)
            if delta_sign(lam) > 0:
                npos += 1
            else:
                nneg += 1
            terms.append(y[lam] * chi_atom[lam] * dl)
        S = mp.fsum(terms)
        B = m_e * abs(S)
        bame = ame.get((Z, Z + N))
        ratio = (bame / float(B)) if (bame and float(B) > 0) else None
        rows.append((atom, n, float(S), float(B), bame, ratio))
        print(f"  {atom:<5}{Z+N:>3}{n:>4}{len(chi_atom):>5}{mp.nstr(S,8):>16}"
              f"{float(B):>11.4f}{(bame if bame else 0):>10.4f}"
              f"{(ratio if ratio else 0):>8.2f}{npos:>7}{nneg:>7}")
    # cross-check vs the deuteron-only compute (binding_energy_categorical_deuteron.py)
    bD = next(r[3] for r in rows if r[0] == "D")
    print("\n  cross-check D: B_pred =", f"{bD:.4f}",
          "MeV vs the deuteron-only compute 0.380 MeV →",
          "MATCH" if abs(bD - 0.380) < 0.02 else f"DIFF (convention?) Δ={bD-0.380:+.3f}")
    print("\n  reading: ratio = B_AME/B_pred (>1 = undershoot). The formula is the"
          " PROVED Δ_λ=sgn·dim;\n  it is known to undershoot the deuteron — this"
          " shows whether the undershoot is uniform across A\n  and what the"
          " per-λ chirality-sign split (#sgn±) looks like. No fit, not wired.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
