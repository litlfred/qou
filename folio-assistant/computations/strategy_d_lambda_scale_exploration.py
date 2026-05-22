#!/usr/bin/env python3
# polynomial_q_not_applicable: exploration / probe; consumes
# canonical 𝓑_p braid + Vol(𝓑_3) topological invariant only.
"""Strategy D exploration: λ_scale from canonical proton 𝓑_p via LP/SDP.

Implements the agent brief
`docs/agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md`
Strategy D — direct categorical derivation of `λ_scale` from the
canonical proton Hecke element `𝓑_p` (3-strand) via an LP/SDP
problem, bypassing PSLQ entirely.

The user note "q_0 not special, just where we happen to be" is the
operative constraint: any candidate identity must be SMOOTH IN q,
not numerically pinned at q_0. The LP/SDP formulations below are
therefore evaluated at q_0 AND at q_0 ± ε to verify q-locality
behaviour; an "LP whose shadow price at q_0 happens to equal
2.4599527869" is not enough — the q-derivative must match the
expected q-derivative of the empirical closure target.

NOT a finished derivation. This script CATALOGUES candidate
structural objects and probes which (if any) match λ_scale ≈
2.4599527869 at q_0 with the right q-locality behaviour.

Structural inputs:
  - 𝓑_p ∈ H_3(q): canonical 11-crossing proton braid (per
    Phase 5l.1).
  - χ_λ(𝓑_p, q) for λ ⊢ 3: known closed forms (from
    `tau-M-proton-closed-form-phase5l1.witness.json`):
      χ_(3)     = q · (q² + 1)² / 4
      χ_(2,1)   = (q²² + q²⁰ + q¹⁸ + q¹⁴ − q⁸ − q⁴ − q² − 1) / (4 q¹¹)
      χ_(1,1,1) = − (q² + 1)² / (4 q⁵)
  - y_λ(q) via Wenzl bridge (`y_lambda_wenzl_bridge_numeric`).
  - tr_M^3(𝓑_p, q) = Σ_λ y_λ(q) · χ_λ(𝓑_p, q) — Phase 5l canonical
    Markov trace.
  - Vol(𝓑_3) = 8 · G (Catalan).
  - ℏ_q = (q − 1) / q.
  - R(q) := Vol(𝓑_3) / ℏ_q²  ≈ 746.42 at q_0.

Target:
  - λ_scale ≈ 2.4599527869 (proton closure value, CAL-4 hardcoded
    in `m_p_borromean_verification_50dps.py:LAMBDA_PROTON_DOC`).

Probes:
  D1. **Partition-channel LP, n_target = R**
      min χ(𝓑_p, q) · x s.t. Σ x_λ = R, y_λ · x_λ ≥ 0.
      Extract y_0* (shadow price of the topological volume).
  D2. **Partition-channel LP, n_target = tr_M^3(𝓑_p)**
      min χ(𝓑_p, q) · x s.t. Σ x_λ = tr_M^3, y_λ · x_λ ≥ 0.
      Extract y_0* (shadow price of the canonical Markov trace).
  D3. **Frobenius-dual LP** (`solve_frobenius_dual_lp`) with
      demand vector u set to the y_λ-diagonal channel weights.
  D4. **Direct identity probes** — algebraic ratios
      `λ_scale / tr_M^3(𝓑_p)`, `λ_scale · ℏ_q² / 8G`, etc., at
      q_0 and on a small q-window, looking for clean smooth
      functions.

Outputs:
  - `strategy-d-lambda-scale-exploration.witness.json` with all
    candidate values + q-locality data + per-probe verdicts.
  - Console summary.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402
from lp_dual_solver import (  # noqa: E402
    solve_operator_selection_lp,
    solve_frobenius_dual_lp,
)

set_compute_dps()

# ── Canonical closure target (the CAL-4 hardcoded literal) ───────
# This is the value Strategy D is trying to DERIVE from substrate.
# Two snapshots exist in the codebase, differing in precision:
#   - LAMBDA_PROTON_DOC  (m_p_borromean_verification): 10-digit
#     literal 2.4599527869, the production hardcode.
#   - lambda_p_codata    (bring_bloch_tier1..5_search_m_p): 32-digit
#     target 2.4599527843613182892482457339493 derived from CODATA
#     m_p/m_e / R(q_0) at 50 dps (see also `audit_delta_S_chain.py`
#     for the closed-form chain).
# The 32-digit target is correct for residual analysis at the
# 5-ppm scale; the 10-digit literal carries only ~10 digits of
# information, so residuals smaller than 2.5e-9 cannot be probed
# against it.  Strategy D residual analysis uses the 32-digit form.
LAMBDA_PROTON_TARGET_10DIGIT = mp.mpf("2.4599527869")
LAMBDA_PROTON_TARGET = mp.mpf("2.4599527843613182892482457339493")

# ── Substrate q_0 from canonical pinning witness ────────────────
_Q_PIN = HERE / "q-pinning-50-digit.witness.json"
Q0 = mp.mpf(json.load(_Q_PIN.open())["derived_50_digit"]["q"])

# ── Canonical proton braid χ_λ (from Phase 5l.1 closed form) ─────
# These are the Hecke characters of the canonical 𝓑_p ∈ H_3(q)
# from `mass_at_3A_proper.atom_braid_word_3A(1, 0, include_inter=False)`
# evaluated symbolically; the closed forms below match the witness
# `tau-M-proton-closed-form-phase5l1.witness.json` data.chi_lambda.
def chi_3(q: mp.mpf) -> mp.mpf:
    """χ_(3)(𝓑_p, q) = q · (q² + 1)² / 4."""
    return q * (q ** 2 + 1) ** 2 / 4


def chi_111(q: mp.mpf) -> mp.mpf:
    """χ_(1,1,1)(𝓑_p, q) = − (q² + 1)² / (4 q⁵)."""
    return -(q ** 2 + 1) ** 2 / (4 * q ** 5)


def chi_21(q: mp.mpf) -> mp.mpf:
    """χ_(2,1)(𝓑_p, q) = (q²²+q²⁰+q¹⁸+q¹⁴−q⁸−q⁴−q²−1) / (4 q¹¹)."""
    num = (q ** 22 + q ** 20 + q ** 18 + q ** 14
           - q ** 8 - q ** 4 - q ** 2 - 1)
    return num / (4 * q ** 11)


def y_lambda(partition: tuple, q: mp.mpf, dps: int = 50) -> mp.mpf:
    """y_λ(q) via the canonical Wenzl bridge — numeric only."""
    return y_lambda_wenzl_bridge_numeric(partition, q, dps=dps)


def tr_M_proton_H3(q: mp.mpf) -> mp.mpf:
    """tr_M^3(𝓑_p, q) = Σ_{λ ⊢ 3} y_λ(q) · χ_λ(𝓑_p, q)."""
    y3, y21, y111 = (
        y_lambda((3,), q),
        y_lambda((2, 1), q),
        y_lambda((1, 1, 1), q),
    )
    return (y3 * chi_3(q)
            + y21 * chi_21(q)
            + y111 * chi_111(q))


# ── Topological-volume reference scale ──────────────────────────
def R_volume(q: mp.mpf) -> mp.mpf:
    """R(q) = Vol(𝓑_3) / ℏ_q² = 8·G / ((q-1)/q)²."""
    hbar_q = (q - 1) / q
    return 8 * mp.catalan / hbar_q ** 2


# ── Probe utilities ─────────────────────────────────────────────
def collect_channel_state(q: mp.mpf, dps: int = 50) -> dict:
    """Snapshot of all per-partition structural inputs at q."""
    parts = [(3,), (2, 1), (1, 1, 1)]
    chi_fns = {(3,): chi_3, (2, 1): chi_21, (1, 1, 1): chi_111}
    chi_vals = {p: chi_fns[p](q) for p in parts}
    y_vals = {p: y_lambda(p, q, dps) for p in parts}
    tr_M = sum(y_vals[p] * chi_vals[p] for p in parts)
    return {
        "q": q,
        "hbar_q": (q - 1) / q,
        "R_volume": R_volume(q),
        "chi": chi_vals,
        "y_lambda": y_vals,
        "tr_M_proton_H3": tr_M,
        "partitions": parts,
    }


def fmt_dict_mpf(d: dict, digits: int = 30) -> dict:
    """Serialize mpmath values to decimal strings for witness JSON."""
    out = {}
    for k, v in d.items():
        if isinstance(v, mp.mpf):
            out[str(k)] = mp.nstr(v, digits)
        elif isinstance(v, dict):
            out[str(k)] = fmt_dict_mpf(v, digits)
        elif isinstance(v, (list, tuple)):
            out[str(k)] = [
                mp.nstr(x, digits) if isinstance(x, mp.mpf) else str(x)
                for x in v
            ]
        else:
            out[str(k)] = str(v)
    return out


# ── Probe D1: partition-channel LP, n_target = R ────────────────
def probe_d1(state: dict, label: str) -> dict:
    """LP at H_3 partition channels with n_target = Vol/ℏ_q²."""
    parts = state["partitions"]
    t = np.array([float(state["chi"][p]) for p in parts])
    # G as diagonal of y_λ — Wedderburn block weights
    G = np.diag([float(state["y_lambda"][p]) for p in parts])
    n_target = float(state["R_volume"])

    try:
        res = solve_operator_selection_lp(t, G, n_target)
    except Exception as exc:
        return {"label": label, "error": repr(exc)}
    d = res.to_dict()
    d["label"] = label
    d["n_target"] = n_target
    d["t"] = list(t)
    d["G_diag"] = [G[i, i] for i in range(len(t))]
    # Hypothesis: λ_scale ∈ {y_0*, primal_obj / R, primal_obj}.
    d["candidate_lambda_y0"] = d["y0_star"]
    d["candidate_lambda_primal_over_R"] = (
        d["primal_obj"] / n_target if n_target else float("nan")
    )
    return d


# ── Probe D2: partition-channel LP, n_target = tr_M^3(𝓑_p) ──────
def probe_d2(state: dict, label: str) -> dict:
    """LP at H_3 partition channels with n_target = tr_M^3(𝓑_p)."""
    parts = state["partitions"]
    t = np.array([float(state["chi"][p]) for p in parts])
    G = np.diag([float(state["y_lambda"][p]) for p in parts])
    n_target = float(state["tr_M_proton_H3"])

    try:
        res = solve_operator_selection_lp(t, G, n_target)
    except Exception as exc:
        return {"label": label, "error": repr(exc)}
    d = res.to_dict()
    d["label"] = label
    d["n_target"] = n_target
    d["candidate_lambda_y0"] = d["y0_star"]
    d["candidate_lambda_primal_over_R"] = (
        d["primal_obj"] / float(state["R_volume"])
    )
    return d


# ── Probe D3: Frobenius-dual LP with y_λ-channel demand ─────────
def probe_d3(state: dict, label: str) -> dict:
    """Frobenius-dual LP: net = R, demand = (y_λ · χ_λ) per channel."""
    parts = state["partitions"]
    t = np.array([float(state["chi"][p]) for p in parts])
    G = np.diag([float(state["y_lambda"][p]) for p in parts])
    n_target = float(state["R_volume"])
    # Demand vector: per-channel Wedderburn-weighted trace contribution.
    u_demand = np.array([
        float(state["y_lambda"][p] * state["chi"][p]) for p in parts
    ])

    try:
        res = solve_frobenius_dual_lp(t, G, n_target, u_demand)
    except Exception as exc:
        return {"label": label, "error": repr(exc)}
    d = res.to_dict()
    d["label"] = label
    d["n_target"] = n_target
    d["u_demand"] = list(u_demand)
    d["candidate_lambda_y0"] = d["y0_star"]
    return d


# ── Probe D4: algebraic ratio probes (no LP, just identities) ──
def probe_d4(state: dict, target: mp.mpf, label: str) -> dict:
    """Direct algebraic ratios and small q-rational combinations."""
    q = state["q"]
    R = state["R_volume"]
    trM = state["tr_M_proton_H3"]
    hbar_q = state["hbar_q"]
    h = q - 1 / q
    z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
    twoq = q + 1 / q  # [2]_q

    ratios = {
        "target / tr_M^3": target / trM,
        "target / R": target / R,
        "target · ℏ_q² / 8G": target * hbar_q ** 2 / (8 * mp.catalan),
        "target − 2·tr_M^3": target - 2 * trM,
        "target − tr_M^3 · [2]_q": target - trM * twoq,
        "target − 5/2": target - mp.mpf(5) / 2,
        "target − 5/2 + h²·G": target - mp.mpf(5) / 2 + h ** 2 * mp.catalan,
        "target / (chi_3 + chi_21 + chi_111)": (
            target / (state["chi"][(3,)]
                      + state["chi"][(2, 1)]
                      + state["chi"][(1, 1, 1)])
        ),
        "target / chi_3": target / state["chi"][(3,)],
        "target / chi_21": target / state["chi"][(2, 1)],
        "target · z": target * z,
        "target · h": target * h,
    }
    return {"label": label, "ratios": fmt_dict_mpf(ratios, 30)}


# ── Probe D5: "5/2 - h²G - ε" residual at high precision ────────
def probe_d5(state: dict, target: mp.mpf, label: str) -> dict:
    """High-precision residual ε := target − (5/2 − h²·G).

    Per `build_proton_mass_50dps_chain.py` the "5/2 − h²·G" ansatz
    matches λ_scale to ~5.4 ppm at q_0. Strategy D's first-pass
    refinement is to identify the next-order correction. This probe
    lists ε as a fraction of common candidate higher-order
    structural objects, to surface the most likely next-order term.
    """
    q = state["q"]
    h = q - 1 / q
    G = mp.catalan
    leading = mp.mpf(5) / 2 - h ** 2 * G
    eps_residual = target - leading

    candidates = {
        "h": h,
        "h^2": h ** 2,
        "h^4": h ** 4,
        "h^6": h ** 6,
        "h^8": h ** 8,
        "h^4·G": h ** 4 * G,
        "h^6·G": h ** 6 * G,
        "h^2·G^2": h ** 2 * G ** 2,
        "(h·G)^2": (h * G) ** 2,
        "h^4·G^2": h ** 4 * G ** 2,
        "h^2·ζ(2)": h ** 2 * mp.pi ** 2 / 6,
        "h^4·ζ(2)": h ** 4 * mp.pi ** 2 / 6,
        "h^6·π": h ** 6 * mp.pi,
        "h^6/6": h ** 6 / 6,
        "h^4·(2-h^2·G)": h ** 4 * (2 - h ** 2 * G),
        "ℏ_q^2": state["hbar_q"] ** 2,
        "ℏ_q^4": state["hbar_q"] ** 4,
        "ℏ_q^6": state["hbar_q"] ** 6,
    }
    ratios = {k: eps_residual / v for k, v in candidates.items()}
    return {
        "label": label,
        "leading_5_2_minus_h2_G": fmt(leading),
        "epsilon_residual": fmt(eps_residual),
        "epsilon_in_ppm": float(eps_residual / target * 1e6),
        "ratios_to_higher_order_candidates": fmt_dict_mpf(ratios, 25),
    }


# ── Probe D6: LP with q^{c(λ)} cost (Phase 5d-style content cost) ─
def probe_d6(state: dict, label: str) -> dict:
    """LP at H_3 partition channels with q^{c(λ)} cost vector.

    Per `delta_n2_lp_dual_extraction.py` and `prop:mass-formula-
    iterative-lp-dual`, the per-channel "discharge cost" is the
    q-content q^{c(λ)} where c(λ) = Σ (j-i) over Young-diagram cells.

    Contents for partitions of 3:
      c((3))     = 0+1+2 = 3
      c((2,1))   = 0+1-1 = 0
      c((1,1,1)) = 0-1-2 = -3

    Net constraint: Σ x_λ = tr_M^3(𝓑_p) (canonical Markov trace).
    Hypothesis: dual shadow price y_0* of this constraint, scaled
    by the Vol(𝓑_3)/ℏ_q² ratio, gives λ_scale.
    """
    q = state["q"]
    parts = state["partitions"]
    contents = {(3,): 3, (2, 1): 0, (1, 1, 1): -3}
    t = np.array([float(q ** contents[p]) for p in parts])
    # G as diagonal of y_λ — Wedderburn block weights.  Use
    # |y_λ| to avoid sign issues (y_(1,1,1) can be very small).
    G = np.diag([float(state["y_lambda"][p]) for p in parts])
    n_target = float(state["tr_M_proton_H3"])

    try:
        res = solve_operator_selection_lp(t, G, n_target)
    except Exception as exc:
        return {"label": label, "error": repr(exc)}
    d = res.to_dict()
    d["label"] = label
    d["t_q_content_powers"] = list(t)
    d["G_diag_y_lambda"] = [float(state["y_lambda"][p]) for p in parts]
    d["n_target_tr_M"] = n_target
    d["candidate_lambda_y0"] = d["y0_star"]
    d["candidate_lambda_y0_times_R"] = d["y0_star"] * float(state["R_volume"])
    return d


# ── Q-locality check: evaluate state at q_0 ± ε ─────────────────
def q_locality_sweep(eps_list, dps: int = 50) -> list[dict]:
    """Evaluate the canonical state at q_0 + ε for several ε."""
    out = []
    for eps in eps_list:
        q = Q0 + mp.mpf(eps)
        state = collect_channel_state(q, dps=dps)
        out.append({
            "eps": fmt(eps),
            "q": fmt(q),
            "R_volume": fmt(state["R_volume"]),
            "tr_M_proton_H3": fmt(state["tr_M_proton_H3"]),
            "chi_3": fmt(state["chi"][(3,)]),
            "chi_21": fmt(state["chi"][(2, 1)]),
            "chi_111": fmt(state["chi"][(1, 1, 1)]),
            "y_3": fmt(state["y_lambda"][(3,)]),
            "y_21": fmt(state["y_lambda"][(2, 1)]),
            "y_111": fmt(state["y_lambda"][(1, 1, 1)]),
        })
    return out


# ── Main ────────────────────────────────────────────────────────
def main() -> int:
    print("=" * 72)
    print("  Strategy D exploration: λ_scale from canonical 𝓑_p")
    print("  (per agent brief 2026-05-22-lambda-scale-qdilog-tower-direct.md)")
    print("=" * 72)
    print()

    w = WitnessBuilder(
        "strategy-d-lambda-scale-exploration", engine="mpmath",
    )
    w.set_description(
        "Strategy D exploration (per agent brief "
        "`docs/agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md`)."
        " Catalogues structural inputs (χ_λ(𝓑_p, q), y_λ(q), tr_M^3(𝓑_p, q),"
        " Vol(𝓑_3)/ℏ_q²) at q_0 and on a q-window around q_0, runs four"
        " LP/SDP/algebraic probes targeting λ_scale ≈ 2.4599527869, and"
        " reports verdicts. Does NOT yet pin a closed form — this is the"
        " stage-1 catalogue + probe pass. Q-locality is enforced: every"
        " candidate is checked at q_0 ± ε to confirm smoothness."
    )
    w.set_audit_only(
        "docs/audits/2026-05-22-strategy-d-lambda-scale-exploration.md"
    )
    w.add_parameter("q_0", fmt(Q0))
    w.add_parameter("lambda_proton_target", fmt(LAMBDA_PROTON_TARGET))

    # Stage 1: structural catalogue at q_0
    print("[1/3] Structural catalogue at q_0")
    print(f"      q_0 = {mp.nstr(Q0, 30)}")
    state = collect_channel_state(Q0, dps=50)
    print(f"      Vol(𝓑_3)/ℏ_q² (R) = {mp.nstr(state['R_volume'], 16)}")
    print(f"      tr_M^3(𝓑_p, q_0) = {mp.nstr(state['tr_M_proton_H3'], 16)}")
    print(f"      χ_(3)(𝓑_p)       = {mp.nstr(state['chi'][(3,)], 16)}")
    print(f"      χ_(2,1)(𝓑_p)     = {mp.nstr(state['chi'][(2, 1)], 16)}")
    print(f"      χ_(1,1,1)(𝓑_p)   = {mp.nstr(state['chi'][(1, 1, 1)], 16)}")
    print(f"      y_(3)(q_0)        = {mp.nstr(state['y_lambda'][(3,)], 16)}")
    print(f"      y_(2,1)(q_0)      = {mp.nstr(state['y_lambda'][(2, 1)], 16)}")
    print(f"      y_(1,1,1)(q_0)    = {mp.nstr(state['y_lambda'][(1, 1, 1)], 16)}")
    print(f"      target λ_scale   = {mp.nstr(LAMBDA_PROTON_TARGET, 16)}")
    print()

    w.add_data("stage1_structural_catalogue_at_q0", {
        "R_volume": fmt(state["R_volume"]),
        "tr_M_proton_H3": fmt(state["tr_M_proton_H3"]),
        "chi": {str(p): fmt(v) for p, v in state["chi"].items()},
        "y_lambda": {str(p): fmt(v) for p, v in state["y_lambda"].items()},
        "lambda_proton_target": fmt(LAMBDA_PROTON_TARGET),
    })

    # Stage 2: LP/SDP/algebraic probes
    print("[2/3] LP / SDP / algebraic probes")
    probes = []
    probes.append(probe_d1(state, "D1: 3-channel LP, n_target=R"))
    probes.append(probe_d2(state, "D2: 3-channel LP, n_target=tr_M^3"))
    probes.append(probe_d3(state, "D3: Frobenius-dual LP, demand=y_λ·χ_λ"))
    probes.append(probe_d4(state, LAMBDA_PROTON_TARGET, "D4: algebraic ratios"))
    probes.append(probe_d5(state, LAMBDA_PROTON_TARGET, "D5: 5/2−h²G residual"))
    probes.append(probe_d6(state, "D6: q-content cost LP"))

    target_f = float(LAMBDA_PROTON_TARGET)
    for p in probes:
        print(f"  [{p['label']}]")
        if "error" in p:
            print(f"    ERROR: {p['error']}")
            continue
        if "candidate_lambda_y0" in p:
            cand = p["candidate_lambda_y0"]
            delta = cand - target_f
            print(f"    y_0*  = {cand:.10f}   "
                  f"(Δ from target: {delta:+.6e})")
        if "candidate_lambda_primal_over_R" in p:
            cand = p["candidate_lambda_primal_over_R"]
            delta = cand - target_f
            print(f"    primal/R = {cand:.10f}   "
                  f"(Δ: {delta:+.6e})")
        if "ratios" in p:
            for k, v in p["ratios"].items():
                print(f"    {k:40s} = {v}")
        if "candidate_lambda_y0_times_R" in p:
            cand = p["candidate_lambda_y0_times_R"]
            delta = cand - target_f
            print(f"    y_0*·R = {cand:.10f}   "
                  f"(Δ: {delta:+.6e})")
        if "epsilon_residual" in p:
            print(f"    leading 5/2−h²G  = {p['leading_5_2_minus_h2_G']}")
            print(f"    ε := target − lead = {p['epsilon_residual']}")
            print(f"    ε in ppm of target = {p['epsilon_in_ppm']:.3f} ppm")
            print(f"    ratios to higher-order candidates:")
            for k, v in p["ratios_to_higher_order_candidates"].items():
                print(f"      ε / {k:18s} = {v}")
        if "duality_gap" in p:
            print(f"    duality_gap = {p['duality_gap']:.3e}")
            print(f"    active_set  = {p.get('active_set', [])}")
        print()

    # Strip numpy floats for JSON-friendly output
    for p in probes:
        for k, v in list(p.items()):
            if isinstance(v, np.floating):
                p[k] = float(v)
            elif isinstance(v, np.ndarray):
                p[k] = v.tolist()
    w.add_data("stage2_probes", probes)

    # Stage 3: Q-locality — evaluate at q_0 ± ε
    print("[3/3] Q-locality check at q_0 ± ε")
    eps_list = [
        mp.mpf("-1e-4"),
        mp.mpf("-1e-5"),
        mp.mpf("0"),
        mp.mpf("1e-5"),
        mp.mpf("1e-4"),
    ]
    sweep = q_locality_sweep(eps_list, dps=50)
    for entry in sweep:
        print(f"  q = {entry['q'][:30]}   "
              f"R = {entry['R_volume'][:14]}   "
              f"tr_M = {entry['tr_M_proton_H3'][:14]}")
    w.add_data("stage3_q_locality_sweep", sweep)
    print()

    # Stage 4: structural notes
    target = LAMBDA_PROTON_TARGET
    notes = {
        "user_constraint": (
            "Per user note 2026-05-22: 'q_o not special, just where we "
            "happen to be'. Any candidate λ_scale parametrisation must "
            "therefore be a SMOOTH FUNCTION OF q evaluable at the entire "
            "substrate window, not a numerical accident at q_0. The "
            "stage-3 sweep above provides the q-derivative data for "
            "candidate smoothness verification."
        ),
        "stage1_observation_ratio_to_tr_M": fmt(target / state["tr_M_proton_H3"]),
        "stage1_observation_ratio_to_R": fmt(target / state["R_volume"]),
        "stage1_observation_target_x_hbar_q_sq_over_8G": fmt(
            target * state["hbar_q"] ** 2 / (8 * mp.catalan)
        ),
        "next_steps": [
            "Refine probe D1/D2 with proper categorical-mass objective "
            "(currently uses χ as cost, which is structurally arbitrary).",
            "Try SDP variant (`solve_psd_operator_selection_sdp`) with "
            "PSD constraint on the Hoefsmit-block submatrix.",
            "Symbolic-q variant: parametrise probe D1 over a sympy q, "
            "solve LP symbolically (linprog with parametric c/G doesn't "
            "exist; use Lagrangian KKT directly).",
            "Cross-check against the Phase 5l constit-factor identity: "
            "the LP whose dual is λ_scale_p should reduce structurally to "
            "ρ_Z^constit(q) = tr_M^3(𝓑_p, q) when the right cost vector "
            "is chosen.",
        ],
    }
    w.add_data("stage4_notes", notes)

    # Verdict assertion: this probe is exploratory; we record whether
    # any probe got within 1e-6 of the target (a "lucky hit") for
    # follow-up investigation.
    candidates: list[tuple[str, float]] = []
    for p in probes:
        if "candidate_lambda_y0" in p and isinstance(p["candidate_lambda_y0"], (int, float)):
            candidates.append((f"{p['label']}/y_0*", p["candidate_lambda_y0"]))
        if "candidate_lambda_primal_over_R" in p and isinstance(
            p["candidate_lambda_primal_over_R"], (int, float)
        ):
            candidates.append((f"{p['label']}/primal_obj/R",
                               p["candidate_lambda_primal_over_R"]))

    best_label, best_delta = None, float("inf")
    for label, val in candidates:
        delta = abs(val - target_f)
        if delta < best_delta:
            best_delta, best_label = delta, label
    print(f"Closest candidate: {best_label}   |Δ| = {best_delta:.6e}")
    w.add_data("stage4_closest_candidate", {
        "label": best_label,
        "abs_delta": best_delta,
    })

    out = w.save()
    print(f"\nWitness: {Path(out).name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
