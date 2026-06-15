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
                                  Phi_q, HA, qi0, z_mark)

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


# ── Positron-dressing probe ─────────────────────────────────
#
# Hypothesis: physical e⁻ is entangled with a virtual e⁺ sector.  Bare
# electron braid σ₀σ₁σ₀ misses the QED self-energy contribution.  A
# fraction η of the positron's V̂ should dress the electron's V̂ per
# generator:
#
#     V̂_{e,dressed}(i) = V̂_{e,bare}(i) + η · V̂_{e⁺,bare}(i)
#
# where η is the entanglement fraction.  Mass follows through the
# same Φ_q tower on the dressed V̂ vector.
#
# Braid-word encoding (on 3 strands = 2 generators):
#   σ₀⁻¹ = σ₀ − HA·I  ↔ (c=1, d=−HA) factor
#   e⁻  = σ₀σ₁σ₀        3 factors at gens 0, 1, 0
#   e⁺  = σ₀⁻¹σ₁⁻¹σ₀⁻¹  3 factors, each with d=−HA


def electron_bare_2strand_braid() -> dict:
    """e⁻ = σ₀³ on 2 strands — matches mass_endomorphism.py convention."""
    return {0: [(1.0, 0.0)] * 3}


def positron_bare_2strand_braid() -> dict:
    """e⁺ = σ₀⁻³ on 2 strands (Markov-equivalent to σ₀⁻¹σ₁⁻¹σ₀⁻¹ on 3).

    σ⁻¹ = σ − HA·I  from the Hecke relation.
    """
    return {0: [(1.0, -HA)] * 3}


def m_cat_from_braid(cross: dict, n_strands: int = 2) -> tuple:
    vols = additive_wedderburn_volumes(n_strands, cross)
    desc, single, crossT, total = mass_from_tower(vols)
    return vols, desc, single, crossT, total


def m_e_dressed_cat(eta: float) -> tuple:
    """Dressed electron: V̂ per gen = V̂_e + η · V̂_{e⁺}.  Mass via tower.

    Both bare braids on 2 strands = 1 generator (trefoil convention).
    """
    e_vols, *_ = m_cat_from_braid(electron_bare_2strand_braid())
    p_vols, *_ = m_cat_from_braid(positron_bare_2strand_braid())
    dressed_vols = []
    for ve, vp in zip(e_vols, p_vols):
        dressed_vols.append({
            "std":  ve["std"]  + eta * vp["std"],
            "sym":  ve["sym"]  + eta * vp["sym"],
            "alt":  ve["alt"]  + eta * vp["alt"],
            "full": ve["full"] + eta * vp["full"],
        })
    desc, single, crossT, total = mass_from_tower(dressed_vols)
    return dressed_vols, desc, single, crossT, total


def m_e_dressed_MeV(eta: float) -> float:
    *_, total = m_e_dressed_cat(eta)
    return E_0_PROTON_TOWER_MEV * total


# ── Positron-sector projection via Wedderburn alt block ─────
#
# In H_n(q), the σ_i eigenvalues {+q, −q⁻¹} split into Wedderburn
# sym (+q) and alt (−q⁻¹) blocks (plus a std 2×2 block).  The alt
# block is the "mirror" direction — σ⁻¹-aligned, which the positron
# braid σ⁻³ selects.  So "positron sector content" of any braid
# element = fraction of its V̂ carried by the alt block.
#
# additive_wedderburn_volumes already computes per-generator
#   sp = Π(c·q + d)      — sym block
#   ap = Π(−c·q⁻¹ + d)   — alt block  (sign-inverted, the "positron" channel)
#   Vs = z_mark·a + b    — std block (2×2)
#   Vf = w_sym·sp + w_std·Vs + w_alt·ap   — full aggregated V̂


def wedderburn_breakdown(cross: dict, n_strands: int) -> dict:
    """Per-generator {sym, std, alt, full} V̂ + weights for the braid."""
    # Re-import w_ weights from mass_endomorphism
    from mass_endomorphism import w_sym, w_std, w_alt
    vols = additive_wedderburn_volumes(n_strands, cross)
    per_gen = []
    for v in vols:
        per_gen.append({
            "sym":   v["sym"],   "sym_weighted":   w_sym * v["sym"],
            "std":   v["std"],   "std_weighted":   w_std * v["std"],
            "alt":   v["alt"],   "alt_weighted":   w_alt * v["alt"],
            "full":  v["full"],
        })
    # Totals across generators (sum of abs for a magnitude proxy)
    def _agg(key):
        return sum(abs(pg[key]) for pg in per_gen)
    alt_fraction = (_agg("alt_weighted")
                     / max(_agg("sym_weighted") + _agg("std_weighted")
                           + _agg("alt_weighted"), 1e-30))
    return {
        "per_gen": per_gen,
        "weights": {"w_sym": w_sym, "w_std": w_std, "w_alt": w_alt},
        "agg_abs_sym_weighted": _agg("sym_weighted"),
        "agg_abs_std_weighted": _agg("std_weighted"),
        "agg_abs_alt_weighted": _agg("alt_weighted"),
        "alt_fraction_of_V": alt_fraction,
    }


