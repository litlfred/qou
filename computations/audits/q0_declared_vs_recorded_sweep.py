#!/usr/bin/env python3
"""q0_declared_vs_recorded_sweep.py — does each witness's recorded q₀ pin agree
with the pin its PRODUCER actually runs at?

COMPLEMENTARY TO `q0_anchor_consistency_audit.py`, NOT A REPLACEMENT
    That audit checks the stamp against ITSELF: a witness claiming
    `q0Anchor: "muon"` must carry the muon `q0Value`. That is a real and useful
    check, and it is the one the corpus has.

    It is structurally blind to the flip that actually occurred (2026-08-08,
    `qbeta-ck-cache.witness.json`): the witness carried `q0Anchor: "muon"` AND
    the muon `q0Value` — perfectly self-consistent, verdict Q0_OK — while the
    producer computed at the **proton** pin. The Q_β prediction sat 30.4 ppb
    away from where the label said it was, and the corpus-wide sweep reported
    `Q0_FLIP: 0`.

    The blind spot is structural: self-consistency cannot detect a stamp that is
    internally coherent and externally wrong. This sweep supplies the missing
    axis — recorded pin vs DECLARED pin.

WHAT COUNTS AS EVIDENCE
    Only a POSITIVE declaration may contradict a recorded pin: an explicit
    `QOU_Q0_ANCHOR` env var, or the producer's stem listed in
    `q0_anchor_manifest.json`. `resolve_q0_anchor` alone is not evidence — it
    returns "proton" for every stem ABSENT from the manifest (~470 producers),
    so treating its default as a declaration would flag legitimate muon
    witnesses en masse. Undeclared producers are reported separately as
    UNDETERMINED, which is a coverage gap, not a defect.

VERDICTS
    DECL_OK            recorded pin == declared pin
    DECL_MISMATCH      recorded pin != declared pin   <- the blind-spot class
    UNDETERMINED       producer not positively declared; nothing to check against
    NO_PIN             witness records no q0Anchor
    NO_PRODUCER        witness records no resolvable scriptFile

No fit, nothing wired. Read-only over committed witnesses.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTE_DIR = HERE.parent
REPO = COMPUTE_DIR.parent
sys.path.insert(0, str(COMPUTE_DIR / "substrate"))
sys.path.insert(0, str(COMPUTE_DIR))
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))

from qou_substrate.witness import (  # noqa: E402
    resolve_q0_anchor, q0_anchor_is_declared,
)


def classify(path: Path) -> tuple[str, str]:
    try:
        body = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return "PARSE_ERROR", repr(exc)[:80]
    if not isinstance(body, dict):
        return "PARSE_ERROR", "not an object"

    recorded = body.get("q0Anchor")
    if recorded not in ("muon", "proton"):
        return "NO_PIN", ""

    script = body.get("scriptFile") or body.get("script")
    if not script:
        return "NO_PRODUCER", f"recorded={recorded}"

    # Resolve the producer path by stem; the manifest is keyed on stem anyway.
    stem_path = Path(str(script))
    if not q0_anchor_is_declared(stem_path):
        return "UNDETERMINED", f"recorded={recorded}, producer={stem_path.name}"

    declared, _ = resolve_q0_anchor(stem_path)
    if declared not in ("muon", "proton"):
        return "UNDETERMINED", f"declared={declared}"
    if declared != recorded:
        return "DECL_MISMATCH", (
            f"recorded={recorded} but {stem_path.name} is declared "
            f"{declared}")
    return "DECL_OK", ""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on any DECL_MISMATCH")
    ap.add_argument("--show", type=int, default=25,
                    help="how many mismatch/undetermined lines to print")
    args = ap.parse_args(argv)

    witnesses = sorted(REPO.rglob("*.witness.json"))
    witnesses = [w for w in witnesses if ".git" not in w.parts]

    counts: Counter = Counter()
    mismatches: list[tuple[str, str]] = []
    undetermined: list[str] = []
    for w in witnesses:
        verdict, detail = classify(w)
        counts[verdict] += 1
        rel = str(w.relative_to(REPO))
        if verdict == "DECL_MISMATCH":
            mismatches.append((rel, detail))
        elif verdict == "UNDETERMINED":
            undetermined.append(rel)

    print("=" * 70)
    print("q₀ declared-vs-recorded sweep — the axis the self-consistency")
    print("audit cannot see")
    print("=" * 70)
    print(f"  witnesses scanned    : {len(witnesses)}")
    for k in ("DECL_OK", "DECL_MISMATCH", "UNDETERMINED", "NO_PIN",
              "NO_PRODUCER", "PARSE_ERROR"):
        if counts[k]:
            print(f"  {k:20s} : {counts[k]}")

    if mismatches:
        print(f"\n  DECL_MISMATCH — recorded pin contradicts the declaration:")
        for rel, detail in mismatches[:args.show]:
            print(f"    {rel}\n        {detail}")
        if len(mismatches) > args.show:
            print(f"    … and {len(mismatches) - args.show} more")

    if undetermined:
        print(f"\n  UNDETERMINED ({len(undetermined)}) — a witness records a pin "
              f"but its producer\n  is not in the manifest, so nothing can "
              f"check it. Coverage gap, not a defect;\n  adding the producer to "
              f"q0_anchor_manifest.json brings it under this sweep.")
        for rel in undetermined[:min(args.show, 8)]:
            print(f"    {rel}")
        if len(undetermined) > min(args.show, 8):
            print(f"    … and {len(undetermined) - min(args.show, 8)} more")

    print("\n" + "=" * 70)
    if counts["DECL_MISMATCH"]:
        print(f"{counts['DECL_MISMATCH']} witness(es) carry a pin their producer "
              f"contradicts.")
    else:
        print("No declared-vs-recorded contradictions among checkable witnesses.")
    print(f"Coverage: {counts['DECL_OK'] + counts['DECL_MISMATCH']} checkable, "
          f"{counts['UNDETERMINED']} undeterminable, {counts['NO_PIN']} unpinned.")
    print("=" * 70)

    if args.strict and counts["DECL_MISMATCH"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
