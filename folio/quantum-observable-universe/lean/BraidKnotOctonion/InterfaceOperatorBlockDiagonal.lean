import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.BraidKnot.InterfaceOperator — block-diagonality of the interface operator

The operator-valued Wenzl branching combiner for per-isotope binding peels one
nucleon at a time through the **interface operator** `A^λ_{ξν}(I)`, defined as the
compression of the bridge generator `I = c·σ_{n-4} + d·𝟙` to the `(ξ,ν)`-isotypic
subspace of `V_λ`:

  `A^λ_{ξν}(I) = P_{ξν} · ρ_λ(I) · P_{ξν}`.

The closure-(b) design
(`docs/audits/2026-06-16-categorical-interface-operator-closure-b-design.md`,
§"Why this is the right object") establishes — in prose — the structural reason
this object is **universal by construction** (no test-word dependence):

> Because `W` acts within `ξ`-blocks and `β_block` within `ν`-blocks (no mixing)
> and the trace is cyclic, **only the diagonal `(ξ,ν)→(ξ,ν)` isotypic block of
> `ρ_λ(I)` survives the closed trace**. Off-diagonal blocks would carry
> `ρ_{ξ'}(W) ⊗ ρ_{ν'}(β)` between *different* irreps and vanish under the closed
> trace.

This file makes that the content of a sorry-free theorem. The decomposition

  `χ^λ(W·I·β) = Σ_{ξν} Tr( A^λ_{ξν}(I) · (ρ_ξ(W) ⊗ ρ_ν(β)) )`

reduces — at the algebra/trace level — to the statement that a cyclic trace `τ`
of `W·I·β`, where `W` and `β` each commute with every projector in an orthogonal
resolution of unity `{P i}`, collapses onto the **diagonal** compressions
`P i · I · P i`:

  `τ(W·I·β) = Σ_i τ( W · (P i · I · P i) · β )`.

This is precisely the "no off-diagonal survives the trace" invariant. It is what
turns the categorical extraction of `A^λ_{ξν}(I)` into a deterministic
*compression* rather than a least-squares *fit* (which was rank-deficient at
`n ≥ 9` and produced the 21–42 % error on T / ³He). The downstream H₉
universality extraction (Rust-gated) inherits this guarantee.

## Scope and base ring (§7c)

Stated over a **generic** commutative ring `R` as the trace codomain and a
generic (possibly noncommutative) ring `A` as the operator algebra — no
archimedean structure, no specialisation to `ℝ`, no fitted constant. The
hypotheses are exactly the categorical facts the design doc cites:

* `{P i}` is an **orthogonal resolution of unity** (`P i · P j = 0` for `i ≠ j`,
  `Σ P i = 1`) — the isotypic projectors `P_{ξν}`;
* `W` and `β` each **commute with every** `P i` — `W` lies in the inner
  subalgebra `H_{n-3}` and `β` in the block subalgebra `H_3`, each acting
  block-diagonally on the isotypic decomposition;
* `τ` is **additive and cyclic** — the Markov trace `τ_M`.

Note the identity holds for *any* orthogonal resolution of unity, not only
idempotent projectors — idempotency of the `P i` is not needed and is therefore
not assumed (the isotypic projectors are the intended special case).

## References

- `docs/audits/2026-06-16-categorical-interface-operator-closure-b-design.md`
  (the structural finding + construction algorithm this formalizes).
