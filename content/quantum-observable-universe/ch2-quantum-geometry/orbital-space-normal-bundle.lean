-- Ref: [manuscript] Ch. 6, §3
-- The orbital space at shell n is the space of framing-k sections
-- of the normal bundle of the trefoil in the Bring surface.
-- dim O_n = n² follows from SO(3) representation decomposition.

-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
sorry

noncomputable section

/-- The space of orbital states at shell n.
    Sections of the normal bundle N_{T_{2,3}/Σ₄} with total
    twist k = 2(n-1) and Laplacian eigenvalue ≤ λ_{n-1}. -/
def OrbitalSpace (n : ℕ) : Type := sorry

/-- Dimension of the orbital space at shell n is n². -/
theorem orbital_space_dim (n : ℕ) (hn : n ≥ 1) :
    sorry -- dim(OrbitalSpace n) = n^2
    := by sorry

/-- The orbital space decomposes under SO(3) into irreducibles
    V_0 ⊕ V_1 ⊕ ... ⊕ V_{n-1}, where dim V_ℓ = 2ℓ+1. -/
theorem orbital_space_decomposition (n : ℕ) (hn : n ≥ 1) :
    sorry -- OrbitalSpace n ≅ ⊕_{ℓ=0}^{n-1} V_ℓ
    := by sorry

/-- Each irreducible V_ℓ has dimension 2ℓ+1. -/
theorem irreducible_dim (ℓ : ℕ) :
    sorry -- dim(V_ℓ) = 2*ℓ + 1
    := by sorry

/-- The sum of dimensions equals n². -/
theorem sum_odd_eq_square (n : ℕ) :
    (Finset.range n).sum (fun ℓ => 2 * ℓ + 1) = n ^ 2 := by
  induction n with
  | zero => simp
  | succ k ih =>
    rw [Finset.sum_range_succ]
    ring_nf
    omega

/-- The cutoff: mode ℓ fits in shell n iff ℓ ≤ n-1.
    This follows from ℓ(ℓ+1) ≤ n(n-1). -/
theorem mode_cutoff (n ℓ : ℕ) (hn : n ≥ 1) :
    ℓ * (ℓ + 1) ≤ n * (n - 1) ↔ ℓ ≤ n - 1 := by
  sorry

end
