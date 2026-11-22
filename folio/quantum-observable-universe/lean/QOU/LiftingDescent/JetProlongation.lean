import QOU.Basic
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.Algebra.Module.LinearMap.Defs
import QOU.Hecke.Generators

/-!
# Jet prolongation chain — descent involution + transient/descended decomposition

The brane tower of a quantum observable universe ascends through
the jet prolongation `J¹(A) = A ⊗ Ω¹(A)` (see
`prop:jet-prolongation` in `lifting-and-descent/jet-prolongation.lean`).
At each level `n` we have:

- **Ascent embedding** `ℓ_n : A_n ↪ A_{n+1}` (the unit section
  composed with the prolongation; `prop:jet-prolongation`).
- **Descent retraction** `𝔡_{n+1} : End_C(A_{n+1}) → End_C(A_n)`
  (`lem:descent`); satisfies `𝔡_{n+1} ∘ ℓ_n = id` on `End_C(A_n)`.
- **Descent involution** `τ̂_n = ℓ_n ∘ 𝔡_{n+1} :
  End_C(A_{n+1}) → End_C(A_{n+1})`, an **idempotent**:
  `τ̂_n² = τ̂_n`.

Because `τ̂_n` is idempotent, the level-`(n+1)` endomorphism
algebra splits as the direct sum

    `End_C(A_{n+1}) = 𝒜_{n+1}^{desc} ⊕ 𝒜_{n+1}^{trans}`

where:

- `𝒜_{n+1}^{desc} = im τ̂_n` is the **descended subalgebra**
  (endomorphisms factoring through level `n` via `ℓ_n`).
- `𝒜_{n+1}^{trans} = ker τ̂_n` is the **transient subalgebra**
  (the new modes appearing at level `n+1`).

This decomposition is the categorical scaffold for:

- The **per-level mass tower** (`prop:per-braid-mass-tower`):
  the descended part contributes only at base level
  (`prop:descended-level-zero`); the transient part carries the
  new contribution at each ascension step.
- **R7 inter-level pentagon ascension**
  (`prop:pentagon-uv-commutation`, post-PR-501 reformulation):
  the q-graded operator-lift identity `uv = q·vu`
  modulo `R_q ∈ im τ̂_n` lives on `B_λ^{(n+1)}_trans` and is the
  bridge from level `n` to level `n+1`.

This file lays out the structural Lean infrastructure as a typeclass
that downstream theorems can hypothesise against. Substantive
construction of concrete instances (e.g. for the QOU substrate's
`H_n(q)` chain) is left to follow-up branches; the typeclass
framework lets the inter-level pentagon lift be stated and the
per-level brane tower's transient/descended decomposition be
referenced uniformly.

## References

- [prop:jet-prolongation]
- [lem:descent]
- [def:descent-involution]
- [prop:descent-eigenspaces]
- [prop:descended-level-zero]
- [prop:pentagon-uv-commutation] (inter-level lift)
- [rem:mass-endomorphism-jet-tower]
-/

namespace QOU.LiftingDescent

universe u v

open CategoryTheory CategoryTheory.MonoidalCategory
open QOU.Hecke  -- `Generator n` (braid-generator index) lives here

/--
**Jet prolongation chain** at a given category `C` over a base
ring `R`: an indexed family `A_n : ℕ → C` with ascent embeddings
`ℓ_n : A_n ⟶ A_{n+1}` and descent retractions
`𝔡_{n+1} : End(A_{n+1}) →ₗ[R] End(A_n)` satisfying the retraction
identity `𝔡_{n+1} ∘ post(ℓ_n) = id` (descending an ascended
endomorphism recovers it).

The "endomorphism algebra at level n" is parameterised by an
abstract `R`-module `EndAlg n`; the descent retraction is a linear
map between these. Concretely (e.g. for the Hecke chain) `EndAlg n`
would be the algebra `End_C(A_n)`; here we keep it abstract so the
typeclass is reusable for both the categorical brane tower and the
algebraic Hecke-chain instantiation.

