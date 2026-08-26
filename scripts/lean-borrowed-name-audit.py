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

DEFAULT_ROOTS = [
    "content/quantum-observable-universe",
    "content/unital-groebner-bases",
    "content/fred2005-formal-groups",
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
    r"cosmetic|bookkeeping|no mathematical content|says nothing",
    re.I)

DECL = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*"
    r"(theorem|lemma|example|def|abbrev|structure|class|inductive|instance)\s+"
    r"([A-Za-z_][A-Za-z0-9_'.]*)")
PROVABLE = {"theorem", "lemma", "example"}
IDENT = re.compile(r"[A-Za-z_][A-Za-z0-9_']*(?:\.[A-Za-z_][A-Za-z0-9_']*)*")

# Lean keywords / tactics that are not declarations.
NOISE = {
    "by", "at", "fun", "let", "have", "show", "from", "with", "do", "then",
    "else", "if", "match", "this", "forall", "exists", "in", "where", "of",
    "Type", "Prop", "Sort", "sorry", "rfl", "and", "or", "not", "iff",
}


def blank_comments(src: str) -> str:
    """Blank out `--` comments and `/- -/` blocks, PRESERVING every newline.

    Line-preserving is load-bearing: declaration line numbers are used to find
    the docstring in the ORIGINAL source, so a stripper that deletes lines
    silently mis-aligns every docstring lookup (it did, and the selftest caught
    it).  Blanking also stops a `theorem ...` line quoted inside a docstring
    from being parsed as a declaration.
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
    """Split a decl body at the top-level `:=` — returns (statement, proof)."""
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


def decl_spans(src: str):
    """Yield (kind, name, header_line_no, body_text) for each top-level decl."""
    lines = src.split("\n")
    hits = []
    for idx, ln in enumerate(lines):
        m = DECL.match(ln)
        if m:
            hits.append((idx, m.group(1), m.group(2)))
    for k, (idx, kind, name) in enumerate(hits):
        end = hits[k + 1][0] if k + 1 < len(hits) else len(lines)
        yield kind, name, idx + 1, "\n".join(lines[idx:end])


def docstring_before(lines: list[str], idx0: int) -> str:
    """The `/-- ... -/` (or `/-! ... -/`) block immediately above line idx0."""
    j = idx0 - 2
    while j >= 0 and (lines[j].lstrip().startswith("--") or not lines[j].strip()):
        j -= 1
    if j < 0 or not lines[j].rstrip().endswith("-/"):
        return ""
    k = j
    while k >= 0 and not (lines[k].lstrip().startswith("/--")
                          or lines[k].lstrip().startswith("/-!")):
        k -= 1
    return "\n".join(lines[max(k, 0):j + 1]) if k >= 0 else ""


BINDER = re.compile(r"[({\u2983\[]\s*([^:()\[\]{}]*?)\s*:")


def binder_names(stmt: str) -> set[str]:
    """Names bound by `(x y : T)` / `{x : T}` / `[inst : C]` groups."""
    out: set[str] = set()
    for m in BINDER.finditer(stmt):
        for tok in m.group(1).split():
            if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_']*", tok):
                out.add(tok)
    return out


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
        local_defs = {n.split(".")[-1]
                      for k, n, _, _ in decl_spans(code)
                      if k in ("def", "abbrev", "structure", "class", "inductive")}
        if not local_defs:
            continue
        for kind, name, lineno, body in decl_spans(code):
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
            steps = [t.strip() for t in re.split(r"[;\n<;>]|\bthen\b", proof)
                     if t.strip() and t.strip() not in ("by",)]
            steps = [re.sub(r"^by\s+", "", t) for t in steps]
            cheap = bool(steps) and all(CHEAP_TACTIC.match(t) for t in steps) \
                and len(steps) <= 4 and not ext_lemmas
            if overclaim and cheap and not disclaimed:
                sev = "CRITICAL"
            elif cheap and not disclaimed:
                sev = "major"
            else:
                sev = "advisory"
            findings.append({
                "file": os.path.relpath(p, base),
                "line": lineno,
                "decl": name,
                "kind": kind,
                "severity": sev,
                "overclaim": overclaim,
                "cheap_proof": cheap,
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
    adv = [f for f in findings if f["severity"] != "CRITICAL"]
    for f in findings:
        print(f"{f['severity']:8s} {f['file']}:{f['line']}  {f['decl']}")
        print(f"         borrowed : {', '.join(f['borrowed'])}")
        print(f"         local    : {', '.join(f['local_defs_in_statement'])}")
        if f["external_lemmas_in_proof"]:
            print(f"         proof cites: {', '.join(f['external_lemmas_in_proof'][:6])}")
        print(f"         stmt     : {f['statement'][:160]}")
    print(f"\nborrowed-name audit: {len(crit)} CRITICAL, {len(adv)} advisory")
    if out:
        json.dump({"schema": "lean-borrowed-name/v1", "findings": findings},
                  open(out, "w"), indent=2)
        print(f"wrote {out}")
    return 1 if (strict and crit) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
