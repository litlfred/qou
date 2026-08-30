/-
# The normalisation, and the discovery that `rothDegrees` already satisfies it

`RothContradiction` left step 4 resting on one hypothesis in additive form,

    log(taylorConst) + ∑_h r_h·log q_h  <  K·(μ − ν),

and `log_taylorConst` showed why it cannot be discharged from a one-sided normalisation: every
term of `log(taylorConst)` except `log H` scales with `∑_h r_h`, so `r_h·log q_h ≥ L` bounds the
right side from below while leaving the left side's `∑_h r_h·log q_h` unbounded above.  What is
needed is `L ≤ r_h·log q_h ≤ L'`.

## `rothDegrees` was already two-sided

That was going to be an extra obligation on whatever supplied the degrees.  It is not:
`rothDegrees H N h` is `log_{H_h} N` (plus one off the first coordinate), and
`rothDegrees_log_bounds` shows

    log N − log H_h  ≤  r_h·log H_h  ≤  log N + log H_h

for every `h`, which is the two-sided normalisation with `L = log N − max_h log H_h` and
`L' = log N + max_h log H_h`.  `Γ_m`'s growth clause consumes the lower half; step 4's inequality
needs both; they are the same construction.  So the worry that opened this bean — two
normalisations for one ladder, which is the shape correction 26 had — was unfounded, and the fix
is to *record* that they coincide rather than to introduce a record reconciling them.

## No `Prop` carrier

The obvious packaging is a structure bundling the normalisation.  I am not doing that, and the
reason is row 19 of the detector-blindness taxonomy, which I opened on exactly this pattern: a
`def : Prop` / `structure : Prop` carrier is invisible to every detector in the suite, so a false
or over-strong clause inside one goes unflagged.  With a single consumer the packaging buys
nothing and re-creates the blind spot, so the normalisation stays as explicit hypotheses.

## The reduction

`log_taylorConst_le` bounds the polynomial's total size by `θ·∑_h r_h·log q_h` from one
per-coordinate condition, `2 + c_H + log(4B) ≤ θ·log q_h` — "each denominator is large compared
with the auxiliary polynomial's per-degree cost", which is Roth's *choose the `q_h` large* in
exactly the form the estimate consumes.  `log_condition_of_cost` then closes the additive
inequality against `(1+θ)·m·L' < K(μ−ν)`.
-/
import QOU.Mathlib.RothContradiction

namespace MvPolynomial

open Finset

section Normalisation

variable {m : ℕ}

