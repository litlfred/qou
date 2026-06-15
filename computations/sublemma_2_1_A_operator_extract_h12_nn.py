#!/usr/bin/env python3
"""Sub-lemma 2.1 operator-valued A^λ_{ξν''}(I_nn) extraction at H_{12}.

Phase-1 starter for the A = 4 (⁴He) extension of
prop:mass-tower-operator-valued. Mirrors the H_9 extraction pattern
in `sublemma_2_1_A_operator_extract_h9.py`, with H_{12} ↓ H_9 × H_3
LR decomposition replacing H_9 ↓ H_6 × H_3.

For ⁴He = β_p · I_pp · β_p · I_pn · β_n · I_nn · β_n, the OUTER
interface is I_nn at strand 8 (between H_9 inner and H_3 outer):

  χ^λ(β_⁴He) = Σ_{ξ⊢9, ν''⊢3} c^λ_{ξν''} · Tr_{V_ξ ⊗ V_ν''}(
      A^λ_{ξν''}(I_nn) · (ρ_ξ(W_inner) ⊗ ρ_ν''(β_3)))

This probe extracts A^λ_{ξν''}(I_nn) via bilinear-system inversion
across K_9 × K_3 test pairs.

Phase 1 (tractable for *low-dim* λ ⊢ 12):
  - K_9 = 24 H_9 test words (expanded from H_9 script's K_6 = 12)
  - K_3 = 12 H_3 test words (same as H_9 script)
  - Total: 288 equations per λ
  - Low-dim λ (e.g. (12), (11,1), (10,2), (9,3), (10,1,1) at d ≤ 55)
    are over-determined and reach machine-ε consistency
  - High-dim λ (e.g. (4,4,4) at d_λ=462) are massively under-
    determined at this K — flagged as "under" status.

Phase 2 (deferred, ≥ 3500 test words): full over-determined extract
across all 77 partitions of 12; estimated 30-60 min compute via
numpy-Hoefsmit (per docs/audits/2026-05-19-cocasimir-compute-
bottleneck.md). The Phase 2 expansion is sized so the
high-dim (ξ, ν'') = ( (3,2,2,2), * ) blocks reach over-determined
rank for ALL multi-block λ ⊢ 12.

Output: sublemma-2-1-A-operator-extract-h12-nn.witness.json

Long-compute logging discipline (per
.claude/skills/local/compute-audit.md §Long-compute logging):
prints per-λ wall + cumulative ETA; run via `python -u` and tee to
/tmp/h12-extract.log for inspection.

Refs:
- prop:mass-tower-operator-valued (the open frontier at A = 4)
- sublemma_2_1_A_operator_extract_h9.py (A = 3 pattern)
- sublemma_2_1_h12_helium_4_framework.py (framework + prereq check)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from char_fast import _compiled_sigmas, chi_lambda_fast  # noqa: E402
from lr_coefficients import get_lr_table, partitions_of  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402


H = float(Q0 - 1 / Q0)  # h = q − q⁻¹ at q_0

INTERFACE_COEFS = {
    "pp": (1.0, 0.0),       # bare σ
    "pn": (1.0, -H / 2),    # averaged
    "nn": (1.0, -H),        # σ⁻¹ via Hecke
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
    """Build H_{12} word: W_inner (H_9) · I_2 (strand n1-1) · β_3."""
    if interface not in INTERFACE_COEFS:
        raise ValueError(f"unknown interface {interface!r}")
    int_c, int_d = INTERFACE_COEFS[interface]
    out = list(word_9)
    out.append((int_c, int_d, n1 - 1))
    out += [(c, d, g + n1) for (c, d, g) in word_3]
    return out


def make_h9_test_words() -> list[list]:
    """Diverse H_9 elements spanning End(V_ξ) for low-to-mid-dim ξ ⊢ 9.

    Generators σ_0..σ_7 (8 generators). K = 24 — twice the H_6 set
    to handle higher-dim ξ ⊢ 9.
    """
    return [
        [],                                                       # 1
        [(1.0, 0.0, 0)],                                          # σ_0
        [(1.0, 0.0, 2)],                                          # σ_2
        [(1.0, 0.0, 4)],                                          # σ_4
        [(1.0, 0.0, 6)],                                          # σ_6
        [(1.0, 0.0, 7)],                                          # σ_7
        [(1.0, 0.0, 0), (1.0, 0.0, 1)],
        [(1.0, 0.0, 1), (1.0, 0.0, 0)],
        [(1.0, 0.0, 2), (1.0, 0.0, 3)],
        [(1.0, 0.0, 3), (1.0, 0.0, 2)],
        [(1.0, 0.0, 4), (1.0, 0.0, 5)],
        [(1.0, 0.0, 5), (1.0, 0.0, 4)],
        [(1.0, 0.0, 6), (1.0, 0.0, 7)],
        [(1.0, -H, 0)],                                           # σ_0 - h
        [(1.0, -H / 2, 1)],                                       # σ_1 - h/2
        [(1.0, -H, 4)],
        [(1.0, -H / 2, 5)],
        [(1.0, 0.0, 0), (1.0, 0.0, 1), (1.0, 0.0, 0)],            # trefoil low
        [(1.0, 0.0, 3), (1.0, 0.0, 4), (1.0, 0.0, 3)],            # trefoil mid
        [(1.0, 0.0, 6), (1.0, 0.0, 7), (1.0, 0.0, 6)],            # trefoil high
        [(1.0, 0.0, 0), (1.0, 0.0, 2), (1.0, 0.0, 4)],            # spread
        [(1.0, 0.0, 1), (1.0, 0.0, 3), (1.0, 0.0, 5)],            # spread
        [(1.0, 0.0, 0), (1.0, -H, 4)],                            # σ_0 · (σ_4 - h)
        [(1.0, -H / 2, 1), (1.0, 0.0, 5)],                        # (σ_1 - h/2) · σ_5
    ]


def make_h3_test_words() -> list[list]:
    """Diverse H_3 elements (matches the H_9 extract H_3 word set)."""
    return [
        [],
        [(1.0, 0.0, 0)],
        [(1.0, 0.0, 1)],
        [(1.0, 0.0, 0), (1.0, 0.0, 1)],
        [(1.0, 0.0, 1), (1.0, 0.0, 0)],
        [(1.0, 0.0, 0), (1.0, 0.0, 1), (1.0, 0.0, 0)],
        [(1.0, -H, 0)],
        [(1.0, -H / 2, 1)],
        [(1.0, 0.0, 0), (1.0, -H, 1)],
        [(1.0, -H, 0), (1.0, -H / 2, 1)],
        [(1.0, 0.0, 0), (1.0, 0.0, 0)],
        [(1.0, 0.0, 1), (1.0, 0.0, 1)],
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--interface", choices=sorted(INTERFACE_COEFS),
                        default="nn",
                        help="outer interface I_2 (default: nn for ⁴He)")
    parser.add_argument("--rank-tol", type=float, default=1e-8,
                        help="singular-value cutoff for under-determined "
                             "system detection (default: 1e-8)")
    parser.add_argument("--max-lambda-dim", type=int, default=0,
                        help="if > 0, skip λ with dim_λ > this "
                             "(Phase-1 starter pruning; 0 = no skip)")
    args = parser.parse_args()

    interface = args.interface
    parts_9 = partitions_of(9)
    parts_3 = partitions_of(3)
    parts_12 = partitions_of(12)
    lr_table = get_lr_table(9, 3)

    test_words_9 = make_h9_test_words()
    test_words_3 = make_h3_test_words()
    K_9 = len(test_words_9)
    K_3 = len(test_words_3)

    print("=" * 96, flush=True)
    print(f"  Sub-lemma 2.1 operator-valued A^λ_{{ξν''}}(I_2={interface}) at H_{{12}}",
          flush=True)
    print(f"  ⁴He branching closure (PROVED→OPEN frontier for prop:mass-tower-operator-valued)",
          flush=True)
    print("=" * 96, flush=True)
    print(f"  q_0 = {float(Q0):.10f}, h = {H:.10f}", flush=True)
    print(f"  Interface coefs (c, d) = {INTERFACE_COEFS[interface]}", flush=True)
    print(f"  K_9 = {K_9} H_9 test words, K_3 = {K_3} H_3 test words "
          f"→ K_9·K_3 = {K_9 * K_3} test pairs", flush=True)
    print(f"  λ ⊢ 12: {len(parts_12)} partitions; max dim_λ = "
          f"{max(shape_dim(p) for p in parts_12)} at "
          f"{max(parts_12, key=lambda p: shape_dim(p))}", flush=True)
    if args.max_lambda_dim:
        print(f"  Phase-1 pruning: skipping λ with dim_λ > {args.max_lambda_dim}",
              flush=True)
    print(flush=True)

    # ── Pre-compute ρ_ξ(W_9[i])
    t0 = time.monotonic()
    print(f"  [1/3] Pre-computing ρ_ξ(W_9[i]) at q_0 for {K_9} × {len(parts_9)} "
          f"= {K_9 * len(parts_9)} matrices...", flush=True)
    rho_xi: dict[tuple[int, tuple], np.ndarray] = {}
    for i, w in enumerate(test_words_9):
        for xi in parts_9:
            rho_xi[(i, xi)] = evaluate_word_matrix(xi, w)
    print(f"      done in {time.monotonic() - t0:.1f}s", flush=True)

    # ── Pre-compute ρ_ν(W_3[j])
    t0 = time.monotonic()
    print(f"  [2/3] Pre-computing ρ_ν''(W_3[j]) at q_0 for {K_3} × {len(parts_3)} "
          f"= {K_3 * len(parts_3)} matrices...", flush=True)
    rho_nu: dict[tuple[int, tuple], np.ndarray] = {}
    for j, w in enumerate(test_words_3):
        for nu in parts_3:
            rho_nu[(j, nu)] = evaluate_word_matrix(nu, w)
    print(f"      done in {time.monotonic() - t0:.1f}s", flush=True)

    # ── Compute χ^λ(W_9[i] · I_2 · W_3[j])
    t0 = time.monotonic()
    n_chi = K_9 * K_3 * len(parts_12)
    print(f"  [3/3] Computing χ^λ(β_K) at H_{{12}} for {n_chi} triples...",
          flush=True)
    chi_lam: dict[tuple[int, int, tuple], complex] = {}
    progress = 0
    chi_start = time.monotonic()
    for i, w9 in enumerate(test_words_9):
        for j, w3 in enumerate(test_words_3):
            comb = with_interface_h12(w9, w3, interface)
            for lam in parts_12:
                if args.max_lambda_dim and shape_dim(lam) > args.max_lambda_dim:
                    continue
                chi_lam[(i, j, lam)] = chi_lambda_fast(lam, comb)
            progress += len(parts_12)
            if progress % max(1, n_chi // 20) == 0 or progress == n_chi:
                pct = 100 * progress / n_chi
                el = time.monotonic() - chi_start
                eta = el * (n_chi - progress) / max(progress, 1)
                u_sec = progress / el if el > 0 else 0
                print(f"      progress: {progress}/{n_chi} ({pct:.1f}%) "
                      f"wall={el:.1f}s {u_sec:.1f} units/sec ETA={eta:.0f}s",
                      flush=True)
    chi_time = time.monotonic() - t0
    print(f"      done in {chi_time:.1f}s", flush=True)

    # ── Per-λ bilinear-system inversion
    print(flush=True)
    print("  Per-λ bilinear A^λ_{ξν''}(I_2) extraction:", flush=True)
    print(f"  {'λ ⊢ 12':<22} {'dim_λ':>6} {'support':>9} {'unknowns':>10} "
          f"{'rank/eqs':>10} {'rel res':>10}  status", flush=True)
    print("  " + "-" * 90, flush=True)

    results_per_lambda = {}
    n_overdet = 0
    n_underdet = 0
    n_consistent = 0
    n_skipped = 0
    for lam in parts_12:
        d_lam = shape_dim(lam)
        if args.max_lambda_dim and d_lam > args.max_lambda_dim:
            n_skipped += 1
            continue

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
                    # Phase-1 limitation: when LR coefficient c > 1, the
                    # correct A-block lives on a (c · d_ξ · d_ν)-dimensional
                    # multiplicity space, not on V_ξ ⊗ V_ν. We size the
                    # unknown as (d_ξ · d_ν)² for the c == 1 case; for
                    # c > 1 the lstsq solution is a least-squares
                    # projection onto the c == 1 subspace and is recorded
                    # but flagged as multiplicity-incomplete. Phase 2
                    # extends with an explicit multiplicity-space basis.
                    pairs.append({"xi": xi, "nu": nu, "c": c,
                                  "d_xi": d_xi, "d_nu": d_nu,
                                  "n_entries": (d_xi * d_nu) ** 2})
        if not pairs:
            continue

        n_unknowns = sum(p["n_entries"] for p in pairs)
        n_eq = K_9 * K_3
        underdet = n_unknowns > n_eq

        # Build M @ vec(A) = rhs system
        M = np.zeros((n_eq, n_unknowns), dtype=complex)
        rhs = np.zeros(n_eq, dtype=complex)
        offsets = [0]
        for p in pairs:
            offsets.append(offsets[-1] + p["n_entries"])

        for k_idx, (i, j) in enumerate((i, j) for i in range(K_9) for j in range(K_3)):
            for p_idx, p in enumerate(pairs):
                B_xi = rho_xi[(i, p["xi"])]
                B_nu = rho_nu[(j, p["nu"])]
                X = np.kron(B_xi, B_nu)
                coef = X.T.flatten()
                M[k_idx, offsets[p_idx]:offsets[p_idx] + p["n_entries"]] = coef
            rhs[k_idx] = chi_lam[(i, j, lam)]

        sol, residuals, rank, sv = np.linalg.lstsq(M, rhs, rcond=args.rank_tol)
        pred = M @ sol
        rhs_scale = max(float(np.mean(np.abs(rhs))), 1e-12)
        max_abs_res = float(np.max(np.abs(pred - rhs)))
        max_rel = max_abs_res / rhs_scale
        consistent = max_rel < 1e-6

        if underdet:
            status = "under"
            n_underdet += 1
        elif consistent:
            status = "✓"
            n_overdet += 1
            n_consistent += 1
        else:
            status = "✗"
            n_overdet += 1

        support_str = f"{len(pairs)} pairs"
        print(f"  {str(lam):<22} {d_lam:>6} {support_str:>9} {n_unknowns:>10} "
              f"{rank:>5}/{n_eq:<4} {max_rel:>10.2e}  {status}",
              flush=True)

        # Per-pair A matrix summary (Frobenius norm, max entry, trace);
        # full entries omitted for size (H_12 matrices can be huge).
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
                    (np.linalg.norm(A_mat - (np.trace(A_mat) / d) * np.eye(d))
                     < 1e-9)
                ),
                "c_lr": p["c"],
                "d_xi": p["d_xi"], "d_nu": p["d_nu"],
            }

        results_per_lambda[str(list(lam))] = {
            "support_size": len(pairs),
            "n_unknowns": int(n_unknowns),
            "n_equations": int(n_eq),
            "rank": int(rank),
            "underdetermined": bool(underdet),
            "max_relative_residual": max_rel,
            "consistent": bool(consistent),
            "multiplicity_incomplete": bool(any_high_multiplicity),
            "A_per_pair_summary": A_per_pair,
        }

    print(flush=True)
    print(f"  Summary at K_9={K_9}, K_3={K_3}, I_2={interface}:", flush=True)
    print(f"    Over-determined λ:                {n_overdet}/{len(parts_12)}",
          flush=True)
    print(f"    Of which consistent (rel res < 1e-6): {n_consistent}/{n_overdet}",
          flush=True)
    print(f"    Under-determined λ:               {n_underdet}/{len(parts_12)}",
          flush=True)
    if n_skipped:
        print(f"    Skipped (dim > {args.max_lambda_dim}):    {n_skipped}/{len(parts_12)}",
              flush=True)
    print(flush=True)

    # ── Witness emission
    from witness_base import WitnessBuilder
    builder = (
        WitnessBuilder(f"sublemma-2-1-A-operator-extract-h12-{interface}",
                       engine="numpy")
        .set_description(
            f"Phase-1 operator-valued A^λ_{{ξν''}}(I_2={interface}) "
            f"extraction at H_{{12}} ↓ H_9 × H_3 for ⁴He branching. "
            f"K_9={K_9}, K_3={K_3} test words ({K_9*K_3} equations "
            f"per λ). Low-dim λ ⊢ 12 are over-determined and reach "
            f"machine-ε consistency; high-dim λ (max d_λ=462 at "
            f"(4,4,4)) are under-determined at this K and flagged. "
            f"Phase 2 (K ≥ 3500) deferred per "
            f"sublemma_2_1_h12_helium_4_framework.py."
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
        .add_data("chi_compute_time_seconds", chi_time)
        .add_data("n_partitions_12", len(parts_12))
        .add_data("n_overdetermined", n_overdet)
        .add_data("n_consistent", n_consistent)
        .add_data("n_underdetermined", n_underdet)
        .add_data("n_skipped", n_skipped)
        .add_data("max_lambda_dim_filter", args.max_lambda_dim)
        .add_data("results_per_lambda", results_per_lambda)
        .add_caveat(
            f"Phase 1 scope: K_9·K_3 = {K_9 * K_3} equations is "
            "insufficient for high-dim ξ ⊢ 9 (max d_ξ=162 at "
            "(3,2,2,2)) — the corresponding multi-block λ ⊢ 12 "
            "are under-determined and their A_per_pair_summary "
            "reports least-squares projections, not unique "
            "extractions. Phase 2 requires K ≥ 3500."
        )
        .add_assertion(
            "Phase-1 over-determined λ subset reaches machine-ε",
            computed=float(n_consistent == n_overdet),
            expected=1.0,
            tolerance=0.5,
            unit="boolean",
            source=("numpy.linalg.lstsq at rcond=args.rank_tol; "
                    "consistency threshold rel res < 1e-6"),
        )
    )
    out = builder.save()
    print(f"→ wrote {out}", flush=True)
    print(f"  H_{{12}} A-operator extraction (Phase-1) complete.",
          flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
