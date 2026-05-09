#!/usr/bin/env python3
"""N_sym candidate (a): Gram-determinant probe.

Per `conj:n-sym-symmetric-channel-normalization` candidate (a):
$\\mathcal{N}_{\\rm sym}^{(a)}(q) = \\frac{\\prod_k \\dim_q(\\mathrm{sym}^{T(2,2k)})}{\\det \\mathcal{G}_{\\rm EW}(q)}$

where $\\mathcal{G}_{\\rm EW}$ is the Gram matrix of the EW Wedderburn-block
bilinear form. The block has 6 idempotents (sym + alt for each of
$T(2,4), T(2,6), T(2,8)$); the natural pairing is via the Markov trace.

This script tests SEVERAL candidate Gram-matrix structures to identify
which (if any) reproduces $\\mathcal{N}_{\\rm sym}(q_0) = 213.111807...$:

  (a1) Block-diagonal idempotent Gram: $\\mathcal{G}_{ij} = \\mathrm{tr}_M(e_i e_j) = \\delta_{ij} \\cdot \\mathrm{tr}_M(e_i)$
       Per host k: diag(1/[2]_q, 1/[2]_q). Combined 6×6 block-diagonal.

  (a2) Eigenvalue-product Gram: $\\mathcal{G}_{ii} = (\\text{eigenvalue})^2$
       Per host k: diag(q^{2k}, q^{-2k})^2. Combined 6×6.

  (a3) Cross-host Cartan-style Gram: per host eigenvalue, with off-host
       coupling q^{|k1-k2|}.

  (a4) Plancherel-normalized: $\\mathcal{G}_{ii} = w_i \\cdot (\\text{eigenvalue})^2$
       where $w_i = \\dim_q^2/[n]_q!$.

  (a5) "Bring-genus-4 analog": treat the 6 idempotents like the 10
       strands of EM Bring; compute $\\binom{6}{2}$-style determinant.

Outputs: which candidate(s) hit 213.11 (or 1/213.11 = 0.00469); rel err
table; recommendation for the next refinement.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
import sys as _sys
import mpmath
mpmath.mp.dps = 100

_sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR
from experimental_constants import M_E_MEV, G_F_MEV

q = mpmath.mpf(Q_50_DIGIT_STR)


def q_int(n):
    if n == 0:
        return mpmath.mpf(0)
    return (q ** n - q ** (-n)) / (q - 1 / q)


# Target value (from PR #515 n_sym numerical anchor)
G_F = mpmath.mpf(str(G_F_MEV))
m_e = mpmath.mpf(str(M_E_MEV))
v_weak = 1 / mpmath.sqrt(mpmath.sqrt(2) * G_F)
E_cross = (q - 1 / q) / 2
mu_0 = m_e / (3 * E_cross)
N_v = v_weak / (E_cross * mu_0)
prod_pl = (q_int(4) ** 2 / q_int(2)) * (q_int(6) ** 2 / q_int(2)) * (q_int(8) ** 2 / q_int(2))
N_sym_target = N_v / prod_pl
print(f"target N_sym(q_0) = {mpmath.nstr(N_sym_target, 20)}")
print(f"reciprocal target = {mpmath.nstr(1/N_sym_target, 20)}")
print()

# K values for the EW sector
K_VALUES = (2, 3, 4)  # T(2,4), T(2,6), T(2,8)


def candidate_a1():
    """Block-diagonal idempotent Gram: per host diag(1/[2]_q, 1/[2]_q) = 1/[2]_q · I_2.
    Combined 6×6 block-diag, det = (1/[2]_q)^6.
    """
    return (1 / q_int(2)) ** 6


def candidate_a2():
    """Eigenvalue-product Gram: per host diag(q^{2k}, q^{-2k}).
    Combined 6×6 block-diag, det = ∏_k (q^{2k} · q^{-2k}) = 1 trivially.
    """
    return mpmath.mpf(1)


def candidate_a2b():
    """Eigenvalue-squared Gram: per host diag((q^{2k})^2, (q^{-2k})^2).
    Combined det = ∏_k (q^{4k} · q^{-4k}) = 1.
    Variant: SUM rather than product per host: q^{4k} + q^{-4k}.
    """
    val = mpmath.mpf(1)
    for k in K_VALUES:
        val *= (q ** (4*k) + q ** (-4*k))
    return val


def candidate_a3():
    """Cross-host Cartan-style Gram: 3×3 matrix indexed by k=2,3,4.
    Diagonal: [2k]_q (or q^{2k} + q^{-2k}); off-diagonal: q^{|k1-k2|}.
    """
    M = mpmath.matrix(3, 3)
    for i, k1 in enumerate(K_VALUES):
        for j, k2 in enumerate(K_VALUES):
            if i == j:
                M[i, j] = q_int(2*k1)
            else:
                M[i, j] = q_int(abs(k1 - k2))
    return mpmath.det(M)


def candidate_a3b():
    """Variant: diagonal q^{2k} + q^{-2k}, off-diag = 1."""
    M = mpmath.matrix(3, 3)
    for i, k1 in enumerate(K_VALUES):
        for j, k2 in enumerate(K_VALUES):
            if i == j:
                M[i, j] = q ** (2*k1) + q ** (-2*k1)
            else:
                M[i, j] = mpmath.mpf(1)
    return mpmath.det(M)


def candidate_a4():
    """Plancherel-normalized: per host w_i = 1/[2]_q (Plancherel for H_2 sym/alt blocks).
    Multiply by eigenvalue squared.
    """
    val = mpmath.mpf(1)
    for k in K_VALUES:
        # sym block contribution: w_+ · q^{2k} = (1/[2]_q) · q^{2k}
        # alt block contribution: w_- · q^{-2k} = (1/[2]_q) · q^{-2k}
        # det of 2×2 diag block = w_+ · w_- · q^{2k} · q^{-2k} = (1/[2]_q)^2
        val *= (1 / q_int(2)) ** 2
    return val


def candidate_a5():
    """6×6 "Bring-style" Gram: indexed by (k, ±) pairs; diagonal = q^{±2k},
    off-diagonal: q^{|k1±-k2±|} where the sign-pattern is the dual.
    """
    pairs = [(k, sign) for k in K_VALUES for sign in (+1, -1)]
    n = len(pairs)
    M = mpmath.matrix(n, n)
    for i, (k1, s1) in enumerate(pairs):
        for j, (k2, s2) in enumerate(pairs):
            exp_i = 2 * k1 * s1
            exp_j = 2 * k2 * s2
            if i == j:
                M[i, j] = q ** exp_i + q ** (-exp_i)  # symmetric pairing
            else:
                M[i, j] = q ** abs(exp_i - exp_j)
    return mpmath.det(M)


def candidate_a6():
    """Conjectured 'natural' Gram-style product: ∏_k (q^{2k} - q^{-2k})·(q^{2k} + q^{-2k}) / (q-q^-1)·(q+q^-1)."""
    val = mpmath.mpf(1)
    for k in K_VALUES:
        # numerator: q^{4k} - q^{-4k} (a Frobenius-like Gram cell)
        val *= (q ** (4*k) - q ** (-4*k)) / (q - 1/q)
    return val


def candidate_a7():
    """Try `[4]_q · [6]_q · [8]_q · [3]_q!`: Bring-EM-style q-factorial × link complexities."""
    return q_int(4) * q_int(6) * q_int(8) * q_int(2) * q_int(3)


candidates = {
    "(a1) block-diag idemp Gram, (1/[2]_q)^6":                candidate_a1(),
    "(a2) eigenvalue product, ∏ q^{2k}·q^{-2k}":              candidate_a2(),
    "(a2b) sum-of-eigenvalues^2, ∏(q^{4k}+q^{-4k})":          candidate_a2b(),
    "(a3) 3×3 Cartan-style, diag [2k]_q":                     candidate_a3(),
    "(a3b) 3×3 variant, diag q^{2k}+q^{-2k}":                 candidate_a3b(),
    "(a4) Plancherel-normalized, ∏(1/[2]_q)^2":               candidate_a4(),
    "(a5) 6×6 Bring-style, off-diag q^|Δ|":                   candidate_a5(),
    "(a6) Frobenius product, ∏(q^{4k}-q^{-4k})/(q-q^-1)":     candidate_a6(),
    "(a7) [4]_q·[6]_q·[8]_q·[2]_q·[3]_q":                     candidate_a7(),
}

# Add inverse forms (in case Gram is in denominator)
candidates_with_inverse = {}
for n, v in candidates.items():
    candidates_with_inverse[n] = v
    if v != 0:
        candidates_with_inverse[f"1 / {n}"] = 1 / v


print(f"{'candidate':<58} {'value':>20} {'rel err vs N_sym %':>22}")
print('-' * 105)
ranked = sorted(
    candidates_with_inverse.items(),
    key=lambda kv: float(abs(kv[1] - N_sym_target) / N_sym_target) if kv[1] != 0 else float('inf'),
)
rows = []
for name, val in ranked:
    if val == 0:
        rel_err = mpmath.inf
    else:
        rel_err = abs(val - N_sym_target) / N_sym_target
    flag = " *** clean" if abs(rel_err) < 1e-3 else (" * close" if abs(rel_err) < 0.05 else "")
    print(f"  {name:<56} {mpmath.nstr(val, 8):>20} {mpmath.nstr(rel_err*100, 6):>21}%{flag}")
    rows.append({
        'candidate': name,
        'value': mpmath.nstr(val, 30),
        'rel_err_pct': float(rel_err) * 100 if val != 0 else None,
    })

# Best candidate
best = ranked[0]
print()
print(f"Best fit: {best[0]} = {mpmath.nstr(best[1], 12)}")
rel_best = abs(best[1] - N_sym_target) / N_sym_target if best[1] != 0 else mpmath.inf
print(f"  rel err: {mpmath.nstr(rel_best*100, 6)}%")

# Verdict
print()
print("=" * 70)
print("VERDICT:")
print("=" * 70)
if float(rel_best) < 1e-3:
    print(f"  CLOSURE: candidate '{best[0]}' matches N_sym to <0.1%.")
    print(f"  → conj:n-sym-symmetric-channel-normalization closes via this form.")
    print(f"  → NV-1 PSLQ extended basis can now confirm.")
elif float(rel_best) < 0.05:
    print(f"  PROMISING: candidate '{best[0]}' matches to {float(rel_best)*100:.2f}%.")
    print(f"  Leading order likely identified; next-order correction needed.")
else:
    print(f"  NO CLEAN MATCH: best candidate is {float(rel_best)*100:.2f}% off.")
    print(f"  Candidate (a) Gram-determinant ansatz is FALSIFIED in this form.")
    print(f"  → pursue candidate (b) Higgs-eaten Goldstone phase space, OR")
    print(f"  → candidate (c) Hochschild-Plancherel ratio.")

# Witness output
out = {
    'computation': 'n-sym-gram-determinant-probe',
    'computedAt': datetime.now(timezone.utc).isoformat(),
    'description': (
        'Probe of conj:n-sym-symmetric-channel-normalization candidate (a) — '
        'Gram determinant of the EW Wedderburn-block bilinear form. Tests 9 '
        'candidate Gram-matrix structures (and their inverses) against the '
        'numerical target N_sym(q_0) = 213.111807...'
    ),
    'q_0_dps': mpmath.mp.dps,
    'q_0': mpmath.nstr(q, 50),
    'N_sym_target': mpmath.nstr(N_sym_target, 25),
    'candidates': rows,
    'best_candidate': best[0],
    'best_value': mpmath.nstr(best[1], 25) if best[1] != 0 else 'inf',
    'best_rel_err_pct': float(rel_best) * 100 if best[1] != 0 else None,
    'verdict': (
        'closure' if float(rel_best) < 1e-3
        else 'promising' if float(rel_best) < 0.05
        else 'falsified — pursue (b) or (c)'
    ),
}
out_path = WitnessBuilder.wrap_legacy("n-sym-gram-determinant-probe", out, script_path=__file__, engine="python").save()
print(f"\n→ wrote {out_path}")
