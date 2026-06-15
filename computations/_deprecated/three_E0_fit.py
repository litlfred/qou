#!/usr/bin/env python3
"""
Three-E_0 fit: rep-theory predicts exactly three independent
dimensional scales for H_3(q) observables.

H_3(q) decomposes into three simple blocks by Wedderburn:
  sym  (1-dim, σ → +q)        — Markov / symmetric channel
  std  (2×2, {+q, -q⁻¹} block)— observed particle mass
  alt  (1-dim, σ → -q⁻¹)      — positron / pair channel

Every observable O has a 3-vector of block projections
(a_sym, a_std, a_alt).  By Schur's lemma and rep theory, O_MeV =
a_sym · E_0^sym + a_std · E_0^std + a_alt · E_0^alt with three
universal constants.  Each of the 7+ E_0 values littering the code
is an observable-specific effective scalar, derivable from the 3.

PROBE: fit (E_0^sym, E_0^std, E_0^alt) by linear least squares
against physical observables (CODATA / AME), and report residuals.
If the 3-E_0 model reproduces all observables within AME precision,
it's rep-theory-complete; otherwise the residuals tell us which
block(s) need refinement.

BLOCK PROJECTION CONVENTION.  For a particle/braid given by its
additive Wedderburn per-generator values (sp, Vs, ap), we project:

  a_sym(obs)  =  Σ_i  w_sym · |sp_i|    (sym-eigenvalue product, gen i)
  a_std(obs)  =  Σ_i  w_std · |Vs_i|    (std 2×2 block value, gen i)
  a_alt(obs)  =  Σ_i  w_alt · |ap_i|    (alt-eigenvalue product, gen i)

(Σ_i over generators in the braid word.)  These are the linear
Wedderburn components BEFORE the Φ_q nonlinearity — exactly the
decomposition that rep theory sanctions as independent.
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
from experimental_constants import (M_E_MEV, M_P_MEV, M_N_MEV,
                                       Q_NEUTRON_MEV)
from mass_endomorphism import (additive_wedderburn_volumes, mass_from_tower,
                                  HA, qi0, z_mark,
                                  w_sym, w_std, w_alt)


def wedderburn_block_projection(cross: dict, n_strands: int) -> dict:
    """Return (a_sym, a_std, a_alt) and full Vf for the braid.

    Uses absolute-value sums across generators — the "total
    Wedderburn weight" in each block, without Φ_q.
    """
    vols = additive_wedderburn_volumes(n_strands, cross)
    a_sym = sum(w_sym * abs(v["sym"]) for v in vols)
    a_std = sum(w_std * abs(v["std"]) for v in vols)
    a_alt = sum(w_alt * abs(v["alt"]) for v in vols)
    vf_sum = sum(abs(v["full"]) for v in vols)
    return {"a_sym": a_sym, "a_std": a_std, "a_alt": a_alt,
             "full_abs_sum": vf_sum,
             "n_gens": len(vols)}


# ── Particle / observable definitions ───────────────────────

def particle_braids() -> dict:
    """Braid-word crossings per particle, in additive_wedderburn format."""
    return {
        "electron": {
            "cross": {0: [(1.0, 0.0)] * 3},       # σ₀³ trefoil
            "n_strands": 2,
        },
        "positron": {
            "cross": {0: [(1.0, -HA)] * 3},       # σ₀⁻³ mirror trefoil
            "n_strands": 2,
        },
        "proton": {
            "cross": {
                0: ([(1.0, 0.0)] * 3
                    + [(1.0, 0.0)]
                    + [(1.0, -HA / 2)]
                    + [(1.0, 0.0)] * 2),
                1: [(1.0, -HA)] * 3 + [(1.0, -HA / 2)],
            },
            "n_strands": 3,
        },
        "neutron": {
            "cross": {
                0: ([(1.0, 0.0)] * 3
                    + [(1.0, -HA)]
                    + [(1.0, -HA / 2)]
                    + [(1.0, 0.0)] * 2),
                1: [(1.0, -HA)] * 3 + [(1.0, -HA / 2)],
            },
            "n_strands": 3,
        },
        "gamma_gamma": {
            # γγ = σ² reduces via Hecke to HA·σ + I; repo convention is
            # (c, d) ↔ c·σ + d·I, so encode as (HA, 1.0).
            "cross": {0: [(HA, 1.0)]},
            "n_strands": 2,
        },
    }


# Physical observables in MeV (CODATA / AME).
OBSERVABLES_MEV = {
    # Authoritative source: experimental_constants (CODATA 2022)
    "electron":    M_E_MEV,
    "positron":    M_E_MEV,          # m_e⁺ = m_e⁻ by CPT
    "proton":      M_P_MEV,
    "neutron":     M_N_MEV,
    "gamma_gamma": 1.021998,         # 2 m_e pair threshold
}


def fit_three_E0(observables: dict) -> dict:
    """Linear least-squares: find (E_0^sym, E_0^std, E_0^alt).

    Solves min Σ_o (O_pred - O_MeV)^2 where
        O_pred = a_sym(o)·E₀^sym + a_std(o)·E₀^std + a_alt(o)·E₀^alt
    """
    particles = particle_braids()
    names = [n for n in observables if n in particles]
    A = np.zeros((len(names), 3))
    b = np.zeros(len(names))
    proj_info = {}
    for i, name in enumerate(names):
        proj = wedderburn_block_projection(
            particles[name]["cross"], particles[name]["n_strands"])
        A[i] = [proj["a_sym"], proj["a_std"], proj["a_alt"]]
        b[i] = observables[name]
        proj_info[name] = {
            "a_sym": proj["a_sym"], "a_std": proj["a_std"],
            "a_alt": proj["a_alt"],
            "full_abs_sum": proj["full_abs_sum"],
            "observed_MeV": observables[name],
        }
    # LSQ fit
    E0_vec, resid_sse, rank, sv = np.linalg.lstsq(A, b, rcond=None)
    O_pred = A @ E0_vec
    residuals = O_pred - b
    return {
        "names": names,
        "A_projection_matrix": A.tolist(),
        "b_observed": b.tolist(),
        "E0_sym": float(E0_vec[0]),
        "E0_std": float(E0_vec[1]),
        "E0_alt": float(E0_vec[2]),
        "rank": int(rank),
        "singular_values": sv.tolist() if sv is not None else None,
        "O_pred_MeV": O_pred.tolist(),
        "residuals_MeV": residuals.tolist(),
        "residuals_pct":
            [(r / o * 100 if o else float("nan"))
              for r, o in zip(residuals, b)],
        "sse": float(np.sum(residuals ** 2)),
        "projections": proj_info,
    }


def predict_from_fit(fit: dict, particles: dict,
                        test_names: list) -> dict:
    """Use the fitted three E_0's to predict held-out observables."""
    E0_vec = np.array([fit["E0_sym"], fit["E0_std"], fit["E0_alt"]])
    preds = {}
    for name in test_names:
        if name not in particles:
            preds[name] = {"status": "no_braid"}
            continue
        proj = wedderburn_block_projection(
            particles[name]["cross"], particles[name]["n_strands"])
        a = np.array([proj["a_sym"], proj["a_std"], proj["a_alt"]])
        o_pred = float(a @ E0_vec)
        o_obs = OBSERVABLES_MEV.get(name, float("nan"))
        preds[name] = {
            "a_sym": proj["a_sym"], "a_std": proj["a_std"],
            "a_alt": proj["a_alt"],
            "pred_MeV": o_pred,
            "obs_MeV": o_obs,
            "residual_MeV": o_pred - o_obs if math.isfinite(o_obs) else None,
            "residual_pct":
                ((o_pred - o_obs) / o_obs * 100
                  if math.isfinite(o_obs) and o_obs
                  else None),
        }
    return preds


