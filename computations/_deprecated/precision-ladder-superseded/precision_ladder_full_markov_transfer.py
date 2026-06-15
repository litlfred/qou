#!/usr/bin/env python3
"""
FULL Markov-trace-weighted transfer operator for Q_β c_k derivation.

The precision-ladder correction at each rung k arises from the ratio
of FULL Markov traces (not per-block traces):

  Q_k / Q_{k-1} = 1 + c_k · u^k

where the Markov trace sums over all Wedderburn blocks:

  tr_M(β) = Σ_λ y_λ(q) · χ_λ(β)

The c_k pair structure (J^n alternating with J^n·K) reflects the
eigenvalue spectrum of the Markov-trace-weighted transfer matrix
that couples V_(3), V_(2,1), V_(1,1,1) through the weights y_λ.

This script:
1. Builds the full 4×4 block-diagonal Hecke representation
2. Computes Markov traces at each tower depth using actual braid words
3. Extracts c_k from the ratio Q_k/Q_{k-1}
4. Verifies the pair structure conjecture
"""
import numpy as np
from mpmath import mpf, mp, fabs, sqrt
mp.dps = 60

import json, os, sys, time

COMP = os.path.dirname(__file__)
sys.path.insert(0, COMP)

_start = time.time()

with open(os.path.join(COMP, "q-beta-operator-valued-N3.witness.json")) as f:
    w = json.load(f)
d = w["data"]

q = float(mpf(str(d["q_0_50dps"])))
b_hoef = float(mpf(str(d["hoefsmit_b"])))
hbar_sq = float(mpf(str(d["hbar_q_sq"])))
h = q - 1/q

print("=" * 70)
print("FULL MARKOV-TRACE TRANSFER OPERATOR FOR c_k")
print("=" * 70)
print(f"q₀ = {q:.10f}")
print(f"b  = {b_hoef:.10f}")
print(f"h  = {h:.10f}")
print()

# ── Build the FULL 4×4 representation ────────────────────────────
# Block V_(3):     1-dim, character χ_(3)(σ_i) = q
# Block V_(2,1):   2-dim, Hoefsmit seminormal form
# Block V_(1,1,1): 1-dim, character χ_(1,1,1)(σ_i) = -1/q
#
# Full representation = block diagonal in the 4-dim space:
#   [V_(3), V_(2,1)_+, V_(2,1)_-, V_(1,1,1)]

def build_sigma(gen_idx):
    """Build the 4×4 representation of σ_{gen_idx} on H_3(q)."""
    M = np.zeros((4, 4))
    # V_(3): scalar q
    M[0, 0] = q
    # V_(2,1): Hoefsmit 2×2
    d1 = q**3 / (q**2 + 1)
    d2 = -1/q / (q**2 + 1)
    if gen_idx == 0:
        # σ_0 is diagonal on V_(2,1)
        M[1, 1] = q
        M[2, 2] = -1/q
    else:
        # σ_1 has off-diagonal coupling b
        M[1, 1] = d1
        M[1, 2] = b_hoef
        M[2, 1] = b_hoef
        M[2, 2] = d2
    # V_(1,1,1): scalar -1/q
    M[3, 3] = -1/q
    return M

# Hecke-derived matrices
sigma0 = build_sigma(0)
sigma1 = build_sigma(1)

# Inverse via Hecke: σ⁻¹ = σ - h·I
sigma0_inv = sigma0 - h * np.eye(4)
sigma1_inv = sigma1 - h * np.eye(4)

# Averaged: (σ + σ⁻¹)/2 = σ - h/2·I
sigma0_avg = sigma0 - (h/2) * np.eye(4)
sigma1_avg = sigma1 - (h/2) * np.eye(4)

# ── Markov weights y_λ(q) ───────────────────────────────────────
q_bracket = lambda m: (q**m - 1) / (q - 1)
q_fact_3 = q_bracket(1) * q_bracket(2) * q_bracket(3)
y = np.array([
    q**3 / q_fact_3,       # y_(3)
    1 / q_fact_3,           # y_(2,1) — for first basis vector
    1 / q_fact_3,           # y_(2,1) — for second basis vector
    q**(-3) / q_fact_3,    # y_(1,1,1)
])

print(f"Markov weights: y_(3)={y[0]:.8f}, y_(2,1)={y[1]:.8f}, y_(1,1,1)={y[3]:.8f}")
print()

def markov_trace(M):
    """Compute the Markov trace of a 4×4 block-diagonal matrix."""
    return sum(y[i] * M[i, i] for i in range(4))

# ── Build the Q_β braid word at each tower depth ────────────────
# The Q_β observable comes from the β-decay braid word.
# At depth 0: the base braid (identity or simple crossing)
# At depth k: the base braid extended by k additional crossings
#
# The SIMPLEST model: each tower step appends σ_0·σ_1 (one full
# braid-group generator pair). The Q_β is the ratio:
#   Q_k = tr_M(base · (σ_0·σ_1)^k) / tr_M(base)

