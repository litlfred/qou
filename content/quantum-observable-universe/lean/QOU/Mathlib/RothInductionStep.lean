/-
  **The interface of Roth's induction step**, composed and checked in Lean.

  Bean `qou-4lbh`.

  ⚠ Not Mathlib-only: it imports `SeparatedWronskian`, `SeparatedIndex` and `SeparatedHeight`.

  ═══ WHY THIS MODULE EXISTS ═══

  This arc has repeatedly asserted, in module docstrings and bean entries, that its pieces
  "compose" — and has been wrong about that five times.  Prose is not evidence.  The cheap
  check is to write the composition down and let the elaborator decide, which is what this
  module is.

  Everything here is one or two lines given what already exists.  That is the point: if the
  claimed interface is real, the composition is trivial; if it is not, the composition does
  not typecheck.  Both halves below did compose, unchanged — so the claim survives its first
  actual test.

  ═══ WHAT THE STEP NEEDS ═══

  Roth's induction writes the auxiliary polynomial in separated form `∑ₖ φₖ(x)ψₖ(y)`, takes a
  generalized Wronskian of it, and uses that it factors as an `x`-Wronskian times a
  `y`-Wronskian (`det_separated_wronskian`).  To recurse it needs, of that factorisation:

  * the **index** to split — `index_sepW`, exactly additive;
  * the **height** of each factor to be controlled by the height of the whole —
    `abs_coeff_le_of_sepW_left` and `..._right`.

  ⚠ What is still **not** here is the recursion: the parameter conditions (`dⱼ/dⱼ₊₁` growth,
  `ε`, the `qⱼ` hypotheses) and the argument that feeds `RothBaseCase` and the `m−1` case back
  into the `m` case.  This module is its interface, not its proof.
-/
import QOU.Mathlib.SeparatedWronskian
import QOU.Mathlib.SeparatedIndex
import QOU.Mathlib.SeparatedHeight

namespace MvPolynomial

variable {σ τ : Type*}

/-- The **separated Wronskian**: the generalized Wronskian of `∑ₖ φₖ(x)ψₖ(y)` taken with the
mixed operator family `(Dx i) ++ (Dy j)`.  Named so the statements below fit on a page. -/
noncomputable def sepW {K : Type*} [CommRing K] {r : ℕ}
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial τ K) : MvPolynomial (σ ⊕ τ) K :=
  (Matrix.of fun i j => pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr)
    (∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k))).det

/-- `det_separated_wronskian`, restated for `sepW`. -/
theorem sepW_eq {K : Type*} [CommRing K] {r : ℕ}
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial τ K) :
    sepW Dx Dy φ ψ = (rename Sum.inl (mvGenWronskian Dx φ) : MvPolynomial (σ ⊕ τ) K)
      * rename Sum.inr (mvGenWronskian Dy ψ) :=
  det_separated_wronskian Dx Dy φ ψ

/-- **The index half of the induction step:** the separated Wronskian's index is exactly the
sum of the two factors' indices.

One line from `det_separated_wronskian` and `index_separated`.  ⚠ `IsDomain` is used, and only
by `index_separated`'s `≤` half — see that module's header for why it is not removable. -/
theorem index_sepW {K : Type*} [CommRing K] [IsDomain K] {r : ℕ}
    (d₁ : σ → ℕ) (d₂ : τ → ℕ) (α : σ → K) (β : τ → K)
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial τ K) :
    index (Sum.elim d₁ d₂) (Sum.elim α β) (sepW Dx Dy φ ψ)
      = index d₁ α (mvGenWronskian Dx φ) + index d₂ β (mvGenWronskian Dy ψ) := by
  rw [sepW, det_separated_wronskian, index_separated]

/-- **The height half, `x` side:** a height bound on the separated Wronskian bounds the
`x`-Wronskian.

Needs the `y`-Wronskian to be non-zero — which is exactly what the bounded-order criterion
(`BoundedOrderWronskian`) is for. -/
theorem abs_coeff_le_of_sepW_left {r : ℕ}
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (φ : Fin r → MvPolynomial σ ℤ) (ψ : Fin r → MvPolynomial τ ℤ)
    (hψ : mvGenWronskian Dy ψ ≠ 0) {B : ℤ}
    (hB : ∀ n, |coeff n (sepW Dx Dy φ ψ)| ≤ B) (i : σ →₀ ℕ) :
    |coeff i (mvGenWronskian Dx φ)| ≤ B := by
  refine abs_coeff_le_of_mul_separated hψ ?_ i
  intro n
  have h := hB n
  rwa [sepW, det_separated_wronskian] at h

/-- **The height half, `y` side.** -/
theorem abs_coeff_le_of_sepW_right {r : ℕ}
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (φ : Fin r → MvPolynomial σ ℤ) (ψ : Fin r → MvPolynomial τ ℤ)
    (hφ : mvGenWronskian Dx φ ≠ 0) {B : ℤ}
    (hB : ∀ n, |coeff n (sepW Dx Dy φ ψ)| ≤ B) (j : τ →₀ ℕ) :
    |coeff j (mvGenWronskian Dy ψ)| ≤ B := by
  refine abs_coeff_le_of_mul_separated_right hφ ?_ j
  intro n
  have h := hB n
  rwa [sepW, det_separated_wronskian] at h

/-! ### Next

⚠ The recursion itself.  Writing Roth's lemma's statement in Lean — with `dⱼ/dⱼ₊₁` growth, `ε`,
and the `qⱼ` hypotheses — and matching each of its hypotheses to a named theorem is the
remaining work, and is also the check that this arc has learned to run: it is what found the
fifth correction, and it is what this module is a small instance of. -/

end MvPolynomial
