import QOU.Mass.ChainTraceFactor
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic

/-!
# The free-energy reading has no energy spectrum

`rem:bond-log-ratio-is-a-free-energy` establishes that
`L = -log tr_2(sigma + d)` is a free-energy difference over the level-2 Wenzl
state sum, and records as **open** the separate claim that `B = alpha L` is the
nuclear binding energy. The evidence already on the books is three misses. This
file proves something prior to all of them, and it is not a measurement at `q0`
but an identity in `q`.

A free energy is `F = -kT log Z` with `Z = sum_i exp(-E_i/kT)`. Every summand of
a partition function is a **positive** Boltzmann factor, and that positivity is
what makes `F` a Legendre transform — hence what gives it an internal energy and
an entropy at all. The `H_2` state sum here has two summands, carrying the
`sigma`-eigenvalues `q` on `(2)` and `-q⁻¹` on `(1,1)`:

    tr_2(sigma + d) = w_+ (q + d) + w_- (-q⁻¹ + d).

**The second one is negative** for every `q > 0` and every `d ≤ 0`
(`minusSummand_neg`), and the corpus's interface letters are exactly the
non-positive ones — `0`, `-h/2`, `d_pn`, `-h` (`admissible_letters_nonpos`).
Positivity would need `d > q⁻¹ > 0`, so the required offset does not merely lie
outside the available range, it lies **on the other side of zero from all of it**
(`positivity_would_need_d_gt_inv_q`). No `q` rescues the sign, because `q⁻¹ > 0`
for every `q > 0`.

Consequently no real `E_-` satisfies `exp(-E_-) = -q⁻¹ + d`
(`no_real_energy_for_minus_block`): `exp` is positive and the factor is not. The
`(1,1)` block has no energy, so there is no `U` and no `S` for `alpha L` to be or
to differ from, and the step "this free energy is the binding energy" has nothing
to stand on.

What is NOT retracted, and it is most of the arc: the total stays **positive**
(`stateSum_pos_but_signed`) — the `(2)` block outweighs the `(1,1)` block — so
`L` is real, exact, convention-D canonical, and every number computed from it is
untouched. The free-energy *description* is also correct: signed free energies
over quasi-probabilities are legitimate objects, and the block names this one
correctly when it says "a free energy of a signed observable over a
quasi-probability, not of a positive one". What this file removes is the
sentence after that.

Measured companion, with the `q0` figures and the `pn` near-cancellation:
`the_free_energy_reading_has_no_energy_spectrum_probe.py`. Bean `qou-qnqf`.
-/

namespace QOU.Mass.FreeEnergySigned

open QOU.Mass.ChainTraceFactor

/-- The `(1,1)` block's summand of `tr_2(sigma + d)`: weight times factor. -/
noncomputable def minusSummand (q d : ℝ) : ℝ := wMinus q * (-q⁻¹ + d)

theorem qint3_pos {q : ℝ} (hq : q ≠ 0) : 0 < qint3 q := by
  unfold qint3
  have : (0:ℝ) < (q ^ 2)⁻¹ := by positivity
  nlinarith [sq_nonneg q]

/-- The `(1,1)` Wenzl weight is strictly positive, so it cannot flip a sign. -/
theorem wMinus_pos {q : ℝ} (hq : q ≠ 0) : 0 < wMinus q := by
  unfold wMinus
  have := qint3_pos hq
  positivity

/-- **The `(1,1)` factor is negative** for every `q > 0` and every non-positive
offset. This is the whole obstruction, and it needs no substrate value. -/
theorem minusFactor_neg {q d : ℝ} (hq : 0 < q) (hd : d ≤ 0) : -q⁻¹ + d < 0 := by
  have : 0 < q⁻¹ := by positivity
  linarith

