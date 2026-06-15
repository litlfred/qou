#!/usr/bin/env python3
"""qbeta_klr_composite3_preflight_run.py
=========================================

**KLR tranche 2 — Composite-3 (Type-B folded crystal) preflight RUN.**
Companion to the Composite-4 + Composite-1 preflights. Same template, applied
to cont. 9 [Option D / Composite 3 (Type-B folded crystal sum)](../../../docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md#composite-3-type-b-folded-crystal-sum)
(12-17 session infra build, highest cost; CLAUDE.md §7b authoring guidance).

## What Composite 3 is

    F(u) = Σ_{T ∈ B_{Type-B fold}(λ)} q^{c(T)} · u^{|T|}

where `B_{Type-B fold}(λ)` is the σ-fixed subset of the sl_n Kashiwara crystal
under the Dynkin automorphism σ (CLAUDE.md §7b: "Type B folding for chirality /
CPT"; σ-fixed crystals are bar-involution invariant by construction).
`c(T)` is the q-content statistic (a sum of positive integers in the standard
crystal model from
[`qbeta_chain4_demazure_fund_weights.py`](../qbeta/qbeta_chain4_demazure_fund_weights.py):
`q^{c(T)} = q^{Σ(a_k − 1)}` for T a subset).

So `[u^k] F = Σ_{T: |T|=k, σ-fixed} q^{c(T)}`.

## Why this preflight settles in one session

Same structural argument as Composite 1 (PR #1914 RUN):

1. **`q^{c(T)} > 0` at q > 0** for any c(T) ∈ ℤ (positive q-powers).
2. **Σ of positives is POSITIVE** at q > 0.
3. **Target `c_2 = -1 < 0`** (proved, PR #1887).
4. **Sign mismatch** ⇒ refutation at u^2, **independent of which λ or which σ
   you pick** — folded or unfolded, the positivity of the q-monomial basis sum
   is fundamental.

The CLAUDE.md §7b "bar-involution invariant" property of folded crystals
*means* the basis sum is bar-invariant; it does NOT mean the sum is negative.
Bar-invariance and sign-positivity are orthogonal properties.

## Concrete verification: sl_4 → C_2 folding, ω_2, |T|=2 σ-fixed elements

For sl_4 at ω_2 (V(ω_2) = Λ² ℂ⁴, basis = 2-subsets), the σ = (s_1 ↔ s_3)
Dynkin automorphism acts on 2-subsets by 1↔4, 2↔3. σ-fixed 2-subsets at any
length:

- highest weight {1,2}: |T|=0, σ-image {3,4} — NOT fixed
- f̃_2 {1,2} = {1,3}: |T|=1, σ-image {2,4} — NOT fixed
- f̃_3 f̃_2 {1,2} = {1,4}: |T|=2, σ-image {1,4} — **FIXED**, c={1,4}=0+3=3
- f̃_1 f̃_2 {1,2} = {2,3}: |T|=2, σ-image {2,3} — **FIXED**, c={2,3}=1+2=3
- f̃_3 f̃_1 f̃_2 {1,2} = {2,4}: |T|=3, σ-image {1,3} — NOT fixed
- f̃_2 f̃_3 f̃_1 f̃_2 {1,2} = {3,4}: |T|=4 (lowest weight), σ-image {1,2} — NOT fixed

So at |T|=2 σ-fixed: A_2 = q^3 + q^3 = 2q^3 (positive at q > 0).

## References
- Composite-3 ansatz: [`2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`](../../../docs/scope/2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md) §Composite 3.
- Sibling preflights (Composite 4 magnitude, Composite 1 standard sign): same scope docs in `docs/scope/2026-06-06-qbeta-klr-composite*-preflight-run-results.md`.
- §7b authoring guidance: CLAUDE.md (Type-B folding).
- Proved `c_2 = -1`: PR #1887, ledger cont. 14.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

from mpmath import mp, mpf, sign  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def sigma_fixed_two_subsets_sl4_omega2_at_length_2() -> list[tuple[int, ...]]:
    """σ-fixed 2-subsets of {1,2,3,4} at crystal length 2 under σ = (1↔4, 2↔3).
    From the docstring analysis: {1,4} and {2,3}."""
    return [(1, 4), (2, 3)]


def q_content(subset: tuple[int, ...], q: mpf) -> mpf:
    """q^{Σ(a_k - 1)} — the Joseph/Andersen Demazure-content formula."""
    return q ** sum(a - 1 for a in subset)


def u2_coefficient_composite3(q: mpf) -> mpf:
    """[u^2] F for Composite 3 at sl_4 / ω_2 / Type-C_2 folding:
    Σ_{T: |T|=2 σ-fixed} q^{c(T)} = q^3 + q^3 = 2q^3."""
    return sum(
        (q_content(S, q) for S in sigma_fixed_two_subsets_sl4_omega2_at_length_2()),
        mpf(0),
    )


def main() -> int:
    set_compute_dps()

    c2_target = mpf(-1)

    print("=" * 88)
    print(" KLR Composite-3 preflight RUN — Type-B folded crystal sign analysis")
    print("=" * 88)
    print(f"  Ansatz: F(u) = Σ_{{T ∈ σ-fixed crystal}} q^{{c(T)}}·u^{{|T|}}")
    print(f"  sl_4 → C_2 fold, ω_2; σ-fixed |T|=2 elements: {{1,4}} and {{2,3}}")
    print(f"  [u²]F = q^3 + q^3 = 2q^3")
    print()
    print(f"  {'anchor':<8}{'q':>12}{'q^3':>14}{'[u²]F=2q^3':>16}{'sign':>8}{'vs c_2=-1':>14}")
    print(f"  {'-'*8}{'-'*12}{'-'*14}{'-'*16}{'-'*8}{'-'*14}")

    rows = []
    for name, qf in (("proton", q_at), ("muon", q_muon_at)):
        q = qf(mp.dps)
        u2 = u2_coefficient_composite3(q)
        s = sign(u2)
        mismatch = (s != sign(c2_target))
        rows.append({
            "anchor": name,
            "q": fmt(q),
            "q_cubed": fmt(q ** 3),
            "u2_coefficient_2q_cubed": fmt(u2),
            "sign": int(s),
            "c2_target": fmt(c2_target),
            "sign_mismatches_c2": bool(mismatch),
        })
        sign_str = "POS" if int(s) > 0 else "NEG"
        match_str = "MISMATCH" if mismatch else "match"
        print(f"  {name:<8}{float(q):>12.7f}{float(q**3):>14.7f}"
              f"{float(u2):>16.7f}{sign_str:>8}{match_str:>14}")

    print()
    print("=" * 88)
    print(" VERDICT")
    print("=" * 88)
    sign_refuted = all(r["sign_mismatches_c2"] for r in rows)
    if sign_refuted:
        print("  TYPE-B FOLDED CRYSTAL × u^|T| REFUTED at u² by SIGN.")
        print(f"    [u²]F = q^3 + q^3 = 2q^3 > 0 at q > 0 (positivity of q-power sums),")
        print(f"    target c_2 = -1 < 0.")
        print(f"  GENERAL: the σ-fixed crystal basis at any length k has POSITIVE")
        print(f"    q-monomial content sum; combined with u^|T| (no q-Pochhammer")
        print(f"    sign-flip factor), [u^k]F > 0 at ALL u^k rungs. CANNOT source")
        print(f"    NEGATIVE c_k for any k (c_2, c_3, c_4 all negative at q₀).")
        print(f"  cont. 9 Option D (12-17 session Composite-3 build) NOT AUTHORISED.")
        print(f"  CLAUDE.md §7b bar-invariance is preserved by the folding but does NOT")
        print(f"    rescue: bar-invariance and sign-negativity are orthogonal.")
        verdict = "TYPEB_FOLDED_CRYSTAL_SIGN_REFUTED_AT_U2"
    else:
        verdict = "SIGN_PASS_NEEDS_MAGNITUDE_CHECK"

    wb = WitnessBuilder("qbeta-klr-composite3-preflight-run", engine="mpmath")
    wb.set_description(
        "KLR tranche 2 — Composite-3 (Type-B folded crystal) preflight RUN, "
        "third in the cont. 9 menu preflight series after Composite-4 (magnitude "
        "refutation) and Composite-1 standard (sign refutation). Tests [u²]F for "
        "the cont. 9 Option D ansatz F(u) = Σ_T q^{c(T)}·u^{|T|} at sl_4 → C_2 "
        "folding, ω_2. σ-fixed 2-subsets at |T|=2 are {1,4} and {2,3} (the only "
        "fixed pairs under σ = 1↔4, 2↔3). [u²]F = q^3 + q^3 = 2q^3 > 0 at q > 0, "
        "sign-incompatible with c_2 = -1 < 0. cont. 9 Option D (12-17 sessions) "
        "NOT authorised. CLAUDE.md §7b bar-invariance of folded crystals does NOT "
        "rescue (bar-invariance and sign-negativity are orthogonal)."
    )
    wb.set_content_block("conj:qbeta-precision-ladder")
    wb.add_data("anchors", rows)
    wb.add_data("verdict", verdict)
    wb.add_data("interpretation", (
        "Same structural refutation pattern as Composite 1 standard: positivity "
        "of q-monomial sums at q > 0 is convention-robust. Folded crystals "
        "(CLAUDE.md §7b) inherit positivity from the unfolded sl_n crystal — the "
        "σ-fixed subset is a SUBSET of positive basis elements, so its q-weight "
        "sum is bounded above by the full sum but still positive. The Composite-3 "
        "ansatz has NO q-Pochhammer factor to flip the sign at u², so the "
        "refutation is even cleaner than Composite 1 (which had (q;q)_2 > 0 at "
        "q > 1 happening to compound the positivity). Combined three-preflight "
        "outcome (B + C + D refuted at u^2; A is the only surviving cont. 9 menu "
        "option not requiring a separate Demazure-Lusztig preflight scope): "
        "~22-30 sessions of Lean + pyhecke infra build avoided. CAL-3-anchored "
        "permanent acceptance is now backed by 3 corpus closures + 3 preflight "
        "refutations."
    ))
    wb.add_assertion(
        "typeb_folded_crystal_sign_refuted_at_u2_both_anchors",
        computed=1.0 if sign_refuted else 0.0,
        expected=1.0,
    )
    wb.add_assertion(
        "u2_coefficient_2q_cubed_positive_both_anchors",
        computed=1.0 if all(r["sign"] > 0 for r in rows) else 0.0,
        expected=1.0,
    )

    wb.save()
    print()
    print(f"  Witness: qbeta-klr-composite3-preflight-run.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
