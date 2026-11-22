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

Young projector trace tau = chi_(3) - chi_(1^3), weights (1, 0, -1)
(added 2026-11-22):
  * tau is not a Markov trace: tau(1) = 0 but tau(sigma_2) = [2]_q, so no z
    satisfies tau(x sigma_2) = z tau(x) on H_2.
  * Split V^{(x)3} by the number k of odd tensor factors (R preserves k).
    The supertrace of sector k has weights k=0: (1,0,0), k=1: (-1,-1,0),
    k=2: (0,1,1), k=3: (0,0,-1). So tau is exactly the supertrace on the two
    extremal sectors (all even, all odd); the mixed sectors carry -tau, which
    is why the full supertrace is 0.
  * No single super vector space gives tau through its supertrace (Lean:
    QOU.AlphaEM.YoungTrace.no_superdim_gives_young_trace, at q = 1).
Nothing here says the photon selects the extremal sectors; that is open.

Can an element of H_3(q), such as the photon, do the selecting? (added
2026-11-22.) No. The ordinary trace of each sector gives its block
multiplicities: k=0 (3), k=1 (3)+(2,1), k=2 (2,1)+(1^3), k=3 (1^3). The
mixed sectors k=1,2 together contain all three blocks, so they are a
faithful H_3(q)-module: an element acting by 0 on them is 0. Every element of
H_3(q) preserves each sector (R preserves k), so none keeps the extremal
sectors while removing the mixed ones. The selection has to come from the
weight projector onto the extremal sectors, which is a Cartan element of
U_q(gl(1|1)) (it commutes with H_3(q)), not from the Hecke side:
tau(x) = str(P_ext x).

Which Cartan insertions give (1, 0, -1)? (added 2026-11-22.) Let H act on
V^{(x)3} by E11 - E22 (value 3 - 2k on sector k) and insert a diagonal f(H)
into the supertrace. The weights are exactly
  (f(3) - f(1), f(-1) - f(1), f(-1) - f(-3)).
So str(f(H) x) is proportional to (1, 0, -1) iff f(1) = f(-1) and
f(3) = f(-3) (f even in H on V^{(x)3}) with f(3) != f(1). K = q^H alone
fails; K + K^-1 gives [2]_q h^2 (1, 0, -1), K^2 + K^-2 and H^2 also work.
The direction is forced by evenness under K -> K^-1; the overall scale
f(3) - f(1) is not fixed by this.

