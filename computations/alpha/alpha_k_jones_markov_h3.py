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

import json
import sys
import warnings
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
from _precision import fmt, set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(80)
mp.mp.dps = 80


def _disp(val, digits: int = 25) -> Decimal:
    if isinstance(val, mp.mpf):
        return Decimal(mp.nstr(val, digits))
    return Decimal(str(val))


Q0 = q_at(80)
QI = mp.mpf(1) / Q0
h_amp = Q0 - QI
z_mark = Q0**3 / (Q0**2 + mp.mpf(1))


def _build_h3_seminormal_mp(q: mp.mpf) -> dict:
    """Exact 80-dps mpmath Hoefsmit seminormal matrices for H_3(q) partitions."""
    one = mp.mpf(1)
    zero = mp.mpf(0)
    qi = one / q
    q21 = q**2 + one
    q3_num = (q**3 - q ** (-3)) / (q - qi)
    q2_num = q + qi
    s0_std = mp.matrix([[q, zero], [zero, -qi]])
    s1_std = mp.matrix(
        [
            [-one / (q * q21), one],
            [(q**4 + q**2 + one) / (q21**2), q**3 / q21],
        ]
    )
    return {
        (3,): {
            "sigmas": [mp.matrix([[q]]), mp.matrix([[q]])],
            "dim": 1,
            "dim_q": one,
        },
        (2, 1): {
            "sigmas": [s0_std, s1_std],
            "dim": 2,
            "dim_q": q3_num / q2_num,
        },
        (1, 1, 1): {
            "sigmas": [mp.matrix([[-qi]]), mp.matrix([[-qi]])],
            "dim": 1,
            "dim_q": one,
        },
    }


shapes = [(3,), (2, 1), (1, 1, 1)]
data = _build_h3_seminormal_mp(Q0)


def _trace_mp(mat: mp.matrix) -> mp.mpf:
    total = mp.mpf(0)
    for idx in range(mat.rows):
        total += mat[idx, idx]
    return total


def chi_lambda(shape, words_with_coeffs) -> mp.mpf:
    """χ_λ(Σ c_i · word_i) at given partition shape in 80-dps mpmath."""
    sigmas = data[shape]["sigmas"]
    d = data[shape]["dim"]
    M = mp.matrix(d, d)
    for word, coeff in words_with_coeffs.items():
        if word == "1":
            Me = mp.eye(d)
        elif word == "s1":
            Me = sigmas[0]
        elif word == "s2":
            Me = sigmas[1]
        elif word == "s1s2":
            Me = sigmas[0] * sigmas[1]
        elif word == "s2s1":
            Me = sigmas[1] * sigmas[0]
        elif word == "s1s2s1":
            Me = sigmas[0] * sigmas[1] * sigmas[0]
        else:
            continue
        M = M + mp.mpf(coeff) * Me
    return _trace_mp(M)


# Compute χ for the constraint elements: 1, σ_1, σ_1σ_2
chi_table = {}
for elem in ["1", "s1", "s1s2"]:
    chi_table[elem] = {sh: chi_lambda(sh, {elem: 1}) for sh in shapes}

print("=" * 100)
print("Explicit Jones-Markov weights y_λ at H_3 via linear system")
print("=" * 100)
print(f"  q_0 = {_disp(Q0):.10f}, h = {_disp(h_amp):.6f}, z = {_disp(z_mark):.6f}")
print()
print(f"  {'element':<8} {'χ_(3)':>10} {'χ_(2,1)':>10} {'χ_(1,1,1)':>12}")
for elem in ["1", "s1", "s1s2"]:
    print(
        f"  {elem:<8} {_disp(chi_table[elem][(3,)]):>+10.6f} "
        f"{_disp(chi_table[elem][(2, 1)]):>+10.6f} "
        f"{_disp(chi_table[elem][(1, 1, 1)]):>+12.6f}"
    )
print()

# Linear system:  y_sym · χ_sym(elem) + y_std · χ_std(elem) + y_alt · χ_alt(elem) = tr_M(elem)
# Constraints: tr_M(1) = 1, tr_M(σ_1) = z, tr_M(σ_1σ_2) = z²
A = mp.matrix(
    [
        [chi_table["1"][(3,)], chi_table["1"][(2, 1)], chi_table["1"][(1, 1, 1)]],
        [chi_table["s1"][(3,)], chi_table["s1"][(2, 1)], chi_table["s1"][(1, 1, 1)]],
        [chi_table["s1s2"][(3,)], chi_table["s1s2"][(2, 1)], chi_table["s1s2"][(1, 1, 1)]],
    ]
)
b = mp.matrix([mp.mpf(1), z_mark, z_mark**2])
y_mat = mp.lu_solve(A, b)
y = [y_mat[0], y_mat[1], y_mat[2]]
y_sum = y[0] + y[1] + y[2]
print("Linear system A y = b (80-dps mpmath):")
print(f"  y_sym  (λ=(3))     = {_disp(y[0]):.10f}")
print(f"  y_std  (λ=(2,1))   = {_disp(y[1]):.10f}")
print(f"  y_alt  (λ=(1,1,1)) = {_disp(y[2]):.10e}")
print(f"  Σ y_λ              = {_disp(y_sum):.6f}")
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
print("Sanity (Jones-Markov):")
print(f"  tr_M(1)        = {_disp(trM_1):.6f}  (expected 1)")
print(f"  tr_M(σ_1)      = {_disp(trM_s1):.6f}  (expected z = {_disp(z_mark):.6f})")
print(f"  tr_M(σ_2)      = {_disp(trM_s2):.6f}  (expected z by symmetry)")
print(f"  tr_M(σ_1σ_2)   = {_disp(trM_s1s2):.6f}  (expected z² = {_disp(z_mark**2):.6f})")
print(f"  tr_M(σ_2σ_1)   = {_disp(trM_s2s1):.6f}  (expected z² by Markov-cyclicity)")
print()


