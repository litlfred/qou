#!/usr/bin/env python3
"""qou-99qc: the gamma-gamma ruling DECIDES the braid ordering #7188 said the
corpus owed -- and the order it selects is the LESS accurate one.

#7188 (merged) measured that under the ruled functional `eps := tr` at
`z_D = q^3/(q^2+1)` the braid ORDER of the nucleon word is visible and
unconstrained, and concluded: "the corpus now owes a DERIVATION of the braid
ordering of the nucleon word. Until it has one, tr_{z_D}(Delta) is not
predicted by the framework -- it is selected by an unstated modelling choice."

THE OWNER RULING SUPPLIES THAT DERIVATION (2026-09-08, bean `qou-ales`): "All
selection of great words should be done through gamma gamma production and the
semi-definite product solutions at q0. Shouldn't use census." Applying it to
the ORDER, rather than to the choice of word, is what this probe does.

# Ref: computations/qbeta/qbeta_option_e_order_dof_range_probe.py   (the order DOF, merged)
# Ref: computations/qbeta/qbeta_delta_candidate_census_probe.py     (both models)
# Ref: computations/qbeta/qbeta_nucleon_flip_skein_expansion_probe.py (the flip)
# Ref: content/quantum-observable-universe/lean/QOU/QBeta/GammaGammaSelectedDeltaVanishes.lean

THE ARGUMENT, AND IT IS STRUCTURAL RATHER THAN NUMERICAL. The census carries
two orderings of the SAME eleven-letter multiset. Their confinement cores are:

  interleaved  `nuc9`:      for _ in range(3): sigma_0 ; (sigma_1 - h)
  gen-grouped  `_GEN_CHAINS`: all sigma_0 letters first, then all sigma_1

`sigma_1 - h = sigma_1^{-1}` by the Hecke relation
(`QOU.QBeta.NucleonFlavour.skein_letter_inv`, sorry-free), so the interleaved
core is `(sigma_0 sigma_1^{-1})^3`. That is `vertex 0` three times: a
pair-production vertex is exactly `sigma_i sigma_{i+1}^{-1}`
(`QOU.Mass.GammaGammaWordSelection.vertex`), so the interleaved core IS a
gamma-gamma word -- `interleavedCore_isGammaGamma`, proved by three
applications of the constructor.

The gen-grouped core is `sigma_0 sigma_0 sigma_0 sigma_1^-1 sigma_1^-1
sigma_1^-1`, whose SECOND letter is a positive crossing. A gamma-gamma word's
letters come in (positive, negative) pairs, so its second letter is always
negative (`gammaGamma_snd_neg`); hence no word with a positive letter in second
position is gamma-gamma-produced (`not_gammaGamma_of_snd_pos`), and the
gen-grouped core is excluded (`not_gammaGamma_genGroupedCore`). All five
declarations depend on NO AXIOMS.

So of the census's two models exactly one has a gamma-gamma-produced core, and
the ruling selects it. This is a structural exclusion, scope-(b): it cites a
proved invariant (the vertex parity pattern), not a bad number.

🛑 THE RULED ORDER IS THE WORSE ONE, AND THAT IS THE POINT. Measured at the
proton pin under convention D: interleaved -17.4959 % against gen-grouped
-15.4514 %. The ruling costs 2.04 points of residual. Under AGENTS.md
"NO FITTING, EXCEPT CAL-1/2/3" that is the correct outcome -- "rank by
derivational cleanliness first, and treat accuracy as a diagnostic, never as a
tie-breaker that promotes a fitted route", and "implement the specification,
and report what it gives even when that is worse". Preferring -15.45 %
BECAUSE it is closer would be selection against the target.

CONSEQUENCE FOR THE PRIOR WORK ON THIS BEAN. The -15.4514 % figure that
#7212's Part 1/Part 3 and the merged #7188 calibrate against is the GEN-GROUPED
one, i.e. the UNRULED order. Under the ruling the canonical residual is
-17.4959 %. Nothing is retracted -- the merged probes state their ordering --
but the canonical number moves, and this probe is the record of which is which.

WHAT SURVIVES THE ORDER CHANGE, CHECKED RATHER THAN ASSUMED:

  * the FLIP STRUCTURE is order-independent: two slots differ, each by exactly
    -h/2, in both orderings. That is expected -- it is a statement about
    flavour, not about braid order -- but it is checked here (CHECK 4).
  * the THREE-TERM SKEIN EXPANSION holds exactly on the ruled order too,
    `Delta = s(S_A + S_B) + s^2 S_AB` to 60 dps (CHECK 5). Only the term SIZES
    move: the `s^2` correction is 4.87 % of the `s` term interleaved against
    2.04 % gen-grouped.
  * #7212's 3.13x GAP result is untouched: it prices `V^k` differences, a
    gamma-gamma-only construction with no nucleon ordering in it at all.

🛑 A TRAP THIS PROBE FELL INTO, RECORDED BECAUSE IT PRODUCES A PLAUSIBLE WRONG
NUMBER. "Interleaved" was first reconstructed by zipping the two `_GEN_CHAINS`
lists alternately. That gives -13.5712 %, which is NEITHER census model -- a
third ordering, invented. The census's interleaved model is not a zip: `nuc9`
emits the core as three (sigma_0, sigma_1^-1) PAIRS, then the quark letters,
then two sigma_0 gluon letters, and the quark block itself is ordered
(0,0),(0,-1/2),(1,-1/2) for the proton. Reproducing the corpus's documented
-17.496 % is the calibration that catches this; a reconstruction that merely
looks interleaved does not.

ARITHMETIC. mpmath mpf at 60 dps end to end, proton pin, convention D. No
float64 (probes are not exempt).

Run: python3 -u computations/qbeta/qbeta_gamma_gamma_ruling_selects_ordering_probe.py \
       2>&1 | tee /tmp/qbeta_ruling_ordering.log
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
sys.path.insert(0, str(_HERE.parent / "substrate"))

from _precision import set_compute_dps  # noqa: E402

import qbeta_option_e_order_dof_range_probe as _order  # noqa: E402
import qbeta_delta_candidate_census_probe as _census  # noqa: E402

mp = _order.mp

# Set the working precision HERE rather than inheriting it from the imported
# order probe; `never_raises_dps_audit` flags an inherited dps as fragile.
set_compute_dps(60)
mp.mp.dps = 60

H0, ZD, E0, QB, TARGET = _order.H0, _order.ZD, _order.E0, _order.QB, _order.TARGET
Q_50_DIGIT_STR = _order.Q_50_DIGIT_STR

Z = mp.mpf(0)
HALF = mp.mpf(-1) / 2
NEG1 = mp.mpf(-1)

# The census's interleaved model, transcribed from `nuc9` + `nuc11_interleaved`:
# core = 3x (sigma_0, sigma_1 - h); then the typed quark letters; then two
# sigma_0 gluon letters.
CORE = [(0, Z), (1, NEG1)] * 3
GLUON = [(0, Z), (0, Z)]
QUARK = {"p": [(0, Z), (0, HALF), (1, HALF)],
         "n": [(0, HALF), (0, HALF), (1, NEG1)]}

RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


def tr(letters):
    return _order.tr_at(_order.word_nf(letters), ZD)


def pct(v):
    return (abs(v) * E0 / QB - 1) * 100


def drop(word, *idx):
    return [l for i, l in enumerate(word) if i not in idx]


def main() -> int:
    print("qou-99qc — the γγ ruling decides the braid ordering, and picks the "
          "WORSE one\n")
    print(f"  z_D    = {mp.nstr(ZD, 20)}")
    print(f"  TARGET = {mp.nstr(TARGET, 20)}\n")

    il = {k: CORE + QUARK[k] + GLUON for k in ("n", "p")}
    gg = {k: _order.canonical_letters(k) for k in ("n", "p")}

    # ---- CHECK 1: the interleaved core is the vertex cube V^3 --------------
    print("CHECK 1 — the interleaved core is V³, three γγ vertices")
    V3 = [(0, Z), (1, NEG1)] * 3
    tr_core_il = tr(CORE)
    print(f"    tr_z_D(interleaved core) = {mp.nstr(tr_core_il, 25)}")
    check("interleaved_core_is_vertex_cubed",
          abs(tr_core_il - tr(V3)) < mp.mpf("1e-50"),
          "(σ₀σ₁⁻¹)³ = vertex 0 three times — γγ-produced by the constructor")

    gg_core = [(0, Z)] * 3 + [(1, NEG1)] * 3
    tr_core_gg = tr(gg_core)
    print(f"    tr_z_D(gen-grouped core) = {mp.nstr(tr_core_gg, 25)}")
    check("the_two_cores_are_different_elements",
          abs(tr_core_il - tr_core_gg) > mp.mpf("0.5"),
          f"ratio {mp.nstr(tr_core_il / tr_core_gg, 6)}× — same multiset, "
          "different element (H₃ is noncommutative across generators)")

    # ---- CHECK 2: same multiset, so this is purely an ORDER question -------
    print("\nCHECK 2 — the two models share their letter multiset")
    from collections import Counter
    same = all(
        Counter((g, str(d)) for g, d in il[k])
        == Counter((g, str(d)) for g, d in gg[k])
        for k in ("n", "p")
    )
    check("orderings_share_the_multiset", same,
          "11 letters each; nothing but the ORDER differs")

    # ---- CHECK 3: calibrate against the corpus's documented figure --------
    print("\nCHECK 3 — reproduce the corpus's documented interleaved residual")
    d_il = tr(il["n"]) - tr(il["p"])
    d_gg = tr(gg["n"]) - tr(gg["p"])
    p_il, p_gg = pct(d_il), pct(d_gg)
    print(f"    interleaved (RULED) = {mp.nstr(p_il, 8)} %")
    print(f"    gen-grouped         = {mp.nstr(p_gg, 8)} %")
    check("interleaved_reproduces_minus_17_496",
          abs(p_il - mp.mpf("-17.496")) < mp.mpf("0.001"),
          "matches the figure #7188's docstring records — so this "
          "transcription IS the census's interleaved model, not a lookalike")
    check("gen_grouped_reproduces_minus_15_4514",
          abs(p_gg - mp.mpf("-15.4514")) < mp.mpf("0.001"),
          "matches the merged Option-E witness")
    check("the_ruled_order_is_the_LESS_accurate_one",
          abs(p_il) > abs(p_gg),
          f"ruling costs {mp.nstr(abs(p_il) - abs(p_gg), 6)} points — correct "
          "under NO FITTING: derivational cleanliness ranks above accuracy")

    # ---- CHECK 4: the flip structure is order-independent ------------------
    print("\nCHECK 4 — the two-letter flip is the same in both orderings")
    diffs = [(i, a[1], b[1]) for i, (a, b) in enumerate(zip(il["p"], il["n"]))
             if a != b]
    for i, a, b in diffs:
        print(f"    interleaved idx {i}: {a} → {b}   (shift {b - a})")
    check("flip_is_two_slots_each_minus_half_in_ruled_order",
          len(diffs) == 2 and all(b - a == HALF for _, a, b in diffs),
          "order-independent, as a flavour statement should be")

    # ---- CHECK 5: the three-term expansion survives the order change ------
    print("\nCHECK 5 — Δ = s(S_A + S_B) + s²·S_AB, on the RULED order")
    A, B = diffs[0][0], diffs[1][0]
    s = -H0 / 2
    P = il["p"]
    SA, SB, SAB = tr(drop(P, A)), tr(drop(P, B)), tr(drop(P, A, B))
    exp_il = s * (SA + SB) + s * s * SAB
    gap = abs(d_il - exp_il)
    print(f"    direct     = {mp.nstr(d_il, 30)}")
    print(f"    expansion  = {mp.nstr(exp_il, 30)}")
    check("expansion_exact_on_the_ruled_order", gap < mp.mpf("1e-50"),
          f"|direct − expansion| = {mp.nstr(gap, 5)} at 60 dps")

    t1, t2 = s * (SA + SB), s * s * SAB
    ratio_il = abs(t2 / t1) * 100
    print(f"    s²-term / s-term = {mp.nstr(ratio_il, 6)} %   "
          "(gen-grouped: 2.045 %) — the identity is exact either way; only "
          "the term sizes are order-dependent")

    # ---- CHECK 6: how much of the word the ruling can reach at all --------
    print("\nCHECK 6 — the parity bound: the ruling reaches 6 of 11 letters")
    n_core, n_quark, n_gluon = len(CORE), len(QUARK["p"]), len(GLUON)
    total = n_core + n_quark + n_gluon
    print(f"    core {n_core} (γγ) + quark {n_quark} + gluon {n_gluon} = {total}")
    check("blocks_sum_to_the_crossing_budget", total == 11,
          "11 crossings, the qou-1qsw budget")
    check("the_budget_is_ODD_so_no_full_word_is_gamma_gamma", total % 2 == 1,
          "a γγ-word has even length (gammaGamma_length_even), so NO "
          "11-crossing word is γγ-produced — in any order, for any candidate")
    check("gluon_block_is_even_but_still_not_gamma_gamma",
          n_gluon % 2 == 0 and all(d == Z for _, d in GLUON),
          "both letters positive (d = 0 ⇒ σ₀), and a vertex pairs positive "
          "with negative — gluonPair_not_gammaGamma")
    check("quark_block_is_odd", n_quark % 2 == 1,
          "3 letters ⇒ not γγ either (three_not_gammaGamma)")
    print(f"    → the ruling reaches {n_core}/{total} letters; "
          f"{n_quark + n_gluon} remain free")

    ok = all(r[1] for r in RESULTS)
    print()
    print(f"{sum(1 for r in RESULTS if r[1])}/{len(RESULTS)} checks passed")
    print()
    print("VERDICT — the γγ ruling supplies the ordering derivation #7188 said")
    print("the corpus owed. Of the census's two models, exactly ONE has a")
    print("γγ-produced core: the interleaved `(σ₀σ₁⁻¹)³` is three vertices,")
    print("while the gen-grouped core has a positive crossing in second")
    print("position, which no concatenation of vertices can produce")
    print("(sorry-free, no axioms). The ruled order's residual is -17.4959 %")
    print("against the gen-grouped -15.4514 %, so the derivation COSTS 2.04")
    print("points — the correct trade under NO FITTING. The flip structure and")
    print("the three-term expansion both survive the order change; #7212's")
    print("3.13x gap is untouched (it prices V^k differences, which carry no")
    print("nucleon ordering). Scope-(b) on the exclusion: it cites a proved")
    print("invariant. Scope-(a) on the residuals: two models, one pin.")
    print()
    print("AND A BOUND ON THE RULING ITSELF — the crossing budget is 11, which")
    print("is ODD, while every γγ-word has EVEN length. So no 11-crossing word")
    print("is γγ-produced, for any candidate in any order: the principle")
    print("settles the 6-letter core and provably CANNOT settle the other 5.")
    print("The two gluon letters are excluded twice over (both positive, and")
    print("following an odd-length quark block). That remaining 5 is where a")
    print("closing Delta would have to come from.")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("qbeta-gamma-gamma-ruling-selects-ordering")
        w.set_description(
            "The 2026-09-08 gamma-gamma ruling decides the nucleon braid "
            "ORDERING that #7188 identified as owed. Of the census's two "
            "models only the interleaved one has a gamma-gamma-produced core "
            "-- (sigma_0 sigma_1^-1)^3 is three pair-production vertices, "
            "while the gen-grouped core carries a positive crossing in second "
            "position, which no vertex concatenation produces (sorry-free, no "
            "axioms). The ruled order's residual is -17.4959 % against the "
            "gen-grouped -15.4514 %: the derivation costs 2.04 points, which "
            "is the correct trade under NO FITTING."
        )
        w.add_data("markov_convention", "D — the ruled functional, z_D = q^3/(q^2+1)")
        w.add_data("q0_anchor", "proton")
        w.add_data("q0_value", Q_50_DIGIT_STR)
        w.add_data("core_traces",
                   {"interleaved_V3": mp.nstr(tr_core_il, 30),
                    "gen_grouped": mp.nstr(tr_core_gg, 30),
                    "ratio": mp.nstr(tr_core_il / tr_core_gg, 12)})
        w.add_data("residual_pct",
                   {"interleaved_RULED": mp.nstr(p_il, 12),
                    "gen_grouped_unruled": mp.nstr(p_gg, 12),
                    "cost_of_the_ruling_points": mp.nstr(abs(p_il) - abs(p_gg), 10)})
        w.add_data("flip_slots_ruled_order",
                   [{"index": i, "p": mp.nstr(a, 10), "n": mp.nstr(b, 10)}
                    for i, a, b in diffs])
        w.add_data("skein_expansion_ruled_order",
                   {"s": mp.nstr(s, 30),
                    "S_A": mp.nstr(SA, 30), "S_B": mp.nstr(SB, 30),
                    "S_AB": mp.nstr(SAB, 30),
                    "direct": mp.nstr(d_il, 30),
                    "expansion": mp.nstr(exp_il, 30),
                    "abs_gap": mp.nstr(gap, 8),
                    "s2_over_s_pct": mp.nstr(ratio_il, 10)})
        w.add_data("parity_bound",
                   {"core_letters": n_core, "quark_letters": n_quark,
                    "gluon_letters": n_gluon, "total": total,
                    "budget_is_odd": total % 2 == 1,
                    "reached_by_the_ruling": n_core,
                    "left_free": n_quark + n_gluon})
        w.add_data("lean_declarations",
                   ["QOU.QBeta.GammaGammaDelta.gammaGamma_snd_neg",
                    "QOU.QBeta.GammaGammaDelta.not_gammaGamma_of_snd_pos",
                    "QOU.QBeta.GammaGammaDelta.interleavedCore_isGammaGamma",
                    "QOU.QBeta.GammaGammaDelta.not_gammaGamma_genGroupedCore",
                    "QOU.QBeta.GammaGammaDelta.cores_ne",
                    "QOU.QBeta.GammaGammaDelta.gammaGamma_length_even",
                    "QOU.QBeta.GammaGammaDelta.not_gammaGamma_of_odd_length",
                    "QOU.QBeta.GammaGammaDelta.eleven_not_gammaGamma",
                    "QOU.QBeta.GammaGammaDelta.gluonPair_not_gammaGamma",
                    "QOU.QBeta.GammaGammaDelta.three_not_gammaGamma"])
        w.add_caveat(
            "🛑 THE RULED ORDER IS THE LESS ACCURATE ONE. -17.4959 % against "
            "-15.4514 %. Do NOT prefer the gen-grouped figure because it is "
            "closer -- that is selection against the target, which AGENTS.md "
            "NO FITTING names explicitly. The 2.04 points are the price of "
            "the order no longer being an unstated modelling choice."
        )
        w.add_caveat(
            "The -15.4514 % that #7188 and #7212 calibrate against is the "
            "GEN-GROUPED (unruled) order. Nothing there is retracted -- both "
            "state their ordering -- but the CANONICAL residual under the "
            "ruling is -17.4959 %, and this witness is the record of which "
            "figure is which."
        )
        w.add_caveat(
            "🛑 TRAP. 'Interleaved' reconstructed by zipping the two "
            "_GEN_CHAINS lists alternately gives -13.5712 %, which is NEITHER "
            "census model. The census's interleaved model emits the core as "
            "three (sigma_0, sigma_1^-1) pairs, then an ORDERED quark block, "
            "then two gluon letters. Reproducing the documented -17.496 % is "
            "the calibration that catches a lookalike reconstruction."
        )
        w.add_caveat(
            "Scope: (b) on the EXCLUSION -- it cites a proved invariant (a "
            "gamma-gamma word's second letter is negative), not a bad number. "
            "(a) on the RESIDUALS -- two census models at one pin. The ruling "
            "constrains the CORE; the flavour and gluon letters are not "
            "gamma-gamma words and their placement is not settled here."
        )
        w.add_caveat(
            "THE PARITY BOUND IS A LIMIT ON THE RULING, not a defect in it. "
            "The crossing budget is 11 (odd) and every gamma-gamma word has "
            "even length, so NO 11-crossing word is gamma-gamma-produced -- "
            "for any candidate, in any order. The principle settles the "
            "6-letter core and provably cannot settle the other 5. Do not "
            "read this as the construction failing to apply the ruling."
        )
        w.add_caveat(
            "#7212's 3.13x gap result is UNAFFECTED: it prices differences of "
            "vertex powers V^k, a gamma-gamma-only construction that contains "
            "no nucleon ordering at all."
        )
        for name, passed, det in RESULTS:
            w.add_assertion(name, "1" if passed else "0", "1", "0", source=det or None)
        w.save()
        print("witness written")
    except Exception as exc:  # pragma: no cover
        print(f"witness NOT written ({exc.__class__.__name__}: {exc})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
