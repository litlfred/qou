import Mathlib.Tactic

/-!
# Excitation in `H₂(q)`: what the Gröbner–Shirshov normal form keeps

Owner question (2026-11-21): is an excited electron a non-reduced word?

`H₂(q)` has Gröbner–Shirshov basis `{σ² → h·σ + 1}` with `h = q − q⁻¹`, so every element has
the unique normal form `b + a·σ`. We represent it as the pair `(b, a)` and reduce a signed
braid word `w` (letters `σ`, `σ⁻¹`, encoded `true`, `false`) left to right; `σ⁻¹ = σ − h`.

Results (all over a generic field `R`, `q ≠ 0`):

* `chi_nf` — the index character `χ(b + aσ) = b + q·a` (the one-dimensional representation
  `σ ↦ q`) of the normal form of **any** signed word equals `q ^ writhe w`. The normal form
  forgets how many rewrites were made, but `χ` of it recovers the writhe exactly. So the
  corpus's shell reading `n = (w − 1)/2` (`hydrogen-orbitals.md`) is a function of the
  normal form: `χ(NF) = q^(2n+1)`.
* `chi_nf_append_two` — two added positive crossings multiply `χ` by `q²`.
* `nf_pow_a`, `nf_pow_b` — closed form of `NF(σ^m) = b_m + a_m σ`:
  `(q + q⁻¹)·a_m = q^m − (−q⁻¹)^m`, `(q + q⁻¹)·b_m = q⁻¹·q^m + q·(−q⁻¹)^m`.
  Every power `σ^m`, `m ≥ 2`, is non-reduced, the trefoil `σ³` included; the normal form stays
  in `span{1, σ}` and the excitation level appears only as the `q`-degree of the coefficients.
-/

namespace QOU.Excitation

variable {R : Type*} [Field R]

/-- The element `b + a·σ` of `H₂(q)` in Gröbner–Shirshov normal form. -/
@[ext] structure H2 (R : Type*) where
  b : R
  a : R

/-- `h = q − q⁻¹`. -/
def hh (q : R) : R := q - q⁻¹

/-- Right multiplication by `σ`, using `σ² = h·σ + 1`:
`(b + aσ)·σ = a + (b + h·a)σ`. -/
def mulS (q : R) (x : H2 R) : H2 R := ⟨x.a, x.b + hh q * x.a⟩

/-- Right multiplication by `σ⁻¹ = σ − h`: `(b + aσ)·σ⁻¹ = (a − h·b) + bσ`. -/
def mulSinv (q : R) (x : H2 R) : H2 R := ⟨x.a - hh q * x.b, x.b⟩

/-- One letter: `true` = `σ`, `false` = `σ⁻¹`. -/
def step (q : R) (x : H2 R) (l : Bool) : H2 R := if l then mulS q x else mulSinv q x

/-- Normal form of a signed word, reduced left to right from `1`. -/
def nf (q : R) (w : List Bool) : H2 R := w.foldl (step q) ⟨1, 0⟩

/-- Writhe of a signed word. -/
def writhe : List Bool → ℤ
  | [] => 0
  | l :: w => (if l then 1 else -1) + writhe w

/-- Index character `σ ↦ q`, read off the normal form. -/
def chi (q : R) (x : H2 R) : R := x.b + q * x.a

theorem chi_mulS (q : R) (hq : q ≠ 0) (x : H2 R) : chi q (mulS q x) = q * chi q x := by
  simp only [chi, mulS, hh]; field_simp; ring

theorem chi_mulSinv (q : R) (hq : q ≠ 0) (x : H2 R) : chi q (mulSinv q x) = q⁻¹ * chi q x := by
  simp only [chi, mulSinv, hh]; field_simp; ring

theorem writhe_append (w v : List Bool) : writhe (w ++ v) = writhe w + writhe v := by
  induction w with
  | nil => simp [writhe]
  | cons l w ih => simp [writhe, ih]; ring

theorem chi_foldl (q : R) (hq : q ≠ 0) (w : List Bool) (x : H2 R) :
    chi q (w.foldl (step q) x) = chi q x * q ^ writhe w := by
  induction w generalizing x with
  | nil => simp [writhe]
  | cons l w ih =>
    rw [List.foldl_cons, ih]
    cases l
    · simp only [step, Bool.false_eq_true, if_false, writhe]
      rw [chi_mulSinv q hq, zpow_add₀ hq]; simp; ring
    · simp only [step, if_true, writhe]
      rw [chi_mulS q hq, zpow_add₀ hq]; simp; ring

/-- **The normal form remembers the writhe.** For every signed word `w`,
`χ(NF(w)) = q ^ writhe(w)`. -/
theorem chi_nf (q : R) (hq : q ≠ 0) (w : List Bool) : chi q (nf q w) = q ^ writhe w := by
  unfold nf; rw [chi_foldl q hq]; simp [chi]

/-- Two added positive crossings (the corpus's `w → w + 2` per shell) multiply `χ` by `q²`. -/
theorem chi_nf_append_two (q : R) (hq : q ≠ 0) (w : List Bool) :
    chi q (nf q (w ++ [true, true])) = q ^ 2 * chi q (nf q w) := by
  rw [chi_nf q hq, chi_nf q hq, writhe_append]
  simp only [writhe]; rw [zpow_add₀ hq]; norm_num; rw [mul_comm]; norm_cast

theorem nf_replicate_succ (q : R) (m : ℕ) :
    nf q (List.replicate (m + 1) true) = mulS q (nf q (List.replicate m true)) := by
  simp [nf, List.replicate_succ', List.foldl_append, step]

/-- Closed form of the normal form of `σ^m`, both coefficients at once. -/
theorem nf_pow (q : R) (hq : q ≠ 0) (m : ℕ) :
    (q + q⁻¹) * (nf q (List.replicate m true)).a = q ^ m - (-q⁻¹) ^ m ∧
    (q + q⁻¹) * (nf q (List.replicate m true)).b = q⁻¹ * q ^ m + q * (-q⁻¹) ^ m := by
  induction m with
  | zero => simp [nf]; ring
  | succ m ih =>
    obtain ⟨ha, hb⟩ := ih
    have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
    rw [nf_replicate_succ]
    simp only [mulS, hh]
    constructor
    · rw [mul_add, hb, show (q + q⁻¹) * ((q - q⁻¹) * (nf q (List.replicate m true)).a)
          = (q - q⁻¹) * ((q + q⁻¹) * (nf q (List.replicate m true)).a) by ring, ha]
      field_simp
      linear_combination (-(q⁻¹ ^ m * (-1) ^ m)) * hqi
    · rw [ha]; field_simp
      linear_combination (q * q⁻¹ ^ m * (-1) ^ m) * hqi

theorem nf_pow_a (q : R) (hq : q ≠ 0) (m : ℕ) :
    (q + q⁻¹) * (nf q (List.replicate m true)).a = q ^ m - (-q⁻¹) ^ m := (nf_pow q hq m).1

theorem nf_pow_b (q : R) (hq : q ≠ 0) (m : ℕ) :
    (q + q⁻¹) * (nf q (List.replicate m true)).b = q⁻¹ * q ^ m + q * (-q⁻¹) ^ m :=
  (nf_pow q hq m).2

/-- The ground-state trefoil `σ³` is already non-reduced: `NF(σ³) = h + (h² + 1)σ`. -/
theorem nf_trefoil (q : R) :
    nf q [true, true, true] = ⟨hh q, hh q * hh q + 1⟩ := by
  simp [nf, step, mulS]; ring

end QOU.Excitation
