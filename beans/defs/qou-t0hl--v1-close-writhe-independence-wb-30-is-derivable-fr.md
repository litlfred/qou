---
# qou-t0hl
title: 'V1: close writhe-independence — w(B_3)=0 is DERIVABLE from the gluon unit'
status: in-progress
type: task
priority: normal
tags:
    - 8f-gen
    - 8f-open
    - reorg-2026-10-04
created_at: 2026-08-10T18:23:24Z
updated_at: 2026-11-16T19:05:33Z
parent: qou-8lxd
---

The eightfold-way requirement 'second invariant INDEPENDENT of the writhe' is
NOT proved; the published p/n argument is a non-sequitur (Y=w^2/4 reproduces both
rows -- WritheIndependenceCriterion.lean). The correct criterion is: two states
with EQUAL writhe and DIFFERENT Y.

THE PREMISE IS NOW DERIVABLE, which is what was missing:
  gluon unit      sigma_0 sigma_1^-1   -> writhe = +1 -1 = 0
  Borromean baryon B_3 = (sigma_0 sigma_1^-1)^3 -> writhe = 3(+1-1) = 0
  vacuum / empty braid                  -> writhe = 0
So w(baryon) = w(vacuum) = 0 by DIRECT COMPUTATION from the braid word, not by
hypothesis. With Y(baryon)=+1 (nucleon_hypercharge_eq_one, merged) and
Y(vacuum)=0, equal_writhe_distinct_Y_forces_non_factoring closes it.
This replaces baryon_vacuum_separating's assumed hypotheses with derived facts.


## Correction 2026-10-10 — the writhe half IS derived; the closing half is not, and the named closer does not exist

Measured during the `8f-gen` front triage. Taking the body's claimed chain
line by line:

| claim | measured |
|---|---|
| `w(gluon unit) = 0` by direct computation | ✅ `writhe_gluon : writhe gluonUnit = 0 := by decide` (`ChiralFermionBraidWords.lean:112`) |
| `w(B₃) = 0` by direct computation | ✅ `writhe_borromean : writhe borromean = 0 := by decide` (`:115`) |
| `Y(baryon) = +1` via `nucleon_hypercharge_eq_one` | ✅ exists (`HyperchargeBatteryReduction.lean:187`), `by decide` |
| `Y(vacuum) = 0` | ❌ **no carrier.** No `vacuum` object with a hypercharge exists anywhere; the only occurrence of "vacuum" in `QOU/StandardModel/*.lean` is `baryon_vacuum_separating`'s own abstract parameter |
| `equal_writhe_distinct_Y_forces_non_factoring` closes it | ❌ **does not exist** — 0 matches across every `.lean` in the tree |
| "replaces `baryon_vacuum_separating`'s assumed hypotheses with derived facts" | ❌ not done; it still takes `hbw hvw hbB hvB` as hypotheses (`SecondCrossingInvariant.lean:118`) and is proved `rw; norm_num` |

So the first half of the body's claim is **right and is real progress** — the
writhe premise is computed from braid words rather than assumed. The second
half is not yet true.

### 🛑 The chain as written straddles two unrelated types

It takes `w` from a braid word and `Y` from `nucleon_hypercharge_eq_one`. Those
live on different types with **no map between them**:

```lean
abbrev BraidWord := List ℤ                        -- QOU.StandardModel.BraidWords
def borromean : BraidWord := gluonUnit ++ gluonUnit ++ gluonUnit

def proton : FermionCharges := ⟨6, 3, 6, 0⟩       -- QOU.StandardModel
```

