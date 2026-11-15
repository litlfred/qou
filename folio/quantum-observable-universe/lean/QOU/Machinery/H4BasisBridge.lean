import QOU.Machinery.MarkovTraceH4
import QOU.Machinery.H4Cyclicity
import QOU.Machinery.HeckeH4AlgebraLaws
import QOU.Machinery.H4AsciiPresentation

/-!
# `QOU.Machinery.H4BasisBridge` — the two `H₄` normal-form bases are one basis

The tree carries two 24-word normal-form bases for `H₄(q)`, and each had exactly
what the other lacked:

| | module | has | lacked |
|---|---|---|---|
| **ASCII** | `MarkovTraceH4` + `MarkovTraceH4Gram0..7` + `H4AsciiPresentation` | `trM`, `gram_symm`, **`trM_cyclic`** | associativity, `Ring` |
| **subscript** | `HeckeH4StabilizationRung` + `HeckeH4AlgebraLaws` | the presentation, `mulNF₄_assoc`, `H4A` `Ring`/`Algebra`, `wedderburn₄` | **cyclicity** |

They are the same basis relabelled. Mapping each reduced word to its `S₄`
element, both lists give the same 24 elements; the index permutation is `piIdx`
below; the trace weights agree under it; and only **6 of 24** words differ at
all, every difference a single far-commutation swap `σ₀σ₂ ↔ σ₂σ₀` — which
`far_commute_σ₀σ₂` proves, so the basis *elements* are equal, not merely the
group elements they index.

`phi` is the relabelling. It intertwines all three generator actions
(`phi_mulσ0/1/2`, depth 1 each), hence every word action (`phi_wordActionA`),
hence the products (**`phi_mulNF`**); and it carries `trM` to `trM4`
(`trM4_phi`). So the missing half transports: **`trM4_cyclic`** — cyclicity on
the subscript basis, with **no second 576-entry Gram closure**.

## The move that makes `phi_mulNF` go through

Both products are 24-term sums over word actions, but the terms correspond
*under `piIdx`*, not position by position. Every attempt that unfolds the two
sums and matches term against term therefore has to permute 24 terms by
rewriting — which `simp` will not do (three failures, postmortem at the foot of
this file). Reindexing does it in one step: put both sides in `Finset.sum` form
(`mulNF_expand_right`, `mulNF₄_expand_right`), carry each term across with
`phi_wordActionA`, and reindex along `piEquiv`. The 24 terms are never written
out.

Bean qou-x64l. Once the consumers move across, the ASCII chain — ~6.5k generated
lines and the tree's build pole, ~4.3 GB peak — can be retired; `trM4_cyclic` is
what they need to move to.

Generated: the permutation and the word correspondence are computed from
`MarkovTraceH4.mulNF` and `HeckeH4AlgebraLaws.wordAction` themselves, so they
cannot drift from the tables they describe.
-/

namespace QOU.Machinery.H4Bridge

open QOU.Machinery.H4

universe u

variable {R : Type u} [CommRing R] (h : R)

/-- ASCII basis index ↦ subscript basis index. -/
def piIdx : Fin 24 → Fin 24 := ![0, 6, 2, 1, 7, 9, 8, 4, 3, 12, 10, 13, 11, 5, 14, 16, 15, 17, 18, 19, 20, 21, 22, 23]

/-- The inverse relabelling. -/
def invIdx : Fin 24 → Fin 24 := ![0, 3, 2, 8, 7, 13, 1, 4, 6, 5, 10, 12, 9, 11, 14, 16, 15, 17, 18, 19, 20, 21, 22, 23]

@[simp] theorem invIdx_piIdx (i : Fin 24) : invIdx (piIdx i) = i := by
  fin_cases i <;> rfl

@[simp] theorem piIdx_invIdx (j : Fin 24) : piIdx (invIdx j) = j := by
  fin_cases j <;> rfl

/-- `piIdx` as an equivalence. This is what lets a 24-term `Finset.sum` be
*reindexed* along the relabelling instead of expanded — the move the whole
product correspondence turns on. -/
def piEquiv : Fin 24 ≃ Fin 24 where
  toFun := piIdx
  invFun := invIdx
  left_inv := invIdx_piIdx
  right_inv := piIdx_invIdx

