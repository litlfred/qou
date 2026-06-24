import QOU.BraidKnot.IdentityIContentDecomposition
import QOU.BraidKnot.WLambdaDefectClosedForm

/-!
# Identity I — the Plancherel content-square mean, conditional on standard `S_n` rep theory

The s5-so3 keystone's falsifiable `W_λ` defect cubic `144·C(n) = −n(n−1)(2n−13)` carries one
representation-theoretic input, **Identity I**

  `M(n) = (1/n!) Σ_{λ⊢n} dim(λ)² Σ_{c∈λ} h_c² = n(3n−1)/2`,

held in `WLambdaDefectClosedForm` as a bare `def twoM n = n(3n−1)` (compute-verified `n ≤ 14`).
This file upgrades that carried `def` to a **rigorous conditional theorem** (AGENTS.md §3b-cond):
Identity I is *proved*, sorry-free, modulo a single named `class` axiomatising the two standard
`ℂ[S_n]` facts that the pinned Mathlib lacks (no Specht modules, no Jucys–Murphy elements, no
Okounkov–Vershik content theorem; full construction is a multi-session Mathlib build).

The split is:

* **(A)** the per-partition `Σ_c h_c² = Σ_c c(c)² + n²` — a single-Young-diagram fact, **proved
  unconditionally** (`sumSqHooks_eq_sumSqContents_add_sq`, all weakly-decreasing partitions);
* **(i)** `Σ_λ dim(λ)² = n!` — the regular representation of `S_n` decomposes with each
  irreducible `V_λ` of multiplicity `dim(λ)` (axiomatised: `PlancherelSnData.sum_dim_sq`);
* **(ii)** the Jucys–Murphy / Okounkov–Vershik content-square Plancherel mean — the central
  `Σ_k X_k²` acts on `V_λ` by the scalar `Σ_{c∈λ} c(c)²`, whose Plancherel average is the
  identity coefficient `Σ_{k<n} k = binom(n,2)` (arithmetic core `jm_identity_coeff_two`,
  proved); axiomatised cleared of `1/n!` as `PlancherelSnData.two_sum_dim_sq_content`.

Given (A), (i), (ii), Identity I is pure algebra: `Σ_λ dim² Σ_c h_c² = Σ_λ dim² (Σc² + n²) =
binom(n,2)·n! + n²·n! = (binom(n,2)+n²)·n! = n(3n−1)/2 · n!`.  The result is the cleared form
`2·Σ_λ dim²·Σ_c h_c² = n(3n−1)·n!`, which `twoM_eq_plancherel_hook_sum` identifies with
`WLambdaDefect.twoM`.

**Discipline.** §3b-cond: the class fields carry only the *inputs* (the partition set, the
dimensions, and the two standard sums); the theorem **derives** Identity I from them and never
assumes its own conclusion — non-degenerate.  Both axioms are textbook-true (regular-rep
decomposition; Okounkov–Vershik), merely absent from the pinned Mathlib.  Base ring `ℤ`; nothing
archimedean (no `q₀`, no 210 ppb); no fit.
-/

open Finset

namespace QOU.BraidKnot.IdentityI

/-- **Plancherel data for `S_n` (the two standard facts the pinned Mathlib lacks).**

