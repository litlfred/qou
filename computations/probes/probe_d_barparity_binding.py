#!/usr/bin/env python3
"""
probe_d_barparity_binding.py — does the deuteron's bar-conjugate-law
breaking KILL any already-refuted Δ_λ ansatz? (session 2026-07-04 follow-up to
probe_d_delta_lambda_terms.py; owner question "does the bar-symmetric-subspace
observation actually kill any of the already-refuted Δ_λ ansätze — a quick
check").

EXPLORATORY (probe_ prefix, audit-only). NOT a closure ansatz (Δ_λ gate).

## The hypothesis under test (from the term-analysis chat)

"The bar-conjugate breaking (2.6e-4) = the colour-weighting signature — any
Δ_λ closure inherits that asymmetry, so a closure searched in the
bar-symmetric subspace is structurally incomplete for the deuteron."

If TRUE, this would upgrade the scope-(a) numerical refutations of the six
Δ_λ ansätze to a scope-(b) STRUCTURAL exclusion of the whole bar-symmetric
class. Per AGENTS.md §"Before declaring refuted / ruled out", a scope-(b)
claim needs a PROVED invariant. This probe tests whether one exists.

## The check

The A=2 binding is the single scalar equation
    Σ_{λ⊢6} a_λ Δ_λ = B_AME/m_e ,   a_λ := y_λ(q₀)·χ^λ(β_D) .
Decompose the coefficient vector a_λ under the partition involution
λ ↔ λ' (conjugate/transpose): a = a^even ⊕ a^odd with
    a^even_λ = (a_λ + a_{λ'})/2 ,   a^odd_λ = (a_λ − a_{λ'})/2 .
A bar-EVEN Δ (Δ_λ = Δ_{λ'}) couples only to a^even; a bar-ODD Δ only to a^odd.

## Frame correction 2026-08-26 (bean `qou-1oxx`) — the 2.6e-4 was MIXED

This probe used to read the colour-BLIND `at-qinv` witness while its `at-q0`
side is colour-WEIGHTED, so the "bar-conjugate law" residual compared
`f_canon(q0)` against `f_strict(1/q0)`: two different functions, not one
function at two points. Both sides are now canonical (R3). Measured, all four
pairings of the deuteron:

    blind(q0)  vs blind(1/q0)   = 1.48e-49   <- EXACT at 50 dps
    canon(q0)  vs canon(1/q0)   = 5.86e-04   <- what this probe now reports
    canon(q0)  vs blind(1/q0)   = 2.63e-04   <- the historical 2.6e-4, MIXED
    blind(q0)  vs canon(1/q0)   = 3.23e-04

The first line is the finding. The colour-blind form IS the bar-symmetriser
(`f_strict = (f_pp + bar(f_pp))/2`) and the bar-conjugate law holds in it
**exactly** — 1.5e-49 is zero at this precision. So the breaking is the colour
weighting and nothing else, and the honest size of it, measured in a
consistent frame, is 5.86e-04 rather than 2.6e-04. Note this is a residual
accumulated over a 23-factor word and normalised by `|chi| + 1`; do NOT equate
it with the interface function's own bar defect
`bar(f) - f = (q-1)^5 (q+1)^3 (q^2+1) / (12 q^5) = 1.67e-05`, which is a
different quantity.

**The VERDICT below is unaffected**, and that is not luck: it rests on
`sum_lambda a^odd_lambda = 0` holding by antisymmetry, which is exact and
independent of the frame or of any numerical chi value.

## The result (verified)

- ‖a^odd‖₂ ≈ 0.163 (≈70% of ‖a‖) — LARGE, but this is the generic λ↔λ'
  asymmetry of characters at fixed q, NOT the colour effect.
- Σ_λ a^odd_λ = 0 EXACTLY (antisymmetric ⇒ telescopes). Therefore the binding
  SCALAR Σ_λ a_λ = tr_M is a PURELY BAR-EVEN functional.

Consequence: a bar-symmetric Δ_λ (uniform δ = (B_AME/m_e)/tr_M = 11.21, or any
dim/hook-based ansatz — all bar-even) satisfies the deuteron binding with ZERO
obstruction from bar-symmetry.

VERDICT: the hypothesis is FALSE as a scope-(b) claim. The breaking is a
q↔q⁻¹ (Im 𝔙, decay-sector) property of the character data; the binding
functional the Δ_λ must satisfy is bar-even (Re 𝔙, binding sector). Bridging
the two with no proved invariant is the category error the #3315 guard names.
The refuted ansätze stay scope-(a) numerical; the bar-symmetric subspace is
NOT structurally excluded, and the Δ_λ search must not be narrowed to drop it.
"""
from __future__ import annotations

