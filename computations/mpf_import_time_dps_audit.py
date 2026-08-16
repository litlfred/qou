#!/usr/bin/env python3
# polynomial_q_not_applicable: source-hygiene audit, no q-dependence.
"""Catch mpf constants built at IMPORT time, when mp.dps is still 15.

Owner directive: NO FLOAT64.

This closes the gap the other two float64 gates structurally cannot see.

    witness_float64_padding_audit.py   finds padding sitting in a witness
    mpf_float_source_audit.py          finds mpf(<float literal>) in source
    THIS                               finds mpf("<string>") built too early

The third is invisible to the second because the call is *already the
compliant form*. `mp.mpf("2.22456607")` is exactly what the source audit
tells you to write. But at module scope it runs at IMPORT time, when
`mp.dps` is still mpmath's default **15** — about binary64. The value is
rounded to ~53 bits before `set_compute_dps()` is ever called, and raising
dps afterwards cannot recover what was already discarded. Serialize it at
50 dps and you print the binary64 expansion:

    mp.mpf("2.22456607")  built at dps=15, printed at 50 dps
      -> 2.2245660699999998399789546965621411800384521484375000...
                          ^^^ binary64 expansion, i.e. float64 padding

So **string-sourcing is necessary but not sufficient — the timing matters
too.** This is why a corpus with 5661 compliant `mpf("...")` call sites
still regenerated 289 padded fields on a single producer re-run.

The correct forms, both already used in this corpus:

    with mp.workdps(max(50, mp.mp.dps)):     # codata_constants._ame_binding_mev
        return +(mp.mpf(str(x)) / 1000)

    set_compute_dps()                        # 152 producers, at module level
    CONST = mp.mpf("2.22456607")             # ...then build constants

**Exactly-representable literals are not flagged** — `mpf(0)`, `mpf(1)`,
`mpf("0.5")`, `mpf("1e-40")`-style tolerances that survive the round trip
lose nothing by being built early. The discriminator is direct: build the
literal at dps=15 and again at dps=60; if they differ, precision was lost.

History: found 2026-08-07 while draining the re-padders measured in
docs/audits/2026-08-07-producer-repadding-empirical-sweep.md. The clean
sibling `binding_depth_stratified.py` reads its constants from
`codata_constants` (workdps-wrapped); the three that re-padded hand-typed
the same numbers at module scope.

RATCHET, not pass/fail (2026-08-10, bean qou-j6gb)
--------------------------------------------------
This audit was written 2026-08-07, worked from the start, and was wired to
NOTHING — it is absent from `scripts/precision-gates.sh`'s `GATES` array, and
since `witness-staleness.yml` is `workflow_dispatch:` only under the owner's
2026-06-30 Actions-billing directive, that script IS the gate. So the detector
for this defect class sat unrun while the class itself landed five more times
(`VOL_41`, `gram_qtrace`'s q0, `TOLERANCE_PPQ`, `REG_ZC`/`REG_ZD`) — each caught
instead by a different gate reacting to a downstream symptom.

The reason it was never wired is the obvious one: 288 findings across 91 files
makes a blocking pass/fail gate red on day one, and a gate that is red on
arrival gets skipped, which is how a checker goes quiet in the first place.

So it enforces the same shape as `witness_raw_float64_audit.py`: the existing
backlog is recorded in `mpf-import-time-dps-baseline.json` and tolerated; a file
NOT in the baseline fails, and a baselined file whose count INCREASES fails.
The backlog may only shrink.

  * per-FILE granularity, deliberately. Per-line churns on every edit above the
    constant and is unreviewable; per-file is stable and still pins the count.
  * `literal` and `expr` counts are baselined and compared SEPARATELY. A
    `literal` finding is statically certain — the decimal string was parsed at
    15 dps and the digits are gone. An `expr` finding is only position-risky and
    some are fine. Summing them would let a proven defect hide behind an
    unproven one drained in the same file.
  * a file the audit CANNOT PARSE is never baselined and always fails `--strict`.
    That case is not "no findings", it is "no information", and treating the two
    alike is the exact bug bean qou-brkp records this audit having had once
    already. There are zero such files at baseline time.

Do not add a file to the baseline to silence a failure — fix it at the source.
The fix is one line: call the idempotent `set_compute_dps()` at module scope
ABOVE the constant.

Usage:
    python3 computations/mpf_import_time_dps_audit.py            # report
    python3 computations/mpf_import_time_dps_audit.py --strict   # exit 1 on NEW/REGRESSED
    python3 computations/mpf_import_time_dps_audit.py --rebaseline   # draining only
    python3 computations/mpf_import_time_dps_audit.py --self-test
"""
from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

