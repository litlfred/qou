#!/usr/bin/env python3
"""Transitive consumer guard for Lean declaration / module renames (bean qou-s63a).

Why this exists
---------------
Two regressions reached `main` and sat there red after Lean renames (#6191 and
#6257), both from the same two gaps in a one-level importer check:

  1. `lean QOU.lean` is not a corpus-wide gate: the root module reaches only a
     subset of `folio/*/lean/QOU/**/*.lean`, and neither broken consumer was in
     `QOU.lean`'s import closure.
  2. A rename's consumer set is the TRANSITIVE reverse-import cone (plus
     `open Ns (ident)` consumers), not the direct importers:
       - `QOU/Archimedean/MassGapGm.lean` (`GroundRing.hbar_q` -> `hbarQ`,
         PR #6191) was missed when a straggler batch got no transitive check.
       - `QOU/BraidKnot/KeystoneMcKayValueMap.lean` (`BraidKnot.qInt` ->
         `qIntGeo`, PR #6257) reached the declaration via
         `open QOU.BraidKnot (qInt qFactorial)` — a second-order consumer.

What this script does
---------------------
Given a renamed declaration (`--old <FQN_or_ident>`) and/or its declaring
module (`--module <QOU.Path>`):

  1. Builds the reverse-import graph across `folio/*/lean/` (reusing the
     comment-stripping and column-0 `IMP` parser from
     `scripts/lean-duplicate-fqn-audit.py`).
  2. Computes the TRANSITIVE reverse-import closure of the declaring module(s),
     union any module carrying an `open <Ns>` for the declaration's namespace.
  3. Greps code (with `/- ... -/` block comments and `-- ...` line comments
     stripped) for residual occurrences of the old identifier / FQN — both
     inside the transitive cone and across all corpus `.lean` files (including
     content-block siblings).
  4. Optionally (`--compile`) runs `lean -DautoImplicit=false -s 65536` on the
     hit modules (or the full transitive cone with `--compile-cone`).

Usage:
    python3 scripts/lean-rename-consumer-guard.py --old QOU.GroundRing.hbar_q --module QOU.GroundRing
    python3 scripts/lean-rename-consumer-guard.py --old QOU.BraidKnot.qInt --module QOU.BraidKnot.Basic
    python3 scripts/lean-rename-consumer-guard.py --self-test
"""
from __future__ import annotations

import argparse
import collections
import importlib.util
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "dfa", REPO / "scripts/lean-duplicate-fqn-audit.py"
)
dfa = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dfa)

OPEN_RE = re.compile(r"^\s*open\s+([^\n]+)")


def strip_all_comments(text: str) -> str:
    """Blank out both `/- ... -/` block comments and `-- ...` line comments."""
    no_block = dfa.strip_block_comments(text)
    return "\n".join(dfa.LINE_CMT.sub("", ln) for ln in no_block.splitlines())


def parse_imports_and_opens(code_text: str) -> tuple[set[str], set[str], set[tuple[str, str]]]:
    """Return (imports, opened_namespaces, explicit_open_items) from comment-stripped Lean code.

    `explicit_open_items` contains `(namespace, ident)` pairs from forms like
    `open QOU.BraidKnot (qInt qFactorial)`.
    """
    imports: set[str] = set()
    opened_ns: set[str] = set()
    open_items: set[tuple[str, str]] = set()
    for ln in code_text.splitlines():
        if (m := dfa.IMP.match(ln)):
            imports.add(m.group(1))
            continue
        if (m := OPEN_RE.match(ln)):
            rest = m.group(1).strip()
            # Handle `open Ns (a b c)` as well as `open Ns1 Ns2 in`
            rest = re.sub(r"\bin\s*$", "", rest).strip()
            paren_m = re.match(r"^([\w.]+)\s*\(([^)]*)\)", rest)
            if paren_m:
                ns = paren_m.group(1)
                opened_ns.add(ns)
                for tok in paren_m.group(2).split():
                    if tok:
                        open_items.add((ns, tok))
            else:
                for tok in rest.split():
                    if re.match(r"^[A-Za-z_][\w.]*$", tok):
                        opened_ns.add(tok)
    return imports, opened_ns, open_items


def transitive_reverse_cone(
    seeds: set[str],
    rev_imports: dict[str, set[str]],
) -> set[str]:
    """Full transitive closure of `seeds` under `rev_imports` (excluding `seeds` unless re-imported)."""
    visited: set[str] = set()
    queue = collections.deque(seeds)
    while queue:
        cur = queue.popleft()
        for imp in rev_imports.get(cur, ()):
            if imp not in visited:
                visited.add(imp)
                queue.append(imp)
    return visited


