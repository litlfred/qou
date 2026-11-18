import QOU.BraidKnot.CompositionYoung
import QOU.BraidKnot.HeckeMurphy

/-!
# `x_μ` for a **composition**, and its eigenvector property

Mathas' Lemma 3.9 — the foundation of the Murphy-basis spanning argument — is stated
for a *composition* `μ`, not a partition.  `QOU.BraidKnot.HeckeMurphy.murphySum` builds
`x_S` for an arbitrary `Finset` of permutations and proves it is a `q`-eigenvector for
any subgroup, so the composition case costs nothing once the *subgroup* exists — which
is what `CompositionYoung.youngOfComp` supplies.

What this file adds is the translation of the eigenvector hypothesis into the
composition's own terms.  `HeckeMurphy.σ_mul_murphySum_subgroup` asks for
`sw i ∈ H`, an opaque condition on a permutation; `mem_youngOfComp_sw` turns it into
the statement it should be — **`i` and `i+1` lie in the same block of `μ`** — which is
how Mathas states it and the only form usable when `μ` is given by its parts.
-/

namespace QOU.BraidKnot.CompositionMurphy

open QOU.BraidKnot.CompositionYoung QOU.BraidKnot.HeckeMurphy Equiv

variable (K : Type*) [Field K] (q : K) {n : ℕ}

/-- Membership of a **simple transposition** in a composition's Young subgroup is
exactly the statement that the two labels it swaps share a block.

The reverse direction is where the content is: a transposition fixes the block
function everywhere outside the two points it moves, so agreement at those two points
is all that is needed. -/
theorem mem_youngOfComp_sw {c : Composition (n + 1)} {i : Fin n} :
    sw i ∈ youngOfComp c ↔ c.index i.castSucc = c.index i.succ := by
  rw [mem_youngOfComp]
  constructor
  · intro h
    have := h i.succ
    rwa [Equiv.symm_swap, Equiv.swap_apply_right] at this
  · intro h l
    rw [Equiv.symm_swap]
    rcases eq_or_ne l i.castSucc with rfl | h1
    · rw [Equiv.swap_apply_left]; exact h.symm
    rcases eq_or_ne l i.succ with rfl | h2
    · rw [Equiv.swap_apply_right]; exact h
    · rw [Equiv.swap_apply_of_ne_of_ne h1 h2]

/-- **Murphy's `x_μ` for a composition**: the sum of `T_w` over the Young subgroup of
`μ`.  For `μ` a partition this is the usual `x_λ`; the point is that it is defined
without one. -/
noncomputable def xComp (c : Composition (n + 1))
    [DecidablePred (· ∈ youngOfComp c)] : QOU.Hecke.IwahoriHecke K q n :=
  murphySum K q n {w | w ∈ youngOfComp c}

/-- **The eigenvector property, in the composition's own terms.**

`σ_i · x_μ = q · x_μ` whenever `i` and `i+1` share a block of `μ` — i.e. for every
simple reflection *inside* a part, which is the generating set of `S_μ`.

The algebra is entirely `HeckeMurphy.σ_mul_murphySum_subgroup`; what this supplies is
the hypothesis in a form that can be checked from the parts of `μ`. -/
theorem σ_mul_xComp (c : Composition (n + 1)) [DecidablePred (· ∈ youngOfComp c)]
    (i : Fin n) (hblock : c.index i.castSucc = c.index i.succ) :
    QOU.Hecke.IwahoriHecke.σ K q n i * xComp K q c = q • xComp K q c :=
  σ_mul_murphySum_subgroup K q n i _ (mem_youngOfComp_sw.mpr hblock)

/-- The same on the right — `x_μ · σ_i = q · x_μ`, the two-sided statement Murphy's
`m_{st} = T_{d(s)}^* x_μ T_{d(t)}` needs. -/
theorem xComp_mul_σ (c : Composition (n + 1)) [DecidablePred (· ∈ youngOfComp c)]
    (i : Fin n) (hblock : c.index i.castSucc = c.index i.succ) :
    xComp K q c * QOU.Hecke.IwahoriHecke.σ K q n i = q • xComp K q c :=
  murphySum_mul_σ_subgroup K q n i _ (mem_youngOfComp_sw.mpr hblock)

/-- Subtracting the scalar multiple of the Murphy element from the generator product cancels to zero (`qou-ip2a`). -/
theorem σ_mul_xComp_sub_eq_zero (c : Composition (n + 1)) [DecidablePred (· ∈ youngOfComp c)]
    (i : Fin n) (hblock : c.index i.castSucc = c.index i.succ) :
    QOU.Hecke.IwahoriHecke.σ K q n i * xComp K q c - q • xComp K q c = 0 := by
  rw [σ_mul_xComp K q c i hblock, sub_self]

end QOU.BraidKnot.CompositionMurphy
