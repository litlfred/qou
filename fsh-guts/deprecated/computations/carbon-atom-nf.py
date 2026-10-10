#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
Full atom NF computation: NF(A(Z, N)) including electrons, via
Gröbner–Shirshov reduction in H_n(q).

Explores whether electron shell structure (2 inner + 4 outer for
carbon) is readable from the GS normal form, and whether quotienting
by the nuclear ideal reveals a graded shell structure.

What is "actual" about this NF
------------------------------
The Hecke relation σ_i² = (q − q⁻¹)σ_i + 1 forces every crossing
type to reduce to a (c·σ + d·𝟏) pair in H_n(q).  The ONLY postulate
is the physical-to-braid-word assignment — which interaction maps to
σ vs σ⁻¹ vs 𝟏.  Once that mapping is chosen (table below), the (c, d)
coefficients are DERIVED from the Hecke relation, NOT free
parameters.  The GS reduction then gives the unique NF.

| Interaction | Braid word     | (c, d) from Hecke relation |
|-------------|----------------|----------------------------|
| p–p (EM rep.)     | σ              | (1, 0)              |
| n–n (strong)      | σ⁻¹            | (1, −(q−q⁻¹))        |
| p–n (mixed)       | ½(σ + σ⁻¹)     | (1, −(q−q⁻¹)/2)     |
| p–e (EM attr.)    | σ⁻¹            | (1, −(q−q⁻¹))        |
| n–e (no EM)       | 𝟏              | (0, 1)              |
| e–e (EM rep.)     | σ              | (1, 0)              |

Canonical (c, d) pairs live in hecke_symbolic.py — this file imports
them rather than re-declaring, so the GS-consistency audit below
checks the shared constants.

Usage:
    cd computations
    python3 carbon-atom-nf.py [--audit-only]
