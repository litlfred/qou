---
# qou-ffwk
title: 'GAP: 10 conjecture carriers use a trivially-inhabited ''residual = 0'' placeholder'
status: todo
type: task
priority: normal
created_at: 2026-08-08T15:15:21Z
updated_at: 2026-08-08T15:17:15Z
---


## The defect

Ten conjecture carriers in the QOU library share this field schema:

```lean
class C where
  residual : ℝ
  residual_eq_zero : residual = 0
```

This is **inhabited by `⟨0, rfl⟩`**. The class asserts nothing, so a
downstream `theorem foo [C] : P` proves `P` outright, not `C → P`.
This is the AGENTS.md §3b-tax "the carrier must assert something" rule
(`proof-claims-unencoded`), one step weaker than the empty-marker
`class C : Prop` case: the fields exist, but their conjunction is
satisfiable by a constant, so they carry no content.

Each of these files also carries a docstring naming a *real* claim
(e.g. `VacuumEpsilon`: "Geom(unknot) = 0"), which the schema does not
encode — the `proof-claims-unencoded` shape exactly.

## Why this matters for the de-laundering work

The axiom-and-global-instance de-laundering (PRs #4743, #4750, and the
`TorusKnotMass` / `VacuumEpsilon` / `TwoFiltrationBridge` batch) is
**necessary but not sufficient** for these ten. Removing
`axiom c : C` + `instance : C := c` restores the *no-instance* open
state, but anyone — including a future agent trying to make a red file
green — can re-close it in one line with `instance : C := ⟨0, rfl⟩`,
with no axiom and no `sorry` to show up in `#print axioms`.

**So: de-laundering these classes does not yet make the downstream
`[C]`-conditional theorems meaningful.** Do not report them as
"conditional results" until the fields are refined.

## Inventory (all confirmed by grep on `residual_eq_zero`)

| File | class | instances remaining |
|---|---|---|
| `AppendixSurreals/VacuumEpsilon.lean` | `VacuumEpsilon` | 0 (de-laundered) |
| `AppendixSurreals/LocalInfinitesimalField.lean` | `LocalInfinitesimalField` | 0 (de-laundered) |
| `AppendixSurreals/SpectralNormalForm.lean` | `SpectralNormalForm` | 0 (de-laundered) |
| `AppendixSurreals/QouInfraDischargesGoncharovZeta5.lean` | `QouInfraDischargesGoncharovZeta5` | 0 (de-laundered) |
| `AppendixSurreals/DiophantineBirthday.lean` | `DiophantineBirthday` | 0 (de-laundered) |
| `BraidKnot/BringFigureEightDepth2Witness.lean` | `BringFigureEightDepth2Witness` | 0 (de-laundered) |
| `BraidKnot/BraidGroupNStrand.lean` | `HeckeQuotient` | 0 |
| `Archimedean/HyperbolicVolumeIndependence.lean` | (anon) | **2** |
| `BraidKnot/HabiroResidueSumEquivalence/archimedean_agreement.lean` | `archimedean_agreement` | **1** |
| `BraidKnot/HabiroResidueSumEquivalence/protonExample/archimedean_agreement.lean` | `archimedean_agreement` | **1** |

The four with instances remaining are on bean `qou-up56` (consumers do
not declare `[C]`, so removing the instance breaks them).

## The fix, per file

Refine the fields to the claim the docstring already states. Worked
target for `VacuumEpsilon`:

```lean
class VacuumEpsilon where
  geom : Link → ℝ
  geom_unknot : geom unknot = 0
```

This is not mechanical — each file needs the right carrier type for its
claim, and some of those types (`Link`, the Hoefsmit pipeline's
`Geom`) may not exist in the library yet. Expect this to surface
further gaps rather than close cleanly. **Do not batch-process.**

## Detection

`grep -rl "residual_eq_zero" QOU --include=*.lean` catches this exact
shape. A general detector for "class whose fields are jointly
satisfiable by a constant" belongs in
`scripts/lean-definition-collapsed-audit.py` alongside the existing
signal-A/signal-B logic — currently it only flags collapsed *proofs*,
not collapsed *carriers*.

## FINDING (2026-08-08) — field refinement is NOT sufficient; the blocker is one level down

