#!/usr/bin/env python3
"""
Independent validation script for the two no-go propositions cited
by `conj:tau-codim-shannon` and `conj:tau-codim-landauer`:

  (1) Jones–Markov weights y_λ are sign-indefinite at n ≥ 4
      (rules out p_q(λ) = y_λ · d_λ as the Shannon-conjecture
      probability measure).

  (2) The L²-Cauchy–Schwarz bound 1/‖C‖² on the trace of a
      unit-normalised creation morphism is strictly weaker than the
      conjectured Landauer bound τ(C_dim_q) for any Frobenius
      algebra with ≥ 2 blocks (rules out a purely L²-Cauchy–Schwarz
      proof of `conj:tau-codim-landauer`).

This script reproduces both facts from scratch using the existing
`y_lambda_jones_markov_witness.solve_jones_markov_weights` solver
and direct linear-algebra computation, and records the result in
`tau-codim-conjectures-validation.witness.json`.

Run:

    cd folio-assistant/computations
    python3 tau_codim_conjectures_validate.py

References:
  - prop:shannon-jones-markov-no-go
  - prop:landauer-cauchy-schwarz-insufficient
  - rem:y-lambda-sign-pattern
"""
from __future__ import annotations

import json
import random
import sys
import warnings
from datetime import datetime, timezone
from pathlib import Path

warnings.filterwarnings("ignore")

sys.path.insert(0, str(Path(__file__).parent))
from y_lambda_jones_markov_witness import solve_jones_markov_weights


# ── Validation 1: Jones–Markov sign-indefiniteness at n ≥ 4 ─────────
def _symbolic_y_one4_at_q0() -> dict | None:
    """Cross-check pathway: evaluate the pre-existing q-rational
    symbolic expression for y_{(1,1,1,1)} at q₀ via sympy."""
    sym_path = (
        Path(__file__).parent / "y-lambda-symbolic-witness.json"
    )
    if not sym_path.exists():
        return None
    try:
        import sympy as sp  # type: ignore[import-not-found]
    except ImportError:
        return None
    payload = json.loads(sym_path.read_text())
    n4 = payload.get("tables_by_n", {}).get("4")
    if n4 is None:
        return None
    for entry in n4.get("weights", []):
        if entry.get("partition") == [1, 1, 1, 1]:
            q = sp.Symbol("q", positive=True)
            sym = sp.sympify(
                entry["y_lambda_symbolic"], locals={"q": q}
            )
            from q_parameter import Q as Q0_FLOAT

            q0_rat = sp.Rational(str(Q0_FLOAT))
            val = float(sym.subs(q, q0_rat).evalf(50))
            return {
                "pathway": "sympy q-rational symbolic",
                "y_lambda_one4_at_q0": val,
                "source_witness": "y-lambda-symbolic-witness.json",
            }
    return None


def _mpfr_y_one4_at_q0() -> dict | None:
    """Cross-check pathway: lift y_{(1,1,1,1)} from the pre-existing
    50-digit mpfr witness."""
    mpfr_path = (
        Path(__file__).parent / "y-lambda-mpfr-witness.json"
    )
    if not mpfr_path.exists():
        return None
    payload = json.loads(mpfr_path.read_text())
    # Two possible layouts: flat 'weights' or 'tables_by_n[4]'
    table = payload.get("tables_by_n", {}).get("4", payload)
    for entry in table.get("weights", []):
        if entry.get("partition") == [1, 1, 1, 1]:
            return {
                "pathway": "pre-existing 50-digit mpfr witness",
                "y_lambda_one4_at_q0": float(entry["y_lambda"]),
                "source_witness": "y-lambda-mpfr-witness.json",
            }
    return None


