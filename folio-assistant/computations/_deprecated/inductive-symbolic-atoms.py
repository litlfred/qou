#!/usr/bin/env python3
# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Inductive atom construction with SYMBOLIC Gröbner--Shirshov basis.

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

import sys
import sympy as sp
import json
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as _Q_CANONICAL
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

    For He-4, expect {0:1, 1:3, 2:4, 3:3, 4:1} — palindromic over the occupied support.
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

    q0 = _Q_CANONICAL  # q₀ for numerical evaluation (from q_parameter)
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

    # ── Poincaré duality check for He-4 ──────────────────────────

    print(f"\n  POINCARÉ DUALITY CHECK (He-4):")
    print(f"    S₄ has 24 elements, longest w₀ has length 6 = 4·3/2")
    print(f"    Duality: w ↔ w₀·w maps length ℓ to length 6−ℓ")
    print(f"    Occupied cells: {He4_nf.n_terms()} / 24 ({He4_nf.n_terms()/24*100:.0f}%)")
    print()

    # For each occupied word at length ℓ, check if dual at length 6-ℓ exists
    he4_by_length = {}
    for w, c in He4_nf.terms.items():
        L = len(w)
        he4_by_length.setdefault(L, []).append((w, c))

    print(f"    {'Length':>6} {'Terms':>5} {'Dual len':>8} {'Dual terms':>10}")
    print(f"    {'-'*35}")
    max_len = max(len(w) for w in He4_nf.terms) if He4_nf.terms else 0
    for L in sorted(he4_by_length.keys()):
        dual_L = max_len - L
        n_at_L = len(he4_by_length[L])
        n_at_dual = len(he4_by_length.get(dual_L, []))
        match = "★" if n_at_L == n_at_dual else "✗"
        print(f"    {L:>6} {n_at_L:>5} {dual_L:>8} {n_at_dual:>10} {match}")

    # Check coefficient pairing more carefully
    print(f"\n    Coefficient pairing at q₀ = {q0}:")
    he4_vals = He4_nf.evaluate(q0)
    for L in sorted(he4_by_length.keys()):
        dual_L = max_len - L
        if dual_L < L:
            continue  # avoid double-printing
        terms_L = sorted(he4_by_length[L], key=lambda x: x[0])
        terms_dual = sorted(he4_by_length.get(dual_L, []), key=lambda x: x[0])
        if terms_L and terms_dual:
            vals_L = sorted([float(c.subs(q, q0)) for _, c in terms_L])
            vals_dual = sorted([float(c.subs(q, q0)) for _, c in terms_dual])
            # Check if signs match
            signs_L = ['+' if v > 0 else '-' for v in vals_L]
            signs_dual = ['+' if v > 0 else '-' for v in vals_dual]
            print(f"      ℓ={L} ↔ ℓ={dual_L}: "
                  f"signs={signs_L} ↔ {signs_dual}")

    # ── Duality check against FULL Bruhat lattice ─────────────

    def bruhat_duality_check(nf, n_strands, name):
        """Check Poincaré duality against the full S_n Bruhat lattice.

        The longest element w₀ has length n(n-1)/2.
        Duality: w ↔ w₀·w maps length ℓ to length n(n-1)/2 − ℓ.
        Self-dual occupancy = palindromic histogram over FULL range.
        """
        max_bruhat = n_strands * (n_strands - 1) // 2
        print(f"\n  {name} DUALITY CHECK (vs FULL S_{n_strands} Bruhat lattice):")
        print(f"    |S_{n_strands}| = {sp.factorial(n_strands)}, "
              f"longest w₀ length = {max_bruhat}")

        by_length = {}
        for w, c in nf.terms.items():
            L = len(w)
            by_length.setdefault(L, []).append((w, c))

        # Build full histogram 0..max_bruhat
        full_hist = [len(by_length.get(L, [])) for L in range(max_bruhat + 1)]
        is_palindrome = full_hist == full_hist[::-1]

        print(f"    Occupied: {nf.n_terms()} / {sp.factorial(n_strands)}")
        print(f"    Full histogram [0..{max_bruhat}]: {full_hist}")
        print(f"    Self-dual (palindromic): {'★ YES' if is_palindrome else '✗ NO'}")

        if not is_palindrome:
            # Show the defects
            defects = []
            for L in range(max_bruhat + 1):
                dual_L = max_bruhat - L
                n_L = full_hist[L]
                n_dual = full_hist[dual_L]
                if n_L != n_dual:
                    defects.append((L, n_L, dual_L, n_dual))
            if defects:
                print(f"    Duality defects:")
                for L, n_L, dual_L, n_dual in defects:
                    print(f"      ℓ={L} ({n_L} terms) ↔ "
                          f"ℓ={dual_L} ({n_dual} terms) — "
                          f"{'excess' if n_L > n_dual else 'deficit'} at ℓ={L}")

        return is_palindrome

    bruhat_duality_check(He4_nf, 4, "He-4")
    bruhat_duality_check(H3_nf, 3, "Tritium")
    bruhat_duality_check(He3_nf, 3, "He-3")
    bruhat_duality_check(D_nf, 2, "Deuterium")

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

    # ── Phase 3c: Collapse formal powers ──────────────────────────

    print(f"\n  COLLAPSE: ℵ₁·ℵ₁·...·ℵ₁ → ℵ₁^n")
    deut_collapsed, n_collapses, collapse_info = div_quark.collapse_formal_powers(deut_nf)
    print(f"    Collapses: {n_collapses}")
    print(f"    Terms before: {deut_nf.n_terms()}")
    print(f"    Terms after:  {deut_collapsed.n_terms()}")

    if collapse_info:
        # Summarize completeness levels
        comp_levels = {}
        for ci in collapse_info:
            key = (ci['run_len'], ci['n_components'])
            comp_levels[key] = comp_levels.get(key, 0) + 1
        print(f"    Completeness distribution:")
        for (run, total), count in sorted(comp_levels.items()):
            print(f"      ℵ₁^{run} (completeness {run}/{total} = {run/total:.1%}): {count} terms")

    # Factor content classes on collapsed result
    classes = div_quark.factor_content_classes(deut_collapsed)
    print(f"\n    Content classes after collapse: {len(classes)}")

    # Show collapsed NF histogram
    hist_c = {}
    for w in deut_collapsed.terms:
        L = len(w)
        hist_c[L] = hist_c.get(L, 0) + 1
    print(f"    Word-length histogram: {dict(sorted(hist_c.items()))}")

    # ── Phase 3d: Identify I₄ neutron tail pattern ────────────────

    print(f"\n  I₄ NEUTRON TAIL ANALYSIS:")
    neutron_tail = (3, 4, 3, 5)  # σ₃·σ₄·σ₃·σ₅

    has_tail = 0
    no_tail = 0
    for w in deut_collapsed.terms:
        sigma_part = tuple(g for g in w if g >= 0)
        if len(sigma_part) >= 4:
            # Check if neutron tail appears as sub-sequence
            found = False
            for pos in range(len(sigma_part) - 3):
                if sigma_part[pos:pos+4] == neutron_tail:
                    found = True
                    break
            if found:
                has_tail += 1
            else:
                no_tail += 1
        else:
            no_tail += 1

    print(f"    Terms with 𝔫₁ = σ₃·σ₄·σ₃·σ₅: {has_tail}")
    print(f"    Terms without 𝔫₁: {no_tail}")
    if has_tail + no_tail > 0:
        print(f"    𝔫₁ prevalence: {has_tail/(has_tail+no_tail)*100:.0f}%")

    # ── Phase 3e: Show top terms of collapsed NF ──────────────────

    print(f"\n    Top 15 collapsed terms by |coeff| at q₀:")
    vals_c = deut_collapsed.evaluate(q0)
    sorted_c = sorted(vals_c.items(), key=lambda x: -abs(x[1]))[:15]
    for w, v in sorted_c:
        ws_parts = []
        for g in w:
            if g < -100:
                # Collapsed formal variable
                atom_k = (-g) // 1000
                run = (-g) % 1000
                ws_parts.append(f"ℵ{atom_k}^{run}")
            elif g < 0:
                ws_parts.append(f"ℵ{-g}")
            else:
                ws_parts.append(f"σ_{g}")
        ws = " · ".join(ws_parts) if ws_parts else "𝟏"
        sign = "INPUT" if v < 0 else "OUTPUT"
        print(f"      {sign:>6} ({v:+.6f}) · {ws}")

    # ── Phase 3f: Completeness layer analysis ────────────────────

    print(f"\n  COMPLETENESS LAYER ANALYSIS:")
    layers = div_quark.extract_completeness_layers(deut_nf, atom_id=-1)
    for n_formal in sorted(layers.keys(), reverse=True):
        layer = layers[n_formal]
        n_comp = 4  # protium has 4 NF terms
        completeness = n_formal / n_comp if n_comp > 0 else 0
        net = sum(layer.terms.values())
        net_val = float(net.subs(q, q0))
        print(f"    ℵ₁^{n_formal} (completeness {completeness:.0%}): "
              f"{layer.n_terms()} terms, net={net_val:+.6f}")

        if n_formal == 4:
            print(f"      ↑ THIS IS THE ATOM (full protium completion)")
            print(f"      Words in ℵ₁⁴ layer:")
            for w, c in sorted(layer.terms.items(), key=lambda x: (len(x[0]), x[0])):
                ws_parts = []
                for g in w:
                    if g < 0:
                        ws_parts.append(f"ℵ₁")
                    else:
                        ws_parts.append(f"σ_{g}")
                ws = " · ".join(ws_parts)
                c_val = float(c.subs(q, q0))
                print(f"        ({c_val:+.6f}) · {ws}")

    # ── Phase 3g: Three-part decomposition ──────────────────────

    print(f"\n  THREE-PART NF DECOMPOSITION:")
    vals_all = deut_nf.evaluate(q0)
    inputs = [(w, v) for w, v in vals_all.items() if v < 0]
    outputs = [(w, v) for w, v in vals_all.items() if v > 0]

    # Separate outputs into observable (ℵ₁⁴) and mediator (not ℵ₁⁴)
    observable = [(w, v) for w, v in outputs
                  if sum(1 for g in w if g == -1) == 4]
    mediator = [(w, v) for w, v in outputs
                if sum(1 for g in w if g == -1) != 4]

    sum_input = sum(v for _, v in inputs)
    sum_observable = sum(v for _, v in observable)
    sum_mediator = sum(v for _, v in mediator)

    print(f"    INPUTS (negative):     {len(inputs)} terms, sum = {sum_input:+.6f}")
    print(f"    MEDIATOR (pos, <ℵ₁⁴): {len(mediator)} terms, sum = {sum_mediator:+.6f}")
    print(f"    OBSERVABLE (pos, ℵ₁⁴): {len(observable)} terms, sum = {sum_observable:+.6f}")
    print(f"    Total net: {sum_input + sum_observable + sum_mediator:+.6f}")

    if sum_observable != 0:
        g_A_quark = abs(sum_observable / (sum_observable + sum_input))
        print(f"\n    g_A(quark) = |observable/(observable+input)| = {g_A_quark:.6f}")

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
        print(f"\n  ⁴He palindromic: {pal['counts']} = palindromic over support ★")

    print(f"\n  QUARK-LEVEL (exact in q):")
    print(f"  {'Particle':>10} {'Strands':>8} {'Terms':>6} {'Target':>7}")
    print(f"  {'-'*35}")
    print(f"  {'Proton':>10} {3:>8} {proton_nf.n_terms():>6} {3:>7}")
    print(f"  {'Neutron':>10} {3:>8} {neutron_nf.n_terms():>6} {3:>7}")
    print(f"  {'Protium':>10} {4:>8} {protium_nf.n_terms():>6} {4:>7}")
    print(f"  {'Deuterium':>10} {7:>8} {deut_nf.n_terms():>6} {7:>7}")

    print(f"\n  g_A = {g_A_numeric:.6f} (PDG: 1.2754)")

    print(f"\n  Total time: {t3-t0:.1f}s")
