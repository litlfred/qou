#!/usr/bin/env python3
"""Which data fields of a Lean `structure` are mentioned by any of its laws?

A field whose name occurs in NO law field's TYPE is *free data*: it can be
replaced by anything without disturbing a single axiom, so no property of it
is derivable from the structure's definition -- and none is refutable either.
Such a field makes every question about it INDEPENDENT of the definition,
which is a different answer from "unproved".

Method (mechanical, not by eye):

  1. Extract the structure body from the source.
  2. Strip docstrings (`/-- ... -/`) and line comments FIRST, so a field named
     only in prose does not count as constrained.  This is the whole point:
     `FrobeniusHopfData.antipode` is described at length in a docstring and
     constrained by nothing.
  3. Split the body into fields.  A field is a LAW if its type elaborates to a
     proposition -- detected syntactically as a type containing `=` at the top
     level of its text, which is what every law in this corpus looks like.
     Anything else is DATA.
  4. For each DATA field, count occurrences of its name as a whole identifier
     in the concatenated types of the LAW fields.

Usage:
    python3 scripts/lean-structure-field-law-audit.py <file.lean> <StructName>

Exit code is 0 always -- this reports, it does not gate.
"""
from __future__ import annotations

import re
import sys


def strip_comments(text: str) -> str:
    """Remove `/-- ... -/` docstrings, `/- ... -/` blocks and `-- ...` lines."""
    out, i, n = [], 0, len(text)
    while i < n:
        if text.startswith("/-", i):
            depth, j = 1, i + 2
            while j < n and depth:
                if text.startswith("/-", j):
                    depth += 1
                    j += 2
                elif text.startswith("-/", j):
                    depth -= 1
                    j += 2
                else:
                    j += 1
            i = j
        elif text.startswith("--", i):
            j = text.find("\n", i)
            i = n if j < 0 else j
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


def structure_body(src: str, name: str) -> str:
    m = re.search(rf"^structure\s+{re.escape(name)}\b", src, re.M)
    if not m:
        sys.exit(f"structure {name} not found")
    start = src.index("where", m.start()) + len("where")
    # The body ends at the first subsequent line that starts in column 0 with
    # something other than whitespace -- structures here are indented two.
    rest = src[start:]
    end = len(rest)
    for mm in re.finditer(r"^\S", rest, re.M):
        end = mm.start()
        break
    return rest[:end]


def fields(body: str) -> list[tuple[str, str]]:
    """Return [(field_name, type_text)] in declaration order."""
    lines = body.split("\n")
    out: list[tuple[str, list[str]]] = []
    for line in lines:
        m = re.match(r"^  (\w+)\s*:(.*)$", line)
        if m:
            out.append((m.group(1), [m.group(2)]))
        elif out and line.strip():
            out[-1][1].append(line)
    return [(nm, " ".join(t)) for nm, t in out]


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    path, name = sys.argv[1], sys.argv[2]
    src = open(path, encoding="utf-8").read()
    body = strip_comments(structure_body(src, name))
    fs = fields(body)
    laws = [(nm, ty) for nm, ty in fs if "=" in ty]
    data = [(nm, ty) for nm, ty in fs if "=" not in ty]
    lawtext = " ".join(ty for _, ty in laws)

    print(f"{name}  ({path})")
    print(f"  DATA fields : {[nm for nm, _ in data]}")
    print(f"  LAW  fields : {[nm for nm, _ in laws]}")
    print()
    free = []
    for nm, _ in data:
        k = len(re.findall(rf"(?<![A-Za-z0-9_.]){re.escape(nm)}(?![A-Za-z0-9_])",
                           lawtext))
        tag = "CONSTRAINED" if k else "*** FREE DATA ***"
        if not k:
            free.append(nm)
        print(f"    {nm:<16} {tag:<20} mentions-in-laws={k}")
    print()
    if free:
        print(f"  FREE DATA: {free}")
        print("  No property of these fields is derivable from the structure's")
        print("  axioms, and none is refutable: every question about them is")
        print("  INDEPENDENT of the definition as it stands.")
    else:
        print("  Every data field is mentioned by at least one law.")


if __name__ == "__main__":
    main()
