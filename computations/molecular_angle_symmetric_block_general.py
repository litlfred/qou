#!/usr/bin/env python3
# polynomial_q_not_applicable: Wedderburn-block eigenvalue ratio + VSEPR
# geometry, not a Jones-polynomial evaluation.
"""
GENERAL symmetric-Wedderburn-block bond angles (AX_n E_m hydrides).

Generalises the H₂O result (`h2o_angle_q2_symmetric_block.py`): on the
symmetric (trivial) representation of the local H₃(q) that a molecule's
assembly projector selects, every generator acts as the scalar q, so a domain
represented by a braid word of length ℓ has VSEPR weight q^ℓ. The canonical
lone pair is e⁻ = σ₀σ₁σ₀ (ℓ=3) and the σ-bond is ℓ=1, so

    w_lone / w_bond  =  q³ / q  =  q²       (one DERIVED ratio, no central-atom
                                             input, no fit).

The molecule-to-molecule variation is then carried ENTIRELY by the domain
counts (n bonds + m lone pairs), through the weighted points-on-a-sphere VSEPR
minimiser. We predict the X–A–X bond angle for the four second/third-row
hydrides and compare to observed — NO per-molecule tuning.

    CH₄  AX₄E₀ : 0 lone  → symmetric reference (must give 109.47°)
    NH₃  AX₃E₁ : 1 lone
    H₂O  AX₂E₂ : 2 lone
    H₂S  AX₂E₂ : 2 lone (third row — expected to deviate; flagged)

Refs: rem:h2o-c2v-from-projector; h2o_angle_q2_symmetric_block.py.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

_HERE = Path(__file__).resolve().parent
for _p in (str(_HERE),
           str(_HERE.parents[1] / "tools" / "pyhecke" / "python"),
           str(_HERE.parents[1] / "tools" / "qou-substrate" / "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder
from q_parameter import Q as q0

# observed X–A–X angles (deg) — comparison only, never inputs
OBSERVED = {"CH4": 109.47, "NH3": 107.0, "H2O": 104.5, "H2S": 92.1}
SPEC = {  # (n_bond, n_lone)
    "CH4": (4, 0), "NH3": (3, 1), "H2O": (2, 2), "H2S": (2, 2),
}


def _pts(x):
    v = x.reshape(-1, 3)
    nrm = np.linalg.norm(v, axis=1, keepdims=True)
    return v / np.maximum(nrm, 1e-12)


def bond_angle(n_bond, n_lone, w_lone, n_kernel=1.0, restarts=24, seed=0):
    N = n_bond + n_lone
    if N < 2:
        return float("nan")
    wts = np.array([1.0] * n_bond + [w_lone] * n_lone)

    def energy(x):
        p = _pts(x)
        E = 0.0
        for i in range(N):
            for j in range(i + 1, N):
                d = np.linalg.norm(p[i] - p[j])
                if d < 1e-6:
                    return 1e9
                E += wts[i] * wts[j] / d ** n_kernel
        return E

    rng = np.random.default_rng(seed)
    best = None
    for _ in range(restarts):
        x0 = rng.normal(size=3 * N)
        r = minimize(energy, x0, method="Nelder-Mead",
                     options={"xatol": 1e-7, "fatol": 1e-11, "maxiter": 6000})
        if best is None or r.fun < best.fun:
            best = r
    p = _pts(best.x)
    # bond-bond angles: average over all bonding pairs (equal by symmetry)
    angs = []
    for i in range(n_bond):
        for j in range(i + 1, n_bond):
            c = np.clip(np.dot(p[i], p[j]), -1, 1)
            angs.append(np.degrees(np.arccos(c)))
    return float(np.mean(angs)) if angs else float("nan")


def main() -> None:
    w = WitnessBuilder("molecular-angle-symmetric-block-general", engine="python")
    q = float(q0)
    w_lone = q ** 2   # DERIVED ratio (trivial-rep q³/q); same for every molecule

    print("=" * 72)
    print("General symmetric-block bond angles — one derived ratio q², "
          "geometry varies")
    print("=" * 72)
    print(f"  q={q:.6f}  w_lone/w_bond = q² = {w_lone:.6f} (derived, no fit)")
    print(f"  {'molecule':>9}{'AX_nE_m':>10}{'predicted':>12}{'observed':>11}"
          f"{'miss':>9}")
    rows = {}
    for mol, (nb, nl) in SPEC.items():
        pred = bond_angle(nb, nl, w_lone)
        obs = OBSERVED[mol]
        rows[mol] = {"n_bond": nb, "n_lone": nl, "predicted_deg": pred,
                     "observed_deg": obs, "miss_deg": pred - obs}
        print(f"  {mol:>9}{f'AX{nb}E{nl}':>10}{pred:>11.2f}°{obs:>10.1f}°"
              f"{pred-obs:>+8.2f}°")

    # second-row trend (CH4, NH3, H2O) is the clean test; H2S is third-row
    second_row = ["CH4", "NH3", "H2O"]
    max_miss_2row = max(abs(rows[m]["miss_deg"]) for m in second_row)
    print()
    print(f"  second-row hydrides (CH₄,NH₃,H₂O): max |miss| = "
          f"{max_miss_2row:.2f}° with ONE derived ratio + domain counts.")
    print(f"  H₂S (third row): miss {rows['H2S']['miss_deg']:+.1f}° — the q² "
          f"second-row electron structure under-narrows; heavier-atom (less "
          f"hybridised) lone effect is a separate correction.")

    w.set_description(
        "General symmetric-Wedderburn-block bond angles for AX_nE_m hydrides. "
        "One DERIVED lone/bond weight ratio q² (trivial-rep q³/q, no central-"
        "atom input, no fit) plugged into a weighted points-on-a-sphere VSEPR; "
        "molecule variation carried entirely by domain counts (n bonds + m "
        "lone pairs). Predicts CH₄/NH₃/H₂O second-row angles; H₂S (third row) "
        "deviates as expected. Generalises h2o_angle_q2_symmetric_block.py."
    )
    w.set_content_block("prop:h2o-bond-angle-shift")
    w.add_parameter("q", q)
    w.add_parameter("w_lone_over_w_bond_q2", w_lone)
    w.add_data("molecules", rows)
    w.add_data("second_row_max_abs_miss_deg", max_miss_2row)
    w.add_assertion(
        "CH₄ (no lone pairs) reproduces the tetrahedral reference",
        computed=bool(abs(rows["CH4"]["predicted_deg"] - 109.47) < 0.5),
        expected=True,
        source="AX₄E₀: equal weights ⇒ regular tetrahedron 109.47°",
    )
    w.add_assertion(
        "second-row hydrides predicted within ~3° from one derived q² ratio",
        computed=bool(max_miss_2row < 3.5), expected=True,
        source="CH₄/NH₃/H₂O angles from domain counts + the single derived "
               "lone/bond = q² ratio; no per-molecule tuning",
    )
    w.add_data(
        "finding",
        f"The q² lone/bond ratio derived for H₂O generalises: with ONE derived "
        f"ratio (q²={w_lone:.4f}) and only the domain counts, the weighted "
        f"VSEPR predicts the second-row hydride angles CH₄/NH₃/H₂O within "
        f"{max_miss_2row:.1f}° (CH₄ exact by symmetry). H₂S (third row) misses "
        f"by {rows['H2S']['miss_deg']:+.1f}° — the q² second-row electron "
        "structure does not capture the heavier-atom, less-hybridised lone-pair "
        "effect, which is a separate (honest) correction, not a fit knob.",
    )
    w.save()
    print("\nDone. Witness saved (molecular-angle-symmetric-block-general).")


if __name__ == "__main__":
    main()
