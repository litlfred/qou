#!/usr/bin/env python3
"""
RT FUSION v2 — reduced colored Jones volume.

Key fix: at fixed q₀ > 1, [N]_q grows exponentially with N,
so ALL |J_N| grow exponentially — the trivial growth from
quantum dimensions masks the knot-specific volume.

The REDUCED colored Jones polynomial removes this:
  Ĵ_N(K; q) = J_N(K; q) / J_N(unknot; q) = J_N(K; q) / [N]_q

The reduced volume:
  Vol_cJ(K) = lim_{N→∞} ln_q|Ĵ_N(K; q₀)| / N

For the unknot: Ĵ_N = 1, so Vol_cJ = 0.  ✓
For hyperbolic knots: Vol_cJ should be proportional to Vol(K).

This file also fixes the 6j symbol normalization using the
Kauffman-Lins convention (consistent with SnapPy).

Usage:
    python3 folio-assistant/computations/atom_rt_fusion_v2.py
"""

import math
import sys
import time
from functools import lru_cache
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


@lru_cache(maxsize=1024)
def qn(n):
    """[n]_q = (q^n - q^{-n})/(q - q^{-1}). Cached."""
    if abs(n) < 1e-15:
        return 0.0
    return (q0**n - q0**(-n)) / HA


def q_dim(j):
    """Quantum dimension [2j+1]_q."""
    return qn(2 * j + 1)


@lru_cache(maxsize=1024)
def qfact(n):
    """[n]_q! cached."""
    if n <= 0:
        return 1.0
    return qfact(n - 1) * qn(n)


def casimir(j):
    """Quadratic Casimir C_j = j(j+1)."""
    return j * (j + 1)


# ══════════════════════════════════════════════════════════════
# §1  QUANTUM 6j SYMBOLS (Kauffman-Lins convention)
# ══════════════════════════════════════════════════════════════

def triangle_coeff(a, b, c):
    """Triangle coefficient Δ(a,b,c) for quantum 6j.

    Δ(a,b,c)² = [a+b-c]![a-b+c]![-a+b+c]! / [a+b+c+1]!

    All arguments are half-integers (spins).
    """
    s = a + b + c
    if abs(s - round(s)) > 0.01:
        return 0.0
    p1 = int(round(a + b - c))
    p2 = int(round(a - b + c))
    p3 = int(round(-a + b + c))
    p4 = int(round(a + b + c + 1))
    if p1 < 0 or p2 < 0 or p3 < 0:
        return 0.0
    val = qfact(p1) * qfact(p2) * qfact(p3) / qfact(p4)
    return math.sqrt(abs(val))


@lru_cache(maxsize=4096)
def q6j(j1, j2, j12, j3, j_total, j23):
    """Quantum 6j symbol { j1  j2  j12 }
                         { j3  j_total  j23 }_q

    Kauffman-Lins / Kirillov-Reshetikhin convention.
    All arguments are half-integer spins.
    """
    # Triangle conditions
    tri1 = triangle_coeff(j1, j2, j12)
    tri2 = triangle_coeff(j12, j3, j_total)
    tri3 = triangle_coeff(j2, j3, j23)
    tri4 = triangle_coeff(j1, j23, j_total)

    if abs(tri1 * tri2 * tri3 * tri4) < 1e-30:
        return 0.0

    # Racah sum
    z_min = max(
        int(round(j1 + j2 + j12)),
        int(round(j12 + j3 + j_total)),
        int(round(j2 + j3 + j23)),
        int(round(j1 + j23 + j_total))
    )
    z_max = min(
        int(round(j1 + j2 + j3 + j_total)),
        int(round(j1 + j12 + j3 + j23)),
        int(round(j2 + j12 + j_total + j23))
    )

    total = 0.0
    for zz in range(z_min, z_max + 1):
        sign = (-1)**zz
        num = qfact(zz + 1)
        d1 = qfact(zz - int(round(j1 + j2 + j12)))
        d2 = qfact(zz - int(round(j12 + j3 + j_total)))
        d3 = qfact(zz - int(round(j2 + j3 + j23)))
        d4 = qfact(zz - int(round(j1 + j23 + j_total)))
        d5 = qfact(int(round(j1 + j2 + j3 + j_total)) - zz)
        d6 = qfact(int(round(j1 + j12 + j3 + j23)) - zz)
        d7 = qfact(int(round(j2 + j12 + j_total + j23)) - zz)
        denom = d1 * d2 * d3 * d4 * d5 * d6 * d7
        if abs(denom) > 1e-30:
            total += sign * num / denom

    return tri1 * tri2 * tri3 * tri4 * total


# ══════════════════════════════════════════════════════════════
# §2  R-MATRIX IN FUSION BASIS
# ══════════════════════════════════════════════════════════════

