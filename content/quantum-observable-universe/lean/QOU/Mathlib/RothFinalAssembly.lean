/-
# The parameter selection, in the currency the final inequality is stated in

`RothSiegelBound.exists_rothGammaFull_auxiliary` produces heights `H` and a threshold `N` with all
seven clauses of `Γ_m` at the auxiliary polynomial's own height.  `RothNormalisation`'s
`roth_contradiction_of_normalisation` consumes a *different* currency: three real constants `cH`,
`θ`, `L'`, a lower bound `K` on `T_h·r_h`, and the single inequality `(1+θ)·m·L' < K(μ−ν)`.

This file is the exchange.  Each lemma converts one clause of the selection's output into one
hypothesis of the normalisation, and every one of them turns out to be a *floor on the heights* or
a *power of the heights below `N`* — which is exactly what the selection takes as parameters.
That is the point: after this file, no hypothesis of the chain refers to data the chain itself
produces.

## The three slack constants, and where each comes from

* `η` is the normalisation slack.  It is `1/k`, where `k` is the exponent in the selection's new
  clause `(H h)^k ≤ N`: the heights are polynomially small in `N`, so `log H_h ≤ (1/k)·log N`, and
  the two-sided `rothDegrees_log_bounds` closes to within `1 ± 1/k`.  Taking `k` large is the
  formal content of "let `N` be large compared with the heights".
* `θ` is the auxiliary polynomial's share of the denominators' size.  It enters through `hpt`,
  which is a lower bound on `log q_h` — on the *denominators*, not the heights.  `height_le_mul_den`
  is what makes the two interchangeable: a rational bounded by `B` has `H ≤ B·q`, so a floor on the
  heights is a floor on the denominators up to the constant `B`.
* `ε` is how far step 1's index falls short of `m/2`, and is unchanged from `RothNormalisation`.

`δ`, the approximation excess, is not a slack — it is the budget the other three are paid out of,
which is what `slack_pos` says.
-/
import QOU.Mathlib.RothIntegerChain
import QOU.Mathlib.RothNormalisation
import QOU.Mathlib.RothSiegelBound

open NumberField Finset

-- The same local instance Mathlib's own `SiegelsLemma` uses: `auxMatrixInt`'s sup norm, which
-- `siegelHeight` is defined from, needs a `Norm` on matrices.
attribute [local instance] Matrix.seminormedAddCommGroup

namespace MvPolynomial

section Logs

/-- `H^k ≤ N`, in logs.  The selection's new clause, made usable. -/
theorem log_pow_le_log {Hh N k : ℕ} (hH : 2 ≤ Hh) (hpow : Hh ^ k ≤ N) :
    (k : ℝ) * Real.log Hh ≤ Real.log N := by
  have hHpos : (0 : ℝ) < (Hh : ℝ) := by
    have : 0 < Hh := by omega
    exact_mod_cast this
  have hcast : ((Hh : ℝ)) ^ k ≤ (N : ℝ) := by exact_mod_cast hpow
  have h := Real.log_le_log (by positivity) hcast
  rwa [Real.log_pow] at h

/-- **The normalisation slack is `1/k`.**  `rothDegrees_log_bounds` is two-sided to within
`log H_h`, and the selection's `(H h)^k ≤ N` bounds that by `(1/k)·log N`.  So the degrees satisfy
`(1 − η)·log N ≤ r_h·log H_h ≤ (1 + η)·log N` with `η = 1/k`, uniformly in `h` — which is what
`hT` and `hL'` need, and neither can get from a one-sided estimate. -/
theorem selection_normalisation {m : ℕ} (H : Fin m → ℕ) (N k : ℕ) (hN : N ≠ 0)
    (hH : ∀ h, 2 ≤ H h) (hk : 0 < k) (hpow : ∀ h, (H h) ^ k ≤ N) (h : Fin m) :
    (rothDegrees H N h : ℝ) * Real.log (H h) ≤ (1 + 1 / (k : ℝ)) * Real.log N
      ∧ (1 - 1 / (k : ℝ)) * Real.log N ≤ (rothDegrees H N h : ℝ) * Real.log (H h) := by
  have hkR : (0 : ℝ) < (k : ℝ) := by exact_mod_cast hk
  have hstep : Real.log (H h) ≤ (1 / (k : ℝ)) * Real.log N := by
    have hle := log_pow_le_log (hH h) (hpow h)
    rw [one_div, inv_mul_eq_div, le_div_iff₀ hkR]
    linarith
  obtain ⟨hlow, hhigh⟩ := rothDegrees_log_bounds H N hN hH h
  constructor
  · calc (rothDegrees H N h : ℝ) * Real.log (H h) ≤ Real.log N + Real.log (H h) := hhigh
      _ ≤ Real.log N + (1 / (k : ℝ)) * Real.log N := by linarith
      _ = (1 + 1 / (k : ℝ)) * Real.log N := by ring
  · calc (1 - 1 / (k : ℝ)) * Real.log N = Real.log N - (1 / (k : ℝ)) * Real.log N := by ring
      _ ≤ Real.log N - Real.log (H h) := by linarith
      _ ≤ (rothDegrees H N h : ℝ) * Real.log (H h) := hlow

end Logs

section Denominators

/-- **A bounded rational's height is at most `B` times its denominator.**  `H = max(|num|, den)`,
and `|num| ≤ B·den` is just `|κ| ≤ B` cleared of its denominator; `den ≤ B·den` needs `B ≥ 1`.

This is the lemma that lets a floor on the *heights* — which is all the selection can impose,
since `S` is a set of heights — serve as a floor on the *denominators*, which is what `hpt`
actually constrains.  Without it the two floors are unrelated: a rational of height `10^9` can
have denominator `1`. -/
theorem height_le_mul_den {κ : ℚ} {B : ℝ} (hB : 1 ≤ B) (hκ : |((κ : ℚ) : ℝ)| ≤ B) :
    ((max κ.num.natAbs κ.den : ℕ) : ℝ) ≤ B * (κ.den : ℝ) := by
  have hden : (0 : ℝ) < (κ.den : ℝ) := by exact_mod_cast κ.pos
  have hcast : ((κ : ℚ) : ℝ) = (κ.num : ℝ) / (κ.den : ℝ) := by
    rw [Rat.cast_def]
  have habs : |((κ : ℚ) : ℝ)| = |(κ.num : ℝ)| / (κ.den : ℝ) := by
    rw [hcast, abs_div, abs_of_pos hden]
  have hnum : |(κ.num : ℝ)| ≤ B * (κ.den : ℝ) := by
    rw [habs, div_le_iff₀ hden] at hκ
    linarith
  have hnat : ((κ.num.natAbs : ℕ) : ℝ) = |(κ.num : ℝ)| := by
    rw [Int.cast_natAbs, Int.cast_abs]
  rw [Nat.cast_max]
  refine max_le ?_ ?_
  · rw [hnat]; exact hnum
  · nlinarith

