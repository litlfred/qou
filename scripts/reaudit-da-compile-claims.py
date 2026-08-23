#!/usr/bin/env python3
"""
Invalidate devils-advocate QA verdicts whose stated ground is a Lean-sibling
compile failure that does not reproduce.

Background
----------
The 2026-07-07 ``qa-agent-drain`` batch (reviewer id ``local/qa-agent-drain``,
``agent_model: gemini-3.1-pro``) wrote 887 ``da-*`` sidecar entries across 258
blocks asserting that the block's Lean sibling "fails to compile". Compiling the
siblings ``lean``-direct against a built import cone shows the claim is false for
the large majority of them.

This is a **recurrence** of a documented failure mode, not a new one. The
2026-06-22 batch from the same drain procedure produced the same defect on the
``proof-*`` axis; it was measured (~76-86% false-positive) and drained in
PR #2775, see ``docs/audits/2026-06-25-proof-qa-reaudit-false-positives.md`` and
``scripts/reaudit-proof-deterministic.py``. The present script is the ``da-*``
analogue, keyed on an actual compile rather than a token scan.

Two recorded error signatures show the batch was compiling without a built
import cone, on a laptop:

  * ``object file '/Users/litlfred/space_cats/qou/.lake/packages/...' does not
    exist``  -- a missing-olean error, i.e. the dependency cone was never built.
  * ``unexpected token 'section'; expected 'lemma'``  -- a *parse* error of the
    kind a statement-extractor emits when it expects a ``lemma`` and meets
    ``noncomputable section``.

Neither is evidence about the mathematics.

Policy (follows PR #2775, deliberately conservative)
----------------------------------------------------
* Only entries whose stated evidence **cannot bear on this repository** are
  touched -- either the note claims the sibling does not compile, or it pastes a
  toolchain error carrying one of the provenance signatures below. Keying on the
  prose alone was tried first and missed twelve entries that simply quoted the
  error without narrating it.
* A false ground makes a *judgment* verdict **unsupported, not disproven**, so
  the correction is ``n/a`` pending re-review -- never ``pass``. This is what
  #2775's follow-up did with its 1,680 judgment verdicts.
* Entries are **appended** (latest-wins), never rewritten or deleted, so the
  original verdict stays in the git history and in the sidecar.
* A block whose sibling genuinely fails to compile is **left alone**: the claim
  is wrong at scale, not always wrong.
* A compile that fails with a *missing-olean* error in THIS environment is
  inconclusive, not a confirmation -- it is the same artifact the batch hit, and
  such blocks are skipped rather than counted either way.

Usage
-----
  python3 scripts/reaudit-da-compile-claims.py --results <tsv> [--apply]

``<tsv>`` is ``<lean-path>\\t<OK|REAL_ERROR|MISSING_OLEAN>\\t<first-error-line>``.
Without ``--apply`` this is a dry run: it prints the plan and writes nothing.
"""
from __future__ import annotations

import argparse
import datetime
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# A note asserting the Lean sibling does not compile, in prose.
COMPILE_CLAIM = re.compile(r"fails? (?:to )?compil|fails compilation", re.I)

# ...but a phrase match alone is not enough: some entries never say "fails to
# compile", they simply paste the toolchain error. Those are the same defect and
# a first pass keyed only on the prose missed twelve of them. So also match the
# provenance signatures that `scripts/qa-evidence-provenance-gate.py` defines --
# a build error naming another machine's checkout, a missing olean, or a
# statement-extractor parse error is not evidence about this repository however
# it happens to be worded.
PROVENANCE_SIGNATURES = [
    re.compile(r"/(?:Users|home)/[A-Za-z0-9._-]+/(?:qou|space_cats)"),
    re.compile(r"object file\b[^\n]*does not exist", re.I),
    re.compile(r"unexpected token '[^']+'; expected '(?:lemma|theorem|def)'", re.I),
]


def unusable_ground(entry_blob: str) -> bool:
    """True when the entry's stated evidence cannot bear on this repository."""
    if COMPILE_CLAIM.search(entry_blob):
        return True
    return any(sig.search(entry_blob) for sig in PROVENANCE_SIGNATURES)


REVIEWER_ID = "local/qa-agent-drain"


def file_hash(path: str) -> str | None:
    if not os.path.exists(path):
        return None
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:12]


def field_hash(qa_path: str) -> dict:
    base = qa_path[: -len(".qa.json")]
    out = {}
    for ext in ("md", "ts", "lean"):
        h = file_hash(f"{base}.{ext}")
        if h:
            out[ext] = h
    return out


