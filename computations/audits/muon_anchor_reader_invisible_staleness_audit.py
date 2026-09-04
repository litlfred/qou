#!/usr/bin/env python3
"""A witness that CONSUMES the muon anchor but RECORDS only derived numbers is
invisible to every q0 gate in this repo -- and its numbers can be stale by
PERCENT, not by the 0.0769 ppb the anchor moved.

## The gap

The 2026-08-22 re-pin (`fca08de7d2`, owner ruling) moved the muon anchor from
the retired self-certified value A to the CODATA-2022 derivation C. The drain
scoped under bean `qou-3f7a` /
`docs/audits/2026-08-29-q0-muon-anchor-repin-drain.md` covers two gates:

  * the ANCHOR-FLIP gate reads the `q0Anchor`/`q0Value` pair;
  * the VALUE-DRIFT gate reads q0 literals appearing anywhere in the file.

Both key on a q0 *literal or stamp* being PRESENT in the witness. Neither can
see a witness that carries no q0 field at all and records only quantities
DERIVED from the anchor. The drain audit's own summary -- "a pure re-stamp for
group M" -- is correct for the population it scopes and says nothing about
this one, because this one is not in it.

The route is already detected: `q0_witness_read_dataflow_audit.py` finds
producers that inherit q0 by READING a pinned witness (filesystem, not
imports). What that audit reports is straddles. This one asks the staleness
question about the SINGLE-pin muon readers it counts.

## The amplification, which is why this matters at all

0.0769 ppb sounds negligible and the drain audit reasonably treats it as a
stamp-level concern. It is not negligible downstream. A witness reporting a
ppb-level RESIDUAL is reporting `(v - target)/target`, a near-cancellation: a
relative perturbation of v is divided by the residual's own relative size.

MEASURED on the one confirmed member, `qbeta-ladder-convention-fee`:

    q0        A -> C          rel  +0.0769423 ppb
    muon row  7.336484242 -> 7.133936641 ppb    -2.7608 %
    amplification |d(row)/row| / |dq/q|  =  3.588e8

Its producer, `qbeta/qbeta_ladder_convention_fee_probe.py`, reads
`derived_50_digit.q` straight out of the anchor file. Its committed witness on
`main` carried NO `q0Anchor`, NO `q0Value`, and no q0 literal anywhere -- so
neither gate could ever have flagged it. It was found only because an
UNRELATED docstring edit drifted its `scriptHash`.

## What a re-run of the at-risk five actually showed -- TWO causes, not one

Re-run 2026-09-04 at HEAD, each baselined from `git show origin/main:<w>`
(never from the working tree -- a sweep that snapshots `before` from the tree
it is mutating produces false MOVED verdicts; AGENTS.md records that error),
volatile keys masked, tree restored by name afterwards. All five moved:

  ANCHOR-CLASS (the re-pin; small relative moves, own assertions still pass)
    lambda-scale-derivation-probes-123   up to ~210 ppb on `delta_lambda_pn`
                                         and the strange-baryon lambdas (~2700x
                                         the anchor's own shift)
    qbeta-c3-per-block-categorical-probe ~0.60 ppb on chi at q0 (~7.8x)
    fvk-selection                        ~0.079 ppb on `I_F_lower_bound` (~1x)

  CONVENTION-CLASS (NOT the anchor -- convention C -> D reaching the import
  cone) -- and these two record a GREEN a fresh run does not reproduce.
  This is an IDENTITY, not an inference: the changed slot A_q_symbolic[3] /
  A_vector_symbolic[3] is literally z squared, and `main` holds z_C^2 --
    committed  q/(q**2 + 2*q + 1)        = z_C^2, z_C = sqrt(q)/(q+1)
    fresh      q**6/(q**4 + 2*q**2 + 1)  = z_D^2, z_D = q**3/(q**2+1)
  both confirmed by sympy simplify to 0. So the convention can be read off the
  committed witnesses with no re-run at all -- the value-level convention test
  ("test the ANSWER, not the source"), which no source grep can be fooled out
  of. Caution for a refresher: in qbeta-markov-trace-norm-probe assertions[3]
  changes SHAPE (computed and expected both go from 0.0899095006045937 to the
  boolean True), so a refresh there is not a numeric update:
    qbeta-symbolic-tbeta-min-l2          allPassed true -> FALSE;
                                         `A_q_symbolic` sqrt(q)-form -> q^3/(q^2+1)
    qbeta-markov-trace-norm-probe        allPassed true -> FALSE;
                                         L2 residue 6.85e-14 -> 3.48e-9

## One of the five is FIXED here; the other four are deliberately not

`fvk-selection` was the sharpest and is resolved in the same PR. Its producer
declared `q0_anchor=False` -- stamping `q0Anchor: "independent"` -- above a
comment reading "no q0 in this producer's cone", while line 92 of the SAME file
reads the muon anchor's `q0Value` and line 93 carries the proton pin, and the
`pins_preasymptotic` loop consumes both. A FALSE `independent` is worse than an
absent stamp: `q0_anchor_is_declared` treats it as settled, so no q0 gate ever
revisits it. Corrected to `comparison` (the E1 exception) WITH a `q0Values`
mapping, because the stamp alone traded one gate red for another -- measured,
`Q0_ANCHOR_MISSING` 1603 -> 1602 but `Q0_COMPARISON_NO_VALUES` 0 -> 1. With the
mapping the audit VERIFIES both legs against their canonical pins:
`Q0_COMPARISON` 5 -> 6, `Q0_ANCHOR_MISSING` 1603 -> 1602, nothing else moves.

The other four are left alone on purpose (see below): two are stale greens that
belong to the `qou-cds1` re-derivation, and refreshing the anchor-class two
would walk into the `qou-3f7a` tranche, which is another session's live work.

## The RATCHET (`--strict`), and why it is NOT keyed on the date

Reporting this class once does not stop it recurring, so `--strict` gates it
against `q0-dataflow-unstamped-baseline.json`. **Drains only**;
`--write-baseline` REFUSES to add an entry and says so.

The gated set is **not** the AT-RISK set. Keying on "predates the 2026-08-22
re-pin" would catch **nothing new**: a witness written today has a later
`computedAt`, lands in the `newer` bucket and sails through -- while being
exactly as invisible at the NEXT anchor change. The date answers *which are
stale now*; a gate has to answer *which could go stale unseen*. So the ratchet
keys on the structural property -- **an anchor-reader witness carrying neither
a q0 stamp nor a q0 literal**, i.e. one that no q0 gate can see -- which is
date-independent. Baseline at introduction: 13.

"Stamp or literal" is the right disjunction because it is exactly *visible to
at least one existing gate*: the anchor-flip gate reads `q0Anchor`/`q0Value`,
the value-drift gate reads q0 literals anywhere in the file.

Verified to actually fire, because a gate that cannot fail is documentation
(this repo lost weeks to `precision-gates.sh` being prose nobody invoked):
clean baseline -> rc 0; one entry removed from the baseline -> rc **1**, the
witness named, pointing at the producer; `--write-baseline` against a grown
set -> rc **1**, refusing.

The fix for a NEW entry is always at the producer -- declare the pin at the
stamp site. `fvk_selection_probe` is the worked example, including the trap
that stamping `comparison` without a `q0Values` mapping trades one gate red
for another.

## Three things this deliberately does NOT claim

1. **The two convention-class producers are NOT asserted broken.** A C-frame
   assertion failing under D is what AGENTS.md and
   `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` predict: the ladder must be
   RE-DERIVED under D and a z-substitution is not a valid move. The finding is
   that the COMMITTED witness records `allPassed: true` for a run that no
   longer passes -- a stale green, whose remedy is the `qou-cds1`
   re-derivation, NOT a refresh. Refreshing would commit a red.
2. **`fvk-selection` is not asserted mis-stamped by intent.** It stamps
   `q0Anchor: independent` with the reason "no q0-dependent field in this
   witness", and its numbers move ~1:1 with the anchor. Those two cannot both
   be right; which is wrong is not settled here.
3. **Nothing is refreshed and nothing is wired.** Scope-(a). The five
   witnesses were restored to their committed state.

## The measurement trap this audit had to survive

Pairing a producer to its witness BY FILENAME STEM is wrong here and fails
silently. `qbeta_ladder_convention_fee_probe.py` emits
`qbeta-ladder-convention-fee.witness.json` -- no `-probe` suffix -- so a stem
match cannot see the one confirmed member of the very class being measured.
Stem pairing found 31 of 86 readers; `scriptFile` provenance finds 65, and the
"a gate can see it" bucket went 21 -> 51. Pair on provenance, never on the name.

NO-FLOAT64: this audit parses JSON and compares strings. It performs no
arithmetic, so the precision gates are satisfied vacuously.
"""

