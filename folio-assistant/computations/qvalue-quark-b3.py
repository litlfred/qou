#!/usr/bin/env python3
"""
Quark-level Q-value with B₃ confinement — symbolic in q.

Each nucleon is a Borromean triple of quarks:
  proton  p = (u, u, d)  — 3 quarks, confined by B₃
  neutron n = (u, d, d)  — 3 quarks, confined by B₃

The typed crossing operator at the QUARK level:
  C(u,u) = σ              (d = 0)
  C(d,d) = σ - (q-q⁻¹)    (d = -(q-q⁻¹))
  C(u,d) = σ - ½(q-q⁻¹)   (d = -½(q-q⁻¹))

For A nucleons → 3A quark strands.
The Garside staircase builds all C(3A, 2) pairwise crossings.

B₃ confinement enters through the ORDERING: quarks within each
nucleon are grouped together: [u,u,d, u,d,d, ...] not interleaved.

All coefficients symbolic in q via sympy. Evaluated at q₀ only
at the end. CODATA values from experimental_constants.py with
uncertainties.

Usage:
    cd folio-assistant/computations && python3 qvalue-quark-b3.py
"""
import sys
import sympy as sp
from pathlib import Path
from itertools import combinations
import time
import math

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0, Q_ERR, VOL_FIGURE_EIGHT, MASS_RATIO_MU_E
from experimental_constants import (
    M_E_MEV, M_E_MEV_ERR,
    Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR,
    M_N_MINUS_P_MEV, M_N_MINUS_P_MEV_ERR,
)

# Symbolic q
q = sp.Symbol('q', positive=True)
HA = q - 1/q


def crossing_d(fi, fj):
    """Quark-level typed crossing coefficient, symbolic in q.
    fi, fj in {'u', 'd'}.
    """
    if fi == 'u' and fj == 'u':
        return sp.Integer(0)
    elif fi == 'd' and fj == 'd':
        return -(q - 1/q)
    else:  # u-d or d-u
        return -(q - 1/q) / 2


# ══════════════════════════════════════════════════════════════
#  SYMBOLIC HECKE ENGINE
# ══════════════════════════════════════════════════════════════

def hecke_mul(t1, t2):
    r = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            r[w] = r.get(w, sp.Integer(0)) + c1 * c2
    return {w: sp.expand(c) for w, c in r.items() if c != 0}


def reduce_nf(terms, max_iter=100000):
    changed = True
    its = 0
    while changed:
        changed = False
        its += 1
        if its > max_iter:
            break
        new = {}
        for word, coeff in terms.items():
            if coeff == 0:
                continue
            done = False
            for p in range(len(word) - 1):
                if word[p] == word[p + 1]:
                    pre, suf = word[:p], word[p + 2:]
                    w1 = pre + (word[p],) + suf
                    w2 = pre + suf
                    new[w1] = new.get(w1, sp.Integer(0)) + sp.expand(coeff * HA)
                    new[w2] = new.get(w2, sp.Integer(0)) + sp.expand(coeff)
                    done = changed = True
                    break
            if done:
                continue
            for p in range(len(word) - 2):
                a, b, c = word[p], word[p + 1], word[p + 2]
                if a == c and abs(a - b) == 1:
                    nt = (b, a, b)
                    if nt < (a, b, c):
                        nw = word[:p] + nt + word[p + 3:]
                        new[nw] = new.get(nw, sp.Integer(0)) + coeff
                        done = changed = True
                        break
            if done:
                continue
            for p in range(len(word) - 1):
                if word[p] > word[p + 1] and abs(word[p] - word[p + 1]) > 1:
                    nw = word[:p] + (word[p + 1], word[p]) + word[p + 2:]
                    new[nw] = new.get(nw, sp.Integer(0)) + coeff
                    done = changed = True
                    break
            if not done:
                new[word] = new.get(word, sp.Integer(0)) + coeff
        terms = {w: sp.expand(c) for w, c in new.items() if c != 0}
    return terms


def build_garside_quark(quark_types):
    """Build typed Garside element at quark level.

    quark_types: list of 'u' or 'd' for each quark strand.
    Garside staircase (canonical right-to-left sweep).
    """
    n_strands = len(quark_types)
    result = {(): sp.Integer(1)}
    for level in range(n_strands - 1):
        for sweep in range(level, -1, -1):
            d = crossing_d(quark_types[sweep], quark_types[level + 1])
            factor = {(sweep,): sp.Integer(1)}
            if d != 0:
                factor[()] = d
            result = hecke_mul(result, factor)
            result = reduce_nf(result)
        if len(result) > 50000:
            print(f"    WARNING: {len(result)} terms at level {level}, truncating")
            break
    return result


def nucleon_to_quarks(ordering):
    """Expand nucleon ordering to quark ordering.
    p = (u, u, d), n = (u, d, d).
    """
    quarks = []
    for t in ordering:
        if t == 1:  # proton
            quarks.extend(['u', 'u', 'd'])
        else:  # neutron
            quarks.extend(['u', 'd', 'd'])
    return quarks


def l1_at(terms, q_val):
    """Evaluate L1 = Σ|c_w(q_val)| at a specific q."""
    total = 0.0
    for c in terms.values():
        val = complex(c.subs(q, q_val))
        total += abs(val)
    return total


# ══════════════════════════════════════════════════════════════
#  GROUND STATE SEARCH (numerical, fast)
# ══════════════════════════════════════════════════════════════

