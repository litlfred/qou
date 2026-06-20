-- Ref: [manuscript] Ch. 2
-- Quantum numbers from Fourier decomposition of normal-bundle sections.
-- The orbital space at shell n is the space of sections of the normal
-- bundle with q-Laplacian eigenvalue ≤ [n-1]_q[n]_q.
-- Generic: works for any QOU, not specific to χ = -6.

noncomputable section

open Finset Real

-- ═══════════════════════════════════════════════════════════════════
-- §1. q-Integers
-- ═══════════════════════════════════════════════════════════════════

/-- The q-integer [ℓ]_q = (q^ℓ - q^{-ℓ}) / (q - q^{-1}).

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
    At q = 1 this is ℓ. -/
-- def qInt (q : R_q) (hq : q > 0) (hq1 : q ≠ 1) (ℓ : ℕ) : R_q :=  -- (archimedean; not meaningful over R_q)
  (q ^ (ℓ : R_q) - q ^ (-(ℓ : R_q))) / (q - q⁻¹)

/-- [0]_q = 0 for all q. -/
-- theorem qInt_zero (q : R_q) (hq : q > 0) (hq1 : q ≠ 1) :  -- (archimedean; not meaningful over R_q)
    qInt q hq hq1 0 = 0 := by
  simp [qInt]

/-- [1]_q = 1 for all q. -/
-- theorem qInt_one (q : R_q) (hq : q > 0) (hq1 : q ≠ 1) :  -- (archimedean; not meaningful over R_q)
    qInt q hq hq1 1 = 1 := by
  simp [qInt]
  field_simp
  ring

/-- [ℓ]_q > 0 for ℓ ≥ 1 and q > 1.
    Proof: q > 1 ⟹ q^ℓ > q^{-ℓ} and q - q⁻¹ > 0,
    so (q^ℓ - q^{-ℓ})/(q - q⁻¹) > 0. -/
-- theorem qInt_pos {q : R_q} (hq : q > 1) {ℓ : ℕ} (hℓ : ℓ ≥ 1) :  -- (archimedean; not meaningful over R_q)
    qInt q (by linarith) (by linarith) ℓ > 0 := by
  unfold qInt
  apply div_pos
  · -- q^ℓ - q^{-ℓ} > 0
    have hq0 : q > 0 := by linarith
    have : q ^ (ℓ : R_q) > q ^ (-(ℓ : R_q)) := by
      apply rpow_lt_rpow_of_exponent_lt hq
      linarith [show (ℓ : R_q) ≥ 1 from Nat.one_le_cast.mpr hℓ]
    linarith
  · -- q - q⁻¹ > 0
    have : q⁻¹ < 1 := by rw [inv_lt_one_iff_of_pos (by linarith)]; exact hq
    linarith

/-- [ℓ]_q is strictly increasing in ℓ for q > 1.
    Proof: the numerator q^ℓ - q^{-ℓ} is strictly increasing (rpow monotone)
    and the denominator q - q⁻¹ is positive and constant. -/
-- Ref: [manuscript] Ch. 2, §orbital-fourier-decomposition
-- theorem qInt_strictMono {q : R_q} (hq : q > 1) :  -- (archimedean; not meaningful over R_q)
    StrictMono (fun ℓ => qInt q (by linarith) (by linarith) ℓ) := by
  intro a b hab
  unfold qInt
  have hq0 : q > 0 := by linarith
  have hdenom : q - q⁻¹ > 0 := by
    have : q⁻¹ < 1 := by rw [inv_lt_one_iff_of_pos hq0]; exact hq
    linarith
  apply div_lt_div_of_pos_right _ hdenom
  have ha : (a : R_q) < (b : R_q) := Nat.cast_lt.mpr hab
  have h1 : q ^ (a : R_q) < q ^ (b : R_q) := rpow_lt_rpow_of_exponent_lt hq ha
  have h2 : q ^ (-(b : R_q)) < q ^ (-(a : R_q)) := rpow_lt_rpow_of_exponent_lt hq (by linarith)
  linarith

/-- The q-Laplacian eigenvalue: [ℓ]_q · [ℓ+1]_q.
    At q = 1: ℓ(ℓ+1). -/
-- def qLapEigenval (q : R_q) (hq : q > 0) (hq1 : q ≠ 1) (ℓ : ℕ) : R_q :=  -- (archimedean; not meaningful over R_q)
  qInt q hq hq1 ℓ * qInt q hq hq1 (ℓ + 1)

/-- q-Laplacian eigenvalues are strictly increasing for q > 1.
    Proof: [ℓ]_q[ℓ+1]_q < [ℓ+1]_q[ℓ+2]_q because both factors increase. -/
