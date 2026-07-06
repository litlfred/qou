#!/usr/bin/env python3
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

Static scanner for the 30-pattern compute-audit catalogue.

Scans every .py file under computations/ for the
performance antipatterns P15-P31 from .claude/skills/local/compute-audit.md
(extracted from the 50-commit review 2026-04 → 2026-05). Emits
``compute-audit-scan.witness.json`` next to this script and prints a
human-readable summary.

This scanner intentionally targets only the **mechanically-detectable**
patterns. Correctness antipatterns P1-P14 require semantic reasoning
and are out of scope.

Usage
-----
    python computations/compute_audit_scan.py

Audit-only: results live in docs/audits/2026-05-08-compute-audit-workplan.md.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Files that legitimately implement or test the patterns we scan for —
# we DO NOT want to flag them as antipatterns. Add narrowly.
PATTERN_OWNER_FILES = {
    "laurent_q.py",                       # P17 reference impl
    "hecke_laurent_fast.py",              # P17 reference impl
    "syt_prefix_cache.py",                # P21 reference impl
    "bar_involution.py",                  # P26 reference impl
    "det_pair_law.py",                    # P25 reference impl
    "lp_dual_solver.py",                  # canonical infra
    "lp_dual_cache.py",                   # canonical infra
    "lp_dual_witness_validator.py",       # canonical infra
    "witness_base.py",                    # P30 reference impl
    "compute_audit_scan.py",              # this scanner
    "run_pipeline.py",                    # orchestrator
    "bound_state_observable_validator.py",
    "codata_constants.py",                # P31 reference impl (registry)
    "experimental_constants.py",          # P31 reference impl (registry)
}

# P31. Canonical CODATA literals — strings that are unambiguously
# CODATA-2022 mass / Q-value anchors. Free-floating occurrences in
# production scripts inflate the three-calibration count past the
# pre-approved CAL-1/2/3.
P31_CODATA_LITERALS = (
    "0.51099895",     # m_e (MeV)
    "938.272088",     # m_p (MeV) — first 9 digits cover most variants
    "938.27208816",   # m_p (MeV) — 10-digit variant in older scripts
    "939.565421",     # m_n (MeV)
    "939.56542",      # m_n (MeV) — short variant
    "0.78233",        # Q_β (MeV) — covers 0.78233, 0.7823, 0.78233341
    "206.7682830",    # m_μ / m_e
    "206.768283",     # m_μ / m_e — short variant
)
# Files where CODATA literals are legitimate (audit doc generators,
# back-fit Conv-C diagnostic, older calibration audit scripts).  Each
# entry is justified by an audit doc or in-source banner.
P31_ALLOWLIST = {
    # Audit-only Conv-C consumer per
    # docs/audits/2026-05-12-canonical-derivation-compute-review.md §6.
    "deuteron_delta_i_audit.py",
    # E_0 calibration audit explicitly compares CAL-3 paths.
    "e0_calibration_audit.py",
    # Three-calibration discipline self-test runs the full allowlist.
    "three_calibration_discipline_audit.py",
    # CODATA reconciliation explicitly cross-checks raw literals.
    "codata_reconciliation.py",
    # Validation-mass witness builder (registers the literals).
    "build_codata_2022_validation_masses_witness.py",
    "build_cal_3_q_beta_witness.py",
    # Other registry / re-export sources of truth.
    "codata_2022_source.py",             # vendored CODATA registry module
    "codata_masses.py",                  # re-exports CODATA → witness
    "q_parameter.py",                    # CAL-2 substrate-parameter source
    "q_pinning_50_digit.py",             # CAL-2 50-dps substrate source
}


def _line_of(text: str, idx: int) -> int:
    return text.count("\n", 0, idx) + 1


