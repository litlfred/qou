#!/usr/bin/env python3
"""Which muon-anchored witnesses are stale for reasons that have NOTHING to do
with the anchor?  Measured on main, before any anchor is moved.

Bean `qou-goc9` sibling / PR #5500 prerequisite.

## Why this exists

PR #5500 moves the *ideal/muon* q₀ anchor from the frozen self-certifying value
`A = 1.10997859555733…` to the live CODATA-2022 derivation `C = 1.10997859564273…`.
Doing so makes every witness stamped `q0Anchor: muon` with `q0Value = A`
inconsistent with its own anchor, and `q0_anchor_consistency_audit` turns red.

The obvious move — regenerate them all in that PR — produces a diff in which
**two unrelated causes are superimposed**: the owner-ruled anchor migration, and
however much ordinary staleness had already accumulated.  A reviewer looking at
a changed number afterwards cannot tell which cause moved it.

So this script measures the second cause **on main, with the anchor untouched**:
re-run each producer and ask whether it still reproduces its committed artifact.
Whatever differs here differs for reasons that predate and are independent of
the anchor ruling, and belongs in its own PR.

## Method, and the three traps it is built around

1. **Producer resolution is by `scriptFile`, never by grep.**  An earlier
   attempt fell back to matching any file *mentioning* a witness's name and
   duly "resolved" a `.txt` and a `.witness.json` as producers.  `scriptFile` is
   a bare basename, so it is resolved against a basename index of the tree and
   an **ambiguous or missing** basename is reported as such rather than guessed.
2. **Producers write SIBLING witnesses.**  The isotope producer rewrites 21
   files the sampler never targeted.  So the whole `computations/` tree is
   restored after every single run, and any sibling that moved is recorded —
   otherwise the run leaves a dirty tree that reads as real work.
3. **Ephemeral fields are masked** using `qou_substrate.witness._EPHEMERAL_META_FIELDS`
   — the same set the enforcement paths use — so a re-run that merely restamps
   `computedAt` / `commitSha` / `environment` is reported as UNCHANGED, not as a
   difference.  Comparing raw bytes would call every single producer stale.

## What a verdict means

    UNCHANGED   re-run reproduces the committed artifact once ephemera are
                masked.  The anchor move is the ONLY thing that will change it.
    SUBSTANTIVE the producer already disagrees with its committed artifact ON
                MAIN.  Pre-existing staleness — drain separately.
    CRASH       the producer does not run at all here; it cannot be regenerated
                in either PR until that is fixed.
    TIMEOUT     exceeded the per-producer budget; unmeasured, not a verdict.

No witness is written and no number is edited.  This is a measurement.
"""
from __future__ import annotations

import argparse, collections, glob, json, os, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MUON_A = "1.109978595557"
sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
try:
    from qou_substrate.witness import _EPHEMERAL_META_FIELDS as EPH
except Exception:
    EPH = frozenset({"commitSha", "computedAt", "durationMs", "environment",
                     "scriptCommitSha", "durationSeconds", "elapsed_seconds",
                     "elapsed_sec", "duration_sec"})


def strip_eph(o):
    if isinstance(o, dict):
        return {k: strip_eph(v) for k, v in o.items() if k not in EPH}
    if isinstance(o, list):
        return [strip_eph(v) for v in o]
    return o


def canon(path):
    try:
        return json.dumps(strip_eph(json.load(open(path))), sort_keys=True)
    except Exception:
        return None


def targets():
    idx = collections.defaultdict(list)
    for p in glob.glob("**/*.py", recursive=True):
        if "/_deprecated/" in p or "/.lake/" in p:
            continue
        idx[os.path.basename(p)].append(p)
    out = []
    for wp in sorted(glob.glob("computations/**/*.witness.json", recursive=True)):
        try:
            d = json.load(open(wp))
        except Exception:
            continue
        if d.get("q0Anchor") != "muon":
            continue
        if not str(d.get("q0Value", "")).startswith(MUON_A):
            continue
        sf = d.get("scriptFile")
        cands = idx.get(os.path.basename(sf), []) if sf else []
        out.append((wp, sf, cands))
    return out


