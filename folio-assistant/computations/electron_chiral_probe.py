#!/usr/bin/env python3
"""
Electron chiral-weak-partner probe.

HYPOTHESIS: the m_p/m_e = 1869.85 (CODATA 1836.15, +1.84%) residual is
the electron braid missing its SU(2)_L weak partner.  The Standard
Model lepton is

    L_e = (ν_e, e⁻)_L   +   (e⁻)_R

left-handed doublet + right-handed singlet.  The current one-strand
braid tracks only the charge line.  Adding a neutrino strand coupled
via a left-handed projector P_L (Hecke coefficient c ∈ [0, 1]) should
lift m_e by a coupling-dependent factor.

This probe sweeps c, computes m_e(cat) via the existing Φ_q tower
(same formula as mass_endomorphism.py, extended from 1 to 2 generators),
calibrates against the unmodified proton, and reports m_e(MeV) vs
CODATA 0.511 MeV.

A physically meaningful c should match a known SM coupling ratio:

    sin²θ_W ≈ 0.2312       (weak mixing, Z pole)
    α_em/α_w ≈ 4           (coupling ratio at low energy)
    m_e/m_W ≈ 6×10⁻⁶       (Higgs-Yukawa ratio)

If the c that reproduces 0.511 MeV matches one of these, the model
is physically consistent.  If it doesn't, the 1.8% residual has a
different origin.

POSITRON INTERLUDE.  pair-production-nf.witness.json shows the e⁺
braid σ₀⁻¹σ₁⁻¹σ₀⁻¹ reduces to a NF with NEGATIVE coefficients on the
ν, L₊, L₋ basis directions:

    e⁺ NF = [ν=-0.218, σ₀=+0.044, σ₁=+0.044, L₊=-0.209, L₋=-0.209, e⁻=+1.0]

while e⁻ = σ₀σ₁σ₀ is the pure basis element [0,0,0,0,0,1].  Dropping
the positron sector = dropping the negative-coefficient directions
of the Gram basis.  Gram-matrix-dual's single negative eigenvalue
(-0.741) lives on a combination that includes these.
"""
from __future__ import annotations

import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0
from mass_endomorphism import (additive_wedderburn_volumes, mass_from_tower,
                                  Phi_q, HA, qi0)

# ── Calibration anchors ─────────────────────────────────────

# Proton total (cat units) — same as mass_endomorphism.py proton.total.
# Calibration: E_0 · m_proton(cat) = 938.272 MeV exactly.
_M_PROTON_CAT = 1178995.5254
M_P_MEV = 938.272
M_E_CODATA_MEV = 0.51099895
E_0_PROTON_TOWER_MEV = M_P_MEV / _M_PROTON_CAT

# Current electron (1 generator, σ₀³) — reference baseline.
_electron_cross_current = {0: [(1.0, 0.0)] * 3}
_e_vols_current = additive_wedderburn_volumes(2, _electron_cross_current)
_, _, _, _e_cat_current = mass_from_tower(_e_vols_current)
_m_e_current_MeV = E_0_PROTON_TOWER_MEV * _e_cat_current


# ── Chiral-weak-partner electron braid ──────────────────────

def electron_chiral_braid(c_weak: float, n_factors_nu: int = 3) -> dict:
    """2-generator electron braid with ν_e partner strand coupled via P_L.

    Generator 0: charge strand — σ₀³ (unchanged trefoil).
    Generator 1: ν_e partner strand — (c_weak·σ + 0)^{n_factors_nu},
                  with c_weak ∈ [0, 1] playing the role of P_L's
                  eigenvalue on the left-handed sector.

    Returns the crossings-per-gen dict for additive_wedderburn_volumes.
    """
    return {
        0: [(1.0, 0.0)] * 3,                     # e⁻ charge strand
        1: [(c_weak, 0.0)] * n_factors_nu,       # ν_e partner, P_L suppressed
    }


