-- Ref: [manuscript] Ch. 6, §3
-- Fermions are knots (1 component, odd n in T(2,n)).
-- Bosons are links (2 components, even n in T(2,n)).
-- The vertical projection π_V detects the Reeb winding number.

noncomputable section

/-- A torus knot/link T(2,n) on the Bring surface. -/
structure TorusKnotLink (n : ℕ) where
  /-- Number of components = gcd(2, n) -/
  components : ℕ := Nat.gcd 2 n
  /-- Seifert genus -/
  genus : ℕ := (n - 1) / 2

/-- T(2,n) is a fermion iff n is odd (1 component). -/
theorem fermion_iff_odd (n : ℕ) (hn : n ≥ 2) :
    (TorusKnotLink.mk n).components = 1 ↔ n % 2 = 1 := by
  simp only [TorusKnotLink.mk]
  -- gcd(2, n) = 1 ↔ n is odd
  constructor
  · intro h
    -- gcd(2, n) = 1 means 2 ∤ n, so n % 2 = 1
    have h2 : ¬ (2 ∣ n) := by
      intro hdvd
      have := Nat.dvd_gcd (dvd_refl 2) hdvd
      omega
    omega
  · intro h
    -- n % 2 = 1 means n is odd, so gcd(2, n) = 1
    have h2 : ¬ (2 ∣ n) := by omega
    have hg := Nat.gcd_dvd_left 2 n
    have hg2 := Nat.gcd_dvd_right 2 n
    interval_cases (Nat.gcd 2 n) <;> omega

/-- T(2,n) is a boson iff n is even (2 components). -/
theorem boson_iff_even (n : ℕ) (hn : n ≥ 2) :
    (TorusKnotLink.mk n).components = 2 ↔ n % 2 = 0 := by
  -- Ref: [manuscript] Ch. 6, §3
  sorry

end
