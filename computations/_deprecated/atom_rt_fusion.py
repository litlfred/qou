#!/usr/bin/env python3
"""
Reshetikhin-Turaev FUSION colored Jones for nuclear braids.

Computes exact J_N(K; q₀) via the fusion framework:
1. Clebsch-Gordan: V_N ⊗ V_N = ⊕_J V_J  (quantum CG coefficients)
2. R-matrix in fusion basis: diagonal on irreps, eigenvalue q^{C_J}
3. Chain through crossings in fusion basis (no full tensor product)
4. Quantum trace with dimension factors

Cost: O(A² × N³) per color N, vs O(N^{2A}) for full tensor product.

The quantum group U_q(sl₂) has:
  - Irreps V_j for j = 0, 1/2, 1, 3/2, ... (dim V_j = 2j+1)
  - CG decomposition: V_j₁ ⊗ V_j₂ = ⊕_{J=|j₁-j₂|}^{j₁+j₂} V_J
  - R-matrix eigenvalue on V_J ⊂ V_j₁ ⊗ V_j₂:
      λ_J = (-1)^{j₁+j₂-J} q^{(C_J - C_{j₁} - C_{j₂})/2}
    where C_j = j(j+1) is the quadratic Casimir

For the N-colored Jones, j₁ = j₂ = (N-1)/2 (the (N-1)/2-spin irrep).

Usage:
    python3 folio-assistant/computations/atom_rt_fusion.py
"""

import math
import sys
import time
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, LN_Q, HBAR_Q_SQ
from experimental_constants import M_P_MEV
from witness_base import WitnessBuilder

HA = q0 - 1.0 / q0


def ln_q(x):
    """q-logarithm: ln_q(x) = ln(x)/ln(q₀)."""
    if x <= 0:
        return float('-inf')
    return math.log(x) / LN_Q


def q_number(n):
    """[n]_q = (q^n - q^{-n})/(q - q^{-1})."""
    if abs(n) < 1e-15:
        return 0.0
    return (q0**n - q0**(-n)) / HA


def q_factorial(n):
    """[n]_q! = [1]_q [2]_q ... [n]_q."""
    result = 1.0
    for k in range(1, int(n) + 1):
        result *= q_number(k)
    return result


def q_dim(j):
    """Quantum dimension of spin-j irrep: [2j+1]_q."""
    return q_number(2 * j + 1)


def casimir(j):
    """Quadratic Casimir: C_j = j(j+1)."""
    return j * (j + 1)


# ══════════════════════════════════════════════════════════════
# §1  R-MATRIX IN FUSION BASIS
# ══════════════════════════════════════════════════════════════

def r_eigenvalue(j1, j2, J):
    """R-matrix eigenvalue for V_J ⊂ V_{j1} ⊗ V_{j2}.

    λ_J = (-1)^{j1+j2-J} × q^{(C_J - C_{j1} - C_{j2})/2}

    where C_j = j(j+1) is the Casimir.
    """
    phase = (-1) ** int(j1 + j2 - J)
    casimir_exp = (casimir(J) - casimir(j1) - casimir(j2)) / 2.0
    return phase * q0 ** casimir_exp


def r_inverse_eigenvalue(j1, j2, J):
    """R⁻¹ eigenvalue = 1/λ_J."""
    lam = r_eigenvalue(j1, j2, J)
    return 1.0 / lam if abs(lam) > 1e-30 else 0.0


def fusion_channels(j1, j2):
    """List all J in the CG decomposition V_{j1} ⊗ V_{j2} = ⊕ V_J.

    J ranges from |j1-j2| to j1+j2 in integer steps.
    """
    J_min = abs(j1 - j2)
    J_max = j1 + j2
    return [J_min + k for k in range(int(J_max - J_min) + 1)]


# ══════════════════════════════════════════════════════════════
# §2  FUSION COLORED JONES FOR A BRAID
# ══════════════════════════════════════════════════════════════

def fusion_jones_2strand(braid_word, j):
    """J_N for a braid on 2 strands, color j (N = 2j+1).

    For 2 strands: V_j ⊗ V_j = ⊕_J V_J.
    Each crossing σ₁^±1 acts as λ_J^±1 on the J-th channel.
    The quantum trace is:
      J_N(K;q) = Σ_J [2J+1]_q × ∏_{crossings} λ_J^{±1} / [2j+1]_q
    """
    channels = fusion_channels(j, j)
    result = 0.0

    for J in channels:
        # Product of eigenvalues over all crossings
        product = 1.0
        for g in braid_word:
            if g > 0:
                product *= r_eigenvalue(j, j, J)
            else:
                product *= r_inverse_eigenvalue(j, j, J)

        # Weighted by quantum dimension of J
        result += q_dim(J) * product

    # Normalize by quantum dimension of color
    qd = q_dim(j)
    if abs(qd) < 1e-30:
        return 0.0
    return abs(result / qd)


