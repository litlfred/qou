# Hecke infrastructure: what exists, what is missing, and what H3/H4 need

> **STATE OF PLAY — end of 2026-08-09. Read this section first; several sections
> below were written earlier the same day and are superseded, each marked.**
>
> This document was begun before `QOU/Machinery/HeckeH3*.lean` and
> `HeckeH4*.lean` had been read. They contain far more than it first said, and
> the corrections are the most important thing in it.

## Where the levels stand

| level | `HeckeAlgebra` class instance | `IsHeckeOfFullRank` | `QOU.Hecke.MarkovTrace` | `MarkovTraceContext` |
|---|---|---|---|---|
| `n = 2` | `InstanceH2.instHeckeAlgebraH2`, on `AdjoinRoot(X² − hX − 1)` | `2 = 2!` | `MarkovTraceH2.markovTraceH2` — but `cyclic` free (commutative) and `trace_prod_gen` vacuous | `contextH2` |
| `n = 3` | `InstanceOnH3A.instHeckeAlgebraH3A`, on the tree's `H3A` | `6 = 3!` | `MarkovTraceOnH3A.markovTraceH3A` — **both fields carry content** | `contextH3` |
| `n = 4` | `InstanceOnH4A.instHeckeAlgebraH4A`, on the tree's `H4A` | `24 = 4!` | **open** — see below | — |
| `n ≥ 5` | GS basis now **proved** for the *completed* system (qou-auq3, 2026-08-24) | — | — | — |

All axiom-clean (`propext, Classical.choice, Quot.sound`). Before this work the
class `QOU.Hecke.HeckeAlgebra` had **no instance anywhere in the tree**, so every
`[HeckeAlgebra R n q A]` hypothesis in the corpus was unwitnessed.

`n = 4` is the last level worth instantiating by hand — it is where `farCommute`
first has content, and `n ≥ 5` adds no new class field. See
*How far up does the ladder need to go?* below, which stands.

## What this document got wrong earlier today

1. **"H4Carrier … but no multiplication at all"** (§*H4 and above*, superseded).
   `QOU.Machinery.HeckeH4AlgebraLaws` has `mulNF₄`, **`mulNF₄_assoc`** — proved
   via the structured route, `mulσₖ (u·v) = u·(v·σₖ)` lifted along the right
   basis, explicitly "no 24³ brute force" — and wraps the result as `H4A R h`
   with `Ring` and `Algebra`. `HeckeH4Wedderburn` then gives
   `wedderburn₄ : H4A K (q − q⁻¹) ≃ₐ[K] K × K × M₂ × M₃ × M₃`, sorry-free.
   `HeckeH4StabilizationRung` proves the whole presentation on the subscript
   basis, including `far_commute_σ₀σ₂`, whose own docstring already recorded that
   far commutation is "non-vacuous for the FIRST time at n = 4".

2. **"H3 … stuck on one lemma"** (§*H3*, superseded). That is true of
   `QOU/Mathlib/HeckeAlgebra.lean`'s `H3Carrier`, and `H3.mul_assoc` does close
   it. But `QOU.Machinery.HeckeH3AlgebraInstance.H3A` was already a `Ring` on the
   H₃ normal-form basis, with `wedderburn₃` alongside. `InstanceH3.H3Alg` and
   `InstanceH4.H4Alg` are therefore **duplicate carriers** built in ignorance of
   `H3A`/`H4A`; bean qou-ti7p records which parts of those two files are
   genuinely their own and should survive retirement.

3. **The rank was never going to need a closure table.** Bean qou-awp7 planned to
   reach `24 = 4!` through a `3 × 24` closure table over the reduced-word
   operators. Unnecessary: `H3A` and `H4A` are structures wrapping their
   coordinate vector (`v : Fin 6 → R`, `v : Fin 24 → R`) with componentwise
   module structures, so each is linearly equivalent to its coordinate space and
   the dimension is unconditional. `FullRankFromWedderburn` also records that the
   Wedderburn block counts agree — `1+1+2² = 3!` and `1+1+2²+3²+3² = 4!` — which
   is a real check on the basis, a generic count matching an unconditional one.

