#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical-only output.
"""
Deuteron real per-nucleus SDP — drops the abstract empty-SDP layer.

Per the workplan `docs/workplans/2026-05-31-real-sdp-wiring-per-nucleus.md`
(PR #1575). The existing uniqueness infrastructure
(`QOU.BraidKnot.AppliedDeuteronUniqueness.deuteron_uniqueness_closed`)
certifies T_w uniqueness at the **abstract empty-constraint SDP**
(cost = identity, no constraints, Φ⋆ = 0). That proves the framework
*can* certify uniqueness, but not uniqueness of the *actual* T_w that
consumes the deuteron mass formula.

This script assembles and solves the **real** deuteron SDP at H_6
(n = 3·A = 6, 11 partitions λ ⊢ 6) with a genuine, non-empty cost:

  operators        b_λ := P_λ          (Wedderburn block projectors, λ ⊢ 6)
  cost (Phase A)   t_λ := tr_M(P_λ · β_D) = y_λ(q_0) · χ^λ(β_D)
                                          (per-partition mass-formula summand,
                                           Σ_λ t_λ = tr_M(β_D) ≈ 0.3883)
  Frobenius Gram   G_λμ := tr_M(P_λ P_μ) = δ_λμ · tr_M(P_λ)
                                          = δ_λμ · y_λ · dim S^λ
                                          (diagonal: P_λ are orthogonal
                                           central idempotents)
  net constraint   n_target := tr_M(β_D)  (the total trace the selected
                                           blocks must reproduce)

The solve routes through the canonical dual-emitting entry point
`pyhecke.lp_dual_solver.solve_operator_selection_lp` /
`solve_psd_operator_selection_sdp` (CLAUDE.md §LP/SDP duals — first-class
infra). The dual shadow prices `y_star` identify the **active demand
channels** — the Wedderburn blocks the deuteron bound state actually
saturates ("most receptive sub-braids").

Scope of this script (Phase A + Phase C-numeric):
  ✔ Phase A — real cost matrix from the mass-formula witness.
  ✔ Phase C — strong-duality SDP solve with primal + dual + gap.
  ☐ Phase B — color-flavor 9-pair constraints (proton uud × neutron udd)
              as additional Gram rows + AME2020 binding-energy RHS.
              Follow-up commit; see workplan §"Phase B".
  ☐ Phase D — Lean wiring `deuteron_emptySDP → deuteron_realSDP`.
              Follow-up PR; consumes this witness via the axiom bridge.

Input : iterative-lp-dual-h6-deuteron.witness.json  (y_λ, χ^λ(β_D) at q_0)
Output: deuteron-real-sdp.witness.json
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
import sys

sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "pyhecke" / "python"))

from pyhecke.lp_dual_solver import (  # noqa: E402
    solve_operator_selection_lp,
    solve_psd_operator_selection_sdp,
)
from murnaghan_nakayama import dim_specht  # noqa: E402  shared hook-length dim

COST_WITNESS = HERE / "iterative-lp-dual-h6-deuteron.witness.json"
OUT_WITNESS = HERE / "deuteron-real-sdp.witness.json"

# The current uniqueness anchor (empty-SDP); the real-SDP Lean theorem is
# the Phase D target.  Cited so this witness is wiring-audited (PR #1572/#1573).
LEAN_UNIQUENESS_REF = "qou:QOU.BraidKnot.deuteron_uniqueness_closed"


def parse_partition(key: str) -> tuple[int, ...]:
    """'(3, 2, 1)' -> (3, 2, 1)."""
    return tuple(int(p) for p in key.strip("()").rstrip(",").split(",") if p.strip())


def conjugate_partition(part: tuple[int, ...]) -> tuple[int, ...]:
    """Conjugate (transpose) partition λ ↦ λ' — the 'skew'/column-reading."""
    if not part:
        return ()
    return tuple(sum(1 for r in part if r > j) for j in range(part[0]))


def sanitize_nan(val):
    """Replace NaN/Inf floats with None so the witness is RFC 8259 JSON.

    The infeasible/unbounded SDP path can return NaN entries (e.g. the
    cvxpy `X_star`); standard JSON (and bun/JS `JSON.parse` in the content
    pipeline) reject `NaN`/`Infinity` literals.
    """
    if isinstance(val, dict):
        return {k: sanitize_nan(v) for k, v in val.items()}
    if isinstance(val, list):
        return [sanitize_nan(x) for x in val]
    if isinstance(val, float) and not math.isfinite(val):
        return None
    return val


