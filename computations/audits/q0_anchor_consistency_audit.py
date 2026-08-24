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


def payload_mislabels(path: Path) -> list[dict]:
    """Fields whose NAME says one anchor while the VALUE is the other one's pin.

    The `Q0_OK`/`Q0_FLIP` verdicts compare the *envelope* (`q0Anchor` vs
    `q0Value`) and never look inside `data`. That is correct for what they
    test, and it leaves a seam: a probe that evaluates BOTH anchors and labels
    one of them wrong is Q0_OK, because its envelope is self-consistent.

    Measured instance (bean `qou-cds3`, 22 witnesses):
    `probes/flavor-split-alpha-dilog-expansion.witness.json` is Q0_OK with
    `q0Anchor: "muon"` matching its `q0Value`, while `data/proton_anchor/q0`
    holds that same *muon* value.

    Diagnostic only — printed, never written to the witness and never able to
    change the exit code. The `Q0_FLIP` gate is CI-failing, and 22 known hits
    would fail the build before the migration that fixes them is authorised.
    """
    out: list[dict] = []
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001 — classify() already reports parse errors
        return out

    def walk(node, jp=""):
        if isinstance(node, dict):
            for k, v in node.items():
                # Use the NEAREST anchor-bearing path segment, not just the
                # immediate key: `/data/proton_anchor/q0` names its anchor on
                # the parent, and keying on `k` alone silently misses it.
                named = _anchor_in_path(f"{jp}/{k}")
                if named is not None and not isinstance(v, (dict, list)):
                    got = _anchor_of_value(str(v))
                    if got is not None and got != named:
                        out.append({
                            "witness": path.name,
                            "field": f"{jp}/{k}",
                            "name_says": named,
                            "value_is": got,
                            "value": str(v)[:34],
                        })
                walk(v, f"{jp}/{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{jp}[{i}]")

    walk(doc)
    return out


def _anchor_in_path(jp: str) -> str | None:
    """Innermost path segment naming an anchor wins.

    `/data/proton_anchor/q0` -> proton.  `/q0_pins/muon` -> muon.  Innermost so
    that a correctly-labelled pair nested under a differently-named parent is
    read by its own label rather than its container's.
    """
    for seg in reversed(jp.split("/")):
        sl = seg.lower()
        if "proton" in sl:
            return "proton"
        if "muon" in sl:
            return "muon"
    return None


def _anchor_of_value(v: str) -> str | None:
    """Which anchor's pin does this literal carry, if any?"""
    pref = v[:_MATCH_PREFIX]
    for anchor, want in _EXPECTED_PREFIX.items():
        if pref == want:
            return anchor
    return None


