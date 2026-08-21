#!/usr/bin/env python3
"""
check-citation-keys — resolve every citation key in the corpus, on all three
paths, and report the ones that resolve to nothing.

The content pipeline validates `\\cite{}` in a `.md`. It does not validate
the other two paths a block can cite by, and both are load-bearing:

    .md    \\cite{key}          <- checked by the pipeline
    .ts    cites: ["key", ...]  <- unchecked
    .lean  -- Ref: [key]        <- unchecked

AGENTS.md §1 is explicit about the Lean one — "The `[key]` must match an
entry in `content/schema/references.ts` exactly (case-sensitive)" and "A
`sorry` without `-- Ref:` is always a review failure". A `sorry` carrying a
key that resolves to nothing satisfies the second rule while breaking the
first: it reads as cited and is not.

## Not everything in brackets is a bibliography key

Counting "key not in references.ts" as broken over-reports by roughly 20x,
because four conventions legitimately put something else there, and three of
them are documented:

  * **`[manuscript]`** — AGENTS.md §1: "If no published reference exists, use
    `[manuscript]` and cite chapter/section." 3,525 sites.
  * **A cross-paper block label**, `paper-dir:label`, per the
    §"Cross-paper references" table.
  * **A same-paper block label**, bare — the same table's first row. Checked
    against the labels that actually exist, so a typo is still caught: this
    is how `prop:jet-convergence-classical-limit` was found, where the block
    exists as a `conj:`.
  * **`[tag] <in-repo-path>`** — the `[manuscript]` shape generalised, where
    the tag names the kind of thing and the path says where it is:

        -- Ref: [audit] docs/audits/2026-06-09-metallic-q-csc-phase-synthesis.md
        -- Ref: [probe] computations/metallic_q_symbolic_galois_proofs.py
        -- Ref: [metallichierarchy] QOU.AlgebraicSubstrate.MetallicHierarchy

    Undocumented but in live use, and it resolves — the path is checked to
    exist, so a stale one is still reported. Only a bare tag with nothing
    resolvable after it is a bibliography claim.

Report the number this script prints, not a raw "key not in references.ts"
count.

## It does not tell you references.ts is well-formed

Entry ids are read by regex over the source, deliberately — the file quotes
`ref({ id: ... })` inside its own comments and a scan has to skip those. The
cost is that a references.ts which does not PARSE still scans normally here.
Nothing else catches that either: `run-validate.ts` reports "Valid" on a
deliberately broken one (measured, bean qou-3vgs). Importing the module is
what fails, so run a script that executes the entries when you need that
answer.

Usage:
    scripts/check-citation-keys.py            # report
    scripts/check-citation-keys.py --strict   # exit 1 if anything dangles
    scripts/check-citation-keys.py --json
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFS = os.path.join(REPO, "content", "schema", "references.ts")

SENTINELS = {"manuscript"}
LABEL_RX = re.compile(r"^(conj|def|thm|lem|prop|cor|rem|ex|sim|alg):")
XPAPER_RX = re.compile(r"^([a-z0-9][a-z0-9-]*):((?:conj|def|thm|lem|prop|cor|rem|ex|sim|alg):.+)$")


def strip_comments(src: str) -> str:
    """Blank `//` and `/* */`, leaving string literals alone.

    references.ts quotes code in its own comments, including a `ref({ id: ... })`
    that a flat scan reads as a live entry; and its JSDoc header contains an
    apostrophe that opens a string literal swallowing 240 lines if `/* */` is
    not handled.
    """
    out: list[str] = []
    i, n, quote = 0, len(src), None
    while i < n:
        c = src[i]
        if quote:
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(src[i + 1]); i += 2; continue
            if c == quote:
                quote = None
            i += 1; continue
        if c in "\"'`":
            quote = c; out.append(c); i += 1; continue
        if c == "/" and i + 1 < n and src[i + 1] == "/":
            j = src.find("\n", i)
            if j == -1: break
            out.append("\n"); i = j + 1; continue
        if c == "/" and i + 1 < n and src[i + 1] == "*":
            j = src.find("*/", i + 2)
            if j == -1: break
            out.append("\n" * src.count("\n", i, j + 2)); i = j + 2; continue
        out.append(c); i += 1
    return "".join(out)


def entry_ids() -> set[str]:
    return set(re.findall(r'\bid:\s*"([^"]+)"',
                          strip_comments(open(REFS, encoding="utf-8").read())))


def block_labels() -> set[str]:
    out: set[str] = set()
    for path in glob.glob(os.path.join(REPO, "content", "**", "*.ts"), recursive=True):
        out.update(re.findall(r'label:\s*"([^"]+)"',
                              open(path, encoding="utf-8", errors="replace").read()))
    return out


def resolves_in_repo(tail: str) -> str | None:
    """A path or Lean module named after the tag, which exists."""
    for cand in re.findall(r"[\w./-]+", tail):
        c = cand.rstrip(".,;:")
        if "/" in c and os.path.exists(os.path.join(REPO, c)):
            return c
        if re.match(r"^(QOU|UGB|Fred2005)\.", c):
            return c
    return None


def scan() -> list[dict]:
    sites: list[dict] = []
    for path in glob.glob(os.path.join(REPO, "content", "**", "*.md"), recursive=True):
        t = open(path, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"\\cite[tp]?\*?(?:\[[^\]]*\])*\{([^}]*)\}", t):
            for k in m.group(1).split(","):
                sites.append({"key": k.strip(), "kind": "md-cite", "path": path,
                              "line": t[:m.start()].count("\n") + 1, "tail": ""})
    for path in glob.glob(os.path.join(REPO, "content", "**", "*.ts"), recursive=True):
        t = open(path, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"cites:\s*\[([^\]]*)\]", t):
            for k in m.group(1).split(","):
                k = k.strip().strip("\"'")
                if k:
                    sites.append({"key": k, "kind": "ts-cites", "path": path,
                                  "line": t[:m.start()].count("\n") + 1, "tail": ""})
    for path in glob.glob(os.path.join(REPO, "content", "**", "*.lean"), recursive=True):
        t = open(path, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"--\s*Ref:\s*\[([^\]]+)\]([^\n]*)", t):
            sites.append({"key": m.group(1).strip(), "kind": "lean-ref", "path": path,
                          "line": t[:m.start()].count("\n") + 1,
                          "tail": m.group(2).strip()})
    return sites


def classify(sites: list[dict], ids: set[str], labels: set[str]) -> dict:
    buckets: dict[str, list[dict]] = {k: [] for k in
                                      ("entry", "sentinel", "block-label",
                                       "cross-paper", "in-repo-pointer", "dangling")}
    for s in sites:
        k = s["key"]
        if k in ids:
            buckets["entry"].append(s)
        elif k in SENTINELS:
            buckets["sentinel"].append(s)
        elif XPAPER_RX.match(k):
            buckets["cross-paper"].append(s)
        elif LABEL_RX.match(k):
            buckets["block-label" if k in labels else "dangling"].append(s)
        elif s["tail"] and resolves_in_repo(s["tail"]):
            buckets["in-repo-pointer"].append(s)
        else:
            buckets["dangling"].append(s)
    return buckets


def main() -> int:
    ap = argparse.ArgumentParser(description="Resolve every citation key in the corpus")
    ap.add_argument("--strict", action="store_true", help="exit 1 if anything dangles")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    ids, labels = entry_ids(), block_labels()
    sites = scan()
    b = classify(sites, ids, labels)

    if args.json:
        print(json.dumps({k: v for k, v in b.items()}, indent=1))
        return 1 if (args.strict and b["dangling"]) else 0

    print(f"{len(sites)} citation sites across content/  "
          f"({len(ids)} entries, {len(labels)} block labels)\n")
    for name, why in (("entry", "resolve to a references.ts entry"),
                      ("sentinel", "are the [manuscript] sentinel (AGENTS.md §1)"),
                      ("block-label", "name a content block in this paper"),
                      ("cross-paper", "name a block in a sibling paper"),
                      ("in-repo-pointer", "are [tag] + an in-repo path that exists")):
        print(f"  {len(b[name]):>5}  {why}")
    d = b["dangling"]
    print(f"  {len(d):>5}  RESOLVE TO NOTHING\n")
    by_key: dict[str, list[dict]] = {}
    for s in d:
        by_key.setdefault(s["key"], []).append(s)
    for key, ss in sorted(by_key.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        kinds = ",".join(sorted({s["kind"] for s in ss}))
        print(f"  {len(ss):>3}  {kinds:<9}  {key}")
        for s in ss[:2]:
            print(f"          {os.path.relpath(s['path'], REPO)}:{s['line']}")
    print(f"\n{len(by_key)} distinct unresolved keys over {len(d)} sites")
    return 1 if (args.strict and d) else 0


if __name__ == "__main__":
    raise SystemExit(main())
