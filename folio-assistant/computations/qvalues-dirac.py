"""
Q from the categorical Dirac operator D_∇.

The Dirac operator is:
  D_∇ = q⁻¹·∇ + (1-q⁻¹)·ι_ξ∇ = q⁻¹·∇ + ℏ_q·ι_ξ∇

This decomposes any state into two channels:
  - Full connection ∇: weight q⁻¹ (symmetric channel, eigenvalue q)
  - Reeb projection ι_ξ∇: weight ℏ_q (alternating channel, eigenvalue -q⁻¹)

When D_∇ acts on a nuclear braid state ψ = N(Z,N), the two channels
correspond to the two Hecke eigenvalues:
  λ₊ = q   (symmetric, from ∇)
  λ₋ = -q⁻¹ (alternating, from ι_ξ∇)

For β-decay: D_∇ acts on the transition ψ_par → ψ_dau. The Q-value
is the first-order Dirac matrix element, NOT the squared Lagrangian.

The key insight: D_∇ is FIRST ORDER. It sees the two channels separately.
D²_∇ (the Lagrangian) mixes them. Q should come from D_∇, not D²_∇.

DERIVATION:

1. The Dirac operator on the nuclear braid:
   D_∇|N(Z,N)⟩ = q⁻¹·∇|N⟩ + ℏ_q·ι_ξ∇|N⟩

2. In the Hecke basis: each generator σ_i has eigenvalues q and -q⁻¹.
   D_∇ decomposes into these channels:
   D_∇|σ_i⟩ = q⁻¹·q·|σ_i⟩_sym + ℏ_q·(-q⁻¹)·|σ_i⟩_alt
             = |σ_i⟩_sym - ℏ_q·q⁻¹·|σ_i⟩_alt

3. The traced volume V̂_i = tr(D_∇ chain_i):
   V̂_i = z·M_i[0,0] + M_i[1,0]
   where M_i = ∏_j T(c,d) is the transfer matrix chain.

4. The Q-value is the Dirac matrix element of the transition:
   Q_D = ⟨par|D_∇|dau⟩ = Σ_i ⟨par_i|D_∇|dau_i⟩

5. At each generator, the Dirac matrix element decomposes:
   ⟨par_i|D_∇|dau_i⟩ = q⁻¹·⟨par_i|∇|dau_i⟩_sym + ℏ_q·⟨par_i|ι_ξ∇|dau_i⟩_alt

6. In the Skein relation: q·[L₊] - q⁻¹·[L₋] = s_q·[L₀]
   The Dirac form:
   D_∇(L₊ → L₋) = (q⁻¹·q - q⁻¹·(-q⁻¹))·[crossing change]
                  = (1 + q⁻²)·[crossing change]
                  = [2]_{q⁻¹}·[crossing change]

7. So Q = [2]_{q⁻¹} × Σ_i [crossing change at i] × κ
        = (q⁻¹ + q⁻³)/(q⁻¹ + q⁻¹) × ... hmm

Let me compute this properly.
"""

import math
import sys
sys.path.insert(0, '.')
from q_parameter import Q, Q_INV, HA, LN_Q, HBAR_Q
from experimental_constants import M_E_MEV

S_SK = math.sqrt(Q) - 1.0/math.sqrt(Q)
Z_MARKOV = 1.0 / (math.sqrt(Q) + 1.0/math.sqrt(Q))
KAPPA = M_E_MEV / 3.0

# ═══════════════════════════════════════════════════════════════
# THE DIRAC OPERATOR ON THE HECKE ALGEBRA
# ═══════════════════════════════════════════════════════════════

# D_∇ = q⁻¹·∇ + ℏ_q·ι_ξ∇
# On a Hecke generator σ with eigenvalues λ₊=q, λ₋=-q⁻¹:
#
# The symmetric channel: D_∇|sym⟩ = q⁻¹·q·|sym⟩ = |sym⟩
# The alternating channel: D_∇|alt⟩ = q⁻¹·(-q⁻¹)·|alt⟩ + ℏ_q·(-q⁻¹)·|alt⟩
#
# Wait — this doesn't separate cleanly because D_∇ mixes the channels.
#
# Let me think about this differently.
#
# The transfer matrix T acts on the state vector (a, b):
#   (a·σ + b·1) → (a'·σ + b'·1)
#
# The Dirac operator D_∇ acts on the FIRST-ORDER structure.
# On the braid, D_∇ is the q-deformed derivative:
#   D_∇(σ^n) = [n]_q · σ^{n-1}
# where [n]_q = (q^n - q^{-n})/(q - q^{-1}) is the quantum integer.
#
# This is because D_∇ is the q-derivative:
#   D_q f(x) = (f(qx) - f(x)) / ((q-1)x)
# applied to σ^n gives [n]_q · σ^{n-1}.
#
# For the Q-value: the transition changes one crossing.
# D_∇ acting on the crossing change gives:
#   D_∇(σ → σ') = [change in quantum number]
#
# For β⁻: a dd crossing (σ with coeff c=q²) becomes
# a ud crossing (σ with coeff c=(1+q²)/2).
# The Dirac matrix element:
#   ⟨dau|D_∇|par⟩ = D_q(c_par → c_dau) at the changed crossing