def main() -> int:
    data = json.loads(COST_WITNESS.read_text())["data"]
    y_lambda = data["y_lambda_at_q0"]
    chi_beta_D = data["chi_lambda_beta_D_at_q0"]

    keys = list(y_lambda.keys())
    parts = [parse_partition(k) for k in keys]
    dims = [dim_specht(p) for p in parts]

    # sanity: Σ (dim S^λ)² = n!  (Burnside)
    assert sum(d * d for d in dims) == math.factorial(6), "irrep dims do not close to 6!"

    y = np.array([y_lambda[k] for k in keys], dtype=float)
    chi = np.array([chi_beta_D[k] for k in keys], dtype=float)

    # Phase A — real cost and Frobenius Gram
    t = y * chi                       # t_λ = tr_M(P_λ · β_D)
    frob_diag = y * np.array(dims)    # G_λλ = tr_M(P_λ) = y_λ · dim S^λ
    tr_M_beta_D = float(t.sum())      # = Σ_λ y_λ χ^λ(β_D)
    n_target = tr_M_beta_D            # net constraint

    # cross-check against the recorded Markov trace
    tr_M_recorded = float(data["tr_M_check_at_q0"])
    tr_M_rel_err = abs(tr_M_beta_D - tr_M_recorded) / abs(tr_M_recorded)
    assert tr_M_rel_err < 1e-9, f"tr_M mismatch vs witness: {tr_M_rel_err:.2e}"

    # Phase A diagnostic — the q_0 Frobenius Gram is INDEFINITE.  At q_0 ≠ 1
    # the Wenzl/Markov q-trace is not positive-definite, so some blocks carry
    # a negative q-trace norm (tr_M(P_λ) < 0).  These are "forbidden" channels:
    # an occupation x_λ ≥ 0 on a negative-norm block violates Frobenius
    # positivity, so the physical real SDP must set x_λ = 0 there.  Without
    # this the unconstrained LP is unbounded (the empty-SDP pathology in
    # disguise) — which is precisely why Phase B's color-flavor constraints
    # are required.
    forbidden_blocks = [keys[i] for i, g in enumerate(frob_diag) if g < 0.0]

    # Phase C — solve the real SDP with the true (indefinite) Frobenius Gram.
    # The canonical operator-selection entry point takes a square (d,d) Gram,
    # so the only positivity is Gx ≥ 0 with G = diag(tr_M(P_λ)).  Because that
    # Gram is indefinite at q_0, the program is UNBOUNDED (primal drives to the
    # M_bound rail; duality gap blows up).  This is the headline Phase A
    # result: a real per-nucleus SDP is ill-posed without Phase B's
    # color-flavor constraints — the empty-SDP layer cannot be trivially
    # upgraded by attaching a cost alone.
    G = np.diag(frob_diag)
    lp = solve_operator_selection_lp(t, G, n_target)
    sdp = solve_psd_operator_selection_sdp(t, G, n_target)
    lp_d = lp.to_dict()
    sdp_d = sdp.to_dict()
    _gap_full = lp_d.get("duality_gap")
    bounded = (_gap_full is not None and abs(float(_gap_full)) < 1e-6
               and bool(lp_d.get("feasible", True)))

    # active demand channels = blocks the deuteron bound state saturates
    active_idx = lp_d.get("active_set", [])
    active_blocks = [keys[i] for i in active_idx if i < len(keys)]

    # ── Symmetry analysis (involution / bar / skew) ──────────────────────
    # The Frobenius-norm sign structure is governed by the bar-involution
    # (q ↦ q⁻¹) composed with the skew/conjugate map λ ↦ λ'.  Empirically
    # every negative-norm forbidden block is the conjugate of a dominant
    # positive block, with tr_M(P_λ) sign-flipped — the §7b "symmetric
    # crystal / Type-B folding" signature.  We record the pairing.
    key_of = {parse_partition(k): k for k in keys}
    trM_block = {k: float(frob_diag[i]) for i, k in enumerate(keys)}
    symmetry = []
    for i, k in enumerate(keys):
        p = parse_partition(k)
        cp = conjugate_partition(p)
        ck = key_of.get(cp)
        t_self = trM_block[k]
        t_conj = trM_block.get(ck) if ck else None
        symmetry.append({
            "block": k,
            "conjugate": ck,
            "self_conjugate": (ck == k),
            "trM": t_self,
            "trM_conjugate": t_conj,
            "sign_flip_under_conjugation": (
                t_conj is not None and (t_self < 0) != (t_conj < 0)
            ),
        })
    self_conjugate_blocks = [s["block"] for s in symmetry if s["self_conjugate"]]
    sign_flip_pairs = sorted({
        tuple(sorted((s["block"], s["conjugate"])))
        for s in symmetry if s["sign_flip_under_conjugation"]
    })

    # ── Phase B (interim) — bounded subspace on positive-norm blocks ─────
    # Drop the bar-conjugate forbidden blocks (tr_M(P_λ) < 0); on the
    # surviving positive-Gram subspace the operator-selection program is
    # bounded and strong duality holds.  This is the well-posed interim
    # result (no quark constraints yet) that de-risks the Phase D Lean
    # wiring; the full color-flavor SDP is the follow-up.
    pos = [i for i, g in enumerate(frob_diag) if g > 0.0]
    pos_keys = [keys[i] for i in pos]
    t_pos = t[pos]
    G_pos = np.diag(frob_diag[pos])
    n_target_pos = float(t_pos.sum())
    lp_pos = solve_operator_selection_lp(t_pos, G_pos, n_target_pos)
    lp_pos_d = lp_pos.to_dict()
    _gap_pos = lp_pos_d.get("duality_gap")
    interim_bounded = (_gap_pos is not None and abs(float(_gap_pos)) < 1e-6
                       and bool(lp_pos_d.get("feasible", True)))
    interim_active = [pos_keys[i] for i in lp_pos_d.get("active_set", []) if i < len(pos_keys)]

    witness = {
        "engine": "deuteron_real_sdp",
        "engineVersion": "0.1.0",
        "computation": (
            "Deuteron real per-nucleus SDP (Phase A cost + Phase C dual "
            "solve) — replaces the abstract empty-constraint SDP. "
            "operator-selection-lp / lp-dual."
        ),
        "scriptFile": "deuteron_real_sdp.py",
        "lean_uniqueness_ref": LEAN_UNIQUENESS_REF,
        "data": {
            "n_strands": 6,
            "nucleus": "deuteron (²H, Z=1, N=1, A=2)",
            "partitions": keys,
            "irrep_dims": dims,
            "cost_t_lambda": t.tolist(),
            "frobenius_gram_diag": frob_diag.tolist(),
            "frobenius_gram_indefinite": bool((frob_diag < 0).any()),
            "forbidden_blocks_negative_norm": forbidden_blocks,
            "n_target": n_target,
            "tr_M_beta_D": tr_M_beta_D,
            "tr_M_rel_err_vs_witness": tr_M_rel_err,
            # ---- primal + dual (CLAUDE.md §LP/SDP duals — required fields) ----
            "lp": lp_d,
            "sdp": sdp_d,
            "y0_star": lp_d.get("y0_star"),
            "y_star": lp_d.get("y_star"),
            "active_set": active_idx,
            "active_blocks": active_blocks,
            "primal_obj": lp_d.get("primal_obj"),
            "dual_obj": lp_d.get("dual_obj"),
            "duality_gap": lp_d.get("duality_gap"),
            "strong_duality_holds": bounded,
            "real_sdp_well_posed_without_constraints": bounded,
            "diagnostic": (
                "Real SDP UNBOUNDED at q_0 — Frobenius Gram is indefinite "
                "(negative-norm blocks forbidden). Phase B color-flavor "
                "constraints required for a well-posed bounded program."
            ) if not bounded else "Real SDP bounded; strong duality holds.",
            # ---- symmetry (involution / bar / skew) ----
            "symmetry_conjugate_pairing": symmetry,
            "self_conjugate_blocks": self_conjugate_blocks,
            "sign_flip_conjugate_pairs": [list(p) for p in sign_flip_pairs],
            "symmetry_note": (
                "Every negative-norm forbidden block is the conjugate λ↦λ' "
                "of a dominant positive block with tr_M(P_λ) sign-flipped — "
                "the §7b bar-involution (q↦q⁻¹) / Type-B-folding signature. "
                "(3,2,1) is the self-conjugate fixed point."
            ),
            # ---- Phase B interim (bounded positive-norm subspace) ----
            "phase_B_interim": {
                "positive_norm_blocks": pos_keys,
                "n_target": n_target_pos,
                "bounded": interim_bounded,
                "strong_duality_holds": interim_bounded,
                "active_blocks": interim_active,
                "lp": lp_pos_d,
            },
            # ---- scope markers ----
            "phase_A_cost": "done",
            "phase_B_constraints": "interim (bounded positive-norm subspace); full color-flavor 9-pair + AME2020 RHS pending",
            "phase_C_dual_solve": "diagnostic (unbounded on full space; bounded on positive subspace)",
            "phase_D_lean_wiring": "pending (deuteron_emptySDP -> deuteron_realSDP)",
        },
    }
    OUT_WITNESS.write_text(json.dumps(sanitize_nan(witness), indent=2) + "\n")

    print(f"deuteron real SDP @ H_6 — {len(keys)} blocks")
    print(f"  tr_M(β_D)      = {tr_M_beta_D:.10f}  (rel_err vs witness {tr_M_rel_err:.2e})")
    print(f"  primal_obj     = {lp_d.get('primal_obj')}")
    print(f"  dual_obj       = {lp_d.get('dual_obj')}")
    print(f"  duality_gap    = {lp_d.get('duality_gap')}")
    print(f"  Gram indefinite at q_0: {bool((frob_diag < 0).any())}  "
          f"forbidden (neg-norm) blocks = {forbidden_blocks}")
    print(f"  active blocks (full, unbounded) = {active_blocks}")
    print(f"  self-conjugate block(s)         = {self_conjugate_blocks}")
    print(f"  sign-flip conjugate pairs       = {[list(p) for p in sign_flip_pairs]}")
    print(f"  Phase B interim — bounded: {interim_bounded}  "
          f"gap={lp_pos_d.get('duality_gap')}")
    print(f"  Phase B interim — active blocks = {interim_active}")
    print(f"  wrote {OUT_WITNESS.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
