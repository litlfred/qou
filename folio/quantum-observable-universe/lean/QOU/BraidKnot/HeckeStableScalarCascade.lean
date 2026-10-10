import QOU.BraidKnot.HeckeJucysMurphyElements

/-!
# The stable Hecke algebra collapses irreducible representations to scalars

`HeckeGenerators` (`HeckeJucysMurphyElements.lean`) presents the **stable** algebra `H_∞(q)`: its
`hecke`, `braid` and `far` relations are quantified over **all** `i : ℕ`.  This file proves that
that arity is not a harmless over-generalisation.  It carries a genuine obstruction:

> **No representation on which `σ₀` and `σ₁` act irreducibly can be a `HeckeGenerators` instance.**

The mechanism is Schur, not dimension.  `far` forces `σ₃` to commute with both `σ₀` and `σ₁`;
if those two generate the full endomorphism algebra, Schur makes `σ₃` a scalar, and then a
**downward cascade** along the braid relation drags `σ₂`, `σ₁`, `σ₀` down to that same scalar.

## What is proved here

* `sigma_eq_of_succ_scalar` — the cascade step, in any `HeckeGenerators` over a field with
  `Nontrivial A`: if `σ (i+1)` is a scalar `s`, then `σ i` is **the same** scalar `s`.
* `sigma_scalar_of_schur` — the exclusion: under a Schur hypothesis on `{σ₀, σ₁}`, `σ₁` is scalar.
* `stdTwo_hecke0` / `stdTwo_hecke1` / `stdTwo_braid` — the explicit 2×2 Young seminormal matrices
  really do satisfy the `H₃(q)` relations, over any field with `q ≠ 0`.
* `stdTwo_centralizer_scalar` — their joint centralizer is exactly the scalars.
* `stdTwo_no_stable_extension` — hence **no** `HeckeGenerators` instance restricts to them.

## Why this matters (bean `qou-t1kv`)

`QOU/Archimedean/HeckeH3.lean` carries `stdRep3`, the 2-dimensional `(2,1)` representation of
`H₃(q)`, with its Hecke and braid relations already proved.  It is the obvious multi-dimensional
witness for `IsJMWeight` (`HeckeSeminormalWeight.lean`), which is currently non-vacuous only at the
**one-dimensional** `scalarGenerators`.  `stdTwo_no_stable_extension` shows that plugging it in is
not merely awkward but **impossible**: the obstruction is real, and a bounded-index variant of the
class (relations required only for `i < n - 1`) is the only route to a `dim > 1` witness.

This is a **scope-(b) structural exclusion** in the sense of `AGENTS.md`: the invariant that
forbids the construction is proved here, not inferred from a failed search.

## Exactly what is excluded — the exclusion does NOT reach reducible representations

The hypothesis that does the work is the **centralizer condition** `sigma_scalar_of_schur.schur`,
not "irreducible" and not "`dim > 1`".  A reducible representation has a non-scalar idempotent in
its centralizer, so it simply fails that hypothesis and the theorem says nothing about it.

That is not a hedge — §5 **proves the boundary is real**: `existsNonscalar_heckeGenerators`
exhibits a genuine `HeckeGenerators` instance on `2×2` matrices whose generators are **not
scalar**, namely the constant diagonal `σᵢ = diag(q, −q⁻¹)` for every `i`.  It is reducible (the
two coordinate lines are invariant), so:

* **`dim > 1` instances exist.**  Any reading of this file as "no multi-dimensional instance
  exists" is wrong, and `constGenerators` is the counterexample.
* **The Schur hypothesis is load-bearing, and the exclusion is sharp.**  What `H_∞` cannot host is
  an *irreducible* action, not a big one.

(Raised by the sibling `Sym²`-gate PR #5764, where an irrep-level exclusion was being read as
covering arbitrary objects — `V_{1/2} ⊕ V_0` has dimension 3, is not an irrep, and passes.  Same
shape of trap, so the boundary is proved here rather than asserted.)

Refs:
- [jones1987] V. Jones, Hecke algebra representations of braid groups and link polynomials.
- [wenzl1988] H. Wenzl, Hecke algebras of type A_n and subfactors.
-/

namespace QOU.BraidKnot.Hecke

open Matrix

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R}

/-! ## §1  A scalar generator is a root of the Hecke quadratic -/

/-- If a generator is the scalar `s`, the Hecke relation forces `s² = (q − q⁻¹)s + 1`.

`Nontrivial A` is what makes `algebraMap` from the field `R` injective; without it `A` is the
zero ring and every relation holds vacuously. -/
theorem scalar_hecke_root [Nontrivial A] (H : HeckeGenerators R A q) (i : ℕ) (s : R)
    (h : H.σ i = algebraMap R A s) : s * s = (q - q⁻¹) * s + 1 := by
  have hh := H.hecke i
  rw [h] at hh
  have hmap : algebraMap R A (s * s) = algebraMap R A ((q - q⁻¹) * s + 1) := by
    simpa using hh
  exact (algebraMap R A).injective hmap

