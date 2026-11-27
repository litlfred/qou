import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Fintype.BigOperators

/-!
# QOU.MassTheory.NucleusBondValence — a valence cap fixes the nucleus bond count

Term-completeness gap **G5** (`docs/audits/2026-11-27-term-completeness-ledger.md`): the production
chain word carries `A − 1` ruled bonds, about one per nucleon. The corpus already proves that the
Artin encoding cannot do better (`LinearLayoutNoBulk`, `GammaGammaForcesTheLayout`), and that the
band reading admits every layout while selecting nothing new (2026-09-14 audit). So the count has
to come from a selection principle acting on the bond graph.

With an **attractive, additive** bond (each bond adds the same positive binding `b`), energy
minimisation takes the most bonds the structure allows. This file proves the two caps the corpus
supplies above the chain, as bond-count bounds, and nothing else:

* **Valence** (`two_mul_card_le_of_valence`). If every nucleon is an end of at most `k` bonds,
  then `2·|E| ≤ k·|V|`. At `k = N_c = 3` (each quark strand carries one bond, the `K₅` valence
  obstruction of `TetrahedralFluxRingAndMajoranaCluster`) this is `|E| ≤ ⌊3A/2⌋`.
* **Colour labels** (`card_le_of_proper_colouring`). If every bond carries one of `k` labels, and
  two bonds with the same label share no nucleon (the `k4TaitEdgeColour` object of the same file),
  then `|E| ≤ k·⌊|V|/2⌋`. At `k = 3` this is `3⌊A/2⌋`, one less than the valence bound at odd
  `A ≥ 5` (`tait_lt_valence_at_five`).
* **Energy** (`binding_le_of_card_le`, `perNucleon_le_of_valence`). With bond value `b > 0`,
  `B = b·|E|` is at most `b` times the cap, and the per-nucleon count is at most `k/2`.

Attainment of each bound (connected graphs meeting it for `A = 2…60`) is measured by the
companion probe, `computations/probes/nucleus_bond_valence/` (5/5), not proved here.

The setting is deliberately bare: bonds are an index type `ι` with a two-element end set in the
nucleon type `V`, so no `SimpleGraph` machinery is needed and multi-edges are not excluded by
definition. No number from measurement appears; the field is generic.
-/

namespace QOU.MassTheory.NucleusBondValence

open Finset

variable {ι V : Type*} [DecidableEq V] [Fintype V]

/-- **Handshake with a valence cap.** If every bond has exactly two ends and every nucleon is an
end of at most `k` bonds of `E`, then `2·|E| ≤ k·|V|`. -/
theorem two_mul_card_le_of_valence (E : Finset ι) (ends : ι → Finset V)
    (htwo : ∀ e ∈ E, (ends e).card = 2) (k : ℕ)
    (hval : ∀ v : V, (E.filter fun e => v ∈ ends e).card ≤ k) :
    2 * E.card ≤ k * Fintype.card V := by
  classical
  have h1 : 2 * E.card = ∑ e ∈ E, (ends e).card := by
    rw [Finset.sum_congr rfl htwo, Finset.sum_const, smul_eq_mul, mul_comm]
  have h2 : ∑ e ∈ E, (ends e).card = ∑ v : V, (E.filter fun e => v ∈ ends e).card := by
    have : ∀ e ∈ E, (ends e).card = ∑ v : V, if v ∈ ends e then 1 else 0 := by
      intro e _
      rw [Finset.sum_boole]
      simp
    rw [Finset.sum_congr rfl this, Finset.sum_comm]
    refine Finset.sum_congr rfl fun v _ => ?_
    rw [Finset.card_filter]
  rw [h1, h2]
  calc ∑ v : V, (E.filter fun e => v ∈ ends e).card ≤ ∑ _v : V, k :=
        Finset.sum_le_sum fun v _ => hval v
    _ = k * Fintype.card V := by rw [Finset.sum_const, smul_eq_mul, Finset.card_univ, mul_comm]

/-- **One colour class is a matching, so it has at most `⌊|V|/2⌋` bonds.** -/
theorem card_le_half_of_matching (S : Finset ι) (ends : ι → Finset V)
    (htwo : ∀ e ∈ S, (ends e).card = 2)
    (hdisj : (S : Set ι).PairwiseDisjoint ends) :
    S.card ≤ Fintype.card V / 2 := by
  rw [Nat.le_div_iff_mul_le (by norm_num)]
  have hcard : (S.biUnion ends).card = ∑ e ∈ S, (ends e).card := Finset.card_biUnion hdisj
  have hsum : ∑ e ∈ S, (ends e).card = S.card * 2 := by
    rw [Finset.sum_congr rfl htwo, Finset.sum_const, smul_eq_mul]
  calc S.card * 2 = (S.biUnion ends).card := by rw [hcard, hsum]
    _ ≤ Fintype.card V := Finset.card_le_univ _

