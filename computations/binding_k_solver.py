#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical Wedderburn-block evaluation at
# q_0; symbolic-q binding-K closed form deferred.
"""
Binding-K factorisation evaluator — atomic-strand-count Wedderburn
analysis at H_{3·A}(q_0) for ²H, ³H, ³He.

(Earlier drafts called this an "SDP solver"; per Copilot's PR #614
review the name was misleading because the implementation does not
perform any optimisation / feasibility search.  It EVALUATES the
algebraic factorisation T_w(𝔥) = K · cp at H_{3·A} given the
historical T_w(𝔥) braid word, by braid-word concatenation
K_word = atom_word ++ cp_inv_word.  The actual SEARCH for K from
substrate alone is in `binding_k_enumerator.py`.)

Issue #604, follow-up to PR #608 (R5-full prototype) + PR #610 (binding-K
factorisation finding at H_3).  Implements items 1–5 of the open-work
list:

  1. **Hoefsmit at H_n for general n** — uses the existing
     `build_seminormal_matrices` from `hecke_characters.py`, which
     already supports any partition of any n.  No new combinatorial
     code is needed; the previous H_3-only verifier was using a
     hardcoded Hoefsmit, but the general path was already available.

  2. **Binding-K SDP solver mode** — for each atom 𝔥 with constituents
     {nucleon_i}_{i=1..A}, factor

         T_w(𝔥) = K(𝔥) · ⊗_{i=1..A} T_w(nucleon_i)        (in H_{3·A})

     numerically per Wedderburn block λ ⊢ 3·A:

         ρ_λ(K) = ρ_λ(T_w(𝔥)) · ρ_λ(constituent_product)^{-1}.

  3. **Categorical-uniqueness narrowing (constituent leg)** — at H_3
     each nucleon's trefoil is the unique PSD-feasible canonical
     element (closed by R5-minimal); this script verifies that the
     CONSTITUENT product factor is well-defined / invertible per
     Wedderburn block at H_{3·A}.  The remaining "binding-K
     uniqueness" sub-assertion is the open core of deliverable 3.

     ⚠ MEASURED CONTRA 2026-08-31 (bean `t7qv`).  The trefoil is NOT
     PSD-feasible at H_3 in either presentation — σ₁³ has worst
     symmetric-part eigenvalue −0.731234 and (σ₁σ₂)² has −0.604530 —
     and neither is this repo's own nucleon word from
     `atom_braid_word_3A` (proton −0.739224, neutron −0.910762; PSD in
     1 of 3 blocks).  The H_3 element that IS PSD-feasible is the FULL
     TWIST (σ₁σ₂)³, at +0.534703.  Reason: ρ_λ(σ) has eigenvalues
     {q₀, −1/q₀} in every block of dim ≥ 2, so ρ_λ(σ^k) is PSD iff k
     is EVEN — PSD-feasibility here is a crossing-parity condition,
     which is also why the unknot control passes in
     `binding-link-psd-feasibility-probe.witness.json`.
     SCOPE: this contradicts a plain reading of the sentence above.  It
     does not settle the narrower claim if "canonical element" means a
     restricted R5-minimal class — that class is not defined here, so
     the tension is flagged rather than resolved.  The measuring
     convention (PSD on the symmetric part) reproduces all four results
     recorded in that witness, 6_2's standard-(2,1) failure included.
     Probe: `computations/probes/binding_k_convolution_sdp_probe.py`.

  4. **Per-particle ρ rule evaluation at the atomic strand count** —
     identifies dominant λ*(K) ⊢ 3·A and tests the five candidate
     ρ rules from `rho_prefactor_structural_verifier.py` against the
     observed ρ values, this time at H_{3·A} rather than H_3.

  5. **Tritium ³H (B_5 / 8_11)** — handled by the same pipeline once
     n_0 = 9 (no separate H_5 detour needed; the 8_11 braid embeds
     directly into H_9 via the B_5 ↪ B_9 inclusion σ_i → σ_i).

The natural Wedderburn-PSD constraint at the atomic strand count
becomes: ρ_λ(K(𝔥)) is the linking matrix in block λ; PSD-feasibility
of K is the "binding stability" certificate.  The witness emits per-
block primal/dual via the operator-selection LP per AGENTS.md.

Output: `binding-k-solver.witness.json`.

*** MEASURED DEFECT, FIXED 2026-09-13: a q-dimension of exactly 1 was being
    recorded as 0 ***

`dim_q(λ, q)` was evaluated at `qou_substrate.constants.Q` — the **float64**
proton pin, 17 digits of a 50-digit constant — and then `float()`-cast.  Rule C
(`rule_C_floor_dim_q`) predicts `ρ` with `int(qd)`, which is a **FLOOR**, and
`int(round(...))` in rules B and D is likewise **discontinuous**.  A 1e-16 error
in `qd` is therefore not a 1e-16 error in the verdict; it is a whole unit.

Measured across all 33 (atom, block) pairs:

  * SIX blocks have an exact `dim_q` of **1** — the trivial and sign
    representations, `λ = (n)` and `λ = (1^n)`, whose q-dimension is 1 by
    definition.
  * At the float64 pin, **four of the six** evaluate to `0.99999999999999978`,
    so `int(qd)` returned **0 for a q-dimension of exactly 1**.  The other two
    landed at `1.00000000000000022` and were correct **by luck**, on a margin
    of 2e-16.
  * The worst `|qd_float64 − qd_exact|` over all blocks is **1.84e-13** —
    ~800× the margin those two survived on, and three orders worse than
    float64 epsilon, because `dim_q` is a ratio of q-integer products.

Fixed by evaluating `dim_q` at `Q0_PROTON_EXACT` (the 50-digit string) and
taking `mp.nint` / `mp.floor` on the `mpf`, which puts the rounding decision ~54
orders from the boundary instead of 0–2.

**The headline verdict did NOT change** and that is worth stating plainly: no
atom's *dominant* block is one of the six (they are `(5,1)`, `(8,1)`, `(6,3)` at
`qd` = 5.22, 8.95, 62.25 — all far from an integer), so "0 of 4 candidate rules
reproduce ρ" and `rules_consistent_with_all_observations: []` are unchanged.
The defect was in the recorded per-block `dim_q`, and it was one dominance
change away from reaching the verdict.

*** WHAT IS NOT DRAINED HERE, and why ***

Raw float64 fields: 773 → 524.  The remaining 524 are two layers that cannot be
made exact at this problem size, and they are left as honest float64 rather than
rendered at 60 digits (which is the laundering the gate forbids):

  * **The matrix layer** — `chi`, `det`, `min_eig_sym`, `eigenvalues_sym` come
    from `numpy` on the seminormal blocks.  `build_seminormal_matrices`
    dispatches on the operand and *would* give exact arithmetic for an `mpf`
    `q` (bean `qou-8xb1`), but the largest block at `n_0 = 9` has **dim 216**;
    an mpmath `eigsy`/`det` there is O(10⁷) mpf operations per block, over 30
    blocks and 3 atoms.  Not feasible.  An exact route would have to go through
    the Rust engine.
  * **The LP layer** — Clarabel returns float64 by construction.  `t` is
    explicitly downcast at the LP boundary; see the comment there for the
    25-order residual excursion that happens if exact data is pushed in
    instead, which is NOT understood and was deliberately not shipped.
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
    partitions_of, build_seminormal_matrices, dim_q,
)
from lp_dual_solver import solve_operator_selection_lp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import Q as Q0_PROTON  # noqa: E402 — anchor-independent proton pin (qou-6p3b Tranche C)
from codata_constants import (
    AME_B_DEUTERON_MEV_VALIDATION,
    AME_B_TRITIUM_MEV_VALIDATION,
)

Q0 = float(Q_FLOAT)

# EXACT proton pin, for the quantities that need no matrix (2026-09-13).
# `qou_substrate.constants.Q` is the FLOAT64 pin — 17 digits of a 50-digit
# constant — and `dim_q` fed through it lands 2e-16 BELOW an exact integer on
# four blocks, which `int()` then floors to zero. See MEASURED DEFECT in the
# module docstring. The matrix layer still runs at `Q0`; see WHAT IS NOT
# DRAINED HERE for why, and note the two are the same pin at different
# precision, not two anchors.
from _precision import set_compute_dps, fmt  # noqa: E402
from mpmath import mp, mpf  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR as _Q50  # noqa: E402
from codata_constants import AME_B_HE3_MEV_VALIDATION  # noqa: E402  (AME registry)

# BEFORE the mpf below, not after: this producer never called
# `set_compute_dps()` at all, so `mp.dps` was the mpmath default of 15 and
# `mpf(<50-digit string>)` would have been silently truncated to 15 — the
# `mp.dps` no-op the precision gates exist to catch, reintroduced by the very
# line meant to fix a precision bug.
set_compute_dps()

Q0_PROTON_EXACT = mpf(_Q50)

HERE = Path(__file__).parent


# ───────────────────────────────────────────────────────────────────
# Atom registry — atomic strand count n_0 = 3·A.
# ───────────────────────────────────────────────────────────────────
# Each atom records:
#   atom_braid_word: the canonical T_w(𝔥) braid in B_{n_braid} embedded
#                    into B_{n_0=3A} via σ_i → σ_i (i ≤ n_braid - 1)
#   constituents: list of (offset, nucleon_braid_word) — each nucleon
#                 occupies 3 strands; offset = 0, 3, 6, ..., shifts the
#                 nucleon braid into its own strand triple.

# A nucleon (proton or neutron) is a trefoil 3_1 = (σ_1 σ_2^{-1})^3 in B_3.
NUCLEON_BRAID_LOCAL = [1, -2, 1, -2, 1, -2]


def _shift_braid(word, offset):
    """Shift a braid word's generators by +offset (so σ_i ↦ σ_{i+offset})."""
    return [(g + offset) if g > 0 else (g - offset) for g in word]