def r_eigenvalue(j1, j2, J):
    """R-matrix eigenvalue for V_J ⊂ V_{j1} ⊗ V_{j2}."""
    phase = (-1) ** int(round(j1 + j2 - J))
    exp = (casimir(J) - casimir(j1) - casimir(j2)) / 2.0
    return phase * q0 ** exp


def fusion_channels(j1, j2):
    """CG channels: J from |j1-j2| to j1+j2 in integer steps."""
    J_min = abs(j1 - j2)
    J_max = j1 + j2
    return [J_min + k for k in range(int(round(J_max - J_min)) + 1)]


# ══════════════════════════════════════════════════════════════
# §3  FUSION JONES: 2 AND 3 STRANDS
# ══════════════════════════════════════════════════════════════

def fusion_jones_2strand(braid_word, j):
    """Exact J_N for 2-strand braid closure, color j."""
    channels = fusion_channels(j, j)
    result = 0.0
    for J in channels:
        product = 1.0
        for g in braid_word:
            lam = r_eigenvalue(j, j, J)
            product *= lam if g > 0 else (1.0 / lam)
        result += q_dim(J) * product
    return result


def fusion_jones_3strand(braid_word, j):
    """Exact J_N for 3-strand braid closure, color j.

    Fusion basis: (J₁₂, J_total) where V_{j}^⊗3 = ⊕ V_{J_total}
    via V_j ⊗ V_j = ⊕ V_{J₁₂}, V_{J₁₂} ⊗ V_j = ⊕ V_{J_total}.

    σ₁ is diagonal: eigenvalue R(j,j,J₁₂).
    σ₂ = F⁻¹ · diag(R(j,j,J₂₃)) · F where F is the 6j F-matrix.
    """
    channels_12 = fusion_channels(j, j)
    basis = []
    for J12 in channels_12:
        for Jtot in fusion_channels(J12, j):
            basis.append((J12, Jtot))

    dim = len(basis)
    if dim == 0:
        return 0.0

    # σ₁: diagonal
    def make_sigma1(sign):
        M = np.zeros((dim, dim))
        for idx, (J12, Jtot) in enumerate(basis):
            lam = r_eigenvalue(j, j, J12)
            M[idx, idx] = lam if sign > 0 else 1.0 / lam
        return M

    # F-matrix: recoupling (J₁₂, Jtot) ↔ (J₂₃, Jtot)
    # F[J₁₂, J₂₃; Jtot] = (-1)^{j+j+j+Jtot} × √([2J₁₂+1][2J₂₃+1])
    #                        × { j   j   J₁₂ }
    #                          { j   Jtot  J₂₃ }_q
    jtot_values = sorted(set(Jt for _, Jt in basis))

    def make_sigma2(sign):
        M = np.zeros((dim, dim))
        for Jtot in jtot_values:
            idxs = [(i, J12) for i, (J12, Jt) in enumerate(basis) if Jt == Jtot]
            n_block = len(idxs)
            if n_block == 0:
                continue

            # F-matrix block
            F = np.zeros((n_block, n_block))
            for a, (ia, J12a) in enumerate(idxs):
                for b, (ib, J23b) in enumerate(idxs):
                    phase = (-1)**int(round(3*j + Jtot))
                    dim_factor = math.sqrt(abs(q_dim(J12a) * q_dim(J23b)))
                    sixj = q6j(j, j, J12a, j, Jtot, J23b)
                    F[a, b] = phase * dim_factor * sixj

            # R in J₂₃ basis
            R23 = np.zeros((n_block, n_block))
            for b, (ib, J23b) in enumerate(idxs):
                lam = r_eigenvalue(j, j, J23b)
                R23[b, b] = lam if sign > 0 else 1.0 / lam

            # σ₂ = F^T · R₂₃ · F  (F is orthogonal in the quantum case)
            # Actually: σ₂ = F⁻¹ R₂₃ F, and for real orthogonal F: F⁻¹ = F^T
            det_F = np.linalg.det(F) if n_block > 0 else 0
            if abs(det_F) > 1e-20:
                F_inv = np.linalg.inv(F)
                block = F_inv @ R23 @ F
            else:
                # F is singular — use pseudoinverse
                block = np.linalg.pinv(F) @ R23 @ F

            for a, (ia, _) in enumerate(idxs):
                for b, (ib, _) in enumerate(idxs):
                    M[ia, ib] += block[a, b]

        return M

    # Build braid matrix
    M = np.eye(dim)
    for g in braid_word:
        if g == 1:
            M = M @ make_sigma1(+1)
        elif g == -1:
            M = M @ make_sigma1(-1)
        elif g == 2:
            M = M @ make_sigma2(+1)
        elif g == -2:
            M = M @ make_sigma2(-1)

    # Quantum trace: Σ_{Jtot} [2Jtot+1]_q × tr(M restricted to Jtot)
    trace = 0.0
    for Jtot in jtot_values:
        idxs = [i for i, (_, Jt) in enumerate(basis) if Jt == Jtot]
        block_trace = sum(M[i, i] for i in idxs)
        trace += q_dim(Jtot) * block_trace

    return trace


