#!/usr/bin/env python3
"""
Inductive atom construction with SYMBOLIC Gröbner basis.

All coefficients are exact in ℤ[q^½, q^{-½}]. No floating point
until final evaluation at q₀.

Phase 1: Nucleon-level NFs (p/n as unit strands)
  - D N(1,1): target 2 terms
  - ³H N(1,2): target 3 terms
  - ³He N(2,1): target 3 terms
  - ⁴He N(2,2): target 4 terms (palindromic check)

Phase 2: Q-values as exact polynomial differences
  - Q(³H→³He) = polynomial in q, evaluate at q₀

Phase 3: Quark-level with quotient ideals
  - Register protium NF as ℵ₁
  - Build deuterium with whole-atom quotient
  - Apply I₁-I₇ to reduce toward n_terms = n_strands

Usage:
    cd folio-assistant/computations
    python3 inductive-symbolic-atoms.py
"""

import sympy as sp
import json
import time
from datetime import datetime, timezone
from pathlib import Path

from hecke_symbolic import (
    SymbolicHeckeDivision, SymbolicHeckeElement,
    q, q_half, q_inv, q_half_inv,
    HA, s_skein, z_markov,
    C_PP, D_PP, C_NN, D_NN, C_MIX, D_MIX, C_HOPF, D_HOPF,
)

# ══════════════════════════════════════════════════════════════
# §1  NUCLEON-LEVEL COMPUTATION
# ══════════════════════════════════════════════════════════════

def build_nucleus_symbolic(p, n, div=None, label=""):
    """Build nucleus N(p,n) with exact symbolic coefficients.

    p: number of protons (strands of type 'p')
    n: number of neutrons (strands of type 'n')

    Returns (reduced_element, steps_dict).
    """
    if div is None:
        div = SymbolicHeckeDivision()

    A = p + n
    types = ['p'] * p + ['n'] * n

    if label:
        print(f"\n  N({p},{n}) [{label}]: {A} strands, H_{A}(q)")

    elem = SymbolicHeckeElement.identity()
    total_steps = {'hecke': 0, 'yb': 0, 'fc': 0, 'quotient': 0}

    for k in range(1, A):
        for i in range(k):
            # Build crossing element
            ti, tk = types[i], types[k]
            if ti == 'p' and tk == 'p':
                cx = SymbolicHeckeElement({(i,): C_PP})
            elif ti == 'n' and tk == 'n':
                cx = SymbolicHeckeElement({(i,): C_NN, (): D_NN})
            elif (ti == 'p' and tk == 'n') or (ti == 'n' and tk == 'p'):
                cx = SymbolicHeckeElement({(i,): C_MIX, (): D_MIX})
            else:
                cx = SymbolicHeckeElement({(i,): C_PP})

            elem = elem * cx
            elem, steps = div.reduce(elem)

            for key in total_steps:
                total_steps[key] += steps.get(key, 0)

    if label:
        print(f"    → {elem.n_terms()} terms (target: {A})")
        print(f"    Steps: {total_steps}")

    return elem, total_steps


def show_nf_symbolic(elem, name=""):
    """Display NF with symbolic coefficients, factored."""
    if name:
        print(f"\n  {name} NF (exact in q):")
    for w, c in sorted(elem.terms.items(), key=lambda x: (len(x[0]), x[0])):
        ws = " · ".join(f"σ_{i}" for i in w) if w else "𝟏"
        c_factored = sp.factor(c)
        print(f"    ({c_factored}) · {ws}")


def show_nf_evaluated(elem, q_val, name=""):
    """Display NF evaluated at specific q."""
    if name:
        print(f"\n  {name} at q₀ = {q_val}:")
    vals = elem.evaluate(q_val)
    for w, v in sorted(vals.items(), key=lambda x: (len(x[0]), x[0])):
        ws = " · ".join(f"σ_{i}" for i in w) if w else "𝟏"
        sign = "INPUT" if v < 0 else "OUTPUT"
        print(f"    {sign:>6} ({v:+.10f}) · {ws}")


# ══════════════════════════════════════════════════════════════
# §2  Q-VALUE AS EXACT POLYNOMIAL
# ══════════════════════════════════════════════════════════════

def compute_qvalue_polynomial(parent_elem, daughter_elem, n_strands, div):
    """Compute Q-value as exact polynomial difference.

    The Q-value comes from the difference in Markov traces:
      Q = |ln(tr_daughter) - ln(tr_parent)| × κ

    But at the symbolic level, we can compute:
      ΔNF = daughter_NF - parent_NF

    which gives the exact polynomial difference.
    """
    # Net coefficients (sum of all terms)
    net_parent = sum(parent_elem.terms.values())
    net_daughter = sum(daughter_elem.terms.values())
    delta_net = sp.simplify(net_daughter - net_parent)

    # Markov traces
    tr_parent = div.markov_trace(parent_elem, n_strands)
    tr_daughter = div.markov_trace(daughter_elem, n_strands)
    delta_trace = sp.simplify(tr_daughter - tr_parent)

    return {
        'net_parent': net_parent,
        'net_daughter': net_daughter,
        'delta_net': delta_net,
        'delta_net_factored': sp.factor(delta_net),
        'tr_parent': tr_parent,
        'tr_daughter': tr_daughter,
        'delta_trace': delta_trace,
    }


