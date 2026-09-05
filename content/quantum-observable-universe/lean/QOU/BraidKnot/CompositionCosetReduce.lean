import QOU.BraidKnot.CompositionEigenPower
import QOU.BraidKnot.CompositionCosetSum

/-!
# The coset reduction: `x_μ · T_a` collapses onto the distinguished representative

This is the step Mathas' Lemma 3.9 performs when it replaces an arbitrary index by a
coset representative:

    `x_μ · T_a = q^{ℓ(v)} · (x_μ · T_e)`,   `a = e·v`, `e ∈ D_μ`, `v ∈ S_μ`

So the family `{x_μ · T_a : a ∈ S_n}` — which has `n!` members — spans the same thing as
`{x_μ · T_e : e ∈ D_μ}`, one per coset, with every ratio a **power of `q`** and nothing
else.  Together with `CompositionCosetSum.linearIndependent_xComp_mul_Tw` (those `x_μ T_e`
are independent) this is the structure of the right module `x_μ H`.

## The three inputs, and why each is needed

* `CompositionCosetSum.existsUnique_isDistinguishedL` — Prop 3.3, left-coset form: the
  factorisation `a = e·v` exists and `e` is unique.
* `CompositionCosetSum.length_mul_eq_add_of_isDistinguishedL` — the lengths add, which is
  what lets `Tw_mul_Tw` fire at all.
* `CompositionEigenPower.xComp_mul_Tw_of_mem` — `x_μ · T_v = q^{ℓ(v)} · x_μ` for the whole
  Young subgroup, not merely its generators.

## Handedness, once more

`Tw_mul_Tw` is flipped (`T_v · T_w = T_{w·v}`), so the factor that ends up **adjacent to
`x_μ`** is `T_v`, the Young-subgroup part — which is exactly the one the eigenvector
property can absorb.  That is why the reduction is stated on the **left** coset `e·S_μ`
with `e⁻¹` distinguished (`IsDistinguishedL`), and not on the right coset.  With the other
orientation the `T_v` lands on the far side of `T_e` and nothing collapses.
-/

namespace QOU.BraidKnot.CompositionCosetReduce

open QOU.BraidKnot.CompositionYoung QOU.BraidKnot.CompositionMinimal
open QOU.BraidKnot.CompositionMurphy QOU.BraidKnot.HeckeMurphy
open QOU.BraidKnot.CompositionCosetSum QOU.BraidKnot.CompositionEigenPower
open QOU.Hecke.SymmetricCoxeter QOU.Hecke.TwBasis Equiv

variable {n : ℕ} (K : Type*) [Field K] (q : K)

/-- **The coset reduction.**  Every `x_μ · T_a` is a `q`-power multiple of the one
attached to `a`'s distinguished representative. -/
theorem xComp_mul_Tw_reduce (c : Composition (n + 1))
    [DecidablePred (· ∈ youngOfComp c)] (a : Perm (Fin (n + 1))) :
    ∃ e v : Perm (Fin (n + 1)),
      IsDistinguishedL c e ∧ v ∈ youngOfComp c ∧ a = e * v ∧
        xComp K q c * Tw K q n a
          = q ^ ((permCoxeterSystem n).length v) • (xComp K q c * Tw K q n e) := by
  obtain ⟨e, ⟨he, hem⟩, -⟩ := existsUnique_isDistinguishedL c a
  -- `a⁻¹ · e ∈ S_μ`, so `v := e⁻¹ · a` is too, and `a = e · v`
  refine ⟨e, e⁻¹ * a, he, ?_, ?_, ?_⟩
  · have : (a⁻¹ * e)⁻¹ ∈ youngOfComp c := inv_mem hem
    simpa [mul_inv_rev] using this
  · group
  · have hv : e⁻¹ * a ∈ youngOfComp c := by
      have : (a⁻¹ * e)⁻¹ ∈ youngOfComp c := inv_mem hem
      simpa [mul_inv_rev] using this
    have hfac : e * (e⁻¹ * a) = a := by group
    -- the lengths add, so `Tw_mul_Tw` applies
    have hlen := length_mul_eq_add_of_isDistinguishedL he hv
    have hTw : Tw K q n a = Tw K q n (e⁻¹ * a) * Tw K q n e := by
      have h := Tw_mul_Tw K q n (e⁻¹ * a) e hlen
      rw [hfac] at h
      exact h.symm
    rw [hTw, ← mul_assoc, xComp_mul_Tw_of_mem K q c hv, smul_mul_assoc]

end QOU.BraidKnot.CompositionCosetReduce
