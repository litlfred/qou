#!/usr/bin/env python3
"""
Gröbner--Shirshov normal form witness for the free neutrino.

Physics: In beta decay  n → p + e⁻ + ν̄ₑ, the neutrino is the residual
after the proton and electron have been accounted for.  Algebraically in
H₃(q), the neutrino sector is what remains when we compose the proton
and electron braids, apply the weak vertex T₃,₅, and Gröbner--Shirshov-reduce.

Procedure:
  1. Build NF(proton)   = NF([u,u,d]) at quark level in H₃(q)
  2. Build NF(electron)  = NF(σ₀³) = trefoil T_{2,3}
  3. Compose:  word = NF(proton) · NF(electron)
  4. Compose:  word = word · NF(T₃,₅)
  5. Gröbner--Shirshov-reduce, showing each intermediate step
  6. Identify each resulting NF term as a particle
  7. Extract the ν-sector coefficient as the free neutrino witness
  8. Verify via Markov trace and crossing budget

The key result: NF(proton · electron · T₃,₅) decomposes over the
H₃(q) Gröbner--Shirshov basis, and the coefficient on 𝟏 (the identity / unknot)
is the neutrino sector — confirming that the free neutrino is the
identity braid with a specific, non-trivial coefficient from the
Gröbner--Shirshov reduction.

Depends on: hecke_symbolic.py, q_parameter.py, experimental_constants.py
"""

import json
import math
import sympy as sp
from datetime import datetime, timezone

from hecke_symbolic import (
    SymbolicHeckeDivision, SymbolicHeckeElement,
    q, HA, s_skein, z_markov, C_PP, C_NN, C_MIX, D_PP, D_NN, D_MIX,
)
from q_parameter import Q as q0, E_CROSS, HBAR_Q, Q_INV as q0_inv
from experimental_constants import M_E_MEV, KAPPA
from witness_polynomial import expose_polynomial


# ════════════════════════════════════════════════════════════════
# SETUP
# ════════════════════════════════════════════════════════════════

div = SymbolicHeckeDivision()

# Scale factor: m_e / (3 × E_cross)
E_cross_num = float(E_CROSS)
mu_0 = M_E_MEV / (3 * E_cross_num)

# ── Particle–knot dictionary ────────────────────────────────────
PARTICLE_KNOT = {
    ():         ("ν",   "K₀  (unknot)",       0, "neutrino sector"),
    (0,):       ("σ₀",  "T₂,₁⁽⁰⁾ (Hopf gen)", 1, "Hopf crossing gen 0"),
    (1,):       ("σ₁",  "T₂,₁⁽¹⁾ (Hopf gen)", 1, "Hopf crossing gen 1"),
    (0, 1):     ("L₊",  "L₂,₁  (Hopf link)",  2, "Hopf pair (positive)"),
    (1, 0):     ("L₋",  "L₂,₁' (Hopf rev)",   2, "Hopf pair (reversed)"),
    (0, 1, 0):  ("e⁻",  "T₂,₃  (trefoil 3₁)", 3, "electron (Garside Δ₃)"),
}


def particle_name(w):
    return PARTICLE_KNOT.get(w, ("?", "unknown", len(w), ""))[0]


def particle_knot(w):
    return PARTICLE_KNOT.get(w, ("?", f"word({w})", len(w), "unknown"))


def word_str(w):
    if not w:
        return "𝟏"
    return " · ".join(f"σ_{i}" for i in w)


def particle_word_str(w):
    pn = particle_name(w)
    ws = word_str(w)
    return f"{ws}  [{pn}]"


def eval_element(elem, q_val):
    result = []
    for w, c in elem.terms.items():
        v = float(c.subs(q, q_val))
        if abs(v) > 1e-15:
            result.append((w, v))
    return sorted(result, key=lambda x: (len(x[0]), x[0]))


def factor_coefficient(c):
    c = sp.simplify(c)
    c_factored = sp.factor(c)
    s = str(c_factored)
    s = s.replace("sqrt(q)", "q^½")
    return s


def show_element(name, elem, indent=4):
    pad = " " * indent
    print(f"{pad}{name}: ({elem.n_terms()} terms)")
    for w, c in sorted(elem.terms.items(), key=lambda x: (len(x[0]), x[0])):
        c_simplified = sp.simplify(c)
        print(f"{pad}  ({c_simplified}) · {particle_word_str(w)}")


def show_element_numeric(name, elem, q_val, indent=4):
    pad = " " * indent
    print(f"{pad}{name} at q₀:")
    for w, v in eval_element(elem, q_val):
        print(f"{pad}  ({v:+.10f}) · {particle_word_str(w)}")


