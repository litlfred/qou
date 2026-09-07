#!/usr/bin/env python3
"""Find vacuous existentials: `theorem f ... : ∃ x, x = e := ⟨e, rfl⟩`.

`∃ x, x = e` is provable by `⟨e, rfl⟩` for **any** well-typed `e`. The
statement is therefore true of every term the corpus could name: it
survives replacing the definition of `e` with anything else of the same
type, so it asserts nothing about `e`. Only the *existence* of a name is
claimed, and in a total type theory that is free.

This is a third vacuity shape, disjoint from the two already covered:

  * `: True := trivial`               -- lean-vacuity-axiom-audit.ts
  * `(h : P) ... : P := h`            -- lean-self-assuming-audit.py
  * `: ∃ x, x = e := ⟨e, rfl⟩`        -- HERE

Neither existing pass sees it: the conclusion is not `True`, and the
proof term is an anonymous constructor rather than a bare hypothesis
identifier. The shape is common in this corpus where a declaration wants
to record "quantity Q is well-defined / has the displayed closed form"
and reaches for an existential instead of an equation.

The honest replacement is almost always the equation itself -- state
`realQ = e` against the independently-defined `realQ`, which is
falsifiable -- or, when no such `realQ` exists yet, a `sorry` + `-- Ref:`
(AGENTS.md honest disposition 2) or a `conjecture` demotion.

What it flags: a provable declaration whose conclusion is exactly
`∃ x (: T)?, x = RHS`, with the bound variable as the equation's LHS and
nothing else in the body.

Deliberately NOT flagged:
  * `∃ x, x = e ∧ P x` / `∨` / `→` -- the extra conjunct can carry the
    real content, so the existential is not vacuous on its face
  * `∃ x ∈ S, x = e` -- the membership constraint is a real claim
  * `∃ x, e = x` -- reversed orientation; rarer, and worth reading by
    hand rather than folding into a conservative syntactic pass
  * `∃ x y, x = e` -- more than one binder; the extra witness may matter

Output is a candidate list for agent inspection, not a verdict.
"""

import re
import sys
import json
from pathlib import Path

# theorem/lemma/def NAME <binders> : CONCLUSION := PROOF
DECL = re.compile(
    r"^(?P<kw>theorem|lemma|def|example)\s+(?P<name>[A-Za-z_][A-Za-z0-9_.']*)\s*(?P<rest>.*?)(?=^\s*(?:@\[|/--|--|theorem|lemma|def|structure|class|instance|abbrev|noncomputable|end|namespace|\Z))",
    re.S | re.M,
)

# ∃ x, x = ...   /   ∃ x : T, x = ...   /   ∃ (x : T), x = ...
#
# The bound variable is matched with `[^\W\d][\w']*`, which is UNICODE-aware
# (Python `\w` covers Unicode letters, digits and subscripts; `[^\W\d]`
# excludes a leading digit). It read `[A-Za-z_][A-Za-z0-9_']*` until 2026-09-05
# and that is ASCII-only, so **every existential bound to a Greek name was
# structurally invisible** — in a corpus that names its mathematical variables
# κ, δ, λ, τ, ρ by convention. Measured on the same tree, same day: the ASCII
# form reported `0 candidates in 0 files`, which reads as a clean bill; the
# Unicode form reports **8 in 3 files**, all bound to `κ`, `δ`, `τ_k`,
# `τ_joint`, `τ_x_k_stab`. Nothing had been drained — they had never been seen.
#
# The optional parens cover `∃ (κ : ℝ), …`. That arm has **zero measured hits**
# on this corpus (variants B and C both report 8), so it is insurance against a
# spelling, not a measured gain; it is covered by `--self-test` rather than by
# any live finding. Note the type group is `[^,)]+?` in this form so a closing
# paren cannot be swallowed into the type.
EXISTS_EQ = re.compile(
    r"^∃\s*\(?\s*(?P<var>[^\W\d][\w']*)\s*(?::\s*(?P<ty>[^,)]+?))?\s*\)?\s*,"
    r"\s*(?P=var)\s*=\s*(?P<rhs>.+)$",
    re.S,
)


def _blank(text: str) -> str:
    """Blank a comment but KEEP its newlines, so byte offsets AND line
    numbers both survive."""
    return "".join(c if c == "\n" else " " for c in text)


