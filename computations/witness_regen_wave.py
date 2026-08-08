#!/usr/bin/env python3
# polynomial_q_not_applicable: orchestration over producers; emits no numeric physics.
"""Re-run every producer that declares an upstream, keeping only clean results.

Owner directive: NO FLOAT64 — this drives the regeneration that lands
`upstream_witness_hashes` in the witnesses whose producers now declare them.

## Why this is a committed tool

The first version of this driver lived in a scratch script, and both of its
failures came from that:

1. **It was bypassed.** Running producers by hand and then `git add -A` staged
   four unreviewed witnesses, one of them a 13/77 partial cache captured
   mid-rebuild. A guard outside the path being used is not a guard.
2. **It discarded its own successes.** Its revert reverted *every* dirty
   witness at the moment it fired, not the one under judgement — so each
   `VALUES` verdict also wiped the `DECLARED` and `ANCHOR_MIGRATION` results
   accumulated before it. The counters read `DECLARED 26 / ANCHOR_MIGRATION 4`
   at 90/163 while leaving a clean tree: the arithmetic was right and the
   retention was not.

Both are fixed here by construction: revert is **per witness**, and keeps are
tracked so a later revert can never touch them.

## Verdicts

Delegated to `witness_regen_classify`, so the policy lives in one place with
its own self-tests. `DECLARED` and `ANCHOR_MIGRATION` are kept; everything else
is reverted, per file.

## Why it reports per producer, and not just counts

The first full wave reported `DECLARED 37 / ANCHOR_MIGRATION 5 / VALUES 59 /
FAILED 36 / NOCHANGE 26` and nothing else. **Those 95 rejections were
uninvestigable**: the rejected witnesses had been reverted, so there was no
artefact left to inspect, and the counters recorded neither which producer nor
which field triggered the verdict. Answering "why is the VALUES rate 45%" took
a separate measurement pass that the driver already had the evidence for and
threw away.

So every producer now yields a record — verdict, the witnesses it touched, the
classifier's own `reason` / `sample` for each rejection, and for a failure the
exit code (or `timeout`) with the last line of stderr. That last field is not
incidental: the dominant failure cause in the first wave was
`ModuleNotFoundError: No module named 'pyhecke'`, pure harness error, and the
counts alone could not distinguish it from 36 real defects.

The report is rewritten after **every** producer, not at the end. A wave over
163 producers runs for hours, and a report that only exists on clean exit is
missing precisely when something went wrong enough to interrupt it.

## Serial by design

Producers write into the shared tree, so two of them in flight can revert each
other's output — exactly how a ⁴He rebuild was clobbered by a concurrent wave.
Never run this alongside anything else that writes a witness.

Usage:
    python3 computations/witness_regen_wave.py --dry-run
    python3 computations/witness_regen_wave.py --timeout 150 [--limit N]
    python3 computations/witness_regen_wave.py --report /path/to/report.json
    python3 computations/witness_regen_wave.py --self-test
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from witness_regen_classify import classify  # noqa: E402

KEEP = {"DECLARED", "ANCHOR_MIGRATION"}

# This repo's env-configurable scratch root (same spelling
# `a4_brunnian_deficit_closed_form` already uses), so the report lands
# somewhere gitignored by construction. A driver whose whole discipline is
# "commit by explicit path" must not drop an artefact into the worktree.
SCRATCH = Path(os.environ.get("QOU_SCRATCHPAD", "/tmp/qou-scratchpad"))


def declares_upstream(source: str) -> bool:
    """True when the module declares an upstream by either spelling."""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return False
    for n in ast.walk(tree):
        if isinstance(n, ast.Call):
            f = n.func
            name = f.attr if isinstance(f, ast.Attribute) else getattr(f, "id", "")
            if name in {"add_upstream", "record_upstream"}:
                return True
    return False


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def dirty_witnesses() -> list[str]:
    out = git("status", "--porcelain", "computations/").stdout.splitlines()
    return [ln[3:] for ln in out if ln.strip().endswith(".witness.json")]


def revert(paths) -> None:
    """Revert exactly these paths. Never a directory, never everything dirty.

    The blanket form (`git checkout -- computations/`) is what made the previous
    driver throw away results it had already accepted, and would also undo
    ported producer sources.
    """
    paths = [p for p in paths if p]
    if paths:
        git("checkout", "--", *paths)


def producers() -> list[Path]:
    out = []
    for p in sorted((ROOT / "computations").rglob("*.py")):
        if "_deprecated" in p.parts:
            continue
        try:
            src = p.read_text(encoding="utf-8")
        except Exception:
            continue
        if ".witness.json" in src and declares_upstream(src):
            out.append(p)
    return out


def tail(stream) -> str:
    """Last non-empty line of a captured stream, whatever type it arrived as.

    Must not assume `str` even though the producer runs under `text=True`:
    `TimeoutExpired` is raised from inside `_communicate` *before* the decode
    step, so its `.stderr` is raw bytes. Assuming otherwise loses the stderr of
    exactly the runs that hung — the ones hardest to diagnose after the fact.

    The last line is the interesting one because a Python failure ends with its
    exception: `ModuleNotFoundError: No module named 'pyhecke'` is the whole
    diagnosis, and it sits under a traceback nobody needs.
    """
    if not stream:
        return ""
    if isinstance(stream, (bytes, bytearray)):
        stream = bytes(stream).decode("utf-8", "replace")
    lines = [ln.strip() for ln in stream.splitlines() if ln.strip()]
    return lines[-1] if lines else ""


def judge(rel: str) -> dict:
    """Classify one dirty witness against HEAD, keeping the classifier's detail.

    Returns the classifier's whole record rather than just its verdict, so a
    rejection carries its `reason` and `sample` into the report. Reducing this
    to a bare string is what made 59 `VALUES` verdicts uninvestigable: the
    witness is reverted moments later, and with it the only other evidence of
    what moved.
    """
    old_raw = git("show", f"HEAD:{rel}").stdout
    if not old_raw:
        return {"path": rel, "verdict": "NEW"}
    try:
        r = classify(json.loads(old_raw),
                     json.loads((ROOT / rel).read_text(encoding="utf-8")))
    except Exception as exc:            # unparseable => never keep, but say why
        return {"path": rel, "verdict": "VALUES",
                "reason": f"unreadable witness: {type(exc).__name__}: {exc}"}
    return {"path": rel, **r}


def roll_up(records: list[dict]) -> tuple[str, list[str], list[str]]:
    """Producer verdict and keep/drop partition from its per-witness verdicts.

    Pure, so the policy can be tested without running a producer or touching
    the tree — the two things the self-test must never do.
    """
    keep = [r["path"] for r in records if r["verdict"] in KEEP]
    drop = [r["path"] for r in records if r["verdict"] not in KEEP]
    verdicts = [r["verdict"] for r in records]
    if not verdicts:
        return "NOCHANGE", [], []
    if not keep:
        return verdicts[0], [], drop
    return ("ANCHOR_MIGRATION" if "ANCHOR_MIGRATION" in verdicts
            else "DECLARED"), keep, drop


def failed_record(rel: str, code, stderr, before: set, seconds: float) -> dict:
    """A producer that never reached a verdict. Revert whatever it left behind.

    `code` is the exit status, or the string `"timeout"`. Both are failures,
    and the wave needs to tell them apart: a timeout says raise `--timeout`, a
    non-zero exit says read the stderr.
    """
    touched = sorted(set(dirty_witnesses()) - before)
    revert(touched)
    return {"producer": rel, "verdict": "FAILED", "exit_code": code,
            "stderr_tail": tail(stderr), "duration_sec": round(seconds, 2),
            "touched": touched, "kept": [], "reverted": touched,
            "witnesses": []}


def run_one(prod: Path, timeout: int, env: dict) -> dict:
    """Run one producer; return its full record. Reverts what it rejects."""
    rel = prod.relative_to(ROOT).as_posix()
    before = set(dirty_witnesses())
    t0 = time.monotonic()
    try:
        r = subprocess.run([sys.executable, prod.name], cwd=prod.parent,
                           capture_output=True, text=True, timeout=timeout, env=env)
    except subprocess.TimeoutExpired as exc:
        return failed_record(rel, "timeout", exc.stderr, before,
                             time.monotonic() - t0)
    if r.returncode != 0:
        return failed_record(rel, r.returncode, r.stderr, before,
                             time.monotonic() - t0)

    # Only what THIS producer touched — never the accumulated set.
    touched = sorted(set(dirty_witnesses()) - before)
    witnesses = [judge(w) for w in touched]
    verdict, keep, drop = roll_up(witnesses)
    revert(drop)
    return {"producer": rel, "verdict": verdict, "exit_code": 0,
            "stderr_tail": tail(r.stderr),
            "duration_sec": round(time.monotonic() - t0, 2),
            "touched": touched, "kept": keep, "reverted": drop,
            "witnesses": witnesses}


def write_report(path: Path, report: dict) -> None:
    """Persist the report atomically, so an interrupt cannot truncate it."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def default_report_path() -> Path:
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    return SCRATCH / f"witness-regen-wave-{stamp}.json"


