import QOU.Mass.BindingQHermiteOscillator

/-!
# QOU.Mass.QWeberInterpolation — parabolic-cylinder-type even/odd channel interpolation

The fibre-level skeleton of the parabolic cylinder function `D_ν(z)` transported to the
q-Hermite / Rogers–Szegő channel towers (2026-07-03 audit
`docs/audits/2026-07-03-parabolic-cylinder-channel-interpolation.md`). Classically

`D_ν = 2^{ν/2}√π [ y_even/Γ((1−ν)/2) − √2·y_odd/Γ(−ν/2) ]`,

one continuous-index family containing both parity towers, with parity selected at integer
`ν` by Γ-pole vanishing: the even-solution coefficient vanishes at odd integers, the
odd-solution coefficient at even integers. The `Γ_q`-pole lattice is identical, so the
mechanism q-deforms verbatim.

`QWeberFamily` carries exactly that structure as a class: a combination field and the two
pole-vanishing fields (the analytic content, taken as hypotheses — §3b). Everything
downstream is **proved**:

* **parity collapse** — at even (resp. odd) integer index the family is a pure even
  (resp. odd) channel (`pure_even_channel`, `pure_odd_channel`);
* **recurrence closure** — if both towers satisfy the Rogers–Szegő three-term recurrence
  (`FollowsRogersSzego`, the q-oscillator bound-state recurrence), then so does the
  interpolant at *every* index `ν` (`interp_follows_rogers_szego`) — the fibre-level face
  of Weber's equation having a two-dimensional solution space;
* **two-step decoupling transfer at `t = −1`** and **odd-term vanishing transfer**
  (`interp_two_step_at_neg_one`, `interp_odd_vanishes_at_neg_one`) — the proved parity
  split of `BindingQHermiteOscillator` lifts through the interpolation;
* **non-vacuity** — an explicit (classical-choice) model `demoA`/`demoB`/`demoD`
  inhabits the class over any field (`demo_family`), so the axiomatisation is consistent.

Ground ring: a generic field `K` (§7c — fibre-level / q-formal; no archimedean
evaluation, no `ℝ`). The index `ν` ranges over `K`, with the integer lattice embedded by
`Nat.cast`.

Ref: [dlmf-ch12] https://dlmf.nist.gov/12 (classical D_ν and the Γ-pole connection
formula); [atakishiyev-suslov1990] https://doi.org/10.1007/BF01017247 (q-oscillator).
-/

namespace QOU.Mass.QWeberInterpolation

open QOU.Mass.BindingQHermiteOscillator

variable {K : Type*} [Field K]

/-- **The q-Weber interpolating family, as a class.** `D ν` is the member of the family at
continuous index `ν : K`; `E`/`O` are the even/odd channel towers; `A`/`B` are the
channel coefficients. The two vanishing fields are the fibre-level shadow of the
`Γ_q`-pole mechanism: `1/Γ_q(−ν/2)` kills the odd part at even integers and
`1/Γ_q((1−ν)/2)` kills the even part at odd integers. -/
class QWeberFamily (D : K → ℕ → K) (E O : ℕ → K) (A B : K → K) : Prop where
  /-- The family is everywhere the two-channel combination `A(ν)·E + B(ν)·O`. -/
  combination : ∀ (ν : K) (m : ℕ), D ν m = A ν * E m + B ν * O m
  /-- The even-channel coefficient vanishes on the odd integer lattice
  (`Γ_q((1−ν)/2)` pole). -/
  A_vanishes_at_odd : ∀ j : ℕ, A ((2 * j + 1 : ℕ) : K) = 0
  /-- The odd-channel coefficient vanishes on the even integer lattice
  (`Γ_q(−ν/2)` pole). -/
  B_vanishes_at_even : ∀ j : ℕ, B ((2 * j : ℕ) : K) = 0

/-- **Parity collapse, even points.** At an even integer index the interpolant is a pure
even channel: `D(2j) = A(2j)·E`. -/
theorem pure_even_channel (D : K → ℕ → K) (E O : ℕ → K) (A B : K → K)
    [inst : QWeberFamily D E O A B] (j m : ℕ) :
    D ((2 * j : ℕ) : K) m = A ((2 * j : ℕ) : K) * E m := by
  rw [inst.combination, inst.B_vanishes_at_even j, zero_mul, add_zero]

/-- **Parity collapse, odd points.** At an odd integer index the interpolant is a pure
odd channel: `D(2j+1) = B(2j+1)·O`. -/
theorem pure_odd_channel (D : K → ℕ → K) (E O : ℕ → K) (A B : K → K)
    [inst : QWeberFamily D E O A B] (j m : ℕ) :
    D ((2 * j + 1 : ℕ) : K) m = B ((2 * j + 1 : ℕ) : K) * O m := by
  rw [inst.combination, inst.A_vanishes_at_odd j, zero_mul, zero_add]

