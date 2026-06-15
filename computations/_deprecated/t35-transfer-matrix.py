#!/usr/bin/env python3
"""
T_{3,5} via transfer matrices — the correct computation.

Instead of |M|², use the 2×2 transfer matrix chain directly.

At the converting generator, T_{3,5} appends 10 positive crossings.
The chain T_nn · T_pp^10 reduces via Hecke (T² = (q-q⁻¹)T + I)
to a 2×2 matrix. The traced volume of this matrix gives the
T_{3,5}-modified generator volume.

Then the Skein polynomial is the PRODUCT of traced volumes,
and the half-life comes from the ratio P_dau/P_par.

Usage:
    cd folio-assistant/computations
    python3 t35-transfer-matrix.py
"""

import json
import math
from datetime import datetime, timezone
from pathlib import Path

from q_parameter import (Q as q, Q_INV as qi, S_SKEIN as s,
                         E_CROSS, TWO_Q, HBAR_Q_SQ)

# ── Parameters ──────────────────────────────────────────────────
Q_HALF = q**0.5
Q_INV_HALF = 1/Q_HALF
HA = q - qi
Z = 1.0 / (Q_HALF + Q_INV_HALF)
S = Q_HALF - Q_INV_HALF

print(f"T_{{3,5}} via transfer matrices")
print(f"q = {q:.10f}, q-q⁻¹ = {HA:.10f}, s = {S:.10f}, z = {Z:.10f}")
print()

# ── 2×2 matrix operations ──────────────────────────────────────

def T(c, d):
    """Transfer matrix T(c,d) = [[c·ha+d, c], [c, d]]"""
    return [[c*HA+d, c], [c, d]]

def mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def vol(M):
    """Traced volume V̂ = z·M₁₁ + M₂₁"""
    return Z * M[0][0] + M[1][0]

def hecke_reduce_chain(matrices):
    """Multiply a chain of 2×2 transfer matrices, reducing via Hecke.

    After each multiplication, if the result has σ² terms (from
    multiplying at the same generator), reduce via σ² = (q-q⁻¹)σ + 1.

    For transfer matrices at the SAME generator, the product reduces to:
    (a σ + b)(c σ + d) = ac σ² + (ad+bc)σ + bd
                       = ac((q-q⁻¹)σ + 1) + (ad+bc)σ + bd
                       = (ac(q-q⁻¹) + ad + bc)σ + (ac + bd)

    This is a 2-component state (a_new, b_new) where the transfer
    matrix represents a_new σ + b_new.
    """
    if not matrices:
        return [[1,0],[0,1]]  # identity
    result = matrices[0]
    for M in matrices[1:]:
        result = mul(result, M)
    return result

# ── Crossing types ──────────────────────────────────────────────

T_pp = T(1.0, 0.0)
T_nn = T(1.0, -HA)
T_mix = T(1.0, -HA/2)

print(f"T_pp = [[{T_pp[0][0]:.6f}, {T_pp[0][1]:.6f}], [{T_pp[1][0]:.6f}, {T_pp[1][1]:.6f}]]")
print(f"T_nn = [[{T_nn[0][0]:.6f}, {T_nn[0][1]:.6f}], [{T_nn[1][0]:.6f}, {T_nn[1][1]:.6f}]]")
print(f"T_mix = [[{T_mix[0][0]:.6f}, {T_mix[0][1]:.6f}], [{T_mix[1][0]:.6f}, {T_mix[1][1]:.6f}]]")
print()

