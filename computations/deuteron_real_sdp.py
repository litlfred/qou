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
`solve_psd_operator_selection_sdp` (AGENTS.md §LP/SDP duals — first-class
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

import _path_bridge  # noqa: F401, E402 — bridge: reads a witness that co-moved into a cluster subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import math
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
import sys

sys.path.insert(0, str(HERE))
# Repo root by LANDMARK SEARCH, not by counting `.parent`s: the fixed
# count was off by one and resolved OUTSIDE the repo, so this bootstrap
# never fired -- masked because `_path_bridge`/PYTHONPATH already supplies
# the same directory in every in-repo run. Bean qou-rug0.
_QOU_REPO_ROOT = next(
    (_a for _a in Path(__file__).resolve().parents
     if (_a / "tools").is_dir() and (_a / "computations").is_dir()),
    Path(__file__).resolve().parent,
)
sys.path.insert(0, str(_QOU_REPO_ROOT / "tools" / "pyhecke" / "python"))

from pyhecke.lp_dual_solver import (  # noqa: E402
    solve_operator_selection_lp,
    solve_psd_operator_selection_sdp,
)
from murnaghan_nakayama import dim_specht  # noqa: E402  shared hook-length dim
from nucleus_sdp_assembly import build_cost_gram, tr_M_from_cache, solve_real_sdp  # noqa: E402

COST_WITNESS = _pb.witness_path("iterative-lp-dual-h6-deuteron.witness.json", HERE)
BRANCHING_WITNESS = _pb.witness_path("sublemma-2-1-deuteron-branching.witness.json", HERE)
OUT_WITNESS = HERE / "deuteron-real-sdp.witness.json"

# The current uniqueness anchor (empty-SDP); the real-SDP Lean theorem is
# the Phase D target.  Cited so this witness is wiring-audited (PR #1572/#1573).
LEAN_UNIQUENESS_REF = "qou:QOU.BraidKnot.deuteron_uniqueness_closed"

# AME2020 deuteron binding energy (MeV) — RHS for the physical constraint.
# Matches the repo-wide constant (probe_k_ud_*, applied_uniqueness_mass_table).
B_D_AME_MeV = 2.22456607
# 9-pair color-flavor structure of p=uud × n=udd: 2·(u,u)+4·(u,d)+1·(d,u)+2·(d,d).
# Neutron-heavy 5:4 weighting with a bar-involution sign flip on the mixed
# (u,d)/(d,u) channel (probe_k_ud_fractional_and_alt_ansatz.nine_pair_ratio).
NINE_PAIR = {"uu": 2, "ud": 4, "du": 1, "dd": 2}  # multiplicities, Σ = 9


def solve_lp_with_eq(t, G, A_eq, b_eq, n_target):
    """LP-dual solve via the canonical entry point, with optional extra
    equality rows folded into the square-Gram operator-selection form.

    The pyhecke entry point takes (t, G_square, n_target) where the only
    constraints are Σx = n_target and Gx ≥ 0. Equality rows A_eq x = b_eq
    are not natively supported there, so for methods that need them we fall
    back to a direct scipy/HiGHS solve and report primal+dual ourselves.
    """
    import numpy as _np
    from scipy.optimize import linprog as _linprog

    t = _np.asarray(t, float)
    G = _np.asarray(G, float)
    d = len(t)
    A_ub = -G  # Gx ≥ 0  ⇔  -Gx ≤ 0
    b_ub = _np.zeros(G.shape[0])
    A_eq_full = [_np.ones(d)]
    b_eq_full = [n_target]
    if A_eq is not None:
        for row, rhs in zip(A_eq, b_eq):
            A_eq_full.append(_np.asarray(row, float))
            b_eq_full.append(float(rhs))
    res = _linprog(
        c=t, A_ub=A_ub, b_ub=b_ub,
        A_eq=_np.array(A_eq_full), b_eq=_np.array(b_eq_full),
        bounds=[(-1e6, 1e6)] * d, method="highs",
    )
    out = {
        "status": res.status,
        "feasible": bool(res.success),
        "primal_obj": float(res.fun) if res.success else None,
        "x_star": res.x.tolist() if res.success else None,
        "duality_gap": 0.0 if res.success else None,
    }
    if res.success and res.eqlin is not None:
        out["eq_duals"] = _np.asarray(res.eqlin.marginals).tolist()
    if res.success and res.ineqlin is not None:
        out["ineq_duals"] = _np.asarray(res.ineqlin.marginals).tolist()
    return out


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

    # Cost + Frobenius Gram via the shared assembly module (centralises the
    # t_λ=y_λ·χ^λ / G_λλ=y_λ·dim pattern duplicated across ~67 scripts; the
    # Burnside dim check + tr_M cross-check run inside build_cost_gram).
    _cg = build_cost_gram(
        y_lambda, chi_beta_D, n=6, tr_M_check=float(data["tr_M_check_at_q0"]),
    )
    keys, parts, dims = _cg.keys, _cg.parts, _cg.dims
    y, chi = _cg.y, _cg.chi
    t, frob_diag = _cg.t, _cg.frob_diag
    tr_M_beta_D = _cg.tr_M
    n_target = tr_M_beta_D            # net constraint
    tr_M_recorded = float(data["tr_M_check_at_q0"])
    tr_M_rel_err = abs(tr_M_beta_D - tr_M_recorded) / abs(tr_M_recorded)

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
    # paired LP+SDP operator-selection solve (always emits both duals) via the
    # shared dual-emitting wrapper.
    _r = solve_real_sdp(_cg, n_target)
    lp_d, sdp_d = _r["lp"], _r["sdp"]
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

    # ── Phase B (full) — four constraint-encoding methods, side by side ──
    # Each tries to regularise the indefinite-Gram unbounded program with a
    # different physical constraint. Reported together so the encoding choice
    # is auditable; method (2) is explicitly flagged as an un-vetted ansatz.
    chi = np.array([chi_beta_D[k] for k in keys])  # χ^λ(β_D) per block
    n_blocks = len(keys)
    methods = {}

    # (1) Bar-involution / Type-B folding (§7b): pair each block with its
    #     conjugate and impose x_λ = x_λ' (symmetric fold). This collapses the
    #     sign-flipped conjugate pairs, definitising the folded Gram — the
    #     symmetry-driven regulariser (no invented weights).
    fold_rows, fold_rhs = [], []
    seen = set()
    for i, k in enumerate(keys):
        cp = conjugate_partition(parse_partition(k))
        ck = key_of.get(cp)
        if ck and ck != k and (k, ck) not in seen and (ck, k) not in seen:
            j = keys.index(ck)
            row = np.zeros(n_blocks); row[i] = 1.0; row[j] = -1.0
            fold_rows.append(row); fold_rhs.append(0.0)
            seen.add((k, ck))
    methods["1_bar_involution_fold"] = {
        "description": "x_λ = x_λ' (bar-involution/Type-B fold, §7b) — symmetry regulariser",
        "ansatz_flag": False,
        "result": solve_lp_with_eq(t, np.diag(frob_diag), fold_rows, fold_rhs, n_target),
    }

    # (2) Character-projection color-flavor constraints (UN-VETTED ANSATZ).
    #     One row per pair-type: A_pair[λ] = mult(pair)·χ^λ(β_D)/[6]_q!, RHS
    #     apportions B_D across pairs by multiplicity. Flagged for the
    #     canonical-watcher — the pair→block map does not exist in the repo.
    bracket6 = float(data.get("bracket_6_q0", 1.0))  # [6]_q! if recorded, else 1
    cf_rows, cf_rhs = [], []
    total_mult = sum(NINE_PAIR.values())
    for pair, mult in NINE_PAIR.items():
        sign = -1.0 if pair in ("ud", "du") else 1.0  # bar-flip on mixed channel
        row = sign * mult * chi / bracket6
        cf_rows.append(row)
        cf_rhs.append(B_D_AME_MeV * mult / total_mult)
    methods["2_character_projection_colorflavor"] = {
        "description": "per-pair χ^λ projection rows + AME-apportioned RHS",
        "ansatz_flag": True,
        "ansatz_warning": "UN-VETTED: pair→block map invented here; flag to canonical-watcher / CAL-4 discipline before any production use.",
        "result": solve_lp_with_eq(t, np.diag(frob_diag), cf_rows, cf_rhs, n_target),
    }

    # (3) Conservation-law constraints only: baryon number (Σx fixes total)
    #     and charge. Minimal and safe; weak (2 rows for 11 blocks).
    #     Baryon: Σ x_λ = n_target (already the net constraint). Charge:
    #     weight blocks by χ^λ sign as a proxy for the +1 deuteron charge.
    cons_rows = [np.sign(chi)]
    cons_rhs = [1.0]  # net charge +1 (proxy)
    methods["3_conservation_laws"] = {
        "description": "baryon (net) + charge (sign-weighted) conservation rows",
        "ansatz_flag": False,
        "result": solve_lp_with_eq(t, np.diag(frob_diag), cons_rows, cons_rhs, n_target),
    }

    # (4) AME-binding equality: retarget the net constraint to the physical
    #     binding energy t·x = B_D instead of tr_M(β_D). One-line physical
    #     anchor; composes with any of 1–3 (here stand-alone).
    methods["4_ame_binding_equality"] = {
        "description": "t·x = B_D_AME (physical binding-energy target)",
        "ansatz_flag": False,
        "production_default": False,
        "non_default_reason": "imposes the AME binding as an equality (consumes "
                              "the experimental answer); a validation anchor, not "
                              "a substrate derivation.",
        "result": solve_lp_with_eq(t, np.diag(frob_diag), [t], [B_D_AME_MeV], n_target),
    }

    # (5) CANONICAL — Littlewood-Richardson branching H_6 ⊃ H_3 × H_3.
    #     The deuteron is proton-H_3 ⊗ neutron-H_3; the constraint rows come
    #     from the *verified* LR breakdown
    #       χ^λ(β_D) = Σ_{μ,ν⊢3} c^λ_{μν} χ^μ(p) χ^ν(n)
    #     (sublemma-2-1-deuteron-branching.witness.json, branching_verified).
    #     For each constituent block μ⊢3 we impose that the occupation projected
    #     through the LR map reproduces the disjoint-product trace — i.e.
    #     Σ_λ [Σ_ν c^λ_{μν} χ^ν(n)] x_λ = χ^μ(p) · tr_M_neutron.  This is a
    #     representation-theory identity, NOT a fit: the c^λ_{μν} are integers
    #     and the χ are computed at q_0.  Three rows (μ ∈ {(3),(2,1),(1³)}).
    branch = json.loads(BRANCHING_WITNESS.read_text())
    lr = branch["lr_breakdown_per_lambda"]            # {λ_key: [{mu,nu,c,term_re}]}
    chi_p = {k: v["re"] for k, v in branch["chi_proton_h3"].items()}
    chi_n = {k: v["re"] for k, v in branch["chi_neutron_h3"].items()}
    parts3 = ["(3,)", "(2, 1)", "(1, 1, 1)"]

    def pkey(lst):  # [3] -> "(3,)" ; [2,1] -> "(2, 1)"
        return "(" + ", ".join(str(x) for x in lst) + ("," if len(lst) == 1 else "") + ")"

    # tr_M_neutron = Σ_ν y_ν χ^ν(n), the canonical H_3 neutron Markov trace
    # (full-Hecke y_ν from the y-lambda-at-q0 cache; no Rust). Centralised in
    # nucleus_sdp_assembly.tr_M_from_cache (the PR #2219 correctness fix —
    # never the unweighted proxy Σ_ν χ^ν, never /len(parts3)).
    tr_M_neutron = tr_M_from_cache(chi_n, n=3)
    lr_rows, lr_rhs = [], []
    for mu in parts3:
        row = np.zeros(n_blocks)
        for li, lkey in enumerate(keys):
            terms = lr.get(lkey, [])
            coeff = 0.0
            for term in terms:
                if pkey(term["mu"]) == mu:
                    coeff += term["c"] * chi_n.get(pkey(term["nu"]), 0.0)
            row[li] = coeff
        lr_rows.append(row)
        lr_rhs.append(chi_p[mu] * tr_M_neutron)  # stated identity: no /len(parts3)
    methods["5_lr_branching_canonical"] = {
        "description": "Littlewood-Richardson H_6⊃H_3×H_3 branching rows: "
                       "Σ_λ[Σ_ν c^λ_{μν} χ^ν(n)] x_λ = χ^μ(p)·tr_M_neutron, "
                       "tr_M_neutron = Σ_ν y_ν χ^ν(n) (canonical, no fit).",
        "ansatz_flag": False,
        "canonical": True,
        "production_default": True,
        "tr_M_neutron": tr_M_neutron,
        "result": solve_lp_with_eq(t, np.diag(frob_diag), lr_rows, lr_rhs, n_target),
    }

    # (6) Scalar 9-pair weighted ratio (FITTED — must be labelled near-match).
    #     Single row Σ_λ r_λ x_λ = ratio · tr_M(β_D), where r_λ is the
    #     per-block interface ratio χ_D/χ_disjoint and `ratio` is the
    #     neutron-heavy 5:4 weighted 9-pair value with the bar-involution
    #     sign flip on the mixed channel.  NOT substrate-canonical.
    interface = branch["deuteron_interface_ratios"]
    r_lambda = np.array([interface[k]["ratio"][0] for k in keys])
    # neutron-heavy weighted ratio using interface magnitudes (bar-flip baked in
    # via signed ratios); scalar target = mean interface ratio · tr_M.
    ratio_scalar = float(np.mean(r_lambda))
    methods["6_scalar_9pair_ratio_fitted"] = {
        "description": "single 9-pair weighted-ratio row (FITTED; bar-flip on mixed channel)",
        "ansatz_flag": True,
        "production_default": False,
        "discipline_label": "near-match / exploratory — NOT substrate-canonical (CAL-4)",
        "result": solve_lp_with_eq(
            t, np.diag(frob_diag), [r_lambda], [ratio_scalar * n_target], n_target,
        ),
    }

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
            # ---- primal + dual (AGENTS.md §LP/SDP duals — required fields) ----
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
            # ---- Phase B full — four encodings compared ----
            "B_D_AME_MeV": B_D_AME_MeV,
            "nine_pair_multiplicities": NINE_PAIR,
            "phase_B_full_methods": methods,
            "production_default_encoding": "5_lr_branching_canonical",
            "production_default_note": (
                "The canonical (substrate-derived, no-fit) LR-branching "
                "encoding is the production default. Encoding 4 (AME equality) "
                "consumes the experimental binding and is a validation anchor "
                "only; encoding 6 is fitted; encoding 2 is an un-vetted ansatz. "
                "The canonical encoding does NOT yet reproduce the deuteron "
                "binding — that closure is the open Δ_λ gate (AGENTS.md); "
                "production reports the honest canonical result, not a fit."
            ),
            # ---- scope markers ----
            "phase_A_cost": "done",
            "phase_B_constraints": "interim (bounded subspace) + 4 full encodings compared (method 2 un-vetted ansatz); full color-flavor 9-pair + AME2020 RHS",
            "phase_C_dual_solve": "diagnostic (unbounded on full space; bounded on positive subspace)",
            "phase_D_lean_wiring": "pending (deuteron_emptySDP -> deuteron_realSDP)",
        },
    }
    # Provenance envelope. This producer writes its witness as raw JSON, so
    # nothing stamps `scriptHash` — and a witness without one cannot be
    # compared against its producer, so it drops OUT of the self-staleness
    # audit and reads as "not stale" forever. Regenerating it then looks
    # like progress while removing it from the count: a false drain.
    # Full rationale and the detector: computations/witness_drain_audit.py.
    #
    # `stamp_staleness_metadata`, not `wrap_legacy().save()`: it adds the
    # fields in place and leaves the on-disk shape untouched, so consumers
    # of legacy `assertions` records (which key on `label`, not `name`) do
    # not have to change. `engine` is passed back from the payload because
    # the helper overwrites it, and a descriptive engine string is worth
    # keeping.
    try:
        from witness_base import WitnessBuilder  # noqa: E402
    except ImportError:  # cluster subdir without the _path_bridge bootstrap
        import sys as _sys
        from pathlib import Path as _Path
        _sys.path.insert(0, str(next(
            _a / "substrate" for _a in _Path(__file__).resolve().parents
            if (_a / "substrate" / "witness_base.py").is_file())))
        from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__,
        engine=witness.get("engine", 'numpy'))
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
    print("  Phase B full — six encodings:")
    for name, m in methods.items():
        r = m["result"]
        flag = "  ⚠ANSATZ" if m["ansatz_flag"] else ""
        print(f"    {name:38} feasible={r['feasible']}  "
              f"primal_obj={r['primal_obj']}{flag}")
    print(f"  wrote {OUT_WITNESS.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
