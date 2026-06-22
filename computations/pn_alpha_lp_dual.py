#!/usr/bin/env python3
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

LP-dual stability probe for the pn-mixing parameter α.

The pn inter-nucleon crossing is postulated in hecke_symbolic.py as
½(σ + σ⁻¹), i.e. (c, d) = (1, −α·HA) with α = ½.  There is no
algebraic derivation of α = ½ from the Hecke relation itself — any
convex combination α ∈ [0, 1] is a valid Hecke element.  This script
asks whether α = ½ is picked out by LP-dual / Frobenius-positivity
stability, or whether it's underdetermined.

Experiment (deuterium, A = 2):
  1. Parameterize pn crossing as (c, d) = (1, −α·HA).
  2. Build D tower: per-generator V̂(α) via atom_per_generator_volumes
     with pn_alpha override.  Free baseline independent of α.
  3. B_pred(α) = E_0 · (m_free − m_atom(α))  — compute on fine grid.
  4. Solve LP (primal + dual) at each α:
       min  Σ tᵢ · xᵢ   (Markov-trace objective)
       s.t. Σ xᵢ = target_net(α)
            G x ≥ 0
     Dual shadow prices y_i tell us which Frobenius-positivity
     constraints are tight at that α.  If shadow prices become
     degenerate at a unique α*, that α* is LP-dual-stable.

Output: table of α, m_atom, B_pred, |tr_M|, primal obj, dual active
constraints.  Plus the α that minimises |B_pred − B_AME|.

Usage:
    python3 pn_alpha_lp_dual.py
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import json
import math
import copy
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0
# z/NF_BASIS/TR_M now owned by pyhecke.gram (M2b inversion). Keep local
# bootstrap for dev mode; the installed-pyhecke path is preferred.
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[2] / "tools" / "pyhecke" / "python"))
from pyhecke.gram import z as _PG_Z, NF_BASIS as _PG_NF_BASIS, TR_M as _PG_TR_M  # noqa: E402

from mass_endomorphism import HA as HA_VAL, z_mark
# Canonical API: prop:mass-tower-operator-valued — re-export of the
# Φ_q tower implementation that lives in mass_endomorphism. Both
# expressions are equivalent at H_{3A} (verified per PR #944's
# H_12 Phase-1 A-operator extract).
from mass_tower_operator_valued import mass_from_tower
from pyhecke.gram import atom_per_generator_volumes
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402 — full-precision m_p for E_0 anchor

E_0_CAL_MEV = float(M_P_MEV_VALIDATION) / 1178995.5254  # proton tower → m_p MeV
B_AME_D_MEV = 2.22452  # deuteron AME2020


# ── Parameterize pn crossing in atom_per_generator_volumes ──────
#
# atom_per_generator_volumes currently hardcodes the pn crossing as
# base_cross = (1.0, -h/2) (h = HA).  We implement the α-sweep by
# monkey-patching _step_chain logic: rather than reach into the
# internals, we call the original function and then, for pn-adjacent
# generators, post-correct via the difference between α and ½.
#
# Simpler & robust: copy the relevant accumulator loop here, using
# the same conventions, but with pn_alpha as a parameter.

sys.path.insert(0, str(Path(__file__).parent))
from hecke_core import _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1

HA = HA_VAL
h = HA
qi = qi0


def q_int_local(k: int) -> float:
    return (q0 ** k - qi ** k) / (q0 - qi) if k else 0.0


