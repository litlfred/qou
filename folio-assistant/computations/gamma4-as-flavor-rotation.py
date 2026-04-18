#!/usr/bin/env python3
"""
Express γ⁴ · B₃(u,u,d) as a Borromean braid over flavor-dressed quarks.

Idea:
    p = B₃(u,u,d) := B₃ · C(u,u;σ₀) · C(u,d;σ₀) · C(u,d;σ₁)

is a Borromean confinement of a specific quark triple.  We ask:

    γ⁴ · B₃(u,u,d) =?= Σ_{T ∈ {u,d}³} c_T(φ, H_A) · B₃(T)

i.e. can the photon's action be absorbed into a SUPERPOSITION OVER
QUARK FLAVOR TRIPLES, each confined by the same Borromean braid?

This is the "flavor-rotation" reading: γ⁴ does not produce new
braid topology, it only reshuffles the quark-flavor assignments.

We compute all 8 flavor triples {u,d}³, build their H₃(q) NF vectors
symbolically in H_A, then solve the linear system

    γ⁴·p_{uud}  =  Σ c_T · p_T + residual

for the coefficients c_T and check if residual = 0 (exact flavor
rotation) or ≠ 0 (requires non-Borromean content).

Usage:
    cd folio-assistant/computations && python3 gamma4-as-flavor-rotation.py
"""
import json
import subprocess
from pathlib import Path
from itertools import product

import sympy as sp

try:
    SHA = subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'],
        cwd=str(Path(__file__).resolve().parent.parent.parent)
    ).decode().strip()
except Exception:
    SHA = "unknown"

HA = sp.Symbol('H_A')
phi0, phi1, phi01 = sp.symbols('phi_0 phi_1 phi_{01}')

NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_NAMES = ["gamma", "sigma_0", "sigma_1", "L_+", "L_-", "e^-"]

# Flavor→ε mapping
# ε_{ij} = 0 if same type, H_A/2 if mixed ud, H_A if both d (same as dd same-type? check)
# From four-term-photon-to-atoms.py crossing():
#   C(u,u;σ) = σ           →  ε = 0
#   C(d,d;σ) = σ - H_A     →  ε = H_A
#   C(u,d;σ) = σ - H_A/2   →  ε = H_A/2
def eps(a, b):
    if a == b == 'u':
        return sp.Integer(0)
    if a == b == 'd':
        return HA
    return HA / 2


# ── Hecke machinery ──────────────────────────────────────────────
def hecke_mul(t1, t2):
    result = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            result[w] = result.get(w, sp.Integer(0)) + c1 * c2
    return {w: sp.expand(c) for w, c in result.items() if sp.simplify(c) != 0}


def reduce_nf(terms):
    changed = True
    while changed:
        changed = False
        new_terms = {}
        for word, coeff in terms.items():
            if sp.simplify(coeff) == 0:
                continue
            done = False
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1]:
                    i = word[pos]
                    pre, suf = word[:pos], word[pos + 2:]
                    new_terms[pre + (i,) + suf] = \
                        new_terms.get(pre + (i,) + suf, sp.Integer(0)) + coeff * HA
                    new_terms[pre + suf] = \
                        new_terms.get(pre + suf, sp.Integer(0)) + coeff
                    done = changed = True
                    break
            if done:
                continue
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and abs(a - b) == 1:
                    new_trip = (b, a, b)
                    if new_trip < (a, b, a):
                        nw = word[:pos] + new_trip + word[pos + 3:]
                        new_terms[nw] = new_terms.get(nw, sp.Integer(0)) + coeff
                        done = changed = True
                        break
            if not done:
                new_terms[word] = new_terms.get(word, sp.Integer(0)) + coeff
        terms = {w: sp.expand(c) for w, c in new_terms.items()
                 if sp.simplify(c) != 0}
    return terms


def to_vec(terms):
    return [sp.expand(terms.get(b, sp.Integer(0))) for b in NF_BASIS]


# ── Build B₃ once ───────────────────────────────────────────────
sigma0 = {(0,): sp.Integer(1)}
sigma1 = {(1,): sp.Integer(1)}
sigma1_inv = {(1,): sp.Integer(1), (): -HA}

