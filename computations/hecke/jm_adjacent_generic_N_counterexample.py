"""Refutes the "arbitrary N" reading of the JM adjacent-commutator normal forms.

`HeckeJucysMurphyAdjacentNormalForm.lean` proves

    L_{k+1} L_{k+2} = (uv) N (uv) N (uv)        u = sigma_k, v = sigma_{k+1}, N = L_k
    L_{k+2} L_{k+1} = (uvu) N (uv) N u

It is tempting to read the remaining question as "does this hold for ANY N commuting
with v?".  IT DOES NOT.  N = v itself commutes with v and fails, so the identity needs
L_k's structure, not merely its commutation with v.

Method: the 2-dimensional irrep of H_3(q) (lambda = (2,1)), EXACT rational arithmetic
via fractions.Fraction at q = 2 -- no float64 anywhere, per the repo precision rules.
A single exact counterexample refutes a claimed identity.

The N = 1 line is a CONTROL: Lean proves that case, so a harness reporting False there
is broken.  It caught exactly that -- a first version of this script compared the
uncancelled left form against the cancelled right form and reported False for N = 1.
Keep the control.

Emits no witness: this is a refutation of a reading, not a measured quantity.
"""
from fractions import Fraction as F
q = F(2); qi = F(1,2); h = q - qi
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def eq(A,B): return all(A[i][j]==B[i][j] for i in range(2) for j in range(2))
I = [[F(1),F(0)],[F(0),F(1)]]
def prod(*Ms):
    R = I
    for M in Ms: R = mm(R,M)
    return R
u = [[q, F(1)], [F(0), -qi]]
v = [[-qi, F(0)], [F(1), q]]
assert eq(prod(u,v,u), prod(v,u,v))
uv = mm(u,v); uvu = prod(u,v,u)

# UNCANCELLED normal forms, exactly as the Lean theorems state them
def L(N): return prod(uv, N, uv, N, uv)      # (uv) N (uv) N (uv)
def Rt(N): return prod(uvu, N, uv, N, u)     # (uvu) N (uv) N u
# CANCELLED forms (drop the leading uv from both)
def Lc(N): return prod(N, uv, N, uv)
def Rc(N): return prod(u, N, uv, N, u)

print("--- control: N = 1 (Lean PROVES this case) ---")
print("uncancelled equal:", eq(L(I), Rt(I)))
print("cancelled   equal:", eq(Lc(I), Rc(I)))
print("cancellation is consistent:", eq(L(I), mm(uv, Lc(I))) and eq(Rt(I), mm(uv, Rc(I))))

print("--- N = v : commutes with v, but is NOT a JM element ---")
print("uncancelled equal:", eq(L(v), Rt(v)))
print("cancelled   equal:", eq(Lc(v), Rc(v)))

print("--- N = the real JM element L_k for k=1, i.e. u_prev^2 is not in this 2-dim rep; use N=1 only ---")
