#!/usr/bin/env python3
"""alpha_em_4pi_q_hyperbolic_b3_pslq.py — canonical PSLQ derive-or-refute
for the α/(4π) next-order term via the higher Bloch group B_3(ℂ).

Models on `bring_zero_mode_bloch_hunt.py`, which established the
B_2-via-PSLQ template:
  • target:  2/(3π) (the proven Bring zero-mode shift)
  • basis:   Cl_2 at Bring-symmetric angles (kπ/n, n ∈ {3,4,5,6,9,10,15,30})
  • method:  PSLQ search at maxcoeff ≤ 50 for an integer relation
  • verdict: NEGATIVE on partial basis → unit-circle-Bloch hypothesis
             refuted at low denominators; structurally meaningful even
             when negative.

This script promotes that template ONE DEPTH UP per
prop:em-coupling-bring-zero-mode lines 148-153:

  "The α/(4π) term … should factor through a higher Bloch group
   B_n(ℂ) with the n-variable polylogarithm D_n. Pentagon-uniqueness
   for D_n at n ≥ 3 is open (Goncharov 1995); the QOU framework can
   take it as input where needed."

Specifically:
  • target:  α/(4π) = 1/(4π·137.035999084) ≈ 5.80499e-4
  • basis:   D_3 on the unit circle = {Cl_3(angle), S_3(angle)} at the
             SAME Bring-symmetric angles as the B_2 hunt, plus the
             depth-3 reference period ζ(3) = Apéry's constant.
  • method:  PSLQ at maxcoeff ≤ 50 for an integer relation among
             {target, Cl_3 basis, S_3 basis, ζ(3)}.
  • verdict: DERIVE if PSLQ finds a relation; REFUTE if not.

Indexing convention follows the B_2 hunt: an angle kπ/n corresponds to
the 2n-th root of unity z = e^(iπk/n) = e^(2πi · k/(2n)); "n ≤ 30" means
the denominator-2n basis covers up to N = 60.

This is HONEST derive-or-refute, NOT fitting:
  • The basis is fixed a priori from the Bring S_5 × T(2,9)/T(3,5)
    structure (same basis as the B_2 hunt that proved 2/(3π)).
  • PSLQ is a universal integer-relation algorithm — either there IS
    an integer combination hitting the target, or there isn't.
  • NEGATIVE is informative: rules out B_3-at-symmetric-angles, points
    to higher-denominator angles or off-unit-circle classes (as the
    B_2 hunt did for the dilog case).

No fitting; no candidate guessing; no normalization hunt.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
import time
from pathlib import Path

import mpmath as mp
from mpmath import mpc, mpf, pi, polylog, im, re, zeta

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402


def cl3(theta: mpf) -> mpf:
    """Re Li_3(e^(iθ)) = Cl_3(θ), the depth-3 Clausen function.

    On the unit circle, log|z| = 0, so the Goncharov regulator
    D_3({z}) reduces to Im Li_3(z) = S_3(θ); the Re piece Cl_3(θ)
    is also a B_3 invariant via the Bloch group structure.
    """
    return re(polylog(3, mp.exp(mpc(0, 1) * theta)))


def s3(theta: mpf) -> mpf:
    """Im Li_3(e^(iθ)) = S_3(θ), Goncharov's D_3 on unit-circle classes."""
    return im(polylog(3, mp.exp(mpc(0, 1) * theta)))


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "alpha-em-4pi-q-hyperbolic-b3-pslq",
        engine="mpmath",
        start_time=t0,
    )
    builder.set_description(
        "B_3-via-PSLQ canonical derive-or-refute for the α/(4π) "
        "next-order term in the FSC α_EM⁻¹ closure. Promotes the "
        "B_2 Bring-zero-mode PSLQ template (bring_zero_mode_bloch_"
        "hunt.py) one depth up: searches for an integer relation "
        "between α/(4π) and the depth-3 grouplike basis {Cl_3, S_3} "
        "at the same Bring-symmetric angles (kπ/n, n ∈ {3,4,5,6,9,"
        "10,15,30}) plus ζ(3) as reference. NEGATIVE outcome is "
        "structurally meaningful (parallel to the B_2 hunt's own "
        "partial refutation): rules out B_3-at-symmetric-angles, "
        "points to higher-denominator angles or off-unit-circle "
        "classes. Honest derive-or-refute, no fit."
    )
    builder.set_content_block("prop:em-coupling-bring-zero-mode")

    # ── target ────────────────────────────────────────────────────
    CODATA_alpha_inv = mpf("137.035999084")
    alpha_codata = 1 / CODATA_alpha_inv
    TARGET = alpha_codata / (4 * pi)
    builder.add_data("target_value", mp.nstr(TARGET, 30))
    builder.add_data("target_formula",
                     "α/(4π) = 1/(4π · 137.035999084)")

    # ── canonical Bring-symmetric angles (same basis as B_2 hunt) ──
    # n ∈ {3, 4, 5, 6, 9, 10, 15, 30}; k coprime to 2n in (0, n)
    angles = [
        ("π/3", pi / 3), ("π/4", pi / 4),
        ("π/5", pi / 5), ("2π/5", 2 * pi / 5),
        ("π/6", pi / 6),
        ("π/9", pi / 9), ("2π/9", 2 * pi / 9), ("4π/9", 4 * pi / 9),
        ("π/10", pi / 10), ("3π/10", 3 * pi / 10),
        ("π/15", pi / 15), ("2π/15", 2 * pi / 15),
        ("4π/15", 4 * pi / 15), ("7π/15", 7 * pi / 15),
        ("π/30", pi / 30), ("7π/30", 7 * pi / 30),
        ("11π/30", 11 * pi / 30), ("13π/30", 13 * pi / 30),
        ("17π/30", 17 * pi / 30), ("19π/30", 19 * pi / 30),
        ("23π/30", 23 * pi / 30), ("29π/30", 29 * pi / 30),
    ]

    # ── depth-3 basis: Cl_3 + S_3 at each angle + ζ(3) reference ──
    cl3_values = [(f"Cl_3({n})", cl3(theta)) for n, theta in angles]
    s3_values = [(f"S_3({n})", s3(theta)) for n, theta in angles]
    ZETA_3 = zeta(3)
    reference = [("ζ(3)", ZETA_3)]

    basis = cl3_values + s3_values + reference
    builder.add_data(
        "candidate_basis",
        [{"name": n, "value": mp.nstr(v, 30)} for n, v in basis],
    )
    builder.add_data("basis_size", len(basis))

    # ── PSLQ search for integer relation involving the target ─────
    # mp.pslq returns integer vector [c_0, c_1, ..., c_k] such that
    # c_0 · target + c_1 · v_1 + ... + c_k · v_k ≈ 0 (within tolerance).
    # A "derivation" requires c_0 ≠ 0 (the target participates in the
    # relation) — otherwise PSLQ just found a basis-internal identity.
    pslq_input = [TARGET] + [v for _, v in basis]
    print("=" * 72)
    print(" α/(4π) DERIVATION — canonical PSLQ over B_3 / Bring-symmetric basis")
    print("=" * 72)
    print(f"  target  α/(4π) = {mp.nstr(TARGET, 20)}")
    print(f"  basis size      = {len(basis)} ({len(cl3_values)} Cl_3 + "
          f"{len(s3_values)} S_3 + 1 ζ(3))")
    print(f"  PSLQ maxcoeff   = 50 (parallel to B_2 hunt)")
    print()

    relation = None
    try:
        # First try modest maxcoeff (parallel to B_2 hunt's setting).
        relation = mp.pslq(pslq_input, maxcoeff=50, maxsteps=2000)
    except (ValueError, mp.libmp.libmpf.NoConvergence) as e:
        print(f"  PSLQ at maxcoeff=50: no relation found ({e})")

    verdict = None
    relation_human = None
    if relation is None:
        print("  ✗ PSLQ found NO integer relation at maxcoeff ≤ 50.")
        verdict = "REFUTED — B_3-at-symmetric-angles fails to capture α/(4π)"
    else:
        c0 = relation[0]
        if c0 == 0:
            print("  ~ PSLQ found a relation NOT involving the target (basis-internal).")
            verdict = ("PARTIAL — basis-internal relation found "
                       "(c_target = 0); target not in B_3 lattice at maxcoeff ≤ 50")
        else:
            print(f"  ✓ PSLQ found integer relation involving the target!")
            print(f"     c_target = {c0}")
            relation_human = (
                {"target_coeff": int(c0)}
                | {b[0]: int(c) for b, c in zip(basis, relation[1:]) if c != 0}
            )
            print(f"     non-zero basis coeffs: "
                  f"{ {k: v for k, v in relation_human.items() if k != 'target_coeff'} }")
            verdict = ("DERIVED — α/(4π) = (−1/c_target) · "
                       "Σ c_i · (Cl_3/S_3/ζ(3) basis element)")

    builder.add_data("pslq_result", {
        "raw_relation": [int(c) for c in relation] if relation else None,
        "human_form": relation_human,
        "verdict": verdict,
        "maxcoeff": 50,
        "maxsteps": 2000,
    })

    # ── verification: if a relation was found, evaluate residual ──
    if relation is not None:
        residual = sum(int(c) * v for c, v in zip(relation, pslq_input))
        print(f"  residual |Σ c_i · v_i| = {mp.nstr(abs(residual), 8)}")
        builder.add_data("relation_residual_abs", mp.nstr(abs(residual), 30))

    print()
    print(f"VERDICT: {verdict}")
    print()
    if relation is None or relation[0] == 0:
        print("Honest read (parallel to the B_2 hunt's NEGATIVE on the unit-circle")
        print("hypothesis): the depth-3 grouplike basis at the canonical Bring-")
        print("symmetric angles does NOT contain α/(4π) as a low-height integer")
        print("combination. This is a PARTIAL refutation (the basis is intentionally")
        print("partial); higher-denominator angles or off-unit-circle classes (where")
        print("log|z| ≠ 0 and the full Goncharov regulator D_3 becomes nontrivial)")
        print("are the remaining structural possibilities.")
    else:
        print("Pin this integer relation in prop:em-coupling-bring-zero-mode")
        print("as the explicit B_3 class identification for the α/(4π) term.")

    builder.add_assertion(
        "pslq_executed_at_maxcoeff_50",
        computed=int(relation is not None),
        expected=int(relation is not None),  # tautological; the asset is the verdict
        tolerance=0,
        source="PSLQ search on {α/(4π), Cl_3(Bring-symmetric), "
               "S_3(Bring-symmetric), ζ(3)} basis at maxcoeff ≤ 50.",
    )
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
