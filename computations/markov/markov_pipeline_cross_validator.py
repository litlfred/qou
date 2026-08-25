#!/usr/bin/env python3
"""
Markov pipeline cross-validator — verify archimedean tr_M(q_0)
agreement across independent producers.

The QOU computation pipeline arrives at the archimedean Markov
trace value `tr_M(q_0)` from at least two independent paths:

1. **Polynomial-ring evaluation** — the path used by
   `markov_substrate_realizer.py`: take the Habiro-completion
   polynomial `p_in_u(u) ∈ ℤ[u]` from
   `habiro-coefficients-atomic.witness.json`, evaluate at
   `u_0 = q_0^{1/2}`, and divide by `denom_in_u(u_0)`.

2. **Mittag-Leffler full pole sum** — the path used by
   `term6_full_pole_sum.py` (currently on
   `claude/continue-pr-442-DJRWm`, expected to land on main as
   `term6-full-pole-sum.witness.json`): record
   `tr_M_at_q0_polynomial` per atom as part of the residue audit.

Both should agree at high precision.  This script forms a
cross-pipeline witness that the polynomial-ring realization
(Lean `MotivicSubstrate.realize Place.infty`) is consistent with
the residue-spectral-sum computation (Lean
`prop:gb-residue-spectral-sum`).

The check is **forward-compatible**: if the term6 witness is not
yet on main (e.g. 442 still open), the script reports SKIP and
exits 0.  Once 442 merges, a green run is direct empirical evidence
for both Lean propositions on the existing witness data.
"""

from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent))
from mpmath import mp  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


HERE = Path(__file__).parent
REALIZER_WITNESS = _pb.witness_path("markov-substrate-realization.witness.json", HERE)
TERM6_FULL_WITNESS = _pb.witness_path("term6-full-pole-sum.witness.json", HERE)
OUTPUT_WITNESS = _pb.witness_path("markov-pipeline-cross-validation.witness.json", HERE)

# A STRING, not a float literal: the comparison below is mpf end to end, and a
# Python float here is the one place a float64 could re-enter the numeric path.
AGREEMENT_RTOL = "1e-9"


def load_realizer() -> Optional[dict]:
    if not REALIZER_WITNESS.exists():
        return None
    with REALIZER_WITNESS.open() as f:
        return json.load(f)


def load_term6_full() -> Optional[dict]:
    if not TERM6_FULL_WITNESS.exists():
        return None
    with TERM6_FULL_WITNESS.open() as f:
        return json.load(f)


def realizer_archimedean_by_atom(realizer_data: dict) -> dict[str, mp.mpf]:
    """Extract per-atom archimedean tr_M(q_0) values.

    The realizer emits results under the WitnessBuilder `data.results`
    field; older revisions stored them at the top level under `results`.
    Look in both places to stay forward- and backward-compatible.
    """
    by_atom: dict[str, float] = {}
    nested = realizer_data.get("data", {}).get("results")
    legacy = realizer_data.get("results")
    atom_records = nested if nested is not None else (legacy or [])
    for atom_record in atom_records:
        atom = atom_record["atom"]
        for rz in atom_record.get("realizations", []):
            if rz.get("place") == "infty" and "tr_M_at_q0" in rz:
                by_atom[atom] = mp.mpf(str(rz["tr_M_at_q0"]))
                break
    return by_atom


def term6_archimedean_by_atom(term6_data: dict) -> dict[str, float]:
    by_atom: dict[str, float] = {}
    for atom_record in term6_data.get("data", {}).get("atoms", []):
        atom = atom_record.get("atom")
        if atom and "tr_M_at_q0_polynomial" in atom_record:
            by_atom[atom] = mp.mpf(str(atom_record["tr_M_at_q0_polynomial"]))
    return by_atom


def compare_value(label: str, x: mp.mpf, y: mp.mpf, rtol: str) -> dict:
    """Relative-tolerance comparison; returns a per-atom check.

    The denominator `max(abs(x), abs(y))` is non-zero whenever
    either value is non-zero, so the single branch handles all
    one-sided-zero cases correctly (rel_diff = 1.0, i.e. 100% off).
    Only the both-zero case needs special-casing to avoid
    division-by-zero.

    PRECISION (2026-08-23, bean `qou-bm4i`). `x` and `y` used to be `float`,
    cast at load. That put an `rtol = 1e-9` comparison on values truncated to
    ~1e-16 while both source witnesses advertise `output_dps: 60` — the
    comparison could not resolve better than seven orders inside its own
    tolerance. `mpf` end to end now, and the serialized fields carry the full
    width rather than a float64 shadow of it.
    """
    if x == 0 and y == 0:
        agree = True
        rel = mp.mpf(0)
    else:
        rel = abs(x - y) / max(abs(x), abs(y))
        agree = rel <= mp.mpf(rtol)
    return {
        "atom": label,
        "realizer_value": fmt(x),
        "term6_value": fmt(y),
        "abs_diff": fmt(abs(x - y)),
        "rel_diff": fmt(rel),
        "agree": bool(agree),
    }


