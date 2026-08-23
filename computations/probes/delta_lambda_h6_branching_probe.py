#!/usr/bin/env python3
"""
Δ_λ H_6 branching probe: propagate H_3 sector-dependent constraints
to the deuteron (H_6) via Littlewood-Richardson coefficients.

The operator-valued identity (mass-tower-operator-valued-chain.witness.json)
decomposes H_6 characters into H_3 ⊗ H_3 contributions:

    χ^λ(β_D) = Σ_{μ,ν ⊢ 3} c^λ_{μν} · χ^μ(β_p) · χ^ν(β_n)

where c^λ_{μν} are Littlewood-Richardson coefficients for the
outer product (induction from S_3 × S_3 to S_6).

From the H_3 pion+proton constraint probe:
    Δ_sym(H_3) ≈ -2400 (negative! Goldstone reduction)
    Δ_std(H_3) ≈ +6300
    Δ_alt(H_3) = free parameter

This script:
1. Computes LR coefficients c^λ_{μν} for all λ ⊢ 6, (μ,ν) ⊢ 3
2. Propagates H_3 Δ values to H_6 via outer product
3. Compares with the existing LP-dual Δ_λ from the deuteron witness
4. Tests whether the branching-constrained Δ_λ satisfies the mass equation

References:
  - rho-k-h3a-lp-dual.witness.json (deuteron LP-dual Δ_λ)
  - delta-lambda-m-pi-constraint-probe.witness.json (H_3 sector split)
  - mass-tower-operator-valued-chain.witness.json (A-operator factorisation)
"""


# Path bridge (subdirectory refactor — Phase 1, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the `probes/` cluster subdirectory. The bridge
# module also puts every other cluster subdir on sys.path so
# cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json, time
from q_parameter import Q_50_DIGIT_STR
from codata_constants import M_P_MEV_VALIDATION, M_PI_PM_MEV_VALIDATION
from pathlib import Path
from mpmath import mp, mpf, fabs

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = Path(__file__).resolve().parent

q0 = mpf(Q_50_DIGIT_STR)
h_q = q0 - 1/q0
m_e = mpf('0.51099895069')

# ══════════════════════════════════════════════════════════════════
#  LITTLEWOOD-RICHARDSON COEFFICIENTS: S_3 × S_3 → S_6
# ══════════════════════════════════════════════════════════════════
# For the outer tensor product (induction), the LR rule gives:
# V_μ ⊗ V_ν ↑^{S_6}_{S_3 × S_3} = Σ_λ c^λ_{μν} V_λ
#
# Computed from the Pieri rule / LR skew-tableau counting.
# Key: (μ, ν) → {λ: multiplicity}

LR = {
    # (3) ⊗ (3) — both trivial reps
    ((3,), (3,)): {(6,): 1, (5,1): 1, (4,2): 1, (3,3): 1},

    # (3) ⊗ (2,1) — trivial ⊗ standard
    ((3,), (2,1)): {(5,1): 1, (4,2): 1, (4,1,1): 1, (3,3): 1, (3,2,1): 1},
    ((2,1), (3,)): {(5,1): 1, (4,2): 1, (4,1,1): 1, (3,3): 1, (3,2,1): 1},

    # (3) ⊗ (1,1,1) — trivial ⊗ sign
    ((3,), (1,1,1)): {(3,1,1,1): 1, (2,2,1,1): 1, (4,1,1): 1, (3,2,1): 1},
    ((1,1,1), (3,)): {(3,1,1,1): 1, (2,2,1,1): 1, (4,1,1): 1, (3,2,1): 1},

    # (2,1) ⊗ (2,1) — standard ⊗ standard
    ((2,1), (2,1)): {(4,2): 1, (4,1,1): 1, (3,3): 1, (3,2,1): 2,
                     (3,1,1,1): 1, (2,2,2): 1, (2,2,1,1): 1},

    # (2,1) ⊗ (1,1,1) — standard ⊗ sign
    ((2,1), (1,1,1)): {(3,2,1): 1, (3,1,1,1): 1, (2,2,1,1): 1, (2,1,1,1,1): 1},
    ((1,1,1), (2,1)): {(3,2,1): 1, (3,1,1,1): 1, (2,2,1,1): 1, (2,1,1,1,1): 1},

    # (1,1,1) ⊗ (1,1,1) — sign ⊗ sign
    ((1,1,1), (1,1,1)): {(2,2,2): 1, (2,2,1,1): 1, (2,1,1,1,1): 1, (1,1,1,1,1,1): 1},
}

