#!/usr/bin/env python3
"""The OLD-MUON (CODATA-2018) witness population: how big is it really, and how
much of it is genuinely stale rather than a deliberate historical record?

Bean `qou-qgnl` / `qou-vn63`.  Sibling of, and deliberately disjoint from,
`q0_muon_witness_staleness_triage.py` (PR #5519), whose selector is the
A-population that PR #5500 owns.

## Three muon values, and why a short prefix cannot tell them apart

    A = 1.109978595557334…   frozen canonical muon pin (what the corpus calls
                             "the muon anchor"; `q-pinning-50-digit.witness.json`)
    B = 1.109978595554180…   the CODATA-2018 lepton-tower derivation   <-- THIS FILE
    C = 1.109978595642739…   the CODATA-2022 derivation, and what
                             `qou_substrate.constants.q_muon_at()` returns TODAY

They agree to eleven significant digits.  A ten- or twelve-digit prefix grep
matches all three, so every count in this file is taken at a **13-digit**
prefix that actually discriminates, and every number this script prints carries
the prefix it was obtained with.  A sibling agent grepping a non-discriminating
prefix reported ~150 and missed two thirds of this population.

## Why the B-population is separable from the A->C anchor migration

A witness whose recorded q0 is B is stale *on its own terms*: B is not the
anchor now and was not the anchor when A was frozen either.  That is true
whatever the anchor eventually becomes, so this drain does not wait on #5500.
Measured file-level overlap with #5500's selector (`q0Anchor == "muon"` AND
`q0Value` starting with A) is **1** file, and it is the probe that deliberately
records all three values.

## The partition — the population is NOT uniformly stale

B almost never appears in the standardized `q0Value` metadata field (1 of 268).
It appears inside the payload, and *where* it appears is what decides whether
the witness is stale or is a correct record OF staleness:

    HISTORICAL  the key names the value as stale/old/legacy — e.g.
                `data.pins.stale_muon_pin_q0` in `mp_dk_decisive_test`, whose
                whole subject is the drift between the stale muon pin and the
                canonical one.  B is the SUBJECT here.  Regenerating it would
                destroy the measurement.  NOT a drain target.
    MUON-LEG    the key names the value as the muon anchor of a cross-anchor
                comparison (`data.q_muon`, `data.anchors.q_muon`).  B here IS
                wrong — the live muon source returns C — but correcting it is
                the A->C anchor migration in substance, on files #5500 does not
                select.  Reported, not drained unilaterally.
    SCANNER     the witness belongs to a corpus-scanning auditor and contains
                B because it FOUND B (`hits[].text`, `data.rows[].issues[]
                .literal`).  It is a report, not a pin; B stays after a re-run
                for as long as B is anywhere in the tree.  Such a witness can
                still be stale -- `q0_consistency_audit`'s hit list moved
                253 -> 318 -- but that is stale AUDIT OUTPUT, a different
                finding from a stale anchor, and must not be counted as one.
    PRIMARY     the key is the producer's own working q0 (`parameters.q_0`,
                `q_0`, `q0`, `q`) with nothing marking it as a reference.  The
                producer computed its result at B.  This is the clean drain.

## The four properties inherited from the A-harness (do not remove any)

1. Producers are resolved by the witness's `scriptFile` field against a
   basename index — never by grepping for files that mention the witness.
2. The whole `computations/` tree is restored after every run (producers write
   SIBLING witnesses), and moved siblings are recorded.
3. Ephemera are masked using `qou_substrate.witness._EPHEMERAL_META_FIELDS`
   PLUS `invocation`, matching `scripts/precision-gates.sh`: a witness
   committed from a bare `python3 <script>` otherwise differs from a harness
   run on argv alone and reads as staleness.
4. A nonzero exit is NOT a crash.  Many producers write their artifact and then
   exit 1 on an internal assertion.  CRASH means "emitted nothing".

No witness is written and no number is edited by this script.  It measures.
"""
from __future__ import annotations

