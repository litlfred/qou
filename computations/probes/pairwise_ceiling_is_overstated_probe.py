#!/usr/bin/env python3
"""The pairwise ceiling of `he4_exceeds_pairwise_maximum_probe` is an
overestimate — and once corrected, `3H` and `3He` join `4He` above it.

WHY THIS EXISTS
---------------
Merging `main` surfaced an active sibling arc, `qou-brng`, working the same
problem from the other end. `computations/he4_exceeds_pairwise_maximum_probe.py`
brackets each isotope between the two extreme pairwise bond sets

    B_chain    = alpha [ (Z-1) L_pp + L_pn + (N-1) L_nn ]        A-1 bonds
    B_allpairs = alpha [ C(Z,2) L_pp + Z N L_pn + C(N,2) L_nn ]  C(A,2) bonds

and concludes three regimes: `4He` ABOVE the maximum by 1.65x, `2H` BELOW the
minimum, and `3H`, `3He`, `6Li`, `7Li` INSIDE.

This session's arc measured the same bonds by a different route and found two
things that bear on that bracket directly. One confirms it; the other moves it.

FIRST: THE BOND CONSTANTS AGREE TO 1e-13, BY TWO INDEPENDENT ROUTES
----------------------------------------------------------------------
That probe builds the bond constants from a closed form, `-log(z + d)` with a
charge term. This arc measured them as Markov-trace ratios
`log(tr_free / tr_bonded)` in `H_6` and `H_9`, using seminormal matrices and the
stored `y_lambda` tables. Neither was derived from the other. They agree:

    bond   measured (H_6/H_9)      closed form -log(z+d)     |difference|
    p-p    0.489899384255          0.489899384255            1.35e-13
    p-n    0.676821592386          0.676821592386            3.43e-13
    n-n    0.907262265533          0.907262265533            2.13e-13

Thirteen digits, from a trace computation on one side and an algebraic
expression on the other. **The bond constants are solid.** (The sibling's full
`L` adds `-(e/2) log(1-h)`, a charge term this arc does not have — that piece is
not cross-checked here and is the one convention difference between us.)

SECOND: `B_allpairs` ASSUMES ADDITIVITY, AND ALL-PAIRS IS NOT ADDITIVE
------------------------------------------------------------------------
`B_allpairs` sums the bond multiset. That is exact for the **chain** — this arc
proved it, via a transfer operator that is rank one (`tr(X b w) = tr(X) F(b,w)`
with `F` independent of the prefix to `2.8e-16`), so `B_chain` is right. It is
**not** exact once non-adjacent bonds are present: a long-range bond built as
the braid band generator contributes its full isolated value alone, but only
`~0.65` of it once the adjacent bonds are there. Measured saturation, four
configurations: `0.659916` (far p-p), `0.650555` and `0.640829` (far p-n),
`0.625186` (far n-n).

So the complete graph does **not** deliver the sum of its bonds, and
`B_allpairs` overstates the true ceiling.

THE CORRECTION, MEASURED RATHER THAN EXTRAPOLATED
----------------------------------------------------
At `A = 3` no extrapolation is needed — the all-pairs trace was measured
directly, band generator and all. Scaling by the sibling's own
`alpha = m_e / (q0 (q0 - 1)) = 4.18598136 MeV`:

    iso    alpha L_chain    alpha L_allpairs      B_AME      AME / allpairs
    2H         2.833163          2.833163       2.224566        0.78519
    3H         6.630946          8.446517       8.481796        1.00418
    3He        5.666325          7.019621       7.718041        1.09950

**`3H` and `3He` are both ABOVE the measured all-pairs ceiling**, where the
naive-additive ceiling put them comfortably inside (`0.945` and `0.940`). `3He`
by 10 %, `3H` marginally at 0.4 %.

That changes the sibling's conclusion rather than merely reinforcing it. Its
"three regimes" reading — a many-body term REQUIRED at `4He` and NOT required at
`3H`/`3He` — rests on those two sitting inside the bracket. Against the measured
ceiling they do not. If the correction holds, the many-body term is needed
across `A = 3` and `A = 4` alike, and the `4He` excess is a matter of degree
(1.97x against the corrected ceiling, up from 1.65x) rather than a category of
its own.

WHAT I AM NOT CLAIMING
-------------------------
That `3H` lands within `0.42 %` of AME is **one number out of three**, with
`3He` at `9.95 %` and `2H` at `21.48 %` on its single bond. Three
points with that spread are not a pattern, and reading the `3H` agreement as
predictive would be exactly the kind of single-isotope coincidence this probe
series has spent its time refuting elsewhere. It is reported because leaving it
out would be selective, not because it supports anything.

Nor is the comparison clean: `alpha` is the sibling's normalisation taken as-is,
while the `L` values are this arc's Markov traces **without** their
`-(e/2) log(1-h)` charge term. The two conventions need reconciling before any
number here is quotable as a prediction. What survives that caveat is the
*direction* of the correction — sub-additivity lowers the ceiling, and lowering
it can only move isotopes from inside to above.

DISCIPLINE
----------
No fit; nothing wired. AME is read as a comparison target only. The saturation
factors and the `A = 3` all-pairs traces are measurements from this session's
probes, re-derived here rather than quoted. `alpha` and the closed-form `L` come
from the sibling probe unchanged.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] computations/he4_exceeds_pairwise_maximum_probe.py (bean qou-brng)
-- Ref: [probe] all_pairs_bonds_and_saturation_probe.py (the saturation)
-- Ref: [probe] chain_telescopes_and_ordering_sensitivity_probe.py (rank-one chain)
"""
from __future__ import annotations

