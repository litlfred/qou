#!/usr/bin/env python3
"""
Per-block Φ_q mass formula + three-E_0 calibration.

The rep-theory-correct refactor: apply Φ_q PER WEDDERBURN BLOCK rather
than once on the Plancherel-aggregated V̂.  This preserves the three-
block independence (sym/std/alt) and admits exactly three independent
dimensional scales (E_0^sym, E_0^std, E_0^alt) — matching Schur's
lemma for H_3(q).

OLD (mass_endomorphism.py, mass_from_tower):
    V̂_i = w_sym·sp_i + w_std·Vs_i + w_alt·ap_i   (aggregate first)
    m = |Π V̂| + Σ_i Φ_q(|V̂_i|) + z² Σ Φ_q(|V̂_i V̂_j|)
    m_MeV = E_0_global · m

NEW (this module, mass_per_block):
    Per block b ∈ {sym, std, alt}:
      m^b = |Π V̂^b| + Σ_i Φ_q(|V̂^b_i|) + z² Σ Φ_q(|V̂^b_i V̂^b_j|)
      (Φ_q applied per block's per-gen values, not on the aggregate)
    m_MeV = Σ_b E_0^b · m^b

where V̂^sym_i = sp_i, V̂^std_i = Vs_i, V̂^alt_i = ap_i — the per-gen
block-diagonal values already computed in additive_wedderburn_volumes.

PROBE: fit (E_0^sym, E_0^std, E_0^alt) from {e⁻, p, n} via linear
least-squares, predict {e⁺, γγ threshold}, compare to CODATA.  If
the per-block model fits all 5 observables within AME precision (say
<0.1%), the refactor is rep-theory-complete.
"""
from __future__ import annotations

import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0
from mass_endomorphism import (additive_wedderburn_volumes,
                                  Phi_q, HA, qi0, z_mark,
                                  w_sym, w_std, w_alt)
from experimental_constants import (M_E_MEV, M_P_MEV, M_N_MEV,
                                       Q_NEUTRON_MEV)


def _phi_safe(v, cap_frac=0.995):
    """Φ_q(|v|) with soft cap to avoid saturation."""
    a = abs(v)
    if a >= q0 * cap_frac:
        return Phi_q(q0 * cap_frac)
    return Phi_q(a)


def mass_per_block(cross: dict, n_strands: int) -> dict:
    """Per-block tower mass: {sym, std, alt, total_block_agg}.

    Each block's mass has the same structure as mass_from_tower
    (descended × |Π V̂| + Σ Φ_q singleton + z² Σ Φ_q pair), but using
    that block's per-gen V̂ values directly.
    """
    vols = additive_wedderburn_volumes(n_strands, cross)
    blocks = {
        "sym": [v["sym"] for v in vols],
        "std": [v["std"] for v in vols],
        "alt": [v["alt"] for v in vols],
    }
    result = {}
    for bname, V in blocks.items():
        n = len(V)
        desc = 1.0
        for v in V:
            desc *= v
        desc = abs(desc)
        single = sum(_phi_safe(v) for v in V)
        cross_t = 0.0
        for i in range(n - 1):
            cross_t += z_mark ** 2 * _phi_safe(V[i] * V[i + 1])
        result[bname] = {
            "V_per_gen": V,
            "desc": desc, "single": single, "cross": cross_t,
            "block_mass": desc + single + cross_t,
        }
    result["sum_blocks"] = (result["sym"]["block_mass"]
                              + result["std"]["block_mass"]
                              + result["alt"]["block_mass"])
    return result


def particle_braids() -> dict:
    """Braid-word crossings per particle."""
    return {
        "electron": {"cross": {0: [(1.0, 0.0)] * 3}, "n_strands": 2},
        "positron": {"cross": {0: [(1.0, -HA)] * 3}, "n_strands": 2},
        "proton": {
            "cross": {
                0: ([(1.0, 0.0)] * 3 + [(1.0, 0.0)]
                    + [(1.0, -HA / 2)] + [(1.0, 0.0)] * 2),
                1: [(1.0, -HA)] * 3 + [(1.0, -HA / 2)],
            },
            "n_strands": 3,
        },
        "neutron": {
            "cross": {
                0: ([(1.0, 0.0)] * 3 + [(1.0, -HA)]
                    + [(1.0, -HA / 2)] + [(1.0, 0.0)] * 2),
                1: [(1.0, -HA)] * 3 + [(1.0, -HA / 2)],
            },
            "n_strands": 3,
        },
        "gamma_gamma": {
            # (c, d) = c·σ + d·I; γγ = σ² → HA·σ + I, so use (HA, 1.0)
            "cross": {0: [(HA, 1.0)]},
            "n_strands": 2,
        },
    }


