---
# qou-x64l
title: Retire the ASCII H4 basis — it is the subscript basis relabelled, and the permutation is explicit
status: in-progress
type: task
created_at: 2026-08-09T17:21:10Z
updated_at: 2026-08-10T02:55:00Z
---


The tree carries **two** 24-word normal-form bases for `H₄(q)`:

| | module | has | lacks |
|---|---|---|---|
| **ASCII** | `QOU/Machinery/MarkovTraceH4.lean` + `MarkovTraceH4Gram0..7` | `trM`, `gram_symm`, **`trM_cyclic`** (all sorry-free) | associativity, `Ring`, `Algebra` |
| **subscript** | `HeckeH4StabilizationRung` + `HeckeH4AlgebraLaws` | the presentation, `mulNF₄_assoc`, `H4A` `Ring`/`Algebra`, `wedderburn₄`, semisimplicity, the `HeckeAlgebra` + `IsHeckeOfFullRank` instances | **cyclicity** |

`HeckeH4AlgebraLaws` deliberately does not import `MarkovTraceH4`, so the two have
never been connected, and the only thing keeping the ASCII chain alive is that it
owns cyclicity.

## They are the same basis, relabelled

Checked by mapping each reduced word to its `S₄` element (`s_k` = adjacent
transposition):

* both word lists give **24 distinct** `S₄` elements, and **the same 24**;
* the index permutation ASCII → subscript is
  `[0,6,2,1,7,9,8,4,3,12,10,13,11,5,14,16,15,17,18,19,20,21,22,23]`;
* the trace weights agree exactly under it — `TRM[i] = TRM4[perm i]` for all `i`;
* only **6 of 24** words differ at all, and every difference is a single
  far-commutation swap `σ₂σ₀ ↔ σ₀σ₂`:

  | i | ASCII | subscript |
  |---|---|---|
  | 12 | `σ₁σ₂σ₀` | `σ₁σ₀σ₂` |
  | 16 | `σ₀σ₁σ₂σ₀` | `σ₀σ₁σ₀σ₂` |
  | 17 | `σ₁σ₂σ₀σ₁` | `σ₁σ₀σ₂σ₁` |
  | 20 | `σ₀σ₁σ₂σ₀σ₁` | `σ₀σ₁σ₀σ₂σ₁` |
  | 22 | `σ₁σ₂σ₀σ₁σ₀` | `σ₁σ₀σ₂σ₁σ₀` |
  | 23 | `σ₀σ₁σ₂σ₀σ₁σ₀` | `σ₀σ₁σ₀σ₂σ₁σ₀` |

  and `far_commute_σ₀σ₂` is proved, so those are equal *in the algebra*, not only
  as group elements.

Two earlier readings of this comparison were wrong and are recorded so nobody
repeats them: comparing the word *tuples* says the sets differ (they do — 6
entries — but the elements do not), and comparing the weight strings without
normalising whitespace says the multisets differ (the subscript `TRM4` literal is
multi-line, so its entries carry newlines).

## The task

1. Define the permutation `π : Fin 24 → Fin 24` above, prove it is a bijection,
   and prove the two bases correspond under it — the 6 differing words need
   `far_commute_σ₀σ₂`, the other 18 are `rfl`.
2. Transport `QOU.Machinery.H4.trM_cyclic` along `π` to give cyclicity for
   `trM4` on the subscript basis. **No second Gram closure.**
3. That unblocks `QOU.Hecke.MarkovTrace 4 q (H4A K (q − q⁻¹))` and a
   `MarkovTraceContext` at `n = 4` — the last open Hecke item below `n = 5`.
4. Then retire the ASCII chain: `MarkovTraceH4.lean` and `MarkovTraceH4Gram0..7`,
   ~6.5k generated lines. `QOU/Machinery/H4AsciiPresentation.lean` goes with it —
   it is the Hecke presentation on the ASCII actions, and its subscript-basis
   counterparts are already proved in `HeckeH4StabilizationRung`. (It replaced
   `QOU/Hecke/InstanceH4.lean`, retired in qou-ti7p; `H4BasisBridge` imports it
   for `mulσ_farcomm02`, so that import goes at the same time.)

