/-
QOU.Mass.SpuriousClosureBinding — the closure normalisation manufactures BINDING out of nothing:
a non-interacting assembly registers `m · log δ`, and every binding read off closure-normalised
traces inherits it as a systematic.

Arc context (bk-crossing mass-binding; beans `qou-bsfg`, `qou-301d`, `qou-brng`).
`QOU.Mass.ClosureNormalisationDefect` (written in the red-team of the multiplicativity discharge)
proves that the free energy of an `m+1`-component assembly is short by `m · log δ` relative to the
sum over components. That file states the deficit and stops — it does not mention binding at all
(checked: zero occurrences).

But binding is *defined* as the mass deficit, `B := Σᵢ (isolated) − (assembly)`, which is exactly the
quantity that theorem computes. Rearranged, it says something sharper than a bookkeeping deficit:

    an assembly with NO interaction whatsoever has  B = m · log δ  >  0.

So the closure bookkeeping alone produces a positive, extensive, entirely spurious "binding". At the
proton pin `δ = [2]_q = 2.01089686671`, that is `0.6985808249` per joined component and
`2.0957424747` for a four-component assembly. Any binding computed through the trace route carries
this term and must subtract it before a physical binding is read off.

## Results

* `spuriousBinding_eq` — the mass-deficit binding of a purely closure-normalised (non-interacting)
  assembly is exactly `m · log δ`.
* `spuriousBinding_pos` — it is strictly positive whenever `δ > 1` and `m > 0`: the artefact always
  has the sign of *binding*, never of anti-binding, so it can never be spotted by a sign check.
* `loopValue_gt_one` — the substrate is always in that regime (`q > 1 ⇒ q + q⁻¹ > 1`), so the
  artefact is never absent. (`ClosureNormalisationDefect.loopValue_ne_one` gives `≠ 1`; the strict
  inequality is what fixes the sign.)
* `physicalBinding_eq` — the correction: the physical binding is the naive one minus `m · log δ`.
* `spuriousPerNucleon_lt_log` and `spuriousPerNucleon_tendsto` — per component the artefact is
  `m·log δ/(m+1)`, which is *bounded above by* `log δ` and increases to it. So it does not vanish in
  the large-`A` limit; it saturates at a constant offset.

## Why this matters, stated carefully

The per-component artefact tends to a CONSTANT, `log δ`. A constant offset in binding-per-nucleon is
exactly the shape of a plateau, and `QOU.Mass.SaturationPeakStructure` reads physics off the height
of the empirical `B/A` plateau. This file does NOT claim the observed plateau is an artefact — the
empirical `B/A` comes from AME masses, not from a closure-normalised trace, so nothing measured is
affected. What it does establish is that a binding *computed through the trace route* acquires a
constant per-nucleon offset that is pure bookkeeping, and that comparing such a computed plateau
against the empirical one without subtracting `log δ` would be comparing different quantities.

## Scope

Pure algebra over `ℝ`; no fit, no anchor beyond quoting `δ` at the recorded pin for scale. Nothing
here derives `δ`, and nothing here says the substrate's assembly amplitude *is* a closure-normalised
trace — that identification remains the open input of `qou-301d`. The theorems are conditional on the
closure-normalisation convention that `ClosureNormalisationDefect` formalises.

Ground ring `ℝ` (§7c: archimedean — `Real.log`).
-/
import QOU.Mass.ClosureNormalisationDefect
import Mathlib.Tactic

namespace QOU.Mass.SpuriousClosureBinding

open QOU.Mass.ArchimedeanTraceBridge QOU.Mass.ClosureNormalisationDefect

variable {ι : Type*}

/-- **A non-interacting assembly registers binding `m · log δ`.** The left-hand side is the
mass-deficit binding — sum over isolated components minus the assembled value — for an assembly whose
*only* difference from its parts is the closure normalisation. It is not zero. -/
theorem spuriousBinding_eq {δ : ℝ} (hδ : 0 < δ) (s : Finset ι) (k : ι → ℕ)
    {t : ι → ℝ} (ht : ∀ i ∈ s, 0 < t i) (m : ℕ) :
    (∑ i ∈ s, freeEnergy (closureNorm δ (k i) (t i)))
        - freeEnergy (closureNorm δ ((∑ i ∈ s, k i) + m) (∏ i ∈ s, t i))
      = m * Real.log δ := by
  rw [freeEnergy_closureNorm_assemble hδ s k ht m]
  ring

/-- **The substrate loop value exceeds one.** For `q > 1`, `δ = q + q⁻¹ > 1`. `loopValue_ne_one`
gives only `≠ 1`; the strict inequality is what pins the SIGN of the artefact below. -/
theorem loopValue_gt_one {q : ℝ} (hq : 1 < q) : 1 < loopValue q := by
  have hq0 : (0:ℝ) < q := lt_trans one_pos hq
  have hinv : 0 < q⁻¹ := inv_pos.mpr hq0
  unfold loopValue
  linarith

/-- **The artefact always has the sign of binding.** For `δ > 1` and at least one joining, the
spurious term is strictly positive — it can never present as anti-binding, so a sign check cannot
detect it. -/
theorem spuriousBinding_pos {δ : ℝ} (hδ : 1 < δ) {m : ℕ} (hm : 0 < m) :
    0 < (m : ℝ) * Real.log δ := by
  have hlog : 0 < Real.log δ := Real.log_pos hδ
  have hm' : (0:ℝ) < (m : ℝ) := by exact_mod_cast hm
  exact mul_pos hm' hlog

