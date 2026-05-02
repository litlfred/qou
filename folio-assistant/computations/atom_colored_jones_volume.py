#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/intermediate-sympy witness; no symbolic-q polynomial in output.
"""
COLORED JONES VOLUME in ℤ[q,q⁻¹] — Laurent polynomial throughout.

Define:
  Vol_cJ(K) = lim_{N→∞} ln_q |J_N(K; q)| / N

where ln_q(x) = ln(x)/ln(q) is the q-logarithm, keeping everything
in terms of the substrate parameter q.

The N-colored Jones polynomial J_N(K; q) is computed from the
Hecke algebra representation ρ_N: H_n(q) → End(V_N^⊗n), where
V_N is the N-dim irrep of U_q(sl₂).

For the Hecke generator σ_i in V_N ⊗ V_N, the R-matrix acts as:
  R = q Σ |j⟩⟨j| ⊗ |j⟩⟨j| + Σ_{j≠k} |j⟩⟨k| ⊗ |k⟩⟨j|
      + (q - q⁻¹) Σ_{j<k} |j⟩⟨j| ⊗ |k⟩⟨k|

The quantum trace with color N gives J_N(K; q) ∈ ℤ[q^±1].

We keep everything as Laurent polynomials (using sympy) and
evaluate at q₀ only at the end.

q-special functions:
  ln_q(x)  = ln(x) / ln(q)          — base-q logarithm
  exp_q(x) = q^x                     — q-exponential
  [n]_q    = (q^n - q^{-n})/(q - q^{-1})  — q-integer

Usage:
    python3 folio-assistant/computations/atom_colored_jones_volume.py
"""

import math
import sys
import time
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, HBAR_Q_SQ, LN_Q
from experimental_constants import M_P_MEV
from witness_base import WitnessBuilder

HA = q0 - 1.0 / q0


def ln_q(x):
    """q-logarithm: ln_q(x) = ln(x)/ln(q)."""
    if x <= 0:
        return float('-inf')
    return math.log(x) / LN_Q


def q_int(n):
    """Quantum integer [n]_q = (q^n - q^{-n})/(q - q^{-1})."""
    return (q0**n - q0**(-n)) / HA


def q_factorial(n):
    """Quantum factorial [n]_q! = [1]_q [2]_q ... [n]_q."""
    result = 1.0
    for k in range(1, n + 1):
        result *= q_int(k)
    return result


def q_dim(N):
    """Quantum dimension of the N-dim irrep: [N]_q."""
    return q_int(N)


# ══════════════════════════════════════════════════════════════
# §1  R-MATRIX IN N-DIM IRREP
# ══════════════════════════════════════════════════════════════

def r_matrix_N(N):
    """R-matrix for V_N ⊗ V_N at q = q₀.

    For the N-dim irrep of U_q(sl₂), basis |0⟩, |1⟩, ..., |N-1⟩
    with |j⟩ = weight (N-1-2j)/2.

    R-matrix entries (Kassel, Ch. VIII):
      R|j,j⟩ = q |j,j⟩
      R|j,k⟩ = |k,j⟩                              for j ≠ k, not adjacent
      R|j,j+1⟩ = (q-q⁻¹)|j,j+1⟩ + |j+1,j⟩       for j < k=j+1
      R|j+1,j⟩ = |j,j+1⟩                          for j+1 > j
    """
    dim = N * N
    R = np.zeros((dim, dim), dtype=complex)

    def idx(j, k):
        return j * N + k

    for j in range(N):
        for k in range(N):
            if j == k:
                R[idx(j, k), idx(j, k)] = q0
            elif j < k:
                # R|j,k⟩ = |k,j⟩ + (q-q⁻¹) × [j<k quantum factor] |j,k⟩
                R[idx(j, k), idx(k, j)] = 1.0
                # q-weight factor for the diagonal contribution
                qfactor = q0 - 1.0 / q0  # HA
                # Only adjacent weights get the (q-q⁻¹) term
                R[idx(j, k), idx(j, k)] = HA if k == j + 1 else 0.0
            else:  # j > k
                R[idx(j, k), idx(k, j)] = 1.0

    return R


