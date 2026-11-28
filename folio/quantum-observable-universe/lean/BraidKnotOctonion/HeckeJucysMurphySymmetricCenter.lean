/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
-/
import BraidKnotOctonion.HeckeJucysMurphyCommutation
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NoncommRing

/-!
# Full Jucys–Murphy Commutativity, Full-Twist Factorization, and the Symmetric Center of `H_n(q)`

Bean `qou-u9o1` (Stability Epic `qou-s028` & Compute-Accuracy Epic `qou-myts`).

`HeckeJucysMurphyCommutation.lean` reduced the structural half of `JucysMurphySpectrum` to one
explicit obstruction: adjacent commutativity `Lᵢ L_{i+1} = L_{i+1} Lᵢ` (leaving general `Lₐ L_b = L_b Lₐ`,
general `∏_{k<n} L_k = Δ_n²`, and centrality of higher symmetric polynomials `e_k(L₀,…,L_{n−1})`
open for `n ≥ 4`).  The exchange relations `σᵢ L_{i+1} = h L_{i+1} + Lᵢ σᵢ` could not close that
gap because they reduce `Lᵢ L_{i+1} = L_{i+1} Lᵢ` to another commutation of the same shape.

This module closes **100% of those structural questions**, working first in complete `[CommRing R]`
(and pure `Monoid`) generality (`§1–§3`, zero `[Field]` binders, zero `field_simp`, zero `sorry`)
and then specialising directly to `QOU.BraidKnot.Hecke.HeckeGenerators` (`§4`):

1. **§1 — Pure Braid Monoid Commutativity & General Full-Twist Factorization (`[Monoid M]`):**
   - `sigma_comm_jmMon_below`: for **all** `k, m : ℕ` with `k + 2 ≤ m`, `σ k * L m = L m * σ k`,
     proved from the braid relation `σ_{m−1} σ_m σ_{m−1} = σ_m σ_{m−1} σ_m` and
     above-commutation `jmMon_comm_sigma_above` (`m < j → σ j * L m = L m * σ j`) alone — **no
     Hecke quadratic relation and no inverses are used**.
   - `jmMon_comm`: **all** multiplicative Jucys–Murphy elements commute (`L a * L b = L b * L a`
     for every `a, b : ℕ`, including the adjacent case `b = a + 1`).
   - `jmMon_prod_eq_fullTwist`: for **every** `n : ℕ`, the ordered product `L₀ L₁ ⋯ L_{n−1}` equals
     the `n`-strand full twist `Δ_n² = (σ₀ σ₁ ⋯ σ_{n−2})^n`, proved via the Coxeter shift identity
     `σ_{j+1} C_{m+1} = C_{m+1} σ_j` (`j < m`).

2. **§2 — `[CommRing R]` Symmetric Center `e_k(L₀, …, L_{n−1}) ∈ Z(H_n(q))`:**
   - Over any `[CommRing R]`, `[Ring A]`, `[Algebra R A]` and deformation parameter `h : R` with
     `σᵢ² = h • σᵢ + 1`, `σᵢ` commutes with `Lᵢ + L_{i+1}`, with `Lᵢ * L_{i+1}`, and with every
     `L_j` for `j ≠ i, i + 1`.
   - `sigma_comm_elemSymmJM`: **every** elementary symmetric polynomial `e_k(L₀, …, L_{n−1})`
     commutes with `σᵢ` for all `i + 1 < n` and all `k : ℕ`.

3. **§3 — Trivial & Sign Character Eigenvalues over `[CommRing R]` (`q : Rˣ`):**
   - Under QOU's §7a balanced quadratic `σᵢ² = (q − q⁻¹)σᵢ + 1`, the trivial one-row character
     `σᵢ ↦ q` maps `L_k ↦ q^{2k}` (exact content eigenvalue `q^{2 c(0, k)}`), while the sign
     one-column character `σᵢ ↦ -q⁻¹` maps `L_k ↦ q^{-2k}` (`q^{2 c(k, 0)}`).

4. **§4 — Direct Discharge on `HeckeGenerators` (`HeckeJucysMurphyCommutation` / Bean `qou-u9o1`):**
   - Transfers `sigma_comm_jmRaw_below`, `jmRaw_comm`, `sigma_comm_jmRaw_prod`,
     `sigma_comm_elemSymm_jmRaw`, `jmRaw_prod_eq_fullTwist`, and `jm_eq_pow_smul_jmRaw` directly
     onto `QOU.BraidKnot.Hecke.HeckeGenerators`.

-- Ref: [dipper-james1986] R. Dipper, G. James, Proc. LMS s3-52 (1986), 20–52.
-- Ref: [dipper-james1987] R. Dipper, G. James, Proc. LMS s3-54 (1987), 57–82.
-- Ref: [murphy1992] G. E. Murphy, J. Algebra 152 (1992), 492–513.
-- Ref: [murphy1995] G. E. Murphy, J. Algebra 173 (1995), 97–121.
-- Ref: [mathas1999] A. Mathas, AMS ULECT 15 (1999), Ch. 3.
-- Ref: [wenzl1988] H. Wenzl, Invent. Math. 92 (1988), 349–383.
-/

set_option autoImplicit false

namespace QOU.BraidKnot.HeckeSymmetricCenter

/-! ## §1. Pure Braid Monoid Commutativity & Full-Twist Factorization -/

section BraidMonoid

variable {M : Type*} [Monoid M]

/-- Minimal Artin braid-monoid data on indexed generators `σ : ℕ → M`: adjacent braid relations
and far commutation. -/
structure BraidMonoidGen (M : Type*) [Monoid M] where
  σ : ℕ → M
  braid : ∀ i : ℕ, σ i * σ (i + 1) * σ i = σ (i + 1) * σ i * σ (i + 1)
  far : ∀ i j : ℕ, i + 1 < j → σ i * σ j = σ j * σ i

/-- Multiplicative Jucys–Murphy elements in any monoid: `L₀ = 1`, `L_{i+1} = σᵢ Lᵢ σᵢ`. -/
def jmMon (B : BraidMonoidGen M) : ℕ → M
  | 0 => 1
  | i + 1 => B.σ i * jmMon B i * B.σ i

@[simp] theorem jmMon_zero (B : BraidMonoidGen M) : jmMon B 0 = 1 := rfl

