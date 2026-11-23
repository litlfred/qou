"""Six-weight two-photon factorisations of V^3 = (s0 s1^-1)^3 in H_3(q).

Numerical search (mpmath, 40 digits, random complex starts) at q = 11/10 and at 1/q, checked
against the three irreps of H_3. Reports each solution and whether the second photon is the
q -> 1/q image of the first. Not a proof: the solution count is what random search found.
Bean qou-99qc; Lean companion QOU/PhotonWeightsForced.lean (V-only case, proved).
"""
import mpmath as mp, random
mp.mp.dps=40
def solve_at(q,seed=1,N=600):
    M=mp.matrix
    S0=M([[q,0],[0,-1/q]])
    S1=M([[-1/(q**3+q),(q**2*(q**2+1)+1)/(q**2+1)**2],[1,q**3/(q**2+1)]])
    reps=[(M([[q]]),M([[q]])),(M([[-1/q]]),M([[-1/q]])),(S0,S1)]
    def F(*p):
        out=[]
        for A,B in reps:
            n=A.rows; I=mp.eye(n); V=A*B**-1
            g=lambda f0,f1,f01: I+f0*A+f1*B+f01*V
            R=g(*p[:3])*g(*p[3:])-V**3
            out+=[R[i,j] for i in range(n) for j in range(n)]
        return out
    sols=[];random.seed(seed)
    for t in range(N):
        x0=[mp.mpc(mp.mpf(random.randint(-4000,4000))/1000,mp.mpf(random.randint(-4000,4000))/1000) for _ in range(6)]
        try: s=mp.findroot(F,x0,tol=1e-30,maxsteps=200)
        except Exception: continue
        s=[mp.mpc(v) for v in s]
        if not any(max(abs(a-b) for a,b in zip(s,u))<mp.mpf('1e-20') for u in sols): sols.append(s)
    return sols
q=mp.mpf(11)/10
A=solve_at(q); B=solve_at(1/q,seed=2)
print(len(A),len(B))
for s in A:
    phi,psi=s[:3],s[3:]
    # theta: second photon at q equals first photon at 1/q
    ok=any(max(abs(a-b) for a,b in zip(psi,t[:3]))<mp.mpf('1e-20') for t in B)
    print([mp.nstr(z,8) for z in phi],[mp.nstr(z,8) for z in psi],"theta-paired:",ok)
