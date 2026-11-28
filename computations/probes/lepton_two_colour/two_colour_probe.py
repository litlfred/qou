"""Two-colour ring trace of the lepton words (unscored probe, exact sympy).

Colour each closure component with its own U_q(sl2) irrep V_a (dim a+1), take the
quantum trace of the 3-braid word, correct the framing per component with the
ribbon twist theta_n = q^{n(n+2)/2}, and divide by the unlink value [a+1][b+1].
The result C_L(a,b) is the cross-component interaction factor: C = 1 at q = 1.
Expand log C in h = log q (the G_m logarithm).

Words: e = s0 s1 s0, mu = s0^4 s1^-1, tau = s0^2 s1^-1 s0 s1^-1.
Exact arithmetic only; q0 is used only for the displayed values (mpmath, 40 dps).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import sympy as sp
import mpmath as mp
from two_colour_trace import s, q, qi, word_rep, qtrace

P = lambda i: (i, 1)
N = lambda i: (i, -1)
WORDS = {
    "e": [P(0), P(1), P(0)],
    "mu": [P(0)] * 4 + [N(1)],
    "tau": [P(0), P(0), N(1), P(0), N(1)],
}


def components(word, n=3):
    pos = list(range(n))
    crossings = []
    for (i, e) in word:
        crossings.append((pos[i], pos[i + 1], e))
        pos[i], pos[i + 1] = pos[i + 1], pos[i]
    nxt = {pos[k]: k for k in range(n)}
    seen, cyc = set(), []
    for j in range(n):
        if j in seen:
            continue
        c, x = [], j
        while x not in seen:
            seen.add(x); c.append(x); x = nxt[x]
        cyc.append(c)
    cid = {x: ci for ci, c in enumerate(cyc) for x in c}
    selfw = [0] * len(cyc)
    for (x, y, e) in crossings:
        if cid[x] == cid[y]:
            selfw[cid[x]] += e
    return cyc, cid, selfw


def theta(n):
    return q ** sp.Rational(n * (n + 2), 2)


def main():
    mp.mp.dps = 40
    q0 = mp.mpf("1.1099785827513808")  # proton pin; display only
    h = sp.symbols("h")
    Cas = lambda n: n * (n + 2)
    for name, wd in WORDS.items():
        cyc, cid, sw = components(wd)
        for (a, b) in [(1, 1), (1, 2), (2, 2)]:
            cs = (a, b)
            cols = [cs[cid[k]] for k in range(3)]
            M, c = word_rep(wd, cols)
            assert c == cols
            J = qtrace(M, c) * sp.prod([theta(cs[i]) ** (-sw[i]) for i in range(2)])
            C = sp.simplify(J / (qi(a + 1) * qi(b + 1)))
            ser = sp.expand(sp.simplify(sp.series(sp.log(C.subs(s, sp.exp(h / 2))), h, 0, 5).removeO()))
            c2, c3 = ser.coeff(h, 2), ser.coeff(h, 3)
            k = Cas(a) * Cas(b)
            val = sp.N(C.subs(s, sp.sqrt(sp.Float(mp.nstr(q0, 35), 40))), 20)
            print(f"{name:3} {cs}  C(q0)={val}  h^2/(CaCb)={sp.nsimplify(c2 / k)}  h^3/(CaCb)={sp.nsimplify(c3 / k)}")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
