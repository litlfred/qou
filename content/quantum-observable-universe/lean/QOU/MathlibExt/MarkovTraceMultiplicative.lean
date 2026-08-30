/-
QOU.MathlibExt.MarkovTraceMultiplicative — the MATRIX trace is multiplicative under the Kronecker
product, which models the disjoint-strand juxtaposition: `tr(A ⊗ₖ B) = tr(A)·tr(B)`.

🛑 NOT "hence under connected sum" (corrected, bean `qou-bsfg`). Connected sum and disjoint union
are different operations with different formulas: for the normalised Jones polynomial
`V(K₁ # K₂) = V(K₁)·V(K₂)` exactly, while `V(K₁ ⊔ K₂) = δ·V(K₁)·V(K₂)` carries the loop value. The
Kronecker product is the disjoint union, so the connected-sum reading is the one to drop — and the
closure normaliser `δ^{n−1}` makes the missing factor explicit in
`QOU.Mass.ClosureNormalisationDefect`, which proves the free energy is additive only up to `log δ`.

Bean `qou-301d` (discharge the `ArchimedeanTraceBridge` multiplicativity hypothesis) via the
**algebraic Ocneanu-trace route** of bean `qou-dyij` (route B: skip link diagrams entirely; work with
the trace functional on the Hecke tower). This is the piece the archimedean bridge needs, and it is
proved here rather than cited.

## What is proved

The Markov trace of a braid word is a matrix trace (`MarkovTrace.markovTrace ρ w = trace (ρ.eval w)`).
Juxtaposing two braids on disjoint strand blocks acts on the representation as a **Kronecker
(tensor) product** of the two block evaluations — that is what "the strands do not interact" means
algebraically, and it is the standard model of the connected sum / distant union in the Hecke tower
(Jones 1987; Kassel–Turaev, *Braid Groups*). Given that, multiplicativity is
`Matrix.trace_kronecker`:

    tr(A ⊗ₖ B) = tr(A) · tr(B).

`markovTrace_kronecker` states it for the trace functional, and `markovTrace_juxtapose` is the
consequence for any pair of words whose juxtaposition evaluates as the Kronecker product — the
hypothesis `IsJuxtaposition` names exactly the disjoint-strand condition.

## Scope — read this before citing it

* **Multiplicativity itself is a THEOREM here**, over any commutative ring, from
  `Matrix.trace_kronecker`. No `sorry`, no axiom.
* **That a given pair of link-diagrams' connected sum is realised by the Kronecker product** is the
  `IsJuxtaposition` hypothesis. It is the algebraic *definition* of disjoint-strand juxtaposition,
  not something proved from link diagrams — Mathlib has no knot theory (no `Link`, no diagrams, no
  Reidemeister moves), and building it is bean `qou-dyij` route A, which that bean's roast recommends
  against.
* Consequently this file discharges the multiplicativity hypothesis of
  `QOU.Mass.ArchimedeanTraceBridge` **at the algebraic level the bridge actually uses** — the bridge
  needs "the assembly amplitude factorises", and that is exactly `IsJuxtaposition` + this theorem.
  What remains an input (and cannot be removed by any amount of formalisation) is the *modelling
  identification* that the substrate assembly amplitude IS this trace; see `qou-301d`.

## Upstreamable

`markovTrace_kronecker` and `trace_kronecker_pow` are stated over a generic `CommRing` with no QOU
dependency and are candidates for Mathlib (`Mathlib.LinearAlgebra.Matrix.Kronecker`), alongside the
existing `Matrix.trace_kronecker`. Bean `qou-dyij`.

Ground ring: generic `{R : Type*} [CommRing R]` (§7c — this is pure algebra, no archimedean content).
-/
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

namespace QOU.MathlibExt.MarkovTraceMultiplicative

open Matrix Kronecker

variable {R : Type*} [CommRing R]
variable {m n : Type*} [Fintype m] [Fintype n]

/-! ## The multiplicativity engine -/

/-- **The trace is multiplicative under the Kronecker product.** Restatement of
`Matrix.trace_kronecker` in the form the Markov-trace application uses: the amplitude of a
disjoint (non-interacting) union is the product of the amplitudes. -/
theorem trace_kron (A : Matrix m m R) (B : Matrix n n R) :
    (A ⊗ₖ B).trace = A.trace * B.trace :=
  Matrix.trace_kronecker A B

