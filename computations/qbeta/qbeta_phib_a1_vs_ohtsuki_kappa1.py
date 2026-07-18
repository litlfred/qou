#!/usr/bin/env python3
"""
qbeta_phib_a1_vs_ohtsuki_kappa1.py — SELF-REVIEW CORRECTION of the merged Φ_b 2-loop
(#3854/#3859): the saddle A₁ is a clean exact object but is NOT the 4₁ Ohtsuki 2-loop
invariant κ₁, so the potential V=Li₂(z)−Li₂(1/z) is not the 4₁ state integral and A₁ is
mis-identified as "the" b-dictionary.

Motivation (no external reviewer since Gemini sunset; standing red-team duty). #3854 derived
A₁ = the 2-loop of V(z)=Li₂(z)−Li₂(1/z) at z*=e^{iπ/3}, gated on G1 (Vol(4₁)) + G2 (torsion
√3) + G3 (formula). Those gates are NECESSARY but NOT SUFFICIENT to identify the potential:
the true 4₁ state integral has the SAME Vol and torsion, but its 2-loop invariant is the
known Ohtsuki κ₁ = 11√3π/108 (corpus #3571/#3606, fit from the Kashaev invariant ⟨4₁⟩_N).
This probe runs the sufficiency check #3854 omitted.

FINDINGS (exact, 50+ dps):
  1. A₁ = 1/3 + (17√3/108)·i  — EXACT (both parts, to 1e-48). A clean, correctly-computed
     2-loop of THAT potential; the #3854 numerics stand.
  2. κ₁ = 11√3π/108 = 0.5542165 (real). Under the ℏ = 2πi/N dictionary the state-integral
     2-loop maps to the coeff of 1/N; A₁·2πi = −1.713 + 2.094i — NOT the real κ₁, and no
     clean single-factor conversion matches (κ₁/A₁ = 0.996 − 0.815i, etc.).
  ⇒ A₁ ≠ κ₁. Since a correct 4₁ state integral's 2-loop WOULD equal the Ohtsuki κ₁
     (Ohtsuki = perturbative-CS = state-integral loop expansion — same invariants),
     V=Li₂(z)−Li₂(1/z) is NOT the 4₁ state integral. It reproduces Vol + torsion but
     diverges at 2-loop.

CORRECTION (scope-(a); re-scope, do not delete — the number stands, the identification was
wrong): #3854's A₁ is the exact 2-loop of a Vol+torsion-matched potential, MIS-IDENTIFIED
as "the 4₁ Φ_b 2-loop b-dictionary". The physical loop invariants / b-dictionary are the
corpus κ-tower (κ₁ = 11√3π/108, κ₃ = (1081/21870)√3π³, κ₄ = (98/729)π⁴), already in hand.
So the A₁↔d_k question resolves: A₁ is not a loop invariant of the physical 4₁ integral, so
it is neither a prefactor normalization nor a ladder coefficient OF THE RIGHT OBJECT — the
κ-tower is. No c_k wired; L2 unchanged (2/7). This retires the "Φ_b 2-loop b-dictionary"
line: the correct object was already the κ-tower the corpus derived.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

mp.mp.dps = 60


def V(z):
    return mp.polylog(2, z) - mp.polylog(2, 1 / z)


def main() -> int:
    print("=== SELF-REVIEW: is #3854's A₁ the 4₁ Ohtsuki 2-loop κ₁? ===\n")
    z = mp.exp(1j * mp.pi / 3)
    V2, V3, V4 = mp.diff(V, z, 2), mp.diff(V, z, 3), mp.diff(V, z, 4)
    A1 = V4 / (8 * V2 ** 2) - 5 * V3 ** 2 / (24 * V2 ** 3)

    # 1. exact closed form of A₁
    re_exact = abs(mp.re(A1) - mp.mpf(1) / 3) < mp.mpf(10) ** (-48)
    im_exact = abs(mp.im(A1) - 17 * mp.sqrt(3) / 108) < mp.mpf(10) ** (-48)
    print(f"A₁ = {mp.nstr(A1, 16)}")
    print(f"  Re A₁ = 1/3            : {'EXACT' if re_exact else 'NO'} "
          f"(resid {mp.nstr(mp.re(A1) - mp.mpf(1)/3, 3)})")
    print(f"  Im A₁ = 17√3/108       : {'EXACT' if im_exact else 'NO'} "
          f"(resid {mp.nstr(mp.im(A1) - 17*mp.sqrt(3)/108, 3)})")
    a1_exact = re_exact and im_exact

    # 2. the true 4₁ Ohtsuki 2-loop invariant (corpus/literature, Kashaev fit)
    kappa1 = 11 * mp.sqrt(3) * mp.pi / 108
    print(f"\nκ₁ (Ohtsuki 2-loop, corpus #3571/#3606) = 11√3π/108 = {mp.nstr(kappa1, 14)} (real)")

    # 3. sufficiency check: does A₁ map to κ₁ under any standard conversion?
    conversions = {
        "A₁": A1, "2πi·A₁ (ℏ=2πi/N)": A1 * 2j * mp.pi, "2π·A₁": A1 * 2 * mp.pi,
        "i·A₁": A1 * 1j, "π·A₁": A1 * mp.pi, "2π·Im A₁": 2 * mp.pi * mp.im(A1),
    }
    print(f"\nsufficiency check — A₁ vs κ₁ under standard normalizations:")
    best_rel = mp.inf
    for name, val in conversions.items():
        rel = abs(val - kappa1) / abs(kappa1)
        best_rel = min(best_rel, rel)
        print(f"  {name:20} = {mp.nstr(val, 10):>26}   |Δκ₁|/κ₁ = {mp.nstr(rel, 6)}")
    matches = best_rel < mp.mpf("1e-6")
    print(f"\n  best relative match to κ₁: {mp.nstr(best_rel, 4)} "
          f"({'MATCH' if matches else 'NO MATCH — A₁ ≠ κ₁'})")

    # verdict
    print(f"\n### Verdict:")
    print(f"  • A₁ = 1/3 + (17√3/108)·i is EXACT — the #3854 saddle 2-loop is correctly computed.")
    print(f"  • A₁ ≠ the Ohtsuki κ₁ = 11√3π/108 (the true 4₁ 2-loop). Since a correct 4₁ state")
    print(f"    integral's 2-loop equals κ₁, V=Li₂(z)−Li₂(1/z) is NOT the 4₁ state integral —")
    print(f"    it matches Vol + torsion but diverges at 2-loop.")
    print(f"  • CORRECTION (scope-(a)): #3854's A₁ is a clean object but MIS-IDENTIFIED as the")
    print(f"    Φ_b 2-loop b-dictionary. The physical b-dictionary is the corpus κ-tower")
    print(f"    (κ₁=11√3π/108, κ₃, κ₄), already derived. Retires the 'Φ_b 2-loop' line.")

    ok = a1_exact and (not matches)   # the finding is: A₁ exact AND A₁ ≠ κ₁
    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("qbeta-phib-a1-vs-ohtsuki-kappa1", engine="mpmath")
        wb.set_description(
            "Self-review correction of the merged Φ_b 2-loop (#3854/#3859). The saddle A₁ of "
            "V=Li2(z)-Li2(1/z) at z*=e^{iπ/3} is EXACT: A₁ = 1/3 + (17√3/108)i (50+ dps). But "
            "A₁ is NOT the 4₁ Ohtsuki 2-loop invariant κ₁ = 11√3π/108 (corpus Kashaev fit) "
            "under any standard normalization (ℏ=2πi/N gives A₁·2πi = −1.713+2.094i ≠ real "
            "κ₁; best rel match ~0.6). Since a correct 4₁ state integral's 2-loop equals the "
            "Ohtsuki κ₁ (Ohtsuki = perturbative-CS = state-integral loop expansion), "
            "V=Li2(z)-Li2(1/z) is NOT the 4₁ state integral — it matches Vol+torsion (the "
            "#3854 G1/G2 gates, necessary not sufficient) but diverges at 2-loop. CORRECTION "
            "(scope-(a), re-scope not delete): #3854's A₁ is a clean but MIS-IDENTIFIED "
            "object; the physical b-dictionary is the corpus κ-tower already derived. A₁↔d_k "
            "resolves: A₁ is not a loop invariant of the physical integral. No c_k wired; L2 "
            "2/7. Retires the Φ_b-2-loop b-dictionary line.")
        wb.add_data("A1", [float(mp.re(A1)), float(mp.im(A1))])
        wb.add_data("A1_exact_form", "1/3 + (17*sqrt(3)/108)*i")
        wb.add_data("A1_re_is_one_third", bool(re_exact))
        wb.add_data("A1_im_is_17sqrt3_over_108", bool(im_exact))
        wb.add_data("ohtsuki_kappa1", float(kappa1))
        wb.add_data("best_rel_match_to_kappa1", float(best_rel))
        wb.add_data("A1_equals_kappa1", bool(matches))
        wb.add_assertion(
            name="A1_exact_but_not_ohtsuki_kappa1",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("A₁ = 1/3 + 17√3/108 i exact (50+ dps); A₁ ≠ Ohtsuki κ₁=11√3π/108 "
                    "(best rel %.3f) ⇒ V=Li2(z)-Li2(1/z) is not the 4₁ state integral; "
                    "#3854's A₁ mis-identified as the b-dictionary — the κ-tower is the "
                    "physical object. Scope-(a) correction; no c_k wired."
                    % float(best_rel)))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness skipped: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
