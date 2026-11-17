---
# qou-tmmt
title: 'GAP: adjudicate the 9 projection-shaped §3b-cond item-5 candidates'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T14:12:30Z
updated_at: 2026-11-15T12:00:00Z
parent: qou-5p7n
---

Found by `bun run scripts/conditional-on-class-hypothesis-audit.ts --projections`
(added 2026-09-04, PR #6662). NOT yet adjudicated — this bean is the work.

## What the filter does

Flags a block whose proof body is a **bare projection** of a bound hypothesis:
`:= h.field …` or `by exact h.field …`, where `h` is a binder of that very
declaration. That is the shape of the one confirmed item-5 violation
(`prop:explicit-central-idempotent`, found and fixed the same day).

It splits `PROJECTION` from `composition`: applying a class field to arguments
that DISCHARGE ITS HYPOTHESES is composition, which is what §3b-cond item 5
asks for. A bare `h.field`, or one applied only to the theorem's own binders,
discharges nothing — the field already IS the conclusion at that instantiation.

## Current output — 9 PROJECTION, 2 composition, of 78 bound blocks

    PROJECTION  cor:knot-factor-borromean-composite         decouple.decouples
    PROJECTION  cor:lr-tensor-character-bridge              h.bridge ν β
    PROJECTION  prop:archimedean-functor-uniqueness         hD.uniqueness τ_arch h_cont h_anti h_pent
    PROJECTION  prop:atom-knot-mass-derivation              h.atom_knot_mass_derivation cert T_w
    PROJECTION  prop:gb-residue-spectral-sum                s.spectral_decomposition
    PROJECTION  prop:hecke-branching-trace-decomposition    h.decomposition lam I beta1 beta2
    PROJECTION  prop:markov-trace-recursive-reducer         ctx.claim_reducer_correct β
    PROJECTION  prop:rho-k-h3a-refinement                   inst.identity data Δ partitions
    PROJECTION  prop:sigma-shell-from-beta-chain-derivation inst.identity data
    composition prop:b1-soft-sharpness-theorem              ctx.depth_bound_of_nonvanishing ctx.lewin_nonvanishing
    composition prop:b1-torus-knot-rows-theorem             ctx.b1_from_tate_rationality ctx.h_bloch_suslin ctx.h_garoufalidis_le

**All 11 are in `binds_other_carrier`** — blocks that mint their own context
class rather than taking the conjecture's published one. That is the predicted
higher-yield bucket: a locally-minted class is freer to carry its author's own
conclusion. **Zero** candidates in `binds_cone_class` now that
`prop:explicit-central-idempotent` is fixed.

Field names on three of them are self-describing: `claim_reducer_correct`,
`inst.identity`, and `h.atom_knot_mass_derivation` (field name == theorem name).

## Limits — read before quoting the 9

- **Sufficient, NOT necessary.** A class can carry the conclusion in a
  rearranged form reachable by `ring`/`simp` and this filter will not see it.
  `prop:proton-mass-substrate-identity` is exactly that and does not appear.
  So 9 is a **LOWER bound** on item-5 violations — the opposite direction from
  every other count in that script, whose header records four narrowings that
  each INFLATED what they claimed.
- **Not verdicts.** `hD.uniqueness τ_arch h_cont h_anti h_pent` applies a field
  to four arguments; whether those discharge hypotheses or are just the
  theorem's own binders decides projection-vs-composition, and the filter
  answers that syntactically. Read each declaration.

## Two bugs found in the filter itself, both fixed, one worth remembering

1. **`\w` is ASCII-ONLY.** Binder names here are routinely `β`, `ν`, `Δ`,
   `τ_arch`. The first cut's binder set missed every Greek one and mis-filed
   THREE blocks as `composition` that are projections. Note the direction:
   this bug caused **under**-flagging, so fixing it raised the count 6 → 9.
2. The declaration-boundary scan did not stop at a module docstring `/-!`, so
   `prop:atom-knot-mass-derivation`'s proof body swallowed the following
   docstring and its argument list was garbage.

Both are the same family as everything else in that file's header: the pattern
decided what could be seen, and the first answer was about the pattern.

## Next step

Open each of the 9 declarations and its bound class; decide whether a field
carries the block's conclusion. Fix as `prop:explicit-central-idempotent` was
fixed — re-encode the class as genuine sub-hypotheses so the theorem composes
them. That is per-block mathematics, not a sweep.


---

## ADJUDICATED 2026-09-04: 2 of 9 read, both CONFIRMED item-5 violations

### 1. `cor:knot-factor-borromean-composite` — CONFIRMED

`folio/quantum-observable-universe/mass-theory/knot-factor-borromean-composite.lean`

    structure BrunnianDecoupling (k : ℕ) (component_factor : ℝ)
        (composite_factor : ℝ) : Prop where
      decouples : composite_factor = component_factor ^ k

    theorem knot_factor_borromean (k : ℕ) (h : ℝ) (composite : ℝ)
        (decouple : BrunnianDecoupling k (1 - h ^ 2) composite) :
        composite = (1 - h ^ 2) ^ k :=
      decouple.decouples

The structure has **exactly one field, and it is the theorem's conclusion**.
Textbook item 5.

Note the file's own comment defending it: *"it genuinely consumes the
`BrunnianDecoupling` hypothesis."* True, and beside the point — consuming a
hypothesis that IS the conclusion is precisely what item 5 forbids. The same
comment records removing a neighbouring vacuity (`∃ a, a = e`), so the author
was auditing for vacuity and this shape passed that filter. **Item 5 is not
visible to a vacuity check.**

### 2. `prop:gb-residue-spectral-sum` — CONFIRMED

    theorem gb_residue_spectral_sum (R) [CommRing R] [LinearOrder R]
        [s : GBResidueSpectralSum R] :
        s.mass = |s.descended| + ∑ ℓ : Fin s.levelBound, s.residue ℓ :=
      s.spectral_decomposition

Field projected directly. And the class's **own docstring already says the
quiet part**: the graded trace is *"supplied freely by the instance … **That
is not encoded here** — no field relates this to `tr_M`, to the filtration, or
to `descended`"*. So the class is documented as asserting nothing structural,
and the theorem projects one of its fields.

### Bonus finding — a same-FQN duplicate, latent not live

`GBResidueSpectralSum` is declared **twice**, both in `namespace QOU.BraidKnot`:

- `folio/quantum-observable-universe/mass-theory/gb-residue-spectral-sum.lean` (block sibling)
- `folio/quantum-observable-universe/lean/QOU/BraidKnot/GBResidueSpectralSum.lean` (library)

i.e. two declarations of `QOU.BraidKnot.GBResidueSpectralSum`. This is the
sibling/library divergence hazard from `qou-e7xv` / PR #6540 §"A cost of this
sweep", and `lean.ref` resolves **sibling-first by file**, so the sibling wins.

**Compared: the field NAMES and types agree for all seven data fields.** The
one multi-line field, `spectral_decomposition`, was truncated by the comparison
and is **NOT** compared — do not read this as "the two are identical". Latent,
not currently diverged as far as checked.

## Still to adjudicate: 7

    cor:lr-tensor-character-bridge              h.bridge ν β
    prop:archimedean-functor-uniqueness         hD.uniqueness τ_arch h_cont h_anti h_pent
    prop:atom-knot-mass-derivation              h.atom_knot_mass_derivation cert T_w
    prop:hecke-branching-trace-decomposition    h.decomposition lam I beta1 beta2
    prop:markov-trace-recursive-reducer         ctx.claim_reducer_correct β
    prop:rho-k-h3a-refinement                   inst.identity data Δ partitions
    prop:sigma-shell-from-beta-chain-derivation inst.identity data

Hit rate so far is 2/2, but two is not a rate — read each.


---

## ALL 9 ADJUDICATED 2026-09-04 — 8 CONFIRMED item-5 violations, 1 legitimate

| block | class.field | verdict |
|---|---|---|
| `cor:knot-factor-borromean-composite` | `BrunnianDecoupling.decouples` | **VIOLATION** |
| `cor:lr-tensor-character-bridge` | `LRTensorCharacterBridge.bridge` | **VIOLATION** |
| `prop:atom-knot-mass-derivation` | `AtomKnotMassDerivationConjecture.atom_knot_mass_derivation` | **VIOLATION** |
| `prop:gb-residue-spectral-sum` | `GBResidueSpectralSum.spectral_decomposition` | **VIOLATION** |
| `prop:hecke-branching-trace-decomposition` | `HeckeBranchingTraceDecomposition.decomposition` | **VIOLATION** |
| `prop:markov-trace-recursive-reducer` | `MarkovTraceRecursiveReducerContext.claim_reducer_correct` | **VIOLATION** |
| `prop:rho-k-h3a-refinement` | `RhoKH3ARefinement.identity` | **VIOLATION** |
| `prop:sigma-shell-from-beta-chain-derivation` | `SigmaShellFromBetaChainDerivation.identity` | **VIOLATION** |
| `prop:archimedean-functor-uniqueness` | `BlochSuslinUniqueness.uniqueness` | legitimate |

In every violation the field's type is the block's conclusion, universally
quantified over the theorem's own parameters, and the proof instantiates it.
**Two classes say so in their own docstrings** — `LRTensorCharacterBridge.bridge`
is annotated *"claim of `cor:lr-tensor-character-bridge`"* and
`HeckeBranchingTraceDecomposition.decomposition` *"claim of
`prop:hecke-branching-trace-decomposition`"*. The authors named the field after
the claim it assumes.

### The one that is legitimate, and why — this is the discriminator

`BlochSuslinUniqueness` carries `d_pentagon`, `d_continuous`, `d_antisymmetric`
(genuine properties of `D`) and

    uniqueness : ∀ φ, Continuous φ → (∀ x ≠ 0,1, φ x⁻¹ = -φ x) →
                 PentagonCoherent φ → ∃ c, ∀ x, φ x = c * D x

— the Bloch–Suslin rigidity theorem, a substantial general claim. The block's
theorem applies it as `hD.uniqueness τ_arch h_cont h_anti h_pent`, **discharging
three non-trivial hypotheses** about `τ_arch` that are the theorem's own
assumptions. That is composition.

**So the discriminator is not "is the field universally quantified" — every
violation above is too.** It is: *does the theorem DISCHARGE hypotheses of the
field, or merely INSTANTIATE its parameters?*

### Limitation of the shape filter, measured

`--projections` classified `prop:archimedean-functor-uniqueness` as
`PROJECTION`, because its arguments `τ_arch h_cont h_anti h_pent` are all
binders of the theorem. The heuristic cannot tell a binder that is a
**hypothesis being discharged** from one that is a **parameter being
instantiated**. So the PROJECTION/composition split is a presentation aid, not
a verdict — as the mode's own header says. 1 false positive in 9.

## Next step per block

Each confirmed one needs the same treatment as `prop:explicit-central-idempotent`
(fixed earlier on this branch): re-encode the class as the genuine
sub-hypotheses of its argument, so the theorem composes them. That is per-block
mathematics — eight separate derivations, not a sweep, and several are
substantial (the LR bridge and the branching decomposition are real theorems).

**Do not "fix" any of them by deleting the theorem or weakening the statement.**


---

## Cross-check against the sibling finding `qou-7yj0` (already merged to main)

`qou-7yj0` (branch `claude/q407-self-assuming-projections-2026-08-21`, landed)
measures a **different** defect: a carrier whose constraining fields relate only
its OWN data fields is **trivially inhabited**, so "conditional on `[C]`" is
decorative. Their test: replicate the class, build an instance from nothing,
`lean`-direct.

**The two defects are independent, and the block sets are DISJOINT.**

- theirs: is the class *inhabitable for free* → the theorem is unconditional
- mine: is the class field *the theorem's conclusion* → the theorem is a
  projection

Their named population (`BorromeanQuark` ×10, `TrefoilElectronMassConj`,
`HypMinimizerUnique`, `CrystalGraphRealization`, `QIntegerMassFormula`,
`CanonicalMarkovWeightsH3`, `CoGroundStateSelection`, `IsOcneanuWeightSystem`,
`CarlemanDeterminacyStieltjes`, `QouObstructionReductionContext`) shares **zero**
classes with my eight. Not a duplicate finding, and not a re-derivation.

### Applying their test to mine — 2 of 8 are BOTH

Evidence: `docs/audits/2026-09-04-item5-carriers-inhabitability.lean`,
`lean`-direct **exit 0**.

| class | trivially inhabited? |
|---|---|
| `GBResidueSpectralSum` | **YES** — `descended := 0`, `levelBound := 0`, `mass := 0`, decomposition by `simp` |
| `MarkovTraceRecursiveReducerContext` | **YES** — `Braid := Unit`, everything trivial |
| `BrunnianDecoupling` | **NO** (negative control) |

So `prop:gb-residue-spectral-sum` and `prop:markov-trace-recursive-reducer`
carry **both** defects at once: the class costs nothing to satisfy AND its field
is the conclusion. Those theorems prove their conclusions from nothing at all.
That is strictly worse than either defect alone and neither audit alone reports
it.

### The control is what makes this a measurement

`BrunnianDecoupling` takes its subject as **parameters** — which is exactly the
parametrised form `qou-7yj0`'s bean recommends as the FIX — and
`¬ BrunnianDecoupling 2 (3:ℝ) 5` is **proved** in the evidence file. So the
method discriminates rather than accepting everything, and `BrunnianDecoupling`
is a live counterexample to any assumption that the two defects travel
together: it is item-5-violating and correctly parametrised at once.

**Consequence for whoever fixes either:** applying `qou-7yj0`'s parametrisation
fix does NOT close item 5, and re-encoding for item 5 does NOT make a carrier
refutable. Both passes are needed, and each should check the other's criterion
on the blocks it touches.


---

## PRIOR ART — credit, and what actually survives as new (2026-09-04, second pass)

I nearly presented the "discharge vs instantiate" discriminator as mine. **It is
not.** `qou-z9ws` (2026-08-30, completed) states it as *"derives vs projects"*
five days earlier, over a **112-entry** population under the existing corpus
criterion **`proof-no-self-assuming-projection`**, with the ledger's own rule:
*a projection is the legitimate Mathlib accessor idiom ONLY when something
builds the bundle.*

And `f744886b3c` on main names the pattern I then repeated:

> Each route flagged on SHAPE and each had to narrow to USE — over-reporting
> first, in the same direction, by roughly the same factor. Whoever builds the
> next detector in this family should start from the narrowed rule and expect
> the first version to over-report.

`--projections` is the **fourth** such route. It flagged on shape, over-reported,
and narrowed to use (discharge-vs-instantiate) — 1 false positive in 9. That is
the predicted behaviour, not an independent discovery, and the convergence note
called it in advance.

## What IS new, measured

**7 of my 8 confirmed blocks are ABSENT from the existing vacuity ledger**
(`docs/audits/lean-vacuity-review-ledger.json`, 406 KB). Only
`GBResidueSpectralSum` appears.

Where each class is declared:

| class | library | sibling | in ledger |
|---|---|---|---|
| `BrunnianDecoupling` | 0 | 1 | no |
| `LRTensorCharacterBridge` | 0 | 1 | no |
| `AtomKnotMassDerivationConjecture` | 0 | 1 | no |
| `HeckeBranchingTraceDecomposition` | 0 | 1 | no |
| `RhoKH3ARefinement` | 0 | 1 | no |
| `SigmaShellFromBetaChainDerivation` | 0 | 1 | no |
| `GBResidueSpectralSum` | **1** | 1 | **YES** |
| `MarkovTraceRecursiveReducerContext` | **1** | 0 | no |

**Six of the seven absences are explained by the sibling surface**: the class is
declared only in a content-block sibling, which sits outside the Lake globs and
is invisible to library-scoped tooling — the same blind spot `qou-e7xv` / #6540
documented for *compilation*, now shown to apply to the *vacuity* detectors too.
The one class with a library twin is the one the ledger has, which is what that
explanation predicts.

**`MarkovTraceRecursiveReducerContext` breaks it.** Library-only, and still
absent. The sibling-blindness account covers 6 of 7, not 7 of 7, and I have not
determined why this one escaped. Do not state the rule without that exception.

## So the honest framing

- the discriminator: **prior art**, `qou-z9ws`, credited;
- the shape→use narrowing: **predicted** by `f744886b3c`, and I reproduced it;
- **new**: the `conditional_on_class` bucket is a reachable population the
  existing detector does not cover, and 6 of the 7 misses are the sibling
  surface.

The right follow-up is therefore **not** another detector. It is extending the
existing `proof-no-self-assuming-projection` sweep to content-block siblings —
one change, covering a whole surface — and separately diagnosing the
`MarkovTraceRecursiveReducerContext` miss, which that change would not fix.


## 2026-10-10 — pointer

Tracked under related carrier M10 of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.

## 2026-11-15 — PR #6681 ported onto main (owner decision), branch `claude/q-rh-item5-port-2026-11-15`

Owner chose "port #6681" in the project thread "Settle open-problem leftovers". #6681 was 4421 commits behind and predates the `content/ → folio/` move, so its block diffs were re-applied 3-way at the new paths.

**Ported (seven of the eight item-5 blocks):** `knot-factor-borromean-composite`, `lr-tensor-character-bridge`, `atom-knot-mass-derivation`, `markov-trace-recursive-reducer`, `rho-k-h3a-refinement`, `hecke-branching-trace-decomposition`, `gb-residue-spectral-sum` (restores the non-vacuous `spectral_sum_finite`; main still had the `Or.inr` form). Plus `docs/audits/2026-09-04-item5-detector-gate-instrumented.md`, `scripts/qa-stale-agent-verdicts.py`, beans `qou-rj0m`, `qou-vstf`, `qou-rdg8`.

**Not ported, main already moved on:**
- `sigma-shell-from-beta-chain-derivation`: main demoted it to a conjecture with no instance and proved `sigma_shell_staircase_vanishes_conventionD`. Merging #6681's re-encoding into that is tied to the open owner question on whether σ_shell is 0 under convention D. Left as main has it.
- Library files from the `qou-tsnp` / `qou-u3wb` side work (`MetallicLPIdentities`, `MetallicPiecewise`, `IwahoriHecke/Tw`, `AlphaShiftTorusKnot`, `shell-closure-nf-term-count`): main fixed the same carriers independently (`tsnp` scrapped as duplicate of `qou-hprp`). Main's versions kept.
- `.qa.json` sidecars and the vacuity witness: to be regenerated, not hand-merged.
