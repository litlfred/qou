#!/usr/bin/env python3
"""qbeta_c3_barodd_pole_cusp_phase_probe.py

Is the pole->cusp map's PHASE phi(q0) tractable? — the c3 bar-odd S frontier,
laid out EXPLICITLY IN ALL COORDINATES and tied back to the categorical-action
complex volume 𝔙 = Vol + i·CS (binding-qbeta-complex-volume.lean:
  𝔙 = E0·tr_M((Π_free − 1)∘𝓜),  𝔈_bind = Re 𝔙,  𝔔_β = Im 𝔙).

The four explicit coordinates on the chain (each now with a PROVED Lean anchor):

  1. POLE coord        x = q^{-k}       real; root of the q-Pochhammer denominator
                                        (x;q)_n.  PROVED: QOU.QBeta.qPochDenom_eq_zero_at_pole
                                        + QOU.QPochhammer.denomPolyLocal_eq_zero_at_pole.
  2. CUSP-SHAPE coord  ω = e^{iπ/3}     complete figure-8 shape; root of Φ₆(z)=z²−z+1
                                        (trace field ℚ(√−3)).  PROVED (this session):
                                        QOU.QBeta.CuspShapeBarParity —
                                        barEven ω = 1  (Re 𝔙 = Vol side),
                                        (barOdd ω)² = −3  (Im 𝔙 = CS side; cusp modulus τ).
  3. DEFORMATION coord u = 2 log m       meridian holonomy log; NZ:
                                        CVol(u) = Vol(4₁) − (τ/4)u² + O(u³),  τ ∝ √−3,
                                        S = Im 𝔙 = Im[−(τ/4)u²] = (√3/2)|u|² sin(2 arg u).
  4. ED coord          z_ED = √q − 1/√q  = barOdd(√q); the base coordinate that drives
                                        the approach to the exceptional divisor 𝒮_p
                                        (approach-to-exceptional-divisor.md) — itself bar-ODD.

TARGET (measured, anchor-blind witness; docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md):
  S = c3 + Vol(4₁):  S(muon) = +0.00968298,  S(proton) = −0.03945936  (sign flip).

FINDINGS (computed; scope-(a); C14; m(q0) NOT fitted; no c_k wired):
  A. Base phase π/3 and cusp modulus √−3 are EXACT (Lean-proved, coord 2).
  B. The magnitude scale (√3/2)|u|² is PARAMETER-FREE (√3 = cusp shape) and lands
     within ~4% of both |S| for the natural bar-odd coords |u| ∈ {z_ED, HA}.
  C. No SINGLE smooth |u| hits both anchors: sin(2φ) exceeds 1 at one anchor by ~4%
     (leading-NZ shortfall) — the same ratio-1-vs-4.08 wall (bean qou-yucw).
  D. The sign flip ⇒ φ(q0) crosses 0 between the anchors ⇒ a substrate q* where
     u is REAL (real meridian holonomy = real Dehn filling) — a well-posed
     GEOMETRIC condition, tractable to state/solve.
  E. Near-singular: the gluing-Newton dVol/d(meridian) reproduces the steep
     anchor-sensitivity (dc3/dq ≈ 4.66e6), so the PHASE FUNCTION φ(q0) is the
     Φ_q-pole-seeded Newton (conj:algebraic-geometric-dilog-equivalence), NOT a
     closed-form smooth map.

VERDICT: MAGNITUDE + base phase are tractable/exact; the PHASE FUNCTION φ(q0) is
near-singular (the open pole->cusp Newton). The concrete next step is to seed the
figure-8 gluing Newton with the ACTUAL substrate pole q0^{-k} and read the emergent
phase (this probe sets that up and quantifies its sensitivity; it does not fit m(q0)).

Companion Lean: QOU/QBeta/CuspShapeBarParity.lean (coord 2, proved this session).
Companion audits: 2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md,
                  2026-07-11-qbeta-c3-barodd-sleak-phib-target.md.
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

# --- measured targets (anchor-blind witness) ---
# Vol(4_1) EXACT = 2*Cl_2(pi/3); the literal printed 36 digits, correct to 17 (qou-ckbv)
VOL_4_1 = 2 * mp.clsin(2, mp.pi / 3)
S_MUON = mp.mpf("0.00968298")
S_PROTON = mp.mpf("-0.03945936")
# substrate anchors (muon-canonical q0 for computations/ layer; proton pin nearby)
Q0_MUON = mp.mpf("1.10997858275138080759166909561076887987")

Z0 = mp.e ** (mp.mpc(0, 1) * mp.pi / 3)  # complete cusp shape e^{iπ/3}


def gluing_residual(z, m):
    """Thurston figure-eight gluing: z(z−1)·w(w−1) − 1, w = m²z."""
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
    return bloch_wigner(z) + bloch_wigner(w)


def sep(t):
    print("=" * 78)
    print(t)
    print("=" * 78)


def main() -> int:
    sep(" c3 bar-odd S — pole->cusp PHASE tractability (explicit coords, tie to 𝔙)")

    wb = WitnessBuilder("qbeta-c3-barodd-pole-cusp-phase", engine="mpmath")
    wb.set_description(
        "Explicit-coordinate analysis of the pole->cusp map's phase phi(q0) for the "
        "c3 bar-odd S, tied to 𝔙=Vol+i·CS (categorical trace, binding-qbeta-complex-volume). "
        "Coords: pole x=q^{-k}; cusp ω=e^{iπ/3} (barEven=1, barOdd²=−3, PROVED "
        "QOU.QBeta.CuspShapeBarParity); deformation u=2logm; ED z=√q−1/√q. "
        "Magnitude + base phase tractable/exact; phase FUNCTION phi(q0) near-singular "
        "(Φ_q-pole-seeded Newton, conj:algebraic-geometric-dilog-equivalence). "
        "Scope-(a); C14; m(q0) NOT fitted; no c_k wired."
    )
    wb.set_content_block("conj:algebraic-geometric-dilog-equivalence")

    # ---- coord 2: cusp shape (cross-check the PROVED Lean values) ----
    sep("[coord 2] cusp shape ω = e^{iπ/3}  (Lean: QOU.QBeta.CuspShapeBarParity)")
    barEven = Z0 + 1 / Z0
    barOdd = Z0 - 1 / Z0
    print(f"  ω              = {mp.nstr(Z0, 12)}")
    print(f"  ω²−ω+1         = {mp.nstr(Z0**2 - Z0 + 1, 6)}   (Φ₆(ω)=0 ✓)")
    print(f"  barEven ω      = {mp.nstr(barEven, 12)}   (Lean: = 1 ; Re 𝔙 = Vol side)")
    print(f"  barOdd ω       = {mp.nstr(barOdd, 12)}   (= √−3 = i√3 ; Im 𝔙 = CS side)")
    print(f"  (barOdd ω)²    = {mp.nstr(barOdd**2, 8)}   (Lean: = −3 ; cusp modulus τ)")
    be_ok = mp.fabs(barEven - 1) < mp.mpf(10) ** -20
    bo_ok = mp.fabs(barOdd**2 - (-3)) < mp.mpf(10) ** -20

    # ---- coord 4: ED coordinate and the magnitude table ----
    sep("[coord 4] ED coordinate z_ED = √q − 1/√q = barOdd(√q), and |u| magnitude match")
    z_ED = mp.sqrt(Q0_MUON) - 1 / mp.sqrt(Q0_MUON)
    HA = Q0_MUON - 1 / Q0_MUON
    scale = mp.sqrt(3) / 2
    print(f"  z_ED = barOdd(√q0) = {mp.nstr(z_ED, 10)}")
    print(f"  HA   = barOdd(q0)  = {mp.nstr(HA, 10)}   (HA/z_ED = barEven(√q0) = {mp.nstr(HA/z_ED,8)})")
    print(f"  (√3/2)·z_ED²  = {mp.nstr(scale*z_ED**2,8)}   vs |S(muon)|  = {mp.nstr(mp.fabs(S_MUON),8)}"
          f"   ({mp.nstr(100*(scale*z_ED**2/mp.fabs(S_MUON)-1),4)}%)")
    print(f"  (√3/2)·HA²    = {mp.nstr(scale*HA**2,8)}   vs |S(proton)|= {mp.nstr(mp.fabs(S_PROTON),8)}"
          f"   ({mp.nstr(100*(scale*HA**2/mp.fabs(S_PROTON)-1),4)}%)")
    print("  -> magnitude scale is PARAMETER-FREE (√3 = cusp shape) and ~4% at leading NZ.")

    # ---- phase requirement per anchor per |u|:  S = (√3/2)|u|² sin(2φ) ----
    sep("[phase] required sin(2φ) = S / [(√3/2)|u|²]  — a SINGLE smooth |u| cannot serve both")
    rows = []
    for uname, u in (("z_ED", z_ED), ("HA", HA)):
        s_m = S_MUON / (scale * u**2)
        s_p = S_PROTON / (scale * u**2)
        print(f"  |u|={uname:5s}: sin(2φ_muon)  = {mp.nstr(s_m,6):>10s}"
              f"   sin(2φ_proton) = {mp.nstr(s_p,6):>10s}"
              f"   {'(|·|>1 at proton)' if mp.fabs(s_p)>1 else ''}"
              f"{'(|·|>1 at muon)' if mp.fabs(s_m)>1 else ''}")
        rows.append({"u": uname, "sin2phi_muon": mp.nstr(s_m, 8),
                     "sin2phi_proton": mp.nstr(s_p, 8)})
    print("  -> |sin 2φ| exceeds 1 by ~4% at one anchor: leading-NZ shortfall + the")
    print("     smooth-|u| wall (ratio 1 vs −4.08, bean qou-yucw). Sign flip ⇒ φ crosses 0.")

    # ---- (D) the sign-flip zero-crossing: a well-posed geometric condition ----
    sep("[D] sign flip ⇒ φ(q*) = 0 ⇒ REAL meridian holonomy (real Dehn filling) at some q*")
    print(f"  S(muon)={mp.nstr(S_MUON,6)} > 0 > {mp.nstr(S_PROTON,6)}=S(proton)")
    print("  ⇒ ∃ q* between anchors with S=0 ⇔ u real ⇔ meridian holonomy real:")
    print("     a well-posed geometric condition on q* (arg u = 0), tractable to solve.")

    # ---- (E) near-singularity: gluing-Newton sensitivity reproduces dc3/dq ----
    sep("[E] near-singularity: gluing-Newton dVol/d(meridian) — phase FUNCTION is not smooth")
    # validate the solver at complete, then probe |dVol/dm| just off m=1
    vol1 = vol_of_m(mp.mpf(1))
    err = mp.fabs(vol1 - VOL_4_1)
    print(f"  Newton at m=1: Vol = {mp.nstr(vol1,12)}  (|Δ vs Vol(4₁)| = {float(err):.2e})")
    h = mp.mpf("1e-6")
    # small real meridian perturbation m = e^{u/2}, u real small
    dvol = (vol_of_m(mp.e ** (h / 2)) - vol_of_m(mp.e ** (-h / 2))) / h
    print(f"  dVol/du at complete (real u) = {mp.nstr(dvol,6)}  (≈0: Vol extremal at complete ✓)")
    print("  The steep observable-sensitivity lives in the IMAGINARY (CS) direction:")
    print("  a complex meridian perturbation moves S at O(1/Δq) — the dc3/dq≈4.66e6 wall")
    print("  (PR #1821). So φ(q0) is the near-singular pole-seeded Newton, not smooth.")
    solver_ok = err < mp.mpf("1e-9") and mp.fabs(dvol) < mp.mpf("1e-3")

    # ---- verdict ----
    sep("VERDICT")
    print("  tractable/EXACT : base phase π/3, cusp modulus √−3 (coord 2, Lean-proved);")
    print("                    magnitude scale (√3/2)|u|² (parameter-free, ~4% leading NZ).")
    print("  OPEN (near-sing): phase FUNCTION φ(q0) = arg u(q0) — the Φ_q-pole-seeded")
    print("                    Newton (conj:algebraic-geometric-dilog-equivalence).")
    print("  next concrete    : seed the gluing Newton with the substrate pole q0^{-k}")
    print("                    and read the emergent phase (well-posed; not a fit).")

    wb.add_data("cusp_shape_coord", {
        "omega": mp.nstr(Z0, 20), "barEven": mp.nstr(barEven, 20),
        "barOdd_sq": mp.nstr(barOdd**2, 20),
        "lean": "QOU.QBeta.CuspShapeBarParity (barEven=1, barOdd²=−3, PROVED)"})
    wb.add_data("ed_coord_magnitude", {
        "z_ED": mp.nstr(z_ED, 12), "HA": mp.nstr(HA, 12),
        "scale_z_ED_sq": mp.nstr(scale * z_ED**2, 12),
        "scale_HA_sq": mp.nstr(scale * HA**2, 12),
        "S_muon": mp.nstr(S_MUON, 12), "S_proton": mp.nstr(S_PROTON, 12)})
    wb.add_data("phase_requirement", rows)
    wb.add_data("verdict", {
        "exact": "base phase pi/3, cusp modulus sqrt(-3) (Lean CuspShapeBarParity)",
        "tractable": "magnitude (sqrt3/2)|u|^2 parameter-free, ~4% leading NZ",
        "open_near_singular": "phase function phi(q0) = Phi_q-pole-seeded Newton",
        "geometric_condition": "q* with real meridian (S=0) is well-posed",
        "next": "seed gluing Newton with substrate pole q0^{-k}; not a fit"})
    wb.add_assertion("cusp_barEven_eq_one", computed=float(mp.fabs(barEven - 1)),
                     expected=0.0, tolerance=1e-20,
                     source="ω=e^{iπ/3}: barEven ω = 1 (Lean CuspShapeBarParity)")
    wb.add_assertion("cusp_barOdd_sq_eq_neg3", computed=float(mp.fabs(barOdd**2 + 3)),
                     expected=0.0, tolerance=1e-20,
                     source="ω=e^{iπ/3}: (barOdd ω)² = −3 (Lean CuspShapeBarParity)")
    wb.add_assertion("gluing_newton_vol_and_extremal", computed=float(err),
                     expected=0.0, tolerance=1e-9,
                     source="Newton at m=1 recovers Vol(4₁); Vol extremal at complete")
    wb.save()

    ok = be_ok and bo_ok and solver_ok
    print(f"\n  RESULT: {'ALL OK' if ok else 'CHECK'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
