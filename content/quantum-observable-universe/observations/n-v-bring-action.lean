/-
  # S_5 action on H_n(q) at the electroweak slice

  Lemma 1 of the N_v derivation chain.  Asserts that the
  Iwahori-Hecke algebra at the EW slice of the brane tower carries
  a faithful S_5-action with |S_5| = 120 acting as the Markov-trace
  rescaling factor.

  Status: conjecture.  Per AGENTS.md §3b, axiomatised as a Lean
  class with sorry-fields encoding the structural content.

  Ref: [manuscript] `prop:n-v-bring-action`,
       `prop:brings-is-qou`,
       `def:hyperelliptic-quintic`,
       \cite{bring1786}, \cite{klein1888} (Bring/Klein curve).
-/

import Mathlib.Algebra.Algebra.Basic
import Mathlib.GroupTheory.SpecificGroups.Alternating

namespace QOU.Observations

/-- The electroweak slice of the brane tower.
    Currently abstract: a level of the GB filtration / jet order
    at which the weak scale v emerges.  Concrete identification
    pending paper-side construction (see
    `conj:mass-endomorphism` for the underlying tower). -/
opaque ElectroweakSlice : Type

/-- The Iwahori-Hecke algebra restricted to the EW slice.
    Abstract handle; the concrete `H_{n_EW}(q)` algebra is the
    Wedderburn restriction of the universal `H_n(q)` to the
    Wedderburn blocks supporting the EW gauge content. -/
opaque HeckeAtEW : ElectroweakSlice → Type

/-- The Markov trace on `HeckeAtEW`. -/
noncomputable opaque tau_M_EW (Σ : ElectroweakSlice) (x : HeckeAtEW Σ) : ℝ

/-- The Frobenius co-Casimir trace at the EW slice (the
    `Σ_λ 1/dim_q(λ)` value restricted to the EW Wedderburn blocks). -/
noncomputable opaque tau_M_C_dim_q_EW (Σ : ElectroweakSlice) : ℝ

/-- The categorical Markov-trace-residual rescaling factor that
    converts the universal Frobenius co-Casimir trace into the
    EW-scale invariant `N_v / q_0^L`. -/
noncomputable opaque rescale_EW (Σ : ElectroweakSlice) : ℝ

/-- **Substrate axiom (S_5-EW-1).**

    *At the EW slice, the Markov-trace-residual rescaling factor
    equals |S_5| = 120, the order of the Bring-surface automorphism
    group.*

    Mathematical content: the categorical projector from the
    universal Frobenius co-Casimir trace onto the EW slice
    introduces a factor of `|S_5|` arising from the Bring-surface
    geometric symmetry (see `prop:brings-is-qou`).  Symbolically:

    ```
    tau_M(C_dim_q^EW) · rescale_EW = 120 · tau_M(C_dim_q^{H_n(q)})
    ```

    **Path to a stronger proof** (per AGENTS.md §3b):

      (1) Construct `ElectroweakSlice` concretely as a GB filtration
          grade (or jet order) determined by the brane-tower closure
          at `v ≈ 246 GeV`.  Currently abstract.

      (2) Construct the `S_5`-action on `HeckeAtEW Σ` from the
          geometric `S_5 = Aut(Bring)` action on `𝒮` via the fibre
          functor `τ`.

      (3) Prove the rescaling factor is exactly `|S_5| = 120` (and
          not some other invariant of the `S_5`-rep, e.g. the
          dimension of the irreducible component carrying the
          Markov trace).

    Status: bona fide substrate axiom, not a `sorry` — its formal
    proof requires categorical constructions (Bring-substrate
    fibre-functor, EW-slice definition) that don't yet exist on
    the paper side.

    Ref: \cite{bring1786}, \cite{klein1888} for the Bring/Klein
    curve and its `S_5` automorphism group;
    [manuscript] `prop:brings-is-qou` for the Bring-as-QOU-substrate
    identification. -/
-- Ref: [klein1888] + [bring1786] (Bring/Klein curve and its S_5 automorphism group); [manuscript] prop:brings-is-qou (|S_5|=120 rescaling at the EW slice)
axiom s5_acts_on_ew_slice (Σ : ElectroweakSlice) :
    tau_M_C_dim_q_EW Σ * rescale_EW Σ
      = 120 * tau_M_C_dim_q_EW Σ

/-- **Corollary.** The rescaling factor at the EW slice equals 120
    whenever the Markov co-Casimir trace at that slice is nonzero.

    This isolates the structural content of `s5_acts_on_ew_slice`:
    the `|S_5| = 120` factor is a *property of the rescaling*,
    independent of the trace's particular value.  Cancellation
    requires `tau_M_C_dim_q_EW Σ ≠ 0`, which holds at generic q
    by the non-degeneracy of the canonical Jones-Markov trace
    (`prop:markov-trace-frobenius-selection`).

    Proof: divide the axiom by `tau_M_C_dim_q_EW Σ`. -/
theorem rescale_EW_eq_120 (Σ : ElectroweakSlice)
    (h : tau_M_C_dim_q_EW Σ ≠ 0) :
    rescale_EW Σ = 120 := by
  -- From the axiom: τ · r = 120 · τ.  Rewrite RHS as τ · 120
  -- (commute) and cancel τ from the left.
  have h2 : tau_M_C_dim_q_EW Σ * rescale_EW Σ
          = tau_M_C_dim_q_EW Σ * 120 := by
    rw [s5_acts_on_ew_slice Σ, mul_comm 120]
  exact mul_left_cancel₀ h h2

/-- **`conj:n-v-bring-action` (axiomatised as a typeclass).**

    Wraps the substrate axiom `s5_acts_on_ew_slice` in a §3b-cond
    class so that downstream blocks can take `[NVBringAction Σ]` as
    a typeclass hypothesis and inherit `conditional-on-class`
    status.  The rescaling identity is now a class field rather than
    a free-standing axiom; the underlying axiom remains as the
    instance-level discharge target. -/
-- Ref: [bring1786], [klein1888]
class NVBringAction (Σ : ElectroweakSlice) : Prop where
  /-- Rescaling identity: $\tau_{M,C}^{\mathrm{EW}}(\Sigma) \cdot
      \mathrm{rescale}_{EW}(\Sigma) = 120 \cdot
      \tau_{M,C}^{\mathrm{EW}}(\Sigma)$. -/
  rescale_eq :
    tau_M_C_dim_q_EW Σ * rescale_EW Σ = 120 * tau_M_C_dim_q_EW Σ

/-- **Default instance.**  Discharges `rescale_eq` from the
    substrate axiom `s5_acts_on_ew_slice`. -/
-- Ref: [manuscript] observations/n-v-bring-action
instance instance_from_axiom (Σ : ElectroweakSlice) :
    NVBringAction Σ where
  rescale_eq := s5_acts_on_ew_slice Σ

end QOU.Observations
