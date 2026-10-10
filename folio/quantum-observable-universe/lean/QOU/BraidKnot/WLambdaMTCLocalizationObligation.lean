import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic
import QOU.BraidKnot.KeystoneC2QDimTranspose

/-!
# W_λ keystone, residual (i): the MTC-matching obligation as a `§3b-cond` class

The s5-so3 keystone reduces the lever-1 binding kernel `R(q,x) = x² − τx + 1` to a single
geometric trace `τ = tr B`, whose geometric face is the **`W_λ` index** — the Beasley–Witten /
Reshetikhin–Turaev localization weight on the Hecke partition blocks. **Residual (i)** (the single
owner-gated open object, opened 2026-06-29) is:

> pin the Beasley–Witten gauge datum on `S³/2I` to the Hecke `Rep U_q(sl_N)` blocks so the
> localization `W_λ = d_q²/D²` is provably **our** Hecke category's Plancherel measure, not
> "some MTC's".

This file does **not** construct that gauge datum (that is the deep, owner-gated differential
geometry — the Chern–Simons group + level on the Poincaré sphere whose equivariant index produces
exactly the Hecke q-dimensions `d_q(λ)`). It does the **formalize-first** complement: it states the
matching as a single named hypothesis and *derives* the keystone's two necessary conditions from it,
turning "pin the gauge datum" from prose into a precise, auditable Lean obligation.

The class (`BeasleyWittenLocalization`) carries, as its only unproved field, the **matching
obligation** `loc p = d_q(p)² / D²` — what the gauge datum must deliver. Everything else is a
*derived consequence*, so the theorems are non-degenerate (AGENTS.md §3b-cond / §3b-tax — the class
axiomatises the input, the theorems derive the conclusions and never assume them):

* **C1 — normalization** (`loc_isProbabilityMeasure`): any localization matching `d_q²/D²` is a
  probability measure, `Σ_λ loc λ = 1`. (`D²` cancels by construction — this is the C1
  normalization the 2026-06-20 audit pinned: the genuine Plancherel `D² = Σ d_q²` normaliser, not
  `[n]_q!`.)
* **C2 — chirality-blindness** (`loc_conj_eq`): any such localization is transpose-invariant,
  `loc λ′ = loc λ`. This transports the corpus-**proved** categorical fact
  `qDim_conj` / `qPlancherelWeight_conj`
  ([`KeystoneC2QDimTranspose.lean`](KeystoneC2QDimTranspose.lean), sorry-free) onto the
  gauge-theory weight `loc` *via the matching*.

So C1 + C2 are **necessary conditions any gauge datum must satisfy** — a falsifiable constraint on
residual (i)'s owner-gated search (a localization whose weight is not normalized, or not
transpose-invariant, cannot be the Hecke Plancherel measure). Two of these (C2 here; the `W_λ`
defect cubic `144·C(n) = −n(n−1)(2n−13)` in
[`WLambdaDefectClosedForm.lean`](WLambdaDefectClosedForm.lean)) are already Lean-proved, so they are
genuine consistency obligations, not vacuous.

**Base ring.** Generic `{R : Type*} [Field R]` (§7c): the measure identity `d_q²/D²` and both
necessary conditions are pure field algebra — no ordering, no `Real.sqrt`, no `q₀`. The
archimedean specialisation (`R := ℝ`, evaluating `d_q` at the substrate `q₀`) lives downstream and
is not needed for the obligation. No fit; the geometric side must *derive* the algebraically-fixed
`τ`, never tune to it.

The class field `qDim_conj` is an **input** (a property of `d_q`), not the conclusion `loc_conj_eq`.
For the **genuine** Hecke q-dimension it is realized by the corpus-proved
`QOU.BraidKnot.IdentityI.qDim_conj` (`KeystoneC2QDimTranspose.lean`, sorry-free) — see
`heckeLocalization` below, which builds a `BeasleyWittenLocalization ℝ` on the real `qDim`,
discharging this field from that theorem rather than carrying it abstractly.
-/

open Finset

namespace QOU.BraidKnot.Keystone

/-- **Residual (i): the Beasley–Witten / RT localization, matched to the Hecke Plancherel measure.**

Carries the Hecke partition blocks `parts` for `λ ⊢ n`, the transpose involution `conj`
(`λ ↦ λ′`), the categorical q-dimension `qDim = d_q`, and — as its single unproved field — the
**MTC-matching obligation** `loc_matches`: the gauge-theory localization weight `loc` equals the
categorical Plancherel measure `d_q(λ)² / D²`, `D² = Σ_λ d_q(λ)²`. This is exactly what the
owner-gated gauge datum on `S³/2I` must deliver; it is **not** constructed here.

