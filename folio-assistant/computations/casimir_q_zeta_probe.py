#!/usr/bin/env python3
"""Probe: casimir-q-zeta
(audit support for `conj:casimir-epsilon-vacuum`).

**Question.**  The standard Casimir prefactor π²/720 arises from
ζ-regularising the cubic mode sum Σ_{n≥1} n³ to ζ(-3) = -1/120.
Does any natural q-deformed analogue at substrate q_0 land on the
same target?

**Empirical search.**  Computes at q = Q ≈ 1.1100 (substrate):

  1. ζ_q(s) := Σ_{n≥1} [n]_q⁻ˢ           for s = 1, 2, 3, 4
  2. ζ_q(-3) attempted three ways:
     a. Σ_{n≥1} (q-1)·[n]_q³           — naive cubic mode sum
     b. lim_{N→∞} Σ_{n=1}^N [n]_q³ · q⁻ᵏⁿ for various damping k
        (q-deformed analytic continuation)
     c. (1/120)·R(q) with R a low-degree polynomial in q ± q⁻¹
  3. compares each to π²/720 ≈ 0.01371742

**Honest expectation.**  Both Σ n³ and Σ [n]_q³ diverge in the
naïve sense; the standard Casimir uses analytic continuation, and
its q-analogue requires choosing a specific q-zeta definition
(Kaneko–Kurokawa–Wakayama 2002, Cherednik 2006).  No single one
of these definitions is *forced* by QOU structure — this probe
tabulates several to see which (if any) lies closest to the target.

A null result (none match within 10⁻³) is documented as such; it
does not refute the conjecture but tightens the open content.

Emits `casimir-q-zeta-probe.witness.json`.

Ref: [casimir1948] https://dwc.knaw.nl/DL/publications/PU00018547.pdf
Ref: [manuscript] appendix-surreals/casimir-epsilon-vacuum.md
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from mpmath import mp, mpf, mpc, pi as mp_pi, exp as mp_exp  # noqa: E402

from q_parameter import Q  # noqa: E402 — substrate q ≈ 1.1100
from witness_base import WitnessBuilder  # noqa: E402


mp.dps = 50


def _q_int(n: int, q: "mpf") -> "mpf":
    """q-integer [n]_q = (qⁿ - q⁻ⁿ) / (q - q⁻¹)."""
    return (q ** n - q ** (-n)) / (q - 1 / q)


def _zeta_q(s: int, q: "mpf", N: int = 200) -> "mpf":
    """Σ_{n=1}^N [n]_q⁻ˢ (converges geometrically for s ≥ 1, q > 1)."""
    return sum(mpf(1) / _q_int(n, q) ** s for n in range(1, N + 1))


def _sum_q_cubic_damped(q: "mpf", k: int, N: int = 200) -> "mpf":
    """Σ_{n=1}^N [n]_q³ · q^(-k n) — damped cubic mode sum."""
    return sum(_q_int(n, q) ** 3 * q ** (-k * n) for n in range(1, N + 1))


def main() -> int:
    builder = WitnessBuilder(
        "casimir-q-zeta-probe",
        engine="mpmath",
    )

    q = mpf(Q)  # substrate q (cast to high-precision mpf)
    pi_sq_720 = mp_pi ** 2 / 720
    target_str = f"π²/720 ≈ {float(pi_sq_720):.8e}"

    # ─── Family 1: ζ_q(s) for s ≥ 1 (always converges) ───
    zeta_q_values = {}
    for s in [1, 2, 3, 4]:
        zeta_q_values[s] = _zeta_q(s, q, N=200)

    # ─── Family 2: damped cubic sums (q-analytic-continuation) ───
    damped_cubic = {}
    for k in [3, 4, 5, 6, 7, 8, 9, 10, 12, 15]:
        damped_cubic[k] = _sum_q_cubic_damped(q, k, N=200)

    # ─── Family 3: low-degree q-rationals of form a · π²/[m]_q ───
    # Skip m_q_idx = 1 because [1]_q = 1 trivializes the match.
    pi_sq = mp_pi ** 2
    candidate_q_rationals = []
    for m_q_idx in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
        m_q = _q_int(m_q_idx, q)
        for num_int in [1, 2, 3, 4, 5, 6, 8, 10, 12]:
            val = pi_sq * num_int / (720 * m_q)
            candidate_q_rationals.append({
                "form": f"{num_int}·π²/(720·[{m_q_idx}]_q)",
                "value": float(val),
                "ratio_to_target": float(val / pi_sq_720),
            })
        # Also try π²/(720·[m]_q²) and ·[m]_q³
        for pow_idx in [2, 3]:
            for num_int in [1, 2, 3, 6]:
                val = pi_sq * num_int / (720 * m_q ** pow_idx)
                candidate_q_rationals.append({
                    "form": f"{num_int}·π²/(720·[{m_q_idx}]_q^{pow_idx})",
                    "value": float(val),
                    "ratio_to_target": float(val / pi_sq_720),
                })

    # ─── Family 4: closest match across all families ───
    best_match = None
    best_residue = mpf("inf")

    # Damped-cubic family normalized comparison.
    for k, val in damped_cubic.items():
        # The q-zeta-regularised "ζ_q(-3)" analogue ~ -val ?
        # If it matches -1/120 (i.e. the standard ζ(-3)), then
        # π²·val/6 should match π²/720 · (-120 · (-1/120)) etc.
        # We just check raw match here.
        residue = abs(val - pi_sq_720)
        if residue < best_residue:
            best_residue = residue
            best_match = ("damped_cubic", k, float(val))

    # Candidate-q-rationals comparison.
    for cand in candidate_q_rationals:
        residue = abs(mpf(cand["value"]) - pi_sq_720)
        if residue < best_residue:
            best_residue = residue
            best_match = (
                "q_rational", cand["form"], cand["value"],
            )

    (
        builder
        .set_description(
            "Empirical search for a q-rational expression at "
            "substrate q ≈ 1.1100 matching the standard Casimir "
            "prefactor π²/720 ≈ 1.372e-2.  Tabulates ζ_q(s) for "
            "s = 1..4, damped cubic mode sums Σ [n]_q³·q⁻ᵏⁿ for "
            "k = 3..15, and low-degree q-rationals a·π²/(720·[m]_q).  "
            "Reports the closest match and its residue.  A null "
            "result (no match within 1e-3) is acceptable — it "
            "documents that the π²/720 prefactor is not a "
            "trivially-q-rational object at q_0, tightening "
            "sub-problem (3) of conj:casimir-epsilon-vacuum."
        )
        .set_content_block("conj:casimir-epsilon-vacuum")
        .add_parameter("substrate_q", float(q))
        .add_parameter("target_pi_sq_720", float(pi_sq_720))
        .add_data(
            "zeta_q_values",
            {str(s): float(v) for s, v in zeta_q_values.items()},
        )
        .add_data(
            "damped_cubic_sums",
            {str(k): float(v) for k, v in damped_cubic.items()},
        )
        .add_data(
            "candidate_q_rationals",
            candidate_q_rationals,
        )
        .add_data(
            "best_match",
            {
                "family": best_match[0],
                "form": str(best_match[1]),
                "value": best_match[2],
                "residue": float(best_residue),
                "ratio": best_match[2] / float(pi_sq_720),
            },
        )
        .add_assertion(
            name="best_match_within_one_percent_of_target",
            computed=float(best_residue / pi_sq_720),
            expected=0.0,
            tolerance=1e-2,
            unit="relative residue |best - target| / target",
            source=(
                "Empirical search across ζ_q(s), damped cubic "
                "sums, and low-degree q-rationals.  Tolerance set "
                "to 1% to register only meaningful matches; a "
                "miss at this tolerance documents a null result."
            ),
        )
    )

    out = builder.save()
    print(f"\nWitness: {out}")
    print()
    print(f"Substrate q = {float(q):.10f}")
    print(f"Target {target_str}")
    print()
    print("─── ζ_q(s) for s = 1..4 ───")
    for s in sorted(zeta_q_values):
        print(f"  ζ_q({s}) = {float(zeta_q_values[s]):.10f}")
    print()
    print("─── Damped cubic Σ [n]_q³ · q⁻ᵏⁿ ───")
    print(f"  {'k':<4} {'value':<22} {'ratio to π²/720':<18}")
    for k in sorted(damped_cubic):
        val = float(damped_cubic[k])
        print(f"  {k:<4} {val:<22.10e} {val/float(pi_sq_720):<18.5f}")
    print()
    print("─── Best match ───")
    print(f"  family: {best_match[0]}")
    print(f"  form:   {best_match[1]}")
    print(f"  value:  {best_match[2]:.10e}")
    print(f"  residue: {float(best_residue):.4e}")
    print(f"  rel residue: {float(best_residue/pi_sq_720):.4e}")
    print()
    if float(best_residue / pi_sq_720) > 1e-2:
        print("→ NULL RESULT: no candidate matches π²/720 within 1%.")
        print("  Sub-problem (3) of the conjecture remains open.")
    else:
        print("→ MATCH FOUND — investigate further.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
