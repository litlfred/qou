---
# qou-h0ou
title: 'GAP: HasAction.action is scalar->scalar, so einsteinTensor cannot be rank-2 — wire FrobeniusPairingData'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-15T06:16:39Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-ddmn
---

## 2026-09-15 — DIAGNOSIS CONFIRMED, and a rank-2 field space is now formalized
Branch `claude/qg-rank-two-field-space-2026-09-15`. Audit:
`docs/audits/2026-09-15-rank-two-field-space-for-the-variational-derivative.md`.

### Diagnosis verified, blast radius measured and SMALL
`MonoidalCalcVar.lean:67` `HasAction.action : ((1_C) -> (1_C)) -> R` — domain is
`End(1_C)`, the SCALARS, so there is no field space to vary and the type never
mentions the objects being paired. Both Einstein slots are scalars wearing a
tensor's name: `ExternalCurrents.einsteinTensor` (`MonoidalCalcVar.lean:89`) and
`CategoricalVariationalData.einsteinTensor` (`GaugeTheory.lean:127`).

`grep -rn einsteinTensor` over the whole tree minus `.beans/`/`.git/`: **9 hits,
3 files, ALL .lean — zero .md, zero .ts, zero witnesses.** MonoidalCalcVar 4,
GaugeTheory 4 (all self-references in that one file), and `Instanton.lean:239`
which is a COMMENT. Consumers of `HasAction`/`VariationalData`/
`ExternalCurrents`/`HasMonoidalEOM` outside their own file: **NONE**, except
`QOU.lean:139` importing the module. **No consumer treats it as rank-2** — so
the problem is unchanged and the fix surface is tiny.

Additionally: **`HasAction` has ZERO instances anywhere** — declared, never
inhabited, so no action functional exists at all. The only `HasMonoidalEOM`
instance (`:130`) proves all three EOM by `rfl` because `vd` is DEFINED as
`<ec.einsteinTensor + ec.stressTensor, ec.gaugeCurrent, 0>` — AGENTS.md
"Defined residual != derived decomposition" in Lean form. The only
`HasCategoricalEOM` instance (`GaugeTheory:172`) takes the three identities as
`Fact` hypotheses, i.e. assumes them.

### What was formalized — NEW FILE, sorry-free
`folio/quantum-observable-universe/lean/QOU/FrobeniusHopfData/PairingVariationalDerivative.lean`,
namespace `QOU.Variational`. Built on the carrier the corpus already holds,
`FrobeniusPairingData` (`FrobeniusPairingCategorical.lean:51`).

§1, generic `{R} [CommRing R]` — `QuadraticAction` on a module field space;
`variation` is a BILINEAR FORM `V ->L V ->L R`, rank-2 *because the field space
is*. Four theorems: `value_add` (the exact Taylor identity that DEFINES the
derivative; uses `form_symm`; false for any other coefficient), `value_smul`
(degree-2 homogeneity), `euler` (`variation e e = 2 * value e` — the contraction
that recovers the scalar), `polarization`. **No limit and no axiom are needed:**
for a quadratic functional the Gateaux derivative is algebraic. MonoidalCalcVar
axiomatises the EOM on the ground that a categorical calculus of variations
"does not yet exist in Lean/Mathlib" — for the quadratic case that is not so.

`value_does_not_determine_variation` — explicit Z-witness: two fields, SAME
action value, DIFFERENT derivatives. That is precisely why one scalar cannot
stand in for a rank-2 object (`polarization` recovers it from the action as a
FUNCTION; `einsteinTensor` is a value at a point).

§2, categorical — `fieldSpace d := d.dual (x) d.obj -> 1_C` is an `R`-module
under `[Preadditive C] [Linear R C]`, so §1 applies to the pairings directly.
`contract d eta` is the `R`-LINEAR trace landing in `End(1_C)` — **exactly the
corpus's einsteinTensor slot**, so the corpus keeps the trace and discards the
tensor. `#check` shows the two shapes side by side: `ScalarFieldAction` takes no
pairing argument at all, `PairingFieldAction` takes `FrobeniusPairingData C`.

### The structural result — scope (b), invariant cited
`subsingleton_of_contract_reflects`: if equality of contractions implied
equality of the rank-2 fields, uniformly in the co-pairing, then
`Subsingleton (fieldSpace d)` — at most ONE pairing. Invariant: `zero_comp`, the
degenerate co-pairing `eta = 0` contracts every field to the same scalar. So a
scalar Einstein-shaped equation is STRICTLY WEAKER than the rank-2 identity it
is named after, in any Preadditive monoidal category with two distinct pairings.
`contract_eq_iff` gives the exact residue: scalar equality is rank-2 equality
modulo `LinearMap.ker (contract d eta)`.

