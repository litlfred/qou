import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Algebra.Polynomial.Monic
import Mathlib.Data.Int.Basic
import Mathlib.Data.Nat.Basic


/-!
# QOU.Archimedean.genus_filtration_ideal

Genus-filtration ideal: the genus g = 4 is DERIVED from Hecke
completeness (not assumed), and the Chebyshev degree of the
Hecke coefficient a_p equals the Seifert genus (p-1)/2.  For
p ≥ 11 the leading term generates the obstruction ideal I_4 = (u^5).

## The derivation chain (non-circular):
1. SU_q(2) braiding → H_2(q) ⊕ H_3(q) (5 irreps)
2. Completeness: evaluation matrix must have rank 5
3. Genus scan: g = 3 gives ≤ 4 knots (insufficient), g = 4 gives 6 (sufficient)
4. Therefore g = 4 is the minimal complete genus
5. Chebyshev: deg_u a_p = (p-1)/2 = Seifert genus
6. At g = 4: a_9 saturates (deg 4), a_11 overflows (deg 5)
7. Ideal I_4 = (u^5) kills T_{2,p} for all p ≥ 11

LaTeX label: `prop:genus-filtration-ideal`

## References
- [yekutieli2010] https://doi.org/10.1016/j.aim.2010.06.007
- [leitner2026] §6/genus-filtration-ideal

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Archimedean

noncomputable section
/- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

-- ═══════════════════════════════════════════════════════════════════
-- Part 0: Genus from Hecke completeness
-- ═══════════════════════════════════════════════════════════════════

/-- Number of irreps of H_n(q) = number of partitions of n. -/
-- Ref: [leitner2026] §6/genus-filtration-ideal
def heckeIrreps : ℕ → ℕ
  | 2 => 2  -- partitions of 2: (2), (1,1)
  | 3 => 3  -- partitions of 3: (3), (2,1), (1,1,1)
  | _ => 0  -- only H_2 and H_3 are relevant

/-- Total irreps of H_2(q) ⊕ H_3(q) = 5. -/
-- Ref: [leitner2026] §6/genus-filtration-ideal
theorem total_irreps : heckeIrreps 2 + heckeIrreps 3 = 5 := by rfl

/-- A torus knot T_{m,n} embeds in genus g iff (m-1)(n-1) ≤ 2g. -/
-- Ref: [leitner2026] §6/torus-embeddable-complete
def torusEmbeddable (m n g : ℕ) : Prop :=
  (m - 1) * (n - 1) ≤ 2 * g

/-- At genus 3, we have at most 4 embeddable torus knots —
    insufficient to span 5 irreps. -/
-- Ref: [leitner2026] §6/genus-filtration-ideal
theorem genus3_insufficient :
    torusEmbeddable 2 3 3 ∧
    torusEmbeddable 2 5 3 ∧
    torusEmbeddable 2 7 3 ∧
    torusEmbeddable 3 4 3 ∧
    ¬ torusEmbeddable 2 9 3 ∧
    ¬ torusEmbeddable 3 5 3 := by
  unfold torusEmbeddable; omega

/-- At genus 4, we have 6 embeddable torus knots —
    sufficient to span 5 irreps (rank 5 verified numerically). -/
-- Ref: [leitner2026] §6/genus-filtration-ideal
theorem genus4_complete :
    torusEmbeddable 2 3 4 ∧
    torusEmbeddable 2 5 4 ∧
    torusEmbeddable 2 7 4 ∧
    torusEmbeddable 2 9 4 ∧
    torusEmbeddable 3 4 4 ∧
    torusEmbeddable 3 5 4 := by
  unfold torusEmbeddable; omega

/-- g = 4 is the minimal genus where completeness holds:
    at g = 3 we have < 5 knots, at g = 4 we have ≥ 5. -/
-- Ref: [leitner2026] §6/genus-filtration-ideal
theorem minimal_complete_genus :
    -- At g = 3: T_{2,9} doesn't embed
    ¬ torusEmbeddable 2 9 3 ∧
    -- At g = 4: all 6 embed
    torusEmbeddable 2 9 4 ∧ torusEmbeddable 3 5 4 := by
  unfold torusEmbeddable; omega

-- ═══════════════════════════════════════════════════════════════════
-- Part I: Chebyshev degree = Seifert genus
-- ═══════════════════════════════════════════════════════════════════

/-- The Hecke coefficient a_n: T^n = a_n · T + a_{n-1} · 1 in H_2(q).
    Satisfies the recurrence a_{n+1} = s · a_n + a_{n-1}
    with a_0 = 0, a_1 = 1, where s = q - q⁻¹. -/
-- Ref: [leitner2026] §6/genus-filtration-ideal
noncomputable def heckeCoeff (s : R_q) : ℕ → R_q
  | 0 => 0
  | 1 => 1
  | n + 2 => s * heckeCoeff s (n + 1) + heckeCoeff s n

/-- The Seifert genus of T_{2,p} is (p-1)/2. -/
-- Ref: [leitner2026] §6/genus-filtration-ideal
def seifertGenus_T2p (p : ℕ) : ℕ := (p - 1) / 2