4. **`trM_cyclic` at `n = 4` is not a `sorry`.** Three docstrings said it was —
   `MarkovTraceH4`'s Proof-status section, `MarkovTraceH4Gram`'s own `trM_cyclic`
   docstring, and (repeating them) `MarkovTraceOnH3A`. `gram_symm` is discharged
   in `MarkovTraceH4Gram` against the 576 entries of the `Gram0..7` chain and
   `#print axioms` is clean. All three corrected.

## The one open Hecke item below `n = 5`

A Markov trace at `n = 4`. The sorry-free cyclicity is on the **ASCII** basis
(`MarkovTraceH4`), while `H4A` — and so `instHeckeAlgebraH4A` — is on the
**subscript** basis, and the two 24-word tables are different data.

The route that needs neither a second Gram closure nor an explicit change of
basis is `QOU.Machinery.BilinearTrace.gram_symm_of_rep_decomp`: if `trM4`
decomposes as a finite weighted sum of representation traces, each multiplicative
on `mulNF₄`, Gram symmetry follows with no per-pair computation, and
`wedderburn₄` supplies exactly those representations. What remains is identifying
the Markov weights — the `y_λ` machinery exists but on `H4Carrier` over `ℝ`,
a third carrier again.

## Gröbner–Shirshov: the route to general `n`, and what it costs

`content/unital-groebner-bases/lean/UGB/GrobnerShirshov/HeckeGS.lean` is the only
route past `n = 4` — a GS basis gives normal forms and the `n!` count for all `n`
at once, and it is the constructive substitute for Matsumoto / Coxeter word
reduction, which Mathlib at rev `f897ebcf` does not have (`find Mathlib -iname
"*Hecke*"` returns nothing). Findings so far:

* The system carried a **sentinel rule with empty leading monomial**. Since
  `[] <:+: m` for every `m`, `isNormalForm` was false for everything with
  non-empty support and `IsGrobnerShirshovBasis` collapsed — it held of *any*
  system, and `hecke_is_gs_basis` was provable in four lines while saying
  nothing. Removed; `gs_basis_of_empty_lm` now proves the collapse in general.
* **And with the sentinel gone the statement is not merely unproved — it is
  FALSE.** Machine-checked at `n = 4`
  (`UGB.GrobnerShirshov.Hecke.NotAGSBasis.hecke_not_gs_basis_four`): Yang–Baxter
  for `(σ₂,σ₃)` (lm `σ₃σ₂σ₃`) overlaps far-commutation for `(σ₃,σ₁)` (lm `σ₃σ₁`)
  on `σ₃σ₂σ₃σ₁`, and the two reductions `σ₂σ₃σ₂σ₁` and `σ₃σ₂σ₁σ₃` are both
  irreducible, so the S-polynomial has a non-zero normal form. The axiom is
  deleted. Bokut & Shiao Thm 3.5 was misapplied: it gives a GS basis for the
  **completed** system, adjoining `sᵢsᵢ₋₁⋯sⱼsᵢ → sᵢ₋₁sᵢsᵢ₋₁⋯sⱼ`, whose first
  instance is exactly this S-polynomial. Nothing `q`-deformed is at fault — the
  same overlap obstructs the Coxeter presentation of `S₄`. (Their general
  *conjecture* for arbitrary Coxeter groups was separately disproved by
  Chen–Liu.) The completion is what qou-auq3 needed.
* **The completion is built and proved** (2026-08-24).
  `HeckeCompletion.lean` adjoins the Bokut–Shiao family and proves
  `heckeCompleted_isGrobnerShirshovBasis` for every `n` and every
  `HeckeParams` — `[propext, Classical.choice, Quot.sound]`, no hypothesis, no
  `sorry`. The last obligation was a single composition, the longest
  Bokut–Shiao word overlapping *itself* in its shared trailing `σᵢ`; it is
  discharged by `deep_selfOverlap_resolves`. Normal-form uniqueness at general
  `n` follows (`heckeCompleted_normalForm_unique`), modulo the two Diamond-Lemma
  axioms `local_confluence` and `reduction_well_founded` that
  `normal_form_unique` carries.
