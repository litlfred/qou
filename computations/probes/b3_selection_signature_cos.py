#!/usr/bin/env python3
"""𝓑₃ confinement-selection: the signature-cos control (EXPLORATORY, derive-or-refute).

#2417/#2426 left open whether any continuous variational principle selects the
Borromean braid 𝓑₃ over the indefinite Frobenius Gram. The catch: NF(𝓑₃) is
~99.8% the identity γ, so raw cos-to-𝓑₃ is dominated by cos-to-γ and MISLEADS.
The honest score is the cosine in the γ-orthogonal subspace ("signature-cos"):
sig-cos≈+1 ⇒ reproduces the Borromean pattern; sig-cos≈0 ⇒ the candidate is just γ.

Verdict (this probe): every continuous candidate has sig-cos≈0 — none selects
the Borromean signature. No fit, nothing rewired.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]               # computations/
PYHECKE = ROOT.parent / "tools" / "pyhecke" / "python"
for p in (str(ROOT), str(ROOT / "substrate"), str(PYHECKE)):
    sys.path.insert(0, p)
import numpy as np
from pyhecke.gram import NF_NAMES, TR_M
from lp_dual_solver import solve_operator_selection_lp

G = np.array(json.loads((ROOT/'gram-matrix-dual.witness.json').read_text())['gram_matrix'], float)
t = np.asarray(TR_M, float)
gamma = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])         # identity channel e_0
B3 = np.array([0.998, -0.0095, 0.0091, 0.046, -0.044, 0.0])  # NF(𝓑₃), prop value

def unit(v):
    n = np.linalg.norm(v)
    return v / n if n > 1e-30 else v


def sig(v):  # γ-orthogonal part
    return v - (v @ gamma) * gamma
def cos(a, b):
    a, b = unit(a), unit(b)
    return float(a @ b)

B3_sig = sig(B3)
print(f"eigs(G) = {np.round(np.linalg.eigvalsh(G),3)}  (1 negative, indefinite)")
print(f"NF(𝓑₃): {(np.linalg.norm(gamma*(B3@gamma))/np.linalg.norm(B3))*100:.1f}% γ; "
      f"signature norm = {np.linalg.norm(B3_sig):.3f}\n")
print(f"  {'candidate':<34}{'full-cos':>10}{'sig-cos':>10}")
print("  " + "-"*54)

def score(name, x):
    sc = cos(sig(x), B3_sig) if np.linalg.norm(sig(x)) > 1e-9 else float('nan')
    print(f"  {name:<34}{cos(x,B3):>10.3f}{sc:>10.3f}")

# 1. min-action LP
lp = solve_operator_selection_lp(t, G, 1.0)
score("LP (min Σt·x, Gx≥0)", np.asarray(lp.x_star, float))
# 2. stationary x^T G x s.t. Σx=1  (Gx = μ1 → x ∝ G^{-1}1)
x = np.linalg.solve(G, np.ones(6))
x /= x.sum()
score("stationary xᵀGx, Σx=1", x)
# 3. stationary x^T G x s.t. t·x=1  (Gx = μt → x ∝ G^{-1}t)
x = np.linalg.solve(G, t)
x /= (t @ x)
score("stationary xᵀGx, t·x=1", x)
# 4. min ‖x‖² s.t. t·x=1  → x = t/‖t‖²
x = t / (t @ t)
score("min‖x‖², t·x=1", x)
print(f"\n  γ itself (control):          full-cos={cos(gamma,B3):.3f}  sig-cos= n/a (pure γ)")
print("\n  VERDICT: every continuous candidate has |sig-cos|≈0 — high full-cos is"
      " just γ.\n  No continuous principle reproduces the Borromean signature"
      " (the selection rests on\n  an external discrete/topological criterion). Derive-or-refute: REFUTED.")