`baryon_vacuum_separating` needs `w : S → ℤ` **and** `B : S → ℚ` on **one**
type `S`, so the chain cannot be assembled at all as stated. This is the
same shape as the 2026-06-01 s5-so3 verdict (*"the two halves live in different
group algebras … with no canonical map"*), and AGENTS.md §"Grep the claim
SHAPE" item 3 names it: *shared type, or shared instance?*

The framing writhes make it concrete: `WritheIndependenceCriterion.lean`'s
docstring gives `w(p) = +2`, `w(n) = −2` — **not** `0` — while
`writhe_borromean = 0` is about the braid word. The chain borrows a zero from
one object and a hypercharge from another.

### What the corpus's own fix says, and where it leaves this

`qou-h0zz`'s 2026-08-10 result settles the datum, and it is **not `Y`**:

> the "second invariant independent of the writhe" is **B** (μ̄₁₂₃), **NOT L**.

Read with `B`, the straddle disappears — `borromean` and `gluonUnit` are **both
braid words**, both with proved writhe `0`, which is exactly
`baryon_vacuum_separating`'s writhe-degenerate pair. The honest instantiation is
`S := BraidWord`, `w := writhe`, `B := μ̄₁₂₃`, `baryon := borromean`,
`vacuum := gluonUnit`, discharging `hbw`/`hvw` by `writhe_borromean` /
`writhe_gluon`.

### The one thing blocking that, and it is a real formalisation task

**μ̄₁₂₃ has no definition on braid words anywhere in the Lean tree.** It occurs
only as prose/docstrings and as an **existentially-quantified field of a
conjecture class** — `MilnorVassilievBridge.muBar_realized : ∀ A, 2 ≤ A → ∃ val
: K → ℤ, …`. Milnor invariants are not in Mathlib. So `hbB : B baryon = 1` and
`hvB : B vacuum = 0` cannot be discharged: there is nothing to evaluate.

So this bean is **not one mechanical composition step**. It is blocked on
defining μ̄₁₂₃ (or a computable triple-linking surrogate) on braid words and
proving its two values on `borromean` and `gluonUnit`. Tagged `8f-open`.

**Do not "fix" the bean by writing the missing closer under its stated name** —
`equal_writhe_distinct_Y_forces_non_factoring` would be the `Y` version, which
`qou-h0zz` supersedes and which cannot be typed without a braid-word→charges
map. And note `WritheIndependenceCriterion.lean` already proves the published
p/n argument is a non-sequitur (`pn_test_admits_writhe_only_map`: `Y = w²/4`
returns `+1` on both), with the general criterion deliberately **not** restated
there — its own closing comment points at `factors_through_iff` in
`sm-hypercharge-invariant.lean`. Read that comment before adding anything here.


## Progress Update — 2026-11-16 (`litlfred/qou#8159`, `4a5bd83fa5c08b2011cfb42b8d918e41431e6d96`)

- **Resolved the `μ̄₁₂₃` formalization blocker on `BraidWord` in Lean 4 (`folio/quantum-observable-universe/lean/QOU/Eightfold/MagnusTripleLinkingAndFlavourGradings.lean`, `0` `sorry`, wired into `QOU.lean`)**:
  - Defines the Artin representation `artinBraid : BraidWord → FreeWord3 → FreeWord3` of $B_3$ on the free group $F_3 = \langle x_1, x_2, x_3 \rangle$ with free reduction (`freeReduce`), and proves `borromean_x2_commutator_conjugate`: under `borromean = [1, -2, 1, -2, 1, -2]`, $x_2$ maps to the exact commutator conjugate $[x_1, x_3] x_2 [x_1, x_3]^{-1} = [1, 3, -1, -3, 2, 3, 1, -3, -1]$ (pure commutator 2nd longitude $\ell_2 = [x_1, x_3]$), whereas under `gluonUnit = [1, -2]`, $x_2$ maps to `[1]`.
  - Defines the multilinear truncated Magnus expansion `evalMagnus` in $\mathbb{Z}\langle X_1, X_2, X_3 \rangle / I^4$ and the computable Milnor triple-linking invariant `magnusMuBar123 (β : BraidWord) : Int := (evalMagnus (artinBraid β [2])).c132`.
  - Proves by `decide` (`magnusMuBar123_gluon_and_borromean`): `magnusMuBar123 gluonUnit = 0`, `magnusMuBar123 borromean = 1`, and all degree-2 Magnus coefficients (`c12`, `c23`, `c13`) of `borromean(x_2)` vanish.
  - Proves **unconditionally** (`0` assumed hypotheses) `borromean_gluon_unconditional_separating_pair` (`writhe borromean = writhe gluonUnit ∧ magnusMuBar123 borromean ≠ magnusMuBar123 gluonUnit`) and `magnusMuBar123_not_factoring_through_writhe` (`¬ ∃ f : Int → Int, ∀ β : BraidWord, magnusMuBar123 β = f (writhe β)`).
- **Probe & Witness (`computations/probes/magnus_triple_linking_and_flavour_gradings_probe.py` + `magnus-triple-linking-and-flavour-gradings.witness.json`)**: `allPassed: true` (`q0Anchor: "independent"`).
