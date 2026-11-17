#!/usr/bin/env python3
r"""Find self-assuming projections: `theorem f (h : P) ... : P := h`.

The triviality probe (folio-assistant lean-triviality-probe.ts) surfaces
these, but costs a `lean` elaboration per declaration (~11 min / 40
blocks). The shape is syntactic, so a static pass covers the whole corpus
in seconds and is the cheap pre-filter.

What it flags: a provable declaration whose entire proof term is a bare
identifier that names one of its own explicit hypotheses, AND whose
conclusion is syntactically the same as that hypothesis's type. That is
`P -> P` proved by `id` -- it asserts nothing about the objects involved.

It also flags the CONJUNCTIVE form of the same defect: a conclusion that
is literally `T1 /\ T2 /\ ... /\ Tn`, proved by the anonymous constructor
`<f1, f2, ..., fn>` whose components project fields of one binder whose
declared types are exactly `T1..Tn`. Nothing is derived -- the tuple only
re-bundles hypotheses the carrier already asserts.

Deliberately NOT flagged:
  * proofs with a tactic block (`:= by ...`) -- a `by exact h` may still
    be vacuous but needs elaboration to judge; out of scope here
  * `h.1`, `h.symm`, `f h` -- projections/applications do real work
  * conclusion differing from the hypothesis type in any way -- even a
    reassociation is content
  * an `Iff` conclusion proved by `<ctx.forward, ctx.backward>`. This is
    the SANCTIONED §3b-cond pattern and AGENTS.md names
    `QOU/FluidDynamics/q_bkm_criterion.lean` as its verified exemplar:
    `A <-> B` is not the conjunction of the two hypothesis types, so
    `Iff.intro` is a composition step and the theorem derives its
    conclusion. Structurally excluded -- a top-level `<->` (or `->`, or a
    leading binder) means the conclusion is not a conjunction at all, so
    the component counts cannot agree.
  * a STRUCTURE-INSTANCE constructor whose conclusion is `S a b c` rather
    than a conjunction. `QOU.Knot.M004AngleStructure.Positive.sigma` proves
    `Positive g1 b1 a1 a2 g2 b2` by `<h.hg1, h.hb1, h.ha1, h.ha2, h.hg2,
    h.hb2>`, which PERMUTES its components -- that is content, not
    re-bundling. Same exclusion mechanism: `S a b c` has no top-level `/\`,
    so no component count can agree.

Output is a candidate list for agent inspection, not a verdict.
"""

import re
import sys
import json
from pathlib import Path