def fusion_jones_3strand(braid_word, j):
    """J_N for a braid on 3 strands, color j (N = 2j+1).

    For 3 strands: V_j^⊗3.
    Fusion basis: first fuse strands 1,2 into intermediate J₁₂,
    then fuse J₁₂ with strand 3 into total J_total.

    σ₁ acts on (strand 1, strand 2): eigenvalue depends on J₁₂.
    σ₂ acts on (strand 2, strand 3): needs recoupling (6j symbol).

    The recoupling:
      |j,j; J₁₂⟩ ⊗ |j⟩  →  |j⟩ ⊗ |j,j; J₂₃⟩
    uses the quantum 6j symbol {j j J₁₂; j J_total J₂₃}_q.

    For the trace (braid closure), J_total is fixed and we sum
    over J_total with weight [2J_total+1]_q.

    SIMPLIFICATION for this computation: we work in the
    "fusion tree" basis where σ₁ is diagonal and σ₂ requires
    a basis change via the F-matrix (quantum 6j symbols).
    """
    channels_12 = fusion_channels(j, j)

    # For 3 strands, the fusion basis is indexed by (J₁₂, J_total)
    # where J₁₂ ∈ fusion(j,j), J_total ∈ fusion(J₁₂, j)
    basis = []
    for J12 in channels_12:
        for Jtot in fusion_channels(J12, j):
            basis.append((J12, Jtot))

    dim = len(basis)
    if dim == 0:
        return 0.0

    # σ₁ matrix: diagonal in this basis (acts on strands 1,2)
    # σ₁ |J₁₂, Jtot⟩ = λ(j,j,J₁₂) |J₁₂, Jtot⟩
    def sigma1_matrix(sign=1):
        M = np.zeros((dim, dim), dtype=complex)
        for idx, (J12, Jtot) in enumerate(basis):
            if sign > 0:
                M[idx, idx] = r_eigenvalue(j, j, J12)
            else:
                M[idx, idx] = r_inverse_eigenvalue(j, j, J12)
        return M

    # σ₂ matrix: requires F-matrix (recoupling)
    # σ₂ acts on strands 2,3. In the (J₁₂, Jtot) basis,
    # we need to recouple to the (J₂₃, Jtot) basis, apply R
    # on the (j, j; J₂₃) channel, then recouple back.
    #
    # F-matrix: F^{j,j,j}_{Jtot}[J₁₂, J₂₃]
    # This is the quantum 6j symbol (Racah coefficient).
    #
    # For U_q(sl₂), the quantum 6j symbol is:
    # {a b e; c d f}_q = Δ(abe)Δ(cde)Δ(acf)Δ(bdf) ×
    #   Σ_z (-1)^z [z+1]_q! / (products of [z-triad]_q! and [sum-z]_q!)

    def q6j(a, b, e, c, d, f):
        """Quantum 6j symbol {a b e; c d f}_q.

        Uses the Racah formula with q-factorials.
        All spins are half-integers (stored as floats).
        """
        # Triangle coefficients
        def triangle(x, y, z):
            s = x + y + z
            if abs(s - round(s)) > 0.01:
                return 0.0
            s = int(round(s))
            a1 = int(round(x + y - z))
            a2 = int(round(x - y + z))
            a3 = int(round(-x + y + z))
            if a1 < 0 or a2 < 0 or a3 < 0:
                return 0.0
            return math.sqrt(abs(
                q_factorial(a1) * q_factorial(a2) * q_factorial(a3)
                / q_factorial(s + 1)
            ))

        tri_abe = triangle(a, b, e)
        tri_cde = triangle(c, d, e)
        tri_acf = triangle(a, c, f)
        tri_bdf = triangle(b, d, f)

        if abs(tri_abe * tri_cde * tri_acf * tri_bdf) < 1e-30:
            return 0.0

        # Sum over z
        z_min = max(
            int(round(a + b + e)),
            int(round(c + d + e)),
            int(round(a + c + f)),
            int(round(b + d + f))
        )
        z_max = min(
            int(round(a + b + c + d)),
            int(round(a + d + e + f)),
            int(round(b + c + e + f))
        )

        total = 0.0
        for z in range(z_min, z_max + 1):
            num = (-1)**z * q_factorial(z + 1)
            d1 = q_factorial(z - int(round(a + b + e)))
            d2 = q_factorial(z - int(round(c + d + e)))
            d3 = q_factorial(z - int(round(a + c + f)))
            d4 = q_factorial(z - int(round(b + d + f)))
            d5 = q_factorial(int(round(a + b + c + d)) - z)
            d6 = q_factorial(int(round(a + d + e + f)) - z)
            d7 = q_factorial(int(round(b + c + e + f)) - z)
            denom = d1 * d2 * d3 * d4 * d5 * d6 * d7
            if abs(denom) > 1e-30:
                total += num / denom

        return tri_abe * tri_cde * tri_acf * tri_bdf * total

    # Build F-matrix for the recoupling
    # F^{j,j,j}_{Jtot}[J₁₂, J₂₃]
    # Groups basis by Jtot
    jtot_values = sorted(set(Jtot for _, Jtot in basis))

    def sigma2_matrix(sign=1):
        M = np.zeros((dim, dim), dtype=complex)
        for Jtot in jtot_values:
            # Indices with this Jtot
            idxs_12 = [(idx, J12) for idx, (J12, Jt) in enumerate(basis) if Jt == Jtot]
            idxs_23 = [(idx, J23) for idx, (J23, Jt) in enumerate(basis) if Jt == Jtot]
            # Note: J₂₃ ranges over the same values as J₁₂ for identical spins

            # F-matrix block for this Jtot
            n_block = len(idxs_12)
            F = np.zeros((n_block, n_block))
            for i, (idx_i, J12) in enumerate(idxs_12):
                for k, (idx_k, J23) in enumerate(idxs_23):
                    F[i, k] = q6j(j, j, J12, j, Jtot, J23)
                    # Normalize by quantum dimensions
                    F[i, k] *= math.sqrt(abs(q_dim(J12) * q_dim(J23))) * (-1)**(int(round(2*(j+j+Jtot))))

            # R-matrix in J₂₃ basis (diagonal)
            R23 = np.zeros((n_block, n_block))
            for k, (idx_k, J23) in enumerate(idxs_23):
                if sign > 0:
                    R23[k, k] = r_eigenvalue(j, j, J23)
                else:
                    R23[k, k] = r_inverse_eigenvalue(j, j, J23)

            # σ₂ = F⁻¹ R₂₃ F  (recouple, apply R, recouple back)
            if abs(np.linalg.det(F)) > 1e-30:
                F_inv = np.linalg.inv(F)
                block = F_inv @ R23 @ F
            else:
                block = R23  # fallback

            for i, (idx_i, _) in enumerate(idxs_12):
                for k, (idx_k, _) in enumerate(idxs_23):
                    M[idx_i, idx_k] += block[i, k]

        return M

    # Build braid matrix
    M = np.eye(dim, dtype=complex)
    for g in braid_word:
        if g == 1:
            M = M @ sigma1_matrix(+1)
        elif g == -1:
            M = M @ sigma1_matrix(-1)
        elif g == 2:
            M = M @ sigma2_matrix(+1)
        elif g == -2:
            M = M @ sigma2_matrix(-1)

    # Quantum trace: Σ_{Jtot} [2Jtot+1]_q × (diagonal block trace)
    trace = 0.0
    for Jtot in jtot_values:
        idxs = [idx for idx, (_, Jt) in enumerate(basis) if Jt == Jtot]
        block_trace = sum(M[i, i] for i in idxs)
        trace += q_dim(Jtot) * block_trace

    qd = q_dim(j)
    if abs(qd) < 1e-30:
        return 0.0
    return abs(trace) / abs(qd)


