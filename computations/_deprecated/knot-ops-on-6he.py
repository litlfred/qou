#!/usr/bin/env python3
"""
Act each knot operator on 6He via Frobenius dual (G^{-1}).

For each torus knot T_{m,n} in the building block table:
  1. Compute NF(T_{m,n}) in H_3(q)
  2. Compute the Frobenius dual T_{m,n}^vee = NF . G^{-1}
  3. Act on NF(6He) by right multiplication: NF(6He . T^vee)
  4. Decompose result - NF(6Li) = emitted particles
  5. Extract Q-value candidates

Usage:
    cd computations && python3 knot-ops-on-6he.py
"""
import math
import json
import sys
import numpy as np
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q, Q_INV as qi, HA as h, HBAR_Q, LN_Q
# z/NF_BASIS/TR_M now owned by pyhecke.gram (M2b inversion). Keep local
# bootstrap for dev mode; the installed-pyhecke path is preferred.
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[2] / "tools" / "pyhecke" / "python"))
from pyhecke.gram import z as _PG_Z, NF_BASIS as _PG_NF_BASIS, TR_M as _PG_TR_M  # noqa: E402


z = _PG_Z  # moved to pyhecke.gram
m_e = 0.51099895
E_cross = 0.5 * h
mu_0 = m_e / (3 * E_cross)

NF_BASIS = _PG_NF_BASIS  # moved to pyhecke.gram
NF_NAMES = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
TR_M = list(_PG_TR_M)  # moved to pyhecke.gram
def hecke_mul(t1, t2):
    r = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            r[w] = r.get(w, 0.0) + c1 * c2
    return {w: c for w, c in r.items() if abs(c) > 1e-15}


def reduce_nf(terms):
    changed = True
    while changed:
        changed = False
        new = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False
            for p in range(len(word) - 1):
                if word[p] == word[p + 1]:
                    pre, suf = word[:p], word[p + 2:]
                    new[pre + (word[p],) + suf] = new.get(pre + (word[p],) + suf, 0) + coeff * h
                    new[pre + suf] = new.get(pre + suf, 0) + coeff
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
                        new[nw] = new.get(nw, 0) + coeff
                        done = changed = True
                        break
            if not done:
                new[word] = new.get(word, 0) + coeff
        terms = {w: c for w, c in new.items() if abs(c) > 1e-15}
    return terms


def to_vec(t):
    return np.array([t.get(b, 0.0) for b in NF_BASIS])


def from_vec(v):
    return {NF_BASIS[i]: v[i] for i in range(6) if abs(v[i]) > 1e-15}


def markov_trace(v):
    return sum(v[i] * TR_M[i] for i in range(6))


def nf_of_word(word):
    """NF of a braid word (tuple of generator indices)."""
    terms = {tuple(word): 1.0}
    return to_vec(reduce_nf(terms))


def nf_of_inverse_word(word):
    """NF of word with negative entries meaning inverses.
    sigma_i^{-1} = sigma_i - h."""
    terms = {(): 1.0}
    for g in word:
        if g >= 0:
            factor = {(g,): 1.0}
        else:
            i = -g - 1
            factor = {(i,): 1.0, (): -h}
        terms = hecke_mul(terms, factor)
        terms = reduce_nf(terms)
    return to_vec(terms)


# ══════════════════════════════════════════════════════════════════
#  GRAM MATRIX
# ══════════════════════════════════════════════════════════════════

G = np.zeros((6, 6))
for i in range(6):
    for j in range(6):
        prod = hecke_mul({NF_BASIS[i]: 1.0}, {NF_BASIS[j]: 1.0})
        nf = reduce_nf(prod)
        vec = to_vec(nf)
        G[i, j] = markov_trace(vec)

G_inv = np.linalg.inv(G)


def frobenius_dual(v):
    """K^vee = v . G^{-1}"""
    return v @ G_inv


def act_dual_right(nucleus_vec, operator_vec):
    """NF(nucleus . operator^vee) where operator^vee = operator . G^{-1}."""
    dual = frobenius_dual(operator_vec)
    prod = hecke_mul(from_vec(nucleus_vec), from_vec(dual))
    return to_vec(reduce_nf(prod))


