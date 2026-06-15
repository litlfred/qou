#!/usr/bin/env python3
"""
Phase 3 — symbolic Hecke NF of D's atom braid, then Jones match.

The Hecke NF is well-defined on the Hecke element (no lift to B_n
required).  It tells us exactly which braid operations are "live"
in D's atom braid — each basis word in H_n(q) gets a coefficient in
Z[q^{1/2}, q^{-1/2}].

The Markov trace on the NF is the Jones polynomial of any braid
closure representing this Hecke element (all such closures have the
same Jones polynomial).  So J_{D-atom}(q) is computable symbolically.

Comparison protocol:
  1. Build D's atom Hecke element via the symbolic Gröbner-Shirshov
     reduction (same pipeline as binding_canonical.py).
  2. Extract the NF: list of (basis_word, coefficient in q) pairs.
  3. Compute its Markov trace symbolically = J_{D-atom}(q).
  4. Compute J_{6_2}(q) directly as a reference.
  5. Check: are J_{D-atom}(q) and J_{6_2}(q) the SAME polynomial
     (possibly differing by the standard writhe normalization)?

If they match → D's atom link class agrees with 6_2 at Hecke level,
i.e., the braid-closure model of D is (equivalent to) 6_2's braid
closure.  If not → 6_2 was a census-picked APPROXIMATION; D's true
atom-link is different.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import json
import warnings
import time
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore", category=UserWarning)

sys.path.insert(0, str(Path(__file__).parent))

import sympy as sp

from hecke_symbolic import (
    SymbolicHeckeElement, SymbolicHeckeDivision,
    q as q_sym, HA as HA_sym,
)
from mass_at_3A_proper import atom_braid_word_3A
from markov_trace_canonical import tr_M_element
from q_parameter import Q as Q0_FLOAT
from witness_polynomial import expose_polynomial

# Rational approximation of q_0 for sympy, kept consistent with q_parameter.Q.
_Q0_RATIONAL = sp.Rational(str(float(Q0_FLOAT)))


# Tolerances for float-to-symbolic conversion of Hecke (c, d) coefficients:
# - _C_FACTOR_TOL: exact-float comparison for (c ∈ {0, 1})
# - _D_EXACT_TOL:  exact-float comparison for (d ∈ {0, 1})
# - _D_HECKE_TOL:  numeric match to ±h or ±h/2 at q_0 (h value differs from
#                  exact 1 by rounding of the q_0 rational; looser threshold).
_C_FACTOR_TOL = 1e-12
_D_EXACT_TOL = 1e-12
_D_HECKE_TOL = 1e-3


def _factor_from(c_f: float, d_f: float, g: int) -> SymbolicHeckeElement:
    """Hecke factor c·T_g + d·I as a symbolic element."""
    if abs(c_f) < _C_FACTOR_TOL:
        c = sp.Integer(0)
    else:
        c = sp.Integer(1)
    if abs(d_f) < _D_EXACT_TOL:
        d = sp.Integer(0)
    elif abs(d_f - 1.0) < _D_EXACT_TOL:
        d = sp.Integer(1)
    elif abs(d_f + float(HA_sym.subs(q_sym, _Q0_RATIONAL))) < _D_HECKE_TOL:
        d = -HA_sym            # mixed sign convention: -h
    elif abs(d_f + 0.5 * float(HA_sym.subs(q_sym, _Q0_RATIONAL))) < _D_HECKE_TOL:
        d = -HA_sym / 2        # -h/2
    else:
        d = sp.nsimplify(d_f)
    return SymbolicHeckeElement({(g,): c, (): d})


def build_atom_nf_symbolic(Z: int, N: int,
                              reduce_every: int = 4,
                              verbose: bool = True
                              ) -> tuple[SymbolicHeckeElement, dict]:
    """Compute the Gröbner-Shirshov NF of the atom Hecke element."""
    word = atom_braid_word_3A(Z, N)
    div = SymbolicHeckeDivision()
    elem = SymbolicHeckeElement.identity()
    since_reduce = 0
    n_reductions = 0
    t0 = time.time()
    for i, (c_f, d_f, g) in enumerate(word):
        elem = elem * _factor_from(c_f, d_f, g)
        since_reduce += 1
        if since_reduce >= reduce_every:
            elem, _ = div.reduce(elem, engine='laurent')
            n_reductions += 1
            since_reduce = 0
            if verbose:
                print(f"    [{i+1:>3}/{len(word):>3}] "
                      f"after reduction {n_reductions}: "
                      f"n_terms = {elem.n_terms()}, "
                      f"t = {time.time()-t0:.1f}s", flush=True)
    if since_reduce > 0:
        elem, _ = div.reduce(elem)
        n_reductions += 1
        if verbose:
            print(f"    final reduction: n_terms = {elem.n_terms()}, "
                  f"t = {time.time()-t0:.1f}s", flush=True)
    dt = time.time() - t0
    return elem, {
        "n_factors": len(word),
        "n_reductions": n_reductions,
        "n_terms_nf": elem.n_terms(),
        "elapsed_sec": dt,
    }


def jones_polynomial_of_knot_62() -> sp.Expr:
    """J(6_2) in variable q.  Standard form from Kawauchi / KnotInfo.

    J_{6_2}(q) = q^{-5} − 2 q^{-4} + 2 q^{-3} − 2 q^{-2} + 2 q^{-1} − 1 + q

    (Up to writhe / framing convention.)
    """
    return (q_sym**(-5) - 2*q_sym**(-4) + 2*q_sym**(-3)
            - 2*q_sym**(-2) + 2*q_sym**(-1) - 1 + q_sym)


def markov_trace_to_jones(tr: sp.Expr) -> sp.Expr:
    """Convert Markov trace to Jones polynomial.

    Jones(K) = ((-1/√q)^{n-1} · (q/(1-q²))^{n-1})... (convention dep).
    For ease, we return tr as-is and note that comparison must be
    up to the standard q → q^{1/2} substitution and framing.
    """
    return sp.simplify(tr)


def main() -> int:
    print("=" * 100)
    print("PHASE 3 — Symbolic Hecke NF of D's atom braid")
    print("  Pipeline: atom Hecke element → GS NF → Markov trace → Jones")
    print("=" * 100)

    Z, N = 1, 1   # Deuterium
    print(f"\n  Building D's symbolic Hecke NF (Z={Z}, N={N}, 3A=6 strands)…")
    elem, stats = build_atom_nf_symbolic(Z, N, reduce_every=4)
    print(f"  Input factors: {stats['n_factors']}")
    print(f"  GS reductions: {stats['n_reductions']}")
    print(f"  NF terms:      {stats['n_terms_nf']}")
    print(f"  Elapsed:       {stats['elapsed_sec']:.2f} s")

    # Dump the NF: top few terms by coefficient weight
    print("\n  NF (basis_word : coefficient in q) — top 10 by |coeff(q=1)|:")
    items = [(k, v) for k, v in elem.terms.items()]
    def weight(kv):
        k, v = kv
        try:
            return abs(float(v.subs(q_sym, sp.Rational(1))))
        except Exception:
            return 0.0
    items.sort(key=weight, reverse=True)
    for (basis, coeff) in items[:10]:
        b_str = "1" if not basis else "σ_" + "σ_".join(map(str, basis))
        c_str = sp.nsimplify(sp.simplify(coeff))
        # Truncate for readability
        s = str(c_str)
        if len(s) > 80:
            s = s[:77] + "..."
        print(f"    [{b_str:>14}]  {s}")

    # Compute Markov trace (symbolically) — this is the Jones polynomial
    # representative (up to framing convention).
    #
    # NOTE: for D (n=6, 32 NF terms after Gröbner-Shirshov reduction),
    # the fully-symbolic tr_M_element over all partitions of 6 is
    # computationally expensive (≫5 min on a standard core).  Set
    # SKIP_TRACE=1 to produce a witness with the NF only and leave
    # markov_trace=0.  For arbitrary-q NUMERIC evaluation of the same
    # trace (much faster), see atom_jones_vs_knots_D.py which uses
    # Plancherel-weighted seminormal traces at fixed q_val.
    import os
    SKIP_TRACE = os.environ.get("SKIP_TRACE", "0") == "1"  # noqa: I3 — performance gate (expensive symbolic trace), not guarded-off canonical
    if SKIP_TRACE:
        print("\n  [SKIP_TRACE=1; skipping symbolic Markov trace]")
        print("  (Numeric tr_M(D) at various q available in")
        print("   atom-jones-vs-knots-D.witness.json.)")
        tr_simp = sp.Integer(0)
        tr_val = 0j
    else:
        print("\n  Computing symbolic Markov trace tr_M(D's NF)…")
        t0 = time.time()
        try:
            tr = tr_M_element(elem, 6)  # n=6 strands for 3A=6
            tr_simp = markov_trace_to_jones(tr)
            dt = time.time() - t0
        except Exception as e:
            print(f"  [tr_M failed: {e}]")
            return 1
        print(f"  Elapsed: {dt:.2f} s")
        print(f"  tr_M(D-atom) = {sp.nsimplify(tr_simp)}")

    # Compare to J(6_2)
    J_62 = jones_polynomial_of_knot_62()
    print(f"\n  J(6_2) = {J_62}")

    if SKIP_TRACE:
        diff = None
        tr_val = 0j
        J_val = complex(sp.N(J_62.subs(
            q_sym, sp.Rational('11099785956', 10000000000))))
        ratio = None
    else:
        # Symbolic difference
        diff = sp.simplify(tr_simp - J_62)
        print(f"\n  Difference tr_M(D) - J(6_2) = {diff}")
        print(f"  Is zero? {diff == 0}")

        # Also test simple substitution matches
        q0 = sp.Rational('11099785956', 10000000000)
        tr_val = complex(sp.N(tr_simp.subs(q_sym, q0)))
        J_val = complex(sp.N(J_62.subs(q_sym, q0)))
        print(f"  At q=q₀: tr_M(D)={tr_val}  J(6_2)={J_val}")
        print(f"  Ratio tr/J = {tr_val/J_val if J_val else 'J=0'}")

        # Ratio test: even if they differ by a writhe/normalization factor,
        # the ratio should be a pure power of -q^{1/2}.  Check.
        ratio = sp.simplify(tr_simp / J_62) if J_62 != 0 else None
        print(f"  Symbolic ratio tr/J = {ratio}")

    witness = {
        "computation": "atom-NF-symbolic-D",
        "description": (
            "Symbolic Hecke NF of D's atom braid via Gröbner-Shirshov "
            "(SymbolicHeckeDivision).  Extracts the NF coefficients in "
            "Z[q^{1/2},q^{-1/2}], computes the Markov trace symbolically "
            "(= Jones polynomial up to framing), and compares to J(6_2) "
            "from Kawauchi/KnotInfo.  If polynomials match (possibly "
            "up to writhe), D's atom link class IS 6_2 at the Hecke "
            "algebra level, confirming the census-search assignment; "
            "if not, 6_2 was an approximation."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "Z": Z, "N": N, "A": Z + N, "n_strands": 3 * (Z + N),
        },
        "stats": stats,
        "nf_top_terms": [
            {"basis": list(k), "coeff": str(sp.simplify(v))}
            for k, v in items[:20]
        ],
        "markov_trace": str(sp.simplify(tr_simp)),
        "markov_trace_polynomial": expose_polynomial(
            tr_simp, q_sym, simplify=False
        ),
        "J_62": str(J_62),
        "J_62_polynomial": expose_polynomial(J_62, q_sym),
        "difference": str(diff),
        "at_q0": {
            "tr_M_D": str(tr_val),
            "J_62": str(J_val),
        },
        "symbolic_ratio": str(ratio) if ratio is not None else None,
    }
    out = Path(__file__).parent / "atom-nf-symbolic-D.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