def atom_per_gen_vols_alpha(Z, N, *, pn_alpha=0.5,
                              m_pp=1, m_pn=1, m_nn=1,
                              include_inter=True):
    """Per-generator V̂_full for the atom braid, with pn_alpha.

    Replicates atom_per_generator_volumes but exposes the pn mixing:
        pn crossing = (c, d) = (1, −pn_alpha · HA).
    pn_alpha = 0 → pure σ (pp-like); 0.5 → symmetric average;
    1 → pure σ⁻¹ (nn-like).
    """
    A = Z + N
    if A < 1:
        return []
    ordering = ['p'] * Z + ['n'] * N
    if include_inter:
        n_strands = 3 * A
        n_gens_total = n_strands - 1
    else:
        n_gens_total = 2 * A

    a_arr = [0.0] * n_gens_total
    b_arr = [1.0] * n_gens_total
    sp_arr = [1.0] * n_gens_total
    ap_arr = [1.0] * n_gens_total

    for k, nuc in enumerate(ordering):
        intra = _PROTON_G0 if nuc == 'p' else _NEUTRON_G0
        intra_g1 = _PROTON_G1 if nuc == 'p' else _NEUTRON_G1
        if include_inter:
            base_g0 = 3 * k
            base_g1 = 3 * k + 1
        else:
            base_g0 = 2 * k
            base_g1 = 2 * k + 1
        for c, d in intra:
            i = base_g0
            a_new = a_arr[i] * c * h + a_arr[i] * d + b_arr[i] * c
            b_new = a_arr[i] * c + b_arr[i] * d
            a_arr[i] = a_new
            b_arr[i] = b_new
            sp_arr[i] *= c * q0 + d
            ap_arr[i] *= -c * qi + d
        for c, d in intra_g1:
            i = base_g1
            a_new = a_arr[i] * c * h + a_arr[i] * d + b_arr[i] * c
            b_new = a_arr[i] * c + b_arr[i] * d
            a_arr[i] = a_new
            b_arr[i] = b_new
            sp_arr[i] *= c * q0 + d
            ap_arr[i] *= -c * qi + d
        if include_inter and k < A - 1:
            i = 3 * k + 2
            next_nuc = ordering[k + 1]
            if nuc == 'p' and next_nuc == 'p':
                base_cross = (1.0, 0.0)
                m_this = m_pp
            elif nuc == 'n' and next_nuc == 'n':
                base_cross = (1.0, -h)
                m_this = m_nn
            else:
                # pn: generalized — (1, −α·HA)
                base_cross = (1.0, -pn_alpha * h)
                m_this = m_pn
            for c, d in [base_cross] * m_this:
                a_new = a_arr[i] * c * h + a_arr[i] * d + b_arr[i] * c
                b_new = a_arr[i] * c + b_arr[i] * d
                a_arr[i] = a_new
                b_arr[i] = b_new
                sp_arr[i] *= c * q0 + d
                ap_arr[i] *= -c * qi + d

    z_m = 1.0 / (q0 ** 0.5 + qi ** 0.5)
    nf3 = q_int_local(1) * q_int_local(2) * q_int_local(3)
    w_sym = 1.0 / nf3
    w_std = q_int_local(2) ** 2 / nf3
    w_alt = 1.0 / nf3
    wt = w_sym + w_std + w_alt
    w_sym /= wt; w_std /= wt; w_alt /= wt

    vols = []
    for i in range(n_gens_total):
        Vs = z_m * a_arr[i] + b_arr[i]
        Vf = w_sym * sp_arr[i] + w_std * Vs + w_alt * ap_arr[i]
        vols.append({"std": Vs, "sym": sp_arr[i], "alt": ap_arr[i], "full": Vf})
    return vols


def binding_at_alpha(Z, N, pn_alpha: float) -> dict:
    """Compute tower binding for (Z, N) at given pn_alpha."""
    va = atom_per_gen_vols_alpha(Z, N, pn_alpha=pn_alpha)
    vf = atom_per_gen_vols_alpha(Z, N, pn_alpha=pn_alpha,
                                   include_inter=False)
    _, _, _, ta = mass_from_tower(va)
    _, _, _, tf = mass_from_tower(vf)
    return {
        "pn_alpha": pn_alpha,
        "m_atom": ta,
        "m_free": tf,
        "B_pred": E_0_CAL_MEV * (tf - ta),
        "V_pn_gen": va[2]["full"] if len(va) > 2 else None,
    }


