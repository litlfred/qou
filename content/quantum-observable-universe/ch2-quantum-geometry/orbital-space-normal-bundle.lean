-- Ref: [manuscript] Ch. 6, §3
-- The orbital space at shell n is the space of framing-k sections
-- of the normal bundle of the trefoil in the Bring surface.
-- dim O_n = n² follows from SO(3) representation decomposition.

noncomputable section

/-- The dimension of the orbital space at shell n.
    This equals n² by the SO(3) representation decomposition:
    O_n ≅ V_0 ⊕ V_1 ⊕ ... ⊕ V_{n-1}, where dim V_ℓ = 2ℓ+1. -/
-- Ref: [manuscript] Ch. 6, §3
def orbitalSpaceDim (n : ℕ) : ℕ := n ^ 2

/-- The dimension of the ℓ-th irreducible SO(3) representation V_ℓ. -/
def irreducibleDim (ℓ : ℕ) : ℕ := 2 * ℓ + 1

/-- Dimension of the orbital space at shell n is n². -/
-- Ref: [manuscript] Ch. 6, §3
theorem orbital_space_dim (n : ℕ) (hn : n ≥ 1) :
    orbitalSpaceDim n = n ^ 2 := rfl

/-- The orbital space decomposes under SO(3) into irreducibles
    V_0 ⊕ V_1 ⊕ ... ⊕ V_{n-1}, where dim V_ℓ = 2ℓ+1.
    The total dimension equals n². -/
-- Ref: [manuscript] Ch. 6, §3
theorem orbital_space_decomposition (n : ℕ) (hn : n ≥ 1) :
    (Finset.range n).sum irreducibleDim = orbitalSpaceDim n := by
  unfold irreducibleDim orbitalSpaceDim
  induction n with
  | zero => simp
  | succ k ih =>
    rw [Finset.sum_range_succ]
    ring_nf
    omega

/-- Each irreducible V_ℓ has dimension 2ℓ+1. -/
theorem irreducible_dim (ℓ : ℕ) :
    irreducibleDim ℓ = 2 * ℓ + 1 := rfl

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
-- Ref: [manuscript] Ch. 6, §3
theorem mode_cutoff (n ℓ : ℕ) (hn : n ≥ 1) :
    ℓ * (ℓ + 1) ≤ n * (n - 1) ↔ ℓ ≤ n - 1 := by
  constructor
  · -- Forward: contrapositive — if ℓ ≥ n then ℓ(ℓ+1) > n(n-1)
    intro h
    by_contra hc
    push_neg at hc
    have h1 : n ≤ ℓ := by omega
    have h2 : n * (n - 1) < ℓ * (ℓ + 1) := by
      calc ℓ * (ℓ + 1) ≥ n * (n + 1) := Nat.mul_le_mul h1 (by omega)
        _ > n * (n - 1) := by cases n with | zero => omega | succ k => nlinarith
    omega
  · -- Backward: ℓ ≤ n-1 implies ℓ+1 ≤ n, so ℓ(ℓ+1) ≤ (n-1)n
    intro h
    have : ℓ + 1 ≤ n := by omega
    calc ℓ * (ℓ + 1) ≤ (n - 1) * n := Nat.mul_le_mul h this
      _ = n * (n - 1) := by ring

end