def head_sha() -> str | None:
    try:
        return subprocess.run(
            ["git", "-C", REPO, "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except Exception:
        return None


def load_results(path: str) -> dict[str, tuple[str, str]]:
    out: dict[str, tuple[str, str]] = {}
    with open(path) as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("\t")
            lean = parts[0]
            kind = parts[1] if len(parts) > 1 else ""
            err = parts[2] if len(parts) > 2 else ""
            out[lean] = (kind, err)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True,
                    help="TSV of lean-path -> compile outcome")
    ap.add_argument("--apply", action="store_true",
                    help="write the corrections (default: dry run)")
    ap.add_argument("--glob",
                    default="content/quantum-observable-universe/*/*.qa.json")
    args = ap.parse_args()

    results = load_results(args.results)
    if not results:
        print(f"no compile results in {args.results}", file=sys.stderr)
        return 2

    stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    sha = head_sha()

    stats = Counter()
    touched_blocks = 0
    per_criterion = Counter()
    genuine_blocks: list[str] = []
    skipped_inconclusive: list[str] = []

    for qa_path in sorted(glob.glob(os.path.join(REPO, args.glob))):
        rel = os.path.relpath(qa_path, REPO)
        with open(qa_path) as fh:
            sidecar = json.load(fh)

        lean = (sidecar.get("paths") or {}).get("lean")
        criteria = sidecar.get("criteria") or {}
        claiming = [
            crit for crit, entries in criteria.items()
            if isinstance(entries, list) and entries
            and unusable_ground(json.dumps(entries[-1]))
        ]
        if not claiming:
            continue

        if not lean or not os.path.exists(os.path.join(REPO, lean)):
            # The verdict cites a build of a sibling that is no longer there
            # (deleted as a shadowing stub, or never existed). The ground is
            # moot, so the verdict is unsupported the same way.
            kind, err = "OK", "sibling absent"
        else:
            outcome = results.get(lean)
            if outcome is None:
                continue
            kind, err = outcome

        if kind == "REAL_ERROR":
            stats["blocks_genuine_failure_left_alone"] += 1
            genuine_blocks.append(f"{os.path.basename(lean)}: {err[:90]}")
            continue
        if kind != "OK":
            # MISSING_OLEAN here is the same artifact the batch hit; it tells us
            # nothing about the file, so neither correct nor confirm.
            stats["blocks_inconclusive_skipped"] += 1
            skipped_inconclusive.append(os.path.basename(lean))
            continue

        touched_blocks += 1
        fh_now = field_hash(qa_path)
        for crit in claiming:
            last = criteria[crit][-1]
            prior = last.get("result")
            if prior == "n/a":
                stats["entries_already_invalidated"] += 1
                continue
            per_criterion[crit] += 1
            stats["entries_invalidated"] += 1
            if args.apply:
                criteria[crit].append({
                    "field_hash": fh_now,
                    "result": "n/a",
                    "reviewer": {
                        "kind": "agent",
                        "id": "local/reaudit-da-compile-claims",
                    },
                    "reviewed_at": stamp,
                    **({"reviewed_sha": sha} if sha else {}),
                    "notes": (
                        f"Invalidated: the prior {prior!r} verdict is grounded on "
                        f"'{os.path.basename(lean)} fails to compile', and it does. "
                        f"Compiled lean-direct against a built import cone: exit 0. " if lean and os.path.exists(os.path.join(REPO, lean)) else "The sibling it cites is not in the tree. "
                        f"The prior entry is from the 2026-07-07 qa-agent-drain batch, "
                        f"which recorded missing-olean and statement-extractor parse "
                        f"errors as compile failures. A false ground leaves this "
                        f"criterion unsupported rather than disproven, so this is n/a "
                        f"pending re-review, not pass. Recurrence of the batch drained "
                        f"in PR #2775 on the proof-* axis; see bean qou-zkia."
                    ),
                })

        if args.apply:
            with open(qa_path, "w") as fh:
                json.dump(sidecar, fh, indent=2)
                fh.write("\n")

    mode = "APPLIED" if args.apply else "DRY RUN (no writes; pass --apply)"
    print(f"=== reaudit-da-compile-claims -- {mode}\n")
    print(f"blocks corrected                     : {touched_blocks}")
    print(f"entries invalidated -> n/a           : {stats['entries_invalidated']}")
    print(f"entries already n/a (skipped)        : {stats['entries_already_invalidated']}")
    print(f"blocks with a GENUINE failure (kept) : {stats['blocks_genuine_failure_left_alone']}")
    print(f"blocks inconclusive here (skipped)   : {stats['blocks_inconclusive_skipped']}")
    if per_criterion:
        print("\nby criterion:")
        for crit, n in per_criterion.most_common():
            print(f"  {n:5d}  {crit}")
    if genuine_blocks:
        print(f"\ngenuine compile failures left as-is ({len(genuine_blocks)}):")
        for g in genuine_blocks:
            print(f"  {g}")
    if skipped_inconclusive:
        print(f"\ninconclusive in this environment ({len(skipped_inconclusive)}):")
        for s in skipped_inconclusive[:20]:
            print(f"  {s}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
