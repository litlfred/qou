#!/usr/bin/env python3
"""
Gram matrix and Frobenius dual construction in H₃(q).

Computes:
  1. The 6×6 Gram matrix G_{ij} = tr_M(b_i · b_j)
  2. Its inverse G⁻¹
  3. The Frobenius dual K∨ = Σ_{i,j} c_i (G⁻¹)_{ij} b_j
     for key particles (e⁺, d-quark, colored photon, etc.)
  4. Demand profiles from negative NF coefficients

Usage:
    cd computations && python3 gram-matrix-dual.py
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import numpy as np
from datetime import datetime, timezone
from pathlib import Path

from mpmath import mp

# ── q parameter (canonical source) ───────────────────────────
try:
    from q_parameter import Q as q0, Q_INV as qi0, HA
except ImportError:
    _V = mp.mpf("2.029883212819307"); _R = mp.mpf("206.768283")  # noqa: P31 — display-only q_0 reconstruction in __main__ block; live value from q_parameter.Q
    _h = mp.sqrt(_V / _R); q0 = mp.mpf(1) / (mp.mpf(1) - _h)
    qi0 = mp.mpf(1) / q0; HA = q0 - qi0
# z, NF_BASIS, NF_NAMES, TR_M moved to pyhecke.gram via M2b inversion.
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[2] / "tools" / "pyhecke" / "python"))
from pyhecke.gram import z, NF_BASIS, NF_NAMES  # noqa: E402

print(f"q₀  = {q0:.10f}")
print(f"HA  = q−q⁻¹ = {HA:.10f}")
print(f"z   = 1/(q^½+q^-½) = {z:.10f}")

# ── NF basis ─────────────────────────────────────────────────
NF_LATEX = [r"\gamma", r"\sigma_0", r"\sigma_1", r"L_+", r"L_-", r"e^-"]

# Markov trace of each basis element:
#   tr_M(𝟏) = 1
#   tr_M(σ₀) = z  (Markov II)
#   tr_M(σ₁) = z  (Markov II)
#   tr_M(σ₀σ₁) = z²  (Markov II on σ₀ · σ₁)
#   tr_M(σ₁σ₀) = z²  (cyclicity)
#   tr_M(σ₀σ₁σ₀) = z³  (Markov chain: tr_M(σ₁σ₀σ₁) = z·tr_M(σ₀σ₁) = z·z² = z³)
#   NOT HA·z² + z — vertex volume product fails for adjacent generators.
from pyhecke.gram import TR_M as _TR_M_NATIVE  # noqa: E402
TR_M_BASIS = list(_TR_M_NATIVE)


def markov_trace_nf(nf_vec):
    """Markov trace of NF element: tr_M(Σ cᵢ bᵢ) = Σ cᵢ tr_M(bᵢ)."""
    return sum(c * t for c, t in zip(nf_vec, TR_M_BASIS))


# ── Hecke algebra engine (same as knot-operator-table.py) ────
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
                    pre, suf = word[:pos], word[pos + 2:]
                    w1 = pre + (word[pos],) + suf
                    w2 = pre + suf
                    new_terms[w1] = new_terms.get(w1, 0.0) + coeff * HA
                    new_terms[w2] = new_terms.get(w2, 0.0) + coeff
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


def to_nf_vector(terms):
    return [terms.get(b, 0.0) for b in NF_BASIS]


def basis_element(idx):
    return {NF_BASIS[idx]: 1.0}


def expand_inverse_word(word):
    """Expand σᵢ⁻¹ → σᵢ − HA using negative indices."""
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
                nw1 = w + (i,)
                new_terms[nw1] = new_terms.get(nw1, 0.0) + c
                new_terms[w] = new_terms.get(w, 0.0) - c * HA
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms


# ══════════════════════════════════════════════════════════════
#  1. GRAM MATRIX  G_{ij} = tr_M(b_i · b_j)
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  1. GRAM MATRIX  G_{ij} = tr_M(b_i · b_j)")
print("=" * 72)

G = np.zeros((6, 6))

for i in range(6):
    for j in range(6):
        prod = hecke_mul(basis_element(i), basis_element(j))
        nf = reduce_nf(prod)
        vec = to_nf_vector(nf)
        G[i, j] = markov_trace_nf(vec)

# Print G
hdr = f"  {'G':6s}"
for name in NF_NAMES:
    hdr += f" | {name:>10s}"
print(hdr)
print("  " + "-" * (len(hdr) - 2))
for i in range(6):
    line = f"  {NF_NAMES[i]:6s}"
    for j in range(6):
        line += f" | {G[i, j]:>10.6f}"
    print(line)

print(f"\n  det(G) = {np.linalg.det(G):.10f}")
print(f"  G is {'positive definite' if np.all(np.linalg.eigvals(G) > 0) else 'NOT positive definite'}")
print(f"  Eigenvalues: {np.linalg.eigvals(G)}")

# ══════════════════════════════════════════════════════════════
#  2. INVERSE GRAM MATRIX  G⁻¹
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  2. INVERSE GRAM MATRIX  G⁻¹")
print("=" * 72)

G_inv = np.linalg.inv(G)

hdr = f"  {'G⁻¹':6s}"
for name in NF_NAMES:
    hdr += f" | {name:>10s}"
print(hdr)
print("  " + "-" * (len(hdr) - 2))
for i in range(6):
    line = f"  {NF_NAMES[i]:6s}"
    for j in range(6):
        line += f" | {G_inv[i, j]:>10.4f}"
    print(line)

# Verify: G · G⁻¹ = I
check = G @ G_inv
max_err = np.max(np.abs(check - np.eye(6)))
print(f"\n  Verification: max|G·G⁻¹ - I| = {max_err:.2e}")

# ══════════════════════════════════════════════════════════════
#  3. FROBENIUS DUAL  K∨ = Σ_{i,j} c_i (G⁻¹)_{ij} b_j
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  3. FROBENIUS DUAL CONSTRUCTION")
print("=" * 72)


def frobenius_dual(nf_vec):
    """K∨ = Σ_{i,j} c_i (G⁻¹)_{ij} b_j"""
    c = np.array(nf_vec)
    return c @ G_inv  # Result is the dual NF vector


def print_particle(name, braid_desc, nf_vec):
    """Print a particle's NF, its dual, and demand profile."""
    dual_vec = frobenius_dual(nf_vec)
    net = sum(nf_vec)
    dual_net = sum(dual_vec)

    print(f"\n  ── {name}  ({braid_desc}) ──")
    hdr = f"  {'':12s}"
    for n in NF_NAMES:
        hdr += f" | {n:>8s}"
    hdr += f" | {'net':>8s}"
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))

    # NF
    line = f"  {'NF(K)':12s}"
    for v in nf_vec:
        line += f" | {v:>8.4f}"
    line += f" | {net:>8.4f}"
    print(line)

    # Dual
    line = f"  {'K∨':12s}"
    for v in dual_vec:
        line += f" | {v:>8.4f}"
    line += f" | {dual_net:>8.4f}"
    print(line)

    # Demand (negative in NF)
    neg_nf = [(NF_NAMES[k], nf_vec[k]) for k in range(6) if nf_vec[k] < -1e-10]
    # Supply (positive in NF)
    pos_nf = [(NF_NAMES[k], nf_vec[k]) for k in range(6) if nf_vec[k] > 1e-10]

    if neg_nf:
        print(f"  NF demand:  {', '.join(f'{n}={v:+.4f}' for n, v in neg_nf)}")
    else:
        print(f"  NF demand:  none (pure supply)")

    # Negative in dual
    neg_dual = [(NF_NAMES[k], dual_vec[k]) for k in range(6) if dual_vec[k] < -1e-10]
    if neg_dual:
        print(f"  Dual demand: {', '.join(f'{n}={v:+.4f}' for n, v in neg_dual)}")
    else:
        print(f"  Dual demand: none")

    # Verification: ⟨K∨, b_i⟩_F = c_i
    print(f"  Verify ⟨K∨, bᵢ⟩_F = cᵢ:")
    for k in range(6):
        # ⟨K∨, b_k⟩_F = Σ_j dual_j · G_{jk}
        pairing = sum(dual_vec[j] * G[j, k] for j in range(6))
        print(f"    ⟨K∨, {NF_NAMES[k]}⟩ = {pairing:>8.4f}  (should be {nf_vec[k]:>8.4f})")

    return dual_vec


