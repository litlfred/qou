#!/usr/bin/env python3
"""qbeta_g3_5two_saddle_exact_predictions.py — port of the completed 4₁
machinery to 5₂: the exact closed-form saddle data and the FALSIFIABLE
pole-position/phase targets for the 5₂ deformed ladder (#3892's lane).

Why 5₂: the 4₁ lane closed with the odd-phase NULL (merged #3930) — the
4₁ resurgent structure is fully phase-law-kinematic (amphichirality;
GGM Prop 21 is the structural reason). The bar-odd A_ω channel must
source from NON-amphichiral geometry. 5₂ is GGM's worked non-amphichiral
example: CS(5₂) ≠ 0, three saddles, complex Borel singularities.

Exact side (GGM §6.1, library/arxiv-2012.00062v3/2012.00062v3.pdf, glyph-extracted):

  * state integral (230): Z₅₂(u;τ) = ∫ Φ_b(v)Φ_b(v+u)Φ_b(v−u) e^{−2πiv²}
  * potential (231): V(u,v) = Li₂(−e^v) + Li₂(−e^{u+v}) + Li₂(−e^{−u+v}) + v²
    (EVEN in u — the chirality lives in the complex saddle VALUES)
  * saddle eq (232): 2v = log(1+e^v) + log(1+e^{u+v}) + log(1+e^{−u+v})
  * curve (233): y² = (1−y)(1−xy)(1−x⁻¹y) with (x,y) = (e^u, −e^v)
    ⇒ cleared cubic  x·y³ − (x²+1)·y² + (x²+x+1)·y − x = 0
    Self-checks: x = 1 reduces to y³ − 2y² + 3y − 1 = 0 = (73)
    ((1−y)³ = y²); its discriminant is −23 = the printed trace-field
    discriminant; the cleared cubic is x↔x⁻¹ palindromic (u-evenness).
    The algebraic layer is Lean-proved in
    content/.../QOU/QBeta/FiveTwoSaddleCurve.lean.

Deliverables (the falsifiable targets, since the corpus has no measured
5₂ deformed rungs yet):
  T1  u = 0 control: the three saddles reproduce the printed (73) roots
      and Im V(σ1) = −Vol(5₂) sign-convention datum |Im V| = 2.82812.
  T2  the three pairwise singularities ι_ij = (V_i − V_j)/(2πi) at u = 0
      — for 5₂ these include genuinely COMPLEX positions (σ3 = the real
      representation; CS ≠ 0), unlike 4₁'s real Vol/π.
  T3  deformed (u_sub = 2t): all V_σ, all ι̃_ij, and their ξ-frame pole
      predictions ι̃·2πi/ξ with the KEY numbers: the deviation of each
      predicted pole arg from the kinematic arctan(t/π). For 4₁ this
      deviation was exactly 0 (the null); for 5₂ a NONZERO deviation is
      the predicted intrinsic odd-phase carrier — the sharp target the
      #3892 ladder can falsify.

Anti-laundering: pure forward predictions from the glyph-extracted
potential; nothing compared to anchors, nothing fitted, nothing wired.
mpmath dps 50, no float64; scope-(a); no c_k wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# Vol(5_2) SnapPy census; the literal printed 17 digits, correct to 15 (qou-ckbv)
VOL52 = mp.mpf("2.82812208833078316276389880928")
PRINTED_XI1 = mp.mpc("0.78492", "1.30714")   # printed (73) root (5 digits)


def saddle_roots(x):
    """Roots of x·y³ − (x²+1)·y² + (x²+x+1)·y − x = 0."""
    return mp.polyroots([x, -(x ** 2 + 1), x ** 2 + x + 1, -x],
                        maxsteps=200, extraprec=80)


def branch_v(u, y):
    """v = log(−y) + 2πik selected by the saddle equation (232), with the
    residual reduced mod 2πi: the RHS log branches are part of the saddle
    data (GGM: V is ℂ/2π²ℤ-valued), so a residual that is an exact 2πi
    multiple means the saddle lies on a shifted log sheet — the V value
    below is then a REPRESENTATIVE of the 2π²ℤ-lattice class, and the
    σ3-pair singularity positions inherit a mod-π ambiguity in their
    imaginary part (documented in the witness; the physical sheet is
    fixed by the measurement, not by this probe)."""
    best = None
    for k in range(-3, 4):
        v = mp.log(-y) + 2 * mp.pi * mp.mpc(0, 1) * k
        resid = 2 * v - mp.log(1 + mp.e ** v) \
            - mp.log(1 + mp.e ** (u + v)) - mp.log(1 + mp.e ** (-u + v))
        n = mp.nint(mp.im(resid) / (2 * mp.pi))
        resid_mod = abs(resid - 2 * mp.pi * mp.mpc(0, 1) * n)
        # select by TRUE residual (nearest-to-principal sheet — every k is
        # ≡ 0 mod 2πi, so the mod metric cannot discriminate); the mod
        # metric is the exactness certificate reported upward.
        if best is None or abs(resid) < best[2]:
            best = (resid_mod, v, abs(resid))
    return best[1], best[0]


def V_of(u, y):
    x = mp.e ** u
    v, resid = branch_v(u, y)
    val = mp.polylog(2, y) + mp.polylog(2, x * y) + mp.polylog(2, y / x) \
        + v ** 2
    return val, resid


def order_saddles(roots):
    """σ1 = geometric (Im y > 0), σ2 = conjugate (Im y < 0), σ3 = real."""
    s1 = max(roots, key=lambda r: mp.im(r))
    s2 = min(roots, key=lambda r: mp.im(r))
    s3 = min(roots, key=lambda r: abs(mp.im(r)))
    return s1, s2, s3


def V_sigma3(u, y):
    """σ3 (real-connection) action: GGM §6.1 (below eq 237) — "for σ3, we
    only keep the real part of V": the imaginary part at the real branch
    is a log-branch artifact, not action data. ERRATUM: the first
    published version of this probe (merged #3937) used the full complex
    V₃; the σ3-pair targets now supersede those numbers."""
    val, resid = V_of(u, y)
    return mp.mpc(mp.re(val), 0), resid


def main() -> int:
    print("=" * 78)
    print(" 5₂ port — exact saddle data + falsifiable pole targets (for #3892)")
    print("=" * 78)

    t = mp.log(q_at(50))
    u_sub = 2 * t
    xi = u_sub + 2 * mp.pi * mp.mpc(0, 1)
    phi_kin = mp.atan(t / mp.pi)

    # ---- T1: u = 0 control ----
    roots0 = saddle_roots(mp.mpf(1))
    s1, s2, s3 = order_saddles(roots0)
    ok_root = abs(s1 - PRINTED_XI1) < mp.mpf("2e-5")
    V1, r1 = V_of(mp.mpf(0), s1)
    V2, r2 = V_of(mp.mpf(0), s2)
    V3, r3 = V_sigma3(mp.mpf(0), s3)
    ok_res = max(r1, r2, r3) < mp.mpf("1e-45")
    vol_meas = abs(mp.im(V1))
    ok_vol = abs(vol_meas - VOL52) / VOL52 < mp.mpf("1e-10")
    print(f"\n[T1] u=0: ξ₁ = {mp.nstr(s1, 10)} (printed {mp.nstr(PRINTED_XI1, 7)}, "
          f"ok={ok_root}); saddle residuals ≤ {mp.nstr(max(r1, r2, r3), 3)}")
    print(f"     |Im V(σ1)| = {mp.nstr(vol_meas, 15)} vs Vol(5₂) = "
          f"{mp.nstr(VOL52, 15)}  ok={ok_vol}")

    # ---- T2: u = 0 singularity positions ----
    print("\n[T2] u=0 pairwise ι_ij = (V_i−V_j)/(2πi):")
    pairs0 = {}
    for (nm, Va, Vb) in (("12", V1, V2), ("13", V1, V3), ("23", V2, V3)):
        iota = (Va - Vb) / (2 * mp.pi * mp.mpc(0, 1))
        pairs0[nm] = iota
        print(f"     ι_{nm} = {mp.nstr(iota, 12)}")
    ok_complex = abs(mp.im(pairs0["13"])) > mp.mpf("0.01")
    print(f"     ι_13 genuinely complex (CS(5₂) ≠ 0 carrier): {ok_complex}"
          f"  [4₁'s analogue was real Vol/π — the structural difference]")
    ok_volpi = abs(pairs0["12"] - VOL52 / mp.pi) < mp.mpf("1e-10")
    print(f"     control: ι_12(0) = Vol(5₂)/π = {mp.nstr(VOL52 / mp.pi, 12)}"
          f"  ok={ok_volpi}")

    # ---- T3: deformed targets at u_sub = 2t ----
    x = mp.e ** u_sub
    rootsD = saddle_roots(x)
    d1, d2, d3 = order_saddles(rootsD)
    W1, q1 = V_of(u_sub, d1)
    W2, q2 = V_of(u_sub, d2)
    W3, q3 = V_sigma3(u_sub, d3)
    ok_resD = max(q1, q2, q3) < mp.mpf("1e-45")
    print(f"\n[T3] deformed saddles at u_sub = 2t (residuals ≤ "
          f"{mp.nstr(max(q1, q2, q3), 3)}):")
    for nm, W in (("σ1", W1), ("σ2", W2), ("σ3", W3)):
        print(f"     V({nm}) = {mp.nstr(W, 18)}")
    targets = {}
    print("     ξ-frame pole predictions ι̃·2πi/ξ and their phase vs kinematic:")
    for (nm, Va, Vb) in (("12", W1, W2), ("13", W1, W3), ("23", W2, W3)):
        iota = (Va - Vb) / (2 * mp.pi * mp.mpc(0, 1))
        pole = iota * 2 * mp.pi * mp.mpc(0, 1) / xi
        dev = mp.arg(pole) - phi_kin
        targets[nm] = (iota, pole, dev)
        print(f"     ι̃_{nm} = {mp.nstr(iota, 12)} → pole {mp.nstr(pole, 10)}"
              f"  arg−kinematic = {mp.nstr(dev, 6)} rad")
    # the odd-phase carrier prediction: at least one pair with a
    # non-kinematic pole phase well above the 4₁ null floor (9.2e-9)
    max_dev = max(abs(d) for _, _, d in targets.values())
    ok_carrier = max_dev > mp.mpf("1e-3")
    print(f"     max |arg−kinematic| = {mp.nstr(max_dev, 6)} rad "
          f"(4₁ null floor was 9.2e-9)  → intrinsic-phase carrier "
          f"predicted: {ok_carrier}")

    ok = (ok_root and ok_res and ok_vol and ok_complex and ok_volpi
          and ok_resD and ok_carrier)
    verdict = (
        f"5_2 exact saddle data derived from the glyph-extracted GGM "
        f"sec-6.1 potential: cleared cubic x y^3 - (x^2+1)y^2 + "
        f"(x^2+x+1)y - x (Lean-proved algebraic layer; reduces to (73) at "
        f"x=1, trace-field discriminant -23), printed root xi_1 "
        f"reproduced ({ok_root}), |Im V(sigma1)| = Vol(5_2) to 1e-10 "
        f"({ok_vol}), saddle residuals ~1e-46. u=0 singularities include "
        f"the genuinely COMPLEX iota_13 ({ok_complex}) — the CS != 0 "
        f"structural difference from 4_1. FALSIFIABLE TARGETS for the "
        f"#3892 5_2 ladder: deformed pole predictions with max "
        f"|arg - kinematic| = {mp.nstr(max_dev, 4)} rad vs the 4_1 null "
        f"floor 9.2e-9 ({ok_carrier}) — a NONZERO intrinsic pole phase is "
        f"predicted for 5_2, exactly the odd-channel carrier the 4_1 null "
        f"excluded. Forward predictions only; nothing fitted, nothing "
        f"wired. Scope-(a); no c_k wired."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-5two-saddle-exact-predictions",
                        engine="mpmath")
    wb.set_description(
        "Port of the completed 4_1 machinery to 5_2: exact closed-form "
        "saddle data from the GGM sec-6.1 potential (curve Lean-proved) "
        "and the falsifiable deformed pole-position/phase targets for "
        "the #3892 5_2 ladder. A nonzero intrinsic pole phase is "
        "predicted — the odd-channel carrier the 4_1 null excluded.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("source", "library/arxiv-2012.00062v3/2012.00062v3.pdf (GGM) eqs 230-233 + 73/75")
    wb.add_data("curve", "x*y^3 - (x^2+1)*y^2 + (x^2+x+1)*y - x = 0 "
                         "[(232)-derived; Lean: FiveTwoSaddleCurve.lean]")
    wb.add_data("u0", {"xi1": mp.nstr(s1, 20),
                       "V_sigma1": mp.nstr(V1, 25),
                       "V_sigma3": mp.nstr(V3, 25),
                       "abs_ImV1_vs_Vol52": mp.nstr(vol_meas - VOL52, 6),
                       "iota_12": mp.nstr(pairs0["12"], 20),
                       "iota_13": mp.nstr(pairs0["13"], 20)})
    wb.add_data("deformed_targets", {
        nm: {"iota": mp.nstr(io, 20), "pole": mp.nstr(po, 20),
             "arg_minus_kinematic_rad": mp.nstr(dv, 10)}
        for nm, (io, po, dv) in targets.items()})
    wb.add_data("prediction",
                {"max_arg_dev_rad": mp.nstr(max_dev, 10),
                 "fourone_null_floor_rad": "9.2e-9",
                 "statement": "the 5_2 deformed ladder should measure a "
                              "non-kinematic Borel pole phase at this "
                              "scale; measuring ~0 falsifies the "
                              "non-amphichiral-carrier hypothesis"})
    wb.add_data("verdict", verdict)
    wb.add_assertion("u0_controls_pass",
                     computed=1.0 if (ok_root and ok_res and ok_vol
                                      and ok_volpi) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="printed (73) root + Vol(5_2) + iota_12 = "
                            "Vol/pi + saddle residuals (mod 2pi i, per "
                            "the C/2pi^2 Z-valued V) all reproduced")
    wb.add_assertion("cs_complex_singularity_present",
                     computed=1.0 if ok_complex else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="iota_13 genuinely complex at u=0 (CS != 0)")
    wb.add_assertion("nonzero_intrinsic_phase_predicted",
                     computed=1.0 if ok_carrier else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="deformed pole-phase deviation from kinematic "
                            "well above the 4_1 null floor")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
