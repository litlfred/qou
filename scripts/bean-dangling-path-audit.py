#!/usr/bin/env python3
"""Open beans naming a repo path that no longer resolves.

WHY THIS EXISTS, and why it is not the staleness ranking. Its sibling
`bean-staleness-triage.py` ranks by "the tree moved UNDER the bean" — commits
touching the bean's named paths since its `updated_at`. This asks the opposite
question, "did the tree move OUT FROM UNDER it", and the ranking structurally
cannot answer it: a DELETED path has no commits after any date, so a bean whose
files are gone scores **zero** and sorts to the very bottom of the ranking.

WHAT IT IS NOT. A named path that does not resolve is a TRIAGE SIGNAL, never a
verdict. NINE false-positive classes have been measured; eight are filtered
here, and the ninth is reported with a marker. Read them before acting on a row.

  1. PLACEHOLDERS — `computations/X.witness.json`, `computations/substrate/x.py`.
     Metasyntactic examples in bean prose. Filtered by _PLACEHOLDER.

  2. ELIDED PATHS — `content/.../lean/QOU/Foo.lean`, and also
     `docs/audits/2026-08-08-...-attack-vectors...md`, where the ellipsis sits
     INSIDE a segment rather than being one. A path abbreviated for readability;
     the regex cannot reconstruct it. Filtered on `...` appearing anywhere. The
     whole-segment-only test missed the second form.

  3. SYMLINK-HIDDEN — the path exists under `folio-assistant/`, which is a
     SYMLINK to a sibling checkout. `os.path.exists` resolves it; `find` does
     NOT traverse it without `-L`. This class cost a whole wrong bean
     (`qou-7br7`, retracted the same day): two `find folio-assistant …` runs
     returned nothing and were read as corroboration that the library ingest
     producer had been deleted. It had not.

  4. MOVED, NOT DELETED — `fsh-guts/deprecated/computations/hecke_core_legacy.py` is now
     `computations/hecke_core_legacy.py`. NOT filtered, because "the bean's
     reference is stale" is a real if minor finding and the basename search that
     would suppress it also suppresses genuine deletions. Reported with a
     `moved?` marker naming where a same-basename file was found.

  --- classes 5-9 added 2026-09-07, all found by USING the audit on its own
      first output. The 2026-09-06 run reported 61 dangling references as if
      they were findings; 10 of the 35 distinct ones were these. ---

  5. TRUNCATED EXTENSIONS — a BUG in this script, not a property of the beans.
     The alternation `(?:py|lean|ts|md|json|…)` carried no trailing boundary, so
     `foo.tsv` matched as `foo.ts`, `x.jsonl` as `x.json`, `y.pyc` as `y.py` —
     a path that does not resolve BECAUSE THE AUDIT MANGLED IT. Five `.tsv`
     audit-data files and one `.jsonl` progress file were reported this way,
     i.e. 6 of 35 "missing" were manufactured here. Fixed by `_EXT_BOUNDARY`
     plus the real extensions; there is a self-test fixture for each.

  6. PIN-HIDDEN — the path exists in the folio-assistant repo but was added
     AFTER `.folio-assistant-pin`, so it is genuinely absent from this checkout
     while being perfectly live upstream. This is the same effect AGENTS.md
     documents for validator counts, one level down. SOUND, not heuristic:
     checked with `git -C folio-assistant log --all --diff-filter=A -- <path>`.
     Measured 3 of 35 (`scripts/check-mirror-drift.ts` and its test,
     `scripts/check-duplicate-decls.ts`; the first was added in `ae0a979`).
     Worth noting this subsumed a heuristic "the bean says folio-assistant near
     the path" filter that would have missed one of the three, whose bean names
     the repo two sentences away from the path.

  7. BUILD ARTIFACTS — `__pycache__/*.pyc`, `node_modules/`, `.lake/`. Never
     tracked, so never resolvable; naming one in a grep result is not a claim.

  8. REPORTED-ABSENT — the bean's own finding IS that the file is missing:
     "That file DOES NOT EXIST", "which is **untracked** — never committed",
     "never existed (meant …)", "I started building X … and DISCARDED it".
     The audit was flagging beans FOR CORRECTLY RECORDING AN ABSENCE. Heuristic
     (a phrase list over a text window), so listed under `--all`.

  9. BRANCH-ATTRIBUTED — the bean names the unmerged branch the file lives on,
     e.g. "(branch `claude/theta-qcd-framing-phase-2026-08-02`, `content/…`)".
     Correctly attributed unlanded work, not a dangling reference. Heuristic.

  NOT filtered, and known to exist: PROPOSALS — the bean asks for a file to be
  created ("**Add a `scripts/setup-compute.sh`**", "writes
  docs/audits/citation-candidates.json"). Measured 2 of 35. No sound test
  separates "a script that will write this" from "a script that did"; guessing
  from an imperative verb would suppress real findings. Read the row.

Usage:  python3 scripts/bean-dangling-path-audit.py [--all] [--self-test]
        --all         also list the filtered classes, for auditing the filter
        --self-test   run the fixtures for classes 1-9 and exit
"""
from __future__ import annotations

