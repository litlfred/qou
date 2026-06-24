#!/usr/bin/env python3
"""Status-label overclaim audit — devil's-advocate class-2 checker.

Catches blocks that wear a confidence label ("proved", "verified",
"closed form", "no-fitting", "RESOLVED", "exact", "✅ proved") while a
non-closure signal in the SAME block contradicts it — the failure class
the devils-advocate watcher surfaced three times (e.g. "✅ proved" over a
§3b-cond `True`-skeleton; `"no-fitting"` tag on a +5.9%-miss near-match;
`status:"verified"` over an empty-assertion witness).

This is a HEURISTIC, high-recall flagger — every hit is a *candidate*
overclaim for an agent/author to confirm, not a proven defect. It is NOT
a da-* sidecar producer (the da-axis is agent-only by design); it feeds
the watcher's backlog.

A block is flagged when BOTH hold:
  (a) a confidence LABEL appears in its `.md` or `.ts` (tags / prose), and
  (b) a NON-CLOSURE SIGNAL appears in the same block triple:
      - `.lean` contains `sorry`, `:= trivial`, `: True`, or `native_decide`
      - `.ts` has `validation: "not_checked"|"stub"` or `status:
        "experimental"|"draft"|"wip"`
      - the block `kind` is `conjecture`
      - a sibling `.qa.json` records a `result: "fail"` on any criterion

Report-only by default (exit 0). `--strict` exits 1 on any hit.

Usage:
  python3 computations/status_label_overclaim_audit.py [--strict] [--json]
"""
from __future__ import annotations
import json, re, sys, glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Closure claims only. Generic "verified"/"exact" are dropped — they are
# witness-status words, not proof-confidence claims, and flooded the
# signal. These remaining labels each assert a CLOSED result.
LABELS = [
    r"✅\s*proved", r"\bproved\b", r"\bclosed[ -]form\b",
    r"\bno[- ]fitting\b", r"\bno[- ]fit\b", r"\bRESOLVED\b",
    r"\bsorry-free\b", r"\brigorous(ly)? (derived|proved)\b",
]
LABEL_RE = re.compile("|".join(LABELS))
# Labels we treat as honest when the block kind warrants — see below.
LEAN_BAD = (re.compile(r"\bsorry\b"), re.compile(r":=\s*trivial\b"),
            re.compile(r":\s*True\b"), re.compile(r"\bnative_decide\b"))
TS_BAD = re.compile(r'(validation|status)\s*:\s*"(not_checked|stub|experimental|draft|wip)"')
KIND_CONJ = re.compile(r'kind\s*:\s*"conjecture"|^export default conjecture\(', re.M)


def read(p):
    try:
        return open(p, encoding="utf-8").read()
    except Exception:
        return ""


def qa_has_fail(qa_path) -> bool:
    if not os.path.exists(qa_path):
        return False
    try:
        doc = json.load(open(qa_path))
    except Exception:
        return False
    for crit, entries in (doc.get("criteria") or {}).items():
        if crit.startswith("da-"):
            continue  # don't let the watcher's own findings self-trigger
        if entries and isinstance(entries, list):
            last = entries[-1]
            if last.get("result") == "fail":
                return True
    return False


def audit_block(ts_path) -> dict | None:
    base = ts_path[:-3]
    md, ts = read(base + ".md"), read(ts_path)
    lean = read(base + ".lean") if os.path.exists(base + ".lean") else ""

    label_hits = sorted({m.group(0) for m in LABEL_RE.finditer(md + "\n" + ts)})
    if not label_hits:
        return None

    signals = []
    if lean:
        for rx in LEAN_BAD:
            m = rx.search(lean)
            if m:
                signals.append(f"lean:{m.group(0).strip()}")
                break
    if TS_BAD.search(ts):
        signals.append("ts:" + TS_BAD.search(ts).group(0))
    is_conj = bool(KIND_CONJ.search(ts))
    if is_conj:
        signals.append("kind:conjecture")
    # qa:fail intentionally NOT a signal — stale bib/cite criteria make it
    # too noisy; the hard signals above (lean sorry/:True/stub, conjecture,
    # not_checked) are the actionable class-2 pattern.

    if not signals:
        return None
    # A `conjecture` block carrying "proved"/"verified" is the sharpest
    # overclaim; flag conjecture+label even if that's the only signal.
    return {"block": os.path.relpath(base, ROOT),
            "labels": label_hits, "signals": signals}


def main() -> int:
    strict = "--strict" in sys.argv
    as_json = "--json" in sys.argv
    hits = []
    for ts in sorted(glob.glob(os.path.join(ROOT, "content", "**", "*.ts"),
                               recursive=True)):
        if "/schema/" in ts or "/pipeline/" in ts or ts.endswith(".d.ts"):
            continue
        h = audit_block(ts)
        if h:
            hits.append(h)
    if as_json:
        print(json.dumps(hits, indent=2))
    else:
        if not hits:
            print("status-label-overclaim: clean — no label/non-closure conflicts.")
        else:
            print(f"status-label-overclaim: {len(hits)} candidate(s) "
                  f"(label + contradicting non-closure signal):\n")
            for h in hits:
                print(f"  {h['block']}")
                print(f"      labels:  {', '.join(h['labels'])}")
                print(f"      signals: {', '.join(h['signals'])}")
    return 1 if (strict and hits) else 0


if __name__ == "__main__":
    sys.exit(main())