from mpmath import mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BASELINE = HERE / "mpf-import-time-dps-baseline.json"
BROKEN_KINDS = ("syntax-error", "unreadable", "unparseable")

# Directories whose constants never reach a committed witness.
SKIP_DIRS = {"_deprecated", "__pycache__", "data"}


def loses_precision(literal: str) -> bool:
    """True if building this literal at dps=15 discards information.

    Exactly-representable values (integers, dyadic rationals) round-trip
    identically and are harmless to build early.
    """
    try:
        with mp.workdps(15):
            early = +mp.mpf(literal)
        with mp.workdps(60):
            late = +mp.mpf(literal)
        with mp.workdps(60):
            return +early != +late
    except Exception:
        return False


def _literal_of(call: ast.Call) -> str | None:
    """The constant argument of an mpf(...) call, as a string, if it is one."""
    if not call.args:
        return None
    a = call.args[0]
    if isinstance(a, ast.Constant) and isinstance(a.value, (str, int, float)):
        return str(a.value)
    # mpf(-x) — unary minus over a constant
    if (isinstance(a, ast.UnaryOp) and isinstance(a.op, ast.USub)
            and isinstance(a.operand, ast.Constant)):
        return f"-{a.operand.value}"
    return None


def _is_mpf(call: ast.Call) -> bool:
    f = call.func
    name = (f.attr if isinstance(f, ast.Attribute)
            else f.id if isinstance(f, ast.Name) else None)
    return name == "mpf"


def _raises_dps(stmt: ast.stmt) -> bool:
    """Does this module-scope statement raise working precision?

    Three idioms are in use here and all three count:
      set_compute_dps()          — 152 producers
      mp.dps = 50 / mp.mp.dps    — the option_e and probe families
      with mp.workdps(...)       — codata_constants
    """
    if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
        f = stmt.value.func
        name = (f.attr if isinstance(f, ast.Attribute)
                else f.id if isinstance(f, ast.Name) else None)
        if name in {"set_compute_dps", "workdps"}:
            return True
    if isinstance(stmt, ast.Assign):
        for t in stmt.targets:
            if isinstance(t, ast.Attribute) and t.attr == "dps":
                return True
    return False


