import QOU.BraidKnot.RowStandardTableau
import QOU.BraidKnot.SytMathlibBridge
import QOU.Hecke.LengthAdditive

/-!
# `d(t)`: the permutation carrying the reference tableau to `t`

Murphy's basis is `m_{st} = T_{d(s)}^* · x_λ · T_{d(t)}`, so **every statement in
that construction is indexed by a permutation attached to a tableau**, and
`QOU.BraidKnot` has had no such map.  This file supplies it.

`Specht.Tableau μ` is `Fin n ≃ μ.cells` with `σ • t = t ∘ σ⁻¹`, and the action is
simply transitive: fixing the row-superstandard tableau `t^μ` as origin, every
tableau is `d • t^μ` for exactly one `d`.  That `d` is `dOf t`.

## Why this is the piece that was missing

Mathas' Lemma 3.13 — the one ingredient of the Murphy spanning argument with no
`q = 1` antecedent in the corpus — reads: for a row-standard non-standard `t`
there are a Garnir tableau `g` and `w` with `t = g · w` and

  `ℓ(d(t)) = ℓ(d(g)) + ℓ(w)`.

`dOf_smul` below turns the *tableau* factorisation `t = w • g` into the
*permutation* factorisation `d(t) = w * d(g)`, which is exactly the input
`QOU.Hecke.Inversions.length_mul_eq_add_iff` consumes.  Composing the two
(`length_dOf_smul_eq_add_iff`) reduces Mathas' length condition to a concrete,
decidable combinatorial claim:

  **no inversion of `d(g)` is undone by `w`.**

What is still absent, and is not attempted here: the Garnir tableau `g_{ij}`
itself and the descent-node ordering.  This file is the bridge, not the lemma —
it makes the length half of 3.13 statable, and says nothing about which `g`
realises it.  Measured support for the target it feeds:
`computations/hecke/murphy_garnir_length_additivity_probe.py` finds the *first*
descent node sufficient in **1789/1789** row-standard non-standard tableaux for
`n = 3,4,5,6`.
-/

open Equiv Finset

namespace QOU.BraidKnot.TableauPerm

variable {μ : YoungDiagram}

/-! ### The reference tableau and `d(t)` -/

/-- The **row-superstandard tableau** `t^μ`, used as the origin of the `S_n`-action
on `μ`-tableaux. -/
noncomputable def refTab (μ : YoungDiagram) : Specht.Tableau μ :=
  QOU.BraidKnot.SpechtStandardBasis.sytToTableau (QOU.BraidKnot.rowSuperstandardBraidKnot μ)

/-- **`d(t)`** — the permutation carrying the reference tableau to `t`.

As an `Equiv` this is `t^μ` followed by `t⁻¹`; `smul_refTab` below is the
characterising property. -/
noncomputable def dOf (t : Specht.Tableau μ) : Perm (Fin (Specht.nOf μ)) :=
  (refTab μ).trans t.symm

@[simp] theorem dOf_apply (t : Specht.Tableau μ) (l : Fin (Specht.nOf μ)) :
    dOf t l = t.symm (refTab μ l) := rfl

/-- **The defining property**: `d(t)` carries the reference tableau to `t`. -/
@[simp] theorem smul_refTab (t : Specht.Tableau μ) : dOf t • refTab μ = t := by
  refine Equiv.ext fun l => ?_
  show (refTab μ) ((dOf t).symm l) = t l
  have h : (dOf t).symm l = (refTab μ).symm (t l) := by
    simp [dOf, Equiv.symm_trans_apply]
  rw [h, Equiv.apply_symm_apply]

/-- **Uniqueness**: nothing else carries the reference tableau to `t`. -/
theorem dOf_unique {t : Specht.Tableau μ} {σ : Perm (Fin (Specht.nOf μ))}
    (h : σ • refTab μ = t) : σ = dOf t := by
  refine Equiv.ext fun x => ?_
  have hx : (refTab μ) (σ.symm (σ x)) = t (σ x) := by
    rw [← h]; rfl
  rw [Equiv.symm_apply_apply] at hx
  show σ x = t.symm (refTab μ x)
  rw [hx, Equiv.symm_apply_apply]

@[simp] theorem dOf_refTab : dOf (refTab μ) = 1 := by
  refine (dOf_unique ?_).symm
  exact one_smul _ _

/-- **The factorisation bridge.**  A tableau factorisation `t = w • g` becomes the
permutation factorisation `d(t) = w * d(g)`.

