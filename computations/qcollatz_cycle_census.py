#!/usr/bin/env python3
"""q-Collatz cycle census — exact integer Laurent-polynomial arithmetic.

Skein module Z[q^{±1}]; Laurent poly = dict {exp:int_coeff} (0 coeffs pruned).
Map:  q-even ([2]|P):  P/[2] ;  q-odd ([2]|P+1): ([3]P+1)/[2]
      [2]=q+1, [3]=q^2+q+1.  Parity read at q=-1 (Z[q^±]/(q+1)≅Z).

Cycle equation for a length-k parity word w (k_odd odd steps):
tracking c_i P_i = m_i P_0 + n_i (c_i=[2]^i), one gets after k steps
  ([2]^k - [3]^{k_odd}) P_0 = n_k,        (D · P_0 = n_k)
with D, n_k ∈ Z[q^{±1}].  So P_0 ∈ Z[q^{±1}] iff D | n_k exactly — a single
exact Laurent division.  Then verify self-consistency (actual parities = w,
returns).  No rational functions; exact throughout.
"""
import sys, json
from itertools import product

TWO = {1: 1, 0: 1}          # q + 1
THREE = {2: 1, 1: 1, 0: 1}  # q^2 + q + 1


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
            e = e1 + e2
            r[e] = r.get(e, 0) + c1 * c2
    return {e: c for e, c in r.items() if c != 0}


def scal_shift(a, e0):  # multiply by q^{e0}
    return {e + e0: c for e, c in a.items()}


def eval_at_minus1(a):
    return sum(c * ((-1) ** e) for e, c in a.items())


def exact_div(num, den):
    """Return quotient Laurent poly if den | num exactly in Z[q^±1], else None."""
    if not num:
        return {}  # 0/den = 0
    if not den:
        return None
    # shift both to ordinary polynomials (non-negative exponents)
    nmin = min(num); dmin = min(den)
    N = {e - nmin: c for e, c in num.items()}
    D = {e - dmin: c for e, c in den.items()}
    Ndeg = max(N); Ddeg = max(D)
    if Ndeg < Ddeg:
        return None
    dlead = D[Ddeg]
    # integer polynomial long division with exact-remainder + exact-coeff check
    rem = dict(N)
    quot = {}
    for k in range(Ndeg - Ddeg, -1, -1):
        rk = rem.get(k + Ddeg, 0)
        if rk == 0:
            continue
        if rk % dlead != 0:
            return None
        qk = rk // dlead
        quot[k] = qk
        for e, c in D.items():
            ek = e + k
            rem[ek] = rem.get(ek, 0) - qk * c
            if rem[ek] == 0:
                del rem[ek]
    if rem:
        return None  # non-zero remainder => not divisible
    # undo the shifts: quotient exponent offset = nmin - dmin
    off = nmin - dmin
    return {e + off: c for e, c in quot.items()}


def parity(P):
    v = eval_at_minus1(P)
    if v == 0:
        return 'E'
    if v == -1:
        return 'O'
    return None


def step(P, kind):
    if kind == 'E':
        return exact_div(P, TWO)
    return exact_div(add(mul(THREE, P), {0: 1}), TWO)


def pow_poly(base, n):
    r = {0: 1}
    for _ in range(n):
        r = mul(r, base)
    return r


def cycle_candidate(word):
    """Return P0 (Laurent dict) or None if D∤n_k. D=[2]^k-[3]^ko, n_k as above."""
    m = {0: 1}      # m_0
    n = {}          # n_0 = 0
    c_pow = 0       # tracks [2]^i via exponent count; we rebuild [2]^i explicitly
    k = len(word)
    two_i = {0: 1}  # [2]^i, starts [2]^0
    for i, kind in enumerate(word):
        if kind == 'E':
            # m,n unchanged; c_{i+1}=[2]^{i+1}
            pass
        else:
            # m <- [3] m ; n <- [3] n + [2]^i
            m = mul(THREE, m)
            n = add(mul(THREE, n), two_i)
        two_i = mul(two_i, TWO)   # now [2]^{i+1}
    ko = sum(1 for x in word if x == 'O')
    D = add(pow_poly(TWO, k), pow_poly(THREE, ko), sb=-1)  # [2]^k - [3]^ko
    if not D:  # D=0 => A=1 balanced sub-case, skip
        return ('A1', None)
    P0 = exact_div(n, D)
    return ('ok', P0)


def self_consistent(P0, word):
    P = P0
    for kind in word:
        if parity(P) != kind:
            return False
        P = step(P, kind)
        if P is None:
            return False
    return P == P0


def poly_str(P):
    if not P:
        return "0"
    terms = []
    for e in sorted(P, reverse=True):
        c = P[e]
        terms.append(f"{c}*q^{e}" if e else f"{c}")
    return " + ".join(terms)


def positive(P0):
    if not P0:
        return False
    cs = list(P0.values())
    return all(c > 0 for c in cs)


def orbit_key(P0, word):
    P = P0; seq = []
    for kind in word:
        seq.append(tuple(sorted(P.items())))
        P = step(P, kind)
    rots = [tuple(seq[i:] + seq[:i]) for i in range(len(seq))]
    return min(rots)


def run(kmax):
    pos, nonpos = {}, {}
    n_scanned = n_A1 = n_integral = n_consistent = 0
    for k in range(1, kmax + 1):
        sys.stderr.write(f"[progress] k={k} (2^{k}={2**k})\n"); sys.stderr.flush()
        for bits in product('EO', repeat=k):
            if 'O' not in bits:
                continue
            # skip imprimitive words (proper repetition of a shorter word)
            w = ''.join(bits)
            if any(k % d == 0 and w == w[:d] * (k // d) for d in range(1, k)):
                continue
            n_scanned += 1
            word = list(bits)
            tag, P0 = cycle_candidate(word)
            if tag == 'A1':
                n_A1 += 1
                continue
            if P0 is None:       # D ∤ n_k  => candidate not Skein-integral
                continue
            n_integral += 1
            if not self_consistent(P0, word):
                continue
            n_consistent += 1
            key = orbit_key(P0, word)
            (pos if positive(P0) else nonpos)[key] = dict(
                period=len(word), word=''.join(word), P0=poly_str(P0))
    return dict(kmax=kmax, words_scanned=n_scanned, balanced_A1=n_A1,
                integral_candidates=n_integral,
                integral_self_consistent=n_consistent,
                primitive_positive_cycles=list(pos.values()),
                primitive_nonpositive_cycles=list(nonpos.values()))


if __name__ == '__main__':
    KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    # sanity: OE => classical {1,2} lift, P0 = q^{-1}
    tag, P0 = cycle_candidate(['O', 'E'])
    print("sanity OE: P0 =", poly_str(P0), "| consistent:",
          self_consistent(P0, ['O', 'E']))
    r = run(KMAX)
    summ = {k: v for k, v in r.items() if 'cycles' not in k}
    print(json.dumps(summ, indent=2))
    print("\nprimitive POSITIVE cycles:")
    for c in r['primitive_positive_cycles']:
        print(f"  period {c['period']:>2}  word={c['word']:<20} P0 = {c['P0']}")
    print("primitive NON-POSITIVE cycles:")
    for c in r['primitive_nonpositive_cycles']:
        print(f"  period {c['period']:>2}  word={c['word']:<20} P0 = {c['P0']}")
    with open('qcollatz_census.json', 'w') as f:
        json.dump(r, f, indent=2)