# ── LP-dual probe on deuteron  ─────────────────────────────────
#
# Use the 6-basis H_3 framework (γ, σ₀, σ₁, L₊, L₋, e⁻) per
# confinement-lp.py, but construct the DEUTERON NF element from the
# pn crossing only (the proton / neutron intra-NFs are separate
# H_3 blocks; the pn crossing mediates between them, which in the
# single-block LP is represented by the mixed (1, −α·HA) element).
#
# What we probe:  how the dual shadow prices y_i react as α sweeps.

NF_BASIS = _PG_NF_BASIS  # moved to pyhecke.gram
NF_NAMES = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
# e⁻ Markov trace is h·z² + z (NOT z³); see docs/audits/2026-05-19-trm5-markov-bug.md
TR_M_BASIS = np.array([1.0, z_mark, z_mark, z_mark**2, z_mark**2,
                        h * z_mark**2 + z_mark])


def hecke_mul(t1, t2):
    result = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            result[w] = result.get(w, 0.0) + c1 * c2
    return {w: c for w, c in result.items() if abs(c) > 1e-15}


def reduce_nf(terms):
    changed = True
    while changed:
        changed = False
        new_terms = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1]:
                    i = word[pos]
                    pre, suf = word[:pos], word[pos + 2:]
                    new_terms[pre + (i,) + suf] = \
                        new_terms.get(pre + (i,) + suf, 0.0) + coeff * HA
                    new_terms[pre + suf] = \
                        new_terms.get(pre + suf, 0.0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and abs(a - b) == 1:
                    new_trip = (b, a, b)
                    if new_trip < (a, b, a):
                        nw = word[:pos] + new_trip + word[pos + 3:]
                        new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                        done = changed = True
                        break
            if not done:
                new_terms[word] = new_terms.get(word, 0.0) + coeff
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms


def build_gram():
    G = np.zeros((6, 6))
    for i in range(6):
        for j in range(6):
            prod = hecke_mul({NF_BASIS[i]: 1.0}, {NF_BASIS[j]: 1.0})
            nf = reduce_nf(prod)
            vec = np.array([nf.get(b, 0.0) for b in NF_BASIS])
            G[i, j] = sum(vec[k] * TR_M_BASIS[k] for k in range(6))
    return G


def pn_element_vec(pn_alpha: float) -> np.ndarray:
    """(1, −α·HA) in the 6-basis: c₀ = −α·HA (γ), c₁ = 1.0 (σ₀)."""
    v = np.zeros(6)
    v[0] = -pn_alpha * HA
    v[1] = 1.0
    return v


def tower_binding_derivative(alpha: float, delta: float = 1e-5) -> dict:
    """Numerical ∂B/∂α on D via central difference.

    A stationary point ∂B/∂α|_{α=½} = 0 would be evidence of a
    tower-level derivation of the ½ postulate (via first-order
    optimality).  Returns the derivative value and the per-generator
    V̂ contributions to disentangle where α enters.
    """
    b_lo = binding_at_alpha(1, 1, alpha - delta)
    b_hi = binding_at_alpha(1, 1, alpha + delta)
    return {
        "alpha": alpha,
        "dB_dalpha": (b_hi["B_pred"] - b_lo["B_pred"]) / (2 * delta),
        "dVpn_dalpha": ((b_hi["V_pn_gen"] - b_lo["V_pn_gen"])
                         / (2 * delta)),
        "B_pred": 0.5 * (b_hi["B_pred"] + b_lo["B_pred"]),
    }


def tower_sdp_dual_at_alpha(alpha: float) -> dict:
    """Adjacent-pair SDP on the D tower at given α.

    Variables V̂_i ≥ 0 for each generator, bounded by the Φ_q
    singularity (V̂_i < q₀ − 0.05).  Per-generator V̂_i is FIXED to
    the tower value at this α (not free) — we still construct a
    2×2 PSD block per adjacent pair and ask cvxpy for shadow prices
    on the PSD constraint.  A non-zero shadow price means that pair
    is tight; how the shadow prices MOVE with α is the tower-level
    LP-dual signal.

    Setup:
        min   Σ w_i · V̂_i  (fixed V̂_i; objective = constant =
              Σ w_i · V̂_i(α), passed through)
        s.t.  [[V̂_i, x_i], [x_i, V̂_{i+1}]] ⪰ 0  (auxiliary x_i ≥ 0)
              x_i ≤ (V̂_i + V̂_{i+1})/2

    Returns per-pair x_i values + SDP dual norms (coarse proxy).
    """
    try:
        import cvxpy as cp
    except ImportError:
        return {"alpha": alpha, "status": "no_cvxpy"}

    va = atom_per_gen_vols_alpha(1, 1, pn_alpha=alpha)
    V_hat = [v["full"] for v in va]
    n = len(V_hat)
    if n < 2:
        return {"alpha": alpha, "status": "trivial"}
    # Auxiliary pair variables
    x = cp.Variable(n - 1, nonneg=True)
    constraints = []
    for i in range(n - 1):
        block = cp.bmat([
            [cp.Constant(V_hat[i]), x[i]],
            [x[i], cp.Constant(V_hat[i + 1])],
        ])
        constraints.append(block >> 0)
        constraints.append(
            x[i] <= (V_hat[i] + V_hat[i + 1]) / 2)
    # Maximize pair couplings x_i (probes adjacent-pair PSD tightness)
    objective = cp.Maximize(cp.sum(x))
    prob = cp.Problem(objective, constraints)
    try:
        prob.solve(solver=cp.SCS, verbose=False)
        if prob.status in [cp.OPTIMAL, cp.OPTIMAL_INACCURATE]:
            x_vals = x.value if x.value is not None else np.zeros(n - 1)
            # Pair tightness: x_i = √(V̂_i V̂_{i+1})?  If so, PSD is
            # marginal (det = 0).  x_i < √(V̂_i V̂_{i+1}) → slack.
            sqrt_geom = [(V_hat[i] * V_hat[i + 1]) ** 0.5
                          for i in range(n - 1)]
            tight = [bool(abs(x_vals[i] - sqrt_geom[i]) < 1e-4)
                      for i in range(n - 1)]
            return {
                "alpha": alpha,
                "status": "solved",
                "V_hat": V_hat,
                "x_pair": list(x_vals),
                "sqrt_geom": sqrt_geom,
                "tight_pairs": tight,
                "objective": float(prob.value),
            }
        return {"alpha": alpha, "status": prob.status}
    except Exception as e:
        return {"alpha": alpha, "status": f"error:{e}"}


def lp_dual_at_alpha(alpha: float, G: np.ndarray) -> dict:
    """Solve the primal + dual LP with pn-element target net.

    Primal:  min t·x  s.t.  1ᵀx = net(pn_α),  G x ≥ 0
    Dual:    max net(pn_α) · y₀  s.t.  y₀·1 + Gᵀ·y ≤ t, y ≥ 0
    """
    pn_vec = pn_element_vec(alpha)
    target_net = float(pn_vec.sum())

    c = TR_M_BASIS.copy()
    A_eq = np.ones((1, 6))
    b_eq = np.array([target_net])
    A_ub = -G
    b_ub = np.zeros(6)
    bounds = [(-10, 10)] * 6
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                   bounds=bounds, method='highs')
    out = {
        "alpha": alpha,
        "target_net": target_net,
        "status": res.message,
        "success": bool(res.success),
    }
    if res.success:
        out["primal_obj"] = float(res.fun)
        out["x_opt"] = res.x.tolist()
        Gx = G @ res.x
        out["tight_constraints"] = [NF_NAMES[i]
                                      for i in range(6)
                                      if abs(Gx[i]) < 1e-6]
        # Canonical LP-dual record (AGENTS.md §"LP / SDP duals — first-
        # class infra"). Lifted from the in-script eqlin/ineqlin to the
        # standardized field names that lp_dual_witness_validator
        # checks: y0_star, y_star, active_set, primal_obj, dual_obj,
        # duality_gap.
        from lp_dual_solver import solve_operator_selection_lp
        # Pin scipy: committed-witness producer → byte-deterministic (the
        # new "auto" default would use clarabel when its binary is built).
        canon = solve_operator_selection_lp(c, G, target_net, backend="scipy").to_dict()
        out["lp_dual"] = canon
        out["y0_star"] = canon["y0_star"]
        out["y_star"] = canon["y_star"]
        out["active_set"] = canon["active_set"]
        out["dual_obj"] = canon["dual_obj"]
        out["duality_gap"] = canon["duality_gap"]
    return out