* Two defects remain before the axiom can be *proved*: `leadingMonomial` ignores
  its order argument (`hf.choose`, an arbitrary support element), and
  `SingleStepReduction` never requires `f − g` to lie in the ideal despite its
  docstring — nor is `OverlapComposition.spoly` computed from the rules.
  Bean qou-auq3.
* The S-polynomial argument also needs the ground algebra to have **no
  quasi-zeros** (Pawloski–Leitner, arXiv:math/0409565v2). The folio's own chapter
  carries that hypothesis through every statement of its main theorem; in Lean it
  appears in two docstrings and no hypothesis. Bean qou-k6ks.

---

*Everything below predates the corrections above.*


**2026-08-09.** Written while extending `QOU.Hecke.InstanceH2` upward. The
survey changed the plan, so it is recorded before any more construction.

## Headline: the class does not characterise `H_n(q)`

`QOU.Hecke.HeckeAlgebra R n q A` asks for four things — a generator map
`embed`, the quadratic relation, the braid relation, far-commutativity, and
that the generators span. It does **not** ask that `A` be free of rank `n!`
over `R`.

Without that, the class is satisfied by algebras far too small. Machine-checked
in `QOU/Hecke/InstanceH2.lean`:

```lean
instance rankOneModel (n : ℕ) : HeckeAlgebra ℚ n 1 ℚ where
  embed := fun _ => 1
  quadratic := by intro i; norm_num
  braid := by intro i j _; simp
  farCommute := by intro i j _; simp
  spans := Subsingleton.elim _ _
```

At `q = 1` the parameter `h = q − q⁻¹` is `0`, so `x = 1` solves `x² = h·x + 1`;
braid and far-commutativity are automatic in a commutative ring; `spans` holds
because `Subalgebra ℚ ℚ` is a subsingleton.

**`ℚ` is a `HeckeAlgebra ℚ n 1 ℚ` for every `n`** — including `n` where
`H_n(1)` has dimension `6, 24, 120, …`.

### What follows

Every result in the corpus proved from `[HeckeAlgebra R n q A]` also holds when
`A = ℚ`, `q = 1`. Those results are not false, but they are **much weaker than
they read**: they are not theorems about the Hecke algebra, they are theorems
about any algebra generated by elements satisfying the braid and quadratic
relations, of which the one-dimensional one is an example.

All five hypothesis sites in the corpus are generic in `n`
(`StaircaseCornerHook`, `Braiding/hecke_mass_trace`,
`BraidsKnots/tmli_constituent_composite_agreement`, `Shared/MarkovTraceClaim`,
and `Machinery/MarkovTraceOnHecke`), so this affects all of them equally.

## So what is actually needed

**Not more instances.** The class is already inhabited at every `n`, trivially.
Building `H3`, `H4`, … against it as written would add nothing that
`rankOneModel` does not already provide.

What is needed, in order:

1. ~~**The missing axiom.**~~ **DONE — `QOU/Hecke/FullRank.lean`.** Added as a
   companion predicate rather than by strengthening `HeckeAlgebra` in place, so
   all five hypothesis sites keep compiling and each can be upgraded
   deliberately:

   ```lean
   class IsHeckeOfFullRank (R : Type u) (n : ℕ) (A : Type u)
       [Field R] [Ring A] [Algebra R A] : Prop where
     free : Module.Free R A
     finrank_eq : Module.finrank R A = n.factorial
   ```

   `not_isHeckeOfFullRank_rankOne` proves the degenerate model fails it at every
   `n ≥ 2`, which is the point. Rank `n!` fixes the *dimension*, not the
   `{T_w}_{w ∈ S_n}` labelling — deliberate: dimension is what downstream
   arguments use and what the degenerate models fail. Granting Iwahori's theorem
   (not formalised; nothing depends on it here), `spans` + `finrank = n!` pins
   `A` to `H_n(q)` up to isomorphism, and neither half alone does.