The two structural inputs `conj_mem` (blocks closed under transpose) and `qDim_conj` (the
corpus-proved `d_q(λ′) = d_q(λ)`) are established facts, not the conclusions; `globalDim_ne` is
`D² ≠ 0`. -/
class BeasleyWittenLocalization (R : Type*) [Field R] where
  /-- Partition index for `λ ⊢ n`. -/
  Part : Type*
  /-- The finite set of Hecke partition blocks `λ ⊢ n`. -/
  parts : Finset Part
  /-- The transpose involution `λ ↦ λ′`. -/
  conj : Part → Part
  /-- The blocks are closed under transpose (`λ ⊢ n ⇒ λ′ ⊢ n`). -/
  conj_mem : ∀ p ∈ parts, conj p ∈ parts
  /-- The categorical q-dimension `d_q(λ)` of the Hecke block. -/
  qDim : Part → R
  /-- **Corpus-proved input** `d_q(λ′) = d_q(λ)` (`KeystoneC2QDimTranspose.qDim_conj`,
  sorry-free) — carried abstractly here (Mathlib-only module). -/
  qDim_conj : ∀ p ∈ parts, qDim (conj p) = qDim p
  /-- The global quantum dimension `D² = Σ_λ d_q(λ)²` is nonzero. -/
  globalDim_ne : (∑ p ∈ parts, qDim p ^ 2) ≠ 0
  /-- The Beasley–Witten / RT localization weight on the blocks (the gauge-theory side). -/
  loc : Part → R
  /-- **THE MTC-MATCHING OBLIGATION (residual i).** The localization equals our category's
  Plancherel measure `d_q(λ)² / D²`. The single unproved field — what the owner-gated gauge datum
  must deliver. -/
  loc_matches : ∀ p ∈ parts, loc p = qDim p ^ 2 / (∑ m ∈ parts, qDim m ^ 2)

variable {R : Type*} [Field R] [h : BeasleyWittenLocalization R]

/-- **C1 — normalization (derived).** Any localization matching `d_q²/D²` is a probability measure:
`Σ_λ loc λ = 1`. The `D²` cancels by construction (`Finset.sum_div` + `div_self globalDim_ne`).
This is the keystone's C1 normalization — the genuine Plancherel `D² = Σ d_q²` normaliser forces
`Σ = 1` (unlike `[n]_q!`). Derived from `loc_matches`, not assumed. -/
theorem loc_isProbabilityMeasure : (∑ p ∈ h.parts, h.loc p) = 1 := by
  rw [Finset.sum_congr rfl h.loc_matches]
  simp only [div_eq_mul_inv]
  rw [← Finset.sum_mul, mul_inv_cancel₀ h.globalDim_ne]

/-- **C2 — chirality-blindness (derived).** Any localization matching `d_q²/D²` is
transpose-invariant: `loc λ′ = loc λ`. Transports the corpus-proved `qDim_conj`
(`d_q(λ′)=d_q(λ)`) onto `loc` via the matching. The keystone necessary condition C2 for the
gauge-theory weight — derived, not assumed. -/
theorem loc_conj_eq (p : h.Part) (hp : p ∈ h.parts) : h.loc (h.conj p) = h.loc p := by
  rw [h.loc_matches (h.conj p) (h.conj_mem p hp), h.loc_matches p hp, h.qDim_conj p hp]

end QOU.BraidKnot.Keystone

namespace QOU.BraidKnot.Keystone.Example

/-- **Non-vacuity witness — `BeasleyWittenLocalization ℚ` is inhabited (`n = 2`).** The partitions
of `2` are `[2]` (trivial) and `[1,1]` (sign), both of q-dimension `d_q = 1` at any `q` (the
one-cell hook products cancel), so `D² = 2`, the Plancherel measure is `loc ≡ 1/2`, and transpose
swaps the two blocks. Both class fields check by `decide` / `norm_num`. This confirms the
conditional theorems above are **not** conditional-on-`False`: there is a genuine model where the
matching holds against the actual `n=2` block combinatorics. (Stronger `n=4` and `n=5` witnesses
with the genuine non-trivial `d_q` values — the physical electron/muon blocks — are supplied in
[`KeystoneWLambdaPhysicalBlocks.lean`](KeystoneWLambdaPhysicalBlocks.lean).) -/
instance localization_two : BeasleyWittenLocalization ℚ where
  Part := Bool
  parts := {false, true}
  conj := not
  conj_mem := by decide
  qDim := fun _ => 1
  qDim_conj := fun _ _ => rfl
  globalDim_ne := by
    rw [Finset.sum_pair (by decide : (false : Bool) ≠ true)]; norm_num
  loc := fun _ => 1 / 2
  loc_matches := by
    intro p _
    rw [Finset.sum_pair (by decide : (false : Bool) ≠ true)]; norm_num

