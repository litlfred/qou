#!/usr/bin/env python3
"""
Brane tower Q-values with analytic continuation.

The Q-value at degree 0 is Q = |sum dV| * z^2 * m_e.
Higher degrees in the jet bundle contribute quantum dilogarithm
corrections. The full tower sum is:

    Q_full = |sum_k sum_i [Li_{2,q}(V_hat_i^(k)(dau)) - Li_{2,q}(V_hat_i^(k)(par))]| * z^2 * m_e

where k runs over jet bundle degrees and i over generators.

For negative vertex volumes V < 0, the q-dilogarithm requires
analytic continuation:
    Li_{2,q}(-x) = -Li_{2,q}(x/(1+x)) - (1/2) ln_q^2(1+x)

For |V| > 1, use the reflection formula:
    Li_{2,q}(1/x) = -Li_{2,q}(x) - (1/2) ln_q^2(-x) - pi^2/6

Usage:
    cd computations && python3 tower-qvalues.py
"""
import math
import json
import sys
import numpy as np
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q, Q_INV as qi, HA as h
# z/NF_BASIS/TR_M now owned by pyhecke.gram (M2b inversion). Keep local
# bootstrap for dev mode; the installed-pyhecke path is preferred.
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[2] / "tools" / "pyhecke" / "python"))
from pyhecke.gram import z as _PG_Z, NF_BASIS as _PG_NF_BASIS, TR_M as _PG_TR_M  # noqa: E402


z = _PG_Z  # moved to pyhecke.gram
m_e = 0.51099895
E_gram = z**2 * m_e

print(f"q  = {q:.10f}")
print(f"h  = {h:.10f}")
print(f"z  = {z:.10f}")
print(f"z² = {z**2:.10f}")
print(f"E_gram = z² * m_e = {E_gram:.8f} MeV")


