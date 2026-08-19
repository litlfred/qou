---
# qou-akb4
title: 'check-sidecars §7c detector: two false-positive classes'
status: todo
type: task
priority: normal
created_at: 2026-08-16T11:40:05Z
updated_at: 2026-08-16T11:40:05Z
---

Worked instance: `qou-7cmk` (a §7c mixed-file advisory judged cosmetic and
deliberately deferred). This bean is about the **detector**, not that file.

## Two false-positive classes, both hit in a single merge pipeline

`scripts/check-sidecars.sh` runs the §7c base-ring check on un-sidecar'd
library Lean. Two of its flags are not archimedean leaks.

### 1. `norm_num` on pure-ℕ arithmetic counts as archimedean

The marker regex (`scripts/check-sidecars.sh:35`) is:

    ARCH='(\(q : ℝ\)|: ℝ\b|\(ℝ\)|Real\.(sqrt|rpow|log|exp|cos|sin|pi)|\blinarith\b|\bpositivity\b|\bnlinarith\b|\bnorm_num\b|LinearOrderedField|0 < q\b|\bCODATA\b|MeV)'

`\bnorm_num\b` is in the alternation. But `norm_num` is the ordinary tactic
for discharging a concrete numeric goal over **any** semiring — closing
`2 + 2 = 4` in ℕ is not crossing the substrate→archimedean wall, and the
§7c harm model is *archimedean ℝ leakage*, which a ℕ-arithmetic goal cannot
produce. `linarith` / `positivity` / `nlinarith` are defensible markers
(they want an order); `norm_num` on its own is not.

### 2. A generic result beside its `_real` specialisation reads as mixing

The `MIXED generic + archimedean` branch (`:87`) fires when one file
contains both a generic-`R` declaration and an archimedean one. It cannot
distinguish:

- **the prescribed pattern** — a generic-`Field` result placed next to its
  `_real` specialisation, which is how §7c says to write the wall crossing;
  from
- **accidental mixing** — an archimedean assumption silently inherited by
  generic downstream code, which is the thing §7c exists to catch.

Both look identical to a per-file marker scan. Only reading the
declarations separates them.

## Evidence: two false positives, one pipeline

- **PR #5185.** Flagged; the §7c judgement was that the flag did not
  indicate a base-ring defect.
- **PR #5187.** Flagged on the same file family; the merge write-up records
  the disposition in full — *"the file is inherently archimedean (`zC` needs
  `Real.sqrt`, the sign theorems need ordering), and the 'generic' half is
  the deliberate §7c pattern of a generic-`Field` result
  (`zD_eq_qsq_div_bracketTwo`) beside its `_real` specialisation. Splitting
  the file would be churn; flagged here rather than silently passed."*

`qou-7cmk` reaches the same verdict from the other direction, on
`MarkovZFullBarCondition.lean`: *"the §7c harm model is archimedean ℝ
leakage across the substrate wall. This file has none."*

Three independent agents have now hand-adjudicated the same two classes to
"not a defect". That is the signal that the detector, not the code, is what
needs the edit.

## Why it matters

A checker whose flags are routinely dispositioned as "acceptable, not a
defect" trains agents to wave through §7c output — and the *next* flag may
be a real leak. The 2026-06-25 history that created this gate is precisely a
gratuitous `(q : ℝ)` reaching an algebraic τ-kernel lemma unswept. Recall is
the point; but recall that is never trusted is not recall.

## What to do

1. Drop `\bnorm_num\b` from `ARCH`, **or** gate it: only count it when the
   file also mentions `ℝ` / a `Real.*` construct. Prefer the gate — a
   `norm_num` inside a genuinely archimedean file is still weak evidence.
2. For class 2, teach the MIXED branch the `_real`-suffix convention: a
   generic declaration `foo` sitting beside `foo_real` is the prescribed
   pattern and should downgrade to informational, not advisory.
3. Re-run over the corpus and record how many of the current advisories
   survive — if the count drops sharply, that is the measure of the noise
   the two classes were adding.
4. Do **not** simply silence the MIXED branch. The class-2 discrimination is
   the useful half; only the undiscriminated version is noise.

## Provenance

Filed 2026-08-16 from an agent that could not reach the `beans` CLI. Regex
quoted from `scripts/check-sidecars.sh:35` at merge `36080a4e21`; PR #5187
disposition quoted from its merged body.