## Why this is worth doing beyond tidiness

The ASCII Gram chain is **the tree's build pole**: eight chained modules, ~4.3 GB
peak, and the reason a full `lake build` takes ~55 minutes instead of ~5. Retiring
it after the transport removes that cost permanently, and removes a standing
drift hazard — two hand-maintained tables for the same algebra, which is the
defect class this whole audit keeps turning up.

## 2026-08-09 — `QOU/Machinery/H4BasisBridge.lean`: the correspondence is proved, one step short of cyclicity

Landed and axiom-clean:

| declaration | content |
|---|---|
| `piIdx`, `invIdx` | the index permutation, with both round-trips (`fin_cases`) |
| `phi`, `psi`, `psi_phi`, `phi_psi` | the relabelling and its inverse |
| `phi_mulσ0/1/2` | **`phi` intertwines all three generator actions** — depth 1 each |
| `phi_word_0 … _23` | **every word action corresponds** — by rewriting, no coordinate expansion; the 18 identical words close on the intertwiners alone, the 6 far-commutation swaps on one `rw [far_commute_σ₀σ₂]` each |
| `trM4_phi` | `trM4 z h (phi u) = trM z h u` |

That is the whole mathematical content of "the two bases are one basis": the
generator actions correspond, hence every word action does, and the traces agree.

## The one remaining step, and why it is stuck

`phi_mulNF : phi (mulNF h u v) = mulNF₄ h (phi u) (phi v)`, from which

```lean
theorem trM4_cyclic (z : R) (x y : Fin 24 → R) :
    trM4 z h (mulNF₄ h x y) = trM4 z h (mulNF₄ h y x) := by
  have hx : x = phi (psi x) := (phi_psi x).symm
  have hy : y = phi (psi y) := (phi_psi y).symm
  rw [hx, hy, ← phi_mulNF, ← phi_mulNF, trM4_phi, trM4_phi]
  exact trM_cyclic z h (psi x) (psi y)
```

**The obstacle is mechanical, not mathematical.** `mulNF` and `mulNF₄` are
literal 24-term sums over exactly the word actions the `phi_word_*` lemmas relate,
with coefficients matching because `(phi v) (piIdx i) = v i`. What fails is
getting `simp` to apply `← phi_word_*` to the unfolded `mulNF₄`: the unused-simp-args
linter reports **all 24 as unused**, so the rewrites never fire and `ring` is then
left with two sums it cannot match.

Tried and rejected:
* `phi` in the same `simp only` as the `←` rewrites — `phi` unfolds first and
  destroys the patterns;
* a two-pass split (`simp only [mulNF₄, ← phi_word_*]` then unfold) — the
  rewrites still do not fire.

Cheapest things to try next: drop `phi_word_0` from the set (it is the degenerate
`phi u = phi u` and may be poisoning it); use `conv` to target only the
right-hand side; or abandon `simp` for an explicit `calc`/`rw` chain over the
unfolded sum. The file carries this note inline so it is not rediscovered.

Nothing is retired yet — the ASCII chain stays until `trM4_cyclic` lands.

## 2026-08-09 (later) — third approach, third failure mode; stop guessing at `simp`

`mulσ_farcomm02` (far-commutation on the **ASCII** generators) is now proved in
`H4BasisBridge.lean` — it is needed regardless, and it was the fix implied by the
second failure. It does not close `phi_mulNF`.

Failure modes so far, all recorded in the file:

1. `phi` in the same `simp only` as `← phi_word_*` — `phi` unfolds first, patterns destroyed.
2. Two-pass split — the linter reports **all 24 `phi_word_*` unused**. `simp`
   rewrites innermost-first, so the single-generator rewrites collapse each
   composite step by step into the *subscript* word shape; for the 6 differing
   words that is not the ASCII word, so the longer lemmas never match.
