#!/usr/bin/env python3
"""Detect *borrowed-name* theorems: a declaration named after an external body
of mathematics whose statement is entirely about the file's own definitions.

Motivation (bean `qou-0avp`).  The corpus-wide claim that the per-partition
`Δ_λ` value is "PROVED, sorry-free, general-n" rests on

    def gradedDimG   (N d k : ℕ) : ℕ := if k = N then d else 0   -- one-hot
    def dtEulerG     (N d : ℕ) : ℤ := Σ_{k ≤ N} (-1)^k * gradedDimG N d k
    def deltaLambdaG (N d : ℕ) : ℤ := (-1)^N * d
    theorem dtEulerG_eq_deltaLambdaG : dtEulerG N d = deltaLambdaG N d := by
      rw [dtEulerG_collapse]; rfl

The "DT / 3d-index graded Euler characteristic" is the alternating sum of a list
that is zero except in one slot.  No moduli space, no Behrend function, no
perverse sheaf: `(-1)^N` is *named* the Behrend sign by the docstring.  The
theorem is true, cheap, and about nothing but the three `def`s above it.

**It is NOT, however, a `rfl`.**  Checked with the kernel companion
(`scripts/lean/BorrowedNameKernel.lean`): `defeq_collapse = false`,
`value_is_rfl = false`.  With `N` free, `List.range (N+1)` does not reduce, so
`dtEulerG_collapse` is a genuine — if elementary — induction.  This audit's
claim is therefore about NAMING and SCOPE (the statement quantifies over
nothing but this file's own definitions, under a name borrowed from
Donaldson-Thomas theory), NOT about the proof being vacuous.  Do not describe a
CRITICAL here as "proved by rfl" without checking; the kernel companion is what
settles that, and it overturned exactly that claim once.

## Why the existing detectors miss this

`scripts/lean-definition-collapsed-audit.py` (bean `qou-k9yt`) needs BOTH

  A. COLLAPSED   proof is `rfl` / `by rfl` / `simp`/`unfold` over a same-file def
  B. OPEN-CLAIM  the docstring ADMITS the statement is open

and this shape defeats both.  B is the mirror image of what happens here — the
docstring *over*-claims ("THE GENERAL-`n` UNIFICATION", "the real content")
rather than admitting openness.  A misses too: `TRIVIAL_TAIL` matches `:= rfl`
and `:= by rfl`, not `:= by rw [dtEulerG_collapse]; rfl`, and the rewrite target
is a *theorem*, not the plain `def` that `SIMP_ARGS` looks for.  Verified: that
script reports the file clean.

Its `DEFAULT_ROOTS` also cover only `content/<paper>/lean/`, so the ~900
content-block `.lean` siblings are outside its scope entirely.  This audit walks
the whole paper tree.

## The two signals

  BORROWED    the decl name or its docstring invokes an external named theory
              (Donaldson-Thomas, Behrend, Springer, Seifert, Verlinde,
              Peter-Weyl, Kazhdan-Lusztig, Chebyshev, Yang-Baxter, ...).
  LOCAL-ONLY  every identifier in the STATEMENT that is declared anywhere in
              this repo's Lean tree is declared in THIS file — and at least one
              is.  Resolution is exact, not a Mathlib-name guess: a global index
              of every declaration in the tree is built first, so an identifier
              absent from it is Mathlib/core by construction.

Those two alone are NOT enough, and shipping them as the CRITICAL rule would
have been useless: measured, `BORROWED and LOCAL-ONLY` fires **1121** times,
about a third of the provable declarations in the tree.  Most are legitimate —
a file that defines an object and proves things about it is normal Lean.  Two
further signals do the discriminating:

  OVERCLAIM   the docstring asserts the declaration CARRIES the external
              theory's content ("the real content", "the unification",
              "derives", "PROVED", "the genuine check").  This is the mirror
              image of the sibling detector's OPEN-CLAIM signal, which is why
              that detector cannot see this shape.
  CHEAP       the proof is <=4 steps drawn only from the restate-only tactics
              (rfl/decide/simp/unfold/rw/norm_num/ring/...) and cites no lemma
              from another file, so it cannot import content from outside.

    CRITICAL  BORROWED and LOCAL-ONLY and OVERCLAIM and CHEAP   ->   12
    major     BORROWED and LOCAL-ONLY and CHEAP                 ->  197
    advisory  BORROWED and LOCAL-ONLY                           ->  939

A docstring that DISCLAIMS ("definitional", "by definition", "a restatement",
"notation for") downgrades to advisory, mirroring the sibling detector's
exclusion discipline: a definitional restatement that says so is legitimate.

## What the 12 look like (spot-checked 4; 3 genuine, 1 arguably legitimate)

`QOU/BraidKnot/Sigma1CubedSeifertTessellation.seifert_euler_relation` is the
clearest, and was found by the detector rather than designed for:

    def seifertDisks : Int := 2          def boundaryComponents : Int := 1
    def seifertBands : Int := 3          def seifertGenus : Int := 1
    def seifertEuler : Int := seifertDisks - seifertBands
    /-- ... This is the genuine check (had the cell count been wrong, this
        would fail). -/
    theorem seifert_euler_relation :
        seifertEuler = 2 - 2 * seifertGenus - boundaryComponents := by decide

Every integer is hand-entered, so `-1 = 2 - 2*1 - 1` cannot fail; the
docstring's falsifiability claim is exactly backwards.  `b3_nf_wedderburn_-
uniqueness : b3_nf_coefficients 5 = 0` reads off entry 5 of a hand-entered
table whose fifth line is literally `| 5 => 0`, under a name claiming
Wedderburn-Artin uniqueness.

The arguably-legitimate one is `hecke_n3_frobenius_codim`, a real symbolic
identity over a locally-defined q-dimension that merely happens to be named
after Frobenius.  Expect roughly that rate; do not quote it as a precision
figure from a sample of four.

Like every other vacuity criterion this is a HIGH-RECALL CANDIDATE GENERATOR.
A CRITICAL is not a verdict — the genuine/legit call is an agent's, and belongs
in `docs/audits/lean-vacuity-review-ledger.json` per AGENTS.md §3b-tax.

Usage:
    python3 scripts/lean-borrowed-name-audit.py [root ...]
    python3 scripts/lean-borrowed-name-audit.py --json out.json
    python3 scripts/lean-borrowed-name-audit.py --selftest
Exit: 0 always, unless --strict (1 on any CRITICAL) or --selftest fails.
"""
from __future__ import annotations
import os, re, sys, json

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from lean_decl_scan import (            # noqa: E402  (path set above)
    blank_comments, split_statement, decl_spans, docstring_before,
    binder_names, assumption_binders, discharges_via_binder_field,
)

