/-
# The chain closes: step 1's output, in the shape steps 2–4 consume

`RothAuxiliaryInt` produces the auxiliary polynomial over `ℤ`, which is the coefficient ring
Roth's Lemma requires.  Two pieces of glue remain before it can actually be handed to
`roth_contradiction`, and both are small enough to be invisible and large enough to be wrong.

**The height.**  Siegel states its bound as a real number; `InRothPolySet` wants an integer `a`
with `|coeff n P| ≤ a`.  `inRothPolySet_of_real_bound` takes the ceiling.  A ceiling is the only
choice that works in this direction — rounding down would be an assertion, not a consequence.

**The index.**  Step 1 proves the index over `K`; step 2 consumes it over `ℝ`.  They are related by
a real embedding, and `index_real_of_index_field` transports along one.  That embedding is a
genuine hypothesis, not a technicality: it is the statement that the `α_h` are *real* algebraic
numbers, which is what Roth's theorem is about.  A number field with no real embedding has nothing
to say here, and the composition correctly refuses to typecheck without one.

## What the composition establishes, and what it does not

`roth_contradiction_int` runs step 1 → step 2 → step 3 → step 4 with the coefficient rings
agreeing throughout.  Its remaining hypotheses are the ones every earlier stage already isolated:
`Γ_m`'s clauses, the approximation quality, and the two numeric comparisons.  It does **not**
choose the parameters — selecting `q_1` large, then `q_2, …, q_m` from an infinite supply of good
approximations is what turns a contradiction into "finitely many solutions", and that is the one
remaining piece of Roth's theorem that is not bookkeeping.
-/
import QOU.Mathlib.RothAuxiliaryInt
import QOU.Mathlib.RothContradiction

open NumberField Finset

namespace MvPolynomial

section Glue

variable {m : ℕ}

/-- **Siegel's real bound becomes `InRothPolySet`'s integer one.**  The ceiling is forced: from
`|coeff| ≤ X` over `ℝ` the only integer bound available is `⌈X⌉`. -/
theorem inRothPolySet_of_real_bound {r : Fin m → ℕ} {P : MvPolynomial (Fin m) ℤ}
    (hne : P ≠ 0) (hdeg : ∀ h, degreeOf h P ≤ r h) {X : ℝ}
    (hX : ∀ n, |((coeff n P : ℤ) : ℝ)| ≤ X) :
    InRothPolySet ⌈X⌉ r P := by
  refine ⟨hne, hdeg, fun n => ?_⟩
  have h1 : (((|coeff n P| : ℤ)) : ℝ) ≤ X := by
    rw [Int.cast_abs]
    exact hX n
  have h3 : (((|coeff n P| : ℤ)) : ℝ) ≤ ((⌈X⌉ : ℤ) : ℝ) := le_trans h1 (Int.le_ceil X)
  exact_mod_cast h3

variable {K : Type*} [Field K] [NumberField K]

omit [NumberField K] in
/-- **The index transports along a real embedding.**  Step 1 proves it over `K`, step 2 consumes it
over `ℝ`; `ψ` is what says the `α_h` are real algebraic numbers.

`NumberField K` is omitted — the linter is right that nothing here uses it.  The transport is a
fact about *any* ring map to `ℝ`; that `K` is a number field is what makes `ψ` exist, not what
makes the index move. -/
theorem index_real_of_index_field (r : Fin m → ℕ) (ψ : K →+* ℝ)
    (α : Fin m → 𝓞 K) (P : MvPolynomial (Fin m) ℤ) :
    index r (fun h => ψ ((algebraMap (𝓞 K) K) (α h))) (map (Int.castRingHom ℝ) P)
      = index r (fun h => (algebraMap (𝓞 K) K) (α h)) (map (algebraMap ℤ K) P) := by
  classical
  have hcomp : ψ.comp (algebraMap ℤ K) = Int.castRingHom ℝ := RingHom.ext_int _ _
  have hmap : map ψ (map (algebraMap ℤ K) P) = map (Int.castRingHom ℝ) P := by
    rw [map_map, hcomp]
  rw [← hmap, index_map ψ ψ.injective]

/-- **Step 1's output, in the shape steps 2–4 consume.**  A polynomial in `R(a; r)` whose index at
the *real* point `(ψα₁,…,ψα_m)` is at least `m/2 − εm`, with `a` also serving as the height bound
step 2 needs.