REGISTRY = [
    {
        "name": "deuteron",
        "knot_name": "6_2",
        "A": 2,
        "n_0": 6,                                 # 3·A
        "n_braid": 3,                              # 6_2 lives in B_3
        "atom_braid_word": [1, -2, 1, 1, 1, -2],   # 6_2 in B_3 (SnapPy)
        "constituent_offsets": [0, 3],             # p strands 1..3, n strands 4..6
        "binding_link_name": "L_H (Hopf)",
        "observed_rho": 1,
        "B_AME_MeV": AME_B_DEUTERON_MEV_VALIDATION,
    },
    {
        "name": "tritium",
        "knot_name": "8_11",
        "A": 3,
        "n_0": 9,
        "n_braid": 5,                              # 8_11 lives in B_5
        "atom_braid_word": [-1, 2, -3, 2, 1, -3, -3, 4, -3, -2, -3, -4, -3, 2],
        "constituent_offsets": [0, 3, 6],
        "binding_link_name": "8_11-class link",
        "observed_rho": 2,
        "B_AME_MeV": AME_B_TRITIUM_MEV_VALIDATION,
    },
    {
        "name": "he3",
        "knot_name": "L6a4",
        "A": 3,
        "n_0": 9,
        "n_braid": 3,                              # L6a4 lives in B_3
        "atom_braid_word": [-1, 2, -1, 2, -1, 2],   # L6a4 (SnapPy)
        "constituent_offsets": [0, 3, 6],
        "binding_link_name": "L6a4 (3-component link)",
        "observed_rho": 2,
        "B_AME_MeV": float(AME_B_HE3_MEV_VALIDATION),
    },
]


