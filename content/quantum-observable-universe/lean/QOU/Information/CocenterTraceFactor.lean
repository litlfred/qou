import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.Quotient.Basic

/-!
# QOU.Information.CocenterTraceFactor — the trace factors through `HH₀ = A/[A,A]`

Sharpens the `[Q,M]` operator lemma (`MagnitudeTraceCommutator`) to the exact
homological home of the magnitude/decision split. The magnitude functional
`M = tr_M` is a **trace**, so it not only *kills* the commutator subspace
`[A,A]` — it **factors through the cocenter**

    HH₀(A) = A / [A,A]

(the zeroth Hochschild homology). This file formalizes that, sorry-free, for any
`R`-algebra `A`, and instantiates it for the Markov-trace model
`A = End V`, `M = LinearMap.trace`.

**Why this is the P-vs-NP-relevant sharpening.** `HH₀(A)` is the space of *trace
functionals* — the **magnitude axis**. Every such functional is a function of the
cocenter class alone, so it is blind to the complementary `[A,A]` — the
**decision/quantifier axis** (`MagnitudeAxisBoundary`). A decision-separating
invariant would therefore have to be a **non-trace** functional: not a class in
`HH₀`, but a cocycle in `HH₁` (outer derivations). For the Iwahori–Hecke algebra
`H_n(q)` the cocenter `HH₀(H_n(q))` and the commutator subspace `[H,H]` have an
explicit basis of minimal-length conjugacy-class representatives (Xuhua He's
cocenter / density theorems); the search for a decision functional is the search
for a `HH₁` class, which (at generic `q`, where `H_n(q)` is semisimple) *vanishes*
— it can live only at the root-of-unity / fibre level. This file supplies the
`HH₀` half rigorously; the `HH₁` search stays open.

Base ring generic `{R : Type*} [CommRing R]` (§7c: no archimedean structure). -/

namespace QOU.Information

variable (R : Type*) [CommRing R] (A : Type*) [Ring A] [Algebra R A]

/-- The **commutator submodule** `[A,A]` — the `R`-span of all `a·b − b·a`. -/
def commutatorSubmodule : Submodule R A :=
  Submodule.span R {x | ∃ a b : A, x = a * b - b * a}

/-- The **cocenter** `HH₀(A) = A / [A,A]` — the target of every trace functional. -/
abbrev cocenter : Type _ := A ⧸ commutatorSubmodule R A

variable {R A}

/-- **A trace functional kills `[A,A]` (sorry-free).**  Any linear `τ` with
    `τ(ab) = τ(ba)` vanishes on every generator `a·b − b·a`, hence on their span
    `[A,A]`. -/
theorem commutatorSubmodule_le_ker_of_trace (τ : A →ₗ[R] R)
    (hτ : ∀ a b : A, τ (a * b) = τ (b * a)) :
    commutatorSubmodule R A ≤ LinearMap.ker τ := by
  rw [commutatorSubmodule, Submodule.span_le]
  rintro x ⟨a, b, rfl⟩
  simp [LinearMap.mem_ker, map_sub, hτ a b]

/-- **A trace factors through the cocenter (sorry-free).**  `τ` descends to a
    linear functional on `HH₀(A) = A/[A,A]`: the magnitude functional is a
    function of the cocenter class alone. -/
noncomputable def traceCocenter (τ : A →ₗ[R] R)
    (hτ : ∀ a b : A, τ (a * b) = τ (b * a)) :
    cocenter R A →ₗ[R] R :=
  (commutatorSubmodule R A).liftQ τ (commutatorSubmodule_le_ker_of_trace τ hτ)

@[simp] theorem traceCocenter_mk (τ : A →ₗ[R] R)
    (hτ : ∀ a b : A, τ (a * b) = τ (b * a)) (a : A) :
    traceCocenter τ hτ (Submodule.Quotient.mk a) = τ a :=
  rfl

/-- **The Markov-trace model: `LinearMap.trace` factors through the cocenter of
    `End V` (sorry-free).**  The trace's commutation `trace(fg) = trace(gf)`
    (`trace_mul_comm`) is exactly the hypothesis, so `tr_M` descends to
    `HH₀(End V)` — the `HH₀`-level form of `MagnitudeTraceCommutator`'s
    `trace_comp_conjOp`.  The decision information the trace discards is the
    complementary `[End V, End V]`. -/
noncomputable def traceCocenter_End {V : Type*} [AddCommGroup V] [Module R V]
    [Module.Free R V] [Module.Finite R V] :
    cocenter R (Module.End R V) →ₗ[R] R :=
  traceCocenter (LinearMap.trace R V) (by
    intro f g
    exact LinearMap.trace_mul_comm (R := R) (M := V) f g)

end QOU.Information
