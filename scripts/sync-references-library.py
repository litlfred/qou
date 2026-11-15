#!/usr/bin/env python3
"""
sync-references-library — record each source's library location + ingestion
stage on its bibliography entry, `folio/references/<id>.json`.

The bibliography is CSL-JSON, one entry per file in `folio/references/`
(bean qou-l7pj; `folio/schema/references.ts` loads them).
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

## Per-entry files (bean qou-l7pj)

The block is the `library` key of each `folio/references/<id>.json`, placed
right after `id`, with its fields in `render()` order. `--apply` rewrites
only the files whose block changed, in the same JSON format the split wrote
(`references_dir.dumps`), so an unchanged file stays byte-identical.

This script refuses to run on a checkout from before the split (entries
inline in `references.ts`). That checkout would show an empty directory,
and the script would report "up to date" while writing nothing.

An entry built by code in `references.ts` (today only `leitner2026`) cannot
carry a block. If a join reaches one, the script names it and leaves it
alone.

Before the split this script found entries by the regex `ref({` followed
directly by `id:`. Three entries open with a comment line before `id:`
(`kobayashi1996`, `borel1986`, `chlouveraki2016`), so
the regex never matched them. Per-entry files have no such blind spot.

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
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import bib_ledger  # noqa: E402  -- the source ledger's reader (attestation store, legacy fallback)
import references_dir  # noqa: E402  -- folio/references/<id>.json, in ORDER
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
    """entry id -> doc-id, via the ledger's source.file."""
    led, note = bib_ledger.read_source_ledger(REPO)
    print(note, file=sys.stderr)
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


def notes_to_doc(files: dict[str, dict]) -> dict[str, str]:
    """entry id -> doc-id, harvested from `note:` prose.

    A second join source, and not a redundant one. Earlier agents recorded
    "PDF library/<doc-id>/<file>" in an entry's note when they identified a
    source by hand, without ever adding a ledger row. Those entries look
    uncited to a ledger-only join even though the identification was already
    done — 12 of them, measured. The ledger still wins where both exist.

    The text searched is the entry's whole file, as the TypeScript entry
    body was before the split (bean qou-l7pj).
    """
    out: dict[str, str] = {}
    for rid, entry in files.items():
        body = references_dir.dumps(entry)
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


def held(doc_id: str) -> bool:
    """Is this copy still on disk? Wider than `library_index()`, which skips a
    split bound issue's container — a copy the library still holds."""
    return bool(doc_id) and os.path.isdir(os.path.join(LIB, doc_id))


RENDER_ORDER = ["docId", "dir", "pdf", "claimedPath", "stage", "pages", "sections", "arxiv",
                "alternates", "duplicateOf"]


def render(info: dict) -> dict:
    """The `library` block, its keys in the fixed order `LibraryRef` documents."""
    return {k: info[k] for k in RENDER_ORDER if k in info}


def with_block(entry: dict, block: dict) -> dict:
    """`entry` with its `library` key set to `block`, placed right after `id`."""
    out: dict = {}
    for k, v in entry.items():
        if k == FIELD:
            continue
        out[k] = v
        if k == "id":
            out[FIELD] = block
    return out


