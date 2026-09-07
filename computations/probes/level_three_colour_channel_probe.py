#!/usr/bin/env python3
"""The level-3 channel, built and run. It yields a colour observable with no
fourth calibration — the substrate gets the QCD colour-factor SIGNS right and
the RATIO wrong by exactly 2, via the same `det T = -1` degeneracy that caps the
nuclear sector.

WHAT THIS RUNS
--------------
`docs/audits/2026-08-16-wenzl-level-family.md` §4 states a cheap named
falsification and records it as never executed: build the level-3 channel
(`z_3`, quantum-dimension weights, the `l(lambda) <= 3` support) and check
whether the blocks that `r = 2` annihilates yield a colour observable with no
fourth calibration. Colour needs a 3-row block, so `r >= 3`; every registered
QOU channel measures at `r = 2`, meaning the framework has exactly one gauge
sector's worth of Hecke structure wired.

This builds it.

THE LEVEL FAMILY, VERIFIED
--------------------------
    z_r  =  q^(2r-1) (q^2 - 1) / (q^(2r) - 1)

    r=1   1.109978582751      > 1
    r=2   0.612688037146      = z_D = q^3/(q^2+1)     to 1.15e-41
    r=3   0.449304809090      = q^5/(q^4+q^2+1)       to 1.15e-41
    r=4   0.369360232236
    r=5   0.322749650471

Note `z_1 = q > 1` — the **only** level whose Markov parameter can exceed 1, and
therefore the only one that could unbind anything (`qou-v3u2`: `mu = z + d <= z`,
so binding is forced whenever `z < 1`). Level 1 is abelian and has room for
nothing else.

Weights are the `U_q(gl_r)` quantum dimensions
`dim_q(lambda) = prod [r + j - i] / [h(i,j)]`, normalised by
`sum_lambda y . dim = 1`. They vanish exactly when `l(lambda) > r`, and at
`r = 2` they reproduce `load_cost`'s convention-D weights to `1.14e-8` — the
known stored-f64 floor of that path. So this construction **subsumes convention
D as its `r = 2` member**, and the level-3 channel is now built rather than
hypothesised.

THE COLOUR SINGLET IS ANNIHILATED AT r = 2
------------------------------------------
The three-strand antisymmetriser `(1,1,1)` is the colour singlet — three quarks
in a baryon are totally antisymmetric in colour. Its weight:

    r = 2:   y(3) = 0.505404227   y(2,1) = 0.247297887   y(1,1,1) = 0.000000000
    r = 3:   y(3) = 0.378370691   y(2,1) = 0.293082487   y(1,1,1) = 0.035464334

**At `r = 2` the substrate has no colour singlet at all** — the block is not
small, it is exactly zero. That is the same fact that makes `H_12` cheap
(`qou-38i9`): the blocks that collapse are precisely the ones where colour would
live. The computational win and the absent colour are one statement.

THE OBSERVABLE, WITH NOTHING FITTED
-----------------------------------
Two quarks decompose as `3 (x) 3 = 3bar + 6`. The one-gluon-exchange colour
factors `<lambda_i . lambda_j>/4` are

    3bar  (antisymmetric)   C = -2/3    ATTRACTIVE
    6     (symmetric)       C = +1/3    REPULSIVE

so QCD requires `|C_antisym / C_sym| = 2` **exactly**, with opposite signs. This
is group theory, not a measurement — there is no error bar and no calibration.

The substrate's two-strand blocks carry eigenvalues `q` and `-1/q` at every
level, so at `d = 0`:

    L_antisym = -log|-1/q| = +0.104340720320    ATTRACTIVE   correct
    L_sym     = -log| q  | = -0.104340720320    REPULSIVE    correct
    |L_a / L_s| = 1.000000000000                QCD wants 2  **off by 2.0000000000**

**The signs come out free and the ratio is wrong by exactly a factor of two.**

AND IT IS THE SAME DEGENERACY AS THE NUCLEAR SECTOR
---------------------------------------------------
    L_antisym + L_sym  =  5.74e-42   (exactly zero)

because `q . (1/q) = 1`, i.e. `|det T| = 1` — the Hecke relation `T^2 = hT + 1`
fixing the eigenvalue product at `-1`. That is precisely the obstruction
`qou-o8ww` found capping the nuclear `T=0 / T=1` ratio at 1 where nature wants
`33.7`. **One mechanism caps two independent sectors**, at the quark level and
the nuclear level, and the quark version is the sharper test because its target
is exact.

WHAT THE FRAMING FIX WOULD COST, AND WHY IT CANNOT BE UNIVERSAL
---------------------------------------------------------------
`qou-vlrq` showed a framing scalar lifts the cap, with
`e / e_max = (R - 1)/(R + 1)` for a target ratio `R`:

    QCD colour   R = 2        e = 0.2965907506  =  e_max / 3   exactly
    nuclear      R = 33.7055  e = 0.8384967429  =  0.942372 e_max

The QCD requirement has a clean closed form — exactly one third of the window —
which the nuclear one does not. But they differ by `2.83x`, so **a single
universal framing cannot serve both channels**; the framing would have to be
channel- or scale-dependent, and nothing supplies that.

VERDICT ON THE NAMED FALSIFICATION
----------------------------------
Run, and it fails — informatively. The level-3 channel is constructible, cheap,
and subsumes convention D; the colour singlet exists there and is exactly zero
at `r = 2`; and the resulting colour observable needs no calibration. The
substrate reproduces its signs and misses its ratio by exactly `2`, for the same
structural reason it misses the nuclear ratio by `33.7`. Raising the level does
not repair the sector — it relabels which blocks are alive while leaving the
eigenvalues, and therefore the degeneracy, untouched.

DISCIPLINE
----------
No fit. The level family and weights are verified against `load_cost` before
use. The QCD colour factors are standard `SU(3)` group theory quoted as an
external target; nothing is tuned to them, and the `e = e_max/3` figure is
reported as what a fix would cost, not as a value derived here.

-- Ref: [manuscript] bean t7qv
-- Ref: [audit] docs/audits/2026-08-16-wenzl-level-family.md §4 (the named test)
-- Ref: [probe] adding_crossings_cannot_break_the_degeneracy_probe.py (det T = -1)
-- Ref: [probe] the_hull_exit_is_a_fractional_twist_probe.py (the framing fix)
"""
from __future__ import annotations