end QOU.BraidKnot.Keystone.Example

namespace QOU.BraidKnot.Keystone

open QOU.MathlibExt.QPartitionCombinatorics QOU.BraidKnot.IdentityI

/-- **Real Hecke q-Plancherel wire-up (removes the abstract `qDim_conj`).**

Builds a `BeasleyWittenLocalization ℝ` from the **genuine** Hecke q-dimension
`qDim` ([`QPartitionCombinatorics.qDim`](../MathlibExt/QPartitionCombinatorics.lean),
`d_q(λ) = [n]_q! / ∏_c [h_c]_q`) on any conjugate-closed set of sorted partitions `P` with
`D² = Σ_λ d_q(λ)² ≠ 0`. The `loc` IS the categorical Plancherel measure `d_q²/D²` (so `loc_matches`
is `rfl`), and — the point of the strengthening — the `qDim_conj` field is discharged by the
**corpus-proved** `QOU.BraidKnot.IdentityI.qDim_conj`
([`KeystoneC2QDimTranspose.lean`](KeystoneC2QDimTranspose.lean), sorry-free), **not** carried
abstractly. So `loc_isProbabilityMeasure` (C1) and `loc_conj_eq` (C2) hold for the *actual* Hecke
Plancherel measure of the blocks `P`, modulo only the structural inputs (conj-closure, `D² ≠ 0`).

`D² ≠ 0` is the sole remaining hypothesis. It does **not** depend on any Wedderburn sum identity:
`D² = Σ_λ d_q²` is its own q-polynomial and is **not** `[n]_q!` (the claim
`Σ d_q² = [n]_q!` is false at generic q — see
[`docs/audits/2026-06-29-wedderburn-trace-identity-false-at-generic-q.md`](../../../../../docs/audits/2026-06-29-wedderburn-trace-identity-false-at-generic-q.md)).
For `1 < q` it is discharged directly from positivity (`qBracket_pos`/`qFactorial_pos` ⇒
`d_q > 0` ⇒ `Σ d_q² > 0`) — a clean follow-up; carried as a hypothesis here. -/
noncomputable def heckeLocalization
    (q : ℝ) (P : Finset (List ℕ))
    (hsorted : ∀ l ∈ P, l.Sorted (· ≥ ·))
    (hconj : ∀ l ∈ P, Partition.conjugate l ∈ P)
    (hD : (∑ m ∈ P, qDim q m ^ 2) ≠ 0) :
    BeasleyWittenLocalization ℝ where
  Part := List ℕ
  parts := P
  conj := Partition.conjugate
  conj_mem := hconj
  qDim := qDim q
  qDim_conj := fun p hp => qDim_conj q p (hsorted p hp)
  globalDim_ne := hD
  loc := fun p => qDim q p ^ 2 / (∑ m ∈ P, qDim q m ^ 2)
  loc_matches := fun _ _ => rfl

/-! ## Discharging `D² ≠ 0` from positivity (no Wedderburn identity needed) -/

/-- Multiplicative `foldl` over positive factors is positive. -/
private theorem foldl_mul_pos {α : Type*} (g : α → ℝ) (L : List α)
    (h : ∀ x ∈ L, 0 < g x) : 0 < L.foldl (fun a x => a * g x) 1 := by
  have aux : ∀ (M : List α) (acc : ℝ), 0 < acc → (∀ x ∈ M, 0 < g x) →
      0 < M.foldl (fun a x => a * g x) acc := by
    intro M
    induction M with
    | nil => intro acc hacc _; simpa using hacc
    | cons x xs ih =>
      intro acc hacc hm
      simp only [List.foldl_cons]
      exact ih (acc * g x) (mul_pos hacc (hm x (by simp)))
        (fun y hy => hm y (List.mem_cons_of_mem _ hy))
  exact aux L 1 one_pos h

/-- A genuine cell's hook length is at least `1`. -/
private theorem one_le_hookLength {lam : List ℕ} {i j : ℕ}
    (hj : j < (lam[i]?).getD 0) : 1 ≤ Partition.hookLength lam i j := by
  unfold Partition.hookLength
  cases hgi : lam[i]? with
  | none => rw [hgi, Option.getD_none] at hj; exact absurd hj (Nat.not_lt_zero j)
  | some row_i =>
    rw [hgi, Option.getD_some] at hj
    simp only [hj, if_true]
    omega

