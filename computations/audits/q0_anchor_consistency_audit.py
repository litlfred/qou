#!/usr/bin/env python3
"""q₀-anchor consistency audit — the muon/proton "flip-flop" detector.

Every witness value is computed at one of two documented q₀ pins (muon-anchored
canonical vs proton-anchored physical, ~11.5 ppb apart). PR #4020 makes the pin
explicit on each witness via `q0Anchor` + `q0Value`. This audit enforces that the
recorded pin is *self-consistent*: a witness that claims `q0Anchor: "muon"` must
carry the muon `q0Value` (and likewise proton). A mismatch is a flip — the exact
bug (bean tnjb) where a value drifts to the wrong anchor.

Verdicts:
  Q0_OK              anchor ∈ {muon,proton} and q0Value matches that anchor's pin
  Q0_FLIP            anchor and q0Value disagree  ← CI-FAILING (the flip)
  Q0_AMBIGUOUS       anchor == "ambiguous" (producer genuinely undetermined)
  Q0_INDEPENDENT     anchor == "independent" WITH a q0AnchorReason saying why
  Q0_INDEPENDENT_NO_REASON
                     anchor == "independent" but no q0AnchorReason — the claim
                     is unverifiable without re-deriving the producer's import
                     cone, which is the work the declaration should have saved
  Q0_ANCHOR_MISSING  no q0Anchor field yet (pre-backfill; not a failure)
  Q0_VALUE_MISSING   anchor present but no q0Value to check
  Q0_AUDIT_EXEMPT    audit/scan/compliance state-tracking witnesses

`independent` vs `ambiguous` — they are not the same state, and collapsing them
loses the distinction this field exists to record:

  ambiguous   the producer DOES depend on q₀, but which pin is undetermined —
              `gen_q0_anchor_manifest.py` assigns it when a witness carries BOTH
              the muon and the proton signature. It is a queue for a manual
              ruling.
  independent the producer never reads q₀. There is nothing to rule on, and no
              `q0Value` exists to record. Stamping `proton` here — the standing
              default for new compute — would assert a layer the numbers do not
              belong to, which is the misrecord this whole field guards against.

Before `independent` existed, a q₀-free producer had no way to say so: the
manifest generator drops it (`# neither: no q₀ field — omit`), so
`q0_anchor_is_declared` is False, nothing is stamped, and it lands in
Q0_ANCHOR_MISSING — indistinguishable from a producer that simply forgot. That
is the state bean qou-rw91 caught (three probes) and bean qou-pin1 hit earlier
on `chi-deuteron-h6` (a purely symbolic artifact, still unstamped today).

`independent` is PRODUCER-DECLARED ONLY — `w.save({"q0Anchor": "independent"})`.
It is deliberately not inferrable from the manifest: "witness records no q₀
value" does not imply "compute never used q₀" (a producer can use q₀ and simply
not serialize it), so auto-classifying would manufacture false independence
claims. An agent must read the import cone and assert it.

Usage:
    python3 q0_anchor_consistency_audit.py            # report
    python3 q0_anchor_consistency_audit.py --strict   # exit 1 on any Q0_FLIP

Emits `q0-anchor-consistency-audit.witness.json`.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))
from witness_base import WitnessBuilder  # noqa: E402
import qou_substrate.witness as _qw  # noqa: E402

AUDIT_SUFFIXES = (
    "-audit.witness.json",
    "-scan.witness.json",
    "-compliance.witness.json",
)

# How many leading digits of q0Value must agree with the anchor's canonical pin.
# The muon/proton pins first differ at digit ~9 (…8595557 vs …8582751), so 12
# significant digits is a safe, unambiguous discriminator.
_MATCH_PREFIX = 14  # includes "1.109978XXXX"


def _canonical(anchor: str) -> str | None:
    v = _qw._q0_value_for_anchor(anchor)
    return v[:_MATCH_PREFIX] if v else None


def classify(path: Path) -> tuple[str, str]:
    if any(path.name.endswith(suf) for suf in AUDIT_SUFFIXES):
        return "Q0_AUDIT_EXEMPT", ""
    try:
        body = json.loads(path.read_text())
    except (json.JSONDecodeError, OSError) as exc:
        return "Q0_PARSE_ERROR", str(exc)
    if not isinstance(body, dict):
        return "Q0_PARSE_ERROR", "root is not an object"
    anchor = body.get("q0Anchor")
    if not anchor:
        return "Q0_ANCHOR_MISSING", ""
    if anchor == "ambiguous":
        return "Q0_AMBIGUOUS", ""
    if anchor == "independent":
        # No q₀ was read, so there is no value to cross-check. A q0Value here
        # is a contradiction, not a bonus: it means something DID supply a pin.
        if body.get("q0Value"):
            return "Q0_FLIP", (
                "anchor=independent but a q0Value is recorded "
                f"({str(body['q0Value'])[:16]}…) — the producer reads q₀ after all"
            )
        # The token alone is a thin record. A reader who opens the witness and
        # finds only `"independent"` has to re-derive the import cone to check
        # it — the exact work the declaration exists to save. Counted apart so
        # a thin declaration cannot pass as a complete one; same reasoning that
        # keeps Q0_INDEPENDENT itself counted beside Q0_ANCHOR_MISSING rather
        # than letting a declaration shrink the inventory into silence
        # (bean qou-mw1p, from design advice on PR #5124).
        if not str(body.get("q0AnchorReason") or "").strip():
            return "Q0_INDEPENDENT_NO_REASON", (
                "anchor=independent with no q0AnchorReason — states that q₀ is "
                "never read, but not why, so the claim cannot be checked "
                "without re-deriving the import cone"
            )
        return "Q0_INDEPENDENT", ""
    if anchor not in ("muon", "proton"):
        return "Q0_FLIP", f"unknown anchor {anchor!r}"
    value = body.get("q0Value")
    if not value:
        return "Q0_VALUE_MISSING", f"anchor={anchor}"
    canon = _canonical(anchor)
    if canon is None:
        return "Q0_VALUE_MISSING", f"cannot load canonical {anchor} pin"
    if str(value)[:_MATCH_PREFIX] != canon:
        return "Q0_FLIP", (
            f"anchor={anchor} but q0Value={str(value)[:16]}… "
            f"(expected {canon}…)"
        )
    return "Q0_OK", ""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict", action="store_true",
        help="Exit 1 if any Q0_FLIP witnesses are found (CI gate).",
    )
    args = parser.parse_args(argv)

    by_verdict: dict[str, list[dict]] = {}
    for wp in sorted((HERE.parent).rglob("*.witness.json")):
        if "_deprecated" in wp.parts:
            continue
        verdict, detail = classify(wp)
        by_verdict.setdefault(verdict, []).append(
            {"witness": wp.name, "detail": detail}
        )

    order = ["Q0_OK", "Q0_AMBIGUOUS", "Q0_INDEPENDENT",
             "Q0_INDEPENDENT_NO_REASON", "Q0_ANCHOR_MISSING",
             "Q0_VALUE_MISSING", "Q0_AUDIT_EXEMPT", "Q0_PARSE_ERROR", "Q0_FLIP"]
    n = {k: len(by_verdict.get(k, [])) for k in order}
    n_flip = n["Q0_FLIP"]

    print("=" * 70)
    print("q₀-anchor consistency audit — muon/proton flip detector")
    print("=" * 70)
    for k in order:
        print(f"  {k:20}: {n[k]}")
    if n_flip:
        print("\n🛑 Q0_FLIP (anchor ≠ value — the flip-flop bug):")
        for r in by_verdict["Q0_FLIP"][:25]:
            print(f"  - {r['witness']}: {r['detail']}")
        if n_flip > 25:
            print(f"  ... (+ {n_flip - 25} more)")

    builder = (
        WitnessBuilder("q0-anchor-consistency-audit", engine="python")
        .set_description(
            "Flip-flop detector: enforces that each witness's q0Value matches "
            "the canonical pin for its q0Anchor (muon vs proton). Q0_FLIP is a "
            "CI-failing anchor/value disagreement. Anchor recording landed in "
            "PR #4020. Q0_INDEPENDENT records a producer that never reads q₀ "
            "at all — a positive, producer-declared statement, distinct from "
            "Q0_AMBIGUOUS (depends on q₀, pin undetermined) and from "
            "Q0_ANCHOR_MISSING (nothing recorded)."
        )
    )
    builder.add_data("counts", n)
    builder.add_data("match_prefix_digits", _MATCH_PREFIX)
    builder.add_data("by_verdict", by_verdict)
    builder.add_assertion(
        "no_q0_flip", computed=n_flip, expected=0, tolerance=0,
        source="every witness's q0Value must match its q0Anchor's canonical pin",
    )
    builder.save()

    if args.strict and n_flip:
        print(f"\nFAIL (--strict): {n_flip} Q0_FLIP witness(es).")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
