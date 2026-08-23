#!/usr/bin/env python3
"""q0_anchor_payload_recovery.py — recover a witness's q₀ anchor from its OWN
payload, for the witnesses that carry no ``q0Anchor`` field.

WHY THIS EXISTS
    As of 2026-08-19 there are ~1905 ``computations/**/*.witness.json`` with no
    ``q0Anchor``. The standing framing of that tranche is *"inspect each
    producer to learn which pin it used"* — expensive, and it needs rule-4
    sign-off before anything may be rewritten.

    There is a cheaper question that had not been asked: **what does the
    witness already say?** A large minority already record the 50-digit q₀ they
    were computed at — just under an ad-hoc key (``q0``, ``q_0_50dps``,
    ``q_proton``, ``q_0``, ``q``, ``Q_0``, ``q0_50dps``, …) instead of the
    canonical ``q0Anchor`` / ``q0Value`` pair. For those, the anchor is
    recoverable by transcription: no producer analysis, no re-run, no
    recomputation, and therefore no numerical risk.

    Measured on the 2026-08-19 corpus: 305 unambiguous (186 proton, 119 muon)
    plus 25 carrying BOTH prefixes.

🛑 THE ``both`` BUCKET IS NOT AN AMBIGUITY TO RESOLVE
    A witness carrying both prefixes is a deliberate **cross-anchor comparison**
    — e.g. ``tau-dictionary-hauptmodul-validator`` has literal ``muon`` and
    ``proton`` keys side by side. The owner ruling of 2026-08-08 (bean
    ``qou-pin2``) is that explicit comparison probes are legitimate and "must
    not be fixed". This script reports them as ``both`` and **never** proposes
    a label for them; they need an explicit *exclusion* from any migration
    batch, not a resolution to one pin.

🛑 THIS SCRIPT NEVER WRITES A WITNESS
    It emits a proposal. Applying it is a separate, reviewed step. That
    separation is the same one ``q0_producer_pin_classifier.py`` enforces for
    the manifest, and for the same reason: a wrong label destroys information
    that was previously correct-but-unlabelled.

NO FLOAT
    Every comparison here is a string-prefix test on the serialized 50-digit
    decimal. Nothing is parsed to a float, so this file has no precision
    surface at all — deliberately, since the whole point is to read what was
    recorded rather than to recompute it.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent
REPO = COMPUTE_DIR.parent

# The two pins, as serialized-decimal prefixes. Long enough to separate them
# (they agree to 1.10997858/1.10997859) and short enough to match a value
# serialized at any dps >= 13.
# 11 digits after the point, NOT 12 — deliberately.
#
# The corpus carries TWO muon values agreeing to 11 digits and diverging at the
# 12th (`q0_muon_population_partition.py` on main):
#     current     1.10997859555733471989…
#     superseded  1.10997859555418057528…   ("the old muon value")
# The first draft of this file used the 12-digit prefix "1.109978595557", which
# matches the current value and MISSES every witness still carrying the
# superseded one — counting them as "no pin in payload" and so shunting them
# into the expensive producer-analysis bucket they do not belong in.
MUON_PREFIX = "1.10997859555"
PROTON_PREFIX = "1.109978582751"

# Kept BYTE-IDENTICAL to q0_anchor_consistency_audit.AUDIT_SUFFIXES. These are
# state-tracking witnesses ABOUT the corpus, not computations in it; they have
# no q₀ of their own and are exempt there, so they must be exempt here too.
# Measured cost of omitting this: the population reads 1964 instead of 1905.
AUDIT_SUFFIXES = (
    "-audit.witness.json",
    "-scan.witness.json",
    "-compliance.witness.json",
)


def _strings(node, path=""):
    """Yield (dotted-path, string) for every string leaf in the payload."""
    if isinstance(node, dict):
        for k, v in node.items():
            yield from _strings(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for v in node:
            yield from _strings(v, f"{path}[]")
    elif isinstance(node, str):
        yield path, node


def classify_payload(body) -> tuple[str, list[tuple[str, str]]]:
    """Return (verdict, evidence) where verdict is muon / proton / both / none.

    Evidence is a list of (key, pin) for every place a pin prefix was found.
    A NUMBER that happens to be a q₀ is not evidence: mpmath-serialized q₀ is
    written as a string throughout this corpus, and a float leaf could not
    carry 50 digits anyway.
    """
    ev = []
    for key, s in _strings(body):
        if MUON_PREFIX in s:
            ev.append((key, "muon"))
        if PROTON_PREFIX in s:
            ev.append((key, "proton"))
    pins = {p for _, p in ev}
    if not pins:
        return "none", []
    if pins == {"muon", "proton"}:
        return "both", ev
    return pins.pop(), ev


def iter_anchor_missing():
    for p in sorted(COMPUTE_DIR.rglob("*.witness.json")):
        # Match q0_anchor_consistency_audit.py exactly. Without this skip the
        # population is 2275 rather than 1905 — 370 _deprecated witnesses that
        # the audit does not count and that nobody should be labelling.
        if "_deprecated" in p.parts:
            continue
        if any(p.name.endswith(suf) for suf in AUDIT_SUFFIXES):
            continue
        try:
            body = json.loads(p.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            continue
        if not isinstance(body, dict):
            continue
        if body.get("q0Anchor"):
            continue
        yield p, body


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--emit-proposal", type=str, default=None,
                    help="write the recoverable labels to this JSON path "
                         "(a PROPOSAL — nothing is applied)")
    ap.add_argument("--show", type=int, default=12)
    args = ap.parse_args(argv)

    counts = Counter()
    keys = Counter()
    proposal = []
    both = []
    for path, body in iter_anchor_missing():
        verdict, ev = classify_payload(body)
        counts[verdict] += 1
        rel = str(path.relative_to(REPO))
        for k in {k.split(".")[-1].replace("[]", "") for k, _ in ev}:
            keys[k] += 1
        if verdict in ("muon", "proton"):
            proposal.append({
                "witness": rel,
                "q0Anchor": verdict,
                "recovered_from": sorted({k for k, _ in ev})[:4],
            })
        elif verdict == "both":
            both.append({"witness": rel,
                         "keys": sorted({k for k, _ in ev})[:6]})

    total = sum(counts.values())
    print("=" * 72)
    print("q₀ anchor recovery from witness payload")
    print("=" * 72)
    print(f"  witnesses with no q0Anchor        : {total}")
    print(f"  RECOVERABLE by transcription      : {counts['muon'] + counts['proton']}")
    print(f"      proton                        : {counts['proton']}")
    print(f"      muon                          : {counts['muon']}")
    print(f"  cross-anchor comparison (EXCLUDE) : {counts['both']}")
    print(f"  no pin in payload                 : {counts['none']}")

    print(f"\n  the key it was recorded under — DISTINCT WITNESSES (top {args.show}):")
    for k, n in keys.most_common(args.show):
        print(f"    {n:5d}  {k}")

    if both:
        print(f"\n  🛑 cross-anchor comparison probes — never propose a label "
              f"for these ({len(both)}):")
        for b in both[:args.show]:
            print(f"    {b['witness']}")
        if len(both) > args.show:
            print(f"    … and {len(both) - args.show} more")

    if args.emit_proposal:
        out = {
            "schema": "q0-anchor-payload-recovery/v1",
            "note": "PROPOSAL ONLY — applying it is a separate reviewed step.",
            "recoverable": proposal,
            "excluded_cross_anchor": both,
        }
        Path(args.emit_proposal).write_text(
            json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"\n  proposal written: {args.emit_proposal} "
              f"({len(proposal)} labels, {len(both)} exclusions)")

    print("\n" + "=" * 72)
    print("This script never writes a witness. A wrong label destroys")
    print("information that was previously correct-but-unlabelled.")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
