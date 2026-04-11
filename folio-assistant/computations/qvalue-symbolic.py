#!/usr/bin/env python3
"""
Symbolic Q-value from Garside NF — exact in q.

All computation is in ℤ[q, q⁻¹]. No floating point until final
evaluation at q₀. No fitting, no free parameters beyond q₀ and m_e.

The formula:
  Q(Z,N) = Σ_{k=0}^{N-1} q^{-k(N-1-k)} × ΔL1_k(q₀) × m_e

where ΔL1_k = ||N_par||₁ - ||N_dau^(k)||₁ is the L1 norm change
when the k-th neutron converts, computed from the full typed
Garside NF in H_A(q).

The typed Garside staircase:
  G(t₀,...,t_{A-1}) = Π_{level=0}^{A-2} Π_{sweep=level}^{0} C(t_sweep, t_{level+1}; σ_sweep)

with crossing coefficients:
  C(p,p) = σ           (d = 0)
  C(n,n) = σ - (q-q⁻¹) (d = -(q-q⁻¹))
  C(p,n) = σ - ½(q-q⁻¹) (d = -½(q-q⁻¹))

These are the typed crossing operators from the quark-level B₃
confinement: p = (u,u,d), n = (u,d,d), averaged over the
Borromean structure.

Usage:
    cd folio-assistant/computations && python3 qvalue-symbolic.py
"""
import sys
import sympy as sp
from pathlib import Path
from itertools import combinations
import time

sys.path.insert(0, str(Path(__file__).parent))

# Symbolic q
q = sp.Symbol('q', positive=True)
HA = q - 1/q  # q - q⁻¹

# Crossing coefficients (exact in q)
def typed_d_sym(ti, tj):
    """Typed crossing coefficient d, symbolic in q."""
    if ti == 1 and tj == 1:   # pp
        return sp.Integer(0)
    elif ti == 0 and tj == 0:  # nn
        return -HA
    else:                       # mixed
        return -HA / 2


# ══════════════════════════════════════════════════════════════
#  SYMBOLIC HECKE ENGINE (exact in q)
# ══════════════════════════════════════════════════════════════

def hecke_mul_sym(t1, t2):
    """Multiply two Hecke elements with symbolic coefficients."""
    r = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            r[w] = r.get(w, sp.Integer(0)) + c1 * c2
    return {w: sp.expand(c) for w, c in r.items() if c != 0}


def reduce_nf_sym(terms):
    """Reduce to NF with symbolic coefficients."""
    changed = True
    its = 0
    while changed:
        changed = False
        its += 1
        if its > 50000:
            print(f"  WARNING: NF reduction hit {its} iterations, {len(terms)} terms")
            break
        new = {}
        for word, coeff in terms.items():
            if coeff == 0:
                continue
            done = False
            # Hecke: σ_i² = HA·σ_i + 1
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
            # Braid: σ_iσ_jσ_i = σ_jσ_iσ_j when |i-j|=1, canonical order
            for p in range(len(word) - 2):
                a, b, c = word[p], word[p + 1], word[p + 2]
                if a == c and abs(a - b) == 1:
                    nt = (b, a, b)
                    if nt < (a, b, a):
                        nw = word[:p] + nt + word[p + 3:]
                        new[nw] = new.get(nw, sp.Integer(0)) + coeff
                        done = changed = True
                        break
            if done:
                continue
            # Far commutativity
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


def build_garside_sym(ordering):
    """Build typed Garside element with symbolic q coefficients.

    Garside staircase (right-to-left sweep = canonical order).
    """
    A = len(ordering)
    result = {(): sp.Integer(1)}
    for level in range(A - 1):
        for sweep in range(level, -1, -1):
            d = typed_d_sym(ordering[sweep], ordering[level + 1])
            factor = {(sweep,): sp.Integer(1)}
            if d != 0:
                factor[()] = d
            result = hecke_mul_sym(result, factor)
            result = reduce_nf_sym(result)
    return result


def l1_at_q0(terms, q0_val):
    """Evaluate L1 = Σ|c_w(q₀)| for an NF element."""
    return sum(abs(complex(c.subs(q, q0_val))) for c in terms.values())


