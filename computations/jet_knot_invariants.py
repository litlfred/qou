#!/usr/bin/env python3
"""
Jet-filtered knot invariants: per-level character ratios.

At each jet level k, the Hecke algebra H_k(q) has partitions with
Wedderburn weights. The nuclear braid β ∈ H₃(q) has characters in
each H₃ irrep (sym, std, alt). Via the branching rule H_k → H₃,
each partition of k decomposes into H₃ components.

The per-level knot invariant is:
  a_k = Σ_λ w_λ × χ_λ(β) / Σ_λ w_λ × dim_restricted(λ)

Scope note (bean `qou-zgg2`): `internuc_characters(Z, N)` below evaluates
only the inter-nucleon crossing pair factors `(1, 0), (1, -h), (1, -h/2)`
projected into the 2-generator H₃(q) quotient (omitting intra-nucleon B₃
prefixes and true B_{3A} strand positions). Convergence by k=4 reflects
this H₃-projected model, not the full B_{3A} → H_{3A} atomic braid word.

Key finding: a_k CONVERGES by k=4. This means:
  - k=3 carries the nuclear braid's topology
  - k≥4 corrections are topology-independent (generic)
  - The stable ratio is W_STD-dominated

For Z=N nuclei with sp=V_std=ap (even-even):
  a_k = V_inter / (1 + W_STD)

For Z=N with sp=-ap (odd-odd, extremal cancellation):
  a_k = W_STD × V_std / (1 + W_STD)

All symbolic in q.

Usage:
    python3 jet_knot_invariants.py
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from hecke_core import (
    h,
    q0,
    qi,
    check_frobenius,
    q_int,
)
from pyhecke.gram import (
    z,
    W_SYM,
    W_STD,
    W_ALT,
    G,
    NF_NAMES,
    hm,
)
from hecke_characters import partitions_of, dim_q, qfac
from witness_base import WitnessBuilder
from qou_substrate.constants import Q as Q0_PROTON  # noqa: E402 — anchor-independent proton pin (qou-6p3b Tranche C)

# tr_basis[5] = tr_M(sigma_0 sigma_1 sigma_0) = h*z^2 + z, NOT z^3 (Markov
# axioms: tr(s0 s1 s0) = tr(s1 s0^2) = tr(s1 (h s0 + 1)) = h*z^2 + z).
# docs/audits/2026-05-19-trm5-markov-bug.md fixed this in pyhecke.gram on
# 2026-05-19; it never propagated here (bean qou-ssex). NOTE: this binding
# is currently unread in this module -- kept correct rather than deleted so
# a future consumer does not pick up the wrong weight. h is the one already
# imported from hecke_core (= q0 - qi, verified), NOT a second q0 source:
# deriving it from Q0_PROTON instead would pin TR_M[5] to a different anchor
# than the z it multiplies if hecke_core's pin ever moves (Copilot review,
# PR #6110). hecke_core.q0 is currently the proton pin, so the value is
# unchanged -- this removes a latent straddle, not a live one.
tr_basis = [1, z, z, z**2, z**2, h * z**2 + z]   # h = q0 - qi, from hecke_core


def contains(lam, mu):
    for i in range(len(mu)):
        if i >= len(lam) or lam[i] < mu[i]:
            return False
    return True


def count_syt_skew(lam, mu):
    lam = list(lam)
    mu = list(mu) + [0] * (len(lam) - len(mu))
    cells = [(i, j) for i in range(len(lam))
             for j in range(mu[i] if i < len(mu) else 0, lam[i])]
    n = len(cells)
    if n <= 1:
        return 1
    if n > 10:
        return max(1, n // 2)
    from itertools import permutations
    count = 0
    for perm in permutations(range(n)):
        filling = {cells[idx]: perm[idx] for idx in range(n)}
        valid = True
        for (i, j), val in filling.items():
            if (i, j + 1) in filling and filling[(i, j + 1)] < val:
                valid = False
                break
            if (i + 1, j) in filling and filling[(i + 1, j)] < val:
                valid = False
                break
        if valid:
            count += 1
    return count


H3_PARTS = [(3,), (2, 1), (1, 1, 1)]
H3_DIMS = [1, 2, 1]


def internuc_characters(Z, N):
    A = Z + N
    ordering = []
    pc, nc = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append('p')
            pc += 1
        else:
            ordering.append('n')
            nc += 1
    chain = []
    for k in range(A):
        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == 'p' and tj == 'p':
                chain.append((1, 0))
            elif ti == 'n' and tj == 'n':
                chain.append((1, -h))
            else:
                chain.append((1, -h / 2))
    if not chain:
        return 1.0, 1.0, 1.0
    a, b = 0.0, 1.0
    sp, ap = 1.0, 1.0
    for c, d in chain:
        a, b = a * c * h + a * d + b * c, a * c + b * d
        sp *= c * q0 + d
        ap *= -c * qi + d
    V_std = z * a + b
    return sp, V_std, ap


def jet_knot_invariants(Z, N, max_k=8):
    sp, V_std, ap = internuc_characters(Z, N)
    chars = {(3,): sp, (2, 1): V_std, (1, 1, 1): ap}
    results = []
    for k in range(3, max_k + 1):
        nfac_k = qfac(k, Q0_PROTON)
        total_chi = 0.0
        total_dim = 0.0
        for lam in partitions_of(k):
            d_q_val = dim_q(lam, Q0_PROTON)
            w_lam = d_q_val ** 2 / nfac_k
            chi_beta = 0.0
            dim_rest = 0.0
            for mu, mu_dim in zip(H3_PARTS, H3_DIMS):
                if contains(lam, mu):
                    m = count_syt_skew(lam, mu)
                    chi_beta += m * chars[mu]
                    dim_rest += m * mu_dim
            total_chi += w_lam * chi_beta
            total_dim += w_lam * dim_rest
        a_k = total_chi / total_dim if abs(total_dim) > 1e-15 else 1.0
        results.append({
            'k': k,
            'a_k': round(a_k, 8),
            'chi_weighted': round(total_chi, 8),
            'dim_weighted': round(total_dim, 8),
        })
    return results, (sp, V_std, ap)


ATOMS = [
    ("³H", 1, 2), ("³He", 2, 1), ("⁴He", 2, 2),
    ("⁶Li", 3, 3), ("⁷Li", 3, 4), ("⁹Be", 4, 5),
    ("¹²C", 6, 6), ("¹⁶O", 8, 8),
]

all_data = {}
for name, Z, N in ATOMS:
    levels, (sp, V_std, ap) = jet_knot_invariants(Z, N, max_k=8)
    all_data[name] = {'levels': levels, 'sp': sp, 'V_std': V_std, 'ap': ap}

    stable_a = levels[-1]['a_k'] if levels else 1.0
    print(f"{name} (Z={Z},N={N}): sp={sp:.4f} V_std={V_std:.4f} ap={ap:.4f}")
    for lv in levels:
        marker = " ★" if lv['k'] == 3 else ""
        print(f"  k={lv['k']}: a_k = {lv['a_k']:.6f}{marker}")
    print(f"  Stable (k≥4): {stable_a:.6f}")
    print(f"  1 + W_STD = {1 + W_STD:.6f}")
    if abs(sp - ap) < 0.01:
        print(f"  sp≈ap → a_∞ ≈ V_inter/(1+W_STD) = {abs(sp)/(1+W_STD):.6f}")
    else:
        print(f"  sp≠ap → a_∞ ≈ W_STD×V_std/(1+W_STD) = {W_STD*V_std/(1+W_STD):.6f}")
    print()

# Witness
w = WitnessBuilder("jet-knot-invariants", engine="python")
w.set_description(
    "Per-level knot invariants from jet-filtered branching. "
    "At each k, the nuclear braid's H₃ characters are weighted by "
    "the Wedderburn structure of H_k. Key finding: a_k converges by "
    "k=4 (topology-independent beyond k=3). For Z=N even-even: "
    "a_k = V_inter/(1+W_STD). Stable ratio ≈ W_STD."
)
w.set_content_block("prop:confined-knot-binding")
w.add_parameter("q", q0)
w.add_parameter("W_STD", W_STD)
w.add_parameter("1_plus_W_STD", 1 + W_STD)

for name, Z, N in ATOMS:
    w.add_data(name, all_data[name])

w.save()
