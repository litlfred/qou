#!/usr/bin/env python3
"""q0_muon_reproduction_sweep.py — validate the muon-q₀ override (bean yfvb).

Re-runs each listed producer under the patched `q_parameter` (muon override) and
compares the freshly-emitted witness to its committed version **numerically**,
NOT byte-wise.  Rationale: two kinds of benign difference must be tolerated —

  1. provenance drift  (computedAt / commitSha / scriptHash / durationMs / …), and
  2. experimental-input precision drift — codata_constants now forces ≥50 dps
     (`_ame_binding_mev` → `mp.workdps(≥50)`), but the committed witnesses predate
     that upgrade, so their AME/CODATA inputs are stale f64.  Physically these agree
     to their ~8 experimental sig figs; only the serialized tail differs.

A field is a **substantive** difference (a real q₀ regression) iff its parsed
numeric value differs by more than `--rel-tol` (default 1e-10) relative — well
below the q₀ μ–p tension (~1.1e-8) it is meant to catch, well above experimental
tail noise.  Non-numeric string differences outside the provenance set are also
flagged.

Usage:
    python3 q0_muon_reproduction_sweep.py [--rel-tol 1e-10] <producer.py> [more.py …]

Each producer is run with the canonical muon override active (via the patched
q_parameter it imports); its witness is diffed against the committed HEAD version
and then restored with `git checkout --`.  Exit 0 iff every producer PASSes.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

# Canonical q₀ decimal signatures (CAL two-layer convention, AGENTS.md).
_MUON_SIG  = "1.109978595557"   # ideal / canonical 3-CAL (CAL-2 = 𝔇_β)
_PROTON_SIG = "1.10997858275"   # physical-observations (m_p/m_e)

HERE = Path(__file__).resolve().parent

_PROVENANCE = {
    "computedAt", "commitSha", "scriptCommitSha", "scriptHash", "durationMs",
    "engineVersion", "engine", "engine_version", "generatedAt", "timestamp",
    "scipy", "numpy", "mpmath", "python", "hostname", "wall_seconds",
    # tool/binding versions — added to witnesses after they were committed;
    # a version string appearing/changing is provenance, not a q₀ regression.
    "pyhecke_native", "pyhecke", "hecke_engine", "hecke-engine", "clarabel",
    "sympy", "snappy", "platform", "git_commit", "gitCommit",
}


def _num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _walk(a, b, path, rel_tol, out):
    """Collect substantive (path, a, b) differences between committed `a` and fresh `b`."""
    if isinstance(a, dict) and isinstance(b, dict):
        for k in set(a) | set(b):
            if k in _PROVENANCE:
                continue
            if k not in a or k not in b:
                out.append((f"{path}.{k}", a.get(k, "<missing>"), b.get(k, "<missing>")))
            else:
                _walk(a[k], b[k], f"{path}.{k}", rel_tol, out)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            out.append((f"{path}[len]", len(a), len(b)))
        for i, (x, y) in enumerate(zip(a, b)):
            _walk(x, y, f"{path}[{i}]", rel_tol, out)
    else:
        na, nb = _num(a), _num(b)
        if na is not None and nb is not None:
            denom = max(abs(na), abs(nb), 1e-300)
            if abs(na - nb) / denom > rel_tol:
                out.append((path, a, b))
        elif a != b:
            out.append((path, a, b))


def _committed(rel_path: str) -> str:
    return subprocess.run(
        ["git", "show", f"HEAD:{rel_path}"], cwd=HERE.parent,
        capture_output=True, text=True,
    ).stdout


def _witness_for(producer: Path) -> Path | None:
    """Best-effort: the producer's witness shares its stem with '-'/'_' swapped."""
    stem = producer.stem
    for cand in (stem.replace("_", "-"), stem):
        for w in HERE.glob(f"{cand}.witness.json"):
            return w
    return None


def run_one(producer: Path, rel_tol: float, timeout: int = 1800) -> tuple[str, list]:
    wit = _witness_for(producer)
    if wit is None:
        return ("NO_WITNESS", [])
    rel = str(wit.relative_to(HERE.parent))
    committed_txt = _committed(rel)
    if not committed_txt:
        return ("NO_COMMITTED", [])
    committed = json.loads(committed_txt)

    # Order the CAL-layer anchors to try by the committed witness's own q₀
    # signature (muon ⇒ ideal, proton ⇒ physical); when absent/ambiguous, try
    # both and keep whichever REPRODUCES — this auto-classifies every producer.
    order = [("muon", "ideal"), ("proton", "physical")]
    if _PROTON_SIG in committed_txt and _MUON_SIG not in committed_txt:
        order = [("proton", "physical"), ("muon", "ideal")]

    best = None  # (n_diffs, anchor, diffs)
    # Defensive PYTHONPATH: most producers self-bootstrap substrate/ onto
    # sys.path, but a handful `from _precision import …` without it and fail
    # standalone. Inject computations/ + computations/substrate/ so every
    # producer resolves its bare-name substrate imports.
    _pp = f"{HERE}{os.pathsep}{HERE / 'substrate'}"
    for anchor, envval in order:
        env = dict(os.environ); env["QOU_Q0_ANCHOR"] = envval
        env["PYTHONPATH"] = _pp + ((os.pathsep + env["PYTHONPATH"]) if env.get("PYTHONPATH") else "")
        r = subprocess.run([sys.executable, "-u", producer.name], cwd=HERE,
                           capture_output=True, text=True, timeout=timeout, env=env)
        try:
            if r.returncode != 0:
                return (f"RUN_FAILED (exit {r.returncode}): {r.stderr.strip()[-160:]}", [])
            fresh = json.loads(wit.read_text())
        finally:
            subprocess.run(["git", "checkout", "--", rel], cwd=HERE.parent, capture_output=True)
        diffs: list = []
        _walk(committed, fresh, producer.stem, rel_tol, diffs)
        if not diffs:
            return (f"PASS [{anchor}]", [])
        if best is None or len(diffs) < best[0]:
            best = (len(diffs), anchor, diffs)
    return (f"SUBSTANTIVE [{best[1]} best] ({best[0]})", best[2])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rel-tol", type=float, default=1e-10)
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--all-manifest", action="store_true")
    ap.add_argument("producers", nargs="*")
    args = ap.parse_args()

    producers = list(args.producers)
    if args.all_manifest:
        man = json.loads((HERE / "q0_anchor_manifest.json").read_text())
        producers = [f"{st}.py" for st in man["ideal_muon"] + man["physical_proton"]]

    overall_ok = True
    npass = nsub = nother = 0
    for p in producers:
        prod = (HERE / p) if not Path(p).is_absolute() else Path(p)
        try:
            status, diffs = run_one(prod, args.rel_tol, args.timeout)
        except subprocess.TimeoutExpired:
            status, diffs = ("TIMEOUT (>1800s)", [])
        mark = "✓" if status.startswith("PASS") else ("–" if status in ("NO_WITNESS", "NO_COMMITTED") else "✗")
        print(f"{mark} {prod.name}: {status}")
        for path, a, b in diffs[:6]:
            print(f"      {path}: committed={str(a)[:32]} fresh={str(b)[:32]}")
        if status.startswith("PASS"):
            npass += 1
        elif status in ("NO_WITNESS", "NO_COMMITTED"):
            pass
        else:
            nother += 1; overall_ok = False
    print(f"\n=== {npass} PASS, {nother} SUBSTANTIVE/FAILED of {len(producers)} ===")
    return 0 if overall_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