DEFAULT_ROOTS = [
    "folio/quantum-observable-universe",
    "folio/unital-groebner-bases",
    "folio/fred2005-formal-groups",
]

# Proper names and theory labels that denote work done OUTSIDE this corpus.
# Calibrated against the tree; the LOCAL-ONLY signal does the discriminating,
# so this list is deliberately generous.
EXTERNAL_NAMES = [
    "Donaldson", "Thomas", "Behrend", "Springer", "Seifert", "Verlinde",
    "Peter-Weyl", "Peter--Weyl", "Kazhdan", "Lusztig", "Chebyshev",
    "Yang-Baxter", "Yang--Baxter", "Schur", "Hoefsmit", "Wedderburn",
    "Ocneanu", "Wenzl", "Habiro", "Kashiwara", "Demazure", "Jones",
    "Alexander", "Milnor", "Bennequin", "Macdonald", "Plancherel",
    "Casimir", "Bloch", "Wigner", "Frobenius", "Markov", "Brauer",
    "Temperley", "Lieb", "Iwahori", "Hecke", "Seiberg", "Witten",
    "Reidemeister", "Bratteli", "Tauber", "Riemann", "Galois",
    "Noether", "Weyl", "Kac", "Moody", "Drinfeld", "Jimbo", "Faddeev",
    "Rogers", "Ramanujan", "Bernstein", "Gelfand", "Langlands",
]
# Abbreviations, matched case-sensitively as standalone tokens only.
EXTERNAL_ABBREV = ["DT", "KL", "YBE", "TQFT", "WRT", "PBW", "RTT"]

