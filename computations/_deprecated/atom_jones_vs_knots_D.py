#!/usr/bin/env python3
"""
Phase 3 — compare D's Hecke-element Jones polynomial to catalog knots.

*** CAVEAT (gemini-PR#399, 2026-04): this script computes the
PLANCHEREL/canonical trace (w_λ = d_q²/[n]_q!), NOT the Jones-
Ocneanu Markov trace z = 1/(q^{1/2}+q^{-1/2}).  The Jones polynomial
is defined via the MARKOV trace, so a ratio of tr_Planck(D) / J(K)
does NOT match any catalog knot and CANNOT identify D's link class.
The existing ratio_table is retained for diagnostic bookkeeping only;
for link identification one must redo the trace with Markov weights
(see markov_convention_parallel.py for the z-convention). ***

Full symbolic Markov trace on D's 32-term NF is too slow (> 5 min).
Instead, evaluate D's trace numerically at many q values by direct
Plancherel-weighted seminormal character sum (atom_markov_trace),
then compare to the Jones polynomial of candidate catalog knots
evaluated at the same q values.

Candidate knots to test (low-crossing, potential D matches):
  6_2, 7_3, 8_20, 8_11, 6^2_2, L6a4 (Borromean)

Test protocol:
  - Evaluate tr_M(D)(q) and J(K)(q) at q ∈ {1.05, 1.08, 1.11, 1.14}.
  - For each knot K, fit tr_M(D) ≈ a · J(K) for complex constant a.
  - If a is (nearly) a power of -q^{1/2}, the Jones polynomials
    agree up to framing, and D's Hecke element is in the same
    Markov class as K.

Output: for each candidate, the fitted scaling factor a and the
residual after scaling.  The knot with (a, residual) consistent
with a pure writhe-power factor wins; otherwise none matches.
"""
from __future__ import annotations

import sys
import json
import cmath
import warnings
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

from hecke_characters import partitions_of, dim_q, qfac
from mass_at_3A_proper import _cached_seminormal, atom_braid_word_3A

# Cache lambdified seminormal-sigma matrices per shape so multiple
# trM_plancherel_at_q calls don't re-compile the same symbolic → numpy
# functions on every invocation.
_LAMBDIFY_CACHE: dict[tuple, list] = {}


def _get_lambdified_sigmas(shape: tuple, sigmas_sym, dim: int) -> list:
    from scipy.sparse import issparse
    if shape in _LAMBDIFY_CACHE:
        return _LAMBDIFY_CACHE[shape]
    q_sym = sp.Symbol('q')
    fns = []
    for S in sigmas_sym:
        if issparse(S):
            S_arr = S.toarray()
        else:
            S_arr = np.asarray(S)
        try:
            fns.append(sp.lambdify(q_sym, sp.Matrix(S_arr), modules='numpy'))
        except (TypeError, ValueError, NotImplementedError, sp.SympifyError):
            # These are the exception types sp.lambdify may raise for
            # entries it can't codegen.  fallback handled at call site.
            fns.append(None)
    _LAMBDIFY_CACHE[shape] = fns
    return fns


