import QOU.Hecke.IwahoriHecke
import QOU.MathlibExt.IwahoriHeckeAlgebra
import QOU.SchurWeyl.HeckeCarrierEquiv
import QOU.IwahoriHecke.BalancedGenerators
import Mathlib.GroupTheory.Coxeter.Matrix

/-!
# `QOU.IwahoriHecke.CoxeterCarrierEquiv` — the `Fin n` presentation *is* the Coxeter one

Bean `qou-0fmb` is titled *"wire the IwahoriHecke algebra to the BraidedTower theorem"*, and
the obstruction it names is real: the Ocneanu trace that is proved to exist and be unique
lives on `QOU.SchurWeyl.Hecke`, while `QOU/IwahoriHecke/` is built on a different
construction. This file supplies the missing link of the isomorphism route.

## What already existed, and what did not

Two of the three legs were already in the corpus, and a corpus-grep found them:

* **`QOU.SchurWeyl.carrierEquiv`** — `Hecke K q qi n ≃ₐ[K] QOU.Hecke.IwahoriHecke K Q n`,
  the skein↔Iwahori *normalisation* change at `Q = q²`, `σ_i ↦ c • T_i`. It crosses the
  quadratic relation.
* **`QOU.IwahoriHecke.Balanced`** — the same rescaling on the *Coxeter-matrix* family
  `QOU.MathlibExt.IwahoriHecke.HeckeAlgebra R Q M`, with `σ_i := qi · T_i` and a balanced
  universal property.

What was missing is the leg between the two **index presentations**, at a fixed
normalisation:

    QOU.Hecke.IwahoriHecke K Q n   ≃ₐ[K]   HeckeAlgebra K Q (Aₙ n)

The left states its braid content as two explicit clauses on `Fin n` — adjacent braiding
`σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}` and far commutation for `j + 2 ≤ i`. The right
states it as one clause quantified over *all* pairs, `altProd (T_i) (T_j) (M i j) =
altProd (T_j) (T_i) (M j i)`, against a Coxeter matrix. Nothing connected them, so a
result about one was not a result about the other — the defect bean `qou-img9` records as
*"a result proved against one presentation is not automatically a result about the object
the paper names"*.

## The content is the Coxeter matrix, and it is finite

For `M = CoxeterMatrix.Aₙ n` the entries are

    M i j = if i = j then 1 else if |i − j| = 1 then 3 else 2

and `altProd` at those three values is `a`, `a * (b * a)`, `a * b` respectively. So the
single quantified clause is *exactly* the conjunction of the two explicit ones plus a
triviality on the diagonal, and the translation is a five-way case split on `(i : ℕ)`
against `(j : ℕ)`. That is `altProd_iff_explicit` below; both lift directions consume it,
and neither presentation is privileged.

The quadratic relations are already the same modulo `Q • 1` versus `algebraMap _ _ Q`, so
nothing has to move there — `quadratic_smul_iff_factored` is the one-line bridge.

## What this buys

Composing with `carrierEquiv` gives `skeinCoxeterEquiv`:

    QOU.SchurWeyl.Hecke K q q⁻¹ n   ≃ₐ[K]   HeckeAlgebra K (q²) (Aₙ n)

i.e. the algebra carrying the proved Ocneanu trace is the algebra the `QOU/IwahoriHecke/`
tree is built on — `TypeA.IwahoriHeckeOfSn` and `Balanced.BalancedHecke` are both
`HeckeAlgebra` at a type-A matrix.

## What this does NOT do

* It does **not** transport the `OcneanuTrace.MarkovTrace` or `BraidedTower` instance.
  Those are structures over a *tower* indexed by `ℕ`; this is one equivalence at each
  fixed `n`, and the transport needs the equivalences to commute with the level
  inclusions. That is not proved here and is assumed nowhere.
* It does **not** touch `TypeA.IwahoriHeckeOfSn`, whose index type is `Fin (n - 1)` with
  truncated subtraction. Relating that re-indexing to `Fin n` is a separate step.