theorem jmMon_succ (B : BraidMonoidGen M) (i : ℕ) :
    jmMon B (i + 1) = B.σ i * jmMon B i * B.σ i := rfl

/-- **Above-commutation:** `σⱼ` commutes with `Lᵢ` whenever `i < j`. -/
theorem jmMon_comm_sigma_above (B : BraidMonoidGen M) :
    ∀ i j : ℕ, i < j → B.σ j * jmMon B i = jmMon B i * B.σ j := by
  intro i
  induction i with
  | zero =>
      intro j _
      simp
  | succ k ih =>
      intro j hj
      have hfar : B.σ k * B.σ j = B.σ j * B.σ k := B.far k j (by omega)
      have hk : B.σ j * jmMon B k = jmMon B k * B.σ j := ih j (by omega)
      rw [jmMon_succ]
      calc B.σ j * (B.σ k * jmMon B k * B.σ k)
          = (B.σ j * B.σ k) * jmMon B k * B.σ k := by simp [mul_assoc]
        _ = (B.σ k * B.σ j) * jmMon B k * B.σ k := by rw [← hfar]
        _ = B.σ k * (B.σ j * jmMon B k) * B.σ k := by simp [mul_assoc]
        _ = B.σ k * (jmMon B k * B.σ j) * B.σ k := by rw [hk]
        _ = B.σ k * jmMon B k * (B.σ j * B.σ k) := by simp [mul_assoc]
        _ = B.σ k * jmMon B k * (B.σ k * B.σ j) := by rw [hfar]
        _ = B.σ k * jmMon B k * B.σ k * B.σ j := by simp [mul_assoc]

/-- **Below-commutation (key lemma closing `qou-u9o1`):** `σ_k` commutes with `L_m` whenever
`k + 2 ≤ m`. -/
theorem sigma_comm_jmMon_below (B : BraidMonoidGen M) :
    ∀ m k : ℕ, k + 2 ≤ m → B.σ k * jmMon B m = jmMon B m * B.σ k := by
  intro m
  induction m with
  | zero =>
      intro k hk
      omega
  | succ n ih =>
      intro k hk
      rcases Nat.eq_or_lt_of_le hk with h_eq | h_lt
      · have hn : n = k + 1 := by omega
        subst hn
        have hb : B.σ k * B.σ (k + 1) * B.σ k = B.σ (k + 1) * B.σ k * B.σ (k + 1) := B.braid k
        have habove : B.σ (k + 1) * jmMon B k = jmMon B k * B.σ (k + 1) :=
          jmMon_comm_sigma_above B k (k + 1) (by omega)
        rw [jmMon_succ, jmMon_succ]
        calc B.σ k * (B.σ (k + 1) * (B.σ k * jmMon B k * B.σ k) * B.σ (k + 1))
            = (B.σ k * B.σ (k + 1) * B.σ k) * jmMon B k * B.σ k * B.σ (k + 1) := by
                simp [mul_assoc]
          _ = (B.σ (k + 1) * B.σ k * B.σ (k + 1)) * jmMon B k * B.σ k * B.σ (k + 1) := by
                rw [hb]
          _ = B.σ (k + 1) * B.σ k * (B.σ (k + 1) * jmMon B k) * B.σ k * B.σ (k + 1) := by
                simp [mul_assoc]
          _ = B.σ (k + 1) * B.σ k * (jmMon B k * B.σ (k + 1)) * B.σ k * B.σ (k + 1) := by
                rw [habove]
          _ = B.σ (k + 1) * B.σ k * jmMon B k * (B.σ (k + 1) * B.σ k * B.σ (k + 1)) := by
                simp [mul_assoc]
          _ = B.σ (k + 1) * B.σ k * jmMon B k * (B.σ k * B.σ (k + 1) * B.σ k) := by
                rw [← hb]
          _ = (B.σ (k + 1) * (B.σ k * jmMon B k * B.σ k) * B.σ (k + 1)) * B.σ k := by
                simp [mul_assoc]
      · have hfar : B.σ k * B.σ n = B.σ n * B.σ k := B.far k n (by omega)
        have hsub : B.σ k * jmMon B n = jmMon B n * B.σ k := ih k (by omega)
        rw [jmMon_succ]
        calc B.σ k * (B.σ n * jmMon B n * B.σ n)
            = (B.σ k * B.σ n) * jmMon B n * B.σ n := by simp [mul_assoc]
          _ = (B.σ n * B.σ k) * jmMon B n * B.σ n := by rw [hfar]
          _ = B.σ n * (B.σ k * jmMon B n) * B.σ n := by simp [mul_assoc]
          _ = B.σ n * (jmMon B n * B.σ k) * B.σ n := by rw [hsub]
          _ = B.σ n * jmMon B n * (B.σ k * B.σ n) := by simp [mul_assoc]
          _ = B.σ n * jmMon B n * (B.σ n * B.σ k) := by rw [hfar]
          _ = B.σ n * jmMon B n * B.σ n * B.σ k := by simp [mul_assoc]

theorem jmMon_comm_of_le (B : BraidMonoidGen M) :
    ∀ a b : ℕ, a ≤ b → jmMon B a * jmMon B b = jmMon B b * jmMon B a := by
  intro a
  induction a with
  | zero =>
      intro b _
      simp
  | succ k ih =>
      intro b hkb
      rcases Nat.eq_or_lt_of_le hkb with rfl | hlt
      · rfl
      · have hsig : B.σ k * jmMon B b = jmMon B b * B.σ k :=
          sigma_comm_jmMon_below B b k (by omega)
        have hprev : jmMon B k * jmMon B b = jmMon B b * jmMon B k :=
          ih b (by omega)
        rw [jmMon_succ]
        calc (B.σ k * jmMon B k * B.σ k) * jmMon B b
            = B.σ k * jmMon B k * (B.σ k * jmMon B b) := by simp [mul_assoc]
          _ = B.σ k * jmMon B k * (jmMon B b * B.σ k) := by rw [hsig]
          _ = B.σ k * (jmMon B k * jmMon B b) * B.σ k := by simp [mul_assoc]
          _ = B.σ k * (jmMon B b * jmMon B k) * B.σ k := by rw [hprev]
          _ = (B.σ k * jmMon B b) * jmMon B k * B.σ k := by simp [mul_assoc]
          _ = (jmMon B b * B.σ k) * jmMon B k * B.σ k := by rw [hsig]
          _ = jmMon B b * (B.σ k * jmMon B k * B.σ k) := by simp [mul_assoc]

