import QOU.BraidKnot.BringWPlaneMonodromy

/-!
# The depth-2 SL₂ power-trace tower of the Bring W-plane monodromy

Follow-up to `BringWPlaneMonodromy` (the unimodular 2×2 monodromy `M` on the W-plane `H¹(E)`,
`E = Bring/S₄`, with `M² = (tr M)·M − I`, `unimodular_two_recurrence`).

The full-Hecke geometric-index program's selection-rule period `a_D^(n) = lw(n−1)` (#1765) was
empirically pinned this session (sibling bean **z2bn**, PRs **#2795 / #2800 / #2808**): the global
`a_D^(n)` is **super-exponential** (a `√`-branch falling factorial `(1/2)_n`), and the **depth-2
SL₂ trace `τ` is only the `n ≤ 4` effective fit** (it caps at the dominant eigenvalue `λ₊ ≈ 2.18`
while the `lw` ratio keeps growing `1.9 → 3.1`, so SL₂ diverges from `lw` by `n = 5/6`).

This file formalizes the **structural reason** that the depth-2 SL₂ side is a *bounded-by-exponential*
object. From the Cayley–Hamilton relation `M² = (tr M)·M − I`, every power obeys the same depth-2
linear recurrence, and so does the **power-trace tower** `t_n := tr(Mⁿ)` (the quantity the sibling
probe computes):

  `t_{n+2} = (tr M)·t_{n+1} − t_n`   (the Chebyshev / Lucas recurrence, with `τ = tr M`).

A solution of a depth-2 *linear* recurrence is `t_n = A·λ₊ⁿ + B·λ₋ⁿ` (`λ_±` the roots of
`x² − τ x + 1`, `λ₊λ₋ = 1`), hence `O(λ₊ⁿ)` — **exponential**. It therefore cannot reproduce a
**super-exponential** `lw(n−1)` for large `n` — the formalized counterpart of the sibling's
numerical "SL₂ diverges by `n = 5/6`".

**Scope (a), per AGENTS.md "before declaring refuted".** This is a *scope-(a)* statement: the depth-2
SL₂ trace tower, *alone*, is an exponential object and so is only the `n ≤ 4` effective fit — it does
not capture the global super-exponential `a_D`. It is **not** a *scope-(b)* structural exclusion of
SL₂/monodromy data from the closure (the exponential-vs-super-exponential growth gap is cited from
the sibling's empirical run #2795/#2808, not Lean-proved here; the global object plausibly composes
the depth-2 tower with higher q-Bessel / Rogers–Szegő layers, per #2800's 3-layer map).

Base ring `ℝ`; pure linear algebra. `τ` appears only as the symbol `tr M`. No fit.
-/

namespace QOU.BraidKnot

open Matrix

/-- **The matrix-power recurrence.** From `M² = (tr M)·M − I` (`unimodular_two_recurrence`), every
power of a unimodular 2×2 monodromy obeys the same depth-2 recurrence:
`M^{n+2} = (tr M)·M^{n+1} − Mⁿ`. -/
theorem unimodular_pow_recurrence (M : Matrix (Fin 2) (Fin 2) ℝ) (hdet : M.det = 1) (n : ℕ) :
    M ^ (n + 2) = M.trace • M ^ (n + 1) - M ^ n := by
  have h2 : M * M = M.trace • M - 1 := unimodular_two_recurrence M hdet
  have hsplit : M ^ (n + 2) = M ^ n * (M * M) := by
    rw [show n + 2 = n + 1 + 1 from rfl, pow_succ, pow_succ, mul_assoc]
  rw [hsplit, h2, mul_sub, mul_one, mul_smul_comm, ← pow_succ]

/-- **The depth-2 SL₂ power-trace tower recurrence.** The trace tower `t_n := tr(Mⁿ)` of a unimodular
2×2 monodromy satisfies the Chebyshev / Lucas depth-2 *linear* recurrence
`t_{n+2} = (tr M)·t_{n+1} − t_n`, with `τ = tr M`. (Linear ⇒ `t_n = O((tr-dominant-root)ⁿ)`,
exponential — the structural reason the depth-2 SL₂ fit is only `n ≤ 4` effective vs the
super-exponential `a_D^(n) = lw(n−1)`; sibling z2bn, #2795/#2800/#2808.) -/
theorem powTrace_recurrence (M : Matrix (Fin 2) (Fin 2) ℝ) (hdet : M.det = 1) (n : ℕ) :
    (M ^ (n + 2)).trace = M.trace * (M ^ (n + 1)).trace - (M ^ n).trace := by
  rw [unimodular_pow_recurrence M hdet n, Matrix.trace_sub, Matrix.trace_smul, smul_eq_mul]

/-- The first two rungs of the tower are the universal SL₂ trace seeds: `t₀ = tr(I) = 2` and
`t₁ = tr M`. With `powTrace_recurrence` these determine the whole tower `t_n = tr(Mⁿ)` — the depth-2
rigidity: two seeds fix every higher rung (so a depth-2 SL₂ tower has only two free parameters, the
formalized sense in which fitting the low-`n` `lw` values over-determines it). -/
theorem powTrace_seeds (M : Matrix (Fin 2) (Fin 2) ℝ) :
    (M ^ 0).trace = 2 ∧ (M ^ 1).trace = M.trace := by
  refine ⟨?_, ?_⟩
  · simp [Matrix.trace_one]
  · rw [pow_one]

/-- **The carried monodromy's trace tower (from the class).** Any `BringWPlaneMonodromy` instance's
operator generates the depth-2 SL₂ trace tower `t_{n+2} = (tr M)·t_{n+1} − t_n`. -/
theorem monodromy_powTrace_recurrence [self : BringWPlaneMonodromy] (n : ℕ) :
    (self.M ^ (n + 2)).trace = self.M.trace * (self.M ^ (n + 1)).trace - (self.M ^ n).trace :=
  powTrace_recurrence self.M self.unimodular n

end QOU.BraidKnot
