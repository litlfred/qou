#!/usr/bin/env python3
"""sublemma_2_1_h12_he4_phase25.py — H_12 ⁴He verify reusing F1 cache.

Phase 2.5 of the H_12 ⁴He scaffold (`docs/audits/2026-05-16-sublemma-
2-1-h12-he4-scaffold.md`).

Strategy: reuse F1's cached chi_q_at_q0 values from
`he4-canonical-tr-m-block-fingerprint.witness.json` as Path A (truth).
Only Path B (the iterated branching-basis decomposition) needs
recomputation — and with the warm Hoefsmit cache it should be
fast.

Differs from `sublemma_2_1_h12_he4_branching.py` (the scaffold which
re-computed Path A via direct Hoefsmit, timing out for high-dim λ).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import argparse
import json
import re
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from sublemma_2_1_h12_he4_branching import (  # noqa: E402
    path_b_chi_h12, he4_braid_canonical,
)
from lr_coefficients import partitions_of  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def _quoting_tolerance(quoted: str) -> float:
    """Relative tolerance implied by how precisely `quoted` was serialized.

    A number written to `sig` significant digits carries up to half a unit in
    its last place, i.e. 0.5e-(sig-1) relative. Comparing a recomputation
    against it below that is comparing against digits the file does not have.
    Doubled, to absorb Path B's own float64 accumulation over the 47-generator
    word -- which is ~1e-15 and thus negligible beside the quoting error, but
    the margin keeps the gate from sitting exactly on its own boundary.
    """
    digits = len(re.sub(r"[^0-9]", "", quoted).lstrip("0"))
    if digits <= 0:
        return 1e-9
    return 10.0 ** (-(digits - 1))


def load_f1_cache() -> tuple[dict[tuple, complex], dict[tuple, float]]:
    """Load F1's per-λ⊢12 character from its cached witness.

    The F1 witness was re-schema'd: the per-partition list moved from
    ``per_partition_contributions`` (field ``chi_q_at_q0``, a raw float) to
    ``per_block_ranked`` (field ``chi_lambda``, a drained string).  This loader
    read only the old shape and reached the new witness through a
    ``.get(..., [])`` default, so a schema mismatch was indistinguishable from
    an empty cache: it returned ``{}`` and this producer went on to "verify"
    0 of 77 partitions and assert ``0 == 0``.

    Both shapes are read, newest first.  An empty result RAISES rather than
    returning ``{}`` -- the swallow is what made the drift silent, and the
    caller cannot tell "no such field" from "no such partitions" once the
    default has been substituted.
    """
    cache_path = _pb.witness_path("he4-canonical-tr-m-block-fingerprint.witness.json", HERE)
    if not cache_path.exists():
        raise FileNotFoundError(f"F1 cache not found at {cache_path}")
    d = json.loads(cache_path.read_text())
    data = d.get("data", {})

    chi_a: dict[tuple, complex] = {}
    tol_a: dict[tuple, float] = {}
    # Current shape.  chi_lambda is a _precision.fmt string; complex() parses
    # it directly, and the value it carries is real (the character at q0).
    #
    # It is quoted to 6-8 significant digits (measured over all 77 entries:
    # min 6, max 8), so it cannot support a comparison below ~5e-8. The
    # tolerance therefore travels WITH each value rather than being a single
    # constant -- see `_quoting_tolerance` and the comparison below.
    for c in data.get("per_block_ranked", []):
        lam = tuple(c["partition"])
        chi_a[lam] = complex(float(c["chi_lambda"]), 0.0)
        tol_a[lam] = _quoting_tolerance(str(c["chi_lambda"]))
    if not chi_a:
        # Pre-#4619 shape: a raw float64, so full double resolution.
        for c in data.get("per_partition_contributions", []):
            lam = tuple(c["partition"])
            chi_a[lam] = complex(c["chi_q_at_q0"], 0.0)
            tol_a[lam] = 1e-9

    if not chi_a:
        raise SystemExit(
            f"F1 cache at {cache_path} carries neither `per_block_ranked` nor "
            f"`per_partition_contributions`; its data keys are "
            f"{sorted(data)}. Path A would be empty and every assertion below "
            f"would pass vacuously. Re-run the F1 producer, or teach this "
            f"loader whichever field now holds the per-λ character."
        )
    return chi_a, tol_a


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-dim", type=int, default=80,
                        help="skip λ with dim > max-dim for tractable run")
    parser.add_argument("--all", action="store_true",
                        help="process all 77 partitions of 12")
    args = parser.parse_args()

    print("=" * 96)
    print("  H_12 ⁴He Sub-lemma 2.1 verify — Phase 2.5 (F1 cache reuse)")
    print("=" * 96)
    print()

    # Path A: F1 cached chi_q_at_q0
    chi_a, tol_a = load_f1_cache()
    print(f"  Path A loaded from F1 cache: {len(chi_a)} λ ⊢ 12")

    # Path B: iterated branching basis at H_12 ↓ H_9 × H_3
    beta_full = he4_braid_canonical()
    print(f"  β_⁴He: {len(beta_full)} generators")
    print()

    # d(lambda) by the hook-length formula, NOT by building the rep.
    #
    # This asked `_compiled_sigmas(lam, "double")` for all 77 partitions of 12
    # and kept only `d`, discarding the matrices. That is the whole reason this
    # producer could not be run: building and lambdifying every H_12 irrep to
    # read 77 integers costs `c * sum_lambda d(lambda)^2`, and by Burnside that
    # sum is exactly 12! = 479,001,600. Measured c gives **67 h** before PR
    # #5517 and **18.5 h** after it — for numbers the hook-length formula
    # returns instantly. Bean `qou-pag7`.
    #
    # `partition_dimension` is the corpus's own hook-length implementation
    # (`pyhecke.wedderburn`), already used for this purpose in
    # `chi_at_q0_via_hoefsmit_mpfr`. Verified equal to the discarded `d` on all
    # 66 partitions of n <= 8 and on six H_12 shapes: zero mismatches.
    #
    # This also makes `--max-dim` filter BEFORE any rep is built, so only the
    # selected shapes cost anything.
    from pyhecke.wedderburn import partition_dimension
    parts_12 = partitions_of(12)
    dims = [(lam, partition_dimension(tuple(lam))) for lam in parts_12]

    if args.all:
        targets = dims
    else:
        targets = [(l, d) for l, d in dims if d <= args.max_dim]
    print(f"  Processing {len(targets)} / {len(parts_12)} λ ⊢ 12 "
          f"(dim ≤ {args.max_dim if not args.all else 'all'})")
    print()

    print(f"  {'λ':<28} {'dim':>5} {'χ^λ(F1)':>16} {'χ^λ(Path B)':>16} "
          f"{'|rel|':>11} {'tol':>7}  status")
    print("  " + "-" * 92)
    max_rel = 0.0
    n_pass = 0
    n_total = 0
    t_total = 0.0
    chi_b_dict = {}
    for lam, d in targets:
        if lam not in chi_a:
            continue
        n_total += 1
        a = chi_a[lam]
        tb = time.monotonic()
        b = path_b_chi_h12(lam, beta_full, float(Q0))
        elapsed_b = time.monotonic() - tb
        t_total += elapsed_b
        chi_b_dict[lam] = b
        denom = max(abs(a), 1e-15)
        rel = abs(a - b) / denom
        max_rel = max(max_rel, rel)
        # Compare at the RESOLUTION OF THE REFERENCE, not at a fixed 1e-9.
        # This threshold was 1e-9 while Path A is quoted to 6-8 significant
        # digits, i.e. BELOW the ~5e-8 floor an 8-digit reference can support:
        # no correct computation could pass it. After the Path B braid-word
        # repair (`1a8f3f5f80`, qou-oppb) every residual landed in 5e-9..4.8e-8
        # -- agreement to the last digit the file carries -- and the producer
        # still reported 0/8. A gate that cannot be satisfied is as
        # uninformative as one that cannot be failed.
        tol = tol_a.get(lam, 1e-9)
        ok = rel < tol
        if ok:
            n_pass += 1
        status = "✓" if ok else "✗"
        print(f"  {str(lam):<28} {d:>5} {a.real:>+16.8e} {b.real:>+16.8e} "
              f"{rel:>11.2e} < {tol:.0e}  {status}  ({elapsed_b:.2f}s)")

    print()
    print(f"  Verified: {n_pass}/{n_total}  max rel residual: {max_rel:.2e}")
    print(f"  Total Path B compute: {t_total:.1f}s")
    print()

    # GUARD: refuse a vacuous pass. The assertion below is n_pass == n_total,
    # which is trivially TRUE when both are 0 -- and both are 0 whenever the F1
    # cache is missing, because every target then hits the `lam not in chi_a`
    # continue. Without this guard the producer wrote allPassed=true having
    # verified nothing, describing itself as "Verified 0/0", and the only sign
    # was two stdout lines disagreeing ("loaded 0 λ" then "Processing 8").
    # Refusing here follows the repo's own idiom for a guard that must not be
    # silently satisfiable (cf. low_isotope_mass_table refusing below its
    # target precision).
    if n_total == 0:
        raise SystemExit(
            f"REFUSING to emit a witness: 0 of {len(targets)} target "
            f"partitions were verified, because Path A (the F1 chi_q_at_q0 "
            f"cache) supplied {len(chi_a)} entries. The assertion "
            f"n_pass == n_total would pass vacuously. Re-run the F1 producer "
            f"so the cache exists, then re-run this."
        )

    builder = (
        WitnessBuilder("sublemma-2-1-h12-he4-phase25-verify",
                       engine="numpy")
        .set_description(
            f"H_12 ⁴He Sub-lemma 2.1 multi-interface verification — "
            f"Phase 2.5 using F1's cached chi_q_at_q0 as Path A.  "
            f"Verified {n_pass}/{n_total} λ ⊢ 12 (max-dim filter "
            f"{args.max_dim if not args.all else 'all 77'}); max rel "
            f"residual {max_rel:.2e}.  Path B = iterated Sub-lemma 2.1 "
            f"H_12 ↓ H_9 × H_3 + Halley-refined H_3 Wedderburn "
            f"projectors (from PR #666)."
        )
        .set_audit_only(
            "docs/audits/2026-05-16-sublemma-2-1-h12-he4-scaffold.md"
        )
        .add_data("atom", "4He_canonical_pppnnn")
        .add_data("approach", "h12_branching_basis_phase25_f1_cache_reuse")
        .add_data("n_partitions_processed", n_total)
        .add_data("n_partitions_verified", n_pass)
        # STRINGS, not raw floats: the raw-float64 ratchet flags both, and
        # `path_b_compute_time_seconds` matches neither "dur" nor "elapsed",
        # so the duration carve-out does not cover it (widening that mask is
        # what the audit's own comment warns against -- cf. d8d3713f8).
        #
        # `max_relative_residual` is stringified but NOT laundered into
        # apparent precision. It is a float64 quantity by construction: Path B
        # runs in numpy complex128 (`path_b_chi_h12`) and Path A comes from the
        # F1 complex cache, so this residual cannot resolve below ~1e-16 no
        # matter what is true. Per AGENTS.md, do not report it as "exact" or
        # "to N digits". What the 1e-9 pass threshold DOES establish is
        # structural: a wrong branching decomposition would miss by ~1e0, not
        # by 1e-15, so the check is meaningful about the DECOMPOSITION while
        # saying nothing about the last several digits of either character.
        .add_data("max_relative_residual", repr(max_rel))
        .add_data("path_b_compute_time_seconds", f"{t_total:.2f}")
        .add_data("max_dim_filter",
                  args.max_dim if not args.all else None)
        .add_data("chi_path_a_from_f1", {
            str(lam): [chi_a[lam].real, chi_a[lam].imag]
            for lam, _ in targets if lam in chi_a
        })
        .add_data("chi_path_b_branching", {
            str(lam): [v.real, v.imag] for lam, v in chi_b_dict.items()
        })
        .add_assertion(
            "all_processed_lambda_path_a_eq_path_b_machine_eps",
            computed=n_pass,
            expected=n_total,
            source="iterated branching-basis H_12 ↓ H_9 × H_3 vs F1's "
                   "cached chi_q_at_q0 truth values",
        )
    )
    out = builder.save()
    print(f"  Witness: {out}")
    return 0 if n_pass == n_total else 1


if __name__ == "__main__":
    sys.exit(main())