/-- **`hpt` from a floor on the heights.**  `roth_contradiction_of_normalisation`'s `hpt` clause is
`2 + cH + log(2B) + log 2 ≤ θ·log q_h`.  Routed through `height_le_mul_den`, it becomes a condition
on a *number* `T` below every height — and `T` is precisely the selection's floor parameter, so this
clause costs nothing beyond enlarging `T`. -/
theorem hpt_of_floor {m : ℕ} {H : Fin m → ℕ} {κ : Fin m → ℚ} {B θ cH : ℝ}
    (hB : 1 ≤ B) (hθ : 0 ≤ θ)
    (hκB : ∀ h, |((κ h : ℚ) : ℝ)| ≤ B)
    (hHκ : ∀ h, max (κ h).num.natAbs (κ h).den = H h)
    {T : ℕ} (hT1 : 1 ≤ T) (hfloorH : ∀ h, T ≤ H h)
    (hfloor : 2 + cH + Real.log (2 * B) + Real.log 2 + θ * Real.log B ≤ θ * Real.log T) :
    ∀ h, 2 + cH + Real.log (2 * B) + Real.log 2 ≤ θ * Real.log ((κ h).den : ℝ) := by
  intro h
  have hB0 : (0 : ℝ) < B := lt_of_lt_of_le zero_lt_one hB
  have hden : (0 : ℝ) < ((κ h).den : ℝ) := by exact_mod_cast (κ h).pos
  have hTR : (0 : ℝ) < (T : ℝ) := by exact_mod_cast hT1
  -- `T ≤ H h ≤ B · den h`
  have hHB : ((H h : ℕ) : ℝ) ≤ B * ((κ h).den : ℝ) := by
    rw [← hHκ h]; exact height_le_mul_den hB (hκB h)
  have hTH : (T : ℝ) ≤ ((H h : ℕ) : ℝ) := by exact_mod_cast hfloorH h
  have hlog : Real.log T ≤ Real.log B + Real.log ((κ h).den : ℝ) := by
    calc Real.log T ≤ Real.log (B * ((κ h).den : ℝ)) :=
          Real.log_le_log hTR (le_trans hTH hHB)
      _ = Real.log B + Real.log ((κ h).den : ℝ) := Real.log_mul (ne_of_gt hB0) (ne_of_gt hden)
  nlinarith [mul_le_mul_of_nonneg_left hlog hθ]

end Denominators

section Assembly

variable {m : ℕ} {K : Type*} [Field K] [NumberField K]

set_option maxHeartbeats 1600000 in
open private c from Mathlib.NumberTheory.NumberField.House in
/-- **Steps 1 → 2 → 3 → 4, with the parameters chosen rather than assumed.**

`roth_contradiction_int` needed nine facts about data it did not produce — the degrees `r`, the
heights `H`, the auxiliary polynomial's height bound, the approximations.  Here every one of them
is produced, and what is left is a list of conditions on constants alone:

* `hfloorExp`, `hgap`, `hpq` — the ladder's own arithmetic, unchanged from `Γ_m`;
* `hm2 : 2·[K:ℚ] < 4ε²m` — unknowns beat conditions, with the factor 2 that keeps Siegel's
  exponent at most 1;
* `hT` — one floor on the heights, discharging *both* the height clause (`hTsiegel`) and the
  polynomial's share of the denominators (`hTtheta`);
* `hfin` — Roth's inequality, with `log N` already divided out.

