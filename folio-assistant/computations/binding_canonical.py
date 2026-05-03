#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
Atom binding via the CANONICAL Jones-Markov trace.

Wires markov_trace_canonical.tr_M_element (Direction 1 of the
validity audit) into the atom braid-word binding calculation:

  B(Z, N) = E_0 · ( |tr_M(W_free)| − |tr_M(W_atom)| )

where tr_M is the Markov-axioms-satisfying trace matching
prop:categorical-mass-markov's explicit values table — NOT the
Plancherel-weighted form used in hecke_core.atom_markov_trace and
mass_at_3A_proper.binding_3A (both deviate from the prop's z =
1/(q^{1/2} + q^{-1/2}) ≈ 0.499).

Result is compared to:
  • binding_3A (Plancherel)         — current best H_{3A} path
  • tower_binding_full (H_3 tower)  — current per-gen path
  • AME experimental binding        — ground truth

For small A (D, T, 3He, 4He), the full atom braid word reduces to a
symbolic Hecke element; the canonical trace gives an exact value
in q that we evaluate at q₀ = 1.11.
"""
from __future__ import annotations

import sys
import json
import time
from pathlib import Path
from datetime import datetime, timezone

import sympy as sp

sys.path.insert(0, str(Path(__file__).parent))
from markov_trace_canonical import tr_M_element
from hecke_symbolic import (
    SymbolicHeckeDivision, SymbolicHeckeElement, HA as H_SYMB, q as q_sym,
)
from mass_at_3A_proper import atom_braid_word_3A
from q_parameter import Q as Q0_NUM, HA as H0_NUM  # central source of truth


def build_atom_symbolic(Z: int, N: int, *, include_inter: bool = True,
                          m_pp: int = 1, m_pn: int = 1,
                          m_nn: int = 1,
                          reduce_every: int = 4,
                          max_terms: int = 50000,
                          ) -> SymbolicHeckeElement:
    """Build atom braid as SymbolicHeckeElement using symbolic q.

    Incremental Gröbner-Shirshov reduction: apply `div.reduce()` after
    every `reduce_every` factors multiplied in, instead of letting
    the flat product expand to millions of terms before a single
    final reduction.  This matches the pattern in
    `nuclear-braid-exact.py::build_nuclear_braid_incremental`.

    Parameters
    ----------
    reduce_every : int
        Number of factors to multiply in between reduction steps.
        Setting this to 1 reduces after every factor (safest, slowest
        per-factor); 4 matches a nucleon intra-shell (two gens × two
        factors); setting it to infinity reproduces the legacy flat
        build (blows up at 4He).  Default 4.
    max_terms : int
        Abort if the intermediate element exceeds this many terms
        after a reduction step.  Matches the nuclear-braid-exact
        default; raises RuntimeError if hit.
    """
    word = atom_braid_word_3A(Z, N, m_pp=m_pp, m_pn=m_pn, m_nn=m_nn,
                                include_inter=include_inter)

    def _factor_from(c_f: float, d_f: float, g: int
                      ) -> SymbolicHeckeElement:
        if abs(c_f) < 1e-12:
            c = sp.Integer(0)
        else:
            c = sp.Integer(1)
        if abs(d_f) < 1e-12:
            d = sp.Integer(0)
        elif abs(d_f - 1.0) < 1e-12:
            d = sp.Integer(1)
        elif abs(d_f + H0_NUM) < 1e-6:
            d = -H_SYMB
        elif abs(d_f + H0_NUM / 2) < 1e-6:
            d = -H_SYMB / 2
        else:
            d = sp.nsimplify(d_f)
        return SymbolicHeckeElement({(g,): c, (): d})

    div = SymbolicHeckeDivision()
    elem = SymbolicHeckeElement.identity()
    since_last_reduce = 0
    for (c_f, d_f, g) in word:
        elem = elem * _factor_from(c_f, d_f, g)
        since_last_reduce += 1
        if since_last_reduce >= reduce_every:
            elem, _ = div.reduce(elem)
            since_last_reduce = 0
            if elem.n_terms() > max_terms:
                raise RuntimeError(
                    f"atom-braid build exceeded max_terms={max_terms} "
                    f"(Z={Z}, N={N}, gen={g}); current terms = "
                    f"{elem.n_terms()}")
    if since_last_reduce > 0:
        elem, _ = div.reduce(elem)
    return elem


def binding_canonical(Z: int, N: int, *, m_pp=1, m_pn=1, m_nn=1,
                        E_0: float = 0.782,
                        reduce_before_trace: bool = True,
                        verbose: bool = False) -> dict:
    """Binding via canonical Markov trace.

    B = E_0 · (|tr_M(W_free)| − |tr_M(W_atom)|),
    E_0 = 0.782 MeV (free-neutron β-decay Q, per
    prop:categorical-mass-markov).
    """
    A = Z + N
    n_strands = 3 * A
    div = SymbolicHeckeDivision() if reduce_before_trace else None

    atom_elem = build_atom_symbolic(Z, N, include_inter=True,
                                      m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
    free_elem = build_atom_symbolic(Z, N, include_inter=False,
                                      m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)

    if reduce_before_trace:
        atom_elem, _ = div.reduce(atom_elem)
        free_elem, _ = div.reduce(free_elem)

    if verbose:
        print(f"  atom NF: {atom_elem.n_terms()} terms;  "
              f"free NF: {free_elem.n_terms()} terms")

    t0 = time.time()
    try:
        # `simplify=False`: skip the `sp.simplify` step in tr_M_element.
        # At A=3 the aggregated total has ~5000-12000 sympy ops; calling
        # `simplify` exceeds 30 minutes (³He) while the recursion itself
        # runs in seconds.  Numerical evaluation at q=q₀ (below) is
        # unaffected.  See #508 Phase 2 part 2.
        tr_atom_sym = tr_M_element(atom_elem, n_strands, simplify=False)
        tr_free_sym = tr_M_element(free_elem, n_strands, simplify=False)
    except (NotImplementedError, RecursionError) as e:
        return {"status": "trace_error", "error": str(e),
                "Z": Z, "N": N, "A": A,
                "n_atom_terms": atom_elem.n_terms(),
                "n_free_terms": free_elem.n_terms()}
    dt = time.time() - t0

    try:
        tr_atom = complex(sp.N(tr_atom_sym.subs(q_sym, Q0_NUM)))
        tr_free = complex(sp.N(tr_free_sym.subs(q_sym, Q0_NUM)))
    except Exception as e:
        return {"status": "eval_error", "error": str(e)}

    tr_atom_r = tr_atom.real if abs(tr_atom.imag) < 1e-6 else tr_atom
    tr_free_r = tr_free.real if abs(tr_free.imag) < 1e-6 else tr_free
    B = E_0 * (abs(tr_free_r) - abs(tr_atom_r))
    return {
        "status": "solved",
        "Z": Z, "N": N, "A": A,
        "tr_M_atom": str(tr_atom_r),
        "tr_M_free": str(tr_free_r),
        "E_0_MeV": E_0,
        "B_MeV": float(B),
        "n_atom_terms": atom_elem.n_terms(),
        "n_free_terms": free_elem.n_terms(),
        "trace_time_sec": dt,
    }


if __name__ == "__main__":
    ATOMS = [
        ("D",    1, 1,  2.22452),
        ("T",    1, 2,  8.481821),
        ("3He",  2, 1,  7.71804),
        ("4He",  2, 2, 28.295674),
    ]
    print("=" * 100)
    print("BINDING via CANONICAL Jones-Markov trace "
          "(prop:categorical-mass-markov)")
    print(f"q₀ = {Q0_NUM}, E_0 = 0.782 MeV (β-decay Q)")
    print("=" * 100)
    results = []
    print(f"  {'Atom':>6} {'A':>3} {'3A':>3} {'B_AME':>8} "
          f"{'|tr_atom|':>12} {'|tr_free|':>12} "
          f"{'B_pred':>10} {'|Δm/m|%':>9} {'time':>8}")
    print("  " + "-" * 96)
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        r = binding_canonical(Z, N, verbose=False)
        if r.get("status") != "solved":
            print(f"  {name:>6} {A:>3} {3*A:>3}  "
                  f"STATUS: {r.get('status')}: "
                  f"{r.get('error', '')[:60]}")
            results.append(r)
            continue
        tr_a = complex(r["tr_M_atom"].replace("(", "").replace(")", ""))
        tr_f = complex(r["tr_M_free"].replace("(", "").replace(")", ""))
        M_total = A * 938.272
        dm = abs(r["B_MeV"] - B_AME) / M_total * 100
        print(f"  {name:>6} {A:>3} {3*A:>3} {B_AME:>8.3f} "
              f"{abs(tr_a):>12.6e} {abs(tr_f):>12.6e} "
              f"{r['B_MeV']:>+10.4f} {dm:>8.4f}% "
              f"{r['trace_time_sec']:>7.2f}s")
        results.append({**r, "atom": name, "B_AME_MeV": B_AME,
                         "delta_m_over_m_pct": dm})

    witness = {
        "computation": "binding-canonical-markov",
        "description": (
            "Atom binding via the canonical Jones-Markov trace "
            "(Direction 1 of validity audit): matches the prop's "
            "explicit-values table tr_M(σ_0)=z, tr_M(σ_0σ_1)=z², "
            "tr_M(σ_0σ_1σ_0)=hz²+z.  Replaces the Plancherel-"
            "weighted trace used in binding_3A and "
            "atom_markov_trace.  Binding = E_0·(|tr_M_free| − "
            "|tr_M_atom|) with E_0 = 0.782 MeV (β-decay Q)."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0_NUM, "E_0_MeV": 0.782},
        "results": results,
    }
    out = Path(__file__).parent / "binding-canonical.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
