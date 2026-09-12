---
# qou-ejde
title: 'KEYSTONE: heckeIncl is injective -- the single input to the colimit bridge (route mapped, all pieces sorry-free on main)'
status: todo
type: task
priority: normal
created_at: 2026-09-12T20:55:31Z
updated_at: 2026-09-12T21:00:02Z
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
