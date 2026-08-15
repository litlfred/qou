/-
# Bring elliptic factor — the α_EM 1/(8π) magnitude leg (durable findings record)

Supports the α_EM single-wall reduction (`1/(8π) = [η-modular value at τ_Bring] ×
[RT (2π)-prescription]`, audit `2026-07-17-alpha-em-kronecker-elliptic-determinant.md`,
PR #3864): `τ_Bring` is the modulus of the elliptic isogeny factor `E` of
`Jac(Bring) ~ E⁴`, and `E ≃ Bring/S₄`.

This file **locks the machine-checkable core** so the derivation path is not
re-walked (a prior session's hand Riemann–Hurwitz wrongly returned genus 0):

* `std_S4_fixed_is_one_dimensional` — PROVED. The `S₄`-fixed subspace of the S₅
  standard representation `std = {v : Fin 5 → ℚ | ∑ vᵢ = 0}` (S₄ = the
  point-stabilizer permuting the first four coordinates) is the **one-dimensional**
  line `ℚ · (1,1,1,1,-4)`: any fixed vector `(a,a,a,a,e)` with zero sum has
  `e = -(4a)`, i.e. is `a · (1,1,1,1,-4)`.
  Since `H^{1,0}(Bring) ≅ std` (the canonical embedding
  `Bring ⊂ P⁴ = {∑xᵢ = ∑xᵢ² = ∑xᵢ³ = 0}` has hyperplane coordinates equal to the
  standard rep) and `genus(Bring/H) = dim H⁰(Ω)^H` (invariant differentials), this
  gives `genus(Bring/S₄) = 1`: `E` is genuinely an **elliptic curve** (NOT genus 0).

* `std_S4_fixed_generator_in_std` — PROVED. The generator `(1,1,1,1,-4)` lies in
  `std` (zero coordinate sum), so the fixed line is nonzero: dimension is exactly 1.

Discriminator (docstring only, not encoded — see the Python witness
`bring-s4-elliptic-factor-genus-verify` for the machine check): the *other* 4-dim
S₅-irrep `(2,1,1,1) = std ⊗ sign` has `dim((2,1,1,1)^{S₄}) = 0` (invariance under
two transpositions of the sign-twisted action forces every coordinate to vanish).
So the two 4-dim irreps give genus 1 vs 0; the canonical `{∑xᵢ=0}` embedding is
`std = (4,1)`, which is what makes `Bring/S₄` genus 1.

Paper-confirmed literature values (NOT derived here; Braden–Disney-Hogg
arXiv:2208.13692 Thm 2.12 + Prop 4.6, PDF in `library/`): the period is
`τ₀ = -0.5 + 0.186676·i` (transcendental), with `j(τ₀) = -29³·5/2⁵ = -121945/32`,
`j(5τ₀) = -25/2` (conductor-50 Q-isogeny class `50a`; the 5-isogeny is the `X₀(5)`
structure). STRUCTURAL: the Jacobian is `Jac(Bring) ≅ E_{5τ₀}³ × E_{τ₀}` as a complex
torus (period `τ₀·diag(5,5,5,1)`), NOT a single `E⁴`; `B/S₄` is genus-1 isogenous to
`E_{3τ₀}` (the residual `S₄/A₄ = C₂` acts by a 2-torsion *translation*, so genus stays
1 — geometric confirmation of `dim(std^{S₄})=1` proved below). The abelian magnitude
leg (the `SL₂(ℤ)`-invariant per-factor `1/(√Im τ·|η|²)`) is the product
`m(5τ₀)³·m(τ₀) ≈ 1.67789³·1.74146 ≈ 8.226` — recorded, NOT interpreted (Prop 4.6: the
decomposition is not principally-polarized, so this naive product is not the polarized
photon determinant; `8.226 ≈ b₁=8` is a coincidence to be resisted, not a derivation).
The reciprocal `π` remains the RT/Front-2 prescription.

Base ring `ℤ` (the integral form): the standard representation's integral lattice
(the `A₄` root lattice) is a `ℤ`-module; the `S₄`-fixed sublattice has **rank 1**,
equal to the `ℚ`-dimension `dim(std^{S₄}) = 1` of the fixed subspace. Stating the
integral version keeps the proof in Lean core (`omega`, no `Mathlib`/`ProofWidgets`
imports — the Mathlib olean cache is unavailable and a from-source build is blocked
by ProofWidgets' network JS fetch in this sandbox). Standalone library file (no
content-block sidecar); numerical `j`/`τ₀`/magnitude values live in the docstring as
cited literature, not as `ℝ` defs.

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
--       (Bring's curve: Old and New — elliptic quotients, j(τ₀), X₀(5)/X₀(50))
-- Ref: [riera-rodriguez-1992] The period matrix of Bring's curve, Pacific J. Math. 154 (1992)
-- Ref: [braden-northover-2012] Bring's Curve: its Period Matrix and the Vector of
--       Riemann Constants, SIGMA 8 (2012) 065 — explicit anti-holomorphic involution
--       (real structure) on Jac(Bring); corrects the j(τ₀)/j(5τ₀) labelling.
-/
import Init.Data.Int.Basic

namespace QOU.Archimedean.BringEllipticFactor

/-- The `S₄`-fixed sublattice of the S₅ standard representation's integral form is
**rank one** (`= dim_ℚ(std^{S₄}) = 1`): any vector fixed by the point-stabilizer
`S₄` (equal first four coordinates, `a = b = c = d`) with zero coordinate-sum
`a+b+c+d+e = 0` satisfies `e = -(4a)`, hence is the multiple `a · (1,1,1,1,-4)` of a
single generator. This is the content of `genus(Bring/S₄) = 1` (elliptic),
correcting a prior hand-computation that returned genus 0. -/
theorem std_S4_fixed_is_one_dimensional
    {a b c d e : Int} (h1 : a = b) (h2 : b = c) (h3 : c = d)
    (hsum : a + b + c + d + e = 0) :
    b = a ∧ c = a ∧ d = a ∧ e = -(4 * a) := by
  omega

/-- The generator `(1,1,1,1,-4)` of the fixed line lies in `std` (its coordinate
sum is zero), so the `S₄`-fixed sublattice is nonzero — rank **exactly** one. -/
theorem std_S4_fixed_generator_in_std :
    (1 : Int) + 1 + 1 + 1 + (-(4 : Int)) = 0 := by omega

/-- Discriminator (integral form): a vector fixed by the **sign-twisted** action
`(2,1,1,1) = std ⊗ sign` must satisfy `σ·v = -v` for the two transpositions
`(1 2)` and `(1 3)`; over the coordinates this forces every entry to vanish, so
`dim((2,1,1,1)^{S₄}) = 0` (genus 0). Encoded via the two transposition constraints:
`(1 2)`: `b=-a, a=-b, c=-c, d=-d, e=-e`; `(1 3)`: `c=-a, b=-b, a=-c`. -/
theorem signtwist_S4_fixed_is_trivial
    {a b c d e : Int}
    (t12b : b = -a) (t12c : c = -c) (t12d : d = -d) (t12e : e = -e)
    (t13c : c = -a) :
    a = 0 ∧ b = 0 ∧ c = 0 ∧ d = 0 ∧ e = 0 := by
  omega

end QOU.Archimedean.BringEllipticFactor
