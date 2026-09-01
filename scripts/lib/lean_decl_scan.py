"""Shared text-level scanning primitives for the Lean vacuity detectors.

Two detectors key on different signals but need the same substrate:

    scripts/lean-definition-collapsed-audit.py   docstring-says-OPEN
                                                 + proof-is-definitional
    scripts/lean-borrowed-name-audit.py          a name invoking a
                                                 MATHEMATICIAN + local-only
                                                 defs + cheap proof

Their populations barely overlap -- measured 2026-08-27, 0 of 19 CRITICAL and
21 of 115 major in common -- so the FRONT-ENDS stay separate.  What was written
twice, independently and identically, is everything below.  Beans `qou-rfq9`
(this module), `qou-k9yt` (the first detector), `qou-0avp` (the second).

Where the two implementations differed, this module takes the stronger one and
says so at the call site.  The differences were not cosmetic:

  * `blank_comments` existed only in borrowed-name.  Without it a `rfl` or a
    def name appearing inside a `--` comment is parsed as code.  Real instance:
    `unit2_nf_hecke_reduction` carries two comment lines between its name and
    its statement.
  * `binder_names` was broader in borrowed-name.  The other matched only
    `[`/`(` with a single identifier, so it missed implicit binders
    (`{R : Type*}`) and multi-name groups (`(a b : R)`) -- and the binder set
    feeds the exclusion that suppresses false positives, so a miss there
    REPORTS A FINDING THAT SHOULD HAVE BEEN SKIPPED.

Both detectors' outputs are published (PR #5875, and the vacuity review ledger
keys verdicts by declaration), so any behaviour change here moves numbers a
reader may already have quoted.  Every delta from adopting this module is
measured and recorded in `scripts/lib/lean_decl_scan_delta.md`; do not change a
primitive without re-measuring.
"""

from __future__ import annotations

import re

__all__ = [
    "blank_comments", "split_statement", "decl_spans", "docstring_before",
    "binder_names", "local_def_names", "discharges_via_binder_field",
    "line_comments_before", "line_comments_inside", "comment_cone",
    "DECL", "PLAIN_DEF",
]

# Declaration heads.  `example` has no name; the front-ends that care about it
# handle the empty-name case.
DECL = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+|"
    r"partial\s+|unsafe\s+)*"
    r"(theorem|lemma|example|def|abbrev|instance|structure|class|opaque|axiom)"
    r"\s+([A-Za-z_][A-Za-z0-9_'.]*)?")

# `def`/`abbrev` only -- NOT `opaque`/`axiom`, which are honest primitives and
# whose presence in a proof is not a collapse.  (definition-collapsed's rule,
# and it is the right one.)
PLAIN_DEF = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*"
    r"(?:def|abbrev)\s+([A-Za-z_][A-Za-z0-9_'.]*)")


def blank_comments(src: str) -> str:
    """Blank `--` comments and `/- -/` blocks, PRESERVING every newline.

    Line-preservation is load-bearing: declaration line numbers index back into
    the ORIGINAL source to find docstrings, so a stripper that deletes lines
    silently mis-aligns every docstring lookup.  That bug happened once and a
    selftest caught it.  Blanking also stops a `theorem ...` line quoted inside
    a docstring from being parsed as a declaration.
    """
    out, i, n, depth = [], 0, len(src), 0
    while i < n:
        c = src[i]
        if depth == 0 and src.startswith("--", i):
            j = src.find("\n", i)
            j = n if j < 0 else j
            out.append(" " * (j - i))
            i = j
        elif src.startswith("/-", i):
            depth += 1
            out.append("  ")
            i += 2
        elif depth and src.startswith("-/", i):
            depth -= 1
            out.append("  ")
            i += 2
        else:
            out.append(c if (not depth or c == "\n") else " ")
            i += 1
    return "".join(out)


def split_statement(chunk: str) -> tuple[str, str]:
    """Split a decl at its top-level `:=`.  Returns (statement, proof).

    Bracket-aware, so a `:=` inside a structure literal or a `let` does not
    split early.  A naive `chunk.split(":=", 1)` gets this wrong on any decl
    whose STATEMENT contains one -- e.g. a structure-literal argument.
    """
    depth, i, n = 0, 0, len(chunk)
    while i < n:
        c = chunk[i]
        if c in "([{⟨⦃":
            depth += 1
        elif c in ")]}⟩⦄":
            depth -= 1
        elif depth <= 0 and chunk.startswith(":=", i):
            return chunk[:i], chunk[i + 2:]
        i += 1
    return chunk, ""


