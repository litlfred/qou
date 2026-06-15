#!/usr/bin/env python3
# polynomial_q_not_applicable: batch orchestrator, not a q-series compute.
"""Batch-regenerate the q₀-stale witnesses, committing + pushing per producer.

**Why.** The 2026-05-28 q₀ muon→proton re-pin (commit `01c18125`) shifted q₀
~1.3e-8 *without touching any producer script*, so `run_pipeline.py`'s
`scriptHash` staleness gate is blind to it and ~392 committed witnesses still
carry the pre-re-pin q₀ (see `witness_constant_staleness.py` +
`docs/audits/2026-05-30-q0-repin-stale-witness-audit.md`).

**What.** Groups the stale witnesses by their recorded ``scriptFile``, runs
each producer (which re-emits its witness against the *live* proton-anchored
q₀ from ``qou_substrate.constants``), and **commits + pushes after every
producer** so progress survives a container death (the owner's explicit
requirement: "progress is not lost on failure").

**Safety.** A regenerated witness is committed **only if** its q₀-shaped
value is now current (else the run is treated as a no-op / failure and the
working tree is reset). Per-producer timeout skips slow heavy-atom producers
for a dedicated long-timeout pass (logged to ``--logfile``). Fully
**resumable** — each invocation re-scans, so already-fresh witnesses are
skipped.

Usage::

    python3 -u q0_repin_regen_batch.py --plan          # list producers, no run
    python3 -u q0_repin_regen_batch.py --timeout 300   # full run (commit+push)
    python3 -u q0_repin_regen_batch.py --limit 5       # first 5 producers only
    python3 -u q0_repin_regen_batch.py --no-push       # commit but don't push
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import glob
import json
import re
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
for p in (str(HERE), str(REPO / "tools" / "qou-substrate" / "python")):
    if p not in sys.path:
        sys.path.insert(0, p)

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

NDIGITS = 12
CUR = Q_50_DIGIT_STR[: NDIGITS + 2]
# Reuse the detector's live-derived basin + audit exemption as the single
# source of truth (fixes the same hard-coded-regex / audit-false-positive
# bugs Copilot flagged on the detector). Local fallback if unavailable.
try:
    from witness_constant_staleness import Q0_SHAPE as SHAPE, AUDIT_SUFFIXES
except Exception:  # pragma: no cover
    SHAPE = re.compile(re.escape(Q_50_DIGIT_STR[:6]) + r"\d{6,}")
    AUDIT_SUFFIXES = ("-audit.witness.json", "-scan.witness.json",
                      "-compliance.witness.json")
WGLOB = "folio-assistant/computations/*.witness.json"
BRANCH = "claude/q0-repin-regen-batch-2026-05-30"


def stale_q0(raw: str) -> bool:
    return any(m.group(0)[: NDIGITS + 2] != CUR for m in SHAPE.finditer(raw))


def scan_stale() -> dict[str, list[str]]:
    """Map producer scriptFile → [stale witness relpaths]."""
    by_script: dict[str, list[str]] = defaultdict(list)
    for wf in glob.glob(str(REPO / WGLOB)):
        if Path(wf).name.endswith(AUDIT_SUFFIXES):
            continue  # state-tracking witness — intentional q₀, not stale
        raw = Path(wf).read_text()
        if not stale_q0(raw):
            continue
        try:
            sf = json.loads(raw).get("scriptFile")
        except Exception:
            sf = None
        rel = str(Path(wf).relative_to(REPO))
        by_script[sf or "<no-scriptFile>"].append(rel)
    return by_script


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=REPO, text=True,
                          capture_output=True, check=check)


def push_with_retry(log) -> bool:
    for i in range(4):
        r = git("push", "-u", "origin", BRANCH, check=False)
        if r.returncode == 0:
            return True
        log(f"    push failed (try {i+1}): {r.stderr.strip()[:120]}")
        time.sleep(2 ** (i + 1))
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true", help="list producers, no run")
    ap.add_argument("--timeout", type=int, default=300, help="per-producer seconds")
    ap.add_argument("--limit", type=int, default=0, help="cap #producers (0=all)")
    ap.add_argument("--no-push", action="store_true", help="commit but don't push")
    ap.add_argument("--skip", default="", help="comma-separated producer "
                    "scriptFiles to defer (e.g. slow heavy-atom producers)")
    ap.add_argument("--logfile", default="/tmp/q0_regen.log")
    args = ap.parse_args()
    skip = {s.strip() for s in args.skip.split(",") if s.strip()}

    logf = open(args.logfile, "a", buffering=1)

    def log(msg: str):
        line = f"[{time.strftime('%H:%M:%S')}] {msg}"
        print(line, flush=True)
        logf.write(line + "\n")

    by_script = scan_stale()
    total_stale = sum(len(v) for v in by_script.values())
    # High-yield producers first; skip the no-scriptFile bucket (manual).
    producers = sorted((s for s in by_script
                        if s != "<no-scriptFile>" and s not in skip),
                       key=lambda s: (-len(by_script[s]), s))
    no_script = by_script.get("<no-scriptFile>", [])

    log(f"=== q₀ regen batch — current q₀≈{CUR} ===")
    log(f"stale={total_stale}  producers={len(producers)}  "
        f"no_scriptFile(manual)={len(no_script)}")
    if args.plan:
        for s in producers:
            exists = (REPO / "folio-assistant" / "computations" / s).exists()
            log(f"  {len(by_script[s]):>3}  {s}  {'' if exists else '(MISSING)'}")
        for n in no_script:
            log(f"   ─  {n}  (no scriptFile — manual)")
        return 0

    if args.limit:
        producers = producers[: args.limit]
    done_w = 0
    done_p = 0
    skipped: list[str] = []
    t_start = time.time()

    for idx, script in enumerate(producers, 1):
        spath = REPO / "folio-assistant" / "computations" / script
        targets = by_script[script]
        if not spath.exists():
            log(f"[{idx}/{len(producers)}] SKIP missing {script}")
            skipped.append(f"{script} (missing)")
            continue
        # Clean slate: discard any residue from a prior timed-out run.
        git("checkout", "--", "folio-assistant/computations", check=False)
        t0 = time.time()
        try:
            r = subprocess.run([sys.executable, "-u", str(spath)], cwd=REPO,
                               capture_output=True, text=True,
                               timeout=args.timeout)
            rc = r.returncode
        except subprocess.TimeoutExpired:
            rc = -1
        dt = time.time() - t0
        if rc != 0:
            git("checkout", "--", "folio-assistant/computations", check=False)
            log(f"[{idx}/{len(producers)}] {'TIMEOUT' if rc==-1 else f'FAIL rc={rc}'}"
                f" {script} ({dt:.0f}s, {len(targets)} witnesses) — skipped")
            skipped.append(f"{script} ({'timeout' if rc==-1 else 'rc'+str(rc)})")
            continue
        # Verify the target witnesses are now FRESH; stage only those.
        fresh = []
        for rel in targets:
            wf = REPO / rel
            if wf.exists() and not stale_q0(wf.read_text()):
                fresh.append(rel)
        if not fresh:
            git("checkout", "--", "folio-assistant/computations", check=False)
            log(f"[{idx}/{len(producers)}] NOCHANGE {script} ({dt:.0f}s) — "
                f"witness still stale, skipped")
            skipped.append(f"{script} (no-fresh)")
            continue
        # Stage every witness this run touched (a producer may emit siblings),
        # but reset non-witness residue to keep the tree clean.
        git("add", *fresh)
        git("add", "folio-assistant/computations/*.witness.json", check=False)
        git("checkout", "--", "folio-assistant/computations", check=False)  # non-staged residue
        diff = git("diff", "--cached", "--name-only", check=False).stdout.split()
        n_committed = len(diff)
        git("commit", "-q", "-m",
            f"q0-regen: {script} ({n_committed} witnesses)", check=False)
        done_w += n_committed
        done_p += 1
        pushed = "(no-push)" if args.no_push else (
            "pushed" if push_with_retry(log) else "PUSH-FAILED")
        rate = done_w / max(time.time() - t_start, 1) * 60
        remaining = total_stale - done_w
        eta_min = remaining / max(rate, 0.1)
        log(f"[{idx}/{len(producers)}] OK {script} ({dt:.0f}s) "
            f"+{n_committed}w {pushed} | total {done_w}/{total_stale} "
            f"({rate:.1f}w/min, ETA {eta_min:.0f}min)")

    log(f"=== batch end: {done_p} producers, {done_w} witnesses committed; "
        f"{len(skipped)} skipped ===")
    if skipped:
        log("skipped (dedicated long-timeout pass): " + ", ".join(skipped[:40]))
    # Final residual scan.
    left = sum(len(v) for v in scan_stale().values())
    log(f"q₀-stale remaining: {left}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
