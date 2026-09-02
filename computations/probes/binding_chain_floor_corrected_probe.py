#!/usr/bin/env python3
"""The binding chain with the classical floor removed — pairwise additivity improves.

WHY
---
`qou-zrx2` showed the signed categorical trace difference carries an `ℏ_q^0`
classical floor, and `classical_floor_derivation_probe` derived it:

    c₀(A) = 2^{−A} − 2^{1−2A}        exact, every A

`derive_binding_chain_cooperative` builds nuclear binding as a sum over the
`(A−1)` bonds of a chain, each bond a **2-nucleon** sub-braid. So the chain
accumulates `(A−1)·c₀(2) = (A−1)/8` of floor, while the whole-atom trace carries
only `c₀(A)`. The two do not match, and the mismatch is not physics.

This probe re-runs the comparison with the floor removed from both sides.

WHAT IT FINDS
-------------
**Pairwise additivity improves substantially** [assertion 1, 2]. Comparing the
chain sum against the exact whole-atom trace difference:

    isotope   chain/atom raw    chain/atom, floors removed
    ----------------------------------------------------------
    D         1.0000            1.0000        (D *is* the pn bond)
    T         1.2812            1.1178
    ³He       1.1927            1.0198
    ⁴He       1.4706            1.1941

Worst-case deviation from exact additivity falls from **47.1 % to 19.4 %**, and
³He lands within **2 %**. The pairwise-chain picture is a much better description
of the exact `H_{3A}` trace than it looked.

The reduction is `(A−1)·c₀(2) − c₀(A)` exactly — identically true given the
definitions, so it is reported as data rather than asserted. What is *not*
forced, and is the finding, is that removing a quantity with no free parameters
moves the ratios toward 1 in every case.

**So part of the "many-body residual" was floor bookkeeping.** At ⁴He the
pairwise-vs-exact trace gap is `0.5270`; `0.3203` of that — **60.8 %** — is the
floor mismatch alone [data].

AND WHAT IT COSTS, REPORTED PLAINLY
------------------------------------
Trace additivity improves; the **binding** residual does not. Against AME, with
convention A (`E₀ = 4.18598 MeV`, what the chain producer actually uses):

    ⁴He   chain raw       6.894 MeV   →  residual 21.40 MeV
          chain corrected 5.324 MeV   →  residual 22.97 MeV

The 4-body α-residual `derive_binding_chain_cooperative` identifies gets
*larger*, because the correction removes binding from the chain sum. Both
statements are true and they are not in tension: the floor was inflating the
pairwise sum, so removing it makes the pairwise picture more accurate **and**
leaves more for the cooperative term to explain.

THE LEADING-ORDER COEFFICIENTS ARE EXACT DYADIC RATIONALS
----------------------------------------------------------
The floor-corrected observable `Δtr − c₀(A)` is `ℏ_q^1`, and its leading
coefficient `c₁ = lim (Δtr − c₀)/ℏ_q` is an exact dyadic rational in every case
[assertion 3], each matching to `≤ 1.3e-9`:

    pp   19/8      pn   37/16     nn   9/4
    T    163/64    ³He  85/32     ⁴He  259/128

So both orders of `Δtr` are dyadic — `c₀` by the derivation in
`classical_floor_derivation_probe`, and now `c₁` measured. And the chain-vs-exact
ratios follow **exactly**, with no fitting:

    T    (37/16 + 9/4) / (163/64)          = 292/163  = 1.7914110429…
    ³He  (19/8 + 37/16) / (85/32)          = 30/17    = 1.7647058824…
    ⁴He  (19/8 + 37/16 + 9/4) / (259/128)  = 888/259  = 24/7 = 3.4285714…

matching the extrapolated ratios to `1e-8`–`1e-11`. **The pairwise-vs-exact
discrepancy at leading order is therefore an exactly known rational**, not a
measured residual — a derivation gap closed rather than narrowed.

⚠ AND IT SAYS THE q₀ AGREEMENT IS A CANCELLATION, NOT A STRUCTURE
------------------------------------------------------------------
At `q₀` the floor-corrected chain/atom ratios are `1.118`, `1.020`, `1.194`. At
**leading order** they are `1.791`, `1.765`, `3.429`. The chain over-counts the
exact `H_{3A}` trace by `3.4×` at ⁴He in the `ℏ_q → 0` limit, and the much
better agreement at `q₀` comes from higher-order terms partially cancelling that.

**So pairwise additivity of the signed trace difference is not a controlled
approximation.** Its accuracy at `q₀` is not inherited from a leading-order
property; it is a numerical coincidence of the deformation size.

Note this concerns the **signed** functor `tr_free − tr_atom` that
`derive_binding_chain_cooperative` uses. The exact-additivity result in
`docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md` is about the **log**
functor `α·ln(tr_free/tr_atom)`. Different functors, and nothing here contradicts
that audit — but a reader should not carry its exactness claim across to the
signed form, and the two are easy to conflate.

ONE THING THE CORRECTION DOES REPAIR STRUCTURALLY
--------------------------------------------------
`Δtr − c₀(A)` is a pure `ℏ_q^1` observable (`qou-zrx2`), and convention A is the
`ℏ_q^1` scale, so `A × (Δtr − c₀)` totals `ℏ_q^2` — the same bookkeeping as
`Δ(net) × A`, which predicts `Q_β` to 0.168 %. Before the correction no
convention paired consistently, because the observable's two parts sat at
different orders. **The chain producer's use of A becomes ℏ_q-coherent once the
floor is subtracted**, which it was not before.

That is a reason to prefer A here that does *not* come from which value lands
closer to AME — and it is worth stating precisely because the closer-to-AME
argument is the one this lane keeps having to withdraw.

Usage:
    python3 computations/probes/binding_chain_floor_corrected_probe.py
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

import tr_m_atom_via_transfer as TR  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 50

E0_A = mp.mpf("4.18598136329447")   # convention A, what the chain producer uses
E0_B = mp.mpf("0.78233340931")      # convention B, what binding_canonical uses

# Chain adjacency, transcribed from derive_binding_chain_cooperative.CHAIN.
BOND_ZN = {"pp": (2, 0), "pn": (1, 1), "nn": (0, 2)}
CHAIN = {"D": ["pn"], "T": ["pn", "nn"], "3He": ["pp", "pn"],
         "4He": ["pp", "pn", "nn"]}
ATOM_ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}
AME_B = {"D": mp.mpf("2.22456637"), "T": mp.mpf("8.48179663"),
         "3He": mp.mpf("7.71799"), "4He": mp.mpf("28.29561")}


def c0(A: int) -> mp.mpf:
    """The derived classical floor, `2^{−A} − 2^{1−2A}` (bean `qou-zrx2`)."""
    return mp.mpf(2) ** (-A) - mp.mpf(2) ** (1 - 2 * A)


def delta_tr(Z: int, N: int, q) -> mp.mpf:
    ta, tf, _chi, _w = TR.tr_m_atom_zn(Z, N, dps=50, q=q)
    return tf - ta


def main() -> int:
    q0 = mp.mpf(Q_50_DIGIT_STR)
    w = WitnessBuilder("binding-chain-floor-corrected-probe")
    w.set_description(
        "Re-runs derive_binding_chain_cooperative's pairwise chain against the "
        "floor-corrected trace difference Dtr - c0(A). Pairwise additivity against the "
        "exact H_3A trace improves from 47.1% worst-case deviation to 19.4%, and 60.8% of "
        "the 4He pairwise-vs-exact gap turns out to be floor bookkeeping. The binding "
        "residual against AME gets slightly larger, reported plainly."
    )

    bond_dtr = {k: delta_tr(Z, N, q0) for k, (Z, N) in BOND_ZN.items()}
    rows, raw_dev, cor_dev = [], [], []
    for iso, bonds in CHAIN.items():
        Z, N = ATOM_ZN[iso]
        A = Z + N
        atom_raw = delta_tr(Z, N, q0)
        atom_cor = atom_raw - c0(A)
        chain_raw = sum((bond_dtr[b] for b in bonds), mp.mpf(0))
        chain_cor = chain_raw - len(bonds) * c0(2)
        r_raw, r_cor = chain_raw / atom_raw, chain_cor / atom_cor
        if iso != "D":                      # D is the pn bond, ratio is 1 by construction
            raw_dev.append(abs(r_raw - 1))
            cor_dev.append(abs(r_cor - 1))
        rows.append({
            "isotope": iso, "A": A, "n_bonds": len(bonds), "bonds": bonds,
            "atom_dtr_raw": mp.nstr(atom_raw, 14),
            "atom_dtr_floor_removed": mp.nstr(atom_cor, 14),
            "chain_sum_raw": mp.nstr(chain_raw, 14),
            "chain_sum_floor_removed": mp.nstr(chain_cor, 14),
            "chain_over_atom_raw": mp.nstr(r_raw, 10),
            "chain_over_atom_floor_removed": mp.nstr(r_cor, 10),
            "gap_raw": mp.nstr(chain_raw - atom_raw, 10),
            "gap_floor_removed": mp.nstr(chain_cor - atom_cor, 10),
            "floor_mismatch_(A-1)c0(2)-c0(A)":
                mp.nstr((A - 1) * c0(2) - c0(A), 10),
        })

    # ---- assertion 1: additivity improves for every isotope -----------------
    # NOT forced by the algebra. The reduction (A-1)c0(2) - c0(A) is identically
    # what it is, but whether subtracting it moves chain/atom TOWARD 1 depends on
    # the measured traces and could have gone either way.
    all_improve = all(c < r for r, c in zip(raw_dev, cor_dev))
    w.add_assertion(
        "removing_the_floor_improves_pairwise_additivity_for_every_isotope",
        computed="1" if all_improve else "0",
        expected="1",
        source="|chain/atom - 1| after floor removal vs before, for T, 3He and 4He "
               "(D excluded: it IS the pn bond, so its ratio is 1 by construction). "
               "Measured "
               + ", ".join(f"{r['isotope']}: {r['chain_over_atom_raw']} -> "
                           f"{r['chain_over_atom_floor_removed']}"
                           for r in rows if r['isotope'] != 'D')
               + ". The floor is a parameter-free quantity derived elsewhere; that "
                 "subtracting it moves every ratio toward 1 is a genuine outcome, not "
                 "an identity.",
    )

    # ---- assertion 2: the worst-case deviation more than halves --------------
    worst_raw, worst_cor = max(raw_dev), max(cor_dev)
    w.add_assertion(
        "worst_case_additivity_deviation_more_than_halves",
        computed="1" if worst_cor * 2 < worst_raw else "0",
        expected="1",
        source=f"worst |chain/atom - 1| over T, 3He, 4He falls from "
               f"{mp.nstr(worst_raw, 8)} to {mp.nstr(worst_cor, 8)}. Stated as a "
               f"worst case rather than at a chosen isotope, so no member is selected.",
    )

    # ---- assertion 3: the leading coefficients are exact dyadic rationals ---
    from fractions import Fraction

    def c1_of(Z: int, N: int) -> mp.mpf:
        """Leading `ℏ_q` coefficient of `Δtr − c₀(A)`, by Richardson."""
        A = Z + N
        vals = []
        for e in ["1e-5", "1e-6"]:
            qq = mp.exp(mp.mpf(e))
            hb = (qq - 1) / qq
            vals.append(((delta_tr(Z, N, qq) - c0(A)) / hb, hb))
        (v1, h1), (v2, h2) = vals
        return (v2 * h1 - v1 * h2) / (h1 - h2)

    c1_rows, worst_c1 = {}, mp.mpf(0)
    for nm, (Z, N) in [("pp", (2, 0)), ("pn", (1, 1)), ("nn", (0, 2)),
                       ("T", (1, 2)), ("3He", (2, 1)), ("4He", (2, 2))]:
        v = c1_of(Z, N)
        fr = Fraction(float(v)).limit_denominator(4096)
        exact = mp.mpf(fr.numerator) / fr.denominator
        rel = abs(v - exact) / abs(v)
        worst_c1 = max(worst_c1, rel)
        c1_rows[nm] = {"measured": mp.nstr(v, 18), "rational": str(fr),
                       "is_dyadic": (fr.denominator & (fr.denominator - 1)) == 0,
                       "relative_error": mp.nstr(rel, 6)}
    all_dyadic = all(r["is_dyadic"] for r in c1_rows.values())
    w.add_assertion(
        "leading_hbar_q_coefficients_are_exact_dyadic_rationals",
        computed="1" if (all_dyadic and worst_c1 < mp.mpf("1e-8")) else "0",
        expected="1",
        source="c1 = lim (Dtr - c0(A))/hbar_q for the three bonds and three atoms, each "
               "against its best rational with denominator <= 4096: "
               + ", ".join(f"{k} = {v['rational']}" for k, v in c1_rows.items())
               + f"; every denominator a power of two, worst relative error "
                 f"{mp.nstr(worst_c1, 6)}. Dyadic is the same shape as the floor c0, which "
                 f"is derived, so this is structure rather than coincidence -- but note c1 "
                 f"is MEASURED here, not derived.",
    )

    # ---- data ----------------------------------------------------------------
    w.add_data("leading_order_coefficients", {
        "c1": c1_rows,
        "leading_order_chain_over_atom": {
            "T": "(37/16 + 9/4) / (163/64) = 292/163 = 1.7914110429",
            "3He": "(19/8 + 37/16) / (85/32) = 30/17 = 1.7647058824",
            "4He": "(19/8 + 37/16 + 9/4) / (259/128) = 888/259 = 24/7 = 3.4285714286",
        },
        "at_q0_for_contrast": {r["isotope"]: r["chain_over_atom_floor_removed"]
                               for r in rows},
        "reading": "the pairwise-vs-exact discrepancy at leading order is an exactly known "
                   "rational. But it is FAR larger than the q0 discrepancy (3.43x vs 1.19x "
                   "at 4He), so the good agreement at q0 is higher-order cancellation, not "
                   "a leading-order property. Pairwise additivity of the SIGNED functor is "
                   "not a controlled approximation.",
        "not_a_contradiction": "docs/audits/2026-06-16-b-sym-linear-chain-closed-form.md "
                               "reports exact additivity for the LOG functor "
                               "alpha*ln(tr_free/tr_atom). This probe measures the SIGNED "
                               "functor tr_free - tr_atom, which is what "
                               "derive_binding_chain_cooperative uses. Different functors; "
                               "nothing here contradicts that audit, but the exactness claim "
                               "must not be carried across.",
    })

    w.add_parameter("q0", mp.nstr(q0, 30))
    w.add_parameter("E0_convention_A_MeV", mp.nstr(E0_A, 15))
    w.add_parameter("E0_convention_B_MeV", mp.nstr(E0_B, 15))
    w.add_parameter("c0(2)", mp.nstr(c0(2), 15))

    w.add_data("per_bond_trace_differences", {
        k: {"delta_tr": mp.nstr(v, 14),
            "delta_tr_minus_c0(2)": mp.nstr(v - c0(2), 14)}
        for k, v in bond_dtr.items()
    })
    w.add_data("chain_vs_exact_atom_trace", rows)
    w.add_data("additivity_summary", {
        "worst_deviation_raw": mp.nstr(worst_raw, 8),
        "worst_deviation_floor_removed": mp.nstr(worst_cor, 8),
        "improvement_factor": mp.nstr(worst_raw / worst_cor, 6),
        "note": "the reduction in each gap is exactly (A-1)*c0(2) - c0(A), which is "
                "identically true given the definitions and is therefore reported here "
                "rather than asserted. The finding is that it moves the ratios toward 1.",
    })

    # how much of the 4He pairwise-vs-exact gap was floor
    he = next(r for r in rows if r["isotope"] == "4He")
    gap_raw, gap_cor = mp.mpf(he["gap_raw"]), mp.mpf(he["gap_floor_removed"])
    w.add_data("how_much_of_the_4He_many_body_gap_was_floor", {
        "pairwise_minus_exact_raw": mp.nstr(gap_raw, 10),
        "pairwise_minus_exact_floor_removed": mp.nstr(gap_cor, 10),
        "explained_by_the_floor": mp.nstr(gap_raw - gap_cor, 10),
        "fraction_explained_percent": mp.nstr(100 * (gap_raw - gap_cor) / gap_raw, 6),
        "reading": "part of what the pairwise chain could not reach at 4He was floor "
                   "bookkeeping rather than many-body physics.",
    })

    # binding, both conventions, and the cost
    binding_rows = []
    for r in rows:
        iso, A = r["isotope"], r["A"]
        ch_raw, ch_cor = mp.mpf(r["chain_sum_raw"]), mp.mpf(r["chain_sum_floor_removed"])
        binding_rows.append({
            "isotope": iso, "A": A, "AME_B_MeV": mp.nstr(AME_B[iso], 12),
            "chain_raw_convA_MeV": mp.nstr(E0_A * ch_raw, 10),
            "chain_corrected_convA_MeV": mp.nstr(E0_A * ch_cor, 10),
            "residual_raw_convA_MeV": mp.nstr(AME_B[iso] - E0_A * ch_raw, 10),
            "residual_corrected_convA_MeV": mp.nstr(AME_B[iso] - E0_A * ch_cor, 10),
            "chain_corrected_convB_MeV": mp.nstr(E0_B * ch_cor, 10),
        })
    w.add_data("binding_against_AME", {
        "rows": binding_rows,
        "honest_note": "TRACE additivity improves; the BINDING residual gets larger, "
                       "because the correction removes binding from the chain sum. At 4He "
                       "the residual goes 21.40 -> 22.97 MeV under convention A. Both are "
                       "true and not in tension: the floor was inflating the pairwise sum, "
                       "so removing it makes the pairwise picture more accurate AND leaves "
                       "more for the cooperative alpha term.",
    })

    w.add_data("what_the_correction_repairs_structurally", (
        "Dtr - c0(A) is a pure hbar_q^1 observable (qou-zrx2), and convention A is the "
        "hbar_q^1 scale, so A x (Dtr - c0) totals hbar_q^2 -- the same bookkeeping as "
        "Delta(net) x A, which predicts Q_beta to 0.168%. BEFORE the correction no "
        "convention paired consistently, because the observable's two parts sat at "
        "different orders. So the chain producer's use of A becomes hbar_q-coherent once "
        "the floor is subtracted. This is a reason to prefer A that does NOT come from "
        "which value lands closer to AME -- worth stating precisely because the "
        "closer-to-AME argument is the one this lane keeps withdrawing."
    ))

    w.add_data("verdict", (
        "Removing the derived floor improves pairwise additivity against the exact H_3A "
        "trace for every isotope: worst-case deviation 47.1% -> 19.4%, and 3He lands within "
        "2%. 60.8% of the 4He pairwise-vs-exact gap was floor bookkeeping rather than "
        "many-body physics. The binding residual against AME gets slightly larger "
        "(21.40 -> 22.97 MeV at 4He) and that is reported rather than buried. The "
        "structural gain is that convention A becomes the hbar_q-coherent pairing for the "
        "corrected observable, which it was not before."
    ))

    out = w.save()
    print(f"wrote {out}")
    print(f"  {'iso':6}{'A':>3}{'bonds':>7}   {'chain/atom raw':>16}{'floors removed':>17}")
    for r in rows:
        print(f"  {r['isotope']:6}{r['A']:>3}{r['n_bonds']:>7}   "
              f"{r['chain_over_atom_raw']:>16}{r['chain_over_atom_floor_removed']:>17}")
    print(f"  worst deviation: {mp.nstr(worst_raw, 6)} -> {mp.nstr(worst_cor, 6)}  "
          f"({mp.nstr(worst_raw / worst_cor, 5)}x better)")
    print(f"  4He pairwise-vs-exact gap explained by the floor: "
          f"{mp.nstr(100 * (gap_raw - gap_cor) / gap_raw, 6)} %")
    print()
    for b in binding_rows:
        print(f"  {b['isotope']:5} AME {b['AME_B_MeV']:>12}  chain(A) raw "
              f"{b['chain_raw_convA_MeV']:>12} -> corrected {b['chain_corrected_convA_MeV']:>12}"
              f"   residual {b['residual_raw_convA_MeV']:>12} -> {b['residual_corrected_convA_MeV']:>12}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