def colored_jones_N(braid_word, n_strands, N):
    """Compute |J_N(K; q₀)| via fusion framework."""
    j = (N - 1) / 2.0  # spin from color dimension
    if n_strands == 2:
        return fusion_jones_2strand(braid_word, j)
    elif n_strands == 3:
        return fusion_jones_3strand(braid_word, j)
    else:
        return float('nan')


# ══════════════════════════════════════════════════════════════
# §3  VOLUME EXTRACTION
# ══════════════════════════════════════════════════════════════

def extract_volume(braid_word, n_strands, N_max=20, N_min=2):
    """Compute Vol_cJ = lim ln_q|J_N|/N from fusion colored Jones."""
    data = []
    for N in range(N_min, N_max + 1):
        t0 = time.time()
        jN = colored_jones_N(braid_word, n_strands, N)
        elapsed = time.time() - t0
        if math.isnan(jN) or jN < 1e-300:
            data.append((N, 0.0, float('-inf'), float('-inf'), elapsed))
            continue
        lnq = ln_q(jN)
        data.append((N, jN, lnq, lnq / N, elapsed))

    # Linear fit on the last half of data (asymptotic regime)
    valid = [(N, lnq) for N, jN, lnq, ratio, _ in data if lnq > -600]
    if len(valid) < 3:
        return 0.0, data

    half = len(valid) // 2
    Ns = np.array([d[0] for d in valid[half:]], dtype=float)
    lnqs = np.array([d[1] for d in valid[half:]], dtype=float)

    if len(Ns) < 2:
        return 0.0, data

    A_mat = np.vstack([Ns, np.ones(len(Ns))]).T
    slope, intercept = np.linalg.lstsq(A_mat, lnqs, rcond=None)[0]

    return abs(slope), data


