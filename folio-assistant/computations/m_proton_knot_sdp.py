#!/usr/bin/env python3
"""
Proton mass via SDP over the knot-operator basis at the quark level.

Uses the confinement_level_sdp infrastructure:
  1. Enumerate all per-quark operator assignments (5^3 = 125 for uud).
  2. SDP picks the tuple minimizing |tr_M_proton| (on-shell ground state).
  3. Compute m_p = (|tr_M_proton| / |tr_M_electron|) × m_e (MeV).

Electron reference = trefoil T_{2,3} on a 3-strand H_3 braid, yielding
the canonical single-vortex Markov trace value.

Dimensional bridge: since both proton and electron go through the same
Plancherel-weighted tr_M construction, their ratio is a pure number
depending only on q₀ and the braid combinatorics — no fitted constant.
"""
import sys, json, math, time
from pathlib import Path
from datetime import datetime, timezone
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from confinement_level_sdp import (
    KNOT_OPERATORS, knot_operator_word, build_level_word,
    tr_M_plancherel, level_sdp, HA
)

U, D = 1, 0


def flavor_crossing(fi: int, fj: int) -> tuple[float, float]:
    """Quark-quark Hecke crossing (c, d) from SU(2) isospin."""
    if fi == U and fj == U: return (1.0, 0.0)        # uu sym
    if fi == D and fj == D: return (1.0, -HA)        # dd antisym
    return (1.0, -HA/2.0)                            # ud mixed


def electron_reference_tr_M(n_strands: int = 3) -> float:
    """|tr_M| of the canonical electron = trefoil T_{2,3}."""
    word = knot_operator_word("T_2_3", base_gen=0)
    return abs(tr_M_plancherel(word, n_strands))


def run_particle_sdp(name: str, flavors: list[int], n_strands: int
                    ) -> dict:
    t0 = time.time()
    optimal, rep = level_sdp(
        n_strands=n_strands, flavors=flavors,
        crossing_fn=flavor_crossing,
        label=f"{name}-quark-level",
        objective="max_abs_trM",
    )
    dt = time.time() - t0

    # Re-compute the actual (signed) tr_M at the optimal tuple
    word_opt = build_level_word(list(optimal), flavors, flavor_crossing)
    trM_signed = tr_M_plancherel(word_opt, n_strands)

    return {
        "name": name,
        "flavors": flavors,
        "n_strands": n_strands,
        "optimal_ops": list(optimal),
        "optimal_abs_trM": rep.optimal_trM,  # |tr_M| under our objective
        "optimal_signed_trM": trM_signed,
        "lp_status": rep.lp_status,
        "n_candidates": rep.n_candidates,
        "compute_seconds": dt,
        "top5": sorted(rep.trM_by_candidate.items(),
                       key=lambda x: x[1])[:5],
    }


print("="*90)
print("PROTON MASS via SDP over knot-operator basis (quark level)")
print(f"q0 = {q0}")
print(f"m_e (CODATA) = {M_E_MEV} MeV")
print(f"m_p (CODATA) = {M_P_MEV} MeV")
print(f"m_n (CODATA) = {M_N_MEV} MeV")
print("="*90)

# Electron reference (common denominator)
e_trM = electron_reference_tr_M(n_strands=3)
print(f"\nElectron reference |tr_M(T_{{2,3}})| at H_3 = {e_trM:.6e}")

# Proton (uud)
print("\n--- Running proton SDP (uud) ---")
p_result = run_particle_sdp("proton", [U, U, D], n_strands=6)
print(f"  Optimal ops : {p_result['optimal_ops']}")
print(f"  |tr_M|       : {p_result['optimal_abs_trM']:.6e}")
print(f"  tr_M (signed): {p_result['optimal_signed_trM']:+.6e}")
print(f"  LP status   : {p_result['lp_status']}")
print(f"  Candidates  : {p_result['n_candidates']}  [{p_result['compute_seconds']:.1f}s]")

