#!/usr/bin/env python3
"""Which committed `q0Anchor` stamps would SURVIVE a re-run of their producer?

A witness can carry `q0Anchor` on disk and have no way to get it back. The
573-witness backfill `b8eb7d9e66d` wrote into FILES; whether the field returns
depends on the producer, and for some it does not. Those stamps are one re-run
from vanishing, and the producers most at risk are the ones that cannot
currently run -- their loss has simply never been triggered.

WHY NOT A GREP. The obvious audit asks whether the producer's source contains
the string "q0Anchor". That is wrong, and wrong in the flattering direction:
`WitnessBuilder.save` stamps the field itself (witness.py:1599), so a producer
using the builder emits it with no literal anywhere in its own source. A
source-text sweep counted 715 of 817 as at-risk; the true number is far lower,
and that figure is retracted (bean `qou-cq2n`).

THE ACTUAL RULE, from `witness.py:1590-1605`: the builder stamps only when the
pin is POSITIVELY DECLARED for that producer -- an env var, or an entry in
`q0_anchor_manifest.json`. Undeclared producers are deliberately left unstamped,
because "defaulting one in would assert a pin nobody established". So a stamp
reproduces when EITHER:

  (a) the producer writes `q0Anchor` itself, or
  (b) the producer is manifest-declared AND reaches `WitnessBuilder.save`.

Anything else on disk is a backfill artifact that a re-run drops.

Run: `python3 computations/audits/q0_anchor_reproducibility_audit.py [--selftest]`
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # computations/
MANIFEST = ROOT / "q0_anchor_manifest.json"


def manifest_stems() -> set[str]:
    """Producer stems with a positively-declared pin."""
    d = json.loads(MANIFEST.read_text())
    stems: set[str] = set()
    for key, val in d.items():
        if key.startswith("_") or not isinstance(val, list):
            continue
        stems |= {str(x) for x in val}
    return stems


def uses_builder(src: str) -> bool:
    """Does this producer reach `WitnessBuilder.save`?

    Deliberately textual on the BUILDER, not on the field: a producer that
    imports WitnessBuilder and calls `.save(` is on the stamping path whatever
    it names its variable. The failure mode this misses -- a builder reached
    only through a helper module -- makes the audit report a stamp as at-risk
    when it is safe, i.e. it over-reports rather than under-reports.
    """
    return "WitnessBuilder" in src and ".save(" in src


def find_producer(witness: Path, body: dict) -> Path | None:
    sf = body.get("scriptFile") or body.get("computation")
    if sf:
        name = Path(str(sf)).name
        for cand in (name, Path(name).stem + ".py"):
            hits = list(ROOT.rglob(cand))
            if hits:
                return hits[0]
    stem = witness.name.replace(".witness.json", "").replace("-", "_")
    hits = list(ROOT.rglob(stem + ".py"))
    return hits[0] if hits else None


def classify(witness: Path, stems: set[str]):
    try:
        body = json.loads(witness.read_text())
    except Exception:
        return None
    if not isinstance(body, dict) or "q0Anchor" not in body:
        return None
    prod = find_producer(witness, body)
    if prod is None:
        return ("producer-not-found", None)
    src = prod.read_text(errors="ignore")
    if "q0Anchor" in src:
        return ("reproduces: producer writes it", prod)
    if prod.stem in stems and uses_builder(src):
        return ("reproduces: manifest + builder", prod)
    if uses_builder(src):
        return ("AT RISK: builder, but not manifest-declared", prod)
    return ("AT RISK: hand-built witness, never stamped", prod)


def main(argv) -> int:
    stems = manifest_stems()
    buckets: dict[str, list] = {}
    for w in sorted(ROOT.rglob("*.witness.json")):
        got = classify(w, stems)
        if got is None:
            continue
        buckets.setdefault(got[0], []).append((w.name, got[1]))

    total = sum(len(v) for v in buckets.values())
    print(f"manifest-declared producer stems : {len(stems)}")
    print(f"witnesses carrying q0Anchor      : {total}\n")
    for k in sorted(buckets, key=lambda k: -len(buckets[k])):
        print(f"  {len(buckets[k]):>5}  {k}")
    risk = sum(len(v) for k, v in buckets.items() if k.startswith("AT RISK"))
    print(f"\n  => {risk} stamp(s) would NOT survive a re-run "
          f"({100*risk/total:.0f}% of {total})")
    for k, v in buckets.items():
        if k.startswith("AT RISK"):
            print(f"\n  {k}:")
            for n, p in v[:10]:
                print(f"    {n}  <- {p.name if p else '?'}")
            if len(v) > 10:
                print(f"    ... and {len(v)-10} more")

    if "--selftest" in argv:
        # Calibrated on answers established by hand. Without this the audit
        # could be narrowed into reporting a clean tree, which is exactly how
        # the retracted grep failed.
        ok = True
        for stem, expect in (("su4_1111_markov_trace_probe", "reproduces"),
                             ("pentagon_rt_torus_knot_higgs_probe", "reproduces")):
            hits = [k for k, v in buckets.items()
                    for n, p in v if p and p.stem == stem]
            got = hits[0] if hits else "(not classified)"
            good = got.startswith(expect)
            ok &= good
            print(f"  selftest {stem}: {got}  {'OK' if good else 'FAIL'}")
        if not ok:
            print("SELFTEST FAILED"); return 1
        print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
