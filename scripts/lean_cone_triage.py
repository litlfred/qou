#!/usr/bin/env python3
"""lean_cone_triage.py — summarise a `lean-direct-cone.sh --all -k --report` run.

Turns the per-module TSV into the numbers a corpus survey actually needs:

* the **measured** red count (modules compiled with every dependency's olean
  present, which still failed) — a hard lower bound on genuine reds;
* the **blocked** count (never compiled, because an upstream module was red) —
  status genuinely *unknown*, so `error + blocked` is the upper bound;
* per-subtree breakdown and the distinct error shapes;
* the **sorry-free illusion** count — modules that never type-checked yet carry
  zero `sorry` tokens, so every source-level audit reads them as clean.

That last one is the number this tool exists to surface. `grep -c sorry` is a
**screen**; the proof term is the **verdict**. A module behind a blocked cone
never produces a proof term at all, so the screen reads green and the verdict is
simply unavailable — and nothing else in the repo distinguishes the two.

Measured on 2026-08-30: one broken module (`QOU.MathlibExt.QIntegerCanonical`)
blocked **210** modules, **179** of which carried zero sorry tokens. Fixing it
revealed two more errors that had been hidden behind it, and fixing *those*
revealed a third in the root aggregator. So the count is a **lower bound that
moves**: a blocked cone hides not only unverified modules but other errors, and
this class must be swept **iteratively** rather than measured once. Beans
`qou-lksc`, `qou-dsif`.

Usage: scripts/lean_cone_triage.py /tmp/qou-cone-all.tsv [--log-dir DIR]
                                   [--lean-root DIR]
"""

from __future__ import annotations

import argparse
import collections
import re
from pathlib import Path

# Normalise a lean error line into a coarse "shape" for grouping.
SHAPES: list[tuple[str, re.Pattern]] = [
    ("invalid-field", re.compile(r"Invalid field .*environment does not contain", re.S)),
    ("already-declared", re.compile(r"has already been declared")),
    ("unknown-identifier", re.compile(r"(?i)unknown (identifier|constant|declaration)")),
    ("unknown-namespace-or-attr", re.compile(r"(?i)unknown (namespace|attribute|tactic)")),
    ("type-mismatch", re.compile(r"type mismatch|has type\b.*but is expected")),
    ("unsolved-goals", re.compile(r"unsolved goals")),
    ("tactic-failed", re.compile(r"tactic '(\w+)' failed|simp made no progress|linarith failed")),
    ("function-expected/app", re.compile(r"function expected|application type mismatch")),
    ("failed-to-synth-instance", re.compile(r"failed to synthesize")),
    ("motive/recursion", re.compile(r"motive is not type correct|maximum recursion")),
    ("universe-mismatch", re.compile(r"universe (level )?(mismatch|metavariable)")),
    ("deterministic-timeout", re.compile(r"deterministic timeout|maximum number of heartbeats")),
    ("missing-olean", re.compile(r"object file .* does not exist")),
    ("syntax-error", re.compile(r"unexpected token|expected .* term|unterminated")),
    ("sorry", re.compile(r"declaration uses 'sorry'")),
]


# An error of the form "object file '<path>' of module <M> does not exist" where
# <M> is NOT a QOU module means the *environment* is short an olean (e.g. the
# restored lake-cache payload has 6990 Mathlib oleans but not the top-level
# `Mathlib.olean` aggregator). That is an environment gap, not a corpus defect,
# and must never be counted as a genuine red.
ENV_GAP_RE = re.compile(r"object file '[^']*' of module ((?!QOU\b)[\w.]+) does not exist")


ERR_LINE_RE = re.compile(r"^\S*?:\d+:\d+: error(?:\([^)]*\))?: (.*)$", re.M)


SORRY_TOKEN = re.compile(r"\bsorry\b")


def sorry_tokens(path: Path) -> int | None:
    """Count real `sorry` tokens in a source file.

    `None` when the file is absent. The phrase "sorry-free" is excluded: this
    corpus writes it constantly in prose, and counting it inverts the verdict on
    exactly the files most likely to claim cleanliness.
    """
    if not path.is_file():
        return None
    n = 0
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        for m in SORRY_TOKEN.finditer(line):
            if line[m.end():m.end() + 5] in ("-free", "_free"):
                continue
            n += 1
    return n


def error_lines(text: str) -> list[str]:
    """Only the compiler's own `error:` payloads — matching against the whole log
    lets file paths and docstrings ('...ObservableUniverse...') hit the shape
    patterns and mis-bucket everything."""
    return ERR_LINE_RE.findall(text)


def shape_of(text: str) -> str:
    """Bucket on the FIRST compiler error. Later errors in the same file are
    usually knock-ons of the first, so classifying on 'any line matches' would
    attribute a file to whichever pattern happens to sit earliest in SHAPES."""
    lines = error_lines(text)
    payload = lines[0] if lines else text
    for name, rx in SHAPES:
        if rx.search(payload):
            return name
    return "other"