2. ~~**Then** the instances mean something.~~ **DONE.**
   `instIsHeckeOfFullRankH2` — `AdjoinRoot` of a monic quadratic is free of rank
   `2 = 2!` (`finrank_H2`, via `heckePoly_monic` + `heckePoly_natDegree`), so
   `instHeckeAlgebraH2` is now *provably* the genuine two-strand algebra rather
   than merely believed to be.

## Assembly is inductive, and that is now machine-checked

The rank condition is **not** something to re-establish level by level. `H_{n+1}`
is free of rank `n+1` over `H_n` — the Iwahori coset decomposition

  `H_{n+1} = ⊕_{i=0}^{n} H_n · σ_n σ_{n-1} ⋯ σ_{n-i+1}`

— so the tower law multiplies ranks and `1 = 0!` starts the induction. Both
halves are proved in `QOU/Hecke/FullRank.lean`:

| declaration | content |
|---|---|
| `finrank_succ_of_rung` | rung of rank `n+1` over a level of rank `n!` ⟹ level of rank `(n+1)!` (via `Module.finrank_mul_finrank`) |
| `finrank_of_rank_recursion` | `d 0 = 1`, `d (n+1) = (n+1)·d n` ⟹ `d n = n!` — depends on **no axioms** |
| `isHeckeOfFullRank_succ` | the two composed, ready to `exact` inside an `induction` |
| `instIsHeckeOfFullRankBase` / `…One` | `R` itself at `n = 0, 1` |

So a tower owes **one rung at a time**: "free of rank `n+1` over the level
below". Everything else follows. That is strictly less work than constructing
each `H_n` and computing its dimension from scratch, and it is the shape
`QOU.Mathlib.HeckeAlgebra.HnCarrierRec` (`H_{n+1} ≅ Fin (n+1) → H_n`) and
`basis_dimension_recurses` (`|H_{n+1}| = (n+1)·|H_n|`) were already reaching for
— those two state the recursion; `finrank_of_rank_recursion` closes it.

What this does **not** do is assert such a tower exists. It says what a tower
owes and discharges the arithmetic once and for all. The rungs are still the
work — and the first one is H3.

## H3: most of the work is already done, and stuck on one lemma — **SUPERSEDED**, see item 2 above

`QOU/Mathlib/HeckeAlgebra.lean` already carries a concrete `H_3`:

| piece | status |
|---|---|
| `H3Carrier R = R × R × R × R × R × R` | rank **6 = 3!** — correct |
| `H3.sigma1`, `H3.sigma2`, basis elements | present |
| `H3.mulSigma1`, `H3.mulSigma2` (generator actions) | present |
| `H3.mul` (full multiplication via basis decomposition) | present |
| `H3.sigma1_sq_eq`, `H3.sigma2_sq_eq` | **proved** |
| `H3.braid_relation` | **proved** |
| `H3.one_mul` | **proved** |
| `mul_assoc` for `H3.mul` | **missing** |
| `Ring` / `Mul` instance on `H3Carrier` | **missing** |

The Hecke relations are already theorems. The blocker is that `H3Carrier` is
not a `Ring`, because associativity of `H3.mul` is unproved — and the class
requires `[Ring A] [Algebra R A]`.

**So the H3 task is one lemma, not a construction**: prove `H3.mul` associative,
derive the `Ring` and `Algebra` instances, restate the three relations in ring
form (they are currently in generator-action form, and over `ℝ` specifically
rather than a general field), and the instance follows.

Associativity of a 6-dimensional structure-constant multiplication is finite and
mechanical — `decide` is out of reach on `ℝ`, but the multiplication is defined
by cases on the basis, so it should reduce to a finite check per basis triple
(6³ = 216 cases) after the definition is made basis-wise rather than via
`H3.smul` folds.

## H4 and above — **SUPERSEDED**, see item 1 above

