---
# qou-s7z2
title: WenzlTowerStep at the Markov trace over the TL_n quotient (successor to the refuted qou-vndn)
status: in-progress
type: task
priority: normal
created_at: 2026-08-26T17:57:00Z
updated_at: 2026-09-26T17:41:43Z
---

Successor to qou-vndn, whose premise ("Hecke radical vanishing") is refuted at
convention D: the radical does not vanish on H_n, it IS the TL ideal. See
qou-vndn for the proved invariant and the exact symbolic determinant.

## The target

Discharge `QOU.Machinery.HeckeTower.WenzlTowerStep`'s field at the MARKOV trace
over the quotient TL_n(delta), where the pairing IS nondegenerate:
`QOU.QBeta.MarkovGramDegenerate.pairing_descends` +
`mem_radical_of_pairing_zero`, both already proved.

## Why this is real work and not a rename

Both hypotheses of the class are stated on H_n objects:
- `HeckeBraidedPresentationOfRank q rank Hn1 sigma_n1` -- the braided
  presentation has to be restated for the quotient (the generators descend, but
  that needs saying).
- `iota : Hn ->a[R] Hn1` -- the tower inclusion has to be shown to descend to
  TL_n -> TL_(n+1) compatibly with the radical.

Neither is automatic and neither is currently in the corpus in that form.

## Already available, do not re-derive (this is the qou-kzjl lesson)

- `TraceNilpotent` -> `TraceFormSemisimple` -> `RegTraceGram` ->
  `HeckeGenericSemisimple` -> `HeckeGramFactorial`: the whole abstract ladder
  from a nondegenerate trace form to semisimplicity, sorry-free.
- `QOU.Machinery.HeckeRank.wenzlTowerStep_regTrace` (PR #5842): the class
  discharged at general rank for the REGULAR trace, plus the finding that
  hypothesis 1 (`IsSemisimpleRing Hn`) is not consumed.
- `QOU.QBeta.TemperleyLiebTower`: convention-D weights, radical two-sidedness.

## Open input, unchanged from HeckeGramFactorial's own note

The general determinant value in the n!-dimensional T_w basis -- the classical
Schur-element product formula. n=2 is done
(`QOU.Hecke.H2CompanionRep.h2GramFromRep_det`, det = [2]_q^2). n=3 is computed
symbolically in gram-matrix-h3-symbolic.md but for the MARKOV form, where it is
0 at convention D -- that is the refutation above, not a rung of this ladder.
No fabricated instance may stand in for the general value.


## Brick 1 LANDED (PR #5850, 2026-08-26): the quotient now exists as an object

`QOU/QBeta/MarkovTraceQuotient.lean`, sorry-free, 10 declarations, 3 of them
depending on no axioms at all.

The gap turned out to be more concrete than this bean anticipated. The corpus
says "H_n / rad tau = TL_n(delta)" in several places, but that phrase had NO
OBJECT in Lean: traceRadical is a Set A, and pairing_descends is a congruence
statement, not a descent to a quotient type. Mathlib's TwoSidedIdeal.mk' wants
six fields and the corpus had two -- the three ADDITIVE closures were missing,
because TemperleyLiebTower states the radical for a bare tr : A -> R with only
[Zero R], so there was no addition on the target to close under.

Supplied: the additive closures, traceRadicalIdeal (TwoSidedIdeal), TraceQuot
(the quotient ring), quotTrace (descended; rad is inside ker tau by taking
b = 1, which is where unitality is spent), and quot_pairing_nondegenerate in
exactly WenzlTowerStep.semisimple_ascend's shape.

Non-vacuity guarded (one_not_mem_traceRadical / quot_one_ne_zero /
quot_pairing_one): without them the nondegeneracy would hold trivially on the
zero ring. Base ring [Module R A] not [Algebra R A], per 7c.

## What brick 1 is NOT

It is not WenzlTowerStep discharged at the Markov trace. Still needed, and
neither is automatic:

1. The braided presentation restated for the quotient -- the generators descend,
   but that needs proving, not asserting.
2. The tower inclusion TL_n -> TL_(n+1) shown to descend from H_n -> H_(n+1)
   compatibly with the radical.

Unchanged: HeckeGramFactorial's open input, the general T_w-basis determinant
(the classical Schur-element product formula). n=2 done; no fabricated instance
may stand in for the general value.


## Brick 3 LANDED as PR #5853 (2026-08-26): the tower is INJECTIVE

`QOU/QBeta/TLTowerRadicalDescent.lean`, 4 declarations, sorry-free, axiom-clean.

Set out to prove preservation (iota carries rad tau_n into rad tau_{n+1}) and
got REFLECTION as well, which is worth more:

  iota a in rad(tau_{n+1})  <->  a in rad(tau_n)

Preservation alone gives a map of quotients. Reflection makes it INJECTIVE, so
TL_n embeds in TL_{n+1} rather than merely mapping to it -- i.e. the quotients
are a TOWER, not a sequence of unrelated algebras. Unexpected, and it is the
brick's real content.

Mechanism: a bare inclusion cannot do this, because membership in rad(tau_{n+1})
quantifies over all of H_{n+1}, not over iota's image. The conditional
expectation is what connects them, via the bimodule law at z = 1
(epsilon_inclusion_mul) moving a test element back down. Preservation spends
BIMODULE; reflection spends RETRACT. Both fields of HeckeConditionalExpectation
are load-bearing.

CONDITIONAL (3b-cond): HeckeConditionalExpectation has NO instance. The
implications are proved; the premise is not established.

## Bricks 1-3 status

1. #5850 MERGED -- the quotient exists as an object (TwoSidedIdeal + quotient
   ring + descended trace + nondegeneracy in WenzlTowerStep's shape).
2. #5852 OPEN -- the braided presentation descends (needed an Algebra instance
   Mathlib does not supply; a scalar-action diamond shaped the proof).
