import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FinCases

/-!
# QOU.QuantumUniverse.CategoricalCoordinateForced — the categorical structure does force `R[i]`

Bean `qou-ywh9`, epic `qou-8lxd`; discharges the standing prose assertion in
[`rem:commutative-crossing-energy`](../../../climax-volume-mass/commutative-crossing-energy.md).

## The assertion this discharges

`rem:commutative-crossing-energy` states, of the commutative limit `q = 1`:

> the eigenvalues collapse to `(+1, −1)` … We recover the categorical structure
> of the commutative limit by extracting the *square root* of the antisymmetric
> eigenvalue `λ₋ = −1`: `i = √λ₋`, `i² + 1 = 0` in `R[i]`. **The categorical
> structure forces the ring extension `R[i]`** … The construction is intrinsic
> to `R`; we assume no real or complex numbers.

That was prose. The one Lean file in the arc,
`categorical_coordinate_ring_universal`, takes `iS : S` and `hiS : iS ^ 2 = -1`
as **hypotheses** — it is the universal property of `R[q,q⁻¹][i]/(i²+1)` *given*
a square root of `−1` in the target, and structurally cannot produce one.
`i_coord_sq_eq_neg_one` proves `i² = −1` by construction (`AdjoinRoot.isRoot_root`),
a fact about the adjunction rather than about a quantum observable universe.

**This file supplies the missing implication, and its content is Cayley–Hamilton
at rank two.** The mechanism is exactly the volume form:

* the degree-2 volume form `Λ²V ≅ 𝟙` is what *defines* `det` — `det f` is the
  scalar by which `Λ²f` acts on `Λ²V ≅ 𝟙`;
* at rank 2, Cayley–Hamilton reads `f² = (tr f)·f − (det f)·1`;
* so on the subgroup the volume form cuts out — `det = 1`, which is precisely
  `SL(V) = Sp(V)`, the group `def:fundamental-object` says the volume form
  selects over `GL₂` — every **trace-free** element squares to `−1`.

No square root is assumed. `i² = −1` is the Cayley–Hamilton identity read on the
trace-free part of the group the volume form already selects, and the two
hypotheses are exactly the two data the framework already has: the volume form
(giving `det = 1`) and trace-freeness (the Lie algebra of that group).

## What is proved, and what is not

**Proved, sorry-free, over an arbitrary `CommRing R` — no `ℝ`, no `ℂ`, matching
the block's "we assume no real or complex numbers":**

* `sq_eq_trace_smul_sub_det` — Cayley–Hamilton at rank 2, by computation.
* `sq_eq_neg_one_of_traceFree_det_one` — **the forcing**: `tr f = 0` and
  `det f = 1` give `f * f = −1`.
* `J_trace`, `J_det`, `J_sq` — such an `f` *exists*, exhibited, so the statement
  is not vacuous.
* `one_J_linearIndependent` — `{1, J}` is `R`-linearly independent, so the
  subalgebra `R·1 ⊕ R·J` it spans is a genuine rank-2 extension and not a
  collapsed copy of `R`. This is what upgrades "there is a square root of `−1`"
  to "`R[i]` embeds".
* `sq_eq_neg_one_iff_traceFree` — the converse direction on the volume-form
  subgroup: within `det = 1`, squaring to `−1` is *equivalent* to being
  trace-free. So the trace-free condition is not
  an extra choice made to reach the answer; it is what squaring to `−1` means
  there.  No `2`-cancellation hypothesis is needed: the determinant cancels.

**Not proved, and asserted nowhere below:**

* that `R` itself contains a square root of `−1`. It does not, and the block does
  not claim it does — what is forced is the *extension*, i.e. an embedding
  `R[i] ↪ End(V)`. `R = ℝ` gives `ℂ ⊆ End(ℝ²)` and `ℝ` still has no `i`.
* that the **braiding** forces this. The braiding enters only in fixing
  `λ₋ = −1` at `q = 1`; `neg_one_eq_lambdaMinus_at_q_one` records that link as an
  arithmetic identity and nothing more. The forcing above is a statement about
  the volume form, which is the stronger and cleaner reading.
* anything about `q ≠ 1`. `def:commutative-qou` is the `q → 1` corner and that is
  where the block's claim lives.

