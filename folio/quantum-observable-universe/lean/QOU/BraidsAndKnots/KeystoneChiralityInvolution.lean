import QOU.MathlibExt.QPartitionCombinatorics

/-!
# QOU.BraidsAndKnots.KeystoneChiralityInvolution
  — C2 of the keystone necessary conditions: the forced transpose / chirality
    involution

The s5-so3 keystone's geometric index must reproduce the q-Plancherel weights
`W_λ = d_q(λ)²/[n]_q!`.  Necessary condition **C2**
(`2026-06-16-keystone-index-necessary-conditions.md`) is **conjugation symmetry**
`W_λ = W_{λ'}`, which holds *exactly* at `q₀` because the hook-length multiset is
transpose-invariant (`h_λ(i,j) = h_{λ'}(j,i)`), so `d_q(λ) = d_q(λ')`.  C2 is the
strongest pruning lever: any construction must carry the involution inducing
transpose `λ ↔ λ'` — which on the QOU side is precisely the **chirality flip
`T₁ ↔ T₂`**.  A construction without it is dead on arrival.

This file machine-checks the structural facets of C2 over the corpus partition
type:

  * `cellContent_transpose_neg` — the **chirality atom**: a cell's content
    `c(i,j) = j − i` *negates* under transpose `(i,j) ↦ (j,i)`.  Chirality = sign
    of content, so transpose flips chirality.
  * `electron_self_conjugate` + `electron_content_zero` — the electron block
    `(3,1,1)` is **self-conjugate** (a transpose fixed point) and hence
    chirality-neutral (`c(λ) = 0`).  This is the keystone's central A₅ rep
    (`(3,1,1) = T₁ ⊕ T₂` self-conjugate; ledger #2424).
  * `conjugate_two_content_flip` — a concrete transpose pair `[2] ↔ [1,1]`
    exhibits the chirality flip `c(λ') = − c(λ)`.

The global `W_λ = W_{λ'}` (transpose-invariance of `d_q`) is the cited +
numerically-witnessed necessary condition (`keystone_index_necessary_conditions.py`,
max diff 0.0 at q₀); these are its formalized facets.

Refs:
- [macdonald1995] Symmetric Functions and Hall Polynomials, I.1 (conjugate / hooks)
- [leitner2026] docs/audits/2026-06-16-keystone-index-necessary-conditions.md (C2)
-/

open QOU.MathlibExt.QPartitionCombinatorics

namespace QOU.BraidsAndKnots.KeystoneChiralityInvolution

/-- **Chirality atom.**  A cell's content `c(i,j) = j − i` negates under transpose
    `(i,j) ↦ (j,i)`.  Since chirality is the sign of the content, transpose flips
    chirality — the involution C2 forces. -/
theorem cellContent_transpose_neg (i j : ℕ) :
    cellContent j i = - cellContent i j := by
  unfold cellContent; ring

/-- The electron block `(3,1,1)` is **self-conjugate** (a transpose fixed point).
    Per the keystone, `(3,1,1) = T₁ ⊕ T₂` is the self-conjugate A₅ rep. -/
theorem electron_self_conjugate :
    Partition.conjugate [3, 1, 1] = [3, 1, 1] := by decide

/-- The self-conjugate electron block is **chirality-neutral**: content sum `0`. -/
theorem electron_content_zero : contentSum [3, 1, 1] = 0 := by decide

/-- A concrete transpose pair `[2] ↔ [1,1]` exhibits the chirality flip
    `c(λ') = − c(λ)` that C2 forces (here `c([2]) = 1`, `c([1,1]) = −1`). -/
theorem conjugate_two_content_flip :
    contentSum (Partition.conjugate [2]) = - contentSum [2] := by decide

end QOU.BraidsAndKnots.KeystoneChiralityInvolution