# The docstring asserts that the declaration CARRIES the external theory's
# content -- the mirror image of the sibling detector's OPEN-CLAIM signal.
OVERCLAIM = re.compile(
    r"the real content|non-?trivial content|the unification|unifies|"
    r"THE GENERAL|derives|derivation of|is derived|proves that|"
    r"establishes|the capstone|forced by|no longer conjectural|"
    r"PROVED|now proved|closes the|the key (?:step|identity|fact)",
    re.I)

# A proof made only of these is cheap: it can restate a definition but cannot
# import content from outside the file.
CHEAP_TACTIC = re.compile(
    r"^(?:rfl|trivial|decide|native_decide|norm_num|simp|simp_all|unfold|"
    r"delta|rw|show|intro|intros|exact|refine|constructor|omega|ring|"
    r"ring_nf|field_simp|dsimp|and_intro|split|rcases|obtain)\b")

DISCLAIM = re.compile(
    r"by definition|definitional|is a definition|a restatement|restates|"
    r"notation for|purely notational|unfolds to|by construction|"
    r"cosmetic|bookkeeping|no mathematical content|says nothing|"
    # A docstring naming its own operands as PLACEHOLDERS, or explaining that
    # the result holds because two carriers are the same type, is disclosing
    # the collapse.  Found via the kernel pass on `card_cells_eq_card_nimbers`,
    # whose docstring reads "provable without any class instance because both
    # placeholder types are `Fin (p^n)`" -- an honest definitional statement
    # that the original DISCLAIM list did not recognise.
    r"placeholder type|both .{0,40}types are|are the same type|"
    r"provable without any class instance",
    re.I)

DECL = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*"
    r"(theorem|lemma|example|def|abbrev|structure|class|inductive|instance)\s+"
    r"([A-Za-z_][A-Za-z0-9_'.]*)")
PROVABLE = {"theorem", "lemma", "example"}
DEFINITIONAL = {"def", "abbrev"}

# A definition whose body is a product with a literal `0` factor is identically
# zero while *appearing* to consume its arguments.  There is no legitimate
# reason to write `0 * (Q + X + n)`: the arguments are mentioned so the
# declaration looks content-bearing, and `zero_mul` throws them away.
#
# Found via a sibling agent's coordination comment on PR #5856 (bean
# `qou-6a7w`), whose docstring in the corpus CONFESSES the idiom verbatim:
#   "Content-bearing placeholder `0 * (Q + X + lam.parts.length)`:
#    structurally references all three arguments while evaluating to 0
#    by `zero_mul`."
# Verified at source before adding this check.
# The `0` must be a WHOLE FACTOR, not a function argument.  First attempt used
# `(?<![\w.])0\s*\*`, which fired on `p 0 * n.1` (indexing), `H.\u03c3 0 * H.\u03c3 0`
# (Hecke generators) and `u 0 * v 0` (octonion multiplication): 22 hits of which
# only 3 were real.  In `p 0 * n.1` the `0` IS preceded by a non-word char --
# a space -- so the lookbehind never helped.  What distinguishes them is what
# comes before the SPACE: an identifier means application.
ZERO_PRODUCT = re.compile(
    r"(?:^|:=|[(\[,+\-*/=]|=>)\s*0\s*\*"      # 0 as left factor
    r"|\*\s*0\s*(?:$|[)\],+\-*/=]|--)")        # 0 as right factor
# The docstring admitting the idiom -- corroboration, not the primary signal.
ZERO_CONFESSION = re.compile(
    r"structurally references.{0,80}evaluat\w*\s+to\s+0|"
    r"content-bearing placeholder|placeholder\s+`?0\s*\*", re.I)
IDENT = re.compile(r"[A-Za-z_][A-Za-z0-9_']*(?:\.[A-Za-z_][A-Za-z0-9_']*)*")

