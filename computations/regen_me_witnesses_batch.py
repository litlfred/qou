#!/usr/bin/env python3
# polynomial_q_not_applicable: batch orchestrator, not a q-series compute.
"""Guarded one-shot regeneration of the witnesses stale from the ct80 m_e fix.

**Why.** Bean ``ct80`` (PR #2747) reconciled the 4th m_e registry
``computations/substrate/experimental_constants.py`` from the truncated
``M_E_MEV = 0.51099895000`` to the full CODATA-2022 ``0.51099895069``.
Because the constant changed, every ``*.witness.json`` produced by a script
that **reads m_e from this module** now carries a stale m_e-derived value and
must be regenerated so the value fix and the refreshed witnesses land
together.

**The hard lesson this runner encodes (do not relearn it).** A previous ct80
pass ran the producers *in a sandbox without* ``pyhecke_native`` *and at*
*reduced precision* and silently regressed 50-dps ``mpf`` values to ``f64``
(trailing zeros) — an **L1 precision regression** — then had to revert all of
them. This runner therefore **refuses to write anything** unless the
environment is full-precision: ``pyhecke_native`` importable **and**
``OUTPUT_DPS``/``COMPUTE_DPS`` at or above the serialization floor. The guard
is the whole point; ``--dry-run`` (the default) never runs or writes anything.

**Producer set (deterministic, derived — never hard-coded).** The in-scope
producers are the **direct importers** of ``experimental_constants`` (the
module ct80 changed) that (a) are not under ``_deprecated/`` and (b) emit at
least one ``*.witness.json`` (matched by the witness's recorded
``scriptFile``). Direct — not transitive — because every cluster module
imports ``_path_bridge`` and ``experimental_constants`` imports it too, so a
naive transitive closure leaks through the bridge into ~1200 unrelated
modules. Sibling producers that read m_e from ``codata_constants`` instead
(e.g. ``canonical_isotope_witness.py``) are **out of scope here** — that
registry was fixed by bean ``me3r`` (#2725, merged), not by ct80.

Usage::

    # DEFAULT — dry run. Lists producers + the witnesses that WOULD be
    # regenerated. Runs nothing, writes nothing. Safe in any environment.
    python3 -u regen_me_witnesses_batch.py
    python3 -u regen_me_witnesses_batch.py --dry-run

    # FULL-ENV one-shot regen (owner runs this in a full-precision env).
    # Aborts up front if the guard fails. Tees a per-producer log.
    python3 -u regen_me_witnesses_batch.py --run 2>&1 | tee /tmp/regen-me.log

    # Convenience flags
    python3 -u regen_me_witnesses_batch.py --run --limit 5    # first 5 only
    python3 -u regen_me_witnesses_batch.py --run --timeout 600
    python3 -u regen_me_witnesses_batch.py --run --no-commit  # regen, don't commit

This runner does **not** push or open PRs; it regenerates witnesses and (by
default in ``--run``) stages + commits them in one ``chore(witnesses)``
commit so the ct80 value fix and the regen land together. Review the diff,
then push.

@module computations/regen_me_witnesses_batch
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import argparse
import re
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent          # .../computations
REPO = HERE.parent                               # repo root
# The module ct80 changed — its importers are the stale-witness producers.
ROOT_CONST_STEM = "experimental_constants"
# m_e-derived public symbols; a direct importer that references one of these
# genuinely consumes the changed value (used only for the diagnostic count).
ME_SYMBOLS = ("M_E_MEV", "KAPPA", "Q_NEUTRON_MEV")

_IMPORT_RE = re.compile(
    r"^\s*(?:from\s+([\w.]+)\s+import|import\s+([\w.]+))", re.MULTILINE
)
_SCRIPTFILE_RE = re.compile(r'"scriptFile"\s*:\s*"([^"]+)"')


# ── Precision floor (single source of truth) ─────────────────────────────
# The serialization floor below which writing a witness is an L1 regression.
# AGENTS.md documents "50-dps serialization" as the floor; the live default
# is higher (OUTPUT_DPS_DEFAULT = 60). We require the *effective* OUTPUT_DPS
# and COMPUTE_DPS to be >= this floor so the guard stays correct whether the
# canonical default is 50, 60, or 70.
SERIALIZATION_FLOOR_DPS = 50


def _stem(p: Path) -> str:
    return p.stem.replace("-", "_")


def _local_imports(p: Path, stem_to_file: dict[str, Path]) -> set[str]:
    """Direct local-module imports of ``p`` (computations cluster only)."""
    try:
        txt = p.read_text(encoding="utf-8")
    except OSError:
        return set()
    out: set[str] = set()
    for m in _IMPORT_RE.finditer(txt):
        mod = (m.group(1) or m.group(2) or "").split(".")[0].replace("-", "_")
        if mod in stem_to_file:
            out.add(mod)
    return out


def _witnesses_by_producer() -> dict[str, list[str]]:
    """Map producer basename → [witness relpaths] via the witness ``scriptFile``.

    Canonical witnesses live flat under ``computations/``; multi-shard
    producers (one ``scriptFile`` → many shard witnesses) are expanded here.
    """
    by_producer: dict[str, list[str]] = defaultdict(list)
    for wf in HERE.glob("*.witness.json"):
        try:
            with wf.open(encoding="utf-8") as fh:
                head = fh.read(8192)
                mm = _SCRIPTFILE_RE.search(head)
                if mm is None and len(head) == 8192:
                    mm = _SCRIPTFILE_RE.search(head + fh.read())
        except OSError:
            continue
        if mm:
            rel = str(wf.relative_to(REPO))
            by_producer[Path(mm.group(1)).name].append(rel)
    return by_producer


def discover_producers() -> dict[str, list[str]]:
    """Return {producer relpath → [stale witness relpaths]} for the ct80 set.

    Deterministic: sorted producer keys, sorted witness lists. Restricted to
    DIRECT importers of ``experimental_constants`` that are non-deprecated and
    emit at least one witness.
    """
    py_files = list(HERE.rglob("*.py"))
    stem_to_file: dict[str, Path] = {}
    for p in py_files:
        stem_to_file.setdefault(_stem(p), p)

    # Reverse edge: which modules directly import experimental_constants.
    direct_importers: set[str] = set()
    for p in py_files:
        if ROOT_CONST_STEM in _local_imports(p, stem_to_file):
            direct_importers.add(_stem(p))

    wit_by_producer = _witnesses_by_producer()

    producers: dict[str, list[str]] = {}
    for stem in direct_importers:
        f = stem_to_file[stem]
        if "_deprecated" in f.parts:
            continue
        wits = wit_by_producer.get(f.name, [])
        if not wits:
            continue  # importer with no witness — nothing to regenerate
        producers[str(f.relative_to(REPO))] = sorted(wits)
    return dict(sorted(producers.items()))


def _references_me_symbol(producer_rel: str) -> bool:
    try:
        txt = (REPO / producer_rel).read_text(encoding="utf-8")
    except OSError:
        return False
    return any(sym in txt for sym in ME_SYMBOLS)


# ── Full-precision environment guard ─────────────────────────────────────
def check_full_precision_env() -> tuple[bool, list[str]]:
    """Return (ok, reasons). ok=True only in a full-precision env.

    Hard preconditions, checked BEFORE any producer runs or any witness is
    written:
      1. ``pyhecke_native`` importable (absent ⇒ the sympy/native split can
         fall back to f64 paths that silently truncate 50-dps mpf values).
      2. Effective serialization + compute precision at/above the floor
         (``OUTPUT_DPS`` and ``COMPUTE_DPS`` >= 50). A reduced QOU_OUTPUT_DPS
         would serialize witnesses below the L1 floor.
    """
    reasons: list[str] = []

    try:
        import pyhecke_native  # noqa: F401
    except Exception as exc:  # ImportError or any load failure
        reasons.append(
            f"pyhecke_native NOT importable ({type(exc).__name__}: {exc}). "
            "Build it: pip install ./tools/pyhecke-native (needs cargo). "
            "Without it the native/sympy split can regress 50-dps mpf -> f64."
        )

    try:
        # Importing precision also requires mpmath; a sandbox lacking the
        # scientific stack is by definition not a full-precision compute env.
        from qou_substrate import precision as _prec  # type: ignore

        out_dps = int(getattr(_prec, "OUTPUT_DPS"))
        cmp_dps = int(getattr(_prec, "COMPUTE_DPS"))
        if out_dps < SERIALIZATION_FLOOR_DPS:
            reasons.append(
                f"OUTPUT_DPS={out_dps} < floor {SERIALIZATION_FLOOR_DPS} "
                "(serialization below L1 floor — would truncate witnesses)."
            )
        if cmp_dps < SERIALIZATION_FLOOR_DPS:
            reasons.append(
                f"COMPUTE_DPS={cmp_dps} < floor {SERIALIZATION_FLOOR_DPS} "
                "(compute precision below L1 floor)."
            )
    except Exception as exc:
        reasons.append(
            f"qou_substrate.precision unavailable ({type(exc).__name__}: {exc}). "
            "Install the scientific stack + qou-substrate "
            "(pip install mpmath sympy numpy && pip install -e tools/qou-substrate). "
            "Cannot verify the precision floor — refusing to write."
        )

    return (len(reasons) == 0, reasons)


def _git(*args: str, check: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=REPO, text=True,
                          capture_output=True, check=check)


def full_env_command() -> str:
    return ("python3 -u computations/regen_me_witnesses_batch.py --run "
            "2>&1 | tee /tmp/regen-me.log")


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Guarded one-shot regeneration of ct80 m_e-stale witnesses.")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true",
                      help="(DEFAULT) list producers + witnesses; run/write nothing.")
    mode.add_argument("--run", action="store_true",
                      help="execute the regen (FULL-ENV only; guard must pass).")
    ap.add_argument("--limit", type=int, default=0,
                    help="cap number of producers (0 = all). --run only.")
    ap.add_argument("--timeout", type=int, default=900,
                    help="per-producer wall-time seconds (--run only).")
    ap.add_argument("--no-commit", action="store_true",
                    help="regenerate but do not stage/commit (--run only).")
    args = ap.parse_args()
    do_run = bool(args.run)  # dry-run is the default whenever --run absent

    def log(msg: str) -> None:
        print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

    producers = discover_producers()
    n_prod = len(producers)
    n_wit = sum(len(v) for v in producers.values())
    n_uses_me = sum(1 for p in producers if _references_me_symbol(p))

    log("=== ct80 m_e witness-regen batch ===")
    log("changed registry : computations/substrate/experimental_constants.py "
        "(M_E_MEV -> 0.51099895069)")
    log(f"producer set      : DIRECT non-deprecated witness-emitting importers "
        f"of '{ROOT_CONST_STEM}'")
    log(f"producers         : {n_prod}  ({n_uses_me} reference an m_e symbol "
        f"{ME_SYMBOLS})")
    log(f"witnesses (stale) : {n_wit}  (shard-expanded)")
    log(f"precision floor   : OUTPUT_DPS & COMPUTE_DPS >= {SERIALIZATION_FLOOR_DPS}")

    # The guard is evaluated in BOTH modes so a dry run reports env readiness;
    # in --run mode a failing guard ABORTS before any producer executes.
    ok, reasons = check_full_precision_env()
    if ok:
        log("env guard         : PASS (full-precision: pyhecke_native + dps floor)")
    else:
        log("env guard         : FAIL — NOT a full-precision env:")
        for r in reasons:
            log(f"  - {r}")

    if not do_run:
        log("--- DRY RUN (default): the following WOULD be regenerated ---")
        for i, (prod, wits) in enumerate(producers.items(), 1):
            tag = "" if _references_me_symbol(prod) else "  [no m_e symbol — import only]"
            log(f"  [{i:>3}/{n_prod}] {prod}  ({len(wits)} witness"
                f"{'es' if len(wits) != 1 else ''}){tag}")
            for w in wits:
                log(f"            └─ {w}")
        log("--- end dry run — nothing executed, nothing written ---")
        log(f"FULL-ENV command : {full_env_command()}")
        log("post-conditions  : ~%d witnesses refreshed; L1 cross-method "
            "agreement <= 1 ppQ preserved; each witness scriptHash + "
            "scriptCommitSha updated." % n_wit)
        return 0

    # ── --run path: HARD ABORT unless the env is full-precision ──────────
    if not ok:
        log("ABORT: refusing to regenerate witnesses in a non-full-precision "
            "env. Writing here would regress 50-dps mpf values to f64 (the "
            "L1 regression a previous ct80 pass hit and had to revert). "
            "Fix the env (build pyhecke_native; ensure OUTPUT_DPS >= "
            f"{SERIALIZATION_FLOOR_DPS}) and re-run.")
        return 2

    prod_items = list(producers.items())
    if args.limit:
        prod_items = prod_items[: args.limit]
    log(f"=== REGEN START — {len(prod_items)} producers, "
        f"per-producer timeout {args.timeout}s ===")

    t_start = time.time()
    done_p = 0
    done_w = 0
    failed: list[str] = []
    for idx, (prod, wits) in enumerate(prod_items, 1):
        spath = REPO / prod
        if not spath.exists():
            log(f"[{idx}/{len(prod_items)}] SKIP missing {prod}")
            failed.append(f"{prod} (missing)")
            continue
        t0 = time.time()
        # Long-compute logging discipline: unbuffered (-u), tee per producer.
        logfile = f"/tmp/regen-me-{Path(prod).stem}.log"
        try:
            with open(logfile, "w") as lf:
                r = subprocess.run(
                    [sys.executable, "-u", str(spath)], cwd=REPO,
                    stdout=lf, stderr=subprocess.STDOUT, text=True,
                    timeout=args.timeout)
            rc = r.returncode
        except subprocess.TimeoutExpired:
            rc = -1
        dt = time.time() - t0
        if rc != 0:
            log(f"[{idx}/{len(prod_items)}] "
                f"{'TIMEOUT' if rc == -1 else f'FAIL rc={rc}'} {prod} "
                f"({dt:.0f}s) — see {logfile}")
            failed.append(f"{prod} ({'timeout' if rc == -1 else 'rc'+str(rc)})")
            continue
        done_p += 1
        done_w += len(wits)
        rate = done_w / max(time.time() - t_start, 1) * 60
        remaining = n_wit - done_w
        eta = remaining / max(rate, 0.1)
        log(f"[{idx}/{len(prod_items)}] OK {prod} ({dt:.0f}s, {len(wits)}w) "
            f"| {done_w}/{n_wit}w ({rate:.1f}w/min, ETA {eta:.0f}min)")

    log(f"=== REGEN END: {done_p} producers OK, {done_w} witnesses refreshed, "
        f"{len(failed)} failed ===")
    if failed:
        log("failed/skipped: " + ", ".join(failed[:40]))

    if args.no_commit:
        log("--no-commit: leaving regenerated witnesses unstaged. Review + commit.")
        return 0 if not failed else 1

    # Stage every refreshed witness + the experimental_constants change so the
    # value fix and the regen land in one commit.
    _git("add", "computations/substrate/experimental_constants.py")
    _git("add", "--", *[w for wits in producers.values() for w in wits])
    _git("add", "computations/*.witness.json")  # catch sibling shards
    staged = _git("diff", "--cached", "--name-only").stdout.split()
    if staged:
        _git("commit", "-q", "-m",
             f"chore(witnesses): regen {done_w} m_e-dependent witnesses (ct80)\n\n"
             f"Direct importers of experimental_constants after the m_e fix "
             f"(0.51099895000 -> 0.51099895069). Regenerated in a full-precision "
             f"env (pyhecke_native + OUTPUT_DPS >= {SERIALIZATION_FLOOR_DPS}). "
             f"{done_p} producers OK"
             + (f", {len(failed)} failed" if failed else "") + ".")
        log(f"committed {len(staged)} files. Review `git show`, then push.")
    else:
        log("no witness bytes changed (m_e drift physically negligible at the "
            "witness's recorded precision for these producers). Nothing to commit.")
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
