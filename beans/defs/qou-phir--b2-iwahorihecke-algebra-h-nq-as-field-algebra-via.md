---
# qou-phir
title: 'B2: Iwahori–Hecke algebra H_n(q) as field-algebra (via Mathlib Coxeter T_w basis / quadratic+braid rels) + cell/Specht modules'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-24T16:21:38Z
updated_at: 2026-11-18T08:59:30Z
parent: qou-k4oq
---

## Worked 2026-08-30 — the ALGEBRA is built; the basis and cell modules are not

This bean was a bare title with no body, so recording both what it turned out to
mean and where it now stands. It has three parts and **one of them is done**.

### First: "we already have Hecke in Lean" is true in a much weaker sense than it sounds

- **Mathlib has no Hecke algebra of any kind.** Measured against the built `.olean`
  tree, because the Mathlib **source is absent in this container** — an initial
  source grep returned zero and that was a *false negative from an empty
  directory*, not a measurement. Re-run over the oleans with `CoxeterSystem` as a
  positive control: `CoxeterSystem` in 3 modules, `Hecke` in **1**, and that one is
  `Mathlib/NumberTheory/FLT/Basic`, a docstring mention of Hecke *operators*.
- **The corpus's `QOU/IwahoriHecke/` is 1429 lines across 7 files and is entirely
  self-contained** — nothing outside that directory imports it.
- **What it builds is not a Hecke algebra.** `IwahoriHeckeQuot` imposes the
  **quadratic relation only**; braid relations were deferred. So it is the free
  product of one copy of `R[x]/((x−q)(x+1))` per generator, and every theorem
  stated about it is a theorem about that free product.
- **The generic `IwahoriHecke W R q` is worse than "quadratic-only": it is
  mis-shaped.** It is `IwahoriHeckeQuot R q (Set.univ : Set W)` — quadratic
  relations imposed on **every group element**, not on simple reflections. For the
  real Hecke algebra `T_w` with `ℓ(w) ≥ 2` does *not* satisfy `(T_w − q)(T_w+1) = 0`,
  so this is not the "well-defined intermediate object" its docstring claims. The
  construction already takes an arbitrary `S : Set W`; the defect is purely that
  this caller passes the wrong `S`. NOT fixed here — see below.
- **`IwahoriHeckeOfSn` is correctly shaped**: it passes
  `adjacentTranspositionIndex n : Set (Fin (n-1))`, i.e. the simple reflections.
  Only braid relations were missing from it.

### Second: a live AXIOM, on a stale excuse — now proved and deleted

`Defn.lean` carried `axiom universal_property`. Its docstring gave the reason: two
tactic attempts *"could not be verified locally because the remote container has no
`lake` binary and elan cannot reach the Lean release server (network policy)"*.

That obstacle is gone. Existence was already proved; only **uniqueness** was
axiomatised, and it is three steps — `RingQuot.mkAlgHom` is surjective, so two
algebra maps out of the quotient agree as soon as their composites with it do; those
are maps out of a **free** algebra, so `FreeAlgebra.hom_ext` reduces that to the
generators, which is the hypothesis. Landed as `Quotient.hom_ext`;
`universal_property` is now a theorem. Choice-free (`[propext, Quot.sound]`).

### Third: the algebra itself — DONE

`QOU/MathlibExt/IwahoriHeckeAlgebra.lean`, Mathlib-style, generic `[CommRing R]`:
`HeckeAlgebra R q M` for a Coxeter matrix `M`, as `RingQuot` of `FreeAlgebra R B`
modulo an **inductive** relation carrying both the quadratic and the braid family.
Delivers `T`, `T_quadratic`, `T_braid`, `lift`, `lift_T`, `hom_ext`,
`exists_unique_lift`. All choice-free.

Three design choices worth keeping: the relation is an inductive rather than a set
of ideal generators (`RingQuot` closes an arbitrary relation into a ring congruence,
so no ideal-membership reasoning reaches any downstream proof); `M` is a bare
`B → B → ℕ` rather than a `CoxeterMatrix` (nothing needs symmetry or the diagonal
condition, and requiring it would couple the file to an API that has drifted across
Mathlib refactors); and `altProd` plus `map_altProd` are defined here because
Mathlib has no alternating-word product over a monoid.

Type A landed alongside it in `QOU/BraidKnot/HeckeTypeAInstance.lean` and closes
`qou-0o6j`.

### What is STILL OPEN in this bean

1. **The `T_w` basis.** The bean's title says "via Mathlib Coxeter `T_w` basis". Not
   built. The construction above is by generators and relations; the standard basis
   indexed by `W` with the length-based multiplication rule
   (`T_s T_w = T_{sw}` when `ℓ(sw) > ℓ(w)`, else `q T_{sw} + (q−1) T_w`) is a
   separate theorem — and it is the one that needs Matsumoto / reduced expressions,
   i.e. the genuinely hard part.
2. **Cell / Specht modules.** Not started.
3. **The mis-shaped generic `IwahoriHecke W R q`** (`Set.univ` over `W`). Deliberately
   not touched: changing which `S` it passes is a signature change across the five
   consumers in that directory, and it is a different job from building the algebra.
   Worth its own bean.

Note for whoever takes (1): the blocker this arc has cited for a year — the Coxeter
order accessor being "in flux in Mathlib's `CoxeterSystem` API" — is not a blocker
for the *presentation*. `m_{st}` is just `orderOf (s * t : W)`. It may still bite for
the basis, where reduced expressions really are needed.


### Correction + coordination (same day): Mathlib HAS `CoxeterMatrix.Aₙ`, and a sibling proved the S_n bridge

Two amendments to the survey above, both found by reading sibling PR #6053
(`qou-lrz1`) rather than by my own greps:

1. **`CoxeterMatrix.Aₙ : (n : ℕ) → CoxeterMatrix (Fin n)` is in Mathlib**, with
   exactly the entries my `typeAMatrix` computes. I wrote mine without knowing it
   existed. The ℕ-indexing is kept deliberately — it is what buys the *unbounded*
   `HeckeGenerators`, where `Aₙ N` is `Fin N`-indexed and pins one `n` — but
   `typeAMatrix_eq_An` now states the agreement so the two are connected rather
   than parallel. **This does not weaken "Mathlib has no Hecke algebra":** the
   Coxeter *theory* is there (that was never in doubt); the *algebra* is not.
2. **`S_{n+1}` IS the Coxeter group of type `Aₙ`, formalized** —
   `QOU/Hecke/SymmetricCoxeter.lean::permCoxeterSystem` on #6053, sorry-free at
   general `n`, plus the `IsCoxeterGroup` instance. That sibling also measured
   that Mathlib has **zero** `IsCoxeterGroup` instances, so `cs.length` and all of
   `Coxeter/Length.lean` / `Coxeter/Inversion.lean` had never been applied to a
   concrete group before.

**This changes the outlook on open item (1), the `T_w` basis.** My note above
said the basis "needs Matsumoto / reduced expressions, i.e. the genuinely hard
part". #6053 is taking the **Bourbaki route instead**, which sidesteps Matsumoto
entirely: build the free module `W →₀ R`, define right multiplication `Rs i`
directly on the basis by the length dichotomy, and get well-definedness as a
*consequence* of having a representation rather than as a prerequisite. Their
`Rs_sq` (the quadratic relation) is proved; the braid relation for `Rs` is the
remaining step.

So the two halves fit: their `Rs` needs braid, and once it has it,
`exists_unique_lift` from `QOU/MathlibExt/IwahoriHeckeAlgebra.lean` is exactly the
map `H_n(q) → End (W →₀ R)` — no hand-built algebra map required. Recorded on
#6053. **The `T_w` basis stays theirs**; this bean should not duplicate it.


---

## 2026-08-30 — the `T_w` basis LANDED (on #6053), and my survey had a gap

**Open item (1) is closed, by the sibling, not by me.** `QOU/Hecke/TwBasisField.lean`
on #6053: `basisTwOfField : Module.Basis (Equiv.Perm (Fin (n+1))) K (IwahoriHecke K q n)`
and `finrank_eq_factorial : Module.finrank K (IwahoriHecke K q n) = (n+1)!`, sorry-free
at general `n`, `#print axioms` clean.

They went **around Matsumoto**, not through it — `T_w` is the product along *some*
reduced word, and well-definedness is never invoked because along any reduced word the
operators merely walk the basis. Matsumoto remains an open Mathlib TODO
(`Coxeter/Basic.lean:78`) and is still unproved here. My note above called the basis
"the genuinely hard part"; that framing was pessimistic about the *route*, not wrong
about Matsumoto.

They also proved `TwBasisBraid.Rs_braid`, the step I had flagged as open.

## My survey had a real gap — recorded because it affects `qou-b5gu` too

I reported "the corpus's `IwahoriHecke` cluster is 1429 lines over 7 files and is
entirely self-contained." True **of that cluster**; I stated it as though it
characterised the corpus's Hecke situation. It does not. I never found
`QOU/Hecke/IwahoriHecke.lean` or `QOU/BraidKnot/IwahoriHeckeAPI.lean`, because I
grepped for **consumers of the names I already had** rather than for Hecke-algebra
**definitions as a class**. The `qou-b5gu` blast-radius measurement inherits that
narrowness.

## Measured: TEN Hecke-algebra-shaped definitions, not six

The sibling opened `qou-img9` listing six. Re-measured with a definition-shaped grep:
**ten**. The four extra are all `structure HeckeAlgebra`, and they are a *different*
defect — three are verbatim identical:

```lean
structure HeckeAlgebra where
  n : ℕ ; carrier : Type* ; q : R_q ; q_ne_zero : q ≠ 0
```

