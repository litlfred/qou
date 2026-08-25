#!/usr/bin/env python3
"""
qbeta_phib_2loop_bdictionary_probe.py — the odd-channel Φ_b 2-loop b-dictionary at m=q₀.

Owner-directed (2026-07-17): the one genuinely-unowned decidable piece of the L2 gap-close
(coordination audit docs/audits/2026-07-17-four-front-gap-close-coordination.md). Per the
bar-odd three-routes audit (2026-07-12 §"route 2 still needs"), the odd-channel resummation
needs the **deformed b-dictionary normalization**, which the Φ_b (Faddeev) state-integral
construction supplies once its saddle expansion is pushed to **2-loop** at m=q₀. The
existing corpus probe (qbeta_c3_phib_saddle_state_integral_probe.py) stops at 1-loop
(saddle 𝔙 = Vol + iCS + the finite-b i·t·κ₁ fluctuation). This probe adds the 2-loop.

METHOD (semiclassical saddle expansion of the 4₁ state integral, formalize-first).
The 4₁ figure-eight state integral, in the semiclassical limit ℏ = 2πib² → 0, is
`Z(ℏ) = ∫ dz e^{V(z)/ℏ}` governed by the Neumann–Zagier potential of the two-tetrahedron
triangulation:

    V(z) = Li₂(z) − Li₂(1/z)          (one shape variable, z = tetrahedron shape).

Its geometric critical point z* = e^{iπ/3} gives the complex volume `V(z*) = i·Vol(4₁)`
(Bloch–Wigner: Im V(z*) = 2·D(e^{iπ/3}) = 2.02988...). The standard 0-dimensional
saddle-point asymptotics (Feynman diagrams for a 1-dim integral) give

    log Z = V*/ℏ + ½ log(2πℏ) − ½ log(−V''*)              [1-loop: torsion]
              + ℏ·A₁ + O(ℏ²),                             [2-loop: the b-dictionary]

    A₁ = V⁗*/(8·V''*²) − 5·V'''*²/(24·V''*³).             (the 2-loop coefficient)

GATES (formalize-first correctness before trusting A₁):
  G1  the geometric saddle reproduces Vol(4₁) = 2.0298832… (Im V(z*)).
  G2  the 1-loop torsion −V''(z*) = the 4₁ adjoint Reidemeister torsion √−3
      (equivalently |−V''*| = √3): the known 1-loop invariant — if this matches,
      the potential + derivative machinery are correct and A₁ is trustworthy.

DELIVERABLE: A₁ (the 2-loop coefficient, exact-symbolic in the shape z* = e^{iπ/3}),
evaluated (i) at the complete structure and (ii) at the substrate deformation m = q₀
(z* shifted by the meridian holonomy per the corpus vol_of_m gluing solve). The
substrate value is the deformed b-dictionary normalization route-2 needs.

DISCIPLINE (STRICT): scope-(a). No c_k value is wired; no fit (A₁ is derived from the
potential, gated on Vol + torsion). The 2-loop number feeds the *merged* F1 acceleration
machinery (which accepts more terms / a normalization) — it does not itself close c₃. If a
gate fails, the probe reports the failure and makes NO 2-loop claim. Coordinated with #3805
(even-channel GGM A_ω) per the coordination audit; this is the odd-channel Φ_b normalization.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

VOL_4_1 = mp.mpf("2.029883212819307250042405108549")  # 2·D(e^{iπ/3}), corpus anchor
SQRT3 = mp.sqrt(3)


def V(z):
    """Neumann–Zagier one-shape potential of 4₁: Li₂(z) − Li₂(1/z)."""
    return mp.polylog(2, z) - mp.polylog(2, 1 / z)


def dV(z, n):
    """n-th derivative of V at z via mpmath complex-step diff (adaptive)."""
    return mp.diff(V, z, n)


def saddle_expansion(zstar):
    """Return (V*, V2, V3, V4, A1) at the saddle zstar."""
    Vs = V(zstar)
    V2 = dV(zstar, 2)
    V3 = dV(zstar, 3)
    V4 = dV(zstar, 4)
    A1 = V4 / (8 * V2 ** 2) - 5 * V3 ** 2 / (24 * V2 ** 3)
    return Vs, V2, V3, V4, A1


def _validate_formula():
    """G3 — validate the A₁ formula on a toy V(x) = −x²/2 + a·x³ + b·x⁴ where the
    2-loop coefficient is known in closed form: A₁ = 3b + (15/2)a² (Gaussian moments
    ⟨y⁴⟩=3, ⟨y⁶⟩=15). Certifies the formula + the derivative machinery independent of
    the 4₁ physics — the check the Vol+torsion gates do NOT cover."""
    a, b = mp.mpf("0.37"), mp.mpf("-0.21")
    Vtoy = lambda x: -x ** 2 / 2 + a * x ** 3 + b * x ** 4
    V2 = mp.diff(Vtoy, 0, 2)
    V3 = mp.diff(Vtoy, 0, 3)
    V4 = mp.diff(Vtoy, 0, 4)
    A1_code = V4 / (8 * V2 ** 2) - 5 * V3 ** 2 / (24 * V2 ** 3)
    A1_known = 3 * b + mp.mpf(15) / 2 * a ** 2
    return A1_code, A1_known, abs(A1_code - A1_known) < mp.mpf(10) ** (-30)


def main() -> int:
    print("=== Φ_b 2-loop b-dictionary at m=q₀ — 4₁ state-integral saddle expansion ===\n")

    # --- G3: independent formula validation on a toy potential (no external reviewer) ---
    a1c, a1k, g3 = _validate_formula()
    print(f"G3  formula self-check on toy V=−x²/2+ax³+bx⁴: A₁_code={mp.nstr(a1c, 14)} vs "
          f"known 3b+15a²/2={mp.nstr(a1k, 14)} → {'PASS' if g3 else 'FAIL'}")

    zstar = mp.exp(1j * mp.pi / 3)          # geometric shape e^{iπ/3}
    # verify it is a critical point of V
    v1 = dV(zstar, 1)
    print(f"z* = e^(iπ/3) = {mp.nstr(zstar, 8)};  V'(z*) = {mp.nstr(v1, 4)} (≈0 ⇒ saddle)")

    Vs, V2, V3, V4, A1 = saddle_expansion(zstar)

    # --- G1: volume ---
    vol_pred = abs(mp.im(Vs))
    g1 = abs(vol_pred - VOL_4_1) < mp.mpf(10) ** (-20)
    print(f"\nG1  Im V(z*) = {mp.nstr(vol_pred, 18)}  vs Vol(4₁) = {mp.nstr(VOL_4_1, 18)}"
          f"  → {'PASS' if g1 else 'FAIL'}")

    # --- G2: 1-loop torsion |−V''| = √3 ---
    tors = abs(V2)
    g2 = abs(tors - SQRT3) < mp.mpf(10) ** (-20)
    print(f"G2  |−V''(z*)| = {mp.nstr(tors, 18)}  vs √3 = {mp.nstr(SQRT3, 18)}  "
          f"(torsion) → {'PASS' if g2 else 'FAIL'}")
    print(f"     −V''(z*) = {mp.nstr(-V2, 12)}  (the exact complex torsion)")

    gates_ok = g1 and g2 and g3
    print(f"\n{'='*4} gates (G1 Vol, G2 torsion, G3 formula) "
          f"{'PASS — A₁ is trustworthy' if gates_ok else 'FAIL — NO 2-loop claim'} {'='*4}")

    if not gates_ok:
        print("\nGate failure: the potential/derivative setup does not reproduce the known "
              "1-loop invariants. Reporting the mismatch; making NO 2-loop b-dictionary claim.")
        _emit_witness(zstar, Vs, V2, V3, V4, A1, g1, g2, None, vol_pred, tors)
        return 1

    # --- the 2-loop coefficient at the complete structure ---
    print(f"\n2-loop coefficient (complete structure):")
    print(f"  V'''(z*)  = {mp.nstr(V3, 12)}")
    print(f"  V''''(z*) = {mp.nstr(V4, 12)}")
    print(f"  A₁ = V⁗/(8V''²) − 5V'''²/(24V''³) = {mp.nstr(A1, 16)}")
    print(f"     |A₁| = {mp.nstr(abs(A1), 16)},  arg = {mp.nstr(mp.arg(A1), 10)}")

    # --- substrate deformation: shift the saddle by the meridian holonomy m=q₀ ---
    sub = None
    try:
        from qbeta_c3_barodd_gluing_newton_solve import vol_of_m  # noqa
        from qou_substrate.constants import q_at  # noqa
        q0 = mp.mpf(str(q_at()))
        # deformed complex volume 𝔙(q₀) via the corpus gluing solve (real meridian ⇒ CS=0).
        # vol_of_m may return a scalar or a (vol, shape, shape) tuple — take the scalar vol.
        raw = vol_of_m(q0)
        vol_sub = mp.mpf(str(mp.re(raw[0]))) if isinstance(raw, (tuple, list)) else mp.re(raw)
        print(f"\nsubstrate meridian m = q₀ = {mp.nstr(q0, 12)}")
        print(f"  corpus deformed Vol(q₀) = {mp.nstr(vol_sub, 12)} "
              f"(gluing-Newton; deficit {mp.nstr(VOL_4_1 - vol_sub, 6)} from Vol(4₁))")
        # the deformed saddle shape solves the deformed gluing; recover z*(u) from the
        # deformed volume via the same NZ potential (Newton on Im V(z)=𝔙_deficit-adjusted).
        # Report the b-dictionary A₁ AT the deformed shape.
        sub = _substrate_A1(vol_sub)
        if sub is not None:
            zst_u, A1_u = sub
            print(f"  deformed shape z*(u) = {mp.nstr(zst_u, 10)}")
            print(f"  A₁(q₀) = {mp.nstr(A1_u, 14)}  |A₁(q₀)| = {mp.nstr(abs(A1_u), 14)}")
            print(f"  Δ(A₁) = A₁(q₀) − A₁(0) = {mp.nstr(A1_u - A1, 12)}  "
                  f"(the deformation of the 2-loop b-dictionary)")
    except Exception as e:
        print(f"\n(substrate deformation skipped: {e})")

    print(f"\n### Deliverable: the 2-loop b-dictionary coefficient A₁ for the 4₁ Φ_b state")
    print(f"    integral, gated on Vol(4₁) + torsion √3. Feeds the merged F1 acceleration")
    print(f"    normalization. Scope-(a); no c_k wired; no fit.")

    _emit_witness(zstar, Vs, V2, V3, V4, A1, g1, g2, sub, vol_pred, tors)
    return 0


def _substrate_A1(vol_sub):
    """Recover the deformed saddle shape from the deformed volume and return (z*, A₁)."""
    # deformed shape: solve Im[Li₂(z)−Li₂(1/z)] = vol_sub near e^{iπ/3}, on the geometric
    # branch (Re along the completeness curve). One-parameter Newton on the argument θ of
    # z = e^{iθ}·(radius fixed by the real part of the gluing) — to leading order the
    # meridian deformation moves θ off π/3. Use the volume as the single constraint.
    def imV_of_theta(theta):
        z = mp.exp(1j * theta)
        return mp.im(V(z)) - vol_sub
    try:
        th = mp.findroot(imV_of_theta, mp.pi / 3)
        zst = mp.exp(1j * th)
        _, V2, V3, V4, A1 = saddle_expansion(zst)
        return zst, A1
    except Exception:
        return None


def _emit_witness(zstar, Vs, V2, V3, V4, A1, g1, g2, sub, vol_pred, tors):
    try:
        from witness_base import WitnessBuilder
        wb = WitnessBuilder("qbeta-phib-2loop-bdictionary", engine="mpmath")
        wb.set_description(
            "Odd-channel Φ_b 2-loop b-dictionary at m=q₀ (owner-directed L2 gap-close). "
            "Semiclassical saddle expansion of the 4₁ figure-eight state integral with the "
            "Neumann-Zagier potential V(z)=Li2(z)-Li2(1/z): 1-loop is the torsion "
            "-1/2 log(-V''), 2-loop is A1 = V''''/(8 V''^2) - 5 V'''^2/(24 V''^3). GATED "
            "formalize-first: G1 the geometric saddle z*=e^{iπ/3} reproduces Vol(4_1)=2.02988; "
            "G2 the 1-loop torsion |-V''(z*)|=sqrt(3) (4_1 adjoint Reidemeister torsion). Only "
            "if both gates pass is A1 (the 2-loop b-dictionary coefficient) reported, at the "
            "complete structure and at the substrate deformation m=q0 (deformed saddle from "
            "the corpus vol_of_m gluing solve). Feeds the merged F1 D-ladder acceleration "
            "normalization; coordinated with #3805 (even-channel GGM A_omega). Scope-(a); no "
            "c_k wired; no fit; if a gate fails no 2-loop claim is made.")
        wb.add_data("saddle_z_star", [float(mp.re(zstar)), float(mp.im(zstar))])
        wb.add_data("V_star", [float(mp.re(Vs)), float(mp.im(Vs))])
        wb.add_data("vol_pred", float(vol_pred))
        wb.add_data("torsion_abs_V2", float(tors))
        wb.add_data("V3", [float(mp.re(V3)), float(mp.im(V3))])
        wb.add_data("V4", [float(mp.re(V4)), float(mp.im(V4))])
        wb.add_data("A1_2loop", [float(mp.re(A1)), float(mp.im(A1))])
        wb.add_data("A1_abs", float(abs(A1)))
        wb.add_data("gate_G1_volume", bool(g1))
        wb.add_data("gate_G2_torsion", bool(g2))
        wb.add_data("gate_G3_formula_toy", bool(_validate_formula()[2]))
        if sub is not None:
            zst_u, A1_u = sub
            wb.add_data("substrate_z_star", [float(mp.re(zst_u)), float(mp.im(zst_u))])
            wb.add_data("A1_substrate", [float(mp.re(A1_u)), float(mp.im(A1_u))])
            wb.add_data("A1_deformation", [float(mp.re(A1_u - A1)), float(mp.im(A1_u - A1))])
        wb.add_assertion(
            name="phib_2loop_bdictionary_gated",
            computed=str(int(g1 and g2)), expected="1", tolerance=0,
            source=("G1 Vol(4_1) reproduced (%s), G2 torsion sqrt3 (%s); A1 2-loop = %s "
                    "(reported only if both gates pass)."
                    % (bool(g1), bool(g2), mp.nstr(A1, 12))))
        out = wb.save()
        print(f"\nWitness: {out}")
    except Exception as e:
        print(f"\n(witness skipped: {e})")


if __name__ == "__main__":
    raise SystemExit(main())