def find_gs(Z, N):
    """Find GS ordering by minimizing Φ (numerical)."""
    A = Z + N
    h_num = Q0 - 1.0 / Q0
    z_num = 1.0 / (Q0**0.5 + Q0**(-0.5))

    def vertex_vol(ordering, gen):
        a, b = 0.0, 1.0
        for j in range(gen + 1, len(ordering)):
            ti, tj = ordering[gen], ordering[j]
            if ti == 1 and tj == 1:
                d = 0.0
            elif ti == 0 and tj == 0:
                d = -h_num
            else:
                d = -h_num / 2
            new_a = a * h_num + a * d + b
            new_b = a + b * d
            a, b = new_a, new_b
        return z_num * a + b

    best = (float('inf'), None)
    for pp in combinations(range(A), Z):
        o = [0] * A
        for p in pp:
            o[p] = 1
        Phi = 0.0
        ok = True
        for gen in range(A - 1):
            V = vertex_vol(o, gen)
            if abs(V) < 1e-300:
                ok = False
                break
            Phi += math.log(abs(V))
        if ok and Phi < best[0]:
            best = (Phi, o[:])
    return best[1]


# ══════════════════════════════════════════════════════════════
#  MAIN: QUARK-LEVEL Q-VALUE
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("QUARK-LEVEL Q-VALUE WITH B₃ CONFINEMENT (symbolic in q)")
    print(f"q₀ = {Q0:.15f} ± {Q_ERR:.2e}")
    print(f"  from Vol(4₁) = {VOL_FIGURE_EIGHT}")
    print(f"  and m_μ/m_e = {MASS_RATIO_MU_E} (CODATA 2022)")
    print(f"m_e = {M_E_MEV} ± {M_E_MEV_ERR} MeV (CODATA 2022)")
    print(f"All computation symbolic in q, evaluated at q₀ at the end.")
    print(f"="*70)

    # Start with A=3 (tritium) — 9 quark strands, C(9,2) = 36 crossings
    # This is tractable symbolically.

    decays = [
        ('3H→3He', 1, 2, Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR),
    ]

    for name, Z, N, Q_exp, Q_exp_err in decays:
        A = Z + N
        t0 = time.time()

        print(f"\n{'━'*70}")
        print(f"  {name}: Z={Z}, N={N}, A={A}")
        print(f"  3A = {3*A} quark strands, C({3*A},2) = {3*A*(3*A-1)//2} crossings")

        # Find GS at nucleon level
        gs_nuc = find_gs(Z, N)
        print(f"  Nucleon GS: {gs_nuc}")

        # Expand to quarks
        quarks_par = nucleon_to_quarks(gs_nuc)
        print(f"  Quark ordering: {quarks_par}")

        # Build parent Garside NF (symbolic)
        print(f"  Building parent Garside NF ({3*A*(3*A-1)//2} crossings)...")
        N_par = build_garside_quark(quarks_par)
        n_terms = len(N_par)
        L1_par = l1_at(N_par, Q0)
        elapsed = time.time() - t0
        print(f"  Parent: {n_terms} terms, L1(q₀) = {L1_par:.10f}, {elapsed:.1f}s")

        if n_terms > 50000:
            print(f"  TOO MANY TERMS — skipping daughters")
            continue

        # Find neutron positions (at nucleon level)
        neutron_pos = [i for i in range(A) if gs_nuc[i] == 0]
        N_n = len(neutron_pos)

        # For each neutron: convert n→p at quark level
        # n = (u,d,d) at positions [3k, 3k+1, 3k+2]
        # p = (u,u,d) at positions [3k, 3k+1, 3k+2]
        # The change: position 3k+1 flips from d to u
        dL1s = []
        for k_idx, nuc_pos in enumerate(neutron_pos):
            quarks_dau = quarks_par[:]
            # Flip the second quark of this neutron: d → u
            quarks_dau[3 * nuc_pos + 1] = 'u'
            print(f"  Daughter k={k_idx} (nucleon {nuc_pos}, quark {3*nuc_pos+1}: d→u)...")

            t1 = time.time()
            N_dau = build_garside_quark(quarks_dau)
            L1_dau = l1_at(N_dau, Q0)
            dL1 = L1_par - L1_dau
            dL1s.append(dL1)
            print(f"    {len(N_dau)} terms, L1 = {L1_dau:.10f}, ΔL1 = {dL1:+.6f}, {time.time()-t1:.1f}s")

        # Q with parabolic weight
        qi0 = 1.0 / Q0
        qweights = [qi0**(k * (N_n - 1 - k)) for k in range(N_n)]
        Q_parab = sum(w * dl for w, dl in zip(qweights, dL1s)) * M_E_MEV
        Q_uniform = sum(dL1s) * M_E_MEV

        # Error propagation: δQ = Q × (δq₀/q₀ + δm_e/m_e)
        # First order: Q depends on q₀ through L1 evaluation
        Q_err_q = abs(Q_parab) * Q_ERR / Q0  # crude
        Q_err_me = abs(Q_parab) * M_E_MEV_ERR / M_E_MEV
        Q_pred_err = math.sqrt(Q_err_q**2 + Q_err_me**2)

        print(f"\n  Q_parabolic = {Q_parab:.6f} ± {Q_pred_err:.2e} MeV")
        print(f"  Q_uniform   = {Q_uniform:.6f} MeV")
        print(f"  Q_exp       = {Q_exp:.6f} ± {Q_exp_err:.6f} MeV (CODATA 2022)")
        print(f"  Deviation   = {Q_parab - Q_exp:+.6f} MeV ({(Q_parab/Q_exp-1)*100:+.2f}%)")

        total_elapsed = time.time() - t0
        print(f"  Total time: {total_elapsed:.1f}s")