I set out to do the fix this bean describes — refine `VacuumEpsilon`'s
`residual = 0` schema to the claim its docstring states — and stopped, because
the premise is wrong. Recording why, since the next agent will otherwise spend
the same time discovering it.

### 1. The docstring states the wrong claim

The class docstring says the content is *"vacuum normalisation requires
`Geom(unknot) = 0`"*. Reading the source block
[`conj:vacuum-epsilon`](content/quantum-observable-universe/appendix-surreals/vacuum-epsilon.md),
that is the **strict** vacuum being *relaxed*, not the conjecture. The
conjecture is the opposite:

> `Geom(🝆) = ε ∈ **No**` — a *positive infinitesimal*, with `st(ε) = 0`.

Encoding the docstring literally would have formalised the negation of the
conjecture. Read the `.md`, not the Lean docstring.

### 2. A second carrier for the same conjecture already exists

`QOU/AppendixSurreals/Conjectures.lean:394` declares `class VacuumEpsilon'`,
"factored out of the original `VacuumEpsilon`", with a narrowing audit and an
`st`-image theorem. So the conjecture has **two** carriers: the legacy
placeholder (de-laundered in #4750) and this one. Consolidating them is its
own task; refining the legacy one in isolation would deepen the split.

### 3. And `VacuumEpsilon'` is *also* trivially inhabited

```lean
instance (K : Type) [SurrealField K] : VacuumEpsilon' K where
  exists_epsilon_vacuum := ⟨epsilonSurreal K, rfl⟩
```

compiles. Its only field is `∃ SQ, QOU_VacuumEnergy SQ = epsilonSurreal K`,
and `QOU_VacuumEnergy Q := Q` is the **identity** — its own docstring says
*"placeholder semantics … Makes `VacuumEpsilon` formally provable (witness:
`Q := ε`)"*. So `ε` witnesses it by `rfl`.

### The actual blocker

**The semantic functions these classes would be refined *against* are
themselves identity or absent placeholders**, so any field written over them
is satisfiable by construction:

| placeholder | status |
|---|---|
| `QOU_VacuumEnergy Q := Q` | identity |
| `QOU_ObservabilityNorm Q := Q` | identity |
| `Knot := ℕ` | index carrier, "sufficient to make `Nonempty Knot` provable" |
| `Geom : Link → ℝ` | does not exist anywhere in the corpus |

So this bean's fix is **necessary but not sufficient** — the same shape as the
finding it was created from (de-laundering was necessary but not sufficient
for these carriers). Two levels stacked:

```
axiom-discharged instance   →  removed (#4750)
trivially-inhabited fields  →  this bean
placeholder semantics       →  the real blocker, below both
```

Refining `residual : ℝ` into `geom_unknot : geom 🝆 = ε` only relocates the
vacuity unless `geom` is a genuine function. Introducing `opaque geom` would
help — an opaque global cannot be satisfied by choosing a convenient value —
but that is a modelling decision about the Hoefsmit pipeline, not a schema
edit, and it belongs with whoever owns `Conjectures.lean`'s narrowing work.

### Revised next step

Not "refine ten field schemas". In order:

1. **Consolidate** the duplicate `VacuumEpsilon` / `VacuumEpsilon'` carriers.
2. **Replace the identity placeholders** (`QOU_VacuumEnergy`,
   `QOU_ObservabilityNorm`) with `opaque` constants. That single change makes
   every class field written over them non-trivial, because an opaque global
   cannot be witnessed by `rfl`. It is likely the highest-leverage edit in
   this whole area and is *not* per-carrier work.
3. Only then refine the per-carrier schemas, against real functions.

Step 2 is cheap and mechanical; I have not done it because it changes the
semantics of a file with an active narrowing audit, and stepping on that is
the coordination failure AGENTS.md warns about. Worth a note to whoever owns
`Conjectures.lean` before it is attempted.

## Progress 2026-08-16 — two carriers refined; and the inventory is short by six

Branch `claude/ffwk-archimedean-agreement-carriers-2026-08-16`. Two of the ten
done, deliberately not batched, per this bean's own instruction.

### The two `archimedean_agreement` carriers