# Lean keywords / tactics that are not declarations.
NOISE = {
    "by", "at", "fun", "let", "have", "show", "from", "with", "do", "then",
    "else", "if", "match", "this", "forall", "exists", "in", "where", "of",
    "Type", "Prop", "Sort", "sorry", "rfl", "and", "or", "not", "iff",
}






# BINDER now comes from scripts/lib/lean_decl_scan (bean qou-rfq9).



def split_camel(name: str) -> str:
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", name).replace("_", " ")


def borrowed_hits(name: str, doc: str) -> list[str]:
    hay_ci = split_camel(name) + " " + doc
    found = []
    for nm in EXTERNAL_NAMES:
        if re.search(r"(?<![A-Za-z])" + re.escape(nm) + r"(?![A-Za-z])",
                     hay_ci, re.I):
            found.append(nm)
    for ab in EXTERNAL_ABBREV:
        if re.search(r"(?<![A-Za-z])" + ab + r"(?![A-Za-z])", hay_ci):
            found.append(ab)
        elif re.search(r"(?<![A-Za-z])" + ab.lower() + r"(?=[A-Z])", name):
            found.append(ab)
    return sorted(set(found))


def build_index(roots: list[str], base: str):
    """Map every declaration name in the tree -> the file that declares it."""
    index: dict[str, str] = {}
    files: list[str] = []
    for root in roots:
        full = os.path.join(base, root)
        for dp, dn, fn in os.walk(full):
            dn[:] = [d for d in dn if d not in (".lake", "build", ".git")]
            for f in fn:
                if f.endswith(".lean"):
                    files.append(os.path.join(dp, f))
    per_file: dict[str, set[str]] = {}
    for p in files:
        src = open(p, encoding="utf-8", errors="replace").read()
        names = set()
        for kind, name, _, _ in decl_spans(blank_comments(src)):
            short = name.split(".")[-1]
            names.add(short)
            index.setdefault(short, p)
        per_file[p] = names
    return index, per_file, files