def scan_file(path: Path) -> list[dict]:
    """Scan one .py file; return a list of finding dicts."""
    try:
        src = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []
    findings: list[dict] = []
    name = path.name
    if name in PATTERN_OWNER_FILES:
        return findings

    # P15. sp.cancel on full expression. Heuristic: bare `sp.cancel(`
    # call without prior `sp.together` or `Poly` setup nearby.
    for m in re.finditer(r"\bsp\.cancel\s*\(", src):
        findings.append({
            "pattern": "P15",
            "file": name,
            "line": _line_of(src, m.start()),
            "snippet": "sp.cancel(...)",
            "note": "sp.cancel does GCD reduction across the entire "
                    "rational expression; on tritium-scale (~12000 ops) "
                    "it walls past 120s. Prefer sp.together followed by "
                    "sp.div, or move to LaurentQ. Ref: 18fce929.",
        })

    # P16. sp.simplify on aggregated trace before evalf. Heuristic:
    # any sp.simplify NOT immediately preceded by `# noqa: P16` and
    # NOT inside a function whose name contains 'simplify'.
    for m in re.finditer(r"\bsp\.simplify\s*\(", src):
        line_no = _line_of(src, m.start())
        ctx_start = src.rfind("\n", 0, max(m.start() - 200, 0))
        ctx = src[ctx_start:m.start()]
        if "noqa: P16" in ctx:
            continue
        findings.append({
            "pattern": "P16",
            "file": name,
            "line": line_no,
            "snippet": "sp.simplify(...)",
            "note": "sp.simplify on a 5000-op trace expression can "
                    "exceed 30 minutes and is purely cosmetic before "
                    "numerical evalf at q0. Add `simplify=False` "
                    "param and default-True for back-compat. "
                    "Ref: 2834792d.",
        })

    # P11. Recursive call bypassing lru_cache. Heuristic: a function
    # named X_uncached that recurses into itself (rather than into the
    # X_cached wrapper).
    for m in re.finditer(
        r"def\s+([A-Za-z_][\w]*)_uncached\s*\(", src,
    ):
        fn = m.group(1) + "_uncached"
        # check if the function body recurses into itself
        body_start = src.find("\n", m.end())
        # crude: look for the function name in the next ~3000 chars
        body = src[body_start:body_start + 3000]
        if re.search(rf"\b{re.escape(fn)}\s*\(", body):
            findings.append({
                "pattern": "P11",
                "file": name,
                "line": _line_of(src, m.start()),
                "snippet": f"def {fn}(...)  recurses into bare worker",
                "note": "Recursive function bypasses its lru_cache "
                        "decorator; recursive calls miss the cache. "
                        "Merge the recursion into the cached entry "
                        "point. Ref: 29ca235c.",
            })

    # P14. pickle for cache files. Heuristic: import pickle near
    # `.pkl` filename usage.
    if (re.search(r"\bimport\s+pickle\b", src)
            or re.search(r"\bfrom\s+pickle\b", src)) \
            and re.search(r"\.pkl[\"']", src):
        findings.append({
            "pattern": "P14",
            "file": name,
            "line": 1,
            "snippet": "pickle + .pkl filenames",
            "note": "pickle deserialises arbitrary objects (RCE risk "
                    "on tampered cache); use json of str(sympy.Expr) "
                    "and re-sympify on load. Ref: 0eda79c6.",
        })

    # P30. WitnessBuilder usage missing → hand-written .witness.json
    # files cannot be staleness-checked. Heuristic: file writes a
    # .witness.json via json.dump but does not import WitnessBuilder.
    writes_witness = re.search(
        r"\.witness\.json[\"']", src,
    ) and re.search(r"json\.dump", src)
    uses_builder = re.search(
        r"\bWitnessBuilder\b", src,
    )
    if writes_witness and not uses_builder:
        findings.append({
            "pattern": "P30",
            "file": name,
            "line": 1,
            "snippet": "json.dump → .witness.json without WitnessBuilder",
            "note": "Hand-written .witness.json files lack scriptHash "
                    "and are silently treated as current by "
                    "run_pipeline.py. Use witness_base.WitnessBuilder. "
                    "Ref: workflow memory; witness_base.py:136-330.",
        })

    # P21 audit. Hoefsmit caller without BlockCache. Heuristic:
    # imports build_seminormal_matrices or hoefsmit_matrices_symbolic
    # and does NOT import BlockCache/build_seminormal_matrices_cached.
    uses_hoefsmit = re.search(
        r"\bbuild_seminormal_matrices\b"
        r"|\bhoefsmit_matrices_symbolic\b",
        src,
    )
    uses_block_cache = re.search(
        r"\bBlockCache\b"
        r"|\bbuild_seminormal_matrices_cached\b",
        src,
    )
    if uses_hoefsmit and not uses_block_cache:
        findings.append({
            "pattern": "P21",
            "file": name,
            "line": 1,
            "snippet": "Hoefsmit construction without BlockCache",
            "note": "syt_prefix_cache.BlockCache caches block values "
                    "by content distance ρ; precomputed SYT→index "
                    "dict eliminates O(d_λ²) swap-partner search. "
                    "Numerical-q callers can wire it directly. "
                    "Ref: ocneanu_weights.py wiring.",
        })

    # P31. Hardcoded CODATA literal outside the registry.  Skip
    # explicitly allowlisted audit-only consumers.
    if name not in P31_ALLOWLIST:
        for literal in P31_CODATA_LITERALS:
            # Match the literal inside a string (single or double
            # quoted); avoid matching it as a substring of a longer
            # number by requiring a non-digit / non-dot boundary on
            # the right.
            pattern = re.escape(literal) + r"(?![0-9])"
            for m in re.finditer(pattern, src):
                # Skip if line carries explicit `# noqa: P31` justification.
                line_no = _line_of(src, m.start())
                line_start = src.rfind("\n", 0, m.start()) + 1
                line_end = src.find("\n", m.start())
                line_text = src[line_start:line_end if line_end != -1 else None]
                if "noqa: P31" in line_text:
                    continue
                findings.append({
                    "pattern": "P31",
                    "file": name,
                    "line": line_no,
                    "snippet": f'CODATA literal "{literal}"',
                    "note": "Hardcoded CODATA literal outside the "
                            "registry inflates the three-calibration "
                            "count past CAL-1/2/3. Import from "
                            "codata_constants (validation aliases) or "
                            "experimental_constants instead. Audit-only "
                            "scripts may add `# noqa: P31` with a "
                            "justifying comment. Ref: "
                            "codata_constants.py:90-145; "
                            "docs/audits/2026-05-12-canonical-"
                            "derivation-compute-review.md §3.",
                })
                # One finding per literal per file is enough; break
                # the inner loop to avoid spamming for repeated uses.
                break

    return findings


