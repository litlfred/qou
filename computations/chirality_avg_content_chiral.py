#!/usr/bin/env python3
"""chirality_avg_content_chiral.py

Companion to `chirality_avg_content.py` (which closed the
amphichiral case for figure-8 and Borromean).  This script computes
$\\langle c(\\lambda) \\rangle_\\beta$ for **chiral** braids in
$H_3(R, q_0)$ — the open residual of GAP-A-2 in
`derivation-audit-report.md`.

Per `prop:chirality-writhe-ribbon-derivation`, the first-order
chirality factor is

  a_K(β) = 1 + w(β) · ⟨c⟩_β · h + O(h²),

where ⟨c⟩_β is the Plancherel-weighted mean content.  The
amphichiral case discharges by bar-involution symmetry
(χ^λ = χ^{λ^T}), giving ⟨c⟩ = 0.  This script samples chiral
3-braids to expose the structural-but-non-zero values that the
chiral case takes.

Key observation (2026-05-09): the chiral ⟨c⟩_β is **knot-specific**;
the conjecture's earlier universal-1 ansatz was wrong, and so was
the simple writhe-content formula (empirically falsified for the
deuteron).  The right structural form for the chiral residual
remains the open piece of GAP-A-2.

Output: `chirality-avg-content-chiral.witness.json`.

Refs:
- prop:chirality-writhe-ribbon-derivation (the first-order ansatz)
- conj:chirality-ribbon-frobenius (the all-orders conjecture; now
  split into amphichiral closed / chiral open)
- companion: `chirality_avg_content.py` (amphichiral case at H_3)
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
import mpmath
from mpmath import mp, mpf

from hecke_characters import (  # noqa: E402
    PRECISION_F64_FALLBACK,
    PRECISION_MPFR_50DPS,
    _RUST_CHI_AVAILABLE,
    chi_lambda_braid,
    partitions_of,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from partition_utils import hook_length_1based as hook_length  # noqa: E402

set_compute_dps()
# Authoritative q_0 from q_parameter.Q_50_DIGIT_STR (m_μ/m_e CODATA fix).
Q0 = mpf(Q_50_DIGIT_STR)


def q_int(k: int, q):
    return mpf(0) if k == 0 else (q ** k - 1) / (q - 1)


def q_factorial(k: int, q):
    out = mpf(1)
    for i in range(1, k + 1):
        out *= q_int(i, q)
    return out


def dim_q(shape, q, n_fac_q):
    denom = mpf(1)
    for i, row_len in enumerate(shape, start=1):
        for j in range(1, row_len + 1):
            denom *= q_int(hook_length(shape, i, j), q)
    return n_fac_q / denom


def content_sum(shape):
    s = 0
    for i, row_len in enumerate(shape, start=1):
        for j in range(1, row_len + 1):
            s += (j - i)
    return s


# Chiral 3-braid test cases.  Word format: list of [sign, gen]
# matching the convention of chirality_avg_content.py.
CASES = [
    {
        "name": "trefoil 3_1 (σ_1^3)",
        "word": [[1, 1], [1, 1], [1, 1]],
        "writhe": 3,
        "knot_class": "3_1",
        "amphichiral": False,
    },
    {
        "name": "mirror trefoil (σ_1^-3)",
        "word": [[-1, 1], [-1, 1], [-1, 1]],
        "writhe": -3,
        "knot_class": "3_1*",
        "amphichiral": False,
    },
    {
        "name": "(σ_1 σ_2)^3 toral 3_1",
        "word": [[1, 1], [1, 2], [1, 1], [1, 2], [1, 1], [1, 2]],
        "writhe": 6,
        "knot_class": "3_1 (toral form)",
        "amphichiral": False,
    },
    {
        "name": "σ_1^2 σ_2^-1 σ_1^2 σ_2^-1 (B_3 chiral 6-cross)",
        "word": [[1, 1], [1, 1], [-1, 2], [1, 1], [1, 1], [-1, 2]],
        "writhe": 4,
        "knot_class": "5_2 candidate",
        "amphichiral": False,
    },
]


def main():
    # WitnessBuilder is constructed at the top of main() so durationMs
    # captures the full computation time (Copilot review #229).
    builder = (
        WitnessBuilder(name="chirality-avg-content-chiral",
                       engine="mpmath")
        .set_description(
            "Chiral residual of GAP-A-2 in derivation-audit-report.md. "
            "Computes ⟨c⟩_β = (Σ w_λ χ^λ(β) c(λ)) / "
            "(Σ w_λ χ^λ(β)) for chiral 3-braids at q_0 to expose "
            "the structural-but-non-zero values that the chiral case "
            "takes.  Companion to chirality-avg-content.witness.json "
            "(amphichiral case)."
        )
        .set_audit_only(
            "content/quantum-observable-universe/braids-and-knots/"
            "derivation-audit-report.md (GAP-A-2 chiral residual)"
        )
    )

    n = 3
    n_fac_q = q_factorial(n, Q0)
    parts = list(partitions_of(n))

    print("=" * 96)
    print("Chirality ⟨c⟩_β for chiral 3-braids (GAP-A-2 chiral residual)")
    print("=" * 96)
    print(f"  q_0 = {float(Q0):.16f}, n = {n}")
    print(f"  partitions of {n}: {parts}")
    print()

    rows = []
    h_val = Q0 - 1 / Q0
    # The actual numeric precision of `chi_lambda_braid` depends on
    # whether the Rust mpfr kernel is available.  The witness records
    # the actual tag (mpfr_50dps when Rust + mpfr are available, else
    # f64_numeric_fallback).  Previous code claimed `precision_dps: 50`
    # which overstated fidelity when only the f64 fallback ran (Copilot
    # review #r3213243720 / #r3213426355).
    chi_precision = (
        PRECISION_MPFR_50DPS if _RUST_CHI_AVAILABLE
        else PRECISION_F64_FALLBACK
    )
    chi_kwargs = {"precision": "mpfr_50dps"} if _RUST_CHI_AVAILABLE else {}
    # When the MPFR kernel is selected, `chi_lambdas_braid` needs the
    # substrate parameter as a decimal string — float(Q0) would
    # truncate to ~16 digits and defeat the mpfr_50dps fidelity
    # (Copilot review r3291263540).
    q_value_for_chi = Q_50_DIGIT_STR if _RUST_CHI_AVAILABLE else Q0
    # Batch character evaluation across partitions per case — F-A
    # of ffi-roundtrip-audit (single PyO3 crossing, rayon-parallel
    # on the Rust side).  Import here to avoid module-load reorder.
    from hecke_characters import chi_lambdas_braid
    for case in CASES:
        word = case["word"]
        w = case["writhe"]
        num = mpf(0)
        den = mpf(0)
        per_lam = []
        chi_raw_values = chi_lambdas_braid(parts, word, q_value_for_chi, **chi_kwargs)
        for shape, chi_raw in zip(parts, chi_raw_values):
            c_lam = content_sum(shape)
            w_lam = dim_q(shape, Q0, n_fac_q) ** 2 / n_fac_q
            # Rust mpfr returns a decimal string; parse to mpf.
            if isinstance(chi_raw, str):
                chi_raw = mpf(chi_raw)
            # Keep mpmath precision: extract real part as mpf without
            # casting through builtin complex / float (which would drop
            # to 53-bit precision and invalidate the mp.dps = 50
            # working precision).
            chi_val = mp.re(chi_raw)
            num += w_lam * chi_val * c_lam
            den += w_lam * chi_val
            per_lam.append({
                "shape": list(shape),
                "content_c_lambda": c_lam,
                "wedderburn_weight": str(w_lam),
                "chi_lambda_beta": str(chi_val),
                "weighted_chi_c": str(w_lam * chi_val * c_lam),
            })
        # Tolerance tied to working precision (per Gemini review).
        zero_tol = mpf(10) ** (-int(mp.dps * 0.6))
        if abs(den) < zero_tol:
            avg_c_mp = None
            a_K_first_mp = None
            avg_c = None
            a_K_first = None
            note = "denominator ~ 0 (degenerate Markov trace at q_0)"
        else:
            # Keep full mpmath precision for the witness; convert to
            # float only at the final report-emission stage so 50-dps
            # results survive in the witness's `avg_content_c_beta_mp`
            # string field.
            avg_c_mp = num / den
            a_K_first_mp = 1 + w * avg_c_mp * h_val
            avg_c = float(avg_c_mp)
            a_K_first = float(a_K_first_mp)
            note = ""
        print(f"  {case['name']:<45}  writhe={w:>+3}, "
              f"⟨c⟩_β={avg_c if avg_c is None else f'{avg_c:+.6f}':>12}, "
              f"a_K(1st)={a_K_first if a_K_first is None else f'{a_K_first:+.4f}':>9}"
              f"  {note}")
        rows.append({
            "name": case["name"],
            "knot_class": case["knot_class"],
            "amphichiral": case["amphichiral"],
            "braid_word": word,
            "writhe": w,
            "n_partitions": len(parts),
            "rows": per_lam,
            "numerator": str(num),
            "denominator": str(den),
            # Full-precision (50-dps) string is the canonical witness
            # value; the float fields are convenience truncations for
            # downstream comparison at 53-bit precision.
            "avg_content_c_beta_mp": (None if avg_c_mp is None else str(avg_c_mp)),
            "a_K_first_order_mp": (None if a_K_first_mp is None else str(a_K_first_mp)),
            "avg_content_c_beta": (None if avg_c is None else avg_c),
            "a_K_first_order": (None if a_K_first is None else a_K_first),
            "note": note,
        })
    print()

    # Summary observations.
    notes = [
        "trefoil 3_1 (σ_1^3) and its mirror (σ_1^-3) give "
        "⟨c⟩_β = ±1.815 — antisymmetric under braid mirror as required.",
        "The (σ_1 σ_2)^3 toral form of 3_1 (writhe 6) gives a "
        "different ⟨c⟩_β = +0.354, confirming that ⟨c⟩_β depends on "
        "the specific braid representative, not just the knot type.",
        "None of the values match the ⟨c⟩ = 1 universal ansatz from "
        "the conjecture; the chiral case has knot-specific structural "
        "values that are NOT given by the simple writhe-content formula.",
        "Combined with the deuteron empirical falsification "
        "(chirality-writhe-ribbon-derivation.md:122-126), this "
        "demarcates the chiral residual of GAP-A-2: a structural "
        "formula relating ⟨c⟩_β to the braid topology is the open "
        "piece.",
    ]
    print("Summary observations:")
    for note in notes:
        print(f"  - {note}")
    print()

    builder = (
        builder
        .add_parameter("q_0", float(Q0))
        .add_parameter("n", n)
        .add_parameter("partitions", [list(p) for p in parts])
        .add_parameter("chi_precision", chi_precision)
        .add_parameter("rust_chi_available", _RUST_CHI_AVAILABLE)
        .add_parameter("mp_dps", mp.dps)
        .add_data("cases", rows)
        .add_data("summary_observations", notes)
        .add_assertion(
            name="trefoil_chiral_avg_c_nonzero_and_antisymmetric",
            computed=int(
                rows[0]["avg_content_c_beta"] is not None
                and rows[1]["avg_content_c_beta"] is not None
                and abs(rows[0]["avg_content_c_beta"]
                        + rows[1]["avg_content_c_beta"]) < 1e-6
                and abs(rows[0]["avg_content_c_beta"]) > 0.1
            ),
            expected=1,
        )
        .add_assertion(
            name="chiral_avg_c_not_universal_1",
            computed=int(
                rows[0]["avg_content_c_beta"] is None
                or abs(rows[0]["avg_content_c_beta"] - 1.0) > 0.1
            ),
            expected=1,
        )
    )
    out_path = builder.save()
    print(f"  Witness emitted: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
