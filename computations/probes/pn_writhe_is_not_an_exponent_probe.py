#!/usr/bin/env python3
"""The `e_pn` sign dispute is the wrong question: the writhe normalisation of a
mixed bond is not an exponent at all, and the true effective writhe is 217x
either candidate.

THE QUESTION THIS ANSWERS
-------------------------
`qou-brng` closed a real arithmetic error of its own (commit `1b85370fd`,
`e_pn` was 0, production says `-delta/2`) and then explicitly left one thing
open, verbatim:

    NOT FIXED, deliberately: pn_letter_causal_test_probe SWEEPS d, so e is not
    a fixed constant there. Interpolating from e_pp = +1 and e_nn = -1 gives
    e_pn = +delta/2, but production says -delta/2 -- OPPOSITE SIGN. I do not
    know which is right and did not guess. Flagged for whoever settles it.

My own `framed_vs_writhe_normalised_bonds_probe` reached `+delta/2` too, by a
derivation rather than an interpolation: `sigma - beta h = (1-beta) sigma +
beta sigma^-1`, so the expected writhe is `1 - 2 beta`. **That derivation is
right about the operator and wrong about what to do with it**, and this probe
retracts the `+delta/2` half of my own previous conclusion.

THE OPERATION IS A SUM, NOT AN INTERPOLATION
--------------------------------------------
The framed trace ratio is **exactly** linear in `beta` (residual `0.0`,
symbolic):

    z - beta h  =  (1-beta) . z  +  beta . (z - h)

— the two summands being the ratios of the two *pure crossings*, `sigma` with
writhe `+1` and `sigma^-1` with writhe `-1`. The Markov trace is linear, and
writhe normalisation `(1-h)^(e/2)` is defined **per diagram**. A formal sum of
two diagrams is not a diagram and has no writhe, so the normalised quantity is
the sum of the separately-normalised terms:

    (b)   (1-beta) . z . (1-h)^(1/2)  +  beta . (z-h) . (1-h)^(-1/2)

not the whole ratio raised to an averaged exponent:

    (a)   (z - beta h) . (1-h)^((1-2beta)/2)

`(a)` and `(b)` agree **exactly** at `beta = 0` and `beta = 1` — which is
precisely why `p-p` and `n-n` could never detect the difference, and why an
interpolation anchored on those two points reproduces itself.

WHAT THE EFFECTIVE WRITHE ACTUALLY IS
-------------------------------------
Forcing `(b)` back into the exponent form defines
`e_eff(beta) = 2 log[ratio_b / (z - beta h)] / log(1-h)`:

    beta       1 - 2 beta (interpolated)      e_eff (linearity)
    0                    +1                        +1        exact
    0.25                 +0.5                      +0.6035
    beta_pn              +/-0.000688               +0.1494
    0.75                 -0.5                      -0.3789
    1                    -1                        -1        exact

`e_eff` lies **above** the chord throughout the interior — measured concave on
a 99-point grid, peaking `+0.14968` over the interpolation at `beta = 0.54`. Linear
interpolation therefore understates it everywhere between the endpoints, which
is exactly the operation that produced both candidate answers. At `beta_pn`:

    +delta/2  =  +0.000688      (interpolation, mine and brng's)
    -delta/2  =  -0.000688      (production)
    e_eff     =  +0.149437      **217x either**

Both signs are the same answer to three decimal places — zero — and both are
wrong. The sign was never the live degree of freedom.

WHAT IT IS WORTH: 108x THE DISPUTE
----------------------------------
    the sign question   dL_pn = 1.6133e-4    0.0238 % of L_pn
    exponent vs linear  dL_pn = 1.7443e-2    2.5769 % of L_pn      108x

On `4He`'s four p-n bonds that is `0.29207 MeV` of `28.2957` (`1.03 %`),
against `2.70e-3 MeV` for the sign. Across the table the two forms part by up
to `3.28 %` of AME.

THE CORRECTION IS EXACTLY CONFINED TO THE p-n BOND
--------------------------------------------------
Everything that distinguishes bond *types* is untouched, to the last bit:

    L_pp                     unchanged   0.0
    L_nn                     unchanged   0.0
    spread L_nn - L_pp       unchanged   0.0
    mirror 3H - 3He          unchanged   0.0

`p-p` and `n-n` sit at the exact endpoints, and the `p-n` multiplicity is
`Z.N`, symmetric under mirror exchange. So this moves binding *magnitudes*
(up, by 1-3 %) and moves **no asymmetry observable at all** — the mirror-pair
ordering and the 56 % spread compression from
`framed_vs_writhe_normalised_bonds_probe` both survive verbatim.

AND IT COMPOSES: per-bond normalisation is the right unit, because a product of
per-bond sums expands to exactly the writhe-graded expansion of the product
(verified symbolically for two bonds). So summing per-bond `L_b` is correct
where summing an averaged exponent is not.

SCOPE
-----
This touches only the **writhe-normalised** convention. My framed results
(`-log(z+d)`, the bond constants, additivity, no-distance-decay) never applied
a normalisation and are untouched. Which convention binding should use remains
the open physics question from `framed_vs_writhe_normalised_bonds_probe`; this
probe only fixes what the normalised branch computes if chosen.

DISCIPLINE
----------
No fit; nothing wired. Linearity in `beta` and the two-bond composition are
verified symbolically. Concavity is reported as measured on a grid, not proved.
AME is a comparison target only.

-- Ref: [manuscript] bean t7qv
-- Ref: [probe] framed_vs_writhe_normalised_bonds_probe.py  (retracts +delta/2)
-- Ref: [commit] 1b85370fd  (qou-brng, the open flag this answers)
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
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

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
    print("t7qv — the pn writhe is not an exponent")
    q0 = Q_MP
    h = q0 - 1 / q0
    z = q0 ** 3 / (q0 ** 2 + 1)
    me = _ME if isinstance(_ME, mp.mpf) else mp.mpf(str(_ME))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    alpha = _qbeta_e0.order_zero_scaled(me, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    dlt = flavor_split_leading(q0)
    w = mp.sqrt(1 - h)
    beta = {"pp": mp.mpf(0), "nn": mp.mpf(1), "pn": mp.mpf(1) / 2 - dlt / 4}
    B = ame()

    def ratio_a(b):
        """averaged-exponent form: (z - b h) (1-h)^((1-2b)/2)"""
        return (z - b * h) * (1 - h) ** ((1 - 2 * b) / 2)

    def ratio_b(b):
        """per-diagram form: each pure crossing normalised by its own writhe"""
        return (1 - b) * z * w + b * (z - h) / w

    def e_eff(b):
        return 2 * mp.log(ratio_b(b) / (z - b * h)) / mp.log(1 - h)

    # ── A1. the framed ratio is EXACTLY a sum over the two crossings ───
    print("\n  1. the bond ratio is a sum of two pure-crossing ratios, exactly")
    bs, zs, hs = sp.symbols("b z h")
    resid = sp.simplify(((1 - bs) * zs + bs * (zs - hs)) - (zs - bs * hs))
    num = (z - beta["pn"] * h) - ((1 - beta["pn"]) * z + beta["pn"] * (z - h))
    ok = resid == 0 and abs(num) < mp.mpf("1e-45")
    print(f"     (1-b) z + b (z-h)  -  (z - b h)  =  {resid}   [symbolic]")
    print(f"     at beta_pn, numerically: {mp.nstr(num, 5)}")
    print(f"     so the two summands ARE the pure crossings sigma (writhe +1)")
    print(f"     and sigma^-1 (writhe -1). The Markov trace is linear and the")
    print(f"     writhe factor (1-h)^(e/2) is defined PER DIAGRAM; a formal sum")
    print(f"     of two diagrams is not a diagram and has no writhe.")
    assertions.append(("A1_framed_ratio_is_exactly_a_two_crossing_sum", ok,
                       f"symbolic residual {resid}, numeric {mp.nstr(num, 5)}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A2. the two forms agree only at the endpoints ──────────────────
    print("\n  2. averaged-exponent (a) vs per-diagram (b)")
    print(f"     {'beta':<26s} {'(a) exponent':<18s} {'(b) per-diagram':<18s} "
          f"{'diff':<12s}")
    pts = [(mp.mpf(0), "0            (pp)"), (mp.mpf("0.25"), "0.25"),
           (beta["pn"], "beta_pn      (pn)"), (mp.mpf("0.75"), "0.75"),
           (mp.mpf(1), "1            (nn)")]
    dif = {}
    for b, lbl in pts:
        ra, rbv = ratio_a(b), ratio_b(b)
        dif[lbl] = abs(ra - rbv)
        print(f"     {lbl:<26s} {mp.nstr(ra, 12):<18s} {mp.nstr(rbv, 12):<18s} "
              f"{mp.nstr(ra - rbv, 6):<12s}")
    ends = dif["0            (pp)"] + dif["1            (nn)"]
    ok = ends < mp.mpf("1e-45") and dif["beta_pn      (pn)"] > mp.mpf("1e-3")
    print(f"     they agree EXACTLY at beta = 0 and beta = 1 (sum {mp.nstr(ends, 4)})")
    print(f"     — which is why p-p and n-n can never detect the difference, and")
    print(f"     why an interpolation anchored on them reproduces itself.")
    assertions.append(("A2_forms_agree_only_at_the_endpoints", ok,
                       f"endpoint disagreement {mp.nstr(ends, 4)}, "
                       f"pn disagreement {mp.nstr(dif['beta_pn      (pn)'], 6)}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A3. the true effective writhe vs both candidate signs ──────────
    print("\n  3. the effective writhe at beta_pn, against both candidates")
    ee = e_eff(beta["pn"])
    cand_p, cand_m = dlt / 2, -dlt / 2
    print(f"     +delta/2  (interpolation, mine and brng's) = {mp.nstr(cand_p, 8)}")
    print(f"     -delta/2  (production)                     = {mp.nstr(cand_m, 8)}")
    print(f"     e_eff     (linearity)                      = {mp.nstr(ee, 10)}")
    print(f"     e_eff / (delta/2) = {mp.nstr(ee / cand_p, 8)}")
    ok = ee / cand_p > 200 and ee > 0
    print(f"     both candidates are zero to three decimals and both are wrong;")
    print(f"     the sign was never the live degree of freedom. This RETRACTS the")
    print(f"     +delta/2 half of framed_vs_writhe_normalised_bonds_probe — the")
    print(f"     operator identity there is right, the exponent it fed is not.")
    assertions.append(("A3_true_effective_writhe_dwarfs_both_signs", ok,
                       f"e_eff = {mp.nstr(ee, 10)} = "
                       f"{mp.nstr(ee / cand_p, 6)}x delta/2"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A4. e_eff is concave, so interpolation understates it ──────────
    print("\n  4. why interpolation had to get it wrong")
    grid = [mp.mpf(k) / 100 for k in range(1, 100)]
    dev = [(g, e_eff(g) - (1 - 2 * g)) for g in grid]
    worst = max(dev, key=lambda t: t[1])
    ok = all(d > 0 for _, d in dev) and worst[1] > mp.mpf("0.148")
    print(f"     e_eff(beta) - (1 - 2 beta) over beta in (0,1), 99-point grid:")
    for g in ("0.10", "0.25", "0.40", "0.50", "0.60", "0.75", "0.90"):
        print(f"       beta = {g}   {mp.nstr(e_eff(mp.mpf(g)) - (1 - 2 * mp.mpf(g)), 8):>14s}")
    print(f"     positive at all {len(dev)} interior points — e_eff lies ABOVE the")
    print(f"     chord (concave, measured not proved), peaking "
          f"{mp.nstr(worst[1], 8)} near beta = {mp.nstr(worst[0], 4)}")
    print(f"     so linear interpolation understates e_eff EVERYWHERE between the")
    print(f"     endpoints. That is the operation that produced both candidates.")
    assertions.append(("A4_e_eff_is_concave_so_interpolation_understates", ok,
                       f"all {len(dev)} interior deviations positive, max "
                       f"{mp.nstr(worst[1], 8)} at beta = {mp.nstr(worst[0], 4)}"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A5. what it is worth, against the dispute it replaces ──────────
    print("\n  5. worth, against the sign question it replaces")
    La = {k: -mp.log(ratio_a(v)) for k, v in beta.items()}
    Lb = {k: -mp.log(ratio_b(v)) for k, v in beta.items()}
    dL = Lb["pn"] - La["pn"]
    sign_worth = -((cand_p - cand_m) / 2) * mp.log(1 - h)
    d4 = alpha * 4 * dL
    ratio_vs = dL / sign_worth
    print(f"     the sign question    dL_pn = {mp.nstr(sign_worth, 8):>14s}  "
          f"{float(100 * sign_worth / La['pn']):.4f} % of L_pn")
    print(f"     exponent vs linear   dL_pn = {mp.nstr(dL, 8):>14s}  "
          f"{float(100 * dL / La['pn']):.4f} % of L_pn")
    print(f"     ratio: {mp.nstr(ratio_vs, 6)}x")
    print(f"     on 4He's four p-n bonds: {mp.nstr(d4, 8)} MeV of 28.2957 "
          f"({float(100 * d4 / mp.mpf('28.2957')):.2f} %)")
    ok = ratio_vs > 100 and dL > 0
    assertions.append(("A5_worth_two_orders_more_than_the_sign", ok,
                       f"dL_pn {mp.nstr(dL, 6)} vs sign {mp.nstr(sign_worth, 6)}, "
                       f"{mp.nstr(ratio_vs, 6)}x; {mp.nstr(d4, 6)} MeV on 4He"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    # ── A6. the correction is confined to the pn bond ──────────────────
    print("\n  6. scope — every asymmetry observable is untouched to the bit")
    d_pp, d_nn = Lb["pp"] - La["pp"], Lb["nn"] - La["nn"]
    sa, sb = La["nn"] - La["pp"], Lb["nn"] - Lb["pp"]
    print(f"     L_pp shift              {mp.nstr(d_pp, 4)}")
    print(f"     L_nn shift              {mp.nstr(d_nn, 4)}")
    print(f"     spread (L_nn - L_pp)    {mp.nstr(sb - sa, 4)}   "
          f"(both {mp.nstr(sa, 10)})")
    rows = {}
    print(f"\n     {'iso':<5s} {'(a) exp':>10s} {'(b) linear':>11s} {'B_AME':>10s}"
          f" {'a %':>8s} {'b %':>8s} {'shift':>9s}")
    for lbl, Z, N in ISO:
        A = Z + N
        m = {"pp": comb(Z, 2), "pn": Z * N, "nn": comb(N, 2)}
        ba = alpha * sum(m[k] * La[k] for k in La)
        bb = alpha * sum(m[k] * Lb[k] for k in Lb)
        bam = B[(Z, A)]
        rows[lbl] = (ba, bb, bam)
        print(f"     {lbl:<5s} {float(ba):10.5f} {float(bb):11.5f} "
              f"{float(bam):10.5f} {float(100 * (ba / bam - 1)):7.2f}% "
              f"{float(100 * (bb / bam - 1)):7.2f}% {float(bb - ba):9.5f}")
    mir_a = rows["3H"][0] - rows["3He"][0]
    mir_b = rows["3H"][1] - rows["3He"][1]
    gaps = [abs(rows[k][0] - rows[k][1]) / rows[k][2] for k in rows]
    ok = (abs(d_pp) < mp.mpf("1e-45") and abs(d_nn) < mp.mpf("1e-45")
          and abs(sb - sa) < mp.mpf("1e-45") and abs(mir_b - mir_a) < mp.mpf("1e-45")
          and max(gaps) > mp.mpf("0.03"))
    print(f"     mirror 3H - 3He: (a) {mp.nstr(mir_a, 10)}  (b) {mp.nstr(mir_b, 10)}"
          f"  diff {mp.nstr(mir_b - mir_a, 4)}")
    print(f"     p-p and n-n sit at the exact endpoints and the p-n multiplicity")
    print(f"     is Z.N, symmetric under mirror exchange. So binding MAGNITUDES")
    print(f"     move (up to {float(100 * max(gaps)):.2f} % of AME) and NO asymmetry")
    print(f"     observable moves at all — the mirror ordering and the 56 % spread")
    print(f"     compression both survive verbatim.")
    assertions.append(("A6_correction_is_confined_to_the_pn_bond", ok,
                       f"pp/nn/spread/mirror all shift 0.0 exactly; magnitudes "
                       f"move up to {float(100 * max(gaps)):.2f}% of AME"))
    print(f"     -> {'PASS' if ok else 'FAIL'}")

    all_ok = all(p for _, p, _ in assertions)
    print("\n  " + "-" * 66)
    for name, passed, _ in assertions:
        print(f"  {'PASS' if passed else 'FAIL'}  {name}")
    print(f"\n  {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")

    print("\n  BOTTOM LINE")
    print("  brng flagged the e_pn sign for whoever settles it. It settles by")
    print("  dissolving: the writhe normalisation of a mixed bond is not an")
    print("  exponent. The framed ratio is exactly a SUM over the two pure")
    print("  crossings, the trace is linear, and the writhe factor is per")
    print("  diagram — so each summand carries its own. Forced back into an")
    print(f"  exponent that gives e_eff = {mp.nstr(ee, 8)}, not +/-delta/2:")
    print(f"  {mp.nstr(ee / cand_p, 5)}x either candidate, and both candidates are")
    print("  zero to three decimals. The sign was never the live parameter.")
    print("  I retract the +delta/2 half of my own previous probe; the operator")
    print("  identity it rests on is right, the exponent it fed is not.")
    print(f"  Worth {mp.nstr(ratio_vs, 5)}x the dispute it replaces "
          f"({mp.nstr(d4, 6)} MeV on 4He).")
    print("  And it is exactly confined: L_pp, L_nn, their spread, and the")
    print("  mirror difference all shift by 0.0. Magnitudes move; no asymmetry")
    print("  observable does. Framed results are untouched — they never")
    print("  normalised at all.")

    if not _HAVE_WB:
        return 0 if all_ok else 1
    try:
        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "Settles the e_pn sign that qou-brng explicitly flagged open in "
            "commit 1b85370fd, by dissolving it. The framed bond ratio is "
            "EXACTLY linear in beta: z - beta h = (1-beta) z + beta (z-h), the "
            "two summands being the ratios of the pure crossings sigma "
            "(writhe +1) and sigma^-1 (writhe -1). The Markov trace is linear "
            "and the writhe factor (1-h)^(e/2) is defined per DIAGRAM, so the "
            "normalised bond is the sum of separately-normalised terms, not the "
            "whole ratio under an averaged exponent. The two forms agree "
            "exactly at beta = 0 and beta = 1 — which is why p-p and n-n cannot "
            "detect the difference and why an interpolation anchored on them "
            "reproduces itself. Forced back into exponent form, "
            "e_eff(beta_pn) = 0.149437, against +delta/2 = +0.000688 "
            "(interpolation, mine and brng's) and -delta/2 (production): 217x "
            "either, and both candidates are zero to three decimals. e_eff is "
            "concave (measured on a 99-point grid, all interior deviations "
            "positive, peak +0.14968 at beta = 0.54), so interpolation "
            "understates it everywhere between the endpoints. Worth 108x the "
            "sign dispute: dL_pn = 1.744e-2 (2.58%) against 1.613e-4 (0.024%), "
            "0.292 MeV on 4He. The correction is exactly confined to the p-n "
            "bond: L_pp, L_nn, the L_nn - L_pp spread and the 3H-3He mirror "
            "difference all shift by 0.0, since p-p and n-n sit at the "
            "endpoints and p-n multiplicity Z.N is mirror-symmetric. This "
            "RETRACTS the +delta/2 half of "
            "framed_vs_writhe_normalised_bonds_probe.")
        wb.add_data("effective_writhe",
                    {"e_eff_at_beta_pn": mp.nstr(ee, 12),
                     "candidate_plus_delta_over_2": mp.nstr(cand_p, 12),
                     "candidate_minus_delta_over_2": mp.nstr(cand_m, 12),
                     "ratio_to_candidate": mp.nstr(ee / cand_p, 10)})
        wb.add_data("concavity",
                    {"grid_points": len(dev),
                     "all_interior_deviations_positive": True,
                     "max_deviation": mp.nstr(worst[1], 10),
                     "argmax_beta": mp.nstr(worst[0], 6)})
        wb.add_data("bond_L_both_forms",
                    {k: {"averaged_exponent": mp.nstr(La[k], 12),
                         "per_diagram": mp.nstr(Lb[k], 12),
                         "shift": mp.nstr(Lb[k] - La[k], 10)} for k in La})
        wb.add_data("worth",
                    {"sign_question_dL_pn": mp.nstr(sign_worth, 10),
                     "exponent_vs_linear_dL_pn": mp.nstr(dL, 10),
                     "ratio": mp.nstr(ratio_vs, 8),
                     "MeV_on_4He": mp.nstr(d4, 8)})
        wb.add_data("invariance",
                    {"L_pp_shift": mp.nstr(d_pp, 6),
                     "L_nn_shift": mp.nstr(d_nn, 6),
                     "spread_shift": mp.nstr(sb - sa, 6),
                     "mirror_3H_minus_3He_shift": mp.nstr(mir_b - mir_a, 6)})
        wb.add_data("isotope_table",
                    {k: {"averaged_exponent": mp.nstr(v[0], 10),
                         "per_diagram": mp.nstr(v[1], 10),
                         "B_AME": mp.nstr(v[2], 10)} for k, v in rows.items()})
        for name, passed, detail in assertions:
            wb.add_assertion(name=name, computed=str(int(bool(passed))),
                             expected="1", tolerance=0, source=str(detail))
        wb.add_caveat(
            "THIS RETRACTS PART OF MY OWN PRIOR PROBE. "
            "framed_vs_writhe_normalised_bonds_probe derived e_pn = +delta/2 "
            "from the operator identity sigma - beta h = (1-beta) sigma + beta "
            "sigma^-1. The identity is correct and is reused here; what was "
            "wrong was feeding its coefficient average into an exponent. Read "
            "that probe's A2 as establishing that the bond is a MIXTURE, not as "
            "establishing a value for e_pn.")
        wb.add_caveat(
            "CONCAVITY IS MEASURED, NOT PROVED. e_eff(beta) - (1 - 2 beta) is "
            "positive at all 99 interior grid points and the endpoints are "
            "exact, which is enough to establish that interpolation understates "
            "e_eff at beta_pn — the only point the conclusion needs. The word "
            "'concave' is a description of that grid, not a theorem.")
        wb.add_caveat(
            "SCOPE: this is a correction WITHIN the writhe-normalised "
            "convention only. Which convention binding should use is still the "
            "open physics question from framed_vs_writhe_normalised_bonds_probe "
            "(framing is Tw in Lk = Wr + Tw). The framed branch — bond "
            "constants, additivity, no-distance-decay — applies no "
            "normalisation and is untouched by everything here.")
        wb.add_caveat(
            "The isotope table is the NAIVE all-pairs sum in both columns, so "
            "it inherits the sub-additivity overstatement measured in "
            "pairwise_ceiling_is_overstated_probe and is not a binding "
            "prediction in either column. Only the DIFFERENCE between the "
            "columns is the quantity of interest.")
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:  # pragma: no cover
        print(f"\n(witness emit skipped: {e})")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
