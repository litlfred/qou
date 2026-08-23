#!/usr/bin/env python3
"""
Flag QA sidecar verdicts whose stated evidence is an artifact of the reviewer's
environment rather than a fact about this repository.

Why this exists
---------------
Twice now, a ``qa-agent-drain`` batch has compiled content-block Lean siblings
*without a built import cone* and recorded the resulting toolchain errors as
substantive QA failures:

  * 2026-06-22, ``proof-*`` axis -- measured ~76-86% false-positive, drained in
    PR #2775 (``docs/audits/2026-06-25-proof-qa-reaudit-false-positives.md``).
  * 2026-07-07, ``da-*`` axis -- 887 entries across 258 blocks asserting the
    sibling "fails to compile" (bean ``qou-zkia``).

The first was corrected as *data*. Nothing stopped the second, because nothing
in the pipeline distinguishes "the Lean is wrong" from "the reviewer could not
build it". This gate is that distinction, and it is deterministic: it never
compiles anything, it only reads what the verdict itself recorded.

Three signatures, each of which is definitionally not evidence about this repo:

  ``foreign-path``   the evidence cites an absolute path outside the repo
                     (``/Users/...``, ``/home/<someone>/...``). A build error
                     naming another machine's checkout says nothing here.
  ``missing-olean``  ``object file '...' does not exist`` -- the dependency cone
                     was not built. This is the reviewer's environment.
  ``extractor-parse`` ``unexpected token 'section'; expected 'lemma'`` and kin --
                     a *statement-extractor* parse error, not a compile of the
                     file. The extractor expected a ``lemma`` and met something
                     else; the file itself was never elaborated.

A hit is not proof the verdict is wrong -- the block may well be defective for
other reasons. It is proof the *stated ground* is unusable, which is what makes
the verdict unreviewable and is exactly the state that should never reach a
reader as a live ``fail``.

Usage
-----
  python3 scripts/qa-evidence-provenance-gate.py [--strict] [--json OUT]

Exits 1 under ``--strict`` if any live (latest, non-``n/a``) verdict rests on
one of these signatures.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from collections import Counter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SIGNATURES: list[tuple[str, re.Pattern[str], str]] = [
    (
        "foreign-path",
        re.compile(r"/(?:Users|home)/[A-Za-z0-9._-]+/[^\s'\"]*"),
        "evidence cites an absolute path outside this repository",
    ),
    (
        "missing-olean",
        re.compile(r"object file\b[^\n]*does not exist", re.I),
        "the dependency cone was not built when the verdict was recorded",
    ),
    (
        "extractor-parse",
        re.compile(r"unexpected token '[^']+'; expected '(?:lemma|theorem|def)'", re.I),
        "a statement-extractor parse error, not a compile of the file",
    ),
]

# A path inside the repo tree is normal evidence, not a foreign path.
INTERNAL = re.compile(r"/(?:Users|home)/[A-Za-z0-9._-]+/(?:qou|space_cats)")


def classify(entry: dict) -> list[tuple[str, str]]:
    """Return (signature, matched-text) for each provenance defect in `entry`."""
    blob = " ".join(
        str(entry.get(k, "")) for k in ("notes", "evidence", "detail", "message")
    )
    if not blob.strip():
        return []
    hits = []
    for name, pat, _why in SIGNATURES:
        m = pat.search(blob)
        if not m:
            continue
        if name == "foreign-path":
            # Only flag when the path is genuinely elsewhere. A repo-relative
            # path, or one under a checkout of this project, is fine evidence.
            frag = m.group(0)
            if not INTERNAL.search(frag):
                continue
        hits.append((name, m.group(0)[:120]))
    return hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any live verdict rests on a flagged signature")
    ap.add_argument("--json", dest="json_out",
                    help="write the full finding list to this path")
    ap.add_argument("--glob", default="content/**/*.qa.json")
    args = ap.parse_args()

    findings: list[dict] = []
    by_sig: Counter = Counter()
    by_criterion: Counter = Counter()
    live = 0
    blocks: set[str] = set()

    pattern = os.path.join(REPO, args.glob)
    for qa_path in sorted(glob.glob(pattern, recursive=True)):
        rel = os.path.relpath(qa_path, REPO)
        try:
            with open(qa_path) as fh:
                sidecar = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        for crit, entries in (sidecar.get("criteria") or {}).items():
            if not isinstance(entries, list) or not entries:
                continue
            latest = entries[-1]
            hits = classify(latest)
            if not hits:
                continue
            result = latest.get("result")
            # An already-invalidated verdict is not live; it is a record.
            is_live = result not in ("n/a", "pass")
            for sig, matched in hits:
                by_sig[sig] += 1
                by_criterion[crit] += 1
                blocks.add(rel)
                if is_live:
                    live += 1
                findings.append({
                    "sidecar": rel,
                    "criterion": crit,
                    "result": result,
                    "signature": sig,
                    "matched": matched,
                    "reviewer": (latest.get("reviewer") or {}).get("id"),
                    "reviewed_at": latest.get("reviewed_at"),
                    "live": is_live,
                })

    print(f"QA evidence-provenance gate — {len(findings)} finding(s) "
          f"across {len(blocks)} block(s); {live} live")
    if by_sig:
        print("\nby signature:")
        for sig, n in by_sig.most_common():
            why = next(w for s, _p, w in SIGNATURES if s == sig)
            print(f"  {n:5d}  {sig:16s} {why}")
    if by_criterion:
        print("\nby criterion:")
        for crit, n in by_criterion.most_common(12):
            print(f"  {n:5d}  {crit}")

    if args.json_out:
        with open(args.json_out, "w") as fh:
            json.dump({"findings": findings,
                       "live": live,
                       "blocks": len(blocks)}, fh, indent=2)
            fh.write("\n")
        print(f"\nwrote {args.json_out}")

    if args.strict and live:
        print(f"\nFAIL: {live} live verdict(s) rest on evidence from the "
              f"reviewer's environment rather than this repository.",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
