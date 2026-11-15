import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.Quotient.Basic
import QOU.Machinery.BilinearTraceCyclicity

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

**Shared trace abstraction (unification with `Machinery.BilinearTraceCyclicity`).**
The cyclicity hypothesis is the single predicate
`QOU.Machinery.BilinearTrace.IsCyclic τ := ∀ x y, τ (x·y) = τ (y·x)` — the same
"a functional is a trace" abstraction the Gram-symmetry / character-decomposition
machinery uses. That file supplies the *constructors* of cyclic functionals — a
matrix character `χ_λ = trace ∘ ρ_λ` is cyclic (`isCyclic_trace_comp`), and a
finite weighted sum `tr_M = ∑_λ w_λ · χ_λ` of cyclic functionals is cyclic
(`isCyclic_weighted_sum`), which is exactly the shape of the QOU Markov trace.
This file supplies the *consequence*: **every** such cyclic functional factors
through the cocenter `HH₀`. So the two independently-developed frameworks meet
here — the character side *builds* the Markov trace, the cocenter side *localizes*
what it discards (the decision axis `[A,A]`).

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

open QOU.Machinery.BilinearTrace (IsCyclic)

variable (R : Type*) [CommRing R] (A : Type*) [Ring A] [Algebra R A]

/-- The **commutator submodule** `[A,A]` — the `R`-span of all `a·b − b·a`. -/
def commutatorSubmodule : Submodule R A :=
  Submodule.span R {x | ∃ a b : A, x = a * b - b * a}

/-- The **cocenter** `HH₀(A) = A / [A,A]` — the target of every trace functional. -/
abbrev cocenter : Type _ := A ⧸ commutatorSubmodule R A

variable {R A}

/-- **A trace functional kills `[A,A]` (sorry-free).**  Any linear `τ` that is
    `IsCyclic` (`τ(ab) = τ(ba)`) vanishes on every generator `a·b − b·a`, hence on
    their span `[A,A]`. The hypothesis is the shared
    `Machinery.BilinearTrace.IsCyclic` predicate. -/
theorem commutatorSubmodule_le_ker_of_trace (τ : A →ₗ[R] R)
    (hτ : IsCyclic (⇑τ)) :
    commutatorSubmodule R A ≤ LinearMap.ker τ := by
  rw [commutatorSubmodule, Submodule.span_le]
  rintro x ⟨a, b, rfl⟩
  simp [LinearMap.mem_ker, map_sub, hτ a b]

/-- **A trace factors through the cocenter (sorry-free).**  A cyclic `τ` descends
    to a linear functional on `HH₀(A) = A/[A,A]`: the magnitude functional is a
    function of the cocenter class alone. -/
noncomputable def traceCocenter (τ : A →ₗ[R] R)
    (hτ : IsCyclic (⇑τ)) :
    cocenter R A →ₗ[R] R :=
  (commutatorSubmodule R A).liftQ τ (commutatorSubmodule_le_ker_of_trace τ hτ)

@[simp] theorem traceCocenter_mk (τ : A →ₗ[R] R)
    (hτ : IsCyclic (⇑τ)) (a : A) :
    traceCocenter τ hτ (Submodule.Quotient.mk a) = τ a :=
  rfl

/-! ### The wrong-axis corollary: a trace cannot separate the `[A,A]` axis

An **Euler characteristic** (`χ(Σ₄) = −6` for the QOU's Bring fibre) is an
*additive-on-triangles / `K₀`* invariant — the Hattori–Stallings/dimension
**trace**. So it factors through `HH₀` and inherits the blindness below: it
cannot distinguish elements differing by a commutator, i.e. it is **blind to the
`[A,A]` (decision/quantifier) axis**. Therefore a nonzero `χ` — however
axiom-fixed — is *never* the P-vs-NP decision residue: that residue must live in
`[A,A]` = `ker(every trace)`, i.e. be a **non-trace** (`HH₁`) object. -/

/-- **A trace is blind to `[A,A]`-differences (sorry-free).**  If `a − b ∈ [A,A]`
    then `τ a = τ b`: no trace (hence no `K₀`/Euler-characteristic invariant)
    distinguishes elements that differ by a sum of commutators. -/
theorem trace_eq_of_sub_mem_commutator (τ : A →ₗ[R] R)
    (hτ : IsCyclic (⇑τ)) {a b : A}
    (h : a - b ∈ commutatorSubmodule R A) : τ a = τ b := by
  have hk : a - b ∈ LinearMap.ker τ := commutatorSubmodule_le_ker_of_trace τ hτ h
  rw [LinearMap.mem_ker, map_sub, sub_eq_zero] at hk
  exact hk

/-- **Adding a commutator does not move a trace (sorry-free).**  `τ(x + (ab − ba))
    = τ x` — the infinitesimal form of trace-blindness on the `[A,A]` axis. -/
theorem trace_add_commutator (τ : A →ₗ[R] R)
    (hτ : IsCyclic (⇑τ)) (x a b : A) :
    τ (x + (a * b - b * a)) = τ x := by
  rw [map_add, map_sub, hτ a b, sub_self, add_zero]

/-- **Any functional separating a commutator-difference is a NON-trace
    (sorry-free).**  The contrapositive of `trace_eq_of_sub_mem_commutator`: if
    `φ` distinguishes `a, b` with `a − b ∈ [A,A]`, then `φ` is *not* cyclic — the
    conclusion `∃ x y, φ(xy) ≠ φ(yx)` is exactly `¬ IsCyclic ⇑φ`.

    This is the precise, **proved** form of the P-vs-NP wall's necessary
    condition: a **decision residue** must separate the `[A,A]` (decision) axis,
    so it is necessarily a **non-trace** — a class in `HH₁`, not `HH₀`, and in
    particular *not* any Euler-characteristic / `K₀` invariant (`χ = −6`). The
    residue's remaining requirement — that such a non-trace `φ` be
    **non-algebraic** (efficiently uncomputable) — is the algebrization barrier
    (Aaronson–Wigderson), which lives outside this algebraic statement and keeps
    `res ≠ 0` open. -/
theorem not_trace_of_separates_commutator (φ : A →ₗ[R] R) {a b : A}
    (hab : a - b ∈ commutatorSubmodule R A) (hsep : φ a ≠ φ b) :
    ¬ IsCyclic (⇑φ) := by
  intro h
  exact hsep (trace_eq_of_sub_mem_commutator φ h hab)

/-- **The Markov-trace model: `LinearMap.trace` factors through the cocenter of
    `End V` (sorry-free).**  The trace's commutation `trace(fg) = trace(gf)`
    (`trace_mul_comm`) is exactly `IsCyclic`, so `tr_M` descends to
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