# ── Compute NF for key particles ─────────────────────────────

# (a) Basis elements (already in NF)
print("\n" + "─" * 72)
print("  PART A: Basis elements")
print("─" * 72)

for idx, (name, desc) in enumerate([
    ("γ (photon)", "𝟏"),
    ("σ₀ (hor. pol.)", "σ₀"),
    ("σ₁ (vert. pol.)", "σ₁"),
    ("L₊ (gluon+)", "σ₀σ₁"),
    ("L₋ (gluon−)", "σ₁σ₀"),
    ("e⁻ (electron)", "σ₀σ₁σ₀"),
]):
    vec = [0.0] * 6
    vec[idx] = 1.0
    print_particle(name, desc, vec)

# (b) Mirror/inverse particles
print("\n" + "─" * 72)
print("  PART B: Mirror / inverse particles")
print("─" * 72)

# Down quark: σ₀⁻¹ = σ₀ − HA·𝟏
d_quark_raw = expand_inverse_word((-1,))  # σ₀⁻¹
d_quark_nf = reduce_nf(d_quark_raw)
d_quark_vec = to_nf_vector(d_quark_nf)
print_particle("𝔡 (down quark)", "σ₀⁻¹ = σ₀ − HA", d_quark_vec)

# Positron: σ₀⁻¹σ₁⁻¹σ₀⁻¹
eplus_raw = expand_inverse_word((-1, -2, -1))
eplus_nf = reduce_nf(eplus_raw)
eplus_vec = to_nf_vector(eplus_nf)
print_particle("e⁺ (positron)", "σ₀⁻¹σ₁⁻¹σ₀⁻¹", eplus_vec)

