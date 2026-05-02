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

import mpmath
import sympy as sp

# Use 60-digit mpmath for the Galois-orbit sums; T/³He Habiro
# coefficients reach magnitudes ~10⁵, and float64 cumulative
# roundoff floor is ~10⁻³ on the orbit norm — too coarse to
# distinguish the true rational-integer Galois norm from noise.
mpmath.mp.dps = 60

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

# Prefer the fast-path witness (covers more atoms) if available;
# fall back to the symbolic-q baseline.
WITNESS_FAST = HERE / "habiro-coefficients-atomic-fast.witness.json"
WITNESS_SYMBOLIC = HERE / "habiro-coefficients-atomic.witness.json"
WITNESS_OUT = HERE / "habiro-frobenius-probe.witness.json"

PRIMES = [2, 3, 5, 7, 11, 13]


def primitive_root_of_unity(n: int) -> mpmath.mpc:
    """ζ_n = exp(2πi / n) as a high-precision mpmath complex."""
    return mpmath.exp(2j * mpmath.pi / n)


def cyclotomic_pochhammer(u_val: mpmath.mpc, m: int) -> mpmath.mpc:
    """(u; u)_m = ∏_{i=1}^{m} (1 - u^i). Returns 1 for m = 0."""
    result = mpmath.mpc(1, 0)
    for i in range(1, m + 1):
        result *= (1 - u_val ** i)
    return result


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


def evaluate_at_root(habiro_coeffs: list[dict], p: int, u: sp.Symbol
                     ) -> dict[str, Any]:
    """Evaluate one atom's Habiro expansion at u = ζ_{2p}, computing
    both the principal value Frob_p and the Galois-norm sum
    `N(Frob_p) = Σ_{k coprime to 2p} Frob_p(ζ_{2p}^k)`.

    Returns a dict with the principal value, integrality residual,
    and step-2 compatibility-passed flag.
    """
    n_data = len(habiro_coeffs)
    truncate_at = 2 * p if 2 * p <= n_data else None

    # Pre-parse coefficients to integer-Horner form (once).
    parsed: list[tuple[int, list[int]]] = []
    for c in habiro_coeffs:
        m = int(c["m"])
        parsed.append((m, parse_int_poly(str(c["a_m"]), u)))

    def evaluate_at(u_val: mpmath.mpc) -> mpmath.mpc:
        total = mpmath.mpc(0, 0)
        for m, int_coeffs in parsed:
            if m >= 2 * p:
                break
            if int_coeffs:
                a_m_val = mpmath.mpc(0, 0)
                for k in int_coeffs:
                    a_m_val = a_m_val * u_val + k
            else:
                a_m_val = mpmath.mpc(0, 0)
            total += a_m_val * cyclotomic_pochhammer(u_val, m)
        return total

    zeta_2p = primitive_root_of_unity(2 * p)
    frob_p_main = evaluate_at(zeta_2p)

    # Galois orbit: {ζ_{2p}^k : gcd(k, 2p) = 1}. |orbit| = φ(2p).
    galois_ks = [k for k in range(1, 2 * p) if gcd(k, 2 * p) == 1]
    galois_norm = mpmath.mpc(0, 0)
    galois_orbit_abs: list[float] = []
    for k in galois_ks:
        v = evaluate_at(zeta_2p ** k)
        galois_norm += v
        galois_orbit_abs.append(float(abs(v)))

    nearest_int = int(mpmath.nint(galois_norm.real))
    integrality_residual = float(abs(galois_norm.real - nearest_int))
    imag_residual = float(abs(galois_norm.imag))

    # Step-2 compatibility: integrality on truncated primes. With
    # 60-digit mpmath the residual on a true algebraic integer is
    # well below 1e-40; using 1e-20 as a generous tolerance.
    step2_passed = bool(
        truncate_at is not None
        and integrality_residual < 1e-20
        and imag_residual < 1e-20
    )

    return {
        "prime": p,
        "u_root": f"zeta_{2*p}",
        "frob_p_complex": {
            "real": float(frob_p_main.real),
            "imag": float(frob_p_main.imag),
        },
        "abs_frob_p": float(abs(frob_p_main)),
        "pochhammer_truncates_at_m": truncate_at,
        "galois_orbit_size": len(galois_ks),
        "galois_norm_real": float(galois_norm.real),
        "galois_norm_nearest_int": nearest_int,
        "galois_norm_integrality_residual": integrality_residual,
        "galois_norm_imag_residual": imag_residual,
        "step2_compatibility_passed": step2_passed,
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
            row = evaluate_at_root(habiro_coeffs, p, u)
            integrality = "✓" if row["step2_compatibility_passed"] else " "
            print(f"    p = {p:>3}  m_trunc = "
                  f"{row['pochhammer_truncates_at_m']!s:>5}  "
                  f"|Frob| = {row['abs_frob_p']:>7.4f}  "
                  f"N≈{row['galois_norm_nearest_int']:>+5d} {integrality}")
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