/-- **Unconditional Jucys–Murphy commutativity (`L_a * L_b = L_b * L_a` for all `a, b : ℕ`).** -/
theorem jmMon_comm (B : BraidMonoidGen M) (a b : ℕ) :
    jmMon B a * jmMon B b = jmMon B b * jmMon B a := by
  rcases le_total a b with hab | hba
  · exact jmMon_comm_of_le B a b hab
  · exact (jmMon_comm_of_le B b a hba).symm

/-- Ascending Coxeter word `C_k = σ₀ σ₁ ⋯ σ_{k−1}` (`C₀ = 1`). -/
def coxeterPrefix (B : BraidMonoidGen M) : ℕ → M
  | 0 => 1
  | k + 1 => coxeterPrefix B k * B.σ k

/-- Reversed Coxeter word `R_k = σ_{k−1} ⋯ σ₁ σ₀` (`R₀ = 1`). -/
def revCoxeterPrefix (B : BraidMonoidGen M) : ℕ → M
  | 0 => 1
  | k + 1 => B.σ k * revCoxeterPrefix B k

/-- Descending partial suffix `D(m, r) = σ_m σ_{m−1} ⋯ σ_{m+1−r}` (`D(m, 0) = 1`). -/
def descFromTop (B : BraidMonoidGen M) (m : ℕ) : ℕ → M
  | 0 => 1
  | r + 1 => descFromTop B m r * B.σ (m - r)

/-- Ordered left-to-right product `L₀ * L₁ * ⋯ * L_{n−1}`. -/
def jmMonProd (B : BraidMonoidGen M) : ℕ → M
  | 0 => 1
  | n + 1 => jmMonProd B n * jmMon B n

/-- The `n`-strand full twist `Δ_n²`: `1` for `n = 0`, and `(σ₀ σ₁ ⋯ σ_{n−2})^n` for `n ≥ 1`. -/
def fullTwistMon (B : BraidMonoidGen M) : ℕ → M
  | 0 => 1
  | k + 1 => (coxeterPrefix B k) ^ (k + 1)

theorem revCoxeter_mul_coxeter_eq_jmMon (B : BraidMonoidGen M) (k : ℕ) :
    revCoxeterPrefix B k * coxeterPrefix B k = jmMon B k := by
  induction k with
  | zero => simp [revCoxeterPrefix, coxeterPrefix]
  | succ m ih =>
      simp only [revCoxeterPrefix, coxeterPrefix, jmMon_succ]
      calc (B.σ m * revCoxeterPrefix B m) * (coxeterPrefix B m * B.σ m)
          = B.σ m * (revCoxeterPrefix B m * coxeterPrefix B m) * B.σ m := by simp [mul_assoc]
        _ = B.σ m * jmMon B m * B.σ m := by rw [ih]

theorem coxeterPrefix_comm_far (B : BraidMonoidGen M) :
    ∀ r s : ℕ, r < s → coxeterPrefix B r * B.σ s = B.σ s * coxeterPrefix B r := by
  intro r
  induction r with
  | zero =>
      intro s _
      simp [coxeterPrefix]
  | succ k ih =>
      intro s hs
      have hfar : B.σ k * B.σ s = B.σ s * B.σ k := B.far k s (by omega)
      have hk : coxeterPrefix B k * B.σ s = B.σ s * coxeterPrefix B k := ih s (by omega)
      simp only [coxeterPrefix]
      calc coxeterPrefix B k * B.σ k * B.σ s
          = coxeterPrefix B k * (B.σ k * B.σ s) := by simp [mul_assoc]
        _ = coxeterPrefix B k * (B.σ s * B.σ k) := by rw [hfar]
        _ = (coxeterPrefix B k * B.σ s) * B.σ k := by simp [mul_assoc]
        _ = (B.σ s * coxeterPrefix B k) * B.σ k := by rw [hk]
        _ = B.σ s * (coxeterPrefix B k * B.σ k) := by simp [mul_assoc]

/-- **Coxeter shift identity:** `σ_{j+1} * C_{k+1} = C_{k+1} * σ_j` whenever `j < k`. -/
theorem sigma_succ_mul_coxeterPrefix (B : BraidMonoidGen M) :
    ∀ k j : ℕ, j < k → B.σ (j + 1) * coxeterPrefix B (k + 1) = coxeterPrefix B (k + 1) * B.σ j := by
  intro k
  induction k with
  | zero =>
      intro j hj
      omega
  | succ m ih =>
      intro j hj
      rcases Nat.eq_or_lt_of_le (Nat.le_of_lt_succ hj) with hjm | hlt
      · subst hjm
        have hcomm : coxeterPrefix B j * B.σ (j + 1) = B.σ (j + 1) * coxeterPrefix B j :=
          coxeterPrefix_comm_far B j (j + 1) (by omega)
        have hb : B.σ (j + 1) * B.σ j * B.σ (j + 1) = B.σ j * B.σ (j + 1) * B.σ j :=
          (B.braid j).symm
        simp only [coxeterPrefix]
        calc B.σ (j + 1) * (coxeterPrefix B j * B.σ j * B.σ (j + 1))
            = (B.σ (j + 1) * coxeterPrefix B j) * B.σ j * B.σ (j + 1) := by simp [mul_assoc]
          _ = (coxeterPrefix B j * B.σ (j + 1)) * B.σ j * B.σ (j + 1) := by rw [← hcomm]
          _ = coxeterPrefix B j * (B.σ (j + 1) * B.σ j * B.σ (j + 1)) := by simp [mul_assoc]
          _ = coxeterPrefix B j * (B.σ j * B.σ (j + 1) * B.σ j) := by rw [hb]
          _ = (coxeterPrefix B j * B.σ j * B.σ (j + 1)) * B.σ j := by simp [mul_assoc]
      · have hprev : B.σ (j + 1) * coxeterPrefix B (m + 1) = coxeterPrefix B (m + 1) * B.σ j :=
          ih j hlt
        have hfar : B.σ j * B.σ (m + 1) = B.σ (m + 1) * B.σ j := B.far j (m + 1) (by omega)
        simp only [coxeterPrefix]
        calc B.σ (j + 1) * (coxeterPrefix B (m + 1) * B.σ (m + 1))
            = (B.σ (j + 1) * coxeterPrefix B (m + 1)) * B.σ (m + 1) := by simp [mul_assoc]
          _ = (coxeterPrefix B (m + 1) * B.σ j) * B.σ (m + 1) := by rw [hprev]
          _ = coxeterPrefix B (m + 1) * (B.σ j * B.σ (m + 1)) := by simp [mul_assoc]
          _ = coxeterPrefix B (m + 1) * (B.σ (m + 1) * B.σ j) := by rw [hfar]
          _ = (coxeterPrefix B (m + 1) * B.σ (m + 1)) * B.σ j := by simp [mul_assoc]

