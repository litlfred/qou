import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Algebra.Algebra.Equiv
import Mathlib.Algebra.Algebra.Pi
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.SchurWeyl — quantum Schur–Weyl / Wedderburn form of the Markov trace (R2)

Quantum Schur–Weyl duality (Jimbo 1986): for `U_q(gl_N)` acting on
`V^{⊗n}` (`V = K^N`), the centralizer `End_{U_q}(V^{⊗n})` is the image of
the Iwahori–Hecke algebra `H_n(q)`, and

  `V^{⊗n} ≅ ⊕_{λ ⊢ n, ℓ(λ) ≤ N} L_λ ⊗ S^λ`,

so `H_n(q) ≅ ⊕_λ M_{d_λ}(K)` (Wedderburn; the matrix units are Hoefsmit's
seminormal form, `d_λ = #SYT(λ)`).  Under this decomposition the Markov
trace becomes the weighted character sum `tr_M = ∑_λ w_λ χ_λ` — which is
exactly the QOU Frobenius pairing and the partition-function reading of
the trace (R1, `QOU.Thermo`).

## Scope of this file (honest, per formalize-first + strict Lean discipline)

Full quantum Schur–Weyl for `H_n(q)` is not in Mathlib (Mathlib has **no**
Schur–Weyl duality at all), and constructing the `U_q(gl_N)`-module
`V^{⊗n}` with its Hoefsmit decomposition is a multi-week formalization.
This file therefore:

* **axiomatizes the Jimbo/Hoefsmit content as a content-bearing structure**
  `HeckeWedderburnData` — the Wedderburn algebra-isomorphism `iso` and the
  Markov-trace-as-weighted-character-sum identity `markov_eq` are its
  **hypotheses** (fields), not assumed conclusions of a fake theorem; and
* **proves the R2 consequences sorry-free and conditionally** on that data
  (`markov_one_eq`, `markov_add`, `markov_smul`), so they are rigorous
  results modulo the single, named, cited construction.

The **open** piece is honestly the *absence of an instance*: constructing a
`HeckeWedderburnData` for the actual `H_n(q)` (the Jimbo-1986 double
centralizer + Hoefsmit matrix units) is tracked as bean `R2-inst` under
`qou-mpq5`.  There is **no `sorry` and no trivial-`True`** here; the open
state is represented, per §3b-tax, by a content-bearing structure with no
instance yet built.

Base ring: a generic field `K` (§7c — algebraic, no archimedean input).

LaTeX label: `prop:hecke-wedderburn-markov`
References: Jimbo (1986) `[jimbo1986]`, Hoefsmit (1974) `[hoefsmit1974]`,
Wenzl (1988) `[wenzl1988]`.
-/

namespace QOU.SchurWeyl

open scoped BigOperators

/-- **Quantum Schur–Weyl / Wedderburn data for a Hecke algebra with a
Markov trace.**  The fields `iso` and `markov_eq` encode the Jimbo (1986)
double-centralizer theorem together with Hoefsmit's (1974) explicit
partition-indexed matrix units: `H ≅ ⊕_λ M_{d_λ}(K)` and the Markov trace
is the weighted character sum `∑_λ w_λ χ_λ`.  A term of this structure is
the *hypothesis* "quantum Schur–Weyl holds for `H`"; the R2 results below
are proved from it. -/
structure HeckeWedderburnData
    (K : Type*) [Field K]
    (Part : Type*) [Fintype Part]
    (H : Type*) [Ring H] [Algebra K H] where
  /-- `d_λ = #SYT(λ)`, the dimension of the Specht module `S^λ`. -/
  dim : Part → ℕ
  /-- `w_λ`, the Markov weight of block `λ`. -/
  weight : Part → K
  /-- The Wedderburn isomorphism `H ≅ ⊕_λ M_{d_λ}(K)` (Hoefsmit matrix units). -/
  iso : H ≃ₐ[K] (Π l : Part, Matrix (Fin (dim l)) (Fin (dim l)) K)
  /-- The Markov trace functional on `H`. -/
  markov : H → K
  /-- The Markov trace is the weighted character sum `tr_M = ∑_λ w_λ χ_λ`. -/
  markov_eq : ∀ h, markov h = ∑ l, weight l * ((iso h) l).trace

variable {K : Type*} [Field K] {Part : Type*} [Fintype Part]
  {H : Type*} [Ring H] [Algebra K H]

/-- **Partition function at the identity = `∑_λ d_λ w_λ`.**  The Markov
trace of `1` is the degeneracy-weighted sum over Wedderburn blocks — the
"total number of states" of the partition function counted by block, with
`d_λ` the block dimension.  Proved from the Wedderburn data. -/
theorem markov_one_eq (D : HeckeWedderburnData K Part H) :
    D.markov 1 = ∑ l : Part, D.weight l * (D.dim l : K) := by
  rw [D.markov_eq]
  refine Finset.sum_congr rfl fun l _ => ?_
  rw [map_one, Pi.one_apply, Matrix.trace_one, Fintype.card_fin]

/-- The Markov trace is additive — it is a genuine trace functional, not an
arbitrary map (consequence of `markov_eq` + linearity of matrix trace). -/
theorem markov_add (D : HeckeWedderburnData K Part H) (a b : H) :
    D.markov (a + b) = D.markov a + D.markov b := by
  simp only [D.markov_eq, map_add, Pi.add_apply, Matrix.trace_add, mul_add]
  rw [Finset.sum_add_distrib]

/-- The Markov trace is `K`-homogeneous. -/
theorem markov_smul (D : HeckeWedderburnData K Part H) (c : K) (a : H) :
    D.markov (c • a) = c * D.markov a := by
  simp only [D.markov_eq, map_smul, Pi.smul_apply, Matrix.trace_smul,
    smul_eq_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl fun l _ => ?_
  ring

end QOU.SchurWeyl