PR **#3793** proposed exactly this fix in July and was **closed unmerged**
(2026-08-03). Half of it had landed by another route — the fabricated
`axiom` + global `instance` pair is gone — but the contentless class body
survived, and the file's own comment recorded that it was inhabited by the
trivial term. This lands the class body.

**The shape, and why it is the fix.** The placeholder bundles the choice of the
scalar *inside* the class, so any instance picks the value that makes its own
field true. Moving the compared quantities *out* as class parameters means an
instance must discharge the claim for whatever data the caller supplied:

```lean
class archimedean_agreement (Braid : Type*)
    (habiroTraceEval gbMass : Braid → ℝ) (ε : ℝ) : Prop where
  tolerance_nonneg : 0 ≤ ε
  agree : ∀ K : Braid, |habiroTraceEval K - gbMass K| ≤ ε
```

**Faithfulness checks against the source blocks**, since this bean's 2026-08-08
finding was that a docstring stated the wrong claim:

- `conj:gs-archimedean-agreement-trace` quantifies over *"every closed braid K
  admitting a Habiro polynomial trace … and a Gröbner–Shirshov mass value"*, so
  the generic carrier quantifies over `K`. A per-braid class would not be the
  conjecture.
- `conj:gs-archimedean-agreement-residue` states **one** identity at **one**
  braid, so the `protonExample` carrier is not quantified — and `specialises`
  derives it from the generic one, which is the block's own sentence ("this
  specializes the generic archimedean agreement to the proton") checked rather
  than asserted twice.
- Both blocks write `≈` and record agreement "to machine precision", so the
  tolerance is an explicit parameter rather than hidden in an `=`. Encoding
  equality would have asserted more than the corpus does.
- The residue block's recorded numeric value is **not** written into the class.
  A carrier fixing a decimal claims more than the conjecture and would need
  re-editing whenever the pin moves.

**What is deliberately not modelled.** `Braid` stays abstract and both pipelines
enter as caller-supplied functions. No Habiro-polynomial type and no
Gröbner–Shirshov mass functional exist in this library; inventing either here
would assert a construction the corpus does not have. This is the "expect this
to surface further gaps" case this bean predicted — the gap is real, and the
carrier is written so it does not paper over it. When those pipelines land they
instantiate the two functions and the class statement is unchanged.

**Anti-vacuity, both directions.** Tightening a vacuous carrier can overshoot
into one nobody can instantiate, which is a false claim rather than an open one.
Both directions are stated, and neither is an `instance`, so typeclass
resolution cannot pick either up and silently close a downstream hypothesis:

- `nonempty_of_eq` — inhabited when the two pipelines coincide, so emptiness is
  not what makes the class open;
- `not_of_gap` — **refutable** at two pipelines a fixed distance apart with a
  smaller tolerance. This is the property the old schema lacked entirely:
  `⟨0, rfl⟩` closed it for every choice of everything, so no wrong pipeline
  could ever fail it.

Verification: both modules compile (`lean-direct-cone -k`, ok=2); `#print axioms`
on all four declarations gives `[propext, Classical.choice, Quot.sound]` — no
`sorryAx`; `check-base-ring` PASS, `check-wall-side` PASS on both. No instance
added, so the open state is preserved. No external consumer existed
(grep-verified), so no downstream signature broke.

### The detector grep, and a trap it would have hit

This bean's inventory method is a grep for the vanishing field's name. Writing
the old schema verbatim in a changelog would leave a refined file matching that
grep forever — a false positive generated by the fix itself. Both files describe
the old shape in prose instead and name it nowhere, so they drop out cleanly:
the corpus count goes **16 → 14** files.

### The inventory is short by six

This bean lists **10** carriers. Grepping current main finds **16**. The six not
listed are co-located `.lean` stubs under content directories rather than library
modules:

```
braids-and-knots/markov-trace-inductive-limit.lean
mass-endomorphism/hecke-algebra-type-scaffold.lean
mass-endomorphism/markov-trace-operator-construction.lean
mass-endomorphism/phi-d-syt-count-conjecture.lean
mass-theory/ck-extraction-from-algebraic-rules.lean
mass-theory/typed-b3-sub-braid-extraction.lean
```

