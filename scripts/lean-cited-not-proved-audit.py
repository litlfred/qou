#!/usr/bin/env python3
"""lean-cited-not-proved-audit.py — the cited-not-proved surface, measured on TERMS.

Every earlier count of this corpus's `sorry`s was a raw grep, and a raw grep cannot
tell a proof term from the word appearing in a docstring.  Measured here: a plain
`git grep sorry` over the Lean tree returns 76 hits; **21** of them are real terms.
The other 55 are prose — headers reading "isolated to the single cited sorry",
docstrings reading "sorry'd `d_1`", and this repo's many "sorry-free" claims.

So this script strips Lean comments and string literals FIRST, with a real scanner
that handles nested `/- -/`, doc comments `/-- -/`, `--` to end of line, and string
escapes, then reports what is left.

Three categories, because they are three different epistemic states and the corpus
conflates them:

  sorry   — the gap is in the TERM.  `#print axioms` shows `sorryAx`; the
            declaration is a lie about itself until it is filled.
  axiom   — the gap is ASSERTED.  `#print axioms` names it, so it is visible, but
            nothing constrains it.
  class   — the gap is in the SIGNATURE (a §3b conditional class with no instance).
            `#print axioms` comes back CLEAN and the honesty lives entirely in the
            fact that no instance can be found.  This is the category a reader is
            most likely to mistake for a proof.

Usage:
  scripts/lean-cited-not-proved-audit.py [--rev REV] [--json OUT] [--kind sorry|axiom|all]
"""
from __future__ import annotations
import argparse, json, re, subprocess, sys
from pathlib import Path

LEAN_ROOT = "content/quantum-observable-universe/lean"
# The Lake LIBRARY tree above is NOT the whole Lean corpus.  Content-block
# SIBLINGS live beside their `.ts`/`.md` under `content/<paper>/<chapter>/`,
# outside the Lake globs -- and under the AGENTS.md 0a resolution order a
# sibling resolves BEFORE the library, so those are the declarations a content
# block's `lean.ref` actually points at.
#
# Scanning only the library silently under-reported this corpus.  Measured on
# origin/main 2026-09-04: 944 sibling files carrying 8 real `sorry` terms and
# 148 `axiom` declarations, against 0 and 19 in the library.  Every "corpus-wide"
# figure this script produced before that date was library-only -- including a
# "0 sorries" claim that was wrong for the corpus and right only for the tree
# it happened to walk.
CONTENT_ROOT = "content"


def scan_paths(rev, root):
    """Every `.lean` file in the corpus: the Lake library AND the siblings."""
    if rev:
        listing = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", rev, CONTENT_ROOT],
            capture_output=True, text=True).stdout.split()
        return sorted(f for f in listing if f.endswith(".lean"))
    return sorted(
        str(p.relative_to(root))
        for p in (root / CONTENT_ROOT).rglob("*.lean")
        if ".lake" not in p.parts)


def is_sibling(rel: str) -> bool:
    """A content-block sibling: under `content/`, but not in a Lake tree."""
    return "/lean/" not in rel


def display(rel: str) -> str:
    """Library files keep their `QOU/...` path; siblings keep enough to locate."""
    return rel[len(LEAN_ROOT) + 1:] if rel.startswith(LEAN_ROOT + "/") else rel