def find_gs_sym(Z, N, q0_val):
    """Find ground state ordering by exhaustive search."""
    from q_parameter import Q as q0_exact
    A = Z + N
    best = (float('inf'), None)
    for pp in combinations(range(A), Z):
        o = [0] * A
        for p in pp:
            o[p] = 1
        # Use numerical vertex volumes for GS search (fast)
        h_num = q0_exact - 1.0/q0_exact
        z_num = 1.0 / (q0_exact**0.5 + q0_exact**(-0.5))
        Phi = 0.0
        ok = True
        for gen in range(A - 1):
            a, b = 0.0, 1.0
            for j in range(gen + 1, A):
                ti, tj = o[gen], o[j]
                if ti == 1 and tj == 1: d = 0.0
                elif ti == 0 and tj == 0: d = -h_num
                else: d = -h_num / 2
                new_a = a * h_num + a * d + b
                new_b = a + b * d
                a, b = new_a, new_b
            V = z_num * a + b
            if abs(V) < 1e-300:
                ok = False
                break
            Phi += abs(V).real
            Phi = sum(abs(V).real for V in [z_num * a + b])  # just use last
            # Actually compute Phi properly
        # Recompute Phi
        import math
        Phi = 0.0
        ok = True
        for gen in range(A - 1):
            a, b = 0.0, 1.0
            for j in range(gen + 1, A):
                ti, tj = o[gen], o[j]
                if ti == 1 and tj == 1: d = 0.0
                elif ti == 0 and tj == 0: d = -h_num
                else: d = -h_num / 2
                new_a = a * h_num + a * d + b
                new_b = a + b * d
                a, b = new_a, new_b
            V = z_num * a + b
            if abs(V) < 1e-300:
                ok = False
                break
            Phi += math.log(abs(V))
        if ok and Phi < best[0]:
            best = (Phi, o[:])
    return best[1]


# ══════════════════════════════════════════════════════════════
#  MAIN COMPUTATION
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    from q_parameter import Q as q0_val

    m_e = 0.510999  # MeV (calibration input)
    qi0 = 1.0 / q0_val

    decays = [
        ('3H→3He', 1, 2, 0.018592),
        ('6He→6Li', 2, 4, 3.508),
    ]

    print(f"SYMBOLIC Q-VALUE FROM GARSIDE NF (exact in q)")
    print(f"Evaluate at q₀ = {q0_val:.10f}")
    print(f"m_e = {m_e:.6f} MeV")
    print(f"No fitting, no free parameters.")
    print(f"="*70)

    for name, Z, N, Q_exp in decays:
        A = Z + N
        t0 = time.time()

        print(f"\n{'━'*70}")
        print(f"  {name}: Z={Z}, N={N}, A={A}")

        # Find GS ordering (numerical search)
        gs = find_gs_sym(Z, N, q0_val)
        print(f"  GS: {gs}")

        # Build parent Garside NF (symbolic in q)
        print(f"  Building parent Garside NF (symbolic)...")
        N_par = build_garside_sym(gs)
        n_par_terms = len(N_par)
        L1_par = l1_at_q0(N_par, q0_val)
        print(f"  Parent: {n_par_terms} terms, L1(q₀) = {L1_par:.10f}")

        # Find neutron positions
        neutron_pos = [i for i in range(A) if gs[i] == 0]
        N_n = len(neutron_pos)

        # Build each daughter (symbolic)
        dL1s = []
        for k, pos in enumerate(neutron_pos):
            dau_ord = gs[:]
            dau_ord[pos] = 1
            print(f"  Daughter k={k} (pos {pos}): {dau_ord}...")
            N_dau = build_garside_sym(dau_ord)
            L1_dau = l1_at_q0(N_dau, q0_val)
            dL1 = L1_par - L1_dau
            dL1s.append(dL1)
            print(f"    {len(N_dau)} terms, L1(q₀) = {L1_dau:.10f}, ΔL1 = {dL1:+.6f}")

        # Q with parabolic weight
        qweights = [qi0**(k * (N_n - 1 - k)) for k in range(N_n)]
        Q_parab = sum(w * dl for w, dl in zip(qweights, dL1s)) * m_e
        Q_uniform = sum(dL1s) * m_e

        elapsed = time.time() - t0

        print(f"\n  Parabolic weights: [{', '.join(f'{w:.4f}' for w in qweights)}]")
        print(f"  ΔL1: [{', '.join(f'{dl:+.4f}' for dl in dL1s)}]")
        print(f"\n  Q_parabolic = {Q_parab:.4f} MeV  ({(Q_parab/Q_exp-1)*100:+.1f}%)")
        print(f"  Q_uniform   = {Q_uniform:.4f} MeV  ({(Q_uniform/Q_exp-1)*100:+.1f}%)")
        print(f"  Q_exp       = {Q_exp:.4f} MeV")
        print(f"  Time: {elapsed:.1f}s")

        # Show a few symbolic coefficients for the parent NF
        print(f"\n  Sample symbolic NF terms (parent):")
        for w, c in sorted(N_par.items(), key=lambda x: (len(x[0]), x[0]))[:5]:
            ws = ''.join(f'σ{g}' for g in w) if w else '1'
            print(f"    {ws}: {c}")