def is_env_gap(text: str) -> str | None:
    m = ENV_GAP_RE.search(text)
    return m.group(1) if m else None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("tsv")
    ap.add_argument("--log-dir", default="/tmp/lean-cone-logs")
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--lean-root",
                    default="folio/quantum-observable-universe/lean",
                    help="root the module names resolve against, for the "
                         "sorry-free-illusion cross-check")
    args = ap.parse_args()

    rows = []
    with open(args.tsv, encoding="utf-8") as fh:
        next(fh)
        for line in fh:
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 5:
                rows.append(dict(zip(
                    ("module", "status", "seconds", "blocker", "error_head"), parts)))

    logdir = Path(args.log_dir)

    # split `error` into genuine corpus reds vs environment olean gaps
    env_gap_mods: set[str] = set()
    for r in rows:
        if r["status"] != "error":
            continue
        lp = logdir / (r["module"] + ".log")
        text = lp.read_text(encoding="utf-8", errors="replace") if lp.is_file() else r["error_head"]
        r["_text"] = text
        g = is_env_gap(text)
        if g:
            r["status"] = "env-gap"
            r["env_missing"] = g
            env_gap_mods.add(r["module"])

    counts = collections.Counter(r["status"] for r in rows)
    total = len(rows)
    ok = counts["ok"] + counts["up-to-date"]
    err = counts["error"]
    blocked = counts["blocked"]
    missing = counts["missing-source"]
    envgap = counts["env-gap"]

    by_blocker = collections.Counter(r["blocker"] for r in rows if r["status"] == "blocked")
    blocked_env = sum(n for b, n in by_blocker.items() if b in env_gap_mods)
    blocked_corpus = blocked - blocked_env

    print(f"total modules                  : {total}")
    print(f"GREEN (compiled clean)         : {ok}")
    print(f"RED, measured directly         : {err}   <- LOWER bound on genuine reds")
    print(f"dangling-import defects        : {missing}")
    print(f"env-gap (missing non-QOU olean): {envgap}   <- environment, NOT a corpus defect")
    print(f"BLOCKED, upstream red          : {blocked_corpus}   <- unknown; would be compiled once the red is fixed")
    print(f"BLOCKED, upstream env-gap      : {blocked_env}   <- unknown; environment-limited")
    print(f"UPPER bound on genuine reds    : {err + missing + blocked_corpus}")
    print(f"never type-checked at all      : {err + missing + envgap + blocked}")
    print()

    for r in rows:
        if r["status"] == "env-gap":
            print(f"  env-gap: {r['module']}  (missing olean: {r['env_missing']})")
    if envgap:
        print()

    if by_blocker:
        print(f"blocked attributed to {len(by_blocker)} distinct root culprits; top:")
        for b, n in by_blocker.most_common(args.top):
            tag = "env-gap" if b in env_gap_mods else "red"
            print(f"  {n:5d}  [{tag}] {b}")
        print()

    bad = [r for r in rows if r["status"] in ("error", "missing-source")]

    def subtree(m: str) -> str:
        p = m.split(".")
        return ".".join(p[:2]) if len(p) > 1 else m

    print("genuine reds by subtree:")
    for s, n in collections.Counter(subtree(r["module"]) for r in bad).most_common():
        print(f"  {n:5d}  {s}")
    print()

    shapes = collections.Counter()
    for r in bad:
        text = r.get("_text") or r["error_head"]
        r["shape"] = shape_of(text)
        shapes[r["shape"]] += 1
    print("genuine reds by error shape:")
    for s, n in shapes.most_common():
        print(f"  {n:5d}  {s}")
    print()

    # --- the sorry-free illusion -------------------------------------------
    #
    # Every module that never type-checked, split by whether a source-level
    # audit would call it clean. The second group is the one that misleads:
    # `grep -c sorry` reads 0 and `#print axioms` cannot run at all.
    lean_root = Path(args.lean_root)
    unchecked = [r for r in rows
                 if r["status"] in ("error", "blocked", "missing-source", "env-gap")]
    illusion, honest, absent = [], [], []
    for r in unchecked:
        n = sorry_tokens(lean_root / (r["module"].replace(".", "/") + ".lean"))
        if n is None:
            absent.append(r)
        elif n == 0:
            illusion.append(r)
        else:
            honest.append(r)

    print("sorry-free illusion (never type-checked, yet reads clean):")
    print(f"  {len(illusion):5d}  zero sorry tokens   <- THE ILLUSION: screen green, no verdict")
    print(f"  {len(honest):5d}  carries a sorry     <- honestly marked as incomplete")
    if absent:
        print(f"  {len(absent):5d}  source not found    <- module name did not resolve under --lean-root")
    print()
    if illusion:
        print("  modules reading sorry-free that were never verified:")
        for r in sorted(illusion, key=lambda r: r["module"])[:args.top]:
            why = r["status"]
            if why == "blocked":
                why = f"blocked by {r['blocker']}"
            print(f"    {r['module']}  ({why})")
        if len(illusion) > args.top:
            print(f"    … and {len(illusion) - args.top} more")
        print()

    print("every genuine red (module | shape | first error line):")
    for r in sorted(bad, key=lambda r: (r.get("shape", ""), r["module"])):
        print(f"  [{r.get('shape','?')}] {r['module']}\n        {r['error_head'][:180]}")


if __name__ == "__main__":
    main()