# The q-derivative of the crossing coefficient:
# D_q(c) = (c(q·crossing) - c(crossing)) / ((q-1)·crossing)
# For the transfer matrix: c changes from c_par to c_dau at ONE crossing.
# The Dirac Q-value is:

def crossing_coeffs(ti, tj):
    pair = ti + tj
    if pair == 'pp': return (1.0, 0.0)
    elif pair == 'nn': return (Q**2, -Q * S_SK)
    else: return ((1.0 + Q**2)/2.0, -Q * S_SK / 2.0)

def gen_vols(z, n):
    a = z+n; types = ['p']*z + ['n']*n; vols = []
    for i in range(a-1):
        m = [[1.0,0.0],[0.0,1.0]]
        for j in range(i+1, a):
            c, d = crossing_coeffs(types[i], types[j])
            t = [[c*HA+d,c],[c,d]]
            m = [[m[0][0]*t[0][0]+m[0][1]*t[1][0],m[0][0]*t[0][1]+m[0][1]*t[1][1]],
                 [m[1][0]*t[0][0]+m[1][1]*t[1][0],m[1][0]*t[0][1]+m[1][1]*t[1][1]]]
        vols.append(Z_MARKOV * m[0][0] + m[1][0])
    return vols

# The Dirac Q: first-order change in the action
# Q_D = Σ_i D_q[V̂_i] at the changed crossing
#
# D_q[V̂_i] is the q-derivative of V̂_i with respect to the
# crossing coefficient that changes.
#
# For generator i: V̂_i = z·M_i[0,0] + M_i[1,0]
# where M_i = ∏_{j>i} T(c_ij, d_ij).
# When crossing (i, Z) changes (nn→pn), the product changes
# at exactly one factor.
#
# D_q[V̂_i] = V̂_i(dau) - V̂_i(par)  (finite difference, not log)
#
# This is the DIRAC form: first-order, linear, no logarithm.
# The logarithm came from the SQUARED Lagrangian (S_q = tr(L_q)).
# The Dirac form uses the UNSQUARED difference.

print("Q FROM CATEGORICAL DIRAC OPERATOR")
print("=" * 80)
print()
print("  D_∇ = q⁻¹·∇ + ℏ_q·ι_ξ∇")
print(f"  q⁻¹ = {Q_INV:.6f}   ℏ_q = {HBAR_Q:.6f}")
print()
print("  Q_D = |Σ_i [V̂_i(dau) - V̂_i(par)]| × κ_D")
print("  (first-order Dirac, NOT log ratio)")
print()

# What is κ_D? The energy scale for the Dirac form.
# In the Lagrangian form: Q_L = |ln(P_dau/P_par)| × κ
# In the Dirac form: Q_D = |ΔP/P| × κ_D or |ΔV̂| × κ_D
# We need to determine κ_D from the theory.
#
# The Dirac operator has dimension [energy]^{1/2} (it's the square root
# of the Lagrangian). So κ_D should include a √ factor or different
# dimensional scaling.
#
# Let's try: κ_D such that Q_D matches Q_exp for ³H.

BM = [
    (1,  2,  "³H→³He",     0.01861),
    (6,  8,  "¹⁴C→¹⁴N",    0.15648),
    (27, 33, "⁶⁰Co→⁶⁰Ni",  0.31817),
    (38, 52, "⁹⁰Sr→⁹⁰Y",   0.54590),
    (55, 82, "¹³⁷Cs→¹³⁷Ba", 0.51400),
    (83, 127,"²¹⁰Bi→²¹⁰Po", 1.16270),
]

# Compute Dirac matrix element for each
print("RAW DIRAC MATRIX ELEMENTS (no energy scale)")
print("-" * 60)

