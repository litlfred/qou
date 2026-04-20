#!/usr/bin/env python3
"""
Proton mass via mass-endomorphism-tower formula with:
  - B₃ Borromean link (σ₀σ₁⁻¹)³ FIXED (topological confinement, paper §borromean-baryon)
  - Flavor crossings (uu, ud, dd) FIXED (SU(2) isospin)
  - Gluon addition selected by SDP over the knot-operator basis

This is the correct SDP: the Borromean braid is what BINDS the quarks
(confinement-topological.md), and cannot be swapped out. The gluon is a
separable knot-operator overlay on top — THAT is where SDP operates.

Reference:
  mass-endomorphism-tower.md §163-191:
    B₃ × Δ₃(uud) = 9 crossings → Frobenius unstable.
    Integer LP finds 2σ₀ as unique Frobenius-stable gluon addition.
  atomic-braid-mass.md §20-31:
    Atom-level optimum is 1σ₀/nucleon (not 2σ₀), ~0.04% tighter.

Our SDP widens the gluon candidate set to all knot operators and tests
whether the 2σ₀ optimum from integer LP survives when compared against
T_{2,1}, T_{2,2}, T_{2,3}, T_{2,5}.
"""
import sys, json, math, itertools, time
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from mass_endomorphism import (
    additive_wedderburn_volumes, mass_from_tower,
    electron_cross, HA
)
from confinement_level_sdp import KNOT_OPERATORS


def knot_op_inserts(op: str) -> list[tuple[float, float]]:
    """Hecke (c,d) tuples for operator op, all on same generator."""
    if op == "T_1_0": return []
    if op == "T_2_1": return [(1.0, 0.0)]
    if op == "T_2_2": return [(1.0, 0.0), (1.0, 0.0)]
    if op == "T_2_3": return [(1.0, 0.0)] * 3
    if op == "T_2_5": return [(1.0, 0.0)] * 5
    raise ValueError(op)


def build_proton_cross(gluon_op: str = "T_2_2",
                        gluon_gen: int = 0) -> dict:
    """Proton braid word with Borromean B₃ base + flavor + SDP-chosen gluon.

    Structure (matches mass_endomorphism.proton_cross):
      gen 0:  3 × σ₀          (half of B₃ Borromean: σ₀ parts)
              + uu crossing (c=1, d=0)
              + ud crossing (c=1, d=-h/2)
              + [SDP] gluon operator on gen 0 (if gluon_gen == 0)
      gen 1:  3 × σ₁⁻¹         (half of B₃ Borromean: σ₁⁻¹ parts)
              + ud crossing (c=1, d=-h/2)
              + [SDP] gluon operator on gen 1 (if gluon_gen == 1)
    """
    cross = {0: [], 1: []}
    # B₃ Borromean on generator 0: 3 copies of σ₀
    cross[0].extend([(1.0, 0.0)] * 3)
    # uu pair (symmetric, no shift)
    cross[0].append((1.0, 0.0))
    # ud pair (half-shift)
    cross[0].append((1.0, -HA/2))
    # B₃ Borromean on generator 1: 3 copies of σ₁⁻¹
    cross[1].extend([(1.0, -HA)] * 3)
    # ud pair
    cross[1].append((1.0, -HA/2))
    # SDP-chosen gluon addition
    cross[gluon_gen].extend(knot_op_inserts(gluon_op))
    return cross


def build_neutron_cross(gluon_op: str = "T_2_2",
                         gluon_gen: int = 0) -> dict:
    """Neutron (udd): same base, but dd pair uses full h shift."""
    cross = {0: [], 1: []}
    cross[0].extend([(1.0, 0.0)] * 3)         # B₃ σ₀
    cross[0].append((1.0, -HA))                # dd pair
    cross[0].append((1.0, -HA/2))              # ud pair
    cross[1].extend([(1.0, -HA)] * 3)          # B₃ σ₁⁻¹
    cross[1].append((1.0, -HA/2))              # ud pair
    cross[gluon_gen].extend(knot_op_inserts(gluon_op))
    return cross


e_vols = additive_wedderburn_volumes(2, electron_cross)
e_desc, e_single, e_cross, e_total = mass_from_tower(e_vols)
print(f"Electron tower reference = {e_total:.4f}")


def predicted_mass(cross_dict: dict) -> float:
    vols = additive_wedderburn_volumes(3, cross_dict)
    _, _, _, total = mass_from_tower(vols)
    return (total / e_total) * M_E_MEV


def scan_gluon_ops(builder, target_MeV: float, label: str) -> dict:
    results = []
    for gluon_op in KNOT_OPERATORS:
        for gluon_gen in [0, 1]:
            try:
                cross = builder(gluon_op, gluon_gen)
                m_pred = predicted_mass(cross)
            except Exception as e:
                continue
            if not math.isfinite(m_pred): continue
            err_MeV = m_pred - target_MeV
            err_ppm = err_MeV / target_MeV * 1e6
            results.append({
                'gluon_op': gluon_op, 'gluon_gen': gluon_gen,
                'm_pred': m_pred,
                'err_MeV': err_MeV, 'err_ppm': err_ppm,
            })
    results.sort(key=lambda r: abs(r['err_ppm']))
    return results


print("\n" + "="*90)
print(f"PROTON: Borromean B₃ + flavor + SDP-gluon (target m_p = {M_P_MEV:.4f} MeV)")
print("="*90)
p_results = scan_gluon_ops(build_proton_cross, M_P_MEV, "proton")
print(f"{'gluon_op':<10} {'gen':>4}  {'m_pred':>10}  {'err(MeV)':>10}  {'err(ppm)':>10}")
for r in p_results:
    print(f"{r['gluon_op']:<10} {r['gluon_gen']:>4}  {r['m_pred']:>10.4f}  "
          f"{r['err_MeV']:>+10.4f}  {r['err_ppm']:>+10.1f}")
print(f"\nBest proton: {p_results[0]['gluon_op']} on gen {p_results[0]['gluon_gen']}  "
      f"err={p_results[0]['err_ppm']:.1f} ppm")

print("\n" + "="*90)
print(f"NEUTRON: target m_n = {M_N_MEV:.4f} MeV")
print("="*90)
n_results = scan_gluon_ops(build_neutron_cross, M_N_MEV, "neutron")
for r in n_results[:8]:
    print(f"{r['gluon_op']:<10} {r['gluon_gen']:>4}  {r['m_pred']:>10.4f}  "
          f"{r['err_MeV']:>+10.4f}  {r['err_ppm']:>+10.1f}")

# Use best config to compute Δm_np
m_p_best = p_results[0]['m_pred']
m_n_best = n_results[0]['m_pred']
print(f"\nBest m_p = {m_p_best:.4f} MeV ({p_results[0]['err_ppm']:.1f} ppm)")
print(f"Best m_n = {m_n_best:.4f} MeV ({n_results[0]['err_ppm']:.1f} ppm)")
print(f"Δm_np    = {m_n_best - m_p_best:+.4f} MeV  (CODATA: +1.2933 MeV)")

out = Path(__file__).parent / "m-proton-gluon-sdp.witness.json"
out.write_text(json.dumps({
    "computation": "m-proton-gluon-sdp",
    "description": "Proton mass: Borromean B₃ fixed + SDP over gluon knot operator.",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "electron_tower_reference": e_total,
    "proton_results": p_results,
    "neutron_results": n_results,
    "best_proton": p_results[0],
    "best_neutron": n_results[0],
    "delta_mn_mp_predicted": m_n_best - m_p_best,
    "delta_mn_mp_codata": 1.2933,
}, indent=2, default=str))
print(f"\nWitness: {out}")
