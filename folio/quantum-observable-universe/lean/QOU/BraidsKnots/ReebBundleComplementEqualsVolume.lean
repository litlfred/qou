import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic

/-!
# QOU.BraidsKnots.ReebBundleComplementEqualsVolume

**Proposition** ([`prop:reeb-bundle-complement-equals-volume`](../../../mass-theory/reeb-bundle-complement-equals-volume.md)),
conditional on [`conj:mass-volume-factorization`](../../../mass-theory/mass-volume-factorization.md).

*Let `𝓡_p ≅ S³` be the Reeb bundle and `K_β` the closure of the colour-tube
trajectory under `β ∈ B₃`.  The categorical Markov-trace observable equals
the JSJ-graded sum over the hyperbolic pieces `P_i` of the knot complement
`𝓡_p \ ν(K_β)`:*

    tr_M(ρ(β)) = Σ_{P_i hyperbolic} ρ_F(P_i) · V_hyp(P_i).

## 2026-09-03 — a second class of the same name, and the JSJ sum collapsed

This file declared `QOU.BraidsKnots.MassVolumeFactorization` with three
fields — `markov_trace : ℝ`, `jsj_volume_sum : ℝ`, and
`factorization_identity : markov_trace = jsj_volume_sum` — and
`ReebBundleComplementEqualsVolume` returned that field.  It cited AGENTS.md
§3b-cond for the pattern, and it is the case §3b-cond **item 5** forbids: the
class carries the block's own conclusion, so the "conditional theorem" derives
nothing and a `[MassVolumeFactorization]` binder assumes nothing (both reals
are chosen by the instance).

**The conjecture already has a carrier, and this was a second one under the
same name.**
[`QOU.ParticleInteractions.MassVolumeFactorization`](../../../mass-theory/mass-volume-factorization.lean)
is the real one, and it has the shape §3b-cond actually describes:
parameterised over the link configuration `K` and strand count `n`, with
`density`, `volume` and `mass` as **functions on `K`** and
`factorization : ∀ k : K, mass k = (density k).value * volume k`.  That field
quantifies over the caller's `K`, so the binder constrains caller data.  The
two classes share only a name and live in different namespaces; nothing
imports this one (grep across `content/` matches the *other* declaration).

**And the degenerate re-declaration erased the proposition's content.**
Collapsing `Σ_{P_i hyperbolic} ρ_F(P_i)·V_hyp(P_i)` into a single opaque
`jsj_volume_sum` removes the JSJ grading — which is the whole of what
"JSJ-graded volume sum" means, and the reason the block is a distinct
proposition rather than a restatement of the conjecture.

## Disposition: name it, assert nothing (AGENTS.md §1a, disposition 3)

`ReebBundleComplementEqualsVolume` now states the identity **with the sum
explicit**, over caller-supplied data, and asserts none of it.  Two
consequences the `.md` itself asserts are **derived** from it:

* `markovTrace_eq_zero_of_no_hyperbolic_pieces` — when no piece is
  hyperbolic the sum is empty and `tr_M(ρ(β)) = 0`.  This is the `.md`'s
  *"pure-rotation 3-cycles trace Heegaard torus trajectories, leaving a
  Seifert-fibered complement where `V_hyp = 0`"*.
* `markovTrace_eq_zero_of_volumes_vanish` — the same conclusion from
  vanishing volumes rather than an empty piece set, which is the other
  reading of that sentence.  Both are now theorems, so the JSJ grading is
  doing work instead of being a name.

## What is still open

The conjecture itself, and everything geometric: nothing here constructs the
Reeb bundle `𝓡_p`, the colour-tube closure `K_β`, the JSJ decomposition of
`𝓡_p \ ν(K_β)`, the Thurston volume, the Frobenius packing density `ρ_F`, or
the Markov trace.  They are a finite index set and two functions the caller
supplies.  The substantive bridge lives in `QOU.PhiQJSJ.bridge`.

Bean `qou-z9ws`.

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/reeb-bundle-complement-equals-volume.md
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/mass-volume-factorization.md
-/

namespace QOU.BraidsKnots

/-- **The claim of `prop:reeb-bundle-complement-equals-volume`**, as a
proposition over caller-supplied data:

    tr_M(ρ(β)) = Σ_{P_i ∈ hyperbolicPieces} ρ_F(P_i) · V_hyp(P_i).

**Named, not asserted**, and conditional on `conj:mass-volume-factorization`.
The sum is explicit rather than collapsed into one scalar — see the module
docstring for why that distinction is the proposition's content. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/reeb-bundle-complement-equals-volume.md
def ReebBundleComplementEqualsVolume {P : Type} (hyperbolicPieces : Finset P)
    (rhoF volHyp : P → ℝ) (markovTrace : ℝ) : Prop :=
  markovTrace = hyperbolicPieces.sum (fun p => rhoF p * volHyp p)

/-- **The Seifert-fibered case, derived**: no hyperbolic piece ⇒ the
observable vanishes.

The `.md`'s *"pure-rotation 3-cycles trace Heegaard torus trajectories,
leaving a Seifert-fibered complement where `V_hyp = 0`"* — obtained from the
graded sum rather than assumed. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/reeb-bundle-complement-equals-volume.md
theorem markovTrace_eq_zero_of_no_hyperbolic_pieces {P : Type}
    {rhoF volHyp : P → ℝ} {markovTrace : ℝ}
    (h : ReebBundleComplementEqualsVolume (∅ : Finset P) rhoF volHyp
          markovTrace) :
    markovTrace = 0 := by
  simpa [ReebBundleComplementEqualsVolume] using h

/-- **The vanishing-volume case, derived**: pieces present but all of zero
Thurston volume ⇒ the observable vanishes.

The other reading of the same sentence in the `.md`. Stated separately
because an empty piece set and a set of volume-zero pieces are different
geometric situations that happen to share a conclusion. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/reeb-bundle-complement-equals-volume.md
theorem markovTrace_eq_zero_of_volumes_vanish {P : Type}
    {hyperbolicPieces : Finset P} {rhoF volHyp : P → ℝ} {markovTrace : ℝ}
    (hvol : ∀ p ∈ hyperbolicPieces, volHyp p = 0)
    (h : ReebBundleComplementEqualsVolume hyperbolicPieces rhoF volHyp
          markovTrace) :
    markovTrace = 0 := by
  simp only [ReebBundleComplementEqualsVolume] at h
  rw [h]
  exact Finset.sum_eq_zero (fun p hp => by rw [hvol p hp, mul_zero])

/-- **The identity is refutable at freely-chosen data**, which is why it is
named rather than carried as a `sorry`.

With no hyperbolic pieces the sum is empty, so a nonzero observable fails. -/
theorem not_ReebBundleComplementEqualsVolume_of_free_data :
    ¬ ReebBundleComplementEqualsVolume (∅ : Finset ℕ)
        (fun _ => 0) (fun _ => 0) 1 := by
  simp [ReebBundleComplementEqualsVolume]

end QOU.BraidsKnots
