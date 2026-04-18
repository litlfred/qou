#!/usr/bin/env python3
"""
Symbolic computation of γ⁴ · 𝔭 in H₃(q).

Keeps the photon's (φ₀, φ₁, φ₀₁) and the proton's six NF coefficients
(p_γ, p_σ₀, p_σ₁, p_L₊, p_L₋, p_e⁻) and H_A = q − q⁻¹ as symbols.
No numerical substitution until the final display.

Usage:
    cd folio-assistant/computations && python3 gamma4-hits-proton-symbolic.py
"""
import json
import subprocess
from pathlib import Path

import sympy as sp

try:
    SHA = subprocess.check_output(
        ['git', 'rev-parse', 'HEAD'],
        cwd=str(Path(__file__).resolve().parent.parent.parent)
    ).decode().strip()
except Exception:
    SHA = "unknown"

# ── Symbols ──────────────────────────────────────────────────────
HA = sp.Symbol('H_A')
phi0, phi1, phi01 = sp.symbols('phi_0 phi_1 phi_{01}')
pG, pS0, pS1, pLp, pLm, pE = sp.symbols('p_gamma p_{sigma_0} p_{sigma_1} p_{L_+} p_{L_-} p_{e^-}')

# H₃ NF basis — same as four-term-photon-to-atoms.py
NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_NAMES = ["gamma", "sigma_0", "sigma_1", "L_+", "L_-", "e^-"]
NF_LATEX = [r"\gamma", r"\sigma_0", r"\sigma_1", r"L_+", r"L_-", r"e^-"]


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
            # σᵢ² = H_A·σᵢ + 1
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
            # braid: σ_a σ_b σ_a = σ_b σ_a σ_b when |a-b|=1
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


def fmt_latex(vec):
    lines = []
    for name, val in zip(NF_LATEX, vec):
        simp = sp.collect(sp.expand(val), [phi0, phi1, phi01])
        lines.append(f"  {name}:  {sp.latex(simp)}")
    return "\n".join(lines)


def fmt_str(vec):
    lines = []
    for name, val in zip(NF_NAMES, vec):
        simp = sp.collect(sp.expand(val), [phi0, phi1, phi01])
        lines.append(f"  {name}:  {simp}")
    return "\n".join(lines)


# ══════════════════════════════════════════════════════════════
#  Symbolic proton and 4-term photon
# ══════════════════════════════════════════════════════════════

print("=" * 78)
print("SYMBOLIC γ⁴ · 𝔭  in  H₃(q)")
print(f"Commit: {SHA[:8]}")
print("=" * 78)

# Proton is a fully generic element of the NF basis
proton = {
    ():         pG,
    (0,):       pS0,
    (1,):       pS1,
    (0, 1):     pLp,
    (1, 0):     pLm,
    (0, 1, 0):  pE,
}

# 4-term photon
gamma4 = {
    ():         sp.Integer(1),
    (0,):       phi0,
    (1,):       phi1,
    (0, 1):     phi01,
}

# ══════════════════════════════════════════════════════════════
#  Compute γ⁴ · 𝔭
# ══════════════════════════════════════════════════════════════

print("\n── γ⁴ · 𝔭 (symbolic, grouped by basis element) ──\n")
prod = reduce_nf(hecke_mul(gamma4, proton))
prod_vec = to_vec(prod)
print(fmt_str(prod_vec))

# ══════════════════════════════════════════════════════════════
#  Compute 𝔭 · γ⁴  and commutator
# ══════════════════════════════════════════════════════════════

print("\n── 𝔭 · γ⁴ (symbolic) ──\n")
prod_rev = reduce_nf(hecke_mul(proton, gamma4))
prod_rev_vec = to_vec(prod_rev)
print(fmt_str(prod_rev_vec))

print("\n── [γ⁴, 𝔭] = γ⁴·𝔭 − 𝔭·γ⁴ ──\n")
comm_vec = [sp.expand(a - b) for a, b in zip(prod_vec, prod_rev_vec)]
print(fmt_str(comm_vec))

# ══════════════════════════════════════════════════════════════
#  LaTeX form
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("LaTeX: γ⁴ · 𝔭  =  Σ c_i · b_i  where c_i is:")
print("=" * 78 + "\n")
print(fmt_latex(prod_vec))

# ══════════════════════════════════════════════════════════════
#  Left-multiplication matrix of γ⁴ on the NF basis
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("LEFT-MULTIPLICATION MATRIX  L_{γ⁴}[i,j]  (γ⁴ · basis_j → coefficient of basis_i)")
print("=" * 78)
M = sp.zeros(6, 6)
for j, bj in enumerate(NF_BASIS):
    basis_elem = {bj: sp.Integer(1)}
    col_nf = reduce_nf(hecke_mul(gamma4, basis_elem))
    col_vec = to_vec(col_nf)
    for i in range(6):
        M[i, j] = col_vec[i]

# Print matrix
print(f"\n  rows/cols: {NF_NAMES}\n")
for i in range(6):
    row = " | ".join(f"{sp.collect(M[i,j], [phi0, phi1, phi01])}" for j in range(6))
    print(f"  {NF_NAMES[i]:>7}: {row}")

print("\nLaTeX matrix L_{γ⁴}:")
print(sp.latex(M))

# ══════════════════════════════════════════════════════════════
#  Substitute in numerical proton + φ's for sanity
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("SANITY CHECK: substitute numerical values, compare to numerical script")
print("=" * 78)

q0 = sp.Rational("1.1099785956")
HA_val = q0 - 1 / q0

subs = {
    HA:   HA_val,
    pG:   sp.Float("-0.099658"),
    pS0:  sp.Float("+0.035729"),
    pS1:  sp.Float("+0.997570"),
    pLp:  sp.Float("+0.099354"),
    pLm:  sp.Float("+0.009337"),
    pE:   sp.Float("-0.043208"),
    phi0: sp.Float("0.0487"),
    phi1: sp.Float("0.0487"),
    phi01: sp.Float("0.02"),
}

print("\n  γ⁴ · 𝔭 numerical (from symbolic):")
for name, val in zip(NF_NAMES, prod_vec):
    v = complex(val.subs(subs))
    print(f"    {name:>7}: {v.real:+.6f}")

# ══════════════════════════════════════════════════════════════
#  Witness
# ══════════════════════════════════════════════════════════════

witness = {
    "metadata": {"commit": SHA, "symbolic": True},
    "product_gamma4_proton": {
        NF_NAMES[i]: str(sp.collect(prod_vec[i], [phi0, phi1, phi01]))
        for i in range(6)
    },
    "product_gamma4_proton_latex": {
        NF_NAMES[i]: sp.latex(sp.collect(prod_vec[i], [phi0, phi1, phi01]))
        for i in range(6)
    },
    "product_proton_gamma4": {
        NF_NAMES[i]: str(sp.collect(prod_rev_vec[i], [phi0, phi1, phi01]))
        for i in range(6)
    },
    "commutator": {
        NF_NAMES[i]: str(sp.collect(comm_vec[i], [phi0, phi1, phi01]))
        for i in range(6)
    },
    "left_mult_matrix_gamma4": [
        [str(M[i, j]) for j in range(6)] for i in range(6)
    ],
}

out_path = Path(__file__).parent / "gamma4-hits-proton-symbolic.witness.json"
with out_path.open("w") as f:
    json.dump(witness, f, indent=2)
print(f"\n  Witness written: {out_path.name}")