def act_dual_left(nucleus_vec, operator_vec):
    """NF(operator^vee . nucleus)."""
    dual = frobenius_dual(operator_vec)
    prod = hecke_mul(from_vec(dual), from_vec(nucleus_vec))
    return to_vec(reduce_nf(prod))


# ══════════════════════════════════════════════════════════════════
#  6He and 6Li GROUND STATES
# ══════════════════════════════════════════════════════════════════

def chain_V(ordering, gen):
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


def find_gs(Z, N):
    from itertools import combinations
    A = Z + N
    best = (float('inf'), None)
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
        if ok and Phi < best[0]:
            best = (Phi, o[:])
    return best[1], best[0]


def nuclear_nf(ordering):
    A = len(ordering)
    if A <= 1:
        return np.array([1.0, 0, 0, 0, 0, 0])
    current = {(): 1.0}
    for i in range(A - 1):
        if ordering[i] != ordering[i + 1]:
            current = hecke_mul(current, {(i % 2,): 1.0})
            current = reduce_nf(current)
    return to_vec(current)


gs_6he, phi_6he = find_gs(2, 4)
gs_6li, phi_6li = find_gs(3, 3)
nf_6he = nuclear_nf(gs_6he)
nf_6li = nuclear_nf(gs_6li)

print(f"q = {q:.10f}, h = {h:.10f}, z = {z:.10f}")
print(f"\n6He GS = {gs_6he}, Phi = {phi_6he:+.4f}")
print(f"  NF = [{', '.join(f'{v:+.4f}' for v in nf_6he)}]")
print(f"  tr_M = {markov_trace(nf_6he):.8f}")
print(f"\n6Li GS = {gs_6li}, Phi = {phi_6li:+.4f}")
print(f"  NF = [{', '.join(f'{v:+.4f}' for v in nf_6li)}]")
print(f"  tr_M = {markov_trace(nf_6li):.8f}")
print(f"\nQ_exp = 3.508 MeV")


# ══════════════════════════════════════════════════════════════════
#  ALL KNOT OPERATORS
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("  KNOT OPERATORS AND THEIR FROBENIUS DUALS")
print("=" * 80)

# Build all knot operators as NF vectors in H_3(q)
# Positive generators: sigma_0 = 0, sigma_1 = 1
# Negative (inverse): -1 = sigma_0^{-1}, -2 = sigma_1^{-1}

KNOTS = [
    ("identity",        [],                      "1 (photon)"),
    ("T_{2,1}",         [0],                     "sigma_0 (up quark)"),
    ("T_{2,1}^inv",     [-1],                    "sigma_0^{-1} (down quark)"),
    ("T_{2,2} Hopf",    [0, 0],                  "sigma_0^2 (Hopf link)"),
    ("T_{2,3} trefoil", [0, 1, 0],               "e^- (electron)"),
    ("T_{2,3}^inv",     [-1, -2, -1],            "e^+ (positron)"),
    ("T_{2,4}",         [0, 1, 0, 0],            "4-crossing torus"),
    ("T_{2,5} cinque",  [0, 1, 0, 1, 0],         "mu^- (muon)"),
    ("T_{2,5}^inv",     [-1, -2, -1, -2, -1],    "mu^+ (antimuon)"),
    ("T_{3,4}",         [0, 1, 0, 1, 0, 0, 1, 0],"Hopf^2 color"),
    ("T_{2,7} septa",   [0, 1, 0, 1, 0, 1, 0],   "tau^- (tau)"),
    ("T_{3,5}",         [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], "weak force"),
    ("T_beta",          None,                     "L+ - h*sigma_0"),
    ("Borromean",       None,                     "sig0 sig1^-1 sig0 sig1^-1 sig0 sig1^-1"),
    ("Figure-8",        None,                     "(trefoil . antitrefoil)"),
]