import argparse, collections, glob, json, os, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MUON_A = "1.109978595557"      # frozen canonical pin
MUON_B = "1.109978595554"      # CODATA-2018 derivation  <-- this file's target
MUON_C = "1.109978595642"      # CODATA-2022 derivation (what q_muon_at() returns)

sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
try:
    from qou_substrate.witness import _EPHEMERAL_META_FIELDS as _SHARED
except Exception:
    _SHARED = frozenset({"commitSha", "computedAt", "durationMs", "environment",
                         "scriptCommitSha", "durationSeconds", "elapsed_seconds",
                         "elapsed_sec", "duration_sec"})
EPH = frozenset(_SHARED | {"invocation"})

try:
    sys.path.insert(0, str(ROOT / "computations"))
    from q0_repin_sweep import ANCHOR_DEFINING          # type: ignore
except Exception:
    ANCHOR_DEFINING = frozenset({"q_pinning_50_digit"})

# A key fragment that marks the occurrence as a RECORD OF a stale value rather
# than a value in use.  Kept deliberately narrow: only words that say "this is
# the old one".  `muon`/`anchor` are NOT here — see MUON_LEG_MARKS.
HISTORICAL_MARKS = ("stale", "old_", "_old", "legacy", "historical",
                    "pre_repin", "prerepin", "three_values", "drift",
                    "superseded", "deprecated")
# A key fragment marking the occurrence as the muon leg of a cross-anchor
# comparison.  Wrong (the live muon source returns C) but its correction is the
# A->C migration, which is PR #5500's subject.
MUON_LEG_MARKS = ("muon", "anchor")
# A key fragment marking the occurrence as SCANNED EVIDENCE: the witness of a
# corpus-scanning auditor, which contains B because it FOUND B in the tree.
# Such a witness is not stale-because-of-its-q0 -- it is a report, and B will
# still be in it after a re-run for as long as B is anywhere in the corpus.
#
# This class was not in the first version of this file and had to be measured
# into existence.  `fitted_labelled_canonical_audit` and `q0_consistency_audit`
# both came back SUBSTANTIVE with B still present afterwards; reading the
# actual values explained why -- `data.rows[].issues[].literal` is
# '1.1099785955541805' quoted FROM a source file, and `hits[].text` is the
# whole line 'q0_proton = 1.10997858275138...  q0_muon = 1.10997859555418...'.
# Neither is the producer's own pin.  A path-name rule alone would have kept
# calling them PRIMARY, i.e. would have reported a scanner's correct report as
# a stale anchor.
SCANNER_MARKS = ("hits", "rows", "issues", "literal", "candidates", "matches",
                 "findings", "evidence", "text", "line", "sample", "snippet",
                 "occurrences", "offenders", "violations")

# Producers that must legitimately keep a muon-side value: their witness is a
# record of, or a comparison against, the muon layer.  Established BEFORE any
# drain, per the task constraint.  Entries are producer stems.
LEGITIMATELY_MUON = frozenset({
    "q_pinning_50_digit",              # DEFINES the anchor (also ANCHOR_DEFINING)
    "muon_pin_three_values_probe",     # its subject is all three values
    "mp_dk_decisive_test",             # subject: drift stale-pin vs canonical
    "cross_check_trM_1ppb",            # docstring: must run under the MUON pin
    "atomic_tr_m_mpfr_50dps",          # dual-layer: one witness per layer
    "he4_stage2_ranking_seminormal_xcheck",   # asserts the muon prefix
    "mu_substrate_tension_audit_100dps",      # measures the mu-p tension itself
})


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


