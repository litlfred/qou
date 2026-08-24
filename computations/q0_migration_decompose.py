#!/usr/bin/env python3
"""Migrate a producer to the proton anchor, separating DRIFT from ANCHOR.

## Why this is not just "re-run at proton"

`q0_repin_sweep.py` re-runs each `ideal_muon` producer once and reports how
far its witness moved. That number is not the anchor's effect. A witness
committed weeks ago also moves because the producer's IMPORT CONE changed
underneath it — measured here on `adjacent_vs_full_probe`, a producer already
at the proton anchor whose `B_adjacent_raw` still moves 4.550 -> 1.463 (3x) on
a plain re-run. Attributing that to the muon->proton migration would write a
month of unrelated code evolution into the corpus under a migration commit,
where nothing can later separate the two.

So each producer is run TWICE, from the same tree:

    committed  --(A)-->  muon_now  --(B)-->  proton_now

  * (A) committed vs muon_now: SAME anchor, current code. This is pure
    staleness -- import-cone drift, library differences, non-determinism.
  * (B) muon_now vs proton_now: SAME code, same instant, anchor swapped.
    This is the migration's actual effect, and it is the only part the
    11.54 ppb muon-proton separation can explain.

`proton_now` is what gets kept. Both magnitudes are reported, so a reviewer
can see which producers moved because of the anchor and which merely had a
stale witness that this sweep happened to refresh.

A producer whose (B) is zero is q0-INDEPENDENT: the migration is a relabel
for it, and any movement it shows is (A) and belongs in a staleness commit,
not this one.

Usage:
    python3 -u q0_migration_decompose.py --list
    python3 -u q0_migration_decompose.py --limit 10
    python3 -u q0_migration_decompose.py --stems a,b,c
    python3 -u q0_migration_decompose.py            # all remaining
"""
from __future__ import annotations

import argparse
import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MU_PREFIX = "1.109978595557"
PROGRESS = HERE / "q0-migration-decompose-progress.json"

# Never re-pin these: they DEFINE an anchor rather than consume one. Re-running
# q_pinning_50_digit at the proton pin does not migrate a consumer, it destroys
# the muon layer -- `qou_substrate.witness._q0_value_for_anchor("muon")` reads
# its `derived_50_digit.q`. That is what took main red on 2026-08-19; see the
# note in q0_repin_sweep.ANCHOR_DEFINING and AGENTS.md.
ANCHOR_DEFINING = frozenset({"q_pinning_50_digit"})

# A producer that spells the muon q0 as a LITERAL in its own source does not
# read q_parameter for it, so QOU_Q0_ANCHOR never reaches the arithmetic. Its
# payload comes back byte-for-byte muon and the only field that moves is
# WitnessBuilder's .q0Value provenance stamp -- producing a witness that
# DECLARES proton over a payload computed at muon, which is the layer straddle
# AGENTS.md forbids and is strictly worse than the honest muon witness.
#
# Measured: 36 of 89 apparently-migrated producers were this, and the
# drift/anchor decomposition scored every one of them anchor+drift, because it
# compares whole witnesses and a provenance stamp is part of the witness.
# Separating drift from anchor is necessary and NOT sufficient; the third
# question is whether the anchor reached the ARITHMETIC. Migrating these needs
# a source change (resolve q0 through q_parameter), not a re-run.
MUON_LITERAL = "1.109978595557"


def hardcodes_muon(script: Path) -> bool:
    try:
        return MUON_LITERAL in script.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False

sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(HERE))
from qou_substrate.witness import _strip_ephemeral_fields as strip  # noqa: E402
# Reuse the sweep's producer->witness->reader graph rather than re-deriving it.
from q0_repin_sweep import build_graph, topo_order  # noqa: E402


def env_for(anchor: str | None) -> dict:
    env = dict(os.environ)
    tools = ROOT / "tools"
    env["PYTHONPATH"] = os.pathsep.join([
        str(tools / "qou-substrate" / "python"),
        str(tools / "pyhecke" / "python"),
        str(tools / "pyhecke-native" / "src"),
        str(HERE), str(HERE / "substrate"),
        env.get("PYTHONPATH", ""),
    ]).rstrip(os.pathsep)
    env.pop("QOU_Q0_ANCHOR", None)
    if anchor:
        env["QOU_Q0_ANCHOR"] = anchor
    return env


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True,
                          text=True).stdout


