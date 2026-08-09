---
# qou-x64l
title: Retire the ASCII H4 basis — it is the subscript basis relabelled, and the permutation is explicit
status: todo
type: task
created_at: 2026-08-09T17:21:10Z
updated_at: 2026-08-09T17:21:10Z
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
   ~6.5k generated lines. `QOU/Hecke/InstanceH4.lean` goes with it — it is built
   on the ASCII actions and qou-ti7p already lists it as a redundant carrier.

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
