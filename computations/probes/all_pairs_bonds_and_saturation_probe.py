#!/usr/bin/env python3
"""All pairs, not a chain — and the falloff is SATURATION, not distance decay.

WHAT WAS ASKED
--------------
Owner, on the bond topology: *"I think we want it between all pairs. it might be
highly concentrated on adjacent pairs but then falls away quickly (rate
depending on the type of bond)."* And on method: the tower carries all the
information but only degree 0 is observable through the trace, so a
higher-order operator is reached indirectly — measure the constituents, measure
the atom, subtract. That is exactly the construction here: `L :=
log(tr_M(free) / tr_M(atom))`, a difference of two degree-0 observables.

Both halves of the topology call are tested. The first is right. The second is
right in effect but wrong in mechanism, and the mechanism matters.

THE NON-ADJACENT BOND, BUILT HONESTLY
---------------------------------------
The adjacent bond is `T_{3k+2}` — the last strand of block `k` crossing the
first strand of block `k+1`. The distance-2 analogue is the braid **band
generator**

    a  =  (T_5 T_4 T_3) (T_2 + d) (T_3 T_4 T_5)^-1 ,     T^-1 = T - h

whose underlying permutation conjugates `(2,3)` to `(2,6)`: strand 2, the last
of block 0, crossing strand 6, the first of block 2. So it is the same crossing,
carried across the intervening block, with no free parameter.

RESULT 1 — THERE IS NO INTRINSIC DISTANCE DECAY
--------------------------------------------------
A distance-2 bond **in isolation** contributes *exactly* what the adjacent one
does:

    3H   far bond p-n alone   L = 0.676821592   (adjacent p-n: 0.676821592)
    3He  far bond p-p alone   L = 0.489899384   (adjacent p-p: 0.489899384)

Ratio `1.000000` in both cases. The band generator is a conjugate of `T_2`, and
the Markov trace does not see how far the band reaches. So a bond that "falls
away with distance" is **not** what the braid produces on its own — any such
decay would have to be put in by hand.

RESULT 2 — BUT THE FALLOFF IS REAL, AS SATURATION
----------------------------------------------------
It appears only in combination. With the adjacent bonds already present, the
*marginal* contribution of the far bond is suppressed:

    3H    L(adjacent only) 1.584083858   +far -> 2.017810479
          marginal 0.433726621  against 0.676821592 alone   =  0.640829
    3He   L(adjacent only) 1.353643185   +far -> 1.676935518
          marginal 0.323292333  against 0.489899384 alone   =  0.659916

**Suppression ~0.65, and nearly type-independent** — 0.6408 for the `p-n` far
bond against 0.6599 for the `p-p` one, differing by 2.9 %. Measured, not fitted.

So the owner's picture is right in outcome — long-range pairs count for much
less than adjacent ones — but the cause is not a decay in the bond. It is that
the bonds do not commute: adjacent bonds sit at generators `3k+2`, three apart
and therefore commuting, while the band generator spans generators 3, 4, 5 and
overlaps both the middle nucleon and the second adjacent bond. Saturation, not
distance.

RESULT 3 — WHICH NARROWS MY OWN PREVIOUS CLAIM
-------------------------------------------------
`binding_lp_with_inter_nucleon_bonds_probe.py` reported that `L` is *exactly*
additive over bonds, residual `4.4e-16`. That is true **only over the adjacent
chain**, for the commutation reason above. Once the band generator is included
the residual is `2.4e-1` at `3H` and `1.7e-1` at `3He` — nine orders worse.
**The claim is hereby narrowed to: `L` is exactly additive over ADJACENT
bonds.** The per-bond constants `L_pn`, `L_nn`, `L_pp` stand; the additive law
built on them does not extend to all pairs.

RESULT 4 — ALL PAIRS IS THE BETTER MODEL
-------------------------------------------
Using measured all-pairs values (not naive sums), against experiment (AME
read-only, nothing tuned):

    model              2H/3He              3H/3He
    chain (adjacent)   0.50000  (+73.5 %)  1.17024  ( +6.5 %)
    all pairs          0.40361  (+40.0 %)  1.20327  ( +9.5 %)
    EXPERIMENT         0.28823             1.09896

All-pairs nearly halves the `A`-scaling error, 73.5 % to 40.0 %, and costs three
points on the mirror ratio, 6.5 % to 9.5 %. **Net, the owner's call is
supported**: all pairs is the better topology, and it also happens to be what
`atom_gen_chains` already does, against `atom_braid_word_3A`'s chain. The
inconsistency between those two builders is therefore not cosmetic — it is a
choice with a measurable consequence, and the evidence here favours the
all-pairs one.

RESULT 5 — AND NEITHER IS RIGHT
----------------------------------
Solving each ratio for a single distance-2 weight `f`:

    from 2H/3He :  f = +2.030134
    from 3H/3He :  f = -0.696951

Wildly inconsistent, and one of them negative. **No single distance weight fits
both ratios**, so a one-parameter falloff is refuted outright. Per-bond-type
rates would be two unknowns against two ratios — exactly determined, i.e. a fit
with zero predictive content at this size. Distinguishing them needs `A = 4`,
which is out of reach here: `H_12` has 77 partitions with Specht dimensions to
2673 and the dense seminormal route does not scale to it.

DISCIPLINE
----------
No fit; nothing wired. The band generator has no adjustable content — it is the
standard BKL band, verified by its permutation. `B_AME` is read for the two
ratio comparisons only, and no quantity is tuned to it. The `~1e-8` agreement
floor throughout is the stored f64 `y_lambda` table's precision.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] binding_lp_with_inter_nucleon_bonds_probe.py (additivity narrowed)
-- Ref: [code] pyhecke.atom.atom_gen_chains (all pairs), atom_braid_word_3A (chain)
"""
from __future__ import annotations

