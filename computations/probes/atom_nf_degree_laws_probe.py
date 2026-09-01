#!/usr/bin/env python3
"""atom_nf_degree_laws_probe.py
================================

**Two closed forms for the q-degree of `build_atom_nf_sym`, both measured
on a stated range and neither derived.**

Companion to `atom_nf_q_degree_probe.py`, which established that the six NF
coefficients are Laurent polynomials in `ℤ[½][q, q^{±1}]` with exactly
symmetric support, that the max-plus (tropical) model of the degree is a
genuine upper bound but not a tight one, and that the shortfall is opened by
the neutron-neutron step — `σ₀ + d(nn) = σ₀ − h = σ₀⁻¹`, the negative
crossing — while the averaged p-n step `½(σ₀ + σ₀⁻¹)` never opens any.

That left two things open.  This probe closes both **as measured laws**.

## 1. The size of the shortfall

For `Z ≥ 5` and `N ≥ 5`:

        gap(Z, N)  =  6N − 19 + [Z > N]

where `gap = tropical − actual` on the largest of the six components.  Zero
exceptions on the whole tested grid.  Two things about its shape:

* **It does not depend on Z** beyond the single indicator.  Once a nucleus
  carries five or more protons, the leading-order loss is a function of the
  **neutron count alone**, linear, at **6 degrees per neutron**.
* `Z ≤ 4` is a genuinely different and larger regime — but it converges to
  the same slope.  Measured asymptotic increments: `Z = 2` and `Z = 4` both
  settle to **+6 per neutron** (with different offsets, `6N + 41` from
  N = 10 and `6N + 7` from N = 9); `Z = 0` alone settles to **+8**
  (`8N + 2` from N = 8).  So the pure-neutron chain is the one outlier in
  slope, not merely in offset.

## 2. The A = 27 break, as a two-branch maximum

The companion probe found that on the pure-neutron ray `deg(γ) = A(A+1)/2`
holds on `7 ≤ A ≤ 26` and then breaks.  Extended to A = 40, the break is
completely regular — the excess over the triangular number grows by exactly
2 per unit A, with no further transition:

        deg(γ)|_{Z=0}  =  A(A+1)/2 + 2·max(0, A − 26)

i.e. the maximum of two branches with the **same quadratic leading term**
whose linear parts differ by `2A − 52`, crossing exactly at A = 26.  And
`deg(σ₀) = deg(γ) − 1` holds **for A = 8…40**, across the break as well as
away from it, so this is not a reordering of which component dominates — both
move together.  **A = 7 is the sole exception**, at offset `+7`; it is the
lower edge of the triangular window itself (the companion probe's window is
7…26), so the regime has not settled there.  This was asserted over 7…40
first, and the producer failed itself on it.

## What is NOT established

* **Neither law is derived.**  No mechanism is offered for the coefficient 6,
  for the constant −19, for the `Z ≥ 5` threshold, or for the crossover at
  A = 26.  They are fits to exact integer data over a stated range, and the
  range is stated because the companion probe's own triangular law looked
  exact over twenty consecutive values before breaking at the twenty-first.
  Treat every constant here the same way.
* The `Z ≤ 4` offsets are read off the *last few* increments of a short
  sequence and are the weakest claims in this file.
* Nothing here is anchor-dependent — `q` is a formal Laurent variable
  throughout and no q₀ is substituted.

Reference: prop:mass-endomorphism-tower
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_HERE = _Path(__file__).resolve()
_ROOT = _HERE.parent.parent.parent
_sys.path.insert(0, str(_ROOT / "computations"))
_sys.path.insert(0, str(_ROOT / "computations" / "substrate"))
_sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _b  # noqa: E402, F401
del _b

import time  # noqa: E402

from atom_nf_q_degree_probe import (build_atom_nf_lp,  # noqa: E402
                                    tropical_degrees)
from qou_substrate.witness import WitnessBuilder  # noqa: E402

# Grid bound. A = Z + N <= MAX_A keeps the tropical sweep affordable; the
# cost of one cell is O(A^4) in Fraction ops.
MAX_A = 17
RAY_MAX = 40


def gap(Z: int, N: int) -> int:
    """tropical - actual, on the largest of the six components."""
    nf, _ = build_atom_nf_lp(Z, N)
    act = max(max(c) for c in nf if c)
    tro = max(x for x in tropical_degrees(Z, N) if x is not None)
    return tro - act


def main() -> int:
    t0 = time.time()
    fails: list[str] = []

    def chk(label: str, cond: bool) -> None:
        print(f"  [{'PASS' if cond else 'FAIL'}] {label}")
        if not cond:
            fails.append(label)

    print("atom NF q-degree — two measured closed forms")
    print("=" * 66)

    # ── 1. gap(Z, N) = 6N - 19 + [Z > N] on Z >= 5, N >= 5 ───────────
    print(f"\n1. gap law on Z >= 5, N >= 5   (A <= {MAX_A})")
    grid = []
    law_ok = True
    tested = 0
    for Z in range(5, MAX_A - 4):
        for N in range(5, MAX_A - Z + 1):
            g = gap(Z, N)
            pred = 6 * N - 19 + (1 if Z > N else 0)
            grid.append({"Z": Z, "N": N, "gap": g, "predicted": pred})
            law_ok &= (g == pred)
            tested += 1
        print(f"      Z={Z:>2} done  ({time.time() - t0:.0f}s elapsed)")
    chk(f"gap = 6N - 19 + [Z > N] on all {tested} cells with Z >= 5, N >= 5",
        law_ok)
    z_independent = len({(r["N"], r["gap"] - (1 if r["Z"] > r["N"] else 0))
                         for r in grid}) == len({r["N"] for r in grid})
    chk("and it is INDEPENDENT of Z once the [Z > N] term is removed",
        z_independent)

    # ── 2. small-Z rays are a different, larger regime ───────────────
    print("\n2. small-Z rays (Z <= 4) — different regime, and its slope")
    small = {}
    for Z in (0, 2, 4):
        vals = [(N, gap(Z, N)) for N in range(6, MAX_A - Z + 1)]
        diffs = [vals[i + 1][1] - vals[i][1] for i in range(len(vals) - 1)]
        small[str(Z)] = {"values": vals, "increments": diffs,
                         "final_increment": diffs[-1] if diffs else None}
        print(f"      Z={Z}: " + " ".join(f"N{n}:{g}" for n, g in vals)
              + f"   diffs {diffs}")
    chk("Z = 2 and Z = 4 settle to the same +6 per neutron as Z >= 5",
        small["2"]["final_increment"] == 6 and small["4"]["final_increment"] == 6)
    chk("Z = 0 is the outlier in SLOPE, settling to +8 per neutron",
        small["0"]["final_increment"] == 8)

    # ── 3. the A = 27 break is one clean two-branch maximum ──────────
    print(f"\n3. pure-neutron ray to A = {RAY_MAX}: two branches, crossing at 26")
    ray = []
    branch_ok = True
    offset_ok = True
    offset_exceptions = []
    for A in range(7, RAY_MAX + 1):
        nf, calls = build_atom_nf_lp(0, A)
        g, s0 = max(nf[0]), max(nf[1])
        pred = A * (A + 1) // 2 + 2 * max(0, A - 26)
        ray.append({"A": A, "calls": calls, "deg_gamma": g, "deg_sigma0": s0,
                    "closed_form": pred, "triangular": A * (A + 1) // 2})
        branch_ok &= (g == pred)
        # The -1 offset holds from A = 8, NOT from A = 7. A = 7 is the
        # lower boundary of the triangular window itself (the companion
        # probe's window is 7..26), so the regime has not settled there.
        if A >= 8:
            offset_ok &= (s0 == g - 1)
        elif s0 != g - 1:
            offset_exceptions.append({"A": A, "deg_gamma": g,
                                      "deg_sigma0": s0, "offset": s0 - g})
        if A % 8 == 0:
            print(f"      A={A:>2} deg={g:<5} pred={pred:<5} "
                  f"({time.time() - t0:.0f}s elapsed)")
    chk(f"deg(gamma) = A(A+1)/2 + 2*max(0, A - 26) for every A = 7..{RAY_MAX}",
        branch_ok)
    chk(f"deg(sigma0) = deg(gamma) - 1 for A = 8..{RAY_MAX}, i.e. across the "
        f"break as well as away from it", offset_ok)
    chk(f"and A = 7 is the ONE exception, offset "
        f"{offset_exceptions[0]['offset'] if offset_exceptions else 'n/a'} "
        f"— the lower edge of the triangular window, not a stray",
        [r["A"] for r in offset_exceptions] == [7])
    excess = [r["deg_gamma"] - r["triangular"] for r in ray]
    incs = {excess[i + 1] - excess[i] for i in range(len(excess) - 1)
            if ray[i]["A"] >= 27}
    chk(f"the excess grows by exactly 2 per unit A past the break, with no "
        f"further transition (increments seen: {sorted(incs)})", incs == {2})

    print(f"\n{'ALL CHECKS PASSED' if not fails else str(len(fails)) + ' CHECK(S) FAILED'}"
          f"   [{time.time() - t0:.0f}s]")

    w = WitnessBuilder("atom-nf-degree-laws", start_time=t0,
                       output_dir=_HERE.parent)
    w.set_description(
        "Two MEASURED closed forms for the q-degree of "
        "hecke_core_symbolic.build_atom_nf_sym, neither derived. (1) The "
        "shortfall of the max-plus bound is gap = 6N - 19 + [Z > N] for "
        "Z >= 5 and N >= 5, with zero exceptions on the tested grid -- so "
        "once a nucleus carries five or more protons the leading-order loss "
        "depends on the NEUTRON COUNT ALONE, linearly, at 6 degrees per "
        "neutron, independent of Z. Z <= 4 is a larger regime but converges "
        "to the same slope: Z=2 and Z=4 both settle to +6 per neutron with "
        "different offsets, and Z=0 alone settles to +8, making the "
        "pure-neutron chain an outlier in slope rather than only in offset. "
        "(2) The A=27 break in the companion probe's triangular law is one "
        "clean two-branch maximum: deg(gamma) = A(A+1)/2 + 2*max(0, A-26), "
        "verified A=7..40, two branches with the SAME quadratic leading term "
        "whose linear parts differ by 2A-52 and cross exactly at A=26; "
        "deg(sigma0) = deg(gamma) - 1 holds for A=8..40, across the break "
        "too, so it is not a reordering of which component dominates; A=7 is "
        "the sole exception at offset +7 and is the lower edge of the "
        "triangular window itself. NOT DERIVED: no "
        "mechanism for the coefficient 6, the constant -19, the Z >= 5 "
        "threshold, or the crossover at 26. These are fits to exact integer "
        "data over a STATED range, and the range is stated because the "
        "companion probe's triangular law looked exact over twenty "
        "consecutive values before breaking at the twenty-first.")
    w.add_data("gap_law", {
        "formula": "gap(Z,N) = 6N - 19 + [Z > N]",
        "domain": f"Z >= 5, N >= 5, A <= {MAX_A}",
        "cells_tested": tested,
        "exceptions": [r for r in grid if r["gap"] != r["predicted"]],
        "z_independent": z_independent,
        "reading": ("the leading-order loss is a function of the neutron "
                    "count alone, at 6 degrees per neutron"),
        "grid": grid,
    })
    w.add_data("small_Z_regime", {
        "note": ("Z <= 4 is larger and does not follow the law; recorded "
                 "because the SLOPE still converges. These offsets are read "
                 "off the last few increments of a short sequence and are "
                 "the weakest claims in this witness."),
        "rays": small,
    })
    w.add_data("pure_neutron_two_branch", {
        "formula": "deg(gamma) = A(A+1)/2 + 2*max(0, A - 26)",
        "verified_range": f"A = 7..{RAY_MAX}",
        "crossover": 26,
        "branch_difference": "2A - 52 (same quadratic leading term)",
        "sigma0_offset": ("deg(sigma0) = deg(gamma) - 1 for A = 8..40, "
                          "across the break too; A = 7 is the sole "
                          "exception at offset +7"),
        "sigma0_offset_exceptions": offset_exceptions,
        "ray": ray,
    })
    w.add_data("not_established", {
        "derivation": "neither law is derived; both are fits to exact data",
        "constants": "no mechanism for 6, -19, the Z>=5 threshold, or 26",
        "beyond_range": f"Z + N > {MAX_A} and A > {RAY_MAX} not measured",
    })
    w.add_data("checks_failed", fails)
    w.add_assertion("gap_law_holds_on_Z_ge_5_N_ge_5", law_ok, True)
    w.add_assertion("gap_law_is_independent_of_Z", z_independent, True)
    w.add_assertion("pure_neutron_two_branch_form_A_7_to_40", branch_ok, True)
    w.add_assertion("sigma0_offset_survives_the_break_A_ge_8", offset_ok, True)
    w.add_assertion("sigma0_offset_sole_exception_is_A_7",
                    [r["A"] for r in offset_exceptions] == [7], True)
    w.add_assertion("excess_increment_is_exactly_2_past_the_break",
                    incs == {2}, True)
    w.save({
        "q0Anchor": "independent",
        "q0AnchorReason": ("q is a formal Laurent variable throughout; no q0 "
                           "is substituted anywhere, so neither pin can "
                           "affect any number in this witness."),
    })
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