def walk(o, pre=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from walk(v, f"{pre}.{k}" if pre else k)
    elif isinstance(o, list):
        for v in o:
            yield from walk(v, f"{pre}[]")
    else:
        yield pre, o


def classify_paths(paths):
    """PRIMARY / MUON-LEG / HISTORICAL for a witness, from its B-carrying keys.

    A witness is classified by its STRONGEST class: any unmarked (primary)
    occurrence makes it PRIMARY, because that is a value the producer was
    actually computing with.  Only when every occurrence is marked does the
    marking decide.
    """
    cls = set()
    for p in paths:
        low = p.lower()
        if any(m in low for m in HISTORICAL_MARKS):
            cls.add("HISTORICAL")
        elif any(m in low for m in SCANNER_MARKS):
            cls.add("SCANNER")
        elif any(m in low for m in MUON_LEG_MARKS):
            cls.add("MUON-LEG")
        else:
            cls.add("PRIMARY")
    for c in ("PRIMARY", "MUON-LEG", "SCANNER"):
        if c in cls:
            return c
    return "HISTORICAL"


def survey():
    """Every witness carrying B, with its B-paths, class and resolved producer."""
    idx = collections.defaultdict(list)
    for p in glob.glob("**/*.py", recursive=True):
        if "/_deprecated/" in p or "/.lake/" in p:
            continue
        idx[os.path.basename(p)].append(p)

    rows = []
    for wp in sorted(glob.glob("computations/**/*.witness.json", recursive=True)):
        try:
            txt = open(wp, encoding="utf-8").read()
        except Exception:
            continue
        if MUON_B not in txt:
            continue
        try:
            d = json.loads(txt)
        except Exception:
            rows.append({"witness": wp, "b_paths": [], "class": "UNPARSEABLE",
                         "scriptFile": None, "producer": None,
                         "resolution": "unparseable"})
            continue
        bp = sorted({k for k, v in walk(d) if MUON_B in str(v)})
        sf = d.get("scriptFile")
        cands = idx.get(os.path.basename(sf), []) if sf else []
        if not sf:
            res = "no-scriptFile"
        elif len(cands) == 1:
            res = "unique"
        elif not cands:
            res = "unresolved"
        else:
            res = f"ambiguous({len(cands)})"
        stem = os.path.splitext(os.path.basename(sf))[0] if sf else ""
        rows.append({
            "witness": wp,
            "b_paths": bp,
            "class": classify_paths(bp) if bp else "TEXT-ONLY",
            "scriptFile": sf,
            "producer": cands[0] if len(cands) == 1 else None,
            "resolution": res,
            "q0Anchor": d.get("q0Anchor"),
            "carries_A": MUON_A in txt,
            "carries_C": MUON_C in txt,
            "deprecated_tree": "/_deprecated/" in wp,
            "legitimately_muon": stem in LEGITIMATELY_MUON,
            "anchor_defining": stem in ANCHOR_DEFINING,
        })
    return rows


def restore():
    """Restore producer-written artifacts — and NEVER source (see A-harness)."""
    out = subprocess.run(["git", "diff", "--name-only", "--", "computations/"],
                         cwd=ROOT, capture_output=True, text=True).stdout.split()
    tg = [f for f in out if not f.endswith(".py")]
    if tg:
        subprocess.run(["git", "checkout", "--"] + tg, cwd=ROOT,
                       capture_output=True)


def environment():
    import platform
    mods = {}
    for name in ("mpmath", "sympy", "numpy", "scipy", "pyhecke_native"):
        try:
            m = __import__(name)
            mods[name] = getattr(m, "__version__", "present")
        except Exception:
            mods[name] = None
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                          capture_output=True, text=True).stdout.strip()
    return {"python": platform.python_version(), "modules": mods,
            "tree_commit": head,
            "prefixes": {"A": MUON_A, "B": MUON_B, "C": MUON_C}}


def diff_paths(a, b, prefix="", out=None, cap=40):
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