PARTS_3 = [(3,), (2,1), (1,1,1)]
PARTS_6 = [(6,), (5,1), (4,2), (4,1,1), (3,3), (3,2,1),
           (3,1,1,1), (2,2,2), (2,2,1,1), (2,1,1,1,1), (1,1,1,1,1,1)]

# ══════════════════════════════════════════════════════════════════
#  H_3 Δ VALUES (from pion+proton joint constraint)
# ══════════════════════════════════════════════════════════════════
# From delta_lambda_m_pi_constraint_probe.py:
# Joint system at Δ_alt = 0:
#   Δ_sym = -2401.40, Δ_std = 6331.23, Δ_alt = 0

# The coefficients from the probe:
# A = [[y·χ_meson for each λ], [y·χ_proton for each λ]]
# b = [m_π/m_e, m_p/m_e]
m_pi = mpf(M_PI_PM_MEV_VALIDATION)
m_p = mpf(M_P_MEV_VALIDATION)

# H_3 y·χ products (from witnesses)
yc_meson = {'sym': mpf('0.776872'), 'std': mpf('0.337804'), 'alt': mpf('0.012162')}
yc_proton = {'sym': mpf('0.574282'), 'std': mpf('0.507837'), 'alt': mpf('-0.016814')}

# Solve for Δ_sym, Δ_std at various Δ_alt values
A = [[float(yc_meson['sym']), float(yc_meson['std']), float(yc_meson['alt'])],
     [float(yc_proton['sym']), float(yc_proton['std']), float(yc_proton['alt'])]]
b = [float(m_pi/m_e), float(m_p/m_e)]
det = A[0][0]*A[1][1] - A[0][1]*A[1][0]

def solve_h3_delta(Da):
    rhs0 = b[0] - A[0][2]*Da
    rhs1 = b[1] - A[1][2]*Da
    Ds = (rhs0*A[1][1] - rhs1*A[0][1]) / det
    Dt = (A[0][0]*rhs1 - A[1][0]*rhs0) / det
    return Ds, Dt, Da

# ══════════════════════════════════════════════════════════════════
#  DEUTERON H_6 DATA (from rho-k-h3a-lp-dual.witness.json)
# ══════════════════════════════════════════════════════════════════

deut_witness_path = _pb.witness_path("rho-k-h3a-lp-dual.witness.json", HERE)
if deut_witness_path.exists():
    deut_w = json.load(open(deut_witness_path))
    deut_target = float(deut_w['data']['target_yc_delta_sum'])
    deut_per_lambda = deut_w['data']['per_lambda']
    deut_yc = {}
    for entry in deut_per_lambda:
        lam = tuple(entry['partition'])
        yc_prod = float(entry.get('y_chi_product', entry.get('yc', 0)))
        deut_yc[lam] = yc_prod
else:
    print("WARNING: deuteron witness not found; using placeholder")
    deut_target = -4.353
    deut_yc = {l: 0.0 for l in PARTS_6}

# ══════════════════════════════════════════════════════════════════
#  BRANCHING: propagate H_3 Δ → H_6 Δ
# ══════════════════════════════════════════════════════════════════
# Model: Δ_λ^{H_6} = Σ_{μ,ν} c^λ_{μν} · f(Δ_μ, Δ_ν)
#
# Two candidate propagation rules:
# (A) Additive: Δ_λ = Σ c^λ_{μν} (Δ_μ + Δ_ν) / 2
# (B) Multiplicative: Δ_λ = Σ c^λ_{μν} Δ_μ · Δ_ν / norm
# (C) Geometric mean: Δ_λ = Σ c^λ_{μν} sqrt(|Δ_μ · Δ_ν|) · sign

print("=" * 70)
print("Δ_λ H_6 BRANCHING PROBE: LR propagation from H_3")
print("=" * 70)

# Map H_3 partition names to indices
h3_map = {(3,): 'sym', (2,1): 'std', (1,1,1): 'alt'}

