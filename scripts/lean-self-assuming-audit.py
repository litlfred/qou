#!/usr/bin/env python3
"""Find self-assuming projections: `theorem f (h : P) ... : P := h`.

The triviality probe (folio-assistant lean-triviality-probe.ts) surfaces
these, but costs a `lean` elaboration per declaration (~11 min / 40
blocks). The shape is syntactic, so a static pass covers the whole corpus
in seconds and is the cheap pre-filter.

What it flags: a provable declaration whose entire proof term is a bare
identifier that names one of its own explicit hypotheses, AND whose
conclusion is syntactically the same as that hypothesis's type. That is
`P -> P` proved by `id` -- it asserts nothing about the objects involved.

Also flagged, as of 2026-08-21 (bean `qou/q407`):

  * `:= by exact h` and `:= exact h` -- the earlier docstring called these
    out of scope as "needing elaboration to judge". They do not: when the
    argument is a BARE IDENTIFIER naming a binder whose type is the
    conclusion, `by exact h` is exactly as certain as `h`. Only a
    `by exact <expression>` needs elaboration, and that is still skipped.
  * `:= by assumption` -- vacuous precisely when some binder already has
    the conclusion's type; the detector reports which one.
  * category `trivial-existential`: `∃ x, e = x` proved by `⟨e, rfl⟩`.
    A different vacuity from self-assumption -- there is no hypothesis
    being echoed -- but the same defect: it holds for EVERY `e` in a total
    type theory, so "`e` is well-defined" is not a theorem about `e`.

Deliberately NOT flagged:
  * `by exact <expression>`, `by simp`, `by simpa using h` -- may be
    vacuous, but judging needs elaboration
  * `h.1`, `h.symm`, `f h` -- projections/applications do real work
  * conclusion differing from the hypothesis type in any way -- even a
    reassociation is content

Output is a candidate list for agent inspection, not a verdict.
"""

import re
import sys
import json
from pathlib import Path

# theorem/lemma NAME <binders> : CONCLUSION := PROOF
#: Keywords that start a new top-level item, i.e. end the previous one.
#:
#: `axiom` was missing, and the omission was **silent and consequential**.
#: `rest` runs to the next terminator, so a theorem followed by an `axiom`
#: swallowed it whole: `y_base_case_singleton` (wedderburn-bratteli-recursion)
#: yielded a 361-character "proof" reading
#: `hbase axiom plancherel_completeness_axiom {R : Type u} …`, which the
#: length guard below then rejected. A textbook `(h : P) : P := h` was
#: therefore invisible — as was `unified_mass_finite`, a textbook trivial
#: existential — and both were found only by cross-checking this script
#: against `content/pipeline/lean-vacuity-axiom-audit.ts`, which splits
#: declarations differently.
#:
#: Note also that `/--` and `--` were dead alternatives here: `analyze`
#: runs this over COMMENT-STRIPPED source, so no comment marker survives to
#: match. Every real terminator has to be a keyword, which is why the list
#: missing one was enough to lose a declaration.
DECL_TERMINATORS = (
    "theorem|lemma|def|abbrev|axiom|example|instance|structure|class|inductive"
    "|opaque|macro|notation|syntax|elab|deriving|mutual|initialize"
    "|private|protected|partial|unsafe|nonrec|scoped|noncomputable|local"
    "|end|namespace|section|variable|universe|open|attribute|set_option"
)
DECL = re.compile(
    r"^(?P<kw>theorem|lemma)\s+(?P<name>[A-Za-z_][A-Za-z0-9_.']*)\s*(?P<rest>.*?)"
    r"(?=^\s*(?:@\[|" + DECL_TERMINATORS + r")\b|\Z)",
    re.S | re.M,
)
# Binder delimiters. Explicit `(..)`, implicit `{..}`, strict-implicit
# `⦃..⦄` and instance `[..]` are all scanned; an anonymous instance binder
# carries no top-level `:` and is skipped naturally.
OPEN_TO_CLOSE = {"(": ")", "{": "}", "[": "]", "\u2983": "\u2984"}
CLOSERS = set(OPEN_TO_CLOSE.values())


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


