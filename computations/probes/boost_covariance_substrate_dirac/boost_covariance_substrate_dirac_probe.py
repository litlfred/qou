#!/usr/bin/env python3
"""Route-2b test on the corpus's concrete Dirac operator (bean qou-2k68).

substrateDirac (QOU/LiftingDescent/ChenMultiplicativeIntegralBridge.lean):
  nablaEndo = ad_Omega : X -> Omega X - X Omega        (Mat_{d+2})
  reeb      = R_{M,N}  : X -> X_11 E_01 + X_01 M + (X_00 - X_11) N
Traced square of D = W_H ad + W_R R, with tau = trace of the endomorphism as a linear map:
  A = tau(R^2), B = tau(ad R + R ad), C = tau(ad^2).
QOU.Core.BoostCovarianceRigidity: boost covariance <=> B = 0 and A = -c_q^2 C; with
q-independent data it can hold for at most one q unless A = C = 0.

PRE-REGISTERED (before the first run):
  P5  A, B, C are not identically zero as polynomials in the entries of Omega, M, N (d+2 = 2).
  P6  hence covariance at q0 would be one polynomial equation on the substrate data that
      also fixes c_q, i.e. q; choosing data to satisfy it is selection, and reading q off
      it would derive q0 from the substrate (forbidden, owner ruling 2026-08-02).
Exact sympy; no floats.
"""
import json
from pathlib import Path
import sympy as sp

n = 2
Om = sp.Matrix(n, n, sp.symbols("w0:4"))
M = sp.Matrix(n, n, sp.symbols("m0:4"))
N = sp.Matrix(n, n, sp.symbols("n0:4"))
basis = [(i, j) for i in range(n) for j in range(n)]


def E(i, j):
    X = sp.zeros(n, n); X[i, j] = 1; return X


def ad(X):
    return Om * X - X * Om


def R(X):
    return X[1, 1] * E(0, 1) + X[0, 1] * M + (X[0, 0] - X[1, 1]) * N


def matrix_of(f):
    cols = []
    for (i, j) in basis:
        Y = f(E(i, j))
        cols.append([Y[k, l] for (k, l) in basis])
    return sp.Matrix(cols).T


Ad = matrix_of(ad)
Rm = matrix_of(R)
A = sp.expand((Rm * Rm).trace())
B = sp.expand((Ad * Rm + Rm * Ad).trace())
C = sp.expand((Ad * Ad).trace())
print("A = tau(R^2)     =", A)
print("B = tau({ad,R})  =", B)
print("C = tau(ad^2)    =", C)
P5 = all(e != 0 for e in (A, B, C))
print("P5 (A, B, C all non-zero polynomials):", P5)
q = sp.symbols("q", positive=True)
cond = sp.simplify(A + C / (q - 1) ** 2)
print("covariance condition: B = 0 and", cond, "= 0")
out = {"description": "qou-2k68 route 2b: traced square of substrateDirac at d+2=2",
       "A": str(A), "B": str(B), "C": str(C), "P5": P5,
       "covariance_condition": ["B = 0", f"{cond} = 0"]}
Path(__file__).with_name("boost-covariance-substrate-dirac.witness.json").write_text(json.dumps(out, indent=2) + "\n")
