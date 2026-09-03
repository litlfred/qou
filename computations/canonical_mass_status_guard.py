#!/usr/bin/env python3
"""Status-claim guard for the canonical absolute-nucleon-mass figure.

The compute layer is guarded (canonical_mass facade + DeprecationWarning on the
Vol(B3)*rho forms). This script guards the *prose* layer: it scans content/ + docs/
for the DEPRECATED absolute-mass magnitudes being presented as the live m_p status.

Recurrence it prevents: an agent citing "m_p misses ~437x / 2.89% Vol.rho gap" as the
current status (2026-08-01). The live canonical m_p is CODATA to +1.35 ppb
(computations/per-observable-100x-status.witness.json). See
docs/canonical-mass-formula-guardrail.md.

The docstring pass (ON by default; `--no-scan-py` disables) scans DOCSTRINGS of
production compute under computations/ (excluding probes/, audits/, sweeps/ and
the audit_/probe_/sweep_ filename prefixes). That surface sits between this
guard's .md scope and noncanonical_reentry_audit.py, which is AST-based and
drops docstrings by design — so a stale formula in a production script's
docstring was invisible to both.

It shipped opt-in (2026-08-08) with 20 untriaged hits; those were triaged and
the pass turned on 2026-08-08 — 9 were stale live-status claims and were fixed,
11 cleared via five detector rules, each preferred over an allowlist entry so
the files stay watched for FUTURE staleness: SUMMARY_SCOPE (an EXPLORATORY /
DEPRECATED / counterfactual marker in the docstring summary governs what is
under it), `no <deprecated-token>` as an absence disclaimer, NAMES_THE_GAP
(.py only — see its note), the audit_/probe_/sweep_ filename prefixes, and
`m_p-pin` excluded from MASS_CONTEXT as a q₀-anchor name.

`--strict` is green as of 2026-08-08. The last two hits were correct,
carefully-qualified prose in docs/precision-goals.md ("2.89 % bare", "+2.89%
open gap", both sitting beside the live +1.35 ppb). They are cleared by
LINE_EXEMPTIONS — a per-LINE, content-hashed exemption — rather than by
loosening the .md pass, which is this guard's primary surface and where the
recurrence actually happened. Editing either sentence re-flags it.

Not yet wired into CI: no workflow currently runs this guard, and repo CI
auto-triggers are disabled (AGENTS.md), so the agent-run path is the gate
(AGENTS.md §"QA is agent-owned; CI is a backup").

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
import hashlib
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
    r"\b966\b|\b406\b|per_knot_density_borromean|Vol\(\U0001d4d1₃\)|lambda_scale|λ_scale)"
)
# Context that makes it a *status* claim about absolute nucleon mass.
# `m_p-pin` / `m_p pin` is EXCLUDED: there it names the q₀ anchor (the
# proton-ratio pin, per AGENTS.md §"q₀ anchor convention"), not a proton-mass
# value — so a line like "3.47% m_p-pin swing" in the Q_β c_k ladder is about
# a truncation coefficient, not about absolute mass.
MASS_CONTEXT = re.compile(
    r"(m_\{?p\}?(?![-_ ]?pin)|\U0001d52a_\U0001d52d|proton mass|nucleon mass|"
    r"absolute mass|m_n|neutron mass)", re.IGNORECASE
)
# Words that mark the line as explicitly flagging the figure as wrong/deprecated (skip).
# NOTE: `\bNOT\b` — the leading `\b` was missing, so this matched the "NOT" inside
# **KNOT**, and "knot" is everywhere in this corpus. That silently negated any line
# near a knot mention. Found 2026-08-08 while extending the guard to .py docstrings:
# it was why mass_table_comprehensive.py's stale λ_A docstring stayed invisible.
NEGATED = re.compile(
    r"(deprecat|wrong|\bNOT\b|never|do not|don't|❌|purged|refut|artifact|"
    r"guardrail|must never|fit\b|mistake|remov|"
    # "no <deprecated thing>" is a disclaimer of ABSENCE — the docstring is
    # saying the script does not use the form ("no m_e·Vol(𝓑₃)",
    # "(no λ_scale, no Skein)"). Kept to the deprecated tokens: a bare `no`
    # is far too common to negate on.
    r"\bno\s+(?:m_e|Vol|λ_scale|lambda_scale|Skein|special-cas))", re.IGNORECASE
)

# The magnitude is NAMING the known discrepancy ("the +2.89 % m_p gap"), not
# claiming a live mass. A gap is by definition the distance from the right
# answer, so a line that calls it one is not asserting it as the status.
# Checked on the hit line only — a "gap" elsewhere in the docstring says
# nothing about this line (the whole-docstring-scope mistake, see below).
#
# 🛑 .py DOCSTRINGS ONLY — do NOT extend this to the .md pass. The prose
# recurrence this guard was built for (2026-08-01) was an agent writing
# "m_p misses ~437× / 2.89% Vol·ρ gap" as the live status: it calls the figure
# a gap AND asserts it as current, so this rule would have missed the exact
# defect the guard exists to catch. In a docstring the two phrasings separate
# cleanly — a stale docstring states a FORMULA ("m(K) = m_e · [Vol(𝓑₃)/ℏ_q²] ·
# λ_A"), it does not narrate a miss — which is why the rule is safe here and
# unsafe there. The two `*_wiring.py` probes reporting "the recovered fraction
# of the +2.89 % m_p gap" are the cases it is for; the alternative was
# allowlisting those files, which would blind the guard to real future
# staleness in them.
NAMES_THE_GAP = re.compile(r"\bgaps?\b", re.IGNORECASE)


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


#: Individual LINES cleared by review, keyed by the sha256 (12 hex) of the
#: stripped line. Content-addressed on purpose, matching how `.qa.json`
#: sidecars and `*.witness.json` pin their sources: **edit the sentence and it
#: re-flags**, which a path-or-line-number exemption cannot promise. Use this
#: instead of adding a whole file to ALLOWLIST_SUBSTR — that blinds the guard
#: to everything else in the file, forever.
#:
#: The bar for adding one: the line must state the deprecated figure *and* its
#: correct scope, so a reader cannot mistake it for the live status. Both
#: entries below do (they say "bare" / "open gap" and sit beside the live
#: +1.35 ppb). A line that merely *mentions* the figure does not qualify —
#: fix its prose instead.
LINE_EXEMPTIONS: dict[str, str] = {
    # docs/precision-goals.md:51 — a table of residual SCALES; "m_avg: 2.89 %
    # bare → 819 ppm spectral" is the bare categorical figure, correctly
    # distinguished from the m_p 242 ppb μ-p floor in the same cell.
    "a78f1225dba6": "precision-goals: bare-vs-anchored residual scale table",
    # docs/precision-goals.md:225 — explicitly contrasts the *bare* categorical
    # value with the live anchored +1.35 ppb two lines above it.
    "15319ed2998a": "precision-goals: bare categorical value, contrasted with +1.35 ppb",
}


def is_exempt_line(line: str) -> bool:
    return hashlib.sha256(line.strip().encode()).hexdigest()[:12] in LINE_EXEMPTIONS


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
#: Same exclusion by FILENAME prefix. `computations/audit_delta_S_chain.py` is
#: the same kind of artifact as anything under `audits/` — it exists to walk the
#: λ_scale-era derivation chain — but it sits at the top level, so the directory
#: rule alone misses it. Same trade-off the directory rule already makes: these
#: files may go stale unwatched, and that is preferable to the guard being
#: ignored for noise.
PY_EXCLUDED_NAME_PREFIXES = ("audit_", "probe_", "sweep_")
#: PREFIX ONLY, DELIBERATELY — do not add the SUFFIX forms (bean `qou-omiu`,
#: measured 2026-08-24). This repo names overwhelmingly by suffix, so the
#: asymmetry looks like an oversight and has been reported as one: 57 files carry
#: `probe_`/`audit_`/`sweep_` as a prefix, while 210 top-level files carry those
#: words as a suffix, and across the full recursive scan surface 742 of the 2790
#: SCANNED files are suffix-class — 26.6 % of everything this guard looks at.
#:
#: Mirroring the prefixes into suffixes was measured and DECLINED. Re-running the
#: guard with both `PY_EXCLUDED_DIR_PARTS` and `PY_EXCLUDED_NAME_PREFIXES`
#: neutralised surfaces 11 hits, and every one is in an already-excluded location
#: (`audit_delta_S_chain.py`, four files under `probes/`, one under `sweeps/`).
#: ZERO are suffix-named files in the scanned surface. So the existing exclusions
#: are load-bearing — they suppress 11 genuine would-be false positives — while a
#: suffix rule would drop a quarter of the scan surface to prevent none.
#:
#: Note the detail that settles it: several of those hits DO end in `_probe.py`
#: (`..._q_locality_probe.py`), and they are already excluded BY DIRECTORY. A
#: suffix rule adds nothing for them; it would only blind the top-level files,
#: which cite nothing. Consistency of naming is not a reason to blind a guard.
#:
#: `_test.py` is separately never a candidate: a real unit test SHOULD be guarded.

#: Markers that, in a docstring's SUMMARY, declare the epistemic scope of
#: everything below it. Deliberately NOT the whole `NEGATED` set: a summary can
#: contain a negation word about some *other* object and mean nothing about the
#: mass form. `yekutieli_volume_join.py` is the case in point — "derive or
#: refute the 2.38× bridge" is about the bridge, while the docstring goes on to
#: label the deprecated Vol·ρ form "Production (m_p path)", which is exactly the
#: claim this guard exists to catch. Scope markers only.
SUMMARY_SCOPE = re.compile(
    r"(exploratory|unproved|deprecat|superseded|obsolete|historical|"
    r"do not wire|not wired)", re.IGNORECASE
)

#: How many leading lines of a docstring count as its SUMMARY. A scope marker
#: there ("EXPLORATORY (UNPROVED — do not wire into production)", "the weight
#: that would make m_p match CODATA") governs everything under it by
#: construction, so it negates the whole docstring.
#:
#: This is NOT the whole-docstring negation that was tried and reverted. That
#: let an incidental disclaimer ANYWHERE — a "not-computed" 18 lines *below* a
#: formula — suppress a real hit. A summary line is different in kind: it
#: states what the docstring is about. The pre-fix mass_table_comprehensive
#: docstring is the control, and its summary ("full mass/binding table at
#: current production tier") carries no marker, so it still trips the guard.
SUMMARY_LINES = 2

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
        if path.name.startswith(PY_EXCLUDED_NAME_PREFIXES):
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


def scan(scan_py: bool = True) -> list[tuple[str, int, str]]:
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
            if is_exempt_line(line):
                continue
            hits.append((rel, i, line.strip()[:160]))
    # Production .py docstrings — the surface between the prose guard (content/
    # + docs/ .md only) and noncanonical_reentry_audit.py (AST, docstrings
    # deliberately dropped). mass_table_comprehensive.py fell in it: its
    # docstring advertised the removed λ_A form while the code below used the
    # canonical facade. Same three filters as the .md pass.
    #
    # ON by default since 2026-08-08 (`--no-scan-py` disables): the hit list it
    # shipped with has been triaged — stale claims fixed, legitimate ones
    # cleared by rule rather than by allowlist. See the module docstring.
    if not scan_py:
        return hits
    for rel, start, doc_lines in _iter_py_docstrings():
        hits.extend(docstring_hits(rel, start, doc_lines))
    return hits


def docstring_hits(rel: str, start: int, doc_lines: list[str]) -> list[tuple[str, int, str]]:
    """Stale live-status hits within ONE docstring.

    Split out from `scan()` so the both-directions regression
    (`canonical_mass_status_guard_test.py`) can drive it with fixture
    docstrings instead of the live tree — the live tree is exactly what these
    filters are tuned against, so a test that reads it proves nothing.
    """
    found: list[tuple[str, int, str]] = []
    # A scope marker in the SUMMARY governs the whole docstring (see
    # SUMMARY_LINES for why this is not the reverted whole-docstring rule).
    summary = "\n".join(doc_lines[:SUMMARY_LINES])
    if SUMMARY_SCOPE.search(summary) or COUNTERFACTUAL.search(summary):
        return found
    for offset, line in enumerate(doc_lines):
        if not DEPRECATED_MAGNITUDE.search(line):
            continue
        if not MASS_CONTEXT.search(line):
            continue
        # Naming the gap is not claiming the status.
        if NAMES_THE_GAP.search(line):
            continue
        # Negation is checked over a PROXIMITY WINDOW, not the whole docstring.
        # Whole-docstring scope over-suppressed: an unrelated "not-computed" 18
        # lines below the formula hid the real hit. A disclaimer that actually
        # governs a formula sits within a line or two of it.
        lo = max(0, offset - NEGATION_WINDOW)
        window = "\n".join(doc_lines[lo:offset + NEGATION_WINDOW + 1])
        if NEGATED.search(window) or COUNTERFACTUAL.search(window):
            continue
        found.append((rel, start + offset, line.strip()[:160]))
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true", help="exit 1 if any hit is found")
    ap.add_argument(
        "--scan-py", dest="scan_py", action="store_true", default=True,
        help="scan docstrings of production compute under computations/ "
             "(default: on)",
    )
    ap.add_argument(
        "--no-scan-py", dest="scan_py", action="store_false",
        help="restrict to the .md prose pass",
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
