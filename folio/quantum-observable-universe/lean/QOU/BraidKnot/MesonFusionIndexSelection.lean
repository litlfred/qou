import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Group.Invertible.Defs
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases

/-!
# m_K/m_π: what the Lean credit on the strong core and the EM factor does and does not select

The L2 row `m_K/m_π` (dashboard `per_observable_100x_status.py`) evaluates

    m_K²/m_π² = [3]_q·[4]_q + (α_em/π)·(1 + log(1 + ℏ_q)).

Two Lean declarations are credited to it: `QOU.BraidKnot.meson_qCG_3x4`
(`[3]_q[4]_q = [2]_q + [4]_q + [6]_q`) and `QOU.BraidKnot.meson_EM_closed_form`
(`1 + ℏ_q − ℏ_q²/2 = (3q² − 1)/(2q²)`). This file asks the formalize-first
question the 2026-08-22 red-team left open: *does anything in the corpus FORCE
the pair `(3,4)`, or the EM factor's form?* What is proved here:

1. `qCG_unnormalised_general` — the q-Clebsch–Gordan fusion holds for **every**
   pair `(m, m+d)`, over a bare `CommRing` with `q·qi = 1`. The `(3,4)` theorem
   is recovered as the instance `m = 3, d = 1`
   (`meson_qCG_3x4_is_family_instance`). So the credited Lean identity is true
   of every member of the scan family `{[a]_q[b]_q}` and carries **no**
   information selecting `(3,4)`: it certifies the algebra of whatever pair is
   chosen, not the choice.
2. `scanPair_four_not_dictionary_index` — the index `4` is not a
   generation index of the dictionary (all are odd: the lepton partners
   `T(2,3), T(2,5), T(2,7)`) and not a meson
   total crossing count (`6, 8, 10`) of the corpus's
   lepton–meson torus-knot dictionary (`prop:lepton-meson-torus-knot-dictionary`,
   `knots-particles-confinement/lepton-meson-torus-knot-dictionary.lean`,
   whose `leptonTorusKnotIndex` / `mesonCrossingCount` the definitions below
   restate value-for-value). Scope: this excludes the *index* reading of `[4]_q`
   against that dictionary (a parity invariant); it does not exclude every
   possible reading (e.g. a spin-3/2 dimension), none of which the corpus
   defines for the kaon.

   **Note (2026-11-21): this side result has lost its premise as a statement
   about quarks.** It was written when the dictionary was read as giving each
   quark its own torus-knot index. Under the owner rulings of 2026-11-20 and
   2026-11-21 a quark is an unknot strand carrying one crossing letter, and
   `3, 5, 7` are the crossing counts of its **lepton partner** — generation
   labels. The theorem still holds as stated (it is arithmetic on
   `quarkTorusIndex`), but it now says "4 is not a generation label", not "4
   is not a quark's knot index". It is kept, not deleted. The credited
   `m_K/m_π` identities (item 1) never read this index and are unaffected.
3. `sqrt_jet_agrees_to_order_two`, `pade_jet_agrees_to_order_two` — the order-2
   jet `1 + h − h²/2`, which is all the 2026-05-28 term-by-term hunt matched
   to data before the factor was named `1 + log(1+h)`, is shared exactly
   (through order `h³` in the stated sense) by `√(1+2h)` and by the `[1/1]`
   Padé `1 + h/(1 + h/2)`. The order-2 data therefore does not identify the
   logarithm; the choice of resummation is not fixed by the matched jet.

Nothing here is a physical identification. All statements are generic-ring
algebra (§7c); none mentions `q₀`.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

namespace QOU.BraidKnot.MesonFusionIndexSelection

open Finset

section QCG

variable {R : Type*} [CommRing R]

/-- Unnormalised q-integer `q^n − qi^n = (q − q⁻¹)·[n]_q` when `qi = q⁻¹`. -/
def qd (q qi : R) (n : ℕ) : R := q ^ n - qi ^ n