3. #5853 OPEN -- the tower inclusion detects the radical exactly; injectivity.

## What is STILL not done

No WenzlTowerStep instance at the Markov trace. Remaining: assemble bricks 2
and 3 into the class. And untouched by all three bricks --
HeckeGramFactorial's own open input, the general T_w-basis determinant (the
classical Schur-element product formula). n=2 done; no fabricated instance may
stand in for the general value.

MERGE NOTE: #5852 and #5853 both anchor guard-registry entries at the same line
and will conflict in scripts/lean-axiom-guard.py. Both sides are pure additions;
keep both.


## Still open — but one named prerequisite landed after this bean was written (checked 2026-09-06)

Reached by `scripts/bean-staleness-triage.py`. **Genuinely open, and correctly
so**: there is **no instance of `WenzlTowerStep` anywhere in the tree**. The
only mention outside its own declaration is a *negative* result —
`QBeta/TraceNondegeneracyInsufficient.lean:43`, *"So an instance of
`WenzlTowerStep` at a general trace cannot be obtained from …"* — which is
consistent with this bean's predecessor `qou-vndn` being refuted, not with the
work having quietly happened.

### What changed under it

`71413d0c0f` (2026-08-30, bean `qou-twwf`) landed
`QOU/Hecke/HeckeTower.lean`, +73 lines:

```lean
noncomputable def freeIncl : …                     -- on the free algebra
theorem freeIncl_rel  (h : HeckeRel K q n x y) : … -- Hecke relations preserved
noncomputable def incl : …                         -- H_n(q) →ₐ H_{n+1}(q)
```

**Why that is upstream of this bean rather than beside it.** `WenzlTowerStep`
takes the inclusion as a *class parameter*, not a field:

```lean
class WenzlTowerStep (R) [Field R] (q : R) (rank : ℕ)
    (Hn Hn1) [Ring Hn] [Ring Hn1] [Algebra R Hn] [Algebra R Hn1]
    (σn1 : ℕ → Hn1) [HeckeBraidedPresentationOfRank q rank Hn1 σn1]
    (ι : Hn →ₐ[R] Hn1) (trn1 : Hn1 → R) : Prop where
  semisimple_ascend : …
```