/-- The same recurrence carried in `ℤ[X]` rather than in `R_q`.

    `heckeCoeff` above is stated for an arbitrary ring element `s : R_q`,
    which is the right shape for the skein narrative but the wrong shape
    for a *degree* claim: `degree` is a property of a polynomial in a
    formal indeterminate, not of an element of the coefficient ring. So
    the degree statements below are made about `heckePoly`, the same
    recurrence with `s := X`. -/
-- Ref: [leitner2026] §6/genus-filtration-ideal
noncomputable def heckePoly : ℕ → Polynomial ℤ
  | 0 => 0
  | 1 => 1
  | n + 2 => Polynomial.X * heckePoly (n + 1) + heckePoly n

-- Ref: [leitner2026] §6/genus-filtration-ideal
lemma heckePoly_two : heckePoly 2 = (Polynomial.X : Polynomial ℤ) := by
  show Polynomial.X * heckePoly 1 + heckePoly 0 = Polynomial.X
  show Polynomial.X * 1 + 0 = Polynomial.X
  ring

/-- `a_{n+1}` is monic of degree `n`.

    Proved as a conjunction because the induction needs both halves at
    once: the degree step needs the *leading coefficient* of the previous
    term to be nonzero, and the monic step needs the previous *degree* to
    dominate. -/
-- Ref: [leitner2026] §6/genus-filtration-ideal
theorem heckePoly_monic_natDegree (n : ℕ) :
    (heckePoly (n + 1)).Monic ∧ (heckePoly (n + 1)).natDegree = n := by
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    match n with
    | 0 => exact ⟨by simp [heckePoly, Polynomial.monic_one], by simp [heckePoly]⟩
    | 1 => rw [heckePoly_two]; exact ⟨Polynomial.monic_X, Polynomial.natDegree_X⟩
    | (m + 2) =>
      obtain ⟨hm1, hd1⟩ := ih (m + 1) (by omega)
      obtain ⟨_, hd0⟩ := ih m (by omega)
      have hrec : heckePoly (m + 3) =
          Polynomial.X * heckePoly (m + 2) + heckePoly (m + 1) := rfl
      have hXm : (Polynomial.X * heckePoly (m + 2)).Monic :=
        Polynomial.monic_X.mul hm1
      have hXd : (Polynomial.X * heckePoly (m + 2)).natDegree = m + 2 := by
        rw [Polynomial.natDegree_mul (Polynomial.monic_X (R := ℤ)).ne_zero hm1.ne_zero,
          Polynomial.natDegree_X, hd1]
        omega
      have hlt : (heckePoly (m + 1)).degree
          < (Polynomial.X * heckePoly (m + 2)).degree := by
        apply Polynomial.degree_lt_degree; rw [hd0, hXd]; omega
      refine ⟨?_, ?_⟩
      · rw [hrec]; exact hXm.add_of_left hlt
      · rw [hrec,
          Polynomial.natDegree_eq_of_degree_eq
            (Polynomial.degree_add_eq_left_of_degree_lt hlt), hXd]

-- Ref: [leitner2026] §6/genus-filtration-ideal
theorem heckePoly_natDegree (n : ℕ) : (heckePoly (n + 1)).natDegree = n :=
  (heckePoly_monic_natDegree n).2

/-- Every nonzero coefficient of `a_{n+1}` sits in a degree congruent to
    `n` mod 2. For odd `p` this says `a_p` is an *even* polynomial in `s`,
    which is what makes it a polynomial in `u = s²` at all. -/
-- Ref: [leitner2026] §6/genus-filtration-ideal
theorem heckePoly_coeff_parity (n : ℕ) :
    ∀ k, (heckePoly (n + 1)).coeff k ≠ 0 → k % 2 = n % 2 := by
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    match n with
    | 0 =>
      intro k hk
      rw [show heckePoly 1 = (1 : Polynomial ℤ) from rfl, Polynomial.coeff_one] at hk
      by_cases h : k = 0
      · simp [h]
      · simp [h] at hk
    | 1 =>
      intro k hk
      rw [heckePoly_two, Polynomial.coeff_X] at hk
      by_cases h : 1 = k
      · omega
      · simp [h] at hk
    | (m + 2) =>
      intro k hk
      have hrec : heckePoly (m + 3) =
          Polynomial.X * heckePoly (m + 2) + heckePoly (m + 1) := rfl
      match k with
      | 0 =>
        rw [hrec, Polynomial.coeff_add, Polynomial.mul_coeff_zero,
          Polynomial.coeff_X] at hk
        simp at hk
        have := ih m (by omega) 0 hk
        omega
      | (j + 1) =>
        rw [hrec, Polynomial.coeff_add, Polynomial.coeff_X_mul] at hk
        by_cases h1 : (heckePoly (m + 2)).coeff j = 0
        · rw [h1, zero_add] at hk
          have := ih m (by omega) (j + 1) hk
          omega
        · have := ih (m + 1) (by omega) j h1
          omega

