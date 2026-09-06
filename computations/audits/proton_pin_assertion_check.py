#!/usr/bin/env python3
"""proton_pin_assertion_check.py — does this producer's OWN assertions still
pass when it runs at the proton pin?

WHY THIS AND NOT THE ANCHOR-FLIP AUDIT

`anchor_flip_straddle_audit` answers "does a layer STRADDLE exist" and is sound
only for producers with a q of their own. Most `ideal_muon` entries do not have
one — they read `q_parameter`'s manifest-resolved shim, so flipping the anchor
changes their ONLY q and everything moves. That is a re-pin, trivially true, and
tells you nothing about whether the producer may be migrated.

The question a migration actually needs is narrower and cheaper:

    if I move this producer to the proton pin, does it still WORK?

A producer answers that itself, through its own assertions. `aoperator_a5_
crosscheck` is the worked case: its source never mentions muon, so a header scan
put it in the "safe to migrate" pile — and running it settled the question the
other way round from the way I first reported it. Silence in the source is not
evidence either way. Run it.

RESUMABILITY — AND WHY THE POINT OF IT IS NOT THE VERDICT
----------------------------------------------------------------------------
The obvious reason to checkpoint a long run is "don't lose the answers". That
is the SMALLER half here. The larger half:

    `check()` restores the witness tree in a `finally`. A `finally` does not
    run when the process is KILLED — OOM, a container reclaim, SIGKILL from a
    wrapping timeout, a lost ssh session.

For a producer that runs beyond twenty minutes that is the LIKELY exit, not the
exotic one. And the tree it leaves behind is dirty in the most expensive way
this repo knows: producers write SIBLING witnesses (AGENTS.md), so a killed run
of one probe can leave dozens of unrelated witnesses rewritten, looking exactly
like real work, ready to be swept into someone's commit.

So the snapshot is written TO DISK BEFORE the producer starts, and the next
process to start reads it and undoes the damage. An in-memory snapshot cannot
survive the failure mode it exists to protect against.

Consequences of that, each one deliberate:

  * The checkpoint records `in_flight` — the producer that was running when the
    process died. On the next start, that is the signal to RESTORE FIRST.
  * An interrupted producer is recorded as NOTHING. It is not UNKNOWN and not a
    failure: an interrupted run measured nothing at all, so it stays pending
    and is re-run. Only a run that finished writes a verdict.
  * Checkpoint writes are atomic (tmp + `os.replace`), so a kill DURING the
    write cannot leave a corrupt checkpoint that strands the recovery.
  * The snapshot stores BYTES only for witnesses that differ from `git HEAD`;
    everything else is recovered from git on demand. The tree is 71 MB across
    2952 witnesses and a clean tree stores zero of them, so the snapshot costs
    a manifest rather than a copy. Measured on a dirty tree it stores only what
    is genuinely dirty.

COST. One leg per producer. TIMEOUT is reported as UNKNOWN, never as a pass —
`block_swap_binding` and `gram_norm_binding_probe` each exceeded 1500 s under
the old default and produced no verdict, which is what this budget is for.

Usage:
    python3 proton_pin_assertion_check.py <producer.py> [...] [--timeout N]
    python3 proton_pin_assertion_check.py --status      # what is recorded
    python3 proton_pin_assertion_check.py --reset       # discard the run state
    ... --force                                         # re-run cached verdicts
"""
from __future__ import annotations

import argparse
import ast as _ast
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
SKIP = (".git", ".claude", "_deprecated", "node_modules", "__pycache__")

STATE_DEFAULT = Path(os.environ.get("TMPDIR", "/tmp")) / "qou-proton-pin-check"
PROGRESS_EVERY = 30.0   # seconds between "still running" lines


# ── witness tree snapshot, crash-safe ───────────────────────────────────────

def _witness_paths() -> list[Path]:
    return sorted(f for f in REPO.rglob("*.witness.json")
                  if not any(x in f.parts for x in SKIP))


def _sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _git_head_bytes(rel: str) -> bytes | None:
    """The committed bytes for a path, or None if it is untracked."""
    r = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=REPO,
                       capture_output=True)
    return r.stdout if r.returncode == 0 else None


