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
import re
import subprocess
import sys
import time
from pathlib import Path, PurePosixPath

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from witness_provenance_audit import builder_names, written_filenames  # noqa: E402
from witness_regen_classify import classify  # noqa: E402

# `SUBFLOAT_MOVE` is kept because a diff bounded at 1e-12 relative cannot
# contain a physics change at 50 dps: it is twelve orders below any real
# quantity here and four above float64 noise. The classifier excludes
# non-numeric and discrete moves from it outright, so the population that
# reaches this verdict is exactly "the stored decimal gained or lost digits
# below the float64 floor" — which is the whole intended output of the NO
# FLOAT64 sweep (bean qou-tj98).
#
# Not a relaxation of the anchor rules: an anchor migration moves ~1e-7, five
# orders above this bound, and still needs its own evidence-gated verdict.
KEEP = {"DECLARED", "ANCHOR_MIGRATION", "SUBFLOAT_MOVE"}

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


def is_witness_name(name: str) -> bool:
    """True for both spellings of a witness filename.

    Most of the corpus is `<stem>.witness.json`, but 12 files use a HYPHEN —
    `y-lambda-mpfr-witness.json`, and with it the whole y-lambda family plus
    `protium-witness.json`, `delta-lambda-witness.json` and others. Those are
    witnesses by every other measure; only their name disagrees.

    Matching `.witness.json` alone made them invisible to this driver. Measured
    live: `regenerate_y_lambda_mpfr.py` re-anchored y_λ muon→proton, the driver
    saw `touched: []`, recorded NOCHANGE, reverted nothing, and left a
    re-anchored witness dirty and UNJUDGED in the worktree — the one outcome
    this driver exists to prevent, since the next `git add` sweeps it up.

    The base of the Wenzl bridge chain is in that blind spot, so an ordered
    re-anchoring wave could not have worked while it existed.
    """
    return name.endswith(".witness.json") or name.endswith("-witness.json")


def dirty_witnesses() -> list[str]:
    """Witness paths git reports as modified. Raises if git could not answer.

    The raise is defensive, not a fix for anything observed: returning `[]` on a
    failed git call is indistinguishable from a clean tree, so a git that could
    not run would read as "this producer touched nothing". An empty answer must
    be a fact about the tree, never about git's ability to report on it.
    """
    r = git("status", "--porcelain", "computations/")
    if r.returncode != 0:
        raise RuntimeError(
            f"git status failed (exit {r.returncode}); refusing to read that "
            f"as a clean tree: {r.stderr.strip()[:200]}")
    return [ln[3:] for ln in r.stdout.splitlines()
            if is_witness_name(ln.strip())]


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
        if ("_deprecated" in p.parts or "fsh-guts" in p.parts):
            continue
        try:
            src = p.read_text(encoding="utf-8")
        except Exception:
            continue
        if ".witness.json" in src and declares_upstream(src):
            out.append(p)
    return out


_WITNESS_RE = re.compile(r"[\w./-]+[-.]witness\.json")
_DOC_OWNERS = (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)


def _docstring_nodes(tree: ast.AST) -> set[int]:
    """id() of every docstring Constant, so prose can be excluded from reads.

    A witness named in a module docstring is documentation, not a dependency.
    `regenerate_y_lambda_mpfr.py` mentions `atomic-tr-m-mpfr-50dps.witness.json`
    in its header prose; counted as a read it made y_λ appear to depend on the
    bridge, and the ordering put the base of the chain last — the exact inverse
    of the right answer.
    """
    out = set()
    for n in ast.walk(tree):
        if isinstance(n, _DOC_OWNERS) and getattr(n, "body", None):
            first = n.body[0]
            if (isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant)
                    and isinstance(first.value.value, str)):
                out.add(id(first.value))
    return out