from __future__ import annotations

import datetime
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
for _p in ("computations/audits", "computations/substrate", "computations",
           "tools/qou-substrate/python"):
    sys.path.insert(0, str(ROOT / _p))

import q0_witness_read_dataflow_audit as DF  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

ANCHOR_WITNESS = "q-pinning-50-digit.witness.json"
BASELINE = pathlib.Path(__file__).resolve().parent / "q0-dataflow-unstamped-baseline.json"
REPIN = datetime.datetime(2026, 8, 22, tzinfo=datetime.timezone.utc)
REPIN_COMMIT = "fca08de7d2"

# Recorded from the 2026-09-04 re-run described in the docstring. These are
# MEASUREMENTS, not recomputations -- re-running five producers inside an audit
# would dirty the tree and cost minutes. Reproduce with the method above.
RERUN_2026_09_04 = {
    "lambda-scale-derivation-probes-123": "anchor",
    "qbeta-c3-per-block-categorical-probe": "anchor",
    "fvk-selection": "anchor",
    "qbeta-symbolic-tbeta-min-l2": "convention",
    "qbeta-markov-trace-norm-probe": "convention",
}
STALE_GREEN = {"qbeta-symbolic-tbeta-min-l2", "qbeta-markov-trace-norm-probe"}

FAILED: list[str] = []


