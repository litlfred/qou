#!/usr/bin/env python3
"""Local uploads/ -> library/ ingester (folio-assistant-free fallback).

The canonical producer is folio-assistant's `scripts/pdf-structure.py`. When
that clone is unavailable (sandbox, firewalled setup-folio-assistant.sh), this
emits the same `pdf-structure/v1` shape so the result is greppable by
corpus-grep path 5, which searches `library/` only.

Deliberately conservative: it never overwrites an existing library/<doc-id>/,
and it reports what it skipped.

Usage:  python3 scripts/ingest-uploads-local.py [--apply] [file.pdf ...]
"""
from __future__ import annotations
import hashlib, json, pathlib, re, sys

# cryptography's rust binding panics in some containers; pypdf falls back to a
# no-crypto provider when the import fails outright, so block it.
class _Block:
    def find_module(self, name, path=None):
        return self if name == "cryptography" or name.startswith("cryptography.") else None
    def load_module(self, name):
        raise ImportError("blocked")
sys.meta_path.insert(0, _Block())
from pypdf import PdfReader  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
UP, LIB = ROOT / "uploads", ROOT / "library"

def slug(s, n=60):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:n].strip("-") or "untitled"

def doc_id_for(text, fname):
    m = re.search(r"arXiv:\s*([\w.\-]+/?[\w.\-]*)", text)
    if m:
        return "arxiv-" + m.group(1).replace("/", "-")
    return slug(pathlib.Path(fname).stem)

def clean(t):
    return re.sub(r"[ \t]+", " ", (t or "")).strip()

def ingest(pdf: pathlib.Path, apply: bool):
    raw = pdf.read_bytes()
    r = PdfReader(str(pdf))
    pages = [clean(p.extract_text() or "") for p in r.pages]
    p1 = pages[0] if pages else ""
    did = doc_id_for(p1, pdf.name)
    out = LIB / did
    if out.exists():
        return did, "EXISTS (skipped)", 0

    lines = [l.strip() for l in (pages[0] if pages else "").split("\n") if l.strip()]
    drop = re.compile(r"^(arXiv:|\d{1,2}\s+\w{3}\s+\d{4}$)")
    cand = [l for l in lines if not drop.match(l)]
    title = " ".join(cand[:2])[:200] if cand else pdf.stem
    authors = cand[2][:200] if len(cand) > 2 else ""
    ab = ""
    m = re.search(r"(?:Abstract|ABSTRACT)[.\s:—-]*(.{40,1200})", p1, re.S)
    if m:
        ab = clean(m.group(1))[:1200]

    # Section split: outline if present, else heading heuristic over full text.
    secs = []
    try:
        for i, it in enumerate(r.outline or []):
            if isinstance(it, dict) and it.get("/Title"):
                secs.append({"title": str(it["/Title"]), "page": i})
    except Exception:
        pass
    full = "\n".join(pages)
    if not secs:
        hd = re.compile(r"^\s*(\d{1,2}(?:\.\d{1,2})*)\.?\s+([A-Z][^\n]{3,70})\s*$", re.M)
        hits = list(hd.finditer(full))
        if hits:
            for j, h in enumerate(hits):
                end = hits[j + 1].start() if j + 1 < len(hits) else len(full)
                secs.append({"title": clean(h.group(2)), "number": h.group(1),
                             "body": full[h.start():end]})
        else:
            secs = [{"title": "full-text", "number": None, "body": full}]
    else:
        n = max(1, len(full) // max(1, len(secs)))
        for j, s in enumerate(secs):
            s["body"] = full[j * n:(j + 1) * n]
            s["number"] = None

    brief = f"{title} — {ab[:110]}" if ab else title
    entries = []
    if apply:
        (out / "sections").mkdir(parents=True, exist_ok=True)
    for j, s in enumerate(secs):
        sid = f"sec-{j:03d}-{slug(s['title'], 46)}"
        entries.append({"section_id": sid, "title": s["title"],
                        "number": s.get("number"), "chars": len(s.get("body", ""))})
        if apply:
            fm = (f"---\ndoc_id: {did}\ndoc_title: \"{title}\"\n"
                  f"section_id: {sid}\nsection_title: \"{s['title']}\"\n"
                  f"section_number: {s.get('number') or 'null'}\n"
                  f"source_pdf: {pdf.name}\n"
                  f"source_sha256: {hashlib.sha256(raw).hexdigest()[:16]}\n"
                  f"doc_brief: \"{brief}\"\n"
                  f"ingested_by: scripts/ingest-uploads-local.py "
                  f"(folio-assistant unavailable)\n---\n")
            (out / "sections" / f"{sid}.md").write_text(fm + s.get("body", ""),
                                                        encoding="utf-8")
    if apply:
        am = re.search(r"arXiv:\s*([\w.\-]+/?[\w.\-]*)", p1)
        struct = {
            "_schema": "pdf-structure/v1",
            "doc_id": did,
            "source": {"file": pdf.name,
                       "sha256": hashlib.sha256(raw).hexdigest(),
                       "bytes": len(raw), "pages": len(r.pages)},
            "metadata": {"arxiv": {"id": am.group(1) if am else None},
                         "doi": None, "title": title,
                         "authors_raw": authors, "abstract": ab, "docinfo": {}},
            "toc": [{"title": e["title"], "number": e["number"]} for e in entries],
            "toc_source": "outline" if r.outline else "heading-heuristic",
            "sections": entries,
            "diagnostics": {"pages_without_text": sum(1 for p in pages if not p),
                            "likely_scanned": sum(1 for p in pages if not p) > len(pages) / 2,
                            "toc_entries": len(entries), "sections": len(entries),
                            "chars_total": len(full),
                            "ingester": "local fallback; not folio-assistant"},
        }
        (out / "structure.json").write_text(json.dumps(struct, indent=2) + "\n")
        (out / "summary.json").write_text(json.dumps(
            {"_schema": "library-summary/v1", "doc_id": did, "brief": brief,
             "provenance": {"kind": "extractive",
                            "note": "local fallback ingester"}}, indent=2) + "\n")
        (out / "candidates.json").write_text(json.dumps(
            {"_schema": "candidates/v1", "doc_id": did, "candidates": [],
             "note": "extract-candidates.py unavailable in this container"},
            indent=2) + "\n")
        (out / pdf.name).write_bytes(raw)
    return did, ("ingested" if apply else "would ingest"), len(entries)

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    apply = "--apply" in sys.argv
    targets = [UP / a for a in args] if args else sorted(UP.glob("*.pdf"))
    for p in targets:
        if not p.exists():
            print(f"  {p.name:32} MISSING"); continue
        try:
            did, status, n = ingest(p, apply)
            print(f"  {p.name[:32]:34} -> {did:34} {status} ({n} sections)")
        except Exception as e:
            print(f"  {p.name[:32]:34} -> ERROR {type(e).__name__}: {str(e)[:60]}")

if __name__ == "__main__":
    main()
