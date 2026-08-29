#!/usr/bin/env python3
"""Full χ_λ(β_⁴He) table — all 77 partitions of 12 at q_0.

Per author direction 2026-05-25: "get us to 1ppb please" + first
measurement (chi_lambda_multi_block_first_measurement.py) established
the wiring works.

## β_⁴He construction

The framework's heuristic ⁴He braid (per `mass_table_ppb.py` magic
A·8G rule) is 4 disjoint copies of Borromean in B_12:

  β_⁴He = β_𝓑₃^{(strands 1,2,3)} · β_𝓑₃^{(4,5,6)} · β_𝓑₃^{(7,8,9)} · β_𝓑₃^{(10,11,12)}

Each Borromean is (σ_i σ_{i+1}⁻¹)³ on its triple. Total braid word
length: 24 letters (4 copies × 6 letters).

This is the EXPLORATORY heuristic per Rule-14 census; the canonical
β_⁴He would have inter-nucleon `⋈_K` bowtie couplings between the 4
nucleon triples (D9 isospin-from-canonical-bowtie scaffold, PR #1162).

## What this script measures

For each of the 77 partitions λ ⊢ 12, compute χ_λ(β_⁴He) at q_0.
Sorted by |χ_λ| descending to identify which partitions dominate
the multi-block distribution.

## Why this matters for 1 ppb path

The canonical mass formula

  B(⁴He) = m_e · Σ_λ y_λ · χ_λ(β_⁴He)

needs both χ_λ (this script supplies all 77) and y_λ (R5-full SDP
pending). With the χ_λ table in hand, ANY proposed y_λ distribution
can be tested immediately against AME = 28.30 MeV.

## §Slot J diagnostics

- GB filtration: ℓ(β_⁴He) = 24 crossings (4 disjoint copies × 6)
- Jet order: f64 evaluation at q_0; for full 1 ppb need MPFR via
  `chi_lambda_braid_mpfr` (also available in pyhecke_native)
- Bar-symmetry: paired partitions λ ↔ λ^T have related χ_λ values;
  test in §3 of output
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

import mpmath as mp
import pyhecke_native as pn
from hecke_characters import chi_lambda_braid as _chi_braid  # noqa: E402
from sympy.utilities.iterables import partitions

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder, record_upstream  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402


def _as_dim(x) -> int:
    """A Specht dimension as an int, refusing anything that is not whole."""
    v = float(x)
    if abs(v - round(v)) > 1e-9:
        raise ValueError(
            f"dim_S_lambda is not a whole number: {v!r}. That is a finding "
            "about the character routine, not a formatting problem -- do not "
            "round it away.")
    return int(round(v))


# Upstream hash records captured before the WitnessBuilder exists;
# attached at construction. Owned by this module — see
# `record_upstream` in qou_substrate.witness for why it is not global.
_UPSTREAM_RECORDS: list = []

set_compute_dps()
Q_PIN = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)
# 🛑 PROTON PIN (migrated 2026-08-29, bean `qou-cds3`). AGENTS.md
# §"q₀ anchor convention": the experimental (proton) anchor is the default
# for all production compute, and the owner authorisation recorded there
# covers this sweep ("we want proton unless for an explicit reason ... fix
# all, even if not visible").
#
# This read `q-pinning-50-digit.witness.json` -> `derived_50_digit.q`, the
# MUON value, which NO manifest entry and NO `QOU_Q0_ANCHOR` could reach: a
# direct read of the anchor-defining witness computes at muon whatever the
# configuration says. The two pins differ by 11.54 ppb, the μ–p substrate
# tension itself.
#
# The upstream record is KEPT — that witness remains the canonical 3-CAL
# (muon) pin document, it is simply no longer the source of this
# computation's q₀. Idiom copied from `alpha/alpha_k_jones_markov_h12.py`.
record_upstream(Q_PIN, _UPSTREAM_RECORDS)
from q_parameter import Q_50_DIGIT_STR as _Q50_PROTON  # noqa: E402
q0_mpf = mp.mpf(_Q50_PROTON)
q0_f64 = float(q0_mpf)
h_f64 = float(q0_mpf - 1 / q0_mpf)
h_sq_f64 = h_f64 * h_f64

# β_⁴He heuristic: 4 disjoint Borromean copies in B_12
# Strands 1,2,3 (gens 1,2); 4,5,6 (gens 4,5); 7,8,9 (gens 7,8); 10,11,12 (gens 10,11)
def borromean_on_strand_triple(base_strand: int) -> list[tuple[int, int]]:
    """Build (σ_b σ_{b+1}⁻¹)³ where b = base_strand (1-based)."""
    s1, s2 = base_strand, base_strand + 1
    word = []
    for _ in range(3):
        word.append((1, s1))
        word.append((-1, s2))
    return word

BETA_HE4 = (
    borromean_on_strand_triple(1)   # strands 1,2,3
    + borromean_on_strand_triple(4)   # strands 4,5,6
    + borromean_on_strand_triple(7)   # strands 7,8,9
    + borromean_on_strand_triple(10)  # strands 10,11,12
)


def partitions_of(n: int) -> list[list[int]]:
    """Return all partitions of n as descending-sorted lists."""
    shapes = []
    for p in partitions(n):
        parts = sorted(p.items(), reverse=True)
        expanded = []
        for size, count in parts:
            expanded.extend([size] * count)
        shapes.append(expanded)
    return shapes


def transpose_partition(shape: list[int]) -> list[int]:
    """Conjugate (transpose) partition λ → λ^T."""
    if not shape:
        return []
    max_part = max(shape)
    return [sum(1 for x in shape if x >= i) for i in range(1, max_part + 1)]


def main() -> int:
    print("=" * 110)
    print("FULL χ_λ(β_⁴He) TABLE — all 77 partitions of 12 at q_0")
    print(f"  q_0 = {q0_f64:.10f}   h = {h_f64:.10f}   h² = {h_sq_f64:.10f}")
    print(f"  β_⁴He = 4 disjoint Borromean copies (24-letter braid in B_12)")
    print("  HEURISTIC per Rule-14 census; canonical β awaits inter-nucleon ⋈_K")
    print("=" * 110)

    shapes_12 = partitions_of(12)
    print(f"\nEnumerating {len(shapes_12)} partitions of 12...")

    rows = []
    t_start = time.time()
    for shape in shapes_12:
        # `chi_lambda_braid_mpf`, not `pn.chi_lambda_braid(..., q0_f64)`:
        # the latter enters the f64 Rust kernel, so every χ_λ in this table
        # was float64 end to end. AGENTS.md §"PROBES ARE NOT EXEMPT": a
        # float64 input poisons the whole result. `f64_into_mpmath_audit`'s
        # own test cases name this exact fix. Bean `qou-k6b3`.
        # the mpfr path returns a decimal STRING so no precision is lost
        # crossing the boundary; re-enter mpmath from it.
        chi = mp.mpf(str(_chi_braid(shape, BETA_HE4, q0_mpf,
                                    precision="mpfr_50dps")))
        dim = mp.mpf(str(_chi_braid(shape, [], q0_mpf,
                                    precision="mpfr_50dps")))
        shape_str = "(" + ",".join(map(str, shape)) + ")"
        rows.append({
            "partition": shape,
            "partition_str": shape_str,
            # A Specht dimension is a COUNT of standard Young tableaux, so it
            # ships as a JSON integer. It was `float(dim)`, which wrote `54.0`
            # -- the same number, a different claim, and one a TypeScript
            # consumer cannot tell from a measurement because `JSON.parse`
            # collapses `54` and `54.0` to the same `number`. Declared in
            # `computations/witness-integer-fields.json` and enforced by
            # `witness_integer_field_audit`. Bean `qou-xt5l`.
            #
            # `_as_dim` refuses a value that is not whole rather than rounding
            # it away: a fractional dimension would be a real finding here, and
            # silently truncating it is how it would stay hidden.
            "dim_S_lambda": _as_dim(dim),
            "chi_lambda_he4": fmt(chi),
            "abs_chi": fmt(abs(chi)),
            # Not serialized — `_abs_mp` carries the mpf for the sort, the
            # ratio arithmetic and the cumulative sums below, so those stay
            # exact while the witness fields are strings. Popped before save.
            "_abs_mp": abs(chi),
            "_chi_mp": chi,
        })
    elapsed = time.time() - t_start
    print(f"All χ_λ computed in {elapsed:.3f}s ({elapsed/len(shapes_12)*1000:.1f}ms per partition)")
    print()

    # Sort by |χ_λ| descending
    rows_sorted = sorted(rows, key=lambda r: -r["_abs_mp"])

    # Print top-20 by |χ_λ|
    print(f"  {'rank':>4}  {'partition':>30}  {'dim S_λ':>9}  {'χ_λ(β_⁴He)':>18}  {'|χ_λ|':>14}  ratio_to_max")
    print("  " + "-" * 108)
    max_abs = rows_sorted[0]["_abs_mp"] if rows_sorted else mp.mpf(1)
    for i, r in enumerate(rows_sorted[:20]):
        ratio = r["_abs_mp"] / max_abs * 100 if max_abs > 0 else mp.mpf(0)
        print(f"  {i+1:>4}  {r['partition_str']:>30}  {r['dim_S_lambda']:>9.1f}  "
              f"{mp.nstr(r['_chi_mp'], 8):>18}  "
              f"{mp.nstr(r['_abs_mp'], 8):>14}  {mp.nstr(ratio, 3):>5}%")

    # Also show the very last 5 (smallest |χ_λ|)
    print()
    print("  Tail (smallest |χ_λ|):")
    for i, r in enumerate(rows_sorted[-5:]):
        rank = len(rows_sorted) - 5 + i + 1
        ratio = r["_abs_mp"] / max_abs * 100 if max_abs > 0 else mp.mpf(0)
        print(f"  {rank:>4}  {r['partition_str']:>30}  {r['dim_S_lambda']:>9.1f}  "
              f"{mp.nstr(r['_chi_mp'], 8):>18}  "
              f"{mp.nstr(r['_abs_mp'], 8):>14}  {mp.nstr(ratio, 3):>5}%")

    # Bar-symmetry / partition-conjugation check
    print()
    print("BAR-SYMMETRY CHECK (paired partitions λ ↔ λ^T):")
    paired_count = 0
    self_conj_count = 0
    matched_pair_count = 0
    seen = set()
    for r in rows:
        shape = r["partition"]
        shape_T = transpose_partition(shape)
        key = tuple(shape)
        key_T = tuple(shape_T)
        if key in seen or key_T in seen:
            continue
        if key == key_T:
            self_conj_count += 1
        else:
            r_T = next((x for x in rows if x["partition"] == shape_T), None)
            if r_T is not None:
                paired_count += 1
                rel_diff = (abs(r["_chi_mp"] - r_T["_chi_mp"])
                            / max(abs(r["_chi_mp"]), mp.mpf("1e-12")))
                if rel_diff < 1e-6:
                    matched_pair_count += 1
            seen.add(key)
            seen.add(key_T)
    print(f"  Self-conjugate partitions:   {self_conj_count}")
    print(f"  Conjugate pairs total:       {paired_count}")
    print(f"  Conjugate pairs with equal χ: {matched_pair_count} / {paired_count}")

    # Weight summary: sum of |χ_λ|
    total_abs = sum((r["_abs_mp"] for r in rows), mp.mpf(0))
    cumulative = 0
    threshold_blocks = None
    for i, r in enumerate(rows_sorted):
        cumulative += r["_abs_mp"]
        if cumulative / total_abs >= 0.95 and threshold_blocks is None:
            threshold_blocks = i + 1
    print()
    print("WEIGHT DISTRIBUTION:")
    print(f"  Σ_λ |χ_λ(β_⁴He)| = {total_abs:.6f}")
    print(f"  Top {threshold_blocks} partitions carry 95% of |χ|-weight")
    print(f"  Production projects to 1 of 77 blocks; 95%-cover needs {threshold_blocks}")

    # Witness
    w = WitnessBuilder("chi-lambda-he4-full-partition-table", engine="python+pyhecke-native")
    w.add_upstream_records(_UPSTREAM_RECORDS)  # declare upstreams read before this builder existed
    w.set_description(
        "Full χ_λ(β_⁴He) table — all 77 partitions of 12 evaluated on "
        "the heuristic 4·Borromean tensor at q_0. Structural template "
        "for the canonical mass formula B(⁴He) = m_e · Σ_λ y_λ · χ_λ "
        "when R5-full SDP supplies y_λ. Shows the multi-block "
        "distribution that production's single-block ν_SDP=2 projection "
        "discards."
    )
    w.add_parameter("q_0_f64", q0_f64)
    w.add_parameter("n_partitions", len(shapes_12))
    w.add_parameter("braid_length", len(BETA_HE4))
    w.add_parameter("beta_construction", "4 disjoint Borromean copies (strands 1-3, 4-6, 7-9, 10-12)")
    w.add_parameter("elapsed_seconds", float(elapsed))
    w.add_data("per_partition_chi_lambda", rows)
    # The mpf helper keys are for arithmetic only and are not JSON types;
    # drop them before any row reaches the witness.
    for _r in rows:
        _r.pop("_abs_mp", None)
        _r.pop("_chi_mp", None)
    w.add_data("top_20_by_abs_chi", rows_sorted[:20])
    w.add_data("self_conjugate_count", self_conj_count)
    w.add_data("conjugate_pair_count", paired_count)
    w.add_data("matched_conjugate_pair_count", matched_pair_count)
    w.add_data("sum_abs_chi", fmt(total_abs))
    w.add_data("blocks_for_95pct_cover", threshold_blocks)
    w.add_assertion(
        "all_77_partitions_evaluated",
        computed=len(rows),
        expected=77,
        tolerance=0,
        unit="partitions",
        source="full partition enumeration via sympy.utilities.iterables.partitions(12)",
    )
    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
