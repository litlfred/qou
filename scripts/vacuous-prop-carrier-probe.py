#!/usr/bin/env python3
"""Find `class C : Prop` carriers that assert NOTHING -- and prove it in Lean.

Motivation
----------
`fluid-dynamics/core-levi-form.lean` declares five classes named after major
open problems in fluid dynamics:

    class NSCounterexample : Prop where
      exists_singularity_time : ∀ (D₀ : ℝ), 0 ≤ D₀ → ∃ T : ℝ, 0 ≤ T
    class CriticalExponent : Prop where
      alpha_three_eq_four : (3 * 4 : ℕ) = 12

Every one is discharged by picking zero, verified against Lean (exit 0, no
`sorryAx`). Both theorems in that file take all five as hypotheses, so their
conditionality is decorative. AGENTS.md §3b-tax names this class of defect --
"every field is a tautology about the subject ... so the carrier is equivalent
to True and any [C]-conditional result is unconditional" -- but the shipped
audit's `proof-claims-unencoded` keys on a DOCSTRING-vs-fields mismatch, so a
carrier with no docstring promises, like these five, is invisible to it.

Method: shape filter, then PROOF
--------------------------------
Syntax alone cannot decide this -- `∃ T : ℝ, 0 ≤ T` and `∃ T : ℝ, IsSingular T`
look alike and only one is trivial. So the shape filter only proposes; the
verdict comes from Lean actually discharging the carrier.

To keep the probe self-contained and honest, only SELF-CONTAINED carriers are
tested: every field type must mention nothing but ℝ/ℕ/ℤ, numerals, and logical
vocabulary. A carrier referring to `Phi1_of_ordering` or `pieceVolume` is
skipped rather than guessed at -- it may well be vacuous too, but proving that
needs its own import cone and is out of scope here.

That restriction is not a limitation of the finding, it IS the finding's
shape: a carrier whose fields mention no domain object cannot say anything
about the domain.

Gate (`--check`)
----------------
Two phases, so the gate is useful whether or not Lean is present:

  Phase 1, no Lean needed -- the shape filter. A NEW self-contained `Prop`
  carrier is itself the smell, since a carrier whose fields mention no domain
  object cannot say anything about the domain. `--check` fails on any carrier
  absent from `docs/audits/vacuous-prop-carrier-baseline.json`.

  Phase 2, needs Lean -- `--emit` the probe and run it, which is what turns a
  candidate into a verdict.

The baseline is a RATCHET in the sense AGENTS.md gives the precision gates:
it drains, it never grows. Adding an entry to silence the gate defeats the
mechanism; the fix is to encode the carrier's real content so the shape filter
stops matching it. If `lean` is unavailable the gate says the proof phase was
SKIPPED rather than passing quietly.

Usage:  vacuous-prop-carrier-probe.py [--self-test] [--emit OUT.lean]
                                      [--json OUT] [--check] [--write-baseline]
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "dupcensus", ROOT / "scripts" / "duplicate-class-declaration-census.py"
)
dupcensus = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dupcensus)

CONTENT = ROOT / "folio"

CLASS_PROP = re.compile(
    r"^\s*(?:noncomputable\s+|private\s+|protected\s+|scoped\s+|local\s+)*"
    r"class\s+(?P<name>[A-Za-z_][A-Za-z0-9_']*)(?P<params>[^:]*):\s*Prop\s*where"
)
FIELD = re.compile(r"^(?P<indent>\s+)(?P<name>[A-Za-z_][A-Za-z0-9_']*)\s*:(?P<type>.*)$")

# Vocabulary a SELF-CONTAINED field type may use. Anything else -- a defined
# function, a structure projection, another class -- means the field talks
# about a domain object, and this probe declines to judge it.
ALLOWED = {
    "ℝ", "ℕ", "ℤ", "ℚ", "Real", "Nat", "Int", "Rat", "Prop", "True", "False",
    "forall", "exists", "fun", "if", "then", "else",
}
IDENT = re.compile(r"[A-Za-zÀ-ʯ_][A-Za-z0-9À-ʯ_'₀-₉]*")


# Names bound INSIDE the type by ∀/∃/λ. Collected explicitly rather than
# guessed at by length or case: an earlier version allowed short lowercase
# identifiers only, which rejected `∀ (E : ℝ), 0 ≤ E → ∃ K : ℝ, …` -- both
# binders uppercase -- and so classified the very shape this probe exists to
# find as "mentions a domain object". The self-test pins that case.
BINDER = re.compile(r"[∀∃λ]\s*(?:\(|\{|⦃)?\s*((?:[A-Za-zÀ-ʯ_][A-Za-z0-9À-ʯ_'₀-₉]*\s*)+)")


def bound_names(ty: str) -> set[str]:
    out: set[str] = set()
    for m in BINDER.finditer(ty):
        out.update(m.group(1).split())
    return out


def self_contained(ty: str, own_fields: set[str], binders: set[str]) -> bool:
    local = bound_names(ty)
    for m in IDENT.finditer(ty):
        w = m.group(0)
        if w in ALLOWED or w in own_fields or w in binders or w in local:
            continue
        return False
    return True


def carriers(lines: list[str]) -> list[dict]:
    out = []
    stack: list[str] = []
    kinds: list[str] = []
    for n, line in enumerate(lines):
        if m := dupcensus.NS_OPEN.match(line):
            stack.append(m.group(1)); kinds.append("ns"); continue
        if dupcensus.SECTION.match(line):
            kinds.append("sec"); continue
        if dupcensus.NS_END.match(line):
            if kinds and kinds.pop() == "ns" and stack:
                stack.pop()
            continue
        m = CLASS_PROP.match(line)
        if not m:
            continue
        fields: dict[str, str] = {}
        pending = None
        for body in lines[n + 1 :]:
            if not body.strip():
                continue
            if not body.startswith((" ", "\t")):
                break
            fm = FIELD.match(body)
            if fm and ":=" not in body:
                pending = fm.group("name")
                fields[pending] = " ".join(fm.group("type").split())
            elif pending is not None:
                fields[pending] = (fields[pending] + " " + " ".join(body.split())).strip()
            else:
                break
        if not fields:
            continue
        binders = set(IDENT.findall(m.group("params")))
        if all(self_contained(t, set(fields), binders) for t in fields.values()):
            out.append(
                {
                    "name": m.group("name"),
                    "namespace": ".".join(stack) or "<root>",
                    "line": n + 1,
                    "params": m.group("params").strip(),
                    "fields": fields,
                    "decl": "\n".join(
                        [line.rstrip()] + [f"  {k} : {v}" for k, v in fields.items()]
                    ),
                }
            )
    return out


def emit(rows: list[dict]) -> str:
    """A standalone Lean file that re-declares each candidate and tries to prove it.

    Each attempt is INDEPENDENT: a failure to discharge one says nothing about
    the others, and a failure is not evidence the carrier has content -- only
    that this tactic did not find the witness. The positive direction is the
    only one this probe can settle.
    """
    parts = [
        "import Mathlib.Data.Real.Basic",
        "import Mathlib.Tactic",
        "",
        "-- Generated by scripts/vacuous-prop-carrier-probe.py. Each carrier is",
        "-- re-declared verbatim and an attempt is made to inhabit it outright.",
        "-- A carrier that elaborates below asserts NOTHING: it is inhabited with",
        "-- no hypothesis, so every `[C]`-conditional result downstream is in fact",
        "-- unconditional. A carrier that does NOT elaborate is simply undecided",
        "-- here -- absence of a witness is not evidence of content.",
        "",
        "set_option linter.unusedVariables false",
        "",
    ]
    for i, r in enumerate(rows):
        safe = f"Cand{i}"
        decl = r["decl"].split("\n")
        head = re.sub(r"class\s+[A-Za-z_][A-Za-z0-9_']*", f"class {safe}", decl[0], count=1)
        parts.append(f"-- {r['namespace']}.{r['name']}  ({r['file']}:{r['line']})")
        parts.append(head)
        parts.extend(decl[1:])
        parts.append(
            f"theorem probe{i} : {safe} := by\n"
            f"  constructor <;>\n"
            f"    first\n"
            # EVERY alternative ends in `done`. Without it the probe silently
            # under-reports: `first` advances to the next alternative only when
            # the previous one FAILS, and a tactic that makes progress without
            # closing the goal has not failed. Measured -- `norm_num` rewrites
            # `∃ q : ℝ, q > 0` to `∃ q, 0 < q`, `first` commits to that, and the
            # goal is left open. That one behaviour put 14 provable carriers in
            # the "undecided" column, and widening the alternative list changed
            # nothing at all until `done` was added.
            f"      | (norm_num; done)\n"
            f"      | (intros; norm_num; done)\n"
            f"      | (intros; exact ⟨0, by norm_num⟩)\n"
            f"      | (intros; exact ⟨1, by norm_num⟩)\n"
            f"      | (intros; refine ⟨0, ?_⟩ <;> norm_num; done)\n"
            f"      | (intros; refine ⟨1, ?_⟩ <;> norm_num; done)\n"
            f"      | (intros; refine ⟨0, ?_, ?_⟩ <;> norm_num; done)\n"
            f"      | (intros; refine ⟨1, ?_, ?_⟩ <;> norm_num; done)\n"
            f"      | (intros; exact ⟨fun _ => 0, fun _ => rfl⟩)\n"
            f"      | (intros; exact ⟨fun _ => 1, fun _ => rfl⟩)\n"
            f"      | (intro e h; exact ⟨e, h, le_refl e⟩)\n"
            f"      | (intros; simp; done)\n"
            f"      | (trivial; done)"
        )
        parts.append("")
    return "\n".join(parts)


FIXTURE = """\
namespace F
class Trivial1 : Prop where
  f : ∀ (E : ℝ), 0 ≤ E → ∃ K : ℝ, 0 ≤ K ∧ K ≤ 2 * E