### Verification
`lean -DautoImplicit=false -s 65536` exit 0, no errors, no warnings (LEAN_PATH
against the main checkout's restored oleans; `lake` never invoked). `#print
axioms` on all 12 declarations: `propext`/`Classical.choice`/`Quot.sound` only —
**no sorryAx**, kernel-checked not grep-checked.
`scripts/lean-self-assuming-audit.py` on the new file: **0 candidates**.

### NOT done, deliberately
No physics wired: no metric, curvature, stress-energy, `G_N`, `8pi`, or any
numerical constant. No general Euler-Lagrange machinery (§1 is QUADRATIC
actions only). The co-pairing's handedness is opposite to
`Nondegenerate`'s `coev` and the braided transport between them is NOT asserted.
`MonoidalCalcVar.lean` and `GaugeTheory.lean` are UNTOUCHED — retyping
`HasAction.action` to take a field space is neither a precision fix nor
corpus-derived, so per AGENTS.md "ASK THE OWNER BEFORE CHANGING THINGS" it needs
owner sign-off. It would be cheap: zero instances, zero consumers.

### Spun out
`qou-1ccx` — `lean-self-assuming-audit.py` rule 2 cannot see the ANONYMOUS
instance binder (`[C X]` + `ClassName.field`), which is how all three
`variational_*` theorems are spelled, so the audit scores 0 on GaugeTheory.lean.
Successor cause to `qou-24m2` (which fixed the NAMED `[ctx : C]` case — confirmed
still working by probe). 91 candidates, LOWER BOUND, shape not defects.

## 2026-09-15 (later) — existence constructors, and the objection they close
`QuadraticAction` had no existence constructor, which the formalizer skill
requires: without one every downstream statement about it is vacuously
satisfiable. Adding `QuadraticAction.ofFunctional eps` (the action
`e |-> (eps e)^2` from any linear functional, plus `Inhabited` via
`ofFunctional 0`) turned out to close the strongest objection to this whole
branch, so it was not bookkeeping.

  ofFunctional_variation : (ofFunctional eps).variation e d = 2 * eps e * eps d

`ofFunctional eps` NEVER SEES A FIELD except through the SCALAR `eps e`, and its
variational derivative is a bilinear form on the field space regardless. So
"but the action is a scalar anyway" is not a defence of the scalar
`einsteinTensor` slot: the action is a scalar in BOTH shapes, and only the
DOMAIN decides the rank of the derivative.

`contractionAction d eta eps` is the same construction on the pairing field
space, built from nothing but a co-pairing and a scalar reading of `End(1_C)`:
`value T = (eps (eta >> T))^2` — the square of EXACTLY the scalar the corpus
keeps — and `variation T d = 2 * eps (eta >> T) * eps (eta >> d)`, still rank-2.
So the same scalar data `HasAction` reads produces a rank-2 derivative once its
domain is the pairings.

Re-verified on the extended file: `lean -DautoImplicit=false -s 65536` exit 0,
no errors, no warnings; `#print axioms` on all **19** declarations gives
propext / Classical.choice / Quot.sound only, **sorryAx count 0**;
`lean-self-assuming-audit.py` 0 candidates; `grep -c sorry` 0.

### Bean stays IN-PROGRESS, deliberately
The gap this bean names is not closed. `HasAction.action` still has the scalar
domain; `MonoidalCalcVar.lean` and `GaugeTheory.lean` are untouched. Retyping
`HasAction.action` to take a field space is neither a precision fix nor
corpus-derived, so per AGENTS.md "ASK THE OWNER BEFORE CHANGING THINGS" it is an
owner call. It is cheap when wanted: zero instances, zero consumers.


## 2026-09-15 (third pass) — RETYPED, owner-authorised. Branch `claude/hasaction-rank-two-retype-2026-09-15`

The owner selected "Retype `HasAction.action` to rank-2", so the §"ASK THE
OWNER BEFORE CHANGING THINGS" gate that held the second pass back is
satisfied for this change. Done, verified, pushed. Bean stays OPEN (§13a) —
the residual problem below is untouched.

### Blast radius — CONFIRMED, with two corrections to the record

`grep -rn einsteinTensor`, tree minus `.beans/`/`.git/`: **9 hits, 3 files,
all `.lean`** — MonoidalCalcVar 4, GaugeTheory 4, Instanton:239 a comment.
Exactly as this bean recorded. `HasAction` had **zero instances**, confirmed.

Two corrections a later reader needs:

1. **The path is `QOU/QuantumObservableUniverse/GaugeTheory.lean`**, not
   `QOU/GaugeTheory.lean`. Line numbers were right; the directory was not.
2. **GaugeTheory does NOT import MonoidalCalcVar.** The two files were
   *parallel duplicates* of the same defect, not consumer and producer. So
   "fix GaugeTheory's consumers" was the wrong shape of task — GaugeTheory
   had to be retyped independently. It now imports MonoidalCalcVar so the
   field space and contraction are shared rather than re-declared.

And one thing the 9-hit grep structurally could not see: a **third** site,
`quantum-observable-universes/categorical-action.lean`, a CONTENT BLOCK
(`.ts`/`.md`/`.qa.json` siblings) redeclaring `QOU.CategoricalAction`,
`QOU.CategoricalConnection` and all three `variational_*` in the same
namespace as the library. It has no `einsteinTensor`, which is why the grep
missed it, and its `variational_einstein` is

    ca.gravity = ca.matter -> ca.gravity = ca.matter := id

— a tautology stating the WRONG equation (gravity = matter, not
gravity = einsteinTensor + stressTensor). `variational_yang_mills` is
`ca.gauge = ca.gauge >> id -> ca.gauge = ca.gauge`. Both are §"Strict Lean
Discipline" item 5 violations. NOT touched: outside the authorised change,
and deciding what that block should say is a separate call.

### What was retyped

Field space `PairingSpace C X Y := X (x) Y --> 1_C`, generic in an ordered
pair of objects. Deliberately NOT indexed by `FrobeniusPairingData`: that
would give the MathlibExt module a QOU-specific import cone, and it is the
same space as the second pass's `fieldSpace d` at `(X,Y) := (d.dual, d.obj)`.

* `HasAction.action : PairingSpace C X Y -> R` (was `End(1_C) -> R`)
* `VariationalData.gravity`, `ExternalCurrents.{einsteinTensor,stressTensor}`
* `CategoricalAction.gravity`,
  `CategoricalVariationalData.{einsteinTensor,stressTensor}`

UNCHANGED, deliberately: `gauge`, `gaugeCurrent`, `matter`, and their two
equations. The split is forced by `gravity = einsteinTensor + stressTensor`
needing one additive group, not by a physics claim about which currents "are"
tensors.

### The bridge — the deliverable that makes it a refactor

`contract eta : PairingSpace C X Y ->+ End(1_C)`, `T |-> eta >> T`. Then
`einstein_contracted` / `einstein_contracted_comp` DERIVE the pre-retype
scalar Einstein equation from the rank-2 one (rw by the identity, then
`map_add`). Nothing previously statable is lost.

On the GaugeTheory side the co-pairing is **not a free parameter**:
`FrobeniusHopfData` already carries `coevaluation : 1_C --> obj (x) obj`, and
`A` is self-dual there — `pairing_snake_left/right` pair that coevaluation
against `mul >> frobeniusForm`, whose type is `obj (x) obj --> 1_C`, i.e. a
`PairingSpace` verbatim. So `frobeniusPairing` gives the retyped slots a
substrate-supplied inhabitant, and `variational_einstein_scalar` is the
bridge at the corpus's own datum.

`coevaluation_contract_eq_iff` states the residue exactly: two rank-2 fields
contract equally iff their difference is killed by `coevaluation`, and
`FrobeniusHopfData` carries **no epi hypothesis** making that kernel trivial.

### What the retype does NOT fix — say this, do not imply otherwise

`hasMonoidalEOM_of_def` still discharges all three EOM by `rfl`. Retyping
does not touch it: rank and tautology are independent defects, and the
honest report has to say so rather than let the reader infer the `rfl` was
what got removed. `einstein_split_iff` now states the residual problem
exactly — `g = G + T <-> T = g - G`, i.e. the identity says only that the
stress term IS the residual and places NO condition on `einsteinTensor`.
AGENTS.md §"Defined residual != derived decomposition", in Lean. Open.

### The one consumer that broke, and the semantic choice it forced

`qou_canonical_action_unique_up_to_scalar` applied the unit automorphism by
PRE-composition (`s.hom >> ca1.action.gravity`). `s.hom` ends at `1_C`, which
is no longer where `gravity` begins:

    error: Type mismatch
      s.hom >> ?m.40 has type 1_C --> ?m.27
      but is expected to have type PairingSpace C fh.obj fh.obj

Under the old typing both sides were `End(1_C)` and the composition side was
unobservable; it became a real question the moment the field space stopped
being the scalars. Fixed by post-composing uniformly, which is the side the
block's OWN docstring argues for (rescaling `\int_A`, the last map into the
unit). Flagged in the commit as a semantic choice, not a mechanical retype.

