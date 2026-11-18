import QOU.IwahoriHecke.TypeA
import QOU.Hecke.IwahoriHecke
import QOU.Hecke.TwBasisField

/-!
# Two of the presentations are the same algebra

The tree holds several Iwahori–Hecke presentations (bean `qou-img9`). This file removes
one from the pile by **proving two of them equal** rather than documenting that they
coexist:

* `QOU.IwahoriHecke.TypeA.IwahoriHeckeOfSn K q (n+1)` — `HeckeAlgebra` at the type-`A`
  Coxeter matrix, i.e. `RingQuot (FreeAlgebra K (Fin n))` modulo a relation carrying the
  quadratic family and one `altProd` family covering braid and far-commutation together;
* `QOU.Hecke.IwahoriHecke K q n` — `RingQuot (FreeAlgebra K (Fin n))` modulo a relation
  with the three families written separately.

Same carrier, same generators, same relations in a different syntactic shape. The
equivalence is built from the two universal properties, so neither construction is
privileged.

## Why this is worth having

`QOU/Hecke/TwBasisField.lean` proves `finrank_eq_factorial` — `dim H = (n+1)!` — against
the second presentation. Its author flagged, correctly, that transporting it to the
first was **unproved and not claimed**. `algEquiv` below is that transport: an
`AlgEquiv` carries a basis and a finrank, so the dimension result reaches
`IwahoriHeckeOfSn` and everything built on it.

## Index bookkeeping

`IwahoriHecke K q n` has `Fin n` generators and is `H_{n+1}(q)`;
`IwahoriHeckeOfSn K q m` has `Fin (m-1)` generators. So the match is at `m = n+1`, where
`Fin (m-1)` reduces to `Fin n` definitionally.
-/

namespace QOU.BraidKnot.Hecke

open QOU.MathlibExt.IwahoriHecke
open QOU.IwahoriHecke.TypeA

universe u

variable (K : Type u) [CommRing K] (q : K) (n : ℕ)

/-! ## The `Fin` index lemmas

`strandMatrix (n+1)` is `CoxeterMatrix.Aₙ n`, whose entries are stated with `ℕ`-valued
coercions; these three lemmas evaluate it on the shapes the relation families use. -/

theorem strandMatrix_self (i : Fin n) : strandMatrix (n + 1) i i = 1 := by
  simp [strandMatrix, CoxeterMatrix.Aₙ]

theorem strandMatrix_adjacent {i j : Fin n} (h : (i : ℕ) + 1 = (j : ℕ)) :
    strandMatrix (n + 1) i j = 3 := by
  simp only [strandMatrix, CoxeterMatrix.Aₙ, Matrix.of_apply, Fin.ext_iff]
  rw [if_neg (by omega), if_pos (by omega)]

theorem strandMatrix_adjacent' {i j : Fin n} (h : (i : ℕ) + 1 = (j : ℕ)) :
    strandMatrix (n + 1) j i = 3 := by
  simp only [strandMatrix, CoxeterMatrix.Aₙ, Matrix.of_apply, Fin.ext_iff]
  rw [if_neg (by omega), if_pos (by omega)]

theorem strandMatrix_far {i j : Fin n} (hne : (i : ℕ) ≠ (j : ℕ))
    (h1 : (j : ℕ) + 1 ≠ (i : ℕ)) (h2 : (i : ℕ) + 1 ≠ (j : ℕ)) :
    strandMatrix (n + 1) i j = 2 := by
  simp only [strandMatrix, CoxeterMatrix.Aₙ, Matrix.of_apply, Fin.ext_iff]
  rw [if_neg hne, if_neg (by omega)]

/-! ## Their generators satisfy my relations -/

open QOU.Hecke.IwahoriHecke in
/-- Their `σ` satisfies the quadratic relation in my `(T − q)(T + 1) = 0` shape.
Theirs is stated as `σ² = (q−1)·σ + q·1`; the two are the same identity rearranged. -/
theorem sigma_quadratic' (i : Fin n) :
    (σ K q n i - algebraMap K (QOU.Hecke.IwahoriHecke K q n) q) * (σ K q n i + 1) = 0 := by
  have h := σ_quadratic K q n i
  have expand : (σ K q n i - algebraMap K (QOU.Hecke.IwahoriHecke K q n) q) * (σ K q n i + 1)
      = σ K q n i * σ K q n i + σ K q n i
        - algebraMap K (QOU.Hecke.IwahoriHecke K q n) q * σ K q n i
        - algebraMap K (QOU.Hecke.IwahoriHecke K q n) q := by
    simp only [sub_mul, mul_add, mul_one]
    abel
  rw [expand, h, Algebra.smul_def, Algebra.smul_def, mul_one]
  simp only [map_sub, map_one, sub_mul, one_mul]
  abel