`hfin` is the interesting one.  In `(1+θ)·m·(1+η) < (2+δ)(1−η)·(m(½−ε) − ν)` the normalisation
slack `η = 1/k` appears on both sides with opposite signs: it inflates the denominators' total
size and deflates the approximation exponent.  Writing `2 + δ' := (2+δ)(1−η)` turns it into
exactly `exists_m_of_slack`'s shape at `δ'`, so **the excess the slack budget is paid from is not
`δ` but `δ − η(2+δ)`** — the approximation quality net of the normalisation.  That is the honest
statement of "choose `N` large compared with the heights", and it is why `k` had to become a
parameter of the selection.

The supply `app` is the negation of Roth's theorem in the form the proof consumes: for every
height in an unbounded set `S` there is a rational of *exactly* that height approximating `ψ α₀` to
within `H^{-(2+δ)}`. -/
theorem roth_contradiction_selected [DecidableEq (K →+* ℂ)]
    (hm : 1 ≤ m) {S : Set ℕ} (hS : ∀ N, ∃ q ∈ S, N ≤ q)
    {p q F k : ℕ} (hp : 0 < p) (hpq : p ≤ q) (hq : 0 < q) (hF : 1 ≤ F) (hk : 1 ≤ k)
    (hfloorExp : q * ((m - 1) * m * (2 * m + 1)) ≤ F * p)
    (α₀ : 𝓞 K) (ψ : K →+* ℝ)
    {B : ℝ} (hB1 : 1 ≤ B) (hhouse : house ((algebraMap (𝓞 K) K) α₀) ≤ B)
    (hψα : |ψ ((algebraMap (𝓞 K) K) α₀)| + 1 ≤ B)
    {ε : ℚ} (hε : 0 < ε) (hε2 : ε ≤ 1 / 2)
    (hm2 : 2 * ((Module.finrank ℚ K : ℕ) : ℚ) < 4 * ε ^ 2 * (m : ℚ))
    {C₀ W : ℤ} (hC₀1 : 1 ≤ C₀) (hC₀ : c K ≤ (C₀ : ℝ)) (hW1 : 1 ≤ W) (hW : 4 * B ≤ (W : ℝ))
    {δ : ℝ} (hδ : 0 ≤ δ)
    (app : ∀ Hv ∈ S, ∃ κ : ℚ, max κ.num.natAbs κ.den = Hv ∧
      |((κ : ℚ) : ℝ) - ψ ((algebraMap (𝓞 K) K) α₀)| ≤ (Hv : ℝ) ^ (-(2 + δ)))
    {θ : ℝ} (hθ0 : 0 ≤ θ) (T : ℕ) (hT1 : 1 ≤ T)
    (hTsiegel : C₀ ^ (m * q) * W ^ (2 * m * m * q) ≤ (T : ℤ))
    (hTtheta : 2 + (Real.log C₀ + Real.log W) + Real.log (2 * B) + Real.log 2
      + θ * Real.log B ≤ θ * Real.log T)
    {ν : ℚ} (hν0 : 0 ≤ ν)
    (hgap : (rothConstant m : ℚ) ^ (2 ^ (m - 1)) * ((p : ℚ) / (q : ℚ)) < ν ^ (2 ^ (m - 1)))
    (hfin : (1 + θ) * ((m : ℝ) * (1 + 1 / (k : ℝ)))
      < (2 + δ) * (1 - 1 / (k : ℝ))
        * ((((m : ℚ) / 2 - ε * (m : ℚ) : ℚ) : ℝ) - ((ν : ℚ) : ℝ))) :
    False := by
  classical
  have hmpos : 0 < m := hm
  have hB0 : (0 : ℝ) < B := lt_of_lt_of_le zero_lt_one hB1
  have hkR : (0 : ℝ) < (k : ℝ) := by exact_mod_cast hk
  have hkinv : 1 / (k : ℝ) ≤ 1 := by rw [div_le_one hkR]; exact_mod_cast hk
  -- 1.  the selection: heights, threshold, and all seven clauses of `Γ_m`
  obtain ⟨H, N, hmem, hN, hH2, hTle, hrne, hkpow, hmono, hg⟩ :=
    exists_rothGammaFull_auxiliary hS p q F k hp hq hF hfloorExp (fun _ => α₀) hε hm2 hB1
      (fun _ => hhouse) hC₀1 hC₀ hW1 hW T hTsiegel
  set r : Fin m → ℕ := rothDegrees H N with hrdef
  have hHpos : ∀ h, 1 ≤ H h := fun h => le_trans one_le_two (hH2 h)
  have hHR : ∀ h, (1 : ℝ) ≤ (H h : ℝ) := fun h => by exact_mod_cast hHpos h
  -- 2.  the approximations at those heights
  choose κ hκH hκclose using fun h : Fin m => app (H h) (hmem h)
  have hqne : ∀ h : Fin m, (κ h).den ≠ 0 := fun h => (κ h).den_nz
  have hfrac : ∀ h : Fin m, (((κ h).num : ℚ) / ((κ h).den : ℚ)) = κ h :=
    fun h => Rat.num_div_den (κ h)
  have hGle1 : ∀ h, ((H h : ℝ)) ^ (-(2 + δ)) ≤ 1 := fun h =>
    Real.rpow_le_one_of_one_le_of_nonpos (hHR h) (by linarith)
  have hκB : ∀ h, |((κ h : ℚ) : ℝ)| ≤ B := by
    intro h
    have h1 := hκclose h
    have h2 := hGle1 h
    have h3 := abs_sub_abs_le_abs_sub (((κ h : ℚ) : ℝ)) (ψ ((algebraMap (𝓞 K) K) α₀))
    linarith
  -- 3.  the approximation quality, in exponential form
  have hGT : ∀ h, ((H h : ℝ)) ^ (-(2 + δ))
      ≤ Real.exp (-((2 + δ) * Real.log (H h))) := by
    intro h
    have hpos : (0 : ℝ) < (H h : ℝ) := lt_of_lt_of_le zero_lt_one (hHR h)
    rw [Real.rpow_def_of_pos hpos]
    exact le_of_eq (by ring_nf)
  -- 4.  `N` is at least 2, so `log N > 0`
  have h2N : 2 ≤ N := by
    have h1 : (2 : ℕ) ≤ H (⟨0, hm⟩ : Fin m) := hH2 _
    calc (2 : ℕ) = 2 ^ 1 := (pow_one 2).symm
      _ ≤ 2 ^ k := Nat.pow_le_pow_right (by norm_num) hk
      _ ≤ (H (⟨0, hm⟩ : Fin m)) ^ k := Nat.pow_le_pow_left h1 k
      _ ≤ N := hkpow _
  have hlogN : (0 : ℝ) < Real.log N := Real.log_pos (by exact_mod_cast h2N)
  have hnorm := fun h : Fin m => selection_normalisation H N k hN hH2 hk hkpow h
  -- 5.  the two normalisation constants
  have hK0 : (0 : ℝ) ≤ (2 + δ) * (1 - 1 / (k : ℝ)) * Real.log N := by
    have : (0 : ℝ) ≤ 1 - 1 / (k : ℝ) := by linarith
    have h2 : (0 : ℝ) ≤ 2 + δ := by linarith
    positivity
  have hTr : ∀ h, (2 + δ) * (1 - 1 / (k : ℝ)) * Real.log N
      ≤ ((2 + δ) * Real.log (H h)) * (r h : ℝ) := by
    intro h
    have h2 : (0 : ℝ) ≤ 2 + δ := by linarith
    calc (2 + δ) * (1 - 1 / (k : ℝ)) * Real.log N
        = (2 + δ) * ((1 - 1 / (k : ℝ)) * Real.log N) := by ring
      _ ≤ (2 + δ) * ((r h : ℝ) * Real.log (H h)) :=
          mul_le_mul_of_nonneg_left (hnorm h).2 h2
      _ = ((2 + δ) * Real.log (H h)) * (r h : ℝ) := by ring
  have hL' : ∀ h : Fin m, (r h : ℝ) * Real.log (((κ h).den : ℕ) : ℝ)
      ≤ (1 + 1 / (k : ℝ)) * Real.log N := by
    intro h
    have hqdle : (κ h).den ≤ H h := by rw [← hκH h]; exact le_max_right _ _
    have hqd1 : (1 : ℝ) ≤ (((κ h).den : ℕ) : ℝ) := by
      have : 1 ≤ (κ h).den := (κ h).pos
      exact_mod_cast this
    have hlogle : Real.log (((κ h).den : ℕ) : ℝ) ≤ Real.log (H h) :=
      Real.log_le_log (by linarith) (by exact_mod_cast hqdle)
    calc (r h : ℝ) * Real.log (((κ h).den : ℕ) : ℝ)
        ≤ (r h : ℝ) * Real.log (H h) :=
          mul_le_mul_of_nonneg_left hlogle (Nat.cast_nonneg _)
      _ ≤ (1 + 1 / (k : ℝ)) * Real.log N := (hnorm h).1
  -- 6.  the auxiliary polynomial's height, and its logarithm
  have hbox : 1 ≤ Fintype.card {n // n ∈ idxBoxF r} := by
    rw [Fintype.card_coe, card_idxBoxF]; exact card_idxBox_pos r
  have hboxR : (1 : ℝ) ≤ (Fintype.card {n // n ∈ idxBoxF r} : ℝ) := by exact_mod_cast hbox
  have hsiegelPos : (0 : ℝ) <
      siegelHeight r (fun _ => α₀) ((m : ℚ) / 2 - ε * (m : ℚ)) := by
    rw [siegelHeight]
    have hmax : (1 : ℝ) ≤ max 1 ‖auxMatrixInt r (fun _ => α₀)
        ((m : ℚ) / 2 - ε * (m : ℚ))‖ := le_max_left _ _
    exact Real.rpow_pos_of_pos (by nlinarith) _
  have hceilPos : (0 : ℤ) < ⌈siegelHeight r (fun _ => α₀) ((m : ℚ) / 2 - ε * (m : ℚ))⌉ :=
    Int.lt_ceil.mpr (by exact_mod_cast hsiegelPos)
  have hHpolyPos : (0 : ℝ) <
      ((⌈siegelHeight r (fun _ => α₀) ((m : ℚ) / 2 - ε * (m : ℚ))⌉ : ℤ) : ℝ) := by
    exact_mod_cast hceilPos
  have hsum1 : 1 ≤ ∑ h, r h := by
    calc 1 ≤ r (⟨0, hm⟩ : Fin m) := Nat.one_le_iff_ne_zero.mpr (hrne _)
      _ ≤ ∑ h, r h := Finset.single_le_sum (fun i _ => Nat.zero_le _) (Finset.mem_univ _)
  have hsumR : (1 : ℝ) ≤ ∑ h, (r h : ℝ) := by
    have : ((∑ h, r h : ℕ) : ℝ) = ∑ h, (r h : ℝ) := by push_cast; ring
    rw [← this]; exact_mod_cast hsum1
  have hE := two_card_prod_le_card_idxBoxF r hrne hε hm2
  have hceil := ceil_siegelHeight_le r (fun _ => α₀) ((m : ℚ) / 2 - ε * (m : ℚ)) hB1
    (fun _ => hhouse) hE hC₀1 hC₀ hW
  have hC₀R : (1 : ℝ) ≤ (C₀ : ℝ) := by exact_mod_cast hC₀1
  have hWR : (1 : ℝ) ≤ (W : ℝ) := by exact_mod_cast hW1
  have hHlog : Real.log ((⌈siegelHeight r (fun _ => α₀)
        ((m : ℚ) / 2 - ε * (m : ℚ))⌉ : ℤ) : ℝ)
      ≤ (Real.log C₀ + Real.log W) * ∑ h, (r h : ℝ) := by
    have hceilR : ((⌈siegelHeight r (fun _ => α₀) ((m : ℚ) / 2 - ε * (m : ℚ))⌉ : ℤ) : ℝ)
        ≤ (C₀ : ℝ) * (W : ℝ) ^ (∑ h, r h) := by exact_mod_cast hceil
    have h1 := Real.log_le_log hHpolyPos hceilR
    rw [Real.log_mul (by linarith) (by positivity), Real.log_pow] at h1
    have hcast : ((∑ h, r h : ℕ) : ℝ) = ∑ h, (r h : ℝ) := by push_cast; ring
    rw [hcast] at h1
    nlinarith [Real.log_nonneg hC₀R, Real.log_nonneg hWR, hsumR, h1]
  have hpt := hpt_of_floor hB1 hθ0 hκB hκH hT1 hTle hTtheta
  -- 7.  `Γ_m`'s Taylor constant is positive, and the final logarithmic inequality
  have hCpos : 0 < taylorConst r ((⌈siegelHeight r (fun _ => α₀)
      ((m : ℚ) / 2 - ε * (m : ℚ))⌉ : ℤ) : ℝ) B := by
    rw [taylorConst]
    have hboxpos : (0 : ℝ) < (((∏ h, (r h + 1) : ℕ)) : ℝ) := by
      have : 0 < ∏ h, (r h + 1) := Finset.prod_pos (fun h _ => Nat.succ_pos _)
      exact_mod_cast this
    positivity
  have hfin' : (1 + θ) * ((m : ℝ) * ((1 + 1 / (k : ℝ)) * Real.log N))
      < ((2 + δ) * (1 - 1 / (k : ℝ)) * Real.log N)
        * ((((m : ℚ) / 2 - ε * (m : ℚ) : ℚ) : ℝ) - ((ν : ℚ) : ℝ)) := by
    calc (1 + θ) * ((m : ℝ) * ((1 + 1 / (k : ℝ)) * Real.log N))
        = ((1 + θ) * ((m : ℝ) * (1 + 1 / (k : ℝ)))) * Real.log N := by ring
      _ < ((2 + δ) * (1 - 1 / (k : ℝ))
            * ((((m : ℚ) / 2 - ε * (m : ℚ) : ℚ) : ℝ) - ((ν : ℚ) : ℝ))) * Real.log N :=
          mul_lt_mul_of_pos_right hfin hlogN
      _ = ((2 + δ) * (1 - 1 / (k : ℝ)) * Real.log N)
            * ((((m : ℚ) / 2 - ε * (m : ℚ) : ℚ) : ℝ) - ((ν : ℚ) : ℝ)) := by ring
  have hlog := log_condition_of_cost r (fun h => (κ h).den) hL' hθ0
    (log_taylorConst_le r (fun h => (κ h).den) hHpolyPos hB0 hHlog hpt) hfin'
  -- 8.  every hypothesis of the integer chain is now in hand
  have hεm : ((Module.finrank ℚ K : ℕ) : ℚ) < 4 * ε ^ 2 * (m : ℚ) := by
    have : (0 : ℚ) ≤ ((Module.finrank ℚ K : ℕ) : ℚ) := Nat.cast_nonneg _
    linarith
  refine roth_contradiction_int hm hp hpq hrne (fun _ => α₀) ψ hε hεm
    (card_prod_pos r hε2 hmpos) (fun h => (κ h).num) (fun h => (κ h).den) hqne
    (fun h => Real.rpow_nonneg (le_trans zero_le_one (hHR h)) _) hGT ?_ hK0 hTr hB1
    (fun _ => by linarith) ?_ hν0 hgap hg hCpos hlog
  · intro h; simp only [hfrac]; exact hκclose h
  · intro h; simp only [hfrac]; exact hκH h

end Assembly

section Slack

/-! ## The slack budget, in the product form this chain actually produces

`RothNormalisation.slack_pos` balances the budget for the *additive* shape `K = (2+δ)L`,
`L' = (1+η)L`.  The chain built here produces something slightly different: the two-sided
normalisation gives `K = (2+δ)(1−η)·log N` and `L' = (1+η)·log N`, so `η` appears **twice, with
opposite signs** — it inflates the denominators' total size and deflates the approximation
exponent.  `slack_pos`'s form sees only the first.