theorem descFromTop_mul_coxeterPrefix (B : BraidMonoidGen M) (m : ℕ) :
    ∀ r : ℕ, r ≤ m →
      descFromTop B m r * coxeterPrefix B (m + 1) = coxeterPrefix B m * descFromTop B m (r + 1) := by
  intro r
  induction r with
  | zero =>
      intro _
      simp [descFromTop, coxeterPrefix]
  | succ s ih =>
      intro hrs
      have hstep : B.σ (m - s) * coxeterPrefix B (m + 1) =
          coxeterPrefix B (m + 1) * B.σ (m - (s + 1)) := by
        have hsub : m - s = (m - (s + 1)) + 1 := by omega
        rw [hsub]
        exact sigma_succ_mul_coxeterPrefix B m (m - (s + 1)) (by omega)
      have hprev := ih (by omega)
      simp only [descFromTop]
      calc descFromTop B m s * B.σ (m - s) * coxeterPrefix B (m + 1)
          = descFromTop B m s * (B.σ (m - s) * coxeterPrefix B (m + 1)) := by simp [mul_assoc]
        _ = descFromTop B m s * (coxeterPrefix B (m + 1) * B.σ (m - (s + 1))) := by rw [hstep]
        _ = (descFromTop B m s * coxeterPrefix B (m + 1)) * B.σ (m - (s + 1)) := by simp [mul_assoc]
        _ = (coxeterPrefix B m * descFromTop B m (s + 1)) * B.σ (m - (s + 1)) := by rw [hprev]
        _ = coxeterPrefix B m * (descFromTop B m (s + 1) * B.σ (m - (s + 1))) := by simp [mul_assoc]

theorem coxeterPrefix_pow_split (B : BraidMonoidGen M) (m : ℕ) :
    ∀ r : ℕ, r ≤ m + 1 →
      (coxeterPrefix B (m + 1)) ^ r = (coxeterPrefix B m) ^ r * descFromTop B m r := by
  intro r
  induction r with
  | zero =>
      intro _
      simp [descFromTop]
  | succ s ih =>
      intro hrs
      have hprev := ih (by omega)
      have hdesc := descFromTop_mul_coxeterPrefix B m s (by omega)
      rw [pow_succ, hprev]
      calc (coxeterPrefix B m) ^ s * descFromTop B m s * coxeterPrefix B (m + 1)
          = (coxeterPrefix B m) ^ s * (descFromTop B m s * coxeterPrefix B (m + 1)) := by
              simp [mul_assoc]
        _ = (coxeterPrefix B m) ^ s * (coxeterPrefix B m * descFromTop B m (s + 1)) := by
              rw [hdesc]
        _ = ((coxeterPrefix B m) ^ s * coxeterPrefix B m) * descFromTop B m (s + 1) := by
              simp [mul_assoc]
        _ = (coxeterPrefix B m) ^ (s + 1) * descFromTop B m (s + 1) := by rw [← pow_succ]

theorem descFromTop_shift (B : BraidMonoidGen M) (n : ℕ) :
    ∀ r : ℕ, r ≤ n + 1 →
      descFromTop B (n + 1) (r + 1) = B.σ (n + 1) * descFromTop B n r := by
  intro r
  induction r with
  | zero => intro _; simp [descFromTop]
  | succ t iht =>
      intro hrt
      have ht := iht (by omega)
      have hidx : n + 1 - (t + 1) = n - t := by omega
      change descFromTop B (n + 1) (t + 1) * B.σ (n + 1 - (t + 1)) =
        B.σ (n + 1) * (descFromTop B n t * B.σ (n - t))
      rw [hidx, ht, mul_assoc]

theorem descFromTop_full_eq_revCoxeter (B : BraidMonoidGen M) (m : ℕ) :
    descFromTop B m (m + 1) = revCoxeterPrefix B (m + 1) := by
  induction m with
  | zero => simp [descFromTop, revCoxeterPrefix]
  | succ n ih =>
      rw [descFromTop_shift B n (n + 1) (le_refl _), ih]
      rfl

/-- **General Full-Twist Factorization (`∏_{k<n} L_k = Δ_n²` for all `n : ℕ`):**
holds unconditionally in every Artin braid monoid. -/
theorem jmMon_prod_eq_fullTwist (B : BraidMonoidGen M) (n : ℕ) :
    jmMonProd B n = fullTwistMon B n := by
  induction n with
  | zero => rfl
  | succ k ih =>
      cases k with
      | zero =>
          simp [jmMonProd, fullTwistMon, coxeterPrefix]
      | succ m =>
          change jmMonProd B (m + 1) * jmMon B (m + 1) = fullTwistMon B (m + 2)
          rw [ih]
          simp only [fullTwistMon]
          have hpow := coxeterPrefix_pow_split B m (m + 1) (le_refl _)
          have hrev := descFromTop_full_eq_revCoxeter B m
          have hjm := revCoxeter_mul_coxeter_eq_jmMon B (m + 1)
          rw [pow_succ (coxeterPrefix B (m + 1)) (m + 1), hpow, hrev, mul_assoc, hjm]

end BraidMonoid

/-! ## §2. `[CommRing R]` Symmetric Center `e_k(L₀, …, L_{n−1}) ∈ Z(H_n(q))` -/

section SymmetricCenter

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- Division-free type-A Hecke algebra presentation over any `[CommRing R]` with deformation
parameter `h : R` (`σᵢ² = h • σᵢ + 1`). -/
structure HeckeRingGen (R : Type*) [CommRing R] (A : Type*) [Ring A] [Algebra R A] (h : R)
    extends BraidMonoidGen A where
  hecke : ∀ i : ℕ, σ i * σ i = h • σ i + 1

