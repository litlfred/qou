import QOU.BraidKnot.CompositionCosetExists

/-!
# `x_μ · T_v = q^{ℓ(v)} · x_μ` for `v` in the Young subgroup

`CompositionMurphy.xComp_mul_σ` is the defining eigenvector property of the Murphy element
at a single **generator** lying in a block: `x_μ · σᵢ = q · x_μ`.  Mathas' Lemma 3.9 needs
it for an arbitrary `v ∈ S_μ`, which is what this file supplies.

    `x_μ · T_v = q^{ℓ(v)} · x_μ`   for every `v ∈ S_μ`

## Why this is not just "iterate the generator case"

The tempting proof — write `v` as a product of simple reflections and iterate — needs every
letter of some reduced word for `v` to lie **inside the block set**.  That is the standard
parabolic fact (a parabolic subgroup is Coxeter on the simple reflections it contains), and
the corpus does **not** have it: `CoxeterParabolicCoset.parabolic` is defined as
`Subgroup.closure (cs.simple '' J)`, and only the easy direction
(`wordProd_mem_parabolic`) is proved.

The route taken here avoids it. The observation is that

**an element of a Young subgroup can only descend *within* a block** (`descent_index_eq`).

If `v` descended across a block boundary at `i`, then `c.index (v i.castSucc) <
c.index (v i.succ)` — because `v` preserves blocks — and `CompositionMinimal.lt_of_index_lt`
turns that straight back into `v i.castSucc < v i.succ`, contradicting the descent.  So every
descent of `v` is automatically at a generator of `S_μ`, and Mathlib's
`exists_rightDescent_of_ne_one` supplies one whenever `v ≠ 1`.  The induction on `ℓ(v)` then
never has to ask which letters a reduced word uses.
-/

namespace QOU.BraidKnot.CompositionEigenPower

open QOU.BraidKnot.CompositionYoung QOU.BraidKnot.CompositionMinimal
open QOU.BraidKnot.CompositionMurphy QOU.BraidKnot.HeckeMurphy
open QOU.Hecke.SymmetricCoxeter QOU.Hecke.TwBasis QOU.Hecke.Inversions
open QOU.Hecke.IwahoriHecke Equiv

variable {n : ℕ}

/-- **A Young-subgroup element can only descend inside a block.**  This is what removes the
need for the parabolic-generation fact. -/
theorem descent_index_eq {c : Composition (n + 1)} {v : Perm (Fin (n + 1))}
    (hv : v ∈ youngOfComp c) {i : Fin n} (hdesc : v i.succ < v i.castSucc) :
    c.index i.castSucc = c.index i.succ := by
  by_contra hne
  -- positions ascend, so their block indices cannot strictly descend
  have hle : c.index i.castSucc ≤ c.index i.succ := by
    by_contra hgt
    exact absurd (lt_of_index_lt c (not_le.mp hgt)) (not_lt.mpr (Fin.castSucc_lt_succ i).le)
  have hlt : c.index i.castSucc < c.index i.succ := lt_of_le_of_ne hle hne
  -- `v` preserves blocks, so the images' indices are still strictly ordered
  have h1 : c.index (v i.castSucc) = c.index i.castSucc := index_apply_of_mem hv _
  have h2 : c.index (v i.succ) = c.index i.succ := index_apply_of_mem hv _
  have hii : c.index (v i.castSucc) < c.index (v i.succ) := by rw [h1, h2]; exact hlt
  exact absurd (lt_of_index_lt c hii) (by omega)

variable (K : Type*) [Field K] (q : K)

/-- **The Murphy element is a `q^ℓ`-eigenvector for the whole Young subgroup**, not merely
for its generators. -/
theorem xComp_mul_Tw_of_mem (c : Composition (n + 1))
    [DecidablePred (· ∈ youngOfComp c)] {v : Perm (Fin (n + 1))}
    (hv : v ∈ youngOfComp c) :
    xComp K q c * Tw K q n v
      = q ^ ((permCoxeterSystem n).length v) • xComp K q c := by
  generalize hk : (permCoxeterSystem n).length v = k
  induction k using Nat.strong_induction_on generalizing v with
  | _ k ih =>
    by_cases hone : v = 1
    · subst hone
      simp [Tw_one, ← hk]
    · -- a right descent exists, and it is automatically a block generator
      obtain ⟨i, hi⟩ := (permCoxeterSystem n).exists_rightDescent_of_ne_one hone
      have hlt : (permCoxeterSystem n).length (v * sw i)
          < (permCoxeterSystem n).length v := by
        rw [← simple_eq_sw]
        have h := (permCoxeterSystem n).isRightDescent_iff.mp hi
        omega
      -- read the descent concretely off the inversion-count step lemma
      have hdesc : v i.succ < v i.castSucc := by
        rcases invCount_mul_swap v i with ⟨-, hup⟩ | ⟨hdown, -⟩
        · rw [length_eq_invCount, length_eq_invCount, sw, hup] at hlt; omega
        · exact hdown
      have hblock : c.index i.castSucc = c.index i.succ := descent_index_eq hv hdesc
      have hsw : sw i ∈ youngOfComp c := mem_youngOfComp_sw.mpr hblock
      have hv' : v * sw i ∈ youngOfComp c := mul_mem hv hsw
      -- lengths: `ℓ(v) = ℓ(v · sᵢ) + 1`
      have hstep : (permCoxeterSystem n).length v
          = (permCoxeterSystem n).length (v * sw i) + 1 := by
        have h := (permCoxeterSystem n).length_mul_simple v i
        rw [simple_eq_sw] at h
        omega
      -- `T_v = σᵢ · T_{v·sᵢ}`, by `Tw_mul_Tw` with the lengths adding
      have hTw : Tw K q n v = σ K q n i * Tw K q n (v * sw i) := by
        have hmul : Tw K q n (sw i) * Tw K q n (v * sw i)
            = Tw K q n (v * sw i * sw i) := by
          refine Tw_mul_Tw K q n (sw i) (v * sw i) ?_
          rw [mul_sw_sw]
          have hs : (permCoxeterSystem n).length (sw i) = 1 := by
            rw [← simple_eq_sw]; exact (permCoxeterSystem n).length_simple i
          omega
        rw [mul_sw_sw] at hmul
        rw [← hmul, Tw_sw]
      rw [hTw, ← mul_assoc, xComp_mul_σ K q c i hblock, smul_mul_assoc,
        ih _ (hk ▸ hlt) hv' rfl, smul_smul, ← hk, hstep]
      ring_nf

/-- Subtracting the length-scaled Murphy element from the right product cancels to zero (`qou-hrwd`). -/
theorem xComp_mul_Tw_sub_eq_zero (c : Composition (n + 1))
    [DecidablePred (· ∈ youngOfComp c)] {v : Perm (Fin (n + 1))}
    (hv : v ∈ youngOfComp c) :
    xComp K q c * Tw K q n v
      - q ^ ((permCoxeterSystem n).length v) • xComp K q c = 0 := by
  rw [xComp_mul_Tw_of_mem K q c hv, sub_self]

end QOU.BraidKnot.CompositionEigenPower
