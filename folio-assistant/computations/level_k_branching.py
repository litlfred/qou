#!/usr/bin/env python3
"""
LEVEL-k BRANCHING: self-conjugate partitions at intermediate Hecke
levels, generalising the Wigner (2,2) ⊢ 4 correction.

Framework
---------

Each self-conjugate partition λ ⊢ k contributes a binding correction

    Δ_λ(Z, N) = m_e · H_q(λ) · f_λ(Z, N) / N_λ

where:

  H_q(λ) = ∏_{x ∈ λ} [h_x(λ)]_q   q-hook product (paper:wigner-np-pairing)
  f_λ(Z, N)                       occupancy: # of times λ structure
                                  appears in atom (Z, N).  Specific
                                  to λ; phenomenological at this stage.
  N_λ                             normalisation (= 1 for simple cases)

For λ = (2,2) ⊢ 4, the paper gives f = min(Z,N)/A (= np-pair count
per nucleon).  H_q((2,2)) = [3]_q [2]_q² ≈ 6.29.

This script:
  1. Enumerates self-conjugate λ ⊢ k for k = 4, 6, 8, 10, 12.
  2. Computes H_q(λ) and dim_q V_λ.
  3. Tries several occupancy models for f_λ.
  4. Adds these corrections to the per-generator + Wigner baseline
     and reports the improvement for D, T, ³He, ⁴He.

Goal: find an occupancy model that bridges D and ⁴He sign flips
while keeping T, ³He close to AME.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

from hecke_core import (h as H_A_F, z as Z_MARKOV, _step_chain_generic)
from hecke_characters import dim_q, young_hooks, partitions_of
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
H_A = Q0 - QI
me = mp.mpf(str(M_E_MEV))
z_m = mp.mpf(str(float(Z_MARKOV)))
G = mp.catalan
alpha_bind = me * 8 * G
q3 = Q0**2 + 1 + QI**2
q2 = Q0 + QI
HA2 = H_A**2


def q_int(n):
    return (Q0**n - QI**n) / (Q0 - QI)


def q_fact(n):
    out = mp.mpf(1)
    for i in range(2, n+1):
        out *= q_int(i)
    return out


def transpose_partition(lam):
    if not lam:
        return tuple()
    return tuple(sum(1 for p in lam if p > j) for j in range(lam[0]))


def hook_product_q(lam):
    out = mp.mpf(1)
    for h in young_hooks(lam):
        out *= q_int(int(h))
    return out


def dim_q_lam(lam):
    n = sum(lam)
    return q_fact(n) / hook_product_q(lam)


def self_conjugate(n):
    return [tuple(lam) for lam in partitions_of(n)
             if transpose_partition(tuple(lam)) == tuple(lam)]


# ─── Per-generator inter-only Phi (from prior work) ───────────────

def chain_lambda_sym(chain):
    out = mp.mpf(1)
    for c, d in chain:
        out *= mp.mpf(c)*Q0 + mp.mpf(d)
    return out


def chain_lambda_alt(chain):
    out = mp.mpf(1)
    for c, d in chain:
        out *= -mp.mpf(c)/Q0 + mp.mpf(d)
    return out


def chain_std_zb(chain):
    a, b = mp.mpf(0), mp.mpf(1)
    for c, d in chain:
        cm, dm = mp.mpf(c), mp.mpf(d)
        a, b = a*(cm*H_A + dm) + b*cm, a*cm + b*dm
    return z_m * a + b


def chain_det(chain):
    D = mp.mpf(1)
    for c, d in chain:
        cm, dm = mp.mpf(c), mp.mpf(d)
        D *= (dm*(cm*H_A + dm) - cm*cm)
    return D


def per_gen_chains(Z, N, include_inter=True, include_intra=True):
    A = Z + N
    n_gens = max(1, 3*A - 1)
    ordering = ['p']*Z + ['n']*N
    gens = [[] for _ in range(n_gens)]
    for k in range(A):
        chain_k = _step_chain_generic(ordering[k], ordering[:k], n_gens, include_inter=include_inter)
        intra_g_lo = 3*k; intra_g_hi = 3*k + 1
        for c, d, g in chain_k:
            is_intra = (intra_g_lo <= g <= intra_g_hi)
            if (is_intra and include_intra) or (not is_intra and include_inter):
                gens[g].append((c, d))
    return gens


def phi_inter(Z, N):
    chains_full = per_gen_chains(Z, N)
    chains_p = per_gen_chains(1, 0, include_inter=False)
    chains_n = per_gen_chains(0, 1, include_inter=False)

    def collect(chains):
        s1, s2, s3 = mp.mpf(0), mp.mpf(0), mp.mpf(0)
        for ch in chains:
            if not ch: continue
            v = chain_std_zb(ch); d = chain_det(ch)
            ls = chain_lambda_sym(ch); la = chain_lambda_alt(ch)
            if v != 0: s1 += mp.log(mp.fabs(v))
            if d != 0: s2 += mp.log(mp.fabs(d))
            if ls != 0 and la != 0: s3 += mp.log(mp.fabs(ls/la))
        return s1, s2, s3

    P1f, P2f, P3f = collect(chains_full)
    P1p, P2p, P3p = collect(chains_p)
    P1n, P2n, P3n = collect(chains_n)
    return (P1f - Z*P1p - N*P1n,
             P2f - Z*P2p - N*P2n,
             P3f - Z*P3p - N*P3n)


# ─── Occupancy models ────────────────────────────────────────────

def occupancy_models(lam, Z, N, A):
    """Return a dict of {model_name: f_lambda(Z, N)} for occupancy."""
    k = sum(lam)
    pn_pairs = min(Z, N)
    half_pairs = max(0, A - max(Z, N))  # all-paired count
    # Number of A's worth of strands per partition
    n_kgroups_in_atom = (3*A) // k if (3*A) % k == 0 else 0

    return {
        # Wigner (works for k=4)
        'wigner_min/A': pn_pairs / A if A > 0 else 0,
        # Pair count over A
        'pn_pairs/A': pn_pairs / A if A > 0 else 0,
        # Total pn pairs
        'pn_pairs': pn_pairs,
        # Per-strand-group count
        'k_groups': n_kgroups_in_atom,
        # Combinatorial Z choose ... × N choose ...
        # For pn-symmetric λ at k=2j: Z choose j × N choose j
        'binomial_zn': (1 if Z >= k//2 and N >= k//2 else 0),
        # Even-A boost (active only when Z=N)
        'zn_match': 1 if Z == N and A >= 1 else 0,
    }


# ─── Main ────────────────────────────────────────────────────────

def main() -> int:
    print("=" * 100)
    print("LEVEL-k BRANCHING: self-conjugate partitions at k = 4, 6, 8, 10, 12")
    print("=" * 100)

    # 1. Enumerate self-conjugate partitions per level
    levels = [4, 6, 8, 10, 12]
    print(f"\n  Self-conjugate partitions and q-hook products:")
    print(f"  {'k':>3} {'partition':<20} {'H_q(lambda)':>14} {'dim_q V_lambda':>18}")
    for k in levels:
        sc_lams = self_conjugate(k)
        for lam in sc_lams:
            Hq = float(hook_product_q(lam))
            dq = float(dim_q_lam(lam))
            print(f"  {k:>3} {str(lam):<20} {Hq:>14.4f} {dq:>18.4e}")
    print()

    # 2. Compute baseline (per-generator inter-only + Wigner k=4)
    delta_W_unit = me * q3 * q2**2  # k=4 Wigner unit, MeV
    AME_BIND = {'D': 2.22456612, 'T': 8.481798,
                 '³He': 7.718058, '⁴He': 28.29566}
    M_H_ATOMIC = M_P_MEV + M_E_MEV
    ISOTOPES = [
        ('D',   1, 1, 1876.12393, AME_BIND['D']),
        ('T',   1, 2, 2809.43215, AME_BIND['T']),
        ('³He', 2, 1, 2809.41347, AME_BIND['³He']),
        ('⁴He', 2, 2, 3728.40133, AME_BIND['⁴He']),
    ]

    # Print baseline (no level-k corrections beyond k=4 Wigner)
    print(f"  Baseline (per-gen inter-only Phi + k=4 Wigner only):")
    print(f"  {'iso':<6} {'binding':>10} {'D_W(k=4)':>10} "
          f"{'M_pred':>10} {'B_pred':>10} {'B_AME':>10} {'B err':>10}")
    baseline_rows = {}
    for name, Z, N, M_ref, B_ame in ISOTOPES:
        A = Z+N
        P1, P2, P3 = phi_inter(Z, N)
        binding = float(alpha_bind) * (float(P1) - 2*float(q3)*float(P2) + float(HA2)*float(P3))
        delta_W = -float(delta_W_unit) * min(Z, N) / A
        M_free = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV
        M_pred = M_free + binding + delta_W
        B_pred = -(binding + delta_W)
        err = (B_pred - B_ame) / B_ame * 100
        print(f"  {name:<6} {binding:>+10.4f} {delta_W:>+10.4f} "
              f"{M_pred:>10.4f} {B_pred:>+10.4f} {B_ame:>+10.4f} {err:>+9.2f}%")
        baseline_rows[name] = {
            'Z':Z,'N':N,'A':A,'binding':binding,'delta_W4':delta_W,
            'M_pred':M_pred,'B_pred':B_pred,'B_AME':B_ame,'M_ref':M_ref,
        }
    print()

    # 3. Try level-k corrections with PLANCHEREL-WEIGHTED normalisation
    # Naive H_q(λ) grows super-exponentially; proper weight is
    # w_λ = (dim_q V_λ)² / [k]_q!  (Plancherel measure on H_k(q))
    # Try: Δ_λ = m_e · w_λ · H_q(λ) · f  (i.e., contribution scaled by
    # algebraic weight) and Δ_λ = m_e · w_λ · f (no H_q at all).
    print(f"  Plancherel-weighted level-k corrections (suppression via [k]_q!)")
    print()

    def w_lambda(lam):
        """Algebraic Wedderburn weight w_λ = (dim_q V_λ)² / [k]_q!."""
        k = sum(lam)
        return (dim_q_lam(lam) ** 2) / q_fact(k)

    schemes = {
        'A: Δ = m_e · w_λ · f (Plancherel only)': lambda lam, f: -float(me) * float(w_lambda(lam)) * f,
        'B: Δ = m_e · w_λ · H_q(λ) · f': lambda lam, f: -float(me) * float(w_lambda(lam)) * float(hook_product_q(lam)) * f,
        'C: Δ = m_e · H_q(λ) / dim_q · f': lambda lam, f: -float(me) * float(hook_product_q(lam)) / float(dim_q_lam(lam)) * f,
    }
    # Use the simple wigner-like occupancy
    occupancy = lambda Z, N, A: min(Z, N) / A if A > 0 else 0
    all_results = {}

    for scheme_name, scheme_fn in schemes.items():
        print(f"  Scheme {scheme_name}, occupancy = min(Z,N)/A:")
        print(f"    {'iso':<6} {'k=6':>9} {'k=8':>9} {'k=10':>9} {'k=12':>9} "
              f"{'sum':>12} {'B_pred':>12} {'AME':>10} {'err %':>10}")
        rows = []
        for name, Z, N, M_ref, B_ame in ISOTOPES:
            A = Z+N
            base = baseline_rows[name]
            f = occupancy(Z, N, A)
            corrections = {}
            total = 0.0
            for k in [6, 8, 10, 12]:
                k_total = 0.0
                for lam in self_conjugate(k):
                    k_total += scheme_fn(lam, f)
                corrections[k] = k_total
                total += k_total
            B_pred_new = -(base['binding'] + base['delta_W4'] + total)
            err = (B_pred_new - B_ame) / B_ame * 100
            print(f"    {name:<6} {corrections[6]:>+9.3f} {corrections[8]:>+9.3f} "
                  f"{corrections[10]:>+9.3f} {corrections[12]:>+9.3f} "
                  f"{total:>+12.4f} {B_pred_new:>+12.4f} {B_ame:>+10.4f} {err:>+9.2f}%")
            rows.append({
                'iso': name, 'Z': Z, 'N': N, 'A': A,
                'baseline_binding': base['binding'],
                'delta_W_k4': base['delta_W4'],
                'level_k_corrections': corrections,
                'total_higher_k': total,
                'B_pred_new': B_pred_new,
                'B_AME': B_ame,
                'err_pct': err,
            })
        all_results[scheme_name] = rows
        print()

    witness = {
        'computation': 'level-k-branching',
        'description': (
            'Generalize Wigner (2,2)|-4 to higher Hecke levels by '
            'summing self-conjugate partitions at k=6,8,10,12 with '
            'q-hook product H_q(lambda) and various occupancy models '
            'f_lambda(Z,N).  Tests whether bridging D, 4He sign flip '
            'is feasible via richer partition spectrum.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'self_conjugate_catalogue': {
            str(k): [{'lambda': list(lam),
                       'H_q': float(hook_product_q(lam)),
                       'dim_q': float(dim_q_lam(lam))}
                      for lam in self_conjugate(k)]
            for k in levels
        },
        'baselines': {n: {k: float(v) if not isinstance(v, str) else v
                            for k, v in r.items()}
                       for n, r in baseline_rows.items()},
        'model_results': all_results,
    }
    out = Path(__file__).parent / "level-k-branching.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
