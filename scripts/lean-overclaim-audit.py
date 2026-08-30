#!/usr/bin/env python3
"""Flag Lean declarations that claim more, or less, than they can.

Two families, both found by reading during the q-RH arc review (2026-08-29) and
neither caught by any existing checker:

  OVERCLAIM  an `axiom` asserted for every inhabitant of a domain wider than the
             claim's subject.  Four such axioms in that arc each proved `False`
             (beans `qou-hwax`, `qou-qexf`); a fifth, `qou-rhax`, was the same
             shape a week earlier.  The tell is a universally quantified axiom
             whose binders range over a structure that does not carry the
             claim's hypotheses, or over two data parameters that must be two
             faces of one object but are quantified independently.

  UNDERCLAIM a conjecture carrier that asserts nothing: a `class`/`structure`
             with no fields, or whose only fields are bare `Prop`/`True`.  The
             `holds : Prop` shape is inhabited by `⟨True⟩`, so a downstream
             `[C]`-conditional theorem proves nothing modulo `C`.

Both are CANDIDATES, not verdicts.  The overclaim family in particular cannot be
decided syntactically -- the check that settles it is semantic and cheap:
*construct the smallest inhabitant of the quantified domain and evaluate the
claim on it*.  That is what found all four (`q := 1, eigenvalues := fun _ => 2`
makes Castelnuovo-Severi read `4 <= 1`; empty ideal and spectrum lists make the
explicit formula read `0 = 2 + positive`).  This script narrows where to look.

COMMENTS ARE STRIPPED BEFORE MATCHING, and that is not a detail.  Measured on
this corpus: a naive grep for `holds : Prop` reports 38 files, of which **15 are
prose only** -- docstrings describing a stub that was already replaced.  A 39 %
false-positive rate from reading comments as code.  The same error inflated a
`sorry` count for a whole chapter to 6 when the true figure was 0.

CALIBRATION -- read before quoting any number this prints.

Measured on `content/` 2026-08-29, and the history matters more than the figure:

  172 candidates   first version
  131 candidates   after fixing a bug of my own: the binder classifier keyed on
                   the NAME (`hq`, `h1`) instead of the TYPE, so `(hq : 1 < q)`
                   and `(R : Type*)` counted as data parameters.  That one fix
                   collapsed `overclaim-independent-binders` from 43 to 3 -- the
                   family was almost entirely noise.

  78  overclaim-structure          <- precision NOT established
  39  contentless-carrier
   9  empty-carrier
   3  overclaim-independent-binders
   2  opaque-type-axiom

**The 78 is the weak number and should not be quoted as a defect count.**
Sampling it shows a substantial share are properly hypothesised: an axiom that
also binds `(hgs : IsGrobnerShirshovBasis ...)` IS constrained.  The script tries
to discount those by treating `Prop`-valued corpus structures as hypotheses --
and on this corpus that refinement changed the count by **zero**, because such
carriers are declared across multiple lines and often carry no `: Prop`
annotation at all.  A `structure` in `Type` used as a hypothesis is not
distinguishable from data by any syntactic rule, so this family will keep
over-flagging until something reads the axiom's statement rather than its
binders.

`contentless-carrier` (39) is the trustworthy family: `holds : Prop` is inhabited
by `<True>` whatever else is true, and the shape admits no benign reading.  A raw
grep for it reports 38 FILES of which 15 are prose only -- a 39 % false-positive
rate that stripping comments removes entirely.

What this detector does NOT see, and what pairs with it
------------------------------------------------------

This asks one question: *is the statement stronger than the truth* -- does a
declaration assert something for every inhabitant of a domain wider than the
claim's subject.  The mirror question -- *is the statement weaker than the
prose*, a docstring promising a limit or a property the statement never
localises -- is a different detector, `scripts/limit-claim-encoding-audit.py`.

**Neither subsumes the other, and the same field can pass one and fail the
other.**  Measured, not supposed: `HasQPlancherelCLT.bound` in
`lean/QOU/MathlibExt/QPlancherel.lean` was flagged by that detector and triaged
a false positive -- correctly for the question it asks, since the field carries
an explicit quantitative bound rather than an unlocalised limit, and blind to
whether that bound was *true*.  It was not: `Cq` fixed by the instance against
an `f_inf` ranging over all of `R` gives `Cq + 1 <= Cq`.  Refuted and fixed on
PR #6041.

So run both, and do not read a clean pass from either as a clean bill.

A repaired carrier needs a witness -- of the right object
--------------------------------------------------------

A refutation-driven repair can trade one unusable class for another, so the fix
should be shown *inhabited*, not merely unrefuted.

The trap is that "show it inhabited" is dischargeable against the wrong object.
A structure and a hypothesis class about that structure are different things,
and a witness for one says nothing about the other.  Worked case:
`reebSpectrumExample` inhabits `ReebSpectrum`, and settles nothing about
`HasReebSpectralCoords`, whose satisfiability needed its own proof -- that
witness has every `spec i = 1`, which would force `alpha_i = q` for all `i`.
Exhibit a witness of the thing the conditional theorems actually depend on.

Usage:
    python3 scripts/lean-overclaim-audit.py [--root content] [--json OUT]
    python3 scripts/lean-overclaim-audit.py --selftest
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

# ---------------------------------------------------------------- comment strip

def strip_comments(src: str) -> str:
    """Remove Lean block comments (`/- -/`, `/-- -/`, `/-! -/`) and `--` lines.

    Block comments nest in Lean, so this tracks depth rather than regexing.
    Newlines are preserved so reported line numbers stay true to the source.
    """
    out: list[str] = []
    i = 0
    depth = 0
    while i < len(src):
        if src.startswith("/-", i):
            depth += 1
            i += 2
            continue
        if src.startswith("-/", i) and depth:
            depth -= 1
            i += 2
            continue
        if depth == 0 and src.startswith("--", i):
            j = src.find("\n", i)
            if j < 0:
                break
            i = j
            continue
        ch = src[i]
        out.append(ch if (depth == 0 or ch == "\n") else " ")
        i += 1
    return "".join(out)


# ------------------------------------------------------------------ declarations

DECL_RE = re.compile(
    r"^(?P<kw>axiom|class|structure)\s+(?P<name>[A-Za-z_][\w'.]*)", re.M)


def _decl_body(code: str, start: int) -> str:
    """Text from `start` to the next top-level declaration keyword."""
    nxt = re.compile(
        r"^(axiom|class|structure|theorem|lemma|def|abbrev|instance|noncomputable|"
        r"example|end|namespace|open|section|@\[)", re.M)
    m = nxt.search(code, start + 1)
    return code[start:m.start() if m else len(code)]


# A binder's TYPE decides what it is -- not its name.  Keying on the name is how
# the first version of this script counted `(hq : 1 < q)` as a data parameter and
# reported 172 candidates where the tightened rule finds far fewer.
_PROPISH = re.compile(r"[<>=≤≥≠∈∉∣]|\\forall|\\exists|∀|∃|¬|Prop\b|Nonempty\b")
_TYPEISH = re.compile(r"^(Type|Sort)\b")
_DATAISH = re.compile(r"→|->|\b(List|Multiset|Finset|Array|Fin)\b")


def _binders(sig: str) -> list[tuple[str, str, str]]:
    """Binders as (names, type, kind) where kind is data | hypothesis | type | inst."""
    out = []
    for m in re.finditer(r"([\(\{\[])\s*([\w'\s₀-₉]+?)\s*:\s*([^\)\}\]]+)[\)\}\]]", sig):
        open_ch, names, ty = m.group(1), m.group(2).strip(), m.group(3).strip()
        if open_ch == "[":
            kind = "inst"
        elif _TYPEISH.match(ty):
            kind = "type"
        elif _PROPISH.search(ty):
            kind = "hypothesis"
        else:
            kind = "data"
        out.append((names, ty, kind))
    return out


def analyse(path: pathlib.Path, corpus_types: set[str],
            prop_types: set[str] | None = None) -> list[dict]:
    prop_types = prop_types or set()
    src = path.read_text(errors="ignore")
    code = strip_comments(src)
    findings = []
    for m in DECL_RE.finditer(code):
        kw, name = m.group("kw"), m.group("name")
        body = _decl_body(code, m.start())
        line = code[: m.start()].count("\n") + 1

        if kw == "axiom":
            sig = body.split(":=")[0]
            binders = _binders(sig)
            # a Type-valued axiom is an opaque carrier, a different smell
            if re.search(r":\s*Type\b", sig) and not binders:
                findings.append(dict(
                    family="opaque-type-axiom", file=str(path), line=line,
                    name=name, severity="major",
                    why="`axiom X : Type` introduces an unconstrained opaque "
                        "constant; statements about it carry no content."))
                continue
            data = [b for b in binders if b[2] == "data"]
            def head(t: str) -> str:
                return t.split()[0].split(".")[-1]
            struct = [b for b in data if head(b[1]) in corpus_types
                      and head(b[1]) not in prop_types]
            # a Prop-valued corpus structure among the binders IS a hypothesis,
            # so the axiom is constrained and not of the over-wide shape.
            hypothesised = any(head(b[1]) in prop_types for b in data)
            # only INDEPENDENT DATA FAMILIES are the shape that actually bit:
            # a function or container, not a scalar index like `n : Nat`.
            families = [b for b in data if _DATAISH.search(b[1])]
            if struct and not hypothesised:
                findings.append(dict(
                    family="overclaim-structure", file=str(path), line=line,
                    name=name, severity="critical",
                    binders=[f"{n} : {t}" for n, t, _ in struct],
                    why="axiom quantified over a corpus structure. If that "
                        "structure does not carry the claim's hypotheses the "
                        "axiom is FALSE. Check: build its smallest inhabitant "
                        "and evaluate the claim."))
            elif len(families) >= 2:
                findings.append(dict(
                    family="overclaim-independent-binders", file=str(path),
                    line=line, name=name, severity="major",
                    binders=[f"{n} : {t}" for n, t, _ in families],
                    why="axiom quantified over >=2 data binders independently. "
                        "If they must be faces of one object the axiom is "
                        "FALSE. Check: instantiate them incompatibly."))
        else:
            fields = [ln.strip() for ln in body.split("\n")[1:]
                      if ln.strip() and ln.startswith((" ", "\t"))]
            typed = [f for f in fields if ":" in f]
            if not typed and "extends" not in body.split("\n")[0]:
                findings.append(dict(
                    family="empty-carrier", file=str(path), line=line,
                    name=name, severity="critical",
                    why="carrier with no fields asserts nothing; any instance "
                        "discharges it."))
            elif typed and all(
                    re.match(r"^\w+\s*:\s*(Prop|True)\s*$", f) for f in typed):
                findings.append(dict(
                    family="contentless-carrier", file=str(path), line=line,
                    name=name, severity="critical", fields=typed,
                    why="every field is a bare `Prop`/`True`, so `<True>` "
                        "inhabits the carrier and a `[C]`-conditional theorem "
                        "proves nothing modulo C."))
    return findings


def corpus_type_names(root: pathlib.Path) -> tuple[set[str], set[str]]:
    """(all corpus structure names, those that are Prop-VALUED).

    The split matters.  A binder whose type is a `Prop`-valued structure --
    `IsGrobnerShirshovBasis`, `SingleStepReduction` -- is a HYPOTHESIS: it
    constrains the other binders, which is exactly what the false axioms of
    `qou-hwax` lacked.  Counting those as data was the second-largest source of
    over-flagging in this script's first version.
    """
    names, propish = set(), set()
    for p in root.rglob("*.lean"):
        if ".lake" in p.parts:
            continue
        code = strip_comments(p.read_text(errors="ignore"))
        for m in re.finditer(
                r"^(?:structure|class)\s+([A-Za-z_][\w']*)([^\n]*)", code, re.M):
            names.add(m.group(1))
            if re.search(r":\s*Prop\b", m.group(2)):
                propish.add(m.group(1))
    return names, propish


# ------------------------------------------------------------------- self-test

FIXTURES = {
    "overclaim-structure": """