Where the evenness comes from (added 2026-11-22). iota: sigma -> -sigma^-1
is an involution of H_3(q) (Hecke and braid checked on V^{(x)3}). On the
gl(1|1) side it is the parity swap: the trace of rho(iota x) on sector k
equals the trace of rho(x) on sector 3 - k. Since 3 is odd, the supertrace
sign (-1)^k flips under k -> 3 - k, so str(f(H) rho(iota x)) =
-str(f(-H) rho(x)). An even f therefore gives an iota-odd functional, and
(Lean: QOU.AlphaEM.IotaOdd.iota_odd_iff) the iota-odd block functionals are
exactly the multiples of (1, 0, -1). Normalisation: among even insertions,
the idempotent ones with nonzero weights are P_ext (weights (1, 0, -1)) and
1 - P_ext (weights (-1, 0, 1)); P_ext is a polynomial in K + K^-1. So
requiring a projection fixes the scale up to the sign choice of which
sectors are kept. Not derived: why the alpha_em functional should be
iota-odd, and that sign.
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
    # Young projector trace tau and the gl(1|1) weight sectors.
    import itertools

    def sector_str(x, k):
        return sp.simplify(sum((-1) ** k * x[i, i] for i, b in
                               enumerate(itertools.product([0, 1], repeat=3))
                               if sum(b) == k))
    expect = {0: [1, 0, 0], 1: [-1, -1, 0], 2: [0, 1, 1], 3: [0, 0, -1]}
    for k, ex in expect.items():
        vals = [sector_str(word(w, s1, s2, sp.eye(8)), k) for w in words]
        sol = sp.solve([sum(c[i] * W[i] for i in range(3)) - v
                        for c, v in zip(chars, vals)], W, dict=True)
        got = [sp.simplify(sol[0][x]) for x in W] if len(sol) == 1 else None
        print(f'sector with {k} odd factors: weights {got}')
        checks.append((f'sector k={k} weights {ex}', got == ex))
    tau = lambda c: c[0] - c[2]
    t1, ts2 = tau(chars[words.index('')]), tau(chars[words.index('2')])
    checks.append(('tau(1) = 0 and tau(s2) = [2]_q, so tau is not Markov',
                   sp.simplify(t1) == 0 and sp.simplify(ts2 - (q + 1 / q)) == 0))
    # Block multiplicities of each sector (ordinary trace) and faithfulness.
    def sector_tr(x, k):
        return sp.simplify(sum(x[i, i] for i, bb in
                               enumerate(itertools.product([0, 1], repeat=3))
                               if sum(bb) == k))
    mult = {0: [1, 0, 0], 1: [1, 1, 0], 2: [0, 1, 1], 3: [0, 0, 1]}
    for k, ex in mult.items():
        vals = [sector_tr(word(w, s1, s2, sp.eye(8)), k) for w in words]
        sol = sp.solve([sum(c[i] * W[i] for i in range(3)) - v
                        for c, v in zip(chars, vals)], W, dict=True)
        got = [sp.simplify(sol[0][x]) for x in W] if len(sol) == 1 else None
        print(f'sector {k} block multiplicities {got}')
        checks.append((f'sector k={k} multiplicities {ex}', got == ex))
    checks.append(('mixed sectors contain every block (faithful)',
                   all(mult[1][i] + mult[2][i] > 0 for i in range(3))))
    # Cartan insertions f(H), H = E11 - E22.
    hval = [sum(1 if bit == 0 else -1 for bit in bb)
            for bb in itertools.product([0, 1], repeat=3)]
    gsign = sp.diag(*[(-1) ** sum(bb) for bb in itertools.product([0, 1], repeat=3)])

    def ins_weights(fdiag):
        F = sp.diag(*fdiag)
        vals = [sp.simplify((gsign * F * word(w, s1, s2, sp.eye(8))).trace())
                for w in words]
        sol = sp.solve([sum(c[i] * W[i] for i in range(3)) - v
                        for c, v in zip(chars, vals)], W, dict=True)
        return [sp.simplify(sol[0][x]) for x in W] if len(sol) == 1 else None
    fv = sp.symbols('f3 f1 fm1 fm3')
    fmap = {3: fv[0], 1: fv[1], -1: fv[2], -3: fv[3]}
    gen = ins_weights([fmap[x] for x in hval])
    checks.append(('general f(H) weights (f3-f1, fm1-f1, fm1-fm3)',
                   gen is not None and all(sp.simplify(g - e) == 0 for g, e in
                   zip(gen, [fv[0] - fv[1], fv[2] - fv[1], fv[2] - fv[3]]))))
    kk = ins_weights([q ** x + q ** -x for x in hval])
    print(f'K + K^-1 weights {[sp.factor(x) for x in kk]}')
    checks.append(('K + K^-1 gives [2]_q h^2 (1,0,-1)',
                   all(sp.simplify(g - (q + 1 / q) * h ** 2 * e) == 0
                       for g, e in zip(kk, [1, 0, -1]))))
    k1 = ins_weights([q ** x for x in hval])
    checks.append(('K alone has a nonzero hook weight', sp.simplify(k1[1]) != 0))
    # iota = sigma -> -sigma^-1 is the parity swap k -> 3 - k.
    i1, i2 = -s1.inv(), -s2.inv()
    checks.append(('iota: Hecke relation', sp.simplify(i1 * i1 - h * i1 - sp.eye(8)) == sp.zeros(8, 8)))
    checks.append(('iota: braid relation', sp.simplify(i1 * i2 * i1 - i2 * i1 * i2) == sp.zeros(8, 8)))
    swap_ok = all(sp.simplify(sector_tr(word(w, i1, i2, sp.eye(8)), k)
                              - sector_tr(word(w, s1, s2, sp.eye(8)), 3 - k)) == 0
                  for w in words for k in range(4))
    checks.append(('iota swaps sector k with sector 3-k', swap_ok))
    # P_ext as a polynomial in c = K + K^-1, and its weights.
    cK = lambda x: q ** x + q ** -x
    pext = [sp.simplify((cK(x) - cK(1)) / (cK(3) - cK(1))) for x in hval]
    checks.append(('P_ext = (c - c(1))/(c(3) - c(1)) is the extremal projector',
                   pext == [1 if abs(x) == 3 else 0 for x in hval]))
    checks.append(('P_ext insertion weights (1,0,-1)', ins_weights(pext) == [1, 0, -1]))
    for n, c in checks:
        print(('PASS ' if c else 'FAIL ') + n)
    return 0 if all(c for _, c in checks) else 1


if __name__ == '__main__':
    raise SystemExit(main())