"""

import sys
import sympy as sp
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as _Q_CANONICAL
from hecke_symbolic import (
    SymbolicHeckeDivision, SymbolicHeckeElement,
    q, HA,
    C_PP, D_PP, C_NN, D_NN, C_MIX, D_MIX,
    C_PE, D_PE, C_NE, D_NE, C_EE, D_EE,
)


# ── GS consistency audit ─────────────────────────────────────
#
# Verifies that every (c, d) crossing pair respects the Hecke
# relation σ² = (q − q⁻¹)σ + 1, i.e. that the element c·σ + d·𝟏
# squares (under the relation) to a valid H_n(q) element and does
# not require any additional reduction axioms.

def gs_consistency_audit():
    """Return a list of (label, (c, d), status, residue) tuples.

    For each labeled crossing (pp, nn, pn, pe, ne, ee), verify:
      (c·σ₀ + d)² in H_2(q) reduces to an H_2(q) NF with no
      residual higher-order terms.

    A failure indicates the (c, d) pair is inconsistent with the
    Hecke relation — i.e. a broken postulate.
    """
    div = SymbolicHeckeDivision()
    pairs = [
        ("pp", C_PP, D_PP),
        ("nn", C_NN, D_NN),
        ("pn", C_MIX, D_MIX),
        ("pe", C_PE, D_PE),
        ("ne", C_NE, D_NE),
        ("ee", C_EE, D_EE),
    ]
    results = []
    for label, c, d in pairs:
        # Build c·σ₀ + d·𝟏
        elem = SymbolicHeckeElement({(0,): c, (): d})
        # Square it: (c·σ + d)² = c²·σ² + 2cd·σ + d²
        # Under Hecke relation σ² → (q−q⁻¹)σ + 𝟏, this becomes
        # c²(HA·σ + 𝟏) + 2cd·σ + d² = (c²·HA + 2cd)·σ + (c² + d²)
        squared = elem * elem
        reduced, _steps = div.reduce(squared)
        # Expected NF: {(0,): c²·HA + 2cd, (): c² + d²}
        expected_sigma = sp.simplify(c * c * HA + 2 * c * d)
        expected_id = sp.simplify(c * c + d * d)
        got_sigma = sp.simplify(reduced.terms.get((0,), sp.Integer(0)))
        got_id = sp.simplify(reduced.terms.get((), sp.Integer(0)))
        residue_sigma = sp.simplify(got_sigma - expected_sigma)
        residue_id = sp.simplify(got_id - expected_id)
        # Extra terms beyond {(0,), ()} would indicate a relation
        # failure; we flag them.
        extra_keys = [w for w in reduced.terms
                       if w not in {(0,), ()}]
        ok = (residue_sigma == 0 and residue_id == 0
               and not extra_keys)
        results.append({
            "label": label,
            "c": str(c),
            "d": str(d),
            "ok": bool(ok),
            "residue_sigma": str(residue_sigma),
            "residue_id": str(residue_id),
            "extra_terms": [str(w) for w in extra_keys],
        })
    return results


def crossing_element(type_i, type_j, gen):
    """Build crossing element for strand pair (type_i, type_j) at generator gen."""
    pair = frozenset([type_i, type_j])

    if type_i == 'p' and type_j == 'p':
        return SymbolicHeckeElement({(gen,): C_PP, (): D_PP})
    elif type_i == 'n' and type_j == 'n':
        return SymbolicHeckeElement({(gen,): C_NN, (): D_NN})
    elif pair == frozenset(['p', 'n']):
        return SymbolicHeckeElement({(gen,): C_MIX, (): D_MIX})
    elif pair == frozenset(['p', 'e']):
        return SymbolicHeckeElement({(gen,): C_PE, (): D_PE})
    elif type_i == 'e' and type_j == 'e':
        return SymbolicHeckeElement({(gen,): C_EE, (): D_EE})
    elif pair == frozenset(['n', 'e']):
        # Neutron-electron: identity (no crossing)
        return SymbolicHeckeElement({(): D_NE})
    else:
        raise ValueError(f"Unknown crossing pair: ({type_i}, {type_j})")


def build_atom(types, div=None, label="", verbose=True):
    """Build atom by sequential crossing + GS reduction.

    types: list of strand types ('p', 'n', 'e')
    Returns (reduced_element, steps_dict, build_log)
    """
    if div is None:
        div = SymbolicHeckeDivision()

    A = len(types)
    if verbose:
        print(f"\n  {label}: {A} strands ({''.join(types)}), H_{A}(q)")

    elem = SymbolicHeckeElement.identity()
    total_steps = {'hecke': 0, 'yb': 0, 'fc': 0, 'quotient': 0}
    build_log = []

    for k in range(1, A):
        for i in range(k):
            cx = crossing_element(types[i], types[k], i)
            # Skip identity crossings (ne pairs produce just 𝟏)
            if cx.n_terms() == 1 and () in cx.terms:
                # Pure scalar — just multiply by the scalar
                elem = elem.scale(cx.terms[()])
            else:
                elem = elem * cx

            elem, steps = div.reduce(elem)
            for key in total_steps:
                total_steps[key] += steps.get(key, 0)

        # Log after each strand
        hist = word_length_histogram(elem)
        build_log.append({
            'strand': k,
            'type': types[k],
            'n_terms': elem.n_terms(),
            'histogram': hist,
            'palindromic': is_palindromic(hist),
        })

        if verbose:
            pal_mark = " ★ PAL" if build_log[-1]['palindromic'] else ""
            print(f"    +{types[k]} (strand {k}): {elem.n_terms()} terms, "
                  f"hist={hist}{pal_mark}")

    if verbose:
        print(f"    → FINAL: {elem.n_terms()} terms (target: {A})")
        print(f"    Steps: {total_steps}")

    return elem, total_steps, build_log


def word_length_histogram(elem):
    """Word-length histogram of NF terms."""
    hist = {}
    for w in elem.terms:
        L = len(w)
        hist[L] = hist.get(L, 0) + 1
    return dict(sorted(hist.items()))


def is_palindromic(hist):
    """Check if histogram counts are palindromic."""
    if not hist:
        return True
    counts = [hist[k] for k in sorted(hist.keys())]
    return counts == counts[::-1]


def show_nf(elem, q0, name=""):
    """Display NF evaluated at q₀."""
    if name:
        print(f"\n  {name} (symbolic):")
    for w, c in sorted(elem.terms.items(), key=lambda x: (len(x[0]), x[0])):
        ws = " · ".join(f"σ_{i}" for i in w) if w else "𝟏"
        c_fac = sp.factor(c)
        print(f"    ({c_fac}) · {ws}")

    if q0:
        print(f"\n  {name} at q₀ = {q0}:")
        vals = elem.evaluate(q0)
        for w, v in sorted(vals.items(), key=lambda x: (len(x[0]), x[0])):
            ws = " · ".join(f"σ_{i}" for i in w) if w else "𝟏"
            print(f"    ({v:+.8f}) · {ws}")


def quotient_nucleus(atom_nf, nucleus_nf, label=""):
    """Quotient the atom NF by the nuclear NF.

    Subtracts the nuclear contribution and examines the residual
    electron chain structure.
    """
    # The nuclear NF occupies the first few generators.
    # The atom NF should contain the nuclear terms plus electron terms.
    # Strategy: identify terms that are purely nuclear (generators < n_nuc)
    # vs terms involving electron generators (generators >= n_nuc).
    print(f"\n  QUOTIENT: {label}")

    # Split terms by whether they use generators in the electron range
    nuclear_terms = {}
    mixed_terms = {}
    electron_terms = {}

    # We don't know the exact generator boundary, so use term structure
    # Nuclear generators: 0..n_nuc-2, electron generators: n_nuc-1..n_total-2
    # But after GS reduction, terms are mixed. Instead, compare to nucleus NF.

    # Method: compute atom_NF - nucleus_NF (as elements in the shared algebra)
    # The nuclear NF uses generators σ_0..σ_{n_nuc-2}
    # The atom extends with σ_{n_nuc-1}..σ_{n_total-2}

    residual_terms = dict(atom_nf.terms)
    for w, c in nucleus_nf.terms.items():
        if w in residual_terms:
            residual_terms[w] = sp.expand(residual_terms[w] - c)
            if sp.simplify(residual_terms[w]) == 0:
                del residual_terms[w]

    residual = SymbolicHeckeElement(residual_terms)
    print(f"    Atom terms: {atom_nf.n_terms()}")
    print(f"    Nucleus terms: {nucleus_nf.n_terms()}")
    print(f"    Residual (atom − nucleus): {residual.n_terms()} terms")

    hist = word_length_histogram(residual)
    print(f"    Residual histogram: {hist}")
    print(f"    Residual palindromic: {is_palindromic(hist)}")

    return residual


# ══════════════════════════════════════════════════════════════
# MAIN: Build atoms H through C, observe shell structure
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--audit-only", action="store_true",
                    help="Run only the GS consistency audit and exit")
    args = ap.parse_args()

    q0 = _Q_CANONICAL
    t0 = time.time()

    print("=" * 72)
    print("ATOM NF WITH ELECTRON SHELL STRUCTURE")
    print("Crossing types: pp=σ, nn=σ⁻¹, pn=½(σ+σ⁻¹), pe=σ⁻¹, ne=𝟏, ee=σ")
    print("(c, d) pairs imported from hecke_symbolic — single source of truth")
    print("=" * 72)

    # ── GS consistency audit ──────────────────────────────────
    print("\n" + "─" * 72)
    print("PHASE 0: GRÖBNER–SHIRSHOV CONSISTENCY AUDIT")
    print("Verify each (c, d) pair respects σ² = (q−q⁻¹)σ + 𝟏")
    print("─" * 72)
    audit = gs_consistency_audit()
    print(f"  {'type':>4} {'c':>10} {'d':>14} {'ok':>4}")
    all_ok = True
    for entry in audit:
        mark = "✓" if entry['ok'] else "✗"
        print(f"  {entry['label']:>4} {entry['c']:>10} "
              f"{entry['d']:>14} {mark:>4}")
        if not entry['ok']:
            all_ok = False
            print(f"    residue_σ = {entry['residue_sigma']}")
            print(f"    residue_𝟏 = {entry['residue_id']}")
            if entry['extra_terms']:
                print(f"    extra terms: {entry['extra_terms']}")
    print(f"\n  GS audit: {'ALL PASS' if all_ok else 'FAILURES'}")

    if args.audit_only:
        raise SystemExit(0 if all_ok else 1)

    div = SymbolicHeckeDivision()

    # ── Phase 1: Nuclei only (for quotient baseline) ─────────

    print("\n" + "─" * 72)
    print("PHASE 1: NUCLEAR CORES (no electrons)")
    print("─" * 72)

    nuclei = {}
    for label, p, n in [
        ("H",  1, 0), ("D",  1, 1), ("He", 2, 2),
        ("Li", 3, 4), ("Be", 4, 5), ("B",  5, 6), ("C", 6, 6),
    ]:
        types = ['p'] * p + ['n'] * n
        if len(types) < 2:
            print(f"\n  {label} N({p},{n}): single strand (trivial)")
            nuclei[label] = SymbolicHeckeElement.identity()
            continue
        nf, steps, log = build_atom(types, div, f"{label} N({p},{n})")
        nuclei[label] = nf

    # ── Phase 2: Full atoms with electrons ───────────────────

    print("\n" + "─" * 72)
    print("PHASE 2: FULL ATOMS (nucleus + electrons)")
    print("─" * 72)

    atoms_config = [
        ("H",   1, 0, 1),   # 1p + 0n + 1e = 2 strands
        ("He",  2, 2, 2),   # 2p + 2n + 2e = 6 strands
        ("Li",  3, 4, 3),   # 3p + 4n + 3e = 10 strands
        ("Be",  4, 5, 4),   # 4p + 5n + 4e = 13 strands
        ("B",   5, 6, 5),   # 5p + 6n + 5e = 16 strands
        ("C",   6, 6, 6),   # 6p + 6n + 6e = 18 strands
    ]

    atoms = {}
    atom_logs = {}

    for label, p, n, e in atoms_config:
        types = ['p'] * p + ['n'] * n + ['e'] * e
        A = p + n + e
        t_start = time.time()

        nf, steps, log = build_atom(types, div, f"{label} A({p},{n}) + {e}e⁻")
        atoms[label] = nf
        atom_logs[label] = log

        elapsed = time.time() - t_start
        print(f"    Time: {elapsed:.1f}s")

        # Show symbolic NF for small atoms
        if A <= 6:
            show_nf(nf, q0, f"{label} atom")

    # ── Phase 3: Electron addition analysis ──────────────────

    print("\n" + "─" * 72)
    print("PHASE 3: ELECTRON-BY-ELECTRON ANALYSIS")
    print("Look for shell closure at electron 2 (1s²) and 10 (2p⁶)")
    print("─" * 72)

    # Build carbon step by step, logging after each electron
    print("\n  Carbon: adding electrons one at a time to N(6,6)")
    nuc_types = ['p'] * 6 + ['n'] * 6

    # First build nucleus
    nuc_nf, _, _ = build_atom(nuc_types, SymbolicHeckeDivision(),
                               "C nucleus N(6,6)", verbose=False)
    print(f"    Nuclear core: {nuc_nf.n_terms()} terms")

    # Now add electrons one at a time
    current = nuc_nf
    current_types = list(nuc_types)
    electron_log = []

    for e_idx in range(1, 7):
        current_types.append('e')
        n_strands = len(current_types)

        # Add crossings for new electron with all existing strands
        for i in range(n_strands - 1):
            cx = crossing_element(current_types[i], 'e', i)
            if cx.n_terms() == 1 and () in cx.terms:
                current = current.scale(cx.terms[()])
            else:
                current = current * cx
            current, _ = div.reduce(current)

        hist = word_length_histogram(current)
        pal = is_palindromic(hist)

        entry = {
            'electron': e_idx,
            'total_strands': n_strands,
            'n_terms': current.n_terms(),
            'histogram': hist,
            'palindromic': pal,
        }
        electron_log.append(entry)

        pal_mark = " ★ SHELL CLOSURE" if pal else ""
        print(f"    +e⁻ #{e_idx}: {current.n_terms()} terms, "
              f"strands={n_strands}, hist={hist}{pal_mark}")

    # ── Phase 4: Quotient by nuclear ideal ───────────────────

    print("\n" + "─" * 72)
    print("PHASE 4: QUOTIENT BY NUCLEAR IDEAL")
    print("Register N(6,6) as formal variable, examine residual")
    print("─" * 72)

    # For atoms where we have both nucleus and full atom
    for label in ["He", "C"]:
        if label in atoms and label in nuclei:
            residual = quotient_nucleus(atoms[label], nuclei[label], label)

    # ── Phase 5: Grading analysis ────────────────────────────

    print("\n" + "─" * 72)
    print("PHASE 5: q-DEGREE GRADING")
    print("Check if electron terms carry a natural q-grading by shell")
    print("─" * 72)

    # For each atom, compute net coefficient and factor it
    for label, p, n, e in atoms_config:
        if label not in atoms:
            continue
        nf = atoms[label]
        net = sum(nf.terms.values())
        net_fac = sp.factor(net)
        print(f"\n  {label} (Z={p}): net = {net_fac}")

        # q-degree: highest power of q in the Laurent polynomial
        net_cancelled = sp.cancel(net)
        num, den = net_cancelled.as_numer_denom()
        if num == 0:
            print(f"    q-degree: 0")
        else:
            deg = sp.degree(num, q) - sp.degree(den, q)
            print(f"    q-degree: {deg}")

    # ── Summary ──────────────────────────────────────────────

    print("\n" + "=" * 72)
    print("SUMMARY: SHELL CLOSURE SIGNATURES")
    print("=" * 72)

    print(f"\n  {'Atom':>4} {'Z':>3} {'Strands':>8} {'Terms':>6} "
          f"{'Target':>7} {'Palindromic':>12}")
    print(f"  {'-' * 50}")

    for label, p, n, e in atoms_config:
        if label not in atoms:
            continue
        nf = atoms[label]
        A = p + n + e
        pal = is_palindromic(word_length_histogram(nf))
        pal_str = "★ YES" if pal else "no"
        print(f"  {label:>4} {p:>3} {A:>8} {nf.n_terms():>6} "
              f"{A:>7} {pal_str:>12}")

    print(f"\n  Electron-by-electron for carbon:")
    print(f"  {'e⁻#':>4} {'Strands':>8} {'Terms':>6} {'Palindromic':>12}")
    print(f"  {'-' * 35}")
    for entry in electron_log:
        pal_str = "★ CLOSURE" if entry['palindromic'] else "open"
        print(f"  {entry['electron']:>4} {entry['total_strands']:>8} "
              f"{entry['n_terms']:>6} {pal_str:>12}")

    total_time = time.time() - t0
    print(f"\n  Total time: {total_time:.1f}s")

    # ── Witness output ───────────────────────────────────────
    from datetime import datetime, timezone
    from pathlib import Path as _Path
    import json as _json

    atom_summaries = []
    for label, p, n, e in atoms_config:
        if label not in atoms:
            continue
        nf = atoms[label]
        A = p + n + e
        hist = word_length_histogram(nf)
        atom_summaries.append({
            "label": label, "Z": p, "N": n, "E": e, "A": A,
            "n_terms": nf.n_terms(),
            "histogram": hist,
            "palindromic": is_palindromic(hist),
        })

    witness = {
        "computation": "carbon-atom-nf",
        "description": (
            "Atom NF via Gröbner–Shirshov reduction in H_n(q). "
            "Includes PHASE 0 (GS consistency audit of every "
            "(c, d) crossing pair against σ² = (q−q⁻¹)σ + 𝟏), "
            "and full atom NF builds H, D, He, Li, Be, B, C with "
            "electron shell structure. Crossing (c, d) pairs are "
            "imported from hecke_symbolic.py — single source of "
            "truth for the pp, nn, pn, pe, ne, ee postulates."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0_numeric": q0},
        "gs_audit": audit,
        "gs_audit_all_pass": all_ok,
        "atoms": atom_summaries,
        "electron_by_electron_carbon": electron_log,
        "total_time_sec": total_time,
    }
    out = _Path(__file__).parent / "carbon-atom-nf.witness.json"
    out.write_text(_json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
