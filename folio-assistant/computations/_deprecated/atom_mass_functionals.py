#!/usr/bin/env python3
"""
Compare three mass functionals on derived atom NFs.

Given the NF element 𝒜(Z,N) = Σ c_w · w ∈ H_A(q), we test:

  F₁  NET SUM:      F₁(𝒜) = Σ c_w                (sum of all coefficients)
  F₂  L¹ NORM:      F₂(𝒜) = Σ |c_w|              (sum of absolute values)
  F₃  GRAM NORM:    F₃(𝒜) = √|𝒜 · G · 𝒜|        (Frobenius norm via Gram matrix)
  F₄  MARKOV TRACE: F₄(𝒜) = Σ c_w · tr_M(w)      (weighted sum, known to decay)

═══════════════════════════════════════════════════════════════

ORIGIN OF EACH FUNCTIONAL:

F₁ — NET SUM  Σ c_w
─────────────────────
The sum of all NF coefficients. In the H₃(q) basis {γ, σ₀, σ₁,
L₊, L₋, e⁻}, this is the coefficient of the "evaluate at the
identity" functional: the augmentation map ε: H_n(q) → ℝ that
sends every generator σᵢ to 1.

Origin: The augmentation map is the SYMMETRIC CHARACTER χ_sym
evaluated at the identity. Since σ ↦ q in the symmetric irrep,
the net = χ_sym(𝒜)/q^{crossing_count}... but more directly, the
net measures the TOTAL PROBABILITY AMPLITUDE of the knot-particle
state: how much of the identity channel survives after all
crossings. It's the closest analogue to "norm of the state."

Physically: net(𝔭) ≈ 0.999 (proton nearly closed), net(𝔫) ≈ 0.811
(neutron has deficit → drives beta decay). For atoms, net should
track total particle content.

F₂ — L¹ NORM  Σ |c_w|
──────────────────────
The sum of absolute values of all NF coefficients. This treats
each basis element as an independent "degree of freedom" and
measures the total algebraic complexity of the element.

Origin: The L¹ norm on the NF basis is the NATURAL COMPLEXITY
MEASURE of the Gröbner-Shirshov reduction. When a nucleus decays
(β⁻: n→p), the daughter has smaller L¹ norm because it has fewer
nn crossings (the most repulsive type, with d = -(q-q⁻¹)).
The difference ||𝒢_par||₁ - ||𝒢_dau||₁ = Δ_k is the NF reduction
cost used in the Gram-weighted Q-value formula.

Physically: ||𝒜||₁ measures the TOTAL CROSSING COMPLEXITY of the
atom. More crossings = more mass. Unlike tr_M, this doesn't suffer
from sign cancellations because all terms are positive.

F₃ — GRAM NORM  √|𝒜 · G · 𝒜|
──────────────────────────────
The Frobenius norm induced by the Gram matrix G_{ij} = tr_M(bᵢ·bⱼ).
The Gram matrix is the inner product on H_n(q) inherited from the
Markov trace: ⟨x, y⟩ = tr_M(x·y).

Origin: The Gram matrix encodes the REPRESENTATION THEORY of H_n(q)
via the Schur elements. Its eigenvalues correspond to the Wedderburn
decomposition: positive eigenvalues = symmetric/standard sectors,
negative eigenvalue = the nn-repulsive direction. The Frobenius norm
projects 𝒜 through all irreducible representations simultaneously.

Physically: ||𝒜||_F = √|𝒜·G·𝒜| measures the TOTAL REPRESENTATION
CONTENT of the atom — how much of the Hecke algebra the atom
"occupies." This is the norm used in the Gram-weighted Q-value
formula for β decay.

F₄ — MARKOV TRACE  Σ c_w · z^{ℓ(w)}
─────────────────────────────────────
The Jones-Markov trace: each word w of length ℓ contributes z^ℓ.
This is the knot invariant — it computes the Jones polynomial of
the closure of the braid.

Origin: The Markov trace is the UNIQUE trace on H_n(q) satisfying
the Markov property: tr(x·σₙ) = z·tr(x). It's the categorical
trace through the fibre functor, giving the topological mass
𝔪 = Vol(K)/ℏ_q² for knots.

Problem: For COMPOSITE objects (multi-nucleon atoms), the trace
has sign cancellations that drive it to zero. This is because the
Markov trace computes the Jones polynomial of the CLOSURE, which
for composite braids becomes trivial. The mass of a composite
object ≠ Jones polynomial of its closure.

═══════════════════════════════════════════════════════════════

Usage:
    python3 folio-assistant/computations/atom_mass_functionals.py
"""

