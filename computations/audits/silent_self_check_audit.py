#!/usr/bin/env python3
# polynomial_q_not_applicable: static source audit; computes no substrate quantity.
"""`silent-self-check` QA axis — a producer that grades itself and then exits 0.

Two defects found by hand in one session, both with the same shape, both
invisible to every gate:

* `qou-9d6h` — `deuteron_tower_fusion_frame_probe` wrote `allPassed: False` and
  exited 0. Its failing assertion was the live detector for the `pyhecke` C/D
  convention split. The regeneration harness recorded it `ok`.
* `qou-7bv5` — `chi_at_q0_via_matrix_m_mpfr` printed
  `cross-check vs chi_q_via_gp: 0/11 match` and exited 0. The deuteron χ cache
  it was grading was stale: **0 of 11** per-λ values matched and `tr_M` was off
  by **63 %**. Every consumer of that cache had been reading it.

Neither was caught by CI, by the witness ratchets, or by the regeneration
harness — because each producer's own verdict never reached its exit status.
The harness reads exit codes; the verdict went to stdout and to a JSON field
nothing gates on.

## The two detectors

`self-check-not-gated` (critical)
    The script computes a self-check — a match count, a pass/fail flag, an
    `allPassed`, a mismatch tally — and no `return`/`sys.exit` depends on it.
    Every exit path is a literal success.

`resume-cache-unvalidated` (major)
    The script reads back a file it also writes and reuses entries from it to
    SKIP recomputation, without re-validating them. This is what made
    `qou-7bv5` durable rather than transient: `build_chi_cache_at_q0_matrix_m`
    loads existing entries into `already` and only fills gaps, so a stale cache
    is served straight back and survives every re-run. Deleting the file was
    the only way to regenerate it.

## Calibration

High-recall candidates, agent-confirmed — the same discipline as the Lean
vacuity audit. A self-check that is *reported* to a human caller rather than
gated can be legitimate (an exploratory probe whose whole output is the
comparison). What is never legitimate is a PRODUCER whose committed witness is
consumed downstream. Severity is therefore the judgement call, not the match.

Usage:
    python3 computations/audits/silent_self_check_audit.py [--strict] [--write-sidecars]
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SELF_ID = "computations/audits/silent_self_check_audit.py"

# Names that denote a self-grading result rather than ordinary data.
# Deliberately NARROW. An earlier cut accepted `ok`, `passed`, `matches`,
# `agree`, `discrepancy` and returned 595 candidates, then 334 — neither is a
# gate. These are the names that denote a COUNTABLE failure or an explicit
# all-or-nothing verdict, which is what both real defects carried
# (`n_match`/`n_total` in qou-7bv5, `allPassed` in qou-9d6h).
VERDICT_NAME = re.compile(
    r"^(n_match(es)?|n_mismatch\w*|n_fail\w*|n_bad|n_err\w*|"
    r"all_?[Pp]assed|allPassed|n_total_fail\w*|mismatch(es)?|failures)$")
# Printed text that reads as a verdict.
VERDICT_TEXT = re.compile(r"\b(match|mismatch|FAIL|PASS|agree|cross-check|"
                          r"disagree|allPassed)\b", re.I)


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:12]


def _exit_values(fn: ast.FunctionDef) -> list[ast.AST]:
    """Every value a `return` or `sys.exit` hands back from this function."""
    out: list[ast.AST] = []
    for node in ast.walk(fn):
        if isinstance(node, ast.Return) and node.value is not None:
            out.append(node.value)
        elif isinstance(node, ast.Call):
            f = node.func
            name = getattr(f, "attr", None) or getattr(f, "id", None)
            if name == "exit" and node.args:
                out.append(node.args[0])
    return out


def _is_literal_success(node: ast.AST) -> bool:
    return isinstance(node, ast.Constant) and node.value in (0, None, True)


def _mentions_verdict(node: ast.AST) -> bool:
    for sub in ast.walk(node):
        if isinstance(sub, ast.Name) and VERDICT_NAME.search(sub.id):
            return True
        if isinstance(sub, ast.Attribute) and VERDICT_NAME.search(sub.attr):
            return True
        if isinstance(sub, ast.Constant) and isinstance(sub.value, str) \
                and VERDICT_NAME.search(sub.value):
            return True
    return False


def _has_self_check(tree: ast.AST, src: str) -> list[str]:
    """Evidence that the script grades itself — a verdict VARIABLE, not a print.

    Deliberately narrow. The first cut of this detector also accepted any
    printed line containing "match"/"PASS"/"FAIL" and returned 595 candidates,
    which is not a gate — most probes print such a line legitimately. What
    distinguishes the two real defects is a verdict held in a VARIABLE (a match
    count, a boolean flag) that the exit path then ignores.
    """
    ev = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and VERDICT_NAME.search(t.id):
                    ev.append(f"line {node.lineno}: assigns verdict `{t.id}`")
        elif isinstance(node, ast.AugAssign):
            t = node.target
            if isinstance(t, ast.Name) and VERDICT_NAME.search(t.id):
                ev.append(f"line {node.lineno}: tallies `{t.id}`")
        elif isinstance(node, ast.Subscript):
            sl = node.slice
            if isinstance(sl, ast.Constant) and isinstance(sl.value, str) \
                    and VERDICT_NAME.search(sl.value):
                ev.append(f"line {node.lineno}: records verdict "
                          f"field `{sl.value}`")
    return ev[:6]


def _writes_witness(src: str) -> bool:
    """Is this a PRODUCER — does it commit a witness a consumer will read?

    The filter that makes the axis actionable. An exploratory probe whose whole
    output is a printed comparison is legitimately ungated; a producer whose
    committed witness is consumed downstream is not. `qou-7bv5` was durable
    precisely because the bad numbers were in a committed cache.
    """
    return bool(re.search(r"\.witness\.json|WitnessBuilder|add_assertion\(", src))


def detect_not_gated(path: Path, src: str, tree: ast.AST) -> list[str]:
    if not _writes_witness(src):
        return []                          # not a producer — ungated is fine
    checks = _has_self_check(tree, src)
    if not checks:
        return []
    fns = [n for n in ast.walk(tree)
           if isinstance(n, ast.FunctionDef) and n.name in ("main", "run")]
    if not fns:
        # Module-level script: gated only if it calls sys.exit on a verdict.
        gated = any(_mentions_verdict(a)
                    for n in ast.walk(tree) if isinstance(n, ast.Call)
                    and (getattr(n.func, "attr", None) == "exit")
                    for a in n.args)
        return [] if gated else checks
    for fn in fns:
        vals = _exit_values(fn)
        if not vals:
            continue
        if any(_mentions_verdict(v) for v in vals):
            return []                      # exit depends on the verdict — fine
        if all(_is_literal_success(v) for v in vals):
            return checks
    return []


def detect_resume_cache(path: Path, src: str, tree: ast.AST) -> list[str]:
    """Reads back a file it also writes, and skips recomputation from it."""
    writes = bool(re.search(r"\.write_text\(|json\.dump\(", src))
    if not writes:
        return []
    ev = []
    for node in ast.walk(tree):
        # `if <path>.exists():` guarding a load
        if isinstance(node, ast.If):
            seg = ast.get_source_segment(src, node) or ""
            if ".exists()" in seg and ("json.load" in seg or "read_text" in seg):
                ev.append(f"line {node.lineno}: loads its own prior output "
                          f"when the file exists")
    if not ev:
        return []
    # ...and that loaded content is used to skip work
    if re.search(r"\bin (already|existing|cached|prior|seen)\b", src) or \
       re.search(r"if \w+ in \w*(cache|already|existing)\w*", src):
        ev.append("reuses those entries to SKIP recomputation "
                  "(stale entries survive every re-run)")
        return ev
    return []


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 when any candidate is found")
    ap.add_argument("--write-sidecars", action="store_true",
                    help="record the criterion into each script's "
                         "*.script-qa.json sidecar")
    args = ap.parse_args()

    self_hash = _digest(Path(__file__).read_text())
    now = datetime.now(timezone.utc).isoformat()
    findings: list[dict] = []

    for p in sorted((ROOT / "computations").rglob("*.py")):
        if "_deprecated" in p.parts or p.name == Path(__file__).name:
            continue
        src = p.read_text()
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        rel = str(p.relative_to(ROOT))
        for crit, fn, sev in (("self-check-not-gated", detect_not_gated, "critical"),
                              ("resume-cache-unvalidated", detect_resume_cache, "major")):
            ev = fn(p, src, tree)
            if ev:
                findings.append({"script": rel, "criterion": crit,
                                 "severity": sev, "evidence": ev,
                                 "source_hash": _digest(src)})

    by_crit: dict[str, int] = {}
    for f in findings:
        by_crit[f["criterion"]] = by_crit.get(f["criterion"], 0) + 1

    print("=" * 72)
    print("SILENT-SELF-CHECK AUDIT — producers that grade themselves and exit 0")
    print("=" * 72)
    for c, n in sorted(by_crit.items()):
        print(f"  {c:<28} {n} candidate(s)")
    print(f"  {'total':<28} {len(findings)}")

    known = {"computations/chi_at_q0_via_matrix_m_mpfr.py",
             "computations/substrate/deuteron_tower_fusion_frame_probe.py"}
    hit = {f["script"] for f in findings} & known
    print(f"\n  regression check — the two hand-found defects are detected: "
          f"{len(hit)}/2  {sorted(hit)}")

    print("\n  candidates:")
    for f in sorted(findings, key=lambda x: (x['criterion'], x['script']))[:40]:
        print(f"    [{f['severity']:<8}] {f['criterion']:<26} {f['script']}")
        print(f"        {f['evidence'][0][:96]}")

    out = ROOT / "computations" / "audits" / "silent-self-check-audit.witness.json"
    out.write_text(json.dumps({
        "computation": "silent-self-check-audit",
        "description": (
            "Producers whose self-check does not reach their exit status, and "
            "producers that reuse their own prior output without re-validating "
            "it. High-recall candidates; the legit/genuine verdict is an agent "
            "call. Motivated by qou-9d6h and qou-7bv5, both of which reported a "
            "real defect into a channel nothing gates on."),
        "computedAt": now,
        "scriptFile": SELF_ID,
        "data": {"by_criterion": by_crit, "total": len(findings),
                 "regression_known_defects_detected": sorted(hit),
                 "findings": findings},
    }, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(ROOT)}")

    if args.write_sidecars:
        n_side = 0
        for f in findings:
            sp = ROOT / f["script"]
            side = sp.parent / "script-qa" / f"{sp.stem}.script-qa.json"
            side.parent.mkdir(exist_ok=True)
            doc = json.loads(side.read_text()) if side.exists() else {
                "$schema": "script-qa/v1", "script_path": f["script"],
                "language": "python", "source_hash": f["source_hash"],
                "updated_at": now, "criteria": {}}
            doc.setdefault("criteria", {})[f["criterion"]] = [{
                "field_hash": {"py": f["source_hash"]},
                "result": "fail",
                "reviewer": {"kind": "script", "id": SELF_ID,
                             "version": "v1", "script_hash": self_hash},
                "reviewed_at": now,
                "severity": f["severity"],
                "evidence": " | ".join(f["evidence"]),
            }]
            doc["updated_at"] = now
            side.write_text(json.dumps(doc, indent=2) + "\n")
            n_side += 1
        print(f"  wrote {n_side} sidecar criterion entr(ies)")

    return 1 if (args.strict and findings) else 0


if __name__ == "__main__":
    sys.exit(main())
