---
# qou-0fmb
title: 'PLAN: wire IwahoriHecke algebra to the BraidedTower theorem (#7153) -- discharge qou-301d instance (growing filtration + h!=0)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T11:54:27Z
updated_at: 2026-11-18T08:22:48Z
parent: qou-59vq
---

Parent epic: qou-08a2. Records the 2026-09-12 finding that the growing+h!=0 BraidedTower instance (qou-301d's remaining gap) is a WIRING job, not a from-scratch build -- the two halves already exist and are unconnected.

## The two halves (both on main / in flight)
- ABSTRACT theorem (PR #7153, open, bean qou-301d): class BraidedTower (quad/far/braid) => sandwichReduces_all => towerSpan_of_braided => disjointBlock_of_braided. The q!=1 rewriting SandwichReduces is PROVED, generic in the tower. Its own caveat: "no BraidedTower instance with a growing filtration + h!=0 is constructed."
- CONCRETE algebra (QOU/IwahoriHecke/, 20 files, 1 axiom): Defn.lean has IwahoriHecke W R q with T_quadratic + T_braid PROVED over Mathlib Coxeter (GroupTheory/Coxeter/{Basic,Length,Inversion,Matrix}); qou-uoal (COMPLETED) gave the coset basis finrank(Hecke) <= (n+1)! sorry-free (HeckeCoset.lean = the Hn+1 = Hn (+) Hn gn Hn structure #7153 said "Mathlib does not supply"); BraidTower.lean has braidTower : BraidGroupN m ->* BraidGroupN(m+1) + braidTrace_peel (the Markov recursion); MarkovTrace.lean has GradedMarkovTraceExistence + markovTrace_cyclic.
- The gap (measured): grep of IwahoriHecke/ for OcneanuTrace/MarkovTrace R A/BraidedTower/TowerSpan is EMPTY. The concrete algebra is not wired to the abstract framework.

## Multi-session steps (the "all mathlib infra" to bean)
S1 (child): a single R-algebra A carrying g:N->A and a growing H:N->Subalgebra (the abstract MarkovTrace tower shape), built from the IwahoriHecke type-A tower / BraidTower.braidTower colimit. h = q - q^-1 != 0. This is the main construction gap.
S2 (links qou-g8i1): package the Ocneanu/Markov trace as the abstract MarkovTrace.tr : A ->L R with z, zinv and the markov / markov_inv axioms. qou-g8i1 (the z_d bond rule tr(x sigma_i)=z_d tr x) IS this axiom; IwahoriHecke/MarkovTrace + BraidTower.braidTrace_peel supply the peel. Do not duplicate g8i1.
S3: prove far (distant generators commute) on the N-indexed generators, from the Coxeter/braid structure.
S4 (child): instantiate #7153 BraidedTower (T_quadratic->quad h!=0, T_braid->braid, S3->far) and fire disjointBlock_of_braided => discharge qou-301d's instance UNCONDITIONALLY.

## Discipline
No fit (the whole point is derivation). Per rule 13a this arc and its children stay open until the math closes; the instance is the honest remaining gap. #7203 (rank-2 H2 functional, MERGED e0c10a77) is the h!=0 base object but single-generator (cannot grow); the symmetric-group tower #7131 is growing but h=0 -- S1 must supply the missing growing+h!=0 quadrant.

Links: qou-08a2 (epic), qou-301d/#7153 (theorem), qou-uoal (coset basis DONE), qou-g8i1 (Markov bond rule), qou-mbm9 (IwahoriHecke 36-axiom build), qou-nkd8 (class strengthening), qou-1ty8/#7203 (rank-2 base, merged).


--------
**2026-09-12, MAJOR RE-SCOPE: S2 is NOT open. Jones' existence theorem is PROVED in the corpus, with uniqueness — in a DIFFERENT Markov-trace abstraction that nothing bridges.**

This plan scoped S2 (qou-g8i1) as "package the Ocneanu/Markov trace ... Jones'
existence theorem is open here". Measured on main (cb2d1f765), that is wrong.

  QOU/SchurWeyl/MarkovTraceInstance.lean   (200 lines, CODE-sorry 0, axiom-decls 0)
    wtrace          x |-> sum_{|nu|=n+1} W_nu * tr(rho_nu x), bundled ->L[R]
    wtrace_cyclic   T1  trace property
    wtrace_one      T2  normalisation
    wtrace_markov   T3  Markov stabilisation
    wtrace_incl     tr_{n+1}(incl x) = tr_n x   -- TOWER compatibility
    ocneanuMarkovTrace : HeckeCoset.MarkovTraceFamily R q q^-1 (q^3/(q^2+1))
    eq_wtrace_of_markov  -- every such trace IS this one

  QOU/SchurWeyl/MarkovTraceUnique.lean     (139 lines, CODE-sorry 0)
    structure MarkovTraceFamily (K) (q qi z)
      tr : (n : N) -> Hecke K q qi n ->L[K] K
      tr_one, tr_cyclic, tr_incl, tr_markov
    markovTrace_unique : any two agree

At CONVENTION D, z = q^3/(q^2+1) -- the canonical one -- with genericity
(q != 0, q^2 != 1, q^2+1 != 0, q^2 not a root of unity). So the existence AND
uniqueness of the Ocneanu trace on the Hecke tower are both proved.

**THE REAL GAP: there are TWO Markov-trace abstractions and NOTHING bridges them.**

  HeckeCoset.MarkovTraceFamily   LEVEL-INDEXED: one tr per n, tied by tr_incl.
                                 SchurWeyl. Has the genuine trace.
  OcneanuTrace.MarkovTrace       ONE algebra A + filtration H : N -> Subalgebra
                                 + ONE tr. MathlibExt. What BraidedTower /
                                 TowerSpanReduction / DisjointBlockTraceLaw consume.

Measured: grep for OcneanuTrace across QOU/SchurWeyl/ returns NOTHING. Zero
bridge. This is the SAME "two halves exist and are unconnected" pattern this plan
was opened to record, one level up -- and it is the same Fin-n-vs-N shape
difference that S1 resolved for the ALGEBRA, now recurring for the TRACE.

**Everything now funnels to ONE object: the colimit colim_n Hecke K q qi n.**
Building an OcneanuTrace.MarkovTrace out of the MarkovTraceFamily needs a single
algebra containing every level -- i.e. the colimit -- and then:

  * the TRACE descends for FREE. tr_incl IS exactly the colimit-compatibility
    condition; that is what it is for. No new trace mathematics is needed.
  * the FILTRATION needs heckeIncl INJECTIVE, which is ALSO what strict growth
    (qou-p8yg) needs.

So the epic's remaining work is not four steps. It is one construction (the
colimit / or the identification twH n ~= Hecke (n-1)) plus one lemma (heckeIncl
injective), and both S2 and qou-p8yg fall out of it.

Measured NOT-present, so do not assume: heckeIncl injectivity does not exist
anywhere (the only "inject" hits alongside heckeIncl are my own docstrings in
HeckeTowerWitness), and there is no DirectLimit of Hecke in the corpus.

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

**2026-09-14 — DONE, all six steps, sorry-free. And read the scope line: this is the SCHUR-WEYL tower, not `QOU/IwahoriHecke/`.**

Branch `claude/markovtrace-colimit-bridge-2026-09-13`, PR #7274. Every step of
the route in the INTENT block above landed as written, and both hazards I
flagged in advance resolved the way I guessed:

| step | declaration | file |
|---|---|---|
| 1 directed system | `heckeInclLE`, `directedSystem`, `heckeInclLE_σ` | `SchurWeyl/HeckeDirectedSystem.lean` |
| 2 carrier + filtration | `HeckeLim`, `instAlgebraHeckeLim`, `ofLimₐ`, `H`, `H_mono` | `SchurWeyl/HeckeColimit.lean` |
| 3 generators | `gLim`, `ginvLim`, `gLim_eq`, `gLim_quadratic/braid/far` | same |
| 4 trace | `wtrace_inclLE`, `trLim` | `SchurWeyl/HeckeColimitMarkovTrace.lean` |
| 5-6 axioms | `trLim_cyclic/one/markov/markov_inv`, `heckeColimitMarkovTrace` | same |
| payoff | `braidedTower_heckeColimit`, `towerSpan_heckeColimit`, `disjointBlock_heckeColimit` | same |

`lean`-direct `-DautoImplicit=false -s 65536` exit 0 on all three files, zero
warnings, zero `sorry`; `#print axioms` is `[propext, Classical.choice,
Quot.sound]` throughout (`heckeInclLE_σ` is `[propext, Quot.sound]`).

**🛑 SCOPE — what this bean's TITLE asks for is still NOT done.** The title says
*"wire IwahoriHecke algebra to the BraidedTower theorem"*, and the body's "two
halves" section means `QOU/IwahoriHecke/` — the 20-file Coxeter-group
implementation over `Mathlib.GroupTheory.Coxeter`. **I wired
`QOU/SchurWeyl/Hecke` instead**, which is a *different* construction (a
`RingQuot` of `FreeAlgebra K (Fin n)`). The grep finding recorded above — that
`IwahoriHecke/` mentions no `OcneanuTrace` / `BraidedTower` / `TowerSpan` —
**is still true and this branch does not change it.**

The reason for the substitution is not evasion and should be checked rather than
taken: the production Ocneanu trace, the one proved to exist and be unique
(`MarkovTraceInstance.wtrace` / `ocneanuMarkovTrace`,
`HeckeCoset.markovTrace_unique`), is defined on the **SchurWeyl** algebras, not
on `IwahoriHecke/`. So the SchurWeyl tower is where a `MarkovTrace` could be
built out of material that already exists; the `IwahoriHecke/` route would need
its own trace first. Whether the two algebras are isomorphic is not established
anywhere I could find, and I did not assume it.

**What IS now closed, and it is the thing both arcs were blocked on.**
`TowerSpan` and `DisjointBlockMultiplicative` were proved abstractly in #7153
but inhabited only on `heckeTowerMarkovTrace` (a free carrier whose trace
factors through a rank-2 quotient — not faithful) and on the symmetric group
(`h = 0`). They now hold on a tower carrying the **genuine Ocneanu trace at
convention D**, `z = q³/(q²+1)`.

**The two flagged hazards, resolved:**

* Step 4 did need the **linear** lift. `wtrace` is `ℝ`-linear and is *not*
  multiplicative, so `DirectLimit.Ring.lift` does not apply at all;
  `DirectLimit.Module.lift` does, and its compatibility hypothesis wants the
  *iterated* inclusion, hence `wtrace_inclLE` as the `Nat.le_induction` iterate
  of the sibling's one-step `wtrace_incl`.
* Step 5's `q * qi = 1` is discharged by `hq0 : q ≠ 0` at `qi = q⁻¹` and never
  surfaces in the instance. `ginvLim` is *defined* unconditionally (`σInv` is);
  only the two inverse laws carry the hypothesis.

**Two measurements worth keeping, neither of which was in the plan:**

1. **Mathlib supplies no `Algebra R (DirectLimit …)` instance.** Enumerated the
   whole namespace out of the olean: `instModule` and the
   `instRing`/`instCommRing`/`instField` family, nothing algebra-valued, and
   `inferInstance` fails. Built here with `Algebra.ofModule` over the
   *existing* `instModule` — deliberately **not** `RingHom.toAlgebra'`, which
   also typechecks and would mint a second `SMul K (HeckeLim …)`, putting a
   diamond against the colimit's own scalar action.
2. **`DirectLimit.Module.of` and `DirectLimit.Ring.of` are the same function**
   (`rfl`). That is what makes the two `Algebra.ofModule` laws cheap.

**`zinv` is derived, not posited:** `σ⁻¹ = σ - (q - q⁻¹)·1`, so
`tr(a σ⁻¹) = tr(a σ) - (q - q⁻¹) tr a`, giving `zinv = q³/(q²+1) - (q - q⁻¹)`.
`z` is inherited from `wtrace_markov`. No parameter is chosen.

**Still open, assumed nowhere:** injectivity of `ofLim n` (`qou-ejde`) — so
`H n` is the *image* of level `n`, not a copy of it; strict growth
(`qou-p8yg`); faithfulness of `trLim`; the bond product for the production atom
word; and the `IwahoriHecke/` wiring this bean is titled for.

**Staying `todo`** — the titled subject is not done, and per AGENTS.md §13a a
bean whose subject is open is not closed by recording progress on it.


--------

**2026-09-14 — CORRECTION to my own figure above: the "99 of 102 stale" was measured with a criterion this repo records as UNSOUND. The sound number is 102 of 102, and the verification is unaffected.**

**What I asserted.** The DONE entry above, PR #7274's body, and a coordination
comment on that PR all say *"99 of the 102 modules in this PR's import cone are
stale"*.

**How it was measured, and why that was wrong.** I compared each olean's
**mtime** against its own source's last commit
(`git log -1 --format=%ct <src>` vs `os.path.getmtime(<olean>)`).
`.claude/agent-memory/lean-verifier/MEMORY.md` already records that exact
criterion as **UNSOUND**, with the mechanism: a restored tarball gives oleans
the *extraction* time, so an olean built from an old source looks fresh. It
therefore **under**-reports staleness. The sound criterion in the same entry is
the **seed commit** — dirty = source changed since the cache's seed, or olean
missing, or an import dirty.

**Re-measured with the sound criterion.** Seed `bbb4127145` (2026-08-23 17:00Z,
the last `main` commit before the oldest QOU olean in this container):
**102 of 102 dirty**, with **99 root causes** (source changed since seed) and
the remaining 3 dirty because they are new on this branch. So the mtime
criterion was short by exactly 3 — and the 3 it called "fresh" were oleans I
had built myself minutes earlier.

**The verification does not depend on this at all, and is if anything better
than I claimed.** I rebuilt **all 102** from source rather than a computed
subset, which is exactly what the sound criterion demands. The criterion only
chose *which* to rebuild, and I chose all of them. `lean`-direct exit 0 on all
three files against that rebuilt cone, `#print axioms` clean, 0 RED across the
102 — unchanged.

**Also measured, and not previously recorded anywhere: the oldest-olean
heuristic is a LOWER BOUND on the seed, and on a reseeded cache it can be far
too old.** `tar` preserves the archive's mtimes, which are *build* times, and a
reseed from an incremental `lake build` rewrites only what was dirty — so one
tarball holds oleans built across weeks. In this tree the oldest **QOU** olean
is 2026-08-23 and the oldest **mathlib** olean is 2026-09-06, a **14-day
spread** inside a cache whose branch describes it as a single 2026-09-06 seed.
Too-old a seed **over**-reports staleness, which is the safe direction; the
mtime criterion under-reports, which is not. Recorded in the `lean-verifier`
memory's dirty-closure entry, whose own seed baseline was stale
(`19e299946a` / 2026-08-16) and is now re-measured per container.

**Contamination check, since a wrong figure in this corpus has repeatedly
survived in five other places after being fixed in one.** The figure appears
in exactly three artifacts, all mine and all from this session: this bean,
PR #7274's body, and one comment on #7274. All three are corrected. It reached
no audit doc, no content block and no witness.

**Separate finding, NOT acted on: `lean-verifier/MEMORY.md` is 734 lines
against the 200-line cap AGENTS.md states for it** (the cap exists to bound
what an agent must read; the file is 3.7x over). Restructuring it is a change
I have not made — per §ASK THE OWNER it is neither a precision fix nor
corpus-derived, and splitting a memory file another agent owns is exactly the
kind of tidying that rule gates. Flagging it rather than doing it.

## 2026-09-14 — the isomorphism route: the missing leg is LANDED, and the remaining gap is NOT a wiring step

**Status stays `todo`** (§13a — the wiring this bean is titled for is not complete).

**What the corpus already had, found by corpus-grep rather than rebuilt.** Two of the
three legs of the isomorphism route existed:

- `QOU.SchurWeyl.carrierEquiv` — `Hecke K q qi n ≃ₐ QOU.Hecke.IwahoriHecke K Q n`
- `QOU.IwahoriHecke.Balanced` — `σ_i := qi · T_i` on the Coxeter-matrix family

**Both cross the NORMALISATION** (skein `σ² = (q−qi)σ + 1` vs Iwahori `(T−Q)(T+1) = 0`,
at `Q = q²`). **Neither crosses the INDEX PRESENTATION**, and that was the real gap:
`QOU.Hecke.IwahoriHecke` states its braid content as two explicit clauses on `Fin n`,
while `MathlibExt.HeckeAlgebra` states it as one `altProd` clause against a Coxeter
matrix quantified over all pairs. That is `qou-img9`'s defect in a specific instance.

**Landed (PR #7395), sorry-free:**

    coxeterCarrierEquiv : QOU.Hecke.IwahoriHecke K Q n ≃ₐ[K] HeckeAlgebra K Q (Aₙ n)
    skeinBalancedEquiv  : SchurWeyl.Hecke K q q⁻¹ n ≃ₐ[K] Balanced.BalancedHecke (Aₙ n) q

The second lands on `BalancedHecke` **on the nose** (no `pow_two` transport), so the
claim "the algebra with the proved-unique Ocneanu trace is the algebra
`QOU/IwahoriHecke/` is built on" is machine-checked rather than asserted.

The content is finite: `Aₙ` entries are 1/3/2 and `altProd` there is `a` / `a·(b·a)` /
`a·b`, so the quantified clause is exactly the two explicit ones plus a diagonal
triviality — a five-way case split (`altProd_of_explicit`, `braid_of_altProd`,
`comm_of_altProd`). No hypothesis on `Q`; `[CommRing K]` suffices.

Verification: `lean -DautoImplicit=false -s 65536` exit 0, 0 errors, 0 warnings;
0 `sorry`; `#print axioms` `[propext, Classical.choice, Quot.sound]` on all seven
declarations, no `sorryAx`.

**🛑 THE REMAINING GAP IS NOT A WIRING STEP — measured, so the next agent does not go
looking.** Transporting the `OcneanuTrace.MarkovTrace` / `BraidedTower` instance needs
the equivalences to commute with the level inclusions. **There is no inclusion
`HeckeAlgebra n → HeckeAlgebra (n+1)` anywhere on the Coxeter side**:
`grep -rn 'HeckeAlgebra.*→ₐ.*HeckeAlgebra\|heckeIncl' IwahoriHecke/ MathlibExt/` returns
only `SchurWeyl.HeckeInclusion.heckeIncl` and prose about it. So the tower the
transport would land on **has to be constructed first**. That is the next honest step,
and it is real work, not plumbing.

Also not done: `TypeA.IwahoriHeckeOfSn` re-indexing (`Fin (n-1)`, truncated
subtraction), and anything about the `Set.univ`-indexed `Defn.IwahoriHecke`.

**Caveat on the novelty claim.** `corpus_search` (path 0) was unavailable — the
`paper-assistant` MCP server failed to connect (`ENOENT … start-folio-assistant.sh`).
Paths 1–6 are greps and share the blind spot path 0 covers, so "nothing connected
them" rests on lexical search plus reading both files.


--------

**2026-10-12 — the `IwahoriHecke/` TRACE is now wired to `BraidedTower`, over ANY field. The Coxeter-side ALGEBRA tower is still not.** Branch `claude/braided-tower-hecke-wiring-2026-10-12`, commit `1b6dbbe2fb`, new file `QOU/IwahoriHecke/HeckeColimitTensorTrace.lean`.

Survey first, so nothing is duplicated: S1-S4 on the SchurWeyl side were already done (#7274, `heckeColimitMarkovTrace`, `braidedTower_heckeColimit`, `disjointBlock_heckeColimit`) — but only over `ℝ`, and only for `q` not a root of unity, because its trace `wtrace` is a seminormal-character sum needing semisimplicity. This file builds a SECOND trace on the SAME carrier `HeckeLim K q q⁻¹` from `IwahoriHecke.TensorMarkovModel` (the normalised quantum trace on `End(V^{⊗(n+1)})^W`), so the hypotheses drop to `[Field K]`, `q ≠ 0`, `q²+1 ≠ 0` (§7c generic ring; no ordering, no genericity).

| decl | content |
|---|---|
| `toModel hq n` | `Hecke K q q⁻¹ n →ₐ TensorMarkovModel.A q n`, `σᵢ ↦ sᵢ` (Hecke.lift + `sA_heckeFamily`) |
| `levelTrace`, `_one`, `_cyc`, `_markov` | Markov at EVERY level `k < n`, `z = zD q = q³/(q²+1)` |
| `levelTrace_incl` | tower compatibility, by UNIQUENESS (`JonesNormalForm.markov_unique_of_adjoin_eq_top`), not by matrix computation |
| `trT`, `trT_one/_cyclic/_markov/_markov_inv` | colimit trace; `zinv = zD q − (q − q⁻¹)` derived |
| `tensorColimitMarkovTrace` | `OcneanuTrace.MarkovTrace K (HeckeLim K q q⁻¹)` |
| `braidedTower_tensorColimit` | instance, `h = q − q⁻¹` (`quad_scalar_ne_zero`: `≠ 0` iff `q² ≠ 1`) |
| `towerSpan_tensorColimit`, `disjointBlock_tensorColimit` | #7153 fired |

Verification: lean-direct `-DautoImplicit=false -s 65536` exit 0, 0 warnings, against a shadow in which all 24 QOU modules of the import cone were rebuilt from this branch's source (the restored cache lacked 8 of them). `#print axioms` on all 19 decls: `[propext, Classical.choice, Quot.sound]`. 0 sorry.

**Still open, assumed nowhere:** (1) the Coxeter-side tower — there is still no inclusion `HeckeAlgebra K Q (Aₙ n) → HeckeAlgebra K Q (Aₙ (n+1))` commuting with `skeinBalancedEquiv`, so the instance is not transported onto `Defn.IwahoriHecke`/`BalancedHecke`; (2) faithfulness — the tensor model is the two-row (TL) quotient, so this trace kills the radical; (3) the identification `trT = trLim` over `ℝ` at generic `q` (should follow from uniqueness, but `wtrace`'s Markov property at levels `k < n` in `HeckeFamily` form is not available; not stated). Bean stays `todo` (§13a: the titled Coxeter-side wiring is not complete).


--------

**2026-10-12 (later) — the Coxeter-side tower is BUILT and the braided Markov trace is on it.** Commit `9d2b8bfd78`, PR #7771.

- `QOU/MathlibExt/AlgebraTowerColimit.lean` (generic): colimit `Lim G f` of an ℕ-tower of K-algebras, `inclLE`, `DirectedSystem`, `Algebra.ofModule` instance (no SMul diamond), `ofₐ`, `ofₐ_comp`, range filtration `H` / `H_mono`.
- `QOU/IwahoriHecke/CoxeterTower.lean`:
  - `coxIncl K Q n : HeckeAlgebra K Q (Aₙ n) →ₐ HeckeAlgebra K Q (Aₙ (n+1))`, `T_i ↦ T_{castSucc i}` (any CommRing, any Q; `AMat_castSucc`).
  - `skeinBalancedEquiv_σ` (σᵢ ↦ q⁻¹•Tᵢ), `skeinBalancedEquiv_heckeIncl` (**e_{n+1} ∘ heckeIncl = coxIncl ∘ e_n**), `skeinBalancedEquiv_inclLE`.
  - `CoxLim q`, `colimEquiv hq : HeckeLim K q q⁻¹ ≃ₐ[K] CoxLim q` (`colimEquiv_ofLim`: it is e_n on level n).
  - generic `transportMarkovTrace` + `braidedTower_transport`.
  - `coxeterMarkovTrace hq hq1 : MarkovTrace K (CoxLim q)`; `coxeterMarkovTrace_H` (H n = image of the Coxeter level n), `coxeterMarkovTrace_g` (g n = `Balanced.sigma` = q⁻¹·T_n at level n+1), `coxeterMarkovTrace_tr_ofₐ`, `coxeterMarkovTrace_z` (= q³/(q²+1)).
  - `braidedTower_coxeter` (h = q − q⁻¹), `towerSpan_coxeter`, `disjointBlock_coxeter`.

Hypotheses `[Field K]`, `q ≠ 0`, `q²+1 ≠ 0`. lean-direct `-DautoImplicit=false -s 65536` exit 0, 0 warnings, against a shadow with every cone module rebuilt from branch source (27 + the 3 new). `#print axioms` on 28 decls: ⊆ `[propext, Classical.choice, Quot.sound]`; 0 sorry.

**What this does NOT close, so the bean stays `todo` (§13a):** (1) faithfulness — the trace is the tensor-model (two-row TL) trace, not faithful; (2) the level maps into `CoxLim` are not shown injective (`H n` is an image; cf. qou-ejde); (3) the `Set.univ`-indexed `Defn.IwahoriHecke` / `TypeA.IwahoriHeckeOfSn` are not touched — the Coxeter tower here is the `HeckeAlgebra K Q (Aₙ n)` family. If the owner reads the title as satisfied by the `HeckeAlgebra (Aₙ n)` tower, the remaining items are (1)–(2), which are the subjects of other beans.

- Round 73 (`lane-e667`): Formalized `qou-0fmb`, `qou-4lft`, `qou-avt2`, `qou-cf3m`, `qou-g6vb` in `QOU.Foundations.TowerCompatibilityRootOfUnitySeminormalNormalizationRadicalKernelBilinearSymmetry` with 80-dps `mpmath` 2-commit witness stamp (`98224baac4097812a7a075b15a3d78cd7d6d0f26` -> `57db1e21b3add3a8efd73f5cd0f4cff40a2a1827`, `scriptHash=28e0042d776cdc079c85f0254ab21558d7f5b492e88420dbd3fa8ba157431743`) in PR `litlfred/qou#8394` (`status: in-progress`).
