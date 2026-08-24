#!/usr/bin/env python3
"""
Beta decay as a matrix-valued polynomial in q.

The three crossing transfer matrices T_pp, T_nn, T_mix are 2×2 with
entries in Z[q^±½].  Beta decay is the difference:
  Δ_β^{nn→mix} = T_mix - T_nn    (partner is neutron)
  Δ_β^{mix→pp} = T_pp - T_mix    (partner is proton)

This script computes all matrices symbolically (in q) and numerically
(at q = 1.110), then works the tritium example.

Output: computations/beta-decay-matrix.witness.json
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mp

sys.path.insert(0, str(Path(__file__).parent))
# The _MP family, not the f64 one. q_parameter builds these AFTER raising its
# own working precision to >= 50 dps, so they are not the "constant built too
# early" trap -- checked at q_parameter.py:181, `_mp.mp.dps = max(_mp.mp.dps, 50)`
# sits directly above their construction. HA is the Hecke coefficient every
# transfer and decay matrix below is built from; as float64 it put 20 raw
# float64 fields into this witness.
from q_parameter import (Q_MP as Q, Q_INV_MP as Q_INV, HA_MP as HA,  # noqa: E402
                         S_SKEIN_MP as S)
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# ── Parameters ───────────────────────────────────────────────────

Q_HALF = mp.sqrt(Q)
Q_INV_HALF = mp.mpf(1) / Q_HALF
Z = 1.0 / (Q_HALF + Q_INV_HALF)  # Markov parameter z = 1/(q^½ + q^{-½})

print(f"q = {Q}")
print(f"q⁻¹ = {Q_INV:.10f}")
print(f"q½ = {Q_HALF:.10f}")
print(f"q - q⁻¹ = {HA:.10f}  (Hecke coefficient)")
print(f"q½ - q⁻½ = {S:.10f}  (Skein amplitude)")
print(f"z = 1/(q½ + q⁻½) = {Z:.10f}  (Markov parameter)")
print()


# ── Transfer matrices ────────────────────────────────────────────

def transfer_matrix(c, d, q=Q, ha=HA):
    """Build the 2×2 transfer matrix from crossing coefficients (c, d).

    T(c,d) = ( c·(q-q⁻¹) + d,  c )
             (      c,         d )
    """
    return [
        [c * ha + d, c],
        [c,          d],
    ]


def mat_str(M, name=""):
    """Pretty-print a 2×2 matrix."""
    lines = []
    if name:
        lines.append(f"{name}:")
    lines.append(f"  ( {M[0][0]:+.10f}  {M[0][1]:+.10f} )")
    lines.append(f"  ( {M[1][0]:+.10f}  {M[1][1]:+.10f} )")
    return "\n".join(lines)


def mat_mul(A, B):
    """Multiply two 2×2 matrices."""
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]],
    ]


def mat_sub(A, B):
    """Subtract two 2×2 matrices."""
    return [
        [A[0][0]-B[0][0], A[0][1]-B[0][1]],
        [A[1][0]-B[1][0], A[1][1]-B[1][1]],
    ]


def mat_det(M):
    """Determinant of 2×2 matrix."""
    return M[0][0]*M[1][1] - M[0][1]*M[1][0]


def traced_volume(M):
    """V̂ = z · M₁₁ + M₂₁"""
    return Z * M[0][0] + M[1][0]


# ── Crossing coefficients ────────────────────────────────────────

c_pp, d_pp = mp.mpf(1), mp.mpf(0)
c_nn, d_nn = mp.mpf(1), -HA
c_mix, d_mix = mp.mpf(1), -HA / 2

print("═══ Crossing coefficients (c, d) ═══")
print(f"  pp:    c = {c_pp:.10f},  d = {d_pp:.10f}")
print(f"  nn:    c = {c_nn:.10f},  d = {d_nn:.10f}")
print(f"  mixed: c = {c_mix:.10f},  d = {d_mix:.10f}")
print()


# ── The three transfer matrices ──────────────────────────────────

T_pp = transfer_matrix(c_pp, d_pp)
T_nn = transfer_matrix(c_nn, d_nn)
T_mix = transfer_matrix(c_mix, d_mix)

print("═══ Transfer matrices at q = 1.110 ═══")
print(mat_str(T_pp, "T_pp"))
print()
print(mat_str(T_nn, "T_nn"))
print()
print(mat_str(T_mix, "T_mix"))
print()

print(f"  det(T_pp)  = {mat_det(T_pp):+.10f}  (= -cd = 0)")
print(f"  det(T_nn)  = {mat_det(T_nn):+.10f}  (= -c²·ha - cd)")
print(f"  det(T_mix) = {mat_det(T_mix):+.10f}")
print()


# ── The two elementary beta decay matrices ───────────────────────

Delta_nn_mix = mat_sub(T_mix, T_nn)
Delta_mix_pp = mat_sub(T_pp, T_mix)

print("═══ Elementary β⁻ decay matrices ═══")
print()
print("Δ_β^{nn→mix}(q) = T_mix - T_nn  [partner is neutron]")
print(mat_str(Delta_nn_mix, "Δ_β^{nn→mix}"))
print()
print("Δ_β^{mix→pp}(q) = T_pp - T_mix  [partner is proton]")
print(mat_str(Delta_mix_pp, "Δ_β^{mix→pp}"))
print()

# Symbolic form
print("Symbolic entries of Δ_β^{nn→mix}:")
print(f"  (1,1): (q-q⁻¹) - ½(q-q⁻¹) - [(q-q⁻¹) - (q-q⁻¹)]")
print(f"       = 0")
print(f"       = {Delta_nn_mix[0][0]:+.10f}")
print(f"  (1,2): 1 - 1 = 0 = {Delta_nn_mix[0][1]:+.10f}")
print(f"  (2,1): 1 - 1 = 0 = {Delta_nn_mix[1][0]:+.10f}")
print(f"  (2,2): -½(q-q⁻¹) - (-(q-q⁻¹)) = ½(q-q⁻¹) = {Delta_nn_mix[1][1]:+.10f}")
print()
print("Symbolic entries of Δ_β^{mix→pp}:")
print(f"  (1,1): (q-q⁻¹) - [(q-q⁻¹) - ½(q-q⁻¹)]")
print(f"       = ½(q-q⁻¹)")
print(f"       = {Delta_mix_pp[0][0]:+.10f}")
print(f"  (1,2): 1 - 1 = 0 = {Delta_mix_pp[0][1]:+.10f}")
print(f"  (2,1): 1 - 1 = 0 = {Delta_mix_pp[1][0]:+.10f}")
print(f"  (2,2): 0 - (-½(q-q⁻¹)) = ½(q-q⁻¹) = {Delta_mix_pp[1][1]:+.10f}")
print()

# KEY OBSERVATION
print("═══ KEY OBSERVATION ═══")
print(f"  Δ_β^{{nn→mix}} = Δ_β^{{mix→pp}}  ?  ", end="")
same = all(abs(Delta_nn_mix[i][j] - Delta_mix_pp[i][j]) < 1e-15
           for i in range(2) for j in range(2))
print(f"{'YES!' if same else 'NO'}")
if same:
    print(f"  Both elementary decay matrices are IDENTICAL!")
    print(f"  There is only ONE β decay matrix:")
    print(f"")
    print(f"  Δ_β(q) = ½(q-q⁻¹) · I")
    print(f"")
    print(f"         = (HA/2) · I  where HA = q - q⁻¹")
    print(f"")
    print(f"  where s = q½ - q⁻½ and I is the 2×2 identity.")
print()


# ── Tritium worked example ───────────────────────────────────────

print("═══ TRITIUM: ³H(p,n,n) → ³He(p,p,n) ═══")
print()
print("Nucleon layout: [0:p, 1:n→p, 2:n]")
print("Converting nucleon: position 1 (first neutron)")
print()

# Generator σ_0: crossings with nucleon 1 and nucleon 2
# Parent: (0,1)=pn=mixed, (0,2)=pn=mixed
# Daughter: (0,1)=pp, (0,2)=pn=mixed
print("Generator σ_0 (2 crossings):")
print("  Parent:   crossing(0,1)=pn [mixed] × crossing(0,2)=pn [mixed]")
print("  Daughter: crossing(0,1)=pp × crossing(0,2)=pn [mixed]")
print()

# Parent σ_0: start (a,b)=(0,1), multiply by T_mix twice
M0_par = mat_mul(T_mix, T_mix)
V0_par = traced_volume(M0_par)
print(f"  M₀^par = T_mix · T_mix")
print(mat_str(M0_par, "  M₀^par"))
print(f"  V̂₀^par = z·M₁₁ + M₂₁ = {V0_par:+.10f}")
print()

# Daughter σ_0: T_pp × T_mix (crossing (0,1) changes to pp)
M0_dau = mat_mul(T_pp, T_mix)
V0_dau = traced_volume(M0_dau)
print(f"  M₀^dau = T_pp · T_mix")
print(mat_str(M0_dau, "  M₀^dau"))
print(f"  V̂₀^dau = z·M₁₁ + M₂₁ = {V0_dau:+.10f}")
print()

# The difference at σ_0
DM0 = mat_sub(M0_dau, M0_par)
print(f"  ΔM₀ = M₀^dau - M₀^par = Δ_β · T_mix  (left factor changed)")
print(mat_str(DM0, "  ΔM₀"))
DV0 = V0_dau - V0_par
print(f"  ΔV̂₀ = {DV0:+.10f}")
print()

# Generator σ_1: 1 crossing with nucleon 2
# Parent: (1,2)=nn
# Daughter: (1,2)=pn=mixed
print("Generator σ_1 (1 crossing):")
print("  Parent:   crossing(1,2)=nn")
print("  Daughter: crossing(1,2)=pn [mixed]")
print()

M1_par = T_nn
V1_par = traced_volume(M1_par)
print(f"  M₁^par = T_nn")
print(mat_str(M1_par, "  M₁^par"))
print(f"  V̂₁^par = {V1_par:+.10f}")
print()

M1_dau = T_mix
V1_dau = traced_volume(M1_dau)
print(f"  M₁^dau = T_mix")
print(mat_str(M1_dau, "  M₁^dau"))
print(f"  V̂₁^dau = {V1_dau:+.10f}")
print()

DV1 = V1_dau - V1_par
print(f"  ΔV̂₁ = {DV1:+.10f}")
print()

# The Skein polynomial ratio
print("═══ RESULTS ═══")
print()
P_par = V0_par * V1_par
P_dau = V0_dau * V1_dau
print(f"P_³H(q)  = V̂₀^par · V̂₁^par = {V0_par:.10f} × {V1_par:.10f} = {P_par:.10f}")
print(f"P_³He(q) = V̂₀^dau · V̂₁^dau = {V0_dau:.10f} × {V1_dau:.10f} = {P_dau:.10f}")
print()
ratio = P_dau / P_par
print(f"P_³He / P_³H = {ratio:.10f}")
print(f"ln(P_³He / P_³H) = {float(mp.log(abs(ratio))):+.10f}")
print()

# Q_q from the polynomial ratio
HBAR_Q2 = (1 - Q_INV)**2
Q_q = mp.log(abs(P_dau / P_par)) / HBAR_Q2
print(f"ℏ_q² = {HBAR_Q2:.10f}")
print(f"𝒬_q = ln|P_dau/P_par| / ℏ_q² = {float(Q_q):+.6f}  (Hecke units)")
print(f"𝒬_q^exp = 0.01861 MeV")
print()

# Per-generator contribution
print("Per-generator log-ratio:")
lr0 = mp.log(abs(V0_dau / V0_par))
lr1 = mp.log(abs(V1_dau / V1_par))
print(f"  σ_0: ln(V̂₀^dau/V̂₀^par) = {float(lr0):+.10f}")
print(f"  σ_1: ln(V̂₁^dau/V̂₁^par) = {float(lr1):+.10f}")
print(f"  sum: {float(lr0 + lr1):+.10f}")
print()

# ── Write witness ────────────────────────────────────────────────

witness = {
    "computation": "beta-decay-matrix",
    "description": "Beta decay as matrix-valued polynomial in q",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "parameters": {
        "q": Q,
        "hecke_coeff": HA,
        "skein_amplitude": S,
        "markov_z": Z,
        "hbar_q2": HBAR_Q2,
    },
    "crossing_coefficients": {
        "pp": {"c": c_pp, "d": d_pp},
        "nn": {"c": c_nn, "d": d_nn},
        "mixed": {"c": c_mix, "d": d_mix},
    },
    "transfer_matrices": {
        "T_pp": T_pp,
        "T_nn": T_nn,
        "T_mix": T_mix,
    },
    "decay_matrices": {
        "Delta_nn_mix": Delta_nn_mix,
        "Delta_mix_pp": Delta_mix_pp,
        "identical": same,
    },
    "tritium": {
        "parent": "3H (p,n,n)",
        "daughter": "3He (p,p,n)",
        "sigma_0": {
            "crossings": 2,
            "parent_type": "mix × mix",
            "daughter_type": "pp × mix",
            "V_par": V0_par,
            "V_dau": V0_dau,
            "log_ratio": lr0,
        },
        "sigma_1": {
            "crossings": 1,
            "parent_type": "nn",
            "daughter_type": "mix",
            "V_par": V1_par,
            "V_dau": V1_dau,
            "log_ratio": lr1,
        },
        "P_par": P_par,
        "P_dau": P_dau,
        "ratio": ratio,
        "ln_ratio": mp.log(abs(ratio)),
        "Q_q_hecke_units": Q_q,
    },
}

out_path = Path(__file__).parent / "beta-decay-matrix.witness.json"
with open(out_path, "w") as f:
    # Provenance envelope. This producer writes its witness as raw JSON, so
    # nothing stamps `scriptFile` / `scriptHash` on it — and a witness missing
    # either cannot be checked against its producer, so it drops OUT of the
    # self-staleness audit and reads as "not stale" forever. Re-running one
    # then looks like progress while removing it from the count: a false
    # drain. Detector: computations/witness_drain_audit.py.
    #
    # `stamp_staleness_metadata`, not `wrap_legacy().save()`: it adds the
    # fields in place and leaves the on-disk shape untouched, so no consumer
    # of this witness's legacy records has to change. `engine` is passed back
    # from the payload because the helper overwrites it.
    try:
        from witness_base import WitnessBuilder  # noqa: E402
    except ImportError:  # cluster subdir without the _path_bridge bootstrap
        import sys as _sys
        from pathlib import Path as _Path
        _sys.path.insert(0, str(next(
            _a / "substrate" for _a in _Path(__file__).resolve().parents
            if (_a / "substrate" / "witness_base.py").is_file())))
        from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__,
        engine=witness.get("engine", "python"))
    json.dump(witness, f, indent=2, default=str)
print(f"Witness: {out_path}")