The budget is correspondingly tighter, and the threshold below is what it comes to: with all four
slacks below a common `t`,

    t·(16 + 5δ) < δ

is enough, and the derivation is tight to it — the surplus works out to `t + t²(3+2δ)`.  In
particular `t < δ/(16+5δ) < 1/5`, which is where the `1/2 − 2t > 0` that the whole estimate rests
on comes from.
-/

/-- **The four slacks, against `δ`.**  Step 1's shortfall `ε`, the polynomial's share `θ`, the
normalisation `η`, and Roth's `ν` measured against `m`, all below `t`, with `t(16+5δ) < δ`.

Only the *upper* bounds are needed.  I wrote `0 ≤ ε`, `0 ≤ η`, `0 ≤ νm` and `t ≤ 1` as well and the
linter reported all four unused, which is right: a negative slack is slack to spare on both sides,
and `t < 1/5` already follows from `t(16+5δ) < δ` with `t, δ > 0`.  The stronger statement is
kept. -/
theorem fin_of_slack {δ ε θ η νm t : ℝ} (hδ : 0 < δ)
    (ht0 : 0 < t) (htδ : t * (16 + 5 * δ) < δ)
    (hεt : ε ≤ t) (hθ0 : 0 ≤ θ) (hθt : θ ≤ t) (hηt : η ≤ t) (hνmt : νm ≤ t) :
    (1 + θ) * (1 + η) + (2 + δ) * (1 - η) * νm < (2 + δ) * (1 - η) * (1 / 2 - ε) := by
  have hd0 : (0 : ℝ) < 2 + δ := by linarith
  -- `t < δ/(16+5δ) < 1/5`, which is what keeps `1/2 − 2t` positive
  have ht5 : t < 1 / 5 := by nlinarith
  have hfac1 : (0 : ℝ) ≤ 1 - t := by linarith
  have hfac2 : (0 : ℝ) ≤ 1 / 2 - 2 * t := by linarith
  have h1 : (1 + θ) * (1 + η) ≤ (1 + t) * (1 + t) := by nlinarith
  have h3 : (2 + δ) * ((1 - t) * (1 / 2 - 2 * t))
      ≤ (2 + δ) * ((1 - η) * (1 / 2 - ε - νm)) :=
    mul_le_mul_of_nonneg_left
      (mul_le_mul (by linarith) (by linarith) hfac2 (by linarith)) (le_of_lt hd0)
  -- the surplus is `t + t²(3+2δ)`
  have h4 : (1 + t) * (1 + t) < (2 + δ) * ((1 - t) * (1 / 2 - 2 * t)) := by
    nlinarith [sq_nonneg t, mul_pos ht0 hδ, mul_nonneg (mul_nonneg ht0.le ht0.le) hδ.le]
  nlinarith [h1, h3, h4]

/-- **The slack form is `hfin`.**  Dividing `roth_contradiction_selected`'s last hypothesis by `m`
is what makes `ν` comparable with the other three slacks: on its own `ν` is not small — it is
bounded below by `hgap` — and only `ν/m` is. -/
theorem hfin_of_slack {δ ε θ η mR ν : ℝ} (hm : 0 < mR)
    (h : (1 + θ) * (1 + η) + (2 + δ) * (1 - η) * (ν / mR)
      < (2 + δ) * (1 - η) * (1 / 2 - ε)) :
    (1 + θ) * (mR * (1 + η)) < (2 + δ) * (1 - η) * (mR * (1 / 2 - ε) - ν) := by
  have hne : mR ≠ 0 := ne_of_gt hm
  have hscale := mul_lt_mul_of_pos_right h hm
  have key : ((1 + θ) * (1 + η) + (2 + δ) * (1 - η) * (ν / mR)) * mR
      = (1 + θ) * (mR * (1 + η)) + (2 + δ) * (1 - η) * ν := by
    field_simp
  rw [key] at hscale
  nlinarith [hscale]