# Column-0 keywords that close a declaration without starting one.
#
# `omit` earns its place the hard way: `omit [Inst] in` is Lean 4's per-decl
# instance suppression and sits at column 0 immediately BEFORE the declaration
# it modifies, so leaving it out extends the PRECEDING decl's body across it.
# Measured: without `omit` here, `conjOp_apply` and `gram_apply` -- both bare
# `:= rfl` -- read as `rfl\n\nomit [...] in` and stopped being flagged.
# Any column-0 `<keyword> ... in` modifier behaves the same way, hence the
# second alternative.
STRUCTURAL = re.compile(
    r"^(?:end|namespace|section|open|variable|variables|import|attribute|"
    r"omit|include|macro|notation|syntax|set_option|deriving|local|@\[)\b"
    r"|^\S.*\bin\s*$")


def decl_spans(src: str):
    """Yield (kind, name, header_line_no_1based, body_text) per top-level decl.

    A body ends at whichever comes first: the next declaration head, or a
    column-0 line that closes the current one.  BOTH bounds are needed and
    getting it wrong is silent:

      * next-decl-head alone swallows `end Foo` / `namespace` into the proof,
        so `:= rfl` reads as `rfl\\n\\nend Foo` and every downstream
        `proof == "rfl"` test fails.  Measured cost when this module first
        shipped without the second bound: 163 findings vanished from the
        definition-collapsed advisory tier, one of them `degree_conj`, whose
        proof is a bare `rfl` two lines above `end ChordDiagram`.
      * column-0 alone truncates a proof whose tactic block is unindented.

    Comments are expected to be blanked first, which is why a `/-! ... -/`
    section marker does not end a body here -- it is already whitespace.
    """
    lines = src.split("\n")
    hits = []
    for idx, ln in enumerate(lines):
        m = DECL.match(ln)
        if m:
            hits.append((idx, m.group(1), m.group(2) or ""))
    for k, (idx, kind, name) in enumerate(hits):
        limit = hits[k + 1][0] if k + 1 < len(hits) else len(lines)
        end = limit
        for j in range(idx + 1, limit):
            ln = lines[j]
            if ln[:1].strip() and not ln.startswith(")") and STRUCTURAL.match(ln):
                end = j
                break
        yield kind, name, idx + 1, "\n".join(lines[idx:end])


def docstring_before(lines: list[str], line_no: int) -> str:
    """The `/-- ... -/` (or `/-! ... -/`) block immediately above `line_no`.

    `line_no` is 1-based, matching `decl_spans`.  Intervening `-- Ref:` lines
    and blank lines are skipped, so a citation between the docstring and the
    declaration does not hide the docstring.
    """
    j = line_no - 2
    while j >= 0 and (lines[j].lstrip().startswith("--") or not lines[j].strip()):
        j -= 1
    if j < 0 or not lines[j].rstrip().endswith("-/"):
        return ""
    k = j
    while k >= 0 and not (lines[k].lstrip().startswith("/--")
                          or lines[k].lstrip().startswith("/-!")):
        k -= 1
    return "\n".join(lines[max(k, 0):j + 1]) if k >= 0 else ""


# `(x y : T)`, `{x : T}`, `[inst : C]`, `⦃x : T⦄` -- all four forms, and
# multi-name groups.  The narrower `[({]\s*(ident)\s*:` misses `{R : Type*}`
# and `(a b : R)`.
BINDER = re.compile(r"([({⦃\[])\s*([^:()\[\]{}]*?)\s*:\s*([^)\]}⦄]*)")

# A binder TYPE that states an assumption rather than introducing a value.
PROP_ISH = re.compile(r"[=≠<≤>≥∈∉∣∀∃∧∨¬]|→|\bNe\b|\bNonempty\b")


def binder_specs(stmt: str) -> list[tuple[str, str, str]]:
    """(name, bracket, type_text) for every name bound by the declaration."""
    out: list[tuple[str, str, str]] = []
    for m in BINDER.finditer(stmt):
        bracket, names, ty = m.group(1), m.group(2), m.group(3)
        for tok in names.split():
            if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_']*", tok):
                out.append((tok, bracket, ty))
    return out


def binder_names(stmt: str) -> set[str]:
    """Every name bound by the declaration's binder groups."""
    return {n for n, _, _ in binder_specs(stmt)}


