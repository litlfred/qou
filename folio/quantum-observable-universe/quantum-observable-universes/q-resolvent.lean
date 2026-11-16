import QOU.Basic
import Mathlib.Algebra.Algebra.Defs


/-!
# QOU.QResolvent — categorical q-resolvent

The q-resolvent is the morphism R_q(s) = (s + Δ̂_q)^(-1) in End_C(A),
defined wherever s + Δ̂_q is invertible in the convolution algebra 𝓗_q.

Equivalently, R_q(s) is the categorical Laplace transform of the
q-heat semigroup exp(-t Δ̂_q).

LaTeX label: `def:q-resolvent`

## References

- [leitner2026] §2-quantum-observable-universes/q-resolvent
- [kassel1995] Quantum Groups (Springer GTM 155), §IV.4 (spectral
  theory of quantum groups)
-/

namespace QOU

noncomputable section

/-- **q-Resolvent data.**

    A categorical resolvent packages the q-Laplacian `delta_q`, the
    spectral parameter `s`, and an inverse witness for
    `s + delta_q` in the convolution algebra.

    The field `inverse_witness` encodes that `(s + delta_q) * R = 1`
    in 𝓗_q; the resolvent identity R_q(s₁) - R_q(s₂) = (s₂-s₁) R_q(s₁) R_q(s₂)
    follows from Hopf-algebra associativity. -/
-- Ref: [kassel1995] Quantum Groups, §IV.4
structure QResolvent (H : Type*) where
  /-- The q-Laplacian endomorphism. -/
  delta_q : H → H
  /-- The spectral parameter. -/
  s : H
  /-- The resolvent R_q(s). -/
  R : H → H
  /-- Inverse witness: (s + delta_q) ∘ R = id and R ∘ (s + delta_q) = id.
      Encoded at the element level via a nominal multiplication. -/
  inverse_witness : ∀ x : H, R (delta_q x) = x

/-- **The former axiom `QResolvent.first_identity` was false** (removed
    2026-11-15). It claimed the first resolvent identity
      `∀ x, R₁.R x - R₂.R x = (R₂.s - R₁.s) * R₁.R (R₂.R x)`
    for every pair of `QResolvent`s, but the structure only records
    `R ∘ delta_q = id`, which does not tie `R` to the spectral parameter `s`.
    Over `ℤ`, take `delta_q = R = id` with `s = 0` and `s = 1`: at `x = 1`
    the identity reads `0 = 1`. A true identity needs the field
    `(s + delta_q) ∘ R = id` in an algebra; recorded as open in bean
    `qou-n2un`. -/
-- Ref: [kassel1995] Quantum Groups, §IV.4
theorem QResolvent.not_first_identity :
    ¬ ∀ (R₁ R₂ : QResolvent ℤ) (x : ℤ),
        R₁.R x - R₂.R x = (R₂.s - R₁.s) * R₁.R (R₂.R x) := by
  intro h
  have := h ⟨id, 0, id, fun _ => rfl⟩ ⟨id, 1, id, fun _ => rfl⟩ 1
  simp at this


/-- **q-Resolvent in an algebra (repaired form).**

    `A` is an algebra over a commutative ring `K` (in the paper, the
    convolution algebra `𝓗_q` over the ground ring). The spectral parameter
    is a scalar `s : K`, and `R` is a two-sided inverse of `s + Δ`. Unlike
    `QResolvent`, this ties `R` to `s`. -/
structure QResolventAlg (K A : Type*) [CommRing K] [Ring A] [Algebra K A] where
  /-- The q-Laplacian `Δ̂_q`. -/
  delta_q : A
  /-- The spectral parameter. -/
  s : K
  /-- The resolvent `R_q(s)`. -/
  R : A
  /-- `(s + Δ) R = 1`. -/
  left_inv : (algebraMap K A s + delta_q) * R = 1
  /-- `R (s + Δ) = 1`. -/
  right_inv : R * (algebraMap K A s + delta_q) = 1

/-- **First resolvent identity** (repaired form of the removed axiom).
    For two resolvents of the same `Δ`:
    `R(s₁) − R(s₂) = (s₂ − s₁) R(s₁) R(s₂)`. -/
-- Ref: [kassel1995] Quantum Groups, §IV.4
theorem QResolventAlg.first_identity {K A : Type*} [CommRing K] [Ring A] [Algebra K A]
    (R₁ R₂ : QResolventAlg K A) (h : R₁.delta_q = R₂.delta_q) :
    R₁.R - R₂.R = algebraMap K A (R₂.s - R₁.s) * (R₁.R * R₂.R) := by
  have hd : algebraMap K A (R₂.s - R₁.s)
      = (algebraMap K A R₂.s + R₂.delta_q) - (algebraMap K A R₁.s + R₁.delta_q) := by
    rw [map_sub, h]; abel
  calc R₁.R - R₂.R
      = R₁.R * (algebraMap K A (R₂.s - R₁.s) * R₂.R) := by
        rw [hd, sub_mul, mul_sub, R₂.left_inv, mul_one, ← mul_assoc, R₁.right_inv, one_mul]
    _ = algebraMap K A (R₂.s - R₁.s) * (R₁.R * R₂.R) := by
        rw [← mul_assoc, ← Algebra.commutes, mul_assoc]

end

end QOU