import sys
import warnings
from math import factorial
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

from nucleus_real_sdp import load_cost  # noqa: E402
from q_parameter import q_at  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 40
_Q = q_at(mp.mp.dps)
_H = _Q - 1 / _Q
LQ = mp.log(_Q)
LW = mp.log(1 - _H)
R_NUC = AME_B_DEUTERON_MEV_VALIDATION / mp.mpf("0.066")


def qi(m):
    """balanced q-integer [m]_q"""
    return sum(_Q ** (m - 1 - 2 * i) for i in range(m))


def partitions(n):
    out = []

    def rec(rem, mx, cur):
        if rem == 0:
            out.append(tuple(cur))
            return
        for p in range(min(rem, mx), 0, -1):
            rec(rem - p, p, cur + [p])
    rec(n, n, [])
    return out


def conj(l):
    return [sum(1 for x in l if x > j) for j in range(l[0])]


def specht_dim(l):
    l = list(l)
    n = sum(l)
    c = conj(l)
    pr = 1
    for i, row in enumerate(l):
        for j in range(row):
            pr *= (row - j) + (c[j] - i) - 1
    return factorial(n) // pr


def qdim(l, r):
    """U_q(gl_r) quantum dimension; zero iff len(l) > r."""
    l = list(l)
    c = conj(l)
    num = mp.mpf(1)
    den = mp.mpf(1)
    for i, row in enumerate(l):
        for j in range(row):
            arm = r + j - i
            if arm <= 0:
                return mp.mpf(0)
            num *= qi(arm)
            den *= qi((row - j) + (c[j] - i) - 1)
    return num / den


