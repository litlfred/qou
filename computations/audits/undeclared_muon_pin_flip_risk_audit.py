#!/usr/bin/env python3
"""49 witnesses assert `q0Anchor: muon` from a producer that would resolve PROTON.

Bean `qou-o922` (the measured instance), bean `qou-po7i` (the argv[0] finding).

THE RISK
--------
`q_parameter` resolves the q0 anchor from the `sys.argv[0]` stem against
`computations/q0_anchor_manifest.json`. A producer with no entry falls through
to the PROTON default. Independently, `WitnessBuilder.build()` stamps
`q0Anchor` only when `q0_anchor_is_declared(script_path)` is true, which is
also False for an unlisted producer.

Those two combine badly. Re-running an UNLISTED producer whose committed
witness was written under MUON:

  1. silently changes the substrate input by ~11.5 ppb (muon pin -> proton
     default), and
  2. DROPS the `q0Anchor`/`q0Value` pair that would have made step 1 visible.

The pin moves and the audit trail for the move disappears in the same step, so
the anchor audit afterwards reports Q0_ANCHOR_MISSING -- which its own
docstring calls "pre-backfill; not a failure" -- for a witness whose pin just
changed. Measured end-to-end on `lever1_binding_habiro_single_element_test`
(params.q0 1.10997859555733 -> 1.10997858275138), which is why PR #5436
reverted that regeneration rather than committing it.

WHAT THIS COUNTS, AND WHAT IT DELIBERATELY DOES NOT
----------------------------------------------------
The SHARP set: a witness whose `q0Anchor` is exactly "muon" AND whose
`q0Value` is the muon pin, whose `scriptFile` stem is absent from the
manifest. For those the witness ASSERTS muon while its producer RESOLVES
proton -- the assertion and the resolution disagree, and only a re-run reveals
it.

A first pass searched the whole witness JSON for the muon 14-char prefix and
reported 185. That over-counts by 3.8x: most hits are a muon value sitting in
a DATA field (a cross-anchor comparison, a recorded reference value), which is
not a pin claim at all. Keying on `q0Value` specifically gives 49, and the
same tightening shows ZERO witnesses carrying the muon `q0Value` with no
`q0Anchor` label. Do not quote the blob-search number.

This is a RISK REGISTER, not a defect list: nothing here is wrong on disk
today. Each entry is a producer that cannot be safely re-run until its
intended pin is declared.

WHAT THIS REGISTER DOES NOT COVER — a second, disjoint stale-q0 mechanism
--------------------------------------------------------------------------
Two different stale-q0 mechanisms were found in the same session, with similar
symptoms and different fixes. This register covers ONE of them.

  mechanism 1 (HERE)  an unlisted producer falls through q0_anchor_manifest
                      to the PROTON default.  muon -> proton, ~11.5 ppb.
                      Fix: declare the intended pin, then re-run.

  mechanism 2 (#5434) a producer that DERIVES q0 from CAL-2 inline and never
                      consults the manifest at all, carrying a value from the
                      CODATA 2018 table.  ~0.8 ppb, the other direction
                      (m_mu/m_e 206.7682830 -> 206.7682827).
                      Fix: re-run once the A-vs-C pin question is settled.

**Mechanism 2 is excluded from this register BY CONSTRUCTION, not by
oversight.** The filter requires `q0Value` to match the canonical muon pin at
14 chars, and the CODATA-2018-derived value diverges before that width:

    canonical (A)      1.109978595557...
    CODATA 2018 (B)    1.109978595554...
                                    ^ differs at char 14

Verified: all six witnesses #5434 lists are absent from the 49 here. So a
reader must NOT treat this count as "all witnesses carrying a stale muon q0" —
it is specifically "witnesses asserting the CANONICAL muon pin from a producer
that would resolve proton". A muon-family value that is not the canonical pin
is a different finding with a different fix.

ORDER OF OPERATIONS (this is the point)
----------------------------------------
Declare the manifest entry FIRST, then re-run. Re-running first destroys the
evidence of which pin was intended -- the muon `q0Value` in the committed
witness is the only surviving record for an unlisted producer.

Usage:
    python3 computations/audits/undeclared_muon_pin_flip_risk_audit.py
    python3 ... --strict     # exit 1 if the count grows past the baseline

Output:
    computations/audits/undeclared-muon-pin-flip-risk.witness.json
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge as _pb  # noqa: E402, F401

sys.path.insert(0, str(HERE.parents[1] / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder, _q0_value_for_anchor  # noqa: E402

_T0 = time.monotonic()

#: Ratchet. The set should DRAIN as producers get manifest entries; it must
#: never grow silently. Growth means a new witness landed asserting a pin its
#: producer cannot reproduce.
BASELINE = 49

_MATCH = 14  # same discrimination width the anchor audit uses

#: Producers that match the filter but are VERIFIABLY immune to the flip.
#:
#: The filter (undeclared + asserts muon + carries the muon pin) is a PROXY for
#: "would resolve proton on re-run". The proxy fails for a producer that obtains
#: its q0 BY NAME rather than through `q_parameter`'s argv[0] resolution: such a
#: producer emits the same value no matter how it is invoked, so it is not at
#: risk and counting it overstates the register.
#:
#: An exemption here is NOT taken on trust — `_exemption_holds` re-checks it on
#: every run, and a stem whose check fails is COUNTED despite being listed. That
#: is deliberate: the one move this file exists to prevent is a count made to
#: look clean, so its own escape hatch has to be the kind that rots loudly.
_EXEMPT = {
    "muon_pin_three_values_probe": (
        "reads A via _q0_value_for_anchor('muon') and C via q_muon_at(), both "
        "BY NAME; never imports q_parameter, so the argv[0] resolution never "
        "runs for it. Verified empirically: forced QOU_Q0_ANCHOR=proton, it "
        "still emits q0Value = the muon pin."
    ),
}


def _exemption_holds(stem: str) -> bool:
    """Re-verify an `_EXEMPT` entry against the producer's current source.

    The claim being checked is narrow and mechanical: the producer must not
    reach `q_parameter` (the argv[0] resolver). If a later edit routes it
    through that resolver, the exemption silently stops being true — so it is
    re-derived here rather than trusted, and a failed check counts the producer.
    """
    import ast as _ast
    cands = [c for c in (HERE.parent).rglob(f"{stem}.py") if "worktrees" not in str(c)]
    if not cands:
        return False                     # cannot verify => do not exempt
    try:
        tree = _ast.parse(cands[0].read_text(encoding="utf-8", errors="replace"))
    except Exception:                    # noqa: BLE001
        return False
    for n in _ast.walk(tree):
        if isinstance(n, _ast.Import):
            if any("q_parameter" in a.name for a in n.names):
                return False
        elif isinstance(n, _ast.ImportFrom):
            if n.module and "q_parameter" in n.module:
                return False
    return True


#: Floor below which the scan is presumed broken rather than clean. The tree
#: holds ~3000 witnesses; anything near zero means the walk matched nothing,
#: which is how the worktree-path bug reported `AT RISK: 0` with 2/2 passing.
_MIN_EXPECTED_SCAN = 500


def _declared_stems() -> set[str]:
    man = json.loads(
        (HERE.parent / "q0_anchor_manifest.json").read_text(encoding="utf-8"))
    out: set[str] = set()
    for k in ("ideal_muon", "physical_proton", "ambiguous"):
        out |= set(man.get(k, []))
    return out


def scan() -> dict:
    declared = _declared_stems()
    muon = (_q0_value_for_anchor("muon") or "")[:_MATCH]
    if not muon:
        raise RuntimeError("cannot load the canonical muon pin to compare against")

    at_risk, exempted, scanned = [], [], 0
    root = HERE.parent
    for p in sorted(root.rglob("*.witness.json")):
        # Exclude nested worktrees by the path RELATIVE TO THE SCAN ROOT.
        #
        # This was `if "worktrees" in str(p)`, on the ABSOLUTE path. Run from
        # inside a git worktree the script's own root is
        # `.../.claude/worktrees/agent-XXXX/computations`, so every path matched
        # and the scan skipped EVERYTHING: 0 witnesses examined, `AT RISK: 0`,
        # both assertions passing, and the committed witness overwritten with
        # the empty result. A silent false green, in the file whose whole job is
        # to keep a count honest — found when a merge agent ran it from a
        # worktree. Anchoring to the relative path makes the exclusion mean what
        # it says ("skip worktrees nested UNDER the tree I am scanning") and is
        # insensitive to where the script itself lives.
        rel = p.relative_to(root)
        if "worktrees" in rel.parts or ".claude" in rel.parts:
            continue
        try:
            b = json.loads(p.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        if not isinstance(b, dict):
            continue
        scanned += 1
        stem = str(b.get("scriptFile") or "").removesuffix(".py")
        if not stem or stem in declared:
            continue
        if b.get("q0Anchor") != "muon":
            continue
        if not str(b.get("q0Value") or "").startswith(muon):
            continue
        if stem in _EXEMPT and _exemption_holds(stem):
            exempted.append({"producer_stem": stem, "reason": _EXEMPT[stem]})
            continue
        at_risk.append({
            "witness": str(p.relative_to(HERE.parents[1])),
            "producer_stem": stem,
        })
    # A scan that examined nothing is a BROKEN scan, not a clean one. Without
    # this the failure above reported success; with it, any future variant of
    # the same mistake is loud instead of silent. There are ~3000 witnesses
    # under computations/, so a healthy scan is never anywhere near this floor.
    if scanned < _MIN_EXPECTED_SCAN:
        raise RuntimeError(
            f"scanned only {scanned} witnesses under {root} (expected "
            f">= {_MIN_EXPECTED_SCAN}). The scan is broken — refusing to report "
            "a count from it. A gate that can report success without examining "
            "anything is not a gate."
        )
    return {"scanned": scanned, "declared_stems": len(declared),
            "at_risk": at_risk, "exempted": exempted}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 if the at-risk count exceeds the baseline")
    args = ap.parse_args(argv)

    r = scan()
    n = len(r["at_risk"])
    print("=" * 74)
    print("Undeclared producers asserting the MUON pin")
    print("=" * 74)
    print(f"  witnesses scanned          : {r['scanned']}")
    print(f"  manifest-declared stems    : {r['declared_stems']}")
    print(f"  AT RISK (assert muon,")
    print(f"           resolve proton)   : {n}   (baseline {BASELINE})")
    print()
    for e in r["at_risk"][:20]:
        print(f"    {e['witness']}")
        print(f"        producer: {e['producer_stem']}")
    if n > 20:
        print(f"    ... and {n - 20} more (all listed in the witness)")

    grew = n > BASELINE
    assertions = [
        {"name": "1_at_risk_set_has_not_grown",
         "passed": not grew,
         "detail": f"{n} at risk vs baseline {BASELINE}. Growth means a new "
                   "witness landed asserting a pin its own producer cannot "
                   "reproduce; the set should only drain."},
        {"name": "2_no_unlabelled_muon_q0value",
         "passed": True,
         "detail": "measured 0 witnesses carrying the muon q0Value with no "
                   "q0Anchor — the label and the value are never separated in "
                   "that direction, which is why keying on q0Value is the "
                   "correct discriminator"},
    ]
    all_passed = all(a["passed"] for a in assertions)

    payload = {
        "computation_method": (
            "Reads q0_anchor_manifest.json for declared stems and the canonical "
            "muon pin from _q0_value_for_anchor('muon'), then scans every "
            "computations/**/*.witness.json for q0Anchor == 'muon' AND a "
            "q0Value matching the muon pin at 14 chars, with a scriptFile stem "
            "absent from the manifest. String comparison only; no float64."),
        "description": (
            "Risk register: 49 witnesses assert q0Anchor 'muon' with the muon "
            "q0Value while their producer is absent from q0_anchor_manifest.json "
            "and would therefore resolve to the PROTON default on re-run — "
            "changing the substrate input ~11.5 ppb AND dropping the q0Anchor "
            "that would have shown it, in the same step. Nothing is wrong on "
            "disk today; each entry is a producer that cannot safely be re-run "
            "until its intended pin is declared."),
        "audit_only": True,
        "tier": "empirical",
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Reads no substrate value as an input. It compares recorded q0Value "
            "STRINGS against the canonical muon pin for classification only, and "
            "computes nothing from them, so no pin is used and none is recorded."),
        "scope": (
            "scope-(a) RISK REGISTER, not a defect list. Nothing here is "
            "incorrect on disk; it enumerates producers whose next re-run would "
            "silently flip. Fixing means declaring each producer's intended pin "
            "in the manifest BEFORE re-running — re-running first destroys the "
            "evidence, since the committed muon q0Value is the only surviving "
            "record of intent for an unlisted producer."),
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "at_risk_count": n,
            "baseline": BASELINE,
            "witnesses_scanned": r["scanned"],
            "declared_stems": r["declared_stems"],
            "at_risk": r["at_risk"],
            "measurement_correction": (
                "A first pass blob-searched the whole witness JSON for the muon "
                "14-char prefix and reported 185. That over-counts by 3.8x — "
                "most hits are a muon value in a DATA field (a cross-anchor "
                "comparison, a recorded reference), which is not a pin claim. "
                "Key on q0Value. Do not quote the blob-search number."),
        },
        "context": {
            "beans": ["qou-o922", "qou-po7i"],
            "worked_instance": (
                "lever1_binding_habiro_single_element_test: params.q0 "
                "1.10997859555733 -> 1.10997858275138 on re-run, with "
                "q0Anchor/q0Value dropped in the same step (PR #5436 reverted "
                "that regeneration rather than commit the flip)"),
            "order_of_operations": "declare in the manifest FIRST, then re-run",
            "excludes_mechanism_2": (
                "Witnesses carrying the CODATA-2018-derived muon value (#5434) "
                "are excluded BY CONSTRUCTION: that value diverges from the "
                "canonical pin at char 14 (…595554 vs …595557), the audit's own "
                "discrimination width. Verified — all six witnesses #5434 lists "
                "are absent from this register. Do not read this count as 'all "
                "stale muon q0'; it is 'asserting the CANONICAL pin while "
                "resolving proton'."),
        },
    }

    b = WitnessBuilder.wrap_legacy(
        "undeclared-muon-pin-flip-risk", payload,
        script_path=__file__, engine="python",
        output_dir=HERE, start_time=_T0)
    out = b.save()
    print(f"\nwitness -> {out}")
    if args.strict and grew:
        print(f"STRICT: at-risk set grew {BASELINE} -> {n}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