def show_nf_shape(name, elem, indent=4):
    pad = " " * indent
    print(f"{pad}┌─────────────────────────────────────────────────")
    print(f"{pad}│ SHAPE OF {name}")
    print(f"{pad}├─────────────────────────────────────────────────")

    all_words = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
    occupied = []
    signs = []

    for w in all_words:
        pn = particle_name(w)
        c = elem.terms.get(w, sp.Integer(0))
        c_simplified = sp.simplify(c)
        v = float(c_simplified.subs(q, q0)) if c_simplified != 0 else 0.0

        if abs(v) < 1e-15:
            print(f"{pad}│  {pn:<4}  ·····  (empty)")
        else:
            sign = "+" if v > 0 else "−"
            signs.append(sign)
            occupied.append(pn)
            c_str = factor_coefficient(c_simplified)
            if len(c_str) > 60:
                c_str = c_str[:57] + "..."
            print(f"{pad}│  {pn:<4}  {sign}{abs(v):.6f}  {c_str}")

    print(f"{pad}├─────────────────────────────────────────────────")
    occ_str = " ".join(occupied)
    sign_str = " ".join(signs)
    print(f"{pad}│  Occupied sectors: [{occ_str}]")
    print(f"{pad}│  Sign pattern:     [{sign_str}]")
    print(f"{pad}│  Term count: {len(occupied)} / 6")
    print(f"{pad}└─────────────────────────────────────────────────")
    print()


def terms_to_dict(elem, q_val):
    """Convert SymbolicHeckeElement to JSON-serializable dict."""
    result = {}
    for w, c in sorted(elem.terms.items(), key=lambda x: (len(x[0]), x[0])):
        ws = ".".join(f"s{i}" for i in w) if w else "1"
        pn, knot, ncx, desc = particle_knot(w)
        result[ws] = {
            "symbolic": str(sp.simplify(c)),
            "at_q0": float(c.subs(q, q_val)),
            "particle": pn,
            "knot": knot,
            "crossings": ncx,
            "description": desc,
        }
    return result


def markov_trace_symbolic(elem, n_strands):
    return div.markov_trace(elem, n_strands)


# ════════════════════════════════════════════════════════════════
# Builders (same as tritium script)
# ════════════════════════════════════════════════════════════════

def build_nucleus_nf(types_list, label="nucleus"):
    """Build the Gröbner--Shirshov normal form for a nucleus at quark level.

    The nucleus is constructed as B₃ · (pairwise crossings), where
    B₃ = (σ₀σ₁⁻¹)³ is the Borromean confinement braid.
    """
    A = len(types_list)
    total_steps = {'hecke': 0, 'yb': 0, 'fc': 0, 'quotient': 0}

    # Start with Borromean confinement braid B₃ = (σ₀σ₁⁻¹)³
    elem, b3_steps = div.borromean_B3()
    for k in b3_steps:
        total_steps[k] += b3_steps[k]

    # Multiply pairwise crossing elements
    for i in range(A - 1):
        for j in range(i + 1, A):
            cx = div.crossing(types_list[i], types_list[j], i)
            elem = elem * cx
            elem, steps = div.reduce(elem)
            for k in steps:
                total_steps[k] += steps[k]

    return elem, total_steps


def build_T35():
    """Build T_{3,5} = (σ₀σ₁)⁵ weak vertex braid and reduce."""
    s0 = SymbolicHeckeElement({(0,): sp.Integer(1)})
    s1 = SymbolicHeckeElement({(1,): sp.Integer(1)})

    elem = SymbolicHeckeElement.identity()
    for _ in range(5):
        elem = elem * s0 * s1

    reduced, steps = div.reduce(elem)
    return reduced, steps


def build_electron():
    """Build the electron as the trefoil T_{2,3} = σ₀³ in H₂(q).

    In H₃(q), we use the Garside element Δ₃ = σ₀σ₁σ₀ (same trefoil).
    """
    s0 = SymbolicHeckeElement({(0,): sp.Integer(1)})
    s1 = SymbolicHeckeElement({(1,): sp.Integer(1)})
    # Garside element Δ₃ = σ₀σ₁σ₀ (trefoil as 3-braid, 3 crossings)
    elem = s0 * s1 * s0
    reduced, steps = div.reduce(elem)
    return reduced, steps


# ════════════════════════════════════════════════════════════════
#  STEP-BY-STEP REDUCTION TRACKER
# ════════════════════════════════════════════════════════════════