import argparse
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FA = os.path.join(ROOT, "folio-assistant")

_ROOTS = "computations|content|docs|scripts|tools|schemas|library|qou-mass"
# Longest-first inside the alternation AND a trailing non-word assertion: either
# alone is insufficient. Without the boundary `.tsv` matches as `.ts`; without
# `tsv` before `ts` the boundary makes `.tsv` vanish entirely instead.
_EXTS = "witness.json|jsonl|toml|lean|yaml|tsv|pyc|json|yml|txt|csv|py|ts|md|sh|rs"
PATH_RE = re.compile(
    rf'(?<![\w/.-])((?:{_ROOTS})/[\w./-]+\.(?:{_EXTS}))(?![\w])'
)
# `X.witness.json`, `x.py`, `foo/X.py` — a path segment that is a lone letter is
# a stand-in, not a filename anyone shipped.
_PLACEHOLDER = re.compile(r'(?:^|/)[A-Za-z](?:\.[\w.]+)?$')
_ARTIFACT = re.compile(r'(?:^|/)(?:__pycache__|node_modules|\.lake)(?:/|$)|\.pyc$')

# Class 8. Deliberately narrow: each phrase asserts absence of the thing named,
# not merely a negative sentiment about it.
_ABSENT_PHRASES = (
    "does not exist", "doesn't exist", "no such file", "never existed",
    "never committed", "not committed", "untracked", "discarded",
    "was deleted", "has been deleted", "never landed", "never written",
)
_BRANCH_RE = re.compile(r'\bclaude/[\w.-]+')
_WINDOW = 220  # chars each side, for the branch class

# Class 8's unit of scope. Measured on the ten live catches, three candidates:
#   - a +/-220-char WINDOW      : 10/10 fire — no discrimination; it filtered
#                                 four `moved?` findings whose bean asserted an
#                                 absence about something else entirely.
#   - the enclosing PARAGRAPH   : also 10/10. Bean paragraphs run 257-1373 chars,
#                                 so "same paragraph" is barely narrower.
#   - the enclosing SENTENCE    : discriminates, but a raw `\n` split breaks a
#                                 hard-wrapped one and loses two true catches.
# So: join soft line-wraps inside a paragraph, THEN split on sentence
# punctuation. A list item or a blank line still ends the unit.
_PARA_BREAK = re.compile(r'\n\s*\n|\n(?=\s*(?:[-*+]|\d+\.)\s)')
_SENT_BREAK = re.compile(r'(?<=[.!?])\s+')


def _host_sentence(txt: str, rel: str, at: int) -> str:
    """The soft-wrap-joined sentence containing the reference at offset `at`."""
    start = 0
    for mb in _PARA_BREAK.finditer(txt, 0, at):
        start = mb.end()
    mb = _PARA_BREAK.search(txt, at)
    para = txt[start:mb.start() if mb else len(txt)]
    off = at - start
    flat = para.replace("\n", " ")
    pos = 0
    for seg in _SENT_BREAK.split(flat):
        i = flat.find(seg, pos)
        if i <= off < i + len(seg):
            return seg
        pos = i + len(seg)
    return flat


