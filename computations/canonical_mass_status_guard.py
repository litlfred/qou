#!/usr/bin/env python3
"""Status-claim guard for the canonical absolute-nucleon-mass figure.

The compute layer is guarded (canonical_mass facade + DeprecationWarning on the
Vol(B3)*rho forms). This script guards the *prose* layer: it scans content/ + docs/
for the DEPRECATED absolute-mass magnitudes being presented as the live m_p status.

Recurrence it prevents: an agent citing "m_p misses ~437x / 2.89% Vol.rho gap" as the
current status (2026-08-01). The live canonical m_p is CODATA to +1.35 ppb
(computations/per-observable-100x-status.witness.json). See
docs/canonical-mass-formula-guardrail.md.

`--scan-py` additionally scans DOCSTRINGS of production compute under
computations/ (excluding probes/, audits/, sweeps/). That surface sits between
this guard's .md scope and noncanonical_reentry_audit.py, which is AST-based and
drops docstrings by design — so a stale formula in a production script's
docstring was invisible to both. It is opt-in until its ~20 remaining hits are
triaged; see the note on the `scan_py` branch.

Verified against the defect it was built for (2026-08-08): with
mass_table_comprehensive.py at its pre-fix revision, `--scan-py` flags line 9
(`m(K) = m_e · [Vol(𝓑₃)/ℏ_q²] · λ_A …`); with the corrected docstring it does
not. Re-check both directions before changing NEGATION_WINDOW or the regexes.

Warn-only by default (exit 0); --strict exits 1 if any un-allowlisted hit is found.
Heuristic (proximity of a deprecated magnitude to a proton/m_p/absolute-mass mention);
eyeball the hits. Add legitimate historical/deprecation docs to ALLOWLIST.
"""
from __future__ import annotations

import argparse
import ast
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
# NOTE: `\bNOT\b` — the leading `\b` was missing, so this matched the "NOT" inside
# **KNOT**, and "knot" is everywhere in this corpus. That silently negated any line
# near a knot mention. Found 2026-08-08 while extending the guard to .py docstrings:
# it was why mass_table_comprehensive.py's stale λ_A docstring stayed invisible.
NEGATED = re.compile(
    r"(deprecat|wrong|\bNOT\b|never|do not|don't|❌|purged|refut|artifact|"
    r"guardrail|must never|fit\b|mistake|remov)", re.IGNORECASE
)