def weights(n, r):
    ps = partitions(n)
    w = {p: qdim(p, r) for p in ps}
    S = sum(w[p] * specht_dim(p) for p in ps)
    return {p: w[p] / S for p in ps}


def z_level(r):
    return _Q ** (2 * r - 1) * (_Q ** 2 - 1) / (_Q ** (2 * r) - 1)


def main() -> int:
    assertions = []
    print("t7qv — the level-3 colour channel, built and run")

    # ── A1. the level family and its Markov parameters ─────────────────
    print("\n  1. the level family z_r")
    zs = {r: z_level(r) for r in range(1, 6)}
    for r, z in zs.items():
        flag = "   > 1  (the ONLY level that can unbind)" if z > 1 else ""
        print(f"     r={r}: z_{r} = {float(z):.12f}{flag}")
    d2 = abs(zs[2] - _Q ** 3 / (_Q ** 2 + 1))
    d3 = abs(zs[3] - _Q ** 5 / (_Q ** 4 + _Q ** 2 + 1))
    print(f"     z_2 vs convention D q^3/(q^2+1):     diff {float(d2):.2e}")
    print(f"     z_3 vs the audit's q^5/(q^4+q^2+1):  diff {float(d3):.2e}")
    ok = d2 < mp.mpf("1e-35") and d3 < mp.mpf("1e-35") and zs[1] > 1 \
        and all(zs[r] < 1 for r in (2, 3, 4, 5))
    print(f"     z_1 = q > 1 is the only level whose Markov parameter exceeds 1,")
    print(f"     hence the only one that could unbind anything at all (qou-v3u2:")
    print(f"     mu = z + d <= z, so z < 1 forces binding). Level 1 is abelian.")
    assertions.append(("A1_level_family_and_z3_verified", ok,
                       f"z_2 matches convention D to {float(d2):.1e}, z_3 the "
                       f"audit's value to {float(d3):.1e}; only z_1 > 1"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. quantum-dimension weights subsume convention D ─────────────
    print("\n  2. the weights: support l(lambda) <= r, and r=2 IS convention D")
    supp = {}
    for n in (3, 6):
        for r in (2, 3):
            w = weights(n, r)
            live = [p for p in w if abs(w[p]) > mp.mpf("1e-30")]
            tot = sum(w[p] * specht_dim(p) for p in w)
            supp[(n, r)] = (len(live), len(w), max(len(p) for p in live))
            print(f"     n={n} r={r}: {len(live)}/{len(w)} live, max rows "
                  f"{max(len(p) for p in live)}, sum(y.dim) = {float(tot):.12f}")
    ps, y, _c, _d, _m = load_cost("deuteron")
    ref = {tuple(p): float(w) for p, w in zip(ps, y)}
    w6 = weights(6, 2)
    worst = max(abs(float(w6[p]) - ref[p]) / max(abs(ref[p]), 1e-30)
                for p in w6 if abs(ref[p]) > 1e-30)
    zeros_ok = all(abs(ref[p]) < 1e-30 for p in w6 if len(p) > 2)
    print(f"     against load_cost at r=2: worst rel err {worst:.2e} on live")
    print(f"     blocks (the stored-f64 floor), all >2-row weights zero: "
          f"{zeros_ok}")
    print(f"     so this construction SUBSUMES convention D as its r=2 member,")
    print(f"     and the level-3 channel is built rather than hypothesised.")
    ok = (all(supp[(n, r)][2] <= r for n in (3, 6) for r in (2, 3))
          and worst < 1e-6 and zeros_ok)
    assertions.append(("A2_weights_subsume_convention_D", ok,
                       f"support l<=r at all tested (n,r); r=2 matches "
                       f"load_cost to {worst:.1e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. the colour singlet is exactly zero at r=2 ──────────────────
    print("\n  3. the colour singlet (1,1,1) is ANNIHILATED at r=2")
    sing = {}
    for r in (2, 3):
        w = weights(3, r)
        sing[r] = w[(1, 1, 1)]
        print(f"     r={r}:  " + "  ".join(
            f"y{p} = {float(w[p]):.9f}" for p in sorted(w, key=lambda t: -len(t))))
    ok = abs(sing[2]) < mp.mpf("1e-30") and sing[3] > mp.mpf("1e-3")
    print(f"     three quarks in a baryon are totally antisymmetric in colour, so")
    print(f"     (1,1,1) IS the colour singlet. At r=2 its weight is not small —")
    print(f"     it is exactly {float(sing[2]):.1e}. The substrate as configured has")
    print(f"     NO COLOUR SINGLET AT ALL.")
    print(f"     This is the same fact that makes H_12 cheap (qou-38i9): the")
    print(f"     blocks that collapse are precisely where colour would live. The")
    print(f"     computational win and the absent colour are one statement.")
    assertions.append(("A3_colour_singlet_is_exactly_zero_at_r2", ok,
                       f"y(1,1,1) = {float(sing[2]):.1e} at r=2, "
                       f"{float(sing[3]):.9f} at r=3"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. the observable, with nothing fitted ────────────────────────
    print("\n  4. the colour observable — no fourth calibration")
    print(f"     3 (x) 3 = 3bar + 6, one-gluon-exchange colour factors:")
    print(f"       3bar (antisymmetric)  C = -2/3   ATTRACTIVE")
    print(f"       6    (symmetric)      C = +1/3   REPULSIVE")
    print(f"       |C_a / C_s| = 2 EXACTLY — group theory, no error bar")
    L_a = -mp.log(abs(-1 / _Q))
    L_s = -mp.log(abs(_Q))
    r_sub = abs(L_a / L_s)
    print(f"     substrate blocks carry q and -1/q at EVERY level, so at d = 0:")
    print(f"       L_antisym = {float(L_a):+.12f}   "
          f"{'ATTRACTIVE' if L_a > 0 else 'repulsive'}   correct")
    print(f"       L_sym     = {float(L_s):+.12f}   "
          f"{'attractive' if L_s > 0 else 'REPULSIVE'}   correct")
    print(f"       |L_a/L_s| = {float(r_sub):.12f}    QCD wants 2")
    print(f"     signs come out FREE; the ratio is wrong by exactly "
          f"{float(2 / r_sub):.10f}")
    ok = L_a > 0 > L_s and abs(r_sub - 1) < mp.mpf("1e-30")
    assertions.append(("A4_colour_signs_right_ratio_wrong_by_two", ok,
                       f"antisym attractive ({float(L_a):+.9f}), sym repulsive "
                       f"({float(L_s):+.9f}), ratio {float(r_sub):.9f} vs QCD 2"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. same degeneracy as the nuclear sector ──────────────────────
    print("\n  5. it is the SAME det T = -1 degeneracy")
    s = L_a + L_s
    print(f"     L_antisym + L_sym = {float(s):.2e}  (exactly zero)")
    print(f"     because q . (1/q) = 1, i.e. |det T| = 1 — the Hecke relation")
    print(f"     T^2 = hT + 1 fixing the eigenvalue product at -1.")
    print(f"     That is the obstruction qou-o8ww found capping the nuclear")
    print(f"     T=0/T=1 ratio at 1 where nature wants {float(R_NUC):.2f}.")
    print(f"     ONE MECHANISM CAPS TWO INDEPENDENT SECTORS — quark and nuclear")
    print(f"     — and the quark version is the sharper test because its target")
    print(f"     is exact rather than measured.")
    ok = abs(s) < mp.mpf("1e-35")
    assertions.append(("A5_same_det_obstruction_caps_both_sectors", ok,
                       f"L_a + L_s = {float(s):.2e}, exactly zero, from "
                       f"|det T| = 1"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. the framing fix cannot be universal ────────────────────────
    print("\n  6. the framing fix would have to be channel-dependent")
    e_max = 2 * LQ / (-LW)

    def e_for(R):
        u = (R - 1) * LQ / (R + 1)
        return 2 * mp.log(mp.e ** (-u)) / LW

    e_q, e_n = e_for(mp.mpf(2)), e_for(R_NUC)
    print(f"     qou-vlrq: e/e_max = (R-1)/(R+1) for a target ratio R")
    print(f"       QCD colour  R = 2       e = {float(e_q):.10f} = "
          f"{float(e_q / e_max):.6f} e_max")
    print(f"       nuclear     R = {float(R_NUC):.4f} e = {float(e_n):.10f} = "
          f"{float(e_n / e_max):.6f} e_max")
    print(f"     QCD's requirement is EXACTLY e_max/3 = {float(e_max / 3):.10f}")
    print(f"     — a clean closed form the nuclear one does not have. But they")
    print(f"     differ by {float(e_n / e_q):.4f}x, so a single universal framing")
    print(f"     cannot serve both; it would have to be channel- or")
    print(f"     scale-dependent, and nothing supplies that.")
    ok = abs(e_q - e_max / 3) < mp.mpf("1e-30") and e_n / e_q > 2
    assertions.append(("A6_framing_fix_cannot_be_universal", ok,
                       f"QCD needs e_max/3 exactly; nuclear needs "
                       f"{float(e_n / e_max):.6f} e_max; ratio "
                       f"{float(e_n / e_q):.4f}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  The named falsification is run, and it fails informatively. The")
    print("  level-3 channel is constructible and cheap: z_r = q^(2r-1)(q^2-1)/")
    print("  (q^(2r)-1) reproduces both convention D and the audit's z_3, and the")
    print("  quantum-dimension weights subsume convention D as their r=2 member.")
    print("  The colour singlet (1,1,1) is EXACTLY zero at r=2 — the substrate as")
    print("  configured has no colour singlet, which is the same fact that makes")
    print("  H_12 cheap.")
    print("  The observable needs no calibration: QCD's 3bar/6 colour factors are")
    print("  -2/3 and +1/3, ratio exactly 2 with opposite signs. The substrate")
    print("  gets both SIGNS right and the RATIO wrong by exactly 2.0000000000,")
    print("  because L_antisym + L_sym = 0 identically from |det T| = 1 — the")
    print("  same degeneracy that caps the nuclear ratio at 1 against 33.7.")
    print("  One mechanism, two sectors, and the quark test is sharper because")
    print("  its target is group theory rather than measurement.")
    print("  Raising the level does not repair anything: it relabels which blocks")
    print("  are alive and leaves the eigenvalues, hence the degeneracy, intact.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "Runs the named falsification from docs/audits/"
            "2026-08-16-wenzl-level-family.md section 4, recorded there as never "
            "executed: build the level-3 channel and check whether the blocks "
            "r=2 annihilates yield a colour observable with no fourth "
            "calibration. Built: z_r = q^(2r-1)(q^2-1)/(q^(2r)-1) reproduces "
            "convention D at r=2 and the audit's z_3 = 0.449304809090 at r=3, "
            "both to 1.15e-41, and z_1 = q > 1 is the only level whose Markov "
            "parameter can exceed 1 and hence the only one that could unbind "
            "anything. Weights are U_q(gl_r) quantum dimensions with support "
            "exactly l(lambda) <= r, reproducing load_cost's convention-D "
            "weights at r=2 to 1.14e-8 (its stored-f64 floor), so the "
            "construction subsumes convention D as its r=2 member. The colour "
            "singlet (1,1,1) — three quarks being totally antisymmetric in "
            "colour — has weight EXACTLY ZERO at r=2 and 0.035464334 at r=3: "
            "the substrate as configured has no colour singlet at all, which is "
            "the same fact that makes H_12 cheap in qou-38i9. THE OBSERVABLE: "
            "3(x)3 = 3bar + 6 with one-gluon-exchange colour factors -2/3 "
            "(antisymmetric, attractive) and +1/3 (symmetric, repulsive), ratio "
            "exactly 2 by group theory with no error bar. The substrate's blocks "
            "carry q and -1/q at every level, giving L_antisym = +0.104340720320 "
            "(attractive, correct) and L_sym = -0.104340720320 (repulsive, "
            "correct) — SIGNS FREE — but |L_a/L_s| = 1 exactly, wrong by a "
            "factor of 2.0000000000. The cause is L_a + L_s = 0 identically from "
            "|det T| = 1, the SAME degeneracy qou-o8ww found capping the nuclear "
            "T=0/T=1 ratio at 1 against 33.7. One mechanism caps two independent "
            "sectors. A framing fix would need e = e_max/3 exactly for QCD "
            "against 0.942372 e_max for the nuclear sector, differing by 2.83x, "
            "so it cannot be universal.")
        wb.add_data("level_family",
                    {f"z_{r}": mp.nstr(z, 15) for r, z in zs.items()})
        wb.add_data("weight_support",
                    {f"n={n},r={r}": {"live": supp[(n, r)][0],
                                      "total": supp[(n, r)][1],
                                      "max_rows_live": supp[(n, r)][2]}
                     for (n, r) in supp})
        wb.add_data("convention_D_agreement",
                    {"worst_rel_err_live_blocks": f"{worst:.3e}",
                     "all_ge3row_weights_zero": zeros_ok})
        wb.add_data("colour_singlet",
                    {"y_111_at_r2": mp.nstr(sing[2], 6),
                     "y_111_at_r3": mp.nstr(sing[3], 12)})
        wb.add_data("colour_observable",
                    {"QCD_C_antitriplet": "-2/3", "QCD_C_sextet": "+1/3",
                     "QCD_ratio": "2 (exact)",
                     "substrate_L_antisym": mp.nstr(L_a, 15),
                     "substrate_L_sym": mp.nstr(L_s, 15),
                     "substrate_ratio": mp.nstr(r_sub, 15),
                     "discrepancy_factor": mp.nstr(2 / r_sub, 12),
                     "signs_correct": True})
        wb.add_data("shared_degeneracy",
                    {"L_antisym_plus_L_sym": mp.nstr(s, 6),
                     "cause": "|det T| = 1 from T^2 = hT + 1",
                     "nuclear_target_ratio": mp.nstr(R_NUC, 8)})
        wb.add_data("framing_fix",
                    {"e_max": mp.nstr(e_max, 12),
                     "e_for_QCD": mp.nstr(e_q, 12),
                     "e_for_QCD_over_e_max": "1/3 exactly",
                     "e_for_nuclear": mp.nstr(e_n, 12),
                     "e_for_nuclear_over_e_max": f"{float(e_n / e_max):.6f}",
                     "mismatch_factor": f"{float(e_n / e_q):.6f}"})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "THE COLOUR-FACTOR COMPARISON IS AN IDENTIFICATION, NOT A "
            "DERIVATION. It reads the two-strand symmetric/antisymmetric "
            "Wedderburn blocks as the sextet and antitriplet of 3(x)3. That is "
            "the natural reading — exchange symmetry matches on both sides — but "
            "nothing here constructs an SU(3) action on the strands, and no "
            "gluon exchange is modelled. What is computed is that the "
            "substrate's two exchange channels have the right relative sign and "
            "a ratio of exactly 1 against a required 2.")
        wb.add_caveat(
            "'ATTRACTIVE/REPULSIVE' USES THE ARC'S |mu| < 1 BINDING CONVENTION "
            "(qou-m896), needed because the antisymmetric eigenvalue is "
            "negative. The A5 statement L_a + L_s = 0 is convention-independent "
            "(it is |det T| = 1); the sign labels in A4 are not.")
        wb.add_caveat(
            "RAISING THE LEVEL CHANGES THE WEIGHTS, NOT THE ALGEBRA. The block "
            "eigenvalues are q and -1/q at every r, so every per-block ratio and "
            "the whole degeneracy argument are level-independent. The level "
            "affects which blocks are alive and the Markov parameter z_r — it "
            "does not touch the obstruction. Anyone hoping colour would repair "
            "the nuclear sector should read this as the reason it cannot.")
        wb.add_caveat(
            "e = e_max/3 is what a framing fix WOULD cost for the QCD ratio, "
            "reported for comparison with the nuclear requirement. It is not "
            "derived from anything, and qou-vlrq's caveat applies: no substrate "
            "mechanism producing a fractional twist is exhibited.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