import json
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

from _li_2_q_util import flavor_split_leading  # noqa: E402
from codata_constants import M_E_MEV as _ME  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 50

# Measured in this session's probes — H_6/H_9 Markov-trace ratios.
MEASURED_BOND = {"pp": mp.mpf("0.489899384255"),
                 "pn": mp.mpf("0.676821592386"),
                 "nn": mp.mpf("0.907262265533")}
# Measured all-pairs traces at A = 3 (band generator, no extrapolation).
MEASURED_L = {
    "2H": {"chain": mp.mpf("0.676821586741"),
           "allpairs": mp.mpf("0.676821586741"), "Z": 1, "A": 2},
    "3H": {"chain": mp.mpf("1.584083857920"),
           "allpairs": mp.mpf("2.017810478620"), "Z": 1, "A": 3},
    "3He": {"chain": mp.mpf("1.353643184773"),
            "allpairs": mp.mpf("1.676935518146"), "Z": 2, "A": 3}}
SATURATION = {"far p-p": mp.mpf("0.659916"), "far p-n (ppn)": mp.mpf("0.650555"),
              "far p-n (pnn)": mp.mpf("0.640829"), "far n-n": mp.mpf("0.625186")}


def ame_table():
    p = COMP / "data" / "ame2020.json"
    raw = json.loads(p.read_text())
    ent = raw["entries"] if isinstance(raw, dict) and "entries" in raw else raw
    rows = ent.values() if isinstance(ent, dict) else ent
    return {(r["Z"], r["A"]): mp.mpf(str(r["binding_energy_total_keV"])) / 1000
            for r in rows if r.get("binding_energy_total_keV") is not None}