def strip_comments(src: str) -> str:
    src = re.sub(r"/-.*?-/", lambda m: _blank(m.group(0)), src, flags=re.S)
    src = re.sub(r"--[^\n]*", lambda m: _blank(m.group(0)), src)
    return src


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _depth_split_ok(s: str) -> bool:
    """True when `s` carries no TOP-LEVEL logical connective. A connective
    outside every bracket means the existential is one conjunct of a
    larger claim, and the extra part may be real content."""
    depth = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c in "(⟨[{":
            depth += 1
        elif c in ")⟩]}":
            depth -= 1
        elif depth == 0 and (s.startswith("∧", i) or s.startswith("∨", i)
                             or s.startswith("→", i) or s.startswith("↔", i)):
            return False
        i += 1
    return True


def strip_forall(concl: str):
    """Strip one leading `∀ <binders> ,` at depth 0, or return None.

    `∀ τ_x, ∃ y, y = τ_x * z` is the same vacuity as `∃ y, y = e`: the
    universal quantifier ranges over a statement that is true for every
    instantiation anyway. `EXISTS_EQ` is anchored at `^∃`, so this shape was
    outside it however wide the bound-variable pattern got.

    MEASURED before wiring, on 3606 files: **exactly one** instance
    (`MarkovTraceAxioms_implies_disjoint_stabilisation`), and it was already
    known — found by reading, not by scanning. So this arm buys no new
    findings today; it closes a documented blind spot so the shape cannot
    become a permanent one. Bean `qou-ekga`.

    One `∀` group only, deliberately: nested `∀ … , ∀ … , ∃ …` is not attested
    here, and each extra stripping level widens what can be mistaken for a
    binder comma."""
    s = concl.strip()
    if not s.startswith("∀"):
        return None
    depth = 0
    for i, c in enumerate(s):
        if c in "(⟨[{":
            depth += 1
        elif c in ")⟩]}":
            depth -= 1
        elif c == "," and depth == 0:
            return s[i + 1:].strip()
    return None


def split_conclusion(sig: str):
    """Return the conclusion: text after the FIRST top-level `:` in the
    signature. Binders `(h : T)` / `{x : T}` / `[C]` are always bracketed,
    so the first depth-0 colon is the signature separator. It must be the
    first, not the last: a conclusion may itself contain an unbracketed
    colon (`∃ a : ℝ, ...`), and splitting there would truncate it."""
    depth = 0
    for i, c in enumerate(sig):
        if c in "(⟨[{":
            depth += 1
        elif c in ")⟩]}":
            depth -= 1
        elif c == ":" and depth == 0:
            # skip `::` and `:=`
            if sig[i:i + 2] in (":=", "::"):
                continue
            return sig[i + 1:]
    return None


def analyze(path: Path):
    raw = path.read_text(encoding="utf-8", errors="replace")
    src = strip_comments(raw)
    out = []
    for m in DECL.finditer(src):
        body = m.group("rest")
        idx = body.rfind(":=")
        if idx < 0:
            continue
        proof = norm(body[idx + 2:])
        sig = body[:idx]
        concl = split_conclusion(sig)
        if concl is None:
            continue
        concl_n = norm(concl)
        em = EXISTS_EQ.match(concl_n)
        forall_prefixed = False
        if not em:
            inner = strip_forall(concl_n)
            if inner is None:
                continue
            em = EXISTS_EQ.match(inner)
            if not em:
                continue
            forall_prefixed = True
        rhs = em.group("rhs").strip()
        if not _depth_split_ok(rhs):
            continue
        # Is the existential discharged by handing back the RHS itself?
        # Both the term form `⟨e, rfl⟩` and the tactic form
        # `by exact ⟨e, rfl⟩` are the same vacuity; the tactic wrapper is
        # not evidence of content.
        rfl_witness = bool(
            re.fullmatch(r"(?:by\s+exact\s+)?⟨.*,\s*rfl\s*⟩", proof, re.S))
        line = src[:m.start()].count("\n") + 1
        out.append({
            "file": str(path),
            "line": line,
            "kind": m.group("kw"),
            "name": m.group("name"),
            "bound_var": em.group("var"),
            "rhs": norm(rhs)[:120],
            "proof": proof[:80],
            "rfl_witness": rfl_witness,
            "forall_prefixed": forall_prefixed,
        })
    return out


