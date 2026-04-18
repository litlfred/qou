#!/usr/bin/env python3
"""
Compute NF of γ⁴ · proton in H₃(q).

The 4-term photon γ⁴ = 𝟙 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁
hits a bare proton (no electron shell).  Does the Hecke NF
pick up a non-trivial product?  What happens to (φ₀, φ₁, φ₀₁)?

Uses the same machinery as four-term-photon-to-atoms.py.

Usage:
    cd folio-assistant/computations && python3 gamma4-hits-proton.py
"""
import json
import subprocess
from pathlib import Path

from q_parameter import Q as q0, HA as HA_val
from experimental_constants import M_E_MEV

try:
    SHA = subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'],
        cwd=str(Path(__file__).resolve().parent.parent.parent)
    ).decode().strip()
except Exception:
    SHA = "unknown"

HA = HA_val
z = 1.0 / (q0**0.5 + q0**(-0.5))

# H₃ NF basis
NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_NAMES = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]


def hecke_mul(t1, t2):
    result = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            result[w] = result.get(w, 0.0) + c1 * c2
    return {w: c for w, c in result.items() if abs(c) > 1e-15}


def reduce_nf(terms):
    changed = True
    while changed:
        changed = False
        new_terms = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False
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


def markov_trace(vec):
    TR_M = [1.0, z, z, z**2, z**2, z**3]
    return sum(c * t for c, t in zip(vec, TR_M))


def nf_net(vec):
    return sum(vec)


def print_nf(label, vec, indent=2):
    parts = []
    for name, val in zip(NF_NAMES, vec):
        if abs(val) > 1e-15:
            parts.append(f"{val:+.6f}·{name}")
    pad = " " * indent
    print(f"{pad}{label}: {' '.join(parts)}")
    print(f"{pad}  net = {nf_net(vec):+.6f}, tr_M = {markov_trace(vec):+.6f}")


def expand_inverse(word):
    terms = {(): 1.0}
    for g in word:
        new_terms = {}
        if g >= 0:
            for w, c in terms.items():
                nw = w + (g,)
                new_terms[nw] = new_terms.get(nw, 0.0) + c
        else:
            i = -g - 1
            for w, c in terms.items():
                nw = w + (i,)
                new_terms[nw] = new_terms.get(nw, 0.0) + c
                new_terms[w] = new_terms.get(w, 0.0) - c * HA
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms


def crossing(type_i, type_j, gen):
    if type_i == type_j == 'u':
        return {(gen,): 1.0}
    elif type_i == type_j == 'd':
        return {(gen,): 1.0, (): -HA}
    else:
        return {(gen,): 1.0, (): -HA / 2}


# ══════════════════════════════════════════════════════════════
#  BUILD PROTON (same as four-term-photon-to-atoms.py)
# ══════════════════════════════════════════════════════════════

print("=" * 78)
print("γ⁴ · PROTON IN H₃(q)")
print(f"q₀ = {q0:.10f}  |  HA = q - q⁻¹ = {HA:.10f}  |  z = {z:.10f}")
print(f"Commit: {SHA[:8]}")
print("=" * 78)

# B₃ Borromean confinement operator
b3_raw = expand_inverse((0, -2, 0, -2, 0, -2))
b3_nf = reduce_nf(b3_raw)

# Build proton (u, u, d) with typed crossings
elem = dict(b3_nf)
for i, j in [(0, 1), (0, 2), (1, 2)]:
    gen = min(i, j)
    if gen > 1:
        gen = 1
    t_i, t_j = ['u', 'u', 'd'][i], ['u', 'u', 'd'][j]
    cx = crossing(t_i, t_j, gen)
    elem = reduce_nf(hecke_mul(elem, cx))

proton = dict(elem)
proton_vec = to_vec(proton)

print("\n── PROTON NF (bare, no shell) ──")
print_nf("𝔭", proton_vec)

# ══════════════════════════════════════════════════════════════
#  4-TERM PHOTON γ⁴
# ══════════════════════════════════════════════════════════════

PHI_0 = 0.0487     # same linear-polarisation value as four-term-photon-to-atoms
PHI_1 = 0.0487
PHI_01 = 0.02      # non-trivial Hopf dressing (opens e⁻ channel)

gamma4 = {
    (): 1.0,
    (0,): PHI_0,
    (1,): PHI_1,
    (0, 1): PHI_01,
}
gamma4_vec = to_vec(gamma4)

print("\n── 4-TERM PHOTON γ⁴ ──")
print(f"  (φ₀, φ₁, φ₀₁) = ({PHI_0}, {PHI_1}, {PHI_01})")
print_nf("γ⁴", gamma4_vec)

# ══════════════════════════════════════════════════════════════
#  γ⁴ · PROTON  (and proton · γ⁴)
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("PRODUCT γ⁴ · 𝔭 IN H₃(q)")
print("=" * 78)

gp_raw = hecke_mul(gamma4, proton)
gp_nf = reduce_nf(gp_raw)
gp_vec = to_vec(gp_nf)

print_nf("γ⁴ · 𝔭", gp_vec)

print("\n── REVERSE ORDER 𝔭 · γ⁴ (for non-commutativity check) ──")
pg_raw = hecke_mul(proton, gamma4)
pg_nf = reduce_nf(pg_raw)
pg_vec = to_vec(pg_nf)
print_nf("𝔭 · γ⁴", pg_vec)

