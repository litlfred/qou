#!/usr/bin/env python3
"""
Proton-braid sweep informed by γγ production structure.

The 1.84% m_p/m_e residual is fixed by the Hecke/Φ_q framework's
prediction of the bare categorical ratio m_p(cat)/m_e(cat) = 1870
(CODATA: 1836).  This is independent of any MeV calibration.

HYPOTHESIS: the proton's actual braid word in the framework should be
γγ-corrected.  The pair-production NF (pair-production-nf.witness.json)
shows:

    γγ = σ_0²  reduces to  (q - q⁻¹)·σ_0 + 𝟏

So a γγ loop inserted into a braid is equivalent to adding one σ
factor with coefficient HA = q - q⁻¹ and a parallel identity factor.
This is the *radiative correction* channel: virtual γγ pairs fuse
and reabsorb inside the proton.

We sweep the baseline 11-factor proton by adding γγ-insertions
(HA·σ + I), single-photon insertions (σ), and virtual e⁺e⁻ loops
(σ·σ⁻¹ — pair-creation-annihilation with net identity).  For each
variant, compute m_p(cat), m_p/m_e(cat), and compare to CODATA 1836.15.

Also computes a calibration-independent HADRON SCALE via the γγ
threshold: Δ(pair) = net(e⁻) + net(e⁺) − net(γγ), which at q₀ gives
0.242 in cat units (= 1.006 MeV via the β-decay calibration — very
close to 2m_e = 1.022 MeV, 1.6% off).  This ties the γγ-correction
scale into a calibration-independent constant.
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
                                  Phi_q, HA, qi0, z_mark,
                                  w_sym, w_std, w_alt)

M_P_CODATA_MEV = 938.272
M_E_CODATA_MEV = 0.510999
M_P_OVER_M_E_CODATA = 1836.152

# ── Baseline electron (unchanged) ───────────────────────────
_electron_cross = {0: [(1.0, 0.0)] * 3}
_e_vols = additive_wedderburn_volumes(2, _electron_cross)
_, _, _, _e_cat = mass_from_tower(_e_vols)
ELECTRON_CAT = _e_cat   # 630.5293


# ── γγ Hecke correction ────────────────────────────────────
# σ² = (q-q⁻¹)·σ + 𝟏, so a γγ insertion at gen g is equivalent
# to applying a quadratic factor that reduces to HA·σ + I.  The
# repo's (c, d) convention is c·σ + d·I, so encode as (c=HA, d=1):
#   c·σ + d·I = HA·σ + I   ← matches σ² Hecke reduction exactly.

GAMMA_GAMMA_FACTOR = (HA, 1.0)


# ── Proton braid variants ──────────────────────────────────

def proton_baseline_11factor() -> dict:
    """Current proton: B_3 + uu + ud + gluon."""
    return {
        0: ([(1.0, 0.0)] * 3        # B_3: 3 × σ_0 (color lattice)
            + [(1.0, 0.0)]           # uu pair
            + [(1.0, -HA / 2)]       # ud pair
            + [(1.0, 0.0)] * 2),     # 2 gluon modes
        1: ([(1.0, -HA)] * 3         # B_3: 3 × σ_1⁻¹
            + [(1.0, -HA / 2)]),     # ud pair
    }


def proton_minimal_6factor() -> dict:
    """QCD-minimal: just the 3-quark B_3 backbone."""
    return {
        0: [(1.0, 0.0)] * 3,         # 3 × σ_0
        1: [(1.0, -HA)] * 3,         # 3 × σ_1⁻¹
    }


def proton_no_gluon_9factor() -> dict:
    """Baseline minus gluon self-coupling."""
    b = proton_baseline_11factor()
    # Drop 2 × σ_0 (gluon modes) from gen 0
    b[0] = b[0][:-2]  # 7 - 2 = 5
    # Add them back: baseline has 3(B) + 1(uu) + 1(ud) + 2(gluon) = 7
    # So removing gluon: 3(B) + 1(uu) + 1(ud) = 5.  Total 5+4 = 9.
    return b


def proton_plus_1gg(base: dict) -> dict:
    """Add one γγ correction factor (HA·σ + I) to each generator."""
    out = {g: list(f) + [GAMMA_GAMMA_FACTOR] for g, f in base.items()}
    return out


def proton_plus_2gg(base: dict) -> dict:
    """Add two γγ correction factors to each generator."""
    out = {g: list(f) + [GAMMA_GAMMA_FACTOR] * 2 for g, f in base.items()}
    return out


def proton_plus_pair_loop(base: dict) -> dict:
    """Add σ·σ⁻¹ loop to each generator (virtual e⁺e⁻ pair).

    σ·σ⁻¹ should reduce to identity under Hecke, but the accumulator
    sees it as two separate multiplications — testing numerical
    stability of the pair-loop interpretation.
    """
    out = {g: list(f) + [(1.0, 0.0), (1.0, -HA)] for g, f in base.items()}
    return out


# ── Evaluation helper ──────────────────────────────────────

def evaluate_proton(cross: dict, n_strands: int = 3, label: str = "") -> dict:
    vols = additive_wedderburn_volumes(n_strands, cross)
    desc, single, crossT, total = mass_from_tower(vols)
    ratio = total / ELECTRON_CAT
    err = (ratio - M_P_OVER_M_E_CODATA) / M_P_OVER_M_E_CODATA * 100
    return {
        "label": label,
        "n_strands": n_strands,
        "n_factors": sum(len(f) for f in cross.values()),
        "V_per_gen": [{"full": v["full"]} for v in vols],
        "desc": desc, "single": single, "cross": crossT,
        "cat_mass": total,
        "cat_ratio_to_electron": ratio,
        "err_vs_CODATA_pct": err,
        "E_0_MeV_per_cat": M_P_CODATA_MEV / total if total else float("nan"),
        "m_e_pred_MeV":
            (M_P_CODATA_MEV / total) * ELECTRON_CAT if total else float("nan"),
    }


# ── γγ threshold sanity check ──────────────────────────────

def gamma_gamma_threshold_cat() -> dict:
    """Reproduce the pair-production threshold in cat units.

    From pair-production-nf.witness.json:
      net(e⁻) = 1.0
      net(e⁺) = 0.4511
      net(γγ) = (HA²+1) at q₀ = 1.2091 ?  Actually the NF of σ² is
      HA·σ + I, net = HA·q₀ + 1 at q₀.

    Δ(pair) = net(e⁻) + net(e⁺) − net(γγ)
    """
    net_eminus = 1.0
    net_eplus = 0.4510942344351552   # from witness
    # γγ = σ² NF = HA·σ + I, net at q₀ = HA·q + 1
    # (Markov trace is σ → z = 1/(q^½ + q⁻^½), but the pair-
    # production witness uses net = sum of NF coefficients at q₀.)
    net_gamma2 = HA * q0 + 1.0
    delta_pair = net_eminus + net_eplus - net_gamma2
    return {
        "net_eminus":  net_eminus,
        "net_eplus":   net_eplus,
        "net_gamma2":  net_gamma2,
        "delta_pair":  delta_pair,
        "delta_pair_via_E0_proton_tower_MeV":
            (M_P_CODATA_MEV / 1178995.5254) * delta_pair,
        "two_m_e_MeV": 2 * M_E_CODATA_MEV,
    }


# ── Sweep + main ───────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 100)
    print("PROTON BRAID SWEEP via γγ production-informed insertions")
    print(f"q₀ = {q0:.6f}, HA = {HA:.4f}, z = {z_mark:.4f}")
    print(f"CODATA m_p/m_e = {M_P_OVER_M_E_CODATA:.4f}")
    print(f"electron cat (fixed, σ_0³ on 2 strands) = {ELECTRON_CAT:.4f}")
    print("=" * 100)

    # γγ threshold
    gg = gamma_gamma_threshold_cat()
    print(f"\nγγ pair-production threshold (sanity check):")
    print(f"  net(e⁻)  = {gg['net_eminus']:.6f}")
    print(f"  net(e⁺)  = {gg['net_eplus']:.6f}")
    print(f"  net(γγ)  = {gg['net_gamma2']:.6f}  (= HA·q₀ + 1)")
    print(f"  Δ(pair)  = {gg['delta_pair']:.6f}  (cat)")
    print(f"  Δ via E_0_proton_tower = "
          f"{gg['delta_pair_via_E0_proton_tower_MeV']:.6f} MeV")
    print(f"  2 m_e (CODATA)         = {gg['two_m_e_MeV']:.6f} MeV")
    print(f"  γγ correction factor:   (c={GAMMA_GAMMA_FACTOR[0]:.4f}, "
          f"d={GAMMA_GAMMA_FACTOR[1]:.4f})  = HA·σ + I  "
          f"(Hecke-reduced σ²)")

    # Assemble variants
    base = proton_baseline_11factor()
    minimal = proton_minimal_6factor()
    no_gluon = proton_no_gluon_9factor()

    variants = [
        ("minimal_6",        minimal),
        ("no_gluon_9",       no_gluon),
        ("baseline_11",      base),
        ("base + 1γγ",       proton_plus_1gg(base)),
        ("base + 2γγ",       proton_plus_2gg(base)),
        ("base + pair_loop", proton_plus_pair_loop(base)),
        ("minimal + 1γγ",    proton_plus_1gg(minimal)),
        ("minimal + 2γγ",    proton_plus_2gg(minimal)),
        ("no_gluon + 1γγ",   proton_plus_1gg(no_gluon)),
        ("no_gluon + 2γγ",   proton_plus_2gg(no_gluon)),
    ]

    results = []
    print(f"\n{'=' * 110}")
    print(f"{'variant':>20} {'n_fact':>7} {'V̂₀':>9} {'V̂₁':>9} "
          f"{'cat_mass':>12} {'m_p/m_e':>10} {'err_%':>9} "
          f"{'m_e_MeV':>10}")
    print("-" * 110)
    for label, cross in variants:
        r = evaluate_proton(cross, n_strands=3, label=label)
        V0 = r["V_per_gen"][0]["full"] if r["V_per_gen"] else float("nan")
        V1 = (r["V_per_gen"][1]["full"]
               if len(r["V_per_gen"]) > 1 else float("nan"))
        print(f"  {label:>20} {r['n_factors']:>5} "
              f"{V0:>+9.4f} {V1:>+9.4f} "
              f"{r['cat_mass']:>12.2f} "
              f"{r['cat_ratio_to_electron']:>10.2f} "
              f"{r['err_vs_CODATA_pct']:>+8.3f}% "
              f"{r['m_e_pred_MeV']:>10.6f}")
        results.append(r)

    # Identify best variant
    finite = [r for r in results
               if math.isfinite(r["err_vs_CODATA_pct"])]
    if finite:
        best = min(finite, key=lambda r: abs(r["err_vs_CODATA_pct"]))
        print(f"\nBEST: {best['label']} — err = "
              f"{best['err_vs_CODATA_pct']:+.4f}%, "
              f"m_e_pred = {best['m_e_pred_MeV']:.6f} MeV "
              f"(CODATA {M_E_CODATA_MEV:.6f})")

    witness = {
        "computation": "proton-braid-sweep-gg",
        "description": (
            "Proton braid sweep informed by γγ pair-production structure. "
            "Baseline 11-factor braid is compared to minimal 6-factor "
            "(QCD-backbone only), 9-factor (no gluon), and each of these "
            "with 1 or 2 γγ radiative-correction insertions.  γγ factor "
            "encoded as (c=1, d=HA) from the Hecke reduction σ² = HA·σ+I. "
            "Also tests a σ·σ⁻¹ virtual-pair loop.  Reports m_p/m_e "
            "categorical ratio (calibration-independent) vs CODATA 1836.152."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q0": q0, "HA": HA,
            "w_sym": w_sym, "w_std": w_std, "w_alt": w_alt,
            "electron_cat_fixed": ELECTRON_CAT,
            "CODATA_m_p_over_m_e": M_P_OVER_M_E_CODATA,
            "CODATA_m_e_MeV": M_E_CODATA_MEV,
            "gamma_gamma_factor": list(GAMMA_GAMMA_FACTOR),
        },
        "gamma_gamma_threshold": gg,
        "variants": results,
        "best_variant":
            best["label"] if finite else None,
        "best_err_pct":
            best["err_vs_CODATA_pct"] if finite else None,
    }
    out = Path(__file__).parent / "proton-braid-sweep-gg.witness.json"
    # Sanitize Infinity → null for strict-JSON compatibility (repo
    # tooling uses JSON.parse which rejects bare Infinity).
    import math as _math

    def _sanitize(o):
        if isinstance(o, float):
            if _math.isinf(o) or _math.isnan(o):
                return None
            return o
        if isinstance(o, dict):
            return {k: _sanitize(v) for k, v in o.items()}
        if isinstance(o, list):
            return [_sanitize(v) for v in o]
        return o

    out.write_text(json.dumps(_sanitize(witness), indent=2, default=str,
                                 allow_nan=False))
    print(f"\nWitness: {out}")
