#!/usr/bin/env python3
"""
Symbolic γ⁴ · 𝔭 as an explicit braid word in quark generators.

Instead of using a precomputed proton NF vector (p_γ, p_σ₀, ...),
this script writes the proton as its constructor word

    𝔭 = B₃ · C(q₁,q₂;σ₀) · C(q₁,q₃;σ₀) · C(q₂,q₃;σ₁)

where
    B₃ = (σ₀σ₁⁻¹)³ = σ₀(σ₁-H_A)σ₀(σ₁-H_A)σ₀(σ₁-H_A)
    C(i,j;σ_k) = σ_k - ε_{ij}, with ε_{uu}=0, ε_{ud}=H_A/2, ε_{dd}=H_A

and computes γ⁴ · 𝔭 keeping (φ₀, φ₁, φ₀₁, H_A, ε₁₂, ε₁₃, ε₂₃) as
symbols.  Results are shown both

  (a) as a raw braid-word polynomial (before NF reduction), exposing
      which quark pair contributes which crossing, and
  (b) as the reduced H₃(q) NF, with each basis coefficient factored
      by quark-pair type (ε's).

Usage:
    cd folio-assistant/computations && python3 gamma4-hits-proton-quark-words.py
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
# Crossing type corrections — kept symbolic so we can see
# flavor dependence.  Specialise at the end.
eps12, eps13, eps23 = sp.symbols('epsilon_{12} epsilon_{13} epsilon_{23}')

NF_BASIS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_NAMES = ["gamma", "sigma_0", "sigma_1", "L_+", "L_-", "e^-"]


# ── Hecke multiplication and NF reduction (symbolic) ─────────────
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


def word_str(word):
    if not word:
        return "1"
    return "".join(f"σ_{i}" for i in word)


# ══════════════════════════════════════════════════════════════
#  Build the proton as an explicit braid word
# ══════════════════════════════════════════════════════════════

print("=" * 78)
print("γ⁴ · 𝔭  as a BRAID WORD in quark generators")
print(f"Commit: {SHA[:8]}")
print("=" * 78)

# σ₁⁻¹ = σ₁ - H_A  (from (σ₁ − q)(σ₁ + q⁻¹) = 0 → σ₁ · σ₁⁻¹ = 1)
sigma0 = {(0,): sp.Integer(1)}
sigma1 = {(1,): sp.Integer(1)}
sigma1_inv = {(1,): sp.Integer(1), (): -HA}

# B₃ = (σ₀ σ₁⁻¹)³
B3 = {(): sp.Integer(1)}
for _ in range(3):
    B3 = hecke_mul(B3, sigma0)
    B3 = hecke_mul(B3, sigma1_inv)

# Typed crossings (kept symbolic in ε so flavor content is visible)
#   C(q_i, q_j ; σ_k) = σ_k − ε_{ij}
C12 = {(0,): sp.Integer(1), (): -eps12}   # quarks 1,2 on σ₀
C13 = {(0,): sp.Integer(1), (): -eps13}   # quarks 1,3 on σ₀
C23 = {(1,): sp.Integer(1), (): -eps23}   # quarks 2,3 on σ₁

# Proton = B₃ · C₁₂ · C₁₃ · C₂₃
proton_raw = hecke_mul(B3, C12)
proton_raw = hecke_mul(proton_raw, C13)
proton_raw = hecke_mul(proton_raw, C23)

print("\n── PROTON as raw braid word (pre-NF-reduction) ──\n")
print(f"  𝔭 = B₃ · (σ₀ − ε₁₂)(σ₀ − ε₁₃)(σ₁ − ε₂₃)")
print(f"    with B₃ = (σ₀ σ₁⁻¹)³ = σ₀(σ₁−H_A)σ₀(σ₁−H_A)σ₀(σ₁−H_A)\n")
print(f"  {len(proton_raw)} distinct words before NF reduction")
for word, coeff in sorted(proton_raw.items(), key=lambda kv: (len(kv[0]), kv[0])):
    cc = sp.collect(sp.expand(coeff), [eps12, eps13, eps23])
    print(f"    {word_str(word):<18} · ({cc})")

# ══════════════════════════════════════════════════════════════
#  Reduce proton to NF and record by-quark-pair contributions
# ══════════════════════════════════════════════════════════════

proton_nf = reduce_nf(proton_raw)
proton_vec = to_vec(proton_nf)

print("\n── PROTON NF (symbolic in H_A, ε₁₂, ε₁₃, ε₂₃) ──\n")
for name, val in zip(NF_NAMES, proton_vec):
    cc = sp.collect(sp.expand(val), [eps12, eps13, eps23])
    print(f"  [{name}]:  {cc}")

# ══════════════════════════════════════════════════════════════
#  Build γ⁴ and compute γ⁴ · 𝔭 on the quark word
# ══════════════════════════════════════════════════════════════

gamma4 = {
    ():       sp.Integer(1),
    (0,):     phi0,
    (1,):     phi1,
    (0, 1):   phi01,
}

print("\n" + "=" * 78)
print("γ⁴ · 𝔭  on the BRAID WORD  (γ⁴ applied to raw proton, pre-reduction)")
print("=" * 78)
print("""
  γ⁴ = 1 + φ₀·σ₀ + φ₁·σ₁ + φ₀₁·σ₀σ₁

  Distributing over the proton's raw braid-word sum gives four
  contributions per word w in 𝔭:

    1 · w,   φ₀·(σ₀ w),   φ₁·(σ₁ w),   φ₀₁·(σ₀ σ₁ w)

  Each is a new braid word; reduction happens afterwards.
