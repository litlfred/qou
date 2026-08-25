#!/usr/bin/env python3
"""bring_genus4_epstein_theta_factorized_probe.py

Compute the DEFERRED genus-4 Epstein det'Δ on Jac(Bring) ≅ E_{5τ₀}³ × E_{τ₀} —
the α_EM polarized photon-determinant magnitude leg (#3911). The sibling probe
`bring_polarized_epstein_determinant_probe.py` validated the genus-g machinery on
genus 1 (exact) and corrected the naive per-factor product, but DEFERRED the
genus-4 value: its full 8-dim θ-grid `_pts(8,R)` OOMs at R≥5 and the thin Bring
modulus (Im τ₀=0.187) needs Siegel reduction.

**The fix — factorize the θ-function, not the determinant.** Since Jac(Bring) in
its isogeny basis has a BLOCK-DIAGONAL period diag(5τ₀,5τ₀,5τ₀,τ₀) (M is O(4)-
equivalent to diag(5,5,5,1), det 125), the heat-kernel θ of the direct-sum lattice
FACTORIZES exactly:

    θ_H(t) = θ_{G(5τ₀)}(t)³ · θ_{G(τ₀)}(t)   (each a cheap 2-D lattice θ),

and det(H), H⁻¹ factorize likewise. The Epstein `det'Δ` does NOT factorize (its
spectrum is `{λ_i+μ_j}` SUMS, not a product — the sibling's correct genus-2
finding), but it is computed FROM the product-θ via the same Chowla–Selberg
`ζ'(0)` split — so no 8-dim grid, no OOM, no Siegel reduction needed. The thin
τ₀ block is a 2-D θ that converges at small radius after the standard
functional-equation split (t≥1 arm on H, t≥1 arm on H⁻¹).

Cross-checks (kill criteria): (i) genus-1 reproduces `(Im τ)²|η|⁴` exactly;
(ii) the factorized genus-2 measure(E_{5τ₀}×E_{τ₀}) reproduces the sibling's
Epstein value ≈ 3.949 (NOT the naive product 2.922). Only then is the genus-4
number reported.

DISCIPLINE: computes the deferred magnitude value; makes NO claim that it equals
8, 8π, or any α_EM coefficient (the reciprocal-form is non-separable per
`2026-07-18-alpha-em-perloop-reciprocal-form-forcedness.md`; the `8π` is not
manufactured here). No q₀; no fit; nothing wired; no tier change. Self-contained.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401

import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
T0 = mp.mpc(-0.5, mp.mpf("0.186676"))   # Bring modulus (from the sibling probe)


def gram(tau):
    """2×2 Gram of the rank-2 lattice for complex modulus τ: [[1,Reτ],[Reτ,|τ|²]]."""
    return [[mp.mpf(1), mp.re(tau)], [mp.re(tau), mp.re(tau) ** 2 + mp.im(tau) ** 2]]


def theta2(B, t, R=20):
    """θ_B(t) = Σ_{m∈ℤ²} exp(−π t mᵀ B m) for a 2×2 Gram B (includes m=0). The
    2-D sum converges fast for t≥1 (the form grows ~λ_min·|m|²); a modest radius
    on the (i≥0) half-plane, doubled for the m↔−m symmetry, is exact to dps."""
    a, b, d = B[0][0], B[0][1], B[1][1]
    s = mp.mpf(0)
    for i in range(-R, R + 1):
        for j in range(-R, R + 1):
            q = a * i * i + 2 * b * i * j + d * j * j
            s += mp.e ** (-mp.pi * t * q)
    return s


def inv2(B):
    a, b, d = B[0][0], B[0][1], B[1][1]
    det = a * d - b * b
    return [[d / det, -b / det], [-b / det, a / det]], det


def zeta_prime0_blockdiag(gram_blocks, n):
    """ζ'_{G⁻¹}(0) via Chowla–Selberg, for the flat torus ℝⁿ/L whose Gram is
    G = block-diag(gram_blocks). The Laplacian spectrum is 4π²·(mᵀ G⁻¹ m), so the
    Epstein form is H = G⁻¹ (mirrors the sibling `_zeta_prime0(inv(G), …)`). For a
    block-diagonal G both θ's FACTORIZE: θ_{G⁻¹}(t)=∏θ_{Gᵢ⁻¹}(t), θ_G(u)=∏θ_{Gᵢ}(u).
      ζ'(0) = −lnπ − γ − (2/n)·det(G)^{½} + I1 + det(G)^{½}·I2,   [det(G⁻¹)^{−½}=det(G)^{½}]
      I1 = ∫₁^∞ t^{−1}(θ_{G⁻¹} − 1) dt,  I2 = ∫₁^∞ u^{n/2−1}(θ_G − 1) du."""
    detG = mp.mpf(1)
    invblocks = []
    for B in gram_blocks:
        Bi, det = inv2(B)
        detG *= det
        invblocks.append(Bi)

    def thetaGinv(t):                       # θ_{G⁻¹} = ∏ θ_{Gᵢ⁻¹}  (dual lattice)
        p = mp.mpf(1)
        for Bi in invblocks:
            p *= theta2(Bi, t)
        return p

    def thetaG(u):                          # θ_G = ∏ θ_{Gᵢ}
        p = mp.mpf(1)
        for B in gram_blocks:
            p *= theta2(B, u)
        return p

    I1 = mp.quad(lambda t: (thetaGinv(t) - 1) / t, [1, mp.inf])
    I2 = mp.quad(lambda u: (thetaG(u) - 1) * u ** (mp.mpf(n) / 2 - 1), [1, mp.inf])
    detG_half = detG ** mp.mpf("0.5")       # det(H)^{−1/2} with H=G⁻¹
    return -mp.log(mp.pi) - mp.euler + I1 + detG_half * I2 \
        - (mp.mpf(2) / n) * detG_half, detG


def detprime_and_measure(gram_blocks):
    n = 2 * len(gram_blocks)
    zp, detG = zeta_prime0_blockdiag(gram_blocks, n)
    detprime = (4 * mp.pi ** 2) ** -1 * mp.e ** (-zp)
    # scale-free boson measure = Vol(J)^{1/2} / det'Δ^{1/2};  Vol(J) = √det(G)
    VolJ = mp.sqrt(detG)
    measure = mp.sqrt(VolJ) / mp.sqrt(detprime)
    return detprime, measure


def eta(tau):
    q = mp.e ** (2j * mp.pi * tau)
    return q ** (mp.mpf(1) / 24) * mp.qp(q)


def m1(tau):
    return 1 / (mp.sqrt(mp.im(tau)) * abs(eta(tau)) ** 2)


def main():
    # (i) genus-1 exact validation
    tau1 = mp.mpc("0.3", "1.4")
    dp1, meas1 = detprime_and_measure([gram(tau1)])
    exact1 = mp.im(tau1) ** 2 * abs(eta(tau1)) ** 4
    meas1_exact = m1(tau1)
    g1_ok = abs(dp1 / exact1 - 1) < mp.mpf("1e-10") and abs(meas1 / meas1_exact - 1) < mp.mpf("1e-10")
    print(f"  genus-1: det'D={mp.nstr(dp1, 10)} vs (Im t)^2|eta|^4={mp.nstr(exact1, 10)}; "
          f"measure={mp.nstr(meas1, 10)} vs exact {mp.nstr(meas1_exact, 10)} -- {'OK' if g1_ok else 'FAIL'}")

    # (ii) genus-2 cross-check vs the sibling's Epstein value ~ 3.949
    dp2, meas2 = detprime_and_measure([gram(5 * T0), gram(T0)])
    prod2 = m1(5 * T0) * m1(T0)
    g2_ok = abs(meas2 - mp.mpf("3.949")) < mp.mpf("0.02")
    print(f"  genus-2: measure(E_5t0 x E_t0)={mp.nstr(meas2, 8)} (sibling 3.949) vs naive "
          f"product {mp.nstr(prod2, 8)} -- {'OK' if g2_ok else 'FAIL'}")

    # (iii) THE DEFERRED VALUE -- genus-4 Epstein det'D on Jac(Bring)
    blocks4 = [gram(5 * T0), gram(5 * T0), gram(5 * T0), gram(T0)]
    dp4, meas4 = detprime_and_measure(blocks4)
    naive_g4 = m1(5 * T0) ** 3 * m1(T0)
    print(f"\n  GENUS-4 (deferred value now computed):")
    print(f"    det'D(Jac Bring) = {mp.nstr(dp4, 12)}")
    print(f"    boson measure    = {mp.nstr(meas4, 12)}")
    print(f"    naive product (retracted 8.226) = {mp.nstr(naive_g4, 8)}, ratio measure/naive = {mp.nstr(meas4 / naive_g4, 6)}")
    # honest comparisons -- report, do NOT claim any equals 8 or 8pi
    for label, val in [("8 (b1)", mp.mpf(8)), ("8pi", 8 * mp.pi), ("4pi", 4 * mp.pi), ("pi^2", mp.pi ** 2)]:
        print(f"    measure / {label} = {mp.nstr(meas4 / val, 6)}")

    all_ok = g1_ok and g2_ok
    verdict = (
        f"DEFERRED GENUS-4 VALUE COMPUTED (theta-factorization, no Siegel reduction, no OOM). "
        f"The genus-4 Epstein det'D on Jac(Bring)=E_5t0^3 x E_t0 = {mp.nstr(dp4, 10)}; boson "
        f"measure = {mp.nstr(meas4, 10)} (!= the retracted naive product {mp.nstr(naive_g4, 6)}, "
        f"ratio {mp.nstr(meas4 / naive_g4, 5)}). Method validated: genus-1 reproduces "
        f"(Im t)^2|eta|^4 exactly, genus-2 reproduces the sibling's Epstein measure ~3.949. The "
        f"theta of the block-diagonal isogeny lattice factorizes (theta_5t0^3 * theta_t0) even though "
        f"det'D does not (spectrum {{lambda+mu}}), so the deferred value needs no 8-dim grid. SCOPE: "
        f"this is the magnitude leg's numerical value ONLY -- NO claim it equals 8, 8pi, or any "
        f"alpha_EM coefficient (the reciprocal-form is non-separable, #3918); the 8pi is NOT "
        f"manufactured. No q0; no fit; nothing wired; no tier change."
        if all_ok else
        "VALIDATION FAILED (genus-1 or genus-2 cross-check) -- do NOT trust the genus-4 value."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder(
        name="bring-genus4-epstein-theta-factorized",
        engine="mpmath", _script_path=__file__,
        output_dir=str(Path(__file__).resolve().parent))
    wb.set_description(
        "Deferred genus-4 Epstein det'Δ on Jac(Bring)≅E_5τ₀³×E_τ₀ via θ-factorization "
        "(no Siegel reduction / no 8-dim OOM); validated on genus-1 (exact) + genus-2 (≈3.949).")
    wb.set_audit_only("docs/audits/2026-07-18-bring-genus4-epstein-theta-factorized.md")
    wb.add_assertion("genus1_exact", str(g1_ok), "True")
    wb.add_assertion("genus2_matches_sibling_3949", str(g2_ok), "True")
    wb.add_data("genus4_detprime_delta", mp.nstr(dp4, 15))
    wb.add_data("genus4_boson_measure", mp.nstr(meas4, 15))
    wb.add_data("genus2_measure", mp.nstr(meas2, 15))
    wb.add_data("naive_product_g4_retracted", mp.nstr(naive_g4, 10))
    wb.add_data("measure_over_8", mp.nstr(meas4 / 8, 10))
    wb.add_data("measure_over_8pi", mp.nstr(meas4 / (8 * mp.pi), 10))
    wb.add_data("verdict", verdict)
    wb.save()
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