* It says nothing about the `Set.univ`-indexed `QOU.IwahoriHecke.Defn.IwahoriHecke`, which
  bean `qou-img9` recommends retiring rather than repairing.

-- Ref: [humphreys1990] §7.1 (the Coxeter presentation of the Hecke algebra)
-- Ref: [geckpfeiffer2000] §4.4 (type A: the braid/commutation split)
-- Ref: [leitner2026] beans `qou-0fmb`, `qou-img9`
-/

namespace QOU.IwahoriHecke.CoxeterCarrier

open QOU.MathlibExt.IwahoriHecke

variable {K : Type*} [CommRing K]

/-! ## The type-A Coxeter matrix as a bare function

`HeckeAlgebra` is parameterised by a plain `B → B → ℕ`, so the `CoxeterMatrix` bundle is
unwrapped once here and never again. -/

/-- The type-`Aₙ` Coxeter matrix on `Fin n`, as the bare function `HeckeAlgebra` wants. -/
abbrev AMat (n : ℕ) : Fin n → Fin n → ℕ := fun i j => (CoxeterMatrix.Aₙ n) i j

/-- The matrix is symmetric — this is `CoxeterMatrix`'s own field, not a fresh proof. -/
theorem AMat_symm (n : ℕ) (i j : Fin n) : AMat n i j = AMat n j i :=
  (CoxeterMatrix.Aₙ n).symmetric i j

/-- On the diagonal the entry is `1`. -/
@[simp] theorem AMat_diag (n : ℕ) (i : Fin n) : AMat n i i = 1 := by
  simp [AMat, CoxeterMatrix.Aₙ]

/-- Adjacent indices braid: the entry is `3`. -/
theorem AMat_adjacent (n : ℕ) (i j : Fin n)
    (h : (i : ℕ) + 1 = (j : ℕ) ∨ (j : ℕ) + 1 = (i : ℕ)) : AMat n i j = 3 := by
  have hne : i ≠ j := by
    intro hij
    rw [hij] at h
    omega
  simp only [AMat, CoxeterMatrix.Aₙ, Matrix.of_apply, if_neg hne, if_pos (by omega : (j : ℕ) + 1 = (i : ℕ) ∨ (i : ℕ) + 1 = (j : ℕ))]

/-- Distinct non-adjacent indices commute: the entry is `2`. -/
theorem AMat_far (n : ℕ) (i j : Fin n) (h : (j : ℕ) + 2 ≤ (i : ℕ)) : AMat n i j = 2 := by
  have hne : i ≠ j := by
    intro hij
    rw [hij] at h
    omega
  simp only [AMat, CoxeterMatrix.Aₙ, Matrix.of_apply, if_neg hne,
    if_neg (by omega : ¬((j : ℕ) + 1 = (i : ℕ) ∨ (i : ℕ) + 1 = (j : ℕ)))]

/-! ## The braid clause, in both shapes

This is the mathematical content of the file: the one `altProd` clause of the Coxeter
presentation and the two explicit clauses of the `Fin n` presentation say the same thing
about any family `g : Fin n → A`. -/

variable {A : Type*} [Ring A]

/-- The braid relation in the associativity shape `altProd` produces. -/
private theorem braid_assoc {n : ℕ} (g : Fin n → A)
    (hbraid : ∀ (i : Fin n) (hi : (i : ℕ) + 1 < n),
      g i * g ⟨(i : ℕ) + 1, hi⟩ * g i
        = g ⟨(i : ℕ) + 1, hi⟩ * g i * g ⟨(i : ℕ) + 1, hi⟩)
    (a b : Fin n) (hab : (a : ℕ) + 1 = (b : ℕ)) :
    g a * (g b * g a) = g b * (g a * g b) := by
  have ha : (a : ℕ) + 1 < n := by
    have := b.isLt
    omega
  have hb : b = ⟨(a : ℕ) + 1, ha⟩ := Fin.ext (by simp [hab.symm])
  subst hb
  have h := hbraid a ha
  rw [← mul_assoc, ← mul_assoc]
  exact h