def audit(base: str, roots: list[str]):
    index, per_file, files = build_index(roots, base)
    findings = []
    for p in files:
        raw = open(p, encoding="utf-8", errors="replace").read()
        lines = raw.split("\n")
        code = blank_comments(raw)
        has_import = bool(re.search(r"^\s*import\s+\S+", code, re.M))
        local_defs = {n.split(".")[-1]
                      for k, n, _, _ in decl_spans(code)
                      if k in ("def", "abbrev", "structure", "class", "inductive")}
        if not local_defs:
            continue
        if not has_import:
            for kind, name, lineno, body in decl_spans(code):
                if kind in PROVABLE:
                    doc = docstring_before(lines, lineno)
                    stmt, _ = split_statement(body)
                    findings.append({
                        "kind_of_finding": "no-import-wrapper",
                        "file": os.path.relpath(p, base),
                        "line": lineno,
                        "decl": name,
                        "kind": kind,
                        "severity": "CRITICAL",
                        "overclaim": True,
                        "cheap_proof": True,
                        "simp_unfold": False,
                        "discharged_via_hypothesis": False,
                        "proof_steps": 0,
                        "borrowed": borrowed_hits(name, doc) or ["NO-IMPORT-WRAPPER"],
                        "local_defs_in_statement": sorted(local_defs)[:6],
                        "external_lemmas_in_proof": [],
                        "disclaimed": False,
                        "statement": re.sub(r"\s+", " ", stmt.strip())[:300],
                    })
            continue
        for kind, name, lineno, body in decl_spans(code):
            if kind in DEFINITIONAL:
                stmt, val = split_statement(body)
                # Only a TOP-LEVEL zero factor counts: `0 * x` buried inside a
                # larger proof or a match arm is not the placeholder idiom.
                first = val.strip().split("\n")[0]
                # A LINEAR FORM with a zero coefficient is legitimate maths,
                # not a placeholder: `mu2 * 1 + mu3 * 0 + mu4 * 0` is a real
                # functional that happens to drop two terms.  Distinguish by
                # the presence of a sibling NON-zero numeric coefficient.
                linear_form = re.search(r"\*\s*[1-9]\d*(?![\w.])", first) is not None
                if ZERO_PRODUCT.search(first) and not linear_form:
                    doc = docstring_before(lines, lineno)
                    findings.append({
                        "kind_of_finding": "zero-placeholder",
                        "file": os.path.relpath(p, base),
                        "line": lineno,
                        "decl": name,
                        "kind": kind,
                        "severity": "CRITICAL",
                        "borrowed": borrowed_hits(name, doc),
                        "local_defs_in_statement": [],
                        "external_lemmas_in_proof": [],
                        "disclaimed": False,
                        "overclaim": False,
                        "cheap_proof": True,
                        "proof_steps": 0,
                        "confesses_in_docstring": bool(ZERO_CONFESSION.search(doc)),
                        "statement": re.sub(r"\s+", " ",
                                            (stmt + " := " + first).strip())[:300],
                    })
                continue
            if kind not in PROVABLE:
                continue
            doc = docstring_before(lines, lineno)
            hits = borrowed_hits(name, doc)
            if not hits:
                continue
            stmt, proof = split_statement(body)
            idents = {m.group(0).split(".")[-1] for m in IDENT.finditer(stmt)}
            idents -= NOISE
            idents -= binder_names(stmt)
            idents.discard(name.split(".")[-1])
            # A one-character name is a bound variable, never a citation.  Left
            # in, `N` and `d` resolve against `def N`/`def d` elsewhere in the
            # tree and veto the finding — which is exactly what suppressed the
            # motivating case on the first run.
            idents = {i for i in idents if len(i) > 1}
            local = sorted(idents & local_defs)
            foreign = sorted(i for i in idents
                             if i in index and i not in per_file[p])
            if not local or foreign:
                continue
            proof_ids = {m.group(0).split(".")[-1] for m in IDENT.finditer(proof)}
            ext_lemmas = sorted(i for i in proof_ids
                                if i in index and i not in per_file[p])
            disclaimed = bool(DISCLAIM.search(doc))
            overclaim = bool(OVERCLAIM.search(doc))

            # EXCLUSION 1 -- a `@[simp]` lemma unfolding a local definition.
            # `@[simp] theorem heckeH4DimQ_one (q : R) : heckeH4DimQ q 1 =
            #  q^2 + 1 + (q^2)inv` is a definitional restatement BY DESIGN:
            # that is what a simp lemma for a table-valued function is for.
            # Measured: 62 of the 197 `major` -- 31% -- were these, all in one
            # file, which is the per-item-counting trap AGENTS.md records for
            # the witness queue (one fact counted 119 times).
            simp_unfold = bool(re.match(r"^\s*@\[[^\]]*\bsimp\b", stmt)) and bool(local)

            # EXCLUSION 2 -- the proof discharges through a FIELD of a binder
            # (`tau.commutator`, `C.ruleLinear`, `h.foo`).  That is a genuine
            # conditional derivation, not a definitional collapse.  Ported from
            # the sibling detector (bean `qou-k9yt`), which excludes the same
            # shape and cites it as the fix for its one known false positive.
            binders = assumption_binders(stmt)
            via_hyp = any(re.search(r"(?<![\w.])" + re.escape(b) + r"\.\w", proof)
                          for b in binders)
            steps = [t.strip() for t in re.split(r"[;\n<;>]|\bthen\b", proof)
                     if t.strip() and t.strip() not in ("by",)]
            steps = [re.sub(r"^by\s+", "", t) for t in steps]
            cheap = bool(steps) and all(CHEAP_TACTIC.match(t) for t in steps) \
                and len(steps) <= 4 and not ext_lemmas
            if simp_unfold or via_hyp:
                sev = "advisory"
            elif overclaim and cheap and not disclaimed:
                sev = "CRITICAL"
            elif cheap and not disclaimed:
                sev = "major"
            else:
                sev = "advisory"
            findings.append({
                "kind_of_finding": "borrowed-name",
                "file": os.path.relpath(p, base),
                "line": lineno,
                "decl": name,
                "kind": kind,
                "severity": sev,
                "overclaim": overclaim,
                "cheap_proof": cheap,
                "simp_unfold": simp_unfold,
                "discharged_via_hypothesis": via_hyp,
                "proof_steps": len(steps),
                "borrowed": hits,
                "local_defs_in_statement": local,
                "external_lemmas_in_proof": ext_lemmas,
                "disclaimed": disclaimed,
                "statement": re.sub(r"\s+", " ", stmt.strip())[:300],
            })
    rank = {"CRITICAL": 0, "major": 1, "advisory": 2}
    findings.sort(key=lambda f: (rank[f["severity"]], f["file"], f["line"]))
    return findings


