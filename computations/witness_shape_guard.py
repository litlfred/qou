#!/usr/bin/env python3
"""witness_shape_guard — refuse to commit a witness whose content collapsed.

WHY THIS EXISTS (bean qou-h4xk, measured twice on 2026-08-15)
-------------------------------------------------------------
`witness_raw_float64_audit.py` scores a witness by **counting raw float64
leaves**. It has no notion of how much content a witness should have, so

    an EMPTY or TRUNCATED witness scores exactly like a fully DRAINED one — zero.

That makes "destroy the file" the most effective way to go green. It is not
hypothetical. `rho_k_co_casimir_extended.py` writes its witness after *each*
atom, so during a multi-hour run the committed path holds a partial file. Read
mid-run, twice:

    raw float64 : 4  ->  0        (looks like a perfect drain)
    durationMs  : 2,552,837 -> 519
    diff        : 2,272 deletions

The ratchet said `REGRESSED: 0`. Committing that would have been a false green
*and* would have destroyed the witness. It was caught only by hand, by noticing
`durationMs`.

This is the same defect class as bean `qou-lb0f`, where the lake-cache restore
no-op'd on a cache gutted from 7268 oleans to 459 because its check asked "are
there *any* oleans" instead of "are there the *expected* oleans". The general
rule both instances teach:

    A CHECK WHOSE SUCCESS CONDITION IS SATISFIED BY THE EMPTY STATE
    IS NOT A CHECK.

WHAT THIS DOES
--------------
A count cannot detect a collapse on its own — it needs a reference. The cheap
reference already in the repo is the committed copy. For every
`*.witness.json` modified relative to `HEAD`, this compares against
`git show HEAD:<path>`:

  * leaf-scalar count   (total payload)
  * assertion count
  * data-key count
  * `durationMs`

and fails when content dropped by more than `--tolerance` (default 30%), or
when assertions/data vanished entirely, or when `durationMs` collapsed by
>= 90%. It deliberately says nothing about float counts — that is the ratchet's
job, and the whole point is that the two questions are independent.

SCOPE, STATED PLAINLY
---------------------
This is a **pre-commit** guard, not a CI gate. The damage happens when a gutted
witness is committed, and CI in this repo is `workflow_dispatch`-only under the
2026-06-30 Actions-billing directive, so CI cannot be the backstop. It also
cannot see a witness that was *always* empty — only one that *shrank*. Detecting
the former needs a per-producer expected-shape manifest, which is a larger piece
of work and is not attempted here.

A NOTE ON LEGITIMATE SHRINKAGE
------------------------------
Witnesses do legitimately get smaller — a probe drops a sweep point, a producer
stops emitting a field. That is why this reports and fails rather than silently
reverting: the fix for a real shrink is `--accept`, which records the intent in
the commit message where a reviewer can see it. Do NOT reach for `--accept` to
get past a run you have not looked at; that reintroduces exactly the hole this
closes.

Usage:
    python3 computations/witness_shape_guard.py            # check modified witnesses
    python3 computations/witness_shape_guard.py --selftest # prove the guard fires
    python3 computations/witness_shape_guard.py --json     # machine-readable
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# A witness may shrink this fraction before it is called a collapse. Set from
# the observed incident: rho-k lost 2272 of ~2280 lines (>99%), while ordinary
# re-runs of the qns probes moved 0%. Anything above ~30% is a content change
# worth a human glance, not routine drift.
DEFAULT_TOLERANCE = 0.30

# durationMs is the single most diagnostic field for a partial write: a run that
# was interrupted records the elapsed time *so far*. rho-k showed 2,552,837 -> 519.
DURATION_COLLAPSE = 0.90
# Below this, durationMs is rounding noise rather than evidence of a partial
# write, so the collapse rule does not apply.
DURATION_FLOOR_MS = 1000.0


# Self-describing audit outputs: their payload IS a list of the corpus's
# current findings, so it shrinks legitimately whenever the corpus gets
# cleaner. Draining 14 files makes witness-raw-float64-audit smaller BY
# DESIGN — flagging that as a collapse would punish exactly the work this
# gate family exists to encourage.
#
# Found the honest way: the guard fired on witness-raw-float64-audit
# (66 -> 20 leaves, 70%) on its first live run, immediately after a genuine
# drain. Mirrors SELF_OUTPUTS in witness_raw_float64_audit.py, which excludes
# the same files from the ratchet for the same reason.
SELF_DESCRIBING = {
    "witness-raw-float64-audit.witness.json",
    "witness-float64-padding-audit.witness.json",
    "q0-value-drift-audit.witness.json",
    "no-free-parameter-certificate.witness.json",
    "q0-anchor-consistency-audit.witness.json",
    "mpf-float-source-audit.witness.json",
    # Same class as its sibling above: this audit's witness LISTS its own
    # candidate rows, so draining the corpus shrinks it by design. The
    # qou-65qv drain took it 28 -> 3 rows, a 75% payload drop, which the
    # guard correctly flagged as a collapse under its 30% tolerance.
    "mpf-mixed-arithmetic-audit.witness.json",
    "compute-audit-scan.witness.json",
    "derivation-chain-audit.witness.json",
}


def count_leaves(obj) -> int:
    """Total scalar leaves — the payload size, independent of type."""
    if isinstance(obj, dict):
        return sum(count_leaves(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(count_leaves(v) for v in obj)
    return 1


def _duration(w) -> float | None:
    for holder in (w, w.get("witness") if isinstance(w, dict) else None):
        if isinstance(holder, dict):
            d = holder.get("durationMs")
            if isinstance(d, (int, float)):
                return float(d)
    return None


def shape_of(w) -> dict:
    data = w.get("data") if isinstance(w, dict) else None
    assertions = w.get("assertions") if isinstance(w, dict) else None
    return {
        "leaves": count_leaves(w),
        "assertions": len(assertions) if isinstance(assertions, list) else 0,
        "data_keys": len(data) if isinstance(data, dict) else 0,
        "durationMs": _duration(w),
    }


def compare(before: dict, after: dict, tolerance: float) -> list[str]:
    """Reasons the new shape looks like a collapse. Empty list == fine."""
    reasons: list[str] = []

    b, a = before["leaves"], after["leaves"]
    if b > 0 and a < b * (1.0 - tolerance):
        reasons.append(
            f"payload collapsed: {b:,} -> {a:,} leaves "
            f"({100.0 * (b - a) / b:.0f}% gone, tolerance {tolerance:.0%})"
        )

    for field in ("assertions", "data_keys"):
        b, a = before[field], after[field]
        if b > 0 and a == 0:
            reasons.append(f"{field} vanished: {b} -> 0")
        elif b > 0 and a < b * (1.0 - tolerance):
            reasons.append(f"{field} dropped: {b} -> {a}")

    b, a = before["durationMs"], after["durationMs"]
    # Floor the rule at DURATION_FLOOR_MS. Below it the field carries no signal:
    # a witness whose producer ran in 1 ms re-runs at 0 ms purely from rounding,
    # which trips a relative-drop test every time. The failure mode this rule
    # exists for is a long run cut off mid-write -- the docstring's own example
    # is 2,552,837 -> 519 -- so a sub-second `before` cannot be an instance of
    # it. Measured false positive: habiro-coefficients-oxygen-14 flagged
    # COLLAPSED on 1 -> 0 while GAINING content (34 -> 35 coefficients, no key
    # removed), which is the opposite of what the guard reports (qou-0ndb).
    if isinstance(b, float) and isinstance(a, float) and b > DURATION_FLOOR_MS:
        if a < b * (1.0 - DURATION_COLLAPSE):
            reasons.append(
                f"durationMs collapsed: {b:,.0f} -> {a:,.0f} "
                f"— the hallmark of a run that was interrupted mid-write"
            )
    return reasons


def _git(*args) -> str | None:
    try:
        out = subprocess.run(["git", *args], cwd=ROOT,
                             capture_output=True, text=True, check=False)
        return out.stdout if out.returncode == 0 else None
    except Exception:
        return None


def modified_witnesses() -> list[str]:
    out = _git("diff", "--name-only", "HEAD", "--", "*.witness.json") or ""
    return [p for p in out.split("\n") if p.strip()]


def check(tolerance: float) -> tuple[list[dict], list[str]]:
    """(findings, skipped) over every witness modified against HEAD."""
    findings, skipped = [], []
    for rel in modified_witnesses():
        if Path(rel).name in SELF_DESCRIBING:
            skipped.append(f"{rel} (self-describing audit output — shrinks "
                           f"legitimately as the corpus is drained)")
            continue
        head_raw = _git("show", f"HEAD:{rel}")
        if head_raw is None:
            skipped.append(f"{rel} (new file — no HEAD copy to compare)")
            continue
        path = ROOT / rel
        if not path.exists():
            skipped.append(f"{rel} (deleted)")
            continue
        try:
            before, after = json.loads(head_raw), json.loads(path.read_text())
        except Exception as exc:
            findings.append({"path": rel, "reasons": [f"unparseable JSON: {exc}"]})
            continue
        reasons = compare(shape_of(before), shape_of(after), tolerance)
        if reasons:
            findings.append({"path": rel, "reasons": reasons,
                             "before": shape_of(before), "after": shape_of(after)})
    return findings, skipped


def self_test() -> int:
    """Prove the guard FAILS on the real incident, and stays quiet otherwise.

    A guard that cannot be demonstrated to fire is indistinguishable from a
    no-op — the same standard the raw-float64 audit holds itself to. Case 1 is
    the actual rho-k gutting, numbers taken from the incident.
    """
    full = {
        "witness": {"durationMs": 2552837},
        "assertions": [],
        "data": {"per_atom": [{"atom": i, "compute_wall_sec": 1.0,
                               "rho": 1.0, "tr": 1.0, "chi": [1.0] * 60}
                              for i in range(6)]},
    }
    gutted = {
        "witness": {"durationMs": 519},
        "assertions": [],
        "data": {"per_atom": [{"atom": 0, "compute_wall_sec": 1.0}]},
    }
    drained = json.loads(json.dumps(full))          # same shape, floats -> str
    for atom in drained["data"]["per_atom"]:
        atom["compute_wall_sec"] = str(atom["compute_wall_sec"])
        atom["chi"] = [str(c) for c in atom["chi"]]

    cases = [
        ("the real rho-k gutting is caught", full, gutted, True),
        ("a genuine drain is NOT flagged", full, drained, False),
        ("identical content is NOT flagged", full, full, False),
        ("assertions vanishing is caught",
         {"assertions": [{"a": 1}] * 4, "data": {"k": [1] * 200}},
         {"assertions": [], "data": {"k": [1] * 200}}, True),
        ("growth is NOT flagged", gutted, full, False),
    ]

    failed = 0
    for name, before, after, want_flag in cases:
        reasons = compare(shape_of(before), shape_of(after), DEFAULT_TOLERANCE)
        got = bool(reasons)
        ok = got == want_flag
        failed += not ok
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
        if not ok:
            print(f"        expected flag={want_flag}, got {reasons or 'no reasons'}")
        elif reasons:
            for r in reasons:
                print(f"        -> {r}")

    print()
    if failed:
        print(f"SELF-TEST FAILED — {failed} case(s). The guard does not do what it claims.")
        return 1
    print(f"SELF-TEST PASSED — {len(cases)} cases, including the measured rho-k incident.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    # `--self-test` is the convention scripts/precision-gates.sh invokes; the
    # unhyphenated spelling is accepted too because the sibling audits in
    # computations/ are not consistent about it.
    ap.add_argument("--self-test", "--selftest", dest="selftest",
                    action="store_true",
                    help="prove the guard fires on the real incident")
    ap.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE,
                    help=f"fraction a witness may shrink (default {DEFAULT_TOLERANCE:.0%})")
    ap.add_argument("--accept", action="store_true",
                    help="report collapses but exit 0 — for a shrink you have "
                         "inspected and intend; say so in the commit message")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    if args.selftest:
        print("=" * 74)
        print("WITNESS SHAPE GUARD — self-test")
        print("=" * 74)
        return self_test()

    findings, skipped = check(args.tolerance)

    if args.json:
        print(json.dumps({"findings": findings, "skipped": skipped}, indent=2))
        return 0 if (not findings or args.accept) else 1

    print("=" * 74)
    print("WITNESS SHAPE GUARD — did any witness lose content?")
    print("=" * 74)
    checked = len(modified_witnesses())
    print(f"  witnesses modified vs HEAD : {checked}")
    print(f"  collapsed                  : {len(findings)}")
    for s in skipped:
        print(f"  skipped: {s}")

    if not findings:
        print("\n  OK — no witness lost content.")
        return 0

    print()
    for f in findings:
        print(f"  COLLAPSED  {f['path']}")
        for r in f["reasons"]:
            print(f"      {r}")
    print()
    print("  A witness that lost this much content is almost certainly a partial")
    print("  write (the producer writes incrementally and was interrupted) rather")
    print("  than a real result. Re-run the producer to completion and re-check.")
    print("  The raw-float64 ratchet will NOT catch this: a gutted witness scores")
    print("  zero raw floats, which reads as a perfect drain (bean qou-h4xk).")
    print()
    print("  If the shrink is real and intended, re-run with --accept and say so")
    print("  in the commit message.")
    return 0 if args.accept else 1


if __name__ == "__main__":
    sys.exit(main())