so any instantiation has to *supply* a concrete `ι`. `qou-twwf`'s `incl` is
exactly such a map at the H-level, and it is **constructed** — built through
the free algebra with `freeIncl_rel` proving the Hecke relations descend —
rather than assumed. This belongs in this bean's own **"Already available, do
not re-derive"** section, which is there precisely because of the `qou-kzjl`
lesson.

### What is NOT thereby done

This bean's two stated obstacles are unchanged in substance:

1. **The braided presentation must be restated for the quotient.**
   `HeckeBraidedPresentationOfRank` is a class parameter on `Hn1`; the
   generators descend to `TL_n(δ)`, but that needs proving and saying.
2. **The inclusion must be shown to descend**, `TL_n → TL_{n+1}`, *compatibly
   with the radical*. `qou-twwf` gives the H-level map; the descent through
   `MarkovGramDegenerate.pairing_descends` / `mem_radical_of_pairing_zero`
   (both already proved, both cited by this bean) is the actual work.

So the honest position is: **prerequisite (2) has its H-level half constructed
and its descent still open**, and (1) is untouched. Left in-progress at
unchanged status — this is real Lean work, not a triage item, and nothing here
shortens it beyond removing one construction from its critical path.


## 2026-09-26 — the `wtrace` / `trLim` half of this is now stated (PR #7458)

This bean's premise is unchanged and it **stays open**: `WenzlTowerStep` over the
`TL_n` quotient is not discharged. What *has* landed is the piece a corpus-grep
identified as the one thing missing from the otherwise-settled picture — the
negative **stated about the carriers the tower results actually use**, rather
than abstractly:

```lean
OcneanuTraceNotFaithful.exists_nonzero_wtrace_orthogonal   -- H_3(q), wtrace
HeckeColimitNotFaithful.exists_nonzero_trLim_orthogonal    -- HeckeLim, trLim
HeckeColimitNotFaithful.not_isFaithful_trLim
```

Assembled from this bean's own bricks plus two facts already on `main` —
`wtrace` is *defined* as the Frobenius sum (`wtrace_apply` is `rfl`) and
`ocneanuWeight_conventionD_eq_zero_of_three_rows` is unconditional. Nothing here
re-derives `MarkovGramDegenerate` or `MarkovTraceQuotient`; only one direction and
one element were needed.

**What this gives the WenzlTowerStep work.** The new
`MathlibExt/MarkovTraceRadical.lean` carries the radical as a first-class object
at the abstract `MarkovTrace` level — `rad`, `IsFaithful`, the two-sided-ideal
lemmas, `one_notMem_rad`, and the lifting chain
`tr_mul_sandwich_of_orthogonal` → `tr_mul_eq_zero_of_mem_sup` →
`tr_mul_eq_zero_of_mem_shiftedUpTo` → `mem_rad_of_exhausted`. That last chain is
`TowerSpan`-driven and is probably reusable for the quotient side: it is the
statement that orthogonality relative to one filtration stage propagates to all
higher stages, which is the tower-compatibility this bean's brick 3
(`TLTowerRadicalDescent`) currently gets only *conditionally*, resting on the
open `HeckeConditionalExpectation` class. The version here needs no such class —
only cyclicity, Markov, and `TowerSpan` — but it gives the FORWARD direction only,
not the reflection `ι a ∈ rad ↔ a ∈ rad` that brick 3 states. Worth checking
whether brick 3's forward half can be discharged from it and the class narrowed
to the converse.

Bean `qou-r7kp` (completed) has the full record. Note also `qou-6moa`: AGENTS.md
cites `markovWeights_eq_jones_of_threeRow_eq_zero` for its own hypothesis, and
that declaration is cited at ~35 corpus sites, so anything in this arc quoting it
for `y_(1³) = 0` under D should be re-read.


