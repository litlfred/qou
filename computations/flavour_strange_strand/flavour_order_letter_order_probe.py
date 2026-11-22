"""Is the flavour order the same convention as the letter (strand) order? Exact over Q(q).

Hypothesis from docs/audits/2026-11-22-sign-conventions-table.md §4 (row F1): the flavour
order that sets the operator-level GMO sign (docs/audits/2026-11-21-octet-gmo-operator-level.md)
is the Gröbner letter order seen on more strands.

Test, on the octet operator of octet_gmo_operator_probe.py (imported unchanged):

* REVERSED FLAVOUR ORDER: run the probe's operator with order s<d<u (the reversal of u<d<s).
* REFLECTED STRANDS: keep u<d<s, but build the Jucys-Murphy elements from the other end of
  the strand line (L3' = 1, L2' = s2^2, L1' = s1 s2^2 s1). Reflecting the strands
  conjugates the braiding by the tensor flip, which is the letter-order reversal
  P: sigma_1 <-> sigma_2.

If the two conventions are one, these two runs give the same masses. Each run also reports
the GMO sign, so the table shows whether a letter-order reversal flips it.

No measured data enter. Usage: python3 flavour_order_letter_order_probe.py  (~15 min)
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import octet_gmo_operator_probe as base  # noqa: E402
from sympy import Rational, factor, simplify, symbols, zeros  # noqa: E402

q = base.q


def run(U, D, S, reflect):
    """Same as base.run, with an option to build the JM elements from the top strand."""
    if not reflect:
        return base.run(U, D, S)
    # Rebuild M with reflected JM elements: patch by recomputing inside a copy of run.
    N, WORDS, IDX = base.N, base.WORDS, base.IDX
    s1, s2 = zeros(N), zeros(N)
    for x in WORDS:
        for y in WORDS:
            if x[2] == y[2]:
                s1[IDX[x], IDX[y]] = base.r2((x[0], x[1]), (y[0], y[1]))
            if x[0] == y[0]:
                s2[IDX[x], IDX[y]] = base.r2((x[1], x[2]), (y[1], y[2]))
    one = base.eye(N)
    Lr = [s1 * s2 * s2 * s1, s2 * s2, one]
    w = [None] * 3
    w[U], w[D], w[S] = base.wu, base.wd, base.ws
    M = zeros(N)
    for x in WORDS:
        j = IDX[x]
        for k in range(3):
            for i in range(N):
                M[j, i] += w[x[k]] * Lr[k][j, i]
    # Reuse base.run for projectors by temporarily swapping its M builder is not possible,
    # so recompute masses here with the base projector code path.
    return _masses(U, D, S, s1, s2, M)


def _masses(U, D, S, s1, s2, M):
    N, WORDS, IDX = base.N, base.WORDS, base.IDX
    one = base.eye(N)
    T = {0: [one], 1: [s1, s2], 2: [s1 * s2, s2 * s1], 3: [s1 * s2 * s1]}
    psym = base.normalise(sum((q ** l * t for l, ts in T.items() for t in ts), zeros(N)))
    panti = base.normalise(sum(((-1 / q) ** l * t for l, ts in T.items() for t in ts), zeros(N)))
    poct = (one - psym - panti).applyfunc(simplify)
    E, F = zeros(3), zeros(3)
    E[U, D] = 1
    F[D, U] = 1
    kd = [base.Integer(1)] * 3
    kd[U], kd[D] = q, 1 / q
    K, Ki, I3 = base.diag(*kd), base.diag(*[base.Integer(1) / x for x in kd]), base.eye(3)
    EE = base.kron(E, K, K) + base.kron(I3, E, K) + base.kron(I3, I3, E)
    FF = base.kron(F, I3, I3) + base.kron(Ki, F, I3) + base.kron(Ki, Ki, F)
    for sg in (s1, s2):
        assert (EE * sg - sg * EE).applyfunc(simplify) == zeros(N)
    cas = (FF * EE + (q * base.kron(K, K, K) + base.kron(Ki, Ki, Ki) / q) / base.h ** 2
           ).applyfunc(simplify)
    lam = lambda i2: (q ** (i2 + 1) + q ** (-(i2 + 1))) / base.h ** 2

    def wsp(ms):
        p = zeros(N)
        for x in WORDS:
            if sorted(x) == sorted(ms):
                p[IDX[x], IDX[x]] = 1
        return p

    def mass(ms, i2):
        Q = (poct * wsp(ms)).applyfunc(simplify)
        for o in [lam(j) for j in range(4) if j != i2]:
            Q = (Q * (cas - o * one) / (lam(i2) - o)).applyfunc(simplify)
        assert Q.subs(q, Rational(3, 2)).rank() == 2
        # Q commutes with s1, s2, hence with every L_k from either end (as in the base probe).
        for Lk in (s2 * s2, s1 * s2 * s2 * s1):
            assert (Q * Lk - Lk * Q).applyfunc(simplify) == zeros(N)
        return simplify((Q * M).trace() / Q.trace())

    m = {'N': mass((U, U, D), 1), 'Sigma': mass((U, U, S), 2), 'Xi': mass((U, S, S), 1),
         'Lambda': mass((U, D, S), 0), 'Sigma0': mass((U, D, S), 2)}
    gmo = simplify(2 * (m['N'] + m['Xi']) - 3 * m['Lambda'] - m['Sigma'])
    return m, gmo


def summary(m, gmo, q0):
    a, b = symbols('a b')
    iso = {base.wu: a, base.wd: a, base.ws: b}
    xn = simplify((m['Xi'] - m['N']).subs(iso))
    r = factor(simplify(gmo.subs(iso) / xn))
    out = {'gmo_over_xi_minus_n': str(r), 'at_q0': str(r.subs(q, q0).evalf(15))}
    for k in ('Sigma', 'Lambda'):
        rk = simplify((m[k] - m['N']).subs(iso) / xn)
        out[f'{k}_minus_N_over_xi_minus_N_at_q0'] = str(rk.subs(q, q0).evalf(15))
    return out, r


if __name__ == '__main__':
    from qou_substrate.constants import Q_50_DIGIT_STR
    q0 = Rational(Q_50_DIGIT_STR)  # proton pin, evaluation only
    runs = {
        'u<d<s': (0, 1, 2, False),
        # s<d<u is the reversal of u<d<s. The simple U_q(sl2) coproduct needs u before d, so
        # it is run as s<u<d: with isospin-symmetric weights (w_u = w_d) the u<->d relabel
        # leaves every multiplet mass unchanged, so the two agree on what is compared here.
        's<d<u (flavour order reversed)': (1, 2, 0, False),
        'u<d<s, strands reflected': (0, 1, 2, True),
    }
    res, masses = {}, {}
    for label, (U, D, S, refl) in runs.items():
        print('== run', label, flush=True)
        m, gmo = run(U, D, S, refl)
        masses[label] = m
        res[label], _ = summary(m, gmo, q0)
        print('  ', res[label], flush=True)
    a, b = symbols('a b')
    iso = {base.wu: a, base.wd: a, base.ws: b}
    same = all(simplify((masses['s<d<u (flavour order reversed)'][k]
                         - masses['u<d<s, strands reflected'][k]).subs(iso)) == 0
               for k in masses['u<d<s'])
    sign_flip = (Rational(res['u<d<s']['at_q0']) * Rational(
        res['s<d<u (flavour order reversed)']['at_q0'])) < 0
    print('reflected strands == reversed flavour order (five masses, exact, w_u = w_d):', same)
    print('reversing the order flips the GMO sign:', sign_flip)
    out = {'q0Anchor': 'proton', 'q0AnchorReason': 'evaluation at the proton 50-digit pin only;'
           ' all algebra exact in Q(q)',
           'hypothesis': 'flavour order = letter order (sign table row F1)',
           'runs': res,
           'reflected_strands_equal_reversed_flavour_order': same,
           'reversal_flips_gmo_sign': bool(sign_flip)}
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'flavour-order-letter-order.witness.json')
    with open(path, 'w') as fh:
        json.dump(out, fh, indent=2)
    print('wrote', path)
