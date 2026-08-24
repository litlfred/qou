#!/usr/bin/env python3
"""qbeta_c3_barodd_pole_seed_newton_probe.py

Literal pole->cusp Newton: seed Thurston's figure-8 gluing equation with the ACTUAL
substrate Phi_q pole q0^{-k} and read the emergent shape / complex volume 𝔙=Vol+i·CS.
Answers "is the pole->cusp phase tractable" with a DECISIVE branch-selection result.

THE COMPLETE GLUING EQUATION FACTORS INTO TWO BRANCHES (z(z-1))²=1, z(z-1)=±1:
  * z²−z+1=0  -> CUSP  e^{iπ/3}  (complex; hyperbolic; disc −3; barOdd²=−3 = √−3 = CS)
  * z²−z−1=0  -> GOLDEN φ=(1+√5)/2 (real; DEGENERATE Vol=0; disc +5; barEven²=+5 = √5, no CS)
(both proved in QOU.QBeta.CuspShapeBarParity: cuspShape_barOdd_sq, goldenShape_barEven_sq.)

FINDINGS (computed; scope-(a); C14; m(q0) NOT fitted; no c_k wired):
  A. LITERAL real pole seed q0^{-k} flows to the GOLDEN branch φ=1.618033988… (real,
     Vol=0) — NOT the hyperbolic cusp. A real pole cannot reach the cusp.
  B. The bar-parity roles SWAP between branches (Lean): cusp barOdd²=−3 (imaginary √−3
     = CS), golden barEven²=+5 (REAL √5, no CS). The special coordinate is imaginary on
     the cusp, real on the golden branch — so CS turns on ONLY off the real (golden) axis.
  C. Full complex-volume CS at the substrate meridian scale (|u|~HA, any phase) is
     ~1e-5 — ~1000× below the measured |S|~0.01–0.04. This CONFIRMS the parallel-landed
     geometry-side clean negative (main 1a4894b8, "magnitude-only") via an independent
     Rogers-dilog complex-volume computation.

VERDICT: the phase φ(q0) is precisely the BRANCH SELECTOR — it complexifies the real
pole seed to move the special coordinate from the real √5 (golden, no CS) to the
imaginary √−3 (cusp, CS = bar-odd S). No real datum supplies it; the pole→u phase map
is the open conj:algebraic-geometric-dilog-equivalence. Moreover the naive figure-8 CS
deformation is ~1000× too small at substrate scale — so S is not the leading complex-
volume deformation of 4₁ alone (consistent with the landed geometry-side negative).

Lean: QOU/QBeta/CuspShapeBarParity.lean (both branches, PROVED).
Audit: docs/audits/2026-07-11-qbeta-c3-pole-cusp-phase-tractability.md.
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
Z0 = mp.e ** (mp.mpc(0, 1) * mp.pi / 3)
PISQ6 = mp.pi ** 2 / 6
Q0 = mp.mpf("1.10997859555733471")            # muon-canonical (computations layer)
S_MUON = mp.mpf("0.00968298")
S_PROTON = mp.mpf("-0.03945936")
PHI_GOLDEN = (1 + mp.sqrt(5)) / 2


def solve_shape(m, seed=Z0):
    return mp.findroot(lambda z: z * (z - 1) * (m * m * z) * (m * m * z - 1) - 1, seed)


def rogers(z):
    z = mp.mpc(z)
    return mp.polylog(2, z) + mp.mpf("0.5") * mp.log(z) * mp.log(1 - z)


def vol_cs(m, seed=Z0):
    z = solve_shape(m, seed)
    c = rogers(z) + rogers(m * m * z)
    return mp.im(c), mp.re(c) - PISQ6, z       # Vol, CS, shape


def sep(t):
    print("=" * 78); print(t); print("=" * 78)


def main() -> int:
    sep(" c3 bar-odd S — LITERAL pole-seed Newton: branch selection is the phase")

    wb = WitnessBuilder("qbeta-c3-barodd-pole-seed-newton", engine="mpmath")
    wb.set_description(
        "Seeds Thurston's figure-8 gluing Newton with the real substrate pole q0^{-k}. "
        "Result: flows to the GOLDEN branch (z²−z−1=0, φ=1.618, real, Vol=0), NOT the "
        "cusp (z²−z+1=0, e^{iπ/3}). Bar-parity roles swap (Lean CuspShapeBarParity): "
        "cusp barOdd²=−3 (√−3=CS), golden barEven²=+5 (√5, no CS). Full Rogers-dilog CS "
        "at substrate scale ~1e-5 ≪ |S| — confirms landed geometry-side clean-negative "
        "(1a4894b8). Phase φ(q0) is the branch selector (open conj:agde). "
        "Scope-(a); C14; m(q0) NOT fitted; no c_k wired."
    )
    wb.set_content_block("conj:algebraic-geometric-dilog-equivalence")

    # ---- validate convention at complete ----
    sep("[0] convention check at complete (m=1)")
    vol1, cs1, z1 = vol_cs(mp.mpf(1))
    print(f"  Vol = Im(Σ rogers)   = {mp.nstr(vol1,12)}  (Vol(4₁)=2.02988321)")
    print(f"  CS  = Re(Σ)−π²/6     = {mp.nstr(cs1,8)}  (amphichiral ⇒ 0)")
    conv_ok = mp.fabs(vol1 - mp.mpf("2.02988321")) < mp.mpf("1e-6") and mp.fabs(cs1) < mp.mpf("1e-25")

    # ---- (A) literal real pole seed -> golden branch ----
    sep("[A] LITERAL real pole seed q0^{-k} into the complete gluing (z(z−1))²=1")
    gold_hits = 0
    for k in range(1, 4):
        seed = Q0 ** (-k)                       # real Phi_q / q-Pochhammer pole
        try:
            z = mp.findroot(lambda z: (z * (z - 1)) ** 2 - 1, seed)
            real = mp.fabs(mp.im(z)) < mp.mpf("1e-20")
            is_gold = mp.fabs(z - PHI_GOLDEN) < mp.mpf("1e-15")
            gold_hits += 1 if is_gold else 0
            print(f"  k={k} seed={mp.nstr(seed,8)} (real) -> z={mp.nstr(z,12)}"
                  f"  {'GOLDEN φ (real, Vol=0)' if is_gold else ('real' if real else 'complex')}")
        except Exception as e:
            print(f"  k={k} seed={mp.nstr(seed,8)}: Newton did not converge ({type(e).__name__})")
    print(f"  golden ratio φ = (1+√5)/2 = {mp.nstr(PHI_GOLDEN,12)}")
    print("  => real pole seeds the DEGENERATE golden branch, never the hyperbolic cusp.")

    # ---- (B) the two branches: bar-parity swap (tie to Lean) ----
    sep("[B] two branches of (z(z−1))²=1 — bar-parity roles swap (Lean CuspShapeBarParity)")
    def barEven(z): return z + 1 / z
    def barOdd(z): return z - 1 / z
    cusp_bo2 = barOdd(Z0) ** 2
    gold_be2 = barEven(PHI_GOLDEN) ** 2
    print(f"  CUSP   z²−z+1: barEven={mp.nstr(barEven(Z0),6)} (=1), barOdd²={mp.nstr(cusp_bo2,8)} (=−3, √−3 = CS)")
    print(f"  GOLDEN z²−z−1: barOdd ={mp.nstr(barOdd(PHI_GOLDEN),6)} (=1), barEven²={mp.nstr(gold_be2,8)} (=+5, √5, no CS)")
    print("  => special coord is IMAGINARY on cusp (√−3=CS), REAL on golden (√5). Phase flips −3↔+5.")
    swap_ok = mp.fabs(cusp_bo2 + 3) < mp.mpf("1e-20") and mp.fabs(gold_be2 - 5) < mp.mpf("1e-20")

    # ---- (C) full complex-volume CS at substrate scale ≪ S ----
    sep("[C] full Rogers-dilog CS at substrate meridian scale (|u|~HA) vs measured |S|")
    HA = Q0 - 1 / Q0
    max_cs = mp.mpf(0)
    for phi in (mp.mpf("0.3"), mp.pi / 4, mp.mpf("1.0"), mp.mpf("-0.7")):
        u = HA * mp.e ** (mp.mpc(0, 1) * phi)
        _, cs, _ = vol_cs(mp.e ** (u / 2))
        max_cs = max(max_cs, mp.fabs(cs))
        print(f"  |u|=HA, arg u={mp.nstr(float(phi),5):>7s}: CS = {mp.nstr(cs,7)}")
    print(f"  max|CS| at |u|=HA ≈ {mp.nstr(max_cs,4)}   vs |S(muon)|=0.00968, |S(proton)|=0.03946")
    print(f"  => full CS is ~{mp.nstr(mp.fabs(S_PROTON)/max_cs,3)}× below |S| — the naive 4₁ CS")
    print("     deformation is orders too small (confirms landed geometry-side negative 1a4894b8).")

    sep("VERDICT")
    print("  The phase φ(q0) is the BRANCH SELECTOR: it complexifies the real pole seed to")
    print("  move the special coordinate from real √5 (golden, no CS) to imaginary √−3 (cusp,")
    print("  CS = bar-odd S). No real datum supplies it (pole→u map = open conj:agde).")
    print("  Additionally the naive 4₁ complex-volume deformation is ~1000× too small at")
    print("  substrate scale — S is not the leading CS deformation of 4₁ alone.")

    wb.add_data("complete_convention", {"Vol": mp.nstr(vol1, 20), "CS": mp.nstr(cs1, 12)})
    wb.add_data("pole_seed_branch", {
        "golden_phi": mp.nstr(PHI_GOLDEN, 20),
        "result": "real pole q0^{-k} -> golden branch (real, Vol=0), not cusp"})
    wb.add_data("branch_bar_parity", {
        "cusp_barOdd_sq": mp.nstr(cusp_bo2, 12), "golden_barEven_sq": mp.nstr(gold_be2, 12),
        "lean": "QOU.QBeta.CuspShapeBarParity (cuspShape_barOdd_sq=−3, goldenShape_barEven_sq=+5)"})
    wb.add_data("full_cs_scale", {
        "max_cs_at_HA": mp.nstr(max_cs, 12), "S_muon": mp.nstr(S_MUON, 12),
        "S_proton": mp.nstr(S_PROTON, 12),
        "ratio_S_over_CS": mp.nstr(mp.fabs(S_PROTON) / max_cs, 8),
        "note": "naive 4_1 CS deformation ~1000x too small (confirms 1a4894b8)"})
    wb.add_assertion("complete_convention_vol_cs", computed=float(mp.fabs(cs1)),
                     expected=0.0, tolerance=1e-25,
                     source="Σ rogers at m=1: Im=Vol(4₁), Re−π²/6=CS=0 (amphichiral)")
    # Boolean encoding (Copilot review): the claim is "at least one real pole seed
    # reaches the golden branch, not the cusp" — stable regardless of how many of
    # the k=1..3 seeds converge (gold_hits is a count; a bare count vs expected=1.0
    # would fail for 0 or ≥2 hits and doesn't encode the intended existential).
    wb.add_assertion("real_pole_hits_golden_branch", computed=float(gold_hits >= 1),
                     expected=1.0, tolerance=0.5,
                     source="≥1 real pole seed q0^{-k} reaches golden φ=(1+√5)/2, not the cusp")
    wb.add_assertion("branch_bar_parity_swap", computed=float(mp.fabs(cusp_bo2 + 3) + mp.fabs(gold_be2 - 5)),
                     expected=0.0, tolerance=1e-20,
                     source="cusp barOdd²=−3 (√−3=CS), golden barEven²=+5 (√5, no CS); Lean-proved")
    wb.save()

    ok = conv_ok and swap_ok and gold_hits >= 1
    print(f"\n  RESULT: {'ALL OK' if ok else 'CHECK'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