## 2026-09-26 (later) — the ⊇ half of "the radical is the TL ideal" at the wtrace carrier

```lean
QOU.SchurWeyl.WtraceRadicalTwoRow.mem_rad_of_twoRow_blocks_vanish
```

Anything annihilated by every at-most-two-row block is in the radical of the
Ocneanu trace form — **at every level**, not just at `n = 2` as in PR #7458. Two
facts already on `main` do it: `wtrace` is *defined* as the Frobenius sum
(`wtrace_apply` is `rfl`), and `ocneanuWeight_conventionD_eq_zero_of_three_rows`
kills every shape with a third row. Each summand dies for one of two reasons and
the case split is on `d.rowLen 2`.

### 🛑 The ⊆ half is NOT written, and the blocker is named

It needs two inputs:

1. **A pairing fact** — a nonzero real matrix is seen by some matrix under the
   trace form (`∃ N, (M * N).trace ≠ 0`, single-entry witness). Standard; **not**
   the obstacle. I started it and stopped: the Lean plumbing
   (`Matrix.single`, `mul_single_apply_same` / `_of_ne`) costs more than the
   content, and it is pointless while (2) is open.
2. **The ≤2-row weights must be NONZERO.** This is the obstacle. The corpus has
   it on `schurPrincipal` (`WenzlWeightVanishing.conventionD_weight_ne_zero_of_two_rows`)
   but the statement at the level of `ocneanuWeight` — what `wtrace` is actually
   defined from — is `conventionD_ocneanuWeight_eq_zero_iff_of_wenzl`,
   **conditional on `IsOcneanuWeightSystem`, which has no instance.**

So the reduction is the deliverable: **the only missing mathematical input to
identifying the radical at this carrier is the non-vanishing of the ≤2-row
Ocneanu weight.** Writing the conditional half and calling the radical
"identified" would be the `sorry-free ≠ derived` failure.

This does not move this bean's `WenzlTowerStep` premise, which stays open.


## 🛑 RETRACTION (2026-09-26, same day as the claim) — the ⊆ half is NOT blocked on Wenzl's theorem

An earlier entry on this bean, `WtraceRadicalTwoRow.lean`'s docstring, and PR #7460's
body all recorded the ⊆ direction of the `wtrace` radical identification as blocked:
it needs the ≤2-row Ocneanu weights nonzero, the only corpus statement of that is
`conventionD_ocneanuWeight_eq_zero_iff_of_wenzl`, and that is conditional on the class
`QBeta.IsOcneanuWeightSystem`, which has **no instance** — so the ⊆ half would be a
§3b-cond result on a premise nobody has established.

**The premise half is right; the conclusion is wrong, because the reasoning went
through the wrong object.** `IsOcneanuWeightSystem` relates an **opaque** weight family
`y` to `schurPrincipal` — an instance of it really is Wenzl's theorem, and its docstring
says exactly that. But the ⊆ direction never needed the class. It needs
`ocneanuWeight q z_D mu ≠ 0` for `mu` with at most two rows, and `ocneanuWeight` is a
**closed form** in `SchurWeyl/OcneanuWeight.lean`, so that is provable directly from the
genericity `wtrace` already carries.

**Proved, no sorry, no instance, no Wenzl theorem** — PR #7461,
`SchurWeyl/OcneanuWeightTwoRowNonzero.lean`:

    ocneanuWeight_conventionD_ne_zero_of_two_rows {R} [Field R] (q : R)
      (hq0 : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0)
      (hgen : ∀ k, 0 < k → (q ^ 2 : R) ^ k ≠ 1)
      (mu : YoungDiagram) (h : mu.rowLen 2 = 0) :
      ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) mu ≠ 0