knot_data = {}
for name, word, desc in KNOTS:
    if name == "T_beta":
        vec = np.array([0.0, -h, 0.0, 1.0, 0.0, 0.0])
    elif name == "Borromean":
        vec = nf_of_inverse_word([0, -2, 0, -2, 0, -2])
    elif name == "Figure-8":
        # trefoil . antitrefoil = (0,1,0) . (-1,-2,-1)
        trefoil = {(0, 1, 0): 1.0}
        anti = nf_of_inverse_word([-1, -2, -1])
        prod = hecke_mul(trefoil, from_vec(anti))
        vec = to_vec(reduce_nf(prod))
    elif word is not None and len(word) == 0:
        vec = np.array([1.0, 0, 0, 0, 0, 0])
    elif word is not None:
        has_neg = any(g < 0 for g in word)
        if has_neg:
            vec = nf_of_inverse_word(word)
        else:
            vec = nf_of_word(word)
    else:
        continue

    dual = frobenius_dual(vec)
    tr = markov_trace(vec)
    tr_dual = markov_trace(dual)

    knot_data[name] = {
        'vec': vec, 'dual': dual,
        'tr': tr, 'tr_dual': tr_dual,
        'desc': desc,
    }

    print(f"\n  {name} ({desc})")
    print(f"    NF   = [{', '.join(f'{v:+.4f}' for v in vec)}]  tr={tr:+.6f}")
    print(f"    Dual = [{', '.join(f'{v:+.4f}' for v in dual)}]  tr={tr_dual:+.6f}")


# ══════════════════════════════════════════════════════════════════
#  ACT EACH KNOT ON 6He VIA DUAL
# ══════════════════════════════════════════════════════════════════

print("\n" + "=" * 80)
print("  ACT EACH KNOT OPERATOR ON 6He VIA FROBENIUS DUAL")
print("=" * 80)
print(f"  6He NF = [{', '.join(f'{v:+.4f}' for v in nf_6he)}]")
print(f"  6Li NF = [{', '.join(f'{v:+.4f}' for v in nf_6li)}]")
print(f"  Q_exp = 3.508 MeV")

E_gram = z**2 * m_e
E_shell = HBAR_Q * E_cross * mu_0

results = []

for name, kd in knot_data.items():
    vec = kd['vec']
    dual = kd['dual']

    # Right action: NF(6He . K^vee)
    result_R = act_dual_right(nf_6he, vec)
    tr_R = markov_trace(result_R)
    emitted_R = result_R - nf_6li

    # Left action: NF(K^vee . 6He)
    result_L = act_dual_left(nf_6he, vec)
    tr_L = markov_trace(result_L)
    emitted_L = result_L - nf_6li

    # Q-value candidates (multiple formulas)
    # (a) e- coefficient * z^2 * m_e
    Q_e_R = abs(result_R[5]) * E_gram
    Q_e_L = abs(result_L[5]) * E_gram

    # (b) Frobenius norm of emitted * z^2 * m_e
    frob_R2 = emitted_R @ G @ emitted_R
    frob_R = math.sqrt(abs(frob_R2))
    Q_frob_R = frob_R * E_gram

    frob_L2 = emitted_L @ G @ emitted_L
    frob_L = math.sqrt(abs(frob_L2))
    Q_frob_L = frob_L * E_gram

    # (c) |tr_M(result) - tr_M(6Li)| * m_e
    Q_tr_R = abs(tr_R - markov_trace(nf_6li)) * m_e
    Q_tr_L = abs(tr_L - markov_trace(nf_6li)) * m_e

    # (d) shell formula: |log_q(tr)| * hbar_q * E_cross * mu_0
    Q_shell_R = abs(tr_R) * E_shell if abs(tr_R) > 1e-15 else 0
    Q_shell_L = abs(tr_L) * E_shell if abs(tr_L) > 1e-15 else 0

    # (e) <emitted, K>_F * m_e (Gram pairing of emitted with operator)
    gram_pair_R = abs(emitted_R @ G @ vec) * m_e
    gram_pair_L = abs(emitted_L @ G @ vec) * m_e

    r = {
        'name': name, 'desc': kd['desc'],
        'result_R': result_R, 'result_L': result_L,
        'tr_R': tr_R, 'tr_L': tr_L,
        'emitted_R': emitted_R, 'emitted_L': emitted_L,
        'Q_e_R': Q_e_R, 'Q_e_L': Q_e_L,
        'Q_frob_R': Q_frob_R, 'Q_frob_L': Q_frob_L,
        'Q_tr_R': Q_tr_R, 'Q_tr_L': Q_tr_L,
        'Q_gram_R': gram_pair_R, 'Q_gram_L': gram_pair_L,
    }
    results.append(r)

    print(f"\n{'─' * 80}")
    print(f"  {name} ({kd['desc']})")
    print(f"  RIGHT: NF(6He . K^vee)")
    print(f"    Result = [{', '.join(f'{v:+.4f}' for v in result_R)}]  tr={tr_R:+.6f}")
    print(f"    Emitted= [{', '.join(f'{v:+.4f}' for v in emitted_R)}]")
    print(f"    Q candidates:  e-={Q_e_R:.4f}  ||F||={Q_frob_R:.4f}  tr={Q_tr_R:.4f}  <em,K>={gram_pair_R:.4f}")
    print(f"  LEFT:  NF(K^vee . 6He)")
    print(f"    Result = [{', '.join(f'{v:+.4f}' for v in result_L)}]  tr={tr_L:+.6f}")
    print(f"    Emitted= [{', '.join(f'{v:+.4f}' for v in emitted_L)}]")
    print(f"    Q candidates:  e-={Q_e_L:.4f}  ||F||={Q_frob_L:.4f}  tr={Q_tr_L:.4f}  <em,K>={gram_pair_L:.4f}")


