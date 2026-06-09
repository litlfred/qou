#!/usr/bin/env python3
"""Helper for Gate #2 lean-compile-diagnostics.json regen.

Reads a list of .lean files (one per line, repo-relative) and emits
JSONL suitable for `content/pipeline/lean-compile-audit.ts --ingest`.

Two modes:

1. `--all-clean` — write empty diagnostics for every file in the list.
   Use when `lake build QOU` returns exit 0 (everything compiles
   clean); this regenerates the cache so the 629 stale per-file fails
   in the proof-lean-compiles QA criterion clear in one sweep.

2. `--from-lake-log <log>` — parse a lake build log for per-file errors.
   Use when `lake build QOU` returns non-zero; assigns errors to their
   originating files, empty diagnostics for the rest.

Output goes to stdout (capture with `> diagnostics.jsonl`).

Usage:
    python3 scripts/lean-compile-diagnostics-regen-helper.py \\
        --files /tmp/lean-files.txt --all-clean > /tmp/diag.jsonl
    bun run content/pipeline/lean-compile-audit.ts --ingest /tmp/diag.jsonl
    bun run content/pipeline/qa-sweep.ts content/quantum-observable-universe --only proof-lean-compiles
"""
import argparse
import json
import re
import sys
from pathlib import Path


def emit_empty(files):
    for f in files:
        sys.stdout.write(json.dumps({"file": f, "diagnostics": []}) + "\n")


def emit_from_log(files, log_path):
    """Parse a lake build log for per-file errors.

    lake output for an error looks like:
        ./content/quantum-observable-universe/path/file.lean:42:5: error: ...
    """
    log = Path(log_path).read_text(encoding="utf-8")
    pat = re.compile(
        r"^(?:\./)?(content/quantum-observable-universe/[^\s:]+\.lean):(\d+):(\d+):\s+(error|warning):\s*(.*?)$",
        re.MULTILINE,
    )
    per_file = {f: [] for f in files}
    for m in pat.finditer(log):
        path, line, _col, sev, msg = m.groups()
        if path in per_file:
            per_file[path].append({
                "line": int(line),
                "severity": sev,
                "message": msg.strip()[:500],
            })
    for f, diags in per_file.items():
        sys.stdout.write(json.dumps({"file": f, "diagnostics": diags}) + "\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--files", required=True, help="Path to file list (one .lean path per line)")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--all-clean", action="store_true", help="Emit empty diagnostics for every file")
    g.add_argument("--from-lake-log", metavar="LOG", help="Parse lake build log for per-file errors")
    args = ap.parse_args()

    with open(args.files, encoding="utf-8") as fp:
        files = [ln.strip() for ln in fp if ln.strip()]

    if args.all_clean:
        emit_empty(files)
    else:
        emit_from_log(files, args.from_lake_log)


if __name__ == "__main__":
    main()