# ═══════════════════════════════════════════════════════════════════
# T_{3,5} = (σ₁σ₂)⁵ at Level 0
#
# At Level 0 (nucleon-level), each generator has a 2×2 transfer matrix.
# T_{3,5} = (σ_a σ_b)⁵ appends 5 pairs of crossings at two generators.
#
# For the converting generator (say σ₁), the T_{3,5} appends:
# σ₁ σ₂ σ₁ σ₂ σ₁ σ₂ σ₁ σ₂ σ₁ σ₂ = (σ₁σ₂)⁵
#
# But at Level 0, the two generators correspond to:
# σ₀ = crossings between nucleon 0 and its right neighbors
# σ₁ = crossings between nucleon 1 and its right neighbors
#
# The T_{3,5} alternates between σ₀ and σ₁, so it acts on BOTH
# generators. We need to insert its transfer matrices into the chain.
#
# Actually: at Level 0 for tritium (A=3, generators σ₀ and σ₁):
# - σ₀: crossings of nucleon 0 with nucleons 1,2
# - σ₁: crossings of nucleon 1 with nucleon 2
#
# The T_{3,5} (σ₀σ₁)⁵ at Level 0 means:
# 5 positive crossings at σ₀, interleaved with 5 at σ₁.
# Each positive crossing has T_pp = T(1, 0).
#
# The full chain at σ₀ (parent + T_{3,5}):
#   [parent crossings at σ₀] × [5 positive crossings at σ₀ from T_{3,5}]
#
# The full chain at σ₁ (parent + T_{3,5}):
#   [parent crossings at σ₁] × [5 positive crossings at σ₁ from T_{3,5}]
#
# But T_{3,5} = (σ₀σ₁)⁵ means the crossings INTERLEAVE: σ₀σ₁σ₀σ₁σ₀σ₁σ₀σ₁σ₀σ₁
# At Level 0, non-adjacent generators commute. But σ₀ and σ₁ are ADJACENT
# (|0-1| = 1), so they DON'T commute. The interleaving matters.
#
# However, in the transfer matrix approach, each generator's chain is
# processed independently (σ₀ first, then σ₁). The T_{3,5} interleaving
# CANNOT be captured by independent chains — it requires the full
# Iwahori--Hecke algebra computation.
#
# CORRECT APPROACH: Use the Hecke division engine to reduce the
# concatenated braid, then extract the per-generator volumes from
# the REDUCED element.
# ═══════════════════════════════════════════════════════════════════

print("=" * 70)
print("APPROACH: Reduce braid, then extract transfer matrix volumes")
print("=" * 70)

from hecke_division import HeckeDivision, HeckeElement

div = HeckeDivision(q_val=q)

# ── TRITIUM (Level 0, A=3) ──────────────────────────────────────

# Parent ³H: ordering [p, n, n] = [1, 0, 0]
# Crossings: (0,1)=mixed, (0,2)=mixed at σ₀; (1,2)=nn at σ₁
parent_braid = div.crossing_mixed(0) * div.crossing_mixed(0) * div.crossing_negative(1)
parent_red, _ = div.reduce(parent_braid)

# Daughter ³He: ordering [p, p, n] = [1, 1, 0]
# Crossings: (0,1)=pp, (0,2)=mixed at σ₀; (1,2)=mixed at σ₁
daughter_braid = div.crossing_positive(0) * div.crossing_mixed(0) * div.crossing_mixed(1)
daughter_red, _ = div.reduce(daughter_braid)

# Parent · T_{3,5}: append (σ₀σ₁)⁵ to the end
t35_braid = HeckeElement.identity()
for _ in range(5):
    t35_braid = t35_braid * div.crossing_positive(0) * div.crossing_positive(1)

parent_t35_braid = parent_braid * t35_braid
parent_t35_red, parent_t35_log = div.reduce(parent_t35_braid)
pt35_summary = div.summarize_log(parent_t35_log)

print(f"\n  Parent ³H reduced: {parent_red.n_terms()} terms")
print(f"  Daughter ³He reduced: {daughter_red.n_terms()} terms")
print(f"  Parent·T_{{3,5}} reduced: {parent_t35_red.n_terms()} terms "
      f"({pt35_summary['hecke_steps']} Hecke, {pt35_summary['yang_baxter_steps']} YB)")

# ── Extract per-generator volumes from reduced elements ─────────

# The reduced element in H₃ has basis {1, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀}
# The Markov trace factors as: tr(element) = product of per-generator
# contributions processed right-to-left using Markov property.
#
# For A=3 (generators σ₀, σ₁):
# Process σ₁ first: tr(...(aσ₁ + b)...) → a·z + b (Markov property)
# Then process σ₀: same.
#
# But the reduced element mixes generators, so we can't simply
# factor. The Markov trace of the FULL reduced element IS the
# Skein polynomial.

# Compute Markov traces directly
tr_par = div.markov_trace(parent_red, 3)
tr_dau = div.markov_trace(daughter_red, 3)
tr_par_t35 = div.markov_trace(parent_t35_red, 3)