/-- **The explicit clauses imply the `altProd` clause.**

Five cases on `(i : ℕ)` against `(j : ℕ)`: equal (diagonal, entry `1`, `altProd _ _ 1 = a`
on both sides), `i + 1 = j` and `j + 1 = i` (the two orientations of the braid, entry `3`),
and `j + 2 ≤ i` and `i + 2 ≤ j` (the two orientations of far commutation, entry `2`). -/
theorem altProd_of_explicit {n : ℕ} (g : Fin n → A)
    (hbraid : ∀ (i : Fin n) (hi : (i : ℕ) + 1 < n),
      g i * g ⟨(i : ℕ) + 1, hi⟩ * g i
        = g ⟨(i : ℕ) + 1, hi⟩ * g i * g ⟨(i : ℕ) + 1, hi⟩)
    (hcomm : ∀ (i j : Fin n), (j : ℕ) + 2 ≤ (i : ℕ) → g i * g j = g j * g i)
    (i j : Fin n) :
    altProd (g i) (g j) (AMat n i j) = altProd (g j) (g i) (AMat n j i) := by
  rcases eq_or_ne i j with rfl | hne
  · simp
  · have hij : (i : ℕ) ≠ (j : ℕ) := fun h => hne (Fin.ext h)
    rcases Nat.lt_or_ge (i : ℕ) (j : ℕ) with hlt | hge
    · rcases Nat.eq_or_lt_of_le hlt with hadj | hfar
      · -- `i + 1 = j`
        rw [AMat_adjacent n i j (Or.inl hadj), AMat_adjacent n j i (Or.inr hadj),
          altProd_three, altProd_three]
        exact braid_assoc g hbraid i j hadj
      · -- `i + 2 ≤ j`
        rw [AMat_far n j i (by omega), AMat_symm n i j, AMat_far n j i (by omega),
          altProd_two, altProd_two]
        exact (hcomm j i (by omega)).symm
    · -- `hge : (j : ℕ) ≤ (i : ℕ)` together with `hij` gives a strict `<`, which is
      -- `(j : ℕ) + 1 ≤ (i : ℕ)` definitionally — that is what splits adjacent from far.
      have hlt' : (j : ℕ) < (i : ℕ) := lt_of_le_of_ne hge (Ne.symm hij)
      rcases Nat.eq_or_lt_of_le hlt' with hadj | hfar
      · -- `j + 1 = i`
        rw [AMat_adjacent n i j (Or.inr hadj), AMat_adjacent n j i (Or.inl hadj),
          altProd_three, altProd_three]
        exact (braid_assoc g hbraid j i hadj).symm
      · -- `j + 2 ≤ i`
        rw [AMat_far n i j (by omega), AMat_symm n j i, AMat_far n i j (by omega),
          altProd_two, altProd_two]
        exact hcomm i j (by omega)

/-- **The `altProd` clause implies adjacent braiding.** -/
theorem braid_of_altProd {n : ℕ} (g : Fin n → A)
    (hb : ∀ i j : Fin n, altProd (g i) (g j) (AMat n i j)
      = altProd (g j) (g i) (AMat n j i))
    (i : Fin n) (hi : (i : ℕ) + 1 < n) :
    g i * g ⟨(i : ℕ) + 1, hi⟩ * g i
      = g ⟨(i : ℕ) + 1, hi⟩ * g i * g ⟨(i : ℕ) + 1, hi⟩ := by
  set j : Fin n := ⟨(i : ℕ) + 1, hi⟩ with hjdef
  have hadj : (i : ℕ) + 1 = (j : ℕ) := by simp [hjdef]
  have h := hb i j
  rw [AMat_adjacent n i j (Or.inl hadj), AMat_adjacent n j i (Or.inr hadj),
    altProd_three, altProd_three] at h
  rw [mul_assoc, mul_assoc]
  exact h

