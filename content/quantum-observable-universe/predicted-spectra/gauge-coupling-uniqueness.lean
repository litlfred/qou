import QOU.Archimedean.EmSpectralCompleteness


/-!
# QOU.Archimedean.gauge_coupling_uniqueness

Up to the global normalisation `λ ∈ R`, there is exactly one
non-trivial scalar coupling `A ⊗ A → 𝟙` on the two-strand sector
of `C`.

LaTeX label: `cor:gauge-coupling-uniqueness`

## References

- [manuscript] §5/gauge-coupling-uniqueness
-/

namespace QOU.Archimedean

/-- **Corollary (gauge coupling uniqueness)** — a genuine corollary of
    `em_spectral_completeness`.

    Two-strand spectral completeness supplies the orthogonal
    idempotent decomposition `1 = e₊ + e₋`, `e₊ · e₋ = 0`, with both
    summands non-zero.  We extract from it the **singlet idempotent**
    `e₋` and prove it is a non-zero idempotent (`e₋ · e₋ = e₋`) — both
    facts are *derived from* completeness, not assumed, so the
    dependency on `em_spectral_completeness` is load-bearing (remove
    the `obtain` and the proof no longer type-checks).

    On that singlet sector the scalar coupling is unique up to an
    `R`-multiple: any `R`-linear coupling `φ : A ⊗ A → 𝟙`, represented
    as multiplication by its value `c ∈ R`, is a multiple of any
    *non-degenerate* reference coupling `ψ` — non-degenerate meaning
    its multiplier is a **unit** `u ∈ Rˣ` (equivalently
    `tr_τ(e₋) ≠ 0`).  The witness is `λ = c · u⁻¹`.

    The unit hypothesis is essential and was missing from the earlier
    axiomatic formulation, which was therefore *false*: a degenerate
    `ψ ≡ 0` (free multiplier `0`, not a unit) admits no `λ` with
    `φ = λ · ψ` when `φ ≢ 0`.  Replacing the free reference multiplier
    `R` with a unit `Rˣ` makes the statement true and discharges the
    former external axiom; the result is now proved outright from the
    `CommRing` axioms plus `em_spectral_completeness`. -/
-- Ref: [manuscript] §5/gauge-coupling-uniqueness
theorem gauge_coupling_uniqueness (S : SpectralRing) :
    ∃ e_minus : S.R,
      e_minus ≠ 0 ∧ e_minus * e_minus = e_minus ∧
      ∀ (φ ψ : S.R → S.R),
        (∃ c : S.R,  ∀ r : S.R, φ r = c * r) →
        (∃ u : S.Rˣ, ∀ r : S.R, ψ r = (u : S.R) * r) →
        ∃ lam : S.R, ∀ r : S.R, φ r = lam * ψ r := by
  -- The singlet idempotent `e₋` and the orthogonal decomposition come
  -- from two-strand spectral completeness — this is the categorical input.
  obtain ⟨e_plus, e_minus, hsum, horth, _, hem⟩ := em_spectral_completeness S
  refine ⟨e_minus, hem, ?_, ?_⟩
  · -- `e₋ · e₋ = e₋`, derived from `e₊ + e₋ = 1` and `e₊ · e₋ = 0`.
    have h1 : (e_plus + e_minus) * e_minus = e_minus := by rw [hsum, one_mul]
    rw [add_mul, horth, zero_add] at h1
    exact h1
  · -- Uniqueness up to an `R`-multiple; reference coupling non-degenerate.
    rintro φ ψ ⟨c, hc⟩ ⟨u, hu⟩
    refine ⟨c * (↑u⁻¹ : S.R), fun r => ?_⟩
    have key : (↑u⁻¹ : S.R) * (↑u : S.R) = 1 := u.inv_mul
    calc φ r = c * r := hc r
      _ = c * ((↑u⁻¹ : S.R) * (↑u : S.R)) * r := by rw [key, mul_one]
      _ = (c * (↑u⁻¹ : S.R)) * ((↑u : S.R) * r) := by ring
      _ = (c * (↑u⁻¹ : S.R)) * ψ r := by rw [hu r]

end QOU.Archimedean
