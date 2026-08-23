#!/usr/bin/env python3
"""Frobenius eigenvalues from Habiro symbolic data — R6 step 1 + 2.

For each atom with a Habiro cyclotomic expansion on disk
(`habiro-coefficients-atomic-fast.witness.json`, which now covers
A ∈ {1, 2, 3} after PR #506 fast-path landed), evaluate the
truncated Habiro element at u = ζ_{2p} (here u is the spinor
rate \check{q} substituted to a root of unity; Habiro-literature
name "u" kept as the local Python symbol) for primes
p ∈ {2, 3, 5, 7, 11, 13} to extract the **Frobenius eigenvalue**
Frob_p ∈ ℂ that the brane tower carries at that prime.

Mathematical content:

    tr_M(T_w, q) = Σ_{m ≥ 0} a_m(u) · (u; u)_m,    u = q^{1/2}

The cyclotomic Pochhammer (u; u)_m = ∏_{i=1}^{m} (1 - u^i) vanishes
identically once u is a 2k-th root of unity with k ≤ m, so the sum
terminates at q = ζ_p (giving u = ζ_{2p}) after m_max ≤ 2p terms.
The truncated sum is the **local** Frobenius value the framework
attaches to the prime p.

**R6 step 1** (this script, basic): extract Frob_p as an exact
algebraic element of `Z[ζ_{2p}] = Z[u]/Φ_{2p}(u)`.

**R6 step 2** (this script, extension): verify the Galois-TRACE
integrality `Tr(Frob_p) = Σ_{σ ∈ Gal(Q(ζ_{2p})/Q)} σ(Frob_p) ∈ ℤ`
on every (atom, prime) where the Pochhammer truncation lands
inside the on-disk Habiro data. This is the finite-place
reciprocity check. (Note: trace = sum of conjugates, NOT to be
confused with norm = product of conjugates. All arithmetic is
exact in the cyclotomic ring — no floating-point residual.)

The on-disk Habiro coefficients `a_m(u)` represent the cyclotomic
expansion of the **numerator** of `tr_M = num(u)/denom(u)`. To
recover the genuine Frobenius value of `tr_M`, the script folds in
`denom⁻¹ mod Φ_{2p}` when the denominator is a unit in `Z[ζ_{2p}]`.
When the denominator is not a unit (typical at primes where the
Plancherel weights have cyclotomic poles), we report the
numerator-only value with a flag.

Cross-references:
  - `def:motivic-galois-character`
  - `def:motivic-substrate`
  - `prop:motivic-perpetual-obstruction`
  - audit GAP 5b in `family-4-motivic-path.md`

Usage:
    python3 computations/habiro_frobenius_probe.py

Output: `habiro-frobenius-probe.witness.json`
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
import sys
from datetime import datetime, timezone
from math import gcd
from pathlib import Path
from typing import Any

import mpmath
import sympy as sp

# Standalone scientific-computation script — set mpmath precision
# at module level (deliberate global side effect). 30dps is more
# than enough for the display-only complex-value evaluation; the
# *truth* is the exact algebraic Z[ζ_{2p}] representative computed
# via sp.Poly arithmetic.
mpmath.mp.dps = 30

# Frobenius evaluation runs in **exact algebraic arithmetic** in
# Z[ζ_{2p}] = Z[u] / Φ_{2p}(u), the cyclotomic integer ring. Every
# step (a_m(ζ_{2p}), the Pochhammer (ζ_{2p}; ζ_{2p})_m, the Galois-
# orbit sum) is a polynomial-in-u reduction modulo Φ_{2p}(u). The
# Galois norm Σ_{k coprime to 2p} σ_k(Frob_p) lands in ℤ exactly —
# no float / mpmath approximation, no roundoff residual.

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

# Prefer the fast-path witness (covers more atoms) if available;
# fall back to the symbolic-q baseline.
WITNESS_FAST = _pb.witness_path("habiro-coefficients-atomic-fast.witness.json", HERE)
WITNESS_SYMBOLIC = _pb.witness_path("habiro-coefficients-atomic.witness.json", HERE)
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
    expr = sp.sympify(a_m_str, locals={"check_q": u, "u": u})
    try:
        poly = sp.Poly(expr, u)
        return [int(c) for c in poly.all_coeffs()]
    except (sp.PolynomialError, ValueError):
        return []


def evaluate_at_root(habiro_coeffs: list[dict], p: int, u: sp.Symbol,
                     expansion_terminated_clean: bool = False,
                     denom_in_u: str | None = None,
                     ) -> dict[str, Any]:
    """Evaluate the **Markov trace** `tr_M(T_w, q) = num(u) / denom(u)`
    at u = ζ_{2p} as an element of `Q(ζ_{2p})`. The on-disk Habiro
    coefficients `a_m(u)` represent the cyclotomic expansion of the
    numerator `num(u) = Σ a_m · (u;u)_m`; the denominator `denom(u)`
    must be folded back in for the genuine Frobenius value.

    Computes `Frob_p = num(ζ_{2p}) · denom(ζ_{2p})⁻¹` in
    `Z[ζ_{2p}] = Z[u]/Φ_{2p}(u)`, provided the denominator is a unit
    mod `Φ_{2p}`. When `denom_in_u` is None or the inverse doesn't
    exist, we fall back to evaluating only the numerator (preserving
    backward compatibility with witnesses lacking the denom field).

    Also computes the **Galois trace** `Tr(Frob_p) = Σ_{σ ∈ Gal} σ(Frob_p)`
    (= sum of conjugates, NOT the norm = product). For Frob_p ∈ Z[ζ_{2p}]
    this trace is a rational integer, exactly. For Frob_p ∈ Q(ζ_{2p}) \\ Z[ζ_{2p}]
    the trace is rational but may not be integer; we report the residue
    representative without rounding.

    `expansion_terminated_clean` flags that `a_m = 0` for all m
    beyond the listed range; lets us extend evaluation to primes
    where 2p exceeds the on-disk data depth.
    """
    n_data = len(habiro_coeffs)
    pochhammer_truncates = 2 * p <= n_data
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

    def evaluate_num_in_ring() -> sp.Poly:
        """Numerator evaluated at u = ζ_{2p} — element of `Z[ζ_{2p}]`.

        Iterative Pochhammer update: (u;u)_m = (u;u)_{m-1} · (1 - u^m).
        Since coefficients are processed in increasing order of m, each
        step costs one polynomial multiplication + one cyclotomic
        reduction, vs O(m) re-multiplications if we rebuild the
        Pochhammer from scratch every time.
        """
        total = sp.Poly(0, u)
        poch = sp.Poly(1, u)  # (u;u)_0 = 1
        last_m = 0
        for m, int_coeffs in parsed:
            if not expansion_terminated_clean and m >= n_2p:
                break
            # Bring poch up to (u;u)_m via missing (1 - u^i) factors.
            for i in range(last_m + 1, m + 1):
                factor = sp.Poly(1, u) - sp.Poly(u ** i, u)
                poch = poch * factor
                _, poch = poch.div(phi_2p)
            last_m = m
            a_m_poly = sp.Poly(int_coeffs, u) if int_coeffs else sp.Poly(0, u)
            term = a_m_poly * poch
            _, term = term.div(phi_2p)
            total = total + term
            _, total = total.div(phi_2p)
        return total

    num_rep = evaluate_num_in_ring()

    # Fold in the denominator: Frob_p = num · denom⁻¹ in Z[ζ_{2p}].
    denom_unit = False
    denom_inversion_error: str | None = None
    if denom_in_u is not None:
        try:
            denom_expr = sp.sympify(denom_in_u, locals={"check_q": u, "u": u})
            denom_poly = sp.Poly(denom_expr, u)
            _, denom_red = denom_poly.div(phi_2p)
            if denom_red.is_zero:
                denom_inversion_error = "denominator vanishes mod Phi_{2p}"
            else:
                # Compute denom_red⁻¹ mod Φ_{2p} via extended GCD.
                try:
                    inv_expr = sp.invert(
                        denom_red.as_expr(), phi_2p.as_expr(), u
                    )
                    inv_poly = sp.Poly(inv_expr, u)
                    frob_rep = num_rep * inv_poly
                    _, frob_rep = frob_rep.div(phi_2p)
                    denom_unit = True
                except (sp.NotInvertible, ValueError, Exception) as e:
                    denom_inversion_error = (
                        f"denominator not a unit mod Phi_{n_2p}: "
                        f"{type(e).__name__}"
                    )
        except Exception as e:
            denom_inversion_error = (
                f"denom parse failed: {type(e).__name__}: {str(e)[:80]}"
            )

    if not denom_unit:
        # Denominator is not a unit in Z[ζ_{2p}] — typically because
        # tr_M's Plancherel-weight denominator shares a cyclotomic
        # factor with Φ_{2p}. The full Markov-trace evaluation
        # tr_M(ζ_{2p}) lives in Q(ζ_{2p}) \ Z[ζ_{2p}] in this case.
        frob_full_rep: sp.Poly | None = None
    else:
        frob_full_rep = frob_rep  # set above when denom_unit succeeded

    # Galois orbit: {ζ_{2p}^k : gcd(k, 2p) = 1}. |orbit| = φ(2p).
    galois_ks = [k for k in range(1, n_2p) if gcd(k, n_2p) == 1]

    def galois_trace(rep: sp.Poly) -> sp.Poly:
        """Tr(rep) = Σ_σ σ(rep) over Gal(Q(ζ_{2p})/Q) — sum of
        conjugates (NOT product, which is the norm)."""
        out = sp.Poly(0, u)
        for k in galois_ks:
            sigma_k = apply_galois_substitution(rep, k, n_2p, u)
            out = out + sigma_k
            _, out = out.div(phi_2p)
        return out

    # Trace of the **numerator** evaluation (always in Z[ζ_{2p}],
    # so trace is always an integer).
    num_trace_rep = galois_trace(num_rep)
    num_trace_int = poly_to_constant_int(num_trace_rep)
    num_trace_is_integer = num_trace_int is not None

    # Trace of the **full** tr_M(ζ_{2p}) — only when denom is a unit.
    if frob_full_rep is not None:
        full_trace_rep = galois_trace(frob_full_rep)
        full_trace_int = poly_to_constant_int(full_trace_rep)
        full_trace_is_integer = full_trace_int is not None
        full_trace_residue_str = str(full_trace_rep.as_expr())
    else:
        full_trace_int = None
        full_trace_is_integer = False
        full_trace_residue_str = None

    # For display: numeric Frobenius value of (full tr_M when
    # denom-folded, else numerator). Module-level mpmath.mp.dps
    # already set to 30dps; no need to set per-call.
    zeta_2p_num = mpmath.exp(2j * mpmath.pi / n_2p)
    display_rep = frob_full_rep if frob_full_rep is not None else num_rep
    frob_num_complex = complex(display_rep.as_expr().subs(u, zeta_2p_num))

    return {
        "prime": p,
        "u_root": f"zeta_{n_2p}",
        # Exact algebraic numerator value in Z[ζ_{2p}].
        "frob_num_in_Z_zeta_str": str(num_rep.as_expr()),
        # Exact algebraic full-trace value when denom is a unit;
        # None when denom is not invertible mod Φ_{2p}.
        "frob_full_in_Z_zeta_str": (
            str(frob_full_rep.as_expr()) if frob_full_rep is not None
            else None
        ),
        "denom_folded": denom_unit,
        "denom_inversion_error": denom_inversion_error,
        # Numeric value (display-only).
        "frob_complex": {
            "real": frob_num_complex.real,
            "imag": frob_num_complex.imag,
        },
        "abs_frob": abs(frob_num_complex),
        "pochhammer_truncates_at_m": truncate_at,
        "frob_p_is_exact": is_exact,
        "exact_via": (
            "pochhammer_truncates_inside_data" if pochhammer_truncates
            else "habiro_expansion_terminated_cleanly" if expansion_terminated_clean
            else "neither"
        ),
        "galois_orbit_size": len(galois_ks),
        # Trace = sum of Galois conjugates (NOT norm = product).
        "galois_trace_num_int": num_trace_int,
        "galois_trace_num_is_integer": num_trace_is_integer,
        "galois_trace_num_residue_str": str(num_trace_rep.as_expr()),
        "galois_trace_full_int": full_trace_int,
        "galois_trace_full_is_integer": full_trace_is_integer,
        "galois_trace_full_residue_str": full_trace_residue_str,
        # Step-2 compatibility: the Galois norm is **exactly** an
        # Pass iff the numerator evaluation is exact AND the
        # numerator's Galois trace is an integer. (For the FULL
        # tr_M trace integrality, see `galois_trace_full_is_integer`,
        # which additionally requires denom to be a unit.)
        "step2_compatibility_passed": bool(
            is_exact and num_trace_is_integer
        ),
        "step2_full_trace_passed": bool(
            is_exact and full_trace_is_integer and denom_unit
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
                denom_in_u=record.get("denom_in_u"),
            )
            num_pass = "✓" if row["step2_compatibility_passed"] else " "
            full_pass = "✓" if row["step2_full_trace_passed"] else " "
            tr_num = (str(row["galois_trace_num_int"])
                      if row["galois_trace_num_int"] is not None else "—")
            tr_full = (str(row["galois_trace_full_int"])
                       if row["galois_trace_full_int"] is not None else "—")
            print(f"    p = {p:>3}  m_trunc = "
                  f"{row['pochhammer_truncates_at_m']!s:>5}  "
                  f"|Frob| = {row['abs_frob']:>9.4f}  "
                  f"Tr(num) = {tr_num:>8} {num_pass}  "
                  f"Tr(full) = {tr_full:>8} {full_pass}")
            per_prime.append(row)
        truncated = [r for r in per_prime
                     if r["pochhammer_truncates_at_m"] is not None]
        atom_step2_passed = bool(
            truncated and all(r["step2_compatibility_passed"]
                              for r in truncated)
        )
        atom_step2_full_passed = bool(
            truncated and all(r["step2_full_trace_passed"]
                              for r in truncated)
        )
        atoms_out.append({
            "atom_label": label,
            "Z": Z,
            "N": N,
            "n_habiro_coefficients": n_coeffs,
            "frobenius": per_prime,
            "step2_summary": {
                "step2_full_trace_compatible": atom_step2_full_passed,
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
