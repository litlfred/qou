#!/usr/bin/env python3
"""
Witness stems that exist at two paths — and the ones whose CONSUMERS DIVERGE.

Bean `qou-kcii`. A witness is normally addressed by bare stem, not path:
`_path_bridge.witness_path("foo.witness.json", HERE)`. That resolver searches
`prefer_dir` first — typically the CALLING SCRIPT'S OWN directory — then the
`computations/` root, then each cluster subdirectory.

So when one stem exists at two paths, WHICH FILE A CONSUMER GETS DEPENDS ON
WHERE THE CONSUMER LIVES. Two scripts can read "the same witness" and receive
different numbers, with nothing in either script indicating it.

WHY THIS AUDIT REPORTS TWO NUMBERS
----------------------------------
Duplicated stems alone over-reports: a stem duplicated in a corner nothing
reads is untidy, not dangerous. The number that matters is how many stems
have consumers resolving to DIFFERENT copies. Measured 2026-08-21: 25 stems
duplicated, 7 of them consumer-splitting.

The 7 are not hypothetical. `habiro-coefficients-extended` is read by three
scripts in `computations/` (including `cross_check_trM_1ppb.py`, the L1
compute-precision gate) and two in `computations/habiro/` — and the two
copies differ: the top-level one holds 4/4 real results, the habiro/ one
holds 4/4 errors (bean `qou-ls7l`). A "cleanup" that unified them the wrong
way would hand the L1 gate a witness full of error stubs.

It already produced one wrong reading: a probe written for bean `qou-3zby`
used `rglob` instead of the resolver, read the other copy, and reported the
wrong `q0Anchor` for its headline input. Caught pre-commit, but only just.

A REFERENCE IS NOT A VERIFIED READ. The consumer scan is textual — it asks
which `.py` files mention the stem — so a stem named in a comment counts as
a consumer. That over-reports rather than under-reports, which is the safe
direction for a detector, but check the call site before acting on a row.

WHAT THIS DOES NOT DO
---------------------
It does not pick a winner or move anything. Which copy is canonical is the
owning arc's call — and for at least one pair the answer is NOT "keep the
one in the tidier directory": `witness_provenance_audit.py` exists twice as
two genuinely DIFFERENT audits (correctness vs completeness, bean `qou-2r42`),
so consolidating by name would silently swap one check for another.

Reported, not gated. A gate red on arrival gets skipped — this file's own
sibling `precision-gates.sh` says so at the top — and this is red at 7.

AND THE MECHANISM, NOT ONLY THE EXPOSURE
----------------------------------------
The duplication above is the hazard; the way code walks into it is a call
that resolves a name RECURSIVELY and then blind-picks. The incident in this
docstring — a probe using `rglob` instead of the resolver, reading the other
copy, reporting the wrong `q0Anchor` — was of exactly that shape, and nothing
here detected it, so a recurrence would not have been caught either.

`--bypasses` scans for it. `Path.rglob`/`glob` yield in `os.scandir` order:
filesystem-dependent, NOT sorted. So `hits[0]`, `next(...)`, a loop that
`break`s on the first hit, or a dict comprehension keyed by `.name` (last
wins) all pick a copy that can differ between machines and can flip on one
machine after unrelated churn — silent, and not reproducible from the source.
`sorted()` makes a pick repeatable but still arbitrary, so it is reported as
a weaker finding rather than a pass.

Like the consumer scan, this OVER-reports: most globs resolve names that are
not duplicated, and are fine. It marks the ones whose target basename IS
duplicated today as `LIVE`, and the rest as `latent`.

**`LIVE` is the narrow tier, and it is currently empty on BOTH trees.** It can
only fire when the glob argument is a string *literal*, since that is the only
case where the target basename is knowable statically. Every one of the six
defects fixed under `qou-kcii` computed its target with an f-string, so
back-testing this detector against the pre-fix `origin/main` sources gives
**0 LIVE and 9 latent sites across those six files** — the detection is real,
but it lands in `latent`. Read `LIVE: 0` as "no statically-decidable case",
never as "clean"; the actionable list is `latent`. Adjudicate at the call
site — the right fix is usually `_path_bridge.witness_path(name, prefer_dir)`
with prefer_dir chosen deliberately (for a witness, the PRODUCER's directory,
because producers emit beside themselves — not the caller's, which is how a
probe read the wrong copy in the first place).

Usage:
    python3 computations/audits/duplicate_witness_stem_audit.py
    python3 computations/audits/duplicate_witness_stem_audit.py --strict
        exit 1 if any stem's consumers resolve to different copies
    python3 computations/audits/duplicate_witness_stem_audit.py --bypasses
        also list name-resolution sites that blind-pick
"""

from __future__ import annotations

import argparse
import ast
import collections
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATIONS = HERE.parent
SKIP_PARTS = {"_deprecated", "__pycache__"}