OBSERVABLES_MEV = {
    # Authoritative source: experimental_constants (CODATA 2022)
    "electron":    M_E_MEV,
    "positron":    M_E_MEV,
    "proton":      M_P_MEV,
    "neutron":     M_N_MEV,
    "gamma_gamma": 1.021998,
}


def fit_three_E0(observables: dict) -> dict:
    """Linear LSQ: O_MeV = E_0^sym·m^sym + E_0^std·m^std + E_0^alt·m^alt."""
    particles = particle_braids()
    names = [n for n in observables if n in particles]
    A = np.zeros((len(names), 3))
    b = np.zeros(len(names))
    proj = {}
    for i, name in enumerate(names):
        p = particles[name]
        blocks = mass_per_block(p["cross"], p["n_strands"])
        A[i] = [blocks["sym"]["block_mass"],
                 blocks["std"]["block_mass"],
                 blocks["alt"]["block_mass"]]
        b[i] = observables[name]
        proj[name] = {
            "m_sym": blocks["sym"]["block_mass"],
            "m_std": blocks["std"]["block_mass"],
            "m_alt": blocks["alt"]["block_mass"],
            "obs_MeV": observables[name],
        }
    E0_vec, _, rank, sv = np.linalg.lstsq(A, b, rcond=None)
    pred = A @ E0_vec
    resid = pred - b
    return {
        "names": names,
        "A": A.tolist(),
        "b": b.tolist(),
        "E0_sym": float(E0_vec[0]),
        "E0_std": float(E0_vec[1]),
        "E0_alt": float(E0_vec[2]),
        "rank": int(rank),
        "sv": sv.tolist() if sv is not None else None,
        "pred_MeV": pred.tolist(),
        "resid_MeV": resid.tolist(),
        "resid_pct": [
            (r / o * 100 if o else float("nan"))
            for r, o in zip(resid, b)
        ],
        "sse": float(np.sum(resid ** 2)),
        "per_particle": proj,
    }


def predict_from_fit(fit: dict, test_names: list) -> dict:
    """Predict held-out observables using fitted E_0's."""
    particles = particle_braids()
    E0 = np.array([fit["E0_sym"], fit["E0_std"], fit["E0_alt"]])
    preds = {}
    for name in test_names:
        if name not in particles:
            preds[name] = {"status": "no_braid"}
            continue
        p = particles[name]
        blocks = mass_per_block(p["cross"], p["n_strands"])
        a = np.array([blocks["sym"]["block_mass"],
                       blocks["std"]["block_mass"],
                       blocks["alt"]["block_mass"]])
        pred = float(a @ E0)
        obs = OBSERVABLES_MEV.get(name, float("nan"))
        preds[name] = {
            "m_sym": blocks["sym"]["block_mass"],
            "m_std": blocks["std"]["block_mass"],
            "m_alt": blocks["alt"]["block_mass"],
            "pred_MeV": pred, "obs_MeV": obs,
            "resid_MeV": pred - obs if math.isfinite(obs) else None,
            "resid_pct":
                ((pred - obs) / obs * 100
                 if math.isfinite(obs) and obs else None),
        }
    return preds


