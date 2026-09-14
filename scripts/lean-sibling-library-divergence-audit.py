#!/usr/bin/env python3
"""Find content-block siblings that DECLARE a name the library also declares.

Why this exists
---------------
`conj:b1-hyperbolic-rows-theorem` had an inconsistent axiom repaired on
2026-08-08 in `lean/QOU/AppendixSurreals/B1HyperbolicRowsTheorem.lean`.  The
**sibling** kept the pre-repair version, and a `False` was still derivable from
it on 2026-09-03 -- reproduced, not inferred.  Nothing in the corpus checks that
a library file and its sibling agree, and the sibling is the copy `lean.ref`
resolves to FIRST (AGENTS.md 0a candidate 1), so it is the one a reader reaches.

What this can and cannot see
----------------------------
It compares DECLARATION TEXT after normalising whitespace and stripping
comments.  It therefore:

  * CAN see a sibling and a library file declaring the same fully-qualified
    name with different statements -- the class that produced the incident;
  * CAN see a sibling declaring an `axiom` where the library has a `theorem`,
    `class` or `structure`, which is strictly worse whether or not the text
    differs;
  * CANNOT see semantic divergence between statements that happen to be
    textually equal after normalisation, nor divergence carried by a shared
    helper rather than by the named declaration itself.

It also builds a declaration's fully-qualified name by concatenating EVERY
`namespace` line in the file, which is wrong for a file that opens and closes
several sibling namespaces in sequence.  Measured 2026-09-03: **55 of 908
sibling files (6.1%) and 216 of 2537 library files (8.5%)** have more than one
distinct namespace, so those files get wrong names.  A wrong concatenated
namespace is very unlikely to collide with a real one, so the error direction is
MISSED pairs rather than invented ones -- read the counts as a **lower bound**.

So a clean run is evidence about NAMES, not about meanings.  Do not quote it as
"the siblings agree with the library".

Verdicts
--------
  divergent-axiom  sibling declares `axiom`, library declares something else
                   -- read first, this is the incident's shape
  divergent        same fully-qualified name, different normalised statement
  duplicate        same name, same statement -- redundant, 0a says drop it

Epistemic ranking
-----------------
A raw `divergent` count is alarming and mostly boring: the bulk is a sibling
restating a declaration with different binders or formatting.  What matters is
whether the two copies disagree about **proof status**, because that is what
misleads a reader who follows `lean.ref` to the sibling.  So the report also
buckets by kind pair, worst first:

  sibling claims PROVED, library ASSUMES   sibling `theorem`/`lemma` against a
                                           library `axiom`/`opaque` -- a reader
                                           sees a proof where the corpus assumes
  sibling ASSUMES, library does not        the `categorical_jet_prolongation`
                                           and b1-hyperbolic-rows shape
  kind mismatch X vs Y                     structural, usually benign
  same kind, text differs                  the boring bulk

Measured 2026-09-03: the first bucket is **0** and the second is **1**.  Quote
that split, not the raw 201 -- I first reported the 201 as needing per-pair
judgement, which overstated it.
"""
from __future__ import annotations
import re, sys, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPER = ROOT / "content" / "quantum-observable-universe"
LIB = PAPER / "lean"

KINDS = ("axiom", "theorem", "lemma", "def", "abbrev", "class", "structure",
         "instance", "opaque", "inductive")
DECL_RE = re.compile(
    r"^\s*(?:@\[[^\]]*\]\s*)?"
    r"(?:noncomputable\s+|private\s+|protected\s+|scoped\s+|partial\s+)*"
    r"(" + "|".join(KINDS) + r")\s+([A-Za-z_][A-Za-z0-9_'!?.]*)",
    re.M,
)
NS_RE = re.compile(r"^\s*namespace\s+([A-Za-z_][A-Za-z0-9_'.]*)", re.M)
# `section` takes MODIFIERS — `noncomputable section` is the common one here —
# so anchoring the keyword at line start misses it while its bare `end` still
# pops the stack. Measured: that single spelling blanked the namespace for
# every declaration after line 49 of `heisenberg-commutator-prop.lean`, losing
# three true file pairs. A named `section Foo` is legal too, so the name is
# optional for `section` and required for `namespace`.
NS_OPEN_RE = re.compile(
    r"^\s*(?:noncomputable\s+|private\s+|protected\s+|scoped\s+|unsafe\s+|partial\s+)*"
    r"(namespace|section)(?:\s+([A-Za-z_][A-Za-z0-9_'.]*))?\s*$"
)
NS_END_RE = re.compile(r"^\s*end\s*([A-Za-z_][A-Za-z0-9_'.]*)?\s*$")