# L₊⁻¹ = (σ₀σ₁)⁻¹ = σ₁⁻¹σ₀⁻¹
lplus_inv_raw = expand_inverse_word((-2, -1))
lplus_inv_nf = reduce_nf(lplus_inv_raw)
lplus_inv_vec = to_nf_vector(lplus_inv_nf)
print_particle("L₊⁻¹ (antigluon+)", "σ₁⁻¹σ₀⁻¹", lplus_inv_vec)

# L₋⁻¹ = (σ₁σ₀)⁻¹ = σ₀⁻¹σ₁⁻¹
lminus_inv_raw = expand_inverse_word((-1, -2))
lminus_inv_nf = reduce_nf(lminus_inv_raw)
lminus_inv_vec = to_nf_vector(lminus_inv_nf)
print_particle("L₋⁻¹ (antigluon−)", "σ₀⁻¹σ₁⁻¹", lminus_inv_vec)

# (c) Colored photon γ_φ = 𝟏 + φσ₀ + φσ₁  (linear, φ = 0.0487)
print("\n" + "─" * 72)
print("  PART C: Colored photons")
print("─" * 72)

phi_lin = 0.0487
gamma_lin = [1.0, phi_lin, phi_lin, 0.0, 0.0, 0.0]
print_particle("γ_φ (linear, φ=0.049)", "𝟏 + φσ₀ + φσ₁", gamma_lin)

s_circ = 0.0978
gamma_circ1 = [1.0, s_circ, 0.0, 0.0, 0.0, 0.0]
gamma_circ2 = [1.0, 0.0, s_circ, 0.0, 0.0, 0.0]
print_particle("γ₁ (circular, s=0.098)", "𝟏 + sσ₀", gamma_circ1)
print_particle("γ₂ (circular, s=0.098)", "𝟏 + sσ₁", gamma_circ2)

# ══════════════════════════════════════════════════════════════
#  4. OPERATOR SELECTION via K∨
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  4. OPERATOR SELECTION: ⟨K∨, β(T_{m,n})⟩_F")
print("=" * 72)
print("  For each particle K, compute the Frobenius pairing of")
print("  K∨ with each knot operator β(T_{m,n}).")