/-- Multiplicative Jucys–Murphy elements `L_k` of `H : HeckeRingGen R A h`. -/
abbrev jmRing {h : R} (H : HeckeRingGen R A h) : ℕ → A :=
  jmMon H.toBraidMonoidGen

theorem sigma_mul_jmRing_succ {h : R} (H : HeckeRingGen R A h) (i : ℕ) :
    H.σ i * jmRing H (i + 1) = h • jmRing H (i + 1) + jmRing H i * H.σ i := by
  unfold jmRing
  rw [jmMon_succ]
  calc H.σ i * (H.σ i * jmMon H.toBraidMonoidGen i * H.σ i)
      = ((H.σ i * H.σ i) * jmMon H.toBraidMonoidGen i) * H.σ i := by
          simp only [mul_assoc]
    _ = ((h • H.σ i + 1) * jmMon H.toBraidMonoidGen i) * H.σ i := by rw [H.hecke i]
    _ = h • (H.σ i * jmMon H.toBraidMonoidGen i * H.σ i) +
          jmMon H.toBraidMonoidGen i * H.σ i := by
          simp only [add_mul, one_mul, smul_mul_assoc]

theorem jmRing_succ_mul_sigma {h : R} (H : HeckeRingGen R A h) (i : ℕ) :
    jmRing H (i + 1) * H.σ i = h • jmRing H (i + 1) + H.σ i * jmRing H i := by
  unfold jmRing
  rw [jmMon_succ]
  calc (H.σ i * jmMon H.toBraidMonoidGen i * H.σ i) * H.σ i
      = (H.σ i * jmMon H.toBraidMonoidGen i) * (H.σ i * H.σ i) := by
          simp only [mul_assoc]
    _ = (H.σ i * jmMon H.toBraidMonoidGen i) * (h • H.σ i + 1) := by rw [H.hecke i]
    _ = h • (H.σ i * jmMon H.toBraidMonoidGen i * H.σ i) +
          H.σ i * jmMon H.toBraidMonoidGen i := by
          simp only [mul_add, mul_one, mul_smul_comm]

/-- `σᵢ` commutes with the adjacent sum `Lᵢ + L_{i+1}` over any `[CommRing R]`. -/
theorem sigma_comm_jmRing_add {h : R} (H : HeckeRingGen R A h) (i : ℕ) :
    H.σ i * (jmRing H i + jmRing H (i + 1)) = (jmRing H i + jmRing H (i + 1)) * H.σ i := by
  have h1 := sigma_mul_jmRing_succ H i
  have h2 := jmRing_succ_mul_sigma H i
  have hσL : H.σ i * jmRing H i = jmRing H (i + 1) * H.σ i - h • jmRing H (i + 1) := by
    rw [h2]; abel
  rw [mul_add, add_mul, hσL, h1]
  abel

/-- **`σᵢ` commutes with the adjacent product `Lᵢ * L_{i+1}` over any `[CommRing R]`.** -/
theorem sigma_comm_jmRing_prod {h : R} (H : HeckeRingGen R A h) (i : ℕ) :
    H.σ i * (jmRing H i * jmRing H (i + 1)) = (jmRing H i * jmRing H (i + 1)) * H.σ i := by
  have h1 := sigma_mul_jmRing_succ H i
  have h2 := jmRing_succ_mul_sigma H i
  have hcomm : jmRing H (i + 1) * jmRing H i = jmRing H i * jmRing H (i + 1) :=
    jmMon_comm H.toBraidMonoidGen (i + 1) i
  have hσL : H.σ i * jmRing H i = jmRing H (i + 1) * H.σ i - h • jmRing H (i + 1) := by
    rw [h2]; abel
  calc H.σ i * (jmRing H i * jmRing H (i + 1))
      = (H.σ i * jmRing H i) * jmRing H (i + 1) := (mul_assoc _ _ _).symm
    _ = (jmRing H (i + 1) * H.σ i - h • jmRing H (i + 1)) * jmRing H (i + 1) := by rw [hσL]
    _ = jmRing H (i + 1) * (H.σ i * jmRing H (i + 1)) -
          h • (jmRing H (i + 1) * jmRing H (i + 1)) := by
        rw [sub_mul, mul_assoc, smul_mul_assoc]
    _ = jmRing H (i + 1) * (h • jmRing H (i + 1) + jmRing H i * H.σ i) -
          h • (jmRing H (i + 1) * jmRing H (i + 1)) := by rw [h1]
    _ = (jmRing H (i + 1) * jmRing H i) * H.σ i := by
        rw [mul_add, mul_smul_comm, add_sub_cancel_left, ← mul_assoc]
    _ = (jmRing H i * jmRing H (i + 1)) * H.σ i := by rw [hcomm]

/-- Elementary symmetric polynomial `e_k` evaluated on an ordered list of ring elements. -/
def elemSymmList : ℕ → List A → A
  | 0, _ => 1
  | _ + 1, [] => 0
  | k + 1, x :: xs => elemSymmList (k + 1) xs + x * elemSymmList k xs

@[simp] theorem elemSymmList_zero (xs : List A) : elemSymmList 0 xs = 1 := by
  cases xs <;> rfl

@[simp] theorem elemSymmList_nil_succ (k : ℕ) : elemSymmList (k + 1) ([] : List A) = 0 := rfl

theorem elemSymmList_cons_succ (k : ℕ) (x : A) (xs : List A) :
    elemSymmList (k + 1) (x :: xs) = elemSymmList (k + 1) xs + x * elemSymmList k xs := rfl

