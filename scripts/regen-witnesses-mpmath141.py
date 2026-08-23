#!/usr/bin/env python3
"""Regenerate committed witnesses under mpmath 1.4.1 (owner directive 2026-08-23).

Unifies the corpus on the most recent stable mpmath, resolving the version split
measured in `computations/audits/witness_environment_split_audit.py` (1159 @
1.3.0 vs 818 @ 1.4.1 vs 738 unrecorded), which defeats before/after witness
diffing in any single container.

RESUMABLE by design: every producer's outcome is appended to a ledger, and a
re-run skips what the ledger already records.  Long-compute discipline (AGENTS
§work-plan 5) — run with `-u` and tee the log.

    python3 -u scripts/regen-witnesses-mpmath141.py --limit 20 2>&1 | tee /tmp/regen.log
    python3 -u scripts/regen-witnesses-mpmath141.py 2>&1 | tee -a /tmp/regen.log

Per producer it records: exit status, wall seconds, which committed witnesses it
rewrote, and how many MATHEMATICAL fields moved (ephemeral/provenance fields are
excluded, so a "0 moved" is a genuine byte-stable re-run).

It does NOT judge whether a movement is acceptable — that is an agent call, and
the ledger is what makes it reviewable.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import subprocess
import sys
import time

REPO = pathlib.Path(__file__).resolve().parents[1]
LEDGER = REPO / "computations/audits/regen-mpmath141-ledger.json"
TARGET = "1.4.1"

EPHEMERAL = ("computedAt", "durationMs", "commitSha", "scriptCommitSha",
             "invocation", "generated", "environment", "engineVersion",
             "scriptHash", "timestamp")


def flat(o, p=""):
    r = {}
    if isinstance(o, dict):
        for k, v in o.items():
            r.update(flat(v, p + "/" + k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            r.update(flat(v, f"{p}[{i}]"))
    else:
        r[p] = o
    return r


def moved_fields(before: dict, after: dict) -> list[str]:
    fa, fb = flat(before), flat(after)
    return [k for k in sorted(set(fa) | set(fb))
            if fa.get(k) != fb.get(k)
            and not any(e in k for e in EPHEMERAL)]


def witness_mpmath(d: dict):
    env = d.get("environment") or {}
    v = env.get("mpmath")
    if not v:
        ev = str(d.get("engineVersion") or "")
        v = ev.split()[-1] if "mpmath" in ev else None
    return v


_PY_INDEX: dict[str, list[pathlib.Path]] | None = None


def _py_index() -> dict[str, list[pathlib.Path]]:
    """Build the basename -> paths map ONCE.

    The first version of this function called `REPO.rglob(base)` per witness.
    With 1887 stale witnesses that is 1887 full tree walks, and it burned a
    10-minute window without reaching a single producer. Indexing once takes
    seconds.
    """
    global _PY_INDEX
    if _PY_INDEX is None:
        idx: dict[str, list[pathlib.Path]] = {}
        for p in REPO.rglob("*.py"):
            sp = str(p)
            if "_deprecated" in sp or ".lake" in sp or "/_internal/" in sp \
                    or "/.git/" in sp:
                continue
            idx.setdefault(p.name, []).append(p)
        _PY_INDEX = idx
    return _PY_INDEX


def resolve_producer(script_file: str | None):
    if not script_file:
        return None
    base = os.path.basename(script_file)
    if not base.endswith(".py"):
        base += ".py"
    hits = list(_py_index().get(base, ()))
    if not hits:
        return None
    hits.sort(key=lambda p: (not str(p).startswith(str(REPO / "computations")),
                             len(str(p))))
    return hits[0]


def load_ledger() -> dict:
    if LEDGER.exists():
        try:
            return json.loads(LEDGER.read_text())
        except Exception:
            pass
    return {"schema": "regen-mpmath141-ledger/v1", "target": TARGET, "runs": {}}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="stop after N producers")
    ap.add_argument("--only", help="file of producer paths, one per line; run "
                                   "only these (order preserved)")
    ap.add_argument("--timeout", type=int, default=900)
    args = ap.parse_args()

    # map producer -> the stale witnesses it is recorded as writing
    todo: dict[str, list[str]] = {}
    unresolved = 0
    for p in sorted((REPO / "computations").rglob("*.witness.json")):
        if "_deprecated" in str(p):
            continue
        try:
            d = json.loads(p.read_text())
        except Exception:
            continue
        if witness_mpmath(d) == TARGET:
            continue
        prod = resolve_producer(d.get("scriptFile"))
        if prod is None:
            unresolved += 1
            continue
        todo.setdefault(str(prod.relative_to(REPO)), []).append(
            str(p.relative_to(REPO)))

    ledger = load_ledger()
    want = []
    if args.only:
        want = [ln.strip() for ln in open(args.only) if ln.strip()]
        missing = [w for w in want if w not in todo]
        if missing:
            print(f"note: {len(missing)} requested producer(s) have no stale "
                  f"witness recorded and are skipped: {missing[:3]}")
        pending = [w for w in want if w in todo and w not in ledger["runs"]]
    else:
        pending = [k for k in sorted(todo) if k not in ledger["runs"]]
    print(f"stale witnesses with a resolvable producer : "
          f"{sum(len(v) for v in todo.values())}")
    print(f"unique producers                           : {len(todo)}")
    # NB: count against the CONSIDERED set, not `todo` -- under --only the
    # considered set is the requested list, and subtracting `pending` from
    # `len(todo)` reported "already in ledger: 1546" when the ledger held 3.
    considered = len(todo) if not args.only else len(
        [w for w in want if w in todo])
    print(f"  considered this run                      : {considered}")
    print(f"  already in ledger                        : "
          f"{considered - len(pending)}")
    print(f"  pending this run                         : {len(pending)}")
    print(f"witnesses with NO resolvable producer      : {unresolved}")
    print()

    if args.limit:
        pending = pending[:args.limit]
    t_start = time.time()
    for i, prod in enumerate(pending, 1):
        wits = todo[prod]
        before = {}
        for w in wits:
            try:
                before[w] = json.loads((REPO / w).read_text())
            except Exception:
                before[w] = {}
        t0 = time.time()
        try:
            r = subprocess.run([sys.executable, "-u", prod], cwd=REPO,
                               capture_output=True, timeout=args.timeout)
            status, code = "ok" if r.returncode == 0 else "nonzero", r.returncode
            tail = (r.stderr or r.stdout).decode(errors="replace")[-300:]
        except subprocess.TimeoutExpired:
            status, code, tail = "timeout", None, ""
        dt = time.time() - t0

        # A producer killed at the timeout, or exiting nonzero, may have
        # rewritten SOME of its witnesses and not others. Committing that
        # half-state is exactly the unattributed value change this ledger
        # exists to prevent, so restore before measuring. Only a clean exit
        # is allowed to leave its output on disk.
        if status != "ok":
            subprocess.run(["git", "checkout", "--", *wits], cwd=REPO,
                           capture_output=True)

        moved_total, per = 0, {}
        for w in wits:
            try:
                after = json.loads((REPO / w).read_text())
            except Exception:
                continue
            m = moved_fields(before.get(w, {}), after)
            if m:
                per[w] = m[:8]
                moved_total += len(m)

        ledger["runs"][prod] = {
            "status": status, "exit": code, "wall_s": round(dt, 1),
            "witnesses": wits, "fields_moved": moved_total,
            "moved_sample": per,
            "tail": tail if status != "ok" else "",
        }
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        LEDGER.write_text(json.dumps(ledger, indent=1))

        el = time.time() - t_start
        eta = (el / i) * (len(pending) - i)
        print(f"[{i}/{len(pending)}] {status:<8} {dt:6.1f}s  moved={moved_total:<4} "
              f"{prod}   (elapsed {el/60:.1f}m, ETA {eta/60:.1f}m)", flush=True)

    runs = ledger["runs"]
    print()
    print(f"ledger now holds {len(runs)} producers")
    for s in ("ok", "nonzero", "timeout"):
        n = sum(1 for v in runs.values() if v["status"] == s)
        print(f"  {s:<8} {n}")
    stable = sum(1 for v in runs.values()
                 if v["status"] == "ok" and v["fields_moved"] == 0)
    print(f"  byte-stable re-runs (ok, 0 fields moved): {stable}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