/-- **Such a `t` exists.**  Pure Archimedes: the threshold `δ/(16+5δ)` is positive. -/
theorem exists_slack_bound {δ : ℝ} (hδ : 0 < δ) :
    ∃ t : ℝ, 0 < t ∧ t ≤ 1 ∧ t * (16 + 5 * δ) < δ := by
  refine ⟨min 1 (δ / (2 * (16 + 5 * δ))), lt_min zero_lt_one (by positivity), min_le_left _ _, ?_⟩
  have hden : (0 : ℝ) < 16 + 5 * δ := by linarith
  have hle : min 1 (δ / (2 * (16 + 5 * δ))) ≤ δ / (2 * (16 + 5 * δ)) := min_le_right _ _
  calc min 1 (δ / (2 * (16 + 5 * δ))) * (16 + 5 * δ)
      ≤ (δ / (2 * (16 + 5 * δ))) * (16 + 5 * δ) :=
        mul_le_mul_of_nonneg_right hle (le_of_lt hden)
    _ = δ / 2 := by field_simp
    _ < δ := by linarith

end Slack

section ParameterExistence

variable {K : Type*} [Field K] [NumberField K]

/-- **The parameters exist.**  Every hypothesis of `roth_contradiction_selected` *except the supply
`app`* is satisfiable, simultaneously, for any `δ > 0` and any `K`, `B`, `C₀`, `W`.

This is the non-vacuity check, and it is not optional.  `roth_contradiction_selected` derives
`False` from a list of conditions; a contradictory list would prove it just as well and would look
exactly the same from outside.  `app` is deliberately excluded — it *is* the negation of Roth's
theorem, so no witness for it can exist and asking for one would be asking to refute the result.

The order of choice is forced, and every step is Archimedean:

1. `t` from `exists_slack_bound` — the common bound on all four slacks.
2. `s : ℚ` below both `t` and `1/2`; it serves as `ε`, as `θ`, and as `ν/m`.
3. `k` past `1/s`, so the normalisation slack `1/k` is below `s`.
4. `m` past `[K:ℚ]/(2s²)` — the *doubled* unknowns-beat-conditions threshold.
5. `ν := s·m`.
6. `q` past `rothConstant(m)^(2^{m−1}) / ν^(2^{m−1})` at `p = 1`, then `F` from `hfloorExp`.
7. `T` past `exp((2 + log C₀W + log 4B + s·log B)/s)` and past `C₀^{mq}·W^{2m²q}`.