def _cluster_dirs() -> list[Path]:
    """Mirror `_path_bridge._WITNESS_DIRS`: root first, then cluster subdirs.

    A cluster is a non-underscore, non-dot directory carrying `__init__.py`
    — the same filter the bridge applies, so an untracked scratch dir does
    not change what this audit predicts.
    """
    dirs = [COMPUTATIONS]
    for child in sorted(COMPUTATIONS.iterdir()):
        if not child.is_dir() or child.name.startswith(("_", ".")):
            continue
        if (child / "__init__.py").is_file():
            dirs.append(child)
    return dirs


def _resolve(stem: str, caller_dir: Path, dirs: list[Path]) -> Path | None:
    """Which copy `witness_path(stem, caller_dir)` would return."""
    for d in [caller_dir] + [x for x in dirs if x != caller_dir]:
        if (d / stem).exists():
            return d
    return None


def _dup_basenames() -> set[str]:
    """Basenames that exist at 2+ paths — witnesses AND scripts.

    A glob whose target is one of these can actually pick wrong today; the
    rest of the glob sites are latent.
    """
    seen: dict[str, int] = collections.Counter()
    for pat in ("*.witness.json", "*.py"):
        for p in COMPUTATIONS.rglob(pat):
            if SKIP_PARTS & set(p.parts):
                continue
            seen[p.name] += 1
    return {k for k, v in seen.items() if v > 1 and k != "__init__.py"}