Per `GroundRingAnnotations`, co-located stubs are documentation and are not
compiled by `lake build`, so they are lower severity than the library carriers —
but they sit next to the `.ts`/`.md` blocks a reader actually opens, which is
arguably worse for the reader even if it is better for the build. Not triaged
here; recorded so the next pass starts from 14, not 8.

### Remaining, unclaimed

Eight library carriers (`VacuumEpsilon`, `LocalInfinitesimalField`,
`SpectralNormalForm`, `QouInfraDischargesGoncharovZeta5`, `DiophantineBirthday`,
`BringFigureEightDepth2Witness`, `HeckeQuotient`, `HyperbolicVolumeIndependence`)
plus the six stubs above. The 2026-08-08 finding on `VacuumEpsilon` still stands
and should be read before attempting it — its docstring states the claim being
*relaxed*, not the conjecture.

> **Filename note for the next agent.** This bean's *title* was updated
> ("VacuumEpsilon class fields…" → "10 conjecture carriers…") but its filename
> still carries the original slug. Appending with `>>` to a path derived from
> the current title silently creates a **second file for the same bean ID** —
> I did exactly that on 2026-08-16 and caught it only because `git status`
> showed `A` instead of `M`. Resolve the path with
> `ls .beans/ | grep <id>`, never by slugifying the title.
## Progress 2026-08-16 (2) — `BringFigureEightDepth2Witness`

Branch `claude/ffwk-bring-fig8-carrier-2026-08-16`. Third of the ten.

**Which half is the conjecture.** The block asserts a chain,
`Vol(S³\4₁) = std(2 Im Li₂^q(e^{iπ/3})) = 2 Cl₂(π/3)`, and its own status note
splits it: the evaluation is *"numerically discharged at 50 digits via mpmath"*
with a committed witness, and only the **structural identification** is
conjectural. So the class carries **one** field. Folding the evaluation in as a
second field would mark verified work as conjectural — the mirror image of the
defect this bean exists to fix. It enters instead as a hypothesis of
`evaluates_to`, so the two halves' provenance stays distinct.

**Exact equality, not a tolerance** — unlike the `gs-archimedean-agreement-*`
carriers done earlier today. Those blocks write `≈` and record agreement "to
machine precision", so a tolerance parameter is faithful. This block writes `=`,
and its 50-digit figure is *evidence for* the identity rather than a claim that
it holds only approximately. Same bean, opposite encoding, because the blocks
differ.

**Depth is not a field.** Both sides carry depth 2, but the block derives that
match "by construction of the Bloch–Wigner regulator" — a fact the conjecture is
stated against, not part of what it asserts. Encoding it would over-claim.

### New gap surfaced: the conditionality cannot be expressed

The block says the conjecture is *"conditional on
`conj:gb-depth-period-correspondence`"*. That is exactly the §3b-cond instance-
parameter shape — and it **cannot be written**, because the corresponding class
`QOU.AlgebraicSubstrate.GBDepthPeriodCorrespondence` exists only as a
**co-located stub** (`mass-theory/gb-depth-period-correspondence.lean`), which
per `QOU.GroundRingAnnotations` is documentation that `lake` does not compile.
A library module under `lean/QOU/` cannot import one.

So an instance of `BringFigureEightDepth2Witness` does **not** discharge the
correspondence it rests on, and the elaborator cannot enforce that it is
carried. Documented in the file rather than dropped. Making it enforceable means
promoting that carrier into the library tree — separate work, not attempted.

This is the second instance of the same structural problem: the earlier pair
could not name a Habiro-polynomial type or a Gröbner–Shirshov mass functional
because neither exists in the library. **Library carriers cannot depend on
content-directory stubs**, and several conjectures are stated in terms that only
exist there. Worth its own bean if a third case appears.

### Two stale statements corrected in passing

The old header said "the `noncomputable instance` is the conjectural witness
whose `sorry` represents the open conjecture" while the body two paragraphs
below said no instance is provided — the axiom-and-instance pair had been
removed without the header following. And what was removed was an `axiom`, not a
`sorry`; the distinction matters because a `sorry` at least surfaces as
`sorryAx`.

### Verification

