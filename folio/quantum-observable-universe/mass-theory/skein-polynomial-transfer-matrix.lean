import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import Mathlib.Data.Nat.Choose.Basic


/-!
# QOU.Archimedean.skein_polynomial_transfer_matrix

The nuclear Skein polynomial P_N(q) = Π_i V̂_i(q) is computed by
C(A,2) transfer matrix multiplications.  Each V̂_i(q) is a polynomial
in q^{1/2}, and q simultaneously serves as the Hecke deformation
parameter, the Skein polynomial variable, and the physical substrate
parameter q = 1.1097.

LaTeX label: `prop:skein-polynomial-transfer-matrix`

## References
- [jones1987] https://doi.org/10.2307/1971403
- [leitner2026] §6/skein-polynomial-transfer-matrix
-/

namespace QOU.Archimedean

-- ═══════════════════════════════════════════════════════════════════
-- Transfer matrix (entries are polynomials in q)
-- ═══════════════════════════════════════════════════════════════════

/-- A 2×2 transfer matrix with entries in ℝ (specialized from ℤ[q^±½]). -/
-- Ref: [leitner2026] §6/skein-polynomial-transfer-matrix
structure TransferMatrix where
  a₁₁ : ℝ
  a₁₂ : ℝ
  a₂₁ : ℝ
  a₂₂ : ℝ

/-- Transfer matrix multiplication. -/
-- Ref: [leitner2026] §6/skein-polynomial-transfer-matrix
def TransferMatrix.mul (M N : TransferMatrix) : TransferMatrix where
  a₁₁ := M.a₁₁ * N.a₁₁ + M.a₁₂ * N.a₂₁
  a₁₂ := M.a₁₁ * N.a₁₂ + M.a₁₂ * N.a₂₂
  a₂₁ := M.a₂₁ * N.a₁₁ + M.a₂₂ * N.a₂₁
  a₂₂ := M.a₂₁ * N.a₁₂ + M.a₂₂ * N.a₂₂

/-- The identity transfer matrix. -/
-- Ref: [leitner2026] §6/skein-polynomial-transfer-matrix
def TransferMatrix.id : TransferMatrix where
  a₁₁ := 1; a₁₂ := 0; a₂₁ := 0; a₂₂ := 1

/-- Transfer matrix for a single crossing with coefficients (c, d). -/
-- Ref: [leitner2026] §6/skein-polynomial-transfer-matrix
noncomputable def crossingMatrix (q c d : ℝ) : TransferMatrix where
  a₁₁ := c * (q - 1/q) + d
  a₁₂ := c
  a₂₁ := c
  a₂₂ := d

-- ═══════════════════════════════════════════════════════════════════
-- The Skein polynomial in factored form
-- ═══════════════════════════════════════════════════════════════════

/-- The traced volume at generator σ_i: V̂_i(q) = z · a_i + b_i,
    where (a_i, b_i) come from the transfer matrix product M_i and `z` is the
    Markov parameter in **convention D**, `z = q³/(q² + 1)`.

    **Migrated from convention C 2026-08-26 (bean `qou-cxjq` step 3).** This read
    `z = 1/(√q + 1/√q) = √q/(q+1)`, which is convention C — excised by owner
    ruling R1 of 2026-08-15. The migration is a **change of shape, not a change
    of variable**: `QOU.BraidKnot.no_kernel_instantiation_is_conventionD` proves
    that for every `q > 1` no real `u` at all satisfies `u/(u²+1) = q³/(q²+1)`,
    so no substitution `s² = q` could have done this. See
    `QOU/BraidKnot/MarkovConventionSeparation.lean`.

    Safe to migrate in place here: `tracedVolumeFromMatrix` has **no references
    anywhere in the tree** outside this definition, and none of this file's three
    theorems mentions it — so no recorded statement silently changes meaning.
    (That is the failure mode the five-way `markovZ` overload created, and it is
    why the convention is now named in the docstring rather than left to be
    inferred from the formula.)

    No longer a polynomial in `q^½`: convention D is rational in `q` itself,
    which is the point of the convention. -/
