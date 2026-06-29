import numpy as np
import cvxpy as cp
import itertools, time

# ---------------------------------------------------------------------------
# 4-site Hubbard ring, half filling (N=4 electrons, r=8 spin-orbitals).
# spin-orbital index = site*2 + spin   (spin 0=up, 1=down);  r_up=2r, r_dn=2r+1
# ---------------------------------------------------------------------------
r = 8
nsite = 4
N = 4                      # electrons
t = 1.0
bonds = [(0,1),(1,2),(2,3),(3,0)]

# ---- Jordan-Wigner fermionic operators on the 2^8 Fock space ----
I2 = np.eye(2); Z = np.array([[1,0],[0,-1]]); Sm = np.array([[0,1],[0,0]])  # a = |0><1|
def kron(mats):
    out = np.array([[1.0]])
    for m in mats: out = np.kron(out, m)
    return out
a = []
for p in range(r):
    mats = [Z]*p + [Sm] + [I2]*(r-1-p)
    a.append(kron(mats))
a = [m.astype(float) for m in a]
ad = [m.T.conj() for m in a]

# one-body hopping matrix h[p,q]
h = np.zeros((r,r))
for (x,y) in bonds:
    for s in range(2):
        p, q = 2*x+s, 2*y+s
        h[p,q] -= t; h[q,p] -= t

def build_H(U):
    H = np.zeros((2**r, 2**r))
    for p in range(r):
        for q in range(r):
            if h[p,q]!=0: H += h[p,q]*(ad[p]@a[q])
    for x in range(nsite):
        pu, pd = 2*x, 2*x+1
        H += U*(ad[pu]@a[pu]@ad[pd]@a[pd])
    return H

# number projector onto N-electron sector
Nop = sum(ad[p]@a[p] for p in range(r))

def ground_state(U):
    H = build_H(U)
    # project to N-electron sector by penalty
    pen = 1e6*(Nop - N*np.eye(2**r))@(Nop - N*np.eye(2**r))
    w,v = np.linalg.eigh(H+pen)
    psi = v[:,0]
    E = float(psi@H@psi)
    return psi, E

def exp(op, psi): return float(psi@op@psi)

# exact RDMs from a state
def exact_rdms(psi):
    D1 = np.zeros((r,r))
    for p in range(r):
        for q in range(r):
            D1[p,q] = exp(ad[p]@a[q], psi)
    D2 = np.zeros((r,r,r,r))
    for p,q,rr,s in itertools.product(range(r),repeat=4):
        # D2[p,q,r,s] = <a†_p a†_q a_s a_r>
        D2[p,q,rr,s] = exp(ad[p]@ad[q]@a[s]@a[rr], psi)
    return D1, D2

# ---- closed-form Q and G maps (to be VERIFIED) ----
def Qmap(D1,D2):
    Q = np.zeros((r,r,r,r))
    d = np.eye(r)
    for p,q,rr,s in itertools.product(range(r),repeat=4):
        Q[p,q,rr,s] = (d[q,s]*d[p,rr] - d[p,s]*d[q,rr]
                       - d[q,s]*D1[rr,p] + d[p,s]*D1[rr,q]
                       + d[q,rr]*D1[s,p] - d[p,rr]*D1[s,q]
                       + D2[s,rr,q,p])
    return Q
def Gmap(D1,D2):
    G = np.zeros((r,r,r,r))
    d = np.eye(r)
    for p,q,rr,s in itertools.product(range(r),repeat=4):
        G[p,q,rr,s] = d[q,s]*D1[p,rr] - D2[p,s,rr,q]
    return G

# exact Q,G directly from operators (for verification)
def exact_QG(psi):
    Q = np.zeros((r,r,r,r)); G = np.zeros((r,r,r,r))
    for p,q,rr,s in itertools.product(range(r),repeat=4):
        Q[p,q,rr,s] = exp(a[p]@a[q]@ad[s]@ad[rr], psi)   # <a_p a_q a†_s a†_r>
        G[p,q,rr,s] = exp(ad[p]@a[q]@ad[s]@a[rr], psi)    # <a†_p a_q a†_s a_r>
    return Q,G

# ===================== VERIFY maps on the U=2 ground state =====================
psi,E0 = ground_state(2.0)
D1,D2 = exact_rdms(psi)
Qx,Gx = exact_QG(psi)
Qc,Gc = Qmap(D1,D2), Gmap(D1,D2)
print("VERIFY  ||Q_closedform - Q_exact|| =", np.max(np.abs(Qc-Qx)))
print("VERIFY  ||G_closedform - G_exact|| =", np.max(np.abs(Gc-Gx)))
# also verify energy and PSD of exact D-matrix
def mat(T): return T.reshape(r*r, r*r)
print("VERIFY  min eig D =", np.linalg.eigvalsh(mat(D2)).min(),
      " Q =", np.linalg.eigvalsh(mat(Qx)).min(),
      " G =", np.linalg.eigvalsh(mat(Gx)).min())