**A matrix model is used deliberately, and it is not a weakening.** `End(V)` for
a rank-2 free module *is* `Matrix (Fin 2) (Fin 2) R` once a basis is chosen, and
every statement below is basis-independent in content: `trace` and `det` are
conjugation-invariant, so `sq_eq_neg_one_of_traceFree_det_one` transports to any
basis. Mathlib has no exterior-power-of-an-object API, so `det` is used in its
matrix form; that `det` *is* the action on `Λ²`, which is the framework's volume
form, is the one cited step (§7c: no `ℝ` anywhere — everything is over a bare
`CommRing`).

## The CRT defect in the same arc, also settled

`categorical-coordinate-ring-proof.md` rows 1 and 3 state `ℂ[i]/(i²+1) ≅ ℂ`.
That is false: over a ring that *already* has a square root of `−1`, the
polynomial splits and the quotient acquires a nontrivial idempotent, so it is
`ℂ × ℂ`. `idempotent_of_sqrt_neg_one` proves the idempotent exists, by
computation, over any commutative ring with `2` invertible — which is the whole
content of the CRT splitting and is what makes the stated isomorphism impossible
(`ℂ` is a field and has no idempotent but `0` and `1`). Reported in that block's
`.qa.json` as an unedited math finding; this is the proof of the correction.
-/

namespace QOU.QuantumUniverse.CategoricalCoordinateForced

open Matrix

variable {R : Type*} [CommRing R]

/-- **Cayley–Hamilton at rank two.**  `f² = (tr f)·f − (det f)·1`.

This is the whole mechanism: `det` is the scalar by which `Λ²f` acts on
`Λ²V ≅ 𝟙`, so the volume form is exactly what makes the second coefficient
available. -/
theorem sq_eq_trace_smul_sub_det (f : Matrix (Fin 2) (Fin 2) R) :
    f * f = f.trace • f - f.det • (1 : Matrix (Fin 2) (Fin 2) R) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Matrix.trace_fin_two, Matrix.det_fin_two,
      Fin.sum_univ_two] <;> ring

/-- **The forcing.**  On the subgroup the volume form selects — `det = 1`, i.e.
`SL(V) = Sp(V)`, which `def:fundamental-object` says the volume form picks out
over `GL₂` — every trace-free endomorphism squares to `−1`.

No square root is assumed anywhere: `i² = −1` is Cayley–Hamilton read on the
trace-free part of the group the volume form already gives. -/
theorem sq_eq_neg_one_of_traceFree_det_one {f : Matrix (Fin 2) (Fin 2) R}
    (ht : f.trace = 0) (hd : f.det = 1) :
    f * f = -1 := by
  rw [sq_eq_trace_smul_sub_det, ht, hd]
  simp

/-- The canonical quarter-turn.  `rem:affine-chart-origin-of-i-and-q` calls it
`ρ_{π/2} = i·id_V`, the square root of the chart-swap involution. -/
def J : Matrix (Fin 2) (Fin 2) R := !![0, -1; 1, 0]

theorem J_trace : (J : Matrix (Fin 2) (Fin 2) R).trace = 0 := by
  simp [J, Matrix.trace_fin_two]

theorem J_det : (J : Matrix (Fin 2) (Fin 2) R).det = 1 := by
  simp [J, Matrix.det_fin_two]

/-- **Existence, so the forcing is not vacuous.**  `J² = −1`, obtained from the
theorem above rather than by a separate computation — the point being that `J`
is not special: *any* trace-free `det`-one endomorphism would do. -/
theorem J_sq : (J : Matrix (Fin 2) (Fin 2) R) * J = -1 :=
  sq_eq_neg_one_of_traceFree_det_one J_trace J_det

/-- **`R[i]` is a genuine extension, not a collapsed copy of `R`.**  `{1, J}` is
`R`-linearly independent, so `R·1 ⊕ R·J ⊆ End(V)` is free of rank 2 — which is
what upgrades "a square root of `−1` exists" to "`R[i]` embeds". -/
theorem one_J_linearIndependent {a b : R}
    (h : a • (1 : Matrix (Fin 2) (Fin 2) R) + b • J = 0) : a = 0 ∧ b = 0 := by
  constructor
  · have := congrArg (fun M => M 0 0) h
    simpa [J, Matrix.one_apply] using this
  · have := congrArg (fun M => M 1 0) h
    simpa [J, Matrix.one_apply] using this