/-- **Colour-labelled bonds.** If every bond of `E` carries a label in `Fin k`, and two distinct
bonds with the same label share no end, then `|E| ≤ k·⌊|V|/2⌋`. -/
theorem card_le_of_proper_colouring {k : ℕ} (E : Finset ι) (ends : ι → Finset V)
    (htwo : ∀ e ∈ E, (ends e).card = 2) (col : ι → Fin k)
    (hproper : ∀ e ∈ E, ∀ e' ∈ E, e ≠ e' → col e = col e' → Disjoint (ends e) (ends e')) :
    E.card ≤ k * (Fintype.card V / 2) := by
  classical
  have hsplit : E.card = ∑ c : Fin k, (E.filter fun e => col e = c).card :=
    Finset.card_eq_sum_card_fiberwise (fun e _ => Finset.mem_univ (col e))
  rw [hsplit]
  calc ∑ c : Fin k, (E.filter fun e => col e = c).card ≤ ∑ _c : Fin k, Fintype.card V / 2 := by
        refine Finset.sum_le_sum fun c _ => card_le_half_of_matching _ ends ?_ ?_
        · intro e he
          exact htwo e (Finset.mem_filter.mp he).1
        · intro e he e' he' hne
          have he1 := Finset.mem_filter.mp (Finset.mem_coe.mp he)
          have he2 := Finset.mem_filter.mp (Finset.mem_coe.mp he')
          exact hproper e he1.1 e' he2.1 hne (he1.2.trans he2.2.symm)
    _ = k * (Fintype.card V / 2) := by
        rw [Finset.sum_const, smul_eq_mul, Finset.card_univ, Fintype.card_fin]

/-- **The colour label costs one bond at odd `A ≥ 5`.** At `A = 5` with `k = 3`: valence allows
`⌊15/2⌋ = 7` bonds, colour labels allow `3·⌊5/2⌋ = 6`. -/
theorem tait_lt_valence_at_five : 3 * (5 / 2) < (3 * 5) / 2 := by norm_num

/-- In general the two caps agree at even `A` and differ by one at odd `A`. -/
theorem tait_vs_valence (A : ℕ) :
    (3 * A) / 2 = 3 * (A / 2) + (if A % 2 = 1 then 1 else 0) := by
  rcases Nat.even_or_odd A with ⟨m, rfl⟩ | ⟨m, rfl⟩
  · have : (m + m) % 2 = 0 := by omega
    simp only [this, show ¬ ((0 : ℕ) = 1) from by norm_num, if_false]
    omega
  · have : (2 * m + 1) % 2 = 1 := by omega
    simp only [this, if_true]
    omega

section Energy

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **An attractive bond rewards the cap.** With bond value `b > 0`, the binding `b·M` of any bond
count `M ≤ cap` is at most `b·cap`, with equality exactly at `M = cap`. -/
theorem binding_le_of_card_le (b : R) (hb : 0 < b) (M cap : ℕ) (h : M ≤ cap) :
    b * M ≤ b * cap ∧ (b * M = b * cap ↔ M = cap) := by
  refine ⟨mul_le_mul_of_nonneg_left (by exact_mod_cast h) hb.le, ?_⟩
  constructor
  · intro heq
    exact_mod_cast mul_left_cancel₀ hb.ne' heq
  · rintro rfl
    rfl

/-- **Per-nucleon bond count under a valence cap.** `2M ≤ kA` gives `M/A ≤ k/2`. At `k = 2`
(the Artin chain's degree bound) this is `1`; at `k = N_c = 3` it is `3/2`. -/
theorem perNucleon_le_of_valence (M A k : ℕ) (hA : 0 < A) (h : 2 * M ≤ k * A) :
    (M : R) / A ≤ (k : R) / 2 := by
  have hA' : (0 : R) < A := by exact_mod_cast hA
  rw [div_le_div_iff₀ hA' (by norm_num : (0 : R) < 2)]
  have : ((2 * M : ℕ) : R) ≤ ((k * A : ℕ) : R) := by exact_mod_cast h
  push_cast at this
  linarith

end Energy

end QOU.MassTheory.NucleusBondValence
