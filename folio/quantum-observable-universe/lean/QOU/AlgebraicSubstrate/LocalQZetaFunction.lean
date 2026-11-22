import Mathlib.RingTheory.Polynomial.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic
import Mathlib.Algebra.Polynomial.Laurent

/-!
# QOU.AlgebraicSubstrate.LocalQZetaFunction

Canonical declaration of the local q-zeta function of Bring's curve, shared
by the `q-geometric-langlands` content blocks.

Moved out of the `local-q-zeta-function.lean` content-block sibling (bean
`qou-lsib`, owner-authorised 2026-08-23). Content-block siblings sit outside
the `qou` package's `["QOU", "QOU.+"]` globs, so they are not modules and
cannot import one another; `spectral-half-line.lean` and
`hasse-weil-bound.lean` referenced this structure and simply failed to
compile as a result. `QOU.Archimedean.ParticleKnots` is the same fix applied
to the particle-knot structures.
-/

open Polynomial Complex

namespace QOU.AlgebraicSubstrate

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over `ℤ`). -/
abbrev R_q := LaurentPolynomial ℤ

/-- The formal parameter `q` of the ground ring. -/
def q_param : R_q := LaurentPolynomial.T 1

/-- The formal parameter `q⁻¹` of the ground ring. -/
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The genus of Bring's curve. -/
def bringsGenus : ℕ := 4

/-- **Local q-zeta function** of Bring's curve.

    Encodes the generating function for point counts over finite
    extensions of `F_q`. The characteristic polynomial `P(t)` has degree
    `2g = 8`, with roots `α₁, …, α₈` — the fundamental Frobenius
    eigenvalues.

    LaTeX: `\label{def:local-q-zeta-function}`
    Ref: [leitner2026] Chapter 8, Section 4 -/
structure LocalQZetaFunction where
  /-- The cardinality of the base field, as a real number.

      **Corrected 2026-08-28 (bean `qou-lsib`).** This field was `q : R_q`,
      i.e. a formal Laurent polynomial over `ℤ`. That contradicted both its own
      narrative and every other field of this structure. The `.md` defines the
      object as the classical Weil zeta function of Bring's curve over a finite
      field — it counts `|ℬ(𝔽_{q^n})|`, its polynomial is the characteristic
      polynomial of `Fr_q`, and the Hasse-Weil bound it exists to state is
      `|αᵢ| = √q` — while `eigenvalues` and `charPoly` were already `ℂ`-valued.
      A field size is not a formal parameter, and `√q`, `q^ρ` and `|α|² ≤ q` are
      not statements about `ℤ[q, q⁻¹]`: `R_q` carries no order and no norm, so
      the two downstream results were not merely unproved but unstatable.

      This is the archimedean side of the wall (§7c): the ordering and `rpow`
      the consumers need are exactly the constructs that require `ℝ`. -/
  q : ℝ
  /-- The base field has more than one element, so `q > 0`.

      Restored 2026-08-28. The pre-migration structure carried this field
      commented out, annotated `-- (archimedean; not meaningful over R_q)` --
      an author wanting exactly this hypothesis and unable to state it, which
      is independent evidence for the `q : ℝ` correction above. Its absence is
      why `hasse_weil_bound` referenced a nonexistent `Z.q_pos`. -/
  q_pos : 0 < q
  /-- The 8 fundamental Frobenius eigenvalues `α₁, …, α₈`. -/
  eigenvalues : Fin 8 → ℂ
  /-- No eigenvalue vanishes.

      Frobenius acts invertibly on `H¹`, with `det(Fr_q) = ±q^g ≠ 0`, so no
      root of the characteristic polynomial is zero. It does not follow from
      `charPoly_roots`, which permits zero roots, so it is carried as a field.

      Added 2026-08-28. Without it `eigenvalue_norm_sq_axiom` in
      `hasse-weil-bound.lean` is not merely unproved but FALSE: the all-zeros
      datum satisfies every other field and every hypothesis of that axiom, and
      its conclusion `‖αᵢ‖² = q` then reads `0 = q`, contradicting `q_pos`.
      Machine-checked before the axiom was replaced by a proof. -/
  eigenvalues_ne_zero : ∀ i, eigenvalues i ≠ 0
  /-- The *reversed* characteristic polynomial `P̃(X) = ∏ᵢ (X − αᵢ)`.
      Related to the standard form `P(t) = ∏ᵢ (1 − αᵢ t)` by
      `P(t) = t^{2g} · P̃(1/t)`, so the roots of `P̃` are the eigenvalues
      `αᵢ` themselves (not their reciprocals). We use this convention
      to match Lean's polynomial root factorization. -/
  charPoly : ℂ[X]
  /-- `P̃` has degree `2g = 8`. -/
  charPoly_degree : charPoly.natDegree = 2 * bringsGenus
  /-- `P̃` factors as `∏ᵢ (X − αᵢ)`. -/
  charPoly_roots :
    charPoly = ∏ i : Fin 8, (X - C (eigenvalues i))


/-! ## Weil numbers: the functional-equation partner is the conjugate

Shared by `hasse-weil-bound.lean` and `spectral-half-line.lean`. It lives here
rather than in either sibling because content-block `.lean` siblings sit outside
the package globs and **cannot import one another** (§0a) — and both need it.
-/

/-- **The functional-equation partner is the complex conjugate.** For a nonzero
    `α` with `‖α‖² = q`, the partner `q/α` supplied by the functional equation
    equals `conj α`.

    This is what makes `|α| = √q` a *symmetry* statement rather than a bare
    magnitude bound: the eigenvalue multiset is closed under conjugation. -/
theorem weil_partner_eq_conj (q : ℝ) (α : ℂ) (hα : α ≠ 0)
    (h : ‖α‖ ^ 2 = q) :
    (q : ℂ) / α = (starRingEnd ℂ) α := by
  have hns : (Complex.normSq α : ℂ) = (q : ℂ) := by
    rw [Complex.normSq_eq_norm_sq, h]
  rw [div_eq_iff hα, ← hns, ← Complex.mul_conj]
  ring

/-! ### Non-vacuity of the conjugate-partner theorem

`weil_partner_eq_conj` is only worth stating if it fires. Two witnesses at
`q = 4`: the supersingular real eigenvalue `α = 2`, where the statement is
`4/2 = 2` and the conjugation is invisible; and the genuinely complex `α = 2i`,
where it says `4/(2i) = -2i` — the partner and the conjugate coincide only
because `|α|² = q`. The second is the case the arc actually needs, since
Frobenius eigenvalues of a curve come in conjugate pairs off the real axis. -/

/-- The real (supersingular) witness: `q = 4`, `α = 2`. -/
theorem weil_partner_real_witness :
    ((4 : ℝ) : ℂ) / (2 : ℂ) = (starRingEnd ℂ) (2 : ℂ) :=
  weil_partner_eq_conj 4 2 (by norm_num) (by norm_num)

/-- The complex witness: `q = 4`, `α = 2i`, partner `= −2i = conj α`. -/
theorem weil_partner_complex_witness :
    ((4 : ℝ) : ℂ) / (2 * Complex.I) = (starRingEnd ℂ) (2 * Complex.I) := by
  refine weil_partner_eq_conj 4 _ (by simp [Complex.ext_iff]) ?_
  rw [← Complex.normSq_eq_norm_sq]
  simp [Complex.normSq_mul]
  norm_num

end

end QOU.AlgebraicSubstrate
