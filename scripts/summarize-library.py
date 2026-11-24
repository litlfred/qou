#!/usr/bin/env python3
"""
summarize-library — two-tier, token-budgeted summaries for every library
document, plus the scan index and the contextual-retrieval injection.

## The problem this solves

`library/*/sections/` is 24.7 M characters. Grep finds a hit in it, but an
agent deciding *which* of 341 documents to open has nothing cheap to read:
the choice costs either a title (too little) or a whole paper (too much).
Retrieval systems solve this with a summary tier; this builds one.

## Three tiers, chosen by what a reader is doing

| Tier | Size | Where | For |
|---|---|---|---|
| **brief** | ≤ 200 chars (~50 tok) | `library/INDEX.md`, one line each | scanning all 341 at once — the whole index is ~17 k tokens |
| **extended** | ~1.5–2.5 k chars (~500 tok) | `narrative` of `library/<id>/manifest.jsonld` | deciding whether to open this document |
| **sections** | the full text | `library/<id>/sections/*.md` | actually reading it |

An agent walks down the tiers and stops when it knows enough, so the cost
of *not* opening a document is one line rather than one paper.

## Contextual retrieval

Each section file gets the document's brief injected into its YAML
front-matter. This is the contextual-retrieval technique (Anthropic,
2024): a chunk retrieved in isolation otherwise loses the context that
makes it interpretable — "the trace is 1.585" means nothing without
knowing which paper and which object. Adding document context *to the
chunk itself* is what makes an isolated grep hit usable, and it costs one
line per section.

## Extractive, not abstractive — and that is a real limit

Every summary here is assembled mechanically from the document's own
abstract, section titles and extracted claims. Nothing is written by a
model. That makes it free, deterministic, and regenerable — and it means
a brief is only as good as the abstract it came from. A document whose
abstract did not extract gets a structural brief instead ("N sections
covering X, Y, Z"), which is weaker.

An LLM-written summary would be better and is a per-document upgrade, not
a replacement: each summary records who drafted it (`drafted_by`), so an
agent- or human-written summary can be dropped in and will not be
overwritten by a re-run. Only a summary this script drafted
(`drafted_by.kind == "script"`) is ever rebuilt.

## Where the summaries live: the document's own KG node

Since 2026-11-24 each document's summary is the `narrative` of its library
entry's KG node, `library/<doc-id>/manifest.jsonld`: a `NarrativeSchema`
record (`text`, `lang`, `state`, `drafted_by`, `drafted_at`), the platform's
form for an account of a library component, reviewed through
`bun run cat narratives` like an image description or a block summary. The
`text` is the brief, a blank line, then the extended summary, so the brief is
its first paragraph.

Until then they were `library/<doc-id>/summary.json` (`library-summary/v1`),
a file the platform's library gate (`check:l1-complete`) does not allow in an
entry. Owner, 2026-11-24 (PR #9399): summaries "should be like ingested KG
for library components in other parts of the harness". The old records'
`sections` and `tokens` are derived here from `structure.json`; their
`provenance.from` / `note` were not carried (git history keeps them).

Usage, tier 2: `scripts/summarize-library.py --show <doc-id>`, or
`jq -r ".narrative[0].text" library/<doc-id>/manifest.jsonld`.

Usage:
    scripts/summarize-library.py --apply            # missing/changed summaries + index + injection (preserves existing)
    scripts/summarize-library.py --only-missing     # explicit alias: generate only missing/changed summaries + update index
    scripts/summarize-library.py --apply --regenerate  # rebuild all extractive summaries (still keeps provenance.kind == 'agent')
    scripts/summarize-library.py --index-only
    scripts/summarize-library.py --check            # exit 1 if stale
    scripts/summarize-library.py --show <doc-id>    # tier 2 for one document
"""

from __future__ import annotations

import argparse
import datetime
import glob
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(REPO, "library")
INDEX = os.path.join(LIB, "INDEX.md")

