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

    Step-2 compatibility: also compute the **Galois norm**
    N(Frob_p) = Σ_{k coprime to 2p} Frob_p evaluated at ζ_{2p}^k.
    For Frob_p ∈ Z[ζ_{2p}] this norm is a rational integer; the
    `galois_norm_integrality_residual` field measures how close the
    computed sum is to the nearest integer (a necessary condition
    for Frob_p to be a true cyclotomic-integer Frobenius value).
    """
    u = sp.symbols("u")
    coeffs = record_data["habiro_coefficients"]

    # Pre-parse all a_m coefficients into integer lists once.
    a_m_int_lists: list[tuple[int, list[int]]] = []
    for c in coeffs:
        m = int(c["m"])
        if m >= 2 * p:
            break
        a_m_str = str(c["a_m"])
        a_m_expr = sp.sympify(a_m_str)
        try:
            poly = sp.Poly(a_m_expr, u)
            int_coeffs = [int(coef) for coef in poly.all_coeffs()]
        except (sp.PolynomialError, ValueError):
            int_coeffs = []  # signal fallback
        a_m_int_lists.append((m, int_coeffs))

    truncate_at: int | None = (
        2 * p if 2 * p <= len(coeffs) else None
    )

    def evaluate_at(u_val: complex) -> complex:
        total: complex = 0 + 0j
        for m, int_coeffs in a_m_int_lists:
            if int_coeffs:
                a_m_val: complex = 0 + 0j
                for k in int_coeffs:
                    a_m_val = a_m_val * u_val + k
            else:
                a_m_val = complex(
                    sp.N(sp.sympify(coeffs[m]["a_m"]).subs(u, u_val), digits)
                )
            total += a_m_val * cyclotomic_pochhammer_numeric(u_val, m)
        return total

    zeta_2p = primitive_root_of_unity_numeric(2 * p)
    frob_p_main = evaluate_at(zeta_2p)

    # Galois orbit: {ζ_{2p}^k : gcd(k, 2p) = 1}, |orbit| = φ(2p).
    from math import gcd, log
    galois_orbit_ks = [k for k in range(1, 2 * p) if gcd(k, 2 * p) == 1]
    galois_orbit_abs: list[float] = []
    galois_norm: complex = 0 + 0j
    for k in galois_orbit_ks:
        v = evaluate_at(zeta_2p ** k)
        galois_norm += v
        galois_orbit_abs.append(abs(v))

    # Weil bound: for a pure motive of weight w at prime p,
    # |σ(Frob_p)| = p^{w/2} for ALL σ in the Galois orbit.
    # Compute the spread of |σ(Frob_p)| values; if it's narrow,
    # the motive is "pure" at that prime and the inferred weight
    # is w = 2 · log_p(|Frob_p|).
    if galois_orbit_abs:
        max_abs = max(galois_orbit_abs)
        min_abs = min(galois_orbit_abs)
        spread = (max_abs - min_abs) / max_abs if max_abs > 1e-10 else 0.0
        if max_abs > 1e-10:
            inferred_weight = 2 * log(max_abs) / log(p)
        else:
            inferred_weight = None
    else:
        spread = None
        inferred_weight = None

    nearest_int = round(galois_norm.real)
    integrality_residual = abs(galois_norm.real - nearest_int)
    imag_residual = abs(galois_norm.imag)

    n_nonzero = len(a_m_int_lists)

    return {
        "prime": p,
        "u_root": f"zeta_{2*p}",
        "frob_p_complex": {
            "real": frob_p_main.real,
            "imag": frob_p_main.imag,
        },
        "abs_frob_p": abs(frob_p_main),
        "pochhammer_truncates_at_m": truncate_at,
        "n_contributions": n_nonzero,
        "galois_orbit_size": len(galois_orbit_ks),
        "galois_norm_real": galois_norm.real,
        "galois_norm_nearest_int": nearest_int,
        "galois_norm_integrality_residual": integrality_residual,
        "galois_norm_imag_residual": imag_residual,
        "is_integral": (
            integrality_residual < 1e-6 and imag_residual < 1e-6
            and truncate_at is not None
        ),
        "weil_orbit_abs_max": max(galois_orbit_abs) if galois_orbit_abs else None,
        "weil_orbit_abs_min": min(galois_orbit_abs) if galois_orbit_abs else None,
        "weil_orbit_spread": spread,
        "weil_inferred_weight": inferred_weight,
        "weil_pure_at_p": (
            spread is not None and spread < 1e-3
            and truncate_at is not None
        ),
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
            integrality = "✓" if row["is_integral"] else " "
            pure = "♦" if row["weil_pure_at_p"] else " "
            wt = (f"w≈{row['weil_inferred_weight']:.2f}"
                  if row["weil_inferred_weight"] is not None else "w=?")
            print(f"    p = {p:>3}  m_trunc = "
                  f"{row['pochhammer_truncates_at_m']}  "
                  f"|Frob| = {row['abs_frob_p']:>8.4f}  "
                  f"N≈{row['galois_norm_nearest_int']:>+6d} {integrality}  "
                  f"spread={row['weil_orbit_spread']:.2e} {pure} {wt}")
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
            "Step 2 (in progress): Galois-norm integrality is the first "
            "finite-place reciprocity check; this witness records "
            "N(Frob_p) = Σ_{k coprime to 2p} Frob_p(ζ_{2p}^k). For "
            "Frob_p ∈ Z[ζ_{2p}] this norm is a rational integer; the "
            "`galois_norm_integrality_residual` field flags any deviation. "
            "Remaining step-2 work: cross-prime compatibility "
            "(Frob_p restricted to subfields agrees with Frob_q for "
            "q | p−1) and Weil/Deligne archimedean behaviour.",
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