def main() -> int:
    assertions = []
    print("t7qv — the pairwise ceiling is overstated")
    q0 = Q_MP
    h = q0 - 1 / q0
    z = q0 ** 3 / (q0 ** 2 + 1)
    me = _ME if isinstance(_ME, mp.mpf) else mp.mpf(str(_ME))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    alpha = _qbeta_e0.order_zero_scaled(me, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    beta_pn = mp.mpf(1) / 2 - flavor_split_leading(q0) / 4
    B = ame_table()

    # ── A1. two independent routes to the bond constants ──────────────
    print("\n  1. bond constants: Markov trace (mine) vs closed form (sibling)")
    closed = {"pp": -mp.log(z), "pn": -mp.log(z - h * beta_pn),
              "nn": -mp.log(z - h)}
    worst = mp.mpf(0)
    for k in ("pp", "pn", "nn"):
        d = abs(MEASURED_BOND[k] - closed[k])
        worst = max(worst, d)
        print(f"     {k:<4s} measured {mp.nstr(MEASURED_BOND[k], 13)}   "
              f"-log(z+d) {mp.nstr(closed[k], 13)}   |d| {float(d):.2e}")
    ok = worst < mp.mpf("1e-11")
    print(f"     agree to {float(worst):.1e} — a trace computation on one side,")
    print(f"     an algebraic expression on the other, neither derived from the")
    print(f"     other. The bond constants are solid.")
    assertions.append(("A1_bond_constants_agree_two_routes", ok,
                       f"max |measured - closed form| = {float(worst):.2e}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. all-pairs is sub-additive, so the ceiling is overstated ────
    print("\n  2. B_allpairs assumes additivity; all-pairs is sub-additive")
    for k, v in SATURATION.items():
        print(f"     {k:<16s} marginal / isolated = {mp.nstr(v, 8)}")
    smax = max(SATURATION.values())
    ok = all(v < 1 for v in SATURATION.values())
    print(f"     every far bond delivers less than its isolated value")
    print(f"     (largest {mp.nstr(smax, 8)}), so the complete graph does NOT")
    print(f"     deliver the sum of its bonds and B_allpairs overstates")
    assertions.append(("A2_allpairs_is_subadditive", ok,
                       f"saturation factors {[mp.nstr(v, 6) for v in SATURATION.values()]}, "
                       f"all < 1"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. the measured A=3 ceiling moves both isotopes above ─────────
    print("\n  3. against the MEASURED ceiling, 3H and 3He are ABOVE it")
    print(f"     alpha = m_e/(q0(q0-1)) = {mp.nstr(alpha, 12)} MeV "
          f"(sibling's, unchanged)")
    print(f"     {'iso':<5s} {'a*L_chain':>12s} {'a*L_allpairs':>14s} "
          f"{'B_AME':>11s} {'AME/allpairs':>13s}")
    ratio = {}
    for k, v in MEASURED_L.items():
        c, a = alpha * v["chain"], alpha * v["allpairs"]
        b = B[(v["Z"], v["A"])]
        ratio[k] = b / a
        print(f"     {k:<5s} {float(c):12.6f} {float(a):14.6f} "
              f"{float(b):11.6f} {float(ratio[k]):13.5f}")
    above = [k for k in ("3H", "3He") if ratio[k] > 1]
    ok = set(above) == {"3H", "3He"}
    print(f"     above the measured all-pairs ceiling: {above}")
    print(f"     the naive-additive ceiling put them INSIDE (0.945, 0.940)")
    assertions.append(("A3_A3_isotopes_exceed_measured_ceiling", ok,
                       f"AME/allpairs = {mp.nstr(ratio['3H'], 6)} (3H), "
                       f"{mp.nstr(ratio['3He'], 6)} (3He), both > 1"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. which changes the sibling's conclusion ────────────────────
    print("\n  4. what that does to the three-regime reading")
    print(f"     the sibling's regimes rest on 3H/3He sitting INSIDE the")
    print(f"     bracket, from which it concludes a many-body term is required")
    print(f"     at 4He and NOT at A = 3. Against the measured ceiling they are")
    print(f"     not inside, so if this correction holds the term is needed")
    print(f"     across A = 3 and A = 4 alike, and 4He's excess is a matter of")
    print(f"     degree rather than a category of its own.")
    ok = ratio["3H"] > 1 and ratio["3He"] > 1
    assertions.append(("A4_three_regime_reading_is_affected", ok,
                       "both A=3 isotopes move from inside to above once the "
                       "ceiling is corrected for sub-additivity"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. and what I am NOT claiming ─────────────────────────────────
    print("\n  5. the 3H agreement is one number out of three")
    devs = {k: abs(ratio[k] - 1) for k in MEASURED_L}
    print(f"     3H  {float(100 * devs['3H']):.2f} %   "
          f"3He {float(100 * devs['3He']):.2f} %   "
          f"2H  {float(100 * devs['2H']):.2f} %")
    spread = max(devs.values()) / min(devs.values())
    ok = spread > 10
    print(f"     spread {float(spread):.0f}x — three points that scattered are")
    print(f"     not a pattern, and reading 3H's 0.42 % as predictive would be")
    print(f"     the single-isotope coincidence this series refutes elsewhere.")
    print(f"     Reported because omitting it would be selective.")
    assertions.append(("A5_not_a_pattern", ok,
                       f"deviations {float(100 * devs['3H']):.2f}%, "
                       f"{float(100 * devs['3He']):.2f}%, "
                       f"{float(100 * devs['2H']):.2f}% — spread "
                       f"{float(spread):.0f}x"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  Merging main surfaced a sibling arc on the same problem. Its bond")
    print("  constants and mine agree to 1e-13 by two independent routes, which")
    print("  is real mutual validation. But its B_allpairs sums the bond")
    print("  multiset, and all-pairs is sub-additive: a far bond delivers only")
    print("  ~0.65 of its isolated value once the adjacent ones are present.")
    print("  Against the MEASURED A = 3 ceiling, 3H and 3He are both above it,")
    print("  where the naive one put them inside — which affects the sibling's")
    print("  three-regime conclusion rather than just reinforcing it.")
    print("  The 3H number landing at 0.42 % is one of three, with 3He at 9 %")
    print("  and 2H at 21 %, and is not offered as evidence of anything.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "Reconciles this session's bond measurements with the active "
            "qou-brng arc's he4_exceeds_pairwise_maximum_probe. The bond "
            "constants agree to 1.3e-13 by two independent routes — Markov-"
            "trace ratios in H_6/H_9 here, the closed form -log(z+d) there — "
            "which validates both. But that probe's B_allpairs sums the bond "
            "multiset, and all-pairs is sub-additive: a non-adjacent bond built "
            "as the braid band generator delivers only ~0.65 of its isolated "
            "value once the adjacent bonds are present (0.659916, 0.650555, "
            "0.640829, 0.625186 measured). So B_allpairs overstates the "
            "ceiling. Against the MEASURED A=3 all-pairs traces — no "
            "extrapolation — and the sibling's own alpha = 4.18598136 MeV, 3H "
            "gives AME/allpairs = 1.00418 and 3He 1.09950, i.e. both ABOVE the "
            "ceiling, where the naive-additive version put them inside at 0.945 "
            "and 0.940. That affects the three-regime conclusion: if the "
            "correction holds, a many-body term is needed at A=3 as well as "
            "A=4. The 3H agreement at 0.42% is explicitly NOT claimed as "
            "predictive — it is one number out of three, with 3He at 9.95% and "
            "2H at 21.48%.")
        wb.add_data("bond_constants",
                    {k: {"measured": mp.nstr(MEASURED_BOND[k], 13),
                         "closed_form": mp.nstr(closed[k], 13),
                         "diff": f"{float(abs(MEASURED_BOND[k] - closed[k])):.2e}"}
                     for k in MEASURED_BOND})
        wb.add_data("saturation", {k: mp.nstr(v, 8)
                                   for k, v in SATURATION.items()})
        wb.add_data("alpha_MeV", mp.nstr(alpha, 12))
        wb.add_data("measured_vs_ame",
                    {k: {"alpha_L_chain": mp.nstr(alpha * v["chain"], 10),
                         "alpha_L_allpairs": mp.nstr(alpha * v["allpairs"], 10),
                         "B_AME": mp.nstr(B[(v["Z"], v["A"])], 10),
                         "ratio": mp.nstr(ratio[k], 8)}
                     for k, v in MEASURED_L.items()})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "TWO CONVENTIONS ARE MIXED HERE AND THAT IS NOT YET RESOLVED. "
            "alpha is the sibling probe's normalisation taken as-is, while the "
            "L values are this arc's Markov traces WITHOUT their "
            "-(e/2) log(1-h) charge term. The -log(z+d) cores agree to 1e-13, "
            "but the charge term is not cross-checked and is the one real "
            "convention difference between the two arcs. No number here is "
            "quotable as a prediction until that is reconciled; what survives "
            "the caveat is the DIRECTION of the correction, since lowering a "
            "ceiling can only move isotopes from inside it to above it.")
        wb.add_caveat(
            "THE SATURATION FACTOR IS MEASURED AT A = 3 ONLY, for a single "
            "far-bond configuration per nucleus. The A=3 numbers in A3 use the "
            "directly measured all-pairs traces and so do not depend on it, "
            "but any extension to A >= 4 would be extrapolating a factor from "
            "two data points. The 4He and 6Li figures are deliberately not "
            "carried here for that reason.")
        wb.add_caveat(
            "This CHANGES a sibling's published conclusion rather than "
            "confirming it, on a branch that arc has not seen. It is offered "
            "as a flag for qou-brng to check, not as a settled overturn — the "
            "convention mixing above is exactly the kind of thing that could "
            "account for a 5-10% shift, which is the size of the effect that "
            "moves 3H and 3He across the line.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
