import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Group.Units.Basic
import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# The two-row condition has two roots, and one of them is the augmentation

Companion to `computations/qbeta/qbeta_admissible_functionals_bracket_probe.py`
(19/19), on beans `qou-99qc` and `qou-cds1`.

Under convention D the corpus places the decay channel in the Temperley–Lieb
quotient (`prf:algebraic-gns-embedding`), and a functional descends to that
quotient exactly when it annihilates the `(1,1,1)` block. For the Ocneanu trace
on `H₃(q)` that condition is `y_(1,1,1)(z) = 0`, whose numerator is

`P(z) = -q²·(q - z)·(q²z + z - q³)`.

Two facts about it are ring identities and are pinned here. Neither is the
identification of `P` with the Markov weight — that is done in the probe, by
solving the defining linear system; these are the statements *about* `P` and
about the trace values that the probe's conclusion rests on.

## What is proved

* `markovTrace_longest_at_q` — the load-bearing one. The Ocneanu trace sends the
  longest basis element to `z·(h·z + 1)`; at `z = q` with `h = q - q⁻¹` that is
  exactly `q³`, which is the augmentation's value there. It needs `h·q = q² - 1`,
  i.e. it is where the Hecke parameter enters.
* `traceValues_eq_augmentationValues_at_q` — all four trace values agree with
  the augmentation's at `z = q`, so at that root the Markov trace *is* the
  augmentation rather than a third functional.
* `twoRow_numerator_eq_zero_iff` — over a domain, `P(z) = 0` exactly at the two
  named roots. This is what makes the admissible set *complete* rather than a
  sample.
* `two_roots_distinct` — the roots are genuinely two, for `q ≠ 0`.

## Base ring (AGENTS.md §7c)

Generic `[CommRing R]`, with `q : Rˣ` carrying the invertibility that `q⁻¹`
presupposes. `twoRow_numerator_eq_zero_iff` additionally assumes `[IsDomain R]`,
which is what "a product vanishes iff a factor does" needs — still not
archimedean: no ordering, no `Real.*`.
-/

namespace QOU.QBeta.TwoRowRootsAndAugmentation

variable {R : Type*} [CommRing R]

/-- The Hecke parameter `h = q - q⁻¹`, with `q` a unit. -/
def hOf (q : Rˣ) : R := (q : R) - (↑q⁻¹ : R)

/-- `h·q = q² - 1`: the one place the Hecke relation enters below. -/
theorem hOf_mul_q (q : Rˣ) : hOf q * (q : R) = (q : R) ^ 2 - 1 := by
  have hq : (↑q⁻¹ : R) * (q : R) = 1 := q.inv_mul
  simp only [hOf]
  linear_combination -hq

/-- The Ocneanu trace's value on the longest basis element `σ₀σ₁σ₀`, as a
function of the loop parameter: `tr(T_{w₀}) = z·(h·z + 1)`. -/
def trLongest (h z : R) : R := z * (h * z + 1)

/-- **At `z = q` the longest element's trace is `q³`** — the augmentation's
value there.

This is the load-bearing identity behind "the second root of the two-row
condition is not a third functional". It is exactly where `h·q = q² - 1` is
used; with any other `h` the two would differ. -/
theorem markovTrace_longest_at_q (q : Rˣ) :
    trLongest (hOf q) (q : R) = (q : R) ^ 3 := by
  have hq := hOf_mul_q q
  simp only [trLongest]
  linear_combination (q : R) * hq

/-- **At `z = q` the Markov trace agrees with the augmentation on every basis
element.**

The four values are the trace's, in increasing length: `1` on the identity, `z`
on each generator, `z²` on the two length-two elements, `z·(h·z+1)` on the
longest. The augmentation `σ ↦ q` gives `q ^ ℓ(w)`. At `z = q` the first three
match by inspection and the fourth is `markovTrace_longest_at_q`, so the trace
at that root *is* the augmentation rather than a third admissible functional —
which is what closes the admissible set at two elements. -/
theorem traceValues_eq_augmentationValues_at_q (q : Rˣ) :
    (1 : R) = (q : R) ^ 0 ∧ (q : R) = (q : R) ^ 1
      ∧ (q : R) ^ 2 = (q : R) ^ 2
      ∧ trLongest (hOf q) (q : R) = (q : R) ^ 3 :=
  ⟨(pow_zero _).symm, (pow_one _).symm, rfl, markovTrace_longest_at_q q⟩

/-- Numerator of the `(1,1,1)` Markov weight, `P(z) = -q²(q - z)(q²z + z - q³)`.
Its vanishing is the two-row condition. -/
def twoRowNumerator (q z : R) : R := -q ^ 2 * (q - z) * (q ^ 2 * z + z - q ^ 3)

/-- The two roots are distinct: `q` is not `q³/(q²+1)` for `q ≠ 0`, stated
division-free as `q·(q²+1) ≠ q³`. -/
theorem two_roots_distinct [IsDomain R] (q : R) (hq : q ≠ 0) :
    q * (q ^ 2 + 1) ≠ q ^ 3 := by
  intro hcontra
  exact hq (by linear_combination hcontra)

/-- **The two-row condition has exactly two roots.**

Over a domain and for `q ≠ 0`, `P(z) = 0` iff `z = q` or `(q²+1)·z = q³` — the
second being `z_D = q³/(q²+1)` written division-free. This is what upgrades the
bracket from "the two functionals I enumerated" to a completeness statement
about the admissible set. -/
theorem twoRow_numerator_eq_zero_iff [IsDomain R] (q z : R) (hq : q ≠ 0) :
    twoRowNumerator q z = 0 ↔ z = q ∨ (q ^ 2 + 1) * z = q ^ 3 := by
  have hq2 : -q ^ 2 ≠ 0 := by
    simpa using pow_ne_zero 2 hq
  constructor
  · intro hz
    rcases mul_eq_zero.1 hz with h1 | h2
    · rcases mul_eq_zero.1 h1 with h3 | h4
      · exact absurd h3 hq2
      · exact Or.inl (by linear_combination -h4)
    · exact Or.inr (by linear_combination h2)
  · rintro (rfl | h)
    · simp [twoRowNumerator]
    · have : q ^ 2 * z + z - q ^ 3 = 0 := by linear_combination h
      simp only [twoRowNumerator, this, mul_zero]

end QOU.QBeta.TwoRowRootsAndAugmentation
