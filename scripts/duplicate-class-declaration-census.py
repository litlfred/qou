#!/usr/bin/env python3
"""Census DUPLICATE class declarations: one class name declared in several files.

Found while draining the "Faithful instance" family (bean `qou-hjf4`). Chasing
one vacuous global instance in `observations/borromean-quark.lean` turned up
that `class BorromeanQuark` is declared **eleven** times across the corpus, and
that the two carrying a vacuous `instance canonical` sit in the same namespace
as a third. The instances are the symptom; the duplication is the structure.

Why it matters, in the corpus's own words --
`QOU/Archimedean/HyperbolicVolumeIndependence.lean` records the failure mode as
a past incident:

    This file previously declared a *duplicate* `HyperbolicVolumeIndependence`
    class with a placeholder shape ... and a **vacuous** global instance
    `{ residual := 0, rfl }`. That was unsound as a conjecture encoding: the
    trivial instance silently discharged every `[HyperbolicVolumeIndependence]`
    hypothesis with no mathematical content, and the duplicate declaration
    collided with the real class when both files were imported.

AGENTS.md §0a bans the shape directly ("NEVER create or keep such a stub when
the real formalisation exists in the library tree"), because a content-block
sibling `<rootName>.lean` resolves BEFORE `<lakeRoot>/<Decl/Path>.lean`.

NAMESPACE ATTRIBUTION IS PER-DECLARATION, NOT PER-FILE
------------------------------------------------------
The first version of this measurement asked only "does this file contain a
`namespace QOU.BraidKnot` line anywhere", which credits a class to every
namespace block in its file and inflates the same-namespace count. Lean
namespaces nest and reopen, so a file may legitimately hold declarations in
`QOU.BraidKnot`, `QOU.BraidKnot.Inner`, and `QOU.Archimedean` at once. This
version tracks the open `namespace`/`end` stack line by line and attributes
each class to the stack in effect AT ITS OWN LINE, which is what determines
whether two declarations can actually collide on import.

A same-name pair in DIFFERENT namespaces is not a collision -- it is two
distinct classes, which may be intentional (or may be an unnoticed fork; this
census does not judge that). Only the same-namespace rows can clash.

Usage:  duplicate-class-declaration-census.py [--self-test] [--json OUT]
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

# ALL declaration kinds that put a name in the environment, not just `class`.
#
# This scanned `class` alone until 2026-08-24, and the omission was found the
# hard way: `R5FullWitness` looked like a mechanical library-vs-sibling dedup
# until the import turned out to be impossible, because the sibling forks
# `inductive LightNucleus` — invisible to a class-only scan. Lean's environment
# is flat, so a duplicated `def` collides on import exactly as a duplicated
# `class` does. Measured, the kinds this used to skip carry 213 same-namespace
# duplicates against `class`/`structure`'s 38.
#
# `theorem`/`lemma` are deliberately EXCLUDED: they are proofs of propositions,
# duplicating one is redundancy rather than a fork of a definition, and
# including them would bury the definitional collisions this exists to surface.
DECL_KINDS = ("class", "structure", "inductive", "abbrev", "def")
CLASS = re.compile(
    r"^\s*(?:noncomputable\s+|private\s+|protected\s+|scoped\s+|local\s+|partial\s+|unsafe\s+)*"
    r"(?:" + "|".join(DECL_KINDS) + r")\s+([A-Za-z_][A-Za-z0-9_'.]*)"
)
NS_OPEN = re.compile(r"^\s*namespace\s+([A-Za-z_][A-Za-z0-9_'.]*)")
NS_END = re.compile(r"^\s*end\b\s*([A-Za-z_][A-Za-z0-9_'.]*)?\s*$")
SECTION = re.compile(r"^\s*section\b")


def strip_comments(text: str) -> str:
    """Blank out `--` line comments and `/- … -/` blocks, preserving line count."""
    out, depth = [], 0
    for line in text.split("\n"):
        buf, i = [], 0
        while i < len(line):
            two = line[i : i + 2]
            if depth == 0 and two == "--":
                break
            if two == "/-":
                depth += 1
                buf.append("  ")
                i += 2
                continue
            if two == "-/" and depth:
                depth -= 1
                buf.append("  ")
                i += 2
                continue
            buf.append(" " if depth else line[i])
            i += 1
        out.append("".join(buf))
    return "\n".join(out)


def declarations(lines: list[str]) -> list[tuple[str, str, int]]:
    """(class name, fully-qualified namespace at its line, 1-indexed line)."""
    out: list[tuple[str, str, int]] = []
    stack: list[str] = []
    # `section` also consumes an `end`, so it must be tracked or every `end`
    # after one incorrectly pops a namespace.
    kinds: list[str] = []
    for n, line in enumerate(lines):
        if m := NS_OPEN.match(line):
            stack.append(m.group(1))
            kinds.append("ns")
            continue
        if SECTION.match(line):
            kinds.append("sec")
            continue
        if NS_END.match(line):
            if kinds:
                if kinds.pop() == "ns" and stack:
                    stack.pop()
            continue
        if m := CLASS.match(line):
            out.append((m.group(1), ".".join(stack) or "<root>", n + 1))
    return out


FIXTURE = """\
namespace Outer