@[simp] theorem piEquiv_apply (i : Fin 24) : piEquiv i = piIdx i := rfl

/-- Relabel an ASCII coordinate vector into subscript coordinates. -/
def phi (u : Fin 24 → R) : Fin 24 → R := fun j => u (invIdx j)

/-- `phi` is a linear bijection; this is its inverse. -/
def psi (w : Fin 24 → R) : Fin 24 → R := fun i => w (piIdx i)

omit [CommRing R] in
@[simp] theorem psi_phi (u : Fin 24 → R) : psi (phi u) = u := by
  funext i; simp [psi, phi]

omit [CommRing R] in
@[simp] theorem phi_psi (w : Fin 24 → R) : phi (psi w) = w := by
  funext j; simp [psi, phi]

omit [CommRing R] in
@[simp] theorem phi_apply_piIdx (u : Fin 24 → R) (i : Fin 24) :
    phi u (piIdx i) = u i := by simp [phi]

theorem phi_smul (c : R) (u : Fin 24 → R) : phi (c • u) = c • phi u := rfl

theorem phi_sum {ι : Type*} (s : Finset ι) (f : ι → (Fin 24 → R)) :
    phi (∑ k ∈ s, f k) = ∑ k ∈ s, phi (f k) := by
  funext j; simp [phi, Finset.sum_apply]

/-! ## `phi` intertwines the three generator actions

Depth 1 on each side — this is what keeps the whole bridge cheap. -/

theorem phi_mulσ0 (u : Fin 24 → R) : phi (mulσ0 h u) = mulσ₀ h (phi u) := by
  funext j
  fin_cases j <;> simp [phi, invIdx, mulσ0, mulσ₀]

theorem phi_mulσ1 (u : Fin 24 → R) : phi (mulσ1 h u) = mulσ₁ h (phi u) := by
  funext j
  fin_cases j <;> simp [phi, invIdx, mulσ1, mulσ₁]

theorem phi_mulσ2 (u : Fin 24 → R) : phi (mulσ2 h u) = mulσ₂ h (phi u) := by
  funext j
  fin_cases j <;> simp [phi, invIdx, mulσ2, mulσ₂]

/-! ## Hence every word action, by rewriting — never by coordinate expansion -/

omit [CommRing R] in
/-- ASCII word 0 (γ) ↦ subscript word 0 (γ). -/
theorem phi_word_0 (u : Fin 24 → R) :
    phi (u) = phi u := by
  rfl

/-- ASCII word 1 (σ₂) ↦ subscript word 6 (σ₂). -/
theorem phi_word_1 (u : Fin 24 → R) :
    phi (mulσ2 h (u)) = mulσ₂ h (phi u) := by
  simp only [phi_mulσ2]

/-- ASCII word 2 (σ₁) ↦ subscript word 2 (σ₁). -/
theorem phi_word_2 (u : Fin 24 → R) :
    phi (mulσ1 h (u)) = mulσ₁ h (phi u) := by
  simp only [phi_mulσ1]

/-- ASCII word 3 (σ₀) ↦ subscript word 1 (σ₀). -/
theorem phi_word_3 (u : Fin 24 → R) :
    phi (mulσ0 h (u)) = mulσ₀ h (phi u) := by
  simp only [phi_mulσ0]

/-- ASCII word 4 (σ₁σ₂) ↦ subscript word 7 (σ₁σ₂). -/
theorem phi_word_4 (u : Fin 24 → R) :
    phi (mulσ2 h (mulσ1 h (u))) = mulσ₂ h (mulσ₁ h (phi u)) := by
  simp only [phi_mulσ1, phi_mulσ2]

/-- ASCII word 5 (σ₂σ₁) ↦ subscript word 9 (σ₂σ₁). -/
theorem phi_word_5 (u : Fin 24 → R) :
    phi (mulσ1 h (mulσ2 h (u))) = mulσ₁ h (mulσ₂ h (phi u)) := by
  simp only [phi_mulσ1, phi_mulσ2]

/-- ASCII word 6 (σ₂σ₀) ↦ subscript word 8 (σ₂σ₀). -/
theorem phi_word_6 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ2 h (u))) = mulσ₀ h (mulσ₂ h (phi u)) := by
  simp only [phi_mulσ0, phi_mulσ2]

