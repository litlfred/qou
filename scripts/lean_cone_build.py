#!/usr/bin/env python3
"""lean_cone_build.py — topologically compile QOU import cones with `lean` directly.

Driver behind ``scripts/lean-direct-cone.sh``.  See that script for motivation
(``lake build`` rebuilds Mathlib from source and wipes restored oleans; when the
Mathlib oleans are already on disk we can bypass Lake entirely).

What this adds over the original inline bash/python:

1. **The root aggregator module is included.**  The old topo-sort walked only the
   ``QOU/`` directory, so ``lean/QOU.lean`` — a *sibling* of that directory — was
   never in the import map.  Asking for target ``QOU`` therefore produced a
   one-element order and invoked ``lean`` on a ~1000-import aggregator with none
   of its dependencies compiled.
2. **Keep-going with dependency propagation.**  A cone builder that aborts on the
   first bad module cannot survey a corpus.  With ``--keep-going`` a failing
   module is recorded and every module transitively importing it is marked
   ``blocked`` *without* being compiled — which is exactly the
   genuine-error vs missing-olean-cascade classification.
3. **Parallel scheduling.**  Ready modules (all deps ``ok``/``up-to-date``) are
   dispatched to a worker pool.
4. **A machine-readable report** (TSV + JSON) of per-module status.

Statuses: ``ok`` | ``up-to-date`` | ``error`` | ``blocked`` | ``missing-source``.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from pathlib import Path

IMPORT_RE = re.compile(r"^import\s+(QOU(?:\.[A-Za-z0-9_'À-￿]+)*)")


def qou_imports(text: str) -> list[str]:
    """QOU modules imported by `text`, read from the header only.

    Lean requires every `import` to precede all other content, so the header is
    exactly the leading run of imports, comments and blank lines — and stopping
    there is not merely an optimisation.  Scanning the whole file (which this
    did, via `re.M`) treats an `import` line written flush-left inside a
    docstring as a real dependency.  A module whose docstring *documents* an
    import cycle then appears to have one, and `topo` aborts the entire build
    with a bogus `IMPORT CYCLE`.  Observed 2026-08-23 on `QOU/GroundRingCore.lean`,
    whose docstring quotes the two-line import that demonstrates bean `qou-kfcl`.
    """
    out: list[str] = []
    in_block_comment = False
    for line in text.splitlines():
        stripped = line.strip()
        if in_block_comment:
            if "-/" in stripped:
                in_block_comment = False
            continue
        if stripped.startswith("/-"):
            if "-/" not in stripped:
                in_block_comment = True
            continue
        if not stripped or stripped.startswith("--"):
            continue
        m = IMPORT_RE.match(line)
        if m:
            out.append(m.group(1))
            continue
        if stripped.startswith("import "):
            continue  # a non-QOU import; still part of the header
        break  # first real declaration — the header is over
    return out

# Extra `lean` flags, e.g. the package's `moreLeanArgs = ["-s", "65536"]`.
EXTRA_ARGS = os.environ.get("LEAN_CONE_EXTRA_ARGS", "").split()

# Per-module failure logs are capped: the error shape lives in the first few
# errors, and 1622 uncapped logs is what filled the disk on the first attempt.
LOG_MAX_LINES = int(os.environ.get("LEAN_CONE_LOG_MAX_LINES", "60"))


def module_of(leandir: Path, path: Path) -> str:
    rel = path.relative_to(leandir).with_suffix("")
    return ".".join(rel.parts)


def scan(leandir: Path) -> dict[str, dict]:
    """Map module name -> {src, imports}. Includes the root QOU.lean aggregator."""
    mods: dict[str, dict] = {}
    roots = [leandir / "QOU.lean", *sorted((leandir / "QOU").rglob("*.lean"))]
    for p in roots:
        if not p.is_file():
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        mods[module_of(leandir, p)] = {
            "src": p,
            "imports": sorted(set(qou_imports(text))),
        }
    return mods


def topo(mods: dict[str, dict], targets: list[str]) -> list[str]:
    order: list[str] = []
    state: dict[str, int] = {}
    stack: list[str] = []

    def visit(m: str) -> None:
        st = state.get(m)
        if st == 2:
            return
        if st == 1:
            cyc = " -> ".join(stack[stack.index(m):] + [m])
            raise SystemExit(f"IMPORT CYCLE: {cyc}")
        state[m] = 1
        stack.append(m)
        for d in mods.get(m, {}).get("imports", ()):
            visit(d)
        stack.pop()
        state[m] = 2
        order.append(m)

    for t in targets:
        visit(t)
    return order


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("targets", nargs="*", help="QOU module names (default: --all)")
    ap.add_argument("--all", action="store_true", help="build every QOU module")
    ap.add_argument("-k", "--keep-going", action="store_true")
    ap.add_argument("-j", "--jobs", type=int, default=max(1, (os.cpu_count() or 2) - 1))
    ap.add_argument("--report", help="write TSV report here (JSON at <report>.json)")
    ap.add_argument("--log-dir", default="/tmp/lean-cone-logs")
    ap.add_argument("--leandir", required=True)
    ap.add_argument("--min-free-gb", type=float, default=1.5,
                    help="stop scheduling new modules below this much free disk; "
                         "drain in-flight work and still write the report")
    args = ap.parse_args()

    leandir = Path(args.leandir).resolve()
    out = leandir / ".lake" / "build" / "lib" / "lean"
    out.mkdir(parents=True, exist_ok=True)
    logdir = Path(args.log_dir)
    logdir.mkdir(parents=True, exist_ok=True)

    mods = scan(leandir)
    if args.all or not args.targets:
        targets = sorted(mods)
    else:
        targets = args.targets
        for t in targets:
            if t not in mods:
                sys.exit(f"unknown module: {t}")

    order = topo(mods, targets)
    total = len(order)
    print(f"cone: {total} modules, jobs={args.jobs}", flush=True)

    def olean_of(m: str) -> Path:
        return out / (m.replace(".", "/") + ".olean")

    status: dict[str, str] = {}
    errhead: dict[str, str] = {}
    secs: dict[str, float] = {}
    blocker: dict[str, str] = {}
    rebuilt: set[str] = set()
    presealed: dict[str, str] = {}  # modules whose verdict is known before scheduling

    # in-cone dependency edges + reverse counts for the scheduler
    deps = {m: [d for d in mods.get(m, {}).get("imports", ()) if d in set(order)] for m in order}
    inorder = set(order)
    for m in order:
        for d in mods.get(m, {}).get("imports", ()):
            if d not in inorder:
                # dangling QOU import (source file absent) — a genuine defect,
                # but distinct from a type error, so it gets its own status.
                presealed.setdefault(m, "missing-source")
                errhead.setdefault(m, f"import of nonexistent module {d}")
    remaining = {m: len(deps[m]) for m in order}
    rdeps: dict[str, list[str]] = {m: [] for m in order}
    for m in order:
        for d in deps[m]:
            rdeps[d].append(m)

    ready = [m for m in order if remaining[m] == 0]
    t0 = time.time()

    def fresh(m: str) -> bool:
        """olean usable as-is: newer than source, newer than every dep olean,
        and no dep was rebuilt in this run."""
        ol = olean_of(m)
        src = mods[m]["src"]
        if not ol.is_file() or ol.stat().st_mtime <= src.stat().st_mtime:
            return False
        for d in deps[m]:
            if d in rebuilt:
                return False
            do = olean_of(d)
            if do.is_file() and do.stat().st_mtime > ol.stat().st_mtime:
                return False
        return True

    def free_gb() -> float:
        st = os.statvfs(str(out))
        return st.f_bavail * st.f_frsize / 1e9

    def compile_one(m: str) -> tuple[str, int, str, float]:
        ol = olean_of(m)
        ol.parent.mkdir(parents=True, exist_ok=True)
        t = time.time()
        proc = subprocess.run(
            ["lean", "-DautoImplicit=false", *EXTRA_ARGS, "-o", str(ol),
             str(mods[m]["src"])],
            capture_output=True, text=True,
        )
        outtxt = (proc.stdout or "") + (proc.stderr or "")
        if proc.returncode != 0:
            # Logs are written for FAILURES ONLY, and capped: classifying an
            # error shape needs the first errors, not a module's entire output.
            lines = outtxt.splitlines()
            capped = "\n".join(lines[:LOG_MAX_LINES])
            if len(lines) > LOG_MAX_LINES:
                capped += f"\n[... {len(lines) - LOG_MAX_LINES} more lines truncated]"
            try:
                (logdir / (m + ".log")).write_text(capped, encoding="utf-8")
            except OSError as e:  # e.g. ENOSPC — never let logging kill the sweep
                outtxt += f"\n[log write failed: {e}]"
            # a failed lean run can leave a truncated olean behind
            if ol.is_file():
                try:
                    ol.unlink()
                except OSError:
                    pass
        return m, proc.returncode, outtxt, time.time() - t

    # Incremental report: a row is appended the moment a module settles, so a
    # crash at 90% leaves 90% of the data rather than nothing (the first
    # full-corpus attempt died mid-run and produced no report at all).
    live = None
    if args.report:
        live = open(str(args.report) + ".partial", "w", encoding="utf-8")
        live.write("module\tstatus\tseconds\tblocker\terror_head\n")

    def emit(m: str, st: str) -> None:
        if live is None:
            return
        live.write(f"{m}\t{st}\t{secs.get(m, 0):.1f}\t"
                   f"{blocker.get(m, '')}\t{errhead.get(m, '')}\n")
        live.flush()

    def settle(m: str, st: str) -> None:
        status[m] = st
        emit(m, st)
        if st in ("ok", "up-to-date"):
            for r in rdeps[m]:
                remaining[r] -= 1
                if remaining[r] == 0:
                    ready.append(r)
        else:
            propagate(m)

    def propagate(m: str) -> None:
        """m failed: every module transitively importing it is `blocked` —
        it is not compiled at all, so it can never be counted as a genuine red.
        `blocker` records the ultimate upstream culprit."""
        root = blocker.get(m, m)
        stack = [m]
        while stack:
            cur = stack.pop()
            for r in rdeps[cur]:
                if status.get(r) is None:
                    status[r] = "blocked"
                    blocker[r] = root
                    emit(r, "blocked")
                    stack.append(r)

    last_report = time.time()
    disk_stop = False
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futs: dict = {}
        while (ready and not disk_stop) or futs:
            if not disk_stop and free_gb() < args.min_free_gb:
                disk_stop = True
                print(f"DISK GUARD: {free_gb():.2f} GB free < {args.min_free_gb} GB — "
                      f"no new modules scheduled; draining {len(futs)} in flight",
                      flush=True)
            while ready and not disk_stop and len(futs) < args.jobs:
                m = ready.pop()
                if status.get(m) is not None:  # already blocked by an upstream failure
                    continue
                if m in presealed:
                    settle(m, presealed[m])
                    continue
                if fresh(m):
                    secs[m] = 0.0
                    settle(m, "up-to-date")
                    continue
                futs[pool.submit(compile_one, m)] = m
            if not futs:
                continue
            done, _ = wait(list(futs), return_when=FIRST_COMPLETED, timeout=30)
            for f in done:
                m = futs.pop(f)
                mm, rc, outtxt, dt = f.result()
                secs[mm] = dt
                if rc == 0:
                    rebuilt.add(mm)
                    settle(mm, "ok")
                else:
                    lines = [l for l in outtxt.splitlines() if l.strip()]
                    errhead[mm] = lines[0][:400] if lines else f"exit {rc}, no output"
                    settle(mm, "error")
                    if not args.keep_going:
                        print(f"FAILED: {mm}\n{outtxt[:4000]}", flush=True)
                        return 1
            if time.time() - last_report > 20:
                last_report = time.time()
                nok = sum(1 for v in status.values() if v in ("ok", "up-to-date"))
                nerr = sum(1 for v in status.values() if v == "error")
                nbl = sum(1 for v in status.values() if v == "blocked")
                el = time.time() - t0
                pct = 100.0 * len(status) / total
                eta = (el / max(len(status), 1)) * (total - len(status))
                print(f"  [{len(status)}/{total} {pct:.1f}%] ok={nok} err={nerr} "
                      f"blocked={nbl} ready={len(ready)} inflight={len(futs)} "
                      f"free={free_gb():.1f}GB elapsed={el:.0f}s eta={eta:.0f}s",
                      flush=True)

    if disk_stop:
        # Distinguish "never scheduled because the disk guard fired" from
        # "blocked by a red upstream" — conflating them would inflate the
        # unknown-because-of-the-corpus bucket with an environment artifact.
        for m in order:
            if status.get(m) is None:
                status[m] = "unscheduled-disk"
    for m in order:
        status.setdefault(m, "blocked")

    counts: dict[str, int] = {}
    for v in status.values():
        counts[v] = counts.get(v, 0) + 1
    print("done:", ", ".join(f"{k}={v}" for k, v in sorted(counts.items())),
          f"in {time.time() - t0:.0f}s", flush=True)

    if live is not None:
        live.close()
    if args.report:
        rp = Path(args.report)
        with rp.open("w", encoding="utf-8") as fh:
            fh.write("module\tstatus\tseconds\tblocker\terror_head\n")
            for m in order:
                fh.write(f"{m}\t{status[m]}\t{secs.get(m, 0):.1f}\t"
                         f"{blocker.get(m, '')}\t{errhead.get(m, '')}\n")
        Path(str(rp) + ".json").write_text(json.dumps({
            "total": total, "counts": counts,
            "modules": {m: {"status": status[m], "seconds": round(secs.get(m, 0), 1),
                            "blocker": blocker.get(m), "error_head": errhead.get(m)}
                        for m in order},
        }, indent=1), encoding="utf-8")
        print(f"report: {rp}", flush=True)

    bad = counts.get("error", 0) + counts.get("missing-source", 0)
    return 1 if bad and not args.keep_going else 0


if __name__ == "__main__":
    sys.exit(main())
