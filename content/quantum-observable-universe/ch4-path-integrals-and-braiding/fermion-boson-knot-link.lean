-- Ref: [manuscript] Ch. 6, §3
-- Fermions are knots (1 component, odd n in T(2,n)).
-- Bosons are links (2 components, even n in T(2,n)).
-- The vertical projection π_V detects the Reeb winding number.

-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
sorry

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
  sorry

/-- T(2,n) is a boson iff n is even (2 components). -/
theorem boson_iff_even (n : ℕ) (hn : n ≥ 2) :
    (TorusKnotLink.mk n).components = 2 ↔ n % 2 = 0 := by
  sorry

end