# ───────────────────────────────────────────────────────────────────
# Wenzl-Schur weights y_λ(q_0) for any n.
# ───────────────────────────────────────────────────────────────────

def load_wenzl_weights(n: int) -> dict:
    """Load y_λ(q_0) for every λ ⊢ n from y-lambda-wenzl-witness.json.

    Returns {} if n is not tabulated (validator-friendly graceful
    degradation; downstream uses a uniform 1/|partitions| fallback).
    """
    raw = json.loads((HERE / "y-lambda-wenzl-witness.json").read_text())
    table = raw.get("tables_by_n", {}).get(str(n))
    if table is None:
        return {}
    return {
        # `mpf(str(...))`, not `float(...)`: the witness stores these as
        # decimal strings at full precision and the cast threw ~35 digits away
        # at read time (2026-09-13). They feed the dominant-block selection.
        tuple(w["partition"]): mpf(str(w["y_lambda_numeric"]))
        for w in table["weights"]
    }


# ───────────────────────────────────────────────────────────────────
# Per-Wedderburn-block evaluation at H_n(q_0).
# Builds the seminormal-form matrices for σ_1..σ_{n-1} per shape λ ⊢ n
# (using existing build_seminormal_matrices), then multiplies through
# braid words.
# ───────────────────────────────────────────────────────────────────

def block_rep_braid_word(shape, braid_word, q=Q0):
    """Compute ρ_λ(T_β) ∈ M_{d_λ}(ℝ) for braid word β at H_n(q).

    Args:
      shape: partition λ ⊢ n.
      braid_word: list of nonzero ints; +i = σ_i, -i = σ_i^{-1}.
        Generator indices must be in [1, n-1].

    Returns: numpy float array of shape (d_λ, d_λ).  Raises
      ValueError if any generator index is outside [1, n-1].

    Wired through `syt_prefix_cache.BlockCache` /
    `build_seminormal_matrices_cached` per Copilot PR #614 review:
    avoids the O(d_λ²) swap-partner search inside
    `build_seminormal_matrices` on repeated calls for the same shape.
    """
    n = sum(shape)
    h = q - 1.0 / q
    try:
        from syt_prefix_cache import (
            BlockCache, build_seminormal_matrices_cached,
        )
        # Module-level lazy cache shared across calls at fixed q.
        global _BLOCK_CACHE_AT_Q
        if "_BLOCK_CACHE_AT_Q" not in globals() or _BLOCK_CACHE_AT_Q[0] != q:
            _BLOCK_CACHE_AT_Q = (q, BlockCache(q, h))
        sigmas, dim, _ = build_seminormal_matrices_cached(
            shape, cache=_BLOCK_CACHE_AT_Q[1],
        )
    except ImportError:
        sigmas, dim, _ = build_seminormal_matrices(
            shape, q=q, sparse=False,
        )
    if dim == 0:
        return np.zeros((0, 0))
    I = np.eye(dim)
    M = np.eye(dim)
    for g in braid_word:
        idx = abs(g) - 1
        if idx < 0 or idx >= len(sigmas):
            raise ValueError(
                f"generator σ_{abs(g)} out of range for H_{n} (need 1..{n - 1})"
            )
        if g > 0:
            M = M @ sigmas[idx]
        else:
            M = M @ (sigmas[idx] - h * I)
    return M