import math
import sys
import time
import numpy as np
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi0, HA as HA_val
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from witness_base import WitnessBuilder

# Import the derived engine
from atom_mass_derived import (
    HA, z, B3_NF, PROTON_NF, NEUTRON_NF,
    build_nucleon, build_atom,
    hecke_mul, reduce_nf, expand_inverse,
    markov_trace_general, nf_net,
    NF_BASIS_3, NF_NAMES_3, TR_M_3,
    nuclear_crossing,
)


# ══════════════════════════════════════════════════════════════
# §1  MASS FUNCTIONALS
# ══════════════════════════════════════════════════════════════

def F_net(terms):
    """F₁: Net sum of all NF coefficients."""
    return sum(terms.values())


def F_L1(terms):
    """F₂: L¹ norm — sum of absolute values."""
    return sum(abs(c) for c in terms.values())


def build_gram_matrix(nf_terms):
    """Build the Gram matrix G on the NF subspace of H_n(q).

    G_{ij} = tr_M(bᵢ · bⱼ) where {bᵢ} are the NF basis elements
    that appear in the element.

    For H₃ (6-element basis): G is 6×6.
    For larger H_n: G is |NF terms| × |NF terms|.
    """
    words = sorted(nf_terms.keys(), key=lambda w: (len(w), w))
    n = len(words)
    G = np.zeros((n, n))
    for i, wi in enumerate(words):
        for j, wj in enumerate(words):
            # tr_M(bᵢ · bⱼ) — multiply and take Markov trace
            prod = hecke_mul({wi: 1.0}, {wj: 1.0})
            prod_nf = reduce_nf(prod)
            G[i, j] = markov_trace_general(prod_nf)
    return G, words


def F_gram(terms):
    """F₃: Gram/Frobenius norm √|𝒜 · G · 𝒜|.

    Builds the Gram matrix on the NF subspace and computes
    the quadratic form.
    """
    if len(terms) == 0:
        return 0.0

    G, words = build_gram_matrix(terms)
    # Coefficient vector
    v = np.array([terms.get(w, 0.0) for w in words])
    # Quadratic form: v^T G v
    quad = v @ G @ v
    return math.sqrt(abs(quad))


def F_trM(terms):
    """F₄: Markov trace (known to decay for composites)."""
    return markov_trace_general(terms)


# ══════════════════════════════════════════════════════════════
# §2  COMPUTE AND COMPARE
# ══════════════════════════════════════════════════════════════

ELEMENTS = {
    1:  ("Hydrogen",   "¹H",   1, 0),
    2:  ("Helium",     "⁴He",  2, 2),
    3:  ("Lithium",    "⁷Li",  3, 4),
    4:  ("Beryllium",  "⁹Be",  4, 5),
    5:  ("Boron",      "¹¹B",  5, 6),
    6:  ("Carbon",     "¹²C",  6, 6),
    7:  ("Nitrogen",   "¹⁴N",  7, 7),
    8:  ("Oxygen",     "¹⁶O",  8, 8),
}

AME2020_MASS = {
    (1, 0): 938.783,     (2, 2): 3728.401,   (3, 4): 6535.367,
    (4, 5): 8394.794,    (5, 6): 10255.103,  (6, 6): 11177.930,
    (7, 7): 13043.781,   (8, 8): 14899.169,
}