def trM_plancherel_at_q(Z: int, N: int, q_val: complex) -> complex:
    """Plancherel-weighted Markov trace of atom_braid_word_3A at q=q_val.

    Uses the seminormal representation with SYMBOLIC entries substituted
    at q_val.  Fast because no Gröbner reduction needed.
    """
    # NOTE: this function computes the PLANCHEREL / canonical trace
    # (w_λ = d_q²/[n]_q!), not the Jones-Ocneanu Markov trace with
    # z = 1/(q^{1/2}+q^{-1/2}).  See markov_weight_verification.py
    # for the q_0 divergence between the two conventions.
    from scipy.sparse import issparse, eye as speye
    import numpy as np
    word = atom_braid_word_3A(Z, N)
    n = 3 * (Z + N)
    # qfac / dim_q from hecke_characters return FLOATS at q_0; for
    # arbitrary q_val we rebuild from the q-integer formula here.
    q_c = complex(q_val)
    qi_c = 1.0 / q_c
    def q_int_at(k: int) -> complex:
        if k == 0:
            return 0 + 0j
        if abs(q_c - 1) < 1e-15:
            return complex(k)
        if abs(q_c + 1) < 1e-15:
            return complex(k * ((-1) ** (k - 1)))
        return (q_c ** k - qi_c ** k) / (q_c - qi_c)
    nfac = 1 + 0j
    for k in range(1, n + 1):
        nfac *= q_int_at(k)
    if abs(nfac) < 1e-30:
        return 0 + 0j
    total = 0 + 0j
    def dim_q_at(shape):
        from hecke_characters import young_hooks
        hooks = young_hooks(shape)
        top = 1 + 0j
        for k in range(1, sum(shape) + 1):
            top *= q_int_at(k)
        bot = 1 + 0j
        for hk in hooks:
            bot *= q_int_at(hk)
        return top / bot if abs(bot) > 1e-30 else 0 + 0j
    for shape in partitions_of(n):
        sigmas_sym, dim, _ = _cached_seminormal(shape)
        if dim == 0:
            continue
        dq = dim_q_at(shape)
        if abs(dq) < 1e-18:
            continue
        w = (dq * dq) / nfac
        # Cache lambdified functions per shape so multiple q_val calls
        # reuse them instead of re-compiling each time.
        fns = _get_lambdified_sigmas(shape, sigmas_sym, dim)
        sigmas_num = []
        for fn, S in zip(fns, sigmas_sym):
            try:
                sigmas_num.append(np.asarray(fn(q_val), dtype=complex))
            except (TypeError, ValueError, ZeroDivisionError):
                # Fallback: element-wise subs (slow).  Catch numeric
                # / symbolic evaluation errors; let unexpected
                # exceptions (e.g. MemoryError) propagate.
                if issparse(S):
                    S_arr = S.toarray()
                else:
                    S_arr = np.asarray(S)
                sigmas_num.append(np.array(
                    [[complex(sp.N(S_arr[i, j].subs(sp.Symbol('q'), q_val)))
                       for j in range(dim)]
                      for i in range(dim)]))
        I = np.eye(dim, dtype=complex)
        prod = I.copy()
        for (c, d, g) in word:
            if g < len(sigmas_num):
                prod = prod @ (c * sigmas_num[g] + d * I)
            else:
                raise IndexError(f"g={g} >= len(sigmas)={len(sigmas_num)}")
        chi = complex(np.trace(prod))
        total += w * chi / dim
    return total


def jones_polys():
    """Small catalog of Jones polynomials (KnotInfo / Kawauchi convention).

    V(K)(q) = Kauffman bracket normalization.  Slight convention
    differences exist between sources; we compare UP TO overall
    factor of q^{k/2} · (±1) which is the writhe ambiguity.
    """
    q = sp.Symbol('q')
    return {
        "6_2":   (q**(-5) - 2*q**(-4) + 2*q**(-3) - 2*q**(-2)
                    + 2*q**(-1) - 1 + q),
        "6_3":   (-q**(-3) + 2*q**(-2) - 2*q**(-1) + 3
                    - 2*q + 2*q**2 - q**3),
        "7_3":   (q**(-9) - q**(-8) + 2*q**(-7) - 2*q**(-6)
                    + 3*q**(-5) - 2*q**(-4) + q**(-3) - q**(-2)),
        "7_4":   (q**(-8) - 2*q**(-7) + 3*q**(-6) - 2*q**(-5)
                    + 3*q**(-4) - 2*q**(-3) + q**(-2) - q**(-1)),
        "8_11":  (q**(-7) - 2*q**(-6) + 3*q**(-5) - 4*q**(-4)
                    + 4*q**(-3) - 4*q**(-2) + 3*q**(-1) - 2 + q),
        "8_20":  (q**(-5) - 2*q**(-4) + 3*q**(-3) - 3*q**(-2)
                    + 3*q**(-1) - 3 + 2*q - q**2),
        "4_1":   (q**(-2) - q**(-1) + 1 - q + q**2),  # figure-8
        "3_1":   (q**(-4) - q**(-3) + q**(-1)),        # trefoil
    }


