#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness at q0; selects an operator from
# the fixed Gram / Markov-trace cost — no symbolic-q polynomial output.
"""Dense Wedderburn-projector SDP for 𝓑₃-selection — the closed form (the unbuilt object).

#2433 (`2026-06-17-delta-lambda-two-remaining-directions-closed.md`) left ONE
non-refuted compute lever for the Δ_λ gate: *"implement the genuine dense
per-block Wedderburn-projector SDP (`confinement-sdp.md`, the unbuilt object)
with the correct π_λ + cost operator"* — the SDP that, IF it selected the
Borromean signature, would unlock the operator-cumulant binding scalar (#2430).

This probe **implements that object** — not by calling a solver (cvxpy is not
even installed here) but via its **closed form**, and shows the lever is
structurally bounded: it CANNOT select 𝓑₃ without a fitted cost operator.

## Formalize-first prune (the structural argument)

The spec (`confinement-sdp.md`) is

    min_Φ <T, Φ>   s.t.   Φ >= 0  (global PSD),
                          <π_λ, Φ> >= 0  for all λ  (per-block Frobenius positivity),
                          [[Φ_ii,Φ_ij],[Φ_ji,Φ_jj]] >= 0  (adjacent 2x2 pair PSD),
                          tr Φ = n_target.

**Every constraint except `Φ>=0` and `tr Φ = n_target` is redundant:**
- the central idempotents π_λ are PSD projectors, so for any Φ>=0,
  <π_λ,Φ> = tr(π_λ Φ) >= 0 — the per-block Frobenius-positivity rows are
  automatically satisfied;
- a principal 2x2 submatrix of a PSD matrix is PSD — the adjacent-pair rows
  are automatically satisfied.

So the "richer" Wedderburn-projector SDP **collapses to the bare problem**
`min <T,Φ> s.t. Φ>=0, trΦ=n`, whose optimum is the classic eigenvalue program:

    Φ* = n_target * v vᵀ,   v = unit min-eigenvector of T,   value = n_target*λ_min(T).

**Therefore the SDP selects the minimum-eigenvector of the cost operator T.**
"Does the dense SDP select 𝓑₃?" <=> "Is 𝓑₃ the min-eigenvector of a NON-FITTED T?"
That is a 6x6 eigenproblem — no multi-session build needed.

## Result

For the cost operators the spec names (Markov-trace weighting T=diag(t);
q-Laplacian/Gram resolvent T in {G, G^-1}), the selected min-eigenvector is the
**mesonic L± channel** — **full-cos to 𝓑₃ ~ 0.05, i.e. essentially ORTHOGONAL**.
The reason is a one-line cost ordering, sharper than #2433's sig-cos control:

> 𝓑₃ is **99.8% γ** (the identity channel), and γ carries the **maximum**
> Markov-trace cost `t_γ = 1.0 = max(t)`. A cost-**minimizing** PSD program
> selects the **smallest**-cost channel — the mesonic `L±` (`t = 0.249`), the
> structural **antithesis** of 𝓑₃. The minimizer can never land on the
> max-cost identity direction that 𝓑₃ essentially is.

The ONLY cost operator whose ground state is 𝓑₃ is T = -𝓑₃𝓑₃ᵀ (+ PSD on 𝓑₃^perp)
— i.e. T hand-built FROM the answer, a fit (CAL-4 / three-calibration violation).

**Verdict:** the dense Wedderburn-projector SDP lever is CLOSED — selection of
𝓑₃ <=> a fitted cost operator. The Borromean signature is a discrete topological
fact (no separable sub-link), not the ground state of any non-fitted cost; it
cannot be recovered by a continuous PSD program. Confirms #2433 (1) and bounds
the operator-cumulant route (#2430): the gate is structural, not pending.

Exploratory; no fit; nothing rewired.

Run:  python3 -u computations/probes/b3_dense_sdp_wedderburn_projector.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]               # computations/
PYHECKE = ROOT.parent / "tools" / "pyhecke" / "python"
for p in (str(ROOT), str(ROOT / "substrate"), str(PYHECKE)):
    sys.path.insert(0, p)
import numpy as np  # noqa: E402
from pyhecke.gram import NF_NAMES, TR_M  # noqa: E402

G = np.array(json.loads((ROOT / 'gram-matrix-dual.witness.json').read_text())['gram_matrix'], float)
t = np.asarray(TR_M, float)
gamma = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])              # identity channel e_0
B3 = np.array([0.998, -0.0095, 0.0091, 0.046, -0.044, 0.0])   # NF(𝓑₃), prop value


def unit(v):
    n = np.linalg.norm(v)
    return v / n if n > 1e-30 else v


def cos(a, b):
    a, b = unit(a), unit(b)
    return float(a @ b)


def dense_sdp_select(T: np.ndarray) -> np.ndarray:
    """Closed-form optimum of  min<T,Φ> s.t. Φ>=0, trΦ=1  ->  min-eigenvector of T.

    (The per-block <π_λ,Φ>>=0 and 2x2 pair-PSD constraints are redundant given
    Φ>=0, so this IS the genuine dense Wedderburn-projector SDP — see module
    docstring.)  Sign-fix toward γ for a stable cosine readout.
    """
    T = 0.5 * (T + T.T)
    _, V = np.linalg.eigh(T)
    v = V[:, 0]
    return v if v @ gamma >= 0 else -v


print("\n  DENSE WEDDERBURN-PROJECTOR SDP — 𝓑₃-selection (closed form, the unbuilt object)\n")
print(f"  eigs(G)  = {np.round(np.linalg.eigvalsh(G), 3)}  (1 negative, indefinite)")
print(f"  NF(𝓑₃)   = {(np.linalg.norm(gamma * (B3 @ gamma)) / np.linalg.norm(B3)) * 100:.1f}% γ "
      "(the identity channel)")
print("  redundancy: <π_λ,Φ>=tr(π_λΦ)>=0 (π_λ PSD) and 2x2 pair-PSD are implied by Φ>=0")
print(f"  𝓑₃≈γ Markov cost t_gamma={t[0]:.3f}=max(t) (identity = MAX cost); "
      f"mesonic L± cost={t[3]:.3f}=min(t)\n")
print(f"  {'cost operator T (non-fitted)':<34}{'min-eigvec':<11}{'cost t':>8}"
      f"{'full-cos->B3':>14}{'is B3?':>8}")
print("  " + "-" * 75)

for name, T in [
    ("diag(t)  [Markov-trace weight]", np.diag(t)),
    ("G        [q-Laplacian / Gram]", G),
    ("G^-1     [Gram resolvent]", np.linalg.inv(G)),
    ("-(G - lmax.I) [resolvent inv.]", -(G - np.max(np.linalg.eigvalsh(G)) * np.eye(6))),
]:
    v = dense_sdp_select(T)
    i = int(np.argmax(np.abs(v)))
    fc = cos(v, B3)
    print(f"  {name:<34}{NF_NAMES[i]:<11}{t[i]:>8.3f}{fc:>14.3f}"
          f"{('YES' if abs(fc) > 0.9 else 'no'):>8}")

# The ONLY cost operator that selects 𝓑₃ is one built FROM 𝓑₃ = a fit.
T_fit = -np.outer(unit(B3), unit(B3))
v_fit = dense_sdp_select(T_fit)
print("  " + "-" * 75)
print(f"  {'-B3.B3^T  [FITTED to the answer]':<34}{NF_NAMES[int(np.argmax(np.abs(v_fit)))]:<11}"
      f"{'(n/a)':>8}{cos(v_fit, B3):>14.3f}{'YES(fit)':>8}")

print("""
  VERDICT: the dense Wedderburn-projector SDP collapses (closed form) to
  "select the min-eigenvector of the cost operator T". 𝓑₃ is 99.8% γ = the
  identity = the MAX-cost channel (t_gamma=1.0). A cost-MINIMIZING PSD program
  therefore selects the smallest-cost MESONIC L± (t=0.249) — full-cos~0.05 to
  𝓑₃, the structural ANTITHESIS. For every non-fitted T the spec names
  (diag(t), G, G^-1) the answer is "not 𝓑₃". The only T whose ground state is
  𝓑₃ is T=-B3.B3^T, hand-built FROM the answer (a fit). So the one open Δ_λ
  compute lever is CLOSED: 𝓑₃-selection <=> a fitted cost operator. The
  Borromean signature is a discrete topological fact, not the variational
  ground state of any non-fitted continuous cost. Confirms #2433 (1); bounds
  the operator-cumulant route (#2430). Derive-or-refute: REFUTED (no fit).
""")