3. Adding `mulσ_farcomm02` to normalise those 6 — still fails, and the RHS now
   comes out with **70 terms instead of 24**, with coefficients indexed by
   `invIdx j` rather than by literals. `simp` is mangling the coefficient vector,
   not just failing to rewrite.

**Recommendation: abandon the unfold-and-`ring` route.** Three attempts have each
broken somewhere different, which is the signal that the shape is wrong rather
than the tactic call. The tree already has the structured accessors —
`mulNF₄_e_right`, `mulNF₄_expand_right`, `mulNF₄_sum_left/right`,
`basis_decomp₄` — and `MarkovTraceH4` has the ASCII counterparts. Express both
products as a `Finset.sum` over the basis and reindex along `piIdx` with
`Finset.sum_nbij` / `Equiv.sum_comp`, so the 24 terms are never written out and
`simp` never sees a 70-term polynomial. The `phi_word_*` lemmas are exactly the
per-term input such a proof needs.

---

## 2026-08-09 — `phi_mulNF` and `trM4_cyclic` are proved

Steps 1–2 of the plan above are done, sorry-free and axiom-clean.

### What closed it: reindex the sum, do not unfold it

The three recorded `simp` failures share a single cause, which was not obvious
until the fourth attempt was framed differently. `mulNF` and `mulNF₄` are both
24-term sums over word actions, but the terms correspond **under `piIdx`**, not
position by position. Any tactic that unfolds both sides and matches term
against term therefore has to permute 24 terms *by rewriting* — which `simp`
will not do, and which `ring` cannot see through the generator actions. That is
why attempt 3 produced 70 terms instead of 24: `simp` was not failing to
rewrite, it was distributing across a mismatched pairing.

Reindexing does it in one step, and never writes the terms out:

```lean
theorem phi_mulNF (u v : Fin 24 → R) :
    phi (mulNF h u v) = mulNF₄ h (phi u) (phi v) := by
  rw [mulNF_expand_right, mulNF₄_expand_right, phi_sum]
  have step : ∀ k : Fin 24, phi (v k • wordActionA h k u)
      = (fun j => phi v j • wordAction h j (phi u)) (piEquiv k) := fun k => by
    rw [phi_smul, phi_wordActionA]; simp
  rw [Finset.sum_congr rfl fun k _ => step k]
  exact Equiv.sum_comp piEquiv (fun j => phi v j • wordAction h j (phi u))
```

The coefficient bookkeeping is the single line `phi v (piIdx k) = v k`, which is
`phi`'s definition composed with `invIdx_piIdx` — not a computation.

### What had to be built first

The subscript basis already had its right basis action packaged
(`HeckeH4AlgebraLaws.wordAction`, `mulNF₄_e_right`, `mulNF₄_expand_right`); the
ASCII basis did not. New in `QOU/Machinery/H4AsciiPresentation.lean`:
`wordActionA`, `mulNF_zero_right`, `mulNF_sum_right`, `basis_decompA`,
`mulNF_e_right`, `mulNF_expand_right` — the same five, on the other table.
`wordActionA` is transcribed from `mulNF`'s own term list and cross-checked
against it **and** against the 24 `phi_word_*` statements; all 24 agree.

New in the bridge: `piEquiv` (the relabelling as an `Equiv`, which is what makes
a sum reindexable), `phi_smul`, `phi_sum`, `phi_apply_piIdx`, and
`phi_wordActionA` — the 24 `phi_word_*` lemmas packaged as one equation in the
index, which is the form a sum can be reindexed by. `fin_cases` + `exacts`;
the five `Matrix.cons_val_*` simp lemmas one expects to need are all reported
unused, so `simp only [wordActionA, wordAction, piIdx]` suffices.

### One `exact` needed its argument spelled out