/-- **The `altProd` clause implies far commutation.** -/
theorem comm_of_altProd {n : ℕ} (g : Fin n → A)
    (hb : ∀ i j : Fin n, altProd (g i) (g j) (AMat n i j)
      = altProd (g j) (g i) (AMat n j i))
    (i j : Fin n) (hij : (j : ℕ) + 2 ≤ (i : ℕ)) :
    g i * g j = g j * g i := by
  have h := hb i j
  rw [AMat_far n i j hij, AMat_symm n j i, AMat_far n i j hij,
    altProd_two, altProd_two] at h
  exact h

/-! ## The quadratic clause

`QOU.Hecke` writes it as `σ² = (Q − 1) • σ + Q • 1`; `HeckeAlgebra` writes it factored as
`(T − algebraMap Q)(T + 1) = 0`. Over a commutative base these are the same statement. -/

/-- The two spellings of the Hecke quadratic relation agree. -/
theorem quadratic_smul_iff_factored [Algebra K A] (Q : K) (x : A) :
    x * x = (Q - 1) • x + Q • 1 ↔ (x - algebraMap K A Q) * (x + 1) = 0 := by
  constructor
  · intro h
    have : (x - algebraMap K A Q) * (x + 1)
        = x * x - (Q - 1) • x - Q • 1 := by
      simp only [Algebra.smul_def, map_sub, map_one, mul_one]
      noncomm_ring
    rw [this, h]
    abel
  · intro h
    have key : (x - algebraMap K A Q) * (x + 1)
        = x * x - (Q - 1) • x - Q • 1 := by
      simp only [Algebra.smul_def, map_sub, map_one, mul_one]
      noncomm_ring
    rw [key] at h
    have := sub_eq_zero.mp (by linear_combination (norm := abel) h :
      x * x - ((Q - 1) • x + Q • 1) = 0)
    exact this

/-! ## The two maps -/

variable (K) in
/-- **`Fin n` presentation → Coxeter presentation**, `σ_i ↦ T_i`.

The parameter does not move and the generators map across on the nose; all that is
checked is that the `T_i` satisfy the two explicit clauses, which they do by
`braid_of_altProd` / `comm_of_altProd` applied to `T_braid`. -/
noncomputable def toCoxeter (Q : K) (n : ℕ) :
    QOU.Hecke.IwahoriHecke K Q n →ₐ[K] HeckeAlgebra K Q (AMat n) :=
  QOU.SchurWeyl.iwahoriLift K Q n (fun i => T K Q (AMat n) i)
    (fun i => (quadratic_smul_iff_factored Q _).mpr (T_quadratic i))
    (fun i hi => braid_of_altProd _ (fun a b => T_braid a b) i hi)
    (fun i j hij => comm_of_altProd _ (fun a b => T_braid a b) i j hij)

variable (K) in
/-- **Coxeter presentation → `Fin n` presentation**, `T_i ↦ σ_i`. -/
noncomputable def fromCoxeter (Q : K) (n : ℕ) :
    HeckeAlgebra K Q (AMat n) →ₐ[K] QOU.Hecke.IwahoriHecke K Q n :=
  lift K Q (AMat n) (fun i => QOU.Hecke.IwahoriHecke.σ K Q n i)
    (fun i => (quadratic_smul_iff_factored Q _).mp (QOU.Hecke.IwahoriHecke.σ_quadratic K Q n i))
    (altProd_of_explicit _ (fun i hi => QOU.Hecke.IwahoriHecke.σ_braid K Q n i hi)
      (fun i j hij => QOU.Hecke.IwahoriHecke.σ_commute K Q n i j hij))

variable (K) in
/-- **The two presentations are the same algebra.**

