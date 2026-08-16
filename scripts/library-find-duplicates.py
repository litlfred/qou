#!/usr/bin/env python3
"""
library-find-duplicates — find documents that are the same work held twice.

Three pairs turned up by hand in one session: an arXiv copy beside its
published version (0306345v1 / agt-v3-n1-p17-p), a preprint beside its
journal form (ki52 / 104171-qt-83), and the same survey ingested under
two filenames (arxiv-2304.12545v1 / hyperbolicandneumann). Finding them
by hand is luck; this looks systematically.

## Why not a byte hash

Because it finds nothing here. Two downloads of one paper differ in
producer, timestamps and compression, and a preprint differs from its
published version in pagination and front matter while being the same
work. The `source.sha256` already recorded per document is exact-file
identity, which is a different and much weaker question.

## What it compares

The extracted *text*, which is version-stable in a way the bytes are not:

  * **head fingerprint** — the first 1,200 alphanumeric-normalised
    characters. Title, authors and abstract survive re-typesetting, so
    this is the strongest signal and it is cheap.
  * **head similarity** — the same normalised head compared by ratio, for
    copies whose banners differ. This is the load-bearing one: word
    shingles turned out to be **fragile to typesetting**. Masbaum's arXiv
    and AGT copies are the same 5,670 words and score Jaccard 0.09,
    because different line-breaking and hyphenation change every 5-word
    shingle while leaving the concatenated character stream intact.
  * **shingle Jaccard** — kept as a secondary signal for copies that
    diverge in the head (a preprint retitled on publication) but share
    body text.

Blocking keeps it from being quadratic in practice: pairs are only
scored when their normalised head shares a 40-character prefix, or when
their word counts are within 15 % of each other.

## What it does NOT do

It does not delete, merge or rewrite anything. Duplicate copies are
worth keeping — a citation may already point at either path — and which
copy is canonical is a judgement (usually: prefer the published one, or
the one carrying an arXiv id). Output is a report; acting on it is a
separate, deliberate step.

Usage:
    scripts/library-find-duplicates.py
    scripts/library-find-duplicates.py --threshold 0.55 --write-report
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
from difflib import SequenceMatcher
from itertools import combinations

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(REPO, "library")
REPORT = os.path.join(REPO, "docs", "audits", "2026-08-15-library-duplicates.md")

HEAD_CHARS = 1200
MAX_WORDS = 4000
SHINGLE = 5

WORD = re.compile(r"[a-z0-9]+")


def doc_text(docdir: str) -> str:
    """Section bodies, front-matter stripped."""
    parts = []
    for f in sorted(glob.glob(os.path.join(docdir, "sections", "*.md"))):
        try:
            raw = open(f, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        if raw.startswith("---\n"):
            end = raw.find("\n---\n", 4)
            if end != -1:
                raw = raw[end + 5:]
        parts.append(raw)
        if sum(len(p) for p in parts) > 400_000:
            break
    return " ".join(parts)


def fingerprint(docdir: str) -> dict | None:
    text = doc_text(docdir)
    words = WORD.findall(text.lower())
    if len(words) < 200:
        return None
    head = "".join(words)[:HEAD_CHARS]
    ws = words[:MAX_WORDS]
    shingles = {hash(" ".join(ws[i:i + SHINGLE])) for i in range(0, max(1, len(ws) - SHINGLE), 3)}
    return {
        "doc": os.path.basename(docdir),
        "head": head,
        "head_hash": hashlib.sha256(head.encode()).hexdigest()[:16],
        "shingles": shingles,
        "nwords": len(words),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Find same-work duplicates in the library")
    ap.add_argument("--threshold", type=float, default=0.55)
    ap.add_argument("--write-report", action="store_true")
    args = ap.parse_args()

    fps = []
    for d in sorted(glob.glob(os.path.join(LIB, "*"))):
        if not os.path.isdir(d):
            continue
        sj = os.path.join(d, "structure.json")
        try:
            if os.path.exists(sj) and json.load(open(sj)).get("container"):
                continue
        except Exception:
            pass
        f = fingerprint(d)
        if f:
            fps.append(f)
    print(f"fingerprinted {len(fps)} documents")

    # Exact head match first — the strongest, cheapest signal.
    by_head: dict[str, list[str]] = {}
    for f in fps:
        by_head.setdefault(f["head_hash"], []).append(f["doc"])
    exact = [v for v in by_head.values() if len(v) > 1]

    # Then blocked pairwise Jaccard for the rest.
    seen = {tuple(sorted(g)) for g in exact}
    near = []
    for a, b in combinations(fps, 2):
        if tuple(sorted((a["doc"], b["doc"]))) in seen:
            continue
        if a["head"][:40] != b["head"][:40]:
            lo, hi = sorted((a["nwords"], b["nwords"]))
            if hi == 0 or lo / hi < 0.85:
                continue
        # Head similarity first: robust to re-typesetting because the head
        # is a concatenated character stream with no word boundaries.
        hs = SequenceMatcher(None, a["head"][:600], b["head"][:600]).ratio()
        # Longest common prefix, which is what actually survives when two
        # copies are sectioned differently. Masbaum's two copies open with
        # 70 identical normalised characters and then diverge because one
        # extraction orders its sections differently — whole-head ratio
        # scores that 0.458, a shared prefix scores it correctly. 60 chars
        # is roughly ten words of identical opening text.
        lcp = 0
        for x, y in zip(a["head"], b["head"]):
            if x != y:
                break
            lcp += 1
        inter = len(a["shingles"] & b["shingles"])
        j = inter / len(a["shingles"] | b["shingles"]) if inter else 0.0
        prefix_score = min(1.0, lcp / 120) if lcp >= 60 else 0.0
        score = max(hs, j, prefix_score)
        if score >= args.threshold:
            how = "prefix" if prefix_score >= max(hs, j) else ("head" if hs >= j else "shingle")
            near.append((round(score, 3), a["doc"], b["doc"], how))
    near.sort(reverse=True)

    print(f"\nexact same-text groups: {len(exact)}")
    for g in exact:
        print("   " + "  ==  ".join(g))
    print(f"\nnear-duplicates (Jaccard >= {args.threshold}): {len(near)}")
    for j, a, b, how in near:
        print(f"   {j:.3f} [{how:>7}]  {a[:34]:<34} {b[:34]}")

    if args.write_report:
        out = [
            "# Library duplicates — same work held more than once",
            "",
            "Generated by `scripts/library-find-duplicates.py`. Regenerate, do not edit.",
            "",
            "Compares extracted **text**, not bytes: two downloads of one paper differ in",
            "producer and compression, and a preprint differs from its published version in",
            "pagination, so `source.sha256` (exact-file identity) finds none of these.",
            "",
            "**Nothing here has been deleted or merged.** A duplicate copy is worth keeping —",
            "an existing citation may point at either path — and which copy is canonical is a",
            "judgement, usually the published one or the one carrying an arXiv id. This is a",
            "report; acting on it is a separate step.",
            "",
            f"## Exact same extracted text ({len(exact)} groups)",
            "",
        ]
        for g in exact:
            out.append("- " + " · ".join(f"[`{x}`](../../library/{x}/)" for x in g))
        out += ["", f"## Near-duplicates, score >= {args.threshold} ({len(near)})", "",
                "`head` = normalised character-stream similarity, robust to re-typesetting.",
                "`shingle` = 5-word Jaccard, which misses re-typeset copies entirely.",
                "`prefix` = longest identical opening character run, which is what survives",
                "when two copies are sectioned in a different order.",
                "", "| score | via | doc | doc |", "|---|---|---|---|"]
        for j, a, b, how in near:
            out.append(f"| {j:.3f} | {how} | [`{a}`](../../library/{a}/) | [`{b}`](../../library/{b}/) |")
        out.append("")
        os.makedirs(os.path.dirname(REPORT), exist_ok=True)
        open(REPORT, "w", encoding="utf-8").write("\n".join(out))
        print(f"\nwrote {REPORT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