/-- **`d_q(λ) > 0` for `q > 1`** — the genuine Hecke q-dimension is positive in the substrate
regime. Numerator `[n]_q! > 0` (`qFactorial_pos`); the denominator is a product of
`qBracket q h > 0` over genuine cells (`qBracket_pos`, hooks `≥ 1`). -/
theorem qDim_pos {q : ℝ} (hq : 1 < q) (lam : List ℕ) : 0 < qDim q lam := by
  unfold qDim
  apply div_pos (qFactorial_pos hq _)
  apply foldl_mul_pos
  intro i _
  apply foldl_mul_pos
  intro j hj
  exact qBracket_pos hq (one_le_hookLength (List.mem_range.mp hj))

/-- **`D² = Σ_λ d_q(λ)² > 0`** on a nonempty block set for `q > 1` — so `globalDim_ne` holds
directly from positivity, **without** the (false) `Σ d_q² = [n]_q!` identity. -/
theorem sum_qDimSq_pos {q : ℝ} (hq : 1 < q) {P : Finset (List ℕ)} (hP : P.Nonempty) :
    0 < ∑ m ∈ P, qDim q m ^ 2 := by
  obtain ⟨m, hm⟩ := hP
  exact Finset.sum_pos' (fun i _ => sq_nonneg _) ⟨m, hm, pow_pos (qDim_pos hq m) 2⟩

/-- **`heckeLocalization` with `D² ≠ 0` discharged from positivity** (`q > 1`, `P` nonempty) —
the last structural input is now *derived*, not assumed. -/
noncomputable def heckeLocalizationOfPos
    (q : ℝ) (hq : 1 < q) (P : Finset (List ℕ))
    (hsorted : ∀ l ∈ P, l.Sorted (· ≥ ·))
    (hconj : ∀ l ∈ P, Partition.conjugate l ∈ P)
    (hP : P.Nonempty) :
    BeasleyWittenLocalization ℝ :=
  heckeLocalization q P hsorted hconj (ne_of_gt (sum_qDimSq_pos hq hP))

/-! ## C6 — full support (derived): every block carries strictly positive Plancherel weight

A necessary condition the keystone's `W_λ` index must satisfy, and the colour-arena lever against
a finite-`N` Sasakian (`ColourArenaBlockCount.lean`, #2605): the genuine Hecke Plancherel measure
`d_q²/D²` is **strictly positive on every block** for `q > 1` — no Wedderburn block is dropped. This
is *derived* from `qDim_pos` (no fit, no extra hypothesis), so any gauge datum claiming to realize
the localization must reproduce full support; a measure that zeroed a block could not match. -/

/-- **C6 — full support (derived).** For `q > 1` every block of the real Hecke localization carries
strictly positive Plancherel weight: `loc p = d_q(p)²/D² > 0`. -/
theorem heckeLocalizationOfPos_loc_pos
    (q : ℝ) (hq : 1 < q) (P : Finset (List ℕ))
    (hsorted : ∀ l ∈ P, l.Sorted (· ≥ ·))
    (hconj : ∀ l ∈ P, Partition.conjugate l ∈ P)
    (hP : P.Nonempty) (p : List ℕ) :
    0 < (heckeLocalizationOfPos q hq P hsorted hconj hP).loc p := by
  show 0 < qDim q p ^ 2 / (∑ m ∈ P, qDim q m ^ 2)
  exact div_pos (pow_pos (qDim_pos hq p) 2) (sum_qDimSq_pos hq hP)

/-- **C6 strengthened — the support is *all* of `P`.** The set of blocks with nonzero Plancherel
weight is exactly the full block set: no block is dropped (`full support`, the no-finite-`N`-Sasakian
necessary condition). -/
theorem heckeLocalizationOfPos_full_support
    (q : ℝ) (hq : 1 < q) (P : Finset (List ℕ))
    (hsorted : ∀ l ∈ P, l.Sorted (· ≥ ·))
    (hconj : ∀ l ∈ P, Partition.conjugate l ∈ P)
    (hP : P.Nonempty) :
    P.filter (fun p => (heckeLocalizationOfPos q hq P hsorted hconj hP).loc p ≠ 0) = P := by
  apply Finset.filter_true_of_mem
  intro p _
  exact ne_of_gt (heckeLocalizationOfPos_loc_pos q hq P hsorted hconj hP p)

end QOU.BraidKnot.Keystone