def parse_binders(sig: str) -> dict:
    """Map binder names to their (normalised) types, at any nesting depth.

    Replaces a regex that permitted only ONE level of parentheses inside a
    binder's type::

        BINDER = re.compile(r"\\((?P<names>[^():]+?)\\s*:\\s*(?P<type>(?:[^()]|\\([^()]*\\))*)\\)")

    A hypothesis like

        (h : ¬(w ≠ [] ∧ (∀ g ∈ w, g ≠ 0) ∧ (∀ g ∈ w, 3 ≤ f g)))

    nests two deep, so the regex did not match, the binder was dropped, and
    the declaration could never be reported — the scan **skipped it
    silently**, indistinguishably from finding it clean. That is how
    `structurallyValidBinding_necessary` (PSDFeasibilityProxy.lean) sat
    unreported in a file whose sibling declaration WAS reported, and it
    biased the sweep against precisely the elaborate statements most likely
    to be hiding a tautology.

    Balanced-delimiter scanning has no depth limit, so the class of
    statement this can miss is no longer a function of how complicated the
    statement is.
    """
    binders: dict = {}
    i, n = 0, len(sig)
    while i < n:
        if sig[i] not in OPEN_TO_CLOSE:
            i += 1
            continue
        depth, j = 0, i
        while j < n:
            if sig[j] in OPEN_TO_CLOSE:
                depth += 1
            elif sig[j] in CLOSERS:
                depth -= 1
                if depth == 0:
                    break
            j += 1
        if j >= n:            # unbalanced tail; nothing further to parse
            break
        inner = sig[i + 1 : j]
        # Cut at the FIRST top-level `:` — `(x y : T)` binds both names,
        # and a type may itself contain `∀ z : T, ..`.
        d, cut = 0, -1
        for k, c in enumerate(inner):
            if c in OPEN_TO_CLOSE:
                d += 1
            elif c in CLOSERS:
                d -= 1
            elif c == ":" and d == 0:
                cut = k
                break
        if cut >= 0:
            typ = norm(inner[cut + 1 :])
            for nm in inner[:cut].split():
                binders[nm] = typ
        i = j + 1
    return binders


def conclusion_colon(sig: str) -> int:
    """Index of the `:` that introduces the conclusion, or -1.

    Walks left to right, skipping each balanced binder group whole, and
    returns the FIRST `:` seen outside any group.

    The previous rule was "the LAST top-level `:`", which is wrong for a
    conclusion that contains one of its own::

        theorem phi_k_finite (k : ℕ) … : ∃ x : ℝ, phi_k k blocks = x

    Here the `:` inside `∃ x : ℝ` is also at depth 0, so "last" picked it
    and the conclusion came out as `ℝ, phi_k k blocks = x` — garbage that
    could never match a hypothesis type. Every quantified conclusion was
    silently unanalysable, which is the same failure mode as the binder
    regex: unparsed and clean looked identical.
    """
    i, n = 0, len(sig)
    while i < n:
        ch = sig[i]
        if ch in OPEN_TO_CLOSE:
            depth, j = 0, i
            while j < n:
                if sig[j] in OPEN_TO_CLOSE:
                    depth += 1
                elif sig[j] in CLOSERS:
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            if j >= n:
                return -1
            i = j + 1
            continue
        if ch == ":":
            if i + 1 < n and sig[i + 1] == "=":
                i += 2
                continue
            return i
        i += 1
    return -1


