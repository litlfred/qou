import Mathlib.LinearAlgebra.Trace

/-!
# QOU.Information.MagnitudeTraceCommutator — `M ∘ Q = M` as an operator lemma

The magnitude functional of the QOU is the **Markov trace** `tr_M` (a trace /
Frobenius pairing / class function).  A trace has a hard algebraic property that
makes the counting/decision wall *native to the categorical machinery*: **it
annihilates commutators.**

With `M = tr_M` and the quantifier step `Q` realized as **conjugation** in the
Hecke/braid algebra (`Q_u : x ↦ u x u⁻¹`, the natural "relabel the computation"
move), the commutator defect `[Q, M] = QM − MQ` is a commutator, so

    M([a, b]) = tr_M(ab) − tr_M(ba) = 0,   hence   M ∘ Q = M.

That is **exactly why the Jones polynomial `J_K = tr_M(ρ β)` is a knot
invariant**: invariance under Markov move I (conjugation `β ↦ α β α⁻¹`) *is*
trace-kills-commutators.  The magnitude is well-defined precisely because it is
**blind to the conjugation `Q`-step** — the counting/decision wall, native to
QOU.

This file formalizes it **at the operator level** (§7c: generic free finite
module, base ring `{R : Type*} [CommRing R]`, no archimedean structure):

* `magnitude_trace_commutator_zero` — `M([f,g]) = 0` (trace kills commutators);
* `conjOp u` — the `Q`-step as an honest R-linear **operator** on `End V`;
* `trace_comp_conjOp` — the operator identity **`M ∘ Q = M`**;
* `trace_comp_conjOp_sub_id` — **`M ∘ (Q − 1) = 0`**, the operator form of
  `tr_M([Q, M]) = 0`.

Where the decision content lives: at the fibre level `[Q, M] ≠ 0` as an algebra
element (it sits in the commutator subspace `[H, H]`); only its **trace**
vanishes.  Crossing the wall needs a functional nonzero on `[H, H]` — a
**non-trace / non-class-function** separating invariant (the `χ(A)` residue),
which is the algebrization barrier in QOU terms.  This is the operator statement
of `MagnitudeAxisBoundary.census_blind_to_decision`.
-/

namespace QOU.Information

open LinearMap

variable {R : Type*} [CommRing R] {V : Type*} [AddCommGroup V] [Module R V]
  [Module.Free R V] [Module.Finite R V]

omit [Module.Free R V] [Module.Finite R V] in
/-- **`M` kills the commutator `[Q, M]` (sorry-free): `tr([f, g]) = 0`.**  The
    magnitude functional (a trace) is blind to the commutator defect — `QM` and
    `MQ` carry equal magnitude.  Toda-blindness realized by the categorical
    trace. -/
theorem magnitude_trace_commutator_zero (f g : V →ₗ[R] V) :
    trace R V (f * g - g * f) = 0 := by
  rw [map_sub, trace_mul_comm, sub_self]

omit [Module.Free R V] [Module.Finite R V] in
/-- **Magnitude is conjugation-invariant (sorry-free): `tr(u f u⁻¹) = tr f`.**
    The scalar form of `M ∘ Q = M` — Markov move I for the Jones invariant. -/
theorem magnitude_trace_conj (u : (V →ₗ[R] V)ˣ) (f : V →ₗ[R] V) :
    trace R V ((↑u : V →ₗ[R] V) * f * ↑u⁻¹) = trace R V f := by
  rw [trace_mul_comm, ← mul_assoc, Units.inv_mul, one_mul]

/-- The **quantifier `Q`-step as an operator**: conjugation by a unit `u`, an
    R-linear map on `End V` (relabel the computation). -/
def conjOp (u : (V →ₗ[R] V)ˣ) : (V →ₗ[R] V) →ₗ[R] (V →ₗ[R] V) where
  toFun x := (↑u : V →ₗ[R] V) * x * ↑u⁻¹
  map_add' x y := by simp only [mul_add, add_mul]
  map_smul' c x := by simp only [RingHom.id_apply, mul_smul_comm, smul_mul_assoc]

omit [Module.Free R V] [Module.Finite R V] in
@[simp] theorem conjOp_apply (u : (V →ₗ[R] V)ˣ) (x : V →ₗ[R] V) :
    conjOp u x = (↑u : V →ₗ[R] V) * x * ↑u⁻¹ := by
  have h1 : (↑u : V →ₗ[R] V) * x * ↑u⁻¹ + 0 = (↑u : V →ₗ[R] V) * x * ↑u⁻¹ :=
    add_zero _
  change (↑u : V →ₗ[R] V) * x * ↑u⁻¹ = _
  exact h1.symm.trans (add_zero _)

