#!/usr/bin/env python3
"""The three surfaces a Lean name can live on in this repo, and what collides
between them — for `def`/`abbrev`, which no existing checker covers.

Three surfaces carry Lean declarations here:

  L  library   `content/<paper>/lean/QOU/**` — real Lake modules, importable
  S  sibling   `content/<paper>/<chapter>/<block>.lean` with a co-located
               `<block>.ts` — compiles standalone, cannot import anything in
               the Lake tree, and wins **candidate 1** of `lean.ref`
               resolution ahead of every Lake candidate
  X  loose     a content-tree `.lean` with no co-located `.ts`

Two checkers already exist and between them leave a hole:

  * `folio-assistant/scripts/check-mirror-drift.ts` compares S against L —
    but reads `structure`/`class` heads only (its own docstring says so), so
    every `def` and `abbrev` is invisible to it. Bean `qou-u87j`.
  * `scripts/lean-duplicate-fqn-audit.py` compares L against L for
    `def`/`abbrev` — and scans `lean/QOU/` and nothing else. Bean `qou-kfcl`.

**Nothing covers S-against-L for `def`/`abbrev`.** That hole is not
hypothetical: `QOU.Archimedean.T_pp` is declared three times — twice in the
library (a `qou-kfcl` collision) and once in `mass-theory/beta-decay-transfer-matrix.lean`,
a block sibling in the same namespace whose body has drifted from the library
copy (`TM` vs `Matrix (Fin 2) (Fin 2) ℝ`). The mirror checker cannot see it
because it is a `def`; the FQN audit cannot see it because it is a sibling.

What each collision costs is different, and the report keeps them apart:

  L~L   a hard import error the moment anything imports both modules
        ("environment already contains"). Latent, never benign.
  L~S   no import error — a sibling imports nothing — but the sibling wins
        `lean.ref`, so the block's checkers audit the sibling while `lake
        build` compiles the library copy. Benign iff the bodies agree.
  S~S   two blocks using one name for two things. No build consequence;
        a reader hazard, and a sign the name wants disambiguating.

Usage:
    python3 scripts/lean-name-surface-audit.py            # summary
    python3 scripts/lean-name-surface-audit.py --detail   # every drifted pair
    python3 scripts/lean-name-surface-audit.py --json

Parser is shared with `lean-duplicate-fqn-audit.py` (imported, not copied), so
the four calibration fixes recorded there — docstring-indented `import`,
`/- -/` blanking, `section`/`end` stack, dotted declaration names — apply
here too. Read that file's SCOPE note before quoting any number from this one.
"""
from __future__ import annotations

import argparse
import collections
import importlib.util
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "dfa", REPO / "scripts/lean-duplicate-fqn-audit.py")
dfa = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dfa)

PAPER = REPO / "content/quantum-observable-universe"
LIB = PAPER / "lean"


def surface(p: Path) -> str:
    if LIB in p.parents:
        return "L"
    return "S" if p.with_suffix(".ts").exists() else "X"


def collect():
    """FQN -> {(surface, path): body}, plus FQN -> set of private sites.

    Private sites are collected but kept out of the L~L bucket: Lean mangles a
    `private` declaration's environment name per module, so two modules can
    both declare one and be imported together without error. Counting such a
    pair as "a hard import error once anything imports both" states something
    that is not true of the code.
    """
    out = collections.defaultdict(dict)
    priv = collections.defaultdict(set)
    for p in sorted(PAPER.rglob("*.lean")):
        if ".lake" in p.parts:
            continue
        s = surface(p)
        if s == "X":
            continue                      # no .ts: not a lean.ref candidate
        lines = dfa.strip_block_comments(
            p.read_text(encoding="utf-8", errors="replace")).splitlines()
        stack = []
        for i, ln in enumerate(lines):
            if dfa.IMP.match(ln):
                continue
            if (m := dfa.NS.match(ln)):
                stack.append(("ns", m.group(1)))
                continue
            if dfa.SEC.match(ln) and not dfa.DECL.match(ln):
                stack.append(("sec", ""))
                continue
            if dfa.END.match(ln) and stack:
                stack.pop()
                continue
            if (m := dfa.DECL.match(ln)):
                ns = ".".join(x for k, x in stack if k == "ns")
                fq = f"{ns}.{m.group(1)}" if ns else m.group(1)
                body = [ln.strip()]
                for nx in lines[i + 1:]:
                    if not nx.strip() or dfa.STOP.match(nx):
                        break
                    body.append(nx.strip())
                # Line comments are stripped: a trailing `-- note` differing
                # between the two copies is not drift in the declaration.
                text = " ".join(dfa.LINE_CMT.sub("", b) for b in body)
                site = (s, str(p.relative_to(REPO)))
                out[fq][site] = " ".join(text.split())
                if dfa.PRIV.match(ln):
                    priv[fq].add(site)
    return out, priv


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--detail", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    decls, priv = collect()
    priv_ll = 0
    surfaces = collections.Counter()
    for fq, sites in decls.items():
        for (s, _) in sites:
            surfaces[s] += 1

    buckets = collections.defaultdict(list)
    for fq, sites in sorted(decls.items()):
        if len(sites) < 2:
            continue
        kinds = set()
        lib_public = [k for k in sites if k[0] == "L" and k not in priv[fq]]
        if len(lib_public) > 1:
            kinds.add("L~L")
        elif sum(1 for s, _ in sites if s == "L") > 1:
            priv_ll += 1
        if any(s == "L" for s, _ in sites) and any(s == "S" for s, _ in sites):
            kinds.add("L~S")
        if sum(1 for s, _ in sites if s == "S") > 1:
            kinds.add("S~S")
        agree = len(set(sites.values())) == 1
        for k in kinds:
            buckets[(k, "identical" if agree else "DRIFTED")].append((fq, sites))

    print(f"def/abbrev declarations   library {surfaces['L']}   block siblings {surfaces['S']}")
    print()
    print("  collision          identical   DRIFTED   what it costs")
    rows = [
        ("L~L", "hard import error once anything imports both"),
        ("L~S", "sibling wins lean.ref; block checkers audit the sibling"),
        ("S~S", "one name, two meanings; no build consequence"),
    ]
    for k, why in rows:
        ident = len(buckets[(k, "identical")])
        drift = len(buckets[(k, "DRIFTED")])
        print(f"  {k:18s} {ident:9d} {drift:9d}   {why}")
    if priv_ll:
        print(f"\n  {priv_ll} same-FQN library pair(s) excluded from L~L: at least one\n"
              f"  side is `private`, so the names are mangled and cannot collide.")

    if args.detail:
        for k, _ in rows:
            got = buckets[(k, "DRIFTED")]
            if not got:
                continue
            print(f"\n=== {k}, bodies DIFFER ({len(got)}) ===")
            for fq, sites in got:
                print(f"  {fq}")
                for (s, path), body in sorted(sites.items()):
                    print(f"    [{s}] {path}")
                    print(f"        {body[:130]}")

    if args.json:
        print(json.dumps({f"{k}/{v}": len(x) for (k, v), x in buckets.items()}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