# ── Main sweep ──────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 80)
    print("LP-DUAL STABILITY PROBE:  pn crossing (1, −α·HA)")
    print(f"q₀ = {q0:.10f}  HA = {HA:.10f}")
    print(f"E_0 = {E_0_CAL_MEV:.6e} MeV/cat  (proton tower calibration)")
    print(f"B_AME(D) = {B_AME_D_MEV:.4f} MeV")
    print("=" * 80)

    G = build_gram()
    print(f"\nH_3 Gram det = {np.linalg.det(G):.6e}")

    alphas = [i / 40.0 for i in range(41)]  # α = 0.000 .. 1.000 step 0.025

    print("\n─── Tower-binding scan on D ───")
    print(f"{'α':>7} {'V̂_pn':>10} {'m_atom':>13} {'m_free':>13} "
          f"{'B_pred (MeV)':>14} {'|Δ|':>9}")
    binding_scan = []
    for a in alphas:
        d = binding_at_alpha(1, 1, a)
        err = abs(d["B_pred"] - B_AME_D_MEV)
        binding_scan.append({**d, "B_err": err})
        marker = ""
        if abs(a - 0.5) < 1e-9:
            marker = "  ← current postulate (½)"
        print(f"{a:>7.3f} {d['V_pn_gen']:>10.4f} {d['m_atom']:>13.3e} "
              f"{d['m_free']:>13.3e} {d['B_pred']:>+14.4f} "
              f"{err:>9.4f}{marker}")

    # Best α for binding
    best = min(binding_scan, key=lambda r: r["B_err"])
    print(f"\nBest α for B_pred ≈ B_AME:  α* = {best['pn_alpha']:.4f}, "
          f"B_pred = {best['B_pred']:.4f} MeV, |Δ| = {best['B_err']:.4f}")

    print("\n─── LP-dual scan on H_3 Gram basis ───")
    print(f"{'α':>7} {'net':>9} {'primal_obj':>12} {'y₀':>10} "
          f"{'tight constraints'}")
    lp_scan = []
    for a in alphas:
        r = lp_dual_at_alpha(a, G)
        tight = ",".join(r.get("tight_constraints", []))
        y0_str = f"{r.get('y0', float('nan')):+.4f}" if r.get("y0") is not None else "   —   "
        obj_str = f"{r.get('primal_obj', float('nan')):+.4e}" if r.get("primal_obj") is not None else "  —  "
        print(f"{a:>7.3f} {r['target_net']:>+9.4f} {obj_str:>12} {y0_str:>10}  {tight}")
        lp_scan.append(r)

    # ── Tower-level ∂B/∂α scan ───────────────────────────────
    print("\n─── Tower-level derivative scan: ∂B_pred/∂α on D ───")
    print(f"{'α':>7} {'B_pred':>12} {'∂B/∂α':>14} {'∂V̂_pn/∂α':>12}")
    deriv_scan = []
    for a in alphas:
        d = tower_binding_derivative(a)
        deriv_scan.append(d)
        marker = ""
        if abs(a - 0.5) < 1e-9:
            marker = "  ← postulate"
        print(f"{a:>7.3f} {d['B_pred']:>+12.4f} {d['dB_dalpha']:>+14.4e} "
              f"{d['dVpn_dalpha']:>+12.4e}{marker}")

    # Scan for zero-crossing (critical points)
    zero_crossings = []
    for i in range(1, len(deriv_scan)):
        if (deriv_scan[i - 1]["dB_dalpha"] * deriv_scan[i]["dB_dalpha"] < 0):
            zero_crossings.append({
                "between": (deriv_scan[i - 1]["alpha"],
                             deriv_scan[i]["alpha"]),
                "dB_lo": deriv_scan[i - 1]["dB_dalpha"],
                "dB_hi": deriv_scan[i]["dB_dalpha"],
            })
    print("\n∂B/∂α zero-crossings (tower-level critical points):")
    if not zero_crossings:
        print(f"  (none — ∂B/∂α is monotone; ½ is NOT a stationary point)")
    else:
        for zc in zero_crossings:
            print(f"  α* ∈ ({zc['between'][0]:.4f}, "
                  f"{zc['between'][1]:.4f})")

    # ── Tower-level adjacent-pair SDP dual sweep ─────────────
    print("\n─── Tower SDP: adjacent-pair PSD on D per α ───")
    print(f"{'α':>7} {'obj':>9} {'x_0':>7} {'x_1':>7} "
          f"{'x_2':>7} {'x_3':>7} {'tight pairs'}")
    sdp_scan = []
    # Cheap grid (every 4th α) — SDP is slow
    sdp_alphas = alphas[::4]
    for a in sdp_alphas:
        r = tower_sdp_dual_at_alpha(a)
        sdp_scan.append(r)
        if r.get("status") == "solved":
            xs = r["x_pair"]
            tight_str = ",".join(f"{i}" for i, t in enumerate(r["tight_pairs"]) if t)
            print(f"{a:>7.3f} {r['objective']:>9.4f} "
                  f"{xs[0]:>7.4f} {xs[1]:>7.4f} "
                  f"{xs[2]:>7.4f} {xs[3]:>7.4f}  {tight_str}")

    # Where do tight constraints change?
    transitions = []
    for i in range(1, len(lp_scan)):
        prev = set(lp_scan[i - 1].get("tight_constraints", []))
        cur = set(lp_scan[i].get("tight_constraints", []))
        if prev != cur:
            transitions.append({
                "alpha_lo": lp_scan[i - 1]["alpha"],
                "alpha_hi": lp_scan[i]["alpha"],
                "enter": list(cur - prev),
                "leave": list(prev - cur),
            })

    print("\nActive-set transitions (LP-dual regimes):")
    if not transitions:
        print("  (none — same active set across the full scan)")
    else:
        for t in transitions:
            print(f"  α ∈ ({t['alpha_lo']:.3f}, {t['alpha_hi']:.3f}): "
                  f"enter={t['enter']}, leave={t['leave']}")

    # Is there a special α at which the dual becomes degenerate?
    y0_vals = [r.get("y0") for r in lp_scan if r.get("y0") is not None]
    if y0_vals:
        print(f"\ny₀ shadow price range:  min={min(y0_vals):+.4e}, "
              f"max={max(y0_vals):+.4e}")

    witness = {
        "computation": "pn-alpha-lp-dual",
        "description": (
            "LP-dual stability scan for the pn-mixing α in the "
            "inter-nucleon crossing (1, −α·HA).  Three probes: "
            "(a) D tower binding B_pred(α) on a fine α grid; "
            "(b) single-block H_3 LP dual (γ, σ₀, σ₁, L₊, L₋, e⁻) "
            "shadow prices; (c) TOWER-LEVEL tests: ∂B/∂α numerical "
            "derivative + adjacent-pair SDP PSD sweep.  Tests "
            "whether α = ½ is picked out by stability (active-set "
            "change, degenerate y₀, ∂B/∂α zero-crossing, tight "
            "pair PSD transition, or minimum |B_pred − B_AME|)."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q0": q0, "HA": HA, "E_0_MeV": E_0_CAL_MEV,
                        "B_AME_D": B_AME_D_MEV},
        "binding_scan": binding_scan,
        "lp_dual_scan_h3": lp_scan,
        "active_set_transitions": transitions,
        "tower_derivative_scan": deriv_scan,
        "tower_derivative_zero_crossings": zero_crossings,
        "tower_sdp_dual_scan": sdp_scan,
        "best_alpha_for_binding": best,
    }
    out = Path(__file__).parent / "pn-alpha-lp-dual.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
