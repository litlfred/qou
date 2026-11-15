import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.BigOperators.Field
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# What the depth-stratified binding functional REQUIRES of its weight family

Formalize-first companion to bean `qou-oots` and
`docs/audits/2026-09-05-phi-k-weight-family.md`. The functional under study is

  `Φ_k(β) = Σ_{λ : depth k} w_λ · log(|χ^λ(β)| · d_q λ)`,
  `B      = Σ_k α_k · (Φ_k(free) − Φ_k(atom))`,

and the open question is which weight family `w_λ` it should carry — four are
live in the corpus (`d_q²/[n]_q!`, `d_q²/D²`, the Molien `f^λ q^{−κ_λ} d_q`,
and the Markov/Ocneanu `y_λ`). Rather than survey them, this file derives what
the functional actually *needs*, so the survey becomes a prune.

Three structural facts, each of which retires or fails to retire a candidate:

* `phiDiff_eq_sum_log_ratio` — **the `d_q λ` inside the logarithm cancels.**
  `Φ_k` never appears alone; only the difference `Φ_k(free) − Φ_k(atom)` is
  observable, and free and atom are summed over the *same* index set with the
  *same* weights. So `B` is a `w`-weighted mean of `log|χ^λ(free)/χ^λ(atom)|`
  — a weighted geometric mean of character ratios, and nothing else. In
  particular `B` is **not linear** in the braid-group algebra element: it is not
  a trace, so no Markov property can be required of, or inherited by, `w`.

* `phiDiff_smul` / `crossRatio_smul` — **a λ-independent rescale of `w` passes
  straight through to `B`, and cancels only WITHIN one nucleus.** The scored
  quantity is `B(A)/B_exp(A)` compared across nuclei of different `A`, and
  `n = 3A`, so a normaliser that varies with `n` moves the cross-nucleus metric
  by exactly the ratio of its two values (`crossRatio_smul`). Hence the
  requirement is *`n`-independence of the total mass*, which is weaker than
  "probability measure" but is a genuine requirement. (Companion:
  `WLambdaNormalizationInvariance.ratio_invariant` proves the *same-`n`* ratio
  is invariant — this file supplies the cross-`n` complement, which is where
  the choice bites.)

* `phi_eq_zero_of_weights_vanish` — **a weight family that vanishes on the
  depth-`k` stratum makes `Φ_k` identically zero**, whatever the characters.
  This is the invariant that retires `y_λ` for `k ≥ N`: at `N = 2` the
  hook-content row cap (`Eightfold.RowCapObstruction`; `[N + c]_q = [0]_q = 0`
  at the cell of content `−N`) forces `y_λ = 0` for every `λ` with more than
  `N` rows, i.e. for every `λ` of depth `≥ N`. The depth-3 chirality channel
  the FR-pullback test probes is therefore *vacuous* under `y_λ`.

Everything here is a real-analysis / field identity over `ℝ` (`log` is
archimedean, §7c) with abstract `w`, `a`, `b`, `c` — no `q₀`, no anchor, no
character theory. The statements bound the numerical companion probe
(`computations/probes/phi_k_weight_family_discriminator.py`) *in advance*.

LaTeX label: `prop:phi-k-weight-family-requirements`

## References

- [leitner2026] docs/audits/2026-09-05-phi-k-weight-family.md (the requirement derivation + prune)
- [leitner2026] docs/audits/2026-09-04-plancherel-convention-gap.md (the `c_n` cross-atom artifact)
- [leitner2026] content/.../lean/QOU/BraidKnot/WLambdaNormalizationInvariance.lean (same-`n` invariance)
- [leitner2026] content/.../lean/QOU/Eightfold/RowCapObstruction.lean (the `y_λ` row cap)
-/

namespace QOU.BraidKnot.DepthWeightReq

open Finset

variable {ι : Type*}

/-- The depth-stratum functional `Φ = Σ_{λ ∈ s} w_λ · log(m_λ · c_λ)`, with
`m_λ = |χ^λ(β)|` the character magnitude and `c_λ = d_q(λ)` the q-dimension
factor the corpus form carries inside the logarithm. -/
noncomputable def phi (s : Finset ι) (w m c : ι → ℝ) : ℝ :=
  ∑ l ∈ s, w l * Real.log (m l * c l)

/-- **The `d_q` factor inside the logarithm cancels in the observable.**
`Φ(free) − Φ(atom) = Σ_λ w_λ · log(m_free λ / m_atom λ)`: the common factor
`c_λ` — here the quantum dimension — contributes nothing, because free and atom
are summed over the same stratum with the same weights.

