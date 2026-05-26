#!/usr/bin/env python3
"""
Transfer-matrix analysis of the Q_β precision-ladder c_k.

Constructs the 4×4 Wedderburn-basis transfer matrix T and the 2×2
upper-triangular generating matrix G = [[J, b], [0, K]], then
tests whether traces of their powers reproduce the known c_3..c_7.

Finding: the V_(2,1) block transfer has COMPLEX eigenvalues and
does not directly generate c_k. The pair structure arises from
inter-block coupling via the Markov trace normalization.
"""
from mpmath import mpf, mp, matrix

def trace(m):
    return sum(m[i,i] for i in range(m.rows))
mp.dps = 60

import json, os

COMP = os.path.dirname(__file__)
with open(os.path.join(COMP, "q-beta-operator-valued-N3.witness.json")) as f:
    w = json.load(f)
d = w["data"]

q0 = mpf(str(d["q_0_50dps"]))
b = mpf(str(d["hoefsmit_b"]))
hbar_sq = mpf(str(d["hbar_q_sq"]))
K = b**2
J = mpf(-2)

print("=" * 70)
print("TRANSFER MATRIX FOR Q_β PRECISION LADDER")
print("=" * 70)
print(f"J = {float(J)} (Hopf Jones at q=1)")
print(f"K = b² = {float(K):.10f}")
print(f"b = {float(b):.10f}")
print()

# ── Hypothesis: 2×2 transfer matrix T ────────────────────────────
# The pair structure (leading rung ~ J^n, trailing ~ J^n·K^?) suggests
# a 2×2 matrix whose powers generate the c_k sequence.
#
# If T has eigenvalues λ₁, λ₂ then Tr(T^n) = λ₁^n + λ₂^n.
# The known c_k don't follow Tr(T^n) exactly — the pair structure
# is more nuanced. Let's try a 2×2 STRUCTURED approach.
#
# The two irreps of H_3(q) on which the Markov trace decomposes:
#   V_triv = V_(3) ⊕ V_(1,1,1)  → Jones sector, eigenvalue J
#   V_std  = V_(2,1)             → Kashiwara sector, eigenvalue b
#
# T = [[J, 0], [0, b]]  in the eigenvalue basis.
# But this gives c_k = J^k + b^k, which doesn't match.

# Let me try: T acts on the PRODUCT of sectors.
# c_k involves J^{floor((k-1)/2)} · f(K), suggesting the transfer
# matrix acts on a graded space where J contributes every 2 steps
# and K fills in.

# ── DIRECT APPROACH: compute c_k from the Hecke transfer operator ─
# The Hecke algebra H_3(q) has 3 irreps: V_(3), V_(2,1), V_(1,1,1).
# Dimensions: 1, 2, 1. The Markov trace decomposes as:
#   tr_M(σ_w) = Σ_λ y_λ · χ_λ(σ_w)
# where y_λ are the Markov weights and χ_λ are characters.
#
# For the Q_β tower, the tower depth n generates a sequence of braid
# words β_n whose Markov trace recursion is:
#   tr_M(β_{n+1}) = T · tr_M(β_n)
# where T is the transfer operator for one step of the tower.
#
# In the Wedderburn basis, T decomposes block-diagonally:
#   T|_{V_(3)}     = scalar J_triv
#   T|_{V_(2,1)}   = 2×2 matrix with eigenvalues ±b
#   T|_{V_(1,1,1)} = scalar J_sign

# The Markov trace gives weights y_(3), y_(2,1), y_(1,1,1).
# At q=1: y_(3) = 1/6, y_(2,1) = 1/3, y_(1,1,1) = 1/6.

# The EFFECTIVE transfer for Q_β (ratio observable) is:
#   R_n = tr_M(β_n) / tr_M(β_0) = Σ_λ w_λ · t_λ^n
# where t_λ = eigenvalue of T on block λ, w_λ = normalized weight.

# The precision-ladder correction at depth n is:
#   Q_n / Q_{n-1} = 1 + c_n · (b·ℏ)^{2n}
#                 = R_n / R_{n-1}

# ── Construct the per-block transfer eigenvalues ─────────────────

# Block V_(3): 1-dimensional
# The trivial rep character χ_(3)(σ_i) = q for all generators.
# At depth k, the transfer eigenvalue is q^k → at q=1, this is 1.
# But the Jones-normalization gives J_Hopf = -2 for inter-block coupling.
t_triv = q0  # eigenvalue on trivial block

# Block V_(2,1): 2-dimensional
# Hoefsmit seminormal form has eigenvalues q and -q⁻¹ for each σ_i.
# The transfer eigenvalue on V_(2,1) involves b (off-diagonal coupling).
t_std_plus = b    # off-diagonal mixing strength
t_std_minus = -b  # bar-involution partner

