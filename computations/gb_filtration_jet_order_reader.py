#!/usr/bin/env python3
# polynomial_q_not_applicable: structural reader for jet-order witness; no symbolic-q polynomial in this layer.
"""GB-filtration / jet-order witness reader · Python fallback for P6 (PR #564).

Per [`AUDIT-DEEP-2026-05.md`](../../AUDIT-DEEP-2026-05.md) §5 +
`docs/coordination/1ppb.md` §Open phases · P6, the
`gb-filtration-jet-order.witness.json` produced by
`gb_filtration_jet_tracker.py` already encodes per-particle
sparsity patterns (filtration grade J^ℓ / J^{ℓ+1}) and
reduction-event ordering (jet order). The Rust SDP solver does
not yet consume them (R5-full SDP is incomplete per
`docs/derivation-tracking-methodology.md`); the legacy Python
solvers (`joint_tower_sdp_solver.py`, `joint_tower_sdp_solver_v2.py`)
do not consume them either — they enumerate the full Hecke basis.

This module is the **Python-fallback bridge**: it loads the
witness, exposes a structured API for sparsity/decomposition
hints, and provides a `decorate_solver_problem(...)` helper that
any Python SDP solver can call to pre-restrict its variable space.

Coordination: P6 was scope-checked on PR #565
(comment 4408891653); no answer yet on Rust solver location or
F11 strict-mode scope. This Python-fallback layer is non-invasive
and doesn't pre-empt those answers — once #565 confirms, the
same patterns can be ported to Rust.

API:
    pattern = load_jet_order_witness("gb-filtration-jet-order.witness.json")
    pattern[atom_name].filtration_shape    # dict[grade → multiplicity]
    pattern[atom_name].max_grade           # int
    pattern[atom_name].n_strands           # H_n index
    pattern[atom_name].n_steps             # reduction events
    decorate_solver_problem(problem, pattern)  # in-place restriction

Output: `gb-filtration-jet-order-reader.witness.json` (audit trail
for which test cases were loaded and what speedup they imply for
each consumer solver).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from math import factorial  # float64-ok: exact integer factorial
from pathlib import Path
from typing import Iterable

import mpmath as mp  # noqa: E402
from _precision import fmt as _fmt, set_compute_dps  # noqa: E402

set_compute_dps()

HERE = Path(__file__).parent

DEFAULT_WITNESS = _pb.witness_path("gb-filtration-jet-order.witness.json", HERE)


@dataclass
class SparsityPattern:
    """Per-test-case sparsity pattern from the GB-filtration witness."""

    name: str
    n_strands: int
    filtration_shape: dict[int, int]      # grade → multiplicity
    max_grade: int
    n_steps: int
    n_hecke_relations_fired: int
    word: list[int] = field(default_factory=list)
    closure_components: int = 0

    @property
    def total_basis_size(self) -> int:
        """`|H_n| = n!` — full enumeration cost without filtration."""
        return factorial(self.n_strands)

    @property
    def filtered_basis_size(self) -> int:
        """`Σ_grade multiplicity` — variable count after filtration."""
        return sum(self.filtration_shape.values())

    @property
    def reduction_factor(self) -> mp.mpf:
        """`|H_n| / Σ multiplicity` — speed-up estimate."""
        if self.filtered_basis_size == 0:
            return mp.mpf(0)
        return mp.mpf(self.total_basis_size) / mp.mpf(self.filtered_basis_size)


def load_jet_order_witness(
    path: Path | str = DEFAULT_WITNESS,
) -> dict[str, SparsityPattern]:
    """Load the GB-filtration / jet-order witness and return one
    `SparsityPattern` per test case keyed by name."""
    from gb_filtration_jet_tracker import closure_component_count
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(
            f"Jet-order witness not found at {p}. Run "
            "gb_filtration_jet_tracker.py first to produce it."
        )
    d = json.loads(p.read_text())
    out: dict[str, SparsityPattern] = {}
    for tc in d.get("test_cases", []):
        # filtration_shape comes back keyed by string grade in JSON.
        shape = {int(k): int(v) for k, v in tc.get("filtration_shape", {}).items()}
        n_s = int(tc.get("n", 0))
        w = list(tc.get("word", []))
        comp = int(tc.get("closure_components") or (closure_component_count(n_s, w) if n_s and w else 0))
        out[tc["name"]] = SparsityPattern(
            name=tc["name"],
            n_strands=n_s,
            filtration_shape=shape,
            max_grade=int(max(shape.keys()) if shape else 0),
            n_steps=int(tc.get("n_steps", 0)),
            n_hecke_relations_fired=int(tc.get("n_hecke_relations_fired", 0)),
            word=w,
            closure_components=comp,
        )
    return out


def decorate_solver_problem(
    problem: dict,
    pattern: SparsityPattern,
    *,
    enforce_strict: bool = False,
) -> dict:
    """In-place decoration of a Python SDP solver's problem dict
    with the jet-order sparsity hints.

    Adds three keys to `problem`:
        filtration_cutoff:  pattern.max_grade
        active_grades:      sorted(pattern.filtration_shape.keys())
        jet_chain_length:   pattern.n_steps

    Solvers that respect these hints can:
      - Restrict variable enumeration to T_w with `gradeOf(w) ≤ filtration_cutoff`
      - Decompose the SDP along the jet-order chain (sequential
        sub-problem solve, one grade at a time)
      - Skip Hecke-basis elements that the filtration says are zero

    `enforce_strict=True` adds a `MUST_RESPECT_FILTRATION = True`
    flag; downstream solvers are expected to fail loudly rather
    than silently ignore the hint.

    Caller's responsibility to actually consume the hints — this
    function only attaches them.
    """
    problem["jet_order_hints"] = {
        "filtration_cutoff": pattern.max_grade,
        "active_grades": sorted(pattern.filtration_shape.keys()),
        "jet_chain_length": pattern.n_steps,
        "n_strands": pattern.n_strands,
        "filtration_shape": dict(pattern.filtration_shape),
    }
    if enforce_strict:
        problem["jet_order_hints"]["MUST_RESPECT_FILTRATION"] = True
    return problem


def report(patterns: dict[str, SparsityPattern]) -> None:
    """Pretty-print the loaded sparsity patterns and their speed-up
    estimates."""
    print("=" * 90)
    print("  GB-filtration / jet-order witness reader (P6 Python fallback, PR #564)")
    print("=" * 90)
    print(f"\n  Loaded {len(patterns)} test case(s):\n")
    print(f"  {'name':<40}  {'n':>3}  {'|H_n|':>8}  "
          f"{'Σ mult':>8}  {'speedup':>8}  {'jet':>4}")
    print("  " + "-" * 86)
    for p in patterns.values():
        speedup = (
            f"×{float(p.reduction_factor):.1f}"  # float64-ok: stdout display only
            if p.filtered_basis_size > 0
            else "n/a"
        )
        print(f"  {p.name[:40]:<40}  {p.n_strands:>3}  "
              f"{p.total_basis_size:>8}  "
              f"{p.filtered_basis_size:>8}  "
              f"{speedup:>8}  {p.n_steps:>4}")


def main() -> int:
    patterns = load_jet_order_witness()
    report(patterns)

    # Demonstrate `decorate_solver_problem` round-trip on the first case.
    if patterns:
        first = next(iter(patterns.values()))
        sample_problem = {"name": "demo SDP", "variables": []}
        decorate_solver_problem(sample_problem, first, enforce_strict=False)
        print(f"\n  Demo decoration on '{first.name}':")
        print("    " + json.dumps(sample_problem["jet_order_hints"], indent=4))

    # Audit witness output
    out = {
        "computation": "gb-filtration-jet-order-reader",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "auditOnly": "AUDIT-DEEP-2026-05.md",
        "description": (
            "Python-fallback reader for the GB-filtration / jet-order "
            "witness (P6 from PR #564). Loads gb-filtration-jet-order.witness.json "
            "and exposes a SparsityPattern API + decorate_solver_problem helper "
            "for any Python SDP solver to consume the filtration cutoffs and "
            "jet-chain ordering. Rust solver wiring is held pending #565's "
            "answers on Rust solver location and F11 strict-mode scope."
        ),
        "engine": "python",
        "scriptFile": "gb_filtration_jet_order_reader.py",
        "patterns_loaded": [
            {
                "name": p.name,
                "n_strands": p.n_strands,
                "closure_components": p.closure_components,
                "max_grade": p.max_grade,
                "filtered_basis_size": p.filtered_basis_size,
                "total_basis_size": p.total_basis_size,
                "speedup_estimate": (
                    _fmt(p.reduction_factor) if p.filtered_basis_size else None
                ),
            }
            for p in patterns.values()
        ],
        "audit_reference": "AUDIT-DEEP-2026-05.md §5 P6, docs/coordination/1ppb.md",
        "pr": "#564",
    }
    _knot_rows = [
        p for p in patterns.values()
        if ("4_1" in p.name or "6_2" in p.name or p.name == "electron σ_1^3 in H_2")
    ]
    _knot_single = sum(1 for p in _knot_rows if p.closure_components == 1)
    from witness_base import WitnessBuilder
    out_path = (
        WitnessBuilder.wrap_legacy(
            "gb-filtration-jet-order-reader",
            out,
            script_path=__file__,
            engine="python",
            output_dir=HERE,
        )
        .add_assertion(
            "gb_reader_knot_named_rows_have_single_component",
            computed=str(_knot_single),
            expected=str(len(_knot_rows)),
            source="every loaded SparsityPattern naming a prime knot in H_2/H_3 "
                   "(3_1, 4_1, 6_2) has closure_components == 1 (bean qou-k3te)",
        )
        .save()
    )
    print(f"\n  Wrote {out_path.name}")
    return 0


def _selftest() -> int:
    patterns = load_jet_order_witness()
    assert len(patterns) >= 5, f"expected >=5 patterns, got {len(patterns)}"
    for p in patterns.values():
        if "4_1" in p.name or "6_2" in p.name:
            assert p.closure_components == 1, f"knot row {p.name!r} has {p.closure_components} components"
        assert "8_11" not in p.name or "not 8_11" in p.name, f"mislabelled 8_11 row: {p.name!r}"
    print(f"self-test: ok ({len(patterns)} patterns loaded, all knot-named rows have 1 component)")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:] or "--selftest" in sys.argv[1:]:
        sys.exit(_selftest())
    sys.exit(main())
