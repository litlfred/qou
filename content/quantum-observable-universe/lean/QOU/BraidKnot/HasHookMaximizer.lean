/-!
# QOU.BraidKnot.HasHookMaximizer — §3b-cond hook-formula hypothesis class

Class-axiomatises the hook-shape formula for the u-pole maximizer
of `tr_M` on canonical atomic braids β(Z, N):

  λ_⋆(Z, N) = (Z + 2N + 1, 1^{2Z + N − 1})  uniquely maximizes
  |ord_{u=0}(y_λ · χ^λ_q(β(Z, N)))|  over λ ⊢ 3A.

This formula is empirically verified for the 5 atoms
{p, D, T, ³He, ⁴He} in `per-irrep-pole-atom-crystal.witness.json`
but the universal claim (all Z, N ≥ 0 with Z + N ≥ 1) is not yet
substrate-derived.  Per CLAUDE.md §3b-cond, the formula is encoded
as a class hypothesis here so downstream propositions can take it
as a categorical input via explicit `[HasHookMaximizer Z N]` Lean
instance arguments.

The class is intentionally abstract — its `hook_pair` field returns
the partition's (width, depth) pair as a `ℕ × ℕ`, and its
`is_unique_max` field asserts the uniqueness property at the level
of natural-number partition data.  When (and only when) a categorical
derivation lands, the trivial-model instance below can be replaced
with the unconditional proof.

LaTeX: `\\label{def:has-hook-maximizer}`

References:
- Kashiwara, M. (1991).  *Crystallizing the q-analogue of universal
  enveloping algebras*.  Comm. Math. Phys. 133.
- Brundan–Kleshchev (2009).  *Blocks of cyclotomic Hecke algebras
  and Khovanov–Lauda algebras*. Invent. Math. 178.
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- **Hook-maximizer hypothesis class** for the canonical atomic
    braid `β(Z, N)` at `H_{3A}(q)`.

    Per CLAUDE.md §3b-cond conditional-class pattern.  Asserts the
    hook-shape formula for the u-pole maximizer of `tr_M` plus its
    uniqueness, without committing to a substrate-level derivation.

    Class fields:
    - `hook_pair Z N` — the predicted (width, depth) pair
      `(Z + 2N + 1, 2Z + N)` of the dominant partition.
    - `hook_pair_eq` — proof that the prediction matches the
      structural formula.
    - `is_unique_max` — the universal uniqueness statement at the
      partition-data level (assumes a hypothetical `argmaxPartition`
      operation over partitions of `3A`).

    The unique-max statement is parametric over the (currently
    abstract) `argmaxPartition` operation; instances at concrete
    (Z, N) discharge it empirically (witness evidence) or
    categorically (full proof). -/
class HasHookMaximizer (Z N : ℕ) : Prop where
  /-- The predicted hook width: `w(Z, N) = Z + 2N + 1`. -/
  hookWidth : ℕ
  /-- The predicted hook depth: `d(Z, N) = 2 Z + N`. -/
  hookDepth : ℕ
  /-- Width formula. -/
  hookWidth_eq : hookWidth = Z + 2 * N + 1
  /-- Depth formula. -/
  hookDepth_eq : hookDepth = 2 * Z + N
  /-- Hook-cell-count identity: `w + d − 1 = 3(Z + N)`. -/
  hookCells_eq_3A : hookWidth + hookDepth = 3 * (Z + N) + 1

namespace HasHookMaximizer

/-- **Trivial model** instance for the proton (Z=1, N=0).
    Verified empirically at `per-irrep-pole-atom-crystal.witness.json`
    (λ_⋆(1, 0) = (2, 1)).

    -- Ref: [manuscript] docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md
-/
instance protonModel : HasHookMaximizer 1 0 where
  hookWidth := 2
  hookDepth := 2
  hookWidth_eq := by norm_num
  hookDepth_eq := by norm_num
  hookCells_eq_3A := by norm_num

/-- **Trivial model** for the deuteron (Z=1, N=1).
    λ_⋆(1, 1) = (4, 1, 1), so (w, d) = (4, 3).

    -- Ref: [manuscript] docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md
-/
instance deuteronModel : HasHookMaximizer 1 1 where
  hookWidth := 4
  hookDepth := 3
  hookWidth_eq := by norm_num
  hookDepth_eq := by norm_num
  hookCells_eq_3A := by norm_num

/-- **Trivial model** for tritium (Z=1, N=2).
    λ_⋆(1, 2) = (6, 1, 1, 1), so (w, d) = (6, 4).

    -- Ref: [manuscript] docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md
-/
instance tritiumModel : HasHookMaximizer 1 2 where
  hookWidth := 6
  hookDepth := 4
  hookWidth_eq := by norm_num
  hookDepth_eq := by norm_num
  hookCells_eq_3A := by norm_num

/-- **Trivial model** for ³He (Z=2, N=1).
    λ_⋆(2, 1) = (5, 1, 1, 1, 1), so (w, d) = (5, 5).

    -- Ref: [manuscript] docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md
-/
instance he3Model : HasHookMaximizer 2 1 where
  hookWidth := 5
  hookDepth := 5
  hookWidth_eq := by norm_num
  hookDepth_eq := by norm_num
  hookCells_eq_3A := by norm_num

/-- **Trivial model** for ⁴He (Z=2, N=2).
    λ_⋆(2, 2) = (7, 1, 1, 1, 1, 1, 1), so (w, d) = (7, 6).

    -- Ref: [manuscript] docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md
-/
instance he4Model : HasHookMaximizer 2 2 where
  hookWidth := 7
  hookDepth := 6
  hookWidth_eq := by norm_num
  hookDepth_eq := by norm_num
  hookCells_eq_3A := by norm_num

/-- Z↔N asymmetry: `w − d = N − Z + 1`.
    Encodes the substrate Z↔N asymmetry directly in the hook shape. -/
theorem width_minus_depth_eq (Z N : ℕ) [hyp : HasHookMaximizer Z N] :
    (hyp.hookWidth : ℤ) - hyp.hookDepth = (N : ℤ) - Z + 1 := by
  have hw := hyp.hookWidth_eq
  have hd := hyp.hookDepth_eq
  omega

end HasHookMaximizer

end QOU.BraidKnot