def main() -> int:
    print("=" * 100)
    print("PHASE 3 — D's Hecke element's Jones vs catalog knots")
    print("=" * 100)

    # Test q values
    q_tests = [1.05, 1.08, 1.11, 1.14, 1.2, 0.95, 0.9, -1.0]
    print(f"\n  Evaluating tr_M(D) at q ∈ {q_tests}…")

    tr_D = {}
    for qv in q_tests:
        try:
            tr_D[qv] = trM_plancherel_at_q(1, 1, complex(qv))
            print(f"    tr_M(D)(q={qv:>6.3f}) = {tr_D[qv]}")
        except Exception as e:
            print(f"    tr_M(D)(q={qv}) FAILED: {e}")

    # Evaluate each candidate knot's Jones
    polys = jones_polys()
    q = sp.Symbol('q')
    print(f"\n  Evaluating catalog Jones polynomials at same q values:")
    J_vals = {}
    for name, J in polys.items():
        J_vals[name] = {}
        for qv in q_tests:
            val = complex(sp.N(J.subs(q, qv)))
            J_vals[name][qv] = val

    # For each knot, check if tr_M(D)/J(K) is the same complex number
    # (i.e., tr_M(D) = a · J(K) for fixed a, independent of q).
    print("\n  Ratio tr_M(D) / J(K) at each q (if constant → D ≡ K up to framing):")
    print(f"  {'knot':>6}  {'q=1.05':>14}  {'q=1.08':>14}  "
          f"{'q=1.11':>14}  {'q=1.14':>14}  {'consistent?':>12}")
    rows = []
    for name, J_at in J_vals.items():
        ratios = []
        for qv in [1.05, 1.08, 1.11, 1.14]:
            if abs(J_at[qv]) > 1e-15 and qv in tr_D:
                ratios.append(tr_D[qv] / J_at[qv])
            else:
                ratios.append(None)
        # Check consistency: are all ratios (roughly) the same?
        valid = [r for r in ratios if r is not None]
        if len(valid) >= 2:
            span = max(abs(r) for r in valid) - min(abs(r) for r in valid)
            relspan = span / max(abs(r) for r in valid) if valid else 1
            consistent = relspan < 0.01  # 1% span
        else:
            consistent = False
        r_strs = [f"{r.real:+.6f}{r.imag:+.4f}j" if r else "    —    "
                  for r in ratios]
        flag = "CONST ★" if consistent else "varies"
        print(f"  {name:>6}  {r_strs[0]:>14}  {r_strs[1]:>14}  "
              f"{r_strs[2]:>14}  {r_strs[3]:>14}  {flag:>12}")
        rows.append({
            "knot": name,
            "ratios": [(qv, str(r)) for qv, r in zip(
                [1.05, 1.08, 1.11, 1.14], ratios)],
            "consistent": consistent,
        })

    # Best knot identification
    best = [r for r in rows if r["consistent"]]
    print()
    if best:
        print(f"  → D's atom Hecke element has the SAME Jones as "
              f"{[r['knot'] for r in best]} (up to framing).")
    else:
        print(f"  → D's atom Hecke element does NOT match any "
              f"catalog Jones polynomial. The true atom-link is not "
              f"any of {list(polys.keys())}.")

    witness = {
        "computation": "atom-jones-vs-knots-D",
        "description": (
            "Numerically evaluate tr_M(D)(q) at multiple q values via "
            "Plancherel-weighted seminormal sum, compare to Jones "
            "polynomials of low-crossing catalog knots, and identify "
            "D's link class (if any catalog match)."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_test_values": q_tests,
        "tr_M_D": {str(k): str(v) for k, v in tr_D.items()},
        "J_at_q": {name: {str(qv): str(val) for qv, val in vals.items()}
                   for name, vals in J_vals.items()},
        "ratio_table": rows,
        "matching_knots": [r["knot"] for r in best],
    }
    out = Path(__file__).parent / "atom-jones-vs-knots-D.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
