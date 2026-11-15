/-
  # S_5 action on H_n(q) at the electroweak slice

  Lemma 1 of the N_v derivation chain.  Asserts that the
  Iwahori-Hecke algebra at the EW slice of the brane tower carries
  a faithful S_5-action with |S_5| = 120 acting as the Markov-trace
  rescaling factor.

  Status: conjecture.  Per AGENTS.md §3b, axiomatised as a Lean
  class with sorry-fields encoding the structural content.

  Ref: [leitner2026] `prop:n-v-bring-action`,
       `prop:brings-is-qou`,
       `def:hyperelliptic-quintic`,
       \cite{bring1786}, \cite{klein1888} (Bring/Klein curve).
-/

import Mathlib.Algebra.Algebra.Basic
import Mathlib.GroupTheory.SpecificGroups.Alternating
import Mathlib.Data.Real.Basic

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
noncomputable opaque tau_M_EW (slice : ElectroweakSlice) (x : HeckeAtEW slice) : ℝ

/-- The Frobenius co-Casimir trace at the EW slice (the
    `Σ_λ 1/dim_q(λ)` value restricted to the EW Wedderburn blocks). -/
noncomputable opaque tau_M_C_dim_q_EW (slice : ElectroweakSlice) : ℝ

/-- The categorical Markov-trace-residual rescaling factor that
    converts the universal Frobenius co-Casimir trace into the
    EW-scale invariant `N_v / q_0^L`. -/
noncomputable opaque rescale_EW (slice : ElectroweakSlice) : ℝ

/- ## The substrate claim (S_5-EW-1)

   Until 2026-09-03 this was an `axiom`. It is now the content of the
   `NVBringAction` class below, carried as an explicit hypothesis rather
   than assumed globally.

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

      (2) Construct the `S_5`-action on `HeckeAtEW slice` from the
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
    [leitner2026] `prop:brings-is-qou` for the Bring-as-QOU-substrate
    identification. -/
/-- **`conj:n-v-bring-action` (axiomatised as a typeclass).**

    The §3b-cond carrier: downstream blocks take `[NVBringAction slice]`
    as a typeclass hypothesis and are then genuinely conditional on it.

    **There is deliberately NO instance.** Until 2026-09-03 this file also
    carried `axiom s5_acts_on_ew_slice` together with

        instance instance_from_axiom (slice) : NVBringAction slice where
          rescale_eq := s5_acts_on_ew_slice slice

    and that combination defeated the whole point of the class: instance
    resolution supplies the hypothesis silently, so a downstream author who
    simply omits `[NVBringAction slice]` gets an axiom-backed theorem whose
    *statement is identical* to the conditional one. Measured on two
    theorems with the same statement, one written each way:

        downstream_conditional   -> [propext, Classical.choice, Quot.sound]
        downstream_unconditional -> [..., QOU.Observations.s5_acts_on_ew_slice]

    AGENTS.md §3b-tax: "An unproved primary is honestly represented by a
    content-bearing class with NO instance (the open state); do not
    fabricate a trivial instance to 'close' it." A global instance
    discharging the class from a global axiom is exactly that fabrication,
    so both are gone and the file is now axiom-free. Constructing a genuine
    instance — deriving the S_5 action rather than assuming it — is the open
    work (bean `qou-5lib`). -/
-- Ref: [bring1786], [klein1888]
class NVBringAction (slice : ElectroweakSlice) : Prop where
  /-- Rescaling identity: $\tau_{M,C}^{\mathrm{EW}}(\Sigma) \cdot
      \mathrm{rescale}_{EW}(\Sigma) = 120 \cdot
      \tau_{M,C}^{\mathrm{EW}}(\Sigma)$. -/
  rescale_eq :
    tau_M_C_dim_q_EW slice * rescale_EW slice = 120 * tau_M_C_dim_q_EW slice

/-- **Corollary.** The rescaling factor at the EW slice equals 120
    whenever the Markov co-Casimir trace at that slice is nonzero.

    This isolates the structural content of `s5_acts_on_ew_slice`:
    the `|S_5| = 120` factor is a *property of the rescaling*,
    independent of the trace's particular value.  Cancellation
    requires `tau_M_C_dim_q_EW slice ≠ 0`, which holds at generic q
    by the non-degeneracy of the canonical Jones-Markov trace
    (`prop:markov-trace-frobenius-selection`).

    Conditional on `[NVBringAction slice]` (§3b-cond item 2), not on a
    global axiom: divide the class field by `tau_M_C_dim_q_EW slice`. -/
theorem rescale_EW_eq_120 (slice : ElectroweakSlice)
    [inst : NVBringAction slice]
    (h : tau_M_C_dim_q_EW slice ≠ 0) :
    rescale_EW slice = 120 := by
  -- From the hypothesis: τ · r = 120 · τ.  Rewrite RHS as τ · 120
  -- (commute) and cancel τ from the left.
  have h2 : tau_M_C_dim_q_EW slice * rescale_EW slice
          = tau_M_C_dim_q_EW slice * 120 := by
    rw [inst.rescale_eq, mul_comm 120]
  exact mul_left_cancel₀ h h2

end QOU.Observations