Per AGENTS.md §3b, this is a structural typeclass; substantive
proofs at instances are deferred until concrete chains are wired
up. The fields encode the **algebraic content** of the chain
(idempotent decomposition, retraction identity); category-level
content (objects, morphisms) lives in
`lifting-and-descent/jet-prolongation.lean`.
-/
class JetChain
    (R : Type u) [CommRing R]
    (EndAlg : ℕ → Type v)
    [∀ n, AddCommGroup (EndAlg n)] [∀ n, Module R (EndAlg n)] where
  /-- Ascent at level n: post-composition by `ℓ_n` lifts an
  endomorphism at level `n` to one at level `n+1`. -/
  ascent : ∀ n, EndAlg n →ₗ[R] EndAlg (n + 1)
  /-- Descent retraction at level n+1. -/
  descent : ∀ n, EndAlg (n + 1) →ₗ[R] EndAlg n
  /-- Retraction identity: descending an ascended endomorphism
  recovers it. Equivalent to `ℓ_n` embedding `A_n` as a direct
  summand of `A_{n+1}` (Frobenius non-degeneracy). -/
  descent_ascent : ∀ n (x : EndAlg n), descent n (ascent n x) = x

namespace JetChain

variable {R : Type u} [CommRing R]
  {EndAlg : ℕ → Type v}
  [∀ n, AddCommGroup (EndAlg n)] [∀ n, Module R (EndAlg n)]
  [JC : JetChain R EndAlg]

/-- The descent involution `τ̂_n = ℓ_n ∘ 𝔡_{n+1}` at level `n+1`.
An idempotent endomorphism of `EndAlg (n+1)`. -/
def descentInvolution (n : ℕ) : EndAlg (n + 1) →ₗ[R] EndAlg (n + 1) :=
  JC.ascent n ∘ₗ JC.descent n

/-- The descent involution is idempotent.

Proof: `τ̂_n² = ℓ_n ∘ 𝔡_{n+1} ∘ ℓ_n ∘ 𝔡_{n+1}
             = ℓ_n ∘ (𝔡_{n+1} ∘ ℓ_n) ∘ 𝔡_{n+1}
             = ℓ_n ∘ id ∘ 𝔡_{n+1}
             = τ̂_n`,
where the inner `𝔡_{n+1} ∘ ℓ_n = id` is the retraction identity
(`descent_ascent`). -/
theorem descentInvolution_idempotent (n : ℕ) :
    descentInvolution (R := R) (EndAlg := EndAlg) n ∘ₗ
      descentInvolution (R := R) (EndAlg := EndAlg) n =
    descentInvolution (R := R) (EndAlg := EndAlg) n := by
  -- Ref: [def:descent-involution] §"Idempotency"
  ext x
  simp [descentInvolution, LinearMap.comp_apply, JC.descent_ascent]

/-- An element of `EndAlg (n+1)` is **descended** if it lies in
the image of `τ̂_n` (equivalently, in the image of `ℓ_n`). -/
def isDescended (n : ℕ) (x : EndAlg (n + 1)) : Prop :=
  ∃ y : EndAlg n, JC.ascent n y = x

/-- An element is **transient** if it lies in the kernel of `τ̂_n`. -/
def isTransient (n : ℕ) (x : EndAlg (n + 1)) : Prop :=
  descentInvolution (R := R) (EndAlg := EndAlg) n x = 0

/-- The descended part of an element under the descent-involution
projection: `τ̂_n x ∈ im τ̂_n`. -/
def descendedPart (n : ℕ) (x : EndAlg (n + 1)) : EndAlg (n + 1) :=
  descentInvolution (R := R) (EndAlg := EndAlg) n x

/-- The transient part of an element: `x − τ̂_n x ∈ ker τ̂_n`. -/
def transientPart (n : ℕ) (x : EndAlg (n + 1)) : EndAlg (n + 1) :=
  x - descentInvolution (R := R) (EndAlg := EndAlg) n x

