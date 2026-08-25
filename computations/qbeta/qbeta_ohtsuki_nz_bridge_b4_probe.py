#!/usr/bin/env python3
"""qbeta_ohtsuki_nz_bridge_b4_probe.py — E1: the order-b⁴ second equation.

Companion to QOU/QBeta/OhtsukiNZBridgeScale.lean (PR #5081). The order-b²
match locks κ_A²·|c²|² = (2πκ₁)² but cannot decide the A-binary (one
equation, one composite unknown). This probe derives the SECOND equation:
matching order b⁴ between

  Ohtsuki tower : 𝔙_b = 𝔙₀ + κ₁(2πb²) + κ₂(2πb²)² + …   (κ_n real, exact:
                  κ₁ = 11√3π/108, κ₂ = 2π²/27)
  NZ geometry   : 𝔙(u) = 𝔙₀ + a₂u² + a₄u⁴ + …            (a₂ = i√3/4 proved)

under the linear bridge u = c·b of the Lean lock. Substituting the order-b²
solution c² = −i·2πκ₁/κ_A and 2πb² = i·t gives u² = (κ₁/κ_A)·t (real), so
the b⁴ terms match iff

  a₄ · (κ₁/κ_A)² = −κ₂        ⇔        a₄ = −κ₂·κ_A²/κ₁²   (and a₄ REAL).

E3 gate (built in): NZ evenness (no u³ rung, `NeumannZagierParity`) and the
integer Ohtsuki rungs make the b⁴ match well-posed; the reality requirement
on a₄ is itself a falsifiable prediction of the linear bridge.

WHAT IS COMPUTED (derived, no fit, scope-(a)):
  [1] The geometric a₂ and a₄ of the 4₁ complex volume 𝔙(u) = Vol + i·CS at
      meridian u, from the VALIDATED gluing Newton solver
      (`qbeta_c3_barodd_gluing_newton_solve`), by 3-point Richardson
      extraction at dps 60 with an h-ladder stability check. The a₂
      extraction is validated against the PROVED i·√3/4 before a₄ is read.
  [2] The two bridge predictions a₄ = −κ₂·κ_A²/κ₁² for κ_A ∈ {κ_pot = √3/4,
      κ_shape = √3/2} (exact rungs; the 𝔙-normalized vs Φ-normalized tower).
  [3] Verdict data: which (if either) prediction the geometric a₄ matches,
      and whether Im(a₄) ≈ 0 as the bridge requires. Outcomes:
      match κ_pot → linear bridge consistent, scale pinned, tower is
      𝔙-normalized; match κ_shape → Φ-normalized; neither / Im(a₄) ≠ 0 →
      the LINEAR bridge is refuted at order b⁴ (scope-(a)) — also decisive.

Nothing is wired; the verdict is reported, not asserted (research probe).
Beans: qou-vfn2 (E1) / qou-yh67. Lean lock: OhtsukiNZBridgeScale.lean.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
_probes = str(Path(__file__).resolve().parent.parent / "probes")
sys.path.insert(0, _probes)
import sdeformed_channel_signflip_probe as t2  # noqa: E402  # V41_integrated (NZ longitude integral)

set_compute_dps()  # mp.mp.dps = COMPUTE_DPS (70)

PISQ6 = mp.pi ** 2 / 6
KAPPA1 = 11 * mp.sqrt(3) * mp.pi / 108
KAPPA2 = 2 * mp.pi ** 2 / 27
KAPPA_POT = mp.sqrt(3) / 4
KAPPA_SHAPE = mp.sqrt(3) / 2
A2_PROVED = mp.mpc(0, 1) * mp.sqrt(3) / 4   # i·√3/4 (imV₄₁, FigureEightComplexVolume)


def V_of_u(u):
    """Deformed complex volume 𝔙(u) via the T2 probe's validated NZ longitude
    integral 𝔙(u) = Vol(4₁) − ½∫₀ᵘ v (the raw Rogers sum is STATIONARY at the
    complete structure — Schläfli — so the u² term lives in this boundary
    term; the first version of this probe learned that from its own a₂
    validation gate)."""
    if u == 0:
        return t2.V41_integrated(mp.mpf("1e-30"))
    return t2.V41_integrated(u)


def extract_a2_a4(h):
    """3-point Richardson: solve for (a2, a4) from V(h), V(2h), V(3h),
    eliminating a6. Even series: V(kh)−V0 = a2(kh)² + a4(kh)⁴ + a6(kh)⁶."""
    V0 = V_of_u(mp.mpf(0))
    d = [V_of_u(k * h) - V0 for k in (1, 2, 3)]
    # rows: k², k⁴, k⁶ for k=1,2,3 (in units of h powers)
    M = mp.matrix([[1, 1, 1], [4, 16, 64], [9, 81, 729]])
    rhs = mp.matrix([d[0], d[1], d[2]])
    sol = mp.lu_solve(M, rhs)     # (a2 h², a4 h⁴, a6 h⁶)
    return sol[0] / h ** 2, sol[1] / h ** 4


def main() -> int:
    print("=" * 78)
    print(" E1 — the order-b⁴ second equation: geometric a₄ vs the bridge predictions")
    print("=" * 78)

    wb = WitnessBuilder("qbeta-ohtsuki-nz-bridge-b4", engine="mpmath")
    wb.set_description(
        "E1 second equation for the OhtsukiNZBridgeScale lock (PR #5081): "
        "geometric a4 of the 4_1 complex volume V(u) (validated gluing "
        "Newton + Rogers dilog, 3-point Richardson, h-ladder stability, a2 "
        "validated against the proved i*sqrt(3)/4) vs the linear-bridge "
        "predictions a4 = -kappa2*kappaA^2/kappa1^2 for kappaA in "
        "{sqrt(3)/4, sqrt(3)/2} (exact Ohtsuki rungs kappa1 = 11*sqrt(3)*pi/108, "
        "kappa2 = 2*pi^2/27). The bridge also REQUIRES Im(a4) = 0. Verdict "
        "reported not asserted; nothing wired; no fit (all quantities derived "
        "or exact). Scope-(a). Beans qou-vfn2 / qou-yh67."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    # [1] extraction with h-ladder stability
    print("\n[1] geometric a₂, a₄ (3-point Richardson, h-ladder):")
    rows = []
    for hexp in (3, 4):
        h = mp.mpf(10) ** (-hexp)
        a2, a4 = extract_a2_a4(h)
        rows.append({"h": mp.nstr(h, 3), "a2": mp.nstr(a2, 15), "a4": mp.nstr(a4, 12)})
        print(f"    h=1e-{hexp}:  a₂ = {mp.nstr(a2, 12)}   a₄ = {mp.nstr(a4, 10)}")
    a2f, a4f = extract_a2_a4(mp.mpf(10) ** (-4))
    a2_err = mp.fabs(a2f - A2_PROVED)
    print(f"    a₂ vs proved i·√3/4: |Δ| = {float(a2_err):.2e}")

    # [2] bridge predictions
    pred_pot = -KAPPA2 * KAPPA_POT ** 2 / KAPPA1 ** 2
    pred_shape = -KAPPA2 * KAPPA_SHAPE ** 2 / KAPPA1 ** 2
    print(f"\n[2] bridge predictions: a₄(κ_pot) = {mp.nstr(pred_pot, 10)}")
    print(f"                        a₄(κ_shape) = {mp.nstr(pred_shape, 10)}")

    # [3] verdict data
    re_a4, im_a4 = mp.re(a4f), mp.im(a4f)
    rel = lambda p: float(mp.fabs(re_a4 - p) / mp.fabs(p))
    rel_pot, rel_shape = rel(pred_pot), rel(pred_shape)
    im_ratio = float(mp.fabs(im_a4) / mp.fabs(a4f)) if mp.fabs(a4f) > 0 else 0.0
    print(f"\n[3] geometric a₄ = {mp.nstr(a4f, 12)}")
    print(f"    Re(a₄) vs κ_pot pred: rel {rel_pot:.4f}   vs κ_shape pred: rel {rel_shape:.4f}")
    print(f"    |Im(a₄)|/|a₄| = {im_ratio:.4f}   (bridge requires ≈ 0)")
    if im_ratio > 0.05:
        verdict = ("LINEAR BRIDGE REFUTED at order b4 (scope-(a)): a4 is not real "
                   "as the bridge requires")
    elif rel_pot < 0.05:
        verdict = "MATCH kappa_pot: bridge consistent; tower V-normalized; scale pinned"
    elif rel_shape < 0.05:
        verdict = "MATCH kappa_shape: bridge consistent; tower Phi-normalized; scale pinned"
    else:
        verdict = ("NO MATCH at order b4: linear bridge refuted as-is (scope-(a)) "
                   "or the tower normalization differs from both candidates")
    print(f"\n    VERDICT: {verdict}")

    wb.add_data("extraction", rows)
    wb.add_data("a2_validation", {"a2_extracted": mp.nstr(a2f, 20),
                                  "a2_proved": "i*sqrt(3)/4",
                                  "abs_err": mp.nstr(a2_err, 6)})
    wb.add_data("geometric_a4", {"a4": mp.nstr(a4f, 20),
                                 "re": mp.nstr(re_a4, 20), "im": mp.nstr(im_a4, 20)})
    wb.add_data("bridge_predictions", {"kappa_pot": mp.nstr(pred_pot, 20),
                                       "kappa_shape": mp.nstr(pred_shape, 20)})
    wb.add_data("verdict", {"text": verdict, "rel_pot": mp.nstr(mp.mpf(rel_pot), 6),
                            "rel_shape": mp.nstr(mp.mpf(rel_shape), 6),
                            "im_ratio": mp.nstr(mp.mpf(im_ratio), 6)})
    wb.add_assertion("a2_matches_proved",
                     computed=mp.nstr(a2_err, 10), expected="0", tolerance="1e-8",
                     source="Richardson a2 vs proved i*sqrt(3)/4 (method validation)")
    # AGENTS.md §"q0 anchor convention" rule 4: say which pin you used. This
    # probe uses NONE. Every input is a pure constant (pi, sqrt(3), the exact
    # Ohtsuki rungs kappa1 = 11*sqrt(3)*pi/108 and kappa2 = 2*pi^2/27) or the
    # 4_1 hyperbolic geometry read off t2.V41_integrated — the NZ longitude
    # integral, a property of the knot complement, not of the substrate. The
    # single non-trivial import, computations/probes/
    # sdeformed_channel_signflip_probe.py, imports only json, subprocess,
    # datetime, pathlib and mpmath: no q_parameter, no constants.Q, and no
    # wedderburn_jones_markov.y_lambda_at, so the muon-cache straddle that
    # AGENTS.md warns about is not reachable from here.
    #
    # So the honest record is `independent`, not the standing proton default:
    # stamping a pin the compute never read is the misrecord this field exists
    # to prevent. Via save(extra=...) and NOT add_data(), which nests under
    # `data` where the audit reading body["q0Anchor"] cannot see it. No
    # q0Value — there is no value, and one here is a Q0_FLIP.
    wb.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Taylor coefficients in a FREE parameter u against proved "
            "constants: pi, sqrt(3), the exact Ohtsuki rungs "
            "k1 = 11*sqrt(3)*pi/108 and k2 = 2*pi^2/27, and 4_1 geometry via "
            "t2.V41_integrated. No substrate value is read. The one "
            "non-trivial import, probes/sdeformed_channel_signflip_probe.py, "
            "imports only json/subprocess/datetime/pathlib/mpmath, so "
            "wedderburn_jones_markov.y_lambda_at — and its muon-cache "
            "straddle — is unreachable from here."
        ),
    })

    ok = a2_err < mp.mpf("1e-8")
    print(f"\n  RESULT: {'method validated; verdict recorded' if ok else 'a2 VALIDATION FAILED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
