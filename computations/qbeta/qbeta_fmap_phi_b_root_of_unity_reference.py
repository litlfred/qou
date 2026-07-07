#!/usr/bin/env python3
"""qbeta_fmap_phi_b_root_of_unity_reference.py — Φ_b reference values at the fibre saddle.

Task-2 step of the f-map program (pre-registered, non-fishing): evaluate the
VALIDATED Faddeev Φ_b (phi_b_evaluator.py — literature-verified against
uploads/0604094v1.pdf, Hikami math/0604094) at REAL b with b² RATIONAL, i.e.
q = e^{2πib²} a ROOT OF UNITY — the fibre/decay saddle where the bar-odd
factor F_odd of the ladder element F(q) = F_even·F_odd must live.

Points (chosen by CORPUS STRUCTURE, not by numerical matching):
  * b² = 1/4  ⇒ q = i = ζ₄        — the corpus's PROVED ζ₄ residue structure
  * b² = 2/5  ⇒ q = e^{4πi/5} = ζ₅² — the ζ₅ / Galois locus (cl3-zeta5 thread)
  * b² = 1/6  ⇒ q = e^{πi/3} = ζ₆  — the Vol(4₁) = 2Λ(π/3) angle π/3
  * b² = 1    ⇒ q = 1 (self-dual point b = 1/b) — degenerate control

At each point: Φ_b(z) for a few small real z, each row GATED by a local shift-
equation check (the value is only recorded if the functional equation holds at
that point to ≥ 1e-15), plus the closed-form special value
Φ_b(0) = ±e^{iπ(b²+b⁻²)/24} (sign branch detected and reported).

ANTI-FITTING (C14 discipline): these are REFERENCE VALUES for the F_odd
construction. Nothing here is compared against c_k, Φ₁ = √2, the residue A,
or any physical constant — a scan for such a match would be a fit.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from phi_b_evaluator import phi_b  # noqa: E402

mp.mp.dps = 35

POINTS = [
    ("zeta_4  (b^2 = 1/4, q = i)", mp.mpf(1) / 4),
    ("zeta_5^2 (b^2 = 2/5)", mp.mpf(2) / 5),
    ("zeta_6  (b^2 = 1/6)", mp.mpf(1) / 6),
    ("self-dual (b^2 = 1, q = 1)", mp.mpf(1)),
]

Z_GRID = [mp.mpf("0"), mp.mpf("0.1"), mp.mpf("0.25")]


def shift_check(b) -> float:
    """Local shift-equation residual at this b (gates the row)."""
    z = mp.mpf("0.13")
    lhs = phi_b(z - mp.mpc(0, 1) * b / 2, b) / phi_b(z + mp.mpc(0, 1) * b / 2, b)
    tgt = 1 + mp.e ** (2 * mp.pi * b * z)
    return float(mp.fabs(lhs - tgt) / mp.fabs(tgt))


def main() -> int:
    print("=" * 78)
    print(" Φ_b at rational b² (root-of-unity q) — F_odd reference values (gated)")
    print("=" * 78)
    ok_all = True
    for label, b2 in POINTS:
        b = mp.sqrt(b2)
        q = mp.e ** (2 * mp.pi * mp.mpc(0, 1) * b2)
        err = shift_check(b)
        gate = err < 1e-15
        ok_all = ok_all and gate
        print(f"\n  {label}:  b = {mp.nstr(b, 10)},  q = {mp.nstr(q, 8)}")
        print(f"     shift-equation gate at this b: rel.err {err:.1e}  {'OK' if gate else 'FAIL'}")
        # special value Φ_b(0) vs ±e^{iπ(b²+b⁻²)/24}
        v0 = phi_b(0, b)
        cand = mp.e ** (mp.mpc(0, 1) * mp.pi * (b2 + 1 / b2) / 24)
        ep = float(mp.fabs(v0 - cand) / mp.fabs(cand))
        em = float(mp.fabs(v0 + cand) / mp.fabs(cand))
        sign = "+" if ep < em else "−"
        print(f"     Φ_b(0) = {mp.nstr(v0, 16)}")
        print(f"       vs {sign}e^(iπ(b²+b⁻²)/24): rel.err {min(ep, em):.1e}"
              f"  {'OK' if min(ep, em) < 1e-15 else 'reported'}")
        for z in Z_GRID[1:]:
            v = phi_b(z, b)
            print(f"     Φ_b({mp.nstr(z, 3)}) = {mp.nstr(v, 16)}   |Φ| = {mp.nstr(mp.fabs(v), 12)}")
    print()
    print("  SCOPE: reference data for the F_odd (bar-odd / fibre-saddle) build.")
    print("  Deliberately NOT compared to c_k / Φ₁ / residue A / any physical")
    print("  constant (C14 anti-fitting). The z-grid is arbitrary small reals.")
    print(f"\n  ALL GATES: {'OK' if ok_all else 'FAILURES'}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