The counting condition is discharged inside, from `finrank ℚ K < 4ε²m` — so `deg α` is not a
hypothesis of the chain, it is a condition on how large `m` must be. -/
theorem exists_rothPolySet_auxiliary (r : Fin m → ℕ) (hr : ∀ h, r h ≠ 0)
    (α : Fin m → 𝓞 K) (ψ : K →+* ℝ) {ε : ℚ} (hε : 0 < ε)
    (hεm : ((Module.finrank ℚ K : ℕ) : ℚ) < 4 * ε ^ 2 * (m : ℚ))
    (hpos : 0 < Fintype.card ({i // i ∈ (idxBoxF r).filter
        (fun i => idxWeight r i ≤ (m : ℚ) / 2 - ε * (m : ℚ))}
      × Module.Free.ChooseBasisIndex ℤ (𝓞 K))) :
    ∃ P : MvPolynomial (Fin m) ℤ,
      InRothPolySet ⌈siegelHeight r α ((m : ℚ) / 2 - ε * (m : ℚ))⌉ r P ∧
      ((((m : ℚ) / 2 - ε * (m : ℚ) : ℚ)) : WithTop ℚ)
        ≤ index r (fun h => ψ ((algebraMap (𝓞 K) K) (α h))) (map (Int.castRingHom ℝ) P) ∧
      (∀ n, |((coeff n P : ℤ) : ℝ)|
        ≤ ((⌈siegelHeight r α ((m : ℚ) / 2 - ε * (m : ℚ))⌉ : ℤ) : ℝ)) := by
  classical
  obtain ⟨P, hne, hdeg, hidx, hbound⟩ :=
    exists_auxiliary_polynomial_int r α ((m : ℚ) / 2 - ε * (m : ℚ)) hpos
      (card_prod_lt_card_idxBoxF r hr hε hεm)
  refine ⟨P, inRothPolySet_of_real_bound hne hdeg hbound, ?_, fun n => ?_⟩
  · rw [index_real_of_index_field r ψ α P]
    exact hidx
  · exact le_trans (hbound n) (Int.le_ceil _)

end Glue

section Chain

variable {m : ℕ} {K : Type*} [Field K] [NumberField K]

/-- **Steps 1 → 2 → 3 → 4, with the coefficient rings agreeing throughout.**

Step 1 supplies the polynomial (`exists_rothPolySet_auxiliary`), step 2 turns the approximation
quality into a lower bound on the index at the rational point, step 3 (Roth's Lemma) caps that
index from above, and step 4 collides them.

What is left over is exactly what the earlier stages isolated and nothing new: `Γ_m`'s clauses
(`hg`), the approximation quality (`hclose`, `hT`), and the two numeric comparisons (`hlog`,
`hgap`).  Choosing parameters that satisfy them is the remaining work. -/
theorem roth_contradiction_int (hm : 1 ≤ m) {p q F : ℕ} (hp : 0 < p) (hpq : p ≤ q)
    {r Hh : Fin m → ℕ} (hr : ∀ h, r h ≠ 0)
    (α : Fin m → 𝓞 K) (ψ : K →+* ℝ) {ε : ℚ} (hε : 0 < ε)
    (hεm : ((Module.finrank ℚ K : ℕ) : ℚ) < 4 * ε ^ 2 * (m : ℚ))
    (hpos : 0 < Fintype.card ({i // i ∈ (idxBoxF r).filter
        (fun i => idxWeight r i ≤ (m : ℚ) / 2 - ε * (m : ℚ))}
      × Module.Free.ChooseBasisIndex ℤ (𝓞 K)))
    (pn : Fin m → ℤ) (qd : Fin m → ℕ) (hq : ∀ h, qd h ≠ 0)
    {G T : Fin m → ℝ} (hG0 : ∀ h, 0 ≤ G h)
    (hGT : ∀ h, G h ≤ Real.exp (-(T h)))
    (hclose : ∀ h, |(((pn h : ℚ) / (qd h : ℚ) : ℚ) : ℝ)
        - ψ ((algebraMap (𝓞 K) K) (α h))| ≤ G h)
    {Kc : ℝ} (hK0 : 0 ≤ Kc) (hT : ∀ h, Kc ≤ T h * (r h : ℝ))
    {B : ℝ} (hB1 : 1 ≤ B) (hα : ∀ h, |ψ ((algebraMap (𝓞 K) K) (α h))| ≤ B)
    (hκ : InRothFracSet Hh (fun h => (pn h : ℚ) / (qd h : ℚ)))
    {ν : ℚ} (hν0 : 0 ≤ ν)
    (hgap : (rothConstant m : ℚ) ^ (2 ^ (m - 1)) * ((p : ℚ) / (q : ℚ)) < ν ^ (2 ^ (m - 1)))
    (hg : RothGammaFull (Equiv.refl (Fin m)) p q F r (fun j => (Hh j : ℤ))
      ⌈siegelHeight r α ((m : ℚ) / 2 - ε * (m : ℚ))⌉)
    (hCpos : 0 < taylorConst r
      ((⌈siegelHeight r α ((m : ℚ) / 2 - ε * (m : ℚ))⌉ : ℤ) : ℝ) B)
    (hlog : Real.log (taylorConst r
        ((⌈siegelHeight r α ((m : ℚ) / 2 - ε * (m : ℚ))⌉ : ℤ) : ℝ) B)
        + ∑ h, (r h : ℝ) * Real.log (qd h)
      < Kc * ((((m : ℚ) / 2 - ε * (m : ℚ) : ℚ) : ℝ) - ((ν : ℚ) : ℝ))) :
    False := by
  classical
  obtain ⟨P, hA, hidx, hH⟩ := exists_rothPolySet_auxiliary r hr α ψ hε hεm hpos
  exact roth_contradiction hm hp hpq hr hg pn qd hq
    (fun h => ψ ((algebraMap (𝓞 K) K) (α h))) hG0 hGT hclose hK0 hT hB1 hα
    P hA.2.1 hA hκ hH hν0 hidx hCpos hlog hgap

end Chain

end MvPolynomial
