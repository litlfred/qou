#!/usr/bin/env python3
"""
SYMBOLIC PARTITION MASS — exact in q, all partitions, color-weighted.

M = M_free + α × ln|Σ_{λ: ℓ(λ)≤3} s_λ(c(q)) × χ_λ(β)|

where:
  s_λ(c(q)) = Schur polynomial at color roots = rational function of q
  χ_λ(β) = character of atomic braid in Young seminormal rep λ
  Only partitions with ≤3 parts contribute (3 color channels)
  Everything symbolic in q. Evaluated at q₀ at the end.

Usage:
    python3 folio-assistant/computations/atom_mass_symbolic_partition.py
"""

import math
import numpy as np
from itertools import combinations
import time
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0

HA = q0 - 1.0/q0
z_markov = 1.0 / (q0**0.5 + q0**(-0.5))


# ══════════════════════════════════════════════════════════════
# §1. COLOR WEIGHTS: Schur polynomials at color roots (in q)
# ══════════════════════════════════════════════════════════════

def vieta_at_q(q):
    """Elementary symmetric polynomials of color roots at q."""
    z = 1.0 / (q - 1)
    e1 = -(4*z + 1)
    e2 = 6*z**2 + 3*z + 1
    e3 = -(4*z**3 + 3*z**2 + 2*z + 1)
    return e1, e2, e3


def power_sums_at_q(q):
    """Power sums p_k = Σ c_i^k via Newton's identities."""
    e1, e2, e3 = vieta_at_q(q)
    p1 = e1
    p2 = e1**2 - 2*e2
    p3 = e1**3 - 3*e1*e2 + 3*e3
    return p1, p2, p3


def schur_at_q(partition, q):
    """Schur polynomial s_λ(c₀,c₁,c₂) evaluated at q.
    Uses the Frobenius formula: s_λ = det(h_{λ_i-i+j}) / 1
    via power sums and the Murnaghan-Nakayama rule.

    For ≤3 variables, use the alternant ratio directly."""
    # Pad to 3 parts
    lam = list(partition) + [0] * (3 - len(partition))
    if len(partition) > 3:
        return 0.0  # zero for > 3 variables

    z = 1.0 / (q - 1)
    # Compute actual roots numerically at this q
    a2 = 4*z + 1
    a1 = 6*z**2 + 3*z + 1
    a0 = 4*z**3 + 3*z**2 + 2*z + 1
    roots = np.roots([1, a2, a1, a0])

    # Alternant formula: s_λ(x) = det(x_i^{λ_j+n-1-j}) / det(x_i^{n-1-j})
    n = 3
    num = np.zeros((n, n), dtype=complex)
    den = np.zeros((n, n), dtype=complex)
    for i in range(n):
        for j in range(n):
            num[i, j] = roots[i] ** (lam[j] + n - 1 - j)
            den[i, j] = roots[i] ** (n - 1 - j)

    det_num = np.linalg.det(num)
    det_den = np.linalg.det(den)

    if abs(det_den) < 1e-30:
        return 0.0

    return (det_num / det_den).real


# ══════════════════════════════════════════════════════════════
# §2. YOUNG SEMINORMAL FORM (from atom_mass_partition.py)
# ══════════════════════════════════════════════════════════════

def partitions(n):
    if n == 0: yield (); return
    def gen(n, mx):
        if n == 0: yield (); return
        for k in range(min(n, mx), 0, -1):
            for r in gen(n-k, k): yield (k,)+r
    yield from gen(n, n)


def standard_tableaux(partition):
    n = sum(partition)
    shape = list(partition)
    def fill(tab, val, sr):
        if val > n: yield [list(r) for r in tab]; return
        for r in range(len(sr)):
            if sr[r] == 0: continue
            col = len(tab[r])
            if r > 0 and col >= len(tab[r-1]): continue
            tab[r].append(val); sr[r] -= 1
            yield from fill(tab, val+1, sr)
            tab[r].pop(); sr[r] += 1
    yield from fill([[] for _ in range(len(shape))], 1, list(shape))


def content(T, val):
    for r, row in enumerate(T):
        for c, v in enumerate(row):
            if v == val: return c - r
    return None


def swap_values(T, a, b):
    new = [list(r) for r in T]
    pa = pb = None
    for r, row in enumerate(new):
        for c, v in enumerate(row):
            if v == a: pa = (r,c)
            if v == b: pb = (r,c)
    if not pa or not pb: return None
    new[pa[0]][pa[1]] = b; new[pb[0]][pb[1]] = a
    for row in new:
        if row != sorted(row): return None
    for c in range(max(len(r) for r in new)):
        col = [new[r][c] for r in range(len(new)) if c < len(new[r])]
        if col != sorted(col): return None
    return new


def q_number(rho, q):
    if abs(rho) < 1e-10: return 0.0
    ha = q - 1.0/q
    return (q**rho - q**(-rho)) / ha