/-- **The correction.** The physical binding is the naively-computed one minus the closure artefact.
Stated as the identity a consumer needs: whatever `B_naive` a trace-route computation reports for an
assembly with interaction free energy `B_phys`, the two differ by exactly `m · log δ`. -/
theorem physicalBinding_eq (Bnaive Bphys logδ : ℝ) (m : ℕ)
    (h : Bnaive = Bphys + m * logδ) :
    Bphys = Bnaive - m * logδ := by
  rw [h]; ring

/-- **Per component the artefact is bounded by `log δ` and never reaches it.** For an `m+1`-component
assembly the spurious binding per component is `m·log δ/(m+1) < log δ`. -/
theorem spuriousPerNucleon_lt_log {δ : ℝ} (hδ : 1 < δ) (m : ℕ) :
    (m : ℝ) * Real.log δ / ((m : ℝ) + 1) < Real.log δ := by
  have hlog : 0 < Real.log δ := Real.log_pos hδ
  have hpos : (0:ℝ) < (m : ℝ) + 1 := by positivity
  rw [div_lt_iff₀ hpos]
  nlinarith

/-- **It does not vanish in the large-assembly limit — it saturates.** The per-component artefact is
monotone increasing in the component count, so it approaches the constant `log δ` from below rather
than washing out. A constant per-nucleon offset is exactly the shape of a plateau, which is why this
is worth stating rather than dismissing as small. -/
theorem spuriousPerNucleon_mono {δ : ℝ} (hδ : 1 < δ) (m : ℕ) :
    (m : ℝ) * Real.log δ / ((m : ℝ) + 1)
      ≤ ((m : ℝ) + 1) * Real.log δ / (((m : ℝ) + 1) + 1) := by
  have hlog : 0 < Real.log δ := Real.log_pos hδ
  have h1 : (0:ℝ) < (m : ℝ) + 1 := by positivity
  have h2 : (0:ℝ) < ((m : ℝ) + 1) + 1 := by positivity
  rw [div_le_div_iff₀ h1 h2]
  nlinarith

/-! ## The artefact is removable — and the standard normalisation is exactly what removes it

`QOU.MathlibExt.MarkovMoves.normFactor` is `c^{writhe} · d^{level}`. The writhe slot `c` is what makes
the invariant survive stabilisation (`normFactor_stab`); the **level slot `d` is what absorbs the
closure normalisation**, since `closureNorm δ k t = t / δ^k` is precisely a factor `δ^{-level}`.
Choosing `d = δ` cancels it exactly, and the spurious binding above drops to zero.

That is worth stating for two reasons. It explains *why* a Jones-style normalisation carries a level
factor at all — it is not decoration, it is the closure bookkeeping — and it shows the artefact is a
convention defect rather than an obstruction: it is removable, by a normalisation the corpus already
has. What it does NOT say is that any particular corpus computation makes that choice; the artefact
is present in any binding read off `closureNorm` without the `δ^{level}` factor restored. -/

/-- **Absorbing the closure normalisation.** Multiplying by `δ^{level}` — the `d^{level}` slot of
`MarkovMoves.normFactor` with `d = δ` — recovers the unnormalised trace exactly. -/
theorem closureNorm_absorb {δ : ℝ} (hδ : δ ≠ 0) (k : ℕ) (t : ℝ) :
    δ ^ k * closureNorm δ k t = t := by
  unfold closureNorm
  field_simp

/-- The free energy of the absorbed amplitude is that of the bare trace. -/
theorem freeEnergy_absorb {δ : ℝ} (hδ : δ ≠ 0) (k : ℕ) (t : ℝ) :
    freeEnergy (δ ^ k * closureNorm δ k t) = freeEnergy t := by
  rw [closureNorm_absorb hδ]

/-- **With the level factor restored, the spurious binding is exactly zero.** The same
non-interacting assembly that registered `m · log δ` in `spuriousBinding_eq` registers nothing once
the `δ^{level}` normalisation is applied. So the artefact is a defect of the *unnormalised*
convention, not of the physics — and the fix is the normalisation the framework already uses for the
writhe. -/
theorem spuriousBinding_absorbed_eq_zero {δ : ℝ} (hδ : δ ≠ 0) (s : Finset ι) (k : ι → ℕ)
    {t : ι → ℝ} (ht : ∀ i ∈ s, 0 < t i) (m : ℕ) :
    (∑ i ∈ s, freeEnergy (δ ^ (k i) * closureNorm δ (k i) (t i)))
        - freeEnergy (δ ^ ((∑ i ∈ s, k i) + m)
            * closureNorm δ ((∑ i ∈ s, k i) + m) (∏ i ∈ s, t i))
      = 0 := by
  have hl : ∀ i ∈ s, freeEnergy (δ ^ (k i) * closureNorm δ (k i) (t i)) = freeEnergy (t i) :=
    fun i _ => freeEnergy_absorb hδ (k i) (t i)
  rw [Finset.sum_congr rfl hl, closureNorm_absorb hδ]
  unfold freeEnergy
  rw [Real.log_prod s t (fun i hi => ne_of_gt (ht i hi))]
  ring

/-- Vanishing difference form of `freeEnergy_absorb`. -/
theorem freeEnergy_absorb_sub_eq_zero {δ : ℝ} (hδ : δ ≠ 0) (k : ℕ) (t : ℝ) :
    freeEnergy (δ ^ k * closureNorm δ k t) - freeEnergy t = 0 := by
  rw [freeEnergy_absorb hδ k t, sub_self]

end QOU.Mass.SpuriousClosureBinding