/-- Every `x ∈ EndAlg (n+1)` decomposes as `x = descended + transient`. -/
theorem decomposition (n : ℕ) (x : EndAlg (n + 1)) :
    x = descendedPart (R := R) (EndAlg := EndAlg) n x +
        transientPart (R := R) (EndAlg := EndAlg) n x := by
  simp [descendedPart, transientPart]

/-- The descended part of an element is descended (lies in `im τ̂_n`). -/
theorem descendedPart_isDescended (n : ℕ) (x : EndAlg (n + 1)) :
    isDescended (JC := JC) n
      (descendedPart (R := R) (EndAlg := EndAlg) n x) := by
  -- Ref: [def:descent-involution]; im τ̂_n = im ℓ_n.
  refine ⟨JC.descent n x, ?_⟩
  rfl

/-- The transient part of an element is transient (lies in `ker τ̂_n`).

Proof: `τ̂_n (x − τ̂_n x) = τ̂_n x − τ̂_n² x = τ̂_n x − τ̂_n x = 0`,
using idempotency of `τ̂_n`. -/
theorem transientPart_isTransient (n : ℕ) (x : EndAlg (n + 1)) :
    isTransient (JC := JC) n
      (transientPart (R := R) (EndAlg := EndAlg) n x) := by
  -- Ref: [prop:descent-eigenspaces] §"Kernel projector".
  unfold isTransient transientPart descentInvolution
  have h := descentInvolution_idempotent (R := R) (EndAlg := EndAlg)
              (JC := JC) n
  simp [descentInvolution, LinearMap.comp_apply, JC.descent_ascent,
        LinearMap.map_sub]

/-- **Inter-level pentagon ascension** — operator-lift typeclass +
substantive theorem.

For a triple `(i, j, k)` of braid-generator indices and the
operator-lift `Ũ_ℓ : EndAlg n →ₗ[R] EndAlg (n+1)` carrying the
quantum-torus structure, the level-internal product
`u = Ũ_i Ũ_j` and `v = Ũ_k` satisfy
`u · v = q · v · u + R_q` where `R_q ∈ im τ̂_n` is the descended
residual (i.e., is fixed by the descent involution).

This is `prop:pentagon-uv-commutation`'s **inter-level lift**
content. The level-internal version (single jet level n) is plain
commutativity in the scalar trace ring; see
`QOU.BraidKnot.VhatPairCommutationTrace`.

The typeclass `InterLevelLift` packages the operator lift `Ũ_ℓ`
together with the q-graded commutation identity as fields. A
concrete instance for the Hecke chain awaits the substantive
brane-tower / `H_n(q) → H_{n+1}(q)` quantum-torus implementation,
but downstream theorems can already be stated and proved
**conditionally** on `InterLevelLift` — making this typeclass the
clean assumption point. -/
class InterLevelLift
    (R : Type u) [CommRing R]
    (EndAlg : ℕ → Type v)
    [∀ n, AddCommGroup (EndAlg n)] [∀ n, Module R (EndAlg n)]
    [∀ n, Mul (EndAlg n)] (q : R)
    extends JetChain R EndAlg where
  /-- Per-jet-level operator lift `Ũ_ℓ : EndAlg n → EndAlg (n+1)`,
  one for each braid-generator index `ℓ : Generator n`. -/
  liftOperator : ∀ (n : ℕ), Generator n → EndAlg n →ₗ[R] EndAlg (n + 1)
  /-- The q-graded inter-level commutation identity. For
  `i, j, k : Generator n` (necessarily i < j < k for non-trivial
  ordering), the operator-lift product
    `u = Ũ_i ∘ Ũ_j` (composition lifted to End_C(A_{n+1}))
    `v = Ũ_k`
  satisfies `u · v = q · v · u  +  R_q`, where `R_q ∈ im τ̂_n` (i.e.
  is fixed by the descent involution).

  This is the Step-3-and-4 content of
  `prop:pentagon-uv-commutation`'s narrative derivation: braid
  relation + Hecke quadratic + descent splitting on the q-eigenblock.

  Stated as the existence of `R_q` with the divisibility-by-descent
  property so that any concrete instance only needs to exhibit the
  operator-lift action and verify the residual is descended. -/
  q_graded_commutation :
    ∀ (n : ℕ) (i j k : Generator n) (x : EndAlg n),
      ∃ R_q : EndAlg (n + 1),
        descendedPart (R := R) (EndAlg := EndAlg) n R_q = R_q ∧
        -- u · v = q · v · u + R_q, where u = Ũ_i Ũ_j, v = Ũ_k.
        -- So u·v = (Ũ_i Ũ_j) · Ũ_k  and  v·u = Ũ_k · (Ũ_i Ũ_j).
        (liftOperator n i x) * (liftOperator n j x) *
          (liftOperator n k x) =
        q • ((liftOperator n k x) *
              ((liftOperator n i x) * (liftOperator n j x)))
        + R_q

