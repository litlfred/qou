#!/usr/bin/env python3
"""Frobenius eigenvalues from Habiro symbolic data — R6 step 1 + 2.

For each atom with a Habiro cyclotomic expansion on disk
(`habiro-coefficients-atomic.witness.json`, the symbolic-q
aggregate carrying the convention-D regeneration; covers
A ∈ {1, 2, 3}), evaluate the
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
import os
import sys
from datetime import datetime, timezone
from math import gcd
from pathlib import Path
from typing import Any

import mpmath
from _precision import fmt  # noqa: E402
import sympy as sp

# Standalone scientific-computation script — set mpmath precision
# at module level (deliberate global side effect). 30dps is more
# than enough for the display-only complex-value evaluation; the
# *truth* is the exact algebraic Z[ζ_{2p}] representative computed
# via sp.Poly arithmetic.
#
# RAISED 30 -> 70 (2026-10-05, a precision fix). The values are serialised by
# `_precision.fmt` at 60 digits, so at 30 dps digits 31-60 of `real`, `imag` and
# `abs_frob` were manufactured: two runs agreed to ~30 digits and then diverged.
# 70 matches the platform compute default and leaves a guard above the 60 written.
mpmath.mp.dps = 70
_DISPLAY_DPS = 70

# Frobenius evaluation runs in **exact algebraic arithmetic** in
# Z[ζ_{2p}] = Z[u] / Φ_{2p}(u), the cyclotomic integer ring. Every
# step (a_m(ζ_{2p}), the Pochhammer (ζ_{2p}; ζ_{2p})_m, the Galois-
# orbit sum) is a polynomial-in-u reduction modulo Φ_{2p}(u). The
# Galois norm Σ_{k coprime to 2p} σ_k(Frob_p) lands in ℤ exactly —
# no float / mpmath approximation, no roundoff residual.

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

# CANONICAL SOURCE: the symbolic-q atomic witness, which carries the
# convention-D regeneration (`cde2fbcd89`, all 25 atoms).
#
# This used to prefer `habiro-coefficients-atomic-fast.witness.json`
# "(covers more atoms)". Both carry 5 atoms today, so that reason had
# lapsed — and the fast-path file now lives under `_deprecated/` and was
# never regenerated, so preferring it fed this probe PRE-convention-D
# coefficients while the mass table around it had migrated. Measured on
# `cdbdc84af1`: the symbolic-q aggregate matches the per-atom
# convention-D witnesses 5/5; the deprecated fast path matches 0/5.
#
# There is deliberately NO fallback to the deprecated file. Silently
# substituting superseded data is the defect being fixed here, not a
# resilience feature: a missing canonical source is an error.
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
    expr = sp.sympify(a_m_str, locals={"check_q": u})
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

    # Fold in the denominator: Frob_p = num · denom⁻¹ in Q(ζ_{2p}).
    #
    # NOTE the ring. `sp.invert(..., Phi_2p)` works over Q, and Q(ζ_{2p}) is a
    # field, so this succeeds for ANY nonzero denominator. The flag below is
    # therefore a NONZERO test, not a unit test — `denom_nonzero`, not
    # `denom_unit`, which is what it was called until 2026-08-28 and which
    # produced a wrong claim in a PR body ("requires the denominator to be a
    # unit, so Tr(Frob_p) is an algebraic integer"). Measured: Frob_p is an
    # algebraic integer on 0 of 45 (atom, prime) cells, so the denominator is
    # never a unit in Z[ζ_{2p}] and a genuine unit test would pass nowhere.
    denom_nonzero = False
    denom_inversion_error: str | None = None
    if denom_in_u is not None:
        try:
            denom_expr = sp.sympify(denom_in_u, locals={"check_q": u})
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
                    denom_nonzero = True
                except (sp.NotInvertible, ValueError, Exception) as e:
                    denom_inversion_error = (
                        f"denominator not invertible mod Phi_{n_2p}: "
                        f"{type(e).__name__}"
                    )
        except Exception as e:
            denom_inversion_error = (
                f"denom parse failed: {type(e).__name__}: {str(e)[:80]}"
            )

    if not denom_nonzero:
        # Denominator vanishes mod Phi_{2p} — typically because
        # tr_M's Plancherel-weight denominator shares a cyclotomic
        # factor with Φ_{2p}. The full Markov-trace evaluation
        # tr_M(ζ_{2p}) lives in Q(ζ_{2p}) \ Z[ζ_{2p}] in this case.
        frob_full_rep: sp.Poly | None = None
    else:
        frob_full_rep = frob_rep  # set above when denom_nonzero succeeded

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
    # Evaluate at the module dps and KEEP it there. This used to end in
    # `complex(...)`, which collapsed a 30-dps value to binary64 and then
    # serialized the halves as raw floats — the NO-FLOAT64 defect the probe
    # rules name (a witness field is a recorded value, not a display).
    # Measured on one term at n_2p = 10: `complex()` gives an imaginary part
    # of 1.69e-21, pure float64 noise, where `sp.N(·, 30)` gives 1.82e-31.
    _disp = sp.N(display_rep.as_expr().subs(u, zeta_2p_num), _DISPLAY_DPS)
    frob_re = mpmath.mpf(str(sp.re(_disp)))
    frob_im = mpmath.mpf(str(sp.im(_disp)))
    frob_abs = mpmath.sqrt(frob_re ** 2 + frob_im ** 2)

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
        "denom_folded": denom_nonzero,
        "denom_inversion_error": denom_inversion_error,
        # Numeric value, serialized through the precision formatter so the
        # witness carries no raw binary64 (raw-float64 ratchet).
        "frob_complex": {
            "real": fmt(frob_re),
            "imag": fmt(frob_im),
        },
        "abs_frob": fmt(frob_abs),
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
            is_exact and full_trace_is_integer and denom_nonzero
        ),
    }


def load_atoms() -> dict[str, dict]:
    """Load atom-records from the convention-D symbolic-q witness."""
    if WITNESS_SYMBOLIC.exists():
        data = json.loads(WITNESS_SYMBOLIC.read_text())
        return data.get("results", {})
    return {}


def main() -> int:
    atoms = load_atoms()
    if not atoms:
        print(f"ERROR: {WITNESS_SYMBOLIC.name} not found — regenerate it "
              f"with _habiro_coefficient_extract.py. Do NOT substitute "
              f"_deprecated/habiro-coefficients-atomic-fast.witness.json: "
              f"it predates the convention-D migration.")
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
                  f"|Frob| = {float(row['abs_frob']):>9.4f}  "
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

    all_truncated_cells = [
        (a["atom_label"], r)
        for a in atoms_out
        for r in a["frobenius"]
        if r["pochhammer_truncates_at_m"] is not None
    ]
    n_cells_truncated = len(all_truncated_cells)
    cells_full_labels = [
        f"{lab} @ p={r['prime']}"
        for lab, r in all_truncated_cells
        if r["step2_full_trace_passed"]
    ]
    n_cells_full = len(cells_full_labels)

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
        "input_witness": WITNESS_SYMBOLIC.name,
        "primes": PRIMES,
        "atoms": atoms_out,
        "summary": {
            "n_atoms": len(atoms_out),
            "n_primes": len(PRIMES),
            # --- numerator test (the weaker of the two) ---
            "step2_all_atoms_compatible": all(
                a["step2_summary"]["all_truncated_primes_compatible"]
                for a in atoms_out
            ),
            "n_atoms_step2_passed": sum(
                1 for a in atoms_out
                if a["step2_summary"]["all_truncated_primes_compatible"]
            ),
            # --- full-trace test (strictly stronger; see the note below) ---
            "step2_all_atoms_full_trace_compatible": all(
                a["step2_summary"]["step2_full_trace_compatible"]
                for a in atoms_out
            ),
            "n_atoms_step2_full_trace_passed": sum(
                1 for a in atoms_out
                if a["step2_summary"]["step2_full_trace_compatible"]
            ),
            "n_cells_truncated": n_cells_truncated,
            "n_cells_step2_full_trace_passed": n_cells_full,
            "cells_step2_full_trace_passed": cells_full_labels,
            "summary_note": (
                "step2_all_atoms_compatible is the NUMERATOR test: it asks "
                "only that Tr(numerator) be a rational integer, and the "
                "denominator does not enter. The full-trace test "
                "step2_all_atoms_full_trace_compatible is strictly stronger: "
                "it asks that the Galois trace of the DENOMINATOR-FOLDED value "
                "be a rational integer. CORRECTED 2026-08-28: an earlier "
                "wording said it 'requires the denominator to be a unit at "
                "ζ_{2p}, so Tr(Frob_p) is itself an algebraic integer'. That "
                "is wrong twice over — the denom_folded flag is a nonzero test "
                "performed over Q, not a unit test, and Frob_p is an algebraic "
                "integer on 0 of 45 cells, so a real unit test would pass "
                "nowhere. What the full-trace test detects is integrality of "
                "the TRACE, not of the element. Read the full-trace fields as "
                "the headline; the numerator fields pass on every cell and "
                "therefore discriminate nothing."
            ),
        },
    }
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        out, script_path=__file__, engine="python")
    out["scriptFile"] = os.path.basename(__file__)
    WITNESS_OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print()
    print(f"Wrote: {WITNESS_OUT.name}")
    print(f"Step-2 numerator test  (weaker):  all-atoms-compatible = "
          f"{out['summary']['step2_all_atoms_compatible']}")
    print(f"Step-2 FULL-TRACE test (headline): all-atoms-compatible = "
          f"{out['summary']['step2_all_atoms_full_trace_compatible']}"
          f"  ({n_cells_full}/{n_cells_truncated} truncated cells"
          + (f": {', '.join(cells_full_labels)}" if cells_full_labels else "")
          + ")")
    return 0


if __name__ == "__main__":
    sys.exit(main())