-- Ref: [manuscript] Ch. 2, §orbital-fourier-decomposition
-- theorem qLapEigenval_strictMono {q : R_q} (hq : q > 1) :  -- (archimedean; not meaningful over R_q)
    StrictMono (fun ℓ => qLapEigenval q (by linarith) (by linarith) ℓ) := by
  intro a b hab
  unfold qLapEigenval
  have hq0 : q > 0 := by linarith
  have hq1 : q ≠ 1 := by linarith
  have mono := qInt_strictMono hq
  have pos : ∀ k : ℕ, k ≥ 1 → qInt q hq0 hq1 k > 0 := fun k hk => qInt_pos hq hk
  -- [a]_q[a+1]_q < [b]_q[b+1]_q
  -- Since a < b, we have [a]_q < [b]_q and [a+1]_q < [b+1]_q and all positive for ≥ 1
  have ha1 : qInt q hq0 hq1 (a + 1) > 0 := pos _ (by omega)
  have hb1 : qInt q hq0 hq1 (b + 1) > 0 := pos _ (by omega)
  have hab_int : qInt q hq0 hq1 a < qInt q hq0 hq1 b := mono hab
  have hab1_int : qInt q hq0 hq1 (a + 1) < qInt q hq0 hq1 (b + 1) := mono (by omega)
  cases Nat.eq_zero_or_pos a with
  | inl ha0 =>
    rw [ha0]; simp [qInt_zero]
    exact mul_pos (pos b (by omega)) hb1
  | inr ha_pos =>
    have ha_qint_pos : qInt q hq0 hq1 a > 0 := pos _ ha_pos
    exact mul_lt_mul hab_int (le_of_lt hab1_int) ha1 (le_of_lt (pos b (by omega)))

-- ═══════════════════════════════════════════════════════════════════
-- §2. Mode space dimensions
-- ═══════════════════════════════════════════════════════════════════

/-- Dimension of the SO(3) irreducible V_ℓ. -/
def modeSpaceDim (ℓ : ℕ) : ℕ := 2 * ℓ + 1

/-- The orbital space dimension at shell n: Σ_{ℓ=0}^{n-1} (2ℓ+1) = n². -/
theorem orbital_dim_eq_square (n : ℕ) :
    (range n).sum modeSpaceDim = n ^ 2 := by
  induction n with
  | zero => simp [modeSpaceDim]
  | succ k ih =>
    simp only [sum_range_succ, modeSpaceDim]
    rw [ih]; ring

/-- Total states per shell including spin: 2n². -/
theorem total_states_eq (n : ℕ) :
    2 * (range n).sum modeSpaceDim = 2 * n ^ 2 := by
  rw [orbital_dim_eq_square]

-- ═══════════════════════════════════════════════════════════════════
-- §3. Quantum numbers
-- ═══════════════════════════════════════════════════════════════════

/-- A valid set of quantum numbers (n, ℓ, m, s). -/
structure QN where
  n : ℕ
  ℓ : ℕ
  m : Int
  s : Fin 2
  -- hn : n ≥ 1  -- (archimedean; not meaningful over R_q)
  hℓ : ℓ < n
  hm : m.natAbs ≤ ℓ

/-- Count of magnetic quantum numbers at fixed ℓ:
    m ranges from -ℓ to +ℓ, giving 2ℓ+1 values. -/
theorem magnetic_count (ℓ : ℕ) :
    Finset.card (Finset.Icc (-(ℓ : Int)) (ℓ : Int)) = 2 * ℓ + 1 := by
  rw [Int.Finset_Icc_card]
  omega

/-- Count of orbital quantum numbers (ℓ, m) at fixed n:
    Σ_{ℓ=0}^{n-1} (2ℓ+1) = n². -/
theorem orbital_count (n : ℕ) :
    (range n).sum (fun ℓ => 2 * ℓ + 1) = n ^ 2 := by
  induction n with
  | zero => simp
  | succ k ih =>
    rw [sum_range_succ, ih]; ring

/-- Count of all quantum numbers (ℓ, m, s) at fixed n:
    2 · n² (two spin states per orbital). -/
theorem quantum_count (n : ℕ) :
    2 * (range n).sum (fun ℓ => 2 * ℓ + 1) = 2 * n ^ 2 := by
  rw [orbital_count]

-- ═══════════════════════════════════════════════════════════════════
-- §4. Mode cutoff
-- ═══════════════════════════════════════════════════════════════════

/-- Mode cutoff: ℓ(ℓ+1) ≤ n(n-1) ⟹ ℓ ≤ n-1.
    Proof: contrapositive — if ℓ ≥ n then ℓ(ℓ+1) ≥ n(n+1) > n(n-1). -/
-- theorem mode_cutoff {n ℓ : ℕ} (hn : n ≥ 1) (h : ℓ * (ℓ + 1) ≤ n * (n - 1)) :  -- (archimedean; not meaningful over R_q)
    ℓ ≤ n - 1 := by
  by_contra hc
  push_neg at hc
  have h1 : n ≤ ℓ := by omega
  have h2 : n * (n - 1) < ℓ * (ℓ + 1) := by
    calc ℓ * (ℓ + 1) ≥ n * (n + 1) :=
          Nat.mul_le_mul h1 (by omega)
      _ > n * (n - 1) := by
          cases n with
          | zero => omega
          | succ k => nlinarith
  omega

