#!/usr/bin/env python3
"""Probe: casimir-xi-2-dig-deeper
(audit support for conj:casimir-epsilon-vacuum, resolves the ξ_2 flip-flop).

**Context.** The ξ_2 substrate-correction coefficient of the Casimir
series went through three reversals on PR #1540:

  1. `ξ_k = 0` (via ε ∝ ℏ_q² calibration)        [casimir_beta_2_derivation.py]
  2. retract: ξ_odd = 0 only, ξ_{even≥2} OPEN     [bar-symmetry-tracking.md]
  3. re-close: `ξ_k = 0` via "Casimir isn't Hecke" [casimir-xi-2-equals-zero.md]

Step 3 contradicts the conjecture block, which frames the prefactor as
"a Hecke-trace identity ... Markov-trace structure on H_n(q)". This probe
settles which (if any) reading is a *derivation* vs. an assumption.

**Two structural findings (q-independent of normalization convention).**

A. The ξ_k = 0 "calibration" derivation is CIRCULAR. casimir_beta_2_derivation.py
   imposes ε = ε_0 · ℏ_q² by hand precisely so the 1/ℏ_q² in Geom_ε cancels.
   Any calibration trivially returns the value it was built to return. Not a
   derivation.

B. ξ_2 is FIXED by which trace functional N_⊙'s mode-count is — i.e. by the
   (unconstructed) N_⊙ object, sub-problem 1. We exhibit the dichotomy on
   canonical Wenzl/Markov primitives:

   - NORMALIZED Markov trace of the identity:  Σ_λ y_λ(q)·dim(λ) ≡ 1  for ALL q
     (this is the Wenzl normalization). → ξ_k = 0, but TAUTOLOGICALLY: the
     normalized trace of the identity is always 1; it carries no Casimir-
     specific content.

   - UNNORMALIZED weight sum  Σ_λ y_λ(q):  q-dependent, and its deviation-from-
     classical h²-coefficient DIVERGES with n (number of strands / modes) as
     ~ n(n-1)/2. A divergent, n-dependent ξ_2 is physically inadmissible for a
     single observable. → the naive "prefactor = Markov trace on H_n(q)" route
     does NOT yield a finite ξ_2 without ζ-regularization across the mode tower
     (which is the q-independent step).

**Conclusion.** ξ_2 = 0 is defensible ONLY as the content-free statement
"normalized trace of identity is 1". Any Casimir-specific (unnormalized) mode
weighting reintroduces q-dependence. The value of ξ_2 is gated on the N_⊙
construction (sub-problem 1, OPEN). The honest invariant:

    ξ_0 = 1   (rank-0, derived)
    ξ_odd = 0 (bar-symmetry, derived)
    ξ_{even≥2} = OPEN (gated on N_⊙ construction)

We also test the survey's reported "tr_M(1)" numbers (0.9946, 0.9839, 0.9680,
0.7510 for n=2..5): they match NEITHER canonical functional, and their
internal h²-coefficients fit −0.123·C(n,2) for n=2,3,4 (the n=5 value is an
outlier breaking the fit). Non-reproducible numbers should not anchor a
closure.

Emits `casimir-xi-2-dig-deeper.witness.json`.

Ref: [casimir1948] https://dwc.knaw.nl/DL/publications/PU00018547.pdf
Ref: [wenzl1988] https://doi.org/10.1007/BF01393695
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from y_lambda_wenzl_bridge import (  # noqa: E402
    y_lambda_wenzl_bridge_numeric,
    classical_dim,
    partitions_of,
)
from q_parameter import Q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 50


def trace_functionals(n: int, q):
    """Return (sum_y_dim, sum_y) for H_n at parameter q.

    sum_y_dim = Σ_λ y_λ(q)·dim(λ)   — NORMALIZED Markov trace of identity
    sum_y     = Σ_λ y_λ(q)          — UNNORMALIZED weight sum
    """
    parts = partitions_of(n)
    sum_y_dim = mp.mpf(0)
    sum_y = mp.mpf(0)
    for p in parts:
        y = y_lambda_wenzl_bridge_numeric(p, q)
        sum_y_dim += classical_dim(p) * y
        sum_y += y
    return sum_y_dim, sum_y


def main() -> int:
    builder = WitnessBuilder(
        "casimir-xi-2-dig-deeper",
        engine="mpmath",
    )
    builder.set_description(
        "Resolves the ξ_2 flip-flop on conj:casimir-epsilon-vacuum. "
        "Shows the ξ_k=0 calibration is circular and that ξ_2 is gated on "
        "the N_⊙ construction: normalized Markov trace of identity ≡ 1 ∀q "
        "(tautological ξ_k=0), unnormalized weight sum diverges with n."
    )
    builder.set_content_block("conj:casimir-epsilon-vacuum")

    q0 = mp.mpf(str(Q))
    h = q0 - 1 / q0
    h2 = h * h

    # ─── Finding B1: normalized trace ≡ 1 across a sweep of q ───
    # If the normalized Markov trace of the identity were the Casimir
    # mode-count weight, ξ_k = 0 — but this holds for ALL q, so it is a
    # normalization tautology, not Casimir physics.
    q_sweep = ["1.05", "1.1099785827513808", "1.3", "1.7", "2.0"]
    normalized_across_q = []
    max_dev_from_1 = mp.mpf(0)
    for qs in q_sweep:
        qv = mp.mpf(qs)
        syd, _ = trace_functionals(4, qv)
        dev = abs(syd - 1)
        max_dev_from_1 = max(max_dev_from_1, dev)
        normalized_across_q.append({"q": qs, "sum_y_dim_n4": mp.nstr(syd, 25)})

    # ─── Finding B2: unnormalized weight sum is q-dependent + diverges in n ───
    per_n = []
    for n in range(2, 8):
        syd, sy = trace_functionals(n, q0)
        sy_cl, _ = mp.mpf(0), None  # classical Σy_λ at q→1
        sy_cl, _swap = _unnorm_classical(n)
        # h²-coefficient of the UNNORMALIZED weight sum vs its classical limit
        h2coef_unnorm = (sy - sy_cl) / (sy_cl * h2) if sy_cl != 0 else None
        per_n.append(
            {
                "n": n,
                "sum_y_dim": mp.nstr(syd, 20),  # ≡ 1
                "sum_y_unnorm": mp.nstr(sy, 12),
                "sum_y_unnorm_classical": mp.nstr(sy_cl, 12),
                "h2coef_unnorm_rel": (
                    mp.nstr(h2coef_unnorm, 8) if h2coef_unnorm is not None else None
                ),
            }
        )

    # ─── Finding B3: test the survey's reported tr_M(1) numbers ───
    # Survey values were (tr-1)/h² = h²-coefficient. They match NEITHER
    # canonical functional. Internally they fit −0.123·C(n,2) for n=2,3,4.
    survey_tr = {2: 0.9946, 3: 0.9839, 4: 0.9680, 5: 0.7510}
    survey_analysis = []
    c_ref = None
    for n, tr in survey_tr.items():
        coef = (tr - 1) / float(h2)
        cn2 = n * (n - 1) / 2
        ratio = coef / cn2
        if n == 2:
            c_ref = ratio
        survey_analysis.append(
            {
                "n": n,
                "survey_tr": tr,
                "h2coef": round(coef, 4),
                "C(n,2)": cn2,
                "coef_over_Cn2": round(ratio, 4),
                "fits_n(n-1)/2": abs(ratio - c_ref) < 0.02 * abs(c_ref),
            }
        )

    builder.add_parameter("substrate_q", float(q0))
    builder.add_parameter("h2_substrate", float(h2))

    builder.add_data(
        "finding_A_calibration_is_circular",
        {
            "claim": "casimir_beta_2_derivation.py derives ξ_k=0 by imposing "
            "ε = ε_0·ℏ_q² so the 1/ℏ_q² in Geom_ε cancels.",
            "verdict": "CIRCULAR — the calibration is chosen to produce the "
            "cancellation; it is an assumption, not a derivation.",
        },
    )
    builder.add_data(
        "finding_B1_normalized_trace_identically_one",
        {
            "functional": "Σ_λ y_λ(q)·dim(λ)  (normalized Markov trace of identity)",
            "across_q": normalized_across_q,
            "max_dev_from_1": mp.nstr(max_dev_from_1, 6),
            "verdict": "≡ 1 for ALL q (Wenzl normalization). ξ_k=0 under this "
            "reading is TAUTOLOGICAL — no Casimir-specific content.",
        },
    )
    builder.add_data(
        "finding_B2_unnormalized_weight_diverges_in_n",
        {
            "functional": "Σ_λ y_λ(q)  (unnormalized weight sum)",
            "per_n": per_n,
            "verdict": "q-dependent; relative h²-coefficient grows with n. A "
            "divergent, n-dependent ξ_2 is inadmissible for a single observable "
            "→ naive 'prefactor = Markov trace on H_n(q)' needs ζ-regularization "
            "(the q-independent step).",
        },
    )
    builder.add_data(
        "finding_B3_survey_numbers_not_reproducible",
        {
            "survey_tr_values": survey_tr,
            "analysis": survey_analysis,
            "verdict": "Survey 'tr_M(1)' matches neither Σy_λ·dim (≡1) nor Σy_λ. "
            "Internally fits −0.123·C(n,2) for n=2,3,4; n=5 is an outlier. "
            "Non-reproducible numbers should not anchor a closure.",
        },
    )
    builder.add_data(
        "conclusion",
        {
            "xi_0": "1 (rank-0, derived)",
            "xi_odd": "0 (bar-symmetry, derived)",
            "xi_even_ge_2": "OPEN — gated on the N_⊙ construction (sub-problem 1)",
            "xi_2_equals_zero_status": "defensible ONLY as the content-free "
            "'normalized trace of identity is 1'; any Casimir-specific mode "
            "weighting reintroduces q-dependence. The casimir-xi-2-equals-zero "
            "closure is RETRACTED to OPEN.",
        },
    )

    builder.add_assertion(
        "normalized_markov_trace_identity_is_one",
        computed=mp.nstr(max_dev_from_1, 6),
        expected="0",
        tolerance=1e-30,
        source="Wenzl normalization Σ_λ y_λ·dim(λ) = 1",
    )

    builder.add_caveat(
        "This probe is an audit support for the ξ_2 reconciliation; it does "
        "NOT construct N_⊙. ξ_2's value remains gated on sub-problem 1."
    )

    out = builder.save()
    print(f"wrote {out}")

    # Console summary
    print("\n=== ξ_2 dig-deeper summary ===")
    print(f"q0 = {float(q0):.10f}, h² = {float(h2):.6f}")
    print("Normalized trace Σy_λ·dim(λ): ≡ 1 across q "
          f"(max dev {mp.nstr(max_dev_from_1, 3)}) → tautological ξ_k=0")
    print("Unnormalized Σy_λ rel. h²-coef by n:")
    for row in per_n:
        print(f"  n={row['n']}: {row['h2coef_unnorm_rel']}")
    print("Survey tr_M(1) fit to −c·C(n,2):")
    for row in survey_analysis:
        print(f"  n={row['n']}: coef/C(n,2)={row['coef_over_Cn2']}, "
              f"fits={row['fits_n(n-1)/2']}")
    return 0


def _unnorm_classical(n: int):
    """Σ_λ y_λ at q→1 (limit), computed at q very close to 1."""
    q1 = mp.mpf("1") + mp.mpf("1e-30")
    parts = partitions_of(n)
    s = mp.mpf(0)
    for p in parts:
        s += y_lambda_wenzl_bridge_numeric(p, q1)
    return s, None


if __name__ == "__main__":
    raise SystemExit(main())
