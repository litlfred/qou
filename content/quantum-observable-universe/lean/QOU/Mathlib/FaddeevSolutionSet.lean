/-
  `hratio` is not a consequence of `FaddeevPhi` — the class has no regularity.

  WHAT THIS SETTLES. After `QOU.Mathlib.FaddeevRatioPeriodic` reduced `hibinv`
  (bean qou-rp5f) to `hratio` (bean qou-cons), `hratio` is the single remaining
  input to `PentagonRigidity.uniqueUpToScalar`:

      Differentiable ℂ (fun z => Ψ z / Φ z)   for two `FaddeevPhi b` solutions.

  It cannot be derived from `FaddeevPhi b Φ` and `FaddeevPhi b Ψ`. The class has
  exactly three fields — `hb`, `shift_b`, `shift_binv` — and **none of them asks
  for holomorphy, continuity, or even measurability.** So the solution set is
  closed under multiplication by ANY function periodic under both `ib` and `i/b`,
  however badly behaved:

      faddeevPhi_mul_periodic :
        FaddeevPhi b Φ → (∀ z, E (z + ib) = E z) → (∀ z, E (z + i/b) = E z)
          → FaddeevPhi b (fun z => Φ z * E z)

  and `latticeIndicator` below is such an `E`, taking only the values `0` and `1`.

  CONSEQUENCE FOR BEAN qou-cons. The bean's title — "prove entireness of Φ₁/Φ₂
  ratio (divisor cancellation: two FaddeevPhi solutions share zero/pole lattice)"
  — describes a fact about the *analytic* `Φ_b`, not about the class. It is not
  provable in the stated generality, and any attempt that only uses the three
  class fields is doomed. Two honest routes:

    (a) strengthen `FaddeevPhi` with a regularity field (meromorphy, say) and
        re-derive the divisor statement from the shift equations; or
    (b) keep the class as-is and carry `hratio` as a hypothesis about the
        specific pair, which is what `ratio_const_of_entire_ratio` already does.

  Either is fine. What is not fine is treating `hratio` as a lemma waiting to be
  proved from what is currently there.

  RELATION TO THE ELLIPTIC PICTURE. This is the well-behaved version of the same
  statement: the classical solution set is `Φ_b · {elliptic}`, and *elliptic*
  carries the regularity that makes the ratio meromorphic. Drop regularity from
  the class and "elliptic" degrades to "doubly periodic", which is far too big.
  `QOU.MathlibExt.DoublyPeriodicLiouville.const_of_doublyPeriodic` is exactly the
  statement that the gap between them is closed by DIFFERENTIABILITY — so the
  missing hypothesis is precisely the one this file shows the class lacks.

  -- Ref: [faddeev1995] Faddeev, Lett. Math. Phys. 34 (1995) 249.
-/
import QOU.MathlibExt.FaddeevQuantumDilogarithm

namespace QOU.Mathlib.FaddeevSolutionSet

open Complex QOU.MathlibExt.FaddeevQuantumDilogarithm

variable {b : ℂ} {Φ : ℂ → ℂ}

/-- **The solution set absorbs any doubly-periodic factor**, with no regularity
asked of it. Both shift equations carry a prefactor that does not see `E`, and
the two half-shifts `±ib/2` differ by exactly the period `ib`. -/
theorem faddeevPhi_mul_periodic (hΦ : FaddeevPhi b Φ) (E : ℂ → ℂ)
    (hE1 : ∀ z, E (z + I * b) = E z) (hE2 : ∀ z, E (z + I / b) = E z) :
    FaddeevPhi b (fun z => Φ z * E z) where
  hb := hΦ.hb
  shift_b := by
    intro z
    have hE : E (z + I * (b / 2)) = E (z - I * (b / 2)) := by
      have h := hE1 (z - I * (b / 2))
      have e : z - I * (b / 2) + I * b = z + I * (b / 2) := by ring
      rwa [e] at h
    rw [hΦ.shift_b z, hE]
    ring
  shift_binv := by
    intro z hz
    have hE : E (z + I / (2 * b)) = E (z - I / (2 * b)) := by
      have h := hE2 (z - I / (2 * b))
      have e : z - I / (2 * b) + I / b = z + I / (2 * b) := by ring
      rwa [e] at h
    rw [hΦ.shift_binv z hz, hE]
    ring

open scoped Classical in
/-- The indicator of the period lattice `ℤ·ib + ℤ·(i/b)`: doubly periodic by
construction, and visibly not continuous anywhere near the lattice. -/
noncomputable def latticeIndicator (b : ℂ) (z : ℂ) : ℂ :=
  if ∃ m n : ℤ, z = (m : ℂ) * (I * b) + (n : ℂ) * (I / b) then 1 else 0

open scoped Classical in
theorem latticeIndicator_periodic_b (b z : ℂ) :
    latticeIndicator b (z + I * b) = latticeIndicator b z := by
  unfold latticeIndicator
  congr 1
  apply propext
  constructor
  · rintro ⟨m, n, hmn⟩
    exact ⟨m - 1, n, by push_cast; linear_combination hmn⟩
  · rintro ⟨m, n, hmn⟩
    exact ⟨m + 1, n, by push_cast; linear_combination hmn⟩

open scoped Classical in
theorem latticeIndicator_periodic_binv (b z : ℂ) :
    latticeIndicator b (z + I / b) = latticeIndicator b z := by
  unfold latticeIndicator
  congr 1
  apply propext
  constructor
  · rintro ⟨m, n, hmn⟩
    exact ⟨m, n - 1, by push_cast; linear_combination hmn⟩
  · rintro ⟨m, n, hmn⟩
    exact ⟨m, n + 1, by push_cast; linear_combination hmn⟩

open scoped Classical in
/-- It is `1` on the lattice — in particular at `0`, so it is not the zero
function, and together with any off-lattice point it is non-constant. -/
theorem latticeIndicator_zero (b : ℂ) : latticeIndicator b 0 = 1 := by
  unfold latticeIndicator
  rw [if_pos]
  exact ⟨0, 0, by simp⟩

open scoped Classical in
/-- **The witness.** Multiplying any `FaddeevPhi b` solution by the lattice
indicator gives another `FaddeevPhi b` solution. Since the indicator takes only
the values `0` and `1`, the two solutions do NOT have a differentiable ratio
wherever the indicator is discontinuous — so `hratio` (bean qou-cons) is not
derivable from the class. -/
theorem faddeevPhi_mul_latticeIndicator (hΦ : FaddeevPhi b Φ) :
    FaddeevPhi b (fun z => Φ z * latticeIndicator b z) :=
  faddeevPhi_mul_periodic hΦ _ (latticeIndicator_periodic_b b)
    (latticeIndicator_periodic_binv b)

end QOU.Mathlib.FaddeevSolutionSet