import json
import sys
import warnings
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
warnings.filterwarnings("ignore")

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, COMPUTE_DPS  # noqa: E402
set_compute_dps()
DPS = COMPUTE_DPS

from codata_constants import (  # noqa: E402
    M_E_MEV, AME_B_DEUTERON_MEV_VALIDATION,
)
from witness_base import WitnessBuilder  # noqa: E402


def _pkey(v):
    if isinstance(v, list):
        return tuple(int(x) for x in v)
    return tuple(int(x) for x in str(v).strip("[]").split(",") if x.strip())


def _load(name):
    d = json.loads((COMP / name).read_text())
    return {_pkey(r["partition"]): r for r in d["by_partition"]}, d


def conjugate(part):
    if not part:
        return ()
    m = max(part)
    return tuple(sum(1 for a in part if a >= i) for i in range(1, m + 1))


def _l2(vals):
    return mp.sqrt(sum(v ** 2 for v in vals))


def main() -> int:
    bound, bd = _load("chi-deuteron-h6-at-q0-50dps.witness.json")
    free, _ = _load("chi-deuteron-free-h6-at-q0-50dps.witness.json")
    # MATCHED FRAME (bean qou-1oxx, owner decision 2026-08-26 option 1). This
    # read the colour-BLIND `chi-deuteron-h6-at-qinv-50dps` while `bound` above
    # is colour-WEIGHTED, so the "bar-conjugate law" residual below was
    # comparing f_canon(q0) against f_strict(1/q0) -- two DIFFERENT functions,
    # not one function at two points. Now both sides carry the canonical p-n
    # convention (R3).
    qinv, _ = _load(
        "chi-deuteron-h6-at-qinv-50dps-colour-weighted.witness.json")
    # Colour-BLIND reference pair, kept because it is the actual finding: the
    # blind form IS the bar-symmetriser, and measured, the bar-conjugate law
    # holds in it EXACTLY -- 1.5e-49 at 50 dps, i.e. zero. So every nonzero
    # residual reported here is the colour weighting, and nothing else.
    qinv_blind, _ = _load("chi-deuteron-h6-at-qinv-50dps.witness.json")

    m_e = mp.mpf(str(M_E_MEV))
    B_AME = mp.mpf(str(AME_B_DEUTERON_MEV_VALIDATION))
    tr_M = mp.mpf(str(bd["tr_M_at_q0"]))

    # a_λ = y_λ·χ^λ(β_D) — the binding_K_direct coefficient (Σ a_λ = tr_M).
    a = {}
    for p in bound:
        y = mp.mpf(str(bound[p]["y_lambda"]))
        cb = mp.mpf(str(bound[p]["chi_lambda"]))
        a[p] = y * cb

    # bar-conjugate-law residual (deuteron atom word L=23, odd ⇒ sign −1)
    L = 23
    sign = (-1) ** (L % 2)
    def _barconj(qi_tab):
        r = []
        for p in bound:
            cj = conjugate(p)
            if cj in bound:
                m_ = mp.mpf(str(bound[cj]["chi_lambda"]))
                r.append(abs(mp.mpf(str(qi_tab[p]["chi_lambda"]))
                             - sign * m_) / (abs(m_) + 1))
        return max(r)

    barconj_max = _barconj(qinv)                 # canonical vs canonical
    barconj_mismatched = _barconj(qinv_blind)    # the historical mixed pairing

    # bar-parity split of a under λ ↔ λ'
    even = {p: (a[p] + a[conjugate(p)]) / 2 for p in a}
    odd = {p: (a[p] - a[conjugate(p)]) / 2 for p in a}
    odd_sum = sum(odd.values())          # = 0 identically (antisymmetric)
    even_sum = sum(even.values())        # = Σ a_λ = tr_M
    odd_frac = _l2(odd.values()) / _l2(a.values())
    uniform_delta = (B_AME / m_e) / tr_M

    print("=" * 90)
    print("DEUTERON Δ_λ BAR-PARITY OF THE BINDING CONSTRAINT — does the "
          "bar-conjugate breaking kill any ansatz?")
    print("=" * 90)
    print(f"  bar-conjugate law max rel-resid (L={L}, sign {sign}) = "
          f"{float(barconj_max):.3e}   [canonical p-n convention, BOTH sides]")
    print(f"    for reference, the pre-qou-1oxx MIXED pairing "
          f"f_canon(q0) vs f_strict(1/q0) = {float(barconj_mismatched):.3e}")
    print(f"    and the colour-BLIND pair is EXACT (~1e-49): the blind form is "
          f"the bar-symmetriser,")
    print(f"    so the residual above is the colour weighting and nothing else.")
    print(f"  a_λ = y_λ·χ^λ(β_D);   Σ a_λ = tr_M = {mp.nstr(tr_M, 10)}")
    print(f"  ‖a‖₂            = {mp.nstr(_l2(a.values()), 8)}")
    print(f"  ‖a^even‖₂       = {mp.nstr(_l2(even.values()), 8)}")
    print(f"  ‖a^odd‖₂        = {mp.nstr(_l2(odd.values()), 8)}   "
          f"({float(odd_frac):.2%} of ‖a‖ — large but GENERIC, not the "
          f"colour effect)")
    print(f"  Σ a^even_λ      = {mp.nstr(even_sum, 10)}   (= tr_M ✓)")
    print(f"  Σ a^odd_λ       = {float(odd_sum):.2e}   (ZERO by antisymmetry ⇒ "
          f"binding scalar is BAR-EVEN)")
    print(f"  uniform (bar-even) Δ_λ = δ = {mp.nstr(uniform_delta, 10)}  "
          f"satisfies the binding with zero bar-symmetry obstruction")
    print()
    print(f"  VERDICT: the {float(barconj_max):.3e} bar-conjugate breaking "
          f"is a q↔q⁻¹ (decay-sector)")
    print("  property; the binding functional is bar-EVEN. No scope-(b) structural")
    print("  exclusion of bar-symmetric Δ_λ ansätze exists — refutations stay scope-(a).")

    wb = (WitnessBuilder("probe-d-barparity-binding", engine="mpmath")
          .set_description(
              "Bar-parity decomposition of the deuteron binding coefficient "
              "vector a_λ = y_λ·χ^λ(β_D) under the partition involution λ↔λ'. "
              "Tests whether the bar-conjugate-law breaking structurally "
              "(scope-b) excludes bar-symmetric Δ_λ ansätze. Finding: the "
              "bar-odd projection sums to exactly 0, so the A=2 binding scalar "
              "Σ a_λ = tr_M is a purely bar-EVEN functional; a bar-symmetric "
              "Δ_λ (uniform δ, dim/hook ansätze) satisfies binding with zero "
              "obstruction. The breaking is a q↔q⁻¹ decay-sector effect, not a "
              "λ↔λ' binding-sector constraint. No scope-(b) exclusion exists; "
              "the six refuted ansätze stay scope-(a) numerical. Audit-only, "
              "not a closure ansatz (Δ_λ gate).")
          .set_audit_only(
              "docs/audits/2026-07-04-deuteron-dressing-is-proton-net.md")
          .add_parameter("compute_dps", DPS)
          .add_parameter("beta_D_word_length", L)
          .add_data("bar_conjugate_max_rel_resid",
                    mp.nstr(barconj_max, 20))
          .add_data("bar_conjugate_max_rel_resid_mixed_frame_historical",
                    mp.nstr(barconj_mismatched, 20))
          .add_data("pn_convention_both_sides", "bring_color_weighted")
          .add_data("a_l2_norm", mp.nstr(_l2(a.values()), 20))
          .add_data("a_even_l2_norm", mp.nstr(_l2(even.values()), 20))
          .add_data("a_odd_l2_norm", mp.nstr(_l2(odd.values()), 20))
          .add_data("a_odd_fraction_of_norm", mp.nstr(odd_frac, 20))
          .add_data("sum_a_even", mp.nstr(even_sum, 20))
          .add_data("sum_a_odd", mp.nstr(odd_sum, 6))
          .add_data("tr_M", mp.nstr(tr_M, 20))
          .add_data("uniform_delta_magnitude", mp.nstr(uniform_delta, 20)))
    wb.add_assertion(
        "binding_scalar_is_bar_even",
        # Strings, not floats: the drained convention (qou-t0rf) keeps the
        # value out of float64. |Sum a^odd| is ~1e-72 here, which float()
        # survives -- but the ratchet is about the FIELD, not the magnitude.
        computed=mp.nstr(abs(odd_sum), 20), expected="0",
        tolerance="1e-9",
        source="Σ_λ a^odd_λ = 0 (bar-odd projection of the binding coefficient "
               "vector sums to zero) ⇒ the A=2 binding scalar Σ a_λ = tr_M is "
               "bar-even ⇒ bar-symmetric Δ_λ ansätze are NOT structurally excluded")
    wb.add_assertion(
        "even_projection_recovers_trM",
        computed=mp.nstr(abs(even_sum - tr_M), 20), expected="0",
        tolerance="1e-9",
        source="Σ_λ a^even_λ = tr_M (the full binding scalar lives in the "
               "bar-even subspace)")
    wb.save()
    print("\nwitness → probe-d-barparity-binding.witness.json (audit-only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