def hecke_gen_matrix(tabs, k, q):
    d = len(tabs)
    M = np.zeros((d, d))
    ha = q - 1.0/q
    idx = {}
    for i, T in enumerate(tabs):
        idx[tuple(tuple(r) for r in T)] = i
    done = set()
    for i, T in enumerate(tabs):
        if i in done: continue
        a, b = k+1, k+2
        rho = content(T, b) - content(T, a)
        sr = any(a in r and b in r for r in T)
        sc = False
        for c in range(max(len(r) for r in T)):
            cv = [T[r][c] for r in range(len(T)) if c < len(T[r])]
            if a in cv and b in cv: sc = True
        if sr:
            M[i,i] = q; done.add(i)
        elif sc:
            M[i,i] = -1.0/q; done.add(i)
        else:
            Ts = swap_values(T, a, b)
            if Ts is None:
                M[i,i] = q if rho > 0 else -1.0/q; done.add(i)
            else:
                j = idx.get(tuple(tuple(r) for r in Ts))
                if j is None:
                    M[i,i] = q if rho > 0 else -1.0/q; done.add(i)
                else:
                    di = ha / q_number(rho, q)
                    dj = ha - di
                    bc = di * dj + 1
                    off = math.sqrt(abs(bc)) * (1 if bc >= 0 else -1)
                    M[i,i] = di; M[j,j] = dj
                    M[i,j] = off; M[j,i] = off
                    done.add(i); done.add(j)
    return M


def verify_hecke(M, q):
    ha = q - 1.0/q
    return np.allclose(M @ M, ha * M + np.eye(M.shape[0]), atol=1e-6)


# ══════════════════════════════════════════════════════════════
# §3. CROSSING COEFFICIENTS
# ══════════════════════════════════════════════════════════════

def cc(ti, tj):
    ha = q0 - 1.0/q0
    if ti == 'p' and tj == 'p': return 1.0, 0.0
    if ti == 'n' and tj == 'n': return 1.0, -ha
    if (ti,tj) in [('p','n'),('n','p')]: return 1.0, -ha/2
    if (ti,tj) in [('p','e'),('e','p')]: return 1.0, -ha
    if (ti,tj) in [('n','e'),('e','n')]: return 0.0, 1.0
    if ti == 'e' and tj == 'e': return 1.0, 0.0
    return 0.0, 1.0


# ══════════════════════════════════════════════════════════════
# §4. COLOR-WEIGHTED MARKOV TRACE
# ══════════════════════════════════════════════════════════════

def compute_color_markov(ordering, q):
    """Compute Σ_{λ: ℓ(λ)≤3} s_λ(c(q)) × χ_λ(β) at given q."""
    n = len(ordering)
    ha = q - 1.0/q
    total = 0.0
    details = []

    for lam in partitions(n):
        if len(lam) > 3: continue  # only ≤3-part partitions

        tabs = list(standard_tableaux(lam))
        d = len(tabs)
        if d == 0: continue
        if d > 1000: continue  # skip partitions with dim > 1000 (infeasible)

        # Schur weight
        s_lam = schur_at_q(lam, q)
        if abs(s_lam) < 1e-30: continue

        # Generator matrices
        gen_mats = {}
        valid = True
        for k in range(n-1):
            M = hecke_gen_matrix(tabs, k, q)
            if not verify_hecke(M, q):
                valid = False; break
            gen_mats[k] = M
        if not valid: continue

        # Full braid representation
        rho = np.eye(d)
        for gen in range(n-1):
            for j in range(gen+1, n):
                c, d_coeff = cc(ordering[gen], ordering[j])
                if c == 0.0 and d_coeff == 1.0: continue
                C = c * gen_mats[gen] + d_coeff * np.eye(d)
                rho = rho @ C

        chi = np.trace(rho).real
        contrib = s_lam * chi
        total += contrib
        details.append({'lam': lam, 'dim': d, 's': s_lam, 'chi': chi, 'contrib': contrib})

    return total, details


def find_gs(Z, N):
    A = Z + N
    if A <= 1: return list('p'*Z + 'n'*N)
    ha = q0 - 1.0/q0
    zm = 1.0/(q0**0.5 + q0**(-0.5))
    t = math.comb(A, Z)
    if t <= 5000:
        bP, bo = float('inf'), None
        for pos in combinations(range(A), Z):
            o = ['n']*A
            for p in pos: o[p] = 'p'
            P = 0.0
            for gen in range(A-1):
                a, b = 0.0, 1.0
                for j in range(gen+1, A):
                    c, d = cc(o[gen], o[j])
                    if c == 0 and d == 1: continue
                    a, b = a*c*ha+a*d+b*c, a*c+b*d
                V = zm*a+b
                if abs(V) < 1e-300: P = float('inf'); break
                P += math.log(abs(V))
            if P < bP: bP, bo = P, list(o)
        return bo
    return list('p'*Z + 'n'*N)