""")

gp_raw = hecke_mul(gamma4, proton_raw)
print(f"  γ⁴ · 𝔭  has {len(gp_raw)} distinct words before NF reduction.")
# Show the top 10 longest words (to keep output sane)
sorted_words = sorted(gp_raw.items(), key=lambda kv: (-len(kv[0]), kv[0]))
print(f"\n  Longest-word contributions (showing up to 10):\n")
for word, coeff in sorted_words[:10]:
    cc = sp.collect(sp.expand(coeff),
                    [phi0, phi1, phi01, eps12, eps13, eps23])
    print(f"    {word_str(word):<26} · ({cc})")

# ══════════════════════════════════════════════════════════════
#  Reduce γ⁴ · 𝔭 to NF, show by-quark-pair contributions
# ══════════════════════════════════════════════════════════════

gp_nf = reduce_nf(gp_raw)
gp_vec = to_vec(gp_nf)

print("\n" + "=" * 78)
print("γ⁴ · 𝔭  REDUCED TO H₃(q) NF (symbolic in everything)")
print("=" * 78)
print("""
  Each NF coefficient is a polynomial in (φ's, H_A, ε's).
  ε₁₂: type of quark pair 1↔2 (u-u in proton → 0)
  ε₁₃: type of quark pair 1↔3 (u-d in proton → H_A/2)
  ε₂₃: type of quark pair 2↔3 (u-d in proton → H_A/2)
""")
for name, val in zip(NF_NAMES, gp_vec):
    cc = sp.collect(sp.expand(val),
                    [phi0, phi1, phi01, eps12, eps13, eps23])
    print(f"  [{name}]:  {cc}")

# ══════════════════════════════════════════════════════════════
#  Specialise to the proton (uud)
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("SPECIALISE TO PROTON (u,u,d):  ε₁₂ = 0,  ε₁₃ = H_A/2,  ε₂₃ = H_A/2")
print("=" * 78 + "\n")
proton_subs = {eps12: 0, eps13: HA / 2, eps23: HA / 2}

print("── Proton NF in H_A alone ──")
for name, val in zip(NF_NAMES, proton_vec):
    pv = sp.nsimplify(sp.expand(val.subs(proton_subs)))
    print(f"  [{name}]:  {pv}")

print("\n── γ⁴ · 𝔭  (proton specialisation) ──")
for name, val in zip(NF_NAMES, gp_vec):
    cc = sp.collect(sp.expand(val.subs(proton_subs)), [phi0, phi1, phi01])
    print(f"  [{name}]:  {cc}")

# ══════════════════════════════════════════════════════════════
#  Specialise to NEUTRON (u,d,d):  ε₁₂ = H_A/2, ε₁₃ = H_A/2, ε₂₃ = H_A
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("SPECIALISE TO NEUTRON (u,d,d):  ε₁₂ = H_A/2,  ε₁₃ = H_A/2,  ε₂₃ = H_A")
print("=" * 78 + "\n")
neutron_subs = {eps12: HA / 2, eps13: HA / 2, eps23: HA}

print("── Neutron NF in H_A alone ──")
for name, val in zip(NF_NAMES, proton_vec):
    pv = sp.nsimplify(sp.expand(val.subs(neutron_subs)))
    print(f"  [{name}]:  {pv}")

print("\n── γ⁴ · 𝔫  (neutron specialisation) ──")
for name, val in zip(NF_NAMES, gp_vec):
    cc = sp.collect(sp.expand(val.subs(neutron_subs)), [phi0, phi1, phi01])
    print(f"  [{name}]:  {cc}")

# ══════════════════════════════════════════════════════════════
#  Witness
# ══════════════════════════════════════════════════════════════

witness = {
    "metadata": {"commit": SHA, "symbolic": True,
                 "quark_word": True},
    "proton_braid_word": {
        word_str(w): str(sp.collect(sp.expand(c), [eps12, eps13, eps23]))
        for w, c in proton_raw.items()
    },
    "proton_nf_symbolic": {
        NF_NAMES[i]: str(sp.collect(sp.expand(proton_vec[i]),
                                    [eps12, eps13, eps23]))
        for i in range(6)
    },
    "gamma4_proton_nf_symbolic": {
        NF_NAMES[i]: str(sp.collect(
            sp.expand(gp_vec[i]),
            [phi0, phi1, phi01, eps12, eps13, eps23]))
        for i in range(6)
    },
    "gamma4_proton_specialised_uud": {
        NF_NAMES[i]: str(sp.collect(
            sp.expand(gp_vec[i].subs(proton_subs)),
            [phi0, phi1, phi01]))
        for i in range(6)
    },
    "gamma4_neutron_specialised_udd": {
        NF_NAMES[i]: str(sp.collect(
            sp.expand(gp_vec[i].subs(neutron_subs)),
            [phi0, phi1, phi01]))
        for i in range(6)
    },
}

out_path = Path(__file__).parent / "gamma4-hits-proton-quark-words.witness.json"
with out_path.open("w") as f:
    json.dump(witness, f, indent=2)
print(f"\nWitness written: {out_path.name}")
