#!/usr/bin/env python3
"""paper_modulus_audit_nonarchimedean.py — full paper audit of |...|
usage in non-archimedean (categorical / pre-τ / fibre-level) sections.

Per user 2026-06-01: "more general statements (even if char p) should be
in paper, and then specialize when needed for archimedean."

Per prop:li2q-phiq-bar-symmetrization + AGENTS.md fibre/observable
distinction (PR #1616): the |...| modulus is an ARCHIMEDEAN operation
(takes a signed real to a positive real, breaking bar-asymmetry). It
should NOT appear in categorical / pre-τ definitions.

AUDIT SCOPE: all .md files under content/quantum-observable-universe/
that contain absolute-value notation (\\|...\\|, \\lvert...\\rvert, or
literal |...|) AROUND tr_M, tr, χ, or other categorical objects.

CLASSIFICATION:
  A. ARCHIMEDEAN-OK — the |...| appears in an explicitly archimedean
     section (e.g., "At q_0", "MeV", "numerical evaluation", "post-τ").
  B. NON-ARCHIMEDEAN MISUSE — the |...| appears in a categorical /
     algebraic / pre-τ context (definition, theorem, conjecture body).
  C. AMBIGUOUS — context not clear from local text; needs human review.

OUTPUT: enumerated by directory + classification, witness JSON with
per-file site list.

NOTE: this is an AUDIT, not a refactor. The refactor (removing |...|
from non-archimedean sections, replacing with signed tr_M + adding
archimedean-specialization clauses) is a substantial paper-wide
edit out of scope for one session.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
# Repo root by LANDMARK SEARCH, not by counting `.parent`s: the fixed
# count was off by one and resolved OUTSIDE the repo, so this bootstrap
# never fired -- masked because `_path_bridge`/PYTHONPATH already supplies
# the same directory in every in-repo run. Bean qou-rug0.
_QOU_REPO_ROOT = next(
    (_a for _a in Path(__file__).resolve().parents
     if (_a / "tools").is_dir() and (_a / "computations").is_dir()),
    Path(__file__).resolve().parent,
)
sys.path.insert(0, str(_QOU_REPO_ROOT / "tools" / "qou-substrate" / "python"))

from witness_base import WitnessBuilder  # noqa: E402

REPO_ROOT = _QOU_REPO_ROOT

# Patterns for absolute-value notation around categorical objects
MODULUS_PATTERNS = [
    re.compile(r'\|\s*\\mathrm\{tr\}_M[^\|]*\|'),
    re.compile(r'\\lvert\s*\\mathrm\{tr\}_M[^\\]*\\rvert'),
    re.compile(r'\|\s*tr_M[^\|]*\|'),
    re.compile(r'\|\s*\\chi[^\|]*\|'),
    re.compile(r'\|\s*\\tau[^\|]*\|'),
]

# Section keywords for ARCHIMEDEAN context (case-insensitive)
ARCHIMEDEAN_HINTS = re.compile(
    r'\b(archimedean|post-?τ|post-?tau|at q_0|at \$q_0\$|numerical|MeV|m_e|specialize|specialised|specialized|evaluat)',
    re.IGNORECASE
)

# Section keywords for CATEGORICAL / PRE-τ context
CATEGORICAL_HINTS = re.compile(
    r'\b(categorical|pre-?τ|pre-?tau|formal q|generic q|Habiro|Hecke|q-deformation|fibre|fiber|bar-symmetric|bar-asymmetric)',
    re.IGNORECASE
)


def classify_site(file_path: Path, line_no: int, line_text: str,
                   lines_before: list[str], lines_after: list[str]) -> str:
    """Classify a |...| occurrence as ARCHIMEDEAN-OK / NON-ARCH-MISUSE / AMBIGUOUS."""
    context = "\n".join(lines_before + [line_text] + lines_after)

    arch_hits = bool(ARCHIMEDEAN_HINTS.search(context))
    cat_hits = bool(CATEGORICAL_HINTS.search(context))

    if cat_hits and not arch_hits:
        return "NON-ARCH-MISUSE"
    if arch_hits and not cat_hits:
        return "ARCHIMEDEAN-OK"
    if arch_hits and cat_hits:
        return "BOTH-SIGNALS"
    return "AMBIGUOUS"


def scan_file(path: Path) -> list[dict]:
    """Find all |...| sites in a single .md file."""
    lines = path.read_text().splitlines()
    sites = []
    for i, line in enumerate(lines):
        for pat in MODULUS_PATTERNS:
            if pat.search(line):
                cls = classify_site(
                    path, i + 1, line,
                    lines[max(0, i-5):i],
                    lines[i+1:min(len(lines), i+6)]
                )
                sites.append({
                    "file": str(path.relative_to(REPO_ROOT)),
                    "line": i + 1,
                    "text": line.strip()[:200],
                    "classification": cls,
                })
                break  # only count first pattern hit per line
    return sites


def main() -> int:
    t0 = time.monotonic()

    builder = WitnessBuilder("paper-modulus-audit-nonarchimedean",
                              engine="python+regex", start_time=t0)
    builder.set_description(
        "Full paper audit of |...| usage in non-archimedean sections. "
        "Per user 2026-06-01: |...| should appear only in archimedean "
        "specializations; categorical / pre-τ statements should use "
        "signed tr_M and let the archimedean reduction add |...| if "
        "convergence requires it."
    )
    builder.set_audit_only(
        "docs/audits/2026-06-01-paper-modulus-nonarchimedean-audit.md"
    )

    content_root = REPO_ROOT / "content" / "quantum-observable-universe"
    all_sites = []
    for md_path in content_root.rglob("*.md"):
        sites = scan_file(md_path)
        all_sites.extend(sites)

    by_directory: dict[str, list[dict]] = {}
    by_classification = {"ARCHIMEDEAN-OK": 0, "NON-ARCH-MISUSE": 0,
                         "BOTH-SIGNALS": 0, "AMBIGUOUS": 0}
    for s in all_sites:
        d = s["file"].split("/")[-2] if "/" in s["file"] else "root"
        by_directory.setdefault(d, []).append(s)
        by_classification[s["classification"]] += 1

    print("=" * 78)
    print(" Paper |...| audit — non-archimedean section misuse")
    print("=" * 78)
    print()
    print(f"Total |...| sites found: {len(all_sites)}")
    print()
    print("By classification:")
    for cls, n in by_classification.items():
        print(f"  {cls:>22s}: {n}")
    print()
    print("By directory (NON-ARCH-MISUSE count):")
    misuse_by_dir = {
        d: sum(1 for s in sites if s["classification"] == "NON-ARCH-MISUSE")
        for d, sites in by_directory.items()
    }
    for d, n in sorted(misuse_by_dir.items(), key=lambda x: -x[1])[:15]:
        if n > 0:
            print(f"  {d:>40s}: {n}")
    print()
    print("Top 10 NON-ARCH-MISUSE examples:")
    misuse_sites = [s for s in all_sites if s["classification"] == "NON-ARCH-MISUSE"]
    for s in misuse_sites[:10]:
        print(f"  {s['file']}:{s['line']}")
        print(f"    {s['text'][:120]}")
    print()

    builder.add_data("total_sites", len(all_sites))
    builder.add_data("by_classification", by_classification)
    builder.add_data("by_directory_misuse_count",
                     dict(sorted(misuse_by_dir.items(), key=lambda x: -x[1])))
    # Cap stored sites to avoid massive witness file
    builder.add_data("non_arch_misuse_sample",
                     [{"file": s["file"], "line": s["line"], "text": s["text"][:150]}
                      for s in misuse_sites[:50]])
    builder.add_data("archimedean_ok_sample",
                     [{"file": s["file"], "line": s["line"], "text": s["text"][:150]}
                      for s in (s for s in all_sites if s["classification"] == "ARCHIMEDEAN-OK")][:20])

    builder.add_data("audit_method", {
        "patterns_searched": [p.pattern for p in MODULUS_PATTERNS],
        "archimedean_hints": ARCHIMEDEAN_HINTS.pattern,
        "categorical_hints": CATEGORICAL_HINTS.pattern,
        "classification_rule": "see classify_site() — context window 5 lines either side",
        "limitation": "regex-based; some misuse may classify as AMBIGUOUS if context lacks clear hints",
    })

    builder.add_data("recommendation", (
        f"Found {by_classification['NON-ARCH-MISUSE']} sites with |...| in "
        f"contexts that read as categorical / pre-τ rather than archimedean. "
        f"Per user 2026-06-01: refactor these to use signed tr_M (or χ, etc.) "
        f"in the categorical statement, with archimedean specialization "
        f"adding |...| ONLY where convergence requires it. The fact that "
        f"sites like conj:im-q-physical-role use |tr_M| at the conjecture "
        f"level — a conjecture about Im(q) — is itself self-contradictory "
        f"and a candidate for the first refactor pass."
    ))

    builder.add_assertion(
        name="found_non_arch_misuse_sites",
        computed=by_classification["NON-ARCH-MISUSE"] > 0,
        expected=True,
        tolerance=0.0,
        source="Regex audit of paper .md files",
    )

    out = builder.save()
    print(f"✓ Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