structure Shape where
  q : Real
  vals : Nat -> Real
axiom bad_bound : forall (S : Shape) (i : Nat), S.vals i <= S.q
""",
    "contentless-carrier": """
class SaysNothing where
  holds : Prop
""",
    "empty-carrier": """
class AlsoNothing : Prop
""",
    "opaque-type-axiom": """
axiom OpaqueThing : Type
""",
    # must NOT fire: the same strings inside comments
    "__negative__": """
/-- Historical note: this file once carried
```lean
class SaysNothing where
  holds : Prop
axiom bad_bound : forall (S : Shape) (i : Nat), S.vals i <= S.q
```
and both were replaced. -/
class RealCarrier where
  f : Real -> Real
  nondegenerate : exists x, f x != 0
""",
}


def selftest() -> int:
    import tempfile
    ok = True
    with tempfile.TemporaryDirectory() as td:
        d = pathlib.Path(td)
        for name, body in FIXTURES.items():
            (d / f"{name}.lean").write_text(body)
        types, props = corpus_type_names(d)
        for name, _ in FIXTURES.items():
            got = {f["family"] for f in analyse(d / f"{name}.lean", types, props)}
            if name == "__negative__":
                if got:
                    print(f"  FAIL {name}: fired on comment text -> {got}")
                    ok = False
                else:
                    print(f"  ok   {name}: correctly silent on prose")
            elif name in got:
                print(f"  ok   {name}")
            else:
                print(f"  FAIL {name}: expected {name}, got {got or 'nothing'}")
                ok = False
    print("selftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="content")
    ap.add_argument("--json")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    root = pathlib.Path(a.root)
    types, props = corpus_type_names(root)
    findings = []
    for p in sorted(root.rglob("*.lean")):
        if ".lake" in p.parts:
            continue
        findings += analyse(p, types, props)

    from collections import Counter
    by = Counter(f["family"] for f in findings)
    print(f"scanned under {root}/  --  {len(findings)} candidates\n")
    for fam, n in by.most_common():
        print(f"  {n:>4}  {fam}")
    print("\nCandidates, not verdicts. For the overclaim families the deciding")
    print("check is semantic: build the smallest inhabitant of the quantified")
    print("domain and evaluate the claim on it.")
    if a.json:
        pathlib.Path(a.json).write_text(json.dumps(
            {"schema": "lean-overclaim-audit/v1", "findings": findings}, indent=2))
        print(f"\nwrote {a.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
