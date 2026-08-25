#!/usr/bin/env python3
# polynomial_q_not_applicable: infra audit; no symbolic-q logic.
"""Can each committed witness's producer still produce it? (coverage-complete)

Every `*.witness.json` in the tree names the script that wrote it. Nothing
checks that the named script still **exists**, still **parses**, or still
**runs**. This audit does.

Why this exists
---------------

On 2026-08-10 `probe_kappa_shell8_excess_convention.py` was drained off the
raw-float64 ratchet by making its constants `mpmath.mpf`. That turned an
untouched line, `print(f"{k:.7f}")`, into a hard error — `mpf` has no
`__format__` — and the script raises **before** its `json.dump`. So the
committed witness could not have been the output of the committed script, and
every gate in the NO-FLOAT64 family passed it, because:

    the ratchets read witnesses; they never run producers.

"Drained" and "reproducible" are independent properties and only the first was
gated. Same shape as the stale-audit class recorded in PR #4929 — *an audit
whose own witness is not regenerated reports yesterday's answer with today's
authority* — one level down: a producer that can no longer speak for its own
witness.

Relationship to `witness_reproducibility_check.py`
--------------------------------------------------

That checker (P32) is the **byte-equality** gate for `*.derivation.json`
builders, over an **explicit registry** of ~13 entries. It is deliberately
opt-in, and its docstring explains why: builders with CLI args cannot be
auto-discovered safely.

This audit is the complement on both axes:

* it covers `*.witness.json`, not `*.derivation.json`;
* it is **auto-discovered**, so coverage is total by construction — the
  question "is this producer checked?" cannot be answered "nobody added it
  to the registry".

The two do not overlap; neither subsumes the other.

Passes
------

**Static** (default; free, whole corpus). Per witness:

    OK                     producer resolves and compiles
    NO_PRODUCER_FIELD      witness names no producer at all
    PRODUCER_NOT_FOUND     names one that is not in the tree
    SYNTAX_ERROR           names one that does not parse

**Smoke** (`--smoke`; bounded, executes producers). Per witness, additionally:

    REPRODUCES / DIFFERS   producer exits 0 (see below)
    CRASHED                producer exits non-zero  <-- the kappa class
    ENV_MISSING            ModuleNotFoundError / ImportError: this RUNNER
                           lacks a dependency. Never a defect, never blocking
    TIMEOUT                exceeded --timeout (recorded, NOT a failure: an
                           expensive producer is not a broken one)

and, when it runs and rewrites its own witness:

    REPRODUCES             regenerated == committed, modulo ephemeral fields
    DIFFERS                regenerated != committed  <-- committed value is
                           not what the producer now emits

The committed witness is **restored from git** after every smoke run, so the
audit never leaves the tree dirty.

Ephemeral fields are excluded from the DIFFERS comparison for the same reason
`witness_dependency_drift.py` excludes them: they move on every run by design.
`scriptCommitSha` is among them — per AGENTS.md it is stale-on-arrival under
rebase-merge and is informational provenance only.

Usage
-----

    python3 computations/witness_producer_executes_audit.py
    python3 computations/witness_producer_executes_audit.py --strict
    python3 computations/witness_producer_executes_audit.py --smoke --timeout 60
    python3 computations/witness_producer_executes_audit.py --smoke --only kappa
    python3 computations/witness_producer_executes_audit.py --list

`--strict` exits 1 on PRODUCER_NOT_FOUND, SYNTAX_ERROR or CRASHED. It does not
fail on TIMEOUT (cost, not breakage) or on NO_PRODUCER_FIELD (a backlog, sized
by the run and drained separately).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge
import argparse
import json
import py_compile
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# Moves on every run by design; never a reproducibility failure.
EPHEMERAL = {
    "computedAt", "computed_at", "timestamp", "durationMs", "duration_ms",
    "elapsed_sec", "elapsed", "wall_sec", "runtime_sec",
    "commitSha", "scriptCommitSha", "gitCommit", "git_commit",
    "scriptHash", "engineVersion", "engine_version", "environment",
    "python", "mpmath", "numpy", "sympy", "platform",
}

# An audit's own output: re-running it is what the caller is already doing.
SELF_AUDIT_SUFFIXES = (
    "-audit.witness.json",
    "witness-raw-float64-audit.witness.json",
    "witness-float64-padding-audit.witness.json",
    "witness-producer-executes-audit.witness.json",
)


def producer_of(body: dict) -> str | None:
    """The script a witness says wrote it, under any of the three spellings."""
    for key in ("scriptFile", "producer", "script"):
        v = body.get(key)
        if isinstance(v, str) and v.strip():
            return v.strip()
    comp = body.get("computation")
    if isinstance(comp, dict):
        v = comp.get("script")
        if isinstance(v, str) and v.strip():
            return v.strip()
    return None


def is_prose(ref: str) -> bool:
    """True when the producer field holds an explanation, not a path.

    Several witnesses carry things like "(legacy — no matching producer found;
    provenance pending manual triage)" in `scriptFile`. That is a real finding
    — the witness cannot say what wrote it — but it is a different finding from
    "the named script is missing", and conflating them would put prose in a
    list of paths.
    """
    if ref.startswith("(") or len(ref) > 120:
        return True
    return "/" not in ref and Path(ref).suffix == "" and " " in ref


def resolve(ref: str) -> Path | None:
    """Resolve a producer reference to a file, trying the usual spellings.

    Searches the whole repo, not just `computations/`: producers are also
    Rust (`tools/hecke-engine/**/*.rs`) and Lean (`content/**/*.lean`).
    """
    ref = ref.strip().lstrip("./")
    for cand in (ROOT / ref, HERE / ref, HERE / Path(ref).name):
        if cand.is_file():
            return cand
    name = Path(ref).name
    # A `_deprecated/` copy is by definition NOT the producer, but it counts
    # toward the uniqueness test below, so a live producer with a retired twin
    # resolved to None. Measured: `rho_k_markov_multiplicativity_probe.py`
    # exists at BOTH computations/probes/ and computations/_deprecated/, and
    # the witness sitting next to the live one was reported producerless --
    # which is how a content block citing it as PROVED came to look like it
    # rested on nothing. Every other scan in this repo already skips
    # `_deprecated`; this one did not.
    hits = [p for p in HERE.rglob(name)
            if p.is_file() and "_deprecated" not in p.parts]
    if len(hits) == 1:
        return hits[0]
    if not hits:
        # Widen to the repo for non-Python producers, skipping build output.
        # `.claude/worktrees/<agent>/` holds checkouts of OTHER branches, so a
        # repo-wide rglob returns the real producer PLUS one copy per stale
        # worktree. The `len(wide) == 1` guard below then rejects the match as
        # ambiguous and the producer resolves to None -- i.e. a producer that
        # plainly exists is reported missing. Measured: `joint_tower_sdp.rs`
        # returned 6 hits, 1 real and 5 from worktrees.
        wide = [p for p in ROOT.rglob(name)
                if p.is_file() and not any(
                    part in (".git", ".claude", ".lake", "node_modules",
                             "target", "__pycache__", "_deprecated")
                    for part in p.parts)]
        if len(wide) == 1:
            return wide[0]
    return None


def strip_ephemeral(obj):
    """Deep-copy with ephemeral keys removed, for the DIFFERS comparison."""
    if isinstance(obj, dict):
        return {k: strip_ephemeral(v) for k, v in obj.items()
                if k not in EPHEMERAL}
    if isinstance(obj, list):
        return [strip_ephemeral(v) for v in obj]
    return obj


def witnesses() -> list[Path]:
    out = []
    for p in sorted(HERE.rglob("*.witness.json")):
        if "_deprecated" in p.parts or "__pycache__" in p.parts:
            continue
        if any(p.name.endswith(s) for s in SELF_AUDIT_SUFFIXES):
            continue
        out.append(p)
    return out


def static_verdict(wpath: Path) -> tuple[str, str, Path | None]:
    try:
        body = json.loads(wpath.read_text())
    except (json.JSONDecodeError, OSError) as exc:
        return "PARSE_ERROR", str(exc)[:120], None
    if not isinstance(body, dict):
        return "PARSE_ERROR", "root is not an object", None
    ref = producer_of(body)
    if not ref:
        return "NO_PRODUCER_FIELD", "", None
    if is_prose(ref):
        return "PRODUCER_FIELD_IS_PROSE", ref, None
    path = resolve(ref)
    if path is None:
        return "PRODUCER_NOT_FOUND", ref, None
    if path.suffix != ".py":
        # Rust and Lean producers are legitimate; this audit can locate them
        # but cannot compile or run them, so it says so rather than guessing.
        return "NON_PYTHON_PRODUCER", path.suffix, path
    try:
        py_compile.compile(str(path), cfile=tempfile.mktemp(), doraise=True)
    except py_compile.PyCompileError as exc:
        return "SYNTAX_ERROR", str(exc).splitlines()[-1][:160], path
    return "OK", ref, path


def smoke(wpath: Path, ppath: Path, timeout: int) -> tuple[str, str]:
    """Run the producer; classify; restore the witness from git afterwards."""
    before = wpath.read_bytes()
    try:
        # Repo root first: producers written with `open("computations/…")`
        # need it, and those using `Path(__file__)` are cwd-independent.
        proc = subprocess.run(
            [sys.executable, str(ppath)], cwd=str(ROOT),
            capture_output=True, text=True, timeout=timeout,
        )
        if proc.returncode != 0 and "No such file or directory" in proc.stderr:
            proc = subprocess.run(
                [sys.executable, str(ppath)], cwd=str(HERE),
                capture_output=True, text=True, timeout=timeout,
            )
    except subprocess.TimeoutExpired:
        _restore(wpath, before)
        return "TIMEOUT", f">{timeout}s"
    except OSError as exc:
        _restore(wpath, before)
        return "CRASHED", str(exc)[:160]

    if proc.returncode != 0:
        tail = (proc.stderr.strip().splitlines() or [""])[-1]
        _restore(wpath, before)
        # A missing dependency says the RUNNER is under-provisioned, not that
        # the producer is broken. Never let that be reported as a defect —
        # a checker that cries wolf on its own environment gets ignored.
        if "ModuleNotFoundError" in tail or "ImportError" in tail:
            return "ENV_MISSING", tail[:200]
        return "CRASHED", tail[:200]

    after = wpath.read_bytes()
    _restore(wpath, before)
    if after == before:
        return "REPRODUCES", "byte-equal"
    try:
        a, b = json.loads(after), json.loads(before)
    except json.JSONDecodeError:
        return "DIFFERS", "regenerated output is not valid JSON"
    if strip_ephemeral(a) == strip_ephemeral(b):
        return "REPRODUCES", "equal modulo ephemeral fields"
    return "DIFFERS", "substantive fields changed"


def _restore(wpath: Path, before: bytes) -> None:
    if wpath.read_bytes() != before:
        wpath.write_bytes(before)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--smoke", action="store_true",
                    help="execute producers (bounded); default is static only")
    ap.add_argument("--timeout", type=int, default=90,
                    help="per-producer seconds in --smoke (default 90)")
    ap.add_argument("--limit", type=int, default=0,
                    help="cap how many producers --smoke executes (0 = all)")
    ap.add_argument("--only", default="",
                    help="substring filter on the witness filename")
    ap.add_argument("--list", action="store_true",
                    help="print every non-OK verdict, not just a sample")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on PRODUCER_NOT_FOUND / SYNTAX_ERROR / CRASHED")
    args = ap.parse_args(argv)

    rows: list[dict] = []
    todo = [w for w in witnesses() if args.only in w.name]

    for w in todo:
        verdict, detail, ppath = static_verdict(w)
        rows.append({
            "witness": str(w.relative_to(ROOT)),
            "producer": str(ppath.relative_to(ROOT)) if ppath else detail,
            "static": verdict,
            "detail": detail if verdict != "OK" else "",
        })

    ran = 0
    if args.smoke:
        for row in rows:
            if row["static"] != "OK":
                continue
            if args.limit and ran >= args.limit:
                row["smoke"] = "NOT_RUN"
                continue
            ran += 1
            wpath = ROOT / row["witness"]
            ppath = ROOT / row["producer"]
            row["smoke"], row["smoke_detail"] = smoke(wpath, ppath, args.timeout)

    print("=" * 74)
    print("WITNESS PRODUCER EXECUTES AUDIT — can the script still write it?")
    print("=" * 74)
    tally: dict[str, int] = {}
    for r in rows:
        tally[r["static"]] = tally.get(r["static"], 0) + 1
    print(f"  witnesses examined : {len(rows)}")
    for k in ("OK", "NON_PYTHON_PRODUCER", "NO_PRODUCER_FIELD",
              "PRODUCER_FIELD_IS_PROSE", "PRODUCER_NOT_FOUND",
              "SYNTAX_ERROR", "PARSE_ERROR"):
        if tally.get(k):
            print(f"    {k:<20s} {tally[k]:5d}")

    hard = [r for r in rows
            if r["static"] in ("PRODUCER_NOT_FOUND", "SYNTAX_ERROR",
                               "PARSE_ERROR")]
    if hard:
        print("\n  BROKEN — the witness names a producer that is missing or "
              "does not parse:")
        for r in (hard if args.list else hard[:20]):
            print(f"    [{r['static']}] {r['witness']}")
            print(f"        {r['detail']}")
        if not args.list and len(hard) > 20:
            print(f"    ... and {len(hard) - 20} more (--list)")

    smoke_tally: dict[str, int] = {}
    crashed = []
    if args.smoke:
        for r in rows:
            v = r.get("smoke")
            if not v or v == "NOT_RUN":
                continue
            smoke_tally[v] = smoke_tally.get(v, 0) + 1
            if v in ("CRASHED", "DIFFERS"):
                crashed.append(r)
        print(f"\n  producers executed : {ran}  (timeout {args.timeout}s)")
        for k in ("REPRODUCES", "DIFFERS", "CRASHED", "ENV_MISSING",
                  "TIMEOUT"):
            if smoke_tally.get(k):
                print(f"    {k:<20s} {smoke_tally[k]:5d}")
        if crashed:
            print("\n  A witness its producer can no longer write:")
            for r in (crashed if args.list else crashed[:20]):
                print(f"    [{r['smoke']}] {r['witness']}")
                print(f"        {r['producer']}: {r.get('smoke_detail','')}")
            if not args.list and len(crashed) > 20:
                print(f"    ... and {len(crashed) - 20} more (--list)")

    out = HERE / "witness-producer-executes-audit.witness.json"
    out.write_text(json.dumps({
        "engine": "python-stdlib",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "witness-producer-executes-audit",
        "scriptFile": "witness_producer_executes_audit.py",
        "description": (
            "Coverage-complete check that every *.witness.json names a "
            "producer that exists, parses, and (with --smoke) still runs and "
            "still emits the committed values. Complements the registry-based "
            "byte-equality check for *.derivation.json builders."
        ),
        "mode": "smoke" if args.smoke else "static",
        "timeout_sec": args.timeout if args.smoke else None,
        "static_tally": tally,
        "smoke_tally": smoke_tally or None,
        "producers_executed": ran if args.smoke else 0,
        "rows": rows,
    }, indent=2) + "\n")
    print(f"\n  witness -> {out.name}")

    if args.strict:
        blocking = len(hard) + smoke_tally.get("CRASHED", 0)
        if blocking:
            print(f"\nSTRICT: {blocking} blocking finding(s) — exiting 1")
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
