/-
# Roth's Lemma without the ladder restriction

⚠⚠ **This module closes correction twenty-three.**

`RothVariableSplit.rothLemmaTheta_of_seq` needed a rational sequence `s` with `s 0 = t` and
`s (n+1)² = s n`, which exists only when `t` is a `2^{M−1}`-th power in `ℚ`.  That restriction
is an artifact of the **root-free encoding**, not of §14 — `RothBound` states
`θ ≤ c_m·t^{2^{−(m−1)}}` as `θ^{2^{m−1}} ≤ c_m^{2^{m−1}}·t` precisely so that no root has to
exist in `ℚ`, and §14's *argument* then needs the root anyway at every intermediate step.

⚠ **A root-free reformulation of the argument does not work**, and it is worth saying why
rather than leaving it as a hope.  Running the step on powers directly needs
`(a+b)^K ≤ 2^{K−1}(a^K + b^K)`, which turns `Θ ≤ 2Θ_n + 3t` into
`Θ^K ≤ 2^{K−1}(2^K c_n^K + 3^K)·t` where `K = 2^n`.  Against the target `(2c_n+3)^K` that is
short by a factor `≈ 2^{K−1}` once `c_n` is large — and `c_n = 2^{n+1}−3` is large.  The root is
not a convenience; it is what keeps the constant from compounding.

So the fix is to take the root where roots exist.  `ℝ` supplies it as an iterated `Real.sqrt`,
`rothConstant_step_lemma4` was already field-generic (it is stated for any
`[Field K] [LinearOrder K] [IsStrictOrderedRing K]`), and both endpoints of the step are
rational, so the excursion is invisible in the statement.

⚠ Not Mathlib-only: imports `QOU/Mathlib/RothVariableSplit.lean` and, for `Real.sqrt`,
`Mathlib/RingTheory/Real/Irrational.lean`.
-/
import QOU.Mathlib.RothVariableSplit
import Mathlib.RingTheory.Real.Irrational

namespace MvPolynomial

/-! ### The `2^n`-th root, as an iterated square root

`Real.rpow` would do this in one line, but it is not in this project's built Mathlib closure and
would be a much larger dependency.  `Real.sqrt^[n]` is enough: the exponent this argument needs
is always a power of two. -/


theorem sqrtIter_nonneg (n : ℕ) {x : ℝ} (hx : 0 ≤ x) : 0 ≤ Real.sqrt^[n] x := by
  induction n generalizing x with
  | zero => simpa using hx
  | succ k ih => rw [Function.iterate_succ_apply]; exact ih (Real.sqrt_nonneg x)

theorem sqrtIter_le_one (n : ℕ) {x : ℝ} (hx0 : 0 ≤ x) (hx1 : x ≤ 1) :
    Real.sqrt^[n] x ≤ 1 := by
  induction n generalizing x with
  | zero => simpa using hx1
  | succ k ih =>
      rw [Function.iterate_succ_apply]
      refine ih (Real.sqrt_nonneg x) ?_
      rw [show (1:ℝ) = Real.sqrt 1 by simp]
      exact Real.sqrt_le_sqrt hx1

theorem sqrtIter_pow (n : ℕ) {x : ℝ} (hx : 0 ≤ x) : (Real.sqrt^[n] x) ^ (2 ^ n) = x := by
  induction n generalizing x with
  | zero => simp
  | succ k ih =>
      rw [Function.iterate_succ_apply, show (2:ℕ) ^ (k + 1) = 2 ^ k * 2 by ring, pow_mul,
        ih (Real.sqrt_nonneg x), Real.sq_sqrt hx]

