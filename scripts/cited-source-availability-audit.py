#!/usr/bin/env python3
"""Which cited sources does this repo actually HOLD?

The corpus-grep checklist's fifth path is "the library" — an item can be open
in this corpus and settled in a paper we already hold, and that difference is
what separates deriving a result from re-deriving one. The path only works if
you can tell which sources are held. Nothing measured that, and the ledger
that records it had drifted in BOTH directions.

Three populations, joined:

  cited     `cites[]` on authored blocks (read from the generated `.jsonld`
            graph) plus `-- Ref: [key]` lines in `.lean` files.
  declared  `content/bib-qa-verifications.json`, the source ledger: each entry
            says `source.kind` is an `upload` (with a `file` path) or
            `external` (with a URL).
  held      what `library/` actually contains.

A key is REACHABLE when a source file for it exists on disk. Everything else
is reported by WHY it is not, because the four reasons need different fixes:

  ledger-external      declared unavailable. May be true, may be stale — this
                       script re-checks each one against `library/`.
  ledger-file-missing  declared an upload whose file is not there.
  ledger-absent        cited but never triaged at all.
  recovered            declared not-held, but IS in `library/`. A ledger bug,
                       and the one class that makes an agent re-derive a result
                       the repo could have cited.

It also reports the OPPOSITE gap, which nothing was measuring: a source that
is held and triaged but carries no bibliography key. It is in the repo and no
block can cite it, so it reads to the corpus exactly like a source we lack.

## What this does NOT claim

**"Not held" is a statement about this repo, never about the literature.** A
missing source is a thing to obtain or to cite externally; it is not evidence
against the work that cites it.

**The recovery pass is deliberately conservative and WILL under-report.** It
matches a DOI or arXiv id against the library's doc-id, and a reference title
against each document's OWN title (`manifest.jsonld`, else the summary brief)
at a 0.7 token-overlap threshold with stopwords dropped. A short generic title
("Quantum Groups") overlaps many documents at 1.0, so a match is offered as a
CANDIDATE and single-word-content titles are suppressed entirely. Confirming
one is an agent's call, not this script's — pass `--candidates` to see them.

Naming a *held* document as not-held is the expensive error (it sends an agent
off to re-derive), so the pass exists at all; naming an *unheld* one as held is
worse still, so it does not guess.

## Sentinel keys

`manuscript` (AGENTS.md §1: the key to use when no published reference exists)
and any key naming this folio itself are self-references, not sources. They
are excluded and counted separately rather than silently dropped.

Usage:
  scripts/cited-source-availability-audit.py                 # summary
  scripts/cited-source-availability-audit.py --list <class>  # one class, full
  scripts/cited-source-availability-audit.py --candidates    # recovery guesses
  scripts/cited-source-availability-audit.py --json OUT.json
  scripts/cited-source-availability-audit.py --min-cites 50  # only load-bearing

Exit 0 always: this reports a state, it does not gate. A cited-but-unheld
source is a research-provenance fact, not a build error.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LEDGER = REPO / "content" / "bib-qa-verifications.json"
LIBRARY = REPO / "library"
CONTENT = REPO / "content"

# Keys that are the folio talking about itself, not a source it could hold.
SELF_KEYS = {"manuscript", "leitner2026"}

STOPWORDS = {"the", "of", "and", "a", "an", "with", "in", "on", "for", "to", "its"}
TITLE_OVERLAP = 0.7


def norm_words(s: str) -> set[str]:
    return {w for w in re.sub(r"[^a-z0-9 ]+", " ", (s or "").lower()).split()
            if w not in STOPWORDS}


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")


def cited_keys() -> Counter:
    """Every bibliography key cited anywhere, with how often."""
    counts: Counter = Counter()
    for f in CONTENT.rglob("*.jsonld"):
        try:
            doc = json.loads(f.read_text())
        except Exception:
            continue
        for c in doc.get("cites") or []:
            if isinstance(c, str) and c.startswith("references/"):
                counts[c.split("/", 1)[1]] += 1
    # Lean cites in comments, which no graph sees. Note the option order:
    # `grep -- '-- Ref:'` makes a following `--include` a PATH, not a flag,
    # which silently searched the wrong files and reported 0 of 6221 lines.
    r = subprocess.run(
        ["grep", "-rhoE", "--include=*.lean", "-e", r"-- Ref: \[[^]]+\]", str(CONTENT)],
        capture_output=True, text=True,
    )
    for line in r.stdout.splitlines():
        if "[" in line:
            counts[line.split("[", 1)[1].rstrip("]")] += 1
    return counts


def load_ledger() -> tuple[dict, list]:
    """(bib-key -> entry, entries carrying NO bib key).

    Half the ledger has `id: null` — a held document that has been read and
    triaged but joined to no `references.ts` entry, so nothing in the corpus
    can cite it. Keying the whole file on `e["id"]` collapses all of those onto
    one `None`, which is how they stayed invisible.
    """
    if not LEDGER.exists():
        return {}, []
    entries = json.loads(LEDGER.read_text()).get("entries", [])
    keyed = {e["id"]: e for e in entries if isinstance(e.get("id"), str)}
    unkeyed = [e for e in entries if not isinstance(e.get("id"), str)]
    dups = sorted(k for k, n in Counter(
        e["id"] for e in entries if isinstance(e.get("id"), str)).items() if n > 1)
    if dups:
        print(f"  ledger has {len(dups)} DUPLICATE bib id(s) — a lookup keyed on id\n"
              f"  silently keeps one and discards the rest: {', '.join(dups[:8])}"
              + (" …" if len(dups) > 8 else "") + "\n")
    return keyed, unkeyed


def load_refs() -> dict:
    """Reference metadata, if `bun` can evaluate `references.ts`.

    Optional: without it the recovery pass is skipped and said to be skipped,
    rather than a clean run being reported as evidence of no recoveries.
    """
    script = REPO / "content" / "schema" / "references.ts"
    if not script.exists():
        return {}
    prog = (
        f'import {{ references }} from "{script}";\n'
        'console.log(JSON.stringify(references.map((r) => ({'
        ' id: r.id, title: r.title, DOI: r.DOI, URL: r.URL }))));\n'
    )
    tmp = REPO / ".cited-source-audit.tmp.ts"
    try:
        tmp.write_text(prog)
        r = subprocess.run(["bun", "run", str(tmp)], capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            return {}
        return {x["id"]: x for x in json.loads(r.stdout)}
    except Exception:
        return {}
    finally:
        tmp.unlink(missing_ok=True)


def library_index() -> tuple[dict, dict]:
    """(doc-id slug -> doc-id, doc-id -> its own title)."""
    by_slug, titles = {}, {}
    if not LIBRARY.is_dir():
        return by_slug, titles
    for p in sorted(LIBRARY.iterdir()):
        if not p.is_dir():
            continue
        by_slug[slug(p.name)] = p.name
        title = ""
        mf = p / "manifest.jsonld"
        if mf.exists():
            try:
                title = json.loads(mf.read_text()).get("title") or ""
            except Exception:
                pass
        if not title:
            sf = p / "summary.json"
            if sf.exists():
                try:
                    title = (json.loads(sf.read_text()).get("brief") or "")[:200]
                except Exception:
                    pass
        titles[p.name] = title
    return by_slug, titles


def recover(key: str, refs: dict, by_slug: dict, titles: dict) -> tuple[str | None, list]:
    """(confirmed doc-id, candidate matches). Only an id/DOI hit is confirmed."""
    r = refs.get(key) or {}
    if r.get("DOI"):
        c = slug(r["DOI"].split("/", 1)[-1])
        if c in by_slug:
            return by_slug[c], []
    m = re.search(r"arxiv\.org/abs/([\w.\-/]+)", r.get("URL") or "", re.I)
    if m:
        for c in (slug("arxiv-" + m.group(1)), slug(m.group(1))):
            if c in by_slug:
                return by_slug[c], []
    tw = norm_words(r.get("title") or "")
    # A one- or two-word title matches far too much to mean anything.
    if len(tw) < 3:
        return None, []
    cands = []
    for doc, dt in titles.items():
        dw = norm_words(dt)
        if not dw:
            continue
        ov = len(tw & dw) / len(tw)
        if ov >= TITLE_OVERLAP:
            cands.append((round(ov, 2), doc, dt[:70]))
    # An exact title match is as good as an id match; anything less is a guess.
    exact = [c for c in cands if c[0] == 1.0 and norm_words(titles[c[1]]) == tw]
    if len(exact) == 1:
        return exact[0][1], []
    return None, sorted(cands, reverse=True)[:3]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", metavar="CLASS",
                    choices=["reachable", "recovered", "ledger-external",
                             "ledger-file-missing", "ledger-absent"])
    ap.add_argument("--candidates", action="store_true",
                    help="show unconfirmed title-overlap guesses")
    ap.add_argument("--min-cites", type=int, default=0)
    ap.add_argument("--json", metavar="OUT")
    args = ap.parse_args()

    cited = cited_keys()
    ledger, unkeyed = load_ledger()
    refs = load_refs()
    by_slug, titles = library_index()

    if not cited:
        print("No citations found. If content/**/*.jsonld is absent, run\n"
              "  bun run folio-assistant/content/pipeline/gen-block-jsonld.ts\n"
              "first — an ungenerated graph reads as a corpus that cites nothing.")
        return 0

    buckets: dict[str, list] = defaultdict(list)
    candidates: dict[str, list] = {}
    self_refs = []

    for key, n in cited.items():
        if key in SELF_KEYS:
            self_refs.append((key, n))
            continue
        entry = ledger.get(key)
        src = (entry or {}).get("source") or {}
        if src.get("kind") == "upload" and (REPO / src.get("file", "")).exists():
            buckets["reachable"].append((key, n, src["file"]))
            continue
        doc, cands = (recover(key, refs, by_slug, titles) if refs else (None, []))
        if doc:
            buckets["recovered"].append((key, n, f"library/{doc}"))
            continue
        if cands:
            candidates[key] = cands
        if entry is None:
            buckets["ledger-absent"].append((key, n, ""))
        elif src.get("kind") == "external":
            buckets["ledger-external"].append((key, n, src.get("url") or "(no url)"))
        else:
            buckets["ledger-file-missing"].append((key, n, src.get("file", "")))

    total = sum(len(v) for v in buckets.values())
    print(f"cited bibliography keys: {total} "
          f"({sum(n for _, n in self_refs)} citations to {len(self_refs)} self-reference "
          f"key(s) excluded: {', '.join(k for k, _ in self_refs) or '—'})")
    print(f"library documents: {len(titles)}\n")
    for name in ("reachable", "recovered", "ledger-external",
                 "ledger-file-missing", "ledger-absent"):
        rows = buckets[name]
        cites = sum(n for _, n, _ in rows)
        print(f"  {name:20} {len(rows):5} key(s)  {cites:6} citation(s)")
    if not refs:
        print("\n  NOTE: `bun` could not evaluate references.ts, so the recovery pass\n"
              "  did NOT run. `recovered` is 0 because it was not measured.")

    # The other direction, and the one nothing was looking at: a source that is
    # HELD and TRIAGED but joined to no bibliography key cannot be cited by any
    # block or any `-- Ref:`. It is in the repo and unreachable from the text.
    if unkeyed:
        verdicts = Counter((e.get("relevance") or {}).get("verdict", "(untriaged)")
                           for e in unkeyed)
        on_disk = sum(1 for e in unkeyed
                      if (REPO / ((e.get("source") or {}).get("file") or "_")).exists())
        print(f"\n  held but UNCITABLE — no bibliography key: {len(unkeyed)} "
              f"({on_disk} with the file on disk)")
        for verdict in ("core", "supporting", "tangential", "not-relevant",
                        "undetermined", "(untriaged)"):
            if verdicts.get(verdict):
                print(f"    relevance {verdict:14} {verdicts[verdict]:4}")
        print("    Each needs a `references.ts` entry before anything can cite it.")

    if args.list:
        rows = sorted(buckets[args.list], key=lambda t: -t[1])
        rows = [r for r in rows if r[1] >= args.min_cites]
        print(f"\n{args.list} ({len(rows)} shown, most-cited first):")
        for key, n, where in rows:
            title = (refs.get(key, {}).get("title") or "")[:58]
            print(f"  {n:5}  {key:26} {title:60} {where}")

    if args.candidates:
        print(f"\nunconfirmed title-overlap candidates ({len(candidates)} key(s)) —\n"
              "AGENT VERDICT REQUIRED; a high score on a short title means nothing:")
        for key in sorted(candidates, key=lambda k: -cited[k]):
            print(f"  {cited[key]:5}  {key}  ({(refs.get(key, {}).get('title') or '')[:50]})")
            for ov, doc, dt in candidates[key]:
                print(f"           {ov:4}  library/{doc:38} {dt}")

    if args.json:
        Path(args.json).write_text(json.dumps({
            "cited_total": total,
            "held_uncitable": len(unkeyed),
            "held_uncitable_by_relevance": dict(Counter(
                (e.get("relevance") or {}).get("verdict", "(untriaged)") for e in unkeyed)),
            "self_references": dict(self_refs),
            "recovery_pass_ran": bool(refs),
            "buckets": {k: [{"id": i, "cites": n, "where": w} for i, n, w in v]
                        for k, v in buckets.items()},
            "candidates": candidates,
        }, indent=1) + "\n")
        print(f"\nWrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
