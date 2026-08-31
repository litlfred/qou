#!/usr/bin/env python3
"""witness_upstream_staleness_audit — is any witness OLDER than a witness it READS?

The existing staleness tools are each scoped to one CAUSE:

    codata_2022_downstream_staleness_scan.py   a constants change
    mpmath_version_staleness_probe.py          an engine version change
    q0_muon_witness_staleness_triage.py        an anchor change
    stale_probe_audit.py                       probe-specific

None asks the cause-free question this one does, and that is how a real defect
went unnoticed for six days (bean `qou-4idm`):

    low_isotope_binding_model_comparison.py does not COMPUTE B_depth. It reads
    it from binding-depth-stratified.witness.json. That upstream was
    regenerated 2026-08-29 and holds D: B_MeV = 0.709992911...; the consumer's
    witness dated from 2026-08-23 and still published 0.606879 -- 17% wrong,
    with allPassed: true. Nothing flagged it. It surfaced only because an
    unrelated edit happened to re-run the producer.

A producer that reads a witness has a DEPENDENCY on it. If the upstream has
been regenerated since the consumer last was, the consumer is publishing
numbers derived from inputs that no longer exist. This audit finds exactly that,
for every cause at once -- including causes nobody has thought of yet.

ORDERING IS BY COMMIT DATE, NOT mtime. A fresh clone gives every file the same
mtime, so an mtime comparison silently reports nothing in exactly the
environment where this runs.

Usage:
    python3 computations/audits/witness_upstream_staleness_audit.py [--strict] [--limit N]
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent

WITNESS_RE = re.compile(r"""["']([A-Za-z0-9._/\-]+\.witness\.json)["']""")
BUILDER_RE = re.compile(r"""WitnessBuilder(?:\.wrap_legacy)?\(\s*["']([a-z0-9\-_]+)["']""")
SKIP_PARTS = ("_deprecated", "__pycache__", ".git", "node_modules")


def _witness_commit_times() -> dict[str, int]:
    """{repo-relative witness path: unix time of the commit that last changed it}.

    One `git log` pass over the whole history, newest first; the first sighting
    of a path is the commit that last touched it.
    """
    out = subprocess.run(
        ["git", "log", "--format=C|%H|%ct", "--name-only", "--", "*.witness.json"],
        cwd=_ROOT, capture_output=True, text=True, check=True).stdout
    times: dict[str, int] = {}
    ts = 0
    for line in out.split("\n"):
        if line.startswith("C|"):
            ts = int(line.rsplit("|", 1)[1])
        elif line.strip() and line not in times:
            times[line.strip()] = ts
    return times


def _index_producers() -> dict[str, dict]:
    """{producer path: {'own': witness-or-None, 'reads': [witness, ...]}}"""
    found: dict[str, dict] = {}
    for dirpath, _dn, filenames in os.walk(_ROOT / "computations"):
        if any(p in dirpath for p in SKIP_PARTS):
            continue
        for fn in sorted(filenames):
            if not fn.endswith(".py"):
                continue
            path = Path(dirpath) / fn
            try:
                src = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            refs = {m.group(1) for m in WITNESS_RE.finditer(src)}
            if not refs:
                continue
            own = None
            m = BUILDER_RE.search(src)
            if m:
                cand = f"{m.group(1)}.witness.json"
                own = next((r for r in refs if r.endswith(cand)), cand)
            rel = str(path.relative_to(_ROOT))
            found[rel] = {
                "own": own,
                "reads": sorted(r for r in refs if r != own),
                "dir": str(path.parent.relative_to(_ROOT)),
            }
    return found


def _resolve(ref: str, prod_dir: str, times: dict[str, int]) -> str | None:
    """Map a bare witness reference onto a real repo path."""
    if ref in times:
        return ref
    cand = os.path.normpath(os.path.join(prod_dir, ref))
    if cand in times:
        return cand
    base = os.path.basename(ref)
    matches = [p for p in times if os.path.basename(p) == base]
    return matches[0] if len(matches) == 1 else None


def main() -> int:
    t0 = time.monotonic()
    strict = "--strict" in sys.argv
    limit = 40
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])

    times = _witness_commit_times()
    producers = _index_producers()

    print("=" * 78)
    print(" Witness upstream staleness — is a witness older than one it READS?")
    print("=" * 78)
    print(f"  witnesses with a commit date : {len(times)}")
    print(f"  producers referencing one    : {len(producers)}")

    stale = []
    for prod, info in producers.items():
        own = info["own"]
        if not own:
            continue
        own_p = _resolve(own, info["dir"], times)
        if own_p is None:
            continue
        own_t = times[own_p]
        for ref in info["reads"]:
            up = _resolve(ref, info["dir"], times)
            if up is None or up == own_p:
                continue
            if times[up] > own_t:
                stale.append((times[up] - own_t, prod, own_p, up))

    stale.sort(reverse=True)
    print(f"\n  STALE consumers (own witness older than an upstream): {len(stale)}")
    print(f"  {'behind':>10}  consumer witness  <-  upstream")
    for delta, prod, own_p, up in stale[:limit]:
        days = delta / 86400.0
        print(f"  {days:9.1f}d  {os.path.basename(own_p)}")
        print(f"              <- {os.path.basename(up)}")
    if len(stale) > limit:
        print(f"  ... and {len(stale) - limit} more (use --limit)")

    print(f"\n  elapsed: {time.monotonic() - t0:.1f}s")
    if strict and stale:
        print("\nFAIL (--strict): stale consumers found.")
        print("  Re-run the consumer producer; its inputs changed after it last ran.")
        return 1
    if strict:
        print("\nPASS (--strict): no consumer is older than an upstream it reads.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