`qou_canonical_action_dirac_sq` (same file) still typechecks unchanged —
`gravity >> gauge` is fine because gravity still ENDS at `1_C`.

### Verification

`lean -DautoImplicit=false -s 65536`, exit 0, against a COMPLETE symlink-farm
overlay (`scripts/lean-overlay-env.sh`) carrying this branch's own
MonoidalCalcVar and GaugeTheory oleans. `lake` never invoked.

**17 files GREEN**: the 3 library files, all 9 importers of GaugeTheory, and
the `CategoricalAction` consumers that do not import it. `qou-canonical-action`
was the only break.

`#print axioms` on all 33 touched/new declarations: **propext only, no
sorryAx** — kernel-checked. `#check` confirms the retype is real, not
cosmetic: `HasAction.action`'s domain and `einsteinTensor`'s codomain both
now name the paired objects.

`scripts/lean-self-assuming-audit.py` on the 3 files: **0 candidates** — and
per `qou-1ccx` that is a LOWER BOUND, so the four new `[HasMonoidalEOM]` /
`[HasCategoricalEOM]` theorems were checked by eye. None is a projection:
each conclusion needs `map_add` on top of the class field, so the field is
not restated verbatim.

No `R`, no ordering, no `Real.*`, no `linarith`/`positivity`/`norm_num`, no
numerical constant added (§7c verified by diff grep). No `sorry`, no `axiom`,
no `native_decide`, no `: True`.

