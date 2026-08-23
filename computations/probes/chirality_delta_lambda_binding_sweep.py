#!/usr/bin/env python3
"""Chirality-Δ_λ binding sweep — magnitude-variant test (EXPLORATORY).

#2405 + keystone wiring established that the PROVED factor Δ_λ=sgn(w₀^{S_λ'})·dim
gives a binding B=m_e·|Σ_λ y_λ χ^λ Δ_λ| that UNDERSHOOTS ≤⁴He then DIVERGES into
overshoot at A≥6 — the bare dim(V_λ) magnitude grows combinatorially. The sign
side (chirality) is proved/fine; the MAGNITUDE side (bare dim) is the failure.

This tests the obvious bounded-magnitude candidates across A (D…⁷Li):
  • Δ_λ = 1          → B = m_e·|tr_M| (raw trace; reference)
  • Δ_λ = sgn        → sign-twist only, NO dim (the Markov weight y_λ already
                       carries a quantum-dimension normalisation, so dropping
                       the bare dim should stay bounded; V_λ⊗sgn≅V_{λ'})
  • Δ_λ = sgn·dim    → the PROVED factor (diverges; baseline)
  • Δ_λ = sgn·dim_q  → quantum dimension [n]_q!/Π[hook]_q at q₀ (q-deformed)

Goal: which magnitude keeps the binding sum BOUNDED across A, and does any track
AME? Derive-or-refute; the formulae are categorical (no C_knot fit), not wired.
Cross-check: Δ=sgn·dim at D must reproduce 0.380 MeV.
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

# Path bridge (moved above the set_compute_dps() call — it is what
# puts computations/substrate on sys.path so `_precision` resolves).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from tr_m_atom_via_transfer import tr_m_atom_zn          # noqa: E402  (PR #2405)
from wedderburn_jones_markov import y_lambda_at          # noqa: E402
# 50-dps source (NO FLOAT64). Behaviour is unchanged: Q_MP differs from the
# f64 Q by ~1e-17, far inside the 1e-12 cache tolerance either way.
#
# NOT a layer straddle, though it looks like one: `y-lambda-at-q0.witness.json`
# is muon-built, but the cache gate compares the caller's q against the
# WITNESS's own recorded q0, not against q_parameter.Q. |q_muon - q_proton| =
# 1.28e-8 is 12810x the 1e-12 tolerance, so a proton-q0 caller misses the
# muon cache and falls through to the live closed form at the q it asked for.
# (The 1e-12 sits between float64 ulp at q~1.11, 2.46e-16, and that anchor gap.)
# AGENTS.md still describes the older, broken gate -- the code is ahead of it.
from q_parameter import Q_MP as q0                       # noqa: E402
from codata_constants import M_E_MEV                     # noqa: E402

ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2),
      "6Li": (3, 3), "7Li": (3, 4)}
_Q = mp.mpf(str(q0))


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
    """sgn(w₀^{S_λ'}) = Π_cols (−1)^{C(λ'_c,2)} — the proved chirality sign."""
    s = 1
    for b in transpose(lam):
        s *= (-1) ** (b * (b - 1) // 2)
    return s


def qint(k: int) -> mp.mpf:
    return (_Q**k - _Q**(-k)) / (_Q - 1 / _Q)


def dim_q(lam) -> mp.mpf:
    """quantum dimension f^λ_q = [n]_q!/Π_cells[hook]_q (q-hook-length, q₀)."""
    n = sum(lam)
    num = mp.mpf(1)
    for k in range(1, n + 1):
        num *= qint(k)
    den = mp.mpf(1)
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = sum(1 for k in range(i + 1, len(lam)) if lam[k] > j)
            den *= qint(arm + leg + 1)
    return num / den


VARIANTS = [
    ("1(raw)",   lambda lam: mp.mpf(1)),
    ("sgn",      lambda lam: mp.mpf(delta_sign(lam))),
    ("sgn·dim",  lambda lam: mp.mpf(delta_sign(lam) * hook_dim(lam))),
    ("sgn·dimq", lambda lam: mp.mpf(delta_sign(lam)) * dim_q(lam)),
]


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
    print(" Chirality-Δ_λ binding — magnitude-variant test:  B = m_e·|Σ_λ y_λ χ^λ(β_atom) Δ_λ|")
    print(" (EXPLORATORY, no fit; sign=proved chirality, vary the MAGNITUDE)")
    print("=" * 96)
    print(f" m_e={float(m_e):.6f}, q₀={float(q0):.8f}\n")

    # precompute χ^λ, y_λ per atom (the expensive part — once)
    data = {}
    for atom, (Z, N) in ZN.items():
        n = 3 * (Z + N)
        _, _, chi_atom, _ = tr_m_atom_zn(Z, N)
        y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(n, q0).items()}
        data[atom] = (Z, N, n, chi_atom, y)

    # B_pred per variant
    print("  B_pred (MeV):")
    print(f"  {'iso':<5}{'A':>3}{'B_AME':>9}" + "".join(f"{v[0]:>12}" for v in VARIANTS))
    print("  " + "-" * 80)
    BP = {}
    for atom, (Z, N, n, chi_atom, y) in data.items():
        bame = ame.get((Z, Z + N))
        line = f"  {atom:<5}{Z+N:>3}{(bame or 0):>9.3f}"
        BP[atom] = {}
        for vname, vfn in VARIANTS:
            S = mp.fsum(y[lam] * chi_atom[lam] * vfn(lam) for lam in chi_atom)
            B = float(m_e * abs(S))
            BP[atom][vname] = B
            line += f"{B:>12.4f}"
        print(line)

    print("\n  ratio AME/B_pred  (1.00 = match; ≫1 under; ≪1 over; — = no AME):")
    print(f"  {'iso':<5}{'A':>3}" + "".join(f"{v[0]:>12}" for v in VARIANTS))
    print("  " + "-" * 71)
    for atom, (Z, N, n, chi_atom, y) in data.items():
        bame = ame.get((Z, Z + N))
        line = f"  {atom:<5}{Z+N:>3}"
        for vname, _ in VARIANTS:
            B = BP[atom][vname]
            r = (bame / B) if (bame and B > 0) else None
            line += f"{(f'{r:.3f}' if r else '—'):>12}"
        print(line)

    bD = BP["D"]["sgn·dim"]
    print(f"\n  cross-check: Δ=sgn·dim at D = {bD:.4f} MeV vs deuteron-only 0.380 →",
          "MATCH" if abs(bD - 0.380) < 0.02 else f"DIFF Δ={bD-0.380:+.3f}")
    print("  reading: does any magnitude stay BOUNDED across A (no ⁶Li/⁷Li blow-up)"
          " and track AME?\n  Derive-or-refute; categorical formulae, no fit, not wired.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
