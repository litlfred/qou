#!/usr/bin/env python3
"""Triage QA sidecar verdicts whose quoted evidence cannot be found in the block.

`qa-sweep` recomputes `script`-kind criteria on every run. It does **not**
recompute `agent`-kind ones — an agent verdict persists until an agent replaces
it. So a `fail` recorded against prose that was never there, or that has since
been rewritten, stays in the sidecar and reads as a live defect.

Two independent axes, kept apart because they are different claims:

  STALE       the recorded `field_hash` disagrees with sha256(file)[:12] on
              disk. The verdict is about a different version of the block. It
              says nothing about whether the finding is still true.

  UNFINDABLE  every quoted span in the evidence is absent from the block's
              .md/.ts/.lean today.

Read together:

  * UNFINDABLE **and** STALE — the block was edited and the quoted prose went
    with it. The verdict is out of date.
  * UNFINDABLE but **not** STALE — the file the verdict was recorded against is
    the file on disk, and the quoted span is not in it. No staleness key can
    catch this one.

🛑 **UNFINDABLE is a staleness signal, NOT a fabrication signal.** It means the
quote is not in the block *now* — nothing more. Every case chased to a
conclusion here turned out to be prose that genuinely existed and was removed by
a `qou-ujp8` trap-drain: the finding was real and someone fixed it.

That reading was published on 2026-09-04 for two named cases as "quotes text that
was never in the block", and is **retracted**. Confirmed fabricated quotes: zero.

**No method available in this repo reliably establishes "never existed", and two
plausible ones both under-report.** Measured, each overturned by the next:

  * `git log --format=%h -- <path>` — not a file's history. Without `--follow` a
    renamed or moved block shows a truncated log; one case returned **1**
    revision where `--follow` returns **12**.
  * `git log --all --follow -p -- <path>` — follows one rename chain, so it
    misses a block that was split, copied, or duplicated under another path.
    It reported "no history hit" for a phrase that
    `git log --all -S` then found in a trap-drain commit. It raised the
    confirmed-stale count from 2 to 8 of 21 and was still wrong.
  * `git log --all -S '<phrase>' -- '*.md'` — the best of the three, and still
    only a positive test: it confirms text *existed*, and its silence has not
    been validated as evidence of absence.

So use this tool to find candidates and to confirm staleness positively. Do not
use its silence to conclude a verdict was fabricated.

## This tool produces a TRIAGE LIST, not a defect count

Do not quote its totals as a number of bad verdicts. It cannot distinguish a
quotation *of the block* from the reviewer's own prose set in quotes, and the
latter is common ("the block's own opening paragraph begins…"). Confirm any
individual case against `git log -p` on the block before acting on it: a span
absent from HEAD may still have existed when the verdict was written.

An opening `'` is only treated as a quote delimiter when it does **not** follow a
letter. An English possessive or contraction in the reviewer's own prose — "the
block's final section is …", "the corpus's named token substitution" — otherwise
opens a phantom quotation that runs to the next apostrophe, capturing reviewer
commentary that was never in the block and is never going to be found there.
Measured on this corpus, before and after the fix: the "unfindable" count fell
from 166 to 125 in the current bucket and from 27 to 21 in the stale one — so
this one defect accounted for about a quarter of the flags, not most of them.

Comparison is on **prose runs only** — maximal runs of >= 5 alphabetic words,
>= 25 characters, with math, punctuation and LaTeX acting as separators — so a
quote that ASCII-ised `$\\lambda$` to `lambda` is not counted as a miss. A
substring test without that normalisation over-reports by roughly 2.9x on this
corpus (re-measured 2026-09-05 with the apostrophe fix in place: 359 against 125
in the current bucket; the pre-fix figures were 393 against 166).

Usage:  python3 scripts/qa-stale-agent-verdicts.py [--list] [--criterion NAME]
"""
from __future__ import annotations
import argparse, collections, glob, hashlib, json, re, sys

FIELDS = ("md", "ts", "lean")
MIN_QUOTE_CHARS = 25
MIN_RUN_WORDS = 5
MIN_RUN_CHARS = 25


def file_hash(path: str) -> str | None:
    try:
        with open(path, "rb") as fh:
            return hashlib.sha256(fh.read()).hexdigest()[:12]
    except FileNotFoundError:
        return None


def read(path: str) -> str:
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return ""