/-- One telescoping step: `(q − qi)(q^{e+1} − qi^{e+1}) = (q^{e+2} − q^e) − (qi^e − qi^{e+2})`
under the unit relation. -/
theorem qd_step (q qi : R) (hq : q * qi = 1) (e : ℕ) :
    (q - qi) * qd q qi (e + 1)
      = q ^ (e + 2) - q ^ e - qi ^ e + qi ^ (e + 2) := by
  unfold qd
  linear_combination (-(q ^ e) - qi ^ e) * hq

/-- The telescoped odd-step sum: `(q − qi)·Σ_{k<m} qd(d+1+2k) = q^{d+2m} − q^d − qi^d + qi^{d+2m}`. -/
theorem qd_sum_telescope (q qi : R) (hq : q * qi = 1) (d : ℕ) :
    ∀ m : ℕ, (q - qi) * ∑ k ∈ range m, qd q qi (d + 1 + 2 * k)
      = q ^ (d + 2 * m) - q ^ d - qi ^ d + qi ^ (d + 2 * m) := by
  intro m
  induction m with
  | zero => simp
  | succ m ih =>
    rw [sum_range_succ, mul_add, ih]
    have hs := qd_step q qi hq (d + 2 * m)
    have e1 : d + 1 + 2 * m = d + 2 * m + 1 := by ring
    rw [e1, hs]
    have e2 : d + 2 * (m + 1) = d + 2 * m + 2 := by ring
    rw [e2]
    ring

/-- **General q-Clebsch–Gordan fusion, unnormalised.** For every `m` and `d`,
`(q^m − qi^m)(q^{m+d} − qi^{m+d}) = (q − qi)·Σ_{k<m} (q^{d+1+2k} − qi^{d+1+2k})`,
i.e. `[m]_q[m+d]_q = Σ_{k<m} [d+1+2k]_q`. Holds for every pair of the scan family. -/
theorem qCG_unnormalised_general (q qi : R) (hq : q * qi = 1) (m d : ℕ) :
    qd q qi m * qd q qi (m + d)
      = (q - qi) * ∑ k ∈ range m, qd q qi (d + 1 + 2 * k) := by
  rw [qd_sum_telescope q qi hq d m]
  have hm : (q * qi) ^ m = 1 := by rw [hq, one_pow]
  unfold qd
  linear_combination (-(qi ^ d + q ^ d)) * hm

/-- The credited theorem `QOU.BraidKnot.meson_qCG_3x4` is the `m = 3, d = 1` instance of
`qCG_unnormalised_general`: it is a property of the q-integer algebra, true of every
scan pair, and selects nothing. (Statement copied verbatim from
`braids-and-knots/meson-qcg-fusion-identity.lean`.) -/
theorem meson_qCG_3x4_is_family_instance (q qi : R) (hq : q * qi = 1) :
    (q^3 - qi^3) * (q^4 - qi^4)
      = (q - qi) * ((q^2 - qi^2) + (q^4 - qi^4) + (q^6 - qi^6)) := by
  have h := qCG_unnormalised_general q qi hq 3 1
  simp only [qd, sum_range_succ, sum_range_zero] at h
  norm_num at h
  linear_combination h

/-- A non-selected neighbour of the scan family, e.g. `(2,6)` (the runner-up at
`26 742 ppm` in `mk_mpi_derivation_status_probe.py`), carries its own identity
`[2]_q[6]_q = [5]_q + [7]_q` of exactly the same standing. -/
theorem qCG_2x6 (q qi : R) (hq : q * qi = 1) :
    (q^2 - qi^2) * (q^6 - qi^6)
      = (q - qi) * ((q^5 - qi^5) + (q^7 - qi^7)) := by
  have h := qCG_unnormalised_general q qi hq 2 4
  simp only [qd, sum_range_succ, sum_range_zero] at h
  norm_num at h
  linear_combination h

end QCG

section Dictionary

