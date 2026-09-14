#!/usr/bin/env python3
"""Detect declarations whose NAME asserts a mathematical STRUCTURE their own
STATEMENT does not contain.

Sibling of `scripts/lean-borrowed-name-audit.py`, and written because that one
is blind to this by construction (detector-blindness taxonomy row 46).  The
borrowed-name audit asks *"is this named after an external BODY whose theorem it
does not use?"* and gates on a table of 54 surnames:

    hits = borrowed_hits(name, doc)
    if not hits: continue                    # line 316

`pole_cusp_bijection_proved` borrowed no eponym.  It borrowed **content** —
*cusp*, *bijection*, *proved* — none of which appears in

    ∃ z : Fin n → ℝ, (∀ k, z k = q^(-k)) ∧ (∀ k, denomPolyLocal q (z k) n = 0)

so `borrowed_hits` returned `[]` and it was discarded before LOCAL-ONLY,
OVERCLAIM or CHEAP was ever evaluated.

**The second half is the one worth internalising: that detector HELD the token
and never looked where it was written.**  `borrowed_hits` reads
`split_camel(name) + " " + doc`, but `overclaim = bool(OVERCLAIM.search(doc))`
(line 338) reads the docstring ALONE — and `OVERCLAIM` matches `'proved'`.  One
signal in that script reads the name and the other does not, for no design
reason.  Measured cost of the asymmetry: 10 of 25,810 provable declarations.

## What this keys on, and the one calibration that matters

A name token that names a STRUCTURE, paired with the Lean token(s) that would
witness it in the statement.  A token present in the name and absent from the
statement is a candidate, never a verdict — `partitionDom_not_iff_lexGt`
refutes one direction of an iff and is defensibly named.

🛑 **The first version of this probe demanded `∃!`/`Unique`/`Subsingleton` for
`unique` and reported 173 hits.  Every one was Mathlib's uniqueness IDIOM** —
`(a b : T) (h…) : a = b`, which states uniqueness with no `∃!` anywhere.  That
is 173 false positives from one unknown-to-me convention, and it is exactly
taxonomy row 45's lesson (an audit that self-certifies its calibration cannot
discover its own blind spot) landing on the probe written to extend row 45.  So
`unique` is earned by an equational/iff/HEq conclusion, and `--selftest` pins
BOTH the catch and that limit.

Usage:
    scripts/lean-structure-word-audit.py                # report
    scripts/lean-structure-word-audit.py --token iff    # one token
    scripts/lean-structure-word-audit.py --rev REV      # measure a git revision
    scripts/lean-structure-word-audit.py --selftest     # gate
"""
from __future__ import annotations
import argparse, importlib.util, os, re, subprocess, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)

# Reuse the sibling's parser so the POPULATION is identical and a count here is
# comparable with a count there.
_spec = importlib.util.spec_from_file_location(
    "bna", os.path.join(HERE, "lean-borrowed-name-audit.py"))
_bna = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_bna)

# An equational / iff / HEq conclusion earns a uniqueness or injectivity name:
# Mathlib states "unique" as `(a b) … : a = b`, not as `∃!`.
EQ_CONCL = r"∃!|Unique|Subsingleton|=|↔|HEq|≃"

CLAIMS: dict[str, str] = {
    "biject":      r"Equiv|Bijective|≃|Bijection",
    "bijection":   r"Equiv|Bijective|≃|Bijection",
    "iff":         r"↔|Iff",
    "injective":   r"Injective|InjOn|" + EQ_CONCL,
    "surjective":  r"Surjective|SurjOn|∃|Set\.range|Function\.range",
    "unique":      EQ_CONCL,
    "iso":         r"≅|Iso\b|Equiv|≃|=",
    "isomorphism": r"≅|Iso\b|Equiv|≃|=",
    "continuous":  r"Continuous",
    "integrable":  r"Integrable|IntegrableOn",
}