def _code_strings(tree: ast.AST) -> list[str]:
    """Every string literal that is not a docstring. Comments never appear."""
    skip = _docstring_nodes(tree)
    return [n.value for n in ast.walk(tree)
            if isinstance(n, ast.Constant) and isinstance(n.value, str)
            and id(n) not in skip]


def _sink_literals(tree: ast.AST) -> set[str]:
    """Witness basenames named literally inside a write-sink's own expression.

    `written_filenames` resolves a path only when the whole expression bottoms
    out in literals, so `OUTPUT = HERE / "y-lambda-mpfr-witness.json"` followed
    by `OUTPUT.write_text(...)` resolves to nothing — `HERE` is
    `Path(__file__).resolve().parent`. The provenance audit is right to be
    strict; it is answering "does this script provably write THAT path". For
    ordering the question is only "which basename does it write", so a literal
    reachable from the sink is enough.

    Without this, the writer of y-lambda-mpfr-witness.json was unknown, nothing
    depended on it, and it sorted last.
    """
    out: set[str] = set()
    assigns = {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and \
                isinstance(n.targets[0], ast.Name):
            assigns[n.targets[0].id] = n.value

    def literals(node, depth=0):
        if node is None or depth > 5:
            return
        for sub in ast.walk(node):
            if isinstance(sub, ast.Constant) and isinstance(sub.value, str) \
                    and is_witness_name(PurePosixPath(sub.value).name):
                out.add(PurePosixPath(sub.value).name)
            elif isinstance(sub, ast.Name) and sub.id in assigns:
                literals(assigns[sub.id], depth + 1)

    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                and n.func.attr in {"write_text", "write_bytes"}:
            literals(n.func.value)
        elif isinstance(n, ast.Call) and getattr(n.func, "id", "") == "open" \
                and n.args and len(n.args) > 1:
            literals(n.args[0])
    return out


def witness_io(path: Path) -> tuple[set[str], set[str]]:
    """(writes, reads) as witness basenames for one producer.

    Writes come from BOTH spellings, and needing both is not a detail:
    `written_filenames` sees only direct sinks (`write_text`, `open(…,"w")`),
    but almost every producer here writes through `WitnessBuilder`. Using the
    direct sink alone found writes for 2 of 163 producers, so the graph had no
    edges and the ordering silently did nothing — and the synthetic self-tests
    passed anyway, because fixtures written by hand use the direct form. A
    fixture that does not write the way the corpus writes tests nothing.

    `builder_names` returns witness STEMS, so `.witness.json` is appended.
    Computed names (`_OPAQUE`) and f-string patterns (`_DYNAMIC`) are skipped:
    an unresolvable name cannot be matched against a read, and guessing one
    would invent edges rather than find them.

    `reads` is every witness basename in the source MINUS what it writes. That
    is deliberately over-broad: a name in a comment counts as a read. For
    ORDERING that is the safe direction — a spurious edge costs a needless
    constraint, a missing edge costs a producer running before its input.
    """
    try:
        src = path.read_text(encoding="utf-8")
        tree = ast.parse(src)
    except Exception:
        return set(), set()
    writes = {PurePosixPath(w).name for w in written_filenames(tree)
              if is_witness_name(PurePosixPath(w).name)}
    for stem in builder_names(tree):
        if not stem.startswith("\x01"):          # skip _OPAQUE / _DYNAMIC
            writes.add(f"{stem}.witness.json")
    writes |= _sink_literals(tree)
    reads = {PurePosixPath(m).name
             for s in _code_strings(tree) for m in _WITNESS_RE.findall(s)}
    return writes, reads - writes


def dependency_order(prods: list[Path]) -> list[Path]:
    """Sort so every producer runs after the ones writing what it reads.

    Wave 3 recorded 6 FAILED as "Run its producer first". None of them was a
    defect: the sweep is alphabetical, so a consumer could run before the
    upstream it reads. In the report those are indistinguishable from real
    failures, which is the expensive part — a harness artefact that reads as
    corpus damage.

    Kahn's algorithm, alphabetical tie-break so a wave is reproducible.
    Cycles cannot be ordered, so their members are appended in alphabetical
    order rather than dropped: a cycle is a reason to run everything and let
    the classifier judge, not a reason to skip.
    """
    io = {p: witness_io(p) for p in prods}
    writer: dict[str, Path] = {}
    for p in sorted(prods):
        for w in io[p][0]:
            writer.setdefault(w, p)
    # deps[p] = producers p must follow.
    deps = {p: {writer[r] for r in io[p][1] if r in writer and writer[r] is not p}
            for p in prods}
    out: list[Path] = []
    done: set[Path] = set()
    remaining = set(prods)
    while remaining:
        ready = sorted(p for p in remaining if deps[p] <= done)
        if not ready:
            out.extend(sorted(remaining))       # cycle: keep them, ordered
            break
        out.extend(ready)
        done.update(ready)
        remaining -= set(ready)
    return out


def select(only: list[str]) -> list[Path]:
    """Resolve `--only` paths, preserving the ORDER the caller gave them.

    The default sweep is alphabetical, which is fine when producers are
    independent and wrong when they are not: a consumer that runs before the
    upstream it reads fails with "Run its producer first", and wave 3 recorded
    6 of those as FAILED — harness ordering, indistinguishable in the report
    from a real defect.

    So this does NOT sort. An ordered re-anchoring wave (regenerate the base
    witness, then everything that reads it) is expressible only if the caller's
    order survives, and sorting here would silently discard the one piece of
    information the caller had that the driver does not.

    Unknown paths raise rather than being skipped: a typo that quietly drops a
    producer from a dependency-ordered wave leaves a half-migrated corpus.
    """
    out = []
    for name in only:
        p = Path(name)
        if not p.is_absolute():
            p = ROOT / name
        p = p.resolve()
        if not p.exists():
            raise SystemExit(f"--only: no such producer: {name}")
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
            "stderr_tail": tail(stderr), "duration_sec": f"{seconds:.2f}",
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
            "duration_sec": f"{time.monotonic() - t0:.2f}",
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
                # Key on the CAUSE, not the field, so a shared cause aggregates
                # instead of scattering under one field name per rejection.
                #
                # The default used to be the literal string "no q0-valued field
                # flipped muon -> proton". That is the OUTER condition — true of
                # every rejection that reaches the inference path — so wave 3
                # filed 50 of its 51 VALUES under it and the histogram
                # distinguished none of them. The classifier now names the gate
                # that actually declined, and a missing reason is a bug in it,
                # not a case to paper over with a plausible-sounding label.
                key = w.get("reason") or "BUG: classifier returned no reason"
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

    # 6b. A git that cannot answer must not read as a clean tree. Returning []
    #     there let a regenerated witness escape judgement entirely.
    real_git = git
    try:
        def _broken(*args):
            return subprocess.CompletedProcess(args, 128, "", "fatal: index.lock")
        globals()["git"] = _broken
        try:
            dirty_witnesses()
            check(False, "dirty_witnesses raises when git fails")
        except RuntimeError:
            check(True, "dirty_witnesses raises when git fails")

        def _clean(*args):
            return subprocess.CompletedProcess(args, 0, "", "")
        globals()["git"] = _clean
        check(dirty_witnesses() == [],
              "an empty answer from a WORKING git is still a clean tree")

        # 6c. The hyphen spelling. 12 witnesses use it, including the whole
        #     y-lambda family at the base of the Wenzl bridge chain, and
        #     matching only ".witness.json" made them invisible: the driver
        #     reported NOCHANGE and left a re-anchored y_λ dirty and unjudged.
        def _both(*args):
            return subprocess.CompletedProcess(
                args, 0,
                " M computations/y-lambda-mpfr-witness.json\n"
                " M computations/chi-proton-h3.witness.json\n"
                " M computations/witness_regen_wave.py\n", "")
        globals()["git"] = _both
        check(dirty_witnesses() == ["computations/y-lambda-mpfr-witness.json",
                                    "computations/chi-proton-h3.witness.json"],
              "dirty_witnesses sees BOTH -witness.json and .witness.json")
    finally:
        globals()["git"] = real_git

    check(is_witness_name("y-lambda-mpfr-witness.json")
          and is_witness_name("chi-proton-h3.witness.json"),
          "is_witness_name accepts both spellings")
    check(not is_witness_name("witness_regen_wave.py")
          and not is_witness_name("results.json"),
          "is_witness_name rejects a non-witness")

    # 7. --only must preserve caller order. Sorting it would make an ordered
    #    re-anchoring wave impossible to express, which is the only reason the
    #    flag exists.
    here = Path(__file__).resolve()
    other = (ROOT / "computations" / "witness_regen_classify.py").resolve()
    rel_here = here.relative_to(ROOT).as_posix()
    rel_other = other.relative_to(ROOT).as_posix()
    # Deliberately reverse-alphabetical, so a stray sort() would show up.
    picked = select([rel_here, rel_other])
    check(picked == [here, other],
          "--only keeps the caller's order, it does not sort")
    check(select([rel_other, rel_here]) == [other, here],
          "--only order is the caller's both ways round")
    try:
        select(["computations/definitely_not_a_producer_xyz.py"])
        check(False, "--only rejects an unknown producer")
    except SystemExit:
        check(True, "--only rejects an unknown producer")

    # 8. dependency_order: a consumer must follow the producer of what it reads,
    #    against alphabetical order, which is the case wave 3 got wrong.
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        # 'a' reads what 'z' writes: alphabetically a<z, topologically z<a.
        (d / "a.py").write_text(
            'import json\njson.load(open("base.witness.json"))\n'
            'Path("a.witness.json").write_text("{}")\n')
        (d / "z.py").write_text('Path("base.witness.json").write_text("{}")\n')
        order = dependency_order([d / "a.py", d / "z.py"])
        check([p.name for p in order] == ["z.py", "a.py"],
              "dependency_order runs the upstream before its consumer")

        # The corpus writes through WitnessBuilder, not through write_text.
        # Detecting only the direct sink found writes for 2 of 163 producers
        # and left the graph edgeless while every synthetic test still passed.
        # This fixture writes the way the corpus does, so that cannot recur.
        (d / "b.py").write_text(
            'w = WitnessBuilder("built-thing")\n'
            'json.load(open("base.witness.json"))\n')
        bw, br = witness_io(d / "b.py")
        check("built-thing.witness.json" in bw,
              "witness_io sees a WitnessBuilder write, not just write_text")
        check("base.witness.json" in br and
              "built-thing.witness.json" not in br,
              "a builder's own output is a write, never also a read")
        check([p.name for p in dependency_order([d / "b.py", d / "z.py"])]
              == ["z.py", "b.py"],
              "a builder-based consumer still orders after its upstream")
        # The real shape of regenerate_y_lambda_mpfr.py: a module-level Path
        # built from a non-literal base, written through a name. The provenance
        # audit resolves nothing here (HERE is Path(__file__)…), so without a
        # looser sink rule the writer of y-lambda-mpfr-witness.json was unknown
        # and it sorted LAST — the inverse of correct, since it is the base of
        # the chain. Hyphen-named on purpose: that is the file this happened to.
        (d / "y.py").write_text(
            'HERE = Path(__file__).resolve().parent\n'
            'OUTPUT = HERE / "y-lambda-mpfr-witness.json"\n'
            'OUTPUT.write_text("{}")\n')
        yw, _ = witness_io(d / "y.py")
        check(yw == {"y-lambda-mpfr-witness.json"},
              "witness_io resolves a write through a module-level Path name")
        (d / "cons.py").write_text(
            'json.load(open("y-lambda-mpfr-witness.json"))\n'
            'w = WitnessBuilder("downstream")\n')
        check([p.name for p in dependency_order([d / "cons.py", d / "y.py"])]
              == ["y.py", "cons.py"],
              "the hyphen-named base of a chain orders first, not last")

        # Prose is not a dependency. y_λ names the bridge witness in its module
        # docstring; counted as a read it inverted the chain order.
        (d / "doc.py").write_text(
            '"""Header mentioning base.witness.json in prose."""\n'
            'Path("doc.witness.json").write_text("{}")\n')
        check("base.witness.json" not in witness_io(d / "doc.py")[1],
              "a witness named in a docstring is not counted as a read")

        # A computed name cannot be matched to a read, so it must not become a
        # write either — guessing would invent edges rather than find them.
        (d / "o.py").write_text('w = WitnessBuilder(some_var)\n')
        check(witness_io(d / "o.py")[0] == set(),
              "an unresolvable builder name yields no phantom write")

        # Merely naming a witness inside a dict literal is not writing it, so
        # it must not make this producer an upstream of anything.
        (d / "m.py").write_text('CATALOG = {"k": "base.witness.json"}\n')
        w, r = witness_io(d / "m.py")
        check(w == set() and "base.witness.json" in r,
              "witness_io counts a mention as a read, never as a write")

        # Independent producers keep alphabetical order, so waves reproduce.
        (d / "p.py").write_text('Path("p.witness.json").write_text("{}")\n')
        (d / "q.py").write_text('Path("q.witness.json").write_text("{}")\n')
        check([x.name for x in dependency_order([d / "q.py", d / "p.py"])]
              == ["p.py", "q.py"],
              "independent producers fall back to a reproducible order")

        # A cycle cannot be ordered. Keep both and let the classifier judge —
        # dropping them would silently shrink the wave.
        (d / "c1.py").write_text(
            'json.load(open("c2.witness.json"))\n'
            'Path("c1.witness.json").write_text("{}")\n')
        (d / "c2.py").write_text(
            'json.load(open("c1.witness.json"))\n'
            'Path("c2.witness.json").write_text("{}")\n')
        cyc = dependency_order([d / "c1.py", d / "c2.py"])
        check(len(cyc) == 2 and {p.name for p in cyc} == {"c1.py", "c2.py"},
              "a cycle keeps every member rather than dropping it")

        # Ordering must never lose or duplicate a producer.
        allp = [d / n for n in ("a.py", "z.py", "m.py", "p.py", "q.py")]
        out8 = dependency_order(allp)
        check(sorted(out8) == sorted(allp) and len(out8) == len(set(out8)),
              "dependency_order is a permutation: nothing lost, nothing doubled")

    out = "\n".join(summarise(records))
    check("1x  killed" in out, "summary histograms the failure causes")
    check("BUG: classifier returned no reason" in out,
          "summary flags a reasonless VALUES as a bug, not a gate finding")
    reasoned = [{**records[0], "witnesses": [
        {**records[0]["witnesses"][0], "reason": "x moved 2e-05, above the "
         "1e-05 anchor bound"}]}]
    out = "\n".join(summarise(reasoned))
    check("above the 1e-05 anchor bound" in out and "BUG:" not in out,
          "summary keys VALUES on the gate the classifier named")

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
    ap.add_argument("--only", action="append", default=[],
                    help="run exactly these producers, IN THE ORDER GIVEN "
                         "(repeatable). For dependency-ordered waves: "
                         "regenerate an upstream, then its consumers.")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()

    if a.only:
        prods = select(a.only)
        print(f"{len(prods)} producer(s) selected, running in the given order",
              flush=True)
    else:
        prods = dependency_order(producers())
        if a.limit:
            prods = prods[:a.limit]
        print(f"{len(prods)} producer(s) declare an upstream, in dependency "
              f"order", flush=True)
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