Five theorems. At `z_D = q³/(q²+1)` the substitution gives `q²−1−q·z_D = −1/(q²+1)`, so
each numerator factor collapses to `(q^{2j+4} − q^{2i})/(q²+1) =
q^{2i}((q²)^{j+2−i} − 1)/(q²+1)`, nonzero when `i ≤ j+1` — which `rowLen 2 = 0` supplies
(every cell then has row ≤ 1). Denominator nonzero by the same `hgen` at the hook length,
positive because a cell's own arm contains it. Exact mirror of
`ocneanuWeight_conventionD_eq_zero_of_three_rows`: a third row gives a cell of content
`−2`, so `q^{2(c+2)} = 1` and the factor dies. **Two rows is the boundary.**

Verification: `lean -DautoImplicit=false -s 65536`, RC=0 first try, 0 diagnostics.
`#print axioms` clean (no `sorryAx`). Two mutants each required to fail and each does:
`rowLen 3` for `rowLen 2` → rewrite failed; dropping `hij : i ≤ j+1` → omega could not
prove. Not content-swept — ~1.1 GB free against the shadow's ~2.3 GB.

### The error class, worth more than the theorem

I conflated *"the corpus's general statement about weight systems is unproved"* with
*"this particular weight is not known to be nonzero."* Only the first is true. **Check
whether the object in hand is opaque or closed-form before inheriting a blocker from an
abstract statement about its family.** A class carrying an abstract family is not the
only route to a fact about a concrete member of it.

### What actually remains for ⊆ — neither blocked

1. A matrix-pairing lemma: `M ≠ 0` over a field ⇒ `∃ N, (M * N).trace ≠ 0`, witnessed by
   `Matrix.single j i 1` at a nonzero entry. Standard; never the obstacle.
2. Block isolation via `heckeProduct_surjective` — hit one Wedderburn summand and zero the
   rest, as `OcneanuTraceNotFaithful` already does for the column shape.

Together with #7461 these give `rad(wtrace) =` the span of the `ℓ(λ) ≥ 3` blocks — an
identification, not an inclusion. **Unwritten, which is a different thing from blocked.**

`WenzlTowerStep` and `HeckeGramFactorial`'s open `T_w`-basis determinant are untouched by
this and stay open — this bean is NOT closed.


## ⊆ CLOSED — the radical is now IDENTIFIED, not merely bounded (2026-09-26, PR #7461)

Following the retraction above, both remaining pieces are written and verified. The
radical of `wtrace` is **exactly** the three-row part.

`SchurWeyl/WtraceRadicalTwoRowSubset.lean`:

    exists_trace_mul_ne_zero        M ≠ 0 over a CommRing ⇒ ∃ N, (M * N).trace ≠ 0
                                   (single-entry matrix at (j,i); the product's
                                   diagonal is supported at i and reads M i j)
    notMem_rad_of_twoRow_block_ne_zero   ⊆ : a live ≤2-row block is VISIBLE to wtrace
    mem_rad_iff_twoRow_blocks_vanish     the identification, as an iff

The block isolation is `heckeProduct_surjective` realising `Function.update 0 lam₀ N`,
so every block but `lam₀` contributes 0 to the Frobenius sum and the surviving term is
`w_d · (M·N).trace` — a product of two nonzero reals, the weight by
`ocneanuWeight_conventionD_ne_zero_of_two_rows`.

Two plumbing notes worth keeping, both about avoiding transport:

- The Frobenius sum is indexed by `{ν : YoungDiagram // ν.cells.card = n+1}` while
  `heckeProduct` is indexed by `Partition (n+1)`. `Equiv.sum_comp (partitionShapeEquiv _)`
  reindexes one to the other, which is what lets `Finset.sum_eq_single_of_mem` see a
  single surviving block.
- `subst hlam₀` (not `hlam₀ ▸ N`) after `exists_partitionShape_eq`: `d` is a variable, so
  the diagram becomes `partitionShape lam₀` everywhere and no `HEq` is ever created. The
  two residual cardinality-proof mismatches close by `rfl` — `Prop` proof irrelevance.
  `hρ`, the identification of a block with a `heckeProduct` component, is `fun _ _ => rfl`.

