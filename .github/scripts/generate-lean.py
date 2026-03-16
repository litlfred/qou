#!/usr/bin/env python3
"""generate-lean.py — Extract labelled items from LaTeX and produce Lean 4 stubs.

Usage
─────
    python3 .github/scripts/generate-lean.py [CHAPTERS_DIR] [OUTPUT_LEAN] [--manifest MANIFEST]

Positional arguments (all optional, sensible defaults):
    CHAPTERS_DIR   Directory containing .tex chapter files   (default: chapters/)
    OUTPUT_LEAN    Path to write the generated Lean file     (default: lean/QOU/Defs.lean)

Optional flags:
    --manifest F   Also write a JSON manifest mapping labels → metadata to F.

The script scans every `*.tex` file under CHAPTERS_DIR for patterns like:

    \\begin{definition}[Display Name]
    \\label{def:foo-bar}

and emits one Lean `def stub_<prefix>_<slug> : Unit := ()` per labelled
item, grouped by source file, with a docstring carrying the LaTeX label,
display name, environment type, and source location.

The generated file is *deterministic*: identical inputs always produce
identical output (sorted by filename then line number).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

# ── Configuration ──────────────────────────────────────────────────────────────

# LaTeX environments whose \label we extract.
TRACKED_ENVS = {"definition", "theorem", "proposition", "lemma", "conjecture"}

# Label prefixes that correspond to formal items.
TRACKED_PREFIXES = {"def", "thm", "prop", "lem", "conj"}

# Hand-written Lean modules that provide deeper formalisations.
# Keys are LaTeX labels; values are the qualified Lean name.
LEAN_XREFS: dict[str, str] = {
    "def:quantum-universe":            "QOU.Basic.QuantumUniverse",
    "def:quantum-observable-universe": "QOU.Basic.QuantumObservableUniverse",
    "def:c-quantum-universe":          "QOU.Basic.QuantumUniverse",
    "def:c-quantum-observable-universe": "QOU.Basic.QuantumObservableUniverse",
    "def:instanton":                   "QOU.Basic.InstantonConnection",
    "lem:irreducible-connection":      "QOU.Basic.irreducible_connection",
    "prop:self-dual-curvature":        "QOU.Basic.self_dual_curvature",
    "def:substrate-parameter":         "QOU.Basic.SubstrateParameter",
    "def:quantum-gauge-group":         "QOU.Basic.QuantumGaugeGroup",
    "def:quantum-planck-constant":     "QOU.QuantumGroup.QuantumPlanckConstant",
    "def:direct-limit-algebra":        "QOU.FrobeniusHopf.DirectLimitAlgebra",
    "def:braid-group":                 "QOU.BraidGroup.BraidGroup3",
    "def:s3-group":                    "QOU.BraidGroup.S3",
    "def:su2-basis":                   "QOU.BraidGroup.SU2Basis",
    "def:braid-twist-flip":            "QOU.BraidGroup.BraidInvolutions",
    "def:quantum-su2":                 "QOU.QuantumGroup.QuantumSU2",
    "thm:descartes":                   "QOU.QuantumGroup.descartes_theorem",
}

# Mathlib4 references for selected labels.
MATHLIB_XREFS: dict[str, str] = {
    "def:quantum-universe":            "Mathlib.CategoryTheory.Monoidal.Basic",
    "def:quantum-observable-universe": "Mathlib.CategoryTheory.Monoidal.Basic",
    "def:quantum-gauge-group":         "Mathlib.RingTheory.HopfAlgebra",
    "def:braid-group":                 "Mathlib.GroupTheory.PresentedGroup",
    "def:s3-group":                    "Equiv.Perm (Fin 3)",
    "def:su2-basis":                   "Mathlib.Algebra.Lie.Basic",
    "def:quantum-su2":                 "Mathlib.RingTheory.HopfAlgebra",
    "def:direct-limit-algebra":        "Mathlib.Algebra.DirectLimit",
    "def:brings-surface":              "Mathlib.AlgebraicGeometry.ProjectiveSpectrum.Basic",
    "prop:chiral-elliptic":            "Mathlib.AlgebraicGeometry.EllipticCurve.Basic",
    "def:quantum-characteristic-classes": "Mathlib.Topology.FiberBundle.Basic",
    "prop:euler-char-stability":       "Mathlib.Topology.Algebra.InfiniteSum.Basic",
}


# ── Data model ─────────────────────────────────────────────────────────────────

@dataclass
class LabelledItem:
    label: str           # e.g. "def:quantum-universe"
    env: str             # e.g. "definition"
    display: str         # e.g. "Quantum Universe"
    source: str          # e.g. "chapters/quantum-observable-universe.tex"
    line: int            # 1-based line number of \label
    lean_ref: str = ""   # qualified Lean name (if hand-written)
    mathlib_ref: str = ""  # Mathlib4 module (if known)


# ── Parsing ────────────────────────────────────────────────────────────────────

# Matches  \begin{definition}[Display Name]  (with optional whitespace/newlines).
# The inner group allows `]` to appear inside $…$ math mode.
_RE_BEGIN = re.compile(
    r"\\begin\{(" + "|".join(TRACKED_ENVS) + r")\}"
    r"(?:\s*\[((?:[^\]$]|\$[^$]*\$)*)\])?"
)

# Matches  \label{prefix:slug}
_RE_LABEL = re.compile(
    r"\\label\{((?:" + "|".join(TRACKED_PREFIXES) + r"):[\w-]+)\}"
)

# LaTeX commands to strip from display names for readability.
_RE_LATEX_CMD = re.compile(r"\\(?:mathbb|mathfrak|mathrm|mathcal|mathsf|operatorname|text)\{([^}]*)\}")
_RE_LATEX_MISC = re.compile(r"\\[a-zA-Z]+")


def _clean_display(raw: str) -> str:
    """Strip LaTeX markup from a display name for use in Lean docstrings."""
    s = raw.strip()
    # Replace \mathbb{X} etc. with just X
    s = _RE_LATEX_CMD.sub(r"\1", s)
    # Remove $..$ math delimiters
    s = s.replace("$", "")
    # Remove remaining backslash commands (e.g. \cdot, \,)
    s = _RE_LATEX_MISC.sub("", s)
    # Remove backslash + single non-letter character (e.g. \, \; \!)
    s = re.sub(r"\\.", "", s)
    # Remove braces and subscript/superscript markers
    s = s.replace("{", "").replace("}", "")
    # Collapse whitespace and stray punctuation artefacts
    s = re.sub(r"\s+", " ", s).strip()
    return s


def scan_tex(path: Path, rel_root: Path) -> list[LabelledItem]:
    """Return all labelled items found in *path*."""
    items: list[LabelledItem] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    pending_env: str | None = None
    pending_display: str | None = None

    for lineno_0, raw in enumerate(lines):
        lineno = lineno_0 + 1

        # Look for \begin{env}[display]
        m_begin = _RE_BEGIN.search(raw)
        if m_begin:
            pending_env = m_begin.group(1)
            pending_display = _clean_display(m_begin.group(2) or "")

        # Look for \label{prefix:slug}
        m_label = _RE_LABEL.search(raw)
        if m_label:
            label = m_label.group(1)
            env = pending_env or _guess_env(label)
            display = pending_display or ""
            rel_path = str(path.relative_to(rel_root))

            item = LabelledItem(
                label=label,
                env=env,
                display=display,
                source=rel_path,
                line=lineno,
                lean_ref=LEAN_XREFS.get(label, ""),
                mathlib_ref=MATHLIB_XREFS.get(label, ""),
            )
            items.append(item)

            # Reset pending state
            pending_env = None
            pending_display = None

    return items


def _guess_env(label: str) -> str:
    """Infer the environment type from a label prefix."""
    prefix = label.split(":")[0]
    return {
        "def": "definition",
        "thm": "theorem",
        "prop": "proposition",
        "lem": "lemma",
        "conj": "conjecture",
    }.get(prefix, "definition")


# ── Code generation ────────────────────────────────────────────────────────────

_HEADER = '''\
/-!
# QOU.Defs — Auto-generated Theorem Index

This file is **auto-generated** by `.github/scripts/generate-lean.py`.
Do not edit manually; re-run the generator after modifying LaTeX sources.

It provides a machine-readable index mapping every labelled definition,
theorem, proposition, lemma, and conjecture from the LaTeX paper to a
Lean 4 declaration stub.

Each entry includes:
- the LaTeX label,
- the environment type (definition / theorem / proposition / lemma / conjecture),
- the display name from the LaTeX `[…]` option,
- the source file and line number, and
- a link to the hand-written Lean formalisation (if one exists).

## Regeneration

```sh
python3 .github/scripts/generate-lean.py chapters/ lean/QOU/Defs.lean
```
-/
'''


def _lean_slug(label: str) -> str:
    """Convert ``def:quantum-universe`` → ``stub_def_quantum_universe``."""
    return "stub_" + label.replace(":", "_").replace("-", "_")


def _chapter_title(source: str) -> str:
    """Derive a chapter title from the filename."""
    stem = Path(source).stem
    return stem.replace("-", " ").title()


def generate_lean(items: list[LabelledItem]) -> str:
    """Return the full content of the generated Lean file."""
    parts: list[str] = [_HEADER]

    # Group by source file (stable order: sorted by filename).
    from collections import OrderedDict
    by_source: OrderedDict[str, list[LabelledItem]] = OrderedDict()
    for it in sorted(items, key=lambda i: (i.source, i.line)):
        by_source.setdefault(it.source, []).append(it)

    for source, group in by_source.items():
        title = _chapter_title(source)
        parts.append(
            f"-- {'═' * 72}\n"
            f"-- {title}\n"
            f"-- Source: {source}\n"
            f"-- {'═' * 72}\n"
        )
        for it in group:
            doc_lines = [f"`{it.label}` — {it.display} ({it.env.capitalize()})"]
            doc_lines.append(f"Source: {it.source}:{it.line}")
            if it.lean_ref:
                doc_lines.append(f"Lean: `{it.lean_ref}`")
            if it.mathlib_ref:
                doc_lines.append(f"Mathlib: `{it.mathlib_ref}`")
            docstring = "\n    ".join(doc_lines)
            slug = _lean_slug(it.label)
            parts.append(f"/-- {docstring} -/\ndef {slug} : Unit := ()\n")

    return "\n".join(parts)


# ── Manifest ───────────────────────────────────────────────────────────────────

def generate_manifest(items: list[LabelledItem]) -> str:
    """Return a JSON manifest of all items."""
    return json.dumps(
        [asdict(i) for i in sorted(items, key=lambda i: (i.source, i.line))],
        indent=2,
        ensure_ascii=False,
    )


# ── CLI ────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract labelled items from LaTeX and produce Lean 4 stubs."
    )
    parser.add_argument(
        "chapters_dir",
        nargs="?",
        default="chapters",
        help="Directory containing .tex chapter files (default: chapters/)",
    )
    parser.add_argument(
        "output_lean",
        nargs="?",
        default="lean/QOU/Defs.lean",
        help="Path to write the generated Lean file (default: lean/QOU/Defs.lean)",
    )
    parser.add_argument(
        "--manifest",
        default=None,
        help="Also write a JSON manifest to this path.",
    )
    args = parser.parse_args()

    chapters_dir = Path(args.chapters_dir)
    if not chapters_dir.is_dir():
        print(f"Error: {chapters_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    # Determine the repository root (parent of chapters_dir).
    repo_root = chapters_dir.parent

    # Scan all .tex files.
    tex_files = sorted(chapters_dir.glob("*.tex"))
    if not tex_files:
        print(f"Warning: no .tex files found in {chapters_dir}", file=sys.stderr)

    all_items: list[LabelledItem] = []
    for tf in tex_files:
        all_items.extend(scan_tex(tf, repo_root))

    print(f"Found {len(all_items)} labelled items in {len(tex_files)} files.")

    # Write Lean file.
    output_path = Path(args.output_lean)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lean_content = generate_lean(all_items)
    output_path.write_text(lean_content, encoding="utf-8")
    print(f"Wrote {output_path}  ({len(all_items)} stubs)")

    # Write manifest if requested.
    if args.manifest:
        manifest_path = Path(args.manifest)
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(generate_manifest(all_items), encoding="utf-8")
        print(f"Wrote {manifest_path}")


if __name__ == "__main__":
    main()