def validate_shannon_no_go() -> dict:
    """Solve the Jones–Markov linear system from scratch at n ∈ {3, 4, 5}
    and report which partitions have negative y_λ at q₀.  Cross-check
    the critical entry y_{(1,1,1,1)}(q₀) against two independent
    pre-existing witnesses (mpfr, sympy symbolic)."""
    results: list[dict] = []
    fresh_y_one4: float | None = None
    for n in (3, 4, 5):
        r = solve_jones_markov_weights(n, do_crt_probes=False)
        negative = [
            {"partition": w["partition"], "y_lambda": w["y_lambda"]}
            for w in r["weights"]
            if w["y_lambda"] < 0
        ]
        if n == 4:
            for w in r["weights"]:
                if w["partition"] == [1, 1, 1, 1]:
                    fresh_y_one4 = w["y_lambda"]
        results.append(
            {
                "n": n,
                "num_partitions": r["num_partitions"],
                "condition_number": r["diagnostics"]["condition_number"],
                "linear_system_residual": r["diagnostics"][
                    "linear_system_residual"
                ],
                "negative_partitions": negative,
                "all_positive": len(negative) == 0,
            }
        )

    # Three-pathway cross-check on y_{(1,1,1,1)}(q₀)
    pathways: list[dict] = [
        {
            "pathway": "fresh numpy linear solve (this script)",
            "y_lambda_one4_at_q0": fresh_y_one4,
            "source_witness": (
                "tau-codim-conjectures-validation.witness.json"
            ),
        }
    ]
    for cross in (_mpfr_y_one4_at_q0(), _symbolic_y_one4_at_q0()):
        if cross is not None:
            pathways.append(cross)
    finite = [p["y_lambda_one4_at_q0"] for p in pathways if p["y_lambda_one4_at_q0"] is not None]
    max_pairwise_diff = (
        max(finite) - min(finite) if len(finite) >= 2 else None
    )

    return {
        "claim": (
            "Jones–Markov block weights y_λ(q₀) are non-negative at "
            "n ≤ 3 and sign-indefinite at n ≥ 4."
        ),
        "tested_n": [3, 4, 5],
        "per_n": results,
        "three_pathway_cross_check_on_y_one4_at_q0": {
            "pathways": pathways,
            "max_pairwise_difference": max_pairwise_diff,
            "all_negative": all(
                p["y_lambda_one4_at_q0"] is not None
                and p["y_lambda_one4_at_q0"] < 0
                for p in pathways
            ),
        },
        "verdict": (
            "VALIDATED" if (
                results[0]["all_positive"]
                and not results[1]["all_positive"]
                and not results[2]["all_positive"]
            ) else "REFUTED"
        ),
    }


# ── Validation 2: Cauchy–Schwarz insufficient for Landauer ──────────
def cs_bound_vs_tau_C(d_q: list[float], tau_p: list[float]) -> dict:
    """For a Frobenius algebra with quantum dimensions d_q and idempotent
    traces tau_p:
      τ(C)   = Σ 1/d_q(λ)
      ‖C‖²   = Σ 1/(d_q(λ)² · τ(p_λ))
      CS bnd = 1/‖C‖²  (best L²-CS lower bound on τ(f†f) under the
               unit-creation normalization τ(f† C) = 1)
    Returns whether the CS bound is strictly weaker than τ(C). """
    tau_C = sum(1.0 / d for d in d_q)
    norm_C_sq = sum(
        1.0 / (d * d * t) for d, t in zip(d_q, tau_p, strict=True)
    )
    cs_bound = 1.0 / norm_C_sq
    return {
        "tau_C": tau_C,
        "norm_C_sq": norm_C_sq,
        "cs_bound": cs_bound,
        "cs_strictly_weaker": cs_bound < tau_C,
    }


