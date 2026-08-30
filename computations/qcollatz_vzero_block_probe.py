#!/usr/bin/env python3
"""Can a v = 0 block (two consecutive odd steps) occur inside D_inf?

The q-Collatz block decomposition assumed "one odd step, then a run of even
steps". `collatz_block_descent.oddStep_next_residue` shows that shape is not
automatic: two consecutive odd steps are possible in the DOMAIN
(`consecutive_odd_steps_exist`, witness -2q-3). Whether one can occur inside the
domain-stable cone D_inf is the arc's one remaining bounded open question.

TWO EXACT CRITERIA, derived before probing.

(1) FORWARD, at the [2]_q-divisor q = -1. Writing P = -1 + [2]_q A, differentiating
    (q+1)A = P+1 gives A(-1) = P'(-1). So

        two consecutive odd steps at P  <=>  P(-1) = -1  and  P'(-1) = -2.

(2) BACKWARD, at a primitive cube root of unity w (where [3]_q vanishes). The odd
    branch-inverse ([2]P - 1)/[3] is an exact Laurent division iff [3]_q divides
    the numerator, iff the numerator vanishes at w:

        odd-preimage of P exists  <=>  (w+1)P(w) = 1  <=>  P(w) = -w

    (using w+1 = -w^2 and w^3 = 1). Differentiating [3]Q = [2]P - 1 at w, where
    [3](w) = 0, gives Q(w) = [P(w) + (w+1)P'(w)] / (2w+1); imposing Q(w) = -w in
    turn forces

        a SECOND chained odd-preimage exists  <=>  P(w) = -w  and  P'(w) = 2.

So a v = 0 block inside D_inf is exactly a backward-tree node satisfying BOTH
conditions of (2). This probe searches for one.

Both criteria are checked against the attractor cycle first: q^-1 has P(w) = w^2,
so NO odd-preimage; 1+q^-1 has P(w) = -w, and its odd-preimage is q^-1 -- both of
which match the map's behaviour computed independently.

Exact arithmetic throughout: Laurent polynomials over Z, and Z[w] as pairs
(x, y) = x + y*w with w^2 = -1 - w. No float.

Exploratory research probe (NOT canonical production).
"""
import sys, json
from collections import deque

TWO = {1: 1, 0: 1}
THREE = {2: 1, 1: 1, 0: 1}
ONE = {0: 1}
ATTR_A = {-1: 1}
ATTR_B = {-1: 1, 0: 1}


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
        quot[k] = rk // dlead
        for e, c in D.items():
            rem[e + k] = rem.get(e + k, 0) - quot[k] * c
            if rem[e + k] == 0:
                del rem[e + k]
    if rem:
        return None
    return {e + (nmin - dmin): c for e, c in quot.items()}


def parity(P):
    v = sum(c * ((-1) ** e) for e, c in P.items())
    return 'E' if v == 0 else ('O' if v == -1 else None)


def step(P):
    p = parity(P)
    if p == 'E':
        return exact_div(P, TWO), 'E'
    if p == 'O':
        return exact_div(add(mul(THREE, P), ONE), TWO), 'O'
    return None, None


def key(P):
    return tuple(sorted(P.items()))


def poly_str(P):
    return "0" if not P else " ".join(f"{P[e]:+d}*q^{e}" for e in sorted(P, reverse=True))


CYCLE = {key(ATTR_A), key(ATTR_B)}

# ---- Z[w] exact arithmetic, w^2 = -1 - w ----
def wmul(a, b):
    (x1, y1), (x2, y2) = a, b
    return (x1 * x2 - y1 * y2, x1 * y2 + y1 * x2 - y1 * y2)


def wpow(a, n):
    base = a if n >= 0 else (-1, -1)      # w^{-1} = w^2 = -1 - w
    r = (1, 0)
    for _ in range(abs(n)):
        r = wmul(r, base)
    return r


W = (0, 1)
NEG_W = (0, -1)
TWO_W = (2, 0)


def at_omega(P):
    r = (0, 0)
    for e, c in P.items():
        p = wpow(W, e)
        r = (r[0] + c * p[0], r[1] + c * p[1])
    return r


