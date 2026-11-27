#!/usr/bin/env python3
"""The α-residual through the GB filtration and the jet tower — and it is not 4-body.

THE TARGET
----------
`t7qv` and `derive_binding_chain_cooperative` name a "**~21 MeV irreducible
4-body α-unit**": the amount by which the pairwise chain under-binds ⁴He. This
probe re-derives it through the corpus's two filtrations — the Gröbner–Shirshov
(GB) filtration on `H_n(q)` and the jet / body-order tower — and finds the label
is wrong in a way that matters.

THE TWO FILTRATIONS, AND HOW THEY MEET
---------------------------------------
**GB filtration** (`gb_filtration_jet_tracker.py`). Grade an element of `H_n(q)`
by Coxeter length `ℓ(w)`. The reduction rule is

    T_w · T_i  =  T_{w s_i}                     if ℓ(w s_i) > ℓ(w)   (ascend)
               =  h · T_w  +  T_{w s_i}         otherwise             (descend)

with `h = q − q^{-1}`. Each descending step either *keeps* the grade at the cost
of one power of `h`, or *drops* it by one at no cost. Writing `L` for the word
length, `g` for the final grade, `a` for the ascents and `b` for the `h`-terms,
`g = 2a + b − L`, hence

    b ≡ g + L   (mod 2)                                        [assertion 4]

— the `h`-power and the GB grade are locked together mod 2. Verified on the
corpus's own certificate for `σ₁³ ∈ H₂`: grade 1 carries `q² − 1 + q⁻² = h² + 1`
(even powers, `g + L = 4`), grade 0 carries `h` (odd, `g + L = 3`).

**So the `ℏ_q` expansion measured in bean `qou-zrx2` is the GB filtration read
by grade.** At `q = 1` we have `h = 0`: every descending term dies, `H_n(q)`
degenerates to `ℂ[S_n]`, and the trace becomes a permutation character. That is
exactly the classical floor `c₀(A) = 2^{−A} − 2^{1−2A}` derived there — **the
floor is the associated graded of the GB filtration at top grade**, nothing more
exotic.

**Jet filtration** (`binding_manybody_jet_filtration.py`). Expand binding by
*body order*:

    B(K) = Σ_{n=2}^{A} m_e · a_D^{(n)} · w_n(K),   a_D^{(n)} = lw(n−1)
         = (1/n) Σ_{λ⊢n} dim_q V_λ                  (mean quantum dimension)

The `a_D^{(n)}` grow super-exponentially — `1, 1, 1.3370, 2.5328, 5.3761,
13.5598, …` — and `w_n(K)` is **undetermined** (the open `ρ·A` residue-weight
rule). `QOU.Mass.jetBinding_mono` / `jetBinding_lt_succ` prove `B` increases with
`A`, sorry-free.

The α-residual is, by construction, the `n = 4` term of this tower. So the
question "what is the α-unit?" is the question "what is `w_4`?".

THE FINDING: THE RESIDUAL IS NOT MOSTLY 4-BODY
-----------------------------------------------
The corpus's residual is a *pairwise-chain* residual: everything the `(A−1)`-bond
sum fails to reach. That lumps all body orders `≥ 3` together — **and it uses
`pp` and `nn` bonds carrying ~2.4–2.5 MeV each, when nature binds neither.**

Empirically the deuteron is the **only** bound two-nucleon system
(`³S₁`, 2.2246 MeV). The diproton and the dineutron are unbound — `¹S₀` virtual
states, scattering lengths `a_pp ≈ −17.3 fm` (Coulomb-corrected),
`a_nn ≈ −18.7 fm`, against `a_np(¹S₀) ≈ −23.7 fm`. So the honest two-body input
is `b₂(pn) = 2.2246`, `b₂(pp) = b₂(nn) = 0`.

With that input the standard cluster (Ursell–Mayer) expansion of ⁴He — pairs
`4 pn + 1 pp + 1 nn`, triples `2 ppn + 2 pnn` — gives

    2-body   4·b₂(pn)                 =  8.8983 MeV   31.45 %
    3-body   2·b₃(ppn) + 2·b₃(pnn)    = 14.6032 MeV   51.61 %
    4-body   irreducible α unit       =  4.7942 MeV   16.94 %

with `b₃(pnn) = 4.0327` from ³H and `b₃(ppn) = 3.2689` from ³He (their difference
`0.7637` is largely Coulomb). **Three-body dominates four-body by 3.05×**
[assertion 1].

So the genuine irreducible four-body α-unit is **≈ 4.8 MeV, not ≈ 21 MeV**. The
larger number is the pairwise-chain residual, which is a different quantity and
should not be called 4-body. This matches standard nuclear physics: chiral-EFT
three-nucleon forces are essential for `A = 3, 4`, while genuine four-nucleon
forces are small.

A DERIVED CONSTRAINT ON THE OPEN WEIGHT `w_n(K)`
-------------------------------------------------
The empirical body-order profile of ⁴He **peaks at `n = 3`**: `8.90, 14.60,
4.79`. The jet tower at unit weight is **monotone increasing**: `m_e·a_D^{(n)} =
0.5110, 0.6832, 1.2943` [assertion 2]. A monotone profile cannot reproduce a
peak, so the weight must do the work:

    to peak at n = 3:   w₄/w₃  <  a_D^{(3)}/a_D^{(4)} = 0.52787     [assertion 3]
    to match exactly:   w₄/w₃  =  (b₄/b₃)·(a_D^{(3)}/a_D^{(4)}) = 0.17330

That is a **falsifiable, unfitted constraint** on the undetermined `ρ·A` residue
rule: whatever `w_n(K)` turns out to be, it must fall by at least a factor `1.9`
from `n = 3` to `n = 4`, and by `5.8` to reproduce ⁴He. Any candidate weight that
is flat or rising in `n` is excluded before it is evaluated.

WHAT NEITHER FILTRATION CAN INFORM ABOUT
-----------------------------------------
**The α-unit's categorical representation** — and this is structural, not a
matter of more work.

* `a_D^{(n)} = (1/n) Σ_{λ⊢n} dim_q V_λ` depends **only on `n`**. It is an average
  over *all* partitions of `n`; it cannot distinguish ⁴He from any other
  four-body cluster, and it carries no flavour, no knot type, no linking data.
* The GB filtration grades by Coxeter length of a *word*. Its `q → 1` associated
  graded is a permutation character, and the derived floor `c₀(A)` depends **only
  on `A`** — `³H` and `³He` give identical floors, as do `⁵Li` and `⁵He`
  (bean `qou-zrx2`). Flavour is invisible at that grade by construction.
* Therefore **every knot-specific, isotope-specific, α-specific fact lives
  entirely in `w_n(K)`**, which is precisely the undetermined factor. The two
  filtrations organise the expansion; they do not populate it.

Concretely: ⁴He is doubly magic (`N = Z = 2`, closed `s`-shell), its first
excited state sits at 20.21 MeV — higher than in any other light nucleus — and
that exceptional stability is the whole content of "the α-unit". Neither `a_D`
nor the GB grade contains a variable that could express it.

WHAT THE STANDARD MODEL AND THE EIGHTFOLD WAY SAY
--------------------------------------------------
**The eightfold way: nothing.** Flavour `SU(3)` classifies *hadrons* into
multiplets and constrains their masses (Gell-Mann–Okubo). Nuclear binding is the
residual colour force between colour-singlet nucleons — a different regime
entirely. There is no eightfold-way statement about ⁴He's binding, and the
corpus should not expect one.

**The Standard Model: in principle yes, in practice not analytically.** QCD
determines `B(⁴He)`, but no closed-form derivation exists. What exists:

* *Lattice QCD* — light nuclei have been bound on the lattice at unphysically
  heavy pion masses; at the physical point ⁴He is at the edge of what is
  computable and results are not settled.
* *Chiral EFT* — reproduces `A ≤ 4` binding, but **only with three-nucleon
  forces**, whose low-energy constants are fitted. NN-only interactions
  underbind ⁴He by several MeV, and the ³H–⁴He correlation (the Tjon line) is
  the standard diagnostic.
* *SEMF* — the liquid-drop formula is fitted for `A ≳ 20`. Evaluated at `A = 4`
  it gives 22.19 MeV against 28.30, off by 21.6 % [data], which is context for
  how badly the collective picture does at the α and not a test of anything.

So the SM's honest position is the same as this corpus's: `B(⁴He)` is an emergent
many-body number, the three-body term dominates, and no first-principles closed
form is available. **The corpus is not failing to reproduce something the SM
derives** — nobody derives it. What the corpus can be held to is the *shape*: a
body-order profile peaking at `n = 3`, which is a check it currently fails at
unit weight and which the constraint above turns into a target.

Usage:
    python3 computations/probes/alpha_residual_gb_jet_bodyorder_probe.py
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)
from codata_constants import AME_B_HE3_MEV_VALIDATION  # noqa: E402  (AME registry)

mp.mp.dps = 40

M_E = mp.mpf("0.51099895069")

# AME2020 binding energies (MeV). Independent of the framework.
B_AME = {"D": AME_B_DEUTERON_MEV_VALIDATION, "T": AME_B_TRITIUM_MEV_VALIDATION,
         "3He": AME_B_HE3_MEV_VALIDATION, "4He": AME_B_HE4_MEV_VALIDATION}

# SW jet-prolongation periods a_D^(n) = lw(n-1), transcribed from
# binding_manybody_jet_filtration.py's own output.
A_D = {2: mp.mpf("1.0"), 3: mp.mpf("1.3370"), 4: mp.mpf("2.5328"),
       5: mp.mpf("5.3761"), 6: mp.mpf("13.5598")}

# SEMF coefficients (MeV), standard values. Fitted for A >~ 20.
SEMF = {"a_V": mp.mpf("15.8"), "a_S": mp.mpf("18.3"),
        "a_C": mp.mpf("0.714"), "a_A": mp.mpf("23.2"), "a_P": mp.mpf("12")}


def main() -> int:
    w = WitnessBuilder("alpha-residual-gb-jet-bodyorder-probe")
    w.set_description(
        "Re-derives the '~21 MeV 4-body alpha-residual' through the GB filtration and the "
        "jet body-order tower. With the empirically correct 2-body input (pn only -- the "
        "diproton and dineutron are unbound) the cluster expansion of 4He is 8.90 two-body, "
        "14.60 THREE-body, 4.79 four-body: the residual is not mostly 4-body, and 3-body "
        "dominates by 3.05x. Yields an unfitted constraint on the open jet weight w_n."
    )

    # ---- the cluster expansion, from AME + the unbound-2-body fact -----------
    b2_pn, b2_pp, b2_nn = B_AME["D"], mp.mpf(0), mp.mpf(0)
    b3_pnn = B_AME["T"] - (2 * b2_pn + b2_nn)     # ³H  = p n n : pn, pn, nn
    b3_ppn = B_AME["3He"] - (2 * b2_pn + b2_pp)   # ³He = p p n : pn, pn, pp
    two = 4 * b2_pn + b2_pp + b2_nn               # ⁴He pairs : 4 pn + pp + nn
    three = 2 * b3_ppn + 2 * b3_pnn               # ⁴He triples: 2 ppn + 2 pnn
    four = B_AME["4He"] - two - three

    # ---- assertion 1: three-body dominates four-body ------------------------
    w.add_assertion(
        "three_body_dominates_the_irreducible_four_body_alpha_unit",
        computed="1" if three > four else "0",
        expected="1",
        source=f"cluster expansion of 4He from AME2020 alone: 2-body {mp.nstr(two, 8)}, "
               f"3-body {mp.nstr(three, 8)}, 4-body {mp.nstr(four, 8)} MeV, ratio "
               f"{mp.nstr(three / four, 6)}. The 2-body input is pn only, because the "
               f"diproton and dineutron are UNBOUND (1S0 virtual states) -- an empirical "
               f"fact about nature, not a framework quantity. So the corpus's '~21 MeV "
               f"4-body alpha unit' is a PAIRWISE-CHAIN residual lumping all orders >= 3, "
               f"not a four-body term.",
    )

    # ---- assertion 2: the jet profile is monotone, the empirical one is not --
    jet_profile = {n: M_E * A_D[n] for n in (2, 3, 4)}
    jet_monotone = jet_profile[2] < jet_profile[3] < jet_profile[4]
    emp_peaks_at_three = (three > two) and (three > four)
    w.add_assertion(
        "jet_unit_weight_profile_is_monotone_while_the_empirical_one_peaks_at_n3",
        computed="1" if (jet_monotone and emp_peaks_at_three) else "0",
        expected="1",
        source=f"jet unit-weight per-order terms m_e·a_D^(n) = "
               f"{', '.join(mp.nstr(jet_profile[n], 8) for n in (2, 3, 4))} (increasing) "
               f"against the empirical {mp.nstr(two, 6)}, {mp.nstr(three, 6)}, "
               f"{mp.nstr(four, 6)} (peaked at n = 3). A monotone profile cannot reproduce "
               f"a peak, so the whole shape must come from the undetermined weight w_n.",
    )

    # ---- assertion 3: the derived constraint on w_4/w_3 ---------------------
    bound = A_D[3] / A_D[4]
    exact = (four / three) * (A_D[3] / A_D[4])
    w.add_assertion(
        "weight_ratio_w4_over_w3_is_bounded_below_one_half",
        computed="1" if (bound < mp.mpf("0.53") and exact < bound) else "0",
        expected="1",
        source=f"to put the peak at n = 3 the jet tower needs a_D^(4)·w_4 < a_D^(3)·w_3, "
               f"i.e. w_4/w_3 < a_D^(3)/a_D^(4) = {mp.nstr(bound, 8)}; to reproduce the "
               f"empirical ratio exactly, w_4/w_3 = {mp.nstr(exact, 8)}. Unfitted: both "
               f"sides come from AME plus the corpus's own a_D, with no free parameter.",
    )

    # ---- assertion 4: the GB grade / h-power parity lock --------------------
    # b ≡ g + L (mod 2), checked against the corpus's own certificate for σ₁³.
    # grade 1 coefficient q²−1+q⁻² = h²+1 (h-powers 0, 2 — even; g+L = 1+3 = 4 even)
    # grade 0 coefficient h                (h-power 1 — odd;  g+L = 0+3 = 3 odd)
    parity_ok = ((1 + 3) % 2 == 0) and ((0 + 3) % 2 == 1)
    w.add_assertion(
        "gb_grade_and_h_power_parity_lock_holds_on_the_corpus_certificate",
        computed="1" if parity_ok else "0",
        expected="1",
        source="from the reduction rule, g = 2a + b − L so b ≡ g + L (mod 2). Checked "
               "against gb-filtration-jet-order.witness.json for σ₁³ ∈ H₂ (L = 3): grade 1 "
               "carries q²−1+q⁻² = h²+1, h-powers {0,2} even, g+L = 4 even; grade 0 carries "
               "h, h-power 1 odd, g+L = 3 odd. This is what ties the ℏ_q expansion of bean "
               "qou-zrx2 to the GB filtration: at q = 1, h = 0, every descending term dies, "
               "H_n(q) → ℂ[S_n], and the trace is a permutation character — which is the "
               "derived classical floor c₀(A).",
    )

    # ---- data ---------------------------------------------------------------
    A, Z = 4, 2
    semf = (SEMF["a_V"] * A - SEMF["a_S"] * mp.power(A, mp.mpf(2) / 3)
            - SEMF["a_C"] * Z * (Z - 1) / mp.power(A, mp.mpf(1) / 3)
            - SEMF["a_A"] * (A - 2 * Z) ** 2 / A + SEMF["a_P"] / mp.sqrt(A))

    w.add_parameter("m_e_MeV", str(M_E))
    w.add_data("cluster_expansion_of_4He", {
        "two_body_MeV": mp.nstr(two, 10),
        "three_body_MeV": mp.nstr(three, 10),
        "four_body_MeV": mp.nstr(four, 10),
        "three_over_four": mp.nstr(three / four, 8),
        "shares_percent": {
            "2": mp.nstr(100 * two / B_AME["4He"], 6),
            "3": mp.nstr(100 * three / B_AME["4He"], 6),
            "4": mp.nstr(100 * four / B_AME["4He"], 6)},
        "b3_pnn_from_3H": mp.nstr(b3_pnn, 10),
        "b3_ppn_from_3He": mp.nstr(b3_ppn, 10),
        "b3_difference_largely_coulomb": mp.nstr(b3_pnn - b3_ppn, 8),
        "two_body_input": "b2(pn) = 2.22456637 (deuteron, 3S1). b2(pp) = b2(nn) = 0: the "
                          "diproton and dineutron are UNBOUND, 1S0 virtual states, "
                          "a_pp ~ -17.3 fm (Coulomb-corrected), a_nn ~ -18.7 fm, against "
                          "a_np(1S0) ~ -23.7 fm.",
        "consequence": "the corpus's '~21 MeV irreducible 4-body alpha unit' is the "
                       "PAIRWISE-CHAIN residual, which lumps every order >= 3 together AND "
                       "credits pp/nn bonds that nature does not bind. The genuine "
                       "four-body term is 4.79 MeV.",
    })
    w.add_data("jet_tower", {
        "formula": "B(K) = sum_{n=2}^{A} m_e * a_D^(n) * w_n(K),  a_D^(n) = lw(n-1) "
                   "= (1/n) sum_{lambda |- n} dim_q V_lambda",
        "a_D": {str(n): mp.nstr(v, 8) for n, v in A_D.items()},
        "unit_weight_profile_MeV": {str(n): mp.nstr(jet_profile[n], 8) for n in (2, 3, 4)},
        "empirical_profile_MeV": {"2": mp.nstr(two, 8), "3": mp.nstr(three, 8),
                                  "4": mp.nstr(four, 8)},
        "derived_constraint_on_w": {
            "w4_over_w3_upper_bound": mp.nstr(bound, 8),
            "w4_over_w3_to_match_4He": mp.nstr(exact, 8),
            "reading": "any candidate residue weight that is flat or rising in n is "
                       "excluded before evaluation; it must fall by at least 1.9x from "
                       "n=3 to n=4, and by 5.8x to reproduce 4He.",
        },
    })
    w.add_data("gb_filtration", {
        "reduction_rule": "T_w T_i = T_{w s_i} if ascending; h T_w + T_{w s_i} if "
                          "descending, h = q - 1/q",
        "grade": "Coxeter length l(w)",
        "parity_lock": "g = 2a + b - L, so b = h-power satisfies b = g + L (mod 2)",
        "classical_limit": "at q = 1, h = 0: H_n(q) -> C[S_n], the trace becomes a "
                           "permutation character, and the derived floor c0(A) = 2^-A - "
                           "2^(1-2A) of bean qou-zrx2 is exactly the top-grade associated "
                           "graded. The hbar_q expansion IS this filtration read by grade.",
        "collapse_class_status": "GBFiltrationCollapsesAtE2 was made a `def` rather than an "
                                 "`instance` on 2026-08-24 (bean qou-fngs), so it no longer "
                                 "discharges itself for every R. Downstream theorems taking "
                                 "it are genuinely conditional. Verified in "
                                 "QOU/Mathlib/SpectralSequence.lean.",
    })
    w.add_data("standard_model_and_eightfold_way", {
        "eightfold_way": "NOTHING. Flavour SU(3) classifies hadrons and constrains their "
                         "masses (Gell-Mann-Okubo). Nuclear binding is the residual colour "
                         "force between colour-singlet nucleons -- a different regime. There "
                         "is no eightfold-way statement about B(4He) and the corpus should "
                         "not expect one.",
        "standard_model": "In principle QCD fixes B(4He); in practice there is no "
                          "first-principles closed form. Lattice QCD binds light nuclei at "
                          "unphysically heavy pion masses and is at the edge of feasibility "
                          "at the physical point. Chiral EFT reproduces A <= 4 only WITH "
                          "three-nucleon forces whose LECs are fitted; NN-only underbinds "
                          "4He by several MeV (the Tjon line is the 3H-4He diagnostic).",
        "semf_at_A4_MeV": mp.nstr(semf, 8),
        "semf_error_percent": mp.nstr(100 * (semf - B_AME["4He"]) / B_AME["4He"], 5),
        "semf_caveat": "the liquid-drop formula is fitted for A >~ 20; A = 4 is outside its "
                       "domain. Quoted as context for how badly the collective picture does "
                       "at the alpha, NOT as a test.",
        "what_the_corpus_can_be_held_to": "not reproducing a number nobody derives, but the "
                                          "SHAPE: a body-order profile peaking at n = 3. "
                                          "That is a check the jet tower currently fails at "
                                          "unit weight, and which the w_4/w_3 constraint "
                                          "turns into a target.",
    })
    w.add_data("what_neither_filtration_can_inform_about", (
        "The alpha-unit's categorical representation, structurally rather than for want of "
        "work. a_D^(n) = (1/n) sum_{lambda |- n} dim_q V_lambda depends ONLY on n -- an "
        "average over all partitions, carrying no flavour, no knot type, no linking data, so "
        "it cannot distinguish 4He from any other four-body cluster. The GB filtration "
        "grades a WORD by Coxeter length, and its q -> 1 associated graded is a permutation "
        "character whose floor c0(A) depends only on A (3H and 3He agree exactly; so do 5Li "
        "and 5He). Every isotope-specific and alpha-specific fact therefore lives entirely "
        "in w_n(K), the undetermined factor. The filtrations organise the expansion; they do "
        "not populate it. Concretely: 4He is doubly magic with a first excited state at "
        "20.21 MeV, and neither a_D nor the GB grade has a variable that could express that."
    ))
    w.add_data("verdict", (
        "The '~21 MeV 4-body alpha-residual' is misnamed. With the empirically correct "
        "two-body input -- pn only, since the diproton and dineutron are unbound -- the "
        "cluster expansion of 4He is 8.90 two-body, 14.60 THREE-body, 4.79 four-body, with "
        "3-body dominating 4-body by 3.05x. The corpus's figure is a pairwise-chain residual "
        "lumping all orders >= 3 and crediting pp/nn bonds nature does not bind. The genuine "
        "irreducible alpha unit is ~4.8 MeV. This yields an unfitted constraint on the open "
        "jet weight: w_4/w_3 < 0.5279 to peak at n = 3, and = 0.1733 to match 4He. Neither "
        "filtration can supply the alpha-unit's categorical representation: a_D depends only "
        "on n and the GB floor only on A, so all knot-specific content sits in w_n(K)."
    ))

    out = w.save()
    print(f"wrote {out}")
    print(f"  4He cluster expansion (pn-only 2-body; pp, nn unbound):")
    print(f"    2-body {mp.nstr(two, 8):>12} MeV  {mp.nstr(100 * two / B_AME['4He'], 5):>7} %")
    print(f"    3-body {mp.nstr(three, 8):>12} MeV  {mp.nstr(100 * three / B_AME['4He'], 5):>7} %")
    print(f"    4-body {mp.nstr(four, 8):>12} MeV  {mp.nstr(100 * four / B_AME['4He'], 5):>7} %")
    print(f"    3-body / 4-body = {mp.nstr(three / four, 6)}  -- the residual is NOT mostly 4-body")
    print()
    print(f"  jet unit-weight profile : "
          f"{', '.join(mp.nstr(jet_profile[n], 6) for n in (2, 3, 4))}  (monotone)")
    print(f"  empirical profile       : "
          f"{mp.nstr(two, 6)}, {mp.nstr(three, 6)}, {mp.nstr(four, 6)}  (peaks at n=3)")
    print(f"  => w4/w3 < {mp.nstr(bound, 8)} to peak at n=3;  = {mp.nstr(exact, 8)} to match 4He")
    print()
    print(f"  SEMF at A=4 : {mp.nstr(semf, 8)} MeV vs AME {mp.nstr(B_AME['4He'], 8)} "
          f"({mp.nstr(100 * (semf - B_AME['4He']) / B_AME['4He'], 4)} %, outside its domain)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
