/-!
# QOU.LiftingDescent.IterativeBraneTower — magic ladder from iterative jet prolongations

Conjectural emergence of the magic ladder `{2, 8, 20, 28, 50, 82,
126}` as the sequence of strand counts where the iteratively-built
brane tower at substrate `q_0` crosses a shell-condensation
threshold.

The brane tower is a sequence `Φ_0, Φ_1, Φ_2, ...` of categorical
mass endomorphisms, each obtained from the previous via Yekutieli
jet prolongation (one strand added). The threshold predicate
`Threshold_{q_0}(Φ_n)` checks whether the n-th jet's obstruction
class vanishes; magic n is the set of strand counts where this
holds.

LaTeX label: `conj:magic-from-iterative-brane-tower`

## References

- [yekutieli2010] https://doi.org/10.1142/9789814322188
- [yekutieli2008] https://doi.org/10.1112/jlms/jdn020
- [mathas1999] https://doi.org/10.1090/ulect/015
- [hoefsmit1974] — Hoefsmit, Representations of Hecke algebras
- [manuscript] lifting-and-descent / magic-from-iterative-brane-tower
-/

import QOU.LiftingDescent.HomologicalCondensation
import Mathlib.Data.Set.Basic

namespace QOU.LiftingDescent.IterativeBraneTower

open QOU.LiftingDescent.HomologicalCondensation

/-! ## §1  Brane-tower state surrogate -/

/-- Surrogate type for the state of the brane tower at level `n` and
    substrate `q`. Concrete instances will package the Hoefsmit
    block-diagonal data, the GB filtration depth, and the q-Pochhammer
    partial product up to the Yekutieli truncation depth. -/
opaque BraneTowerState (n : ℕ) (q : ℝ) : Type

/-- Yekutieli jet-prolongation step: extend the brane-tower state by
    one strand, adding one transient contribution `Φ_q(z_{n+1})`. -/
opaque jetProlongation (q : ℝ) :
    {n : ℕ} → BraneTowerState n q → BraneTowerState (n + 1) q

/-! ## §2  The threshold predicate -/

/-- Iterative shell-condensation threshold. `Threshold q s` holds
    when the state `s : BraneTowerState n q` has all jet-prolongation
    obstruction classes `J^k(Φ_n)` zero in `E_2^{*, k}` for every
    `k > 0`. -/
opaque Threshold (q : ℝ) {n : ℕ} (s : BraneTowerState n q) : Prop

/-! ## §3  Iterative emergence conjecture -/

/-- **Conjecture (Proposition 6).** For substrate `q = q_0`, the
    set of strand counts `n` at which the iteratively-built brane
    tower crosses the shell-condensation threshold equals the magic
    ladder `{2, 8, 20, 28, 50, 82, 126}`.

    Concrete instances supply:
    - The substrate constant `q_0_value : ℝ`;
    - The initial vacuum state `vacuumState : BraneTowerState 0 q_0`;
    - And verify that `Threshold` holds exactly on the magic
      ladder under iterated `jetProlongation`.

    The claim is exposed as a typeclass field for downstream
    theorems that consume the iterative emergence. -/
-- Ref: [manuscript] conj:magic-from-iterative-brane-tower
class MagicEmergesIteratively where
  /-- Substrate parameter value. -/
  q_0_value : ℝ
  /-- Substrate is in the substrate regime `q > 1`. -/
  q_0_pos : 1 < q_0_value
  /-- Initial (vacuum) state. -/
  vacuumState : BraneTowerState 0 q_0_value
  /-- The iterated state at level `n` is constructed by repeated
      jet prolongation from the vacuum. We name it abstractly. -/
  stateAt : ∀ (n : ℕ), BraneTowerState n q_0_value
  /-- Vacuum is at level zero. -/
  vacuum_eq : stateAt 0 = vacuumState
  /-- Successor states arise by jet prolongation. -/
  successor :
    ∀ (n : ℕ), stateAt (n + 1) = jetProlongation q_0_value (stateAt n)
  /-- The conjectural emergence: threshold holds iff `n` is magic. -/
  threshold_iff_magic :
    ∀ (n : ℕ),
      Threshold q_0_value (stateAt n) ↔ n ∈ magicLadder

/-- Re-export: at magic `n`, the iteratively-built brane tower
    state at level `n` crosses the shell-condensation threshold. -/
-- Ref: [manuscript] conj:magic-from-iterative-brane-tower
theorem threshold_at_magic
    [E : MagicEmergesIteratively]
    {n : ℕ} (hn : n ∈ magicLadder) :
    Threshold E.q_0_value (E.stateAt n) :=
  (E.threshold_iff_magic n).mpr hn

/-- Re-export: if the brane-tower state at level `n` crosses the
    threshold, then `n` is on the magic ladder. -/
-- Ref: [manuscript] conj:magic-from-iterative-brane-tower
theorem magic_of_threshold
    [E : MagicEmergesIteratively]
    {n : ℕ} (ht : Threshold E.q_0_value (E.stateAt n)) :
    n ∈ magicLadder :=
  (E.threshold_iff_magic n).mp ht

/-- The magic ladder cumulative-jump structure: between consecutive
    magic numbers, no threshold crossing occurs. This is a direct
    corollary of the iff above. -/
-- Ref: [manuscript] conj:magic-from-iterative-brane-tower
theorem no_threshold_between_magic
    [E : MagicEmergesIteratively]
    {n : ℕ} (h_not_magic : n ∉ magicLadder) :
    ¬ Threshold E.q_0_value (E.stateAt n) := by
  intro h
  exact h_not_magic (magic_of_threshold h)

end QOU.LiftingDescent.IterativeBraneTower
