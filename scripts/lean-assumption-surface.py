#!/usr/bin/env python3
"""Report the Lean tree's REAL assumption surface — and refuse to be fooled by prose.

WHY THIS EXISTS
---------------
On 2026-08-25 an agent (me) reported "~500 `sorry` tokens across 36 modules,
`SpechtStandardBasisCore` alone has 106" into a scope doc, a bean and a PR body.
The true count is **zero**. The figure came from `grep -c sorry`, which matches the
WORD — and this corpus documents its own history heavily, so files that once carried
a sorry still discuss it at length. `SpechtStandardBasisCore` supplied 101 phantom
hits and has no real sorry; its own docstring says "its single honest straightening
stub", which I read past.

Two lessons are baked into this script:

1. **Strip comments before counting.** A docstring is not a proof obligation.
2. **A sorry count is NOT the assumption surface.** Zero sorries is compatible with
   substantial assumed mathematics, because the obligation can live in an `axiom`
   declaration, a `native_decide`, or a `: True :=` body — none of which contain the
   token `sorry`. AGENTS.md §"Axiomatization is NOT a Proof" is about exactly this.
   Measured here the same day: 0 sorries, but **24 `axiom` declarations** and one
   `native_decide`. Reporting "zero sorries" alone would have been true and
   misleading in the other direction.

`--selftest` exercises the parser on every output shape, including the three comment
forms that produced the phantom count. It needs no Lean and no oleans.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

DEFAULT_ROOT = pathlib.Path("content/quantum-observable-universe/lean/QOU")
# The whole Lean corpus, for the scope line. `DEFAULT_ROOT` is the QOU LIBRARY only;
# content blocks carry sibling `.lean` files outside it, and they hold the large
# majority of the corpus's axioms. Reporting the library figure without saying so
# understates the assumption surface by an order of magnitude -- measured 2026-08-26,
# 22 in the library against 198 corpus-wide. Never quote one for the other.
CORPUS_ROOT = pathlib.Path("content")

PATTERNS = {
    "sorry": re.compile(r"(?<![\w.])sorry(?![\w])"),
    "sorryAx": re.compile(r"(?<![\w.])sorryAx(?![\w])"),
    "axiom": re.compile(r"^\s*axiom\s+\w"),
    "native_decide": re.compile(r"(?<![\w.])native_decide(?![\w])"),
    "true_vacuity": re.compile(r":\s*True\s*:="),
}


def strip_comments(text: str) -> list[str]:
    """Return the source with `--` and `/- -/` content blanked, line numbering intact."""
    out: list[str] = []
    in_block = False
    for line in text.split("\n"):
        s = line
        if in_block:
            if "-/" in s:
                in_block = False
                s = s.split("-/", 1)[1]
            else:
                out.append("")
                continue
        while "/-" in s:
            before, rest = s.split("/-", 1)
            if "-/" in rest:
                s = before + rest.split("-/", 1)[1]
            else:
                s = before
                in_block = True
                break
        out.append(s.split("--", 1)[0])
    return out


def scan(root: pathlib.Path) -> dict:
    # Exclude `.lake/` or the walk swallows Mathlib and every vendored package.
    # Measured 2026-08-26: including it reported 418 axioms over 11198 files for
    # `content/`, against 198 over 3185 once excluded -- i.e. it was mostly counting
    # Mathlib's axioms and calling them ours.
    files = sorted(f for f in root.rglob("*.lean") if ".lake" not in f.parts)
    hits: dict[str, list] = {k: [] for k in PATTERNS}
    for f in files:
        try:
            code = strip_comments(f.read_text())
        except Exception:
            continue
        for key, rx in PATTERNS.items():
            for i, ln in enumerate(code, 1):
                if rx.search(ln):
                    hits[key].append((str(f), i, ln.strip()[:100]))
    return {"files": len(files), "hits": hits}


_SELFTEST = [
    ("bare sorry", "theorem t : True := by\n  sorry\n", "sorry", 1),
    ("tactic-mode sorry", "theorem t : True := by\n  simp; sorry\n", "sorry", 1),
    ("term-mode sorry", "theorem t : True := sorry\n", "sorry", 1),
    ("line-comment sorry", "theorem t : True := by\n  trivial -- sorry here\n", "sorry", 0),
    ("block-comment sorry", "/- a sorry -/\ntheorem t : True := trivial\n", "sorry", 0),
    ("docstring sorry", "/-! the sorry is gone -/\ntheorem t : True := trivial\n", "sorry", 0),
    ("multiline docstring", "/-!\nline one sorry\nline two sorry\n-/\ndef f := 1\n", "sorry", 0),
    ("axiom decl", "axiom foo : True\n", "axiom", 1),
    ("axiom in comment", "-- axiom foo : True\n", "axiom", 0),
    ("native_decide", "example : True := by native_decide\n", "native_decide", 1),
    # BOTH lines are vacuity and both must be counted: the `def`-disguised form is the
    # documented dodge (AGENTS.md §1a `def-disguised-true`), so a detector that scored
    # only the `theorem` would miss the case the rule was written for. The first draft
    # of this row expected 1 and the selftest caught it — the expectation was wrong,
    # not the parser.
    ("True vacuity, theorem + def", "theorem t : True := trivial\ndef d : True := trivial\n",
     "true_vacuity", 2),
]


def selftest() -> int:
    bad = 0
    for label, src, key, want in _SELFTEST:
        code = strip_comments(src)
        got = sum(1 for ln in code if PATTERNS[key].search(ln))
        if got != want:
            print(f"  [FAIL] {label:22} {key}: got {got}, want {want}")
            bad += 1
        else:
            print(f"  [ok  ] {label:22} {key}={got}")
    print("assumption-surface selftest: " + ("PASS" if not bad else f"{bad} FAILURE(S)"))
    return 0 if not bad else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=pathlib.Path, default=DEFAULT_ROOT)
    ap.add_argument("--selftest", action="store_true",
                    help="exercise the parser on every output shape; needs no Lean")
    ap.add_argument("--list", action="store_true", help="print every hit, not just counts")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    if not args.root.is_dir():
        print(f"assumption-surface: no such root {args.root}", file=sys.stderr)
        return 2

    r = scan(args.root)
    h = r["hits"]
    print(f"scanned {r['files']} .lean files under {args.root}")
    if CORPUS_ROOT.is_dir() and args.root != CORPUS_ROOT:
        corpus = scan(CORPUS_ROOT)
        ca, cf = len(corpus["hits"]["axiom"]), corpus["files"]
        print(f"  SCOPE: this is a SUBTREE. Corpus-wide ({CORPUS_ROOT}, {cf} files): "
              f"{ca} axioms. Quote the figure whose scope you name.")
    print()
    print("  PROOF-OBLIGATION MARKERS (a sorry count alone is NOT the surface)")
    for key in ("sorry", "sorryAx", "true_vacuity"):
        print(f"    {key:16}: {len(h[key])}")
    print("\n  ASSUMED MATHEMATICS (invisible to a sorry count)")
    for key in ("axiom", "native_decide"):
        print(f"    {key:16}: {len(h[key])}")

    if h["axiom"]:
        by_dir: dict[str, int] = {}
        for f, _, _ in h["axiom"]:
            top = pathlib.Path(f).relative_to(args.root).parts[0]
            by_dir[top] = by_dir.get(top, 0) + 1
        print("\n  axiom declarations by area:")
        for d, n in sorted(by_dir.items(), key=lambda kv: -kv[1]):
            print(f"    {n:4}  {d}")

    if args.list:
        for key in ("sorry", "axiom", "native_decide", "true_vacuity"):
            if h[key]:
                print(f"\n--- {key} ---")
                for f, i, t in h[key]:
                    print(f"  {f}:{i}\n      {t}")
    # Informational by design: the counts are a report, not a ratchet.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
