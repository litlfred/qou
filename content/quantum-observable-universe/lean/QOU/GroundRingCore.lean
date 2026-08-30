import Mathlib.Algebra.Polynomial.Laurent

/-!
# QOU.GroundRingCore — the one ground ring, and nothing else

`R_q = ℤ[q, q⁻¹]` and its indeterminate, in a module light enough that any
other module can import it.

## Why this module exists (bean `qou-kfcl`)

Seven library modules declared their own `R_q`, in five namespaces, because
each wanted the ground ring without taking a dependency. Two of those are
outright FQN collisions, and **collisions make modules mutually
un-importable** — Lean's environment is flat, so

```
    import QOU.BraidKnot.CasimirShared
    import QOU.CategoricalDqSquared
```

(indented on purpose — `scripts/lean_cone_build.py` reads `^import` anywhere in
the file, so an example written flush-left becomes a phantom dependency)

fails with `environment already contains 'QOU.q_param'`. The worse of the two
was `QOU.R_q` itself, which denoted `RatFunc ℚ` in one module and
`LaurentPolynomial ℤ` in the other: **the same name for two different rings.**

`QOU.Archimedean.GroundRing` was the natural home and could not serve, because
it pulls `Mathlib.Tactic` and `QOU.MathlibExt.QIntegerCanonical`. Pointing a
module with three Mathlib imports at that, to fix a three-line duplication, is
a build-cost regression rather than a cleanup — so the ring moved down here
instead, and `GroundRing` keeps its tactic-heavy material on top.

**One import, three declarations, one theorem. Keep it that way.** The value of
this module is entirely in being cheap enough that nobody has a reason to
re-declare the ring locally again. Anything needing tactics, order, or the
archimedean specialisation belongs in `QOU.Archimedean.GroundRing` or further
out.

## Not the archimedean side

`R_q` is the *algebraic* ground ring: an un-ordered commutative ring with no
canonical topology. The archimedean specialisation `ι : R_q → ℝ, q ↦ q₀` lives
on the far side of the §7c wall and is deliberately absent here.
-/

namespace QOU.GroundRing

/-- The ground ring for QOU formal proofs: `R_q := ℤ[q, q⁻¹]`, the Laurent
    polynomials over `ℤ`, with `q` as the indeterminate. -/
abbrev R_q := LaurentPolynomial ℤ

/-- The indeterminate `q` of `R_q`. -/
noncomputable def q_param : R_q := LaurentPolynomial.T 1

/-- The formal inverse `q⁻¹` of the indeterminate.

    Carried as its own declaration rather than written `q_param⁻¹`: `R_q` is a
    ring, not a field, so it has no `Inv` instance and `q⁻¹` cannot be written
    even though `q` is invertible in it. `q_param_mul_inv` below is the
    defining relation. -/
noncomputable def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- `q · q⁻¹ = 1`. The relation that makes `q_inv_param` an inverse rather
    than an unrelated element — without it, the pair says nothing. -/
theorem q_param_mul_inv : q_param * q_inv_param = 1 := by
  unfold q_param q_inv_param
  rw [← LaurentPolynomial.T_add]
  norm_num

end QOU.GroundRing