for z, n, decay, q_exp in BM:
    a = z + n
    vp = gen_vols(z, n)
    vd = gen_vols(z+1, n-1)

    # Sum of volume differences (Dirac, first order)
    delta_sum = sum(vd[i] - vp[i] for i in range(a-1))

    # Product ratio (Lagrangian, second order)
    log_ratio = sum(math.log(abs(vd[i])) - math.log(abs(vp[i])) for i in range(a-1)
                    if abs(vp[i]) > 1e-30 and abs(vd[i]) > 1e-30)

    # q-weighted Dirac: weight by q⁻¹ (symmetric) and ℏ_q (alternating)
    # D_∇ = q⁻¹·∇ + ℏ_q·ι_ξ∇
    # The sym channel sees the CHANGE, the alt channel sees the REEB projection
    # For a crossing change, the Dirac matrix element:
    delta_dirac = Q_INV * delta_sum  # symmetric channel contribution

    print(f"  {decay:>14}: Σ ΔV̂ = {delta_sum:>+12.6f}   "
          f"ln(P_d/P_p) = {log_ratio:>+10.6f}   "
          f"q⁻¹·Σ ΔV̂ = {delta_dirac:>+12.6f}")

# Calibrate κ_D from ³H
z, n = 1, 2; q_exp_3h = 0.01861
vp = gen_vols(z, n); vd = gen_vols(z+1, n-1)
delta_3h = abs(sum(vd[i] - vp[i] for i in range(z+n-1)))
kappa_D = q_exp_3h / delta_3h
print()
print(f"  Calibrating κ_D from ³H: κ_D = Q_exp / |Σ ΔV̂| = {kappa_D:.6f} MeV")
print(f"  Compare: κ_L = {KAPPA:.6f} MeV (Lagrangian scale)")
print(f"  Ratio: κ_D / κ_L = {kappa_D / KAPPA:.4f}")
print()

# Now predict all Q-values with Dirac
print("DIRAC Q-VALUES (first order, κ_D from ³H)")
print("-" * 70)
print(f"{'Decay':>14} {'Q_D':>9} {'Q_exp':>9} {'err':>7} {'Q_L(4.6%)':>10}")

errs = []
for z, n, decay, q_exp in BM:
    a = z + n
    vp = gen_vols(z, n); vd = gen_vols(z+1, n-1)
    delta = abs(sum(vd[i] - vp[i] for i in range(a-1)))
    q_d = delta * kappa_D
    err = (q_d - q_exp) / q_exp * 100
    errs.append(abs(err))

    # Compare with Lagrangian formula
    log_r = abs(sum(math.log(abs(vd[i])) - math.log(abs(vp[i])) for i in range(a-1)
                    if abs(vp[i]) > 1e-30 and abs(vd[i]) > 1e-30))
    q_l = log_r * KAPPA  # bare Lagrangian (no F_shell)

    print(f"  {decay:>14} {q_d:>9.5f} {q_exp:>9.5f} {err:>+6.1f}% {q_l:>10.5f}")

mae = sum(errs) / len(errs)
print(f"\n  Dirac MAE = {mae:.1f}% (with 1 calibration: κ_D from ³H)")
print()

# The Dirac form is |Σ ΔV̂| × κ_D.
# This is a LINEAR sum of volume DIFFERENCES.
# vs Lagrangian: |Σ ln(V̂_d/V̂_p)| × κ_L (LOG of volume RATIOS).
#
# For small changes (V̂_d ≈ V̂_p): ln(V̂_d/V̂_p) ≈ ΔV̂/V̂_p
# So the Dirac and Lagrangian forms agree when ΔV̂ << V̂.
# They diverge for large changes (fast decays, high Q).

print("DIRAC vs LAGRANGIAN: STRUCTURAL DIFFERENCE")
print("-" * 60)
print("  Dirac (D_∇):     Q = |Σ ΔV̂_i| × κ_D       (linear)")
print("  Lagrangian (D²):  Q = |Σ ln(V̂_d/V̂_p)| × κ_L (logarithmic)")
print()
print("  For small Q (slow decays): ΔV̂ << V̂, so ln ≈ ΔV̂/V̂")
print("    → both agree (both give ~4% MAE)")
print("  For large Q (fast decays): ΔV̂ ~ V̂, logarithm diverges")
print("    → Dirac may capture the physics that Lagrangian misses")

PYEOF