/-- ASCII word 7 (σ₀σ₁) ↦ subscript word 4 (σ₀σ₁). -/
theorem phi_word_7 (u : Fin 24 → R) :
    phi (mulσ1 h (mulσ0 h (u))) = mulσ₁ h (mulσ₀ h (phi u)) := by
  simp only [phi_mulσ0, phi_mulσ1]

/-- ASCII word 8 (σ₁σ₀) ↦ subscript word 3 (σ₁σ₀). -/
theorem phi_word_8 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ1 h (u))) = mulσ₀ h (mulσ₁ h (phi u)) := by
  simp only [phi_mulσ0, phi_mulσ1]

/-- ASCII word 9 (σ₁σ₂σ₁) ↦ subscript word 12 (σ₁σ₂σ₁). -/
theorem phi_word_9 (u : Fin 24 → R) :
    phi (mulσ1 h (mulσ2 h (mulσ1 h (u)))) = mulσ₁ h (mulσ₂ h (mulσ₁ h (phi u))) := by
  simp only [phi_mulσ1, phi_mulσ2]

/-- ASCII word 10 (σ₀σ₁σ₂) ↦ subscript word 10 (σ₀σ₁σ₂). -/
theorem phi_word_10 (u : Fin 24 → R) :
    phi (mulσ2 h (mulσ1 h (mulσ0 h (u)))) = mulσ₂ h (mulσ₁ h (mulσ₀ h (phi u))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 11 (σ₂σ₀σ₁) ↦ subscript word 13 (σ₂σ₀σ₁). -/
theorem phi_word_11 (u : Fin 24 → R) :
    phi (mulσ1 h (mulσ0 h (mulσ2 h (u)))) = mulσ₁ h (mulσ₀ h (mulσ₂ h (phi u))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 12 (σ₁σ₂σ₀) ↦ subscript word 11 (σ₁σ₀σ₂) — one `σ₀σ₂` swap. -/
theorem phi_word_12 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ2 h (mulσ1 h (u)))) = mulσ₂ h (mulσ₀ h (mulσ₁ h (phi u))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]
  rw [far_commute_σ₀σ₂]

/-- ASCII word 13 (σ₀σ₁σ₀) ↦ subscript word 5 (σ₀σ₁σ₀). -/
theorem phi_word_13 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ1 h (mulσ0 h (u)))) = mulσ₀ h (mulσ₁ h (mulσ₀ h (phi u))) := by
  simp only [phi_mulσ0, phi_mulσ1]

/-- ASCII word 14 (σ₂σ₁σ₀) ↦ subscript word 14 (σ₂σ₁σ₀). -/
theorem phi_word_14 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ1 h (mulσ2 h (u)))) = mulσ₀ h (mulσ₁ h (mulσ₂ h (phi u))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 15 (σ₀σ₁σ₂σ₁) ↦ subscript word 16 (σ₀σ₁σ₂σ₁). -/
theorem phi_word_15 (u : Fin 24 → R) :
    phi (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (u))))) = mulσ₁ h (mulσ₂ h (mulσ₁ h (mulσ₀ h (phi u)))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 16 (σ₀σ₁σ₂σ₀) ↦ subscript word 15 (σ₀σ₁σ₀σ₂) — one `σ₀σ₂` swap. -/
theorem phi_word_16 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (u))))) = mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h (phi u)))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]
  rw [far_commute_σ₀σ₂]

/-- ASCII word 17 (σ₁σ₂σ₀σ₁) ↦ subscript word 17 (σ₁σ₀σ₂σ₁) — one `σ₀σ₂` swap. -/
theorem phi_word_17 (u : Fin 24 → R) :
    phi (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (u))))) = mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h (phi u)))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]
  rw [far_commute_σ₀σ₂]

/-- ASCII word 18 (σ₁σ₂σ₁σ₀) ↦ subscript word 18 (σ₁σ₂σ₁σ₀). -/
theorem phi_word_18 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (u))))) = mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₁ h (phi u)))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 19 (σ₂σ₀σ₁σ₀) ↦ subscript word 19 (σ₂σ₀σ₁σ₀). -/
theorem phi_word_19 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (u))))) = mulσ₀ h (mulσ₁ h (mulσ₀ h (mulσ₂ h (phi u)))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 20 (σ₀σ₁σ₂σ₀σ₁) ↦ subscript word 20 (σ₀σ₁σ₀σ₂σ₁) — one `σ₀σ₂` swap. -/
theorem phi_word_20 (u : Fin 24 → R) :
    phi (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (u)))))) = mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h (phi u))))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]
  rw [far_commute_σ₀σ₂]