def m_e_cat_at_c(c_weak: float, n_factors_nu: int = 3) -> float:
    cross = electron_chiral_braid(c_weak, n_factors_nu=n_factors_nu)
    vols = additive_wedderburn_volumes(3, cross)   # 3 strands for 2 gens
    _, _, _, total = mass_from_tower(vols)
    return total


def m_e_MeV_at_c(c_weak: float, n_factors_nu: int = 3) -> float:
    return E_0_PROTON_TOWER_MEV * m_e_cat_at_c(c_weak, n_factors_nu=n_factors_nu)


# ── Positron / negative-coefficient diagnostic ──────────────

def positron_nf_summary() -> dict:
    """Load pair-production-nf.witness.json, extract e⁺ NF and
    highlight the negative-coefficient directions."""
    p = Path(__file__).parent / "pair-production-nf.witness.json"
    if not p.exists():
        return {"status": "missing"}
    w = json.loads(p.read_text())
    eplus = w.get("nf_eplus", {})
    eminus = w.get("nf_eminus", {})
    neg_dirs = {k: v["at_q0"] for k, v in eplus.items()
                 if isinstance(v, dict) and v.get("at_q0", 0) < 0}
    pos_dirs = {k: v["at_q0"] for k, v in eplus.items()
                 if isinstance(v, dict) and v.get("at_q0", 0) >= 0}
    eplus_net = w.get("nf_eplus", {}).get("_net",
                       sum(v.get("at_q0", 0) for v in eplus.values()
                            if isinstance(v, dict)))
    eminus_net = w.get("nf_eminus", {}).get("_net",
                        sum(v.get("at_q0", 0) for v in eminus.values()
                             if isinstance(v, dict)))
    return {
        "eminus_nf_basis":
            {k: v.get("at_q0", 0) for k, v in eminus.items()
              if isinstance(v, dict)},
        "eminus_net": eminus_net,
        "eplus_nf_basis":
            {k: v.get("at_q0", 0) for k, v in eplus.items()
              if isinstance(v, dict)},
        "eplus_net": eplus_net,
        "eplus_negative_directions": neg_dirs,
        "eplus_positive_directions": pos_dirs,
        "asymmetry_net": (eminus_net - eplus_net),
        "comment": (
            "Positron NF has negative coefs on ν, L₊, L₋; electron "
            "NF is pure +1 on e⁻=σ₀σ₁σ₀ basis element.  Dropping "
            "positron tracking = dropping the negative-coefficient "
            "sector of H_3(q)."
        ),
    }


