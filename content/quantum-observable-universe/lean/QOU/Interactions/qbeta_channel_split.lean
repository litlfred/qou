import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring

/-!
# Q_β channel split — locating the binding/Q_β double-count

Reconciles two framings of the nucleon `Q`-value:

* **#2363 (counit):** `Q_β = ε(Δ)·𝔈₀` with `ε(Δ) = h²/2 − h` (`h = q − q⁻¹`);
* **#2346 (complex volume):** `𝔙 = 𝔈₀·tr_M((Π_free−1)∘𝓜) ∈ ℂ`, with
  `binding = Re 𝔙` (bar-even / `cosh`) and `Q_β = Im 𝔙` (bar-odd / `sinh`),
  split by the bar-involution `σ : q ↦ q⁻¹`, i.e. `h ↦ −h`.

The net difference `Δ` splits by bar-parity into a **vacuum** channel
(`γ`-coefficient `h²/2`, bar-**even**) and a **crossing** channel
(`σ`-coefficients summing to `−h`, bar-**odd**). #2346 assigns the
bar-even channel to *binding* and the bar-odd channel to *Q_β*. But the
#2363 counit `Q_β = ε(Δ)` uses the **full** sum `h²/2 − h` — it carries the
bar-even vacuum channel that #2346 books as binding. That channel is the
**double-count**: it cannot belong to both observables. Numerically it is
exactly the piece that moves the prediction from `+11.86%` (bar-odd only)
to `+0.17%` (full counit).

Generic field; `h` free (CLAUDE.md §7c).
-/

namespace QOU.Interactions.QBetaChannelSplit

variable {R : Type*} [Field R]

/-- Vacuum (`γ`) channel of the nucleon net difference — the bar-**even**
    part, `h²/2`. #2346 books this as binding (`Re 𝔙`). -/
def vacuumChannel (h : R) : R := h ^ 2 / 2

/-- Crossing (`σ`) channel — the bar-**odd** part, `−h`. #2346 books this as
    `Q_β` (`Im 𝔙`). -/
def crossingChannel (h : R) : R := -h

/-- The counit `ε(Δ) = h²/2 − h` is the sum of the two channels. -/
theorem counit_split (h : R) :
    h ^ 2 / 2 - h = vacuumChannel h + crossingChannel h := by
  unfold vacuumChannel crossingChannel; ring

/-- The vacuum channel is **bar-even**: invariant under `h ↦ −h`. -/
theorem vacuum_bar_even (h : R) : vacuumChannel (-h) = vacuumChannel h := by
  unfold vacuumChannel; ring

/-- The crossing channel is **bar-odd**: negated under `h ↦ −h`. -/
theorem crossing_bar_odd (h : R) :
    crossingChannel (-h) = - crossingChannel h := by
  unfold crossingChannel; ring

/-- **The double-count, exactly.** The #2363 counit `Q_β` (the full
    `ε(Δ) = h²/2 − h`) exceeds the bar-odd transition channel
    (`#2346`'s `Im 𝔙`) by precisely the bar-even vacuum channel
    `h²/2` — the quantity `#2346` independently books as binding
    (`Re 𝔙`). So the two framings cannot both be right as stated:
    the vacuum channel is attributed to *binding* and to *Q_β*
    simultaneously. -/
theorem double_count (h : R) :
    (h ^ 2 / 2 - h) - crossingChannel h = vacuumChannel h := by
  unfold vacuumChannel crossingChannel; ring

end QOU.Interactions.QBetaChannelSplit
