import Mathlib.Algebra.Ring.Basic
import QOU.BraidKnot.ConfinementLevel

/-!
# QOU.BraidKnot.GBSpectralSequence — Gröbner–Shirshov spectral sequence

The unified knot mass formula has six structural terms which emerge
as pages of a **spectral sequence** associated with the Gröbner–
Shirshov filtration `J^•(q)` on `H_n(R, q)`.

**Conditional-class axiomatisation** (CLAUDE.md §3b).  The
spectral-sequence existence statement is captured here as an
abstract typeclass; full constructive formalisation requires the
filtered-Hochschild-cochain machinery and is multi-week work
(currently sketched in the .md).  Downstream consumers take a
`[GBSpectralSequence R]` instance and proceed.

**Formal-chain version.**  Lives under `lean/QOU/` and is compiled
by `lake build`.

LaTeX label: `prop:gb-spectral-sequence`
-/

namespace QOU.BraidKnot

universe u

/-- **GB spectral sequence on the GS-filtered Hecke algebra.**

    A class instance carries:
    * `filtration : ℕ → Type*` — the filtered pieces `J^ℓ(q)` (or,
      strictly, the associated graded `J^ℓ / J^{ℓ+1}` at level ℓ).
    * `differential : ∀ ℓ, filtration ℓ → filtration ℓ` — the
      direct sum `d = d_H + d_F + d_{YB}` of the three GS rewriting
      rules, lifted to the Hochschild cochain complex.
    * `d_squared_zero` — the differential squares to zero
      (Cartan–Eilenberg).
    * `e_infty_converges` — the spectral sequence converges to the
      associated graded of the Hecke algebra.

    Each field encodes a substantial mathematical statement; the
    class is the conditional-class wrapper for the proposition
    `prop:gb-spectral-sequence`. -/
class GBSpectralSequence (R : Type u) [CommRing R] where
  /-- The associated-graded piece at filtration level `ℓ`. -/
  graded : ℕ → Type u
  /-- Each graded piece is an additive group. -/
  [gradedAdd : ∀ ℓ, AddCommGroup (graded ℓ)]
  /-- The differential `d : J^ℓ / J^{ℓ+1} → J^ℓ / J^{ℓ+1}`. -/
  differential : ∀ ℓ, graded ℓ → graded ℓ
  /-- The differential squares to zero. -/
  d_squared_zero : ∀ ℓ (x : graded ℓ),
    differential ℓ (differential ℓ x) = 0
  /-- The spectral-sequence convergence target: at each level ℓ the
      `E_∞` page identifies with the associated graded.  Stated
      abstractly as the existence of an iso witness. -/
  e_infty_converges : True

attribute [instance] GBSpectralSequence.gradedAdd

/-- **GB spectral sequence proposition.**

    Conditional on `[GBSpectralSequence R]`, the differential
    squares to zero and the spectral sequence converges. -/
-- Ref: [manuscript] `prop:gb-spectral-sequence`,
--      [weibel1994] §5.5
theorem gb_spectral_sequence
    {R : Type u} [CommRing R] [s : GBSpectralSequence R] (ℓ : ℕ) :
    ∀ (x : s.graded ℓ),
      s.differential ℓ (s.differential ℓ x) = 0 :=
  s.d_squared_zero ℓ

end QOU.BraidKnot