def reduce_stepwise(div_inst, elem, label="reduction"):
    """Reduce with step-by-step logging.

    Returns (reduced_elem, total_steps, step_log).
    step_log is a list of dicts recording each rule application.
    """
    total_steps = {'hecke': 0, 'yb': 0, 'fc': 0, 'quotient': 0}
    step_log = []
    iteration = 0
    max_iterations = 10000

    changed = True
    while changed and iteration < max_iterations:
        changed = False
        new_terms = {}

        for word, coeff in elem.terms.items():
            if coeff == 0:
                continue

            reduced_this = False

            # Rule 1: Hecke — σ_i² → (q−q⁻¹)σ_i + 1
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1] and word[pos] >= 0:
                    i = word[pos]
                    prefix = word[:pos]
                    suffix = word[pos + 2:]

                    w1 = prefix + (i,) + suffix
                    c1 = sp.expand(coeff * div_inst.hecke_a)
                    w2 = prefix + suffix
                    c2 = sp.expand(coeff * div_inst.hecke_b)

                    new_terms[w1] = sp.expand(new_terms.get(w1, sp.Integer(0)) + c1)
                    new_terms[w2] = sp.expand(new_terms.get(w2, sp.Integer(0)) + c2)

                    total_steps['hecke'] += 1
                    step_log.append({
                        'rule': 'R1 (Hecke)',
                        'detail': f"σ_{i}² → (q−q⁻¹)σ_{i} + 1",
                        'word_before': word_str(word),
                        'split_into': [word_str(w1), word_str(w2)],
                        'iteration': iteration,
                    })
                    reduced_this = True
                    changed = True
                    break

            if reduced_this:
                continue

            # Rule 2: Far-comm
            for pos in range(len(word) - 1):
                i_gen, j_gen = word[pos], word[pos + 1]
                if i_gen >= 0 and j_gen < 0:
                    new_word = word[:pos] + (j_gen, i_gen) + word[pos + 2:]
                    new_terms[new_word] = sp.expand(
                        new_terms.get(new_word, sp.Integer(0)) + coeff)
                    total_steps['fc'] += 1
                    step_log.append({
                        'rule': 'R2 (Far-comm)',
                        'detail': f"σ_{i_gen}·ℵ_{abs(j_gen)} → ℵ_{abs(j_gen)}·σ_{i_gen}",
                        'word_before': word_str(word),
                        'word_after': word_str(new_word),
                        'iteration': iteration,
                    })
                    reduced_this = True
                    changed = True
                    break
                if (abs(i_gen - j_gen) >= 2 and i_gen > j_gen
                        and i_gen >= 0 and j_gen >= 0):
                    new_word = word[:pos] + (j_gen, i_gen) + word[pos + 2:]
                    new_terms[new_word] = sp.expand(
                        new_terms.get(new_word, sp.Integer(0)) + coeff)
                    total_steps['fc'] += 1
                    step_log.append({
                        'rule': 'R2 (Far-comm)',
                        'detail': f"σ_{i_gen}·σ_{j_gen} → σ_{j_gen}·σ_{i_gen}",
                        'word_before': word_str(word),
                        'word_after': word_str(new_word),
                        'iteration': iteration,
                    })
                    reduced_this = True
                    changed = True
                    break

            if reduced_this:
                continue

            # Rule 3: Yang-Baxter
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and a >= 0 and b >= 0 and abs(a - b) == 1:
                    new_trip = (b, a, b)
                    old_trip = (a, b, a)
                    if new_trip < old_trip:
                        new_word = word[:pos] + new_trip + word[pos + 3:]
                        new_terms[new_word] = sp.expand(
                            new_terms.get(new_word, sp.Integer(0)) + coeff)
                        total_steps['yb'] += 1
                        step_log.append({
                            'rule': 'R3 (Yang-Baxter)',
                            'detail': (f"σ_{a}·σ_{b}·σ_{a} → "
                                       f"σ_{b}·σ_{a}·σ_{b}"),
                            'word_before': word_str(word),
                            'word_after': word_str(new_word),
                            'iteration': iteration,
                        })
                        reduced_this = True
                        changed = True
                        break

            if not reduced_this:
                new_terms[word] = sp.expand(
                    new_terms.get(word, sp.Integer(0)) + coeff)

        elem = SymbolicHeckeElement(new_terms)
        iteration += 1

    return elem, total_steps, step_log


# ════════════════════════════════════════════════════════════════
#  MAIN COMPUTATION
# ════════════════════════════════════════════════════════════════

print("=" * 80)
print("FREE NEUTRINO WITNESS: NF(proton · electron · T₃,₅)")
print("Gröbner--Shirshov normal form computation in H₃(q)")
print("All coefficients exact in ℤ[q^½, q^{-½}]")
print("=" * 80)
print()

# ── Particle–knot legend ──
print("  PARTICLE–KNOT DICTIONARY  (H₃(q) Gröbner--Shirshov basis ↔ particle sector)")
print("  ┌────────────┬────────┬────────────────────┬──────────────────────────┐")
print("  │ Braid word │ Cross. │ Closure knot       │ Particle name            │")
print("  ├────────────┼────────┼────────────────────┼──────────────────────────┤")
for w in [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]:
    sym, knot, n_cx, desc = particle_knot(w)
    ws = word_str(w)
    print(f"  │ {ws:<10} │ {n_cx:>6} │ {knot:<18} │ {sym:<4} {desc:<20} │")
print("  └────────────┴────────┴────────────────────┴──────────────────────────┘")
print()


# ════════════════════════════════════════════════════════════════
# STEP 1: Build NF(proton) at quark level
# ════════════════════════════════════════════════════════════════

print("─" * 60)
print("STEP 1: NF(proton) = NF([u, u, d]) at quark level")
print("─" * 60)
print()
print("  Quark assignment: [u₁=strand 0, u₂=strand 1, d=strand 2] in B₃")
print("  Crossings:")
print("    (u₁, u₂) at gen 0 → u-u:  σ₀")
print("    (u₁, d)  at gen 0 → mixed: ((1+q²)/2)·σ₀ + (−q·s/2)·ν")
print("    (u₂, d)  at gen 1 → mixed: ((1+q²)/2)·σ₁ + (−q·s/2)·ν")
print()

