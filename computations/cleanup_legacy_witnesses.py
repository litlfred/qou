#!/usr/bin/env python3
"""Identify and (optionally) move clearly-legacy witness probes.

Criteria (all must hold for a script to be moved to ``_deprecated/``):

1. The script's ``*.witness.json`` exists and contains no top-level
   ``contentBlock`` self-claim. (``run_pipeline.py --list-orphaned``
   uses this same predicate.)
2. The witness is not marked ``auditOnly: true`` — those are
   deliberately unwired sidecars kept for audit reports.
3. No other live (non-``_deprecated/``) ``*.py`` under
   ``folio-assistant/computations/`` imports the script's module.
4. No markdown file under ``_audits/`` or ``docs/audits/`` cites the
   script filename, the witness filename, or the script stem.

This mirrors the heuristic recorded in
``folio-assistant/computations/_deprecated/README.md`` from the
original cleanup pass.

Usage
─────
    python3 cleanup_legacy_witnesses.py               # dry run, prints list
    python3 cleanup_legacy_witnesses.py --apply       # move files
    python3 cleanup_legacy_witnesses.py --apply --git # also `git mv`

The ``--apply`` mode moves both the ``.py`` and its ``*.witness.json``
into ``_deprecated/`` (and the matching ``.derivation.json`` if any).
Restoration only requires running the producer to re-emit the witness
next to its script.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

COMP_DIR = Path(__file__).resolve().parent
DEPRECATED_DIR = COMP_DIR / "_deprecated"
REPO_ROOT = COMP_DIR.parent.parent

_IMPORT_RE = re.compile(
    r"^\s*(?:from\s+([\w_]+)\s+import|import\s+([\w_]+))", re.MULTILINE
)


def _load_live_text() -> dict[str, str]:
    """Read every live `.py` under computations/ (skipping _deprecated/)."""
    out: dict[str, str] = {}
    for p in COMP_DIR.glob("*.py"):
        try:
            out[p.name] = p.read_text(encoding="utf-8")
        except Exception:
            out[p.name] = ""
    return out


def _build_importer_map(live_text: dict[str, str]) -> dict[str, set[str]]:
    importers: dict[str, set[str]] = {}
    for fname, text in live_text.items():
        for m in _IMPORT_RE.finditer(text):
            mod = m.group(1) or m.group(2)
            importers.setdefault(mod, set()).add(fname)
    return importers


def _is_imported_by_live(
    script_name: str, importers: dict[str, set[str]]
) -> set[str]:
    stem = Path(script_name).stem
    keys = {stem, stem.replace("-", "_")}
    hits: set[str] = set()
    for k in keys:
        for who in importers.get(k, set()):
            if who != script_name:
                hits.add(who)
    return hits


def _load_audit_text() -> str:
    """Concatenate every markdown file under _audits/ + docs/audits/."""
    chunks: list[str] = []
    for d in (REPO_ROOT / "_audits", REPO_ROOT / "docs" / "audits"):
        if not d.exists():
            continue
        for f in d.rglob("*.md"):
            try:
                chunks.append(f.read_text(encoding="utf-8", errors="ignore"))
            except Exception:
                continue
    return "\n".join(chunks)


def _witness_for(script_name: str) -> Path | None:
    stem = Path(script_name).stem
    for candidate in (
        f"{stem}.witness.json",
        f"{stem.replace('_', '-')}.witness.json",
    ):
        p = COMP_DIR / candidate
        if p.exists():
            return p
    return None


def _derivation_for(script_name: str) -> Path | None:
    stem = Path(script_name).stem
    for candidate in (
        f"{stem}.derivation.json",
        f"{stem.replace('_', '-')}.derivation.json",
    ):
        p = COMP_DIR / candidate
        if p.exists():
            return p
    return None


# Names that should never be moved even if all four heuristics pass.
# These are infrastructure-style scripts that may not declare a
# contentBlock but are wired into CI, into other live scripts via
# string-literal lookup, or are convention-protected (I14: audit/
# scan/compliance scripts are exempt from provenance requirements
# and are explicitly long-lived).
_PROTECTED_SUFFIX_RE = re.compile(r"(_audit|_scan|_compliance|_dashboard|_validator)$")


def _load_external_text() -> str:
    """Concatenate non-python places that might reference a witness/
    script by string literal: CI workflows, shell scripts, TS pipeline
    code. We deliberately exclude other ``.py`` files under
    ``computations/`` because (a) genuine python imports are already
    caught by ``_is_imported_by_live``, and (b) free-form prose in
    docstrings / comments produces too many false positives on bare
    stems (e.g. one script citing a related result in a docstring).

    We *do* include python files that load witness JSON by string
    literal — these match on the ``*.witness.json`` filename, which is
    far less collision-prone than the ``.py`` stem and is what callers
    like ``canonical_derivation_pipeline_compliance.py`` use."""
    chunks: list[str] = []

    for d in (
        REPO_ROOT / ".github" / "workflows",
        REPO_ROOT / "scripts",
        REPO_ROOT / "content" / "pipeline",
        REPO_ROOT / "tools",
    ):
        if not d.exists():
            continue
        for ext in ("*.yml", "*.yaml", "*.sh", "*.ts", "*.tsx", "*.js"):
            for f in d.rglob(ext):
                try:
                    chunks.append(f.read_text(encoding="utf-8", errors="ignore"))
                except Exception:
                    continue

    # Other live python files: only their string literals can be a
    # cross-script reference. We grab the whole file but the (5) check
    # restricts the lookup to ``*.witness.json`` filenames, so prose
    # mentions of a sibling .py module name will not trigger a match.
    for f in COMP_DIR.glob("*.py"):
        try:
            chunks.append(f.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            continue

    return "\n".join(chunks)


def find_legacy_candidates() -> list[tuple[Path, Path, Path | None]]:
    """Return (script_path, witness_path, derivation_path|None) tuples."""
    live_text = _load_live_text()
    importers = _build_importer_map(live_text)
    audit_text = _load_audit_text()
    external_text = _load_external_text()

    out: list[tuple[Path, Path, Path | None]] = []
    for p in sorted(COMP_DIR.glob("*.py")):
        if p.name == "__init__.py":
            continue
        # I14 convention: audit/scan/compliance scripts are infra.
        if _PROTECTED_SUFFIX_RE.search(p.stem):
            continue
        wp = _witness_for(p.name)
        if wp is None:
            continue
        try:
            w = json.loads(wp.read_text(encoding="utf-8"))
        except Exception:
            continue

        # (1) no contentBlock self-claim
        if w.get("contentBlock"):
            continue
        # (2) not flagged auditOnly
        if w.get("auditOnly"):
            continue
        # (3) not imported by any live module
        if _is_imported_by_live(p.name, importers):
            continue
        # (4) not cited in any audit markdown
        stem = p.stem
        hyphen_stem = stem.replace("_", "-")
        if (
            p.name in audit_text
            or wp.name in audit_text
            or stem in audit_text
            or hyphen_stem in audit_text
        ):
            continue
        # (5) not referenced by string-literal in CI/scripts/pipeline/
        # tooling or by any other live python via the witness JSON
        # filename. Match only on the witness file name and the .py
        # filename — both contain extensions, so collisions on bare
        # stems in docstrings/comments are avoided.
        if (
            wp.name in external_text
            or p.name in external_text
        ):
            continue

        out.append((p, wp, _derivation_for(p.name)))
    return out


def move_one(
    script: Path,
    witness: Path,
    derivation: Path | None,
    use_git: bool,
) -> None:
    DEPRECATED_DIR.mkdir(parents=True, exist_ok=True)
    targets = [(script, DEPRECATED_DIR / script.name),
               (witness, DEPRECATED_DIR / witness.name)]
    if derivation is not None:
        targets.append((derivation, DEPRECATED_DIR / derivation.name))

    for src, dst in targets:
        if dst.exists():
            print(f"  skip (target exists): {dst.name}", file=sys.stderr)
            continue
        if use_git:
            subprocess.run(
                ["git", "mv", str(src), str(dst)],
                cwd=str(REPO_ROOT),
                check=True,
            )
        else:
            shutil.move(str(src), str(dst))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true",
                    help="actually move files (default: dry run)")
    ap.add_argument("--git", action="store_true",
                    help="use `git mv` so the move is staged")
    args = ap.parse_args()

    cands = find_legacy_candidates()
    print(f"Found {len(cands)} legacy candidates "
          f"(orphan witness + no importer + no audit cite):")
    for script, witness, derivation in cands:
        extra = f" (+{derivation.name})" if derivation else ""
        print(f"  {script.name} -> _deprecated/  [{witness.name}{extra}]")

    if not args.apply:
        print("\nDry run. Pass --apply to move files (add --git to stage).")
        return 0

    for script, witness, derivation in cands:
        move_one(script, witness, derivation, use_git=args.git)
    print(f"\nMoved {len(cands)} script(s) and their witness sidecars "
          f"to {DEPRECATED_DIR.relative_to(REPO_ROOT)}/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