/-- Generation index `g` of the lepton–meson dictionary: the crossing count of
the lepton partner `T(2,3), T(2,5), T(2,7)` of the generation-`g` quarks
(restates `leptonTorusKnotIndex`). The name `quarkTorusIndex` predates the
owner rulings of 2026-11-20 / 2026-11-21 (a quark is an unknot strand, the
torus knot is its lepton partner) and is kept as an identifier only. -/
def quarkTorusIndex : Fin 3 → ℕ
  | 0 => 3
  | 1 => 5
  | 2 => 7

/-- Meson total crossing count by row: `π = 3+3`, `K = 3+5`, `φ = 5+5`
(restates `mesonCrossingCount`). -/
def mesonCrossingCount : Fin 3 → ℕ
  | 0 => 6
  | 1 => 8
  | 2 => 10

/-- Every generation index of the dictionary (a lepton partner's crossing
count) is odd. -/
theorem quarkTorusIndex_odd (g : Fin 3) : Odd (quarkTorusIndex g) := by
  fin_cases g
  · exact ⟨1, rfl⟩
  · exact ⟨2, rfl⟩
  · exact ⟨3, rfl⟩

/-- **The index `4` of the scan-selected pair is not a dictionary index** — neither a
generation index (parity; read as the lepton partner's crossing count since the
2026-11-21 ruling, not as a quark's own knot index) nor a meson total crossing
count; and the kaon's own constituent label pair `(3, 5)` is not `(3, 4)`. -/
theorem scanPair_four_not_dictionary_index :
    (∀ g : Fin 3, quarkTorusIndex g ≠ 4) ∧
    (∀ g : Fin 3, mesonCrossingCount g ≠ 4) ∧
    (quarkTorusIndex 0, quarkTorusIndex 1) ≠ (3, 4) := by
  refine ⟨fun g h => ?_, fun g => ?_, by decide⟩
  · obtain ⟨k, hk⟩ := quarkTorusIndex_odd g
    omega
  · fin_cases g <;> decide

end Dictionary

section EMJet

variable {R : Type*} [CommRing R] [Invertible (2 : R)]

/-- `√(1 + 2h)` has the same order-2 jet `1 + h − h²/2` as `1 + log(1 + h)`:
`(1 + h − h²/2 + h³/2)² = 1 + 2h + h⁴·(5/4 − h/2 + h²/4)`. The `h³` coefficient (`1/2`)
differs from the logarithm's (`1/3`). -/
theorem sqrt_jet_agrees_to_order_two (h : R) :
    (1 + h - h ^ 2 * ⅟(2 : R) + h ^ 3 * ⅟(2 : R)) ^ 2
      = 1 + 2 * h + h ^ 4 * (5 * ⅟(2 : R) * ⅟(2 : R) - h * ⅟(2 : R)
          + h ^ 2 * ⅟(2 : R) * ⅟(2 : R)) := by
  have h2 : (2 : R) * ⅟(2 : R) = 1 := mul_invOf_self 2
  linear_combination (-h ^ 2 * (h ^ 3 * ⅟(2 : R) + 2 * h ^ 2 * ⅟(2 : R) + 1)) * h2

/-- The `[1/1]` Padé `1 + h/(1 + h/2)` has the same order-2 jet:
`(1 + h/2)·(1 + h − h²/2 + h³/4) = 1 + 3h/2 + h⁴/8`. -/
theorem pade_jet_agrees_to_order_two (h : R) :
    (1 + h * ⅟(2 : R)) * (1 + h - h ^ 2 * ⅟(2 : R) + h ^ 3 * ⅟(2 : R) * ⅟(2 : R))
      = 1 + 3 * h * ⅟(2 : R) + h ^ 4 * ⅟(2 : R) * ⅟(2 : R) * ⅟(2 : R) := by
  have h2 : (2 : R) * ⅟(2 : R) = 1 := mul_invOf_self 2
  linear_combination (-h) * h2

end EMJet

end QOU.BraidKnot.MesonFusionIndexSelection
