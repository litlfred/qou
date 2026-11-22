"""PRE-REGISTERED (written before running), np-splitting audit §20.
Question: do the second-order weak terms FE and EF of U_q(gl_2) give a u/d ratio
on the ruled nucleon larger than the level-2 weight ratio q^{-2} (§13, §16, §17)?

Fixed before running (nothing here is chosen after seeing output):
  element  : gamma-gamma nucleon V^3, V = s1 s2^{-1} (ruled, qou-ales). V^6 reported as a check.
  R-matrix : the Jimbo R of §13/§18, R = [[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]], h = q - 1/q.
  K        : diag(q, 1/q), forced by convention D (MarkovOrientationForced.lean).
  u        : e1 (the K = q vector), PR #7971.  p = weight (u,u,d), n = weight (u,d,d).
  E, F     : E = e_{12} (e2 -> e1), F = e_{21}. The 3-fold coproduct is the one of the two
             standard forms (E x K + 1 x E  or  E x 1 + K x E, F mirrored with K^{-1}) under which
             Delta(E), Delta(F) commute with s1, s2. That is a check, not a choice: exactly one
             form is expected to pass; the probe asserts it.
  trace    : D quantum trace t_mu(X) = tr_{weight mu}(K^{x3} X) / [2]^3.
  inserted : X in {1 (control), FE, EF}, each times V^3.
Primary quantity: r_X = t_n(X V^3) / t_p(X V^3), exact in Q(q).
  "Larger than the level-2 weight" is pre-registered as |ln|r_X|| > 2 ln q at q0
  (and the exact ratio r_X * q^2 != 1 as a rational function).
Ratios do not depend on the normalisation of E, F (E -> aE, F -> bF scales both by ab).
Also reported, not used to select: the U_q isotypic split (V_{3/2} x M_(3)  +  V_{1/2} x M_(2,1)),
and the S0 (alpha*|ln r|, alpha asserted, H_alpha) and D1 (E0_full*|t_n - t_p|) MeV figures.
CODATA 1.29333205 MeV is comparison only; nothing is selected by residual.
Exact sympy over Q(q); numerics in mpmath at 40 dps.
"""
import itertools, sympy as sp
from mpmath import mp, mpf, log, catalan
mp.dps = 40
q = sp.symbols('q', positive=True); h = q - 1/q
qs = sp.Rational('1.1099785827513808075916690956107688798744991218736')
R = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]])
I2 = sp.eye(2); kp = sp.kronecker_product
s1 = kp(R, I2); s2 = kp(I2, R)
V = s1*s2.inv()
Kd = sp.diag(q, 1/q); Ki = sp.diag(1/q, q)
E1 = sp.Matrix([[0,1],[0,0]]); F1 = sp.Matrix([[0,0],[1,0]])
def k3(a,b,c): return kp(kp(a,b),c)
cop = {
 'A: E(x)K + 1(x)E': (k3(E1,Kd,Kd)+k3(I2,E1,Kd)+k3(I2,I2,E1), k3(F1,I2,I2)+k3(Ki,F1,I2)+k3(Ki,Ki,F1)),
 'B: E(x)1 + K(x)E': (k3(E1,I2,I2)+k3(Kd,E1,I2)+k3(Kd,Kd,E1), k3(F1,Ki,Ki)+k3(I2,F1,Ki)+k3(I2,I2,F1)),
}
passing = []
for name,(E,F) in cop.items():
    ok = all(sp.simplify(X*s - s*X) == sp.zeros(8) for X in (E,F) for s in (s1,s2))
    print(f'coproduct {name}: commutes with s1,s2 = {ok}')
    if ok: passing.append((name,E,F))
assert len(passing) == 1, 'expected exactly one coproduct to commute with the braid'
name,E,F = passing[0]
K3 = k3(Kd,Kd,Kd)
assert sp.simplify(E*F - F*E - (K3 - K3.inv())/h) == sp.zeros(8)
basis = list(itertools.product(range(2), repeat=3))
def t(W, wt):
    tot = 0
    for k,b in enumerate(basis):
        if tuple(sorted(b)) == wt: tot += K3[k,k]*W[k,k]
    return sp.factor(sp.simplify(tot/(q+1/q)**3))
