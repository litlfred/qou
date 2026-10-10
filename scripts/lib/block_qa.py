"""Where Python scripts read and write a block's QA verdict, after the split.

Issue #7642, owner ruling 2026-10-10. Block QA is split the way the platform
splits it:

* the DERIVED report (``block-qa/v1``) is at
  ``test/results/block-qa/<repo-relative block root>.qa.json``. That directory
  is gitignored; its durable copy is the ``cat/cat-harness/qa-reports`` branch,
  keyed by commit. Fetch it with
  ``bun run folio-assistant/cat-harness/scripts/qa-store.ts fetch --ref main``;
* the JUDGEMENTS (entries whose ``reviewer.kind`` is not ``script``) are in
  ``test/attestations/block-qa/<same mirror>.attestations.json``, on main.

This module is the Python face of ``folio/pipeline/block-qa-io.ts``. READ
paths follow the platform's rule from ``qa-paths.ts``: the results tree first,
then the legacy sibling. WRITES are not reimplemented here; they shell out to
``block-qa-io.ts save``, which writes the judgement half to the attestation
store with the platform's ``resolvePrior`` + ``finalizeCriteria``. So there is
one writer, not two that can drift apart.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Iterator

REPO = Path(__file__).resolve().parents[2]
RESULTS_DIR = REPO / "test" / "results" / "block-qa"
ATTESTATIONS_DIR = REPO / "test" / "attestations" / "block-qa"
SUFFIX = ".qa.json"
_IO = REPO / "folio" / "pipeline" / "block-qa-io.ts"

FETCH_HINT = (
    "no block-QA results tree in this checkout (test/results/block-qa is empty). "
    "Fetch it first: bun run folio-assistant/cat-harness/scripts/qa-store.ts fetch --ref main"
)


def block_root_of(p: str | os.PathLike) -> Path:
    """``foo.md`` / ``foo.ts`` / ``foo.qa.json`` / results-tree path / ``foo`` -> absolute block root."""
    a = Path(p).resolve()
    s = str(a)
    for ext in (SUFFIX, ".md", ".ts", ".lean"):
        if s.endswith(ext):
            s = s[: -len(ext)]
            break
    a = Path(s)
    try:
        rel = a.relative_to(RESULTS_DIR)
    except ValueError:
        return a
    return REPO / rel


def results_path(block_root: str | os.PathLike) -> Path:
    """Where a NEW derived report for this block lives (never the sibling)."""
    root = block_root_of(block_root)
    return RESULTS_DIR / (str(root.relative_to(REPO)) + SUFFIX)


def legacy_path(block_root: str | os.PathLike) -> Path:
    return Path(str(block_root_of(block_root)) + SUFFIX)


def attestation_path(block_root: str | os.PathLike) -> Path:
    root = block_root_of(block_root)
    return ATTESTATIONS_DIR / (str(root.relative_to(REPO)) + ".attestations.json")


def read_path(block_root: str | os.PathLike) -> Path | None:
    """The report to READ: the results tree, else the legacy sibling, else ``None``."""
    for p in (results_path(block_root), legacy_path(block_root)):
        if p.exists():
            return p
    return None


def results_tree_present() -> bool:
    return RESULTS_DIR.is_dir() and any(RESULTS_DIR.iterdir())


def warn_if_unfetched(prog: str) -> bool:
    """Print a loud warning and return False when there is no results tree.

    An empty tree is "unknown", never "clean". A reader that saw no reports
    would otherwise report the corpus as passing.
    """
    if results_tree_present():
        return True
    print(f"{prog}: WARNING {FETCH_HINT}", file=sys.stderr)
    return False


def iter_reports(under: str | os.PathLike = "folio") -> Iterator[tuple[Path, Path]]:
    """Every block report under ``under`` (repo-relative or absolute), as
    (block root, report path). A results-tree report shadows a legacy sibling
    for the same block, which is the platform's read rule."""
    base = Path(under)
    if not base.is_absolute():
        base = REPO / base
    base = base.resolve()
    seen: dict[Path, Path] = {}
    rbase = RESULTS_DIR / base.relative_to(REPO)
    if rbase.exists():
        for p in sorted(rbase.rglob("*" + SUFFIX)):
            if p.name.endswith(".script-qa.json"):
                continue
            seen[block_root_of(p)] = p
    if base.exists():
        for p in sorted(base.rglob("*" + SUFFIX)):
            if p.name.endswith(".script-qa.json") or "node_modules" in p.parts:
                continue
            seen.setdefault(block_root_of(p), p)
    for root in sorted(seen):
        yield root, seen[root]


def load(block_root: str | os.PathLike) -> dict | None:
    p = read_path(block_root)
    if p is None:
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def save(block_root: str | os.PathLike, report: dict, mode: str = "attesting") -> Path:
    """Save through ``block-qa-io.ts``: the judgements go to the attestation
    store and are read back, then the derived projection is written. Raises on
    a refusal, in which case nothing was written."""
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False)
        tmp = f.name
    try:
        r = subprocess.run(
            ["bun", str(_IO), "save", str(block_root_of(block_root)), tmp, "--mode", mode],
            cwd=REPO, capture_output=True, text=True,
        )
    finally:
        os.unlink(tmp)
    if r.returncode != 0:
        raise RuntimeError(f"block-qa-io save refused for {block_root}: {r.stderr.strip() or r.stdout.strip()}")
    return Path(r.stdout.strip())
