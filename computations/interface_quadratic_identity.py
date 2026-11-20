#!/usr/bin/env python3
"""
Interface quadratic structure — (σ−h/2)² = 1+h²/4 (SCALAR).

Computes binding predictions using the quadratic factorization:
  n crossings of averaged σ₃:
    n even: (σ−h/2)^n = (1+h²/4)^{n/2} · I   (pure scalar)
    n odd:  (σ−h/2)^n = (1+h²/4)^{(n-1)/2} · (σ−h/2)  (linear)

The interface's quadratic terms factor as a universal scalar.
Only ONE effective crossing carries operator-valued content.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json, time
from q_parameter import Q_50_DIGIT_STR, Q_MP
from pathlib import Path
from mpmath import mp, mpf, fabs

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
HERE = Path(__file__).resolve().parent

q0 = Q_MP
qi = 1/q0
h = q0 - qi
two_q = q0 + qi
m_e = mpf('0.51099895069')

# The scalar factor
scalar_sq = 1 + h**2/4  # (σ−h/2)² = this scalar
assert fabs(scalar_sq - two_q**2/4) < mpf('1e-40'), "scalar ≠ [2]²/4"

print("INTERFACE QUADRATIC IDENTITY")
print(f"  (σ−h/2)² = 1 + h²/4 = [2]_q²/4 = {float(scalar_sq):.10f}")
print(f"  Verified: matches (q+q⁻¹)²/4 to 10⁻⁴⁰")
print()

# For n averaged crossings:
for n in [1, 2, 3, 4, 5, 6, 7]:
    if n % 2 == 0:
        factor = scalar_sq ** (n // 2)
        kind = "SCALAR"
    else:
        factor = scalar_sq ** ((n - 1) // 2)
        kind = f"× (σ−h/2)"
    print(f"  n={n}: (σ−h/2)^{n} = {float(factor):.8f} {kind}")

print()

# Deuteron: 5 interface crossings → scalar × (σ−h/2)
# The scalar part = (1+h²/4)² ≈ 1.022
# The (σ−h/2) part has eigenvalues ±[2]/2 ≈ ±1.005

n_interface_D = 5
scalar_D = float(scalar_sq ** ((n_interface_D - 1) // 2))
eig_plus = float(two_q / 2)
eig_minus = float(-two_q / 2)

print(f"DEUTERON (5 interface crossings):")
print(f"  scalar part: (1+h²/4)² = {scalar_D:.8f}")
print(f"  linear eigenvalues: +{eig_plus:.6f} and {eig_minus:.6f}")
print(f"  → R(extremal) ≈ ±{scalar_D * eig_plus:.6f}")
print(f"  Observed R((6,)) = +1.005, R((1⁶)) = −1.005")
print(f"  Match: {abs(scalar_D * eig_plus - 1.005) / 1.005 * 100:.1f}%")

# Witness — routed through WitnessBuilder (cmiy/1j39: staleness-tracked,
# replaces the hand-rolled dict + json.dump so the witness carries
# scriptHash / commitSha / durationMs / engineVersion).
from witness_base import WitnessBuilder  # noqa: E402

data_payload = {
    "identity": "(sigma - h/2)^2 = 1 + h^2/4",
    "scalar_value": str(scalar_sq),
    "equals_two_q_sq_over_4": True,
    "deuteron_5_crossings": {
        "scalar_factor": scalar_D,
        "linear_eigenvalues": [eig_plus, eig_minus],
        "R_extremal_predicted": scalar_D * eig_plus,
        "R_extremal_observed": 1.005,
        "match_pct": abs(scalar_D * eig_plus - 1.005) / 1.005 * 100,
    },
}
wb = WitnessBuilder.wrap_legacy(
    "interface-quadratic-identity", data_payload,
    script_path=__file__, engine="python3/mpmath",
)
wb.set_description(
    "PROVED: (sigma-h/2)^2 = 1+h^2/4 = [2]_q^2/4 (SCALAR). "
    "From Hecke relation sigma^2 = h*sigma + 1. "
    "Even powers are identity; odd powers are linear. "
    "5 interface crossings = (1+h^2/4)^2 * (sigma-h/2). "
    "Lean-proved in TwoRoutesProtonMass.lean."
)
wb.add_assertion(
    "scalar = [2]_q^2/4",
    computed=int(bool(fabs(scalar_sq - two_q ** 2 / 4) < mpf('1e-40'))),
    expected=1,
)
wb.add_assertion(
    "extremal R within 3%",
    computed=int(bool(abs(scalar_D * eig_plus - 1.005) < 0.03 * 1.005)),
    expected=1,
)
out = wb.save()
print(f"\nWitness: {out}")
