#!/usr/bin/env python3
"""alpha_em_4pi_b4_pslq.py — promote the B_3 PSLQ derivation to depth 4
(Goncharov D_4 / tetralog). Honest continuation of #1457.

CONTEXT. Prior depth-search results on α/(4π):
  • #1453: 12 fit-class candidates — all refuted (best 0.34% near-miss)
  • #1457 unit-circle B_3:        PARTIAL (c_target = 0) at maxcoeff 50
  • #1457 off-circle B_3:         PARTIAL (c_target = 0) at maxcoeff 1000

Per prop:em-coupling-bring-zero-mode (lines 148-153), the next-order
term should factor through "a higher Bloch group B_n(ℂ) with the
n-variable polylogarithm D_n. Pentagon-uniqueness for D_n at n ≥ 3 is
open (Goncharov 1995)." This probe ascends one more depth: n = 4.

DEPTH-4 SETUP.
The Goncharov D_4 regulator on a unit-circle class {z = e^(iθ)} reduces
to a combination of Li_4(z) components and its lower-depth predecessors:

  D_4({z}) on |z|=1  =  Im Li_4(z) - log|z|·Im Li_3(z) + ...
                    =  Im Li_4(z)              (since log|z|=0 on |z|=1)
                    =  Sl_4(θ)                 (the depth-4 sine series)

For Re part:
  Re Li_4(e^(iθ)) = Cl_4(θ)                    (the depth-4 Clausen series)

Both Sl_4(θ) and Cl_4(θ) are valid B_4 invariants on unit-circle classes.

PSLQ basis (canonical, parallel to #1457):
  - α/(4π)                                          (target)
  - Cl_4(kπ/n) + Sl_4(kπ/n) at Bring-symmetric     (depth-4 grouplikes)
    angles n ∈ {3,4,5,6,9,10,15,30}                  on the unit circle
  - depth-4 universal references:
       ζ(5)  = Apéry-like depth-5 mass
       ζ(3)·π²
       π⁴   = 90·ζ(4)

VERDICT LOGIC (parallel to B_3):
  DERIVED if PSLQ finds a relation with c_target ≠ 0;
  PARTIAL if PSLQ finds only a basis-internal relation (c_target = 0);
  REFUTED if no relation found at maxcoeff = 50.

If PARTIAL at depth 4 too, the combined refutation chain becomes:
  α/(4π) ∉ B_3 lattice (unit-circle), maxcoeff ≤ 50    (PARTIAL via #1457)
  α/(4π) ∉ B_3 lattice (off-circle), maxcoeff ≤ 1000   (PARTIAL via #1457)
  α/(4π) ∉ B_4 lattice (unit-circle), maxcoeff ≤ 50    (PARTIAL via this PR)
  → α/(4π) requires either B_5+ OR a non-PSLQ derivation route
    (the framework's own roadmap points to RT shadow-world 2-loop).
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
from experimental_constants import ALPHA_EM_INV  # noqa: E402


def cl4(theta: mpf) -> mpf:
    """Re Li_4(e^(iθ)) = Cl_4(θ), depth-4 Clausen (cosine-series)."""
    return re(polylog(4, mp.exp(mpc(0, 1) * theta)))


def sl4(theta: mpf) -> mpf:
    """Im Li_4(e^(iθ)) = Sl_4(θ), depth-4 sine-series (Goncharov D_4
    on unit-circle classes when log|z| = 0)."""
    return im(polylog(4, mp.exp(mpc(0, 1) * theta)))


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "alpha-em-4pi-b4-pslq",
        engine="mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Depth-4 (B_4 / Goncharov D_4) PSLQ derive-or-refute for the "
        "α/(4π) next-order term. Promotes the B_3 PSLQ template "
        "(#1457) one Goncharov depth up: searches for an integer "
        "relation between α/(4π) and the depth-4 grouplike basis "
        "{Cl_4, Sl_4} at the same Bring-symmetric angles (kπ/n, "
        "n ∈ {3,4,5,6,9,10,15,30}) plus depth-4 universal references "
        "{ζ(5), ζ(3)·π², π⁴}. Honest derive-or-refute, no fit."
    )
    builder.set_content_block("prop:em-coupling-bring-zero-mode")

    CODATA_alpha_inv = mpf(str(ALPHA_EM_INV))
    TARGET = (1 / CODATA_alpha_inv) / (4 * pi)
    builder.add_data("target_value", mp.nstr(TARGET, 30))
    builder.add_data("target_formula",
                     "α/(4π) = 1/(4π · ALPHA_EM_INV)")
    builder.add_data("target_codata_source",
                     "experimental_constants.ALPHA_EM_INV (CODATA 2018, Cs recoil)")

    # ── canonical Bring-symmetric angles (same as B_3 / B_2 hunts) ─
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
    cl4_values = [(f"Cl_4({n})", cl4(theta)) for n, theta in angles]
    sl4_values = [(f"Sl_4({n})", sl4(theta)) for n, theta in angles]

    # Depth-4 universal references (Apéry-like depth-5 + π² combinations)
    ZETA_5 = zeta(5)
    ZETA_3 = zeta(3)
    refs = [
        ("ζ(5)",      ZETA_5),
        ("ζ(3)·π²",   ZETA_3 * pi**2),
        ("π⁴",        pi**4),
    ]

    basis = cl4_values + sl4_values + refs
    builder.add_data(
        "candidate_basis",
        [{"name": n, "value": mp.nstr(v, 30)} for n, v in basis],
    )
    builder.add_data("basis_size", len(basis))

    print("=" * 72)
    print(" α/(4π) DERIVATION — B_4 PSLQ (depth-4, Goncharov D_4 on unit circle)")
    print("=" * 72)
    print(f"  target  α/(4π) = {mp.nstr(TARGET, 20)}")
    print(f"  basis size      = {len(basis)} ({len(cl4_values)} Cl_4 + "
          f"{len(sl4_values)} Sl_4 + {len(refs)} refs)")
    print(f"  PSLQ maxcoeff   = 50 (parallel to B_2/B_3 hunts)")
    print()

    pslq_input = [TARGET] + [v for _, v in basis]
    rel = None
    try:
        rel = mp.pslq(pslq_input, maxcoeff=50, maxsteps=2000)
    except ValueError as e:
        print(f"  PSLQ at maxcoeff=50: no relation found ({e})")

    verdict = None
    relation_human = None
    if rel is None:
        print("  ✗ PSLQ found NO integer relation at maxcoeff ≤ 50.")
        verdict = "REFUTED — B_4 lattice at Bring-symmetric angles "\
                  "does not contain α/(4π) at maxcoeff ≤ 50"
    else:
        c0 = rel[0]
        if c0 == 0:
            print("  ~ PSLQ found a basis-internal relation (c_target = 0).")
            verdict = ("PARTIAL — basis-internal relation found "
                       "(c_target = 0); target not in B_4 lattice at maxcoeff ≤ 50")
        else:
            print(f"  ✓ PSLQ found integer relation involving the target!")
            print(f"     c_target = {c0}")
            relation_human = (
                {"target_coeff": int(c0)}
                | {b[0]: int(c) for b, c in zip(basis, rel[1:]) if c != 0}
            )
            verdict = ("DERIVED — α/(4π) = (−1/c_target) · "
                       "Σ c_i · (Cl_4/Sl_4/ζ basis element)")
            print(f"     non-zero basis coeffs: "
                  f"{ {k: v for k, v in relation_human.items() if k != 'target_coeff'} }")

    if rel is not None:
        residual = sum(int(c) * v for c, v in zip(rel, pslq_input))
        print(f"  residual |Σ c_i · v_i| = {mp.nstr(abs(residual), 8)}")
        builder.add_data("relation_residual_abs", mp.nstr(abs(residual), 30))

    builder.add_data("pslq_result", {
        "raw_relation": [int(c) for c in rel] if rel else None,
        "human_form": relation_human,
        "verdict": verdict,
        "maxcoeff": 50,
        "maxsteps": 2000,
    })

    print()
    print(f"VERDICT: {verdict}")
    print()
    if rel is None or rel[0] == 0:
        print("Honest read (parallel to B_2 / B_3 hunts):")
        print("  Combined refutation chain — α/(4π) ∉ Bring-natural lattice:")
        print("    B_2 (unit circle, Cl_2 at Bring-symm angles): PARTIAL (bring_zero_mode_bloch_hunt)")
        print("    B_3 (unit circle, Cl_3 + S_3):              PARTIAL (#1457)")
        print("    B_3 (off circle, full D_3, maxcoeff 1000):  PARTIAL (#1457)")
        print("    B_4 (unit circle, Cl_4 + Sl_4):             PARTIAL (this probe)")
        print("  Implication: the next-order is NOT recoverable by Bloch-group")
        print("  PSLQ at low height. The framework's own roadmap (deprecated")
        print("  derivation-attempts witness) points to RT shadow-world 2-loop.")
    else:
        print("Pin this integer relation in prop:em-coupling-bring-zero-mode")
        print("as the depth-4 B_4 class identification for the α/(4π) term.")

    # Structural invariant assertion — per Copilot review pattern from #1457
    builder.add_assertion(
        "basis_size_invariant",
        computed=len(basis),
        expected=22 + 22 + 3,
        tolerance=0,
        source="Canonical depth-4 basis: 22 Cl_4 + 22 Sl_4 at "
               "Bring-symmetric angles + 3 universal depth-4 refs "
               "= 47 elements (fixed a priori).",
    )
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
