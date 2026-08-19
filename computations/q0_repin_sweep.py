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
import signal
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROGRESS = HERE / "q0-repin-sweep-progress.json"
NUM = re.compile(r"^-?\d*\.?\d+(?:[eE][-+]?\d+)?$")

# Live producer subprocesses, so a SIGTERM/SIGINT to this driver takes them
# with it instead of orphaning them to init. See the comment at the Popen call.
_CHILDREN: list = []


def _kill_group(proc) -> None:
    """SIGKILL a producer's whole process group; tolerate an already-dead one."""
    if proc is None:
        return
    try:
        os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
    except (ProcessLookupError, PermissionError, OSError):
        try:
            proc.kill()
        except Exception:  # noqa: BLE001
            pass


def _on_signal(signum, _frame):  # noqa: ANN001
    for p in list(_CHILDREN):
        _kill_group(p)
    raise SystemExit(128 + signum)


for _s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
    try:
        signal.signal(_s, _on_signal)
    except (ValueError, OSError):
        pass


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
    stems = json.loads(out.stdout).get("ideal_muon", [])
    return [s for s in stems if s not in ANCHOR_DEFINING]


# The producers that DEFINE the muon anchor rather than merely consume it.
# Sweeping one of these does not migrate a consumer to the proton pin — it
# destroys the muon layer, because `qou_substrate.witness._q0_value_for_anchor`
# resolves the muon anchor by READING the witness they emit.
#
# This exclusion exists because the sweep did exactly that in 9a9c6b31c7
# ("first 25 witnesses regenerated at the proton pin"), which re-pinned
# computations/q-pinning-50-digit.witness.json to 1.10997858275… . Three
# things broke at once on main:
#   * _q0_value_for_anchor("muon") began returning the PROTON value, so both
#     anchors resolved identically;
#   * 262 correctly-stamped muon witnesses flipped to Q0_FLIP (Q0_OK 654 -> 392);
#   * the anti-corruption guard at substrate/q_parameter.py:224 hard-failed
#     EVERY ideal_muon producer — "Refusing to fall back to proton silently
#     (bean yfvb / tnjb)" — so they could not be run at all, including the one
#     that would regenerate the anchor.
# The guard did its job; nothing silently corrupted. But the sweep had no
# exclusion list, so a re-run would reproduce all three.
# PAIRED WITH `ANCHOR_DEFINITIONS` BELOW — two guards, two layers, and the
# names are one letter apart, so read both before editing either. This one
# holds PRODUCER STEMS and drops them from former_ideal_muon(), so the
# producer is never scheduled. `ANCHOR_DEFINITIONS` holds WITNESS FILENAMES
# and drops them in build_graph(), so the witness is never treated as a
# consumer node. They were added independently for the same incident (this
# PR #5296 / bean qou-w4gn; the other PR #5265-adjacent / bean qou-cezp) and
# are complementary, not redundant — but editing one and assuming the defect
# is covered would leave the other layer open.
ANCHOR_DEFINING = frozenset({"q_pinning_50_digit"})


# Witnesses that DEFINE an anchor rather than consume one. The sweep must
# never re-pin these: doing so redefines the anchor instead of migrating a
# consumer. See the note in build_graph. Bean qou-cezp.
# PAIRED WITH `ANCHOR_DEFINING` ABOVE — see the note there. This set is keyed
# on WITNESS FILENAME and guards build_graph(); that one is keyed on PRODUCER
# STEM and guards former_ideal_muon().
ANCHOR_DEFINITIONS = frozenset({"q-pinning-50-digit.witness.json"})


def build_graph(stems: set[str]):
    """producer stem -> (script path, its witness names, stems it reads)."""
    wit: dict[str, set[str]] = {}
    for w in HERE.rglob("*.witness.json"):
        if "_deprecated" in w.parts:
            continue
        if w.name in ANCHOR_DEFINITIONS:
            # NOT a consumer. `q-pinning-50-digit.witness.json` DEFINES the muon
            # anchor: qou_substrate.witness._q0_value_for_anchor("muon") reads
            # its `derived_50_digit.q`, and q_parameter.py reads it to build the
            # whole ideal/muon q-closure family. Re-pinning it to proton does
            # not migrate a consumer -- it redefines what "muon" MEANS, so every
            # muon-anchored witness in the corpus then disagrees with its own
            # anchor. That happened in 9a9c6b31c7 and produced 262 Q0_FLIPs plus
            # a hard RuntimeError on QOU_Q0_ANCHOR=ideal|muon. Bean qou-cezp.
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


# Relative movement is meaningless once the denominator approaches the
# numerical floor: a residual going 1e-60 -> 1.5e-59 reads as "9e9 ppb" and
# says nothing. Fields below this magnitude are excluded from the movement
# statistic (they still count for "did anything change at all").
_DENOM_FLOOR = 1e-20


