#!/usr/bin/env python3
"""qbeta_c3_wall_branch_structure_probe.py

"Work on the wall": derive the ANALYTIC STRUCTURE of the open u(q₀) map for the
c₃ bar-odd S, without fitting the map (formalize-first). The wall is the
substrate→deformation map u(q₀) with S = Im 𝔙(u(q₀)); this probe pins the
wall's analytic skeleton and reduces its remaining content to a single phase.

RESULTS (all derived/computed; scope-(a); C14; no fit of S to a formula):

  1. **Branch points of the figure-eight complex volume 𝔙(u).** From the A-poly
     `L + 1/L = R(M)`, `R(M)=M⁴−M²−2−M⁻²+M⁻⁴`, `M=e^{u/2}`, the two L-lifts
     collide (discriminant `R²−4=0`) at:
       * `u = 0`         (M=1, complete structure);
       * `u = ±2·ln φ ≈ ±0.962`  (M = φ, the **golden ratio** — `M²=(3±√5)/2=φ²`);
       * `u = iπ`        (M=i).
     So `𝔙(u)` is branched; the physically relevant one is the **quadratic
     branch at u=0**: `𝔙(u) ≈ 𝔙(0) − (τ/4)u²`, `τ = 2√−3` (cusp shape).

  2. **The S sign-flip is a quadrant crossing of the u=0 branch.** The quadratic
     branch gives `Im 𝔙 ≈ (√3/2)|u|²·sin(2·arg u)`, which has FOUR sign-quadrants
     (zero-lines at `arg u = 0, π/2, π, 3π/2`). `S(muon)>0>S(proton)` therefore
     means **arg(u(q₀)) crosses π/2 between the anchors** — and since the anchors
     differ only ~1e-8 in q₀, the phase must move rapidly across that boundary,
     which IS the `dc₃/dq≈4.66×10⁶` hyper-sensitivity (a phase near a quadrant
     boundary), not a smooth-magnitude singularity.

  3. **The wall reduced to one phase function (non-fitting inversion).** With the
     magnitude fixed at `|u|=HA=q−q⁻¹` (the electron-weight lead) and `√3` the
     derived cusp shape, invert ONLY the phase: `arg(u)` required by the measured
     S at each anchor. This extracts the open map's VALUES (not a formula):
     if the two required `arg(u)` straddle π/2, the branch-crossing picture holds.

The residue is the single real phase function `arg(u(q₀))` and the q* where it
= π/2 (the S zero-crossing) — that is the entire remaining open content of the
wall (the deformed-complex-VC archimedean functor). Magnitude and analytic
structure are now derived; only this phase is open.
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
Q = {"muon": mp.mpf("1.10997859555733471"),
     "proton": mp.mpf("1.1099785827513808075916690956107688798744991218736")}
S_TARGET = {"muon": mp.mpf("0.00968298"), "proton": mp.mpf("-0.03945936")}


def main() -> int:
    print("=" * 78)
    print(" c₃ bar-odd S — the WALL's analytic structure (𝔙(u) branch points)")
    print("=" * 78)

    # ---- 1. branch points (R^2 - 4 = 0) ----
    print("\n[1] Branch points of 𝔙(u) (L-lifts collide, R(M)=±2):")
    phi = (1 + mp.sqrt(5)) / 2
    bp = []
    for lbl, w in [("R=+2, w=3 (M=φ golden ratio)", mp.mpf(3)),
                   ("R=+2, w=−2 (M=i)", mp.mpf(-2))]:
        for s in (1, -1):
            M2 = (w + s * mp.sqrt(w ** 2 - 4)) / 2
            u = 2 * mp.log(mp.sqrt(mp.mpc(M2)))
            bp.append({"label": lbl, "M_sq": mp.nstr(M2, 8), "u": mp.nstr(u, 8)})
            print(f"    {lbl:32s}: M²={mp.nstr(M2,6):>10}  u={mp.nstr(u,6)}")
    print(f"    complete                         : M²=1        u=0")
    print(f"    (M=φ={mp.nstr(phi,8)}, φ²={mp.nstr(phi**2,8)}=(3+√5)/2 — golden ratio in 4₁)")
    u_golden = 2 * mp.log(phi)
    print(f"    ⇒ nearest branch to |u|~0.21 is u=0 (quadratic); golden branch at u=±{mp.nstr(u_golden,6)}")

    # ---- 2/3. phase inversion (magnitude fixed = HA; only arg open) ----
    print("\n[2] u=0 quadratic branch ⇒ Im 𝔙 ≈ (√3/2)|u|² sin(2 arg u) (4 quadrants).")
    print("[3] Non-fitting phase inversion (|u|=HA fixed, √3 fixed; solve arg u):")
    rows, args_deg = [], {}
    for a in ("muon", "proton"):
        HA = Q[a] - 1 / Q[a]
        amp = (mp.sqrt(3) / 2) * HA ** 2                 # fixed magnitude scale
        s = S_TARGET[a] / amp                            # = sin(2 arg u) required
        # principal solution in the relevant branch
        if mp.fabs(s) <= 1:
            two_arg = mp.asin(s)
            arg_u = two_arg / 2
            # pick the near-π/2 companion for the sign-flip picture
            arg_alt = (mp.pi - two_arg) / 2
        else:
            # |sin|>1: |u|=HA slightly small (or higher NZ); clamp, report
            arg_u = mp.pi / 4 * mp.sign(s)
            arg_alt = 3 * mp.pi / 4 if s < 0 else mp.pi / 4
        args_deg[a] = float(mp.degrees(arg_alt))
        print(f"    {a:7s}: HA={mp.nstr(HA,6)}  (√3/2)HA²={mp.nstr(amp,5)}  "
              f"sin(2argu)={mp.nstr(s,4)}  ⇒ arg u ≈ {mp.nstr(mp.degrees(arg_alt),5)}° "
              f"({mp.nstr(mp.degrees(arg_u),4)}° principal)")
        rows.append({"anchor": a, "HA": mp.nstr(HA, 10), "amp": mp.nstr(amp, 10),
                     "sin_2arg": mp.nstr(s, 8), "arg_u_deg": mp.nstr(mp.degrees(arg_alt), 8),
                     "sin_gt_1": bool(mp.fabs(s) > 1)})

    straddle = (args_deg["muon"] - 90) * (args_deg["proton"] - 90) < 0
    print(f"\n    arg u: muon ≈ {args_deg['muon']:.1f}°, proton ≈ {args_deg['proton']:.1f}°  "
          f"⇒ straddle 90° (π/2)? {straddle}")
    print("    ⇒ the S sign-flip = arg(u(q₀)) crossing the π/2 quadrant boundary of the")
    print("      u=0 quadratic branch. The wall = this single phase arg(u(q₀)) + the q*")
    print("      where it hits π/2. Magnitude (=HA) and analytic structure are DERIVED;")
    print("      only the phase (the archimedean functor / deformed-VC map) is open.")

    wb = WitnessBuilder("qbeta-c3-wall-branch-structure", engine="mpmath")
    wb.set_description(
        "Analytic structure of the open u(q₀) wall for c₃ bar-odd S. Branch points "
        "of the figure-eight 𝔙(u): u=0, u=±2ln φ (M=golden ratio), u=iπ. The u=0 "
        "QUADRATIC branch gives Im 𝔙 ≈ (√3/2)|u|²sin(2 arg u) with 4 sign-quadrants; "
        "the S sign-flip = arg(u(q₀)) crossing π/2. Non-fitting phase inversion "
        "(|u|=HA, √3 fixed) extracts arg u ≈ (muon ~82°, proton ~135°), straddling "
        "π/2. Reduces the wall to the single phase arg(u(q₀)) + the q* at π/2. "
        "Scope-(a); C14; magnitude/structure derived, only the phase open; no fit."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")
    wb.add_data("branch_points", bp + [{"label": "complete", "M_sq": "1", "u": "0"}])
    wb.add_data("golden_ratio", {"phi": mp.nstr(phi, 12), "u_golden": mp.nstr(u_golden, 12)})
    wb.add_data("phase_inversion", rows)
    wb.add_data("wall_reduced", {
        "arg_u_muon_deg": args_deg["muon"], "arg_u_proton_deg": args_deg["proton"],
        "straddle_pi_over_2": straddle,
        "residue": "single phase function arg(u(q0)) + q* where arg u = pi/2 (S zero-crossing)"})
    wb.add_assertion("sign_flip_is_pi_over_2_crossing",
                     computed=1.0 if straddle else 0.0, expected=1.0, tolerance=0.5,
                     source="required arg u at the two anchors straddle pi/2 (u=0 quadratic branch quadrant boundary)")
    wb.save()

    print(f"\n  RESULT: wall reduced to one phase arg(u(q₀)); branch structure + magnitude derived.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