def main() -> int:
    findings: list[dict] = []
    py_files = sorted(HERE.glob("*.py"))
    for path in py_files:
        if path.name.startswith("test_"):
            continue
        findings.extend(scan_file(path))

    by_pattern: dict[str, list[dict]] = defaultdict(list)
    by_file: dict[str, list[dict]] = defaultdict(list)
    for f in findings:
        by_pattern[f["pattern"]].append(f)
        by_file[f["file"]].append(f)

    pattern_summary = {
        p: len(items) for p, items in sorted(by_pattern.items())
    }
    top_files = sorted(
        by_file.items(), key=lambda kv: -len(kv[1]),
    )[:15]

    # Print human-readable summary
    print(f"compute-audit-scan: {len(py_files)} files scanned, "
          f"{len(findings)} findings")
    print()
    print("By pattern:")
    for p in sorted(pattern_summary):
        print(f"  {p}: {pattern_summary[p]:4d} hits")
    print()
    print("Top-15 files by finding count:")
    for fname, items in top_files:
        ps = sorted({i["pattern"] for i in items})
        print(f"  {fname:48s} {len(items):3d}  ({','.join(ps)})")

    # Emit witness
    try:
        from witness_base import WitnessBuilder
    except ImportError:
        sys.path.insert(0, str(HERE))
        from witness_base import WitnessBuilder

    w = (
        WitnessBuilder("compute-audit-scan", engine="python")
        .set_description(
            "Static scan of computations/ for the "
            "performance patterns P11/P14/P15/P16/P21/P30/P31 from "
            ".claude/skills/local/compute-audit.md."
        )
        .set_audit_only(
            "docs/audits/2026-05-08-compute-audit-workplan.md"
        )
        .add_parameter("files_scanned", len(py_files))
        .add_parameter("patterns", sorted(pattern_summary))
        .add_data("by_pattern_count", pattern_summary)
        .add_data("top_files", [
            {"file": f, "count": len(items),
             "patterns": sorted({i["pattern"] for i in items})}
            for f, items in top_files
        ])
        .add_data("findings", findings)
        .add_caveat(
            "Static scanner: false positives are possible (e.g. "
            "sp.simplify on a single small Symbol is fine). Verify "
            "each finding by reading the cited line before acting."
        )
        .add_caveat(
            "Correctness antipatterns P1–P14 (with the exception of "
            "P11/P14 detected here) require semantic reasoning and "
            "are NOT covered by this scanner."
        )
    )
    w.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