def deriv_at_omega(P):
    r = (0, 0)
    for e, c in P.items():
        if e == 0:
            continue
        p = wpow(W, e - 1)
        r = (r[0] + c * e * p[0], r[1] + c * e * p[1])
    return r


# ---- the two forward conditions at q = -1 ----
def at_minus_one(P):
    return sum(c * ((-1) ** e) for e, c in P.items())


def deriv_at_minus_one(P):
    return sum(c * e * ((-1) ** (e - 1)) for e, c in P.items() if e != 0)


def even_preimage(P):
    return mul(TWO, P)


def odd_preimage(P):
    return exact_div(add(mul(TWO, P), ONE, sb=-1), THREE)


def run(depth, node_cap=400000):
    seen = set(CYCLE)
    frontier = deque([(dict(ATTR_A), 0), (dict(ATTR_B), 0)])
    nodes = 0
    odd_pre_nodes = 0            # nodes admitting an odd-preimage
    chained = []                 # nodes admitting TWO chained odd-preimages
    fwd_consecutive = []         # nodes that ARE the start of a v=0 block
    while frontier and nodes < node_cap:
        P, d = frontier.popleft()
        if d >= depth:
            continue
        for Q in (even_preimage(P), odd_preimage(P)):
            if Q is None or not Q:
                continue
            kq = key(Q)
            if kq in seen:
                continue
            seen.add(kq)
            nodes += 1
            # backward criterion (2)
            if at_omega(Q) == NEG_W:
                odd_pre_nodes += 1
                if deriv_at_omega(Q) == TWO_W:
                    chained.append(poly_str(Q))
            # forward criterion (1): is Q itself the start of a v=0 block?
            if at_minus_one(Q) == -1 and deriv_at_minus_one(Q) == -2:
                fwd_consecutive.append(poly_str(Q))
            frontier.append((Q, d + 1))
    return dict(
        depth=depth, nodes=nodes,
        nodes_admitting_odd_preimage=odd_pre_nodes,
        nodes_admitting_TWO_chained_odd_preimages=len(chained),
        chained_examples=chained[:5],
        nodes_starting_a_v0_block=len(fwd_consecutive),
        v0_block_examples=fwd_consecutive[:5],
    )


if __name__ == '__main__':
    depth = int(sys.argv[1]) if len(sys.argv) > 1 else 40

    # sanity: both criteria reproduce the map's behaviour on the cycle
    assert at_omega(ATTR_A) != NEG_W, "q^-1 must have NO odd-preimage"
    assert odd_preimage(ATTR_A) is None, "and the map must agree"
    assert at_omega(ATTR_B) == NEG_W, "1+q^-1 must HAVE an odd-preimage"
    assert key(odd_preimage(ATTR_B)) == key(ATTR_A), "and it must be q^-1"
    # forward criterion agrees with the known domain witness -2q-3
    Wt = {1: -2, 0: -3}
    assert at_minus_one(Wt) == -1 and deriv_at_minus_one(Wt) == -2
    assert parity(Wt) == 'O' and parity(step(Wt)[0]) == 'O'
    print("sanity OK: both criteria agree with the map on the cycle and on -2q-3")

    r = run(depth)
    print(json.dumps(r, indent=2))
    w = {
        'schema': 'qou-probe/v0',
        'description': ('Can a v=0 block (two consecutive odd steps) occur inside '
                        'the q-Collatz domain-stable cone D_inf? Searches the '
                        'backward-orbit tree of the attractor using two exact '
                        'criteria: forward P(-1)=-1 & P\'(-1)=-2, backward '
                        'P(w)=-w & P\'(w)=2 at a primitive cube root of unity. '
                        'Exact Laurent and Z[w] arithmetic. Exploratory research '
                        'probe (NOT canonical production).'),
        'result': r,
    }
    with open('qcollatz_vzero_block_probe.witness.json', 'w') as f:
        json.dump(w, f, indent=2)
    print("wrote qcollatz_vzero_block_probe.witness.json")