P, N = (0,0,1), (0,1,1)
qm = mpf(str(sp.N(qs,45))); lq2 = 2*log(qm)
me = mpf('0.51099895069'); cod = mpf('1.29333205')
alpha = me*8*catalan; hb = 1-1/qm; E0f = me/(qm*(qm-1))/(1-hb**2)
def num(x): return mpf(str(sp.N(x.subs(q,qs),45)))
for wname, W in (('V^3', V**3), ('V^6', V**6)):
    print(f'\n=== {wname} ===')
    for xname, X in (('1', sp.eye(8)), ('FE', F*E), ('EF', E*F)):
        tp, tn = t(X*W, P), t(X*W, N)
        r = sp.factor(sp.simplify(tn/tp)) if tp != 0 else sp.oo
        print(f'X={xname}: t_p = {tp}\n       t_n = {tn}\n       r = t_n/t_p = {r}   r*q^2 = {sp.factor(sp.simplify(r*q**2)) if tp!=0 else "-"}')
        if tp != 0 and tn != 0:
            lr = abs(log(abs(num(r))))
            same = sp.simplify(r*q**2 - 1) == 0
            print(f'       |ln|r|| = {mp.nstr(lr,12)}  vs 2 ln q = {mp.nstr(lq2,12)}  ratio {mp.nstr(lr/lq2,10)}  '
                  f'larger: {"no (exactly equal, r q^2 = 1)" if same else lr > lq2}')
            print(f'       S0 alpha*|ln|r|| = {mp.nstr(alpha*lr,8)} MeV ({mp.nstr(100*(alpha*lr/cod-1),5)} %);'
                  f'  D1 E0_full*|t_n-t_p| = {mp.nstr(E0f*abs(num(tn-tp)),8)} MeV ({mp.nstr(100*(E0f*abs(num(tn-tp))/cod-1),5)} %)')
# isotypic check: FE and EF act on each weight space through the Casimir sectors
Cas = F*E + (q*K3 + K3.inv()/q)/(q-1/q)**2
print('\nCasimir commutes with s1,s2:', all(sp.simplify(Cas*s-s*Cas)==sp.zeros(8) for s in (s1,s2)))
for wname, W in (('V^3', V**3),):
    for lab,wt in (('p',P),('n',N)):
        idx=[k for k,b in enumerate(basis) if tuple(sorted(b))==wt]
        sub=lambda M: M.extract(idx,idx)
        print(f'{lab}: eigenvalues FE on weight space:', {sp.factor(k):v for k,v in sub(F*E).eigenvals().items()},
              ' EF:', {sp.factor(k):v for k,v in sub(E*F).eigenvals().items()})

# ---- STRUCTURAL CHECKS, added after the first run (explain the numbers; select nothing) ----
# omega: E <-> F, K <-> K^{-1} swaps the p and n weight spaces. Claims checked here:
#  (i)  r_FE * r_EF = q^{-4}                       for every braid word tested
#  (ii) omega-symmetric insertions FE+EF and the Casimir give r = q^{-2} exactly
#  (iii) r_FE = q^{-2} A, A = ([2]^2 chi_(3) + chi_(2,1)) / ([3] chi_(3))
print('\n--- structural checks over all words in s1^{+-1}, s2^{+-1} of length <= 4 ---')
gens = {'a':s1,'A':s1.inv(),'b':s2,'B':s2.inv()}
Cq = F*E + (q*K3 + K3.inv()/q)/h**2
bad = 0; cnt = 0
for L in range(0,5):
    for w in itertools.product('aAbB', repeat=L):
        W = sp.eye(8)
        for c in w: W = W*gens[c]
        rs = {}
        for xname,X in (('FE',F*E),('EF',E*F),('FE+EF',F*E+E*F),('Cas',Cq)):
            tp, tn = t(X*W,P), t(X*W,N)
            rs[xname] = None if tp == 0 else sp.simplify(tn/tp)
        cnt += 1
        ok1 = rs['FE'] is None or rs['EF'] is None or sp.simplify(rs['FE']*rs['EF'] - q**-4) == 0
        ok2 = all(rs[k] is None or sp.simplify(rs[k] - q**-2) == 0 for k in ('FE+EF','Cas'))
        if not (ok1 and ok2): bad += 1; print('FAIL', ''.join(w), rs)
print(f'words tested {cnt}, failures {bad}')
# (iii) chi_(2,1)(V^3) and A
br = (q+1/q)**2; tr3 = q**2+1+q**-2
idx=[k for k,b in enumerate(basis) if tuple(sorted(b))==P]
plain = sp.simplify(sum((V**3)[k,k] for k in idx))
chi21 = sp.factor(sp.simplify(plain - 1))   # chi_(3)(V^3) = q*q^{-1}... = 1 on the symmetric line
A = sp.factor(sp.simplify((br*1 + chi21)/tr3))
print('chi_(2,1)(V^3) =', chi21, ' at q=1:', chi21.subs(q,1), ' at q0:', mp.nstr(num(chi21),12))
print('A =', A, ' at q=1:', A.subs(q,1), ' at q0:', mp.nstr(num(A),12))

# --- Follow-up (2026-11-15, raised by the weak-vertex thread, pre-registered before running):
# state-dependent order. The neutron's virtual loop is FE (go to p and back), and the proton's is EF.
# Question: does r_state = t_n(FE.W)/t_p(EF.W) differ from q^-2? Also the reverse assignment.
print('\n=== state-dependent order (follow-up) ===')
for wname, W in (('V^3', V**3), ('V^6', V**6)):
    for lab, Xn, Xp in (('n:FE, p:EF', F*E, E*F), ('n:EF, p:FE', E*F, F*E)):
        r = sp.factor(sp.simplify(t(Xn*W, N)/t(Xp*W, P)))
        print(f'{wname} {lab}: r = {r}   r*q^2 = {sp.factor(sp.simplify(r*q**2))}')
