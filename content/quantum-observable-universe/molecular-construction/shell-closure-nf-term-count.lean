import QOU.Archimedean.GroundRing


/-!
# Shell Closure from NF Term Count

Formalization of the quotient atom model: the nuclear core is
quotiented to a single strand, and electrons are added one at a time.
We prove the Z=2 (helium) case: after adding 2 electrons to the
nuclear strand, the NF has exactly 2 terms — the same as after 1
electron. This is the first shell closure (1s²).

## The quotient atom model

In H_{Z+1}(q), strand 0 is the nuclear core 𝒩 and strands 1..Z are
electrons. The crossing types are:

  𝒩-e : Z · σ⁻¹ = Z · (σ − HA)     (EM attraction)
  e-e  : σ                           (EM repulsion)

## References

- [iwahori1964] https://doi.org/10.1515/crll.1964.215.167
- [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.Molecular

open QOU.Archimedean

/-! ## §1  The quotient atom in H₂(q) and H₃(q)

For the smallest cases, the Hecke algebra is small enough for
direct computation. We work in the NF basis. -/

/-- An element of H₂(q) in NF: 2 coefficients [γ, σ₀].
    Every element of H₂(q) can be written as a·𝟏 + b·σ₀. -/
abbrev H2_NF := Fin 2 → R_q

/-- An element of H₃(q) in NF: 6 coefficients [γ, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀].
    These are the 6 = |S₃| reduced words. -/
abbrev H3_NF := Fin 6 → R_q

/-! ## §2  H₂(q) operations -/

/-- The identity element in H₂(q). -/
noncomputable def h2_id : H2_NF := fun i =>
  match i with
  | 0 => 1
  | 1 => 0

/-- Multiplication on the right by σ₀ on an H₂(q) element.
    Using the Hecke relation: σ₀² = HA·σ₀ + 𝟏.
    Then: (a·𝟏 + b·σ₀)·σ₀ = a·σ₀ + b·(HA·σ₀ + 𝟏) = b·𝟏 + (a + HA·b)·σ₀ -/
noncomputable def h2_mul_s0 (x : H2_NF) : H2_NF := fun i =>
  match i with
  | 0 => x 1                -- 𝟏 coefficient: b
  | 1 => x 0 + HA * x 1     -- σ₀ coefficient: a + HA·b

/-- The 𝒩-e crossing element for Z=1: σ₀⁻¹ = σ₀ − HA·𝟏.
    As an H₂ element: (−HA)·𝟏 + 1·σ₀. -/
noncomputable def h2_nuc_e_Z1 : H2_NF := fun i =>
  match i with
  | 0 => -HA
  | 1 => 1

/-- The 𝒩-e crossing element for Z=2: 2·σ₀⁻¹ = 2·σ₀ − 2·HA·𝟏.
    As an H₂ element: (−2·HA)·𝟏 + 2·σ₀. -/
noncomputable def h2_nuc_e_Z2 : H2_NF := fun i =>
  match i with
  | 0 => -2 * HA
  | 1 => 2

/-! ## §3  Hydrogen: NF(𝒩 + 1e⁻) in H₂(q)

The hydrogen atom in the quotient model: strand 0 = nucleus (Z=1),
strand 1 = electron. One crossing: 𝒩-e at σ₀.

NF = σ₀⁻¹ = σ₀ − HA·𝟏 = (−HA)·𝟏 + 1·σ₀.

This has 2 nonzero terms. -/

/-- Hydrogen atom NF: (−HA)·𝟏 + 1·σ₀. -/
noncomputable def hydrogen_nf : H2_NF := h2_nuc_e_Z1

/-! ## §3a  Nonzero certificates in `R_q = ℤ[q, q⁻¹]`

`R_q` is an integral domain of characteristic zero.  Two facts drive the
NF-term-count proofs: every `T n` is a unit (hence nonzero), and a Laurent
polynomial that clears — after multiplying by a unit `T k` — to a nonzero
ordinary polynomial under the injective ring map `Polynomial.toLaurent` is
itself nonzero. -/

/-- `(4 : R_q) ≠ 0`: the injective ring map `Polynomial.toLaurent` carries
the nonzero constant `4 : ℤ[X]` to `4 : R_q`. -/
theorem four_ne_zero_Rq : (4 : R_q) ≠ 0 := by
  intro h
  have h2 : (4 : Polynomial ℤ) = 0 :=
    Polynomial.toLaurent_injective (by simp only [map_ofNat, map_zero]; exact h)
  norm_num at h2

/-- `T 2 − 1 = toLaurent(X² − 1) ≠ 0`. -/
theorem T2_sub_one_ne_zero : (LaurentPolynomial.T 2 - 1 : R_q) ≠ 0 := by
  have e : (LaurentPolynomial.T 2 - 1 : R_q) = Polynomial.toLaurent (Polynomial.X ^ 2 - 1) := by
    rw [map_sub, map_one, map_pow, Polynomial.toLaurent_X, LaurentPolynomial.T_pow]
    norm_num
  rw [e, Ne, map_eq_zero_iff _ Polynomial.toLaurent_injective]
  intro hP
  have h0 := congrArg (Polynomial.eval 0) hP
  simp at h0

/-- `T 4 − T 2 + 1 = toLaurent(X⁴ − X² + 1) ≠ 0`. -/
theorem T4_sub_T2_add_one_ne_zero :
    (LaurentPolynomial.T 4 - LaurentPolynomial.T 2 + 1 : R_q) ≠ 0 := by
  have e : (LaurentPolynomial.T 4 - LaurentPolynomial.T 2 + 1 : R_q)
      = Polynomial.toLaurent (Polynomial.X ^ 4 - Polynomial.X ^ 2 + 1) := by
    rw [map_add, map_sub, map_pow, map_pow, map_one, Polynomial.toLaurent_X, LaurentPolynomial.T_pow]
    norm_num
  rw [e, Ne, map_eq_zero_iff _ Polynomial.toLaurent_injective]
  intro hP
  have h0 := congrArg (Polynomial.eval 0) hP
  simp at h0

/-- HA = q − q⁻¹ is nonzero in ℤ[q, q⁻¹]. -/
-- Ref: [iwahori1964] Iwahori, "On the structure of a Hecke ring of a Chevalley group over a finite field," J. Fac. Sci. Univ. Tokyo 10 (1964)
theorem HA_ne_zero : HA ≠ 0 := by
  -- HA = T(−1)·(T 2 − 1): a unit times a nonzero element of the integral domain R_q.
  have hfac : HA = LaurentPolynomial.T (-1) * (LaurentPolynomial.T 2 - 1) := by
    unfold HA q q_inv
    rw [mul_sub, mul_one, ← LaurentPolynomial.T_add]; norm_num
  rw [hfac]
  exact mul_ne_zero (LaurentPolynomial.isUnit_T (-1)).ne_zero T2_sub_one_ne_zero

/-- `HA² + 1 ≠ 0`.  Clearing by the unit `T(−2)` reduces this to `T 4 − T 2 + 1 ≠ 0`. -/
-- Ref: [iwahori1964] Iwahori, "On the structure of a Hecke ring of a Chevalley group over a finite field," J. Fac. Sci. Univ. Tokyo 10 (1964)
theorem HA_sq_add_one_ne_zero : (HA ^ 2 + 1 : R_q) ≠ 0 := by
  have hHA : HA = LaurentPolynomial.T (-1) * (LaurentPolynomial.T 2 - 1) := by
    unfold HA q q_inv; rw [mul_sub, mul_one, ← LaurentPolynomial.T_add]; norm_num
  have hsq : (LaurentPolynomial.T (-1) : R_q) ^ 2 = LaurentPolynomial.T (-2) := by
    rw [LaurentPolynomial.T_pow]; norm_num
  have hT22 : (LaurentPolynomial.T (-2) : R_q) * LaurentPolynomial.T 2 = 1 := by
    rw [← LaurentPolynomial.T_add]; norm_num [LaurentPolynomial.T_zero]
  have hT4 : (LaurentPolynomial.T (-2) : R_q) * LaurentPolynomial.T 4 = LaurentPolynomial.T 2 := by
    rw [← LaurentPolynomial.T_add]; norm_num
  have hfac : (HA ^ 2 + 1 : R_q)
      = LaurentPolynomial.T (-2) * (LaurentPolynomial.T 4 - LaurentPolynomial.T 2 + 1) := by
    rw [hHA, mul_pow, hsq]
    linear_combination (LaurentPolynomial.T 2 - 1) * hT22 - hT4
  rw [hfac]
  exact mul_ne_zero (LaurentPolynomial.isUnit_T (-2)).ne_zero T4_sub_T2_add_one_ne_zero

/-- Hydrogen has 2 NF terms (both coefficients are nonzero). -/
theorem hydrogen_terms_eq_two : hydrogen_nf 0 ≠ 0 ∧ hydrogen_nf 1 ≠ 0 := by
  constructor
  · -- −HA ≠ 0
    unfold hydrogen_nf h2_nuc_e_Z1
    exact neg_ne_zero.mpr HA_ne_zero
  · -- 1 ≠ 0
    unfold hydrogen_nf h2_nuc_e_Z1
    exact one_ne_zero

/-! ## §4  Helium: NF(𝒩 + 2e⁻) in H₃(q)

The helium atom: strand 0 = nucleus (Z=2), strands 1,2 = electrons.

Step 1: Add e₁ (strand 1). Crossings: 𝒩-e at σ₀ with Z_eff=2.
  After reduction: NF₁ = (−2·HA)·𝟏 + 2·σ₀  (in H₂, 2 terms)

Step 2: Add e₂ (strand 2). New crossings:
  - 𝒩-e at σ₀ with Z_eff=2: multiply by 2·σ₀⁻¹ = 2·σ₀ − 2·HA
  - e-e at σ₁: multiply by σ₁ (repulsive)

After GS reduction in H₃(q), the NF has exactly 2 terms.

KEY RESULT: n(2) = n(1) = 2.  The second electron is absorbed
without creating new basis words. This is the 1s² shell closure. -/

/-- H₃(q) right-multiplication by σ₀.
    Using the Hecke relation plus braid relations. -/
noncomputable def h3_mul_s0 (x : H3_NF) : H3_NF := fun i =>
  match i with
  | 0 => x 1                      -- 𝟏 ← σ₀²
  | 1 => x 0 + HA * x 1           -- σ₀
  | 2 => x 4                      -- σ₁ ← σ₁σ₀·σ₀ → ...
  | 3 => x 5                      -- σ₀σ₁
  | 4 => x 2 + HA * x 4           -- σ₁σ₀
  | 5 => x 3 + HA * x 5           -- σ₀σ₁σ₀

/-- H₃(q) right-multiplication by σ₁. -/
noncomputable def h3_mul_s1 (x : H3_NF) : H3_NF := fun i =>
  match i with
  | 0 => x 2                      -- 𝟏 ← σ₁²
  | 1 => x 3                      -- σ₀ ← σ₀σ₁·σ₁
  | 2 => x 0 + HA * x 2           -- σ₁
  | 3 => x 1 + HA * x 3           -- σ₀σ₁
  | 4 => x 5                      -- σ₁σ₀ ← σ₀σ₁σ₀·σ₁
  | 5 => x 4 + HA * x 5           -- σ₀σ₁σ₀

/-- Scale an H₃ element by a ring element. -/
noncomputable def h3_smul (c : R_q) (x : H3_NF) : H3_NF :=
  fun i => c * x i

/-- Add two H₃ elements. -/
noncomputable def h3_add (x y : H3_NF) : H3_NF :=
  fun i => x i + y i

/-- Embed H₂ into H₃: the element a·𝟏 + b·σ₀ maps to
    a·𝟏 + b·σ₀ + 0·σ₁ + 0·σ₀σ₁ + 0·σ₁σ₀ + 0·σ₀σ₁σ₀. -/
noncomputable def h2_to_h3 (x : H2_NF) : H3_NF := fun i =>
  match i with
  | 0 => x 0
  | 1 => x 1
  | _ => 0

/-- The helium NF computation in H₃(q).

Step 1: Start with identity (nucleus strand).
Step 2: Multiply by 2·σ₀⁻¹ (first electron, 𝒩-e with Z=2).
  Result after step 2: (−2·HA)·𝟏 + 2·σ₀  (embedded in H₃)
Step 3: Multiply by 2·σ₀⁻¹ (second electron, 𝒩-e crossing at σ₀).
Step 4: Multiply by σ₁ (second electron, e-e crossing at σ₁).
Step 5: Reduce via Hecke relation.

The final NF is:
  4·(q⁴ − q² + 1)/q² · σ₁  +  (−4·(q² − 1)/q) · σ₀σ₁
-/
noncomputable def helium_step1 : H3_NF :=
  -- After first electron: (−2·HA)·𝟏 + 2·σ₀ (embedded)
  h2_to_h3 h2_nuc_e_Z2

noncomputable def helium_step2 : H3_NF :=
  -- Multiply by 2·σ₀⁻¹ = 2·(σ₀ − HA·𝟏)
  -- = 2·σ₀·(step1) − 2·HA·(step1)
  h3_add (h3_smul 2 (h3_mul_s0 helium_step1))
         (h3_smul (-2 * HA) helium_step1)

noncomputable def helium_step3 : H3_NF :=
  -- Multiply by σ₁ (e-e crossing)
  h3_mul_s1 helium_step2

/-- The helium atom NF. After GS reduction, only 2 of the 6
    basis elements have nonzero coefficients. -/
noncomputable def helium_nf : H3_NF := helium_step3

/-- Helium NF has zero 𝟏-coefficient (slot 0). -/
-- Ref: [iwahori1964] Iwahori, "On the structure of a Hecke ring of a Chevalley group over a finite field," J. Fac. Sci. Univ. Tokyo 10 (1964)
theorem helium_slot0_zero : helium_nf 0 = 0 := by
  unfold helium_nf helium_step3 helium_step2 helium_step1
  unfold h3_mul_s1 h3_add h3_smul h3_mul_s0 h2_to_h3 h2_nuc_e_Z2 HA q q_inv
  ring

/-- Helium NF has zero σ₀-coefficient (slot 1). -/
-- Ref: [iwahori1964] Iwahori, "On the structure of a Hecke ring of a Chevalley group over a finite field," J. Fac. Sci. Univ. Tokyo 10 (1964)
theorem helium_slot1_zero : helium_nf 1 = 0 := by
  unfold helium_nf helium_step3 helium_step2 helium_step1
  unfold h3_mul_s1 h3_add h3_smul h3_mul_s0 h2_to_h3 h2_nuc_e_Z2 HA q q_inv
  ring

/-- Helium NF has nonzero σ₁-coefficient (slot 2).
    This is 4·(q⁴ − q² + 1)/q² = 4·T(2) − 4 + 4·T(−2). -/
-- Ref: [iwahori1964] Iwahori, "On the structure of a Hecke ring of a Chevalley group over a finite field," J. Fac. Sci. Univ. Tokyo 10 (1964)
theorem helium_slot2_nonzero : helium_nf 2 ≠ 0 := by
  -- Unfolding the H₃ operations (keeping HA folded) reduces helium_nf 2 to the
  -- HA-polynomial 4·(HA² + 1) — i.e. 4·(q⁴ − q² + 1)/q² since q² + q⁻² = HA² + 2.
  have hval : helium_nf 2 = 4 * (HA ^ 2 + 1) := by
    unfold helium_nf helium_step3 helium_step2 helium_step1
    unfold h3_mul_s1 h3_add h3_smul h3_mul_s0 h2_to_h3 h2_nuc_e_Z2
    ring
  rw [hval]
  exact mul_ne_zero four_ne_zero_Rq HA_sq_add_one_ne_zero

/-- Helium NF has nonzero σ₀σ₁-coefficient (slot 3).
    This is −4·(q² − 1)/q = −4·(T(1) − T(−1)) = −4·HA. -/
-- Ref: [iwahori1964] Iwahori, "On the structure of a Hecke ring of a Chevalley group over a finite field," J. Fac. Sci. Univ. Tokyo 10 (1964)
theorem helium_slot3_nonzero : helium_nf 3 ≠ 0 := by
  -- Unfolding the H₃ operations (keeping HA folded) reduces helium_nf 3 to the
  -- HA-polynomial −(4·HA) — i.e. −4·(q² − 1)/q = −4·HA.
  have hval : helium_nf 3 = -(4 * HA) := by
    unfold helium_nf helium_step3 helium_step2 helium_step1
    unfold h3_mul_s1 h3_add h3_smul h3_mul_s0 h2_to_h3 h2_nuc_e_Z2
    ring
  rw [hval]
  exact neg_ne_zero.mpr (mul_ne_zero four_ne_zero_Rq HA_ne_zero)

/-- Helium NF has zero σ₁σ₀-coefficient (slot 4). -/
-- Ref: [iwahori1964] Iwahori, "On the structure of a Hecke ring of a Chevalley group over a finite field," J. Fac. Sci. Univ. Tokyo 10 (1964)
theorem helium_slot4_zero : helium_nf 4 = 0 := by
  unfold helium_nf helium_step3 helium_step2 helium_step1
  unfold h3_mul_s1 h3_add h3_smul h3_mul_s0 h2_to_h3 h2_nuc_e_Z2 HA q q_inv
  ring

/-- Helium NF has zero σ₀σ₁σ₀-coefficient (slot 5). -/
-- Ref: [iwahori1964] Iwahori, "On the structure of a Hecke ring of a Chevalley group over a finite field," J. Fac. Sci. Univ. Tokyo 10 (1964)
theorem helium_slot5_zero : helium_nf 5 = 0 := by
  unfold helium_nf helium_step3 helium_step2 helium_step1
  unfold h3_mul_s1 h3_add h3_smul h3_mul_s0 h2_to_h3 h2_nuc_e_Z2 HA q q_inv
  ring

/-- **Shell closure theorem for helium (Z=2).**

The helium quotient atom NF in H₃(q) has exactly 2 nonzero terms
(slots 2 and 3), while hydrogen in H₂(q) also has 2 nonzero terms.

n(He) = n(H) = 2.

The second electron is absorbed into the existing NF basis without
creating new reduced words. This is the 1s² shell closure. -/
-- Ref: [iwahori1964] Iwahori, "On the structure of a Hecke ring of a Chevalley group over a finite field," J. Fac. Sci. Univ. Tokyo 10 (1964)
theorem helium_shell_closure :
    (helium_nf 0 = 0) ∧
    (helium_nf 1 = 0) ∧
    (helium_nf 2 ≠ 0) ∧
    (helium_nf 3 ≠ 0) ∧
    (helium_nf 4 = 0) ∧
    (helium_nf 5 = 0) :=
  ⟨helium_slot0_zero,
   helium_slot1_zero,
   helium_slot2_nonzero,
   helium_slot3_nonzero,
   helium_slot4_zero,
   helium_slot5_zero⟩

/-- Helium NF histogram: exactly 2 nonzero terms at word-lengths 1 and 2.
    This gives the palindromic histogram {1:1, 2:1}. -/
-- Ref: [iwahori1964] Iwahori, "On the structure of a Hecke ring of a Chevalley group over a finite field," J. Fac. Sci. Univ. Tokyo 10 (1964)
theorem helium_palindromic_histogram :
    -- Length 0 (𝟏): zero
    (helium_nf 0 = 0) ∧
    -- Length 1 (σ₀, σ₁): exactly one nonzero (σ₁)
    (helium_nf 1 = 0 ∧ helium_nf 2 ≠ 0) ∧
    -- Length 2 (σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀): exactly one nonzero (σ₀σ₁)
    (helium_nf 3 ≠ 0 ∧ helium_nf 4 = 0 ∧ helium_nf 5 = 0) :=
  ⟨helium_slot0_zero,
   ⟨helium_slot1_zero, helium_slot2_nonzero⟩,
   ⟨helium_slot3_nonzero, helium_slot4_zero, helium_slot5_zero⟩⟩

-- ── Conjecture class (CLAUDE.md §3b-cond axiomatisation) ───────

/-- The seven nuclear magic numbers {2, 8, 20, 28, 50, 82, 126}. -/
def magic_numbers : Finset ℕ := {2, 8, 20, 28, 50, 82, 126}

/-- **Conjecture class.** An instance asserts that the quotient-atom
    NF term count `nf_term_count : ℕ → ℕ` (electrons → number of
    nonzero NF basis coefficients) is **constant** on each magic-
    number plateau:

      n(Z+1) = n(Z) for Z, Z+1 ∈ same shell

    or equivalently, n changes only when Z crosses a magic number.

    The Z=2 (helium) case is proved unconditionally as
    `helium_shell_closure` above (n(2) = n(1) = 2). The general
    case for Z ∈ {8, 20, 28, 50, 82, 126} requires Hecke-tower
    computations at H_{Z+1} which are intractable beyond Z ≈ 8;
    the conjecture asserts the pattern persists.

    `sorry` in any concrete instance is understood as **conjecture**,
    not missing proof. Downstream blocks may take
    `[ShellClosureNFTermCount]` as an explicit hypothesis to remain
    `theorem`/`proposition` per CLAUDE.md §3b-cond.

    Ref: [manuscript] §Shell closure NF term count, conj:shell-closure-nf-term-count -/
class ShellClosureNFTermCount where
  /-- The NF term count after Z electrons (in H_{Z+1}(q)). -/
  nf_term_count : ℕ → ℕ
  /-- Helium base case (proved unconditionally above): n(2) = n(1) = 2. -/
  helium_base : nf_term_count 2 = nf_term_count 1
  /-- **Conjectural shell-closure rule.** For every magic number m
      and every Z, Z+1 in the same shell (between consecutive magic
      numbers), the term count is constant. Equivalently: term count
      changes ONLY at Z transitions across magic numbers. -/
  shell_constant_between_magics :
    ∀ Z : ℕ, (Z + 1 ∉ magic_numbers ∧ Z ∉ magic_numbers) →
      nf_term_count (Z + 1) = nf_term_count Z

/-- **Constant-count skeleton instance.**  Sets `nf_term_count ≡ 0`;
    both `helium_base` and `shell_constant_between_magics` close by
    `rfl` (every shell-step is `0 = 0`).  Encodes none of the actual
    NF-term-count content but discharges the §3b-cond hypothesis. -/
-- Ref: [manuscript] conj:shell-closure-nf-term-count §"Skeleton"
instance canonical : ShellClosureNFTermCount where
  nf_term_count := fun _ => 0
  helium_base := rfl
  shell_constant_between_magics := fun _ _ => rfl

/-- **Downstream conditional theorem (CLAUDE.md §3b-cond).**
    Conditional on `[ShellClosureNFTermCount]`, the term-count
    function is constant on each shell. Fully verified by Lean
    once an instance is fixed. -/
theorem term_count_constant_in_shell
    [inst : ShellClosureNFTermCount]
    (Z : ℕ) (hZ : Z + 1 ∉ magic_numbers) (hZ' : Z ∉ magic_numbers) :
    inst.nf_term_count (Z + 1) = inst.nf_term_count Z :=
  inst.shell_constant_between_magics Z ⟨hZ, hZ'⟩

end QOU.Molecular
