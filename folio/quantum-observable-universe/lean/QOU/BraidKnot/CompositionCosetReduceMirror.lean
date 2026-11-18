import QOU.BraidKnot.CompositionCosetReduce

/-!
# The mirror side: `T_a · x_μ` collapses onto the right-coset representative

`CompositionCosetReduce.xComp_mul_Tw_reduce` handles `x_μ · T_a`, on the **left** coset
`e·S_μ` with `e⁻¹` distinguished.  Mathas' `m_{st} = T*_{d(s)} · x_μ · T_{d(t)}` has a
factor on **each** side, so 3.9 needs the mirror too:

    `T_a · x_μ = q^{ℓ(v)} · (T_d · x_μ)`,   `a = v·d`, `d ∈ D_μ`, `v ∈ S_μ`

and this time it is the ordinary **right** coset `S_μ·d`, with `IsDistinguished` rather
than `IsDistinguishedL`.  The two orientations are not interchangeable — see the
handedness note in `CompositionCosetReduce` — and having both is exactly what lets a
two-sided expression be reduced on both sides independently.

## Structure

`Tw_mul_xComp_of_mem` mirrors `CompositionEigenPower.xComp_mul_Tw_of_mem` and its proof is
the same induction, differing only in which of the two eigenvector identities it consumes
(`σ_mul_xComp` here, `xComp_mul_σ` there).  In particular it reuses `descent_index_eq`
verbatim: that lemma is about `v` alone, not about which side it is multiplied on, so the
"a Young-subgroup element can only descend within a block" argument carries over unchanged.
-/

namespace QOU.BraidKnot.CompositionCosetReduceMirror

open QOU.BraidKnot.CompositionYoung QOU.BraidKnot.CompositionMinimal
open QOU.BraidKnot.CompositionMurphy QOU.BraidKnot.HeckeMurphy
open QOU.BraidKnot.CompositionEigenPower
open QOU.Hecke.SymmetricCoxeter QOU.Hecke.TwBasis QOU.Hecke.Inversions
open QOU.Hecke.IwahoriHecke Equiv

variable {n : ℕ} (K : Type*) [Field K] (q : K)

/-- **The mirror eigenvector power**: `T_v · x_μ = q^{ℓ(v)} · x_μ` for `v ∈ S_μ`. -/
theorem Tw_mul_xComp_of_mem (c : Composition (n + 1))
    [DecidablePred (· ∈ youngOfComp c)] {v : Perm (Fin (n + 1))}
    (hv : v ∈ youngOfComp c) :
    Tw K q n v * xComp K q c
      = q ^ ((permCoxeterSystem n).length v) • xComp K q c := by
  generalize hk : (permCoxeterSystem n).length v = k
  induction k using Nat.strong_induction_on generalizing v with
  | _ k ih =>
    by_cases hone : v = 1
    · subst hone
      simp [Tw_one, ← hk]
    · obtain ⟨i, hi⟩ := (permCoxeterSystem n).exists_rightDescent_of_ne_one hone
      have hlt : (permCoxeterSystem n).length (v * sw i)
          < (permCoxeterSystem n).length v := by
        rw [← simple_eq_sw]
        have h := (permCoxeterSystem n).isRightDescent_iff.mp hi
        omega
      have hdesc : v i.succ < v i.castSucc := by
        rcases invCount_mul_swap v i with ⟨-, hup⟩ | ⟨hdown, -⟩
        · rw [length_eq_invCount, length_eq_invCount, sw, hup] at hlt; omega
        · exact hdown
      have hblock : c.index i.castSucc = c.index i.succ := descent_index_eq hv hdesc
      have hsw : sw i ∈ youngOfComp c := mem_youngOfComp_sw.mpr hblock
      have hv' : v * sw i ∈ youngOfComp c := mul_mem hv hsw
      have hstep : (permCoxeterSystem n).length v
          = (permCoxeterSystem n).length (v * sw i) + 1 := by
        have h := (permCoxeterSystem n).length_mul_simple v i
        rw [simple_eq_sw] at h
        omega
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
      rw [hTw, mul_assoc, ih _ (hk ▸ hlt) hv' rfl, mul_smul_comm,
        σ_mul_xComp K q c i hblock, smul_smul, ← hk, hstep]
      ring_nf

/-- **The mirror coset reduction.**  Every `T_a · x_μ` is a `q`-power multiple of the one
attached to `a`'s distinguished representative, on the **right** coset `S_μ·d`. -/
theorem Tw_mul_xComp_reduce (c : Composition (n + 1))
    [DecidablePred (· ∈ youngOfComp c)] (a : Perm (Fin (n + 1))) :
    ∃ d v : Perm (Fin (n + 1)),
      IsDistinguished c d ∧ v ∈ youngOfComp c ∧ a = v * d ∧
        Tw K q n a * xComp K q c
          = q ^ ((permCoxeterSystem n).length v) • (Tw K q n d * xComp K q c) := by
  obtain ⟨d, ⟨hd, hdm⟩, -⟩ :=
    QOU.BraidKnot.CompositionCosetExists.existsUnique_isDistinguished_mem_coset c a
  -- `d · a⁻¹ ∈ S_μ`, so `v := a · d⁻¹` is too, and `a = v · d`
  have hv : a * d⁻¹ ∈ youngOfComp c := by
    have h : (d * a⁻¹)⁻¹ ∈ youngOfComp c := inv_mem hdm
    simpa [mul_inv_rev] using h
  refine ⟨d, a * d⁻¹, hd, hv, by group, ?_⟩
  have hfac : a * d⁻¹ * d = a := by group
  have hlen := length_mul_eq_add_of_isDistinguished hd hv
  have hTw : Tw K q n a = Tw K q n d * Tw K q n (a * d⁻¹) := by
    have h := Tw_mul_Tw K q n d (a * d⁻¹) hlen
    rw [hfac] at h
    exact h.symm
  rw [hTw, mul_assoc, Tw_mul_xComp_of_mem K q c hv, mul_smul_comm]

/-- Subtracting the length-scaled Murphy element from the left product cancels to zero (`qou-grph`). -/
theorem Tw_mul_xComp_sub_eq_zero (c : Composition (n + 1))
    [DecidablePred (· ∈ youngOfComp c)] {v : Perm (Fin (n + 1))}
    (hv : v ∈ youngOfComp c) :
    Tw K q n v * xComp K q c
      - q ^ ((permCoxeterSystem n).length v) • xComp K q c = 0 := by
  rw [Tw_mul_xComp_of_mem K q c hv, sub_self]

end QOU.BraidKnot.CompositionCosetReduceMirror