commutator = [a - b for a, b in zip(gp_vec, pg_vec)]
print("\n── COMMUTATOR [γ⁴, 𝔭] = γ⁴·𝔭 − 𝔭·γ⁴ ──")
print_nf("[γ⁴, 𝔭]", commutator)

# ══════════════════════════════════════════════════════════════
#  TRACK φ's THROUGH THE PRODUCT
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("HOW DO THE φ's PROPAGATE?  Scan (φ₀, φ₁, φ₀₁) → output NF")
print("=" * 78)

print(f"\n  Reference proton NF (φ-free):")
print_nf("  𝔭", proton_vec)
print()

# Sweep each φ independently with others = 0 to isolate contribution
scenarios = [
    ("φ₀ only (horiz. polarization)",  0.0487, 0.0,     0.0),
    ("φ₁ only (vert. polarization)",   0.0,    0.0487,  0.0),
    ("φ₀₁ only (Hopf dressing)",       0.0,    0.0,     0.02),
    ("full 4-term",                    0.0487, 0.0487,  0.02),
    ("zero photon (identity)",         0.0,    0.0,     0.0),
]

print(f"  {'scenario':<35} {'γ':>9} {'σ₀':>9} {'σ₁':>9} {'L₊':>9} {'L₋':>9} {'e⁻':>9}  {'Δe⁻':>9}")
print("  " + "─" * 108)
for name, f0, f1, f01 in scenarios:
    g = {(): 1.0}
    if f0:  g[(0,)] = f0
    if f1:  g[(1,)] = f1
    if f01: g[(0, 1)] = f01
    prod = reduce_nf(hecke_mul(g, proton))
    v = to_vec(prod)
    delta_e = v[5] - proton_vec[5]
    print(f"  {name:<35} " + " ".join(f"{v[i]:+.4f}" for i in range(6)) + f"  {delta_e:+.4f}")

# ══════════════════════════════════════════════════════════════
#  SUMMARY
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("INTERPRETATION")
print("=" * 78)
print(f"""
  The 4-term photon γ⁴ does operate on the bare proton — the Hecke product
  γ⁴ · 𝔭 has a non-trivial NF distinct from 𝔭 alone.

  Proton-only net:        {nf_net(proton_vec):+.6f}
  γ⁴ · 𝔭 net:             {nf_net(gp_vec):+.6f}
  Δnet (photon-induced):  {nf_net(gp_vec) - nf_net(proton_vec):+.6f}

  Proton-only e⁻ coeff:   {proton_vec[5]:+.6f}
  γ⁴ · 𝔭 e⁻ coeff:        {gp_vec[5]:+.6f}
  Δ(e⁻):                  {gp_vec[5] - proton_vec[5]:+.6f}

  The φ's DO NOT erase (that universality applies to confinement, i.e.,
  the construction of the proton). Once γ⁴ interacts with a built proton,
  it acts as a left-multiplier in H₃(q), and each φ coefficient
  distributes into the NF via the Hecke relations.

  Specifically:
    - φ₀ shifts σ₀ and γ (via σ₀² = HA·σ₀ + 1)
    - φ₁ shifts σ₁ and L₋ (via σ₁·𝔭-generators)
    - φ₀₁ opens the e⁻ channel (Hopf dressing → trefoil)
""")

# Write witness
out_path = Path(__file__).parent / "gamma4-hits-proton.witness.json"
witness = {
    "metadata": {
        "commit": SHA,
        "q0": q0,
        "HA": HA,
        "phi_0": PHI_0,
        "phi_1": PHI_1,
        "phi_01": PHI_01,
    },
    "proton_nf": {NF_NAMES[i]: proton_vec[i] for i in range(6)},
    "gamma4_nf": {NF_NAMES[i]: gamma4_vec[i] for i in range(6)},
    "product_gamma4_proton": {NF_NAMES[i]: gp_vec[i] for i in range(6)},
    "product_proton_gamma4": {NF_NAMES[i]: pg_vec[i] for i in range(6)},
    "commutator": {NF_NAMES[i]: commutator[i] for i in range(6)},
    "net": {
        "proton": nf_net(proton_vec),
        "gamma4_proton": nf_net(gp_vec),
        "delta_net": nf_net(gp_vec) - nf_net(proton_vec),
    },
    "markov_trace": {
        "proton": markov_trace(proton_vec),
        "gamma4_proton": markov_trace(gp_vec),
    },
    "phi_sweep": [],
}
for name, f0, f1, f01 in scenarios:
    g = {(): 1.0}
    if f0:  g[(0,)] = f0
    if f1:  g[(1,)] = f1
    if f01: g[(0, 1)] = f01
    prod = reduce_nf(hecke_mul(g, proton))
    v = to_vec(prod)
    witness["phi_sweep"].append({
        "scenario": name,
        "phi_0": f0, "phi_1": f1, "phi_01": f01,
        "nf": {NF_NAMES[i]: v[i] for i in range(6)},
        "delta_e": v[5] - proton_vec[5],
    })
with out_path.open("w") as f:
    json.dump(witness, f, indent=2)
print(f"  Witness written: {out_path.name}")