def colored_jones_N(braid_word, n_strands, N):
    """Compute J_N(K; q₀) via RT fusion."""
    j = (N - 1) / 2.0
    if n_strands == 2:
        return fusion_jones_2strand(braid_word, j)
    elif n_strands == 3:
        return fusion_jones_3strand(braid_word, j)
    return float('nan')


# ══════════════════════════════════════════════════════════════
# §4  REDUCED COLORED JONES VOLUME
# ══════════════════════════════════════════════════════════════

def extract_reduced_volume(braid_word, n_strands, N_max=15, N_min=2):
    """Compute Vol_cJ = lim ln_q|Ĵ_N|/N where Ĵ_N = J_N/[N]_q.

    Subtracts the trivial quantum dimension growth.
    """
    data = []
    for N in range(N_min, N_max + 1):
        t0 = time.time()
        jN_raw = colored_jones_N(braid_word, n_strands, N)
        elapsed = time.time() - t0

        if math.isnan(jN_raw):
            data.append((N, float('nan'), float('nan'), float('nan'), float('nan'), elapsed))
            continue

        j = (N - 1) / 2.0
        qd = q_dim(j)  # [N]_q = quantum dimension of color

        # Reduced: Ĵ_N = J_N / [N]_q
        if abs(qd) > 1e-30:
            j_reduced = abs(jN_raw) / abs(qd)
        else:
            j_reduced = abs(jN_raw)

        lnq_raw = ln_q(abs(jN_raw)) if abs(jN_raw) > 1e-300 else float('-inf')
        lnq_red = ln_q(j_reduced) if j_reduced > 1e-300 else float('-inf')

        data.append((N, abs(jN_raw), j_reduced, lnq_raw, lnq_red, elapsed))

    # Fit: ln_q|Ĵ_N| = a × N + b → Vol_cJ = |a|
    valid = [(N, lnq_red) for N, _, _, _, lnq_red, _ in data
             if not math.isnan(lnq_red) and lnq_red > -600]
    if len(valid) < 3:
        return 0.0, 0.0, data

    Ns = np.array([d[0] for d in valid], dtype=float)
    lnqs = np.array([d[1] for d in valid], dtype=float)
    A_mat = np.vstack([Ns, np.ones(len(Ns))]).T
    slope, intercept = np.linalg.lstsq(A_mat, lnqs, rcond=None)[0]

    # Also fit the raw (unreduced) for comparison
    valid_raw = [(N, lnq_raw) for N, _, _, lnq_raw, _, _ in data
                 if not math.isnan(lnq_raw) and lnq_raw > -600]
    if len(valid_raw) >= 3:
        Ns_r = np.array([d[0] for d in valid_raw], dtype=float)
        lnqs_r = np.array([d[1] for d in valid_raw], dtype=float)
        A_r = np.vstack([Ns_r, np.ones(len(Ns_r))]).T
        slope_raw = np.linalg.lstsq(A_r, lnqs_r, rcond=None)[0][0]
    else:
        slope_raw = 0.0

    return abs(slope), abs(slope_raw), data


# ══════════════════════════════════════════════════════════════
# §5  MAIN
# ══════════════════════════════════════════════════════════════