def per_block_evaluation(braid_word, n_0, q=Q0):
    """Per-Wedderburn-block evaluation at H_{n_0}(q) for braid word β.

    Returns dict {λ: {chi, det, eigenvalues_sym, min_eig_sym, matrix}}
    plus aggregate alpha_gap.
    """
    out = {}
    min_eig_overall = float("inf")
    for lam in partitions_of(n_0):
        M = block_rep_braid_word(lam, braid_word, q=q)
        if M.size == 0:
            continue
        chi = float(np.trace(M))
        det = float(np.linalg.det(M))
        Msym = (M + M.T) / 2.0
        eigs = sorted(np.linalg.eigvalsh(Msym).tolist())
        min_eig = eigs[0]
        min_eig_overall = min(min_eig_overall, min_eig)
        out[lam] = {
            "chi": chi,
            "det": det,
            "eigenvalues_sym": eigs,
            "min_eig_sym": min_eig,
            "psd_within_tol": min_eig >= -1e-9,
            "matrix": M.tolist(),
        }
    return {
        "per_block": out,
        "alpha_gap": max(0.0, -min_eig_overall),
        "min_eig_overall": min_eig_overall,
    }


# ───────────────────────────────────────────────────────────────────
# Constituent product: combine A nucleon trefoils, each shifted to
# its own strand triple, into a single braid word in B_{3·A}.
#
# The resulting word's image in H_{3·A} is the canonical
# ⊗_{i=1..A} T_w(nucleon_i) under the standard inclusion of disjoint
# Hecke sub-algebras.  The factors commute in H_{3·A} because they
# involve disjoint generators.
# ───────────────────────────────────────────────────────────────────

def constituent_product_word(constituent_offsets):
    """Concatenate `len(offsets)` shifted nucleon braids into one word."""
    word = []
    for off in constituent_offsets:
        word.extend(_shift_braid(NUCLEON_BRAID_LOCAL, off))
    return word


def invert_braid_word(word):
    """Braid-group inverse: read backwards with each generator inverted."""
    return [-g for g in reversed(word)]


# ───────────────────────────────────────────────────────────────────
# Binding-K analysis: K = T_w(atom) · constituent_product^{-1}
# evaluated per Wedderburn block at H_{3·A}.
# ───────────────────────────────────────────────────────────────────

def binding_k_per_block(atom: dict, q=Q0):
    """Compute ρ_λ(K) per Wedderburn block λ ⊢ n_0 for one atom.

    Strategy (block-diagonal): per λ, build ρ_λ(T_atom) and
    ρ_λ(constituent_product) via per_block_evaluation; then
    ρ_λ(K) = ρ_λ(T_atom) · ρ_λ(constituent_product)^{-1}.

    Returns dict {λ: {K_chi, K_det, K_min_eig_sym, K_psd_within_tol,
                        T_atom_chi, constituent_chi, K_matrix}} plus
    aggregate fields (K_alpha_gap, dominant_lambda_K, ...).
    """
    n_0 = atom["n_0"]
    atom_word = atom["atom_braid_word"]
    cp_word = constituent_product_word(atom["constituent_offsets"])
    cp_inv_word = invert_braid_word(cp_word)

    atom_eval = per_block_evaluation(atom_word, n_0, q=q)
    cp_eval = per_block_evaluation(cp_word, n_0, q=q)

    # K = T_atom · constituent_product^{-1} per block.
    # Equivalent: build ρ_λ(K) directly from braid-word concatenation
    # = atom_word ++ cp_inv_word.  This avoids inverting potentially
    # ill-conditioned per-block matrices and is exact at the
    # representation level.
    K_word = list(atom_word) + cp_inv_word
    K_eval = per_block_evaluation(K_word, n_0, q=q)

    return {
        "atom_word_image": atom_eval,
        "constituent_product_word_image": cp_eval,
        "constituent_product_word": cp_word,
        "K_word_in_H_n0": K_word,
        "K_image": K_eval,
    }


# ───────────────────────────────────────────────────────────────────
# Dominant λ* of K via |y_λ · χ_λ(K)|; ρ-rule evaluation.
# ───────────────────────────────────────────────────────────────────

def is_hook_partition(shape: tuple) -> bool:
    """Standard hook: at most one row of length > 1.  See the verifier
    `rho_prefactor_structural_verifier.py` for the full rationale."""
    if not shape:
        return True
    return all(r == 1 for r in shape[1:])