/-- The scalar in `scalar_hecke_root` is a unit: `s · (s − (q − q⁻¹)) = 1`. -/
theorem scalar_mul_sub_eq_one [Nontrivial A] (H : HeckeGenerators R A q) (i : ℕ) (s : R)
    (h : H.σ i = algebraMap R A s) : s * (s - (q - q⁻¹)) = 1 := by
  have := scalar_hecke_root H i s h
  linear_combination this

/-! ## §2  The downward cascade -/

/-- **Cascade step.**  In `H_∞(q)`, if `σ (i+1)` is the scalar `s` then `σ i` is *the same*
scalar `s`.

Proof: the braid relation at `i` reads `σᵢ · s · σᵢ = s · σᵢ · s`.  Scalars are central, so this
is `s · σᵢ² = s² · σᵢ`.  Substituting the Hecke relation `σᵢ² = (q − q⁻¹)σᵢ + 1` and collecting
gives `s·(s − (q − q⁻¹)) · σᵢ = s`, and the bracket is `1` by `scalar_mul_sub_eq_one`. -/
theorem sigma_eq_of_succ_scalar [Nontrivial A] (H : HeckeGenerators R A q) (i : ℕ) (s : R)
    (h : H.σ (i + 1) = algebraMap R A s) : H.σ i = algebraMap R A s := by
  have hunit : s * (s - (q - q⁻¹)) = 1 := scalar_mul_sub_eq_one H (i + 1) s h
  have hb := H.braid i
  rw [h] at hb
  -- Move the central scalars out of both sides.
  have hcom : algebraMap R A s * H.σ i = H.σ i * algebraMap R A s := Algebra.commutes s (H.σ i)
  have hL : H.σ i * algebraMap R A s * H.σ i
      = algebraMap R A s * (H.σ i * H.σ i) := by
    rw [← hcom, mul_assoc]
  have hR : algebraMap R A s * H.σ i * algebraMap R A s
      = algebraMap R A (s * s) * H.σ i := by
    rw [mul_assoc, ← hcom, map_mul, mul_assoc]
  rw [hL, hR, H.hecke i, mul_add, mul_one] at hb
  -- hb : s·((q−q⁻¹)·σᵢ) + s = (s·s)·σᵢ
  have key : algebraMap R A (s * (s - (q - q⁻¹))) * H.σ i = algebraMap R A s := by
    have expand : algebraMap R A (s * (s - (q - q⁻¹))) * H.σ i
        = algebraMap R A (s * s) * H.σ i
          - algebraMap R A s * (algebraMap R A (q - q⁻¹) * H.σ i) := by
      simp [map_mul, map_sub, mul_sub, sub_mul, mul_assoc]
    rw [expand, ← hb]
    abel
  rw [hunit, map_one, one_mul] at key
  exact key