def scan_file(path: Path) -> list[dict]:
    """Module-scope mpf literals built BEFORE precision is raised.

    Position matters: a constant appearing after a module-level
    `set_compute_dps()` / `mp.dps = 50` is built at full precision and is
    correct. Only what precedes the raise is lossy — so this walks module
    statements in order and stops flagging once precision has been set.

    ⚠ Every row this returns carries `file`. The three early-exit rows
    (`unreadable` / `syntax-error` / `unparseable`) once omitted it, and
    `main`'s per-file grouping does `r["file"]` — so the first unparseable file
    in the tree crashed the whole audit with `KeyError: 'file'`. That is
    *worse* than the silent `return []` this branch was added to replace: a
    false clean at least reported the other files. Caught by running the script
    against the real tree rather than against the one crafted bad file.
    """
    try:
        rel = path.relative_to(ROOT).as_posix()
    except ValueError:
        rel = path.as_posix()
    try:
        src = path.read_text(encoding="utf-8")
    except Exception as e:
        return [{"file": rel, "line": 0, "kind": "unreadable",
                 "text": f"{type(e).__name__}: {e}"}]
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        # A file that does not parse must NOT read as clean. `return []` here
        # made "unparseable" indistinguishable from "no findings" — and the
        # commit that introduced this audit (2bcbefee49) broke exactly two of
        # the fourteen files it edited, by inserting `mp.dps = 50` between a
        # dict's opening brace and its first entry. This audit reported both as
        # having nothing wrong, because they no longer parsed. A checker that
        # goes quiet on the files it broke is worse than no checker.
        return [{"file": rel, "line": e.lineno or 0, "kind": "syntax-error",
                 "text": f"file does not parse: {e.msg}"}]
    except Exception as e:
        return [{"file": rel, "line": 0, "kind": "unparseable",
                 "text": f"{type(e).__name__}: {e}"}]
    out: list[dict] = []
    # `if __name__ == "__main__":` bodies are scanned with their OWN raise
    # state, not the module's. Two reasons, and the second is the stronger:
    #
    #   1. Position still matters inside the block, so a constant built after
    #      an in-block `mp.dps = 50` is built at 50 dps and is correct. The
    #      outer loop only tested `_raises_dps` on TOP-LEVEL statements, so the
    #      whole guard was one opaque `ast.If` and an in-block raise was
    #      invisible -- while the `mpf(...)` calls inside it were still
    #      collected by `ast.walk`. 17 of the 21 in-guard findings in
    #      witness-emitting files were of exactly that shape.
    #   2. This audit is about IMPORT time -- its first line says so. A
    #      `__main__` body does not run on import at all.
    #
    # It is deliberately NOT a blanket skip of the guard. A `__main__` block
    # that builds constants BEFORE raising precision is a real precision defect,
    # just not an import-time one, and 4 such findings survive this change
    # (borromean_binding_recompute.py:172 x3, gram_matrix_seminormal_n.py:231);
    # both files are already baselined at exactly those counts, so nothing new
    # goes red. Skipping the guard outright would have hidden all four.
    def _collect(stmt, out_):
        for node in ast.walk(stmt):
            if not (isinstance(node, ast.Call) and _is_mpf(node)):
                continue
            lit = _literal_of(node)
            if lit is None:
                out_.append({"file": rel, "line": node.lineno,
                             "literal": None, "kind": "expr"})
                continue
            if loses_precision(lit):
                out_.append({"file": rel, "line": node.lineno,
                             "literal": lit, "kind": "literal"})

    def _walk_block(stmts, rel_out):
        for st in stmts:
            if isinstance(st, (ast.FunctionDef, ast.AsyncFunctionDef,
                               ast.ClassDef)):
                continue
            if _raises_dps(st):
                return                          # everything after is fine
            if isinstance(st, ast.With) and "workdps" in ast.dump(st):
                continue
            _collect(st, rel_out)

    for stmt in tree.body:                      # module scope only, in order
        if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            continue
        if _raises_dps(stmt):
            break                               # everything after is fine
        # `with mp.workdps(...)` at module scope is the correct pattern
        if isinstance(stmt, ast.With) and "workdps" in ast.dump(stmt):
            continue
        if isinstance(stmt, ast.If) and "__main__" in ast.dump(stmt.test):
            _walk_block(stmt.body, out)
            continue
        # mpf(<expression>) — e.g. mpf(str(G_A_PDG_ERR)) — is reported as
        # `expr`, not as proven: lossiness cannot be shown statically because
        # the value is not in the source, but the POSITION carries the same
        # risk. Skipping those was a real miss — gt_matrix_pslq_probe's
        # `PDG_G_A_ERR = mp.mpf(str(G_A_PDG_ERR))` emits
        # 0.00129999999999999994032551242639… for a datum of 0.0013.
        _collect(stmt, out)
    return out


