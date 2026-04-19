#!/usr/bin/env python3
"""
Electron placement via FROBENIUS DEMAND-SUPPLY SDP over the knot-
operator basis.

Per user (2026-04-19): "the NF reduction does that" — no free
location parameter, no reserved strands.  Work entirely in H_3(q)
NF space (6-D basis {γ, σ₀, σ₁, L₊, L₋, e⁻}) and apply the
demand-supply SDP from
[prop:knot-operator-selection](#prop:knot-operator-selection)
clause (iv).

**SDP construction (content block clauses iii, iv):**

Given the atom state  K ∈ H_3(q)  (NF vector [c₀, ..., c₅]):

  dem_coord_i  =  max(-c_i, 0)                   (demand per basis)
  dem(K)       =  Σ_i dem_coord_i · b_i^∨         (dual basis)
  ||dem(K)||_F =  √(dem_coord^T · G^{-1} · dem_coord)

The electron operator Φ is a linear combination over the torus-knot
operator basis:

  Φ  =  Σ_α  a_α · β(T_α),    a_α ≥ 0

with T_α ∈ {T_{1,0}, T_{2,1}, T_{2,2}, T_{2,3}, T_{2,5}}.

SDP:

  min    Σ_α  c(T_α) · a_α                   (crossing energy)
  s.t.   Φ_NF · dem_coord ≥ ||dem(K)||_F      (satisfy demand)
         a_α ≥ 0

where c(T_α) is the crossing count (0, 1, 2, 3, 5 respectively)
and Φ_NF = Σ_α a_α · T_NF_α is the NF coefficient vector of Φ.

For Z electrons the SDP is solved iteratively: after applying Φ₁
the atom state updates to K · Φ₁, its demand is recomputed, and
the SDP selects Φ₂ — and so on for Z electrons.

This is the correct Frobenius demand-supply SDP, replacing the
heuristic "min tr_M_atom" criterion of the earlier
electron_knot_operator_sdp.py.
"""
from __future__ import annotations

import sys
import json
import time
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as Q0, HA as h
from canonical_plus_multibrane import E_0_BETA_DECAY_MEV
from hecke_core import hm
from mass_at_3A_proper import atom_braid_word_3A, _cached_seminormal
from hecke_characters import partitions_of, dim_q, qfac

import importlib.util
_conf_spec = importlib.util.spec_from_file_location(
    "_conflp", Path(__file__).parent / "confinement-lp.py")
_conf_mod = importlib.util.module_from_spec(_conf_spec)
import os as _os
_old = _os.dup(1); _null = _os.open(_os.devnull, _os.O_WRONLY)
_os.dup2(_null, 1)
try:
    _conf_spec.loader.exec_module(_conf_mod)
finally:
    _os.dup2(_old, 1); _os.close(_null); _os.close(_old)
G_h3 = np.asarray(_conf_mod.G, dtype=float)

try:
    import cvxpy as cp
    HAVE_CVXPY = True
except ImportError:
    HAVE_CVXPY = False


# ──────────────────────────────────────────────────────────────────
# Knot-operator basis: exact Hecke braid words and crossing counts
# ──────────────────────────────────────────────────────────────────

KNOT_OP_BRAID_WORDS = {
    "T_1_0": [],                                       # identity
    "T_2_1": [(1.0, 0.0, 0)],                          # σ_0
    "T_2_2": [(1.0, 0.0, 0), (1.0, 0.0, 0)],           # σ_0^2
    "T_2_3": [(1.0, 0.0, 0), (1.0, 0.0, 1), (1.0, 0.0, 0)],  # σ_0 σ_1 σ_0
    "T_2_5": [(1.0, 0.0, 0), (1.0, 0.0, 1),            # (σ_0 σ_1)^2 σ_0
                 (1.0, 0.0, 0), (1.0, 0.0, 1),
                 (1.0, 0.0, 0)],
}

KNOT_OP_CROSSINGS = {"T_1_0": 0, "T_2_1": 1, "T_2_2": 2,
                          "T_2_3": 3, "T_2_5": 5}

