#!/usr/bin/env python3
"""R6 step-1 probe — Frobenius eigenvalues from Habiro symbolic data.

For each atom with a Habiro cyclotomic expansion on disk
(`habiro-coefficients-atomic.witness.json`), evaluate the Habiro
element at the primitive p-th root of unity ζ_p for small rational
primes p ∈ {2, 3, 5, 7, 11, 13}, producing the **Frobenius
eigenvalue** Frob_p ∈ ℂ that the brane tower carries at that prime.

Mathematical identity (Habiro, 2004):

    tr_M(T_w, q) = Σ_{m ≥ 0} a_m(u) · (u; u)_m,    u = q^{1/2}

The cyclotomic Pochhammer (u; u)_m = ∏_{i=1}^{m} (1 - u^i) vanishes
identically once u is a 2k-th root of unity with k ≤ m, so the sum
terminates at q = ζ_p (giving u = ζ_{2p}) after m_max ≤ 2p terms.
The truncated sum is the **local** Frobenius value the framework
attaches to the prime p. The fact that it depends only on the
cyclotomic class — not on the choice of representative — is the
"Habiro symbolic-in-q" guarantee.

This script does NOT discharge the `MotivicGaloisCharacter`
axiom-class instance: that requires the compatibility verifications
(Frobenius commutes with norms, satisfies Weil/Deligne reciprocity).
But it makes the Habiro → Frob_p map **explicit and tabulated**,
which is step 1 of the three-step plan in
`docs/audits/2026-05-02-queued-research.md` §R6.

Output: `habiro-frobenius-probe.witness.json`
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from habiro_types import HabiroAtomicWitness  # noqa: E402

WITNESS_IN = HERE / "habiro-coefficients-atomic.witness.json"
WITNESS_OUT = HERE / "habiro-frobenius-probe.witness.json"

PRIMES = [2, 3, 5, 7, 11, 13]


def primitive_root_of_unity_numeric(n: int) -> complex:
    """Return ζ_n = exp(2πi/n) as a high-precision complex value."""
    import cmath
    return cmath.exp(2j * cmath.pi / n)


def cyclotomic_pochhammer_numeric(u_val: complex, m: int) -> complex:
    """(u; u)_m = ∏_{i=1}^{m} (1 - u^i). Returns 1 for m = 0."""
    result = 1 + 0j
    for i in range(1, m + 1):
        result *= (1 - u_val**i)
    return result


def evaluate_at_root(record_data: dict, p: int, *,
                     digits: int = 15) -> dict[str, Any]:
    """Evaluate one atom's Habiro expansion at u = ζ_{2p} numerically.

    Symbolic approach is too slow on the larger Habiro coefficients;
    a 64-bit complex evaluation gives ample precision for the
    witness (the Frobenius eigenvalue is a finite cyclotomic integer
    and its complex value is exact up to machine epsilon).

    Uses 2p (not p) because u = q^{1/2}; q = ζ_p ⇒ u = ζ_{2p}.
    """
    u = sp.symbols("u")
    zeta_2p = primitive_root_of_unity_numeric(2 * p)
    coeffs = record_data["habiro_coefficients"]

    # Truncation: (zeta_{2p}; zeta_{2p})_m = 0 once 2p divides some i ≤ m,
    # i.e. m ≥ 2p. (More precisely the product hits zero whenever
    # zeta_{2p}^i = 1, i.e. i is a multiple of 2p.) So m_max = 2p - 1.
    truncate_at: int | None = None
    total: complex = 0 + 0j
    n_nonzero = 0

    for c in coeffs:
        m = int(c["m"])
        if m >= 2 * p:
            if truncate_at is None:
                truncate_at = m
            break
        # Evaluate a_m(zeta_{2p}) numerically.
        a_m_str = str(c["a_m"])
        a_m_expr = sp.sympify(a_m_str)
        # a_m is a polynomial in u with integer coefficients; substitute
        # numerically using sp.Poly to avoid sp.simplify on each term.
        try:
            poly = sp.Poly(a_m_expr, u)
            int_coeffs = [int(coef) for coef in poly.all_coeffs()]
            # Horner's method
            a_m_val: complex = 0 + 0j
            for k in int_coeffs:
                a_m_val = a_m_val * zeta_2p + k
        except (sp.PolynomialError, ValueError):
            a_m_val = complex(sp.N(a_m_expr.subs(u, zeta_2p), digits))
        poch = cyclotomic_pochhammer_numeric(zeta_2p, m)
        contrib = a_m_val * poch
        total += contrib
        if abs(contrib) > 1e-12:
            n_nonzero += 1

    return {
        "prime": p,
        "u_root": f"zeta_{2*p}",
        "frob_p_complex": {
            "real": total.real,
            "imag": total.imag,
        },
        "abs_frob_p": abs(total),
        "pochhammer_truncates_at_m": truncate_at,
        "n_contributions": n_nonzero,
    }


def main() -> int:
    if not WITNESS_IN.exists():
        print(f"ERROR: missing input witness {WITNESS_IN}")
        return 1

    witness_in = HabiroAtomicWitness.from_json(WITNESS_IN)
    raw = json.loads(WITNESS_IN.read_text())["results"]

    print("=" * 72)
    print("R6 step-1: Frobenius eigenvalue probe (Habiro → Frob_p)")
    print("=" * 72)
    print(f"  Input: {WITNESS_IN.name}")
    print(f"  Primes: {PRIMES}")
    print(f"  Atoms:  {len(witness_in.records)}")
    print()

    atoms_out: list[dict[str, Any]] = []
    for record in witness_in.records:
        label = record.atom_label
        record_data = raw[label]
        n_coeffs = len(record_data["habiro_coefficients"])
        print(f"  {label}  (n_coeffs = {n_coeffs})")
        per_prime: list[dict[str, Any]] = []
        for p in PRIMES:
            row = evaluate_at_root(record_data, p)
            print(f"    p = {p:>3}  m_trunc = "
                  f"{row['pochhammer_truncates_at_m']}  "
                  f"|Frob| = {row['abs_frob_p']:.6f}")
            per_prime.append(row)
        atoms_out.append({
            "atom_label": label,
            "Z": record.Z,
            "N": record.N,
            "n_habiro_coefficients": n_coeffs,
            "frobenius": per_prime,
        })

    out = {
        "computation": "habiro-frobenius-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "R6 step-1 probe: extract Frobenius eigenvalues Frob_p(q) "
            "from the Habiro cyclotomic expansion of each atom's "
            "Markov trace by evaluating at u = ζ_{2p}. The cyclotomic "
            "Pochhammer (u; u)_m vanishes once m ≥ 2p, so the sum "
            "truncates after a finite number of terms. This makes the "
            "Habiro → Frob_p map explicit and tabulated, which is the "
            "first concrete step toward the Habiro → MotivicGaloisCharacter "
            "instance (audit GAP 5b)."
        ),
        "reference_blocks": [
            "def:motivic-galois-character",
            "def:motivic-substrate",
            "prop:motivic-perpetual-obstruction",
        ],
        "input_witness": WITNESS_IN.name,
        "primes": PRIMES,
        "atoms": atoms_out,
        "summary": {
            "n_atoms": len(atoms_out),
            "n_primes": len(PRIMES),
            "atoms_with_full_truncation": sum(
                1 for a in atoms_out
                if all(p["pochhammer_truncates_at_m"] is not None
                       for p in a["frobenius"])
            ),
        },
        "next_steps": [
            "Step 2: verify Frobenius commutes with norms (finite-place "
            "reciprocity) and satisfies Weil/Deligne at archimedean place.",
            "Step 3: construct the explicit MotivicGaloisCharacter "
            "instance, discharging the axiom class for the QOU substrate.",
        ],
    }

    WITNESS_OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print()
    print(f"Wrote: {WITNESS_OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
