import Mathlib.Algebra.FreeAlgebra
import Mathlib.Algebra.RingQuot
import Mathlib.Tactic

/-!
# QOU.Hecke.IwahoriHecke — the Iwahori–Hecke algebra `H_n(q)`

Mathlib has Coxeter groups but **no Hecke algebra**; this file supplies
the construction (track 2 of the Hecke-semisimplicity attack, epic
`qou-hnhg`, bean `qou-w8hn`).

The type-`A_n` Iwahori–Hecke algebra `H_{n+1}(q)` is the free
`K`-algebra on `n` generators `σ₀, …, σ_{n-1}` modulo the standard
relations (Kassel–Turaev; the QOU Hecke–skein convention, AGENTS.md §7a):

* **quadratic** `σ_i² = (q - 1)·σ_i + q` (i.e. `(σ_i - q)(σ_i + 1) = 0`);
* **braid** `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}`;
* **commutation** `σ_i σ_j = σ_j σ_i` for `|i - j| ≥ 2`.

It is realised as a `RingQuot` of `FreeAlgebra K (Fin n)`, so it is an
associative unital `K`-algebra by construction, and the generator
relations hold in it (proved below).  The standard `n!`-dimensional
`T_w`-basis theorem (Bott–Samelson) is deliberately *not* claimed here —
it is a separate, deep brick (`qou-lrz1`).
-/

namespace QOU.Hecke

open FreeAlgebra

/-- The defining relations of the type-`A` Iwahori–Hecke algebra on `n`
    generators, as a `RingQuot` relation on `FreeAlgebra K (Fin n)`. -/
inductive HeckeRel (K : Type*) [CommRing K] (q : K) (n : ℕ) :
    FreeAlgebra K (Fin n) → FreeAlgebra K (Fin n) → Prop where
  /-- `σ_i² = (q - 1)·σ_i + q`. -/
  | quadratic (i : Fin n) :
      HeckeRel K q n (ι K i * ι K i) ((q - 1) • ι K i + q • 1)
  /-- `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}`. -/
  | braid (i : Fin n) (hi : (i : ℕ) + 1 < n) :
      HeckeRel K q n
        (ι K i * ι K ⟨(i : ℕ) + 1, hi⟩ * ι K i)
        (ι K ⟨(i : ℕ) + 1, hi⟩ * ι K i * ι K ⟨(i : ℕ) + 1, hi⟩)
  /-- `σ_i σ_j = σ_j σ_i` for `|i - j| ≥ 2` (stated for `j + 2 ≤ i`; the
      generated congruence is symmetric). -/
  | commute (i j : Fin n) (h : (j : ℕ) + 2 ≤ (i : ℕ)) :
      HeckeRel K q n (ι K i * ι K j) (ι K j * ι K i)

/-- The **Iwahori–Hecke algebra** `H_{n+1}(q)` of type `A_n`. -/
def IwahoriHecke (K : Type*) [CommRing K] (q : K) (n : ℕ) : Type _ :=
  RingQuot (HeckeRel K q n)

namespace IwahoriHecke

variable (K : Type*) [CommRing K] (q : K) (n : ℕ)

noncomputable instance : Ring (IwahoriHecke K q n) :=
  inferInstanceAs (Ring (RingQuot (HeckeRel K q n)))

noncomputable instance : Algebra K (IwahoriHecke K q n) :=
  inferInstanceAs (Algebra K (RingQuot (HeckeRel K q n)))

/-- The canonical algebra map from the free algebra onto `H`. -/
noncomputable def mk : FreeAlgebra K (Fin n) →ₐ[K] IwahoriHecke K q n :=
  RingQuot.mkAlgHom K (HeckeRel K q n)

/-- The generator `σ_i ∈ H`. -/
noncomputable def σ (i : Fin n) : IwahoriHecke K q n := mk K q n (ι K i)

/-- **The quadratic relation holds in `H` (sorry-free):**
    `σ_i² = (q - 1)·σ_i + q`. -/
