#!/usr/bin/env python3
"""validate-tex-snippets.py — validate TeX snippets embedded in .md content files.

Extracts inline math ($...$), display math ($$...$$), and fenced ```tex blocks
from content .md files, compiles each snippet with pdflatex in nonstop mode,
and reports errors.

Usage
-----
    # Validate all .md files under content/
    python validate-tex-snippets.py content/

    # Validate specific files
    python validate-tex-snippets.py content/qou/ch1/quantum-connection.md

    # Output JSON (for QA report integration)
    python validate-tex-snippets.py content/ --json > tex-validation.json

    # Output warnings log (compatible with generate-qa.py)
    python validate-tex-snippets.py content/ --warnings-log tex-warnings.log

Requires: pdflatex (from TeX Live).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass, field
from pathlib import Path

# ── Snippet extraction ─────────────────────────────────────────────

@dataclass
class TexSnippet:
    """A TeX snippet extracted from a .md file."""
    file: str
    line: int
    kind: str          # "inline", "display", "fenced"
    content: str
    raw: str           # original text including delimiters

@dataclass
class ValidationError:
    """A validation error for a TeX snippet."""
    file: str
    line: int
    kind: str
    snippet_preview: str
    error: str
    category: str      # "TeX Syntax", "Missing Package", "Math Mode", etc.


def extract_snippets(filepath: str, text: str) -> list[TexSnippet]:
    """Extract all TeX snippets from a markdown file."""
    snippets: list[TexSnippet] = []
    lines = text.split("\n")
    i = 0

    while i < len(lines):
        line = lines[i]

        # Fenced TeX block: ```tex ... ```
        if line.strip().startswith("```tex"):
            start_line = i + 1
            i += 1
            tex_lines: list[str] = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                tex_lines.append(lines[i])
                i += 1
            content = "\n".join(tex_lines)
            raw = "```tex\n" + content + "\n```"
            if content.strip():
                snippets.append(TexSnippet(
                    file=filepath, line=start_line,
                    kind="fenced", content=content, raw=raw,
                ))
            i += 1  # skip closing ```
            continue

        # Skip other fenced blocks
        if line.strip().startswith("```"):
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                i += 1
            i += 1
            continue

        # Display math: $$...$$ (possibly multi-line)
        if "$$" in line:
            # Check for single-line display math: $$...$$
            single = re.findall(r'\$\$(.+?)\$\$', line)
            if single:
                for m in single:
                    snippets.append(TexSnippet(
                        file=filepath, line=i + 1,
                        kind="display", content=m.strip(), raw=f"$${m}$$",
                    ))
                i += 1
                continue

            # Multi-line: $$ on its own line
            if line.strip().startswith("$$"):
                start_line = i + 1
                first = line.strip()[2:]
                math_lines = [first] if first.strip() else []
                i += 1
                while i < len(lines) and "$$" not in lines[i]:
                    math_lines.append(lines[i])
                    i += 1
                if i < len(lines):
                    last = lines[i].replace("$$", "").strip()
                    if last:
                        math_lines.append(last)
                    i += 1
                content = "\n".join(math_lines).strip()
                if content:
                    snippets.append(TexSnippet(
                        file=filepath, line=start_line,
                        kind="display", content=content,
                        raw=f"$$\n{content}\n$$",
                    ))
                continue

        # Inline math: $...$ (but not $$)
        # Match $...$ that aren't escaped and aren't part of $$
        for m in re.finditer(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', line):
            content = m.group(1).strip()
            if content:
                snippets.append(TexSnippet(
                    file=filepath, line=i + 1,
                    kind="inline", content=content, raw=m.group(0),
                ))

        i += 1

    return snippets


# ── TeX compilation validation ─────────────────────────────────────

# Minimal LaTeX preamble matching the project's actual packages
_PREAMBLE = r"""\documentclass[12pt]{report}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{mathtools}
\usepackage{tikz}
\usepackage{tikz-cd}
\usepackage[dvipsnames]{xcolor}
\usepackage{graphicx}
\usepackage{hyperref}
\newtheorem{theorem}{Theorem}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{example}[theorem]{Example}
\newtheorem{remark}[theorem]{Remark}
\newcommand{\lean}[1]{\ensuremath{\forall}}
\newcommand{\leanok}{\ensuremath{\checkmark}}
\newcommand{\notready}{\ensuremath{\times}}
\newcommand{\mathlibok}{\ensuremath{\checkmark\checkmark}}
\newcommand{\uses}[1]{}
\begin{document}
"""

_POSTAMBLE = r"""
\end{document}
"""

# Errors to ignore (not real problems)
_IGNORE_PATTERNS = [
    re.compile(r"Underfull \\[hv]box"),
    re.compile(r"Overfull \\[hv]box"),
]


def _wrap_snippet(snippet: TexSnippet) -> str:
    """Wrap a snippet in a compilable LaTeX document."""
    content = snippet.content
    if snippet.kind == "inline":
        return _PREAMBLE + f"$${content}$$\n" + _POSTAMBLE
    elif snippet.kind == "display":
        return _PREAMBLE + f"\\[\n{content}\n\\]\n" + _POSTAMBLE
    else:  # fenced — raw LaTeX, may be a full environment
        return _PREAMBLE + content + "\n" + _POSTAMBLE


def _classify_error(error_line: str) -> str:
    """Classify a TeX error into a category."""
    lower = error_line.lower()
    if "undefined control sequence" in lower:
        return "Undefined Command"
    if "missing" in lower and ("$" in lower or "math" in lower):
        return "Math Mode"
    if "missing" in lower:
        return "Missing Token"
    if "extra" in lower:
        return "Extra Token"
    if "environment" in lower:
        return "Environment"
    if "file" in lower and "not found" in lower:
        return "Missing Package"
    if "runaway" in lower:
        return "Runaway"
    return "TeX Syntax"


def validate_snippet(snippet: TexSnippet, tmpdir: str) -> list[ValidationError]:
    """Compile a TeX snippet and return any errors."""
    doc = _wrap_snippet(snippet)
    tex_file = os.path.join(tmpdir, "snippet.tex")
    with open(tex_file, "w", encoding="utf-8") as f:
        f.write(doc)

    try:
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
             "-no-shell-escape", "snippet.tex"],
            cwd=tmpdir,
            capture_output=True,
            text=True,
            timeout=15,
        )
    except subprocess.TimeoutExpired:
        return [ValidationError(
            file=snippet.file, line=snippet.line, kind=snippet.kind,
            snippet_preview=snippet.content[:80],
            error="pdflatex timed out (>15s)",
            category="Timeout",
        )]
    except FileNotFoundError:
        return [ValidationError(
            file=snippet.file, line=snippet.line, kind=snippet.kind,
            snippet_preview=snippet.content[:80],
            error="pdflatex not found — install TeX Live",
            category="Missing Tool",
        )]

    if result.returncode == 0:
        return []

    # Parse errors from the log
    errors: list[ValidationError] = []
    log_file = os.path.join(tmpdir, "snippet.log")
    log_text = ""
    if os.path.exists(log_file):
        with open(log_file, "r", encoding="utf-8", errors="replace") as f:
            log_text = f.read()

    # Extract ! Error lines
    for m in re.finditer(r'^! (.+)$', log_text, re.MULTILINE):
        error_msg = m.group(1).strip()

        # Skip ignorable warnings
        if any(p.search(error_msg) for p in _IGNORE_PATTERNS):
            continue

        errors.append(ValidationError(
            file=snippet.file, line=snippet.line, kind=snippet.kind,
            snippet_preview=snippet.content[:80],
            error=error_msg,
            category=_classify_error(error_msg),
        ))

    # If return code was non-zero but we found no specific errors, add a generic one
    if not errors:
        # Check for common patterns in stdout
        stderr = result.stderr.strip()
        stdout_tail = result.stdout[-500:] if result.stdout else ""
        msg = stderr or "pdflatex failed (see log for details)"
        errors.append(ValidationError(
            file=snippet.file, line=snippet.line, kind=snippet.kind,
            snippet_preview=snippet.content[:80],
            error=msg[:200],
            category="TeX Syntax",
        ))

    return errors


# ── Main validation ────────────────────────────────────────────────

@dataclass
class ValidationReport:
    """Aggregate validation report."""
    files_scanned: int = 0
    snippets_found: int = 0
    snippets_valid: int = 0
    errors: list[ValidationError] = field(default_factory=list)

    @property
    def snippets_invalid(self) -> int:
        return self.snippets_found - self.snippets_valid


def validate_files(paths: list[str], verbose: bool = False) -> ValidationReport:
    """Validate TeX snippets in the given .md files."""
    report = ValidationReport()

    # Collect all .md files
    md_files: list[str] = []
    for p in paths:
        path = Path(p)
        if path.is_file() and path.suffix == ".md":
            md_files.append(str(path))
        elif path.is_dir():
            md_files.extend(str(f) for f in path.rglob("*.md"))

    report.files_scanned = len(md_files)

    # Extract and validate
    all_snippets: list[TexSnippet] = []
    for md_file in sorted(md_files):
        text = Path(md_file).read_text(encoding="utf-8", errors="replace")
        snippets = extract_snippets(md_file, text)
        all_snippets.extend(snippets)

    report.snippets_found = len(all_snippets)
    if verbose:
        print(f"Found {len(all_snippets)} TeX snippets in {len(md_files)} files", file=sys.stderr)

    with tempfile.TemporaryDirectory(prefix="tex-validate-") as tmpdir:
        for i, snippet in enumerate(all_snippets):
            if verbose and (i + 1) % 50 == 0:
                print(f"  Validating snippet {i + 1}/{len(all_snippets)}...", file=sys.stderr)

            errs = validate_snippet(snippet, tmpdir)
            if errs:
                report.errors.extend(errs)
            else:
                report.snippets_valid += 1

            # Clean up auxiliary files between runs
            for ext in (".aux", ".log", ".pdf", ".dvi"):
                f = os.path.join(tmpdir, f"snippet{ext}")
                if os.path.exists(f):
                    os.remove(f)

    return report


# ── Output formats ─────────────────────────────────────────────────

def format_text(report: ValidationReport) -> str:
    """Human-readable text output."""
    lines: list[str] = []
    lines.append(f"TeX Snippet Validation Report")
    lines.append(f"{'=' * 40}")
    lines.append(f"Files scanned:   {report.files_scanned}")
    lines.append(f"Snippets found:  {report.snippets_found}")
    lines.append(f"Snippets valid:  {report.snippets_valid}")
    lines.append(f"Snippets invalid: {report.snippets_invalid}")
    lines.append("")

    if report.errors:
        lines.append("Errors:")
        lines.append("-" * 40)
        for e in report.errors:
            rel_file = e.file
            lines.append(f"  {rel_file}:{e.line} [{e.kind}] ({e.category})")
            lines.append(f"    {e.error}")
            preview = e.snippet_preview.replace("\n", " ")[:60]
            lines.append(f"    snippet: {preview}...")
            lines.append("")
    else:
        lines.append("No errors found.")

    return "\n".join(lines)


def format_json(report: ValidationReport) -> str:
    """JSON output for programmatic consumption."""
    return json.dumps({
        "files_scanned": report.files_scanned,
        "snippets_found": report.snippets_found,
        "snippets_valid": report.snippets_valid,
        "snippets_invalid": report.snippets_invalid,
        "errors": [asdict(e) for e in report.errors],
    }, indent=2)


def format_warnings_log(report: ValidationReport) -> str:
    """Warnings log format compatible with generate-qa.py."""
    lines: list[str] = []
    for e in report.errors:
        # Format as: LaTeX Warning: [category] file:line — message
        lines.append(f"LaTeX Warning: [{e.category}] {e.file}:{e.line} — {e.error}")
    return "\n".join(lines)


# ── CLI ────────────────────────────────────────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Validate TeX snippets in .md content files",
    )
    ap.add_argument("paths", nargs="+", help="Files or directories to scan")
    ap.add_argument("--json", action="store_true", help="Output JSON")
    ap.add_argument("--warnings-log", metavar="FILE",
                    help="Write warnings in generate-qa.py compatible format")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    report = validate_files(args.paths, verbose=args.verbose)

    if args.json:
        print(format_json(report))
    else:
        print(format_text(report))

    if args.warnings_log:
        Path(args.warnings_log).write_text(
            format_warnings_log(report), encoding="utf-8",
        )
        if not args.json:
            print(f"\nWarnings log written to {args.warnings_log}")

    sys.exit(0 if not report.errors else 1)


if __name__ == "__main__":
    main()