`lean-direct-cone -k` ok=1; `#print axioms` on all three declarations gives
`[propext, Classical.choice, Quot.sound]`, no `sorryAx`; `check-base-ring` PASS;
`check-wall-side` PASS; both `lean-content-siblings` local gates exit 0.
Anti-vacuity both directions (`nonempty_of_eq`, `not_of_ne`), neither an
`instance`. No instance added — open state preserved.

Detector count: main is at 16 files; this branch takes it to 15, and the
`archimedean_agreement` branch takes it to 14. Both landed together give 13.

### `HeckeQuotient` — the inventory names the wrong class

The row `BraidGroupNStrand.lean | HeckeQuotient` is misattributed. The class in
that file carrying the vanishing-scalar shape is **`MarkovTraceN`**, and it is a
harder case than the ones done so far: it bundles four Markov axioms M1–M4, of
which `tau_identity = 1` is already substantive and only the cyclic and
stabilisation residuals are placeholders. It should be split field by field
rather than replaced wholesale. Not attempted here.

## Progress 2026-08-16 (3) — `SpectralNormalForm`

Branch `claude/ffwk-spectral-normal-form-2026-08-16`. Fourth of the ten, and the
first that needed **no invented types**: `SurrealField`, `IsInfinitesimal`,
`IsFinite` and `OmegaOrder.Ow` all already exist, so the conjecture is stated in
the corpus's own vocabulary rather than against caller-supplied stand-ins.

**What the conjecture is.** The block's three parts share one thing: a bridge
between two independent structures on `K` — the *order* (infinitesimal, finite,
from `SurrealField`'s `LinearOrder`) and the *valuation* (`Ow`, the leading
Conway exponent). `OmegaOrder` axiomatises `Ow`'s multiplicativity and its
behaviour under real rescaling and **says nothing relating it to the order**.
The conjecture is exactly that relation, so the two fields are

- part 1 (gap closure) → `IsInfinitesimal x ↔ Ow x < 0`
- part 3 (singularity) → `¬ IsFinite x ↔ 0 < Ow x`

**The `x ≠ 0` side condition is load-bearing, not decorative.** `0` is
infinitesimal (`zero_isInfinitesimal`) while `Ow 0 = ⊤` by `Ow_zero`, and `⊤` is
not `< 0`. Without the hypothesis part 1 is outright **false at zero**; same for
part 3, where `0` is finite and `⊤` is `> 0`. Caught by checking the statement
against the existing lemmas rather than by transcribing the block.

**Part 2 is deliberately not a field.** It reads off *rates* — `Ow(Δ) = -n` is
polynomial closure of order `n`, a value in `(-ω·2, -ω)` signals transcendental
quantum-dilogarithm behaviour. That classifies the exponent once parts 1 and 3
are granted; encoding a rate table as fields would claim the classification is
part of what must be assumed.

**Anti-vacuity, by a different route than the earlier three.** No degenerate
data is available to refute against here, so instead `Ow_normalises_on_ofReal`
derives from the two fields that `Ow (ofReal r) = 0` **exactly**, for every
non-zero real `r`. `OmegaOrder` alone cannot give this: `Ow_ofReal_mul` says
rescaling by a non-zero real leaves the leading exponent *unchanged*, which
constrains differences and never fixes an absolute value. So the class demonstrably
adds content, and an instance cannot be manufactured by adjusting `Ow` freely.
`not_infinitesimal_and_not_finite` exercises both fields together.