`H4Carrier R = Fin 24 → R` exists, with `H4.one`, `H4.basis`, `basis_count`,
Wedderburn projectors and `H4.markovTraceOnBasis` — but **no multiplication at
all**. `QOU/Machinery/MarkovTraceH4.lean` supplies `mulNF` and the 576-entry
Gram closure (see bean qou-8hjy) on a *different* normal-form basis, and the
two are not connected.

So H4 is a genuine construction, not a bridging exercise, and it should wait
until (1) the class carries the rank axiom and (2) H3 has demonstrated the
pattern.

## Compute side

`computations/` already contains the H3/H4 numerics — `atom_vol_hecke_unified.py`,
`canonical_isospin_pyhecke*.py`, `crt_markov_v2.py`,
`build_markov_trace_assembly_chain.py`, plus witness JSON. These compute with
explicit matrices and normal forms and do **not** depend on the Lean class at
all.

That is the right division, but it means the compute results are not currently
*connected* to anything in Lean: there is no theorem saying the Python normal
form and the Lean carrier agree. The `hecke_regular_nf_table.py` →
`MarkovTraceH4.lean` generator is the one place where they are, and it emits
data rather than a correspondence proof.

**What compute needs from Lean**: nothing urgent. **What Lean needs from
compute**: the H3 structure constants in a form that makes the associativity
check above mechanical — `gen_gram_closure.py` already demonstrates the
generator pattern that would do it.

## Recommended order

1. ~~Add the rank axiom (as a companion predicate).~~ **DONE** —
   `QOU/Hecke/FullRank.lean`, bean qou-nkd8. Carried the induction with it, so
   the remaining levels are rungs rather than constructions.
2. ~~Prove `H3.mul` associativity; derive `Ring`/`Algebra`; instantiate at
   `n = 3`.~~ **DONE** — `QOU/Hecke/InstanceH3.lean`, bean qou-jr3k. See below.
3. `MarkovTrace` on `H2` (bean qou-ghak) — independent of the above and cheap.
4. ~~H4 multiplication~~ **Instance DONE** — `QOU/Hecke/InstanceH4.lean`. Rank
   `24 = 4!` still open (bean qou-awp7). See below.

## How far up does the ladder need to go? — **stop at 4**

Asked and answered with evidence, because it decides how much of this is worth
building.

1. **No site asks for a specific `n`.** Every `[HeckeAlgebra R n q A]` binder in
   the tree has `n` as a *variable* — `QuantumBloch/PentagonUvCommutation.lean`,
   `Hecke/MarkovTrace.lean`, `Machinery/MarkovTraceOnHecke.lean`. Nothing is
   waiting on `H₁₂`.

2. **Three axiom shapes, and `n = 4` exhausts them.** `Generator n` carries
   `idx : Fin (n - 1)`.

   | level | first satisfiable |
   |---|---|
   | `n = 2` | quadratic only — one index, so braid and far-commutativity are unsatisfiable |
   | `n = 3` | **braid** (`Generator.adjacent ⟨0⟩ ⟨1⟩`) |
   | `n = 4` | **far-commutativity** — needs indices differing by `≥ 2`, so `n - 1 ≥ 3` |
   | `n ≥ 5` | nothing new |

   Machine-checked: `∀ i j : Generator 3, ¬ Generator.farCommuting i j`, and
   `Generator.farCommuting (⟨0⟩ : Generator 4) ⟨2⟩`.

3. **The corpus's `n = 12` content never touches the algebra.**
   `wedderburn_n12_via_witness` (`p(12) = 77`, `12! = 479001600`),
   `TwoRowStratum`, `WenzlBridgeConcrete`, `RSKSubstrateInstances`,
   `witness_12C` — combinatorics and numerics, discharged by witness-supplying
   factories. The physics levels (`H₆` ²H, `H₉` ³H/³He, `H₁₂` ⁴He, `H₁₈` ⁶Li, up
   to `H₁₂₀`) live in `computations/`, with explicit matrices.