def main():
    print("=" * 120)
    print("MASS FUNCTIONAL COMPARISON — FOUR CANDIDATES ON DERIVED ATOM NFs")
    print("=" * 120)
    print()
    print("FUNCTIONALS:")
    print("  F₁ NET:   Σ c_w               — augmentation map (symmetric character at identity)")
    print("  F₂ L¹:    Σ |c_w|             — algebraic complexity (crossing count)")
    print("  F₃ GRAM:  √|𝒜·G·𝒜|           — Frobenius norm (representation content)")
    print("  F₄ tr_M:  Σ c_w·z^ℓ(w)       — Markov trace (Jones polynomial, known to decay)")
    print()

    # First: compute functionals for proton and neutron
    print("─" * 120)
    print("NUCLEON CALIBRATION:")
    for name, nf in [("Proton", PROTON_NF), ("Neutron", NEUTRON_NF)]:
        f1 = F_net(nf)
        f2 = F_L1(nf)
        f3 = F_gram(nf)
        f4 = F_trM(nf)
        print(f"  {name:>8}: F₁(net)={f1:+.6f}  F₂(L¹)={f2:.6f}  F₃(Gram)={f3:.6f}  F₄(tr_M)={f4:.6f}")

    # Calibrate each functional to m_p
    p_net = F_net(PROTON_NF)
    p_L1 = F_L1(PROTON_NF)
    p_gram = F_gram(PROTON_NF)
    p_trM = F_trM(PROTON_NF)

    E0_net = M_P_MEV / p_net
    E0_L1 = M_P_MEV / p_L1
    E0_gram = M_P_MEV / p_gram
    E0_trM = M_P_MEV / p_trM

    n_net = F_net(NEUTRON_NF)
    n_L1 = F_L1(NEUTRON_NF)
    n_gram = F_gram(NEUTRON_NF)
    n_trM = F_trM(NEUTRON_NF)

    print()
    print("  CALIBRATION (E₀ = m_p / F(proton)):")
    print(f"    E₀(net)  = {E0_net:.3f} MeV")
    print(f"    E₀(L¹)   = {E0_L1:.3f} MeV")
    print(f"    E₀(Gram) = {E0_gram:.3f} MeV")
    print(f"    E₀(tr_M) = {E0_trM:.3f} MeV")
    print()
    print("  DERIVED NEUTRON MASS (F(neutron) × E₀):")
    print(f"    m_n(net)  = {n_net * E0_net:.3f} MeV  (CODATA: {M_N_MEV:.3f}, Δ={n_net*E0_net - M_N_MEV:+.3f})")
    print(f"    m_n(L¹)   = {n_L1 * E0_L1:.3f} MeV  (CODATA: {M_N_MEV:.3f}, Δ={n_L1*E0_L1 - M_N_MEV:+.3f})")
    print(f"    m_n(Gram) = {n_gram * E0_gram:.3f} MeV  (CODATA: {M_N_MEV:.3f}, Δ={n_gram*E0_gram - M_N_MEV:+.3f})")
    print(f"    m_n(tr_M) = {n_trM * E0_trM:.3f} MeV  (CODATA: {M_N_MEV:.3f}, Δ={n_trM*E0_trM - M_N_MEV:+.3f})")
    print()

    # Now compute for each atom
    print("=" * 120)
    print("ATOM-BY-ATOM RESULTS")
    print("=" * 120)

    rows = []
    for Z in sorted(ELEMENTS.keys()):
        name, label, z_check, N = ELEMENTS[Z]
        A = Z + N
        M_obs = AME2020_MASS.get((Z, N), 0.0)
        t0 = time.time()

        nucleus_nf, atom_nf, meta = build_atom(Z, N)

        f1 = F_net(atom_nf)
        f2 = F_L1(atom_nf)
        # Gram is expensive for large NFs — skip if > 50 terms
        if len(atom_nf) <= 50:
            f3 = F_gram(atom_nf)
        else:
            f3 = float('nan')
        f4 = F_trM(atom_nf)

        M_net = f1 * E0_net
        M_L1 = f2 * E0_L1
        M_gram = f3 * E0_gram if not math.isnan(f3) else float('nan')
        M_trM = f4 * E0_trM

        elapsed = time.time() - t0

        row = {
            'label': label, 'name': name, 'Z': Z, 'N': N, 'A': A,
            'terms': len(atom_nf),
            'F_net': f1, 'F_L1': f2, 'F_gram': f3, 'F_trM': f4,
            'M_net': M_net, 'M_L1': M_L1, 'M_gram': M_gram, 'M_trM': M_trM,
            'M_obs': M_obs, 'elapsed': elapsed,
        }
        rows.append(row)

        d_net = M_net - M_obs
        d_L1 = M_L1 - M_obs
        d_gram = M_gram - M_obs if not math.isnan(M_gram) else float('nan')
        d_trM = M_trM - M_obs

        print(f"{'─' * 120}")
        print(f"  {label} ({name}): Z={Z}, N={N}, A={A}, NF terms={len(atom_nf)}, time={elapsed:.1f}s")
        print(f"  {'Functional':>12} | {'Value':>14} | {'M_pred (MeV)':>14} | {'M_obs':>14} | {'Δ MeV':>10} | {'Δ%':>8}")
        print(f"  {'─'*12}-+-{'─'*14}-+-{'─'*14}-+-{'─'*14}-+-{'─'*10}-+-{'─'*8}")
        print(f"  {'F₁ NET':>12} | {f1:14.6f} | {M_net:14.3f} | {M_obs:14.3f} | {d_net:+10.1f} | {d_net/M_obs*100 if M_obs else 0:+7.2f}%")
        print(f"  {'F₂ L¹':>12} | {f2:14.6f} | {M_L1:14.3f} | {M_obs:14.3f} | {d_L1:+10.1f} | {d_L1/M_obs*100 if M_obs else 0:+7.2f}%")
        if not math.isnan(f3):
            print(f"  {'F₃ GRAM':>12} | {f3:14.6f} | {M_gram:14.3f} | {M_obs:14.3f} | {d_gram:+10.1f} | {d_gram/M_obs*100 if M_obs else 0:+7.2f}%")
        else:
            print(f"  {'F₃ GRAM':>12} | {'(skipped)':>14} | {'—':>14} | {M_obs:14.3f} | {'—':>10} | {'—':>8}")
        print(f"  {'F₄ tr_M':>12} | {f4:14.6e} | {M_trM:14.3f} | {M_obs:14.3f} | {d_trM:+10.1f} | {d_trM/M_obs*100 if M_obs else 0:+7.2f}%")
        print()

    # Summary table
    print("=" * 120)
    print("SUMMARY: WHICH FUNCTIONAL SCALES WITH MASS?")
    print("=" * 120)
    print(f"{'Atom':>5} | {'A':>3} | {'terms':>6} | {'F₁ net':>10} | {'F₂ L¹':>10} | {'F₃ Gram':>10} | {'F₄ tr_M':>12} | {'M_obs':>10}")
    print("─" * 120)
    for r in rows:
        gram_str = f"{r['F_gram']:10.4f}" if not math.isnan(r['F_gram']) else '     —    '
        print(f"{r['label']:>5} | {r['A']:3d} | {r['terms']:6d} | {r['F_net']:10.4f} | "
              f"{r['F_L1']:10.4f} | {gram_str} | {r['F_trM']:+12.4e} | {r['M_obs']:10.1f}")

    print()
    print("SCALING CHECK: F(atom) / F(proton) vs M(atom) / m_p")
    print("─" * 120)
    print(f"{'Atom':>5} | {'M/m_p':>8} | {'net/net_p':>10} | {'L¹/L¹_p':>10} | {'Gram/G_p':>10} | {'trM/trM_p':>12}")
    print("─" * 120)
    for r in rows:
        ratio_m = r['M_obs'] / M_P_MEV
        ratio_net = r['F_net'] / p_net
        ratio_L1 = r['F_L1'] / p_L1
        ratio_gram = r['F_gram'] / p_gram if not math.isnan(r['F_gram']) else float('nan')
        ratio_trM = r['F_trM'] / p_trM
        gram_str = f"{ratio_gram:10.4f}" if not math.isnan(ratio_gram) else '     —    '
        print(f"{r['label']:>5} | {ratio_m:8.3f} | {ratio_net:10.4f} | "
              f"{ratio_L1:10.4f} | {gram_str} | {ratio_trM:+12.4e}")

    # Witness
    w = WitnessBuilder("atom-mass-functionals", engine="python")
    w.set_description(
        "Comparison of 4 mass functionals (net, L¹, Gram, tr_M) on "
        "derived atom NFs Z=1-8. Tests which functional scales with mass."
    )
    w.add_parameter("q0", str(q0))
    w.add_parameter("proton_values", {
        "net": p_net, "L1": p_L1, "gram": p_gram, "trM": p_trM,
    })
    w.add_data("results", rows)
    w.save()


if __name__ == "__main__":
    main()
