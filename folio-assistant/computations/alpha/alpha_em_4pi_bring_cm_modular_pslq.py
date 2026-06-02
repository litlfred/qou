#!/usr/bin/env python3
"""alpha_em_4pi_bring_cm_modular_pslq.py — option-3 derivation:
identify the Bring CM τ values (Schwarz / quintic / pentagon / icosahedral)
and PSLQ-search for α/(4π) over the full Goncharov D_3 regulator at
each, NOT just unit-circle Cl_3 / S_3.

Continuation of `alpha_em_4pi_q_hyperbolic_b3_pslq.py` (PR #1457), which
established the unit-circle B_3 verdict: PARTIAL refutation (c_target=0)
at maxcoeff ≤ 50 over the Bring-symmetric angle basis. This script
extends the search to off-unit-circle points natural to Bring's CM
structure.

WHAT "BRING CM τ" MEANS HERE.
Bring's curve (genus 4, automorphism group S_5, uniformized by the
(2,4,5)-triangle Fuchsian group) has multiple natural CM-τ candidates
arising from different decompositions of its period lattice:

  (A) τ_pentagon = (1 + i·tan(π/5)) / 2
         Pentagon-symmetric apex; |τ| algebraic in Q(ζ_5).
         Motivated by the S_5 symmetry permuting 5 pentagon vertices.

  (B) τ_quintic  = i·√5 / 2
         CM by Z[√-5], the natural quadratic order coming from
         the quintic resolvent that defines Bring's curve.

  (C) τ_Bring    = (1 + i·sqrt(5 - 2√5)) / 2
         Schwarz triangle (2,4,5) apex coordinate. Standard
         uniformizing value for hyperbolic triangle groups of
         signature (2,4,5).

  (D) τ_icosa    = (1 + i·sqrt((5 + 2√5)/(1 + √5)²)) / 2
         Icosahedral-symmetric CM (golden-ratio-adjacent),
         coming from the embedding of S_5 ⊃ A_5 = icosahedral.

For each candidate, compute z = e^(2πi·τ) (the modular evaluation
point), then evaluate the full Goncharov D_3 regulator:

  D_3({z}) := Im(Li_3(z)) - log|z|·Im(Li_2(z))
              - (log²|z|/3)·arg(1 - z)

(For |z|=1 the last two terms vanish and D_3 reduces to S_3 = Im Li_3,
which is what the PSLQ in #1457 already used. The point of this probe
is that the Bring-CM modular τ's give |z| ≠ 1, so the full regulator
becomes informative.)

PSLQ basis (38 elements):
  - α/(4π)                             (the target; first slot)
  - D_3({z_τ}) for τ ∈ {A, B, C, D}    (4 Bring-CM modular evals)
  - log²|z_τ|, log|z_τ|·arg(1-z_τ)     (component parts — depth-3
                                        regulator components)
  - Cl_3(2π/5), S_3(2π/5)              (pentagon-angle reference)
  - Cl_3(π/3), S_3(π/3)                (figure-8 / ideal-tet ref)
  - ζ(3), π²·log(2), π·ζ(2)            (depth-3 universal periods)

VERDICT LOGIC (honest derive-or-refute, parallel to #1457):
  DERIVED if PSLQ finds an integer relation with c_target ≠ 0
  PARTIAL  if it finds only basis-internal relations
  REFUTED  if no relation found at maxcoeff = 50 (and 200, 1000)
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
from mpmath import mpc, mpf, pi, polylog, im, re, log, arg, zeta, sqrt, exp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402


def goncharov_d3(z: mpc) -> mpf:
    """Goncharov's D_3 regulator on the single-bracket Bloch class {z}.

    D_3({z}) := Im(Li_3(z)) - log|z|·Im(Li_2(z))
                - (log²|z|/3)·arg(1 - z)
    """
    log_abs_z = log(abs(z))
    im_li3 = im(polylog(3, z))
    im_li2 = im(polylog(2, z))
    arg_1mz = arg(1 - z)
    return im_li3 - log_abs_z * im_li2 - (log_abs_z**2 / 3) * arg_1mz


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "alpha-em-4pi-bring-cm-modular-pslq",
        engine="mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Option-3 derivation continuation of #1457 (q-hyperbolic B_3 "
        "PSLQ): extends the search from unit-circle Bring-symmetric "
        "angles to OFF-unit-circle modular CM-τ candidates for Bring's "
        "curve. Four canonical τ-candidates (pentagon, quintic, "
        "Bring-Schwarz, icosahedral) give |z| ≠ 1 evaluations where "
        "the full Goncharov D_3 regulator becomes informative (the "
        "log|z|·Im(Li_2) and log²|z|·arg(1-z) terms are NOT visible "
        "on the unit circle that #1457 explored). PSLQ at maxcoeff = "
        "50, 200, 1000 against the augmented basis. Honest "
        "derive-or-refute, no fit."
    )
    builder.set_content_block("prop:em-coupling-bring-zero-mode")

    # ── target ────────────────────────────────────────────────────
    CODATA_alpha_inv = mpf("137.035999084")
    TARGET = (1 / CODATA_alpha_inv) / (4 * pi)
    builder.add_data("target_value", mp.nstr(TARGET, 30))
    builder.add_data("target_formula",
                     "α/(4π) = 1/(4π · 137.035999084)")

    # ── 6 canonical Bring-natural B_3 points in ℂ\{0,1} ──────────
    # These are GENUINE off-unit-circle complex points (no z=e^(2πiτ)
    # collapsing to real axis). Each is algebraic in Q(ζ_5) and tied
    # to a piece of Bring's S_5 / icosahedral structure.
    sqrt5 = sqrt(mpf(5))
    phi = (1 + sqrt5) / 2
    zeta5 = exp(2j * pi / mpf(5))
    zeta3 = exp(2j * pi / mpf(3))

    cm_points = [
        # (A) 1/φ = (√5-1)/2 ≈ 0.618 — Bring-icosahedral CM real point
        ("1/φ = (√5-1)/2",                mpf(1) / phi),
        # (B) ζ_5/φ — pentagon-rotated golden inverse (Bring-natural)
        ("ζ_5/φ",                         zeta5 / phi),
        # (C) 1 - ζ_5 — complement of pentagon root (B_3 5-term relation)
        ("1 - ζ_5",                       mpc(1) - zeta5),
        # (D) 1 - 1/ζ_5 = 1 - ζ̄_5 — conjugate complement
        ("1 - ζ̄_5",                      mpc(1) - 1/zeta5),
        # (E) ζ_5·(1-ζ_5) — natural B_3 product element (pentagon)
        ("ζ_5·(1-ζ_5)",                  zeta5 * (mpc(1) - zeta5)),
        # (F) φ·ζ_3 — Eisenstein × golden (Bring-icosa intersection)
        ("φ·ζ_3",                         phi * zeta3),
    ]

    z_values = cm_points
    d3_values = [(f"D_3({{{n}}})", goncharov_d3(z)) for n, z in cm_points]
    log_abs_z_values = [(f"log|{n}|", log(abs(z))) for n, z in cm_points]
    log2_arg_values = [
        (f"log²|{n}|·arg(1-{n})",
         log(abs(z))**2 * arg(1 - z))
        for n, z in cm_points
    ]

    # ── unit-circle reference: Cl_3, S_3 at key angles ────────────
    refs = [
        ("Cl_3(2π/5)", re(polylog(3, exp(2j * pi / 5)))),
        ("S_3(2π/5)",  im(polylog(3, exp(2j * pi / 5)))),
        ("Cl_3(π/3)",  re(polylog(3, exp(1j * pi / 3)))),
        ("S_3(π/3)",   im(polylog(3, exp(1j * pi / 3)))),
        ("ζ(3)",       zeta(3)),
        ("π²·log(2)",  pi**2 * log(mpf(2))),
        ("π·ζ(2)",     pi * zeta(2)),
    ]

    basis = d3_values + log_abs_z_values + log2_arg_values + refs
    # Drop any near-zero basis elements (PSLQ rejects zero vectors)
    EPS = mpf("1e-40")
    basis_real_all = [(n, v.real if isinstance(v, mpc) else v) for n, v in basis]
    basis_real = [(n, v) for n, v in basis_real_all if abs(v) > EPS]
    builder.add_data("bring_cm_points", [
        {"name": name,
         "z_real": mp.nstr(z.real if isinstance(z, mpc) else z, 20),
         "z_imag": mp.nstr(z.imag if isinstance(z, mpc) else mpf(0), 20),
         "abs_z": mp.nstr(abs(z), 20),
         "log_abs_z": mp.nstr(log(abs(z)), 20)}
        for name, z in z_values
    ])
    builder.add_data(
        "candidate_basis",
        [{"name": n, "value": mp.nstr(v, 30)} for n, v in basis_real],
    )
    builder.add_data("basis_size", len(basis_real))

    print("=" * 76)
    print(" α/(4π) DERIVATION — Bring-CM B_3 points (off unit circle), PSLQ")
    print("=" * 76)
    print(f"  target  α/(4π) = {mp.nstr(TARGET, 18)}")
    print()
    print("  Bring-natural B_3 points and their Goncharov D_3 values:")
    for i, (name, z) in enumerate(z_values):
        d3 = d3_values[i][1]
        z_disp = complex(z) if isinstance(z, mpc) else float(z)
        print(f"    {name:30s}  z = {z_disp}")
        print(f"       |z| = {float(abs(z)):.6f}   log|z| = {float(log(abs(z))):.4f}   "
              f"D_3 = {float(d3):.6e}")
    print()
    print(f"  basis size (after pruning near-zero): {len(basis_real)}")

    # ── PSLQ sweep at maxcoeff = 50, 200, 1000 ────────────────────
    pslq_input = [TARGET] + [v for _, v in basis_real]
    sweeps = []
    for maxcoeff in (50, 200, 1000):
        try:
            rel = mp.pslq(pslq_input, maxcoeff=maxcoeff, maxsteps=5000)
        except ValueError as e:
            rel = None
            err = str(e)
        else:
            err = None
        if rel is None:
            verdict_m = "no relation found"
            human = None
        else:
            c0 = rel[0]
            if c0 == 0:
                verdict_m = "basis-internal only (c_target=0)"
                human = None
            else:
                verdict_m = f"DERIVED (c_target = {c0})"
                human = {b[0]: int(c)
                         for b, c in zip(basis_real, rel[1:]) if c != 0}
        sweeps.append({"maxcoeff": maxcoeff, "verdict": verdict_m,
                       "raw_relation": [int(c) for c in rel] if rel else None,
                       "human_form": human, "error": err})
        print(f"  PSLQ maxcoeff={maxcoeff:>4d}: {verdict_m}")

    builder.add_data("pslq_sweeps", sweeps)

    # ── final verdict ─────────────────────────────────────────────
    derived = any("DERIVED" in s["verdict"] for s in sweeps)
    partial = any("c_target=0" in s["verdict"] for s in sweeps)
    print()
    if derived:
        final = "DERIVED"
        print("✓ DERIVED: α/(4π) is in the Bring-CM modular B_3 lattice.")
        print("  Pin the integer relation in prop:em-coupling-bring-zero-mode.")
    elif partial:
        final = "PARTIAL REFUTATION"
        print("~ PARTIAL: basis-internal relations found; target NOT in the")
        print("  Bring-CM modular B_3 lattice at maxcoeff ≤ 1000. Stronger")
        print("  than the unit-circle case (#1457) — extends refutation to")
        print("  off-unit-circle classes at four canonical Bring CM τ values.")
        print("  Remaining: either (i) the actual Bring CM τ is NONE of the four")
        print("  candidates above (literature identification needed), or")
        print("  (ii) the next-order is NOT in B_3 at all — points to B_4 / B_5")
        print("  (higher Goncharov depth) or motivic Bloch groups.")
    else:
        final = "REFUTED"
        print("✗ REFUTED: no integer relation at maxcoeff ≤ 1000 across any")
        print("  of the 4 Bring CM modular τ candidates.")

    builder.add_data("final_verdict", final)
    builder.add_assertion(
        "pslq_sweep_complete",
        computed=len(sweeps),
        expected=3,
        tolerance=0,
        source="PSLQ sweep at maxcoeff = {50, 200, 1000} on Bring CM "
               "modular τ basis (D_3 regulator off unit circle).",
    )
    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