def find_identifier_hits(code_text: str, old_fqn: str) -> list[tuple[int, str]]:
    """Return `(lineno, line)` for every code line referencing `old_fqn` or its short name."""
    short = old_fqn.rsplit(".", 1)[-1]
    alts = [re.escape(old_fqn)]
    if "." in old_fqn:
        # Also match suffix-qualified forms (e.g. `GroundRing.hbar_q`) and bare `hbar_q`
        parts = old_fqn.split(".")
        for k in range(1, len(parts)):
            alts.append(re.escape(".".join(parts[k:])))
    pat = re.compile(rf"(?<![\w.])(?:{'|'.join(alts)})(?![\w'])")
    hits: list[tuple[int, str]] = []
    for idx, ln in enumerate(code_text.splitlines(), 1):
        if pat.search(ln):
            hits.append((idx, ln.strip()))
    return hits


def analyze_corpus(
    files: dict[str, str],
    old_fqn: str,
    seed_modules: set[str],
) -> dict:
    """Run transitive reverse-import + `open Ns` + token scan over `files` (`mod_or_path -> raw_text`)."""
    rev_imports: dict[str, set[str]] = collections.defaultdict(set)
    opened_by_ns: dict[str, set[str]] = collections.defaultdict(set)
    opened_item_mods: dict[tuple[str, str], set[str]] = collections.defaultdict(set)
    stripped_by_mod: dict[str, str] = {}

    for mod, raw in files.items():
        code = strip_all_comments(raw)
        stripped_by_mod[mod] = code
        imps, opens, items = parse_imports_and_opens(code)
        for target in imps:
            rev_imports[target].add(mod)
        for ns in opens:
            opened_by_ns[ns].add(mod)
        for ns_item in items:
            opened_item_mods[ns_item].add(mod)

    ns_prefix = old_fqn.rsplit(".", 1)[0] if "." in old_fqn else ""
    short = old_fqn.rsplit(".", 1)[-1]

    cone = transitive_reverse_cone(seed_modules, rev_imports)
    open_consumers: set[str] = set()
    if ns_prefix:
        open_consumers |= opened_by_ns.get(ns_prefix, set())
        open_consumers |= opened_item_mods.get((ns_prefix, short), set())

    candidate_consumers = (cone | open_consumers) - seed_modules
    cone_hits: dict[str, list[tuple[int, str]]] = {}
    outside_hits: dict[str, list[tuple[int, str]]] = {}

    for mod, code in sorted(stripped_by_mod.items()):
        if mod in seed_modules:
            continue
        hits = find_identifier_hits(code, old_fqn)
        if not hits:
            continue
        if mod in candidate_consumers:
            cone_hits[mod] = hits
        else:
            outside_hits[mod] = hits

    return {
        "seeds": sorted(seed_modules),
        "transitive_cone": sorted(cone),
        "open_consumers": sorted(open_consumers),
        "cone_hits": cone_hits,
        "outside_hits": outside_hits,
    }


def load_corpus_lean_files() -> dict[str, str]:
    """Load all `.lean` files under `folio/` (from disk when present, else `git show HEAD:<path>`)."""
    out = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", "HEAD", "folio/"],
        cwd=REPO, capture_output=True, text=True, check=False,
    ).stdout.splitlines()
    paths = [p for p in out if p.endswith(".lean") and "/.lake/" not in p]
    for p in (REPO / "folio").rglob("*.lean"):
        if ".lake" in p.parts:
            continue
        rel = p.relative_to(REPO).as_posix()
        if rel not in paths:
            paths.append(rel)

    files: dict[str, str] = {}
    lib_prefix = "folio/quantum-observable-universe/lean/"
    for rel in sorted(set(paths)):
        disk_p = REPO / rel
        if disk_p.exists():
            raw = disk_p.read_text(encoding="utf-8", errors="replace")
        else:
            raw = subprocess.run(
                ["git", "show", f"HEAD:{rel}"],
                cwd=REPO, capture_output=True, text=True, check=False,
            ).stdout
        if rel.startswith(lib_prefix) and rel.endswith(".lean"):
            key = rel[len(lib_prefix) : -len(".lean")].replace("/", ".")
        else:
            key = rel
        files[key] = raw
    return files


