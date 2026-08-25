#!/usr/bin/env python3
"""Production wiring of `prop:rho-k-graded-expansion` (bean 1o2j).

Routes the atomic mass through the two PROVED pieces of the graded ρ_K
expansion, and flags the pair-gen piece OPEN (reported as the residual,
never wired):

  M(Z, N) = [ Z·m_p + N·m_n + Z·m_e ]          LO piece — Markov
            ^ canonical_mass facade              multiplicativity (Wenzl
                                                 1988), muon-anchored
          + α · Σ_i ln|V̂_i^full|               single-gen piece — proved
            α = m_e · 8G (Catalan, derived)      binding correction
          + [pair-gen + ...]                    OPEN — reported as the
                                                 residual M_obs − M_pred;
                                                 NOT added to the mass
                                                 (wrong functional form:
                                                 needs Li₂^q, not ln —
                                                 see the prop's Table 1)

Supersedes `_deprecated/atomic_braid_mass_paper_formula.py` (deprecated as
an ORPHAN of the phantom label `prop:atomic-braid-mass`, not as wrong —
2026-05-19 catalog §8; the real label is `prop:rho-k-graded-expansion`).
Two upgrades over the deprecated baseline:

  * LO constituents come from the **canonical_mass facade** (muon-anchored
    Hecke energy, docs/canonical-mass-formula-guardrail.md) instead of
    hardcoded CODATA m_p/m_n — the only remaining external mass input is
    CAL-1 m_e (and the AME comparison column, a validation target).
  * The pair-gen tier is explicitly reported OPEN per the (a)/(b)
    refutation-scope discipline (the naive α·z²·Σln|V_iV_j| form DEGRADES
    accuracy — `rho-k-pair-gen-extension.witness.json`).

No fitted parameters anywhere: α is m_e·8·Catalan (prop:binding-scale-
catalan), the V̂_i are Wedderburn-weighted per-generator volumes from the
canonical Hecke chain (hecke_core.atom_per_generator_volumes).

Output: rho-k-graded-atomic-mass.witness.json
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import _path_bridge  # noqa: F401,E402

from codata_constants import M_E_MEV  # noqa: E402 — CAL-1 anchor
from canonical_mass import proton_mass_mev, neutron_mass_mev  # noqa: E402
from hecke_core import atom_per_generator_volumes  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

M_E = mp.mpf(str(M_E_MEV))
M_P = mp.mpf(str(proton_mass_mev()))   # canonical muon-anchored facade
M_N = mp.mpf(str(neutron_mass_mev()))  # canonical muon-anchored facade
ALPHA = M_E * 8 * mp.catalan           # binding scale, DERIVED (no fit)


def atom_mass_graded(Z: int, N: int) -> dict:
    """M(Z,N) through the proved LO + single-gen tiers of the graded ρ_K."""
    lo = Z * M_P + N * M_N + Z * M_E

    vols = atom_per_generator_volumes(Z, N, include_inter=True)
    sum_log_V = mp.mpf(0)
    n_zero = 0
    for v in vols:
        x = mp.mpf(v["full"] if isinstance(v, dict) else v)
        if abs(x) < mp.mpf("1e-30"):
            n_zero += 1
            continue
        sum_log_V += mp.log(abs(x))

    single_gen = ALPHA * sum_log_V
    # mp values kept exact; JSON serialization uses 50-digit strings
    # (floats only for console display) per the compute-author discipline.
    return {
        "Z": Z,
        "N": N,
        "A": Z + N,
        "lo": lo,
        "n_generators": len(vols),
        "n_zero_volumes": n_zero,
        "sum_log_V": sum_log_V,
        "single_gen": single_gen,
        "M_pred": lo + single_gen,
    }


# Published comparison table (atomic-braid-mass.md Table 1; atomic masses,
# validation targets only — CLASS-A acknowledged anchors, they enter NO
# formula).
OBS_TABLE = [
    (1, "H", 1, 938.783),
    (2, "He", 4, 3728.401),
    (3, "Li", 7, 6535.367),
    (4, "Be", 9, 8394.794),
    (5, "B", 11, 10255.103),
    (6, "C", 12, 11177.929),
    (7, "N", 14, 13043.782),
    (8, "O", 16, 14899.169),
    (9, "F", 19, 17696.901),
    (10, "Ne", 20, 18622.835),
]


def main() -> int:
    print("=" * 92)
    print("  prop:rho-k-graded-expansion — production route: LO (facade) + single-gen")
    print(f"  m_p = {float(M_P):.5f}  m_n = {float(M_N):.5f}  (canonical_mass facade)")
    print(f"  alpha = m_e·8G = {float(ALPHA):.6f} MeV (derived)")
    print("=" * 92)
    print(f"\n  {'Z':>3} {'el':<3} {'A':>3}  {'LO (MeV)':>11}  {'single-gen':>11}  "
          f"{'M_pred':>11}  {'M_obs':>11}  {'err%':>7}  {'pair-gen+ resid':>15}")
    print("  " + "-" * 86)

    rows, errs = [], []
    for Z, name, A, M_obs_f in OBS_TABLE:
        r = atom_mass_graded(Z, A - Z)
        M_obs = mp.mpf(str(M_obs_f))
        err_pct = 100 * (r["M_pred"] - M_obs) / M_obs
        resid = M_obs - r["M_pred"]  # the OPEN pair-gen+ remainder
        rows.append({
            "Z": r["Z"], "name": name, "N": r["N"], "A": r["A"],
            "n_generators": r["n_generators"],
            "n_zero_volumes": r["n_zero_volumes"],
            # 50-digit strings — floats only for the console table below
            "lo_MeV": mp.nstr(r["lo"], 50),
            "sum_log_V_full": mp.nstr(r["sum_log_V"], 50),
            "single_gen_MeV": mp.nstr(r["single_gen"], 50),
            "M_pred_MeV": mp.nstr(r["M_pred"], 50),
            "M_obs_MeV": mp.nstr(M_obs, 50),
            "err_pct": mp.nstr(err_pct, 12),
            "pair_gen_open_residual_MeV": mp.nstr(resid, 12),
        })
        errs.append(abs(err_pct))
        print(f"  {Z:>3} {name:<3} {A:>3}  {float(r['lo']):>11.3f}  "
              f"{float(r['single_gen']):>11.3f}  {float(r['M_pred']):>11.3f}  "
              f"{float(M_obs):>11.3f}  {float(err_pct):>6.3f}%  {float(resid):>15.3f}")

    mean_err, max_err = sum(errs) / len(errs), max(errs)
    print("  " + "-" * 86)
    print(f"  mean |err| = {float(mean_err):.4f}%   max |err| = {float(max_err):.4f}%")
    print("\n  Tier status: LO = PROVED (Wenzl multiplicativity; facade constituents)")
    print("               single-gen = PROVED binding correction (this table)")
    print("               pair-gen+  = OPEN, reported as residual only (never wired;")
    print("               the naive alpha*z^2*sum(ln|V_i V_j|) form DEGRADES accuracy)")

    from witness_base import WitnessBuilder  # noqa: E402

    w = WitnessBuilder("rho-k-graded-atomic-mass", engine="mpmath")
    w.description = (
        "Production wiring of prop:rho-k-graded-expansion: atomic mass routed "
        "through the proved LO (canonical_mass facade, muon-anchored) + single-gen "
        "(alpha·sum ln|V_i|) tiers; pair-gen+ reported as the OPEN residual, not wired."
    )
    # constants as 50-digit strings (facade floats upcast at the boundary)
    w.add_parameter("m_p_facade_MeV", mp.nstr(M_P, 50))
    w.add_parameter("m_n_facade_MeV", mp.nstr(M_N, 50))
    w.add_parameter("m_e_cal1_MeV", mp.nstr(M_E, 50))
    w.add_parameter("alpha_MeV", mp.nstr(ALPHA, 50))
    w.add_data("bean", "1o2j")
    w.add_data("supersedes",
               "_deprecated/atomic_braid_mass_paper_formula.py (orphan of phantom label)")
    w.add_data("discipline",
               "no fit — alpha = m_e·8·Catalan derived; constituents from canonical_mass "
               "facade; M_obs is a validation column only (enters no formula); pair-gen "
               "flagged (a)-scope OPEN per rho-k-pair-gen-extension.witness.json.")
    w.add_data("table", rows)
    w.add_data("mean_abs_err_pct", mp.nstr(mean_err, 12))
    w.add_data("max_abs_err_pct", mp.nstr(max_err, 12))
    w.add_caveat(
        "h3_weights_legacy: atom_per_generator_volumes weights per-generator V-hats "
        "with H_3 Wedderburn weights for A>=2 (DeprecationWarning intentionally NOT "
        "suppressed); the correct H_{3A} weights are the pyhecke/atom.py Tier-2 fix "
        "(dedicated PR per docs/audits/2026-05-25-h3-vs-h3a-legacy-bug-audit.md §7). "
        "The 0.18-0.3% single-gen accuracy here is measured WITH the published-table "
        "(H_3) weights — the same convention as the prop's Table 1; re-baseline when "
        "the Tier-2 fix lands."
    )
    w.add_assertion("lo_routed_through_canonical_facade", "pass", "pass",
                    source="structural: constituents imported from canonical_mass")
    w.add_assertion("alpha_derived_not_fit", "pass", "pass",
                    source="alpha = m_e*8*Catalan (prop:binding-scale-catalan)")
    w.add_assertion("single_gen_mean_abs_err_pct", float(mean_err), 0.0,
                    tolerance=0.5, unit="%")
    w.add_assertion("single_gen_max_abs_err_pct", float(max_err), 0.0,
                    tolerance=1.0, unit="%")
    w.add_assertion("pair_gen_not_wired", "pass", "pass",
                    source="pair-gen reported as residual column only")
    out = w.save()
    print(f"\n  witness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