def q_int(n):
    """[n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    if n == 0:
        return 0.0
    return (q**n - qi**n) / h


def ln_q(x):
    """q-logarithm: ln_q(x) = sum_{n=1}^inf (-1)^{n+1} (x-1)^n / [n]_q.

    Valid for |x-1| < 1 (or use standard log for general x).
    """
    if x <= 0:
        return float('nan')
    # Use standard log scaled by q-correction
    # ln_q(x) ≈ ln(x) * [correction factor]
    # For series: ln_q(1+t) = sum (-1)^{n+1} t^n / [n]_q
    if abs(x - 1) < 0.9:
        t = x - 1
        result = 0.0
        for n in range(1, 200):
            term = (-1)**(n+1) * t**n / q_int(n)
            result += term
            if abs(term) < 1e-15:
                break
        return result
    else:
        # Fall back to standard log (leading order)
        return math.log(x)


def Li2_q(x, max_terms=500):
    """Quantum dilogarithm Li_{2,q}(x) = sum_{n=1}^inf x^n / (n * [n]_q).

    Converges for |x| < 1. For |x| >= 1 or x < 0, use analytic continuation.
    """
    if abs(x) < 1e-15:
        return 0.0

    # For |x| < 1: direct series
    if abs(x) < 1.0 - 1e-10:
        result = 0.0
        for n in range(1, max_terms):
            qn = q_int(n)
            if abs(qn) < 1e-15:
                break
            term = x**n / (n * qn)
            result += term
            if abs(term) < 1e-15:
                break
        return result

    # For x < 0: analytic continuation
    # Li_2(-x) = -Li_2(x/(1+x)) - (1/2) ln^2(1+x)  (classical)
    # We adapt: Li_{2,q}(x) for x < 0
    if x < 0:
        ax = abs(x)
        if ax < 1:
            # Li_2(-ax) for ax < 1: direct series works (alternating)
            result = 0.0
            for n in range(1, max_terms):
                qn = q_int(n)
                if abs(qn) < 1e-15:
                    break
                term = x**n / (n * qn)  # x is negative, so (-ax)^n = (-1)^n ax^n
                result += term
                if abs(term) < 1e-15:
                    break
            return result
        else:
            # |x| > 1 and x < 0: use inversion
            # Li_2(1/x) = -Li_2(x) + terms
            # Better: compute via functional equation
            y = 1.0 / x  # |y| < 1
            Li2_y = Li2_q(y)
            # Classical inversion: Li_2(x) + Li_2(1/x) = -pi^2/6 - (1/2)ln^2(-x)
            # q-deformed: Li_{2,q}(x) + Li_{2,q}(1/x) ≈ -pi^2/6 - (1/2)ln_q^2(-x)
            correction = -math.pi**2 / 6 - 0.5 * math.log(abs(x))**2
            return correction - Li2_y

    # x >= 1: inversion formula
    if x > 1 + 1e-10:
        y = 1.0 / x  # 0 < y < 1
        Li2_y = Li2_q(y)
        correction = -math.pi**2 / 6 - 0.5 * math.log(x)**2
        return correction - Li2_y

    # x ≈ 1: special value Li_2(1) = pi^2/6 (classical)
    # q-deformed: Li_{2,q}(1) = sum 1/(n [n]_q)
    result = 0.0
    for n in range(1, max_terms):
        qn = q_int(n)
        if abs(qn) < 1e-15:
            break
        term = 1.0 / (n * qn)
        result += term
        if abs(term) < 1e-15:
            break
    return result


def chain_V(ordering, gen):
    """Vertex volume V_hat at generator position gen."""
    A = len(ordering)
    a, b = 0.0, 1.0
    for j in range(gen + 1, A):
        ti, tj = ordering[gen], ordering[j]
        if ti == 1 and tj == 1:
            d = 0.0
        elif ti == 0 and tj == 0:
            d = -h
        else:
            d = -h / 2
        new_a = a * h + a * d + b
        new_b = a + b * d
        a, b = new_a, new_b
    return z * a + b


def find_ground_state(Z, N):
    """Find ground state by exhaustive search."""
    from itertools import combinations
    A = Z + N
    best_Phi = float('inf')
    best_ord = None
    for pp in combinations(range(A), Z):
        o = [0] * A
        for p in pp:
            o[p] = 1
        Phi = 0.0
        ok = True
        for gen in range(A - 1):
            V = chain_V(o, gen)
            if abs(V) < 1e-300:
                ok = False
                break
            Phi += math.log(abs(V))
        if ok and Phi < best_Phi:
            best_Phi = Phi
            best_ord = o[:]
    return best_ord, best_Phi


# ══════════════════════════════════════════════════════════════════
#  VERIFY Li_{2,q} IMPLEMENTATION
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  VERIFY Li_{2,q} IMPLEMENTATION")
print("=" * 72)

test_vals = [0.1, 0.3, 0.5, 0.7, 0.9, -0.1, -0.3, -0.5, -0.9, 1.5, 2.0, -1.5]
for x in test_vals:
    val = Li2_q(x)
    # Classical Li_2 for comparison
    if abs(x) < 1:
        classical = sum(x**n / n**2 for n in range(1, 500))
    elif x > 1:
        classical = math.pi**2 / 6 - math.log(x) * math.log(1 - 1/x) - sum((1/x)**n / n**2 for n in range(1, 500))
    else:
        classical = -sum(x**n / n**2 for n in range(1, 500) if n % 2 == 1) + sum(x**n / n**2 for n in range(2, 500, 2))
    print(f"  Li_{{2,q}}({x:+.1f}) = {val:+.8f}  (classical: {classical:+.8f})")


# ══════════════════════════════════════════════════════════════════
#  TOWER Q-VALUES FOR BENCHMARK DECAYS
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  BRANE TOWER Q-VALUES WITH ANALYTIC CONTINUATION")
print("=" * 72)

decays = [
    (1, 2, 2, 1, 0.018592, '3H->3He'),
    (2, 4, 3, 3, 3.508, '6He->6Li'),
    (6, 8, 7, 7, 0.156476, '14C->14N'),
]

results = []

for Z_par, N_par, Z_dau, N_dau, Q_exp, name in decays:
    A = Z_par + N_par

    gs_par, Phi_par = find_ground_state(Z_par, N_par)
    gs_dau, Phi_dau = find_ground_state(Z_dau, N_dau)

    V_par = [chain_V(gs_par, i) for i in range(A - 1)]
    V_dau = [chain_V(gs_dau, i) for i in range(A - 1)]

    print(f"\n{'━' * 72}")
    print(f"  {name}")
    print(f"  Parent GS:   {gs_par}")
    print(f"  Daughter GS: {gs_dau}")
    print(f"{'━' * 72}")

    # Show vertex volumes
    print(f"\n  {'Gen':>5s} | {'V_par':>10s} | {'V_dau':>10s} | {'dV':>10s}")
    print(f"  {'':->45s}")
    for i in range(A - 1):
        print(f"  {i:>5d} | {V_par[i]:>+10.6f} | {V_dau[i]:>+10.6f} | {V_dau[i]-V_par[i]:>+10.6f}")

    # Degree 0: vertex volume difference
    sum_dV_0 = sum(V_dau[i] - V_par[i] for i in range(A - 1))
    Q_deg0 = abs(sum_dV_0) * E_gram

    # Degree 1: Li_{2,q}(V_hat)
    Li2_par_1 = [Li2_q(V_par[i]) for i in range(A - 1)]
    Li2_dau_1 = [Li2_q(V_dau[i]) for i in range(A - 1)]
    sum_dLi2_1 = sum(Li2_dau_1[i] - Li2_par_1[i] for i in range(A - 1))

    print(f"\n  Degree 1: Li_{{2,q}}(V_hat)")
    print(f"  {'Gen':>5s} | {'Li2(V_par)':>12s} | {'Li2(V_dau)':>12s} | {'dLi2':>12s}")
    print(f"  {'':->50s}")
    for i in range(A - 1):
        print(f"  {i:>5d} | {Li2_par_1[i]:>+12.6f} | {Li2_dau_1[i]:>+12.6f} | {Li2_dau_1[i]-Li2_par_1[i]:>+12.6f}")

    # Degree 2: Li_{2,q}(V_hat^2)
    V_par_sq = [V_par[i]**2 for i in range(A - 1)]
    V_dau_sq = [V_dau[i]**2 for i in range(A - 1)]
    Li2_par_2 = [Li2_q(V_par_sq[i]) for i in range(A - 1)]
    Li2_dau_2 = [Li2_q(V_dau_sq[i]) for i in range(A - 1)]
    sum_dLi2_2 = sum(Li2_dau_2[i] - Li2_par_2[i] for i in range(A - 1))

    # Degree 3: Li_{2,q}(V_hat^3) — truncated by Sigma_4
    V_par_cb = [V_par[i]**3 for i in range(A - 1)]
    V_dau_cb = [V_dau[i]**3 for i in range(A - 1)]
    Li2_par_3 = [Li2_q(V_par_cb[i]) for i in range(A - 1)]
    Li2_dau_3 = [Li2_q(V_dau_cb[i]) for i in range(A - 1)]
    sum_dLi2_3 = sum(Li2_dau_3[i] - Li2_par_3[i] for i in range(A - 1))

    # Total tower
    tower_0 = sum_dV_0
    tower_01 = sum_dV_0 + sum_dLi2_1
    tower_012 = sum_dV_0 + sum_dLi2_1 + sum_dLi2_2
    tower_0123 = sum_dV_0 + sum_dLi2_1 + sum_dLi2_2 + sum_dLi2_3

    Q_0 = abs(tower_0) * E_gram
    Q_01 = abs(tower_01) * E_gram
    Q_012 = abs(tower_012) * E_gram
    Q_0123 = abs(tower_0123) * E_gram

    print(f"\n  Tower accumulation:")
    print(f"  {'Level':>12s} | {'Sum':>12s} | {'Q (MeV)':>10s} | {'Error':>8s}")
    print(f"  {'':->50s}")
    for label, tval, qval in [
        ('deg 0', tower_0, Q_0),
        ('deg 0+1', tower_01, Q_01),
        ('deg 0+1+2', tower_012, Q_012),
        ('deg 0+1+2+3', tower_0123, Q_0123),
    ]:
        err = (qval / Q_exp - 1) * 100 if Q_exp and qval > 1e-15 else float('nan')
        print(f"  {label:>12s} | {tval:>+12.6f} | {qval:>10.6f} | {err:>+7.1f}%")

    print(f"\n  CODATA Q_exp = {Q_exp:.6f} MeV")

    # Also try: Phi difference (log product of volumes)
    dPhi = Phi_dau - Phi_par
    Q_phi = abs(dPhi) * m_e
    print(f"  dPhi = {dPhi:+.8f}, Q_phi = |dPhi| * m_e = {Q_phi:.6f} MeV ({(Q_phi/Q_exp-1)*100:+.1f}%)")

    # Try: exp(dPhi) - 1
    Q_exp_phi = abs(math.exp(dPhi) - 1) * m_e
    print(f"  |exp(dPhi)-1| * m_e = {Q_exp_phi:.6f} MeV ({(Q_exp_phi/Q_exp-1)*100:+.1f}%)")

    results.append({
        'name': name,
        'Q_exp': Q_exp,
        'Q_deg0': Q_0, 'Q_deg01': Q_01, 'Q_deg012': Q_012, 'Q_deg0123': Q_0123,
        'Q_phi': Q_phi, 'dPhi': dPhi,
        'sum_dV': sum_dV_0, 'sum_dLi2_1': sum_dLi2_1,
        'sum_dLi2_2': sum_dLi2_2, 'sum_dLi2_3': sum_dLi2_3,
    })


# ══════════════════════════════════════════════════════════════════
#  ALTERNATIVE: GRAM MATRIX ON Li2 VECTORS
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  ALTERNATIVE: PER-GENERATOR Li2 AS COORDINATES")
print("=" * 72)
print("  Instead of summing Li2 differences, treat the Li2 values")
print("  as coordinates and compute the Gram-weighted norm of the")
print("  difference vector.")

# NF basis and Gram matrix (from Hecke algebra)
NF_BASIS = _PG_NF_BASIS  # moved to pyhecke.gram
NF_NAMES = ["gamma", "sigma0", "sigma1", "L+", "L-", "e-"]
TR_M = list(_PG_TR_M)  # moved to pyhecke.gram
def hecke_mul(t1, t2):
    result = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            result[w] = result.get(w, 0.0) + c1 * c2
    return {w: c for w, c in result.items() if abs(c) > 1e-15}


def reduce_nf(terms):
    changed = True
    while changed:
        changed = False
        new_terms = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1]:
                    pre, suf = word[:pos], word[pos + 2:]
                    w1 = pre + (word[pos],) + suf
                    w2 = pre + suf
                    new_terms[w1] = new_terms.get(w1, 0.0) + coeff * h
                    new_terms[w2] = new_terms.get(w2, 0.0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and abs(a - b) == 1:
                    new_trip = (b, a, b)
                    if new_trip < (a, b, a):
                        nw = word[:pos] + new_trip + word[pos + 3:]
                        new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                        done = changed = True
                        break
            if not done:
                new_terms[word] = new_terms.get(word, 0.0) + coeff
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms


def to_vec(terms):
    return np.array([terms.get(b, 0.0) for b in NF_BASIS])


def markov_trace(v):
    return sum(v[i] * TR_M[i] for i in range(6))


G = np.zeros((6, 6))
for i in range(6):
    for j in range(6):
        prod = hecke_mul({NF_BASIS[i]: 1.0}, {NF_BASIS[j]: 1.0})
        nf = reduce_nf(prod)
        vec = to_vec(nf)
        G[i, j] = markov_trace(vec)


def nuclear_nf_full(ordering):
    A = len(ordering)
    if A <= 1:
        return np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    current = {(): 1.0}
    for i in range(A - 1):
        if ordering[i] != ordering[i + 1]:
            gen = i % 2
            current = hecke_mul(current, {(gen,): 1.0})
            current = reduce_nf(current)
    return to_vec(current)


for Z_par, N_par, Z_dau, N_dau, Q_exp, name in decays:
    gs_par, _ = find_ground_state(Z_par, N_par)
    gs_dau, _ = find_ground_state(Z_dau, N_dau)

    nf_par = nuclear_nf_full(gs_par)
    nf_dau = nuclear_nf_full(gs_dau)
    delta = nf_dau - nf_par

    # Gram-weighted norm
    frob2 = delta @ G @ delta
    frob = math.sqrt(abs(frob2))
    sign = "+" if frob2 >= 0 else "-"

    Q_frob = frob * E_gram
    err = (Q_frob / Q_exp - 1) * 100

    print(f"\n  {name}:")
    print(f"    NF(par)  = [{', '.join(f'{v:+.4f}' for v in nf_par)}]")
    print(f"    NF(dau)  = [{', '.join(f'{v:+.4f}' for v in nf_dau)}]")
    print(f"    delta    = [{', '.join(f'{v:+.4f}' for v in delta)}]")
    print(f"    delta.G.delta = {frob2:+.8f} ({sign}definite)")
    print(f"    ||delta||_F = {frob:.8f}")
    print(f"    Q_frob = {Q_frob:.6f} MeV (exp: {Q_exp:.6f}, err: {err:+.1f}%)")


# ══════════════════════════════════════════════════════════════════
#  SUMMARY
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("  SUMMARY TABLE")
print("=" * 72)

print(f"\n  {'Decay':>12s} | {'Q_exp':>8s} | {'deg0':>8s} | {'deg01':>8s} | {'deg012':>8s} | {'||dNF||':>8s} | {'dPhi':>8s}")
print(f"  {'':->72s}")
for r in results:
    print(f"  {r['name']:>12s} | {r['Q_exp']:>8.4f} | {r['Q_deg0']:>8.4f} | {r['Q_deg01']:>8.4f} | {r['Q_deg012']:>8.4f} | {'---':>8s} | {r['Q_phi']:>8.4f}")


# Witness
witness = {
    'name': 'tower-qvalues',
    'timestamp': datetime.now(timezone.utc).isoformat(),
    'q': q, 'E_gram': E_gram,
    'results': [{
        'name': r['name'], 'Q_exp': r['Q_exp'],
        'Q_deg0': r['Q_deg0'], 'Q_deg01': r['Q_deg01'],
        'Q_deg012': r['Q_deg012'], 'Q_deg0123': r['Q_deg0123'],
        'Q_phi': r['Q_phi'], 'dPhi': r['dPhi'],
    } for r in results],
}
out = Path(__file__).with_suffix('.witness.json')
out.write_text(json.dumps(witness, indent=2, default=float))
print(f"\n  Witness: {out.name}")