/-- **Recurrence closure.** If both channel towers satisfy the Rogers–Szegő three-term
recurrence at `(t, q)`, then the interpolant satisfies it at every index `ν` — the
solution set of the fibre q-difference equation is closed under the two-channel
combination (Weber's equation has a 2-dimensional solution space). -/
theorem interp_follows_rogers_szego {D : K → ℕ → K} (E O : ℕ → K) (A B : K → K)
    {t q : K} (ν : K) [instW : QWeberFamily D E O A B]
    [instE : FollowsRogersSzego E t q] [instO : FollowsRogersSzego O t q] :
    FollowsRogersSzego (D ν) t q := by
  refine ⟨fun m => ?_⟩
  rw [instW.combination, instW.combination, instW.combination,
    instE.recurrence m, instO.recurrence m]
  ring

/-- **Two-step decoupling transfers through the interpolation.** At `t = −1` the
interpolant inherits the parity-decoupled two-step recurrence
`D ν (m+2) = (1 − q^{m+1})·D ν m` for every `ν`. -/
theorem interp_two_step_at_neg_one {D : K → ℕ → K} (E O : ℕ → K) (A B : K → K)
    {q : K} (ν : K) [instW : QWeberFamily D E O A B]
    [instE : FollowsRogersSzego E (-1) q] [instO : FollowsRogersSzego O (-1) q]
    (m : ℕ) :
    D ν (m + 2) = (1 - q ^ (m + 1)) * D ν m := by
  haveI := interp_follows_rogers_szego (D := D) (t := -1) (q := q) E O A B ν
  exact rogers_szego_t_neg_one_two_step (D ν) q m

/-- **Odd-term vanishing transfers through the interpolation.** At `t = −1` with both
channel boundary values `E 1 = O 1 = 0`, every member of the family has vanishing odd
terms — the q-deformed parity of `rogers_szego_odd_vanishes_at_neg_one`, uniformly
in `ν`. -/
theorem interp_odd_vanishes_at_neg_one {D : K → ℕ → K} (E O : ℕ → K) (A B : K → K)
    {q : K} (ν : K) [instW : QWeberFamily D E O A B]
    [instE : FollowsRogersSzego E (-1) q] [instO : FollowsRogersSzego O (-1) q]
    (hE1 : E 1 = 0) (hO1 : O 1 = 0) (j : ℕ) :
    D ν (2 * j + 1) = 0 := by
  haveI := interp_follows_rogers_szego (D := D) (t := -1) (q := q) E O A B ν
  have hD1 : D ν 1 = 0 := by
    rw [instW.combination, hE1, hO1, mul_zero, mul_zero, add_zero]
  exact rogers_szego_odd_vanishes_at_neg_one (D ν) q hD1 j

section DemoModel

open Classical in
/-- Demo even-channel coefficient: `1` off the odd integer lattice, `0` on it. -/
noncomputable def demoA (ν : K) : K :=
  if ∃ j : ℕ, ν = ((2 * j + 1 : ℕ) : K) then 0 else 1

open Classical in
/-- Demo odd-channel coefficient: `1` off the even integer lattice, `0` on it. -/
noncomputable def demoB (ν : K) : K :=
  if ∃ j : ℕ, ν = ((2 * j : ℕ) : K) then 0 else 1

/-- Demo interpolating family built from the demo coefficients. -/
noncomputable def demoD (E O : ℕ → K) : K → ℕ → K :=
  fun ν m => demoA ν * E m + demoB ν * O m

/-- **Non-vacuity.** The demo model inhabits `QWeberFamily` for any pair of towers over
any field, so the class is consistent (not an empty axiomatisation). Deliberately a
`theorem`, not a global `instance`: exporting a default instance of a `Prop` class
would pollute downstream typeclass search (use `haveI := demo_family E O` locally if
the instance is wanted). -/
theorem demo_family (E O : ℕ → K) :
    QWeberFamily (demoD E O) E O (demoA (K := K)) (demoB (K := K)) :=
  { combination := fun _ _ => rfl
    A_vanishes_at_odd := fun j => by
      simp only [demoA]
      exact if_pos ⟨j, rfl⟩
    B_vanishes_at_even := fun j => by
      simp only [demoB]
      exact if_pos ⟨j, rfl⟩ }

end DemoModel

end QOU.Mass.QWeberInterpolation
