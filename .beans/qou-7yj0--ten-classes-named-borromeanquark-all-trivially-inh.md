---
# qou-7yj0
title: 'Ten classes named BorromeanQuark, all trivially inhabited: conditional-on-conjecture is decorative'
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T12:32:32Z
updated_at: 2026-09-04T12:33:02Z
---

Measured 2026-09-04, compiler-verified.  Full write-up:
`docs/audits/2026-09-04-self-satisfying-conjecture-carriers.md`;
evidence `docs/audits/2026-09-04-borromean-quark-carriers-trivial.lean`
(`lean`-direct exit 0, zero `sorryAx`).

**Finding.** Ten separate `class BorromeanQuark` declarations exist, no two
with the same fields, nine of them file-local in the ROOT namespace.  All ten
are trivially inhabited — each was replicated and handed an instance built
from nothing but its own field types, and every one typechecks.  So every
theorem marked "conditional on `[BorromeanQuark]`" is unconditional.

**Root cause.** A carrier whose constraining fields relate only its own DATA
fields is a definition of a structure, not a statement of a conjecture.  A
group is rightly such a carrier; a conjecture is not, because a conjecture is
a claim about objects fixed elsewhere.  If the carrier chooses its own
subject it always satisfies itself.

Clearest case is `q-beta-spectral-bridge`: the conjecture is that two
specific, independently defined Q-value presentations agree; the carrier
encodes them as two FREE reals asserted equal, and `⟨0, 0, rfl⟩` inhabits it.

**Fix pattern.** Parametrise rather than field:
`class BorromeanQuark (bareMass : ℝ → ℝ) : Prop where …` is refutable
(`¬ BorromeanQuark (fun _ => 0)`); the field form is not.

**Not yet done.**  (1) Applying the fix — each of the ten needs its own
parametrisation and its downstream theorem re-typed; T3 (canonical) has 13
files referencing the name.  (2) The other conjecture-shaped carriers in the
169-theorem "conditional on" population — `TrefoilElectronMassConj` (6),
`HypMinimizerUnique` (5), `CrystalGraphRealization`, `QIntegerMassFormula`,
`CanonicalMarkovWeightsH3`, `CoGroundStateSelection`, `IsOcneanuWeightSystem`,
`CarlemanDeterminacyStieltjes`, `QouObstructionReductionContext` — are NAMED,
not measured.  The check is mechanical: replicate, attempt an instance from
the field types, run `lean`-direct.

**Do not quote the 874/1450 shape scan as the finding.**  It counts carriers
whose Prop fields mention their own data, which is what an ordinary algebraic
structure looks like; the large majority are correct.
