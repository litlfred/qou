#!/usr/bin/env python3
"""Triage the 29 q-parametric CLASSICAL [n]_q definitions by their BASIS.

Bean `qou-gl58`.  The bean asks whether each consumer of the classical bracket
(q^n-1)/(q-1) actually wants it rather than the symmetric one.  Its own
2026-09-13 append, closing a disjoint set of ten, records the discriminator
that actually worked -- and records that it was never the function NAME:

  (a) the file publishes a figure its bracket must reproduce;
  (b) the file's own internal check verifies the bracket;
  (c) the subject names a grading / Coxeter statistic that audit sec 22
      already rules classical;
  (d) the docstring declares the convention.

Only when none of (a)-(d) applies is a per-file basis determination needed.
On that sample it was needed in ZERO of ten.  This script applies (c) and (d)
mechanically -- they are the two a machine can see -- plus two of its own:

  (c') the USE SITE.  The AST shows what the bracket is built INTO, which is
       stronger than what the prose says about it: `q_int(hook_length(...))`
       in a running product IS the q-hook-length formula whether or not any
       docstring mentions one.
  (e)  FAMILY -- undeclared, but a nearby file with an identical definition
       DOES declare.  Reported separately and WEAKLY; see the long note at
       its implementation for why it is close to vacuous as mathematics and
       useful only as an authoring-hygiene queue.

It does NOT attempt (a) or (b): "publishes a figure its bracket must
reproduce" is a judgement about what a number means, and a regex that guessed
at it would manufacture verdicts.

WHAT THIS MEASURED, and it is a fact about the DETECTOR, not the corpus.  The
residue needing human reading went 20 -> 15 -> 10 -> 7 -> 0 without a single
file being read, purely by fixing four blind spots in this script:

  1. `(1 - q^n)/(1 - q)` -- the same function with both signs flipped.
  2. `1 + q + ... + q^(n-1)` -- the geometric-sum spelling.
  3. U+2212 MINUS SIGN in `q^{k-1}`, which hid the three files whose
     docstrings cite a Lean declaration -- the strongest evidence in the set.
  4. The use site, (c') above.

Four spellings of one function, and each defeated an ASCII-shaped regex.
That is this repo's recurring detector-blindness class, and the lesson for
the next auditor is the ordering: exhaust the detector before reading files.

  audit sec 22, the rule this leans on:
      T_w / Iwahori UNNORMALISED basis          -> classical is CORRECT
      normalised / quantum-dimension basis      -> symmetric is correct
  and a Poincare / Coxeter-length / major-index / content grading is the
  classical bracket by construction (its generating function IS [n]_q!).

VERDICTS

  DECLARED    the file says which bracket it uses (name or docstring).  No
              reader is misled; whether the convention is mathematically
              right for the subject is a separate question this does not
              answer, and says so.
  BASIS       the subject names a grading or Coxeter statistic that sec 22
              rules classical, OR the use site shows the bracket's role.
              Correct as written.
  FAMILY      WEAK.  The file declares nothing; a nearby file with an
              identical definition declares.  An authoring queue, not a
              determination -- never add it to DECLARED + BASIS.
  READ        none applies -- needs (a)/(b) or a human determination.

Reports the evidence STRING for every non-READ verdict, so a reader can
disagree with the classification without re-running anything.  A verdict with
no quotable evidence is the failure mode this whole bean is about.
"""

from __future__ import annotations

import ast
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# The 29, as the duplication audit classifies them.  Recomputed rather than
# hardcoded: a frozen list goes stale the moment a producer lands.
sys.path.insert(0, str(ROOT / "computations"))
sys.path.insert(0, str(ROOT / "computations" / "audits"))

import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "_dupaudit", ROOT / "computations" / "audits" / "q_integer_duplication_audit.py")
_dup = importlib.util.module_from_spec(_spec)
sys.modules["_dupaudit"] = _dup
_spec.loader.exec_module(_dup)


