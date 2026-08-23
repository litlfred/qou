#!/usr/bin/env python3
"""Algebraic norm computation for Habiro Frobenius eigenvalues — Route A extension.

Extends the Galois-trace computation in `habiro_frobenius_probe.py` with the
**algebraic norm** N(Frob_p) = ∏_{σ ∈ Gal} σ(Frob_p), which is the product
(not sum) of Galois conjugates.

If Frob_p were a unit in Z[ζ_{2p}], then N(Frob_p) = ±1. Showing
|N(Frob_p)| > 1 for all p beyond some bound is the Route A proof of
`almost_everywhere_nontrivial`.

This script reads the existing witness `habiro-frobenius-probe.witness.json`
and recomputes norms from the stored algebraic representatives.

Cross-references:
  - `conj:motivic-perpetual-obstruction`
  - `def:motivic-galois-character`
  - Route A in the refactoring plan

Usage:
    python3 computations/probes/habiro_frobenius_norm_probe.py
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from math import gcd
from pathlib import Path
from typing import Any

import sympy as sp

HERE = Path(__file__).parent
REPO = HERE.parent.parent  # computations/probes/.. -> computations/.. -> repo root

# Habiro coefficient witnesses — try fast-path first, then symbolic.
WITNESS_FAST = REPO / "computations" / "_deprecated" / "habiro-coefficients-atomic-fast.witness.json"
WITNESS_SYMBOLIC = REPO / "computations" / "habiro" / "habiro-coefficients-atomic.witness.json"
WITNESS_OUT = HERE / "habiro-frobenius-norm-probe.witness.json"

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def reduce_mod_cyclotomic(p_in_u: sp.Expr, n: int,
                          u: sp.Symbol) -> sp.Poly:
    """Reduce p(u) ∈ Z[u] modulo Φ_n(u)."""
    phi_n = sp.Poly(sp.cyclotomic_poly(n, u), u)
    p_poly = sp.Poly(sp.expand(p_in_u), u)
    if p_poly.is_zero:
        return sp.Poly(0, u)
    _, rem = p_poly.div(phi_n)
    return rem


def apply_galois(rep: sp.Poly, k: int, n: int,
                 u: sp.Symbol) -> sp.Poly:
    """Apply σ_k: ζ_n ↦ ζ_n^k to rep ∈ Z[ζ_n]."""
    expr = rep.as_expr().subs(u, u ** k)
    return reduce_mod_cyclotomic(expr, n, u)


def poly_to_constant_int(rep: sp.Poly) -> int | None:
    """Extract integer if rep is degree 0, else None."""
    if rep.is_zero:
        return 0
    if rep.degree() != 0:
        return None
    c = rep.all_coeffs()[0]
    if c.is_Integer:
        return int(c)
    return None


def cyclotomic_pochhammer(n: int, m: int, u: sp.Symbol) -> sp.Poly:
    """(ζ_n; ζ_n)_m = ∏_{i=1}^m (1 - u^i) mod Φ_n(u)."""
    phi_n = sp.Poly(sp.cyclotomic_poly(n, u), u)
    result = sp.Poly(1, u)
    for i in range(1, m + 1):
        factor = sp.Poly(1 - u**i, u)
        result = result * factor
        _, result = result.div(phi_n)
    return result


def evaluate_habiro_at_root(habiro_coeffs: list[dict], p: int,
                            u: sp.Symbol) -> dict[str, Any]:
    """Evaluate Habiro element at ζ_{2p} and compute Galois norm."""
    n_2p = 2 * p
    phi_2p = sp.Poly(sp.cyclotomic_poly(n_2p, u), u)

    # Build the truncated Habiro sum: Σ_m a_m(ζ_{2p}) · (ζ_{2p};ζ_{2p})_m
    frob_rep = sp.Poly(0, u)
    truncate_at = None

    for m, coeff_record in enumerate(habiro_coeffs):
        # Pochhammer vanishes at m ≥ 2p, truncating the sum.
        poch = cyclotomic_pochhammer(n_2p, m, u)
        if poch.is_zero:
            truncate_at = m
            break

        a_m_str = coeff_record.get("a_m_str", coeff_record.get("a_m", "0"))
        a_m_expr = sp.sympify(a_m_str, locals={"check_q": u, "u": u})
        a_m_at_zeta = reduce_mod_cyclotomic(a_m_expr, n_2p, u)

        term = a_m_at_zeta * poch
        frob_rep = frob_rep + term
        _, frob_rep = frob_rep.div(phi_2p)

    if truncate_at is None:
        # Data exhausted before Pochhammer vanished — not exact.
        return {
            "prime": p,
            "exact": False,
            "galois_norm_int": None,
            "galois_norm_is_unit": None,
            "galois_trace_int": None,
        }

    # Galois orbit: {k : gcd(k, 2p) = 1}
    galois_ks = [k for k in range(1, n_2p) if gcd(k, n_2p) == 1]

    # Galois TRACE (sum of conjugates)
    trace_rep = sp.Poly(0, u)
    for k in galois_ks:
        sigma_k = apply_galois(frob_rep, k, n_2p, u)
        trace_rep = trace_rep + sigma_k
        _, trace_rep = trace_rep.div(phi_2p)
    trace_int = poly_to_constant_int(trace_rep)

    # Galois NORM (product of conjugates) — the key Route A computation
    norm_rep = sp.Poly(1, u)
    for k in galois_ks:
        sigma_k = apply_galois(frob_rep, k, n_2p, u)
        norm_rep = norm_rep * sigma_k
        _, norm_rep = norm_rep.div(phi_2p)
    norm_int = poly_to_constant_int(norm_rep)

    return {
        "prime": p,
        "exact": True,
        "truncates_at_m": truncate_at,
        "galois_orbit_size": len(galois_ks),
        "galois_trace_int": trace_int,
        "galois_trace_is_integer": trace_int is not None,
        "galois_norm_int": norm_int,
        "galois_norm_is_integer": norm_int is not None,
        "galois_norm_is_unit": (
            norm_int in (1, -1) if norm_int is not None else None
        ),
        "galois_norm_abs": abs(norm_int) if norm_int is not None else None,
    }


def main() -> int:
    # Load Habiro coefficients
    witness_path = WITNESS_FAST if WITNESS_FAST.exists() else WITNESS_SYMBOLIC
    if not witness_path.exists():
        print(f"ERROR: no Habiro coefficient witness at {witness_path}")
        return 1

    data = json.loads(witness_path.read_text())
    atoms = data.get("results", {})
    if not atoms:
        print("ERROR: no atoms in witness")
        return 1

    u = sp.symbols("u")

    print("=" * 72)
    print("Route A: Frobenius algebraic norm probe")
    print("  N(Frob_p) = ∏_σ σ(Frob_p) — is it ±1 (unit) or not?")
    print("=" * 72)

    all_atoms: list[dict] = []
    any_unit_found = False

    for label, record in atoms.items():
        habiro_coeffs = record.get("habiro_coefficients", [])
        if not habiro_coeffs:
            continue

        print(f"\n  {label}:")
        atom_results: list[dict] = []

        for p in PRIMES:
            row = evaluate_habiro_at_root(habiro_coeffs, p, u)
            atom_results.append(row)

            if not row["exact"]:
                print(f"    p={p:>3}  (data exhausted, not exact)")
                continue

            norm_int = row["galois_norm_int"]
            trace_int = row["galois_trace_int"]
            is_unit = row["galois_norm_is_unit"]

            unit_flag = "UNIT!" if is_unit else "non-unit ✓" if is_unit is False else "?"
            if is_unit:
                any_unit_found = True

            print(
                f"    p={p:>3}  "
                f"Tr={str(trace_int):>8s}  "
                f"N={str(norm_int):>12s}  "
                f"|N|={str(row['galois_norm_abs']):>12s}  "
                f"{unit_flag}"
            )

        all_atoms.append({
            "atom_label": label,
            "frobenius_norms": atom_results,
        })

    # Summary
    n_exact = sum(
        1 for a in all_atoms
        for r in a["frobenius_norms"] if r["exact"]
    )
    n_unit = sum(
        1 for a in all_atoms
        for r in a["frobenius_norms"]
        if r.get("galois_norm_is_unit") is True
    )
    n_nonunit = sum(
        1 for a in all_atoms
        for r in a["frobenius_norms"]
        if r.get("galois_norm_is_unit") is False
    )

    print(f"\n{'=' * 72}")
    print(f"Summary: {n_exact} exact evaluations")
    print(f"  non-unit (|N| > 1): {n_nonunit}")
    print(f"  unit (|N| = 1):     {n_unit}")
    print(f"  Route A {'BLOCKED — found unit Frobenius' if any_unit_found else 'SUPPORTED — no units found'}")
    print(f"{'=' * 72}")

    out = {
        "computation": "habiro-frobenius-norm-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Route A probe: compute the algebraic norm "
            "N(Frob_p) = ∏_σ σ(Frob_p) for each (atom, prime). "
            "If Frob_p is a unit in Z[ζ_{2p}], N(Frob_p) = ±1. "
            "Any |N| > 1 proves non-unitality at that prime."
        ),
        "primes": PRIMES,
        "atoms": all_atoms,
        "summary": {
            "n_exact": n_exact,
            "n_unit": n_unit,
            "n_nonunit": n_nonunit,
            "route_a_supported": not any_unit_found,
        },
    }
    WITNESS_OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\nWrote: {WITNESS_OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
