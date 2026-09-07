"""sigma on K, via the QUADRATIC over Q(zeta_3) rather than the quartic over Q.

[K:Q] = 4 and zeta_3 in K, so [K:Q(u)] = 2 and {1,T} is a Q(u)-basis.  Then:
  1. express T^2 = A + B*T with A,B in Q(u)   -- a LINEAR system over Q (fast)
  2. sigma fixes Q and swaps u <-> u^2, so sigma(T) is a root of X^2 - s(B)X - s(A)
  3. solve that QUADRATIC in K for y = sigma(T)  -- degree 2, not degree 4

Every candidate is then verified EXACTLY: f(sigma(T)) == 0 and sigma(u) == u^2.
"""
import json, re, warnings; warnings.filterwarnings('ignore')
import sympy as sp
T = sp.Symbol('T')
d = json.load(open('computations/ptolemy/L6a4-c1-ptolemy-in-K.json'))
f = sp.sympify(d['field']['min_poly'].replace('t','T'))
red = lambda e: sp.expand(sp.rem(sp.expand(e), f, T))
co = {k: sp.expand(sp.sympify(re.sub(r'\bt\b','T',v))) for k,v in d['ptolemy'].items()}
u2 = co['u']; u1 = red(-1 - u2)
assert red(u1**2+u1+1) == 0

def vec(x):
    c = sp.Poly(red(x), T).all_coeffs()[::-1]
    return [sp.Rational(c[i]) if i < len(c) else sp.Integer(0) for i in range(4)]

# step 1: T^2 = (a0+a1 u1) + (b0+b1 u1) T   -- linear in a0,a1,b0,b1 over Q
a0,a1,b0,b1 = sp.symbols('a0 a1 b0 b1', rational=True)
A = a0 + a1*u1; B = b0 + b1*u1
eqs = [x - y for x, y in zip(vec(T**2), [sum(sp.expand(red(A + B*T)).coeff(T, k) for _ in [0]) for k in range(4)])]
expr = sp.expand(red(A + B*T)) - sp.expand(red(T**2))
P = sp.Poly(expr, T)
sol = sp.solve(P.all_coeffs(), [a0,a1,b0,b1], dict=True)
assert sol, "no Q(u)-representation of T^2"
S = sol[0]; Av = sp.expand(A.subs(S)); Bv = sp.expand(B.subs(S))
assert red(T**2 - Av - Bv*T) == 0
print("T^2 = A + B*T over Q(u), verified exactly")

# step 2: conjugate the coefficients (u1 -> u2)
def conj(x):
    # x = p + q*u1 with p,q rational -> p + q*u2
    p_, q_ = sp.symbols('p_ q_', rational=True)
    ss = sp.solve(sp.Poly(sp.expand(red(p_ + q_*u1)) - sp.expand(red(x)), T).all_coeffs(), [p_, q_], dict=True)
    assert ss, f"{x} not in Q(u)"
    return sp.expand(ss[0][p_] + ss[0][q_]*u2)
As, Bs = conj(Av), conj(Bv)
print("conjugated A,B")

# step 3: solve y^2 = Bs*y + As in K  (quadratic, 4 rational unknowns)
c0,c1,c2,c3 = sp.symbols('c0 c1 c2 c3', rational=True)
y = c0 + c1*T + c2*T**2 + c3*T**3
Q = sp.Poly(red(y**2 - Bs*y - As), T)
print("solving the quadratic for sigma(T) ...", flush=True)
sols = sp.solve(Q.all_coeffs(), [c0,c1,c2,c3], dict=True)
auts = []
for s in sols:
    if len(s) != 4 or not all(v.is_rational for v in s.values()): continue
    g = sp.expand(y.subs(s))
    if red(f.subs(T, g)) != 0: continue                      # EXACT check
    su = red(u1.subs(T, g))                                  # sigma(u1)
    tag = "u1->u2" if red(su - u2) == 0 else ("u1->u1" if red(su - u1) == 0 else "?")
    auts.append((g, tag))
    print(f"  sigma: T -> {g}      [{tag}]")
good = [g for g, t in auts if t == "u1->u2"]
print(f"\n{len(auts)} automorphism(s) found; {len(good)} invert zeta_3")
if good: json.dump(str(good[0]), open('/tmp/sigma.json','w')); print("wrote /tmp/sigma.json")
