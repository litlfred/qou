import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Ring.Hom.Defs
import Mathlib.Tactic.Ring

/-!
# The Faddeev inversion relation narrows the elliptic freedom (input 3, partial)

`QOU.QBeta.FaddeevPhiEllipticFreedom.faddeevPhi_mul_elliptic` proves that the two
**first-order** shift equations of the `FaddeevPhi` class cannot pin `Φ_b`'s divisor:
for any lattice-elliptic `e` (`e(w+ib)=e(w)`, `e(w+i/b)=e(w)`), `e · Φ` is again a
solution, so a nonconstant `℘` produces a solution with a different divisor. That
obstruction is stated relative to the shift equations **alone**.

The physical `Φ_b` satisfies a *second* functional equation the shift class does not
record — the **Faddeev inversion relation** `Φ(x)·Φ(−x) = c`
(`QOU.QBeta.FaddeevModularDouble.inversion`). This file proves inversion **excludes the
even part of the elliptic freedom**, algebraically and over any integral domain
(pure ring identity — §7c generic, no archimedean content):

* `elliptic_factor_reciprocal_of_inversion` — if `Φ` and `e · Φ` both satisfy inversion
  with the same nonzero constant `c`, then `e(x)·e(−x) = 1` for every `x`: the surviving
  factors are **reciprocal-odd**, not the full elliptic group.
* `even_factor_sq_eq_one_of_inversion` — for an **even** factor (`e(−x)=e(x)`), reciprocity
  forces `e(x)² = 1`, hence (integral domain) `e(x) = 1 ∨ e(x) = −1` pointwise
  (`even_factor_eq_one_or_neg_one_of_inversion`). A nonconstant *elliptic* (in particular
  continuous) function is not `±1`-valued, so the **even** elliptic freedom — the generic
  `℘` factor — is excluded by inversion. The residual reciprocal-odd freedom is what the
  growth/boundedness route (`BoundedMeromorphicLiouville`) or the pentagon then removes.

This sharpens the elliptic-freedom obstruction into a concrete, corpus-grounded
strengthening: `FaddeevPhi` **+ inversion** already kills the even elliptic factor, using
an equation the corpus has (`FaddeevModularDouble`), not the analytic growth hypothesis.
The final `±1 ⇒ constant` step is the archimedean (identity-theorem) tail, noted but not
part of the algebraic core here.

Verified `lean`-direct against the pinned toolchain (exit 0). Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-07-25-faddeev-uniqueness-keystone-state.md
-/

namespace QOU.QBeta.InversionKillsEvenElliptic

variable {R : Type*} [CommRing R] [IsDomain R]

/-- **Inversion forces the surviving factor to be reciprocal-odd.** If `Φ` satisfies the
Faddeev inversion `Φ(x)·Φ(−x) = c` and the modified solution `e · Φ` satisfies the *same*
inversion, then `e(x)·e(−x) = 1` at every `x` (`c ≠ 0`). So the elliptic factors compatible
with inversion are exactly the reciprocal-odd ones — a proper subgroup of the full elliptic
group that the shift equations alone allow. -/
theorem elliptic_factor_reciprocal_of_inversion
    {Φ e : R → R} {c : R} (hc : c ≠ 0)
    (hΦ : ∀ x, Φ x * Φ (-x) = c)
    (heΦ : ∀ x, e x * Φ x * (e (-x) * Φ (-x)) = c) (x : R) :
    e x * e (-x) = 1 := by
  have hkey : e x * e (-x) * c = c := by
    calc e x * e (-x) * c
        = e x * e (-x) * (Φ x * Φ (-x)) := by rw [hΦ x]
      _ = e x * Φ x * (e (-x) * Φ (-x)) := by ring
      _ = c := heΦ x
  have hc1 : e x * e (-x) * c = 1 * c := by rw [hkey, one_mul]
  exact mul_right_cancel₀ hc hc1

/-- **An even inversion-compatible factor squares to one.** If additionally `e` is even
(`e(−x) = e(x)`), reciprocity `e(x)·e(−x) = 1` collapses to `e(x)² = 1`. -/
theorem even_factor_sq_eq_one_of_inversion
    {Φ e : R → R} {c : R} (hc : c ≠ 0)
    (hΦ : ∀ x, Φ x * Φ (-x) = c)
    (heΦ : ∀ x, e x * Φ x * (e (-x) * Φ (-x)) = c)
    (heven : ∀ x, e (-x) = e x) (x : R) :
    e x ^ 2 = 1 := by
  have h := elliptic_factor_reciprocal_of_inversion hc hΦ heΦ x
  rw [heven x] at h
  rw [sq]; exact h

