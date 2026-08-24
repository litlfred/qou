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

    UNCHANGED      re-run reproduces the committed artifact once ephemera are
                   masked.  The anchor move is the ONLY thing that changes it.
    SUBSTANTIVE    already disagrees with its committed artifact ON MAIN.
                   Pre-existing staleness — drain separately.
    …/ASSERT-FAIL  as above, but the producer also exited nonzero because an
                   assertion INSIDE it failed.  It still ran and still wrote its
                   artifact, so the staleness verdict stands and it CAN be
                   regenerated; the failing assertion is a separate question.
    CRASH          emitted nothing at all.  This one genuinely cannot be
                   regenerated until it is fixed.
    TIMEOUT        exceeded the per-producer budget; unmeasured, not a verdict.

A nonzero exit was originally classified CRASH outright.  That was wrong in the
direction that matters: `cyclic_intertwiner_verify.py` exits 1 while writing its
witness and reporting `PASS=False, max_abs=0.001150426`, so calling it a crash
discarded a real SUBSTANTIVE answer *and* put a false claim in a PR body — that
it could not be regenerated at all.

No witness is written and no number is edited.  This is a measurement.
"""
from __future__ import annotations

import argparse, collections, glob, json, os, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MUON_A = "1.109978595557"
sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
try:
    from qou_substrate.witness import _EPHEMERAL_META_FIELDS as _SHARED
except Exception:
    _SHARED = frozenset({"commitSha", "computedAt", "durationMs", "environment",
                         "scriptCommitSha", "durationSeconds", "elapsed_seconds",
                         "elapsed_sec", "duration_sec"})

# The shared set PLUS `invocation`, matching `scripts/precision-gates.sh`.
# That script masks `invocation` locally rather than widening the shared set,
# and its reason (precision-gates.sh:434) is that `invocation` is genuine
# provenance -- it records argv so a reader can reproduce the number -- while
# 309 in-repo importers depend on `witness.py`'s comparison semantics.  That is
# correct and is left alone.  The same local widening is required *here* for a
# different reason: a witness committed from a bare `python3 <script>` differs
# from this harness's run on argv ALONE, so without it every such producer reads
# SUBSTANTIVE for a reason unrelated to staleness.  Deliberately NOT masked:
# `scriptHash` and `engineVersion` -- a changed producer or engine is signal.
EPH = frozenset(_SHARED | {"invocation"})

# Producers whose witness DEFINES an anchor rather than consuming one.  Single
# source of truth is `computations/q0_repin_sweep.py`; mirrored only if that
# import fails, never re-derived.
#
# This matters because a verdict here reads as a drain instruction.
# `q-pinning-50-digit.witness.json` is what `_q0_value_for_anchor("muon")`
# READS, so regenerating it does not migrate a consumer -- it redefines what
# "muon" MEANS, and every muon-stamped witness in the corpus then disagrees
# with its own anchor (AGENTS.md records 262 Q0_FLIPs and a hard-fail of every
# `ideal_muon` producer, including the one that would regenerate the anchor).
# Listing it beside 18 ordinary staleness rows, indistinguishable, is how that
# gets done by accident.
try:
    sys.path.insert(0, str(ROOT / "computations"))
    from q0_repin_sweep import ANCHOR_DEFINING          # type: ignore
except Exception:
    ANCHOR_DEFINING = frozenset({"q_pinning_50_digit"})


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


def environment():
    """What this run ran against.

    Verdicts are not comparable across containers without it, and that is not
    hypothetical: this sweep was run once with `mpmath` absent (all 55
    producers died at import, every verdict wrong) and once with `scipy`
    absent (`hadron_knot_table` CRASHed for a reason that is this container's,
    not the corpus's). Neither run said so anywhere in its output.
    """
    import platform
    mods = {}
    for name in ("mpmath", "sympy", "numpy", "scipy", "pyhecke_native"):
        try:
            m = __import__(name)
            mods[name] = getattr(m, "__version__", "present")
        except Exception:
            mods[name] = None          # explicit: absent, not merely unrecorded
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                          capture_output=True, text=True).stdout.strip()
    return {"python": platform.python_version(), "modules": mods,
            "tree_commit": head}


def diff_paths(a, b, prefix="", out=None, cap=40):
    """Dotted paths at which two stripped witness bodies differ.

    A SUBSTANTIVE verdict alone says a number moved but not WHICH one, and the
    tree is restored straight afterwards -- so answering "what changed?" later
    means re-running the producer, which for several here costs 420s.  The
    drain PR needs the field list, so record it while it is in hand.
    """
    if out is None:
        out = []
    if len(out) >= cap:
        return out
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a:
                out.append(prefix + k + " (added)")
            elif k not in b:
                out.append(prefix + k + " (removed)")
            else:
                diff_paths(a[k], b[k], prefix + k + ".", out, cap)
            if len(out) >= cap:
                break
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            out.append(f"{prefix.rstrip('.')} (len {len(a)} -> {len(b)})")
        else:
            for i, (x, y) in enumerate(zip(a, b)):
                diff_paths(x, y, f"{prefix}{i}.", out, cap)
                if len(out) >= cap:
                    break
    elif a != b:
        out.append(prefix.rstrip("."))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=300, help="per-producer seconds")
    ap.add_argument("--limit", type=int, default=0, help="0 = all")
    ap.add_argument("--out", default="")
    ap.add_argument("--resume", action="store_true",
                    help="skip producers already measured in --out")
    args = ap.parse_args()

    ENV = environment()
    missing = [k for k, v in ENV["modules"].items()
               if v is None and k in ("mpmath", "sympy", "numpy")]
    if missing:
        # Refuse rather than attribute the resulting silence to the corpus.
        print(f"REFUSING TO RUN: {', '.join(missing)} not importable. Every "
              f"producer would die at import and the sweep would report the "
              f"whole corpus as reproducing its artifacts.")
        return 2
    print(f"environment: {ENV['modules']}")

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

    # Checkpointing.  The first version of this harness held every result in
    # memory and wrote --out once, at the end.  A multi-hour sweep against a
    # container that can be reclaimed therefore had exactly one durable moment,
    # and losing it lost every measurement.  It did get reclaimed, at 7/55.
    # So each result is flushed as it lands, and --resume reads them back.
    def dump(rs, partial):
        if not args.out:
            return
        tmp = args.out + ".tmp"
        for r in rs:            # annotate on every write, resumed rows included
            r["anchor_defining"] = (
                os.path.splitext(os.path.basename(r["producer"]))[0]
                in ANCHOR_DEFINING)
        # 🛑 `tree_commit` and `population` sit BESIDE the tally, not only inside
        # `environment`. A tally is meaningless without the population it was
        # computed over, and this selector's population is not fixed: `targets()`
        # selects on `q0Anchor == "muon"` in the CURRENT tree, so it grows every
        # time someone labels an unstamped witness. Measured 2026-08-24 — the
        # in-scope set went **47 -> 142 in one day**, because main's
        # `4101909790` ("label 229 witnesses from their own payload") stamped
        # 229 previously-unlabelled witnesses and every muon one entered here.
        #
        # So a reader comparing two tallies must be able to see, without
        # digging, that they cover different populations — otherwise "47/47"
        # reads as completion when it is only completion *relative to one
        # tree*. Bean `qou-6q7q`.
        json.dump({"results": rs, "tally": dict(collections.Counter(
                       r["verdict"] for r in rs)),
                   "tree_commit": ENV.get("tree_commit"),
                   "population": len(runnable),
                   "partial": partial, "measured": len(rs),
                   "total": len(runnable), "environment": ENV,
                   "skipped": [{"witness": w, "scriptFile": s_, "candidates": c}
                               for w, s_, c in skipped]},
                  open(tmp, "w"), indent=2)
        os.replace(tmp, args.out)          # atomic: never a half-written file

    results, t0 = [], time.time()
    if args.resume and args.out and os.path.exists(args.out):
        try:
            results = json.load(open(args.out)).get("results", [])
            print(f"resuming: {len(results)} producer(s) already measured")
        except Exception as e:
            print(f"resume failed ({e}); starting from scratch")
    done = {r["producer"] for r in results}
    for i, (wp, _sf, cands) in enumerate(runnable, 1):
        prod = cands[0]
        if prod in done:
            print(f"[{i}/{len(runnable)}] {prod}  -- already measured, skipping",
                  flush=True)
            continue
        # Snapshot content AND mtime.  `produced` must mean "this run wrote
        # something", which content alone cannot tell you: a producer that
        # rewrites a byte-identical witness and one that dies before writing
        # anything both leave the content unchanged.
        def snap():
            out = {}
            for p in glob.glob("computations/**/*.witness.json", recursive=True):
                try:
                    out[p] = (canon(p), os.stat(p).st_mtime_ns)
                except OSError:
                    out[p] = (None, None)
            return out
        before = snap()
        el = time.time() - t0
        print(f"[{i}/{len(runnable)}] {prod}  (elapsed {el/60:.1f}m, "
              f"eta {(el/max(i-1,1))*(len(runnable)-i+1)/60:.0f}m)", flush=True)
        err = ""
        try:
            r = subprocess.run([sys.executable, prod], cwd=ROOT,
                               capture_output=True, timeout=args.timeout)
            rc = r.returncode
            # Keep the tail of stderr.  Without it a CRASH verdict says only
            # THAT the producer died, and diagnosing why means re-running it by
            # hand -- for a producer that may cost 420s.
            err = (r.stderr or b"").decode("utf-8", "replace")[-800:]
        except subprocess.TimeoutExpired:
            rc = None
        if rc is None:
            verdict, sib = "TIMEOUT", []
        else:
            after = snap()
            moved = [p for p in after if before.get(p, (None, None))[0] != after[p][0]]
            sib = [p for p in moved if p != wp]
            # A file this run actually touched, identical content or not.
            touched = [p for p in after
                       if before.get(p, (None, None))[1] != after[p][1]]
            # This was `bool(moved) or canon(wp) is not None`, and `canon(wp)`
            # reads the COMMITTED file, which is on disk whether or not the run
            # wrote anything -- so `produced` was unconditionally True, CRASH
            # was unreachable, and a producer that died at import was reported
            # `UNCHANGED/ASSERT-FAIL`: "reproduces its artifact".  Measured: with
            # mpmath absent, 23 of 23 producers died on the import line and all
            # 23 came back UNCHANGED.  A crash must never read as agreement.
            produced = bool(touched)
            if rc != 0 and not produced:
                verdict = "CRASH"          # genuinely emitted nothing
            else:
                # A nonzero exit does NOT mean the producer failed to run: many
                # write their witness and THEN exit 1 because an ASSERTION
                # inside it failed.  Measured: cyclic_intertwiner_verify.py
                # exits 1, writes its artifact, and reports PASS=False with
                # max_abs=0.001150426.  Calling that CRASH discards a real
                # staleness answer and wrongly implies it cannot be regenerated.
                verdict = "SUBSTANTIVE" if wp in moved else "UNCHANGED"
                if rc != 0:
                    verdict += "/ASSERT-FAIL"
        rec = {"producer": prod, "witness": wp, "verdict": verdict,
               "siblings_moved": sib}
        if verdict.startswith("SUBSTANTIVE"):
            b_, a_ = before.get(wp, (None, None))[0], after.get(wp, (None, None))[0]
            if b_ and a_:
                try:
                    rec["changed_fields"] = diff_paths(json.loads(b_), json.loads(a_))
                except Exception:
                    pass
        if verdict.startswith("CRASH") or "ASSERT-FAIL" in verdict:
            rec["stderr_tail"] = err
        results.append(rec)
        extra = f"  (+{len(sib)} sibling(s) moved)" if sib else ""
        print(f"      -> {verdict}{extra}", flush=True)
        dump(results, partial=True)
        restore()

    restore()
    tally = collections.Counter(r["verdict"] for r in results)
    print("\n" + "=" * 66)
    print("TALLY:", dict(tally))
    ad = [r for r in results if r.get("anchor_defining")]
    if ad:
        print("\nANCHOR-DEFINING — DO NOT DRAIN (regenerating redefines the "
              "anchor itself):")
        for r in ad:
            print(f"  {r['producer']}  [{r['verdict']}]")
    for v in ("SUBSTANTIVE", "CRASH", "TIMEOUT"):
        rs = [r for r in results if r["verdict"] == v]
        if rs:
            print(f"\n{v} ({len(rs)}):")
            for r in rs:
                print(f"  {r['producer']}")
    print(f"\nwall {(time.time()-t0)/60:.1f} min")
    if args.out:
        dump(results, partial=False)
        print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
