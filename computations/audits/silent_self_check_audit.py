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


# Agent verdicts. A high-recall axis needs a place to record "looked at it, it
# is fine", or the same candidates get re-investigated every pass.
#
# Triage 2026-08-16: of the 65 `self-check-not-gated` candidates, only TWO have
# a failing state recorded in a committed witness at all — and both are
# legitimate. Their single assertion is an EXISTENTIAL,
# `..._at_least_one_passes_10_ppm`; the per-k `passed: False` entries are the
# probe's measurement of which (convention, k) pairs meet 10 ppm, not assertions.
# k4 passes for every convention, so `allPassed: True` is right and the nested
# False values are data.
#
# So the axis currently has near-zero LIVE damage. Its value is forward-looking:
# it caught the shape in the two cases where it had already bitten (a live
# convention-split detector, and a 63 %-wrong consumed cache).
ADJUDICATED_LEGIT = {
    "computations/qbeta/qbeta_wenzl_habiro_chain_alpha.py":
        "assertion is existential (at_least_one_passes); per-k False is the "
        "measurement, not a failed check",
    "computations/qbeta/qbeta_kashaev_habiro_chain_beta.py":
        "same existential shape as the alpha probe",
}


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
    """A literal success exit — `return 0`, `return None`, `sys.exit(0)`.

    NOT `node.value in (0, None, True)`: in Python `1 == True`, so that
    spelling classified `sys.exit(1)` as a SUCCESS and reported an
    already-repaired script as still defective. Compare by identity/type.
    """
    if not isinstance(node, ast.Constant):
        return False
    v = node.value
    if v is None or v is True:
        return True
    return isinstance(v, int) and not isinstance(v, bool) and v == 0


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
        # Module-level script. Gated either when the exit VALUE mentions the
        # verdict, or — the common spelling, and the one `qou-9d6h` was fixed
        # with — when a non-zero exit sits inside an `if` that TESTS it:
        #
        #     if not witness["allPassed"]:
        #         sys.exit(1)
        #
        # An earlier cut only inspected exit arguments, so it reported that
        # already-repaired script as still defective. A false positive on a
        # fixed file is worse than a miss: it teaches readers to ignore the axis.
        gated = any(_mentions_verdict(a)
                    for n in ast.walk(tree) if isinstance(n, ast.Call)
                    and (getattr(n.func, "attr", None) == "exit")
                    for a in n.args)
        if not gated:
            for node in ast.walk(tree):
                if not isinstance(node, ast.If) or not _mentions_verdict(node.test):
                    continue
                for sub in ast.walk(node):
                    if isinstance(sub, ast.Call) and \
                            getattr(sub.func, "attr", None) == "exit" and sub.args and \
                            not _is_literal_success(sub.args[0]):
                        gated = True
                        break
                if gated:
                    break
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
            if not (".exists()" in seg and ("json.load" in seg or "read_text" in seg)):
                continue
            # A BASELINE read is not a resume cache. The ratchet audits
            # (`witness_raw_float64_audit`, `never_raises_dps_audit`, …) load a
            # *separate* baseline file to report drift against — they are not
            # skipping work, and the loaded file is not the one they write.
            # Four of the nine candidates were this, and flagging a ratchet for
            # reading its own ratchet is exactly the noise that gets an axis
            # ignored.
            if re.search(r"\bBASELINE\b|baseline", seg):
                continue
            # The read must be of the file this script WRITES. Reading an
            # UPSTREAM input on `.exists()` is ordinary dependency loading, not
            # a resume cache — `nucleus_real_sdp` reads the y_λ witnesses,
            # `deuteron_tr_M_symbolic` reads chi-deuteron-h6. Neither resumes
            # anything of its own, and flagging them is the same category error
            # as flagging the ratchets for reading a baseline.
            #
            # Proxy: the path expression guarding the load must also appear in
            # a write. Cheap and conservative — it misses a resume cache whose
            # read and write name the path differently, which is a miss rather
            # than a false accusation.
            paths = {n.id for n in ast.walk(node.test) if isinstance(n, ast.Name)}
            paths |= {n.attr for n in ast.walk(node.test) if isinstance(n, ast.Attribute)}
            # `open(P, "w")` counts as a write. Restricting to `.write_text(`
            # and `json.dump(` MISSED `ordering_cache`, which writes with
            # `with open(CACHE_FILE, "w") as f: json.dump(..., f)` — the path
            # and the dump are on different lines. That is the miss this
            # comment predicted, found by checking the drop rather than
            # trusting it.
            if not any(re.search(rf"\b{re.escape(p)}\b[^\n]*"
                                 rf"(\.write_text\(|json\.dump\()|"
                                 rf"(write_text|json\.dump)\([^\n]*\b{re.escape(p)}\b|"
                                 rf"open\(\s*{re.escape(p)}\s*,\s*[\"']w",
                                 src) for p in paths if p):
                continue
            ev.append(f"line {node.lineno}: loads the file it also WRITES, "
                      f"when it exists")
    if not ev:
        return []
    # ...and that loaded content is used to skip work
    reuses = (re.search(r"\bin (already|existing|cached|prior|seen)\b", src)
              or re.search(r"if \w+ in \w*(cache|already|existing)\w*", src))
    if not reuses:
        return []
    # GUARDED resumes are not the defect. `chi_at_q0_via_hoefsmit_mpfr`
    # compares the STORED q₀ against the current one and discards on
    # mismatch, and offers `--fresh` for a cache that was already relabelled.
    # That is the correct shape, and flagging it would train readers to
    # ignore this axis. Only an UNCONDITIONAL resume is reported.
    guarded = (re.search(r"prev_q\b|q0 CHANGED|q_0_50dps.*!=|!=.*q_0_50dps", src)
               or re.search(r"\bfresh\b.*discard|discard.*\bfresh\b", src, re.I)
               or re.search(r"source_hash|deps_hash|scriptHash", src))
    if guarded:
        return []
    ev.append("reuses those entries to SKIP recomputation with NO q₀/hash "
              "guard — a stale cache is served back on every re-run")
    return ev


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
    adjudicated: list[dict] = []
    scanned: list[str] = []
    unparseable: list[str] = []

    for p in sorted((ROOT / "computations").rglob("*.py")):
        if "_deprecated" in p.parts or p.name == Path(__file__).name:
            continue
        src = p.read_text()
        rel = str(p.relative_to(ROOT))
        scanned.append(rel)
        try:
            tree = ast.parse(src)
        except SyntaxError as exc:
            # NOT clean: a file that does not parse is a file no criterion ran
            # against. It also silently satisfies the regression check below,
            # which reads "fixed" from ABSENCE among the findings.
            unparseable.append(f"{rel}: {exc.__class__.__name__}")
            continue
        for crit, fn, sev in (("self-check-not-gated", detect_not_gated, "critical"),
                              ("resume-cache-unvalidated", detect_resume_cache, "major")):
            ev = fn(p, src, tree)
            if not ev:
                continue
            if rel in ADJUDICATED_LEGIT and crit == "self-check-not-gated":
                adjudicated.append({"script": rel, "criterion": crit,
                                    "verdict": "legit",
                                    "why": ADJUDICATED_LEGIT[rel]})
                continue
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
    print(f"  {'adjudicated legit':<28} {len(adjudicated)} (agent-reviewed, excluded above)")
    print(f"  {'scripts scanned':<28} {len(scanned) - len(unparseable)} of {len(scanned)}")
    if unparseable:
        print(f"  {'UNPARSEABLE (no criterion ran)':<28} {len(unparseable)}")
        for u in unparseable:
            print(f"      {u}")

    # Regression check. Both scripts below carried a REAL defect found by hand,
    # and both have since been repaired — matrix-M got the q₀ resume guard,
    # deuteron_tower got a non-zero exit. So the honest assertion is "each is
    # either flagged or demonstrably fixed", NOT "each is still flagged": a
    # bare count reads as a detector regression the moment a repair lands.
    REPAIRED = {
        "computations/chi_at_q0_via_matrix_m_mpfr.py":
            "q₀ resume guard + --fresh ported from the hoefsmit producer",
        "computations/substrate/deuteron_tower_fusion_frame_probe.py":
            "exits 1 when allPassed is False (qou-9d6h)",
    }
    flagged = {f["script"] for f in findings}
    # "fixed" is read from ABSENCE among the findings, and a script that failed
    # to parse is also absent. Without this third state a syntax error in a
    # watched file reports as a repair.
    unparsed_scripts = {u.split(":", 1)[0] for u in unparseable}
    print("\n  regression check — each hand-found defect is flagged or fixed:")
    for s, how in sorted(REPAIRED.items()):
        if s in unparsed_scripts:
            state = "UNKNOWN — this file did not parse, so no criterion ran on it"
        elif s in flagged:
            state = "still FLAGGED"
        else:
            state = f"fixed — {how}"
        print(f"    {s}\n        {state}")

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
                 "scan_coverage": {
                     "scripts_seen": len(scanned),
                     "scripts_parsed": len(scanned) - len(unparseable),
                     "unparseable": unparseable,
                 },
                 "regression_repaired_still_flagged": sorted(flagged & set(REPAIRED)),
                 "adjudicated_legit": adjudicated,
                 "findings": findings},
    }, indent=2) + "\n")
    print(f"\n  witness -> {out.relative_to(ROOT)}")

    if args.write_sidecars:
        # PRUNE first. A sidecar flag must disappear when the defect does,
        # or the axis accumulates accusations against repaired code and stops
        # being readable. This run already dropped 13 entries that a `1 == True`
        # bug in `_is_literal_success` had invented.
        ours = {(f["script"], f["criterion"]) for f in findings}
        CRITS = {"self-check-not-gated", "resume-cache-unvalidated"}
        n_pruned = 0
        for side in sorted((ROOT / "computations").rglob("*.script-qa.json")):
            if "_deprecated" in side.parts:
                continue
            try:
                doc = json.loads(side.read_text())
            except json.JSONDecodeError:
                continue
            sp = doc.get("script_path", "")
            drop = [c for c in list(doc.get("criteria", {}))
                    if c in CRITS and (sp, c) not in ours]
            if not drop:
                continue
            for c in drop:
                del doc["criteria"][c]
                n_pruned += 1
            doc["updated_at"] = now
            side.write_text(json.dumps(doc, indent=2) + "\n")
        if n_pruned:
            print(f"  pruned {n_pruned} stale criterion entr(ies)")
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
