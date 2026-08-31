#!/usr/bin/env python3
# polynomial_q_not_applicable: infra audit; no symbolic-q logic.
"""Do a witness's recorded assertions still hold? (the third member of the family)

A committed `*.witness.json` records `allPassed: true` and a list of assertions
with the values that produced that verdict. Nothing checks that re-running the
producer TODAY still yields those values. So a witness can sit on `main`
asserting a green verdict that its own producer no longer reproduces, and every
existing gate passes it.

WHY THIS IS A GAP AND NOT A DUPLICATE
-------------------------------------

Four auditors already look at witnesses. None covers this:

* `witness_hollowness_audit`        — green with NO assertions behind it.
* `witness_failed_assertion_audit`  — recorded `allPassed: false`, committed anyway.
* `witness_producer_executes_audit` — can the producer still RUN? (not: does it
                                      still agree)
* `witness_reproducibility_check`   — byte-equality, and for `*.derivation.json`.

The uncovered case is the quiet one: **recorded green, no longer true.** The
verdict was correct when written; the code moved; nobody re-ran it. The
staleness machinery keys on `scriptHash` / `scriptCommitSha` — on whether the
PRODUCER changed — never on whether the ANSWER still reproduces. A witness whose
producer is untouched but whose *dependencies* moved is invisible to all of it.

THREE INSTANCES, FOUND BY HAND, 15 DAYS APART
---------------------------------------------

Each was found by an agent who happened to re-run one producer:

* `qou-u6cz` (2026-08-15) `qbeta-ck-basis-constrained-pslq.witness.json` —
  "asserts allPassed:true for a chain that now FAILS".
* `qou-wlaf` (2026-08-25) `gram-norm-binding-probe.witness.json` — "fails its
  own cross-check assertion by 7 orders of magnitude".
* `qou-i7ju` (2026-08-30) `hadron-knot-table.witness.json` — `tr_M(protium)`
  asserts 1.123183539266; the tree computes 1.1463376906350053, 2.1 % out, and
  measurably NOT caused by the change that found it.

Three independent discoveries of one class is the argument for a detector.

WHAT THIS COSTS, AND WHY IT IS OPT-IN
--------------------------------------

It re-runs producers, which is exactly why nobody does it. Use `--limit` and
`--timeout`; it is a sweep to run deliberately, not on every commit. It reports
the sample size it actually achieved rather than implying coverage it did not.

TRAPS THIS RESPECTS (all recorded in AGENTS.md, all learned the hard way)
------------------------------------------------------------------------

* **Producers write SIBLING witnesses.** The isotope producer rewrote 21 files
  a sampler never targeted. Restoring only the witness under test leaves a
  dirty tree that reads as real work — so this restores the whole
  `computations/` tree from git after EVERY run.
  (`witness_producer_executes_audit` restores one file; that is a live gap.)
* **A non-zero exit is not a defect.** Several producers refuse BY DESIGN and
  explain themselves on stdout. Classified `REFUSED`, not `CRASHED`.
* **A missing module is the RUNNER's fault**, never the producer's —
  `ENV_MISSING`, kept out of the defect count.
* **Compare assertions, not payloads.** Payload comparison drowns in
  timestamps and durations; the assertions carry the claim.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def _env() -> dict:
    env = dict(os.environ)
    extra = [ROOT / "tools" / "qou-substrate" / "python",
             ROOT / "tools" / "pyhecke" / "python",
             HERE, HERE / "substrate"]
    env["PYTHONPATH"] = os.pathsep.join(
        [str(p) for p in extra] + ([env["PYTHONPATH"]] if env.get("PYTHONPATH") else []))
    return env


def _restore_tree() -> None:
    """Restore the WHOLE computations/ tree — producers write siblings."""
    subprocess.run(["git", "checkout", "--", "computations/"], cwd=str(ROOT),
                   capture_output=True)


def _assertions(doc: dict) -> dict:
    out = {}
    for a in doc.get("assertions") or []:
        name = a.get("name")
        if name is not None:
            out[name] = (str(a.get("computed")), bool(a.get("passed", True)))
    return out


def _find_producer(doc: dict, wpath: Path) -> Path | None:
    ref = doc.get("scriptFile")
    if not ref:
        return None
    for cand in (wpath.parent / ref, HERE / ref, ROOT / ref):
        if cand.is_file():
            return cand
    hits = list(HERE.rglob(Path(ref).name))
    return hits[0] if len(hits) == 1 else None


def replay(wpath: Path, timeout: int) -> tuple[str, str]:
    doc = json.loads(wpath.read_text())
    if not doc.get("allPassed", False):
        return "SKIP_NOT_GREEN", "allPassed is not true"
    recorded = _assertions(doc)
    if not recorded:
        return "SKIP_NO_ASSERTIONS", "nothing to replay (hollowness audit's case)"
    prod = _find_producer(doc, wpath)
    if prod is None:
        return "NO_PRODUCER", str(doc.get("scriptFile"))[:80]

    try:
        proc = subprocess.run([sys.executable, str(prod)], cwd=str(ROOT), env=_env(),
                              capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        _restore_tree()
        return "TIMEOUT", f">{timeout}s"
    except OSError as exc:
        _restore_tree()
        return "CRASHED", str(exc)[:120]

    blob = (proc.stderr or "") + (proc.stdout or "")
    if proc.returncode != 0:
        tail = (proc.stderr.strip().splitlines() or [""])[-1]
        _restore_tree()
        if "ModuleNotFoundError" in blob or "ImportError" in blob:
            return "ENV_MISSING", tail[:140]
        if "Traceback" not in blob:
            # exits non-zero deliberately and says why on stdout
            return "REFUSED", tail[:140] or "non-zero exit, no traceback"
        return "CRASHED", tail[:140]

    try:
        fresh = _assertions(json.loads(wpath.read_text()))
    except json.JSONDecodeError:
        _restore_tree()
        return "CRASHED", "regenerated witness is not valid JSON"
    _restore_tree()

    if not fresh:
        return "NO_FRESH_ASSERTIONS", "producer ran but emitted no assertions"
    now_failing = [n for n, (_, ok) in fresh.items() if not ok]
    if now_failing:
        return "NOW_FAILS", f"{len(now_failing)} assertion(s) now fail: {', '.join(now_failing[:3])}"
    drifted = [n for n, (v, _) in recorded.items()
               if n in fresh and fresh[n][0] != v]
    if drifted:
        n = drifted[0]
        return "VALUE_DRIFT", f"{len(drifted)} changed, e.g. {n}: {recorded[n][0]} -> {fresh[n][0]}"
    missing = sorted(set(recorded) - set(fresh))
    if missing:
        # CALIBRATION (measured on active-set-lr-scaling-profile): assertion
        # names are sometimes INDEXED BY THE PRODUCER'S REACH — that one
        # renamed `max_block_dim_eq_2_pow_A_at_A6` to `..._at_A7` when it
        # started profiling one atom further. Both pass; nothing is stale.
        # A vanished name with a green non-empty replacement is a RENAME, and
        # reporting it as a finding would be a false positive, so it is
        # advisory. The finding is reserved for a name that vanished with
        # nothing passing in its place.
        if fresh and all(ok for _, ok in fresh.values()):
            return "ASSERTIONS_RENAMED", (
                f"{len(missing)} name(s) gone, e.g. {missing[0]}; "
                f"{len(fresh)} fresh assertion(s), all passing — advisory")
        return "ASSERTIONS_VANISHED", f"{len(missing)} gone, e.g. {missing[0]}"
    return "REPRODUCES", f"{len(recorded)} assertion(s) still hold"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--limit", type=int, default=25, help="witnesses to replay (default 25)")
    ap.add_argument("--timeout", type=int, default=120, help="seconds per producer")
    ap.add_argument("--only", default="", help="substring filter on the witness path")
    ap.add_argument("--strict", action="store_true", help="exit 1 on any NOW_FAILS / VALUE_DRIFT")
    args = ap.parse_args(argv)

    listed = subprocess.run(["git", "ls-files", "computations/*.witness.json"],
                            cwd=str(ROOT), capture_output=True, text=True).stdout.split()
    # `_deprecated/` is retired by definition — a stale verdict there is not a
    # finding, and including it wastes the whole budget (measured: the first 12
    # alphabetically are all deprecated, decidable sample 0).
    cands = [ROOT / p for p in listed
             if args.only in p and "/_deprecated/" not in p]

    # Pre-filter to what is actually REPLAYABLE before applying --limit, so the
    # limit bounds WORK DONE rather than files glanced at. Without this the
    # budget is spent on skips and the run decides nothing.
    replayable = []
    for w in sorted(cands):
        try:
            doc = json.loads(w.read_text())
        except Exception:                              # noqa: BLE001
            continue
        if doc.get("allPassed") and (doc.get("assertions") or []) and _find_producer(doc, w):
            replayable.append(w)

    print("=" * 74)
    print("WITNESS ASSERTION REPLAY — do the recorded assertions still hold?")
    print("=" * 74)
    print(f"  committed (live) witnesses : {len(cands)}")
    print(f"  green, with assertions,")
    print(f"    and a locatable producer : {len(replayable)}   <- the replayable population")
    print(f"  replaying this run         : {min(args.limit, len(replayable))}"
          f"   timeout: {args.timeout}s\n")

    tally, findings = {}, []
    for w in replayable[: args.limit]:
        try:
            verdict, detail = replay(w, args.timeout)
        except Exception as exc:                       # noqa: BLE001
            _restore_tree()
            verdict, detail = "AUDIT_ERROR", str(exc)[:120]
        tally[verdict] = tally.get(verdict, 0) + 1
        rel = str(w.relative_to(ROOT))
        if verdict in ("NOW_FAILS", "VALUE_DRIFT", "ASSERTIONS_VANISHED"):
            findings.append((verdict, rel, detail))
            print(f"  🛑 {verdict:<20} {rel}\n        {detail}")
        else:
            print(f"     {verdict:<20} {rel}")

    print("\n  " + "-" * 70)
    for k in sorted(tally):
        print(f"    {k:<22} {tally[k]}")
    # ASSERTIONS_RENAMED is decidable — the producer ran and we learned the
    # answer — it is simply not a finding.
    scored = sum(tally.get(k, 0) for k in
                 ("REPRODUCES", "NOW_FAILS", "VALUE_DRIFT",
                  "ASSERTIONS_VANISHED", "ASSERTIONS_RENAMED"))
    print(f"\n  DECIDABLE SAMPLE: {scored}  (the rest could not be run and say nothing)")
    if findings:
        print(f"  🛑 {len(findings)} witness(es) no longer reproduce their own recorded verdict.")
    elif scored:
        print("  ✓ every decidable witness in this sample still reproduces.")
    return 1 if (args.strict and findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