IDENT = re.compile(r"[A-Za-z_][A-Za-z0-9_']*")
#: A binder type containing a relation/quantifier reads as a hypothesis
#: rather than a plain type or instance argument.
PROPISH = re.compile(r"[=≤<∈¬∀∃≥→]")
#: `h`, `by exact h`, `exact h`, `by exact (h)` — all identity proofs when
#: `h` names a binder whose type is the conclusion.
EXACT_IDENT = re.compile(
    r"(?:by\s+)?exact\s*\(?\s*(?P<name>[A-Za-z_][A-Za-z0-9_']*)\s*\)?"
)
ASSUMPTION = re.compile(r"by\s+assumption")
#: `⟨e, rfl⟩` — or `⟨_, rfl⟩` — optionally behind `by exact`.
ANON_REFL = re.compile(r"(?:by\s+)?(?:exact\s+)?⟨\s*(?P<wit>.+?)\s*,\s*rfl\s*⟩", re.S)
#: `∃ x, body` or `∃ x : T, body` (single binder).
EXISTS_HEAD = re.compile(
    r"^∃\s*(?P<var>[A-Za-z_][A-Za-z0-9_']*)\s*(?::(?P<ty>[^,]*))?,\s*(?P<body>.+)$",
    re.S,
)


def self_assuming_witness(proof: str, binders: dict, conclusion: str):
    """Name of the echoed hypothesis, or None."""
    p = proof.strip()
    m = EXACT_IDENT.fullmatch(p)
    if m:
        p = m.group("name")
    if IDENT.fullmatch(p):
        if p in binders and binders[p] == conclusion:
            return p
        return None
    if ASSUMPTION.fullmatch(p):
        for nm, ty in binders.items():
            if ty == conclusion:
                return nm
    return None


def trivial_existential_witness(proof: str, conclusion: str):
    """Witness term of a `∃ x, e = x := ⟨e, rfl⟩`, or None.

    Holds for every `e`, so it asserts nothing about `e`. "Well-defined"
    is not a theorem in a total type theory.
    """
    m = ANON_REFL.fullmatch(proof.strip())
    if not m:
        return None
    em = EXISTS_HEAD.match(conclusion.strip())
    if not em:
        return None
    var, body, wit = em.group("var"), norm(em.group("body")), norm(m.group("wit"))
    if body in (f"{wit} = {var}", f"{var} = {wit}"):
        return wit
    if wit == "_":
        # `⟨_, rfl⟩` is the SAME defect and a stronger tell: the author did
        # not even name the witness, and the elaborator recovered it by
        # unifying `rfl`. Requiring the witness to be spelled out is what
        # let `knot_factor_amphicheiral` (KnotFactorAmphicheiral.lean) sit
        # unreported while its own sibling `knot_factor_amphicheiral_value`
        # — the identical shape, witness written out — was reported. The
        # first is `lean.ref`-bound and carries two substantive-looking
        # hypotheses; the second is unreferenced. The scan was blind to
        # exactly the more consequential of the two.
        sides = split_top_level_eq(body)
        if sides is None:
            return None
        lhs, rhs = sides
        if lhs == var and var not in IDENT.findall(rhs):
            return rhs
        if rhs == var and var not in IDENT.findall(lhs):
            return lhs
    return None


def split_top_level_eq(body: str):
    """`(lhs, rhs)` of the first `=` outside every bracket group, or None.

    A nested `=` must not be mistaken for the equation's own — `∃ x, f (a =
    b) = x` splits at the second `=`, not the first.
    """
    depth = 0
    for i, ch in enumerate(body):
        if ch in OPEN_TO_CLOSE:
            depth += 1
        elif ch in CLOSERS:
            depth -= 1
        elif ch == "=" and depth == 0:
            # not `≠`, `≤`, `≥`, `:=`, `==`
            if body[i - 1 : i] in (":", "<", ">", "!", "=") or body[i + 1 : i + 2] == "=":
                continue
            return norm(body[:i]), norm(body[i + 1 :])
    return None