if __name__ == "__main__":
    print("=" * 100)
    print("PER-BLOCK Φ_q + THREE-E_0 FIT")
    print(f"q₀ = {q0:.6f}, HA = {HA:.4f}, z = {z_mark:.4f}")
    print("=" * 100)

    particles = particle_braids()

    # Per-particle per-block masses
    print(f"\n{'=' * 90}")
    print("PER-BLOCK Φ_q MASSES (cat units)")
    print("=" * 90)
    print(f"  {'particle':>12} {'m_sym':>14} {'m_std':>14} "
          f"{'m_alt':>14} {'m_sum':>14} {'obs_MeV':>12}")
    for name in ["electron", "positron", "proton", "neutron", "gamma_gamma"]:
        p = particles[name]
        blocks = mass_per_block(p["cross"], p["n_strands"])
        obs = OBSERVABLES_MEV[name]
        print(f"  {name:>12} "
              f"{blocks['sym']['block_mass']:>14.4f} "
              f"{blocks['std']['block_mass']:>14.4f} "
              f"{blocks['alt']['block_mass']:>14.4f} "
              f"{blocks['sum_blocks']:>14.4f} "
              f"{obs:>12.6f}")

    # Full fit on all 5
    print(f"\n{'=' * 90}")
    print("FULL FIT on 5 observables")
    print("=" * 90)
    fit = fit_three_E0(OBSERVABLES_MEV)
    print(f"  E_0^sym = {fit['E0_sym']:+.6e} MeV/cat")
    print(f"  E_0^std = {fit['E0_std']:+.6e} MeV/cat")
    print(f"  E_0^alt = {fit['E0_alt']:+.6e} MeV/cat")
    print(f"  SSE = {fit['sse']:.4e}, "
          f"singular values = {[f'{v:.2e}' for v in fit['sv']]}")
    print(f"\n  {'observable':>12} {'obs_MeV':>12} {'pred_MeV':>12} "
          f"{'resid':>12} {'%':>8}")
    for i, name in enumerate(fit["names"]):
        print(f"  {name:>12} {fit['b'][i]:>12.6f} "
              f"{fit['pred_MeV'][i]:>12.6f} "
              f"{fit['resid_MeV'][i]:>+12.4e} "
              f"{fit['resid_pct'][i]:>+7.3f}%")

    # Held-out train/test
    print(f"\n{'=' * 90}")
    print("TRAIN on {e⁻, p, n}, PREDICT {e⁺, γγ}")
    print("=" * 90)
    TRAIN = {
        "electron": OBSERVABLES_MEV["electron"],
        "proton":   OBSERVABLES_MEV["proton"],
        "neutron":  OBSERVABLES_MEV["neutron"],
    }
    fit_tr = fit_three_E0(TRAIN)
    print(f"  E_0^sym = {fit_tr['E0_sym']:+.6e} MeV/cat")
    print(f"  E_0^std = {fit_tr['E0_std']:+.6e} MeV/cat")
    print(f"  E_0^alt = {fit_tr['E0_alt']:+.6e} MeV/cat")
    print(f"  train SSE = {fit_tr['sse']:.4e}  (3 eq, 3 unk → exact)")
    preds = predict_from_fit(fit_tr, ["positron", "gamma_gamma"])
    print(f"\n  {'obs':>12} {'m_sym':>12} {'m_std':>12} {'m_alt':>12} "
          f"{'obs':>10} {'pred':>10} {'resid%':>10}")
    for name, r in preds.items():
        if r.get("status") == "no_braid":
            continue
        print(f"  {name:>12} {r['m_sym']:>12.4f} {r['m_std']:>12.4f} "
              f"{r['m_alt']:>12.4f} "
              f"{r['obs_MeV']:>10.6f} {r['pred_MeV']:>10.6f} "
              f"{r['resid_pct']:>+9.3f}%")

    # Compare fitted E_0^block vs existing hardcoded scales
    print(f"\n{'=' * 90}")
    print("COMPARISON to existing hardcoded E_0 values")
    print("=" * 90)
    E0_BETA_DECAY = float(Q_NEUTRON_MEV)  # 0.78233341 MeV (CODATA-derived)
    E0_PROTON_TOWER = float(M_P_MEV) / 1178995.5254
    E0_FROM_NET = 4.154925
    print(f"  fitted E_0^sym  = {fit['E0_sym']:+.6e}  "
          f"(Markov-trace / β-decay-like)")
    print(f"  fitted E_0^std  = {fit['E0_std']:+.6e}  "
          f"(observed-mass / bulk)")
    print(f"  fitted E_0^alt  = {fit['E0_alt']:+.6e}  "
          f"(positron / pair channel)")
    print(f"  hardcoded β-decay      = {E0_BETA_DECAY:+.6e}")
    print(f"  hardcoded proton-tower = {E0_PROTON_TOWER:+.6e}")
    print(f"  hardcoded from-net     = {E0_FROM_NET:+.6e}")

    witness = {
        "computation": "per-block-phi-q",
        "description": (
            "Per-block Φ_q mass formula: apply Φ_q to each Wedderburn "
            "block (sym/std/alt) per generator, then sum blockwise "
            "with three independent E_0 scales.  This preserves the "
            "rep-theory three-block structure.  Linear LSQ fit of "
            "(E_0^sym, E_0^std, E_0^alt) against CODATA observables "
            "{m_e⁻, m_e⁺, m_p, m_n, 2m_e (γγ)}.  Held-out test on "
            "e⁺ and γγ after fitting on {e⁻, p, n}.  If residuals "
            "stay within AME (~0.1%), the per-block model is rep-"
            "theory-complete."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q0": q0, "HA": HA,
            "w_sym": w_sym, "w_std": w_std, "w_alt": w_alt,
            "observables_MeV": OBSERVABLES_MEV,
        },
        "full_fit": fit,
        "train_test": {"fit": fit_tr, "predictions": preds},
        "hardcoded_comparison": {
            "E0_BETA_DECAY": E0_BETA_DECAY,
            "E0_PROTON_TOWER": E0_PROTON_TOWER,
            "E0_FROM_NET": E0_FROM_NET,
        },
    }
    out = Path(__file__).parent / "per-block-phi-q.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
