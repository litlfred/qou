#!/usr/bin/env python3
"""Does v_[2] descend on the domain-stable cone D_inf?  (bean qou-4atn)

BACKGROUND.  `reaches_cycle_of_descent_domainStable` reduces q-Collatz
convergence on D_inf to the existence of a measure that strictly descends off
the attractor.  The natural candidate is the [2]_q-adic valuation v_[2].  Two
landed Lean results bracket it:

  * collatz_vtwo_obstruction.qcollatz_vTwo_increases_on_odd_branch -- v_[2]
    INCREASES on the witness -X-2 (an odd step, 0 -> 2);
  * collatz_vtwo_domain_rescope.qcollatz_vTwo_witness_escapes_domain -- but that
    witness ESCAPES the domain at step 4, so it says nothing about D_inf.

That re-opened the question (qou-4atn): v_[2] might still descend ON D_inf.
The one positive datum was collatz_vtwo_cycle_descent (the even step of the
fundamental cycle drops 1 -> 0).

WHAT THIS PROBE DOES.  It settles the question by CONSTRUCTING D_inf elements
instead of searching for them.  Every backward orbit of the attractor cycle is
in D_inf by construction: if C^[n](P) is the cycle then every forward iterate of
P is defined, so P is domain-stable.  The two branch-inverses are

    even-preimage  of P :  [2]_q * P            (always exists; always q-even)
    odd-preimage   of P :  ([2]_q*P - 1)/[3]_q  (when that division is exact)

so the tree is generated exactly, with no search and no float anywhere.

Every node is ALSO verified forward -- iterate C until the cycle is reached --
so D_inf membership is established twice, by construction and by orbit, rather
than asserted.

Then for each node Q off the attractor we compare v_[2](Q) against
v_[2](C(Q)).  A single node with v_[2](C(Q)) >= v_[2](Q) refutes v_[2] as a
descent measure on D_inf.

PRECISION.  Exact integer Laurent arithmetic throughout (dict {exponent: int});
no float, no mpmath, nothing to lose precision in.  v_[2] is computed by
repeated exact division by [2]_q, so it is an exact integer count.

Exploratory research probe (NOT canonical production).
"""
import sys, json
from collections import Counter, deque
from pathlib import Path  # witness path must be FILE-relative, not cwd-relative

TWO = {1: 1, 0: 1}          # [2]_q = q + 1
THREE = {2: 1, 1: 1, 0: 1}  # [3]_q = q^2 + q + 1
ONE = {0: 1}
ATTR_A = {-1: 1}            # q^{-1}
ATTR_B = {-1: 1, 0: 1}      # 1 + q^{-1}


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
    """Exact Laurent division, or None when it does not divide."""
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


def parity(P):
    """P(-1): 'E' (q-even) if 0, 'O' (q-odd) if -1, None if off-domain."""
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
        return exact_div(add(mul(THREE, P), ONE), TWO), 'O'
    return None, None


def vtwo(P):
    """The [2]_q-adic valuation: multiplicity of (q+1) in P. Exact."""
    if not P:
        return None  # v(0) = infinity; never reached on this tree
    v, cur = 0, dict(P)
    while True:
        nxt = exact_div(cur, TWO)
        if nxt is None:
            return v
        v += 1
        cur = nxt


def key(P):
    return tuple(sorted(P.items()))


def poly_str(P):
    if not P:
        return "0"
    terms = []
    for e in sorted(P, reverse=True):
        c = P[e]
        terms.append(f"{c:+d}*q^{e}")
    return " ".join(terms)


CYCLE = {key(ATTR_A), key(ATTR_B)}


def reaches_cycle(P, budget=2000):
    """Forward-verify D_inf membership: iterate until the attractor cycle."""
    cur, n = dict(P), 0
    while n < budget:
        if key(cur) in CYCLE:
            return True, n
        nxt, _ = step(cur)
        if nxt is None:
            return False, n   # left the domain -- would mean the tree is wrong
        cur, n = nxt, n + 1
    return False, n


def even_preimage(P):
    return mul(TWO, P)


def odd_preimage(P):
    return exact_div(add(mul(TWO, P), ONE, sb=-1), THREE)


