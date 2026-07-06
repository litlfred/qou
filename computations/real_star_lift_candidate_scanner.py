#!/usr/bin/env python3
"""Scan QOU Lean files for substrate-lift candidates.

A "substrate-lift candidate" is a .lean file whose declarations are
currently specialized to (q : ℝ) (hq : 1 < q) or similar, but whose
proof body uses NO archimedean tactic — no Real.sqrt, no Real.rpow,
no Real.cos/sin/cosh/exp/log/pi, no linarith / norm_num on q's
ordering, no CODATA value comparison. Such files are eligible to be
refactored to the generic ground ring R per AGENTS.md §7c:

    (q : ℝ) (hq : 1 < q)
      ↓
    {R : Type*} [Field R] (q : R) (hq : IsUnit q)
      OR
    {R : Type*} [NormedField R] (q : R) (hq : 1 < ‖q‖)

This is the operational realization of the §7c base-ring discipline
audited in docs/audits/2026-05-24-real-star-lift-inventory.md.

OUTPUT: real-star-lift-candidates.witness.json — a per-file
classification (CANDIDATE / ARCHIMEDEAN / ALREADY_GENERIC) with the
matched archimedean-tactic evidence for each non-candidate.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402

# Archimedean-tactic patterns. Any match makes a file ARCHIMEDEAN.
ARCHIMEDEAN_PATTERNS = [
    (r"\bReal\.sqrt\b", "Real.sqrt"),
    (r"\bReal\.rpow\b", "Real.rpow"),
    (r"\bReal\.cos\b", "Real.cos"),
    (r"\bReal\.sin\b", "Real.sin"),
    (r"\bReal\.cosh\b", "Real.cosh"),
    (r"\bReal\.sinh\b", "Real.sinh"),
    (r"\bReal\.tanh\b", "Real.tanh"),
    (r"\bReal\.exp\b", "Real.exp"),
    (r"\bReal\.log\b", "Real.log"),
    (r"\bReal\.pi\b", "Real.pi"),
    # CODATA literals (representative — not exhaustive)
    (r"0\.5109989\d*", "CODATA m_e literal"),
    (r"938\.272\d*", "CODATA m_p literal"),
    (r"939\.565\d*", "CODATA m_n literal"),
    (r"206\.7682\d*", "CODATA m_μ/m_e literal"),
    (r"1\.109978\d*", "q_0 numerical pin literal"),
]

# Substrate-specialization signature pattern: declarations typed
# `(q : ℝ)` with a strict-ordering hypothesis. We do not require
# `(hq : 1 < q)` literally — `0 < q`, `q > 0`, etc. all count.
REAL_Q_SIG = re.compile(r"\(\s*q\s*:\s*ℝ\s*\)")

# Generic-R signatures (already §7c-compliant). If a file has these
# AND no `(q : ℝ)` signature, it's ALREADY_GENERIC.
GENERIC_R_SIG = re.compile(r"\{\s*R\s*:\s*Type\*?\s*\}")


def classify_file(content: str) -> tuple[str, list[str]]:
    """Return (verdict, evidence) for a single .lean file's content."""
    archimedean_hits = []
    for pattern, name in ARCHIMEDEAN_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            archimedean_hits.append(f"{name} ×{len(matches)}")

    has_real_q = bool(REAL_Q_SIG.search(content))
    has_generic_r = bool(GENERIC_R_SIG.search(content))

    if archimedean_hits:
        return ("ARCHIMEDEAN", archimedean_hits)
    if has_real_q and not has_generic_r:
        # ℝ-specialized but no archimedean tactic → CANDIDATE
        return ("CANDIDATE", [])
    if has_real_q and has_generic_r:
        # Mixed: some decls generic, some real-specialized → MIXED
        return ("MIXED", [])
    if has_generic_r and not has_real_q:
        return ("ALREADY_GENERIC", [])
    # No q : ℝ and no {R : Type*} — typically a Mathlib glue file
    return ("OTHER", [])


