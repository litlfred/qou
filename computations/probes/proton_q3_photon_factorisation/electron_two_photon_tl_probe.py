"""Electron sigma0 sigma1 sigma0 as a two-photon product in the TL quotient of H_3(q).

Photon (owner ruling 2026-11-20): gamma(a,b,c) = 1 + a sigma0 + b sigma1 + c sigma0 sigma1^{-1}.

H_3(q) has three blocks: trivial (sigma -> q), sign (sigma -> -1/q) and the 2-dim
block.  On (C^2)^{(x)3} (Jimbo U_q(sl2) check-R) only the trivial and 2-dim blocks
occur (Schur-Weyl for sl2: partitions (3) and (2,1); convention D, y_(1^3) = 0).
The Lean file ElectronNotTwoPhoton.lean proves the electron is NOT a two-photon
product in H_3(q) with all three blocks.  This probe shows that when the sign
block is dropped (TL quotient), exact two-photon factorisations exist at generic q.

Exact symbolic arithmetic (sympy, symbol q); no floats.  Checks, for each family:
  * gamma1 * gamma2 = lam * E on the 2-dim block (identically in q),
  * triv(gamma1) triv(gamma2) = lam q^3 (identically in q),
  * lam != 0 as a rational function,
  * the sign-block mismatch sign(g1) sign(g2) + lam/q^3 is a nonzero rational
    function (consistent with the H_3 negative).
"""
import json, sys
import sympy as sp

q = sp.symbols('q')
a, b, c, a2, b2, c2, lam = sp.symbols('a b c a2 b2 c2 lam')
S0 = sp.Matrix([[q, 0], [1, -1/q]]); S1 = sp.Matrix([[-1/q, 1], [0, q]])
S1i = sp.Matrix([[-q, 1], [0, 1/q]]); I2 = sp.eye(2)
assert sp.simplify(S1*S1i - I2) == sp.zeros(2)
M = lambda x, y, z: I2 + x*S0 + y*S1 + z*S0*S1i
triv = lambda x, y, z: 1 + q*(x + y) + z          # sigma0 sigma1^{-1} -> 1
sign = lambda x, y, z: 1 - (x + y)/q + z          # sigma0 sigma1^{-1} -> 1
E = S0*S1*S0

P = M(a, b, c)*M(a2, b2, c2)
eqs = [sp.numer(sp.together(sp.expand(P[i, j] - lam*E[i, j]))) for i in range(2) for j in range(2)]
eqs.append(sp.expand(triv(a, b, c)*triv(a2, b2, c2) - lam*q**3))

# consistency condition on gamma1 (5 linear eqs in a2,b2,c2,lam)
A_, bv = sp.linear_eq_to_matrix(eqs, [a2, b2, c2, lam])
cond = sp.factor(A_.row_join(bv).det())
f0 = [f for f, _ in sp.factor_list(cond)[1] if f.has(a) and f.has(b) and f.has(c)][0]

out = {"probe": "electron_two_photon_tl", "photon": "1 + a s0 + b s1 + c s0 s1^-1",
       "consistency_factor": str(f0), "families": []}
ok = True
for cv in (sp.Integer(1), sp.Integer(-1)):
    bsol = sp.solve(f0.subs({a: 0, c: cv}), b)[0]
    sub = {a: 0, b: bsol, c: cv}
    sols = sp.solve([sp.simplify(e.subs(sub)) for e in eqs], [a2, b2, c2, lam], dict=True)
    for so in sols:
        g1 = (sp.Integer(0), bsol, cv); g2 = tuple(so[v] for v in (a2, b2, c2)); L = so[lam]
        blk = sp.simplify(M(*g1)*M(*g2) - L*E) == sp.zeros(2)
        tv = sp.simplify(triv(*g1)*triv(*g2) - L*q**3) == 0
        lnz = sp.simplify(L) != 0
        mism = sp.factor(sign(*g1)*sign(*g2) + L/q**3)
        fam = {"gamma1": [str(sp.factor(v)) for v in g1], "gamma2": [str(sp.factor(v)) for v in g2],
               "lambda": str(sp.factor(L)), "block2_ok": blk, "triv_ok": tv,
               "lambda_nonzero": lnz, "sign_mismatch": str(mism), "sign_mismatch_nonzero": mism != 0}
        ok &= blk and tv and lnz and (mism != 0)
        out["families"].append(fam)
        print(json.dumps(fam, indent=1))
out["all_checks_pass"] = bool(ok)
json.dump(out, open(__file__.replace('_probe.py', '_result.json'), 'w'), indent=1)
print("all_checks_pass:", ok)
sys.exit(0 if ok else 1)