def strip_comments(src: str) -> str:
    """Blank out Lean comments and string literals, preserving offsets and newlines."""
    out = list(src)
    i, n = 0, len(src)
    depth = 0                      # nested /- -/ depth
    in_line = False                # inside a -- comment
    in_str = False                 # inside a "..." literal
    while i < n:
        c = src[i]
        nxt = src[i + 1] if i + 1 < n else ""
        if in_line:
            if c == "\n":
                in_line = False
            else:
                out[i] = " "
            i += 1
        elif depth:
            if c == "/" and nxt == "-":
                depth += 1
                out[i] = out[i + 1] = " "
                i += 2
            elif c == "-" and nxt == "/":
                depth -= 1
                out[i] = out[i + 1] = " "
                i += 2
            else:
                if c != "\n":
                    out[i] = " "
                i += 1
        elif in_str:
            if c == "\\":
                out[i] = " "
                if i + 1 < n and src[i + 1] != "\n":
                    out[i + 1] = " "
                i += 2
            elif c == '"':
                in_str = False
                out[i] = " "
                i += 1
            else:
                if c != "\n":
                    out[i] = " "
                i += 1
        else:
            if c == "-" and nxt == "-":
                in_line = True
                out[i] = out[i + 1] = " "
                i += 2
            elif c == "/" and nxt == "-":
                depth = 1
                out[i] = out[i + 1] = " "
                i += 2
            elif c == '"':
                in_str = True
                out[i] = " "
                i += 1
            else:
                i += 1
    return "".join(out)


TOKEN = re.compile(r"(?<![A-Za-z0-9_'.!?])(sorry|sorryAx)(?![A-Za-z0-9_'])")
AXIOM = re.compile(r"^\s*axiom\s+([A-Za-z0-9_'.]+)", re.M)
DECL = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)*(?:private\s+|protected\s+|noncomputable\s+|partial\s+|unsafe\s+)*"
    r"(theorem|lemma|def|abbrev|instance|example|structure|class|inductive)\s+([A-Za-z0-9_'.]+)?",
    re.M,
)


def decl_before(src: str, pos: int):
    """Name and kind of the declaration a given offset sits inside."""
    best = None
    for m in DECL.finditer(src, 0, pos):
        best = m
    if not best:
        return ("<none>", "<none>")
    return (best.group(1), best.group(2) or "<anonymous>")


def ref_above(raw_lines: list[str], line_idx: int, window: int = 25):
    """Nearest `-- Ref:` citation above a line (the AGENTS.md §1 requirement)."""
    for j in range(line_idx, max(-1, line_idx - window), -1):
        s = raw_lines[j].strip()
        if s.startswith("-- Ref:"):
            return s[len("-- Ref:"):].strip()
    return None



