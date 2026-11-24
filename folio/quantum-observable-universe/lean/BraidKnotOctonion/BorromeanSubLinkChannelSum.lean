/-
# The A=3 magnitude factor `r* ≈ 1.585` is NOT supplied by the multi-sub-link
# channel decomposition — Brunnian triviality collapses every sub-link channel.

ROUTE 3 of the A=3 magnitude cross-channel program (companion to the sibling
operator-branching (ROUTE 1) and super-Berezinian (ROUTE 2) attacks).

## The gap

`#4364` lifted the derived A=3 3-body cluster to the `H₉` joint-trace level and
reached the **complete finite-type sum of the ONE Borromean deficit**
`c₃ = E₀·(1 − τ_Borr) = +0.297 MeV = 0.63× μ₃` — a `~1.6×` near-miss against the
derived target `μ₃ = +0.4708` (`AdditiveResidualSimplex`, #4320).  Every single
probe (level / geometric-`W_λ` / edge / exact-order / Vassiliev-weight) was a
**re-weighting of the one 3-body Borromean trace** and all bracket the missing
magnitude factor `r* = μ₃/c₃ ≈ 1.585` out (`docs/coordination/option-e.md`).

## The channel-sum reading (this file)

The triton is 3 nucleons = **three 2-body sub-channels PLUS the 3-body
Borromean** link.  A genuinely *many-body* object different from every bracketed
re-weighting: a sum over the **distinct** sub-link trace objects (three pairwise
2-sub-links + the triple), not a reweighting of one.  Two candidate closures:

* additive         `Σ = f₁₂ + f₁₃ + f₂₃ + f₁₂₃`,
* multiplicative   `C = 1 − ∏ᵢ(1 − fᵢ)`   (interface-product / Ursell form),

where each sub-link deficit `fᵢ = 1 − τ(sub-linkᵢ)` is measured against that
sub-link's own unlink baseline (unit-normalized, matching the corpus convention
`one_sub_tauBorromean`, so `τ_unlink = 1`).

## Why it is REFUTED — scope-(b), Brunnian sub-link triviality (invariant cited)

The Borromean rings `𝓑₃` are the **archetype Brunnian** link: *every proper
2-sub-link is the unlink* (delete any one of the three components and the
remaining two fall apart).  In the band-word model
`w₃ = [A₀₁, A₁₂] = A₀₁ A₁₂ A₀₁⁻¹ A₁₂⁻¹`, forgetting any single strand deletes one
commutator argument, so the 2-sub-word freely reduces to the **empty word**
(engine-verified, `borromean_sublink_channel_sum_probe.py`).  The empty word's
Markov trace equals the unlink baseline, so **each pairwise deficit is exactly
`fᵢ = 0`** — not small, identically zero.

Consequently *both* closures collapse to the single Borromean triple deficit:

* `brunnian_channelSumAdd_eq_triple`     — additive sum `= 1 − τ₁₂₃`,
* `brunnian_channelClosureMul_eq_triple` — **the multiplicative closure's cross
  terms all vanish** (each factor `1 − fᵢ = 1`), also `= 1 − τ₁₂₃`.

This is exactly the AGENTS.md "compositional/trace object is already many-body"
caveat *turned decisive*: the caveat warns a "pairwise can't do it" argument is a
category error *when the pairwise deficits are nonzero* (then `1 − ∏(1−fᵢ)`
carries live cross terms measuring a missing higher term).  Here the pairwise
deficits are **provably zero** (Brunnian), so the cross terms are zero and the
channel decomposition supplies **magnitude factor exactly `1`** — it collapses
back onto `c₃` and adds nothing.  `brunnian_channel_no_magnitude`: the closure
equals `r*·c₃` only in the degenerate `c₃ = 0`; for the derived `r* ≈ 1.585 ≠ 1`
and the physical `c₃ > 0` (`h ≠ 0`), it never does
(`borromean_channelClosure_eq_c3` + `borromean_channel_ne_r_star`).

**Verdict: WALL (scope-b) — the sub-link channel sum cannot supply `r*`.  The
invariant is Brunnian sub-link triviality; the missing A=3 magnitude is NOT in
the sub-link decomposition of the Borromean triton model.**  (A *non*-Brunnian
3-component model with linked pairs would give nonzero pairwise channels, but
that is a different, non-canonical link choice; selecting one whose sub-link
weighting hits `1.585` would be a FIT and is not made here.)

Anti-fit: only the derived closed form + the Brunnian invariant are used; `μ₃`
enters no proof; nothing is wired.

Base ring (§7c): generic `[CommRing R]` for the algebraic collapse identities;
`[IsDomain R]` only for the cancellation in `brunnian_channel_no_magnitude`; `ℝ`
only for the concrete positivity corollary `borromean_channel_ne_r_star`.
-/
import Mathlib.Tactic

namespace QOU.MassTheory

section Generic

variable {R : Type*} [CommRing R]

/-- Normalized trace deficit of a sub-link against its unit unlink baseline
(corpus convention, matches `BorromeanThreeBodyCluster.one_sub_tauBorromean`):
`f = 1 − τ`.  So `τ = τ_unlink = 1 ⇒ f = 0`. -/
def deficit (τ : R) : R := 1 - τ

/-- Additive sub-link channel sum over the three 2-sub-links + the triple. -/
def channelSumAdd (τ12 τ13 τ23 τ123 : R) : R :=
  deficit τ12 + deficit τ13 + deficit τ23 + deficit τ123

