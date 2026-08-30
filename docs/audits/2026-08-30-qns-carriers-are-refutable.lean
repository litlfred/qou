/-
  Bean `qou-rq9n` — the gate for the q-NS carrier re-encoding.

  Three of the five carriers in `ConditionalClasses.lean` were re-encoded on
  2026-08-30 by transcribing the claim each docstring already made:
  `QAubinLions` (`qou-3ytx`), `NSCounterexample` (`qou-5nj1`) and
  `RegularityBreakdown` (`qou-m7a2`), joining `CriticalExponent` (`qou-93hu`).

  COMPILATION IS NOT THE GATE. The previous fields compiled too, and AGENTS.md
  §3b-tax cited them as the model of a carrier "in the *shape* of the claim".
  The shape was right and the content was absent, because every field was an
  existential over a quantity the class got to pick — and an `∃` you witness
  yourself cannot be false.

  So the gate is REFUTABILITY: for each re-encoded carrier there must be a
  value at which the class is FALSE. That is what the previous fields could not
  offer and what makes a `[C]` hypothesis a real assumption rather than
  decoration.

  WHAT THIS FILE SHOWS, EXACTLY — stated narrowly on purpose:

    - refutations for all four re-encoded carriers (two for `CriticalExponent`,
      one per field);
    - satisfiability for `QAubinLions`, `RegularityBreakdown` and
      `CriticalExponent`.

  It does NOT exhibit a satisfiability witness for `NSCounterexample`, and the
  header said otherwise until review on PR #6122 caught it — an over-claim in a
  file whose whole job is to be evidence, which is the defect this arc keeps
  finding, here in my own audit.

  🛑 REFUTABILITY WAS NOT SUFFICIENT, AND `CriticalExponent` IS THE PROOF
  (2026-08-30, bean `qou-4670`). Its first re-encoding was `α = 4/3`, which
  passes every test this file applies: refutable (`α = 2` falsifies it),
  satisfiable, non-trivial, in the shape of the claim. It was still wrong,
  because `4/3` is not a result the corpus holds — `p2-critical-exponent.md`
  offers it as one of two heuristic values under two named turbulence closures
  and says the true exponent is **open**. A field can be perfectly refutable
  and still assert something nobody derived.

  So refutability rules out the vacuous carrier; it does not rule out the
  *fabricated* one, and the second question has to be asked separately: **is
  the proposition this field states one the corpus actually asserts?** That is
  a corpus-grep, not a Lean check, and no proof in this file can stand in for
  it. The witnesses below are now for the de-boxed carrier — positivity plus
  the divergence statement, both transcribed from upstream.

  **Read that absence correctly.** A satisfiability witness for the blow-up
  carrier needs a function unbounded on *every* left-neighbourhood of `T` (e.g.
  `1/(1-t)` at `T = 1`) together with the ε-style argument picking `t` close
  enough to `T` for each `M` — a genuine analysis exercise, not a one-liner. Its
  absence here is a fact about this file's scope, **not** evidence that the
  class is uninhabitable. Forcing a fragile proof to make a header true would
  be the wrong trade.

  `BlowupYekutieli` is absent deliberately: it was NOT re-encoded (bean
  `qou-88nf`), because its docstring names "an explicit constant determined by
  the substrate scale" and never says which, so any bound would be chosen by the
  agent rather than transcribed. It remains inhabitable by zero. See
  `2026-08-30-blowup-yekutieli-has-no-source.md` — the rate is not in the corpus
  at all.

  That companion audit ALSO said "its conjecture block does not exist", which is
  true of the label `conj:blowup-yekutieli` and false of the corpus: the live
  block is `prop:blowup-yekutieli` in `lifting-and-descent/`, carrying
  `smooth ↔ ∀ n, obstruction n = 0` and a derived theorem. Corrected there
  (bean `qou-4670`); the recommended disposition is now to transcribe THAT,
  which needs no rate.

  VERIFY (lean-direct, Mathlib oleans restored, no `lake build` — a build
  against a restored cache with `traces=0` evicts it):

      LEAN_PATH=<mathlib libs>:<dir with QOU/AlgebraicSubstrate/ConditionalClasses.olean> \
        lean docs/audits/2026-08-30-qns-carriers-are-refutable.lean

  Measured 2026-08-30: exit 0, 0 errors.
