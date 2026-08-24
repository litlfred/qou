#!/usr/bin/env python3
"""I14 audit — witness provenance completeness.

Every `computations/*.witness.json` MUST declare:

  - `engine` (e.g. "mpmath", "python+snappy", "rust+mpmath",
    "markov_peel+mpmath") — what produced the value.
  - `scriptFile` (e.g. "canonical_mass_table_extended.py") — the
    Python entry point that emitted the witness.
  - `commitSha` (40-char git SHA) — repo HEAD at emission time.

Witnesses without these three fields cannot be reproduced or
traced back to source code. Historical pattern: hand-edited JSON
output (predating `WitnessBuilder`) produced ~18 witnesses with
null provenance, including `canonical-mass-table.witness.json`
(orphan), `atomic-braid-mass-table.witness.json` (off-main),
`mass-table-ppb.witness.json` (pre-fix), and ~15 chi-cache /
A-operator artifacts.

This audit categorizes each witness as:

  PROV_OK              all three fields present and non-null
  PROV_MISSING         at least one of the three fields null/absent
  PROV_AUDIT_EXEMPT    name matches `*-audit.witness.json` /
                       `*-scan.witness.json` /
                       `*-compliance.witness.json` (state-tracking
                       outputs whose convention does not require
                       provenance; their refresh IS the signal)

Witnesses listed in `methodology-deprecation.witness.json` under
`removed_legacy_compute_artifacts.removed_witnesses` are skipped
(they were deleted by design).

CLI:
    python3 witness_provenance_audit.py            # report mode
    python3 witness_provenance_audit.py --strict   # exit 1 on any PROV_MISSING

Emits `witness-provenance-audit.witness.json`.

Per repo-owner directive 2026-05-19: "fix all of these tables so
they always have correct witnessed data from canonical pipeline.
too much divergence." This audit operationalises the structural
half of that directive — provenance completeness is the
machine-checkable condition for "correct witnessed data".
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
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
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from mpmath import mpf  # noqa: E402


REQUIRED_FIELDS = ("engine", "scriptFile", "commitSha")

# Glob suffixes — audit witnesses are state-tracking outputs whose
# refresh IS the signal, not a regression. They are exempt from
# provenance-completeness checks (though most do carry the fields
# anyway via WitnessBuilder).
AUDIT_SUFFIXES = (
    "-audit.witness.json",
    "-scan.witness.json",
    "-compliance.witness.json",
)


def load_legacy_removed_set() -> set[str]:
    """Witness names removed via methodology-deprecation."""
    path = _pb.witness_path("methodology-deprecation.witness.json", HERE)
    if not path.exists():
        return set()
    try:
        d = json.loads(path.read_text())
    except json.JSONDecodeError:
        return set()
    removed = d.get("removed_legacy_compute_artifacts", {})
    listed = removed.get("removed_witnesses", []) or []
    out: set[str] = set()
    for entry in listed:
        # entries are free-text "name (note)" — extract leading filename.
        if isinstance(entry, str):
            name = entry.split(" ")[0].strip()
            if name.endswith(".witness.json") or name.endswith(".derivation.json"):
                out.add(name)
    return out


def _is_prose(value: str) -> bool:
    """True when a provenance field holds an EXPLANATION rather than a value.

    Seven witnesses carry `scriptFile` values like
    "(legacy - no matching producer found; provenance pending manual triage)".
    That string is truthy, so the old `not body.get(f)` emptiness test scored
    them PROV_OK: the I14 campaign (f893cc92, 2026-05-19) reached
    `prov_missing: 0` / `completeness_ratio: 1.00` partly by WRITING THIS
    MARKER, and the gate that should have noticed went green. The marker
    itself is honest -- it says exactly what is wrong, and the 2026-08-19
    triage found these witnesses by it. The defect is counting it as present.

    A field whose value says "we do not know" is missing provenance, not
    provenance. Two of the seven now back paper-facing claims
    (`4he-binding-full-pipeline` -> `content/values/registry.ts`;
    `hecke-core-symbolic-migration` -> two appendix blocks at
    `status: "verified"`), which is what this check exists to surface.

    Same predicate shape as `witness_producer_executes_audit.is_prose`, kept
    in sync deliberately: two different answers to "is this a real producer
    reference?" is how the wrong one gets acted on.

    A witness that genuinely cannot carry a producer belongs on the
    acknowledged floor (provenance-acknowledged-floor.json) with an
    investigated reason -- NOT behind a truthy marker string.
    """
    v = value.strip()
    if v.startswith("("):
        return True
    if len(v) > 120:
        return True
    return "/" not in v and not Path(v).suffix and " " in v


#: Provenance fields that are supposed to hold a FILE REFERENCE. The prose
#: check applies to these only. `engine` is free text by design -- values like
#: "sympy + pyhecke_native" or "mpmath (witness-fed; no new tr_M compute)" are
#: informative, not evasive -- and running the predicate over it flagged 49 of
#: them, which would have manufactured false PROV_MISSING and dropped the
#: completeness ratio on noise. Measured before shipping: of the 50 values the
#: unrestricted check caught, 49 were `engine` descriptions and 7 were the real
#: `scriptFile` markers. `commitSha` wants a sha-shaped check, not this one.
PATH_VALUED_FIELDS = ("scriptFile",)


def _has_provenance(body: dict, field: str) -> bool:
    """A provenance field counts as present only if it carries a real value."""
    v = body.get(field)
    if not v:
        return False
    if field in PATH_VALUED_FIELDS and isinstance(v, str) and _is_prose(v):
        return False
    return True


def classify(path: Path) -> tuple[str, list[str]]:
    """Return (verdict, missing_fields) for a single witness file."""
    if any(path.name.endswith(suf) for suf in AUDIT_SUFFIXES):
        return "PROV_AUDIT_EXEMPT", []
    try:
        body = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        return "PROV_PARSE_ERROR", [str(exc)]
    if not isinstance(body, dict):
        return "PROV_PARSE_ERROR", ["root is not an object"]
    missing = [f for f in REQUIRED_FIELDS if not _has_provenance(body, f)]
    return ("PROV_MISSING" if missing else "PROV_OK"), missing


def load_acknowledged_floor() -> "dict[str, str]":
    """Load-bearing witnesses that cannot carry a producer-backed provenance
    triple, each with an investigated reason (hand-authored by design, or a
    legacy artifact whose producer was removed). Returns {witness_name: reason}.
    These are classified PROV_EXEMPT_ACKNOWLEDGED — on the record, never
    re-chased. See provenance-acknowledged-floor.json for the discipline (a
    reason from a completed investigation is required; not a silencing list)."""
    path = HERE / "provenance-acknowledged-floor.json"
    if not path.exists():
        return {}
    try:
        d = json.loads(path.read_text())
    except json.JSONDecodeError:
        return {}
    return {e["witness"]: e.get("reason", "")
            for e in d.get("acknowledged", []) if e.get("witness")}


def build_reference_index() -> tuple[set[str], "dict[str, int]"]:
    """Return (paper_referenced_names, py_mention_counts).

    A witness's provenance only matters if something depends on it. This indexes
    two cheap single-pass greps: witness names cited under `content/` (the paper),
    and how many `.py` files mention each witness name. A witness that is cited by
    NO content block and mentioned by ≤1 `.py` (only its own producer) has no
    reader — a missing provenance triple on it is not a real gap, so it is exempted
    (PROV_EXEMPT_NO_READER) rather than counted as PROV_MISSING. Owner directive
    2026-07-18: don't chase provenance on caches/dead-ends nothing consumes.
    """
    import re
    import subprocess
    from collections import Counter

    repo = HERE.parent.parent
    pat = r"[a-z0-9][a-z0-9._-]*\.witness\.json"
    paper: set[str] = set()
    try:
        out = subprocess.run(
            ["grep", "-rhoE", pat, str(repo / "content")],
            capture_output=True, text=True, timeout=120,
        ).stdout
        paper = set(out.split())
    except Exception:  # noqa: BLE001
        pass
    py_counts: "dict[str, int]" = {}
    try:
        out = subprocess.run(
            ["grep", "-rhoE", "--include=*.py", pat, str(HERE.parent)],
            capture_output=True, text=True, timeout=120,
        ).stdout
        py_counts = dict(Counter(out.split()))
    except Exception:  # noqa: BLE001
        pass
    return paper, py_counts


def has_reader(name: str, paper: set[str], py_counts: "dict[str, int]") -> bool:
    """A witness has a reader if the paper cites it or a non-producer `.py`
    mentions it (>1 `.py` mention ⇒ something beyond the producer reads it)."""
    return name in paper or py_counts.get(name, 0) > 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict", action="store_true",
        help="Exit 1 if any PROV_MISSING witnesses are found (CI gate).",
    )
    args = parser.parse_args(argv)

    legacy_removed = load_legacy_removed_set()
    acknowledged_floor = load_acknowledged_floor()
    paper_refs, py_counts = build_reference_index()
    by_verdict: dict[str, list[dict]] = {
        "PROV_OK": [], "PROV_MISSING": [],
        "PROV_AUDIT_EXEMPT": [], "PROV_EXEMPT_NO_READER": [],
        "PROV_EXEMPT_ACKNOWLEDGED": [], "PROV_PARSE_ERROR": [],
    }
    # Scan the whole compute tree's witnesses (reorg scan-root fix).
    for wp in sorted((HERE.parent).rglob("*.witness.json")):
        if "_deprecated" in wp.parts:
            continue
        if wp.name in legacy_removed:
            continue
        verdict, missing = classify(wp)
        # A missing triple on a witness nothing consumes is not a real gap
        # (owner directive 2026-07-18): exempt no-reader witnesses.
        if verdict == "PROV_MISSING" and not has_reader(wp.name, paper_refs, py_counts):
            verdict, missing = "PROV_EXEMPT_NO_READER", missing
        # Investigated, documented floor: load-bearing but no attributable
        # producer (hand-authored / legacy orphan). On the record, not a gap.
        elif verdict == "PROV_MISSING" and wp.name in acknowledged_floor:
            verdict, missing = "PROV_EXEMPT_ACKNOWLEDGED", [acknowledged_floor[wp.name]]
        by_verdict[verdict].append(
            {"witness": wp.name, "missing_fields": missing}
        )

    n_total = sum(len(v) for v in by_verdict.values())
    n_ok = len(by_verdict["PROV_OK"])
    n_missing = len(by_verdict["PROV_MISSING"])
    n_audit = len(by_verdict["PROV_AUDIT_EXEMPT"])
    n_no_reader = len(by_verdict["PROV_EXEMPT_NO_READER"])
    n_ack = len(by_verdict["PROV_EXEMPT_ACKNOWLEDGED"])
    n_parse_err = len(by_verdict["PROV_PARSE_ERROR"])
    # Carry the ratio as mpmath.mpf and serialize with `_precision.fmt`.
    # A bare Python `/` here produces a float64, which the raw-float64 ratchet
    # correctly flags on this audit's OWN witness (`.data.counts
    # .completeness_ratio`) — a provenance auditor tripping a precision gate on
    # its own output. The quantity is an exact rational (a ratio of counts), so
    # there is nothing to lose by carrying it exactly to the serializer.
    set_compute_dps()
    n_clean = n_ok + n_audit + n_no_reader + n_ack
    completeness_ratio = mpf(n_clean) / mpf(n_total) if n_total > 0 else mpf(0)

    print("=" * 70)
    print("I14 audit — witness provenance completeness")
    print("=" * 70)
    print(f"  total scanned          : {n_total}")
    print(f"  PROV_OK                : {n_ok}")
    print(f"  PROV_AUDIT_EXEMPT      : {n_audit}")
    print(f"  PROV_EXEMPT_NO_READER  : {n_no_reader}")
    print(f"  PROV_EXEMPT_ACKNOWLEDGED: {n_ack}")
    print(f"  PROV_MISSING           : {n_missing}")
    print(f"  PROV_PARSE_ERROR       : {n_parse_err}")
    print(f"  completeness ratio     : {float(completeness_ratio):.3f}")
    print(f"  legacy_removed_skipped: {len(legacy_removed)}")
    if n_missing:
        print()
        print("PROV_MISSING witnesses (need WitnessBuilder migration "
              "or removal):")
        for r in by_verdict["PROV_MISSING"][:25]:
            print(f"  - {r['witness']}: missing {r['missing_fields']}")
        if n_missing > 25:
            print(f"  ... (+ {n_missing - 25} more)")

    builder = (
        WitnessBuilder("witness-provenance-audit", engine="python")
        .set_description(
            "I14 audit per repo-owner directive 2026-05-19: every "
            "witness JSON must declare engine, scriptFile, commitSha "
            "(WitnessBuilder convention) so it can be reproduced and "
            "traced. Witnesses ending in -audit/-scan/-compliance "
            "are exempt by glob (state-tracking outputs). Files "
            "listed under methodology-deprecation's "
            "removed_legacy_compute_artifacts.removed_witnesses are "
            "skipped (deleted by design)."
        )
        .add_parameter("required_fields", list(REQUIRED_FIELDS))
        .add_parameter("audit_suffixes", list(AUDIT_SUFFIXES))
        .add_parameter("legacy_removed_count", len(legacy_removed))
        .add_data("counts", {
            "total_scanned": n_total,
            "prov_ok": n_ok,
            "prov_audit_exempt": n_audit,
            "prov_exempt_no_reader": n_no_reader,
            "prov_exempt_acknowledged": n_ack,
            "prov_missing": n_missing,
            "prov_parse_error": n_parse_err,
            "completeness_ratio": fmt(completeness_ratio),
        })
        .add_data("by_verdict", by_verdict)
        .add_assertion(
            "no_missing_provenance",
            computed=n_missing,
            expected=0,
            tolerance=0,
            source="every witness must declare engine/scriptFile/commitSha",
        )
    )
    out = builder.save()
    print()
    print(f"Witness: {out}")

    if args.strict and n_missing > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