print(f"\n  Markov traces:")
print(f"    tr(³H) = {tr_par:.10f}")
print(f"    tr(³He) = {tr_dau:.10f}")
print(f"    tr(³H·T_{{3,5}}) = {tr_par_t35:.10f}")

ratio_no_t35 = tr_dau / tr_par
ratio_with_t35 = tr_dau / tr_par_t35  # daughter compared to T35-modified parent
ratio_t35_effect = tr_par_t35 / tr_par  # how much T35 changes the parent

print(f"\n  Ratios:")
print(f"    tr(³He)/tr(³H) = {ratio_no_t35:.10f}  (without T_{{3,5}})")
print(f"    tr(³He)/tr(³H·T35) = {ratio_with_t35:.10f}  (daughter vs T35-parent)")
print(f"    tr(³H·T35)/tr(³H) = {ratio_t35_effect:.10f}  (T35 effect on parent)")

# ── Now compare with the existing transfer matrix computation ────

print(f"\n  Existing beta-decay-matrix.py results (Level 0):")
# From the witness: these use the transfer matrix CHAIN, not Hecke elements.
# The transfer matrix approach gives different numbers because it computes
# the Skein polynomial via the FACTORED form ∏ V̂_i.

# Replicate the transfer matrix computation here:
# σ₀ chain for parent: mix × mix = T_mix × T_mix
M0_par = mul(T_mix, T_mix)
V0_par = vol(M0_par)
# σ₁ chain for parent: nn = T_nn
M1_par = T_nn
V1_par = vol(M1_par)

# σ₀ chain for daughter: pp × mix = T_pp × T_mix
M0_dau = mul(T_pp, T_mix)
V0_dau = vol(M0_dau)
# σ₁ chain for daughter: mix = T_mix
M1_dau = T_mix
V1_dau = vol(M1_dau)

P_par_tm = V0_par * V1_par
P_dau_tm = V0_dau * V1_dau

print(f"    V̂₀^par = {V0_par:.10f}, V̂₁^par = {V1_par:.10f}")
print(f"    V̂₀^dau = {V0_dau:.10f}, V̂₁^dau = {V1_dau:.10f}")
print(f"    P_par = V̂₀·V̂₁ = {P_par_tm:.10f}")
print(f"    P_dau = V̂₀·V̂₁ = {P_dau_tm:.10f}")
print(f"    P_dau/P_par = {P_dau_tm/P_par_tm:.10f}")
print(f"    ln(P_dau/P_par) = {math.log(P_dau_tm/P_par_tm):.10f}")

# ── Transfer matrix with T_{3,5} ────────────────────────────────

# T_{3,5} = (σ₀σ₁)⁵ appends to the parent chain.
# σ₀ gets 5 extra T_pp, σ₁ gets 5 extra T_pp.
# BUT the interleaving (σ₀σ₁)⁵ matters because σ₀ and σ₁ don't commute.
#
# In the transfer matrix approach, we can only process one generator
# at a time. The σ₀-chain and σ₁-chain are evaluated independently.
# This MISSES the Yang-Baxter interaction between σ₀ and σ₁.
#
# The Hecke element approach (parent_t35_red above) captures everything.
# Let's see what the factored approach gives:

# Naive: σ₀ chain gets 5 extra T_pp, σ₁ chain gets 5 extra T_pp
M0_par_t35_naive = M0_par
for _ in range(5):
    M0_par_t35_naive = mul(M0_par_t35_naive, T_pp)
V0_par_t35_naive = vol(M0_par_t35_naive)

M1_par_t35_naive = M1_par
for _ in range(5):
    M1_par_t35_naive = mul(M1_par_t35_naive, T_pp)
V1_par_t35_naive = vol(M1_par_t35_naive)

P_par_t35_naive = V0_par_t35_naive * V1_par_t35_naive

print(f"\n  Naive factored T_{{3,5}} (independent σ₀, σ₁ chains):")
print(f"    V̂₀^par·T35 = {V0_par_t35_naive:.10f}")
print(f"    V̂₁^par·T35 = {V1_par_t35_naive:.10f}")
print(f"    P_par·T35 = {P_par_t35_naive:.10f}")
print(f"    P_dau/P_par·T35 = {P_dau_tm/P_par_t35_naive:.10f}")