KNOT_OPS = {
    "T_{1,0}": (),
    "T_{2,1}": (0,),
    "T_{2,2}": (0, 0),
    "T_{2,3}": (0, 1, 0),
    "T_{2,5}": (0, 1, 0, 1, 0),
}

particles = {
    "γ": [1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    "σ₀": [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
    "e⁻": [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
    "e⁺": eplus_vec,
    "𝔡": d_quark_vec,
}

for pname, pvec in particles.items():
    dual = frobenius_dual(pvec)
    print(f"\n  ── {pname} ──")

    hdr = f"    {'Operator':10s} | {'⟨K∨,β(T)⟩':>12s} | {'|⟨⟩|':>8s}"
    print(hdr)
    print("    " + "-" * (len(hdr) - 4))

    for op_name, op_word in KNOT_OPS.items():
        # NF of operator
        if op_word:
            op_terms = {op_word: 1.0}
        else:
            op_terms = {(): 1.0}
        op_nf = reduce_nf(op_terms)
        op_vec = to_nf_vector(op_nf)

        # Pairing: ⟨K∨, β(T)⟩_F = Σ_{i,j} dual_i · G_{ij} · op_j
        # = dual · G · op  (matrix multiplication)
        pairing = dual @ G @ np.array(op_vec)
        print(f"    {op_name:10s} | {pairing:>12.6f} | {abs(pairing):>8.6f}")


# ══════════════════════════════════════════════════════════════
#  5. PAIR INTERACTION: ⟨(K₁⊗K₂)∨, β(T)⟩_F
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  5. PAIR INTERACTION via dual")
print("     For incoming pair K₁,K₂: compute NF(K₁·K₂),")
print("     then its dual, then pair with each operator.")
print("=" * 72)

pairs = [
    ("γ⊗γ", (0,), (0,), "bare photon pair σ₀²"),
    ("γ₁⊗γ₂ (circ)", None, None, "circular polarized pair"),
    ("e⁻⊗e⁺", None, None, "electron-positron"),
    ("σ₀⊗σ₁", (0,), (1,), "orthogonal polarizations"),
]

# γ⊗γ = σ₀ · σ₀
gg_terms = hecke_mul({(0,): 1.0}, {(0,): 1.0})
gg_nf = reduce_nf(gg_terms)
gg_vec = to_nf_vector(gg_nf)
gg_dual = frobenius_dual(gg_vec)

print(f"\n  ── γ⊗γ (bare photon pair σ₀²) ──")
print(f"  NF(γγ) = {['%.4f' % v for v in gg_vec]}")
print(f"  (γγ)∨  = {['%.4f' % v for v in gg_dual]}")

hdr = f"    {'Operator':10s} | {'⟨(γγ)∨,T⟩':>12s}"
print(hdr)
for op_name, op_word in KNOT_OPS.items():
    op_terms = {op_word: 1.0} if op_word else {(): 1.0}
    op_nf = reduce_nf(op_terms)
    op_vec = to_nf_vector(op_nf)
    pairing = gg_dual @ G @ np.array(op_vec)
    print(f"    {op_name:10s} | {pairing:>12.6f}")

# σ₀⊗σ₁ = σ₀ · σ₁ = L₊ (orthogonal polarizations)
cross_terms = hecke_mul({(0,): 1.0}, {(1,): 1.0})
cross_nf = reduce_nf(cross_terms)
cross_vec = to_nf_vector(cross_nf)
cross_dual = frobenius_dual(cross_vec)

print(f"\n  ── σ₀⊗σ₁ (orthogonal polarizations → L₊) ──")
print(f"  NF(σ₀σ₁) = {['%.4f' % v for v in cross_vec]}")
print(f"  (σ₀σ₁)∨  = {['%.4f' % v for v in cross_dual]}")

hdr = f"    {'Operator':10s} | {'⟨L₊∨,T⟩':>12s}"
print(hdr)
for op_name, op_word in KNOT_OPS.items():
    op_terms = {op_word: 1.0} if op_word else {(): 1.0}
    op_nf = reduce_nf(op_terms)
    op_vec = to_nf_vector(op_nf)
    pairing = cross_dual @ G @ np.array(op_vec)
    print(f"    {op_name:10s} | {pairing:>12.6f}")

# e⁻⊗e⁺ = σ₀σ₁σ₀ · σ₀⁻¹σ₁⁻¹σ₀⁻¹
ee_terms = hecke_mul({(0, 1, 0): 1.0}, eplus_nf)
ee_nf = reduce_nf(ee_terms)
ee_vec = to_nf_vector(ee_nf)
ee_dual = frobenius_dual(ee_vec)

print(f"\n  ── e⁻⊗e⁺ (electron-positron annihilation) ──")
print(f"  NF(e⁻·e⁺) = {['%.4f' % v for v in ee_vec]}")
print(f"  (e⁻e⁺)∨   = {['%.4f' % v for v in ee_dual]}")

hdr = f"    {'Operator':10s} | {'⟨(e⁻e⁺)∨,T⟩':>12s}"
print(hdr)
for op_name, op_word in KNOT_OPS.items():
    op_terms = {op_word: 1.0} if op_word else {(): 1.0}
    op_nf = reduce_nf(op_terms)
    op_vec = to_nf_vector(op_nf)
    pairing = ee_dual @ G @ np.array(op_vec)
    print(f"    {op_name:10s} | {pairing:>12.6f}")


# ══════════════════════════════════════════════════════════════
#  WITNESS
# ══════════════════════════════════════════════════════════════

witness = {
    "name": "gram-matrix-dual",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "parameters": {"q0": q0, "HA": HA, "z": z},
    "markov_trace_basis": dict(zip(NF_NAMES, TR_M_BASIS)),
    "gram_matrix": G.tolist(),
    "gram_inverse": G_inv.tolist(),
    "gram_determinant": float(np.linalg.det(G)),
    "gram_eigenvalues": np.linalg.eigvals(G).real.tolist(),
    "particles": {
        "e_plus": {"nf": eplus_vec, "dual": frobenius_dual(eplus_vec).tolist()},
        "d_quark": {"nf": d_quark_vec, "dual": frobenius_dual(d_quark_vec).tolist()},
        "photon": {"nf": [1, 0, 0, 0, 0, 0], "dual": frobenius_dual([1, 0, 0, 0, 0, 0]).tolist()},
        "electron": {"nf": [0, 0, 0, 0, 0, 1], "dual": frobenius_dual([0, 0, 0, 0, 0, 1]).tolist()},
    },
}

from witness_base import WitnessBuilder  # noqa: E402

out_path = WitnessBuilder.wrap_legacy(
    "gram-matrix-dual", json.loads(json.dumps(witness, default=float)),
    script_path=__file__, engine="numpy",
).save()
print(f"\n  Witness written to {out_path.name}")


# ══════════════════════════════════════════════════════════════
#  HOMFLYPT SU(N) GRAM MATRIX (multi-channel extension)
# ══════════════════════════════════════════════════════════════
# The SU(2) Gram matrix above uses the Markov trace (∝ Jones).
# For SU(N>2), the HOMFLYPT engine provides multi-channel Gram
# entries via the quantum Schur function weights.
#
# Usage (when homflypt_engine is available):
#   from homflypt_engine import homflypt_gram_entry
#   G_su3[i][j] = homflypt_gram_entry(basis_braid_i, basis_braid_j,
#                                      n_strands=3, N=3, q=q0)
#
# Per prop:markov-trace-ratio-exact, the RATIOS between Gram
# entries are exact regardless of the Markov/Jones normalisation
# convention. The Gram matrix determinant, eigenvalues, and inverse
# are therefore correct up to a global scalar (C^{2·dim}) which
# cancels in the Frobenius dual and LP shadow prices.
#
# See rem:archimedean-image-table row 5 for the SU(N) family
# interpretation and row 9 for the LP duality structure.
