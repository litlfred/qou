#!/usr/bin/env python3
"""q-Collatz divergence-half probe (forward orbits) — exact Laurent arithmetic.

The cycle census (qcollatz_cycle_census.py) settled the *cycle* half through
period 18. This probe attacks the *divergence* half: iterate the Skein-Collatz
map forward from many positive Skein seeds and classify each orbit.

Skein module ℤ[q^{±1}]; Laurent poly = dict {exp:int}.  Map (partial):
  q-even  ([2]|P, i.e. P(-1)=0):   C(P)=P/[2]
  q-odd   ([2]|P+1, i.e. P(-1)=-1): C(P)=([3]P+1)/[2]
  else UNDEFINED (P not in the map's domain).
Fundamental attractor cycle: {q^{-1}, 1+q^{-1}} (q-lift of classical {1,2}).

Outcome classes per seed:
  CONVERGED     — reaches the fundamental 2-cycle.
  ESCAPE_DOMAIN — an iterate leaves the domain (P(-1) ∉ {0,-1}); C undefined.
  ROGUE_CYCLE   — revisits a non-attractor element (a NEW cycle — would be major).
  UNRESOLVED    — exceeds the step budget without any of the above.
Also records the excursion height (max L1 coeff-norm along the orbit) and the
q=3 value trajectory (a real-q>1 descent diagnostic).
"""
import sys, json
from itertools import product

TWO = {1: 1, 0: 1}          # q + 1
THREE = {2: 1, 1: 1, 0: 1}  # q^2 + q + 1
ATTR_A = {-1: 1}            # q^{-1}
ATTR_B = {-1: 1, 0: 1}     # 1 + q^{-1}


def add(a, b, sb=1):
    r = dict(a)
    for e, c in b.items():
        r[e] = r.get(e, 0) + sb * c
        if r[e] == 0:
            del r[e]
    return r


def mul(a, b):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            r[e1 + e2] = r.get(e1 + e2, 0) + c1 * c2
    return {e: c for e, c in r.items() if c != 0}


def exact_div(num, den):
    if not num:
        return {}
    nmin, dmin = min(num), min(den)
    N = {e - nmin: c for e, c in num.items()}
    D = {e - dmin: c for e, c in den.items()}
    Ndeg, Ddeg = max(N), max(D)
    if Ndeg < Ddeg:
        return None
    dlead = D[Ddeg]
    rem, quot = dict(N), {}
    for k in range(Ndeg - Ddeg, -1, -1):
        rk = rem.get(k + Ddeg, 0)
        if rk == 0:
            continue
        if rk % dlead != 0:
            return None
        qk = rk // dlead
        quot[k] = qk
        for e, c in D.items():
            rem[e + k] = rem.get(e + k, 0) - qk * c
            if rem[e + k] == 0:
                del rem[e + k]
    if rem:
        return None
    off = nmin - dmin
    return {e + off: c for e, c in quot.items()}


def eval_at(a, x):
    return sum(c * (x ** e) for e, c in a.items())  # x may be Fraction for x=-1 ok with ints


def parity(P):
    v = sum(c * ((-1) ** e) for e, c in P.items())
    if v == 0:
        return 'E'
    if v == -1:
        return 'O'
    return None


def step(P):
    p = parity(P)
    if p == 'E':
        return exact_div(P, TWO), 'E'
    if p == 'O':
        return exact_div(add(mul(THREE, P), {0: 1}), TWO), 'O'
    return None, None


def l1(P):
    return sum(abs(c) for c in P.values())


def key(P):
    return tuple(sorted(P.items()))


def positive(P):
    return bool(P) and all(c >= 0 for c in P.values())


def classify(seed, max_steps=400):
    P = dict(seed)
    seen = set()
    height = l1(P)
    val3 = [sum(c * (3 ** e) for e, c in P.items())]
    for _ in range(max_steps):
        if key(P) in (key(ATTR_A), key(ATTR_B)):
            return dict(outcome='CONVERGED', steps=_, height=height,
                        val3_start=val3[0], val3_end=val3[-1])
        if key(P) in seen:
            return dict(outcome='ROGUE_CYCLE', steps=_, height=height, P=str(P))
        seen.add(key(P))
        nxt, br = step(P)
        if nxt is None:
            return dict(outcome='ESCAPE_DOMAIN', steps=_, height=height, P=str(P))
        P = nxt
        height = max(height, l1(P))
        val3.append(sum(c * (3 ** e) for e, c in P.items()))
    return dict(outcome='UNRESOLVED', steps=max_steps, height=height, P=str(P))


def gen_seeds(exp_lo, exp_hi, cmax):
    """positive Laurent polys, support in [exp_lo,exp_hi], coeffs 0..cmax,
    nonzero, in the map domain (P(-1) ∈ {0,-1})."""
    exps = list(range(exp_lo, exp_hi + 1))
    for coeffs in product(range(cmax + 1), repeat=len(exps)):
        P = {e: c for e, c in zip(exps, coeffs) if c}
        if not P:
            continue
        if parity(P) is None:
            continue  # not in domain
        yield P


def run(exp_lo=-2, exp_hi=4, cmax=2, max_steps=400):
    from collections import Counter
    tally, escape_depth = Counter(), Counter()
    rogues, unresolved, converged = [], [], []
    max_height = 0
    max_indomain = 0  # longest in-domain prefix seen before escape
    n = 0
    for seed in gen_seeds(exp_lo, exp_hi, cmax):
        n += 1
        r = classify(seed, max_steps)
        tally[r['outcome']] += 1
        max_height = max(max_height, r['height'])
        if r['outcome'] == 'ESCAPE_DOMAIN':
            escape_depth[r['steps']] += 1
            max_indomain = max(max_indomain, r['steps'])
        elif r['outcome'] == 'CONVERGED':
            converged.append({'seed': str(seed), 'steps': r['steps']})
        elif r['outcome'] == 'ROGUE_CYCLE':
            rogues.append({'seed': str(seed), **r})
        elif r['outcome'] == 'UNRESOLVED':
            unresolved.append({'seed': str(seed), **r})
        if n % 2000 == 0:
            sys.stderr.write(f"[progress] {n} seeds, tally={dict(tally)}\n")
            sys.stderr.flush()
    return dict(seeds=n, window=[exp_lo, exp_hi], cmax=cmax, max_steps=max_steps,
                tally=dict(tally), max_excursion_height=max_height,
                escape_depth_histogram=dict(sorted(escape_depth.items())),
                max_indomain_prefix_before_escape=max_indomain,
                converged_seeds=converged,
                rogue_cycles=rogues, unresolved_sample=unresolved[:12])


if __name__ == '__main__':
    lo = int(sys.argv[1]) if len(sys.argv) > 1 else -2
    hi = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    cm = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    # sanity: the two attractor elements converge at step 0
    for a in (ATTR_A, ATTR_B):
        print("sanity", a, "->", classify(a)['outcome'])
    r = run(lo, hi, cm)
    print(json.dumps({k: v for k, v in r.items()
                      if k not in ('rogue_cycles', 'unresolved_sample')}, indent=2))
    if r['rogue_cycles']:
        print("!!! ROGUE CYCLES:", json.dumps(r['rogue_cycles'], indent=2))
    if r['unresolved_sample']:
        print("UNRESOLVED sample:", json.dumps(r['unresolved_sample'], indent=2))
    with open('qcollatz_divergence.json', 'w') as f:
        json.dump(r, f, indent=2)
