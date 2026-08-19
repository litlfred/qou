#!/usr/bin/env python3
"""
sync-references-library — record each source's library location + ingestion
stage on its `references.ts` entry.

`content/schema/references.ts` is the authoritative bibliography (CSL-JSON).
It says what a source *is*; until now nothing there said whether we hold a
copy, where, or how far it has been processed. Answering that meant joining
three files by hand.

This adds one derived field per entry:

    library: {
      docId: "arxiv-2411.03801v2",
      dir: "library/arxiv-2411.03801v2",
      pdf: "library/arxiv-2411.03801v2/2411.03801v2.pdf",
      stage: "candidates",          // held < structure < sections < candidates
      pages: 24,
      sections: 14,
      arxiv: "2411.03801v2",
    },

## Derived, never authored

Every value comes from the library tree and the source ledger, so the field
is regenerated, not maintained. Re-running is a no-op when nothing moved;
`--check` exits 1 if the file is out of date, which makes it usable as a
preflight gate the way `sync-qou-mass-vendor.py --check` is.

Do not hand-edit a `library:` block — the next sync overwrites it. If it is
wrong, the library tree or the ledger is wrong.

## Why here and not in the ledger

`local/document-intake` is explicit that bibliographic metadata belongs to
`references.ts` alone and the ledger holds examination state. "Where is our
copy" is a property of the source, not a verdict about it, so it belongs on
this side of that line. The ledger keeps `source.file` as the join key; this
field is the resolved, enriched view of it.

Usage:
    scripts/sync-references-library.py --check     # exit 1 if stale
    scripts/sync-references-library.py --apply
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFS = os.path.join(REPO, "content", "schema", "references.ts")
LEDGER = os.path.join(REPO, "content", "bib-qa-verifications.json")
LIB = os.path.join(REPO, "library")

FIELD = "library"
MISSING = "\0missing:"   # sentinel prefix; never appears in a real doc-id


def library_index() -> dict[str, dict]:
    """doc-id -> facts, read from the library tree itself."""
    out: dict[str, dict] = {}
    if not os.path.isdir(LIB):
        return out
    for doc_id in sorted(os.listdir(LIB)):
        d = os.path.join(LIB, doc_id)
        if not os.path.isdir(d):
            continue
        sj = os.path.join(d, "structure.json")
        try:
            if os.path.exists(sj) and json.load(open(sj)).get("container"):
                continue          # split bound issue; its children carry the content
        except Exception:
            pass
        info: dict = {"docId": doc_id, "dir": f"library/{doc_id}"}
        pdfs = sorted(f for f in os.listdir(d) if f.lower().endswith(".pdf"))
        if pdfs:
            info["pdf"] = f"library/{doc_id}/{pdfs[0]}"

        stage = "held"
        if os.path.exists(sj):
            try:
                art = json.load(open(sj))
            except Exception:
                art = {}
            stage = "structure"
            info["pages"] = art.get("source", {}).get("pages")
            ax = (art.get("metadata") or {}).get("arxiv") or {}
            if ax.get("id"):
                info["arxiv"] = ax["id"] + (f"v{ax['version']}" if ax.get("version") else "")
            nsec = len(art.get("sections") or [])
            sdir = os.path.join(d, "sections")
            if os.path.isdir(sdir) and any(f.endswith(".md") for f in os.listdir(sdir)):
                stage = "sections"
                info["sections"] = nsec
            # Other copies of this same work, so a reader of the entry can
            # see the library holds it more than once. Derived from the
            # markers `library-resolve-duplicates.py` writes, not kept by
            # hand — a hand-added field here would be silently dropped by
            # `render()`, whose field list is fixed.
            if art.get("duplicate_copies"):
                info["alternates"] = sorted(art["duplicate_copies"])
            elif art.get("duplicate_of"):
                info["duplicateOf"] = art["duplicate_of"]
        if os.path.exists(os.path.join(d, "candidates.json")):
            stage = "candidates"
        info["stage"] = stage
        out[doc_id] = {k: v for k, v in info.items() if v is not None}
    return out


def ref_to_doc() -> dict[str, str]:
    """references.ts id -> doc-id, via the ledger's source.file."""
    if not os.path.exists(LEDGER):
        return {}
    led = json.load(open(LEDGER))
    entries = led.get("entries", [])
    # `entries` may be a dict keyed by reference id, and a row does not
    # have to repeat that id inside itself — 269 of 355 do not. Take the
    # key as the id and let an inner `id` override it.
    if isinstance(entries, dict):
        rows = [{"id": k, **v} if isinstance(v, dict) else v for k, v in entries.items()]
    else:
        rows = entries
    out: dict[str, str] = {}
    for r in rows:
        if not isinstance(r, dict):
            continue
        rid = r.get("id")
        src = r.get("source")
        path = src.get("file") if isinstance(src, dict) else None
        if not rid or not isinstance(path, str):
            continue
        m = re.match(r"library/([^/]+)/", path)
        if m:
            out[rid] = m.group(1)
        elif path.startswith("library/") and not os.path.exists(os.path.join(REPO, path)):
            # The ledger claims `kind: "upload"` for a file that is not in
            # the repo and, per git history, never was. Record the claim as
            # a `missing` stage rather than dropping the entry: silence here
            # reads identically to "not ingested yet", and these are a
            # different thing — a source we believed we held.
            out[rid] = MISSING + path
    return out


