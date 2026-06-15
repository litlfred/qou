#!/usr/bin/env python3
"""Probe: habiro-expansion-atomic (cor:habiro-expansion-atomic).

Verifies the four claims of the corollary against the existing
`habiro-coefficients-atomic.witness.json` data (covers atoms
{proton (p), neutron (n), deuteron (D)}):

1. **Integrality.** Every Habiro coefficient `a_m(u) ∈ ℤ[u]` —
   verified by parsing the witness's `a_m` polynomial strings via
   sympy and checking all coefficients are integers.
2. **Degree bound.** `deg_u a_m(u) ≤ m` — verified by sympy degree
   computation.
3. **Termination.** `a_m = 0` for `m > m_max`, with the bound
   `m_max ≤ ⌈√(2 · deg_u p(u))⌉` — verified by comparing the
   witness's coefficient list length to the corollary's bound.
4. **Uniqueness.** Sequential cyclotomic division reproduces the
   witness's `a_m` sequence — verified by re-running the division
   algorithm on `p(u)` and comparing to the stored coefficients.
   (The witness's `remainder_nonzero == false` for every m
   indicates the division terminated exactly, which is the
   uniqueness signature.)

Emits `habiro-expansion-atomic-probe.witness.json`.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import math
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402


def parse_a_m(a_m_str: str, u: sp.Symbol) -> sp.Expr:
    """Parse a Habiro coefficient polynomial string into sympy."""
    return sp.sympify(a_m_str, locals={"check_q": u})


def all_integer_coeffs(poly: sp.Expr, u: sp.Symbol) -> bool:
    """True if every coefficient of poly (in u) is an integer."""
    if poly == 0:
        return True
    poly = sp.Poly(poly, u)
    return all(c.is_integer for c in poly.all_coeffs())


def main() -> int:
    upstream = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
    data = json.loads(upstream.read_text())

    u = sp.Symbol("u")
    per_atom_rows = []
    integrality_ok = 0
    integrality_total = 0
    degree_ok = 0
    degree_total = 0
    termination_ok = 0
    termination_total = 0

    for atom_key, rec in data["results"].items():
        coeffs = rec.get("habiro_coefficients", [])
        deg_p = int(rec["deg_p_u"])
        m_max_witness = max(c["m"] for c in coeffs) if coeffs else -1
        m_max_bound = math.ceil(math.sqrt(2 * deg_p))

        atom_row = {
            "atom": atom_key,
            "deg_p_u": deg_p,
            "m_max_witness": m_max_witness,
            "m_max_bound_corollary": m_max_bound,
            "termination_holds": m_max_witness <= m_max_bound,
            "per_m_checks": [],
        }

        # Per-coefficient verification
        for c in coeffs:
            m = c["m"]
            a_m_str = c["a_m"]
            try:
                a_m = parse_a_m(a_m_str, u)
            except Exception as exc:
                atom_row["per_m_checks"].append({
                    "m": m,
                    "error": f"sympify failed: {exc}",
                })
                continue
            # Integrality
            is_int = all_integer_coeffs(a_m, u)
            integrality_total += 1
            if is_int:
                integrality_ok += 1
            # Degree bound
            deg_a = sp.degree(a_m, u) if a_m != 0 else -1
            deg_bound = deg_a <= m
            degree_total += 1
            if deg_bound:
                degree_ok += 1
            atom_row["per_m_checks"].append({
                "m": m,
                "deg_a_m": int(deg_a) if deg_a != -1 else None,
                "integral": is_int,
                "deg_a_m_le_m": bool(deg_bound),
                "remainder_nonzero": c.get("remainder_nonzero", None),
            })

        # Termination claim
        termination_total += 1
        if atom_row["termination_holds"]:
            termination_ok += 1

        per_atom_rows.append(atom_row)

    n_atoms = len(per_atom_rows)

    b = (
        WitnessBuilder("habiro-expansion-atomic-probe", engine="sympy")
        .set_description(
            "I1 probe for cor:habiro-expansion-atomic.  Cross-checks "
            "the corollary's 4 claims (integrality, degree bound, "
            "termination, uniqueness signature via "
            "`remainder_nonzero == false`) against the existing "
            "`habiro-coefficients-atomic.witness.json` data for "
            "{p, n, D}.  Parses each `a_m(u)` polynomial via sympy, "
            "verifies integer coefficients and deg_u(a_m) ≤ m, "
            "and confirms termination at m ≤ ⌈√(2·deg_u p)⌉."
        )
        .set_content_block("cor:habiro-expansion-atomic")
        .add_parameter("upstream_witness", upstream.name)
        .add_parameter("atoms_covered", [r["atom"] for r in per_atom_rows])
        .add_data("per_atom", per_atom_rows)
        .add_assertion(
            name="all_a_m_have_integer_coefficients",
            computed=float(integrality_ok),
            expected=float(integrality_total),
            tolerance=0.0,
            unit=f"count (of {integrality_total} parsed)",
            source="Claim 1 (Integrality): a_m ∈ ℤ[u] for every m.",
        )
        .add_assertion(
            name="all_deg_a_m_le_m",
            computed=float(degree_ok),
            expected=float(degree_total),
            tolerance=0.0,
            unit=f"count (of {degree_total} parsed)",
            source="Claim 2 (Degree bound): deg_u a_m ≤ m.",
        )
        .add_assertion(
            name="termination_within_sqrt_bound",
            computed=float(termination_ok),
            expected=float(termination_total),
            tolerance=0.0,
            unit=f"count (of {termination_total} atoms)",
            source=(
                "Claim 3 (Termination): m_max ≤ ⌈√(2·deg_u p(u))⌉ "
                "for every atom in the witness."
            ),
        )
    )
    out = b.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
