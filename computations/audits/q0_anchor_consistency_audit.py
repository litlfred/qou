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
  Q0_COMPARISON      anchor == "comparison" — the producer reads BOTH pins
                     deliberately, with a q0Values mapping whose every entry
                     was checked against its canonical pin, and a reason
  Q0_COMPARISON_NO_REASON
                     as above but no q0AnchorReason — cannot be told from an
                     accidental straddle without reading the producer
  Q0_COMPARISON_NO_VALUES
                     anchor == "comparison" but fewer than two verifiable
                     {anchor: value} entries — the claim is unchecked
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


# The muon/proton pins agree to 8 digits and then diverge; these prefixes are
# the shortest that separate them.
_EXPECTED_PREFIX = {"muon": "1.109978595557", "proton": "1.109978582751"}


def check_reference_integrity() -> list[str]:
    """Is the audit's own notion of each anchor still correct?

    Without this the audit cannot tell "262 witnesses are wrong" from "my
    reference for what muon MEANS is wrong", and it reports the first when the
    second is true. Measured: 9a9c6b31c7 re-pinned
    `q-pinning-50-digit.witness.json` -- which DEFINES the muon anchor -- to the
    proton value, and this audit then flagged 262 correct muon witnesses as
    flipped. An agent reading that output would go fix 262 files. Bean qou-cezp.
    """
    bad = []
    for anchor, want in _EXPECTED_PREFIX.items():
        got = _qw._q0_value_for_anchor(anchor)
        if got is None:
            bad.append(f"{anchor}: reference pin could not be loaded at all")
        elif not got.startswith(want):
            bad.append(
                f"{anchor}: reference pin is {got[:16]}…, expected {want}… — "
                f"the SOURCE OF TRUTH for the {anchor} anchor is corrupt, so "
                f"every {anchor}-anchored witness below is being compared "
                f"against the wrong value. Fix the reference, not the consumers."
            )
    return bad


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
    if anchor == "comparison":
        # The producer reads MORE THAN ONE anchor deliberately: the comparison
        # IS the subject. Distinct from every other value —
        #   muon/proton   assert ONE pin, and there is no single pin here;
        #   ambiguous     says the pin is UNDETERMINED and queues a manual
        #                 ruling. A deliberate comparison is not undetermined,
        #                 and filing it there mislabels it for whoever drains
        #                 that queue;
        #   independent   would be a FALSE claim of layer-freedom — this
        #                 compute reads q₀ twice.
        # Before this value the four such probes had no honest option and sat
        # in Q0_ANCHOR_MISSING, indistinguishable from producers that forgot
        # (bean qou-po7i).
        #
        # A single `q0Value` is a contradiction here for the same reason it is
        # under `independent`: it asserts the one pin the label denies.
        if body.get("q0Value"):
            return "Q0_FLIP", (
                "anchor=comparison but a single q0Value is recorded "
                f"({str(body['q0Value'])[:16]}…) — a comparison has no ONE pin; "
                "record each under q0Values"
            )
        values = body.get("q0Values")
        if not isinstance(values, dict) or len(values) < 2:
            return "Q0_COMPARISON_NO_VALUES", (
                "anchor=comparison without a q0Values mapping of at least two "
                "{anchor: value} entries — the claim is that two or more pins "
                "were read, so the values read are what make it checkable"
            )
        # This is the one label the audit can VERIFY rather than take on trust.
        # `independent` is an assertion about an import cone; `comparison`
        # names pins, and each named pin either matches its canonical value or
        # does not.
        for a, v in sorted(values.items()):
            if a not in ("muon", "proton"):
                return "Q0_FLIP", f"q0Values has unknown anchor {a!r}"
            canon = _canonical(a)
            if canon is None:
                return "Q0_COMPARISON_NO_VALUES", (
                    f"cannot load canonical {a} pin to check q0Values")
            if str(v)[:_MATCH_PREFIX] != canon:
                return "Q0_FLIP", (
                    f"q0Values[{a}]={str(v)[:16]}… (expected {canon}…) — a "
                    "comparison mislabelling one of its own legs is the "
                    "flip-flop bug with extra steps"
                )
        if not str(body.get("q0AnchorReason") or "").strip():
            return "Q0_COMPARISON_NO_REASON", (
                "anchor=comparison with no q0AnchorReason — states that two "
                "pins were read on purpose, but not what is being compared, "
                "so a reader cannot tell it from an accidental straddle"
            )
        return "Q0_COMPARISON", ""
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

    ref_bad = check_reference_integrity()
    if ref_bad:
        print("=" * 74)
        print("🛑 REFERENCE CORRUPTION — do NOT treat any row below as a finding")
        print("=" * 74)
        for m in ref_bad:
            print(f"  {m}")
        print()
        print("  `computations/q-pinning-50-digit.witness.json` DEFINES the muon")
        print("  anchor; the qou-substrate package constant defines proton. One")
        print("  of them is wrong, and every consumer would be measured against")
        print("  it — so this audit stops here rather than reporting hundreds of")
        print("  correct witnesses as flipped. Fix the reference. Bean qou-cezp.")
        return 1

    by_verdict: dict[str, list[dict]] = {}
    for wp in sorted((HERE.parent).rglob("*.witness.json")):
        if "_deprecated" in wp.parts:
            continue
        verdict, detail = classify(wp)
        by_verdict.setdefault(verdict, []).append(
            {"witness": wp.name, "detail": detail}
        )

    order = ["Q0_OK", "Q0_AMBIGUOUS", "Q0_INDEPENDENT",
             "Q0_INDEPENDENT_NO_REASON", "Q0_COMPARISON",
             "Q0_COMPARISON_NO_REASON", "Q0_COMPARISON_NO_VALUES",
             "Q0_ANCHOR_MISSING",
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