KNOT_OPS = list(KNOT_OP_BRAID_WORDS.keys())
# Electron candidates exclude T_{1,0} (identity) — electrons are
# physical knots, not the elastic channel. T_{1,0} with 0 crossings
# would trivially dominate min-E_cross at arbitrary scale.
ELECTRON_OPS = [op for op in KNOT_OPS if op != "T_1_0"]


def nf_identity() -> list[float]:
    return [1.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def apply_braid_word(nf: list[float],
                       word: list[tuple[float, float, int]]
                       ) -> list[float]:
    out = list(nf)
    for (c, d, g) in word:
        out = hm(out, c, d, g)
    return out


def knot_op_nf(op: str) -> np.ndarray:
    """NF vector of β(T_α) applied to identity in H_3(q)."""
    return np.asarray(
        apply_braid_word(nf_identity(), KNOT_OP_BRAID_WORDS[op]),
        dtype=float)


T_NF_BASIS = np.stack([knot_op_nf(op) for op in KNOT_OPS])  # 5 × 6
T_NF_ELECTRON = np.stack([knot_op_nf(op) for op in ELECTRON_OPS])  # 4 × 6


def tr_m_nf(nf_vec: np.ndarray) -> float:
    """Markov trace of an NF vector in H_3(q) at q₀."""
    from pyhecke.gram import TR_M
    return float(np.asarray(TR_M, dtype=float) @ nf_vec)


def apply_phi_linear(nf: np.ndarray, phi_weights: np.ndarray
                         ) -> np.ndarray:
    """Multiply an NF vector on the right by Φ = Σ a_α β(T_α).

    Since multiplication in H_3 is linear, apply each β(T_α) to nf
    separately, then take the weighted sum.
    """
    result = np.zeros(6, dtype=float)
    for i, op in enumerate(KNOT_OPS):
        after = apply_braid_word(list(nf), KNOT_OP_BRAID_WORDS[op])
        result += phi_weights[i] * np.asarray(after, dtype=float)
    return result


# ──────────────────────────────────────────────────────────────────
# Atom NF without electrons
# ──────────────────────────────────────────────────────────────────

def build_atom_nf_no_electrons(Z: int, N: int) -> np.ndarray:
    """Same as hecke_core.build_atom_nf but stop before the Z × σ₁⁻¹
    electron applications.  (Matches lines 856-911 of hecke_core.py.)
    """
    A = Z + N
    if A == 0:
        return np.array(nf_identity(), dtype=float)

    ordering = []
    pc, nc = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append('p'); pc += 1
        else:
            ordering.append('n'); nc += 1

    nf = nf_identity()
    for k in range(A):
        if ordering[k] == 'p':
            for _ in range(3):
                nf = hm(nf, 1, 0, 0); nf = hm(nf, 1, -h, 1)
            nf = hm(nf, 1, 0, 0)                 # pair(0,1) uu
            nf = hm(nf, 1, -h/2, 0)              # pair(0,2) ud
            nf = hm(nf, 1, -h/2, 1)              # pair(1,2) ud
            nf = hm(nf, 1, 0, 0)                 # gluon
        else:
            for _ in range(3):
                nf = hm(nf, 1, 0, 0); nf = hm(nf, 1, -h, 1)
            nf = hm(nf, 1, -h/2, 0)              # pair(0,1) ud
            nf = hm(nf, 1, -h/2, 0)              # pair(0,2) ud
            nf = hm(nf, 1, -h, 1)                # pair(1,2) dd
            nf = hm(nf, 1, 0, 0)                 # gluon
        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == 'p' and tj == 'p':
                nf = hm(nf, 1, 0, 0)
            elif ti == 'n' and tj == 'n':
                nf = hm(nf, 1, -h, 0)
            else:
                nf = hm(nf, 1, -h/2, 0)
    return np.asarray(nf, dtype=float)


# ──────────────────────────────────────────────────────────────────
# Demand-supply SDP
# ──────────────────────────────────────────────────────────────────

def solve_demand_supply_sdp(K: np.ndarray, G: np.ndarray
                                  ) -> dict:
    """For a given H_3 state K, solve:

      min    c^T a                 (c_α = crossing count of T_α)
      s.t.   Φ_NF · dem ≥ ||dem||_F
             a ≥ 0
      with   Φ_NF = T_NF_BASIS^T · a

    Returns a dict with weights, dominant operator, dual info.
    """
    if not HAVE_CVXPY:
        raise ImportError("cvxpy required for demand-supply SDP")

    dem_coord = np.maximum(-K, 0.0)
    G_inv = np.linalg.inv(G)
    dem_norm_sq = float(dem_coord @ G_inv @ dem_coord)
    dem_norm = float(np.sqrt(max(dem_norm_sq, 0.0)))

    if dem_norm < 1e-12:
        return {
            "status": "no_demand",
            "weights": {op: 0.0 for op in KNOT_OPS},
            "dominant": "T_1_0",
            "E_cross": 0.0,
            "dem_norm": dem_norm,
            "dem_coord": dem_coord.tolist(),
            "phi_nf": [0.0] * 6,
        }

    n = len(ELECTRON_OPS)
    a = cp.Variable(n, nonneg=True)
    phi_nf = T_NF_ELECTRON.T @ a
    crossings = np.array([KNOT_OP_CROSSINGS[op] for op in ELECTRON_OPS],
                              dtype=float)
    constraints = [phi_nf @ dem_coord >= dem_norm]
    prob = cp.Problem(cp.Minimize(crossings @ a), constraints)
    prob.solve(solver="CLARABEL")

    weights = {op: 0.0 for op in KNOT_OPS}
    for i, op in enumerate(ELECTRON_OPS):
        weights[op] = float(a.value[i])
    dominant = max(weights.items(), key=lambda kv: kv[1])[0]
    return {
        "status": prob.status,
        "weights": weights,
        "dominant": dominant,
        "E_cross": float(crossings @ a.value),
        "dem_norm": dem_norm,
        "dem_coord": dem_coord.tolist(),
        "phi_nf": (T_NF_ELECTRON.T @ a.value).tolist(),
    }


# ──────────────────────────────────────────────────────────────────
# Main run
# ──────────────────────────────────────────────────────────────────

def iterate_demand_supply(Z: int, N: int, B_AME: float) -> dict:
    """For a (Z, N) atom, compute K_atom (no electrons) then
    iteratively apply Z Φs via the demand-supply SDP."""
    A = Z + N
    K_atom_no_e = build_atom_nf_no_electrons(Z, N)
    K_free_no_e = build_atom_nf_no_electrons(0, Z + N)  # no inter-nuc

    # Baselines (no electrons): tr_M at H_3 NF level
    trM_a_no_e = tr_m_nf(K_atom_no_e)
    trM_f_no_e = tr_m_nf(K_free_no_e)
    B_no_e = E_0_BETA_DECAY_MEV * (abs(trM_f_no_e) - abs(trM_a_no_e))
    err_no_e = abs(B_no_e - B_AME) / (A * 938.272) * 100

    result = {
        "Z": Z, "N": N, "A": A, "B_AME_MeV": B_AME,
        "K_atom_no_e": K_atom_no_e.tolist(),
        "baseline_no_electrons_H3": {
            "trM_atom": trM_a_no_e, "trM_free": trM_f_no_e,
            "B_pred_MeV": B_no_e, "err_pct": err_no_e,
        },
        "electrons": [],
    }

    K = K_atom_no_e.copy()
    K_free = K_free_no_e.copy()
    for e_i in range(Z):
        sdp = solve_demand_supply_sdp(K, G_h3)
        weights = sdp["weights"]
        dominant = sdp["dominant"]
        # Apply Φ linearly to both atom and free states
        phi_weights = np.array([weights[op] for op in KNOT_OPS],
                                    dtype=float)
        # Scale weights so that the applied Φ has unit "volume" —
        # otherwise min-E_cross can drive all weights to 0 when
        # demand is small.  Normalize by sum(weights).  But if sum=0
        # (no demand), Φ = identity.
        w_sum = phi_weights.sum()
        if w_sum > 1e-12:
            phi_norm = phi_weights / w_sum
        else:
            phi_norm = np.array([1.0, 0, 0, 0, 0], dtype=float)  # T_1_0

        K_next = apply_phi_linear(K, phi_norm)
        K_free_next = apply_phi_linear(K_free, phi_norm)

        trM_a = tr_m_nf(K_next)
        trM_f = tr_m_nf(K_free_next)
        B = E_0_BETA_DECAY_MEV * (abs(trM_f) - abs(trM_a))
        err = abs(B - B_AME) / (A * 938.272) * 100

        print(f"  e {e_i+1}/{Z}: dominant={dominant}  "
              f"E_cross={sdp['E_cross']:+.4f}  "
              f"dem_norm={sdp['dem_norm']:+.4e}  "
              f"B={B:+.4f}  err={err:.4f}%")
        for op in KNOT_OPS:
            w = weights[op]
            if w > 1e-6:
                print(f"    a_{op} = {w:+.4e}  "
                      f"(normalized: {phi_norm[KNOT_OPS.index(op)]:+.4f})")

        result["electrons"].append({
            "electron_index": e_i,
            "sdp_status": sdp["status"],
            "dominant_op": dominant,
            "weights": weights,
            "weights_normalized": phi_norm.tolist(),
            "E_cross": sdp.get("E_cross"),
            "dem_norm": sdp["dem_norm"],
            "dem_coord": sdp["dem_coord"],
            "K_after": K_next.tolist(),
            "trM_atom_after": trM_a,
            "trM_free_after": trM_f,
            "B_pred_MeV": B,
            "err_pct": err,
        })
        K = K_next
        K_free = K_free_next

    # Also compare to the legacy Z × σ₁⁻¹ pile-up
    K_legacy = K_atom_no_e.copy()
    K_free_legacy = K_free_no_e.copy()
    for _ in range(Z):
        K_legacy = np.asarray(
            hm(list(K_legacy), 1, -h, 1), dtype=float)
        K_free_legacy = np.asarray(
            hm(list(K_free_legacy), 1, -h, 1), dtype=float)
    trM_a_leg = tr_m_nf(K_legacy)
    trM_f_leg = tr_m_nf(K_free_legacy)
    B_leg = E_0_BETA_DECAY_MEV * (abs(trM_f_leg) - abs(trM_a_leg))
    err_leg = abs(B_leg - B_AME) / (A * 938.272) * 100
    result["legacy_Z_sigma1_inv"] = {
        "trM_atom": trM_a_leg, "trM_free": trM_f_leg,
        "B_pred_MeV": B_leg, "err_pct": err_leg,
    }

    result["final"] = {
        "trM_atom": tr_m_nf(K), "trM_free": tr_m_nf(K_free),
        "B_pred_MeV": E_0_BETA_DECAY_MEV * (abs(tr_m_nf(K_free))
                                                 - abs(tr_m_nf(K))),
        "err_pct": None,
        "dominant_ops": [e["dominant_op"] for e in result["electrons"]],
    }
    result["final"]["err_pct"] = (
        abs(result["final"]["B_pred_MeV"] - B_AME) / (A * 938.272) * 100)

    # Plancherel-level re-evaluation: apply the SDP-chosen dominant
    # operator per electron to the H_{3A} atom word, then compute the
    # Plancherel Markov trace. This is comparable to the audit's mass
    # predictions. Each T_α's braid word is anchored at gen 0 (NF
    # reduction in H_{3A} collapses location equivalence).
    word_a = list(atom_braid_word_3A(
        Z, N, include_inter=True, include_electrons=False))
    word_f = list(atom_braid_word_3A(
        Z, N, include_inter=False, include_electrons=False))
    for elec in result["electrons"]:
        op = elec["dominant_op"]
        if op == "T_1_0":
            continue
        op_word = KNOT_OP_BRAID_WORDS[op]
        word_a = word_a + op_word
        word_f = word_f + op_word
    n_strands = 3 * A

    def _trM(word, n):
        from scipy.sparse import issparse, eye as speye
        nfac = qfac(n)
        total = 0.0
        for shape in partitions_of(n):
            sigmas, dim, _ = _cached_seminormal(shape)
            if dim == 0: continue
            dq = dim_q(shape)
            if dq == 0: continue
            sparse = bool(sigmas) and issparse(sigmas[0])
            if sparse:
                prod = speye(dim, format='csr'); I = speye(dim, format='csr')
            else:
                prod = np.eye(dim); I = np.eye(dim)
            for (c, d, g) in word:
                if g < len(sigmas):
                    prod = prod @ (c * sigmas[g] + d * I)
            chi = float(prod.diagonal().sum()) if sparse else float(np.trace(prod))
            total += (dq * dq) / nfac * chi / dim
        return total

    trM_a_pl = _trM(word_a, n_strands)
    trM_f_pl = _trM(word_f, n_strands)
    B_pl = E_0_BETA_DECAY_MEV * (abs(trM_f_pl) - abs(trM_a_pl))
    err_pl = abs(B_pl - B_AME) / (A * 938.272) * 100
    result["plancherel_evaluation"] = {
        "n_strands": n_strands,
        "dominant_ops_applied": [e["dominant_op"]
                                      for e in result["electrons"]],
        "trM_atom": trM_a_pl, "trM_free": trM_f_pl,
        "B_pred_MeV": B_pl, "err_pct": err_pl,
    }
    return result


if __name__ == "__main__":
    ATOMS = [
        ("D",   1, 1,  2.22452),
        ("T",   1, 2,  8.481821),
        ("3He", 2, 1,  7.71804),
    ]

    out = (Path(__file__).parent
             / "electron-demand-supply-sdp.witness.json")
    print("=" * 110)
    print("ELECTRON DEMAND-SUPPLY SDP (Frobenius, H_3 NF only)")
    print("per prop:knot-operator-selection clause (iv)")
    print(f"q0 = {Q0}, E_0 = {E_0_BETA_DECAY_MEV} MeV")
    print("=" * 110)

    all_results = []
    for name, Z, N, B_AME in ATOMS:
        A = Z + N
        print(f"\n{name} (Z={Z}, N={N}, A={A})")
        try:
            r = iterate_demand_supply(Z, N, B_AME)
            r["atom"] = name
            all_results.append(r)
            base = r["baseline_no_electrons_H3"]
            leg = r["legacy_Z_sigma1_inv"]
            fin = r["final"]
            print(f"  baseline (no e, H_3):    "
                  f"B={base['B_pred_MeV']:+.4f}  err={base['err_pct']:.4f}%")
            print(f"  legacy Z×σ₁⁻¹:           "
                  f"B={leg['B_pred_MeV']:+.4f}  err={leg['err_pct']:.4f}%")
            print(f"  demand-supply SDP (H_3, ops={fin['dominant_ops']}): "
                  f"B={fin['B_pred_MeV']:+.4f}  err={fin['err_pct']:.4f}%")
            pl = r["plancherel_evaluation"]
            print(f"  demand-supply Plancherel (n={pl['n_strands']}, "
                  f"ops={pl['dominant_ops_applied']}): "
                  f"B={pl['B_pred_MeV']:+.4f}  err={pl['err_pct']:.4f}%")
        except Exception as e:
            import traceback
            print(f"  ERR: {type(e).__name__}: {e}")
            traceback.print_exc()
            all_results.append({"atom": name, "Z": Z, "N": N,
                                    "error": str(e)})
        out.write_text(json.dumps({
            "computation": "electron-demand-supply-sdp",
            "description": (
                "Electron placement via Frobenius demand-supply SDP "
                "per prop:knot-operator-selection clause (iv). Works "
                "entirely in H_3(q) NF (6-D); location is not a free "
                "parameter — NF reduction collapses placement "
                "equivalences. The SDP minimises crossing energy "
                "subject to the dual-pairing satisfy-demand constraint "
                "Φ_NF · dem_coord ≥ ||dem||_F. Iterative for Z > 1."),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "parameters": {"q0": Q0, "E_0_MeV": E_0_BETA_DECAY_MEV,
                              "knot_operators": KNOT_OPS},
            "results": all_results,
        }, indent=2, default=str))

    print(f"\nWitness: {out}")