def _dirty_vs_head() -> set[str]:
    """Witness paths git cannot give back — modified, staged, or untracked.

    ONE `git status` call, not one `git show` per witness. The first draft asked
    git for every file's committed bytes to decide whether to store it: 2952
    subprocesses per snapshot, and the snapshot is redone before every producer.
    `git status --porcelain` answers the same question in a single call, and the
    answer on a clean tree is the empty set, so nothing is stored at all.
    """
    r = subprocess.run(["git", "status", "--porcelain", "-z", "--",
                        "*.witness.json"], cwd=REPO, capture_output=True)
    if r.returncode != 0:
        # No git, or a broken repo: fall back to storing EVERYTHING, because
        # "cheap" is worth nothing next to "can put the tree back".
        return {str(f.relative_to(REPO)) for f in _witness_paths()}
    out: set[str] = set()
    fields = r.stdout.split(b"\0")
    i = 0
    while i < len(fields):
        rec = fields[i]
        i += 1
        if len(rec) < 4:
            continue
        xy, path = rec[:2], rec[3:].decode()
        out.add(path)
        if b"R" in xy or b"C" in xy:      # rename/copy: the ORIGIN follows
            if i < len(fields):
                out.add(fields[i].decode())
                i += 1
    return out


def snapshot(state: Path) -> None:
    """Record the tree so ANOTHER PROCESS can put it back.

    Stores bytes only where the working tree differs from git HEAD; the rest is
    recoverable with `git show`. That is what keeps this cheap enough to redo
    before every producer rather than once per run — and redoing it matters,
    because producer N-1's restore is the baseline producer N is measured
    against.
    """
    blobs = state / "blobs"
    blobs.mkdir(parents=True, exist_ok=True)
    for stale in blobs.iterdir():
        stale.unlink()
    dirty = _dirty_vs_head()
    manifest: dict[str, dict] = {}
    for f in _witness_paths():
        rel = str(f.relative_to(REPO))
        try:
            cur = f.read_bytes()
        except OSError:
            continue
        entry = {"sha": _sha(cur)}
        if rel in dirty:
            # git cannot give this one back, so keep the bytes.
            name = _sha(rel.encode())[:32] + ".blob"
            (blobs / name).write_bytes(cur)
            entry["blob"] = name
        manifest[rel] = entry
    _atomic_write(state / "manifest.json", json.dumps(manifest).encode())


def restore(state: Path) -> int:
    """Undo whatever a producer wrote. Returns the number of files touched."""
    mf = state / "manifest.json"
    if not mf.exists():
        return 0
    manifest = json.loads(mf.read_text())
    blobs = state / "blobs"
    touched = 0

    for f in _witness_paths():                       # written that did not exist
        rel = str(f.relative_to(REPO))
        if rel not in manifest:
            f.unlink(missing_ok=True)
            touched += 1

    for rel, entry in manifest.items():
        f = REPO / rel
        try:
            if f.exists() and _sha(f.read_bytes()) == entry["sha"]:
                continue
        except OSError:
            pass
        if "blob" in entry:
            data = (blobs / entry["blob"]).read_bytes()
        else:
            data = _git_head_bytes(rel)
            if data is None:                          # unrecoverable; say so
                print(f"    ! cannot restore {rel} — not in git and not stored",
                      file=sys.stderr)
                continue
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(data)
        touched += 1
    return touched


def written_since(state: Path) -> dict[Path, dict]:
    """Witness files whose bytes differ from the snapshot — i.e. this run's."""
    manifest = json.loads((state / "manifest.json").read_text())
    out = {}
    for f in _witness_paths():
        rel = str(f.relative_to(REPO))
        try:
            b = f.read_bytes()
        except OSError:
            continue
        if manifest.get(rel, {}).get("sha") != _sha(b):
            try:
                out[f] = json.loads(b)
            except json.JSONDecodeError:
                out[f] = {}
    return out


# ── checkpoint ──────────────────────────────────────────────────────────────

