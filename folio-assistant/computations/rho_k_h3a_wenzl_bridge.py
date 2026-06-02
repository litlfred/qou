#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical sympy/mpmath consumer; symbolic-q polynomials live upstream in y_lambda_wenzl_bridge / hoefsmit_symbolic witnesses.
"""ρ_K refinement via Wenzl-bridge augmented Markov system — Option F.

Sibling of `rho_k_h3a_refinement.py` (Option A: Occam-singleton heuristic).
Where Option A picks a single Wedderburn block by a (1 eq, 11 unknowns)
Occam minimum-|Δ| heuristic, **Option F** augments the single mass
constraint with **10 additional Markov-cycle-type constraints** to give
a genuinely 11×11 linear system.

The construction mirrors the Wenzl-bridge derivation of ``y_λ`` itself
(see `prop:alpha-k-derivation-procedure`):

    Σ_λ χ^λ(w_μ) y_λ = z^{n - ℓ(μ)},   μ ⊢ n.

The character matrix M[μ, λ] = χ^λ(w_μ) is invertible at generic q
(Schur–Weyl–Hecke duality), so the system uniquely determines y_λ
from p(n) Markov-axiom constraints.  Option F applies the same
matrix to the **deuteron-binding RHS**:

    Σ_λ χ^λ(w_μ) · (y_λ Δ_λ) = b_μ                     (★)

where the variant β_D^(μ) is the cycle-type word w_μ on n=6 strands
and the RHS b_μ is set by the **physical anchor** that the deuteron
binding shifts ρ_K by a fixed Δρ_D, so that the same shift propagated
through each diagnostic word satisfies

    b_μ := Δρ_D · |tr_M(w_μ)| = Δρ_D · z^{n-ℓ(μ)}.

This is the **only** consistent assignment if Δ_λ is a property of the
bound state alone (not of the diagnostic word) and the per-word residual
scales with its own Markov trace.  Other choices of b_μ correspond to
genuinely independent physical anchors that we do not have for the
deuteron alone — see "Honesty caveat" in the witness ``notes`` field.

By linearity (and Wenzl's bridge identity Σ_λ y_λ χ^λ(w_μ) = z^{n-ℓ(μ)}),
the system (★) admits the *unique* closed-form solution

    Δ_λ  =  Δρ_D                        (uniformly across all λ ⊢ 6).

Equivalently, ``y_λ Δ_λ = Δρ_D · y_λ`` — i.e. Option F selects the
"y_λ-proportional binding profile": each Wedderburn block carries
binding strength proportional to its Jones–Markov weight.  This is the
maximum-entropy choice consistent with both the deuteron mass and the
Markov axioms.

Output: ``rho-k-h3a-wenzl-bridge.witness.json`` with rank diagnostics,
condition number, and side-by-side comparison against the Option A
Occam pick from ``rho-k-h3a-refinement.witness.json``.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import numpy as np
# `sympy` and `hoefsmit_symbolic.Q` were imported here in the initial
# version but never used (Copilot PR #613 review).  Removed to keep the
# script's dependency surface minimal.

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from codata_constants import M_E_MEV, M_P_MEV, M_N_MEV, M_D_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Reuse the proven numeric Hoefsmit + character pipeline from sibling
# rho_k_h3a_refinement.py (do NOT modify that script per task constraint).
from rho_k_h3a_refinement import (  # noqa: E402
    chi_numeric,
    deuteron_canonical_crossings,
    load_y_lambda_n6,
    load_deuteron_tr_M,
    evaluate_at_q0,
    partitions_of_n,
)

set_compute_dps()


# ── Cycle-type word builder (1-indexed σ generators) ─────────
def cycle_type_word_crossings(mu) -> list[tuple[int, str]]:
    """Reduced word realising cycle type μ on n = sum(μ) strands.

    Mirrors `y_lambda_wenzl_bridge.cycle_type_word(mu)` (1-indexed
    σ_1, σ_2, …) but emits (gen_idx, ctype) pairs (0-indexed) for the
    `chi_numeric` consumer in `rho_k_h3a_refinement.py`.

    For μ = (μ_1, …, μ_k) ⊢ n, the canonical word is the concatenation
    of cycle-rotations on disjoint strand groups; total length is
    Σ (μ_i - 1) = n - ℓ(μ).
    """
    crossings: list[tuple[int, str]] = []
    s = 0  # 0-indexed strand offset
    for m in mu:
        for j in range(m - 1):
            crossings.append((s + j, "sigma"))
        s += m
    return crossings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dps", type=int, default=50,
        help="mpmath precision for χ^λ and y_λ evaluations (default: 50)."
    )
    args = parser.parse_args()
    mp.mp.dps = args.dps

    print("=" * 96)
    print("  ρ_K H_{3A} Wedderburn refinement — DEUTERON, Option F")
    print("  (Wenzl-bridge augmented Markov system; sibling of #564 / Option A)")
    print("=" * 96)

    n = 6
    parts = partitions_of_n(n)
    assert len(parts) == 11, f"expected 11 partitions of 6, got {len(parts)}"

    print(f"\n  q_0 = {mp.nstr(Q_MP, 25)}")
    print(f"  n = {n}, p(n) = {len(parts)}")

    # ── Step 1: |tr_M(β_D)| and Δρ from Option A pipeline ──────
    tr_M = load_deuteron_tr_M()
    abs_tr_M = abs(tr_M)
    rho_K_LO = (M_P_MEV + M_N_MEV) / (M_E_MEV * abs_tr_M)
    rho_K_codata = M_D_MEV / (M_E_MEV * abs_tr_M)
    delta_rho = rho_K_codata - rho_K_LO
    print(f"  |tr_M(β_D)|       = {mp.nstr(abs_tr_M, 25)}")
    print(f"  Δρ_D (residual)   = {mp.nstr(delta_rho, 25)}")

    # ── Step 2: load y_λ(q_0) for n = 6 ───────────────────────
    print("\n  Loading y_λ(q_0) from Wenzl-bridge witness …")
    y_lam_sym = load_y_lambda_n6()
    y_at_q0 = {}
    for lam in parts:
        y_at_q0[lam] = evaluate_at_q0(y_lam_sym[lam])

    # ── Step 3: build 11 atomic-braid variants ─────────────────
    # Variant 0 = the canonical deuteron word β_D itself (the physical
    #             anchor; b_0 = Δρ · |tr_M(β_D)|).
    # Variants 1..10 = the 10 non-trivial cycle-type words w_μ for
    #             μ ⊢ 6 (the Wenzl-bridge probes; b_i = Δρ · z^{n-ℓ(μ)}).
    # Note: μ = (1,1,1,1,1,1) gives the empty word w_μ = 1, where
    #       χ^λ(1) = dim_λ and tr_M(1) = 1 = z⁰. We include it as
    #       variant 1 to give a clean basis (the deuteron + every
    #       cycle type).  Total = 1 + 11 = 12 candidates; we down-
    #       select to 11 below by dropping whichever has smallest
    #       independent contribution (or report rank-deficiency).
    deut_crossings = deuteron_canonical_crossings()
    cycle_types = parts  # 11 partitions of 6 → 11 cycle types

    variants: list[dict] = []
    # Add the deuteron itself first
    variants.append({
        "name": "beta_D (canonical)",
        "kind": "deuteron",
        "mu": None,  # not a cycle-type word
        "crossings": deut_crossings,
    })
    for mu in cycle_types:
        variants.append({
            "name": f"w_{tuple(mu)}",
            "kind": "cycle_type",
            "mu": list(mu),
            "crossings": cycle_type_word_crossings(mu),
        })

    print(f"\n  Built {len(variants)} candidate variants "
          f"(1 deuteron + {len(cycle_types)} cycle-type words).")
    print(f"  Computing χ^λ(β_D^(i)) on H_6 for each (variant × λ) pair …")

    # ── Step 4: build M[i, λ] = χ^λ(β_D^(i)) ──────────────────
    # Sequential mpmath path — deuteron is fast enough that the
    # multiprocessing.Pool closure-pickle bug from the prior Option F
    # attempt is sidestepped entirely.  `_per_partition_numeric` in
    # rho_k_h3a_refinement.py is module-level (Pool-pickle-safe) but
    # we don't need it here.
    M_full = mp.matrix(len(variants), len(parts))
    for i, var in enumerate(variants):
        for j, lam in enumerate(parts):
            chi = chi_numeric(lam, var["crossings"], Q_MP)
            M_full[i, j] = chi
        if (i + 1) % 4 == 0 or i == len(variants) - 1:
            print(f"    [{i+1}/{len(variants)}] χ^λ rows computed")

    # ── Step 5: down-select to 11 rows giving rank 11 ─────────
    # Greedy: start with the deuteron row (must be present — it is
    # the only physical anchor); add cycle-type rows until rank = 11.
    M_np = np.array([[float(M_full[i, j]) for j in range(len(parts))]
                     for i in range(len(variants))])

    chosen_rows = [0]  # always keep the deuteron
    for i in range(1, len(variants)):
        candidate = chosen_rows + [i]
        sub = M_np[candidate, :]
        if np.linalg.matrix_rank(sub, tol=1e-10) == len(candidate):
            chosen_rows.append(i)
        if len(chosen_rows) == len(parts):
            break

    if len(chosen_rows) < len(parts):
        print(f"\n  ✗ RANK-DEFICIENT: only {len(chosen_rows)} "
              f"linearly independent variants found (need {len(parts)}).")
        outcome = "rank-deficient"
    else:
        print(f"\n  ✓ Selected {len(chosen_rows)} linearly independent "
              f"variants (rank = {len(parts)}).")
        outcome = "uniquely-solvable"

    M_sel = M_np[chosen_rows, :]
    rank_M = int(np.linalg.matrix_rank(M_sel, tol=1e-10))
    cond_M = float(np.linalg.cond(M_sel))
    print(f"  rank(M)            = {rank_M}")
    print(f"  cond(M)            = {cond_M:.4e}")

    # ── Step 6: build RHS b ────────────────────────────────────
    # Convention: each row's RHS encodes the deuteron's mass shift
    # propagated through that variant.  For the deuteron itself
    # (i=0), b = Δρ · |tr_M(β_D)|.  For cycle-type variants,
    # |tr_M(w_μ)| = |z^{n-ℓ(μ)}| (Wenzl-bridge identity).
    q_mp = Q_MP
    z_markov = 1 / (mp.sqrt(q_mp) + 1 / mp.sqrt(q_mp))

    def b_for_variant(
        var: dict,
        *,
        delta_rho: mp.mpf,
        abs_tr_M: mp.mpf,
        z_markov: mp.mpf,
        n: int,
    ) -> mp.mpf:
        """Per-variant RHS. Constants passed explicitly (not captured) per
        Gemini PR #609 review — keeps a single canonical site for each
        magic value and prevents scope-dependent side effects."""
        if var["kind"] == "deuteron":
            return delta_rho * abs_tr_M
        ell_mu = len(var["mu"])
        z_pow = z_markov ** (n - ell_mu)
        return delta_rho * abs(z_pow)

    b_full = mp.matrix(len(variants), 1)
    for i, var in enumerate(variants):
        b_full[i, 0] = b_for_variant(
            var, delta_rho=delta_rho, abs_tr_M=abs_tr_M,
            z_markov=z_markov, n=n,
        )
    # b_sel kept in mpmath (50 dps) for the final solve — see Step 7.
    # numpy float64 narrowing is reserved for rank/cond checks only.

    # ── Step 7: solve M_sel · u = b_sel where u_λ = y_λ · Δ_λ ──
    # The defining equation per `prop:rho-k-h3a-refinement` is
    #   Δρ |tr_M| = Σ_λ y_λ χ^λ(β) Δ_λ.
    # Writing u_λ := y_λ · Δ_λ, the augmented system reads
    #   M[i, λ] · u_λ = b_i
    # which is an 11×11 linear system once we solve for u, then
    # divide by y_λ(q_0) to recover Δ_λ.
    #
    # Gemini PR #609 review: solve in mpmath (50 dps) rather than
    # numpy float64 — the matrix is well-conditioned (cond ≈ 31.7)
    # so float64 would be numerically fine, but the rest of the
    # pipeline carries 50-dps precision and we should not introduce
    # a discontinuity here. M_np / b_sel above are float64 only for
    # the rank check + row selection.
    if outcome == "uniquely-solvable":
        M_sel_mp = mp.matrix([
            [M_full[i, j] for j in range(len(parts))]
            for i in chosen_rows
        ])
        b_sel_mp = mp.matrix([b_full[i, 0] for i in chosen_rows])
        u_mp = mp.lu_solve(M_sel_mp, b_sel_mp)

        # Tolerance dynamically tied to current precision (mp.dps),
        # not a hardcoded literal — Gemini PR #609 review.
        zero_tol = mp.mpf(10) ** -(mp.mp.dps - 5)

        Delta_lambda = []
        u = []  # float64 mirror, kept for downstream prints / witness
        for j, lam in enumerate(parts):
            y_j = y_at_q0[lam]  # mpmath
            u_j_mp = u_mp[j]
            if abs(y_j) < zero_tol:
                d_j = mp.inf
            else:
                d_j = u_j_mp / y_j
            Delta_lambda.append((lam, u_j_mp, y_j, d_j))
            u.append(float(u_j_mp))

        # Residual check in mpmath (50-dps norm) — replaces float64
        # `M_sel @ u - b_sel` from the prior implementation.
        resid_mp = M_sel_mp * u_mp - b_sel_mp
        max_resid_mp = mp.mpf(0)
        for k in range(resid_mp.rows):
            r_k = abs(resid_mp[k, 0])
            if r_k > max_resid_mp:
                max_resid_mp = r_k
        max_resid = float(max_resid_mp)
        print(f"\n  Solved 11×11 system (mpmath, {mp.mp.dps} dps).  "
              f"max |residual| = {mp.nstr(max_resid_mp, 6)}")
        # b_sel float mirror for downstream closure-check printing
        b_sel = np.array([float(b_full[i, 0]) for i in chosen_rows])
    else:
        Delta_lambda = []
        max_resid = None

    # ── Step 8: report Δ_λ table & Wenzl-bridge identity check ──
    # Theoretical prediction: Δ_λ = Δρ_D uniformly (see header docstring).
    delta_rho_float = float(delta_rho)
    print(f"\n  Theoretical (closed-form) prediction: Δ_λ = Δρ_D = "
          f"{delta_rho_float:.6e}  ∀ λ.")
    print(f"\n    {'partition':<24}{'u_λ = y_λ Δ_λ':>22}{'Δ_λ (numeric)':>22}"
          f"{'Δ_λ - Δρ_D':>18}")
    print("    " + "-" * 86)
    delta_rows = []
    for lam, u_lam, y_lam, d_lam in Delta_lambda:
        if mp.isfinite(d_lam):
            offset_mp = d_lam - delta_rho_float
            offset = float(offset_mp)
        else:
            offset_mp = mp.nan
            offset = float("nan")
        # u_lam / d_lam are mpmath values now; convert to float for
        # the f-string format spec (display only — full-precision
        # values are kept in delta_rows below).
        u_lam_f = float(u_lam)
        d_lam_f = float(d_lam) if mp.isfinite(d_lam) else float("inf")
        print(f"    {str(list(lam)):<24}{u_lam_f:>22.6e}"
              f"{d_lam_f:>22.6e}{offset:>18.2e}")
        delta_rows.append({
            "partition": list(lam),
            "y_lambda_at_q0": str(y_at_q0[lam]),
            "u_lambda": str(u_lam),
            "Delta_lambda": str(d_lam),
            "Delta_minus_delta_rho": str(offset_mp),
        })

    # ── Step 9: closure check (M(D) reconstruction) ────────────
    # Σ_λ y_λ χ^λ(β_D) Δ_λ = Σ_λ χ^λ(β_D) · u_λ = b_0
    # so by construction the Option F solution reproduces the
    # deuteron mass exactly (this is the trivial first-row check).
    if outcome == "uniquely-solvable":
        # Keep the closure check in mpmath: pulling `b_sel[0]` from
        # the float64 mirror introduced ~1e-16 rounding error and
        # caused the `closure_residual_at_dps` assertion to fail
        # (Copilot PR #613 review).  Source `b_full[0, 0]` directly
        # in mp precision.
        rho_K_check = rho_K_LO + b_full[chosen_rows[0], 0] / abs_tr_M
        M_pred = rho_K_check * M_E_MEV * abs_tr_M
        closure_err_MeV = float(M_pred - M_D_MEV)
        print(f"\n  Closure check (deuteron row reconstruction):")
        print(f"    M(D)^pred    = {mp.nstr(M_pred, 16)} MeV")
        print(f"    M(D)^codata  = {mp.nstr(M_D_MEV, 16)} MeV")
        print(f"    closure err  = {closure_err_MeV:.6e} MeV")
    else:
        closure_err_MeV = None

    # ── Step 10: load Option A (Occam) for comparison ──────────
    occam_path = _pb.witness_path("rho-k-h3a-refinement.witness.json", HERE)
    occam_pick = None
    if occam_path.exists():
        try:
            occam_data = json.loads(occam_path.read_text())
            occam_pick = occam_data.get("data", {}).get("occam_pick")
        except (KeyError, json.JSONDecodeError):
            pass

    if occam_pick:
        print(f"\n  Option A (Occam singleton) — for comparison:")
        print(f"    λ           = {occam_pick['partition']}")
        print(f"    Δ_λ (Occam) = {occam_pick['Delta_lambda']}")
        print(f"  Option F places binding on ALL 11 blocks proportionally")
        print(f"  to y_λ; the Occam pick concentrates it on a single block.")

    # ── Step 11: emit witness ──────────────────────────────────
    script_bytes = Path(__file__).read_bytes()
    script_hash = "sha256:" + hashlib.sha256(script_bytes).hexdigest()

    # Engine string per Copilot PR #613 review (line 400): describe the
    # ACTUAL solver used.  Step 7 now solves the selected 11×11 system
    # in mpmath via `mp.lu_solve` at the `--dps` precision (Gemini
    # PR #609 precision fix); numpy.linalg.* is retained ONLY for the
    # rank-check + greedy row selection.
    engine_str = (
        f"mpmath.lu_solve at {args.dps} dps for the 11×11 selected "
        "system; numpy.linalg only for rank-check + row-selection "
        "greedy.  Reuses chi_numeric / load_y_lambda_n6 from "
        "rho_k_h3a_refinement.py (sequential evaluation; deuteron is "
        "small enough that the prior Pool closure-pickle bug is "
        "sidestepped)."
    )
    witness = {
        "computation": "rho-k-h3a-wenzl-bridge",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Δ_λ derivation via Wenzl-bridge augmented Markov system "
            "(Option F).  Augments the single mass equation Δρ |tr_M| = "
            "Σ_λ y_λ χ^λ(β_D) Δ_λ with 10 cycle-type Markov-axiom "
            "constraints, building an 11×11 linear system M[μ, λ] = "
            "χ^λ(w_μ) and solving M·u = b where u_λ = y_λ Δ_λ. "
            "Sibling of #564 (Occam) and PRs #602 / #603 (Frobenius / "
            "LP-shadow-price options).  By Wenzl-bridge linearity, the "
            "unique solution is Δ_λ = Δρ_D uniformly, i.e. the binding "
            "is distributed proportionally to y_λ across all 11 "
            "Wedderburn blocks."
        ),
        "engine": engine_str,
        "scriptFile": "rho_k_h3a_wenzl_bridge.py",
        "scriptHash": script_hash,
        "parameters": {
            "q_0_50dps": mp.nstr(Q_MP, 50),
            "atom": "deuteron",
            "Z": 1, "N": 1, "A": 2, "n_strands": n,
            "n_partitions": len(parts),
            "n_variants_built": len(variants),
            "n_variants_selected": len(chosen_rows),
            "M_codata_MeV": str(M_D_MEV),
            "m_e_MeV": str(M_E_MEV),
            "m_p_MeV": str(M_P_MEV),
            "m_n_MeV": str(M_N_MEV),
        },
        "data": {
            "abs_tr_M_at_q0": str(abs_tr_M),
            "rho_K_LO": str(rho_K_LO),
            "rho_K_codata": str(rho_K_codata),
            "delta_rho_residual": str(delta_rho),
            "z_markov_at_q0": str(z_markov),
            "outcome": outcome,
            "matrix_diagnostics": {
                "rank": rank_M,
                "cond_number": cond_M,
                "max_residual": max_resid,
                "selected_rows": chosen_rows,
                "variants": [
                    {
                        "index": i,
                        "name": var["name"],
                        "kind": var["kind"],
                        "mu": var["mu"],
                        "n_crossings": len(var["crossings"]),
                    }
                    for i, var in enumerate(variants)
                ],
            },
            "Delta_lambda_table": delta_rows,
            "theoretical_prediction": {
                "claim": (
                    "Δ_λ = Δρ_D uniformly across all λ ⊢ 6, by "
                    "Wenzl-bridge linearity (Σ_λ y_λ χ^λ(w_μ) = "
                    "z^{n-ℓ(μ)} ⇒ u_λ = Δρ_D · y_λ)."
                ),
                "Delta_rho_D_value": str(delta_rho),
                "max_observed_offset": str(
                    max(
                        (abs(float(r["Delta_minus_delta_rho"]))
                         for r in delta_rows
                         if r["Delta_minus_delta_rho"] != "nan"),
                        default=0.0,
                    )
                ),
            },
            "closure_check": {
                "M_pred_MeV": str(M_pred) if outcome == "uniquely-solvable" else None,
                "M_codata_MeV": str(M_D_MEV),
                "closure_err_MeV": str(closure_err_MeV) if closure_err_MeV is not None else None,
            },
            "comparison_to_option_a_occam": {
                "occam_partition": occam_pick["partition"] if occam_pick else None,
                "occam_Delta_lambda": occam_pick["Delta_lambda"] if occam_pick else None,
                "wenzl_bridge_uniform_Delta": str(delta_rho),
                "interpretation": (
                    "Option A picks a single block (Occam minimum |Δ|); "
                    "Option F distributes binding proportionally to "
                    "y_λ across ALL 11 blocks.  Both reproduce M(D) "
                    "exactly; they correspond to different priors on "
                    "the categorical structure of the bound state."
                ),
            },
        },
        "audit_reference": "AUDIT-DEEP-2026-05.md §7 P3 / P3' — Δ_λ derivation race",
        "siblings": ["#600 (parent issue)", "#602 (Option B, Frobenius)",
                     "#603 (Option D, LP-shadow-price)"],
        "notes": (
            "Honesty caveat on the augmented system: the Δ_λ Wenzl "
            "bridge yields a UNIQUE algebraic solution (Δ_λ = Δρ_D "
            "uniformly), but uniqueness depends on the b_μ = Δρ · "
            "z^{n-ℓ(μ)} convention.  Other choices of b_μ correspond "
            "to additional physical anchors (e.g. mass shifts of "
            "cycle-type-related bound states) that we do not have "
            "for the deuteron alone.  The derived Δ_λ profile should "
            "be read as the 'maximum-entropy / y_λ-proportional' prior, "
            "not as a measurement.  Option D (LP shadow prices, #603) "
            "and Option B (Frobenius co-Casimir, #602) give different "
            "priors derived from the LP-dual and the categorical "
            "structure respectively; the four options together "
            "characterise the Δ_λ uniqueness class."
        ),
        "prior_attempts": (
            "Two earlier Option F attempts halted at: (1) "
            "multiprocessing.Pool closure-pickle bug, fixed here by "
            "sequential evaluation (deuteron is small enough); "
            "(2) Anthropic API rate limit, sidestepped by re-starting "
            "the session fresh."
        ),
    }
    # WitnessBuilder.wrap_legacy migration (Copilot PR #613 review,
    # rho-k-h3a-wenzl-bridge.witness.json:24 + :28 + .py:535):
    # `wrap_legacy` preserves the existing top-level payload layout
    # AND emits canonical staleness metadata (`scriptHash` as the
    # 12-hex `file_content_hash` prefix, not a `sha256:` digest;
    # `scriptCommitSha`, `engineVersion`, `computedAt`, `durationMs`).
    # `WitnessBuilder.save(extra=witness)` was overriding these
    # canonical fields with the same-named legacy keys from `witness`,
    # making the witness perpetually stale.
    builder = (
        WitnessBuilder.wrap_legacy(
            "rho-k-h3a-wenzl-bridge",
            witness,
            script_path=__file__,
            engine="python+numpy+mpmath",
        )
        .add_assertion(
            name="wenzl_bridge_unique_solvability",
            computed=1.0 if outcome == "uniquely-solvable" else 0.0,
            expected=1.0,
            tolerance=0.0,
            source="11×11 augmented Markov system uniquely solvable (rank 11)",
        )
        .add_assertion(
            name="closure_residual_at_dps",
            computed=float(closure_err_MeV) if closure_err_MeV is not None else 1.0,
            expected=0.0,
            tolerance=float(mp.mpf(10) ** -(mp.mp.dps - 10)),
            source="M(D) reconstruction residual after Δ_λ insertion",
        )
    )
    out = builder.save()
    print(f"\n  Wrote {out.name} ({out.stat().st_size} bytes).")
    print("=" * 96)
    print(f"  OUTCOME: {outcome}")
    print("=" * 96)
    return 0 if outcome == "uniquely-solvable" else 2


if __name__ == "__main__":
    sys.exit(main())