# Fixtures for `--self-test`. The point is NOT coverage for its own sake: this
# detector reported `0 candidates` for an unknown period while eight live
# instances sat in the tree, and a zero from a detector with no self-test is
# indistinguishable from a clean corpus. Each POSITIVE below is a spelling that
# the ASCII-only pattern missed; each NEGATIVE is a shape the docstring says
# must NOT be flagged, so a future widening cannot quietly swallow them.
SELF_TEST = [
    # (conclusion, should_match, why)
    ("∃ a : ℝ, a = knotFactor n b m", True, "ascii — the original shape"),
    ("∃ κ : ℝ, κ = gramKappa n qf nf cs cw", True, "greek bound var"),
    ("∃ (κ : ℝ), κ = gramKappa n qf nf cs cw", True, "greek, parenthesised"),
    ("∃ τ_k, τ_k = τ * z^k", True, "greek with ascii subscript, no type"),
    ("∃ x₀, x₀ = f y", True, "unicode subscript in the name"),
    ("∃ x, x = e ∧ P x", False, "conjunct may carry content"),
    ("∃ x, x = e → P x", False, "implication may carry content"),
    ("∃ x, e = x", False, "reversed orientation — read by hand"),
    ("∃ x y, x = e", False, "two binders; the extra witness may matter"),
    ("∃ x : ℝ, y = e", False, "equation LHS is not the bound variable"),
    ("∀ τ_x : R, ∃ τ_s : R, τ_s = τ_x * markovZax u", True,
     "∀-prefixed — same vacuity, outside the ^∃ anchor"),
    ("∀ x, ∃ y, y = e ∧ P y", False, "∀-prefixed, conjunct may carry content"),
    ("∀ x : ℝ, f x = g x", False, "∀ over a real equation — not an existential"),
]


def _flags(concl: str) -> bool:
    """Run the SAME two stages `analyze` runs. `EXISTS_EQ` alone is not the
    decision: it matches `∃ x, x = e ∧ P x` happily, and the conjunct is
    excluded downstream by `_depth_split_ok` on the RHS. A self-test that
    asserted the pipeline's behaviour while exercising only the regex FAILED
    on its own two negative fixtures when first written — recorded because it
    is the same error the fixtures exist to catch, one stage up."""
    c = norm(concl)
    m = EXISTS_EQ.match(c)
    if not m:
        inner = strip_forall(c)
        m = EXISTS_EQ.match(inner) if inner is not None else None
    return bool(m) and _depth_split_ok(m.group("rhs").strip())


def self_test() -> int:
    bad = 0
    for concl, want, why in SELF_TEST:
        got = _flags(concl)
        if got is not want:
            bad += 1
            print(f"FAIL want={want} got={got}  {concl!r}  ({why})")
    if bad:
        print(f"\nself-test: {bad} of {len(SELF_TEST)} FAILED")
        return 1
    print(f"self-test: {len(SELF_TEST)}/{len(SELF_TEST)} pass")
    return 0


def main(argv):
    if "--self-test" in argv:
        return self_test()
    roots = [Path(a) for a in argv[1:]] or [Path("content")]
    as_json = False
    if "--json" in argv:
        as_json = True
        roots = [r for r in roots if str(r) != "--json"] or [Path("content")]

    findings = []
    scanned = 0
    for root in roots:
        # A ROOT MAY BE A SINGLE FILE. `rglob` on a file path matches nothing,
        # so `<script> path/to/One.lean` printed "scanned 0 .lean files / 0
        # candidates" and exited 0 -- an absent check indistinguishable from a
        # passing one. There is also no `--diff` flag, though its absence is
        # silent: `--diff` is simply taken as a root, matches nothing, and
        # contributes 0. Both were hit for real before being fixed.
        cands = [root] if (root.is_file() and root.suffix == ".lean") \
            else sorted(root.rglob("*.lean"))
        for f in cands:
            if ".lake" in f.parts:
                continue
            scanned += 1
            findings.extend(analyze(f))

    if as_json:
        json.dump(
            {"schema": "lean-vacuous-existential/v1",
             "scanned_files": scanned,
             "count": len(findings),
             "findings": findings},
            sys.stdout, indent=2, ensure_ascii=False)
        print()
    else:
        print(f"scanned {scanned} .lean files")
        print(f"vacuous-existential candidates: {len(findings)} "
              f"in {len(set(f['file'] for f in findings))} files\n")
        for f in findings:
            flag = "rfl-witness" if f["rfl_witness"] else "other-proof"
            if f.get("forall_prefixed"):
                flag += ", ∀-prefixed"
            print(f"{f['file']}:{f['line']}  [{flag}]")
            print(f"    {f['kind']} {f['name']} : ∃ {f['bound_var']}, "
                  f"{f['bound_var']} = {f['rhs']}")
    if scanned == 0:
        print("error: scanned 0 .lean files — this is NOT a pass. Nothing was "
              "audited; check the root(s) given.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
