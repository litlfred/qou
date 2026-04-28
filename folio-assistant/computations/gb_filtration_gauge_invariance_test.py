#!/usr/bin/env python3
"""GB filtration gauge-invariance test.

Compare depth-stratum decomposition Σ_{depth(λ)=k} y_λ in TWO Hecke
conventions:

  (A) σ-convention: σ² = (q − q⁻¹)σ + 1, eigenvalues (q, −q⁻¹),
      z_my = 1/(q^{1/2} + q^{−1/2}).
  (B) Wenzl/GL g-convention: g² = (Q − 1)g + Q, eigenvalues (Q, −1),
      z_GL = q · z_my, with Q = q².

Both define the SAME GB filtration (depth-k strata are partition-
combinatorial, NOT convention-dependent). What may differ is the
y_λ values themselves and hence the per-stratum sums.

Test:
- Compute y_λ_my from existing witness (already in σ-convention).
- Compute y_λ_GL from Wenzl's Schur-element formula at Q = q² with
  the corresponding r (solving z_GL = Q^r(1-Q)/(1-Q^r)).
- Bin both by depth(λ) = height(λ) - 1.
- Compare per-stratum sums.

If the gauge-invariance hypothesis holds, the strata STRUCTURE
(geometric decay, alternating signs) is preserved. Absolute values
will differ.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
import mpmath as mp

mp.mp.dps = 30
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q0_FLOAT

q = mp.mpf(repr(Q0_FLOAT))
z_my = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))

# Wenzl convention parameters
Q_W = q**2
z_GL = q * z_my  # convention shift from G = qσ

print("=" * 80)
print("GB FILTRATION GAUGE-INVARIANCE TEST")
print("=" * 80)
print(f"My σ-convention:    q     = {float(q):.10f}, z_my  = {float(z_my):.10f}")
print(f"Wenzl g-convention: Q=q² = {float(Q_W):.10f}, z_GL  = {float(z_GL):.10f}")
print()

# Solve for r in Wenzl: z_GL = Q^r (1-Q) / (1-Q^r)
# X = Q^r → X(1-Q) = z_GL (1-X) → X(1-Q+z_GL) = z_GL → X = z_GL/(1-Q+z_GL)
X = z_GL / (1 - Q_W + z_GL)
r_W = mp.log(X) / mp.log(Q_W)
print(f"Wenzl level r = log(X)/log(Q) = {float(r_W):.6f}  (X = Q^r = {float(X):.6f})")
print()


def n_partition(lam):
    return sum(i * lami for i, lami in enumerate(lam))


def hooks_contents(lam):
    hs, cs = [], []
    rows = len(lam)
    for i in range(rows):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            hs.append(arm + leg + 1)
            cs.append(j - i)
    return hs, cs


def hook_dim(lam):
    """f^λ via hook formula (classical S_n irrep dim)."""
    n = sum(lam)
    hs, _ = hooks_contents(lam)
    from math import factorial
    prod = 1
    for h in hs: prod *= h
    return factorial(n) // prod


def schur_principal(lam, r, Q):
    """s_λ(1, Q, Q², ..., Q^{r-1}) = Q^{n(λ)} · ∏ (1 - Q^{r+c})/(1 - Q^h)"""
    hs, cs = hooks_contents(lam)
    num = mp.mpf(1); den = mp.mpf(1)
    for h, c in zip(hs, cs):
        num *= (1 - Q**(r + c))
        den *= (1 - Q**h)
    return Q**n_partition(lam) * num / den


# Load witness y_λ (σ-convention)
with open(Path(__file__).parent / "y-lambda-jones-markov-witness.json") as f:
    W = json.load(f)


def partitions_at(n_str):
    return [(tuple(w["partition"]), mp.mpf(str(w["y_lambda"])))
            for w in W["tables_by_n"][n_str]["weights"]]


# Compute Wenzl y_λ from Schur-element formula, normalized so Σ y · d = 1
def wenzl_y_lambda(n):
    parts = partitions_at(str(n))
    # Compute s_λ for each partition
    s_vals = {}
    for lam, _ in parts:
        s = schur_principal(lam, r_W, Q_W)
        s_vals[lam] = s
    # Normalize: tr(1) = Σ y · d = 1
    Z = sum(s_vals[lam] * hook_dim(lam) for lam, _ in parts)
    return {lam: s_vals[lam] / Z for lam, _ in parts}


# Per-n comparison of depth-stratum sums
print(f"{'n':>3}  Convention  " + "  ".join(f"k={k:>2}" for k in range(7)))
print("-" * 80)
for n in [3, 4, 5, 6, 7, 8, 9]:
    parts_my = partitions_at(str(n))
    by_depth_my = {}
    for lam, y in parts_my:
        d = len(lam) - 1
        by_depth_my[d] = by_depth_my.get(d, mp.mpf(0)) + y

    y_W = wenzl_y_lambda(n)
    by_depth_GL = {}
    for lam, _ in parts_my:
        d = len(lam) - 1
        by_depth_GL[d] = by_depth_GL.get(d, mp.mpf(0)) + y_W[lam]

    # Print
    line_my = f"{n:>3}  σ-conv:    "
    line_GL = f"     g-conv:    "
    line_diff = f"     diff:      "
    for k in range(7):
        line_my += f"{float(by_depth_my.get(k, 0)):>+13.10f}  "
        line_GL += f"{float(by_depth_GL.get(k, 0)):>+13.10f}  "
        d = by_depth_my.get(k, mp.mpf(0)) - by_depth_GL.get(k, mp.mpf(0))
        line_diff += f"{float(d):>+13.4e}  "
    print(line_my)
    print(line_GL)
    print(line_diff)

    print()

# Output witness
out = {
    "computation": "gb-filtration-gauge-invariance-test",
    "description": (
        "Compares depth-stratum sums Σ_{depth(λ)=k} y_λ in σ-convention "
        "(my y_λ from witness) vs g-convention (Wenzl Schur-element "
        "formula at Q=q², r solved from z_GL=q·z_my). Tests whether the "
        "GB filtration is a gauge-invariant structure (yes by construction; "
        "y_λ values differ but stratum partition is identical) — and "
        "whether stratum-sum ratios are constant across n."
    ),
    "q_my": float(q),
    "z_my": float(z_my),
    "Q_W": float(Q_W),
    "z_GL": float(z_GL),
    "r_W": float(r_W),
    "precision": "f64_numeric_fallback",
    "truncation_eps": 0.0,
}
out_path = Path(__file__).parent / "gb-filtration-gauge-invariance.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2, default=str)
print(f"Witness: {out_path}")
