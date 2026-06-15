#!/usr/bin/env python3
"""sublemma_2_1_A_operator_extract_h12_nn_streamed.py

Streamed / chunked variant of `sublemma_2_1_A_operator_extract_h12_nn.py`
that processes λ ⊢ 12 ONE AT A TIME, writing incremental checkpoints to
disk after each partition, so the script can resume if killed and so
peak memory stays bounded by per-λ working set (rather than the
22 K-entry χ_λ pre-cache + simultaneous M matrices for all λ at once).

Per CLAUDE.md "Long-compute logging discipline" — emits a progress
line for every λ + every major step, with wall elapsed and ETA.

## Usage

  python3 -u sublemma_2_1_A_operator_extract_h12_nn_streamed.py \\
    --interface nn --max-lambda-dim 55 \\
    --checkpoint /tmp/h12-extract-ckpt.json

If `--checkpoint` exists and has partial results, the script resumes
by skipping λ already in the checkpoint. The final witness is emitted
on completion to `sublemma-2-1-A-operator-extract-h12-{iface}.witness.json`.

## Memory-discipline notes

- ρ_ξ(W_9[i]) and ρ_ν''(W_3[j]) are pre-computed once (fixed cost
  proportional to K_9 × |parts_9| × d_ξ² + K_3 × |parts_3| × d_ν²).
  Worst-case: 24 × 30 × 162² ≈ 19 M complex entries ≈ 300 MB at f64.

- The per-λ M matrix is the killer in the all-at-once version:
  for λ = (4,4,4) (d=462), n_unknowns ≈ 462² × n_LR_pairs and
  M shape (288, n_unknowns) blows past available RAM. The
  `--max-lambda-dim 55` flag caps d_λ to skip those; the streamed
  version additionally `del`s M after each λ and runs `gc.collect()`
  so the high-water-mark is one λ's M, not 77.

- chi_lam values are stored per-λ in a small dict that's discarded
  after the bilinear solve; no global accumulation.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import gc
import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from char_fast import _compiled_sigmas, chi_lambda_fast  # noqa: E402
from lr_coefficients import get_lr_table, partitions_of  # noqa: E402
from murnaghan_nakayama import dim_specht  # noqa: E402  # combinatorial d_λ
from q_parameter import Q as Q0  # noqa: E402

# Re-use the EXACT test-word sets + interface helper from the
# non-streamed sibling so checkpoint / witness comparisons are valid
# (Copilot review #944 r3292557282 + r3292557286: ad-hoc copies
# omitted the empty / identity word and changed the equation system).
from sublemma_2_1_A_operator_extract_h12_nn import (  # noqa: E402
    make_h9_test_words as _make_h9_test_words_orig,
    make_h3_test_words as _make_h3_test_words_orig,
)


H = float(Q0 - 1 / Q0)

INTERFACE_COEFS = {
    "pp": (1.0, 0.0),
    "pn": (1.0, -H / 2),
    "nn": (1.0, -H),
}


def shape_dim(shape: tuple) -> int:
    _, d = _compiled_sigmas(shape, "double")
    return d


def evaluate_word_matrix(shape: tuple, word: list) -> np.ndarray:
    sigmas, dim = _compiled_sigmas(shape, "double")
    if dim == 0:
        return np.zeros((0, 0), dtype=complex)
    q_val = float(Q0)
    sigma_mats = [np.asarray(fn(q_val), dtype=complex) for fn in sigmas]
    I = np.eye(dim, dtype=complex)
    M = I.copy()
    for c, d, g in word:
        if g >= len(sigma_mats):
            return np.zeros((dim, dim), dtype=complex)
        M = M @ (complex(c) * sigma_mats[g] + complex(d) * I)
    return M


def with_interface_h12(word_9: list, word_3: list, interface: str,
                       n1: int = 9) -> list:
    """Concatenate a H_9 word + interface generator + H_3 word into H_12.

    The H_3 word's generators (0..1) are shifted to (n1..n1+1) =
    (9..10) — i.e., σ_{n1+1} and σ_{n1+2} in 1-indexed terms — and
    an interface generator at position n1-1 = 8 connects the two
    sub-algebras. H_12 has generators σ_1..σ_11 (0-indexed: 0..10);
    the shift `+ n1` lands them at indices 9 and 10 (in-range),
    whereas the earlier `+ n1 + 1` shifted to 10 and 11 — and 11
    is out-of-bounds, silently zeroing the matrix (PR #944 r3292555464,
    r3292557276).
    """
    c_iface, d_iface = INTERFACE_COEFS[interface]
    return (
        list(word_9)
        + [(c_iface, d_iface, n1 - 1)]
        + [(c, d, g + n1) for c, d, g in word_3]
    )


def make_h9_test_words() -> list[list]:
    """Re-export of the canonical H_9 test-word set from the sibling
    non-streamed script, so checkpoints + witnesses are comparable."""
    return _make_h9_test_words_orig()


def make_h3_test_words() -> list[list]:
    """Re-export of the canonical H_3 test-word set from the sibling
    non-streamed script."""
    return _make_h3_test_words_orig()


def _load_checkpoint(path: Path | None, expected_config: dict) -> dict:
    """Load checkpoint; validate `run_config` matches `expected_config`.

    A mismatch on interface / K_9 / K_3 / rank_tol / max_lambda_dim /
    test-word hash means the partial results are NOT comparable —
    discard them rather than silently mixing into a hybrid witness
    (PR #944 r3292557290).
    """
    if path is None or not path.exists():
        return {
            "version": 2,
            "run_config": expected_config,
            "results_per_lambda": {},
        }
    try:
        ckpt = json.loads(path.read_text())
    except Exception as e:
        print(f"  WARN: checkpoint load failed ({e}); starting fresh",
              flush=True)
        return {
            "version": 2,
            "run_config": expected_config,
            "results_per_lambda": {},
        }
    rc = ckpt.get("run_config") or {}
    mismatched = [
        k for k in expected_config
        if rc.get(k) != expected_config[k]
    ]
    if mismatched:
        print(
            f"  WARN: checkpoint run_config mismatch on {mismatched}; "
            f"expected={[expected_config[k] for k in mismatched]} "
            f"got={[rc.get(k) for k in mismatched]}; "
            f"starting fresh to avoid hybrid witness",
            flush=True,
        )
        return {
            "version": 2,
            "run_config": expected_config,
            "results_per_lambda": {},
        }
    # Compatible — keep partial results, update run_config to current.
    ckpt["run_config"] = expected_config
    ckpt.setdefault("version", 2)
    ckpt.setdefault("results_per_lambda", {})
    return ckpt


def _save_checkpoint(path: Path | None, ckpt: dict) -> None:
    if path is None:
        return
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(ckpt))
    tmp.replace(path)


def process_one_lambda(
    lam: tuple,
    parts_9: list, parts_3: list,
    test_words_9: list, test_words_3: list,
    combined_words: list,
    rho_xi: dict, rho_nu: dict,
    lr_table: dict,
    rank_tol: float,
    max_lambda_dim: int,
) -> tuple[str, dict | None]:
    """Process a single λ ⊢ 12; return (status, result_or_None).

    Status: 'skipped' | 'no_support' | 'solved' | 'error'.
    """
    # Use combinatorial Specht dimension (hook-length formula) for the
    # dim filter, NOT shape_dim() — the latter calls _compiled_sigmas
    # which BUILDS the full Hoefsmit matrices (~minutes per high-dim λ)
    # just to read the dim. dim_specht is O(|λ|²).
    d_lam = dim_specht(list(lam))
    if max_lambda_dim and d_lam > max_lambda_dim:
        return "skipped", {"d_lam": int(d_lam)}

    # Identify the (ξ, ν) support for this λ
    pairs = []
    any_high_multiplicity = False
    for xi in parts_9:
        for nu in parts_3:
            c = lr_table.get((xi, nu, lam), 0)
            if c > 0:
                if c > 1:
                    any_high_multiplicity = True
                d_xi = shape_dim(xi)
                d_nu = shape_dim(nu)
                pairs.append({"xi": xi, "nu": nu, "c": c,
                              "d_xi": d_xi, "d_nu": d_nu,
                              "n_entries": (d_xi * d_nu) ** 2})
    if not pairs:
        return "no_support", {"d_lam": d_lam}

    K_9 = len(test_words_9)
    K_3 = len(test_words_3)
    n_eq = K_9 * K_3
    n_unknowns = sum(p["n_entries"] for p in pairs)
    underdet = n_unknowns > n_eq

    # Compute chi^λ JUST for this λ (not all-at-once across all λ)
    chi_lam_this = np.zeros(n_eq, dtype=complex)
    for k_idx, (i, j) in enumerate(
        (i, j) for i in range(K_9) for j in range(K_3)
    ):
        chi_lam_this[k_idx] = chi_lambda_fast(lam, combined_words[i][j])

    # Build M @ vec(A) = rhs system
    try:
        M = np.zeros((n_eq, n_unknowns), dtype=complex)
        rhs = chi_lam_this.copy()
        offsets = [0]
        for p in pairs:
            offsets.append(offsets[-1] + p["n_entries"])

        for k_idx, (i, j) in enumerate(
            (i, j) for i in range(K_9) for j in range(K_3)
        ):
            for p_idx, p in enumerate(pairs):
                B_xi = rho_xi[(i, p["xi"])]
                B_nu = rho_nu[(j, p["nu"])]
                X = np.kron(B_xi, B_nu)
                coef = X.T.flatten()
                M[k_idx, offsets[p_idx]:offsets[p_idx] + p["n_entries"]] = coef
                del X, coef

        sol, residuals, rank, sv = np.linalg.lstsq(M, rhs, rcond=rank_tol)
        pred = M @ sol
        rhs_scale = max(float(np.mean(np.abs(rhs))), 1e-12)
        max_abs_res = float(np.max(np.abs(pred - rhs)))
        max_rel = max_abs_res / rhs_scale
        consistent = max_rel < 1e-6

        # Per-pair A matrix summary
        A_per_pair = {}
        for p_idx, p in enumerate(pairs):
            d = p["d_xi"] * p["d_nu"]
            A_flat = sol[offsets[p_idx]:offsets[p_idx] + p["n_entries"]]
            A_mat = A_flat.reshape((d, d), order="C")
            A_per_pair[f"({p['xi']},{p['nu']})"] = {
                "frobenius_norm": float(np.linalg.norm(A_mat)),
                "max_abs_entry": float(np.max(np.abs(A_mat))),
                "trace_real": float(np.trace(A_mat).real),
                "is_scalar_multiple_of_id": bool(
                    d == 1 or
                    (np.linalg.norm(A_mat - (np.trace(A_mat) / d)
                                    * np.eye(d)) < 1e-9)
                ),
                "c_lr": p["c"],
                "d_xi": p["d_xi"], "d_nu": p["d_nu"],
            }
            del A_mat, A_flat

        result = {
            "d_lam": int(d_lam),
            "support_size": len(pairs),
            "n_unknowns": int(n_unknowns),
            "n_equations": int(n_eq),
            "rank": int(rank),
            "underdetermined": bool(underdet),
            "max_relative_residual": float(max_rel),
            "consistent": bool(consistent),
            "multiplicity_incomplete": bool(any_high_multiplicity),
            "A_per_pair_summary": A_per_pair,
        }

        # Free the heaviest per-λ allocations before returning.
        del M, rhs, sol, pred, chi_lam_this
        gc.collect()

        return "solved", result
    except (np.linalg.LinAlgError, MemoryError, ValueError) as e:
        gc.collect()
        return "error", {
            "d_lam": int(d_lam),
            "n_unknowns": int(n_unknowns),
            "n_equations": int(n_eq),
            "support_size": len(pairs),
            "error": f"{type(e).__name__}: {e}",
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--interface", choices=sorted(INTERFACE_COEFS),
                        default="nn")
    parser.add_argument("--rank-tol", type=float, default=1e-8)
    parser.add_argument("--max-lambda-dim", type=int, default=55)
    parser.add_argument("--checkpoint", type=Path, default=None,
                        help="optional JSON checkpoint path; resumes if "
                             "exists, writes incrementally per λ")
    args = parser.parse_args()
    interface = args.interface

    print("=" * 96, flush=True)
    print(f"  Sub-lemma 2.1 operator-valued A^λ_{{ξν''}}(I_2={interface}) "
          f"at H_{{12}} — STREAMED", flush=True)
    print(f"  q_0 = {float(Q0):.10f}, h = {H:.10f}", flush=True)
    print(f"  Interface coefs (c, d) = {INTERFACE_COEFS[interface]}", flush=True)
    print(f"  Phase-1 pruning: skipping λ with dim_λ > {args.max_lambda_dim}",
          flush=True)
    print(f"  Checkpoint: {args.checkpoint or '(disabled)'}", flush=True)

    # Pre-stamp the WitnessBuilder start_time so durationMs reflects
    # the FULL wall-clock from script start, not just the post-loop
    # builder construction (PR #944 r3292557294).
    t_script_start = time.monotonic()

    t_setup = time.monotonic()
    print(f"  [setup] loading partitions + LR table...", flush=True)
    parts_9 = partitions_of(9)
    parts_3 = partitions_of(3)
    parts_12 = partitions_of(12)
    lr_table = get_lr_table(9, 3)
    print(f"      parts_9={len(parts_9)}, parts_3={len(parts_3)}, "
          f"parts_12={len(parts_12)}, lr_table={len(lr_table)} entries "
          f"({time.monotonic() - t_setup:.1f}s)", flush=True)

    test_words_9 = make_h9_test_words()
    test_words_3 = make_h3_test_words()
    K_9 = len(test_words_9)
    K_3 = len(test_words_3)
    print(f"  K_9 = {K_9}, K_3 = {K_3}, K_9·K_3 = {K_9*K_3} equations/λ",
          flush=True)

    # Pre-compute ρ_ξ + ρ_ν (fixed cost, retained throughout)
    t0 = time.monotonic()
    print(f"  [pre-1] ρ_ξ(W_9[i]) for {K_9}×{len(parts_9)} = "
          f"{K_9*len(parts_9)} matrices...", flush=True)
    rho_xi: dict = {}
    for i, w in enumerate(test_words_9):
        for xi in parts_9:
            rho_xi[(i, xi)] = evaluate_word_matrix(xi, w)
    print(f"      done ({time.monotonic() - t0:.1f}s)", flush=True)

    t0 = time.monotonic()
    print(f"  [pre-2] ρ_ν(W_3[j]) for {K_3}×{len(parts_3)} = "
          f"{K_3*len(parts_3)} matrices...", flush=True)
    rho_nu: dict = {}
    for j, w in enumerate(test_words_3):
        for nu in parts_3:
            rho_nu[(j, nu)] = evaluate_word_matrix(nu, w)
    print(f"      done ({time.monotonic() - t0:.1f}s)", flush=True)

    # Pre-compute combined words (small list, no λ dependence)
    t0 = time.monotonic()
    print(f"  [pre-3] combined words W_9[i] · I_2 · W_3[j] for "
          f"{K_9*K_3} pairs...", flush=True)
    combined_words: list[list] = [
        [with_interface_h12(w9, w3, interface) for w3 in test_words_3]
        for w9 in test_words_9
    ]
    print(f"      done ({time.monotonic() - t0:.1f}s)", flush=True)

    # Resume from checkpoint if present (with run_config validation)
    run_config = {
        "interface": interface,
        "K_9": K_9,
        "K_3": K_3,
        "rank_tol": args.rank_tol,
        "max_lambda_dim": args.max_lambda_dim,
        # Coarse fingerprint of the test-word definitions so a change
        # to the H_9 / H_3 word lists invalidates the checkpoint.
        "test_word_h9_count": len(test_words_9),
        "test_word_h3_count": len(test_words_3),
    }
    ckpt = _load_checkpoint(args.checkpoint, run_config)
    done_lams = set(ckpt.get("results_per_lambda", {}).keys())
    if done_lams:
        print(f"  [resume] {len(done_lams)} λ found in checkpoint; "
              f"skipping those", flush=True)

    # Per-λ stream
    print(flush=True)
    print(f"  Per-λ extraction (streamed):", flush=True)
    n_overdet = 0
    n_underdet = 0
    n_consistent = 0
    n_skipped = 0
    n_no_support = 0
    n_error = 0
    t_loop = time.monotonic()
    for lam_idx, lam in enumerate(parts_12, start=1):
        lam_key = str(list(lam))
        if lam_key in done_lams:
            r = ckpt["results_per_lambda"][lam_key]
            status_str = "resumed"
            # Update counters from the resumed result so the final
            # summary + witness reflect the full run (PR #944
            # r3292555471).
            st = r.get("status")
            if st == "skipped_dim_filter":
                n_skipped += 1
            elif st == "no_support":
                n_no_support += 1
            elif st == "error":
                n_error += 1
            elif st == "solved":
                if r.get("underdetermined"):
                    n_underdet += 1
                else:
                    n_overdet += 1
                    if r.get("consistent"):
                        n_consistent += 1
        else:
            status, result = process_one_lambda(
                lam, parts_9, parts_3,
                test_words_9, test_words_3, combined_words,
                rho_xi, rho_nu, lr_table,
                args.rank_tol, args.max_lambda_dim,
            )
            if status == "skipped":
                n_skipped += 1
                ckpt["results_per_lambda"][lam_key] = {
                    "status": "skipped_dim_filter", **result,
                }
            elif status == "no_support":
                n_no_support += 1
                ckpt["results_per_lambda"][lam_key] = {
                    "status": "no_support", **result,
                }
            elif status == "error":
                n_error += 1
                ckpt["results_per_lambda"][lam_key] = {
                    "status": "error", **result,
                }
            else:  # solved
                ckpt["results_per_lambda"][lam_key] = {
                    "status": "solved", **result,
                }
                if result["underdetermined"]:
                    n_underdet += 1
                else:
                    n_overdet += 1
                    if result["consistent"]:
                        n_consistent += 1
            r = ckpt["results_per_lambda"][lam_key]
            status_str = r.get("status", "unknown")
            _save_checkpoint(args.checkpoint, ckpt)

        elapsed = time.monotonic() - t_loop
        eta_s = elapsed * (len(parts_12) - lam_idx) / max(lam_idx, 1)
        rate = lam_idx / max(elapsed, 1e-9)
        d_lam = r.get("d_lam", "?")
        max_rel = r.get("max_relative_residual")
        max_rel_str = f"{max_rel:.2e}" if max_rel is not None else "—"
        # units/sec rate per CLAUDE.md long-compute logging discipline
        # (PR #944 r3292555475).
        print(f"  λ={lam_key:<22} d={d_lam:>4}  status={status_str:<14} "
              f"rel_res={max_rel_str:<9}  "
              f"[{lam_idx}/{len(parts_12)}] wall={elapsed:.1f}s "
              f"rate={rate:.2f}λ/s ETA={eta_s:.0f}s", flush=True)

    total_wall = time.monotonic() - t_loop
    print(flush=True)
    print(f"  Summary at K_9={K_9}, K_3={K_3}, I_2={interface}:", flush=True)
    print(f"    Over-determined consistent: {n_consistent}/{n_overdet}",
          flush=True)
    print(f"    Under-determined:           {n_underdet}", flush=True)
    print(f"    No support:                 {n_no_support}", flush=True)
    print(f"    Skipped (dim > {args.max_lambda_dim}):     {n_skipped}",
          flush=True)
    print(f"    Errored:                    {n_error}", flush=True)
    print(f"    Total wall (per-λ loop):    {total_wall:.1f}s", flush=True)

    # Emit witness from checkpoint
    from witness_base import WitnessBuilder
    builder = (
        WitnessBuilder(
            f"sublemma-2-1-A-operator-extract-h12-{interface}",
            engine="numpy",
            start_time=t_script_start,
        )
        .set_description(
            f"Phase-1 operator-valued A^λ_{{ξν''}}(I_2={interface}) "
            f"extraction at H_{{12}} ↓ H_9 × H_3 — STREAMED variant. "
            f"K_9={K_9}, K_3={K_3} test words ({K_9*K_3} equations / λ). "
            f"Processes λ ⊢ 12 one at a time, writing per-λ "
            f"checkpoint to avoid OOM at high d_λ. max_lambda_dim "
            f"filter: {args.max_lambda_dim}."
        )
        .set_audit_only(
            "docs/coordination/2026-05-20-lambda-p-followons-ledger.md"
        )
        .add_data("interface_type", interface)
        .add_data("interface_coefs", list(INTERFACE_COEFS[interface]))
        .add_data("q_0", float(Q0))
        .add_data("h", H)
        .add_data("K_9_h9_test_words", K_9)
        .add_data("K_3_h3_test_words", K_3)
        .add_data("n_test_pairs", K_9 * K_3)
        .add_data("n_partitions_12", len(parts_12))
        .add_data("n_overdetermined", n_overdet)
        .add_data("n_consistent", n_consistent)
        .add_data("n_underdetermined", n_underdet)
        .add_data("n_no_support", n_no_support)
        .add_data("n_error", n_error)
        .add_data("n_skipped", n_skipped)
        .add_data("max_lambda_dim_filter", args.max_lambda_dim)
        .add_data("results_per_lambda", ckpt["results_per_lambda"])
        .add_data("streamed", True)
        .add_caveat(
            f"Phase 1 streamed run: K_9·K_3 = {K_9*K_3} equations is "
            "insufficient for high-dim λ; under-determined entries "
            "report least-squares projections. Phase 2 requires "
            "K ≥ 3500 and a larger memory budget."
        )
        .add_assertion(
            "Phase-1 over-determined λ subset reaches consistency",
            computed=float(n_consistent == n_overdet),
            expected=1.0,
            tolerance=0.5,
            unit="boolean",
            source=("per-λ numpy.linalg.lstsq at rcond=args.rank_tol; "
                    "consistency threshold rel res < 1e-6"),
        )
    )
    out = builder.save()
    print(f"→ wrote {out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