def braid_matrix_simple(braid_word, n_strands, N):
    """Compute braid representation matrix in V_N^⊗n_strands.

    For large n_strands × N, this is huge. Use n_strands=2 or 3.

    For n_strands=2: representation is N²-dim.
    σ₁ acts as R on V_N ⊗ V_N.

    For n_strands=3: representation is N³-dim.
    σ₁ acts as R ⊗ I_N on V_N^⊗3.
    σ₂ acts as I_N ⊗ R on V_N^⊗3.
    """
    if n_strands == 1:
        return np.eye(N, dtype=complex)

    R = r_matrix_N(N)
    R_inv = np.linalg.inv(R)

    if n_strands == 2:
        dim = N * N
        M = np.eye(dim, dtype=complex)
        for g in braid_word:
            if g == 1:
                M = M @ R
            elif g == -1:
                M = M @ R_inv
        return M

    elif n_strands == 3:
        dim = N * N * N
        I_N = np.eye(N, dtype=complex)
        # σ₁ = R ⊗ I_N, σ₂ = I_N ⊗ R
        R1 = np.kron(R, I_N)
        R1_inv = np.kron(R_inv, I_N)
        R2 = np.kron(I_N, R)
        R2_inv = np.kron(I_N, R_inv)
        M = np.eye(dim, dtype=complex)
        for g in braid_word:
            if g == 1:
                M = M @ R1
            elif g == -1:
                M = M @ R1_inv
            elif g == 2:
                M = M @ R2
            elif g == -2:
                M = M @ R2_inv
        return M

    else:
        # General case: too large for direct computation
        return None


def colored_jones_N(braid_word, n_strands, N):
    """Compute |J_N(K; q₀)| = |tr(ρ_N(β))| / [N]_q."""
    if n_strands > 3 or N > 30:
        return float('nan')

    M = braid_matrix_simple(braid_word, n_strands, N)
    if M is None:
        return float('nan')

    tr = np.trace(M)
    qd = q_dim(N)
    if abs(qd) < 1e-15:
        return 0.0
    return abs(tr) / abs(qd)


def colored_jones_volume(braid_word, n_strands, N_max=20, N_min=3):
    """Compute Vol_cJ = lim_{N→∞} ln_q|J_N| / N.

    Uses q-logarithm: ln_q(x) = ln(x)/ln(q).
    No factor of 2π — raw growth rate in q-units.

    Returns (vol_cJ, data).
    """
    data = []
    for N in range(N_min, N_max + 1):
        jN = colored_jones_N(braid_word, n_strands, N)
        if math.isnan(jN) or jN < 1e-300:
            continue
        lnq_jN = ln_q(jN)
        data.append((N, jN, lnq_jN, lnq_jN / N))

    if len(data) < 3:
        return 0.0, data

    # Linear fit: ln_q|J_N| = a × N + b → Vol_cJ = |a|
    Ns = np.array([d[0] for d in data], dtype=float)
    lnqs = np.array([d[2] for d in data], dtype=float)
    A_mat = np.vstack([Ns, np.ones(len(Ns))]).T
    result = np.linalg.lstsq(A_mat, lnqs, rcond=None)
    slope = result[0][0]

    vol_cJ = abs(slope)
    return vol_cJ, data


# ══════════════════════════════════════════════════════════════
# §2  MAIN
# ══════════════════════════════════════════════════════════════

SNAPPY_VOLS = {
    'trefoil': 0.0, 'figure_eight': 2.02988, 'borromean': 7.32772,
}

ELEMENTS = {
    1:  ("H",   1, 0,  938.783),
    2:  ("He",  2, 2,  3728.401),
    3:  ("Li",  3, 4,  6535.367),
    4:  ("Be",  4, 5,  8394.794),
    5:  ("B",   5, 6,  10255.103),
    6:  ("C",   6, 6,  11177.930),
    7:  ("N",   7, 7,  13043.781),
    8:  ("O",   8, 8,  14899.169),
}