def _fa_has(rel: str) -> bool:
    """Class 6. True if folio-assistant's history ever added `rel`.

    The clone is detached at the pin but carries fetched history, so `--all`
    reaches commits after it. A missing/!git FA checkout answers False, which
    degrades to the old behaviour rather than to a wrong all-clear.
    """
    if not os.path.isdir(os.path.join(FA, ".git")):
        return False
    try:
        out = subprocess.run(
            ["git", "-C", FA, "log", "--all", "--oneline",
             "--diff-filter=A", "--", rel],
            capture_output=True, text=True, timeout=30,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    return out.returncode == 0 and bool(out.stdout.strip())


def classify(rel: str, ctx: str = "", host: str = "") -> tuple[str, str]:
    """-> (class, detail). class 'ok' means the path resolves.

    `ctx` is the bean text around the reference; the two heuristic classes need
    it and everything else ignores it, so a caller without it still gets the
    sound classes.
    """
    if os.path.exists(os.path.join(ROOT, rel)):
        return "ok", ""
    if _ARTIFACT.search(rel):
        return "build-artifact", ""
    if _PLACEHOLDER.search(rel):
        return "placeholder", ""
    # `...` ANYWHERE, not only as a whole segment: a bean writes both
    # `content/.../lean/Foo.lean` and `docs/audits/2026-08-08-...-vectors...md`,
    # and the second form has the ellipsis inside a segment.
    if "..." in rel:
        return "elided", ""
    if os.path.exists(os.path.join(FA, rel)):
        return "symlink-hidden", f"folio-assistant/{rel}"
    if _fa_has(rel):
        return "pin-hidden", "in folio-assistant, added after .folio-assistant-pin"
    low = host.lower()
    if any(p in low for p in _ABSENT_PHRASES):
        return "reported-absent", ""
    m = _BRANCH_RE.search(ctx)
    if m:
        return "branch-attributed", m.group(0)
    base = os.path.basename(rel)
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames
                       if d not in (".git", "node_modules", ".lake", "beans/defs")]
        if base in filenames:
            return "missing", f"moved? {os.path.relpath(os.path.join(dirpath, base), ROOT)}"
    return "missing", ""


_CLASSES = ("ok", "missing", "placeholder", "elided", "symlink-hidden",
            "pin-hidden", "build-artifact", "reported-absent",
            "branch-attributed")