/-- ASCII word 21 (σ₀σ₁σ₂σ₁σ₀) ↦ subscript word 21 (σ₀σ₁σ₂σ₁σ₀). -/
theorem phi_word_21 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ1 h (mulσ2 h (mulσ1 h (mulσ0 h (u)))))) = mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₁ h (mulσ₀ h (phi u))))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]

/-- ASCII word 22 (σ₁σ₂σ₀σ₁σ₀) ↦ subscript word 22 (σ₁σ₀σ₂σ₁σ₀) — one `σ₀σ₂` swap. -/
theorem phi_word_22 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (u)))))) = mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h (phi u))))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]
  rw [far_commute_σ₀σ₂]

/-- ASCII word 23 (σ₀σ₁σ₂σ₀σ₁σ₀) ↦ subscript word 23 (σ₀σ₁σ₀σ₂σ₁σ₀) — one `σ₀σ₂` swap. -/
theorem phi_word_23 (u : Fin 24 → R) :
    phi (mulσ0 h (mulσ1 h (mulσ0 h (mulσ2 h (mulσ1 h (mulσ0 h (u))))))) = mulσ₀ h (mulσ₁ h (mulσ₂ h (mulσ₀ h (mulσ₁ h (mulσ₀ h (phi u)))))) := by
  simp only [phi_mulσ0, phi_mulσ1, phi_mulσ2]
  rw [far_commute_σ₀σ₂]

/-! ## The traces correspond -/

theorem trM4_phi (z : R) (u : Fin 24 → R) : trM4 z h (phi u) = trM z h u := by
  simp only [trM, trM4, TRM, TRM4, phi, invIdx, Fin.sum_univ_succ, Fin.sum_univ_zero]
  simp
  ring

/-! ## Far-commutation on the ASCII side

`simp` rewrites innermost-first, so the three intertwiners collapse a subscript
composite to `phi (…)` one generator at a time — producing the *subscript* word
shape. For the 6 words where the two bases differ that is not the ASCII word, and
the two sides no longer match. Normalising needs `σ₀σ₂ = σ₂σ₀` on the ASCII
generators as well: `QOU.Machinery.H4.mulσ_farcomm02`, imported above, whose
subscript counterpart is `HeckeH4StabilizationRung.far_commute_σ₀σ₂`. (This file
carried its own copy until bean qou-ti7p folded the whole ASCII presentation into
`H4AsciiPresentation`.) -/

/-! ## The word actions correspond, as functions of the index

`phi_word_0 … phi_word_23` say the same thing one index at a time. Packaged
against `wordActionA` / `wordAction` — the two tables' right basis actions — the
statement becomes a single equation in `k`, which is what a `Finset.sum` can be
reindexed by. -/

theorem phi_wordActionA (k : Fin 24) (u : Fin 24 → R) :
    phi (wordActionA h k u) = wordAction h (piIdx k) (phi u) := by
  fin_cases k <;> simp only [wordActionA, wordAction, piIdx]
  exacts [rfl, phi_mulσ2 h u, phi_mulσ1 h u, phi_mulσ0 h u,
    phi_word_4 h u, phi_word_5 h u, phi_word_6 h u, phi_word_7 h u, phi_word_8 h u,
    phi_word_9 h u, phi_word_10 h u, phi_word_11 h u, phi_word_12 h u, phi_word_13 h u,
    phi_word_14 h u, phi_word_15 h u, phi_word_16 h u, phi_word_17 h u, phi_word_18 h u,
    phi_word_19 h u, phi_word_20 h u, phi_word_21 h u, phi_word_22 h u, phi_word_23 h u]

/-! ## The product correspondence

