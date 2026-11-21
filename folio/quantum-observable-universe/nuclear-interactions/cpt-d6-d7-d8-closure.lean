import Mathlib.Algebra.Ring.Defs
import Mathlib.Logic.Function.Basic

/-!
# `conj:cpt-d6-d7-d8-closure` — CPT closure compound conjecture

Parent conjecture for the discrete-symmetry trio: charge
conjugation, parity, and time reversal.
Each component (`conj:c-from-color-flavor-swap`,
`conj:p-from-braid-mirror`, `conj:t-from-trace-cyclicity`) names
a QOU-canonical realisation of one symmetry; the **joint**
statement is that they compose to give CPT preservation of the
Markov trace.

Axiomatised as a Lean class with no instance.  Downstream blocks that need
CPT-closure as a hypothesis take `[CPTClosure R B tr cpt]`.

## 2026-08-31 — the trace and the CPT action are PARAMETERS now

The class used to carry `ClosedBraid`, `markovTrace` and `cptComposite` as
**fields** alongside the conjecture, and the module docstring described it as
*"a Lean class with no instance"*.  That was false: `ClosedBraid := Unit`,
`markovTrace := fun _ => 0`, `cptComposite := id` inhabits it, so a
`[CPTClosure R]` binder assumed nothing about anything the caller brought.
An open conjecture is honestly represented by a **content-bearing class with
no instance** (AGENTS.md §3b-tax); a class whose own instance supplies the
objects the claim is about is not that.  `cpt_closure` then returned the
conjecture field directly — §3b-cond item 5 (bean `qou-z9ws`).

`ClosedBraid`, the trace and the composite are now class **parameters**, so
`[CPTClosure R B tr cpt]` constrains `tr` and `cpt` as the caller supplied
them.  No instance is provided; the class is still the conjecture.

**And one implication is now derived rather than asserted.**  The `.md` says
*"The three components are not logically independent; they collectively
constitute the conjecture"* — and the direction that matters is provable:
if each of `C`, `P`, `T` preserves the Markov trace, so does the composite
(`cptClosure_of_components`).  So the conjecture reduces to its three
component conjectures, which is what the `.md` claims and what the previous
encoding merely restated.

**What is still open**, stated rather than implied: that the three *named*
realisations — the colour-sheet flavour swap, the braid-diagram mirror, and
Markov-trace word reversal — each preserve `tr_M`.  Those are the three
component conjectures and none is proved here.

**Base ring (AGENTS.md §7c).** The Markov trace is the Jones invariant,
whose home is the Laurent ring $\mathbb{Z}[q, q^{-1}]$ — not the
archimedean completion.  The trace codomain is therefore a generic
`(R : Type*) [CommRing R]`, and the file never mentions `ℝ`.  An
archimedean evaluation of the invariant at the substrate $q_0$ is the
instantiation `R := ℝ`, which belongs on the observation side of the
substrate→archimedean wall.

`CommRing` is documentation of the invariant's actual home rather than
a proof obligation: the closure statement below is an equation between
two trace *values*, so it would type-check over a bare `Type`.  The
component conjectures (`conj:c-from-color-flavor-swap`,
`conj:p-from-braid-mirror`, `conj:t-from-trace-cyclicity`) do use the
ring structure — the bar involution $q \mapsto q^{-1}$ and the skein
relation — so weakening past `CommRing` would misname the object.
-/

namespace QOU.ParticleInteractions

/-- **A symmetry action preserves the Markov trace**:
`tr_M(f β) = tr_M(β)` for every closed-braid representative `β`.

Stated over a caller-supplied trace `tr` and action `f`.  This is the shape
each of `C`, `P`, `T` is conjectured to have, and the shape their composite
is conjectured to inherit. -/
-- Ref: [jones1987] V. Jones, Hecke algebra representations of braid groups
def PreservesMarkovTrace {B R : Type*} (tr : B → R) (f : B → B) : Prop :=
  ∀ b : B, tr (f b) = tr b

/-- **The claim of `conj:cpt-d6-d7-d8-closure`**: the composite `C · P · T`
preserves the Markov trace.

Named over caller-supplied data, **not asserted** — this is the conjecture.
The class below is its hypothesis-carrying form. -/
-- Ref: [leitner2026] conj:cpt-d6-d7-d8-closure
-- Ref: [wigner1937], [jones1987], [kassel1995]
def cpt_closure {B R : Type*} (markovTrace : B → R) (cptComposite : B → B) :
    Prop :=
  PreservesMarkovTrace markovTrace cptComposite

/-- The CPT-closure compound conjecture, as a class over the objects it is
about.

`B` is the closed-braid representative space, `markovTrace : B → R` the Jones
invariant valued in the generic coefficient ring `R` — canonically
$\mathbb{Z}[q, q^{-1}]$, never `ℝ` — and `cptComposite` the joint `C · P · T`
action.  All three are **parameters**, so a `[CPTClosure R B tr cpt]` binder
is a hypothesis about the caller's trace and action.

No instance is supplied; the class *is* the conjecture. -/
-- Ref: [leitner2026] prop:cpt-orbit-closure-density (substrate-side density)
-- Ref: [leitner2026] def:bar-involution (categorical CPT building block)
-- Ref: [wigner1937], [jones1987], [kassel1995]
class CPTClosure (R : Type*) [CommRing R] (B : Type*)
    (markovTrace : B → R) (cptComposite : B → B) : Prop where
  /-- **The conjecture itself** (joint closure of the three symmetries): the
      CPT composite preserves the Markov trace on every closed braid. -/
  cpt_trace_preserved : cpt_closure markovTrace cptComposite

/-- **CPT closure follows from its three components.**

If each of charge conjugation, parity and time reversal preserves the Markov
trace, then so does `C ∘ P ∘ T`.  This is the reduction the `.md` asserts
when it says the three components *"collectively constitute the
conjecture"*, and it is derived rather than assumed.

What remains open is each component hypothesis — that the colour-sheet
flavour swap, the braid-diagram mirror and Markov-trace word reversal are the
right realisations and are individually trace-preserving. -/
-- Ref: [leitner2026] conj:c-from-color-flavor-swap
-- Ref: [leitner2026] conj:p-from-braid-mirror
-- Ref: [leitner2026] conj:t-from-trace-cyclicity
theorem cptClosure_of_components {B R : Type*} (tr : B → R) (C P T : B → B)
    (hC : PreservesMarkovTrace tr C)
    (hP : PreservesMarkovTrace tr P)
    (hT : PreservesMarkovTrace tr T) :
    cpt_closure tr (C ∘ P ∘ T) := by
  intro b
  show tr (C (P (T b))) = tr b
  rw [hC (P (T b)), hP (T b), hT b]

end QOU.ParticleInteractions
