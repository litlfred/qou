#!/usr/bin/env python3
"""
Full atom NF computation: NF(A(Z,N)) including electrons.

Explores whether electron shell structure (2 inner + 4 outer for carbon)
is readable from the Gröbner–Shirshov normal form, and whether
quotienting by the nuclear ideal reveals a graded shell structure.

Crossing types:
  pp (proton-proton):     σ         (c=1, d=0)        — Coulomb repulsion
  nn (neutron-neutron):   σ⁻¹       (c=1, d=−HA)      — strong force
  pn (proton-neutron):    ½(σ+σ⁻¹)  (c=1, d=−HA/2)    — mixed
  pe (proton-electron):   σ⁻¹       (c=1, d=−HA)      — EM attraction
  ne (neutron-electron):  𝟏         (c=0, d=1)         — no interaction
  ee (electron-electron): σ         (c=1, d=0)         — EM repulsion

Usage:
    cd folio-assistant/computations
    python3 carbon-atom-nf.py
"""

import sympy as sp
import time
from hecke_symbolic import (
    SymbolicHeckeDivision, SymbolicHeckeElement,
    q, HA, C_PP, D_PP, C_NN, D_NN, C_MIX, D_MIX,
)

# ── Crossing coefficients ────────────────────────────────────

# Electron crossing types
C_PE = sp.Integer(1)       # proton-electron: σ⁻¹ (attractive)
D_PE = -(q - 1/q)          # same as nn

C_NE = sp.Integer(0)       # neutron-electron: identity (no interaction)
D_NE = sp.Integer(1)

C_EE = sp.Integer(1)       # electron-electron: σ (repulsive)
D_EE = sp.Integer(0)       # same as pp


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
    q0 = 1.10998
    t0 = time.time()

    print("=" * 72)
    print("ATOM NF WITH ELECTRON SHELL STRUCTURE")
    print("Crossing types: pp=σ, nn=σ⁻¹, pn=½(σ+σ⁻¹), pe=σ⁻¹, ne=𝟏, ee=σ")
    print("=" * 72)

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

        # q-degree: highest power of q in the net coefficient
        net_poly = sp.Poly(sp.expand(net * q**10), q)  # shift to avoid negative powers
        if net_poly.is_zero:
            print(f"    q-degree: 0")
        else:
            deg = net_poly.degree()
            print(f"    q-degree (shifted): {deg}")

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