4. **There is no ladder to 12 anyway.** `H3.mul_assoc` was 6 components over 18
   variables. `H₄` is 24 over 72 — at the edge, and only reachable because Python
   generated the tables. `H₅` is 120; `H₁₂` is 479 001 600 basis elements.

If `H₁₂` is ever needed it comes generically — one
`instance : HeckeAlgebra R n q (H R n q)` by induction on `n`, discharging every
site at every `n` at once. The rank half of that induction is done
(`FullRank.lean`); the multiplication half needs Coxeter word reduction /
Matsumoto, and Mathlib at rev `f897ebcf` has `GroupTheory/Coxeter/{Basic,
Inversion,Length,Matrix}` but **no Hecke algebras at all**. Mathlib-scale, not a
session.

## H4, done — via the operator algebra

The obvious route died on measurement. Putting a `Ring` on `Fin 24 → R` with
`MarkovTraceH4`'s `mulNF` (as `InstanceH3` does with `H3.mul`) hits the depth-6
`whnf` wall that module's docstring names: `mulNF` composes up to six `mulσ`s, so
associativity unfolds to depth twelve. Measured — `simp` exhausts 4 000 000
heartbeats after **seven minutes** without closing one generator case.

`QOU/Hecke/InstanceH4.lean` uses the **right regular representation** instead:
each `mulσk` is an `R`-linear endomorphism of `Fin 24 → R`, and the algebra is
the subalgebra of `Module.End R (Fin 24 → R)` they generate. Associativity is
function composition — free, never unfolded. What remains is exactly the Hecke
presentation, at depth ≤ 3:

| lemma | depth | relation |
|---|---|---|
| `mulσ_sq0/1/2` | 2 | `σₖ² = 1 + h·σₖ` |
| `mulσ_farcomm02` | 2 | `σ₀σ₂ = σ₂σ₀` — the point of `n = 4` |
| `mulσ_braid01/12` | 3 | `σᵢσⱼσᵢ = σⱼσᵢσⱼ` |

All six in 13 seconds. They are independently valuable: until now the claim that
`mulσ0/1/2` satisfy the Hecke presentation rested on the Python generator's
cross-validation, not on anything Lean had checked.

`not_commutative` (the two products send the identity basis vector to normal-form
positions 8 and 7) excludes every commutative model, `rankOneModel` included,
before any rank computation. Full rank `24 = 4!` is bean qou-awp7 — and with the
six relations proved, its `3 × 24` closure table is symbolic word rewriting
rather than coordinate expansion.

Step 3 is a day or less. Step 4 is the real infrastructure work the manuscript
cites — but the inductive framing is what makes it finite: each level is `n+1`
cosets over the level below, never `n!` structure constants from scratch.

## H3, done

`H3.mul_assoc` closed on the first attempt. Every coefficient of `H3.mul` is
polynomial in the eighteen input coefficients and the single scalar `q - q⁻¹`, so
associativity is a polynomial identity that `ring` discharges componentwise. That
it *is* an identity is the content — it says `H3.mulSigma1` and `H3.mulSigma2` are
a faithful transcription of left multiplication in `H₃(q)`, not merely a plausible
pair of `6 × 6` matrices.

`QOU/Hecke/InstanceH3.lean` then carries `H3Alg R q` (a `def` synonym for
`H3Carrier R`, so `Prod`'s componentwise `CommRing` cannot leak in), its `Ring`
and `Algebra` instances, the quadratic and braid relations restated over an
arbitrary field in ring form, `decompose` (every element is an `R`-combination of
words in the generators), **`instHeckeAlgebraH3`**, and
**`instIsHeckeOfFullRankH3`** — rank `6 = 3!`. All axiom-clean.

**It is the first non-vacuous braid relation in the tree.** `InstanceH2` said so
about itself: at `n = 2`, `Generator 2` has a single index, so `BraidRelation` and
`FarCommutativity` are never satisfiable and both fields are discharged by
`absurd`. At `n = 3` the two indices *are* adjacent and `braid` must be real.