/-- Multiplicative sub-link channel closure `1 − ∏ᵢ(1 − fᵢ)` (interface-product
/ Ursell form).  Written verbatim in the `1 − ∏(1 − fᵢ)` shape so the cross-term
structure is visible; the pairwise cross terms are what Brunnian triviality
kills. -/
def channelClosureMul (τ12 τ13 τ23 τ123 : R) : R :=
  1 - (1 - deficit τ12) * (1 - deficit τ13) * (1 - deficit τ23) * (1 - deficit τ123)

/-- **Brunnian collapse (additive).**  Every proper 2-sub-link of `𝓑₃` is the
unlink (`τ₁₂ = τ₁₃ = τ₂₃ = 1`), so its deficit vanishes and the additive channel
sum equals the single 3-body Borromean deficit. -/
theorem brunnian_channelSumAdd_eq_triple (τ123 : R) :
    channelSumAdd 1 1 1 τ123 = deficit τ123 := by
  unfold channelSumAdd deficit; ring

/-- **Brunnian collapse (multiplicative) — the decisive identity.**  With the
three pairwise deficits `= 0`, *every cross term of* `1 − ∏(1 − fᵢ)` *vanishes*
(each factor `1 − fᵢ = 1`), so the multiplicative closure also equals the single
3-body deficit.  This is why the interface-product's "beyond-pairwise content"
supplies nothing here: the pairwise factors are identically the unlink. -/
theorem brunnian_channelClosureMul_eq_triple (τ123 : R) :
    channelClosureMul 1 1 1 τ123 = deficit τ123 := by
  unfold channelClosureMul deficit; ring

/-- Under Brunnian triviality the additive and multiplicative closures agree —
both are the single Borromean deficit, no channel structure survives. -/
theorem brunnian_closures_agree (τ123 : R) :
    channelSumAdd 1 1 1 τ123 = channelClosureMul 1 1 1 τ123 := by
  rw [brunnian_channelSumAdd_eq_triple, brunnian_channelClosureMul_eq_triple]

end Generic

section Domain

variable {R : Type*} [CommRing R] [IsDomain R]

/-- **No magnitude (the refutation).**  The Brunnian sub-link channel closure
equals the single Borromean deficit, so it reproduces a target `r*·c₃`
(`c₃ = deficit τ₁₂₃`) with `r* ≠ 1` *only* in the degenerate `c₃ = 0`.  For the
derived A=3 factor `r* = μ₃/c₃ ≈ 1.585 ≠ 1` and any nonzero deficit, the channel
decomposition cannot supply it: it contributes magnitude factor exactly `1`. -/
theorem brunnian_channel_no_magnitude
    (τ123 rstar : R) (hr : rstar ≠ 1)
    (h : channelClosureMul 1 1 1 τ123 = rstar * deficit τ123) :
    deficit τ123 = 0 := by
  rw [brunnian_channelClosureMul_eq_triple] at h
  have hz : (1 - rstar) * deficit τ123 = 0 := by linear_combination h
  rcases mul_eq_zero.mp hz with h1 | h2
  · exact absurd (sub_eq_zero.mp h1).symm hr
  · exact h2

end Domain

section Borromean

/-- **Concrete: the channel closure over the `𝓑₃` sub-links equals exactly `c₃`.**
Plugging the derived Borromean triple trace
`τ_Borr(h) = (4 + h² − 3h⁴ − h⁶)/(h² + 4)` (GAP-A-4 closed form;
`BorromeanThreeBodyCluster.tauBorromean`) into the three-unlink-pairwise +
triple channel closure reproduces the `#4364` near-miss deficit
`1 − τ_Borr = h⁴(3 + h²)/(h² + 4)` — the `0.297 MeV`, `0.63× μ₃` value — with **no
magnitude factor**. -/
theorem borromean_channelClosure_eq_c3 (h : ℝ) :
    channelClosureMul 1 1 1 ((4 + h ^ 2 - 3 * h ^ 4 - h ^ 6) / (h ^ 2 + 4))
      = h ^ 4 * (3 + h ^ 2) / (h ^ 2 + 4) := by
  rw [brunnian_channelClosureMul_eq_triple]
  unfold deficit
  have hd : h ^ 2 + 4 ≠ 0 := by positivity
  field_simp; ring

/-- **Concrete refutation.**  In the physical regime (`h ≠ 0`, so `c₃ > 0`) the
Brunnian channel closure `= c₃` never equals `r*·c₃` for the derived
`r* ≈ 1.585 ≠ 1`.  The missing A=3 magnitude is not in the sub-link
decomposition. -/
theorem borromean_channel_ne_r_star {h rstar : ℝ} (hh : h ≠ 0) (hr : rstar ≠ 1) :
    channelClosureMul 1 1 1 ((4 + h ^ 2 - 3 * h ^ 4 - h ^ 6) / (h ^ 2 + 4))
      ≠ rstar * (h ^ 4 * (3 + h ^ 2) / (h ^ 2 + 4)) := by
  rw [borromean_channelClosure_eq_c3]
  have hden : (0 : ℝ) < h ^ 2 + 4 := by positivity
  have h4 : (0 : ℝ) < h ^ 4 := by positivity
  have hnum : (0 : ℝ) < h ^ 4 * (3 + h ^ 2) := mul_pos h4 (by positivity)
  have hc3 : (0 : ℝ) < h ^ 4 * (3 + h ^ 2) / (h ^ 2 + 4) := div_pos hnum hden
  intro hcontra
  -- c₃ = r*·c₃ with c₃ > 0 ⇒ r* = 1, contradicting hr
  have hz : (1 - rstar) * (h ^ 4 * (3 + h ^ 2) / (h ^ 2 + 4)) = 0 := by
    linear_combination hcontra
  rcases mul_eq_zero.mp hz with h1 | h2
  · exact absurd (sub_eq_zero.mp h1).symm hr
  · exact absurd h2 (ne_of_gt hc3)

end Borromean

end QOU.MassTheory
