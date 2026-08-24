#!/usr/bin/env python3
"""Census the SKELETON-INSTANCE shape: a global `instance` that inhabits a
carrier class by filling its fields with constant content.

Why this shape and not the "axiom-shim" shape it was found alongside
--------------------------------------------------------------------
Five files in `b67ee924e84` received the sorry-drain treatment yet raise no
candidate in `lean-vacuity-axiom-audit.ts`. Reading all five, the shared shape
is an *axiom shim*: a `Foo` carrier holding the content, a companion
`FooAxiom : Prop` holding the same field, and an `instance … : Foo` that
forwards `ctx.field`. Wiring a detector on THAT shape would be wrong --
measured, four of the five have no instance of the axiom class anywhere, and
`QOU/Archimedean/HyperbolicVolumeIndependence.lean` documents the shim as the
REPAIR of a prior vacuous `{ residual := 0, rfl }` instance. A detector on the
shim flags the fix.

What separates the one real defect from the four benign ones is not the shim,
it is whether the instance is GUARDED:

    -- phi-q-tower-jsj-bridge.lean -- UNCONDITIONAL, discharges globally
    instance skeletonRealisation (q : ℝ) : TowerSummandRealization q where
      realisation := fun _ _ => 0

    -- prop-rigid-monoidal-structural-gap-invariance.lean -- guarded, inert
    instance canonical (α : Type*) [ctx : RigidMonoidalStructuralGapInvarianceAxiom α] :
        RigidMonoidalStructuralGapInvariance α where
      categorical_trace _ := (0 : ℝ)
      convention_factorisation := ctx.convention_factorisation

Both fill a field with `0`. Only the first silently satisfies every
`[TowerSummandRealization q]` binder in the file -- including the two theorems
`bridge` and `bridge_nonneg`, which then quantify over a class inhabited only
by the zero realisation. This is the `triv_hecke` shape demoted in PR #5581.

Reported only when the class is CONSUMED as an instance-binder `[C …]`
somewhere, since an inert carrier nothing depends on discharges nothing. That
clause is also what keeps `he4_strong_duality_value` out: its global instance
fills `strong_duality := by norm_num` over concrete rationals -- a checked LP
certificate, not a constant -- so inhabitation alone never decides it.

Two corrections to my own first run, both of which produced unusable numbers
-----------------------------------------------------------------------------
The first version reported **273 actionable** rows. Both causes are worth
recording, because each one alone is enough to make the census meaningless:

1. **Scope.** `CONTENT.rglob("*.lean")` reaches
   `content/…/lean/.lake/packages/mathlib`, so it scanned 11125 files where the
   vacuity audit scans 3112. Every high-consumer row was Mathlib.
2. **`rfl` on a PROOF field is a real proof.** The criterion flagged
   `one_smul := rfl`, `mul_assoc := rfl`, `bot_le := …` — but those fields are
   *obligations*, and the instance's data fields make them hold definitionally.
   What is content-free is a constant in a **data** field. Restricting to data
   fields is what took 273 to 14.

A third bug was caught by the self-test rather than by reading output: a field
whose type begins on the NEXT line (`realisation_nonneg :` / newline / `∀ β S,
0 ≤ …`) captures an EMPTY type, and an empty string contains no Prop marker, so
it read as data. Same trap as in `free-prop-field-audit.py`; the self-test now
pins both halves of that one instance so it cannot come back silently.

Result: 3112 files -> 37 instances with a constant data field -> 23 unguarded
-> **14 whose class is consumed as a hypothesis**. Three hand-read, three
confirmed harmful (`TowerSummandRealization`, `MassEndomorphism`,
`QIntegerMassFormula`); the other 11 are unread candidates, not findings.

Usage:  trivially-inhabiting-instance-census.py [--self-test] [--json OUT]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

# `instance foo (a : T) [Inst] : ClassName args where` / `:= …`, possibly
# wrapped across lines. Captured lazily to the LAST top-level `:` before the
# body, which is where the inhabited class sits.
INSTANCE_HEAD = re.compile(
    r"^(?P<indent>[ \t]*)(?:noncomputable\s+|scoped\s+|local\s+|private\s+|protected\s+)*"
    r"instance\b(?P<rest>.*)$"
)

# Content that asserts nothing about the subject. `rfl`/`trivial`/`le_refl`
# close a goal the constant field just made trivially true; `0`/`True`/
# `PUnit.unit` are the constants themselves.
TRIVIAL_VALUE = re.compile(
    r"^(?:"
    r"\(?\s*(?:-\s*)?0\s*(?::[^)]*)?\)?"          # 0, (0 : ℝ), (0:ℤ)
    r"|True|trivial|PUnit\.unit|⟨⟩|\(\)"
    r"|rfl|Eq\.refl\b.*|le_refl\b.*|Nat\.le_refl\b.*"
    r"|fun\s+[^=]*=>\s*(?:\(?\s*(?:-\s*)?0\s*(?::[^)]*)?\)?|True|trivial|PUnit\.unit|rfl|le_refl\b.*)"
    r"|by\s+(?:trivial|rfl|simp|exact\s+(?:rfl|trivial|le_refl\b.*))\s*"
    r")$"
)

FIELD_ASSIGN = re.compile(r"^\s+(?P<name>[A-Za-z_][A-Za-z0-9_']*)\s*(?P<args>[^:=]*):=\s*(?P<val>.*?)\s*$")

# A class field declaration inside a `class`/`structure … where` block.
FIELD_DECL = re.compile(r"^\s+(?P<name>[A-Za-z_][A-Za-z0-9_']*)\s*:(?P<type>.*?)\s*$")
CARRIER_HEAD = re.compile(
    r"^(?:[ \t]*)(?:noncomputable\s+|scoped\s+|private\s+|protected\s+)*"
    r"(?:class|structure)\s+(?P<name>[A-Za-z_][A-Za-z0-9_'.]*)"
)

# Logical/relational vocabulary. A field type containing any of it is a PROOF
# obligation, not data.
#
# This distinction is the whole criterion, and getting it wrong is what made
# the first run of this census useless: `rfl` closing `one_smul` for a concrete
# action is a REAL proof -- the data fields make the equation hold
# definitionally -- while `realisation := fun _ _ => 0` closing a data field is
# content-free. Treating both as "trivial" returned 273 candidates, essentially
# all of them ordinary Mathlib instances.
#
# `Prop` is deliberately NOT in this list: a field declared `foo : Prop` is a
# FREE proposition -- data, not an obligation -- and filling it with `True` is
# the `triv_hecke` shape (`hecke_relation := True`) that PR #5581 demoted.
PROP_MARKERS = ("=", "≠", "<", "≤", ">", "≥", "∈", "∉", "∣", "↔", "∧", "∨", "¬", "∀", "∃")


def field_types(lines: list[str]) -> dict[str, dict[str, str]]:
    """Map every `class`/`structure` in a file to {field name: declared type}."""
    out: dict[str, dict[str, str]] = {}
    for n, line in enumerate(lines):
        m = CARRIER_HEAD.match(line)
        if not m or "where" not in line and not any(
            "where" in lines[k] for k in range(n, min(n + 8, len(lines)))
        ):
            continue
        start = next(
            (k for k in range(n, min(n + 8, len(lines))) if "where" in lines[k]), None
        )
        if start is None:
            continue
        fields: dict[str, str] = {}
        pending: str | None = None
        for body in lines[start + 1 :]:
            if body.strip() == "":
                continue
            if not body.startswith((" ", "\t")):
                break
            fm = FIELD_DECL.match(body)
            if fm and ":=" not in body:
                pending = fm.group("name")
                fields[pending] = fm.group("type")
            elif pending is not None:
                # A field whose type starts on the NEXT line is written `name :`
                # with nothing after the colon, so the captured type is EMPTY --
                # and an empty string contains no Prop marker, which reads as
                # DATA. That is how `realisation_nonneg : ∀ β S, 0 ≤ …` was
                # first reported as a trivial data field. Keep accumulating
                # continuation lines until the next declaration.
                fields[pending] += " " + body.strip()
        out[m.group("name").split(".")[-1]] = fields
    return out


def is_data_field(cls: str, field: str, index: dict[str, dict[str, str]]) -> bool:
    """True when the field carries DATA rather than a proof obligation.

    Unknown fields (an inherited or Mathlib-declared class we never saw
    declared) return False: the census reports only what it can justify.
    """
    ty = index.get(cls, {}).get(field)
    if ty is None:
        return False
    return not any(mark in ty for mark in PROP_MARKERS)


def strip_comments(text: str) -> str:
    """Blank out `--` line comments and `/- … -/` blocks, preserving line count."""
    out = []
    depth = 0
    for line in text.split("\n"):
        buf = []
        i = 0
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


def split_binders(rest: str) -> tuple[str, str]:
    """Split an instance header's `rest` into (binders, inhabited-class type).

    The split point is the top-level `:` -- top-level meaning outside every
    bracket, so `(q : ℝ)` and `[ctx : FooAxiom q]` do not fool it.
    """
    depth = 0
    for i, ch in enumerate(rest):
        if ch in "([{⦃":
            depth += 1
        elif ch in ")]}⦄":
            depth -= 1
        elif ch == ":" and depth == 0:
            if rest[i : i + 2] == ":=":
                break
            return rest[:i], rest[i + 1 :]
    return rest, ""


def bracket_binders(binders: str) -> list[str]:
    """Every `[…]` instance-binder in a header, as raw strings."""
    out, depth, start = [], 0, None
    for i, ch in enumerate(binders):
        if ch == "[":
            if depth == 0:
                start = i + 1
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0 and start is not None:
                out.append(binders[start:i])
                start = None
    return out


def head_class(type_expr: str) -> str:
    m = re.search(r"([A-Za-z_][A-Za-z0-9_'.]*)", type_expr)
    return m.group(1).split(".")[-1] if m else ""


def scan_file(path: Path, lines: list[str], index: dict[str, dict[str, str]]) -> list[dict]:
    hits = []
    for n, line in enumerate(lines):
        m = INSTANCE_HEAD.match(line)
        if not m:
            continue
        # Accumulate the header until `where` or `:=` appears at top level.
        rest = m.group("rest")
        end = n
        while "where" not in rest and ":=" not in rest and end + 1 < len(lines) and end - n < 12:
            end += 1
            rest += " " + lines[end].strip()
        if "where" not in rest:
            continue  # `:= …` instances carry no field block to inspect
        header = rest[: rest.index("where")]
        binders, type_expr = split_binders(header)
        cls = head_class(type_expr)
        if not cls:
            continue

        # Guarded? Any instance-binder whose class is NOT the inhabited one.
        guards = [b for b in bracket_binders(binders) if head_class(b.split(":")[-1]) != cls]

        trivial_fields, real_fields = [], []
        for body_line in lines[end + 1 :]:
            if body_line.strip() == "":
                continue
            if not body_line.startswith((" ", "\t")):
                break
            fm = FIELD_ASSIGN.match(body_line)
            if not fm:
                break
            name = fm.group("name")
            trivial = TRIVIAL_VALUE.match(fm.group("val")) and is_data_field(cls, name, index)
            (trivial_fields if trivial else real_fields).append(name)
        if not trivial_fields:
            continue
        hits.append(
            {
                "file": str(path.relative_to(ROOT)),
                "line": n + 1,
                "instance_class": cls,
                "guarded_by": [head_class(g.split(":")[-1]) for g in guards],
                "trivial_fields": trivial_fields,
                "real_fields": real_fields,
            }
        )
    return hits


def consumers(cls: str, stripped: dict[Path, list[str]]) -> int:
    """Count declarations elsewhere binding `[… : cls …]` or `[cls …]`."""
    pat = re.compile(r"\[\s*(?:[A-Za-z_][A-Za-z0-9_']*\s*:\s*)?" + re.escape(cls) + r"\b")
    return sum(
        1
        for lines in stripped.values()
        for ln in lines
        if pat.search(ln) and not ln.lstrip().startswith("instance")
    )


def self_test(rows: list[dict]) -> int:
    """Four hand-read cases. A narrowing that loses any of them is not a
    narrowing, it is the name-gate failure this whole audit exists to avoid."""
    by = {(r["file"].split("/")[-1], r["instance_class"]): r for r in rows}
    fails = []

    r = by.get(("phi-q-tower-jsj-bridge.lean", "TowerSummandRealization"))
    if not r:
        fails.append("MISS: skeletonRealisation (unconditional, fills `fun _ _ => 0`)")
    else:
        if r["guarded_by"]:
            fails.append(f"skeletonRealisation must be UNGUARDED, got {r['guarded_by']}")
        # The data/proof split, pinned on the one instance that exercises both.
        if "realisation" not in r["trivial_fields"]:
            fails.append("`realisation : … → ℝ` filled `fun _ _ => 0` must read as trivial DATA")
        if "realisation_nonneg" in r["trivial_fields"]:
            fails.append(
                "`realisation_nonneg : ∀ β S, 0 ≤ …` must read as a PROOF, not data "
                "-- its type starts on the next line, so an empty capture reads as data"
            )

    r = by.get(("prop-rigid-monoidal-structural-gap-invariance.lean", "RigidMonoidalStructuralGapInvariance"))
    if not r:
        fails.append("MISS: `canonical` -- it fills `categorical_trace _ := (0 : ℝ)`")
    elif "RigidMonoidalStructuralGapInvarianceAxiom" not in r["guarded_by"]:
        fails.append(f"`canonical` must read as GUARDED, got {r['guarded_by']}")

    # triv_hecke was demoted to `def` in PR #5581; it must not reappear.
    if any(r["instance_class"] == "IwahoriHeckeAlgebra" for r in rows):
        fails.append("REGRESSION: triv_hecke is an `instance` again (PR #5581 demoted it)")

    # he4's global instance discharges `strong_duality := by norm_num`, a
    # checked certificate over concrete rationals -- never a trivial field.
    for r in rows:
        if "he4" in r["file"] and "strong_duality" in r["trivial_fields"]:
            fails.append(f"FALSE POSITIVE: he4 strong_duality read as trivial ({r['file']})")

    for f in fails:
        print("  self-test FAIL:", f)
    return len(fails)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--json")
    args = ap.parse_args()

    # Strip once: `strip_comments` walks character-by-character, so re-running
    # it per (row x file) inside the consumer count made the census unusable.
    # `.lake` holds Mathlib and the other vendored packages. The vacuity audit
    # excludes them and so must this: the first run scanned 11125 files instead
    # of 3112 and every high-consumer row was a Mathlib instance.
    stripped = {
        p: strip_comments(p.read_text(encoding="utf-8", errors="replace")).split("\n")
        for p in CONTENT.rglob("*.lean")
        if ".lake" not in p.parts
    }
    index: dict[str, dict[str, str]] = {}
    for lines in stripped.values():
        index.update(field_types(lines))
    rows = []
    for p, lines in stripped.items():
        rows.extend(scan_file(p, lines, index))

    if args.self_test:
        n = self_test(rows)
        print(f"self-test: {'PASS' if n == 0 else f'{n} FAILURE(S)'} ({len(rows)} rows scanned)")
        if n:
            return 1

    seen: dict[str, int] = {}
    for r in rows:
        cls = r["instance_class"]
        if cls not in seen:
            seen[cls] = consumers(cls, stripped)
        r["consumers"] = seen[cls]

    unguarded = [r for r in rows if not r["guarded_by"]]
    harmful = [r for r in unguarded if r["consumers"] > 0]

    print(f"scanned {len(stripped)} .lean under content/")
    print(f"  instances filling >=1 field with constant content : {len(rows)}")
    print(f"  of those, UNGUARDED (no conditional-class binder)  : {len(unguarded)}")
    print(f"  of those, class is consumed as a hypothesis        : {len(harmful)}  <-- actionable")
    print()
    for r in sorted(harmful, key=lambda r: (-r["consumers"], r["file"])):
        print(f"{r['file']}:{r['line']}  {r['instance_class']}")
        print(
            f"    trivial={r['trivial_fields']} real={r['real_fields']} "
            f"consumers={r['consumers']}"
        )

    if args.json:
        Path(args.json).write_text(json.dumps({"rows": rows}, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