theorem rothBound_succ_of_lemma4' {n : ℕ} (hn : 1 ≤ n) {t Θ Θ' w : ℚ}
    (ht0 : 0 ≤ t) (ht1 : t ≤ 1) (hΘ0 : 0 ≤ Θ)
    (hsub : RothBound n t Θ')
    (hw : w ≤ Θ' + t ∨ w ^ 2 ≤ Θ' + t)
    (hΘ : Θ ≤ t + 2 * w) :
    RothBound (n + 1) t Θ := by
  obtain ⟨hΘ'0, hsub'⟩ := hsub
  have htR : (0:ℝ) ≤ (t : ℝ) := by exact_mod_cast ht0
  set u : ℝ := Real.sqrt^[n] (t : ℝ) with hudef
  have hu0 : 0 ≤ u := sqrtIter_nonneg n htR
  have hu1 : u ≤ 1 := sqrtIter_le_one n htR (by exact_mod_cast ht1)
  have hupow : u ^ (2 ^ n) = (t : ℝ) := sqrtIter_pow n htR
  have hsplit : (2 : ℕ) ^ n = 2 ^ (n - 1) * 2 := by
    conv_lhs => rw [show n = (n - 1) + 1 by omega]
    rw [pow_succ]
  have husq : (u ^ 2) ^ (2 ^ (n - 1)) = (t : ℝ) := by
    rw [← pow_mul, mul_comm, ← hsplit, hupow]
  -- the induction hypothesis, de-powered
  have hsubR : ((Θ' : ℝ)) ^ (2 ^ (n - 1))
      ≤ ((rothConstant n : ℝ) * u ^ 2) ^ (2 ^ (n - 1)) := by
    rw [mul_pow, husq]
    exact_mod_cast hsub'
  have hΘ'le : (Θ' : ℝ) ≤ (rothConstant n : ℝ) * u ^ 2 := by
    refine le_of_pow_le_pow_left₀ (by positivity) ?_ hsubR
    exact mul_nonneg (by positivity) (by positivity)
  -- `t ≤ u²` and `t ≤ u`
  have h2le : (2 : ℕ) ≤ 2 ^ n := by
    calc (2:ℕ) = 2 ^ 1 := by norm_num
      _ ≤ 2 ^ n := Nat.pow_le_pow_right (by norm_num) hn
  have htu2 : (t : ℝ) ≤ u ^ 2 := by rw [← hupow]; exact pow_le_pow_of_le_one hu0 hu1 h2le
  have hu2u : u ^ 2 ≤ u := by nlinarith
  -- the step
  have hΨ : (Θ' : ℝ) + (t : ℝ) ≤ ((rothConstant n : ℝ) + 1) * u ^ 2 := by nlinarith
  have hwR : (w : ℝ) ≤ (Θ' : ℝ) + (t : ℝ) ∨ (w : ℝ) ^ 2 ≤ (Θ' : ℝ) + (t : ℝ) := by
    rcases hw with h | h
    · exact Or.inl (by exact_mod_cast h)
    · exact Or.inr (by exact_mod_cast h)
  have hθR : (Θ : ℝ) ≤ u + 2 * (w : ℝ) := by
    have : (Θ : ℝ) ≤ (t : ℝ) + 2 * (w : ℝ) := by exact_mod_cast hΘ
    linarith
  have hstep := rothConstant_step_lemma4 (K := ℝ) hn hu0 hu1 hΨ hwR hθR
  -- back to `RothBound`
  refine ⟨hΘ0, ?_⟩
  have hfin : ((Θ : ℝ)) ^ (2 ^ n) ≤ ((rothConstant (n + 1) : ℝ)) ^ (2 ^ n) * (t : ℝ) := by
    calc ((Θ : ℝ)) ^ (2 ^ n)
        ≤ ((rothConstant (n + 1) : ℝ) * u) ^ (2 ^ n) :=
          pow_le_pow_left₀ (by exact_mod_cast hΘ0) hstep _
      _ = ((rothConstant (n + 1) : ℝ)) ^ (2 ^ n) * (t : ℝ) := by rw [mul_pow, hupow]
  have hexp : (n + 1) - 1 = n := by omega
  rw [hexp]
  exact_mod_cast hfin

theorem rothLemmaTheta_succ' {σ : Type*} {n p q F : ℕ} (hn : 1 ≤ n)
    (h4 : RothLemma4 σ n p q F) (hIH : RothLemmaTheta (Fin n) n p q F) :
    RothLemmaTheta σ (n + 1) p q F := by
  intro hp hpq o a r H Θ hg hΘ
  obtain ⟨b, ρ, H', Θ', w, hg', hΘ', hw, hle⟩ := h4 hp hpq o a r H Θ hg hΘ
  have hsub : RothBound n ((p : ℚ) / (q : ℚ)) Θ' :=
    hIH hp hpq (Equiv.refl (Fin n)) b ρ H' Θ' hg' hΘ'
  have hpQ : (0:ℚ) < (p:ℚ) := by exact_mod_cast hp
  have hqQ : (0:ℚ) < (q:ℚ) := by exact_mod_cast lt_of_lt_of_le hp hpq
  refine rothBound_succ_of_lemma4' hn (le_of_lt (div_pos hpQ hqQ)) ?_ hΘ.nonneg hsub hw hle
  rw [div_le_one hqQ]; exact_mod_cast hpq

theorem rothLemmaTheta_all {p q F : ℕ} : ∀ m, 1 ≤ m → RothLemmaTheta (Fin m) m p q F := by
  intro m hm
  induction m, hm using Nat.le_induction with
  | base => exact rothLemmaTheta_one_fin
  | succ n hn ih => exact rothLemmaTheta_succ' hn (rothLemma4_of_one_le hn) ih

/-! ### Roth's Lemma, stated on the index directly

`RothLemmaTheta` speaks of `Θ_m`; this says what that means for a polynomial and a point. -/

/-- **Roth's Lemma (§14).**  If `a; r₁,…,r_m; H₁,…,H_m` has property `Γ_m` with `t = p/q`, then
every `A ∈ R(a;r)` has index at most `c_m·t^{2^{−(m−1)}}` at every `κ ∈ Q(H)`, where
`c_m = 2^{m+1} − 3`.

The conclusion is root-free: `Θ^{2^{m−1}} ≤ c_m^{2^{m−1}}·t`.  ⚠ `Θ` is existential because it
is `Θ_m` — the bound is uniform over `R(a;r) × Q(H)`, which is stronger than a bound depending
on `A` and `κ`, and is what §12 invokes when it recurses. -/
theorem index_le_rothBound {σ : Type*} {m : ℕ} (hm : 1 ≤ m) {p q F : ℕ}
    (hp : 0 < p) (hpq : p ≤ q) (o : σ ≃ Fin m) {a : ℤ} {r H : σ → ℕ}
    (hg : RothGammaFull o p q F r (fun j => (H j : ℤ)) a)
    {A : MvPolynomial σ ℤ} {κ : σ → ℚ}
    (hA : InRothPolySet a r A) (hκ : InRothFracSet H κ) :
    ∃ Θ : ℚ, 0 ≤ Θ ∧
      Θ ^ (2 ^ (m - 1)) ≤ (rothConstant m : ℚ) ^ (2 ^ (m - 1)) * ((p : ℚ) / (q : ℚ)) ∧
      index r κ (map (algebraMap ℤ ℚ) A) ≤ ((Θ : ℚ) : WithTop ℚ) := by
  classical
  haveI : Fintype σ := Fintype.ofEquiv _ o.symm
  have ha1 : 1 ≤ a := by
    obtain ⟨m0, hm0⟩ := support_nonempty.mpr hA.1
    exact le_trans (Int.one_le_abs (mem_support_iff.mp hm0)) (hA.2.2 m0)
  have hH1 : ∀ j, 1 ≤ H j := by
    intro j
    have h2 : (2 : ℤ) ≤ (H j : ℤ) := hg.two_le j
    omega
  obtain ⟨Θ, hΘ⟩ := exists_isRothTheta a r H ha1 hH1
  obtain ⟨h0, hb⟩ :=
    RothLemmaTheta.rename_equiv o (rothLemmaTheta_all m hm) hp hpq o a r H Θ hg hΘ
  exact ⟨Θ, h0, hb, hΘ.1 A κ hA hκ⟩

/-- **Non-vacuity of Roth's Lemma at `m = 2`** — the arity §13 actually needs (`m ≥ 2`).

`p = q = 1` (so `t = 1`), `F = 10`, `d ≡ 1`, `H ≡ 1024`, `a = 1`, `A = 1`, `κ ≡ 1024`.

⚠ The heights **cannot** be small.  Clause 3 forces `2^F ≤ K₁` with `q·(m−1)m(2m+1) ≤ F·p`, so
at `m = 2` the floor is `2^{10} = 1024`.  Every other witness in this arc got away with `H = 2`;
this is the one place where clause 3 bites, and exhibiting it is the point — a satisfiability
claim about `Γ_m` that quietly used `H = 2` would be about a different hypothesis.

⚠ `t = 1` makes the bound itself weak (`Θ ≤ c₂ = 5`).  That is a limitation of *this witness*,
not of the theorem: what it establishes is that the hypothesis stack is satisfiable at `m ≥ 2`,
so the theorem is not vacuous where §13 lives. -/
theorem index_le_rothBound_witness :
    ∃ Θ : ℚ, 0 ≤ Θ ∧
      Θ ^ (2 ^ (2 - 1)) ≤ (rothConstant 2 : ℚ) ^ (2 ^ (2 - 1)) * ((1 : ℚ) / (1 : ℚ)) ∧
      index (fun _ : Fin 2 => 1) (fun _ : Fin 2 => (1024 : ℚ))
          (map (algebraMap ℤ ℚ) (1 : MvPolynomial (Fin 2) ℤ)) ≤ ((Θ : ℚ) : WithTop ℚ) :=
  index_le_rothBound (m := 2) (by norm_num) (p := 1) (q := 1) (F := 10) one_pos le_rfl
    (Equiv.refl (Fin 2)) (a := 1) (r := fun _ => 1) (H := fun _ => 1024)
    { growth := by intro j k hjk; norm_num
      height := by intro j k _; exact le_rfl
      floorExp := by norm_num
      floor := by intro j _; norm_num
      heightBound := by intro j _; norm_num
      two_le := fun _ => by norm_num
      degPos := fun _ => one_ne_zero }
    (A := 1) (κ := fun _ => (1024 : ℚ))
    ⟨one_ne_zero, fun h => by rw [← C_1, degreeOf_C]; norm_num, fun n => by
      simp only [coeff_one]; split_ifs <;> norm_num⟩
    (by intro _; norm_num)

end MvPolynomial