/-- **Downward propagation.**  A scalar at index `j` forces the same scalar at every `i ≤ j`. -/
theorem sigma_eq_of_le_of_scalar [Nontrivial A] (H : HeckeGenerators R A q) (s : R) :
    ∀ (k : ℕ) (j : ℕ), H.σ (j + k) = algebraMap R A s → H.σ j = algebraMap R A s := by
  intro k
  induction k with
  | zero => intro j h; simpa using h
  | succ n ih =>
      intro j h
      have h' : H.σ ((j + n) + 1) = algebraMap R A s := by
        rw [show (j + n) + 1 = j + (n + 1) by ring]; exact h
      exact ih j (sigma_eq_of_succ_scalar H (j + n) s h')

/-! ## §3  Schur forces every generator to be scalar -/

/-- **The exclusion.**  If the joint centralizer of `σ₀` and `σ₁` consists of scalars — the Schur
condition satisfied by any irreducible representation — then `σ₁` is itself a scalar.

`far` places `σ₃` in that centralizer (`0 + 1 < 3` and `1 + 1 < 3`), so `σ₃` is a scalar `s`; the
cascade of §2 then drags `σ₂` and `σ₁` down to `s`. -/
theorem sigma_scalar_of_schur [Nontrivial A] (H : HeckeGenerators R A q)
    (schur : ∀ x : A, x * H.σ 0 = H.σ 0 * x → x * H.σ 1 = H.σ 1 * x →
      ∃ c : R, x = algebraMap R A c) :
    ∃ c : R, H.σ 1 = algebraMap R A c := by
  obtain ⟨s, hs⟩ := schur (H.σ 3) (H.far 0 3 (by norm_num)).symm (H.far 1 3 (by norm_num)).symm
  refine ⟨s, ?_⟩
  exact sigma_eq_of_le_of_scalar H s 2 1 (by simpa using hs)

/-! ## §4  The explicit 2-dimensional `H₃(q)` representation -/

section StdTwo

variable {K : Type*} [Field K]

/-- `σ₀` in Young seminormal form for the `(2,1)` representation of `H₃(q)`. -/
noncomputable def stdTwo0 (q : K) : Matrix (Fin 2) (Fin 2) K := !![q, 1; 0, -q⁻¹]

/-- `σ₁` in Young seminormal form for the `(2,1)` representation of `H₃(q)`. -/
noncomputable def stdTwo1 (q : K) : Matrix (Fin 2) (Fin 2) K := !![-q⁻¹, 0; 1, q]

/-- `σ₀` satisfies the Hecke relation. -/
-- Ref: [jones1987] Hecke algebra representations of braid groups and link polynomials.
theorem stdTwo_hecke0 {q : K} (hq : q ≠ 0) :
    stdTwo0 q * stdTwo0 q = (q - q⁻¹) • stdTwo0 q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [stdTwo0, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- `σ₁` satisfies the Hecke relation. -/
-- Ref: [jones1987] Hecke algebra representations of braid groups and link polynomials.
theorem stdTwo_hecke1 {q : K} (hq : q ≠ 0) :
    stdTwo1 q * stdTwo1 q = (q - q⁻¹) • stdTwo1 q + 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [stdTwo1, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- `σ₀` and `σ₁` satisfy the braid relation. -/
-- Ref: [wenzl1988] Hecke algebras of type A_n and subfactors.
theorem stdTwo_braid {q : K} (hq : q ≠ 0) :
    stdTwo0 q * stdTwo1 q * stdTwo0 q = stdTwo1 q * stdTwo0 q * stdTwo1 q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [stdTwo0, stdTwo1, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- `σ₀`'s Hecke relation in the **class's own vocabulary** (`algebraMap`, not `•`), so that the
non-vacuity claim is literally the relation `HeckeGenerators.hecke` demands. -/
theorem stdTwo_hecke0_algebraMap {q : K} (hq : q ≠ 0) :
    stdTwo0 q * stdTwo0 q
      = algebraMap K (Matrix (Fin 2) (Fin 2) K) (q - q⁻¹) * stdTwo0 q + 1 := by
  rw [Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]
  exact stdTwo_hecke0 hq

/-- `σ₁`'s Hecke relation in the class's own vocabulary. -/
theorem stdTwo_hecke1_algebraMap {q : K} (hq : q ≠ 0) :
    stdTwo1 q * stdTwo1 q
      = algebraMap K (Matrix (Fin 2) (Fin 2) K) (q - q⁻¹) * stdTwo1 q + 1 := by
  rw [Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]
  exact stdTwo_hecke1 hq

/-- **Schur for the explicit pair.**  Anything commuting with both `σ₀` and `σ₁` is scalar. -/
theorem stdTwo_centralizer_scalar {q : K} (x : Matrix (Fin 2) (Fin 2) K)
    (h0 : x * stdTwo0 q = stdTwo0 q * x) (h1 : x * stdTwo1 q = stdTwo1 q * x) :
    x = algebraMap K (Matrix (Fin 2) (Fin 2) K) (x 0 0) := by
  have e00 := congr_fun (congr_fun h0 0) 0
  have e10 := congr_fun (congr_fun h1 1) 0
  have e11 := congr_fun (congr_fun h1 0) 0
  simp [stdTwo0, stdTwo1, Matrix.mul_apply, Fin.sum_univ_two] at e00 e10 e11
  have h10 : x 1 0 = 0 := by linear_combination -e00
  have h01 : x 0 1 = 0 := by linear_combination e11
  have h11 : x 1 1 = x 0 0 := by rw [h10] at e10; linear_combination e10
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Algebra.algebraMap_eq_smul_one, h10, h01, h11]

/-- `σ₁` of the explicit pair is **not** a scalar: its `(1,0)` entry is `1`. -/
theorem stdTwo1_not_scalar {q : K} (c : K) :
    stdTwo1 q ≠ algebraMap K (Matrix (Fin 2) (Fin 2) K) c := by
  intro h
  have he := congr_fun (congr_fun h 1) 0
  simp [stdTwo1, Algebra.algebraMap_eq_smul_one] at he

/-- **The obstruction, concretely.**  There is no `HeckeGenerators` structure on `2×2` matrices
whose first two generators are the `(2,1)` seminormal pair.

So the stable presentation cannot host `stdRep3`, and the `dim > 1` witness for `IsJMWeight`
cannot be obtained by instantiating the class as it stands (bean `qou-t1kv`). -/
theorem stdTwo_no_stable_extension {q : K}
    (H : HeckeGenerators K (Matrix (Fin 2) (Fin 2) K) q)
    (h0 : H.σ 0 = stdTwo0 q) (h1 : H.σ 1 = stdTwo1 q) : False := by
  obtain ⟨c, hc⟩ := sigma_scalar_of_schur H (fun x hx0 hx1 => by
    refine ⟨x 0 0, stdTwo_centralizer_scalar (q := q) x ?_ ?_⟩
    · rw [← h0]; exact hx0
    · rw [← h1]; exact hx1)
  rw [h1] at hc
  exact stdTwo1_not_scalar c hc

/-! ## §5  The exclusion is sharp: a non-scalar (reducible) instance exists -/

end StdTwo

/-- **Constant generators.**  Any Hecke-quadratic unit `X` gives a `HeckeGenerators` with
`σᵢ = X` for every `i`.

Braid and far-commutation are `rfl` once all generators coincide, so the only real content is the
Hecke relation.  This is the general form of the counterexample that refutes reading the cascade
as a statement about dimension. -/
def constGenerators (X Xi : A) (hX : X * Xi = 1) (hXi : Xi * X = 1)
    (hHecke : X * X = algebraMap R A (q - q⁻¹) * X + 1) : HeckeGenerators R A q where
  σ _ := X
  σinv _ := Xi
  mul_σinv _ := hX
  σinv_mul _ := hXi
  hecke _ := hHecke
  braid _ := rfl
  far _ _ _ := rfl

section Sharp

variable {K : Type*} [Field K]

/-- The reducible 2-dimensional generator `diag(q, −q⁻¹)`: the two Hecke eigenvalues placed on
the diagonal, so each coordinate line is invariant. -/
noncomputable def diagTwo (q : K) : Matrix (Fin 2) (Fin 2) K := !![q, 0; 0, -q⁻¹]

/-- Its inverse `diag(q⁻¹, −q)`. -/
noncomputable def diagTwoInv (q : K) : Matrix (Fin 2) (Fin 2) K := !![q⁻¹, 0; 0, -q]

theorem diagTwo_mul_inv {q : K} (hq : q ≠ 0) : diagTwo q * diagTwoInv q = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [diagTwo, diagTwoInv, Matrix.mul_apply, Fin.sum_univ_two, hq]

theorem diagTwoInv_mul {q : K} (hq : q ≠ 0) : diagTwoInv q * diagTwo q = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [diagTwo, diagTwoInv, Matrix.mul_apply, Fin.sum_univ_two, hq]

/-- `diag(q, −q⁻¹)` satisfies the Hecke relation, in the class's `algebraMap` vocabulary. -/
theorem diagTwo_hecke {q : K} (hq : q ≠ 0) :
    diagTwo q * diagTwo q
      = algebraMap K (Matrix (Fin 2) (Fin 2) K) (q - q⁻¹) * diagTwo q + 1 := by
  rw [Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [diagTwo, Matrix.mul_apply, Fin.sum_univ_two] <;> field_simp <;> ring

/-- It is **not** a scalar matrix, provided `q² ≠ −1` (i.e. `q ≠ −q⁻¹`, so the two Hecke
eigenvalues are distinct). -/
theorem diagTwo_not_scalar {q : K} (hq : q ≠ 0) (hq2 : q * q + 1 ≠ 0) (c : K) :
    diagTwo q ≠ algebraMap K (Matrix (Fin 2) (Fin 2) K) c := by
  intro h
  have e00 := congr_fun (congr_fun h 0) 0
  have e11 := congr_fun (congr_fun h 1) 1
  simp [diagTwo, Algebra.algebraMap_eq_smul_one] at e00 e11
  -- q = c and -q⁻¹ = c, so q = -q⁻¹, i.e. q² = -1
  apply hq2
  field_simp at e11
  linear_combination q * e00 - e11

/-- **The exclusion is sharp.**  There *is* a `HeckeGenerators` instance on `2×2` matrices whose
generators are not scalar — so `H_∞(q)` does have multi-dimensional representations, and what
§3 excludes is precisely the **irreducible** ones.

Any reading of `stdTwo_no_stable_extension` as "no `dim > 1` instance exists" is refuted by this. -/
theorem existsNonscalar_heckeGenerators {q : K} (hq : q ≠ 0) (hq2 : q * q + 1 ≠ 0) :
    ∃ H : HeckeGenerators K (Matrix (Fin 2) (Fin 2) K) q,
      ∀ c : K, H.σ 0 ≠ algebraMap K (Matrix (Fin 2) (Fin 2) K) c :=
  ⟨constGenerators (diagTwo q) (diagTwoInv q) (diagTwo_mul_inv hq) (diagTwoInv_mul hq)
      (diagTwo_hecke hq),
   fun c => diagTwo_not_scalar hq hq2 c⟩

end Sharp

end QOU.BraidKnot.Hecke