import math
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
import numpy as np  # noqa: E402

from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE3_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)
from hecke_characters import build_seminormal_matrices  # noqa: E402
from nucleus_real_sdp import load_cost  # noqa: E402
from pyhecke.atom import D_PN  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 30
_Q = mp.mpf(str(Q0))
_H = _Q - 1 / _Q
HF = float(_H)
DPN = float(D_PN)
B_P = (0.0, 0.5, 0.5)
B_N = (0.5, 0.5, 1.0)


def nucleon_word(betas, g0: int, g1: int):
    w = []
    for _ in range(3):
        w += [(1, 0.0, g0), (1, -HF, g1)]
    w += [(1, -betas[0] * HF, g0), (1, -betas[1] * HF, g0),
          (1, -betas[2] * HF, g1)]
    return w + [(1, 0.0, g0), (1, 0.0, g0)]


def bond_cd(a: str, b: str):
    if a == b == "p":
        return (1, 0.0)
    if a == b == "n":
        return (1, -HF)
    return (1, DPN)


def band(d: float):
    """(T5 T4 T3)(T2 + d)(T3 T4 T5)^-1 — strand 2 crossing strand 6."""
    return [(1, 0.0, 5), (1, 0.0, 4), (1, 0.0, 3), (1, d, 2),
            (1, -HF, 3), (1, -HF, 4), (1, -HF, 5)]


def band_permutation(n: int = 9):
    """Underlying permutation of the band word — should be the (2,6) swap."""
    p = list(range(n))
    for g in (5, 4, 3, 2, 3, 4, 5):
        p[g], p[g + 1] = p[g + 1], p[g]
    return p


_BLK: dict = {}


def blocks(name: str):
    if name not in _BLK:
        parts, y, _c, _d, _m = load_cost(name)
        _BLK[name] = [
            (y[i], [np.asarray(m, dtype=float)
                    for m in build_seminormal_matrices(list(p))[0]])
            for i, p in enumerate(parts)]
    return _BLK[name]


def trM(blks, word):
    tot = 0.0
    for wt, s in blks:
        d = s[0].shape[0]
        m = np.eye(d)
        for c, dd, g in word:
            m = m @ (c * s[g] + dd * np.eye(d))
        tot += wt * float(np.trace(m))
    return tot


def setup(order):
    blks = blocks("tritium")
    base = []
    for k, x in enumerate(order):
        base += nucleon_word(B_P if x == "p" else B_N, 3 * k, 3 * k + 1)
    tf = trM(blks, base)
    adj = []
    for k in range(len(order) - 1):
        c, d = bond_cd(order[k], order[k + 1])
        adj.append((c, d, 3 * k + 2))
    _c, dfar = bond_cd(order[0], order[2])
    return blks, base, tf, adj, band(dfar), order[0] + order[2]


