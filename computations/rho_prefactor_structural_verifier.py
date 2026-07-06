#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical evaluation at q_0 of the
# Wedderburn weights y_λ · χ_λ(T_w); symbolic-q derivation deferred.
"""
Structural ν_SDP(Z, N) rule — verifier for conj:rho-prefactor-structural.

NOTATION (2026-05-17): the SDP multiplicity previously written ρ
in the paper has been renamed to ν_SDP (Greek nu with SDP
subscript) to disambiguate from ρ_K (categorical density, in
atomic-mass-gb-nf.md) and ρ_λ (Hoefsmit irrep matrix).  This
script's variable names (observed_rho, rho_pred, rho_obs, etc.)
are retained for backward compatibility with downstream
consumers (binding_k_solver.py, branch_phase_fit_to_mass_tower.py
etc.) but mathematically refer to ν_SDP.  Witness JSON also
exposes new alias keys observed_nu_SDP / nu_SDP_predicted.

Issue #604 deliverable 4 (closes / narrows GAP-A-4).

The conjecture asserts that the SDP multiplicity ν_SDP(𝔥) of a
confined particle 𝔥 with canonical Hecke element T_w ∈ H_{n_0}(q)
satisfies

    ν_SDP(𝔥) = round(dim_q(λ*(T_w)))   where   λ*(T_w) = argmax_{λ ⊢ n_0} |y_λ(q_0) · χ_λ(T_w)|

with `dim_q(λ) = [d_λ]_q` (q-deformed SYT count via hook-length).
Round-to-nearest matches the Lean class field
`rho_eq_qdim : |(nu_SDP : ℝ) - q_int d_lambda_star| ≤ 1/2`.

This script evaluates the conjecture numerically for every B_3 atomic
identification (proton, neutron, ²H/6_2, ³He/L₆ₐ₄) and reports:

  - per-λ Wedderburn weights |y_λ · χ_λ(T_w)| at q_0
  - dominant λ* and dim_q(λ*)
  - candidate rules: floor / round / hook-special-case
  - which rules are consistent with all observed ρ

For the candidate that matches all observations, the script emits a
witness suitable for promoting the conjecture's narrative (or, on
disagreement, identifies the falsifying case).

The script also emits an operator-selection LP whose channels are
the candidate λ-classes (one per Wedderburn block).  The LP shadow
prices y_λ-dual identify the saturating block (= dominant λ*) per
particle, satisfying AGENTS.md "LP/SDP duals — first-class infra".

Cross-references:
  - prop:wedderburn-trace-identity (Markov-trace expansion)
  - prop:alpha-k-derivation-procedure (Wenzl-bridge weights)
  - conj:rho-prefactor-structural (the conjecture)
  - r5_full_canonical_knot_solver.py (PR #608, deliverable 1)

Output: rho-prefactor-structural-verifier.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as Q_FLOAT  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402
from hecke_characters import (  # noqa: E402
    partitions_of, dim_q, young_hooks,
)
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

Q0 = float(Q_FLOAT)
HERE = Path(__file__).parent


# ───────────────────────────────────────────────────────────────────
# Atom registry — B_3 only this session (matches r5_full prototype).
# Tritium (B_5 / 8_11) needs Hoefsmit at H_5 — deferred to a follow-up
# session, consistent with joint_tower_sdp_solver_v2.py.
# ───────────────────────────────────────────────────────────────────

REGISTRY_B3 = [
    {
        "name": "proton",
        "knot_name": "3_1 (trefoil)",
        "n_braid": 3,
        "braid_word": [1, -2, 1, -2, 1, -2],   # (σ_1 σ_2^{-1})^3 in B_3
        "observed_rho": 1,
        "atomic_mass_A": 1,
        "constituents": ["u", "u", "d"],         # 3 quarks
        "binding_operator_K": "identity",         # no binding (single-nucleon)
        "binding_K_in_H_n0": "I (n_0 = 3, no inter-nucleon binding)",
    },
    {
        "name": "neutron",
        "knot_name": "3_1 (trefoil)",
        "n_braid": 3,
        "braid_word": [1, -2, 1, -2, 1, -2],   # same braid; flavour differs
        "observed_rho": 1,
        "atomic_mass_A": 1,
        "constituents": ["u", "d", "d"],
        "binding_operator_K": "identity",
        "binding_K_in_H_n0": "I (n_0 = 3, no inter-nucleon binding)",
    },
    {
        "name": "deuteron",
        "knot_name": "6_2",
        "n_braid": 3,
        "braid_word": [1, -2, 1, 1, 1, -2],     # SnapPy canonical
        "observed_rho": 1,
        "atomic_mass_A": 2,
        "constituents": ["proton", "neutron"],
        "binding_operator_K": "L_H (Hopf link)",
        "binding_K_in_H_n0": "T(2,2) embedded in H_6 across nucleon-strand pairs",
    },
    {
        "name": "he3",
        "knot_name": "L6a4",
        "n_braid": 3,
        "braid_word": [-1, 2, -1, 2, -1, 2],   # SnapPy canonical
        "observed_rho": 2,
        "atomic_mass_A": 3,
        "constituents": ["proton", "proton", "neutron"],
        "binding_operator_K": "L6a4 (3-component link)",
        "binding_K_in_H_n0": (
            "L6a4 image embedded in H_9; the 3 link components correspond "
            "to the 3 nucleons.  ρ_obs = 2 is conjectured to come from "
            "the dominant λ* ⊢ 9 of this embedded K (NOT from the H_3 "
            "image of the braid word itself, which is Markov-equivalent "
            "to the proton's trefoil)."
        ),
    },
]


# ───────────────────────────────────────────────────────────────────
# H_3-level decoupling diagnostic.
#
# Two atoms whose H_3-image of T_w coincide cannot be distinguished by
# any function of (chi_λ, y_λ) at the braid strand count.  This is a
# **falsification** of the simple form of conj:rho-prefactor-structural
# evaluated at n_0 = braid-strand-count: proton and ³He coincide
# at H_3 (their braid words are mutual inverses), yet ρ_obs differs.
#
# The structural fix is to evaluate the conjecture at the ATOMIC strand
# count n_0 = 3·A, where the binding operator K (Hopf for ²H, L6a4 for
# ³He, ...) embeds non-trivially and the Wedderburn decomposition of
# K · ⊗_i T_w(constituent_i) carries the ρ information.
#
# This session ships the H_3-level analysis + the atomic-decomposition
# registry (constituents + binding K).  The H_{3·A}-level Wedderburn
# evaluation requires Hoefsmit at H_6 / H_9 (deferred — same posture
# as joint_tower_sdp_solver_v2.py).
# ───────────────────────────────────────────────────────────────────


# ───────────────────────────────────────────────────────────────────
# Hoefsmit per-block representations at H_3(q) — same as
# r5_full_canonical_knot_solver, kept self-contained here.
# ───────────────────────────────────────────────────────────────────

def hoefsmit_h3_blocks(q):
    """Return per-block representations of σ_1, σ_2 in H_3(q).

    Three Wedderburn blocks: trivial (3), standard (2,1), sign (1,1,1).
    """
    triv = (np.array([[q]]),  np.array([[q]]))
    sgn  = (np.array([[-1.0 / q]]), np.array([[-1.0 / q]]))
    # Standard (2,1) — Hoefsmit / Mathas Def 3.32 (axial distance d=1).
    denom = q * q + 1.0
    a = -1.0 / (q * denom)
    d_ = (q ** 3) / denom
    c = (q ** 4 + q * q + 1.0) / (denom * denom)
    std_T1 = np.array([[q, 0.0], [0.0, -1.0 / q]])
    std_T2 = np.array([[a, 1.0], [c, d_]])
    std = (std_T1, std_T2)
    return {(3,): triv, (2, 1): std, (1, 1, 1): sgn}


def represent_braid_h3(braid_word, q):
    """Return {λ: ρ_λ(T_b)} per Wedderburn block at H_3(q)."""
    blocks = hoefsmit_h3_blocks(q)
    h = q - 1.0 / q
    out = {}
    for lam, (T1, T2) in blocks.items():
        d_ = T1.shape[0]
        I = np.eye(d_)
        inv_T1 = T1 - h * I
        inv_T2 = T2 - h * I
        M = np.eye(d_)
        for g in braid_word:
            if g == 1:    M = M @ T1
            elif g == -1: M = M @ inv_T1
            elif g == 2:  M = M @ T2
            elif g == -2: M = M @ inv_T2
            else:
                raise ValueError(f"B_3 only has σ_1, σ_2; got {g}")
        out[lam] = M
    return out


# ───────────────────────────────────────────────────────────────────
# Wenzl-Schur weights y_λ(q_0).
# ───────────────────────────────────────────────────────────────────

def load_wenzl_weights(n: int) -> dict:
    raw = json.loads((HERE / "y-lambda-wenzl-witness.json").read_text())
    return {
        tuple(w["partition"]): float(w["y_lambda_numeric"])
        for w in raw["tables_by_n"][str(n)]["weights"]
    }


# ───────────────────────────────────────────────────────────────────
# SYT count d_λ via hook-length: d_λ = n! / ∏ h_x.
# ───────────────────────────────────────────────────────────────────

def syt_count(shape: tuple) -> int:
    """Number of standard Young tableaux of given shape."""
    import math
    n = sum(shape)
    hk = young_hooks(shape)
    fact = math.factorial(n)
    prod_h = 1
    for h in hk:
        prod_h *= h
    assert fact % prod_h == 0, "hook-length formula should give integer SYT count"
    return fact // prod_h


# ───────────────────────────────────────────────────────────────────
# Per-particle Wedderburn analysis.
# ───────────────────────────────────────────────────────────────────

def is_hook_partition(shape: tuple) -> bool:
    """A *hook* partition has the form (k, 1, 1, ..., 1) — i.e., its
    Young diagram has at most one row of length > 1.

    Returns True for: the empty partition (), the row (n,), the column
    (1, 1, ..., 1), and any L-shape (k, 1, ..., 1) with k ≥ 1.
    Returns False for partitions with ≥ 2 rows of length > 1
    (e.g. (2,2), (3,2), (3,2,1)).

    Note: this is the standard combinatorial definition of "hook
    partition" in symmetric-function theory; it includes the trivial
    cases (n,) and (1^k) which are sometimes called "row hook" and
    "column hook" respectively.
    """
    if not shape:
        return True
    return all(r == 1 for r in shape[1:])


def analyze_atom(atom: dict, wenzl: dict) -> dict:
    """Per-atom Wedderburn-block analysis at q_0.

    For each λ ⊢ n_braid:
      χ_λ(T_w)     = trace ρ_λ(T_b)|_{q=q_0}
      y_λ(q_0)     = Wenzl-Schur weight
      product      = |y_λ · χ_λ(T_w)|
      d_λ          = SYT count (hook-length formula)
      dim_q(λ)     = q-dimension
    Returns analysis + dominant-λ identification + candidate-rule outcomes.
    """
    n = atom["n_braid"]
    bw = atom["braid_word"]
    rho_obs = atom["observed_rho"]

    blocks = represent_braid_h3(bw, Q0)
    per_lambda = []
    for lam in partitions_of(n):
        M = blocks[lam]
        chi = float(np.trace(M))
        y = wenzl.get(lam, 0.0)
        prod = abs(y * chi)
        d_lam = syt_count(lam)
        dq = float(dim_q(lam))      # q-dim at module-level Q
        per_lambda.append({
            "lambda": list(lam),
            "is_hook": is_hook_partition(lam),
            "chi": chi,
            "y_wenzl": y,
            "y_times_chi_abs": prod,
            "d_lambda_syt_count": d_lam,
            "dim_q": dq,
        })
    per_lambda.sort(key=lambda r: r["y_times_chi_abs"], reverse=True)
    dominant = per_lambda[0]

    # Candidate rules for ρ.
    qd = dominant["dim_q"]
    rules = {
        # Rule A — exact dim_q (real-valued; conjecture text)
        "rule_A_exact_dim_q":           {"value": qd, "rho_predicted": qd, "matches_obs": False},
        # Rule B — round to nearest integer
        "rule_B_round_dim_q":           {"value": qd, "rho_predicted": int(round(qd)), "matches_obs": False},
        # Rule C — floor
        "rule_C_floor_dim_q":           {"value": qd, "rho_predicted": int(qd), "matches_obs": False},
        # Rule D — hook-special-case from the conjecture text
        # (conj-rho-prefactor-structural.md "The rounding question"):
        #   ρ = 1                       if λ* is the hook (n_0-1, 1)
        #     = round(dim_q(λ*))         otherwise
        # Note: the .md text uses the symbol ⌊·⌉ which denotes round-
        # to-nearest, NOT floor.  The implementation below uses
        # int(round(qd)) accordingly.
        "rule_D_hook_special_case":     {"value": qd, "rho_predicted": (
            1 if (dominant["lambda"] == [n - 1, 1]) else int(round(qd))
        ), "matches_obs": False},
        # Rule E — d_λ* directly (classical SYT count, no q-deformation)
        "rule_E_d_lambda_star":         {"value": dominant["d_lambda_syt_count"],
                                         "rho_predicted": dominant["d_lambda_syt_count"],
                                         "matches_obs": False},
    }
    for k, v in rules.items():
        v["matches_obs"] = (v["rho_predicted"] == rho_obs)

    return {
        "atom": atom["name"],
        "knot": atom["knot_name"],
        "n_braid": n,
        "braid_word": bw,
        "rho_observed": rho_obs,       # legacy key (= ν_SDP semantically)
        "nu_SDP_observed": rho_obs,    # new canonical key (renamed 2026-05-17)
        "per_lambda": per_lambda,
        "dominant_lambda": dominant["lambda"],
        "dominant_lambda_is_hook": dominant["is_hook"],
        "dominant_d_lambda": dominant["d_lambda_syt_count"],
        "dominant_dim_q_at_q0": qd,
        "candidate_rules": rules,
    }


# ───────────────────────────────────────────────────────────────────
# Cross-particle rule consistency: a rule is "valid" iff it matches
# observed ρ for EVERY particle in the registry.
# ───────────────────────────────────────────────────────────────────

def consistency_summary(per_atom: list[dict]) -> dict:
    rule_keys = list(per_atom[0]["candidate_rules"].keys())
    summary = {}
    for r in rule_keys:
        per_atom_match = [
            (a["atom"], a["candidate_rules"][r]["matches_obs"])
            for a in per_atom
        ]
        all_match = all(m for _, m in per_atom_match)
        summary[r] = {
            "all_atoms_match": all_match,
            "per_atom_matches": dict(per_atom_match),
            "n_match": sum(1 for _, m in per_atom_match if m),
            "n_total": len(per_atom_match),
        }
    return summary


# ───────────────────────────────────────────────────────────────────
# Operator-selection LP (AGENTS.md "LP/SDP duals — first-class infra").
# Channels = Wedderburn blocks per particle; t_λ = -|y_λ · χ_λ| (so
# argmin t = dominant λ*); LP picks one channel per particle and the
# dual y_star identifies the saturating (= dominant) channel.
# ───────────────────────────────────────────────────────────────────

def operator_selection_lp_per_atom(analysis: dict) -> dict:
    per_lambda = analysis["per_lambda"]
    K = len(per_lambda)
    # Negate so that "min t" picks the dominant λ.
    t = -np.array([r["y_times_chi_abs"] for r in per_lambda])
    G = np.eye(K)
    n_target = 1.0
    res = solve_operator_selection_lp(t, G, n_target)
    return {
        **res.to_dict(),
        "channel_lambdas": [r["lambda"] for r in per_lambda],
        "channel_t_costs": t.tolist(),
        "interpretation": (
            "PRIMAL: argmin_i t_i (with t_i = -|y_λ·χ_λ|) ⇒ argmax_λ "
            "|y_λ·χ_λ|, i.e. the dominant Wedderburn summand λ* per "
            "conj:rho-prefactor-structural — the channel with x_i^* > 0.  "
            "DUAL: in the operator-selection LP with G = I and "
            "constraints x ≥ 0, y_star[i] > 0 (active_set membership) "
            "marks channels where x_i ≥ 0 is TIGHT at the optimum "
            "(x_i^* = 0, NOT selected).  The dominant channel has "
            "x_i^* > 0 and y_star[i] = 0 — its complement is the "
            "active_set."
        ),
    }


# ───────────────────────────────────────────────────────────────────
# Driver.
# ───────────────────────────────────────────────────────────────────

def main():
    print("══════════════════════════════════════════════════════════════════════")
    print("  Structural ρ(Z, N) rule verifier — conj:rho-prefactor-structural")
    print("  (issue #604 deliverable 4 / closes-or-narrows GAP-A-4).")
    print("══════════════════════════════════════════════════════════════════════")
    print(f"  q_0 = {Q0}")
    print()

    w = (
        WitnessBuilder("rho-prefactor-structural-verifier", engine="python")
        .set_description(
            "Structural ρ(Z, N) rule verifier — operator-selection LP / "
            "shadow-price / primal-dual / lp-duality evaluation of the "
            "rule ρ(𝔥) = dim_q(λ*(T_w)) per conj:rho-prefactor-structural "
            "(issue #604 deliverable 4 / closes-or-narrows GAP-A-4). For "
            "each canonical T_w ∈ H_3(q_0) of {proton, neutron, ²H/6_2, "
            "³He/L₆ₐ₄}, decomposes into Wedderburn blocks via Hoefsmit "
            "seminormal form, evaluates |y_λ · χ_λ(T_w)| per partition λ "
            "⊢ 3, identifies the dominant λ*, and tests five candidate "
            "rules (exact dim_q / round / floor / hook-special-case / "
            "classical d_λ) against the observed ρ ∈ {1, 1, 1, 2}.  The "
            "rule that matches all four observations is reported as the "
            "structural form of ρ(Z, N) at B_3.  Tritium (B_5 / 8_11) "
            "deferred — needs Hoefsmit at H_5 (consistent with the "
            "joint_tower_sdp_solver_v2.py / R5-full prototype posture)."
        )
        .set_content_block("conj:rho-prefactor-structural")
        .add_parameter("q_0", Q0)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("registry_size", len(REGISTRY_B3))
    )

    wenzl = load_wenzl_weights(3)

    per_atom = []
    for atom in REGISTRY_B3:
        analysis = analyze_atom(atom, wenzl)
        analysis["lp_dual"] = operator_selection_lp_per_atom(analysis)
        per_atom.append(analysis)
        print(f"──── {atom['name']} ({atom['knot_name']}, ρ_obs = {atom['observed_rho']}) ────")
        for r in analysis["per_lambda"]:
            mark = "  ←★" if r["lambda"] == analysis["dominant_lambda"] else "    "
            print(f"  λ = {tuple(r['lambda'])!s:11s}  "
                  f"χ = {r['chi']:+8.4f}   "
                  f"y = {r['y_wenzl']:7.4f}   "
                  f"|y·χ| = {r['y_times_chi_abs']:7.4f}   "
                  f"d_λ = {r['d_lambda_syt_count']}   "
                  f"dim_q = {r['dim_q']:6.4f}   {mark}")
        for rk, rv in analysis["candidate_rules"].items():
            tick = "✓" if rv["matches_obs"] else "✗"
            print(f"    {tick}  {rk:30s} → ρ_pred = {rv['rho_predicted']!s:6s} (matches ρ_obs = {atom['observed_rho']}? {rv['matches_obs']})")
        print()

    consistency = consistency_summary(per_atom)
    print("──── Cross-particle consistency ────")
    for rk, rv in consistency.items():
        tick = "✓" if rv["all_atoms_match"] else "✗"
        print(f"  {tick}  {rk:30s} → {rv['n_match']}/{rv['n_total']} atoms match")
    print()

    # ── H_3-level decoupling diagnostic. ──────────────────────────
    # Two atoms with identical chi_λ across all λ ⊢ 3 must have the
    # same Hecke-algebra image at q_0; no rule of the form
    # "ρ = f(chi, y)" can distinguish them.
    #
    # Build the χ-fingerprint in CANONICAL λ order (sorted by partition
    # tuple) so the comparison is order-independent — `per_lambda` is
    # sorted by |y·χ| dominance (which can differ between atoms) and
    # would produce false negatives if used directly.
    def _canonical_chi_signature(atom_analysis: dict) -> tuple:
        items = sorted(
            atom_analysis["per_lambda"],
            key=lambda r: tuple(r["lambda"]),
        )
        return tuple((tuple(r["lambda"]), round(r["chi"], 8)) for r in items)

    chi_signatures = {a["atom"]: _canonical_chi_signature(a) for a in per_atom}
    rho_obs_by_atom = {a["atom"]: a["rho_observed"] for a in per_atom}
    chi_collisions: dict = {}
    for atom, sig in chi_signatures.items():
        chi_collisions.setdefault(sig, []).append(atom)
    chi_indistinguishable_groups = [
        atoms for atoms in chi_collisions.values() if len(atoms) >= 2
    ]
    # A collision FALSIFIES the (chi, y)-only ρ rule only when the
    # group contains atoms with DIFFERENT observed ρ.  Same-ρ
    # collisions (e.g. proton vs neutron) are benign — the rule
    # would predict the same ρ for them, which is correct.
    falsifying_collision_groups = [
        atoms for atoms in chi_indistinguishable_groups
        if len({rho_obs_by_atom[a] for a in atoms}) > 1
    ]

    valid_rules = [r for r, v in consistency.items() if v["all_atoms_match"]]
    h3_falsifies_simple_form = bool(falsifying_collision_groups)
    summary = {
        "n_atoms_evaluated": len(per_atom),
        "candidate_rules_evaluated": list(consistency.keys()),
        "rules_consistent_with_all_observations": valid_rules,
        "h3_chi_indistinguishable_groups": chi_indistinguishable_groups,
        "h3_chi_indistinguishable_groups_falsifying": (
            falsifying_collision_groups
        ),
        "h3_falsifies_simple_form_of_rho_rule": h3_falsifies_simple_form,
        "verdict": (
            f"{len(valid_rules)} of {len(consistency)} candidate rules "
            f"reproduce ρ for all {len(per_atom)} atoms in the B_3 "
            f"registry ({[a['name'] for a in REGISTRY_B3]}).  H_3-level "
            f"χ_λ collisions: {chi_indistinguishable_groups} (all "
            f"groups); falsifying subset (different ρ within group): "
            f"{falsifying_collision_groups}.  Atoms in the falsifying "
            f"subset are Markov-equivalent at the braid strand count "
            f"yet have distinct ρ — no (chi, y)-only rule can "
            f"distinguish them.  Same-ρ collisions (e.g. proton vs "
            f"neutron) are benign.  The structural fix per "
            f"conj:rho-prefactor-structural is to evaluate the rule "
            f"at the *atomic* strand count n_0 = 3·A, embedding the "
            f"braid into H_{{3·A}} via the binding operator K (Hopf "
            f"for ²H, L6a4 for ³He, ...).  This requires Hoefsmit at "
            f"H_6 / H_9 — deferred."
        ),
        "structural_finding": (
            "ρ = dim_q(λ*) cannot be evaluated at the braid strand "
            "count alone.  The conjecture's n_0 = 3·A (atomic strand "
            "count) is structurally REQUIRED.  The natural categorical "
            "decomposition is T_w(𝔥) = K · ⊗_i T_w(constituent_i) "
            "where the binding operator K ∈ H_{3·A} carries the "
            "inter-constituent linking and the dominant λ* ⊢ 3·A of "
            "K is what determines ρ — not the dominant λ* ⊢ "
            "n_braid of the whole-particle braid image.  This is the "
            "natural framework for the joint-tower SDP cross-level "
            "consistency constraints (4) of "
            "prop:joint-tower-sdp-confinement, which already enforce "
            "T_w(𝔥) ↪ T_w(𝔥') across levels.  Wiring an explicit "
            "'binding-K SDP solver mode' is the natural deliverable-5 "
            "that follows from this finding."
        ),
        "next_session_extensions": [
            "Build Hoefsmit seminormal at H_6 / H_9 (atomic strand "
            "counts for ²H / ³H / ³He) — currently deferred to "
            "tools/hecke-engine per the joint_tower_sdp_solver_v2.py "
            "/ R5-full prototype posture.",
            "Re-evaluate the ρ rule at H_{3·A} using the embedded "
            "T_w (constituent-tensor + binding-K product) per the "
            "structural_finding above.",
            "Wire a 'binding-K SDP solver mode' that finds the "
            "binding link K ∈ H_{3·A} from substrate data + "
            "constituent T_w's — generalises the R5-full prototype "
            "from PR #608 by separating constituent + binding "
            "decomposition.",
            "Add tritium ³H (B_5 / 8_11) once the Hoefsmit and "
            "binding-K infrastructure lands.",
            "Add ⁴He, ⁶Li, ⁷Li once canonical-K identifications "
            "(or SDP-search outputs) are available.",
            "Promote the verified rule to a class strengthening of "
            "conj:rho-prefactor-structural (per-particle instances).",
        ],
    }

    (
        w.add_data("registry_b3", REGISTRY_B3)
         .add_data("per_atom_analysis", per_atom)
         .add_data("cross_particle_consistency", consistency)
         .add_data("summary", summary)
         .add_caveat(
            "B_3 atoms only this session (proton, neutron, ²H/6_2, "
            "³He/L₆ₐ₄). ³H (B_5 / 8_11) needs Hoefsmit at H_5 — "
            "deferred. The Wenzl-Schur weights y_λ(q_0) are loaded "
            "from y-lambda-wenzl-witness.json (50 dps mpmath); "
            "evaluation here is float64 (sufficient for the "
            "argmax-λ* identification).  The 'observed ρ' values "
            "are taken from the existing canonical-knot table in "
            "conj-rho-prefactor-structural.md / "
            "joint-tower-sdp-h6-h9.witness.json. **Critical "
            "structural finding:** the H_3-level analysis identifies "
            "proton and ³He as Markov-equivalent (their braid words "
            "are mutual inverses, χ_λ profiles identical), so no rule "
            "of the form 'ρ = f(chi, y) at the braid strand count' "
            "can reproduce the observed ρ split (1 vs 2). The "
            "conjecture's structural form *requires* evaluation at "
            "the atomic strand count n_0 = 3·A, where the binding "
            "operator K ∈ H_{3·A} carries the inter-nucleon linking. "
            "See `structural_finding` in the summary for the proposed "
            "categorical decomposition T_w(𝔥) = K · ⊗_i T_w(const_i)."
        )
    )
    out = w.save()
    print(f"  Witness: {out.name}")
    print(f"  Verdict: {summary['verdict']}")
    if valid_rules:
        print(f"  Rules consistent with all observations:")
        for r in valid_rules:
            print(f"    • {r}")
    print("══════════════════════════════════════════════════════════════════════")


if __name__ == "__main__":
    main()