### Not done

* **Root `QOU.lean` cannot be checked here** — blocked behind
  `QOU.Eightfold.ObstructionClassForcesComplexType`, which has no olean in
  the cache because it is red on `main` (AGENTS.md records the same
  `[6459/6460]` failure). Pre-existing, unrelated.
* **`proof-statement-integrity` on `qou-canonical-action` left
  `needs-agent`**, deliberately. The existing entry is
  `[EXPIRED-NO-FIELD-HASH]`, which the sidecar's own `$expired` note says
  adjudicates nothing — so there is no live verdict, and an honest one would
  be FAIL: the `.md` asserts `D^2 = q R_int + tr_A(F /\_q *_q F)` and the
  Lean concludes `gravity >> gauge = gravity >> gauge` by `rfl`. Pre-existing
  and a separate adjudication.
* **`qa-staleness` on the whole chapter: 310 blocks, fresh=0,
  stale/partial=310.** The block I refreshed was not singled out by my
  change; the chapter is uniformly stale on `main`.
* **§7c warning at `GaugeTheory.lean:220`** (`obs : StateSections -> R` in
  `ArchimedeanObservation`) is PRE-EXISTING — verified absent from my diff —
  and is arguably a false positive, since the structure is the archimedean
  side of the wall by name and construction.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-15 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress (PR #8457)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/PairingSpaceActionRetypeRuledOddProjectionLetterInvolutionPullbackQuotientKernelMultiplierSlope.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_h0ou_hlx8_hlxp_i9gk_slpd_probe.witness.json` (`Commit 1` = `6615e05829d98e7dc8f3151a6136022620b0fa75`, `HEAD` = `87f824354a46b08a4af8436ed872967b2f3dfc59`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8457, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — physics-scope re-check on main 2ae54ab40 (bean-drain sibling, issue #8810)

Resolved on main. `MathlibExt/MonoidalCalcVar.lean:181-184` `HasAction.action : PairingSpace C X Y → R`; `:231` `einsteinTensor : PairingSpace C X Y`; `GaugeTheory.lean:161` likewise; `FrobeniusHopfData/PairingVariationalDerivative.lean` is on main. The scalar→scalar gap is closed. Remaining scope item (not this bean): the Einstein equation is still a class field (`HasCategoricalEOM`), whose one instance takes it as a `Fact`; recorded in the audit §2c. Audit: `docs/audits/2026-11-21-physics-claim-scope-recheck.md` on branch `claude/physics-scope-audit-2026-11-21` (4df574c79).