def notes_to_doc(text: str) -> dict[str, str]:
    """references.ts id -> doc-id, harvested from `note:` prose.

    A second join source, and not a redundant one. Earlier agents recorded
    "PDF library/<doc-id>/<file>" in an entry's note when they identified a
    source by hand, without ever adding a ledger row. Those entries look
    uncited to a ledger-only join even though the identification was already
    done — 12 of them, measured. The ledger still wins where both exist.
    """
    out: dict[str, str] = {}
    for m in re.finditer(r'\n\s*id: "([^"]+)",(.*?)\n  \}\)', text, re.S):
        rid, body = m.group(1), m.group(2)
        # A note that merely *mentions* another document must not create a
        # link. Three false links came from taking any path in the prose:
        # a note comparing this paper to another one, and a DEPRECATED
        # entry whose note names the entry that replaced it. Require an
        # explicit possession marker, which is the convention every
        # hand-written note already uses ("PDF library/<id>/ — ...").
        if re.search(r"\bDEPRECATED\b", body):
            continue
        mm = re.search(r"(?:PDF|held(?: at)?|copy(?: at)?)\s+library/([A-Za-z0-9._-]+)/", body, re.I)
        if mm and os.path.isdir(os.path.join(LIB, mm.group(1))):
            out[rid] = mm.group(1)
    return out


def render(info: dict, indent: str = "    ") -> str:
    order = ["docId", "dir", "pdf", "claimedPath", "stage", "pages", "sections", "arxiv",
             "alternates", "duplicateOf"]
    lines = [f"{indent}{FIELD}: {{"]
    for k in order:
        if k not in info:
            continue
        v = info[k]
        lines.append(f'{indent}  {k}: {json.dumps(v)},')
    lines.append(f"{indent}}},")
    return "\n".join(lines)


def sync(text: str, mapping: dict[str, str], index: dict[str, dict]) -> tuple[str, int, int]:
    """Insert or refresh the library block on each matching ref({...})."""
    added = updated = 0
    out: list[str] = []
    pos = 0
    # Each entry starts `ref({` and its id line follows shortly after.
    for m in re.finditer(r"\n(\s*)ref\(\{\n(\s*)id:\s*\"([^\"]+)\",", text):
        entry_indent = m.group(2)
        rid = m.group(3)
        doc_id = mapping.get(rid)
        if doc_id and doc_id.startswith(MISSING):
            info = {"stage": "missing", "claimedPath": doc_id[len(MISSING):]}
        else:
            info = index.get(doc_id) if doc_id else None
            # Follow a duplicate to the canonical copy. The join names
            # whichever file was ingested for this entry, which is not
            # necessarily the better copy: Riera-Rodríguez was joined to an
            # extraction that recovered 2 sections of 22 pages while another
            # copy of the same paper had 8 of 25. Redirect, and keep the
            # joined path as an alternate so nothing is lost.
            if info and info.get("duplicateOf"):
                canon = index.get(info["duplicateOf"])
                if canon:
                    info = dict(canon)
                    info["alternates"] = sorted(set(info.get("alternates", [])) | {doc_id})

        insert_at = m.end()
        out.append(text[pos:insert_at])
        pos = insert_at

        # An existing block sits immediately after the id line.
        existing = re.match(
            r"\n" + re.escape(entry_indent) + FIELD + r": \{.*?\n" + re.escape(entry_indent) + r"\},",
            text[pos:], re.S,
        )
        if existing:
            pos += existing.end()
            if info:
                updated += 1
        elif info:
            added += 1

        if info:
            out.append("\n" + render(info, entry_indent))

    out.append(text[pos:])
    return "".join(out), added, updated


def main() -> int:
    ap = argparse.ArgumentParser(description="Record library location + ingestion stage on references.ts")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true", help="exit 1 if references.ts is stale")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    index = library_index()
    text = open(REFS, encoding="utf-8").read()
    mapping = notes_to_doc(text)
    mapping.update(ref_to_doc())        # ledger is authoritative where both exist
    new, added, updated = sync(text, mapping, index)

    joined = sum(1 for r in mapping if mapping[r] in index)
    absent = sum(1 for r in mapping if mapping[r].startswith(MISSING))
    print(f"library documents      : {len(index)}")
    print(f"joins usable (ledger+note): {joined}")
    print(f"claimed-but-absent files : {absent}")
    print(f"entries added / refreshed: {added} / {updated}")

    stages: dict[str, int] = {}
    for v in index.values():
        stages[v["stage"]] = stages.get(v["stage"], 0) + 1
    print("stages:", ", ".join(f"{k}={v}" for k, v in sorted(stages.items())))

    if new == text:
        print("\nreferences.ts is up to date")
        return 0
    if args.check:
        print("\nreferences.ts is STALE — run --apply", file=sys.stderr)
        return 1
    open(REFS, "w", encoding="utf-8").write(new)
    print("\nreferences.ts updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