# (d) -- the convention is DECLARED.  Each pattern is quoted back as evidence.
DECLARE_NAME = (
    ("_geo", "name says 'geo': the geometric sum 1+q+...+q^(n-1) IS the classical bracket"),
    ("_asym", "name says 'asym': asymmetric, i.e. not the balanced bracket"),
    ("_gauss", "name says 'gauss': the Gaussian bracket IS the classical one"),
)
# BOTH ORIENTATIONS.  (q^n - 1)/(q - 1) and (1 - q^n)/(1 - q) are the SAME
# function -- numerator and denominator both negated -- and the corpus writes
# it both ways.  The first version of this script matched only the first
# spelling and reported 7 of the 9 `qlift_*` probes as unresolved when 5 of
# them declare the convention in their own function docstring.  That is the
# repo's recurring detector-blindness class in miniature ("I clustered on
# representation, not value"), and it is the reason every pattern below is
# written for an arbitrary index letter as well.
_IDX = r"[a-z]\w*"
DECLARE_DOC = (
    (rf"\(\s*q\s*(?:\*\*|\^)\s*{_IDX}\s*-\s*1\s*\)\s*/\s*\(\s*q\s*-\s*1\s*\)",
     "docstring writes the classical formula"),
    (rf"\(\s*1\s*-\s*q\s*(?:\*\*|\^)\s*{_IDX}\s*\)\s*/\s*\(\s*1\s*-\s*q\s*\)",
     "docstring writes the classical formula, sign-flipped spelling"),
    # NOTE the character class [-\u2212] on the exponent's minus.  The corpus
    # writes "q^{k\u22121}" with U+2212 MINUS SIGN, not ASCII hyphen, and an
    # ASCII-only regex silently missed three files whose docstrings name a Lean
    # declaration as the convention -- the strongest evidence in the set.
    # Fourth spelling of one function to defeat this detector; see the header.
    (rf"1\s*\+\s*q\s*\+\s*(?:\.\.\.|\u2026|\u22ef|\\cdots|\\dots)\s*\+\s*"
     rf"q\s*(?:\*\*|\^)\s*\{{?\s*{_IDX}\s*[-\u2212]\s*1",
     "docstring writes the geometric-sum spelling 1 + q + ... + q^(n-1)"),
    # A docstring that names a LEAN DECLARATION as "the corpus convention" is
    # the strongest evidence available: it cites an artifact a reviewer can
    # open, rather than asserting a convention in prose.
    (r"corpus convention,\s*(QOU\.[\w.]+)",
     "docstring cites a Lean declaration as the corpus convention"),
    (r"\bone-sided quantum integer\b",
     "docstring says 'one-sided quantum integer' (i.e. not the balanced one)"),
    (r"\bunbalanced\b", "docstring says 'unbalanced' (i.e. not the symmetric bracket)"),
    (r"\bgeometric sum\b", "docstring says 'geometric sum'"),
    (r"\bGaussian (?:bracket|binomial|integer)\b", "docstring says 'Gaussian'"),
    (r"\bNOT the balanced\b", "docstring says 'NOT the balanced'"),
    (r"\bnot the balanced\b", "docstring says 'not the balanced'"),
    (r"\bclassical (?:bracket|convention|q-integer)\b", "docstring says 'classical'"),
    (r"\bunnormalis?zed\b", "docstring says 'unnormalised'"),
)

# (c) -- the SUBJECT is a grading / Coxeter statistic that sec 22 rules
# classical.  Matched against the module docstring only, never the whole
# file: a mention of 'Poincare' inside an unrelated comment 300 lines down is
# not evidence about the bracket.
BASIS_DOC = (
    (r"\bT_w\b|\bTw(?:Basis|Mul|Gram)\b|\bIwahori\b", "T_w / Iwahori basis (sec 22: classical)"),
    (r"\bPoincar[eé]\b", "Poincare grading (its generating function IS [n]_q!)"),
    (r"\bmajor index\b|\bmaj\b", "major index -- a Coxeter-length statistic"),
    (r"\bCoxeter[- ]length\b|\bcoinvariant\b", "Coxeter-length / coinvariant grading"),
    (r"\bgraded dimension\b|\bgrading\b|\bfiltration\b", "a grading / filtration"),
    (r"\bhook[- ]length\b|\bprincipal specciali[sz]ation\b|\bprincipal speciali[sz]ation\b",
     "hook-length / principal specialisation"),
    (r"\bcontent (?:statistic|sum|average)\b|\bavg content\b",
     "the content statistic on partitions"),
)


def module_doc(path: Path) -> str:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        return ""
    return ast.get_docstring(tree) or ""


def func_doc(path: Path, fname: str) -> str:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        return ""
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == fname:
            return ast.get_docstring(node) or ""
    return ""


# (c') -- the USE SITE.  Stronger than a docstring: the AST shows what the
# bracket is actually built into.  `q_int(hook_length(...), q)` in a running
# product IS the q-hook-length formula, which is a principal specialisation
# and therefore classical by construction -- whether or not the module
# docstring happens to say "hook-length".  Found because three
# `chirality_avg_content*` files compute the identical thing and only the one
# that MENTIONED it was being classified.
USE_SITE_INNER = (
    ("hook_length", "argument is a hook length: this is the q-hook-length formula"),
    ("hook", "argument is a hook length: this is the q-hook-length formula"),
    ("content", "argument is a partition content"),
    ("maj", "argument is the major index"),
    ("inv", "argument is an inversion count"),
)


def use_site_evidence(path: Path, fname: str) -> str:
    """Evidence from how the bracket is CALLED, not from how it is described."""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        return ""
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == fname
                and node.args):
            continue
        inner = node.args[0]
        if isinstance(inner, ast.Call) and isinstance(inner.func, ast.Name):
            for frag, why in USE_SITE_INNER:
                if frag == inner.func.id or inner.func.id.startswith(frag + "_"):
                    return f"{why}  [{ast.unparse(node)}]"
    return ""


