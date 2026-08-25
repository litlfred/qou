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
import re as _re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # computations/
MANIFEST = ROOT / "q0_anchor_manifest.json"



# ── can a manifest entry actually fix it? ───────────────────────────────
#
# "Just add manifest entries" is the obvious remediation for the
# builder-but-undeclared bucket, and for a quarter of it that would be a LIE:
# the producer never consults the manifest, so an entry declares a pin it does
# not obey. Measured, per DISTINCT PRODUCER rather than per witness -- 241
# witnesses are only 93 producers, and one of them (`canonical_isotope_witness`)
# accounts for 120 of the witnesses, so a per-witness rate is dominated by a
# single file. That distortion is the one AGENTS.md records costing a 39%-vs-73%
# swing on the staleness census; counting producers is what avoids it.
_ANCHOR_READ = _re.compile(r"q[-_]pinning[-_]50[-_]digit|q_pinning_50_digit")
_QPARAM = _re.compile(r"from\s+q_parameter\s+import|q_parameter\.")
_HARDCODE = _re.compile(r"1\.10997858\d|1\.10997859\d")


def manifest_efficacy(src: str) -> str:
    """Would a `q0_anchor_manifest.json` entry change this producer's pin?

    EFFECTIVE only when the producer reads `q_parameter`, which is what
    consults the manifest. A producer that reads the anchor-defining witness
    directly (the `qou-aj91` class, 85 corpus-wide) or hardcodes a literal
    resolves its q0 with the manifest out of the loop entirely.
    """
    if _ANCHOR_READ.search(src):
        return "INERT: reads the anchor witness directly (qou-aj91)"
    if _QPARAM.search(src):
        return "EFFECTIVE: reads q_parameter"
    if _HARDCODE.search(src):
        return "INERT: hardcoded q0 literal"
    return "UNKNOWN: no visible q0 source (indirect/helper)"


def declarable_proton(buckets) -> list[str]:
    """Producer stems in the at-risk builder bucket that a `physical_proton`
    entry would fix TRUTHFULLY.

    The entry is safe because it is a RUNTIME NO-OP. An undeclared producer
    already resolves proton -- `q_parameter.py:100-113` and `witness.py:324`
    both default not-in-`ideal_muon` to proton -- so adding the stem changes
    `q0_anchor_is_declared` False->True and nothing else. Verified directly:
    `resolve_q0_anchor` returns "proton" before and after. The entry does not
    re-pin anything; it records the pin the producer was already using, which
    is the whole reason this is not the `qou-1c4y` bulk migration.

    Scoped to EFFECTIVE producers: one that hardcodes q0 or reads the anchor
    witness directly never consults the manifest, so an entry there would
    assert a pin it does not obey.
    """
    stems: list[str] = []
    for k, v in buckets.items():
        if not k.startswith("AT RISK: builder"):
            continue
        for _n, prod in v:
            if prod is None:
                continue
            if manifest_efficacy(prod.read_text(errors="ignore")).startswith("EFFECTIVE"):
                stems.append(prod.stem)
    return sorted(set(stems))


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

    if "--by-producer" in argv:
        # The remediation view: group the at-risk builder bucket by producer and
        # by whether a manifest entry would even reach it.
        from collections import Counter
        pw, pk = Counter(), {}
        for k, v in buckets.items():
            if not k.startswith("AT RISK: builder"):
                continue
            for _n, prod in v:
                if prod is None:
                    continue
                pw[prod.stem] += 1
                pk.setdefault(prod.stem, manifest_efficacy(prod.read_text(errors="ignore")))
        cp, cw = Counter(), Counter()
        for stem, k in pk.items():
            cp[k] += 1
            cw[k] += pw[stem]
        print(f"\n  builder-but-undeclared, BY PRODUCER: {len(pk)} producers, "
              f"{sum(cw.values())} witnesses")
        for k in sorted(cp, key=lambda k: -cp[k]):
            print(f"    {cp[k]:>4} producers {cw[k]:>5} witnesses  {k}")
        inert = sum(cp[k] for k in cp if k.startswith("INERT"))
        if pk:
            print(f"    => {inert} of {len(pk)} producers "
                  f"({100*inert//len(pk)}%) cannot be fixed by a manifest entry")
        for stem, n in pw.most_common(3):
            print(f"       heaviest: {stem} ({n} witnesses)")

    if "--declare-proton" in argv:
        cand = declarable_proton(buckets)
        d = json.loads(MANIFEST.read_text(encoding="utf-8"))
        already = {s for k, v in d.items()
                   if not k.startswith("_") and isinstance(v, list) for s in v}
        new = [s for s in cand if s not in already]
        print(f"\n  --declare-proton: {len(cand)} EFFECTIVE at-risk producer(s), "
              f"{len(new)} not yet declared")
        for s in new:
            print(f"    + {s}")
        if "--apply" in argv and new:
            d["physical_proton"] = sorted(set(d.get("physical_proton", [])) | set(new))
            MANIFEST.write_text(
                json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"  applied: physical_proton now {len(d['physical_proton'])} stems")
        elif new:
            print("  (dry run -- pass --apply to write)")

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
