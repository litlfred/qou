#!/usr/bin/env python3
"""Find content-block siblings that DECLARE a name the library also declares.

Why this exists
---------------
`conj:b1-hyperbolic-rows-theorem` had an inconsistent axiom repaired on
2026-08-08 in `lean/QOU/AppendixSurreals/B1HyperbolicRowsTheorem.lean`.  The
**sibling** kept the pre-repair version, and a `False` was still derivable from
it on 2026-09-03 -- reproduced, not inferred.  Nothing in the corpus checks that
a library file and its sibling agree, and the sibling is the copy `lean.ref`
resolves to FIRST (AGENTS.md 0a candidate 1), so it is the one a reader reaches.

What this can and cannot see
----------------------------
It compares DECLARATION TEXT after normalising whitespace and stripping
comments.  It therefore:

  * CAN see a sibling and a library file declaring the same fully-qualified
    name with different statements -- the class that produced the incident;
  * CAN see a sibling declaring an `axiom` where the library has a `theorem`,
    `class` or `structure`, which is strictly worse whether or not the text
    differs;
  * CANNOT see semantic divergence between statements that happen to be
    textually equal after normalisation, nor divergence carried by a shared
    helper rather than by the named declaration itself.

It also builds a declaration's fully-qualified name by concatenating EVERY
`namespace` line in the file, which is wrong for a file that opens and closes
several sibling namespaces in sequence.  Measured 2026-09-03: **55 of 908
sibling files (6.1%) and 216 of 2537 library files (8.5%)** have more than one
distinct namespace, so those files get wrong names.  A wrong concatenated
namespace is very unlikely to collide with a real one, so the error direction is
MISSED pairs rather than invented ones -- read the counts as a **lower bound**.

So a clean run is evidence about NAMES, not about meanings.  Do not quote it as
"the siblings agree with the library".

Verdicts
--------
  divergent-axiom  sibling declares `axiom`, library declares something else
                   -- read first, this is the incident's shape
  divergent        same fully-qualified name, different normalised statement
  duplicate        same name, same statement -- redundant, 0a says drop it
"""
from __future__ import annotations
import re, sys, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPER = ROOT / "content" / "quantum-observable-universe"
LIB = PAPER / "lean"

KINDS = ("axiom", "theorem", "lemma", "def", "abbrev", "class", "structure",
         "instance", "opaque", "inductive")
DECL_RE = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?"
    r"(?:noncomputable\s+|private\s+|protected\s+|scoped\s+|partial\s+)*"
    r"(" + "|".join(KINDS) + r")\s+([A-Za-z_][A-Za-z0-9_'!?.]*)",
    re.M,
)
NS_RE = re.compile(r"^\s*namespace\s+([A-Za-z_][A-Za-z0-9_'.]*)", re.M)


def strip_comments(text: str) -> str:
    text = re.sub(r"/-.*?-/", " ", text, flags=re.S)   # block + doc comments
    text = re.sub(r"--[^\n]*", " ", text)              # line comments
    return text


def declarations(path: Path) -> dict[str, tuple[str, str]]:
    """fully-qualified name -> (kind, normalised statement text)."""
    raw = path.read_text(encoding="utf8", errors="replace")
    body = strip_comments(raw)
    ns = ".".join(NS_RE.findall(body))          # nested namespaces concatenate
    out: dict[str, tuple[str, str]] = {}
    hits = list(DECL_RE.finditer(body))
    for i, m in enumerate(hits):
        start = m.start()
        end = hits[i + 1].start() if i + 1 < len(hits) else len(body)
        stmt = " ".join(body[start:end].split())
        name = m.group(2)
        fq = f"{ns}.{name}" if ns and not name.startswith(ns) else name
        out[fq] = (m.group(1), stmt)
    return out


def main() -> int:
    lib_files = sorted(LIB.rglob("*.lean"))
    lib_files = [p for p in lib_files if ".lake" not in p.parts]
    lib: dict[str, tuple[str, str, Path]] = {}
    for p in lib_files:
        for fq, (kind, stmt) in declarations(p).items():
            lib.setdefault(fq, (kind, stmt, p))

    sib_files = [p for p in sorted(PAPER.rglob("*.lean"))
                 if LIB not in p.parents and p != LIB]

    findings = []
    for p in sib_files:
        for fq, (kind, stmt) in declarations(p).items():
            if fq not in lib:
                continue
            lkind, lstmt, lpath = lib[fq]
            if kind == "axiom" and lkind != "axiom":
                verdict = "divergent-axiom"
            elif stmt != lstmt:
                verdict = "divergent"
            else:
                verdict = "duplicate"
            findings.append({
                "name": fq,
                "verdict": verdict,
                "sibling": str(p.relative_to(ROOT)),
                "sibling_kind": kind,
                "library": str(lpath.relative_to(ROOT)),
                "library_kind": lkind,
            })

    order = {"divergent-axiom": 0, "divergent": 1, "duplicate": 2}
    findings.sort(key=lambda f: (order[f["verdict"]], f["name"]))

    print(f"sibling .lean files scanned : {len(sib_files)}")
    print(f"library .lean files scanned : {len(lib_files)}")
    print(f"library declarations indexed: {len(lib)}")
    print()
    for v in ("divergent-axiom", "divergent", "duplicate"):
        n = sum(1 for f in findings if f["verdict"] == v)
        print(f"  {n:4d}  {v}")
    print()
    for f in findings:
        if f["verdict"] == "duplicate":
            continue
        print(f"[{f['verdict']}] {f['name']}")
        print(f"    sibling {f['sibling_kind']:9s} {f['sibling']}")
        print(f"    library {f['library_kind']:9s} {f['library']}")

    if len(sys.argv) > 2 and sys.argv[1] == "--json":
        Path(sys.argv[2]).write_text(json.dumps(findings, indent=2), encoding="utf8")
        print(f"\nwrote {sys.argv[2]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