def envelope_vs_payload(path: Path) -> dict | None:
    """The stamped anchor's value appears NOWHERE in the payload, the other's does.

    A THIRD seam, distinct from both existing checks and caught by neither:

      * `Q0_OK` / `Q0_FLIP` compare envelope to envelope — `q0Anchor` against
        `q0Value`. Both can be perfectly self-consistent while the numbers were
        computed at the other pin.
      * `payload_mislabels` compares a field's NAME to its VALUE inside `data`.
        It is silent when the name and value agree — `data.q_proton` holding the
        proton pin is correct by that test.

    So a witness stamped `muon`, whose `q0Value` is the canonical muon pin, and
    whose payload contains only proton-valued fields correctly named `q_proton`,
    passes both. Measured instance (bean `qou-cds3`, 2026-08-23): six witnesses
    regenerated by producers listed `ideal_muon` in `q0_anchor_manifest.json` —
    so `WitnessBuilder` stamped them muon — while every one imports `q_at` from
    `qou_substrate.constants`, which the manifest auto-select never rebinds, so
    they compute at proton. All six were `Q0_OK` with zero payload mislabels.

    Reported only when the evidence is unambiguous: the other anchor's pin is
    present AND the stamped anchor's is absent. A witness with no q0-shaped
    payload yields no evidence either way and is not reported.

    Diagnostic only, like `payload_mislabels` — printed, never written to the
    witness, never able to change the exit code.
    """
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001 — classify() already reports parse errors
        return None
    if not isinstance(doc, dict):
        return None
    anchor = doc.get("q0Anchor")
    if anchor not in ("muon", "proton"):
        return None
    other = "proton" if anchor == "muon" else "muon"
    want_self, want_other = _EXPECTED_PREFIX[anchor], _EXPECTED_PREFIX[other]
    saw_self, saw_other = [], []
    def walk(o, trail):
        if isinstance(o, dict):
            for k, v in o.items():
                walk(v, trail + [str(k)])
        elif isinstance(o, list):
            for i, v in enumerate(o):
                walk(v, trail + [str(i)])
        else:
            t = str(o)
            if t.startswith(want_self):
                saw_self.append(".".join(trail))
            elif t.startswith(want_other):
                saw_other.append(".".join(trail))
    for key in ("data", "parameters"):
        if key in doc:
            walk(doc[key], [key])
    if saw_other and not saw_self:
        return {
            "witness": str(path),
            "stamped": anchor,
            "computed": other,
            "fields": saw_other[:6],
            "why": (f"q0Anchor={anchor} and q0Value matches the {anchor} pin, but "
                    f"the payload carries only {other}-pin values "
                    f"({', '.join(saw_other[:3])}) — the envelope is "
                    f"self-consistent and describes a different anchor than the "
                    f"numbers were computed at"),
        }
    return None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict", action="store_true",
        help="Exit 1 if any Q0_FLIP witnesses are found (CI gate).",
    )
    parser.add_argument(
        "--payload-check", action="store_true",
        help="Also report fields INSIDE data whose name says one anchor while "
             "the value carries the other's pin — the seam Q0_OK/Q0_FLIP "
             "cannot see, since they compare only q0Anchor vs q0Value. "
             "Diagnostic: printed, not written to the witness, and cannot "
             "change the exit code.",
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

    if args.payload_check:
        mis = [m
               for w in sorted((HERE.parent).rglob("*.witness.json"))
               for m in payload_mislabels(w)]
        print("\n" + "=" * 74)
        print("  payload anchor-label check (--payload-check, diagnostic only)")
        print("=" * 74)
        print(f"  fields whose NAME and VALUE disagree on the anchor: {len(mis)}")
        print(f"  witnesses affected: {len({m['witness'] for m in mis})}")
        for m in mis[:25]:
            print(f"    {m['witness'][:44]:46} {m['field'][:30]:32} "
                  f"name={m['name_says']:6} value={m['value_is']}")
        if len(mis) > 25:
            print(f"    … and {len(mis) - 25} more")

        # The THIRD seam: envelope self-consistent, payload computed at the
        # other anchor. Neither Q0_OK/Q0_FLIP (envelope vs envelope) nor the
        # check above (field name vs field value) can see it.
        env = [e for w in sorted((HERE.parent).rglob("*.witness.json"))
               if "_deprecated" not in w.parts
               for e in ([envelope_vs_payload(w)] if envelope_vs_payload(w) else [])]
        print()
        print(f"  envelope-vs-payload mismatches: {len(env)}")
        print("    (q0Anchor + q0Value agree with each other, but every q0-shaped")
        print("     value in the payload belongs to the OTHER anchor)")
        for e in env[:25]:
            print(f"    {Path(e['witness']).name[:52]:54} "
                  f"stamped={e['stamped']:6} payload={e['computed']}")
        if len(env) > 25:
            print(f"    … and {len(env) - 25} more")

        print("\n  Exit code unchanged — Q0_FLIP remains the only gate.")

    if args.strict and n_flip:
        print(f"\nFAIL (--strict): {n_flip} Q0_FLIP witness(es).")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
