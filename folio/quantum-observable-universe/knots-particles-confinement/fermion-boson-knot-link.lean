import Mathlib.Data.Nat.GCD.Basic

-- Ref: [leitner2026] Ch. 6, §3
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
    ({ } : TorusKnotLink n).components = 1 ↔ n % 2 = 1 := by
  show Nat.gcd 2 n = 1 ↔ n % 2 = 1
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
    have hg : Nat.gcd 2 n ∣ 2 := Nat.gcd_dvd_left 2 n
    have hg2 : Nat.gcd 2 n ∣ n := Nat.gcd_dvd_right 2 n
    -- gcd divides 2, so gcd ∈ {1, 2}; but gcd ∣ n and 2 ∤ n, so gcd = 1
    have : Nat.gcd 2 n = 1 ∨ Nat.gcd 2 n = 2 := by
      have hle : Nat.gcd 2 n ≤ 2 := Nat.le_of_dvd (by decide) hg
      have hpos : 0 < Nat.gcd 2 n := Nat.gcd_pos_of_pos_left n (by decide)
      omega
    rcases this with h1 | h1
    · exact h1
    · exfalso; exact h2 (h1 ▸ hg2)

/-- T(2,n) is a boson iff n is even (2 components). -/
theorem boson_iff_even (n : ℕ) (hn : n ≥ 2) :
    ({ } : TorusKnotLink n).components = 2 ↔ n % 2 = 0 := by
  show Nat.gcd 2 n = 2 ↔ n % 2 = 0
  constructor
  · intro h
    -- gcd(2, n) = 2 means 2 ∣ n
    have hg2 : Nat.gcd 2 n ∣ n := Nat.gcd_dvd_right 2 n
    rw [h] at hg2
    omega
  · intro h
    -- n % 2 = 0 means 2 ∣ n, so gcd(2, n) = 2
    have h2 : 2 ∣ n := by omega
    exact Nat.gcd_eq_left h2

end