def main() -> int:
    qou_root = Path(__file__).resolve().parents[2]
    lean_dirs = [
        qou_root / "content" / "quantum-observable-universe",
    ]

    scanned: dict[str, tuple[str, list[str]]] = {}
    for d in lean_dirs:
        for lean_file in sorted(d.rglob("*.lean")):
            try:
                text = lean_file.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            rel = str(lean_file.relative_to(qou_root))
            scanned[rel] = classify_file(text)

    candidates = [p for p, (v, _) in scanned.items() if v == "CANDIDATE"]
    archimedean = [p for p, (v, _) in scanned.items() if v == "ARCHIMEDEAN"]
    mixed = [p for p, (v, _) in scanned.items() if v == "MIXED"]
    already_generic = [p for p, (v, _) in scanned.items() if v == "ALREADY_GENERIC"]
    other = [p for p, (v, _) in scanned.items() if v == "OTHER"]

    print(f"Scanned {len(scanned)} .lean files:")
    print(f"  CANDIDATE       (lift-eligible):     {len(candidates)}")
    print(f"  ALREADY_GENERIC (§7c-compliant):     {len(already_generic)}")
    print(f"  MIXED (some decls generic, some ℝ):  {len(mixed)}")
    print(f"  ARCHIMEDEAN (genuinely needs ℝ):     {len(archimedean)}")
    print(f"  OTHER (no q : ℝ, no {{R : Type*}}):   {len(other)}")
    print()
    print(f"Top 10 CANDIDATE files (lift-eligible per §7c):")
    for f in candidates[:10]:
        print(f"  - {f}")

    w = WitnessBuilder(
        "real-star-lift-candidates",
        engine="real_star_lift_candidate_scanner.py",
    )
    w.set_description(
        "Per-file inventory of QOU Lean files classified by lift "
        "eligibility under AGENTS.md §7c base-ring discipline. "
        "CANDIDATE = ℝ-specialized signature `(q : ℝ)` present, "
        "but no archimedean tactic in the file body (Real.sqrt, "
        "Real.rpow, Real.cos/sin/cosh/exp/log/pi, CODATA literals). "
        "Such files can be refactored to `{R : Type*} [Field R] "
        "(q : R) (hq : IsUnit q)` or `[NormedField R] (hq : 1 < ‖q‖)`. "
        "ARCHIMEDEAN = at least one archimedean tactic present; the "
        "evidence list records which. ALREADY_GENERIC = §7c-compliant "
        "already. MIXED = both signatures present (refactor on a "
        "per-declaration basis). OTHER = no q-parameter at all."
    )
    w.set_content_block("prop:q-zero-complex-extension")
    w.set_audit_only(
        "docs/audits/2026-05-24-real-star-lift-inventory.md"
    )

    w.add_parameter("scanner_version", "1.0")
    w.add_parameter("scanned_root", "content/quantum-observable-universe")
    w.add_parameter(
        "archimedean_patterns",
        [name for _, name in ARCHIMEDEAN_PATTERNS],
    )

    w.add_data("total_files_scanned", len(scanned))
    w.add_data("counts", {
        "CANDIDATE": len(candidates),
        "ALREADY_GENERIC": len(already_generic),
        "MIXED": len(mixed),
        "ARCHIMEDEAN": len(archimedean),
        "OTHER": len(other),
    })
    w.add_data("candidate_files", candidates)
    w.add_data("already_generic_files", already_generic)
    w.add_data("mixed_files", mixed)
    # Cap archimedean evidence at 50 files to keep witness manageable
    w.add_data(
        "archimedean_files_sample",
        [
            {"file": p, "evidence": scanned[p][1]}
            for p in archimedean[:50]
        ],
    )
    w.add_data(
        "archimedean_files_count_total",
        len(archimedean),
    )

    w.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