def main() -> int:
    # `_precision` does not set mp.dps on import; without this the mpf
    # path below runs at mpmath's default 15 and the fix is cosmetic.
    set_compute_dps()
    realizer_data = load_realizer()
    if realizer_data is None:
        print(
            f"realizer witness missing at {REALIZER_WITNESS}; "
            "run markov_substrate_realizer.py first.",
            file=sys.stderr,
        )
        return 1

    term6_data = load_term6_full()
    realizer_arch = realizer_archimedean_by_atom(realizer_data)

    if term6_data is None:
        # SKIP path: don't write a witness — absence of file means
        # "not yet generated", which lets run_pipeline.py and human
        # readers detect that the cross-validation is pending.  When
        # the term6 witness lands, this script will produce a real
        # PASS/FAIL witness with full WitnessBuilder metadata.
        if OUTPUT_WITNESS.exists():
            OUTPUT_WITNESS.unlink()
        print(
            f"markov_pipeline_cross_validator: SKIP "
            f"({TERM6_FULL_WITNESS.name} not present)"
        )
        print(f"  realizer has {len(realizer_arch)} atoms with archimedean values:")
        for a, v in realizer_arch.items():
            print(f"    {a:>24}  tr_M(q_0) = {v:.10f}")
        print(
            "  no witness written — re-run after term6 lands to "
            "produce the cross-validation certificate."
        )
        return 0

    term6_arch = term6_archimedean_by_atom(term6_data)

    # Compare on the intersection of atom labels; flag missing atoms.
    common = sorted(set(realizer_arch) & set(term6_arch))
    only_in_realizer = sorted(set(realizer_arch) - set(term6_arch))
    only_in_term6 = sorted(set(term6_arch) - set(realizer_arch))

    checks = [
        compare_value(atom, realizer_arch[atom], term6_arch[atom], AGREEMENT_RTOL)
        for atom in common
    ]

    w = WitnessBuilder("markov-pipeline-cross-validation", engine="python")
    w.set_description(
        "Verifies archimedean tr_M(q_0) agreement between the polynomial-"
        "ring realization (markov_substrate_realizer.py) and the "
        "Mittag-Leffler full-pole-sum computation (term6_full_pole_sum.py)."
    )
    w.set_content_block("prop:full-pole-structure-mass-trace")
    w.add_parameter("agreement_rtol", fmt(mp.mpf(AGREEMENT_RTOL)))
    w.add_data("reference_blocks", [
        "prop:full-pole-structure-mass-trace",
        "prop:gb-residue-spectral-sum",
        "def:motivic-substrate",
    ])
    w.add_data("lean_classes", [
        "qou:QOU.AlgebraicSubstrate.MotivicSubstrate",
        "qou:QOU.BraidKnot.HabiroCompletion",
    ])
    w.add_data("checks", checks)
    w.add_data("atoms_only_in_realizer", only_in_realizer)
    w.add_data("atoms_only_in_term6", only_in_term6)

    for c in checks:
        w.add_assertion(
            f"tr_M_at_q0_archimedean[{c['atom']}]",
            computed=c["realizer_value"],
            expected=c["term6_value"],
            tolerance=fmt(mp.mpf(AGREEMENT_RTOL)
                          * max(abs(mp.mpf(c["realizer_value"])),
                                abs(mp.mpf(c["term6_value"])))),
        )

    # Asymmetric coverage is a failure: a PASS witness must require
    # both pipelines to cover the same atom set, and the empty-
    # intersection case must not vacuously pass.
    w.add_assertion(
        "no_atoms_only_in_realizer",
        computed=len(only_in_realizer),
        expected=0,
    )
    w.add_assertion(
        "no_atoms_only_in_term6",
        computed=len(only_in_term6),
        expected=0,
    )
    # `atom_intersection_size` passes iff there is at least one common
    # atom (max(n, 1) == n only when n ≥ 1); avoids a vacuous PASS.
    w.add_assertion(
        "atom_intersection_size",
        computed=len(common),
        expected=max(len(common), 1),
    )

    overall_pass = all(a.passed for a in w.assertions)
    w.save()

    status = "PASS" if overall_pass else "FAIL"
    print(f"markov_pipeline_cross_validator: {status}")
    for c in checks:
        marker = "✓" if c["agree"] else "✗"
        print(
            # These are 60-digit `fmt` strings now, not floats; re-parse for display.
            f"  {marker} {c['atom']:>24}  realizer={mp.mpf(c['realizer_value']):.10f}  "
            f"term6={mp.mpf(c['term6_value']):.10f}  rel_diff={mp.mpf(c['rel_diff']):.2e}"
        )
    if only_in_realizer or only_in_term6:
        print(f"  asymmetric atom coverage: realizer-only={only_in_realizer}, term6-only={only_in_term6}")
    return 0 if overall_pass else 2


if __name__ == "__main__":
    sys.exit(main())
