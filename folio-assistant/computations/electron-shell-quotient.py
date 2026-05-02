#!/usr/bin/env python3
# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Electron shell structure via quotient by the nuclear ideal.

KEY IDEA: Quotient the nuclear core to a single formal variable 𝒩.
This reduces A(Z,N) from (Z+N+Z_e) strands to (1 + Z_e) strands.

The electron chain then lives in H_{Z+1}(q) with:
  - Strand 0: nuclear core 𝒩 (charge Z)
  - Strands 1..Z: electrons e₁, ..., e_Z

Crossing types in the quotient:
  𝒩-e  (nucleus-electron): σ⁻¹ with strength ∝ Z  (EM attraction)
  e-e  (electron-electron): σ                       (EM repulsion)

We explore THREE models:
  Model A: Pure electron chain (no nucleus strand, just ee repulsion)
  Model B: Single nucleus strand + electrons (Ne attraction + ee repulsion)
  Model C: Graded nucleus — inner shell acts as sub-quotient

Question: Does the NF naturally split into {1s²} ⊕ {2s²2p²} for carbon?

Usage:
    cd folio-assistant/computations
    python3 electron-shell-quotient.py
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
)

q0 = _Q_CANONICAL

# ══════════════════════════════════════════════════════════════
# Crossing coefficients
# ══════════════════════════════════════════════════════════════

# ee: σ (repulsive, same as pp)
C_EE = sp.Integer(1)
D_EE = sp.Integer(0)

# 𝒩e: σ⁻¹ (attractive, same as nn)
C_NE_attract = sp.Integer(1)
D_NE_attract = -(q - 1/q)       # = −HA


def sigma_inv_power(Z_eff):
    """Compute (σ⁻¹)^Z via the Hecke recurrence.

    The quotient of Z proton-electron crossings is (σ⁻¹)^Z, NOT Z·σ⁻¹.
    In the braid picture, Z protons quotiented to one strand means the
    electron wraps Z times — giving the Z-fold composition, reduced by
    the Hecke relation σ² = hσ + 1.

    Recurrence: (σ⁻¹)^Z = c_Z σ + d_Z with
      c_{Z+1} = d_Z,  d_{Z+1} = c_Z - h·d_Z
    """
    h = q - 1/q
    if Z_eff == 0:
        return sp.Integer(0), sp.Integer(1)
    c, d = sp.Integer(1), -(q - 1/q)  # Z=1: σ⁻¹ = σ - h
    for _ in range(Z_eff - 1):
        c, d = d, c - h * d
    return sp.expand(c), sp.expand(d)


def crossing(type_i, type_j, gen, Z_eff=1):
    """Build crossing element.

    type_i, type_j: 'nuc' (nuclear core) or 'e' (electron)
    Z_eff: effective nuclear charge (number of protons in nucleus)

    For nuclear-electron crossings: uses (σ⁻¹)^Z (Z-fold Hecke
    composition), not Z·σ⁻¹ (scalar multiple).
    """
    if type_i == 'e' and type_j == 'e':
        # ee repulsion: σ
        return SymbolicHeckeElement({(gen,): C_EE, (): D_EE})
    elif 'nuc' in (type_i, type_j):
        # Nuclear-electron: (σ⁻¹)^Z_eff via Hecke recurrence
        c, d = sigma_inv_power(Z_eff)
        return SymbolicHeckeElement({(gen,): c, (): d})
    else:
        raise ValueError(f"Unknown pair: ({type_i}, {type_j})")