`ν` is the step worth naming.  `hgap` bounds it **below** and `hfin` bounds it **above**, so `ν`
cannot be made small; only `ν/m` can, which is why `hfin_of_slack`'s division by `m` is not
cosmetic.  Taking `ν = s·m` pins `ν/m` at `s` while `hgap`'s lower bound falls away as `q` grows —
the two constraints are compatible only in that order. -/
theorem exists_roth_parameters {δ : ℝ} (hδ : 0 < δ) {B : ℝ} {C₀ W : ℤ}
    (hC₀1 : 1 ≤ C₀) (hW1 : 1 ≤ W) :
    ∃ (m p q F k T : ℕ) (ε ν : ℚ) (θ : ℝ),
      1 ≤ m ∧ 0 < p ∧ p ≤ q ∧ 0 < q ∧ 1 ≤ F ∧ 1 ≤ k ∧
      q * ((m - 1) * m * (2 * m + 1)) ≤ F * p ∧
      0 < ε ∧ ε ≤ 1 / 2 ∧
      2 * ((Module.finrank ℚ K : ℕ) : ℚ) < 4 * ε ^ 2 * (m : ℚ) ∧
      0 ≤ θ ∧ 1 ≤ T ∧
      C₀ ^ (m * q) * W ^ (2 * m * m * q) ≤ (T : ℤ) ∧
      2 + (Real.log C₀ + Real.log W) + Real.log (2 * B) + Real.log 2 + θ * Real.log B
        ≤ θ * Real.log T ∧
      0 ≤ ν ∧
      (rothConstant m : ℚ) ^ (2 ^ (m - 1)) * ((p : ℚ) / (q : ℚ)) < ν ^ (2 ^ (m - 1)) ∧
      (1 + θ) * ((m : ℝ) * (1 + 1 / (k : ℝ)))
        < (2 + δ) * (1 - 1 / (k : ℝ))
          * ((((m : ℚ) / 2 - ε * (m : ℚ) : ℚ) : ℝ) - ((ν : ℚ) : ℝ)) := by
  classical
  -- 1.  the common slack bound, and 2. a rational slack below it and below `1/2`
  obtain ⟨t, ht0, -, htδ⟩ := exists_slack_bound hδ
  obtain ⟨s, hs0R, hsmin⟩ :=
    exists_rat_btwn (show (0 : ℝ) < min t (1 / 2) from lt_min ht0 (by norm_num))
  have hst : (s : ℝ) < t := lt_of_lt_of_le hsmin (min_le_left _ _)
  have hs0 : (0 : ℚ) < s := by exact_mod_cast hs0R
  have hs2 : s ≤ 1 / 2 := by
    have h : ((s : ℚ) : ℝ) < (((1 : ℚ) / 2 : ℚ) : ℝ) := by
      push_cast
      exact lt_of_lt_of_le hsmin (min_le_right _ _)
    exact le_of_lt (by exact_mod_cast h)
  -- 3.  `k` past `1/s`, so `1/k < s`
  obtain ⟨k₀, hk₀⟩ := exists_nat_gt (1 / (s : ℝ))
  set k : ℕ := max k₀ 1 with hk_def
  have hk1 : 1 ≤ k := le_max_right _ _
  have hkR : (0 : ℝ) < (k : ℝ) := by exact_mod_cast hk1
  have hks : 1 / (k : ℝ) < (s : ℝ) := by
    have hkk : (k₀ : ℝ) ≤ (k : ℝ) := by exact_mod_cast le_max_left k₀ 1
    have hlt : 1 / (s : ℝ) < (k : ℝ) := lt_of_lt_of_le hk₀ hkk
    rw [div_lt_iff₀ hs0R] at hlt
    rw [div_lt_iff₀ hkR]
    linarith
  -- 4.  `m` past the doubled threshold
  obtain ⟨m₀, hm₀⟩ := exists_nat_gt ((2 * ((Module.finrank ℚ K : ℕ) : ℚ)) / (4 * s ^ 2))
  set m : ℕ := max m₀ 1 with hm_def
  have hm1 : 1 ≤ m := le_max_right _ _
  have hmQ : (0 : ℚ) < (m : ℚ) := by exact_mod_cast hm1
  have hm2 : 2 * ((Module.finrank ℚ K : ℕ) : ℚ) < 4 * s ^ 2 * (m : ℚ) := by
    have hmm : (m₀ : ℚ) ≤ (m : ℚ) := by exact_mod_cast le_max_left m₀ 1
    have h := lt_of_lt_of_le hm₀ hmm
    rw [div_lt_iff₀ (by positivity : (0 : ℚ) < 4 * s ^ 2)] at h
    calc 2 * ((Module.finrank ℚ K : ℕ) : ℚ) < (m : ℚ) * (4 * s ^ 2) := h
      _ = 4 * s ^ 2 * (m : ℚ) := by ring
  -- 5.  `ν := s·m` — small only after division by `m`
  set ν : ℚ := s * (m : ℚ) with hν_def
  have hνpos : (0 : ℚ) < ν := mul_pos hs0 hmQ
  -- 6.  `q` at `p = 1`, then `F`
  obtain ⟨q₀, hq₀⟩ := exists_nat_gt ((rothConstant m : ℚ) ^ (2 ^ (m - 1)) / ν ^ (2 ^ (m - 1)))
  set q : ℕ := max q₀ 1 with hq_def
  have hq1 : 1 ≤ q := le_max_right _ _
  have hqQ : (0 : ℚ) < (q : ℚ) := by exact_mod_cast hq1
  have hgap : (rothConstant m : ℚ) ^ (2 ^ (m - 1)) * (((1 : ℕ) : ℚ) / (q : ℚ))
      < ν ^ (2 ^ (m - 1)) := by
    have hqq : (q₀ : ℚ) ≤ (q : ℚ) := by exact_mod_cast le_max_left q₀ 1
    have h := lt_of_lt_of_le hq₀ hqq
    rw [div_lt_iff₀ (pow_pos hνpos _)] at h
    rw [Nat.cast_one, mul_one_div, div_lt_iff₀ hqQ]
    calc (rothConstant m : ℚ) ^ (2 ^ (m - 1)) < (q : ℚ) * ν ^ (2 ^ (m - 1)) := h
      _ = ν ^ (2 ^ (m - 1)) * (q : ℚ) := mul_comm _ _
  set F : ℕ := max 1 (q * ((m - 1) * m * (2 * m + 1))) with hF_def
  -- 7.  `T` past both thresholds
  set Mexp : ℝ := (2 + (Real.log C₀ + Real.log W) + Real.log (2 * B) + Real.log 2
      + (s : ℝ) * Real.log B) / (s : ℝ) with hM_def
  obtain ⟨T₀, hT₀⟩ := exists_nat_gt (Real.exp Mexp)
  set T : ℕ := max T₀ (max 1 (C₀ ^ (m * q) * W ^ (2 * m * m * q)).toNat) with hT_def
  have hone : (1 : ℤ) ≤ C₀ ^ (m * q) * W ^ (2 * m * m * q) := by
    have h1 : (1 : ℤ) ≤ C₀ ^ (m * q) := one_le_pow₀ hC₀1
    have h2 : (1 : ℤ) ≤ W ^ (2 * m * m * q) := one_le_pow₀ hW1
    nlinarith
  have hTsiegel : C₀ ^ (m * q) * W ^ (2 * m * m * q) ≤ (T : ℤ) := by
    have hle : (C₀ ^ (m * q) * W ^ (2 * m * m * q)).toNat ≤ T :=
      le_trans (le_max_right 1 _) (le_max_right T₀ _)
    have hcast := Int.ofNat_le.mpr hle
    rwa [Int.toNat_of_nonneg (le_trans zero_le_one hone)] at hcast
  have hTtheta : 2 + (Real.log C₀ + Real.log W) + Real.log (2 * B) + Real.log 2
      + (s : ℝ) * Real.log B ≤ (s : ℝ) * Real.log T := by
    have hTle : (T₀ : ℝ) ≤ (T : ℝ) := by exact_mod_cast le_max_left T₀ _
    have hTexp : Real.exp Mexp < (T : ℝ) := lt_of_lt_of_le hT₀ hTle
    have hlogT : Mexp < Real.log T := by
      have h := Real.log_lt_log (Real.exp_pos Mexp) hTexp
      rwa [Real.log_exp] at h
    rw [hM_def, div_lt_iff₀ hs0R] at hlogT
    have hcomm : Real.log T * (s : ℝ) = (s : ℝ) * Real.log T := mul_comm _ _
    linarith
  -- the final inequality, through the slack budget
  have hmR : (0 : ℝ) < (m : ℝ) := by exact_mod_cast hm1
  have hslack := fin_of_slack (δ := δ) (ε := (s : ℝ)) (θ := (s : ℝ)) (η := 1 / (k : ℝ))
    (νm := (s : ℝ)) (t := t) hδ ht0 htδ (le_of_lt hst) (le_of_lt hs0R) (le_of_lt hst)
    (le_of_lt (lt_trans hks hst)) (le_of_lt hst)
  have hνm : ((ν : ℚ) : ℝ) / (m : ℝ) = (s : ℝ) := by
    rw [hν_def]; push_cast; field_simp
  have hfin0 : (1 + (s : ℝ)) * (1 + 1 / (k : ℝ))
      + (2 + δ) * (1 - 1 / (k : ℝ)) * (((ν : ℚ) : ℝ) / (m : ℝ))
      < (2 + δ) * (1 - 1 / (k : ℝ)) * (1 / 2 - (s : ℝ)) := by
    rw [hνm]; exact hslack
  have hfinal := hfin_of_slack hmR hfin0
  have hcast : ((((m : ℚ) / 2 - s * (m : ℚ) : ℚ)) : ℝ) = (m : ℝ) * (1 / 2 - (s : ℝ)) := by
    push_cast; ring
  exact ⟨m, 1, q, F, k, T, s, ν, (s : ℝ), hm1, one_pos, hq1, hq1, le_max_left _ _, hk1,
    by rw [mul_one]; exact le_max_right _ _, hs0, hs2, hm2, le_of_lt hs0R, 
    le_trans (le_max_left 1 _) (le_max_right T₀ _), hTsiegel, hTtheta, le_of_lt hνpos, hgap,
    by rw [hcast]; exact hfinal⟩

end ParameterExistence

section Roth

variable {K : Type*} [Field K] [NumberField K]

open private c from Mathlib.NumberTheory.NumberField.House in
/-- **Step 5 — Roth's theorem, in the "not approximable to order `2 + δ`" form.**

For a real embedding `ψ` of a number field and an algebraic integer `α₀`, there is **no** sequence
of rationals of unbounded height approximating `ψ α₀` to within `H^{-(2+δ)}`.

Everything the contradiction needs is now manufactured here rather than assumed:

* the constants — `B` above the house of `α₀` and above `|ψ α₀| + 1`, `C₀` above `c K`, `W` above
  `4B` — are ceilings, and exist because those are three real numbers;
* the parameters come from `exists_roth_parameters`, which is where the non-vacuity lives;
* the supply `S` is *defined* as the set of heights that admit a good approximation, so `app` holds
  by unfolding and `hS` is exactly the hypothesis being refuted.