# Counterfactual / hypothesis framing: the docstring is not asserting the form as
# the live route, it is testing or targeting it — guardrail §3's permitted
# "studying λ_A itself" case. Checked docstring-scoped, like NEGATED. Kept
# deliberately narrow (no bare "would") so an actual stale assertion, which reads
# as a flat equation, still trips the guard.
COUNTERFACTUAL = re.compile(
    r"(hypothesis|tests? whether|would make|what we need to hit|"
    r"calibrated against|only into the target)",
    re.IGNORECASE,
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


# Production compute whose DOCSTRINGS are read as the spec for how a number is
# produced. Same rationale as LIVE_REFERENCE_DOCS: an agent opening
# mass_table_comprehensive.py to compute a mass reads its docstring as current.
# `probes/`, `audits/` and `sweeps/` are excluded for the same reason the dated
# doc archive is — they legitimately study the λ_A fit (guardrail §3), so
# scanning them would be pure noise and the guard would be ignored.
PY_SCAN_ROOT = "computations"
PY_EXCLUDED_DIR_PARTS = ("probes", "audits", "sweeps")

#: Lines either side of a flagged formula that a disclaimer must fall within to
#: count as negating it. 2 covers the usual "formula line / blank / ⚠ …" shape
#: without letting an unrelated mention elsewhere in the docstring suppress it.
NEGATION_WINDOW = 2


def _iter_target_files():
    content = REPO / "content"
    if content.exists():
        yield from content.rglob("*.md")
    for rel in LIVE_REFERENCE_DOCS:
        p = REPO / rel
        if p.exists():
            yield p


def _iter_py_docstrings():
    """Yield (rel, start_lineno, [lines]) for every docstring in production
    compute — module, class and function docstrings only.

    Yields whole docstrings, not single lines, because the negation check has to
    be docstring-scoped: a deprecation disclaimer is nearly always on a
    *neighbouring* line from the formula it disclaims ("m_p ≈ 406 (−57%)." /
    "The CANONICAL nucleon mass is …"). Per-line negation flagged 32 docstrings
    here, almost all of which already said the form was wrong — including this
    guard's own sibling modules and the very fix that prompted the extension.

    Docstrings, not comments and not code: a *comment* next to a call site is
    usually the correction ("this λ_A fallback was removed"), while the
    docstring above it is what goes stale. Code references are already covered
    by `noncanonical_reentry_audit.py`, which drops docstrings by design — this
    scans exactly the surface that audit cannot see.
    """
    root = REPO / PY_SCAN_ROOT
    if not root.exists():
        return
    for path in sorted(root.rglob("*.py")):
        rel_parts = path.relative_to(REPO).parts
        if any(part in PY_EXCLUDED_DIR_PARTS for part in rel_parts):
            continue
        rel = str(path.relative_to(REPO))
        if is_allowlisted(rel):
            continue
        try:
            src = path.read_text(encoding="utf-8")
            tree = ast.parse(src)
        except (UnicodeDecodeError, OSError, SyntaxError):
            continue
        lines = src.splitlines()
        for node in ast.walk(tree):
            if not isinstance(
                node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)
            ):
                continue
            body = getattr(node, "body", None)
            if not body:
                continue
            first = body[0]
            if not (
                isinstance(first, ast.Expr)
                and isinstance(first.value, ast.Constant)
                and isinstance(first.value.s, str)
            ):
                continue
            start = first.value.lineno
            end = min(getattr(first.value, "end_lineno", start), len(lines))
            yield rel, start, lines[start - 1:end]


def scan(scan_py: bool = False) -> list[tuple[str, int, str]]:
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
    # Production .py docstrings — the surface between the prose guard (content/
    # + docs/ .md only) and noncanonical_reentry_audit.py (AST, docstrings
    # deliberately dropped). mass_table_comprehensive.py fell in it: its
    # docstring advertised the removed λ_A form while the code below used the
    # canonical facade. Same three filters as the .md pass.
    #
    # OPT-IN (`--scan-py`) until triaged. The pass is verified to catch the
    # defect it was built for (see the module docstring's test note), but it
    # currently also raises ~15 untriaged files — deprecated modules describing
    # themselves, and λ_A research/verification scripts that guardrail §3
    # permits. Turning it on by default would flip a green guard red on hits
    # nobody has read yet, which is how a guard gets ignored. Triage is tracked
    # as a bean; wire it into the default (and CI) once the list is classified.
    if not scan_py:
        return hits
    for rel, start, doc_lines in _iter_py_docstrings():
        # Negation is docstring-scoped: if the docstring anywhere marks the form
        # as deprecated/wrong/a fit, it is not a stale live-status claim.
        for offset, line in enumerate(doc_lines):
            if not DEPRECATED_MAGNITUDE.search(line):
                continue
            if not MASS_CONTEXT.search(line):
                continue
            # Negation is checked over a PROXIMITY WINDOW, not the whole docstring.
            # Whole-docstring scope over-suppressed: an unrelated "not-computed" 18
            # lines below the formula hid the real hit. A disclaimer that actually
            # governs a formula sits within a line or two of it.
            lo = max(0, offset - NEGATION_WINDOW)
            window = "\n".join(doc_lines[lo:offset + NEGATION_WINDOW + 1])
            if NEGATED.search(window) or COUNTERFACTUAL.search(window):
                continue
            hits.append((rel, start + offset, line.strip()[:160]))
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true", help="exit 1 if any hit is found")
    ap.add_argument(
        "--scan-py",
        action="store_true",
        help="also scan docstrings of production compute under computations/ "
             "(opt-in until the current hit list is triaged)",
    )
    args = ap.parse_args()

    hits = scan(scan_py=args.scan_py)
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