`carrier : Type*` with **no relation of any kind** and nothing tying it to `n` or `q`;
the only assertion is `q ≠ 0`. (`knot-eigenbasis-complete.lean:53`,
`QOU/PathIntegrals.lean:294`, `QOU/BraidKnot/CasimirShared.lean:176`.) The fourth,
`frobenius-antipode-lean-stub.lean:35`, wraps a single real: `{coeff : ℝ}`, both
parameters underscore-prefixed, over `ℝ`.

So the bare name `HeckeAlgebra` resolves to **five** things, four carrying no Hecke
content. That is a naming defect, not a reconciliation problem, and belongs as its own
rows in `qou-img9`.

**Measurement trap for whoever re-runs this:** the raw grep returns **twelve**. Two are
false positives from my own docstrings — the `Defn.lean` and `TypeA.lean` rebuilds
quote the superseded definitions inside ` ```lean ` fences to show what changed, and a
line-oriented grep counts those as live.

## What is still open in this bean

**Cell / Specht modules only.** Not started. The `T_w` basis is done and is not mine to
redo.

Two caveats on the basis, from the sibling and not contested: it is at `Q = q` while
`HeckeAlgebra R q M` here is used at `Q = q²`, and **the transport across the
convention bridge is unproved** — do not cite the basis as applying to `HeckeAlgebra`
until someone proves it. The field hypothesis is confined to the dimension squeeze;
everything upstream holds over a commutative ring.


## 2026-08-30 — the T_w basis TRANSPORTS: two presentations proved equal

`QOU/BraidKnot/HeckeTypeAPresentationEquiv.lean`:

```lean
noncomputable def algEquiv :
    IwahoriHeckeOfSn K q (n + 1) ≃ₐ[K] QOU.Hecke.IwahoriHecke K q n
```

sorry-free, `#print axioms` clean, generic `[CommRing K]`.

This closes the gap #6053's author flagged and explicitly did **not** claim: their
`finrank_eq_factorial` (`dim H = (n+1)!`) is proved against *their* presentation, and
whether it reached mine was unproved. An `AlgEquiv` carries a basis and a finrank, so it
now does — and through `IwahoriHeckeOfSn` it reaches the `HeckeGenerators` instance and
the whole JM/full-twist arc.

**It went through because the two are the same relations in different shape.** Both are
`RingQuot (FreeAlgebra K (Fin n))`; theirs writes quadratic / braid / commute as three
constructors with `Fin`-index side conditions, mine packages the last two into one
`altProd` family indexed by the Coxeter matrix. Built from the two universal properties,
so neither presentation is privileged.

Two reconciliation details worth keeping:

- **My family has a case theirs has no constructor for.** `altProd (σ i) (σ j) (M i j)`
  at `i = j` gives `M i i = 1`, `altProd a b 1 = a`, so the diagonal is `rfl`. Theirs
  omits it. It is the first case in every split.
- **Their `commute` is one-sided** (`j + 2 ≤ i`), mine symmetric — so the far case
  splits on `lt_or_gt_of_ne` and uses `σ_commute` one way and `.symm` the other.

**Index offset:** theirs has `Fin n` generators and is `H_{n+1}(q)`; mine at `m` has
`Fin (m-1)`. The match is `m = n+1`.

**Not done:** the `finrank_eq_factorial` corollary itself. `TwBasisField` is on their
branch, not main, so it cannot be written yet — `algEquiv` is the mechanism, the
one-line corollary waits on their merge. Offered it to them since the basis is theirs.

**This changes the read on `qou-b5gu` / `qou-img9`.** If presentations can be *proved
equal* pairwise, "retire vs repair" is less pressing than it looked: the cost of an
extra name is bounded by whether an equivalence exists, and here one did. That argues
for proving more of these before deleting any.


## 2026-08-30 — the cell/Specht half: what is now proved, and what is not

`QOU/BraidKnot/HeckeCellular.lean`. **This is not a cellular structure**, and the file
header says so first. It is the part of the Graham–Lehrer datum provable from the
presentation alone, plus the two cell modules that exist for every `n`.

### Proved

- **`antiAut` — cellular axiom (C2).** The anti-automorphism fixing every generator, as
  an algebra map into the opposite algebra. It exists because the defining relations are
  **palindromic**. This is a prerequisite for Specht theory rather than a corollary: it
  is what makes the bilinear form on a cell module symmetric, hence what lets the
  radical of that form cut out the simple head.
- **`T_quadratic_swap`** — the quadratic relation with factors reversed, which is the
  form the opposite algebra needs. Choice-free.
- **`signRep`** (in MathlibExt, beside `indexRep`) — `T_i ↦ −1`. Its quadratic check is
  *cheaper* than `indexRep`'s: the **second** factor `(T_i + 1)` vanishes outright, so
  `q` is never used.
- **`typeAIndexRep` / `typeASignRep`** — the `q`-analogues of the trivial and sign
  representations, i.e. the extreme cell modules `S^{(n)}` and `S^{(1ⁿ)}`.
- **`indexRep_ne_signRep`** — they are distinct exactly when `q ≠ −1`. That collision
  point is where semisimplicity starts to fail, which is why the cellular machinery is
  needed at all.

`lean`-direct exit 0, no warnings, no sorries; `#print axioms` clean on all nine.
`T_quadratic_swap`, `signRep` and `indexRep_ne_signRep` are choice-free.

### Why type A, and not a general Coxeter matrix

Worth recording because it is the whole reason this was tractable. For general `M` the
reversal of `altProd a b m` is `altProd a b m` when `m` is odd and `altProd b a m` when
`m` is even, so the general anti-involution needs a parity lemma **plus** a chain of
auxiliary word identities (`altProd a b (n+1) = altProd a b n * last`, and the
even/odd split). In type `A` the matrix takes only `1, 2, 3`, and at each value the
commutation the reversal needs is *supplied by the relation itself*:

| `m` | reversal needs | supplied by |
|---|---|---|
| 1 (`i = j`) | nothing | both sides are `altProd _ _ 1` |
| 2 (far) | `a·b = b·a` | far-commutation |
| 3 (adjacent) | `a·b·a = b·a·b` | braid |

Three-way case split, no parity argument. And type `A` is where Specht modules live.

### STILL OPEN — the Murphy basis