def _scan_bypasses(roots: list[Path]) -> list[dict]:
    """Name-resolution sites that blind-pick from an unordered glob.

    Detected by AST, so a `sorted()` wrapper is recognised structurally rather
    than by grepping for the word on the same line.
    """
    dups = _dup_basenames()
    self_path = Path(__file__).resolve()
    out: list[dict] = []

    for root in roots:
        for f in sorted(root.rglob("*.py")):
            if SKIP_PARTS & set(f.parts) or f.resolve() == self_path:
                continue
            try:
                tree = ast.parse(f.read_text(errors="ignore"))
            except (OSError, SyntaxError):
                continue

            parent: dict[int, ast.AST] = {}
            for node in ast.walk(tree):
                for kid in ast.iter_child_nodes(node):
                    parent[id(kid)] = node

            for node in ast.walk(tree):
                if not (isinstance(node, ast.Call)
                        and isinstance(node.func, ast.Attribute)
                        and node.func.attr in ("rglob", "glob")):
                    continue

                # Sorted anywhere up the expression chain => ordered.
                ordered, cur = False, node
                for _ in range(4):
                    up = parent.get(id(cur))
                    if up is None:
                        break
                    if (isinstance(up, ast.Call)
                            and isinstance(up.func, ast.Name)
                            and up.func.id == "sorted"):
                        ordered = True
                        break
                    cur = up

                # How is the result consumed?
                how, cur = None, node
                for _ in range(4):
                    up = parent.get(id(cur))
                    if up is None:
                        break
                    if isinstance(up, ast.Subscript):
                        how = "[index]"
                        break
                    if (isinstance(up, ast.Call)
                            and isinstance(up.func, ast.Name)
                            and up.func.id == "next"):
                        how = "next()"
                        break
                    if isinstance(up, ast.For):
                        body = up.body
                        if any(isinstance(s, (ast.Break, ast.Return))
                               for s in ast.walk(up)) and body:
                            how = "for+break/return"
                        break
                    if isinstance(up, (ast.DictComp, ast.SetComp)):
                        how = "comprehension (last/first wins)"
                        break
                    if isinstance(up, ast.Assign):
                        # `hits = list(root.rglob(name))` — the pick happens
                        # LATER, at `hits[0]`, so the expression walk alone
                        # cannot see it. This shape is not academic: it is
                        # exactly how two of the sites bean qou-kcii lists
                        # were written, and an earlier version of this
                        # detector missed both while happily flagging an
                        # unrelated `sorted()` comprehension a few lines up.
                        # Caught by back-testing the detector against the
                        # pre-fix sources instead of trusting it on the
                        # fixed tree, where it reports a clean 0.
                        tgts = [t.id for t in up.targets
                                if isinstance(t, ast.Name)]
                        fn = up
                        while (fn is not None
                               and not isinstance(fn, (ast.FunctionDef,
                                                       ast.AsyncFunctionDef,
                                                       ast.Module))):
                            fn = parent.get(id(fn))
                        if tgts and fn is not None:
                            for sub in ast.walk(fn):
                                if (isinstance(sub, ast.Subscript)
                                        and isinstance(sub.value, ast.Name)
                                        and sub.value.id in tgts):
                                    how = "assigned then [index]"
                                    break
                        break
                    cur = up
                if how is None:
                    continue          # full listing: order does not decide

                # Which basename is being resolved, if it is a literal?
                target = None
                if node.args and isinstance(node.args[0], ast.Constant) \
                        and isinstance(node.args[0].value, str):
                    target = node.args[0].value
                live = bool(target and target in dups)
                if target and ("*" in target or "?" in target):
                    live = False      # a wildcard sweep, not a name lookup

                try:
                    shown = f.relative_to(COMPUTATIONS.parent).as_posix()
                except ValueError:
                    shown = f.as_posix()   # scanning a tree outside the repo
                out.append({
                    "file": shown,
                    "line": node.lineno, "how": how, "ordered": ordered,
                    "target": target, "live": live,
                })
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any stem's consumers resolve to different copies")
    ap.add_argument("--bypasses", action="store_true",
                    help="also list name-resolution sites that blind-pick")
    args = ap.parse_args()

    dirs = _cluster_dirs()

    by_stem: dict[str, list[Path]] = collections.defaultdict(list)
    for p in COMPUTATIONS.rglob("*.witness.json"):
        if SKIP_PARTS & set(p.parts):
            continue
        by_stem[p.name].append(p.parent)
    dups = {k: v for k, v in by_stem.items() if len(v) > 1}

    # Self-excluded: this file names several stems in its own docstring, and
    # a docstring mention is not a read.
    self_path = Path(__file__).resolve()
    sources = {}
    for p in COMPUTATIONS.rglob("*.py"):
        if SKIP_PARTS & set(p.parts) or p.resolve() == self_path:
            continue
        try:
            sources[p] = p.read_text(errors="ignore")
        except OSError:
            continue

    split = []
    for stem in sorted(dups):
        key = stem[: -len(".witness.json")]
        got: dict[str, list[str]] = collections.defaultdict(list)
        for path, text in sources.items():
            if key not in text:
                continue
            r = _resolve(stem, path.parent, dirs)
            if r is not None:
                got[str(r.relative_to(COMPUTATIONS.parent))].append(path.name)
        if len(got) > 1:
            split.append({"stem": stem,
                          "resolves_to": {k: sorted(v) for k, v in sorted(got.items())}})

    print("=" * 70)
    print("duplicate-witness-stem audit")
    print("=" * 70)
    print(f"  witness stems duplicated across paths : {len(dups)}")
    print(f"  of those, CONSUMERS DIVERGE on        : {len(split)}")
    if split:
        print("\n  consumer-splitting stems (a 'cleanup' here changes what code reads):")
        for row in split:
            print(f"    {row['stem']}")
            for d, cs in row["resolves_to"].items():
                head = ", ".join(cs[:3]) + (" …" if len(cs) > 3 else "")
                print(f"        -> {d}/   read by {len(cs)}: {head}")
    print("\n  These are REFERENCES, not verified reads: the scan is textual, so a "
          "stem\n  named only in a comment counts. That over-reports rather than "
          "under-reports,\n  which is the right direction for a detector — but check "
          "the call site\n  before acting on a row.\n\n  Reported, not gated. Which "
          "copy is canonical is the owning arc's call;\n  see bean qou-2r42 for a pair "
          "where consolidating by name would swap\n  one audit for a different one.")

    if args.bypasses:
        rows = _scan_bypasses([COMPUTATIONS, COMPUTATIONS.parent / "scripts"])
        unordered = [r for r in rows if not r["ordered"]]
        live = [r for r in rows if r["live"]]
        print("\n" + "=" * 70)
        print("name-resolution sites that blind-pick from a glob")
        print("=" * 70)
        print(f"  glob sites whose result is decided by ORDER : {len(rows)}")
        print(f"    of those, not wrapped in sorted()         : {len(unordered)}")
        print(f"    of those, resolving a DUPLICATED basename : {len(live)}")
        if not live:
            print("      ^ do NOT read 0 here as 'clean'. LIVE requires the glob")
            print("        argument to be a STRING LITERAL, and every one of the")
            print("        six defects fixed under qou-kcii built its target with")
            print("        an f-string, so all six land in the latent tier below.")
            print("        Back-tested against origin/main: 0 LIVE, 9 latent sites")
            print("        across those six files. The actionable signal is the")
            print("        latent list; LIVE is the narrower, currently-empty tier.")
        for tag, sel in (("LIVE (literal target, duplicated basename today)", live),
                         ("unordered (latent — target not duplicated, or "
                          "not a literal)",
                          [r for r in unordered if not r["live"]])):
            if not sel:
                continue
            print(f"\n  {tag}:")
            for r in sel:
                t = r["target"] or "<non-literal>"
                s = "" if r["ordered"] else "  UNSORTED"
                print(f"    {r['file']}:{r['line']}  {r['how']}  "
                      f"target={t}{s}")
        print("\n  Over-reports by design, like the consumer scan above: most "
              "of these\n  resolve names that are not duplicated. Adjudicate "
              "at the call site.\n  The usual fix is "
              "_path_bridge.witness_path(name, prefer_dir) with\n  prefer_dir "
              "chosen deliberately — for a witness that is the PRODUCER's\n  "
              "directory, since producers emit beside themselves.")

    if args.strict and split:
        print(f"\nSTRICT: {len(split)} stem(s) resolve differently per consumer — "
              "exiting 1", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