def namespace_at(body: str) -> list[tuple[int, str]]:
    """(offset, enclosing-namespace) checkpoints, from a real OPEN/END STACK.

    Replaces `".".join(NS_RE.findall(body))`, which concatenated EVERY
    `namespace` line in the file regardless of whether it was still open.  The
    script's own docstring named that as its known limitation and predicted the
    error direction correctly — MISSED pairs, so every count it produced was a
    lower bound.

    Confirmed instance, which is what this fix is verified against:
    `lean/QOU/BraidKnot/HeckeAnyonicSubstrate.lean` opens `namespace
    QOU.BraidKnot`, closes the class, then opens a NESTED `namespace
    HeckeAnyonicSubstrate` for the class's lemmas.  Concatenation gave the
    class the name `QOU.BraidKnot.HeckeAnyonicSubstrate.HeckeAnyonicSubstrate`,
    which matches nothing — so its duplicate in
    `nuclear-interactions/hecke-anyonic-substrate.lean`, a DIFFERENT class of
    the same real name `QOU.BraidKnot.HeckeAnyonicSubstrate` in the SAME
    namespace, was invisible.

    `section` is tracked alongside `namespace` because a `section ... end` pair
    otherwise pops a namespace off the stack — the same defect
    `lean-duplicate-fqn-audit.py` records having had to fix.  Only `namespace`
    frames contribute to the name; `section` frames are pushed so that their
    `end` consumes the right frame and no more.
    """
    stack: list[tuple[str, str]] = []          # (kind, name)
    checkpoints: list[tuple[int, str]] = []
    off = 0
    for line in body.splitlines(keepends=True):
        m = NS_OPEN_RE.match(line)
        if m and (m.group(1) == "section" or m.group(2)):
            stack.append((m.group(1), m.group(2) or ""))
        else:
            e = NS_END_RE.match(line)
            if e:
                want = e.group(1)
                if want:
                    for i in range(len(stack) - 1, -1, -1):
                        if stack[i][1] == want:
                            del stack[i:]
                            break
                    else:
                        if stack:
                            stack.pop()
                elif stack:
                    stack.pop()
        checkpoints.append(
            (off, ".".join(n for k, n in stack if k == "namespace" and n))
        )
        off += len(line)
    return checkpoints


def ns_for_offset(checkpoints: list[tuple[int, str]], pos: int) -> str:
    lo, hi, best = 0, len(checkpoints) - 1, ""
    while lo <= hi:
        mid = (lo + hi) // 2
        if checkpoints[mid][0] <= pos:
            best = checkpoints[mid][1]; lo = mid + 1
        else:
            hi = mid - 1
    return best


def _blank_keep_newlines(m: re.Match) -> str:
    """Replace a comment with spaces, PRESERVING its newlines and length."""
    return "".join("\n" if c == "\n" else " " for c in m.group(0))


def strip_comments(text: str) -> str:
    # Blank comments IN PLACE rather than collapsing them to a single space,
    # so that line structure survives for the line-based namespace stack below.
    #
    # HONESTY NOTE: I introduced this believing it was what lost three true
    # file pairs. It was not — measured, it changes no verdict on this corpus
    # (207 file pairs either way); the real cause was `noncomputable section`,
    # fixed in NS_OPEN_RE. It is kept because a line-based scan should not
    # depend on comments happening not to precede a `namespace` line, and
    # because it keeps byte offsets aligned for `ns_for_offset`. The normalised
    # statement text is unchanged either way (whitespace collapses downstream).
    text = re.sub(r"/-.*?-/", _blank_keep_newlines, text, flags=re.S)
    text = re.sub(r"--[^\n]*", _blank_keep_newlines, text)
    return text


