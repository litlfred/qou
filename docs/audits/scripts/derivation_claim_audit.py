#!/usr/bin/env python3
"""Where does the paper claim something is DERIVED when it is actually assumed?

Bean `qou-5r17`. Prompted by the #5044 retraction: the Ch9 §1 opener said the
pairwise result was "forced by the braiding rather than assumed" when the
hexagon identities are CLASS FIELDS of Mathlib's `BraidedCategory` — axioms.

## Why this is not a grep

A bare search for "derived" returns ~450 hits across ~290 files and is almost
all noise: `def:derived-atom` is a defined term, "derived from the Markov trace"
is an ordinary and correct usage, "derived category" is standard vocabulary.

The claims that matter are PREDICATIVE — prose asserting that some X is derived
*rather than* assumed. Those carry an epistemic claim that can be wrong. This
script surfaces those and ranks them by whether the subject is something the
corpus itself declares as an axiom, a definition, or a conjecture.

## The verdict is still an agent call

Every row is a CANDIDATE. Deciding whether a claim is earned needs reading what
discharges it: proved from stated axioms (earned), a rearrangement of an axiom
(not earned), an axiom itself (not earned), or conditional on a class-axiomatised
conjecture (not earned — the §3b-cond / "conditional-proved ≠ premise-established"
case). The script cannot do that. It narrows ~450 to something readable.

Usage:
  python3 -u docs/audits/scripts/derivation_claim_audit.py 2>&1 | tee /tmp/derivaudit.log
  python3 -u docs/audits/scripts/derivation_claim_audit.py --json
"""
from __future__ import annotations

import json
import os
import re
import sys
from glob import glob
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
CONTENT = REPO / "content/quantum-observable-universe"
OUT = Path(__file__).with_suffix(".witness.json")

# Predicative derivation claims. The contrastive forms ("not assumed", "rather
# than assumed", "forced by") are the high-risk ones: they explicitly deny that
# something is an assumption, which is exactly the claim that can be false.
CONTRASTIVE = re.compile(
    r"(?:not\s+(?:assumed|postulated|imposed|stipulated)"
    r"|rather\s+than\s+(?:assumed|postulated|imposed|stipulated)"
    r"|forced\s+by"
    r"|(?:is|are)\s+not\s+a\s+(?:choice|convention|assumption)"
    r"|emerges?\s+(?:rather\s+than|not\s+by))",
    re.I,
)
# Weaker: a plain predicative "is/are derived". Legitimate far more often.
PREDICATIVE = re.compile(
    r"\b(?:is|are|was|were|becomes?)\s+(?:therefore\s+|thus\s+|then\s+)?derived\b", re.I
)
# Noun usages to discount entirely.
NOUN_NOISE = re.compile(
    r"derived\s+(?:atom|category|categories|functor|series|set|from\s+the\s+"
    r"(?:AME|CODATA|PDG))", re.I
)

LABEL = re.compile(r"\b(?:def|thm|lem|prop|cor|conj|rem|ax[a-z]*):[a-z0-9][a-z0-9-]*")


def sentences(text: str):
    """Crude sentence split that keeps display math intact enough for context."""
    for para in text.split("\n\n"):
        flat = " ".join(para.split())
        for s in re.split(r"(?<=[.!?])\s+", flat):
            if s.strip():
                yield s.strip()


def axiom_like_labels() -> dict[str, str]:
    """Labels whose block kind means 'assumed, not proved'.

    definition  — names a construction; nothing is proved
    conjecture  — explicitly open
    Both are things a 'derived, not assumed' claim must not be about.
    """
    kinds = {}
    for ts in glob(str(CONTENT / "*/*.ts")):
        try:
            src = open(ts).read()
        except Exception:
            continue
        m = re.search(r'label:\s*"([^"]+)"', src)
        if not m:
            continue
        label = m.group(1)
        if re.search(r"\bdefinition\(\{", src):
            kinds[label] = "definition"
        elif re.search(r"\bconjecture\(\{", src):
            kinds[label] = "conjecture"
    return kinds


