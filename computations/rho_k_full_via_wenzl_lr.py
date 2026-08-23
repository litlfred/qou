#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath consumer; combines
# pre-computed χ^λ (from Rust binary) with y_λ at q_0 (from
# y-lambda-at-q0.witness.json).
"""ρ_K^full consumer wiring the Wenzl LR producer (PR #674).

⚠ **CONSUMER-SCOPE BUG (2026-05-17, found by
`cross_check_trM_wenzl_lr_1ppb.py`):** the Wenzl LR identity

    χ^λ(β_1 ⊗ β_2) = Σ_{μν} c^λ_{μν} · χ^μ(β_1) · χ^ν(β_2)

applies to **tensor-product (disjoint) braids** only. The
canonical atomic braid `atom_canonical_crossings(Z, N)` is **not**
a tensor product — it includes inter-nucleon arc crossings (the
"averaged" ctype). This script therefore computes
`|tr_M(β_p ⊗ β_n ⊗ ...)|` (disjoint product), **not**
`|tr_M(β_canonical(Z, N))|`. The two diverge by ~80 % relative
on D, T, ³He (cross-check vs Hoefsmit/markov_peel).

The script is retained as the **producer-side primitive** for
tensor-product χ^λ — a building block for a future canonical
consumer that handles non-tensor inter-nucleon braiding per
`hecke-branching-trace-decomposition.md`. The
`atomic_mass_via_rho_k.py` overlay layer 4 was disabled after
this finding; |tr_M| values continue to flow from the Hoefsmit /
markov_peel paths.

Original framing (pre-bug-discovery):

Removes the LO tautology in `atomic_mass_via_rho_k.py` for atoms
A ≥ 2 by computing `|tr_M(canonical β)|` directly via the LR
bridge:

    |tr_M(β)| = | Σ_λ y_λ(q_0) · χ^λ_LR(β) / averaging_denominator |

where:

  - `χ^λ_LR(β)` is the Hecke character of the canonical atomic
    braid β computed via Wenzl LR factorisation across per-nucleon
    sub-braids. Produced by `hecke-tr-m-wenzl-lr` (Rust+rayon).
  - `y_λ(q_0)` is the Jones-Markov central coefficient at the
    substrate parameter, loaded from `y-lambda-at-q0.witness.json`
    via `wedderburn_jones_markov.y_lambda_at(n, Q_0)`.
  - `averaging_denominator = 2^Σ k_i` accounts for the "averaged"
    crossings `0.5·(σ + σ⁻¹)` in the canonical decomposition.

For ⁴He at H_12 this is the first canonical |tr_M| value (the
prior `atomic-tr-m-helium4.witness.json` was a
`DEPRECATED_DISJOINT` placeholder per `atomic_tr_m_mpfr_50dps.py`
deferral note).

## Calibration discipline

This script **does NOT** introduce any new calibration. The Markov
trace `|tr_M(β)|` is a pure prediction from `q_0` (CAL-2 input)
and the canonical braid word (topologically determined by `(Z, N)`).
Per `prop:three-calibration-inputs`, `m_p, m_n` enter only as
CODATA cross-check targets in the side-by-side diff below.

## Status

⚠ **NOT consumable as a canonical |tr_M| source for mass
derivation.** The output of this script is the
tensor-product |tr_M(β_p ⊗ β_n ⊗ …)|, not |tr_M(β_canonical(Z, N))|
— the two diverge by ~80 % on D, T, ³He per
`cross_check_trM_wenzl_lr_1ppb.py`. The witness is emitted with
`set_audit_only` so any downstream wiring that imports it must
treat it as an audit-only / building-block artefact.

**Canonical consumer:** [`canonical_tr_m_via_rust.py`](canonical_tr_m_via_rust.py)
is the production consumer — it calls the
`hecke-canonical-chi` Rust binary which handles the averaged-
crossing inter-nucleon arc structure correctly. Mass-prediction
chains (`atomic_mass_via_rho_k.py`, `rho_k_h3a_refinement.py`,
the Borromean-tower chain) consume canonical |tr_M| via that
path, never via this script's output.

**Building-block role:** This script remains in the codebase as
a tensor-product χ^λ primitive — useful as input to a future
canonical Wenzl-bridge consumer that handles non-tensor inter-
nucleon braiding per
[`hecke-branching-trace-decomposition.md`](../../content/quantum-observable-universe/braids-and-knots/hecke-branching-trace-decomposition.md).
Until that consumer is implemented, the script's output stays
audit-only.

Workplan: `docs/audits/2026-05-17-1ppb-workplan-v4.md` §3 Item 1
(superseded by the canonical Rust route documented in
`docs/audits/2026-05-17-knot-fusion-step1-audit.md`).

## Dependencies

- Rust binary: `tools/hecke-engine/target/{release,debug}/hecke-tr-m-wenzl-lr`
  (build: `cd tools/hecke-engine && cargo build --release --bin hecke-tr-m-wenzl-lr`)
- Python:
  - `markov_trace_via_wenzl_lr.canonical_factor_spec` (binary wrapper)
  - `wedderburn_jones_markov.y_lambda_at` (Markov weights at q_0)
  - `canonical_braid_crossings.atom_canonical_crossings` (canonical word)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def _hash_upstream(path: Path) -> dict:
    """Compute (sha256, commitSha, scriptCommitSha, computedAt) for
    a witness file, for inclusion in
    `derivation_inputs.upstream_witness_hashes` per the anti-staleness
    convention from PR #663.

    Returns an empty record if the path does not exist; emits the
    sha256 unconditionally otherwise (so even legacy witnesses
    without their own metadata get a stable hash entry).
    """
    import hashlib
    import json as _json
    rec: dict = {"path": str(path)}
    if not path.exists():
        rec["status"] = "missing"
        return rec
    raw = path.read_bytes()
    rec["sha256"] = hashlib.sha256(raw).hexdigest()
    rec["bytes"] = len(raw)
    try:
        body = _json.loads(raw)
    except (_json.JSONDecodeError, ValueError):
        rec["status"] = "non-json"
        return rec
    for k in ("commitSha", "scriptCommitSha", "computedAt"):
        if k in body:
            rec[k] = body[k]
    return rec


# Atoms in scope for the LR-bridge consumer. Each entry:
#   (Z, N, label, [per-nucleon-spec])
# where per-nucleon-spec is a list of (sub_Z, sub_N, sub_label) tuples,
# applied via `canonical_factor_spec(sub_Z, sub_N, sub_label)`.
#
# Atoms with H_n ≤ 12 use the cached `y-lambda-at-q0.witness.json`
# (n=2..12 precomputed). ⁶Li (H_18) and ⁷Li (H_21) require live
# y_λ compute via `wedderburn_jones_markov.y_lambda_at(n, q_0)` —
# tractable on the numerical-q-from-start path but minutes/atom.
# Kept out of the default smoke-test list; enable by editing the
# tuple below.
ATOMS = [
    # Deuteron: p ⊗ n at H_6
    (1, 1, "D",  [(1, 0, "p"), (0, 1, "n")]),
    # Tritium: p ⊗ n ⊗ n at H_9
    (1, 2, "T",  [(1, 0, "p"), (0, 1, "n"), (0, 1, "n")]),
    # Helion: p ⊗ p ⊗ n at H_9
    (2, 1, "3He", [(1, 0, "p"), (1, 0, "p"), (0, 1, "n")]),
    # Helium-4: p ⊗ p ⊗ n ⊗ n at H_12 (y_λ cached n=12)
    (2, 2, "4He", [(1, 0, "p"), (1, 0, "p"), (0, 1, "n"), (0, 1, "n")]),
]
# ⁶Li (H_18) and ⁷Li (H_21) deferred: the Rust `hecke-tr-m-wenzl-lr`
# binary timed out at 600 s on ⁶Li under the *debug* build
# (p(18) = 385 partitions × 71 crossings × averaged-expansion).
# Two unblocks (either suffices):
#   - Build release: `cd tools/hecke-engine && cargo build --release
#     --bin hecke-tr-m-wenzl-lr` — typically 5–10× faster.
#   - Use the y_λ-parallel path (`y_lambda_at(n, q_0, workers=…)`)
#     and increase `compute_tr_m_for_atom(..., timeout_sec=…)`
#     to ~3600 s.
# Re-enable by appending to ATOMS:
ATOMS_DEFERRED_NEEDS_RELEASE_BUILD = [
    (3, 3, "6Li", [(1, 0, "p"), (1, 0, "p"), (1, 0, "p"),
                   (0, 1, "n"), (0, 1, "n"), (0, 1, "n")]),
    (3, 4, "7Li", [(1, 0, "p"), (1, 0, "p"), (1, 0, "p"),
                   (0, 1, "n"), (0, 1, "n"), (0, 1, "n"), (0, 1, "n")]),
]


def compute_tr_m_for_atom(Z: int, N: int, label: str,
                          factor_specs: list[tuple[int, int, str]],
                          *, timeout_sec: int = 600) -> dict:
    """Compute |tr_M(canonical β(Z, N))| via the Wenzl LR bridge.

    Returns a dict with `n_strands`, `n_partitions`,
    `averaging_denominator`, `chi_lambda_at_q0_table`,
    `y_lambda_at_q0_table`, `tr_M_q0_mp50dps`, `tr_M_q0_unavail_reason`.
    """
    from markov_trace_via_wenzl_lr import (  # noqa: E402
        canonical_factor_spec,
        find_binary,
        run_lr_compute,
    )
    n_strands = 3 * (Z + N)
    factors = [
        canonical_factor_spec(sub_z, sub_n, sub_lbl)
        for (sub_z, sub_n, sub_lbl) in factor_specs
    ]
    bin_path = find_binary()
    if bin_path is None:
        return {
            "atom": label,
            "Z": Z, "N": N, "n_strands": n_strands,
            "tr_M_q0_unavail_reason": (
                "hecke-tr-m-wenzl-lr binary not built; build via "
                "`cd tools/hecke-engine && cargo build --release "
                "--bin hecke-tr-m-wenzl-lr` to enable this consumer"
            ),
        }
    lr_result = run_lr_compute(
        factors, all_partitions=True, timeout_sec=timeout_sec
    )
    chi_terms = lr_result.get("chi_lambda_terms", [])
    averaging_denominator = int(lr_result["averaging_denominator"])

    # Load y_λ at q_0 for n = n_strands.
    from wedderburn_jones_markov import y_lambda_at  # noqa: E402
    from q_parameter import Q_50_DIGIT_STR  # noqa: E402

    # Combine: tr_M = (1 / averaging_denominator) · Σ_λ y_λ · χ^λ
    # χ^λ_LR contains q in symbolic form; we evaluate at q_0.
    Q_0 = mp.mpf(Q_50_DIGIT_STR)  # 50-dps q, not f64-quantised
    # NO FLOAT64 (AGENTS.md "PROBES ARE NOT EXEMPT"; bean qou-65qv). The line
    # above has always declared the intent -- "50-dps q, not f64-quantised" --
    # and three lines below it was thrown away by `subs("q", float(Q_0))`, with
    # the weights separately taken at the float64 `Q_FLOAT`. Every downstream
    # value then carried ~16 good digits into a field named `..._mp30dps`.
    y_table = y_lambda_at(n_strands, Q_0)
    tr_m_sum = mp.mpf(0)
    chi_lambda_table = []
    for term in chi_terms:
        lam = tuple(term["lambda"])
        # The Rust binary's `chi_polynomial` field is a Laurent
        # polynomial in q rendered as a string. We parse via sympy
        # and evaluate at q_0. (This is O(n_partitions · poly_length)
        # — small.)
        try:
            chi_expr = sp.sympify(
                term["chi_polynomial"].replace("^", "**")
            )
        except (sp.SympifyError, SyntaxError) as e:
            return {
                "atom": label, "Z": Z, "N": N, "n_strands": n_strands,
                "tr_M_q0_unavail_reason": (
                    f"sympify of chi_polynomial for λ={lam} failed: {e}"
                ),
            }
        # Substitute q by name (sympify creates its own symbol; we
        # cannot rely on a pre-built `sp.Symbol("q")` matching it).
        # `subs("q", ...)` finds the symbol by name.
        # Substitute at 50 dps and evaluate symbolically, rather than
        # collapsing q to a double first.
        chi_at_q0 = mp.mpf(str(sp.N(
            chi_expr.subs("q", sp.Float(Q_50_DIGIT_STR, 50)), 50)))
        y_lam = y_table.get(lam)
        if y_lam is None:
            return {
                "atom": label, "Z": Z, "N": N, "n_strands": n_strands,
                "tr_M_q0_unavail_reason": (
                    f"y_λ table at H_{n_strands} missing partition "
                    f"λ={lam}"
                ),
            }
        y_at_q0 = mp.mpf(y_lam)
        contribution = y_at_q0 * chi_at_q0
        tr_m_sum += contribution
        chi_lambda_table.append({
            "lambda": list(lam),
            "chi_q0": mp.nstr(chi_at_q0, 12),
            "y_q0": mp.nstr(y_at_q0, 12),
            "contribution_q0": mp.nstr(contribution, 12),
        })
    tr_m_q0 = tr_m_sum / mp.mpf(averaging_denominator)
    return {
        "atom": label,
        "Z": Z, "N": N, "n_strands": n_strands,
        "n_partitions": len(chi_terms),
        "averaging_denominator": averaging_denominator,
        "factor_labels": [s[2] for s in factor_specs],
        "tr_M_q0_mp30dps": mp.nstr(tr_m_q0, 30),
        "abs_tr_M_q0_mp30dps": mp.nstr(abs(tr_m_q0), 30),
        "chi_lambda_table_top10": chi_lambda_table[:10],
        "duration_ms_total": sum(
            t.get("duration_ms", 0) for t in chi_terms
        ),
    }


def main() -> int:
    from q_parameter import Q as _Q_FLOAT_DOC  # noqa: E402
    global Q_FLOAT_FOR_DOC  # captured by the witness's calibration_anchors
    Q_FLOAT_FOR_DOC = _Q_FLOAT_DOC
    rows = []
    for (Z, N, label, specs) in ATOMS:
        print(f"\n→ Computing |tr_M({label})| via Wenzl LR "
              f"at H_{3*(Z+N)} ({len(specs)}-way factorisation)...")
        row = compute_tr_m_for_atom(Z, N, label, specs)
        rows.append(row)
        if "tr_M_q0_unavail_reason" in row:
            print(f"  ✗ unavailable: {row['tr_M_q0_unavail_reason']}")
        else:
            print(f"  |tr_M| at q_0 = {row['abs_tr_M_q0_mp30dps']} "
                  f"({row['n_partitions']} partitions, "
                  f"{row['duration_ms_total']} ms LR total)")

    # Anti-staleness: hash every upstream witness this script reads
    # so `witness_dependency_drift.py` can detect silent staleness
    # when the upstream changes without this consumer regenerating.
    upstream_paths = [
        _pb.witness_path("y-lambda-at-q0.witness.json", HERE),
    ]
    upstream_hashes = [_hash_upstream(p) for p in upstream_paths]

    out = {
        "computation": "rho-k-full-via-wenzl-lr",
        "derivation_inputs": {
            "upstream_witness_hashes": upstream_hashes,
            "calibration_anchors": {
                "Q_0": str(Q_FLOAT_FOR_DOC),
                "note": (
                    "q_0 is the CAL-2 substrate parameter; no other "
                    "calibration enters this consumer."
                ),
            },
        },
        "description": (
            "ρ_K^full producer-side primitive: emits the tensor-"
            "product |tr_M(β_p ⊗ β_n ⊗ …)| via the Wenzl LR bridge "
            "(PR #674). ⚠ **Output is NOT the canonical |tr_M(β_canonical)|** — "
            "the canonical atomic braid is not a tensor product (inter-"
            "nucleon arc crossings break tensor structure), and the two "
            "diverge by ~80 % on D, T, ³He per "
            "`cross_check_trM_wenzl_lr_1ppb.py`. The canonical mass-"
            "derivation consumer is `canonical_tr_m_via_rust.py` "
            "(via `hecke-canonical-chi` Rust binary), which handles "
            "the averaged-crossing structure correctly. This script's "
            "witness is retained as an audit-only building block for a "
            "future non-tensor Wenzl bridge per "
            "`hecke-branching-trace-decomposition.md`."
        ),
        "calibration_discipline": (
            "Pure prediction from q_0 (CAL-2 input) and per-nucleon "
            "braid words. No new calibration. Output is audit-only "
            "per the consumer-scope bug — does not feed any production "
            "mass-derivation chain."
        ),
        "rows": rows,
        "workplan_ref": (
            "docs/audits/2026-05-17-1ppb-workplan-v4.md §3 Item 1 "
            "(superseded by canonical Rust route in "
            "docs/audits/2026-05-17-knot-fusion-step1-audit.md). "
            "Canonical consumer: canonical_tr_m_via_rust.py."
        ),
    }
    out_path = (
        WitnessBuilder.wrap_legacy(
            "rho-k-full-via-wenzl-lr",
            out,
            script_path=__file__,
            engine="rust+mpmath",
        )
        .set_audit_only(
            "docs/audits/2026-05-17-1ppb-workplan-v4.md")
        .save()
    )
    print(f"\n→ wrote {out_path}")
    print(f"  atoms: {len(rows)}; "
          f"available: {sum(1 for r in rows if 'tr_M_q0_unavail_reason' not in r)}/"
          f"{len(rows)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
