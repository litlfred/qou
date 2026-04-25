#!/usr/bin/env python3
"""
V-hat-within-level Candidate #1: JM cells under production calibration.

Runs the unified_lift.binding_unified pipeline (canonical Ocneanu
trace + β-decay E_0 + ℏ_q^{2n} brane scaling) but replaces the
scalar per-generator V̂_i baseline with the SYT-cell JM volumes
V̂_k^{JM} from syt_cell_tower.  Kähler order 0 only (higher
orders diverge on T/3He per session finding; JM cells are numeric
at q₀ anyway — symbolic q-derivative of partition sums is hard).

Comparison axes:

  • scalar-under-production: unified_lift.binding_unified
    (β-decay E_0, Kähler order 0, scalar V̂_i)
  • JM-under-production: this module
    (β-decay E_0, no Kähler, V̂_k^{JM} per cell)
  • JM-under-probe: syt_cell_tower
    (proton-calibrated E_0, no Kähler, V̂_k^{JM} per cell)

Tests whether the JM form — known to be empirically much stronger
than scalar under probe calibration on T/3He (0.28 / 0.22 % vs
18 / 60 %) — also holds up under the production calibration, or
over-corrects like the content-weighted pair did.
"""
from __future__ import annotations

import sys
import json
import math
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0
from canonical_plus_multibrane import (HBAR_Q_SQ, E_0_BETA_DECAY_MEV,
                                          z_mark, phi_q_safe,
                                          lift_V_markov)
from ocneanu_weights import tr_M_via_ocneanu_word
from syt_cell_tower import V_hat_JM_all, tower_mass_JM


def binding_jm_under_production(Z: int, N: int, *,
                                   E_0: float = E_0_BETA_DECAY_MEV,
                                   target_ppm: float = 1.0,
                                   jet_cap: int = 60,
                                   sdp_gluon: bool = False) -> dict:
    """Production pipeline with JM-cell V̂ baseline (Kähler order 0).

    At Kähler order 0, V_level_1 = z · V̂^(0).  For JM cells the raw
    `V_hat_JM_all` output already carries the Markov-trace weight
    (Σ_λ w_λ · (1/d_λ) · Σ_T q^{2 c_T(k)} · ⟨T|W^λ|T⟩), but it does
    NOT carry the external z factor applied by the scalar
    unified_lift.  We multiply by z once for level-1 parity.
    """
    A = Z + N
    n = 3 * A

    # Canonical (unchanged from scalar production)
    t0 = time.time()
    tr_atom = tr_M_via_ocneanu_word(Z, N, include_inter=True)
    tr_free = tr_M_via_ocneanu_word(Z, N, include_inter=False)
    canonical_MeV = E_0 * (abs(tr_free) - abs(tr_atom))
    canon_dt = time.time() - t0

    # JM cell volumes at q₀ (numeric; no Kähler q-derivatives)
    t0 = time.time()
    V_a_JM = V_hat_JM_all(Z, N, include_inter=True,
                              sdp_gluon=sdp_gluon)
    V_f_JM = V_hat_JM_all(Z, N, include_inter=False,
                              sdp_gluon=sdp_gluon)
    jm_dt = time.time() - t0

    # Level-1 baseline: V_level_1 = z · V_JM (parity with
    # unified_lift's V_markov = z · V̂^(0)).
    V_a_1 = [z_mark * v for v in V_a_JM]
    V_f_1 = [z_mark * v for v in V_f_JM]

    # Multi-level jet loop with ℏ_q^{2n} brane scaling.
    n_mev = n * 938.272
    target_term_cat = (target_ppm * 1e-6 * n_mev) / max(E_0, 1e-12)
    tower_term_cat = 0.0
    delta_1 = None
    jet_log = []
    k = 0
    V_a_k = list(V_a_1)
    V_f_k = list(V_f_1)
    while k < jet_cap:
        k += 1
        if k > 1:
            V_a_k = lift_V_markov(V_a_1, k - 1)
            V_f_k = lift_V_markov(V_f_1, k - 1)
        m_a_k, _ = tower_mass_JM(V_a_k)
        m_f_k, _ = tower_mass_JM(V_f_k)
        delta_k = m_f_k - m_a_k
        if delta_1 is None:
            delta_1 = delta_k
        term_cat = (HBAR_Q_SQ ** k) * delta_k
        tower_term_cat += term_cat
        jet_log.append({"level": k, "delta": delta_k,
                          "term_cat": term_cat,
                          "cumulative_cat": tower_term_cat})
        if abs(term_cat) < target_term_cat:
            break
    tower_MeV = E_0 * tower_term_cat

    return {
        "Z": Z, "N": N, "A": A, "n_cells": n,
        "E_0_MeV": E_0, "sdp_gluon": sdp_gluon,
        "tr_M_atom_abs": abs(tr_atom),
        "tr_M_free_abs": abs(tr_free),
        "canonical_MeV": canonical_MeV,
        "tower_delta_1_cat": delta_1,
        "tower_MeV": tower_MeV,
        "B_MeV": canonical_MeV + tower_MeV,
        "jet_levels_used": k,
        "jet_log": jet_log,
        "V_a_JM": V_a_JM,
        "V_f_JM": V_f_JM,
        "canonical_time_sec": canon_dt,
        "jm_time_sec": jm_dt,
    }