- `docs/audits/2026-06-23-interface-operator-derivation-and-4body-assembly.md`.
- `computations/a_operator/a_operator_categorical.py` (the verified preflight).
- [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors",
  Invent. Math. 92 (1988) 349-383.
-/

namespace QOU.BraidKnot.InterfaceOperator

open Finset

variable {R : Type*} [CommRing R]
variable {A : Type*} [Ring A]
variable {ι : Type*} [Fintype ι]

/-- The diagonal isotypic block of the interface operator:
    `A_i = P i · I · P i`, the compression of `I = ρ_λ(I)` to the
    `i = (ξ,ν)` isotypic sector. -/
def interfaceBlock (P : ι → A) (I : A) (i : ι) : A := P i * I * P i

/-- **Block-diagonality of the interface operator under a cyclic trace.**

Let `{P i}` be an orthogonal resolution of unity in `A` (`P i · P j = 0` for
`i ≠ j`, and `Σ i, P i = 1`). Let `W, β ∈ A` each commute with every `P i`, and
let `τ : A →+ R` be cyclic (`τ (x*y) = τ (y*x)`). Then the trace of `W · I · β`
collapses onto the diagonal compressions of `I`:

  `τ (W · I · β) = Σ i, τ ( W · (P i · I · P i) · β )`.

This is the "only the diagonal isotypic block survives the closed trace"
invariant from the closure-(b) design — the structural reason the interface
operator `A^λ_{ξν}(I) = P_{ξν} ρ_λ(I) P_{ξν}` is universal by construction. -/
theorem trace_block_diagonal
    (τ : A →+ R)
    (hcyc : ∀ x y : A, τ (x * y) = τ (y * x))
    (P : ι → A)
    (horth : ∀ i j, i ≠ j → P i * P j = 0)
    (hsum : ∑ i, P i = 1)
    (W I β : A)
    (hWP : ∀ i, W * P i = P i * W)
    (hβP : ∀ i, β * P i = P i * β) :
    τ (W * I * β) = ∑ i, τ (W * (P i * I * P i) * β) := by
  -- Off-diagonal blocks vanish under the closed trace.
  have offdiag : ∀ i j, i ≠ j → τ (W * (P i * I * P j) * β) = 0 := by
    intro i j hij
    -- Rotate the word cyclically so the two projectors meet, after commuting
    -- `β` and `W` (which commute with every `P`) out from between them.
    have rot : τ (W * (P i * I * P j) * β) = τ (P j * β * W * P i * I) := by
      rw [show W * (P i * I * P j) * β = (W * P i * I) * (P j * β) from by noncomm_ring,
          hcyc (W * P i * I) (P j * β)]
      congr 1
      noncomm_ring
    have e2 : P j * β * W * P i * I = β * W * (P j * P i) * I := by
      rw [← hβP j, mul_assoc β (P j) W, ← hWP j]
      noncomm_ring
    rw [rot, e2, horth j i hij.symm]
    simp
  -- Expand `I = (Σ P i) · I · (Σ P j)` and distribute (controlled, to fix the
  -- summation order).
  have key : (∑ i, P i) * I * (∑ j, P j) = ∑ i, ∑ j, P i * I * P j := by
    rw [Finset.sum_mul, Finset.sum_mul]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    rw [Finset.mul_sum]
  have expand : W * I * β = ∑ i, ∑ j, W * (P i * I * P j) * β := by
    calc W * I * β
        = W * ((∑ i, P i) * I * (∑ j, P j)) * β := by rw [hsum, one_mul, mul_one]
      _ = W * (∑ i, ∑ j, P i * I * P j) * β := by rw [key]
      _ = ∑ i, ∑ j, W * (P i * I * P j) * β := by
            rw [Finset.mul_sum, Finset.sum_mul]
            refine Finset.sum_congr rfl (fun i _ => ?_)
            rw [Finset.mul_sum, Finset.sum_mul]
  rw [expand, map_sum]
  simp_rw [map_sum]
  refine Finset.sum_congr rfl (fun i _ => ?_)
  rw [Finset.sum_eq_single i
        (fun j _ hji => offdiag i j hji.symm)
        (fun hi => absurd (mem_univ i) hi)]

/-- Restatement of `trace_block_diagonal` in terms of the named
    `interfaceBlock` compressions `A_i = P i · I · P i`. -/
theorem trace_eq_sum_interfaceBlock
    (τ : A →+ R)
    (hcyc : ∀ x y : A, τ (x * y) = τ (y * x))
    (P : ι → A)
    (horth : ∀ i j, i ≠ j → P i * P j = 0)
    (hsum : ∑ i, P i = 1)
    (W I β : A)
    (hWP : ∀ i, W * P i = P i * W)
    (hβP : ∀ i, β * P i = P i * β) :
    τ (W * I * β) = ∑ i, τ (W * interfaceBlock P I i * β) := by
  simp only [interfaceBlock]
  exact trace_block_diagonal τ hcyc P horth hsum W I β hWP hβP

/-- Additivity and zero-preservation of the diagonal isotypic compression
`interfaceBlock P I i = P i * I * P i` in the bridge operator argument `I`. -/
theorem interfaceBlock_zero_and_add (P : ι → A) (I J : A) (i : ι) :
    interfaceBlock P 0 i = 0 ∧
      interfaceBlock P (I + J) i = interfaceBlock P I i + interfaceBlock P J i := by
  unfold interfaceBlock
  constructor
  · simp
  · noncomm_ring

end QOU.BraidKnot.InterfaceOperator