`exact Equiv.sum_comp piEquiv _` fails with "typeclass instance problem is
stuck" — with `f` a metavariable the `AddCommMonoid` on the codomain cannot be
found. Passing `f` explicitly fixes it. Worth remembering: that error message
does not mean the lemma is wrong for the goal.

### Correction to step 4 of the plan above

**Retiring the ASCII chain does not follow from the consumers moving across.**
The importers are now exactly: the chain itself, `H4AsciiPresentation`, and
`H4BasisBridge`. Nothing else in the tree imports `MarkovTraceH4` or
`MarkovTraceH4Gram*`. But the bridge is not a consumer that can be repointed —
`trM4_cyclic`'s *proof* runs through `H4.trM_cyclic`, so the 576-entry Gram
closure is a dependency of the theorem, not merely of its users. Deleting the
chain would delete the proof.

What this does achieve is narrowing the target: the ASCII chain now has exactly
**one** remaining job in the whole tree, and it is `trM_cyclic`. Retiring it
requires an independent proof of cyclicity on the subscript basis, and the route
is already identified — `QOU.Machinery.BilinearTrace.gram_symm_of_rep_decomp`:
if `trM4` decomposes as a finite weighted sum of representation traces, each
multiplicative on `mulNF₄`, Gram symmetry follows with no per-pair computation,
and `HeckeH4Wedderburn.wedderburn₄` supplies exactly those five representations.
What remains is identifying the Markov weights. Not attempted.

### Step 3 done too: the Markov trace at `n = 4`

`QOU/Hecke/MarkovTraceOnH4A.lean` — `markovTraceH4A : MarkovTrace 4 q (H4A K (q − q⁻¹))`
and `contextH4 : QOU.Shared.MarkovTraceContext`. `cyclic` is `trM4_cyclic`; that
was the whole obstruction, and it is not free at `n = 4` because `H₄(q)` is
noncommutative.

The trace values cost nothing to evaluate, because every one of them is a basis
vector and `trM4 z h (e₄ j) = TRM4 z h j` collapses the 24-term sum to a single
weight (`trM4_e₄`, by `Pi.single_apply` + `Finset.sum_ite_eq'`). The generators
are `b 1`, `b 2`, `b 6`; the three ordered products are

| product | basis vector | via | weight |
|---|---|---|---|
| `σ₀σ₁` | `b 4` | `b_tree_4` | `z²` |
| `σ₁σ₂` | `b 7` | `b_tree_7` | `z²` |
| `σ₀σ₂` | `b 8` | `farcomm02`, then `b_tree_8` | `z²` |

The third is the one `n = 3` cannot ask — the far-commuting pair — and reaching
its basis vector needs the *relation*, not just the word tree, since the tree
only gives `σ₂σ₀ = b 8`.

Supporting: `trM4_add` / `trM4_smul` added next to `trM4` in
`HeckeH4StabilizationRung` (the `trM4` counterparts of `MarkovTraceH4`'s
`trM_add` / `trM_smul`, which existed only on the ASCII side).

**Cost warning, measured.** Touching `HeckeH4StabilizationRung` invalidates
`HeckeH4BlockMap211` and `HeckeH4BlockMap31`, which are the real build pole:
each ran **>25 minutes of wall time at ~6 GB RSS** (both at once, ~12 GB), with
`set_option maxHeartbeats` up to 16 000 000 and ten such settings per file — the
`.olean` is 69 MB, against 36 MB for a Gram chunk. Any future edit to the rung
pays that again. If `trM4_add`/`trM4_smul` had gone in the leaf that uses them
instead, the rung would not have been touched at all; they are placed next to
`trM4` deliberately, but the price is worth knowing before the next edit there.

### One-line trap: `rw` against a `def`

`s0 K q` is a `def` for `b K q 1`, so `rw [b_tree_4 K q]` fails on a goal
mentioning `s0` — "did not find an occurrence" — even though the two are
definitionally equal. `show traceMap K q z (b K q 1 * s1 K q) = z * z` first;
`show` goes through `isDefEq`, `rw` does not. Cost me three identical errors.