omit [Module.Free R V] [Module.Finite R V] in
/-- **The operator lemma `M ∘ Q = M` (sorry-free).**  As linear maps
    `End V → R`, the magnitude `M = trace` composed with the conjugation
    `Q`-step `conjOp u` equals `M`: the quantifier step is invisible to the
    magnitude functional. -/
theorem trace_comp_conjOp (u : (V →ₗ[R] V)ˣ) :
    (trace R V).comp (conjOp u) = trace R V := by
  ext x
  simp only [LinearMap.comp_apply, conjOp_apply]
  exact magnitude_trace_conj u x

omit [Module.Free R V] [Module.Finite R V] in
/-- **The operator lemma `M ∘ (Q − 1) = 0` (sorry-free).**  The commutator
    defect `[Q, M]` is annihilated by `M`: `trace ∘ (conjOp u − id) = 0` as
    linear maps `End V → R` — the operator form of `tr_M([Q, M]) = 0`, and the
    reason no trace-based (class-function) functional, including the surreal
    birthday of `tr_M`, separates conjugate operators.  Crossing the wall
    requires a functional nonzero on the commutator subspace `[H, H]`. -/
theorem trace_comp_conjOp_sub_id (u : (V →ₗ[R] V)ˣ) :
    (trace R V).comp (conjOp u - LinearMap.id) = 0 := by
  ext x
  simp only [LinearMap.comp_apply, LinearMap.sub_apply, LinearMap.id_coe, id_eq,
    conjOp_apply, map_sub, LinearMap.zero_apply]
  rw [magnitude_trace_conj, sub_self]

omit [Module.Free R V] [Module.Finite R V] in
/-- Conjugation by the identity unit is the identity operator on `End V`. -/
theorem conjOp_one : conjOp (1 : (V →ₗ[R] V)ˣ) = LinearMap.id := by
  ext x
  have h : conjOp (1 : (V →ₗ[R] V)ˣ) x = (1 : V →ₗ[R] V) * x * 1 := conjOp_apply 1 x
  rw [h, one_mul, mul_one]
  rfl

omit [Module.Free R V] [Module.Finite R V] in
/-- Conjugation operators compose multiplicatively: `conjOp (u * v) = conjOp u ∘ conjOp v`. -/
theorem conjOp_mul (u v : (V →ₗ[R] V)ˣ) :
    conjOp (u * v) = (conjOp u).comp (conjOp v) := by
  ext x
  simp only [LinearMap.comp_apply, conjOp_apply, Units.val_mul, mul_inv_rev]
  simp only [mul_assoc]

/-- **Observed halting predicate (`qou-hrom`).** An operator `f : V →ₗ[R] V`
    halts-observed at target trace `target : R` when `trace R V f = target`. -/
def haltsObserved (target : R) (f : V →ₗ[R] V) : Prop :=
  trace R V f = target

omit [Module.Free R V] [Module.Finite R V] in
/-- **Observed halting is invariant under the conjugation `Q`-step (`qou-hrom`).**
    Because `trace ∘ conjOp u = trace`, `conjOp u f` halts-observed at `target`
    if and only if `f` does. -/
theorem haltsObserved_conjOp_iff (target : R) (u : (V →ₗ[R] V)ˣ) (f : V →ₗ[R] V) :
    haltsObserved target (conjOp u f) ↔ haltsObserved target f := by
  have htr : trace R V (conjOp u f) = trace R V f :=
    LinearMap.congr_fun (trace_comp_conjOp u) f
  constructor
  · intro h
    exact htr.symm.trans h
  · intro h
    exact htr.trans h

omit [Module.Free R V] [Module.Finite R V] in
/-- **Lossy shadow / converse-failure for observed halting (`qou-hrom`).**
    Whenever a unit `u` moves `f` (`conjOp u f ≠ f`), the two distinct operators
    `conjOp u f` and `f` have identical observed-halting status at every target
    value, demonstrating that `haltsObserved` cannot separate conjugate states. -/
theorem haltsObserved_converse_failure_of_conjOp_ne (target : R)
    (u : (V →ₗ[R] V)ˣ) (f : V →ₗ[R] V) (hne : conjOp u f ≠ f)
    (hobs : haltsObserved target f) :
    haltsObserved target (conjOp u f) ∧ conjOp u f ≠ f := by
  have hiff := (haltsObserved_conjOp_iff target u f).mpr hobs
  refine ⟨?_, ?_⟩
  · exact hiff
  · exact hne

end QOU.Information