# ── CLI ─────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 100)
    print("ELECTRON CHIRAL-WEAK-PARTNER PROBE")
    print(f"q₀ = {q0:.6f}")
    print(f"proton calibration: E_0 = {E_0_PROTON_TOWER_MEV:.4e} MeV/cat "
          f"(m_p = {M_P_MEV} MeV by construction)")
    print(f"CODATA m_e = {M_E_CODATA_MEV:.6f} MeV")
    print(f"BASELINE (1 gen, no ν partner): m_e = {_m_e_current_MeV:.6f} MeV "
          f"(err {(_m_e_current_MeV - M_E_CODATA_MEV) / M_E_CODATA_MEV * 100:+.4f}%)")
    print("=" * 100)

    # Physically meaningful c values to probe
    C_PROBES = [
        ("zero",                0.0),
        ("m_e/m_W Higgs-Yukawa", 6.2e-6),
        ("alpha_em",             1/137.036),
        ("alpha_em · 100",        0.0729),          # heuristic
        ("sin²θ_W",              0.2312),
        ("sin θ_W",              0.4815),
        ("half",                 0.5),
        ("unit",                 1.0),
    ]

    rows = []
    print(f"\n{'label':>22} {'c_weak':>11} {'m_e_cat':>14} "
          f"{'m_e_MeV':>12} {'err_%':>10}")
    print("  " + "-" * 78)
    for label, c in C_PROBES:
        cat = m_e_cat_at_c(c, n_factors_nu=3)
        mev = E_0_PROTON_TOWER_MEV * cat
        err = (mev - M_E_CODATA_MEV) / M_E_CODATA_MEV * 100
        print(f"  {label:>20} {c:>11.4e} {cat:>14.3f} "
              f"{mev:>12.6f} {err:>+9.4f}%")
        rows.append({"label": label, "c_weak": c,
                      "m_e_cat": cat, "m_e_MeV": mev,
                      "err_pct": err})

    # Fine sweep to find c_star such that m_e(pred) = CODATA
    print(f"\n{'=' * 80}")
    print("BINARY-SEARCH for c_star such that m_e_pred = CODATA 0.511 MeV")
    print("=" * 80)
    lo, hi = 0.0, 2.0
    for _ in range(80):
        mid = (lo + hi) / 2
        m = E_0_PROTON_TOWER_MEV * m_e_cat_at_c(mid)
        if m < M_E_CODATA_MEV:
            lo = mid
        else:
            hi = mid
    c_star = (lo + hi) / 2
    m_star = E_0_PROTON_TOWER_MEV * m_e_cat_at_c(c_star)
    print(f"  c_star = {c_star:.8f}   m_e(c_star) = {m_star:.6f} MeV  "
          f"(CODATA {M_E_CODATA_MEV:.6f})")

    # Compare c_star to known couplings
    print(f"\n  known SM coupling ratios at low energy:")
    print(f"    m_e/m_W           = {M_E_CODATA_MEV/80400:.4e}")
    print(f"    alpha_em          = {1/137.036:.4e}")
    print(f"    alpha_w/alpha_em  = {1/0.23:.4e}")
    print(f"    sin²θ_W           = 2.3120e-01")
    print(f"    sin θ_W           = 4.8083e-01")

    # Positron/negative-coef diagnostic
    print(f"\n{'=' * 80}")
    print("POSITRON NF — NEGATIVE-COEFFICIENT DIAGNOSTIC")
    print("=" * 80)
    pos_info = positron_nf_summary()
    if pos_info.get("status") != "missing":
        print("  e⁻ NF coefficients (q₀ basis):")
        for k, v in pos_info["eminus_nf_basis"].items():
            print(f"    {k:>20}: {v:+.6f}")
        print(f"    net = {pos_info['eminus_net']:+.6f}")
        print("\n  e⁺ NF coefficients (q₀ basis):")
        for k, v in pos_info["eplus_nf_basis"].items():
            mark = "  <-- NEG" if v < 0 else ""
            print(f"    {k:>20}: {v:+.6f}{mark}")
        print(f"    net = {pos_info['eplus_net']:+.6f}")
        print(f"\n  asymmetry (net_e⁻ − net_e⁺) = "
              f"{pos_info['asymmetry_net']:+.6f}")
    else:
        print("  pair-production-nf.witness.json not present; skipping")

    # Write witness
    witness = {
        "computation": "electron-chiral-probe",
        "description": (
            "Sweep P_L coefficient c ∈ [0,1] on ν_e partner strand added "
            "to the electron braid; compute m_e(cat) via Φ_q tower, "
            "calibrate against proton (E_0 = m_p_MeV/m_p_cat).  Binary-"
            "search c_star such that m_e_pred = CODATA 0.511 MeV; compare "
            "c_star to known SM coupling ratios (m_e/m_W, α_em, sin²θ_W).  "
            "Also reports positron NF negative-coefficient directions "
            "from pair-production-nf.witness.json (the sector that was "
            "dropped when electron-only tracking was adopted)."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q0": q0,
            "E_0_proton_tower_MeV": E_0_PROTON_TOWER_MEV,
            "m_e_CODATA_MeV": M_E_CODATA_MEV,
            "baseline_m_e_MeV": _m_e_current_MeV,
            "baseline_err_pct":
                (_m_e_current_MeV - M_E_CODATA_MEV) / M_E_CODATA_MEV * 100,
        },
        "sweep": rows,
        "c_star_fit": {"c": c_star, "m_e_pred_MeV": m_star},
        "positron_nf_diagnostic": pos_info,
    }
    out = Path(__file__).parent / "electron-chiral-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