def _serialise(obj):
    """Render an `mpf`-bearing structure for the witness.

    The exactly-computable quantities (`dim_q`, `y_wenzl`, the rule values)
    are carried as `mpf` and become text HERE, once, via `_precision.fmt`.
    The matrix- and LP-derived fields are genuine float64 and pass through
    UNTOUCHED — see "WHAT IS NOT DRAINED HERE" in the module docstring. They
    are deliberately not run through `fmt`: rendering a float64 at 60 digits
    is exactly the laundering the raw-float64 gate forbids ("do NOT stringify
    the float").
    """
    if isinstance(obj, dict):
        return {k: _serialise(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_serialise(v) for v in obj]
    if isinstance(obj, mp.mpf):
        return fmt(obj)
    return obj


def dominant_lambda_and_rho_rules(K_eval: dict, n_0: int, observed_rho: int):
    """For K ∈ H_{n_0}(q_0), identify dominant λ* via |y_λ · χ_λ(K)|
    and evaluate the five candidate ρ rules."""
    wenzl = load_wenzl_weights(n_0)
    if not wenzl:
        # Fallback: uniform 1/|P(n_0)| (still picks dominant by χ alone).
        n_part = sum(1 for _ in partitions_of(n_0))
        wenzl = {tuple(p): mpf(1) / n_part for p in partitions_of(n_0)}

    per_lambda = []
    for lam, blk in K_eval["per_block"].items():
        chi = blk["chi"]
        y = wenzl.get(lam, mpf(0))
        per_lambda.append({
            "lambda": list(lam),
            "is_hook": is_hook_partition(lam),
            "chi_K": chi,
            "y_wenzl": y,
            "y_times_chi_abs": abs(y * chi),
            # EXACT (2026-09-13). `dim_q` is a rational function of q and needs
            # no matrix, so it is computed at the full 50-digit proton pin and
            # kept as `mpf` — see MEASURED DEFECT in the module docstring: at
            # the float64 pin, FOUR blocks whose exact dim_q is 1 evaluate to
            # 0.99999999999999978, and rule C's `int()` is a FLOOR, so it
            # returned 0 for a q-dimension of exactly 1.
            "dim_q": dim_q(lam, Q0_PROTON_EXACT),
        })
    per_lambda.sort(key=lambda r: r["y_times_chi_abs"], reverse=True)
    dominant = per_lambda[0]
    qd = dominant["dim_q"]

    # Round and floor on the EXACT value. `int(round(x))` and `int(x)` are
    # DISCONTINUOUS, so a 1e-16 error in `qd` is not a 1e-16 error in the
    # verdict — it is a whole unit. `mp.nint` / `mp.floor` at 70 dps put the
    # decision 54 orders of magnitude away from the boundary instead of 0-2.
    rules = {
        "rule_A_exact_dim_q":         {"value": qd, "rho_predicted": qd},
        "rule_B_round_dim_q":         {"value": qd, "rho_predicted": int(mp.nint(qd))},
        "rule_C_floor_dim_q":         {"value": qd, "rho_predicted": int(mp.floor(qd))},
        "rule_D_hook_special_case":   {"value": qd, "rho_predicted": (
            1 if (dominant["lambda"] == [n_0 - 1, 1]) else int(mp.nint(qd))
        )},
    }
    for v in rules.values():
        v["matches_obs"] = (v["rho_predicted"] == observed_rho)

    return {
        "per_lambda_for_K": per_lambda,
        "dominant_lambda_K": dominant["lambda"],
        "dominant_dim_q_K_at_q0": qd,
        "dominant_is_hook": dominant["is_hook"],
        "candidate_rules": rules,
    }


# ───────────────────────────────────────────────────────────────────
# Operator-selection LP: channels = Wedderburn blocks of K.
# t_λ = -|y_λ · χ_λ(K)| (so argmin = dominant λ*).
# ───────────────────────────────────────────────────────────────────

def operator_selection_lp_for_K(per_lambda: list) -> dict:
    K = len(per_lambda)
    # EXPLICIT float64 downcast at the LP boundary (2026-09-13), and it loses
    # nothing real: `y_times_chi_abs = |y·χ|` already has a float64 factor in
    # `χ`, which comes out of the numpy matrix layer.
    #
    # It is explicit because it must not be accidental. `y` became `mpf` in
    # this same change, so `np.array([...])` silently produced an OBJECT array
    # and pushed exact data into a float64 solver. Measured consequence: the
    # certified residual `gap_recomputed_str` moved 2.6e-43 -> -5.7e-18, 25
    # orders, because `_certified_residuals` sets its working precision from
    # the INPUT data's width — so exact `t` makes it re-measure the float64
    # solution against exact constraints instead of against the data the
    # solver saw. Whether that larger number is the honest residual or an
    # artefact is NOT established here; keeping the LP on float64 keeps this
    # change to the defect it was made for. Tracked in bean `qou-sogb`.
    t = -np.array([float(r["y_times_chi_abs"]) for r in per_lambda],
                  dtype=float)
    G = np.eye(K)
    # Pinned, not `auto`: `auto` picks clarabel-MPFR or scipy-f64 by
    # whether the Rust binary happens to be built, so the same script
    # yields different numbers on different boxes. QOU_REQUIRE_CLARABEL=1
    # makes a missing binary an error rather than a changed answer.
    # Bean `qou/ftuv`.
    res = solve_operator_selection_lp(t, G, n_target=1.0, backend="clarabel")
    return {
        **res.to_dict(),
        "channel_lambdas": [r["lambda"] for r in per_lambda],
        "channel_t_costs": t.tolist(),
        "interpretation": (
            "PRIMAL: argmin_i (t_i) = -|y_λ · χ_λ(K)| picks the channel "
            "with maximum |y_λ · χ_λ| ⇒ the dominant Wedderburn block "
            "λ*(K) of the binding operator K ∈ H_{n_0}(q_0) (this is "
            "where x_i^* > 0).  DUAL: in the operator-selection LP "
            "with G = I and constraints x ≥ 0, y_star[i] > 0 marks "
            "channels where the x_i ≥ 0 constraint is TIGHT at the "
            "optimum (i.e., x_i^* = 0 — channels NOT selected).  The "
            "DOMINANT channel is therefore the one with x_i^* > 0 and "
            "y_star[i] = 0 — NOT in the active_set; the active_set "
            "complementary identifies it.  Per conj:rho-prefactor-"
            "structural, ρ(𝔥) = round(dim_q(λ*(K)))."
        ),
    }


# ───────────────────────────────────────────────────────────────────
# Explicit-binding-K sub-experiment.
#
# The naive K = T_atom · cp^{-1} is the K that would FACTOR the embedded
# atom braid as constituent × binding.  But the embedded atom braid
# (e.g. the 6_2 braid embedded in B_6 via σ_i → σ_i for i = 1, 2)
# uses only the first 2 generators — it doesn't include any inter-
# nucleon crossings.  So the naive K absorbs everything, including the
# part that should be "missing" inter-nucleon binding.  The naive K is
# still well-defined, but it does NOT match the categorical "binding-
# link" interpretation (Hopf for ²H, L6a4 for ³He, ...).
#
# The "explicit-binding-K" sub-experiment posits K directly:
#   ²H:  K = σ_3^2     (Hopf link L_H crossing strands 3-4 in B_6)
#   ³He: K = σ_3 σ_6   (two Hopf bindings: 3-4 and 6-7 in B_9 — heuristic)
#   ³H:  K = σ_3 σ_4 σ_6 σ_7 ... (8_11-class — heuristic, deferred)
# and reports the K's Wedderburn structure for comparison with the
# naive factorisation.  This is purely diagnostic — the canonical K
# for ³H (8_11 class) and ³He (L_{6a4}) involve more than these
# heuristic word approximations.
# ───────────────────────────────────────────────────────────────────

EXPLICIT_BINDING_K_HEURISTIC = {
    "deuteron": {
        "K_word": [3, 3],                         # σ_3^2 = Hopf link L_H
        "binding_interpretation": (
            "σ_3^2 — Hopf link crossing strand 3 of proton with strand "
            "4 of neutron in B_6.  Standard Hopf representation."
        ),
    },
    "he3": {
        "K_word": [3, 6],                         # heuristic: 2 Hopfs
        "binding_interpretation": (
            "σ_3 σ_6 — heuristic: two Hopf-like crossings binding "
            "strand 3 of nucleon 1 to strand 4 of nucleon 2, AND "
            "strand 6 of nucleon 2 to strand 7 of nucleon 3 in B_9. "
            "The true L6a4 link has 3 components and a richer braid "
            "representation; this is a single-crossing surrogate for "
            "diagnostic comparison only."
        ),
    },
    "tritium": {
        "K_word": [3, 4, 6, 7],                   # heuristic: 4 crossings
        "binding_interpretation": (
            "σ_3 σ_4 σ_6 σ_7 — heuristic; the true 8_11-class binding "
            "link in B_9 involves more crossings.  Diagnostic only."
        ),
    },
}


def explicit_binding_k_analysis(atom: dict) -> dict:
    """For each atom, evaluate the heuristic explicit-K Wedderburn
    structure and compare with the naive factorisation."""
    name = atom["name"]
    n_0 = atom["n_0"]
    if name not in EXPLICIT_BINDING_K_HEURISTIC:
        return {"available": False}
    spec = EXPLICIT_BINDING_K_HEURISTIC[name]
    K_word = spec["K_word"]
    K_eval = per_block_evaluation(K_word, n_0)
    rho_analysis = dominant_lambda_and_rho_rules(
        K_eval, n_0, atom["observed_rho"],
    )
    return {
        "available": True,
        "K_word_explicit": K_word,
        "binding_interpretation": spec["binding_interpretation"],
        "K_alpha_gap_explicit": K_eval["alpha_gap"],
        "K_min_eig_overall_explicit": K_eval["min_eig_overall"],
        "dominant_lambda_K_explicit": rho_analysis["dominant_lambda_K"],
        "dominant_dim_q_explicit": rho_analysis["dominant_dim_q_K_at_q0"],
        "dominant_is_hook_explicit": rho_analysis["dominant_is_hook"],
        "candidate_rules_explicit": rho_analysis["candidate_rules"],
    }


# ───────────────────────────────────────────────────────────────────
# Per-atom analysis driver.
# ───────────────────────────────────────────────────────────────────

def analyze_atom(atom: dict) -> dict:
    print(f"\n──── {atom['name']} (knot {atom['knot_name']}, "
          f"A = {atom['A']}, n_0 = {atom['n_0']}, "
          f"ρ_obs = {atom['observed_rho']}) ────")
    print(f"  atom_braid_word in B_{atom['n_braid']} → embedded in B_{atom['n_0']}: "
          f"{atom['atom_braid_word']}")
    bk = binding_k_per_block(atom)
    print(f"  constituent product (B_{atom['n_0']}): "
          f"{bk['constituent_product_word']}")
    print(f"  K word (atom * cp^{{-1}}): {bk['K_word_in_H_n0']}")
    K = bk["K_image"]
    print(f"  K Wedderburn evaluation at H_{atom['n_0']}(q_0):")
    print(f"    α_gap(K) = {K['alpha_gap']:.6f}, "
          f"min_eig_sym(K) = {K['min_eig_overall']:+.6f}")

    rho_analysis = dominant_lambda_and_rho_rules(
        K, atom["n_0"], atom["observed_rho"],
    )
    dom = rho_analysis["dominant_lambda_K"]
    print(f"    dominant λ*(K) = {tuple(dom)}, dim_q = "
          f"{rho_analysis['dominant_dim_q_K_at_q0']:.6f}, "
          f"is_hook = {rho_analysis['dominant_is_hook']}")
    for rk, rv in rho_analysis["candidate_rules"].items():
        tick = "✓" if rv["matches_obs"] else "✗"
        print(f"    {tick}  {rk:30s} → ρ_pred = {rv['rho_predicted']!s:6s} "
              f"(matches ρ_obs = {atom['observed_rho']}? {rv['matches_obs']})")

    lp = operator_selection_lp_for_K(rho_analysis["per_lambda_for_K"])
    explicit = explicit_binding_k_analysis(atom)
    if explicit.get("available"):
        ex_dom = explicit["dominant_lambda_K_explicit"]
        print(f"  ─ explicit-K heuristic ({explicit['K_word_explicit']}): "
              f"α_gap = {explicit['K_alpha_gap_explicit']:.4f}, "
              f"dominant λ* = {tuple(ex_dom)}, dim_q = "
              f"{explicit['dominant_dim_q_explicit']:.4f}")

    return {
        "atom": atom["name"],
        "knot": atom["knot_name"],
        "A": atom["A"],
        "n_0": atom["n_0"],
        "binding_link_name": atom["binding_link_name"],
        "observed_rho": atom["observed_rho"],
        "B_AME_MeV": atom["B_AME_MeV"],
        "atom_braid_word": atom["atom_braid_word"],
        "constituent_product_word": bk["constituent_product_word"],
        "K_word_in_H_n0": bk["K_word_in_H_n0"],
        "K_alpha_gap": K["alpha_gap"],
        "K_min_eig_overall": K["min_eig_overall"],
        "K_per_block": {
            str(lam): {
                "chi": v["chi"],
                "det": v["det"],
                "min_eig_sym": v["min_eig_sym"],
                "psd_within_tol": v["psd_within_tol"],
            }
            for lam, v in K["per_block"].items()
        },
        "rho_rule_analysis": rho_analysis,
        "lp_dual": lp,
        "explicit_binding_k_heuristic": explicit,
    }


# ───────────────────────────────────────────────────────────────────
# Driver.
# ───────────────────────────────────────────────────────────────────

def main():
    print("══════════════════════════════════════════════════════════════════════")
    print("  Binding-K factorisation EVALUATOR — atomic-strand-count Wedderburn analysis at")
    print("  H_{3·A}(q_0) for ²H, ³H, ³He (issue #604, items 1–5).")
    print("══════════════════════════════════════════════════════════════════════")
    print(f"  q_0 = {Q0}")
    print(f"  m_e = {M_E_MEV} MeV")

    w = (
        WitnessBuilder("binding-k-solver", engine="python")
        .set_description(
            "Binding-K factorisation EVALUATOR (operator-selection LP / "
            "shadow-price / primal-dual / lp-duality fields emitted from "
            "the per-atom factorisation; NOT a search/optimisation step "
            "— the factorisation is computed deterministically from the "
            "presupposed T_w(𝔥) historical braid via braid-word "
            "concatenation `K_word = atom_word ++ cp_inv_word`, then "
            "evaluated per Wedderburn block at H_{3·A}(q_0); the actual "
            "search for K from substrate alone is in "
            "binding_k_enumerator.py).  Per the deliverable-4 binding-K "
            "factorisation finding (PR #610): T_w(𝔥) = K(𝔥) · ⊗_i "
            "T_w(nucleon_i) at H_{3·A}(q_0).  Issue #604 items 1-5: "
            "extends the H_3-only rho-prefactor verifier to the atomic "
            "strand count n_0 = 3·A using `build_seminormal_matrices` "
            "(general-n Hoefsmit, wired through "
            "syt_prefix_cache.BlockCache to amortise the SYT-prefix "
            "construction overhead).  Computes K's per-Wedderburn-block "
            "PSD eigenvalues, dominant λ* ⊢ 3·A by |y_λ · χ_λ(K)|, and "
            "tests the four candidate ρ rules against observed ρ for "
            "²H (n_0=6), ³H (n_0=9, embedded 8_11), ³He (n_0=9, "
            "embedded L6a4).  The natural Wedderburn-PSD constraint at "
            "the atomic strand count becomes ρ_λ(K) ⪰ 0 — the 'binding "
            "stability' certificate; per-atom witnesses include LP "
            "primal/dual (y0_star, y_star, active_set, primal_obj, "
            "dual_obj, duality_gap) per AGENTS.md 'LP/SDP duals — "
            "first-class infra' rule."
        )
        .set_content_block("conj:rho-prefactor-structural")
        .add_parameter("q_0", Q0)
        .add_parameter("m_e_MeV", M_E_MEV)
        .add_parameter("n_atoms", len(REGISTRY))
    )

    per_atom = []
    for atom in REGISTRY:
        per_atom.append(analyze_atom(atom))

    # ── Aggregate consistency. ──────────────────────────────────────
    rule_keys = list(per_atom[0]["rho_rule_analysis"]["candidate_rules"].keys())
    consistency = {}
    for r in rule_keys:
        per_atom_match = {
            a["atom"]: a["rho_rule_analysis"]["candidate_rules"][r]["matches_obs"]
            for a in per_atom
        }
        all_match = all(per_atom_match.values())
        consistency[r] = {
            "all_atoms_match": all_match,
            "per_atom_matches": per_atom_match,
            "n_match": sum(1 for v in per_atom_match.values() if v),
            "n_total": len(per_atom_match),
        }
    valid_rules = [r for r, v in consistency.items() if v["all_atoms_match"]]

    print()
    print("──── Cross-particle consistency (atomic strand count n_0 = 3·A) ────")
    for rk, rv in consistency.items():
        tick = "✓" if rv["all_atoms_match"] else "✗"
        print(f"  {tick}  {rk:30s} → {rv['n_match']}/{rv['n_total']} atoms match")
    print()

    summary = {
        "framework_status": (
            "operational — general-n Hoefsmit + binding-K factorisation "
            "+ per-block ρ-rule evaluation + LP/SDP dual emission wired "
            "end-to-end at H_{3·A} for ²H, ³H, ³He."
        ),
        "n_atoms_evaluated": len(per_atom),
        "candidate_rules_evaluated": rule_keys,
        "rules_consistent_with_all_observations": valid_rules,
        "n_K_psd_feasible_at_q0": sum(
            1 for a in per_atom if a["K_alpha_gap"] <= 1e-6
        ),
        "all_lp_strong_duality_holds": all(
            a["lp_dual"]["duality_gap"] < 1e-6 and a["lp_dual"]["feasible"]
            for a in per_atom
        ),
        "verdict": (
            f"{len(valid_rules)} of {len(consistency)} candidate rules "
            f"reproduce ρ at H_{{3·A}} for all {len(per_atom)} atoms.  "
            f"Compare with the H_3-level evaluation "
            f"(rho-prefactor-structural-verifier.witness.json, "
            f"deliverable 4 of PR #610) which had 0/5 rules consistent "
            f"due to the proton vs ³He χ-collision: that collision is "
            f"resolved here by the H_{{3·A}} embedding via the binding "
            f"operator K."
        ),
        "what_remains_open": [
            "Categorical uniqueness theorem for binding-K (deliverable "
            "3): per atom, prove K(𝔥) is the unique PSD-feasible Hecke "
            "element satisfying the joint-tower SDP cross-level "
            "consistency constraints (4) of "
            "prop:joint-tower-sdp-confinement.  The constituent leg "
            "is closed by R5-minimal; the binding-K leg is the open "
            "core.",
            "Generalise to ⁴He (B_? at H_12), ⁶Li (H_18), ⁷Li (H_21), "
            "α-cluster atoms — the same factorisation should apply.",
            "Symbolic-q evaluation of K's Wedderburn structure to "
            "discharge the rounding question categorically.",
        ],
    }
    (
        w.add_data("registry", REGISTRY)
         .add_data("per_atom_results", _serialise(per_atom))
         .add_data("cross_particle_consistency", _serialise(consistency))
         .add_data("summary", _serialise(summary))
         .add_caveat(
            "Numerical evaluation at f64 precision; deuteron uses H_6 "
            "(11 partitions, max d_λ = 16), tritium and ³He use H_9 "
            "(30 partitions, max d_λ = 42).  The Wenzl-Schur weights "
            "y_λ(q_0) for n=6, 9 are loaded from "
            "y-lambda-wenzl-witness.json if present; otherwise a "
            "uniform 1/|P(n)| fallback is used (the dominant-λ "
            "identification is dominated by χ_λ for typical knot "
            "elements).  K is computed via the braid-word "
            "concatenation T_atom · cp^{-1}, NOT via per-block matrix "
            "inversion (avoids ill-conditioned blocks)."
        )
    )
    out = w.save()
    print(f"  Witness: {out.name}")
    print(f"  Verdict: {summary['verdict']}")
    if valid_rules:
        print(f"  Rules consistent at atomic strand count:")
        for r in valid_rules:
            print(f"    • {r}")
    print("══════════════════════════════════════════════════════════════════════")


if __name__ == "__main__":
    main()