---

## 2026-08-10 — step 4: the Markov weights are identified, in closed form

The blocker recorded above was *"what remains is identifying the Markov weights.
Not attempted."* They are now identified, exactly, and verified.

Producer: [`computations/h4_markov_weights_closed_form.py`](../computations/h4_markov_weights_closed_form.py)
→ `computations/h4-markov-weights-closed-form.witness.json`.

With `A = q²+1`, `B = q⁴+q²+1`, `C = q⁴+1`:

| λ | d | w_λ |
|---|---|---|
| `(4)` | 1 | `(qz+1)(qAz+1)(qBz+1) / (A²BC)` |
| `(3,1)` | 3 | `−q (z−q)(qz+1)(qAz+1) / (A²C)` |
| `(2,2)` | 2 | `−q³(z−q)(qz+1) / (A²B)` |
| `(2,1,1)` | 3 | `q²(z−q)(qz+1)(Az−q³) / (A²C)` |
| `(1,1,1,1)` | 1 | `−q³(z−q)(Az−q³)(Bz−q⁵) / (A²BC)` |

**A, B, C are exactly the `wedderburn₄` genericity hypotheses `h2`, `h3`, `h4`.**
The weights are singular precisely off that locus — which is the consistency
check that they belong to that decomposition, not merely that they fit.

Every weight carries `(z−q)` except `(4)` and `(qz+1)` except `(1,1,1,1)`; `q`
and `−q⁻¹` are the two Hecke eigenvalues.

### What was verified, and how

Nothing here is fitted. The centre is computed as the nullspace of the
commutator system, a generic central element is diagonalised to give the five
central primitive idempotents, and the characters are read off as
`χ_λ(x) = tr(R_x·P_λ)/d_λ`, the weights as `w_λ = tr_M(z_λ)/d_λ`. The closed
forms above were then *recognised* from those and re-checked. At each of
`q = 2, 3, 5/2, 7/3, 4`, exactly:

* block dims `1,1,2,3,3`, `Σd² = 24`;
* all 5 closed forms match the spectral weights;
* `χ_λ(1) = d_λ`;
* **`tr_M(b_i) = Σ_λ w_λ χ_λ(b_i)` on all 24 basis elements** — this is
  precisely the `hdecomp` hypothesis of `gram_symm_of_rep_decomp`.

Arithmetic is exact (sympy `Rational` + symbolic `z`); no float64 in the
derivation.

### Independent confirmation, and a label correction

`computations/alpha-k-jones-markov-h4.witness.json` already carried these five
weights as **floats** at the substrate anchor, from a different method (a
numerical constraint system, `status: exploratory`). The closed forms reproduce
all five to ≤ 2.1e-14 relative, and `Σ_λ w_λ d_λ = 1 = tr_M(1)` exactly.

That cross-check also **fixed the partition labelling**, which the spectral
computation alone does not determine — my first reading had the two `d=1` blocks
and the two `d=3` blocks swapped. The table above is the corrected one.

### Also established, independently of the weights

The same script's sibling probe verified **Gram symmetry on all 576 basis
pairs** of `trM4` symbolically in full generality (`h`, `z` free) — i.e.
`trM4_cyclic` on the subscript basis is true and reachable by
`cyclic_of_gram_symm` alone. That is a 576-entry closure, which is the thing the
rep-decomposition route exists to avoid, but it is worth recording that the
target theorem is confirmed independently of the ASCII chain.

The transcription of the three generator actions was checked by re-deriving the
whole Hecke presentation from them (both quadratics, both braid relations, far
commutation).

### What remains for step 4

The Lean wiring. `gram_symm_of_rep_decomp` needs the five `ρ_λ` as maps
`(Fin 24 → R) → Matrix (dim λ) (dim λ) R` with `ρ_λ (mulNF₄ h u v) = ρ_λ u * ρ_λ v`,
plus `hdecomp`. `HeckeH4Wedderburn` supplies the `ρ_λ` (`chiNF₄ q`,
`chiNF₄ (-q⁻¹)`, `blockOf22`, `blockOf31`, `blockOf211`) and `wedderburnHom₄`
is already an `AlgHom`, so multiplicativity should come from that rather than
from a fresh computation. `hdecomp` is the 24 equations verified above.