/-- If `z` commutes with every element of `xs`, `z` commutes with `elemSymmList k xs`. -/
theorem comm_elemSymmList_of_forall {z : A} {xs : List A}
    (hz : ∀ x ∈ xs, z * x = x * z) :
    ∀ k : ℕ, z * elemSymmList k xs = elemSymmList k xs * z := by
  induction xs with
  | nil =>
      intro k
      cases k <;> simp
  | cons x rest ih =>
      intro k
      cases k with
      | zero => simp
      | succ m =>
          have hx : z * x = x * z := hz x List.mem_cons_self
          have hrest : ∀ y ∈ rest, z * y = y * z :=
            fun y hy => hz y (List.mem_cons_of_mem _ hy)
          have ih1 := ih hrest (m + 1)
          have ih0 := ih hrest m
          rw [elemSymmList_cons_succ]
          calc z * (elemSymmList (m + 1) rest + x * elemSymmList m rest)
              = z * elemSymmList (m + 1) rest + (z * x) * elemSymmList m rest := by noncomm_ring
            _ = elemSymmList (m + 1) rest * z + (x * z) * elemSymmList m rest := by rw [ih1, hx]
            _ = elemSymmList (m + 1) rest * z + x * (z * elemSymmList m rest) := by noncomm_ring
            _ = elemSymmList (m + 1) rest * z + x * (elemSymmList m rest * z) := by rw [ih0]
            _ = (elemSymmList (m + 1) rest + x * elemSymmList m rest) * z := by noncomm_ring

/-- Swapping the first two elements of `x :: y :: xs` preserves `elemSymmList k` whenever `x * y = y * x`. -/
theorem elemSymmList_swap_head {x y : A} (hxy : x * y = y * x) (xs : List A) (k : ℕ) :
    elemSymmList k (x :: y :: xs) = elemSymmList k (y :: x :: xs) := by
  cases k with
  | zero => simp
  | succ m =>
      cases m with
      | zero =>
          simp only [elemSymmList_cons_succ, elemSymmList_zero, mul_one]
          abel
      | succ r =>
          simp only [elemSymmList_cons_succ]
          calc (elemSymmList (r + 2) xs + y * elemSymmList (r + 1) xs) +
                x * (elemSymmList (r + 1) xs + y * elemSymmList r xs)
              = elemSymmList (r + 2) xs + y * elemSymmList (r + 1) xs +
                  x * elemSymmList (r + 1) xs + (x * y) * elemSymmList r xs := by noncomm_ring
            _ = elemSymmList (r + 2) xs + y * elemSymmList (r + 1) xs +
                  x * elemSymmList (r + 1) xs + (y * x) * elemSymmList r xs := by rw [hxy]
            _ = (elemSymmList (r + 2) xs + x * elemSymmList (r + 1) xs) +
                  y * (elemSymmList (r + 1) xs + x * elemSymmList r xs) := by noncomm_ring

/-- Pulling `a` past `us` (when every `u ∈ us` commutes with `a`) preserves `elemSymmList k`. -/
theorem elemSymmList_pull_front {a : A} {us vs : List A}
    (ha : ∀ u ∈ us, u * a = a * u) :
    ∀ k : ℕ, elemSymmList k (us ++ a :: vs) = elemSymmList k (a :: (us ++ vs)) := by
  induction us with
  | nil => intro _; rfl
  | cons u rest ih =>
      intro k
      have hua : u * a = a * u := ha u List.mem_cons_self
      have hrest : ∀ x ∈ rest, x * a = a * x :=
        fun x hx => ha x (List.mem_cons_of_mem _ hx)
      simp only [List.cons_append]
      have hstep : ∀ m : ℕ, elemSymmList m (u :: (rest ++ a :: vs)) =
          elemSymmList m (u :: a :: (rest ++ vs)) := by
        intro m
        cases m with
        | zero => simp
        | succ r =>
            rw [elemSymmList_cons_succ r u (rest ++ a :: vs),
              elemSymmList_cons_succ r u (a :: (rest ++ vs)),
              ih hrest (r + 1), ih hrest r]
      rw [hstep k, elemSymmList_swap_head hua (rest ++ vs) k]

/-- If `z` commutes with `a + b`, with `a * b`, and with every element of `xs`, then `z` commutes
with `elemSymmList k (a :: b :: xs)`. -/
theorem comm_elemSymmList_pair_head {z a b : A} {xs : List A}
    (hsum : z * (a + b) = (a + b) * z)
    (hprod : z * (a * b) = (a * b) * z)
    (hxs : ∀ x ∈ xs, z * x = x * z) (k : ℕ) :
    z * elemSymmList k (a :: b :: xs) = elemSymmList k (a :: b :: xs) * z := by
  cases k with
  | zero => simp
  | succ m =>
      cases m with
      | zero =>
          have h1 := comm_elemSymmList_of_forall hxs 1
          have hexp : elemSymmList 1 (a :: b :: xs) = elemSymmList 1 xs + (a + b) := by
            simp only [elemSymmList_cons_succ, elemSymmList_zero, mul_one]
            abel
          rw [hexp, mul_add, add_mul, h1, hsum]
      | succ r =>
          have h2 := comm_elemSymmList_of_forall hxs (r + 2)
          have h1 := comm_elemSymmList_of_forall hxs (r + 1)
          have h0 := comm_elemSymmList_of_forall hxs r
          have hexp : elemSymmList (r + 2) (a :: b :: xs) =
              elemSymmList (r + 2) xs + (a + b) * elemSymmList (r + 1) xs +
                (a * b) * elemSymmList r xs := by
            simp only [elemSymmList_cons_succ]
            noncomm_ring
          rw [hexp]
          calc z * (elemSymmList (r + 2) xs + (a + b) * elemSymmList (r + 1) xs +
                  (a * b) * elemSymmList r xs)
              = z * elemSymmList (r + 2) xs + (z * (a + b)) * elemSymmList (r + 1) xs +
                  (z * (a * b)) * elemSymmList r xs := by noncomm_ring
            _ = elemSymmList (r + 2) xs * z + ((a + b) * z) * elemSymmList (r + 1) xs +
                  ((a * b) * z) * elemSymmList r xs := by rw [h2, hsum, hprod]
            _ = elemSymmList (r + 2) xs * z + (a + b) * (z * elemSymmList (r + 1) xs) +
                  (a * b) * (z * elemSymmList r xs) := by noncomm_ring
            _ = elemSymmList (r + 2) xs * z + (a + b) * (elemSymmList (r + 1) xs * z) +
                  (a * b) * (elemSymmList r xs * z) := by rw [h1, h0]
            _ = (elemSymmList (r + 2) xs + (a + b) * elemSymmList (r + 1) xs +
                  (a * b) * elemSymmList r xs) * z := by noncomm_ring