/-- **Hence an even inversion-compatible factor is `±1`-valued** (integral domain). A
nonconstant elliptic (continuous) function is not `±1`-valued, so inversion excludes the
even elliptic freedom — the generic `℘` factor. -/
theorem even_factor_eq_one_or_neg_one_of_inversion
    {Φ e : R → R} {c : R} (hc : c ≠ 0)
    (hΦ : ∀ x, Φ x * Φ (-x) = c)
    (heΦ : ∀ x, e x * Φ x * (e (-x) * Φ (-x)) = c)
    (heven : ∀ x, e (-x) = e x) (x : R) :
    e x = 1 ∨ e x = -1 := by
  have h := even_factor_sq_eq_one_of_inversion hc hΦ heΦ heven x
  have h2 : (e x - 1) * (e x + 1) = 0 := by
    rw [show (e x - 1) * (e x + 1) = e x ^ 2 - 1 from by ring, h, sub_self]
  rcases mul_eq_zero.mp h2 with h3 | h3
  · exact Or.inl (sub_eq_zero.mp h3)
  · exact Or.inr (eq_neg_of_add_eq_zero_left h3)

/-! ## The σ-unitarity (self-duality) route to the reciprocal-odd residual

The `even_factor_*` results above kill the **even** elliptic freedom using inversion.
The residual is the **reciprocal-odd** elliptic factor (`e(x)·e(−x)=1`, `e` not even).
The physical `Φ_b` carries a second Frobenius-side datum the shift class omits:
**σ-unitarity** `σ(Φ)·Φ = 1` (the `|Φ_b| = 1` pure phase,
`QOU.QBeta.FaddeevModularDouble.IsSigmaUnitary`, `σ` = complex conjugation / the bar
involution). This section shows σ-unitarity forces the surviving factor to be
**σ-reflective** (`σ(e(x)) = e(−x)`), and that its **bar-even (σ-fixed)** part is then
`±1` — an algebraic exclusion, complementary to the analytic growth route. -/

section SigmaUnitary

variable (σ : R →+* R)

/-- **The connecting factor inherits σ-unitarity.** If both `Φ` and the modified
solution `e · Φ` are σ-unitary (`σ(Φ)Φ = 1`, `σ(eΦ)(eΦ) = 1`), then `e` is σ-unitary
(`σ(e x)·e x = 1`): the elliptic factor connecting two pure phases is itself a pure
phase. -/
theorem factor_sigmaUnitary_of_mul {Φ e : R → R}
    (hΦ : ∀ x, σ (Φ x) * Φ x = 1)
    (heΦ : ∀ x, σ (e x * Φ x) * (e x * Φ x) = 1) (x : R) :
    σ (e x) * e x = 1 := by
  have h := heΦ x
  rw [map_mul] at h
  have h2 : (σ (e x) * e x) * (σ (Φ x) * Φ x) = 1 := by rw [← h]; ring
  rwa [hΦ x, mul_one] at h2

/-- **σ-unitary + reciprocal-odd ⇒ σ-reflective.** A σ-unitary factor (`σ(e x)e x = 1`)
that is reciprocal-odd (`e x · e(−x) = 1`, the inversion residual) satisfies
`σ(e x) = e(−x)`: complex conjugation acts as argument reflection. -/
theorem sigma_eq_reflection_of_reciprocal {e : R → R}
    (hunit : ∀ x, σ (e x) * e x = 1)
    (hrecip : ∀ x, e x * e (-x) = 1) (x : R) :
    σ (e x) = e (-x) := by
  have hex : e x ≠ 0 := fun h => by
    have hr := hrecip x; rw [h, zero_mul] at hr; exact zero_ne_one hr
  have h1 : σ (e x) * e x = e (-x) * e x := by
    rw [hunit x, mul_comm (e (-x)) (e x), hrecip x]
  exact mul_right_cancel₀ hex h1

/-- **The bar-even reciprocal-odd σ-unitary factor squares to one.** If the σ-reflective
factor is additionally σ-fixed (bar-even, `σ(e x) = e x`), then `e(−x) = e x` (even), so
with reciprocity `e x ^ 2 = 1`. Thus inversion + σ-unitarity exclude the **bar-even** part
of the reciprocal-odd residual algebraically; the remaining non-σ-fixed part is what the
growth/boundedness route (`BoundedMeromorphicLiouville`) removes. -/
theorem bar_even_reciprocal_sq_eq_one {e : R → R}
    (hunit : ∀ x, σ (e x) * e x = 1)
    (hrecip : ∀ x, e x * e (-x) = 1)
    (hfix : ∀ x, σ (e x) = e x) (x : R) :
    e x ^ 2 = 1 := by
  have hrefl : σ (e x) = e (-x) := sigma_eq_reflection_of_reciprocal σ hunit hrecip x
  have heven : e (-x) = e x := by rw [← hrefl, hfix x]
  have hr := hrecip x
  rw [heven, ← sq] at hr
  exact hr

end SigmaUnitary

end QOU.QBeta.InversionKillsEvenElliptic
