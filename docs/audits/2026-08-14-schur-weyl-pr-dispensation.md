# Quantum Schur–Weyl arc: PR dispensation and the three-gap frontier (2026-08-14)

**Scope.** Records the dispensation of PRs [#4982](https://github.com/litlfred/qou/pull/4982)
and [#4980](https://github.com/litlfred/qou/pull/4980) (both closed unmerged,
superseded), the landed arc that absorbed them, and the exact state of the three
remaining gaps. Written so that a later corpus-grep for "general-λ Hoefsmit
braid", "HeckeWedderburnData instance", or "dim H_n(q) ≤ n!" lands on the current
frontier rather than re-deriving it.

Beans: `qou-fz23` (session), `qou-c275` (this doc), `qou-j6f9` / `qou-tpl5` /
`qou-gjg6` (the three gaps).

## 1. The landed arc

| PR | Landed | Contribution |
|---|---|---|
| [#4963](https://github.com/litlfred/qou/pull/4963) | merged | `n=3` complete: `dim H_3(q) = 6`, Wedderburn iso `H_3 ≅ ℝ × ℝ × M₂`, Markov trace |
| [#4978](https://github.com/litlfred/qou/pull/4978) | merged | General `n`: tower inclusion + generators-generate; Hoefsmit block scaffolding (`seminormalBlock`, `seminormalRep22` = the λ=(2,2) 4-strand rep); canonical Ocneanu Markov weights |
| [#5004](https://github.com/litlfred/qou/pull/5004) | merged (rebase, `6bb7908`) | General `dim ≤ n!`: the coset spanning machinery of `SchurWeyl/HeckeCoset.lean`, reduced to a single combinatorial lemma |
| [#4982](https://github.com/litlfred/qou/pull/4982) | **closed unmerged** | Superseded — its work was integrated onto #4978 against current `main` |
| [#4980](https://github.com/litlfred/qou/pull/4980) | **closed unmerged** | Superseded — Part (A) integrated onto #4978; Part (B) remains open |

## 2. Why #4982 and #4980 were not merged (SHA-level verification, 2026-08-14)

Both branches were cut from, or stacked on, the pre-merge `dim6-closure` branch.
By the time their content had been integrated elsewhere, merging the branches
themselves would have *reverted* `main`. Verified against `main` at `42d54441`:

**#4982**, head `6ddb7a0b7b1405a70c3f066da04cb54b929447ea` —
`git diff --stat origin/main 6ddb7a0b -- .../SchurWeyl/` shows 7 files changed,
19 insertions, **1174 deletions**: `HeckeCoset` (−259), `HeckeDim3Dim` (−80),
`HeckeDim3Indep` (−104), `HeckeInclusion` (−86), `HeckeMarkov3` (−220),
`HeckeWedderburn3` (−102), `QJucysMurphy` (−342). `HoefsmitRep.lean` — the PR's
entire contribution — **does not appear in the diff**, i.e. is byte-identical to
`main`. Whole-tree diff: 130 files, ~10 000 lines each way.

**#4980**, head `a3b30df37e9d93036aa80c6c3766c0913496a51a` —
same comparison shows 4 files, 8 insertions, **866 deletions**: `HeckeCoset`
(−259), `HeckeInclusion` (−86), `HoefsmitRep` (−187, the branch being *behind*
#4982's scaffolding), `QJucysMurphy` (−342). `HeckeMarkov3.lean` — the PR's Part
(A) — **does not appear in the diff**. `mergeable_state` was already `dirty`.
Whole-tree diff: 127 files.

Spot-check that the substance is on `main`, in `SchurWeyl/`: `seminormalBlock`
(23 refs), `seminormalRep22` (17), `S1_eq_seminormalBlock` (5) in
`HoefsmitRep.lean`; `markovWeight0` (11), `markovWeights_markov_σ0σ1` (2) in
`HeckeMarkov3.lean`.

**Dispensation.** Both stay closed; both branches are retained per AGENTS.md
branch-workflow rule 9. There is no rebase-salvage to do — neither branch holds
anything `main` lacks. Receipts recording this verification are posted on each PR.

## 3. The three-gap frontier

All three are isolated, self-contained pickups. None is a fit; each is a stated
proposition with a `-- Ref:` citation or an open bean.

### 3.1 `qou-j6f9` — CLOSED this session: the gap was handedness, not depth

File: [`SchurWeyl/HeckeCoset.lean`](../../content/quantum-observable-universe/lean/QOU/SchurWeyl/HeckeCoset.lean).
**The file is now sorry-free**, and `finrank_le_factorial` — the general-`n`
bound `finrank_K H_{n+1}(q) ≤ (n+1)!` — is axiom-clean
(`[propext, Classical.choice, Quot.sound]`, no `sorryAx`).

**What the gap actually was.** The open `sorry` sat in `gen_mul_span_mem`, which
stated that *left* multiplication by a generator preserves the span of the coset
family. That formulation is mismatched with the family: `cosetFam` carries the
subalgebra on the **left** (`ι(H_m)·r_j`), so left multiplication by the top
generator has to move `σ_m` past the opaque `ι(w)` — and no Hecke relation does
that. Restating the closure lemma on the **right** (`span_mul_gen_mem`, with
`Submonoid.closure_induction_right` replacing `_left` in
`span_cosetFam_eq_top`) puts the generator next to the `r_j` factor, where the
relations live. The top generator then needs no special treatment at all: the
case split is on `i + j` versus `m`, not on whether `i` is the top index.

**The four cases** (each its own sorry-free lemma), with
`r_j = σ_m σ_{m-1} ⋯ σ_{m-j+1}`:

| lemma | condition | `r_j · σ_i` |
|---|---|---|
| `descProd_mul_σ_of_add_lt` | `i + j + 1 ≤ m` | `σ_i · r_j` (far commutation) |
| `descProd_mul_σ_of_add_eq` | `i + j = m` | `r_{j+1}` (the defining recursion) |
| `descProd_mul_σ_of_add_eq_succ` | `i + j = m + 1` | `(q-qi)·r_j + (q·qi)·r_{j-1}` (quadratic) |
| `descProd_mul_σ_of_le_add` | `m + 2 ≤ i + j` | `σ_{i-1} · r_j` (braid) |

Only the braid case needs an induction of its own: for `i + j = m + 2` the
Yang–Baxter move `σ_i σ_{i-1} σ_i = σ_{i-1} σ_i σ_{i-1}` plus far commutation
pulls `σ_{i-1}` out on the left; for `i + j ≥ m + 3` the generator commutes with
the last factor and the length drops. A length bound `j ≤ m + 1` is required and
is supplied by the family's index type `Fin (m+2)` — without it the statement is
false at `j = m + 2`, where `i` may be `0` and `σ_{i-1}` is not the intended
predecessor.

Refs as cited in the file: [mathas1999] Ch. 1, [geckpfeiffer2000] §4.4. The
`n = 3` template (`HeckeDim3.gen_mul_mem`, twelve explicit reductions) matches
the four cases above.

**Scope note (unchanged).** This is the *spanning* (upper-bound) half only. The
linear-independence half — `dim ≥ n!` — is still not claimed in general `n`; at
`n = 3` it is `HeckeDim3Indep`. So `dim H_n(q) = n!` remains open in general;
what is now proved in general is `≤`.

**Verification.** `lean`-direct exit 0 against the real Mathlib + `HeckeInclusion`
import cone (Mathlib oleans restored from `lake-cache/qou-v4-24-0`; QOU cone built
from source). `#print axioms` on all eight new/changed declarations shows no
`sorryAx`; `descProd_mul_σ_of_add_lt`, `_of_add_eq` and `_of_le_add` do not even
use `Classical.choice`.

### 3.2 `qou-tpl5` (B) — CLOSED this session: the `HeckeWedderburnData` instance

New sorry-free file
[`SchurWeyl/HeckeWedderburnData3.lean`](../../content/quantum-observable-universe/lean/QOU/SchurWeyl/HeckeWedderburnData3.lean).
`heckeDim3 = ![1,1,2]`; `piReshape3` is the algebra isomorphism
`ℝ × ℝ × M₂(ℝ) ≃ₐ[ℝ] Π l : Fin 3, M_{d_l}(ℝ)` (fully proved — both inverse laws,
`map_mul`, `map_add`, `commutes'`), using `M₁(ℝ) ≅ ℝ` on the two scalar blocks;
`heckeWedderburnData3` is the bundle, from `wedderburn3` (SW-7) plus the
canonical Ocneanu weights (SW-8 part A) plus `markovTrace3`. Its `markov_eq`
field is **proved**, not assumed: the weighted-character definition agrees
termwise with the block traces, because the trace of a `1 × 1` block is its
single entry. `markov_one_eq₃` records the payoff — every conditional result in
`QSchurWeyl.lean` (`markov_one_eq`, `markov_add`, `markov_smul`) now applies
concretely to `H_3(q)` rather than to an assumed bundle.

**Note for the next reshape.** The friction was elaboration, not mathematics:
`(0 : Fin (heckeDim3 0))` cannot be elaborated, because instance synthesis runs
at *reducible* transparency and will not evaluate `![1,1,2] 0` down to `1` —
even though `heckeDim3_zero` is `rfl`. The fix is `entry11`, which takes the
width as an explicit hypothesis and builds the index with `omega` instead of a
numeral.

Refs [jones1987], [wenzl1988].

### 3.3 `qou-gjg6` — the general-λ Hoefsmit braid (size-6 S₃-orbit)

The residual `sorry` in `hoefsmit_seminormal_rep`
([`SchurWeyl/HoefsmitRep.lean`](../../content/quantum-observable-universe/lean/QOU/SchurWeyl/HoefsmitRep.lean)),
Ref'd [hoefsmit1974], [ram1997]. What is landed sorry-free: the generic axial-
distance `2×2` block `seminormalBlock` with its quadratic relation and
non-degeneracy, `S1_eq_seminormalBlock`, and `seminormalRep22` (the first
4-strand seminormal rep, carrying the first non-vacuous far-commutation
`σ₀σ₂ = σ₂σ₀`).

**Step (iii) closed this session; steps (i)–(ii) remain.** The axial-distance
parameter is identified and machine-verified, and the size-6 orbit braid is proved;
what is left is orbit enumeration and block assembly.

New sorry-free file
[`SchurWeyl/SeminormalParam.lean`](../../content/quantum-observable-universe/lean/QOU/SchurWeyl/SeminormalParam.lean)
supplies the rational function the general construction needs:

$$a(d) \;=\; \frac{q - q^{-1}}{1 - q^{-2d}}$$

This is **anchored, not asserted.** `S1` was built by hand in `HoefsmitRep.lean`
to satisfy the braid relation with `S0`, with no axial-distance formula involved,
and its `(0,0)` entry is `-1/(q³+q)`. In `[[1,2],[3]]` the entry `2` has content
`1` and `3` has content `-1`, so `σ₁` acts at axial distance `d = -2`, and
`a(-2) = (q-q⁻¹)/(1-q⁴) = -1/(q³+q)`. That agreement is `S1_eq_seminormalParam`.

Two consequences remove choices from the remaining build:

- `a(1) = q` and `a(-1) = -q⁻¹` — the **size-1 orbit eigenvalues are the same
  formula** as the size-2 blocks. So the orbit trichotomy of step (i) is a case
  split on *block size* only, not on the parameter.
- `a(d) + a(-d) = q - q⁻¹` — matches `seminormalBlock`'s trace, so a size-2 orbit
  is exactly `seminormalBlock q (a d)`, its lower-right entry being `a(-d)` read
  from the partner tableau. Step (ii) assembly needs no extra normalisation.

**A hypothesis worth carrying forward:** `q² ≠ 1` is real, not cosmetic. At
`q = ±1` both `q - q⁻¹` and `1 - q⁴` vanish, so `a(-2)` evaluates to `0` (Lean's
`0/0`) while `S1`'s entry is `-1/(2q) ≠ 0`. That is the Hecke algebra degenerating
to the group algebra, where the seminormal form is not given by this formula. Any
general-`λ` statement must carry it.

**Step (iii) — CLOSED.** New sorry-free file
[`SchurWeyl/Orbit6Braid.lean`](../../content/quantum-observable-universe/lean/QOU/SchurWeyl/Orbit6Braid.lean):
`genA_genB_braid` proves `ABA = BAB` on a generic size-6 `S₃`-orbit, axiom-clean.

Two things made it tractable.

*The statement is polynomial, not rational.* The three parameters `a₁ = a(p)`,
`a₂ = a(r)`, `a₃ = a(p+r)` are **not independent**; eliminating the multiplicative
coordinates leaves exactly one relation,

$$a_3\,(a_1 + a_2 - c) = a_1 a_2, \qquad c = q - q^{-1}$$

and that relation is precisely what the braid needs — checked sufficient (free
random `a₁, a₂, c`) and necessary (perturbing `a₃` breaks it). So the theorem
carries no `q`, no `u`/`v`, and no integer distances; `seminormalParam_mul_rel`
ties it back to the real seminormal parameters, making it a statement about the
Hoefsmit matrices rather than about abstract arrays.

*The orientation convention was identified, not guessed.* An exhaustive
exact-rational search over the four orientation combinations found both-negative
and both-positive holding, and **both mixed combinations failing** with six
nonzero entries in `ABA - BAB`. Only the consistent case is formalised; the mixed
negative is labelled in the file as numerical rather than formal.

**Performance note worth reusing.** `!![…]` literals are the wrong representation
for a 6×6 identity: `simp` chases `vecCons` chains through a 1296-term triple
product and times out at 2M heartbeats *even on a pure-`ring` goal*. Defining via
`Matrix.of fun i j => match (i : ℕ), (j : ℕ) with …` makes entry lookup a single
iota reduction — same theorem, 100 seconds.

**Step (i), partially landed.** New sorry-free file
[`SchurWeyl/TableauCells.lean`](../../content/quantum-observable-universe/lean/QOU/SchurWeyl/TableauCells.lean).
The `StandardYoungTableau` structure carries `bijOn` — the entry map is a bijection
from cells onto `{1,…,|μ|}` — but does not *expose* the inverse, and the whole
construction has to run backwards: given entry `k`, which cell holds it. Now
`cellOf T k` does, total (off-range `k ↦ (0,0)`, so no subtype bookkeeping leaks
downstream), with `cellOf_spec` / `cellOf_mem` / `entry_cellOf` and `cellOf_unique`
— the last being what lets `cellOf` be computed from an explicit tableau. On top of
it, `axialDist T k` is the `seminormalParam` argument for `σ_k`, and
`axialDist_of_sameRow = +1` / `axialDist_of_sameCol = -1` settle **the two size-1
orbit cases**; composed with `seminormalParam_one` / `_neg_one` those are exactly the
scalar eigenvalues `q` and `-q⁻¹`.

The content sits in `sameRow_adjacent` / `sameCol_adjacent`: consecutive entries
sharing a row or column must occupy **adjacent** cells, since a cell strictly between
them would carry an entry strictly between two consecutive integers. That is where
standardness (bijection onto an interval) is doing the work rather than mere
semistandardness, and it is why the distance is exactly `±1` and not merely signed.

**The `s_k`-action also landed.** `SwapAdmissible T k` — the cells of `k` and `k+1`
share neither a row nor a column — is, by the two adjacency lemmas, exactly the
complement of the size-1 cases, i.e. *the* size-2 orbit condition. `swapTableau`
builds `s_k · T` and proves it is again standard, and `swapTableau_involutive` makes
`{T, s_k·T}` a genuine two-element orbit. The order proof has a pleasant shape: the
swap can only disturb order at the two swapped values, and the single bad configuration
— `k` and `k+1` sharing a row or column — is precisely what admissibility excludes, so
handing that negation to `omega` closes every `split_ifs` branch at once. Standardness
of the filling survives because the value-swap is an involution of `{1,…,n}`
(`bijOn_swapVal`, via `Set.InvOn.bijOn`).

*The one assumed hypothesis has since been discharged.* `cellOf_swapTableau_self` and
`cellOf_swapTableau_succ` compute `cellOf` of the swapped tableau — the swap merely
exchanges the cells of `k` and `k+1`, each by `cellOf_unique` — so
`swapAdmissible_swapTableau` **derives** admissibility of `s_k·T` from that of `T`, and
`swapTableau_involutive` now carries no side hypothesis. `{T, s_k·T}` is a two-element
orbit outright.

**Step (i) is complete**, and — as of 2026-08-15 — two of the four step-(ii) blockers
have closed as well. Current state:

| step-(ii) blocker | state |
|---|---|
| far commutation of the `s_k`-actions (`σ_kσ_l = σ_lσ_k`, `\|k-l\| ≥ 2`) | **closed** — `swapTableau_comm` (#5053) |
| the size-3 orbit identity | **closed** — `Orbit3Braid` (#5062) |
| orbit-size classification for `⟨s_k, s_{k+1}⟩` on `SYT λ` | open |
| per-orbit basis correspondence onto the explicit index orderings | open |

**Every orbit-*local* identity is now proved**: size 1 (the scalars `q`, `-q⁻¹`, via
`axialDist_of_sameRow`/`_sameCol` with `seminormalParam_one`/`_neg_one`), size 2
(`seminormalBlock`, with `swapTableau` as the orbit partner), size 3 (`Orbit3Braid` — the
standard fillings of a domino together with a disjoint cell, `3!/2! = 3`), and size 6
(`Orbit6Braid`). `Orbit3Braid`'s two hypotheses are derived from `seminormalParam`, not
merely stated.

What is left is therefore **assembly**, not new identities: classify the orbits, and map
each onto the explicit index ordering in which its identity is stated.
`hoefsmit_seminormal_rep` keeps its `-- Ref:`-cited `sorry` until both land.

**Two corrections worth keeping.** Both were mine, and both were wrong at the time of
writing. Step (ii) was first described in this document as "bookkeeping rather than new
mathematics"; it in fact required four distinct blockers, two of which needed real proofs.
And the size-3 case was initially probed with the scalar left unconstrained, which made
every relation fail — including the quadratic — until `sc² = c·sc + 1` was imposed. They
are recorded rather than silently overwritten, because the failure mode they share —
assuming the remaining work is plumbing — is the one most likely to recur.

## 4. Verification posture

CI is `workflow_dispatch`-only under the 2026-06-30 Actions-billing directive, so
agent-owned verification is the gate (AGENTS.md §"QA is agent-owned"). The merged
arc was verified `lean`-direct (exit 0) against the real Mathlib + QOU import
cone, with `#print axioms` confirming `[propext, Classical.choice, Quot.sound]`
on the new declarations and `sorryAx` present only where a `-- Ref:`-cited gap is
declared. The dispensation in §2 is a pure git-level check and required no build.