# Paths migrated so far. A reset has to cover the WHOLE computations tree --
# producers write sibling witnesses, so a narrower one leaves others dirty --
# but a blanket reset would also discard everything migrated earlier in the
# run, leaving only the last producer's output in the tree. So the reset skips
# the migrated paths: the WORKING TREE is the accumulator, which also means the
# results survive a container restart and a consumer run later in topological
# order reads its upstream's MIGRATED value rather than the stale committed one.
MIGRATED: set[str] = set()


def restore() -> None:
    """Reset every dirty file under computations/ EXCEPT the migrated ones."""
    # Witness/data JSON only. An earlier version reverted every dirty tracked
    # file under computations/, which includes the producers' own sources and
    # this script -- it silently ate an edit to itself mid-run. A sweep must
    # never revert source it did not write.
    revert = [rel for rel in dirty()
              if rel not in MIGRATED and rel.endswith(".json")]
    for i in range(0, len(revert), 200):       # argv limit on a wide sweep
        subprocess.run(["git", "checkout", "--", *revert[i:i + 200]],
                       cwd=ROOT, capture_output=True)


def dirty() -> list[str]:
    out = git("status", "--porcelain", "computations/")
    return [ln[3:].strip() for ln in out.splitlines() if ln.strip()]


def snapshot() -> dict[str, str]:
    """Path -> text, for every witness the last run touched."""
    snap = {}
    for rel in dirty():
        p = ROOT / rel
        if p.suffix == ".json" and p.exists():
            try:
                snap[rel] = p.read_text(encoding="utf-8")
            except Exception:  # noqa: BLE001
                pass
    return snap


def run_once(script: Path, anchor: str | None, timeout: int):
    t0 = time.monotonic()
    # Popen, not subprocess.run: run()'s timeout kills only the DIRECT child, so
    # a producer that spawns children leaves them alive and reparented to init,
    # and the next leg then writes the same witness concurrently.
    # q0_repin_sweep records observing exactly that. start_new_session puts the
    # producer in its own group so the whole group can be killed by pgid.
    proc = subprocess.Popen([sys.executable, script.name], cwd=script.parent,
                            env=env_for(anchor), stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, text=True,
                            start_new_session=True)
    try:
        _, stderr = proc.communicate(timeout=timeout)
        rc = proc.returncode
        # Last NON-EMPTY line: a traceback often ends blank, and reporting that
        # made alpha_high_precision's rc=1 undiagnosable.
        err = [ln for ln in (stderr or "").splitlines() if ln.strip()]
    except subprocess.TimeoutExpired:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        except (ProcessLookupError, PermissionError, OSError):
            proc.kill()
        proc.communicate()
        rc, err = -9, [f"TIMEOUT >{timeout}s"]
    return rc, snapshot(), round(time.monotonic() - t0, 1), (err[-1].strip() if err else "")