def declarations(path: Path) -> dict[str, tuple[str, str]]:
    """fully-qualified name -> (kind, normalised statement text)."""
    raw = path.read_text(encoding="utf8", errors="replace")
    body = strip_comments(raw)
    checkpoints = namespace_at(body)
    out: dict[str, tuple[str, str]] = {}
    hits = list(DECL_RE.finditer(body))
    for i, m in enumerate(hits):
        start = m.start()
        end = hits[i + 1].start() if i + 1 < len(hits) else len(body)
        stmt = " ".join(body[start:end].split())
        name = m.group(2)
        ns = ns_for_offset(checkpoints, start)   # the namespace OPEN AT THIS DECL
        fq = f"{ns}.{name}" if ns and not name.startswith(ns) else name
        out[fq] = (m.group(1), stmt)
    return out


def main() -> int:
    lib_files = sorted(LIB.rglob("*.lean"))
    lib_files = [p for p in lib_files if ".lake" not in p.parts]
    lib: dict[str, tuple[str, str, Path]] = {}
    for p in lib_files:
        for fq, (kind, stmt) in declarations(p).items():
            lib.setdefault(fq, (kind, stmt, p))

    sib_files = [p for p in sorted(PAPER.rglob("*.lean"))
                 if LIB not in p.parents and p != LIB]

    findings = []
    for p in sib_files:
        for fq, (kind, stmt) in declarations(p).items():
            if fq not in lib:
                continue
            lkind, lstmt, lpath = lib[fq]
            if kind == "axiom" and lkind != "axiom":
                verdict = "divergent-axiom"
            elif stmt != lstmt:
                verdict = "divergent"
            else:
                verdict = "duplicate"
            findings.append({
                "name": fq,
                "verdict": verdict,
                "sibling": str(p.relative_to(ROOT)),
                "sibling_kind": kind,
                "library": str(lpath.relative_to(ROOT)),
                "library_kind": lkind,
            })

    ASSUMED = {"axiom", "opaque"}
    PROVED = {"theorem", "lemma"}
    for f in findings:
        sk, lk = f["sibling_kind"], f["library_kind"]
        if f["verdict"] == "duplicate":
            f["risk"] = "duplicate"
        elif sk in PROVED and lk in ASSUMED:
            f["risk"] = "sibling claims PROVED, library ASSUMES"
        elif sk in ASSUMED and lk not in ASSUMED:
            f["risk"] = "sibling ASSUMES, library does not"
        elif sk != lk:
            f["risk"] = f"kind mismatch {sk} vs {lk}"
        else:
            f["risk"] = f"same kind ({sk}), text differs"

    order = {"divergent-axiom": 0, "divergent": 1, "duplicate": 2}
    findings.sort(key=lambda f: (order[f["verdict"]], f["name"]))

    print(f"sibling .lean files scanned : {len(sib_files)}")
    print(f"library .lean files scanned : {len(lib_files)}")
    print(f"library declarations indexed: {len(lib)}")
    print()
    for v in ("divergent-axiom", "divergent", "duplicate"):
        n = sum(1 for f in findings if f["verdict"] == v)
        print(f"  {n:4d}  {v}")
    print()
    print("  by epistemic risk (worst first):")
    RISK_ORDER = ["sibling claims PROVED, library ASSUMES",
                  "sibling ASSUMES, library does not"]
    seen = {}
    for f in findings:
        seen[f["risk"]] = seen.get(f["risk"], 0) + 1
    def rank(k: str) -> tuple:
        return (RISK_ORDER.index(k) if k in RISK_ORDER else len(RISK_ORDER),
                -seen[k], k)
    for k in sorted(seen, key=rank):
        print(f"  {seen[k]:4d}  {k}")
    print()
    for f in findings:
        if f["verdict"] == "duplicate":
            continue
        print(f"[{f['verdict']}] {f['name']}")
        print(f"    sibling {f['sibling_kind']:9s} {f['sibling']}")
        print(f"    library {f['library_kind']:9s} {f['library']}")

    if len(sys.argv) > 2 and sys.argv[1] == "--json":
        Path(sys.argv[2]).write_text(json.dumps(findings, indent=2), encoding="utf8")
        print(f"\nwrote {sys.argv[2]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