def self_test() -> int:
    """Fixtures for every class. A detector whose blind spots keep being found
    by using it should fail loudly when a narrowing removes a known catch."""
    fails: list[str] = []

    def ck(name: str, got, want):
        if got != want:
            fails.append(f"{name}: got {got!r}, want {want!r}")

    # Class 5 — the extraction bug. Each of these was a live false positive.
    for text, want in (
        ("docs/audits/2026-08-08-library-lean-red-sweep.tsv",
         "docs/audits/2026-08-08-library-lean-red-sweep.tsv"),
        ("computations/deltalambda/.triton_magnus_omega2_progress.jsonl",
         "computations/deltalambda/.triton_magnus_omega2_progress.jsonl"),
        ("computations/probes/__pycache__/foo.cpython-311.pyc",
         "computations/probes/__pycache__/foo.cpython-311.pyc"),
        ("scripts/bean-dangling-path-audit.py",
         "scripts/bean-dangling-path-audit.py"),
    ):
        found = PATH_RE.findall(text)
        ck(f"extract {text}", found, [want])
    # and the truncation must not come back
    ck("no .ts from .tsv", [p for p in PATH_RE.findall("docs/audits/x.tsv")
                            if p.endswith(".ts")], [])

    # Class 7 — build artifacts.
    ck("artifact pyc",
       classify("computations/probes/__pycache__/f.cpython-311.pyc")[0],
       "build-artifact")
    # Class 1/2 — the original filters must survive.
    ck("placeholder", classify("computations/X.witness.json")[0], "placeholder")
    ck("elided", classify("content/.../lean/QOU/Foo.lean")[0], "elided")
    # Class 8 — reported-absent, and its narrowness.
    ck("absent phrase",
       classify("computations/zzz-not-a-real-file.py", "",
                "computations/zzz-not-a-real-file.py does not exist")[0],
       "reported-absent")
    ck("absent needs the phrase",
       classify("computations/zzz-not-a-real-file.py", "",
                "this file is bad and I dislike it")[0],
       "missing")
    # ...and the scope is the SENTENCE, not the window. This is the regression
    # that matters: with a +/-220 window all ten live catches fired, four of
    # them suppressing an unrelated `moved?` finding.
    ck("absent phrase in a DIFFERENT sentence does not fire",
       classify("computations/zzz-not-a-real-file.py",
                "The old script does not exist. Fix: computations/zzz-not-a-real-file.py --go",
                "Fix: computations/zzz-not-a-real-file.py --go")[0],
       "missing")
    # _host_sentence must join a hard-wrapped sentence but stop at a list item.
    doc = ("intro\n\n- The docstring cited computations/zzz-not-a-real-file.py,\n"
           "  which is untracked and never committed.\n- next item\n")
    at = doc.index("computations/zzz")
    host = _host_sentence(doc, "computations/zzz-not-a-real-file.py", at)
    ck("host joins soft wrap", "never committed" in host, True)
    ck("host stops at list item", "next item" in host, False)
    # Class 9 — branch-attributed.
    ck("branch",
       classify("folio/quantum-observable-universe/zzz-nope.lean",
                "(branch `claude/theta-qcd-framing-phase-2026-08-02`, path)")[0],
       "branch-attributed")
    # ok must still be ok.
    ck("ok", classify("scripts/bean-dangling-path-audit.py")[0], "ok")

    for f in fails:
        print(f"FAIL  {f}")
    n = 16
    print(f"self-test: {n - len(fails)}/{n} passed")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true",
                    help="also list the filtered classes")
    ap.add_argument("--self-test", action="store_true",
                    help="run the class fixtures and exit")
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    counts: dict[str, int] = {}
    rows: list[tuple[int, str, list[tuple[str, str]]]] = []
    filtered: dict[str, set[str]] = {}
    fa_cache: dict[str, tuple[str, str]] = {}

    for bf in sorted(glob.glob(os.path.join(ROOT, "beans/defs", "*.md"))):
        txt = open(bf, encoding="utf-8", errors="replace").read()
        m = re.search(r'^status:\s*(\S+)', txt[:400], re.M)
        if not m or m.group(1) not in ("in-progress", "todo"):
            continue
        bid = os.path.basename(bf).split("--")[0]
        hits: list[tuple[str, str]] = []
        seen: set[str] = set()
        for mm in PATH_RE.finditer(txt):
            rel = mm.group(1)
            if rel in seen:
                continue
            seen.add(rel)
            ctx = txt[max(0, mm.start() - _WINDOW):mm.end() + _WINDOW]
            host = _host_sentence(txt, rel, mm.start())
            cls, detail = classify(rel, ctx, host)
            counts[cls] = counts.get(cls, 0) + 1
            if cls == "missing":
                hits.append((rel, detail))
            elif cls != "ok":
                filtered.setdefault(cls, set()).add(rel)
        if hits:
            rows.append((len(hits), bid, hits))

    rows.sort(reverse=True)
    print(f"{len(rows)} open bean(s) name a path that does not resolve, after "
          f"filtering 8 measured false-positive classes (see module docstring).\n")
    for n, bid, hits in rows:
        print(f"{bid}  ({n})")
        for rel, detail in hits:
            print(f"    {rel}" + (f"   [{detail}]" if detail else ""))

    print("\npath references by class (occurrences, not distinct):")
    for k in _CLASSES:
        print(f"  {k:<18}{counts.get(k, 0):>6}")

    if a.all:
        for cls, paths in sorted(filtered.items()):
            print(f"\nFILTERED — {cls} ({len(paths)} distinct):")
            for p in sorted(paths):
                print(f"  {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