def conclusion_mentions_no_binder(binders: dict, conclusion: str):
    """Names bound by the declaration but absent from its conclusion, or None.

    A heuristic, deliberately reported as its own low-confidence category.
    Hypotheses routinely fail to appear in a conclusion — `hA : 4 ≤ Z + N`
    does not occur in `nuclearKnotType Z N = .borromean`, and that is a
    perfectly good theorem. What is suspicious is the stronger condition
    checked here: the conclusion mentions **none** of the declaration's
    binders at all, so it cannot be a statement about the objects the
    declaration is parameterised by.

    Measured on the 27 confirmed findings, this is what separates the
    harmful from the benign. `wenzl_annihilator`'s conclusion
    `∃ x : R, x = 0` names no binder — its `firstCol ≥ 4` hypothesis is
    inert — whereas `archimedean_eval_well_defined`'s `∃ y, evalAtQZero p = y`
    does mention `p`, and is merely a definition restated.

    **It does not generalise, and the measurement says so.** Corpus-wide
    it fires 854 times without the Prop-ish requirement and 447 with it —
    roughly 15% of all provable declarations. Perfectly ordinary theorems
    about globally-defined constants mention globals rather than binders,
    and that is not a defect. So this is **not gate material**, and it is
    deliberately behind `--heuristic` rather than on by default: it is a
    triage aid for a human working through a file, not a check anything
    should fail on. Recorded rather than dropped because the negative is
    worth knowing — the obvious generalisation of the tell does not work.
    """
    if not binders:
        return None
    tokens = set(IDENT.findall(conclusion))
    if any(nm in tokens for nm in binders):
        return None
    # Require at least one binder that actually looks like a HYPOTHESIS.
    # Without this the rule fires on every ordinary theorem about global
    # constants — measured 854 hits corpus-wide, ~28%, unusable as a gate.
    if not any(PROPISH.search(ty) for ty in binders.values()):
        return None
    return sorted(binders)


#: `-- vacuous-by-design: <reason>` immediately above a declaration.
VACUOUS_OK = re.compile(r"--\s*vacuous-by-design:\s*(?P<why>\S.*?)\s*$")


def acknowledgment(raw_lines: list, line: int):
    """Reason from a `-- vacuous-by-design:` marker above `line`, or None.

    Some trivial existentials are *deliberate* and their triviality is the
    point. `qou_standardPart_image_exists` (AppendixSurreals/Conjectures.lean)
    exists to record that a conjunct of the original `VacuumEpsilon`
    conjecture was provable for any `SQ`, so that the surviving conjecture
    asserts only what is irreducibly open — and it is *used*, to rebuild the
    original wider statement. Deleting it would destroy a narrowing audit.

    Such a declaration is still reported, in its own section, never dropped:
    a check that silently excuses cases is indistinguishable from one that
    never ran, which is the defect class this whole script exists for. The
    marker moves a finding out of the actionable list and into the record,
    and it must carry a reason — a bare mute is not accepted.

    Only the contiguous run of `--` lines, attributes and blanks directly
    above the declaration is searched, so a marker cannot drift onto an
    unrelated neighbour.
    """
    i = line - 2  # 0-based index of the line above the declaration
    while i >= 0:
        t = raw_lines[i].strip()
        if not t or t.startswith("@["):
            i -= 1
            continue
        if not t.startswith("--"):
            return None
        m = VACUOUS_OK.search(t)
        if m:
            return m.group("why")
        i -= 1
    return None


#: Declarations rejected by the proof-length guard, so the number is
#: reportable rather than silent. See the guard in `analyze`.
SKIPPED_LONG: list = []