class InOuter where
  f : Nat

inductive AnInductive : Type
  | a
noncomputable def ADef : Nat := 0
abbrev AnAbbrev := Nat
theorem NotADecl : True := trivial

section
class AlsoInOuter where
  g : Nat
end

namespace Inner
class InInner where
  h : Nat
end Inner

class StillOuter where
  k : Nat

end Outer

class AtRoot where
  m : Nat
"""


def self_test() -> int:
    """Pins the two things a per-file attribution gets wrong: a nested namespace,
    and a `section`'s `end` stealing a namespace pop."""
    got = {name: ns for name, ns, _ in declarations(FIXTURE.split("\n"))}
    want = {
        # kinds beyond `class` must be scanned -- the LightNucleus blocker
        "AnInductive": "Outer",
        "ADef": "Outer",
        "AnAbbrev": "Outer",
        "InOuter": "Outer",
        "AlsoInOuter": "Outer",   # `section`/`end` must not pop `Outer`
        "InInner": "Outer.Inner",  # nested, not "Outer"
        "StillOuter": "Outer",     # `end Inner` pops only Inner
        "AtRoot": "<root>",
    }
    fails = [f"{k}: got {got.get(k)!r}, want {v!r}" for k, v in want.items() if got.get(k) != v]
    # theorems are deliberately out of scope; including them would bury the
    # definitional collisions this census exists to surface.
    if "NotADecl" in got:
        fails.append("theorem must NOT be scanned -- it is a proof, not a definition")
    for f in fails:
        print("  self-test FAIL:", f)
    print(f"self-test: {'PASS' if not fails else f'{len(fails)} FAILURE(S)'}")
    return len(fails)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--json")
    args = ap.parse_args()

    if args.self_test and self_test():
        return 1

    by_name: dict[str, list[dict]] = collections.defaultdict(list)
    n_files = 0
    for p in sorted(CONTENT.rglob("*.lean")):
        if ".lake" in str(p):
            continue
        n_files += 1
        for name, ns, line in declarations(strip_comments(p.read_text(errors="replace")).split("\n")):
            by_name[name].append(
                {"file": str(p.relative_to(ROOT)), "namespace": ns, "line": line}
            )

    multi = {k: v for k, v in by_name.items() if len({d["file"] for d in v}) > 1}
    collide: dict[str, dict[str, list[str]]] = {}
    for k, v in multi.items():
        per_ns = collections.defaultdict(set)
        for d in v:
            per_ns[d["namespace"]].add(d["file"])
        hot = {ns: sorted(fs) for ns, fs in per_ns.items() if len(fs) > 1}
        if hot:
            collide[k] = hot

    print(f"scanned {n_files} .lean under content/ (comment-stripped)")
    print(f"  distinct declaration names               : {len(by_name)}")
    print(f"  declared in >1 FILE                      : {len(multi)}")
    print(f"  ...with >1 file in the SAME namespace    : {len(collide)}   <- can collide on import")
    print()
    print("same-namespace collisions, most declarations first:")
    for k in sorted(collide, key=lambda k: -len(multi[k])):
        print(f"  {k}  ({len({d['file'] for d in multi[k]})} files)")
        for ns, fs in sorted(collide[k].items()):
            print(f"      {ns}")
            for f in fs:
                print(f"        {f.replace('folio/quantum-observable-universe/', '')}")

    if args.json:
        Path(args.json).write_text(
            json.dumps({"multi": multi, "collide": collide}, indent=2) + "\n"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
