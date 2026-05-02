#!/usr/bin/env python3
"""
CONVENTION NOTE:  Plancherel weights w_λ = d_q(λ)² / [n]_q! are
used throughout; these give the CANONICAL trace, not the Jones-
Ocneanu Markov trace with z = 1/(q^{1/2}+q^{-1/2}).  See
markov_weight_verification.py for the q-dependent divergence.

Compute D's Wedderburn profile: per-partition character of D's atom
braid at q₀.

Decomposition: H_n(q) = ⊕_{λ ⊢ n} End(V_λ).  For D, n = 3A = 6
(3-strand particle model with A = 2 nucleons + atomic electron).

Partitions of 6 and their special roles:
  (6)                  = sym       (eigenvalue +q on every σ_i)
  (1, 1, 1, 1, 1, 1)   = alt       (eigenvalue -q⁻¹ on every σ_i)
  others               = mixed / std-type

For each partition λ:
  * dim V_λ  (classical)
  * dim_q V_λ  (quantum dim)
  * w_λ = dim_q(λ)² / [n]_q!   (Plancherel weight)
  * χ_λ(β_D)  (character of D's atom braid at q₀)
  * contribution to Markov trace: w_λ · χ_λ / dim_λ

If χ_alt(β_D) = 0 → "alt block unpopulated" claim is verified, the
1.09% must live elsewhere (Kashaev tail, pentagon defects, knot
assignment).  If χ_alt(β_D) ≠ 0 with numerical value ≈ 0.0108 →
the ρ_F rule needs fractional correction.
"""
from __future__ import annotations

import sys
import json
import warnings
import cmath
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore", category=UserWarning)

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
import sympy as sp

# P2.5 migration: helper available; per-witness expose_polynomial call is a follow-up
import sys as _p25_sys
from pathlib import Path as _P25Path
_p25_sys.path.insert(0, str(_P25Path(__file__).parent))
from witness_polynomial import expose_polynomial  # noqa: F401
from scipy.sparse import issparse, eye as speye

from hecke_characters import partitions_of, dim_q, qfac
from mass_at_3A_proper import _cached_seminormal, atom_braid_word_3A
from q_parameter import Q as Q0, HA as H_VAL


def is_alt_partition(shape: tuple) -> bool:
    """(1,1,...,1) is the alternating partition."""
    return all(s == 1 for s in shape)


def is_sym_partition(shape: tuple, n: int) -> bool:
    """(n,) is the symmetric partition."""
    return shape == (n,)


_NUMERIC_SIGMAS_CACHE: dict[tuple, tuple[list, int]] = {}


def _numeric_sigmas_for_shape(shape: tuple):
    """Return (sigmas_num, dim) for shape, caching across calls so that
    the expensive lambdify/subs work happens ONCE per partition even
    when chi_lambda_at_q0 is called many times in the outer loop.
    """
    if shape in _NUMERIC_SIGMAS_CACHE:
        return _NUMERIC_SIGMAS_CACHE[shape]
    sigmas, dim, _syts = _cached_seminormal(shape)
    if dim == 0:
        _NUMERIC_SIGMAS_CACHE[shape] = ([], 0)
        return [], 0
    q_sym = sp.Symbol('q')
    sigmas_num = []
    for S in sigmas:
        if hasattr(S, "toarray"):
            S_arr = S.toarray()
        else:
            S_arr = np.asarray(S)
        S_mat = sp.Matrix(S_arr)
        try:
            numeric_fn = sp.lambdify(q_sym, S_mat, modules="numpy")
            arr = np.asarray(numeric_fn(complex(Q0)), dtype=complex)
        except Exception:
            arr = np.empty((dim, dim), dtype=complex)
            for i in range(dim):
                for j in range(dim):
                    elem = S_arr[i, j]
                    if hasattr(elem, "subs"):
                        arr[i, j] = complex(sp.N(elem.subs(q_sym, Q0)))
                    else:
                        arr[i, j] = complex(elem)
        sigmas_num.append(arr)
    _NUMERIC_SIGMAS_CACHE[shape] = (sigmas_num, dim)
    return sigmas_num, dim


def chi_lambda_at_q0(shape: tuple, word) -> complex:
    """Character χ_λ(W) in the λ-irrep at q = q₀, numerically."""
    sigmas_num, dim = _numeric_sigmas_for_shape(shape)
    if dim == 0:
        return 0.0 + 0j
    I = np.eye(dim, dtype=complex)
    prod = I.copy()
    for (c, d, g) in word:
        if g < len(sigmas_num):
            prod = prod @ (c * sigmas_num[g] + d * I)
        else:
            return 0.0 + 0j
    return complex(np.trace(prod))