def prose_words(text: str) -> str:
    """Lowercase alphabetic words only, space-delimited and space-padded."""
    return " " + " ".join(re.findall(r"[a-z]+", text.lower())) + " "


def prose_runs(quote: str) -> list[str]:
    """Maximal runs of plain English words inside a quoted span."""
    runs: list[str] = []
    for fragment in re.split(r"\.\.\.|…", quote):
        current: list[str] = []
        for token in re.split(r"[^A-Za-z-]+", fragment):
            word = token.strip("-")
            if word and word.isalpha():
                current.append(word.lower())
                continue
            joined = " ".join(current)
            if len(current) >= MIN_RUN_WORDS and len(joined) >= MIN_RUN_CHARS:
                runs.append(joined)
            current = []
        joined = " ".join(current)
        if len(current) >= MIN_RUN_WORDS and len(joined) >= MIN_RUN_CHARS:
            runs.append(joined)
    return runs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true",
                    help="print every unfindable verdict, not just the counts")
    ap.add_argument("--criterion", help="restrict to one criterion id")
    ap.add_argument("--root", default="content", help="tree to scan")
    args = ap.parse_args()

    counts: collections.Counter[str] = collections.Counter()
    per_criterion: collections.Counter[str] = collections.Counter()
    hits: list[tuple[str, str, str, str]] = []

    for sidecar in glob.glob(f"{args.root}/**/*.qa.json", recursive=True):
        stem = sidecar[: -len(".qa.json")]
        current = {f: file_hash(f"{stem}.{f}") for f in FIELDS}
        body = prose_words("\n".join(read(f"{stem}.{f}") for f in FIELDS))
        try:
            with open(sidecar, encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"  ! unreadable {sidecar}: {exc}", file=sys.stderr)
            continue

        for crit, entries in (data.get("criteria") or {}).items():
            if not entries or (args.criterion and crit != args.criterion):
                continue
            entry = entries[-1]
            if entry.get("result") != "fail":
                continue
            kind = (entry.get("reviewer") or {}).get("kind")
            if kind != "agent":
                counts[f"fail_{kind}"] += 1
                continue

            recorded = entry.get("field_hash")
            stale = (not recorded) or any(
                recorded.get(f) and current.get(f) and recorded[f] != current[f]
                for f in FIELDS
            )
            bucket = "stale" if stale else "current"
            counts[bucket] += 1
            if stale and not recorded:
                counts["stale_no_hash"] += 1

            evidence = entry.get("evidence") or entry.get("notes") or ""
            runs = [
                run
                for quote in re.findall(rf"(?<![A-Za-z])'([^']{{{MIN_QUOTE_CHARS},}})'", evidence)
                for run in prose_runs(quote)
            ]
            if not runs:
                counts[f"{bucket}_undecidable"] += 1
            elif all(f" {run} " not in body for run in runs):
                counts[f"{bucket}_unfindable"] += 1
                per_criterion[crit] += 1
                hits.append((bucket, stem, crit, runs[0]))
            else:
                counts[f"{bucket}_present"] += 1

    print(f"agent-kind FAIL verdicts : {counts['stale'] + counts['current']}")
    for bucket, label in (("stale", "STALE (hash mismatch/absent)"),
                          ("current", "current (hash matches disk)")):
        suffix = (f"   [{counts['stale_no_hash']} carry no field_hash]"
                  if bucket == "stale" else "")
        print(f"  {label:29s}: {counts[bucket]}{suffix}")
        print(f"      quoted prose UNFINDABLE  : {counts[f'{bucket}_unfindable']}")
        print(f"      quoted prose present     : {counts[f'{bucket}_present']}")
        print(f"      no quotable prose run    : {counts[f'{bucket}_undecidable']}")
    print(f"  script-kind FAIL verdicts    : {counts['fail_script']}"
          "   (recomputed by qa-sweep; not counted above)")
    print("\nThese are TRIAGE CANDIDATES, not a defect count — the tool cannot tell")
    print("a quotation of the block from the reviewer's own prose set in quotes.")
    print("Confirm each against `git log -p` on the block before acting.")

    if per_criterion:
        print("\nunfindable by criterion:")
        for crit, n in per_criterion.most_common():
            print(f"  {n:5d}  {crit}")
    if args.list:
        print("\nunfindable verdicts:")
        for bucket, stem, crit, run in sorted(hits):
            print(f"  [{bucket}] {stem}\n    {crit}: “{run[:120]}…”")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