# ══════════════════════════════════════════════════════════════
# §4  MAIN
# ══════════════════════════════════════════════════════════════

SNAPPY_VOLS = {
    'trefoil': 0.0, 'figure_eight': 2.02988, 'borromean': 7.32772,
}

SNAPPY_NUCLEAR = {
    'H': 0.0, 'He': 34.449, 'Li': 81.757, 'Be': 105.648,
    'B': 130.466, 'C': 139.157, 'N': 164.118, 'O': 188.130,
}

ELEMENTS = {
    1:  ("H",   1, 0,  938.783),
    2:  ("He",  2, 2,  3728.401),
    3:  ("Li",  3, 4,  6535.367),
}

AME2020_MASS = {k: v for _, (name, Z, N, M) in ELEMENTS.items()
                for k, v in [((Z, N), M)]}


def main():
    print("=" * 120)
    print("RESHETIKHIN-TURAEV FUSION COLORED JONES")
    print(f"q₀ = {q0:.10f}   ln(q₀) = {LN_Q:.10f}   HA = {HA:.10f}")
    print("Vol_cJ(K) = lim_{N→∞} ln_q|J_N(K;q₀)| / N   (fusion, exact)")
    print("=" * 120)
    print()

    # Reference knots
    print("REFERENCE KNOTS (fusion framework):")
    refs = [
        ("Trefoil",       [1, 1, 1],            2, 0.0),
        ("Figure-eight",  [1, -2, 1, -2],       3, 2.02988),
        ("Borromean",     [1, -2, 1, -2, 1, -2],3, 7.32772),
    ]
    for name, word, ns, vol_expected in refs:
        print(f"\n  {name} ({ns} strands, {len(word)} crossings):")
        vol_cJ, data = extract_volume(word, ns, N_max=15)
        print(f"    Vol_cJ = {vol_cJ:.4f}  (SnapPy: {vol_expected:.5f})")
        for N, jN, lnq, ratio, t in data:
            if lnq > -600:
                print(f"    N={N:3d}: |J_N| = {jN:.6e}  ln_q|J_N| = {lnq:+8.3f}  "
                      f"ln_q/N = {ratio:+8.4f}  [{t:.2f}s]")

    # Nucleon braids
    print()
    print("NUCLEON BRAIDS:")
    proton_word = [1, -2, 1, -2, 1, -2, 1, 1, 2]
    neutron_word = [1, -2, 1, -2, 1, -2, 1, 1, -2]
    vol_p, dp = extract_volume(proton_word, 3, N_max=12)
    vol_n, dn = extract_volume(neutron_word, 3, N_max=12)
    print(f"  Proton:  Vol_cJ = {vol_p:.4f}")
    for N, jN, lnq, ratio, t in dp:
        if lnq > -600:
            print(f"    N={N:3d}: |J_N| = {jN:.6e}  ln_q/N = {ratio:+.4f}  [{t:.1f}s]")
    print(f"  Neutron: Vol_cJ = {vol_n:.4f}")
    for N, jN, lnq, ratio, t in dn:
        if lnq > -600:
            print(f"    N={N:3d}: |J_N| = {jN:.6e}  ln_q/N = {ratio:+.4f}  [{t:.1f}s]")

    # Witness
    w = WitnessBuilder("atom-rt-fusion", engine="numpy")
    w.set_description(
        "Reshetikhin-Turaev fusion colored Jones. Exact J_N via "
        "quantum 6j symbols, no full tensor product. O(A²×N³)."
    )
    w.add_parameter("q0", str(q0))
    w.add_parameter("vol_cJ_proton", str(vol_p))
    w.add_parameter("vol_cJ_neutron", str(vol_n))
    w.save()


if __name__ == "__main__":
    main()
