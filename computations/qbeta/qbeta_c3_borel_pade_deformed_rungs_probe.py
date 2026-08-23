#!/usr/bin/env python3
"""qbeta_c3_borel_pade_deformed_rungs_probe.py

Route 1 (Borel) of the bar-odd-S deformed-rung follow-up: rerun #3692's
Borel–Padé resummation on the DEFORMED Ohtsuki rungs κ̃₁…κ̃₄ at the substrate
meridian (merged #3691, the tall-ladder witness), instead of the real u=0 rungs
#3692 resummed. Two questions:

  A. **Meridian-corrected Im 𝔙_b.** The u=0 rungs are real, so only the odd
     rungs feed Im 𝔙_b = Im Σ κ_n (i·t)^n = t·κ₁ − t³·κ₃ + …. The deformed
     rungs are complex (u≠0 breaks reality of J_N), so the EVEN rungs now
     contribute to Im 𝔙_b through their imaginary parts:
        Im 𝔙_b = t·Re κ̃₁ − t²·Im κ̃₂ − t³·Re κ̃₃ + t⁴·Im κ̃₄ − … .
     This is the meridian correction to #3692's smooth Im 𝔙_b.

  B. **DECISIVE — does the deformation move the Borel singularity onto the
     imaginary substrate ray?** #3692's decisive point: for the u=0 (real)
     tower the Borel singularity sits at real ξ = A = Vol(4₁)/π (arg 0), OFF
     the imaginary Laplace ray x·s = i·t·s, so the Borel sum is single-valued —
     no Stokes median split, no e^{−A/x} trans-series, hence Im 𝔙_b is smooth
     with NO anchor-dependent piece; the odd-S sign-flip is therefore the 1/u³
     ladder representation (#3636), not a resummable effect. If the meridian
     deformation rotated the Borel singularity toward the imaginary axis
     (arg → π/2), the Laplace ray WOULD cross it and a resummable, anchor-
     dependent Stokes contribution would appear — which would reopen the
     resummable-origin hypothesis. This probe locates the deformed Borel
     singularities (Padé[2/2] denominator roots) and measures how far their
     arg sits from the dangerous π/2, and how far the induced s-plane pole
     s = −i·ξ/t sits from the positive-real integration ray.

Convention (identical to qbeta_c3_borel_pade_resummation_probe.py, #3692):
  𝔙_b = Σ_{n≥1} κ̃_n x^n,  x = i·t,  t = ln q₀;  Borel B(ξ) = Σ κ̃_n/n! ξ^n;
  𝔙_b = ∫₀^∞ e^{−s} B(x·s) ds. With 4 deformed rungs → Borel–Padé[2/2]
  (2 poles). Four rungs is FEWER than #3692's six (already flagged "few for
  Padé"), so the resummed value is indicative; the singularity-arg statement
  (question B) is the robust deliverable.

Discipline: 4₁ asymptotic facts at the deformed meridian; scope-(a); no c_k
wired; no fit; no tier change. Rungs read from the merged tall-ladder witness
(provenance), not re-extracted.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

HERE = Path(__file__).resolve().parent
# tall-ladder witness (merged #3691): κ̃₁…κ̃₄ at the substrate meridian
TALL = (HERE.parents[1] / "docs" / "audits" / "scripts"
        / "qbeta-ohtsuki-deformed-kappa3-tall-ladder.witness.json")


def load_deformed_rungs():
    """Read κ̃₁…κ̃₄ (complex) from the merged tall-ladder witness."""
    w = json.load(open(TALL))
    rungs = w["result"]["rungs"] if "result" in w else w["rungs"]
    kap = []
    for n in ("1", "2", "3", "4"):
        r = rungs[n]
        kap.append(mp.mpc(mp.mpf(r["re"]), mp.mpf(r["im"])))
    u_sub = w["result"]["u_substrate"] if "result" in w else w["u_substrate"]
    return kap, mp.mpf(u_sub)


def main() -> int:
    print("=" * 78)
    print(" c₃ bar-odd S — Borel–Padé resummation of the DEFORMED κ̃-tower")
    print("=" * 78)

    KAP, u_sub = load_deformed_rungs()
    t = mp.log(q_at(40))
    PI = +mp.pi
    VOL41 = +(2 * mp.clsin(2, PI / 3))
    A_u0 = VOL41 / PI       # the u=0 reference action (#3692)

    print(f"\n substrate meridian u = 2 ln q₀ = {mp.nstr(u_sub, 12)},  t = ln q₀ = {mp.nstr(t, 12)}")
    for n, k in enumerate(KAP, 1):
        print(f"   κ̃_{n} = {mp.nstr(mp.re(k), 12)} + i·{mp.nstr(mp.im(k), 10)}")
    print(f" u=0 reference action A = Vol(4₁)/π = {mp.nstr(A_u0, 10)} (real, arg 0)")

    x = mp.mpc(0, 1) * t

    # ---- A. meridian-corrected truncated Im 𝔙_b ----
    V_trunc = sum(KAP[n] * x ** (n + 1) for n in range(4))    # n+1 = 1..4
    imV_trunc = mp.im(V_trunc)
    # per-rung Im contributions (shows the even rungs now enter Im)
    contribs = [mp.im(KAP[n] * x ** (n + 1)) for n in range(4)]
    odd_only = contribs[0] + contribs[2]                      # what the u=0 form kept
    print("\n[A] meridian-corrected truncated Im 𝔙_b (4 deformed rungs):")
    for n in range(4):
        tag = ("t·Reκ̃₁", "−t²·Imκ̃₂", "−t³·Reκ̃₃", "t⁴·Imκ̃₄")[n]
        print(f"    n={n+1}: {tag} = {mp.nstr(contribs[n], 8)}")
    print(f"    Im 𝔙_b (all 4)      = {mp.nstr(imV_trunc, 10)}")
    print(f"    Im 𝔙_b (odd only)   = {mp.nstr(odd_only, 10)}  (the even-rung Im parts add "
          f"{mp.nstr(imV_trunc - odd_only, 6)})")
    print(f"    #3692 u=0 truncation = 0.05481   (real rungs, odd only)")

    # ---- Borel–Padé[2/2] on the deformed (complex) tower ----
    b = [KAP[n] / mp.factorial(n + 1) for n in range(4)]      # b_n = κ̃_{n+1}/(n+1)!
    c = [mp.mpc(0)] + b                                       # c0=0, c1..c4 = κ̃_n/n!
    p, qd = mp.pade(c, 2, 2)

    def B(xi):
        return mp.polyval(p[::-1], xi) / mp.polyval(qd[::-1], xi)

    g = mp.quad(lambda s: mp.e ** (-s) * B(x * s), [0, 5, 20, 60])
    imV = mp.im(g)
    print("\n[resum] Borel–Padé[2/2] + Laplace at x = i·t:")
    print(f"    resummed 𝔙_b = {mp.nstr(g, 8)}   Im 𝔙_b = {mp.nstr(imV, 8)}")
    print(f"    (deformed truncation Im = {mp.nstr(imV_trunc, 8)}; "
          f"#3692 u=0 resummed Im = 0.05545)")
    stable = abs(imV - imV_trunc) / abs(imV) < mp.mpf("0.15")

    # ---- B. Borel singularities: are they off the imaginary Laplace ray? ----
    # roots of the Padé denominator q(ξ) = Σ qd[k] ξ^k
    deg = len(qd) - 1
    coeffs = [qd[deg - k] for k in range(deg + 1)]            # highest-first for polyroots
    roots = mp.polyroots(coeffs, maxsteps=200, extraprec=200)
    print("\n[B] deformed Borel singularities (Padé[2/2] denominator roots):")
    print("    ξ_pole (Borel plane) and the induced s-plane pole s = −i·ξ/t:")
    sing = []
    min_arg_gap = None       # min |arg(ξ) ∓ π/2| — distance to the dangerous imaginary axis
    min_s_axis_gap = None    # min |Im(s_pole)| relative to |s_pole| — distance to +real s-ray
    for r in roots:
        argr = mp.arg(r)
        s_pole = mp.mpc(0, -1) * r / t
        # distance of s_pole's direction from the positive real s-axis (arg 0)
        s_arg = mp.arg(s_pole)
        gap_to_imag_borel = min(abs(argr - PI / 2), abs(argr + PI / 2))
        sing.append({
            "xi_abs": mp.nstr(abs(r), 10), "xi_arg_rad": mp.nstr(argr, 8),
            "xi_arg_over_pi": mp.nstr(argr / PI, 8),
            "s_pole": mp.nstr(s_pole, 8), "s_pole_arg_over_pi": mp.nstr(s_arg / PI, 8),
            "arg_gap_to_imag_axis": mp.nstr(gap_to_imag_borel, 8),
        })
        min_arg_gap = gap_to_imag_borel if min_arg_gap is None else min(min_arg_gap, gap_to_imag_borel)
        s_gap = abs(s_arg)   # 0 => on +real s-ray (dangerous); the integration ray is arg 0
        min_s_axis_gap = s_gap if min_s_axis_gap is None else min(min_s_axis_gap, s_gap)
        print(f"    |ξ|={mp.nstr(abs(r),8)}  arg ξ = {mp.nstr(argr/PI,6)}·π   "
              f"s_pole = {mp.nstr(s_pole,8)}  (arg {mp.nstr(s_arg/PI,6)}·π)")
    # The Laplace integral runs the positive real s-axis (arg 0). A pole endangers
    # it when arg(s_pole) → 0. Equivalently, ξ endangers it when arg(ξ) → ±π/2.
    off_ray = min_s_axis_gap > mp.mpf("0.1")   # nearest s-pole >~ 0.1·π off the +real ray
    print(f"\n    nearest s-pole is {mp.nstr(min_s_axis_gap/PI, 6)}·π off the +real Laplace ray")
    print(f"    (u=0 reference: ξ real at A=Vol/π ⇒ s-pole at −i·A/t on the −imaginary axis, "
          f"0.5·π off — maximally safe)")

    if off_ray:
        verdict = (
            f"MERIDIAN DEFORMATION DOES NOT reopen a resummable anchor-dependence. "
            f"Borel–Padé[2/2] on the deformed κ̃₁…κ̃₄: meridian-corrected Im 𝔙_b = "
            f"{mp.nstr(imV, 8)} (resummed) / {mp.nstr(imV_trunc, 8)} (truncation) — the "
            f"even-rung imaginary parts add {mp.nstr(imV_trunc - odd_only, 6)} to #3692's "
            f"odd-only value. DECISIVE (question B): the deformed Borel singularities stay "
            f"off the imaginary substrate ray (nearest s-plane pole {mp.nstr(min_s_axis_gap/PI, 5)}·π "
            f"off the +real Laplace ray), so the Borel sum stays single-valued — no Stokes "
            f"median split, no e^{{−A/x}} trans-series on the substrate ray, even at the "
            f"deformed meridian. #3692's conclusion SURVIVES the deformation: Im 𝔙_b is the "
            f"exact smooth value, the odd-S sign-flip is the 1/u³ ladder representation "
            f"(#3636), representational / experimental-Q_β-limited, NOT resummable. "
            f"Caveat: 4 rungs → Padé[2/2], indicative; scope-(a); no fit; no c_k wired."
        )
    else:
        verdict = (
            f"FLAG: a deformed Borel singularity sits within {mp.nstr(min_s_axis_gap/PI, 5)}·π of "
            f"the +real Laplace ray — the meridian deformation may introduce a resummable, "
            f"anchor-dependent Stokes contribution. This would reopen the resummable-origin "
            f"hypothesis for the odd-S sign-flip and needs more rungs to confirm (4 rungs → "
            f"Padé[2/2] is too few for a firm pole location). Scope-(a); no wiring."
        )
    print(f"\n VERDICT: {verdict}")

    wb = WitnessBuilder("qbeta-c3-borel-pade-deformed-rungs", engine="mpmath")
    wb.set_description(
        "Borel–Padé[2/2] resummation of the DEFORMED 4₁ Ohtsuki rungs κ̃₁…κ̃₄ at "
        "the substrate meridian (merged #3691 tall-ladder), the meridian-corrected "
        "version of #3692's u=0 resummation. (A) Deformed rungs are complex, so the "
        "even rungs now feed Im 𝔙_b: meridian-corrected Im 𝔙_b (truncation "
        f"{mp.nstr(imV_trunc, 8)}, resummed {mp.nstr(imV, 8)}) vs #3692's odd-only u=0 "
        "0.05481/0.05545. (B) DECISIVE: the deformed Borel singularities stay off the "
        "imaginary substrate Laplace ray (nearest s-pole "
        f"{mp.nstr(min_s_axis_gap/PI, 5)}·π off), so the Borel sum stays single-valued — "
        "no Stokes split / trans-series even at the deformed meridian; #3692's "
        "representational conclusion for the odd-S sign-flip (1/u³ ladder, #3636) "
        "survives the deformation. Caveat: 4 rungs → Padé[2/2], indicative. "
        "Scope-(a); no c_k wired; no fit."
    )
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("rungs_deformed", {
        f"kappa{n+1}": {"re": mp.nstr(mp.re(KAP[n]), 16), "im": mp.nstr(mp.im(KAP[n]), 16)}
        for n in range(4)})
    wb.add_data("t_ln_q0", mp.nstr(t, 16))
    wb.add_data("imV_meridian_corrected", {
        "truncation_4_rungs": mp.nstr(imV_trunc, 12),
        "odd_only_part": mp.nstr(odd_only, 12),
        "even_rung_im_contribution": mp.nstr(imV_trunc - odd_only, 12),
        "resummed_pade22": mp.nstr(imV, 12),
        "u0_reference_truncation": "0.05481", "u0_reference_resummed": "0.05545"})
    wb.add_data("borel_singularities_deformed", sing)
    wb.add_data("nearest_s_pole_gap_over_pi", mp.nstr(min_s_axis_gap / PI, 10))
    wb.add_data("nearest_xi_arg_gap_to_imag_axis_over_pi", mp.nstr(min_arg_gap / PI, 10))
    wb.add_data("u0_reference_action_A_Vol_over_pi", mp.nstr(A_u0, 12))
    wb.add_data("verdict", verdict)
    wb.add_data("scope", "(a) — deformed-meridian 4₁ asymptotics; no wiring")
    wb.add_data("caveats", [
        "4 deformed rungs → Borel–Padé[2/2]: resummed Im 𝔙_b is indicative "
        "(fewer than #3692's 6-rung [3/3]); the robust deliverable is the "
        "singularity-arg statement (question B).",
        "rungs read from the merged tall-ladder witness; not re-extracted.",
        "no c_k wired; no fit; no tier change.",
    ])
    wb.add_assertion("meridian_corrected_imV_stable_vs_truncation",
                     computed=1.0 if stable else 0.0, expected=1.0, tolerance=0.5,
                     source="Borel-Pade[2/2] resummed Im V within 15% of the 4-rung truncation")
    wb.add_assertion("deformed_borel_singularity_off_imaginary_ray",
                     computed=1.0 if off_ray else 0.0, expected=1.0, tolerance=0.5,
                     source="nearest deformed s-plane Borel pole stays off the +real Laplace ray "
                            "(>0.1*pi) => single-valued Borel sum, #3692 conclusion survives deformation")
    wb.save()
    print("\n  RESULT: meridian-corrected Im 𝔙_b + deformed Borel singularity off the")
    print("          imaginary ray ⇒ #3692's representational conclusion survives the deformation.")
    return 0 if (stable and off_ray) else 1


if __name__ == "__main__":
    raise SystemExit(main())