Verification: `lean -DautoImplicit=false -s 65536` RC=0, zero diagnostics.
`#print axioms` on all three: `[propext, Classical.choice, Quot.sound]` — no `sorryAx`.
Two mutants each required to fail and each does: single-entry matrix at `(i,j)` instead of
`(j,i)` → 3 unsolved goals; `rowLen 3 = 0` for `rowLen 2 = 0` in the ⊆ statement → 2
application type mismatches (the weight theorem cannot apply, and the iff breaks).
Not content-swept — ~1.1 GB free against the shadow's ~2.3 GB.

**This bean still does NOT close.** `WenzlTowerStep` and `HeckeGramFactorial`'s open
`T_w`-basis determinant are untouched by any of this (rule 13a).


## The tower comparison is now an IFF — forward direction closed, no conditional expectation (2026-09-26, PR #7463)

#7461 (merged `19387e870751`) gave reflection from `wtrace_incl` alone. The forward
direction is the hard half and is now done, so `heckeIncl` detects the radical **exactly**:

    incl_mem_rad_iff : (∀ x, wtrace (m+1) (heckeIncl a * x) = 0)
                         ↔ ∀ b, wtrace m (a * b) = 0

i.e. `H_m / rad ↪ H_{m+1} / rad` is injective AND well defined — the TL quotients are a
**tower**, not a sequence of algebras with maps between them.

`SchurWeyl/WtraceRadicalTowerForward.lean`:

    rowLen_two_eq_zero_eraseCorner   erasing a corner cannot create a third row
    eq_zero_of_blockPreserving_of_compress_eq_zero
                                     block-diagonal + every diagonal block zero ⇒ zero
    twoRow_blocks_vanish_incl        forward, at the block level
    incl_mem_rad_iff                 the identification

### Why it works where the abstract version needs an open class

`QBeta/TLTowerRadicalDescent`'s docstring states the obstruction correctly — *"membership
in `rad τn1` quantifies over all of `Hn1`, not over `ι '' Hn`"* — and answers it with
`HeckeConditionalExpectation`, which has no instance. That is right about an **arbitrary**
trace. It is not right about `wtrace`, because **wtrace has a branching rule**: route the
forward direction through the radical IDENTIFICATION from #7461 and it reduces to a fact
about diagrams (erasing a corner keeps ≤2 rows). The reduction is the work; the diagram
fact is three lines.

**This does NOT remove that file's conditionality** and the new file says so. Its class is
a genuine hypothesis about an arbitrary tower and stays open. What is shown is that the
CANONICAL carrier does not need one.

Everything consumed was already on `main`, none of it open:
`seminormalRep_heckeIncl_mem_blockSubalgebra` (the image is block-preserving — the ONE
place the image hypothesis is used, and why this holds for `heckeIncl a` and not an
arbitrary element), `compress_seminormalRep_heckeIncl`, `exists_insertMax_of_cellOf_top`,
`isCornerCell_cellOf_card`, `mem_eraseCorner`, `card_eraseCorner`.

### One trap worth keeping

`rowLen_two_eq_zero_eraseCorner` is the **universal** statement over corners. It is NOT
`YoungDiagramThreeRowCorner.youngPred`, which is existential, runs the other way (it
*finds* a corner preserving ≥3 rows) and carries a load-bearing `3 ≤ n` guard that does
not apply here. Easy to reach for the wrong one by name.

Verification: `lean -DautoImplicit=false -s 65536` RC=0, zero diagnostics; `#print axioms`
on all four `[propext, Classical.choice, Quot.sound]`, no `sorryAx`; three mutants each
required to fail and each does — `rowLen 3` for `rowLen 2` in the erase lemma, the
off-block branch replaced by `rfl` (confirming block-diagonality does real work), and
`h.symm → h` in the `S` factorisation. Not content-swept (~1.1 GB free vs ~2.3 GB).

**Still NOT closed.** `WenzlTowerStep` and `HeckeGramFactorial`'s open `T_w`-basis
determinant are untouched by any of the radical arc (rule 13a).
