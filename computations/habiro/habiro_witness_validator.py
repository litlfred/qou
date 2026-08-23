#!/usr/bin/env python3


# Re-trigger CI for PR #566 (round 9 witness regen + audit gate).
"""
Habiro divisibility validator — `tail_in_ideal` axiom witness.

The Lean class `QOU.BraidKnot.HabiroCompletion`
(content/quantum-observable-universe/braids-and-knots/full-pole-structure-mass-trace.lean)
records the Habiro-ideal property as

    ∀ N : ℕ,
      qPochhammerPoly N ∣
        (trace - ∑ m ∈ Finset.range N, coeff m · qPochhammerPoly m)

where `qPochhammerPoly N = ∏_{k=1..N} (1 − u^k) ∈ ℤ[u]`.

This script consumes `habiro-coefficients-atomic.witness.json`
(produced by `habiro_coefficients_atomic.py`), reconstructs each
truncation residual as a `sympy.Poly` over ℤ[u], and certifies
divisibility by `(u;u)_N` for every atom and every truncation
order N up to the recorded coefficient list length.

The output witness `habiro-tail-in-ideal-validation.witness.json`
records, per atom and per N:
  - `divisible` — whether `(u;u)_N` exactly divides the residual,
  - `residual_deg`, `divisor_deg`, `quotient_deg` — for sanity,
  - `quotient_norm` — sup-norm of the quotient coefficients (sanity).

A green run of this script is direct empirical evidence for the
`tail_in_ideal` axiom on the existing Habiro coefficients.
"""

from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp
from sympy import Integer, Symbol

sys.path.insert(0, str(Path(__file__).parent))
from habiro_types import HabiroAtomicWitness, HabiroCompletionRecord  # noqa: E402


def _git_head_sha() -> str:
    """Return the current `git rev-parse HEAD`, or 'unknown' if unavailable."""
    import subprocess
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=Path(__file__).parent,
            stderr=subprocess.DEVNULL,
        ).decode().strip()
    except Exception:
        return "unknown"


HERE = Path(__file__).parent
INPUT_WITNESS = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
OUTPUT_WITNESS = _pb.witness_path("habiro-tail-in-ideal-validation.witness.json", HERE)


def q_pochhammer_poly(N: int, u: Symbol) -> sp.Poly:
    """`(u;u)_N = ∏_{k=1..N} (1 − u^k)` as a sympy Poly over ℤ[u]."""
    expr = Integer(1)
    for k in range(1, N + 1):
        expr *= (1 - u ** k)
    return sp.Poly(sp.expand(expr), u, domain="ZZ")


def parse_poly(s: str, u: Symbol) -> sp.Poly:
    """Parse a witness-format polynomial string to `sympy.Poly` over ℤ[u]."""
    expr = sp.sympify(s, locals={"check_q": u, "u": u})
    return sp.Poly(sp.expand(expr), u, domain="ZZ")


def validate_atom(record: HabiroCompletionRecord, u: Symbol) -> dict:
    """Reconstruct residuals and certify divisibility for one atom."""
    p_u = parse_poly(record.p_in_u, u)
    coeffs = [parse_poly(c.a_m, u) for c in record.habiro_coefficients]

    checks: list[dict] = []
    overall_pass = True

    for N in range(1, len(coeffs) + 1):
        partial_sum = sp.Poly(Integer(0), u, domain="ZZ")
        for m in range(N):
            partial_sum = partial_sum + coeffs[m] * q_pochhammer_poly(m, u)
        residual = p_u - partial_sum
        divisor = q_pochhammer_poly(N, u)

        try:
            quotient, remainder = sp.div(residual, divisor, u, domain="ZZ")
            divisible = remainder.is_zero
        except sp.PolynomialError as exc:
            quotient, remainder = None, None
            divisible = False
            checks.append({
                "N": N,
                "divisible": False,
                "error": str(exc),
            })
            overall_pass = False
            continue

        # Sanity stats
        residual_deg = sp.Poly(residual, u, domain="ZZ").degree() if not residual.is_zero else -1
        divisor_deg = divisor.degree()
        quotient_deg = quotient.degree() if quotient is not None and not quotient.is_zero else -1
        if quotient is not None:
            qcoeffs = quotient.all_coeffs()
            quotient_norm = max((abs(int(c)) for c in qcoeffs), default=0)
        else:
            quotient_norm = None

        checks.append({
            "N": N,
            "divisible": bool(divisible),
            "residual_deg": int(residual_deg),
            "divisor_deg": int(divisor_deg),
            "quotient_deg": int(quotient_deg),
            "quotient_norm": int(quotient_norm) if quotient_norm is not None else None,
        })
        if not divisible:
            overall_pass = False

    # Termination check: p_u must equal the full partial sum exactly.
    full_sum = sp.Poly(Integer(0), u, domain="ZZ")
    for m, a_m in enumerate(coeffs):
        full_sum = full_sum + a_m * q_pochhammer_poly(m, u)
    full_residual = p_u - full_sum
    exact_reconstruction = full_residual.is_zero
    if not exact_reconstruction:
        overall_pass = False

    return {
        "atom": record.atom_label,
        "deg_p_u": record.deg_p_u,
        "n_coefficients": len(coeffs),
        "all_pass": overall_pass,
        "exact_reconstruction": bool(exact_reconstruction),
        "checks": checks,
    }


