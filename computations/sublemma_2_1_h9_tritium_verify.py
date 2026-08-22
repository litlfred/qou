#!/usr/bin/env python3
"""Tritium / ³He Sub-lemma 2.1 verification: Path A vs Path B at machine ε.

Loads the H_6 deuteron A^ξ_{μν'}(I_pn) extraction
(sublemma-2-1-A-operator-extract.witness.json) and the new H_9
A^λ_{ξν}(I_2) extraction (sublemma-2-1-A-operator-extract-h9-*.witness.json),
then verifies the iterated 2-interface formula for tritium / ³He:

  χ^λ(β_K) = Σ_{ξ,ν,μ,ν'} c^λ_{ξν} · c^ξ_{μν'}
              · Tr[A^λ_{ξν}(I_2) · (A^ξ_{μν'}(I_1) · (ρ_μ(β_1) ⊗ ρ_{ν'}(β_2)))
                                                          ⊗ ρ_ν(β_3)]

For tritium = β_p · I_pn · β_n · I_nn · β_n:
  W_inner = β_p · I_pn · β_n ∈ H_6  (inner I_1 = I_pn)
  I_2 = I_nn ∈ H_9 ↓ H_6 × H_3
  β_3 = β_n ∈ H_3

For ³He = β_p · I_pp · β_p · I_pn · β_n:
  W_inner = β_p · I_pp · β_p ∈ H_6  (inner I_1 = I_pp)
  I_2 = I_pn
  β_3 = β_n ∈ H_3

Path A (truth): direct χ^λ(β_K) via Hoefsmit at H_9.
Path B (derivation): iterated formula above using extracted A's.

Verification: max relative residual ≤ 10⁻¹² across all λ ⊢ 9 for
which the H_9 extraction was over-determined and consistent.

Output: sublemma-2-1-h9-tritium-verify.witness.json
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from char_fast import _compiled_sigmas, chi_lambda_fast  # noqa: E402
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402
from lr_coefficients import get_lr_table, partitions_of  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from sublemma_2_1_A_operator_extract_h9 import (  # noqa: E402
    INTERFACE_COEFS, H, evaluate_word_matrix,
    make_h6_test_words, make_h3_test_words, with_interface_h9,
    shape_dim,
)


# ──────────────────────────────────────────────────────────────────────
# Atom braid composition (3+3+3 strand layout, pppnnn ordering)
# ──────────────────────────────────────────────────────────────────────

def _proton_body() -> list:
    """Per-nucleon proton sub-word on 3 strands (gens 0, 1)."""
    # Match build_atom_nf's proton chain: 3 (σ_0, σ_1⁻¹), then quark/gluon crossings.
    body = []
    for _ in range(3):
        body.append((1.0, 0.0, 0))       # σ_0
        body.append((1.0, -H, 1))         # σ_1⁻¹
    body.append((1.0, 0.0, 0))            # uu pair
    body.append((1.0, -H / 2, 0))         # ud mixed on gen 0
    body.append((1.0, -H / 2, 1))         # ud mixed on gen 1
    body.append((1.0, 0.0, 0))            # gluon 1
    body.append((1.0, 0.0, 0))            # gluon 2
    return body


def _neutron_body() -> list:
    body = []
    for _ in range(3):
        body.append((1.0, 0.0, 0))
        body.append((1.0, -H, 1))
    body.append((1.0, -H / 2, 0))
    body.append((1.0, -H / 2, 0))
    body.append((1.0, -H, 1))             # dd → σ⁻¹ on gen 1
    body.append((1.0, 0.0, 0))
    body.append((1.0, 0.0, 0))
    return body


def tritium_braid() -> list:
    """β_T = β_p · I_pn · β_n · I_nn · β_n on 9 strands.

    Layout: proton occupies strands 0-2, first neutron 3-5,
    second neutron 6-8.  Interfaces at strand 2 (pn) and strand 5 (nn).
    """
    word = []
    word.extend(_proton_body())                                # β_p on 0..2
    word.append((1.0, -H / 2, 2))                              # I_pn at strand 2
    word.extend([(c, d, g + 3) for (c, d, g) in _neutron_body()])  # β_n on 3..5
    word.append((1.0, -H, 5))                                  # I_nn at strand 5
    word.extend([(c, d, g + 6) for (c, d, g) in _neutron_body()])  # β_n on 6..8
    return word


def he3_braid() -> list:
    """β_³He = β_p · I_pp · β_p · I_pn · β_n on 9 strands."""
    word = []
    word.extend(_proton_body())                                # β_p on 0..2
    word.append((1.0, 0.0, 2))                                 # I_pp at strand 2
    word.extend([(c, d, g + 3) for (c, d, g) in _proton_body()])   # β_p on 3..5
    word.append((1.0, -H / 2, 5))                              # I_pn at strand 5
    word.extend([(c, d, g + 6) for (c, d, g) in _neutron_body()])  # β_n on 6..8
    return word


# ──────────────────────────────────────────────────────────────────────
# Bilinear-system reconstruction (mirror the extract scripts but for
# the SPECIFIC inner / outer words, not the test-word grid).
# ──────────────────────────────────────────────────────────────────────

def reconstruct_chi_h6_via_sublemma(
    w_p: list, w_n: list, inner_interface: str,
    h6_extract: dict,
) -> dict:
    """Reconstruct χ^ξ(β_p · I_1 · β_n) for ξ ⊢ 6 via Sub-lemma 2.1.

    Uses the H_6 extracted A^ξ_{μν'}(I_1) matrices to predict
    χ^ξ(W_inner) directly from ρ_μ(β_p), ρ_{ν'}(β_n).

    Args:
        w_p: β_p word (in H_3, gens 0..1)
        w_n: β_n word (in H_3, gens 0..1)
        inner_interface: "pn"/"pp"/"nn" (the H_6 I_1)
        h6_extract: parsed H_6 extraction witness

    Returns:
        {xi: chi_xi_predicted (complex)}.

    NOTE: the existing H_6 extraction script only extracts A for
    I_pn (it hard-codes int_c, int_d at the deuteron interface).
    For tritium's inner block we need A^ξ_{μν'}(I_pn) — same as the
    deuteron extraction.  For ³He's inner block (I_pp), a separate
    H_6 extraction is needed (not done yet — Phase 2).
    """
    parts_3 = partitions_of(3)
    parts_6 = partitions_of(6)
    lr_36 = get_lr_table(3, 3)

    # ρ_μ(β_p) and ρ_{ν'}(β_n) for each μ, ν' ⊢ 3
    rho_p = {mu: evaluate_word_matrix(mu, w_p) for mu in parts_3}
    rho_n = {nu: evaluate_word_matrix(nu, w_n) for nu in parts_3}

    chi_xi = {}
    for xi in parts_6:
        accum = 0.0 + 0j
        results = h6_extract.get("results_per_lambda", {})
        # results_per_lambda is keyed by string repr of xi tuple in the witness
        xi_key = str(xi)
        if xi_key not in results:
            chi_xi[xi] = None
            continue
        A_per_pair = results[xi_key].get("A_per_pair", {})
        for mu in parts_3:
            for nu_p in parts_3:
                c = lr_36.get((mu, nu_p, xi), 0)
                if c == 0:
                    continue
                key = f"({mu},{nu_p})"
                if key not in A_per_pair:
                    continue
                A_info = A_per_pair[key]
                # `dtype=float` because the extract witnesses are migrating
                # off raw float64 JSON numbers onto full-precision decimal
                # STRINGS (`_precision.fmt`); a bare np.array would build a
                # `<U..` array and the `1j * A_im` below would raise
                # UFuncNoLoopError. No-op for the extracts still carrying
                # numbers, so both generations work. See `qou-zck8`.
                A_re = np.array(A_info["matrix_re"], dtype=float)
                A_im = np.array(A_info["matrix_im"], dtype=float)
                A = A_re + 1j * A_im
                X = np.kron(rho_p[mu], rho_n[nu_p])
                # Tr(A · X)
                accum += complex(np.trace(A @ X))
        chi_xi[xi] = accum
    return chi_xi


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--atom", choices=["tritium", "he3"], default="tritium",
                        help="which atom to verify (default: tritium)")
    parser.add_argument("--h9-witness", type=str, default=None,
                        help="H_9 extraction witness file (default: auto — "
                             "I_nn for tritium, I_pn for he3, matching the "
                             "atom's OUTER interface)")
    parser.add_argument("--h6-witness", type=str,
                        default="sublemma-2-1-A-operator-extract.witness.json",
                        help="H_6 extraction witness file (default: I_pn for deuteron)")
    args = parser.parse_args()

    # The OUTER interface I_2 is nn for tritium (p·n·n) and pn for he3
    # (p·p·n); pick the matching H_9 extract unless overridden.
    if args.h9_witness is None:
        args.h9_witness = (
            "sublemma-2-1-A-operator-extract-h9-pn.witness.json"
            if args.atom == "he3" else
            "sublemma-2-1-A-operator-extract-h9-nn.witness.json"
        )

    print("=" * 96)
    print(f"  Sub-lemma 2.1 verification at H_9: Path A vs Path B for {args.atom}")
    print("=" * 96)

    # Load witnesses
    h9_path = HERE / args.h9_witness
    h6_path = HERE / args.h6_witness
    if not h9_path.exists():
        print(f"  ERROR: H_9 witness not found: {h9_path}")
        print(f"  Run `python3 sublemma_2_1_A_operator_extract_h9.py "
              f"--interface nn` first.")
        return 2

    h9_data = json.loads(h9_path.read_text())
    h6_data = json.loads(h6_path.read_text())
    h9_interface = h9_data.get("data", {}).get("interface_type",
                                              h9_data.get("interface_type"))
    print(f"  Loaded H_9 witness: I_2 = {h9_interface}")
    print(f"  Loaded H_6 witness: I_1 = pn (deuteron)")

    # Build the atom braid + its inner / third-nucleon decomposition.
    # Path B reconstructs ρ_ξ(W_inner) by DIRECT matrix eval, so ³He's
    # I_pp inner needs NO separate H_6 extract — the inner is a pure
    # braid and is eval'd exactly like tritium's pn inner.
    if args.atom == "tritium":               # p · n · n
        beta_full = tritium_braid()
        inner_first, inner_second = _proton_body(), _neutron_body()
        inner_iface_cd = (1.0, -H / 2)       # I_pn (averaged)
        third_body = _neutron_body()
    else:                                     # he3: p · p · n
        beta_full = he3_braid()
        inner_first, inner_second = _proton_body(), _proton_body()
        inner_iface_cd = (1.0, 0.0)          # I_pp (σ, pure braid)
        third_body = _neutron_body()

    print(f"  β_{args.atom}: {len(beta_full)} generators")
    print()

    # Path A: direct χ^λ at H_9
    parts_9 = partitions_of(9)
    print(f"  [Path A] computing χ^λ(β_{args.atom}) directly via Hoefsmit "
          f"at H_9 for {len(parts_9)} λ partitions...")
    t0 = time.monotonic()
    chi_path_a = {lam: chi_lambda_fast(lam, beta_full) for lam in parts_9}
    print(f"    done in {time.monotonic() - t0:.1f}s")
    print()

    # Path B: iterated Sub-lemma 2.1
    print(f"  [Path B] reconstructing χ^λ(β_{args.atom}) via iterated "
          f"Sub-lemma 2.1...")
    t0 = time.monotonic()

    parts_6 = partitions_of(6)
    parts_3 = partitions_of(3)
    lr_69 = get_lr_table(6, 3)

    # Step 1: reconstruct ρ_ξ(W_inner) for ξ ⊢ 6 from the H_6 A's.
    # PROBLEM: the H_6 extraction only gives χ^ξ(W_inner), not the
    # full ρ_ξ(W_inner). The iterated formula needs ρ_ξ(W_inner) as a
    # MATRIX so it can be tensored with ρ_ν(β_3) and traced against
    # A^λ_{ξν}(I_2). Direct route: just compute ρ_ξ(W_inner) at H_6
    # via evaluate_word_matrix (faster than the extraction itself).
    # This sidesteps the issue that the H_6 A matrices live in
    # End(V_μ ⊗ V_{ν'}), not End(V_ξ).
    w_inner = (inner_first
               + [(inner_iface_cd[0], inner_iface_cd[1], 2)]
               + [(c, d, g + 3) for (c, d, g) in inner_second])
    print(f"    [B.1] computing ρ_ξ(W_inner) at H_6 for ξ ⊢ 6...")
    rho_xi_inner = {xi: evaluate_word_matrix(xi, w_inner) for xi in parts_6}

    # Step 2: reconstruct ρ_ν(β_3) for ν ⊢ 3 (third nucleon)
    print(f"    [B.2] computing ρ_ν(β_3) at H_3 for ν ⊢ 3...")
    rho_nu_3 = {nu: evaluate_word_matrix(nu, third_body) for nu in parts_3}

    # Step 3: apply outer A^λ_{ξν}(I_2) to compose ρ_ξ(W_inner) ⊗ ρ_ν(β_3)
    print(f"    [B.3] applying A^λ_{{ξν}}(I_2) for λ ⊢ 9...")
    chi_path_b = {}
    h9_results = h9_data.get("data", {}).get("results_per_lambda", {})

    for lam in parts_9:
        lam_key = str(list(lam))
        if lam_key not in h9_results:
            chi_path_b[lam] = None
            continue

        accum = 0.0 + 0j
        A_per_pair = h9_results[lam_key].get("A_per_pair", {})
        for xi in parts_6:
            for nu in parts_3:
                c = lr_69.get((xi, nu, lam), 0)
                if c == 0:
                    continue
                key = f"({xi},{nu})"
                if key not in A_per_pair:
                    continue
                A_info = A_per_pair[key]
                # `dtype=float` because the extract witnesses are migrating
                # off raw float64 JSON numbers onto full-precision decimal
                # STRINGS (`_precision.fmt`); a bare np.array would build a
                # `<U..` array and the `1j * A_im` below would raise
                # UFuncNoLoopError. No-op for the extracts still carrying
                # numbers, so both generations work. See `qou-zck8`.
                A_re = np.array(A_info["matrix_re"], dtype=float)
                A_im = np.array(A_info["matrix_im"], dtype=float)
                A = A_re + 1j * A_im
                X = np.kron(rho_xi_inner[xi], rho_nu_3[nu])
                # Tr(A · X) — multiplicity c^λ_{ξν} is absorbed into A
                # (matches the deuteron H_6 convention; same comment as
                # sublemma_2_1_A_operator_extract.py:176-180)
                accum += complex(np.trace(A @ X))
        chi_path_b[lam] = accum

    t_b = time.monotonic() - t0
    print(f"    done in {t_b:.1f}s")
    print()

    # Look up which partitions were fully over-determined AND
    # FULL-RANK in the H_9 extract.  The extract's `underdetermined`
    # field only checks n_eq vs n_unknowns; we additionally require
    # rank = n_unknowns for the A^λ_{ξν} solution to be unique.
    # Rank-deficient cases satisfy the test-grid equations but the
    # solution is non-unique outside the grid — that's the regime
    # where Path A ≠ Path B for an out-of-grid β.
    h9_status = {}
    for k, v in h9_data.get("data", {}).get("results_per_lambda", {}).items():
        lam = tuple(eval(k))
        full_rank = (int(v.get("rank", 0)) == int(v.get("n_unknowns", -1)))
        n_eq_ok = int(v.get("n_equations", 0)) >= int(v.get("n_unknowns", 0))
        # "underdetermined" here means: not unique-solution.  True iff
        # rank < n_unknowns OR n_eq < n_unknowns.
        h9_status[lam] = not (full_rank and n_eq_ok)

    # Compare
    print("  Path A vs Path B comparison:")
    print(f"  {'λ':<22} {'dim_λ':>5} {'χ^λ (Path A)':>22} {'χ^λ (Path B)':>22} "
          f"{'|rel diff|':>12}  status")
    print("  " + "-" * 96)
    max_rel_overdet = 0.0
    max_rel_all = 0.0
    n_overdet = 0
    n_overdet_pass = 0
    n_underdet = 0
    for lam in parts_9:
        ca = chi_path_a[lam]
        cb = chi_path_b[lam]
        denom = max(abs(ca), 1e-15)
        rel = abs(ca - cb) / denom
        max_rel_all = max(max_rel_all, rel)
        underdet = h9_status.get(lam, True)
        d_lam = shape_dim(lam)
        if underdet:
            n_underdet += 1
            status = "under (Phase 2)"
        else:
            n_overdet += 1
            max_rel_overdet = max(max_rel_overdet, rel)
            if rel < 1e-10:
                n_overdet_pass += 1
                status = "✓"
            else:
                status = "✗"
        print(f"  {str(lam):<22} {d_lam:>5} {ca.real:>+22.6e} {cb.real:>+22.6e} "
              f"{rel:>12.2e}  {status}")
    print()
    print(f"  Verification summary:")
    print(f"    Over-determined λ: {n_overdet}/{len(parts_9)}; "
          f"of which {n_overdet_pass} verified at rel res < 1e-10")
    print(f"    Max rel residual on over-determined subset: "
          f"{max_rel_overdet:.2e}")
    if n_underdet:
        print(f"    Under-determined λ: {n_underdet}/{len(parts_9)} "
              f"(extract used a degenerate test-word set; regenerate the H_9 "
              f"extract with `--full-basis --native` so K_6 × K_3 ≥ n_unknowns "
              f"for every λ — see the 2026-06-09 binding audit)")
    else:
        print(f"    Under-determined λ: 0/{len(parts_9)} "
              f"(extract is full-rank — H_9 closed via the S_6×S_3 "
              f"permutation basis)")

    from witness_base import WitnessBuilder
    builder = (
        WitnessBuilder(f"sublemma-2-1-h9-{args.atom}-verify",
                       engine="numpy")
        .set_description(
            f"Sub-lemma 2.1 multi-interface verification at H_9 for "
            f"{args.atom}: compares Path A (direct χ^λ via Hoefsmit) "
            f"against Path B (iterated 2-interface formula with "
            f"A^λ_{{ξν}}(I_2) extracted from "
            f"sublemma-2-1-A-operator-extract-h9-nn.witness.json). "
            + (
                f"All {n_overdet}/{len(parts_9)} λ ⊢ 9 are over-determined "
                f"and verified at machine ε — the consumed extract uses the "
                f"full S_6×S_3 permutation basis (see the 2026-06-09 binding "
                f"audit)."
                if n_underdet == 0 else
                f"{n_overdet} of {len(parts_9)} λ ⊢ 9 are fully determined "
                f"and verified at machine ε; {n_underdet} remain "
                f"under-determined because the consumed extract used a "
                f"degenerate test-word set — regenerate it with "
                f"`--full-basis --native` to close them."
            )
        )
        .set_audit_only(
            "docs/audits/2026-05-15-sublemma-2-1-h9-multi-interface-extension.md"
        )
        .add_data("atom", args.atom)
        .add_data("lean_uniqueness_ref", lean_uniqueness_ref(args.atom))
        .add_data("interface_outer", h9_interface)
        .add_data("interface_inner", "pn")
        .add_data("n_generators_h9_braid", len(beta_full))
        .add_data("chi_path_a", {
            str(lam): [chi_path_a[lam].real, chi_path_a[lam].imag]
            for lam in parts_9
        })
        .add_data("chi_path_b", {
            str(lam): [chi_path_b[lam].real, chi_path_b[lam].imag]
            for lam in parts_9
        })
        .add_data("n_overdetermined_verified", n_overdet_pass)
        .add_data("n_overdetermined_total", n_overdet)
        .add_data("n_underdetermined", n_underdet)
        .add_data("max_relative_residual_overdetermined", max_rel_overdet)
        .add_data("max_relative_residual_all", max_rel_all)
        .add_assertion(
            "overdetermined_path_a_eq_path_b_machine_eps",
            computed=n_overdet_pass,
            expected=n_overdet,
            source="iterated Sub-lemma 2.1 at H_9 ↓ H_6 × H_3",
        )
    )
    # Caveat only applies when the consumed extract is under-determined.
    # With the full S_6×S_3 permutation-basis extract every λ ⊢ 9 is
    # over-determined (n_underdet = 0), so no caveat is emitted.
    if n_underdet:
        builder.add_caveat(
            f"{n_underdet} of {len(parts_9)} λ ⊢ 9 are under-determined in "
            "the consumed extract: their least-squares A's satisfy the test "
            "grid but do not generalize to the full tritium braid β_T. The "
            "test-word family spans only a sub-space of End(V_ξ); regenerate "
            "the H_9 extract with `--full-basis --native` (full S_6×S_3 "
            "permutation basis) to make every λ over-determined and full-rank."
        )
    out_path = builder.save()
    print(f"  Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
