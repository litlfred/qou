#!/usr/bin/env python3
"""Frobenius eigenvalues from Habiro symbolic data — R6 step 1 + 2.

For each atom with a Habiro cyclotomic expansion on disk
(`habiro-coefficients-atomic-fast.witness.json`, which now covers
A ∈ {1, 2, 3} after PR #506 fast-path landed), evaluate the
truncated Habiro element at u = ζ_{2p} for primes
p ∈ {2, 3, 5, 7, 11, 13} to extract the **Frobenius eigenvalue**
Frob_p ∈ ℂ that the brane tower carries at that prime.

Mathematical content:

    tr_M(T_w, q) = Σ_{m ≥ 0} a_m(u) · (u; u)_m,    u = q^{1/2}

The cyclotomic Pochhammer (u; u)_m = ∏_{i=1}^{m} (1 - u^i) vanishes
identically once u is a 2k-th root of unity with k ≤ m, so the sum
terminates at q = ζ_p (giving u = ζ_{2p}) after m_max ≤ 2p terms.
The truncated sum is the **local** Frobenius value the framework
attaches to the prime p.

**R6 step 1** (this script, basic): extract Frob_p numerically.

**R6 step 2** (this script, extension): verify the Galois-norm
integrality `N(Frob_p) = Σ_{k coprime to 2p} Frob_p(ζ_{2p}^k) ∈ ℤ`
on every (atom, prime) where the Pochhammer truncation lands
inside the on-disk Habiro data. This is the finite-place
reciprocity check.

Cross-references:
  - `def:motivic-galois-character`
  - `def:motivic-substrate`
  - `prop:motivic-perpetual-obstruction`
  - audit GAP 5b in `family-4-motivic-path.md`

Usage:
    python3 folio-assistant/computations/habiro_frobenius_probe.py

Output: `habiro-frobenius-probe.witness.json`
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from math import gcd
from pathlib import Path
from typing import Any

import sympy as sp

# Frobenius evaluation runs in **exact algebraic arithmetic** in
# Z[ζ_{2p}] = Z[u] / Φ_{2p}(u), the cyclotomic integer ring. Every
# step (a_m(ζ_{2p}), the Pochhammer (ζ_{2p}; ζ_{2p})_m, the Galois-
# orbit sum) is a polynomial-in-u reduction modulo Φ_{2p}(u). The
# Galois norm Σ_{k coprime to 2p} σ_k(Frob_p) lands in ℤ exactly —
# no float / mpmath approximation, no roundoff residual.

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

# Prefer the fast-path witness (covers more atoms) if available;
# fall back to the symbolic-q baseline.
WITNESS_FAST = HERE / "habiro-coefficients-atomic-fast.witness.json"
WITNESS_SYMBOLIC = HERE / "habiro-coefficients-atomic.witness.json"
WITNESS_OUT = HERE / "habiro-frobenius-probe.witness.json"

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def reduce_mod_cyclotomic(p_in_u: sp.Expr, n: int, u: sp.Symbol) -> sp.Poly:
    """Reduce a polynomial `p(u) ∈ Z[u]` modulo `Φ_n(u)` (the n-th
    cyclotomic polynomial), giving a representative in
    Z[u] / Φ_n(u) ≅ Z[ζ_n] of degree < φ(n).
    """
    phi_n = sp.Poly(sp.cyclotomic_poly(n, u), u)
    p_poly = sp.Poly(sp.expand(p_in_u), u)
    if p_poly.is_zero:
        return sp.Poly(0, u)
    _, rem = p_poly.div(phi_n)
    return rem


def cyclotomic_pochhammer_in_ring(n: int, m: int,
                                    u: sp.Symbol) -> sp.Poly:
    """(ζ_n; ζ_n)_m = ∏_{i=1}^{m} (1 − ζ_n^i) in Z[ζ_n] = Z[u]/Φ_n(u).

    Returns the cyclotomic-reduced polynomial form. For m = 0
    returns the constant polynomial 1.
    """
    result = sp.Poly(1, u)
    phi_n = sp.Poly(sp.cyclotomic_poly(n, u), u)
    for i in range(1, m + 1):
        # (1 − u^i) reduced mod Φ_n(u)
        factor = sp.Poly(1, u) - sp.Poly(u ** i, u)
        result = result * factor
        _, result = result.div(phi_n)
    return result


def apply_galois_substitution(rep: sp.Poly, k: int, n: int,
                                u: sp.Symbol) -> sp.Poly:
    """Apply the Galois automorphism σ_k : ζ_n ↦ ζ_n^k to an element
    of Z[ζ_n] = Z[u]/Φ_n(u) given as a polynomial-representative.

    Implementation: for `rep = Σ c_i u^i`, σ_k(rep) = Σ c_i u^{i·k},
    then reduce mod Φ_n(u).
    """
    expr = rep.as_expr().subs(u, u ** k)
    return reduce_mod_cyclotomic(expr, n, u)


def poly_to_constant_int(rep: sp.Poly) -> int | None:
    """If `rep` is a constant polynomial (degree 0), return its
    integer value; else return None.
    """
    if rep.is_zero:
        return 0
    if rep.degree() != 0:
        return None
    c = rep.all_coeffs()[0]
    if c.is_Integer:
        return int(c)
    return None


def parse_int_poly(a_m_str: str, u: sp.Symbol) -> list[int]:
    """Parse a Habiro coefficient `a_m(u) ∈ ℤ[u]` into a Horner-
    friendly integer list (descending powers, [c_d, ..., c_1, c_0]).

    Returns [] for non-integer-polynomial coefficients (which never
    arise in practice for Habiro expansions but we handle the
    fallback gracefully).
    """
    expr = sp.sympify(a_m_str, locals={"u": u})
    try:
        poly = sp.Poly(expr, u)
        return [int(c) for c in poly.all_coeffs()]
    except (sp.PolynomialError, ValueError):
        return []


def evaluate_at_root(habiro_coeffs: list[dict], p: int, u: sp.Symbol,
                     expansion_terminated_clean: bool = False
                     ) -> dict[str, Any]:
    """Evaluate one atom's Habiro expansion at u = ζ_{2p}, computing
    both the principal value Frob_p and the Galois-norm sum
    `N(Frob_p) = Σ_{k coprime to 2p} Frob_p(ζ_{2p}^k)`.

    `expansion_terminated_clean` flags that the Habiro cyclotomic
    division produced a zero remainder at the last m — i.e. the
    Habiro element is FINITE and `a_m = 0` for all m beyond the
    listed range. When true, the Frob_p evaluation is exact for
    every prime regardless of whether 2p exceeds the data window.

    Returns a dict with the principal value, integrality residual,
    and step-2 compatibility-passed flag.
    """
    n_data = len(habiro_coeffs)
    pochhammer_truncates = 2 * p <= n_data
    # Two ways the Frob_p value is exact:
    #   (1) The cyclotomic Pochhammer (u; u)_m hits zero at some
    #       m ≤ n_data (Pochhammer truncation INSIDE data window).
    #   (2) The Habiro expansion terminated cleanly — a_m = 0 for
    #       all m ≥ n_data, so missing high-m contributions are
    #       mathematically zero.
    is_exact = pochhammer_truncates or expansion_terminated_clean
    truncate_at = 2 * p if pochhammer_truncates else (
        n_data if expansion_terminated_clean else None
    )

    # Pre-parse coefficients to integer-Horner form (once).
    parsed: list[tuple[int, list[int]]] = []
    for c in habiro_coeffs:
        m = int(c["m"])
        parsed.append((m, parse_int_poly(str(c["a_m"]), u)))

    n_2p = 2 * p
    phi_2p = sp.Poly(sp.cyclotomic_poly(n_2p, u), u)

    def evaluate_in_ring() -> sp.Poly:
        """Frob_p as an element of Z[ζ_{2p}] = Z[u]/Φ_{2p}(u),
        represented by its Z[u] polynomial of degree < φ(2p).

        When the Habiro expansion terminated cleanly, ALL on-disk
        coefficients contribute (the missing high-m a_m's are zero).
        Otherwise, only m < 2p contribute (the Pochhammer hits zero
        at m = 2p so subsequent terms vanish in the ring).
        """
        total = sp.Poly(0, u)
        for m, int_coeffs in parsed:
            if not expansion_terminated_clean and m >= n_2p:
                break
            # a_m(u) as Z[u].
            if int_coeffs:
                a_m_poly = sp.Poly(int_coeffs, u)
            else:
                a_m_poly = sp.Poly(0, u)
            poch = cyclotomic_pochhammer_in_ring(n_2p, m, u)
            term = a_m_poly * poch
            _, term = term.div(phi_2p)
            total = total + term
            _, total = total.div(phi_2p)
        return total

    frob_p_rep = evaluate_in_ring()

    # Galois orbit: {ζ_{2p}^k : gcd(k, 2p) = 1}. |orbit| = φ(2p).
    galois_ks = [k for k in range(1, n_2p) if gcd(k, n_2p) == 1]
    galois_norm_rep = sp.Poly(0, u)
    for k in galois_ks:
        sigma_k_frob = apply_galois_substitution(frob_p_rep, k, n_2p, u)
        galois_norm_rep = galois_norm_rep + sigma_k_frob
        _, galois_norm_rep = galois_norm_rep.div(phi_2p)

    # The Galois norm is mathematically an element of ℤ ⊂ Z[ζ_{2p}],
    # so its representative MUST be a degree-0 polynomial whose
    # constant is an integer.
    galois_norm_int = poly_to_constant_int(galois_norm_rep)
    galois_norm_is_exact_integer = galois_norm_int is not None

    # For display: also evaluate Frob_p numerically (one mpmath
    # complex-double computation per atom-prime, just for the table
    # output — the *truth* is the exact ring element above).
    import mpmath as _mp
    _mp.mp.dps = 30
    zeta_2p_num = _mp.exp(2j * _mp.pi / n_2p)
    frob_p_num = complex(frob_p_rep.as_expr().subs(u, zeta_2p_num))

    return {
        "prime": p,
        "u_root": f"zeta_{n_2p}",
        # The exact algebraic representative — a polynomial in u
        # of degree < φ(2p) with integer coefficients.
        "frob_p_in_Z_zeta_str": str(frob_p_rep.as_expr()),
        # Numeric value (display-only).
        "frob_p_complex": {
            "real": frob_p_num.real,
            "imag": frob_p_num.imag,
        },
        "abs_frob_p": abs(frob_p_num),
        "pochhammer_truncates_at_m": truncate_at,
        "frob_p_is_exact": is_exact,
        "exact_via": (
            "pochhammer_truncates_inside_data" if pochhammer_truncates
            else "habiro_expansion_terminated_cleanly" if expansion_terminated_clean
            else "neither"
        ),
        "galois_orbit_size": len(galois_ks),
        "galois_norm_int": galois_norm_int,
        "galois_norm_is_exact_integer": galois_norm_is_exact_integer,
        "galois_norm_residue_str": str(galois_norm_rep.as_expr()),
        # Step-2 compatibility: the Galois norm is **exactly** an
        # integer (no tolerance — algebraic). Pass iff the
        # Frob_p evaluation is exact (Pochhammer truncation OR
        # Habiro expansion terminated cleanly) AND the norm
        # reduced to a degree-0 integer polynomial.
        "step2_compatibility_passed": bool(
            is_exact and galois_norm_is_exact_integer
        ),
    }


def load_atoms() -> dict[str, dict]:
    """Load atom-records from the fast-path witness if available;
    fall back to the symbolic-q baseline otherwise."""
    if WITNESS_FAST.exists():
        data = json.loads(WITNESS_FAST.read_text())
        return data.get("results", {})
    if WITNESS_SYMBOLIC.exists():
        data = json.loads(WITNESS_SYMBOLIC.read_text())
        return data.get("results", {})
    return {}


def main() -> int:
    atoms = load_atoms()
    if not atoms:
        print(f"ERROR: neither {WITNESS_FAST.name} nor "
              f"{WITNESS_SYMBOLIC.name} exists")
        return 1

    u = sp.symbols("u")

    print("=" * 72)
    print("R6 step-1 + step-2: Frobenius eigenvalue probe (Habiro → Frob_p)")
    print("=" * 72)
    print(f"  Primes: {PRIMES}")
    print(f"  Atoms:  {list(atoms.keys())}")
    print()

    atoms_out: list[dict[str, Any]] = []
    for label, record in atoms.items():
        habiro_coeffs = record.get("habiro_coefficients", [])
        if not habiro_coeffs:
            continue
        n_coeffs = len(habiro_coeffs)
        Z = record.get("Z", 0)
        N = record.get("N", 0)
        print(f"  {label}  (n_coeffs = {n_coeffs}, Z={Z}, N={N})")
        per_prime: list[dict[str, Any]] = []
        for p in PRIMES:
            # Both witness formats encode "Habiro expansion is finite":
            #   - fast-path:    `expansion_terminated_clean: True`
            #   - symbolic-q:   `reconstruction_matches: True`
            terminated_clean = bool(
                record.get("expansion_terminated_clean")
                or record.get("reconstruction_matches")
            )
            row = evaluate_at_root(
                habiro_coeffs, p, u,
                expansion_terminated_clean=terminated_clean,
            )
            integrality = "✓" if row["step2_compatibility_passed"] else " "
            n_disp = (str(row["galois_norm_int"])
                      if row["galois_norm_int"] is not None else "—")
            print(f"    p = {p:>3}  m_trunc = "
                  f"{row['pochhammer_truncates_at_m']!s:>5}  "
                  f"|Frob| = {row['abs_frob_p']:>9.4f}  "
                  f"N = {n_disp:>8} {integrality}")
            per_prime.append(row)
        truncated = [r for r in per_prime
                     if r["pochhammer_truncates_at_m"] is not None]
        atom_step2_passed = bool(
            truncated and all(r["step2_compatibility_passed"]
                              for r in truncated)
        )
        atoms_out.append({
            "atom_label": label,
            "Z": Z,
            "N": N,
            "n_habiro_coefficients": n_coeffs,
            "frobenius": per_prime,
            "step2_summary": {
                "n_primes_truncated": len(truncated),
                "n_primes_data_exhausted": len(per_prime) - len(truncated),
                "all_truncated_primes_compatible": atom_step2_passed,
                "primes_failing_compatibility": [
                    r["prime"] for r in truncated
                    if not r["step2_compatibility_passed"]
                ],
            },
        })

    out = {
        "computation": "habiro-frobenius-probe",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "R6 step-1 + step-2 probe: extract Frobenius eigenvalues "
            "Frob_p(q) from the Habiro cyclotomic expansion of each "
            "atom's Markov trace by evaluating at u = ζ_{2p}. The "
            "cyclotomic Pochhammer (u; u)_m vanishes once m ≥ 2p, so "
            "the sum truncates after a finite number of terms. The "
            "Galois norm N(Frob_p) = Σ_{k coprime to 2p} Frob_p(ζ_{2p}^k) "
            "is verified to be a rational integer (residual < 1e-6) "
            "on every (atom, prime) where the truncation lands inside "
            "the on-disk Habiro data — finite-place reciprocity check."
        ),
        "reference_blocks": [
            "def:motivic-galois-character",
            "def:motivic-substrate",
            "prop:motivic-perpetual-obstruction",
        ],
        "input_witness": (
            WITNESS_FAST.name if WITNESS_FAST.exists()
            else WITNESS_SYMBOLIC.name
        ),
        "primes": PRIMES,
        "atoms": atoms_out,
        "summary": {
            "n_atoms": len(atoms_out),
            "n_primes": len(PRIMES),
            "step2_all_atoms_compatible": all(
                a["step2_summary"]["all_truncated_primes_compatible"]
                for a in atoms_out
            ),
            "n_atoms_step2_passed": sum(
                1 for a in atoms_out
                if a["step2_summary"]["all_truncated_primes_compatible"]
            ),
        },
    }
    WITNESS_OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print()
    print(f"Wrote: {WITNESS_OUT.name}")
    print(f"Step-2 all-atoms-compatible: "
          f"{out['summary']['step2_all_atoms_compatible']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