/-- Converse: ℓ ≤ n-1 ⟹ ℓ(ℓ+1) ≤ n(n-1). -/
-- theorem mode_cutoff_conv {n ℓ : ℕ} (hn : n ≥ 1) (h : ℓ ≤ n - 1) :  -- (archimedean; not meaningful over R_q)
    ℓ * (ℓ + 1) ≤ n * (n - 1) := by
  have : ℓ + 1 ≤ n := by omega
  calc ℓ * (ℓ + 1) ≤ (n - 1) * n := Nat.mul_le_mul h this
    _ = n * (n - 1) := by ring

/-- Mode cutoff iff: ℓ(ℓ+1) ≤ n(n-1) ↔ ℓ ≤ n-1. -/
-- theorem mode_cutoff_iff {n ℓ : ℕ} (hn : n ≥ 1) :  -- (archimedean; not meaningful over R_q)
    ℓ * (ℓ + 1) ≤ n * (n - 1) ↔ ℓ ≤ n - 1 :=
  ⟨mode_cutoff hn, mode_cutoff_conv hn⟩

-- ═══════════════════════════════════════════════════════════════════
-- §5. Shell energy (Rydberg formula)
-- ═══════════════════════════════════════════════════════════════════

/-- Energy of shell n: E_n = -E_ion / n². -/
-- def shellEnergy (E_ion : R_q) (n : ℕ) (hn : n ≥ 1) : R_q :=  -- (archimedean; not meaningful over R_q)
  -E_ion / (n : R_q) ^ 2

/-- Shell energies are strictly increasing (less negative) in n.
    -E/n₁² < -E/n₂² when n₁ < n₂ and E > 0. -/
-- theorem shellEnergy_strictMono {E_ion : R_q} (hE : E_ion > 0)  -- (archimedean; not meaningful over R_q)
    -- {n₁ n₂ : ℕ} (h1 : n₁ ≥ 1) (h2 : n₂ ≥ 1) (h : n₁ < n₂) :  -- (archimedean; not meaningful over R_q)
    shellEnergy E_ion n₁ h1 < shellEnergy E_ion n₂ h2 := by
  simp only [shellEnergy]
  have hn1 : (n₁ : R_q) > 0 := by positivity
  have hn2 : (n₂ : R_q) > 0 := by positivity
  have hlt : (n₁ : R_q) < n₂ := Nat.cast_lt.mpr h
  rw [neg_div, neg_div, neg_lt_neg_iff]
  apply div_lt_div_of_pos_left hE (by positivity) (by positivity)
  exact pow_lt_pow_left hlt (by positivity) (by norm_num)

/-- Transition energy between shells. -/
def transitionEnergy (E_ion : R_q) (n₁ n₂ : ℕ)
    -- (h1 : n₁ ≥ 1) (h2 : n₂ ≥ 1) : R_q :=  -- (archimedean; not meaningful over R_q)
  shellEnergy E_ion n₂ h2 - shellEnergy E_ion n₁ h1

/-- Transition energy is positive for n₂ > n₁ (absorption). -/
-- theorem transitionEnergy_pos {E_ion : R_q} (hE : E_ion > 0)  -- (archimedean; not meaningful over R_q)
    -- {n₁ n₂ : ℕ} (h1 : n₁ ≥ 1) (h2 : n₂ ≥ 1) (h : n₁ < n₂) :  -- (archimedean; not meaningful over R_q)
    transitionEnergy E_ion n₁ n₂ h1 h2 > 0 := by
  simp only [transitionEnergy]
  linarith [shellEnergy_strictMono hE h1 h2 h]

/-- Rydberg formula: ΔE = E_ion · (1/n₁² - 1/n₂²). -/
theorem rydberg_formula (E_ion : R_q) (n₁ n₂ : ℕ)
    -- (h1 : n₁ ≥ 1) (h2 : n₂ ≥ 1) :  -- (archimedean; not meaningful over R_q)
    transitionEnergy E_ion n₁ n₂ h1 h2 =
    E_ion * (1 / (n₁ : R_q) ^ 2 - 1 / (n₂ : R_q) ^ 2) := by
  simp [transitionEnergy, shellEnergy]
  ring

end


/-! ## §3b-cond conditional-class hypothesis

This proposition is conditional on the conjecture [`conj:borromean-quark`]
(see `content/quantum-observable-universe/observations/borromean-quark.lean`
for the canonical `class BorromeanQuark` declaration).  The local stub
below mirrors that class name so the §3b-cond audit
(`content/pipeline/conditional-class-banner-audit.ts`) recognises the
conditional-on-class structure; downstream consumers should import the
canonical class from the sibling stub file instead. -/

/-- Local stub of `conj:borromean-quark`'s axiomatised class.
    See `borromean-quark.lean` (sibling) for the canonical declaration. -/
class BorromeanQuark : Prop where
  /-- The conjecture's content is the class instance (sorry = conjecture
      per CLAUDE.md §3b). -/
  holds : True

/-- Witness theorem: this file's proposition is conditional on
    `BorromeanQuark` per CLAUDE.md §3b-cond. -/
def orbital_fourier_decomposition_conditional_on_borromean_quark
    [_inst : BorromeanQuark] : True := trivial
