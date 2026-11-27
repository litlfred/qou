#!/usr/bin/env python3
"""Read all agent/human QA verdicts for a content block across all 3 QA stores (bean qou-tv74).

Corpus-grep Path 7 (`AGENTS.md` §"Before declaring open") requires reading a
content block's own agent/human QA verdicts before declaring an item open or
unexamined. Two structural facts make a naive `grep` or single-file `jq` miss
verdicts:

1. Agent analyses sit inside escaped JSON strings (`evidence` / `notes`) keyed
   by the invoking criterion (`trap-superlative`, `da-non-sequitur`, etc.)
   rather than by mathematical topic.
2. Platform `qa-sweep` splits block QA storage across up to three paths:
   - beside-the-block legacy sidecar: `folio/<paper>/<chapter>/<block>.qa.json`
   - derived results tree: `test/results/block-qa/folio/<paper>/<chapter>/<block>.qa.json`
   - canonical attestation store: `test/attestations/block-qa/folio/<paper>/<chapter>/<block>.attestations.json`

This read-only helper resolves a block by path prefix (with or without `.md` /
`.ts` / `.qa.json`) or by block label (e.g. `tbl:unified-iterative-correction-table-data`),
unions and deduplicates `agent` and `human` verdicts across all three stores,
and tags each entry `FRESH`, `STALE`, or `UNHASHED` against the live `.md`
12-char SHA-256 prefix.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LABEL_RE = re.compile(r'\blabel:\s*"([^"]+)"')


def sha12(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def resolve_block_stem(target: str, repo_root: Path = REPO_ROOT) -> Path:
    """Resolve a block path, file, or `kind:slug` label to its repo-relative stem."""
    cleaned = target.strip()
    for suffix in (".qa.json", ".attestations.json", ".jsonld", ".lean", ".md", ".ts"):
        if cleaned.endswith(suffix):
            cleaned = cleaned[: -len(suffix)]
            break
    for prefix in ("test/results/block-qa/", "test/attestations/block-qa/"):
        if cleaned.startswith(prefix):
            cleaned = cleaned[len(prefix) :]
            break

    cand = repo_root / cleaned
    if cand.with_suffix(".md").exists() or cand.with_suffix(".ts").exists() or cand.with_suffix(".qa.json").exists():
        return cand.resolve().relative_to(repo_root.resolve())

    # Search by label in folio/**/*.ts (excluding .lake and node_modules)
    folio_dir = repo_root / "folio"
    if folio_dir.exists():
        for ts_path in sorted(folio_dir.rglob("*.ts")):
            if ".lake" in ts_path.parts or "node_modules" in ts_path.parts:
                continue
            try:
                txt = ts_path.read_text(encoding="utf-8")
            except OSError:
                continue
            m = LABEL_RE.search(txt)
            if m and m.group(1) == target.strip():
                return ts_path.with_suffix("").resolve().relative_to(repo_root.resolve())
            if ts_path.stem == cleaned:
                return ts_path.with_suffix("").resolve().relative_to(repo_root.resolve())

    raise FileNotFoundError(f"Could not resolve block stem or label: {target!r}")


def collect_verdicts(
    stem_rel: Path,
    repo_root: Path = REPO_ROOT,
    min_chars: int = 0,
    include_script: bool = False,
) -> dict:
    """Collect deduplicated agent/human verdicts across all three QA sidecar stores."""
    stem_str = stem_rel.as_posix()
    md_path = repo_root / f"{stem_str}.md"
    live_md_sha = sha12(md_path.read_bytes()) if md_path.exists() else None

    sources = [
        ("results-tree", repo_root / "test" / "results" / "block-qa" / f"{stem_str}.qa.json"),
        ("attestations", repo_root / "test" / "attestations" / "block-qa" / f"{stem_str}.attestations.json"),
        ("sibling-qa", repo_root / f"{stem_str}.qa.json"),
    ]

    found_sources: list[str] = []
    seen: set[tuple] = set()
    entries_out: list[dict] = []

    for source_kind, path in sources:
        if not path.exists():
            continue
        found_sources.append(path.relative_to(repo_root).as_posix())
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"warning: could not parse {path}: {exc}", file=sys.stderr)
            continue
        criteria = doc.get("criteria") or {}
        for crit, arr in criteria.items():
            if not isinstance(arr, list):
                continue
            for entry in arr:
                if not isinstance(entry, dict):
                    continue
                rev = entry.get("reviewer") or {}
                rkind = rev.get("kind", "unknown")
                if not include_script and rkind not in ("agent", "human"):
                    continue
                fh = entry.get("field_hash") or {}
                md_hash = fh.get("md")
                body = (entry.get("evidence") or entry.get("notes") or "").strip()
                if len(body) < min_chars:
                    continue
                ident = (
                    crit,
                    rkind,
                    rev.get("id"),
                    md_hash,
                    entry.get("reviewed_at"),
                    entry.get("result"),
                    body,
                )
                if ident in seen:
                    continue
                seen.add(ident)
                if md_hash is None:
                    freshness = "UNHASHED"
                elif live_md_sha is not None and md_hash == live_md_sha:
                    freshness = "FRESH"
                elif live_md_sha is not None:
                    freshness = "STALE"
                else:
                    freshness = "NO_MD"
                entries_out.append(
                    {
                        "criterion": crit,
                        "result": entry.get("result", "?"),
                        "freshness": freshness,
                        "reviewer_kind": rkind,
                        "reviewer_id": rev.get("id", "?"),
                        "reviewed_at": entry.get("reviewed_at", ""),
                        "field_hash_md": md_hash,
                        "source": source_kind,
                        "text": body,
                    }
                )

    return {
        "block": stem_str,
        "live_md_hash": live_md_sha,
        "sources_read": found_sources,
        "count": len(entries_out),
        "verdicts": entries_out,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("target", help="Block path, .md/.ts/.qa.json file, or block label (e.g. tbl:...)")
    ap.add_argument("--min-chars", type=int, default=0, help="Only show verdicts whose evidence/notes >= N chars")
    ap.add_argument("--only-nonpass", action="store_true", help="Only show fail/warn verdicts")
    ap.add_argument("--include-script", action="store_true", help="Include automated script entries")
    ap.add_argument("--json", action="store_true", help="Emit JSON report")
    args = ap.parse_args(argv)

    try:
        stem = resolve_block_stem(args.target, REPO_ROOT)
    except FileNotFoundError as exc:
        print(f"qa-block-verdicts: {exc}", file=sys.stderr)
        return 2

    report = collect_verdicts(
        stem,
        repo_root=REPO_ROOT,
        min_chars=args.min_chars,
        include_script=args.include_script,
    )
    if args.only_nonpass:
        report["verdicts"] = [v for v in report["verdicts"] if v["result"] not in ("pass", "n/a")]
        report["count"] = len(report["verdicts"])

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0

    print(f"block: {report['block']}  (live .md sha12: {report['live_md_hash'] or 'absent'})")
    print(f"sources ({len(report['sources_read'])}): {', '.join(report['sources_read']) or 'none'}")
    print(f"verdicts: {report['count']}")
    for v in report["verdicts"]:
        ts = f" {v['reviewed_at']}" if v["reviewed_at"] else ""
        print(
            f"  [{v['freshness']}] {v['criterion']} [{v['result']}] "
            f"({v['reviewer_kind']}:{v['reviewer_id']}{ts}, {v['source']}): {v['text']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
