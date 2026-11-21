import QOU.Mass.QuantumSl2Markov
import QOU.Torsion.MassTraceMarkovClass

/-!
# Both Markov moves for the `U_q(sl₂)` quantum trace on `V_{d+1}^{⊗(n+1)}`

Stages 3–5 of issue #8894. Let `ρ_n : B_{n+1} → GL(V^{⊗(n+1)})`, `V = V_{d+1}`, be the
braid action of `QuantumSl2BraidAction`, and let

    τ_n(β) = tr(K^{⊗(n+1)} ρ_n(β)),   K = diag(s^{2 wt(r)}) = q^H, q = s²,

be the quantum trace. Then

* **Markov I** (`wtrace_conj`): `τ_n(xy) = τ_n(yx)`, because `K^{⊗(n+1)}` commutes with every
  `ρ_n(β)` (each `Ř` preserves the total weight).
* **Markov II** (`wtrace_stab`, `wtrace_stabInv`): `τ_{n+1}(β σ_n^{±1}) = θ^{±1} τ_n(β)`,
  `θ = q^{(N²−1)/2}`, from the local partial traces `ptr(Ř^{±1}) = θ^{±1}·1` of
  `QuantumSl2Markov`.

So `τ` is a scaled Markov functional on the Artin tower (`quantumTrace_isScaledMarkov`) and its
writhe normalisation `θ^{−w(β)} τ(β)` is a Markov invariant (`jonesSl2_isMarkovInvariant`).
Dividing by the constant `[N]_q = τ_0(1)` changes nothing, so this is the coloured Jones
functional `J_N`.

The generic part (`Generic` section) works for any weight `c : ι → R` and any weight-conserving
two-site matrix.

-- Ref: [turaev1988] Turaev, "The Yang–Baxter equation and invariants of links"
-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. X.6 and XIV.3
-/

namespace QOU.Mass.QuantumSl2.MarkovTrace

open Matrix
open QOU.Mass.QuantumSl2.BraidAction
open QOU.IwahoriHecke.TensorEmbed (coxA coxA_symm)
open QOU.IwahoriHecke.BraidGroup (BraidGroupN braidGen)

set_option linter.unusedSectionVars false

section Generic

variable {R : Type*} [CommRing R] {ι : Type*} [Fintype ι] [DecidableEq ι] (c : ι → R)

/-- The product weight `∏_k c(a_k)` of a basis vector of `ι^{⊗n}`. -/
def siteWt {n : ℕ} (a : Fin n → ι) : R := ∏ k, c (a k)

/-- The weighted trace `tr(K^{⊗n} A) = Σ_a (∏_k c(a_k)) A_{aa}`. -/
def wtrace {n : ℕ} (A : Matrix (Fin n → ι) (Fin n → ι) R) : R := ∑ a, siteWt c a * A a a

theorem wtrace_eq_trace {n : ℕ} (A : Matrix (Fin n → ι) (Fin n → ι) R) :
    wtrace c A = trace (diagonal (siteWt c) * A) := by
  simp [wtrace, trace, diagonal_mul]

/-- A two-site matrix `M` conserves the weight `c`. -/
def Conserves (M : Matrix (ι × ι) (ι × ι) R) : Prop :=
  ∀ x y, M x y ≠ 0 → c x.1 * c x.2 = c y.1 * c y.2

