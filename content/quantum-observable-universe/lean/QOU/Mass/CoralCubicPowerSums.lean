import Mathlib.Tactic

/-!
# Coral spectral cubic — color-root power sums are q-free

The lever-1 binding Seiberg–Witten differential is `λ_SW = X dz`, with the color coordinate `X` cut
out by the **coral spectral cubic**

    X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1) = 0

(`color-tube-fibers.lean`, `mi-sw-abelianisation-cartan.md`). This cubic — and hence every classical
jet/period built from it — is **q-free**: no quantum-deformation parameter appears. This file records
the color-root power sums `p_n = Σ Xᵢⁿ` for `n = 1,2,3`, computed by Newton's identities from the
cubic's elementary symmetric functions, all equal to the clean q-free polynomials `−(zⁿ+1)`.

**Why this matters (z2bn second probe).** Because the spectral data is q-free, a *classical* (d/dz)
jet prolongation of `λ_SW` yields **q-independent** periods `∮λ_SW^(n)`, which cannot equal the
**q-dependent** binding anchors `a_D^(3) = (q+1)²/(3q)` etc. That q-type-consistency mismatch
**(b)-excludes the classical-jet identification** and forces the binding-kernel prolongation to be a
**q-difference** operator (the bean's "fibre q-difference kernel `R(q,x)`"). See
`computations/substrate/z2bn_prolongation_qdifference_constraint.py` and the audit
`docs/audits/2026-06-25-z2bn-prolongation-qdifference-constraint.md`. Generic base ring `R` — the
absence of any quantum parameter in the statement is the point.
-/

namespace QOU.Mass.CoralPowerSums

variable {R : Type*} [CommRing R]

/-- First elementary symmetric function of the coral cubic's roots: `e₁ = −(z+1)`. -/
def e1 (z : R) : R := -(z + 1)

/-- Second elementary symmetric function: `e₂ = z²+z+1`. -/
def e2 (z : R) : R := z ^ 2 + z + 1

/-- Third elementary symmetric function: `e₃ = −(z³+z²+z+1)`. -/
def e3 (z : R) : R := -(z ^ 3 + z ^ 2 + z + 1)

/-- Power sum `p₁ = Σ Xᵢ = e₁`. -/
def psum1 (z : R) : R := e1 z

/-- Power sum `p₂ = e₁p₁ − 2e₂` (Newton). -/
def psum2 (z : R) : R := e1 z * psum1 z - 2 * e2 z

/-- Power sum `p₃ = e₁p₂ − e₂p₁ + 3e₃` (Newton). -/
def psum3 (z : R) : R := e1 z * psum2 z - e2 z * psum1 z + 3 * e3 z

/-- **Coral-cubic color-root power sums are the q-free polynomials `−(zⁿ+1)`** for `n = 1,2,3`.
The statement lives over a generic commutative ring with `z : R` — **no quantum parameter appears**,
which is exactly the q-freeness that forces the binding prolongation operator to be q-difference
rather than a classical jet (z2bn second probe). Pure ring identities. -/
theorem coral_power_sums (z : R) :
    psum1 z = -(z + 1) ∧ psum2 z = -(z ^ 2 + 1) ∧ psum3 z = -(z ^ 3 + 1) := by
  refine ⟨?_, ?_, ?_⟩ <;> simp only [psum1, psum2, psum3, e1, e2, e3] <;> ring

end QOU.Mass.CoralPowerSums
