"""bring_color_weighted_base_scale_probe.py — PROBE.

Extends `bring_color_weighted` from per-interface p-n averaging
(closed_form_tau_M.py:178) to the BASE mass scale via the new
`bring_color_weighted_linking_weight(Z, N, q)` in _li_2_q_util.py.

Measures the shift on m_p, m_n, m_avg, D, ⁴He vs Family A
(H_4 Wedderburn average, current production default).

Run: `python3 -u bring_color_weighted_base_scale_probe.py`
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 1 catch-up, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import mpmath as mp  # noqa: E402

from _li_2_q_util import (  # noqa: E402
    bring_color_weighted_linking_weight,
    per_knot_density_borromean,
    per_knot_density_borromean_bring_color_weighted,
    linking_weight_family_a,
    flavor_split_leading,
)
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_MP as Q_CANONICAL  # noqa: E402
from codata_constants import M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402

set_compute_dps()

q = mp.mpf(str(Q_CANONICAL))
m_e = mp.mpf("0.51099895000")  # CAL-1 anchor (MeV)

# CODATA targets (codata_constants registry)
m_p_codata = mp.mpf(M_P_MEV_VALIDATION)
m_n_codata = mp.mpf(M_N_MEV_VALIDATION)
m_avg_codata = (m_p_codata + m_n_codata) / 2

print(f"=== bring_color_weighted base-scale probe at q_0 = {mp.nstr(q, 12)} ===\n")

delta = flavor_split_leading(q)
base = linking_weight_family_a(q)
print(f"δ = flavor_split_leading(q_0) = {mp.nstr(delta, 12)}")
print(f"linking_weight_family_a (H_4 avg) = {mp.nstr(base, 12)}")
print()

# Per-atom Bring linking_weights
print("Per-atom linking_weights:")
for (Z, N, label) in [(1, 0, "proton"), (0, 1, "neutron"),
                       (1, 1, "deuteron"), (2, 2, "⁴He")]:
    lw_bring = bring_color_weighted_linking_weight(Z, N, q)
    shift_ppm = (lw_bring / base - 1) * mp.mpf("1e6")
    print(f"  {label:8s} (Z={Z}, N={N}): {mp.nstr(lw_bring, 12)}  "
          f"shift = {mp.nstr(shift_ppm, 4)} ppm")
print()

# Mass predictions (using per_knot_density_borromean directly for m_p, m_n)
m_p_family_a = m_e * per_knot_density_borromean(q)  # H_4 average (production)
m_p_bring = m_e * per_knot_density_borromean_bring_color_weighted(1, 0, q)
m_n_bring = m_e * per_knot_density_borromean_bring_color_weighted(0, 1, q)
m_avg_family_a = m_p_family_a
m_avg_bring = (m_p_bring + m_n_bring) / 2

print("Mass predictions (MeV):")
print(f"  m_p   Family A: {mp.nstr(m_p_family_a, 10)}  CODATA: {m_p_codata}")
print(f"  m_p   Bring   : {mp.nstr(m_p_bring, 10)}")
print(f"  m_n   Bring   : {mp.nstr(m_n_bring, 10)}  CODATA: {m_n_codata}")
print(f"  m_avg Family A: {mp.nstr(m_avg_family_a, 10)}  CODATA: {mp.nstr(m_avg_codata, 10)}")
print(f"  m_avg Bring   : {mp.nstr(m_avg_bring, 10)}")
print()

err_avg_family_a = (m_avg_family_a / m_avg_codata - 1) * mp.mpf("100")
err_avg_bring = (m_avg_bring / m_avg_codata - 1) * mp.mpf("100")
print(f"  m_avg err Family A: {mp.nstr(err_avg_family_a, 4)} %")
print(f"  m_avg err Bring   : {mp.nstr(err_avg_bring, 4)} %")
print(f"  Δ(Family A → Bring) on m_avg: "
      f"{mp.nstr((m_avg_bring/m_avg_family_a - 1) * mp.mpf('1e9'), 4)} ppb")
print()

# Verdict
shift_avg_ppb = (m_avg_bring / m_avg_family_a - 1) * mp.mpf("1e9")
gap_ppm = mp.mpf("28900")  # the +2.89% gap
print(f"VERDICT: Bring m_avg shift = {mp.nstr(shift_avg_ppb, 4)} ppb")
print(f"         Required to close +2.89%: {mp.nstr(gap_ppm, 4)} ppm = "
      f"{mp.nstr(gap_ppm * 1000, 4)} ppb")
ratio = gap_ppm * 1000 / abs(shift_avg_ppb) if shift_avg_ppb != 0 else mp.inf
print(f"         Required/Actual ratio: ~{mp.nstr(ratio, 4)}×")
print(f"         → Bring-color-tube at H_4 is STRUCTURALLY INSUFFICIENT for m_avg")
print(f"         (confirms `lambda-scale-absorbed-into-vol-density.md`)")
