---
# qou-qflp
title: 'Q0_FLIP 262 was ONE corrupted reference file, not a drainable tranche — restored + guarded'
status: in-progress
type: task
priority: high
tags:
    - precision-gates
    - q0-anchor
    - data-integrity
created_at: 2026-08-19T17:50:00Z
updated_at: 2026-08-19T17:50:00Z
---

## What was asked vs what was there

Asked to work the Q0_FLIP tranche, drain it, and spin up a medium swarm.
THE TRANCHE DOES NOT EXIST. Q0_FLIP 262 -> 0 by restoring one file.

## Root cause

The muon pin is NOT a constant in the audit -- it is READ from
computations/q-pinning-50-digit.witness.json via
qou_substrate.witness._q0_value_for_anchor("muon"). Commit 9a9c6b31c
("sweep(tnjb): first 25 witnesses regenerated at the proton pin") swept that
reference along with 24 ordinary computation witnesses, replacing the muon
50-digit constants with proton ones and flipping its q0Anchor muon -> proton.
So the muon lookup returned the PROTON value and every muon-tagged witness in
the corpus read as a flip.

CATEGORY ERROR, not a migration step. Migrating a COMPUTATION witness
muon -> proton is legitimate under qou-1c4y (in-progress). Migrating the datum
that DEFINES what "muon" means deletes the vocabulary the q0Anchor field is
written in. This file must keep the muon pin no matter how far the proton
migration proceeds.

## Measured

  reference as on main (proton) : Q0_FLIP 262, Q0_OK 392
  reference restored (muon)     : Q0_FLIP   0, Q0_OK 654

The 262 move WHOLESALE into Q0_OK (654-392=262) -- not a mixed bag with real
defects hiding inside. Every one a false positive.

## Why it mattered more than an ordinary false positive

Every sampled flagged witness DECLARES muon AND CARRIES the muon value:
internally consistent, correct as written. Draining them to green the gate
would have rewritten 262 CORRECT witnesses to the wrong q0 -- the exact corpus
corruption the gate exists to prevent, performed in the gate's name. Concrete
case behind AGENTS.md's "never make a red run green ... fix at the producer".

## Done

1. Restored the reference to its pre-sweep muon state.
2. GUARD in computations/audits/q0_anchor_consistency_audit.py:
   reference_integrity() runs BEFORE classification, reports one loud line
   instead of hundreds of derived rows, and --strict exits 1 on a corrupt
   reference even when Q0_FLIP would be 0. The message says explicitly: do NOT
   drain the flips.
3. Probe computations/probes/q0_anchor_flip_false_positive_probe.py, 5/5 --
   measures the audit under BOTH states of the reference rather than asserting.
4. Audit doc docs/audits/2026-08-19-q0-anchor-flip-262-false-positives.md.

## NEXT STEP

1. TELL qou-1c4y TO EXCLUDE THE REFERENCE. The migration is in-progress and will
   re-sweep this file otherwise. The guard now catches it, but an exclusion is
   the real fix. Coordinate with whoever owns that sweep.
2. THE REAL DRAINABLE TRANCHE, if one is wanted, is Q0_ANCHOR_MISSING = 1905 --
   witnesses with no anchor declared at all. That IS large and swarm-shaped, but
   it is NOT mechanical: each needs its producer inspected to learn which pin it
   actually used, and AGENTS.md rule 4 says the muon->proton mass migration
   needs scoped sign-off before it runs. Do not start it unprompted.
3. Do NOT re-open the 262. They are correct as written.

## Classification arm (2026-08-19, after "why did you not swarm?")

Swarm spun: 13 read-only agents over the 889 file-locally-clean producers
(10 shards) + 2 adversarial spot-checks + 1 residue triage. Running.

Mechanical cross-check, run in parallel, is done and is the stronger result:

1. **The answer is dominated by the infra exclusion list.** Same 889
   producers, "reaches no q₀" went **173 → 562 → 722** as two artifacts were
   removed: `qou_substrate/witness.py` (knows both pins because it *stamps*
   the field; every producer imports it — 400 spurious straddles) and
   **docstring** matches (`_precision.py` has no q₀ at all, its docstring
   mentions `wedderburn_jones_markov` — 195 of 198 muon reaches).
2. **245 of the 1905 already carry their pin in payload** under ad-hoc keys
   (`q0`, `q_0_50dps`, `q_proton`, …). Labelling them is transcription — no
   producer analysis, no re-run, no numerical change. Plus **25** carrying
   BOTH prefixes: deliberate cross-anchor comparisons, EXCLUDE per the
   2026-08-08 owner ruling in `qou-pin2`.
3. New read-only audit `computations/audits/q0_anchor_payload_recovery.py`,
   population matched byte-identically to the consistency audit (1905 exactly).

**Corrected my own figures once**: first reported 305 of 330, which mixed two
populations (the scan walked `_deprecated` + `AUDIT_SUFFIXES`, the label came
from the audit that skips both). 245 / 25 / 1635 are the figures.

**I duplicated existing infra before grepping for it.** `q0_producer_pin_classifier.py`
(AST-based, `if __name__` exclusion, BOTH detection) already existed and is
better than the regex I wrote. Its *population* is disjoint from mine — it
compares code against a **recorded** pin, so it cannot speak about the 1905 —
but I should have found it first and reused `classify()` from the start, which
is what the corpus-grep checklist is for.

## 2026-08-23 — superseded on main; the swarm overturned my method

**#5324's fix is redundant.** `main` landed the restore (`2e4745448`), the
diagnosis + guard (`7ddaeab36`, bean `qou-cezp`), and a `comparison` anchor
(`31d1bdf6e`) while this branch was open. Branch rebuilt on main carrying only
additive work; the duplicate commits are dropped, not defended.