**Cost warning, measured this session:** the H4 machinery is *absent from the
`lake-cache/qou-v4-24-0-new` olean set* — `HeckeH4StabilizationRung`,
`HeckeH4AlgebraLaws`, `HeckeH4Wedderburn`, `H4BasisBridge` and the three
`HeckeH4BlockMap*` are all missing. So the Lean side of step 4 starts with a
from-source build of that cone, and the bean's own measurement says
`HeckeH4BlockMap211` and `HeckeH4BlockMap31` are >25 min each at ~6 GB. Budget
for that before starting, and seed the cache branch afterwards.

## CLAIM 2026-08-10

`in-progress`, branch `claude/x64l-retire-ascii-h4-chain`.

Steps 1–3 are done and merged. **Step 4 only**: an independent proof of `trM4`
cyclicity on the subscript basis, so the ASCII Gram chain stops being a
dependency of the theorem and can be deleted. Route as recorded above —
`gram_symm_of_rep_decomp` over `wedderburn₄`'s five representations; the open
part is identifying the Markov weights.

### Scoping, before any code: `hmul` is already proved — only `hdecomp` is open

`gram_symm_of_rep_decomp` needs two hypotheses. Checking what the tree already
has, rather than assuming:

* **`hmul` — done.** `ρ_λ (mulNF₄ u v) = ρ_λ u * ρ_λ v` exists for all three
  matrix blocks, as the `map_mul'` field of the block algebra homs:

      QOU/Machinery/HeckeH4BlockMap211.lean:518  blockOf211_mulNF₄
      QOU/Machinery/HeckeH4BlockMap22.lean:343   blockOf22_mulNF₄
      QOU/Machinery/HeckeH4BlockMap31.lean:518   blockOf31_mulNF₄

  and `wedderburn₄` packages all five as
  `H4A ≃ₐ[K] K × K × M₂ × M₃ × M₃`, so the two one-dimensional blocks come with
  the same field. **Nothing has to be built for `hmul`.**

* **`hdecomp` — the whole remaining task.**
  `trM4 z h x = ∑_λ w_λ · (ρ_λ x).trace`.

**Why that is smaller than it looks.** `trM4` is linear (`trM4_add`,
`trM4_smul`, both already present), so `hdecomp` need only hold on the 24 basis
vectors, and `trM4 z h (e₄ j) = TRM4 z h j` collapses each left side to a single
table entry (`trM4_e₄`, already proved). So the identity is 24 scalar equations

    TRM4 z h j  =  ∑_λ w_λ · (ρ_λ (e₄ j)).trace       (j : Fin 24)

in **five** unknowns. Five of them determine the weights; the other nineteen are
then checks, not solves. That is the shape of the "identify the Markov weights"
step, and it is finite and mechanical rather than open-ended.

**And it does not touch the build pole.** All of this is downstream of
`HeckeH4StabilizationRung`, so it goes in a new leaf module and does **not**
invalidate `HeckeH4BlockMap211`/`31` (>25 min each at ~6 GB RSS). The cost
warning recorded above applies to edits *in* the rung; this is not one.

**Not yet checked:** whether the corpus already carries these five weights under
the `y_λ` name. They are not in `QOU/Mathlib/HeckeAlgebra.lean` under `y_`, so
either they live elsewhere or they have to be computed from the block traces.
Deriving them from the 24 equations needs no external formula either way.

## 2026-08-10 — a better route than the one this bean recommends, and a cost measurement

### The recommended route (representation decomposition) is not the cheapest