proton, steps_p = build_nucleus_nf(['u', 'u', 'd'], "proton")
show_element("NF(proton)", proton)
print()
print(f"  Reduction steps: {steps_p}")
print()
show_element_numeric("NF(proton)", proton, q0)
show_nf_shape("NF(proton)", proton)

tr_p = markov_trace_symbolic(proton, 3)
tr_p_num = float(tr_p.subs(q, q0))
print(f"  Markov trace (symbolic): {sp.simplify(tr_p)}")
print(f"  Markov trace at q₀:     {tr_p_num:.10f}")
print(f"  ln|tr(proton)|:          {math.log(abs(tr_p_num)):.10f}")


# ════════════════════════════════════════════════════════════════
# STEP 2: Build NF(electron) = NF(σ₀σ₁σ₀) = Garside Δ₃
# ════════════════════════════════════════════════════════════════

print()
print("─" * 60)
print("STEP 2: NF(electron) = NF(σ₀σ₁σ₀) = Garside Δ₃")
print("  (trefoil T₂,₃ as a 3-braid, 3 crossings)")
print("─" * 60)
print()
print("  Unreduced word: σ₀ · σ₁ · σ₀ (3 crossings)")
print("  Gröbner--Shirshov reduction:")
print("    σ₀σ₁σ₀: check R1 (Hecke) — no adjacent equal generators")
print("    σ₀σ₁σ₀: check R3 (YB) — σ₀σ₁σ₀ → σ₁σ₀σ₁  (since (0,1,0) > (1,0,1) lexically? No: (0,1,0) < (1,0,1))")
print("    σ₀σ₁σ₀ is already in NF!  (no rule applies)")
print()

electron, steps_e = build_electron()
show_element("NF(electron)", electron)
print()
print(f"  Reduction steps: {steps_e}")
print()
show_element_numeric("NF(electron)", electron, q0)
show_nf_shape("NF(electron)", electron)

tr_e = markov_trace_symbolic(electron, 3)
tr_e_num = float(tr_e.subs(q, q0))
print(f"  Markov trace (symbolic): {sp.simplify(tr_e)}")
print(f"  Markov trace at q₀:     {tr_e_num:.10f}")


# ════════════════════════════════════════════════════════════════
# STEP 3: Build NF(T₃,₅) = (σ₀σ₁)⁵
# ════════════════════════════════════════════════════════════════

print()
print("─" * 60)
print("STEP 3: NF(T₃,₅) = NF((σ₀σ₁)⁵)  (10 crossings, weak vertex)")
print("─" * 60)
print()

T35, steps_T35 = build_T35()
show_element("NF(T₃,₅)", T35)
print()
print(f"  Reduction steps: {steps_T35}")
print()
show_element_numeric("NF(T₃,₅)", T35, q0)
show_nf_shape("NF(T₃,₅)", T35)

tr_T35 = markov_trace_symbolic(T35, 3)
tr_T35_num = float(tr_T35.subs(q, q0))
print(f"  Markov trace (symbolic): {sp.simplify(tr_T35)}")
print(f"  Markov trace at q₀:     {tr_T35_num:.10f}")


# ════════════════════════════════════════════════════════════════
# STEP 4: Compose  proton · electron  (unreduced)
# ════════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("STEP 4: COMPOSE  NF(proton) · NF(electron)")
print("=" * 80)
print()

product_pe = proton * electron
print(f"  NF(proton): {proton.n_terms()} terms")
print(f"  NF(electron): {electron.n_terms()} terms")
print(f"  Unreduced product: {product_pe.n_terms()} terms")
print()

# Show the unreduced terms
print("  Unreduced terms (before GB reduction):")
for w, c in sorted(product_pe.terms.items(), key=lambda x: (len(x[0]), x[0])):
    v = float(c.subs(q, q0))
    if abs(v) > 1e-15:
        ws = word_str(w)
        print(f"    ({v:+.10f}) · {ws}")
print()

# Now reduce step by step
print("  Gröbner--Shirshov-reducing NF(proton) · NF(electron)...")
print()
reduced_pe, steps_pe, log_pe = reduce_stepwise(div, product_pe,
                                               "proton · electron")
print(f"  Total reduction steps: {steps_pe}")
print(f"  Step log ({len(log_pe)} rule applications):")
for i, step in enumerate(log_pe):
    print(f"    [{i+1}] {step['rule']}: {step['detail']}")
    if 'split_into' in step:
        print(f"         {step['word_before']} → {step['split_into'][0]} + {step['split_into'][1]}")
    elif 'word_after' in step:
        print(f"         {step['word_before']} → {step['word_after']}")
print()

show_element("NF(proton · electron)", reduced_pe)
print()
show_element_numeric("NF(proton · electron)", reduced_pe, q0)
show_nf_shape("NF(proton · electron)", reduced_pe)