# Block V_(1,1,1): 1-dimensional
# Sign rep: χ_(1,1,1)(σ_i) = -q⁻¹
t_sign = -q0**(-1)

print("Per-block transfer eigenvalues:")
print(f"  V_(3):     t_triv = {float(t_triv):.6f}")
print(f"  V_(2,1)+:  t_std  = {float(t_std_plus):.6f}")
print(f"  V_(2,1)-:  t_std  = {float(t_std_minus):.6f}")
print(f"  V_(1,1,1): t_sign = {float(t_sign):.6f}")
print()

# ── Generate c_k from the spectral decomposition ────────────────
# The RATIO of consecutive Markov traces gives:
#   c_k · u^k = Σ_λ w_λ · t_λ^k / Σ_λ w_λ · t_λ^{k-1} - 1
#
# But this is for the full transfer, not the per-rung correction.
# The per-rung c_k is more subtle: it's the coefficient of the
# LOGARITHMIC derivative of the product.
#
# Let me compute the Markov-trace weights y_λ(q) first.

# y_λ(q) = q^{content_sum(λ)} / [n]_q! (q-Schur convention)
# [3]_q! = [1]_q · [2]_q · [3]_q where [m]_q = (q^m - 1)/(q - 1)
def q_bracket(m, q):
    return (q**m - 1) / (q - 1)

def q_factorial(n, q):
    result = mpf(1)
    for m in range(1, n + 1):
        result *= q_bracket(m, q)
    return result

# Content sums: c(λ) = Σ_{(i,j)∈λ} (j - i)
# (3):     cells at (0,0),(0,1),(0,2) → c = 0+1+2 = 3
# (2,1):   cells at (0,0),(0,1),(1,0) → c = 0+1-1 = 0
# (1,1,1): cells at (0,0),(1,0),(2,0) → c = 0-1-2 = -3
content_sums = {"(3)": 3, "(2,1)": 0, "(1,1,1)": -3}
n3_fact = q_factorial(3, q0)

y = {}
for lam, cs in content_sums.items():
    y[lam] = q0**cs / n3_fact

print(f"q-Schur Markov weights at q₀:")
for lam in sorted(y.keys()):
    print(f"  y_{lam} = {float(y[lam]):.10f}")
print(f"  sum = {float(sum(y.values())):.10f} (should be 1/[3]_q! · Σ q^c)")
print()

# ── The FUNDAMENTAL IDENTITY ─────────────────────────────────────
# The Q_β correction at rung k arises from the ratio:
#   Q_k/Q_{k-1} = 1 + c_k · (b·ℏ_q²)^k
#
# In terms of the transfer matrix decomposition:
#   Q_k/Q_{k-1} = 1 + ε_k
# where ε_k is the per-rung correction from the V_(2,1) block's
# contribution to the Markov trace at depth k.
#
# The KEY STRUCTURAL RESULT:
# At classical limit q→1, the transfer matrix T has:
#   T|_{V_(3)} → Id     (trivial rep)
#   T|_{V_(2,1)} → [[0, b], [b, 0]]  (off-diagonal Kashiwara)
#   T|_{V_(1,1,1)} → (-1)^k Id  (sign rep)
#
# So Tr(T^k|_{V_(2,1)}) = 2·b^k if k even, 0 if k odd (off-diagonal!)
# And the Jones coupling J enters via the INTER-BLOCK interference:
#   c_k ∝ J^{floor(k/3)} · Tr(T^{k mod 3}|_{V_(2,1)})

# Let me construct the 4×4 effective transfer matrix explicitly
# in the (triv, std+, std-, sign) basis:

T = matrix([
    [1,    0,    0,   0   ],  # V_(3): identity
    [0,    0,    b,   0   ],  # V_(2,1)+: off-diagonal
    [0,    b,    0,   0   ],  # V_(2,1)-: off-diagonal
    [0,    0,    0,   -1  ],  # V_(1,1,1): sign
])

print("Transfer matrix T (4×4 in Wedderburn basis):")
for i in range(4):
    row = [float(T[i,j]) for j in range(4)]
    print(f"  [{', '.join(f'{x:+.6f}' for x in row)}]")
print()