def sync(files: dict[str, dict], order: list[str], mapping: dict[str, str], index: dict[str, dict],
         kept: list[str] | None = None, unreachable: list[str] | None = None) -> tuple[dict[str, dict], int, int]:
    """Insert or refresh the library block on each entry file.

    Returns the entries whose file content changes, keyed by id. An existing
    block whose entry no join reaches is kept verbatim and its id appended
    to `kept`: unconfirmed, not refuted. A join that reaches an entry built
    by code in references.ts is appended to `unreachable`, since no file
    exists to carry the block.
    """
    kept = [] if kept is None else kept
    unreachable = [] if unreachable is None else unreachable
    canon_of = {a: d for d, v in index.items() for a in v.get("alternates", [])}
    added = updated = 0
    changed: dict[str, dict] = {}
    for rid in order:
        doc_id = mapping.get(rid)
        if rid not in files:
            if doc_id:
                unreachable.append(rid)
            continue
        entry = files[rid]
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
            # The marker can sit on either side: a copy may say `duplicate_of`,
            # or only the canonical copy may list it in `duplicate_copies`.
            # Read both — with one side missing, Riera-Rodríguez flipped back
            # to its 3-section extraction from the 8-section one.
            target = (info or {}).get("duplicateOf") or canon_of.get(doc_id or "")
            if info and target and target != doc_id:
                canon = index.get(target)
                if canon:
                    info = dict(canon)
                    info["alternates"] = sorted(set(info.get("alternates", [])) | {doc_id})

        block = entry.get(FIELD)
        if isinstance(block, dict):
            if not info:
                # No join reaches this entry any more, but a block is already
                # here. It is an earlier identification (by hand or by an
                # older join) that this run cannot CONFIRM — which is not the
                # same as refuting it. Dropping it read as "not held" for ten
                # sources we hold (owner ruling 2026-10-05: keep unconfirmed
                # links). Keep it verbatim and count it, so it is visible.
                kept.append(rid)
                continue
            # Alternates already recorded stay recorded while the copy is
            # still in the library: a refresh must not forget a known copy
            # just because the duplicate markers moved.
            # So does the copy the block used to name, when the join now
            # resolves to a different (canonical) one.
            old_alt = {a for a in (block.get("alternates") or []) if isinstance(a, str) and held(a)}
            prior_doc = block.get("docId")
            if isinstance(prior_doc, str) and held(prior_doc):
                old_alt.add(prior_doc)
            alt = (set(info.get("alternates", [])) | old_alt) - {info.get("docId")}
            if alt:
                info = {**info, "alternates": sorted(alt)}
            updated += 1
        elif info:
            added += 1
        else:
            continue

        new = with_block(entry, render(info))
        if references_dir.dumps(new) != references_dir.dumps(entry):
            changed[rid] = new
    return changed, added, updated


def main() -> int:
    ap = argparse.ArgumentParser(description="Record library location + ingestion stage on folio/references/<id>.json")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true", help="exit 1 if any entry file is stale")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    # Refuse the pre-split layout rather than report "up to date" over nothing.
    try:
        references_dir.require_split_layout(REPO)
    except SystemExit as e:
        print(f"sync-references-library: {e}", file=sys.stderr)
        return 2

    index = library_index()
    files = references_dir.file_entries(REPO)
    order = references_dir.order(REPO)
    order += [rid for rid in sorted(files) if rid not in set(order)]
    mapping = notes_to_doc(files)
    mapping.update(ref_to_doc())        # ledger is authoritative where both exist
    kept: list[str] = []
    unreachable: list[str] = []
    changed, added, updated = sync(files, order, mapping, index, kept, unreachable)

    joined = sum(1 for r in mapping if mapping[r] in index)
    absent = sum(1 for r in mapping if mapping[r].startswith(MISSING))
    print(f"library documents      : {len(index)}")
    print(f"joins usable (ledger+note): {joined}")
    print(f"claimed-but-absent files : {absent}")
    print(f"entries added / refreshed: {added} / {updated}")
    print(f"kept, unconfirmed by any join: {len(kept)}" + (f" ({', '.join(kept)})" if kept else ""))
    if unreachable:
        print(f"joined but built in references.ts, no file to write: {', '.join(unreachable)}")

    stages: dict[str, int] = {}
    for v in index.values():
        stages[v["stage"]] = stages.get(v["stage"], 0) + 1
    print("stages:", ", ".join(f"{k}={v}" for k, v in sorted(stages.items())))

    if not changed:
        print("\nfolio/references/ is up to date")
        return 0
    if args.check:
        print(f"\n{len(changed)} file(s) in folio/references/ are STALE — run --apply", file=sys.stderr)
        for rid in sorted(changed)[:20]:
            print(f"  {rid}.json", file=sys.stderr)
        return 1
    for entry in changed.values():
        references_dir.write_entry(REPO, entry)
    print(f"\nfolio/references/: {len(changed)} file(s) updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
