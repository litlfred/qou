---
# qou-93hu
title: 'Conjecture carrier: CriticalExponent — fabricated trivial-zero instance, asserts nothing'
status: completed
type: task
priority: normal
created_at: 2026-08-29T19:46:35Z
updated_at: 2026-08-30T03:33:48Z
parent: qou-rq9n
---

Carrier at ConditionalClasses.lean:68; instance `critical_exponent_canonical` at :110, discharged `rfl`.
Field, in full: `alpha_three_eq_four : (3 * 4 : N) = 12`.

The entire content of a class named for the q-NS critical exponent is the
numeral identity 3*4=12. **No exponent variable occurs in it.** The docstring
claims the field is "the scaling-exponent identity 3 * alpha_num = 4 (cleared
form of alpha = 4/3)" -- but the numerals are already substituted in, so
nothing constrains alpha. A class whose field is a closed true numeral
statement cannot constrain anything; `rfl` proves it and would prove it
whatever the physics.

Of the five this is the least defensible, because unlike the other four it is
not even the right SHAPE -- there is no quantifier and no free variable.

Bound as `[CriticalExponent]` in 5 files. Ledger entries: 0.
Parent: qou-rq9n.



## RESOLVED 2026-08-30 (PR #6068)

    class CriticalExponent (alpha : R) : Prop where
      alpha_eq : alpha = 4 / 3

Transcription of the class's own docstring, not new mathematics. A Prop class
cannot carry data, so alpha is a PARAMETER.

**Content verified, not asserted** -- the old field was 'the right shape' too:
- `example : CriticalExponent (4/3) := <rfl>` — inhabitable at the value
- `example : not (CriticalExponent 2)` — **refutable elsewhere**, which the old
  `(3*4 : N) = 12` could never be: it excluded no alpha at all
- `example (a : R) [h : CriticalExponent a] : a = 4/3 := h.alpha_eq` — the
  hypothesis is real, not free

**The fix created a second defect, caught on the next detector run.** Once the
field is typed `alpha = 4/3`, a theorem concluding it and proving it by
`h.alpha_eq` is a §3b-cond item 5 self-assuming projection —
`proof-no-self-assuming-projection` flagged `critical_exponent_identity` and
`qNS_critical_exponent_with_compactness` as NEW. Note what that means: the
**vacuous version was invisible to the projection detector precisely by being
vacuous**, since a closed numeral is not character-identical to any field type.

Resolved by the cleared form the original docstring already promised:
`3 * alpha = 4`, proved `rw [h.alpha_eq]; norm_num`. Conclusion is not the
field's type; the proof does arithmetic. Both flags clear.

**Left the vacuous population.** Probe baseline 23 -> 22; the carrier 'no longer
matches the filter' — the first in this arc to leave by being fixed rather than
by being re-adjudicated.

**Still NOT encoded, so do not over-read this**: nothing ties this alpha to the
q-NS scaling regime. That needs the scaling definition, which is open. This is
the conjecture's VALUE claim conditional on naming the exponent, not the whole
conjecture. Stated in the class docstring.

**Flagged, deliberately not fixed here**: `qNS_enstrophy_cube_bound` proves
`0 <= Z^3` by `pow_nonneg h_Z 3` and uses NONE of its five class
hypotheses; `qNS_reeb_period_bound` and `qNS_rogue_zero_cost_nonneg` are the
same shape. Decorative hypotheses on an unconditionally-true claim — a
different defect, noted at the site.

**Same defect, different carrier, still open**: `fluid-dynamics/core-levi-form.lean:59`
declares a SEPARATE `CriticalExponent` still carrying `alpha_three_eq_four :
(3 * 4 : N) = 12`. Content sibling, different namespace, its own baseline
entry. Not covered by this bean.