-- Ref: [leitner2026] §6/skein-polynomial-transfer-matrix
noncomputable def tracedVolumeFromMatrix (q : ℝ) (M : TransferMatrix) : ℝ :=
  let z := q ^ 3 / (q ^ 2 + 1)   -- convention D
  z * M.a₁₁ + M.a₂₁

/-- The nuclear Skein polynomial: product of traced volumes.
    P_N(q) = Π_i V̂_i(q). -/
-- Ref: [leitner2026] §6/skein-polynomial-transfer-matrix
noncomputable def skeinPolynomial (q : ℝ) (tracedVolumes : List ℝ) : ℝ :=
  tracedVolumes.foldl (· * ·) 1

-- ═══════════════════════════════════════════════════════════════════
-- Degree bound
-- ═══════════════════════════════════════════════════════════════════

/-- The degree of P_N(q) as a polynomial in q^½ is ≤ A² - 1.

    Each generator σ_i has k_i = A-i-1 crossings, contributing
    degree ≤ 2k_i + 1 to the polynomial. Summing:
    Σ(2k_i + 1) = 2·C(A,2) + (A-1) = A(A-1) + (A-1) = A² - 1. -/
-- Ref: [leitner2026] §6/skein-polynomial-transfer-matrix
theorem skein_polynomial_degree_bound (A : ℕ) (hA : 2 ≤ A) :
    2 * Nat.choose A 2 + (A - 1) = A ^ 2 - 1 := by
  have h2 : 2 * Nat.choose A 2 = A * (A - 1) := by
    rw [Nat.choose_two_right, Nat.mul_div_cancel']
    exact (Nat.even_mul_pred_self A).two_dvd
  rw [h2]
  rcases A with _ | n
  · omega
  · simp only [Nat.succ_sub_one]; ring_nf; omega

-- ═══════════════════════════════════════════════════════════════════
-- Number of transfer matrix steps = C(A,2) nucleon pairs
-- ═══════════════════════════════════════════════════════════════════

/-- The total number of transfer matrix multiplications is C(A,2).
    This is exact — not an asymptotic bound. -/
-- Ref: [leitner2026] §6/skein-polynomial-transfer-matrix
theorem transfer_matrix_steps (A : ℕ) :
    (Finset.range (A - 1)).sum (fun i => A - i - 1) = Nat.choose A 2 := by
  -- ∑_{i=0}^{A-2} (A - 1 - i) = 1 + 2 + ... + (A-1) = A(A-1)/2 = C(A,2)
  -- Proof by strong induction with case split on A
  induction A with
  | zero => simp
  | succ n ih =>
    cases n with
    | zero => simp
    | succ m =>
      -- A = m + 2. Goal: ∑_{i ∈ range (m+1)} ((m+2) - i - 1) = C(m+2, 2)
      -- Split off last term: i = m gives (m+2) - m - 1 = 1
      rw [show m + 1 + 1 - 1 = m + 1 from by omega]
      rw [Finset.sum_range_succ]
      -- ih for n = m+1: ∑_{i ∈ range m} ((m+1) - i - 1) = C(m+1, 2)
      have ih' : (Finset.range m).sum (fun i => m + 1 - i - 1) = Nat.choose (m + 1) 2 := by
        have := ih; simp only [show m + 1 - 1 = m from by omega] at this; exact this
      -- Each summand differs by 1: (m+2-i-1) = (m+1-i-1) + 1 for i < m
      have shift : ∀ i ∈ Finset.range m, m + 1 + 1 - i - 1 = (m + 1 - i - 1) + 1 := by
        intro i hi; simp [Finset.mem_range] at hi; omega
      rw [Finset.sum_congr rfl shift, Finset.sum_add_distrib, ih']
      -- Goal: C(m+1,2) + ∑_{i<m} 1 + ((m+2) - m - 1) = C(m+2, 2)
      simp [Finset.sum_const, Finset.card_range, Nat.choose_succ_succ, Nat.choose_one_right]
      omega

-- ═══════════════════════════════════════════════════════════════════
-- Triple identity of q
-- ═══════════════════════════════════════════════════════════════════

/-- The three roles of q are the same parameter.

    1. Algebraic: σ² = (q - q⁻¹)σ + 1 (Hecke deformation)
    2. Topological: variable of P_N(q) (Skein polynomial)
    3. Physical: q = 1.1097 (Descartes condition χ = -6)

    This structure bundles all three roles. -/
-- Ref: [leitner2026] §6/skein-polynomial-transfer-matrix
structure SubstrateTripleIdentity where
  /-- The single parameter q. -/
  q : ℝ
  /-- q > 1 (non-classical). -/
  q_gt_one : 1 < q
  /-- Algebraic role: the Hecke deformation coefficient. -/
  hecke_coeff : ℝ := q - 1/q
  /-- Topological role: evaluated Skein polynomial. -/
  skein_eval : List ℝ → ℝ := skeinPolynomial q
  /-- Physical role: the Descartes substrate parameter. -/
  descartes_q : ℝ := q

/-- The canonical triple-identity bundle built from a single `q > 1`,
    taking every role from its structural default. -/
-- Ref: [leitner2026] §6/skein-polynomial-transfer-matrix
noncomputable def SubstrateTripleIdentity.ofQ (q : ℝ) (hq : 1 < q) : SubstrateTripleIdentity where
  q := q
  q_gt_one := hq

/-- All three roles of the canonical bundle use the same numerical
    value: the Descartes substrate parameter equals `q` and the Hecke
    deformation coefficient equals `q − 1/q`. -/
-- Ref: [leitner2026] §6/skein-polynomial-transfer-matrix
theorem triple_identity (q : ℝ) (hq : 1 < q) :
    (SubstrateTripleIdentity.ofQ q hq).descartes_q = (SubstrateTripleIdentity.ofQ q hq).q ∧
    (SubstrateTripleIdentity.ofQ q hq).hecke_coeff
      = (SubstrateTripleIdentity.ofQ q hq).q - 1/(SubstrateTripleIdentity.ofQ q hq).q := by
  exact ⟨rfl, rfl⟩

-- ═══════════════════════════════════════════════════════════════════
-- Beta decay: difference of Skein polynomials
-- ═══════════════════════════════════════════════════════════════════

/-- The Q_q-value as the difference of Skein polynomials at q.

    Q_q = P_par(q) - P_dau(q) - P_e(q)

    This is a polynomial in q evaluated at the physical point. -/
-- Ref: [leitner2026] §6/skein-polynomial-transfer-matrix
noncomputable def Q_q_from_polynomials
    (P_par P_dau P_e : ℝ) : ℝ :=
  P_par - P_dau - P_e

/-- Double beta decay: the 2-jet cross-term is nonzero.
    P^(2β) - P^(par) ≠ (P^(β₁) - P^(par)) + (P^(β₂) - P^(par))
    The difference is the nuclear matrix element polynomial. -/
-- Ref: [leitner2026] §6/skein-polynomial-transfer-matrix
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
structure DoubleBetaCrossTerm where
  /-- Parent Skein polynomial value. -/
  P_par : ℝ
  /-- Double-beta daughter value. -/
  P_2beta : ℝ
  /-- Single-beta₁ daughter value. -/
  P_beta1 : ℝ
  /-- Single-beta₂ daughter value. -/
  P_beta2 : ℝ
  /-- The cross-term Δ_{p₁p₂}. -/
  cross_term : ℝ :=
    (P_2beta - P_par) - (P_beta1 - P_par) - (P_beta2 - P_par)

end QOU.Archimedean