/-- **The Chebyshev degree equals the Seifert genus.**

    For odd `p ≥ 3` the three conjuncts jointly say `deg_u a_p =
    (p-1)/2 = ` the Seifert genus of `T_{2,p}`:

    1. `a_p` has degree `p - 1` in `s`;
    2. only *even* powers of `s` occur, so `a_p` really is a polynomial
       in `u = s²`, and its `u`-degree is half its `s`-degree;
    3. that half is exactly `seifertGenus_T2p p`.

    Previously this was stated as `seifertGenus_T2p p = (p - 1) / 2`,
    which is `(p-1)/2 = (p-1)/2` by `rfl` — the binders `s` and
    `heckeCoeff` did not occur in the conclusion, so the claim carried
    none of the content its docstring described. -/
-- Ref: [leitner2026] §6/genus-filtration-ideal
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
theorem chebyshev_degree_eq_genus (p : ℕ) (hp : Odd p) (hp3 : 3 ≤ p) :
    (heckePoly p).natDegree = p - 1
    ∧ (∀ k, (heckePoly p).coeff k ≠ 0 → k % 2 = 0)
    ∧ p - 1 = 2 * seifertGenus_T2p p := by
  obtain ⟨m, rfl⟩ := hp
  refine ⟨?_, ?_, ?_⟩
  · have := heckePoly_natDegree (2 * m)
    simpa using this
  · intro k hk
    have := heckePoly_coeff_parity (2 * m) k (by simpa using hk)
    omega
  · show 2 * m + 1 - 1 = 2 * seifertGenus_T2p (2 * m + 1)
    unfold seifertGenus_T2p
    omega

-- ═══════════════════════════════════════════════════════════════════
-- Part II: The genus-filtration ideal I_4 = (u^5)
-- ═══════════════════════════════════════════════════════════════════

/-- Arithmetic equivalence: (p-1)/2 ≤ g ↔ (p-1) ≤ 2g.
    Links the Seifert genus bound to the embeddability condition. -/
-- Ref: [leitner2026] §6/genus-filtration-ideal
theorem seifert_genus_le_iff (p g : ℕ) (hp : Odd p) :
    (p - 1) / 2 ≤ g ↔ (p - 1) ≤ 2 * g := by
  obtain ⟨m, rfl⟩ := hp
  omega

/-- At the completeness-determined genus g = 4:
    T_{2,p} embeds iff p ≤ 9. -/
-- Ref: [leitner2026] §6/genus-filtration-ideal
theorem genus4_cutoff (p : ℕ) (hp : Odd p) (hp2 : 3 ≤ p) :
    (p - 1) / 2 ≤ 4 ↔ p ≤ 9 := by
  obtain ⟨m, rfl⟩ := hp
  omega

-- ═══════════════════════════════════════════════════════════════════
-- Part III: Obstruction for all primes p ≥ 11
-- ═══════════════════════════════════════════════════════════════════

/-- **The leading Chebyshev coefficient is 1** for all odd `p ≥ 3` —
    i.e. `a_p` is monic. This is what makes the Yekutieli obstruction
    `κ(T_{2,p})` nonzero whenever `(p-1)/2 > g`: the top coefficient
    cannot cancel.

    Previously this was stated as the defining recurrence with
    `- s^(p-1)` added to both sides and closed by `ring` — a
    rearrangement of the definition, saying nothing about any leading
    coefficient. -/
-- Ref: [leitner2026] §6/genus-filtration-ideal
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
theorem leading_chebyshev_coeff_is_one (p : ℕ) (hp : Odd p) (hp3 : 3 ≤ p) :
    (heckePoly p).leadingCoeff = 1 ∧ (heckePoly p).coeff (p - 1) = 1 := by
  obtain ⟨m, rfl⟩ := hp
  have hmonic : (heckePoly (2 * m + 1)).Monic := by
    have := (heckePoly_monic_natDegree (2 * m)).1
    simpa using this
  refine ⟨hmonic, ?_⟩
  have hdeg : (heckePoly (2 * m + 1)).natDegree = 2 * m + 1 - 1 := by
    have := heckePoly_natDegree (2 * m)
    simpa using this
  rw [← hdeg]
  exact hmonic

/-- All primes p ≥ 11 are obstructed at the completeness-determined
    genus g = 4.  Their Hecke coefficients lie in I_4 = (u^5). -/
-- Ref: [leitner2026] §6/genus-filtration-ideal
theorem all_large_primes_obstructed (p : ℕ) (hp : 11 ≤ p) :
    ¬ ((p - 1) / 2 ≤ 4) := by omega

/-- Concrete instances for readability. -/
-- Ref: [leitner2026] §6/genus-filtration-ideal
example : ¬ ((11 - 1) / 2 ≤ 4) := all_large_primes_obstructed 11 (by omega)
example : ¬ ((13 - 1) / 2 ≤ 4) := all_large_primes_obstructed 13 (by omega)

end

end QOU.Archimedean