def main() -> int:
    assertions = []
    print("t7qv — all pairs, and where the falloff actually is")

    # ── A1. the band generator is the right long-range crossing ───────
    print("\n  1. the distance-2 bond is the braid band generator")
    perm = band_permutation()
    moved = [i for i, v in enumerate(perm) if v != i]
    ok = sorted(moved) == [2, 6] and perm[2] == 6 and perm[6] == 2
    print(f"     a = (T5 T4 T3)(T2 + d)(T3 T4 T5)^-1,  T^-1 = T - h")
    print(f"     its permutation moves only {moved} — the (2,6) swap")
    print(f"     strand 2 = last of block 0, strand 6 = first of block 2")
    print(f"     no free parameter: same crossing, carried across the middle")
    assertions.append(("A1_band_generator_is_the_right_crossing", ok,
                       f"permutation moves exactly {moved}, a (2,6) transposition"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. no intrinsic distance decay ───────────────────────────────
    print("\n  2. a far bond ALONE contributes exactly what an adjacent one does")
    solo, ratios_solo = {}, {}
    for order, lbl in ((["p", "n", "n"], "3H"), (["p", "n", "p"], "3He")):
        blks, base, tf, adj, far, typ = setup(order)
        L_far = math.log(tf / trM(blks, base + far))
        # its adjacent counterpart, same type, measured on the same nucleus
        c, d = bond_cd(typ[0], typ[1])
        L_adj_same = math.log(tf / trM(blks, base + [(c, d, 2)]))
        solo[lbl] = (typ, L_far, L_adj_same)
        ratios_solo[lbl] = L_far / L_adj_same
        print(f"     {lbl:<4s} far bond ({typ}) alone     L = {L_far:.12f}")
        print(f"          adjacent, same type     L = {L_adj_same:.12f}"
              f"   ratio {L_far / L_adj_same:.9f}")
    ok = all(abs(r - 1) < 1e-8 for r in ratios_solo.values())
    print(f"     ratio 1 to {max(abs(r - 1) for r in ratios_solo.values()):.0e} — "
          f"the Markov trace does not see the distance")
    assertions.append(("A2_no_intrinsic_distance_decay", ok,
                       f"far/adjacent ratios "
                       f"{ {k: f'{v:.9f}' for k, v in ratios_solo.items()} }"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. the falloff is saturation ─────────────────────────────────
    print("\n  3. the falloff appears only in combination — SATURATION")
    sat, tab = {}, {}
    for order, lbl in ((["p", "n", "n"], "3H"), (["p", "n", "p"], "3He")):
        blks, base, tf, adj, far, typ = setup(order)
        L_adj = math.log(tf / trM(blks, base + adj))
        L_far = math.log(tf / trM(blks, base + far))
        L_all = math.log(tf / trM(blks, base + adj + far))
        marg = L_all - L_adj
        sat[lbl] = marg / L_far
        tab[lbl] = (L_adj, L_far, L_all, marg)
        print(f"     {lbl:<4s} adjacent only {L_adj:.9f} -> all pairs "
              f"{L_all:.9f}")
        print(f"          marginal of far {marg:.9f}  against {L_far:.9f} "
              f"alone  =  {sat[lbl]:.6f}")
    spread = abs(sat["3H"] / sat["3He"] - 1)
    ok = all(0.5 < v < 0.8 for v in sat.values()) and spread < 0.05
    print(f"     suppression {sat['3H']:.6f} (p-n far) vs {sat['3He']:.6f} "
          f"(p-p far), differ {100 * spread:.2f} %")
    print(f"     cause: adjacent bonds sit at gens 3k+2, three apart, so they")
    print(f"     COMMUTE; the band spans gens 3,4,5 and overlaps both the middle")
    print(f"     nucleon and the second adjacent bond. Saturation, not distance.")
    assertions.append(("A3_falloff_is_saturation", ok,
                       f"marginal/isolated = {sat['3H']:.6f} and "
                       f"{sat['3He']:.6f}, nearly type-independent "
                       f"({100 * spread:.2f}% apart)"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. narrowing my own previous additivity claim ────────────────
    print("\n  4. narrowing the previous probe: additive over ADJACENT bonds only")
    res_adj, res_all = 0.0, 0.0
    for order, lbl in ((["p", "n", "n"], "3H"), (["p", "n", "p"], "3He")):
        blks, base, tf, adj, far, typ = setup(order)
        singles_adj = [math.log(tf / trM(blks, base + [a])) for a in adj]
        L_adj = math.log(tf / trM(blks, base + adj))
        res_adj = max(res_adj, abs(L_adj - sum(singles_adj)))
        singles_all = singles_adj + [math.log(tf / trM(blks, base + far))]
        L_all = math.log(tf / trM(blks, base + adj + far))
        res_all = max(res_all, abs(L_all - sum(singles_all)))
        print(f"     {lbl:<4s} adjacent : sum {sum(singles_adj):.12f} vs "
              f"{L_adj:.12f}   |d| {abs(L_adj - sum(singles_adj)):.1e}")
        print(f"          all pairs: sum {sum(singles_all):.12f} vs "
              f"{L_all:.12f}   |d| {abs(L_all - sum(singles_all)):.1e}")
    ok = res_adj < 1e-12 and res_all > 1e-2
    print(f"     adjacent residual {res_adj:.1e}; all-pairs residual "
          f"{res_all:.1e} — nine orders worse")
    print(f"     the previous probe's 'exactly additive over bonds' is NARROWED")
    print(f"     to 'over adjacent bonds'. The per-bond constants stand.")
    assertions.append(("A4_additivity_only_over_adjacent", ok,
                       f"adjacent residual {res_adj:.2e}, all-pairs residual "
                       f"{res_all:.2e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. all pairs is the better topology ──────────────────────────
    print("\n  5. all pairs beats the chain on A-scaling")
    b2 = float(AME_B_DEUTERON_MEV_VALIDATION)
    b3h = float(AME_B_TRITIUM_MEV_VALIDATION)
    b3he = float(AME_B_HE3_MEV_VALIDATION)
    L2 = 0.676821586741                       # 2H, its single p-n bond
    e_a, e_m = b2 / b3he, b3h / b3he
    out = {}
    print(f"     {'model':<18s} {'2H/3He':>18s} {'3H/3He':>18s}")
    for lbl, i in (("chain (adjacent)", 0), ("all pairs", 2)):
        ra, rm = L2 / tab["3He"][i], tab["3H"][i] / tab["3He"][i]
        out[lbl] = (ra, rm, 100 * (ra / e_a - 1), 100 * (rm / e_m - 1))
        print(f"     {lbl:<18s} {ra:8.5f} ({out[lbl][2]:+6.1f}%) "
              f"{rm:8.5f} ({out[lbl][3]:+6.1f}%)")
    print(f"     {'EXPERIMENT':<18s} {e_a:8.5f}           {e_m:8.5f}")
    better_a = abs(out["all pairs"][2]) < abs(out["chain (adjacent)"][2])
    worse_m = abs(out["all pairs"][3]) > abs(out["chain (adjacent)"][3])
    ok = better_a and worse_m
    print(f"     all pairs nearly halves the A-scaling error (73.5 -> 40.0 %)")
    print(f"     and costs three points on the mirror (6.5 -> 9.5 %). Net, the")
    print(f"     owner's call is supported — and it is what atom_gen_chains does.")
    assertions.append(("A5_all_pairs_better_on_A_scaling", ok,
                       f"chain {out['chain (adjacent)'][2]:+.1f}%/"
                       f"{out['chain (adjacent)'][3]:+.1f}%, all pairs "
                       f"{out['all pairs'][2]:+.1f}%/{out['all pairs'][3]:+.1f}%"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. no single distance weight fits both ratios ────────────────
    print("\n  6. and no single distance weight fits both ratios")
    L_pn, L_pp, L_nn = 0.676821592386, 0.489899384255, 0.907262265533
    f_a = (L_pn / e_a - 2 * L_pn) / L_pp
    f_m = (e_m * 2 * L_pn - (L_pn + L_nn)) / (L_pn - e_m * L_pp)
    ok = abs(f_a - f_m) > 1.0 and f_m < 0
    print(f"     solving 2H/3He for f : f = {f_a:+.6f}")
    print(f"     solving 3H/3He for f : f = {f_m:+.6f}   (negative)")
    print(f"     a ONE-parameter falloff is refuted outright. Per-type rates")
    print(f"     would be 2 unknowns against 2 ratios — exactly determined,")
    print(f"     i.e. a fit with no predictive content at this size.")
    print(f"     Separating them needs A = 4: H_12, 77 partitions, Specht dims")
    print(f"     to 2673 — out of reach for the dense seminormal route.")
    assertions.append(("A6_no_single_falloff_fits_both", ok,
                       f"f = {f_a:+.4f} from A-scaling vs {f_m:+.4f} from the "
                       f"mirror, one of them negative"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  All pairs: supported. It nearly halves the A-scaling error against")
    print("  the chain and costs three points on the mirror.")
    print("  Falloff: real, but not what it looked like. A far bond ALONE")
    print("  contributes exactly what an adjacent one does — the band generator")
    print("  is a conjugate of T_2 and the trace cannot see the distance. The")
    print("  suppression appears only in combination, at ~0.65 and nearly")
    print("  type-independent, because adjacent bonds commute with each other")
    print("  and the band does not. Saturation, not decay.")
    print("  Which also narrows my last claim: L is exactly additive over")
    print("  ADJACENT bonds (4e-16), not over all pairs (2e-1).")
    print("  And neither topology is right: no single distance weight fits both")
    print("  ratios (+2.03 against -0.70), so the remaining freedom is per-type")
    print("  rates — two unknowns for two numbers, which A=3 cannot test.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "Tests the owner's call that inter-nucleon bonds should run between "
            "ALL pairs with a falloff. The non-adjacent bond is built as the "
            "braid band generator (T5 T4 T3)(T2 + d)(T3 T4 T5)^-1, verified by "
            "its permutation to be the (2,6) swap — last strand of block 0 to "
            "first of block 2 — with no free parameter. A far bond in "
            "ISOLATION contributes exactly what an adjacent one does (ratio 1 "
            "to 1e-8), since the band is a conjugate of T_2 and the Markov "
            "trace does not see the distance: there is no intrinsic distance "
            "decay. The falloff appears only in combination, as SATURATION: "
            "with the adjacent bonds present the far bond's marginal "
            "contribution drops to 0.640829 (p-n) and 0.659916 (p-p) of its "
            "isolated value, nearly type-independent at 2.9% apart, because "
            "adjacent bonds sit at generators 3k+2 and commute while the band "
            "spans 3,4,5 and does not. This narrows the previous probe's claim: "
            "L is exactly additive over ADJACENT bonds (residual 4e-16) but not "
            "over all pairs (2e-1). Against experiment, all-pairs gives 2H/3He "
            "0.40361 (+40.0%) and 3H/3He 1.20327 (+9.5%) against the chain's "
            "0.50000 (+73.5%) and 1.17024 (+6.5%), so all pairs is the better "
            "topology overall — and is what atom_gen_chains already does. But "
            "no single distance weight fits both ratios (+2.03 from A-scaling, "
            "-0.70 from the mirror), refuting a one-parameter falloff.")
        wb.add_data("band_generator",
                    {"word": "(T5 T4 T3)(T2 + d)(T3 T4 T5)^-1",
                     "permutation_moves": moved})
        wb.add_data("far_alone_over_adjacent",
                    {k: f"{v:.12f}" for k, v in ratios_solo.items()})
        wb.add_data("saturation", {k: f"{v:.9f}" for k, v in sat.items()})
        wb.add_data("L_values",
                    {k: {"adjacent": f"{v[0]:.12f}", "far_alone": f"{v[1]:.12f}",
                         "all_pairs": f"{v[2]:.12f}", "marginal": f"{v[3]:.12f}"}
                     for k, v in tab.items()})
        wb.add_data("additivity_residuals",
                    {"adjacent": f"{res_adj:.3e}", "all_pairs": f"{res_all:.3e}"})
        wb.add_data("ratio_table",
                    {k: {"2H/3He": f"{v[0]:.6f}", "3H/3He": f"{v[1]:.6f}",
                         "err_a_pct": f"{v[2]:+.2f}", "err_m_pct": f"{v[3]:+.2f}"}
                     for k, v in out.items()})
        wb.add_data("experiment", {"2H/3He": f"{e_a:.6f}", "3H/3He": f"{e_m:.6f}"})
        wb.add_data("single_f_solutions", {"from_A_scaling": f"{f_a:+.6f}",
                                           "from_mirror": f"{f_m:+.6f}"})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "THE OWNER'S FALLOFF IS CONFIRMED IN OUTCOME BUT NOT IN MECHANISM, "
            "and the difference is testable. A distance decay put into the bond "
            "would suppress a far bond even in isolation; saturation does not — "
            "it suppresses only the marginal contribution once neighbours are "
            "present. These predict different things at A >= 4, where a nucleon "
            "can have several far neighbours at several distances, so the two "
            "readings are separable in principle even though A = 3 cannot "
            "separate them.")
        wb.add_caveat(
            "NARROWS binding_lp_with_inter_nucleon_bonds_probe.py, which "
            "reported L exactly additive over bonds at 4.4e-16. That holds only "
            "over the adjacent chain, whose bonds commute. The per-bond "
            "constants L_pn, L_nn, L_pp are unaffected and still measured, but "
            "the additive law built on them does not extend to all pairs.")
        wb.add_caveat(
            "Only two independent ratios exist at A <= 3, so any model with two "
            "or more free falloff parameters is exactly determined by them and "
            "predicts nothing. The one-parameter version is refuted here; the "
            "per-type version is untestable without A = 4, which needs H_12 "
            "(77 partitions, Specht dimensions to 2673) and does not fit the "
            "dense seminormal route used throughout this series.")
        out_p = wb.save()
        print(f"\nWitness: {out_p}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
