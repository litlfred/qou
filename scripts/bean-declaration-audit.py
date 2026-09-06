#!/usr/bin/env python3
"""Find open beans whose cited Lean declaration is already proved.

WHY THIS EXISTS
===============

Measured 2026-09-06 (beans `sp00`, `qou-sxyr`): of the ten bricks in the Specht /
Okounkov-Vershik epic, **all ten were proved and axiom-clean, and six were still
recorded `todo`**. The epic itself sat `in-progress` while complete. Two of the
six -- the OV seminormal eigenvector and the Burnside identity -- were the
obvious next research targets in this repo, both labelled "Famous", and an agent
picking either up would have spent its opening hours re-deriving something
already in the tree.

Four of the ten *were* updated by hand when they closed. That asymmetry is the
diagnosis: closing a bean when its declaration lands is a manual step, so it
happens exactly as often as somebody remembers.

The population is large enough to be worth a check: **248 non-completed beans
cite 456 distinct `QOU.*` dotted identifiers.**

WHAT IT CHECKS, AND WHAT IT REFUSES TO
======================================

For each identifier cited by a non-completed bean, this resolves the owning
module from the source tree (exactly -- module name is the file path), then asks
Lean whether the constant exists and whether it depends on `sorryAx`.

Three rules, each of which cost this session something to learn:

* **Verify by artifact, not by parsing prose.** A grep for "sorry-free" in a
  docstring is the failure mode this exists to catch, not the check. The verdict
  is `#print axioms` on the proof term.

* **"Could not resolve" is a third state.** It is reported separately and never
  folded into either "still open" or "done". An identifier that does not resolve
  is usually a *renamed or deleted* declaration, which is its own finding -- and
  a module with no olean is not a module whose declarations are unproved.

* **A definition is not a theorem.** The first version flagged any resolvable
  constant as "proved", which inflated the count: `qou-6dzi` cites
  `Wedderburn.WedderburnDecomposition`, an `abbrev` for a type. It exists; that
  says nothing about whether the bean's work is done. Only `thmInfo` constants
  can make a bean a stale candidate.

* **A class binder means the check is NOT finished.** `sn_rational_specht_split`
  is axiom-clean *and* carries `[SnIsotypicSpechtSplit R]`, and is proved by
  unpacking that class's only field -- `X |- X`. It is nonetheless established,
  because an instance inhabits the class. Clean alone told neither story. So a
  flagged declaration whose type mentions an instance binder is reported as
  **REVIEW**, not as done; a human decides.

Usage
-----
    python3 scripts/bean-declaration-audit.py --emit > /tmp/probe.lean
    lean /tmp/probe.lean            # with LEAN_PATH set, see lean-direct-env.sh
    python3 scripts/bean-declaration-audit.py --report /tmp/probe.out

`--emit` writes the Lean probe; `--report` reads its output back and prints the
bean-level verdict. Split in two so the Lean step can be run under whatever
environment the caller already has, and so the expensive half is never run twice
by accident.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BEANS = ROOT / ".beans"
SRC = ROOT / "content/quantum-observable-universe/lean/QOU"
BUILD = ROOT / "content/quantum-observable-universe/lean/.lake/build/lib/lean/QOU"

DONE = {"completed", "done", "scrapped"}
IDENT = re.compile(r"\bQOU(?:\.[A-Za-z_][A-Za-z0-9_']*){2,}\b")


NS_RE = re.compile(r"^namespace\s+(\S+)", re.M)
DECL_RE = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+|"
    r"partial\s+|unsafe\s+)*"
    r"(?:theorem|lemma|def|abbrev|instance|structure|class|inductive|axiom|opaque)"
    r"\s+([A-Za-z_][A-Za-z0-9_'!?]*)", re.M)


def _scan_declarations(path: Path, mod: str):
    """Yield (fully-qualified name, module) for each declaration in one file.

    Tracks the enclosing `namespace` as it goes. The first version took the CROSS
    PRODUCT of every namespace in a file with every declaration in it, which
    manufactures names that do not exist: a file holding `namespace A … end A`
    followed by `namespace B … end B` produced `A.<declaration from B>`. Those
    phantom entries then matched *themselves* in the rename-drift shortlist,
    reporting `cites: X / near: X` for 10+ identifiers -- a tool inventing the
    evidence for its own finding. Found and fixed 2026-09-06.
    """
    stack: list[str] = []
    for line in path.read_text(errors="replace").splitlines():
        m = re.match(r"\s*namespace\s+(\S+)", line)
        if m:
            stack.append(m.group(1))
            continue
        if re.match(r"\s*end\s+\S+", line) and stack:
            stack.pop()
            continue
        d = DECL_RE.match(line)
        if d:
            ns = ".".join(stack) if stack else mod
            yield f"{ns}.{d.group(1)}", mod


def fullname_index() -> dict[str, str]:
    """Fully-qualified declaration name -> the module that declares it.

    The prefix rule (longest module prefix of the identifier) is exact when it
    fires, but fires less often than one would like: a declaration's NAMESPACE
    routinely differs from its module, and then no prefix of the name is a module
    at all. Measured 2026-09-06, that left 79 of 455 cited identifiers unresolved
    and so never probed -- and most of them exist, e.g. `QOU.Braiding.HeckeAlgebra`
    resolves as a full name while `QOU.Braiding` is not a module.

    Source-derived, and used ONLY to choose which module to import. The verdict
    still comes from Lean.
    """
    idx: dict[str, str] = {}
    for f in SRC.rglob("*.lean"):
        mod = "QOU." + str(f.relative_to(SRC))[:-5].replace("/", ".")
        for name, m in _scan_declarations(f, mod):
            idx.setdefault(name, m)
    return idx


def modules() -> set[str]:
    return {"QOU." + str(p.relative_to(SRC))[:-5].replace("/", ".")
            for p in SRC.rglob("*.lean")}


def has_olean(mod: str) -> bool:
    return (BUILD / (mod[len("QOU."):].replace(".", "/") + ".olean")).exists()


def owning_module(ident: str, mods: set[str]) -> str | None:
    """Longest strict prefix of `ident` that is a real module, or None.

    Exact rather than heuristic: a module's name IS its path under QOU/, so the
    prefix test cannot mistake a namespace for a module the way a guess would.
    """
    parts = ident.split(".")
    for cut in range(len(parts) - 1, 1, -1):
        cand = ".".join(parts[:cut])
        if cand in mods:
            return cand
    return None


def collect() -> tuple[dict[str, set[str]], dict[str, str]]:
    """(ident -> {bean ids citing it}, bean id -> status), open beans only."""
    cites: dict[str, set[str]] = {}
    status: dict[str, str] = {}
    for f in sorted(BEANS.glob("*.md")):
        txt = f.read_text(errors="replace")
        m = re.search(r"^status:\s*(\S+)", txt, re.M)
        st = (m.group(1) if m else "?").strip()
        if st in DONE:
            continue
        bid = f.name.split("--")[0]
        status[bid] = st
        for ident in set(IDENT.findall(txt)):
            # Lean identifiers may contain `'`, so the pattern also captures English
            # possessives out of prose -- "QOU.Hecke.Wedderburn's" was matched as a
            # name. Strip a trailing `'s`; a real Lean name ending that way is
            # vanishingly rare next to the prose it would otherwise pollute.
            if ident.endswith("'s"):
                ident = ident[:-2]
            cites.setdefault(ident, set()).add(bid)
    return cites, status


def classify_absent(idents: list[str], mods: set[str]) -> int:
    """Split unresolved identifiers into the three things they actually are.

    Measured 2026-09-06. Of 44 identifiers the probe reported ABSENT, **27** were
    simply somewhere else -- a declaration's namespace routinely differs from its
    module, so the longest-module-prefix rule imports the wrong file. That is a
    limitation of the resolver, not a defect in the corpus.

    Of the remaining 17, most are NOT defects either, and this is the distinction
    worth keeping: **a bean that names a declaration it intends to CREATE should
    cite a name that does not exist yet.** That is correct usage. Reporting those
    as "cites a missing declaration" would manufacture 12 findings out of ordinary
    planning.

    What is left is rename drift -- a bean tracking a name that has since changed,
    which can never be checked again because nothing resolves it. The fuzzy match
    below proposes those; it OVER-FIRES (it matched a module name against a
    declaration inside that module), so its output is a shortlist for a human, not
    a verdict.
    """
    import difflib
    fullnames = set(fullname_index())

    drift, planned = [], []
    for ident in sorted(idents):
        near = difflib.get_close_matches(ident, fullnames, n=1, cutoff=0.90)
        (drift if near else planned).append((ident, near[0] if near else None))

    print(f"unresolved identifiers: {len(idents)}\n")
    print(f"RENAME-DRIFT SHORTLIST ({len(drift)}) -- a near-identical name exists.")
    print("  Shortlist, not verdict: this matcher over-fires (a module name scores")
    print("  highly against a declaration inside it). Read each before acting.")
    for ident, near in drift:
        print(f"    cites : {ident}\n    near  : {near}")
    print()
    print(f"NO NEAR MATCH ({len(planned)}) -- most likely a declaration the bean")
    print("  intends to CREATE. That is correct usage, not a defect.")
    for ident, _ in planned:
        print(f"    {ident}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--emit", action="store_true", help="write the Lean probe to stdout")
    ap.add_argument("--emit-dir", type=Path, metavar="DIR",
                    help="write ONE probe per owning module into DIR. Preferred over "
                         "--emit: a single probe importing every owning module can fail "
                         "outright, because the corpus contains modules that declare the "
                         "same constant and so cannot be co-imported (found 2026-09-06: "
                         "QOU.Archimedean.R_q is declared by both GroundRing and "
                         "WeierstrassProjection). One probe per module sidesteps that "
                         "and degrades per-module instead of all-or-nothing")
    ap.add_argument("--report", type=Path, help="read the probe's output and report")
    ap.add_argument("--limit", type=int, default=0, help="cap identifiers probed")
    ap.add_argument("--classify-absent", type=Path, metavar="PROBE_OUT",
                    help="read a probe output and split its ABSENT lines into "
                         "rename-drift vs planned-work. Takes the PROBE OUTPUT, not "
                         "the pre-probe bucket: an identifier that never resolved to "
                         "a module was never asked about, so it is not evidence of "
                         "anything")
    args = ap.parse_args()

    cites, status = collect()
    mods = modules()
    fnidx = fullname_index()

    resolvable: dict[str, str] = {}
    unbuilt: list[tuple[str, str]] = []
    no_module: list[str] = []
    for ident in sorted(cites):
        if ident in mods:            # the identifier IS a module, not a declaration
            continue
        # The index FIRST, the prefix rule as fallback. The prefix rule is a guess
        # -- "the longest prefix that happens to be a module" -- and it wins for the
        # wrong reason whenever a namespace shares a name with a module that does
        # not declare the constant. Measured case: `JucysMurphy.syt_adjacentSwap_connected`
        # is declared in module `JucysMurphyOV` under namespace `JucysMurphy`; the
        # prefix rule imported `JucysMurphy`, found nothing, and reported ABSENT for
        # a theorem that exists. The index is derived from actual declarations, so
        # it knows the declaring module and should be consulted first.
        owner = fnidx.get(ident) or owning_module(ident, mods)
        if owner is None:
            no_module.append(ident)
        elif not has_olean(owner):
            unbuilt.append((ident, owner))
        else:
            resolvable[ident] = owner

    if args.emit:
        items = sorted(resolvable.items())
        if args.limit:
            items = items[:args.limit]
        for owner in sorted({o for _, o in items}):
            print(f"import {owner}")
        print("\nopen Lean in\nrun_cmd do\n  let env ← Lean.getEnv")
        for ident, _ in items:
            print(f'  match env.find? `{ident} with')
            print(f'  | none => Lean.logInfo m!"ABSENT {ident}"')
            print(f'  | some ci =>')
            print(f'    let (_, s) := ((Lean.CollectAxioms.collect `{ident}).run env).run '
                  '{}')
            print(f'    let binder := (toString ci.type).splitOn "[inst" |>.length > 1')
            print(f'    if s.axioms.contains ``sorryAx then '
                  f'Lean.logInfo m!"SORRY {ident}"')
            print(f'    else if binder then Lean.logInfo m!"REVIEW {ident}"')
            print(f'    else Lean.logInfo m!"CLEAN {ident}"')
        return 0

    if args.emit_dir:
        args.emit_dir.mkdir(parents=True, exist_ok=True)
        by_mod: dict[str, list[str]] = {}
        for ident, owner in sorted(resolvable.items()):
            by_mod.setdefault(owner, []).append(ident)
        for owner, idents in sorted(by_mod.items()):
            lines = [f"import {owner}", "",
                     "-- Instance-binder detection walks the forall telescope's binderInfo.",
                     "-- A string test on the pretty-printed type was tried first and is",
                     "-- wrong twice over: it does not parse without parentheses, and the",
                     "-- printed form is not a reliable carrier of binder info anyway.",
                     "partial def hasInstBinder : Lean.Expr → Bool",
                     "  | .forallE _ _ b bi => bi.isInstImplicit || hasInstBinder b",
                     "  | _ => false", "",
                     "open Lean in", "run_cmd do",
                     "  let env ← Lean.getEnv"]
            for ident in idents:
                lines += [
                    f'  match env.find? `{ident} with',
                    f'  | none => Lean.logInfo m!"ABSENT {ident}"',
                    f'  | some ci =>',
                    f'    let (_, s) := ((Lean.CollectAxioms.collect `{ident}).run env).run {{}}',
                    f'    if !(ci matches .thmInfo _) then Lean.logInfo m!"DEF {ident}"',
                    f'    else if s.axioms.contains ``sorryAx then Lean.logInfo m!"SORRY {ident}"',
                    f'    else if hasInstBinder ci.type then Lean.logInfo m!"REVIEW {ident}"',
                    f'    else Lean.logInfo m!"CLEAN {ident}"',
                ]
            (args.emit_dir / (owner + ".lean")).write_text("\n".join(lines) + "\n")
        print(f"wrote {len(by_mod)} probe file(s) to {args.emit_dir}")
        return 0

    if args.classify_absent:
        absent = [ln.strip().split("info: ")[-1][len("ABSENT "):].strip()
                  for ln in args.classify_absent.read_text(errors="replace").splitlines()
                  if ln.strip().split("info: ")[-1].startswith("ABSENT ")]
        return classify_absent(sorted(set(absent)), mods)

    if args.report:
        verdict: dict[str, str] = {}
        for line in args.report.read_text(errors="replace").splitlines():
            line = line.strip().split("info: ")[-1]
            for tag in ("CLEAN", "REVIEW", "SORRY", "ABSENT", "DEF"):
                if line.startswith(tag + " "):
                    verdict[line[len(tag) + 1:].strip()] = tag
        buckets: dict[str, list[str]] = {t: [] for t in
                                         ("CLEAN", "REVIEW", "SORRY", "ABSENT", "DEF")}
        for ident, tag in verdict.items():
            buckets[tag].append(ident)
        print(f"probed {len(verdict)} identifier(s) cited by non-completed beans\n")
        print(f"  CLEAN  {len(buckets['CLEAN']):>4}  proved, no instance binder "
              "-- the bean citing it is a CANDIDATE STALE")
        print(f"  REVIEW {len(buckets['REVIEW']):>4}  proved BUT the type carries an "
              "instance binder; clean does not settle it (see sp07)")
        print(f"  SORRY  {len(buckets['SORRY']):>4}  genuinely open")
        print(f"  ABSENT {len(buckets['ABSENT']):>4}  does not resolve -- renamed, "
              "deleted, or namespace != module; its own finding")
        print(f"  DEF    {len(buckets['DEF']):>4}  a DEFINITION, not a theorem -- "
              "\"proved\" is meaningless for it, so\n"
              "                citing one says nothing about whether the bean is done")
        print()
        stale: dict[str, list[str]] = {}
        for ident in buckets["CLEAN"]:
            for bid in cites.get(ident, ()):
                stale.setdefault(bid, []).append(ident)
        if stale:
            print(f"CANDIDATE-STALE BEANS ({len(stale)}) -- open, citing a proved "
                  "binder-free declaration:")
            for bid, ids in sorted(stale.items(), key=lambda kv: -len(kv[1]))[:25]:
                print(f"  {bid:<12} [{status.get(bid,'?'):<11}] {len(ids):>2}  {ids[0]}")
            if len(stale) > 25:
                print(f"  ... and {len(stale) - 25} more")
            print("\n  Candidate, not verdict: a bean can legitimately stay open for "
                  "wiring,\n  documentation or a consumer even once its core lands. "
                  "Read before closing.")
        return 0

    print(f"non-completed beans citing a QOU.* identifier: "
          f"{len({b for s in cites.values() for b in s})}")
    print(f"distinct identifiers: {len(cites)}")
    print(f"  resolvable now (owning module has an olean): {len(resolvable)}")
    print(f"  owning module not built: {len(unbuilt)}  "
          "<- NOT a finding; build them or accept the gap")
    print(f"  no module prefix matches: {len(no_module)}  "
          "<- NOT necessarily missing: a declaration's NAMESPACE often differs "
          "from its\n     module (QOU.Mathlib.dimSYT lives in "
          "QOU.Mathlib.RSKBurnsideTarget), so this bucket\n     mixes that "
          "common case with genuinely renamed or deleted names")
    print("\nNext:  --emit > probe.lean ; lean probe.lean > probe.out ; "
          "--report probe.out")
    return 0


if __name__ == "__main__":
    sys.exit(main())