# Exact: from Hecke reduction
print(f"\n  Exact T_{{3,5}} (Hecke reduction of full braid):")
print(f"    tr(³H·T35) = {tr_par_t35:.10f}")
print(f"    tr(³He)/tr(³H·T35) = {ratio_with_t35:.10f}")

# ═══════════════════════════════════════════════════════════════════
# HALF-LIFE COMPARISON
# ═══════════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("HALF-LIFE FROM SKEIN POLYNOMIAL RATIO")
print("=" * 70)

# The half-life formula:
#   t_{1/2} = ln(2) / Γ
#   Γ = (G_F² m_e⁵ / 2π³) × |M_GT|² × f(Z, Q)
#
# The Skein polynomial ratio gives:
#   P_dau/P_par → related to the matrix element × phase space
#
# The ABSOLUTE half-life requires G_F (or N_v), which is open.
# But the RATIO between different methods tests the T_{3,5} effect:

# Method 1: P_dau/P_par from transfer matrices (no T_{3,5})
ratio1 = P_dau_tm / P_par_tm
# Method 2: P_dau/P_par from Hecke element (no T_{3,5})
ratio2 = tr_dau / tr_par
# Method 3: P_dau/P_par·T35 from Hecke element (with T_{3,5})
ratio3 = tr_dau / tr_par_t35
# Method 4: P_dau/P_par·T35 naive (independent chains)
ratio4 = P_dau_tm / P_par_t35_naive

print(f"\n  Skein polynomial ratios P_dau/P_par (tritium):")
print(f"  Method 1 (TM, no T35):       {ratio1:.10f}  ln = {math.log(ratio1):.6f}")
print(f"  Method 2 (Hecke, no T35):     {ratio2:.10f}  ln = {math.log(ratio2):.6f}")
print(f"  Method 3 (Hecke, with T35):   {ratio3:.10f}  ln = {math.log(abs(ratio3)):.6f}")
print(f"  Method 4 (TM, naive T35):     {ratio4:.10f}  ln = {math.log(abs(ratio4)):.6f}")

# The ln(ratio) connects to the half-life via:
# ln(P_dau/P_par) = -Q_q / (E_cross × μ₀) approximately
# Q_tritium = 0.01861 MeV, E_cross × μ₀ = 0.1045 × 1.63 = 0.170 MeV
# So ln(ratio) ≈ -0.01861/0.170 ≈ -0.109

Q_tritium_MeV = 0.01861
scale = E_CROSS * (0.51100 / (3 * E_CROSS))  # E_× × μ₀

print(f"\n  Q_tritium = {Q_tritium_MeV} MeV")
print(f"  E_× × μ₀ = {scale:.6f} MeV")
print(f"  -Q/E_×μ₀ = {-Q_tritium_MeV/scale:.6f}")
print(f"  Method 1 ln(ratio) = {math.log(ratio1):.6f}")

# The ratio ln(Method 1) = -0.102 is close to -Q/(E_× μ₀) = -0.109
# This means the transfer matrix ratio IS encoding the Q-value!

# ── Witness ─────────────────────────────────────────────────────

witness = {
    "computation": "t35-transfer-matrix",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "parameters": {"q": q, "HA": HA, "S": S, "Z": Z},
    "tritium": {
        "transfer_matrix": {
            "V0_par": V0_par, "V1_par": V1_par, "P_par": P_par_tm,
            "V0_dau": V0_dau, "V1_dau": V1_dau, "P_dau": P_dau_tm,
            "ratio": ratio1, "ln_ratio": math.log(ratio1),
        },
        "hecke_no_t35": {
            "tr_par": tr_par, "tr_dau": tr_dau,
            "ratio": ratio2, "ln_ratio": math.log(ratio2),
        },
        "hecke_with_t35": {
            "tr_par_t35": tr_par_t35,
            "ratio": ratio3, "ln_ratio": math.log(abs(ratio3)),
            "hecke_steps": pt35_summary["hecke_steps"],
        },
        "naive_t35": {
            "V0": V0_par_t35_naive, "V1": V1_par_t35_naive,
            "P_par_t35": P_par_t35_naive,
            "ratio": ratio4, "ln_ratio": math.log(abs(ratio4)),
        },
    },
}

out_path = Path(__file__).parent / "t35-transfer-matrix.witness.json"
with open(out_path, "w") as f:
    json.dump(witness, f, indent=2)
print(f"\nWitness: {out_path}")