⚠ **Scope.**  This is Roth for `ψ α₀` with `α₀` an algebraic *integer* of `K`.  Extending to every
real algebraic number needs one more step — clearing denominators, so that an arbitrary algebraic
`x` is `ψ α₀ / n` for some `α₀ ∈ 𝓞 K` — and the approximation exponent has to be carried across
that scaling.  That step is not done here, and the statement below says only what it proves. -/
theorem not_approximable_of_algebraic (α₀ : 𝓞 K) (ψ : K →+* ℝ) {δ : ℝ} (hδ : 0 < δ) :
    ¬ ∀ N : ℕ, ∃ κ : ℚ, N ≤ max κ.num.natAbs κ.den ∧
        |((κ : ℚ) : ℝ) - ψ ((algebraMap (𝓞 K) K) α₀)|
          ≤ ((max κ.num.natAbs κ.den : ℕ) : ℝ) ^ (-(2 + δ)) := by
  classical
  letI : DecidableEq (K →+* ℂ) := Classical.decEq _
  intro happrox
  -- the three constants, as ceilings
  set B : ℝ := max 1 (max (house ((algebraMap (𝓞 K) K) α₀))
    (|ψ ((algebraMap (𝓞 K) K) α₀)| + 1)) with hB_def
  have hB1 : 1 ≤ B := le_max_left _ _
  have hhouse : house ((algebraMap (𝓞 K) K) α₀) ≤ B :=
    le_trans (le_max_left _ _) (le_max_right _ _)
  have hψα : |ψ ((algebraMap (𝓞 K) K) α₀)| + 1 ≤ B :=
    le_trans (le_max_right _ _) (le_max_right _ _)
  set C₀ : ℤ := max 1 ⌈c K⌉ with hC_def
  have hC₀1 : (1 : ℤ) ≤ C₀ := le_max_left _ _
  have hC₀ : c K ≤ (C₀ : ℝ) := by
    have hle : ((⌈c K⌉ : ℤ) : ℝ) ≤ (C₀ : ℝ) := by exact_mod_cast le_max_right (1 : ℤ) ⌈c K⌉
    exact le_trans (Int.le_ceil _) hle
  set W : ℤ := max 1 ⌈4 * B⌉ with hW_def
  have hW1 : (1 : ℤ) ≤ W := le_max_left _ _
  have hW : 4 * B ≤ (W : ℝ) := by
    have hle : ((⌈4 * B⌉ : ℤ) : ℝ) ≤ (W : ℝ) := by exact_mod_cast le_max_right (1 : ℤ) ⌈4 * B⌉
    exact le_trans (Int.le_ceil _) hle
  -- the parameters
  obtain ⟨m, p, q, F, k, T, ε, ν, θ, hm1, hp, hpq, hq, hF, hk, hfloorExp, hε, hε2, hm2, hθ0,
    hT1, hTsiegel, hTtheta, hν0, hgap, hfin⟩ :=
    exists_roth_parameters (K := K) (B := B) hδ hC₀1 hW1
  -- the supply: the heights that admit a good approximation
  set S : Set ℕ := {Hv | ∃ κ : ℚ, max κ.num.natAbs κ.den = Hv ∧
    |((κ : ℚ) : ℝ) - ψ ((algebraMap (𝓞 K) K) α₀)| ≤ (Hv : ℝ) ^ (-(2 + δ))} with hS_def
  have hS : ∀ N, ∃ Hv ∈ S, N ≤ Hv := by
    intro N
    obtain ⟨κ, hN, hclose⟩ := happrox N
    exact ⟨max κ.num.natAbs κ.den, ⟨κ, rfl, hclose⟩, hN⟩
  exact roth_contradiction_selected hm1 hS hp hpq hq hF hk hfloorExp α₀ ψ hB1 hhouse hψα
    hε hε2 hm2 hC₀1 hC₀ hW1 hW (le_of_lt hδ) (fun _ hHv => hHv) hθ0 T hT1 hTsiegel hTtheta
    hν0 hgap hfin

end Roth

section Scaling

/-! ## Clearing denominators: what the height does under an integer multiple

`not_approximable_of_algebraic` is stated for `ψ α₀` with `α₀` an algebraic *integer*.  Reaching an
arbitrary real algebraic number goes through `IsAlgebraic.exists_integral_multiple`: some `n·x` is
integral.  So the approximation hypothesis has to be transported along `κ ↦ n·κ`, and these lemmas
are what that costs.

The scaling is **two-sided and lossy in the same factor**: `H(nκ) ≤ n·H(κ)` and `H(κ) ≤ n·H(nκ)`.
The first bounds the new height from above; the second is what keeps the transported heights
unbounded, and it does not follow from the first — without it every `nκ` could have height 1.  Both
come from one fact about an unreduced fraction, read in opposite directions.

⚠ The factor `n` is why the exponent cannot be preserved.  `|nx − nκ| = n|x − κ| ≤ n·H(κ)^{-(2+δ)}`,
and `n·H^{-(2+δ)} ≤ H^{-(2+δ')}` only once `H^{δ−δ'} ≥ n`.  The transported statement therefore
holds at every `δ' < δ` and at no `δ' = δ`; the loss is real, not slack in the estimate. -/

/-- **The height of any representation bounds the height.**  For `b ≠ 0`, reducing `a/b` divides the
numerator and the denominator, so `H(a/b) ≤ max(|a|, |b|)` whether or not `a/b` was in lowest
terms.  Both scaling bounds are this lemma at a different representation. -/
theorem height_divInt_le {a b : ℤ} (hb : b ≠ 0) :
    max (Rat.divInt a b).num.natAbs (Rat.divInt a b).den ≤ max a.natAbs b.natAbs := by
  have hden : (Rat.divInt a b).den ≤ b.natAbs := by
    have hdvd : (((Rat.divInt a b).den : ℤ)) ∣ b := Rat.den_dvd a b
    have hle := Nat.le_of_dvd (Int.natAbs_pos.mpr hb) (Int.natAbs_dvd_natAbs.mpr hdvd)
    rwa [Int.natAbs_natCast] at hle
  refine max_le ?_ (le_trans hden (le_max_right _ _))
  rcases eq_or_ne a 0 with rfl | ha
  · simp
  · exact le_trans (Nat.le_of_dvd (Int.natAbs_pos.mpr ha)
      (Int.natAbs_dvd_natAbs.mpr (Rat.num_dvd a hb))) (le_max_left _ _)

/-- **`H(nκ) ≤ n·H(κ)`**, from the representation `nκ = (n·κ.num)/κ.den`. -/
theorem height_nsmul_le {n : ℕ} (hn : 0 < n) (κ : ℚ) :
    max (((n : ℚ) * κ).num.natAbs) (((n : ℚ) * κ).den)
      ≤ n * max κ.num.natAbs κ.den := by
  have hden0 : ((κ.den : ℕ) : ℤ) ≠ 0 := Int.natCast_ne_zero.mpr κ.den_nz
  have hrepr : ((n : ℚ) * κ) = Rat.divInt ((n : ℤ) * κ.num) ((κ.den : ℕ) : ℤ) := by
    rw [Rat.divInt_eq_div]
    conv_lhs => rw [← Rat.num_div_den κ]
    push_cast
    ring
  rw [hrepr]
  refine le_trans (height_divInt_le hden0) ?_
  rw [Int.natAbs_mul, Int.natAbs_natCast, Int.natAbs_natCast]
  refine max_le (Nat.mul_le_mul_left n (le_max_left _ _)) ?_
  calc κ.den ≤ max κ.num.natAbs κ.den := le_max_right _ _
    _ = 1 * max κ.num.natAbs κ.den := (one_mul _).symm
    _ ≤ n * max κ.num.natAbs κ.den := Nat.mul_le_mul_right _ hn

