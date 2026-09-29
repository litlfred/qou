#!/usr/bin/env python3
"""Triage the same-namespace duplicate class declarations by DIVERGENCE.

`duplicate-class-declaration-census.py` answers *where* one class name is
declared twice in one namespace. That count alone cannot be acted on, because
the copies are not the same kind of thing and the right disposition differs:

  IDENTICAL   same field names and types -- AGENTS.md §0a already decides it
              ("NEVER create or keep such a stub when the real formalisation
              exists in the library tree"); keep the library copy, delete the
              sibling, no authorial input needed.
  STUB        one copy has no fields, or only `True`-typed ones, while the
              other carries content. Also §0a: the stub SHADOWS the real
              declaration, since a sibling `<rootName>.lean` resolves before
              `<lakeRoot>/<Decl/Path>.lean`.
  DIVERGENT   the copies state genuinely different things. This is the only
              class that needs the author, because deciding which is canonical
              is deciding what the paper claims -- see `IsAMEValue` in
              docs/audits/2026-08-24-faithful-instance-family.md, where one
              copy gates on an AME-database hypothesis and the other quantifies
              over an arbitrary real.

Field types are compared after whitespace normalisation only. Two copies that
differ solely in a docstring, a comment, or line wrapping compare IDENTICAL;
any difference in a field's NAME or TYPE makes them DIVERGENT. That is
deliberately conservative in the direction of asking rather than assuming: a
false DIVERGENT costs a read, a false IDENTICAL could delete a real statement.

Usage:  duplicate-class-divergence-triage.py [--self-test] [--json OUT]
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from importlib import import_module  # noqa: E402

_census = import_module("duplicate-class-declaration-census".replace("-", "_")) if False else None

# The census script's name is not a valid module identifier, so load it by path.
import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "dupcensus", ROOT / "scripts" / "duplicate-class-declaration-census.py"
)
dupcensus = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dupcensus)

CONTENT = ROOT / "folio"

FIELD = re.compile(r"^(?P<indent>\s+)(?P<name>[A-Za-z_][A-Za-z0-9_']*)\s*:(?P<type>.*)$")
EXTENDS = re.compile(r"\bextends\b")


def class_fields(lines: list[str], start: int) -> dict[str, str]:
    """Field name -> normalised type, for the class whose header is at `start`
    (0-indexed). A field whose type begins on the following line is joined --
    the empty-capture trap that made an earlier audit read such fields as data.
    """
    # Advance to the line carrying `where`; a header may wrap.
    i = start
    while i < len(lines) and "where" not in lines[i] and i - start < 10:
        i += 1
    if i >= len(lines) or "where" not in lines[i]:
        return {}
    fields: dict[str, str] = {}
    pending: str | None = None
    for line in lines[i + 1 :]:
        if not line.strip():
            continue
        if not line.startswith((" ", "\t")):
            break
        m = FIELD.match(line)
        if m and ":=" not in line:
            pending = m.group("name")
            fields[pending] = " ".join(m.group("type").split())
        elif pending is not None:
            fields[pending] = (fields[pending] + " " + " ".join(line.split())).strip()
        else:
            break
    return fields


def is_stub(fields: dict[str, str]) -> bool:
    """No fields at all, or every field typed literally `True`."""
    if not fields:
        return True
    return all(t.strip() == "True" for t in fields.values())


def collect() -> dict:
    per: dict[tuple[str, str], list[dict]] = collections.defaultdict(list)
    for p in sorted(CONTENT.rglob("*.lean")):
        if ".lake" in str(p):
            continue
        lines = dupcensus.strip_comments(p.read_text(errors="replace")).split("\n")
        for name, ns, line in dupcensus.declarations(lines):
            per[(name, ns)].append(
                {
                    "file": str(p.relative_to(ROOT)),
                    "line": line,
                    "fields": class_fields(lines, line - 1),
                }
            )
    return {k: v for k, v in per.items() if len({d["file"] for d in v}) > 1}


def classify(copies: list[dict]) -> str:
    sigs = {tuple(sorted(c["fields"].items())) for c in copies}
    if len(sigs) == 1:
        return "IDENTICAL"
    stubs = [c for c in copies if is_stub(c["fields"])]
    if stubs and len(stubs) < len(copies):
        return "STUB"
    return "DIVERGENT"


FIXTURE_A = """\
namespace N
class C where
  a : Nat
  b :
    Nat -> Nat
end N
"""
FIXTURE_B = """\
namespace N
/-- a docstring that must not matter -/
class C where
  a : Nat
  b : Nat -> Nat
end N
"""
FIXTURE_STUB = """\
namespace N
class C where
  marker : True
end N
"""


def self_test() -> int:
    fails = []

    def fields_of(src: str) -> dict[str, str]:
        lines = dupcensus.strip_comments(src).split("\n")
        decls = dupcensus.declarations(lines)
        return class_fields(lines, decls[0][2] - 1)

    fa, fb, fs = fields_of(FIXTURE_A), fields_of(FIXTURE_B), fields_of(FIXTURE_STUB)

    # A field whose type starts on the NEXT line must join, not read as empty.
    if fa.get("b") != "Nat -> Nat":
        fails.append(f"wrapped field type must join: got {fa.get('b')!r}")
    # A docstring difference must not make two copies diverge.
    if classify([{"fields": fa}, {"fields": fb}]) != "IDENTICAL":
        fails.append(f"docstring-only difference must be IDENTICAL: {fa} vs {fb}")
    # A `True`-only carrier is a stub against a content-bearing copy.
    if not is_stub(fs):
        fails.append(f"`marker : True` must read as a stub: {fs}")
    if classify([{"fields": fa}, {"fields": fs}]) != "STUB":
        fails.append("content vs True-only must classify STUB")
    # A real field difference must NOT be swallowed.
    if classify([{"fields": fa}, {"fields": {"a": "Int"}}]) != "DIVERGENT":
        fails.append("a differing field type must classify DIVERGENT")

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

    groups = collect()
    out = []
    for (name, ns), copies in sorted(groups.items()):
        verdict = classify(copies)
        lib = [c for c in copies if "/lean/QOU/" in c["file"]]
        sib = [c for c in copies if "/lean/QOU/" not in c["file"]]
        out.append(
            {
                "class": name,
                "namespace": ns,
                "verdict": verdict,
                "library_copies": len(lib),
                "sibling_copies": len(sib),
                "files": [c["file"] for c in copies],
            }
        )

    tally = collections.Counter(r["verdict"] for r in out)
    print(f"same-namespace duplicate class groups: {len(out)}")
    for v in ("IDENTICAL", "STUB", "DIVERGENT"):
        print(f"  {v:<10} {tally[v]:>3}")
    print()
    print("mechanically resolvable per AGENTS.md §0a (IDENTICAL + STUB):",
          tally["IDENTICAL"] + tally["STUB"])
    print("needs an authorial call (DIVERGENT):", tally["DIVERGENT"])
    print()
    for v in ("DIVERGENT", "STUB", "IDENTICAL"):
        rows = [r for r in out if r["verdict"] == v]
        if not rows:
            continue
        print(f"--- {v} ({len(rows)})")
        for r in rows:
            print(f"  {r['class']}  [{r['namespace']}]  lib={r['library_copies']} sib={r['sibling_copies']}")
            for f in r["files"]:
                print(f"      {f.replace('folio/quantum-observable-universe/', '')}")

    if args.json:
        Path(args.json).write_text(json.dumps(out, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