def emits_witness(path: Path) -> bool:
    """Does this script write a committed witness?

    A constant that never reaches a witness can lose precision at import
    without misrepresenting anything — a plot bound or a grid step is not
    a claim. Restricting to witness-emitting scripts is what separates
    'lossy' from 'dishonest'.
    """
    try:
        s = path.read_text(encoding="utf-8")
    except Exception:
        return False
    return "WitnessBuilder" in s or ".witness.json" in s


def scan(all_files: bool = False) -> list[dict]:
    rows: list[dict] = []
    for p in sorted(HERE.rglob("*.py")):
        if set(p.relative_to(HERE).parts) & SKIP_DIRS:
            continue
        if p.name == Path(__file__).name:
            continue
        if not all_files and not emits_witness(p):
            continue
        rows.extend(scan_file(p))
    return rows


def self_test() -> int:
    cases = [
        # (literal, loses precision at dps=15?)
        ("2.22456607", True),    # the live instance
        ("7.7180428", True),
        ("28.295674", True),
        ("1.1099785955573347", True),
        ("0.5", False),          # dyadic — exact
        ("0", False),
        ("1", False),
        ("0.25", False),
    ]
    bad = 0
    for lit, want in cases:
        got = loses_precision(lit)
        if got != want:
            print(f"  FAIL {lit}: expected {want}, got {got}")
            bad += 1

    # `__main__`-guard scoping. The guard used to be one opaque module-level
    # `ast.If`: an in-block `mp.dps = 50` was invisible while the `mpf(...)`
    # calls after it were still collected, so a correct main block read as 5
    # findings. These four cases pin BOTH halves — the false positive must stay
    # dead, and the real defect must stay visible, or the fix has become a way
    # to silence the guard.
    import tempfile as _tf
    scan_cases = [
        ("raise-then-build inside __main__ is CLEAN",
         'import mpmath as mp\nif __name__ == "__main__":\n'
         '    mp.mp.dps = 50\n    x = mp.mpf("2.22456607")\n', 0),
        ("build-then-raise inside __main__ is still FLAGGED",
         'import mpmath as mp\nif __name__ == "__main__":\n'
         '    x = mp.mpf("2.22456607")\n    mp.mp.dps = 50\n', 1),
        ("no raise at all inside __main__ is still FLAGGED",
         'import mpmath as mp\nif __name__ == "__main__":\n'
         '    x = mp.mpf("2.22456607")\n', 1),
        ("a module-scope build before any raise is still FLAGGED",
         'import mpmath as mp\nx = mp.mpf("2.22456607")\n'
         'if __name__ == "__main__":\n    mp.mp.dps = 50\n', 1),
    ]
    for label, src, want in scan_cases:
        with _tf.NamedTemporaryFile("w", suffix=".py", delete=False) as fh:
            fh.write(src)
            tmp = Path(fh.name)
        got = len(scan_file(tmp))
        tmp.unlink(missing_ok=True)
        if got != want:
            print(f"  FAIL {label}: expected {want} finding(s), got {got}")
            bad += 1
    cases = list(cases) + scan_cases

    if bad:
        print(f"SELF-TEST FAILED — {bad}/{len(cases)}")
        return 1
    print(f"SELF-TEST PASSED — {len(cases)} cases: lossy literals detected, "
          f"exactly-representable ones not flagged.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if any import-time-lossy constant is found")
    ap.add_argument("--all", action="store_true",
                    help="include scripts that emit no witness (candidates, not defects)")
    ap.add_argument("--rebaseline", action="store_true",
                    help="regenerate the baseline (draining only — counts must go DOWN)")
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    rows = scan(all_files=a.all)
    by_file: dict[str, list[dict]] = {}
    for r in rows:
        by_file.setdefault(r["file"], []).append(r)

    scope = "all scripts" if a.all else "witness-emitting scripts"
    lit = sum(1 for r in rows if r.get("kind") == "literal")
    exp = sum(1 for r in rows if r.get("kind") == "expr")
    # Files that do not parse (or do not read) are reported FIRST and on their
    # own. Folding them into the ranked per-file list buried them: a broken file
    # yields one row, so it never reached the top-25 cut and the report looked
    # clean while the audit had in fact learned nothing about it. That is the
    # same silent-lie shape this audit was written to remove, one layer up.
    broken = [r for r in rows
              if r.get("kind") in ("syntax-error", "unreadable", "unparseable")]
    print(f"module-scope mpf built before precision is raised: {len(rows) - len(broken)}"
          f"  [{scope}]")
    print(f"   proven lossy (literal arg): {lit}")
    print(f"   position-risky (expr arg, not statically provable): {exp}")
    print(f"files affected: {len(by_file) - len(broken)}\n")
    if broken:
        print(f"⚠ {len(broken)} file(s) the audit could NOT read — "
              f"NOT a clean result for them, no claim is made about their contents:")
        for r in broken:
            print(f"  {r['file']}:{r['line']}  [{r['kind']}]  {r.get('text', '')}")
        print()
    ranked = {f: rs for f, rs in by_file.items()
              if any(r.get("kind") in ("literal", "expr") for r in rs)}
    for f in sorted(ranked, key=lambda k: -len(ranked[k]))[:25]:
        print(f"  {f}  ({len(by_file[f])})")
        for r in ranked[f][:3]:
            k = r.get("kind", "literal")
            arg = repr(r['literal']) if r.get('literal') is not None else '<expr>'
            print(f"      L{r['line']}: mpf({arg})  [{k}]")

    if rows:
        print("\nFix: build the constant at compute precision — either call "
              "set_compute_dps() at module level BEFORE it, or wrap "
              "construction in `with mp.workdps(max(50, mp.mp.dps)):`, or "
              "read it from codata_constants (already workdps-wrapped).")

    # ── RATCHET (bean qou-j6gb) ────────────────────────────────────────────
    # `--all` widens the scan to scripts that emit no witness, i.e. candidates
    # rather than defects. Those are not what the baseline records, so a widened
    # run reports but never ratchets — otherwise `--all` would look like 100+
    # NEW files against a baseline that never claimed to cover them.
    found = {f: {"literal": sum(1 for r in rs if r.get("kind") == "literal"),
                 "expr": sum(1 for r in rs if r.get("kind") == "expr")}
             for f, rs in by_file.items()
             if any(r.get("kind") in ("literal", "expr") for r in rs)}
    prior: dict[str, dict] = {}
    if BASELINE.exists():
        prior = json.loads(BASELINE.read_text())["files"]

    new_files = {f: c for f, c in found.items() if f not in prior}
    grew = {f: (prior[f], c) for f, c in found.items()
            if f in prior and (c["literal"] > prior[f].get("literal", 0)
                               or c["expr"] > prior[f].get("expr", 0))}
    drained = {f: (prior[f], found.get(f, {"literal": 0, "expr": 0}))
               for f in prior
               if (found.get(f, {}).get("literal", 0) < prior[f].get("literal", 0)
                   or found.get(f, {}).get("expr", 0) < prior[f].get("expr", 0))}

    if prior:
        b_lit = sum(c.get("literal", 0) for c in prior.values())
        b_exp = sum(c.get("expr", 0) for c in prior.values())
        print(f"\n  baseline files                 : {len(prior)}")
        print(f"  baseline literal / expr        : {b_lit:,} / {b_exp:,}")
        print(f"  now      literal / expr        : {lit:,} / {exp:,}"
              f"   ({lit - b_lit:+,} / {exp - b_exp:+,})")
        print(f"  NEW files (not baselined)      : {len(new_files)}")
        print(f"  REGRESSED (count increased)    : {len(grew)}")
        print(f"  drained since baseline         : {len(drained)} file(s)")

    if new_files:
        print("\n  NEW files building mpf before precision is raised — fix AT THE"
              "\n  SOURCE (idempotent set_compute_dps() at module scope, ABOVE the"
              "\n  constant). Do NOT add the file to the baseline to silence this.")
        for f, c in sorted(new_files.items(),
                           key=lambda kv: -(kv[1]["literal"] + kv[1]["expr"]))[:25]:
            print(f"    literal={c['literal']:<4d} expr={c['expr']:<4d}  {f}")
        if len(new_files) > 25:
            print(f"    ... and {len(new_files) - 25} more")

    if grew:
        print("\n  REGRESSED — these files gained import-time constants:")
        for f, (was, now) in sorted(grew.items())[:25]:
            print(f"    literal {was.get('literal', 0)} -> {now['literal']}, "
                  f"expr {was.get('expr', 0)} -> {now['expr']}  {f}")

    if drained:
        print(f"\n  Drained (progress): {len(drained)} file(s)")
        for f, (was, now) in sorted(drained.items())[:10]:
            print(f"    literal {was.get('literal', 0)} -> {now['literal']}, "
                  f"expr {was.get('expr', 0)} -> {now['expr']}  {f}")

    if a.rebaseline:
        if a.all:
            print("\nRefusing to --rebaseline under --all: that scan includes "
                  "scripts emitting no witness, which the baseline does not "
                  "cover. Re-run without --all.")
            return 1
        BASELINE.write_text(json.dumps(
            {"note": "Files building an mpf constant at module scope before "
                     "mp.dps is raised, by count. The backlog is tolerated; it "
                     "must only SHRINK. Regenerate ONLY when draining. Adding a "
                     "file here to silence a failure defeats the gate — fix at "
                     "the source instead (set_compute_dps() above the constant).",
             "enforced_rule": "AGENTS.md: NO-FLOAT64. String-sourcing an mpf is "
                              "necessary but not sufficient; the TIMING matters "
                              "too — at import mp.dps is still 15.",
             "granularity": "per-file, with `literal` and `expr` counted "
                            "separately: `literal` is statically proven lossy, "
                            "`expr` is only position-risky. Summing them would "
                            "let a proven defect hide behind an unproven one.",
             "drain_owner": "bean qou-j6gb (do the `literal` ones first)",
             "files_count": len(found),
             "literal_count": lit,
             "expr_count": exp,
             "files": dict(sorted(found.items()))}, indent=2) + "\n")
        print(f"\nRebaselined: {len(found)} files / {lit:,} literal / "
              f"{exp:,} expr recorded.")

    out = HERE / "mpf-import-time-dps-audit.witness.json"
    out.write_text(json.dumps({
        "schema": "witness/v1",
        "name": "mpf-import-time-dps-audit",
        "description": "Files building an mpf constant at module scope while "
                       "mp.dps is still mpmath's default 15. String-sourcing is "
                       "necessary but not sufficient — the timing matters too. "
                       "Ratchet only; drain owner is bean qou-j6gb.",
        "data": {
            "files_with_findings": len(found),
            "literal_findings": lit,
            "expr_findings": exp,
            "baseline_files": len(prior),
            "new_not_baselined": len(new_files),
            "regressed": len(grew),
            "drained_files": len(drained),
            "unparseable_files": len(broken),
        },
    }, indent=2) + "\n")
    print(f"\nWrote {out.name}")

    # A file the audit could not parse is never baselined and always fails
    # --strict. That case is not "no findings", it is "no information" — and
    # treating the two alike is exactly the bug bean qou-brkp records this audit
    # having had once already (a parse failure returned zero rows, so the audit
    # reported clean for the two files its own remediation had just broken).
    # There are zero such files at baseline time, so this cannot be red on
    # arrival; if one appears, that is a real regression and worth the stop.
    if a.strict and (new_files or grew or broken):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
