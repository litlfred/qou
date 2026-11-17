import QOU.AlgebraicSubstrate.LocalQZetaFunction
import Mathlib.Algebra.Module.LinearMap.Defs

/-!
# QOU.AlgebraicSubstrate.ReebSpectrum

The shape a Reeb spectrum must have, and the named — **unproved** — hypothesis
tying it to the Frobenius eigenvalues of `LocalQZetaFunction`.

## What this is for (bean `qou-qspc`)

`cor:spectral-half-line` concludes `Re(ρᵢ) = 1/2` for exponents satisfying
`αᵢ = q^{ρᵢ}`, and `exists_spectral_coord` shows such exponents always exist. But
the arc wants to say something stronger — that the **Reeb spectrum** lies on the
critical line — and nothing in the corpus related the two. Measured: the
identifier `ReebEigenvalue` occurred in exactly one file, a content-block sibling
no module can import, and the library's Reeb infrastructure (`ReebEpsilon`,
`QReebFlow`, `ReebDecomposition`) carries no spectrum with complex eigenvalues.

## What this does NOT claim

**It does not say what `ξ_q` is.** The operator is *data*, supplied by whoever
instantiates the structure; this file fixes only the shape any Reeb spectrum must
have — eight modes, each a genuine eigenvector with a complex eigenvalue — and
names the identification as a hypothesis.

That distinction is the whole design. An opaque carrier (`holds : Prop`, or a
structure whose fields promise properties they do not encode) would assert
nothing and could be discharged by `⟨True⟩`; `is_eigen` is a real equation, so an
instance has to produce an operator and vectors that actually satisfy it.
`reebSpectrumExample` below witnesses that the shape is inhabited, so it is not
an empty interface either.

`HasReebSpectralCoords` carries **no instance**. That is the honest open state
(§3b-tax): the identification of the Frobenius exponents with the Reeb spectrum
is precisely what is unproved, and it is now stated where it can be cited and
attacked rather than absent.
-/

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

/-- **The shape of a Reeb spectrum.** An operator on a `ℂ`-module together with
    eight nonzero eigenvectors and their complex eigenvalues.

    `H` and `op` are parameters, not claims: this says what it means to *be* a
    spectrum of eight modes, not which operator the framework's `ξ_q` is. -/
structure ReebSpectrum (H : Type*) [AddCommGroup H] [Module ℂ H] where
  /-- The operator whose spectrum this is (the Reeb derivation, when
      instantiated at it). -/
  op : H →ₗ[ℂ] H
  /-- The eight fundamental modes. -/
  mode : Fin 8 → H
  /-- Their eigenvalues, complex — the critical line is a line in `ℂ`, so a real
      spectrum could not carry the claim `Re(ρ) = 1/2` non-trivially. -/
  spec : Fin 8 → ℂ
  /-- A mode is a genuine eigenvector, not the zero vector. -/
  mode_ne_zero : ∀ i, mode i ≠ 0
  /-- The eigenvalue equation. This is what makes the structure content-bearing:
      an instance must exhibit an operator and vectors satisfying it. -/
  is_eigen : ∀ i, op (mode i) = spec i • mode i

/-- **The identification, as a named hypothesis.** The Frobenius eigenvalues of
    `Z` are the `q`-powers of the Reeb spectrum of `R`.

    This is the open content of bean `qou-qspc`. **No instance is provided** —
    supplying one would assert the identification, which is exactly what is not
    established. Downstream results take it as an explicit `[…]` hypothesis
    (§3b-cond) so the dependency is visible in the type. -/
class HasReebSpectralCoords (Z : LocalQZetaFunction) {H : Type*}
    [AddCommGroup H] [Module ℂ H] (R : ReebSpectrum H) : Prop where
  /-- `αᵢ = q^{ρᵢ}` with `ρᵢ` the `i`-th Reeb eigenvalue. -/
  coords : ∀ i, Z.eigenvalues i = (Z.q : ℂ) ^ (R.spec i)

/-! ## Non-vacuity

The interface is inhabited: `H = ℂ`, the identity operator, every mode `1` with
eigenvalue `1`. Trivial as a spectrum, but it establishes that `ReebSpectrum` is
a shape something can have — unlike a carrier whose fields cannot be satisfied,
and unlike one any `⟨True⟩` discharges. -/

/-- A witness that `ReebSpectrum` is inhabited. -/
def reebSpectrumExample : ReebSpectrum ℂ where
  op := LinearMap.id
  mode := fun _ => 1
  spec := fun _ => 1
  mode_ne_zero := by intro i; norm_num
  is_eigen := by intro i; simp

/-! ## Operator-spectral consequences (bean `qou-qspc`) -/

/-- Each fundamental mode lies in the kernel of the shifted action `v ↦ R.op v - R.spec i • v`. -/
theorem sub_spec_smul_mode_eq_zero {H : Type*} [AddCommGroup H] [Module ℂ H]
    (R : ReebSpectrum H) (i : Fin 8) :
    R.op (R.mode i) - R.spec i • R.mode i = 0 :=
  sub_eq_zero.mpr (R.is_eigen i)

/-- Iterated action of `R.op` on the `i`-th fundamental mode scales by `(R.spec i) ^ n`. -/
theorem op_iterate_mode {H : Type*} [AddCommGroup H] [Module ℂ H]
    (R : ReebSpectrum H) (n : ℕ) (i : Fin 8) :
    (R.op ^[n]) (R.mode i) = (R.spec i) ^ n • R.mode i := by
  induction n with
  | zero =>
      simp
  | succ k ih =>
      rw [Function.iterate_succ_apply', ih, LinearMap.map_smul, R.is_eigen i,
        ← mul_smul, pow_succ, mul_comm]

/-- Under `[HasReebSpectralCoords Z R]`, the product of any pair of spectral coordinates
factors as the product of the corresponding complex `q`-powers of `R.spec`. -/
theorem eigenvalues_mul_of_hasReebSpectralCoords (Z : LocalQZetaFunction)
    {H : Type*} [AddCommGroup H] [Module ℂ H] (R : ReebSpectrum H)
    [h : HasReebSpectralCoords Z R] (i j : Fin 8) :
    Z.eigenvalues i * Z.eigenvalues j =
      ((Z.q : ℂ) ^ (R.spec i)) * ((Z.q : ℂ) ^ (R.spec j)) := by
  have hi := h.coords i
  have hj := h.coords j
  rw [hi, hj]

end QOU.AlgebraicSubstrate