open QOU.Hecke.IwahoriHecke in
/-- Their `σ` satisfies my single `altProd` braid family, which packages their separate
braid and commutation relations plus the trivial diagonal case. -/
theorem sigma_braid' (i j : Fin n) :
    altProd (σ K q n i) (σ K q n j) (strandMatrix (n + 1) i j)
      = altProd (σ K q n j) (σ K q n i) (strandMatrix (n + 1) j i) := by
  rcases eq_or_ne (i : ℕ) (j : ℕ) with hij | hij
  · have : i = j := Fin.ext hij
    subst this; rfl
  · rcases eq_or_ne ((i : ℕ) + 1) (j : ℕ) with hadj | hadj
    · -- j = i + 1
      have hi1 : (i : ℕ) + 1 < n := by omega
      have hj : j = (⟨(i : ℕ) + 1, hi1⟩ : Fin n) := Fin.ext (by simpa using hadj.symm)
      rw [strandMatrix_adjacent n hadj, strandMatrix_adjacent' n hadj,
        altProd_three, altProd_three, hj, ← mul_assoc, ← mul_assoc]
      exact σ_braid K q n i hi1
    · rcases eq_or_ne ((j : ℕ) + 1) (i : ℕ) with hadj' | hadj'
      · -- i = j + 1
        have hj1 : (j : ℕ) + 1 < n := by omega
        have hi : i = (⟨(j : ℕ) + 1, hj1⟩ : Fin n) := Fin.ext (by simpa using hadj'.symm)
        rw [strandMatrix_adjacent' n hadj', strandMatrix_adjacent n hadj',
          altProd_three, altProd_three, hi, ← mul_assoc, ← mul_assoc]
        exact (σ_braid K q n j hj1).symm
      · -- far apart
        rw [strandMatrix_far n hij (by omega) (by omega),
          strandMatrix_far n (Ne.symm hij) (by omega) (by omega),
          altProd_two, altProd_two]
        rcases lt_or_gt_of_ne hij with hlt | hgt
        · exact (σ_commute K q n j i (by omega)).symm
        · exact σ_commute K q n i j (by omega)

/-! ## The maps -/

open QOU.Hecke.IwahoriHecke in
/-- **The canonical algebra map** from my type-`A` presentation onto theirs, sending
generator to generator. -/
noncomputable def toTheirs : IwahoriHeckeOfSn K q (n + 1) →ₐ[K] QOU.Hecke.IwahoriHecke K q n :=
  lift K q (strandMatrix (n + 1)) (σ K q n) (sigma_quadratic' K q n) (sigma_braid' K q n)

open QOU.Hecke.IwahoriHecke in
@[simp] theorem toTheirs_sigma (i : Fin n) :
    toTheirs K q n (QOU.IwahoriHecke.TypeA.σ K q (n + 1) i) = σ K q n i :=
  lift_T K q (strandMatrix (n + 1)) _ _ _ i

/-! ## My generators satisfy their relations -/

/-- My `σ` in their quadratic shape `σ² = (q−1)·σ + q·1`. -/
theorem my_sigma_quadratic (i : Fin n) :
    QOU.IwahoriHecke.TypeA.σ K q (n + 1) i * QOU.IwahoriHecke.TypeA.σ K q (n + 1) i
      = (q - 1) • QOU.IwahoriHecke.TypeA.σ K q (n + 1) i
        + q • (1 : IwahoriHeckeOfSn K q (n + 1)) := by
  have h := QOU.IwahoriHecke.TypeA.sigma_quadratic (R := K) (q := q) (n := n + 1) i
  have expand : (QOU.IwahoriHecke.TypeA.σ K q (n + 1) i
        - algebraMap K (IwahoriHeckeOfSn K q (n + 1)) q)
      * (QOU.IwahoriHecke.TypeA.σ K q (n + 1) i + 1)
      = QOU.IwahoriHecke.TypeA.σ K q (n + 1) i * QOU.IwahoriHecke.TypeA.σ K q (n + 1) i
        + QOU.IwahoriHecke.TypeA.σ K q (n + 1) i
        - algebraMap K (IwahoriHeckeOfSn K q (n + 1)) q
          * QOU.IwahoriHecke.TypeA.σ K q (n + 1) i
        - algebraMap K (IwahoriHeckeOfSn K q (n + 1)) q := by
    simp only [sub_mul, mul_add, mul_one]; abel
  rw [expand] at h
  rw [Algebra.smul_def, Algebra.smul_def, mul_one, map_sub, map_one, sub_mul, one_mul]
  refine sub_eq_zero.mp ?_
  linear_combination (norm := abel) h

/-- My `σ` satisfies their braid relation. -/
theorem my_sigma_braid (i : Fin n) (hi : (i : ℕ) + 1 < n) :
    QOU.IwahoriHecke.TypeA.σ K q (n + 1) i
        * QOU.IwahoriHecke.TypeA.σ K q (n + 1) ⟨(i : ℕ) + 1, hi⟩
        * QOU.IwahoriHecke.TypeA.σ K q (n + 1) i
      = QOU.IwahoriHecke.TypeA.σ K q (n + 1) ⟨(i : ℕ) + 1, hi⟩
        * QOU.IwahoriHecke.TypeA.σ K q (n + 1) i
        * QOU.IwahoriHecke.TypeA.σ K q (n + 1) ⟨(i : ℕ) + 1, hi⟩ := by
  have h := QOU.IwahoriHecke.TypeA.sigma_braid (R := K) (q := q) (n := n + 1)
    i (⟨(i : ℕ) + 1, hi⟩ : Fin n)
  rw [strandMatrix_adjacent n (by simp), strandMatrix_adjacent' n (by simp),
    altProd_three, altProd_three] at h
  rw [mul_assoc, mul_assoc]
  exact h

/-- My `σ` satisfies their far-commutation relation. -/
theorem my_sigma_commute (i j : Fin n) (h : (j : ℕ) + 2 ≤ (i : ℕ)) :
    QOU.IwahoriHecke.TypeA.σ K q (n + 1) i * QOU.IwahoriHecke.TypeA.σ K q (n + 1) j
      = QOU.IwahoriHecke.TypeA.σ K q (n + 1) j * QOU.IwahoriHecke.TypeA.σ K q (n + 1) i := by
  have hb := QOU.IwahoriHecke.TypeA.sigma_braid (R := K) (q := q) (n := n + 1) i j
  rw [strandMatrix_far n (by omega) (by omega) (by omega),
    strandMatrix_far n (by omega) (by omega) (by omega), altProd_two, altProd_two] at hb
  exact hb

/-! ## The equivalence -/

open QOU.Hecke.IwahoriHecke in
/-- **The canonical algebra map back**, generator to generator. -/
noncomputable def toMine : QOU.Hecke.IwahoriHecke K q n →ₐ[K] IwahoriHeckeOfSn K q (n + 1) :=
  RingQuot.liftAlgHom K
    ⟨FreeAlgebra.lift K (fun i : Fin n => QOU.IwahoriHecke.TypeA.σ K q (n + 1) i), by
      intro x y hr
      induction hr with
      | quadratic i =>
          simpa [map_mul, map_add, map_smul, FreeAlgebra.lift_ι_apply]
            using my_sigma_quadratic K q n i
      | braid i hi =>
          simpa [map_mul, FreeAlgebra.lift_ι_apply] using my_sigma_braid K q n i hi
      | commute i j h =>
          simpa [map_mul, FreeAlgebra.lift_ι_apply] using my_sigma_commute K q n i j h⟩

open QOU.Hecke.IwahoriHecke in
@[simp] theorem toMine_sigma (i : Fin n) :
    toMine K q n (σ K q n i) = QOU.IwahoriHecke.TypeA.σ K q (n + 1) i := by
  show RingQuot.liftAlgHom K _ (RingQuot.mkAlgHom K (QOU.Hecke.HeckeRel K q n) (FreeAlgebra.ι K i)) = _
  rw [RingQuot.liftAlgHom_mkAlgHom_apply]
  simp

open QOU.Hecke.IwahoriHecke in
/-- Two algebra maps out of *their* presentation agreeing on generators are equal —
the same `mkAlgHom`-surjective plus `FreeAlgebra.hom_ext` argument as on my side. -/
theorem theirs_hom_ext {A : Type*} [Ring A] [Algebra K A]
    (φ ψ : QOU.Hecke.IwahoriHecke K q n →ₐ[K] A)
    (h : ∀ i, φ (σ K q n i) = ψ (σ K q n i)) : φ = ψ := by
  have hcomp : φ.comp (RingQuot.mkAlgHom K (QOU.Hecke.HeckeRel K q n))
      = ψ.comp (RingQuot.mkAlgHom K (QOU.Hecke.HeckeRel K q n)) := by
    apply FreeAlgebra.hom_ext
    funext i
    simpa [QOU.Hecke.IwahoriHecke.σ, QOU.Hecke.IwahoriHecke.mk] using h i
  apply AlgHom.ext
  intro x
  obtain ⟨y, rfl⟩ := RingQuot.mkAlgHom_surjective K (QOU.Hecke.HeckeRel K q n) x
  exact congrArg (fun (α : FreeAlgebra K (Fin n) →ₐ[K] A) => α y) hcomp

open QOU.Hecke.IwahoriHecke in
/-- **The two presentations are the same algebra.**

This is what transports `QOU/Hecke/TwBasisField.lean`'s `finrank_eq_factorial` — proved
against their presentation, and explicitly *not* claimed for mine by its author — onto
`IwahoriHeckeOfSn`. An `AlgEquiv` carries a basis and a finrank. -/
noncomputable def algEquiv : IwahoriHeckeOfSn K q (n + 1) ≃ₐ[K] QOU.Hecke.IwahoriHecke K q n :=
  AlgEquiv.ofAlgHom (toTheirs K q n) (toMine K q n)
    (theirs_hom_ext K q n _ _ (by intro i; simp))
    (hom_ext K q (strandMatrix (n + 1)) _ _ (by
      intro i
      show toMine K q n (toTheirs K q n (QOU.IwahoriHecke.TypeA.σ K q (n + 1) i)) = _
      simp
      rfl))

/-! ## The transport

`QOU/Hecke/TwBasisField.lean` proves `finrank_eq_factorial` against the sibling
presentation, and its author flagged — correctly — that carrying it to this one was
unproved. `algEquiv` is the mechanism; these two are the carry. An `AlgEquiv` is in
particular a linear equivalence, so it moves both the dimension and the basis. -/

section FieldTransport

variable (K : Type u) [Field K] (q : K) (n : ℕ)

/-- **`dim_K H_n(q) = (n+1)!` for the `HeckeAlgebra`-backed presentation**, transported
across `algEquiv` from `QOU.Hecke.TwBasis.finrank_eq_factorial`. -/
theorem finrank_IwahoriHeckeOfSn :
    Module.finrank K (IwahoriHeckeOfSn K q (n + 1)) = Nat.factorial (n + 1) := by
  rw [(algEquiv K q n).toLinearEquiv.finrank_eq]
  exact QOU.Hecke.TwBasis.finrank_eq_factorial K q n

/-- **The `T_w` basis, transported.** Indexed by `Equiv.Perm (Fin (n+1))`, as on the
sibling side. -/
noncomputable def basisTwOfSn :
    Module.Basis (Equiv.Perm (Fin (n + 1))) K (IwahoriHeckeOfSn K q (n + 1)) :=
  (QOU.Hecke.TwBasis.basisTwOfField K q n).map (algEquiv K q n).toLinearEquiv.symm

/-- Subtracting the factorial of the strand count from the transported algebra dimension cancels to zero (`qou-mfps`). -/
theorem finrank_IwahoriHeckeOfSn_sub_eq_zero :
    Module.finrank K (IwahoriHeckeOfSn K q (n + 1)) - Nat.factorial (n + 1) = 0 := by
  rw [finrank_IwahoriHeckeOfSn K q n, Nat.sub_self]

end FieldTransport

end QOU.BraidKnot.Hecke
