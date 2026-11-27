import HeckeTemperleyLieb.TemperleyLiebMarkovNondegenerate
import QOU.Observations.QCltCut

/-!
# The second moment of the centred generator sum under any Markov trace

Bean `qou-e1uf`, first step of the classical CLT for `tr_M` (owner pick 2026-11-27:
the cumulant route).

Fix a Markov trace `T` on the Temperley–Lieb tower (`MarkovTower δ ε`: `τ_0(1) = 1`,
compatible with the inclusions, tracial, and `τ(ι(x)·e_last) = ε·τ(x)`). On level `n`
let `X_i = e_i − ε` be the centred generators and `S_n = Σ_i X_i`.

* `tau_one`, `tau_e`: `τ_n(1) = 1` and `τ_n(e_i) = ε` for every generator.
* `tau_e_mul_e`: `τ_n(e_i e_j) = ε²` for `i ≠ j`, adjacent or not. This is where the
  Markov property does the work: it kills every off-diagonal covariance.
* `tau_X_mul_X`: hence `τ(X_i X_j) = 0` for `i ≠ j` and `τ(X_i²) = δε − ε²`.
* `tau_S_sq`: **`τ_n(S_n²) = n·(δε − ε²)` exactly**, for every `n`.
* `secondMoment_converges`: the normalised second moment `τ_n(S_n²)/n` converges (it is
  constant from `n = 1`) to the variance `v = δε − ε²`. At `ε = δ⁻¹` this is `1 − δ⁻²`.

This is the `k = 1` field of `QCltCut` for a Markov trace, with no hypothesis on `q`
(the second q-Gaussian moment is `1` for every `q`). The `k ≥ 2` fields are not proved
here; they need the locality (cluster factorisation) of the spin-chain state and,
because their corrections are `O(1/n)`, an Archimedean `K`.

No empirical input.
-/

namespace QOU.Observations.QCltMarkovSecondMoment

open QOU.MathlibExt.TemperleyLieb QOU.MathlibExt.TemperleyLiebMarkov
open QOU.Core.CutLimit

variable {K : Type*} [Field K] {δ ε : K} (T : MarkovTower δ ε)

/-- The generator `e_i` on level `n`. -/
noncomputable abbrev gen {n : ℕ} (i : Fin n) : TLFin K δ n := e K δ adjFin i

theorem tau_one : ∀ n, T.τ n 1 = 1
  | 0 => T.tr_one
  | n + 1 => by rw [← map_one (incl δ n), T.tr_incl, tau_one n]

theorem tau_e : ∀ {n : ℕ} (i : Fin n), T.τ n (gen (δ := δ) i) = ε
  | 0, i => i.elim0
  | n + 1, i => by
    induction i using Fin.lastCases with
    | last =>
      have := T.tr_markov n 1
      rwa [map_one, one_mul, tau_one, mul_one] at this
    | cast i =>
      rw [gen, ← incl_e, T.tr_incl]
      exact tau_e i

theorem tau_e_mul_e : ∀ {n : ℕ} (i j : Fin n), i ≠ j →
    T.τ n (gen (δ := δ) i * gen j) = ε ^ 2
  | 0, i, _, _ => i.elim0
  | n + 1, i, j, hij => by
    induction j using Fin.lastCases with
    | last =>
      induction i using Fin.lastCases with
      | last => exact absurd rfl hij
      | cast i =>
        have := T.tr_markov n (gen i)
        rw [incl_e, tau_e] at this
        rw [this, sq]
    | cast j =>
      induction i using Fin.lastCases with
      | last =>
        have := T.tr_markov n (gen j)
        rw [incl_e, tau_e] at this
        rw [T.tr_comm, this, sq]
      | cast i =>
        rw [gen, gen, ← incl_e, ← incl_e, ← map_mul, T.tr_incl]
        exact tau_e_mul_e i j (fun h => hij (by rw [h]))

/-- The centred generator `X_i = e_i − ε`. -/
noncomputable def X (ε : K) {n : ℕ} (i : Fin n) : TLFin K δ n := gen i - algebraMap K _ ε

/-- The centred generator sum `S_n = Σ_i X_i`. -/
noncomputable def S (ε : K) (n : ℕ) : TLFin K δ n := ∑ i, X (δ := δ) ε i

theorem tau_X_mul_X {n : ℕ} (i j : Fin n) :
    T.τ n (X (δ := δ) ε i * X ε j) = if i = j then δ * ε - ε ^ 2 else 0 := by
  have hexp : X (δ := δ) ε i * X ε j =
      gen i * gen j - ε • gen i - ε • gen j + (ε ^ 2) • (1 : TLFin K δ n) := by
    simp only [X, Algebra.algebraMap_eq_smul_one, sub_mul, mul_sub, smul_mul_assoc,
      mul_smul_comm, one_mul, mul_one, smul_sub, smul_smul, sq]
    abel
  rw [hexp, map_add, map_sub, map_sub, map_smul, map_smul, map_smul, tau_e, tau_e, tau_one]
  simp only [smul_eq_mul]
  split_ifs with h
  · subst h
    rw [gen, e_sq', map_smul, tau_e, smul_eq_mul]; ring
  · rw [tau_e_mul_e T i j h]; ring

/-- **Exact second moment:** `τ_n(S_n²) = n·(δε − ε²)`. -/
theorem tau_S_sq (n : ℕ) :
    T.τ n (S (δ := δ) ε n * S ε n) = n * (δ * ε - ε ^ 2) := by
  simp only [S, Finset.sum_mul, Finset.mul_sum, map_sum, tau_X_mul_X T]
  simp; ring

/-- The normalised second moment `τ_n(S_n²)/n`. -/
noncomputable def secondMoment (n : ℕ) : K := T.τ n (S (δ := δ) ε n * S ε n) / n

theorem secondMoment_eq {n : ℕ} (hn : (n : K) ≠ 0) :
    secondMoment T n = δ * ε - ε ^ 2 := by
  rw [secondMoment, tau_S_sq]; field_simp

/-- In characteristic zero the normalised second moment converges to `δε − ε²`. -/
theorem secondMoment_converges [LinearOrder K] [IsStrictOrderedRing K] :
    ConvergesTo (secondMoment T) (δ * ε - ε ^ 2) := by
  apply convergesTo_of_tendstoEps
  intro η hη
  refine ⟨1, fun n hn => ?_⟩
  rw [secondMoment_eq T (by exact_mod_cast (show n ≠ 0 by omega)), sub_self, abs_zero]
  exact hη

end QOU.Observations.QCltMarkovSecondMoment
