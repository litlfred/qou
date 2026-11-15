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

**Superseded 2026-08-23 — the class is inhabited at every `n`, by a proof.** The paragraph above
describes the state of the world when this file was written. The corpus now has the Specht modules,
the Jucys–Murphy elements and the Okounkov–Vershik content theorem it calls absent (the OV tower,
`OVTopAssembly.snSpectralData`), and
`PlancherelSnDataGeneral.plancherelSnDataGeneral n : PlancherelSnData n` builds the datum for
**every** `n` from them: field (i) from the Robinson–Schensted correspondence
(`QOU.Mathlib.rskBurnsideHolds`), field (ii) from `identityB_general`. So the two fields are no
longer *unproved* inputs — they are proved, in this file's own list model.

What has **not** changed: the fields are still class fields, every signature below still carries
`[PlancherelSnData n]`, and the per-`n` `decide` instances are still the ones instance resolution
picks (the general datum is deliberately a `def`, since the class carries data). The
hypothesis-free restatements of the two payoffs are
`PlancherelSnDataGeneral.two_sum_dim_sq_hooks_general` and
`twoM_eq_plancherel_hook_sum_general`.

Given (A), (i), (ii), Identity I is pure algebra: `Σ_λ dim² Σ_c h_c² = Σ_λ dim² (Σc² + n²) =
binom(n,2)·n! + n²·n! = (binom(n,2)+n²)·n! = n(3n−1)/2 · n!`.  The result is the cleared form
`2·Σ_λ dim²·Σ_c h_c² = n(3n−1)·n!`, which `twoM_eq_plancherel_hook_sum` identifies with
`WLambdaDefect.twoM`.

**Discipline.** §3b-cond: the class fields carry only the *inputs* (the partition set, the
dimensions, and the two standard sums); the theorem **derives** Identity I from them and never
assumes its own conclusion — non-degenerate.  Both axioms are textbook-true (regular-rep
decomposition; Okounkov–Vershik), merely absent from the pinned Mathlib.  Base ring `ℤ`; nothing
archimedean (no `q₀`, no 210 ppb); no fit.