def assumption_binders(stmt: str) -> set[str]:
    """Binders that state an ASSUMPTION, as opposed to introducing a value.

    Three kinds qualify: an instance binder `[Field R]` / `[C M]`, a binder
    whose type is Prop-ish (`(hA : A < 4)`, `(h : x ∈ s)`), and the `h`-prefixed
    naming convention this corpus uses consistently for hypotheses.

    The distinction is load-bearing for `discharges_via_binder_field`, which
    looks for `binder.field` in the proof.  Feeding it EVERY binder makes it
    fire on ordinary dot-notation over a value -- `A.choose` where `A : ℕ`,
    `l.length`, `n.succ` -- which is not a field projection of an assumption at
    all.  Measured instance: `mu4_unconstrained_below_four` has `{A : ℕ}` and a
    proof using `A.choose 4`; with every binder in scope the exclusion
    suppressed it, which was the right outcome for the wrong reason (its real
    hypothesis `hA : A < 4` IS used) and would have over-suppressed elsewhere.
    """
    out: set[str] = set()
    for name, bracket, ty in binder_specs(stmt):
        if bracket == "[" or PROP_ISH.search(ty) or re.match(r"h[A-Z_']|^h$|^h\d", name):
            out.add(name)
    return out


def local_def_names(src_blanked: str) -> set[str]:
    """Last components of every `def`/`abbrev` name declared in this file."""
    out: set[str] = set()
    for ln in src_blanked.split("\n"):
        m = PLAIN_DEF.match(ln)
        if m:
            out.add(m.group(1).split(".")[-1])
    return out


def discharges_via_binder_field(proof: str, binders: set[str]) -> bool:
    """True when the proof projects a FIELD out of a binder (`C.rule`, `h.foo`).

    That is a genuine conditional derivation -- the goal is discharged from a
    STATED assumption, not by unfolding a local definition -- so both detectors
    skip it.  Worked case: `BraneTowerLevelAmplitude.fullCoordAmplitude_eq`,
    whose docstring correctly disclaims ("not a proof of the rule; the rule
    `ruleLinear` is the open input") and whose disclaimer was itself tripping
    the open-claim signal into a false CRITICAL.
    """
    return any(re.search(rf"\b{re.escape(b)}\.[A-Za-z_]", proof) for b in binders)


def line_comments_before(lines: list[str], line_no: int) -> str:
    """The contiguous `--` comment block immediately above `line_no`.

    `docstring_before` deliberately *skips* `--` lines while walking up, so
    that a `-- Ref:` citation sitting between a docstring and its declaration
    does not hide the docstring.  The cost of that skip is that prose written
    in `--` comments -- which in this corpus is where the honest admissions
    tend to live -- is invisible to every caller of `docstring_before`.

    Worked case (`qou-rfq9`): `b3_nf_wedderburn_uniqueness` carries a docstring
    ending "the NF coefficients are PROVED CORRECT", and immediately below it,
    in `--` comments, "The formal proof needs: Wedderburn for finite-dim
    algebras (Mathlib)".  Only the first is read.

    Blank lines are skipped between comment lines but the walk stops at the
    first non-blank, non-`--` line, so this never reaches over a declaration.
    """
    j = line_no - 2
    out: list[str] = []
    while j >= 0:
        s = lines[j].lstrip()
        if s.startswith("--"):
            out.append(lines[j])
            j -= 1
        elif not lines[j].strip():
            j -= 1
        else:
            break
    return "\n".join(reversed(out))


def line_comments_inside(lines: list[str], line_no: int, span_lines: int) -> str:
    """`--` comments occurring INSIDE a declaration's own source span.

    `blank_comments` runs before parsing, so by the time a detector sees a
    statement every inline comment in it is whitespace.  This reads them back
    out of the raw lines.

    This is not a stylistic nicety: in the worked case the admission
    "Full proof requires Wedderburn-Artin over R_q" sits between the theorem
    name and the proposition it is introducing -- i.e. inside the statement,
    where nothing else looks.
    """
    out = [ln for ln in lines[line_no - 1: line_no - 1 + span_lines]
           if ln.lstrip().startswith("--")]
    return "\n".join(out)


def comment_cone(lines: list[str], line_no: int, span_lines: int) -> str:
    """All authored prose attached to one declaration.

    docstring above + `--` block above + `--` comments inside the span.
    Detectors that ask "does the author's own prose admit this is open?"
    should read this, not `docstring_before` alone.
    """
    return "\n".join(x for x in (
        docstring_before(lines, line_no),
        line_comments_before(lines, line_no),
        line_comments_inside(lines, line_no, span_lines),
    ) if x)
