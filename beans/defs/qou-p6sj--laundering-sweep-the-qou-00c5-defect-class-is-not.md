---
# qou-p6sj
title: 'Laundering sweep: the qou-00c5 defect class is NOT mechanically detectable — two detectors, both failed'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T20:27:08Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-cdx1
---

## Outcome: NEGATIVE. Do not trust a proximity detector for this defect class.

Asked to sweep for other instances of the `qou-00c5` shape — an uninhabited Lean
`class` that durable artifacts report as PROVED. Two detectors written; **both
failed, in different ways**, and the honest conclusion is that this class is not
mechanically detectable by text proximity.

### Detector 1 — measured itself

Keyed on a twist NAME and the OTHER twist's exponent within a +-2 line window.
Reported **22 candidates**. Inspection: the "hit" lines were things like
`"probe": true,` and `{`, because the window caught a name and an exponent from
unrelated neighbouring text. Worse, it flagged the two files that had **just been
fixed** — a file that correctly distinguishes two objects mentions BOTH names, so
a one-name/other-exponent heuristic fires precisely on the careful ones.

### Detector 2 — substring and file-name matching

Cross-referenced uninhabited classes against `proved`/`sorry-free` claims naming
them. Reported **296 candidates over 956 uninhabited classes**. Inspection: class
`MarkovTrace` "matched" the string `BorromeanMarkovTrace.lean` — substring, not
word. It also matched on FILE names, which say nothing about which class a claim
refers to.

### Detector 3 — tightened, and still not usable as a verdict

Whole-word class names only, no file-name matching, widened instance detection.
**67 candidates** over 778 uninhabited classes. Legible at last, but precision is
still too low to act on:

- `RibbonTwistEigenvalue` (3 sites) — **all three are the qou-00c5 FIX**, which
  contains the word "proved" inside the phrase "AXIOMATIZED, not proved".
- `SDeformedVolumeChannel` — the sites say "theta_K HAS NO CORPUS DEFINITION",
  i.e. they are *reporting the gap*, not laundering it.
- `TauRhoHodgeLift` — "GIVEN R1+R2 ... **THEN** TauRhoHodgeLift holds. Sorry-free"
  — correctly stated conditional.
- `PlanckStepAtomicity` — "deliberately NOT a `PlanckStepAtomicity`",
  "conditional discharge" — correctly stated.

**The word "proved" near a class name is not the signal.** The signal is whether
a sentence asserts *the class itself* is established, and negation, conditionals
and corrections all sit inside the same window. That is a semantic judgement.

### The one candidate examined, and why it is NOT the same defect

`CategoricalHiggsIdempotent` (uninhabited) with
`docs/duality-tracker.md:109`: *"`CategoricalHiggsIdempotent` proved
`m_W/m_Z = cos θ_W`"*.

Checked the Lean rather than filing it. The class carries `cos_theta_W_def`,
`m_W_GeV`, `m_Z_GeV` as **defining fields**, and the ratio theorem derives the
conclusion from them — its own docstring calls it "mechanical algebra from the
definitions". So it is a genuine (if easy) derivation conditional on the class,
and the offending line is a **PR changelog entry**, not an audit claim or a
witness field. Materially weaker than `anchored_on_proved` on a numerical
anchor. **Not filed as a defect.**

### What this means for the qou-00c5 fix

`qou-00c5` was found by READING, prompted by a specific conflation, and its
discriminator was semantic. It should not be presented as the first hit of a
sweep, because no sweep found it and no sweep would have.

**Do not read this bean as "the corpus is clear."** It is "the corpus is
UNMEASURED for this defect, and the obvious way to measure it does not work."
Anyone wanting a real answer needs an agent-adjudicated pass over the 67, in the
style of the `lean-vacuity-review-ledger` — machine flags, agent verdicts — not
another regex.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8384, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