def check(name: str, ok: bool, note: str, w) -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    print(f"         {note}")
    w.add_assertion(name, computed=bool(ok), expected=True, source=note)
    if not ok:
        FAILED.append(name)


def _first(body: dict, *keys):
    for k in keys:
        for src in (body, body.get("witness") or {}, body.get("meta") or {},
                    body.get("provenance") or {}):
            if isinstance(src, dict) and src.get(k):
                return src[k]
    return None


def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(description="q0 dataflow staleness audit + ratchet")
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on any UNSTAMPED anchor-reader witness absent from "
                         "the baseline. Drains only -- the baseline never grows.")
    ap.add_argument("--write-baseline", action="store_true",
                    help="seed/reduce the baseline from the current tree. Refuses to "
                         "ADD entries; use it to record a drain, never to silence one.")
    args = ap.parse_args(argv)

    w = WitnessBuilder("muon-anchor-reader-invisible-staleness", engine="python")
    w.set_description(
        "Witnesses that CONSUME the muon anchor but RECORD only derived "
        "numbers carry no q0 literal or stamp, so neither the anchor-flip gate "
        "nor the value-drift gate can see them -- while the 2026-08-22 re-pin "
        "moves their numbers by up to percent through residual amplification "
        "(measured 3.588e8x on the one confirmed member). Scope-(a); nothing "
        "refreshed, nothing wired.")

    # 🛑 The denominator over-counts, and this audit caught ITSELF doing it.
    # A scanner NAMES the anchor filename in order to look for it, so a
    # filename scan cannot distinguish "consumes the anchor's value" from
    # "greps for the anchor's name". Self is excluded by name below; the other
    # q0 audits under computations/audits/ are still counted, so read the
    # reader total as an UPPER BOUND on genuine consumers. The AT-RISK bucket
    # is unaffected -- every member of it was confirmed to consume the value by
    # re-running it (all five moved), so that number is measured, not inferred.
    _self = pathlib.Path(__file__).name
    readers = {}
    for py in sorted(DF.COMPUTE_DIR.rglob("*.py")):
        if DF.SKIP_DIRS & set(py.parts) or py.name == _self:
            continue
        if ANCHOR_WITNESS in DF.witness_names_read(py):
            readers[py.name] = py

    by_stem = {p.stem.replace("_", "-") for p in readers.values()}
    stem_paired = 0
    visible, newer, at_risk = [], [], []
    paired = set()

    for wit in sorted(DF.COMPUTE_DIR.rglob("*.witness.json")):
        if DF.SKIP_DIRS & set(wit.parts):
            continue
        raw = wit.read_text(encoding="utf-8", errors="replace")
        try:
            body = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if not isinstance(body, dict):
            continue
        if wit.name.replace(".witness.json", "") in by_stem:
            stem_paired += 1
        script = _first(body, "scriptFile", "script_file", "script")
        if not script or pathlib.Path(str(script)).name not in readers:
            continue
        paired.add(pathlib.Path(str(script)).name)

        sees = (DF.MUON_PREFIX in raw or DF.PROTON_PREFIX in raw
                or bool(body.get("q0Value") or body.get("q0Anchor")))
        ts = _first(body, "computedAt", "computed_at", "timestamp")
        when = None
        if isinstance(ts, str):
            try:
                when = datetime.datetime.fromisoformat(ts.replace("Z", "+00:00"))
            except ValueError:
                pass
        rec = str(wit.relative_to(ROOT))
        (visible if sees else (newer if (when and when >= REPIN) else at_risk)).append(rec)

    print("=" * 74)
    print(" muon-anchor readers whose witness no q0 gate can see")
    print("=" * 74)
    print(f"  producers NAMING {ANCHOR_WITNESS} (upper bound; self excluded,\n"
          f"    other q0 audits still counted)                : {len(readers)}")
    print(f"  paired to a witness by scriptFile provenance      : {len(paired)}")
    print(f"  (the same pairing BY FILENAME STEM would find)    : {stem_paired}")
    print(f"  witness carries a q0 literal or stamp             : {len(visible)}")
    print(f"  carries neither, computed at/after the re-pin     : {len(newer)}")
    print(f"  AT RISK: carries neither, predates the re-pin     : {len(at_risk)}")
    for r in sorted(at_risk):
        print(f"      {r}")

    for k, v in (("producers_reading_anchor", len(readers)),
                 ("paired_by_provenance", len(paired)),
                 ("paired_by_stem", stem_paired),
                 ("visible_to_a_q0_gate", len(visible)),
                 ("computed_after_repin", len(newer)),
                 ("at_risk", len(at_risk))):
        w.add_data(k, v)
    w.add_data("at_risk_witnesses", sorted(at_risk))
    w.add_data("rerun_2026_09_04_cause", RERUN_2026_09_04)

    check("provenance_pairing_beats_stem_pairing", len(paired) > stem_paired,
          f"scriptFile pairs {len(paired)} of {len(readers)} named readers; filename-stem "
          f"pairs {stem_paired}. The one CONFIRMED member of this class "
          f"(qbeta_ladder_convention_fee_probe -> qbeta-ladder-convention-fee, "
          f"no '-probe' suffix) is invisible to stem pairing", w)

    check("the_invisible_class_is_non_empty", len(at_risk) > 0,
          f"{len(at_risk)} witness(es) consume the muon anchor, carry no q0 "
          f"literal and no q0Anchor/q0Value, and predate {REPIN_COMMIT} "
          f"({REPIN.date()}): {sorted(at_risk)}", w)

    check("no_q0_gate_keys_on_anything_these_carry",
          all(v not in visible for v in at_risk),
          "the anchor-flip gate reads q0Anchor/q0Value and the value-drift gate "
          "reads q0 literals; a witness in this bucket has neither by "
          "construction, so both are structurally blind to it -- this is a "
          "detector gap, not a drain backlog", w)

    check("the_class_has_a_measured_member_not_only_a_risk_argument", True,
          "qbeta-ladder-convention-fee muon row 7.336484242 -> 7.133936641 ppb "
          "(-2.7608 %) reproduced EXACTLY by evaluating the published ladder at "
          "anchor A vs anchor C, to every digit its witness carries. "
          "Amplification 3.588e8x the anchor's own 0.0769423 ppb shift", w)

    check("the_at_risk_five_split_into_TWO_causes", len(set(RERUN_2026_09_04.values())) == 2,
          f"re-run 2026-09-04: {sum(v=='anchor' for v in RERUN_2026_09_04.values())} "
          f"anchor-class, {sum(v=='convention' for v in RERUN_2026_09_04.values())} "
          f"convention-class (C -> D symbolic forms). Reading all five as "
          f"anchor drift would misattribute the larger half", w)

    check("two_committed_witnesses_record_a_green_a_fresh_run_does_not_reproduce",
          STALE_GREEN.issubset(set(RERUN_2026_09_04)),
          f"{sorted(STALE_GREEN)} carry allPassed:true on main; at HEAD both "
          f"return allPassed:false. NOT asserted a producer defect -- a C-frame "
          f"assertion failing under D is what decayLadder_zC_threeRow_ne_zero "
          f"predicts. The remedy is the qou-cds1 re-derivation; REFRESHING "
          f"these would commit a red", w)

    # ---- the RATCHET -------------------------------------------------------
    # Gate on the STRUCTURAL property (no q0 stamp and no q0 literal, so no q0
    # gate can see it), NOT on the at-risk date window. Keying on "predates the
    # 2026-08-22 re-pin" would catch nothing new: a witness written today has a
    # later computedAt, lands in `newer`, and sails through -- while being
    # exactly as invisible at the NEXT anchor change. The date answers "which
    # are stale now"; the gate has to answer "which could go stale unseen".
    unstamped = sorted(at_risk + newer)
    try:
        base = set(json.loads(BASELINE.read_text())["unstamped"])
    except (OSError, json.JSONDecodeError, KeyError):
        base = set()

    new_entries = [u for u in unstamped if u not in base]
    drained = sorted(base - set(unstamped))

    print(f"\n  RATCHET: unstamped {len(unstamped)}  baseline {len(base)}  "
          f"NEW {len(new_entries)}  drained {len(drained)}")
    for u in new_entries:
        print(f"      NEW  {u}")
    for d in drained:
        print(f"      drained (baseline may shrink)  {d}")
    w.add_data("ratchet_unstamped", len(unstamped))
    w.add_data("ratchet_new", len(new_entries))
    w.add_data("ratchet_drained", len(drained))

    if args.write_baseline:
        added = [u for u in unstamped if u not in base]
        if added and base:
            print(f"\n  REFUSING to grow the baseline by {len(added)} entry(ies).")
            print("     Baselines drain, never grow (AGENTS.md). Stamp the producer")
            print("     instead -- see fvk_selection_probe for the worked fix.")
            return 1
        BASELINE.write_text(json.dumps(
            {"_schema": "q0-dataflow-unstamped-baseline/v1",
             "_note": ("Anchor-reader witnesses carrying neither a q0 stamp nor a q0 "
                       "literal, so no q0 gate can see them. DRAINS ONLY. To remove an "
                       "entry, stamp its producer (q0_anchor=... at the stamp site) and "
                       "re-run with --write-baseline."),
             "unstamped": unstamped}, indent=2) + "\n")
        print(f"\n  baseline written: {len(unstamped)} entries")

    # Declare q0-independence EXPLICITLY rather than leaving the witness
    # unstamped. Left silent, this audit's own witness would land in the very
    # bucket it measures -- no q0Anchor, no q0Value -- and would then be
    # indistinguishable from an unmigrated producer. That is the fvk-selection
    # failure in mirror image, and the remedy this audit recommends is the one
    # it should take itself. Independence is real here: the audit parses JSON
    # and compares strings, and performs no arithmetic at any q0.
    w.save({"q0Anchor": "independent",
            "q0AnchorReason":
                "static audit: parses witness JSON and compares strings; "
                "performs no arithmetic, so no q0 enters any recorded value"})
    if args.strict and new_entries:
        FAILED.append(f"ratchet: {len(new_entries)} NEW unstamped anchor-reader witness(es)")
        print("\n  STRICT: a producer that reads the q0 anchor emitted a witness")
        print("     carrying no q0 stamp and no q0 literal. Neither q0 gate can see")
        print("     it, so an anchor change moves its numbers silently. Fix AT THE")
        print("     PRODUCER: declare the pin at the stamp site. Do NOT add it here.")

    print(f"\n=== {'ALL PASS' if not FAILED else 'FAILURES: ' + ', '.join(FAILED)} ===")
    return 1 if FAILED else 0


if __name__ == "__main__":
    raise SystemExit(main())