def main():
    print("=" * 120)
    print("RT FUSION v2 — REDUCED COLORED JONES VOLUME")
    print(f"q₀ = {q0:.10f}   ln(q₀) = {LN_Q:.10f}")
    print(f"Vol_cJ(K) = lim ln_q|Ĵ_N|/N   where Ĵ_N = J_N/[N]_q  (reduced)")
    print("=" * 120)
    print()

    # Show [N]_q growth for reference
    print("Quantum dimensions [N]_q at q₀:")
    for N in range(2, 16):
        j = (N - 1) / 2.0
        print(f"  [N={N:2d}]_q = {q_dim(j):12.4f}   ln_q = {ln_q(abs(q_dim(j))):+8.3f}")
    print()

    # Reference knots
    print("=" * 120)
    print("REFERENCE KNOTS")
    print("=" * 120)

    refs = [
        ("Unknot",        [],                  2, 0.0),
        ("Trefoil",       [1, 1, 1],           2, 0.0),
        ("Figure-eight",  [1, -2, 1, -2],      3, 2.02988),
        ("Borromean",     [1, -2, 1, -2, 1, -2], 3, 7.32772),
    ]

    for name, word, ns, vol_snap in refs:
        print(f"\n  {name} ({ns} strands, {len(word)} crossings, SnapPy Vol = {vol_snap:.5f}):")
        vol_red, vol_raw, data = extract_reduced_volume(word, ns, N_max=15)
        print(f"    Vol_cJ (reduced) = {vol_red:.4f}")
        print(f"    Vol_cJ (raw)     = {vol_raw:.4f}")
        print(f"    {'N':>4} | {'|J_N|':>12} | {'|Ĵ_N|':>12} | {'ln_q|J_N|':>10} | {'ln_q|Ĵ_N|':>10} | {'ln_q|Ĵ|/N':>10}")
        print(f"    {'─'*4}-+-{'─'*12}-+-{'─'*12}-+-{'─'*10}-+-{'─'*10}-+-{'─'*10}")
        for N, jN_raw, jN_red, lnq_raw, lnq_red, t in data:
            if math.isnan(jN_raw):
                print(f"    {N:4d} | {'nan':>12} | {'nan':>12} | {'nan':>10} | {'nan':>10} | {'nan':>10}")
            elif lnq_red > -600:
                print(f"    {N:4d} | {jN_raw:12.4e} | {jN_red:12.4e} | {lnq_raw:+10.3f} | {lnq_red:+10.3f} | {lnq_red/N:+10.4f}")

    # Ratio check
    print()
    print("=" * 120)
    print("RATIO CHECK: Vol_cJ(reduced) ratios vs SnapPy ratios")
    print("=" * 120)

    vols = {}
    for name, word, ns, vol_snap in refs:
        vol_red, _, _ = extract_reduced_volume(word, ns, N_max=15)
        vols[name] = (vol_red, vol_snap)
        print(f"  {name:15s}: Vol_cJ = {vol_red:8.4f}   Vol_snap = {vol_snap:.5f}")

    if vols['Figure-eight'][0] > 0 and vols['Borromean'][0] > 0:
        r_cJ = vols['Figure-eight'][0] / vols['Borromean'][0]
        r_snap = vols['Figure-eight'][1] / vols['Borromean'][1]
        print(f"\n  Figure-eight / Borromean:")
        print(f"    Vol_cJ ratio:   {r_cJ:.4f}")
        print(f"    SnapPy ratio:   {r_snap:.4f}")

    # Nucleon braids
    print()
    print("=" * 120)
    print("NUCLEON BRAIDS")
    print("=" * 120)
    proton_word = [1, -2, 1, -2, 1, -2, 1, 1, 2]
    neutron_word = [1, -2, 1, -2, 1, -2, 1, 1, -2]

    vol_p, _, dp = extract_reduced_volume(proton_word, 3, N_max=12)
    vol_n, _, dn = extract_reduced_volume(neutron_word, 3, N_max=12)

    print(f"  Proton:  Vol_cJ(reduced) = {vol_p:.4f}")
    for N, jN_raw, jN_red, _, lnq_red, t in dp:
        if not math.isnan(jN_red) and lnq_red > -600:
            print(f"    N={N:3d}: |Ĵ_N| = {jN_red:.4e}  ln_q|Ĵ|/N = {lnq_red/N:+.4f}  [{t:.1f}s]")

    print(f"\n  Neutron: Vol_cJ(reduced) = {vol_n:.4f}")
    for N, jN_raw, jN_red, _, lnq_red, t in dn:
        if not math.isnan(jN_red) and lnq_red > -600:
            print(f"    N={N:3d}: |Ĵ_N| = {jN_red:.4e}  ln_q|Ĵ|/N = {lnq_red/N:+.4f}  [{t:.1f}s]")

    print(f"\n  Neutron/Proton Vol_cJ ratio: {vol_n/vol_p:.4f}  (CODATA m_n/m_p: {939.565/938.272:.4f})")

    # Witness
    w = WitnessBuilder("atom-rt-fusion-v2", engine="numpy")
    w.set_description(
        "RT fusion v2: REDUCED colored Jones volume. "
        "Ĵ_N = J_N/[N]_q removes trivial dimension growth. "
        "Exact via quantum 6j symbols."
    )
    w.add_parameter("q0", str(q0))
    w.add_parameter("proton_vol_cJ", str(vol_p))
    w.add_parameter("neutron_vol_cJ", str(vol_n))
    ref_data = {name: {'vol_cJ': v, 'vol_snap': vs}
                for name, (v, vs) in vols.items()}
    w.add_data("reference_knots", ref_data)
    w.save()


if __name__ == "__main__":
    main()
