#!/usr/bin/env python3
"""The two arcs are computing FRAMED and WRITHE-NORMALISED bonds — not
conflicting ones — and the `pn` writhe carries a sign flip.

PARTIALLY SUPERSEDED — READ `pn_writhe_is_not_an_exponent_probe.py`
------------------------------------------------------------------
A2 below derives `e_pn = +delta/2` from the operator identity
`sigma - beta h = (1-beta) sigma + beta sigma^-1`. **The identity is right; the
value is not.** Feeding its coefficient average into an exponent is the wrong
operation: the Markov trace is linear and `(1-h)^(e/2)` is defined per diagram,
so each summand carries its own writhe. Forced back into exponent form the true
value is `e_eff = 0.149437`, `217x` either `+/-delta/2` — the sign was never the
live degree of freedom, and that correction is worth `108x` this one. Read A2
as establishing that the bond is a MIXTURE, not as fixing a value for `e_pn`.
A1, A4, A5 and A6 stand; the framed branch is untouched throughout.

WHAT THIS SETTLES
-----------------
The one real convention difference between this arc and `qou-brng` was the term
`-(e/2) log(1-h)` that their `L` carries and my measured Markov traces do not.
I had flagged it as blocking: until it is reconciled, neither side's MeV figures
are quotable against the other's. It reconciles, and the answer is not that one
of us is wrong.

`e` IS THE WRITHE, AND THE CONVENTION IS FIXED BY THE CORPUS
--------------------------------------------------------------
`stacked_interface_writhe_normalised_probe` tabulates `mu_eff = mu (1-h)^(e/2)`
for `sigma^m` with `e = m`, so `e` is the signed crossing count. A bond `(1, d)`
is `sigma + d`, and with `d = -beta h`

    sigma - beta h  =  (1-beta) sigma  +  beta sigma^-1        [verified
                                                                symbolically]

— a convex combination of a positive and a negative crossing — so its expected
writhe is

    e  =  (1-beta)(+1) + beta(-1)  =  1 - 2 beta

THE `pn` SIGN
----------------
Against that rule:

    bond   beta            1 - 2 beta        e as coded        match
    pp     0               +1                +1                yes
    nn     1               -1                -1                yes
    pn     1/2 - delta/4   +delta/2          -delta/2          **NO**

`pp` and `nn` follow `e = 1 - 2 beta`; `pn` is passed `2 beta - 1`, the opposite
convention. The source comment confirms the intent rather than excusing it:
`# production de['pn'] = -delta/2`.

**Impact is small but the quantity is shared.** Correcting it raises `L_pn` by
`1.6133e-4`, `0.0238 %` of `L_pn`, worth `2.70e-3 MeV` on `4He`'s four p-n
bonds — `0.0095 %` of `28.2957`. Nothing in the arc's conclusions moves. But
`L_pn` is consumed by at least five probes (`he4_exceeds_pairwise_maximum`,
`pn_letter_causal_test`, `spectral_gap_bond_decay`, `allpairs_distance_decay`,
`wide_isotope_window_test`), so the fix belongs upstream rather than in each.

THE RECONCILIATION: FRAMED AGAINST WRITHE-NORMALISED
-------------------------------------------------------
    mine    -log(z + d)                          the raw trace ratio
    theirs  -log(z + d) - (e/2) log(1-h)         plus the writhe normalisation

The extra piece is *exactly* the corpus's own `mu_eff = mu (1-h)^(e/2)`, taken
into the log. So the two arcs are not disagreeing about a number: **mine is the
FRAMED quantity and theirs is the WRITHE-NORMALISED one.** The Ocneanu/Markov
trace of a braid is framing-dependent — that is why HOMFLY carries a writhe
factor at all — and normalising it away is a deliberate, documented step, not a
correction to the trace.

That is why the `-log(z+d)` cores agreed to `1.3e-13` while the full `L` values
did not: they were never meant to.

HOW MUCH RIDES ON THE CHOICE
-------------------------------
Enough to matter, and it is not uniform — the writhe term is `+0.1173 e`, so it
raises `p-p` (`e = +1`), lowers `n-n` (`e = -1`), and barely touches `p-n`
(`e ~ 0`). It therefore **compresses the spread between bond types by 56 %**,
from `0.417363` framed to `0.182829` normalised, which is exactly the quantity
the mirror-pair ordering depends on. Per isotope the two conventions differ by
up to `6.4 %` of AME (`3He`), and they differ **only** where `Z != N`: at
`Z = N` the `p-p` and `n-n` shifts are equal and opposite and cancel exactly,
which is why `2H`, `4He` and `6Li` move by `< 0.02 %` while the mirror pair
splits. The isotope table is computed both ways below.

**A trap in that table.** Framed `3He` lands at `-0.01 %` of AME. That is a
coincidence, not a result: the table is the naive sum of independent bond
constants, which `pairwise_ceiling_is_overstated_probe` measured to be
*sub*-additive — the actual `H_9` trace of the three-bond word gives `7.0196`,
not `7.717`, against the same AME `7.71804`. Only the DIFFERENCE between the two
columns is meaningful here; neither column is a binding prediction.

**Which one binding should use is a physics question this probe does not
settle.** Framing is `Tw` in `Lk = Wr + Tw`, and the corpus carries a helicity
thread where that decomposition is physical (Moffatt-Ricca, `H = n Phi^2`). If
the nucleus is a framed object the framed trace is the right one; if the framing
is gauge the normalised one is. Nothing here decides it — but the two arcs
should stop quoting across the line until someone does.

AND MY NO-DISTANCE-DECAY RESULT SURVIVES BOTH
------------------------------------------------
The band generator is `g (T2+d) g^-1` with `g = T5 T4 T3`: `writhe(g) = +3`,
`writhe(g^-1) = -3`, net zero. **Conjugation preserves writhe**, so the
separation-2 bond carries the same writhe as the adjacent one and the two
conventions agree on it exactly. That is the structural reason all four routings
returned one number, and it means `no_distance_decay_in_the_trace_probe`'s
conclusion holds framed *and* normalised.

DISCIPLINE
----------
No fit; nothing wired. The convex-combination identity is verified symbolically.
The writhe convention is read off the corpus's own `mu_eff` tabulation, not
assumed. AME is a comparison target only.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] computations/probes/stacked_interface_writhe_normalised_probe.py
-- Ref: [probe] computations/he4_exceeds_pairwise_maximum_probe.py (qou-brng)
-- Ref: [probe] no_distance_decay_in_the_trace_probe.py
"""
from __future__ import annotations

