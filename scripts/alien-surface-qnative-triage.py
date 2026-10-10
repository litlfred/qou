#!/usr/bin/env python3
r"""
alien-surface-qnative-triage.py — Brick 0 of the q-native alien calculus epic (qou-frzo).

## What this answers

The corpus has a large alien/Borel/Stokes Lean surface, mostly sorry-free. The closure
audit `2026-08-08-rsz-c1-infinity-route-closed.md` says C1 **cannot** be confluenced to
the classical setting, so any classical-only brick is a TRAP: it compiles, it is
sorry-free, it looks applicable, and it silently assumes a limit that does not exist
for this object.

**Sorry-freeness says the proofs are complete. It says nothing about whether the
STATEMENTS apply to a q-difference object.** That distinction is what this triages, and
it is criterion (D) of `qou-frzo`'s acceptance definition -- the one condition of the
four that a script can decide rather than a reviewer.

## Method, and its deliberate limits

For each file, extract every declaration SIGNATURE -- the text from the declaration
keyword up to `:=` or `by` -- and classify by which markers appear THERE:

  * **q-marker**    : the statement quantifies over a q-difference object
                      (`qShift`, `qBorel`, `qInt`, `Habiro`, `markovZ`, `σ`, `q ^`, ...)
  * **classical-marker**: the statement quantifies over a continuous/archimedean object
                      (`deriv`, `HasDerivAt`, `Continuous`, `Tendsto`, `∫`, `Real.exp`, ...)

Signatures only -- NOT proof bodies, NOT docstrings. A `Real.exp` inside a proof is an
implementation detail; a `Real.exp` in the statement is a commitment about the domain.
A docstring mentioning "q-analogue" is a claim, not a type.

**Two limits stated up front, because a triage that oversells itself is worse than
none:**

1. This decides criterion (D) only. (A) domain class, (B) twisted Leibniz and
   (C) commutation with `sigma_q` are mathematical judgements no grep can make. A file
   marked Q-NATIVE here has passed the cheapest gate, not all four.
2. `CLASSICAL-ONLY` is not an accusation. Much of this surface was built for classical
   resurgence and is correct there. The finding is about REUSE for the q-object.

## Population

Two populations are reported, deliberately:

  * **by filename** -- the obvious set. This is the selection method that failed me
    earlier in this same session (`ColourCubicBranchLocus` is named for its conclusion,
    not its topic, and a filename filter missed it).
  * **by content** -- files whose declarations carry alien/Borel/Stokes vocabulary
    regardless of name.

The difference between the two is itself reported. If content finds files that filename
misses, the filename set was never the surface.

Usage:  python3 scripts/alien-surface-qnative-triage.py [--json OUT]
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

LEAN_ROOT = pathlib.Path("folio/quantum-observable-universe/lean/QOU")

DECL = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+|private\s+|protected\s+)*"
                  r"(theorem|lemma|def|abbrev|structure|class|instance)\s+([A-Za-z_][^\s:(){\[]*)",
                  re.M)

Q_MARKERS = [
    "qShift", "qBorel", "qInt", "Habiro", "markovZ", "qDeriv", "qDifference",
    "QDiff", "qFactorial", "qBinom", "σ", "qPochhammer", "qExp", "qAnalog",
]
CLASSICAL_MARKERS = [
    "deriv", "HasDerivAt", "Continuous", "Tendsto", "Filter", "∫", "Real.exp",
    "Real.log", "Real.sqrt", "Complex.exp", "Complex.log", "AnalyticAt",
    "AnalyticOn", "DifferentiableAt", "MeromorphicAt", "nhds", "𝓝",
]
TOPIC_MARKERS = ["alien", "borel", "stokes", "resurgen", "instanton", "watson", "ecalle", "écalle"]


def signatures(text: str) -> list[tuple[str, str, str]]:
    """(kind, name, signature-text) for each declaration; signature = up to := or by."""
    out = []
    for m in DECL.finditer(text):
        kind, name = m.group(1), m.group(2)
        rest = text[m.end():]
        # cut at the first := or standalone `by` at the top level of the signature
        cut = len(rest)
        for pat in (r":=", r"\bby\b"):
            mm = re.search(pat, rest)
            if mm and mm.start() < cut:
                cut = mm.start()
        out.append((kind, name, rest[:cut]))
    return out


def strip_comments(text: str) -> str:
    text = re.sub(r"/-.*?-/", " ", text, flags=re.S)   # block + docstrings
    text = re.sub(r"--[^\n]*", " ", text)              # line comments
    return text


def classify(path: pathlib.Path) -> dict:
    raw = path.read_text(encoding="utf-8", errors="replace")
    body = strip_comments(raw)
    sigs = signatures(body)
    q_hits, c_hits = {}, {}
    for kind, name, sig in sigs:
        for mk in Q_MARKERS:
            if mk in sig:
                q_hits.setdefault(mk, []).append(name)
        for mk in CLASSICAL_MARKERS:
            if re.search(r"\b" + re.escape(mk) + r"\b" if mk.isalnum() or "." in mk else re.escape(mk), sig):
                c_hits.setdefault(mk, []).append(name)
    has_q, has_c = bool(q_hits), bool(c_hits)
    if has_q and not has_c:
        verdict = "Q-NATIVE-CANDIDATE"
    elif has_c and not has_q:
        verdict = "CLASSICAL-ONLY"
    elif has_q and has_c:
        verdict = "MIXED"
    else:
        verdict = "NEITHER"
    return {
        "path": str(path), "decls": len(sigs), "verdict": verdict,
        "q_markers": sorted(q_hits), "classical_markers": sorted(c_hits),
    }


def topical(path: pathlib.Path) -> bool:
    body = strip_comments(path.read_text(encoding="utf-8", errors="replace")).lower()
    return any(t in body for t in TOPIC_MARKERS)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", help="write full result here")
    a = ap.parse_args()

    if not LEAN_ROOT.exists():
        print(f"lean root not found: {LEAN_ROOT}", file=sys.stderr)
        return 2

    all_lean = sorted(LEAN_ROOT.rglob("*.lean"))
    name_re = re.compile(r"alien|borel|resurg|stokes|instanton|watson", re.I)
    by_name = {p for p in all_lean if name_re.search(p.name)}
    by_content = {p for p in all_lean if topical(p)}

    print("=" * 74)
    print("BRICK 0 — q-native vs classical-only triage of the alien/Borel/Stokes surface")
    print("=" * 74)
    print(f"\nPOPULATION")
    print(f"  by filename : {len(by_name)}")
    print(f"  by content  : {len(by_content)}")
    only_content = sorted(by_content - by_name)
    print(f"  content-only (filename selection MISSED these): {len(only_content)}")
    for p in only_content[:12]:
        print(f"      {p.relative_to(LEAN_ROOT)}")
    if len(only_content) > 12:
        print(f"      ... and {len(only_content)-12} more")

    surface = sorted(by_name | by_content)
    results = [classify(p) for p in surface]

    order = ["Q-NATIVE-CANDIDATE", "MIXED", "CLASSICAL-ONLY", "NEITHER"]
    counts = {v: sum(1 for r in results if r["verdict"] == v) for v in order}
    print(f"\nVERDICTS over the union ({len(surface)} files)")
    for v in order:
        print(f"  {v:22s} {counts[v]:4d}")

    for v in order:
        rows = [r for r in results if r["verdict"] == v]
        if not rows:
            continue
        print(f"\n--- {v} ({len(rows)}) ---")
        for r in sorted(rows, key=lambda r: -r["decls"])[:18]:
            rel = pathlib.Path(r["path"]).relative_to(LEAN_ROOT)
            mk = ",".join((r["q_markers"] + r["classical_markers"])[:4])
            print(f"  {r['decls']:4d} decls  {str(rel):58s} {mk}")
        if len(rows) > 18:
            print(f"  ... and {len(rows)-18} more")

    print("\nSCOPE: this decides criterion (D) ONLY -- no archimedean/confluence")
    print("dependence in the STATEMENTS. (A) domain class, (B) twisted Leibniz and")
    print("(C) commutation with sigma_q are mathematical judgements no grep can make.")
    print("CLASSICAL-ONLY is not an accusation: that work is correct for classical")
    print("resurgence. The finding is about REUSE for the q-object.")

    if a.json:
        pathlib.Path(a.json).write_text(json.dumps(
            {"population": {"by_filename": len(by_name), "by_content": len(by_content),
                            "content_only": [str(p) for p in only_content]},
             "counts": counts, "results": results}, indent=2))
        print(f"\nwrote {a.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