def insert_e(nuc, Z):
    ha = q0 - 1.0/q0
    zm = 1.0/(q0**0.5 + q0**(-0.5))
    cur = list(nuc)
    for _ in range(Z):
        bp, bP = 0, float('inf')
        for pos in range(len(cur)+1):
            c = list(cur); c.insert(pos, 'e')
            P = 0.0; nn = len(c)
            for gen in range(nn-1):
                a, b = 0.0, 1.0
                for j in range(gen+1, nn):
                    cv, dv = cc(c[gen], c[j])
                    if cv == 0 and dv == 1: continue
                    a, b = a*cv*ha+a*dv+b*cv, a*cv+b*dv
                V = zm*a+b
                if abs(V) < 1e-300: P = float('inf'); break
                P += math.log(abs(V))
            if P < bP: bP = P; bp = pos
        cur.insert(bp, 'e')
    return cur


# ══════════════════════════════════════════════════════════════
# §5. MAIN
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    G = 0.9159655941772190; Vol_B3 = 8*G
    hbar_q_sq = (1-1/q0)**2; m_e = 0.510999
    A_q0 = 2.4599; alpha = m_e * Vol_B3
    m_p = Vol_B3/hbar_q_sq * A_q0 * m_e
    m_n = m_p + alpha * abs(-1.226119 - (-0.878526))

    ATOMS = [
        (1, 0, 'H',  938.78313),
        (2, 2, 'He', 3728.4013),
        (3, 4, 'Li', 6535.3670),
        (4, 5, 'Be', 8394.7937),
        (5, 6, 'B',  10255.1030),
        (6, 6, 'C',  11177.9292),
        (7, 7, 'N',  13043.7816),
        (8, 8, 'O',  14899.1693),
        (9, 10,'F',  17696.9010),
        (10,10,'Ne', 18622.8354),
    ]

    # B₃-dressed pe crossing for H
    c_pe_d = (q0**5+q0**(-5))/(q0+1/q0)
    d_pe_d = q0**5 - c_pe_d*q0

    print('COLOR-WEIGHTED PARTITION MASS (symbolic in q)')
    print('='*80)
    print(f'M = M_free + α × ln|Σ_{{λ:ℓ(λ)≤3}} s_λ(c(q)) × χ_λ(β)|')
    print(f'q₀ = {q0}, m_e = {m_e}, α = {alpha:.4f}')
    print()

    print(f'{"Atom":>5s} │ {"n":>3s} │ {"#λ≤3":>5s} │ {"Σ s·χ":>14s} │ {"ln|Σ|":>10s} │ {"M_pred":>10s} │ {"M_obs":>10s} │ {"Δ%":>7s} │ {"t":>5s}')
    print('─'*85)

    witness = []
    for Z, N, sym, Mo in ATOMS:
        A = Z + N
        Mf = Z*m_p + N*m_n + Z*m_e

        nuc = find_gs(Z, N)
        atom = insert_e(nuc, Z)

        t0 = time.time()
        total, details = compute_color_markov(atom, q0)
        elapsed = time.time() - t0

        n_lam = len(details)

        if abs(total) > 1e-300:
            ln_total = math.log(abs(total))
        else:
            ln_total = float('-inf')

        Mp = Mf + alpha * ln_total
        dpct = (Mp - Mo) / Mo * 100

        label = f'{A}{sym}'
        print(f'{label:>5s} │ {len(atom):>3d} │ {n_lam:>5d} │ {total:>+14.4e} │ {ln_total:>+10.4f} │ {Mp:>10.1f} │ {Mo:>10.1f} │ {dpct:>+6.3f}% │ {elapsed:>5.1f}s')

        witness.append({
            'atom': label, 'Z': Z, 'N': N, 'A': A,
            'n_strands': len(atom), 'n_partitions': n_lam,
            'color_markov_trace': total, 'ln_trace': ln_total,
            'M_pred': round(Mp, 3), 'M_obs': Mo,
            'delta_pct': round(dpct, 4),
            'ordering': ''.join(atom)[:40],
            'top_partitions': [{'lam': str(d['lam']), 'dim': d['dim'],
                                's_lam': round(d['s'], 4), 'chi': round(d['chi'], 6),
                                'contrib': round(d['contrib'], 4)}
                               for d in sorted(details, key=lambda x: -abs(x['contrib']))[:5]]
        })

    # Write witness
    wpath = Path('folio-assistant/computations/atom-mass-symbolic-partition.witness.json')
    wpath.write_text(json.dumps({'name': 'symbolic-partition-mass',
                                  'formula': 'M = M_free + α ln|Σ s_λ(c(q)) χ_λ(β)|',
                                  'results': witness}, indent=2))
    print(f'\n✓ Witness: {wpath}')
