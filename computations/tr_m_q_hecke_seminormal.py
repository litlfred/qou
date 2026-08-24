#!/usr/bin/env python3
"""
tr_m_q_hecke_seminormal.py — close the character gap completely.

Per docs/audits/2026-05-08-p3-h-3a-divergence.md (cross-check finding),
the partition-sum path

    tr_M(β) = Σ_λ y_λ(q) · χ^λ_q(β)

correctly computes tr_M IFF both (a) y_λ is the canonical Jones-Markov
weight (Wenzl Schur principal specialization — fixed in PR #572 commit
ac7880c5) AND (b) χ^λ_q is the q-deformed Hecke character at q_0
(NOT the q=1 classical Murnaghan–Nakayama character that
`schur_weyl_symbolic.specht_character_atomic` returns).

This script closes (b) by composing two existing modules:

  1. `wedderburn_jones_markov.y_lambda_at(n, q_val=q_0)` — Wenzl y_λ at q_0
  2. `hecke_characters.build_seminormal_matrices(shape, q=q_0)` — Hoefsmit
     seminormal matrices σ_1, …, σ_{n−1} at q_0
  3. `mass_at_3A_proper.chi_lambda_of_word(sigmas, dim, word, ...)` —
     trace of the matrix product over the atomic-braid word

The seminormal-trace χ^λ_q is the **canonical Hecke character**
(Hoefsmit 1974, Mathas 1999 §3.4); χ^λ_q(σ_i) on a SYT pair (T, T')
is the (T, T') matrix entry of σ_i in the seminormal basis, summed
over the diagonal.  At q = 1 it reduces to the classical Murnaghan–
Nakayama character; at q = q_0 it is the q-deformed Hecke character.

The integrated cross-check:

    tr_M_pred(β_atomic(Z, N))
        = Σ_{λ ⊢ 3A} y_λ(q_0) · tr(ρ_λ_q0(β_atomic(Z, N)))

should agree with `markov_trace_recursive` (canonical Markov-axiom
reducer; reference at `atomic-tr-m-mpfr-50dps.witness.json`) to
1e-6 relative or better.  If yes: the character gap is **closed**.

Witness: tr-m-q-hecke-seminormal.witness.json
Audit-only: docs/audits/2026-05-08-q-hecke-character-gap-closure.md

@module computations/tr_m_q_hecke_seminormal
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import os
import sys
import time
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

from hecke_characters import partitions_of  # noqa: E402
from hoefsmit_mpmath import (BlockCacheMP,  # noqa: E402
                             chi_lambda_of_word_sparse_mp,
                             seminormal_matrices_mp)
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from q_parameter import Q_MP  # noqa: E402  — single source of truth (mpf)
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Was `sp.Float(Q_0_FLOAT, 30)`, i.e. THIRTY DIGITS OF A SEVENTEEN-DIGIT VALUE:
# `q_parameter.Q` is the float64 q₀, so asking sympy for 30 dps could not
# recover precision that was already gone. It read as a high-precision call and
# was not one. `Q_MP` is the mpf q₀ and carries the digits for real.
Q_0_HIGH = Q_MP
# ANCHOR-MATCHED REFERENCE. This producer computes at Q_MP, the PROTON pin, and
# the base-name reference `atomic-tr-m-mpfr-50dps.witness.json` is the MUON one
# (`atomic_tr_m_mpfr_50dps` is tagged `ideal_muon`). Comparing across that
# boundary is the straddle AGENTS.md forbids regardless of size -- and here it
# was the WHOLE measured disagreement:
#
#     atom       vs MUON ref     vs PROTON ref
#     proton      7.8403e-8       4.67e-51
#     deuteron    1.5143e-7       1.86e-50
#     helium-3    2.5171e-7       3.31e-51
#
# The two routes agree EXACTLY, to the serialization limit. The ~1e-7 was never
# a methodological difference between the q-Hecke partition sum and the
# canonical route; it was a proton computation measured against a muon
# reference, and it scaled linearly with strand count because tr_M is a product
# over ~n crossings and so inherits ~n x the 11.5 ppb mu-p q0 gap.
#
# The straddle PREDATES the exact-arithmetic migration: the producer previously
# read `Q_0_FLOAT = q_parameter.Q`, which is the proton float64. Removing the
# float64 noise did not create the discrepancy, it made it legible -- the noise
# had been the same order as the straddle.
_REF_NAME = ("atomic-tr-m-mpfr-50dps-proton.witness.json"
             if str(Q_MP).startswith("1.10997858")
             else "atomic-tr-m-mpfr-50dps.witness.json")
REF_WITNESS = _pb.witness_path(_REF_NAME, HERE)


_Y_LAMBDA_CACHE: dict[int, dict] = {}


def _y_lambda_cached(n: int):
    """Cache y_λ across atoms with the same n (T + ³He both share n=9)."""
    if n not in _Y_LAMBDA_CACHE:
        _Y_LAMBDA_CACHE[n] = y_lambda_at(n, q_val=Q_0_HIGH)
    return _Y_LAMBDA_CACHE[n]


def _load_canonical_tr_m() -> dict:
    """Canonical tr_M reference, kept as mpf.

    The field is named `tr_M_at_q0_50dps` and `float()` threw 33 of those
    digits away on the way in -- while this producer's whole purpose is to
    measure agreement AGAINST that reference to 1e-6.
    """
    if not REF_WITNESS.exists():
        return {}
    data = json.loads(REF_WITNESS.read_text())
    out: dict = {}
    for row in data.get("results", []):
        name = row.get("atom")
        val = row.get("tr_M_at_q0_50dps")
        if name and val is not None:
            out[name] = mp.mpf(str(val))
    return out


def _chi_contribution_worker(args):
    """Top-level worker for multiprocessing.Pool over partitions.

    Computes the per-partition contribution
    `y_λ · χ^λ_q(β_atomic)` for one shape.  Returns the row dict (or
    None if the partition cannot support the generator count, e.g. a
    column partition (1^k) at H_n with k < n_gens_required + 1).
    """
    shape, y_val, q_val, word, n_gens_required = args
    sigmas, dim, _syts = seminormal_matrices_mp(
        tuple(shape), cache=BlockCacheMP(mp.mpf(str(q_val))))
    if dim == 0:
        return None
    try:
        chi = chi_lambda_of_word_sparse_mp(sigmas, dim, word, n_gens_required)
    except IndexError:
        return None
    y_mp = mp.mpf(str(y_val))
    contrib = y_mp * chi
    return {
        "partition": list(shape),
        "dim": int(dim),
        "y_at_q0": fmt(y_mp),
        "chi_q_at_q0": fmt(chi),
        "contribution": fmt(contrib),
        "_contribution_mp": contrib,
    }


def tr_m_via_partition_sum_q_hecke(
    Z: int, N: int, q_val=Q_MP,
    *, include_inter: bool = True, workers: int | None = None,
) -> tuple[float, list[dict]]:
    """tr_M(β_atomic(Z, N)) = Σ_{λ ⊢ 3A} y_λ(q) · χ^λ_q(β_atomic).

    Composes:
      - y_λ via Wenzl (numerical-q-from-start for n ≥ 6)
      - χ^λ_q via Hoefsmit seminormal matrices at q_val (numerical)

    `workers` (default None = sequential) enables `multiprocessing.Pool`
    over the per-partition χ^λ_q loop.  Recommended for n ≥ 9 where
    partition count is large (n=9: 30 partitions; n=12: 77).

    Returns (tr_M_value, per_partition_breakdown).
    """
    A = Z + N
    n = 3 * A

    # Build the atomic braid word once.
    word = atom_braid_word_3A(Z, N, include_inter=include_inter)

    # y_λ at q_0 for all λ ⊢ n.
    # Hybrid precision: 30-dps sympy Float for y_λ (preserves
    # accuracy on q^large_exponent Wenzl-Schur terms) + float64 for
    # the seminormal χ^λ_q below.  This combination closes T (n=9)
    # at machine ε in ~2s vs 1.6e-5 for pure float64 or 240+s
    # timeouts for full symbolic.
    y_vals = _y_lambda_cached(n)

    n_gens_required = n - 1
    work = [(shape, y, q_val, word, n_gens_required)
            for shape, y in y_vals.items()]

    rows = []
    if workers and workers > 1 and len(work) > 1:
        with Pool(processes=workers) as pool:
            for row in pool.imap_unordered(_chi_contribution_worker, work):
                if row is not None:
                    rows.append(row)
    else:
        for w in work:
            row = _chi_contribution_worker(w)
            if row is not None:
                rows.append(row)

    total = mp.fsum(r.pop("_contribution_mp") for r in rows)
    return total, rows


# Test bench scoped to A ≤ 2 to keep session-time tractable
# (n=3: ~0.2s for y_λ + small seminormals; n=6: ~3.8s for y_λ +
# 11 seminormal builds).  A = 3 (n = 9) takes ~63s for y_λ + 30
# seminormal builds — feasible but extends the witness substantially.
ATOMIC_TEST_BENCH = [
    (1, 1, 0, "proton"),
    (1, 0, 1, "neutron"),
    (2, 1, 1, "deuteron"),
    (3, 1, 2, "tritium"),
    (3, 2, 1, "helium-3"),
    # ⁴He (4, 2, 2): timed out at 600s — y_λ at n=12 with 30-dps
    # sympy Float requires ~6-13 minutes for the Wenzl-Schur sum
    # over p(12)=77 partitions.  The hybrid 30-dps path is feasible
    # for n ≤ 9; A=4 (n=12) needs either parallelisation
    # (multiprocessing on the 77 partitions) or full 50-dps mpmath
    # (#564's rho_k_h3a_refinement.py path).  Deferred to a
    # follow-up that adds the parallel option.
]


def main() -> int:
    canonical = _load_canonical_tr_m()
    if not canonical:
        print("ERROR: canonical reference witness not loadable", file=sys.stderr)
        return 1

    builder = (
        WitnessBuilder(
            name="tr-m-q-hecke-seminormal",
            engine="numpy",
        )
        .set_description(
            "Closes the character gap in the partition-sum tr_M path: "
            "tr_M(β) = Σ_λ y_λ(q) · χ^λ_q(β) via canonical Wenzl y_λ "
            "(numerical-q-from-start) + Hoefsmit seminormal χ^λ_q at q_0. "
            "Cross-checks against `markov_trace_recursive` reference "
            "(atomic-tr-m-mpfr-50dps.witness.json). Closes the residual "
            "gap identified in tr-m-jones-markov-cross-check.witness.json "
            "(rel err ~55-80% with q=1 MN character → expected ~1e-6 "
            "with q-Hecke seminormal character)."
        )
    )

    rows = []
    all_passed = True
    for A_param, Z, N, name in ATOMIC_TEST_BENCH:
        canonical_val = canonical.get(name)
        # No canonical reference yet for ⁴He+ at canonical-word
        # convention (per convention_status="DEPRECATED_DISJOINT" in
        # PR #564's atomic-tr-m-helium4.witness.json).  Compute the
        # value via this PR's hybrid-precision path and emit it as
        # the FIRST canonical-word reference (no rel-err comparison).
        t0 = time.monotonic()
        try:
            total, breakdown = tr_m_via_partition_sum_q_hecke(
                Z, N, q_val=Q_MP
            )
            elapsed = time.monotonic() - t0
            new_abs = abs(total)
            if canonical_val is None:
                # No canonical reference: this PR establishes the first
                # canonical-word value.  Future regeneration of
                # atomic-tr-m-mpfr-50dps.witness.json will validate
                # against this number.
                rel_err = mp.nan
                agrees_1e6 = False
                agrees_1e3 = False
                row = {
                    "atom": name,
                    "Z": Z,
                    "N": N,
                    "A": Z + N,
                    "n_strands": 3 * (Z + N),
                    "canonical_abs_tr_M": None,
                    "canonical_status": (
                        "no canonical-word reference yet — this PR's "
                        "hybrid-precision value is the FIRST canonical "
                        "(operator-valued interface) tr_M for this atom"
                    ),
                    "q_hecke_partition_sum": fmt(total),
                    "q_hecke_abs": fmt(new_abs),
                    "elapsed_sec": f"{elapsed:.3f}",
                    "non_zero_partitions": len(breakdown),
                    "top_3_contributions": sorted(
                        breakdown,
                        key=lambda r: -abs(mp.mpf(r["contribution"])),
                    )[:3],
                }
                rows.append(row)
                builder.add_assertion(
                    name=f"q_hecke_seminormal_value_finite[{name}]",
                    computed=str(mp.mpf(0) < new_abs < mp.mpf("1e6")),
                    expected="True",
                )
                print(f"  {name}: canonical=N/A (first-time computation), "
                      f"q-Hecke seminormal={mp.nstr(new_abs, 12)}, {elapsed:.2f}s",
                      file=sys.stderr)
                continue
            rel_err = (
                abs(new_abs - canonical_val) / canonical_val
                if canonical_val != 0
                else mp.inf
            )
            agrees_1e6 = rel_err < mp.mpf("1e-6")
            agrees_1e3 = rel_err < mp.mpf("1e-3")
            rows.append({
                "atom": name,
                "Z": Z,
                "N": N,
                "A": Z + N,
                "n_strands": 3 * (Z + N),
                "canonical_abs_tr_M": fmt(canonical_val),
                "q_hecke_partition_sum": fmt(total),
                "q_hecke_abs": fmt(new_abs),
                "rel_err_vs_canonical": fmt(rel_err),
                "agrees_to_1e_minus_3": bool(agrees_1e3),
                "agrees_to_1e_minus_6": bool(agrees_1e6),
                "elapsed_sec": f"{elapsed:.3f}",
                "non_zero_partitions": len(breakdown),
                "top_3_contributions": sorted(
                    breakdown,
                    key=lambda r: -abs(mp.mpf(r["contribution"])),
                )[:3],
            })
            builder.add_assertion(
                name=f"q_hecke_seminormal_closes_gap[{name}]_to_1e-3",
                computed=str(agrees_1e3),
                expected="True",
            )
            builder.add_assertion(
                name=f"q_hecke_seminormal_closes_gap[{name}]_to_1e-6",
                computed=str(agrees_1e6),
                expected="True",
            )
            if not agrees_1e3:
                all_passed = False
            print(f"  {name}: canonical={mp.nstr(canonical_val, 6)}, "
                  f"q-Hecke seminormal={mp.nstr(new_abs, 6)}, "
                  f"rel_err={mp.nstr(rel_err, 3)}, {elapsed:.2f}s",
                  file=sys.stderr)
        except Exception as exc:
            elapsed = time.monotonic() - t0
            rows.append({
                "atom": name, "Z": Z, "N": N,
                "error": f"{type(exc).__name__}: {exc}",
                "elapsed_sec": f"{elapsed:.3f}",
            })
            print(f"  {name}: ERROR after {elapsed:.2f}s — "
                  f"{type(exc).__name__}: {exc}", file=sys.stderr)
            all_passed = False

    builder.add_data("cross_check_table", rows)
    builder.add_data(
        "method",
        {
            "formula": "tr_M(β) = Σ_{λ ⊢ 3A} y_λ(q_0) · χ^λ_q(β_atomic)",
            "y_lambda_source": (
                "wedderburn_jones_markov.y_lambda_at — Wenzl Schur "
                "principal specialization with numerical-q-from-start "
                "(closes the WEIGHT bug; PR #572 ac7880c5)"
            ),
            "chi_q_source": (
                "hecke_characters.build_seminormal_matrices + "
                "mass_at_3A_proper.chi_lambda_of_word — Hoefsmit "
                "seminormal matrices at q = q_0, traced through the "
                "atomic braid word (closes the CHARACTER gap; this "
                "PR's contribution)"
            ),
            "canonical_reference": (
                "atomic-tr-m-mpfr-50dps.witness.json — produced by "
                "markov_trace_recursive (canonical Markov-axiom "
                "recursive ascent), mpfr 50-dps."
            ),
            "tolerance_tight": "1e-6 relative (full-precision agreement)",
            "tolerance_loose": "1e-3 relative (engineering tolerance)",
        },
    )

    out_path = builder.save()
    print(f"\n  Wrote {out_path}", file=sys.stderr)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