# ══════════════════════════════════════════════════════════════
# §3  PALINDROMIC CHECK
# ══════════════════════════════════════════════════════════════

def check_palindromic(elem):
    """Check if word-length histogram is palindromic.

    For He-4, expect {0:1, 1:3, 2:4, 3:3, 4:1} = Poincaré(S₄).
    """
    hist = {}
    for w in elem.terms:
        L = len(w)
        hist[L] = hist.get(L, 0) + 1

    lengths = sorted(hist.keys())
    counts = [hist[L] for L in lengths]

    is_palindrome = counts == counts[::-1]
    return {
        'histogram': dict(sorted(hist.items())),
        'counts': counts,
        'is_palindromic': is_palindrome,
    }


# ══════════════════════════════════════════════════════════════
# §4  QUARK-LEVEL COMPUTATION WITH QUOTIENT
# ══════════════════════════════════════════════════════════════

def build_quark_atom_symbolic(types, div=None, label=""):
    """Build atom at quark level with symbolic coefficients.

    types: list of quark/particle types
      'u' = up quark, 'd' = down quark, 'e' = electron

    Returns (reduced_element, steps_dict).
    """
    if div is None:
        div = SymbolicHeckeDivision()

    A = len(types)
    if label:
        print(f"\n  {label}: {A} strands, H_{A}(q)")

    elem = SymbolicHeckeElement.identity()
    total_steps = {'hecke': 0, 'yb': 0, 'fc': 0, 'quotient': 0}

    for k in range(1, A):
        for i in range(k):
            cx = div.crossing(types[i], types[k], i)
            elem = elem * cx
            elem, steps = div.reduce(elem)

            for key in total_steps:
                total_steps[key] += steps.get(key, 0)

        if label:
            print(f"    Step {k}: {elem.n_terms()} terms after adding strand {k}")

    if label:
        print(f"    → {elem.n_terms()} terms (target: {A})")
        print(f"    Steps: {total_steps}")

    return elem, total_steps