**Non-emptiness is NOT shown, and that is a real gap.** It needs an `OmegaOrder`
instance and **this tree has none** — `Asymptotics.lean` says so in its own
header ("Mathlib does not yet expose Conway normal form on `𝐍𝐨`, so neither
class is populated here"). `HyperrealLimitTransfer.lean` has a `SurrealField ℝ*`
model but no `Ow` for it. So satisfiability is untested in either direction.
Recorded rather than papered over with a degenerate instance — which is what the
old schema effectively was.

Verification: compiles (`lean-direct-cone -k` ok=1); `#print axioms` gives
`[propext, Classical.choice, Quot.sound]` on both derived theorems, no
`sorryAx`; `check-base-ring` PASS; `check-wall-side` PASS; both
`lean-content-siblings` local gates exit 0; orphan gate exit 0; `run-validate`
exit 0. No instance added.

Detector count **13 → 12**.

### Running total

Four of ten library carriers done (`archimedean_agreement` ×2,
`BringFigureEightDepth2Witness`, `SpectralNormalForm`); count 16 → 12.
Remaining library: `DiophantineBirthday`, `LocalInfinitesimalField`,
`QouInfraDischargesGoncharovZeta5`, `VacuumEpsilon`,
`HyperbolicVolumeIndependence`, and `BraidGroupNStrand` (whose class is
`MarkovTraceN`, not `HeckeQuotient` as the inventory says). Plus six co-located
stubs this bean's inventory omits.

## Progress 2026-08-16 (4) — `DiophantineBirthday`

Branch `claude/ffwk-diophantine-birthday-2026-08-16`. Fifth of the ten.

**Only one of the block's four parts is encoded, and that is the point.**

- **Part 1 (algebraic rigidity)** — "if `α` is algebraic of degree `d` then
  `b_α(n) = O(log n)`" — is unhedged and is the field. The implied constant is
  existential and `α`-dependent because the block ties it to the degree; a
  single global constant would claim more than the block does.
- **Part 2 (transcendental depth) is deliberately NOT encoded.** The block says
  "if `α` is transcendental *(of 'generic' type, e.g. Liouville number)*". The
  parenthesis is a hedge — the claim is for a generic subclass, not for every
  transcendental. Writing `∀ α, Transcendental ℚ α → …` would assert the
  unhedged converse the corpus does not. Inventing an `IsGenericTranscendental`
  predicate to carry the hedge would be worse: a stand-in with no definition
  anywhere.
- **Parts 3 and 4** (Roth threshold, continued-fraction correspondence) need the
  continued-fraction expansion, which nothing in this library constructs.

**The discrimination survives on the unhedged half alone.**
`transcendental_of_not_logarithmic` derives from part 1 that a number whose
trajectory outruns every logarithmic bound cannot be algebraic. That *is* the
block's title — "algebraic vs transcendental numbers are separated by birthday
trajectory". Encoding part 2 would have added a converse the separation does not
need. Worth remembering as a general move: when a block hedges half a
biconditional, check whether the headline follows from the unhedged half before
reaching for a stand-in predicate.

**`trajectory` is caller-supplied**, like the `archimedean_agreement` pipelines:
`b_α` is defined in the block by minimisation over bounded-denominator rational
approximations, and this library constructs no such function.

**Anti-vacuity, both directions, and this time both are concrete:**

- `nonempty_of_const_zero` — the identically-zero trajectory satisfies the class
  (`0 ≤ 1·log n + 1` for `n ≥ 1`), so openness is not an artefact of emptiness.
- `not_of_quadratic` — the quadratic trajectory is **refuted**: `0` is algebraic
  and `n²` outruns every `C·log n + C`, via `log n ≤ n − 1`. A genuine
  countermodel, not just a restatement — which is what the earlier
  `SpectralNormalForm` could not have, since no `OmegaOrder` instance exists to
  build one from.

Also fixed a wrong docstring link: it pointed into `appendix-surreals/` and the
block lives in `appendix-surreals-archimedean/`.

Verification: compiles (ok=1); `#print axioms` `[propext, Classical.choice,
Quot.sound]` on all three, no `sorryAx`; base-ring PASS; wall-side PASS; both
siblings gates exit 0; orphan gate exit 0; run-validate exit 0. No instance
added.

Detector count **12 → 11**.

### Running total

Five of ten library carriers done; count 16 → 11. Each needed a **different**
encoding — tolerance parameter, exact equality, structural bridge between two
typeclass structures, and now an asymmetric one-half-only encoding — which is
why this bean's "do not batch-process" instruction is right.

Remaining library: `LocalInfinitesimalField` (needs sheaf/scheme machinery for
"ε is a sheaf across a scheme X" — likely blocked the way
`GBDepthPeriodCorrespondence` was), `QouInfraDischargesGoncharovZeta5`,
`VacuumEpsilon` (blocked on its 2026-08-08 docstring finding),
`HyperbolicVolumeIndependence`, `BraidGroupNStrand` (class is `MarkovTraceN`,
wants field-by-field splitting). Plus the six co-located stubs this bean's
inventory omits.