B3 = {(): sp.Integer(1)}
for _ in range(3):
    B3 = hecke_mul(B3, sigma0)
    B3 = hecke_mul(B3, sigma1_inv)


def B3_of_triple(q1, q2, q3):
    """Return NF vector of B₃(q1,q2,q3) = B₃·C(q1,q2;σ₀)·C(q1,q3;σ₀)·C(q2,q3;σ₁)."""
    C12 = {(0,): sp.Integer(1), (): -eps(q1, q2)}
    C13 = {(0,): sp.Integer(1), (): -eps(q1, q3)}
    C23 = {(1,): sp.Integer(1), (): -eps(q2, q3)}
    w = hecke_mul(B3, C12)
    w = hecke_mul(w, C13)
    w = hecke_mul(w, C23)
    return to_vec(reduce_nf(w))


# ══════════════════════════════════════════════════════════════
#  Build all 8 flavor triples
# ══════════════════════════════════════════════════════════════

print("=" * 78)
print("γ⁴ · B₃(u,u,d) as a LINEAR COMBINATION over {u,d}³ FLAVOR TRIPLES")
print(f"Commit: {SHA[:8]}")
print("=" * 78)

triples = list(product(['u', 'd'], repeat=3))
triple_vecs = {}
print("\nFlavor triples and their NFs (symbolic in H_A):\n")
for t in triples:
    v = B3_of_triple(*t)
    triple_vecs[t] = v
    name = "".join(t)
    print(f"  B₃({name}) =")
    for nm, val in zip(NF_NAMES, v):
        simp = sp.nsimplify(sp.expand(val))
        print(f"    [{nm}]: {simp}")
    print()

# ══════════════════════════════════════════════════════════════
#  Compute γ⁴ · B₃(u,u,d)
# ══════════════════════════════════════════════════════════════

# Proton raw expression (symbolic)
gamma4 = {(): sp.Integer(1), (0,): phi0, (1,): phi1, (0, 1): phi01}
C12 = {(0,): sp.Integer(1), (): -eps('u', 'u')}   # 0
C13 = {(0,): sp.Integer(1), (): -eps('u', 'd')}   # H_A/2
C23 = {(1,): sp.Integer(1), (): -eps('u', 'd')}   # H_A/2
proton_raw = hecke_mul(B3, C12)
proton_raw = hecke_mul(proton_raw, C13)
proton_raw = hecke_mul(proton_raw, C23)

gp_raw = hecke_mul(gamma4, proton_raw)
gp_nf = reduce_nf(gp_raw)
gp_vec = to_vec(gp_nf)

print("=" * 78)
print("γ⁴ · B₃(u,u,d):  target NF (symbolic in φ's, H_A)")
print("=" * 78 + "\n")
for nm, val in zip(NF_NAMES, gp_vec):
    print(f"  [{nm}]: {sp.collect(sp.expand(val), [phi0, phi1, phi01])}")

# ══════════════════════════════════════════════════════════════
#  Solve for decomposition  γ⁴·p  =  Σ c_T(φ, H_A) · B₃(T)
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("SOLVE:  γ⁴ · B₃(u,u,d) = Σ_T c_T · B₃(T)  with T ∈ {u,d}³ (8 unknowns)")
print("=" * 78 + "\n")

# Unknowns: one coefficient per flavor triple
c_vars = {t: sp.Symbol(f"c_{{{''.join(t)}}}") for t in triples}

# 6 equations (one per NF basis element), 8 unknowns → 2-dim solution space
equations = []
for i in range(6):
    lhs = gp_vec[i]
    rhs = sum(c_vars[t] * triple_vecs[t][i] for t in triples)
    equations.append(sp.expand(lhs - rhs))

# Linear solve; treat H_A and φ's as parameters
unknowns = list(c_vars.values())
sol = sp.solve(equations, unknowns, dict=True)