# ══════════════════════════════════════════════════════════════
# §5  MAIN COMPUTATION
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    import sys

    q0 = 1.10998  # q₀ for numerical evaluation
    kappa_approx = 0.510999 / 3  # m_e / 3 in MeV (approx)

    print("=" * 80)
    print("INDUCTIVE SYMBOLIC ATOM CONSTRUCTION")
    print(f"  All coefficients exact in ℤ[q^½, q^{{-½}}]")
    print("=" * 80)

    div = SymbolicHeckeDivision()

    # ── Phase 1: Nucleon-level NFs ──────────────────────────────

    print("\n" + "─" * 80)
    print("PHASE 1: NUCLEON-LEVEL NORMAL FORMS")
    print("─" * 80)

    t0 = time.time()

    # Deuterium N(1,1)
    D_nf, D_steps = build_nucleus_symbolic(1, 1, div, "Deuterium")
    show_nf_symbolic(D_nf, "D N(1,1)")
    show_nf_evaluated(D_nf, q0, "D N(1,1)")

    # Tritium N(1,2)
    H3_nf, H3_steps = build_nucleus_symbolic(1, 2, div, "Tritium")
    show_nf_symbolic(H3_nf, "³H N(1,2)")

    # Helium-3 N(2,1)
    He3_nf, He3_steps = build_nucleus_symbolic(2, 1, div, "Helium-3")
    show_nf_symbolic(He3_nf, "³He N(2,1)")

    # Helium-4 N(2,2)
    He4_nf, He4_steps = build_nucleus_symbolic(2, 2, div, "Helium-4")
    show_nf_symbolic(He4_nf, "⁴He N(2,2)")

    # Palindromic check for He-4
    pal = check_palindromic(He4_nf)
    print(f"\n  ⁴He palindromic check:")
    print(f"    Word-length histogram: {pal['histogram']}")
    print(f"    Counts: {pal['counts']}")
    print(f"    Palindromic: {'★ YES' if pal['is_palindromic'] else 'NO'}")

    t1 = time.time()
    print(f"\n  Phase 1 time: {t1-t0:.1f}s")

    # ── Phase 2: Q-values as exact polynomials ──────────────────

    print("\n" + "─" * 80)
    print("PHASE 2: Q-VALUES AS EXACT POLYNOMIALS")
    print("─" * 80)

    # Tritium → Helium-3 beta decay
    print("\n  ³H → ³He beta decay:")
    qval = compute_qvalue_polynomial(H3_nf, He3_nf, 3, div)

    print(f"    Net(³H)  = {sp.factor(qval['net_parent'])}")
    print(f"    Net(³He) = {sp.factor(qval['net_daughter'])}")
    print(f"    ΔNet     = {qval['delta_net_factored']}")

    # Evaluate at q₀
    delta_at_q0 = float(qval['delta_net'].subs(q, q0))
    print(f"\n    At q₀ = {q0}:")
    print(f"    ΔNet(q₀) = {delta_at_q0:+.10f}")

    # The Q-value relates to the trace ratio
    tr_H3 = float(qval['tr_parent'].subs(q, q0)) if qval['tr_parent'] != 0 else 0
    tr_He3 = float(qval['tr_daughter'].subs(q, q0)) if qval['tr_daughter'] != 0 else 0

    if tr_H3 != 0 and tr_He3 != 0:
        import math
        Q_trace = abs(math.log(abs(tr_He3)) - math.log(abs(tr_H3))) * kappa_approx
        print(f"    tr(³H)  = {tr_H3:.10f}")
        print(f"    tr(³He) = {tr_He3:.10f}")
        print(f"    Q_trace = |ln(tr_He3/tr_H3)| × κ = {Q_trace:.5f} MeV")
        print(f"    Q_exp   = 0.01861 MeV")
        if Q_trace > 0:
            print(f"    error   = {(Q_trace - 0.01861) / 0.01861 * 100:+.1f}%")

    # Q from net coefficient difference
    Q_net = abs(delta_at_q0) * kappa_approx
    print(f"\n    Q_net   = |ΔNet| × κ = {Q_net:.5f} MeV")

    # Also compute D → H (deuterium proton to neutron, sanity check)
    print("\n  D: net coefficient analysis:")
    net_D = float(sum(D_nf.terms.values()).subs(q, q0))
    print(f"    Net(D) at q₀ = {net_D:+.10f}")

    t2 = time.time()
    print(f"\n  Phase 2 time: {t2-t1:.1f}s")

    # ── Phase 3: Quark-level protium with symbolic q ─────────────

    print("\n" + "─" * 80)
    print("PHASE 3: QUARK-LEVEL PROTIUM (SYMBOLIC)")
    print("─" * 80)

    div_quark = SymbolicHeckeDivision()
    protium_types = ['u', 'u', 'd', 'e']

    protium_nf, protium_steps = build_quark_atom_symbolic(
        protium_types, div_quark, "Protium ℵ(1,0) = B₃(u,u,d) + e⁻")
    show_nf_symbolic(protium_nf, "Protium")
    show_nf_evaluated(protium_nf, q0, "Protium")

    # Register protium NF as quotient relation ℵ₁
    div_quark.register_quotient(-1, protium_nf, name="protium")
    print(f"\n  Registered protium as ℵ₁ ({protium_nf.n_terms()} terms)")

    # ── Phase 3b: Neutron at quark level ─────────────────────────

    neutron_types = ['u', 'd', 'd']
    print("\n  Building neutron B₃(u,d,d) for Q-value comparison...")
    neutron_nf, neutron_steps = build_quark_atom_symbolic(
        neutron_types, SymbolicHeckeDivision(), "Neutron B₃(u,d,d)")
    show_nf_symbolic(neutron_nf, "Neutron")

    proton_types = ['u', 'u', 'd']
    proton_nf, proton_steps = build_quark_atom_symbolic(
        proton_types, SymbolicHeckeDivision(), "Proton B₃(u,u,d)")
    show_nf_symbolic(proton_nf, "Proton")

    # g_A from quark-level amplitude ratio
    net_proton = sum(proton_nf.terms.values())
    net_neutron = sum(neutron_nf.terms.values())
    g_A_symbolic = sp.simplify(sp.Abs(net_proton / net_neutron))
    g_A_numeric = abs(float(net_proton.subs(q, q0)) / float(net_neutron.subs(q, q0)))

    print(f"\n  g_A = |α_proton / α_neutron|:")
    print(f"    Symbolic: {sp.factor(net_proton)} / {sp.factor(net_neutron)}")
    print(f"    At q₀:    {g_A_numeric:.6f}")
    print(f"    PDG:      1.2754 ± 0.0013")
    print(f"    Error:    {(g_A_numeric - 1.2754) / 1.2754 * 100:+.1f}%")

    # ── Phase 3c: Deuterium at quark level WITH quotient ─────────

    print("\n  Building deuterium at quark level WITH quotient...")
    print("  (7 strands: u_r, u_g, d_b, u_r2, d_g2, d_b2, e⁻)")

    deuterium_quark_types = ['u', 'u', 'd', 'u', 'd', 'd', 'e']
    deut_nf, deut_steps = build_quark_atom_symbolic(
        deuterium_quark_types, div_quark,
        "Deuterium ℵ(1,1) WITH ℵ₁ quotient")

    print(f"\n  Deuterium (quark-level):")
    print(f"    Terms: {deut_nf.n_terms()} (target: 7)")
    print(f"    Steps: {deut_steps}")
    print(f"    Quotient reductions: {deut_steps.get('quotient', 0)}")

    # Show word histogram
    hist = {}
    for w in deut_nf.terms:
        L = len(w)
        hist[L] = hist.get(L, 0) + 1
    print(f"    Word-length histogram: {dict(sorted(hist.items()))}")

    # Count formal variables in terms
    formal_count = sum(1 for w in deut_nf.terms if any(g < 0 for g in w))
    print(f"    Terms containing ℵ₁: {formal_count}")

    # Analyze deuterium NF structure
    print(f"\n  DEUTERIUM NF STRUCTURE ANALYSIS:")

    # Count terms by formal variable content
    pure_sigma = 0
    has_formal = 0
    formal_counts = {}  # how many ℵ₁ per term
    for w, c in deut_nf.terms.items():
        n_formal = sum(1 for g in w if g < 0)
        n_sigma = sum(1 for g in w if g >= 0)
        if n_formal == 0:
            pure_sigma += 1
        else:
            has_formal += 1
        formal_counts[n_formal] = formal_counts.get(n_formal, 0) + 1

    print(f"    Pure σ terms (no ℵ₁): {pure_sigma}")
    print(f"    Terms with ℵ₁: {has_formal}")
    print(f"    Formal variable count distribution: {dict(sorted(formal_counts.items()))}")

    # Show a few representative terms evaluated
    print(f"\n    Top 10 terms by |coefficient| at q₀:")
    vals = deut_nf.evaluate(q0)
    sorted_terms = sorted(vals.items(), key=lambda x: -abs(x[1]))[:10]
    for w, v in sorted_terms:
        ws_parts = []
        for g in w:
            if g < 0:
                ws_parts.append(f"ℵ{-g}")
            else:
                ws_parts.append(f"σ_{g}")
        ws = " · ".join(ws_parts) if ws_parts else "𝟏"
        sign = "INPUT" if v < 0 else "OUTPUT"
        print(f"      {sign:>6} ({v:+.8f}) · {ws}")

    # Identify generator content classes
    content_classes = {}
    for w in deut_nf.terms:
        # Content = sorted set of generators used (ignoring formal vars)
        gens = tuple(sorted(g for g in w if g >= 0))
        content_classes.setdefault(gens, []).append(w)

    print(f"\n    Generator content classes: {len(content_classes)}")
    print(f"    Classes with multiple members (YB-related):")
    for gens, words in sorted(content_classes.items()):
        if len(words) > 1:
            print(f"      {gens}: {len(words)} members")

    t3 = time.time()
    print(f"\n  Phase 3 time: {t3-t2:.1f}s")

    # ── Summary ──────────────────────────────────────────────────

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    print(f"\n  NUCLEON-LEVEL NFs (exact in q):")
    print(f"  {'Nucleus':>10} {'Strands':>8} {'Terms':>6} {'Target':>7} {'Status':>15}")
    print(f"  {'-'*50}")
    for name, nf, p, n in [("D N(1,1)", D_nf, 1, 1),
                           ("³H N(1,2)", H3_nf, 1, 2),
                           ("³He N(2,1)", He3_nf, 2, 1),
                           ("⁴He N(2,2)", He4_nf, 2, 2)]:
        A = p + n
        status = "OPTIMAL ★" if nf.n_terms() == A else f"{nf.n_terms() - A} over"
        print(f"  {name:>10} {A:>8} {nf.n_terms():>6} {A:>7} {status:>15}")

    if pal['is_palindromic']:
        print(f"\n  ⁴He palindromic: {pal['counts']} = Poincaré(S₄) ★")

    print(f"\n  QUARK-LEVEL (exact in q):")
    print(f"  {'Particle':>10} {'Strands':>8} {'Terms':>6} {'Target':>7}")
    print(f"  {'-'*35}")
    print(f"  {'Proton':>10} {3:>8} {proton_nf.n_terms():>6} {3:>7}")
    print(f"  {'Neutron':>10} {3:>8} {neutron_nf.n_terms():>6} {3:>7}")
    print(f"  {'Protium':>10} {4:>8} {protium_nf.n_terms():>6} {4:>7}")
    print(f"  {'Deuterium':>10} {7:>8} {deut_nf.n_terms():>6} {7:>7}")

    print(f"\n  g_A = {g_A_numeric:.6f} (PDG: 1.2754)")

    print(f"\n  Total time: {t3-t0:.1f}s")
