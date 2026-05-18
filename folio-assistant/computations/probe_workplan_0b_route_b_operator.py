#!/usr/bin/env python3
"""Route B concrete compute: operator-valued Frobenius at H_4 for
the nucleon mass M_N.

Per the Workplan-0b/M_N spec, the operator-valued LR-decomposition
framework (introduced by PR #663 / wired by PR #689) gives a richer
Frobenius structure than the scalar Markov trace. Test whether
this richer structure produces M_N at substrate level.

## The operator-valued setup

At H_4(q), the canonical Markov trace splits via Littlewood-
Richardson into a SUM of partition-block contributions:

  τ_M(β) = Σ_λ y_λ(q) · χ^λ(β)        (scalar form)

vs the OPERATOR-valued form:

  T̂_M(β) = Σ_λ y_λ(q) · ρ_λ(β)         (operator, ∈ ⊕_λ End(V_λ))

The scalar τ_M loses the per-block matrix structure. M_N may
correspond to a SPECIFIC matrix entry or eigenvalue of T̂_M, not
the full trace.

## Test bench

1. Compute χ^λ(β_proton) symbolically for each λ ⊢ 4
2. For each λ, find scalar invariants of ρ_λ(β_proton):
   - eigenvalues (Λ_λ_i)
   - trace (= χ^λ already)
   - determinant (= product of eigenvalues)
   - spectral radius (max |eigenvalue|)
3. Test scale factors: m_e · invariant · Vol-factor
4. Find best match to M_N ≈ 938.918 MeV
"""
from __future__ import annotations
import json, sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from witness_base import WitnessBuilder
from q_parameter import Q_50_DIGIT_STR
from experimental_constants import M_E_MEV, M_P_MEV, Q_NEUTRON_MEV
from hoefsmit_symbolic import Q, chi_lambda_symbolic
from hecke_character_symbolic import hoefsmit_matrices_symbolic

mp.mp.dps = 80
Q_NUM = mp.mpf(Q_50_DIGIT_STR)
HBAR = (Q_NUM - 1) / Q_NUM
G = mp.catalan
VOL_B3 = 8 * G

M_E = mp.mpf(repr(M_E_MEV))
M_P = mp.mpf(repr(M_P_MEV))
M_N = M_P + mp.mpf(repr(Q_NEUTRON_MEV)) + M_E
M_NUCLEON = (M_P + M_N) / 2


def main() -> int:
    w = WitnessBuilder("workplan-0b-route-b-operator", engine="sympy+mpmath")
    w.set_description(
        "Route B concrete: operator-valued ρ_λ(β_proton) at H_4 + "
        "scalar-invariant scan (eigenvalues, det, spectral radius) "
        "against M_N target."
    )
    w.set_content_block("conj:flavor-dressed-mass-from-substrate-split")

    # Canonical proton: σ_1 σ_2 σ_1 = full positive twist Δ on 3 strands
    # Or the Borromean (σ_1 σ_2^{-1})^3 — try both
    # H_4 requires 3 generators (σ_1, σ_2, σ_3 = gen_idx 0,1,2)
    # For proton in H_3 stabilised to H_4: append σ_3^?
    # Test β = (σ_1 σ_2^{-1})^3 · σ_3 (Markov-stabilised Borromean)
    crossings_borromean_stab = []
    for _ in range(3):
        crossings_borromean_stab.append((0, "sigma"))
        crossings_borromean_stab.append((1, "sigma_inv"))
    crossings_borromean_stab.append((2, "sigma"))

    # Compute ρ_λ(β) matrices at H_4 for each partition of 4
    shapes = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
    invariants = {}
    print(f"Operator-valued ρ_λ(β_Bor_stab) at H_4(q_0):")
    print(f"  β = (σ_1 σ_2^{{-1}})^3 · σ_3 (Markov-stabilised Borromean)")
    print()
    print(f"  {'λ':<12s}  {'dim':>3s}  {'tr':>20s}  {'det':>20s}  {'spec_rad':>20s}")
    for shape in shapes:
        try:
            matrices, dim, _ = hoefsmit_matrices_symbolic(shape, Q)
        except Exception as e:
            print(f"  {str(shape):<12s}: FAIL ({e})")
            continue
        # Build ρ(β) matrix product
        from sympy import eye
        rho = eye(dim)
        h_sym = Q - 1/Q
        for gen_idx, ctype in crossings_borromean_stab:
            sigma_g = matrices[gen_idx]
            if ctype == "sigma":
                cross = sigma_g
            elif ctype == "sigma_inv":
                # σ^{-1} = σ - h (from Hecke σ²=hσ+1)
                cross = sigma_g - h_sym * eye(dim)
            elif ctype == "averaged":
                cross = sigma_g - (h_sym/2) * eye(dim)
            rho = sp.cancel(rho * cross)
        # Scalar invariants:
        trace_rho = sp.cancel(rho.trace())
        det_rho = sp.cancel(rho.det())
        # Eigenvalues at q_0 (numerical)
        try:
            rho_num = rho.evalf(subs={Q: float(Q_NUM)})
            eigvals = list(rho_num.eigenvals().keys())
            spec_rad_num = max(abs(complex(ev)) for ev in eigvals)
        except Exception:
            spec_rad_num = float("nan")
        trace_num = float(trace_rho.evalf(subs={Q: float(Q_NUM)}))
        det_num = float(det_rho.evalf(subs={Q: float(Q_NUM)}))
        print(f"  {str(shape):<12s}  {dim:>3d}  {trace_num:>20.10f}  {det_num:>20.10e}  {spec_rad_num:>20.10f}")
        invariants[str(shape)] = {
            "dim": dim,
            "trace": trace_num,
            "det": det_num,
            "spec_rad": float(spec_rad_num),
        }
    w.add_data("rho_lambda_invariants_at_q0", invariants)

    print()
    # Test scale: m_e · (sum of spec radii) · Vol_factor
    scale_factors = {
        "Σ spec_rad · Vol(B_3)/ℏ_q² · m_e":
            sum(inv["spec_rad"] for inv in invariants.values()) * float(VOL_B3 / HBAR**2 * M_E),
        "Σ |det| · Vol(B_3)/ℏ_q² · m_e":
            sum(abs(inv["det"]) for inv in invariants.values()) * float(VOL_B3 / HBAR**2 * M_E),
        "max spec_rad · Vol(B_3)/ℏ_q² · m_e":
            max(inv["spec_rad"] for inv in invariants.values()) * float(VOL_B3 / HBAR**2 * M_E),
        "Σ trace · Vol(B_3)/ℏ_q² · m_e (= τ_M)":
            sum(inv["trace"] for inv in invariants.values()) * float(VOL_B3 / HBAR**2 * M_E),
        "spec_rad(λ=(2,2)) · Vol(B_3)/ℏ_q² · m_e":
            invariants["(2, 2)"]["spec_rad"] * float(VOL_B3 / HBAR**2 * M_E) if "(2, 2)" in invariants else None,
    }
    print(f"  Scale candidates vs M_N = {float(M_NUCLEON):.3f} MeV:")
    for name, val in scale_factors.items():
        if val is None:
            continue
        rel = (val - float(M_NUCLEON)) / float(M_NUCLEON) * 100
        marker = " *MATCH" if abs(rel) < 1 else ""
        print(f"    {name:50s} = {val:>12.4f}  ({rel:+.2f}%){marker}")

    w.add_data("scale_candidates", {k: v for k, v in scale_factors.items() if v is not None})
    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