`{m_{s,t}}` indexed by pairs of standard tableaux. It is what makes cellular axioms
**(C1)** and **(C3)** statable at all, and with it the general Specht module `S^λ`.
Needs the `T_w` basis (proved on #6053, transported here by `algEquiv`) plus
standard-tableau combinatorics and the dominance order. Nothing in the file claims any
of it.

So this bean's remaining scope is now exactly: **the Murphy basis and `S^λ`**. The two
extreme cell modules are done; the general ones are not.


## 2026-08-30 — the transport landed, and the Murphy base case with it

**#6053 merged at 07:52Z**, so both halves of what I offered there became writable.

### The transport (closes the gap #6053's author declined to claim)

```lean
theorem finrank_IwahoriHeckeOfSn :
    Module.finrank K (IwahoriHeckeOfSn K q (n + 1)) = Nat.factorial (n + 1)
noncomputable def basisTwOfSn :
    Module.Basis (Equiv.Perm (Fin (n + 1))) K (IwahoriHeckeOfSn K q (n + 1))
```

`algEquiv` is an `AlgEquiv`, hence a linear equivalence, so it moves both the dimension
and the basis. `dim_K H_n(q) = (n+1)!` now holds on the `HeckeAlgebra`-backed side.

### Murphy, base case

Murphy's basis is `m_{st} = T_{d(s)}^* · x_λ · T_{d(t)}` with `x_λ = Σ_{w ∈ S_λ} T_w`,
whose defining property is being a **`q`-eigenvector**: `σ_i · x_λ = q · x_λ` for
`s_i ∈ S_λ`.

The **rank-one** case is proved — `S_λ = ⟨s_i⟩`, `x = 1 + σ_i`, both multiplication
orders. It needs nothing but the quadratic relation: `σ_i + σ_i² = q(1 + σ_i)` *is*
that relation rearranged. `parabolicSym`, `sigma_mul_parabolicSym`,
`parabolicSym_mul_sigma`.

### The general case — precisely what is left

`x_λ` for a general Young subgroup is a sum over `S_λ`, and the eigenvector property is
proved by **pairing each `w` with `w s_i`**: one of the two has length going up, the
other down, and the two `rsFun` branches combine to `q·(T_w + T_{w s_i})`. That pairing
argument over `Equiv.Perm (Fin (n+1))` is the open work.

**The blocker is now the combinatorics, not the algebra.** The `T_w` basis the argument
needs is merged and transported. What remains is the Young subgroup as a subgroup of
`Equiv.Perm`, the sum over it, and the length-involution pairing.

`lean`-direct exit 0 on both files, zero errors, zero warnings, re-run after rebasing
across a further 124 commits of main. `#print axioms` clean on all five new
declarations.

### Method note worth keeping — the stale-olean trap

Building the sibling's `QOU/Hecke/` chain with a loop that builds only **missing**
oleans left pre-existing stale ones in place, and they shadowed newer sources. The
symptom is an `unknown constant` error that reads exactly like a broken `main` — I
nearly reported `WedderburnRankDegeneracy.lean` as broken twice. Both constants
(`yLambda_determined`, `dimHLF_column`) existed; the oleans were up to **five days**
older than their sources. Refresh on `source -nt olean`, not on absence.


---

## 2026-08-30 — the general Murphy `x_λ` is CLOSED. `QOU/BraidKnot/HeckeMurphy.lean`.

The item this bean left open — *"that pairing argument over `Equiv.Perm (Fin (n+1))` is the open
work"* — is proved, for **general** `λ`, not just the rank-one case that landed earlier today.

- `σ_mul_Tw_pair (i) (v) : σ_i · (T_v + T_{v s_i}) = q · (T_v + T_{v s_i})` — **unconditional**,
  no ascent/descent hypothesis.
- `σ_mul_murphySum (i) (S) (hS : ∀ w ∈ S, w * s_i ∈ S) : σ_i · x_S = q · x_S`, where
  `x_S = Σ_{w ∈ S} T_w`.
- `σ_mul_murphySum_subgroup (i) (H) (hi : s_i ∈ H)` — the Young-subgroup form, i.e. Murphy's
  `x_λ` proper.

`lean`-direct EXIT=0, errors=0 warnings=0; `#print axioms` on all seven declarations gives
`propext / Classical.choice / Quot.sound`, no `sorryAx`.

### The move that made it tractable, which is worth carrying to the next piece

I had this bean's own plan wrong. It said the blocker was "the combinatorics" — pairing `w` with
`w s_i`, one length up and one down, then combining the two `rsFun` branches. That is the right
mathematics, but implemented directly it means partitioning `S` into ascents and descents and
building a bijection between the halves, which is the expensive part.

**None of that is needed.** The two branches are exactly complementary *on a pair*, so the pair
identity holds with no hypothesis at all — whichever of `w`, `w s_i` ascends, the coefficients
recombine the same way (`1 + (q−1) = q`). Restated as `f w + f (w s_i) = 0` for
`f w = σ_i T_w − q T_w`, that is verbatim the hypothesis of `Finset.sum_involution`. The sum then
vanishes with no partition of `S` at all.

**And the payoff is not just brevity.** The obvious one-line alternative — sum the pair identity
over all of `S`, getting `2σx = 2qx` — needs `2` invertible and would have quietly imported a
characteristic hypothesis into the foundation of the Murphy basis. The involution route does not.

Built on `QOU.Hecke.TwMul`'s `σ_mul_Tw_of_lt` / `σ_mul_Tw_of_not_lt` rather than re-deriving the
structure constants, and on the `T_w` basis from #6053 that this branch transported — so the
transport was load-bearing rather than decorative.

### What remains of `qou-phir`, stated so nothing reads as covered

The eigenvector property is **not** the Murphy basis. Still open:

1. **That the `m_{st} = T_{d(s)}^* x_λ T_{d(t)} are a basis** — needs coset representatives `d(s)`
   indexed by standard tableaux, hence standard-tableau combinatorics, which the corpus does not
   have.
2. **Cellular axioms (C1) and (C3)** — (C1) is the basis statement plus the indexing; (C3) needs
   the **dominance order** on partitions and the filtration it cuts out. (C2), the anti-involution,
   is already proved (`antiAut`, this branch).

So the remaining blocker really is combinatorics this time — specifically standard tableaux and
dominance — and unlike the eigenvector property there is no algebraic shortcut around it.

### An authoring trap that cost a compile cycle

`abbrev sw (i : Fin n)` written under a `variable (n : ℕ)` block makes `n` an **explicit**
argument of `sw`, so every later `sw i` elaborates as `sw (n := i)` with `i` read as the rank. The
error surfaces far from the cause, as `Fin ↑i → Equiv.Perm (Fin (↑i + 1))` mismatches at the use
sites. Bind `n` implicitly in the signature when a helper needs only some of the block's variables.


---

## 🛑 CORRECTION 2026-08-30 — the "remaining scope" I wrote above is WRONG (PR #6239)

The entry above says the Murphy basis needs *"standard-tableau combinatorics and the dominance
order"* and calls that the blocker, having said in the merged #6158 that **neither is in the
corpus**. Both are in the corpus. I never ran the six-path check on that claim — I ran it on
*"is the Murphy basis already done"*, which is a different question.

**Present, measured on `main` at `23eb5aa296`:**

- `StandardYoungTableau (μ : YoungDiagram)` — **twice**, in `QOU/BraidKnot/` and `QOU/Mathlib/`,
  with a `Finite` instance, `numSYT`, `hookLength`, `hookProduct`, and roughly **seventy**
  supporting files (`SYTEnumeration`, `SYTHookFormula*`, the Schensted group, `SYTBranching*`).
  Mathlib has `YoungDiagram` and `SemistandardTableau` but **no** `StandardYoungTableau`, so this
  is all local — which is part of why it reads as absent.
- `partitionDom`, the **dominance order**, at `QOU/BraidKnot/SpechtClassification.lean`, with
  `partitionDom_refl` and `partitionDom_antisymm` **proved**; `domRel` on tabloids in
  `SpechtDominanceCore`; the classification direction `dom_of_intertwiner`.
- `colSuperstandard (μ) : Specht.Tableau μ` and `colSuperstandardSYT` — the reference tableau
  `t^λ` that `d(t)` is defined against. I did not even know to look for this one.

**What IS missing, stated precisely so this entry does not repeat the error in the other
direction:** the **`q`-deformation**. The entire 21-file Specht cluster is the **`q = 1`
symmetric-group** theory — it works over `Representation k (Perm (Fin n))` and no file in it
imports the Hecke algebra. Murphy's basis is the `q`-analogue over `H_n(q)`, and that does not
exist.

**And the cluster is not a settled base:** **310 `sorry`s** across those 21 files —
`SpechtStandardBasisCore` 107, `SpechtIrreducible` 57, `SpechtDominanceCore` 51. So the inputs
exist as definitions and partial theory, not as something to lean on unchecked.

### Corrected remaining scope

Only the `q`-analogue steps, and each one now names an existing object to build against:

1. **`d(t)`** — the permutation with `t = t^λ · d(t)`, against `colSuperstandard`.
2. **Index reconciliation** — `Perm (Fin (Specht.nOf μ))` (the Specht cluster) against
   `Equiv.Perm (Fin (n+1))` (the Hecke `T_w` basis). This is bookkeeping but it is real, and it
   is the join point between the two clusters.
3. **(C1)** — that `m_{st} = T_{d(s)}^* x_λ T_{d(t)}` spans and is independent, using the
   transported `basisTwOfSn`.
4. **(C3)** — the filtration, against the **existing** `partitionDom` rather than a new order.

(C2) is already proved (`antiAut`, #6158) and the eigenvector property `σ_i x_λ = q x_λ` is
proved for general `λ` (`σ_mul_murphySum`, #6158).

### The method note, which is the durable part

The failure was not the fact, it was that I asserted an absence without checking it — and this
is the **second** instance in one session. The first: I reported the `IwahoriHecke` cluster as
"entirely self-contained" and a sibling (#6053) found two presentations I had missed, because I
grepped for *consumers of names I already held* rather than for the concept as a class. Same
shape both times — a search scoped to what I already knew about, reported as a fact about the
corpus.

Had the wording stood, it would have sent the next agent to rebuild seventy existing files.


---

## 2026-08-30 — (C1) route MEASURED: it is a PORT, not a from-scratch build

#6239 merged (`03472c8e88`). (C1) is now both **statable** and **one-sided**, and — the finding
that matters — the corpus already contains a **complete, sorry-free proof of its `q = 1`
analogue**, by exactly the argument Murphy's basis needs.

### What landed (#6158 + #6239)

`QOU/BraidKnot/HeckeMurphyYoung.lean`, 12 declarations, all axiom-clean:

- `youngSubgroup`, `σ_mul_murphySum_young` — `σ_i · x_λ = q · x_λ` for a real tableau's Young
  subgroup (`Specht.rowStab`, re-indexed).
- `dOf` + `dOf_colSuperstandard` + `colSuperstandard_trans_dOf` + `dOf_injective` — `d(t)`.
- `antiAutTw` — cellular (C2) transported across `algEquiv` via Mathlib's `AlgEquiv.op`.
- `dAt`, **`murphyM`** — Murphy's `m_{st}`, definable for the first time.
- `murphyIndex_card_eq_finrank` — `∑_p (#SYT p)² = dim_K H_n(q)`.
- `MurphyIndex` + `murphyIndex_card` — the index as a **type**, `Nat.card = n!`.

So (C1) is writable as `Module.Basis (MurphyIndex (n+1)) K (QOU.Hecke.IwahoriHecke K q n)` over
an index of provably correct size, and **proving either spanning or independence finishes it** —
the other follows by dimension count.

### The `q = 1` template, all sorry-free (verified by comment-stripped count)

| declaration | file | what it gives |
|---|---|---|
| `standardPolytabloid_triangular` | `SpechtStandardBasis` | triangularity w.r.t. the dominance order |
| `standardPolytabloid_linearIndependent` | `SpechtStandardBasis` | independence, **from** triangularity |
| `standardPolytabloid_span` | `SpechtStandardBasisCore` | spanning, by **Garnir straightening** (`straightening_step_colMax`) |
| `standardBasis` | `SpechtStandardBasis` | `Module.Basis (StandardYoungTableau μ) k (SpechtSubmodule μ)` |
| `specht_finrank_eq_numSYT` | `SpechtStandardBasis` | `dim_k S^μ = #SYT μ` |

Supporting machinery in `SpechtTriangularCore` (also sorry-free): `standardPolytabloid_dominance_order`,
`leadTab_injective`, `standardPolytabloid_diag_unit`, `colStab_inf_rowStab_eq_one`.

**This is the same argument, at `q = 1`.** It works over `Representation k (Perm (Fin n))`; nothing
in the cluster imports the Hecke algebra. So (C1) is the `q`-deformation of a proof this corpus
already owns end-to-end — a port with a worked reference, not a blank page.

### Concrete next step

Port `standardPolytabloid_triangular` to `H_n(q)`: show `m_{st}` expands in the `T_w` basis
(`basisTwOfSn`, transported #6158) with a **unit** diagonal coefficient and strictly-dominance-lower
off-diagonal terms. Independence then follows exactly as at `q = 1`
(`Triangular.linearIndependent`), and `murphyIndex_card` upgrades it to a basis without needing
Garnir straightening at all — which is the expensive half of the `q = 1` proof and is **avoidable
here**, because the cardinality is already known.

That last point is the payoff of `murphyIndex_card`: at `q = 1` both spanning and independence had
to be proved; here only one does.

### Scale note, stated honestly

`SpechtStandardBasisCore` is 170 KB. The `q = 1` triangularity took that much. The port is a real
tranche, not a session's tail — do not start it expecting a quick win, and do not pad it with a
`sorry`-laden scaffold if it does not close.


---

## 2026-08-30, later — the (C1) remainder is SHARPER than #6281 said: no machinery port at all

#6281 said (C1) is "a port of `standardPolytabloid_triangular`". Measured, that **overstates the
work**: the two load-bearing levers are **fully generic** and already sorry-free, so nothing needs
porting. Only three field proofs remain, at named instantiations.

### The two levers, verified generic by `#check` and axiom-clean by `#print axioms`

```
QOU.BraidKnot.SpechtStandardBasis.Triangular.linearIndependent :
  ∀ {ι α R} [LinearOrder α] [CommRing R] {v : ι → α →₀ R} {lead : ι → α},
    Triangular v lead → LinearIndependent R v
```

No Specht, no partition, no `q = 1` — it is a statement about an arbitrary `Finsupp` family over an
arbitrary `CommRing`. Its own docstring calls it *"the lemma the pinned Mathlib lacks"* and *"a
natural Mathlib-upstream candidate"*.

```
QOU.BraidKnot.SpechtDominanceCore.exists_linearOrder_of_partialOrder :
  ∀ {α} [Fintype α] [DecidableEq α] (r) [DecidableRel r],
    reflexive → transitive → antisymmetric → ∃ _ : LinearOrder α, ∀ a b, r a b → a ≤ b
```

Also generic, also filling a Mathlib gap (no `Szpilrajn` / `LinearExtension` at the pin). This
manufactures the linear order the `Triangular` structure requires **from** a partial order — so the
dominance order does not have to be linearised by hand.

Both: `propext / Classical.choice / Quot.sound`, no `sorryAx`.

### What actually remains — three goals, not a tranche

Instantiate `Triangular v lead` with

| slot | value |
|---|---|
| `ι` | `MurphyIndex (n+1)` (#6239) |
| `α` | `Equiv.Perm (Fin (n+1))` — `Fintype` + `DecidableEq` ✓, linear order via the lever above |
| `R` | `K` |
| `v i` | `(basisTwOfField K q n).repr (murphyM K q n h i.s i.t)` |
| `lead` | the leading permutation of `m_{st}` — **the one genuinely new object** |

and prove the three fields:

1. **`lead_inj`** — distinct tableau pairs have distinct leading permutations. The `q = 1` analogue
   is `leadTab_injective`, proved via `leadTab_injective_core`, `rowSet_eq_of_rowPattern_eq` and
   `entry_eq_orderEmbOfFin`; the argument is about **tableau combinatorics, not about `q`**, so it
   should transfer with the index re-mapping rather than be re-derived.
2. **`diag_unit`** — the diagonal coefficient is a unit. `repr_murphySum_one_of_subgroup` (#6285)
   gives coefficient **exactly 1** at `w = 1` for `x_λ`; what remains is carrying it through the
   two `T_{d(·)}` conjugations.
3. **`supp_le`** — the off-diagonal support is bounded by `lead` in the dominance order. **This is
   the real remaining work**, and the only one with no `q = 1` shortcut, because it is where `q`
   actually enters: the `rsFun` down-branch contributes `(q−1)T_v + qT_{vs}` rather than a single
   term, so the support argument is genuinely `q`-deformed.

Then `Triangular.linearIndependent` gives independence, and `murphyIndex_card` (#6239) upgrades it
to a basis — **spanning and Garnir straightening never enter**.

### Correcting my own framing from #6281

#6281 called the whole thing "a port ... a real tranche, not a session's tail", citing
`SpechtStandardBasisCore`'s 170 KB. That size is mostly the **spanning** half (Garnir straightening)
plus the generic levers — and `murphyIndex_card` makes spanning unnecessary while the levers are
reusable as-is. So the estimate was too pessimistic, in a way that would have discouraged the next
agent from starting. The honest scope is: **one new definition (`lead`), two transferable proofs,
and one genuinely new `q`-deformed support argument.**


### Refinement to the above — `lead` has a missing prerequisite, and a possible way around it

The note above calls `lead` "the one genuinely new object" and leaves it at that. Measured, it is
**harder than that reads**, and the reason is worth stating before someone starts.

**Murphy's canonical leading term is `d(s)⁻¹ · w_λ · d(t)`, where `w_λ` is the LONGEST ELEMENT of
the Young subgroup — and no longest-element construction exists here or in Mathlib.**

Verified against a positive control so the absence is a measurement, not a failed grep:

| symbol | oleans in the pinned Mathlib |
|---|---|
| `CoxeterSystem` | 3 |
| `wordProd` | 3 |
| `IsReduced` | 58 |
| **`longestElement`** | **0** |
| **`longest_element`** | **0** |

And nothing in `QOU/` constructs one. The three corpus hits that look like candidates are not:
`DeltaLambdaSignRule.sgnLongest` is the **sign** `(-1)^{C(k,2)}` (a formula, no group element),
`GZThirdKnotRankGrading.w0Multiplicities` is a literal `[2,1,0]`, and
`TwoRowRootsAndAugmentation.trLongest` is a trace polynomial `z(hz+1)`. Names containing "longest"
are not longest elements.

**But `Triangular` is weaker than Murphy's canonical statement, and that is the opening.** Its three
fields ask only for *some* injective `lead` with a unit diagonal and support bounded above — not for
*the* leading term of the classical theory. So there are two routes, and the second may skip the
missing prerequisite entirely:

* **(a) Canonical.** Construct `w_λ` (longest element of a Young subgroup, by length maximisation
  over a `Fintype`), then `lead (s,t) := d(s)⁻¹ w_λ d(t)`. This is the textbook object and it makes
  `supp_le` the classical argument — but the construction is a genuine new prerequisite, plausibly
  Mathlib-upstreamable in its own right.
* **(b) Opportunistic.** Pick any `lead` making the three fields provable. The order on
  `Equiv.Perm (Fin (n+1))` is itself free — `exists_linearOrder_of_partialOrder` accepts **any**
  partial order — so `lead` and the order can be chosen together to fit the proof rather than the
  tradition.

**I have not established that (b) works**, and it may not: the freedom in the order is real, but
`lead_inj` still has to hold across all tableau pairs, which is what forces something canonical in
the classical treatment. Recording it as a route to *test*, not a route that works.

Net effect on the scope stated above: `lead` is not a one-liner, and the "three field proofs" figure
should be read as **three field proofs plus either a longest-element construction or a demonstration
that (b) avoids one.**

---

## 🛑 2026-08-30 — the candidate `lead` is REFUTED. Measured before formalising.

The entry above sets up `lead(λ,s,t) = d(s)⁻¹ · w_λ · d(t)` as the leading-permutation map for
(C1)'s triangularity, and calls `lead_inj` "the hard field". It is worse than hard: **as defined it
is FALSE**, and it fails for a structural reason.

Probe: [`computations/hecke/murphy_lead_injectivity_probe.py`](../computations/hecke/murphy_lead_injectivity_probe.py).
Full enumeration, exact integer arithmetic, no sampling and no tolerance.

### The measurement

| `n+1` | pairs `(s,t)` over all λ | distinct `lead` values | collisions |
|---|---|---|---|
| 3 | 6 | 5 | **1** |
| 4 | 24 | 17 | **7** |
| 5 | 120 | 54 | **66** |

The pair count is exactly `m!` — as `murphyIndex_card` proves — so the deficit is pure degeneracy,
and it **worsens with rank** (1/6 → 7/24 → 66/120). Not a small-rank artifact.

### The structural cause, and why this is a scope-(b) exclusion for the SHAPE

`λ ↦ w_λ` is **itself not injective**, at every rank tested:

| `m` | partitions | distinct `w_λ` | collisions |
|---|---|---|---|
| 3 | 3 | 2 | `w_(3) = w_(2,1) = (2 1 0)` |
| 4 | 5 | 4 | `w_(3,1) = w_(2,1,1)` |
| 5 | 7 | 5 | `w_(5) = w_(3,2)`, `w_(3,1,1) = w_(2,1,1,1)` |
| 6 | 11 | 9 | `w_(3,3) = w_(2,2,1,1)`, `w_(3,1,1,1) = w_(2,1,1,1,1)` |

Combined with a **proved** Lean lemma — `dOf_colSuperstandard : d(t^λ) = 1` (#6283) — this gives a
two-line structural argument, not merely an enumeration:

1. `d(t^λ) = 1` (Lean, proved).
2. Hence `lead(λ, t^λ, t^λ) = w_λ`.
3. `λ ↦ w_λ` is not injective (measured, every rank 3–6).
4. So `lead(λ, t^λ, t^λ) = lead(μ, t^μ, t^μ)` for `λ ≠ μ` sharing a longest element. ∎

The reference tableau always exists, so the witness is always available. **Any `lead` of this shape
fails**, at every rank where two partitions share a longest element.

### Scoping, per AGENTS.md

* **(b) structural exclusion, invariant cited** — for the *shape* `d(s)⁻¹ w_λ d(t)`. The invariant
  is `dOf_colSuperstandard` plus non-injectivity of `λ ↦ w_λ`.
* **(a) scope-limited** — for `lead_inj` in general. `Triangular` asks only for *some* injective
  `lead`, and this does **not** exclude other constructions. It excludes the textbook-shaped one.

### What this costs and saves

It **invalidates the plan in the two entries above.** #6293 said "three field proofs plus a
longest-element construction"; the longest-element construction (landed on #6297) is real and
reusable, but the `lead` it was meant to feed does not work. `supp_le` was never the blocker —
`lead_inj` was, and the obvious `lead` is false.

Saved: a formalisation attempt against a false statement. The probe cost minutes; `lead_inj` would
have cost a tranche and could not have closed.

### What the next agent should do

Do **not** attempt `lead_inj` for this `lead`. Either:

* find a `lead` that separates partitions — the collisions are all *cross-λ*, so the map needs to
  see λ beyond `w_λ` (the obvious repair: pair `w_λ` with λ itself, i.e. order `MurphyIndex` by
  dominance on λ first and permutation second, which is legitimate since
  `exists_linearOrder_of_partialOrder` accepts any partial order); or
* abandon single-`lead` triangularity for the cell-module **filtration** formulation, which is how
  Murphy's theory actually stratifies by dominance.

The first is worth probing before formalising — and the probe now exists to test it.


### …and the repair is RSK, which the corpus already has. `lead_inj` is FREE.

The refutation above says the collisions are cross-λ, so `lead` must see λ. My first repair idea —
*"order `MurphyIndex` by dominance on λ first, permutation second"* — **cannot work**, and checking
why is what found the real answer.

**`Triangular`'s `α` is forced.** Its field is `v : ι → (α →₀ R)`, so `α` is the index type of the
*coordinate vectors* — for us the `T_w` basis index, `Equiv.Perm (Fin (n+1))`. `lead` therefore
**must** land in permutations and cannot carry λ alongside.

That looks like a dead end, and is the opposite:

> `Nat.card (MurphyIndex m) = m!` (`murphyIndex_card`, #6239) and `|S_m| = m!`.
> So for `lead : MurphyIndex m → S_m`, **injective ⟺ bijective.**

And the canonical bijection between permutations and same-shape SYT pairs is **Robinson–Schensted**
— which is already here, sorry-free:

```
QOU.Mathlib.Schensted.rskEquiv (n : ℕ) :
  Equiv.Perm (Fin n) ≃ { X : Σ μ : YoungDiagram, SYT μ × SYT μ // X.fst.cells.card = n }
```

`#print axioms` → `propext / Classical.choice / Quot.sound`, no `sorryAx`. Built in-repo precisely
because the pinned Mathlib has no RSK, and already load-bearing: it is what proves
`rskBurnsideHolds`, which is what `murphyIndex_card` rests on.

**So `lead := (rskEquiv m).symm` is injective for free — it is an `Equiv`.** The hard field of
`Triangular` is not hard; it was only hard for the wrong candidate.

This also explains the refutation cleanly: `d(s)⁻¹ w_λ d(t)` was never going to be a bijection,
because `λ ↦ w_λ` already collapses partitions before the `d`'s are applied.

### One bookkeeping gap, stated so it is not mistaken for zero work

`MurphyIndex n` (mine, #6239) is `Σ p : Nat.Partition n, SYT(partitionShape p)²`; `rskEquiv`'s
codomain is a **subtype over `YoungDiagram`** cut by `cells.card = n`. Equivalent, not definitionally
equal. The bridge is `partitionEquivYoungIndex` (`SpechtClassification`) plus a `Sigma`/subtype
shuffle — real but mechanical.

### Revised state of (C1)

| field | status |
|---|---|
| `lead_inj` | **free**, via `rskEquiv` (modulo the index bridge above) |
| `diag_unit` | `repr_murphySum_one_of_subgroup` (#6285) gives coefficient 1; carry through the two `T_{d(·)}` conjugations |
| `supp_le` | **the genuine remaining content** — that the RSK-leading permutation dominates the support of `m_{st}`. This is essentially Murphy's theorem, and it is where `q` enters via the `rsFun` down-branch |

So `supp_le` is the last substantive step after all — but for the **RSK** `lead`, not the `w_λ` one,
and with `lead_inj` no longer in front of it.

**Note for whoever picks this up:** #6297 (the maximal-length element) is now **unused by this
route**. It was built for the refuted `lead`. It is correct, sorry-free and plausibly
Mathlib-upstreamable on its own, but do not assume the (C1) proof needs it.


## 2026-08-31 — supp_le is UNREACHABLE, and the Triangular route is retired (session hecke-murphy-index-bridge)

**Index bridge: DONE.** `murphyIndexEquivRSKCodomain` + `murphyIndexEquivPerm : MurphyIndex n ≃
Equiv.Perm (Fin n)` + `lead` + `lead_injective`, all sorry-free. The composition was already
inside `SchenstedRSKBurnside.card_pairs_eq_sum`'s proof, kept only as a shadow on `Nat.card`;
lifting it to the `Equiv` was assembly. **`lead_inj` is discharged** — `Equiv.injective`.

**supp_le: REFUTED, and not only for RSK.** `computations/hecke/murphy_supp_rsk_probe.py`
(exact integer arithmetic, complete at n=3,4,5) establishes two things:

1. RSK is not even a legal lead — `diag_unit` needs `lead x ∈ supp (m x)`, true for only
   1/6, 3/24, 11/120 of indices (3/6, 9/24, 23/120 with the other (P,Q) orientation).
   Hand-checkable witness: n=3, λ=(2,1), s=t=t^λ ⇒ d(s)=d(t)=1 ⇒ m = x_λ = T_1 + T_{s₁},
   support {1, s₁}; RSK⁻¹(s,t) = s₂ is not in it.
2. NO bijective lead works, for ANY linear order. The order-maximum M must lie in exactly one
   support (else injectivity fails), so peeling M+its index is forced; a Triangular structure
   exists iff the peel never stalls. At n=3 it stalls at once — all six permutations lie in
   ≥2 of the six supports (multiplicities 4,2,4,2,2,2), because x_{(3)} = Σ_{w∈S₃} T_w already
   has full support. Stalls after 1/24 at n=4, 5/120 at n=5.

Scope-(b) structural exclusion of THIS LEVER on THIS PAIR OF BASES — cited invariant is the
peeling argument, n=3 exhaustive not sampled. Says nothing against the Murphy basis (a theorem)
or against `Triangular` (which the Specht standard basis still runs on).

**Replacement route, from the corpus's own library.** `library/hecke-alg/` (Mathas, Thm 3.20)
proves the Murphy basis by **spanning + rank**, no triangularity: M spans, H is free of rank n!,
|M| = Σ_λ (f^λ)² = n! by RSK, done. Every ingredient but spanning is sorry-free here — and the
RSK ingredient is the same bijection that gave lead_inj.

**Landed sorry-free this session** (all `[propext, Classical.choice, Quot.sound]`):
`murphyFamily` (the m_{st} indexed by MurphyIndex (n+1); the SYT-type bridge it needed,
`NumSYTBridge.toBraidKnotSYT`, was already in the corpus — eighth such instance this arc),
`instFintypeMurphyIndex`, `murphyIndex_fintypeCard`, `basisOfSpanning`,
`murphyBasisOfSpanning`, `murphyFamily_linearIndependent`.

**next**: Mathas Lemma 3.9 + 3.14 — spanning — is now the SINGLE open input to (C1).
Audit: docs/audits/2026-08-31-murphy-basis-triangular-lever-refuted.md


### 2026-08-31 (cont.) — the right-handed structure constants, x_λ two-sided

`σ_mul_Tw` only goes one way, and the handedness is inverted: left multiplication by σ_i in
the algebra is RIGHT multiplication by s_i on the permutation. So Murphy's `T_{d(t)}` factor
had no lemma at all. Built the mirror, sorry-free, all from what was already on main:

- `Tw_sw` — `T_{s_i} = σ_i` (reproved locally; the corpus copy is in TwGramRankOne, whose
  Gram cone this file has no use for)
- `Tw_mul_σ_of_length_add` — ascending case, ONE LINE from `Tw_mul_Tw` (whose convention
  already reverses the order: `T_v · T_w = T_{wv}`)
- `Tw_mul_σ_of_length_sub` — descending case, from the ascending one + `σ_quadratic`
- `simple_eq_sw` — `(permCoxeterSystem n).simple i = sw i`, via `toPerm_simple`
- `sw_length_dichotomy` — from Mathlib `length_simple_mul` + `length_simple`; this is what
  makes the pair lemma UNCONDITIONAL, matching its left twin (whose dichotomy came free
  from the concrete descent test)
- `Tw_mul_σ_pair` / `Tw_mul_σ_pair'` — the right-handed q-eigenvector pair
- `murphySum_mul_σ` — `x_S · σ_i = q·x_S` for S closed under LEFT mult by s_i
- `murphySum_mul_σ_subgroup` — so `x_λ` is a **two-sided** q-eigenvector for every
  generator of its Young subgroup. That is what Mathas uses throughout Lemma 3.9/3.12.

All nine `[propext, Classical.choice, Quot.sound]`; downstream HeckeMurphyYoung re-verified
exit 0. These three `Tw_mul_σ_*` belong upstream in `QOU.Hecke.TwMul` beside their left
twins — left here because that file sits deep in the Hecke cluster and this is the only
consumer so far.

**next**: Mathas Lemma 3.13 — the Hecke Garnir decomposition `t = g·w` with
`ℓ(d(t)) = ℓ(d(g)) + ℓ(w)` — then Lemma 3.14's dominance induction. This is the q-analogue
of `standardPolytabloid_straightening`, which the corpus already proved sorry-free on the
`colWordNum` measure for the q=1 side; that proof is the template. Multi-session.


### 2026-08-31 — 🛑 TWO CORRECTIONS, one of them a defect in `murphyM` on main

**(1) My own supp_le probe had the WRONG HANDEDNESS.** The first run computed
`m_st = T_{d(s)^-1} x T_{d(t)}` — inverting on the LEFT only. That family is NOT a basis
(rank 19/24 at n=4), so its supports were of the wrong object. A sweep of all 16
combinations (reference tableau x d-direction x which side inverted) shows exactly 4 are
full rank at n=4, and they are precisely those inverting the two d-factors on OPPOSITE
sides. Which side carries it depends on d's own direction, so Murphy's
`T_{d(s)}^* x_λ T_{d(t)}` is the same convention read with the other d; what is
convention-independent is the opposite-side inversion.

**The refutation SURVIVES and is stronger.** The n=3 support table — the hand-checkable
witness — is byte-identical under both conventions (they first differ at n=4). Corrected
numbers: peel stalls at 0/6, **0/24**, **0/120** (was 0, 1, 5); `diag_unit` for RSK
1/6, **1/24**, **1/120** (was 1, 3, 11), and 3/6, 9/24, **29/120** for the other
orientation. Only those figures were wrong.

**(2) `murphyM` ON MAIN IS NOT MURPHY'S ELEMENT AND CANNOT SPAN.** It sums over
`youngSubgroup n h t = Specht.rowStab t` — the SECOND TABLEAU's own row stabiliser, a
different conjugate subgroup per t. Murphy's `x_λ` is one FIXED subgroup (the reference
tableau's row stabiliser) for every pair of that shape. Exact rank at q=7:

  n     fixed x_λ [Murphy]     rowStab t [corpus murphyM]
  3     6/6  FULL              5/6
  4     24/24 FULL             23/24 (row ref) / 21/24 (col ref)
  5     120/120 FULL           117/120 (row ref) / 112/120 (col ref)

Full rank in EVERY fixed-x cell, deficient in EVERY rowStab-t cell, under both reference
tableaux and all handedness variants. Note the axis I suspected first — colSuperstandard
(column-major) vs Murphy's row-superstandard t^λ — is a RED HERRING: both are full rank.
The subgroup is the defect.

**Consequence.** `basisOfSpanning` is stated for an ARBITRARY family and is unaffected —
that genericity was deliberate and is what saves the work. `murphyFamily`,
`murphyBasisOfSpanning`, `murphyFamily_linearIndependent` remain TRUE but their hypothesis
is now measured UNSATISFIABLE (conditional-proved ≠ premise-established). Re-documented in
place rather than deleted, so the shape the corrected family slots into survives.

**Lesson, recorded because it generalises:** a probe measuring a rich structural property
(supports, orders, peelings) says nothing if the object is wrong, and it will NOT announce
that — it returns a well-formed table either way. A RANK TEST is seconds of exact
arithmetic and caught both errors, the second AFTER the Lean built on it was written,
verified sorry-free, committed and described in a PR body as Murphy's family. Sorry-free
and wrong are entirely compatible. Guard is now `run_rank_guard` in the probe.

**next**: fix `murphyM` to sum over the reference tableau's row stabiliser, then re-point
`murphyFamily` at it and re-run the rank guard as the acceptance test. THEN spanning.


### 2026-08-31 — murphyM FIXED; and the anchor lemma is the one that couldn't see the bug

`murphyM` now sums over the reference tableau's row stabiliser
(`youngSubgroup n h (colSuperstandard μ)`) instead of `rowStab t`. Contained change: that
file was the only consumer in the whole Lean tree. lean-direct exit 0; all seven touched
declarations `[propext, Classical.choice, Quot.sound]`. Acceptance test is `run_rank_guard`:
6/6, 24/24, 120/120 (was 5/6, 23/24, 117/120).

**That is evidence, not proof.** Full rank at n=3,4,5 says the spanning hypothesis is no
longer measured UNSATISFIABLE; it does not say Mathas Lemma 3.14 holds. `murphyBasisOfSpanning`
and `murphyFamily_linearIndependent` still prove only `spans -> basis` / `spans -> independent`.

**Worth flagging so nobody "fixes" a correct lemma:** `murphyM_colSuperstandard_diag`
(`m_{t^λ t^λ} = x_λ`, the sibling's anchor from claude/hecke-c1-triangular-2026-08-30) is
stated at `t = colSuperstandard μ` — exactly where the defective and correct definitions
COINCIDE. It was right throughout, and it is precisely the case that cannot detect the defect.
A base case that is invariant under the bug is not evidence the definition is sound.

**next**: spanning (Mathas Lemma 3.9 + 3.14) — now genuinely the single open input to (C1).
The q=1 template is the corpus's own sorry-free `standardPolytabloid_straightening` on the
`colWordNum` measure.


### 2026-08-31 — CORRECTING my own scoping of "spanning"

I have twice written that spanning is "Mathas Lemma 3.9 + 3.14". Having now read the actual
statements rather than the sentence that cites them, that is imprecise in a way that matters
for planning.

**Lemma 3.9 is NOT the spanning lemma.** It says: for a COMPOSITION μ with λ the partition
obtained by reordering μ's parts, and s,t row-standard μ-tableaux, `m_st` is an R-combination
of `m_uv` with u,v row-standard λ-tableaux. It moves compositions to partitions. Useful, not
the spanning step.

**Lemma 3.14 is the straightening**: for s,t ROW-standard λ-tableaux, `m_st` is a combination
of `m_uv` with u,v STANDARD ν-tableaux, where either ν ⊳ λ, or ν = λ and u ⊵ s, v ⊵ t. It runs
through Lemma 3.13 (the Garnir decomposition t = g·w with ℓ(d(t)) = ℓ(d(g)) + ℓ(w)) and
Lemma 3.12.

**The actual spanning chain is three steps, and step 1 is already ours:**

1. `{T_w}` spans H — the corpus HAS this (`QOU.Hecke.TwSpanning`, `basisTwOfField`).
2. **Every `T_w` IS a Murphy element of the one-column shape.** For μ = (1^n) the Young
   subgroup is trivial, so `x_μ = 1` and `m_st = T_{d(s)^-1} T_{d(t)}`; every filling of a
   single column is row-standard, so there are n! of them and `d(t)` ranges over all of S_n.
   Taking s = t^μ gives `m = T_{d(t)}`, i.e. every `T_w`. Hence the ROW-STANDARD Murphy family
   spans, immediately, from step 1.
3. Lemma 3.14 straightens row-standard to standard, moving up in dominance. (1^n) is the
   dominance-minimum, so everything is reachable.

**Structural consequence for the Lean, and it is not a detail.** Steps 2-3 are about the
family indexed by ROW-STANDARD pairs — n! per shape, not (f^λ)². `MurphyIndex` and
`murphyFamily` are over STANDARD pairs only. So spanning cannot even be STATED for
`murphyFamily` directly: it needs a row-standard-indexed family first, which does not exist in
the corpus. For the one-column shape the standard family has exactly ONE element while the
row-standard family has n!, so the gap is the whole of the argument, not a technicality.

**next**, in order: (a) a row-standard tableau type + the row-standard-indexed family;
(b) step 2, `x_{(1^n)} = 1` and hence every `T_w` is a one-column Murphy element — small,
self-contained, and it reduces spanning to straightening alone; (c) Lemma 3.13/3.14, the hard
core, with the corpus's own sorry-free `standardPolytabloid_straightening` on the `colWordNum`
measure as the q=1 template.


### 2026-08-31 — step 2 landed; spanning now reduces to straightening alone

`murphySum_singleton_one` (`x_{(1^n)} = 1`) and `span_murphySum_one_conjugates_eq_top` (the
two-sided conjugates of that 1 span H). Both sorry-free, lean-direct exit 0,
`[propext, Classical.choice, Quot.sound]`.

**It is a CHEAP result and I want that on record rather than dressed up**: it is `x = 1` plus
the fact that the `T_w` are a basis. What it buys is not difficulty but a pin — with step 1
(`basisTwOfField`) and step 2 both in hand, the ENTIRE spanning input to `basisOfSpanning` is
Mathas Lemma 3.14's straightening. Nothing else is outstanding on that leg.

Stated over the conjugating PAIR rather than over tableaux, deliberately: the row-standard
tableau type does not exist in the corpus, and this is the algebraic content, which does not
have to wait for the indexing.

**next** (the honest remaining cost, in order):
(a) a row-standard tableau type + a row-standard-indexed Murphy family — without it Lemma 3.14
    cannot be STATED, since it quantifies over n! pairs per shape and MurphyIndex has (f^λ)²;
(b) Lemma 3.13, the Garnir decomposition `t = g·w` with `ℓ(d(t)) = ℓ(d(g)) + ℓ(w)`;
(c) Lemma 3.14's dominance induction. The q=1 template is the corpus's own sorry-free
    `standardPolytabloid_straightening` on the `colWordNum` measure — same argument, and it
    already carries the hard measure-descent work.


### 2026-08-31 — the row-standard index set exists (step (a) of the spanning blocker)

`QOU/BraidKnot/RowStandardTableau.lean`, sorry-free:
`IsRowStandard`, `RowStandardTab` (subtype), `Decidable`/`Fintype` instances,
`isRowStandard_of_no_second_column`, `equivTableauOfNoSecondColumn`,
`card_eq_factorial_of_no_second_column`.

**Design note worth keeping.** It is a PREDICATE on `Specht.Tableau μ`, not a new structure.
`Tableau μ = Fin (nOf μ) ≃ μ.cells` is already the arbitrary bijective filling and is what
`dOf`/`dAt`/`murphyM` consume, so row-standardness is a condition on it and a row-standard
tableau is a subtype — nothing downstream needs re-plumbing. (`BraidKnot.StandardYoungTableau`
is a separate `entry`-based structure carrying both `row_strict` and `col_strict`; row-standard
is that minus the column half, but expressed on the type the Hecke side already speaks.)

`card_eq_factorial_of_no_second_column` makes the gap quantitative and Lean-checked: on a
one-column shape there are `n!` row-standard tableaux against exactly ONE standard tableau.
That is why Lemma 3.14 cannot be stated against `MurphyIndex`, and why
`span_murphySum_one_conjugates_eq_top` had to be phrased over conjugating permutations.

Note the hypothesis is `(0,1) ∉ μ` — YoungDiagram is closed under up-left, so "no cell in
column 1" IS "every row has length ≤ 1", and the row-standard condition is then vacuous.

**next**: (b) Lemma 3.13, the Garnir decomposition `t = g·w` with `ℓ(d(t)) = ℓ(d(g)) + ℓ(w)`;
then (c) 3.14's dominance induction. Also still open and cheap-ish: `IsRowStandard` for the
image of a standard tableau under `sytToTableau` (the forgetful direction), which the
straightening's target side will want.


### 2026-08-31 — the forgetful map Std -> RowStd, and the lemma it needed

`entry_lt_entry_of_lt` and `isRowStandard_sytToTableau`, both sorry-free.

**It was not immediate, and the reason is worth recording.**
`StandardYoungTableau.row_strict` compares only ADJACENT cells (`entry i j < entry i (j+1)`),
while row-standardness compares arbitrary pairs within a row. The corpus had no transitive form
and Mathlib has none for this type, so `entry_lt_entry_of_lt` proves it by induction on the
right-hand column, using the diagram's up-left closure to know the intermediate cells exist.
That transitive step IS the content; the bridging lemma on top of it is bookkeeping
(`sytToTableau` is the inverse of `cellLabel`, and `cellLabel` is literally `T.entry`).

`entry_lt_entry_of_lt` is about `StandardYoungTableau` alone and BELONGS UPSTREAM in
`QOU.BraidKnot.StandardYoungTableau`; kept in RowStandardTableau.lean to hold the change to one
file, same call as the `Tw_mul_σ_*` lemmas in HeckeMurphyYoung. Both are flagged in their
docstrings as misplaced-on-purpose so a later tidy-up knows where they go.

**next**: Mathas Lemma 3.13 — the Garnir decomposition `t = g·w` with
`ℓ(d(t)) = ℓ(d(g)) + ℓ(w)` for a row-standard non-standard `t` — then 3.14's dominance
induction. Both index sets and the map between them now exist, so 3.14 is finally STATABLE,
which it was not before this session.


### 2026-08-31 — IsStandard on the filling type; and a RECONNAISSANCE of the q=1 Garnir apparatus

Landed sorry-free: `IsColStandard`, `IsStandard`, `entry_lt_entry_of_lt_row`,
`isColStandard_sytToTableau`, `isStandard_sytToTableau`, `IsStandard.isRowStandard`, plus
Decidable instances. All three of Lemma 3.14's index sets — row-standard source, standard
target, and the map between them — are now on ONE type, `Specht.Tableau μ`. **3.14 has nothing
missing from its statement any more.**

**Reconnaissance of what the q=1 side already provides (ninth reuse find this arc), and — more
usefully — what it does NOT.**

Already built, all on `Specht.Tableau μ`, the same type: `colWordNum` / `cmajSig` (the validated
straightening measure), `garnirA` / `garnirB` (the label sets), `garnirG` / `garnirH` (the
permutation sets), `garnirGSub` / `garnirHSub` (as subgroups), `garnir_full_annihilation`,
`colStandard_of_colWordMin`, `exists_row_descent_of_colWordMin`, `exists_descent_of_not_mem_range`.

**But the reuse is LESS DIRECT than the names suggest, and this is the part worth recording.**
The descent lemmas are phrased against POLYTABLOID MEMBERSHIP
(`Specht.polytabloid t ∉ Set.range standardPolytabloid`), not against tableau standardness, so
they are Specht-module statements rather than combinatorial ones. `IsStandard` above is what
lets that be restated combinatorially, but the restatement is work, not a rename.

**Three genuinely new pieces remain for Mathas 3.13, and #2 is why his proof differs from
Sagan's at all:**
1. the Garnir TABLEAU `g` (the corpus has Garnir SETS and SUBGROUPS, not the tableau) and the
   factorisation `t = g·w`;
2. **the length additivity `ℓ(d(t)) = ℓ(d(g)) + ℓ(w)`** — a Coxeter-length statement, and the
   q=1 side never tracks lengths at all, so there is nothing to transport;
3. the q-analogue of Garnir annihilation: at q=1 the relation is `sign`-weighted
   (`garnir_full_annihilation`), in `H_n(q)` it is weighted by the Hecke relation.

**next**: (1) and (2) above. (2) is the load-bearing one and is where I would start, since it
is the piece with no q=1 antecedent and therefore the one most likely to reveal that the route
needs rethinking.

### 2026-08-31 — Lemma 3.13's length additivity PROBED, and it is stronger than Mathas states it

`computations/hecke/murphy_garnir_length_additivity_probe.py` — exact integer arithmetic
(tableaux as tuples, permutations as tuples, Coxeter length as inversion count; no float).

Applied the session's own lesson: this is the one ingredient with NO q=1 antecedent (Sagan's
Garnir straightening never tracks Coxeter lengths), so it is the piece most likely to reveal
that the route needs rethinking — measure it before formalising.

**Result: it holds, on every case, and the FIRST descent node always works.**

  n     row-standard non-standard t     SOME node works     FIRST node works
  3     6                               6/6                 6/6
  4     37                              37/37               37/37
  5     220                             220/220             220/220
  6     1526                            1526/1526           1526/1526

**Mathas states EXISTENCE of a descent node; the probe says the first one always suffices.**
That is a constructive strengthening and it matters for the Lean: no search over nodes and no
induction on the node choice — take the first descent, done. Mathas' own proof handles the
non-Garnir case by induction ("otherwise there exists s in S such that t' = ts is row standard
... by induction"); if the first-node form holds in general, that induction collapses.

The probe also asserts `d(t) = w . d(g)` on every case (1789 of them), which confirms the
composition convention rather than leaving it inferred — the exact class of error that cost
this session a wrong-handed supp_le probe earlier.

The Garnir-tableau construction is verified against Mathas' own three worked examples for
lambda = (3,3) (`g_11`, `g_12`, `g_13`) BEFORE any measurement runs, and the script refuses to
proceed if they mismatch. Same discipline as the rank guard: check the object before measuring
a property of it.

**n <= 6 is evidence, not proof** — the claim is over all n. But it de-risks the hardest
remaining piece and tells the formaliser exactly what to prove.

**next**: formalise `l(d(t)) = l(d(g)) + l(w)` at the first descent node. Then the Garnir
tableau itself as a Lean definition, then 3.14's dominance induction.

## Length additivity — CLOSED (PR #6444, 2026-09-03)

`length_mul_eq_add_iff` is proved sorry-free in
`QOU/Hecke/LengthAdditive.lean`:

    ℓ(u * v) = ℓ(u) + ℓ(v)  ↔  invSet v ⊆ invSet (u * v)

i.e. length is additive exactly when `u` undoes none of `v`'s inversions.
Via the counting identity, also proved:

    ℓ(u) + ℓ(v) = ℓ(u * v) + 2 · #{p ∈ Inv v : p ∉ Inv (u * v)}

**STABLE — this is a Mathlib gap, not a Murphy-only stepping stone.** Mathlib
has subadditivity (`CoxeterSystem.length_mul_le`) and one-sided bounds, but no
equality criterion (checked in `GroupTheory/Coxeter/Length.lean`).
`finPairsLT` does not substitute: sigma-typed scaffolding for `sign`, carries
a parity not a count. So the lemma is reusable well beyond this arc.

**STABLE — the enabling fact is `length_eq_invCount`** (`QOU.Hecke.PermLength`,
already on main): Coxeter length IS the inversion count. That is what converts
the obligation from Coxeter theory into combinatorics, and Mathlib lacks it too.
Any future length-additivity work should start there rather than from `length`.

**TRAP — `set` on a membership predicate breaks `rw`.** Binding
`a := fun p => p ∈ invSet v` with `set ... with ha` and then `rw [ha]` fails
with *"motive is not type correct"*: the `Finset.filter` carries a
`DecidablePred` instance depending on the abstracted predicate. Symptom is an
`Application type mismatch` naming `decidableMem`. Fix used: never abstract the
predicate — work with the difference sets `D₁ := (invSet v).filter (· ∉ invSet (u*v))`
directly, prove the symmetric-difference decomposition by `ext`, and finish with
`filter_card_add_filter_neg_card_eq_card` + `filter_mem_eq_inter` + `omega`.

**Verification** (CI is dispatch-only; the agent's own check is the gate):
`lean`-direct exit 0 on the new file and on `PermLength.lean`, zero warnings;
`#print axioms` on all four new results shows only
[propext, Classical.choice, Quot.sound] — no sorryAx; zero `sorry` in the file.

Non-vacuity is committed in-file as `decide` guards rather than checked once:
the criterion is false for the collapsing `s₀ * s₀`, true for the reduced
`s₀ * s₁`, and the defect there is genuinely 2. Both sides of the iff occur.

## Mathas 3.13 length half COMPLETE (2026-09-04)

Four PRs, all merged, all sorry-free:

| PR | result |
|---|---|
| #6444 `a2edbcffb7` | `length_mul_eq_add_iff` — additivity iff no inversion undone (a Mathlib gap) |
| #6527 `fd7f900170` | `d(t)`, the tableau<->perm bijection, `refTab` closed form, the length bridge |
| #6557 `2c37ac54b1` | `g_{ij}` as an interval ROTATION, descent nodes, additivity AT a node |
| #6598 `5ff6492fac` | descent-node EXISTENCE; `exists_garnir_length_additive` composes both halves |

**Two findings that made it tractable, both from measuring BEFORE formalizing:**

1. **`g_{ij}` is a cyclic rotation of the label interval `[a,b]` by `j+1`**, not
   a placement procedure (108/108, all partitions n=3..7). A rotation is
   invertible by construction, so bijectivity was FREE — no surjectivity
   obligation, no sorting argument.
2. **Additivity holds at EVERY descent node**, not just the first (3685/3685
   over 1789 tableaux, n=3..6). So the theorem needs NO minimality hypothesis —
   stronger than Mathas states AND easier to prove. Mathas asks for 'some'; the
   prior corpus probe reported 'the first'; both understate it.

**STABLE — the criterion.** `length_mul_eq_add_iff` reduces additivity to
inversion containment, which unfolds (via the rotation's inversion set) to
`t(i,c) > t(i+1,c')` for c>=j, c'<=j, which row-standardness chains out of the
single descent inequality. That chain IS the proof.

**TRAP — omega holds `rowLen i + 1 - (j+1)` as ONE OPAQUE ATOM**, so
`rowPrefix_succ` never reaches the constraint set. Rewrite the Nat subtraction
first. Diagnosed with `trace_state`.

**TRAP — `set x := ...` hides the defining equation from omega/rw.** Hit twice
(#6557 `p.1 = rowPrefix i + c`; #6598 the pattern lemmas). Use an explicit
`obtain <c, hc> : exists c, ... = ... + c`, or helper lemmas over the patterns.

**TRAP — `subst h` FAILS when both sides are function applications** (e.g.
`colPattern t l = colPattern t l'`). Route the transport through a lemma whose
variable is a genuine variable; there subst fires.

## Next front OPENED: PR #6612 (parabolic pairing)

`HeckeCellular` names its own blocker: x_lambda for a general Young subgroup
needs the w <-> w.s_i pairing over `Perm (Fin (n+1))`, and says 'the blocker is
the combinatorics, not the algebra'. #6612 supplies that: `length_swap_dichotomy`
(exactly one of the pair is longer, by one), `mulSwap` as a fixed-point-free
involution, and the ascending/image split. x_lambda itself is NOT defined and the
eigenvector property is NOT proved.

## CORRECTION to my own #6614 (2026-09-04)

**I proved a Perm-specific specialization of lemmas Mathlib already has
generically, and described it as supplying the blocker. That overstated it.**

Mathlib carries `CoxeterSystem.length_mul_simple` (the two-branch length
dichotomy) and `length_mul_simple_ne` (the two are never equal), for ANY Coxeter
system. `QOU.Hecke.TwBasis.length_flip` — already on main, in the very file
defining `rsFun` — already packages them. So #6614's `length_swap_cases` and
`length_swap_ne` are specializations, not new results.

**What in #6614 survives as additive:** `mulSwap` as a named involution,
`mulSwap_ne` (fixed-point-freeness, proved directly rather than via lengths),
the ascending/image split, and `mulSwap_mem` (subgroup closure is free). Thin,
but not nothing. Nothing in it is WRONG — it compiles sorry-free — the defect is
in how I priced it.

**Root cause: I grepped the CORPUS for prior work and never grepped MATHLIB.**
The corpus-grep checklist has six paths and Mathlib is not one of them, because
it is normally reached through the Lean tooling — which was down this session
(lean-lsp CONNECT_TIMEOUT throughout, so no `leansearch`/`loogle`). A dead
search tool silently removed a whole search surface, and I did not notice its
absence. **Grep `.lake/packages/mathlib` directly when the LSP is down.**

## What is genuinely NOT in Mathlib — PR #6616

The pair identity, which is HeckeCellular's own sentence:

    rsFun_add_rsFun : rsFun i w + rsFun i (w * s_i)
                        = q . (single w 1 + single (w * s_i) 1)

Stated for an ARBITRARY Coxeter system. The dichotomy it rests on is Mathlib's;
the CONSEQUENCE — that the two branches collapse to q times the pair, with the
(q-1) and the 1 combining exactly — is not, and is the step a sum over a Young
subgroup is reorganised by. It holds over any CommRing: nothing divides by 2,
which the naive 'sum equals its own reindexing' argument would need.

## RETRACTED: PR #6626 and its follow-on were DUPLICATES (2026-09-04)

**Both `ParabolicSum.lean` and an unpushed `ParabolicEigen.lean` re-derived results
that have been on `main` since 2026-08-30.** Removed; #6626 closed.

What is already there, in `QOU/BraidKnot/HeckeMurphy.lean`, sorry-free (0 code
sorries; the 5 grep hits are the WORD in docstrings, a miscount a previous agent
already made and corrected in that same file's prose):

| I wrote | already on main | model |
|---|---|---|
| `rsFun_add_rsFun` | `σ_mul_Tw_pair` | mine free-module, theirs the algebra |
| `mul_simple_ne` | `mul_sw_ne` | — |
| `mul_simple_mul_simple` | `mul_sw_sw` | — |
| `Rs_parabolicSum` | `σ_mul_murphySum` | same `Finset.sum_involution` proof, line for line |
| `Rs_parabolicSum_subgroup` | `σ_mul_murphySum_subgroup` | — |
| — | `murphySum_mul_σ{,_subgroup}` | right action, which I did not even have |
| — | `HeckeMurphyYoung.σ_mul_murphySum_young` | the GENUINE `x_λ` on a tableau's row stabiliser |

Theirs is strictly stronger: stated in `IwahoriHecke K q n` rather than in the free
module `W →₀ R`, both-sided, and connected to an actual Young subgroup. The only
thing mine had that theirs does not is generality in the Coxeter system — which
nothing in the corpus consumes.

**Root cause: a STALE DOCSTRING, and my second miss of the same kind in one session.**
`HeckeCellular.lean`'s §"Toward the Murphy basis" said the pairing argument "is the
open work". It was superseded by `5f38f5286b` **the same day it was written**
(`a4e94c8b11`, both 2026-08-30) and never updated. I read it and built on it.

The corpus-grep checklist would have caught this — grepping `x_lambda|parabolicSum`
in `content/**/*.lean` is path 2 — and I DID run that grep. It returned
`HeckeCellular.parabolicSym` and I stopped there, because that was the file I had
already read and it matched the story I had. **A grep that confirms your prior is
where the checklist fails; the hit to chase is the one you did not expect.**
`murphySum` was one file away and I never searched for it under any name.

The `HeckeCellular` docstring is now corrected in place, pointing at `HeckeMurphy`,
so the next agent does not repeat this.

## WHERE THE ARC ACTUALLY STANDS

The length half of Mathas 3.13 (#6444, #6527, #6557, #6598) is **not** wasted — it is
input to the step that IS open. `HeckeMurphyYoung.lean` §9 names it exactly:

> spanning reduces to straightening alone ... **Lemma 3.14** straightens row-standard
> pairs to standard ones, moving up in dominance ... **the corpus has no row-standard
> tableau type.** That gap is the whole of step 3.

Steps 1 and 2 of spanning are done (`basisTwOfField`;
`span_murphySum_one_conjugates_eq_top`). `basisOfSpanning` /
`murphyBasisOfSpanning` take spanning as an explicit hypothesis, correctly labelled
"conditional-proved ≠ premise-established".

**Next, in order:**
1. A row-standard tableau **type** (`IsRowStandard` exists in `GarnirTableau.lean` as
   a predicate; the family Mathas indexes by needs the subtype + its `Fintype`).
2. The straightening step, using `exists_garnir_length_additive` (#6598): at a descent
   node the Garnir permutation's inversions sit inside `d(t)`'s, so
   `ℓ(g·d(t)) = ℓ(g) + ℓ(d(t))`, hence `T_g · T_{d(t)} = T_{g d(t)}` — which is the
   multiplicativity straightening runs on.
3. Dominance monotonicity, then discharge `basisOfSpanning`'s hypothesis.

- Round 76 (`lane-e667`): Formalized `qou-gmfz`, `qou-img9`, `qou-phir`, `qou-siin`, `qou-l25z` in `QOU.Foundations.TriangularBarInvolutionLengthTwoQuadraticDefectRightMultiplicationDichotomyRootParameterRescalingWritheHomomorphism` with 80-dps `mpmath` 2-commit witness stamp (`1d514d8cc14cab86cdbfe50f0bca4313a91a6db7` -> `8fbc40e0a853ba6aa21eab5cf4d1947155a2d115`, `scriptHash=b5b4b562fbd04cd73aa5a68e31eebc858e55abd805cb24915d3a249d657d689c`) in PR `litlfred/qou#8409` (`status: in-progress`).