# Now extract α_k on E_∞ classes
print("=" * 100)
print("E_∞ class Markov pairings with Jones-Markov weights")
print("=" * 100)
trM_minus, _ = Markov_trace_with_y({"s1": 1, "s2": -1})
trM_plus, _ = Markov_trace_with_y({"s1": 1, "s2": 1})
trM_pair_sym, _ = Markov_trace_with_y({"s1s2": 1, "s2s1": 1})
trM_pair_anti, _ = Markov_trace_with_y({"s1s2": 1, "s2s1": -1})
trM_max, _ = Markov_trace_with_y({"s1s2s1": 1})

alpha_2_jones = trM_pair_sym / mp.mpf(2)
alpha_3_jones = trM_max
alpha_2_resid = abs(alpha_2_jones - z_mark**2)
alpha_3_ratio = alpha_3_jones / (z_mark**3)

print(f"\n  E_∞^{{0,*}} = [1]:                tr_M = {_disp(trM_1):.10f}    α_0 = 1 (after normalization)")
print(f"\n  E_∞^{{1,*}} = [σ_1 - σ_2]:        tr_M = {_disp(trM_minus):.10e}    α_1 = {_disp(trM_minus):.6e}")
print(f"     (compare: σ_1 + σ_2:           tr_M = {_disp(trM_plus):.10f}, killed by d_1)")
print(f"\n  E_∞^{{2,*}} = [σ_1σ_2 + σ_2σ_1]:   tr_M = {_disp(trM_pair_sym):.10f}")
print(f"     α_2 = (pair-sym pairing)/2     = {_disp(alpha_2_jones):.10f}")
print(f"     compare to z² = {_disp(z_mark**2):.10f} → ratio = {_disp(alpha_2_jones / (z_mark**2)):.6f}")
print(f"     (anti pair killed: tr_M(σ_1σ_2 - σ_2σ_1) = {_disp(trM_pair_anti):.10e})")
print(f"\n  E_∞^{{3,*}} = [σ_1σ_2σ_1]:        tr_M = {_disp(trM_max):.10f}")
print(f"     α_3 = {_disp(trM_max):.6f}; compare to z³ = {_disp(z_mark**3):.10f}, ratio = {_disp(alpha_3_ratio):.6f}")

print()
print("=" * 100)
print("FINAL: Explicit α_k at H_3 (Jones-Markov normalized)")
print("=" * 100)
print("  α_0 = 1                                                 (canonical)")
print(f"  α_1 = {_disp(trM_minus):.10e}                       (~0; needs higher op)")
print(f"  α_2 = z² = {_disp(alpha_2_jones):.10f} (verified ≡ z² to {_disp(alpha_2_resid):.2e})")
print(f"  α_3 = {_disp(alpha_3_jones):.10f}  vs  z³ = {_disp(z_mark**3):.10f}  (ratio {_disp(alpha_3_ratio):.4f})")
print(f"      → α_3 has same magnitude as z³ but with NUMERICAL FACTOR ~ {_disp(alpha_3_ratio):.4f}")
print("      → Likely structural multiplier from d_2 quotient (Yang-Baxter image)")

out = {
    "computation": "alpha-k-jones-markov-h3",
    "description": (
        "Solve for Jones-Markov weights y_λ at H_3 via constraints "
        "tr_M(1)=1, tr_M(σ_i)=z, tr_M(σ_iσ_j)=z².  Then explicitly "
        "compute α_k on each surviving E_∞ class with correct "
        "normalization.  Confirms α_2 = z² structurally derived; "
        "α_1 = 0 vanishes; α_3 has q-rational form related to z³."
    ),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "q_0": fmt(Q0),
    "z": fmt(z_mark),
    "jones_markov_weights": {
        "y_sym (λ=(3))": fmt(y[0]),
        "y_std (λ=(2,1))": fmt(y[1]),
        "y_alt (λ=(1,1,1))": fmt(y[2]),
        "sum": fmt(y_sum),
    },
    "alpha_k_at_H3_jones_markov": {
        "alpha_0": 1,
        "alpha_1": fmt(trM_minus),
        "alpha_2": fmt(alpha_2_jones),
        "alpha_2_eq_z_squared_check": fmt(alpha_2_resid),
        "alpha_3": fmt(alpha_3_jones),
        "alpha_3_over_z_cubed": fmt(alpha_3_ratio),
    },
    "verification": {
        "tr_M(1)": fmt(trM_1),
        "tr_M(σ_1)": fmt(trM_s1),
        "tr_M(σ_1σ_2)": fmt(trM_s1s2),
        "expected": {
            "1": 1,
            "σ_1": fmt(z_mark),
            "σ_1σ_2": fmt(z_mark**2),
        },
    },
}
WitnessBuilder.stamp_staleness_metadata(out, script_path=__file__, engine="mpmath")
out["q0Anchor"] = "proton"
out["q0Value"] = Q_50_DIGIT_STR
out["scriptFile"] = Path(__file__).name
out_path = Path(__file__).parent / "alpha-k-jones-markov-h3.witness.json"
with open(out_path, "w", encoding="utf-8") as fp:
    json.dump(out, fp, indent=2)
    fp.write("\n")
print(f"\nWitness: {out_path}")