**The swarm measured my mechanical classifier at 37 % FALSE-`independent`** —
130 of 352, in the dangerous direction. 443 of 889 adjudicated (8 of 13 agents
hit a weekly limit; it has since reset, 446 remain). Dominant blind routes:
a literal in the producer's own file (72) and **reading a q₀-bearing witness
JSON by path (49)** — the second is structural: an import graph cannot see it,
at any depth. **Do not quote the 722.** ~55 % independent ⇒ ~490 of 889, and
that is an extrapolation from a sample.

**Real defect found and fixed:** `q0_producer_pin_classifier.classify()` tested
only the muon literal — no proton branch existed. 137 producers carry a live
proton literal; 53 classified `none`, which its docstring calls "purely
symbolic". Fix moves proton 37→42, none 25→20, muon disagreements 7→5.

**Two corrections to my own payload scan**, opposite directions: population
mismatch (over-count, mixed `_deprecated`/`AUDIT_SUFFIXES` into a count labelled
with the audit's population) and a 12-digit muon prefix (under-count — the
corpus has two muon values agreeing to 11 digits; recoverable muon read 93 when
it is 179). Final: 326 recoverable / 40 `comparison` / 1558 open, of 1924.

## 2026-08-23 (evening) — swarm complete: 887/889, and each fix is quantified

| method | proposes independent | false | rate |
|---|---|---|---|
| A import-cone as first reported | 720 | 285 | **39.6 %** |
| B + proton-literal + artifact-resolution | 588 | 159 | 27.0 % |
| C + witness-read data-flow detector | 495 | **82** | **16.6 %** |

Ground truth 460 independent / 420 dependent / 7 undetermined. **71 % of the
false `independent` calls removed.** The 37 % I extrapolated from 443 held
(true 39.6 %) — but it could have been wrong, and finishing was the only way
to know. **The 722 is retired; do not quote it.**

Three defects fixed, all measured:
1. `classify()` had **no proton branch** — 137 producers carry a live proton
   literal, 53 read as `none` ("purely symbolic"). Route d: 136 → 41.
2. `MUON_ARTIFACTS` **asserted a pin that changed underneath it** —
   `y-lambda-at-q0` went proton in the convention-D cascade; 57 producers name
   it, 37 verdicts change, incl. `wedderburn_jones_markov` itself. Mirror of
   (1) and worse: asserts a wrong pin rather than missing one.
3. New **data-flow detector** for the filesystem route: 542 direct + 239 via an
   imported module. Route b: 97 → 26.

Plus `Q0_AMBIGUOUS_NO_REASON` (17 of 18 lack a reason; the 1 that has one is
mislabelled by it) and the straddle split (53 → 29 protected + 24 actionable).

**The recurring lesson, four times over:** every headline number in this arc was
an artifact first — 400 (`witness.py` stamps the field), 195 (`_precision.py`
docstring), 1117 (`q_parameter` IS the accessor), 53 (deliberate comparisons).
A shared module's q₀ knowledge is infrastructure for its importers, not
evidence about them. And the fix for one artifact CAUSED the route-b blind spot:
discounting string constants as prose also discounted a filename.

**Open:** 82 known-false in C (d=41, b=26, f=9); the 326 transcribable
witnesses (mutation, needs sign-off); the AGENTS.md `y_lambda_at` "muon-built
cache" description vs the proton file on disk.

## 2026-08-23 (late) — "do all": the remaining items, done

**Verified first**: main's `q-pinning-50-digit.witness.json` holds **muon**
(so main's own retraction `2b370512b` is consistent with this work), and
`y-lambda-at-q0.witness.json` still carries proton — the `MUON_ARTIFACTS` fix
stands. Both branches rebased onto main (+213) and re-verified: `lean`-direct
exit 0 sorry-free, probe 29/29, all blocking precision gates green.

**Fixed the 7 off-pin fallbacks.** Each carried `Q0 = 1.1099780333553254` in an
`except` handler — 506 ppb from muon, 495 from proton, ~44× the μ–p tension —
substituted silently on any import hiccup. Now raise. Verified both ways: scan
reports 0, and the live accessor returns `1.1099785827513808`, so the removed
fallback differed from the real value by 495 ppb.
`hbond_categorical_action.py` had commented its literal "documented substrate
q₀ (proton-anchor pin)" — false by 495 ppb.

**Extended `q0_hardcoded_pin_audit` with OFF_PIN.** Its population was a grep of
the two pin literals, so a file carrying only an off-pin value was never in
scope — **the third audit with that blind spot**. 18 files found (excluding
`computations/audits/`, since a detector necessarily contains what it hunts).

**Fixed a guard that could never succeed, over a typo'd pin.**
`phase1c_proton_h3_symbolic_decomposition.py:219`, three defects in one line:
`dir()` returns LOCALS and the line is inside `main()`; `Q_50_DIGIT_STR` is
imported *after* `main()`, so the guard was **always False** and the fallback
**always** taken; and that fallback is a **digit-transposed** muon pin
(`1.10977…` for `1.10997…`), 0.018 % off ≈ **15,600× the μ–p tension**. Scoped
honestly — it sits under `if diff != 0`, so it is a rarely-executed path.

**Left as a reported class (not swept):** 17 remaining off-pin literals, mostly
legacy (`1.1097090249` ×4, `1.10970000000` ×3, `1.10997861` ×2). Each needs a
judgement on whether it is a deliberate legacy comparison.

**Still owner-gated:** the AGENTS.md `y_lambda_at` "muon-built cache" text vs
the proton file on disk; the 326 transcribable witnesses (a mutation).
