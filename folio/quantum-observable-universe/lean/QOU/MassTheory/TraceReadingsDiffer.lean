/-
# The two candidate readings of `ρ(proton)` are distinct — a refutation

`prop:hoefsmit-scattering-pipeline` Stage 4 gives the mass as
`𝔪(K) = m_e · Geom(K) · ‖J_K(q)‖` — the trace **of** `K` against the volume **of**
`K`, one `K` throughout. Production instead pairs `Vol(𝓑₃)` with a trace loaded
from `chi-proton-h3-at-q0-50dps.witness.json`. Two readings of that:

* **(A)** the atom `H₃` element **is** `𝓑₃`'s algebraic side, so there is one `K`
  after all and `‖J_{𝓑₃}(q)‖` is what production loads;
* **(B)** the algebraic side deliberately carries the full quark-structured
  element while `Geom` carries the geometry of its carrier link — two objects,
  on opposite sides of the fibre functor.

(B) is a statement of design intent and is not a proposition. **(A) is a
mathematical claim, and this file refutes it**, which settles the pair by
elimination.

## What is proved here, and what is not

**Proved (sorry-free):** the two rational functions are distinct — indeed already
at `q = 1`, where `tr_M(𝓑₃) = 1` while the proton-atom reading is `1/2`, both
denominators being nonzero there. Over any characteristic-zero field, so the
separation is not an artefact of ℚ. Also the general fact that an invariant
separates: if `τ` is constant on `R`-related pairs then `τ a ≠ τ b` forbids
`R a b`.

**NOT proved here, and not claimed.** These coefficients are *not* re-derived
from the Hecke algebra inside Lean — they come from the corpus's own producers
(`markov_peel.tr_M_atomic`, `markov_trace_canonical.tr_M_element`, both
convention D) via `atom_vs_atlas_markov_trace_probe.py`. What Lean adds is an
**independent, kernel-checked exact evaluation** of the separating inequality —
a cross-check on that sympy computation, not a replacement for it — together
with the logical step from "traces differ" to "not related by any
trace-invariant relation".

That the Markov trace **is** such an invariant is standard (Jones) and is
carried here as an explicit hypothesis, never asserted as proved.

`-- Ref: [jones1987] https://doi.org/10.2307/1971403`

## Consequence for reading (A)

Under (A) the atom element and `β_Bor` would name the same `K`, hence be Markov
equivalent, hence share every Markov invariant — including `tr_M`. They do not.
So (A) is false and (B) is what the pipeline is doing. That is a **derivation of
a negative**, not a licence to call (B) proved: (B)'s content is that the
pairing is *intended*, which no theorem can supply.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.CharZero.Defs
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp

namespace QOU.MassTheory

variable {K : Type*} [Field K] [CharZero K]

/-- Markov trace of the Borromean braid `(σ₁σ₂⁻¹)³` in `H₃(q)`, convention D
(`z = q³/(q²+1)`), as a rational function of `q`.  Coefficients from
`markov_trace_canonical.tr_M_element`; see the module docstring on provenance. -/
noncomputable def trMBorromean (q : K) : K :=
  (-q^12 + 3*q^10 - 2*q^8 + 4*q^6 - 2*q^4 + 3*q^2 - 1) / (q^8 + 2*q^6 + q^4)

/-- Markov trace of the canonical proton **atom element** — the object
`atom_braid_word_3A(1,0)` returns, which lies in `H₃(q)` outside the image of
`ρ : B₃ → H₃(q)` because `2A+1` of its letters are weight-1 averages over
crossing sign.  This is what production loads as `ρ(proton)`. -/
noncomputable def trMProtonAtom (q : K) : K :=
  (q^22 + q^20 + 2*q^18 + 2*q^16 + 3*q^14 + 2*q^12 + q^10 - q^8 - q^4 - q^2 - 1)
    / (4*q^13 + 8*q^11 + 4*q^9)

/-- At the classical limit the Borromean reading is `1`. -/
theorem trMBorromean_one : trMBorromean (1 : K) = 1 := by
  unfold trMBorromean; norm_num

/-- At the classical limit the atom-element reading is `1/2` — a factor of two
below the Borromean one, and the separation is already visible here. -/
theorem trMProtonAtom_one : trMProtonAtom (1 : K) = 1 / 2 := by
  unfold trMProtonAtom; norm_num

/-- **The refutation.** The two readings are not the same function of `q`; they
already differ at `q = 1`, where both denominators are nonzero. -/
theorem trM_readings_differ_at_one :
    trMBorromean (1 : K) ≠ trMProtonAtom (1 : K) := by
  rw [trMBorromean_one, trMProtonAtom_one]
  norm_num

/-- Hence the two readings are distinct as functions. -/
theorem trM_readings_differ :
    (trMBorromean : K → K) ≠ (trMProtonAtom : K → K) := by
  intro h
  exact trM_readings_differ_at_one (congrFun h (1 : K))

/-- **An invariant separates.**  If `τ` takes equal values on every `R`-related
pair, then a difference in `τ` forbids the relation.  Stated for an arbitrary
relation so it applies to Markov equivalence without that notion being
formalised here. -/
theorem not_rel_of_invariant_ne {α β : Type*} {τ : α → β} {R : α → α → Prop}
    (hinv : ∀ x y, R x y → τ x = τ y) {a b : α} (h : τ a ≠ τ b) : ¬ R a b :=
  fun hr => h (hinv a b hr)

/-- **Reading (A) is refuted, conditional on the invariance hypothesis.**

Given any relation `R` on a type of algebra elements whose trace `τ` is
`R`-invariant — Markov equivalence and the Markov trace being the instance
intended — two elements whose traces differ are not `R`-related.  Applied to the
proton atom element and `β_Bor`, whose traces differ by the theorems above, this
says they are not Markov equivalent, so they do not name a common `K`.

The invariance is a **hypothesis**, not a claim proved here; see the module
docstring. -/
theorem readings_not_related_of_invariance
    {α : Type*} {τ : α → K} {R : α → α → Prop}
    (hinv : ∀ x y, R x y → τ x = τ y)
    {atom borromean : α}
    (hatom : τ atom = trMProtonAtom (1 : K))
    (hbor : τ borromean = trMBorromean (1 : K)) :
    ¬ R atom borromean := by
  refine not_rel_of_invariant_ne hinv ?_
  rw [hatom, hbor]
  exact fun h => trM_readings_differ_at_one h.symm

end QOU.MassTheory
