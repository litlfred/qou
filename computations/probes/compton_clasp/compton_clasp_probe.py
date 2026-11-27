#!/usr/bin/env python3
"""Photon-clasp ("Compton subtraction") probe on the Borromean core, exact.

Hecke algebra H_n(q), sigma^2 = (q - q^-1) sigma + 1, Ocneanu trace with the
convention-D Markov parameter z_D = q^3/(q^2+1), tr(1) = 1. A fourth strand
clasps quark strand i (pure-braid generator A_{i,3}) or strands i then j
(A_{i,3} A_{j,3}); E_4 : H_4 -> H_3 is the Markov conditional expectation.
D_ij = tr(B * L_ij) with B = (s0 s1^-1)^3, the Borromean core.

All arithmetic is exact in Q(q) (sympy); no float enters. Output:
compton_clasp_probe.out.json. See RESULT.md for the reading.
"""
import json, itertools, pathlib
import sympy as sp
q=sp.symbols('q',positive=True); h=q-1/q; z=q**3/(q**2+1)
def inv(w): return sum(1 for i in range(len(w)) for j in range(i+1,len(w)) if w[i]>w[j])
def comp(u,v): return tuple(u[v[x]] for x in range(len(v)))
def s(i,n): w=list(range(n)); w[i],w[i+1]=w[i+1],w[i]; return tuple(w)
def add(a,b,c=1):
    r=dict(a)
    for k,v in b.items(): r[k]=r.get(k,0)+c*v
    return {k:sp.simplify(v) for k,v in r.items() if sp.simplify(v)!=0}
def lmul_gen(i,x,n):
    S=s(i,n); r={}
    for w,c in x.items():
        sw=comp(S,w)
        if inv(sw)>inv(w): r=add(r,{sw:c})
        else: r=add(r,{sw:c, w:h*c})
    return r
def redword(w):
    w=list(w); word=[]
    while True:
        d=[i for i in range(len(w)-1) if w[i]>w[i+1]]
        if not d: return word[::-1]
        i=d[0]; w[i],w[i+1]=w[i+1],w[i]; word.append(i)
def mul(x,y,n):
    r={}
    for u,c in x.items():
        t=dict(y)
        # T_u = T_{a1}...T_{ak}; reduce word of u: u = s_{a1}...s_{ak}
        wd=redword(u)
        for i in reversed(wd): t=lmul_gen(i,t,n)
        r=add(r,t,c)
    return r
def one(n): return {tuple(range(n)):1}
def gen(i,n,e=1): return {s(i,n):1} if e==1 else add({s(i,n):1},one(n),-h)
def word(lst,n):
    x=one(n)
    for (i,e) in lst: x=mul(x,gen(i,n,e),n)
    return x
def perms(n): return list(itertools.permutations(range(n)))
def E(x,n):
    """conditional expectation H_n -> H_{n-1}, Ocneanu, convention D"""
    r={}
    sub=[p for p in perms(n-1)]
    for w,c in x.items():
        if w[n-1]==n-1: r=add(r,{w[:n-1]:c}); continue
        done=False
        for a in sub:
            for b in sub:
                if inv(a)+1+inv(b)!=inv(w): continue
                A=a+(n-1,); B=b+(n-1,)
                if comp(comp(A,s(n-2,n)),B)==w:
                    r=add(r,mul({a:1},{b:1},n-1),c*z); done=True; break
            if done: break
        assert done
    return r
def tr(x,n):
    while n>1: x=E(x,n); n-=1
    return sp.simplify(x.get((0,),0))

def A(i):
    """photon strand 3 clasps strand i (passes under the strands between)."""
    up = [(j, 1) for j in range(2, i, -1)]
    dn = [(j, -1) for j in range(i + 1, 3)]
    return up + [(i, 1), (i, 1)] + dn

def main():
    out = {}
    B = word([(0, 1), (1, -1)] * 3, 3)
    B4 = {k + (3,): v for k, v in B.items()}
    trB = sp.factor(tr(B, 3))
    m = (q**4 + 1) / (q**2 + 1)
    out["trB"] = str(trB)
    out["trB_minus_1"] = str(sp.factor(trB - 1))
    # single-strand clasps: E_4 is a scalar
    out["E_single_clasp"] = {str(i): {str(k): str(sp.factor(v)) for k, v in E(word(A(i), 4), 4).items()} for i in range(3)}
    L = {}
    for i in range(3):
        L[(i, i)] = word(A(i), 4)
        for j in range(3):
            if i != j:
                L[(i, j)] = word(A(i) + A(j), 4)
    D = {k: sp.factor(tr(mul(B4, v, 4), 4)) for k, v in L.items()}
    out["E_pair_clasp"] = {str(k): {str(a): str(sp.factor(b)) for a, b in E(v, 4).items()} for k, v in L.items() if k[0] != k[1]}
    out["D"] = {str(k): str(v) for k, v in D.items()}
    S = {(i, j): (D[(i, j)] + D[(j, i)]) / 2 for i in range(3) for j in range(3)}
    C = {k: sp.factor(S[k] - trB * (m if k[0] == k[1] else m**2)) for k in S}
    out["connected_symmetrised"] = {str(k): str(v) for k, v in C.items() if k[0] < k[1]}
    out["diag_factorises"] = all(sp.simplify(C[(i, i)]) == 0 for i in range(3))
    Qu, Qd = sp.Rational(2, 3), sp.Rational(-1, 3)
    def form(M, Q): return sum(Q[i] * Q[j] * M[(i, j)] for i in range(3) for j in range(3))
    e = sp.symbols("epsilon")
    out["p_minus_n"] = {}
    for odd in range(3):
        Qp = [Qu] * 3; Qp[odd] = Qd
        Qn = [Qd] * 3; Qn[odd] = Qu
        full = sp.factor(form(S, Qp) - form(S, Qn))
        conn = sp.factor(form(C, Qp) - form(C, Qn))
        out["p_minus_n"][str(odd)] = {
            "full": str(full),
            "full_minus_factorised": str(sp.factor(full - trB * (m / 3 + 2 * m**2 / 3))),
            "connected": str(conn),
            "full_at_q1": str(sp.limit(full, q, 1)),
            "full_series_q_eq_1_plus_eps": str(sp.series(full.subs(q, 1 + e), e, 0, 3).removeO()),
        }
    p = pathlib.Path(__file__).with_name("compton_clasp_probe.out.json")
    p.write_text(json.dumps(out, indent=1) + "\n")
    for k, v in out["p_minus_n"].items(): print("odd strand", k, v["full_at_q1"], "| connected:", v["connected"])

if __name__ == "__main__":
    main()
