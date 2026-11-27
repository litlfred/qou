#!/usr/bin/env python3
"""Base-ring audit: a shrink-only post-merge QA check on Lean (AGENTS.md §7c,
owner 2026-11-27, bean qou-8318).

On the algebraic side of the corpus, a Lean statement should use the weakest
typeclass that admits it. A field or division-ring binder, or a `field_simp`
call, marks a place where the statement may be
restatable over a commutative ring, usually with `q : Rˣ` for an invertible
parameter or by clearing denominators. This script counts those markers per
file and holds the counts to a baseline that only shrinks.

Scope. The paper's Lean tree minus:
  * `QOU/Transcendental/` (the analytic boundary, where fields are expected);
  * every module listed in `docs/audits/transcendental-boundary-baseline.json`
    (still analytic, on its way behind the boundary).
Comments, docstrings and string literals are stripped before matching.

Modes
  (default)  print totals by class and the largest files
  --write    write the baseline from the current tree (first run only:
             refuses to overwrite an existing baseline)
  --shrink   lower baseline counts to the current ones; never raises a count
  --check    exit 1 if any (file, class) count is above the baseline (NEW or
             GREW), or if a count dropped and the baseline was not shrunk (STALE)

Post-merge QA, not a pre-merge gate (owner ruling 2026-11-27: the KG JSON-LD
check is the only red gate before a merge). Run it on `main` after a merge (skill
`post-merge-rebuild`). A failure becomes a bean and a follow-up PR.

Never raise a baseline count by hand to get past --check. Restate the new
statement over a ring instead.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEAN = ROOT / "folio/quantum-observable-universe/lean"
BOUNDARY = "QOU/Transcendental/"
TRANS_BASELINE = ROOT / "docs/audits/transcendental-boundary-baseline.json"
BASELINE = ROOT / "docs/audits/base-ring-baseline.json"
SCHEMA = "base-ring-audit/v1"

CLASSES = {
    "field-class": r"\[\s*(?:Field|DivisionRing|LinearOrderedField|IsROrC|RCLike)\s",
    "field-tactic": r"\bfield_simp\b",
}
# Not counted, on purpose: `⁻¹` (braid generators σᵢ⁻¹ are group inverses, and
# Rˣ inverses are the very restatement this check pushes toward) and `ℚ`
# (concrete rational data is legitimate). Both would make every new braid or
# data file trip the check.
RX = {k: re.compile(v) for k, v in CLASSES.items()}


def strip_comments(src: str) -> str:
    out, i, depth, n = [], 0, 0, len(src)
    while i < n:
        if src.startswith("/-", i):
            depth += 1; i += 2; continue
        if depth and src.startswith("-/", i):
            depth -= 1; i += 2; continue
        if depth:
            i += 1; continue
        if src.startswith("--", i):
            j = src.find("\n", i); i = n if j < 0 else j; continue
        if src[i] == '"':
            j = i + 1
            while j < n and src[j] != '"':
                j += 2 if src[j] == "\\" else 1
            out.append('""'); i = j + 1; continue
        out.append(src[i]); i += 1
    return "".join(out)


def analytic_modules():
    if not TRANS_BASELINE.exists():
        return set()
    return set(json.loads(TRANS_BASELINE.read_text())["modules"])


def scan():
    skip = analytic_modules()
    hits = {}
    for p in sorted(LEAN.rglob("*.lean")):
        rel = p.relative_to(LEAN).as_posix()
        if rel.startswith(".lake/") or rel.startswith(BOUNDARY) or rel in skip:
            continue
        code = strip_comments(p.read_text(encoding="utf-8", errors="replace"))
        c = {k: len(rx.findall(code)) for k, rx in RX.items()}
        c = {k: v for k, v in c.items() if v}
        if c:
            hits[rel] = c
    return hits


def load():
    return json.loads(BASELINE.read_text())["files"]


def save(files):
    BASELINE.write_text(json.dumps({"schema": SCHEMA, "boundary": BOUNDARY,
                                    "classes": CLASSES, "files": files},
                                   indent=1, ensure_ascii=False, sort_keys=True) + "\n")


def compare(hits, base):
    grew, stale = [], []
    for f in sorted(set(hits) | set(base)):
        h, b = hits.get(f, {}), base.get(f, {})
        for k in CLASSES:
            if h.get(k, 0) > b.get(k, 0):
                grew.append((f, k, b.get(k, 0), h.get(k, 0)))
            elif h.get(k, 0) < b.get(k, 0):
                stale.append((f, k, b.get(k, 0), h.get(k, 0)))
    return grew, stale


def totals(d):
    return {k: sum(v.get(k, 0) for v in d.values()) for k in CLASSES}


def main():
    hits = scan()
    if "--write" in sys.argv:
        if BASELINE.exists():
            print(f"refusing: {BASELINE.relative_to(ROOT)} exists; use --shrink")
            return 2
        save(hits)
        print(f"wrote {len(hits)} files to {BASELINE.relative_to(ROOT)}")
        return 0
    if "--shrink" in sys.argv:
        base = load()
        new = {}
        for f, b in base.items():
            h = hits.get(f, {})
            m = {k: min(b.get(k, 0), h.get(k, 0)) for k in CLASSES}
            m = {k: v for k, v in m.items() if v}
            if m:
                new[f] = m
        save(new)
        print(f"shrunk baseline: {len(base)} -> {len(new)} files; totals {totals(new)}")
        grew, _ = compare(hits, new)
        for f, k, b, h in grew:
            print(f"GREW {f} {k}: {b} -> {h}  (not absorbed; restate over a ring)")
        return 1 if grew else 0
    if "--check" in sys.argv:
        base = load()
        grew, stale = compare(hits, base)
        for f, k, b, h in grew:
            tag = "NEW " if f not in base else "GREW"
            print(f"{tag} {f}  {k}: {b} -> {h}")
        for f, k, b, h in stale:
            print(f"STALE {f}  {k}: {b} -> {h}  (run --shrink)")
        print(f"algebraic side: {len(hits)} files (baseline {len(base)}); "
              f"totals {totals(hits)}; grew {len(grew)}, stale {len(stale)}")
        return 1 if (grew or stale) else 0
    t = totals(hits)
    print(f"algebraic-side files with field markers: {len(hits)}")
    for k, v in t.items():
        print(f"  {k}: {v} in {sum(1 for x in hits.values() if k in x)} files")
    for f, c in sorted(hits.items(), key=lambda x: -sum(x[1].values()))[:15]:
        print(f"  {sum(c.values()):5d} {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
