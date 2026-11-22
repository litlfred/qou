import Mathlib.Algebra.Module.LinearMap.End

/-!
# QOU.Mass.sl2_prolongation_recurrence — symplectic ⇒ one-parameter recurrence

Keystone, final structural step. The depth of the prolonged-period
recurrence is `2` (`s5_bring_hodge_depth.py`: `H¹ = 2·W`, Schur ⇒
`M = id_W ⊗ B` with `B` a 2×2 operator). The Gauss–Manin monodromy
preserves the curve's principal polarisation (the cup-product symplectic
form), so `B ∈ Sp(2) = SL₂` ⇒ **`det B = 1`**, i.e. Cayley–Hamilton reads
`B² = τ • B − 1` with `τ = tr B`.

This lemma shows that constraint collapses the kernel `R = x² − τ x + det B`
to **one parameter**: with `det B = 1` the prolonged periods obey the
"Lucas/Chebyshev" recurrence `a_{n+2} = τ · a_{n+1} − a_n`. (The torus
sector confirms the form: its recurrence is `x² − 2cosh(2η₀) x + 1`, `det = 1`.)

LaTeX label: `prop:sl2-prolongation-recurrence`.

**Ground ring**: generic `[CommRing R]`. See `GroundRingAnnotations.lean`.
-/

namespace QOU.Mass

variable {R : Type*} [CommRing R] {V : Type*} [AddCommGroup V] [Module R V]

/-- **Symplectic ⇒ one-parameter recurrence.** If the 2×2 prolongation
operator `B` satisfies the `SL₂` Cayley–Hamilton relation `B² = τ • B − 1`
(`det B = 1`, `τ = tr B`), then its powers — and hence the prolonged
periods `a n = φ(Bⁿ v₀)` — obey `a_{n+2} = τ · a_{n+1} − a_n`. -/
-- Ref: [leitner2026] §mass-theory/sl2-prolongation-recurrence
theorem sl2_prolongation_recurrence (B : Module.End R V) (τ : R)
    (hCH : B ^ 2 = τ • B - 1) (n : ℕ) :
    B ^ (n + 2) = τ • B ^ (n + 1) - B ^ n := by
  rw [pow_add, hCH, mul_sub, mul_one, mul_smul_comm, ← pow_succ]

end QOU.Mass
