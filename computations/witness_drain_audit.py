#!/usr/bin/env python3
"""witness_drain_audit — did self-staleness FALL because witnesses got
fresher, or because they fell out of the audit?

WHY THIS EXISTS (measured 2026-08-23, during a 601-witness drain)
-----------------------------------------------------------------
`witness_dependency_drift.py --strict` reports a single number: how many
witnesses carry a `scriptHash` that no longer matches their producer. That
number is the obvious way to score a drain campaign, and it has a hole:

    a witness with NO `scriptHash` is not self-stale — it is UNVERIFIABLE,
    and unverifiable witnesses are not counted.

So there are two ways to make the number go down. Re-run the producer and
record a fresh hash (a real drain), or write a witness with no `scriptHash`
at all (the witness leaves the audit). Both read as progress. The second is
strictly a loss: it destroys the provenance the audit is built on.

This is not hypothetical. Four witnesses hit it in one batch:

    nucleus-real-sdp-he3          scriptHash e376dec214d2 -> absent
    he4-stage2-ranking-...        scriptHash + scriptFile -> both absent
    option-e-a4-full-reconc...    scriptHash absent
    yekutieli-volume-join         scriptHash + scriptFile -> both absent

Their producers write raw JSON with no `WitnessBuilder` envelope; the
committed copies had been stamped post-hoc by `stamp_staleness_metadata`,
so re-running wrote the only envelope those producers have ever written —
none — and self-staleness fell by four without a single number being
recomputed.

    A METRIC THAT IMPROVES WHEN YOU DELETE THE EVIDENCE IS NOT A METRIC.

Same defect class as bean qou-h4xk (a gutted witness scores zero raw
float64 leaves, which reads as a perfect drain) and qou-lb0f (a cache
check that asked "are there ANY oleans" instead of "the EXPECTED oleans").

WHAT THIS DOES
--------------
Classifies every witness against HEAD, so a drain can be scored honestly:

  DRAINED       stale at HEAD, fresh now                (real progress)
  STILL_STALE   stale at HEAD, stale now
  FRESH         fresh at both
  LOST_PROV     had scriptFile/scriptHash at HEAD, lacks it now   <-- FAILS
  NO_PROV       had none at HEAD and has none now       (pre-existing backlog)
  UNRESOLVABLE  declares a scriptFile no file in the tree bears

"Stale at HEAD" is computed honestly: HEAD's recorded `scriptHash` against
the hash of HEAD's version of the producer, not today's.

`--strict` exits 1 on any LOST_PROV. The pre-existing NO_PROV backlog is
REPORTED, NOT GATED — it is red on arrival, and gating it would make this
script fail on its first run and be disabled, per scripts/precision-gates.sh's
own preamble on red-on-arrival gates.

Complements, does not duplicate, `witness_provenance_audit.py`: that one
asks "does this witness declare a resolvable producer"; this one asks "did
this drain campaign move witnesses forward or just shrink the denominator".
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent

sys.path.insert(0, str(HERE))
try:
    import witness_dependency_drift as wdd
except ImportError:  # pragma: no cover
    wdd = None


def _sha12(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:12]


def _git_show(rev_path: str) -> bytes | None:
    r = subprocess.run(["git", "show", rev_path], cwd=REPO,
                       capture_output=True)
    return r.stdout if r.returncode == 0 else None


def _resolve(script_file: str, witness: Path, index) -> Path | None:
    cands = index.get(script_file, [])
    if not cands:
        return None
    return wdd._resolve_producer(cands, witness)


def classify(witness: Path, index, head_cache: dict) -> tuple[str, dict]:
    rel = str(witness.relative_to(REPO))
    try:
        cur = json.loads(witness.read_text())
    except (json.JSONDecodeError, OSError, UnicodeDecodeError):
        return "UNREADABLE", {"witness": rel}
    if not isinstance(cur, dict):
        return "UNREADABLE", {"witness": rel}

    head_raw = _git_show(f"HEAD:{rel}")
    at_head = head_raw is not None
    head = None
    if head_raw is not None:
        try:
            head = json.loads(head_raw)
        except (json.JSONDecodeError, UnicodeDecodeError):
            head = None
        if not isinstance(head, dict):
            head = None

    c_sf, c_sh = cur.get("scriptFile"), cur.get("scriptHash")
    h_sf = head.get("scriptFile") if head else None
    h_sh = head.get("scriptHash") if head else None

    info = {"witness": rel, "head_scriptFile": h_sf, "now_scriptFile": c_sf,
            # Recorded so the NO_PROV report can split "no hash to compare"
            # from "no producer to locate". Without it the split reads
            # `i.get("scriptHash")` as absent on every row and reports 100%
            # of the backlog as hash-less, which is the same predicate/label
            # mismatch the split was added to fix.
            "now_scriptHash": c_sh}

    # Provenance LOST relative to HEAD — the false-drain case.
    #
    # Fire only on a field that WAS present at HEAD and is now ABSENT. The
    # obvious form of this test — "HEAD had either field and now lacks a
    # complete pair" — over-fires on the pre-existing backlog: a witness
    # carrying a `scriptFile` but no `scriptHash`, unchanged since HEAD, is
    # not a loss, it is red on arrival. Measured: that form reported ~200
    # such witnesses as regressions on its first run, which would have
    # buried the four real ones.
    lost_sf = bool(h_sf) and not c_sf
    lost_sh = bool(h_sh) and not c_sh
    if head is not None and (lost_sf or lost_sh):
        gone = ", ".join(n for n, f in (("scriptFile", lost_sf),
                                        ("scriptHash", lost_sh)) if f)
        info["detail"] = (f"lost {gone}: HEAD scriptFile={h_sf!r} "
                          f"scriptHash={h_sh!r}; now scriptFile={c_sf!r} "
                          f"scriptHash={c_sh!r}")
        return "LOST_PROV", info
    if not (c_sf and c_sh):
        # A witness that did not exist at HEAD and is born without provenance
        # is NOT the pre-existing backlog — it is the backlog GROWING, right
        # now, under whoever just ran the producer. It can never appear as
        # self-stale and can never be drained. Measured 2026-08-23:
        # `probes/motivic_obstruction_symbolic.py` minted one during an
        # unrelated fix (bean qou-nb4s). Unlike NO_PROV this is gateable —
        # it is zero on arrival, so failing on it cannot be red-on-arrival.
        info["detail"] = (f"created since HEAD with scriptFile={c_sf!r} "
                          f"scriptHash={c_sh!r}")
        return ("NEW_NO_PROV" if not at_head else "NO_PROV"), info

    prod = _resolve(c_sf, witness, index)
    if prod is None:
        info["detail"] = f"no file in tree named {c_sf!r}"
        return "UNRESOLVABLE", info

    cur_fresh = (_sha12(prod.read_bytes()) == c_sh)

    head_stale = None
    if head is not None and h_sf and h_sh:
        prel = str(prod.relative_to(REPO))
        if prel not in head_cache:
            hb = _git_show(f"HEAD:{prel}")
            head_cache[prel] = _sha12(hb) if hb is not None else None
        hp = head_cache[prel]
        if hp is not None:
            head_stale = (hp != h_sh)

    if cur_fresh:
        return ("DRAINED" if head_stale else "FRESH"), info
    return "STILL_STALE", info


def self_test() -> int:
    """A detector that cannot be shown to fire is a no-op."""
    import tempfile
    ok = True
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "w.witness.json"
        # A witness that HAD provenance and lost it must classify LOST_PROV.
        def rule(head, now):
            lost_sf = bool(head.get("scriptFile")) and not now.get("scriptFile")
            lost_sh = bool(head.get("scriptHash")) and not now.get("scriptHash")
            return lost_sf or lost_sh

        def born_rule(at_head, now):
            return (not at_head) and not (now.get("scriptFile")
                                          and now.get("scriptHash"))

        H = {"scriptFile": "x.py", "scriptHash": "aaaaaaaaaaaa"}
        cases = [
            ("NEW_NO_PROV fires on a witness born with no provenance",
             born_rule(False, {}), True),
            ("...and NOT on one born WITH provenance",
             born_rule(False, {"scriptFile": "x.py", "scriptHash": "b"*12}), False),
            ("...and NOT on the pre-existing backlog (present at HEAD)",
             born_rule(True, {}), False),
            ("fires on a stripped witness",
             rule(H, {}), True),
            ("fires when only scriptHash is stripped",
             rule(H, {"scriptFile": "x.py"}), True),
            ("stays quiet when provenance is intact",
             rule(H, {"scriptFile": "x.py", "scriptHash": "bbbbbbbbbbbb"}), False),
            ("stays quiet on the UNCHANGED no-scriptHash backlog",
             rule({"scriptFile": "x.py"}, {"scriptFile": "x.py"}), False),
            ("stays quiet when a witness never had provenance",
             rule({}, {}), False),
        ]
        for label, got, want in cases:
            good = (got == want)
            print(f"  {'ok ' if good else 'FAIL'} {label}: {got} (want {want})")
            ok &= good
        _ = p
    print("  SELF-TEST", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--self-test", "--selftest", dest="selftest",
                    action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 when any witness LOST provenance vs HEAD")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    print("=" * 74)
    print("WITNESS DRAIN AUDIT — did staleness fall, or did the denominator?")
    print("=" * 74)
    if args.selftest:
        return self_test()
    if wdd is None:
        print("  cannot import witness_dependency_drift"); return 1

    index = wdd._build_producer_index([HERE, REPO / "tools"])
    buckets: dict[str, list] = {}
    head_cache: dict[str, str | None] = {}
    for w in sorted(HERE.rglob("*.witness.json")):
        if "_deprecated" in w.parts:
            continue
        kind, info = classify(w, index, head_cache)
        buckets.setdefault(kind, []).append(info)

    order = ["DRAINED", "STILL_STALE", "FRESH", "LOST_PROV", "NEW_NO_PROV",
             "NO_PROV", "UNRESOLVABLE", "UNREADABLE"]
    total = sum(len(v) for v in buckets.values())
    print(f"  witnesses examined : {total}")
    for k in order:
        n = len(buckets.get(k, []))
        if n:
            print(f"  {k:13s}: {n}")

    born = buckets.get("NEW_NO_PROV", [])
    if born:
        print(f"\n  *** {len(born)} WITNESS(ES) CREATED WITHOUT PROVENANCE —")
        print("      unverifiable from birth: never stale, never drainable:")
        for i in born:
            print(f"      {i['witness']}")
            print(f"        {i.get('detail','')}")
    lost = buckets.get("LOST_PROV", [])
    if lost:
        print(f"\n  *** {len(lost)} WITNESS(ES) LOST PROVENANCE vs HEAD —")
        print("      these left the staleness audit rather than being drained:")
        for i in lost:
            print(f"      {i['witness']}")
            print(f"        {i.get('detail','')}")
    noprov = buckets.get("NO_PROV", [])
    if noprov:
        # The label used to read "no scriptHash at all", which does not match
        # the predicate above (`not (c_sf and c_sh)` — missing EITHER field).
        # Both matter, and for different reasons: without `scriptHash` there is
        # no recorded value to compare, and without `scriptFile` the producer
        # cannot be located to re-hash. So the union IS the right bucket for
        # "outside the audit" — it was only the sentence that was wrong.
        # Corpus at the time of writing: 2296 complete, 138 file-but-no-hash,
        # 24 hash-but-no-file, 259 neither.
        print(f"\n  (backlog, reported not gated) {len(noprov)} witnesses are "
              f"missing scriptFile, scriptHash, or both,")
        print("   so they sit outside the self-staleness audit entirely:")
        _nh = sum(1 for i in noprov if not i.get("now_scriptHash"))
        _nf = sum(1 for i in noprov if not i.get("now_scriptFile"))
        _both = sum(1 for i in noprov
                    if not i.get("now_scriptHash") and not i.get("now_scriptFile"))
        print(f"     {_nh} carry no scriptHash — no recorded value to compare")
        print(f"     {_nf} carry no scriptFile — producer cannot be located "
              f"to re-hash")
        print(f"     {_both} carry neither")

    if args.json:
        print(json.dumps({k: v for k, v in buckets.items()}, indent=1))
    if lost or born:
        print("\n  FAIL — provenance lost or born missing. Stamp via "
              "WitnessBuilder.stamp_staleness_metadata().")
        return 1 if args.strict else 0
    print("\n  OK — no witness left the audit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
