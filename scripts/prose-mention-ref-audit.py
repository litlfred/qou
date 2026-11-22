#!/usr/bin/env python3
"""Report-only audit: named objects in a block's prose that the reader was never pointed to.

Bean ``qou-noj1`` (owner ask, 2026-07-07; owner chose "report-only" 2026-11-15).

The detangler sees only the ``uses[]`` DAG, so a forward reference that lives in
prose alone is invisible to it. Worked case: ``ex:vacuum-state-su2`` (chapter
"Lifting and Descent") has a paragraph headed "Bring's surface specialisation",
while ``def:brings-surface`` is introduced chapters later and is neither in the
block's ``uses[]`` nor linked inline.

What this script does
---------------------
1. Builds a term index from the corpus itself: the titles of ``definition``
   blocks, each block's ``defines[]`` slugs, and ``glossary.json`` narrative
   terms. Each term points at the block that introduces it.
2. Orders every block by its position in the paper (paper manifest ->
   chapter manifest -> section ``blocks``).
3. For every block's ``.md``, strips math, code, inline links and
   ``:defterm``/``:refterm`` directives, and searches the remaining prose for
   indexed terms.
4. Classifies each unlinked mention:

   * ``forward``     -- the term is introduced *later* in the paper and the
                        block neither lists it in ``uses[]``/``interprets`` nor
                        links it. The reader meets it before its definition.
                        This is the finding the bean asks for.
   * ``undeclared``  -- introduced *earlier*, but not in ``uses[]`` and not
                        linked. Advisory: "introduced before use" holds, so
                        this is a completeness hint, not a defect.

What this script does NOT do (by owner ruling, bean ``fwr10``, 2026-08-10)
------------------------------------------------------------------------
It never edits a block and never proposes a ``uses[]`` edge. A prose mention is
a weaker claim than "the reader must read that first" -- bean ``fwr5`` rejected
2 of 8 such candidates as related-but-not-dependent. The output ranks blocks for
a human reading; it is not a source to populate ``uses[]`` from.

Known limits, so a clean result is not over-read:
* Terms of one word are skipped (too noisy: "mass", "trace"); a forward
  reference to a single-word concept is invisible here.
* Matching is case-insensitive on whole words after stripping; paraphrases and
  plurals other than a trailing "s" are not matched.
* Titles of non-``definition`` blocks are not indexed.

Usage::

    python3 scripts/prose-mention-ref-audit.py                 # summary
    python3 scripts/prose-mention-ref-audit.py --json out.json # full list
    python3 scripts/prose-mention-ref-audit.py --block ex:vacuum-state-su2
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPER = ROOT / "folio" / "quantum-observable-universe"

BUILDER_RE = re.compile(r"export\s+default\s+(\w+)\s*\(")
LABEL_RE = re.compile(r"\blabel:\s*[\"']([^\"']+)[\"']")
TITLE_RE = re.compile(r"\btitle:\s*((?:[\"'][^\"']*[\"']\s*\+?\s*)+)", re.S)
INTERPRETS_RE = re.compile(r"\binterprets:\s*[\"']([^\"']+)[\"']")
ARRAY_RE = r"\b{key}:\s*\[(.*?)\]"
STR_RE = re.compile(r"[\"']([^\"']+)[\"']")


def _array(src: str, key: str) -> list[str]:
    m = re.search(ARRAY_RE.format(key=key), src, re.S)
    return STR_RE.findall(m.group(1)) if m else []


def _title(src: str) -> str:
    m = TITLE_RE.search(src)
    if not m:
        return ""
    return "".join(STR_RE.findall(m.group(1)))


def parse_block(ts: Path) -> dict | None:
    src = ts.read_text(encoding="utf-8", errors="replace")
    b = BUILDER_RE.search(src)
    lab = LABEL_RE.search(src)
    if not b or not lab:
        return None
    if b.group(1) in {"chapter", "paper", "section"}:
        return None
    interp = INTERPRETS_RE.search(src)
    return {
        "label": lab.group(1),
        "kind": b.group(1),
        "title": _title(src),
        "uses": _array(src, "uses"),
        "defines": _array(src, "defines"),
        "interprets": interp.group(1) if interp else None,
        "ts": ts,
        "md": ts.with_suffix(".md"),
    }


def paper_order() -> list[tuple[str, str]]:
    """Return (chapter_dir, block_stem) in reading order."""
    manifest = (PAPER / "quantum-observable-universe.ts").read_text()
    dirs = re.findall(r"dir:\s*[\"']([^\"']+)[\"']", manifest)
    order: list[tuple[str, str]] = []
    for d in dirs:
        ch = PAPER / d / f"{d}.ts"
        if not ch.exists():
            continue
        src = ch.read_text()
        for blk in re.finditer(r"\bblocks:\s*\[(.*?)\]", src, re.S):
            body = re.sub(r"//[^\n]*", "", blk.group(1))
            for stem in STR_RE.findall(body):
                order.append((d, stem))
    return order


MATH_RE = [
    re.compile(r"```.*?```", re.S),
    re.compile(r"\$\$.*?\$\$", re.S),
    re.compile(r"\$[^$\n]*\$"),
    re.compile(r"`[^`\n]*`"),
]
LINK_RE = re.compile(r"\[([^\]]*)\]\(#([^)\s]+)\)")
DIRECTIVE_RE = re.compile(r":(?:defterm|refterm)\[([^\]]*)\](?:\{#([^}]+)\})?")


def strip_prose(md: str) -> tuple[str, set[str], set[str]]:
    """Return prose with linked/marked spans blanked, linked labels, refterm slugs."""
    linked = {m.group(2) for m in LINK_RE.finditer(md)}
    slugs = set()
    for m in DIRECTIVE_RE.finditer(md):
        slugs.add((m.group(2) or m.group(1)).strip().lower())
    for rx in MATH_RE:
        md = rx.sub(" ", md)
    md = LINK_RE.sub(" ", md)
    md = DIRECTIVE_RE.sub(" ", md)
    md = re.sub(r"<[^>]+>", " ", md)
    return md, linked, slugs


# Back-matter reference chapters: a term "introduced" there (a Mathlib glossary
# wrapper, the notation register, the definition index) is a lookup aid, not the
# place a reader first meets the concept, so mentions of it are never forward.
REFERENCE_CHAPTERS = {"glossary", "index-of-definitions", "notation"}
# Preview chapters are allowed to look ahead (their own manifest comments say so),
# so forward mentions from them are counted apart and not listed as findings.
PREVIEW_CHAPTERS = {"introduction", "models-of-qous", "notation", "index-of-definitions"}

TRAILING = {"as", "of", "for", "in", "on", "and", "to", "via", "from", "with", "at", "by", "is"}
LEAD = re.compile(r"^(the|a|an)\s+", re.I)


def clean_term(t: str) -> str:
    t = re.sub(r"\$[^$]*\$", " ", t)
    t = re.sub(r"\([^)]*\)", " ", t)
    t = re.sub(r"[{}\\*_]", " ", t)
    t = t.split(":")[0].split("—")[0].split(" -- ")[0]
    t = LEAD.sub("", re.sub(r"\s+", " ", t).strip()).strip(" .,;").lower()
    # A title cut at a math span leaves a dangling connective ("substrate
    # parameter as $q$" -> "substrate parameter as"); drop it.
    while t.split() and t.split()[-1] in TRAILING:
        t = " ".join(t.split()[:-1])
    return t


def usable(term: str) -> bool:
    words = term.split()
    if not (2 <= len(words) <= 5):
        return False
    if any(len(w) < 2 for w in words):
        return False
    return bool(re.fullmatch(r"[a-z0-9'’\- ]+", term))


def build_index(blocks: dict[str, dict]) -> dict[str, str]:
    """term -> label of the block that introduces it."""
    index: dict[str, str] = {}
    ambiguous: set[str] = set()

    def add(term: str, label: str) -> None:
        term = clean_term(term)
        if not usable(term):
            return
        if term in index and index[term] != label:
            ambiguous.add(term)
        index.setdefault(term, label)

    for lab, b in blocks.items():
        if b["kind"] == "definition" and b["title"]:
            add(b["title"], lab)
        for slug in b["defines"]:
            add(slug.replace("-", " "), lab)
    gl = ROOT / "glossary.json"
    if gl.exists():
        for e in json.loads(gl.read_text()).get("entries", []):
            if e.get("latex_label") in blocks:
                add(e.get("narrative_term", ""), e["latex_label"])
    for t in ambiguous:
        index.pop(t, None)
    return index


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--json", help="write the full finding list here")
    ap.add_argument("--block", help="report one block label only")
    ap.add_argument("--top", type=int, default=25)
    args = ap.parse_args()

    blocks: dict[str, dict] = {}
    by_stem: dict[tuple[str, str], str] = {}
    for ts in PAPER.glob("*/*.ts"):
        b = parse_block(ts)
        if b:
            blocks[b["label"]] = b
            by_stem[(ts.parent.name, ts.stem)] = b["label"]

    pos: dict[str, int] = {}
    chap: dict[str, str] = {}
    for i, key in enumerate(paper_order()):
        lab = by_stem.get(key)
        if lab and lab not in pos:
            pos[lab] = i
            chap[lab] = key[0]

    index = build_index(blocks)
    patterns = {
        t: re.compile(r"(?<![\w-])" + re.escape(t).replace(r"\ ", r"\s+") + r"s?(?![\w-])", re.I)
        for t in index
    }

    findings = []
    for lab, b in blocks.items():
        if args.block and lab != args.block:
            continue
        if not b["md"].exists() or lab not in pos:
            continue
        prose, linked, slugs = strip_prose(b["md"].read_text(encoding="utf-8", errors="replace"))
        declared = set(b["uses"]) | linked | {b["interprets"]} | {lab}
        seen: set[str] = set()
        for term, target in index.items():
            if target in declared or target in seen or target not in pos:
                continue
            if term in slugs or term.replace(" ", "-") in slugs:
                continue
            m = patterns[term].search(prose)
            if not m:
                continue
            seen.add(target)
            line = prose[: m.start()].count("\n") + 1
            if chap[target] in REFERENCE_CHAPTERS:
                continue
            cls = "forward" if pos[target] > pos[lab] else "undeclared"
            if cls == "forward" and (
                chap[lab] in PREVIEW_CHAPTERS
                # A chapter or section intro announcing what the chapter will
                # define is a roadmap, not a forward dependency.
                or (lab.startswith(("sec:", "chap:")) and chap[target] == chap[lab])
            ):
                cls = "preview"
            findings.append({
                "block": lab,
                "file": str(b["md"].relative_to(ROOT)),
                "line": line,
                "term": term,
                "target": target,
                "class": cls,
                "gap": pos[target] - pos[lab],
            })

    fwd = [f for f in findings if f["class"] == "forward"]
    und = [f for f in findings if f["class"] == "undeclared"]
    pre = [f for f in findings if f["class"] == "preview"]
    print(f"blocks scanned: {len(pos)}   terms indexed: {len(index)}")
    print(f"forward (defined later, unlinked):   {len(fwd)} mentions in "
          f"{len({f['block'] for f in fwd})} blocks")
    print(f"undeclared (defined earlier, unlinked, not in uses[]): {len(und)} mentions in "
          f"{len({f['block'] for f in und})} blocks  [advisory]")
    print(f"preview (forward, but from a preview chapter or a same-chapter intro): {len(pre)}")
    print("\nREPORT ONLY. Never populate uses[] from this list (bean fwr10 ruling).")
    print(f"\nTop forward mentions by distance (of {len(fwd)}):")
    for f in sorted(fwd, key=lambda f: -f["gap"])[: args.top]:
        print(f"  {f['file']}:{f['line']}  \"{f['term']}\" -> {f['target']}  (+{f['gap']})")
    terms = Counter(f["term"] for f in fwd)
    print("\nMost frequent forward terms:")
    for t, n in terms.most_common(10):
        print(f"  {n:4d}  {t}")
    if args.json:
        Path(args.json).write_text(json.dumps({
            "schema": "prose-mention-ref-audit/v1",
            "report_only": True,
            "blocks_scanned": len(pos),
            "terms_indexed": len(index),
            "findings": findings,
        }, indent=2, ensure_ascii=False))
        print(f"\nwrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