This is what lets a statement about tableaux be handed to
`QOU.Hecke.Inversions.length_mul_eq_add_iff`. -/
theorem dOf_smul (w : Perm (Fin (Specht.nOf μ))) (g : Specht.Tableau μ) :
    dOf (w • g) = w * dOf g := by
  refine (dOf_unique ?_).symm
  rw [mul_smul, smul_refTab]

/-- `dOf` is injective: a tableau is determined by its permutation. -/
theorem dOf_injective : Function.Injective (dOf (μ := μ)) := by
  intro s t h
  rw [← smul_refTab s, ← smul_refTab t, h]

/-- `dOf` recovers the acting permutation: `d(σ • t^μ) = σ`. -/
@[simp] theorem dOf_smul_refTab (σ : Perm (Fin (Specht.nOf μ))) :
    dOf (σ • refTab μ) = σ := by
  rw [dOf_smul, dOf_refTab, mul_one]

theorem dOf_surjective : Function.Surjective (dOf (μ := μ)) :=
  fun σ => ⟨σ • refTab μ, dOf_smul_refTab σ⟩

/-- **The action is simply transitive**: `dOf` is a bijection from `μ`-tableaux to
permutations.

This is the non-vacuity statement for everything above — `dOf` is not merely
*some* map to permutations, it identifies the two sets, so a claim about `d(t)`
is a claim about every permutation and vice versa. -/
noncomputable def equivPerm : Specht.Tableau μ ≃ Perm (Fin (Specht.nOf μ)) :=
  Equiv.ofBijective dOf ⟨dOf_injective, dOf_surjective⟩

@[simp] theorem equivPerm_apply (t : Specht.Tableau μ) : equivPerm t = dOf t := rfl

/-! ### Transport to `Fin (n+1)`

`QOU.Hecke.Inversions` works over `Fin (n+1)` (that is where the Coxeter system
`permCoxeterSystem` lives), while a tableau's permutation lives over
`Fin (nOf μ)`.  For a diagram with at least one cell the two agree up to the
evident cast, and `toFinSucc` carries permutations across it. -/

/-- The cast `Perm (Fin (nOf μ)) ≃ Perm (Fin (n+1))` induced by `nOf μ = n + 1`. -/
def toFinSucc {n : ℕ} (hn : Specht.nOf μ = n + 1) :
    Perm (Fin (Specht.nOf μ)) ≃ Perm (Fin (n + 1)) :=
  Equiv.permCongr (finCongr hn)

@[simp] theorem toFinSucc_mul {n : ℕ} (hn : Specht.nOf μ = n + 1)
    (a b : Perm (Fin (Specht.nOf μ))) :
    toFinSucc hn (a * b) = toFinSucc hn a * toFinSucc hn b := by
  refine Equiv.ext fun x => ?_
  simp [toFinSucc, Equiv.permCongr_apply, Equiv.Perm.mul_apply]

/-! ### Mathas' length condition, reduced to inversion containment -/

/-- **The length half of Mathas 3.13, as a combinatorial criterion.**

For a tableau factorisation `t = w • g`, the length is additive —
`ℓ(d(t)) = ℓ(w) + ℓ(d(g))` — **exactly when `w` undoes none of `d(g)`'s
inversions**.

The right-hand side is decidable and mentions no lengths and no reduced words,
which is what makes it checkable for a proposed Garnir tableau. -/
theorem length_dOf_smul_eq_add_iff {n : ℕ} (hn : Specht.nOf μ = n + 1)
    (w : Perm (Fin (Specht.nOf μ))) (g : Specht.Tableau μ) :
    (QOU.Hecke.SymmetricCoxeter.permCoxeterSystem n).length (toFinSucc hn (dOf (w • g)))
        = (QOU.Hecke.SymmetricCoxeter.permCoxeterSystem n).length (toFinSucc hn w)
          + (QOU.Hecke.SymmetricCoxeter.permCoxeterSystem n).length (toFinSucc hn (dOf g))
      ↔ QOU.Hecke.Inversions.invSet (toFinSucc hn (dOf g))
          ⊆ QOU.Hecke.Inversions.invSet (toFinSucc hn (dOf (w • g))) := by
  rw [dOf_smul, toFinSucc_mul]
  exact QOU.Hecke.Inversions.length_mul_eq_add_iff _ _

end QOU.BraidKnot.TableauPerm