def self_test() -> int:
    """Verify multi-hop transitive import closure, `open Ns (ident)` edges, and comment stripping."""
    synthetic = {
        "QOU.GroundRing": (
            "namespace QOU.GroundRing\n"
            "def hbarQ : Int := 1\n"
            "end QOU.GroundRing\n"
        ),
        "QOU.Archimedean.Mid": (
            "import QOU.GroundRing\n"
            "namespace QOU.Archimedean\n"
            "def midVal : Int := QOU.GroundRing.hbarQ\n"
            "end QOU.Archimedean\n"
        ),
        # Multi-hop consumer (#6191 MassGapGm shape): imports Mid, not GroundRing directly
        "QOU.Archimedean.MassGapGm": (
            "import QOU.Archimedean.Mid\n"
            "namespace QOU.Archimedean\n"
            "def staleRef := QOU.GroundRing.hbar_q\n"
            "end QOU.Archimedean\n"
        ),
        # Second-order `open Ns (ident)` consumer (#6257 KeystoneMcKayValueMap shape)
        "QOU.BraidKnot.KeystoneMcKayValueMap": (
            "import QOU.BraidKnot.Other\n"
            "open QOU.BraidKnot (qInt qFactorial)\n"
            "def badUse := qInt 3\n"
        ),
        # Comment-only mention must NOT be flagged
        "QOU.Archimedean.CleanConsumer": (
            "import QOU.Archimedean.Mid\n"
            "/- Historical note: renamed hbar_q -> hbarQ and qInt -> qIntGeo. -/\n"
            "-- Also in line comment: hbar_q qInt\n"
            "def okVal : Int := QOU.GroundRing.hbarQ\n"
        ),
    }

    r1 = analyze_corpus(synthetic, "QOU.GroundRing.hbar_q", {"QOU.GroundRing"})
    ok1 = (
        "QOU.Archimedean.MassGapGm" in r1["transitive_cone"]
        and "QOU.Archimedean.MassGapGm" in r1["cone_hits"]
        and "QOU.Archimedean.CleanConsumer" not in r1["cone_hits"]
    )

    r2 = analyze_corpus(synthetic, "QOU.BraidKnot.qInt", {"QOU.BraidKnot.Basic"})
    ok2 = (
        "QOU.BraidKnot.KeystoneMcKayValueMap" in r2["open_consumers"]
        and "QOU.BraidKnot.KeystoneMcKayValueMap" in r2["cone_hits"]
        and "QOU.Archimedean.CleanConsumer" not in r2["cone_hits"]
    )

    r3 = analyze_corpus(synthetic, "QOU.GroundRing.nonexistentOldName", {"QOU.GroundRing"})
    ok3 = not r3["cone_hits"] and not r3["outside_hits"]

    cases = [
        ("2-hop transitive importer (MassGapGm #6191 shape) is caught", ok1),
        ("open Ns (ident) consumer (KeystoneMcKayValueMap #6257 shape) is caught", ok2),
        ("comment-only mentions and clean renames produce 0 hits", ok3),
    ]
    failed = 0
    for label, ok in cases:
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")
        if not ok:
            failed += 1
    if failed:
        print(f"SELF-TEST FAILED ({failed} case(s))")
        return 1
    print(f"SELF-TEST PASSED ({len(cases)}/{len(cases)} cases)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--old", help="old declaration FQN or identifier (e.g. QOU.BraidKnot.qInt)")
    ap.add_argument(
        "--module",
        action="append",
        default=[],
        help="declaring module name (e.g. QOU.GroundRing); repeatable",
    )
    ap.add_argument(
        "--compile",
        action="store_true",
        help="run `lean -DautoImplicit=false -s 65536` on any library module with hits",
    )
    ap.add_argument(
        "--self-test",
        "--selftest",
        dest="selftest",
        action="store_true",
        help="run built-in unit tests on the #6191 and #6257 regression shapes",
    )
    args = ap.parse_args()

    if args.selftest:
        return self_test()

    if not args.old:
        ap.error("--old <FQN_or_ident> is required (or pass --self-test)")

    files = load_corpus_lean_files()
    seeds = set(args.module)
    if not seeds and "." in args.old:
        prefix = args.old.rsplit(".", 1)[0]
        if prefix in files:
            seeds.add(prefix)

    res = analyze_corpus(files, args.old, seeds)
    print(f"old declaration / ident : {args.old}")
    print(f"seed module(s)          : {res['seeds'] or '(none)'}")
    print(f"transitive import cone  : {len(res['transitive_cone'])} module(s)")
    print(f"open-namespace consumers: {len(res['open_consumers'])} module(s)")
    print(f"hits in consumer cone   : {len(res['cone_hits'])} file(s)")
    print(f"hits outside cone       : {len(res['outside_hits'])} file(s)")

    all_hits = {**res["cone_hits"], **res["outside_hits"]}
    for mod, hits in sorted(all_hits.items()):
        bucket = "CONE" if mod in res["cone_hits"] else "OUTSIDE"
        print(f"\n  [{bucket}] {mod}")
        for lineno, snippet in hits[:5]:
            print(f"    L{lineno}: {snippet}")

    if args.compile and all_hits:
        lean_root = REPO / "folio/quantum-observable-universe/lean"
        for mod in sorted(all_hits):
            if not mod.startswith("QOU."):
                continue
            lean_file = lean_root / (mod.replace(".", "/") + ".lean")
            if not lean_file.exists():
                continue
            r = subprocess.run(
                ["lean", "-DautoImplicit=false", "-s", "65536", str(lean_file)],
                cwd=lean_root,
                env=os.environ.copy(),
            )
            if r.returncode != 0:
                return r.returncode

    return 1 if all_hits else 0


if __name__ == "__main__":
    raise SystemExit(main())
