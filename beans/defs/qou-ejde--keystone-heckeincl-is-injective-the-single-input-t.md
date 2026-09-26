---
# qou-ejde
title: 'KEYSTONE: heckeIncl is injective -- the single input to the colimit bridge (route mapped, all pieces sorry-free on main)'
status: completed
type: task
priority: normal
created_at: 2026-09-12T20:55:31Z
updated_at: 2026-09-26T12:25:09Z
---

Parent: qou-0fmb (plan), epic qou-08a2. Opened 2026-09-12 after the plan re-scope
(#7246) showed the epic funnels to ONE object.

## Why this is the keystone
Mathlib's Algebra/Colimit/Ring.lean has DirectLimit.of_injective: the canonical
map into a direct limit is injective when the TRANSITION maps are. So with
heckeIncl injective:
  * colim_n Hecke K q q^-1 n exists with injective canonical maps;
  * the TRACE descends for free -- MarkovTraceInstance.wtrace_incl
    (tr_{n+1}(incl x) = tr_n x) IS the colimit-compatibility condition;
  * the FILTRATION is strict, because dim Hecke n = (n+1)! is proved
    (finrank_hecke_eq_factorial) and the levels then embed properly.
That single lemma therefore unlocks S2's bridge (qou-g8i1), S4 (qou-ss88) and
strict growth (qou-p8yg) together.

## THE ROUTE -- every piece is already on main and CODE-sorry 0. UNVERIFIED as a
## composition: this is a mapped route, NOT a result. Do not cite it as proved.

Step 1. seminormalRep is FAITHFUL.
  QOU/SchurWeyl/HeckeProductSurjective.lean:117
    heckeProduct_surjective : Function.Surjective (heckeProduct q hq0 hq2 n)
  QOU/SchurWeyl/HeckeWedderburnGeneral.lean:77
    finrank_hecke_eq_factorial  : finrank K (Hecke K q q^-1 n) = (n+1)!
  QOU/SchurWeyl/HeckeWedderburnGeneral.lean:65
    finrank_blocks_eq_factorial : finrank K (block product)     = (n+1)!
  A SURJECTIVE linear map between spaces of EQUAL FINITE dimension is bijective,
  so heckeProduct is injective. Mathlib: LinearMap.injective_iff_surjective, or
  the finrank rank-nullity route. This is the step that is genuinely missing --
  everything else is citation.

Step 2. blocks restrict along the inclusion.
  QOU/SchurWeyl/SeminormalBlockEquality.lean:165
    compress_seminormalRep_heckeIncl (hq0) (hq2) (m) (hN : mu.cells.card = m+2)
      (c) (hc : IsCornerCell mu c) (hNs : (eraseCorner mu c hc).cells.card = m+1)
      (y : Hecke R q q^-1 m) :
      compress c hc (seminormalRep q hq0 hq2 (m+1) hN (heckeIncl R q q^-1 m y))
        = seminormalRep q hq0 hq2 m hNs y

Step 3. compose.
  heckeIncl x = 0  =>  seminormalRep_{m+1} (heckeIncl x) = 0 for every mu
                   =>  (step 2) seminormalRep_m x = 0 for every eraseCorner mu
                   =>  heckeProduct_m x = 0
                   =>  (step 1) x = 0.

## THE GAP IN THE ROUTE -- state it, do not gloss it
Step 3 quantifies over partitions of m+1 obtained as eraseCorner of a partition
of m+2. That IS all of them (add a corner cell to any partition of m+1), but the
surjectivity of `eraseCorner` onto partitions of m+1 must be STATED and proved,
not assumed. SchurWeyl/SytInsertMaxTransport.lean carries insertMax machinery
that looks relevant; check it before building one.

## Scope it inherits, to state and not gloss
finrank_hecke_eq_factorial needs [Field K] [CharZero K], q != 0 and
NotRootOfUnity q. compress_seminormalRep_heckeIncl is stated over R (real) with
qi = q^-1. So the resulting injectivity is at GENERIC q over a characteristic-zero
field, NOT over a bare CommRing, and every downstream consequence (the colimit,
the bridge, strict growth) inherits that.

## Measured absent -- do not assume otherwise
heckeIncl injectivity exists NOWHERE in the corpus today (the only "inject" hits
alongside heckeIncl are docstrings in MathlibExt/HeckeTowerWitness). There is no
DirectLimit of Hecke. Both re-measured 2026-09-12 on main b2843e4f2.

## Discipline
No fit. This bean stays open until the composition is verified sorry-free by
lean-direct; the route being mapped is not the theorem being proved. Five times
this session a "build" turned out to be a wire -- and once a narrowing that looked
safe was refuted by an interior case nobody checked (qou-p8yg). Compose it and
RUN it before believing it.


--------
**2026-09-12: STEP 1 IS PROVED. The route's one genuinely-missing step is closed.**

  QOU/SchurWeyl/HeckeProductInjective.lean
    heckeProduct_injective  : Function.Injective (heckeProduct q hq0 hq2 n)
    eq_of_seminormalRep_eq  : agreeing in every block implies equal

Proof is three lines: finiteDimensional_hecke, then
finrank_hecke_eq_factorial = finrank_blocks_eq_factorial = (n+1)!, then
Mathlib's LinearMap.injective_iff_surjective_of_finrank_eq_finrank applied to
heckeProduct_surjective. So the seminormal family is FAITHFUL.

**Not circular, and worth stating because it looks like it might be.**
finrank_hecke_eq_factorial obtains its LOWER bound from that same surjection and
its UPPER bound from HeckeCoset.finrank_le_factorial. The dimension equality is
therefore not derived from injectivity, so using it to get injectivity is sound.

Verified in-session: lean -DautoImplicit=false -s 65536, exit 0 (captured
directly, not through a pipe), 0 errors, 0 warnings, first attempt. #print axioms
on both declarations: [propext, Classical.choice, Quot.sound]. No sorryAx.

Scope, inherited and to be stated downstream: [Field K] [CharZero K], q != 0,
NotRootOfUnity q -- generic q over a characteristic-zero field, because
finrank_hecke_eq_factorial needs semisimplicity.

## WHAT REMAINS on this bean -- steps 2 and 3, unchanged
Step 2 (compress_seminormalRep_heckeIncl) is cited, not composed. Step 3 still
needs the eraseCorner-surjectivity gap recorded above: the quantification over
partitions of m+1 arising as eraseCorner of one of m+2 is ALL of them, but that
must be proved (check SytInsertMaxTransport before building one). Then
heckeIncl_injective, and only then Ring.DirectLimit.of_injective.

Bean stays OPEN. One of three steps is done; the composition is not.

--------

**2026-09-13 (measured from `qou-301d` / PR #7258): `heckeIncl` injectivity is the keystone for STRICT GROWTH, not for the colimit bridge. The bridge is not gated on it.**

`qou-ejde` says injectivity is *"the single input to the colimit bridge"* and lists
three things it buys. Measured against the **pinned** Mathlib (v4.24.0, the
restored `lake-cache/qou-v4-24-0`), only the third needs it:

```
$ lean -DautoImplicit=false -s 65536   # import Mathlib.Algebra.Colimit.DirectLimit
@DirectLimit : {ι : Type u_1} → [Preorder ι] → (F : ι → Type u_2) → {T : …} →
  (f : (i j : ι) → (h : i ≤ j) → T h) → [FunLike …] →
  [DirectedSystem F …] → [IsDirected ι …] → Type (max u_2 u_1)

@DirectLimit.Ring.of : … [NonAssocSemiring (G i)] → [RingHomClass …] →
  [Nonempty ι] → (i : ι) → G i →+* DirectLimit G f
```

**Neither carries an injectivity hypothesis.** The direct limit exists, and the
canonical ring homs `G i →+* DirectLimit G f` exist, for an arbitrary directed
system. So:

1. *"colim exists with injective canonical maps"* — **existence is free**;
   injectivity of the canonical maps is the extra part.
2. *"the trace descends for free — `wtrace_incl` IS the colimit-compatibility
   condition"* — **correct, and independent of injectivity**: descent is the
   universal property, which needs compatibility only.
3. *"the FILTRATION is strict"* — **this is the one that needs it**, and it is
   `qou-p8yg`'s question.

**Consequence for the plan.** `OcneanuTrace.MarkovTrace` requires
`H_mono : Monotone H` and **not** strictness (checked field by field:
`H`, `H_mono`, `g`, `g_mem`, `ginv`, `ginv_mem`, `ginv_mul`, `mul_ginv`, `tr`,
`tr_mul_comm`, `tr_one`, `z`, `zinv`, `markov`, `markov_inv` — no field mentions
injectivity or strict inclusion). Taking `H n := (DirectLimit.Ring.of _ _ n).range`
gives a monotone filtration unconditionally, and `MarkovTraceInstance.wtrace_incl`
descends the trace. **So the bridge
`HeckeCoset.MarkovTraceFamily → OcneanuTrace.MarkovTrace` can be built today,
without `qou-ejde`** — and it is what would let `DisjointBlockTraceLaw` /
`TowerSpanReduction` / `HeckeSandwichReduces` consume the genuine Ocneanu trace
rather than `HeckeTowerWitness`'s collapse functional.

**Two caveats on this measurement, stated because they bound it.**

* **It is a signature check, not a build.** I verified that no injectivity
  hypothesis appears in `@DirectLimit` / `@DirectLimit.Ring.of`; I did **not**
  construct the bridge. An obstruction could still surface in the `MarkovTrace`
  fields themselves (most plausibly in `ginv`, which needs `σ⁻¹` in the colimit —
  available from the quadratic relation, but unchecked).
* **`DirectLimit.of_injective` does not exist under that name in the pinned
  Mathlib.** `qou-ejde` cites *"Mathlib's Algebra/Colimit/Ring.lean has
  DirectLimit.of_injective"*. In v4.24.0 the namespace is unified
  (`DirectLimit.Ring.of`, `DirectLimit.Ring.lift`, …), `Mathlib.Algebra.Colimit.Ring`
  is not even in the restored cache (its olean is missing — the documented
  cache-gap class), and the injectivity lemmas that DO exist are
  `DirectLimit.lift_injective` and `DirectLimit.mk_injective`. Whoever works
  `qou-ejde` should re-target the citation before building on it.

Not taken — `qou-ejde` / `qou-p8yg` are a live arc. Handing the measurement over.

--------

**2026-09-13 — INTENT (from `qou-301d`, branch `claude/markovtrace-colimit-bridge-2026-09-13`): taking the colimit bridge, with the route named.**

No live branch on this arc and both beans are `todo`; the last commits landed
straight to `main` 11 h ago. Taking it rather than leaving it, per the
stalled-claim rule. Say so and I will hand it straight back.

**Why now.** Since `qou-301d` and `qou-gr3t` merged
(`HeckeSandwichReduces.disjointBlock_of_braided`,
`InteriorMarkovOfBraidedTower.tr_bondWord_of_braided`), this bridge is the
**single blocker for both arcs**: the bond product and the disjoint-block law
are theorems of every `BraidedTower`, and the only `OcneanuTrace.MarkovTrace`
in the tree — `heckeTowerMarkovTrace` — factors through a rank-2 quotient and
is not faithful. The production Ocneanu trace exists and is unique, but as a
`HeckeCoset.MarkovTraceFamily`.

**Route.** Build `OcneanuTrace.MarkovTrace` on the colimit of the Hecke tower:

1. **Directed system.** `f i j (h : i ≤ j) : Hecke K q qi i →ₐ[K] Hecke K q qi j`
   by `Nat.leRec` over `SchurWeyl.heckeIncl`, with `DirectedSystem` from
   `Nat.leRec_self` / `Nat.leRec_succ`.
2. **Carrier.** `A := DirectLimit (Hecke K q qi) f`. Per the measurement already
   in these beans, `@DirectLimit` and `@DirectLimit.Ring.of` carry **no
   injectivity hypothesis**, so this step does not wait on `qou-ejde`.
3. **Filtration.** `H n := (DirectLimit.Ring.of … n).range`; `H_mono` from
   `DirectLimit.Ring.of_f`. Only `Monotone` is required — **not** strictness,
   which is `qou-p8yg`.
4. **Trace.** descends by the universal property; `MarkovTraceFamily.tr_incl`
   IS the compatibility condition (`DirectLimit.Module.lift`).
5. **Generators.** `g n := of (n+1) (σ …)`, `ginv n := of (n+1) (σInv …)`;
   `ginv_mul` / `mul_ginv` from `SchurWeyl.σUnit` under `q * qi = 1`.
6. **Axioms.** `tr_mul_comm` ← `tr_cyclic`, `tr_one` ← `tr_one`,
   `markov` ← `tr_markov`, at `z = q³/(q²+1)`.

**What I expect to be hard, stated in advance so a failure is legible.** Step 5
is the one I flagged as unchecked when I handed over the `DirectLimit`
measurement — `ginv` needs `σ⁻¹` to survive into the colimit, and `σUnit`
requires `q * qi = 1`, which `ocneanuMarkovTrace` supplies only at
`qi = q⁻¹` over `ℝ`. Step 4 needs a *linear* lift, not the ring lift. If either
blocks, I will say which and leave the gap rather than axiomatise it.

**Scope I am NOT claiming.** This bridges the abstractions; it does not make
`heckeTowerMarkovTrace` faithful, prove strict growth (`qou-p8yg`), or derive
the bond product for the production atom word. Nothing here closes either bean
on its own.


--------

**2026-09-26 — STEP 3 IS COMPOSED. `heckeIncl_injective` is proved sorry-free.
Branch `claude/ejde-heckeincl-injective-2026-09-26`. Bean stays IN-PROGRESS: it is
on a branch, not in the product.**

All three steps of the route now exist:

    QOU/Mathlib/YoungDiagramEraseCornerSurjective.lean   (the stated gap)
      isAddableCell_rowLen_zero  -- (0, rowLen 0) is addable to ANY diagram
      exists_eraseCorner_eq      -- hence every diagram is some mu \ c
    QOU/SchurWeyl/HeckeInclInjective.lean                 (step 3)
      seminormalRep_eq_of_heckeIncl_eq
      heckeIncl_injective

**The gap this bean stated was smaller than it looked, and the corpus already held
most of it.** The bean says the eraseCorner-surjectivity "must be STATED and
proved, not assumed" and points at `SytInsertMaxTransport`. The pieces that close
it are in `YoungDiagramAddCell` and `YoungDiagramAddable` instead:
`eraseCorner_addCell` supplies the round-trip outright, and `addable_iff`
characterises addability so that at row 0 the side condition is `0 = 0`. So the
new mathematics is two lines, and the empty diagram needs no case split.

Also worth recording for whoever reads the bean next: `SeminormalBlockEquality`'s
own docstring points at `QOU.Mathlib.YoungDiagramCornerReindex`, which carries
`cornerAddEquiv`, a full BIJECTION of pairs (diagram of n+1, removable corner) <->
(diagram of n, addable cell). That is strictly sharper than the surjectivity. I
used the bare surjectivity deliberately: a `forall nu` goal is discharged by
`subst`, which wants an equation with the variable on one side, and the bijection's
Sigma form is the one the corpus notes produces `HEq`.

**What made the composition two lines.** Step 2 concludes at the diagram
`eraseCorner mu c hc` while the goal wants `nu`, and `seminormalRep`'s OUTPUT TYPE
depends on the diagram (a matrix indexed by its standard tableaux) -- so relating
them is a dependent rewrite and transporting lands in HEq. Stating the bridge with
`nu` as a VARIABLE avoids it entirely: `exists_eraseCorner_eq` returns an equation
whose right side is that variable, `subst` rewrites it and carries `hnu` along, and
step 2 then applies on the nose with `hnu` itself as its `hNs`.

**Verification, stated rather than implied.** `lean -DautoImplicit=false -s 65536`,
exit 0 captured directly (not through a pipe), zero diagnostics, first attempt on
the composition. `#print axioms` on all four declarations: [propext,
Classical.choice, Quot.sound] -- no sorryAx. No `sorry`, no `native_decide`, no new
axiom. Mutant M1 (drop the hypothesis `h` from the rewrite) fails with `unsolved
goals`, so the proof consumes its hypothesis. `heckeIncl_injective` re-grepped by
IDENTIFIER corpus-wide: no prior declaration -- the bean's 2026-09-12 "measured
absent" still holds.

NOT run: the content sweep (needs a ~2.3 GB shadow; 1.2 GB free). These are library
modules with no .qa.json sidecar, so lean-direct plus the axiom audit is the whole
gate available in this container.

**What this does NOT close, and the bean's own later note is why.** This is NOT the
colimit bridge. The 2026-09-13 measurement in this bean records that @DirectLimit
and @DirectLimit.Ring.of carry NO injectivity hypothesis, so the colimit and its
canonical maps exist without it. What injectivity unlocks is STRICT growth --
`qou-p8yg`. It says nothing about `ofLim` being injective for
heckeColimitMarkovTrace and does not make trLim faithful, so the faithfulness
question that #7442 names as the surviving keystone is NOT answered by this.

Scope inherited: R, q != 0, NotRootOfUnity q -- generic q over a characteristic-zero
field, because finrank_hecke_eq_factorial needs semisimplicity. At a root of unity
the proof fails rather than weakens. Every downstream consequence inherits it.


--------

**2026-09-26 — MERGED to main as PR #7454 (rebase-merge, commits e82d718b9e / 1c79876082 /
8d7a36ecb8). `heckeIncl_injective` is in the product, sorry-free. COMPLETING this bean.**

Re-verified on main after the merge: both files `lean -DautoImplicit=false -s 65536` exit 0.

**One claim of this bean is REFUTED by the follow-on work, and it is this bean's own
"what it unlocks" list.** The Why-this-is-the-keystone section says injectivity gives, third,
"the FILTRATION is strict, because dim Hecke n = (n+1)! is proved and the levels then embed
properly". Measured in PR #7456: non-surjectivity of `heckeIncl` needs NO injectivity at all --
`finrank(range) <= finrank H_m = (m+1)! < (m+2)! = finrank H_{m+1}`, first step
`LinearMap.finrank_range_le`, which has no injectivity hypothesis. The independence is enforced
structurally there: `HeckeTowerStrict` does not import `HeckeInclInjective` and compiles RC=0.

So of the three things this bean said injectivity unlocks, the 2026-09-13 note already withdrew
the first two (the colimit and the trace descent need no injectivity) and #7456 withdraws the
third. What injectivity actually buys is the SHARP value `finrank(range) = (m+1)!`
(`finrank_range_heckeIncl`), which is a real strengthening but not the strictness.

That does not make the theorem less worth having -- it is the faithfulness of the tower at the
level of the inclusion, and it is what pins the image dimension exactly. It does mean this bean's
framing of WHY was wrong in all three of its stated consequences, which is worth recording where
the next reader will see it.

Completing rather than leaving open: the subject is a proved sorry-free theorem in the product,
not an open conjecture, so rule 13a does not hold it. The faithfulness question that #7442 names
as the surviving keystone -- whether `ofLim n` is injective for `heckeColimitMarkovTrace`, and
whether `trLim` is faithful -- is NOT this bean and remains untouched.


--------

**2026-09-26, TWO HOURS AFTER COMPLETING THIS BEAN: `ofLim` faithfulness is PROVED
(PR #7456, `QOU/SchurWeyl/HeckeColimitFaithful.lean`). And completing this bean when I
did was premature IN SCOPE -- my own note above got the bean's boundary wrong.**

When I completed this I wrote: "The faithfulness question that #7442 names as the
surviving keystone -- whether `ofLim n` is injective for `heckeColimitMarkovTrace` --
is NOT this bean and remains untouched."

**The corpus disagrees, and I should have checked it.** `HeckeColimit.lean` says three
times, and `HeckeColimitMarkovTrace.lean` repeats, that `H n` is "the image, not an
isomorphic copy ... those coincide exactly when `ofLim n` is injective, **which is the
open question of bean `qou-ejde`**". So this bean was the carrier for BOTH the one-step
inclusion and `ofLim` faithfulness. The theorem it is titled for was genuinely done, so
the completion was not dishonest -- but the scope claim in that note was wrong, and it
is the same class of error as the #7442 correction earlier today: a claim about what a
corpus object covers, asserted without grepping the corpus for it.

**Now proved anyway**, so the bean is complete on both readings:

    heckeInclLE_injective   every transition, by Nat.le_induction over heckeInclLE_succ
    ofLim_injective         DirectLimit.mk_injective applied to it
    finrank_H               finrank (H n) = (n+1)!
    H_lt_succ               H n < H (n+1)

**The dead citation in this bean's route is now confirmed dead and replaced.** This bean
cites "Mathlib's Algebra/Colimit/Ring.lean has DirectLimit.of_injective". Grepping
declaration names out of the pinned v4.24.0 oleans: no `of_injective` anywhere; only
`DirectLimit.lift_injective` and `DirectLimit.mk_injective`. **`mk_injective` is the
lemma**, and its hypothesis is exactly "every transition map is injective" -- which is
what made this three lines once `heckeIncl_injective` existed. A later note on this bean
already flagged that the citation needed re-targeting; this is the re-target.

**So this bean's "what it unlocks" list ends 1 for 3, not 0 for 3.** The 2026-09-13 note
withdrew the colimit-existence and trace-descent claims; #7456 withdrew strict growth of
the CONCRETE tower. But strict growth of the COLIMIT filtration (`H_lt_succ`) genuinely
does need faithfulness, which genuinely does need this bean's theorem. The third claim
was right about the colimit and wrong about the concrete tower.

Still NOT closed by any of this: `trLim` faithfulness (whether the TRACE separates
points) and `twH` in MathlibExt/HeckeTowerWitness.