SELFTEST_MUST_FIRE = "dtEulerG_eq_deltaLambdaG"


def main(argv: list[str]) -> int:
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    selftest = "--selftest" in argv
    strict = "--strict" in argv
    out = None
    if "--json" in argv:
        out = argv[argv.index("--json") + 1]
    roots = [a for a in argv[1:] if not a.startswith("--")
             and a != out] or DEFAULT_ROOTS

    findings = audit(base, roots if not selftest else DEFAULT_ROOTS)

    if selftest:
        # The detector must catch the shape it was written for.  Without this
        # a future narrowing could report a clean tree the way a name-keyed
        # `cached_accessor_shape_audit` once did.
        fired = [f for f in findings if f["decl"].endswith(SELFTEST_MUST_FIRE)]
        if not fired:
            print(f"SELFTEST FAIL: {SELFTEST_MUST_FIRE} not detected", file=sys.stderr)
            return 1
        if fired[0]["severity"] != "CRITICAL":
            print(f"SELFTEST FAIL: {SELFTEST_MUST_FIRE} not CRITICAL", file=sys.stderr)
            return 1
        print(f"SELFTEST OK: {SELFTEST_MUST_FIRE} detected CRITICAL "
              f"(borrowed={fired[0]['borrowed']}, "
              f"local={fired[0]['local_defs_in_statement']})")
        return 0

    crit = [f for f in findings if f["severity"] == "CRITICAL"]
    major = [f for f in findings if f["severity"] == "major"]
    adv = [f for f in findings if f["severity"] == "advisory"]
    for f in findings:
        print(f"{f['severity']:8s} {f['file']}:{f['line']}  {f['decl']}")
        print(f"         borrowed : {', '.join(f['borrowed'])}")
        print(f"         local    : {', '.join(f['local_defs_in_statement'])}")
        if f["external_lemmas_in_proof"]:
            print(f"         proof cites: {', '.join(f['external_lemmas_in_proof'][:6])}")
        print(f"         stmt     : {f['statement'][:160]}")
    print(f"\nborrowed-name audit: {len(crit)} CRITICAL, {len(major)} major, "
          f"{len(adv)} advisory")
    if out:
        # Persist CRITICAL + major only.  The advisory tier is 939 of 1148 rows
        # and ~700 KB; it is the tier this tool deliberately does not even
        # print, it carries no verdict, and it churns on every Lean edit.  Its
        # count is kept in the header so the denominator is not lost.
        keep = [f for f in findings if f["severity"] in ("CRITICAL", "major")]
        json.dump({
            "schema": "lean-borrowed-name/v1",
            "producer": "scripts/lean-borrowed-name-audit.py",
            "counts": {"critical": len(crit), "major": len(major),
                       "advisory_not_persisted": len(adv), "total": len(findings)},
            "note": ("High-recall candidate generator. A CRITICAL is a candidate, "
                     "not a verdict; the genuine/legit call is an agent call per "
                     "AGENTS.md 3b-tax. Advisory rows are counted but not stored."),
            "findings": keep,
        }, open(out, "w"), indent=2)
        print(f"wrote {out} ({len(keep)} rows; {len(adv)} advisory counted, not stored)")
    return 1 if (strict and crit) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