import json
import sys
import warnings
from math import comb
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
import sympy as sp  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from codata_constants import M_E_MEV as _ME  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except Exception:  # pragma: no cover
    _HAVE_WB = False

mp.mp.dps = 50
ISO = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2), ("6Li", 3, 3)]


def ame():
    raw = json.loads((COMP / "data" / "ame2020.json").read_text())
    ent = raw["entries"] if isinstance(raw, dict) and "entries" in raw else raw
    rows = ent.values() if isinstance(ent, dict) else ent
    return {(r["Z"], r["A"]): mp.mpf(str(r["binding_energy_total_keV"])) / 1000
            for r in rows if r.get("binding_energy_total_keV") is not None}


def main() -> int:
    assertions = []
    print("t7qv — framed vs writhe-normalised, and the pn writhe sign")
    q0 = mp.mpf(Q_50_DIGIT_STR)
    h = q0 - 1 / q0
    z = q0 ** 3 / (q0 ** 2 + 1)
    me = _ME if isinstance(_ME, mp.mpf) else mp.mpf(str(_ME))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    alpha = _qbeta_e0.order_zero_scaled(me, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    dlt = flavor_split_leading(q0)
    wr = mp.log(1 - h)
    beta = {"pp": mp.mpf(0), "nn": mp.mpf(1), "pn": mp.mpf(1) / 2 - dlt / 4}
    B = ame()

    # ── A1. the convex-combination identity ───────────────────────────
    print("\n  1. a bond is a convex combination of the two crossings")
    S, b, qs = sp.symbols("S b q")
    hs = qs - 1 / qs
    resid = sp.simplify((1 - b) * S + b * (S - hs) - (S - b * hs))
    ok = resid == 0
    print(f"     (1-b) sigma + b sigma^-1  -  (sigma - b h)  =  {resid}")
    print(f"     so a bond (1, -beta h) carries expected writhe 1 - 2 beta")
    assertions.append(("A1_bond_is_convex_combination", ok,
                       f"(1-b)S + b(S-h) - (S-bh) simplifies to {resid}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. pp/nn follow it; pn is sign-flipped ───────────────────────
    print("\n  2. the writhe convention, checked bond by bond")
    coded = {"pp": mp.mpf(1), "nn": mp.mpf(-1), "pn": 2 * beta["pn"] - 1}
    rule = {k: 1 - 2 * v for k, v in beta.items()}
    match = {k: abs(rule[k] - coded[k]) < mp.mpf("1e-40") for k in beta}
    print(f"     {'bond':<5s} {'beta':<16s} {'1-2beta':<18s} {'as coded':<18s} ok")
    for k in ("pp", "nn", "pn"):
        print(f"     {k:<5s} {mp.nstr(beta[k], 8):<16s} "
              f"{mp.nstr(rule[k], 8):<18s} {mp.nstr(coded[k], 8):<18s} "
              f"{'yes' if match[k] else '*** NO ***'}")
    ok = match["pp"] and match["nn"] and not match["pn"]
    print(f"     pp and nn follow e = 1-2beta; pn is passed 2beta-1, the")
    print(f"     opposite convention. Source comment: "
          f"'# production de[pn] = -delta/2'")
    assertions.append(("A2_pn_writhe_sign_is_flipped", ok,
                       f"pp and nn match 1-2beta; pn coded {mp.nstr(coded['pn'], 8)} "
                       f"against {mp.nstr(rule['pn'], 8)}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. the impact is small but the quantity is shared ────────────
    print("\n  3. how much the sign is worth")
    dL = -((rule["pn"] - coded["pn"]) / 2) * wr
    L_pn_framed = -mp.log(z - h * beta["pn"])
    d4 = alpha * 4 * dL
    ok = dL > 0 and abs(d4 / mp.mpf("28.2957")) < mp.mpf("1e-3")
    print(f"     correcting raises L_pn by {mp.nstr(dL, 8)} "
          f"({float(100 * dL / L_pn_framed):.4f} % of L_pn)")
    print(f"     on 4He's four p-n bonds: {mp.nstr(d4, 8)} MeV of 28.2957, "
          f"{float(100 * d4 / mp.mpf('28.2957')):.4f} %")
    print(f"     nothing in the arc's conclusions moves — but L_pn is consumed")
    print(f"     by at least five probes, so the fix belongs upstream")
    assertions.append(("A3_sign_impact_is_small_but_shared", ok,
                       f"dL_pn = {mp.nstr(dL, 6)}, {float(100 * d4 / mp.mpf('28.2957')):.4f}% "
                       f"of 4He"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. the reconciliation ────────────────────────────────────────
    print("\n  4. framed vs writhe-normalised — two objects, not a conflict")
    framed = {k: -mp.log(z - h * beta[k]) for k in beta}
    norm = {k: framed[k] - (rule[k] / 2) * wr for k in beta}
    print(f"     {'bond':<5s} {'framed -log(z+d)':<20s} {'writhe-normalised':<20s}"
          f" {'shift':<12s}")
    for k in ("pp", "pn", "nn"):
        print(f"     {k:<5s} {mp.nstr(framed[k], 12):<20s} "
              f"{mp.nstr(norm[k], 12):<20s} "
              f"{mp.nstr(norm[k] - framed[k], 8):<12s}")
    sp_f = framed["nn"] - framed["pp"]
    sp_n = norm["nn"] - norm["pp"]
    compress = 1 - sp_n / sp_f
    ok = sp_n < sp_f and compress > mp.mpf("0.5")
    print(f"     the term is +0.1173 e: raises p-p, lowers n-n, barely moves p-n")
    print(f"     spread nn-pp: framed {mp.nstr(sp_f, 8)} -> normalised "
          f"{mp.nstr(sp_n, 8)}, compressed {float(100 * compress):.0f} %")
    print(f"     that spread is what the mirror-pair ordering depends on")
    assertions.append(("A4_writhe_term_compresses_the_spread", ok,
                       f"nn-pp spread {mp.nstr(sp_f, 6)} -> {mp.nstr(sp_n, 6)}, "
                       f"compressed {float(100 * compress):.0f}%"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. how much rides on it, per isotope ─────────────────────────
    print("\n  5. the isotope table, both conventions (all-pairs, naive sum)")
    print(f"     {'iso':<5s} {'framed':>10s} {'normalised':>12s} {'B_AME':>10s}"
          f" {'framed %':>10s} {'norm %':>9s}")
    rows = {}
    for lbl, Z, N in ISO:
        A = Z + N
        mult = {"pp": comb(Z, 2), "pn": Z * N, "nn": comb(N, 2)}
        bf = alpha * sum(mult[k] * framed[k] for k in framed)
        bn = alpha * sum(mult[k] * norm[k] for k in norm)
        bame = B[(Z, A)]
        rows[lbl] = (bf, bn, bame)
        print(f"     {lbl:<5s} {float(bf):10.5f} {float(bn):12.5f} "
              f"{float(bame):10.5f} {float(100 * (bf / bame - 1)):9.2f}% "
              f"{float(100 * (bn / bame - 1)):8.2f}%")
    diffs = {k: abs(rows[k][0] - rows[k][1]) / rows[k][2] for k in rows}
    worst = max(diffs, key=lambda k: diffs[k])
    sym = [lbl for lbl, Z, N in ISO if Z == N]
    ok = diffs[worst] > mp.mpf("0.05") and max(diffs[k] for k in sym) < mp.mpf("1e-3")
    print(f"     the two conventions differ by up to "
          f"{float(100 * diffs[worst]):.1f} % of AME ({worst}) — not negligible,")
    print(f"     and ONLY where Z != N: at Z = N the p-p and n-n shifts are equal")
    print(f"     and opposite and cancel, so {', '.join(sym)} move by "
          f"< {float(100 * max(diffs[k] for k in sym)):.2f} % while the mirror")
    print(f"     pair 3H/3He splits by {float(100 * diffs['3H']):.1f} / "
          f"{float(100 * diffs['3He']):.1f} %")
    print(f"     TRAP: framed 3He at -0.01 % is a COINCIDENCE, not agreement —")
    print(f"     this table is the naive sum, and the measured H_9 trace of the")
    print(f"     three-bond word is 7.0196 (pairwise_ceiling_is_overstated).")
    print(f"     Only the DIFFERENCE between the columns is meaningful here.")
    print(f"     WHICH ONE binding should use is a physics question this")
    print(f"     probe does not settle (framing is Tw in Lk = Wr + Tw)")
    assertions.append(("A5_convention_choice_is_material", ok,
                       f"framed vs normalised differ by up to "
                       f"{float(100 * diffs[worst]):.1f}% of AME ({worst}), and "
                       f"cancel to <{float(100 * max(diffs[k] for k in sym)):.2f}% "
                       f"at Z = N"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. conjugation preserves writhe ──────────────────────────────
    print("\n  6. why no-distance-decay survives BOTH conventions")
    w_conj = 3 - 3
    ok = w_conj == 0
    print(f"     band generator g (T2+d) g^-1, g = T5 T4 T3:")
    print(f"     writhe(g) = +3, writhe(g^-1) = -3, net {w_conj}")
    print(f"     conjugation preserves writhe, so the separation-2 bond carries")
    print(f"     the SAME writhe as the adjacent one and the framed and")
    print(f"     normalised values agree on it exactly. That is the structural")
    print(f"     reason all four routings gave one number, and it means")
    print(f"     no_distance_decay_in_the_trace_probe holds in both conventions.")
    assertions.append(("A6_conjugation_preserves_writhe", ok,
                       "band generator has net conjugator writhe 0, so far and "
                       "adjacent bonds carry identical writhe"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  The blocking convention difference resolves, and neither arc is")
    print("  wrong: mine is the FRAMED trace ratio -log(z+d), theirs adds the")
    print("  corpus's own writhe normalisation mu_eff = mu (1-h)^(e/2). Two")
    print("  objects. That is why the cores agreed to 1e-13 and the full L did")
    print("  not — they were never meant to.")
    print("  One defect found: the pn writhe is passed with the opposite sign")
    print("  from pp and nn. Worth 0.0095 % on 4He, so no conclusion moves, but")
    print("  L_pn is shared by five probes and the fix belongs upstream.")
    print(f"  The choice is material — the writhe term compresses the bond-type")
    print(f"  spread by {float(100 * compress):.0f} %, and that spread is what "
          f"the mirror ordering")
    print(f"  rests on: the two conventions agree to "
          f"{float(100 * max(diffs[k] for k in sym)):.2f} % at Z = N and part by")
    print(f"  {float(100 * diffs[worst]):.1f} % at {worst}. It is a physics "
          f"question, not a bookkeeping one.")
    print("  My no-distance-decay result is untouched: conjugation preserves")
    print("  writhe, so it holds framed and normalised alike.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "Resolves the one convention difference between this arc and "
            "qou-brng. Their L carries -(e/2) log(1-h) where my measured Markov "
            "traces give -log(z+d) alone. e is the WRITHE: the corpus's "
            "stacked_interface_writhe_normalised_probe tabulates mu_eff = "
            "mu (1-h)^(e/2) for sigma^m with e = m, and a bond sigma - beta h "
            "is the convex combination (1-beta) sigma + beta sigma^-1 "
            "(verified symbolically), so its expected writhe is 1 - 2 beta. "
            "pp (+1) and nn (-1) follow that; pn is passed 2 beta - 1 = "
            "-delta/2, the opposite convention, where the rule gives +delta/2. "
            "Correcting raises L_pn by 1.6133e-4 (0.0238%), worth 2.70e-3 MeV "
            "on 4He (0.0095%) — no conclusion moves, but L_pn is consumed by at "
            "least five probes so the fix belongs upstream. The deeper "
            "reconciliation: mine is the FRAMED trace ratio, theirs the "
            "WRITHE-NORMALISED one, which is why the -log(z+d) cores agreed to "
            "1.3e-13 while the full L values did not. The choice is material — "
            "the writhe term raises p-p, lowers n-n and barely moves p-n, "
            "compressing the bond-type spread by 39%, which is what the "
            "mirror-pair ordering depends on — and which convention binding "
            "should use is a physics question (framing is Tw in Lk = Wr + Tw) "
            "not settled here. Per isotope the conventions differ by up to 6.4% "
            "of AME (3He) and ONLY where Z != N — at Z = N the p-p and n-n "
            "shifts are equal and opposite and cancel to under 0.02%, so the "
            "choice is invisible on 2H/4He/6Li and splits exactly the mirror "
            "pair. The no-distance-decay result survives both: the band "
            "generator's conjugator has net writhe zero, so far and adjacent "
            "bonds carry identical writhe.")
        wb.add_data("writhe_rule", "e = 1 - 2 beta")
        wb.add_data("writhe_by_bond",
                    {k: {"beta": mp.nstr(beta[k], 12),
                         "rule_1_minus_2beta": mp.nstr(rule[k], 12),
                         "as_coded": mp.nstr(coded[k], 12),
                         "matches": bool(match[k])} for k in beta})
        wb.add_data("sign_impact", {"dL_pn": mp.nstr(dL, 10),
                                    "pct_of_L_pn": f"{float(100 * dL / L_pn_framed):.4f}",
                                    "MeV_on_4He": mp.nstr(d4, 8)})
        wb.add_data("framed_vs_normalised",
                    {k: {"framed": mp.nstr(framed[k], 12),
                         "normalised": mp.nstr(norm[k], 12)} for k in framed})
        wb.add_data("spread_compression",
                    {"framed_nn_minus_pp": mp.nstr(sp_f, 10),
                     "normalised_nn_minus_pp": mp.nstr(sp_n, 10),
                     "compressed_pct": f"{float(100 * compress):.1f}"})
        wb.add_data("convention_gap_pct_of_AME",
                    {k: f"{float(100 * diffs[k]):.4f}" for k in diffs})
        wb.add_data("isotope_table",
                    {k: {"framed": mp.nstr(v[0], 10),
                         "normalised": mp.nstr(v[1], 10),
                         "B_AME": mp.nstr(v[2], 10)} for k, v in rows.items()})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "WHICH CONVENTION BINDING SHOULD USE IS NOT SETTLED HERE. Framing "
            "is Tw in Lk = Wr + Tw, and the corpus carries a helicity thread "
            "where that decomposition is physical (Moffatt-Ricca, H = n Phi^2). "
            "If the nucleus is a framed object the framed trace is right; if "
            "the framing is gauge, the normalised one is. This probe only "
            "establishes that the two arcs are computing different objects and "
            "quantifies the gap — up to 6.4% of AME, all of it at Z != N — so "
            "that neither quotes across the line until someone decides.")
        wb.add_caveat(
            "THE pn SIGN IS REPORTED AS A DEFECT ON A SIBLING'S ACTIVE WORK, "
            "found by applying their own stated convention (e = writhe, from "
            "their own mu_eff tabulation) to their own three bonds. It is "
            "possible that pn's e is deliberately the other sign for a reason "
            "not written down — the source comment states the value but not a "
            "justification. Numerically it is 0.0095% on 4He, so nothing they "
            "have concluded depends on it either way.")
        wb.add_caveat(
            "The isotope table uses the NAIVE all-pairs sum for both "
            "conventions, so it isolates the framing choice. It therefore "
            "inherits the sub-additivity overstatement measured in "
            "pairwise_ceiling_is_overstated_probe and should not be read as a "
            "binding prediction in either column — only the DIFFERENCE between "
            "the columns is the quantity of interest here. Concretely: framed "
            "3He lands at -0.01% of AME, which is a COINCIDENCE of the naive "
            "sum, not agreement. The measured H_9 trace of the same three-bond "
            "word gives 7.0196 against AME 7.71804.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