**Abstract (unlabelled) form of (i)+(ii): PROVED on main (2026-07-02).**
`QOU.BraidKnot.IdentityBWedderburn.identityB_via_wedderburn_unconditional` proves, fully
sorry-free (axioms `[propext, Classical.choice, Quot.sound]`), that for `ℂ[Sₙ]` there exist block
data `(N, d, ω)` with `∑ dᵢ² = n!` **and** `∑ dᵢ²·ωᵢ = n!·binom(n,2)` — the Artin–Wedderburn
block decomposition plus the regular-representation trace of `C₂ = ∑ₖ Xₖ²`, whose centrality
(Jucys' theorem) is machine-checked in `QOU.BraidKnot.IdentityBCentrality.centralC2_mem_center`
(coefficient of `C₂` is a class function: `binom(n,2)` at `1`, `1` at each 3-cycle, `0`
elsewhere).  What this class still adds over that abstract statement is exactly the
**partition labelling** of the blocks: that the Wedderburn blocks are indexed by `parts` (the
partitions of `n`), with `d = dim` (the SYT dimension) and `ω = sumSqContents` (the
Okounkov–Vershik content-square scalar).  That labelling — blocks ↔ partitions, `dim = #SYT`,
JM-eigenvalue = contents — is the residual OV content, carried by the brick-5 cores in
`QOU.BraidKnot.JucysMurphy` (`seminormalVector_data_exists`, `exists_indep_seminormal_family`).
-/

open Finset

namespace QOU.BraidKnot.IdentityI

/-- **Plancherel data for `S_n` (the two standard facts the pinned Mathlib lacks).**

Carries the partitions of `n` (weakly-decreasing `List ℕ`), their SYT dimensions `dim(λ)`, and
the two standard representation-theoretic identities (i) `Σ dim² = n!` and (ii) the cleared
content-square Plancherel mean.  These axiomatise exactly what is **not** in the pinned Mathlib;
the per-partition (A) is proved separately and used in the theorems below, so this class is the
*only* unproved input to a conditional Identity I (§3b-cond).

The **unlabelled** form of (i)+(ii) is proved sorry-free on main
(`IdentityBWedderburn.identityB_via_wedderburn_unconditional`: abstract Wedderburn block data
with `∑ d² = n!` and `∑ d²·ω = n!·binom(n,2)`, Jucys centrality machine-checked in
`IdentityBCentrality`); the residual content of these two fields is the **partition labelling**
of the blocks (`parts`/`dim`/`sumSqContents` naming the abstract `(N, d, ω)`). -/
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
  sum_dim_sq : ∑ l ∈ parts, (dim l : ℤ) ^ 2 = (n.factorial : ℤ)
  /-- **(ii)** Jucys–Murphy / Okounkov–Vershik content-square mean, cleared of `1/n!`:
  `2·Σ_λ dim(λ)²·Σ_c c(c)² = n(n−1)·n!`. -/
  two_sum_dim_sq_content :
    2 * ∑ l ∈ parts, (dim l : ℤ) ^ 2 * sumSqContents l
      = (n : ℤ) * ((n : ℤ) - 1) * (n.factorial : ℤ)

/-- **Identity I, conditional (sorry-free modulo `PlancherelSnData`).** The Plancherel-expected
squared-**hook** sum, cleared of `1/n!`, equals `n(3n−1)·n!` — i.e. `M(n) = n(3n−1)/2`.

Proof: replace each `Σ_c h_c²` by `Σ_c c(c)² + n²` (**(A)**, using `parts_sorted`/`parts_sz`),
split, discharge the content half by **(ii)** and the `n²·Σdim²` half by **(i)**; the residue is
`ring`.  The only unproved inputs are the two class fields. -/
theorem two_sum_dim_sq_hooks (n : ℕ) [h : PlancherelSnData n] :
    2 * ∑ l ∈ h.parts, (h.dim l : ℤ) ^ 2 * sumSqHooks l
      = (n : ℤ) * (3 * (n : ℤ) - 1) * (n.factorial : ℤ) := by
  have hstep : ∀ l ∈ h.parts, (h.dim l : ℤ) ^ 2 * sumSqHooks l
      = (h.dim l : ℤ) ^ 2 * sumSqContents l + (h.dim l : ℤ) ^ 2 * (n : ℤ) ^ 2 := by
    intro l hl
    rw [sumSqHooks_eq_sumSqContents_add_sq l (h.parts_sorted l hl), h.parts_sz l hl]; ring
  rw [Finset.sum_congr rfl hstep, Finset.sum_add_distrib, mul_add, h.two_sum_dim_sq_content]
  have hpull : ∑ l ∈ h.parts, (h.dim l : ℤ) ^ 2 * (n : ℤ) ^ 2
      = (∑ l ∈ h.parts, (h.dim l : ℤ) ^ 2) * (n : ℤ) ^ 2 := by
    rw [Finset.sum_mul]
  rw [hpull, h.sum_dim_sq]
  ring

/-- **Identity I wires into the keystone `twoM` (conditional).** `WLambdaDefect.twoM n = n(3n−1)`
carries Identity I as a bare `def`; this proves that closed form **is** the Plancherel
squared-hook sum (cleared by `2` / `n!`), conditional on `PlancherelSnData`.  So the keystone's
`twoM` is no longer carried — it equals its representation-theoretic definition modulo the two
named, standard, Mathlib-absent axioms. -/
theorem twoM_eq_plancherel_hook_sum (n : ℕ) [h : PlancherelSnData n] :
    2 * ∑ l ∈ h.parts, (h.dim l : ℤ) ^ 2 * sumSqHooks l
      = QOU.BraidKnot.WLambdaDefect.twoM (n : ℤ) * (n.factorial : ℤ) := by
  rw [two_sum_dim_sq_hooks]
  unfold QOU.BraidKnot.WLambdaDefect.twoM
  ring

/-- **Non-vacuity witness — `PlancherelSnData 2` is inhabited.** The partitions of `2` are
`[2]` and `[1,1]`, both of SYT dimension `1`; both standard axioms (i)/(ii) check by `decide`
(`Σ dim² = 1+1 = 2 = 2!`; `2·Σ dim²·Σc² = 2·(1+1) = 4 = 2·1·2!`).  This confirms the conditional
theorems above are **not** conditional-on-`False`: the class has a genuine model where the
axioms hold against the actual partition combinatorics. -/
instance plancherelSnData_two : PlancherelSnData 2 where
  parts := {[2], [1, 1]}
  parts_sorted := by decide
  parts_sz := by decide
  dim := fun _ => 1
  sum_dim_sq := by decide
  two_sum_dim_sq_content := by decide

/-- **Stronger non-vacuity witness — `PlancherelSnData 4` from genuine combinatorics.** The
`n = 2` instance above takes `dim ≡ 1` (both partitions one-dimensional), so it does not exercise
the dimensions at all.  This instance is the first with **non-trivial SYT dimensions**: the five
partitions of `4` are `[4],[3,1],[2,2],[2,1,1],[1,1,1,1]` with `dim = 1,3,2,3,1`, and crucially
`dim := dimHLF` is the **actual Frame–Robinson–Thrall hook-length dimension** (not a hand-supplied
constant).  Both standard axioms then check against real partition combinatorics by `decide`:

* **(i)** `Σ dim² = 1+9+4+9+1 = 24 = 4!` (`sum_dim_sq`); and
* **(ii)** `2·Σ dim²·Σc² = 2·144 = 288 = 4·3·4!` (`two_sum_dim_sq_content`), the cleared
  content-square Plancherel mean — the per-partition `Σc²` being `14,6,2,6,14`.

So the conditional Identity I (`two_sum_dim_sq_hooks`, `twoM_eq_plancherel_hook_sum`) is
non-degenerate over a model where the dimensions are the genuine `dimHLF` values and the two
axioms are not vacuously `dim ≡ 1` arithmetic — it is the same `dimHLF`/`sumSqContents`
combinatorics that `idB_verified_le12` / `dim_validated_le12` verify across all `n ≤ 12`.

(Both non-vacuity witnesses are subsumed as of 2026-08-23: `plancherelSnDataGeneral` is a model at
every `n`, so conditional-on-`False` is ruled out without exhibiting a small case. They are kept —
they are cheap, and a `decide` against the actual partition combinatorics is an independent check
on the general construction rather than a consequence of it.) -/
instance plancherelSnData_four : PlancherelSnData 4 where
  parts := {[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]}
  parts_sorted := by decide
  parts_sz := by decide
  dim := dimHLF
  sum_dim_sq := by decide
  two_sum_dim_sq_content := by decide


end QOU.BraidKnot.IdentityI