/-- The `k`-th elementary symmetric Jucys–Murphy central element `e_k(L₀, …, L_{n−1})` in `H_n(q)`. -/
def elemSymmJM {h : R} (H : HeckeRingGen R A h) (n k : ℕ) : A :=
  elemSymmList k ((List.range n).map (jmRing H))

theorem range_add_shift (a : ℕ) :
    ∀ b : ℕ, List.range (a + b) = List.range a ++ (List.range b).map (fun d => a + d) := by
  intro b
  induction b with
  | zero => simp
  | succ s ih =>
      rw [Nat.add_succ, List.range_succ, List.range_succ, List.map_append, List.map_singleton,
        ih, List.append_assoc]

/-- Decomposition of `List.range n` around an adjacent pair `(i, i + 1)` when `i + 1 < n`. -/
theorem range_split_pair {n i : ℕ} (hi : i + 1 < n) :
    List.range n =
      List.range i ++ [i, i + 1] ++ (List.range (n - (i + 2))).map (fun d => i + 2 + d) := by
  have hn : n = (i + 2) + (n - (i + 2)) := by omega
  have hi2 : List.range (i + 2) = List.range i ++ [i, i + 1] := by
    rw [Nat.add_succ, List.range_succ, List.range_succ, List.append_assoc]
    rfl
  conv_lhs => rw [hn]
  rw [range_add_shift (i + 2) (n - (i + 2)), hi2]

/-- **Main Symmetric Center Theorem (`[CommRing R]`):** for every `n, k : ℕ` and every generator
`σᵢ` of `H_n(q)` (`i + 1 < n`), `σᵢ` commutes with `e_k(L₀, …, L_{n−1})`. -/
theorem sigma_comm_elemSymmJM {h : R} (H : HeckeRingGen R A h) {n i : ℕ}
    (hi : i + 1 < n) (k : ℕ) :
    H.σ i * elemSymmJM H n k = elemSymmJM H n k * H.σ i := by
  unfold elemSymmJM
  rw [range_split_pair hi]
  simp only [List.map_append, List.map_cons, List.map_map, List.append_assoc,
    List.cons_append, List.nil_append]
  set pref := (List.range i).map (jmRing H)
  set suff := (List.range (n - (i + 2))).map (jmRing H ∘ fun d => i + 2 + d)
  have hpull1 : elemSymmList k (pref ++ jmRing H i :: jmRing H (i + 1) :: suff) =
      elemSymmList k (jmRing H i :: (pref ++ jmRing H (i + 1) :: suff)) := by
    apply elemSymmList_pull_front
    intro u hu
    rcases List.mem_map.mp hu with ⟨j, _, rfl⟩
    exact jmMon_comm H.toBraidMonoidGen j i
  have hpull2 : elemSymmList k (jmRing H i :: (pref ++ jmRing H (i + 1) :: suff)) =
      elemSymmList k (jmRing H i :: jmRing H (i + 1) :: (pref ++ suff)) := by
    cases k with
    | zero => simp
    | succ m =>
        have hp : ∀ r, elemSymmList r (pref ++ jmRing H (i + 1) :: suff) =
            elemSymmList r (jmRing H (i + 1) :: (pref ++ suff)) := by
          intro r
          apply elemSymmList_pull_front
          intro u hu
          rcases List.mem_map.mp hu with ⟨j, _, rfl⟩
          exact jmMon_comm H.toBraidMonoidGen j (i + 1)
        rw [elemSymmList_cons_succ m (jmRing H i) (pref ++ jmRing H (i + 1) :: suff),
          elemSymmList_cons_succ m (jmRing H i) (jmRing H (i + 1) :: (pref ++ suff)),
          hp (m + 1), hp m]
  rw [hpull1, hpull2]
  apply comm_elemSymmList_pair_head (sigma_comm_jmRing_add H i) (sigma_comm_jmRing_prod H i)
  intro x hx
  rcases List.mem_append.mp hx with hpref | hsuff
  · rcases List.mem_map.mp hpref with ⟨j, hj, rfl⟩
    exact jmMon_comm_sigma_above H.toBraidMonoidGen j i (List.mem_range.mp hj)
  · rcases List.mem_map.mp hsuff with ⟨d, _, rfl⟩
    simp only [Function.comp_apply]
    exact sigma_comm_jmMon_below H.toBraidMonoidGen (i + 2 + d) i (by omega)

end SymmetricCenter

/-! ## §3. Constructive Trivial & Sign Character Models over `[CommRing R]` (`q : Rˣ`) -/

section CharacterModels

variable {R : Type*} [CommRing R]

/-- The one-row trivial Hecke model `σᵢ ↦ q` over `[CommRing R]` (`q : Rˣ`), satisfying
`σᵢ² = (q − q⁻¹)σᵢ + 1`. -/
def trivialHeckeModel (q : Rˣ) : HeckeRingGen R R ((q : R) - ((q⁻¹ : Rˣ) : R)) where
  σ := fun _ => (q : R)
  braid := fun _ => by ring
  far := fun _ _ _ => by ring
  hecke := fun _ => by
    have hq : (q : R) * ((q⁻¹ : Rˣ) : R) = 1 := Units.mul_inv q
    simp only [Algebra.id.smul_eq_mul]
    calc (q : R) * (q : R)
        = ((q : R) - ((q⁻¹ : Rˣ) : R)) * (q : R) + (q : R) * ((q⁻¹ : Rˣ) : R) := by ring
      _ = ((q : R) - ((q⁻¹ : Rˣ) : R)) * (q : R) + 1 := by rw [hq]

/-- The one-column sign Hecke model `σᵢ ↦ -q⁻¹` over `[CommRing R]` (`q : Rˣ`), also satisfying
`σᵢ² = (q − q⁻¹)σᵢ + 1`. -/
def signHeckeModel (q : Rˣ) : HeckeRingGen R R ((q : R) - ((q⁻¹ : Rˣ) : R)) where
  σ := fun _ => -((q⁻¹ : Rˣ) : R)
  braid := fun _ => by ring
  far := fun _ _ _ => by ring
  hecke := fun _ => by
    have hq : (q : R) * ((q⁻¹ : Rˣ) : R) = 1 := Units.mul_inv q
    simp only [Algebra.id.smul_eq_mul]
    calc (-((q⁻¹ : Rˣ) : R)) * (-((q⁻¹ : Rˣ) : R))
        = ((q : R) - ((q⁻¹ : Rˣ) : R)) * (-((q⁻¹ : Rˣ) : R)) +
            (q : R) * ((q⁻¹ : Rˣ) : R) := by ring
      _ = ((q : R) - ((q⁻¹ : Rˣ) : R)) * (-((q⁻¹ : Rˣ) : R)) + 1 := by rw [hq]