# ════════════════════════════════════════════════════════════════
# STEP 5: Compose  (proton · electron) · T₃,₅   and reduce
# ════════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("STEP 5: COMPOSE  NF(proton · electron) · NF(T₃,₅)")
print("  The weak vertex T₃,₅ acts on the RHS of the proton-electron word.")
print("=" * 80)
print()

product_peT = reduced_pe * T35
print(f"  NF(proton · electron): {reduced_pe.n_terms()} terms")
print(f"  NF(T₃,₅): {T35.n_terms()} terms")
print(f"  Unreduced product: {product_peT.n_terms()} terms")
print()

# Show unreduced terms (may be many)
n_unreduced = product_peT.n_terms()
print(f"  Unreduced terms ({n_unreduced} total, showing first 20):")
count = 0
for w, c in sorted(product_peT.terms.items(), key=lambda x: (len(x[0]), x[0])):
    v = float(c.subs(q, q0))
    if abs(v) > 1e-15:
        ws = word_str(w)
        print(f"    ({v:+.10f}) · {ws}")
        count += 1
        if count >= 20:
            remaining = sum(1 for _, c2 in product_peT.terms.items()
                           if abs(float(c2.subs(q, q0))) > 1e-15) - 20
            if remaining > 0:
                print(f"    ... and {remaining} more terms")
            break
print()

# Step-by-step reduction
print("  Gröbner--Shirshov-reducing NF(proton · electron) · NF(T₃,₅)...")
print()
reduced_peT, steps_peT, log_peT = reduce_stepwise(div, product_peT,
                                                   "p·e⁻·T₃,₅")
print(f"  Total reduction steps: {steps_peT}")
print(f"  Step log ({len(log_peT)} rule applications):")

# Show condensed log: group by rule type
from collections import Counter
rule_counts = Counter(step['rule'] for step in log_peT)
for rule, cnt in sorted(rule_counts.items()):
    print(f"    {rule}: {cnt} applications")
print()

# Show first N detailed steps
MAX_DETAIL = 30
print(f"  First {min(MAX_DETAIL, len(log_peT))} detailed steps:")
for i, step in enumerate(log_peT[:MAX_DETAIL]):
    print(f"    [{i+1}] {step['rule']}: {step['detail']}")
    if 'split_into' in step:
        print(f"         {step['word_before']} → "
              f"{step['split_into'][0]} + {step['split_into'][1]}")
    elif 'word_after' in step:
        print(f"         {step['word_before']} → {step['word_after']}")
if len(log_peT) > MAX_DETAIL:
    print(f"    ... ({len(log_peT) - MAX_DETAIL} more steps)")
print()

show_element("NF(proton · electron · T₃,₅)", reduced_peT)
print()
show_element_numeric("NF(proton · electron · T₃,₅)", reduced_peT, q0)
show_nf_shape("NF(proton · electron · T₃,₅)", reduced_peT)


# ════════════════════════════════════════════════════════════════
# STEP 6: Markov traces and energy analysis
# ════════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("STEP 6: MARKOV TRACES AND ENERGY ANALYSIS")
print("=" * 80)
print()

tr_peT = markov_trace_symbolic(reduced_peT, 3)
tr_peT_num = float(tr_peT.subs(q, q0))
print(f"  tr(proton · electron · T₃,₅) symbolic: {sp.simplify(tr_peT)}")
print(f"  tr(proton · electron · T₃,₅) at q₀:    {tr_peT_num:.10f}")
print(f"  ln|tr|:                                  {math.log(abs(tr_peT_num)):.10f}")
print()

tr_pe = markov_trace_symbolic(reduced_pe, 3)
tr_pe_num = float(tr_pe.subs(q, q0))
print(f"  tr(proton · electron) at q₀:  {tr_pe_num:.10f}")
print(f"  ln|tr(p·e⁻)|:                 {math.log(abs(tr_pe_num)):.10f}")
print()


# ════════════════════════════════════════════════════════════════
# STEP 7: PARTICLE DECOMPOSITION OF THE RESULT
# ════════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("STEP 7: PARTICLE DECOMPOSITION")
print("  Identifying each NF term of NF(proton · electron · T₃,₅)")
print("=" * 80)
print()

all_words = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]

print("  RESULT — NF(proton · electron · T₃,₅):")
print("  ┌──────────┬──────────────────┬────────────┬──────────────┐")
print("  │ Particle │ Coefficient(q₀)  │ Crossings  │ Knot         │")
print("  ├──────────┼──────────────────┼────────────┼──────────────┤")

for w in all_words:
    pn, knot, ncx, desc = particle_knot(w)
    c = reduced_peT.terms.get(w, sp.Integer(0))
    c_simplified = sp.simplify(c)
    v = float(c_simplified.subs(q, q0)) if c_simplified != 0 else 0.0

    if abs(v) > 1e-15:
        sign = "+" if v > 0 else "−"
        print(f"  │ {pn:<8} │ {sign}{abs(v):<16.10f} │ {ncx:>10} │ {knot:<12} │")
    else:
        print(f"  │ {pn:<8} │ {'(empty)':<17} │ {ncx:>10} │ {knot:<12} │")