Consequence (the reason this is the first lemma): `B` is a `w`-weighted mean of
log character-ratios, hence **not a linear functional of the braid element**, so
it is not a trace and the Markov property is not a requirement on `w`. -/
theorem phiDiff_eq_sum_log_ratio (s : Finset ι) (w mf ma c : ι → ℝ)
    (hf : ∀ l ∈ s, mf l ≠ 0) (ha : ∀ l ∈ s, ma l ≠ 0) (hc : ∀ l ∈ s, c l ≠ 0) :
    phi s w mf c - phi s w ma c = ∑ l ∈ s, w l * Real.log (mf l / ma l) := by
  unfold phi
  rw [← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl fun l hl => ?_
  rw [Real.log_mul (hf l hl) (hc l hl), Real.log_mul (ha l hl) (hc l hl),
    Real.log_div (hf l hl) (ha l hl)]
  ring

/-- **A λ-independent rescale of the weights rescales the observable.**
`Φ` is linear in `w`, so `w → k · w` sends `Φ(free) − Φ(atom)` to
`k · (Φ(free) − Φ(atom))`. Within one nucleus this is a global factor and
cancels out of any ratio; across nuclei it does not, because `k` is a function
of `n = 3A`. -/
theorem phiDiff_smul (s : Finset ι) (w mf ma c : ι → ℝ) (k : ℝ) :
    phi s (fun l => k * w l) mf c - phi s (fun l => k * w l) ma c
      = k * (phi s w mf c - phi s w ma c) := by
  have h : ∀ m : ι → ℝ, phi s (fun l => k * w l) m c = k * phi s w m c := by
    intro m
    unfold phi
    rw [Finset.mul_sum]
    exact Finset.sum_congr rfl fun l _ => by ring
  rw [h mf, h ma, mul_sub]

/-- **The cross-nucleus metric moves by exactly the ratio of the two
normalisers.** With `B₁, B₂` the predictions for two nuclei and `E₁, E₂` their
experimental values, the scored cross-nucleus quantity is
`(B₁/E₁)/(B₂/E₂)`. Rescaling the weights of nucleus `i` by `kᵢ` multiplies it
by `k₁/k₂`.

So the requirement is **not** that `Σ_λ w_λ = 1`, but that the normaliser be
the *same for every `n`* — `k₁ = k₂` makes the factor `1`. A family whose total
mass drifts with `n` (`Σ_λ d_q²/[n]_q! = 0.991 / 1.111 / 1.517` at
`n = 6 / 9 / 12`) fails this, and distorts every cross-nucleus comparison. -/
theorem crossRatio_smul (B₁ E₁ B₂ E₂ k₁ k₂ : ℝ)
    (hE₁ : E₁ ≠ 0) (hB₂ : B₂ ≠ 0) (hE₂ : E₂ ≠ 0) (hk₂ : k₂ ≠ 0) :
    (k₁ * B₁ / E₁) / (k₂ * B₂ / E₂) = (k₁ / k₂) * ((B₁ / E₁) / (B₂ / E₂)) := by
  field_simp

/-- **The cross-nucleus metric is unchanged exactly when the two normalisers
agree.** The `k₁ = k₂` specialisation of `crossRatio_smul` — the positive form
of the requirement. -/
theorem crossRatio_invariant_of_eq (B₁ E₁ B₂ E₂ k : ℝ)
    (hE₁ : E₁ ≠ 0) (hB₂ : B₂ ≠ 0) (hE₂ : E₂ ≠ 0) (hk : k ≠ 0) :
    (k * B₁ / E₁) / (k * B₂ / E₂) = (B₁ / E₁) / (B₂ / E₂) := by
  field_simp

/-- **A weight family vanishing on the stratum makes the functional vacuous.**
If `w_λ = 0` for every `λ` in the depth-`k` stratum `s`, then `Φ_k = 0`
identically — for *every* braid, so the stratum carries no information at all.

This is the invariant behind the `y_λ` exclusion: at `SU(N)` the Markov/Ocneanu
weight is `y_λ ∝ ∏_□ [N + c(□)]_q / [h(□)]_q`, and a `λ` with more than `N` rows
has a cell of content `−N`, contributing `[0]_q = 0`
(`Eightfold.RowCapObstruction`). Depth `k` means `k + 1` rows, so `y_λ = 0`
throughout every stratum of depth `≥ N`. At the production `N = 2` that is
every stratum from depth 2 up — including the depth-3 chirality channel. -/
theorem phi_eq_zero_of_weights_vanish (s : Finset ι) (w m c : ι → ℝ)
    (hw : ∀ l ∈ s, w l = 0) :
    phi s w m c = 0 := by
  unfold phi
  exact Finset.sum_eq_zero fun l hl => by rw [hw l hl]; ring

/-- Corollary of the above at the observable level: a stratum on which the
weights vanish contributes nothing to the binding, so no choice of
distinguished knot at that depth can change anything. -/
theorem phiDiff_eq_zero_of_weights_vanish (s : Finset ι) (w mf ma c : ι → ℝ)
    (hw : ∀ l ∈ s, w l = 0) :
    phi s w mf c - phi s w ma c = 0 := by
  rw [phi_eq_zero_of_weights_vanish s w mf c hw,
    phi_eq_zero_of_weights_vanish s w ma c hw, sub_self]

end QOU.BraidKnot.DepthWeightReq
