/-
# The Borromean (Brunnian) irreducible 3-body cluster is non-negative
# — the forward complement of the `Mu4RhoFCluster` multiplicative sign wall.

Companion to `QOU.MassTheory.Mu4RhoFCluster` (#4354), which proved a 3-body
**sign wall**: the beyond-pairwise content of any *multiplicative* interface
product `1 − ∏ᵢ fᵢ` (`fᵢ ∈ [0,1]`) is `≤ 0` (`pairwise_3body_content_nonpos`),
while the Δ_λ residual simplex needs `μ₃ = +0.4708 > 0`.  The standing open door
was a **non-multiplicative, enhancing** 3-body operator.

**This file: the Borromean operator supplies the forbidden `+` sign, structurally.**
The Borromean rings `𝓑₃` are the archetype of a *Brunnian* 3-body object — three
components, every 2-sub-link *trivial*, yet the whole genuinely 3-body linked.
So the pairwise (multiplicative) content **vanishes by construction**, and the
whole binding content is the irreducible 3-body cluster.  Its magnitude is the
`H₃` Markov-trace deficit against the 3-component unlink (`τ_free = τ(0) = 1`),
using the GAP-A-4 closed form (`QOU.BraidsAndKnots.BorromeanMarkovTrace`)

    τ_Borr(h) = (4 + h² − 3h⁴ − h⁶)/(h² + 4),   h = q − q⁻¹.

The deficit has the closed form `1 − τ_Borr = h⁴(3 + h²)/(h² + 4) ≥ 0` for every
real `h`, strictly `> 0` for `h ≠ 0` (`q ≠ 1`).  Hence the Borromean cluster
`c₃ = E₀·(1 − τ_Borr) ≥ 0` (`> 0` in the physical regime) — the sign
`Mu4RhoFCluster.pairwise_3body_content_nonpos` (`≤ 0`) provably cannot give.
The `μ₃ > 0` sign therefore **selects** the Brunnian (non-multiplicative) operator.

This is a **scope-(a) sign lead, not a Δ_λ closure**: it fixes the *sign*, not
the per-λ magnitude (bare-`H₃` scale `~0.006 MeV` ≪ the `+0.4708`/`~1.5 MeV`
target; any level-lift tuned to the target would be a FIT and is not made here).

Probe: `computations/deltalambda/borromean_3body_cluster_sign_probe.py`.
Anti-fit: only the derived closed form + its sign are used; `μ₃` enters nowhere
in any proof below; nothing is wired.

Base ring (§7c): `ℝ` is used because the statements are *ordering* facts
(`≤ 1`, `0 <`), archimedean by nature.  The algebraic identity
`one_sub_tauBorromean` holds over any field but is stated over `ℝ` for uniformity
with the positivity lemmas it feeds.
-/
import Mathlib.Tactic

namespace QOU.MassTheory

/-! ### The Borromean `H₃` Markov trace and its unlink deficit -/

/-- The Borromean `H₃` Markov-trace closed form (GAP-A-4,
`QOU.BraidsAndKnots.BorromeanMarkovTrace`), as a function of `h = q − q⁻¹`:
`τ_Borr(h) = (4 + h² − 3h⁴ − h⁶)/(h² + 4)`.  Amphichiral ⇒ even in `h`. -/
noncomputable def tauBorromean (h : ℝ) : ℝ := (4 + h ^ 2 - 3 * h ^ 4 - h ^ 6) / (h ^ 2 + 4)

/-- The 3-component unlink is `τ_Borr(0) = 1` (writhe-0 trivial eigenvalue). -/
theorem tauBorromean_zero : tauBorromean 0 = 1 := by
  unfold tauBorromean; norm_num

/-- **Trace-deficit closed form.**  `1 − τ_Borr = h⁴(3 + h²)/(h² + 4)`.  This is
the irreducible 3-body content: the Borromean trace measured against the unlink
`τ(0) = 1`.  (Being Brunnian, no pairwise part is subtracted — it vanishes.) -/
theorem one_sub_tauBorromean (h : ℝ) :
    1 - tauBorromean h = h ^ 4 * (3 + h ^ 2) / (h ^ 2 + 4) := by
  unfold tauBorromean
  have hd : h ^ 2 + 4 ≠ 0 := by positivity
  field_simp
  ring

/-! ### Positivity: the deficit (hence the cluster) is non-negative -/

/-- **The Borromean trace lies at or below the unlink value `1`** for every real
`h`.  (`h⁴ ≥ 0`, `3 + h² > 0`, `h² + 4 > 0` ⇒ the deficit `≥ 0`.) -/
theorem tauBorromean_le_one (h : ℝ) : tauBorromean h ≤ 1 := by
  have hdef : 1 - tauBorromean h = h ^ 4 * (3 + h ^ 2) / (h ^ 2 + 4) := one_sub_tauBorromean h
  have hpos : 0 ≤ h ^ 4 * (3 + h ^ 2) / (h ^ 2 + 4) := by positivity
  linarith

/-- **Strictly below `1` for `h ≠ 0`** (the physical regime `q ≠ 1`). -/
theorem tauBorromean_lt_one {h : ℝ} (hh : h ≠ 0) : tauBorromean h < 1 := by
  have hdef : 1 - tauBorromean h = h ^ 4 * (3 + h ^ 2) / (h ^ 2 + 4) := one_sub_tauBorromean h
  have hh2 : 0 < h ^ 2 := by positivity
  have h4 : 0 < h ^ 4 := by nlinarith [mul_pos hh2 hh2]
  have hnum : 0 < h ^ 4 * (3 + h ^ 2) := mul_pos h4 (by positivity)
  have hden : 0 < h ^ 2 + 4 := by positivity
  have hpos : 0 < h ^ 4 * (3 + h ^ 2) / (h ^ 2 + 4) := div_pos hnum hden
  linarith

/-- **(LEAD) The Borromean irreducible 3-body cluster is non-negative.**  For a
non-negative energy scale `E₀`, the Brunnian binding cluster
`c₃ = E₀·(1 − τ_Borr)` is `≥ 0` — the forward complement of
`Mu4RhoFCluster.pairwise_3body_content_nonpos` (which is `≤ 0`).  This is the
sign the *multiplicative* pairwise route provably cannot supply. -/
theorem borromean_cluster_nonneg {E0 h : ℝ} (hE : 0 ≤ E0) :
    0 ≤ E0 * (1 - tauBorromean h) :=
  mul_nonneg hE (by linarith [tauBorromean_le_one h])

/-- **(LEAD, strict) `c₃ > 0` in the physical regime** (`E₀ > 0`, `q ≠ 1`).  So
the Borromean cluster is *sign-compatible* with `μ₃ > 0` — unlike any pairwise
interface product (`Mu4RhoFCluster.mu3_ne_pairwise_3body_cluster`). -/
theorem borromean_cluster_pos {E0 h : ℝ} (hE : 0 < E0) (hh : h ≠ 0) :
    0 < E0 * (1 - tauBorromean h) :=
  mul_pos hE (by linarith [tauBorromean_lt_one hh])

/-- **Sign selection.**  The residual moment `μ₃ > 0` and the Borromean cluster
`c₃ = E₀·(1 − τ_Borr) > 0` (physical regime) lie on the *same* strictly-positive
side — so the Brunnian operator is sign-compatible with `μ₃`.  Contrast
`Mu4RhoFCluster.mu3_ne_pairwise_3body_cluster`, where the `≤ 0` pairwise content
is sign-*incompatible* with the same `μ₃`.  (This fixes the *sign* only; it makes
no magnitude claim — `μ₃`'s value enters neither statement nor proof.) -/
theorem mu3_sign_compatible_with_borromean_cluster {μ₃ E0 h : ℝ}
    (hμ : 0 < μ₃) (hE : 0 < E0) (hh : h ≠ 0) :
    0 < μ₃ ∧ 0 < E0 * (1 - tauBorromean h) :=
  ⟨hμ, borromean_cluster_pos hE hh⟩

end QOU.MassTheory