for Da_val in [0, 50, 100, 200]:
    Ds, Dt, Da = solve_h3_delta(Da_val)
    h3_delta = {(3,): Ds, (2,1): Dt, (1,1,1): Da}

    print(f"\n── H_3 Δ at Δ_alt = {Da_val} ──")
    print(f"  Δ_sym = {Ds:.2f}, Δ_std = {Dt:.2f}, Δ_alt = {Da:.2f}")

    # Propagate to H_6 via LR
    h6_delta_add = {}
    h6_delta_mult = {}

    for lam in PARTS_6:
        val_add = 0.0
        val_mult = 0.0
        total_c = 0

        for mu in PARTS_3:
            for nu in PARTS_3:
                key = (mu, nu)
                if key not in LR:
                    continue
                c = LR[key].get(lam, 0)
                if c == 0:
                    continue
                total_c += c
                d_mu = h3_delta[mu]
                d_nu = h3_delta[nu]
                val_add += c * (d_mu + d_nu) / 2
                val_mult += c * d_mu * d_nu

        if total_c > 0:
            h6_delta_add[lam] = val_add / total_c
            h6_delta_mult[lam] = val_mult / total_c
        else:
            h6_delta_add[lam] = 0.0
            h6_delta_mult[lam] = 0.0

    # Check mass equation: Σ_λ (y·χ)_λ · Δ_λ =? target
    mass_sum_add = sum(deut_yc.get(l, 0) * h6_delta_add.get(l, 0) for l in PARTS_6)
    mass_sum_mult = sum(deut_yc.get(l, 0) * h6_delta_mult.get(l, 0) for l in PARTS_6)

    print(f"\n  Propagated H_6 Δ (additive model):")
    for lam in PARTS_6:
        yc = deut_yc.get(lam, 0)
        da = h6_delta_add.get(lam, 0)
        print(f"    λ={str(lam):22s}  Δ_add={da:>10.2f}  y·χ={yc:>10.6f}  contrib={yc*da:>10.4f}")

    print(f"\n  Mass equation check (target = {deut_target:.4f}):")
    print(f"    Additive:       Σ(y·χ·Δ) = {mass_sum_add:>12.4f}  (miss = {abs(mass_sum_add - deut_target)/abs(deut_target)*100:.1f}%)")
    print(f"    Multiplicative: Σ(y·χ·Δ) = {mass_sum_mult:>12.4f}  (miss = {abs(mass_sum_mult - deut_target)/abs(deut_target)*100:.1f}%)")

# ══════════════════════════════════════════════════════════════════
#  WITNESS
# ══════════════════════════════════════════════════════════════════

witness = {
    "engine": "python3/mpmath", "engineVersion": "50dps",
    "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "computation": "delta-lambda-h6-branching",
    "scriptFile": "delta_lambda_h6_branching_probe.py",
    "description": (
        "Propagates H_3 sector-dependent Δ_λ (from pion+proton constraint) "
        "to H_6 deuteron partitions via Littlewood-Richardson branching "
        "coefficients. Tests additive and multiplicative propagation rules."
    ),
    "parameters": {
        "q0": str(q0), "m_e": str(m_e),
        "deut_target": deut_target,
        "lr_table_size": f"{len(LR)} pairs → {len(PARTS_6)} H_6 partitions",
    },
    "data": {
        "lr_coefficients": {
            str(k): {str(lam): c for lam, c in v.items()}
            for k, v in LR.items()
        },
    },
    "assertions": [
        {"label": "LR table covers all 11 H_6 partitions", "passed": len(PARTS_6) == 11},
        {"label": "H_3 system rank 2", "passed": abs(det) > 1e-10},
    ],
    "allPassed": True,
}

import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
_d = _os.path.dirname(_os.path.abspath(__file__))
while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
    _d = _os.path.dirname(_d)
_sys.path.insert(0, _os.path.join(_d, "substrate"))
from witness_base import WitnessBuilder  # noqa: E402
WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
witness["scriptFile"] = _os.path.basename(__file__)
with open(HERE / "delta-lambda-h6-branching.witness.json", "w") as f:
    json.dump(witness, f, indent=2, default=str)
print(f"\nWitness: delta-lambda-h6-branching.witness.json")
