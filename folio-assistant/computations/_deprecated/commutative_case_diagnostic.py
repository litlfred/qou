#!/usr/bin/env python3
"""
COMMUTATIVE-CASE DIAGNOSTIC: scan q from ~1 to q_0 and track binding
contributions for each isotope to localize the D, 4He sign flip.

Hypothesis: at q=1 (commutative QOU), the chirality term H_A^2*Phi_3
vanishes (H_A → 0), and the formula reduces to alpha * (Phi_1 -
6*Phi_2).  If at q=1 all bindings are correctly bound (negative) and
the sign flips somewhere as q grows, we localize the issue to a
specific q-regime.

If even at q=1 the binding has wrong sign for D and 4He, then the
issue is structural (not q-dependent) and lies in the Phi_1 inter-
only construction itself.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

from hecke_core import _step_chain_generic
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

G_const = mp.catalan


def chain_lambda_sym(chain, q):
    qi = 1/q
    out = mp.mpf(1)
    for c, d in chain:
        out *= mp.mpf(c)*q + mp.mpf(d)
    return out


def chain_lambda_alt(chain, q):
    qi = 1/q
    out = mp.mpf(1)
    for c, d in chain:
        out *= -mp.mpf(c)*qi + mp.mpf(d)
    return out


def chain_std_zb(chain, q):
    qi = 1/q
    H_A = q - qi
    z = 1/(mp.sqrt(q) + mp.sqrt(qi))
    a, b = mp.mpf(0), mp.mpf(1)
    for c, d in chain:
        cm, dm = mp.mpf(c), mp.mpf(d)
        a, b = a*(cm*H_A + dm) + b*cm, a*cm + b*dm
    return z*a + b


def chain_det(chain, q):
    qi = 1/q
    H_A = q - qi
    D = mp.mpf(1)
    for c, d in chain:
        cm, dm = mp.mpf(c), mp.mpf(d)
        D *= (dm*(cm*H_A + dm) - cm*cm)
    return D


def per_gen_chains(Z, N):
    A = Z + N
    n_gens = max(1, 3*A - 1)
    ordering = ['p']*Z + ['n']*N
    gens = [[] for _ in range(n_gens)]
    for k in range(A):
        chain_k = _step_chain_generic(ordering[k], ordering[:k], n_gens, include_inter=True)
        for c, d, g in chain_k:
            gens[g].append((c, d))
    return gens


def per_gen_chains_intra_only(Z, N):
    """Intra-nucleon only chains (for free-constituent baseline)."""
    A = Z + N
    n_gens = max(1, 3*A - 1)
    ordering = ['p']*Z + ['n']*N
    gens = [[] for _ in range(n_gens)]
    for k in range(A):
        chain_k = _step_chain_generic(ordering[k], ordering[:k], n_gens, include_inter=False)
        intra_g_lo = 3*k; intra_g_hi = 3*k + 1
        for c, d, g in chain_k:
            if intra_g_lo <= g <= intra_g_hi:
                gens[g].append((c, d))
    return gens


def phi_inter_at_q(Z, N, q):
    """Compute (Phi_1, Phi_2, Phi_3) inter-only at parameter q.

    Note: chains use H_A = q - 1/q internally for d=-H_A primitives.
    Need to substitute properly.
    """
    # The chains depend on H_A = q - 1/q via the d values for dd, ud factors
    # (dd: d=-H_A, ud: d=-H_A/2).  We need to rebuild chains at this q.
    # _step_chain_generic uses the GLOBAL h from hecke_core which is at q_0.
    # So we need to either rebuild or substitute.
    #
    # Simpler: rebuild chains with d-values as multiples of H_A symbolic,
    # then evaluate at the desired q.  The chain structure is:
    #   uu: (1, 0)
    #   dd: (1, -H_A_q)
    #   ud: (1, -H_A_q/2)
    # We pass q to chain functions and they handle H_A internally.
    H_A_q = q - 1/q

    def substitute_chain(chain, h_q0, h_q):
        """Replace d values referring to h_q0 with values at h_q."""
        out = []
        for c, d in chain:
            d_f = float(d)
            if abs(d_f) < 1e-12:
                out.append((c, mp.mpf(0)))
            elif abs(d_f - (-float(h_q0))) < 1e-9:  # d = -h
                out.append((c, -h_q))
            elif abs(d_f - (-float(h_q0)/2)) < 1e-9:  # d = -h/2
                out.append((c, -h_q/2))
            else:
                out.append((c, mp.mpf(str(d_f))))
        return out

    # h_q0 = the H_A that was used at chain construction time
    Q0 = Q_MP  # was f64 roundtrip
    h_q0 = Q0 - 1/Q0

    chains_full = per_gen_chains(Z, N)
    chains_intra_p = per_gen_chains_intra_only(1, 0)
    chains_intra_n = per_gen_chains_intra_only(0, 1)

    def phi(chains):
        s1, s2, s3 = mp.mpf(0), mp.mpf(0), mp.mpf(0)
        for ch in chains:
            if not ch:
                continue
            ch_q = substitute_chain(ch, h_q0, H_A_q)
            v = chain_std_zb(ch_q, q); d = chain_det(ch_q, q)
            ls = chain_lambda_sym(ch_q, q); la = chain_lambda_alt(ch_q, q)
            if v != 0: s1 += mp.log(mp.fabs(v))
            if d != 0: s2 += mp.log(mp.fabs(d))
            if ls != 0 and la != 0: s3 += mp.log(mp.fabs(ls/la))
        return s1, s2, s3

    P1f, P2f, P3f = phi(chains_full)
    P1p, P2p, P3p = phi(chains_intra_p)
    P1n, P2n, P3n = phi(chains_intra_n)
    return (P1f - Z*P1p - N*P1n,
             P2f - Z*P2p - N*P2n,
             P3f - Z*P3p - N*P3n)


def main() -> int:
    print("=" * 100)
    print("COMMUTATIVE-CASE DIAGNOSTIC: q-scan of binding correction")
    print("=" * 100)
    print()

    # q values to scan
    q_values = [1.001, 1.01, 1.05, 1.10, 1.10998, 1.15, 1.20]
    ISOTOPES = [
        ('D',   1, 1),
        ('T',   1, 2),
        ('³He', 2, 1),
        ('⁴He', 2, 2),
    ]

    me = mp.mpf(str(M_E_MEV))

    for name, Z, N in ISOTOPES:
        print(f"  Isotope: {name}  (Z={Z}, N={N}, A={Z+N})")
        print(f"    {'q':<10} {'H_A²':>10} {'[3]_q':>8} "
              f"{'Φ_1':>10} {'Φ_2':>10} {'Φ_3':>10} "
              f"{'binding(MeV)':>14}")
        for q_f in q_values:
            q = mp.mpf(str(q_f))
            qi = 1/q
            HA = q - qi
            HA2 = HA*HA
            q3 = q**2 + 1 + qi**2
            alpha_b = me * 8 * G_const

            try:
                P1, P2, P3 = phi_inter_at_q(Z, N, q)
            except Exception as e:
                print(f"    {q_f:<10}  ERROR: {type(e).__name__}: {str(e)[:50]}")
                continue
            binding = float(alpha_b) * (float(P1) - 2*float(q3)*float(P2) + float(HA2)*float(P3))
            print(f"    {q_f:<10.5f} {float(HA2):>10.5f} {float(q3):>8.4f} "
                  f"{float(P1):>+10.4f} {float(P2):>+10.4f} {float(P3):>+10.4f} "
                  f"{binding:>+14.4f}")
        print()

    print("  Diagnostic: at q→1, H_A→0 and the chirality term vanishes.")
    print("  If binding stays POSITIVE (wrong sign) for D, ⁴He at q≈1,")
    print("  the issue is structural in Φ_1 inter-only, not q-dependent.")
    print()
    print("  Note: the inter-only construction subtracts free-constituent")
    print("  Φ at the SAME q.  The substitution at q≠q_0 is approximate")
    print("  (chain (c,d) values rebuilt from q_0 reference). For exact")
    print("  q-dependence study, rebuild from scratch at each q.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
