#!/usr/bin/env python3
"""Does the U_q(gl(1|1)) quantum supertrace supply the (1, 0, -1) weights?

Question (alpha_em audit 2026-11-21, section 8 item 1): the linchpin
(sigma_1 sigma_2)^5 -> q^10 - q^-10 = (q - q^-1)[10]_q needs Markov weights
(w_(3), w_(2,1), w_(1^3)) = (1, 0, -1) on the three blocks of H_3(q)
(Lean: QOU.AlphaEM.T35TenLinchpin.t35_weights_unique). A supertrace is the
obvious candidate for an alternating sign. This probe tests it.

Test (fixed before reading the result): the weights of each gl(1|1) trace, solved exactly
from the block characters. Pass = proportional to (1, 0, -1). No data, no
fit, no float: everything is exact in Q(q) with sympy.

Representation: V = C^{1|1}, R-check on V (x) V with diagonal q (even),
-q^-1 (odd), swap off-diagonal, h = q - q^-1 on the lower entry. Hecke and
braid relations are checked. Markov twist mu = 1 (solved, not assumed).

Result (both traces; the cut trace is the Alexander polynomial, as expected):
  * full supertrace on V^{(x)3}: identically 0 on H_3(q) -> weights (0,0,0);
  * cut supertrace (supertrace on strands 2,3, strand 1 left open; scalar
    on strand 1, checked): weights q^2/[3]_q * (1, -1, 1), with
    [3]_q = q^2 + 1 + q^-2. On (sigma_1 sigma_2)^5 it gives
    q^2/[3]_q (q^10 + 1 + q^-10), not (q - q^-1)[10]_q.

So gl(1|1) does NOT supply (1, 0, -1): the sign alternates on the hook too.
Scope (a): this representation, alone. It does not exclude other super or
partial traces.
"""
import sympy as sp

q = sp.symbols('q', nonzero=True)
h = q - 1 / q
I2 = sp.eye(2)
grade = sp.diag(1, -1)


def rcheck():
    M = sp.zeros(4, 4)
    idx = lambda i, j: 2 * i + j
    for i in range(2):
        for j in range(2):
            if i == j:
                M[idx(i, i), idx(i, i)] = q if i == 0 else -1 / q
            else:
                M[idx(j, i), idx(i, j)] = 1
                if i > j:
                    M[idx(i, j), idx(i, j)] = h
    return M


R = rcheck()
s1 = sp.kronecker_product(R, I2)
s2 = sp.kronecker_product(I2, R)
hs1 = sp.Matrix([[q, 1], [0, -1 / q]])        # hook rep, as in
hs2 = sp.Matrix([[-1 / q, 0], [1, q]])        # T35TenLinchpinFromH3.lean


def word(w, a, b, one):
    x = one
    for c in w:
        x = x * (a if c == '1' else b)
    return x


def full_str(x):
    g = sp.kronecker_product(grade, sp.kronecker_product(grade, grade))
    return sp.simplify((g * x).trace())


def cut_str(x):
    y = sp.kronecker_product(I2, sp.kronecker_product(grade, grade)) * x
    pt = sp.Matrix(2, 2, lambda a, b: sp.simplify(
        sum(y[4 * a + k, 4 * b + k] for k in range(4))))
    assert sp.simplify(pt[0, 1]) == 0 and sp.simplify(pt[1, 0]) == 0
    assert sp.simplify(pt[0, 0] - pt[1, 1]) == 0, 'cut trace not scalar'
    return pt[0, 0]


def main():
    checks = []
    checks.append(('Hecke', sp.simplify(s1 * s1 - h * s1 - sp.eye(8)) == sp.zeros(8, 8)))
    checks.append(('braid', sp.simplify(s1 * s2 * s1 - s2 * s1 * s2) == sp.zeros(8, 8)))
    # Markov twist: partial supertrace of (I (x) mu grade) R must be scalar.
    mu = sp.symbols('mu')
    P = sp.kronecker_product(I2, sp.diag(1, mu) * grade) * R
    pt = sp.Matrix(2, 2, lambda a, b: sum(P[2 * a + k, 2 * b + k] for k in range(2)))
    checks.append(('Markov twist mu = 1', sp.solve(sp.Eq(pt[0, 0], pt[1, 1]), mu) == [1]))

    words = ['', '1', '2', '12', '21', '121', '11', '121212', '1212121212']
    chars = []
    for w in words:
        chars.append([q ** len(w),
                      sp.simplify(word(w, hs1, hs2, sp.eye(2)).trace()),
                      (-1 / q) ** len(w)])
    W = sp.symbols('w3 w21 w111')
    t35 = words.index('1212121212')
    for name, tr in (('full supertrace', full_str), ('cut supertrace', cut_str)):
        vals = [tr(word(w, s1, s2, sp.eye(8))) for w in words]
        sol = sp.solve([sum(c[i] * W[i] for i in range(3)) - v
                        for c, v in zip(chars, vals)], W, dict=True)
        ok = len(sol) == 1
        s = sol[0] if ok else {}
        ws = [sp.factor(s.get(x, sp.nan)) for x in W]
        prop = ok and sp.simplify(ws[1]) == 0 and sp.simplify(ws[0] + ws[2]) == 0 \
            and sp.simplify(ws[0]) != 0
        print(f'{name}: weights (w3, w21, w111) = {ws}')
        print(f'   on (s1 s2)^5: {sp.factor(vals[t35])}')
        print(f'   proportional to (1, 0, -1): {prop}')
        checks.append((f'{name}: consistent over {len(words)} words', ok))
        checks.append((f'{name}: weights are not (1,0,-1) (recorded result)', not prop))
    three = q ** 2 + 1 + q ** -2
    vals = cut_str(word('1212121212', s1, s2, sp.eye(8)))
    checks.append(('cut value = q^2/[3] (q^10 + 1 + q^-10)',
                   sp.simplify(vals - q ** 2 / three * (q ** 10 + 1 + q ** -10)) == 0))
    for n, c in checks:
        print(('PASS ' if c else 'FAIL ') + n)
    return 0 if all(c for _, c in checks) else 1


if __name__ == '__main__':
    raise SystemExit(main())