def main() -> int:
    print("=" * 100)
    print("D's WEDDERBURN PROFILE — per-partition character of the atom braid")
    print(f"  q₀ = {Q0}   h = {H_VAL}")
    print("=" * 100)

    Z, N = 1, 1
    A = Z + N
    n = 3 * A   # 6 strands
    word = atom_braid_word_3A(Z, N)
    print(f"\n  Atom: D (Z={Z}, N={N}, A={A}, n = 3A = {n} strands)")
    print(f"  Atom braid: {len(word)} Hecke factors")

    parts = list(partitions_of(n))
    q_sym = sp.Symbol('q')
    # qfac / dim_q return floats at q = Q0
    nfac_q0 = complex(float(qfac(n)))
    print(f"  Partitions of {n}: {len(parts)}")
    print(f"  [n]_q! at q₀:   {nfac_q0.real:.4f}")

    print(f"\n  {'partition':<16} {'role':>8} {'dim':>4} "
          f"{'dim_q':>10} {'w_λ':>10} {'χ_λ(β_D)':>14} "
          f"{'contribution':>14}")
    print("  " + "-" * 96)

    results = []
    markov_total = 0 + 0j
    for shape in parts:
        # Classical and quantum dim
        sigmas, dim, _ = _cached_seminormal(shape)
        if dim == 0:
            continue
        dq = complex(float(dim_q(shape)))
        w_lambda = (dq * dq) / nfac_q0
        chi_lam = chi_lambda_at_q0(shape, word)
        # Normalise by quantum dim so τ(1) = Σ w_λ · d_q/d_q = Σ w_λ
        # is consistent at q ≠ 1 (classical dim gives an offset).
        contribution = w_lambda * chi_lam / dq
        markov_total += contribution
        role = ""
        if is_sym_partition(shape, n):
            role = "sym"
        elif is_alt_partition(shape):
            role = "alt"
        else:
            role = "mixed"
        print(f"  {str(shape):<16} {role:>8} {dim:>4} "
              f"{dq.real:>+10.4f} {w_lambda.real:>+10.4f} "
              f"{chi_lam.real:>+10.4f}{chi_lam.imag:+.2e}j "
              f"{contribution.real:>+10.4e}{contribution.imag:+.1e}j")
        results.append({
            "shape": list(shape),
            "role": role,
            "dim": dim,
            "dim_q_q0": str(dq),
            "w_lambda_q0": str(w_lambda),
            "chi_q0": str(chi_lam),
            "contribution": str(contribution),
        })

    print(f"\n  Σ contributions = Markov trace of D at q₀:")
    print(f"    total         = {markov_total}")
    print(f"    |total|       = {abs(markov_total):.10f}")
    print(f"    Re(total)     = {markov_total.real:+.10f}")

    # Cross-check with binding_canonical: tr_M_atom(D) ≈ 0.3883 from
    # witness (Plancherel-weighted).  If close → Plancherel path is
    # consistent.
    try:
        witness_path = Path(__file__).parent / "binding-canonical.witness.json"
        bc = json.loads(witness_path.read_text())
        tr_atom = complex(bc["results"][0]["tr_M_atom"])
        print(f"\n  Cross-check: binding_canonical tr_M_atom(D) = {tr_atom}")
        print(f"    |Re ratio| = {abs(markov_total.real/tr_atom.real) if tr_atom.real else 'nan'}")
    except Exception as e:
        print(f"\n  (cross-check failed: {e})")

    # Extract the alt-partition character
    alt_row = next(r for r in results if r["role"] == "alt")
    sym_row = next(r for r in results if r["role"] == "sym")
    print(f"\n  ALT partition (1^{n}):")
    print(f"    dim: {alt_row['dim']}")
    print(f"    χ_alt(β_D) at q₀: {alt_row['chi_q0']}")
    print(f"    contribution: {alt_row['contribution']}")
    alt_chi = complex(alt_row['chi_q0'])
    print(f"    |χ_alt| numerical: {abs(alt_chi):.10f}")

    print(f"\n  SYM partition ({n},):")
    print(f"    dim: {sym_row['dim']}")
    print(f"    χ_sym(β_D) at q₀: {sym_row['chi_q0']}")
    print(f"    contribution: {sym_row['contribution']}")

    # Interpretation
    print(f"\n  {'=' * 70}")
    print("  INTERPRETATION")
    print(f"  {'=' * 70}")
    print(f"  The ρ_F rule says: alt block unpopulated → ρ_F = m_e.")
    print(f"  If χ_alt(β_D) = 0 exactly, rule is consistent for D.")
    print(f"  If |χ_alt(β_D)| ≈ 0.0108, this matches the residual ratio")
    print(f"  (B_AME/B_pred - 1 = -0.01078), and the ρ_F rule needs")
    print(f"  a fractional correction ρ_F = m_e · (1 - |χ_alt|).")

    witness = {
        "computation": "d-wedderburn-profile",
        "description": (
            "Per-partition character χ_λ(β_D) at q₀ for every "
            "partition λ of n = 3A = 6.  Tests the conjectured "
            "ρ_F = m_e rule for D by checking whether the alt "
            "partition (1,1,...,1) is unpopulated (χ = 0) or "
            "lightly populated (χ small but nonzero)."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "Z": Z, "N": N, "A": A, "n_strands": n,
            "q_0": Q0,
        },
        # P2.5: sympy-as-matrix-stepping-stone pattern.  This script
        # uses sp.Symbol('q') only inside _numeric_sigmas_for_shape
        # to build Hoefsmit seminormal matrices ρ_λ(σ_i) ∈ Mat(ℚ(q));
        # each matrix is then immediately lambdified at q = q_0 and
        # the downstream products / traces run in numpy.  Per-trace
        # χ_λ(β_D) values are numerical specialisations, not Laurent
        # polynomials in q.
        "symbolic_q_form": {
            "engine": "sympy (matrix construction only) + numpy",
            "q_symbol": "q (sp.Symbol('q'))",
            "pattern_note": (
                "sympy-as-matrix-stepping-stone: ρ_λ(σ_i) ∈ "
                "Mat_{d_λ × d_λ}(ℚ(q)) is symbolic in "
                "_numeric_sigmas_for_shape; the lambdify-at-q_0 step "
                "eagerly converts to numpy before computing products.  "
                "Per-trace χ_λ(β_D) values reported here are numerical "
                "specialisations at q = q_0, not Laurent polynomials in q."
            ),
            "symbolic_source": "hecke_characters.build_seminormal_matrices",
            "specialisation_point": "q = q_0",
        },
        "partitions": results,
        "markov_trace_total": str(markov_total),
        "alt_chi_abs": str(abs(alt_chi)),
    }
    out = Path(__file__).parent / "d-wedderburn-profile.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