# Neutron (udd)
print("\n--- Running neutron SDP (udd) ---")
n_result = run_particle_sdp("neutron", [U, D, D], n_strands=6)
print(f"  Optimal ops : {n_result['optimal_ops']}")
print(f"  |tr_M|       : {n_result['optimal_abs_trM']:.6e}")
print(f"  tr_M (signed): {n_result['optimal_signed_trM']:+.6e}")
print(f"  Candidates  : {n_result['n_candidates']}  [{n_result['compute_seconds']:.1f}s]")

# Dimensional bridge via Φ_q (categorical mass)
def phi_q(v, max_k=500):
    """Φ_q(v) = ∏(1-q^{-k}v)^{-1} for |v|<q."""
    if abs(v) >= q0: return float('inf')
    p = 1.0
    for k in range(1, max_k+1):
        f = 1 - qi0**k * v
        p /= f
        if abs(qi0**k * v) < 1e-15: break
    return p

V_p = p_result['optimal_signed_trM']  # Markov trace = normalized V̂
V_n = n_result['optimal_signed_trM']
V_e = tr_M_plancherel(knot_operator_word("T_2_3", 0), 3)

# Categorical mass m = |Φ_q(V̂)| in m_e units
Phi_p = abs(phi_q(abs(V_p)))
Phi_n = abs(phi_q(abs(V_n)))
Phi_e = abs(phi_q(abs(V_e)))

ratio_p = Phi_p / Phi_e
ratio_n = Phi_n / Phi_e
m_p_pred = ratio_p * M_E_MEV
m_n_pred = ratio_n * M_E_MEV
err_p = (m_p_pred - M_P_MEV) / M_P_MEV * 1e6
err_n = (m_n_pred - M_N_MEV) / M_N_MEV * 1e6

print("\n" + "="*90)
print(f"DIMENSIONAL BRIDGE: m_X = (|Φ_q(tr_M_X)| / |Φ_q(tr_M_e)|) × m_e")
print("="*90)
print(f"\n  tr_M_e = {V_e:+.6e}   Φ_q(|tr_M_e|) = {Phi_e:.6e}")
print(f"  tr_M_p = {V_p:+.6e}   Φ_q(|tr_M_p|) = {Phi_p:.6e}")
print(f"  tr_M_n = {V_n:+.6e}   Φ_q(|tr_M_n|) = {Phi_n:.6e}")
print(f"\n              Φ_X / Φ_e       × m_e    =  m_pred      CODATA      err(ppm)")
print(f"  proton       {ratio_p:.4e}      {M_E_MEV:.4f}     {m_p_pred:+.4f}    {M_P_MEV:.4f}   {err_p:+.1f}")
print(f"  neutron      {ratio_n:.4e}      {M_E_MEV:.4f}     {m_n_pred:+.4f}    {M_N_MEV:.4f}   {err_n:+.1f}")
print(f"\nΔm_np predicted = {m_n_pred - m_p_pred:+.4f} MeV  (CODATA: +1.2933 MeV)")

print(f"\nProton top-5 candidates by tr_M (sorted):")
for name, t in p_result['top5']:
    print(f"  {name:<36} tr_M={t:+.6e}")

out = Path(__file__).parent / "m-proton-knot-sdp.witness.json"
out.write_text(json.dumps({
    "computation": "m-proton-knot-sdp",
    "description": "Proton mass via SDP over knot-operator basis at quark level.",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "q0": q0,
    "electron_reference_trM": e_trM,
    "proton": {**p_result, 'm_predicted_MeV': m_p_pred,
               'm_codata_MeV': M_P_MEV, 'err_ppm': err_p},
    "neutron": {**n_result, 'm_predicted_MeV': m_n_pred,
                'm_codata_MeV': M_N_MEV, 'err_ppm': err_n},
}, indent=2, default=str))
print(f"\nWitness: {out}")
