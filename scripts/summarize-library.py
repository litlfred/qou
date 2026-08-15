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
| **extended** | ~1.5–2.5 k chars (~500 tok) | `library/<id>/summary.json` | deciding whether to open this document |
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
a replacement: `summary.json` records `provenance.kind`, so an
agent-written summary can be dropped in and will not be overwritten by a
re-run (`--keep-agent`, the default).

Usage:
    scripts/summarize-library.py --apply            # summaries + index + injection
    scripts/summarize-library.py --index-only
    scripts/summarize-library.py --check            # exit 1 if stale
"""

from __future__ import annotations

import argparse
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
    if art.get("container"):
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


def inject_context(docdir: str, brief: str) -> int:
    """Contextual retrieval: put the document brief in each chunk."""
    n = 0
    for f in sorted(glob.glob(os.path.join(docdir, "sections", "*.md"))):
        raw = open(f, encoding="utf-8", errors="replace").read()
        if not raw.startswith("---\n"):
            continue
        end = raw.find("\n---\n", 4)
        if end == -1:
            continue
        fm, body = raw[4:end], raw[end + 5:]
        fm = "\n".join(l for l in fm.splitlines() if not l.startswith("doc_brief:"))
        esc = brief.replace('"', "'")
        fm += f'\ndoc_brief: "{esc}"'
        open(f, "w", encoding="utf-8").write("---\n" + fm + "\n---\n" + body)
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
        "`library/<doc-id>/summary.json` for the extended summary, and only then",
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


def main() -> int:
    ap = argparse.ArgumentParser(description="Two-tier summaries + scan index for the library")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--index-only", action="store_true")
    ap.add_argument("--no-inject", action="store_true", help="skip front-matter context injection")
    args = ap.parse_args()

    rows, injected, kept = [], 0, 0
    for d in sorted(glob.glob(os.path.join(LIB, "*"))):
        if not os.path.isdir(d):
            continue
        path = os.path.join(d, "summary.json")
        if os.path.exists(path):
            try:
                prev = json.load(open(path))
            except Exception:
                prev = {}
            if (prev.get("provenance") or {}).get("kind") == "agent":
                # Keep the summary, but still push its brief into the chunks:
                # an agent-written brief is the one most worth having there,
                # and an earlier version of this skipped injection along with
                # regeneration, leaving the best briefs out of the sections
                # that most needed them.
                rows.append(prev)
                kept += 1
                if args.apply and not args.index_only and not args.no_inject:
                    injected += inject_context(d, prev.get("brief", ""))
                continue
        s = build(d)
        if not s:
            continue
        rows.append(s)
        if args.apply and not args.index_only:
            json.dump(s, open(path, "w"), indent=1, ensure_ascii=False)
            if not args.no_inject:
                injected += inject_context(d, s["brief"])

    idx = write_index(rows)
    stale = (not os.path.exists(INDEX)) or open(INDEX, encoding="utf-8").read() != idx
    if args.apply or args.index_only:
        open(INDEX, "w", encoding="utf-8").write(idx)

    bt = sum(r["tokens"]["brief"] for r in rows)
    et = sum(r["tokens"]["extended"] for r in rows)
    print(f"{len(rows)} documents ({kept} agent-written kept)")
    print(f"  index (scan tier)   ~{bt:,} tokens total")
    print(f"  extended summaries  ~{et:,} tokens total, ~{et//max(len(rows),1)} each")
    if injected:
        print(f"  contextual retrieval: doc_brief injected into {injected} section files")
    if args.check:
        print("\nindex is", "STALE" if stale else "up to date")
        return 1 if stale else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