print("  └──────────┴──────────────────┴────────────┴──────────────┘")
print()

# Neutrino coefficient
c_nu = reduced_peT.terms.get((), sp.Integer(0))
c_nu_simplified = sp.simplify(c_nu)
c_nu_factored = factor_coefficient(c_nu_simplified)
v_nu = float(c_nu_simplified.subs(q, q0)) if c_nu_simplified != 0 else 0.0

print("  ╔══════════════════════════════════════════════════════════════╗")
print("  ║  FREE NEUTRINO SECTOR  (identity term 𝟏 in the Gröbner--Shirshov NF)║")
print("  ╠══════════════════════════════════════════════════════════════╣")
print(f"  ║  Symbolic coefficient:  {c_nu_factored:<35} ║")
print(f"  ║  At q₀ = {q0}:       {v_nu:+.10f}                   ║")
print(f"  ║  Knot type:             K₀ (unknot), 0 crossings          ║")
print(f"  ║  Jones polynomial:      J(K₀) = 1                         ║")
print(f"  ║  Hyperbolic volume:     Vol(K₀) = 0                       ║")
print("  ╚══════════════════════════════════════════════════════════════╝")
print()

# Also try the inverse: proton · electron · T₃,₅⁻¹
# T₃,₅⁻¹ in H₃(q) is the word (σ₁⁻¹σ₀⁻¹)⁵ — but inverses are
# non-trivial in the Iwahori--Hecke algebra.  Instead we use the Hecke relation:
# σᵢ⁻¹ = σᵢ − (q − q⁻¹) · 𝟏  (from σᵢ² = (q−q⁻¹)σᵢ + 1)
# → σᵢ⁻¹ = σᵢ + (q⁻¹ − q) · 𝟏

print()
print("─" * 60)
print("STEP 7b: COMPARISON — also compose proton · electron · T₃,₅⁻¹")
print("  where σᵢ⁻¹ = σᵢ − (q − q⁻¹) in H₃(q)")
print("─" * 60)
print()

# Build T₃,₅⁻¹ using the Hecke inverse: σᵢ⁻¹ = σᵢ − HA
# (σ₁⁻¹σ₀⁻¹)⁵
s0 = SymbolicHeckeElement({(0,): sp.Integer(1)})
s1 = SymbolicHeckeElement({(1,): sp.Integer(1)})
id_elem = SymbolicHeckeElement.identity()

s0_inv = s0 + id_elem.scale(-HA)  # σ₀⁻¹ = σ₀ − (q − q⁻¹)
s1_inv = s1 + id_elem.scale(-HA)  # σ₁⁻¹ = σ₁ − (q − q⁻¹)

T35_inv = SymbolicHeckeElement.identity()
for _ in range(5):
    T35_inv = T35_inv * s1_inv * s0_inv  # (σ₁⁻¹ · σ₀⁻¹)⁵

T35_inv, steps_T35_inv = div.reduce(T35_inv)
print(f"  NF(T₃,₅⁻¹): {T35_inv.n_terms()} terms")
print(f"  Reduction steps: {steps_T35_inv}")
show_element("NF(T₃,₅⁻¹)", T35_inv)
print()
show_element_numeric("NF(T₃,₅⁻¹)", T35_inv, q0)
show_nf_shape("NF(T₃,₅⁻¹)", T35_inv)

# Compose proton · electron · T₃,₅⁻¹
product_peT_inv = reduced_pe * T35_inv
reduced_peT_inv, steps_peT_inv = div.reduce(product_peT_inv)

print(f"  NF(proton · electron · T₃,₅⁻¹): {reduced_peT_inv.n_terms()} terms")
print(f"  Reduction steps: {steps_peT_inv}")
print()
show_element("NF(proton · electron · T₃,₅⁻¹)", reduced_peT_inv)
print()
show_element_numeric("NF(proton · electron · T₃,₅⁻¹)", reduced_peT_inv, q0)
show_nf_shape("NF(proton · electron · T₃,₅⁻¹)", reduced_peT_inv)

# Neutrino coefficient in inverse composition
c_nu_inv = reduced_peT_inv.terms.get((), sp.Integer(0))
c_nu_inv_simplified = sp.simplify(c_nu_inv)
v_nu_inv = float(c_nu_inv_simplified.subs(q, q0)) if c_nu_inv_simplified != 0 else 0.0
print(f"  ν coefficient (T₃,₅⁻¹ version): {v_nu_inv:+.10f}")
print(f"  Symbolic: {factor_coefficient(c_nu_inv_simplified)}")


# ════════════════════════════════════════════════════════════════
# STEP 8: VERIFICATION — T₃,₅ identity
# ════════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("STEP 8: VERIFICATION — NF(T₃,₅) · NF(T₃,₅⁻¹) should ≈ 𝟏")
print("=" * 80)
print()

