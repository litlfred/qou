"""Exploration (not a target test; no measured value, no 12 search). Exact sympy, no floats.

Which choices of connection nabla = F(hol) change the n - p structure? For F a function of hol,
p and n stay conjugate, and Delta_F = tr_n(D_F^2) - tr_p(D_F^2) = -2 q^-1 (1 - q^-1) tr_p F(hol)
(Lean: DeltaNPMatrixIdentity.delta_np_general). So only tr_p F matters.
Spectrum of hol on W_p: {1, e^{i theta}, e^{-i theta}}, det = 1 (from the charpoly).
"""
import json, itertools, sympy as sp

q = sp.symbols('q', positive=True)
Rc = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,q-1/q,0],[0,0,0,q]])
I2 = sp.eye(2)
s0 = sp.kronecker_product(Rc, I2); s1 = sp.kronecker_product(I2, Rc)
hol8 = sp.simplify((s0*s1.inv())**3)
basis = list(itertools.product([0,1], repeat=3))
idx = [i for i,b in enumerate(basis) if b.count(0) == 2]
H = sp.simplify(hol8.extract(idx, idx)); Hi = sp.simplify(H.inv()); I3 = sp.eye(3)
h = q - 1/q; t3 = q**2 + 1 + q**-2
res = {"det_hol_p": str(sp.factor(sp.simplify(H.det()))), "candidates": {}}
alg = {"hol - 1": H - I3,
       "(hol - hol^-1)/2  (odd under hol -> hol^-1)": (H - Hi)/2,
       "(hol + hol^-1)/2 - 1  (even under hol -> hol^-1)": (H + Hi)/2 - I3}
for name, F in alg.items():
    tr = sp.factor(sp.simplify(F.trace()))
    res["candidates"][name] = {"tr_p_F": str(tr), "equals -h^4[3]_q": sp.simplify(tr + h**4*t3) == 0,
                               "Delta_F": str(sp.factor(-2/q*(1-1/q)*tr))}
res["candidates"]["log hol  (principal branch, elliptic range)"] = {
    "tr_p_F": "0 (eigenvalues 0, i theta, -i theta; det hol = 1)", "Delta_F": "0"}
res["note"] = ("Only the part of F even under hol -> hol^-1 (not the q -> q^-1 bar) reaches Delta. hol - 1 and its inversion-even "
               "symmetrisation give the same Delta; log hol and the inversion-odd part give Delta = 0.")
s = json.dumps(res, indent=2); print(s)
open(__file__.replace('.py', '.out.json'), 'w').write(s + "\n")
