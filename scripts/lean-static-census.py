#!/usr/bin/env python3
"""lean-static-census — story L0 (bean qou-4lx3): the static Lean parity baseline.

P-Lean checks 1-3 (docs/audits/2026-10-04-workplan-and-migration/
LEANNODES_report.md §3), all WITHOUT elaborating anything:

  1. byte parity      sha256 of every tracked `.lean` file
  2. declarations     the multiset of fully qualified names per file
                      (heuristic parser: tracks `namespace`/`section`/`end`;
                      it is a parity instrument, not a Lean front end)
  3. lexical counts   `sorry` and `axiom` tokens per file, comments and string
                      literals stripped

READ-ONLY on the corpus. Deterministic: sorted keys and files, no timestamps,
no absolute paths, so two runs on one tree are byte-identical.

Usage:
  python3 scripts/lean-static-census.py                       # census of the working tree -> stdout
  python3 scripts/lean-static-census.py --rev <commit>        # census of a commit, read from git blobs
  python3 scripts/lean-static-census.py --check <commit>      # working tree vs <commit>
      exit 0 IDENTICAL; 1 differs (prints per-file differences)
  add --digest to print only the sha256 of the census JSON.

THE BASELINE IS A COMMIT, NOT A FILE. The census is a pure function of the
tracked `.lean` blobs plus this script, so "the L0 baseline" is "the census at
main@<sha>", re-derivable at any time with --rev. Nothing is stored: publishing
a lone file as qa-reports `main/<sha>` would make it the first (and therefore
standing) entry for that commit, shadowing a later complete `qa:refresh`
(cat-harness qa-reports skill, bean 3hk4). `producerSha256` is recorded, so a
census made by a different version of this script is visibly different.

Measured 2026-10-04 at main 41f7d91d052 (census sha256 8175b24e2ed4…; bean qou-4lx3
carries both): library 2,953 files / 44,908 decls / 0 sorry / 12 axiom; siblings
1,039 / 7,856 / 15 / 101. The analysis's "library 1/24" was a lexical
over-count: it read `sorry`/`axiom` quoted inside docstrings (e.g. the
history blocks of B1HyperbolicRowsTheorem.lean and LpDualityHypothesisClass.lean),
which this script strips.

Check 4 (the elaborated census, G-L5) needs a Lake build and is out of scope.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIBRARY_PREFIX = "folio/quantum-observable-universe/lean/"

DECL_KW = (r"(?:theorem|lemma|def|abbrev|structure|class|inductive|instance|axiom|"
           r"opaque|noncomputable\s+def|example|proposition|corollary)")
MODIFIERS = r"(?:(?:private|protected|noncomputable|partial|unsafe|nonrec|scoped|local)\s+)*"
ATTR = r"(?:@\[[^\]]*\]\s*)*"
DECL_RE = re.compile(rf"^\s*{ATTR}{MODIFIERS}({DECL_KW})\s+([^\s:(\[{{]+)?", re.M)
NS_RE = re.compile(r"^\s*(namespace|section|end)\b\s*([^\s]*)", re.M)


def strip_comments_and_strings(src: str) -> str:
    out, i, n, depth = [], 0, len(src), 0
    while i < n:
        if depth:
            if src.startswith("/-", i):
                depth += 1; i += 2
            elif src.startswith("-/", i):
                depth -= 1; i += 2
            else:
                if src[i] == "\n":
                    out.append("\n")
                i += 1
        elif src.startswith("/-", i):
            depth = 1; i += 2
        elif src.startswith("--", i):
            j = src.find("\n", i)
            i = n if j < 0 else j
        elif src[i] == '"':
            j = i + 1
            while j < n and src[j] != '"':
                j += 2 if src[j] == "\\" else 1
            out.append('""'); i = j + 1
        else:
            out.append(src[i]); i += 1
    return "".join(out)


def declarations(code: str) -> list[str]:
    events = [(m.start(), "ns", m.group(1), m.group(2)) for m in NS_RE.finditer(code)]
    events += [(m.start(), "decl", m.group(1), m.group(2) or "") for m in DECL_RE.finditer(code)]
    stack: list[tuple[str, str]] = []
    names = []
    for _, kind, kw, name in sorted(events):
        if kind == "ns":
            if kw in ("namespace", "section"):
                stack.append((kw, name))
            elif stack:
                stack.pop()
            continue
        if kw == "example" or not name:
            names.append(f"<{kw.split()[-1]}>")
            continue
        if name.startswith("_root_."):
            names.append(name[len("_root_."):])
            continue
        prefix = ".".join(n for k, n in stack if k == "namespace" and n)
        names.append(f"{prefix}.{name}" if prefix else name)
    return names


def blobs(rev: str | None) -> list[tuple[str, bytes]]:
    """(path, bytes) for every tracked .lean file, from the tree or from <rev>."""
    if rev is None:
        files = sorted(subprocess.run(["git", "ls-files", "*.lean"], cwd=ROOT,
                                      capture_output=True, text=True, check=True).stdout.split())
        return [(f, (ROOT / f).read_bytes()) for f in files]
    ls = subprocess.run(["git", "ls-tree", "-r", rev], cwd=ROOT,
                        capture_output=True, text=True, check=True).stdout
    entries = sorted((line.split("\t", 1)[1], line.split()[2]) for line in ls.splitlines()
                     if line.endswith(".lean") and line.split()[1] == "blob")
    proc = subprocess.run(["git", "cat-file", "--batch"], cwd=ROOT, check=True, capture_output=True,
                          input="".join(f"{sha}\n" for _, sha in entries).encode())
    out, buf, i = [], proc.stdout, 0
    for path, _ in entries:
        nl = buf.index(b"\n", i)
        size = int(buf[i:nl].split()[2])
        out.append((path, buf[nl + 1: nl + 1 + size]))
        i = nl + 1 + size + 1
    return out


def census(rev: str | None = None) -> dict:
    per_file, totals = {}, Counter()
    for rel, raw in blobs(rev):
        code = strip_comments_and_strings(raw.decode("utf-8", errors="replace"))
        decls = declarations(code)
        part = "library" if rel.startswith(LIBRARY_PREFIX) else "siblings"
        sorry = len(re.findall(r"\bsorry\b", code))
        axiom = len(re.findall(r"^\s*(?:private\s+|protected\s+)?axiom\b", code, re.M))
        per_file[rel] = {
            "sha256": hashlib.sha256(raw).hexdigest(),
            "decls": dict(sorted(Counter(decls).items())),
            "sorry": sorry,
            "axiom": axiom,
        }
        totals[f"{part}.files"] += 1
        totals[f"{part}.decls"] += len(decls)
        totals[f"{part}.sorry"] += sorry
        totals[f"{part}.axiom"] += axiom
    return {
        "$schema": "qou-lean-static-census/v1",
        "producer": "scripts/lean-static-census.py",
        "producerSha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "checks": ["byte-parity", "declaration-multiset", "lexical-sorry-axiom"],
        "totals": dict(sorted(totals.items())),
        "files": per_file,
    }


def dump(d: dict) -> str:
    return json.dumps(d, indent=1, sort_keys=True, ensure_ascii=False) + "\n"


def diff(base: dict, now: dict) -> list[str]:
    out = []
    bf, nf = base["files"], now["files"]
    for p in sorted(set(bf) | set(nf)):
        if p not in nf:
            out.append(f"- removed {p}")
        elif p not in bf:
            out.append(f"+ added {p}")
        else:
            for k in ("sha256", "decls", "sorry", "axiom"):
                if bf[p][k] != nf[p][k]:
                    out.append(f"~ {p}: {k} differs")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--rev", help="census of this commit instead of the working tree")
    ap.add_argument("--check", metavar="COMMIT", help="compare the working tree against COMMIT")
    ap.add_argument("--digest", action="store_true", help="print only sha256 of the census JSON")
    a = ap.parse_args()
    now = census(a.rev)
    if a.check:
        d = diff(census(a.check), now)
        print("\n".join(d) if d else f"IDENTICAL to {a.check}  {json.dumps(now['totals'])}")
        return 1 if d else 0
    text = dump(now)
    if a.digest:
        print(hashlib.sha256(text.encode()).hexdigest(), json.dumps(now["totals"]))
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
