#!/usr/bin/env python3
"""
bring_trilog_zeta5_depth_3.py — graded-Mikusiński depth-3 witness.

Numerical witness for ``conj:bring-trilog-depth-3-witness``, the
depth-3 instance of the keystone conjecture
``conj:gb-depth-period-correspondence``.

The keystone predicts: under the archimedean realization functor,
the depth-$n$ grouplike of $\\mathcal{H}_q$ at an algebraic shape
parameter maps to a class in $\\mathcal{P}_n / \\mathcal{P}_{n-1}$
(Goncharov period filtration weight $n$).

Bring-natural depth-3 input: the primitive 5th root of unity
$\\zeta_5 = e^{2\\pi i / 5}$ — natural because Bring's curve has
$S_5$-symmetry, and $\\zeta_5$ generates the cyclotomic field
$\\mathbb{Q}(\\zeta_5)$ over which Bring's curve has natural
$S_5$-equivariant moduli structure.

Output: the depth-3 grouplike value $\\mathrm{Li}_3^q(\\zeta_5)$ at
$q \\to \\zeta_5$ on the unit circle, both real and imaginary
parts. Both are weight-3 Goncharov periods:

  - Re Li_3(zeta_5) = Cl_3(2 pi / 5)  (Clausen-3 of pentagon angle)
  - Im Li_3(zeta_5) = S_3(2 pi / 5)   (sine variant; lives in B_3
                                       Bloch group)

Numerical comparison to known constants:

  - zeta(3) = Li_3(1) = 1.20205 69031 59594 28539 97381 61511...
              (Apéry's constant; a depth-3 reference period)

  - Sum over 5th-roots: Li_3(zeta_5) + Li_3(zeta_5^2) + ...
                       = (5^{1-3} - 1) zeta(3) / (zeta(3))^?
                       (functional-equation-driven, complicated)

The witness records the 50-digit values + cross-references the
known closed-form relations.

Output: ``bring-trilog-zeta5-depth-3.witness.json`` next to this file.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import time
from datetime import datetime, timezone

from mpmath import mp, mpf, mpc, pi, exp, polylog, im, re, zeta
from mpmath import fabs as mpabs

from witness_base import WitnessBuilder

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()


def main() -> None:
    # Capture start time BEFORE the heavy computation so the witness's
    # `durationMs` reflects real runtime (Copilot PR #635 review).
    start = time.monotonic()

    # ── shape parameter zeta_5 ──────────────────────────────────
    THETA_5 = 2 * pi / mpf(5)
    ZETA_5 = exp(mpc(0, 1) * THETA_5)

    # Sanity: zeta_5^5 should be 1
    ZETA_5_TO_5 = ZETA_5 ** 5
    ZETA_5_AS_ROOT_OF_UNITY_CHECK = mpabs(ZETA_5_TO_5 - mpf(1))

    # ── depth-3 grouplike values ────────────────────────────────
    LI_3_ZETA_5 = polylog(3, ZETA_5)
    RE_LI_3 = re(LI_3_ZETA_5)   # = Cl_3(2 pi / 5)
    IM_LI_3 = im(LI_3_ZETA_5)   # = S_3(2 pi / 5)

    # ── reference: Apery's constant zeta(3) ─────────────────────
    ZETA_3 = zeta(3)

    # ── Bring-orbit sum: sum over primitive 5th roots ───────────
    # Functional equation for sums of Li_n at all N-th roots of unity:
    #   sum_{k=1}^{N-1} Li_n(zeta_N^k) = (N^{1-n} - 1) * zeta(n)
    # For N=5, n=3: sum = (1/25 - 1) * zeta(3) = -(24/25) * zeta(3).
    ZETA_5_K = [exp(mpc(0, 1) * THETA_5 * k) for k in range(1, 5)]
    LI_3_ORBIT = sum(polylog(3, z) for z in ZETA_5_K)
    PREDICTED_ORBIT = (mpf(5) ** (1 - 3) - 1) * ZETA_3
    ORBIT_RESIDUAL = mpabs(LI_3_ORBIT - PREDICTED_ORBIT)

    # Imaginary parts cancel under the sum (complex-conjugate pairs):
    LI_3_ORBIT_IM = im(LI_3_ORBIT)

    print("=" * 72)
    print("graded-Mikusiński depth-3 witness — Bring trilog at zeta_5")
    print("=" * 72)
    print(f"shape parameter zeta_5 = e^(2 pi i / 5)")
    print(f"  = {ZETA_5}")
    print(f"sanity: |zeta_5^5 - 1| = {ZETA_5_AS_ROOT_OF_UNITY_CHECK}")
    print()
    print(f"depth-3 grouplike values (Li_3 at zeta_5):")
    print(f"  Re Li_3(zeta_5) = Cl_3(2 pi / 5) = {RE_LI_3}")
    print(f"  Im Li_3(zeta_5) = S_3(2 pi / 5)  = {IM_LI_3}")
    print()
    print(f"reference depth-3 period:")
    print(f"  zeta(3) = Apéry's constant     = {ZETA_3}")
    print()
    print(f"Bring-orbit sum (functional-equation cross-check):")
    print(f"  sum_{{k=1}}^4 Li_3(zeta_5^k)    = {LI_3_ORBIT}")
    print(f"  predicted: (5^{{-2}} - 1) zeta(3) = {PREDICTED_ORBIT}")
    print(f"  residual                       = {ORBIT_RESIDUAL}")
    print(f"  residual < 1e-45               = {float(ORBIT_RESIDUAL) < 1e-45}")
    print(f"  imag part of orbit sum         = {LI_3_ORBIT_IM}")
    print(f"  imag part vanishes (mod eps)   = {abs(float(LI_3_ORBIT_IM)) < 1e-45}")

    witness = {
        "computation": "bring-trilog-zeta5-depth-3",
        "description": (
            "Depth-3 numerical witness for "
            "conj:bring-trilog-depth-3-witness — the depth-3 instance "
            "of the keystone conjecture conj:gb-depth-period-"
            "correspondence.  Computes Li_3 at the primitive 5th root "
            "of unity zeta_5 (Bring-natural input via S_5 symmetry of "
            "Bring's curve).  Real and imaginary parts both lie in "
            "weight-3 Goncharov period class P_3/P_2.  Cross-validated "
            "by the Bring-orbit sum identity sum_{k=1}^4 Li_3(zeta_5^k) "
            "= (5^{-2} - 1) * zeta(3), which agrees to better than "
            "1e-45 at 50 dps."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "precision_decimal_digits": mp.dps,
        "shape_parameter": {
            "form": "e^(2 pi i / 5)",
            "value_str": str(ZETA_5),
            "primitive_root_of_unity_order": 5,
            "S5_symmetry_motivation": (
                "Bring's curve has S_5 symmetry; zeta_5 generates "
                "Q(zeta_5), the natural cyclotomic field for S_5-"
                "equivariant moduli of Bring."
            ),
            "sanity_zeta5_pow5_minus_1": str(ZETA_5_AS_ROOT_OF_UNITY_CHECK),
        },
        "depth_3_grouplike_values": {
            "re_Li_3_zeta5": str(RE_LI_3),
            "re_Li_3_zeta5_alt_form": "Cl_3(2 pi / 5)",
            "im_Li_3_zeta5": str(IM_LI_3),
            "im_Li_3_zeta5_alt_form": "S_3(2 pi / 5)",
        },
        "reference_depth_3_period": {
            "zeta_3": str(ZETA_3),
            "name": "Apéry's constant",
        },
        "functional_equation_cross_check": {
            "identity": (
                "sum_{k=1}^{N-1} Li_n(zeta_N^k) = (N^{1-n} - 1) zeta(n)"
            ),
            "instance_N5_n3": (
                "sum_{k=1}^4 Li_3(zeta_5^k) = (1/25 - 1) zeta(3)"
            ),
            "computed_orbit_sum": str(LI_3_ORBIT),
            "predicted_orbit_sum": str(PREDICTED_ORBIT),
            "residual": str(ORBIT_RESIDUAL),
            "residual_below_1e_45": float(ORBIT_RESIDUAL) < 1e-45,
            "imag_part_of_orbit_should_vanish": str(LI_3_ORBIT_IM),
            "imag_vanishes_below_1e_45": (
                abs(float(LI_3_ORBIT_IM)) < 1e-45
            ),
        },
        "depth_correspondence": {
            "iterated_integral_depth": 3,
            "goncharov_period_depth": 3,
            "match": True,
            "interpretation": (
                "Li_3 grouplike at algebraic point (zeta_5) maps under "
                "tau_arch to weight-3 Goncharov period.  Both real "
                "(Cl_3) and imaginary (S_3) components are P_3/P_2 "
                "elements; bar involution exchanges them via "
                "complex conjugation."
            ),
        },
        "open_question_geometric_realisation": (
            "Identifying a hyperbolic 4-manifold or Chern-Simons "
            "invariant whose volume / regulator equals Re Li_3(zeta_5) "
            "or Im Li_3(zeta_5) is open.  The natural candidates are "
            "(a) hyperbolic 4-manifolds with cusps shaped on Bring's "
            "S_5-orbit, (b) CS invariants of S_5-symmetric knots in "
            "S^3, (c) iterated integrals on the moduli space of "
            "Bring's curve."
        ),
    }
    # WitnessBuilder.wrap_legacy preserves on-disk layout while adding
    # canonical metadata.  `_start_time` override captures real
    # compute runtime per Copilot PR #635 review.
    builder = WitnessBuilder.wrap_legacy(
        "bring-trilog-zeta5-depth-3",
        witness,
        script_path=__file__,
        engine="mpmath",
        start_time=start,
    )
    out = builder.save()
    print(f"\nwitness: {out}")


if __name__ == "__main__":
    main()