product_TT = T35 * T35_inv
reduced_TT, steps_TT = div.reduce(product_TT)
print(f"  NF(T₃,₅ · T₃,₅⁻¹): {reduced_TT.n_terms()} terms")
show_element_numeric("NF(T₃,₅ · T₃,₅⁻¹)", reduced_TT, q0)

# Check if it's close to identity
id_coeff = reduced_TT.terms.get((), sp.Integer(0))
id_coeff_num = float(sp.simplify(id_coeff).subs(q, q0)) if id_coeff != 0 else 0.0
other_coeffs = {w: float(sp.simplify(c).subs(q, q0))
                for w, c in reduced_TT.terms.items()
                if w != () and abs(float(sp.simplify(c).subs(q, q0))) > 1e-15}
print(f"  Identity coefficient: {id_coeff_num:.10f}")
if other_coeffs:
    print(f"  Non-identity terms: {len(other_coeffs)}")
    for w, v in sorted(other_coeffs.items(), key=lambda x: (len(x[0]), x[0])):
        print(f"    ({v:+.10f}) · {word_str(w)}")
else:
    print(f"  ✓ T₃,₅ · T₃,₅⁻¹ = {id_coeff_num:.6f} · 𝟏  (pure identity)")


# ════════════════════════════════════════════════════════════════
# STEP 9: SUMMARY
# ════════════════════════════════════════════════════════════════

print()
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print()
print("  The free neutrino witness is the Gröbner--Shirshov normal form of")
print("  NF(proton · electron · T₃,₅) in H₃(q).")
print()
print("  This is NOT trivial: the composition produces an unreduced")
print(f"  product with {product_peT.n_terms()} terms, which Gröbner--Shirshov-reduces to")
print(f"  {reduced_peT.n_terms()} NF terms via {sum(steps_peT.values())} rule applications.")
print()
print("  The neutrino is identified as the coefficient on the")
print("  identity word 𝟏 (= unknot K₀, 0 crossings) in the NF.")
print()
print(f"  ν coefficient (symbolic): {c_nu_factored}")
print(f"  ν coefficient (at q₀):    {v_nu:+.10f}")
print()

# Occupied sectors summary
print("  Sector decomposition:")
for w in all_words:
    pn, knot, ncx, desc = particle_knot(w)
    c = reduced_peT.terms.get(w, sp.Integer(0))
    v = float(sp.simplify(c).subs(q, q0)) if c != 0 else 0.0
    if abs(v) > 1e-15:
        c_p = reduced_pe.terms.get(w, sp.Integer(0))
        v_p = float(sp.simplify(c_p).subs(q, q0)) if c_p != 0 else 0.0
        source = "from p·e⁻" if abs(v_p) > 1e-15 else "NEW from T₃,₅"
        print(f"    {pn:<4} = {v:+.10f}  ({source})")


# ════════════════════════════════════════════════════════════════
# STEP 10: WRITE WITNESS JSON
# ════════════════════════════════════════════════════════════════

print()
print("─" * 60)
print("Writing witness file...")
print("─" * 60)

