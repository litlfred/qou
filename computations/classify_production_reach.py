#!/usr/bin/env python3
"""Does a producer reach production? — the f64-tier decision, made checkable.

## Why this exists

Owner ruling 2026-08-15: *"mpmath on anything in production; if not, deprecate
it with `precision_tier = float64`."* That makes "is this production?" a
question with a consequence, asked once per float64-carrying producer — and the
q₀ re-pin sweep is surfacing them in bulk, because resurrecting a producer that
had quietly stopped running puts its float64 into the ratchet.

Answering it by eye, dozens of times, is how a wrong call gets made and then
inherited. `local/production-vs-exploratory-discipline` already defines the
answer as a decision tree over named locations; this walks that tree
mechanically so the verdict is reproducible and its evidence is printed rather
than asserted.

## What it does NOT do

It does not decide. A `NOT-PRODUCTION` verdict here is *necessary* evidence for
the deprecate-with-tier route, not sufficient authority for it — the skill's
tree also asks whether the code changes a cheat-sheet "closed" status or a
`LAMBDA_*` / `ALPHA_*` / `Q_*` constant, which is a judgement about intent that
no reachability walk can make. Read the printed evidence; do not paste the
verdict into a witness unread.

Usage:
    python3 classify_production_reach.py atom_level_wedderburn_tower [more...]
    python3 classify_production_reach.py --all-dirty     # every f64-red producer
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# The production locations named by
# `.claude/skills/local/production-vs-exploratory-discipline.md` §decision tree,
# plus the two canonical facades AGENTS.md routes absolute mass and binding
# through. Kept as a literal list, not inferred: the skill is the authority, and
# a list that drifts from it silently is worse than no list.
PRODUCTION_STEMS = {
    "m_p_borromean_verification_50dps",
    "mass_table_ppb",
    "codata_constants",
    "per_observable_100x_status",
    "onepb_status_dashboard",
    "canonical_mass",
    "binding_canonical",
    "canonical_mass_table_extended",
}

# Constants whose definition site is production regardless of who reads it.
PRODUCTION_CONST = re.compile(r"\b(LAMBDA_[A-Z_]+|ALPHA_[A-Z_]+|Q_[A-Z0-9_]+)\s*=")


class _SearchHealth:
    """Records whether the reachability searches actually ran.

    `_rg` returned an empty set both when a pattern genuinely matched nothing
    and when neither `rg` nor `grep` could be run at all.  Those are opposite
    facts: "no readers" is evidence toward NOT-PRODUCTION, "never searched" is
    no evidence whatsoever — and they were indistinguishable in the output, so
    a broken search tool produced a confident-looking empty reader list.
    """

    def __init__(self) -> None:
        self.attempted = 0
        self.failed = 0

    @property
    def degraded(self) -> bool:
        return self.failed > 0


SEARCH = _SearchHealth()


def _rg(pattern: str, *, fixed: bool = False) -> set[str]:
    """Stems of live .py files matching `pattern` (ripgrep, else grep)."""
    SEARCH.attempted += 1
    for cmd in (["rg", "-l"] + (["-F"] if fixed else []) + ["--glob", "*.py",
                                pattern, str(HERE)],
                ["grep", "-rl"] + (["-F"] if fixed else []) +
                ["--include=*.py", pattern, str(HERE)]):
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue
        if out.returncode in (0, 1):
            return {Path(l).stem for l in out.stdout.splitlines()
                    if l and "_deprecated" not in l}
    # Neither tool ran — absent, timed out, or exited outside {0,1}.  The empty
    # set below means "not searched", NOT "no matches"; record it so the caller
    # cannot present the difference as a measurement.
    SEARCH.failed += 1
    return set()


def witnesses_of(stem: str) -> set[str]:
    """Witness filenames this producer emits, per each witness's own scriptFile."""
    names = set()
    for w in HERE.rglob("*.witness.json"):
        if "_deprecated" in w.parts:
            continue
        try:
            d = json.loads(w.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        if isinstance(d, dict):
            sf = d.get("scriptFile") or ""
            if isinstance(sf, str) and sf[:-3] == stem:
                names.add(w.name)
    return names


def readers_of(stem: str, wnames: set[str]) -> set[str]:
    """Stems that read one of this producer's witnesses, or import it."""
    out: set[str] = set()
    for n in wnames:
        out |= _rg(n, fixed=True)
    out |= _rg(rf"^\s*(from|import)\s+{re.escape(stem)}\b")
    return out - {stem}


def classify(stem: str, depth: int = 3) -> dict:
    """Walk outward from `stem` looking for a production location."""
    failed_before = SEARCH.failed
    frontier, seen, path = {stem}, set(), []
    for _ in range(depth):
        nxt: set[str] = set()
        for s in sorted(frontier - seen):
            seen.add(s)
            hit = PRODUCTION_STEMS & {s}
            if hit:
                return {"stem": stem, "production": True,
                        "via": path + [s], "reason": "named production location",
                        "search_degraded": SEARCH.failed > failed_before}
            r = readers_of(s, witnesses_of(s))
            nxt |= r
        if not nxt:
            break
        path.append(f"<{len(nxt)} readers>")
        frontier = nxt
    src = HERE / f"{stem}.py"
    hits = list(src.rglob("*")) if src.is_dir() else []
    defines_const = False
    for p in ([src] if src.exists() else
              [p for p in HERE.rglob(f"{stem}.py") if "_deprecated" not in p.parts]):
        if PRODUCTION_CONST.search(p.read_text(encoding="utf-8", errors="ignore")):
            defines_const = True
    return {"stem": stem, "production": defines_const,
            "via": path, "direct_readers": sorted(readers_of(stem, witnesses_of(stem))),
            "search_degraded": SEARCH.failed > failed_before,
            "reason": ("defines a LAMBDA_/ALPHA_/Q_ production constant"
                       if defines_const else
                       "reaches no production location within depth")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("stems", nargs="*")
    ap.add_argument("--all-dirty", action="store_true",
                    help="classify every producer the raw-float64 audit flags")
    args = ap.parse_args()

    stems = list(args.stems)
    if args.all_dirty:
        aud = HERE / "witness-raw-float64-audit.witness.json"
        d = json.loads(aud.read_text(encoding="utf-8")).get("data", {})
        for f in list(d.get("regressed", {}) or {}):
            w = HERE / Path(f).name
            if w.exists():
                try:
                    sf = json.loads(w.read_text(encoding="utf-8")).get("scriptFile", "")
                    if sf.endswith(".py"):
                        stems.append(sf[:-3])
                except Exception:  # noqa: BLE001
                    pass
    if not stems:
        print("no stems given; pass names or --all-dirty")
        return 2

    for s in stems:
        r = classify(s)
        verdict = "PRODUCTION" if r["production"] else "NOT-PRODUCTION"
        print(f"\n{s}")
        print(f"  verdict : {verdict}  ({r['reason']})")
        if r.get("direct_readers") is not None:
            print(f"  readers : {r['direct_readers'] or 'NONE (leaf)'}")
        if r.get("search_degraded"):
            print("  SEARCH  : *** INCOMPLETE *** one or more reachability searches"
                  "\n            could not be run (rg and grep both absent, timed"
                  "\n            out, or errored). An empty 'readers' above is NOT"
                  "\n            evidence of non-reachability — it is no evidence.")
        if r["production"]:
            print("  action  : convert to mpmath — do NOT deprecate-and-tier")
        else:
            print("  action  : eligible for precision_tier='float64' + deprecated,"
                  "\n            AFTER checking the skill's non-reachability arms"
                  "\n            (cheat-sheet 'closed' status, production constants)")

    ran = SEARCH.attempted - SEARCH.failed
    print(f"\nsearch coverage: {ran}/{SEARCH.attempted} reachability searches ran")
    if SEARCH.degraded:
        print(f"WARNING: {SEARCH.failed} search(es) did NOT run. This is not a"
              "\n         classification failure — it means part of the evidence"
              "\n         was never gathered. Any NOT-PRODUCTION verdict above that"
              "\n         rests on an empty reader set is unsupported. Re-run with"
              "\n         rg or grep available before acting on it.")
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
