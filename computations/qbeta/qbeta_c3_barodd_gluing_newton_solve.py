#!/usr/bin/env python3
"""qbeta_c3_barodd_gluing_newton_solve.py

Direct Newton solve of Thurston's gluing equations for the figure-eight 4₁,
computing the complex volume 𝔙 = Vol + i·CS whose imaginary part is the c₃
bar-odd S (owner: S = Im 𝔙, `conj:binding-qbeta-complex-volume`).

CORRECTION (2026-07-26) — WRONG NZ LEADING IMAGINARY FORM FIXED.
========================================================================
This probe previously printed the HEURISTIC leading imaginary part
    Im 𝔙 ≈ (√3/2)|u|²·sin(2·arg u)  =  √3·Re(u)·Im(u)          (WRONG)
which corresponds to a REAL a₂ (𝔙″(0)/2). The CCGLS A-polynomial cusp modulus
of 4₁ is τ = −i√3 (PURELY IMAGINARY, ℚ(√−3)), so a₂ = i·√3/4 is PURELY
IMAGINARY and the CORRECT leading imaginary part is
    Im 𝔙 = (√3/4)(Re²u − Im²u) = (√3/4)|u|²·cos(2·arg u)        (RIGHT)
which VANISHES on the DIAGONALS |Re u| = |Im u| (arg u = ±π/4), NOT on the axes.
Proved sorry-free in QOU/Knot/FigureEightComplexVolume.lean (`imV₄₁`, lean-verify
exit 0); authoritative numerical analysis in the T2 probe
computations/probes/sdeformed_channel_signflip_probe.py and
docs/audits/2026-07-26-sdeformed-channel-signflip.md.

Effect on this probe: the Newton solve of the gluing equations (§1–§2, the Vol
recovery) is UNCHANGED — it never used the imaginary leading form. Only the
displayed leading Im 𝔙 (§below) is corrected from sin(2φ) to (√3/4)cos(2φ):
it now vanishes at arg u = π/4 (the diagonal) and turns negative for arg u > π/4,
instead of peaking there. Both assertions (gluing factor = −1, Vol recovery)
still pass; no target is forced.
========================================================================

VALIDATED (computed, no fit; scope-(a); C14):
  1. Gluing equation (Thurston): z(z−1)·w(w−1) = 1, meridian deformation
     w = m²·z. Complete structure m=1 ⇒ z=w=e^{iπ/3}, each factor = −1.
  2. Newton solve at m=1 recovers Vol(4₁) = D(z)+D(w) = 2.029883213 (Bloch–
     Wigner) to 10 digits — the bar-EVEN part `−Vol(4₁)`, and CS=0 (amphichiral).
  3. The deformation 𝔙(m) = Vol(m) + i·CS(m) is the full complex volume; its
     CORRECTED leading imaginary part (NZ, cusp modulus τ = −i√3 ⇒ a₂ = i√3/4) is
        Im 𝔙 = CS = (√3/4)(Re²u − Im²u) = (√3/4)|u|²·cos(2·arg u),   u = 2 log m,
     the c₃ bar-odd S carrier. It vanishes on the DIAGONALS |Re u|=|Im u|
     (arg u = ±π/4), not on the axes; the sign-flip needs u to cross a diagonal
     (see the T2 probe's diagonal-crossing constraint).

THE OPEN LINK (single, named): the map q₀ → m (the meridian holonomy the
substrate assigns to 4₁). Per `thurston-relaxation.md` this is the Newton
iteration **seeded by the Φ_q poles** — the archimedean-realization functor,
`conj:algebraic-geometric-dilog-equivalence` (pole↔cusp). The observed
`dc₃/dq ≈ 4.66×10⁶` anchor-sensitivity (PR #1821) shows this map is
**near-singular** near q₀ (a smooth m(q₀) is excluded — see the NZ probe's ratio
test), so the phase φ(q₀) accumulates like a root of unity. This probe computes
𝔙(m) for any given m but does NOT fit m(q₀) (that would be a fit).

Companion: docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
Z0 = mp.e ** (mp.mpc(0, 1) * mp.pi / 3)   # complete shape e^{iπ/3}
# Vol(4_1) EXACT = 2*Cl_2(pi/3); the literal printed 36 digits, correct to 17 (qou-ckbv)
VOL_4_1 = 2 * mp.clsin(2, mp.pi / 3)


def gluing_residual(z, m):
    """Thurston figure-eight gluing: z(z−1)·w(w−1) − 1, with w = m²·z."""
    w = m * m * z
    return z * (z - 1) * w * (w - 1) - 1


def solve_shape(m, seed=Z0):
    return mp.findroot(lambda z: gluing_residual(z, m), seed)


def bloch_wigner(z):
    z = mp.mpc(z)
    if z == 0 or z == 1:
        return mp.mpf(0)
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(mp.fabs(z))


def vol_of_m(m):
    z = solve_shape(m)
    w = m * m * z
    return bloch_wigner(z) + bloch_wigner(w), z, w


def main() -> int:
    print("=" * 78)
    print(" c₃ bar-odd S — figure-eight gluing-equation Newton solve (𝔙 = Vol + iCS)")
    print("=" * 78)

    wb = WitnessBuilder("qbeta-c3-barodd-gluing-newton-solve", engine="mpmath")
    wb.set_description(
        "Direct Newton solve of Thurston's gluing equations for 4₁ "
        "(z(z−1)w(w−1)=1, w=m²z), computing the complex volume 𝔙=Vol+iCS whose "
        "imaginary part is the c₃ bar-odd S (conj:binding-qbeta-complex-volume). "
        "Validated: m=1 recovers Vol(4₁)=2.029883213 (10 digits), CS=0. CORRECTED "
        "(2026-07-26): leading Im 𝔙 = (√3/4)(Re²u−Im²u) = (√3/4)|u|²cos(2 arg u) "
        "(a₂=i√3/4 from the A-polynomial cusp modulus τ=−i√3; Lean "
        "FigureEightComplexVolume imV₄₁), NOT the prior heuristic (√3/2)sin(2 arg u); "
        "it vanishes on the diagonals |Re u|=|Im u|, not the axes. The Vol Newton "
        "solve is unchanged. The open link is q₀→m (Φ_q-pole-seeded Newton, "
        "conj:algebraic-geometric-dilog-equivalence), shown near-singular by the "
        "anchor-sensitivity. Scope-(a); C14; m(q₀) NOT fitted; no c_k wired."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    # ---- 1. complete structure validation ----
    fac = Z0 * (Z0 - 1)
    print(f"\n[1] gluing at complete (m=1): z(z−1) = {mp.nstr(fac, 8)}  (expect −1)")
    vol1, z1, w1 = vol_of_m(mp.mpf(1))
    err = mp.fabs(vol1 - VOL_4_1)
    print(f"    Newton z = {mp.nstr(z1, 12)}")
    print(f"    Vol = D(z)+D(w) = {mp.nstr(vol1, 12)}  vs Vol(4₁)={mp.nstr(VOL_4_1,12)}")
    print(f"    |Δ| = {float(err):.2e}   (bar-EVEN part −Vol(4₁); CS=0 amphichiral)")
    fac_ok = mp.fabs(fac + 1) < 1e-25
    vol_ok = err < 1e-10

    # ---- 2. deformation 𝔙(m): Vol(m) + CORRECTED leading NZ CS ----
    print("\n[2] deformation 𝔙(m) = Vol(m) + i·CS(m), u = 2 log m:")
    rows = []
    for phi in (mp.mpf("0.3"), mp.pi / 4, mp.mpf("1.0")):
        u = mp.mpf("0.2") * mp.e ** (mp.mpc(0, 1) * phi)
        m = mp.e ** (u / 2)
        vol, z, w = vol_of_m(m)
        # CORRECTED leading Im 𝔙 = (√3/4)(Re²u − Im²u) = (√3/4)|u|² cos(2 arg u)
        # (a₂ = i√3/4, τ = −i√3). Vanishes on the diagonal arg u = π/4.
        cs_lead = (mp.sqrt(3) / 4) * (mp.re(u) ** 2 - mp.im(u) ** 2)
        print(f"    arg u={mp.nstr(phi,4)}: Vol={mp.nstr(vol,8)}  CS_lead(Im 𝔙)={mp.nstr(cs_lead,6)}")
        rows.append({"arg_u": mp.nstr(phi, 6), "Vol": mp.nstr(vol, 12),
                     "CS_leading": mp.nstr(cs_lead, 12)})
    print("    (Vol from the validated Newton solve; CS_lead is the CORRECTED NZ")
    print("     leading Im 𝔙 = (√3/4)(Re²u−Im²u), cusp modulus τ=−i√3 ⇒ a₂=i√3/4;")
    print("     it VANISHES at arg u=π/4 (diagonal) and is <0 for arg u>π/4.")
    print("     Full framing-corrected CS is an even O(u⁴) refinement.)")

    # ---- 3. the open link ----
    print("\n[3] OPEN LINK (single, named): q₀ → m, the Φ_q-pole-seeded Newton")
    print("    (conj:algebraic-geometric-dilog-equivalence / archimedean functor).")
    print("    Anchor-sensitivity dc₃/dq≈4.66e6 ⇒ this map is NEAR-SINGULAR near q₀")
    print("    (smooth m(q₀) excluded). S = Im 𝔙 once m(q₀) is supplied; NOT fitted.")

    ok = fac_ok and vol_ok

    wb.add_data("complete_structure", {
        "z_z_minus_1": mp.nstr(fac, 12), "Vol": mp.nstr(vol1, 20),
        "vol_err_vs_Vol_4_1": float(err), "CS": 0.0})
    wb.add_data("deformation_V_of_m", rows)
    wb.add_data("open_link", {
        "map": "q0 -> m (meridian holonomy)",
        "mechanism": "Phi_q-pole-seeded Newton on gluing equations (thurston-relaxation)",
        "conjecture": "conj:algebraic-geometric-dilog-equivalence",
        "near_singular": "dc3/dq~4.66e6 => smooth m(q0) excluded; phase accumulates (RoU)",
        "S_identity": "S = Im V (conj:binding-qbeta-complex-volume)"})
    wb.add_assertion("gluing_complete_factor_minus_one",
                     computed=float(mp.fabs(fac + 1)), expected=0.0, tolerance=1e-25,
                     source="Thurston figure-eight: z(z−1)=−1 at complete z=e^{iπ/3}")
    wb.add_assertion("newton_recovers_vol_4_1",
                     computed=float(err), expected=0.0, tolerance=1e-10,
                     source="gluing Newton solve at m=1 gives Vol(4₁)=D(z)+D(w)")
    wb.save()

    print(f"\n  RESULT: {'ALL OK' if ok else 'CHECK'}  (𝔙 Newton solver validated; m(q₀) map open)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