if __name__ == "__main__":
    print("=" * 100)
    print("THREE-E_0 FIT — rep-theory says H_3(q) admits exactly 3 scales")
    print(f"q₀ = {q0:.6f}, HA = {HA:.4f}")
    print(f"Wedderburn weights: w_sym={w_sym:.4f}, "
          f"w_std={w_std:.4f}, w_alt={w_alt:.4f}")
    print("=" * 100)

    particles = particle_braids()
    # Per-particle Wedderburn block projections
    print(f"\nBlock projections per particle:")
    print(f"  {'particle':>12} {'n_gens':>7} {'a_sym':>10} {'a_std':>10} "
          f"{'a_alt':>10} {'|Σ V̂|':>10} {'obs_MeV':>12}")
    for name in ["electron", "positron", "proton", "neutron", "gamma_gamma"]:
        p = particles[name]
        proj = wedderburn_block_projection(p["cross"], p["n_strands"])
        obs = OBSERVABLES_MEV.get(name, float("nan"))
        print(f"  {name:>12} {proj['n_gens']:>7} "
              f"{proj['a_sym']:>10.4f} {proj['a_std']:>10.4f} "
              f"{proj['a_alt']:>10.4f} "
              f"{proj['full_abs_sum']:>10.4f} {obs:>12.6f}")

    # Fit from ALL 5 observables
    print(f"\n{'=' * 80}")
    print("FULL FIT on 5 observables (e⁻, e⁺, p, n, γγ)")
    print("=" * 80)
    fit = fit_three_E0(OBSERVABLES_MEV)
    print(f"  E_0^sym = {fit['E0_sym']:+.6f} MeV/cat")
    print(f"  E_0^std = {fit['E0_std']:+.6f} MeV/cat")
    print(f"  E_0^alt = {fit['E0_alt']:+.6f} MeV/cat")
    print(f"  SSE = {fit['sse']:.6e}")
    print(f"\n  {'observable':>12} {'a_sym':>10} {'a_std':>10} {'a_alt':>10} "
          f"{'obs_MeV':>12} {'pred_MeV':>12} {'resid':>12} {'%':>8}")
    for i, name in enumerate(fit["names"]):
        o = fit["b_observed"][i]
        p = fit["O_pred_MeV"][i]
        r = fit["residuals_MeV"][i]
        pct = fit["residuals_pct"][i]
        a = fit["A_projection_matrix"][i]
        print(f"  {name:>12} {a[0]:>10.4f} {a[1]:>10.4f} {a[2]:>10.4f} "
              f"{o:>12.6f} {p:>12.6f} {r:>+12.4e} {pct:>+7.3f}%")

    # Train on 3, predict 2 (held-out test)
    print(f"\n{'=' * 80}")
    print("TRAIN on (p, e⁻, Q_β)-like triple, PREDICT e⁺, n, γγ")
    print("=" * 80)
    TRAIN_SET = {
        "electron": OBSERVABLES_MEV["electron"],
        "proton":   OBSERVABLES_MEV["proton"],
        "neutron":  OBSERVABLES_MEV["neutron"],
    }
    fit_train = fit_three_E0(TRAIN_SET)
    print(f"  Fitted E_0's from {{e⁻, p, n}}:")
    print(f"    E_0^sym = {fit_train['E0_sym']:+.6f} MeV/cat")
    print(f"    E_0^std = {fit_train['E0_std']:+.6f} MeV/cat")
    print(f"    E_0^alt = {fit_train['E0_alt']:+.6f} MeV/cat")
    print(f"    (3 obs, 3 unknowns → exact fit, SSE = {fit_train['sse']:.2e})")
    test_names = ["positron", "gamma_gamma"]
    preds = predict_from_fit(fit_train, particles, test_names)
    print(f"\n  Predictions on held-out observables:")
    print(f"  {'obs':>12} {'a_sym':>10} {'a_std':>10} {'a_alt':>10} "
          f"{'obs':>10} {'pred':>10} {'resid%':>10}")
    for name, r in preds.items():
        if r.get("status") == "no_braid":
            print(f"  {name:>12}: no braid defined")
            continue
        print(f"  {name:>12} {r['a_sym']:>10.4f} {r['a_std']:>10.4f} "
              f"{r['a_alt']:>10.4f} "
              f"{r['obs_MeV']:>10.6f} {r['pred_MeV']:>10.6f} "
              f"{r['residual_pct']:>+9.3f}%")

    # Calibration ratios: relate fitted E_0's to the existing code's
    # hardcoded E_0 values.
    print(f"\n{'=' * 80}")
    print("RELATE to existing hardcoded E_0 values")
    print("=" * 80)
    E0_BETA_DECAY = float(Q_NEUTRON_MEV)  # 0.78233341 MeV
    E0_PROTON_TOWER = float(M_P_MEV) / 1178995.5254
    E0_FROM_NET = 4.154925
    print(f"  fitted E_0^sym = {fit['E0_sym']:+.6f} MeV/cat")
    print(f"  fitted E_0^std = {fit['E0_std']:+.6f} MeV/cat")
    print(f"  fitted E_0^alt = {fit['E0_alt']:+.6f} MeV/cat")
    print(f"  hardcoded E_0_BETA_DECAY   = {E0_BETA_DECAY:+.6f}")
    print(f"  hardcoded E_0_PROTON_TOWER = {E0_PROTON_TOWER:+.6e}")
    print(f"  hardcoded E_0_FROM_NET     = {E0_FROM_NET:+.6f}")

    witness = {
        "computation": "three-E0-fit",
        "description": (
            "Rep-theory-sanctioned three-E_0 fit for H_3(q) observables. "
            "Wedderburn decomposes H_3(q) into three simple blocks "
            "(sym, std, alt), so by Schur's lemma exactly three "
            "dimensional scales are free.  Each particle/observable has "
            "a 3-vector of block projections; O_MeV should equal the "
            "inner product with (E_0^sym, E_0^std, E_0^alt).  Probe: "
            "linear LSQ fit over {e⁻, e⁺, p, n, γγ}; held-out train/test "
            "on (p, e⁻, n) → predict e⁺ and γγ threshold.  If residuals "
            "are within AME precision, the 3-E_0 model is complete."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q0": q0, "HA": HA,
            "w_sym": w_sym, "w_std": w_std, "w_alt": w_alt,
            "observables_MeV": OBSERVABLES_MEV,
        },
        "full_fit_5obs": fit,
        "train_3_test_2": {
            "train_set": TRAIN_SET,
            "fit": fit_train,
            "predictions": preds,
        },
        "hardcoded_E0_comparison": {
            "E0_BETA_DECAY":   E0_BETA_DECAY,
            "E0_PROTON_TOWER": E0_PROTON_TOWER,
            "E0_FROM_NET":     E0_FROM_NET,
        },
    }
    out = Path(__file__).parent / "three-E0-fit.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