/-- **`H(κ) ≤ n·H(nκ)`**, from the representation `κ = (nκ).num / (n·(nκ).den)`.  This is the half
that keeps the transported heights unbounded. -/
theorem height_le_height_nsmul {n : ℕ} (hn : 0 < n) (κ : ℚ) :
    max κ.num.natAbs κ.den ≤ n * max (((n : ℚ) * κ).num.natAbs) (((n : ℚ) * κ).den) := by
  have hn0 : (n : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hn.ne'
  have hnZ : (n : ℤ) ≠ 0 := Int.natCast_ne_zero.mpr hn.ne'
  have hD0 : (((((n : ℚ) * κ).den : ℕ)) : ℚ) ≠ 0 := by
    exact_mod_cast ((n : ℚ) * κ).den_nz
  have hd0 : ((n : ℤ) * ((((n : ℚ) * κ).den : ℕ) : ℤ)) ≠ 0 :=
    mul_ne_zero hnZ (Int.natCast_ne_zero.mpr ((n : ℚ) * κ).den_nz)
  have hrepr : κ = Rat.divInt (((n : ℚ) * κ).num) ((n : ℤ) * ((((n : ℚ) * κ).den : ℕ) : ℤ)) := by
    have hAD := Rat.num_div_den ((n : ℚ) * κ)
    rw [div_eq_iff hD0] at hAD
    rw [Rat.divInt_eq_div]
    push_cast
    rw [hAD]
    field_simp
  conv_lhs => rw [hrepr]
  refine le_trans (height_divInt_le hd0) ?_
  rw [Int.natAbs_mul, Int.natAbs_natCast, Int.natAbs_natCast]
  refine max_le ?_ (Nat.mul_le_mul_left n (le_max_right _ _))
  calc (((n : ℚ) * κ).num).natAbs
      ≤ max (((n : ℚ) * κ).num.natAbs) (((n : ℚ) * κ).den) := le_max_left _ _
    _ = 1 * max (((n : ℚ) * κ).num.natAbs) (((n : ℚ) * κ).den) := (one_mul _).symm
    _ ≤ n * max (((n : ℚ) * κ).num.natAbs) (((n : ℚ) * κ).den) := Nat.mul_le_mul_right _ hn

/-- **Every rational has height at least 1**, because its denominator does. -/
theorem one_le_height (κ : ℚ) : 1 ≤ max κ.num.natAbs κ.den :=
  le_trans κ.pos (le_max_right _ _)

/-- **Approximability transports along an integer multiple, at a strictly smaller exponent.**  If
`x` admits rational approximations of unbounded height to order `2 + δ`, then `n·x` admits them to
order `2 + δ'` for every `δ' < δ`.

The whole argument is linear once written in logarithms, which is why it is written that way here:
the condition is `(3 + δ')·log n ≤ (δ − δ')·log H`, so the threshold fed to the hypothesis is
`exp((3+δ')·log n / (δ−δ'))`, and both height bounds enter as `log H(nκ) ≤ log n + log H(κ)` and
`H(κ) ≤ n·H(nκ)`.  Nothing here needs the monotonicity of `x ↦ x^c` for negative `c`. -/
theorem approximable_nsmul {x : ℝ} {n : ℕ} (hn : 0 < n) {δ δ' : ℝ} (hδ'0 : 0 < δ') (hlt : δ' < δ)
    (h : ∀ N : ℕ, ∃ κ : ℚ, N ≤ max κ.num.natAbs κ.den ∧
        |((κ : ℚ) : ℝ) - x| ≤ ((max κ.num.natAbs κ.den : ℕ) : ℝ) ^ (-(2 + δ))) :
    ∀ N : ℕ, ∃ κ : ℚ, N ≤ max κ.num.natAbs κ.den ∧
        |((κ : ℚ) : ℝ) - (n : ℝ) * x| ≤ ((max κ.num.natAbs κ.den : ℕ) : ℝ) ^ (-(2 + δ')) := by
  intro N
  have hnR : (0 : ℝ) < (n : ℝ) := by exact_mod_cast hn
  have hn1 : (1 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
  have hδd : (0 : ℝ) < δ - δ' := by linarith
  obtain ⟨N₀, hN₀⟩ :=
    exists_nat_gt (max (Real.exp ((3 + δ') * Real.log n / (δ - δ'))) ((n * N : ℕ) : ℝ))
  obtain ⟨κ, hNκ, hclose⟩ := h N₀
  refine ⟨(n : ℚ) * κ, ?_, ?_⟩
  · -- the transported height is still at least `N`, via `H(κ) ≤ n·H(nκ)`
    have hbig : n * N ≤ max κ.num.natAbs κ.den := by
      have h1 : ((n * N : ℕ) : ℝ) < (N₀ : ℝ) := lt_of_le_of_lt (le_max_right _ _) hN₀
      have h2 : n * N ≤ N₀ := by exact_mod_cast le_of_lt h1
      exact le_trans h2 hNκ
    have hmul := height_le_height_nsmul hn κ
    have : n * N ≤ n * max (((n : ℚ) * κ).num.natAbs) (((n : ℚ) * κ).den) :=
      le_trans hbig hmul
    exact Nat.le_of_mul_le_mul_left this hn
  · -- the exponent, in logarithms
    set Hk : ℝ := ((max κ.num.natAbs κ.den : ℕ) : ℝ) with hHk_def
    set Hn : ℝ := ((max (((n : ℚ) * κ).num.natAbs) (((n : ℚ) * κ).den) : ℕ) : ℝ) with hHn_def
    have hHk1 : (1 : ℝ) ≤ Hk := by rw [hHk_def]; exact_mod_cast one_le_height κ
    have hHn1 : (1 : ℝ) ≤ Hn := by rw [hHn_def]; exact_mod_cast one_le_height ((n : ℚ) * κ)
    have hHk0 : (0 : ℝ) < Hk := lt_of_lt_of_le zero_lt_one hHk1
    have hHn0 : (0 : ℝ) < Hn := lt_of_lt_of_le zero_lt_one hHn1
    -- `|nκ − nx| = n·|κ − x|`
    have habs : |(((n : ℚ) * κ : ℚ) : ℝ) - (n : ℝ) * x| = (n : ℝ) * |((κ : ℚ) : ℝ) - x| := by
      have hcast : (((n : ℚ) * κ : ℚ) : ℝ) = (n : ℝ) * ((κ : ℚ) : ℝ) := by push_cast; ring
      rw [hcast, ← mul_sub, abs_mul, abs_of_pos hnR]
    -- the threshold, in logarithms
    have hHkN : (N₀ : ℝ) ≤ Hk := by rw [hHk_def]; exact_mod_cast hNκ
    have hexp : Real.exp ((3 + δ') * Real.log n / (δ - δ')) < Hk :=
      lt_of_lt_of_le (lt_of_le_of_lt (le_max_left _ _) hN₀) hHkN
    have hlogHk : (3 + δ') * Real.log n / (δ - δ') < Real.log Hk := by
      have hh := Real.log_lt_log (Real.exp_pos _) hexp
      rwa [Real.log_exp] at hh
    have hkey : (3 + δ') * Real.log n ≤ (δ - δ') * Real.log Hk := by
      rw [div_lt_iff₀ hδd] at hlogHk
      nlinarith [hlogHk]
    -- `log H(nκ) ≤ log n + log H(κ)`
    have hHnle : Hn ≤ (n : ℝ) * Hk := by
      rw [hHn_def, hHk_def]; exact_mod_cast height_nsmul_le hn κ
    have hlogHn : Real.log Hn ≤ Real.log n + Real.log Hk := by
      calc Real.log Hn ≤ Real.log ((n : ℝ) * Hk) := Real.log_le_log hHn0 hHnle
        _ = Real.log n + Real.log Hk := Real.log_mul (ne_of_gt hnR) (ne_of_gt hHk0)
    -- assemble
    rw [habs]
    refine le_trans (mul_le_mul_of_nonneg_left hclose (le_of_lt hnR)) ?_
    rw [hHk_def] at *
    rw [Real.rpow_def_of_pos hHk0, Real.rpow_def_of_pos hHn0,
      show (n : ℝ) = Real.exp (Real.log n) from (Real.exp_log hnR).symm, ← Real.exp_add]
    refine Real.exp_le_exp.mpr ?_
    have hneg : (-(2 + δ') : ℝ) ≤ 0 := by linarith
    have hstep : Real.log Hn * (-(2 + δ')) ≥ (Real.log n + Real.log Hk) * (-(2 + δ')) :=
      mul_le_mul_of_nonpos_right hlogHn hneg
    nlinarith [hstep, hkey]

end Scaling

end MvPolynomial
