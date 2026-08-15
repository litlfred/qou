#!/usr/bin/env python3
"""Regenerate every producer that was pinned to the muon q₀ (bean tnjb).

## Why

`q0_anchor_manifest.json` listed 257 producer stems under `ideal_muon`, and
`substrate/q_parameter.py` auto-selects the anchor from `Path(sys.argv[0]).stem`
— so each of those, when run under its own name, silently took the muon pin for
its ENTIRE `q_parameter` surface (`q_at`, `Q_50_DIGIT_STR`, the `_MP` family).
The owner directive of 2026-08-15 makes proton the default everywhere, and the
list is now empty. Every witness those producers emitted beforehand is a
muon-layer number sitting in a proton-layer corpus, 11.54 ppb off.

Owner directive, same day: **fix all, even if not visible.** So this sweep does
not triage by whether the shift shows at a witness's reported precision. It was
tempting to: a first pass tried bucketing by significant digits and found the
test discriminates nothing (255 of 255 carry ≥9 sig figs somewhere), and a
second tried triaging by reader count (44 have a reader, 211 are leaves). Both
would have left a stale number in the corpus on the theory that nobody was
looking at it, which is exactly how the μ–p tension audit came to under-report
its own subject by 155× without anyone noticing.

## Dependency order is the point

`qou-lt8x` established that a re-run is not automatically a migration. Several
of these producers read each other's witnesses, so running them alphabetically
re-emits stale upstream values into freshly-run downstreams — the defect
`topo_order()` exists to prevent. This driver builds producer → witness →
reader edges from the actual files and runs in topological order, so a
consumer never runs before the thing it consumes.

## Resumable

Long compute (several producers are ≥20 min alone). Progress is journalled to
`q0-repin-sweep-progress.json` after every producer, so an interrupted run
resumes rather than restarting. Re-running is safe.

Usage:
    python3 -u q0_repin_sweep.py                 # full sweep, resuming
    python3 -u q0_repin_sweep.py --dry-run       # print the order, run nothing
    python3 -u q0_repin_sweep.py --limit 20      # first 20 in topo order
    python3 -u q0_repin_sweep.py --timeout 1800  # per-producer cap (default 900s)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROGRESS = HERE / "q0-repin-sweep-progress.json"
NUM = re.compile(r"^-?\d*\.?\d+(?:[eE][-+]?\d+)?$")


def former_ideal_muon() -> list[str]:
    """The 257 stems, read from the pre-flip manifest on origin/main.

    Read from git rather than the working tree: the flip emptied the list, so
    the working copy no longer knows which producers were affected.
    """
    out = subprocess.run(
        ["git", "show", "origin/main:computations/q0_anchor_manifest.json"],
        capture_output=True, text=True, cwd=HERE.parent)
    if out.returncode != 0:
        raise SystemExit("cannot read the pre-flip manifest from origin/main; "
                         "fetch first")
    return json.loads(out.stdout).get("ideal_muon", [])


def build_graph(stems: set[str]):
    """producer stem -> (script path, its witness names, stems it reads)."""
    wit: dict[str, set[str]] = {}
    for w in HERE.rglob("*.witness.json"):
        if "_deprecated" in w.parts:
            continue
        try:
            d = json.loads(w.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001 — a malformed witness is not this sweep's problem
            continue
        if not isinstance(d, dict):
            continue
        sf = d.get("scriptFile") or ""
        st = sf[:-3] if isinstance(sf, str) and sf.endswith(".py") else sf
        if st in stems:
            wit.setdefault(st, set()).add(w.name)

    paths: dict[str, Path] = {}
    for s in stems:
        hits = [p for p in HERE.rglob(f"{s}.py") if "_deprecated" not in p.parts]
        if hits:
            paths[s] = hits[0]

    # reads-edges: stem A depends on stem B if A's source mentions any witness
    # filename B emits.
    blobs = {s: p.read_text(encoding="utf-8", errors="ignore")
             for s, p in paths.items()}
    deps: dict[str, set[str]] = {s: set() for s in paths}
    for a, txt in blobs.items():
        for b, names in wit.items():
            if a != b and b in paths and any(n in txt for n in names):
                deps[a].add(b)
    return paths, wit, deps


def topo_order(paths: dict[str, Path], deps: dict[str, set[str]]) -> list[str]:
    """Dependencies first. Cycles are broken deterministically, not dropped."""
    order, seen, stack = [], set(), set()

    def visit(n: str) -> None:
        if n in seen:
            return
        if n in stack:          # cycle — emit here rather than recursing forever
            return
        stack.add(n)
        for d in sorted(deps.get(n, ())):
            visit(d)
        stack.discard(n)
        seen.add(n)
        order.append(n)

    for n in sorted(paths):
        visit(n)
    return order


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.exists() else ""


def _numbers(o, out: dict, pre: str = "") -> dict:
    if isinstance(o, dict):
        for k, v in o.items():
            _numbers(v, out, f"{pre}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            _numbers(v, out, f"{pre}[{i}]")
    elif isinstance(o, (int, float)) and not isinstance(o, bool):
        out[pre] = float(o)
    elif isinstance(o, str) and NUM.match(o):
        try:
            out[pre] = float(o)
        except ValueError:
            pass
    return out


def max_rel_move(before: str, after: Path) -> float | None:
    """Largest relative movement of any shared numeric field. None if new."""
    if not before or not after.exists():
        return None
    try:
        A = _numbers(json.loads(before), {})
        B = _numbers(json.loads(after.read_text(encoding="utf-8")), {})
    except Exception:  # noqa: BLE001
        return None
    worst = 0.0
    skip = ("computedAt", "durationMs", "commitSha", "scriptCommitSha",
            "scriptHash", "engineVersion", "timestamp")
    for k, a in A.items():
        if k not in B or any(s in k for s in skip) or a == 0:
            continue
        worst = max(worst, abs(B[k] - a) / abs(a))
    return worst


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--timeout", type=int, default=900,
                    help="per-producer seconds (default 900)")
    args = ap.parse_args()

    stems = set(former_ideal_muon())
    paths, wit, deps = build_graph(stems)
    order = topo_order(paths, deps)
    if args.limit:
        order = order[:args.limit]

    print("=" * 78)
    print(f" q0 re-pin sweep — {len(order)} producers, dependency-ordered")
    print(f"   unresolvable stems: {len(stems) - len(paths)}")
    print("=" * 78, flush=True)

    if args.dry_run:
        for i, s in enumerate(order, 1):
            d = sorted(deps.get(s, ()))
            print(f"  {i:3}. {s:52} after: {', '.join(d[:3]) or '—'}")
        return 0

    done = {}
    if PROGRESS.exists():
        try:
            done = json.loads(PROGRESS.read_text(encoding="utf-8")).get("done", {})
        except Exception:  # noqa: BLE001
            done = {}
        print(f"  resuming: {len(done)} already recorded\n", flush=True)

    env = dict(os.environ)
    env["PYTHONPATH"] = str(HERE.parent / "tools" / "qou-substrate" / "python") \
        + os.pathsep + env.get("PYTHONPATH", "")
    t_all = time.monotonic()

    for i, s in enumerate(order, 1):
        if s in done:
            continue
        p = paths[s]
        outs = sorted(wit.get(s, ()))
        # Snapshot every witness this producer owns, so movement is measured
        # rather than asserted.
        before = {}
        for n in outs:
            for w in HERE.rglob(n):
                if "_deprecated" not in w.parts:
                    before[n] = w.read_text(encoding="utf-8")
                    break
        t0 = time.monotonic()
        try:
            r = subprocess.run([sys.executable, "-u", p.name],
                               cwd=p.parent, env=env, capture_output=True,
                               text=True, timeout=args.timeout)
            rc, err = r.returncode, (r.stderr or "").strip().splitlines()[-1:] or [""]
        except subprocess.TimeoutExpired:
            rc, err = -9, [f"TIMEOUT >{args.timeout}s"]
        dt = time.monotonic() - t0

        moves = {}
        for n in outs:
            for w in HERE.rglob(n):
                if "_deprecated" in w.parts:
                    continue
                m = max_rel_move(before.get(n, ""), w)
                if m is not None:
                    moves[n] = m
                break
        worst = max(moves.values(), default=0.0)
        done[s] = {"rc": rc, "sec": round(dt, 1), "witnesses": outs,
                   "max_rel_move": worst, "err": err[0][:200]}
        PROGRESS.write_text(json.dumps({"done": done}, indent=1), encoding="utf-8")

        tag = "ok " if rc == 0 else f"FAIL({rc})"
        mv = f"{worst*1e9:.1f} ppb" if worst else "no change"
        print(f"  [{i:3}/{len(order)}] {tag} {dt:6.1f}s  {s:46} {mv}"
              + (f"  {err[0][:60]}" if rc else ""), flush=True)

    ok = sum(1 for v in done.values() if v["rc"] == 0)
    moved = sum(1 for v in done.values() if v["max_rel_move"] > 1e-12)
    print(f"\n  {ok}/{len(done)} exit 0 · {moved} moved · "
          f"{(time.monotonic()-t_all)/60:.1f} min", flush=True)
    print(f"  progress journal: {PROGRESS.name}")
    return 0 if ok == len(done) else 1


if __name__ == "__main__":
    raise SystemExit(main())