def summarise(records: list[dict], limit: int = 8) -> list[str]:
    """The two histograms the counts could not give: why FAILED, why VALUES."""
    lines: list[str] = []
    causes: dict[str, int] = {}
    for rec in records:
        if rec["verdict"] == "FAILED":
            key = rec["stderr_tail"] or f"exit {rec['exit_code']}, no stderr"
            causes[key] = causes.get(key, 0) + 1
    reasons: dict[str, int] = {}
    for rec in records:
        for w in rec.get("witnesses", []):
            if w["verdict"] == "VALUES":
                # Key on the CAUSE, not the field. "no q0 flip" is the finding
                # (the evidence gate cannot fire); it stays invisible while
                # every rejection prints a different field name.
                key = w.get("reason") or "no q0-valued field flipped muon -> proton"
                reasons[key] = reasons.get(key, 0) + 1
    for title, hist in (("FAILED causes", causes), ("VALUES reasons", reasons)):
        if not hist:
            continue
        lines.append(f"\n{title} ({len(hist)} distinct):")
        for k, n in sorted(hist.items(), key=lambda kv: (-kv[1], kv[0]))[:limit]:
            lines.append(f"  {n:>3}x  {k[:140]}")
    return lines


SELF_TEST_NOTE = """\
Self-test covers the two structural properties the previous driver got wrong,
and the record-keeping that makes a verdict investigable afterwards. The
verdict policy itself is tested in witness_regen_classify.

Nothing here runs a producer, shells out to git, or writes into the tree: the
effects are stubbed, and roll_up / tail are pure so the policy can be tested
without any of that.
"""