def run(depth=14, node_cap=200000):
    """BFS the backward tree of the attractor; test v_[2] descent at each node."""
    seen = set(CYCLE)
    frontier = deque([(dict(ATTR_A), 0), (dict(ATTR_B), 0)])
    nodes = 0
    odd_preimages = 0
    transitions = Counter()      # (v_before, v_after, branch) -> count
    violations = []              # v_[2] did NOT strictly descend, off-attractor
    forward_checked = 0
    forward_failed = []
    max_v = 0

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

            # D_inf membership, verified forward as well as by construction
            ok, steps_to_cycle = reaches_cycle(Q)
            forward_checked += 1
            if not ok:
                forward_failed.append(poly_str(Q))
                continue

            R, branch = step(Q)
            if branch == 'O':
                odd_preimages += 1
            vq, vr = vtwo(Q), vtwo(R)
            max_v = max(max_v, vq)
            transitions[(vq, vr, branch)] += 1
            # descent is required only OFF the attractor
            if kq not in CYCLE and vr >= vq:
                violations.append({
                    'P': poly_str(Q), 'v_P': vq,
                    'C_P': poly_str(R), 'v_CP': vr,
                    'branch': branch,
                    'steps_to_cycle': steps_to_cycle,
                })
            frontier.append((Q, d + 1))
            if nodes % 20000 == 0:
                sys.stderr.write(f"[progress] {nodes} nodes, "
                                 f"{len(violations)} violations\n")
                sys.stderr.flush()

    return dict(
        depth=depth, nodes=nodes,
        odd_branch_nodes=odd_preimages,
        forward_verified_in_Dinf=forward_checked,
        forward_verification_failures=forward_failed,
        max_v_two_seen=max_v,
        transition_histogram={f"v{a}->v{b}/{br}": c
                              for (a, b, br), c in sorted(transitions.items())},
        descent_violations_count=len(violations),
        descent_violations=violations[:25],
    )


if __name__ == '__main__':
    depth = int(sys.argv[1]) if len(sys.argv) > 1 else 14

    # sanity: the two attractor elements, and the landed Lean cycle facts
    assert vtwo(ATTR_A) == 0, "v_[2](q^-1) must be 0 (a unit)"
    assert vtwo(ATTR_B) == 1, "v_[2](1+q^-1) must be 1"
    a_next, a_br = step(ATTR_A)
    b_next, b_br = step(ATTR_B)
    assert key(a_next) == key(ATTR_B) and a_br == 'O', "q^-1 --odd--> 1+q^-1"
    assert key(b_next) == key(ATTR_A) and b_br == 'E', "1+q^-1 --even--> q^-1"
    print("sanity OK: cycle values and both cycle steps match the Lean facts")

    r = run(depth)
    print(json.dumps(r, indent=2))

    w = {
        'schema': 'qou-probe/v0',
        'description': ('Does v_[2] descend on the q-Collatz domain-stable cone '
                        'D_inf? Backward-orbit construction of D_inf elements '
                        'from the attractor cycle, exact Z[q^{+-1}] arithmetic. '
                        'Bean qou-4atn. Exploratory research probe (NOT '
                        'canonical production).'),
        'map': {
            'even': 'C(P)=P/[2]_q when P(-1)=0',
            'odd': 'C(P)=([3]_q P+1)/[2]_q when P(-1)=-1',
            'attractor_cycle': ['q^-1', '1+q^-1'],
            'even_preimage': '[2]_q * P (always exists)',
            'odd_preimage': '([2]_q P - 1)/[3]_q (when exact)',
        },
        'question': ('Is v_[2](C(P)) < v_[2](P) for every P in D_inf off the '
                     'attractor? A single violation refutes v_[2] as a descent '
                     'measure on D_inf.'),
        'result': r,
    }
    with open(Path(__file__).with_name('qcollatz_vtwo_domain_stable_probe.witness.json'), 'w') as f:
        w["q0Anchor"] = "independent"
        w["q0AnchorReason"] = "No substrate pin enters this computation: neither the producer nor its transitive import cone inside computations/ references q_at, q_muon_at, Q_50_DIGIT_STR, q_parameter or resolve_q0_anchor outside comments (AST import-cone walk, 2026-09-03). The probe computes: Does v_[2] descend on the domain-stable cone D_inf?  (bean qou-4atn)."
        json.dump(w, f, indent=2)
    print("wrote qcollatz_vtwo_domain_stable_probe.witness.json")