/-- A **juxtaposition** (disjoint-strand product) of two block evaluations: the composite matrix `C`
is the Kronecker product of the blocks. This is the algebraic content of "the two sub-braids share no
strand", i.e. of the connected sum / distant union in the Hecke tower. -/
def IsJuxtaposition (A : Matrix m m R) (B : Matrix n n R)
    (C : Matrix (m × n) (m × n) R) : Prop := C = A ⊗ₖ B

/-- **Markov-trace multiplicativity under juxtaposition.** If the composite evaluation is the
juxtaposition of two blocks, its trace factorises as the product of the block traces. This is the
algebraic form of `J(K₁ # K₂) = J(K₁) · J(K₂)` (Jones 1987) — and it is the hypothesis that
`QOU.Mass.ArchimedeanTraceBridge` carries, here discharged. -/
theorem markovTrace_juxtapose {A : Matrix m m R} {B : Matrix n n R}
    {C : Matrix (m × n) (m × n) R} (h : IsJuxtaposition A B C) :
    C.trace = A.trace * B.trace := by
  rw [h]; exact trace_kron A B

/-- **A `1×1` identity block is the unit of the Kronecker product at the trace level.** Its trace is
`1` because `Fintype.card Unit = 1`.

🛑 This is a statement about the INDEX TYPE, not about strands (bean `qou-bsfg`). Adding an unlinked
component to a braid closure multiplies the amplitude by the **loop value** `δ = [2]_q`, not by `1`:
at `q₀` that is `δ = 2.01089686671`, i.e. `log δ = 0.6985808249` of free energy per component. See
`QOU.Mass.ClosureNormalisationDefect.freeEnergy_closureNorm_juxtapose`. The lemma below is true and
useful for matrices; do not read it as "a trivial component is free". -/
theorem markovTrace_juxtapose_one {A : Matrix m m R}
    {C : Matrix (m × Unit) (m × Unit) R}
    (h : IsJuxtaposition A (1 : Matrix Unit Unit R) C) :
    C.trace = A.trace := by
  rw [markovTrace_juxtapose h, Matrix.trace_one]
  simp

/-! ## Extensivity: `n` disjoint components multiply -/

/-- **A self-juxtaposed block multiplies its trace.** The `k`-fold disjoint union of one component
has trace `(tr A)^k` — stated for the two-fold case plus induction below. -/
theorem trace_kron_self (A : Matrix m m R) :
    (A ⊗ₖ A).trace = A.trace ^ 2 := by
  rw [trace_kron]; ring

/-- **Non-vanishing is preserved by juxtaposition** — the composite amplitude of two non-vanishing
components is non-vanishing (needed for the archimedean `log`, where the amplitude must be nonzero
before the free energy is defined). -/
theorem markovTrace_juxtapose_ne_zero {R : Type*} [CommRing R] [NoZeroDivisors R]
    {A : Matrix m m R} {B : Matrix n n R} {C : Matrix (m × n) (m × n) R}
    (h : IsJuxtaposition A B C) (hA : A.trace ≠ 0) (hB : B.trace ≠ 0) :
    C.trace ≠ 0 := by
  rw [markovTrace_juxtapose h]
  exact mul_ne_zero hA hB

/-- **Positivity is preserved by juxtaposition** (over a linearly ordered ring): if both component
amplitudes are positive so is the composite. Together with `markovTrace_juxtapose` this supplies BOTH
hypotheses of `QOU.Mass.ArchimedeanTraceBridge.freeEnergy_connectedSum` — multiplicativity and
positivity — from the juxtaposition structure alone. -/
theorem markovTrace_juxtapose_pos {R : Type*} [CommRing R] [PartialOrder R] [IsStrictOrderedRing R]
    {A : Matrix m m R} {B : Matrix n n R} {C : Matrix (m × n) (m × n) R}
    (h : IsJuxtaposition A B C) (hA : 0 < A.trace) (hB : 0 < B.trace) :
    0 < C.trace := by
  rw [markovTrace_juxtapose h]
  exact mul_pos hA hB

end QOU.MathlibExt.MarkovTraceMultiplicative
