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


def selftest() -> int:
    bad = 0
    for src, cls, want in SELFTEST:
        idx = build_provider_index({"t.lean": strip_comments(src)})
        got = bool(idx.get(cls.split(".")[-1]))
        ok = "ok " if got == want else "FAIL"
        if got != want:
            bad += 1
        print(f"  [{ok}] {cls}: inhabited={got} expected={want}")
    print("selftest FAILED" if bad else "selftest passed")
    return 1 if bad else 0


def git_show(rev: str, path: str) -> str | None:
    r = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rev", default="", help="git revision (default: working tree)")
    ap.add_argument("--json", default="")
    ap.add_argument("--kind", default="all", choices=["sorry", "axiom", "class", "all"])
    ap.add_argument("--selftest", action="store_true",
                    help="run the known-positive/negative cases and exit")
    a = ap.parse_args()

    if a.selftest:
        return selftest()

    root = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                               capture_output=True, text=True).stdout.strip())
    if a.rev:
        listing = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", a.rev, LEAN_ROOT],
            capture_output=True, text=True).stdout.split()
        files = [f for f in listing if f.endswith(".lean")]
    else:
        files = [str(p.relative_to(root)) for p in (root / LEAN_ROOT).rglob("*.lean")]

    sorries, axioms, prose_hits = [], [], 0
    uninhabited_out: list = []
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
                "file": rel[len(LEAN_ROOT) + 1:], "line": li + 1,
                "decl_kind": kind, "decl": name,
                "ref": ref_above(raw_lines, li),
            })
        for m in AXIOM.finditer(code):
            li = code.count("\n", 0, m.start())
            axioms.append({
                "file": rel[len(LEAN_ROOT) + 1:], "line": li + 1,
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
            all_code[rel[len(LEAN_ROOT) + 1:]] = code
            for m in CLASS_DECL.finditer(code):
                classes.append({"file": rel[len(LEAN_ROOT) + 1:],
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

    if a.json:
        Path(a.json).write_text(json.dumps(
            {"rev": a.rev or "working-tree", "files_scanned": len(files),
             "sorries": sorries, "axioms": axioms,
             "prose_occurrences": prose_hits,
             "class_totals": class_totals,
             "uninhabited_classes": uninhabited_out}, indent=2))
        print(f"\nwrote {a.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