theorem σ_quadratic (i : Fin n) :
    σ K q n i * σ K q n i = (q - 1) • σ K q n i + q • 1 := by
  have h := RingQuot.mkAlgHom_rel (S := K) (HeckeRel.quadratic (q := q) i)
  simpa only [σ, mk, map_mul, map_add, map_smul, map_one] using h

/-- **The braid relation holds in `H` (sorry-free):**
    `σ_i σ_{i+1} σ_i = σ_{i+1} σ_i σ_{i+1}`. -/
theorem σ_braid (i : Fin n) (hi : (i : ℕ) + 1 < n) :
    σ K q n i * σ K q n ⟨(i : ℕ) + 1, hi⟩ * σ K q n i
      = σ K q n ⟨(i : ℕ) + 1, hi⟩ * σ K q n i * σ K q n ⟨(i : ℕ) + 1, hi⟩ := by
  have h := RingQuot.mkAlgHom_rel (S := K) (HeckeRel.braid (q := q) i hi)
  simpa only [σ, mk, map_mul] using h

/-- **The commutation relation holds in `H` (sorry-free):**
    `σ_i σ_j = σ_j σ_i` for `j + 2 ≤ i`. -/
theorem σ_commute (i j : Fin n) (h : (j : ℕ) + 2 ≤ (i : ℕ)) :
    σ K q n i * σ K q n j = σ K q n j * σ K q n i := by
  have hr := RingQuot.mkAlgHom_rel (S := K) (HeckeRel.commute (q := q) i j h)
  simpa only [σ, mk, map_mul] using hr

/-- The quadratic relation in factored form: `(σ_i - q)(σ_i + 1) = 0`. -/
theorem σ_quadratic_factored (i : Fin n) :
    (σ K q n i - q • 1) * (σ K q n i + 1) = 0 := by
  have hq := σ_quadratic K q n i
  have key : (σ K q n i - q • 1) * (σ K q n i + 1)
      = σ K q n i * σ K q n i - (q - 1) • σ K q n i - q • 1 := by
    simp only [Algebra.smul_def, map_sub, map_one, map_mul]
    noncomm_ring
  rw [key, hq]; abel

section Units

variable [Invertible q]

/-- The explicit inverse of a generator: `σ_i⁻¹ = q⁻¹·(σ_i - (q-1))`,
    read off the quadratic relation `σ_i(σ_i - (q-1)) = q`. -/
noncomputable def σInv (i : Fin n) : IwahoriHecke K q n :=
  ⅟q • (σ K q n i - (q - 1) • 1)

/-- `σ_i · σ_i⁻¹ = 1` when `q` is invertible (sorry-free). -/
theorem σ_mul_σInv (i : Fin n) :
    σ K q n i * σInv K q n i = 1 := by
  have hquad := σ_quadratic K q n i
  simp only [σInv, mul_smul_comm, mul_sub, mul_one, hquad]
  rw [add_sub_cancel_left, smul_smul, invOf_mul_self, one_smul]

/-- `σ_i⁻¹ · σ_i = 1` when `q` is invertible (sorry-free). -/
theorem σInv_mul_σ (i : Fin n) :
    σInv K q n i * σ K q n i = 1 := by
  have hquad := σ_quadratic K q n i
  simp only [σInv, smul_mul_assoc, sub_mul, one_mul, hquad]
  rw [add_sub_cancel_left, smul_smul, invOf_mul_self, one_smul]

/-- **The generators are units (sorry-free).**  When `q` is invertible
    each `σ_i` is a unit of `H_n(q)` with inverse `σInv`; hence the braid
    group maps into `H_n(q)ˣ` (the Hecke representation of braids). -/
noncomputable def σUnit (i : Fin n) : (IwahoriHecke K q n)ˣ where
  val := σ K q n i
  inv := σInv K q n i
  val_inv := σ_mul_σInv K q n i
  inv_val := σInv_mul_σ K q n i

theorem isUnit_σ (i : Fin n) : IsUnit (σ K q n i) :=
  ⟨σUnit K q n i, rfl⟩

end Units

end IwahoriHecke

end QOU.Hecke