def cmd_survey(args):
    rows = survey()
    print(f"B-population (prefix {MUON_B!r}): {len(rows)} witnesses\n")
    for key in ("class", "resolution", "q0Anchor"):
        c = collections.Counter(str(r.get(key)) for r in rows)
        print(f"by {key}:")
        for k, n in c.most_common():
            print(f"  {n:5d}  {k}")
        print()
    prim = [r for r in rows if r["class"] == "PRIMARY"]
    drainable = [r for r in prim if r["producer"] and not r["legitimately_muon"]
                 and not r["anchor_defining"] and not r["deprecated_tree"]]
    print(f"PRIMARY: {len(prim)};  of those with a uniquely-resolved producer, "
          f"not legitimately-muon, not anchor-defining, not _deprecated: "
          f"{len(drainable)}")
    print(f"distinct producers in that set: "
          f"{len({r['producer'] for r in drainable})}")
    if args.out:
        # Provenance stamp (bean qou-f1rs): the witness dict was built
        # INLINE at the write below, so there was nothing to stamp. It
        # is bound to a name here so this producer records which script
        # wrote it -- a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        _prov_payload_1 = {"prefixes": {"A": MUON_A, "B": MUON_B, "C": MUON_C},
                   "population": len(rows),
                   "by_class": dict(collections.Counter(r["class"] for r in rows)),
                   "by_resolution": dict(collections.Counter(r["resolution"]
                                                             for r in rows)),
                   "rows": rows, "environment": environment()}
        _prov_payload_1.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            _prov_payload_1, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(_prov_payload_1,
                  open(args.out, "w"), indent=2)
        print(f"\nwrote {args.out}")
    return 0