def validate_landauer_no_go() -> dict:
    """A *single* Frobenius-algebra witness where CS bound < τ(C) is
    enough to rule out a purely L²-Cauchy–Schwarz proof of
    `conj:tau-codim-landauer`.  The two-block balanced witness
    (d_q = τ_p = (1, 1)) delivers CS = 1/2 < τ(C) = 2.

    For honesty we *also* report random trials demonstrating the
    converse direction (CS > τ(C)) does occur — i.e. CS and τ(C)
    are incomparable in general.  This means the conjecture is
    *non-trivial* (CS does not imply it) and may be improvable for
    "imbalanced" algebras where CS is the tighter bound."""
    fixed = cs_bound_vs_tau_C([1.0, 1.0], [1.0, 1.0])

    # Family witness: |Λ| balanced blocks, d_q = τ_p = 1 → CS/τ(C) = 1/|Λ|²
    family_witness: list[dict] = []
    for nblocks in (2, 3, 5, 10, 20):
        family_witness.append(
            {
                "nblocks": nblocks,
                **cs_bound_vs_tau_C([1.0] * nblocks, [1.0] * nblocks),
            }
        )

    rng = random.Random(0)
    random_trials: list[dict] = []
    for _ in range(50):
        nblocks = rng.randint(2, 20)
        d_q = [rng.uniform(0.5, 3.0) for _ in range(nblocks)]
        tau_p = [rng.uniform(0.5, 3.0) for _ in range(nblocks)]
        random_trials.append(
            {
                "nblocks": nblocks,
                **cs_bound_vs_tau_C(d_q, tau_p),
            }
        )

    n_cs_weaker = sum(t["cs_strictly_weaker"] for t in random_trials)
    n_cs_stronger = len(random_trials) - n_cs_weaker
    return {
        "claim": (
            "There exists a semisimple Frobenius algebra (in fact an "
            "infinite balanced family) for which the L²-Cauchy–Schwarz "
            "lower bound 1/‖C‖² on τ(f†f) under unit-creation "
            "normalisation is strictly less than the conjectured "
            "Landauer bound τ(C_dim_q) = Σ 1/d_q(λ).  Hence no proof "
            "of `conj:tau-codim-landauer` can rest on the L²-Cauchy–"
            "Schwarz inequality alone."
        ),
        "fixed_two_block_witness": {
            "d_q": [1.0, 1.0],
            "tau_p": [1.0, 1.0],
            **fixed,
        },
        "balanced_family_witness": family_witness,
        "incomparability_evidence": {
            "n_random_trials": len(random_trials),
            "n_with_cs_strictly_weaker": n_cs_weaker,
            "n_with_cs_strictly_stronger": n_cs_stronger,
            "min_ratio_cs_over_tau_C": min(
                t["cs_bound"] / t["tau_C"] for t in random_trials
            ),
            "max_ratio_cs_over_tau_C": max(
                t["cs_bound"] / t["tau_C"] for t in random_trials
            ),
            "interpretation": (
                "CS and τ(C) are incomparable in general: both "
                "directions occur in random Frobenius algebras with "
                "block counts in [2, 20] and parameters in [0.5, 3]. "
                "This makes the conjecture non-trivial (not implied "
                "by CS) for the balanced class, and potentially "
                "non-tight (weaker than CS) for the imbalanced class."
            ),
        },
        "verdict": (
            "VALIDATED"
            if (
                fixed["cs_strictly_weaker"]
                and all(f["cs_strictly_weaker"] for f in family_witness)
            )
            else "REFUTED"
        ),
    }


# ── Main ────────────────────────────────────────────────────────────
def main() -> None:
    shannon = validate_shannon_no_go()
    landauer = validate_landauer_no_go()
    payload = {
        "description": (
            "Independent validation of the two no-go propositions "
            "supporting `conj:tau-codim-shannon` and "
            "`conj:tau-codim-landauer`."
        ),
        "references": [
            "prop:shannon-jones-markov-no-go",
            "prop:landauer-cauchy-schwarz-insufficient",
            "rem:y-lambda-sign-pattern",
            "conj:tau-codim-shannon",
            "conj:tau-codim-landauer",
        ],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "shannon_no_go": shannon,
        "landauer_no_go": landauer,
    }
    out = (
        Path(__file__).parent
        / "tau-codim-conjectures-validation.witness.json"
    )
    out.write_text(json.dumps(payload, indent=2, sort_keys=False))
    print(f"Wrote {out}")
    print(f"Shannon no-go:  {shannon['verdict']}")
    print(f"Landauer no-go: {landauer['verdict']}")


if __name__ == "__main__":
    main()
