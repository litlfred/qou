---
# qou-h0ou
title: 'GAP: HasAction.action is scalar->scalar, so einsteinTensor cannot be rank-2 — wire FrobeniusPairingData'
status: in-progress
type: task
priority: normal
created_at: 2026-09-15T06:16:39Z
updated_at: 2026-09-15T06:45:53Z
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
`content/quantum-observable-universe/lean/QOU/FrobeniusHopfData/PairingVariationalDerivative.lean`,
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