if sol:
    sol_dict = sol[0]
    print(f"  System: 6 equations, 8 unknowns — underdetermined.\n")
    print(f"  {len(sol_dict)} unknowns pinned; {8 - len(sol_dict)} free parameter(s):\n")

    fixed = set(sol_dict.keys())
    free = [c for c in unknowns if c not in fixed]
    print(f"  Free: {free}\n")

    print("  Solution (with free parameters):\n")
    for t in triples:
        c = c_vars[t]
        val = sol_dict.get(c, c)
        val_c = sp.collect(sp.expand(val), [phi0, phi1, phi01] + free)
        name = "".join(t)
        print(f"    c_{name:<4} = {val_c}")

    # Specialise: set all free parameters = 0 for a canonical representative
    print(f"\n  Canonical (set {', '.join(str(f) for f in free)} = 0):\n")
    spec_subs = {f: 0 for f in free}
    canonical = {}
    for t in triples:
        c = c_vars[t]
        val = sol_dict.get(c, 0)
        val_s = sp.collect(sp.expand(val.subs(spec_subs))
                           if hasattr(val, 'subs') else val,
                           [phi0, phi1, phi01])
        canonical[t] = val_s
        name = "".join(t)
        print(f"    c_{name:<4} = {val_s}")

    # Check reconstruction
    print("\n  Reconstruction check (canonical):\n")
    for i in range(6):
        rhs = sum(canonical[t] * triple_vecs[t][i] for t in triples)
        diff = sp.simplify(sp.expand(gp_vec[i] - rhs))
        print(f"    residual[{NF_NAMES[i]}] = {diff}")

else:
    print("  No solution — γ⁴·p is NOT in the span of {B₃(T) : T ∈ {u,d}³}.")
    print("  i.e. γ⁴ produces non-Borromean content (extra braid topology).")

# ══════════════════════════════════════════════════════════════
#  Structural readout: which photon modes create which flavor flips?
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("WHICH PHOTON MODE FLIPS WHICH QUARK?")
print("=" * 78)
print("""
  Isolating each φ-channel in the canonical decomposition shows
  which flavor triples the photon populates.
""")

if sol:
    for phi_sym, phi_name in [(phi0, 'φ₀  (horizontal polarisation)'),
                              (phi1, 'φ₁  (vertical polarisation)'),
                              (phi01, 'φ₀₁ (Hopf dressing)')]:
        print(f"\n  {phi_name}:")
        for t in triples:
            c = canonical.get(t, 0)
            if hasattr(c, 'coeff'):
                piece = sp.expand(c.coeff(phi_sym))
                if piece != 0:
                    name = "".join(t)
                    print(f"    B₃({name}):  {sp.nsimplify(piece)}")

    print(f"\n  Vacuum (φ-independent baseline, should ≈ proton itself):")
    for t in triples:
        c = canonical.get(t, 0)
        if hasattr(c, 'subs'):
            piece = sp.nsimplify(sp.expand(c.subs({phi0: 0, phi1: 0, phi01: 0})))
        else:
            piece = c
        if piece != 0:
            name = "".join(t)
            print(f"    B₃({name}):  {piece}")

# ══════════════════════════════════════════════════════════════
#  Witness
# ══════════════════════════════════════════════════════════════

witness = {
    "metadata": {"commit": SHA, "symbolic": True,
                 "flavor_rotation": True},
    "triple_nfs": {
        "".join(t): {NF_NAMES[i]: str(sp.nsimplify(triple_vecs[t][i]))
                     for i in range(6)}
        for t in triples
    },
    "gamma4_B3_uud_nf": {
        NF_NAMES[i]: str(sp.collect(sp.expand(gp_vec[i]),
                                    [phi0, phi1, phi01]))
        for i in range(6)
    },
}
if sol:
    witness["flavor_rotation_decomposition"] = {
        "".join(t): str(canonical[t]) for t in triples
    }
    witness["free_parameters"] = [str(f) for f in free]

out_path = Path(__file__).parent / "gamma4-as-flavor-rotation.witness.json"
with out_path.open("w") as f:
    json.dump(witness, f, indent=2)
print(f"\nWitness written: {out_path.name}")
