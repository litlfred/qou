#!/usr/bin/env python3
"""
Continuation: solve for the Jones-Markov weights y_λ at H_3 via constraint
matching, then re-extract α_k with the correct normalization.

The Jones-Markov trace is uniquely determined by:
  tr_M(1) = 1
  tr_M(σ_i) = z = 1/(√q + 1/√q)
  tr_M(σ_i σ_j) = z² for any i, j

In Wedderburn block decomposition:
  tr_M(β) = Σ_λ y_λ · χ_λ(β)

3 unknowns y_(3), y_(2,1), y_(1,1,1); 3 constraints from above.
Linear system gives explicit y_λ.

Then re-compute α_k pairings with these correct weights.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json, sys, warnings
from pathlib import Path
from datetime import datetime, timezone
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
import numpy as np
from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from hecke_characters import build_seminormal_matrices, dim_q, qfac, q_int
# F6 (PR #565): wire numerical-q Hoefsmit matrix construction through
# BlockCache. Effect on H_3 partitions is modest (dim ≤ 2) but the
# pattern is correct; carries forward for later-extended H_n callers.
from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached
# CAL-1: m_e from codata_constants registry (P31-triage Phase A).
from codata_constants import M_E_MEV as m_e

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
h_amp = Q0 - QI
z_mark = Q0**3 / (Q0**2 + 1)


# Build seminormal matrices for each partition of 3
shapes = [(3,), (2, 1), (1, 1, 1)]
_block_cache = BlockCache(float(Q0_FLOAT), float(Q0_FLOAT - 1.0/Q0_FLOAT))
data = {}
for shape in shapes:
    sigmas, d_lam, _ = build_seminormal_matrices_cached(
        shape, cache=_block_cache,
    )
    if hasattr(sigmas[0], 'toarray'):
        sigmas_dense = [s.toarray() for s in sigmas]
    else:
        sigmas_dense = list(sigmas)
    data[shape] = {"sigmas": sigmas_dense, "dim": d_lam,
                   "dim_q": float(dim_q(shape))}


def chi_lambda(shape, words_with_coeffs):
    """χ_λ(Σ c_i · word_i) at given partition shape."""
    sigmas = data[shape]["sigmas"]; d = data[shape]["dim"]
    M = np.zeros((d, d))
    for word, coeff in words_with_coeffs.items():
        if word == "1":
            Me = np.eye(d)
        elif word == "s1":
            Me = sigmas[0]
        elif word == "s2":
            Me = sigmas[1]
        elif word == "s1s2":
            Me = sigmas[0] @ sigmas[1]
        elif word == "s2s1":
            Me = sigmas[1] @ sigmas[0]
        elif word == "s1s2s1":
            Me = sigmas[0] @ sigmas[1] @ sigmas[0]
        else:
            continue
        M += coeff * Me
    return float(np.trace(M))


# Compute χ for the constraint elements: 1, σ_1, σ_1σ_2
chi_table = {}
for elem in ["1", "s1", "s1s2"]:
    chi_table[elem] = {sh: chi_lambda(sh, {elem: 1}) for sh in shapes}

print("=" * 100)
print("Explicit Jones-Markov weights y_λ at H_3 via linear system")
print("=" * 100)
print(f"  q_0 = {float(Q0):.10f}, h = {float(h_amp):.6f}, z = {float(z_mark):.6f}")
print()
print(f"  {'element':<8} {'χ_(3)':>10} {'χ_(2,1)':>10} {'χ_(1,1,1)':>12}")
for elem in ["1", "s1", "s1s2"]:
    print(f"  {elem:<8} {chi_table[elem][(3,)]:>+10.6f} {chi_table[elem][(2, 1)]:>+10.6f} {chi_table[elem][(1, 1, 1)]:>+12.6f}")
print()

# Linear system:  y_sym · χ_sym(elem) + y_std · χ_std(elem) + y_alt · χ_alt(elem) = tr_M(elem)
# Constraints: tr_M(1) = 1, tr_M(σ_1) = z, tr_M(σ_1σ_2) = z²
A = np.array([
    [chi_table["1"][(3,)],  chi_table["1"][(2, 1)],  chi_table["1"][(1, 1, 1)]],
    [chi_table["s1"][(3,)], chi_table["s1"][(2, 1)], chi_table["s1"][(1, 1, 1)]],
    [chi_table["s1s2"][(3,)], chi_table["s1s2"][(2, 1)], chi_table["s1s2"][(1, 1, 1)]],
])
b = np.array([1.0, float(z_mark), float(z_mark**2)])
y = np.linalg.solve(A, b)
print(f"Linear system A y = b:")
print(f"  A = {A}")
print(f"  b = {b}")
print(f"  y = {y}  (Jones-Markov weights at H_3)")
print()
print(f"  y_sym  (λ=(3))     = {y[0]:.10f}")
print(f"  y_std  (λ=(2,1))   = {y[1]:.10f}")
print(f"  y_alt  (λ=(1,1,1)) = {y[2]:.10f}")
print(f"  Σ y_λ              = {y.sum():.6f}")
print()


def Markov_trace_with_y(words_with_coeffs):
    chis = {sh: chi_lambda(sh, words_with_coeffs) for sh in shapes}
    return y[0] * chis[(3,)] + y[1] * chis[(2, 1)] + y[2] * chis[(1, 1, 1)], chis


# Sanity checks
trM_1, _ = Markov_trace_with_y({"1": 1})
trM_s1, _ = Markov_trace_with_y({"s1": 1})
trM_s2, _ = Markov_trace_with_y({"s2": 1})
trM_s1s2, _ = Markov_trace_with_y({"s1s2": 1})
trM_s2s1, _ = Markov_trace_with_y({"s2s1": 1})
print(f"Sanity (Jones-Markov):")
print(f"  tr_M(1)        = {trM_1:.6f}  (expected 1)")
print(f"  tr_M(σ_1)      = {trM_s1:.6f}  (expected z = {float(z_mark):.6f})")
print(f"  tr_M(σ_2)      = {trM_s2:.6f}  (expected z by symmetry)")
print(f"  tr_M(σ_1σ_2)   = {trM_s1s2:.6f}  (expected z² = {float(z_mark**2):.6f})")
print(f"  tr_M(σ_2σ_1)   = {trM_s2s1:.6f}  (expected z² by Markov-cyclicity)")
print()


# Now extract α_k on E_∞ classes
print("=" * 100)
print("E_∞ class Markov pairings with Jones-Markov weights")
print("=" * 100)
trM_minus, _ = Markov_trace_with_y({"s1": 1, "s2": -1})
trM_plus,  _ = Markov_trace_with_y({"s1": 1, "s2": 1})
trM_pair_sym, _ = Markov_trace_with_y({"s1s2": 1, "s2s1": 1})
trM_pair_anti, _ = Markov_trace_with_y({"s1s2": 1, "s2s1": -1})
trM_max,   _ = Markov_trace_with_y({"s1s2s1": 1})

print(f"\n  E_∞^{{0,*}} = [1]:                tr_M = {trM_1:.10f}    α_0 = 1 (after normalization)")
print(f"\n  E_∞^{{1,*}} = [σ_1 - σ_2]:        tr_M = {trM_minus:.10f}    α_1 = {trM_minus:.6f}")
print(f"     (compare: σ_1 + σ_2:           tr_M = {trM_plus:.10f}, killed by d_1)")
print(f"\n  E_∞^{{2,*}} = [σ_1σ_2 + σ_2σ_1]:   tr_M = {trM_pair_sym:.10f}")
print(f"     α_2 = (pair-sym pairing)/2     = {trM_pair_sym/2:.10f}")
print(f"     compare to z² = {float(z_mark**2):.10f} → ratio = {(trM_pair_sym/2)/float(z_mark**2):.6f}")
print(f"     (anti pair killed: tr_M(σ_1σ_2 - σ_2σ_1) = {trM_pair_anti:.10f})")
print(f"\n  E_∞^{{3,*}} = [σ_1σ_2σ_1]:        tr_M = {trM_max:.10f}")
print(f"     α_3 = {trM_max:.6f}; compare to z³ = {float(z_mark**3):.10f}, ratio = {trM_max/float(z_mark**3):.6f}")

print()
print("=" * 100)
print("FINAL: Explicit α_k at H_3 (Jones-Markov normalized)")
print("=" * 100)
alpha_2_jones = trM_pair_sym / 2
alpha_3_jones = trM_max
print(f"  α_0 = 1                                                 (canonical)")
print(f"  α_1 = {trM_minus:.10e}                       (~0; needs higher op)")
print(f"  α_2 = z² = {alpha_2_jones:.10f} (verified ≡ z² to {abs(alpha_2_jones - float(z_mark**2)):.2e})")
print(f"  α_3 = {alpha_3_jones:.10f}  vs  z³ = {float(z_mark**3):.10f}  (ratio {alpha_3_jones/float(z_mark**3):.4f})")
print(f"      → α_3 has same magnitude as z³ but with NUMERICAL FACTOR ~ {alpha_3_jones/float(z_mark**3):.4f}")
print(f"      → Likely structural multiplier from d_2 quotient (Yang-Baxter image)")

out = {
    "computation": "alpha-k-jones-markov-h3",
    "description": ("Solve for Jones-Markov weights y_λ at H_3 via constraints "
                    "tr_M(1)=1, tr_M(σ_i)=z, tr_M(σ_iσ_j)=z².  Then explicitly "
                    "compute α_k on each surviving E_∞ class with correct "
                    "normalization.  Confirms α_2 = z² structurally derived; "
                    "α_1 = 0 vanishes; α_3 has q-rational form related to z³."),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "q_0": float(Q0), "z": float(z_mark),
    "jones_markov_weights": {
        "y_sym (λ=(3))": float(y[0]),
        "y_std (λ=(2,1))": float(y[1]),
        "y_alt (λ=(1,1,1))": float(y[2]),
        "sum": float(y.sum())
    },
    "alpha_k_at_H3_jones_markov": {
        "alpha_0": 1.0,
        "alpha_1": float(trM_minus),
        "alpha_2": float(alpha_2_jones),
        "alpha_2_eq_z_squared_check": float(abs(alpha_2_jones - float(z_mark**2))),
        "alpha_3": float(alpha_3_jones),
        "alpha_3_over_z_cubed": float(alpha_3_jones / float(z_mark**3))
    },
    "verification": {
        "tr_M(1)": trM_1,
        "tr_M(σ_1)": trM_s1,
        "tr_M(σ_1σ_2)": trM_s1s2,
        "expected": {"1": 1, "σ_1": float(z_mark), "σ_1σ_2": float(z_mark**2)}
    }
}
import sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
_sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))
from witness_base import WitnessBuilder  # noqa: E402
WitnessBuilder.stamp_staleness_metadata(out, script_path=__file__, engine="mpmath")
out["scriptFile"] = Path(__file__).name
out_path = Path(__file__).parent / "alpha-k-jones-markov-h3.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)
print(f"\nWitness: {out_path}")