SCHEMA = "library-summary/v1"
BRIEF_MAX = 200
EXTENDED_MAX = 2400

# chars/4 is the usual rough token heuristic; exact enough for budgeting.
tok = lambda s: max(1, len(s) // 4)


def first_sentences(text: str, limit: int) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if not text:
        return ""
    out = ""
    for s in re.split(r"(?<=[.!?])\s+", text):
        if len(out) + len(s) + 1 > limit:
            break
        out = (out + " " + s).strip()
    return out or text[:limit].rsplit(" ", 1)[0]


def build(docdir: str) -> dict | None:
    sj = os.path.join(docdir, "structure.json")
    if not os.path.exists(sj):
        return None
    try:
        art = json.load(open(sj))
    except Exception:
        return None
    # A container holds other documents; a duplicate is another copy of one
    # already in the index. Neither should occupy its own index line — the
    # point of the scan tier is one line per *work*.
    if art.get("container") or art.get("duplicate_of"):
        return None

    doc_id = art.get("doc_id") or os.path.basename(docdir)
    md = art.get("metadata") or {}
    title = (md.get("title") or "").strip()
    authors = (md.get("authors_raw") or "").strip()
    abstract = (md.get("abstract") or "").strip()
    secs = art.get("sections") or []
    pages = art.get("source", {}).get("pages")

    # ---- brief -------------------------------------------------------
    # Strip journal furniture that leaked into the extracted title. AGT
    # and Geometry & Topology print an ISSN banner and the opening page
    # number above the title, and those led ~10 index lines instead of the
    # paper's name. Cut everything up to the banner; if nothing survives,
    # the abstract carries the brief on its own.
    head = re.sub(
        r"^\s*ISSN[^A-Za-z]*[\d\-]+\s*\((?:on[- ]?line|printed)\)"
        r"(?:\s*[\d\-]+\s*\((?:on[- ]?line|printed)\))?\s*\d*\s*",
        "", title or "", flags=re.I,
    ).strip()
    head = re.sub(r"^(?:Vol(?:ume)?\.?\s*\d+[^A-Za-z]{0,12})", "", head).strip()
    head = head or doc_id if not abstract else head
    if abstract:
        gist = first_sentences(abstract, BRIEF_MAX - len(head) - 3)
        brief = f"{head} — {gist}" if (gist and head) else (gist or head or doc_id)
    else:
        names = [s.get("title", "") for s in secs if s.get("title")][:3]
        tail = "; ".join(n[:34] for n in names)
        brief = f"{head} — {len(secs)} sections" + (f": {tail}" if tail else "")
    brief = re.sub(r"\s+", " ", brief)[:BRIEF_MAX].rstrip(" ,;:-—")

    # ---- key claims from the Stage-B extraction ----------------------
    claims = []
    cj = os.path.join(docdir, "candidates.json")
    if os.path.exists(cj):
        try:
            cand = json.load(open(cj)).get("candidates", [])
        except Exception:
            cand = []
        rank = {"theorem": 0, "proposition": 1, "definition": 2, "corollary": 3, "lemma": 4}
        cand = sorted((c for c in cand if c.get("kind") in rank),
                      key=lambda c: rank[c["kind"]])
        for c in cand[:6]:
            n = f" {c['number']}" if c.get("number") else ""
            claims.append(f"{c['kind'].title()}{n}: {first_sentences(c.get('statement',''), 180)}")

    # ---- extended ----------------------------------------------------
    parts = [f"**{title or doc_id}**"]
    if authors:
        parts.append(f"*{authors[:120]}*")
    if pages:
        parts.append(f"{pages} pp, {len(secs)} sections.")
    if abstract:
        parts.append("**Abstract.** " + first_sentences(abstract, 900))
    outline = [f"{(s.get('number') or '').strip()} {s.get('title','')}".strip()
               for s in secs if s.get("title")]
    if outline:
        parts.append("**Outline.** " + "; ".join(o[:46] for o in outline[:18]))
    if claims:
        parts.append("**Extracted claims (proposals, not verified).**\n" +
                     "\n".join("- " + c for c in claims))
    extended = "\n\n".join(parts)[:EXTENDED_MAX]

    return {
        "_schema": SCHEMA,
        "doc_id": doc_id,
        "source_sha256": art.get("source", {}).get("sha256", "")[:16],
        "brief": brief,
        "extended": extended,
        "tokens": {"brief": tok(brief), "extended": tok(extended)},
        "sections": [
            {"id": s.get("id"), "title": s.get("title"),
             "pages": f"{s.get('page_start')}-{s.get('page_end')}"}
            for s in secs
        ],
        "provenance": {
            "kind": "extractive",
            "from": [k for k, v in (("abstract", abstract), ("section-titles", outline),
                                    ("candidates", claims)) if v],
            "note": "Assembled mechanically from the document's own text. Replace "
                    "`kind` with 'agent' to protect a hand-written summary from "
                    "regeneration.",
        },
    }


def inject_context(docdir: str, brief: str, duplicate_of: str = "") -> int:
    """Contextual retrieval: put the document brief in each chunk.

    Duplicate copies get this too. They keep their sections on disk and
    stay greppable, so a hit landing in one needs the same context as any
    other — plus a pointer saying which copy is canonical, otherwise the
    reader has no way to tell they are looking at the second of two.
    """
    n = 0
    for f in sorted(glob.glob(os.path.join(docdir, "sections", "*.md"))):
        raw = open(f, encoding="utf-8", errors="replace").read()
        if not raw.startswith("---\n"):
            continue
        end = raw.find("\n---\n", 4)
        if end == -1:
            continue
        fm, body = raw[4:end], raw[end + 5:]
        fm = "\n".join(l for l in fm.splitlines()
                       if not l.startswith(("doc_brief:", "duplicate_of:")))
        esc = brief.replace('"', "'")
        fm += f'\ndoc_brief: "{esc}"'
        if duplicate_of:
            fm += f'\nduplicate_of: "{duplicate_of}"'
        new_raw = "---\n" + fm + "\n---\n" + body
        if new_raw != raw:
            open(f, "w", encoding="utf-8").write(new_raw)
            n += 1
    return n


def write_index(rows: list[dict]) -> str:
    rows = sorted(rows, key=lambda r: r["doc_id"])
    total = sum(r["tokens"]["brief"] for r in rows)
    out = [
        "# Library index — one line per document",
        "",
        "Generated by `scripts/summarize-library.py`. Regenerate, do not edit.",
        "",
        f"**{len(rows)} documents, ~{total:,} tokens for the whole index.** This is the",
        "scan tier: grep *this file* to find which document to open, rather than",
        "grepping 24.7 M characters of section text. Then read",
        "`scripts/summarize-library.py --show <doc-id>` (the `narrative` of",
        "`library/<doc-id>/manifest.jsonld`) for the extended summary, and only then",
        "`library/<doc-id>/sections/` for the text.",
        "",
        "Briefs are **extractive** — assembled from each document's own abstract,",
        "section titles and extracted claims, with nothing written by a model. A",
        "brief is therefore only as good as the abstract it came from; documents",
        "whose abstract did not extract get a structural brief instead.",
        "",
        "| doc-id | brief |",
        "|---|---|",
    ]
    for r in rows:
        b = r["brief"].replace("|", "\\|")
        out.append(f"| [`{r['doc_id']}`]({r['doc_id']}/) | {b} |")
    out.append("")
    return "\n".join(out)


MANIFEST = "manifest.jsonld"


def manifest_of(docdir: str) -> dict | None:
    """The entry's KG node, or None when it has none (or it will not parse)."""
    path = os.path.join(docdir, MANIFEST)
    try:
        return json.load(open(path, encoding="utf-8"))
    except Exception:
        return None


def english(slot) -> dict | None:
    """The English narrative of a slot (a list, one per language), else the first."""
    if isinstance(slot, dict):
        return slot if slot.get("text") else None
    if isinstance(slot, list) and slot:
        return next((n for n in slot if isinstance(n, dict) and n.get("lang") == "en"), slot[0])
    return None


def row_from_narrative(doc_id: str, docdir: str, nar: dict) -> dict:
    """An index row from the manifest's `narrative`: brief = first paragraph."""
    text = (nar.get("text") or "").strip()
    brief, _, extended = text.partition("\n\n")
    sj = os.path.join(docdir, "structure.json")
    try:
        secs = (json.load(open(sj)).get("sections") or []) if os.path.exists(sj) else []
    except Exception:
        secs = []
    return {
        "doc_id": doc_id,
        "brief": brief,
        "extended": extended,
        "tokens": {"brief": tok(brief), "extended": tok(extended)},
        "sections": [
            {"id": s.get("id"), "title": s.get("title"),
             "pages": f"{s.get('page_start')}-{s.get('page_end')}"}
            for s in secs
        ],
        "drafted_by": nar.get("drafted_by"),
        "state": nar.get("state"),
    }


def write_narrative(docdir: str, s: dict) -> bool:
    """Set the manifest's `narrative` to this script's draft of `s`, in place.

    The key goes after `provenance`; every other field and the file's
    formatting (2-space JSON, trailing newline, as gen-library-jsonld writes
    it) are kept. Returns False when the entry has no manifest to carry it.
    """
    path = os.path.join(docdir, MANIFEST)
    man = manifest_of(docdir)
    if man is None:
        return False
    nar = [{
        "text": s["brief"].strip() + "\n\n" + s["extended"].strip(),
        "lang": "en",
        "state": "draft",
        "drafted_by": {"kind": "script", "id": "scripts/summarize-library.py"},
        "drafted_at": datetime.date.today().isoformat(),
    }]  # a list, one per language: the platform's narrative slot (NarrativeSlotSchema)
    out: dict = {}
    for k, v in man.items():
        if k == "narrative":
            continue
        out[k] = v
        if k == "provenance":
            out["narrative"] = nar
    out.setdefault("narrative", nar)
    open(path, "w", encoding="utf-8").write(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    return True


def show(doc_id: str) -> int:
    """Tier 2 for one document: its brief, extended summary and who drafted it."""
    d = os.path.join(LIB, doc_id)
    man = manifest_of(d)
    nar = english((man or {}).get("narrative"))
    if not nar:
        print(f"{doc_id}: no summary (library/{doc_id}/{MANIFEST} carries no `narrative`)", file=sys.stderr)
        return 1
    r = row_from_narrative(doc_id, d, nar)
    by = r["drafted_by"] or {}
    print(r["brief"] + "\n\n" + r["extended"])
    print(f"\n[{r['state']}, drafted by {by.get('kind')} {by.get('id')}"
          + (f", {by['session']}" if by.get("session") else "") + "]")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Two-tier summaries + scan index for the library")
    ap.add_argument("--apply", action="store_true",
                    help="write missing/stale summaries (each entry's manifest.jsonld `narrative`), inject changed doc_brief headers, and update INDEX.md")
    ap.add_argument("--only-missing", action="store_true",
                    help="write only missing/stale summaries (default behavior of --apply; implies --apply)")
    ap.add_argument("--regenerate", action="store_true",
                    help="rebuild this script's own summaries as well (one drafted by an agent or a person is always preserved)")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--index-only", action="store_true")
    ap.add_argument("--no-inject", action="store_true", help="skip front-matter context injection")
    ap.add_argument("--show", metavar="DOC_ID", help="print one document's summary (tier 2) and exit")
    args = ap.parse_args()
    if args.show:
        return show(args.show)
    if args.only_missing:
        args.apply = True

    rows, injected, kept, preserved_extractive = [], 0, 0, 0
    dup_dirs: list[tuple[str, str]] = []
    for d in sorted(glob.glob(os.path.join(LIB, "*"))):
        if not os.path.isdir(d):
            continue
        sj_path = os.path.join(d, "structure.json")
        try:
            art_meta = json.load(open(sj_path)) if os.path.exists(sj_path) else {}
        except Exception:
            art_meta = {}
        if art_meta.get("container"):
            continue
        dup = art_meta.get("duplicate_of")
        if dup:
            dup_dirs.append((d, dup))
            continue
        expected_doc_id = art_meta.get("doc_id") or os.path.basename(d)
        expected_sha = (art_meta.get("source") or {}).get("sha256", "")
        man = manifest_of(d)
        nar = english((man or {}).get("narrative"))
        if nar and nar.get("text"):
            prev = row_from_narrative(expected_doc_id, d, nar)
            if (nar.get("drafted_by") or {}).get("kind") != "script":
                # Written by an agent or a person: never rebuilt. Ensure its
                # brief is present in chunks (`inject_context` is a no-op when
                # sections are already current).
                rows.append(prev)
                kept += 1
                if args.apply and not args.index_only and not args.no_inject:
                    injected += inject_context(d, prev.get("brief", ""))
                continue
            if (not args.regenerate
                    and ((man or {}).get("meta") or {}).get("source_sha256") == expected_sha
                    and prev.get("brief")):
                # Preserve this script's existing summary while the manifest
                # still describes the same source bytes, so ingesting one new
                # paper does not clobber ~740 existing entries (`qou-pmgw`).
                # Pass `--regenerate` when extractor rules change.
                rows.append(prev)
                preserved_extractive += 1
                if args.apply and not args.index_only and not args.no_inject:
                    injected += inject_context(d, prev.get("brief", ""))
                continue
        s = build(d)
        if not s:
            continue
        rows.append(s)
        if args.apply and not args.index_only:
            if not write_narrative(d, s):
                print(f"  {os.path.basename(d)}: no {MANIFEST} to carry its summary; "
                      "run gen-library-jsonld for the entry first", file=sys.stderr)
            if not args.no_inject:
                injected += inject_context(d, s["brief"])

    # Duplicate copies carry the canonical's brief so a grep hit inside one
    # is still interpretable, and a `duplicate_of` line so the reader knows
    # to prefer the other copy. They get no index line of their own.
    by_id = {r["doc_id"]: r for r in rows}
    dup_injected = 0
    if args.apply and not args.index_only and not args.no_inject:
        for d, canon in dup_dirs:
            src = by_id.get(canon)
            if src:
                dup_injected += inject_context(d, src["brief"], duplicate_of=canon)

    idx = write_index(rows)
    stale = (not os.path.exists(INDEX)) or open(INDEX, encoding="utf-8").read() != idx
    if args.apply or args.index_only:
        open(INDEX, "w", encoding="utf-8").write(idx)

    bt = sum(r["tokens"]["brief"] for r in rows)
    et = sum(r["tokens"]["extended"] for r in rows)
    print(f"{len(rows)} documents ({kept} agent- or person-written kept, {preserved_extractive} existing extractive preserved)")
    print(f"  index (scan tier)   ~{bt:,} tokens total")
    print(f"  extended summaries  ~{et:,} tokens total, ~{et//max(len(rows),1)} each")
    if injected:
        print(f"  contextual retrieval: doc_brief injected into {injected} section files")
    if dup_injected:
        print(f"  duplicate copies: canonical brief + duplicate_of into {dup_injected} sections "
              f"across {len(dup_dirs)} copies (no index line of their own)")
    if args.check:
        print("\nindex is", "STALE" if stale else "up to date")
        return 1 if stale else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