# theorem/lemma NAME <binders> : CONCLUSION := PROOF
DECL = re.compile(
    r"^(?P<kw>theorem|lemma)\s+(?P<name>[A-Za-z_][A-Za-z0-9_.']*)\s*(?P<rest>.*?)(?=^\s*(?:@\[|/--|--|theorem|lemma|def|structure|class|instance|abbrev|noncomputable|end|namespace|\Z))",
    re.S | re.M,
)
# (name : type) explicit binder
BINDER = re.compile(r"\((?P<names>[^():]+?)\s*:\s*(?P<type>(?:[^()]|\([^()]*\))*)\)")
# [name : type] instance-implicit and {name : type} implicit binders.
# Matching ONLY round brackets is what made this detector blind to the
# class-instance self-assuming variant that AGENTS.md §3b-cond rule 5 names:
# an `[ctx : C]` binder never entered the binder map at all (bean qou-24m2).
BINDER_INST = re.compile(
    r"\[(?P<names>[^\[\]:]+?)\s*:\s*(?P<type>(?:[^\[\]]|\[[^\[\]]*\])*)\]"
)
# Anonymous instance-implicit binder `[HasClaim X]` (no `:`). With no binder
# name, Lean projects fields through the class name (`HasClaim.claim`), so
# keying the binder map by the head class identifier lets Rule 2 (`qou-1ccx`)
# resolve `binders.get("HasClaim")` identically to `[ctx : HasClaim X]`.
BINDER_INST_ANON = re.compile(
    r"\[(?P<type>[^\[\]:]+?)\]"
)
BINDER_IMPL = re.compile(
    r"\{(?P<names>[^{}:]+?)\s*:\s*(?P<type>(?:[^{}]|\{[^{}]*\})*)\}"
)
# `class C ... where` / `structure S ... where` + its indented field block.
#
# Matching `class` alone was NECESSARY but NOT SUFFICIENT to see the
# structure-valued variant: widening this regex on its own moved the corpus
# count 13 -> 13, because the comparison below then still failed on sibling
# qualification.  Both changes are required; either alone reports nothing.
CLASS_DECL = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?(?:class|structure)\s+(?P<name>[A-Za-z_][A-Za-z0-9_.']*)"
    # `params` may span LINES: a structure often carries its typeclass binders
    # over several.  It was `[^\n]*?` — single-line — so a declaration whose
    # `where` sat on line 4 never matched at all, and its fields were absent
    # from the map.  That was the THIRD independent reason the motivating case
    # went undetected, after `class`-only matching and sibling qualification.
    # Bounded to 6 lines and forbidden from crossing a blank line so it cannot
    # run away into the next declaration.
    r"(?P<params>(?:[^\n]*\n(?=[ \t]*\S)){0,6}[^\n]*?)\bwhere\b"
    r"(?P<body>(?:\n(?:[ \t]+[^\n]*|[ \t]*))*)",
    re.M,
)
# Lean identifiers are UNICODE: this corpus names structure fields `hγ₁`,
# `hα₂`, `h_ΔE_exp`.  An ASCII-only `[A-Za-z_][A-Za-z0-9_']*` silently drops
# every one of them from the field map -- taxonomy row 35, the identifier's
# alphabet, in a detector whose whole job is to compare against field types.
# `\w` is Unicode-aware for `str` patterns in Python and matches Greek letters
# and the subscript digits `₀-₉` (they are `isdigit()`), so `[^\W\d][\w'!?]*`
# is the right class: a leading non-digit word character, then word characters,
# primes, and Lean's `!`/`?` suffixes.
IDENT = r"[^\W\d][\w'!?]*"
CLASS_FIELD = re.compile(
    rf"^[ \t]+(?P<field>{IDENT})\s*:\s*(?P<type>.+)$"
)
# A component of an anonymous constructor: `binder.field`, EXACTLY one dot and
# no arguments.  An applied component (`ctx.field s t`) has type `P s t`, which
# cannot equal a conjunct written without the application, so allowing args
# would only widen the surface without ever matching -- see the audit doc.
TUPLE_COMPONENT = re.compile(rf"^(?P<binder>{IDENT})\.(?P<field>{IDENT})$")
# `ctx.claim n ps hc hn` — a projection APPLICATION. The old bare-identifier
# guard rejected these outright, which was the second independent cause of the
# blindness: even with the binder parsed, the proof term never matched.
PROJ_APP = re.compile(
    r"^(?P<binder>[A-Za-z_][A-Za-z0-9_']*)\.(?P<field>[A-Za-z_][A-Za-z0-9_']*)"
    r"(?P<args>\s.*)?$",
    re.S,
)


def parse_classes(src: str) -> dict[str, dict[str, str]]:
    """Map `class name -> {field: declared type}` for classes declared in this
    file.  Cross-file classes are NOT resolved — see the module docstring note."""
    classes: dict[str, dict[str, str]] = {}
    for m in CLASS_DECL.finditer(src):
        fields: dict[str, str] = {}
        cur = None
        for line in m.group("body").split("\n"):
            if not line.strip():
                continue
            fm = CLASS_FIELD.match(line)
            if fm:
                cur = fm.group("field")
                fields[cur] = fm.group("type").strip()
            elif cur and line[:1] in (" ", "\t"):
                fields[cur] = fields[cur] + " " + line.strip()
            else:
                break
        classes[m.group("name")] = fields
    return classes


def _blank(text: str) -> str:
    """Blank a comment but KEEP its newlines, so byte offsets AND line
    numbers both survive. Replacing '\\n' with ' ' preserves offsets but
    silently shifts every reported line number after the first block
    comment."""
    return "".join(c if c == "\n" else " " for c in text)


def strip_comments(src: str) -> str:
    src = re.sub(r"/-.*?-/", lambda m: _blank(m.group(0)), src, flags=re.S)
    src = re.sub(r"--[^\n]*", lambda m: _blank(m.group(0)), src)
    return src


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


# --- conjunctive-projection helpers (rule 3) ---------------------------------
#
# Every bracket family Lean uses as a delimiter.  `⟨⟩` MUST be in here: the
# whole point of rule 3 is that the proof term is an anonymous constructor, and
# a splitter that does not track it splits `⟨a, ⟨b, c⟩⟩` in the wrong places.
_OPEN, _CLOSE = "([{⟨⦃", ")]}⟩⦄"
_QUANT = "∀∃"


def _match_bracket(s: str, i: int) -> int:
    """Index of the bracket closing the one at `s[i]`, or -1."""
    depth = 0
    for j in range(i, len(s)):
        if s[j] in _OPEN:
            depth += 1
        elif s[j] in _CLOSE:
            depth -= 1
            if depth == 0:
                return j
    return -1


def _depth_split(text: str, seps: tuple[str, ...]) -> list[str]:
    """Split `text` at TOP-LEVEL occurrences of any separator in `seps`."""
    parts: list[str] = []
    depth = start = i = 0
    while i < len(text):
        ch = text[i]
        if ch in _OPEN:
            depth += 1
            i += 1
            continue
        if ch in _CLOSE:
            depth -= 1
            i += 1
            continue
        if depth == 0:
            hit = next((s for s in seps if text.startswith(s, i)), None)
            if hit is not None:
                parts.append(text[start:i])
                i += len(hit)
                start = i
                continue
        i += 1
    parts.append(text[start:])
    return [p.strip() for p in parts]


def _has_top_level(text: str, seps: tuple[str, ...]) -> bool:
    return len(_depth_split(text, seps)) > 1


def strip_outer_parens(s: str) -> str:
    s = s.strip()
    while s.startswith("(") and _match_bracket(s, 0) == len(s) - 1:
        s = s[1:-1].strip()
    return s


# A lambda's domain ascription (`fun j : Fin n => …`) is the same kind of
# inferable annotation as a quantifier's, and is stripped for the same reason.
# Measured over `content/` (3852 `.lean`) 2026-09-14: OFF -> 6 conjunctive
# candidates, ON -> 7.  The extra one is `lp_dual_stability`, a 4-way re-bundle
# whose carrier writes `fun j => G i j * x_star j` and whose conclusion writes
# `fun j : Fin ctx.channels => ctx.G i j * ctx.x_star j`.  Flipping this to
# False is the way to re-measure that.
STRIP_LAMBDA_ASCRIPTIONS = True


def _scan_binder_group(s: str, i: int, term: str) -> tuple[list[str], int]:
    """Read binder groups from `s[i]` up to and including `term`.

    Returns the bound NAMES and the index just past `term`. Handles
    `(x y : T)`, `{x : T}`, `x : T` and a bare `x`, in any mixture."""
    names: list[str] = []
    n = len(s)
    while i < n:
        while i < n and s[i].isspace():
            i += 1
        if i >= n or s.startswith(term, i):
            i = i + len(term) if i < n else i
            break
        if s[i] in "({[":
            j = _match_bracket(s, i)
            if j < 0:
                break
            inner = s[i + 1 : j]
            head = _depth_split(inner, (":",))
            names.append(head[0] if len(head) > 1 else inner.strip())
            i = j + 1
            continue
        start = i
        while i < n and s[i] not in ":({[" and not s.startswith(term, i):
            i += 1
        names.append(s[start:i].strip())
        if i < n and s[i] == ":":
            depth = 0
            i += 1
            while i < n:
                if s[i] in _OPEN:
                    depth += 1
                elif s[i] in _CLOSE:
                    depth -= 1
                elif depth == 0 and s.startswith(term, i):
                    break
                i += 1
            i = min(i + len(term), n)
            break
    return [x for x in names if x], i


def _binder_head(s: str, i: int) -> tuple[str, str, int] | None:
    """`(rendered-keyword, terminator, index-after-keyword)` at `s[i]`."""
    ch = s[i]
    if ch in _QUANT:
        return ch, ",", i + 1
    if not STRIP_LAMBDA_ASCRIPTIONS:
        return None
    if ch == "λ":
        return "fun", "=>", i + 1
    if s.startswith("fun", i):
        before_ok = i == 0 or not (s[i - 1].isalnum() or s[i - 1] in "_'")
        after = s[i + 3 : i + 4]
        if before_ok and not (after.isalnum() or after in ("_", "'")):
            return "fun", "=>", i + 3
    return None


def strip_binder_types(s: str) -> str:
    """`∀ (x : T), P` -> `∀ x, P`; `fun j : U => e` -> `fun j => e`.

    A field type is written INSIDE the carrier, where the binder's type is
    spelled out; the conclusion is written at the USE SITE, where Lean infers
    it and the author omits it.  `JetHorizon.degree_zero_vanishes` declares
    `∀ (s : algebra.sections 0), s = algebra.zero 0` and `qou_is_ccc`'s
    conjunct is `∀ s, s = H.algebra.zero 0` -- the SAME proposition, differing
    only by an inferable annotation.  Comparing raw text can never see that.

    This is the one deliberately tolerant step, and it is narrow: it drops a
    binder's type ascription and nothing else.  Two propositions it equates
    differ ONLY in an ascription the elaborator supplies, so if the file
    compiles they are the same proposition -- the tolerance cannot manufacture
    an agreement that Lean does not already have.

    Measured, `content/` 2026-09-14, conjunctive candidates by tolerance tier:
    literal text 1; + outer-paren strip 4; + quantifier ascription 6;
    + lambda ascription 7.  So each tier is load-bearing rather than
    defensive, and NONE of them is doing most of the work on its own."""
    out: list[str] = []
    i = 0
    while i < len(s):
        head = _binder_head(s, i)
        if head is None:
            out.append(s[i])
            i += 1
            continue
        kw, term, i = head
        names, i = _scan_binder_group(s, i, term)
        joiner = " => " if term == "=>" else ", "
        out.append(kw + " " + " ".join(names) + joiner)
    return norm("".join(out))


def tuple_components(proof: str) -> list[str] | None:
    """Components of an anonymous constructor that is the WHOLE proof term."""
    t = proof.strip()
    if not t.startswith("⟨") or not t.endswith("⟩"):
        return None
    # `⟨a, b⟩.1` and `⟨a⟩ ⟨b⟩` both start `⟨` and end `⟩` and are not this.
    if _match_bracket(t, 0) != len(t) - 1:
        return None
    return _depth_split(t[1:-1], (",",))


def _flatten_right(parts: list[str], expand) -> list[str]:
    """Splice the RIGHT spine.  Lean's anonymous constructor is right-nested,
    so `⟨a, ⟨b, c⟩⟩ : A ∧ (B ∧ C)` is the same term as `⟨a, b, c⟩ : A ∧ B ∧ C`.
    Only the right spine is spliced: `⟨⟨a, b⟩, c⟩ : (A ∧ B) ∧ C` is a DIFFERENT
    association and flattening it would compare mismatched shapes."""
    out = list(parts)
    while True:
        sub = expand(out[-1])
        if sub is None or len(sub) < 2:
            return out
        out = out[:-1] + sub


def conjuncts(conclusion: str) -> list[str] | None:
    """Top-level conjuncts of `conclusion`, or None if it is not a conjunction.

    The guards are what keep the SANCTIONED §3b-cond pattern out. `↔` and `→`
    bind looser than `∧` in Lean, so a top-level one means the conclusion is an
    iff or an implication -- `A ↔ B ∧ C` is `A ↔ (B ∧ C)`, and splitting it on
    `∧` would invent a conjunction that is not there. A top-level comma means a
    quantifier body (`∀ x, P x ∧ Q x`), same hazard. `q_bkm_criterion`'s
    `ctx.extendsSmoothly ↔ ctx.vorticityIntegralFinite` is excluded here, by
    structure rather than by a name list."""
    c = conclusion.strip()
    if not c:
        return None
    if _has_top_level(c, ("↔", "<->", "→", "->", ",")):
        return None
    parts = _depth_split(c, ("∧", "/\\"))
    if len(parts) < 2 or any(not p for p in parts):
        return None
    return parts


def _expand_conjunct(part: str) -> list[str] | None:
    inner = strip_outer_parens(part)
    sub = conjuncts(inner)
    return sub


def _qualify(ftype: str, bname: str, siblings: dict[str, str], fname: str) -> str:
    """Prefix sibling-field mentions with the binder, as the USE SITE writes
    them.  `JetHorizon.degree_zero_vanishes` says `algebra.zero 0`; the theorem
    says `H.algebra.zero 0`.  Same rewrite the rule-2 comparison already does."""
    q = norm(ftype)
    for sib in siblings:
        if sib == fname:
            continue
        q = re.sub(rf"(?<![.\w]){re.escape(sib)}\b", f"{bname}.{sib}", q)
    return q


def _same_prop(a: str, b: str) -> bool:
    """Tolerant only in the two ways the two spellings LEGITIMATELY differ:
    outer parentheses (a conjunct is parenthesised, a field type is not) and an
    inferable binder ascription.  Measured both ways -- with the ascription
    strip disabled, `qou_is_ccc` and `ccc_boundary_data_exists` are missed and
    the corpus count is 0, so it is load-bearing rather than defensive."""
    a, b = norm(strip_outer_parens(a)), norm(strip_outer_parens(b))
    if a == b:
        return True
    return strip_binder_types(a) == strip_binder_types(b)


def analyze_text(raw: str, file_str: str = "<mem>"):
    src = strip_comments(raw)
    classes = parse_classes(src)
    out = []
    for m in DECL.finditer(src):
        body = m.group("rest")
        # split at the LAST top-level `:=` (depth == 0) that starts the proof
        # term, so named arguments like `(vd := vd)` inside the proof term do
        # not steal the split (`GaugeTheory.variational_transport`).
        idx = -1
        d_eq = 0
        for i_eq, ch_eq in enumerate(body):
            if ch_eq in _OPEN:
                d_eq += 1
            elif ch_eq in _CLOSE:
                d_eq = max(0, d_eq - 1)
            elif d_eq == 0 and body.startswith(":=", i_eq):
                idx = i_eq
        if idx < 0:
            continue
        proof = norm(body[idx + 2 :])
        # A bare identifier is rule 1; a projection application is rule 2; an
        # anonymous constructor is rule 3.  Anything else (tactic block, real
        # term) is not a candidate.
        #
        # This gate used to `continue` on anything `PROJ_APP` did not match,
        # and `⟨` matches no rule-1/rule-2 pattern, so the ENTIRE conjunctive
        # class exited here -- before any conclusion was even parsed.
        is_bare = bool(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_']*", proof))
        proj = None if is_bare else PROJ_APP.match(proof)
        tup = None if (is_bare or proj is not None) else tuple_components(proof)
        if not is_bare and proj is None and tup is None:
            continue
        sig = body[:idx]
        # conclusion = text after the FIRST top-level `:` outside binders.
        #
        # This used to take the LAST such colon, which silently mis-parses any
        # conclusion containing a binder of its own: in
        #   theorem t (n : Nat) [ctx : C n] : ∀ ps : List Nat, P ps
        # every binder colon is inside brackets (depth > 0), so the only
        # top-level colons are the conclusion separator and the one in
        # `∀ ps : List Nat`.  Taking the last one made the "conclusion"
        # `List Nat, P ps` and no comparison could ever match.  Taking the
        # first is correct for both rules, since binder colons are bracketed.
        depth = 0
        concl_at = -1
        for i, ch in enumerate(sig):
            if ch in "([{":
                depth += 1
            elif ch in ")]}":
                depth -= 1
            elif ch == ":" and depth == 0:
                if i + 1 < len(sig) and sig[i + 1] == "=":
                    continue
                concl_at = i
                break
        if concl_at < 0:
            continue
        conclusion = norm(sig[concl_at + 1 :])
        binders = {}
        for rx in (BINDER, BINDER_INST, BINDER_IMPL):
            for b in rx.finditer(sig[:concl_at]):
                for nm in b.group("names").split():
                    binders[nm] = norm(b.group("type"))
        for b in BINDER_INST_ANON.finditer(sig[:concl_at]):
            t_anon = norm(b.group("type"))
            if t_anon:
                cname = t_anon.split()[0].lstrip("@")
                if cname in classes:
                    binders.setdefault(cname, t_anon)

        def _hit(hypothesis: str, variant: str, **extra) -> None:
            out.append(
                {
                    "decl": m.group("name"),
                    "kind": m.group("kw"),
                    "hypothesis": hypothesis,
                    "statement": conclusion,
                    "variant": variant,
                    "file": file_str,
                    "line": src[: m.start()].count("\n") + 1,
                    **extra,
                }
            )

        if not conclusion:
            continue
        # Rule 1 — the proof IS a hypothesis whose type is the conclusion.
        if is_bare:
            if proof in binders and binders[proof] == conclusion:
                _hit(proof, "hypothesis-is-conclusion")
            continue
        # Rule 3 — the CONJUNCTIVE form.  The conclusion is literally
        # `T1 ∧ … ∧ Tn` and the proof is `⟨b.f1, …, b.fn⟩`, where the fields
        # `f1..fn` of ONE binder `b` declare exactly `T1..Tn`.  The anonymous
        # constructor is then the identity on the hypotheses: the carrier
        # already asserts every conjunct and the theorem only re-tuples them,
        # which is §3b-cond rule 5's "carries the block's own conclusion as a
        # field", n times over.
        #
        # What this must NOT catch is the sanctioned pattern AGENTS.md names:
        # an `Iff` assembled by `⟨ctx.forward, ctx.backward⟩`.  That is handled
        # in `conjuncts()` by structure, not by a name list -- `A ↔ B` has no
        # top-level `∧`, so no component count can ever agree.
        if tup is not None:
            parts = conjuncts(conclusion)
            if parts is None:
                continue
            # Try the un-flattened shapes first, then the right-spine-flattened
            # ones.  `⟨a, b, c⟩ : A ∧ B ∧ C` agrees at the first; `⟨a, ⟨b, c⟩⟩
            # : A ∧ (B ∧ C)` only at the second.
            for comps, cjs in (
                (tup, parts),
                (
                    _flatten_right(tup, tuple_components),
                    _flatten_right(parts, _expand_conjunct),
                ),
            ):
                if len(comps) < 2 or len(comps) != len(cjs):
                    continue
                ms = [TUPLE_COMPONENT.match(c) for c in comps]
                if any(mc is None for mc in ms):
                    continue
                bnames = {mc.group("binder") for mc in ms}
                if len(bnames) != 1:
                    continue
                bname = next(iter(bnames))
                btype = binders.get(bname)
                if not btype:
                    continue
                base = btype.split()[0].lstrip("@")  # `C M q` -> `C`
                siblings = classes.get(base, {})
                ftypes = [siblings.get(mc.group("field")) for mc in ms]
                if any(ft is None for ft in ftypes):
                    continue
                ok = all(
                    _same_prop(ft, cj)
                    or _same_prop(_qualify(ft, bname, siblings,
                                           mc.group("field")), cj)
                    for ft, cj, mc in zip(ftypes, cjs, ms)
                )
                if ok:
                    _hit(
                        ", ".join(f"{bname}.{mc.group('field')}" for mc in ms),
                        "conjunction-is-conclusion",
                        carrier=base,
                        components=len(ms),
                    )
                    break
            continue
        # Rule 2 — the proof projects a class field whose DECLARED TYPE is the
        # conclusion: `class C where claim : P` + `theorem t [ctx : C] : P :=
        # ctx.claim ...`.  The class axiomatises the conclusion instead of the
        # hypotheses, which is exactly what §3b-cond rule 5 forbids.
        if proj is None:  # rule 3 consumed it (or was disabled) — not rule 2
            continue
        bname, fname = proj.group("binder"), proj.group("field")
        btype = binders.get(bname)
        if not btype:
            continue
        base = btype.split()[0].lstrip("@")  # `C M q` -> `C`
        siblings = classes.get(base, {})
        ftype = siblings.get(fname)
        if not ftype:
            continue
        # A field type is written INSIDE the structure, where sibling fields are
        # bare (`commutes : ... ≫ connection = prolonged_connection ≫ ...`).
        # The conclusion is written at the USE SITE, where the same fields carry
        # the binder prefix (`jp.connection`).  A raw comparison therefore never
        # matches precisely for the interesting case -- a field whose type
        # mentions its siblings, which is what a `commutes`/`claim` field is.
        # Qualify the siblings before comparing.
        qualified = norm(ftype)
        for sib in siblings:
            if sib == fname:
                continue
            qualified = re.sub(rf"(?<![.\w]){re.escape(sib)}\b",
                               f"{bname}.{sib}", qualified)
        if norm(ftype) == conclusion or qualified == conclusion:
            _hit(f"{bname}.{fname}", "class-field-is-conclusion")
    return out


def analyze(path: Path):
    raw = path.read_text(encoding="utf-8", errors="replace")
    return analyze_text(raw, str(path))


VARIANTS = (
    "hypothesis-is-conclusion",
    "class-field-is-conclusion",
    "conjunction-is-conclusion",
)

# (path, decl, expected-variant-or-None).  `None` means "must NOT be flagged".
#
# The negative is the point of this fixture, not padding.  AGENTS.md §3b-cond
# item 5 names `q_bkm_criterion` as the VERIFIED EXEMPLAR of a legitimate
# conditional-class theorem -- an `Iff` assembled from the two directional
# hypotheses -- and its proof term `⟨ctx.bkm_necessity, ctx.bkm_continuation⟩`
# is shape-identical to the defect.  A rule 3 that widens until it catches that
# is worse than no rule 3, so the selftest pins BOTH ends.
_SELFTEST = (
    ("folio/quantum-observable-universe/lean/QOU/JetHorizon.lean",
     "qou_is_ccc", "conjunction-is-conclusion"),
    ("folio/quantum-observable-universe/lean/QOU/JetHorizon.lean",
     "ccc_boundary_data_exists", "conjunction-is-conclusion"),
    ("folio/quantum-observable-universe/lean/QOU/FluidDynamics/"
     "q_bkm_criterion.lean", "q_bkm_criterion", None),
    ("folio/quantum-observable-universe/lean/QOU/Information/"
     "PNeqNpEquivalence.lean", "equivalence_of_faithfulness", None),
    # A structure-instance constructor that PERMUTES its components: content,
    # not re-bundling, and structurally excluded because `Positive a b c` has
    # no top-level `∧`.
    ("folio/quantum-observable-universe/lean/QOU/Knot/"
     "M004AngleStructure.lean", "Positive.sigma", None),
    # Pins STRIP_LAMBDA_ASCRIPTIONS: this 4-way re-bundle is the ONLY corpus
    # hit that needs the lambda arm, so without it here that flag can be
    # flipped off and the selftest still passes (measured — it did).
    ("folio/quantum-observable-universe/lean/QOU/ParticleInteractions/"
     "lp_dual_stability.lean", "lp_dual_stability",
     "conjunction-is-conclusion"),
    # The rules the conjunctive arm must not disturb.
    ("folio/quantum-observable-universe/lean/QOU/Torsion/"
     "JetProlongation.lean", "jet_prolongation_C", "class-field-is-conclusion"),
    ("folio/quantum-observable-universe/lean/QOU/MathlibExt/SDP.lean",
     "strong_duality", "class-field-is-conclusion"),
)


def selftest() -> int:
    """Fail unless the detector still catches its known positives AND still
    lets the sanctioned `Iff` exemplar through."""
    bad = []
    for rel, decl, want in _SELFTEST:
        path = Path(rel)
        if not path.exists():
            bad.append(f"FIXTURE MISSING  {rel}")
            continue
        got = [h for h in analyze(path) if h["decl"] == decl]
        if want is None:
            if got:
                bad.append(f"FALSE POSITIVE   {decl} flagged "
                           f"{got[0]['variant']} ({rel})")
            else:
                print(f"  ok  {decl:34s} not flagged (as required)")
            continue
        if not got:
            bad.append(f"MISSED           {decl} ({rel}) — expected {want}")
        elif got[0]["variant"] != want:
            bad.append(f"WRONG VARIANT    {decl}: {got[0]['variant']} "
                       f"!= {want} ({rel})")
        else:
            print(f"  ok  {decl:34s} {want}")
    # Unit-level guards on the two pieces that carry the discrimination.
    units = [
        ("iff is not a conjunction",
         conjuncts("ctx.extendsSmoothly ↔ ctx.vorticityIntegralFinite"), None),
        ("implication is not a conjunction", conjuncts("A → B ∧ C"), None),
        ("quantifier body is not a conjunction",
         conjuncts("∀ x, P x ∧ Q x"), None),
        ("structure application is not a conjunction",
         conjuncts("Positive γ₁ β₁ α₁ α₂ γ₂ β₂"), None),
        ("right-nested tuple flattens",
         _flatten_right(tuple_components("⟨a.x, ⟨a.y, a.z⟩⟩"),
                        tuple_components), ["a.x", "a.y", "a.z"]),
        ("left-nested tuple does NOT flatten",
         _flatten_right(tuple_components("⟨⟨a.x, a.y⟩, a.z⟩"),
                        tuple_components), ["⟨a.x, a.y⟩", "a.z"]),
        ("unicode field component parses",
         bool(TUPLE_COMPONENT.match("h.hγ₁")), True),
        ("applied component is rejected",
         TUPLE_COMPONENT.match("ctx.field s t"), None),
        ("anonymous instance binder [HasClaim X] + HasClaim.claim caught (qou-1ccx)",
         [h["variant"] for h in analyze_text(
             "class HasClaim (X : Type) : Prop where\n"
             "  claim : X = X\n"
             "theorem probeB (X : Type) [HasClaim X] : X = X := HasClaim.claim\n"
         )], ["class-field-is-conclusion"]),
    ]
    for label, got, want in units:
        if got != want:
            bad.append(f"UNIT             {label}: {got!r} != {want!r}")
        else:
            print(f"  ok  unit: {label}")
    if bad:
        print("\nSELFTEST FAILED:", file=sys.stderr)
        for b in bad:
            print("  " + b, file=sys.stderr)
        return 1
    print("\nselftest ok")
    return 0


def main():
    if "--selftest" in sys.argv[1:]:
        return selftest()
    roots = sys.argv[1:] or ["folio"]
    hits = []
    scanned = 0
    for root in roots:
        # A ROOT MAY BE A SINGLE FILE. `rglob` on a file path matches nothing,
        # so without this the script printed "scanned 0 .lean files -- 0
        # candidates" and exited 0 for `<script> path/to/One.lean`: an absent
        # check that reads exactly like a passing one. Same shape as
        # `real-sorry-scan.py`, which already got this right.
        rp = Path(root)
        cands = [rp] if (rp.is_file() and rp.suffix == ".lean") else rp.rglob("*.lean")
        for p in sorted(cands):
            # Vendored dependency trees are not our corpus: Mathlib ships
            # `(h : P) : P := h` fixtures in MathlibTest/ on purpose.
            if ".lake" in p.parts:
                continue
            scanned += 1
            try:
                hits.extend(analyze(p))
            except Exception as e:  # noqa: BLE001
                print(f"  ! {p}: {e}", file=sys.stderr)
    counts = {v: sum(1 for h in hits if h["variant"] == v) for v in VARIANTS}
    print(f"scanned {scanned} .lean files — {len(hits)} self-assuming candidate(s)")
    for v in VARIANTS:
        print(f"  {counts[v]:4d}  {v}")
    # A carrier declared in ANOTHER file is not resolved (see `parse_classes`),
    # so a clean run is evidence about same-file carriers only.  Say so: an
    # unstated limitation reads exactly like an all-clear.
    print("\nnote: carriers are resolved WITHIN the declaring file only — a "
          "`class`/`structure`\n      imported from another module, or "
          "inherited via `extends`, is not resolved,\n      so these counts "
          "are a LOWER BOUND, not a clean bill.\n")
    if scanned == 0:
        print("error: scanned 0 .lean files — this is NOT a pass. Check the "
              "root(s) given; nothing was audited.", file=sys.stderr)
        return 2
    for v in VARIANTS:
        sel = sorted((h for h in hits if h["variant"] == v),
                     key=lambda x: (x["file"], x["line"]))
        if not sel:
            continue
        print(f"── {v} ({len(sel)}) " + "─" * 20)
        for h in sel:
            print(f"  {h['kind']} {h['decl']}")
            print(f"    {h['file']}:{h['line']}")
            if v == "class-field-is-conclusion":
                print(f"    class field {h['hypothesis']} : {h['statement']}"
                      f"  ⊢  {h['statement']}")
            elif v == "conjunction-is-conclusion":
                print(f"    ⟨{h['hypothesis']}⟩   ({h['components']} fields of "
                      f"{h['carrier']})")
                print(f"    ⊢  {h['statement']}")
            else:
                print(f"    ({h['hypothesis']} : {h['statement']})"
                      f"  ⊢  {h['statement']}")
            print()
    Path("/tmp/self-assuming.json").write_text(json.dumps(hits, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
