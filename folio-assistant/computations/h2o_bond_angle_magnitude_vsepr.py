#!/usr/bin/env python3
"""
H₂O bond-angle MAGNITUDE from trace-weighted VSEPR (no fit parameter).

Content block: prop:h2o-bond-angle-shift (the b/(2a) magnitude leg).
Companion to `h2o_bond_angle_shift_phi1.py` (which fixed the SIGN of b via
the Markov trace). This probe supplies the geometric stiffness `a` — the
curvature of the tetrahedral well — explicitly, so the model returns a
predicted angle rather than only a sign.

THE MODEL (standard VSEPR points-on-a-sphere, NO free fit parameter)
--------------------------------------------------------------------
Four electron domains around O sit on a unit sphere (fixed bond length):
two bonding O–H pairs and two lone pairs, in the C₂ᵥ arrangement (H's in
the xz-plane, lone pairs in the yz-plane). Each domain i carries a
repulsion weight w_i, and the total energy is the pairwise Coulomb sum

    E(θ,φ) = Σ_{i<j} w_i w_j / d_ij     (d_ij = chord distance)

minimised over the H–O–H angle θ and the lone–lone angle φ. The ONLY
inputs are:
  • the weights, taken q-exactly from the Markov trace (NOT fitted):
        w_bond = tr_M(σ)        = z
        w_lone = tr_M(σ₀σ₁σ₀)   = h z² + z          ⇒  w_lone/w_bond = h z + 1
  • a fixed Coulomb (n = 1) kernel (the standard VSEPR choice).
There is no scale or exponent tuned to the answer.

SELF-VALIDATION
---------------
With EQUAL weights the minimiser is the exact tetrahedral angle
arccos(−1/3) = 109.47° — the model has no built-in bias.

RESULT (Tier 2 — magnitude, honest residual)
---------------------------------------------
With the trace weights (w_lone/w_bond ≈ 1.104, a 10 % lone-pair excess)
the Coulomb minimiser gives θ ≈ 107.2°: the angle NARROWS by ≈ 2.3° below
tetrahedral — the correct SIGN and the correct ORDER OF MAGNITUDE
(observed narrowing 4.97°, i.e. 104.5°). The trace fix propagates
correctly through the magnitude model — contrast the prior |Φ₁| weighting,
which OPENED the angle to ≈ 140° (+35 %). The residual (model 107.2° vs
observed 104.5°) is reported, NOT fitted away: closing it would require
either a larger effective domain asymmetry or a non-Coulomb kernel, and
tuning the kernel to hit 104.5° is exactly the magnitude-fit the
three-calibration / formalize-first discipline forbids.
"""
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parents[1]
for _p in (str(_HERE),
           str(_ROOT / "tools" / "pyhecke" / "python"),
           str(_ROOT / "tools" / "qou-substrate" / "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: F401
from pyhecke.gram import z, nf_of_word, nf_tr
from q_parameter import HA as h  # h = q − q⁻¹
from witness_base import WitnessBuilder
from experimental_constants import ANGLE_H2O_HOH_DEG, ANGLE_H2O_TETRAHEDRAL_DEG

W_BOND = float(nf_tr(nf_of_word((0,))))      # z
W_LONE = float(nf_tr(nf_of_word((0, 1, 0))))  # h z² + z


def _energy(x, wH, wL, n=1.0):
    th, ph = x
    sH, cH = np.sin(th / 2), np.cos(th / 2)
    sL, cL = np.sin(ph / 2), np.cos(ph / 2)
    dHH, dLL = 2 * sH, 2 * sL
    dHL = np.sqrt(sH ** 2 + sL ** 2 + (cH + cL) ** 2)
    if min(dHH, dLL, dHL) < 1e-6:
        return 1e9
    return wH * wH / dHH ** n + wL * wL / dLL ** n + 4 * wH * wL / dHL ** n


def _minimise(wH, wL, n=1.0):
    r = minimize(_energy, [np.radians(109.47), np.radians(109.47)],
                 args=(wH, wL, n), method="Nelder-Mead",
                 options={"xatol": 1e-7, "fatol": 1e-12})
    return float(np.degrees(r.x[0])), float(np.degrees(r.x[1]))


def main() -> None:
    print("=" * 70)
    print("H₂O BOND-ANGLE MAGNITUDE — trace-weighted VSEPR (no fit)")
    print("=" * 70)
    ratio = W_LONE / W_BOND
    print(f"  w_bond = z = {W_BOND:.6f}   w_lone = h z²+z = {W_LONE:.6f}")
    print(f"  w_lone/w_bond = {ratio:.6f}  (= h z + 1; q-exact, not fitted)")
    print()

    theta0 = ANGLE_H2O_TETRAHEDRAL_DEG
    theta_obs = ANGLE_H2O_HOH_DEG

    # self-validation: equal weights must reproduce the tetrahedral angle
    th_ctrl, _ = _minimise(W_BOND, W_BOND, n=1.0)
    print(f"  CONTROL (equal weights, n=1): θ = {th_ctrl:.3f}°  "
          f"(must be {theta0:.2f}° — self-validation)")

    # trace-weighted prediction at several kernels (n=1 Coulomb is canonical)
    preds = {}
    for n in (1.0, 2.0, 6.0):
        th, ph = _minimise(W_BOND, W_LONE, n=n)
        preds[n] = (th, ph)
        print(f"  n={n:>4}: θ_HOH = {th:7.3f}°  φ_LL = {ph:7.3f}°  "
              f"narrowing {theta0 - th:+.2f}° (obs {theta0 - theta_obs:+.2f}°)")
    th1 = preds[1.0][0]
    print()
    print(f"  Coulomb (n=1) prediction: θ ≈ {th1:.2f}°  vs observed {theta_obs}°")
    print(f"  → right sign (narrows), ~{(theta0-th1)/(theta0-theta_obs)*100:.0f}% "
          f"of the observed narrowing; residual NOT fitted.")

    ctrl_ok = abs(th_ctrl - theta0) < 0.05
    narrows = th1 < theta0

    w = WitnessBuilder("h2o-bond-angle-magnitude-vsepr", engine="python")
    w.set_description(
        "H₂O H–O–H angle magnitude via trace-weighted VSEPR (points-on-a-"
        "sphere, Coulomb kernel, NO fit parameter). Domain weights are "
        "q-exact Markov traces (w_lone/w_bond = h z + 1). Self-validates at "
        "equal weights (θ=109.47°). Trace weights give θ≈107.2° (narrows "
        "≈2.3°): correct sign and order of magnitude vs observed 104.5° "
        "(narrows 4.97°); residual reported, not fitted. Supplies the "
        "geometric stiffness a for prop:h2o-bond-angle-shift's b/(2a)."
    )
    w.set_content_block("prop:h2o-bond-angle-shift")
    w.add_parameter("w_bond_tr_M", W_BOND)
    w.add_parameter("w_lone_tr_M", W_LONE)
    w.add_parameter("weight_ratio_hz_plus_1", ratio)
    w.add_data("theta0_tetrahedral_deg", theta0)
    w.add_data("theta_observed_deg", theta_obs)
    w.add_data("theta_control_equal_weights_deg", th_ctrl)
    w.add_data("theta_pred_coulomb_n1_deg", preds[1.0][0])
    w.add_data("phi_LL_coulomb_n1_deg", preds[1.0][1])
    w.add_data("theta_pred_n2_deg", preds[2.0][0])
    w.add_data("theta_pred_n6_deg", preds[6.0][0])
    w.add_data("narrowing_pred_n1_deg", theta0 - preds[1.0][0])
    w.add_data("narrowing_observed_deg", theta0 - theta_obs)
    w.add_assertion(
        "model self-validates: equal weights ⇒ tetrahedral 109.47°",
        computed=bool(ctrl_ok), expected=True,
        source="no built-in angular bias; minimiser of the symmetric "
               "Coulomb energy is arccos(−1/3)",
    )
    w.add_assertion(
        "trace weights NARROW the angle below tetrahedral (correct sign)",
        computed=bool(narrows), expected=True,
        source=f"θ_pred={preds[1.0][0]:.2f}° < {theta0:.2f}°; reverses the "
               "|Φ₁| model that opened to ~140°",
    )
    w.add_data(
        "finding",
        "Trace-weighted VSEPR (Coulomb, no fit) predicts θ_HOH ≈ "
        f"{preds[1.0][0]:.2f}° — narrowing ≈{theta0-preds[1.0][0]:.1f}° vs "
        f"observed {theta0-theta_obs:.1f}°. Right sign + order of magnitude; "
        "the 10% q-exact trace asymmetry under-predicts the full shift by "
        "~2×. The residual is honest (not fitted): closing it would require "
        "a tuned kernel/asymmetry, forbidden by the no-magnitude-fit rule. "
        "Self-validates at equal weights (109.47°).",
    )
    w.save()
    print("Done. Witness saved (h2o-bond-angle-magnitude-vsepr).")


if __name__ == "__main__":
    main()