def differs(a: str | None, b: str | None) -> bool:
    """Substantive inequality: ephemeral meta (timestamps, shas, env) masked."""
    if a is None or b is None:
        return a != b
    try:
        return strip(json.loads(a)) != strip(json.loads(b))
    except Exception:  # noqa: BLE001
        return a != b


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int)
    ap.add_argument("--stems")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--timeout", type=int, default=900)
    a = ap.parse_args()

    man = json.loads((HERE / "q0_anchor_manifest.json").read_text())
    ideal = [s for s in man["ideal_muon"] if s not in ANCHOR_DEFINING]

    # Only the ones whose witness still carries the muon q0 -- the rest are
    # already migrated in data and need the manifest move, not a re-run.
    todo, paths = [], {}
    for p in HERE.rglob("*.witness.json"):
        if "_deprecated" in p.parts:
            continue
        try:
            t = p.read_text(encoding="utf-8")
            d = json.loads(t)
        except Exception:  # noqa: BLE001
            continue
        if not isinstance(d, dict):
            continue
        sf = d.get("scriptFile") or ""
        stem = sf[:-3] if isinstance(sf, str) and sf.endswith(".py") else sf
        if stem in ideal and MU_PREFIX in t:
            todo.append(stem)
    todo = sorted(set(todo))
    for s in todo:
        for c in HERE.rglob(f"{s}.py"):
            if "_deprecated" not in c.parts:
                paths[s] = c
                break

    todo = [s for s in todo if s in paths]
    # Dependencies first: a consumer run before its producer would re-emit the
    # stale upstream value into a freshly-migrated downstream (bean qou-lt8x).
    _paths, _wit, _deps = build_graph(set(todo))
    _rank = {s: i for i, s in enumerate(topo_order(_paths, _deps))}
    todo.sort(key=lambda s: (_rank.get(s, len(_rank)), s))
    if a.stems:
        want = {x.strip() for x in a.stems.split(",")}
        todo = [s for s in todo if s in want]

    done = {}
    if PROGRESS.exists():
        try:
            done = json.loads(PROGRESS.read_text()).get("done", {})
        except Exception:  # noqa: BLE001
            done = {}
    done = {k: v for k, v in done.items() if v.get("rc_proton") == 0}
    # Resume: the migrated files are still in the working tree from the earlier
    # run, so re-register them or the first restore() would revert the lot.
    for v in done.values():
        MIGRATED.update(v.get("files") or ())

    todo = [s for s in todo if s not in done]
    if a.limit:
        todo = todo[:a.limit]

    hard = [s for s in todo if hardcodes_muon(paths[s])]
    if hard:
        print(f"skipping {len(hard)} producer(s) that hardcode the muon q0 in "
              f"source -- a re-run cannot migrate them, it only flips the "
              f"provenance stamp:", flush=True)
        for s in hard:
            print(f"    {s}", flush=True)
        print(flush=True)
    todo = [s for s in todo if s not in set(hard)]

    if a.list:
        for s in todo:
            print(s)
        print(f"\n{len(todo)} producer(s) to migrate", file=sys.stderr)
        return 0

    print(f"{len(todo)} producer(s); {len(done)} already done\n", flush=True)
    for i, s in enumerate(todo, 1):
        restore()
        base = {}
        rc_m, snap_m, sec_m, err_m = run_once(paths[s], None, a.timeout)
        # Baseline = what is committed, for exactly the files this run touched.
        for rel in snap_m:
            base[rel] = git("show", f"HEAD:{rel}") or None
        restore()
        rc_p, snap_p, sec_p, err_p = run_once(paths[s], "proton", a.timeout)

        files = sorted(set(snap_m) | set(snap_p))
        drift = any(differs(base.get(f), snap_m.get(f)) for f in files)
        anchor = any(differs(snap_m.get(f), snap_p.get(f)) for f in files)

        if rc_p != 0 or rc_m != 0:
            tag = f"FAIL(m={rc_m},p={rc_p})"
        else:
            tag = ("anchor+drift" if (anchor and drift) else
                   "anchor-only" if anchor else
                   "DRIFT-ONLY (q0-independent)" if drift else
                   "no change")
        print(f"[{i:3d}/{len(todo)}] {sec_m + sec_p:6.1f}s  {s:<52s} {tag}"
              f"{('  ' + (err_p or err_m)) if rc_p or rc_m else ''}", flush=True)

        done[s] = {"rc_muon": rc_m, "rc_proton": rc_p,
                   "sec": round(sec_m + sec_p, 1), "files": files,
                   "drift": drift, "anchor": anchor,
                   "err": (err_p or err_m)[:400]}
        PROGRESS.write_text(json.dumps({"done": done}, indent=1) + "\n")
        # Keep the PROTON result -- that is the migration target. A refused
        # proton leg (a producer that needs muon by design) keeps nothing.
        if rc_p == 0:
            MIGRATED.update(snap_p.keys())
        else:
            restore()

    n_anchor = sum(1 for v in done.values() if v.get("anchor"))
    n_drift = sum(1 for v in done.values() if v.get("drift"))
    print(f"\nof {len(done)}: {n_anchor} moved by the ANCHOR, "
          f"{n_drift} also carried pre-existing DRIFT", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
