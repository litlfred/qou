/-!
# Wigner-2 coefficient from self-conjugate trace pairing

For any self-conjugate partition λ = λ', the per-generator trace
in the Hoefsmit seminormal representation equals h/2:

  tr(σ_g) / dim(λ) = (q - q⁻¹) / 2

The proof has two parts:
1. Paired sum identity: a_ρ + a_{-ρ} = h  (algebraic, `field_simp; ring`)
2. Involution doubling: Σf = Σ(f∘σ) ⟹ 2·Σf = Σ(f+f∘σ) = d·h
-/

-- Ref: [hoefsmit1974] Representations of Hecke algebras
-- Ref: [jucys1974] Symmetric polynomials and the center

namespace QOU.BraidKnot

/-- Seminormal diagonal entry: a_ρ = h/(1 - q^{-2ρ}).
    Archimedean specialisation per AGENTS.md §7c — q : ℝ throughout
    this block (sibling .md narrative carries the §7c banner). -/
noncomputable def a_rho (q : ℝ) (h : ℝ) (ρ : ℤ) : ℝ :=
  h / (1 - q ^ (-2 * ρ))

/-- **Paired sum identity**: a_ρ + a_{-ρ} = h.

The algebraic core of the self-conjugate trace theorem. -/
theorem paired_sum_identity (q : ℝ) (hq_pos : 0 < q) (hq_ne_one : q ≠ 1)
    (ρ : ℤ) (hρ : ρ ≠ 0)
    (h1 : q ^ (-2 * ρ) ≠ 1) (h2 : q ^ (2 * ρ) ≠ 1) :
    a_rho q (q - q⁻¹) ρ + a_rho q (q - q⁻¹) (-ρ) = q - q⁻¹ := by
  unfold a_rho
  have hd1 : (1 : ℝ) - q ^ (-2 * ρ) ≠ 0 := sub_ne_zero.mpr (Ne.symm h1)
  have hd2 : (1 : ℝ) - q ^ (2 * ρ) ≠ 0 := sub_ne_zero.mpr (Ne.symm h2)
  rw [show (-2 : ℤ) * (-ρ) = 2 * ρ by ring]
  field_simp
  ring

/-- **Involution doubling**: if σ is an involution on a Finset and
    f(i) + f(σ(i)) = c for all i, then 2 · Σf = |S| · c.

    Proof: Σf∘σ = Σf (reindex by bijection), so 2Σf = Σ(f + f∘σ) = Σc. -/
theorem sum_involution_double {n : ℕ} (f : Fin n → ℝ) (c : ℝ)
    (σ : Fin n → Fin n)
    (hσ_invol : Function.Involutive σ)
    (h_pair : ∀ i, f i + f (σ i) = c) :
    2 * Finset.univ.sum f = n * c := by
  have hσ_bij : Function.Bijective σ := hσ_invol.bijective
  -- Σ (f ∘ σ) = Σ f by reindexing
  have h_reindex : Finset.univ.sum (f ∘ σ) = Finset.univ.sum f := by
    exact Finset.sum_equiv (Equiv.ofBijective σ hσ_bij)
      (fun _ _ => Finset.mem_univ _) (fun _ _ => rfl)
  -- 2·Σf = Σf + Σ(f∘σ) = Σ(f + f∘σ) = Σc = n·c
  calc 2 * Finset.univ.sum f
      = Finset.univ.sum f + Finset.univ.sum f := by ring
    _ = Finset.univ.sum f + Finset.univ.sum (f ∘ σ) := by rw [h_reindex]
    _ = Finset.univ.sum (fun i => f i + f (σ i)) := by
        rw [← Finset.sum_add_distrib]; rfl
    _ = Finset.univ.sum (fun _ => c) := by
        congr 1; ext i; exact h_pair i
    _ = n * c := by simp [Finset.sum_const, Finset.card_fin]

/-- The self-conjugate trace theorem:
    if λ = λ' with dim d, then tr(σ_g)/d = h/2.

    Combines paired_sum_identity with sum_involution_double. -/
theorem self_conjugate_trace (n d : ℕ) (hd_pos : 0 < d)
    (q_val : ℝ) (hq_pos : 0 < q_val) (hq_ne_one : q_val ≠ 1)
    (axial : Fin d → ℤ)
    (σ : Fin d → Fin d) (hσ : Function.Involutive σ)
    (hσ_ax : ∀ i, axial (σ i) = -axial i)
    (hρ_ne : ∀ i, axial i ≠ 0)
    (hq_pow : ∀ i, q_val ^ (-2 * axial i) ≠ 1)
    (hq_pow' : ∀ i, q_val ^ (2 * axial i) ≠ 1) :
    let h := q_val - q_val⁻¹
    (Finset.univ.sum fun i => a_rho q_val h (axial i)) = (d : ℝ) / 2 * h := by
  intro hv
  -- Each pair sums to h by paired_sum_identity
  have h_pair : ∀ i, a_rho q_val hv (axial i) + a_rho q_val hv (axial (σ i)) = hv := by
    intro i
    rw [hσ_ax i]
    exact paired_sum_identity q_val hq_pos hq_ne_one (axial i) (hρ_ne i)
      (hq_pow i) (hq_pow' i)
  -- Apply involution doubling
  have h2 := sum_involution_double
    (fun i => a_rho q_val hv (axial i)) hv σ hσ h_pair
  linarith

end QOU.BraidKnot