def build_chain(types, div=None, label="", Z_eff=1, verbose=True):
    """Build electron chain by sequential crossing + GS reduction.

    types: list of strand types ('nuc', 'e')
    Z_eff: effective nuclear charge for nuc-e crossings
    """
    if div is None:
        div = SymbolicHeckeDivision()

    A = len(types)
    if verbose:
        type_str = ''.join('N' if t == 'nuc' else 'e' for t in types)
        print(f"\n  {label}: {A} strands ({type_str}), H_{A}(q), Z_eff={Z_eff}")

    elem = SymbolicHeckeElement.identity()
    total_steps = {'hecke': 0, 'yb': 0, 'fc': 0, 'quotient': 0}

    for k in range(1, A):
        for i in range(k):
            cx = crossing(types[i], types[k], i, Z_eff)
            elem = elem * cx
            elem, steps = div.reduce(elem)
            for key in total_steps:
                total_steps[key] += steps.get(key, 0)

        hist = histogram(elem)
        pal = is_pal(hist)
        pal_mark = " ★ PAL" if pal else ""
        if verbose:
            print(f"    +{types[k]} (strand {k}): {elem.n_terms()} terms, "
                  f"hist={hist}{pal_mark}")

    if verbose:
        print(f"    → {elem.n_terms()} terms, steps={total_steps}")

    return elem, total_steps


def histogram(elem):
    h = {}
    for w in elem.terms:
        L = len(w)
        h[L] = h.get(L, 0) + 1
    return dict(sorted(h.items()))


def is_pal(hist):
    if not hist:
        return True
    counts = [hist[k] for k in sorted(hist.keys())]
    return counts == counts[::-1]


def show_nf(elem, name=""):
    """Show symbolic NF."""
    if name:
        print(f"\n  {name} (symbolic):")
    for w, c in sorted(elem.terms.items(), key=lambda x: (len(x[0]), x[0])):
        ws = " · ".join(f"σ_{i}" for i in w) if w else "𝟏"
        c_fac = sp.factor(c)
        c_val = float(c.subs(q, q0))
        print(f"    ({str(c_fac):>30}) · {ws}  = {c_val:+.6f}")


def analyze_shell_structure(elem, n_nuc_strands, name=""):
    """Analyze whether the NF has a natural shell decomposition.

    Look at terms grouped by which generators they use.
    Generators 0..n_nuc-1 are nucleus-electron.
    Generators n_nuc..end are electron-electron.
    """
    print(f"\n  SHELL ANALYSIS: {name}")

    # Group by generator range
    nuc_e_terms = {}   # terms using only generators 0..n_nuc-2
    ee_terms = {}      # terms using generators >= n_nuc-1
    mixed_terms = {}   # terms using both ranges

    n_nuc = n_nuc_strands  # nucleus takes strand 0

    for w, c in elem.terms.items():
        gens = [g for g in w if g >= 0]
        if not gens:
            # Identity term
            nuc_e_terms[w] = c
            continue

        max_gen = max(gens)
        min_gen = min(gens)

        if max_gen < n_nuc:
            nuc_e_terms[w] = c
        elif min_gen >= n_nuc:
            ee_terms[w] = c
        else:
            mixed_terms[w] = c

    print(f"    Pure nucleus-electron terms (σ < {n_nuc}): {len(nuc_e_terms)}")
    print(f"    Pure electron-electron terms (σ ≥ {n_nuc}): {len(ee_terms)}")
    print(f"    Mixed terms: {len(mixed_terms)}")

    # Net coefficients by group
    net_ne = sum(nuc_e_terms.values()) if nuc_e_terms else sp.Integer(0)
    net_ee = sum(ee_terms.values()) if ee_terms else sp.Integer(0)
    net_mix = sum(mixed_terms.values()) if mixed_terms else sp.Integer(0)

    print(f"    Net(N-e): {sp.factor(net_ne)} = {float(net_ne.subs(q, q0)):+.6f}")
    print(f"    Net(e-e): {sp.factor(net_ee)} = {float(net_ee.subs(q, q0)):+.6f}")
    print(f"    Net(mix): {sp.factor(net_mix)} = {float(net_mix.subs(q, q0)):+.6f}")

    return nuc_e_terms, ee_terms, mixed_terms


# ══════════════════════════════════════════════════════════════
# MODEL A: Pure electron chain (no nucleus, just ee repulsion)
# ══════════════════════════════════════════════════════════════

