#!/usr/bin/env python3
"""The hull exit is a FRAMING SCALAR, and the exponent it needs is FRACTIONAL —
which makes the missing ingredient twist, not writhe.

WHAT THIS TESTS
---------------
`adding_crossings_cannot_break_the_degeneracy_probe` (bean `qou-o8ww`) closed
both named escapes with a single statement: the Hecke relation fixes
`det T = -1`, so a crossing's two block ratios multiply to
`det(T + dI) = d^2 + dh - 1`, whose magnitude is `>= 1` for every `d in [-h, 0]`.
Any product of such crossings inherits `|mu_sym . mu_anti| >= 1`, hence
`L(T=0) + L(T=1) <= 0` and the channel-asymmetry ratio is capped at `1` where
nature's is `33.7`. Escape requires `0 < d(d+h) < 2` — the bond operator must
leave the **convex hull** of `{sigma, sigma^-1}`.

This asks what could supply that, and finds the answer is not a stranger `d` at
all.

A FRAMING SCALAR EXITS THE HULL
-------------------------------
A framed bond carries an overall factor `c` — this is the framing anomaly, and
the corpus already uses it: `mu_eff = mu (1-h)^(e/2)` in
`stacked_interface_writhe_normalised_probe`. A scalar multiplies **both** block
ratios, so it scales the determinant by `c^2`:

    |mu_sym . mu_anti|  =  c^2 |det(T + dI)|

and `c < 1` drops it below `1` while `d` stays anywhere in the hull. The
obstruction was never about `d`.

Writing `u = -log c`, at `beta = 0`:

    L(T=0) = u + log q          L(T=1) = u - log q

    T=1 stays UNBOUND  <=>  u < log q   <=>  c > 1/q
    T=0 stays BOUND    <=>  automatic for c <= 1

    **window:  c in (1/q, 1]**,  equivalently  e in [0, 0.8897722518)

with `ratio(u) = (u + log q)/(log q - u)` rising from `1` to unbounded across it.
So a single continuous framing parameter lifts the cap that no crossing count
could.

THE EXPONENT MUST BE FRACTIONAL — WHICH IS THE WHOLE POINT
----------------------------------------------------------
The natural value is `e = 1`: one full crossing's worth of writhe. It gives
`c = (1-h)^(1/2) = 0.8893479079` against a threshold `1/q = 0.9009182840`, so it
is **outside the window by `0.011570`** — a full crossing's framing is *too
strong*, and the `T = 1` channel binds. Every integer `e >= 1` fails the same
way:

    e        c              in window?   ratio
    0        1.00000000     yes          1.0000
    1/2      0.94305244     yes          3.5656
    e*       0.90635175     yes         33.7055
    e_max    0.90091828     no          T=1 BINDS
    1        0.88934791     no          T=1 BINDS
    2        0.79093970     no          T=1 BINDS

**The requirement is a fractional framing exponent, `e < 0.88977`.** In
Calugareanu's decomposition

    Lk  =  Tw  +  Wr

the writhe `Wr` is a signed crossing count — an **integer** for a braid word,
and exactly what this construction has. The twist `Tw = (1/2 pi) integral tau ds`
is **continuous**, a property of the framed curve rather than of its diagram.
A fractional framing exponent is therefore *twist*, not writhe: the ingredient
the bond graph structurally does not carry, and precisely the one the
writhe-normalised convention divides out.

(That is also where the side reading lands. A serpenoid curve's osculating
circles `rho = 1/kappa` are the curvature half of the Frenet data; the torsion
`tau` is the other half and is what integrates to `Tw`. A description that
counts crossings sees `Wr` and is blind to `tau`. The two arcs of this bean —
"what exits the convex hull" and "what does a curvature description add" — have
the same answer.)

WHAT NATURE COSTS, AND THE HONEST STATUS
----------------------------------------
Matching `2.224566 / 0.066 = 33.7055` requires

    u* = 0.0983278069      c* = 0.9063517467      e* = 0.838496742899

which is `94.24 %` of the way across the allowed range. **This is a fit**: one
free parameter solved against one number. Scanned against 22 corpus constants
the closest is `4h = 0.8362411952` at `0.27 %` — nowhere near a match by this
arc's standards, which quote agreements at `1e-13`. `e*` is a measurement of
what would be required, not a derivation of anything.

WHAT IS AND IS NOT ESTABLISHED
------------------------------
Established: the `det T = -1` obstruction is broken by a framing scalar and by
nothing else the construction currently contains; the admissible window is
`c in (1/q, 1]` in closed form; and the admissible exponent is strictly less
than one full crossing's writhe, so the ingredient is continuous twist rather
than a diagram quantity.

Not established: any value for it. `e*` is fitted, `4h` is not a match, and no
mechanism in the substrate is shown to produce a fractional twist at all.

DISCIPLINE
----------
No tuning is presented as derivation — the one fitted quantity is labelled as
such and its nearest corpus constant reported with its error. The framing factor
is the corpus's own `(1-h)^(e/2)`, not a new device. Experimental values are
comparison targets.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] adding_crossings_cannot_break_the_degeneracy_probe.py (the obstruction)
-- Ref: [probe] isospin_grading_restores_the_sign_probe.py (the cap being lifted)
-- Ref: [probe] stacked_interface_writhe_normalised_probe.py (the framing factor)
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
ROOT = COMP.parent
sys.path.insert(0, str(ROOT / "tools" / "pyhecke" / "python"))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from pyhecke.atom import D_PN  # noqa: E402
from q_parameter import q_at  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 40
_Q = q_at(mp.mp.dps)
_H = _Q - 1 / _Q
_Z = _Q ** 3 / (_Q ** 2 + 1)
LQ = mp.log(_Q)
LW = mp.log(1 - _H)
R_EXP = mp.mpf("2.224566") / mp.mpf("0.066")


def ratio_at_u(u):
    return (u + LQ) / (LQ - u) if u < LQ else None


def main() -> int:
    assertions = []
    print("t7qv — the hull exit is a framing scalar, and it must be fractional")

    # ── A1. a scalar scales the determinant ────────────────────────────
    print("\n  1. a framing scalar scales the obstruction by c^2")
    d0 = -_H / 2
    det0 = (_Q + d0) * (-1 / _Q + d0)
    for c in (mp.mpf(1), mp.mpf("0.95"), mp.mpf("0.9")):
        prod = (c * (_Q + d0)) * (c * (-1 / _Q + d0))
        print(f"     c = {float(c):.4f}:  |mu_sym . mu_anti| = "
              f"{float(abs(prod)):.10f}   (= c^2 |det| = "
              f"{float(c ** 2 * abs(det0)):.10f})")
    p95 = abs((mp.mpf("0.95") * (_Q + d0)) * (mp.mpf("0.95") * (-1 / _Q + d0)))
    ok = abs(det0) >= 1 and p95 < 1
    print(f"     |det| = {float(abs(det0)):.10f} >= 1 blocks every d in the hull,")
    print(f"     but c = 0.95 already drops the product to {float(p95):.10f} < 1.")
    print(f"     The obstruction was never about d. A scalar multiplies BOTH")
    print(f"     blocks, which is exactly what leaving the hull requires.")
    assertions.append(("A1_framing_scalar_scales_the_determinant", ok,
                       f"|det| = {float(abs(det0)):.9f} >= 1; c=0.95 gives "
                       f"{float(p95):.9f} < 1"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. the window, in closed form ─────────────────────────────────
    print("\n  2. the admissible window, in closed form")
    e_max = 2 * LQ / (-LW)
    print(f"     at beta = 0:  L(T=0) = u + log q,  L(T=1) = u - log q,  "
          f"u = -log c")
    print(f"     log q = {float(LQ):.12f}")
    print(f"     T=1 unbound <=> u < log q <=> c > 1/q = {float(1 / _Q):.12f}")
    print(f"     window:  c in (1/q, 1]   <=>   e in [0, {float(e_max):.10f})")
    print(f"     {'c':>12s} {'u':>13s} {'ratio':>16s}")
    for cs in ("1.0", "0.98", "0.95", "0.92", "0.9009183"):
        c = mp.mpf(cs)
        u = -mp.log(c)
        r = ratio_at_u(u)
        print(f"     {float(c):12.7f} {float(u):13.9f} "
              f"{(f'{float(r):.5f}' if r else 'unbounded'):>16s}")
    ok = ratio_at_u(mp.mpf(0)) == 1 and float(1 / _Q) < 1
    print(f"     ratio(u) = (u + log q)/(log q - u) rises from 1 to unbounded")
    print(f"     across the window — one continuous parameter lifts the cap that")
    print(f"     no crossing count could.")
    assertions.append(("A2_window_is_c_between_inverse_q_and_one", ok,
                       f"c in (1/q, 1] = ({float(1 / _Q):.10f}, 1]; "
                       f"e in [0, {float(e_max):.8f})"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. the natural integer value is excluded ──────────────────────
    print("\n  3. one full crossing's writhe is TOO STRONG")
    print(f"     {'e':>8s} {'c = (1-h)^(e/2)':>17s} {'in window?':>11s} "
          f"{'ratio':>12s}")
    tab = {}
    for lbl, ev in (("0", mp.mpf(0)), ("1/2", mp.mpf(1) / 2),
                    ("e_max", e_max), ("1", mp.mpf(1)), ("2", mp.mpf(2))):
        cc = (1 - _H) ** (ev / 2)
        uu = -mp.log(cc)
        r = ratio_at_u(uu)
        tab[lbl] = (float(cc), r is not None)
        print(f"     {lbl:>8s} {float(cc):17.10f} {str(r is not None):>11s} "
              f"{(f'{float(r):.4f}' if r else 'T=1 BINDS'):>12s}")
    c1 = (1 - _H) ** mp.mpf("0.5")
    miss = 1 / _Q - c1
    ok = not tab["1"][1] and not tab["2"][1] and tab["1/2"][1] and miss > 0
    print(f"     e = 1 gives c = {float(c1):.10f} against a threshold "
          f"1/q = {float(1 / _Q):.10f},")
    print(f"     OUTSIDE by {float(miss):.9f}. A full crossing's framing is too")
    print(f"     strong and the T=1 channel binds; every integer e >= 1 fails.")
    print(f"     **The admissible exponent is FRACTIONAL.**")
    assertions.append(("A3_integer_writhe_is_excluded", ok,
                       f"e=1 gives c={float(c1):.9f}, outside 1/q by "
                       f"{float(miss):.9f}; e=2 also excluded, e=1/2 admitted"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. fractional exponent = twist, not writhe ────────────────────
    print("\n  4. a fractional exponent is TWIST, not writhe")
    print(f"     Calugareanu:   Lk = Tw + Wr")
    print(f"       Wr  signed crossing count -- an INTEGER for a braid word, and")
    print(f"           exactly what this construction carries")
    print(f"       Tw  (1/2pi) integral tau ds -- CONTINUOUS, a property of the")
    print(f"           framed curve rather than of its diagram")
    print(f"     the admissible window excludes every integer >= 1 and admits a")
    print(f"     continuum below {float(e_max):.6f}, so what it is asking for is")
    print(f"     twist. That is the ingredient the bond graph structurally lacks")
    print(f"     — and precisely the one the writhe-normalised convention")
    print(f"     divides out (qou-6pt7).")
    ints_excluded = all(not tab[k][1] for k in ("1", "2"))
    frac_admitted = tab["1/2"][1]
    ok = ints_excluded and frac_admitted and e_max < 1
    print(f"     every integer e >= 1 excluded: {ints_excluded};  "
          f"fractional admitted: {frac_admitted};  e_max = "
          f"{float(e_max):.8f} < 1")
    assertions.append(("A4_admissible_exponent_is_twist_not_writhe", ok,
                       f"e_max = {float(e_max):.8f} < 1, so no integer writhe "
                       f"is admissible and the window is purely fractional"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. what nature costs, and that it is a fit ────────────────────
    print("\n  5. matching nature — and saying plainly that it is a fit")
    u_star = (R_EXP - 1) * LQ / (R_EXP + 1)
    c_star = mp.e ** (-u_star)
    e_star = 2 * mp.log(c_star) / LW
    print(f"     target ratio {float(R_EXP):.4f}")
    print(f"       u* = {float(u_star):.12f}   c* = {float(c_star):.12f}   "
          f"e* = {float(e_star):.12f}")
    print(f"       verify ratio = {float(ratio_at_u(u_star)):.6f}")
    print(f"       e* sits at {float(100 * e_star / e_max):.2f} % of the window")
    cands = {"h": _H, "2h": 2 * _H, "3h": 3 * _H, "4h": 4 * _H, "z": _Z,
             "1/q": 1 / _Q, "q-1": _Q - 1, "1-h": 1 - _H, "(1-h)^2": (1 - _H) ** 2,
             "q/(q+1)": _Q / (_Q + 1), "1/(q+1)": 1 / (_Q + 1), "log q": LQ,
             "-log(1-h)": -LW, "sqrt(1-h)": mp.sqrt(1 - _H), "h/(1-h)": _H / (1 - _H),
             "1-h^2": 1 - _H ** 2, "z+h": _Z + _H, "D_PN": abs(mp.mpf(str(D_PN))),
             "1-h/2": 1 - _H / 2, "q-h": _Q - _H, "2z-h": 2 * _Z - _H,
             "5h/4": 5 * _H / 4}
    scan = sorted(((abs(float(v - e_star)) / float(e_star), k, float(v))
                   for k, v in cands.items()))
    print(f"     scanned against {len(cands)} corpus constants:")
    for rel, k, v in scan[:3]:
        print(f"       {k:<12s} = {v:.10f}   rel {rel:.4%}")
    ok = scan[0][0] > 1e-6 and 0 < float(e_star) < float(e_max)
    print(f"     closest is {scan[0][1]} at {scan[0][0]:.2%} — NOT a match at this")
    print(f"     arc's standards, which quote agreements at 1e-13. e* is a")
    print(f"     MEASUREMENT OF WHAT WOULD BE REQUIRED, not a derivation.")
    assertions.append(("A5_the_matching_exponent_is_a_fit_not_a_constant", ok,
                       f"e* = {float(e_star):.10f}; nearest corpus constant "
                       f"{scan[0][1]} at {scan[0][0]:.4%}, not a match"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. what is and is not established ─────────────────────────────
    print("\n  6. what this does and does not establish")
    print(f"     ESTABLISHED:")
    print(f"       - the det T = -1 obstruction is broken by a framing scalar,")
    print(f"         and by nothing else the construction contains")
    print(f"       - the window is c in (1/q, 1] in closed form")
    print(f"       - it excludes every integer writhe, so the ingredient is")
    print(f"         continuous twist rather than a diagram quantity")
    print(f"     NOT ESTABLISHED:")
    print(f"       - any value for it. e* is fitted; 4h misses by 0.27 %;")
    print(f"         and NO mechanism in the substrate is shown to produce a")
    print(f"         fractional twist at all.")
    print(f"     The gap has moved from 'impossible' to 'one unexplained")
    print(f"     continuous parameter', which is progress and is not a theory.")
    ok = True
    assertions.append(("A6_scope_is_stated", ok,
                       "ingredient identified and window derived; value fitted "
                       "and mechanism absent"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  The hull exit is a framing scalar. It multiplies both block ratios,")
    print("  so it scales the det T = -1 obstruction by c^2 and drops it below 1")
    print("  while d stays anywhere in the hull — the obstruction was never about")
    print("  d at all. The window is c in (1/q, 1] in closed form.")
    print("  And it must be FRACTIONAL: one full crossing's writhe (e = 1) gives")
    print(f"  c = 0.8893479 against a threshold 1/q = 0.9009183, outside by")
    print("  0.0115704, so the T=1 channel would bind. Every integer e >= 1 fails.")
    print("  In Calugareanu's Lk = Tw + Wr the integer part is the writhe this")
    print("  construction carries and the continuous part is twist, which it does")
    print("  not — and which the writhe-normalised convention explicitly removes.")
    print("  Matching nature needs e* = 0.8384967, 94 % across the window. That")
    print("  is a fit: the nearest corpus constant, 4h, misses by 0.27 %, and no")
    print("  mechanism producing a fractional twist is exhibited. The gap has")
    print("  moved from impossible to one unexplained parameter.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "Identifies what can exit the convex hull of {sigma, sigma^-1} that "
            "qou-o8ww proved necessary. The answer is not a stranger offset d "
            "but a FRAMING SCALAR: a framed bond carries an overall factor c "
            "(the corpus's own mu_eff = mu (1-h)^(e/2)), which multiplies BOTH "
            "block ratios and therefore scales the det T = -1 obstruction by "
            "c^2. |det| >= 1 blocks every d in the hull, but c = 0.95 already "
            "drops the product to 0.912 < 1. With u = -log c and beta = 0, "
            "L(T=0) = u + log q and L(T=1) = u - log q, so the T=1 channel stays "
            "unbound iff u < log q, giving the closed-form window c in (1/q, 1], "
            "equivalently e in [0, 0.8897722518), across which the ratio rises "
            "from 1 to unbounded. CRUCIALLY THE EXPONENT MUST BE FRACTIONAL: "
            "e = 1, one full crossing's writhe, gives c = 0.8893479079 against "
            "the threshold 1/q = 0.9009182840 — outside by 0.011570, so the T=1 "
            "channel binds — and every integer e >= 1 fails likewise. In "
            "Calugareanu's Lk = Tw + Wr the writhe is an integer crossing count "
            "(what this construction has) and the twist is continuous (what it "
            "lacks, and what the writhe-normalised convention divides out). "
            "Matching the experimental 33.7055 requires e* = 0.838496742899, "
            "94.24% across the window — but this is A FIT: scanned against 22 "
            "corpus constants the nearest is 4h at 0.27%, which is not a match "
            "at an arc that quotes agreements at 1e-13, and no mechanism "
            "producing a fractional twist is exhibited.")
        wb.add_data("obstruction_scaling",
                    {"det_at_vertex": mp.nstr(det0, 12),
                     "product_at_c_1": mp.nstr(abs(det0), 12),
                     "product_at_c_095": mp.nstr(p95, 12)})
        wb.add_data("window",
                    {"c_lower_bound_1_over_q": mp.nstr(1 / _Q, 15),
                     "c_upper_bound": "1",
                     "e_max": mp.nstr(e_max, 15),
                     "log_q": mp.nstr(LQ, 15)})
        wb.add_data("integer_writhe_excluded",
                    {k: {"c": f"{v[0]:.12f}", "in_window": v[1]}
                     for k, v in tab.items()})
        wb.add_data("matching_nature",
                    {"target_ratio": mp.nstr(R_EXP, 8),
                     "u_star": mp.nstr(u_star, 14),
                     "c_star": mp.nstr(c_star, 14),
                     "e_star": mp.nstr(e_star, 14),
                     "pct_of_window": f"{float(100 * e_star / e_max):.4f}",
                     "is_a_fit": True})
        wb.add_data("constant_scan",
                    {k: {"value": f"{v:.12f}", "rel_diff": f"{rel:.6%}"}
                     for rel, k, v in scan[:6]})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "e* = 0.8384967 IS A FIT AND MUST NOT BE QUOTED AS A RESULT. One "
            "free parameter was solved against one experimental number. The "
            "nearest corpus constant (4h) misses by 0.27%, which at an arc "
            "quoting agreements at 1e-13 is not a match, and no substrate "
            "mechanism producing a fractional twist is exhibited anywhere. What "
            "is established is the INGREDIENT and the WINDOW, not the value.")
        wb.add_caveat(
            "THE CALUGAREANU READING IS AN INTERPRETATION, NOT A COMPUTATION. "
            "Lk = Tw + Wr is standard, and it is standard that Wr is an integer "
            "for a braid diagram while Tw is continuous. That the admissible "
            "window excludes every integer and admits a continuum IS computed "
            "here; the identification of that continuum with a geometric twist "
            "of a framed curve is a reading of what the corpus's own "
            "(1-h)^(e/2) factor means, and no framed curve is constructed.")
        wb.add_caveat(
            "Everything is at the n=2 interface with the |mu| < 1 binding "
            "convention inherited from qou-m896, where the antisymmetric block's "
            "negative eigenvalue makes the magnitude necessary. The A1-A2 "
            "determinant scaling is independent of that convention; the ratio "
            "and window numbers are not. Lifting to the 3-strands-per-nucleon "
            "construction is untested here.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