def main() -> int:
    if not INPUT_WITNESS.exists():
        print(f"ERROR: input witness not found at {INPUT_WITNESS}", file=sys.stderr)
        return 1

    witness = HabiroAtomicWitness.from_json(INPUT_WITNESS)

    u = sp.symbols("u")
    per_atom_results: list[dict] = []
    overall_pass = True

    for record in witness.records:
        atom_result = validate_atom(record, u)
        per_atom_results.append(atom_result)
        overall_pass = overall_pass and atom_result["all_pass"]

    output = {
        "computation": "habiro-tail-in-ideal-validation",
        "description": (
            "Certifies the Lean axiom HabiroCompletion.tail_in_ideal "
            "on the witnesses produced by habiro_coefficients_atomic.py: "
            "for every atom and every truncation order N, the residual "
            "p(u) − Σ_{m<N} a_m(u) · (u;u)_m is exactly divisible by "
            "(u;u)_N in ℤ[u]."
        ),
        "reference_blocks": [
            "prop:full-pole-structure-mass-trace",
            "def:habiro-ring",
        ],
        "lean_axiom": "qou:QOU.BraidKnot.HabiroCompletion.tail_in_ideal",
        "input_witness": INPUT_WITNESS.name,
        "overall_pass": overall_pass,
        "results": per_atom_results,
        "scriptFile": "habiro_witness_validator.py",
        "commitSha": _git_head_sha(),
    }
    # polynomial_q_not_applicable: validator emits boolean divisibility /
    # exact-reconstruction checks over ZZ[u], not a polynomial-in-q form.
    # The symbolic Habiro polynomials live in
    # habiro-coefficients-atomic.witness.json (validated input).
    # The NA marker therefore belongs in the source comment, not in
    # the witness JSON itself (which is bit-checked by CI drift
    # detection in .github/workflows/witness-pipeline.yml).

    # Migrated to WitnessBuilder.wrap_legacy per repo-wide provenance
    # convention (Copilot review on PR #819): preserves the legacy
    # payload keys verbatim while emitting `scriptFile`, `scriptHash`,
    # `scriptCommitSha`, `commitSha`, `computedAt`, `durationMs`,
    # `engineVersion` for run_pipeline.py's staleness detection (P30).
    from witness_base import WitnessBuilder
    builder = WitnessBuilder.wrap_legacy(
        name="habiro-tail-in-ideal-validation",
        payload=output,
        script_path=__file__,
        engine="sympy.div over ZZ[u]",
    )
    builder.save()

    # Console summary
    status = "PASS" if overall_pass else "FAIL"
    print(f"habiro_witness_validator: {status}")
    for r in per_atom_results:
        atom = r["atom"]
        n_checks = len(r["checks"])
        n_passed = sum(1 for c in r["checks"] if c.get("divisible"))
        recon = "exact" if r.get("exact_reconstruction") else "INCOMPLETE"
        print(f"  {atom:>24}  {n_passed}/{n_checks} divisibility   reconstruction: {recon}")

    print(f"Wrote {OUTPUT_WITNESS}")
    return 0 if overall_pass else 2


if __name__ == "__main__":
    sys.exit(main())