class HasDomainObject : Prop where
  g : ∀ q : ℝ, pieceVolume q = 0
end F
"""


def self_test() -> int:
    rows = carriers(FIXTURE.split("\n"))
    names = {r["name"] for r in rows}
    fails = []
    if "Trivial1" not in names:
        fails.append("a self-contained numeric carrier must be a candidate")
    if "HasDomainObject" in names:
        fails.append(
            "a carrier mentioning a domain object (`pieceVolume`) must be SKIPPED "
            "-- this probe declines to judge what it cannot re-declare standalone"
        )
    for f in fails:
        print("  self-test FAIL:", f)
    print(f"self-test: {'PASS' if not fails else f'{len(fails)} FAILURE(S)'}")
    return len(fails)


BASELINE = ROOT / "docs" / "audits" / "vacuous-prop-carrier-baseline.json"


def key(r: dict) -> str:
    return f"{r['file']}::{r['namespace']}.{r['name']}"


def gate(rows: list[dict], write: bool) -> int:
    import shutil

    have_lean = shutil.which("lean") is not None
    current = {key(r): r for r in rows}

    if write:
        old = json.loads(BASELINE.read_text())["entries"] if BASELINE.exists() else {}
        entries = {
            k: old.get(k, {"verdict": "unreviewed", "note": ""}) for k in sorted(current)
        }
        dropped = sorted(set(old) - set(entries))
        BASELINE.write_text(
            json.dumps(
                {
                    "schema": "vacuous-prop-carrier-baseline/v1",
                    "note": (
                        "Self-contained `class … : Prop where` carriers -- every field type "
                        "mentioning nothing but numeric types, numerals and logical "
                        "vocabulary. Such a carrier cannot say anything about the domain. "
                        "This baseline DRAINS and never grows: silence a new entry and the "
                        "gate stops meaning anything. The fix is to encode the carrier's "
                        "real content so the shape filter no longer matches it."
                    ),
                    "entries": entries,
                },
                indent=2,
                ensure_ascii=False,
            )
            + "\n"
        )
        print(f"\nbaseline written: {len(entries)} entries"
              + (f", {len(dropped)} drained" if dropped else ""))
        for d in dropped:
            print(f"  drained: {d}")
        return 0

    if not BASELINE.exists():
        print(f"\nFAIL: no baseline at {BASELINE.relative_to(ROOT)} -- "
              f"run --write-baseline once to establish it")
        return 1
    base = json.loads(BASELINE.read_text())["entries"]
    new = sorted(set(current) - set(base))
    drained = sorted(set(base) - set(current))

    print()
    if not have_lean:
        print("NOTE: `lean` not on PATH -- phase 2 (proving the candidates) was SKIPPED.")
        print("      Phase 1 (the shape filter) still ran and is what follows.")
    if drained:
        print(f"{len(drained)} baseline entr{'y' if len(drained)==1 else 'ies'} no longer "
              f"match the filter -- re-run with --write-baseline to drain:")
        for d in drained:
            print(f"  drained: {d}")
    if new:
        print(f"FAIL: {len(new)} self-contained Prop carrier(s) not in the baseline.")
        print("      A carrier whose fields mention no domain object asserts nothing about")
        print("      it. Encode the real content -- do NOT add the entry to the baseline.")
        for k in new:
            print(f"  new: {k}")
        return 1
    print(f"OK: all {len(current)} self-contained carriers are in the baseline.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--emit")
    ap.add_argument("--json")
    ap.add_argument("--check", action="store_true",
                    help="fail if any self-contained carrier is absent from the baseline")
    ap.add_argument("--write-baseline", action="store_true",
                    help="(re)write the baseline from the current tree -- only ever to "
                         "REMOVE drained entries, never to silence a new one")
    args = ap.parse_args()
    if args.self_test and self_test():
        return 1

    rows: list[dict] = []
    n_files = n_prop = 0
    for p in sorted(CONTENT.rglob("*.lean")):
        if ".lake" in str(p):
            continue
        n_files += 1
        lines = dupcensus.strip_comments(p.read_text(errors="replace")).split("\n")
        n_prop += sum(1 for l in lines if CLASS_PROP.match(l))
        for r in carriers(lines):
            r["file"] = str(p.relative_to(ROOT))
            rows.append(r)

    print(f"scanned {n_files} .lean under content/")
    print(f"  `class … : Prop where` carriers          : {n_prop}")
    print(f"  ...self-contained (no domain object)     : {len(rows)}  <- candidates to PROVE")
    print()
    for r in rows:
        print(f"  {r['namespace']}.{r['name']}")
        print(f"      {r['file'].replace('folio/quantum-observable-universe/','')}:{r['line']}"
              f"  ({len(r['fields'])} field(s))")

    if args.emit:
        Path(args.emit).write_text(emit(rows))
        print(f"\nwrote {args.emit} — run `lean` on it; every `probe<i>` that elaborates"
              f"\nis a carrier that asserts nothing.")
    if args.json:
        Path(args.json).write_text(json.dumps(rows, indent=2) + "\n")

    if args.write_baseline or args.check:
        rc = gate(rows, write=args.write_baseline)
        if rc:
            return rc
    return 0


if __name__ == "__main__":
    sys.exit(main())
