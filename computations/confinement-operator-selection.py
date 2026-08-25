#!/usr/bin/env python3
"""
Confinement operator selection via Frobenius dual / minimum-action.

Derives which binding operator confines 3 quarks into a nucleon.
Does NOT assert B₃ — instead explores candidates and shows which
one the Gram matrix inverse / minimum-action principle selects.

Phase 0a: NF of 3 unconfined quarks (should be unstable)
Phase 0b: Candidate operators compared (B₃, Hopf chains, trefoil, G⁻¹ action)
Phase 0c: Full G⁻¹ action on demand profile
Phase 1:  Verify selected operator reproduces known proton/neutron NFs

Usage:
    cd computations && python3 confinement-operator-selection.py
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import numpy as np
import subprocess
from datetime import datetime, timezone
from pathlib import Path

# ── q parameter (canonical source) ───────────────────────────
from q_parameter import Q as q0, HA as HA_val, E_CROSS
# z/NF_BASIS/TR_M now owned by pyhecke.gram (M2b inversion). Keep local
# bootstrap for dev mode; the installed-pyhecke path is preferred.
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[1] / "tools" / "pyhecke" / "python"))
from pyhecke.gram import z as _PG_Z, NF_BASIS as _PG_NF_BASIS, TR_M as _PG_TR_M  # noqa: E402
from derived_masses import (  # noqa: E402
    target_net_proton as TARGET_NET_PROTON_FN,
    target_net_neutron as TARGET_NET_NEUTRON_FN,
)


try:
    SHA = subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'],
        cwd=str(Path(__file__).resolve().parent.parent.parent),
        stderr=subprocess.DEVNULL
    ).decode().strip()
except (subprocess.CalledProcessError, FileNotFoundError):
    SHA = "unknown"

# ── Hecke algebra engine (numerical, same as gram-matrix-dual.py) ──
HA = HA_val  # q - q⁻¹
z = _PG_Z  # moved to pyhecke.gram
NF_BASIS = _PG_NF_BASIS  # moved to pyhecke.gram
NF_NAMES = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
TR_M_BASIS = list(_PG_TR_M)  # moved to pyhecke.gram
def hecke_mul(t1, t2):
    """Multiply two H₃(q) elements."""
    result = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            result[w] = result.get(w, 0.0) + c1 * c2
    return {w: c for w, c in result.items() if abs(c) > 1e-15}


def reduce_nf(terms):
    """Gröbner-Shirshov normal form in H₃(q)."""
    changed = True
    while changed:
        changed = False
        new_terms = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False
            # R1: Hecke σᵢ² → HAσᵢ + 1
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1]:
                    i = word[pos]
                    pre, suf = word[:pos], word[pos + 2:]
                    new_terms[pre + (i,) + suf] = new_terms.get(pre + (i,) + suf, 0.0) + coeff * HA
                    new_terms[pre + suf] = new_terms.get(pre + suf, 0.0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            # R3: Yang-Baxter σᵢσⱼσᵢ → σⱼσᵢσⱼ
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and abs(a - b) == 1:
                    new_trip = (b, a, b)
                    if new_trip < (a, b, a):
                        nw = word[:pos] + new_trip + word[pos + 3:]
                        new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                        done = changed = True
                        break
            if not done:
                new_terms[word] = new_terms.get(word, 0.0) + coeff
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms


def to_vec(terms):
    return [terms.get(b, 0.0) for b in NF_BASIS]


def from_vec(v):
    return {NF_BASIS[i]: v[i] for i in range(6) if abs(v[i]) > 1e-15}


def markov_trace(vec):
    return sum(c * t for c, t in zip(vec, TR_M_BASIS))


def nf_net(vec):
    return sum(vec)


def expand_inverse(word):
    """Build element from word with negative indices = inverses.
    -1 means σ₀⁻¹, -2 means σ₁⁻¹."""
    terms = {(): 1.0}
    for g in word:
        new_terms = {}
        if g >= 0:
            for w, c in terms.items():
                nw = w + (g,)
                new_terms[nw] = new_terms.get(nw, 0.0) + c
        else:
            i = -g - 1  # σ₀⁻¹ = σ₀ - HA
            for w, c in terms.items():
                nw = w + (i,)
                new_terms[nw] = new_terms.get(nw, 0.0) + c
                new_terms[w] = new_terms.get(w, 0.0) - c * HA
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms


def crossing(type_i, type_j, gen):
    """Typed crossing element for quark pair."""
    if type_i == type_j == 'u':
        return {(gen,): 1.0}
    elif type_i == type_j == 'd':
        return {(gen,): 1.0, (): -HA}
    else:  # u-d or d-u mixed
        return {(gen,): 1.0, (): -HA / 2}


def print_nf(label, vec):
    """Pretty-print NF vector."""
    net = nf_net(vec)
    parts = []
    for i, (name, val) in enumerate(zip(NF_NAMES, vec)):
        if abs(val) > 1e-15:
            parts.append(f"{val:+.6f}·{name}")
    print(f"  {label}: {' '.join(parts)}  [net={net:+.6f}]")


def demand_profile(vec):
    """Return indices and values of negative NF coefficients."""
    return [(i, NF_NAMES[i], vec[i]) for i in range(6) if vec[i] < -1e-10]


def supply_profile(vec):
    """Return indices and values of positive NF coefficients."""
    return [(i, NF_NAMES[i], vec[i]) for i in range(6) if vec[i] > 1e-10]


def crossing_energy(vec):
    """Total crossing energy = sum of |cᵢ| × degree(bᵢ) × E_×."""
    degrees = [0, 1, 1, 2, 2, 3]  # word lengths
    return sum(abs(vec[i]) * degrees[i] * E_CROSS for i in range(6))


# ══════════════════════════════════════════════════════════════
#  GRAM MATRIX
# ══════════════════════════════════════════════════════════════

def build_gram():
    """Build 6×6 Gram matrix G_{ij} = tr_M(b_i · b_j)."""
    G = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            prod = hecke_mul({NF_BASIS[i]: 1.0}, {NF_BASIS[j]: 1.0})
            nf = reduce_nf(prod)
            vec = to_vec(nf)
            G[i, j] = markov_trace(vec)
    return G


print("=" * 80)
print("CONFINEMENT OPERATOR SELECTION VIA FROBENIUS DUAL")
print(f"q₀ = {q0:.10f}  |  HA = {HA:.10f}  |  z = {z:.10f}")
print(f"Commit: {SHA[:8]}")
print("=" * 80)

G = build_gram()
# Guarded: np.linalg.inv does NOT raise on the convention-D Markov Gram, it
# returns inverted rounding noise -- entries ~7.6e15, and the residual is
# ||G@inv - I||_F = 4.14 (Frobenius) = 1.64 (max-entry).  BOTH figures are in
# the corpus for this one quantity and neither used to name its norm, so they
# read as a contradiction; they are the same matrix under two norms.
# safe_inverse raises instead and names the quotient inverse. See qou-m7py.
# `safe_inverse` RAISES here by design (qou-m7py): under convention D this
# form is singular, so the object it is asked for does not exist.  This
# producer called it anyway and so died at line 201 on every run -- the
# second of two independent import/run failures, the first being the two
# phantom `TARGET_NET_*` constants that live inside a docstring.
#
# The honest replacement is the pseudoinverse of THIS producer's own G.  Note
# it is NOT `pyhecke.gram.G_PINV`: that is the pinv of pyhecke's G at
# pyhecke's q, and silently substituting one for the other is the layer
# straddle AGENTS.md warns about.  They are cross-checked below rather than
# assumed equal.
G_inv = np.linalg.pinv(G)

try:
    from pyhecke.gram import G as _PYHECKE_G  # noqa: E402

    _g_drift = float(np.max(np.abs(G - np.asarray(_PYHECKE_G, dtype=float))))
    print(f"\nCross-check vs pyhecke.gram.G: max entry drift = {_g_drift:.2e}")
except ImportError:
    print("\nCross-check vs pyhecke.gram.G: skipped (pyhecke unavailable)")

# G_inv is the Moore-Penrose PSEUDOinverse -- the 6x6 form is singular under
# convention D, so no inverse exists.  `G @ G_inv` is therefore the projector
# onto the rank-5 range, NOT the identity, and the residual against I is a
# structural constant rather than an error estimate:
#
#     max|G G+ - I| = 0.2234...,  ||G G+ - I||_F = sqrt(corank) = 1
#
# This block used to print exactly that max-norm under the label
# "Verification: max|G.G^-1 - I|", which is a number that can never be small
# presented as though it were a check that passed.  The real check is
# idempotency of the projector, which DOES hold to machine precision.
P = G @ G_inv
proj_residual = float(np.max(np.abs(P @ P - P)))
range_defect = float(np.max(np.abs(P - np.eye(6))))
print(f"\nGram matrix: det(G) = {np.linalg.det(G):.10f}")
print(f"Verification: max|P² - P| = {proj_residual:.2e}   (P = G·G⁺ is a projector)")
print(f"  rank-5 defect: max|P - I| = {range_defect:.2e}   (expected O(1): the form is singular)")


def frobenius_dual(vec):
    return np.array(vec) @ G_inv


# ══════════════════════════════════════════════════════════════
#  PHASE 0a: UNCONFINED 3-QUARK NF
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("PHASE 0a: UNCONFINED THREE-QUARK STATES")
print("=" * 80)
print("\nCompute NF of three typed crossings WITHOUT any binding operator.")
print("These represent free quarks — should show instability (large demand).\n")

for nucleon_name, quark_types in [("proton (u,u,d)", ['u', 'u', 'd']),
                                   ("neutron (u,d,d)", ['u', 'd', 'd'])]:
    print(f"\n{'─' * 70}")
    print(f"  {nucleon_name} — unconfined quarks")
    print(f"{'─' * 70}")

    # Build product of typed crossings only (no B₃)
    A = len(quark_types)
    elem = {(): 1.0}  # start with identity
    for i in range(A):
        for j in range(i + 1, A):
            gen = min(i, j)  # generator index
            if gen > 1:
                gen = 1  # only σ₀, σ₁ in H₃
            cx = crossing(quark_types[i], quark_types[j], gen)
            pair_label = f"({i},{j}) {quark_types[i]}-{quark_types[j]}"
            elem = hecke_mul(elem, cx)
            elem = reduce_nf(elem)
            vec = to_vec(elem)
            print(f"  After crossing {pair_label}:")
            print_nf("    NF", vec)

    final_vec = to_vec(elem)
    print(f"\n  UNCONFINED {nucleon_name} NF:")
    print_nf("    NF", final_vec)

    dem = demand_profile(final_vec)
    sup = supply_profile(final_vec)
    E_x = crossing_energy(final_vec)

    print(f"  Demand profile: {', '.join(f'{n}={v:+.4f}' for _, n, v in dem) if dem else 'NONE'}")
    print(f"  Supply profile: {', '.join(f'{n}={v:+.4f}' for _, n, v in sup)}")
    print(f"  Crossing energy: {E_x:.6f}")
    print(f"  Markov trace: {markov_trace(final_vec):.6f}")

    # Frobenius dual of unconfined state
    dual = frobenius_dual(final_vec)
    print(f"\n  Frobenius dual of unconfined state:")
    print_nf("    K∨", list(dual))


# ══════════════════════════════════════════════════════════════
#  PHASE 0b: CANDIDATE CONFINEMENT OPERATORS
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("PHASE 0b: CANDIDATE CONFINEMENT OPERATORS")
print("=" * 80)
print("\nFor each candidate operator Φ, compute:")
print("  1. NF(Φ) — the operator's own normal form")
print("  2. NF(Φ · crossings) — the operator applied to typed crossings")
print("  3. Crossing energy of the result")
print("  4. Demand satisfaction: how many demand channels are filled")
print("  5. Frobenius pairing ⟨Φ∨, demand⟩_F\n")

# Build candidate operators
candidates = {}

# 1. B₃ = (σ₀σ₁⁻¹)³
b3_raw = expand_inverse((0, -2, 0, -2, 0, -2))
b3_nf = reduce_nf(b3_raw)
candidates["B₃ = (σ₀σ₁⁻¹)³"] = b3_nf

# 2. Single Hopf: L₊ = σ₀σ₁
candidates["L₊ = σ₀σ₁"] = {(0, 1): 1.0}

# 3. Double Hopf: (σ₀σ₁)²
dh_raw = hecke_mul({(0, 1): 1.0}, {(0, 1): 1.0})
dh_nf = reduce_nf(dh_raw)
candidates["(σ₀σ₁)² (double Hopf)"] = dh_nf

# 4. Trefoil: e⁻ = σ₀σ₁σ₀
candidates["e⁻ = σ₀σ₁σ₀ (trefoil)"] = {(0, 1, 0): 1.0}

# 5. Identity (no confinement)
candidates["𝟏 (identity, no binding)"] = {(): 1.0}

# 6. σ₀σ₁⁻¹ (single unit of B₃)
unit_raw = expand_inverse((0, -2))
unit_nf = reduce_nf(unit_raw)
candidates["σ₀σ₁⁻¹ (single unit)"] = unit_nf

# 7. (σ₀σ₁⁻¹)² — partial Borromean
unit2_raw = hecke_mul(unit_nf, unit_raw)
unit2_nf = reduce_nf(unit2_raw)
candidates["(σ₀σ₁⁻¹)² (partial B)"] = unit2_nf

# 8. L₋ = σ₁σ₀
candidates["L₋ = σ₁σ₀"] = {(1, 0): 1.0}

# 9. σ₁⁻¹σ₀⁻¹ (inverse Hopf)
inv_hopf_raw = expand_inverse((-2, -1))
inv_hopf_nf = reduce_nf(inv_hopf_raw)
candidates["σ₁⁻¹σ₀⁻¹ (inv Hopf)"] = inv_hopf_nf

# Print NF of each candidate operator
print("─" * 70)
print("  NF of each candidate operator:")
print("─" * 70)
for name, op_terms in candidates.items():
    vec = to_vec(op_terms)
    print_nf(f"  {name}", vec)

# Now apply each candidate to proton quarks (u,u,d) and neutron quarks (u,d,d)
for nucleon_name, quark_types in [("PROTON (u,u,d)", ['u', 'u', 'd']),
                                   ("NEUTRON (u,d,d)", ['u', 'd', 'd'])]:
    print(f"\n{'═' * 70}")
    print(f"  {nucleon_name} — all candidate operators")
    print(f"{'═' * 70}")

    results_table = []

    for cand_name, op_terms in candidates.items():
        # Apply: operator × typed crossings
        elem = dict(op_terms)
        A = len(quark_types)
        for i in range(A):
            for j in range(i + 1, A):
                gen = min(i, j)
                if gen > 1:
                    gen = 1
                cx = crossing(quark_types[i], quark_types[j], gen)
                elem = hecke_mul(elem, cx)
                elem = reduce_nf(elem)

        vec = to_vec(elem)
        net = nf_net(vec)
        E_x = crossing_energy(vec)
        dem = demand_profile(vec)
        n_demand = len(dem)
        demand_magnitude = sum(abs(v) for _, _, v in dem)
        tr = markov_trace(vec)

        results_table.append({
            'name': cand_name,
            'nf': vec,
            'net': net,
            'E_x': E_x,
            'n_demand': n_demand,
            'demand_mag': demand_magnitude,
            'trace': tr,
        })

    # Print comparison table
    print(f"\n  {'Operator':<30s} | {'net':>8s} | {'E_×':>8s} | {'#dem':>4s} | {'|dem|':>8s} | {'tr_M':>8s}")
    print(f"  {'─'*30}-+-{'─'*8}-+-{'─'*8}-+-{'─'*4}-+-{'─'*8}-+-{'─'*8}")
    for r in results_table:
        print(f"  {r['name']:<30s} | {r['net']:>+8.4f} | {r['E_x']:>8.4f} | {r['n_demand']:>4d} | {r['demand_mag']:>8.4f} | {r['trace']:>8.4f}")

    # Print full NF for each
    print(f"\n  Full NF vectors:")
    for r in results_table:
        print_nf(f"    {r['name'][:25]}", r['nf'])

    # ── Ranking by multiple criteria ──────────────────────────────
    is_proton = 'u' == quark_types[0] and quark_types.count('u') == 2
    target_net = TARGET_NET_PROTON_FN() if is_proton else TARGET_NET_NEUTRON_FN()

    print(f"\n  RANKING 1 — Naive (fewer demand channels, lower E_×):")
    ranked1 = sorted(results_table, key=lambda r: (r['n_demand'], r['E_x']))
    for rank, r in enumerate(ranked1, 1):
        marker = " ◀ NAIVE" if rank == 1 else ""
        print(f"    #{rank}: {r['name']:<30s}  E_×={r['E_x']:.4f}  "
              f"demand={r['n_demand']}  |dem|={r['demand_mag']:.4f}{marker}")

    print(f"\n  RANKING 2 — Net constraint (|net - target|, target ≈ {target_net:.3f}):")
    ranked2 = sorted(results_table, key=lambda r: abs(r['net'] - target_net))
    for rank, r in enumerate(ranked2, 1):
        delta = abs(r['net'] - target_net)
        marker = " ◀ NET-MATCH" if rank == 1 else ""
        print(f"    #{rank}: {r['name']:<30s}  net={r['net']:+.4f}  "
              f"|Δnet|={delta:.4f}  tr_M={r['trace']:.4f}{marker}")

    print(f"\n  RANKING 3 — Minimum action (lowest tr_M among net-matching):")
    # Only consider operators within 0.1 of target net
    net_ok = [r for r in results_table if abs(r['net'] - target_net) < 0.1]
    ranked3 = sorted(net_ok, key=lambda r: r['trace'])
    for rank, r in enumerate(ranked3, 1):
        marker = " ◀ MIN-ACTION" if rank == 1 else ""
        print(f"    #{rank}: {r['name']:<30s}  tr_M={r['trace']:.4f}  "
              f"net={r['net']:+.4f}  |Δnet|={abs(r['net'] - target_net):.4f}{marker}")
    if not net_ok:
        print(f"    (no candidates within 0.1 of target net)")

    # Physical interpretation of demand in B₃-confined state
    b3_result = next(r for r in results_table if 'B₃' in r['name'])
    b3_nf_vec = b3_result['nf']
    print(f"\n  PHYSICAL INTERPRETATION of B₃-confined demand:")
    for i, (name, val) in enumerate(zip(NF_NAMES, b3_nf_vec)):
        if val < -1e-10:
            if name == 'γ':
                print(f"    {name} = {val:+.4f}  → vacuum energy deficit (mass via Borromean volume)")
            elif name == 'e⁻':
                print(f"    {name} = {val:+.4f}  → trefoil demand = BETA DECAY CHANNEL")
            elif name == 'L₊':
                print(f"    {name} = {val:+.4f}  → Hopf link deficit (gluon field deficit)")
            else:
                print(f"    {name} = {val:+.4f}  → crossing deficit")


# ══════════════════════════════════════════════════════════════
#  PHASE 0c: FULL G⁻¹ ACTION ON DEMAND PROFILE
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("PHASE 0c: FULL G⁻¹ ACTION ON 3-QUARK DEMAND PROFILE")
print("=" * 80)
print("\nApply G⁻¹ directly to the demand vector of the unconfined quarks.")
print("This gives the 'ideal binding operator' in the Frobenius dual basis.\n")

for nucleon_name, quark_types in [("proton (u,u,d)", ['u', 'u', 'd']),
                                   ("neutron (u,d,d)", ['u', 'd', 'd'])]:
    print(f"\n{'─' * 70}")
    print(f"  {nucleon_name}")
    print(f"{'─' * 70}")

    # Recompute unconfined quarks
    elem = {(): 1.0}
    A = len(quark_types)
    for i in range(A):
        for j in range(i + 1, A):
            gen = min(i, j)
            if gen > 1:
                gen = 1
            cx = crossing(quark_types[i], quark_types[j], gen)
            elem = hecke_mul(elem, cx)
            elem = reduce_nf(elem)

    unconfined_vec = np.array(to_vec(elem))
    print_nf("  Unconfined NF", list(unconfined_vec))

    # Extract demand vector (negative components only)
    demand_vec = np.array([min(0, v) for v in unconfined_vec])
    print_nf("  Demand vector", list(demand_vec))

    # Apply G⁻¹ to demand
    ginv_demand = demand_vec @ G_inv
    print_nf("  G⁻¹ · demand", list(ginv_demand))

    # Apply G⁻¹ to full unconfined state
    ginv_full = unconfined_vec @ G_inv
    print_nf("  G⁻¹ · unconfined", list(ginv_full))

    # The G⁻¹ action on the demand tells us what operator fills it
    # Compare with B₃ NF
    b3_vec = np.array(to_vec(b3_nf))
    print_nf("  B₃ NF", list(b3_vec))

    # Frobenius pairing of B₃ with the unconfined state
    pairing = float(b3_vec @ G @ unconfined_vec)
    print(f"\n  ⟨B₃, unconfined⟩_F = {pairing:+.6f}")

    # Frobenius pairing of each candidate with unconfined demand
    print(f"\n  Frobenius pairings ⟨candidate, unconfined⟩_F:")
    for cand_name, op_terms in candidates.items():
        cand_vec = np.array(to_vec(op_terms))
        p = float(cand_vec @ G @ unconfined_vec)
        print(f"    {cand_name:<30s}: {p:+.10f}")

    # Now: apply B₃ then crossings (the correct derivation)
    print(f"\n  === Applying B₃ then typed crossings ===")
    elem_b3 = dict(b3_nf)
    for i in range(A):
        for j in range(i + 1, A):
            gen = min(i, j)
            if gen > 1:
                gen = 1
            cx = crossing(quark_types[i], quark_types[j], gen)
            elem_b3 = hecke_mul(elem_b3, cx)
            elem_b3 = reduce_nf(elem_b3)
    confined_vec = to_vec(elem_b3)
    print_nf("  Confined NF (B₃ · crossings)", confined_vec)
    dem = demand_profile(confined_vec)
    print(f"  Demand after confinement: {', '.join(f'{n}={v:+.4f}' for _, n, v in dem) if dem else 'NONE — fully confined'}")


# ══════════════════════════════════════════════════════════════
#  PHASE 1: KNOWN NF VERIFICATION
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("PHASE 1: VERIFY AGAINST KNOWN PROTON/NEUTRON NFs")
print("=" * 80)

known = {
    "proton": {
        'quarks': ['u', 'u', 'd'],
        'known_nf': [-0.0997, +0.0357, +0.9976, +0.0994, +0.0093, -0.0432],
        'known_net': +0.9991,
    },
    "neutron": {
        'quarks': ['u', 'd', 'd'],
        'known_nf': [-0.2017, +0.0481, +1.0090, -0.0096, +0.0092, -0.0442],
        'known_net': +0.8108,
    },
}

for name, data in known.items():
    print(f"\n{'─' * 70}")
    print(f"  {name}")
    print(f"{'─' * 70}")

    # Compute from B₃ + typed crossings
    elem = dict(b3_nf)
    for i in range(3):
        for j in range(i + 1, 3):
            gen = min(i, j)
            if gen > 1:
                gen = 1
            cx = crossing(data['quarks'][i], data['quarks'][j], gen)
            elem = hecke_mul(elem, cx)
            elem = reduce_nf(elem)

    computed = to_vec(elem)
    computed_net = nf_net(computed)

    print_nf("  Computed", computed)
    print_nf("  Known   ", data['known_nf'])
    print(f"  Net: computed={computed_net:+.6f}  known={data['known_net']:+.6f}")

    # Check match
    max_diff = max(abs(computed[i] - data['known_nf'][i]) for i in range(6))
    print(f"  Max |diff| = {max_diff:.6f}")
    if max_diff < 0.01:
        print(f"  ✓ MATCH (within tolerance)")
    else:
        print(f"  ✗ MISMATCH — investigate")


# ══════════════════════════════════════════════════════════════
#  WITNESS OUTPUT
# ══════════════════════════════════════════════════════════════

witness = {
    "name": "confinement-operator-selection",
    "description": "Derives confinement operator from Frobenius dual minimum-action principle",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "git_sha": SHA,
    "parameters": {
        "q0": q0,
        "HA": HA,
        "z": z,
        "E_cross": E_CROSS,
    },
    "gram_matrix": G.tolist(),
    # Key kept as `gram_inverse` for schema compatibility: three consumers
    # read it by that name (delta_lambda_master_formula_h3_probe,
    # bound_state_observable_validator, audit_frobenius_pairing).  The object
    # is the pseudoinverse, so `gram_inverse_kind` names it -- matching the
    # sibling emitter `borromean-axial-coupling.py`, which already does this
    # and which this producer was silently inconsistent with.
    "gram_inverse": G_inv.tolist(),
    "gram_inverse_kind": "moore-penrose-pseudoinverse",
    "gram_det": float(np.linalg.det(G)),
    "candidates": {},
}

# Recompute candidate results for witness
for nucleon_name, quark_types in [("proton", ['u', 'u', 'd']),
                                   ("neutron", ['u', 'd', 'd'])]:
    nuc_results = {}

    for cand_name, op_terms in candidates.items():
        elem = dict(op_terms)
        for i in range(3):
            for j in range(i + 1, 3):
                gen = min(i, j)
                if gen > 1:
                    gen = 1
                cx = crossing(quark_types[i], quark_types[j], gen)
                elem = hecke_mul(elem, cx)
                elem = reduce_nf(elem)
        vec = to_vec(elem)
        nuc_results[cand_name] = {
            "nf": vec,
            "net": nf_net(vec),
            "crossing_energy": crossing_energy(vec),
            "n_demand": len(demand_profile(vec)),
            "demand_magnitude": sum(abs(v) for _, _, v in demand_profile(vec)),
        }

    witness["candidates"][nucleon_name] = nuc_results

out_path = Path(__file__).parent / "confinement-operator-selection.witness.json"

# ── GUARD: this producer is BEHIND its own committed witness ────────────
#
# The committed witness carries 12 keys this script cannot produce. MEASURED,
# because the distinction matters and the first version of this comment got
# it wrong:
#
#   9 are STUBS, not data -- `active_set`, `primal_obj`, `dual_obj`,
#     `duality_gap`, `y0_star`, `y_star` are all `None`, and the three
#     `*_status` fields read "STUB -- re-run script through lp_dual_solver.py
#     to populate". They satisfy the LP-dual validator's field-PRESENCE check;
#     they carry no shadow prices.
#
#   3 are REAL -- `engine`, `scriptFile`, `commitSha`: WitnessBuilder
#     provenance, and the only content actually at risk here.
#
# So an overwrite does not destroy computed duals; there are none to destroy.
# What it does is drop `gram_inverse`'s companions below the REQUIRED_FIELDS
# of `bound_state_observable_validator` and `audit_frobenius_pairing`, and
# lose the provenance stamp. Both are still reasons not to clobber silently.
#
# AND NOTE WHAT THE STUB NOTE ASKS FOR IS NOT AVAILABLE. "Re-run through
# lp_dual_solver.py" presumes an LP in this file. There is none -- the three
# RANKING passes are sorts, not optimisations, and nothing here has a primal
# to take a dual of. So the duals either belong to a different producer or
# want an LP that was never written. That is an open question, not a wiring
# task; do not "fix" it by calling the solver on a problem that is not posed.
#
# Refuse to overwrite a witness that holds keys we cannot regenerate. Set
# QOU_ALLOW_WITNESS_DOWNGRADE=1 only if you have deliberately decided the
# drop is correct.
import os  # noqa: E402

_existing = {}
if out_path.exists():
    try:
        _existing = json.loads(out_path.read_text())
    except (OSError, ValueError):
        _existing = {}
_lost = sorted(set(_existing) - set(witness))

if _lost and os.environ.get("QOU_ALLOW_WITNESS_DOWNGRADE") != "1":
    print(f"\n\nWitness NOT written to {out_path.name} -- refusing a downgrade.")
    print(f"  the committed witness holds {len(_lost)} key(s) this producer "
          f"cannot emit:")
    print(f"    {', '.join(_lost)}")
    print("  (9 of those are None/STUB placeholders, 3 are real provenance --"
          " see the guard comment.)")
    print("  Set QOU_ALLOW_WITNESS_DOWNGRADE=1 to override.")
    print("Done (witness preserved).")
else:
    if _lost:
        print(f"\n\nWitness DOWNGRADE forced: dropping {', '.join(_lost)}")
    with open(out_path, 'w') as f:
        json.dump(witness, f, indent=2)
    print(f"\n\nWitness written to: {out_path.name}")
    print("Done.")


# ══════════════════════════════════════════════════════════════
#  HOMFLYPT SU(N) COST VECTORS (multi-channel operator selection)
# ══════════════════════════════════════════════════════════════
# The operator-selection LP above uses SU(2) cost vectors (Markov
# trace values). For SU(N>2), different cost vectors give different
# optimal operators — different binding-energy predictions per
# representation-theoretic channel.
#
# Usage (when homflypt_engine is available):
#   from homflypt_engine import homflypt_operator_cost_vector
#   costs_su3 = homflypt_operator_cost_vector(
#       basis_braids=[(name, word) for name, word in ...],
#       target_braid=proton_word,
#       n_strands=3, N=3, q=q0
#   )
#
# Per prop:markov-trace-ratio-exact, cost-vector RATIOS are exact
# regardless of normalisation — the LP optimal solution x* and
# shadow prices y* are normalisation-independent.
#
# See rem:archimedean-image-table row 9 for the LP duality
# interpretation across SU(N) channels.
