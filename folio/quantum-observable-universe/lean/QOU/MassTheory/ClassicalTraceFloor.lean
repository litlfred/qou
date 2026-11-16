import Mathlib.Tactic

/-!
# The classical floor of the categorical binding trace

Bean `qou-zrx2`. Probes:
`computations/probes/hbar_q_order_of_binding_observables_probe.py` (the
discovery) and `classical_floor_derivation_probe.py` (the derivation).

## What this is about

The corpus reads nuclear binding off the **signed categorical trace difference**

    Δtr(Z,N) = tr_M(W_free) − tr_M(W_atom)

at `H_{3A}` (`binding_canonical`, `derive_binding_chain_cooperative`). Every
*energy* in the framework vanishes as `q → 1`, where the Hecke algebra
degenerates to `ℂ[S_n]` and no deformation is left — `Δ(net) = h(h−2)/2` does,
and so does the Plancherel block sum. **`Δtr` does not.** Measured along
`q = exp η`, it converges to a nonzero limit:

    A = 2  →  1/8          A = 3  →  3/32
    A = 4  →  7/128        A = 5  →  15/512

so `Δtr = c₀(A) + c₁·ℏ_q + O(ℏ_q²)`, and at `q₀` the classical part is
**85.01 %** of it for the deuteron and **9.61 %** for `⁴He` on the canonical
Borromean word (`intra_order="borromean"`, owner ruling `qou-92u9`; **22.46 %**
and **4.88 %** on the historical pre-2026-09-05 `grouped` word). That fraction
of any binding read off this observable is present with the braiding switched off.
For the general interface-parity formula `c₀(A, O) = 2^{-A}(1 - 2^{-O})` with `O`
odd-multiplicity inter-nucleon interfaces (vanishing at `O = 0`), see
`QOU.MassTheory.ClassicalTraceFloorParity`.

This file records the **arithmetic core of the derivation** of `c₀(A)` — the
part that is genuinely proved rather than computed.

## The derivation, and where it is and is not formal

