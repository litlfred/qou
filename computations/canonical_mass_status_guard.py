#!/usr/bin/env python3
"""Status-claim guard for the canonical absolute-nucleon-mass figure.

The compute layer is guarded (canonical_mass facade + DeprecationWarning on the
Vol(B3)*rho forms). This script guards the *prose* layer: it scans content/ + docs/
for the DEPRECATED absolute-mass magnitudes being presented as the live m_p status.

Recurrence it prevents: an agent citing "m_p misses ~437x / 2.89% Vol.rho gap" as the
current status (2026-08-01). The live canonical m_p is CODATA to +1.35 ppb
(computations/per-observable-100x-status.witness.json). See
docs/canonical-mass-formula-guardrail.md.

Warn-only by default (exit 0); --strict exits 1 if any un-allowlisted hit is found.
Heuristic (proximity of a deprecated magnitude to a proton/m_p/absolute-mass mention);
eyeball the hits. Add legitimate historical/deprecation docs to ALLOWLIST.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Files/dirs that legitimately cite the deprecated figures (to warn about / resolve them).
ALLOWLIST_SUBSTR = (
    "docs/canonical-mass-formula-guardrail.md",
    "docs/coordination/2026-06-24-lambda-a",
    "docs/coordination/2026-08-01-l2-strategy-q0-observed",  # this coord doc explains the trap
    "docs/audits/",           # audits document the deprecation
    "computations/canonical_mass_status_guard.py",
    "AGENTS.md",              # the STRICT banner explains the wrong forms
    "CLAUDE.md",
)

# Deprecated absolute-mass magnitude tokens (the Vol(B3)*lambda_A / naive tr_M wrong forms).
DEPRECATED_MAGNITUDE = re.compile(
    r"(2\.89\s*%|2\.96\s*%|\+?\s*2\.9\d\s*%|-?\s*57\s*%|−57\s*%|"
    r"\b966\b|\b406\b|vol_density_borromean|Vol\(\U0001d4d1₃\)|lambda_scale|λ_scale)"
)
# Context that makes it a *status* claim about absolute nucleon mass.
MASS_CONTEXT = re.compile(
    r"(m_p|m_\{?p\}?|\U0001d52a_\U0001d52d|proton mass|nucleon mass|absolute mass|"
    r"m_n|neutron mass)", re.IGNORECASE
)
# Words that mark the line as explicitly flagging the figure as wrong/deprecated (skip).
NEGATED = re.compile(
    r"(deprecat|wrong|NOT\b|never|do not|don't|❌|purged|refut|artifact|"
    r"guardrail|must never|fit\b|mistake)", re.IGNORECASE
)


def is_allowlisted(rel: str) -> bool:
    return any(s in rel for s in ALLOWLIST_SUBSTR)


# Scope: the surfaces where a STALE live-status claim actually misleads a reader — the
# authoritative paper (content/) + the live top-level reference docs. The dated historical
# archive (docs/coordination|workplans|agent-briefs|audits) legitimately records the 2.89%
# figure from the λ_scale era (pre-2026-06-24 deprecation) and is deliberately NOT scanned;
# guarding it would be pure noise and the guard would be ignored.
LIVE_REFERENCE_DOCS = (
    "docs/precision-goals.md",
    "docs/canonical-derivation-cheat-sheet.md",
)


def _iter_target_files():
    content = REPO / "content"
    if content.exists():
        yield from content.rglob("*.md")
    for rel in LIVE_REFERENCE_DOCS:
        p = REPO / rel
        if p.exists():
            yield p


def scan() -> list[tuple[str, int, str]]:
    hits: list[tuple[str, int, str]] = []
    for path in _iter_target_files():
        rel = str(path.relative_to(REPO))
        if is_allowlisted(rel):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for i, line in enumerate(lines, 1):
            if not DEPRECATED_MAGNITUDE.search(line):
                continue
            # need a mass-status context on the same line, and no negation flag
            if not MASS_CONTEXT.search(line):
                continue
            if NEGATED.search(line):
                continue
            hits.append((rel, i, line.strip()[:160]))
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true", help="exit 1 if any hit is found")
    args = ap.parse_args()

    hits = scan()
    if not hits:
        print("canonical-mass status guard: OK — no deprecated absolute-mass figure cited as live status.")
        return 0

    print(f"canonical-mass status guard: {len(hits)} possible deprecated m_p-status citation(s):")
    for rel, ln, txt in hits:
        print(f"  {rel}:{ln}: {txt}")
    print()
    print("Live status is CODATA +1.35 ppb (canonical_mass facade); the 2.89%/966/406/-57% "
          "figures are the DEPRECATED Vol(B3)*rho forms. See docs/canonical-mass-formula-guardrail.md.")
    print("If a hit is a legitimate historical/deprecation mention, add it to ALLOWLIST_SUBSTR.")
    return 1 if args.strict else 0


if __name__ == "__main__":
    sys.exit(main())
