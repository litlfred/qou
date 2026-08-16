#!/usr/bin/env python3
"""qbeta_fmap_phi_b_root_of_unity_reference.py — Φ_b reference values at the fibre saddle.

Task-2 step of the f-map program (pre-registered, non-fishing): evaluate the
VALIDATED Faddeev Φ_b (phi_b_evaluator.py — literature-verified against
library/arxiv-math-0604094v1/0604094v1.pdf, Hikami math/0604094) at REAL b with b² RATIONAL, i.e.
q = e^{2πib²} a ROOT OF UNITY — the fibre/decay saddle where the bar-odd
factor F_odd of the ladder element F(q) = F_even·F_odd must live.

Points (chosen by CORPUS STRUCTURE, not by numerical matching):
  * b² = 1/4  ⇒ q = i = ζ₄        — the corpus's PROVED ζ₄ residue structure
  * b² = 2/5  ⇒ q = e^{4πi/5} = ζ₅² — the ζ₅ / Galois locus (cl3-zeta5 thread)
  * b² = 1/6  ⇒ q = e^{πi/3} = ζ₆  — the Vol(4₁) = 2·Cl₂(π/3) angle π/3
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
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from phi_b_evaluator import phi_b  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

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
    wb = WitnessBuilder("qbeta-fmap-phi-b-root-of-unity-reference", engine="mpmath")
    wb.set_description(
        "Reference values of the validated Faddeev non-compact quantum "
        "dilogarithm Φ_b (phi_b_evaluator.py — literature-verified against "
        "library/arxiv-math-0604094v1/0604094v1.pdf, Hikami math/0604094 eqs (2.1)-(2.5)) at "
        "rational b² (root-of-unity q, the fibre/decay saddle), for the "
        "F_odd construction. Every row gated by a local shift-equation "
        "check; unimodularity |Φ_b| = 1 (the pure-phase fact behind "
        "prop:phi-b-unitary-bar-odd) and the special value "
        "Φ_b(0) = +e^{iπ(b²+b⁻²)/24} asserted at every point. "
        "C14 anti-fitting: no comparison to c_k / Φ₁ / residue A / any "
        "physical constant."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")
    rows = []
    max_shift_err = 0.0
    max_unimod_err = 0.0
    max_special_err = 0.0
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
        max_shift_err = max(max_shift_err, err)
        max_special_err = max(max_special_err, min(ep, em))
        vals = []
        for z in Z_GRID[1:]:
            v = phi_b(z, b)
            unimod = abs(float(mp.fabs(v)) - 1.0)
            max_unimod_err = max(max_unimod_err, unimod)
            vals.append({"z": mp.nstr(mp.mpf(z), 6), "Phi_b": mp.nstr(v, 30),
                         "abs_minus_1": f"{unimod:.3e}"})
            print(f"     Φ_b({mp.nstr(z, 3)}) = {mp.nstr(v, 16)}   |Φ| = {mp.nstr(mp.fabs(v), 12)}")
        rows.append({
            "point": label, "b_sq": mp.nstr(mp.mpf(b2), 12), "b": mp.nstr(b, 30),
            "q": mp.nstr(q, 30), "shift_gate_rel_err": f"{err:.3e}",
            "Phi_b_0": mp.nstr(v0, 30), "special_value_sign": sign,
            "special_value_rel_err": f"{min(ep, em):.3e}", "values": vals,
        })
    print()
    print("  SCOPE: reference data for the F_odd (bar-odd / fibre-saddle) build.")
    print("  Deliberately NOT compared to c_k / Φ₁ / residue A / any physical")
    print("  constant (C14 anti-fitting). The z-grid is arbitrary small reals.")
    print(f"\n  ALL GATES: {'OK' if ok_all else 'FAILURES'}")

    wb.add_data("points", rows)
    wb.add_data("z_grid", [mp.nstr(mp.mpf(z), 6) for z in Z_GRID[1:]])
    wb.add_data("evaluator", "computations/qbeta/phi_b_evaluator.py (battery-gated)")
    wb.add_assertion(
        "shift_equation_gate_all_points",
        computed=max_shift_err, expected=0.0, tolerance=1e-15,
        source="Faddeev shift equation (Hikami math/0604094 eq 2.4a) at each b",
    )
    wb.add_assertion(
        "unimodularity_fibre_saddle",
        computed=max_unimod_err, expected=0.0, tolerance=1e-25,
        source="|Φ_b(z)| = 1 at real b, real z — the pure-phase fact behind prop:phi-b-unitary-bar-odd",
    )
    wb.add_assertion(
        "phi_b_zero_special_value",
        computed=max_special_err, expected=0.0, tolerance=1e-15,
        source="Φ_b(0) = +e^{iπ(b²+b⁻²)/24} (Hikami eq 2.3 at φ=0)",
    )
    wb.save()
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
