#!/usr/bin/env python3
"""mu4_vs_nuclear_4n_force_bound_probe.py — is the μ₄ target a physical 4-body
quantity at all? Measured against the nuclear-physics literature: NO, by ~34×.

WHY THIS EXISTS. GAP-8 measured the block-trace operator's 4-body moment at
A=4/H₁₂ and found the hierarchy FLAT (|μ₄/μ₃| = 1.02) against a target of 9.75,
and the follow-up bean asked "what supplies ~10× per-order growth?". This probe
tests the prior question — whether that growth is physical at all — and finds it
is not. The question was wrong, not just unanswered.

THE MAGNITUDE ARGUMENT (the decisive one). The moments are in units of B(D):

    μ₄ = −4.591  ×  B(D) = 2.224566 MeV  =  −10.21 MeV
    B(⁴He) = 28.296 MeV   ⇒   |μ₄| is 36% of the ⁴He binding energy.

The nuclear-physics literature bounds the GENUINE four-nucleon content of ⁴He
far below that:

  * Jurgenson–Navrátil–Furnstahl (PRL 103, 082501 / arXiv:0905.1873) measure the
    SRG-induced four-body force at λ = 2 fm⁻¹ and find it contributes "about
    50 keV net" to ⁴He — 0.18% of the binding.
  * The same paper quotes the estimate that the long-ranged part of the N³LO
    four-nucleon force contributes "of order a few hundred keV" — ~1.1%.

So the QOU μ₄ exceeds the N³LO 4N estimate by ~34× and the SRG-induced 4N by
~204×. A quantity 36% of the total binding is not a four-body force.

WHERE IT ACTUALLY COMES FROM. With the corpus's own (unbalanced) q-integer
`[n]_q = 1 + q + … + q^{n-1}`, the ladders separate cleanly:

    s₄ (ρ_strong's own 4-body coeff)  = +3.7804  =  +8.41 MeV
    g₄ (ρ_grad's  own 4-body coeff)   = +8.3706  = +18.62 MeV
    μ₄ = s₄ − g₄                      = −4.5902  = −10.21 MeV

The large NEGATIVE μ₄ is the reference `ρ_grad = [A]_q!/[2]_q!` OVER-SUBTRACTING,
not 4-body physics. And note s₄ = +8.41 MeV is *itself* 30% of B(⁴He) — also far
too large for a 4N force. So the inflation is not specific to ρ_grad: it is in
the C(A,k) simplex basis, which has no saturation mechanism and therefore
attributes all departure from pairwise additivity to high-body coefficients.

WHY THAT MATTERS FOR THE PROGRAMME. Nuclear binding is not pairwise-additive
(saturation), and pionless EFT explains the empirical Tjon correlation between
B(³H) and B(⁴He) by the ABSENCE of a four-nucleon force at leading order —
Platter–Hammer–Meißner (arXiv:nucl-th/0409040) state it exactly: "In order to
renormalize the four-nucleon system, it is sufficient to include a SU(4)-
symmetric one-parameter three-nucleon interaction … The absence of a
four-nucleon force at this order explains the empirically observed correlation."
B(⁴He) is fixed by B(³H) plus one three-body parameter; there is no independent
four-body scale for μ₄ to be measuring.

CONSEQUENCE — a scope-(a) finding about the TARGET, not the operator. This does
NOT show ρ_grad is wrong, and it does NOT show the block-trace operator is right.
It shows that matching μ₄ = −4.591 is not the same thing as reproducing 4-body
physics, so GAP-8's "flat hierarchy" is not by itself evidence against the
operator, and the follow-up question "what supplies ~10× growth?" is chasing a
basis artifact. The honest reformulation is to test the operator against the
Tjon correlation (B(³H) ↔ B(⁴He)), which is convention-free and is the field's
own robust observable for exactly this 3-body/4-body question.

Corpus-grep before declaring: `Tjon`, `four-nucleon force`, `4N force` return
ZERO hits across content/, docs/ and computations/ — this connection is new to
the corpus. `C(A,k) basis` appears once (the κ ledger) with no critique attached.

Papers on disc under library/ (owner upload 41930f2a): 0409040v2, 0610105v2,
0811.1338v1, 0905.1873v2, plus Klein's 2018 Bonn thesis (50067518). The original
Tjon reference (PRC 20, 340, 1979) is paywalled and pre-arXiv; it is NOT needed —
it is the empirical observation, and Platter–Hammer–Meißner both states and
explains it.

No Δ_λ, no μ fitted, nothing wired, no target adopted or rejected in compute.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE.parent), str(HERE.parent / "substrate")]

import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 25

B_D = mp.mpf("2.224566")       # deuteron binding, MeV (AME2020)
B_4HE = mp.mpf("28.295662")    # 4He binding, MeV (AME2020)
MU3 = mp.mpf("0.4707689")      # corpus residual-simplex 3-body coeff (B(D) units)
MU4 = mp.mpf("-4.591048")      # corpus residual-simplex 4-body coeff (B(D) units)
S4 = mp.mpf("3.7804")          # rho_strong's own 4-body simplex coeff
G4 = mp.mpf("8.3706")          # rho_grad's  own 4-body simplex coeff

SRG_4N_MEV = mp.mpf("0.050")   # Jurgenson+ arXiv:0905.1873: "about 50 keV net"
N3LO_4N_MEV = mp.mpf("0.300")  # same paper: "of order a few hundred keV"


def main() -> int:
    print("=" * 78)
    print(" Is the μ₄ target a physical 4-body quantity? (vs the nuclear literature)")
    print("=" * 78)

    mu4_mev = MU4 * B_D
    frac = abs(mu4_mev) / B_4HE
    print(f"\n [1] the target in physical units")
    print(f"     μ₄ = {float(MU4):+.4f} × B(D) = {float(B_D):.6f} MeV  "
          f"= {float(mu4_mev):+.3f} MeV")
    print(f"     B(⁴He) = {float(B_4HE):.3f} MeV")
    print(f"     ⇒ |μ₄| is {float(100 * frac):.1f}% of the ⁴He binding energy")

    r_n3lo = abs(mu4_mev) / N3LO_4N_MEV
    r_srg = abs(mu4_mev) / SRG_4N_MEV
    print(f"\n [2] literature bounds on the GENUINE 4N content of ⁴He")
    print(f"     SRG-induced 4N, λ=2 fm⁻¹ (arXiv:0905.1873): ~{float(SRG_4N_MEV):.3f} MeV"
          f"  = {float(100 * SRG_4N_MEV / B_4HE):.2f}%")
    print(f"     N³LO long-range 4N (same paper's estimate): ~{float(N3LO_4N_MEV):.3f} MeV"
          f"  = {float(100 * N3LO_4N_MEV / B_4HE):.2f}%")
    print(f"     ⇒ QOU μ₄ exceeds the N³LO 4N estimate by {float(r_n3lo):.0f}×")
    print(f"     ⇒ QOU μ₄ exceeds SRG-induced 4N by        {float(r_srg):.0f}×")

    mu4_check = S4 - G4
    print(f"\n [3] where the size comes from — the reference, not the physics")
    print(f"     s₄ (ρ_strong own 4-body) = {float(S4):+.4f} = {float(S4 * B_D):+.2f} MeV")
    print(f"     g₄ (ρ_grad  own 4-body)  = {float(G4):+.4f} = {float(G4 * B_D):+.2f} MeV")
    print(f"     μ₄ = s₄ − g₄             = {float(mu4_check):+.4f} = "
          f"{float(mu4_check * B_D):+.2f} MeV   (reproduces the witness)")
    print(f"     but s₄ alone is {float(100 * S4 * B_D / B_4HE):.0f}% of B(⁴He) — ALSO far too")
    print(f"     large for a 4N force. The inflation is in the C(A,k) simplex basis,")
    print(f"     which has no saturation mechanism, not only in ρ_grad.")

    decomp_ok = abs(mu4_check - MU4) < mp.mpf("1e-3")
    implausible = r_n3lo > 10
    s4_also_inflated = (S4 * B_D / B_4HE) > mp.mpf("0.1")

    print(f"\n ⇒ VERDICT: μ₄ = −4.591 is NOT a physical four-body quantity. Matching it")
    print(f"   is not the same as reproducing 4-body physics, so GAP-8's flat hierarchy")
    print(f"   is not by itself evidence against the operator, and 'what supplies ~10×")
    print(f"   growth?' is chasing a basis artifact. Reformulate against the Tjon")
    print(f"   correlation B(³H) ↔ B(⁴He) — convention-free, and the field's own robust")
    print(f"   observable for the 3-body/4-body question.")
    print(f"\n   SCOPE (a): this constrains the TARGET's physical interpretation. It does")
    print(f"   NOT show ρ_grad is wrong, and does NOT show the operator is right.")

    wb = WitnessBuilder("mu4-vs-nuclear-4n-force-bound", engine="mpmath")
    wb.set_description(
        "Tests whether the residual-simplex target μ₄ = −4.591 is a physical four-body quantity, "
        "by converting it to MeV and comparing against the nuclear-physics literature bounds on "
        "the genuine four-nucleon content of ⁴He. In units of B(D) = 2.224566 MeV the target is "
        "−10.21 MeV, i.e. 36% of the ⁴He binding energy (28.296 MeV). Jurgenson–Navrátil–"
        "Furnstahl (PRL 103, 082501 / arXiv:0905.1873) measure the SRG-induced four-body force at "
        "λ=2 fm⁻¹ as 'about 50 keV net' (0.18%) and quote the N³LO long-range 4N estimate as 'of "
        "order a few hundred keV' (~1.1%); the QOU μ₄ exceeds these by ~34× and ~204× "
        "respectively. Decomposed with the corpus's own unbalanced [n]_q, μ₄ = s₄ − g₄ with "
        "s₄ = +3.7804 (+8.41 MeV) and g₄ = +8.3706 (+18.62 MeV), so the large negative value is "
        "the ρ_grad = [A]_q!/[2]_q! reference OVER-SUBTRACTING. Note s₄ alone is 30% of B(⁴He), "
        "also far too large for a 4N force — the inflation is in the C(A,k) simplex basis, which "
        "has no saturation mechanism and attributes all departure from pairwise additivity to "
        "high-body coefficients, not specifically in ρ_grad. Pionless EFT (Platter–Hammer–"
        "Meißner, arXiv:nucl-th/0409040) explains the empirical Tjon B(³H)↔B(⁴He) correlation by "
        "the ABSENCE of a four-nucleon force at leading order, so there is no independent "
        "four-body scale for μ₄ to measure. CONSEQUENCE: matching μ₄ is not equivalent to "
        "reproducing 4-body physics; GAP-8's flat operator hierarchy (|μ₄/μ₃| = 1.02 vs 9.75) is "
        "not by itself evidence against the operator, and the bean qou-pve2 question 'what "
        "supplies ~10× per-order growth' is chasing a basis artifact. Honest reformulation: test "
        "the operator against the Tjon correlation, which is convention-free. SCOPE-(a): this "
        "constrains the TARGET's physical interpretation; it does NOT show ρ_grad is wrong and "
        "does NOT show the block-trace operator is right. Corpus-grep before declaring: 'Tjon', "
        "'four-nucleon force', '4N force' return ZERO hits across content/, docs/, computations/. "
        "No Δ_λ, no μ fitted, nothing wired.")
    wb.set_content_block("conj:binding-manybody-eq-jet-filtration")
    wb.add_data("mu4_physical_plausibility", {
        "mu4_in_B_D_units": float(MU4),
        "B_D_MeV": float(B_D), "B_4He_MeV": float(B_4HE),
        "mu4_MeV": float(mu4_mev),
        "mu4_as_fraction_of_B4He": float(frac),
        "lit_srg_induced_4N_MeV": float(SRG_4N_MEV),
        "lit_n3lo_4N_MeV": float(N3LO_4N_MEV),
        "excess_over_n3lo": float(r_n3lo), "excess_over_srg": float(r_srg),
        "s4": float(S4), "g4": float(G4),
        "s4_MeV": float(S4 * B_D), "g4_MeV": float(G4 * B_D),
        "s4_as_fraction_of_B4He": float(S4 * B_D / B_4HE),
        "references": [
            "Jurgenson, Navratil, Furnstahl, PRL 103, 082501 (2009), arXiv:0905.1873",
            "Platter, Hammer, Meissner, arXiv:nucl-th/0409040",
            "Epelbaum, Modern Theory of Nuclear Forces, arXiv:0811.1338",
            "Tjon, PRC 20, 340 (1979) — paywalled/pre-arXiv, NOT needed: superseded for "
            "this argument by nucl-th/0409040 which states and explains the correlation"],
        "verdict": ("mu4 = -4.591 is not a physical four-body quantity (34x the N3LO 4N "
                    "estimate, 36% of B(4He)); its size is the C(A,k) simplex basis and the "
                    "rho_grad over-subtraction, so matching it is not equivalent to reproducing "
                    "4-body physics — scope-(a) on the TARGET, not on the operator")})
    wb.add_assertion("mu4_decomposition_reproduces_witness", str(bool(decomp_ok)), "True")
    wb.add_assertion("mu4_exceeds_literature_4N_by_over_10x", str(bool(implausible)), "True")
    wb.add_assertion("s4_alone_also_exceeds_10pct_of_B4He", str(bool(s4_also_inflated)), "True")
    wb.save()
    print("\nwitness → mu4-vs-nuclear-4n-force-bound.witness.json")
    ok = decomp_ok and implausible and s4_also_inflated
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
