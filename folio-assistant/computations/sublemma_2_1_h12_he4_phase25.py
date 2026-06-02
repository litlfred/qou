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


def load_f1_cache() -> dict[tuple, complex]:
    """Load F1's chi_q_at_q0 per λ ⊢ 12 from cached witness."""
    cache_path = _pb.witness_path("he4-canonical-tr-m-block-fingerprint.witness.json", HERE)
    if not cache_path.exists():
        raise FileNotFoundError(f"F1 cache not found at {cache_path}")
    d = json.loads(cache_path.read_text())
    data = d.get("data", {})
    contribs = data.get("per_partition_contributions", [])
    chi_a = {}
    for c in contribs:
        part = tuple(c["partition"])
        chi = complex(c["chi_q_at_q0"], 0.0)
        chi_a[part] = chi
    return chi_a


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
    chi_a = load_f1_cache()
    print(f"  Path A loaded from F1 cache: {len(chi_a)} λ ⊢ 12")

    # Path B: iterated branching basis at H_12 ↓ H_9 × H_3
    beta_full = he4_braid_canonical()
    print(f"  β_⁴He: {len(beta_full)} generators")
    print()

    from char_fast import _compiled_sigmas
    parts_12 = partitions_of(12)
    dims = []
    for lam in parts_12:
        _, d = _compiled_sigmas(lam, "double")
        dims.append((lam, d))

    if args.all:
        targets = dims
    else:
        targets = [(l, d) for l, d in dims if d <= args.max_dim]
    print(f"  Processing {len(targets)} / {len(parts_12)} λ ⊢ 12 "
          f"(dim ≤ {args.max_dim if not args.all else 'all'})")
    print()

    print(f"  {'λ':<28} {'dim':>5} {'χ^λ(F1)':>16} {'χ^λ(Path B)':>16} "
          f"{'|rel|':>11}  status")
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
        ok = rel < 1e-9
        if ok:
            n_pass += 1
        status = "✓" if ok else "✗"
        print(f"  {str(lam):<28} {d:>5} {a.real:>+16.8e} {b.real:>+16.8e} "
              f"{rel:>11.2e}  {status}  ({elapsed_b:.2f}s)")

    print()
    print(f"  Verified: {n_pass}/{n_total}  max rel residual: {max_rel:.2e}")
    print(f"  Total Path B compute: {t_total:.1f}s")
    print()

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
        .add_data("max_relative_residual", max_rel)
        .add_data("path_b_compute_time_seconds", t_total)
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