assert np.max(np.abs(Qc-Qx))<1e-8 and np.max(np.abs(Gc-Gx))<1e-8, "MAP VERIFICATION FAILED"
print("maps verified.\n")

# ===================== build linear maps as constant matrices =================
def idx(p,q,rr,s): return ((p*r+q)*r+rr)*r+s
M = r**4
# D1[a,b] = 1/(N-1) sum_k D2[a,k,b,k]   -> linear in vec(D2)
# Build A_Q d + bQ = vec(Q),  A_G d + bG = vec(G)
A_Q = np.zeros((M,M)); bQ = np.zeros(M)
A_G = np.zeros((M,M)); bG = np.zeros(M)
d = np.eye(r)
def D1coeff(a_,b_):
    # returns dict col->coeff for D1[a_,b_] in terms of vec(D2)
    c = {}
    for k in range(r):
        c[idx(a_,k,b_,k)] = c.get(idx(a_,k,b_,k),0)+1.0/(N-1)
    return c
for p,q,rr,s in itertools.product(range(r),repeat=4):
    row = idx(p,q,rr,s)
    bQ[row] = d[q,s]*d[p,rr] - d[p,s]*d[q,rr]
    A_Q[row, idx(s,rr,q,p)] += 1.0
    for (a_,b_),sgn in [((rr,p),-d[q,s]),((rr,q),d[p,s]),((s,p),d[q,rr]),((s,q),-d[p,rr])]:
        if sgn!=0:
            for col,co in D1coeff(a_,b_).items(): A_Q[row,col]+=sgn*co
    bG[row] = 0.0
    A_G[row, idx(p,s,rr,q)] += -1.0
    for col,co in D1coeff(q,rr).items(): A_G[row,col]+=d[q,s]*0  # placeholder
    # G: + delta_qs * D1[p,rr]
    for col,co in D1coeff(p,rr).items(): A_G[row,col]+=d[q,s]*co

# sanity: re-derive Q,G from linear maps on exact d and compare
dvec = D2.reshape(M)
assert np.max(np.abs((A_Q@dvec+bQ)-Qx.reshape(M)))<1e-8
assert np.max(np.abs((A_G@dvec+bG)-Gx.reshape(M)))<1e-8
print("linear maps verified against exact.\n")

# permutation that swaps (p,q)->(q,p) on the 64-index pair space
Sigma = np.zeros((r*r,r*r))
for p in range(r):
    for q in range(r):
        Sigma[p*r+q, q*r+p]=1.0

# D1 as linear map on dvec (matrix 64 -> r*r)
A_D1 = np.zeros((r*r, M))
for a_ in range(r):
    for b_ in range(r):
        for col,co in D1coeff(a_,b_).items(): A_D1[a_*r+b_,col]+=co

def solve_DQG(U):
    dv = cp.Variable(M)
    Dm = cp.reshape(dv, (r*r,r*r), order='C')
    Qm = cp.reshape(A_Q@dv+bQ, (r*r,r*r), order='C')
    Gm = cp.reshape(A_G@dv+bG, (r*r,r*r), order='C')
    D1v = A_D1@dv
    cons = [Dm==Dm.T, Qm==Qm.T, Gm==Gm.T, Dm>>0, Qm>>0, Gm>>0,
            Sigma@Dm==-Dm, Dm@Sigma==-Dm]                 # antisymmetry
    # trace conditions
    tr_d2 = sum(dv[idx(p,q,p,q)] for p in range(r) for q in range(r))
    cons += [tr_d2==N*(N-1)]
    cons += [sum(D1v[p*r+p] for p in range(r))==N]
    # Sz=0: equal up/down occupancy
    cons += [sum(D1v[(2*x)*r+(2*x)] for x in range(nsite))==N/2]
    # energy
    e1 = sum(h[p,q]*D1v[p*r+q] for p in range(r) for q in range(r) if h[p,q]!=0)
    e2 = U*sum(dv[idx(2*x,2*x+1,2*x,2*x+1)] for x in range(nsite))
    prob = cp.Problem(cp.Minimize(e1+e2), cons)
    try:
        prob.solve(solver=cp.SCS, max_iters=20000, eps=1e-6)
    except Exception:
        prob.solve(solver=cp.CLARABEL)
    return prob.value

print(f"{'U/t':>5} {'E_exact':>12} {'E_DQG(LB)':>12} {'gap':>10} {'gap/|E|%':>9}")
for U in [0.0,1.0,2.0,4.0,8.0]:
    _,Eex = ground_state(U)
    Elb = solve_DQG(U)
    gap = Eex-Elb
    print(f"{U:>5.1f} {Eex:>12.5f} {Elb:>12.5f} {gap:>10.5f} {100*gap/abs(Eex):>8.3f}%")