def _sources(rev: str | None):
    if rev is None:
        for root in _bna.DEFAULT_ROOTS:
            for dp, dn, fn in os.walk(os.path.join(REPO, root)):
                dn[:] = [d for d in dn if d not in (".lake", "build", ".git")]
                for f in fn:
                    if f.endswith(".lean"):
                        p = os.path.join(dp, f)
                        yield (os.path.relpath(p, REPO),
                               open(p, encoding="utf-8", errors="replace").read())
        return
    listing = subprocess.run(["git", "-C", REPO, "ls-tree", "-r", "--name-only", rev],
                             capture_output=True, text=True).stdout.split("\n")
    for path in listing:
        if path.endswith(".lean") and any(path.startswith(r) for r in _bna.DEFAULT_ROOTS):
            yield path, subprocess.run(["git", "-C", REPO, "show", f"{rev}:{path}"],
                                       capture_output=True, text=True).stdout


def audit(rev: str | None = None, only: str | None = None):
    hits: dict[str, list] = defaultdict(list)
    total = 0
    for relpath, raw in _sources(rev):
        code = _bna.blank_comments(raw)
        for kind, name, lineno, body in _bna.decl_spans(code):
            if kind not in _bna.PROVABLE:
                continue
            total += 1
            short = name.split(".")[-1]
            toks = set(re.split(r"[_\s]+", _bna.split_camel(short).lower()))
            stmt, _ = _bna.split_statement(body)
            for tok, need in CLAIMS.items():
                if only and tok != only:
                    continue
                if tok in toks and not re.search(need, stmt):
                    hits[tok].append((relpath, lineno, short,
                                      re.sub(r"\s+", " ", stmt).strip()[:200]))
    return total, hits


def selftest() -> int:
    """Pin the CATCH and the LIMIT.  Row 45: a self-certifying calibration
    cannot discover its own blind spot, so neither assertion is hardcoded."""
    ok = True

    # CATCH -- the motivating declaration, at the commit before it was renamed.
    _, before = audit(rev="926f2c71ec^", only="bijection")
    names = [h[2] for h in before.get("bijection", [])]
    if names != ["pole_cusp_bijection_proved"]:
        print(f"  FAIL catch: expected exactly ['pole_cusp_bijection_proved'], got {names}")
        ok = False
    else:
        print("  ok  catch    : pole_cusp_bijection_proved is the sole `bijection` hit at 926f2c71ec^")

    # DRAIN -- and gone afterwards, so the probe tracks the fix rather than the file.
    _, after = audit(only="bijection")
    if after.get("bijection"):
        print(f"  FAIL drain: `bijection` should be empty now, got {after['bijection']}")
        ok = False
    else:
        print("  ok  drain    : zero `bijection` hits on the working tree")

    # LIMIT -- the uniqueness idiom must NOT be flagged.  If this fires, the
    # `unique` rule has regressed to demanding `∃!` and will report ~173 false
    # positives (see the module docstring).
    _, now = audit(only="unique")
    idiom = [h for h in now.get("unique", []) if re.search(r":\s*[^:]*=", h[3])]
    if idiom:
        print(f"  FAIL limit: Mathlib uniqueness idiom flagged ({len(idiom)}), e.g. {idiom[0][2]}")
        ok = False
    else:
        print("  ok  limit    : `(a b : T) … : a = b` uniqueness idiom is not flagged")

    print("selftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--rev", help="git revision to measure instead of the working tree")
    ap.add_argument("--token", help="restrict to one structure word")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()

    total, hits = audit(rev=a.rev, only=a.token)
    n = sum(len(v) for v in hits.values())
    print(f"rev={a.rev or 'WORKING TREE'}   provable={total}   unearned-structure-word={n}")
    for tok in sorted(hits, key=lambda t: -len(hits[t])):
        print(f"   {tok:<12} {len(hits[tok])}")
    print()
    for tok in sorted(hits):
        for relpath, lineno, short, stmt in hits[tok]:
            print(f"[{tok}] {relpath}:{lineno}  {short}")
            print(f"        {stmt}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
