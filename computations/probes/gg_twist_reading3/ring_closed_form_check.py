#!/usr/bin/env python3
"""ring_closed_form_check.py — stage 6b: exact check of the ring closed form, n = 3..8.

Checks d<ring_n> = <H>^n + u^n (d W_n - 1) exactly, where u = 1 - A^(-+4), <H> = A^(+-2) d + u is the
Hopf bond, and W_n is the bracket of the all-e state; and that W_n = (-A^3)^(n-2) <T(2,n-2)>.
Exact integer Laurent polynomials; no evaluation. -- Ref: [leitner2026] bean qou-a1hh
"""
import sys, itertools
from pathlib import Path; sys.path.insert(0, str(Path(__file__).resolve().parent))
import tl_bracket as tl
from collections import defaultdict
import nstrand_connected_probe as P
D=tl.D_LOOP
def bracket_mixed(word,n):
    state={tl.ident(n):{0:1}}
    for g,s in word:
        E=tl.egen(g,n); new=defaultdict(dict)
        for Dg,c in state.items():
            if s=='e':
                D2,L=tl.compose(Dg,E,n); new[D2]=tl.padd(new[D2],tl.pmul(c,tl.ppow(D,L)))
                continue
            a_id,a_e=(1,-1) if s>0 else (-1,1)
            new[Dg]=tl.padd(new[Dg],tl.pmul(c,{a_id:1}))
            D2,L=tl.compose(Dg,E,n); new[D2]=tl.padd(new[D2],tl.pmul(c,tl.pmul({a_e:1},tl.ppow(D,L))))
        state={k:v for k,v in new.items() if v}
    tot={}
    for Dg,c in state.items():
        tot=tl.padd(tot,tl.pmul(c,tl.ppow(D,tl.closure_loops(Dg,n)-1)))
    return tot
def W(n,e):
    rho=[(g,1) for g in range(n-1)]
    return bracket_mixed([(i,'e') for i in range(n-1)]+rho+[(n-2,'e')]+P.inv(rho),n)
for e in (2,-2):
  for n in range(3,9):
    Wn=W(n,e)
    sg=1 if e>0 else -1
    # <H> and u
    u={0:1,-4*sg:-1}
    H={2*sg:1}; H=tl.pmul(H,D); H=tl.padd(H,u)
    # ring bracket check: <ring> = d^-1 ... use identity d<ring> = <H>^n + u^n (dW-1)
    ring=tl.bracket(P.ring(n,e),n)
    lhs=tl.pmul(D,ring)
    rhs=tl.padd(tl.ppow(H,n), tl.pmul(tl.ppow(u,n), tl.padd(tl.pmul(D,Wn),{0:1},-1)))
    w1=sum(Wn.values())
    print(n,e,'identity',P.eq(lhs,rhs),'W(1)=',w1,'W=',dict(sorted(Wn.items())))
print('--- torus check')
for n in range(3,9):
    Wn=W(n,2); m=n-2
    T=tl.bracket([(0,1)]*m,2)
    # find shift k with W = +-A^k T
    ks=[(a-b) for a in Wn for b in T]
    for k in set(ks):
        for sgn in (1,-1):
            if P.eq(Wn,{e+k:sgn*v for e,v in T.items()}): print(n,'W = %+d A^%d <T(2,%d)>'%(sgn,k,m))