CLASS_DECL = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)*(?:private\s+|protected\s+)?class\s+([A-Za-z0-9_'.]+)", re.M)
# An instance/def/theorem whose TYPE mentions the class name: the inhabitant.
def result_type(code: str, pos: int) -> str:
    """The result type of a declaration starting at `pos`.

    Two phases, and the split is the point.

    * **Before** the top-level colon everything bracketed is a BINDER — `(x : T)`,
      `{X : C}`, `[Category C]`, and attribute payloads like `(priority := 100)`.
      Those are consumers, and their contents must be discarded or every
      `[C M]` hypothesis would read as an inhabitant of `C`.
    * **After** the colon, parentheses are part of the TYPE — `Nonempty (PagedSS R page)`
      inhabits `PagedSS`, so their contents must be kept.

    Ordering matters twice over.  Brackets are handled before the body marker is
    looked for, because `instance (priority := 100) name … : C` puts a `:=`
    inside parentheses; a scanner that searches for `:=` first truncates the
    signature and reports a real inhabitant as missing.  That exact bug called
    `BalancedCategory` and `RibbonCategory` uninhabited when both carry an
    `ofSymmetric` instance — see `--selftest`, which pins both directions.
    """
    n = min(len(code), pos + 4000)
    i, depth = pos, 0
    # phase 1: find the top-level colon, discarding binders
    while i < n:
        c = code[i]
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth = max(0, depth - 1)
        elif depth == 0:
            if code.startswith(":=", i):
                return ""                      # a body with no ascribed type
            if c == ":":
                i += 1
                break
            if c == "\n" and re.match(
                    r"\n(?:theorem|lemma|def|instance|abbrev|structure|class|inductive|end|namespace)",
                    code[i:]):
                return ""
        i += 1
    else:
        return ""
    # phase 2: accumulate the type, keeping bracketed subterms
    out, depth = [], 0
    while i < n:
        c = code[i]
        if c in "([{":
            depth += 1
        elif c in ")]}":
            if depth == 0:
                break
            depth -= 1
        elif depth == 0:
            if code.startswith(":=", i):
                break
            if code.startswith("where", i) and (i + 5 >= n or not code[i + 5].isalnum()):
                break
            if c == "\n" and re.match(
                    r"\n(?:theorem|lemma|def|instance|abbrev|structure|class|inductive|end|namespace|open|section|variable|@\[)",
                    code[i:]):
                break
        out.append(" " if c == "\n" else c)
        i += 1
    return "".join(out)


def build_provider_index(all_code: dict[str, str]) -> dict[str, list]:
    """Index every declaration by the identifiers in its RESULT TYPE.

    A mention inside a BINDER (`[C M]`) is a *consumer*; a mention after the
    top-level colon is a *provider*.  `result_type` drops binders, so only
    providers are indexed.

    Both `instance` and `def` count as inhabitants: this corpus deliberately
    demotes trivial witnesses from `instance` to `def` (PagedSpectralSequence.lean
    gives the reason), so a `def` inhabitant is still an inhabitant — merely
    invisible to typeclass resolution.
    """
    decl = re.compile(
        r"^[ \t]*(?:@\[[^\]]*\]\s*)*(?:private\s+|protected\s+|noncomputable\s+|partial\s+|unsafe\s+)*"
        r"(instance|def|theorem|abbrev)\b", re.M)
    ident = re.compile(r"[A-Za-z_][A-Za-z0-9_'.]*")
    index: dict[str, list] = {}
    for f, code in all_code.items():
        for m in decl.finditer(code):
            res = result_type(code, m.end())
            if not res:
                continue
            line = code.count("\n", 0, m.start()) + 1
            for sym in ident.findall(res):
                index.setdefault(sym.split(".")[-1], []).append((f, line, m.group(1)))
    return index


SELFTEST = [
    # (source, class name, expected-inhabited)
    ("instance (priority := 100) ofSymmetric (C : Type*) [Category C] : BalancedCategory C where\n  x := 1\n",
     "BalancedCategory", True),
    ("instance foo :\n    QOU.Mass.TowerGeometricLowerBound wStd r c 3 where\n  a := b\n",
     "TowerGeometricLowerBound", True),
    ("theorem t {X : C} [RibbonCategory C] (h : X = X) : X = X := rfl\n",
     "RibbonCategory", False),          # binder only — a consumer, not a provider
    ("def canonicalTrivial (R : Type u) : GBFiltrationCollapsesAtE2 R where\n  ss := s\n",
     "GBFiltrationCollapsesAtE2", True),   # a `def` inhabitant still inhabits
    ("theorem nonempty_it : Nonempty (PagedSS R page) := ⟨s⟩\n",
     "PagedSS", True),                  # reached through Nonempty
    ("class Lonely (C : Type*) where\n  f : C -> C\n",
     "Lonely", False),
]


PROP_SELFTEST = [
    # (source, field, expected shape) — the two shapes that wear the same syntax
    ("class StandardYoungCount (n : Nat) where\n"
     "  dim : Nat -> Nat\n"
     "  squares_sum_factorial : Prop\n"
     "  squares_sum_holds : squares_sum_factorial\n",
     "squares_sum_factorial", "self_nominating"),
    ("class AtomLike where\n"
     "  stable : Prop\n"
     "  IsFullOfCurls : Prop\n"
     "  IsNobleGas : Prop\n"
     "  claim_noble_iff_curls : stable -> (IsNobleGas <-> IsFullOfCurls)\n",
     "IsNobleGas", "parameterised"),
    # `stable` appears only as an ANTECEDENT, so it is parameterised too
    ("class AtomLike where\n"
     "  stable : Prop\n"
     "  IsFullOfCurls : Prop\n"
     "  IsNobleGas : Prop\n"
     "  claim_noble_iff_curls : stable -> (IsNobleGas <-> IsFullOfCurls)\n",
     "stable", "parameterised"),
]



# A self-nominating witness is a defect only when a proof term PROJECTS it.
# Case 1 is the `B1TorusKnotRowsTheorem` shape -- two named literature results
# carried as opaque `Prop`s and fed straight into the conclusion.  Case 2 is the
# `BringWPlaneMonodromy` shape -- an open geometric identification carried as an
# input, with the file's theorem deriving from a DIFFERENT, content-bearing
# field.  Case 3 pins the scoping bug these cases were written to catch: the
# consuming theorem sits AFTER the carrier, and an earlier version searched only
# the text outside the carrier block, which runs to EOF when nothing follows it.
CONSUMED_SELFTEST = [
    ("""class C where
  bloch_suslin : Prop
  h_bloch_suslin : bloch_suslin
  concl : bloch_suslin -> P

theorem t [ctx : C] : P := ctx.concl ctx.h_bloch_suslin
""", "bloch_suslin", True),
    ("""class D where
  M : Matrix (Fin 2) (Fin 2) Real
  unimodular : M.det = 1
  is_seifert : Prop
  seifert_holds : is_seifert

theorem u [self : D] : self.M * self.M = self.M.trace * self.M - 1 :=
  unimodular_two_recurrence self.M self.unimodular
""", "is_seifert", False),
    ("""class E where
  claim : Prop
  h_claim : claim
  impl : claim -> Q

theorem v [ctx : E] : Q := ctx.impl ctx.h_claim
""", "claim", True),
]

def selftest() -> int:
    bad = 0
    for src, field, want in PROP_SELFTEST:
        got = {e["field"]: e["shape"] for e in prop_valued_fields(strip_comments(src))}
        g = got.get(field, "<missing>")
        ok = "ok " if g == want else "FAIL"
        if g != want:
            bad += 1
        print(f"  [{ok}] {field}: shape={g} expected={want}")
    # The CROSS-FILE path: the same carrier, with no consumer in its own file,
    # is `unconsumed` file-locally and `consumed` once the corpus set carries
    # the witness.  Neither answer is reachable from the other source alone.
    _xf = """class F where
  claim : Prop
  h_claim : claim
  impl : claim -> Q
"""
    for projected, want in ((None, False), ({"h_claim"}, True)):
        got = {e["field"]: e.get("consumed")
               for e in prop_valued_fields(strip_comments(_xf), projected)}
        g = got.get("claim", "<missing>")
        ok = "ok " if g == want else "FAIL"
        if g != want:
            bad += 1
        label = "corpus" if projected else "file-local"
        print(f"  [{ok}] claim ({label}): consumed={g} expected={want}")
    for src, field, want in CONSUMED_SELFTEST:
        got = {e["field"]: e.get("consumed") for e in prop_valued_fields(strip_comments(src))}
        g = got.get(field, "<missing>")
        ok = "ok " if g == want else "FAIL"
        if g != want:
            bad += 1
        print(f"  [{ok}] {field}: consumed={g} expected={want}")
    for src, cls, want in SELFTEST:
        idx = build_provider_index({"t.lean": strip_comments(src)})
        got = bool(idx.get(cls.split(".")[-1]))
        ok = "ok " if got == want else "FAIL"
        if got != want:
            bad += 1
        print(f"  [{ok}] {cls}: inhabited={got} expected={want}")
    print("selftest FAILED" if bad else "selftest passed")
    return 1 if bad else 0


# A dotted projection `ctx.foo` / `self.foo_holds` -- how a witness is USED.
# Field DECLARATIONS are `name : type` and never dotted, so this cannot match one.
PROJECTION = re.compile(r"\.\s*([A-Za-z_][A-Za-z0-9_']*)")

# A field whose TYPE is literally `Prop`: the instance chooses the proposition.
PROP_FIELD = re.compile(r"^([ \t]+)([a-zA-Z_][A-Za-z0-9_']*)[ \t]*:[ \t]*Prop[ \t]*$", re.M)
CARRIER = re.compile(r"^[ \t]*(?:@\[[^\]]*\]\s*)*(?:private\s+|protected\s+)?(class|structure)\s+([A-Za-z0-9_'.]+)", re.M)


def carrier_blocks(code: str):
    """Split the file into (carrier name, kind, start, end) blocks by indentation."""
    out = []
    for m in CARRIER.finditer(code):
        nxt = CARRIER.search(code, m.end())
        out.append((m.group(2), m.group(1), m.start(),
                    nxt.start() if nxt else len(code)))
    return out


FIELD = re.compile(r"^([ \t]+)([a-zA-Z_][A-Za-z0-9_']*)[ \t]*:[ \t]*([^\n]*)$", re.M)


def prop_valued_fields(code: str, projected: set | None = None):
    """Fields declared `name : Prop`, SPLIT by whether the carrier proves them directly.

    Two shapes wear the same syntax and they are not the same defect.  Conflating
    them inflates the count, which this scan did until a false positive on
    `QOU/Archimedean/noble_gas_characterization.lean` exposed it.

    **self_nominating** — the defect.  A companion field's type is the `Prop`
    field itself::

        squares_sum_factorial : Prop
        squares_sum_holds : squares_sum_factorial

    An instance supplies both the proposition and its proof, so
    `:= True; := trivial` discharges it and the carrier constrains nothing.
    Worse than a bare `True` field (which `AGENTS.md` §3b-tax's
    `proof-claims-unencoded` flags) because it does not even say WHICH nothing.

    **parameterised** — legitimate, and NOT a defect.  The `Prop` field is an
    abstract predicate used as a *component* of some other field's statement::

        IsNobleGas : Prop
        IsFullOfCurls : Prop
        claim_noble_iff_curls : stable -> (IsNobleGas <-> IsFullOfCurls)

    Here the content is the relation, and the predicates are parameters of it —
    the same move as taking `(P : alpha -> Prop)` as an argument.  An instance
    choosing `True` for both satisfies a *weaker instance*, not a vacuous class:
    the iff still has to hold for whatever it chose.

    The discriminator is therefore whether the carrier proves the field
    DIRECTLY, not whether the field is typed `Prop`.

    **And a self-nominating field is a defect only if something PROJECTS it.**
    Third refinement, from a false positive on
    `QOU/BraidKnot/BringWPlaneMonodromy.lean`::

        is_seifert_gauss_manin : Prop
        seifert_holds : is_seifert_gauss_manin

    is self-nominating by the rule above, yet the file is exemplary: the
    proposition is a genuinely-open *geometric identification* deliberately left
    abstract, and the file's one theorem derives from the `unimodular` field via
    a proved lemma, explicitly NOT from `seifert_holds`.  That is the honest
    `AGENTS.md` §3b conjecture-class pattern — an open input carried as an
    input.

    Contrast `QOU/AppendixSurreals/B1TorusKnotRowsTheorem.lean`, where
    `h_bloch_suslin` and `h_garoufalidis_le` are fed straight into
    `b1_from_tate_rationality` to produce the theorem's conclusion.  There the
    witnesses ARE the proof, and two named literature results (Bloch-Suslin,
    Garoufalidis-Le) are laundered through opaque `Prop`s.

    So `consumed` marks the ones where a proof term in the same file mentions
    the witness field; `unconsumed` marks a carried open input.  Only
    `consumed` is actionable.
    """
    out = []
    for name, kind, lo, hi in carrier_blocks(code):
        block = code[lo:hi]
        fields = [(m.group(2), m.group(3).strip(), m.start())
                  for m in FIELD.finditer(block)]
        prop_names = {f for f, ty, _ in fields if ty == "Prop"}
        # a field whose ENTIRE type is another field's name proves it directly
        proved_directly = {ty for f, ty, _ in fields if ty in prop_names}
        # witness field(s) for each self-nominating Prop field
        witnesses = {}
        for f, ty, _ in fields:
            if ty in prop_names:
                witnesses.setdefault(ty, []).append(f)
        for f, ty, off in fields:
            if ty != "Prop":
                continue
            shape = "self_nominating" if f in proved_directly else "parameterised"
            entry = {
                "line": code.count("\n", 0, lo + off) + 1,
                "field": f, "carrier": name, "carrier_kind": kind,
                "shape": shape,
            }
            if shape == "self_nominating":
                # A witness is CONSUMED when some proof term projects it
                # (`ctx.h_foo`, `self.foo_holds`, ...).
                #
                # Search the WHOLE file, not the region outside the carrier:
                # `carrier_blocks` runs a block to EOF when nothing follows it,
                # which excluded the very theorem that consumes the witness
                # (measured on B1TorusKnotRowsTheorem.lean, which reported
                # False against a true True).  A dotted projection cannot occur
                # in a field DECLARATION -- those are `name : type` -- so the
                # whole-file search introduces no false positive.
                #
                # And prefer `projected`, the CORPUS-WIDE set of dotted names,
                # when the caller supplies it: a class declared in one file can
                # be consumed from another, and a file-local search reports
                # that as `unconsumed`, i.e. UNDER-counts the defect.  Measured
                # 2026-09-04 on all 15 unconsumed witnesses: none is projected
                # anywhere in the corpus, so the file-local answer happened to
                # be right -- but it was right by luck, not by construction.
                # Prompted by a sibling agent on #6540, whose own count moved
                # four times and never because a number looked wrong.
                wits = witnesses.get(f, [])
                if projected is not None:
                    used = any(w in projected for w in wits)
                else:
                    used = any(re.search(r"\.\s*" + re.escape(w) + r"\b", code)
                               for w in wits)
                entry["witnesses"] = witnesses.get(f, [])
                entry["consumed"] = used
            out.append(entry)
    return out


def git_show(rev: str, path: str) -> str | None:
    r = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rev", default="", help="git revision (default: working tree)")
    ap.add_argument("--json", default="")
    ap.add_argument("--kind", default="all",
                    choices=["sorry", "axiom", "class", "prop-field", "all"])
    ap.add_argument("--selftest", action="store_true",
                    help="run the known-positive/negative cases and exit")
    a = ap.parse_args()

    if a.selftest:
        return selftest()

    root = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                               capture_output=True, text=True).stdout.strip())
    files = scan_paths(a.rev, root)

    sorries, axioms, prose_hits = [], [], 0
    uninhabited_out: list = []
    prop_fields_out: list = []
    class_totals = {}
    for rel in sorted(files):
        raw = git_show(a.rev, rel) if a.rev else (root / rel).read_text(errors="replace")
        if raw is None:
            continue
        code = strip_comments(raw)
        raw_lines = raw.splitlines()

        prose_hits += len(TOKEN.findall(raw)) - len(TOKEN.findall(code))

        for m in TOKEN.finditer(code):
            li = code.count("\n", 0, m.start())
            kind, name = decl_before(code, m.start())
            sorries.append({
                "file": display(rel), "line": li + 1,
                "decl_kind": kind, "decl": name,
                "ref": ref_above(raw_lines, li),
            })
        for m in AXIOM.finditer(code):
            li = code.count("\n", 0, m.start())
            axioms.append({
                "file": display(rel), "line": li + 1,
                "axiom": m.group(1), "ref": ref_above(raw_lines, li),
            })

    print(f"scanned {len(files)} .lean files at {a.rev or '<working tree>'}\n")
    if a.kind in ("sorry", "all"):
        cited = sum(1 for s in sorries if s["ref"])
        print(f"REAL `sorry` TERMS: {len(sorries)}   ({cited} cited, "
              f"{len(sorries) - cited} uncited)" + (" — UNCITED sorries are an AGENTS.md §1 review failure" if len(sorries) - cited else ""))
        print(f"  (a raw grep also matches {prose_hits} occurrences in comments/strings)")
        for s in sorries:
            tag = "cited  " if s["ref"] else "UNCITED"
            print(f"  {tag} {s['file']}:{s['line']}  {s['decl_kind']} {s['decl']}")
            if s["ref"]:
                print(f"          Ref: {s['ref'][:100]}")
    if a.kind in ("axiom", "all"):
        cited = sum(1 for x in axioms if x["ref"])
        print(f"\nREAL `axiom` DECLARATIONS: {len(axioms)}   ({cited} cited)")
        for x in axioms:
            print(f"  {x['file']}:{x['line']}  {x['axiom']}")


    if a.kind in ("class", "all"):
        all_code, classes = {}, []
        for rel in sorted(files):
            raw = git_show(a.rev, rel) if a.rev else (root / rel).read_text(errors="replace")
            if raw is None:
                continue
            code = strip_comments(raw)
            all_code[display(rel)] = code
            for m in CLASS_DECL.finditer(code):
                classes.append({"file": display(rel),
                                "line": code.count("\n", 0, m.start()) + 1,
                                "class": m.group(1)})
        index = build_provider_index(all_code)
        uninhabited, inhabited = [], 0
        for c in classes:
            prov = index.get(c["class"].split(".")[-1], [])
            if prov:
                inhabited += 1
            else:
                uninhabited.append(c)
        print(f"\nCLASSES: {len(classes)} declared, {inhabited} with an inhabitant, "
              f"{len(uninhabited)} with NO instance or def anywhere")
        print("  A class with no inhabitant is the cited-not-proved category whose")
        print("  `#print axioms` comes back CLEAN — the gap is in the signature.")
        for c in uninhabited:
            print(f"  {c['file']}:{c['line']}  class {c['class']}")
        uninhabited_out.extend(uninhabited)
        class_totals.update(declared=len(classes), inhabited=inhabited,
                            uninhabited=len(uninhabited))


    if a.kind in ("prop-field", "all"):
        pf = []
        # PASS 1 -- every dotted projection anywhere in the corpus.  A class
        # declared in one file can be consumed from another, and a file-local
        # search reports that as `unconsumed`, i.e. UNDER-counts the defect.
        sources = {}
        projected: set = set()
        for rel in sorted(files):
            raw = git_show(a.rev, rel) if a.rev else (root / rel).read_text(errors="replace")
            if raw is None:
                continue
            sources[rel] = strip_comments(raw)
            projected.update(PROJECTION.findall(sources[rel]))
        # PASS 2 -- classify, resolving `consumed` against the corpus set.
        for rel, code in sources.items():
            for e in prop_valued_fields(code, projected):
                e["file"] = display(rel)
                pf.append(e)
        selfnom = [e for e in pf if e["shape"] == "self_nominating"]
        param = [e for e in pf if e["shape"] == "parameterised"]
        print(f"\nPROP-VALUED FIELDS: {len(pf)} total — and they are TWO shapes, not one")
        print(f"  self_nominating {len(selfnom):3d}  the DEFECT: a companion field proves it")
        print(f"                            directly, so the instance picks the claim AND")
        print(f"                            proves it. `:= True; := trivial` discharges it.")
        print(f"  parameterised   {len(param):3d}  NOT a defect: an abstract predicate used as a")
        print(f"                            COMPONENT of another field's statement. The content")
        print(f"                            is the relation; the predicate is its parameter.")
        for e in selfnom:
            print(f"  DEFECT {e['file']}:{e['line']}  {e['carrier_kind']} {e['carrier']} . {e['field']}")
        prop_fields_out.extend(pf)

    if a.json:
        Path(a.json).write_text(json.dumps(
            {"rev": a.rev or "working-tree", "files_scanned": len(files),
             "sorries": sorries, "axioms": axioms,
             "prose_occurrences": prose_hits,
             "class_totals": class_totals,
             "uninhabited_classes": uninhabited_out,
             "prop_valued_fields": prop_fields_out}, indent=2))
        print(f"\nwrote {a.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
