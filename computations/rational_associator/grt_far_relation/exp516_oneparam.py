# Exact over Q. Bean qou-3fdg. One-parameter law for the (5.16) exponential of exp516.py:
#   Exp(s psi) o Exp(t psi) = Exp((s+t) psi)  in Q<X,Y> modulo degree D+1,
# for psi = sigma3 (in grt) and psi = [X,[X,Y]] (not in grt). Composition is Drinfeld's (5.16).
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.argv = sys.argv[:1]
from exp516 import *
D = 9  # checked: True for both psi and both (s, t)
def finv(g):  # inverse of 1+n
    n = fadd(g, fsc(-1, F1)); r = dict(F1); t = dict(F1)
    for k in range(1, D + 1):
        t = fsc(-1, fmul(t, n, D)); r = fadd(r, t)
    return r
def subst(g, a, b):  # g(a,b)
    r = {}
    for w, c in g.items():
        t = dict(F1)
        for l in w: t = fmul(t, a if l == 0 else b, D)
        r = fadd(r, fsc(c, t))
    return r
def comp(g1, g2): return fmul(subst(g1, fmul(fmul(g2, FX, D), finv(g2), D), FY), g2, D)
def main():
    sig3 = fadd(fbr(FX, fbr(FX, FY, D), D), fbr(FY, fbr(FX, FY, D), D))
    for name, psi in [('sigma3', sig3), ('[X,[X,Y]]', fbr(FX, fbr(FX, FY, D), D))]:
        for s, t in [(1, 1), (Fr(1, 3), Fr(2, 5))]:
            lhs = comp(Exp516(fsc(s, psi), D), Exp516(fsc(t, psi), D)); rhs = Exp516(fsc(s + t, psi), D)
            diff = fadd(lhs, fsc(-1, rhs))
            print(name, s, t, 'Exp(s)∘Exp(t) = Exp(s+t) through degree', D, ':', not diff,
                  'lowest diff deg', min((len(k) for k in diff), default=None))
    

if __name__ == '__main__':
    main()