def cmd_rerun(args):
    ENV = environment()
    missing = [k for k, v in ENV["modules"].items()
               if v is None and k in ("mpmath", "sympy", "numpy")]
    if missing:
        print(f"REFUSING TO RUN: {', '.join(missing)} not importable. Every "
              f"producer would die at import and the sweep would report the "
              f"whole corpus as reproducing its artifacts.")
        return 2
    print(f"environment: {ENV['modules']}")

    rows = survey()
    sel = [r for r in rows
           if r["class"] == "PRIMARY" and r["producer"]
           and not r["legitimately_muon"] and not r["anchor_defining"]
           and not r["deprecated_tree"]]
    # One row per PRODUCER: a producer rewrites all its own witnesses in one run.
    byprod = {}
    for r in sel:
        byprod.setdefault(r["producer"], []).append(r["witness"])
    runnable = sorted(byprod.items())
    if args.limit:
        runnable = runnable[: args.limit]
    print(f"B-population {len(rows)}; PRIMARY drain candidates "
          f"{len(sel)} witnesses over {len(byprod)} producers; "
          f"measuring {len(runnable)} with a {args.timeout}s budget each\n")

    def dump(rs, partial):
        if not args.out:
            return
        tmp = args.out + ".tmp"
        # Provenance stamp (bean qou-f1rs): the witness dict was built
        # INLINE at the write below, so there was nothing to stamp. It
        # is bound to a name here so this producer records which script
        # wrote it -- a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        _prov_payload_2 = {"results": rs,
                   "tally": dict(collections.Counter(r["verdict"] for r in rs)),
                   "tree_commit": ENV.get("tree_commit"),
                   "prefixes": {"A": MUON_A, "B": MUON_B, "C": MUON_C},
                   "population": len(runnable), "partial": partial,
                   "measured": len(rs), "total": len(runnable),
                   "environment": ENV}
        _prov_payload_2.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            _prov_payload_2, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(_prov_payload_2, open(tmp, "w"), indent=2)
        os.replace(tmp, args.out)

    results, t0 = [], time.time()
    if args.resume and args.out and os.path.exists(args.out):
        try:
            results = json.load(open(args.out)).get("results", [])
            print(f"resuming: {len(results)} producer(s) already measured")
        except Exception as e:
            print(f"resume failed ({e}); starting from scratch")
    done = {r["producer"] for r in results}

    def snap():
        out = {}
        for p in glob.glob("computations/**/*.witness.json", recursive=True):
            try:
                out[p] = (canon(p), os.stat(p).st_mtime_ns)
            except OSError:
                out[p] = (None, None)
        return out

    for i, (prod, wits) in enumerate(runnable, 1):
        if prod in done:
            print(f"[{i}/{len(runnable)}] {prod}  -- already measured", flush=True)
            continue
        before = snap()
        el = time.time() - t0
        print(f"[{i}/{len(runnable)}] {prod}  (elapsed {el/60:.1f}m, "
              f"eta {(el/max(i-1,1))*(len(runnable)-i+1)/60:.0f}m)", flush=True)
        err = ""
        t1 = time.time()
        try:
            r = subprocess.run([sys.executable, prod], cwd=ROOT,
                               capture_output=True, timeout=args.timeout)
            rc = r.returncode
            err = ((r.stderr or b"") + b"\n--stdout--\n"
                   + (r.stdout or b"")).decode("utf-8", "replace")[-900:]
        except subprocess.TimeoutExpired:
            rc = None
        secs = round(time.time() - t1, 1)
        if rc is None:
            verdict, sib, moved = "TIMEOUT", [], []
        else:
            after = snap()
            moved = [p for p in after
                     if before.get(p, (None, None))[0] != after[p][0]]
            sib = [p for p in moved if p not in wits]
            touched = [p for p in after
                       if before.get(p, (None, None))[1] != after[p][1]]
            if rc != 0 and not touched:
                verdict = "CRASH"
            else:
                verdict = ("SUBSTANTIVE" if any(w in moved for w in wits)
                           else "UNCHANGED")
                if rc != 0:
                    verdict += "/ASSERT-FAIL"
        rec = {"producer": prod, "witnesses": wits, "verdict": verdict,
               "seconds": secs, "siblings_moved": sib}
        if verdict.startswith("SUBSTANTIVE"):
            fields = {}
            still_b = []
            for w in wits:
                if w not in moved:
                    continue
                b_ = before.get(w, (None, None))[0]
                a_ = after.get(w, (None, None))[0]
                if b_ and a_:
                    try:
                        fields[w] = diff_paths(json.loads(b_), json.loads(a_))
                    except Exception:
                        pass
                try:
                    now = open(w, encoding="utf-8").read()
                    if MUON_B in now:
                        still_b.append(w)
                except Exception:
                    pass
            rec["changed_fields"] = fields
            # Did the re-run actually clear B, and to WHAT?  A drain that leaves
            # B in place is not a drain, and one that lands on C rather than the
            # proton pin is the A->C migration arriving by another door.
            rec["still_carries_B_after"] = still_b
            landed = collections.Counter()
            for w in wits:
                try:
                    now = open(w, encoding="utf-8").read()
                except Exception:
                    continue
                landed["A" if MUON_A in now else ""] += 0
                for lab, pre in (("A", MUON_A), ("B", MUON_B), ("C", MUON_C)):
                    if pre in now:
                        landed[lab] += 1
            rec["landed_on"] = {k: v for k, v in landed.items() if k}
        if verdict.startswith("CRASH") or "ASSERT-FAIL" in verdict:
            rec["stderr_tail"] = err
        results.append(rec)
        extra = f"  (+{len(sib)} sibling(s) moved)" if sib else ""
        print(f"      -> {verdict} [{secs}s]{extra}", flush=True)
        dump(results, partial=True)
        restore()

    restore()
    print("\n" + "=" * 66)
    print("TALLY:", dict(collections.Counter(r["verdict"] for r in results)))
    for v in ("SUBSTANTIVE", "SUBSTANTIVE/ASSERT-FAIL", "CRASH", "TIMEOUT"):
        rs = [r for r in results if r["verdict"] == v]
        if rs:
            print(f"\n{v} ({len(rs)}):")
            for r in rs:
                print(f"  {r['producer']}  [{r['seconds']}s]")
    print(f"\nwall {(time.time()-t0)/60:.1f} min")
    if args.out:
        dump(results, partial=False)
        print(f"wrote {args.out}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("survey", help="classify the B-population; runs nothing")
    s.add_argument("--out", default="")
    s.set_defaults(fn=cmd_survey)
    r = sub.add_parser("rerun", help="re-run PRIMARY-class producers")
    r.add_argument("--timeout", type=int, default=300)
    r.add_argument("--limit", type=int, default=0)
    r.add_argument("--out", default="")
    r.add_argument("--resume", action="store_true")
    r.set_defaults(fn=cmd_rerun)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
