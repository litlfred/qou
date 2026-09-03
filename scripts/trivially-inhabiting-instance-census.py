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
    # Strip the ASCII function arrow FIRST. `->` is legal Lean and contains `>`,
    # which is a Prop marker -- so `realisation : Nat → Nat → R`, a plain data
    # field, reads as a proof obligation and its constant value is never
    # flagged. Unicode `→` never tripped this because it is not a marker, so the
    # bug was invisible in the corpus's dominant spelling; 4 field declarations
    # under content/ use the ASCII form. It fails in the SAFE direction (missed
    # candidates, not false ones), which is exactly why it would not have
    # surfaced on its own.
    ty = ty.replace("->", " ")
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


def scan_file(path: Path, lines: list[str], index: dict[str, dict[str, str]],
              corpus_classes: set[str]) -> list[dict]:
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

        # Guarded? Only by a CONTENT CARRIER -- a class this corpus declares.
        #
        # An earlier version counted EVERY `[…]` binder as a guard, which is
        # wrong and under-counts badly: `instance canonical {R} [CommRing R] {β} :
        # MassEndomorphism R β` reads as "guarded by CommRing" and disappears,
        # even though `CommRing` is ordinary structural machinery that constrains
        # nothing about the conjecture. Measured, that hid the WORSE of the two
        # `MassEndomorphism` instances -- the fully generic all-zeros one -- while
        # keeping `trivial_int_zero`, which was visible only because it is pinned
        # at concrete `ℤ` and so carries no `[CommRing]` binder at all.
        #
        # A guard is what makes `prop-rigid-monoidal`'s `canonical` inert:
        # `[ctx : RigidMonoidalStructuralGapInvarianceAxiom α]`, a carrier with no
        # instance of its own. Mathlib structure is not that.
        guards = [
            g
            for b in bracket_binders(binders)
            if (g := head_class(b.split(":")[-1])) != cls and g in corpus_classes
        ]

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


FIXTURE = """\
class Carrier (q : R) where
  realisation : Nat → Nat → R
  realisation_nonneg :
    ∀ b s, 0 ≤ realisation b s

class CarrierAxiom (q : R) : Prop where
  bridge : ∀ b, realisation b = 0

class Generic (R : Type*) [CommRing R] (b : Type*) where
  q : R
  coeff : Nat -> R
  vol_eq : q = q

instance unguarded (q : R) : Carrier q where
  realisation := fun _ _ => 0
  realisation_nonneg := fun _ _ => le_refl 0

instance guarded (q : R) [ctx : CarrierAxiom q] : Carrier q where
  realisation := fun _ _ => 0
  realisation_nonneg := ctx.bridge

instance structural {R : Type*} [CommRing R] {b : Type*} : Generic R b where
  q := 0
  coeff := fun _ => 0
  vol_eq := by ring
"""


def self_test(rows: list[dict]) -> int:
    """Two halves, deliberately separated.

    The FIXTURE half pins the criterion itself. It used to be pinned against
    live declarations, and that was a design error I only saw when it fired:
    `skeletonRealisation` was the positive case, PR #5621 demoted it to a `def`
    -- the correct fix -- and the self-test failed because the corpus had been
    REPAIRED. A regression test that depends on the corpus staying broken
    deletes itself on success.

    The CORPUS half keeps only what must remain absent (or present) in the real
    tree, which is what a corpus assertion is actually for.
    """
    fails = []

    fx = scan_file(ROOT / "fixture.lean", FIXTURE.split("\n"),
                   field_types(FIXTURE.split("\n")), {"Carrier", "CarrierAxiom", "Generic"})
    fxby = {r["instance_class"] + ":" + str(r["line"]): r for r in fx}
    byname = {}
    for r in fx:
        byname.setdefault(r["instance_class"], []).append(r)

    ung = [r for r in fx if not r["guarded_by"]]
    grd = [r for r in fx if r["guarded_by"]]

    if not any("realisation" in r["trivial_fields"] for r in ung):
        fails.append("fixture: `realisation := fun _ _ => 0` must read as trivial DATA")
    if any("realisation_nonneg" in r["trivial_fields"] for r in fx):
        fails.append(
            "fixture: `realisation_nonneg` must read as a PROOF, not data -- its type "
            "starts on the NEXT line, so an empty capture wrongly reads as data"
        )
    if not grd:
        fails.append("fixture: `[ctx : CarrierAxiom q]` must count as a content-carrier GUARD")
    # The bug this fix exists for: `[CommRing R]` is structural, not a guard.
    # ASCII `->` in a data field's type must not make it read as a proof.
    if gen := byname.get("Generic", []):
        if "coeff" not in gen[0]["trivial_fields"]:
            fails.append(
                "fixture: `coeff : Nat -> R` filled `fun _ => 0` must read as trivial DATA "
                "-- the ASCII arrow contains `>`, a Prop marker, and must be stripped first"
            )
    if not gen:
        fails.append("fixture: the generic all-zeros instance must be detected at all")
    elif gen[0]["guarded_by"]:
        fails.append(
            f"fixture: `[CommRing R]` must NOT count as a guard -- it is structural "
            f"machinery, not a content carrier; got {gen[0]['guarded_by']}"
        )

    # -- corpus assertions: things that must stay fixed --------------------
    # triv_hecke (PR #5581) and skeletonRealisation (PR #5621) were both demoted
    # to `def`. Either reappearing as an `instance` is a regression.
    for cls, pr in (("IwahoriHeckeAlgebra", "#5581"), ("TowerSummandRealization", "#5621")):
        if any(r["instance_class"] == cls for r in rows):
            fails.append(f"REGRESSION: {cls} is an `instance` again ({pr} demoted it)")

    # he4's global instance discharges `strong_duality := by norm_num`, a checked
    # certificate over concrete rationals -- never a trivial field.
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
    # Every class/structure this corpus declares. A `[…]` binder counts as a
    # guard only if it names one of these -- see the note in scan_file.
    corpus_classes = {
        m.group("name").split(".")[-1]
        for lines in stripped.values()
        for ln in lines
        if (m := CARRIER_HEAD.match(ln))
    }
    rows = []
    for p, lines in stripped.items():
        rows.extend(scan_file(p, lines, index, corpus_classes))

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