def self_test() -> int:
    fails = ran = 0

    def check(ok, label: str) -> None:
        nonlocal fails, ran
        ran += 1
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {label}")

    # 1. revert() must never accept a directory or an empty entry.
    calls = []
    global git
    real_git = git
    try:
        git = lambda *a: calls.append(a) or subprocess.CompletedProcess(a, 0, "", "")  # noqa: E731
        revert(["a.witness.json", "", None])
        check(calls and calls[0] == ("checkout", "--", "a.witness.json"),
              "revert passes only real paths")
        calls.clear()
        revert([])
        check(not calls, "revert with nothing to do is a no-op")
    finally:
        git = real_git

    # 2. declares_upstream sees both spellings and nothing else.
    for src, want, label in [
        ("b.add_upstream(p)", True, "add_upstream"),
        ("record_upstream(p, L)", True, "record_upstream"),
        ("json.loads(p.read_text())", False, "plain read"),
        ("def (:", False, "syntax error"),
    ]:
        check(declares_upstream(src) == want, f"declares_upstream: {label}")

    # 3. tail(): the diagnosis is the last line, and a timed-out producer
    #    hands it over as bytes even though the run was text=True.
    check(tail("Traceback (most recent call last):\n  File x\n"
               "ModuleNotFoundError: No module named 'pyhecke'\n")
          == "ModuleNotFoundError: No module named 'pyhecke'",
          "tail takes the exception line, not the traceback")
    check(tail(b"partial output\nKilled at 150s\n") == "Killed at 150s",
          "tail decodes the bytes a TimeoutExpired carries")
    check(tail("done\n\n  \n") == "done", "tail skips trailing blank lines")
    check(tail("") == "" and tail(None) == "", "tail of nothing is empty")

    # 4. roll_up: the verdict policy, and the keep/drop partition with it.
    check(roll_up([]) == ("NOCHANGE", [], []), "roll_up: nothing touched")
    check(roll_up([{"path": "a", "verdict": "DECLARED"}])
          == ("DECLARED", ["a"], []), "roll_up: a declaration is kept")
    check(roll_up([{"path": "a", "verdict": "DECLARED"},
                   {"path": "b", "verdict": "ANCHOR_MIGRATION"}])
          == ("ANCHOR_MIGRATION", ["a", "b"], []),
          "roll_up: ANCHOR_MIGRATION wins the producer verdict, both kept")
    check(roll_up([{"path": "a", "verdict": "VALUES"},
                   {"path": "b", "verdict": "DECLARED"}])
          == ("DECLARED", ["b"], ["a"]),
          "roll_up: a rejected witness is dropped, its sibling still kept")
    check(roll_up([{"path": "a", "verdict": "VALUES"},
                   {"path": "b", "verdict": "NEW"}])
          == ("VALUES", [], ["a", "b"]),
          "roll_up: all-rejected reports the first verdict and reverts every path")

    # 5. A failure records WHICH failure. The counts could not tell a timeout
    #    from a missing module, and 36 FAILED read as 36 defects because of it.
    calls.clear()
    try:
        git = lambda *a: calls.append(a) or subprocess.CompletedProcess(a, 0, "", "")  # noqa: E731
        rec = failed_record("computations/p.py", "timeout", b"boom\nkilled\n",
                            set(), 150.0)
        check(rec["verdict"] == "FAILED" and rec["exit_code"] == "timeout"
              and rec["stderr_tail"] == "killed" and rec["kept"] == [],
              "failed_record: a timeout is labelled, with its stderr tail")
        rec = failed_record("computations/p.py", 1, "ImportError: no pyhecke\n",
                            set(), 0.4)
        check(rec["exit_code"] == 1
              and rec["stderr_tail"] == "ImportError: no pyhecke",
              "failed_record: a non-zero exit keeps its code and diagnosis")
    finally:
        git = real_git

    # 6. The report must survive the trip through JSON with its detail intact —
    #    a reason that does not round-trip is a reason nobody can grep for.
    records = [
        {"producer": "computations/a.py", "verdict": "VALUES", "exit_code": 0,
         "stderr_tail": "", "duration_sec": 1.0, "touched": ["a.witness.json"],
         "kept": [], "reverted": ["a.witness.json"],
         "witnesses": [{"path": "a.witness.json", "verdict": "VALUES",
                        "moved": 3, "flips": 0, "sample": ["x.y"]}]},
        {"producer": "computations/b.py", "verdict": "FAILED",
         "exit_code": "timeout", "stderr_tail": "killed", "duration_sec": 150.0,
         "touched": [], "kept": [], "reverted": [], "witnesses": []},
    ]
    round_tripped = json.loads(json.dumps({"records": records}))["records"]
    check(round_tripped == records, "report records round-trip through JSON")
    w = round_tripped[0]["witnesses"][0]
    check(w.get("sample") == ["x.y"] and w.get("moved") == 3,
          "report keeps the classifier's sample and moved count per witness")

    out = "\n".join(summarise(records))
    check("1x  killed" in out, "summary histograms the failure causes")
    check("no q0-valued field flipped" in out,
          "summary names the unreasoned VALUES rejections as the gate finding")

    print(f"\n{ran - fails}/{ran} passed")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=150)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true",
                    help="list the producers that would run, change nothing")
    ap.add_argument("--report", default="",
                    help="write the machine-readable per-producer report here "
                         f"(default: a timestamped file under {SCRATCH})")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    prods = producers()
    if a.limit:
        prods = prods[:a.limit]
    print(f"{len(prods)} producer(s) declare an upstream", flush=True)
    if a.dry_run:
        for p in prods:
            print(f"  {p.relative_to(ROOT).as_posix()}")
        return 0

    if dirty_witnesses():
        print("REFUSING: witnesses are already dirty. This driver must start "
              "from a clean tree, or it cannot tell its own output from "
              "someone else's.", file=sys.stderr)
        return 2

    # Both in-repo packages, not just the substrate. `pyhecke` (the Python
    # package under tools/pyhecke) is distinct from the `pyhecke_native`
    # extension, and leaving it off the path made producers fail with
    # `ModuleNotFoundError: No module named 'pyhecke'` — which the driver then
    # recorded as FAILED, indistinguishable from a real defect. It was the
    # dominant cause of an alarming failure rate that was pure harness error.
    env = dict(os.environ, PYTHONPATH=os.pathsep.join([
        str(ROOT / "tools/qou-substrate/python"),
        str(ROOT / "tools/pyhecke/python"),
    ]))
    counts: dict[str, int] = {}
    kept: list[str] = []
    records: list[dict] = []
    report_path = Path(a.report).expanduser() if a.report else default_report_path()
    # The mutable containers are shared with the report, so each rewrite below
    # publishes the current state without any copying back and forth.
    report = {
        "schema": "witness-regen-wave/1",
        "startedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "base": git("rev-parse", "HEAD").stdout.strip(),
        "timeout_sec": a.timeout,
        "producers_total": len(prods),
        "counts": counts,
        "kept": kept,
        "records": records,
    }
    write_report(report_path, report)      # the printed path always resolves
    print(f"report {report_path}", flush=True)

    for i, prod in enumerate(prods, 1):
        rec = run_one(prod, a.timeout, env)
        records.append(rec)
        counts[rec["verdict"]] = counts.get(rec["verdict"], 0) + 1
        kept.extend(rec["kept"])
        # After every producer, not at the end: a wave runs for hours, and the
        # report matters most when something interrupts it.
        report["finishedAt"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        report["producers_run"] = i
        write_report(report_path, report)
        if i % 10 == 0 or i == len(prods):
            print(f"  [{i}/{len(prods)}] {counts}  kept={len(kept)}", flush=True)

    print(f"\nFINAL {counts}")
    print(f"kept {len(kept)} witness(es) — verify with "
          f"`git status` before committing, and commit by explicit path")
    for k in kept[:40]:
        print(f"    {k}")
    for line in summarise(records):
        print(line)
    print(f"\nper-producer report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