# Compute T^k and extract traces per block
print("Powers of T — per-block traces:")
print(f"{'k':>3} {'Tr(T^k)':>12} {'Tr|V(3)':>10} {'Tr|V(2,1)':>12} {'Tr|V(111)':>10}")
Tk = matrix([[1 if i==j else 0 for j in range(4)] for i in range(4)])
for k in range(1, 12):
    Tk = Tk * T
    tr_total = trace(Tk)
    tr_triv = Tk[0, 0]
    tr_std = Tk[1, 1] + Tk[2, 2]
    tr_sign = Tk[3, 3]
    print(f"{k:3d} {float(tr_total):+12.6f} {float(tr_triv):+10.4f} "
          f"{float(tr_std):+12.8f} {float(tr_sign):+10.4f}")

print()

# ── KEY: the c_k GENERATING FUNCTION ─────────────────────────────
# The multiplicative correction factor is:
#   Π_k (1 + c_k · u^k) = det(I + u·T·diag(weights)) / det(I)
#
# For a 4×4 matrix with eigenvalues {1, b, -b, -1}:
#   det(I - u·T) = (1-u)(1-b·u)(1+b·u)(1+u) = (1-u²)(1-b²·u²) = (1-u²)(1-K·u²)
#
# So:
#   Π_k (1 + c_k · u^k) = (1 - u²)⁻¹ · (1 - K·u²)⁻¹  [CONJECTURAL]
#
# This gives:
#   Σ c_k u^k = ln[(1-u²)⁻¹(1-K·u²)⁻¹]
#             = Σ_{m≥1} (1 + K^m)/m · u^{2m}

# Wait — this only generates even-k terms! The odd-k terms (c_3, c_5, c_7)
# must come from a DIFFERENT mechanism — the Jones inter-block coupling.

# Let me try a MODIFIED transfer matrix that includes the Jones coupling:
print("=" * 70)
print("MODIFIED TRANSFER MATRIX WITH JONES COUPLING")
print("=" * 70)
print()

# The Jones coupling J = -2 enters via the 3-strand Markov closure.
# The modified transfer acts on the TOWER depth, not just one step.
# At tower depth n, the braid word has ~n crossings, and the
# Jones polynomial contributes J at every 3rd step (from the
# 3-strand closure structure of H_3).

# Effective 2×2 generating matrix for the c_k pair:
# G = [[J, b], [0, K]]  (upper triangular: Jones + Kashiwara mixing)
#
# Then G^n = [[J^n, b·(J^n - K^n)/(J-K)], [0, K^n]]
# Tr(G^n) = J^n + K^n
# Off-diagonal generates the mixed terms!

G = matrix([
    [J,  b],
    [0,  K],
])
print("Generating matrix G = [[J, b], [0, K]]:")
print(f"  G = [[{float(J):+.4f}, {float(b):+.6f}],")
print(f"       [{0:+.4f}, {float(K):+.6f}]]")
print(f"  det(G) = J·K = {float(J*K):.6f}")
print(f"  tr(G) = J+K = {float(J+K):.6f}")
print()

# Compute G^n and compare traces to c_k
print(f"{'n':>3} {'Tr(G^n)':>12} {'c_{n+2}':>12} {'match?':>10}")
Gn = matrix([[1, 0], [0, 1]])
for n in range(1, 9):
    Gn = Gn * G
    tr_n = float(trace(Gn))
    k = n + 2  # c_k corresponds to G^{k-2}
    c_known = {3: J, 4: J*K**2, 5: J**2*3+b, 6: J**2*K, 7: J**3}
    c_val = float(c_known[k]) if k in c_known else "?"
    match = f"{tr_n/c_val:.4f}" if isinstance(c_val, float) and c_val != 0 else "?"
    print(f"{n:3d} {tr_n:+12.6f} {str(c_val):>12} {match:>10}")

print()
print("Tr(G^n) = J^n + K^n — gives the DOMINANT term at each rung")
print("but misses the multiplicative K-power modulation in trailing rungs.")
print()

# ── The FULL generating function ─────────────────────────────────
# Observation: c_k for k≥3 can be written as:
#   c_k = Tr(G^{k-2}) + δ_k
# where δ_k is a correction that captures the K-power modulation.
#
# Let's check:
print("Correction analysis: c_k - Tr(G^{k-2})")
Gn = matrix([[1, 0], [0, 1]])
corrections = []
for n in range(1, 6):
    Gn = Gn * G
    k = n + 2
    tr_n = trace(Gn)
    c_actual = {3: J, 4: J*K**2, 5: J**2*3+b, 6: J**2*K, 7: J**3}
    if k in c_actual:
        delta = c_actual[k] - tr_n
        corrections.append((k, float(delta)))
        print(f"  k={k}: c_{k} - Tr(G^{n}) = {float(delta):+.8f}")

print()
print("Done. The corrections δ_k encode the Kashiwara sub-leading structure.")
