#!/usr/bin/env python3
"""For each still-live self-assuming projection, is its carrier a DEFECT or an ACCESSOR?

## The question this answers, and the one it replaces

`scripts/sap-projection-liveness.py` says *which* ledger findings are still
`:= ctx.field`. It does not say which of those are worth fixing, and the
obvious discriminator is wrong.

**"Is the class parameterised?" does not separate them.** Tried first, on the
31 library projections: it splits 8 / 10 / 13, and the 8 "parameterised" bucket
contained `KnotFactorSpectralContext`, `SortingColorEnergyContext` and
`SixTermMassFormulaContext` — carriers with **ten, twelve and eight data
fields** respectively — counts taken from the source by hand, since every
parser this script has had got them wrong. A class can take a parameter *and*
carry ten objects the instance chooses; the parameter buys nothing then. (All
three have since been repaired and none appears in a current run.)

**The discriminator is DATA FIELDS.** AGENTS.md §3b-cond item 5 asks whether
the class axiomatises *hypotheses* or supplies the objects the claim is about.
Operationally:

- **`data = 0`** — every field is a proposition about the class's own
  parameters, so a `[C args]` binder constrains what the *caller* brought and
  the projection is Mathlib's accessor idiom (`Group.mul_assoc :=
  Group.mul_assoc`). Not a defect. Adjudicated so for the §4 gate classes on
  2026-08-31.
- **`data > 0`** — the instance chooses the objects, so the binder assumes
  nothing about anything the caller supplied. This is the defect, and the
  repair is to move the data to parameters.

Measured on `main` 2026-09-02 over the 31 library projections:
**19 defect, 2 accessor, 10 unresolved.** After eleven repairs and the five
fixes below: library **2 / 13 / 0**, whole tree **6 / 24 / 0**.

**`unresolved` is now 0, and that is where the last two library defects came
from.** The ten unresolved rows were never "clean" — the note below said so —
and once `find_class` handled multi-line signatures, eleven of the fifteen
tree-wide turned out to be **accessors** and the rest real defects that had
been invisible. `NobleGasMultiOperator` and `AtomicNfWitnessContext` (thirteen
data fields) are both in that second group.

## The parser was wrong five times, and three of them moved verdicts

Two came out of Copilot's review of PR #6422; the rest out of reading a file
whose real answer was already known. **None was visible in the totals.**

4. **Wrong carrier.** `carrier_of` returned the *first* class-shaped binder,
   not the one the body projects. On
   `ShellClosureStability.lean::shell_closure_monotone` that is
   `[HasFrobeniusStability D_prev]` (one data field) rather than
   `hi : ShellClosureMonotone …` (zero) — DEFECT for a row whose true verdict
   is ACCESSOR. It also returned **`CommRing`** as the carrier for two rows,
   by matching `[CommRing R]`. Now the projected variable is read out of the
   body and *its* binder type looked up.
5. **One-line class signatures only.** A `class … where` spanning lines read
   as `unresolved`, which the note below correctly said was not `clean`:
   fixing it emptied that bucket and surfaced two real library defects.

1. **Under-count.** `FIELD` was `^  (\w+)\s*:`. `\w` excludes the characters
   Lean identifiers use — `'`, `!`, `?`, all of unicode — so a field named
   `S'` or `y_λ` was invisible; and it captured one name per line, so
   `W_sym W_std W_alt : R` read as one field instead of three.
2. **Over-count.** The first repair accepted any run of non-delimiter tokens
   before a colon, so a *docstring* line carrying a colon parsed as fields:
   `/-- Manuscript claim — atomic-mass recovery: …` became six.
   `BindingAssemblyContext` (four data fields) was reported with eleven.
3. **Mis-classification, and this is the one that mattered.** A field whose
   type begins on the *next* line shows an empty type on its own line, so
   `CLAIMY` finds no `=` and a **claim field is counted as data**.

### 🛑 The "zero verdicts flipped" claim recorded here earlier was WRONG

It compared the original parser against the *over-counting* intermediate,
where (2) inflated exactly the rows (3) deflated, so the two errors cancelled
in the totals and nothing appeared to move. Against the corrected parser,
**8 of 36 rows flip `DEFECT` → `ACCESSOR`** — every change is downward; no row
moved the other way.

The structural argument offered for that claim was also wrong. It reasoned
that an under-count can only manufacture a *false accessor* — true of bug (1),
and irrelevant, because the bug that decided verdicts was in the **claim**
direction and manufactures false *defects*.

**The corrected parser reproduces the known hand adjudication**, which is the
real evidence it is right: all four §4 gate classes
(`MassAnchorStableGateClass`, `MassDirectionSanityGateClass`,
`DirectionSanityGateClass`, `RadiusOfConvergenceGateClass`) now read
`ACCESSOR` — the verdict reached by hand on 2026-08-31 and recorded in the
ledger, which the old parser contradicted.

`--selftest` pins the parser against hand-counted carriers so a fourth
regression is caught by the script rather than by whoever next opens a file.

Quote the counts from a run, never from this docstring.

## Three sharper discriminators were tried after this one. All three fail.

Recorded so the next agent does not build a fourth heuristic instead of
reading the files.

1. **Explicit argument vs instance binder.** `(h : C)` looks like the caller
   supplying the record and `[ctx : C]` looks like instance search supplying
   it. Measured over the 19: 2 explicit, 17 instance. But it is **not a
   logical difference** — both elaborate to `∀ c : C, P c`. The binder style
   changes how the value is *found*, not what the theorem *says*. Two files
   with identical content would land in different buckets.

2. **Does the carrier's docstring disclose the field as an open input?**
   (Matching `open hypothesis` / `not derived` / `conjectural` / `OPEN` /
   `never asserting` near the declaration.) Splits 7 / 12 — and is wrong in
   both directions. `HasFrobeniusStability` scores **disclosed**, and that is
   the file whose ambient `LE` was `fun _ _ => True`, so every `≤` in it was
   `True`: a carrier can be candid in prose while the surrounding file empties
   the claim. Worse, the 7 includes a file this session had just edited, so
   the signal partly measured my own newly-written note. A prose signal
   graded on prose the grader wrote is not a measurement.

3. **Data-field count**, the one this script reports. It over-flags:
   `BondExtensiveBinding` (`data = 2` when measured 2026-09-02; the row has
   since left the queue) is the *honest* version of the same shape — the file
   states plainly that `extensive` is the arc's open input and that
   `binding_eq_bond_energy` is *"just `h.extensive`, exposed as a named
   consumer"*. Counting fields cannot see that.

**Why no syntactic signal can work.** `theorem foo [ctx : C] : ctx.a = ctx.b
:= ctx.claim` is a true, non-vacuous statement — it is the identity on a
field. What AGENTS.md §3b-cond item 5 asks is whether that field is an honest
*open hypothesis* the file names as such, or the block's own *conclusion*
dressed as a derivation. That is a question about the claim's role in the
argument, and it is settled by reading the file and its `.md`, not by shape.

Use this script to **order** the reading. Do not use it to skip it.

## Limits — quote them with the number

- **`unresolved` is 0 as of 2026-09-03, and was never "clean" when it was
  not.** Multi-line `class … where` signatures are now handled; an `extends`
  chain or a carrier in some other form would still land there, and would
  still need reading rather than counting. When the bucket was ten rows deep
  it was hiding two real library defects and eight accessors.
- **The data/claim split is heuristic.** A field counts as a *claim* when its
  type contains a relation or quantifier (`= ≤ < > ∀ ∃ ↔ ≠ ∈`, `Nonempty`,
  `IsOpen`, `Subsingleton`, or ends in `Prop`); everything else counts as
  data. A `Prop`-valued field whose type is an opaque alias reads as data, and
  a data field whose type happens to mention `→` reads as a claim.
- So this is a **work-order, not a verdict**. Each row still needs the class
  read before it is repaired, and `data = 0` in particular is a reason to look
  rather than a licence to skip — see the gate classes, where the real gap was
  the *converse* of the equivalence the `.md` claimed, not the accessor.

USAGE
    python3 scripts/sap-carrier-shape.py                 # all trees
    python3 scripts/sap-carrier-shape.py --tree LIB      # library only
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
import tempfile
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "folio/quantum-observable-universe"

# A field's type "looks like a claim" if it carries a relation or quantifier.
#
# **`≥` was missing while `≤` was present** — the sixth bug in this file, and
# the same *direction* as the multi-line-type one: a claim read as data, which
# manufactures a false DEFECT. Measured: `NobleGasMultiOperator.multi :
# bindingMultiplicity S q ≥ 2` and `HasBindingMultiplicity`'s field both
# counted as data, so two parameterised accessors were reported as the last
# two library defects.
#
# The asymmetry is the lesson. An operator absent here does not merely go
# uncounted — it lands in the *other* bucket. So the set is written out
# symmetrically, with each relation's mirror beside it.
CLAIMY = re.compile(
    r"[=≠∀∃∈∉↔]"          # equality, membership, quantifiers, iff
    r"|[≤≥<>]"             # order — BOTH directions
    r"|[⊆⊇⊂⊃]"             # inclusion — both directions
    r"|[≡≃≅≈]"             # equivalence / isomorphism
    r"|∣"                  # divides (U+2223; NOT the ASCII bar of `|x|`)
    r"|Nonempty|IsOpen|Subsingleton"
    r"|Prop\s*$"
)

# A field line: exactly two spaces, then one or more names, then `:` (not `:=`).
#
# `(\w+)` was WRONG in two ways, both of which UNDER-count data fields — and an
# under-count flips a DEFECT verdict to ACCESSOR, which is the one direction
# that hides work rather than inventing it.
#
#   1. `\w` excludes the characters Lean identifiers actually use — `'`, `!`,
#      `?`, and the whole unicode range (`Δ`, `χ`, `y_λ`, `σ₀`). A field named
#      `S'` was invisible. (Copilot review, PR #6422.)
#   2. It captured only ONE name, so the standard multi-binder line
#      `W_sym W_std W_alt : R` counted as a single field instead of three.
#
# The first repair — "any run of non-delimiter tokens before a colon" — then
# OVER-counted, and by more than the original under-counted. A DOCSTRING line
# can contain a colon:
#
#     /-- Manuscript claim — atomic-mass recovery: the atomic mass is the
#
# and its six words parsed as six field names. `BindingAssemblyContext` has
# four data fields and was reported with eleven. So the run is now checked
# token by token against what a Lean identifier can actually be, and comment
# openers are rejected outright.
#
# Two parser bugs in this one function in one session, in opposite directions.
# Both were caught by reading a carrier whose real field count I already knew —
# which is the argument for the `--selftest` below, and against trusting any
# count from this script that has not been spot-checked against a file.
_NAME = r"[^\s:()\[\]{}⟨⟩,]+"
FIELD = re.compile(rf"^  ((?:{_NAME}[ \t]+)*{_NAME})[ \t]*:(?!=)(.*)$", re.M)

# A Lean identifier: a letter or `_`, then word chars and the marks Lean allows
# (`'`, `!`, `?`, subscripts). Deliberately permissive about unicode letters —
# `Δ`, `χ`, `σ₀` are all real field names here — and deliberately strict about
# the first character, which is what rejects `/--`, `--`, `—` and `*`.
_IDENT = re.compile(r"[^\W\d]['\w!?₀-₉ₐ-ₜᵢⱼₖ]*$", re.UNICODE)


def _field_names(line_names: str) -> list[str] | None:
    """The names on a field line, or `None` if this is not a field line."""
    names = line_names.split()
    if not names or not all(_IDENT.match(n) for n in names):
        return None
    return names


def _fields(body: str) -> list[tuple[list[str], str]]:
    """`(names, type)` per field, with MULTI-LINE types joined.

    The third defect this parser has had, and the one the earlier
    line-at-a-time version could not see: a field whose type starts on the
    following line —

        claim_six_term_recovery :
          atomic_mass = (Finset.univ.sum …)

    presents an EMPTY type on its own line, so `CLAIMY` finds no `=` and the
    field is counted as data. That is the direction that matters:
    `BindingAssemblyContext` read `data = 5, claim = 0` against a true 4 / 1,
    so a claim field masqueraded as a fifth object the instance chooses.

    So the type of each field is everything up to the next field line.
    """
    out: list[tuple[list[str], str]] = []
    pending: list[str] | None = None
    parts: list[str] = []
    for line in body.splitlines():
        m = FIELD.match(line)
        names = _field_names(m.group(1)) if m else None
        if names is None:
            if pending is not None:
                parts.append(line)
            continue
        if pending is not None:
            out.append((pending, " ".join(parts)))
        pending, parts = names, [m.group(2)]
    if pending is not None:
        out.append((pending, " ".join(parts)))
    return out


def load_tree() -> dict[str, str]:
    out = {}
    for f in glob.glob(str(CONTENT / "**/*.lean"), recursive=True):
        if "/.lake/" in f:
            continue
        out[os.path.relpath(f, ROOT)] = Path(f).read_text(errors="replace")
    return out


def find_class(tree: dict[str, str], cname: str):
    # The signature may span lines. Continuation lines are indented, so the
    # span allows a newline only when the next character is whitespace — that
    # bounds the match without letting `.*?` run to some later `where`.
    #
    # `ShellClosureMonotone` is why: its binders occupy four lines, so the
    # one-line matcher reported it `unresolved`, and `unresolved` is not
    # `clean` — hand-read, it has ZERO data fields and is an ACCESSOR.
    pat = re.compile(
        rf"^(?:class|structure)\s+{re.escape(cname)}\b"
        rf"((?:[^\n]|\n(?=\s))*?)\bwhere\s*$",
        re.M,
    )
    for f, t in tree.items():
        m = pat.search(t)
        if not m:
            continue
        body = t[m.end():]
        nb = re.search(r"\n(?=\S)", body)
        body = body[: nb.start()] if nb else body[:4000]
        # One entry PER NAME: `W_sym W_std W_alt : R` is three fields, not one.
        data = claim = 0
        for names, ty in _fields(body):
            if CLAIMY.search(ty):
                claim += len(names)
            else:
                data += len(names)
        return f, m.group(1).strip(), data, claim
    return None, None, None, None


def carrier_of(tree: dict[str, str], path: str, decl: str) -> str | None:
    t = tree.get(path) or Path(ROOT / path).read_text(errors="replace")
    short = decl.split(".")[-1]
    m = re.search(
        rf"^\s*(?:theorem|lemma|def|noncomputable def)\s+{re.escape(short)}\b(.*?)(?=\n\S)",
        t,
        re.S | re.M,
    )
    if not m:
        return None
    whole = m.group(1)
    sig = whole.split(":=")[0]

    # FIRST: the class the body actually PROJECTS.
    #
    # Taking "the first class-shaped binder" is wrong whenever the projected
    # class is not the first one, and the miss is not cosmetic — it reports
    # the wrong carrier's field counts and so the wrong verdict.
    #
    # Measured on `ShellClosureStability.lean::shell_closure_monotone`: the
    # signature opens `[HasFrobeniusStability D_prev]` (one DATA field,
    # `sigma`), which the old scan returned, giving `data = 1` -> DEFECT. The
    # body is `hi.monotone`, and `hi : ShellClosureMonotone D_prev D q h` has
    # **zero** data fields — its one field is a proposition about the class's
    # own parameters, so a `ShellClosureMonotone D_prev D q h` hypothesis
    # constrains what the CALLER brought. That is the accessor idiom, and the
    # true verdict is ACCESSOR.
    #
    # So: read the projected variable out of the body, then look up ITS binder
    # type. Only fall back to binder order when that fails.
    pm = re.search(r":=\s*(?:by\s+exact\s+)?([A-Za-z_][\w']*)\.[A-Za-z_]", whole)
    if pm:
        var = pm.group(1)
        bm = re.search(rf"[\[(]\s*{re.escape(var)}\s*:\s*([A-Z][\w'.]*)", sig)
        if bm:
            return bm.group(1).split(".")[-1]

    for pat in (r"\[\s*\w+\s*:\s*([A-Z][\w'.]*)", r"\[\s*([A-Z][\w'.]*)",
                r"\(\s*\w+\s*:\s*([A-Z][\w'.]*)"):
        cm = re.search(pat, sig)
        if cm:
            return cm.group(1).split(".")[-1]
    return None


def selftest() -> int:
    """Regression tests for the field parser and the carrier resolver.

    Every bug these have had was found by reading a file whose real answer was
    already known, and none was visible in the totals — an UNDER-count (`\\w`
    missing `S'`, one name per line), an OVER-count (a docstring line with a
    colon parsing as six fields), a MIS-CLASSIFICATION (a type starting on the
    next line, so a claim counted as data), and a wrong CARRIER (the first
    class binder rather than the projected one).

    ## Fixtures, not live carriers

    The first version of this selftest pinned `BindingAssemblyContext` at its
    hand-counted `4 / 1` — and then **this drain deleted that class**, so the
    test failed for a reason that had nothing to do with the parser. A test
    pinned to a carrier the work is removing goes stale by construction.

    So each bug shape is captured as a literal fixture. These survive the
    drain and say what they are testing.
    """
    bad = 0

    def check(name: str, got, want) -> None:
        nonlocal bad
        ok = got == want
        bad += not ok
        print(f"  {'ok  ' if ok else 'FAIL'} {name:<44} {got}  (want {want})")

    # (1) UNDER-count: `\w` misses `'` and unicode, and captures one name per
    #     line. `S'`, `y_λ` and the three-name binder must all be seen.
    check("under: apostrophe / unicode / multi-binder",
          _fields("  S' : R\n  y_λ : R\n  W_sym W_std W_alt : R\n"),
          [(["S'"], " R"), (["y_λ"], " R"), (["W_sym", "W_std", "W_alt"], " R")])

    # (2) OVER-count: a docstring line carrying a colon is not a field line.
    check("over: docstring line with a colon",
          _fields("  /-- Manuscript claim — atomic-mass recovery: the mass is\n"
                  "      the sum. -/\n  atomic_mass : ℝ\n"),
          [(["atomic_mass"], " ℝ")])

    # (3) MIS-CLASSIFICATION: a type beginning on the NEXT line must still be
    #     seen as a claim, not silently counted as data.
    ml = _fields("  claim :\n    mass = other\n")
    check("multi-line type is still a claim",
          (len(ml), bool(ml and CLAIMY.search(ml[0][1]))), (1, True))

    # (4) `:=` is a default value, not a field declaration.
    check("`:=` is not a field", _fields("  foo := 3\n"), [])

    # (5) CLAIMY must be symmetric in each relation. `≥` was missing while `≤`
    #     was present, so `multi : … ≥ 2` counted as DATA and two accessors
    #     were reported as defects. Every operator is checked in both
    #     directions, since an absent one lands in the wrong bucket rather
    #     than in none.
    for op in "= ≠ ≤ ≥ < > ⊆ ⊇ ⊂ ⊃ ≡ ≃ ≅ ≈ ∈ ∉ ∣ ↔".split():
        check(f"CLAIMY sees `{op}`", bool(CLAIMY.search(f" a {op} b")), True)
    # …and must NOT fire on an ordinary function-typed data field.
    check("CLAIMY ignores a plain arrow", bool(CLAIMY.search(" ℕ → R")), False)

    # find_class must handle a signature on one line AND one spanning lines —
    # `ShellClosureMonotone`'s occupies four, and the one-line matcher
    # reported it `unresolved`, which is not `clean`.
    for label, src in [
        ("find_class: one-line signature", "class Foo where\n  a : Nat\n  h : a = a\n"),
        ("find_class: multi-line signature",
         "class Foo\n    (x : Nat)\n    [Bar x] : Prop where\n  h : x = x\n"),
    ]:
        f, _p, d, c = find_class({"fixture.lean": src}, "Foo")
        check(label, (f is not None, d, c),
              (True, 1, 1) if "one-line" in label else (True, 0, 1))

    print("selftest: PASS" if not bad else f"selftest: {bad} FAILED")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--selftest", action="store_true",
                    help="check the field parser against hand-counted carriers")
    ap.add_argument("--tree", choices=["LIB", "SIBLING"], help="restrict to one tree")
    ap.add_argument("--json", help="write the full result set here")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    # A private temp file, cleaned up on any exit path. The previous fixed
    # `ROOT / "sap-live.tmp.json"` clobbered concurrent runs and, when the
    # liveness call raised, left an untracked file in the repo root — which in
    # this repo reads as real work to the next agent's `git status`.
    fd, tmp = tempfile.mkstemp(prefix="sap-live-", suffix=".json")
    os.close(fd)
    try:
        # `capture_output=True, check=True` raised a CalledProcessError whose
        # message names the command and NOTHING the child printed, so a
        # liveness failure surfaced as an exit code with the traceback that
        # explains it discarded. Relay both streams before failing (Copilot,
        # PR #6422). This is the whole reason a script gets called "flaky":
        # the output that would identify the fault is captured and dropped.
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/sap-projection-liveness.py"),
             "--json", tmp],
            capture_output=True, text=True,
        )
        if proc.returncode != 0:
            sys.stderr.write(proc.stdout or "")
            sys.stderr.write(proc.stderr or "")
            raise SystemExit(
                f"sap-projection-liveness.py exited {proc.returncode} "
                f"(its output is above)")
        rows = json.loads(Path(tmp).read_text())
    finally:
        Path(tmp).unlink(missing_ok=True)

    sel = [r for r in rows if r["status"] == "PROJECTION"
           and (args.tree is None or r["tree"] == args.tree)]
    tree = load_tree()

    out, buckets = [], {"DEFECT": [], "ACCESSOR": [], "unresolved": []}
    for r in sorted(sel, key=lambda r: r["file"]):
        c = carrier_of(tree, r["file"], r["decl"])
        if not c:
            buckets["unresolved"].append((r, "no class binder found"))
            out.append({**r, "carrier": None, "verdict": "unresolved"})
            continue
        f, params, nd, nc = find_class(tree, c)
        if f is None:
            buckets["unresolved"].append((r, f"class {c} not found"))
            out.append({**r, "carrier": c, "verdict": "unresolved"})
            continue
        v = "ACCESSOR" if nd == 0 else "DEFECT"
        buckets[v].append(
            (r, f"{c}  data={nd} claim={nc}  params={'YES' if params else 'NONE'}")
        )
        out.append({**r, "carrier": c, "carrier_file": f, "data_fields": nd,
                    "claim_fields": nc, "verdict": v})

    for k in ("DEFECT", "ACCESSOR", "unresolved"):
        v = buckets[k]
        print(f"\n### {k}: {len(v)}")
        for r, s in v:
            print(f"  {s:<62} {os.path.basename(r['file'])}::{r['decl']}")
    print(f"\ntotals: DEFECT {len(buckets['DEFECT'])}  "
          f"ACCESSOR {len(buckets['ACCESSOR'])}  "
          f"unresolved {len(buckets['unresolved'])}")

    if args.json:
        Path(args.json).write_text(json.dumps(out, indent=2))
        print(f"wrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