def _atomic_write(path: Path, data: bytes) -> None:
    """A kill during this must not strand the recovery it enables."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    # Already atomic before qou-sidu -- sibling temp, fsync, os.replace, which
    # is exactly what that bean asks for. The transform did not notice and
    # added a SECOND temp, so the write went X.tmp.tmp -> X.tmp -> X and the
    # fsync landed on the inner temp while the file actually promoted to
    # `path` was never synced, quietly weakening the durability this
    # function's own docstring promises. One hop, as it was.
    with open(tmp, "wb") as fh:
        fh.write(data)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def load_ckpt(state: Path) -> dict:
    p = state / "checkpoint.json"
    if not p.exists():
        return {"verdicts": {}, "in_flight": None}
    try:
        d = json.loads(p.read_text())
    except json.JSONDecodeError:
        return {"verdicts": {}, "in_flight": None}
    d.setdefault("verdicts", {})
    d.setdefault("in_flight", None)
    return d


def save_ckpt(state: Path, ck: dict) -> None:
    _atomic_write(state / "checkpoint.json", json.dumps(ck, indent=2).encode())


# ── the check itself ────────────────────────────────────────────────────────

def run_producer_at(prod: Path, timeout: int, log_dir: Path | None,
                    anchor: str = "physical"):
    """Run at the proton pin with LIVE logging. (rc|None, tail, seconds).

    The producer's stdout goes STRAIGHT TO A FILE, not through a pipe this
    process drains at the end. The first version read the pipe only after the
    process exited, so `--log-dir` held an empty file for the whole run —
    measured: 0 bytes at 4 minutes into a 7200 s budget.

    That is not merely unhelpful, it is the exact signature AGENTS.md tells
    agents to read as a crash ("ends silently with 0-byte output ... assume it
    crashed"). A logging option that manufactures the symptom of the failure it
    exists to diagnose is worse than no logging, so the file is written as the
    producer writes it and can be tailed mid-run.

    A pipe would also deadlock a producer verbose enough to fill the OS buffer
    while nobody is reading — which a two-hour run is a good candidate for.
    """
    env = dict(os.environ)
    env["QOU_Q0_ANCHOR"] = anchor
    if log_dir:
        log_dir.mkdir(parents=True, exist_ok=True)
        log_path = log_dir / f"{prod.stem}.{anchor}.log"
    else:
        log_path = Path(tempfile.gettempdir()) / f"ppc-{prod.stem}-{os.getpid()}.log"
    t0 = time.monotonic()
    with open(log_path, "wb") as sink:
        proc = subprocess.Popen([sys.executable, "-u", prod.name], cwd=prod.parent,
                                stdout=sink, stderr=subprocess.STDOUT, env=env)
        next_tick = t0 + PROGRESS_EVERY
        while True:
            rc = proc.poll()
            if rc is not None:
                break
            now = time.monotonic()
            if now >= next_tick:
                size = log_path.stat().st_size if log_path.exists() else 0
                print(f"      … {prod.stem}: {now - t0:6.0f}s elapsed "
                      f"(budget {timeout}s, {size} B logged)", flush=True)
                next_tick = now + PROGRESS_EVERY
            if now - t0 > timeout:
                proc.kill()
                proc.wait()
                return None, "", now - t0
            time.sleep(0.5)
    try:
        tail = log_path.read_bytes()[-400:].decode(errors="replace")
    except OSError:
        tail = ""
    if not log_dir:
        log_path.unlink(missing_ok=True)
    return rc, tail, time.monotonic() - t0


# Producers that read the anchor-defining witness FILE directly do not go
# through `q_parameter`, so QOU_Q0_ANCHOR does not reach them. Measured on
# main 2026-08-29: 17 of the 32 `ideal_muon` stems. Raised from #5792, and
# the count there (7 of 13) is a different subset, not a disagreement.
# THE FIRST VERSION OF THIS LIST WAS WRONG IN BOTH DIRECTIONS, and the count
# hid it. Matching the bare strings "q-pinning-50-digit"/"q_pinning_50_digit"
# anywhere in the source gave 15 of 21 stems on 2026-08-29. The corrected test
# also gives 15 — over a DIFFERENT SET:
#
#   FALSE POSITIVE  rho_f_categorical_probe names `q_pinning_50_digit.py` in a
#                   docstring markdown link and never reads the witness. It was
#                   refused as unmeasurable; run, it returns NO-ASSERTIONS.
#   FALSE NEGATIVE  qbeta_jacobi_anger_tower_general reaches muon through
#                   `q_muon_at()` and never names the file, so no filename test
#                   of any tightness sees it. It was being RUN, and its verdict
#                   would have been a FALSE PASS — the dangerous direction.
#
# So a matching count is not agreement, and tightening a pattern is not the same
# as fixing it: this had to widen (the anchor APIs) as well as narrow (the
# actual witness filename, not the producer's name).
# CORRECTED 2026-09-03 (bean `qou-aj91`): the first entry was the witness
# FILENAME, "q-pinning-50-digit.witness.json". A filename cannot tell READING a
# file from MENTIONING it, and after nine producers were correctly routed
# through `q_parameter` the tool still called every one of them bypassed --
# matching a comment documenting the routing, a `w.add_upstream(witness_path(
# ...))` provenance edge, and a witness string describing the file
# historically. None of those source a value.
#
# The filename is replaced by `derived_50_digit`, the field a value-read of
# that witness ALWAYS subscripts (`d["derived_50_digit"]["q"]`), and which a
# provenance reference never does. Verified 15/15 on the two known sets: the 9
# routed producers and the 6 that must stay bypassed (the anchor definer, the
# flip detector, the L1-muon cross-check, the dual-layer producer, the
# deliberate two-anchor comparison, and the probe that validates other fields
# of the same witness).
_PIN_FILE_MARKERS = (
    "derived_50_digit",                  # the field a direct value-read subscripts
    "q_muon_at",                         # the muon anchor API, by name
    "_q0_value_for_anchor",              # the underlying anchor resolver
    "load_q_50dps",                      # muon default (qou-dkm2)
)


def env_override_reaches(prod: Path) -> bool:
    """False when this producer takes its pin from the file, not the manifest.

    THIS IS THE DIFFERENCE BETWEEN A VERDICT AND A LIE. The check works by
    setting QOU_Q0_ANCHOR=physical, which only `q_parameter` reads. A producer
    that loads `q-pinning-50-digit.witness.json` itself gets MUON no matter
    what the environment says — so it would run at muon, pass its muon-tuned
    assertions, and be reported PASSES-AT-PROTON. A false pass on a migration
    question is the worst output this tool can produce, worse than no answer,
    because it is indistinguishable from a real one.

    MEASURED FALSE NEGATIVE, FIXED 2026-09-03 (bean `qou-aj91`). See the note on
    `_PIN_FILE_MARKERS` for what was wrong. The remaining half of the fix is
    here: match against the source with COMMENTS AND DOCSTRINGS REMOVED, so
    prose about the anchor cannot masquerade as a read of it. Comments never
    reach the AST; docstrings are blanked explicitly.

    An unparseable file falls back to the raw substring test, and an unreadable
    one is reported as reached. Both fall on the safe side of the asymmetry
    above: unmeasurable is a worse answer than nothing, but a FALSE PASS is
    worse than either.
    """
    try:
        src = prod.read_text(errors="replace")
    except OSError:
        return True                       # cannot tell; run it and find out

    try:
        tree = _ast.parse(src)
    except SyntaxError:
        return not any(m in src for m in _PIN_FILE_MARKERS)   # conservative

    for node in _ast.walk(tree):
        if isinstance(node, (_ast.Module, _ast.FunctionDef, _ast.AsyncFunctionDef,
                             _ast.ClassDef)) and node.body:
            first = node.body[0]
            if (isinstance(first, _ast.Expr)
                    and isinstance(first.value, _ast.Constant)
                    and isinstance(first.value.value, str)):
                first.value.value = ""
    try:
        code_only = _ast.unparse(tree)
    except Exception:
        return not any(m in src for m in _PIN_FILE_MARKERS)   # conservative
    return not any(m in code_only for m in _PIN_FILE_MARKERS)


def check(prod: Path, timeout: int, state: Path, log_dir: Path | None):
    """(verdict, detail, seconds) — does it pass its own assertions at proton?"""
    if not env_override_reaches(prod):
        return ("UNSOUND-ENV-BYPASS",
                "reads q-pinning-50-digit.witness.json directly, so "
                "QOU_Q0_ANCHOR never reaches it — running would measure the "
                "MUON leg and report it as proton. Route it through "
                "q_parameter first (qou-aj91 mechanism 5).", 0.0)
    snapshot(state)
    rc, tail, secs = run_producer_at(prod, timeout, log_dir, "physical")
    try:
        if rc is None:
            return "UNKNOWN", f"exceeded {timeout}s — not a pass, not a fail", secs
        if rc != 0:
            # A NON-ZERO EXIT IS NOT EVIDENCE ABOUT THE ANCHOR. Measured twice:
            # binding_via_interface_knot dies on `data_loaded`, and
            # qbeta_hoefsmit_tbeta_matrix_build_probe on `TypeError:
            # unsupported format string passed to mpf.__format__` — both
            # IDENTICALLY at either pin. Calling those FAILS-AT-PROTON reads as
            # "it depends on the muon pin" and would freeze a merely broken
            # producer in ideal_muon forever, for a reason unrelated to q0.
            #
            # So on failure ONLY, spend a second leg to disambiguate. The common
            # path stays one leg, which is what makes this check cheap and what
            # distinguishes it from the anchor-flip audit.
            rc2, tail2, _ = run_producer_at(prod, timeout, log_dir, "ideal")
            if rc2 == rc:
                return ("BROKEN-AT-BOTH",
                        f"exit {rc} at BOTH pins — pre-existing, not anchor-"
                        f"dependent: {tail[-110:].replace(chr(10), ' ')}", secs)
            return ("FAILS-AT-PROTON",
                    f"exit {rc} at proton but {rc2} at muon — genuinely "
                    f"anchor-dependent: {tail[-110:].replace(chr(10), ' ')}", secs)

        wrote = written_since(state)
        if not wrote:
            return "NO-WITNESS", "writes nothing — no assertions to check", secs

        # READ THE VALUE, NOT THE DELTA — and distinguish false from absent.
        # `True -> False`, `True -> null`, and the field going AWAY are three
        # findings wearing one shape (#5805). `is False` alone silently passes
        # the latter two.
        bad, unclear = [], []
        for f, doc in wrote.items():
            if "allPassed" in doc and doc["allPassed"] is not True:
                (bad if doc["allPassed"] is False else unclear).append(
                    f"{f.name}: allPassed={doc['allPassed']!r}")
            for a in doc.get("assertions", []):
                if a.get("passed") is not True:
                    (bad if a.get("passed") is False else unclear).append(
                        f"{f.name}: assertion {a.get('name')!r} "
                        f"passed={a.get('passed')!r}")
        if bad:
            return "FAILS-AT-PROTON", "; ".join(bad[:3]), secs
        if unclear:
            return ("UNCLEAR", "neither true nor false: " +
                    "; ".join(unclear[:3]), secs)
        n = sum(len(d.get("assertions", [])) for d in wrote.values())
        if n == 0 and not any("allPassed" in d for d in wrote.values()):
            # It wrote a witness but asserts nothing, so running it at proton
            # established nothing. Reporting that as a pass would be the same
            # false reassurance as the env-bypass case, one layer down.
            return ("NO-ASSERTIONS",
                    f"{len(wrote)} witness(es) written, 0 assertions — "
                    f"nothing to pass or fail", secs)
        return ("PASSES-AT-PROTON",
                f"{len(wrote)} witness(es), {n} assertion(s), all pass", secs)
    finally:
        restore(state)


# ── self-test ───────────────────────────────────────────────────────────────
#
# The crash-safety claim above is the whole reason this file is more than
# twenty lines, and a claim like that is worth exactly as much as its test. So
# case 3 does not simulate a crash — it SIGKILLs a real run of this script and
# checks that the next one cleans up after it.

_SELFTEST_PRODUCER = """import json, sys, time
from pathlib import Path
w = Path(__file__).resolve().parent / "_proton_pin_selftest.witness.json"
w.write_text(json.dumps({"allPassed": True, "assertions": []}))
sys.stdout.write("wrote\\n"); sys.stdout.flush()
time.sleep(600)
"""


def selftest() -> int:
    import shutil
    import signal
    import tempfile

    state = Path(tempfile.mkdtemp(prefix="ppc-selftest-"))
    victim = REPO / "computations" / "_proton_pin_selftest_victim.witness.json"
    stray = REPO / "computations" / "_proton_pin_selftest.witness.json"
    fake = REPO / "computations" / "_proton_pin_selftest_producer.py"
    fail = 0

    def chk(name, want, got):
        nonlocal fail
        if want == got:
            print(f"  [ok  ] {name}")
        else:
            print(f"  [FAIL] {name}\n         want: {want!r}\n         got : {got!r}")
            fail = 1

    try:
        # 1. A killed producer's LEFTOVER is deleted. This is the file that
        #    would otherwise be swept into someone's commit as real work.
        snapshot(state)
        stray.write_text('{"allPassed": true}')
        restore(state)
        chk("stray witness from a killed run is deleted", False, stray.exists())

        # 2. An OVERWRITTEN witness gets its bytes back — including one that was
        #    already dirty vs HEAD before the run, which git alone cannot undo.
        victim.write_text('{"original": true}')
        snapshot(state)
        victim.write_text('{"clobbered": true}')
        restore(state)
        chk("dirty-vs-HEAD witness restored byte-exact",
            '{"original": true}', victim.read_text())
        stored = json.loads((state / "manifest.json").read_text())
        rel = str(victim.relative_to(REPO))
        chk("...and its bytes were STORED, not left to git",
            True, "blob" in stored.get(rel, {}))
        victim.unlink(missing_ok=True)

        # 3. THE REAL THING. SIGKILL a live run; the next one must recover.
        fake.write_text(_SELFTEST_PRODUCER)
        proc = subprocess.Popen(
            [sys.executable, "-u", str(Path(__file__).resolve()),
             str(fake.relative_to(REPO)), "--state", str(state), "--timeout", "600"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for _ in range(1200):                      # wait for the producer's write
            if stray.exists():
                break
            time.sleep(0.1)
        else:
            chk("selftest producer wrote its witness", True, False)
        proc.send_signal(signal.SIGKILL)
        proc.wait()
        subprocess.run(["pkill", "-9", "-f", "_proton_pin_selftest_producer"],
                       capture_output=True)
        time.sleep(0.3)

        chk("after SIGKILL: tree is DIRTY (the hazard is real)",
            True, stray.exists())
        chk("after SIGKILL: checkpoint records in_flight",
            "_proton_pin_selftest_producer", load_ckpt(state).get("in_flight"))

        r = subprocess.run(
            [sys.executable, "-u", str(Path(__file__).resolve()),
             str(fake.relative_to(REPO)), "--state", str(state), "--timeout", "5"],
            capture_output=True, text=True)
        chk("restart announces the recovery",
            True, "RECOVERED from an interrupted run" in r.stdout)
        # The re-run itself times out at 5 s and restores again, so by now the
        # tree must be clean either way — which is the point.
        chk("restart leaves the tree clean", False, stray.exists())
        chk("interrupted producer was NOT recorded as a verdict on the kill",
            "UNKNOWN", load_ckpt(state)["verdicts"]
            .get("_proton_pin_selftest_producer", {}).get("verdict"))
    finally:
        for f in (stray, victim, fake):
            f.unlink(missing_ok=True)
        shutil.rmtree(state, ignore_errors=True)

    print()
    print("proton-pin-assertion-check self-test "
          + ("passed" if not fail else "FAILED"))
    return fail


# ── driver ──────────────────────────────────────────────────────────────────

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("producers", nargs="*")
    ap.add_argument("--timeout", type=int, default=1800,
                    help="per-producer budget in seconds (default 1800)")
    ap.add_argument("--state", default=str(STATE_DEFAULT),
                    help=f"run-state directory (default {STATE_DEFAULT})")
    ap.add_argument("--log-dir", default=None,
                    help="tee each producer's output here (long-compute discipline)")
    ap.add_argument("--force", action="store_true",
                    help="re-run producers that already have a recorded verdict")
    ap.add_argument("--status", action="store_true", help="print run state, exit")
    ap.add_argument("--reset", action="store_true", help="discard run state, exit")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the crash-recovery path, incl. a real SIGKILL")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    state = Path(args.state)
    log_dir = Path(args.log_dir) if args.log_dir else None
    ck = load_ckpt(state)

    if args.status:
        print(json.dumps(ck, indent=2))
        return 0
    if args.reset:
        if ck.get("in_flight"):
            n = restore(state)
            print(f"  restored {n} witness file(s) before discarding state")
        for p in ("checkpoint.json", "manifest.json"):
            (state / p).unlink(missing_ok=True)
        blobs = state / "blobs"
        if blobs.exists():
            for b in blobs.iterdir():
                b.unlink()
        print(f"  run state discarded: {state}")
        return 0
    if not args.producers:
        ap.error("give at least one producer, or --status / --reset")

    print("=" * 72)
    print("proton-pin assertion check — may this producer be migrated?")
    print(f"  state: {state}   budget: {args.timeout}s/producer")
    print("=" * 72)

    # RECOVERY. A recorded in_flight means the last process was killed before
    # its restore ran, so the tree may carry that producer's writes — and its
    # siblings'. Undo them before measuring anything, or producer N is measured
    # against producer N-1's wreckage.
    if ck.get("in_flight"):
        stem = ck["in_flight"]
        n = restore(state)
        print(f"  RECOVERED from an interrupted run of {stem!r}: "
              f"restored {n} witness file(s).")
        print(f"  {stem!r} is left PENDING — an interrupted run measured "
              f"nothing, so it is neither UNKNOWN nor a failure.")
        ck["in_flight"] = None
        save_ckpt(state, ck)

    rc = 0
    for p in args.producers:
        path = Path(p) if Path(p).is_absolute() else REPO / p
        stem = path.stem
        prev = ck["verdicts"].get(stem)
        if prev and not args.force:
            print(f"  {prev['verdict']:17s} {stem}: {prev['detail']}")
            print(f"      (cached from {prev['at']}, {prev['seconds']:.0f}s — "
                  f"--force to re-run)")
            if prev["verdict"] == "FAILS-AT-PROTON":
                rc = 1
            continue
        if not path.exists():
            print(f"  {'MISSING':17s} {stem}: no such file: {path}")
            rc = 1
            continue

        # Do not announce a run that is about to be refused — the tool said
        # "running X" and then reported it had not run X, which is the kind of
        # small untruth that makes a log unusable as evidence.
        if env_override_reaches(path):
            print(f"  running {stem} …", flush=True)
        ck["in_flight"] = stem
        save_ckpt(state, ck)
        v, d, secs = check(path, args.timeout, state, log_dir)
        ck["verdicts"][stem] = {
            "verdict": v, "detail": d, "seconds": secs,
            "timeout": args.timeout,
            "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        ck["in_flight"] = None
        save_ckpt(state, ck)
        print(f"  {v:17s} {stem}: {d}  [{secs:.0f}s]", flush=True)
        if v == "FAILS-AT-PROTON":
            rc = 1

    print("=" * 72)
    print("  PASSES-AT-PROTON -> safe to migrate (still diff its witness on the real move)")
    print("  FAILS-AT-PROTON  -> HOLD: it depends on the muon pin, whatever its source says")
    print("  UNKNOWN          -> untested; do NOT read as either")
    print("  UNSOUND-ENV-BYPASS-> the pin override cannot reach it; not run")
    print("  UNCLEAR          -> an assertion is neither true nor false")
    print("  NO-ASSERTIONS    -> wrote a witness but asserts nothing")
    print("  BROKEN-AT-BOTH   -> same failure at either pin; NOT a hold, fix the producer")
    print(f"  resume/inspect:  {sys.argv[0]} --status --state {state}")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
