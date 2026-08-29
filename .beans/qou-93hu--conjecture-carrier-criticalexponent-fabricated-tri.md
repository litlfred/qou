---
# qou-93hu
title: 'Conjecture carrier: CriticalExponent — fabricated trivial-zero instance, asserts nothing'
status: todo
type: task
priority: normal
created_at: 2026-08-29T19:46:35Z
updated_at: 2026-08-29T19:46:35Z
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