def model_A():
    print("\n" + "=" * 72)
    print("MODEL A: PURE ELECTRON CHAIN")
    print("Z electrons, ee crossings only (σ repulsion)")
    print("Question: does the NF show 2-periodicity (shell closures)?")
    print("=" * 72)

    for Z in range(2, 11):
        types = ['e'] * Z
        div = SymbolicHeckeDivision()
        elem, _ = build_chain(types, div, f"Z={Z} electron chain", verbose=False)
        hist = histogram(elem)
        pal = is_pal(hist)
        net = sum(elem.terms.values())
        net_val = float(net.subs(q, q0))
        pal_str = "★ PAL" if pal else "      "
        noble = " ← He" if Z == 2 else " ← Ne" if Z == 10 else ""
        print(f"  Z={Z:>2}: {elem.n_terms():>4} terms, "
              f"hist={hist}, net={net_val:+.6f} {pal_str}{noble}")

        # Show full NF for small Z
        if Z <= 3:
            show_nf(elem, f"Z={Z} electrons")


# ══════════════════════════════════════════════════════════════
# MODEL B: Nucleus + electron chain
# ══════════════════════════════════════════════════════════════

def model_B():
    print("\n" + "=" * 72)
    print("MODEL B: SINGLE NUCLEUS + ELECTRON CHAIN")
    print("Strand 0 = 𝒩 (nuclear core, charge Z)")
    print("Strands 1..Z = electrons")
    print("𝒩-e: Z·σ⁻¹ (attraction), e-e: σ (repulsion)")
    print("=" * 72)

    results = {}

    for Z in range(1, 11):
        types = ['nuc'] + ['e'] * Z
        div = SymbolicHeckeDivision()
        elem, _ = build_chain(types, div, f"Z={Z} atom (quotient)",
                              Z_eff=Z, verbose=(Z <= 6))
        hist = histogram(elem)
        pal = is_pal(hist)
        net = sum(elem.terms.values())
        net_val = float(net.subs(q, q0))
        pal_str = "★ PAL" if pal else "      "
        noble = " ← He" if Z == 2 else " ← Li" if Z == 3 else \
                " ← C" if Z == 6 else " ← Ne" if Z == 10 else ""
        print(f"\n  Z={Z:>2}: {elem.n_terms():>4} terms, "
              f"hist={hist}, net={net_val:+.6f} {pal_str}{noble}")

        results[Z] = elem

        # Show full NF
        if Z <= 6:
            show_nf(elem, f"A(Z={Z}) quotient atom")

    return results


# ══════════════════════════════════════════════════════════════
# MODEL C: Graded quotient — inner shell as sub-quotient
# ══════════════════════════════════════════════════════════════