The step three `simp`-based attempts could not reach — see the postmortem below.
It goes through by never writing the 24 terms out: both products become a
`Finset.sum` over the basis (`mulNF_expand_right`, `mulNF₄_expand_right`), `phi`
passes through the sum termwise, each term is carried across by
`phi_wordActionA`, and the sum is *reindexed* along `piEquiv`. The coefficient
bookkeeping is the one line `phi v (piIdx k) = v k` — which is `phi`'s
definition composed with `invIdx_piIdx`, not a computation. -/

theorem phi_mulNF (u v : Fin 24 → R) :
    phi (mulNF h u v) = mulNF₄ h (phi u) (phi v) := by
  rw [mulNF_expand_right, mulNF₄_expand_right, phi_sum]
  have step : ∀ k : Fin 24, phi (v k • wordActionA h k u)
      = (fun j => phi v j • wordAction h j (phi u)) (piEquiv k) := fun k => by
    rw [phi_smul, phi_wordActionA]
    simp
  rw [Finset.sum_congr rfl fun k _ => step k]
  exact Equiv.sum_comp piEquiv (fun j => phi v j • wordAction h j (phi u))

/-! ## Cyclicity transports — now in the other direction

**This arrow used to run ASCII → subscript**, deriving `trM4_cyclic` from the
ASCII `trM_cyclic`, which rested on `gram_symm`'s 576 computed entries. That is
why the Gram chain stayed alive: it was the only proof of cyclicity at `n = 4`.

`QOU.Machinery.H4.trM4_cyclic` (`H4Cyclicity`) now proves cyclicity directly on
the subscript basis, from the three generators and the subalgebra argument, with
no Gram closure anywhere. So the transport runs **subscript → ASCII**, and the
576 entries are dead weight — `MarkovTraceH4Gram0..7` and `MarkovTraceH4Gram`
(6604 generated lines, the tree's build pole) are deleted in the same commit.

Nothing downstream loses a theorem: `H4.trM4_cyclic` replaces this file's own
former `trM4_cyclic` (one canonical statement rather than two proofs of it), and
`H4.trM_cyclic` below is the ASCII statement, re-proved as a corollary. -/

/-- **ASCII-basis cyclicity, as a corollary of the subscript proof.**

Formerly `MarkovTraceH4Gram.trM_cyclic`, proved from `gram_symm`'s 576 entries.
The bridge carries products to products and `trM` to `trM4`, so it now follows
from `H4.trM4_cyclic` in three rewrites. Kept under its original fully-qualified
name `QOU.Machinery.H4.trM_cyclic` so nothing has to be renamed to find it. -/
theorem _root_.QOU.Machinery.H4.trM_cyclic (z : R) (u v : Fin 24 → R) :
    trM z h (mulNF h u v) = trM z h (mulNF h v u) := by
  rw [← trM4_phi, ← trM4_phi, phi_mulNF, phi_mulNF]
  exact QOU.Machinery.H4.trM4_cyclic z h (phi u) (phi v)

/-! ## Postmortem: three `simp` routes that do not work

Kept because the failures are instructive about *why* the structured route is
the right one, not merely that it is.

1. **`phi` in the same `simp only` as `← phi_word_*`.** `phi` unfolds first and
   destroys the rewrite patterns.
2. **Two passes: `simp only [mulNF₄, ← phi_word_*]`, then unfold.** The
   unused-simp-args linter reports **all 24 `phi_word_*` as unused** — they never
   fire. Diagnosis: `simp` rewrites innermost-first, so `← phi_mulσ*` (which are
   `phi_word_1/2/3` in disguise) collapse each composite one generator at a time,
   yielding the *subscript* word shape; for the 6 words where the bases differ
   that is not the ASCII word, so the longer lemmas never match.
3. **Adding `mulσ_farcomm02` to normalise those 6.** Still fails, and worse: the
   right-hand side comes out with **70 terms instead of 24**, carrying
   coefficients indexed by `invIdx j` rather than by literals — `simp` is
   mangling the coefficient vector, not merely failing to rewrite.

All three unfold `mulNF`/`mulNF₄` into their 24 inline terms and then try to
match term against term. But the two tables' terms are *not* in correspondence
position-by-position — they correspond under `piIdx` — so any tactic that
rewrites in place has to permute 24 terms by rewriting, which `simp` will not do
and `ring` cannot see through the generator actions. Reindexing a `Finset.sum`
does it in one step. Bean qou-x64l.
-/

end QOU.Machinery.H4Bridge