theorem minusSummand_neg {q d : ℝ} (hq : 0 < q) (hd : d ≤ 0) :
    minusSummand q d < 0 :=
  mul_neg_of_pos_of_neg (wMinus_pos hq.ne') (minusFactor_neg hq hd)

/-- Positivity of the `(1,1)` summand would need `d > q⁻¹`, and `q⁻¹ > 0`: the
required offset is on the other side of ZERO from every non-positive letter. -/
theorem positivity_would_need_d_gt_inv_q {q d : ℝ} (hq : 0 < q)
    (hpos : 0 < -q⁻¹ + d) : q⁻¹ < d ∧ 0 < d := by
  have h1 : q⁻¹ < d := by linarith
  exact ⟨h1, lt_trans (by positivity) h1⟩

/-- **No real energy.** `exp` is positive; the `(1,1)` factor is not. So the
block carries no `E_-`, and the Legendre structure `F = U - TS` is absent. -/
theorem no_real_energy_for_minus_block {q d : ℝ} (hq : 0 < q) (hd : d ≤ 0) :
    ¬ ∃ E : ℝ, Real.exp (-E) = -q⁻¹ + d := by
  rintro ⟨E, hE⟩
  have hpos := Real.exp_pos (-E)
  rw [hE] at hpos
  exact absurd hpos (not_lt.mpr (minusFactor_neg hq hd).le)

/-- The three interface letters the algebra supplies — `0`, `-h`, and `d_pn` —
are all non-positive for `1 ≤ q` with `δ ≤ 2`, so the theorem above applies to
every one of them. (`-h/2` is the `δ = 0` case of `d_pn`.) -/
theorem admissible_letters_nonpos {q : ℝ} (hq : 1 ≤ q) (hd2 : deltaPN q ≤ 2) :
    (0:ℝ) ≤ 0 ∧ -(heckeH q) ≤ 0 ∧ dPN q ≤ 0 := by
  have hh := heckeH_nonneg hq
  have hd := deltaPN_nonneg hq
  refine ⟨le_refl 0, by linarith, ?_⟩
  unfold dPN
  nlinarith

/-- **The state sum is positive overall and signed term by term.** That pairing
is the whole finding: `L = -log(z + d)` is a real number, so nothing computed
from it moves, and yet the object under the logarithm is not a partition
function. -/
theorem stateSum_pos_but_signed {q d : ℝ} (hq : 0 < q) (hd : d ≤ 0)
    (hz : 0 < markovZ q + d) :
    0 < twoStrandTrace q d ∧ minusSummand q d < 0 :=
  ⟨by rw [twoStrandTrace_eq q d hq.ne']; exact hz, minusSummand_neg hq hd⟩

/-- The `pp` instance, with the positivity discharged from the arc's own lemma:
`tr_2(sigma) = z > 0`, while its `(1,1)` summand is negative. -/
theorem pp_pos_but_signed {q : ℝ} (hq : 0 < q) :
    0 < twoStrandTrace q 0 ∧ minusSummand q 0 < 0 :=
  stateSum_pos_but_signed hq (le_refl 0) (by simpa using markovZ_pos hq)

/-- The `nn` instance: `tr_2(sigma⁻¹) = z - h > 0`, `(1,1)` summand negative. -/
theorem nn_pos_but_signed {q : ℝ} (hq : 1 ≤ q) :
    0 < twoStrandTrace q (-(heckeH q)) ∧ minusSummand q (-(heckeH q)) < 0 := by
  have hq0 : 0 < q := by linarith
  exact stateSum_pos_but_signed hq0 (by linarith [heckeH_nonneg hq])
    (by simpa using mirror_pos hq0)

/-- The `pn` instance, the letter the binding arc turns on. -/
theorem pn_pos_but_signed {q : ℝ} (hq : 1 ≤ q) (hd2 : deltaPN q ≤ 2) :
    0 < twoStrandTrace q (dPN q) ∧ minusSummand q (dPN q) < 0 := by
  have hq0 : 0 < q := by linarith
  obtain ⟨_, _, hpn⟩ := admissible_letters_nonpos hq hd2
  exact stateSum_pos_but_signed hq0 hpn (pn_factor_pos hq)

/-- The unweighted block sum, whose `pn` value is the probe's `h·δ/2`. Recorded
because it is what makes the `pn` letter the near-null vector of the unweighted
sum — it survives in `z + d` only because `w_+ ≠ w_-`. -/
theorem blockSum_eq (q d : ℝ) : (q + d) + (-q⁻¹ + d) = heckeH q + 2 * d := by
  unfold heckeH; ring

theorem pn_blockSum_eq_h_delta_half (q : ℝ) :
    (q + dPN q) + (-q⁻¹ + dPN q) = heckeH q * deltaPN q / 2 := by
  rw [blockSum_eq]
  unfold dPN
  ring

end QOU.Mass.FreeEnergySigned