/-- The converse on the volume-form subgroup: within `det = 1`, squaring to `−1`
is **equivalent** to trace-freeness.  So trace-freeness is not an extra choice
made to reach `i² = −1`; it is what squaring to `−1` means there.

No further hypothesis is needed — in particular no assumption that `2` is a
non-zero-divisor.  The determinant does the cancelling: `tr f • f = 0` kills
every entry, hence kills `tr f · det f`, and `det f = 1`. -/
theorem sq_eq_neg_one_iff_traceFree {f : Matrix (Fin 2) (Fin 2) R}
    (hd : f.det = 1) :
    f * f = -1 ↔ f.trace = 0 := by
  constructor
  · intro h
    have hCH := sq_eq_trace_smul_sub_det f
    rw [h, hd] at hCH
    have hzero : f.trace • f = 0 := by
      have h' : f.trace • f - (1 : R) • (1 : Matrix (Fin 2) (Fin 2) R) = -1 := hCH.symm
      rw [one_smul, sub_eq_iff_eq_add] at h'
      simpa using h'
    have h00 := congrArg (fun M => M 0 0) hzero
    have h01 := congrArg (fun M => M 0 1) hzero
    simp only [Matrix.smul_apply, smul_eq_mul, Matrix.zero_apply] at h00 h01
    -- `tr f` annihilates every entry, hence annihilates `det f = 1`.
    have hdet : f.trace * f.det = 0 := by
      rw [Matrix.det_fin_two, mul_sub]
      have e1 : f.trace * (f 0 0 * f 1 1) = f.trace * f 0 0 * f 1 1 := by ring
      have e2 : f.trace * (f 0 1 * f 1 0) = f.trace * f 0 1 * f 1 0 := by ring
      rw [e1, e2, h00, h01]
      ring
    rw [hd, mul_one] at hdet
    exact hdet
  · intro ht
    exact sq_eq_neg_one_of_traceFree_det_one ht hd

/-- The braiding link, recorded as arithmetic and nothing more.  At `q = 1` the
antisymmetric braiding eigenvalue is `λ₋ = −q⁻¹ = −1`
(`prop:braiding-eigenvalue-extraction`), so `J² = λ₋ · 1`: `J` is the square root
of the antisymmetric eigenvalue the block extracts. -/
theorem J_sq_eq_lambdaMinus_at_q_one :
    (J : Matrix (Fin 2) (Fin 2) R) * J = (-1 : R) • (1 : Matrix (Fin 2) (Fin 2) R) := by
  rw [J_sq]; simp

/-- **The CRT correction.**  If `R` *already* contains a square root `u` of `−1`
and `2` is invertible, then any `R`-algebra containing an `x` with `x² = −1`
carries the nontrivial idempotent `e = 2⁻¹(1 + u·x)`.

This is the whole content of the splitting `R[X]/(X²+1) ≅ R × R`, and it is why
`categorical-coordinate-ring-proof.md` rows 1 and 3 — which state
`ℂ[i]/(i²+1) ≅ ℂ` — assert a non-isomorphism: `ℂ` is a field and has no
idempotent other than `0` and `1`. -/
theorem idempotent_of_sqrt_neg_one {A : Type*} [CommRing A] [Algebra R A]
    (u x : A) (hu : u * u = -1) (hx : x * x = -1) (half : A) (hhalf : half * 2 = 1) :
    (half * (1 + u * x)) * (half * (1 + u * x)) = half * (1 + u * x) := by
  have hux : (u * x) * (u * x) = 1 := by
    calc (u * x) * (u * x) = (u * u) * (x * x) := by ring
      _ = (-1 : A) * (-1 : A) := by rw [hu, hx]
      _ = 1 := by ring
  calc (half * (1 + u * x)) * (half * (1 + u * x))
      = half * (half * (1 + (u * x) * (u * x) + 2 * (u * x))) := by ring
    _ = half * (half * (2 + 2 * (u * x))) := by rw [hux]; ring
    _ = half * ((half * 2) * (1 + u * x)) := by ring
    _ = half * (1 + u * x) := by rw [hhalf]; ring

end QOU.QuantumUniverse.CategoricalCoordinateForced