def positron_projected_calibration() -> dict:
    """Split proton V̂ into + (sym+std) and − (alt) sectors, recalibrate."""
    # Proton braid as in mass_endomorphism.py
    proton_cross = {
        0: [(1.0, 0.0)] * 3          # B₃: 3 × σ₀
           + [(1.0, 0.0)]            # uu
           + [(1.0, -HA / 2)]        # ud
           + [(1.0, 0.0)] * 2,       # 2 gluon modes
        1: [(1.0, -HA)] * 3          # B₃: 3 × σ₁⁻¹
           + [(1.0, -HA / 2)],       # ud
    }
    breakdown = wedderburn_breakdown(proton_cross, n_strands=3)

    # Proton full cat mass (= 1,178,995 baseline)
    p_vols = additive_wedderburn_volumes(3, proton_cross)
    _, _, _, full_cat = mass_from_tower(p_vols)

    # Build projected V̂ excluding the alt (positron) sector.
    # V̂_projected per gen = w_sym·sp + w_std·Vs  (drop w_alt·ap)
    from mass_endomorphism import w_sym, w_std, w_alt
    projected_vols = []
    for v in p_vols:
        v_plus = w_sym * v["sym"] + w_std * v["std"]
        projected_vols.append({
            "sym": v["sym"], "std": v["std"], "alt": 0.0,
            "full": v_plus,
        })
    _, _, _, projected_cat = mass_from_tower(projected_vols)

    # Electron under both calibrations
    e_vols, _, _, _, e_cat = m_cat_from_braid(
        electron_bare_2strand_braid())

    E_0_full = M_P_MEV / full_cat         # current (un-projected)
    E_0_proj = M_P_MEV / projected_cat    # new (positron-excluded proton)
    m_e_full = E_0_full * e_cat
    m_e_proj = E_0_proj * e_cat

    return {
        "proton_full_cat":       full_cat,
        "proton_projected_cat":  projected_cat,
        "alt_fraction_of_proton_V":
            breakdown["alt_fraction_of_V"],
        "fractional_shift":
            (full_cat - projected_cat) / full_cat,
        "E_0_full_MeV_per_cat":  E_0_full,
        "E_0_projected_MeV_per_cat": E_0_proj,
        "electron_cat":          e_cat,
        "m_e_full_calibration_MeV":    m_e_full,
        "m_e_projected_calibration_MeV": m_e_proj,
        "m_e_CODATA_MeV":        M_E_CODATA_MEV,
        "err_full_pct":
            (m_e_full - M_E_CODATA_MEV) / M_E_CODATA_MEV * 100,
        "err_projected_pct":
            (m_e_proj - M_E_CODATA_MEV) / M_E_CODATA_MEV * 100,
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

    # Positron-dressing probe: V̂_e_dressed = V̂_e + η · V̂_{e⁺}
    print(f"\n{'=' * 80}")
    print("POSITRON-DRESSING PROBE: m_e(η) = mass(V̂_e + η·V̂_{e⁺})")
    print("=" * 80)
    # First, compute bare e⁻ and e⁺ cat-masses on 3 strands for reference.
    ev, _, _, _, e_cat = m_cat_from_braid(electron_bare_2strand_braid())
    pv, _, _, _, p_cat = m_cat_from_braid(positron_bare_2strand_braid())
    print(f"  bare e⁻ (σ₀³, 2 strands): V̂ = [{ev[0]['full']:.4f}], "
          f"cat = {e_cat:.3f}  ({E_0_PROTON_TOWER_MEV*e_cat:.6f} MeV)")
    print(f"  bare e⁺ (σ₀⁻³, 2 strands): V̂ = [{pv[0]['full']:.4f}], "
          f"cat = {p_cat:.3f}  ({E_0_PROTON_TOWER_MEV*p_cat:.6f} MeV)")

    eta_probes = [
        0.0,
        -1/(137.036*math.pi),    # α/π — QED 1-loop
        -1/(137.036*2*math.pi),  # α/(2π) — Schwinger
        -0.0180,                 # match the 1.80% defect
        -0.04,                   # one-loop-ish
        -1/137.036,              # α
        -0.1,
        -0.5,
        0.007297,                # α (positive, sanity)
        0.5,
    ]
    print(f"\n  {'η':>14} {'m_cat':>12} {'m_MeV':>10} {'err_%':>10} {'comment':>30}")
    comments = ["zero", "−α/π  (QED 1-loop)", "−α/(2π) (Schwinger)",
                 "−0.0180 (err match)", "−4% (self-E scale)",
                 "−α",  "−10%", "−50%",
                 "+α (sanity)", "+50%"]
    dress_rows = []
    for eta, comment in zip(eta_probes, comments):
        mev = m_e_dressed_MeV(eta)
        err = (mev - M_E_CODATA_MEV) / M_E_CODATA_MEV * 100
        print(f"  {eta:>14.6f} {mev/E_0_PROTON_TOWER_MEV:>12.3f} "
              f"{mev:>10.6f} {err:>+9.4f}% {comment:>30}")
        dress_rows.append({"eta": eta, "m_e_MeV": mev,
                             "err_pct": err, "comment": comment})

    # Binary-search η that reproduces CODATA m_e.  m(η) is DECREASING in η
    # (positron's V̂ is negative, so positive η shrinks V̂_e).  Search
    # from negative side: large negative η → high mass, positive η → low mass.
    lo, hi = -2.0, 0.0
    # Verify sign: m(lo) should be > CODATA, m(hi) < CODATA
    m_lo = m_e_dressed_MeV(lo)
    m_hi = m_e_dressed_MeV(hi)
    if m_lo < M_E_CODATA_MEV or m_hi > M_E_CODATA_MEV:
        print(f"  warning: bracketing failed: m({lo})={m_lo:.6f}, "
              f"m({hi})={m_hi:.6f}")
    for _ in range(80):
        mid = (lo + hi) / 2
        m = m_e_dressed_MeV(mid)
        if m > M_E_CODATA_MEV:
            lo = mid
        else:
            hi = mid
    eta_star = (lo + hi) / 2
    m_eta_star = m_e_dressed_MeV(eta_star)
    print(f"\n  η_star = {eta_star:.6f}   m_e(η_star) = "
          f"{m_eta_star:.6f} MeV  (CODATA {M_E_CODATA_MEV:.6f})")
    print(f"  comparison to physical small-parameter scales:")
    print(f"    α_em             = {1/137.036:.6f}")
    print(f"    α_em/(2π)        = {1/(137.036*2*math.pi):.6f}  (QED 1-loop)")
    print(f"    α_em/π           = {1/(137.036*math.pi):.6f}")
    print(f"    1/(2π)           = {1/(2*math.pi):.6f}")
    print(f"    1 − z²           = {1-z_mark**2:.6f}  (Hecke)")
    print(f"    positron net     = 0.451094")

    # Positron-projected calibration: remove proton's alt-block content,
    # rerun electron prediction under the (+)-sector calibration.
    print(f"\n{'=' * 80}")
    print("POSITRON-PROJECTED CALIBRATION")
    print("  = drop proton's alt-block (σ⁻¹ / positron) content before")
    print("    fixing E_0, then apply to the unchanged electron braid.")
    print("=" * 80)
    proj = positron_projected_calibration()
    print(f"  proton full cat mass:           {proj['proton_full_cat']:.3f}")
    print(f"  proton (+)-projected cat mass:  {proj['proton_projected_cat']:.3f}")
    print(f"  alt-block fractional shift:     "
          f"{proj['fractional_shift']*100:+.4f}%")
    print(f"  E_0 (full):       {proj['E_0_full_MeV_per_cat']:.6e} MeV/cat")
    print(f"  E_0 (projected):  {proj['E_0_projected_MeV_per_cat']:.6e} MeV/cat")
    print(f"  electron cat (unchanged):  {proj['electron_cat']:.3f}")
    print(f"  m_e with FULL calibration:       "
          f"{proj['m_e_full_calibration_MeV']:.6f} MeV  "
          f"({proj['err_full_pct']:+.4f}%)")
    print(f"  m_e with PROJECTED calibration:  "
          f"{proj['m_e_projected_calibration_MeV']:.6f} MeV  "
          f"({proj['err_projected_pct']:+.4f}%)")
    print(f"  CODATA m_e:                     "
          f"{proj['m_e_CODATA_MeV']:.6f} MeV")

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
        "positron_dressing": {
            "bare_e_minus_cat":  e_cat,
            "bare_e_plus_cat":   p_cat,
            "sweep": dress_rows,
            "eta_star": eta_star,
            "m_e_at_eta_star_MeV": m_eta_star,
            "reference_scales": {
                "alpha_em":        1/137.036,
                "alpha_em_2pi":    1/(137.036*2*math.pi),
                "one_over_2pi":    1/(2*math.pi),
                "one_minus_z_sq":  1 - z_mark**2,
                "positron_net":    0.451094,
            },
        },
        "positron_projected_calibration": proj,
        "positron_nf_diagnostic": pos_info,
    }
    out = Path(__file__).parent / "electron-chiral-probe.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
