/-
# Step 4: the two bounds meet, and the inequality they meet at

Steps 2 and 3 are both proved and both are about the same number — the index of the auxiliary
polynomial at the rational point.  Step 2 (`le_index_rational_of_taylor`) bounds it from **below**
by `ν`; step 3 (`index_le_rothBound`, Roth's Lemma) bounds it from **above** by a `Θ` satisfying
`Θ^{2^{m−1}} ≤ c_m^{2^{m−1}}·(p/q)`.  Roth's theorem is the observation that for the right
parameters those two cannot both hold.  This file performs that collision.

## The interfaces fit — checked, not assumed

Correction 26 was a pair of halves that were each correct and did not compose, so the expectation
going in was that composing steps 2 and 3 would surface mismatches: `algebraMap ℤ ℚ` against
`Int.castRingHom ℚ`, `κ` against `p_h/q_h`, and step 3's `p`, `q` — which are `Γ_m`'s ratio
parameters and have nothing to do with the numerators and denominators of the approximations,
despite the shared letters.

It surfaced none.  `algebraMap ℤ ℚ` and `Int.castRingHom ℚ` unify definitionally, and I verified
that by deleting the rewrite that bridged them and rebuilding: the file still compiles, so
`algebraMap_int_rat` below is a recorded check rather than a load-bearing step.  The `p`,`q`
overloading is a real trap for a reader and was navigated by naming step 2's data `pn`, `qd`, but
nothing about it failed.  The honest report is that the two halves fit as they stood — which is
the good outcome, and worth stating as an outcome rather than dressed up as a discovery.

## The two shapes of the numeric hypothesis

`le_index_rational_of_taylor` takes its last hypothesis in multiplicative form,
`taylorConst · e^{−K(μ−ν)} < ∏_h q_h^{−r_h}`.  That is the form the estimate produces but not the
form anyone reasons in.  `mul_exp_neg_lt_one_div` converts it to

    log(taylorConst) + ∑_h r_h·log q_h  <  K·(μ − ν),

which is Roth's inequality as it is actually stated: the auxiliary polynomial's size and the
denominators' size on the left, the index gap times the approximation exponent on the right.  Both
forms are kept — the multiplicative one is what the estimate hands over, the additive one is what
a parameter choice is checked against.

## Scope

`roth_contradiction` is the collision, with both steps' hypotheses in one list.  It is deliberately
*not* wrapped in a parameter record yet: a record with one consumer is speculative structure, and
this hypothesis list is the specification such a record would have to meet.  The record earns its
place once `RothGammaProducer` is retargeted onto it — tracked on `qou-ujl8`.
-/
import QOU.Mathlib.RothIndexGap
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import QOU.Mathlib.RothRealLadder

namespace MvPolynomial

open Finset

section LogForm

variable {m : ℕ}

/-- The constant `le_index_rational_of_taylor` multiplies `e^{−K(μ−ν)}` by: the box count twice
(once for the support of `P`, once for the support of its translate), the height, and the two
peeling factors. -/
noncomputable def taylorConst (r : Fin m → ℕ) (H B : ℝ) : ℝ :=
  ((∏ h, (r h + 1) : ℕ) : ℝ) * (((∏ h, (r h + 1) : ℕ) : ℝ) * (H * (2 * B) ^ (∑ h, r h)))
    * ((2 : ℝ) ^ (∑ h, r h))

/-- **The additive form of the numeric hypothesis.**  `C·e^{−g} < 1/D` is `log C + log D < g`. -/
theorem mul_exp_neg_lt_one_div {C D g : ℝ} (hC : 0 < C) (hD : 0 < D)
    (h : Real.log C + Real.log D < g) : C * Real.exp (-g) < 1 / D := by
  rw [lt_div_iff₀ hD]
  calc C * Real.exp (-g) * D = (C * D) * Real.exp (-g) := by ring
    _ = Real.exp (Real.log C + Real.log D) * Real.exp (-g) := by
        rw [Real.exp_add, Real.exp_log hC, Real.exp_log hD]
    _ = Real.exp (Real.log C + Real.log D + -g) := (Real.exp_add _ _).symm
    _ < Real.exp 0 := Real.exp_lt_exp.mpr (by linarith)
    _ = 1 := Real.exp_zero

/-- `log ∏_h q_h^{r_h} = ∑_h r_h·log q_h` — the denominators' contribution, in the currency the
normalisation `r_h·log q_h ≈ L` is stated in. -/
theorem log_prod_pow (qd : Fin m → ℕ) (hq : ∀ h, qd h ≠ 0) (r : Fin m → ℕ) :
    Real.log (∏ h, (qd h : ℝ) ^ (r h)) = ∑ h, (r h : ℝ) * Real.log (qd h) := by
  rw [Real.log_prod]
  · exact Finset.sum_congr rfl (fun h _ => Real.log_pow _ _)
  · intro h _
    exact pow_ne_zero _ (Nat.cast_ne_zero.mpr (hq h))

/-- **Step 2, with its numeric hypothesis in additive form.**  The left side is the auxiliary
polynomial's size plus the denominators' size; the right side is the index gap times the
approximation exponent.  That is Roth's inequality as it is stated in prose. -/
theorem le_index_rational_of_log (r : Fin m → ℕ) (hr : ∀ h, r h ≠ 0)
    (pn : Fin m → ℤ) (qd : Fin m → ℕ) (hq : ∀ h, qd h ≠ 0)
    (α : Fin m → ℝ) {G T : Fin m → ℝ} (hG0 : ∀ h, 0 ≤ G h)
    (hGT : ∀ h, G h ≤ Real.exp (-(T h)))
    (hclose : ∀ h, |(((pn h : ℚ) / (qd h : ℚ) : ℚ) : ℝ) - α h| ≤ G h)
    {K : ℝ} (hK0 : 0 ≤ K) (hT : ∀ h, K ≤ T h * (r h : ℝ))
    {B : ℝ} (hB1 : 1 ≤ B) (hα : ∀ h, |α h| ≤ B)
    (P : MvPolynomial (Fin m) ℤ) (hdeg : ∀ h, degreeOf h P ≤ r h)
    {H : ℝ} (hH : ∀ k, |((coeff k P : ℤ) : ℝ)| ≤ H)
    {μ ν : ℚ} (hidx : ((μ : ℚ) : WithTop ℚ) ≤ index r α (map (Int.castRingHom ℝ) P))
    (hCpos : 0 < taylorConst r H B)
    (hlog : Real.log (taylorConst r H B) + ∑ h, (r h : ℝ) * Real.log (qd h)
      < K * ((μ : ℝ) - (ν : ℝ))) :
    ((ν : ℚ) : WithTop ℚ)
      ≤ index r (fun h => (pn h : ℚ) / (qd h : ℚ)) (map (Int.castRingHom ℚ) P) := by
  have hD : (0 : ℝ) < ∏ h, (qd h : ℝ) ^ (r h) :=
    Finset.prod_pos (fun h _ => pow_pos (by exact_mod_cast Nat.pos_of_ne_zero (hq h)) _)
  have hlog' : Real.log (taylorConst r H B) + Real.log (∏ h, (qd h : ℝ) ^ (r h))
      < K * ((μ : ℝ) - (ν : ℝ)) := by
    rw [log_prod_pow qd hq r]
    exact hlog
  have hmul := mul_exp_neg_lt_one_div hCpos hD hlog'
  refine le_index_rational_of_taylor r hr pn qd hq α hG0 hGT hclose hK0 hT hB1 hα
    P hdeg hH hidx ?_
  calc ((∏ h, (r h + 1) : ℕ) : ℝ)
        * ((((∏ h, (r h + 1) : ℕ) : ℝ) * (H * (2 * B) ^ (∑ h, r h)))
            * ((2 : ℝ) ^ (∑ h, r h) * Real.exp (-(K * ((μ : ℝ) - (ν : ℝ))))))
      = taylorConst r H B * Real.exp (-(K * ((μ : ℝ) - (ν : ℝ)))) := by
        rw [taylorConst]; ring
    _ < 1 / (∏ h, (qd h : ℝ) ^ (r h)) := hmul

/-- **What a parameter choice has to beat, term by term.**  `log(taylorConst)` splits into four
named costs: the box count (twice — once for `P`'s support, once for its translate), the height of
`P`, the translation cost `(2B)^{Σr}`, and the peeling cost `2^{Σr}`.

Writing it out is the point of the exercise.  In the additive form of Roth's inequality the whole
left side is `2·log(box) + log H + Σr·log(4B) + Σ_h r_h·log q_h`, and every one of those terms
scales with `Σ_h r_h` except `log H`.  So the normalisation cannot be one-sided: `r_h·log q_h ≥ L`
alone bounds the right side from below but leaves `Σ_h r_h·log q_h` on the left unbounded above,
and a parameter record that carries only the lower bound cannot discharge this.  That is a
constraint on the record, discovered by writing the decomposition rather than by assuming it. -/
theorem log_taylorConst (r : Fin m → ℕ) {H B : ℝ} (hH : 0 < H) (hB : 0 < B) :
    Real.log (taylorConst r H B)
      = 2 * Real.log (((∏ h, (r h + 1) : ℕ)) : ℝ) + Real.log H
        + ((∑ h, r h : ℕ) : ℝ) * Real.log (2 * B)
        + ((∑ h, r h : ℕ) : ℝ) * Real.log 2 := by
  have hbox : (0 : ℝ) < ((∏ h, (r h + 1) : ℕ) : ℝ) := by
    have : 0 < ∏ h, (r h + 1) := Finset.prod_pos (fun h _ => Nat.succ_pos _)
    exact_mod_cast this
  have h2B : (0 : ℝ) < 2 * B := by linarith
  have hboxne : ((∏ h, (r h + 1) : ℕ) : ℝ) ≠ 0 := ne_of_gt hbox
  have hHne : H ≠ 0 := ne_of_gt hH
  have hpowne : ((2 : ℝ) * B) ^ (∑ h, r h) ≠ 0 := pow_ne_zero _ (ne_of_gt h2B)
  have h2ne : ((2 : ℝ)) ^ (∑ h, r h) ≠ 0 := by positivity
  rw [taylorConst,
    Real.log_mul (by exact mul_ne_zero hboxne (mul_ne_zero hboxne (mul_ne_zero hHne hpowne))) h2ne,
    Real.log_mul hboxne (mul_ne_zero hboxne (mul_ne_zero hHne hpowne)),
    Real.log_mul hboxne (mul_ne_zero hHne hpowne),
    Real.log_mul hHne hpowne,
    Real.log_pow, Real.log_pow]
  ring

end LogForm

section Collision

variable {m : ℕ}

/-- **The collision.**  A lower bound `ν` and Roth's Lemma's upper bound cannot both hold once
`c_m^{2^{m−1}}·(p/q)` drops below `ν^{2^{m−1}}`.  Everything else in Roth's theorem exists to make
that one inequality available. -/
theorem false_of_le_index_of_rothBound {r : Fin m → ℕ} {κ : Fin m → ℚ}
    {Pq : MvPolynomial (Fin m) ℚ} {ν Θ t : ℚ} (hν0 : 0 ≤ ν)
    (h2 : ((ν : ℚ) : WithTop ℚ) ≤ index r κ Pq)
    (h3 : index r κ Pq ≤ ((Θ : ℚ) : WithTop ℚ))
    (hΘ : Θ ^ (2 ^ (m - 1)) ≤ (rothConstant m : ℚ) ^ (2 ^ (m - 1)) * t)
    (hgap : (rothConstant m : ℚ) ^ (2 ^ (m - 1)) * t < ν ^ (2 ^ (m - 1))) :
    False := by
  have hνΘtop : ((ν : ℚ) : WithTop ℚ) ≤ ((Θ : ℚ) : WithTop ℚ) := le_trans h2 h3
  have hνΘ : ν ≤ Θ := by exact_mod_cast hνΘtop
  have hpow : ν ^ (2 ^ (m - 1)) ≤ Θ ^ (2 ^ (m - 1)) := pow_le_pow_left₀ hν0 hνΘ _
  linarith

/-- The unique ring hom `ℤ → ℚ`, under its two names — step 3 states its conclusion with
`algebraMap`, step 2 with `Int.castRingHom`.

⚠ **Not load-bearing.**  I wrote this expecting to need it and used it to bridge the two
statements; deleting the bridging rewrite and rebuilding shows the file still compiles, so the two
unify definitionally.  Kept as a recorded check — the claim "composing the halves surfaced an
interface mismatch" was mine and was wrong, and the lemma is the evidence for the correction. -/
theorem algebraMap_int_rat : (algebraMap ℤ ℚ) = Int.castRingHom ℚ := RingHom.ext_int _ _

/-- **Step 4.**  Steps 2 and 3 in one place: the Taylor lower bound and Roth's Lemma's upper bound
on the same index, contradicting each other as soon as the numeric hypotheses hold.

The last two hypotheses are the whole of the parameter bookkeeping — `hlog` is Roth's inequality
(sizes on the left, index gap times approximation exponent on the right) and `hgap` says the ratio
`p/q` that `Γ_m` supplies is smaller than `(ν/c_m)^{2^{m−1}}`. -/
theorem roth_contradiction (hm : 1 ≤ m) {p q F : ℕ} (hp : 0 < p) (hpq : p ≤ q)
    {a : ℤ} {r Hh : Fin m → ℕ} (hr : ∀ h, r h ≠ 0)
    (hg : RothGammaFull (Equiv.refl (Fin m)) p q F r (fun j => (Hh j : ℤ)) a)
    (pn : Fin m → ℤ) (qd : Fin m → ℕ) (hq : ∀ h, qd h ≠ 0)
    (α : Fin m → ℝ) {G T : Fin m → ℝ} (hG0 : ∀ h, 0 ≤ G h)
    (hGT : ∀ h, G h ≤ Real.exp (-(T h)))
    (hclose : ∀ h, |(((pn h : ℚ) / (qd h : ℚ) : ℚ) : ℝ) - α h| ≤ G h)
    {K : ℝ} (hK0 : 0 ≤ K) (hT : ∀ h, K ≤ T h * (r h : ℝ))
    {B : ℝ} (hB1 : 1 ≤ B) (hα : ∀ h, |α h| ≤ B)
    (P : MvPolynomial (Fin m) ℤ) (hdeg : ∀ h, degreeOf h P ≤ r h)
    (hA : InRothPolySet a r P) (hκ : InRothFracSet Hh (fun h => (pn h : ℚ) / (qd h : ℚ)))
    {H : ℝ} (hH : ∀ k, |((coeff k P : ℤ) : ℝ)| ≤ H)
    {μ ν : ℚ} (hν0 : 0 ≤ ν)
    (hidx : ((μ : ℚ) : WithTop ℚ) ≤ index r α (map (Int.castRingHom ℝ) P))
    (hCpos : 0 < taylorConst r H B)
    (hlog : Real.log (taylorConst r H B) + ∑ h, (r h : ℝ) * Real.log (qd h)
      < K * ((μ : ℝ) - (ν : ℝ)))
    (hgap : (rothConstant m : ℚ) ^ (2 ^ (m - 1)) * ((p : ℚ) / (q : ℚ)) < ν ^ (2 ^ (m - 1))) :
    False := by
  obtain ⟨Θ, _, hΘbound, hΘidx⟩ :=
    index_le_rothBound hm hp hpq (Equiv.refl (Fin m)) hg hA hκ
  -- no coercion bridge needed: `algebraMap ℤ ℚ` and `Int.castRingHom ℚ` unify definitionally
  -- (see `algebraMap_int_rat`, which is a recorded check rather than a step).
  exact false_of_le_index_of_rothBound hν0
    (le_index_rational_of_log r hr pn qd hq α hG0 hGT hclose hK0 hT hB1 hα P hdeg hH hidx
      hCpos hlog)
    hΘidx hΘbound hgap

/-- **The structural hypotheses are jointly satisfiable.**  `roth_contradiction` concludes `False`,
so its hypotheses are *supposed* to be jointly unsatisfiable — which means vacuity is not the risk.
The risk is that some **structural** subset is already inconsistent, making the theorem true for a
reason having nothing to do with Roth.  This rules that out by supplying every structural argument
at the parameters of `index_le_rothBound_witness` (`m = 2`, `p = q = 1`, `F = 10`, `a = 1`,
`r = (1,1)`, `H = (1024,1024)`, `P = 1`, `κ = 1024`, `α = 1024`, `G = 0`), leaving exactly the two
numeric conditions as hypotheses.

⚠ It does **not** show the collision fires.  At `μ = ν = 0` both remaining hypotheses are false —
`hlog` because `taylorConst > 1` makes its left side positive while its right side is `0`, and
`hgap` because `c₂² · 1 = 25` is not below `0`.  They must be false somewhere, or `False` would be
derivable from satisfiable hypotheses.  Both holding at once needs `μ ≈ m(½−ε)` from step 1 and
`K ≈ (2+δ)L` from an approximation exponent above `2`, which is Roth's inequality and is what a
parameter record has to deliver — not something a small witness can exhibit. -/
theorem roth_contradiction_at_witness
    (hlog : Real.log (taylorConst (fun _ : Fin 2 => 1) 1 1024)
        + ∑ _ : Fin 2, (((1 : ℕ) : ℝ)) * Real.log (((1 : ℕ) : ℝ))
        < 8 * (((0 : ℚ) : ℝ) - ((0 : ℚ) : ℝ)))
    (hgap : (rothConstant 2 : ℚ) ^ (2 ^ (2 - 1)) * (((1 : ℕ) : ℚ) / ((1 : ℕ) : ℚ))
        < (0 : ℚ) ^ (2 ^ (2 - 1))) :
    False :=
  roth_contradiction (m := 2) (by norm_num) (p := 1) (q := 1) (F := 10) one_pos le_rfl
    (a := 1) (r := fun _ => 1) (Hh := fun _ => 1024) (fun _ => one_ne_zero)
    { growth := by intro j k hjk; norm_num
      height := by intro j k _; exact le_rfl
      floorExp := by norm_num
      floor := by intro j _; norm_num
      heightBound := by intro j _; norm_num
      two_le := fun _ => by norm_num
      degPos := fun _ => one_ne_zero }
    (fun _ => (1024 : ℤ)) (fun _ => (1 : ℕ)) (fun _ => one_ne_zero)
    (fun _ => (1024 : ℝ)) (G := fun _ => 0) (T := fun _ => 8)
    (fun _ => le_rfl) (fun _ => Real.exp_nonneg _) (fun _ => by norm_num)
    (K := 8) (by norm_num) (fun _ => by norm_num)
    (B := 1024) (by norm_num) (fun _ => by norm_num)
    (1 : MvPolynomial (Fin 2) ℤ) (fun h => by rw [← C_1, degreeOf_C]; norm_num)
    ⟨one_ne_zero, fun h => by rw [← C_1, degreeOf_C]; norm_num, fun n => by
      simp only [coeff_one]; split_ifs <;> norm_num⟩
    (by intro _; norm_num [InRothFracSet])
    (H := 1) (fun k => by simp only [coeff_one]; split_ifs <;> norm_num)
    (μ := 0) (ν := 0) le_rfl (by simpa using index_nonneg _ _ _)
    (by rw [taylorConst]; positivity)
    hlog hgap

end Collision

end MvPolynomial