witness = {
    "name": "free-neutrino-groebner-nf",
    "description": (
        "Gröbner--Shirshov normal form witness for the free neutrino. "
        "Computes NF(proton · electron · T₃,₅) in H₃(q) and identifies "
        "the neutrino as the coefficient on the identity word 𝟏 (unknot K₀). "
        "All coefficients exact in ℤ[q^½, q^{-½}]."
    ),
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "particle_knot_dictionary": {
        "1":     {"symbol": "ν",  "knot": "K₀ (unknot)", "crossings": 0,
                  "description": "neutrino sector"},
        "s0":    {"symbol": "σ₀", "knot": "T₂,₁⁽⁰⁾ (Hopf gen)", "crossings": 1,
                  "description": "Hopf crossing gen 0"},
        "s1":    {"symbol": "σ₁", "knot": "T₂,₁⁽¹⁾ (Hopf gen)", "crossings": 1,
                  "description": "Hopf crossing gen 1"},
        "s0.s1": {"symbol": "L₊", "knot": "L₂,₁ (Hopf link)", "crossings": 2,
                  "description": "Hopf pair (positive)"},
        "s1.s0": {"symbol": "L₋", "knot": "L₂,₁' (Hopf rev)", "crossings": 2,
                  "description": "Hopf pair (reversed)"},
        "s0.s1.s0": {"symbol": "e⁻", "knot": "T₂,₃ (trefoil 3₁)", "crossings": 3,
                     "description": "electron (Garside Δ₃)"},
    },
    "parameters": {
        "q": "symbolic",
        "q0": q0,
        "HA": str(HA),
        "E_cross": E_cross_num,
        "mu_0": mu_0,
    },
    "proton": {
        "composition": "[u, u, d] (quark level)",
        "strands": 3,
        "n_terms": proton.n_terms(),
        "reduction_steps": steps_p,
        "nf": terms_to_dict(proton, q0),
        "markov_trace": {
            "symbolic": str(sp.simplify(tr_p)),
            "polynomial": expose_polynomial(tr_p, q),
            "at_q0": tr_p_num,
            "ln_abs": math.log(abs(tr_p_num)),
        },
    },
    "electron": {
        "braid_word": "σ₀σ₁σ₀ = Δ₃ (Garside element)",
        "crossings": 3,
        "genus": 1,
        "n_terms": electron.n_terms(),
        "reduction_steps": steps_e,
        "nf": terms_to_dict(electron, q0),
        "markov_trace": {
            "symbolic": str(sp.simplify(tr_e)),
            "polynomial": expose_polynomial(tr_e, q),
            "at_q0": tr_e_num,
        },
    },
    "T35_weak_vertex": {
        "braid_word": "(σ₀σ₁)⁵",
        "crossings": 10,
        "genus": 4,
        "n_terms": T35.n_terms(),
        "reduction_steps": steps_T35,
        "nf": terms_to_dict(T35, q0),
        "markov_trace": {
            "symbolic": str(sp.simplify(tr_T35)),
            "polynomial": expose_polynomial(tr_T35, q),
            "at_q0": tr_T35_num,
        },
    },
    "T35_inverse": {
        "braid_word": "(σ₁⁻¹σ₀⁻¹)⁵",
        "crossings": 10,
        "n_terms": T35_inv.n_terms(),
        "reduction_steps": steps_T35_inv,
        "nf": terms_to_dict(T35_inv, q0),
    },
    "composition_proton_times_electron": {
        "order": "NF(proton) · NF(electron)",
        "unreduced_terms": product_pe.n_terms(),
        "reduced_terms": reduced_pe.n_terms(),
        "reduction_steps": steps_pe,
        "step_log_summary": dict(Counter(s['rule'] for s in log_pe)),
        "nf": terms_to_dict(reduced_pe, q0),
        "markov_trace": {
            "at_q0": tr_pe_num,
            "ln_abs": math.log(abs(tr_pe_num)),
        },
    },
    "composition_pe_times_T35": {
        "order": "NF(proton · electron) · NF(T₃,₅)",
        "unreduced_terms": product_peT.n_terms(),
        "reduced_terms": reduced_peT.n_terms(),
        "reduction_steps": steps_peT,
        "step_log_summary": dict(Counter(s['rule'] for s in log_peT)),
        "total_rule_applications": len(log_peT),
        "nf": terms_to_dict(reduced_peT, q0),
        "markov_trace": {
            "symbolic": str(sp.simplify(tr_peT)),
            "polynomial": expose_polynomial(tr_peT, q),
            "at_q0": tr_peT_num,
            "ln_abs": math.log(abs(tr_peT_num)),
        },
    },
    "composition_pe_times_T35_inv": {
        "order": "NF(proton · electron) · NF(T₃,₅⁻¹)",
        "unreduced_terms": product_peT_inv.n_terms(),
        "reduced_terms": reduced_peT_inv.n_terms(),
        "reduction_steps": steps_peT_inv,
        "nf": terms_to_dict(reduced_peT_inv, q0),
    },
    "neutrino_witness": {
        "description": (
            "The free neutrino is the coefficient on the identity word 𝟏 "
            "(unknot K₀, 0 crossings) in NF(proton · electron · T₃,₅). "
            "This is the result of a non-trivial Gröbner--Shirshov reduction, NOT "
            "a trivial assertion."
        ),
        "composition": "NF(proton · electron · T₃,₅)",
        "neutrino_coefficient_symbolic": str(c_nu_factored),
        "neutrino_coefficient_at_q0": v_nu,
        "neutrino_coefficient_inverse_symbolic": str(factor_coefficient(c_nu_inv_simplified)),
        "neutrino_coefficient_inverse_at_q0": v_nu_inv,
        "knot": "K₀ (unknot)",
        "crossings": 0,
        "jones_polynomial": "J(K₀) = 1",
        "hyperbolic_volume": 0.0,
        "genus": 0,
        "total_reduction_steps": sum(steps_peT.values()),
        "total_rule_applications": len(log_peT),
    },
    "verification": {
        "T35_times_T35_inv": {
            "n_terms": reduced_TT.n_terms(),
            "identity_coefficient": id_coeff_num,
            "non_identity_terms": len(other_coeffs),
            "is_identity": len(other_coeffs) == 0 and abs(id_coeff_num - 1.0) < 1e-6,
        },
    },
    "assertions": [
        {
            "name": "NF(proton · electron · T₃,₅) has neutrino sector",
            "result": abs(v_nu) > 1e-15,
            "value": v_nu,
        },
        {
            "name": "Gröbner--Shirshov reduction is non-trivial",
            "result": len(log_peT) > 0,
            "total_steps": len(log_peT),
        },
        {
            "name": "NF has correct number of terms (≤ 6 for H₃(q))",
            "result": reduced_peT.n_terms() <= 6,
            "n_terms": reduced_peT.n_terms(),
        },
    ],
}

witness_path = "free-neutrino-groebner-nf.witness.json"
with open(witness_path, 'w') as f:
    json.dump(witness, f, indent=2, default=str)

print(f"  Written to: {witness_path}")
print()
print("Done.")
