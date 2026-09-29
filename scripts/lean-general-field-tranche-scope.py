#!/usr/bin/env python3
"""Scope the general-field tranche by DECLARATION reachability, not by file.

Bean `qou-j377`.  The tranche is "make `QOU.SchurWeyl.heckeWedderburn` hold over a general
field instead of `ℝ`".  Sizing it by *files carrying `ℝ`* gives 13-14 files and ~244
occurrences of the character.  That is the wrong unit twice over:

1. **A file is in the import cone if anything imports it, not if the goal depends on it.**
   `HoefsmitRep` reaches the chain only through `QJucysMurphy.qJM_seminormalRep21_one`, a
   concrete rank-2 sanity check with **zero consumers**; and `seminormalRep21`'s other users
   (`HeckeWedderburn3`, `HeckeDim3Indep`, `HeckeMarkov3`) are not in the cone at all.  So
   `HoefsmitRep`'s 12 `ℝ`-carrying declarations are off the general path entirely.
2. **`ℝ` is a character; a declaration is the unit of work.**  Counting occurrences inflates
   a file whose one theorem mentions `ℝ` six times.

This script walks declaration references from `heckeWedderburn` and reports, per module, how
many `ℝ`-carrying declarations exist and how many are reachable.

**Its limits, which decide whether you can trust a zero.**  Reachability is name-based, so:

- it can **over**-reach, if a declaration name also occurs as an ordinary word elsewhere;
- it can **under**-reach, because names of 3 characters or fewer are excluded from the
  pattern set (a bare `S0` or `S1` matches far too much prose to follow safely).

The second limit is the dangerous one: it is exactly how a file gets wrongly declared
off-path.  `--check-short` closes it for the case that matters here, by asking directly
whether any *reachable* body mentions `S0` or `S1`.  Run it before believing an OFF verdict;
for this corpus it answers NONE, which is what makes the `HoefsmitRep` verdict safe.

    python3 scripts/lean-general-field-tranche-scope.py --root folio/quantum-observable-universe/lean
    python3 scripts/lean-general-field-tranche-scope.py --check-short
"""
from __future__ import annotations

import argparse
import pathlib
import re
from collections import defaultdict

GOAL = "QOU.SchurWeyl.HeckeWedderburnGeneral"
ROOTS = ["heckeWedderburn", "heckeProduct_bijective", "finrank_hecke_eq_factorial"]
SHORT_NAMES = ["S0", "S1"]

DECL = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*"
    r"(theorem|lemma|def|abbrev|instance)\s+([A-Za-z_][A-Za-z0-9_'.]*)", re.M)


def strip_noncode(text: str) -> str:
    text = re.sub(r"/-.*?-/", "", text, flags=re.S)
    text = re.sub(r"--.*?$", "", text, flags=re.M)
    return re.sub(r"^\s*import\s+.*$", "", text, flags=re.M)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="folio/quantum-observable-universe/lean")
    ap.add_argument("--check-short", action="store_true",
                    help="report reachable bodies mentioning S0/S1, which reachability cannot follow")
    args = ap.parse_args()
    root = pathlib.Path(args.root)

    files = [p for p in root.rglob("*.lean") if ".lake" not in str(p)]
    mod = {p.relative_to(root).as_posix()[:-5].replace("/", "."): p for p in files}
    imports = {p: set(re.findall(r"^import\s+([A-Za-z0-9_.]+)", p.read_text(), re.M))
               for p in files}

    seen, stack = set(), [GOAL]
    while stack:
        m = stack.pop()
        if m in seen:
            continue
        seen.add(m)
        if (q := mod.get(m)) is not None:
            stack.extend(imports[q])
    cone = {m for m in seen if m in mod}

    body_of, mod_of, has_r = {}, {}, {}
    for m in sorted(cone):
        b = strip_noncode(mod[m].read_text())
        ms = list(DECL.finditer(b))
        for i, mm in enumerate(ms):
            n = mm.group(2)
            seg = b[mm.start(): ms[i + 1].start() if i + 1 < len(ms) else len(b)]
            body_of[n], mod_of[n], has_r[n] = seg, m, "ℝ" in seg

    pats = {n: re.compile(r"\b" + re.escape(n) + r"\b") for n in body_of if len(n) > 3}
    reach, stack = set(), [r for r in ROOTS if r in body_of]
    while stack:
        n = stack.pop()
        if n in reach:
            continue
        reach.add(n)
        for other, pat in pats.items():
            if other not in reach and pat.search(body_of[n]):
                stack.append(other)

    if args.check_short:
        hits = [(mod_of[n], n, s) for n in sorted(reach) for s in SHORT_NAMES
                if re.search(r"\b" + s + r"\b", body_of[n])]
        if hits:
            print("reachable bodies mentioning a short name (reachability cannot follow these):")
            for m, n, s in hits:
                print(f"  {m.split('.')[-1]}.{n}  mentions {s}")
        else:
            print("NONE — no reachable declaration mentions S0/S1, so an OFF verdict is safe")
        return 0

    print(f"cone modules {len(cone)}   declarations {len(body_of)}   "
          f"reachable from {'/'.join(ROOTS)}: {len(reach)}")
    total, live = defaultdict(int), defaultdict(int)
    for n, r in has_r.items():
        if r:
            total[mod_of[n]] += 1
            if n in reach:
                live[mod_of[n]] += 1
    print(f"\n{'ℝ-decls':>8} {'reachable':>10}  module")
    for m in sorted(total, key=lambda k: -total[k]):
        off = "   <-- OFF the general path" if live[m] == 0 else ""
        print(f"{total[m]:>8} {live[m]:>10}  {m.split('.')[-1]}{off}")
    print(f"\nTRANCHE: {sum(live.values())} ℝ-carrying declarations across "
          f"{sum(1 for m in live if live[m])} modules "
          f"(of {sum(total.values())} across {len(total)} in the cone)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