-/
import QOU.AlgebraicSubstrate.ConditionalClasses

open QOU.AlgebraicSubstrate

/-! ## Refutations — the gate -/

/-- The zero function is not linear with a strictly positive constant. -/
example : ¬ QAubinLions (fun _ => 0) := by
  rintro ⟨C, hC, h⟩
  have := h 1 (by norm_num)
  simp at this
  nlinarith [this, hC]

/-- A bounded vorticity cannot blow up: the field demands values exceeding
every `M`, and the constant `0` function exceeds none. -/
example : ¬ NSCounterexample (fun _ => 0) := by
  rintro ⟨T, _, h⟩
  obtain ⟨t, _, _, hM⟩ := h 1 (T - 1) (by linarith)
  norm_num at hM

/-- A positive-measure set is not Lebesgue-null. -/
example : ¬ RegularityBreakdown (Set.Ioo (0:ℝ) 1) := by
  rintro ⟨h⟩
  rw [Real.volume_Ioo] at h
  norm_num at h

/-- A non-positive exponent refutes the carrier, whatever the enstrophy. -/
example (e : ℝ → ℝ) : ¬ CriticalExponent e (-1) := by
  rintro ⟨hpos, _⟩; norm_num at hpos

/-- A bounded enstrophy refutes it, whatever the exponent: the field demands
values exceeding every `M` arbitrarily close to `1`, and the constant `0`
function exceeds none. -/
example (α : ℝ) : ¬ CriticalExponent (fun _ => 0) α := by
  rintro ⟨_, hdiv⟩
  obtain ⟨q, _, _, hM⟩ := hdiv 1 1 one_pos
  norm_num at hM

/-! ## Satisfiability — three of the four, per the header -/

example : QAubinLions (fun E => 2 * E) := ⟨2, by norm_num, fun E _ => rfl⟩
example : RegularityBreakdown (∅ : Set ℝ) := ⟨by simp⟩

/-- `enstrophy q = (q-1)⁻¹` does diverge as `q → 1⁺`, at exponent `1`.

Unlike the two above this is not a one-liner, and it is the reason the carrier
is worth having: given a bound `M` and a neighbourhood radius `ε`, pick
`δ = min ε c⁻¹ / 2` with `c = max M 1`, so that `δ < ε` puts `1 + δ` inside the
neighbourhood and `δ < c⁻¹` makes `δ⁻¹ > c ≥ M`. -/
example : CriticalExponent (fun q => (q - 1)⁻¹) 1 where
  alpha_pos := one_pos
  enstrophy_diverges := by
    intro M ε hε
    set c : ℝ := max M 1 with hc
    have hc1 : (1:ℝ) ≤ c := le_max_right _ _
    have hcpos : (0:ℝ) < c := lt_of_lt_of_le one_pos hc1
    have hcinv : (0:ℝ) < c⁻¹ := inv_pos.mpr hcpos
    set δ : ℝ := min ε c⁻¹ / 2 with hδ
    have hδpos : 0 < δ := by positivity
    have hmin : (0:ℝ) < min ε c⁻¹ := lt_min hε hcinv
    have hδε : δ < ε := by
      have := min_le_left ε c⁻¹
      simp only [hδ]; linarith
    have hδc : δ < c⁻¹ := by
      have := min_le_right ε c⁻¹
      simp only [hδ]; linarith
    refine ⟨1 + δ, by linarith, by simpa using hδε, ?_⟩
    have hsimp : (1 + δ - 1)⁻¹ = δ⁻¹ := by ring_nf
    rw [hsimp]
    have : c < δ⁻¹ := by
      rw [lt_inv_comm₀ hcpos hδpos]
      exact hδc
    exact lt_of_le_of_lt (le_max_left M 1) this
