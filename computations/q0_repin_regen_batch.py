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
REPO = HERE.parent
for p in (str(HERE), str(REPO / "tools" / "qou-substrate" / "python")):
    if p not in sys.path:
        sys.path.insert(0, p)

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402
from q0_migration_tolerance_triage import (  # noqa: E402
    carries_the_anchor,
    is_discrete,
    slack_of,
    ANCHOR_IMPACT,
    AT_RISK,
)

#: Producers DECLARED to run at the ideal (muon) anchor, from
#: `computations/q0_anchor_manifest.json`. These are not unmigrated leftovers
#: -- they are the canonical 3-CAL layer, where CAL-2 is 𝔇_β with proxy
#: m_mu/m_e, so muon is correct there BY DEFINITION. Sweeping one does not
#: migrate a stale witness; it moves a canonical-chain artifact off the layer
#: it is declared to live on.
#:
#: The μ-p tension (11.54 ppb; 9.5 sigma on m_mu) is only measurable because
#: both pins exist. Collapsing the ideal layer into the experimental one does
#: not tidy the corpus, it deletes the comparison.
#:
#: Measured 2026-08-19: of 576 muon-anchored witnesses, 219 come from a
#: declared ideal_muon producer and 357 do not. The 357 are the migration.
def _declared_ideal_muon() -> set[str]:
    try:
        man = json.loads((REPO / "computations" / "q0_anchor_manifest.json").read_text())
    except Exception:
        return set()
    return set(man.get("ideal_muon") or [])


#: Producers that must NEVER be swept, with the reason.
#:
#: `q_pinning_50_digit` writes `q-pinning-50-digit.witness.json`, which is not
#: a datum -- it is what `qou_substrate.witness._q0_value_for_anchor` reads as
#: THE DEFINITION of the muon pin. Regenerating it at the proton pin therefore
#: does not migrate a witness, it deletes the muon anchor: both anchors then
#: resolve to the same value and every muon-anchored witness reports a flip.
#:
#: That is not hypothetical. It happened -- commit 9a9c6b31c ("first 25
#: witnesses regenerated at the proton pin") produced 262 Q0_FLIPs and had to
#: be reverted by 2e4745448d. Beans `qou-m9xp`, `qou-cezp`, `qou-1c4y`.
NEVER_SWEEP = {
    "q_pinning_50_digit.py":
        "defines the muon pin that _q0_value_for_anchor reads; sweeping it "
        "deletes the anchor (262 Q0_FLIPs, 9a9c6b31c -> reverted 2e4745448d)",
}

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
WGLOB = "computations/*.witness.json"
BRANCH = "claude/q0-repin-regen-batch-2026-05-30"


def at_risk_count(witness_relpaths: list[str]) -> int:
    """Assertions in these witnesses whose margin cannot absorb the anchor move.

    Reuses `q0_migration_tolerance_triage` rather than re-deriving the test --
    that module already separates the three classes that LOOK like zero margin
    and are not (counts, threshold semantics, real-valued exacts). Wiring it in
    here is the point: the triage merged on 2026-08-15 and, measured four days
    later, was referenced by nothing but its own test. A triage nothing calls
    does not order anything.
    """
    n = 0
    for rel in witness_relpaths:
        try:
            doc = json.loads((REPO / rel).read_text())
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue
        for a in doc.get("assertions") or []:
            if not isinstance(a, dict) or is_discrete(a) or a.get("passed") is False:
                continue
            sl = slack_of(a)
            if sl is None or sl < 0:
                continue
            if carries_the_anchor(a) or sl < AT_RISK * ANCHOR_IMPACT:
                n += 1
    return n


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
    ap.add_argument("--include-declared-ideal", action="store_true",
                    help="also sweep producers DECLARED ideal_muon in "
                         "q0_anchor_manifest.json (default: exclude — they "
                         "are on their correct layer by declaration; "
                         "re-declaring one is an owner call)")
    ap.add_argument("--include-at-risk", action="store_true",
                    help="also sweep producers whose witnesses carry "
                         "assertions too tight to absorb the ~1e-7 anchor "
                         "move (default: defer them, listed at the end)")
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

    # Never-sweep list: these are DEFINITIONS, not data. See NEVER_SWEEP.
    blocked = [s for s in producers if Path(s).name in NEVER_SWEEP]
    producers = [s for s in producers if Path(s).name not in NEVER_SWEEP]

    # Manifest gate. Declared ideal-layer producers are on their correct
    # anchor already; the migration targets the UNDECLARED remainder.
    ideal = _declared_ideal_muon()
    declared = [s for s in producers if Path(s).stem in ideal]
    if not args.include_declared_ideal:
        producers = [s for s in producers if Path(s).stem not in ideal]

    # Risk gate. A producer whose witnesses carry assertions with no margin
    # left is deferred by default rather than swept blind: those failures are
    # FINDINGS and are worth reading one at a time, not discovering in the
    # middle of a 25-producer batch where they are indistinguishable from a
    # real regression.
    risk = {s: at_risk_count(by_script[s]) for s in producers}
    at_risk = [s for s in producers if risk[s]]
    if not args.include_at_risk:
        producers = [s for s in producers if not risk[s]]

    log(f"=== q₀ regen batch — current q₀≈{CUR} ===")
    log(f"stale={total_stale}  producers={len(producers)}  "
        f"no_scriptFile(manual)={len(no_script)}")
    for s in blocked:
        log(f"  BLOCKED  {s} — {NEVER_SWEEP[Path(s).name]}")
    if declared:
        verb = "INCLUDED" if args.include_declared_ideal else "EXCLUDED"
        log(f"  {len(declared)} producer(s) DECLARED ideal_muon in the "
            f"manifest ({verb}; muon is correct there by declaration):")
        for s in sorted(declared):
            log(f"    ideal-layer  {s}")
    if at_risk:
        verb = "INCLUDED" if args.include_at_risk else "DEFERRED"
        log(f"  {len(at_risk)} producer(s) carry at-risk assertions "
            f"({verb}; --include-at-risk to sweep them):")
        for s in sorted(at_risk, key=lambda s: (-risk[s], s)):
            log(f"    {risk[s]:>3} at-risk  {s}")

    if args.plan:
        for s in producers:
            exists = (REPO / "computations" / s).exists()
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
        spath = REPO / "computations" / script
        targets = by_script[script]
        if not spath.exists():
            log(f"[{idx}/{len(producers)}] SKIP missing {script}")
            skipped.append(f"{script} (missing)")
            continue
        # Clean slate: discard any residue from a prior timed-out run.
        git("checkout", "--", "computations", check=False)
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
            git("checkout", "--", "computations", check=False)
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
            git("checkout", "--", "computations", check=False)
            log(f"[{idx}/{len(producers)}] NOCHANGE {script} ({dt:.0f}s) — "
                f"witness still stale, skipped")
            skipped.append(f"{script} (no-fresh)")
            continue
        # Stage every witness this run touched (a producer may emit siblings),
        # but reset non-witness residue to keep the tree clean.
        git("add", *fresh)
        git("add", "computations/*.witness.json", check=False)
        git("checkout", "--", "computations", check=False)  # non-staged residue
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