Both composites are the identity on generators, so `hom_ext` on each side finishes. No
hypothesis on `Q` is needed: unlike the *normalisation* change of
`QOU.SchurWeyl.carrierEquiv`, this is a change of how the relations are *written*, and no
scalar is inverted. -/
noncomputable def coxeterCarrierEquiv (Q : K) (n : ℕ) :
    QOU.Hecke.IwahoriHecke K Q n ≃ₐ[K] HeckeAlgebra K Q (AMat n) :=
  AlgEquiv.ofAlgHom (toCoxeter K Q n) (fromCoxeter K Q n)
    (hom_ext K Q (AMat n) _ _ (by
      intro i
      simp only [AlgHom.comp_apply, AlgHom.coe_id, id_eq, fromCoxeter, toCoxeter,
        lift_T, QOU.SchurWeyl.iwahoriLift_σ]))
    (QOU.SchurWeyl.iwahori_hom_ext K Q n (by
      intro i
      simp only [AlgHom.comp_apply, AlgHom.coe_id, id_eq, fromCoxeter, toCoxeter,
        QOU.SchurWeyl.iwahoriLift_σ, lift_T]))

@[simp] theorem coxeterCarrierEquiv_σ (Q : K) (n : ℕ) (i : Fin n) :
    coxeterCarrierEquiv K Q n (QOU.Hecke.IwahoriHecke.σ K Q n i) = T K Q (AMat n) i :=
  QOU.SchurWeyl.iwahoriLift_σ K Q n _ _ _ _ i

/-! ## The composite: the skein algebra is the Coxeter algebra

This is the statement bean `qou-0fmb` wants. The algebra on the left is the one carrying
the proved-unique Ocneanu trace (`QOU.SchurWeyl.MarkovTraceInstance.wtrace`); the algebra
on the right is the one `QOU/IwahoriHecke/` is built on. -/

/-- **`H^skein_n(q) ≃ₐ HeckeAlgebra K q² (Aₙ n)`** over a field, for `q ≠ 0`. -/
noncomputable def skeinCoxeterEquiv {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (n : ℕ) :
    QOU.SchurWeyl.Hecke K q q⁻¹ n ≃ₐ[K] HeckeAlgebra K (q ^ 2) (AMat n) :=
  (QOU.SchurWeyl.skeinIwahoriEquiv q hq n).trans (coxeterCarrierEquiv K (q ^ 2) n)

/-- **The target is *literally* `Balanced.BalancedHecke`**, not merely isomorphic to it.

`BalancedHecke M q` is by definition `HeckeAlgebra R (q * q) M`, so taking `Q = q * q`
directly in `carrierEquiv` — rather than composing through `skeinIwahoriEquiv`, which
fixes `q ^ 2` — lands on that object on the nose, with no transport along `pow_two`.

This is what makes the headline claim checkable rather than asserted: the algebra on the
left carries the proved-unique Ocneanu trace, and the algebra on the right is the one
`IwahoriHecke/BalancedGenerators.lean` builds its §7a generators `σ_i = qi · T_i` on. -/
noncomputable def skeinBalancedEquiv {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (n : ℕ) :
    QOU.SchurWeyl.Hecke K q q⁻¹ n ≃ₐ[K] Balanced.BalancedHecke (AMat n) q :=
  (QOU.SchurWeyl.carrierEquiv K q q⁻¹ (q * q) q⁻¹ q n
      (by field_simp) (by field_simp) (by field_simp)).trans
    (coxeterCarrierEquiv K (q * q) n)

/-- The composite sends the skein generator `σ_i` to `q⁻¹ • T_i` — the §7a rescaling,
    now landing in the Coxeter presentation. -/
@[simp] theorem skeinCoxeterEquiv_σ {K : Type*} [Field K] (q : K) (hq : q ≠ 0) (n : ℕ)
    (i : Fin n) :
    skeinCoxeterEquiv q hq n (QOU.SchurWeyl.Hecke.σ K q q⁻¹ n i)
      = q⁻¹ • T K (q ^ 2) (AMat n) i := by
  simp only [skeinCoxeterEquiv, AlgEquiv.trans_apply, QOU.SchurWeyl.skeinIwahoriEquiv,
    QOU.SchurWeyl.carrierEquiv, AlgEquiv.ofAlgHom_apply, QOU.SchurWeyl.toIwahori,
    QOU.SchurWeyl.Hecke.lift_σ, map_smul, coxeterCarrierEquiv_σ]

end QOU.IwahoriHecke.CoxeterCarrier