def analyze(path: Path, report_heuristic: bool = False):
    raw = path.read_text(encoding="utf-8", errors="replace")
    raw_lines = raw.splitlines()
    src = strip_comments(raw)
    out = []
    for m in DECL.finditer(src):
        body = m.group("rest")
        # split at the LAST top-level `:=` that starts the proof term
        idx = body.rfind(":=")
        if idx < 0:
            continue
        proof = norm(body[idx + 2 :])
        # Cheap reject: only short proof terms can be vacuous in the shapes
        # below. This used to demand a BARE IDENTIFIER, which is what kept
        # `by exact h`, `by assumption` and `⟨e, rfl⟩` out of reach.
        #
        # COUNTED, not silent. A mis-split declaration lands here looking
        # like a very long proof, so a rise in this number is the symptom of
        # a `DECL_TERMINATORS` gap rather than of long proofs. That is
        # exactly how `axiom` went missing for as long as it did: the guard
        # rejected the runaway `rest` and said nothing. `--diagnostics`
        # prints the tally.
        if not proof:
            continue
        if len(proof) > 200:
            SKIPPED_LONG.append((str(path), m.group("name"), len(proof)))
            continue
        sig = body[:idx]
        concl_at = conclusion_colon(sig)
        if concl_at < 0:
            continue
        conclusion = norm(sig[concl_at + 1 :])
        if not conclusion:
            continue
        binders = parse_binders(sig[:concl_at])
        rec = {
            "decl": m.group("name"),
            "kind": m.group("kw"),
            "statement": conclusion,
            "file": str(path),
            "line": src[: m.start()].count("\n") + 1,
        }
        hyp = self_assuming_witness(proof, binders, conclusion)
        if hyp is not None:
            out.append({**rec, "category": "self-assuming", "hypothesis": hyp})
            continue
        wit = trivial_existential_witness(proof, conclusion)
        if wit is not None:
            why = acknowledgment(raw_lines, rec["line"])
            cat = "trivial-existential-by-design" if why else "trivial-existential"
            hit = {**rec, "category": cat, "hypothesis": wit}
            if why:
                hit["acknowledged"] = why
            out.append(hit)
            continue
        if report_heuristic:
            inert = conclusion_mentions_no_binder(binders, conclusion)
            if inert is not None:
                out.append({**rec, "category": "conclusion-mentions-no-binder",
                            "hypothesis": ", ".join(inert)})
    return out


def main():
    argv = [a for a in sys.argv[1:] if a not in ("--heuristic", "--diagnostics")]
    heuristic = "--heuristic" in sys.argv[1:]
    diagnostics = "--diagnostics" in sys.argv[1:]
    roots = argv or ["content"]
    hits = []
    scanned = 0
    for root in roots:
        for p in Path(root).rglob("*.lean"):
            # Vendored dependency trees are not our corpus: Mathlib ships
            # `(h : P) : P := h` fixtures in MathlibTest/ on purpose.
            if ".lake" in p.parts:
                continue
            scanned += 1
            try:
                hits.extend(analyze(p, report_heuristic=heuristic))
            except Exception as e:  # noqa: BLE001
                print(f"  ! {p}: {e}", file=sys.stderr)
    by_cat: dict = {}
    for h in hits:
        by_cat.setdefault(h["category"], []).append(h)
    tally = ", ".join(f"{len(v)} {k}" for k, v in sorted(by_cat.items()))
    print(f"scanned {scanned} .lean files — {len(hits)} candidate(s): {tally}\n")
    if SKIPPED_LONG:
        print(
            f"  {len(SKIPPED_LONG)} declaration(s) skipped: proof term over 200 "
            "chars. A mis-split declaration looks exactly like this, so treat a "
            "rise as a DECL_TERMINATORS gap until shown otherwise"
            + (" (--diagnostics to list)" if not diagnostics else ":")
        )
        if diagnostics:
            for f, n, ln in sorted(SKIPPED_LONG, key=lambda x: -x[2])[:40]:
                print(f"    {ln:>6}  {n}  {f}")
        print()
    for cat in sorted(by_cat):
        print(f"── {cat} ──\n")
        for h in sorted(by_cat[cat], key=lambda x: (x["file"], x["line"])):
            print(f"  {h['kind']} {h['decl']}")
            print(f"    {h['file']}:{h['line']}")
            if cat == "conclusion-mentions-no-binder":
                print(f"    ⊢ {h['statement']}")
                print(f"    binds {h['hypothesis']} — none of which the conclusion mentions")
            elif cat == "self-assuming":
                print(f"    ({h['hypothesis']} : {h['statement']})  ⊢  {h['statement']}")
            else:
                print(f"    ⊢ {h['statement']}   witnessed by ⟨{h['hypothesis']}, rfl⟩")
                if h.get("acknowledged"):
                    print(f"    acknowledged: {h['acknowledged']}")
            print()
    Path("/tmp/self-assuming.json").write_text(json.dumps(hits, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