Carries the partitions of `n` (weakly-decreasing `List ℕ`), their SYT dimensions `dim(λ)`, and
the two standard representation-theoretic identities (i) `Σ dim² = n!` and (ii) the cleared
content-square Plancherel mean.  These axiomatise exactly what is **not** in the pinned Mathlib;
the per-partition (A) is proved separately and used in the theorems below, so this class is the
*only* unproved input to a conditional Identity I (§3b-cond). -/
class PlancherelSnData (n : ℕ) where
  /-- The partitions of `n`, as weakly-decreasing `List ℕ`. -/
  parts : Finset (List ℕ)
  /-- Each listed partition is weakly decreasing — the hypothesis (A) needs. -/
  parts_sorted : ∀ l ∈ parts, l.Sorted (· ≥ ·)
  /-- Each listed partition has size `n`. -/
  parts_sz : ∀ l ∈ parts, sz l = n
  /-- The SYT dimension `dim(λ)`. -/
  dim : List ℕ → ℕ
  /-- **(i)** `Σ_λ dim(λ)² = n!` — the regular-representation dimension sum. -/
  sum_dim_sq : ∑ l ∈ parts, ((dim l : ℤ)) ^ 2 = (n.factorial : ℤ)
  /-- **(ii)** Jucys–Murphy / Okounkov–Vershik content-square mean, cleared of `1/n!`:
  `2·Σ_λ dim(λ)²·Σ_c c(c)² = n(n−1)·n!`. -/
  two_sum_dim_sq_content :
    2 * ∑ l ∈ parts, ((dim l : ℤ)) ^ 2 * sumSqContents l
      = (n : ℤ) * ((n : ℤ) - 1) * (n.factorial : ℤ)

/-- **Identity I, conditional (sorry-free modulo `PlancherelSnData`).** The Plancherel-expected
squared-**hook** sum, cleared of `1/n!`, equals `n(3n−1)·n!` — i.e. `M(n) = n(3n−1)/2`.

Proof: replace each `Σ_c h_c²` by `Σ_c c(c)² + n²` (**(A)**, using `parts_sorted`/`parts_sz`),
split, discharge the content half by **(ii)** and the `n²·Σdim²` half by **(i)**; the residue is
`ring`.  The only unproved inputs are the two class fields. -/
theorem two_sum_dim_sq_hooks (n : ℕ) [h : PlancherelSnData n] :
    2 * ∑ l ∈ h.parts, ((h.dim l : ℤ)) ^ 2 * sumSqHooks l
      = (n : ℤ) * (3 * (n : ℤ) - 1) * (n.factorial : ℤ) := by
  have hstep : ∀ l ∈ h.parts, ((h.dim l : ℤ)) ^ 2 * sumSqHooks l
      = ((h.dim l : ℤ)) ^ 2 * sumSqContents l + ((h.dim l : ℤ)) ^ 2 * (n : ℤ) ^ 2 := by
    intro l hl
    rw [sumSqHooks_eq_sumSqContents_add_sq l (h.parts_sorted l hl), h.parts_sz l hl]; ring
  rw [Finset.sum_congr rfl hstep, Finset.sum_add_distrib, mul_add, h.two_sum_dim_sq_content]
  have hpull : ∑ l ∈ h.parts, ((h.dim l : ℤ)) ^ 2 * (n : ℤ) ^ 2
      = (∑ l ∈ h.parts, ((h.dim l : ℤ)) ^ 2) * (n : ℤ) ^ 2 := by
    rw [Finset.sum_mul]
  rw [hpull, h.sum_dim_sq]
  ring

/-- **Identity I wires into the keystone `twoM` (conditional).** `WLambdaDefect.twoM n = n(3n−1)`
carries Identity I as a bare `def`; this proves that closed form **is** the Plancherel
squared-hook sum (cleared by `2` / `n!`), conditional on `PlancherelSnData`.  So the keystone's
`twoM` is no longer carried — it equals its representation-theoretic definition modulo the two
named, standard, Mathlib-absent axioms. -/
theorem twoM_eq_plancherel_hook_sum (n : ℕ) [h : PlancherelSnData n] :
    2 * ∑ l ∈ h.parts, ((h.dim l : ℤ)) ^ 2 * sumSqHooks l
      = QOU.BraidKnot.WLambdaDefect.twoM (n : ℤ) * (n.factorial : ℤ) := by
  rw [two_sum_dim_sq_hooks]
  unfold QOU.BraidKnot.WLambdaDefect.twoM
  ring

end QOU.BraidKnot.IdentityI
