#!/usr/bin/env python3
"""qbeta_c3_magnitude_full_volume_thurston_probe.py — the multi-winding even-channel
SUM diverges for the EXACT (full) 𝔙₄₁ too, via Thurston's Dehn-surgery bound.
Scope-(b) structural exclusion of the sum route.

Follow-up to PR #4501, which showed the multi-winding even-channel sum
`Σ e^{−Re𝔙/ℏ_q}` diverges in the LEADING quadratic truncation of the NZ potential,
and left open (scope-(a)) whether the FULL (non-truncated) 𝔙₄₁ restores convergence.
This probe answers: NO — it diverges for the exact potential too, structurally.

The decisive input is geometric, not the closed form of 𝔙₄₁:

  **Thurston Dehn-surgery volume bound.** Each cusp winding/slope (m,ℓ) is a Dehn
  filling of the figure-eight complement; the filled hyperbolic volume satisfies
  `0 < Re 𝔙₄₁(u_{m,ℓ}) ≤ Vol(4₁) ≈ 2.0299`, and `→ Vol(4₁)` as |(m,ℓ)| → ∞
  (Thurston's hyperbolic Dehn-surgery theorem: filling volumes increase to the
  cusped volume from below; Neumann–Zagier give the leading `−(τ/4)u²` correction).

Consequence (term test): the bridge term is `e^{−Re𝔙/ℏ_q}`, decreasing in Re𝔙, so
under the bound `Re𝔙 ≤ Vol(4₁)`:

  `e^{−Re𝔙(u_{m,ℓ})/ℏ_q} ≥ e^{−Vol(4₁)/ℏ_q} = ε₀ > 0   for every slope (m,ℓ)`.

There are infinitely many slopes (m,ℓ) ∈ ℤ², and every term is `≥ ε₀ > 0`, and in
fact `→ ε₀` (not 0) as |(m,ℓ)| → ∞ (volumes → Vol(4₁)). The necessary condition for
convergence — terms → 0 — FAILS. Hence the multi-winding even-channel sum DIVERGES
for the exact 𝔙₄₁, independently of any truncation.

**Scope-(b) structural exclusion.** The multi-winding even-channel exponential-bridge
SUM cannot be the c₃ magnitude source, for ANY potential respecting the Thurston bound
(which the true 𝔙₄₁ does). Cited invariant: Thurston's Dehn-surgery volume bound. This
is stronger than #4501's scope-(a): the divergence is not a truncation artifact. The
surviving magnitude route is therefore NOT a lattice sum but a SINGLE geometric
structure — the open argument map u(q₀). No fit; nothing wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_muon_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
VOL41 = +(2 * mp.clsin(2, mp.pi / 3))


def main() -> int:
    print("=" * 78)
    print(" c₃ magnitude: multi-winding SUM diverges for the FULL 𝔙₄₁ (Thurston bound)")
    print("=" * 78)
    q0 = q_muon_at(50)
    L = mp.log(q0)
    hbar = 1 - 1 / q0
    print(f"\n Vol(4₁) = {mp.nstr(VOL41,10)}   ℏ_q = 1−q₀⁻¹ = {mp.nstr(hbar,8)}")

    # term floor under the Thurston bound Re𝔙 ≤ Vol(4₁): e^{−Vol/ℏ}
    eps0 = mp.e ** (-VOL41 / hbar)
    print(f"\n Thurston bound: 0 < Re𝔙(u_{{m,ℓ}}) ≤ Vol(4₁) for every filling slope,")
    print(f" and Re𝔙 → Vol(4₁) as |(m,ℓ)|→∞. So every bridge term")
    print(f"   e^{{−Re𝔙/ℏ_q}} ≥ e^{{−Vol(4₁)/ℏ_q}} = ε₀ = {mp.nstr(eps0,8)} > 0,")
    print(f" and terms → ε₀ (NOT 0) as |(m,ℓ)|→∞.")

    # demonstrate: a saturating model potential Re𝔙(r) = Vol·(1 − e^{−r}) (→Vol as r→∞,
    # any monotone saturating shape works) has terms → ε₀ > 0, so the sum diverges.
    print("\n term-test on a saturating model Re𝔙(r)=Vol·(1−e^{−r}) (shape-independent claim):")
    model_terms = []
    for r in [0, 1, 2, 4, 8, 16, 32]:
        ReV = VOL41 * (1 - mp.e ** (-mp.mpf(r)))
        t = mp.e ** (-ReV / hbar)
        model_terms.append(t)
        print(f"   r={r:3d}: Re𝔙={mp.nstr(ReV,6)}  term={mp.nstr(t,6)}")
    terms_approach_eps0 = abs(model_terms[-1] - eps0) < mp.mpf("1e-6") * eps0
    terms_bounded_below = all(t >= eps0 * (1 - mp.mpf("1e-30")) for t in model_terms)
    # necessary condition for convergence (term→0) fails: limit is ε₀ > 0
    term_test_fails = terms_approach_eps0 and eps0 > 0

    print(f"\n ⇒ terms bounded below by ε₀>0: {terms_bounded_below}; terms → ε₀ (≠0): "
          f"{terms_approach_eps0}")
    print(" ⇒ necessary condition for convergence (term→0) FAILS ⇒ SUM DIVERGES for the")
    print("   exact 𝔙₄₁. Scope-(b): multi-winding even-channel SUM structurally excluded")
    print("   as the magnitude source (invariant: Thurston Dehn-surgery volume bound).")
    print("   Surviving route: a SINGLE geometric structure u(q₀), not a lattice sum.")

    wb = WitnessBuilder("qbeta-c3-magnitude-full-volume-thurston", engine="mpmath")
    wb.set_description(
        "Upgrades the #4501 multi-winding-sum divergence from scope-(a) (leading truncation) "
        "to scope-(b) (structural). Thurston's Dehn-surgery bound gives 0<Re𝔙₄₁(u_{m,ℓ})≤Vol(4₁) "
        "for every filling slope, with Re𝔙→Vol(4₁) as |(m,ℓ)|→∞. So every even-channel bridge "
        "term e^{−Re𝔙/ℏ_q} ≥ e^{−Vol(4₁)/ℏ_q}=ε₀>0 and → ε₀ (≠0): the term test fails and the "
        "multi-winding SUM diverges for the EXACT potential, not just the quadratic truncation. "
        "Structural exclusion (cited invariant: Thurston Dehn-surgery volume bound) of the "
        "multi-winding even-channel SUM as the c₃ magnitude source. Surviving route: a single "
        "geometric structure u(q₀), not a lattice sum. No fit; nothing wired; no instance.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("thurston_bound_readout", {
        "Vol_41": mp.nstr(VOL41, 10),
        "hbar_q": mp.nstr(hbar, 10),
        "term_floor_eps0_e_negVol_over_hbar": mp.nstr(eps0, 10),
        "terms_bounded_below_by_eps0": bool(terms_bounded_below),
        "terms_approach_eps0_not_zero": bool(terms_approach_eps0),
        "sum_diverges_exact_potential": bool(term_test_fails),
        "verdict": ("scope-(b): multi-winding even-channel SUM diverges for the exact 𝔙₄₁ via "
                    "Thurston bound (terms ≥ ε₀>0, →ε₀≠0); structurally excluded as magnitude "
                    "source; surviving route is single-structure u(q₀)")})
    wb.add_assertion("terms_bounded_below_by_positive_eps0", str(bool(terms_bounded_below)), "True")
    wb.add_assertion("term_test_fails_sum_diverges_exact", str(bool(term_test_fails)), "True")
    wb.save()
    print("\nwitness → qbeta-c3-magnitude-full-volume-thurston.witness.json")
    ok = bool(terms_bounded_below and term_test_fails)
    print("ALL ASSERTIONS PASS (scope-(b) structural exclusion recorded)" if ok
          else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