# ══════════════════════════════════════════════════════════════════
#  SUMMARY: WHICH KNOT GIVES CLOSEST Q?
# ══════════════════════════════════════════════════════════════════

Q_exp = 3.508

print("\n" + "=" * 80)
print("  SUMMARY: CLOSEST Q-VALUE BY KNOT OPERATOR")
print("=" * 80)
print(f"  Q_exp = {Q_exp:.3f} MeV")
print(f"\n  {'Knot':>18s} | {'Q_e(R)':>7s} | {'Q_F(R)':>7s} | {'Q_tr(R)':>7s} | {'Q_G(R)':>7s} | {'Q_e(L)':>7s} | {'Q_F(L)':>7s} | {'Q_tr(L)':>7s} | {'Q_G(L)':>7s}")
print(f"  {'':->115s}")

for r in results:
    print(f"  {r['name']:>18s} | {r['Q_e_R']:>7.3f} | {r['Q_frob_R']:>7.3f} | {r['Q_tr_R']:>7.3f} | {r['Q_gram_R']:>7.3f} | {r['Q_e_L']:>7.3f} | {r['Q_frob_L']:>7.3f} | {r['Q_tr_L']:>7.3f} | {r['Q_gram_L']:>7.3f}")

# Find best match across all formulas
print(f"\n  Best matches to Q_exp = {Q_exp:.3f} MeV:")
all_qs = []
for r in results:
    for key in ['Q_e_R', 'Q_e_L', 'Q_frob_R', 'Q_frob_L', 'Q_tr_R', 'Q_tr_L', 'Q_gram_R', 'Q_gram_L']:
        val = r[key]
        if val > 0.01:
            err = (val / Q_exp - 1) * 100
            all_qs.append((abs(err), r['name'], key, val, err))

all_qs.sort()
for _, name, key, val, err in all_qs[:15]:
    print(f"    {name:>18s} {key:>10s} = {val:.4f} MeV ({err:+.1f}%)")


# Witness
witness = {
    'name': 'knot-ops-on-6he',
    'timestamp': datetime.now(timezone.utc).isoformat(),
    'q': q, 'Q_exp': Q_exp,
    'nf_6he': nf_6he.tolist(),
    'nf_6li': nf_6li.tolist(),
    'knot_results': [{
        'name': r['name'],
        'Q_e_R': r['Q_e_R'], 'Q_e_L': r['Q_e_L'],
        'Q_frob_R': r['Q_frob_R'], 'Q_frob_L': r['Q_frob_L'],
        'Q_tr_R': r['Q_tr_R'], 'Q_tr_L': r['Q_tr_L'],
        'Q_gram_R': r['Q_gram_R'], 'Q_gram_L': r['Q_gram_L'],
    } for r in results],
}
out = Path(__file__).with_suffix('.witness.json')
out.write_text(json.dumps(witness, indent=2, default=float))
print(f"\n  Witness: {out.name}")
