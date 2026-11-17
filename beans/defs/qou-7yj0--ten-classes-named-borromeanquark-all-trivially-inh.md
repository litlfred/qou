---
# qou-7yj0
title: 'Ten classes named BorromeanQuark, all trivially inhabited: conditional-on-conjecture is decorative'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T12:32:32Z
updated_at: 2026-10-04T15:14:07Z
parent: qou-5p7n
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


## Prior-work cross-reference (PR #6666) — and a disagreement, not a duplication

Corpus-grepped `docs/audits/` and `.beans/` for EVERY carrier named, after the
`[IsAMEValue]` retraction showed I had skipped that step.

Nearest prior work: `docs/audits/2026-08-23-free-prop-field-census.md`
(PR #5562, beans `qou-lo1t` / `qou-tsnp`).  It ALREADY NAMES `BorromeanQuark` —
`instance canonical` declared twice, sibling and library, "the shadow-pair
shape again".

**Different questions, mechanically.**  That census: which carriers have a FREE
`Prop` FIELD.  This audit: which carriers SATISFY THEMSELVES.  Neither
contains the other — `q-beta-spectral-bridge`'s carrier has no `Prop`-typed
field at all yet `⟨0, 0, rfl⟩` inhabits it; and a free `Prop` field can live in
a carrier whose other fields constrain something external.

**Where they disagree.**  The census finds 89 free-`Prop` carriers with no
inhabitant and reads that as the "§3b-tax honest open state — nothing inhabits
them, so a downstream `[C] → P` can never be applied.  Weak, but inert."  For a
SELF-SATISFYING carrier that is wrong: "nothing inhabits it" is not evidence of
an open state when inhabiting costs one line.  The theorem is gated by a fact
nobody typed, not by an open problem.  Inhabitation-IN-THE-TREE is the wrong
probe; the question is whether an instance is AVAILABLE.

Carried over from the same census, applied to my own evidence: a `lean` run
killed by a 2-minute timeout leaves a zero-error log that reads as success.
Every check here was run to completion in the background with the exit status
captured AFTER the process exited.

## Merged

#6644 (q-codifferential 13 axioms -> 0) and #6657 (the carrier audit) both
merged by rebase after a fresh-fetch mergeability check, a semantic-conflict
check (main touched NONE of the changed files across 132 / 92 commits), and a
re-run of `lean`-direct on both changed `.lean` files at their branch tips
(both exit 0).


## C1 was a RE-DISCOVERY — qou-4els named it on 2026-08-24

Read `qou-4els` (completed) properly instead of only seeing it in a grep hit
list.  Its table already names the C1 vacuity in the same words:
`CrystalGraphRealization.canonical` — `CrystalNode := PUnit`,
`raising _ _ := none` → `crystal_realises` is `none = none`.  That IS `C1.triv`.

Second re-discovery this session (the `[IsAMEValue]` retraction was the first
and costlier).  **Seeing a bean in a grep hit list is not reading it** — that
is the durable lesson, not either instance.

**What qou-4els fixed, verified on main:** all six `canonical`s are `def` now,
not `instance`, so `[CrystalGraphRealization R q]` no longer resolves silently.

**What survives:** demotion removes AUTOMATIC resolution; it does not make the
carrier constrain anything.  One line still satisfies the class and `C1.triv`
is that line.  Downstream conditionals are gated by nobody having typed it, not
by mathematics.  Demotion moves a carrier from "inhabited" to "inhabitable" —
smaller than it reads as, and it strengthens rather than undercuts
parametrise-don't-field: demotion is necessary, not sufficient.

**Detector caveat from qou-09mr:** `checkNoVacuousInstanceData` needs a
degenerate VALUE, so definitional laundering (a real non-degenerate function
chosen to make the claim reflexive) is invisible, as are fields inside a tactic
`exact { … }` rather than a `where`.  Upstream `folio-assistant-ilbh`.

**Still first measurements:** C2 (`CrystalGraphRealization : Prop`,
transfer-matrix), C3 (`CanonicalMarkovWeightsH3`), C4 (`QIntegerMassFormula :
Prop`, wigner) — in neither qou-4els's six nor qou-tsnp's twelve (`holds :
Prop`, a third shape).


## MAJOR CORRECTION — the headline over-claims; qou-z9ws had the rule first

`docs/audits/2026-08-30-the-remainder-is-vacuous-not-open.md` (bean qou-z9ws,
2026-08-30) states this thesis more sharply, on 52-of-79 measured context
classes, with a probe (`scripts/lean-context-class-inhabitation-probe.py`).
It corrects me twice:

1. **Inhabitation does not decide it.**  Discriminator = what the downstream
   declaration DOES with the field.  Re-checked bodies: T1, T2, T6, T8 all
   DERIVE -> §3b-cond working, NOT defects (the Aug-30 audit names T1 as its
   worked counter-example).  T3 (`:= inst.volume_calibrates_mass`) and T10
   (`:= inst.forms_agree`) PROJECT -> defects stand.
2. **"Inhabited => vacuous" only for an UNPARAMETERISED class.**  `C1.triv`
   inhabits `CrystalGraphRealization ℤ 0`, parameterised -> satisfiability.

So the headline is WRONG.  Measurements right, inference wrong.  Sharp cases:
T3, T10, and T4 (fixed) — T4's field existentially bound BOTH V and m, a defect
the derives/projects rule does not reach.

**Round two was prior work in full.**  C1 = qou-4els.  C2/C4 =
docs/audits/2026-08-24-undecided-carrier-witnesses.lean, IDENTICAL witnesses.
C3 STOOD DOWN: CanonicalMarkovWeightsH3 worked 2026-09-03 with owner approval
("2y", qou-6u92), inhabitant wired to Markov-DERIVED n=3 weights (qou-c35w,
#6506), guarded by `delta_tau_M_canonical_resolves_to_canonical` which is
rfl-provable only because resolution picks those weights.  Parametrising breaks
that guard.

**Survives:** #6644 entirely; the two `rfl` axioms + T4 parametrisation;
`¬ Nonempty QIntegerMassFormula` as a proof (prior probe's seventh is
`SeparateLambdaScale_Antipattern`, different decl); the name-collision counts.

**PATTERN — the durable part.**  Four re-discoveries in one session
(`[IsAMEValue]`, C1, C2/C4, the thesis), each found AFTER writing the claim,
three in files a grep had already surfaced.  A corpus this heavily audited
should be assumed to hold the finding already.

**Apply-phase: NOT to be done from this bean as written.**  T1/T2/T6/T8 are
working as intended; C3 is owner-approved and guarded; C2/C4 belong to the
Aug-24 probe.  What is left is T3 and T10, and both are authorial (they change
what the paper claims).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
