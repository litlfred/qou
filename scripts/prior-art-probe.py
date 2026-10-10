#!/usr/bin/env python3
"""Before you write it, or call it absent: does the corpus already declare it?

Greps DECLARATION LINES ONLY -- Lean `theorem`/`lemma`/`def`/`class`/`structure`
/`abbrev`/`instance` and Python `def`/`class` -- for concept keywords, across
BOTH Lean trees (library `lean/QOU/**` and content-block siblings) and
`computations/`. Prose and docstrings are deliberately excluded: a topic grep
returns hundreds of hits and is what fails.

WHY THIS EXISTS. Five misses in one session on PR #5744, every one the same
shape -- grepping the TOPIC rather than the named OBJECT, then declaring the item
absent or writing a duplicate:

  1. a Milnor triple-linking Lean file duplicating committed PYTHON
     (`computations/binding_mn_milnor_linking.py`)  <- cross-language, which no
     existing duplicate checker covers
  2. `qb`, character-for-character `QOU.BraidKnot.AJTrefoil.qInt`
  3. `sub_inv_ne_zero`, same NAME as `QOU.Mass.QHookDimensionBalanced`'s
  4. "the brane tower has no invariance result" -- `BraneTowerIsospinBlind`
     proves it on main
  5. "chirality carries no invariance result" -- `chirality_is_unique_S_odd`
     and `prop:chirality-dual-space-derivation` both settle it

The existing `scripts/duplicate-*.py` family censuses duplicate CLASS names.
That catches case 3 only. Cases 1, 2, 4, 5 need concept keywords against
declaration lines, which is what this does.

NOT a replacement for the AGENTS.md corpus-grep checklist -- it is the missing
mechanical half of path 2/3, for the question "is there already a declaration
about X?".

    scripts/prior-art-probe.py brane tower
    scripts/prior-art-probe.py chirality invariant
    scripts/prior-art-probe.py --selftest
"""
from __future__ import annotations
import re, subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEAN_KINDS = r"(?:noncomputable\s+)?(?:private\s+)?(?:theorem|lemma|def|abbrev|class|structure|instance)"
DECL_RE = re.compile(rf"^\s*{LEAN_KINDS}\s+([A-Za-z_][A-Za-z0-9_.']*)")
PY_RE = re.compile(r"^\s*(?:async\s+)?(?:def|class)\s+([A-Za-z_][A-Za-z0-9_]*)")

def _tracked(*globs: str) -> list[pathlib.Path]:
    out = subprocess.run(["git", "ls-files", *globs], cwd=ROOT,
                         capture_output=True, text=True).stdout.split("\n")
    return [ROOT / p for p in out if p and ".lake" not in p and ("_deprecated" not in p and "fsh-guts" not in p)]

def declarations() -> list[tuple[pathlib.Path, int, str, str]]:
    """(path, lineno, declared-name, full line) over every tracked decl site."""
    hits = []
    for p in _tracked("content/**/*.lean"):
        try: text = p.read_text(errors="replace")
        except OSError: continue
        for i, line in enumerate(text.split("\n"), 1):
            m = DECL_RE.match(line)
            if m: hits.append((p, i, m.group(1), line.strip()))
    for p in _tracked("computations/**/*.py", "tools/**/*.py"):
        try: text = p.read_text(errors="replace")
        except OSError: continue
        for i, line in enumerate(text.split("\n"), 1):
            m = PY_RE.match(line)
            if m: hits.append((p, i, m.group(1), line.strip()))
    return hits

def _flat(s: str) -> str:
    return s.lower().replace("_", "").replace("-", "").replace(".", "").replace("/", "")

def probe(keywords: list[str], decls=None):
    """Rank every declaration by how many keywords hit its NAME or its PATH,
    case- and separator-insensitively. Returns `(score, path, line, name, src,
    locus)` for score > 0, best first.

    **Ranked, not filtered, and that is the whole design.** The first version
    required ALL keywords and was tested on the query that actually mattered:
    `brane tower invariant` returned **nothing**, because the corpus states that
    result as `BraneTowerIsospinBlind` -- "isospin blind", never the word
    "invariant". An AND-filter fails exactly when your vocabulary differs from
    the author's, which is the case prior-art search exists for.

    Matching the **path** as well as the name is the other half. The Milnor
    producer `computations/binding_mn_milnor_linking.py` declares `mul`,
    `magnus_gen`, `magnus_word`, `comm`, `mu`, `main`: **not one name contains
    "milnor"**. The concept lives in the filename."""
    decls = decls if decls is not None else declarations()
    keys = [_flat(k) for k in keywords if k]
    if not keys: return []
    out = []
    for p, i, name, line in decls:
        fname, fpath = _flat(name), _flat(str(p))
        n_name = sum(1 for k in keys if k in fname)
        n_path = sum(1 for k in keys if k in fpath)
        score = max(n_name, n_path)
        if score:
            out.append((score, p, i, name, line, "name" if n_name >= n_path else "path"))
    out.sort(key=lambda h: (-h[0], str(h[1])))
    return out

SELFTEST = [  # (keywords, a declaration that MUST be found -- the five real misses)
    (["milnor"],              "computations/"),
    (["qint"],                "AJTrefoil"),
    (["subinvnezero"],        "QHookDimensionBalanced"),
    (["branetower"],          "BraneTowerIsospinBlind"),
    (["chirality"],           "frobenius-s-classification"),
]

def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--selftest"]
    if "--selftest" in sys.argv[1:]:
        decls = declarations()
        print(f"indexed {len(decls)} declarations")
        bad = 0
        for keys, must_contain in SELFTEST:
            found = probe(keys, decls)
            ok = any(must_contain in str(p) for _, p, _, _, _, _ in found)
            print(f"  {'PASS' if ok else 'FAIL'}  {'+'.join(keys):16s} -> "
                  f"{len(found):3d} hits, expected one under {must_contain!r}")
            bad += 0 if ok else 1
        print("selftest:", "all five known misses are caught" if not bad else f"{bad} REGRESSION(S)")
        return 1 if bad else 0
    if not args:
        print(__doc__); return 2
    found = probe(args)
    n = len(args)
    if not found:
        print(f"nothing in the corpus names or is filed under any of {args!r}.")
        print("Evidence of absence for the VOCABULARY only. Before writing "
              "'no result exists', grep the docstrings and docs/audits/ too — "
              "a result can be stated under a word you did not guess.")
        return 0
    best = found[0][0]
    print(f"{len(found)} hit(s) for {' + '.join(args)!r}; best matches {best}/{n} "
          f"keyword(s). Ranked, not filtered — read the top rows even if the "
          f"score is partial, since the corpus may use different words.\n")
    shown, seen_paths = 0, set()
    for score, p, i, name, line, locus in found:
        if score < best: break            # only the top tier by default
        rel = p.relative_to(ROOT)
        if locus == "path":
            if rel in seen_paths: continue
            seen_paths.add(rel)
            print(f"  [{score}/{n} path] {rel}   (concept in the FILENAME, not in a declaration name)")
        else:
            print(f"  [{score}/{n} name] {rel}:{i}\n        {line[:100]}")
        shown += 1
        if shown >= 40:
            print(f"  ... {len(found) - shown} further hit(s) suppressed; narrow the keywords.")
            break
    lower = [h for h in found if h[0] < best]
    if lower:
        print(f"\n  ({len(lower)} lower-scoring hit(s) not shown — re-run with "
              f"fewer keywords to see them.)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