/-- On the trivial `[n]` representation (`σᵢ ↦ q`), `jmRing` acts by `q^{2k}` (exact content
eigenvalue `q^{2 c(0, k)}` without any `q⁻¹` rescaling). -/
theorem jmRing_trivialHeckeModel (q : Rˣ) (k : ℕ) :
    jmRing (trivialHeckeModel q) k = (q : R) ^ (2 * k) := by
  induction k with
  | zero => simp [jmRing]
  | succ m ih =>
      rw [jmRing, jmMon_succ, ← jmRing, ih]
      simp only [trivialHeckeModel]
      have hexp : 2 * (m + 1) = 2 * m + 2 := by omega
      rw [hexp]
      ring

/-- On the sign `[1ⁿ]` representation (`σᵢ ↦ -q⁻¹`), `jmRing` acts by `(q⁻¹)^{2k}`
(exact content eigenvalue `q^{2 c(k, 0)}`). -/
theorem jmRing_signHeckeModel (q : Rˣ) (k : ℕ) :
    jmRing (signHeckeModel q) k = (((q⁻¹ : Rˣ) : R)) ^ (2 * k) := by
  induction k with
  | zero => simp [jmRing]
  | succ m ih =>
      rw [jmRing, jmMon_succ, ← jmRing, ih]
      simp only [signHeckeModel]
      have hexp : 2 * (m + 1) = 2 * m + 2 := by omega
      rw [hexp]
      ring

end CharacterModels

/-! ## §4. Direct Discharge on `QOU.BraidKnot.Hecke.HeckeGenerators` (Bean `qou-u9o1`) -/

section BridgeToHeckeGenerators

open QOU.BraidKnot.Hecke

variable {K : Type*} [Field K] {A : Type*} [Ring A] [Algebra K A] {q : K}

/-- Canonical forgetful view of `H : HeckeGenerators K A q` as a `[CommRing]` `HeckeRingGen`. -/
def toHeckeRingGen (H : HeckeGenerators K A q) : HeckeRingGen K A (q - q⁻¹) where
  σ := H.σ
  braid := H.braid
  far := H.far
  hecke := fun i => by rw [H.hecke i, Algebra.smul_def]

@[simp] theorem jmRing_toHeckeRingGen_eq_jmRaw (H : HeckeGenerators K A q) (k : ℕ) :
    jmRing (toHeckeRingGen H) k = jmRaw H k := by
  induction k with
  | zero => rfl
  | succ m ih =>
      rw [jmRing, jmMon_succ, ← jmRing, ih, jmRaw_succ]
      rfl

/-- **Discharges `qou-u9o1` (below-commutation on `HeckeGenerators`):** `σ_k` commutes with
`jmRaw H m` whenever `k + 2 ≤ m`. -/
theorem sigma_comm_jmRaw_below (H : HeckeGenerators K A q) {m k : ℕ} (hk : k + 2 ≤ m) :
    H.σ k * jmRaw H m = jmRaw H m * H.σ k := by
  simpa using sigma_comm_jmMon_below (toHeckeRingGen H).toBraidMonoidGen m k hk

/-- **Discharges `qou-u9o1` (general JM commutativity on `HeckeGenerators`):**
`jmRaw H a * jmRaw H b = jmRaw H b * jmRaw H a` for **all** `a, b : ℕ`. -/
theorem jmRaw_comm (H : HeckeGenerators K A q) (a b : ℕ) :
    jmRaw H a * jmRaw H b = jmRaw H b * jmRaw H a := by
  simpa using jmMon_comm (toHeckeRingGen H).toBraidMonoidGen a b

/-- **Discharges `qou-u9o1` (`σᵢ` commutes with adjacent `jmRaw` product).** -/
theorem sigma_comm_jmRaw_prod (H : HeckeGenerators K A q) (i : ℕ) :
    H.σ i * (jmRaw H i * jmRaw H (i + 1)) = (jmRaw H i * jmRaw H (i + 1)) * H.σ i := by
  simpa using sigma_comm_jmRing_prod (toHeckeRingGen H) i

/-- **Discharges `qou-u9o1` (centrality of all `e_k(L₀, …, L_{n−1})` on `HeckeGenerators`).** -/
theorem sigma_comm_elemSymm_jmRaw (H : HeckeGenerators K A q) {n i : ℕ}
    (hi : i + 1 < n) (k : ℕ) :
    H.σ i * elemSymmList k ((List.range n).map (jmRaw H)) =
      elemSymmList k ((List.range n).map (jmRaw H)) * H.σ i := by
  have hmap : (List.range n).map (jmRaw H) = (List.range n).map (jmRing (toHeckeRingGen H)) := by
    apply List.map_congr_left
    intro m _; exact (jmRing_toHeckeRingGen_eq_jmRaw H m).symm
  rw [hmap]
  exact sigma_comm_elemSymmJM (toHeckeRingGen H) hi k

/-- **Discharges `qou-u9o1` (general `n` full-twist factorization on `HeckeGenerators`).** -/
theorem jmRaw_prod_eq_fullTwist (H : HeckeGenerators K A q) (n : ℕ) :
    jmMonProd (toHeckeRingGen H).toBraidMonoidGen n =
      fullTwistMon (toHeckeRingGen H).toBraidMonoidGen n :=
  jmMon_prod_eq_fullTwist (toHeckeRingGen H).toBraidMonoidGen n

/-- **Exact normalisation bridge for all `k : ℕ`:** `jm H k = (q⁻¹)^k • jmRaw H k`. -/
theorem jm_eq_pow_smul_jmRaw (H : HeckeGenerators K A q) (k : ℕ) :
    jm H k = (q⁻¹) ^ k • jmRaw H k := by
  induction k with
  | zero => simp [jmRaw_zero]
  | succ m ih =>
      rw [jm_succ, ih, jmRaw_succ, mul_smul_comm, smul_mul_assoc, smul_smul, pow_succ']

end BridgeToHeckeGenerators

end QOU.BraidKnot.HeckeSymmetricCenter
