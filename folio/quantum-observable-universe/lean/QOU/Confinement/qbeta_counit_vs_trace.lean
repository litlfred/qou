import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Q_β net-ansatz: counit vs Markov trace (algebraic core)

Formalises the algebraic identities behind the audit
`docs/audits/2026-06-16-q-beta-net-ansatz-path-a-counit-vs-trace.md`.

The `N=0` neutron−proton Hecke normal-form difference is, in the basis
`[γ, σ₀, σ₁, L₊, L₋, e⁻]`,
`(n − p) = [h²/2, −h/2, −h/2, 0, 0, 0]`, with `h = q − q⁻¹` the Hecke
parameter. Two canonical functionals act on it:

* the **Frobenius counit** (augmentation) `ε`, which weights every basis
  element by `1` — giving the unweighted sum `ε(n−p) = h²/2 − h`;
* the **Markov trace** `tr_M`, which by axiom **M1** weights the identity
  `γ = 𝟙` by `tr_M(𝟙) = 1` and each crossing `σ` by the loop value `z` —
  giving `tr_M(n−p) = h²/2 − h·z`.

The per-braid mass tower is built on `tr_M`; the `Q_β` ansatz uses `ε`.
These lemmas pin the precise relation between the two: they coincide
exactly at the trivial loop `z = 1`, and differ by `h·(z − 1)` otherwise.

All statements hold over an arbitrary field (the substrate→archimedean
wall is not crossed: no ordering, no `Real.sqrt`). See AGENTS.md §7c.
-/

namespace QOU.Interactions.QBetaCounitTrace

variable {R : Type*} [Field R]

/-- Frobenius counit (augmentation) of the `N=0` neutron−proton NF
    difference: every basis element weighted by `1`. -/
def epsNP (h : R) : R := h ^ 2 / 2 - h

/-- Markov trace of the `N=0` neutron−proton NF difference: identity
    weight `1` (axiom M1), each surviving crossing weighted by the loop
    value `z`. -/
def trMNP (h z : R) : R := h ^ 2 / 2 - h * z

/-- **Coincidence at the trivial loop.** The counit is the Markov trace
    at `z = 1` (the `q`-stripped / topological limit). -/
theorem trMNP_at_one (h : R) : trMNP h 1 = epsNP h := by
  unfold trMNP epsNP; ring

/-- **The exact gap.** Counit minus Markov trace is `h·(z − 1)`. -/
theorem eps_sub_trMNP (h z : R) : epsNP h - trMNP h z = h * (z - 1) := by
  unfold epsNP trMNP; ring

/-- For `h ≠ 0`, the two functionals agree on the nucleon difference
    **iff** the Markov loop is trivial, `z = 1`. -/
theorem agree_iff (h z : R) (hh : h ≠ 0) :
    epsNP h = trMNP h z ↔ z = 1 := by
  rw [← sub_eq_zero, eps_sub_trMNP, mul_eq_zero]
  constructor
  · rintro (h0 | hz1)
    · exact absurd h0 hh
    · exact sub_eq_zero.mp hz1
  · intro hz; right; rw [hz]; ring

/-- **Counit closed form in `q`** (via `h = q − q⁻¹`):
    `ε(n−p) = (q² − 1)(q² − 2q − 1) / (2 q²)`.
    The `(2 : R) ≠ 0` hypothesis excludes characteristic `2`, where the
    `/2` in the mass normalisation is ill-defined. -/
theorem epsNP_q (q : R) (hq : q ≠ 0) (htwo : (2 : R) ≠ 0) :
    epsNP (q - q⁻¹) = (q ^ 2 - 1) * (q ^ 2 - 2 * q - 1) / (2 * q ^ 2) := by
  unfold epsNP; field_simp; ring

/-- **Markov-trace closed form in `q`** (via `h = q − q⁻¹`):
    `tr_M(n−p) = (q² − 1)(q² − 2qz − 1) / (2 q²)` — note **no** spurious
    overall factor of `z` (the identity `γ` carries weight `1`, not `z`). -/
theorem trMNP_q (q z : R) (hq : q ≠ 0) (htwo : (2 : R) ≠ 0) :
    trMNP (q - q⁻¹) z = (q ^ 2 - 1) * (q ^ 2 - 2 * q * z - 1) / (2 * q ^ 2) := by
  unfold trMNP; field_simp; ring

/-! ## Bar-decomposition of the evaluation map (the standing reading, realized)

The Hecke parameter `h = q − q⁻¹` is the fundamental **bar-odd** object:
under the fibre bar involution `q ↦ q⁻¹` it flips sign, `h ↦ −h`. The Markov
loop parameter `z = √q/(1+q)` is **bar-even** (`QOU.QBeta.z_bar_invariant`,
fixed under `q ↦ q⁻¹`, i.e. under `h ↦ −h`). So the evaluation map splits
cleanly, and the split IS the standing reading (owner-granted 2026-07-07,
registry KC6/KC10): the **bar-even part is the identity/mass term `h²/2`**
(carries the shadow), the **bar-odd part is the crossing/loop term** (`−h` for
the counit, `−h·z` for the Markov trace) — the odd channel.

The lemmas below realize this over any field by expressing the bar involution
on `h` as the sign flip `h ↦ −h` (`z` held fixed, being bar-even). -/

/-- **Counit bar-decomposition.** `ε = h²/2 + (−h)`: an even part `h²/2` plus
    an odd part `−h`. Under `h ↦ −h` the even part is invariant and the odd
    part flips sign, so the odd channel of `Q_β` (built on `ε`) is exactly the
    unweighted crossing term `−h`. -/
theorem epsNP_decomp (h : R) : epsNP h = h ^ 2 / 2 + (-h) := by
  unfold epsNP; ring

/-- **Markov-trace bar-decomposition.** `tr_M = h²/2 + (−h·z)` — even identity
    term plus odd loop term. -/
theorem trMNP_decomp (h z : R) : trMNP h z = h ^ 2 / 2 + (-(h * z)) := by
  unfold trMNP; ring

/-- **Counit bar-image.** Under the bar flip `h ↦ −h`, `ε(−h) = h²/2 + h`:
    the even part `h²/2` is invariant and the odd part `−h` flips to `+h`.
    Read against `epsNP_decomp` (`ε(h) = h²/2 − h`), this exhibits the split
    `ε = (bar-even h²/2) + (bar-odd −h)`. -/
theorem epsNP_bar_image (h : R) : epsNP (-h) = h ^ 2 / 2 + h := by
  unfold epsNP; ring

/-- **Markov-trace bar-decomposition.** `tr_M = h²/2 + (−h·z)` with `z`
    bar-even (`z ↦ z`). Under `h ↦ −h`: `tr_M(−h, z) = h²/2 + h·z` — even
    identity part invariant, odd **loop/crossing** part `−h·z` flips sign. So
    the odd channel of the observable is the Markov loop term; the bar-odd
    carrier (KC15 `D(q)`) feeds it through this term, not the identity term. -/
theorem trMNP_bar_image (h z : R) : trMNP (-h) z = h ^ 2 / 2 + h * z := by
  unfold trMNP; ring

end QOU.Interactions.QBetaCounitTrace
