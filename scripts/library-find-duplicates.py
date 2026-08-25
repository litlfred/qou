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
    copies whose banners differ. Secondary: it fails whenever one copy's
    extraction leads with a table of contents and the other's with the
    abstract, which is common.
  * **character 12-grams, content-sampled** — the signal that actually
    works, and the one the threshold is set on. Every 12-character
    window of the normalised stream is kept when its own hash lands in
    a fixed residue class, so *which* windows are kept depends on their
    content rather than their offset. Two copies of one paper therefore
    keep the same windows even when one carries 700 words of extra
    front matter.

    Measured over the library: same-work pairs score **0.276–1.000**,
    known-different pairs (a paper and its sequel; a 40-page paper whose
    title is contained in a different 108-page one) score 0.038–0.079,
    and 946 random pairs have a median of 0.004 and a maximum of 0.063.
    The threshold sits at 0.15, between those.

Two approaches were tried here first and are recorded because both look
reasonable and both fail:

  * *Word shingles.* A 5-word shingle needs five consecutive words to
    survive re-typesetting, so the same paper in two typesettings scores
    0.016–0.048 — inside the random-pair range.
  * *Position-sampled* character grams, and *title containment* as a
    tie-breaker over them. Position sampling depresses true pairs to
    0.038 (offsets differ, so the samples do not line up), which forces
    the threshold down into the noise; the title tie-breaker then merged
    a paper with its sequel, and fired on one document whose extracted
    "title" was nothing but the journal name — which would have matched
    every Pacific J. Math paper in the library against every other.

Blocking keeps it from being quadratic in practice: pairs are only
scored when their normalised head shares a 40-character prefix or their
word counts are within 15 % of each other.

## What it does NOT do

It does not decide, delete, merge or rewrite anything — and it is not
reliable enough to be allowed to. Because the same-work and
different-work score ranges overlap, **every pair here needs a reading**;
verdicts go in `docs/audits/library-duplicate-ledger.json`, and
`library-resolve-duplicates.py` acts on that ledger rather than on this
output. Duplicate copies are kept on disk in any case: a citation may
already point at either path.

Usage:
    scripts/library-find-duplicates.py
    scripts/library-find-duplicates.py --json          # full doc-ids
    scripts/library-find-duplicates.py --write-report
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import re
import sys
from difflib import SequenceMatcher
from itertools import combinations

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(REPO, "library")
REPORT = os.path.join(REPO, "docs", "audits", "2026-08-15-library-duplicates.md")

HEAD_CHARS = 1200
CHAR_N = 12    # character n-gram width
CHAR_MOD = 24  # keep grams whose content hash lands in one residue class of this

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
    stream = "".join(words)
    head = stream[:HEAD_CHARS]
    # Selection by content hash, not by offset: both copies of a paper
    # keep the same windows even when one carries extra front matter.
    chargrams = {stream[i:i + CHAR_N] for i in range(0, max(1, len(stream) - CHAR_N))
                 if (hash(stream[i:i + CHAR_N]) & 0xffff) % CHAR_MOD == 0}
    return {
        "doc": os.path.basename(docdir),
        "head": head,
        "head_hash": hashlib.sha256(head.encode()).hexdigest()[:16],
        "chargrams": chargrams,
        "nwords": len(words),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Find same-work duplicates in the library")
    ap.add_argument("--threshold", type=float, default=0.15,
                    help="char-gram Jaccard floor; measured separation is "
                         "0.276 (same work) vs 0.079 (different work)")
    ap.add_argument("--write-report", action="store_true")
    ap.add_argument("--json", action="store_true",
                    help="emit full doc-ids as JSON; the human output truncates names")
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
    print(f"fingerprinted {len(fps)} documents", file=sys.stderr if args.json else sys.stdout)

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
        # Length blocking only, and loose: a preprint and its published
        # version legitimately differ by a lot (Ohtsuki's two copies are
        # 18k and 24k words, and a 0.85 ratio silently dropped that pair
        # even though it scores 0.28). Char-gram sets are small enough
        # that scoring nearly every pair is affordable.
        lo, hi = sorted((a["nwords"], b["nwords"]))
        if hi == 0 or lo / hi < 0.25:
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
        prefix_score = min(1.0, lcp / 120) if lcp >= 60 else 0.0
        ci = len(a["chargrams"] & b["chargrams"])
        cj = ci / len(a["chargrams"] | b["chargrams"]) if ci else 0.0
        # Char-grams and the head signals live on different scales — a
        # same-work pair scores 0.28+ in chars but ~1.0 in head ratio, so
        # they get their own thresholds rather than being max()'d into one
        # number that means different things depending on which won.
        if cj >= args.threshold:
            near.append((round(cj, 3), a["doc"], b["doc"], "chars"))
        elif max(hs, prefix_score) >= 0.55:
            how = "prefix" if prefix_score >= hs else "head"
            near.append((round(max(hs, prefix_score), 3), a["doc"], b["doc"], how))
    near.sort(reverse=True)

    if args.json:
        print(json.dumps({"exact": exact,
                          "near": [{"score": s, "a": a, "b": b, "via": h}
                                   for s, a, b, h in near]}, indent=1))
        return 0

    print(f"\nexact same-text groups: {len(exact)}")
    for g in exact:
        print("   " + "  ==  ".join(g))
    print(f"\nnear-duplicates (char-gram Jaccard >= {args.threshold}, or head/prefix >= 0.55): {len(near)}")
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
