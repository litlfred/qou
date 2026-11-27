import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Basic
import Mathlib.Tactic

/-!
# QOU.EightfoldWay.HyperchargeUniqueness — hypercharge is unique up to scale on `V ⊕ W*`

Track C1 of session epic `qou-x08k`, uniqueness half.  Take the two fundamentals of the
flavoured definition (`def:flavoured-quantum-observable-universe`): `V` with `Λ²V ≅ 𝟙` and
`W` with `Λ³W ≅ 𝟙`, and the split bundle `F = V ⊕ W*` of the flavour-charges remark.  The two
volume forms give one on `F`, `Λ⁵F ≅ Λ²V ⊗ Λ³W* ≅ 𝟙`, so infinitesimal symmetries of `F`
are **traceless**.

* `hypercharge_unique` — a traceless operator on `F` commuting with `𝔰𝔩(V)` and `𝔰𝔩(W*)`
  (their split `ℚ`-forms, given by raising and lowering operators) is a multiple of
  `Y = diag(3, 3, -2, -2, -2)`.
* `hypercharge_ratio` — hence on `F` the hypercharges satisfy `y₃ = -⅔ y₂`.

So the extended axioms leave room for exactly one abelian generator commuting with both
gauge factors.  Its **scale** is not fixed here, and the identification of `F` with a
fermion multiplet is the flavour-charges remark's, not this file's.  This is a consequence
of the postulated `W`, not a derivation of hypercharge from knot data; the
crossing-invariant route of `conj:sm-hypercharge-invariant` is a separate, open question.

Base `ℚ`; exact certificate by Gaussian elimination; no empirical input.
-/

namespace QOU.EightfoldWay.HyperchargeUniqueness

/-- The raising operator of 𝔰𝔩(V) on `F = V ⊕ W*`. -/
def E₂ : Matrix (Fin 5) (Fin 5) ℚ :=
  !![(0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)]

/-- The lowering operator of 𝔰𝔩(V) on `F = V ⊕ W*`. -/
def F₂ : Matrix (Fin 5) (Fin 5) ℚ :=
  !![(0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)]

/-- The first raising operator of 𝔰𝔩(W*) on `F = V ⊕ W*`. -/
def E₃₁ : Matrix (Fin 5) (Fin 5) ℚ :=
  !![(0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)]

/-- The first lowering operator of 𝔰𝔩(W*) on `F = V ⊕ W*`. -/
def F₃₁ : Matrix (Fin 5) (Fin 5) ℚ :=
  !![(0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)]

/-- The second raising operator of 𝔰𝔩(W*) on `F = V ⊕ W*`. -/
def E₃₂ : Matrix (Fin 5) (Fin 5) ℚ :=
  !![(0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)]

/-- The second lowering operator of 𝔰𝔩(W*) on `F = V ⊕ W*`. -/
def F₃₂ : Matrix (Fin 5) (Fin 5) ℚ :=
  !![(0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ)]

/-- The hypercharge generator `Y = diag(3, 3, -2, -2, -2)` on `F = V ⊕ W*`. -/
def Ydiag : Matrix (Fin 5) (Fin 5) ℚ := Matrix.diagonal ![3, 3, -2, -2, -2]

set_option linter.unusedSimpArgs false in
set_option linter.unreachableTactic false in
set_option linter.unnecessarySeqFocus false in
set_option maxHeartbeats 4000000 in
/-- **Hypercharge is unique up to scale.**  A traceless operator on `V ⊕ W*` commuting with
`𝔰𝔩(V)` and `𝔰𝔩(W*)` is `(-X₄₄/2) • Y`. -/
theorem hypercharge_unique (X : Matrix (Fin 5) (Fin 5) ℚ)
    (he2 : X * E₂ = E₂ * X)
    (hf2 : X * F₂ = F₂ * X)
    (he3a : X * E₃₁ = E₃₁ * X)
    (hf3a : X * F₃₁ = F₃₁ * X)
    (he3b : X * E₃₂ = E₃₂ * X)
    (_hf3b : X * F₃₂ = F₃₂ * X)
    (htr : Matrix.trace X = 0) :
    X = (-(X 4 4) / 2) • Ydiag := by
  ext i j
  fin_cases i <;> fin_cases j
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      (1/2) * (congrFun (congrFun he2 0) 1) + (-1/2) * (congrFun (congrFun he3a 2) 3) + -(congrFun (congrFun he3b 3) 4) + (1/2) * (htr)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      (congrFun (congrFun hf2 0) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      -(congrFun (congrFun hf2 1) 2)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      -(congrFun (congrFun hf2 1) 3)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      -(congrFun (congrFun hf2 1) 4)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      -(congrFun (congrFun he2 0) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      (-1/2) * (congrFun (congrFun he2 0) 1) + (-1/2) * (congrFun (congrFun he3a 2) 3) + -(congrFun (congrFun he3b 3) 4) + (1/2) * (htr)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      -(congrFun (congrFun he2 0) 2)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      -(congrFun (congrFun he2 0) 3)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      -(congrFun (congrFun he2 0) 4)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      (congrFun (congrFun he2 2) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      (congrFun (congrFun hf2 2) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      (congrFun (congrFun he3a 2) 3) + (congrFun (congrFun he3b 3) 4)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      (congrFun (congrFun hf3a 2) 2)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      -(congrFun (congrFun hf3a 3) 4)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      (congrFun (congrFun he2 3) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      (congrFun (congrFun hf2 3) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      -(congrFun (congrFun he3a 2) 2)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      (congrFun (congrFun he3b 3) 4)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      -(congrFun (congrFun he3a 2) 4)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      (congrFun (congrFun he2 4) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      (congrFun (congrFun hf2 4) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      (congrFun (congrFun he3a 4) 3)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_five, Matrix.trace, Matrix.diag, E₂, F₂, E₃₁, F₃₁, E₃₂, F₃₂, Ydiag, Matrix.smul_apply, Matrix.diagonal] <;> ring1))
      (congrFun (congrFun hf3a 4) 2)
  · simp [Ydiag, Matrix.diagonal]

/-- **The hypercharge ratio.**  The `V`-eigenvalue and `W*`-eigenvalue of `Y` satisfy
`y₃ = -⅔ y₂`; with `Y` unique up to scale, so does every admissible hypercharge. -/
theorem hypercharge_ratio : Ydiag 2 2 = -(2 / 3) * Ydiag 0 0 := by
  simp [Ydiag, Matrix.diagonal]

theorem Ydiag_trace : Matrix.trace Ydiag = 0 := by
  simp [Ydiag, Matrix.trace, Matrix.diagonal, Fin.sum_univ_five]; norm_num

end QOU.EightfoldWay.HyperchargeUniqueness