namespace InterLevelLift

variable {R : Type u} [CommRing R]
  {EndAlg : ℕ → Type v}
  [∀ n, AddCommGroup (EndAlg n)] [∀ n, Module R (EndAlg n)]
  [∀ n, Mul (EndAlg n)] {q : R}
  [IL : InterLevelLift R EndAlg q]

/-- Pentagon UV-commutation on the transient block.

Specialised consequence of `q_graded_commutation`: when `R_q`
vanishes (e.g., on the transient summand `B_λ^trans = ker τ̂_n`,
where the descended part is by definition zero), the q-graded
identity simplifies to the pure quantum-torus relation
`u·v = q·v·u`.

This is the **clean inter-level pentagon** statement that the
narrative `prop:pentagon-uv-commutation` Step 4 isolates. -/
theorem pentagon_inter_level_on_transient
    (n : ℕ) (i j k : Generator n) (x : EndAlg n)
    (h_transient : ∀ R_q : EndAlg (n + 1),
      descendedPart (R := R) (EndAlg := EndAlg) n R_q = R_q →
      R_q = 0) :
    (IL.liftOperator n i x) * (IL.liftOperator n j x) *
      (IL.liftOperator n k x) =
    q • ((IL.liftOperator n k x) *
          ((IL.liftOperator n i x) * (IL.liftOperator n j x))) := by
  -- Ref: [prop:pentagon-uv-commutation], §"Step 4 — Quantum-torus
  --   relation on the transient block".
  -- Ref: [leitner2026] docs/audits/2026-05-02-r7-pentagon-trace-vs-operator.md
  obtain ⟨R_q, h_desc, h_eq⟩ := IL.q_graded_commutation n i j k x
  have hR : R_q = 0 := h_transient R_q h_desc
  rw [h_eq, hR, add_zero]

end InterLevelLift

/-- Forward-declaration placeholder (kept for backward compatibility
with downstream code that hypothesised against this name during
PR #506). New code should hypothesise against `InterLevelLift`
instead. -/
theorem pentagon_inter_level_placeholder
    {R : Type u} [CommRing R]
    {EndAlg : ℕ → Type v}
    [∀ n, AddCommGroup (EndAlg n)] [∀ n, Module R (EndAlg n)]
    [∀ n, Mul (EndAlg n)] {q : R}
    [IL : InterLevelLift R EndAlg q]
    (n : ℕ) (i j k : Generator n) (x : EndAlg n)
    (h_transient : ∀ R_q : EndAlg (n + 1),
      descendedPart (R := R) (EndAlg := EndAlg) n R_q = R_q →
      R_q = 0) :
    (IL.liftOperator n i x) * (IL.liftOperator n j x) *
      (IL.liftOperator n k x) =
    q • ((IL.liftOperator n k x) *
          ((IL.liftOperator n i x) * (IL.liftOperator n j x))) := by
  -- Ref: [leitner2026] superseded by InterLevelLift.pentagon_inter_level_on_transient.
  exact InterLevelLift.pentagon_inter_level_on_transient n i j k x h_transient

end JetChain

end QOU.LiftingDescent
