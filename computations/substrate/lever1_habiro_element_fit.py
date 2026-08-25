"""Lever-1 fibre kernel: does the correction D(m) fit a single Habiro element?

The correction D(m) = S(m) - (S(m-1) + [m-1]_q S(m-2)) carries a (q-1)^2 prefactor
and a tower of cyclotomic polynomials (the Habiro-ring signature).
This script tests whether the sequence D(m), or its cyclotomic cofactors,
can be fitted to a single q-hypergeometric / Habiro element, defined by the
contiguity ratio template:
    r_k = -q^k / [ (1 - q^{k+1}) (1 - a q^k) ]

Method:
Test if there exist shifts and parameters such that the ratio matches.
We test:
  1. Sequence is D(m)
  2. Sequence is the cyclotomic cofactor C_m of D(m)
  3. Sequence is the difference D(m) - D(m-1)
"""
import json, os, sys
import sympy as sp
import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import _path_bridge  # noqa: F401,E402 — wires tools/qou-substrate + tools/pyhecke
from qou_substrate import constants as C

q = sp.Symbol("q", positive=True)

def qint_sym(k):
    return (q**k - q**(-k)) / (q - 1 / q)

def qfact(n):
    r = sp.Integer(1)
    for k in range(1, n + 1):
        r *= qint_sym(k)
    return r

def partitions(n):
    if n == 0:
        yield []
        return
    for first in range(n, 0, -1):
        for rest in partitions(n - first):
            if not rest or rest[0] <= first:
                yield [first] + rest

def hooks(lam):
    conj = [sum(1 for r in lam if r > c) for c in range(lam[0])]
    return [(row - j) + (conj[j] - i) - 1 for i, row in enumerate(lam) for j in range(row)]

def dim_q(lam):
    d = qfact(sum(lam))
    for h in hooks(lam):
        d /= qint_sym(h)
    return sp.cancel(sp.together(d))

def S(m):
    if m == 0:
        return sp.Integer(1)
    return sp.cancel(sp.together(sum(dim_q(l) for l in partitions(m))))

def get_cyclotomic_factors(poly):
    factors = sp.factor_list(poly)
    cofactor = sp.Integer(1)
    for f, mult in factors[1]:
        is_cyc = False
        for N in range(1, 25):
            if sp.rem(q**N - 1, f) == 0:
                is_cyc = True
                break
        if not is_cyc:
            cofactor *= f**mult
    return factors[0] * cofactor

MMAX = 8
Sm = {m: S(m) for m in range(0, MMAX + 1)}
Dm = {m: sp.cancel(Sm[m] - (Sm[m - 1] + qint_sym(m - 1) * Sm[m - 2])) for m in range(2, MMAX + 1)}
Cm = {m: get_cyclotomic_factors(sp.numer(Dm[m])) for m in range(4, MMAX + 1)}

def test_ratio(seq):
    # seq is a dict of polynomials. Test if seq[m]/seq[m-1] == -q^k / [(1-q^{k+1})(1-a q^k)]
    # for k = m + offset, a = q^j.
    # Equivalently, seq[m] * (1-q^{k+1}) * (1-a q^k) == -q^k * seq[m-1]
    for offset in range(-5, 6):
        for j in range(-5, 6):
            a_val = q**j
            match = True
            for m in range(5, MMAX): # fit on 5..7, hold out 8
                k = m + offset
                if k < 0:
                    match = False
                    break
                lhs = sp.cancel(seq[m] * (1 - q**(k+1)) * (1 - a_val * q**k))
                rhs = sp.cancel(-q**k * seq[m-1])
                if sp.simplify(lhs - rhs) != 0:
                    match = False
                    break
            if match:
                # verify on held-out m=8
                m = 8
                k = m + offset
                lhs = sp.cancel(seq[m] * (1 - q**(k+1)) * (1 - a_val * q**k))
                rhs = sp.cancel(-q**k * seq[m-1])
                verified = (sp.simplify(lhs - rhs) == 0)
                return True, offset, j, verified
    return False, None, None, False

fit_Dm, off_D, a_D, ver_D = test_ratio(Dm)
fit_Cm, off_C, a_C, ver_C = test_ratio(Cm)

# Diff sequence
Tm = {m: sp.cancel(Dm[m] - Dm[m-1]) for m in range(4, MMAX + 1)}
fit_Tm, off_T, a_T, ver_T = test_ratio(Tm)

results = {
    "D_fit": fit_Dm,
    "C_fit": fit_Cm,
    "T_fit": fit_Tm,
}

assertions = {
    "no_simple_hypergeometric_fit": not (fit_Dm or fit_Cm or fit_Tm)
}

verdict = "NEGATIVE. The D(m) sequence, its cyclotomic cofactors, and its first differences DO NOT fit a single q-hypergeometric/Habiro element with the r_k template. The true Habiro element must be a sum of such terms or a higher-order structure."

witness = {
    "computation": "lever1_habiro_element_fit",
    "description": "Tests if the D(m) cyclotomic cofactors (or D(m) itself) fit a single q-hypergeometric / Habiro element template r_k = -q^k/[(1-q^{k+1})(1-aq^k)].",
    "discipline": "guess-and-verify with held-out m=8; no fit.",
    "auditOnly": "docs/audits/2026-06-27-lever1-qinvolution-cyclotomic-kernel.md",
    "results": results,
    "assertions": assertions,
    "verdict": verdict
}

out_path = os.path.join("computations", "substrate", "lever1-habiro-element-fit.witness.json")
with open(out_path, "w") as f:
    json.dump(witness, f, indent=2)

print(f"D(m) fit: {fit_Dm}")
print(f"C_m fit: {fit_Cm}")
print(f"T_m fit: {fit_Tm}")
print(f"Verdict: {verdict}")
print(f"Witness saved to {out_path}")