def rel_moves(before: str, after: Path) -> tuple[float, float, int] | None:
    """(max, median, n) relative movement over shared numeric fields.

    The max alone is a poor summary — one near-zero denominator dominates it —
    so the median is carried too. Both exclude the ephemeral meta fields, so
    rebase drift is never mistaken for a result.
    """
    if not before or not after.exists():
        return None
    try:
        A = _numbers(json.loads(before), {})
        B = _numbers(json.loads(after.read_text(encoding="utf-8")), {})
    except Exception:  # noqa: BLE001
        return None
    skip = ("computedAt", "durationMs", "commitSha", "scriptCommitSha",
            "scriptHash", "engineVersion", "timestamp")
    moves = []
    for k, a in A.items():
        if k not in B or any(s in k for s in skip) or abs(a) < _DENOM_FLOOR:
            continue
        moves.append(abs(B[k] - a) / abs(a))
    if not moves:
        return (0.0, 0.0, 0)
    moves.sort()
    return (moves[-1], moves[len(moves) // 2], len(moves))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--timeout", type=int, default=900,
                    help="per-producer seconds (default 900)")
    ap.add_argument("--skip", default="", metavar="STEM,STEM",
                    help="producers to leave alone — for long-compute cases "
                         "being run standalone. Without this, a producer that "
                         "exceeds --timeout is requeued on every resume and "
                         "burns the full timeout again each time, which with "
                         "frequent container restarts costs more than the "
                         "producer does.")
    args = ap.parse_args()

    stems = set(former_ideal_muon())
    skip = {s.strip() for s in args.skip.split(",") if s.strip()}
    paths, wit, deps = build_graph(stems)
    order = [s for s in topo_order(paths, deps) if s not in skip]
    if skip:
        print(f"  skipping {len(skip)}: {', '.join(sorted(skip))}", flush=True)
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
        # Retry failures on resume. A journalled rc != 0 is unfinished work,
        # not a result — treating it as done would silently leave the producer
        # stale, which is the whole thing this sweep exists to prevent.
        retry = [s for s, v in done.items() if v.get("rc") != 0]
        for s in retry:
            del done[s]
        print(f"  resuming: {len(done)} complete, {len(retry)} failures requeued\n",
              flush=True)

    # Producers live in several subdirectories and reach each other by bare
    # name (`from _precision import …`, `import _path_bridge`). Running one
    # from its own directory is not enough — `computations/` and
    # `computations/substrate/` must be importable too, or ~40 of them die on
    # ModuleNotFoundError before computing anything.
    env = dict(os.environ)
    _tools = HERE.parent / "tools"
    env["PYTHONPATH"] = os.pathsep.join([p for p in [
        str(_tools / "qou-substrate" / "python"),
        str(_tools / "pyhecke" / "python"),
        str(_tools / "pyhecke-native" / "src"),
        str(HERE),
        str(HERE / "substrate"),
        env.get("PYTHONPATH", ""),
    ] if p]).rstrip(os.pathsep)
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
        # Run each producer in its OWN process group, and kill the group — not
        # just the immediate child — on timeout or on our own termination.
        #
        # Measured: `pkill`-ing this driver (which the container restarts force
        # several times a run) left its producer alive and REPARENTED TO INIT.
        # The relaunched sweep then started the same script again, so two
        # processes wrote one witness concurrently — observed with
        # block_swap_binding.py running twice, 6 min and 3 min in. A
        # double-write is precisely the silent corruption this whole re-pin
        # exists to remove, so the sweep must not be a source of it.
        proc = None
        try:
            proc = subprocess.Popen([sys.executable, "-u", p.name],
                                    cwd=p.parent, env=env,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, text=True,
                                    start_new_session=True)
            _CHILDREN.append(proc)
            _out, _errtxt = proc.communicate(timeout=args.timeout)
            rc = proc.returncode
            err = (_errtxt or "").strip().splitlines()[-1:] or [""]
        except subprocess.TimeoutExpired:
            _kill_group(proc)
            proc.communicate()
            rc, err = -9, [f"TIMEOUT >{args.timeout}s"]
        finally:
            if proc in _CHILDREN:
                _CHILDREN.remove(proc)
        dt = time.monotonic() - t0

        mx = md = 0.0
        nfields = 0
        for n in outs:
            for w in HERE.rglob(n):
                if "_deprecated" in w.parts:
                    continue
                r = rel_moves(before.get(n, ""), w)
                if r:
                    mx, md = max(mx, r[0]), max(md, r[1])
                    nfields += r[2]
                break
        done[s] = {"rc": rc, "sec": round(dt, 1), "witnesses": outs,
                   "max_rel_move": mx, "median_rel_move": md,
                   "n_fields": nfields, "err": err[0][:200]}
        PROGRESS.write_text(json.dumps({"done": done}, indent=1), encoding="utf-8")

        tag = "ok " if rc == 0 else f"FAIL({rc})"
        mv = (f"med {md*1e9:,.1f} / max {mx*1e9:,.1f} ppb" if mx else "no change")
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