if __name__ == "__main__":
    ATOMS = [
        ("D",    1, 1,  2.22452),
        ("T",    1, 2,  8.481821),
        ("3He",  2, 1,  7.71804),
    ]

    print("=" * 110)
    print("CANDIDATE #1: JM CELLS UNDER PRODUCTION CALIBRATION")
    print(f"q0 = {Q0}, ℏ_q^2 = {HBAR_Q_SQ:.6f}, "
          f"E_0 = {E_0_BETA_DECAY_MEV} MeV")
    print("=" * 110)

    # Scalar-under-production reference (for comparison).
    from unified_lift import binding_unified
    scalar_ref = {}
    print(f"\n{'─' * 80}\nSCALAR production reference  (unified_lift, Kähler 0)"
          f"\n{'─' * 80}")
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        t0 = time.time()
        r = binding_unified(Z, N, pair_mode="full", kahler_order=0)
        dt = time.time() - t0
        err = abs(r["B_MeV"] - B_AME) / (A * 938.272) * 100
        scalar_ref[name] = {"B": r["B_MeV"], "err": err, "t": dt,
                              "canonical": r["canonical_MeV"],
                              "tower": r["tower_MeV"]}
        print(f"  {name:>5}  B_AME={B_AME:>8.3f}  B_pred={r['B_MeV']:>+10.4f}  "
              f"canon={r['canonical_MeV']:>+8.4f}  tower={r['tower_MeV']:>+8.4f}  "
              f"err={err:.4f}%  ({dt:.1f}s)")

    # JM-under-production
    print(f"\n{'─' * 80}\nJM CELLS under production  (new)"
          f"\n{'─' * 80}")
    print(f"  {'Atom':>5}  {'B_AME':>8}  {'B_scalar':>10}  {'B_JM':>10}  "
          f"{'err_s%':>8}  {'err_JM%':>8}  {'Δerr%':>9}  {'t(JM)':>7}")
    print("  " + "-" * 92)
    results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        t0 = time.time()
        try:
            r = binding_jm_under_production(Z, N)
            dt = time.time() - t0
            err_JM = abs(r["B_MeV"] - B_AME) / (A * 938.272) * 100
            ref = scalar_ref[name]
            d_err = err_JM - ref["err"]
            print(f"  {name:>5}  {B_AME:>8.3f}  "
                  f"{ref['B']:>+10.4f}  {r['B_MeV']:>+10.4f}  "
                  f"{ref['err']:>7.4f}% {err_JM:>7.4f}%  "
                  f"{d_err:>+8.4f}%  {dt:>5.1f}s")
            results.append({
                **r, "atom": name, "B_AME_MeV": B_AME,
                "err_pct": err_JM, "err_scalar_ref_pct": ref["err"],
                "delta_err_pct": d_err, "time_sec": dt,
            })
        except Exception as e:
            print(f"  {name:>5}  ERR: {type(e).__name__}: {str(e)[:70]}")

    print("\n" + "=" * 110)
    print("VERDICT")
    print("=" * 110)
    for r in results:
        verdict = ("✓ JM BEATS scalar" if r["delta_err_pct"] < -1e-4
                    else "— JM tied"     if abs(r["delta_err_pct"]) < 1e-4
                    else "✗ JM WORSE than scalar")
        print(f"  {r['atom']:>5}: scalar={r['err_scalar_ref_pct']:.4f}%  "
              f"JM={r['err_pct']:.4f}%  Δ={r['delta_err_pct']:+.4f}%  "
              f"{verdict}")

    witness = {
        "computation": "binding-full-jm-cells",
        "description": (
            "V-hat-within-level Candidate #1: production pipeline "
            "(Ocneanu canonical trace + β-decay E_0 + ℏ_q^{2n} brane "
            "scaling) with JM-cell V̂_k baseline instead of scalar "
            "per-generator V̂_i.  No Kähler q-derivative (order 0; "
            "higher orders would require symbolic JM which is "
            "expensive, and diverge on T/3He anyway).  Tests whether "
            "the JM form's empirical strength under probe calibration "
            "(D/T/3He = 0.10/0.28/0.22 %) survives production, or "
            "over-corrects like content-weighted pair did."),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": Q0, "hbar_q_sq": HBAR_Q_SQ,
                         "E_0_MeV": E_0_BETA_DECAY_MEV},
        "scalar_reference": scalar_ref,
        "results": results,
    }
    out = Path(__file__).parent / "binding-full-jm-cells.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