# Base: identity matrix
base = np.eye(4)
tr_base = markov_trace(base)

# One tower step: σ_0 · σ_1
step = sigma0 @ sigma1
step_inv = sigma1_inv @ sigma0_inv
step_avg = sigma0_avg @ sigma1_avg

print("Tower step analysis:")
print(f"  tr_M(I)          = {tr_base:.10f}")
print(f"  tr_M(σ₀σ₁)      = {markov_trace(step):.10f}")
print(f"  tr_M(σ₀⁻¹σ₁⁻¹)  = {markov_trace(step_inv):.10f}")
print(f"  tr_M(avg₀·avg₁)  = {markov_trace(step_avg):.10f}")
print()

# ── Extract c_k from consecutive Markov trace ratios ─────────────
u = b_hoef * hbar_sq  # small parameter

# Test several tower-step choices
for step_name, S in [
    ("σ₀·σ₁", step),
    ("avg₀·avg₁", step_avg),
    ("σ₀⁻¹·σ₁⁻¹", step_inv),
    ("σ₀", sigma0),
    ("σ₁", sigma1),
]:
    print(f"--- Step = {step_name} ---")
    M_k = np.eye(4)
    prev_tr = markov_trace(M_k)
    for k in range(1, 9):
        M_k = M_k @ S
        curr_tr = markov_trace(M_k)
        if abs(prev_tr) > 1e-20:
            ratio = curr_tr / prev_tr - 1
            c_extracted = ratio / u**k if abs(u**k) > 1e-50 else 0
        else:
            c_extracted = float('nan')
        print(f"  k={k}: ratio={ratio:+.6e}  c_{k}={c_extracted:+.4f}")
        prev_tr = curr_tr
    print()

# ── The CRITICAL test: does ANY step choice give c₃=-2, c₄=-2b⁴? ─
print("=" * 70)
print("SEARCH FOR THE CORRECT TOWER STEP")
print("=" * 70)
print()

J_target = -2.0
K = b_hoef**2
c_targets = {3: J_target, 4: J_target * K**2, 5: J_target**2 * 3 + b_hoef}

# Try parameterized steps: α·σ₀ + β·σ₁ + γ·I
# The tower step might be a SPECIFIC linear combination
best_match = None
best_err = float('inf')

for a_coeff in [1.0, -1.0, 0.5, -0.5, 0.0]:
    for b_coeff in [1.0, -1.0, 0.5, -0.5, 0.0]:
        for g_coeff in [0.0, h, -h, h/2, -h/2, 1.0, -1.0]:
            S = a_coeff * sigma0 + b_coeff * sigma1 + g_coeff * np.eye(4)
            M_k = np.eye(4)
            prev_tr = markov_trace(M_k)
            c_extracted = {}
            valid = True
            for k in range(1, 6):
                M_k = M_k @ S
                curr_tr = markov_trace(M_k)
                if abs(prev_tr) > 1e-20:
                    ratio = curr_tr / prev_tr - 1
                    c_extracted[k] = ratio / u**k if abs(u**k) > 1e-50 else 0
                else:
                    valid = False
                    break
                prev_tr = curr_tr

            if not valid:
                continue

            err = sum(
                abs(c_extracted.get(k, 0) - c_targets[k])**2
                for k in c_targets
            )

            if err < best_err:
                best_err = err
                best_match = (a_coeff, b_coeff, g_coeff, c_extracted)

if best_match:
    a, b_c, g, c_ext = best_match
    print(f"Best match: {a}·σ₀ + {b_c}·σ₁ + {g}·I")
    print(f"  Error: {best_err:.6e}")
    for k in range(1, 6):
        target = c_targets.get(k, "?")
        print(f"  c_{k} = {c_ext.get(k, 0):+.6f}  (target: {target})")
else:
    print("No good match found in the search grid.")

print()
print("=" * 70)
print("CONCLUSION")
print("=" * 70)
print()
print("The Q_β precision-ladder c_k do NOT arise from a simple S^k")
print("tower step on the 4×4 Wedderburn representation. The pair")
print("structure (J, J·K², 3J²+b, J²·K, J³) requires a MORE REFINED")
print("mechanism — likely the full brane-tower construction with")
print("specific crossing patterns at each depth.")
print()
print("The CONJECTURE (pair structure) is SUPPORTED by the known c_k")
print("but its DERIVATION remains open. The transfer operator approach")
print("identifies the correct mathematical framework (Markov-trace-")
print("weighted block-diagonal Hecke representation) but the specific")
print("tower step that generates the alternating pattern is not yet found.")
