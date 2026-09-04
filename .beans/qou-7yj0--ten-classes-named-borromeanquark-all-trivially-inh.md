---
# qou-7yj0
title: 'Ten classes named BorromeanQuark, all trivially inhabited: conditional-on-conjecture is decorative'
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T12:32:32Z
updated_at: 2026-09-04T12:49:40Z
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


## Round two (same day) — the other nine carriers, measured

Evidence `docs/audits/2026-09-04-conjecture-carriers-round-two.lean`,
`lean`-direct exit 0.  Not "all vacuous"; the split is the finding.

**Five are WELL-FORMED** — subject is a parameter or entirely external:
`HypMinimizerUnique`, `CarlemanDeterminacyStieltjes`, `IsOcneanuWeightSystem`,
`CoGroundStateSelection`, `TrefoilElectronMassConj`.  The last one's own
docstring records that this exact defect was already found and fixed there
(strand/crossing counts "were previously free fields of the conjecture class
beside equations naming their values").  So the proposed fix is the repo's own
better practice, not a new idea.

**Four more are SELF-SATISFYING**, each verified by instance:
`CrystalGraphRealization (R) (q)` (`raising := fun _ _ => none`; two identical
copies), `CrystalGraphRealization : Prop` (**no axioms at all**),
`CanonicalMarkovWeightsH3` (two copies), `QIntegerMassFormula : Prop` in
wigner-coefficient-derivation.

**One is the OPPOSITE defect and is proved so.**  `QIntegerMassFormula` at
mass-theory/q-integer-mass-formula.lean:150 is UNINHABITABLE
(`¬ Nonempty QIntegerMassFormula`), so its conditional theorems are vacuously
true.  Quantifier scope, not physics: `fits_AME` ranges over EVERY real
`B_AME`, while `{(1+δ)X : |δ| ≤ t}` is a bounded interval around one fixed `X`.
The sibling at lean/QOU/Interactions/QIntegerMassFormula.lean:178 carries the
missing `[IsAMEValue Z N B_AME]` binder — a one-binder fix, correct form
already in the tree.

**Name collisions** (the `markovZ` defect one level up): 10 `BorromeanQuark`,
4 `CrystalGraphRealization`, 3 `QIntegerMassFormula`, 2
`CanonicalMarkovWeightsH3`.  The three `QIntegerMassFormula` are respectively
vacuous, uninhabitable and correct.

**Left unmeasured on purpose:** `CrystalGraphRealization (n) (q)` in
confinement-grading-correspondence-conditional.lean — `klr_lift` is a field but
the constraint relates two EXTERNAL functions through it, so it is neither
clearly free nor clearly constraining.  Not guessed at.

**Still not done:** applying the fixes.  Measurement only so far.


## RETRACTION (same day) — the `[IsAMEValue]` recommendation was wrong

I recommended porting the `[IsAMEValue Z N B_AME]` binder into
mass-theory/q-integer-mass-formula.lean, calling it "a one-binder fix" and the
gated form "the correct form already in the tree".  Retracted in the audit doc,
on PR #6657 and here.

**Why it is wrong.**  The gated form is laundered one level up.  `IsAMEValue`
is documented as carrying "the two physical invariants every real entry
satisfies" and has a THIRD field, `fits_bound`, whose own docstring reads
"Trivialized bound hypothesis to close sorry" and which asserts the 1 %
agreement outright.  So `fits_AME_conditional` there reduces to
`∀ …, [claim] → [claim]`, and `canonical` discharges `fits_AME` by projecting
it (`f_magic := fun _ => 0` makes the two sides definitionally equal).  Porting
the binder trades a vacuous-because-unsatisfiable statement for a
`claim → claim` one WITH a model available.

**New recommendation: touch neither file.**  Author's call, already framed on
bean `qou-hjf4`.

**How I missed it** — ran none of the six corpus-grep paths for
`QIntegerMassFormula`.  Paths 1 (`docs/audits/`) and 6 (`.beans/`) each hold
the answer alone: `qou-hjf4`, and Finding B of
docs/audits/2026-08-24-faithful-instance-family.md, which carries the same
two-file comparison I rebuilt and states the conclusion I contradicted.

**What survives.**  `¬ Nonempty QIntegerMassFormula` is a machine-checked proof
of what that note asserted in prose; a proof is stronger and re-runnable.

**Not a duplicate of qou-hjf4**, mechanically: that census
(scripts/trivially-inhabiting-instance-census.py) keys on `INSTANCE_HEAD` — an
unguarded global `instance` with constant data content.  This is about the
CLASS and needs no instance.  Measured: of the ten `class BorromeanQuark`
declarations exactly ONE has an instance in the tree
(observations/borromean-quark.lean:120); the other nine have none, so an
instance-keyed census cannot see them at all.  Complementary; neither subsumes
the other.