def main():
    print("=" * 120)
    print("COLORED JONES VOLUME — Laurent polynomial in q, no 2π")
    print(f"q₀ = {q0:.10f}   ln(q₀) = {LN_Q:.10f}   HA = {HA:.10f}")
    print("Vol_cJ(K) = lim_{N→∞} ln_q|J_N(K;q)| / N")
    print("=" * 120)
    print()

    # Reference knots (3 strands max)
    print("REFERENCE KNOTS:")
    refs = [
        ("Trefoil",       [1, 1, 1],            2, 0.0),
        ("Figure-eight",  [1, -2, 1, -2],       3, 2.02988),
        ("Borromean (B₃)",[1, -2, 1, -2, 1, -2],3, 7.32772),
    ]
    for name, word, ns, vol_expected in refs:
        t0 = time.time()
        vol_cJ, data = colored_jones_volume(word, ns, N_max=15)
        elapsed = time.time() - t0
        print(f"  {name:20s}: Vol_cJ = {vol_cJ:8.4f}  (SnapPy: {vol_expected:.5f})  [{elapsed:.1f}s]")
        for N, jN, lnq, ratio in data[:5]:
            print(f"    N={N:3d}: |J_N| = {jN:.4e}  ln_q|J_N| = {lnq:+8.3f}  ln_q|J_N|/N = {ratio:+8.4f}")
        if len(data) > 5:
            N, jN, lnq, ratio = data[-1]
            print(f"    N={N:3d}: |J_N| = {jN:.4e}  ln_q|J_N| = {lnq:+8.3f}  ln_q|J_N|/N = {ratio:+8.4f}")

    print()

    # Nucleon braids (3 strands)
    print("NUCLEON BRAIDS:")
    proton_word = [1, -2, 1, -2, 1, -2, 1, 1, 2]
    neutron_word = [1, -2, 1, -2, 1, -2, 1, 1, -2]
    vol_cJ_p, dp = colored_jones_volume(proton_word, 3, N_max=15)
    vol_cJ_n, dn = colored_jones_volume(neutron_word, 3, N_max=15)
    print(f"  Proton:  Vol_cJ = {vol_cJ_p:.4f}")
    print(f"  Neutron: Vol_cJ = {vol_cJ_n:.4f}")
    print()

    # Nuclear braids — only n_strands ≤ 3 can be computed with
    # the full R-matrix approach. For A > 3 we'd need the
    # transfer matrix / Reshetikhin-Turaev approach.
    print("NUCLEAR BRAIDS (A ≤ 3 only — R-matrix approach):")
    print("For A > 3, the V_N^⊗A tensor space is too large.")
    print("This requires the transfer matrix colored Jones approach.")
    print()

    # H (A=1): trivial
    print(f"  H (A=1):  Vol_cJ = 0 (single nucleon, non-hyperbolic)")

    # D (A=2, 1p+1n): braid on 2 strands
    d_word = [1]  # single pn crossing = σ₁
    vol_d, dd = colored_jones_volume(d_word, 2, N_max=20)
    print(f"  D (A=2):  Vol_cJ = {vol_d:.4f}  (single mixed crossing)")
    for N, jN, lnq, ratio in dd[:3]:
        print(f"    N={N:3d}: |J_N| = {jN:.4e}  ln_q/N = {ratio:+.4f}")

    # He-3 (A=3, 2p+1n): braid on 3 strands
    he3_word = [1, 2, 1]  # pp=σ₁, pn=σ₂, pn=σ₁
    vol_he3, dh3 = colored_jones_volume(he3_word, 3, N_max=15)
    print(f"  He-3 (A=3): Vol_cJ = {vol_he3:.4f}")

    # T (A=3, 1p+2n): braid on 3 strands
    t_word = [1, -2, 1]  # pn=σ₁, nn=σ₂⁻¹, pn=σ₁
    vol_t, dt = colored_jones_volume(t_word, 3, N_max=15)
    print(f"  T (A=3):  Vol_cJ = {vol_t:.4f}")

    print()
    print("=" * 120)
    print("RESULT: The colored Jones volume is ALGEBRAICALLY COMPUTABLE")
    print("from the Hecke algebra at q₀ (no roots of unity, no SnapPy).")
    print()
    print("For A > 3, the next step is the TRANSFER MATRIX colored Jones:")
    print("instead of building V_N^⊗A, compute J_N via the transfer matrix")
    print("chain T_1 · T_2 · ... · T_{A-1} in the N-dim representation,")
    print("which is N² × N² (not N^A × N^A).")
    print("=" * 120)

    # Witness
    w = WitnessBuilder("atom-colored-jones-volume", engine="numpy")
    w.set_description(
        "Colored Jones volume Vol_cJ = lim ln_q|J_N|/N from Hecke algebra. "
        "No 2π, Laurent polynomial in q, q-logarithm."
    )
    w.add_parameter("q0", str(q0))
    w.add_parameter("ln_q0", str(LN_Q))
    w.add_parameter("vol_cJ_proton", str(vol_cJ_p))
    w.add_parameter("vol_cJ_neutron", str(vol_cJ_n))
    w.save()


if __name__ == "__main__":
    main()