`gram_symm_of_rep_decomp` works, and `hmul` is free (above). But `hdecomp` needs
the five Markov weights, and getting them means reading `tr(ρ_λ(e₄ j))` off
`blockOf31` / `blockOf22` / `blockOf211` — whose diagonal entries are single
linear forms in `v 0 … v 23` running to **thousands of characters each**, with
`(q⁴+q²+1)⁻¹` and `(q²+1)⁻¹` denominators throughout. Any Lean proof of
`hdecomp` unfolds those 24 times. That plausibly costs more than the Gram chain
being deleted.

### The cheaper route: cyclicity only has to be checked on the generators

`{y | ∀ x, tr(xy) = tr(yx)}` is a **subalgebra**, not merely a subspace:

    tr(x·y₁y₂) = tr((x y₁)·y₂) = tr(y₂·(x y₁)) = tr((y₂ x)·y₁)
               = tr(y₁·(y₂ x)) = tr(y₁y₂·x)

It contains `1`, is closed under `+` and `•`, and `mulNF₄_assoc` is already
proved. So cyclicity follows from the **three generators**, and by linearity in
`x` from basis vectors only:

    ∀ g ∈ {1, 2, 6}, ∀ i : Fin 24,
      trM4 z h (wordAction h g (e₄ i)) = trM4 z h (wordAction h i (e₄ g))

using `mulNF₄_e_right : mulNF₄ h u (e₄ j) = wordAction h j u` on both sides.

**72 identities, not 576**, and none of them mentions Wedderburn, a block map,
or a Markov weight. Everything needed is already in the tree:

* `mulσ₀/₁/₂` and `wordAction` — `HeckeH4StabilizationRung`, `HeckeH4AlgebraLaws`
* `mulNF₄_e_right`, `mulNF₄_sum_left`, `basis_decomp₄`, `mulNF₄_assoc`
* `b_tree_1 … b_tree_23` — `QOU/Hecke/InstanceOnH4A.lean`, the complete word
  tree: every basis vector is `b j' * s_g` for an earlier `j'`, so the induction
  that lifts the generator cases to all 24 basis vectors is already written down.

### Measured: the naive tactic script does not work

Two probes, both run to completion, neither of which should be repeated:

1. `fin_cases i <;> simp [wordAction, mulσ₀, mulσ₁, mulσ₂, e₄, trM4, TRM4,
   Fin.sum_univ_succ, Pi.single_apply] <;> ring` over all 24 `i` at once —
   **4m16s, then `maximum recursion depth` on six goals and a heartbeat timeout
   at 1 000 000 on another.** One `simp` set cannot simultaneously unfold
   six-deep `mulσ` composites and expand a 24-term sum.
2. Staged (`simp only` for the actions, then `simp only` for the sum), two
   individual goals, `maxRecDepth 4000`, `maxHeartbeats 2000000` — **4m09s and
   still open.** The residue shows exactly what is missing: `Pi.single_apply`
   leaves `if (3 : ℕ) = 0 then 1 else 0` unresolved, and `![…] 2` applications
   are not reduced. So it needs `Matrix.cons_val_succ` and a decision procedure
   on the `Fin` literals, not more heartbeats.

**~2 minutes per goal × 72 is not viable.** The fix is to stop expanding
`trM4`'s sum at all:

* `mulσ_g h (e₄ i)` has **at most two** non-zero entries — visible directly in
  the tables, whose entries are `v k` or `v k + h * v k'`. So each action of a
  generator on a basis vector is a two-term combination of basis vectors, and
  `trM4` of it collapses through `trM4_e₄` to at most two table entries. Proving
  those 72 small identities (`funext k; fin_cases k <;> simp`) never builds a
  24-term sum.
* The composite side (`wordAction h i (e₄ g)` for long words) should be reached
  by *iterating* that lemma along the word, not by unfolding the composite.

**Next**: build the 72 `mulσ_g (e₄ i) = <two-term combination>` lemmas first and
measure one, before writing any of the cyclicity statement. If a single one is
not sub-second, this route is no better than the last and the bean should say so.