/-- **The upper half of the normalisation does the work.**  With `∑_h r_h·log q_h ≤ m·L'` and the
polynomial's size a `θ`-fraction of it, the additive form of Roth's inequality reduces to a
comparison of constants. -/
theorem log_condition_of_cost (r qd : Fin m → ℕ) {C L' θ K μ ν : ℝ}
    (hL' : ∀ h, (r h : ℝ) * Real.log (qd h) ≤ L')
    (hθ0 : 0 ≤ θ)
    (hcost : C ≤ θ * (∑ h, (r h : ℝ) * Real.log (qd h)))
    (hfin : (1 + θ) * ((m : ℝ) * L') < K * (μ - ν)) :
    C + ∑ h, (r h : ℝ) * Real.log (qd h) < K * (μ - ν) := by
  have hsum : (∑ h, (r h : ℝ) * Real.log (qd h)) ≤ (m : ℝ) * L' := by
    calc (∑ h, (r h : ℝ) * Real.log (qd h)) ≤ ∑ _h : Fin m, L' :=
          Finset.sum_le_sum (fun h _ => hL' h)
      _ = (m : ℝ) * L' := by
          rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  have hscale : (1 + θ) * (∑ h, (r h : ℝ) * Real.log (qd h)) ≤ (1 + θ) * ((m : ℝ) * L') :=
    mul_le_mul_of_nonneg_left hsum (by linarith)
  nlinarith [hcost, hscale]

/-- **The polynomial's size, bounded per coordinate.**  `2 + c_H + log(4B) ≤ θ·log q_h` — each
denominator large compared with the per-degree cost — gives
`log(taylorConst) ≤ θ·∑_h r_h·log q_h`.

`c_H` is the rate at which step 1's height bound grows with `∑_h r_h`; taking it as a hypothesis
rather than deriving it keeps this file independent of which Siegel lemma produced the
polynomial. -/
theorem log_taylorConst_le (r qd : Fin m → ℕ) {H B θ cH : ℝ}
    (hH : 0 < H) (hB : 0 < B)
    (hHlog : Real.log H ≤ cH * ∑ h, (r h : ℝ))
    (hpt : ∀ h, 2 + cH + Real.log (2 * B) + Real.log 2 ≤ θ * Real.log (qd h)) :
    Real.log (taylorConst r H B) ≤ θ * ∑ h, (r h : ℝ) * Real.log (qd h) := by
  have hboxcast : (((∏ h, (r h + 1) : ℕ)) : ℝ) = ∏ h, ((r h : ℝ) + 1) := by push_cast; ring
  have hbox : Real.log (((∏ h, (r h + 1) : ℕ)) : ℝ) ≤ ∑ h, (r h : ℝ) := by
    rw [hboxcast, Real.log_prod _ _ (fun h _ => by positivity)]
    refine Finset.sum_le_sum (fun h _ => ?_)
    have := Real.log_le_sub_one_of_pos (x := ((r h : ℝ) + 1)) (by positivity)
    linarith
  have hSum : (((∑ h, r h : ℕ)) : ℝ) = ∑ h, (r h : ℝ) := by push_cast; ring
  have hkey : (∑ h, (r h : ℝ)) * (2 + cH + Real.log (2 * B) + Real.log 2)
      ≤ θ * ∑ h, (r h : ℝ) * Real.log (qd h) := by
    rw [Finset.sum_mul, Finset.mul_sum]
    refine Finset.sum_le_sum (fun h _ => ?_)
    have hr : (0 : ℝ) ≤ (r h : ℝ) := Nat.cast_nonneg _
    have := mul_le_mul_of_nonneg_left (hpt h) hr
    calc (r h : ℝ) * (2 + cH + Real.log (2 * B) + Real.log 2)
        ≤ (r h : ℝ) * (θ * Real.log (qd h)) := this
      _ = θ * ((r h : ℝ) * Real.log (qd h)) := by ring
  rw [log_taylorConst r hH hB, hSum]
  nlinarith [hbox, hHlog, hkey]

end Normalisation

section Degrees

/-- **`rothDegrees` is two-sided.**  `r_h = log_{H_h} N` (plus one off the first coordinate) puts
`r_h·log H_h` within `log H_h` of `log N` on both sides — so the degrees `Γ_m`'s growth clause is
built from already satisfy the normalisation step 4's inequality needs.  The two halves of the
argument were never using different normalisations. -/
theorem rothDegrees_log_bounds {m : ℕ} (H : Fin m → ℕ) (N : ℕ) (hN : N ≠ 0)
    (hH : ∀ h, 2 ≤ H h) (h : Fin m) :
    Real.log N - Real.log (H h) ≤ (rothDegrees H N h : ℝ) * Real.log (H h)
      ∧ (rothDegrees H N h : ℝ) * Real.log (H h) ≤ Real.log N + Real.log (H h) := by
  have hHb : 1 < H h := lt_of_lt_of_le one_lt_two (hH h)
  have hHR : (1 : ℝ) < (H h : ℝ) := by exact_mod_cast hHb
  have hHpos : (0 : ℝ) < (H h : ℝ) := by linarith
  have hNR : (0 : ℝ) < (N : ℝ) := by exact_mod_cast Nat.pos_of_ne_zero hN
  have h1 : (H h) ^ (Nat.log (H h) N) ≤ N := Nat.pow_log_le_self _ hN
  have h2 : N < (H h) ^ (Nat.log (H h) N + 1) := Nat.lt_pow_succ_log_self hHb N
  have g1 : ((Nat.log (H h) N : ℝ)) * Real.log (H h) ≤ Real.log N := by
    have hcast : ((H h : ℝ)) ^ (Nat.log (H h) N) ≤ (N : ℝ) := by exact_mod_cast h1
    have := Real.log_le_log (by positivity) hcast
    rwa [Real.log_pow] at this
  have g2 : Real.log N < ((Nat.log (H h) N : ℝ) + 1) * Real.log (H h) := by
    have hcast : (N : ℝ) < ((H h : ℝ)) ^ (Nat.log (H h) N + 1) := by exact_mod_cast h2
    have := Real.log_lt_log hNR hcast
    rw [Real.log_pow] at this
    push_cast at this
    linarith
  simp only [rothDegrees]
  split_ifs
  · exact ⟨by linarith, by linarith⟩
  · push_cast
    constructor
    · nlinarith [g2]
    · nlinarith [g1]

/-- **The normalisation in the denominators' currency, and what does not transfer.**  Step 4 wants
bounds on `r_h·log q_h`, but `rothDegrees` is built from the *heights* `H_h = max(|p_h|, q_h)`.
The **upper** half transfers for free, because `q_h ≤ H_h`.

The **lower** half does not, and the asymmetry is real rather than an artefact: `H_h ≤ q_h` fails
whenever the numerator dominates, and then `r_h·log q_h` sits arbitrarily far below `r_h·log H_h`.
`height_le_den` below identifies exactly what recovers it — `|p_h| ≤ q_h`, which in Roth's setting
is the harmless consequence of approximating a number of absolute value at most `1`.  It is a
hypothesis on the approximations, not a consequence of the degree choice, and stating which one
is the point of separating these two lemmas. -/
theorem rothDegrees_log_bounds_den {m : ℕ} (H qd : Fin m → ℕ) (N : ℕ) (hN : N ≠ 0)
    (hH : ∀ h, 2 ≤ H h) (hq1 : ∀ h, 1 ≤ qd h) (hqH : ∀ h, qd h ≤ H h) (h : Fin m) :
    (rothDegrees H N h : ℝ) * Real.log (qd h) ≤ Real.log N + Real.log (H h) := by
  have hqpos : (0 : ℝ) < (qd h : ℝ) := by exact_mod_cast Nat.lt_of_lt_of_le Nat.zero_lt_one (hq1 h)
  have hle : Real.log (qd h) ≤ Real.log (H h) :=
    Real.log_le_log hqpos (by exact_mod_cast hqH h)
  have hr : (0 : ℝ) ≤ (rothDegrees H N h : ℝ) := Nat.cast_nonneg _
  exact le_trans (mul_le_mul_of_nonneg_left hle hr) (rothDegrees_log_bounds H N hN hH h).2

/-- **What recovers the lower half.**  If the numerator does not exceed the denominator then the
height of the reduced fraction is at most `q`, so `log H_h ≤ log q_h` and the normalisation's
lower bound transfers from heights to denominators.

Note it is the *reduced* fraction's height: `2/4` has height `2`, not `4`, which is why this is an
inequality rather than the equality `H_h = q_h` one might expect. -/
theorem height_le_den {p : ℤ} {q : ℕ} (hq : q ≠ 0) (hpq : p.natAbs ≤ q) :
    max ((p : ℚ) / (q : ℚ)).num.natAbs ((p : ℚ) / (q : ℚ)).den ≤ q := by
  have hq0 : (q : ℤ) ≠ 0 := Int.natCast_ne_zero.mpr hq
  have hqpos : (0 : ℤ) < (q : ℤ) := by exact_mod_cast Nat.pos_of_ne_zero hq
  have hdiv : ((p : ℚ) / (q : ℚ)) = (Rat.divInt p (q : ℤ)) := (Rat.divInt_eq_div _ _).symm
  rw [hdiv]
  have hden : (((Rat.divInt p (q : ℤ)).den : ℤ)) ∣ (q : ℤ) := Rat.den_dvd p (q : ℤ)
  have hden' : (Rat.divInt p (q : ℤ)).den ≤ q := by
    have := Int.le_of_dvd hqpos hden
    exact_mod_cast this
  have hnum' : (Rat.divInt p (q : ℤ)).num.natAbs ≤ q := by
    rcases eq_or_ne p 0 with rfl | hp0
    · simp
    · have hdvd : (Rat.divInt p (q : ℤ)).num.natAbs ∣ p.natAbs :=
        Int.natAbs_dvd_natAbs.mpr (Rat.num_dvd p hq0)
      exact le_trans (Nat.le_of_dvd (Int.natAbs_pos.mpr hp0) hdvd) hpq
  exact max_le hnum' hden'

end Degrees

section Assembled

variable {m : ℕ}

/-- **Step 4 from the normalisation.**  `roth_contradiction` with its additive hypothesis replaced
by data a parameter choice can actually be checked against: an upper normalisation `r_h·log q_h ≤
L'`, a per-coordinate size condition, and one comparison of constants.

The remaining `hfin` is Roth's inequality with everything named: `(1+θ)·m·L'` on the left — the
denominators' total size inflated by the polynomial's `θ`-share — against `K·(μ−ν)` on the right,
the approximation exponent times the index gap. -/
theorem roth_contradiction_of_normalisation (hm : 1 ≤ m) {p q F : ℕ} (hp : 0 < p) (hpq : p ≤ q)
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
    {H : ℝ} (hHpos : 0 < H) (hH : ∀ k, |((coeff k P : ℤ) : ℝ)| ≤ H)
    {cH θ L' : ℝ} (hθ0 : 0 ≤ θ)
    (hHlog : Real.log H ≤ cH * ∑ h, (r h : ℝ))
    (hpt : ∀ h, 2 + cH + Real.log (2 * B) + Real.log 2 ≤ θ * Real.log (qd h))
    (hL' : ∀ h, (r h : ℝ) * Real.log (qd h) ≤ L')
    {μ ν : ℚ} (hν0 : 0 ≤ ν)
    (hidx : ((μ : ℚ) : WithTop ℚ) ≤ index r α (map (Int.castRingHom ℝ) P))
    (hfin : (1 + θ) * ((m : ℝ) * L') < K * (((μ : ℚ) : ℝ) - ((ν : ℚ) : ℝ)))
    (hgap : (rothConstant m : ℚ) ^ (2 ^ (m - 1)) * ((p : ℚ) / (q : ℚ)) < ν ^ (2 ^ (m - 1))) :
    False := by
  have hB0 : (0 : ℝ) < B := lt_of_lt_of_le zero_lt_one hB1
  have hboxpos : (0 : ℝ) < (((∏ h, (r h + 1) : ℕ)) : ℝ) := by
    have : 0 < ∏ h, (r h + 1) := Finset.prod_pos (fun h _ => Nat.succ_pos _)
    exact_mod_cast this
  have hCpos : 0 < taylorConst r H B := by rw [taylorConst]; positivity
  exact roth_contradiction hm hp hpq hr hg pn qd hq α hG0 hGT hclose hK0 hT hB1 hα
    P hdeg hA hκ hH hν0 hidx hCpos
    (log_condition_of_cost r qd hL' hθ0 (log_taylorConst_le r qd hHpos hB0 hHlog hpt) hfin)
    hgap

end Assembled

section TakeMLarge

/-! ## Discharging the last inequality: what "take `m` sufficiently large" actually needs

Substituting the standard relations — `K = (2+δ)L` from an approximation exponent `2+δ`,
`L' = (1+η)L` from a normalisation tight to within `η`, and `μ = m(½−ε)` from step 1 — turns
`(1+θ)·m·L' < K(μ−ν)` into

    (2+δ)·ν  <  m · [ (2+δ)(½−ε) − (1+θ)(1+η) ],

so everything hinges on the bracket being positive, and `slack_pos` says exactly when:

    (2+δ)·ε + θ + η + θ·η  <  δ/2.

**The approximation excess `δ/2` must exceed the total slack**, and the three slacks are of
different origin — `ε` is how far step 1's index falls short of `m/2`, `η` is how far the
normalisation is from exact, `θ` is the auxiliary polynomial's share of the denominators' size.
Only after that is `m` free: `exists_m_of_slack` is then pure Archimedes.

Writing this out is what makes the four constants comparable.  Before it, `η` in particular had no
budget at all — it entered only in the last commit, when `rothDegrees` turned out to be two-sided,
and nothing said how tight the two sides had to be relative to `δ`.  Now `δ/2` pays for it.
-/

/-- **When the slack budget balances.**  The bracket that has to be positive before enlarging `m`
helps at all. -/
theorem slack_pos {δ η θ ε : ℝ}
    (hslack : (2 + δ) * ε + θ + η + θ * η < δ / 2) :
    0 < (2 + δ) * (1 / 2 - ε) - (1 + θ) * (1 + η) := by
  nlinarith [hslack]

/-- **Take `m` large.**  Once the slack budget balances, an `m` making the inequality strict
exists — and this is the only place in Roth's theorem where "sufficiently large" is used for its
Archimedean content rather than as shorthand for a counting bound.

No sign condition on `ν` is needed; I wrote one and the linter reported it unused, which is right —
`exists_nat_gt` does not care.  The stronger statement is kept. -/
theorem exists_m_of_slack {δ η θ ε ν : ℝ}
    (hslack : (2 + δ) * ε + θ + η + θ * η < δ / 2) :
    ∃ m : ℕ, (2 + δ) * ν < (m : ℝ) * ((2 + δ) * (1 / 2 - ε) - (1 + θ) * (1 + η)) := by
  set c : ℝ := (2 + δ) * (1 / 2 - ε) - (1 + θ) * (1 + η) with hc
  have hcpos : 0 < c := slack_pos hslack
  obtain ⟨m, hm⟩ := exists_nat_gt (((2 + δ) * ν) / c)
  exact ⟨m, by rwa [div_lt_iff₀ hcpos] at hm⟩

/-- **The last inequality, discharged.**  `(1+θ)·m·L' < K(μ−ν)` under the standard relations
`K = (2+δ)L`, `L' = (1+η)L`, `μ = m(½−ε)`, given the `m` that `exists_m_of_slack` produces. -/
theorem hfin_of_large {δ η θ ε L ν : ℝ} (hL : 0 < L) {m : ℕ}
    (hm : (2 + δ) * ν < (m : ℝ) * ((2 + δ) * (1 / 2 - ε) - (1 + θ) * (1 + η))) :
    (1 + θ) * ((m : ℝ) * ((1 + η) * L))
      < ((2 + δ) * L) * (((m : ℝ) * (1 / 2 - ε)) - ν) := by
  nlinarith [mul_pos hL (sub_pos.mpr hm)]

end TakeMLarge

end MvPolynomial