def classify(path: Path, fname: str) -> tuple[str, str]:
    """-> (verdict, evidence).  Evidence is quotable or the verdict is READ."""
    mdoc = module_doc(path)
    fdoc = func_doc(path, fname)
    doc = f"{mdoc}\n{fdoc}"

    for frag, why in DECLARE_NAME:
        if frag in fname:
            return "DECLARED", f"{why}  [name: {fname}]"

    for pat, why in DECLARE_DOC:
        mo = re.search(pat, doc, re.IGNORECASE)
        if mo:
            return "DECLARED", f"{why}  [{mo.group(0).strip()!r}]"

    for pat, why in BASIS_DOC:
        mo = re.search(pat, doc)
        if mo:
            return "BASIS", f"{why}  [{mo.group(0).strip()!r}]"

    ev = use_site_evidence(path, fname)
    if ev:
        return "BASIS", ev

    return "READ", ""


def normalised_body(path: Path, fname: str) -> str:
    """The function's source with comments, docstring and formatting removed."""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        return ""
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == fname:
            body = list(node.body)
            if (body and isinstance(body[0], ast.Expr)
                    and isinstance(body[0].value, ast.Constant)
                    and isinstance(body[0].value.value, str)):
                body = body[1:]          # drop the docstring
            return "\n".join(ast.unparse(st) for st in body)
    return ""


def main() -> int:
    cands = _dup.candidates()
    classical: list[tuple[Path, str]] = []
    for p, name, args, body in cands:
        sig = _dup.symbolic_signature(body, args)
        if sig is not None and _dup.same(sig, _dup.CLASSICAL):
            classical.append((Path(p), name))
    classical.sort(key=lambda e: (str(e[0]), e[1]))

    print(f"CLASSICAL q-parametric definitions: {len(classical)}")
    print("(recomputed from q_integer_duplication_audit, not hardcoded)\n")

    buckets: dict[str, list] = defaultdict(list)
    for p, name in classical:
        verdict, ev = classify(p, name)
        buckets[verdict].append((p, name, ev))

    # (e) -- FAMILY.  A file that does not declare, but whose definition is
    # byte-identical (after stripping docstring and formatting) to a DECLARED
    # sibling in the SAME directory, inherits that sibling's convention.
    #
    # 🛑 FAMILY IS WEAK EVIDENCE AND MUST NOT BE COUNTED WITH THE OTHER TWO.
    # Two reasons, both measured rather than felt:
    #
    #   * Body-identity is nearly VACUOUS here.  Every file in this list is
    #     already in the CLASSICAL bucket by symbolic signature, so "same
    #     body" restates how it got here.  It adds almost nothing.
    #   * The directory constraint does almost no work either:
    #     `computations/probes/` holds ~1200 files, so two probes sharing it
    #     are not siblings in any meaningful sense.
    #
    # What FAMILY genuinely IS: a list of files that do NOT declare their
    # convention, each paired with a nearby file that DOES -- i.e. an
    # actionable authoring-hygiene queue whose remedy is one docstring line
    # copied from the named sibling.  It is a statement about documentation,
    # NOT a determination that the bracket is right for the subject.
    #
    # A reader of one of these files alone is still not told which bracket it
    # uses.  Report FAMILY separately from DECLARED + BASIS, always.
    declared_bodies: dict[tuple[str, str], Path] = {}
    for verdict in ("DECLARED", "BASIS"):
        for p, name, _ev in buckets[verdict]:
            body = normalised_body(p, name)
            if body:
                declared_bodies.setdefault((str(p.parent), body), p)

    still_read = []
    for p, name, _ev in buckets["READ"]:
        body = normalised_body(p, name)
        sib = declared_bodies.get((str(p.parent), body)) if body else None
        if sib is not None:
            rel = sib.relative_to(ROOT) if sib.is_absolute() else sib
            buckets["FAMILY"].append(
                (p, name, f"identical definition to a declaring sibling: {rel}"))
        else:
            still_read.append((p, name, _ev))
    buckets["READ"] = still_read

    for verdict in ("DECLARED", "BASIS", "FAMILY", "READ"):
        rows = buckets[verdict]
        print("=" * 78)
        print(f"{verdict}: {len(rows)}")
        print("=" * 78)
        for p, name, ev in rows:
            rel = p.relative_to(ROOT) if p.is_absolute() else p
            print(f"  {rel}::{name}")
            if ev:
                print(f"      {ev}")
        print()

    n_read = len(buckets["READ"])
    n_fam = len(buckets["FAMILY"])
    print("-" * 78)
    strong = len(classical) - n_read - n_fam
    print(f"STRONG (DECLARED+BASIS) : {strong} / {len(classical)}")
    print(f"WEAK   (FAMILY)         : {n_fam}   <- an authoring-hygiene queue,")
    print("                             NOT a determination.  The file itself")
    print("                             still does not say which bracket it uses;")
    print("                             a nearby file with the same body does.")
    print(f"needs reading (a)/(b)   : {n_read}")
    print()
    print("A DECLARED verdict says the file is HONEST about its bracket, not")
    print("that the bracket is mathematically right for its subject.  Those are")
    print("different claims and this script only makes the first.")
    print()
    print("Do NOT quote a single combined figure.  'STRONG + WEAK' would read as")
    print(f"{len(classical)}/{len(classical)} resolved, and 7 of those are files that say nothing at all.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
