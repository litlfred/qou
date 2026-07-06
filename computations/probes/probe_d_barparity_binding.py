#!/usr/bin/env python3
"""
probe_d_barparity_binding.py — does the deuteron's 2.6e-4 bar-conjugate-law
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

## The result (verified)

- ‖a^odd‖₂ ≈ 0.163 (≈70% of ‖a‖) — LARGE, but this is the generic λ↔λ'
  asymmetry of characters at fixed q, NOT the 2.6e-4 colour effect.
- Σ_λ a^odd_λ = 0 EXACTLY (antisymmetric ⇒ telescopes). Therefore the binding
  SCALAR Σ_λ a_λ = tr_M is a PURELY BAR-EVEN functional.

Consequence: a bar-symmetric Δ_λ (uniform δ = (B_AME/m_e)/tr_M = 11.21, or any
dim/hook-based ansatz — all bar-even) satisfies the deuteron binding with ZERO
obstruction from bar-symmetry.

VERDICT: the hypothesis is FALSE as a scope-(b) claim. The 2.6e-4 is a
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
    qinv, _ = _load("chi-deuteron-h6-at-qinv-50dps.witness.json")

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
    barres = []
    for p in bound:
        cj = conjugate(p)
        chi_qi = mp.mpf(str(qinv[p]["chi_lambda"]))
        if cj in bound:
            m_ = mp.mpf(str(bound[cj]["chi_lambda"]))
            barres.append(abs(chi_qi - sign * m_) / (abs(m_) + 1))
    barconj_max = max(barres)

    # bar-parity split of a under λ ↔ λ'
    even = {p: (a[p] + a[conjugate(p)]) / 2 for p in a}
    odd = {p: (a[p] - a[conjugate(p)]) / 2 for p in a}
    odd_sum = sum(odd.values())          # = 0 identically (antisymmetric)
    even_sum = sum(even.values())        # = Σ a_λ = tr_M
    odd_frac = _l2(odd.values()) / _l2(a.values())
    uniform_delta = (B_AME / m_e) / tr_M

    print("=" * 90)
    print("DEUTERON Δ_λ BAR-PARITY OF THE BINDING CONSTRAINT — does 2.6e-4 kill any ansatz?")
    print("=" * 90)
    print(f"  bar-conjugate law max rel-resid (L={L}, sign {sign}) = {float(barconj_max):.3e}")
    print(f"  a_λ = y_λ·χ^λ(β_D);   Σ a_λ = tr_M = {mp.nstr(tr_M, 10)}")
    print(f"  ‖a‖₂            = {mp.nstr(_l2(a.values()), 8)}")
    print(f"  ‖a^even‖₂       = {mp.nstr(_l2(even.values()), 8)}")
    print(f"  ‖a^odd‖₂        = {mp.nstr(_l2(odd.values()), 8)}   "
          f"({float(odd_frac):.2%} of ‖a‖ — large but GENERIC, not the 2.6e-4)")
    print(f"  Σ a^even_λ      = {mp.nstr(even_sum, 10)}   (= tr_M ✓)")
    print(f"  Σ a^odd_λ       = {float(odd_sum):.2e}   (ZERO by antisymmetry ⇒ "
          f"binding scalar is BAR-EVEN)")
    print(f"  uniform (bar-even) Δ_λ = δ = {mp.nstr(uniform_delta, 10)}  "
          f"satisfies the binding with zero bar-symmetry obstruction")
    print()
    print("  VERDICT: the 2.6e-4 bar-conjugate breaking is a q↔q⁻¹ (decay-sector)")
    print("  property; the binding functional is bar-EVEN. No scope-(b) structural")
    print("  exclusion of bar-symmetric Δ_λ ansätze exists — refutations stay scope-(a).")

    wb = (WitnessBuilder("probe-d-barparity-binding", engine="mpmath")
          .set_description(
              "Bar-parity decomposition of the deuteron binding coefficient "
              "vector a_λ = y_λ·χ^λ(β_D) under the partition involution λ↔λ'. "
              "Tests whether the 2.6e-4 bar-conjugate-law breaking structurally "
              "(scope-b) excludes bar-symmetric Δ_λ ansätze. Finding: the "
              "bar-odd projection sums to exactly 0, so the A=2 binding scalar "
              "Σ a_λ = tr_M is a purely bar-EVEN functional; a bar-symmetric "
              "Δ_λ (uniform δ, dim/hook ansätze) satisfies binding with zero "
              "obstruction. The 2.6e-4 is a q↔q⁻¹ decay-sector effect, not a "
              "λ↔λ' binding-sector constraint. No scope-(b) exclusion exists; "
              "the six refuted ansätze stay scope-(a) numerical. Audit-only, "
              "not a closure ansatz (Δ_λ gate).")
          .set_audit_only(
              "docs/audits/2026-07-04-deuteron-dressing-is-proton-net.md")
          .add_parameter("compute_dps", DPS)
          .add_parameter("beta_D_word_length", L)
          .add_data("bar_conjugate_max_rel_resid", float(barconj_max))
          .add_data("a_l2_norm", mp.nstr(_l2(a.values()), 20))
          .add_data("a_even_l2_norm", mp.nstr(_l2(even.values()), 20))
          .add_data("a_odd_l2_norm", mp.nstr(_l2(odd.values()), 20))
          .add_data("a_odd_fraction_of_norm", float(odd_frac))
          .add_data("sum_a_even", mp.nstr(even_sum, 20))
          .add_data("sum_a_odd", mp.nstr(odd_sum, 6))
          .add_data("tr_M", mp.nstr(tr_M, 20))
          .add_data("uniform_delta_magnitude", mp.nstr(uniform_delta, 20)))
    wb.add_assertion(
        "binding_scalar_is_bar_even",
        computed=float(abs(odd_sum)), expected=0.0, tolerance=1e-9,
        source="Σ_λ a^odd_λ = 0 (bar-odd projection of the binding coefficient "
               "vector sums to zero) ⇒ the A=2 binding scalar Σ a_λ = tr_M is "
               "bar-even ⇒ bar-symmetric Δ_λ ansätze are NOT structurally excluded")
    wb.add_assertion(
        "even_projection_recovers_trM",
        computed=float(abs(even_sum - tr_M)), expected=0.0, tolerance=1e-9,
        source="Σ_λ a^even_λ = tr_M (the full binding scalar lives in the "
               "bar-even subspace)")
    wb.save()
    print("\nwitness → probe-d-barparity-binding.witness.json (audit-only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