def lean_axiom_names() -> set[str]:
    """Declarations that are structurally ASSUMED: Lean `axiom`s, and `class`
    carriers used via the §3b-cond conditional pattern."""
    names = set()
    for f in glob(str(REPO / "content/**/lean/**/*.lean"), recursive=True):
        if "/.lake/" in f:
            continue
        try:
            src = open(f).read()
        except Exception:
            continue
        for m in re.finditer(r"^\s*(?:axiom|class)\s+([A-Za-z_][A-Za-z0-9_.']*)", src, re.M):
            names.add(m.group(1))
    return names


def main() -> None:
    as_json = "--json" in sys.argv
    kinds = axiom_like_labels()
    lean_axioms = lean_axiom_names()

    rows = []
    for md in sorted(glob(str(CONTENT / "*/*.md"))):
        rel = os.path.relpath(md, REPO)
        try:
            text = open(md).read()
        except Exception:
            continue
        for s in sentences(text):
            if NOUN_NOISE.search(s):
                continue
            contrastive = bool(CONTRASTIVE.search(s))
            predicative = bool(PREDICATIVE.search(s))
            if not (contrastive or predicative):
                continue
            labels = LABEL.findall(s)
            assumed = sorted({l for l in labels if kinds.get(l) in ("definition", "conjecture")})
            rows.append(
                {
                    "file": rel,
                    "sentence": s[:400],
                    "contrastive": contrastive,
                    "labels_in_sentence": sorted(set(labels)),
                    "assumed_labels_in_sentence": assumed,
                    # tier 1 is the retraction's own shape: a contrastive denial
                    # of assumption sitting next to a definition or conjecture.
                    "tier": 1 if (contrastive and assumed) else (2 if contrastive else 3),
                }
            )

    rows.sort(key=lambda r: (r["tier"], r["file"]))
    t1 = [r for r in rows if r["tier"] == 1]
    t2 = [r for r in rows if r["tier"] == 2]
    t3 = [r for r in rows if r["tier"] == 3]

    if not as_json:
        print(f"corpus: {len(glob(str(CONTENT / '*/*.md')))} .md files")
        print(f"blocks classified assumed-kind: {len(kinds)} "
              f"(definition/conjecture); lean axiom+class names: {len(lean_axioms)}")
        print(f"\ncandidates: {len(rows)}  "
              f"[tier1 {len(t1)} | tier2 {len(t2)} | tier3 {len(t3)}]\n")
        print("TIER 1 — contrastive denial of assumption, next to a definition/conjecture")
        print("         (this is the shape the #5044 retraction had)\n")
        for r in t1:
            print(f"  {r['file']}")
            print(f"    {r['sentence'][:200]}")
            print(f"    assumed-kind labels: {', '.join(r['assumed_labels_in_sentence'])}\n")
        print(f"\nTIER 2 — contrastive denial of assumption, no assumed-kind label in sentence"
              f"  ({len(t2)} rows; listing files only)")
        for f in sorted({r["file"] for r in t2}):
            print(f"  {f}")

    OUT.write_text(
        json.dumps(
            {
                "schema": "qou-audit-probe/v1",
                "bean": "qou-5r17",
                "question": (
                    "Where does the corpus claim something is derived / not assumed / "
                    "forced, about something that is actually assumed?"
                ),
                "method": (
                    "Predicative + contrastive claim detection over content .md, "
                    "cross-referenced against blocks whose kind is definition or "
                    "conjecture. Tiering is heuristic; every row is an agent-judged "
                    "candidate, not a finding."
                ),
                "counts": {"total": len(rows), "tier1": len(t1), "tier2": len(t2), "tier3": len(t3)},
                "tier1": t1,
                "tier2": t2,
            },
            indent=2,
        )
        + "\n"
    )
    if not as_json:
        print(f"\nwrote {os.path.relpath(OUT, REPO)}")


if __name__ == "__main__":
    main()