def restore():
    """Restore producer-written artifacts — and NEVER source.

    This originally ran `git checkout -- computations/`, which reverts
    *everything* under that tree.  This script lives there, so its own
    end-of-run restore silently reverted its own uncommitted source edits: a
    fix was written, tested green, and was gone from disk before it could be
    staged, leaving a commit that carried the message but not the change.

    So: restore only modified NON-`.py` paths.  Producers write witnesses and
    data artifacts, never source, so nothing legitimate is lost — and leaving a
    stray artifact behind is a far cheaper failure than silently reverting code.
    """
    out = subprocess.run(["git", "diff", "--name-only", "--", "computations/"],
                         cwd=ROOT, capture_output=True, text=True).stdout.split()
    targets = [f for f in out if not f.endswith(".py")]
    if targets:
        subprocess.run(["git", "checkout", "--"] + targets,
                       cwd=ROOT, capture_output=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=300, help="per-producer seconds")
    ap.add_argument("--limit", type=int, default=0, help="0 = all")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    tg = targets()
    print(f"muon-anchored witnesses carrying A: {len(tg)}")
    runnable = [(w, s, c) for w, s, c in tg if len(c) == 1]
    skipped = [(w, s, c) for w, s, c in tg if len(c) != 1]
    for w, s, c in skipped:
        why = "no scriptFile" if not s else f"{len(c)} candidates for {s!r}"
        print(f"  SKIP  {w}  ({why})")
    if args.limit:
        runnable = runnable[: args.limit]
    print(f"measuring {len(runnable)} producers, {args.timeout}s budget each\n")

    results, t0 = [], time.time()
    for i, (wp, _sf, cands) in enumerate(runnable, 1):
        prod = cands[0]
        before = {p: canon(p) for p in
                  glob.glob("computations/**/*.witness.json", recursive=True)}
        el = time.time() - t0
        print(f"[{i}/{len(runnable)}] {prod}  (elapsed {el/60:.1f}m, "
              f"eta {(el/max(i-1,1))*(len(runnable)-i+1)/60:.0f}m)", flush=True)
        try:
            r = subprocess.run([sys.executable, prod], cwd=ROOT,
                               capture_output=True, timeout=args.timeout)
            rc = r.returncode
        except subprocess.TimeoutExpired:
            rc = None
        if rc is None:
            verdict, sib = "TIMEOUT", []
        elif rc != 0:
            verdict, sib = "CRASH", []
        else:
            after = {p: canon(p) for p in
                     glob.glob("computations/**/*.witness.json", recursive=True)}
            moved = [p for p in after if before.get(p) != after[p]]
            verdict = "SUBSTANTIVE" if wp in moved else "UNCHANGED"
            sib = [p for p in moved if p != wp]
        results.append({"producer": prod, "witness": wp, "verdict": verdict,
                        "siblings_moved": sib})
        extra = f"  (+{len(sib)} sibling(s) moved)" if sib else ""
        print(f"      -> {verdict}{extra}", flush=True)
        restore()

    restore()
    tally = collections.Counter(r["verdict"] for r in results)
    print("\n" + "=" * 66)
    print("TALLY:", dict(tally))
    for v in ("SUBSTANTIVE", "CRASH", "TIMEOUT"):
        rs = [r for r in results if r["verdict"] == v]
        if rs:
            print(f"\n{v} ({len(rs)}):")
            for r in rs:
                print(f"  {r['producer']}")
    print(f"\nwall {(time.time()-t0)/60:.1f} min")
    if args.out:
        json.dump({"results": results, "tally": dict(tally),
                   "skipped": [{"witness": w, "scriptFile": s,
                                "candidates": c} for w, s, c in skipped]},
                  open(args.out, "w"), indent=2)
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