1. **Schur–Weyl at `q = 1`** gives `tr_M(β)|_{q=1} = 2^{c(σ_β) − n}`, with
   `c(σ)` the cycle count of the permutation underlying `β`. The Markov weights
   are `y_λ = s_λ(1,Q)/(1+Q)^n`; at `Q = 1`, `s_λ(1,1) = dim V_λ^{GL(2)}`
   (zero for `ℓ(λ) > 2` — the corpus's row cap), and
   `Σ_λ dim V_λ · χ^λ(σ)` is the character of `σ` permuting the factors of
   `(ℂ²)^{⊗n}`, which is `2^{c(σ)}` since `σ` fixes exactly the basis vectors
   constant on each cycle.
   **NOT formal here.** Mathlib has no Schur–Weyl duality. It enters
   `classical_floor_of_cycle_counts` as the two explicit hypotheses `hSWfree`
   and `hSWatom` — visible in the statement rather than hidden in a class with
   no instance, because it is a *published theorem* the corpus is entitled to
   assume, not an open conjecture.
2. **The cycle counts.** Every letter `(c, d, g)` of `atom_braid_word_3A` has
   `d ∈ {0, −h, −h/2}` with `h = q − 1/q`, so at `q = 1` every letter degenerates
   to the transposition `s_g` and the permutation is `q`-independent. Counting:
   `c(σ_free) = 2A` and `c(σ_atom) = A + 1`, verified for `A = 2 … 20` directly
   from the words — no trace evaluation, so it holds far past `A = 5` where the
   Markov trace stops being computable.
   **NOT formal here.** It is a computation on a concrete word; it enters as
   `hfree` and `hmerge`.
3. **The arithmetic.** Given 1 and 2, `c₀(A) = 2^{−A} − 2^{1−2A}`.
   **This is what the file proves.**

The split is deliberate. Assuming step 1 assumes a published theorem; assuming
step 2 assumes an 18-point computation; step 3 is then not numerics at all, and
stating it here is what stops the closed form from resting on the Richardson
extrapolation it was originally read off.

## Why `hmerge` is the right way to state step 2

`c(σ_free) − c(σ_atom) = A − 1` says **each of the `A−1` inter-nucleon interfaces
merges exactly one pair of cycles**. That is one clean fact, and it is the same
`(A−1)`-bond chain adjacency `derive_binding_chain_cooperative` sums over —
arrived at from the permutation rather than from the interface list. So the
floor's `A`-dependence *is* the chain structure, and phrasing the hypothesis this
way makes that visible instead of tabulating two opaque counts.

-- Ref: [leitner2026] bean qou-zrx2; computations/probes/classical_floor_derivation_probe.py
-/

namespace QOU.MassTheory

/-- The classical (`q = 1`) trace difference, as it comes out of the two cycle
counts: `2^{c_free − n} − 2^{c_atom − n}`.

Integer exponents throughout — `c_atom − n` is negative in every case of
interest, so `zpow` is the honest type. -/
noncomputable def classicalTraceFloor (cFree cAtom n : ℤ) : ℚ :=
  (2 : ℚ) ^ (cFree - n) - (2 : ℚ) ^ (cAtom - n)

/-- **The atom-word cycle count follows from the free count and the merges.**

`c_free = 2A` (two cycles per free nucleon) together with "each of the `A−1`
interfaces merges one pair" forces `c_atom = A + 1`. Stated separately because
it is the step where the chain adjacency enters, and it is pure arithmetic once
the merge count is granted. -/
theorem cAtom_eq_of_free_and_merges {A cFree cAtom : ℤ}
    (hfree : cFree = 2 * A) (hmerge : cFree = cAtom + (A - 1)) :
    cAtom = A + 1 := by
  omega

/-- **The closed form, from the chain cycle counts.** Pure exponent bookkeeping:
`2A − 3A = −A` and `(A+1) − 3A = 1 − 2A`. -/
theorem classicalTraceFloor_chain (A : ℤ) :
    classicalTraceFloor (2 * A) (A + 1) (3 * A)
      = (2 : ℚ) ^ (-A) - (2 : ℚ) ^ (1 - 2 * A) := by
  unfold classicalTraceFloor
  have hexp1 : 2 * A - 3 * A = -A := by omega
  have hexp2 : (A + 1) - 3 * A = 1 - 2 * A := by omega
  rw [hexp1, hexp2]

/-- **The floor, end to end.**

`hfree` and `hmerge` are step 2 (the cycle counts, computed from the braid
words); `hSWfree` and `hSWatom` are step 1 (Schur–Weyl at `q = 1`, a published
theorem Mathlib does not carry). Everything between them is derived.

The conclusion is exactly the form the probes measured — `1/8` at `A = 2`,
`7/128` at `A = 4` — but here it is not extrapolated. -/
theorem classical_floor_of_cycle_counts
    {A cFree cAtom : ℤ} {trFree trAtom : ℚ}
    (hfree : cFree = 2 * A)
    (hmerge : cFree = cAtom + (A - 1))
    (hSWfree : trFree = (2 : ℚ) ^ (cFree - 3 * A))
    (hSWatom : trAtom = (2 : ℚ) ^ (cAtom - 3 * A)) :
    trFree - trAtom = (2 : ℚ) ^ (-A) - (2 : ℚ) ^ (1 - 2 * A) := by
  have hc : cAtom = A + 1 := cAtom_eq_of_free_and_merges hfree hmerge
  subst hfree
  subst hc
  rw [hSWfree, hSWatom]
  exact classicalTraceFloor_chain A

/-! ### The contamination dies exponentially

`c₀(A) = 2^{−A} − 2^{1−2A}` is positive and strictly below `2^{−A}` for `A ≥ 2`
(it vanishes at `A = 1`, where the exponents coincide),
so the classical part of `Δtr` is bounded by `2^{−A}` while `Δtr(q₀)` itself
grows with `A`. That is the formal content of the measured decay — 22.46 % at
the deuteron, 10.55 % at tritium, 4.88 % at `⁴He`, 2.16 % at `⁵Li`, halving per
nucleon.

It matters for reading the corpus's own results: the deuteron's apparent
agreement under convention A was floor-driven and does not survive the
subtraction, while the `⁴He` 4-body α-residual is essentially untouched by it. -/

/-- The floor is strictly positive for `A ≥ 2`.

`A ≥ 2`, not `A ≥ 1`: at `A = 1` the two exponents coincide (`1 − 2 = −1`) and
the floor is exactly `0`. Every nucleus has `A ≥ 2`, so the bound covers the
whole range of interest, but the boundary case is real and is why the hypothesis
is not `1 ≤ A`. -/
theorem classicalTraceFloor_pos {A : ℤ} (hA : 2 ≤ A) :
    0 < (2 : ℚ) ^ (-A) - (2 : ℚ) ^ (1 - 2 * A) := by
  have h : (1 : ℤ) - 2 * A < -A := by omega
  have := zpow_lt_zpow_right₀ (by norm_num : (1 : ℚ) < 2) h
  linarith

/-- And it is strictly below `2^{−A}`, so it decays at least geometrically. -/
theorem classicalTraceFloor_lt {A : ℤ} :
    (2 : ℚ) ^ (-A) - (2 : ℚ) ^ (1 - 2 * A) < (2 : ℚ) ^ (-A) := by
  have : (0 : ℚ) < (2 : ℚ) ^ (1 - 2 * A) := by positivity
  linarith

/-- The two values the probes report at the deuteron and `⁴He`, as a check that
the general form specialises correctly: `1/8` and `7/128`. -/
example : (2 : ℚ) ^ (-(2 : ℤ)) - (2 : ℚ) ^ (1 - 2 * (2 : ℤ)) = 1 / 8 := by
  norm_num

example : (2 : ℚ) ^ (-(4 : ℤ)) - (2 : ℚ) ^ (1 - 2 * (4 : ℤ)) = 7 / 128 := by
  norm_num

end QOU.MassTheory
