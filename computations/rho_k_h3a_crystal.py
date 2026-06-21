#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath/sympy consumer; symbolic-q
# polynomials live downstream in hoefsmit_symbolic / y_lambda_wenzl_bridge.
"""rho_K refinement option E — Kashiwara crystal weights c_lambda(q) for the deuteron.

REPLACES the Occam single-partition heuristic in
``rho_k_h3a_refinement.py`` (which picks the partition with smallest
|Delta_lambda| from a 1-equation, 11-unknowns underdetermined system)
by a STRUCTURAL choice for the per-block binding fraction:

    Delta_lambda(K)  ==  c_lambda  (Kashiwara symmetric-crystal weight)

This script does NOT modify ``rho_k_h3a_refinement.py``. It builds an
independent crystal-side derivation of Delta_lambda from the new
crystal-bases primitives that landed via PR #599
(commits ``3d22baee`` / ``1eca8880`` / ``6b4a4e21``).

Definition of c_lambda(q)
=========================

The Kashiwara symmetric-crystal carries a NATURAL q-deformed weight on
each connected component B(lambda). Per AGENTS.md sec.7b shortcut #3
("Demazure-fiber Markov-trace functional"), the canonical structural
weight on B(lambda) at the longest Weyl element w_0 is the principal
q-specialisation of the Schur polynomial:

    c_lambda(q) := s_lambda(1, q, q^2, ..., q^{n-1})
                 = q^{n(lambda)} * prod_{x in lambda} (1 - q^{n+c(x)})/(1 - q^{h(x)})

This is the Macdonald hook-content formula. Verified equality with the
Demazure character ``D_{w_0}(lambda)`` at principal specialisation by
``demazure_markov_trace.verify_w0_equals_schur`` (witness:
``demazure-markov-trace.witness.json``).

At q -> 1, c_lambda(1) = f^lambda * (n-1)! / hook product * |something|
= dim V_lambda for sl_n, which equals the cardinality of the Kashiwara
crystal ``|B(lambda, n)|`` (Weyl dimension formula). The crystal-bases
primitives in ``crystal_basis.py`` enumerate B(lambda, n); we
independently confirm that ``c_lambda(1) == |B(lambda, 6)|`` for every
lambda |- 6 with at most 6 parts (a self-test).

Type-B fold-orbit closure (CPT)
-------------------------------

The CPT-saturation / Type-B fold-orbit closure work
(commits ``4ca31f17`` / ``657a4f82`` per the parent-PR brief) uses the
SAME Kashiwara symmetric-crystal weights to identify which Wedderburn
blocks are populated by stable matter. Plugging c_lambda(q) into
Delta_lambda is therefore the structurally-consistent next step:
the per-block binding fraction is the structural weight of the block
in the Kashiwara crystal of the Hecke algebra H_n(q).

Honest reporting policy
-----------------------

The mass-equation residual  Delta_rho_K - (1/|tr_M|) sum_lambda y_lambda chi_lambda Delta_lambda
is computed AS-IS. We do NOT scale Delta_lambda to force closure.
If c_lambda overshoots / undershoots the binding-energy target,
the residual is reported in MeV and ppm; a normalisation scalar
``alpha_E`` such that  alpha_E * (sum c_lambda * y_lambda * chi_lambda)
= target  is also reported (interpretation: factor by which the
crystal weights would need to be scaled to close exactly), but
``alpha_E`` is purely a diagnostic — the witness does NOT silently
apply it.

Output: ``rho-k-h3a-crystal.witness.json`` with full per-partition data
and a side-by-side ``comparison_to_occam`` block.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from multiprocessing import Pool, cpu_count
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
# Reused machinery from the Occam baseline (do NOT modify upstream).
from rho_k_h3a_refinement import (  # noqa: E402
    chi_numeric,
    deuteron_canonical_crossings,
    evaluate_at_q0,
    load_deuteron_tr_M,
    load_y_lambda_n6,
    partitions_of_n,
    _per_partition_numeric,
    _per_partition_symbolic,
)
from codata_constants import M_E_MEV, M_P_MEV, M_N_MEV, M_D_MEV  # noqa: E402
from crystal_basis import crystal_B  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from partition_utils import hook_lengths_with_cells as hook_lengths  # noqa: E402

set_compute_dps()


# ---------------------------------------------------------------------
#  c_lambda(q) — principal q-specialisation of the Schur polynomial
# ---------------------------------------------------------------------


def n_lambda(shape: tuple[int, ...]) -> int:
    """n(lambda) = sum_i (i - 1) * lambda_i  (1-indexed convention)."""
    return sum(i * shape[i] for i in range(len(shape)))


def c_lambda_q(shape: tuple[int, ...], n_strands: int, q: mp.mpf) -> mp.mpf:
    """Kashiwara symmetric-crystal weight at parameter q.

    Defined as the principal q-specialisation of the Schur polynomial
    s_lambda(x_1, ..., x_{n_strands}) at x_i = q^{i-1}, evaluated by
    the Macdonald hook-content formula:

        c_lambda(q) = q^{n(lambda)} * prod_{(i,j) in lambda}
                          (1 - q^{n_strands + (j-i)}) / (1 - q^{h(i,j)})

    All arithmetic in ``mpmath`` at the current precision
    (``mp.mp.dps``). At q -> 1 this evaluates to dim V_lambda = |B(lambda, n_strands)|.
    """
    if not shape:
        return mp.mpf(1)
    if max(shape, default=0) > 0 and len(shape) > n_strands:
        # Empty crystal: lambda has more rows than letters available.
        return mp.mpf(0)

    q = mp.mpf(q)
    out = q ** n_lambda(shape)
    for (i, j, h) in hook_lengths(shape):
        c = j - i  # content of cell
        num = mp.mpf(1) - q ** (n_strands + c)
        den = mp.mpf(1) - q ** h
        out = out * num / den
    return out


def c_lambda_at_one_via_crystal(shape: tuple[int, ...], n_strands: int) -> int:
    """|B(lambda, n_strands)|  — the q -> 1 limit of c_lambda(q),
    computed by direct BFS on the Kashiwara crystal (validates the
    Macdonald hook-content formula combinatorially).
    """
    if shape and len(shape) > n_strands:
        return 0
    return len(crystal_B(shape, n_strands))


# ---------------------------------------------------------------------
#  Self-test: c_lambda(1) == |B(lambda, n)|  for all lambda |- 6
# ---------------------------------------------------------------------


def selftest_crystal_dim(n: int = 6) -> list[dict]:
    """For each partition lambda |- n with at most n parts, verify that
    the Macdonald hook-content closed form ``c_lambda(1)`` agrees with
    the BFS enumeration of the Kashiwara crystal ``|B(lambda, n)|``.
    """
    rows = []
    one = mp.mpf(1) + mp.mpf("1e-40")  # avoid divide-by-zero singularities at h=n+c
    # Use a near-1 value via L'Hopital-stable formula:
    # c_lambda(1) = prod_{(i,j)} (n + c) / h
    out_all_ok = True
    for shape in partitions_of_n(n):
        if len(shape) > n:
            continue
        # Direct closed-form at q=1 (no divergence — both sides have
        # matching factors of (1-q) that cancel; use the Weyl formula
        # directly: dim = prod_{(i,j)} (n + j - i) / h(i,j)).
        prod = mp.mpf(1)
        for (i, j, h) in hook_lengths(shape):
            prod *= mp.mpf(n + (j - i)) / mp.mpf(h)
        c_at_1 = prod
        # Reference: Kashiwara crystal cardinality
        cardinal = c_lambda_at_one_via_crystal(shape, n)
        ok = abs(c_at_1 - mp.mpf(cardinal)) < mp.mpf("1e-30")
        rows.append({
            "partition": list(shape),
            "c_lambda_at_1_macdonald": str(c_at_1),
            "B_lambda_n_cardinality": cardinal,
            "agree": bool(ok),
        })
        out_all_ok = out_all_ok and ok
    return rows, out_all_ok


# ---------------------------------------------------------------------
#  Main pipeline
# ---------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--symbolic", action="store_true",
        help="Use the slow symbolic-q chi^lambda path (sympy). "
             "Default: numeric mpmath path (~100x faster, "
             "bit-identical to the symbolic path at q_0)."
    )
    parser.add_argument(
        "--workers", type=int, default=min(cpu_count(), 11),
        help="multiprocessing.Pool size (default = min(cpu_count, 11))."
    )
    args = parser.parse_args()
    engine = "symbolic" if args.symbolic else "numeric"

    print("=" * 96)
    print("  rho_K H_{3A} refinement — option E (Kashiwara crystal weights)")
    print(f"  Replaces Occam single-partition heuristic for DEUTERON. engine={engine}")
    print("=" * 96)

    print(f"\n  q_0 = {mp.nstr(Q_MP, 25)}")
    print(f"  m_e = {mp.nstr(M_E_MEV, 8)} MeV (CODATA)")
    print(f"  m_p = {mp.nstr(M_P_MEV, 8)} MeV (CODATA)")
    print(f"  m_n = {mp.nstr(M_N_MEV, 8)} MeV (CODATA)")
    print(f"  M(D) = {mp.nstr(M_D_MEV, 12)} MeV (CODATA)")

    # ---- Step 1: |tr_M(beta_D)|  (reused from Occam baseline) ----
    tr_M = load_deuteron_tr_M()
    abs_tr_M = abs(tr_M)
    print(f"\n  |tr_M(beta_D)| (50 dps) = {mp.nstr(abs_tr_M, 30)}")

    # ---- Step 2: rho_K^LO and the residual to be explained ----
    rho_K_LO = (M_P_MEV + M_N_MEV) / (M_E_MEV * abs_tr_M)
    M_pred_LO = rho_K_LO * M_E_MEV * abs_tr_M  # = m_p + m_n by construction
    rho_K_codata = M_D_MEV / (M_E_MEV * abs_tr_M)
    delta_rho = rho_K_codata - rho_K_LO
    err_pct_LO = (M_pred_LO - M_D_MEV) / M_D_MEV * 100
    target = delta_rho * abs_tr_M  # = sum_lambda y_lambda chi_lambda Delta_lambda
    print(f"\n  rho_K^LO       = {mp.nstr(rho_K_LO, 25)}")
    print(f"  rho_K^CODATA   = {mp.nstr(rho_K_codata, 25)}")
    print(f"  Delta_rho      = {mp.nstr(delta_rho, 25)}")
    print(f"  M^LO(D)        = {mp.nstr(M_pred_LO, 14)} MeV  "
          f"(err = {mp.nstr(err_pct_LO, 4)} %)")
    print(f"  binding gap    = {mp.nstr(M_pred_LO - M_D_MEV, 8)} MeV  "
          f"(should be approx +2.225 MeV deuteron binding)")
    print(f"  target         = Delta_rho * |tr_M| = {mp.nstr(target, 16)}")

    # ---- Step 3: per-lambda y_lambda and chi^lambda(beta_D) at q_0 ----
    print("\n  Loading y_lambda(q_0) from Wenzl-bridge witness ...")
    y_lam_sym = load_y_lambda_n6()
    crossings = deuteron_canonical_crossings()
    parts = partitions_of_n(6)
    assert len(parts) == 11, f"expected 11 partitions, got {len(parts)}"
    print(f"  Computing chi^lambda(beta_D) via {engine} engine "
          f"({len(parts)} partitions, {len(crossings)} crossings on H_6) ...")

    q_str_50 = mp.nstr(Q_MP, 50)
    worker = _per_partition_symbolic if args.symbolic else _per_partition_numeric
    work = [(lam, crossings, q_str_50, mp.mp.dps) for lam in parts]

    chi_at_q0 = {}
    if args.workers > 1 and len(parts) > 1:
        with Pool(args.workers) as pool:
            for lam, chi_str in pool.imap_unordered(worker, work):
                chi_at_q0[lam] = mp.mpf(chi_str)
    else:
        for w in work:
            lam, chi_str = worker(w)
            chi_at_q0[lam] = mp.mpf(chi_str)

    # ---- Step 4: c_lambda(q_0) — Kashiwara crystal weights ----
    print("\n  Computing Kashiwara crystal weights c_lambda(q_0) "
          "(Macdonald hook-content) ...")
    n_strands = 6
    c_at_q0: dict[tuple, mp.mpf] = {}
    c_at_one: dict[tuple, mp.mpf] = {}
    for lam in parts:
        # At q_0 (q-deformed crystal weight)
        c_at_q0[lam] = c_lambda_q(lam, n_strands, Q_MP)
        # At q -> 1 (cardinality of Kashiwara crystal)
        if len(lam) > n_strands:
            c_at_one[lam] = mp.mpf(0)
        else:
            prod = mp.mpf(1)
            for (i, j, h) in hook_lengths(lam):
                prod *= mp.mpf(n_strands + (j - i)) / mp.mpf(h)
            c_at_one[lam] = prod

    # ---- Step 5: cross-check c_lambda(1) == |B(lambda, 6)| ----
    print("\n  Self-test: c_lambda(1) == |B(lambda, 6)| (Weyl dimension)?")
    selftest_rows, selftest_ok = selftest_crystal_dim(6)
    print(f"  {'lambda':<24}{'c_lambda(1) closed':>22}{'|B(lambda,6)| BFS':>22}{'agree':>8}")
    print("  " + "-" * 76)
    for r in selftest_rows:
        print(f"  {str(r['partition']):<24}{r['c_lambda_at_1_macdonald'][:20]:>22}"
              f"{r['B_lambda_n_cardinality']:>22}{('OK' if r['agree'] else 'FAIL'):>8}")
    if not selftest_ok:
        print("  *** WARNING: Macdonald hook-content disagrees with crystal BFS!")
    else:
        print("  All shapes agree: c_lambda(1) matches |B(lambda, 6)| exactly.")

    # ---- Step 6: Schur-Weyl identity sanity check ----
    sw_sum = mp.mpf(0)
    rows_per_lambda = []
    for lam in parts:
        chi_q0 = chi_at_q0[lam]
        if lam not in y_lam_sym:
            raise RuntimeError(f"y_lambda for partition {lam} missing from witness")
        y_q0 = evaluate_at_q0(y_lam_sym[lam])
        contribution = y_q0 * chi_q0
        sw_sum += contribution
        rows_per_lambda.append({
            "partition": list(lam),
            "y_lambda_at_q0": str(y_q0),
            "chi_lambda_beta_D_at_q0": str(chi_q0),
            "y_chi_product": str(contribution),
            "abs_y_chi": str(abs(contribution)),
            "c_lambda_at_q0": str(c_at_q0[lam]),
            "c_lambda_at_one": str(c_at_one[lam]),
        })

    sw_err = abs(sw_sum - tr_M)
    sw_match = sw_err < mp.mpf("1e-40")
    print(f"\n  Schur-Weyl identity check:")
    print(f"    sum_lambda y_lambda chi^lambda(beta_D) = {mp.nstr(sw_sum, 30)}")
    print(f"    tr_M(beta_D)                          = {mp.nstr(tr_M, 30)}")
    print(f"    |residual|                            = {mp.nstr(sw_err, 6)}  "
          f"{'OK' if sw_match else 'FAIL'}")

    # ---- Step 7: Plug Delta_lambda := c_lambda into the mass equation ----
    # Two variants to report side-by-side:
    #   (a)  Delta_lambda = c_lambda(q_0)         -- q-deformed crystal weight
    #   (b)  Delta_lambda = c_lambda(1)           -- crystal cardinality |B(lambda, n)|
    print("\n  Plugging Delta_lambda := c_lambda into the mass equation ...")
    print(f"\n    target = Delta_rho * |tr_M| = {mp.nstr(target, 16)}")
    print()
    print(f"    {'partition':<24}{'y chi':>14}{'c_lambda(q_0)':>20}{'c_lambda(1)':>16}")
    print("    " + "-" * 74)

    sum_q0 = mp.mpf(0)
    sum_one = mp.mpf(0)
    for lam in parts:
        chi_q0 = chi_at_q0[lam]
        y_q0 = evaluate_at_q0(y_lam_sym[lam])
        y_chi = y_q0 * chi_q0
        sum_q0 += y_chi * c_at_q0[lam]
        sum_one += y_chi * c_at_one[lam]
        print(f"    {str(list(lam)):<24}{mp.nstr(y_chi, 6):>14}"
              f"{mp.nstr(c_at_q0[lam], 6):>20}"
              f"{mp.nstr(c_at_one[lam], 6):>16}")

    print(f"\n    sum_lambda y_lambda chi^lambda c_lambda(q_0) = {mp.nstr(sum_q0, 16)}")
    print(f"    sum_lambda y_lambda chi^lambda c_lambda(1)   = {mp.nstr(sum_one, 16)}")
    print(f"    target                                     = {mp.nstr(target, 16)}")

    residual_q0 = target - sum_q0
    residual_one = target - sum_one

    print(f"\n  Residuals (target - sum):")
    print(f"    residual at q_0 = {mp.nstr(residual_q0, 12)}")
    print(f"    residual at q=1 = {mp.nstr(residual_one, 12)}")

    # Honest-reporting diagnostics: the scalar alpha_E that WOULD close
    # the equation if we scaled Delta_lambda := alpha_E * c_lambda. We
    # report alpha_E but do NOT apply it.
    if abs(sum_q0) > mp.mpf("1e-40"):
        alpha_E_q0 = target / sum_q0
    else:
        alpha_E_q0 = mp.mpf("inf")
    if abs(sum_one) > mp.mpf("1e-40"):
        alpha_E_one = target / sum_one
    else:
        alpha_E_one = mp.mpf("inf")

    print(f"\n  Diagnostic normalisations (would-close-it scalars; NOT applied):")
    print(f"    alpha_E (q_0) = {mp.nstr(alpha_E_q0, 12)}")
    print(f"    alpha_E (q=1) = {mp.nstr(alpha_E_one, 12)}")

    # Convert residuals to physical units
    rho_K_pred_q0 = rho_K_LO + sum_q0 / abs_tr_M
    rho_K_pred_one = rho_K_LO + sum_one / abs_tr_M
    M_pred_q0 = rho_K_pred_q0 * M_E_MEV * abs_tr_M
    M_pred_one = rho_K_pred_one * M_E_MEV * abs_tr_M
    err_q0_MeV = M_pred_q0 - M_D_MEV
    err_one_MeV = M_pred_one - M_D_MEV
    err_q0_ppm = err_q0_MeV / M_D_MEV * mp.mpf("1e6")
    err_one_ppm = err_one_MeV / M_D_MEV * mp.mpf("1e6")
    relative_q0 = sum_q0 / target if abs(target) > mp.mpf("1e-40") else mp.mpf("nan")
    relative_one = sum_one / target if abs(target) > mp.mpf("1e-40") else mp.mpf("nan")

    print(f"\n  Closure verification (Delta_lambda := c_lambda inserted into rho_K):")
    print(f"    [q_0 variant]")
    print(f"      M(D)^pred       = {mp.nstr(M_pred_q0, 16)} MeV")
    print(f"      M(D)^codata     = {mp.nstr(M_D_MEV, 16)} MeV")
    print(f"      closure error   = {mp.nstr(err_q0_MeV, 6)} MeV  "
          f"({mp.nstr(err_q0_ppm, 4)} ppm)")
    print(f"      sum / target    = {mp.nstr(relative_q0, 6)} "
          f"(1.0 = exact closure)")
    print(f"    [q=1 variant]")
    print(f"      M(D)^pred       = {mp.nstr(M_pred_one, 16)} MeV")
    print(f"      closure error   = {mp.nstr(err_one_MeV, 6)} MeV  "
          f"({mp.nstr(err_one_ppm, 4)} ppm)")
    print(f"      sum / target    = {mp.nstr(relative_one, 6)} "
          f"(1.0 = exact closure)")

    # Headline outcome
    if abs(relative_q0 - 1) < mp.mpf("0.01"):
        outcome = "CLOSE_TO_CLOSE"
    elif relative_q0 > 1:
        outcome = "OVERSHOOT"
    elif relative_q0 < 0:
        outcome = "WRONG_SIGN"
    else:
        outcome = "UNDERSHOOT"
    print(f"\n  Outcome (q_0 variant): {outcome}  "
          f"(sum/target = {mp.nstr(relative_q0, 6)})")

    # ---- Step 8: emit witness ----
    script_bytes = Path(__file__).read_bytes()
    script_hash = "sha256:" + hashlib.sha256(script_bytes).hexdigest()

    # Per-partition rich row
    per_lambda_full = []
    for r, lam in zip(rows_per_lambda, parts):
        y_chi = mp.mpf(r["y_chi_product"])
        c_q0 = c_at_q0[lam]
        c_one = c_at_one[lam]
        contrib_q0 = y_chi * c_q0
        contrib_one = y_chi * c_one
        per_lambda_full.append({
            "partition": list(lam),
            "y_lambda_at_q0": r["y_lambda_at_q0"],
            "chi_lambda_beta_D_at_q0": r["chi_lambda_beta_D_at_q0"],
            "y_chi_product": r["y_chi_product"],
            "c_lambda_at_q0_macdonald": str(c_q0),
            "c_lambda_at_one_macdonald": str(c_one),
            "B_lambda_n_cardinality": (
                c_lambda_at_one_via_crystal(lam, n_strands)
                if len(lam) <= n_strands else 0
            ),
            "Delta_lambda_q0": str(c_q0),
            "Delta_lambda_one": str(c_one),
            "contribution_q0": str(contrib_q0),
            "contribution_one": str(contrib_one),
        })

    # Comparison to Occam baseline
    occam_path = _pb.witness_path("rho-k-h3a-refinement.witness.json", HERE)
    if occam_path.exists():
        occam_witness = json.loads(occam_path.read_text())
        occam_pick = occam_witness["data"]["occam_pick"]
        occam_321 = occam_witness["data"]["balanced_321_heuristic"]
    else:
        occam_pick = None
        occam_321 = None

    witness = {
        "computation": "rho-k-h3a-crystal",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "Option E for the H_{3A} per-block binding fraction "
            "Delta_lambda(K): plug in the Kashiwara symmetric-crystal "
            "weight c_lambda(q) := s_lambda(1, q, ..., q^{n-1}) "
            "(Macdonald hook-content; equals the Demazure character "
            "D_{w_0}(lambda) at principal specialisation, verified by "
            "demazure-markov-trace.witness.json) as Delta_lambda. "
            "Independent of Occam single-partition heuristic in "
            "rho_k_h3a_refinement.py; deuteron-only proof of concept. "
            "Reports residual honestly (no scaling)."
        ),
        "engine": (
            f"mpmath numeric Hoefsmit at q_0 (50 dps), "
            f"multiprocessing.Pool({args.workers}); Macdonald "
            f"hook-content for c_lambda; crystal_basis.crystal_B "
            f"BFS for self-test"
            if not args.symbolic
            else "sympy symbolic-q + mpmath evaluation (50 dps), "
                 "single-threaded; Macdonald hook-content for c_lambda"
        ),
        "scriptFile": "rho_k_h3a_crystal.py",
        "scriptHash": script_hash,
        "parameters": {
            "q_0_50dps": mp.nstr(Q_MP, 50),
            "atom": "deuteron",
            "Z": 1, "N": 1, "A": 2, "n_strands": 6,
            "braid_word_source": "mass_at_3A_proper.atom_braid_word_3A(1, 1)",
            "braid_word_str": (
                "beta_p . I . beta_n  (canonical: H_3 (x) H_3 c H_6 with "
                "interface I = sigma_3 - h/2 . 1 at gen_idx=2)"
            ),
            "crossings_typed": [[g, t] for (g, t) in crossings],
            "n_crossings": len(crossings),
            "n_partitions": len(parts),
            "compute_status": "deuteron",
            "M_codata_MeV": str(M_D_MEV),
            "m_e_MeV": str(M_E_MEV),
            "m_p_MeV": str(M_P_MEV),
            "m_n_MeV": str(M_N_MEV),
        },
        "data": {
            "abs_tr_M_at_q0_50dps": str(abs_tr_M),
            "rho_K_LO": str(rho_K_LO),
            "rho_K_codata": str(rho_K_codata),
            "delta_rho_residual": str(delta_rho),
            "M_LO_pred_MeV": str(M_pred_LO),
            "M_LO_err_pct": str(err_pct_LO),
            "binding_gap_MeV": str(M_pred_LO - M_D_MEV),
            "target_sum_y_chi_Delta": str(target),
            "schur_weyl_check": {
                "sum_y_chi": str(sw_sum),
                "tr_M": str(tr_M),
                "abs_residual": str(sw_err),
                "match_at_1e_40": bool(sw_match),
            },
            "crystal_self_test": {
                "rows": selftest_rows,
                "all_match": bool(selftest_ok),
                "comment": (
                    "c_lambda(q=1) closed form vs |B(lambda, 6)| "
                    "BFS enumeration (Weyl dimension formula). "
                    "Validates the Macdonald hook-content c_lambda "
                    "implementation against the Kashiwara crystal "
                    "primitives in crystal_basis.py (PR #599)."
                ),
            },
            "per_lambda": per_lambda_full,
            "crystal_q0": {
                "sum_y_chi_c_lambda_at_q0": str(sum_q0),
                "residual_target_minus_sum": str(residual_q0),
                "alpha_E_diagnostic": (
                    str(alpha_E_q0) if mp.isfinite(alpha_E_q0) else "inf"
                ),
                "ratio_sum_over_target": str(relative_q0),
                "M_pred_MeV": str(M_pred_q0),
                "closure_err_MeV": str(err_q0_MeV),
                "closure_err_ppm": str(err_q0_ppm),
            },
            "crystal_at_one": {
                "sum_y_chi_c_lambda_at_one": str(sum_one),
                "residual_target_minus_sum": str(residual_one),
                "alpha_E_diagnostic": (
                    str(alpha_E_one) if mp.isfinite(alpha_E_one) else "inf"
                ),
                "ratio_sum_over_target": str(relative_one),
                "M_pred_MeV": str(M_pred_one),
                "closure_err_MeV": str(err_one_MeV),
                "closure_err_ppm": str(err_one_ppm),
            },
            "outcome": outcome,
            "comparison_to_occam": {
                "occam_picks_partition": (
                    occam_pick["partition"] if occam_pick else None
                ),
                "occam_Delta_lambda": (
                    occam_pick["Delta_lambda"] if occam_pick else None
                ),
                "occam_M_pred_MeV": (
                    occam_pick["M_pred_MeV"] if occam_pick else None
                ),
                "occam_closure_err_MeV": (
                    occam_pick["closure_err_MeV"] if occam_pick else None
                ),
                "balanced_321_Delta_lambda": (
                    occam_321["Delta_lambda"] if occam_321 else None
                ),
                "crystal_q0_M_pred_MeV": str(M_pred_q0),
                "crystal_q0_closure_err_MeV": str(err_q0_MeV),
                "crystal_q0_ratio_sum_over_target": str(relative_q0),
                "interpretation": (
                    "Occam reproduces M(D) exactly because it solves "
                    "1 equation in 1 unknown (free Delta_lambda for the "
                    "selected partition). Option E is over-determined: "
                    "Delta_lambda is FIXED by the crystal weight c_lambda, "
                    "leaving NO free parameter, so the mass equation has "
                    "a residual measuring the gap between the structural "
                    "prediction and the empirical binding. A residual of "
                    "0 ppm would be an exact match; the magnitude reported "
                    "is the falsification metric for this option."
                ),
            },
        },
        "audit_reference": "AUDIT-DEEP-2026-05.md sec.7 P3' (option E)",
        "pr_parent": "#600",
        "pr_prerequisite": "#599",
        "related_commits": {
            "type_b_fold_orbit_closure": ["4ca31f17", "657a4f82"],
            "crystal_bases_primitives": [
                "3d22baee", "1eca8880", "6b4a4e21",
            ],
        },
        "notes": (
            "Definition: c_lambda(q) := s_lambda(1, q, ..., q^{n_strands-1}) "
            "= principal q-specialisation of the Schur polynomial = "
            "Macdonald hook-content formula = Demazure character "
            "D_{w_0}(lambda) at x_i := q^{i-1} (verified by "
            "demazure-markov-trace witness). At q -> 1 this equals "
            "dim V_lambda for sl_n = |B(lambda, n)| from "
            "crystal_basis.crystal_B (Weyl dimension formula). "
            "We report BOTH the q-deformed (q_0) and the q -> 1 "
            "variants, since AGENTS.md sec.7b shortcut #3 leaves the "
            "choice open for the symmetric-crystal case (the Type-B "
            "fold-orbit closure work uses crystal *cardinality* at q=1, "
            "while the Demazure-fiber Markov-trace functional uses the "
            "q-deformed character)."
        ),
        "honest_reporting": (
            "Per protocol: c_lambda is NOT scaled to force the mass "
            "equation to close. The residual (target - sum) and the "
            "diagnostic scalar alpha_E (the would-close-it factor) are "
            "both reported. If alpha_E differs significantly from 1, the "
            "Kashiwara crystal weights are NOT the correct closed form "
            "for Delta_lambda; a flat-transport correction (q -> 0 -> q_0 "
            "connection curvature, per rem:ontological-agnosticism) "
            "would have to make up the difference, OR a different "
            "structural weight (Plancherel-truncated, jet-knot, ...) "
            "applies."
        ),
        "follow_up": (
            "If option E shows |alpha_E - 1| << 1 (close to closure), "
            "extend to (T, 3He) at n=9 and 4He at n=12. If alpha_E is "
            "far from 1, compare the residual to the four other options "
            "(A: crystal-truncated minimum-norm, B: Plancherel bound, "
            "C: jet-knot Hochschild, D: Type-B fold-orbit projection) "
            "in the parent PR #600 brief; the smallest residual wins."
        ),
    }

    out = HERE / "rho-k-h3a-crystal.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n  Wrote {out.name} ({out.stat().st_size} bytes).")
    print("=" * 96)
    return 0 if sw_match else 2


if __name__ == "__main__":
    sys.exit(main())