def model_C(model_b_results):
    print("\n" + "=" * 72)
    print("MODEL C: GRADED QUOTIENT (inner shell → formal variable)")
    print("Step 1: Build He (Z=2) = 1s² shell → register as ℵ_He")
    print("Step 2: Build C(Z=6) using ℵ_He as inner shell quotient")
    print("Residual = atom / (1s²) should show the 2s²2p² structure")
    print("=" * 72)

    # Step 1: Helium as inner shell
    div_c = SymbolicHeckeDivision()
    he_types = ['nuc'] + ['e'] * 2
    he_nf, _ = build_chain(he_types, div_c, "He (1s² shell)", Z_eff=2)
    show_nf(he_nf, "He = 1s² closed shell")

    # Register He NF as formal variable ℵ_He
    div_c.register_quotient(-1, he_nf, name="He_1s2")
    print(f"\n  Registered He (1s²) as ℵ₁ ({he_nf.n_terms()} terms)")

    # Step 2: Build carbon with Z_eff=6
    # The first 2 electrons should form the He-like 1s² core
    # The remaining 4 should be the valence shell
    c_types = ['nuc'] + ['e'] * 6
    c_nf, c_steps = build_chain(c_types, div_c, "C(Z=6) with ℵ₁ quotient",
                                 Z_eff=6)
    show_nf(c_nf, "C atom (with 1s² quotient)")

    # Analyze what gets quotiented
    print(f"\n  Quotient reductions: {c_steps.get('quotient', 0)}")

    # Shell analysis: generators 0 = nuc-e, generators 1+ = ee
    analyze_shell_structure(c_nf, 1, "Carbon (quotient)")

    # Step 3: Explicit subtraction — remove the He NF terms
    print(f"\n  EXPLICIT RESIDUAL: C − He")
    residual_terms = dict(c_nf.terms)
    for w, c in he_nf.terms.items():
        if w in residual_terms:
            residual_terms[w] = sp.expand(residual_terms[w] - c)
            if sp.simplify(residual_terms[w]) == 0:
                del residual_terms[w]

    residual = SymbolicHeckeElement(residual_terms)
    print(f"    C terms: {c_nf.n_terms()}")
    print(f"    He terms: {he_nf.n_terms()}")
    print(f"    Residual: {residual.n_terms()} terms")
    show_nf(residual, "Residual = 2s²2p²?")

    hist_r = histogram(residual)
    print(f"\n    Residual histogram: {hist_r}")
    print(f"    Residual palindromic: {is_pal(hist_r)}")

    # Step 4: Compare to standalone 4-electron chain with reduced Z_eff
    # Inner shell screens: Z_eff = 6 - 2 = 4 for valence electrons
    print(f"\n  COMPARISON: standalone 4-electron chain with Z_eff=4")
    val_types = ['nuc'] + ['e'] * 4
    val_nf, _ = build_chain(val_types, SymbolicHeckeDivision(),
                            "Valence shell (Z_eff=4)", Z_eff=4)
    show_nf(val_nf, "Standalone valence (Z_eff=4)")

    return he_nf, c_nf, residual


# ══════════════════════════════════════════════════════════════
# MODEL D: Electron-by-electron addition with running q-degree
# ══════════════════════════════════════════════════════════════

def model_D():
    print("\n" + "=" * 72)
    print("MODEL D: ELECTRON-BY-ELECTRON ADDITION")
    print("Build carbon by adding electrons one at a time.")
    print("Track: terms, palindromicity, net coefficient, q-degree")
    print("Look for discontinuity at electron 2 → 3 (shell boundary)")
    print("=" * 72)

    Z = 6
    types = ['nuc']
    div = SymbolicHeckeDivision()
    elem = SymbolicHeckeElement.identity()

    print(f"\n  {'e#':>3} {'strands':>8} {'terms':>6} {'net_coeff':>12} "
          f"{'PAL':>5} {'Δterms':>7} note")
    print(f"  {'-' * 60}")

    prev_terms = 1

    for e_idx in range(1, Z + 1):
        types.append('e')
        n = len(types)

        # Add crossings for new electron with all existing strands
        for i in range(n - 1):
            cx = crossing(types[i], 'e', i, Z_eff=Z)
            elem = elem * cx
            elem, _ = div.reduce(elem)

        hist = histogram(elem)
        pal = is_pal(hist)
        net = sum(elem.terms.values())
        net_val = float(net.subs(q, q0))
        n_terms = elem.n_terms()
        delta = n_terms - prev_terms

        note = ""
        if e_idx == 2:
            note = "← 1s² fills"
        elif e_idx == 3:
            note = "← 2s starts"
        elif e_idx == 4:
            note = "← 2s² fills"
        elif e_idx == 5:
            note = "← 2p starts"
        elif e_idx == 6:
            note = "← 2p² (carbon)"

        pal_str = "★" if pal else " "
        print(f"  {e_idx:>3} {n:>8} {n_terms:>6} {net_val:>+12.6f} "
              f"{pal_str:>5} {delta:>+7} {note}")

        prev_terms = n_terms

        # Show NF at key points
        if e_idx in (2, 3, 6):
            show_nf(elem, f"After electron #{e_idx}")


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    t0 = time.time()

    model_A()
    results_b = model_B()
    he_nf, c_nf, residual = model_C(results_b)
    model_D()

    print(f"\n{'=' * 72}")
    print(f"Total time: {time.time() - t0:.1f}s")