theorem siteWt_eq_of_pembed {n : ℕ} {i j : Fin n} (hij : i ≠ j)
    {M : Matrix (ι × ι) (ι × ι) R} (hM : Conserves c M) (a b : Fin n → ι)
    (h : pembed i j M a b ≠ 0) : siteWt c a = siteWt c b := by
  rw [pembed_apply] at h
  split_ifs at h with hab
  swap; · exact absurd rfl h
  have hw := hM _ _ h
  have hj : j ∈ (Finset.univ : Finset (Fin n)).erase i :=
    Finset.mem_erase.2 ⟨hij.symm, Finset.mem_univ j⟩
  unfold siteWt
  rw [← Finset.mul_prod_erase _ _ (Finset.mem_univ i), ← Finset.mul_prod_erase _ _ hj,
    ← Finset.mul_prod_erase _ (fun k => c (b k)) (Finset.mem_univ i),
    ← Finset.mul_prod_erase _ (fun k => c (b k)) hj, ← mul_assoc, ← mul_assoc]
  simp only at hw
  rw [hw]
  congr 1
  refine Finset.prod_congr rfl fun k hk => ?_
  obtain ⟨hkj, hk'⟩ := Finset.mem_erase.1 hk
  rw [hab k (Finset.mem_erase.1 hk').1 hkj]

/-- `K^{⊗n}` commutes with a weight-conserving matrix on two sites. -/
theorem commute_diag_pembed {n : ℕ} {i j : Fin n} (hij : i ≠ j)
    {M : Matrix (ι × ι) (ι × ι) R} (hM : Conserves c M) :
    Commute (diagonal (siteWt c)) (pembed i j M) := by
  ext a b
  rw [diagonal_mul, mul_diagonal]
  by_cases h : pembed i j M a b = 0
  · simp [h]
  · rw [siteWt_eq_of_pembed c hij hM a b h, mul_comm]

/-- **Markov I, abstractly.** If `K^{⊗n}` commutes with `A`, the weighted trace is cyclic on
`A, B`. -/
theorem wtrace_mul_comm {n : ℕ} {A B : Matrix (Fin n → ι) (Fin n → ι) R}
    (hA : Commute (diagonal (siteWt c)) A) : wtrace c (A * B) = wtrace c (B * A) := by
  rw [wtrace_eq_trace, wtrace_eq_trace, ← mul_assoc, hA.eq, mul_assoc, trace_mul_comm,
    mul_assoc]

/-! ### Adding a strand on the right -/

/-- Sum over `ι^{⊗(n+1)}` as a sum over the first `n` sites and the last one. -/
theorem sum_snoc {n : ℕ} (F : (Fin (n + 1) → ι) → R) :
    ∑ a, F a = ∑ u : Fin n → ι, ∑ r : ι, F (Fin.snoc u r) := by
  rw [← (Fin.snocEquiv fun _ => ι).sum_comp, Fintype.sum_prod_type, Finset.sum_comm]
  rfl

theorem siteWt_snoc {n : ℕ} (u : Fin n → ι) (r : ι) :
    siteWt c (Fin.snoc u r : Fin (n + 1) → ι) = siteWt c u * c r := by
  simp [siteWt, Fin.prod_univ_castSucc]

/-- `A ⊗ 1`: `A` on the first `n` sites, the identity on a new last site. -/
def extLast {n : ℕ} (A : Matrix (Fin n → ι) (Fin n → ι) R) :
    Matrix (Fin (n + 1) → ι) (Fin (n + 1) → ι) R :=
  Matrix.of fun a b => if a (Fin.last n) = b (Fin.last n) then A (Fin.init a) (Fin.init b) else 0

theorem extLast_snoc {n : ℕ} (A : Matrix (Fin n → ι) (Fin n → ι) R) (u v : Fin n → ι)
    (r r' : ι) :
    extLast A (Fin.snoc u r) (Fin.snoc v r') = if r = r' then A u v else 0 := by
  simp [extLast, Fin.init_snoc, Fin.snoc_last]

theorem extLast_one {n : ℕ} : extLast (1 : Matrix (Fin n → ι) (Fin n → ι) R) = 1 := by
  ext a b
  rw [← Fin.snoc_init_self a, ← Fin.snoc_init_self b, extLast_snoc, one_apply, one_apply]
  by_cases h1 : a (Fin.last n) = b (Fin.last n)
  · by_cases h2 : Fin.init a = Fin.init b
    · simp [h1, h2]
    · rw [if_pos h1, if_neg h2, if_neg]
      intro h; exact h2 (by simpa using congrArg Fin.init h)
  · rw [if_neg h1, if_neg]
    intro h; exact h1 (by simpa using congrArg (fun f => f (Fin.last n)) h)

theorem extLast_mul {n : ℕ} (A B : Matrix (Fin n → ι) (Fin n → ι) R) :
    extLast (A * B) = extLast A * extLast B := by
  ext a b
  rw [← Fin.snoc_init_self a, ← Fin.snoc_init_self b, extLast_snoc, mul_apply, mul_apply,
    sum_snoc (n := n)]
  simp_rw [extLast_snoc, ite_mul, zero_mul, mul_ite, mul_zero]
  by_cases h : a (Fin.last n) = b (Fin.last n)
  · simp [h]
  · simp only [if_neg h]
    refine (Finset.sum_eq_zero fun u _ => Finset.sum_eq_zero fun r _ => ?_).symm
    split_ifs with h1 h2 <;> first | rfl | exact absurd (h1.trans h2) h

/-- `A ↦ A ⊗ 1` as a monoid homomorphism. -/
def extLastHom (n : ℕ) :
    Matrix (Fin n → ι) (Fin n → ι) R →* Matrix (Fin (n + 1) → ι) (Fin (n + 1) → ι) R where
  toFun := extLast
  map_one' := extLast_one
  map_mul' := extLast_mul

theorem extLast_pembed {n : ℕ} {i j : Fin n} (M : Matrix (ι × ι) (ι × ι) R) :
    extLast (pembed i j M) = pembed i.castSucc j.castSucc M := by
  ext a b
  rw [← Fin.snoc_init_self a, ← Fin.snoc_init_self b, extLast_snoc, pembed_apply, pembed_apply]
  simp only [Fin.snoc_castSucc, Fin.forall_fin_succ', Fin.snoc_last, ne_eq, Fin.castSucc_inj]
  have hi : ¬ Fin.last n = i.castSucc := (Fin.castSucc_ne_last i).symm
  have hj : ¬ Fin.last n = j.castSucc := (Fin.castSucc_ne_last j).symm
  simp only [hi, hj, not_false_eq_true, forall_const]
  by_cases h1 : a (Fin.last n) = b (Fin.last n) <;> simp [h1]

/-- The partial trace of `M` over its second site is `t · 1`. -/
def PtrScalar (M : Matrix (ι × ι) (ι × ι) R) (t : R) : Prop :=
  ∀ x y, ∑ r, c r * M (x, r) (y, r) = if x = y then t else 0

theorem sum_pembed_last {n : ℕ} {M : Matrix (ι × ι) (ι × ι) R} {t : R} (hM : PtrScalar c M t)
    (u v : Fin (n + 1) → ι) :
    ∑ r, c r * pembed (Fin.last n).castSucc (Fin.last (n + 1)) M (Fin.snoc v r) (Fin.snoc u r)
      = if v = u then t else 0 := by
  have key : ∀ r, pembed (Fin.last n).castSucc (Fin.last (n + 1)) M (Fin.snoc v r) (Fin.snoc u r)
      = if (∀ k : Fin (n + 1), k ≠ Fin.last n → v k = u k)
        then M (v (Fin.last n), r) (u (Fin.last n), r) else 0 := by
    intro r
    rw [pembed_apply, Fin.snoc_castSucc, Fin.snoc_castSucc, Fin.snoc_last, Fin.snoc_last]
    have hiff : (∀ k, k ≠ (Fin.last n).castSucc → k ≠ Fin.last (n + 1) →
        Fin.snoc (α := fun _ => ι) v r k = Fin.snoc (α := fun _ => ι) u r k)
        ↔ ∀ k : Fin (n + 1), k ≠ Fin.last n → v k = u k := by
      constructor
      · intro h k hk
        have := h k.castSucc (fun e => hk (Fin.castSucc_inj.1 e)) (Fin.castSucc_ne_last k)
        simpa only [Fin.snoc_castSucc] using this
      · intro h k hk1 hk2
        induction k using Fin.lastCases with
        | last => exact absurd rfl hk2
        | cast k =>
          rw [Fin.snoc_castSucc, Fin.snoc_castSucc]
          exact h k (fun e => hk1 (by rw [e]))
    by_cases hag : ∀ k : Fin (n + 1), k ≠ Fin.last n → v k = u k
    · rw [if_pos (hiff.2 hag), if_pos hag]
    · rw [if_neg (fun h => hag (hiff.1 h)), if_neg hag]
  simp_rw [key, mul_ite, mul_zero]
  by_cases hag : ∀ k : Fin (n + 1), k ≠ Fin.last n → v k = u k
  · simp only [if_pos hag]
    rw [hM]
    by_cases hl : v (Fin.last n) = u (Fin.last n)
    · rw [if_pos hl, if_pos]
      funext k
      by_cases hk : k = Fin.last n
      · subst hk; exact hl
      · exact hag k hk
    · rw [if_neg hl, if_neg]
      rintro rfl; exact hl rfl
  · simp only [if_neg hag, Finset.sum_const_zero]
    rw [if_neg]
    rintro rfl; exact hag fun _ _ => rfl

/-- **Markov II, abstractly.** If the partial trace of `M` over its second site is `t · 1`, then
adding a strand and crossing it with `M` multiplies the weighted trace by `t`. -/
theorem wtrace_extLast_mul_pembed {n : ℕ} (A : Matrix (Fin (n + 1) → ι) (Fin (n + 1) → ι) R)
    {M : Matrix (ι × ι) (ι × ι) R} {t : R} (hM : PtrScalar c M t) :
    wtrace c (extLast A * pembed (Fin.last n).castSucc (Fin.last (n + 1)) M)
      = t * wtrace c A := by
  set P := pembed (Fin.last n).castSucc (Fin.last (n + 1)) M with hP
  have step : ∀ (u : Fin (n + 1) → ι) (r : ι),
      (extLast A * P) (Fin.snoc u r) (Fin.snoc u r) = ∑ v, A u v * P (Fin.snoc v r) (Fin.snoc u r) := by
    intro u r
    rw [mul_apply, sum_snoc]
    refine Finset.sum_congr rfl fun v _ => ?_
    simp_rw [extLast_snoc, ite_mul, zero_mul]
    rw [Finset.sum_ite_eq]
    simp
  unfold wtrace
  rw [sum_snoc]
  simp_rw [siteWt_snoc, step]
  calc ∑ u, ∑ r, siteWt c u * c r * ∑ v, A u v * P (Fin.snoc v r) (Fin.snoc u r)
      = ∑ u, siteWt c u * ∑ v, A u v * ∑ r, c r * P (Fin.snoc v r) (Fin.snoc u r) := by
        refine Finset.sum_congr rfl fun u _ => ?_
        simp_rw [Finset.mul_sum]
        rw [Finset.sum_comm]
        refine Finset.sum_congr rfl fun v _ => Finset.sum_congr rfl fun r _ => ?_
        ring
    _ = ∑ u, siteWt c u * (A u u * t) := by
        refine Finset.sum_congr rfl fun u _ => ?_
        simp_rw [hP, sum_pembed_last c hM, mul_ite, mul_zero]
        rw [Finset.sum_ite_eq']
        simp
    _ = t * ∑ u, siteWt c u * A u u := by
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl fun u _ => ?_
        ring

end Generic

end QOU.Mass.QuantumSl2.MarkovTrace
