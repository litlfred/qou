/-
# The all-`n` Temperley–Lieb weight-vanishing lemma

`y_λ = 0 ⟺ λ has ≥ 3 rows`, at the convention-D Markov parameter
`z_D = q³/(q²+1)`.

This is the statement PR #5207 named as the step that upgrades the
Temperley–Lieb identification from **measured** (`radical = ⟨E⁽³⁾⟩` as ideals
at `n = 3, 4, 5, 6`, coranks `1, 10, 78, 588 = n! − Catalan(n)`) to **proved
for all `n`**.

## What is proved here, and what is cited

The argument has two halves, and only the first is an external input.

* **Cited** — Wenzl's theorem that the Ocneanu/Markov trace weights on `H_n(Q)` at Markov
  parameter `z_W = Q^r(1−Q)/(1−Q^r)` are the principal specialisations
  `s_λ(1, Q, …, Q^{r−1})`, normalised so that `Σ_λ f^λ y_λ = tr(1) = 1`.  See `-- Ref:` on
  `schurPrincipal`.  It is no longer an external input: it is proved in
  `SchurWeyl.WenzlMarkovTraceInstance` and `SchurWeyl.JimboGLWeyl` (section *The weights
  themselves* below).  The class `IsOcneanuWeightSystem` that carried it as a hypothesis was
  deleted on 2026-11-15 (bean `qou-gld2`).

* **Proved here, sorry-free, for all `n` and all `λ`** — everything else:

  1. `wenzlLevel_conventionD` : convention D *is* Wenzl level `r = 2`. The
     level is recovered from the Markov parameter by
     `Q^r = q·z/(1 − Q + q·z)`; at `z = z_D` and `Q = q²` this is `q⁴ = Q²`.
     An algebraic identity, so it is proved rather than cited.
  2. `schurPrincipal_eq_zero_iff` : the level-`r` principal specialisation
     vanishes **iff** `λ` has more than `r` rows. General `r`, general `λ`.
  3. `conventionD_weight_eq_zero_iff` / `conventionD_weight_eq_zero_iff_rowLens`
     : the `r = 2` corollary — `y_λ = 0 ⟺ λ has ≥ 3 rows` — at the level of
     the normalised weight.

The mechanism is a single cell. The numerator of the hook-content product
carries a factor `1 − Q^{r + c(x)}` per cell `x`, and `r + c(x) = 0` exactly
when `c(x) = −r`. A cell of content `−r` is `(r, 0)` — the first cell of row
`r + 1` — and a Young diagram contains it precisely when it has more than `r`
rows. At `r = 2` that cell is `(2, 0)`, of content `−2`, and "more than 2
rows" is "at least 3 rows": the Temperley–Lieb row cap.

## Cross-check

`computations/probes/wenzl_level_two_vanishing.py` verifies, exactly over
`ℚ(q)`, that the formula stated here reproduces PR #5185's `n = 3` triple
`(q⁴+1)/(q²+1)²`, `q²/(q²+1)²`, `0`; the two-row closed form
`TemperleyLiebTower.yw = [n−2k+1]_q/[2]_q^n` for all `λ` at `n = 2 … 7`; the
vanishing set for `n = 1 … 8`; and PR #5207's coranks `1, 10, 78, 588`.

## Base ring

Generic `[Field R]` throughout — no ordering, no `ℝ`, no archimedean
construct (AGENTS.md §7c). The only hypothesis on `Q` is that it is not a
root of unity, which is exactly the genericity under which the Hecke algebra
is semisimple and the weights are defined.
-/
import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Algebra.BigOperators.Group.Finset.Defs
import Mathlib.Algebra.BigOperators.GroupWithZero.Finset
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.GroupWithZero.Unbundled.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Algebra.GroupWithZero.Units.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination

namespace QOU.QBeta.WenzlWeight

open Finset

/-! ## Cell statistics -/

/-- The **content** of a cell, `c(i, j) = j − i`, as an integer (cells are
0-indexed, matching `YoungDiagram`). Contents in the first column are
`0, −1, −2, …`, so a cell of content `−r` exists exactly when the diagram has
more than `r` rows — the fact the whole file turns on. -/
def content (x : ℕ × ℕ) : ℤ := (x.2 : ℤ) - (x.1 : ℤ)

/-- The **hook length** `h(i, j) = arm + leg + 1` of a cell of `μ`. Matches
`computations/markov/markov_weights_symbolic.hooks_and_contents`. -/
def hook (μ : YoungDiagram) (x : ℕ × ℕ) : ℕ :=
  (μ.rowLen x.1 - x.2) + (μ.colLen x.2 - x.1) - 1

/-- `n(λ) = Σ_i (i−1)·λ_i`, i.e. the sum of the 0-indexed row indices over the
cells. Matches `markov_weights_symbolic.n_partition`. -/
def nPart (μ : YoungDiagram) : ℕ := ∑ x ∈ μ.cells, x.1

/-- Every cell of a diagram has hook length at least `1`: its arm and its leg
are each at least `0`, and the `+1` counts the cell itself. -/
theorem one_le_hook {μ : YoungDiagram} {x : ℕ × ℕ} (hx : x ∈ μ.cells) :
    1 ≤ hook μ x := by
  have hx' : (x.1, x.2) ∈ μ := by simpa using (YoungDiagram.mem_cells x).mp hx
  have hrow : x.2 < μ.rowLen x.1 := YoungDiagram.mem_iff_lt_rowLen.mp hx'
  have hcol : x.1 < μ.colLen x.2 := YoungDiagram.mem_iff_lt_colLen.mp hx'
  unfold hook
  omega

/-! ## The Wenzl hook–content weight -/

variable {R : Type*} [Field R]

/-- The **level-`r` principal specialisation** of the Schur function, in the
hook-content product form used throughout the corpus:

`s_λ(1, Q, …, Q^{r−1}) = Q^{n(λ)} · ∏_{x ∈ λ} (1 − Q^{r + c(x)}) / (1 − Q^{h(x)})`

This is `markov_weights_symbolic.schur_principal_symbolic` and
`schur_principal_mpmath._schur_principal_with`, transcribed verbatim.

Wenzl's theorem — the external input, and the only one — is that these *are*
the Ocneanu/Markov trace weights on `H_n(Q)` at Markov parameter
`z_W = Q^r(1−Q)/(1−Q^r)`, up to the normalisation `Σ_λ f^λ y_λ = 1`.
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
   Wenzl, "Hecke algebras of type $A_n$ and subfactors", Invent. Math. 92
   (1988) 349–383 — the source of the weight formula.
-- Ref: [orellana1998] https://arxiv.org/abs/math/9806163
   Orellana, "Weights of Markov Traces on Hecke Algebras", p. 17, restates
   Wenzl's type-A result in exactly this form: *"In [W1] Wenzl showed that
   the weights of the Markov trace (with parameter `z = q^r(1−q)/(1−q^r)`)
   on the Hecke algebra of type A are given by the symmetric Schur functions
   `s_{λ,r}(q)`."* **Caution:** Orellana's "type D" is the *Coxeter* type
   `D_n` and has nothing to do with this repo's trace convention D. Only the
   type-A statement above is used. -/
noncomputable def schurPrincipal (r : ℕ) (Q : R) (μ : YoungDiagram) : R :=
  Q ^ nPart μ * ∏ x ∈ μ.cells, (1 - Q ^ ((r : ℤ) + content x)) / (1 - Q ^ hook μ x)

/-- **Convention D is Wenzl level `r = 2`.**

Wenzl's parameter relation `z_W = Q^r(1−Q)/(1−Q^r)` inverts to
`Q^r = z_W/(1 − Q + z_W)`. Convention D sits at `Q = q²` and `z_W = q·z_D`
(the factor `q` is the Hecke-normalisation shift between
`g² = (Q−1)g + Q` and `σ² = (q − q⁻¹)σ + 1`, under which `σ = g/q` and
`Q = q²`). Substituting `z_D = q³/(q²+1)` gives `Q^r = q⁴ = Q²`, so `r = 2`
on the nose — the SU(2) level, whose row cap is the Temperley–Lieb one.

Not cited: this is an algebraic identity in `q`, so it is proved. -/
theorem wenzlLevel_conventionD (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    q * (q ^ 3 / (q ^ 2 + 1)) / (1 - q ^ 2 + q * (q ^ 3 / (q ^ 2 + 1)))
      = (q ^ 2) ^ 2 := by
  have hden : 1 - q ^ 2 + q * (q ^ 3 / (q ^ 2 + 1)) = 1 / (q ^ 2 + 1) := by
    field_simp
    ring
  rw [hden]
  field_simp

/-! ## The vanishing criterion -/

/-- A cell of `μ` of content `−r` forces `μ` to contain `(r, 0)`, hence to have
more than `r` rows. -/
theorem colLen_gt_of_content_eq_neg {μ : YoungDiagram} {x : ℕ × ℕ} {r : ℕ}
    (hx : x ∈ μ.cells) (hc : (r : ℤ) + content x = 0) : r < μ.colLen 0 := by
  have hx' : (x.1, x.2) ∈ μ := by simpa using (YoungDiagram.mem_cells x).mp hx
  have hxr : x.1 = x.2 + r := by
    unfold content at hc
    omega
  have : (r, 0) ∈ μ := μ.up_left_mem (by omega) (Nat.zero_le _) hx'
  exact YoungDiagram.mem_iff_lt_colLen.mp this

/-- **The vanishing criterion, for every `n`, every `λ` and every level `r`.**

The level-`r` principal specialisation vanishes exactly when `λ` has more than
`r` rows:

`s_λ(1, Q, …, Q^{r−1}) = 0 ⟺ ℓ(λ) > r`.

`Q` is assumed not to be a root of unity — precisely the genericity under
which `H_n(Q)` is semisimple and the weights are defined. Without it the
statement is false, so the hypothesis is doing real work rather than
decorating the signature: at a root of unity a *hook length* can also kill a
denominator and further numerator factors can vanish off content `−r`. -/
theorem schurPrincipal_eq_zero_iff {Q : R} (hQ0 : Q ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (r : ℕ) (μ : YoungDiagram) :
    schurPrincipal r Q μ = 0 ↔ r < μ.colLen 0 := by
  have hpow : (Q : R) ^ nPart μ ≠ 0 := pow_ne_zero _ hQ0
  -- denominators never vanish: hook lengths are ≥ 1 and `Q` is not a root of unity
  have hden : ∀ x ∈ μ.cells, (1 : R) - Q ^ hook μ x ≠ 0 := by
    intro x hx hcon
    have h1 : (Q : R) ^ hook μ x = 1 := (sub_eq_zero.mp hcon).symm
    have h1' : (Q : R) ^ ((hook μ x : ℤ)) = 1 := by
      rw [zpow_natCast]; exact h1
    exact hQ _ (by have := one_le_hook hx; omega) h1'
  constructor
  · -- a vanishing product exhibits a cell of content `−r`
    intro h
    rw [schurPrincipal, mul_eq_zero] at h
    rcases h with h | h
    · exact absurd h hpow
    rw [Finset.prod_eq_zero_iff] at h
    obtain ⟨x, hx, hfac⟩ := h
    rcases div_eq_zero_iff.mp hfac with hnum | hbad
    · have hone : (Q : R) ^ ((r : ℤ) + content x) = 1 := by
        exact (sub_eq_zero.mp hnum).symm
      by_contra hlt
      exact hlt (colLen_gt_of_content_eq_neg hx
        (by by_contra hk; exact hQ _ hk hone))
    · exact absurd hbad (hden x hx)
  · -- more than `r` rows ⇒ the cell `(r, 0)` is present, and it kills the product
    intro h
    have hmem : (r, 0) ∈ μ := YoungDiagram.mem_iff_lt_colLen.mpr h
    have hcell : ((r, 0) : ℕ × ℕ) ∈ μ.cells := (YoungDiagram.mem_cells _).mpr hmem
    rw [schurPrincipal]
    refine mul_eq_zero_of_right _ (Finset.prod_eq_zero hcell ?_)
    have : ((r : ℤ) + content ((r, 0) : ℕ × ℕ)) = 0 := by unfold content; simp
    rw [this]
    simp

/-! ## The Temperley–Lieb corollary -/

/-- **The all-`n` Temperley–Lieb weight-vanishing lemma, at the level of the
formula.**

At convention D — equivalently, by `wenzlLevel_conventionD`, at Wenzl level
`r = 2` — the normalised level-2 principal specialisation of `λ` vanishes
**iff** `λ` has at least three rows. `Z` is the normaliser `Σ_μ f^μ s_μ`
enforcing `Σ_λ f^λ y_λ = tr(1) = 1`; only its non-vanishing is used, so the
statement is independent of which normalisation convention is in force.

**Unconditional, and about `schurPrincipal` — not about the Ocneanu weight.**
This says nothing about the Markov trace on `H_n(Q)`; it is a fact about the
hook-content product. The corresponding statement about the actual weight is
`SchurWeyl.ocneanuWeight_conventionD_eq_zero_iff`, unconditional (see *The weights
themselves* below).

This is the statement PR #5207 named. It holds for every `n` and every `λ`,
and it is the reason `radical = ⟨E⁽³⁾⟩`: the blocks the trace annihilates are
exactly the `≥ 3`-row ones, whose dimensions sum to `n! − Catalan(n)`. -/
theorem conventionD_weight_eq_zero_iff {Q Z : R} (hQ0 : Q ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hZ : Z ≠ 0) (μ : YoungDiagram) :
    schurPrincipal 2 Q μ / Z = 0 ↔ 2 < μ.colLen 0 := by
  rw [div_eq_zero_iff]
  simp only [hZ, or_false]
  exact schurPrincipal_eq_zero_iff hQ0 hQ 2 μ

/-- The same statement with "at least three rows" spelled as the length of the
row-length list, which is how `λ`'s number of rows is usually written. -/
theorem conventionD_weight_eq_zero_iff_rowLens {Q Z : R} (hQ0 : Q ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hZ : Z ≠ 0) (μ : YoungDiagram) :
    schurPrincipal 2 Q μ / Z = 0 ↔ 3 ≤ μ.rowLens.length := by
  rw [conventionD_weight_eq_zero_iff hQ0 hQ hZ, YoungDiagram.length_rowLens]
  omega

/-- The surviving side, stated positively: a diagram with at most two rows has
nonzero weight. This is the half that makes the criterion sharp — without it
"the `≥ 3`-row blocks die" would be compatible with everything dying. -/
theorem conventionD_weight_ne_zero_of_two_rows {Q Z : R} (hQ0 : Q ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hZ : Z ≠ 0) (μ : YoungDiagram)
    (h : μ.rowLens.length ≤ 2) : schurPrincipal 2 Q μ / Z ≠ 0 := by
  rw [Ne, conventionD_weight_eq_zero_iff_rowLens hQ0 hQ hZ]
  omega

/-! ## The hypothesis is satisfiable, and the criterion is not vacuous

An `iff` guarded by an unsatisfiable hypothesis proves nothing. The two
results below rule that out: the first exhibits a broad class of `Q` meeting
the root-of-unity hypothesis — including the substrate value `Q = q₀² ≈ 1.232`
— and the second evaluates the criterion on the smallest diagram that
discriminates, checking that it returns *different* answers on the two sides.
-/

/-- **The genericity hypothesis holds at every positive `Q ≠ 1`**, hence in
particular at the substrate `Q = q₀²` (`q₀ ≈ 1.10998`, so `Q ≈ 1.232`). This
is the archimedean instantiation: it lives after the substrate→archimedean
wall and is not used by any statement above it. -/
theorem not_root_of_unity_of_pos_ne_one {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] {Q : K} (hpos : 0 < Q) (hne : Q ≠ 1) :
    ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1 := by
  intro k hk hcon
  exact hk ((zpow_eq_one_iff_right₀ hpos.le hne).mp hcon)

/-- `(1,1,1)` — three rows — has `colLen 0 = 3`. -/
theorem colLen_ofRowLens_one_one_one :
    (YoungDiagram.ofRowLens [1, 1, 1] (by decide)).colLen 0 = 3 := by
  rw [← YoungDiagram.length_rowLens,
    YoungDiagram.rowLens_ofRowLens_eq_self (by decide)]
  rfl

/-- `(2,1)` — two rows — has `colLen 0 = 2`. -/
theorem colLen_ofRowLens_two_one :
    (YoungDiagram.ofRowLens [2, 1] (by decide)).colLen 0 = 2 := by
  rw [← YoungDiagram.length_rowLens,
    YoungDiagram.rowLens_ofRowLens_eq_self (by decide)]
  rfl

/-- **The criterion discriminates.** At `n = 3` over `ℚ` with `Q = 2`, the
three-row diagram `(1³)` has weight zero and the two-row diagram `(2,1)` does
not. These are the two blocks PR #5185 measured — `y₍₁³₎ = 0`,
`y₍₂,₁₎ = q²/(q²+1)² ≠ 0` — so the Lean returns the measured verdict on the
measured case, and it is not returning "zero" for everything. -/
theorem discriminates_at_n_three :
    schurPrincipal 2 (2 : ℚ) (YoungDiagram.ofRowLens [1, 1, 1] (by decide)) / 1 = 0
      ∧ schurPrincipal 2 (2 : ℚ) (YoungDiagram.ofRowLens [2, 1] (by decide)) / 1 ≠ 0 := by
  have hQ : ∀ k : ℤ, k ≠ 0 → (2 : ℚ) ^ k ≠ 1 :=
    not_root_of_unity_of_pos_ne_one (by norm_num) (by norm_num)
  constructor
  · rw [conventionD_weight_eq_zero_iff (by norm_num) hQ one_ne_zero,
      colLen_ofRowLens_one_one_one]
    norm_num
  · rw [Ne, conventionD_weight_eq_zero_iff (by norm_num) hQ one_ne_zero,
      colLen_ofRowLens_two_one]
    norm_num

/-! ## The weights themselves: proved, not assumed

This file once carried Wenzl (1988) as a hypothesis, the class `IsOcneanuWeightSystem Q z r y`,
asserting `y μ = schurPrincipal r Q μ / Z` for a **single** normaliser `Z`.  That class was deleted
on 2026-11-15 (owner ruling, bean `qou-gld2`), for two reasons:

* no per-size-normalised weight family could inhabit it, because the correct normaliser depends
  on the size `|μ|`;
* what it carried is now a theorem.  `SchurWeyl.wenzlMarkovTrace` is a Markov trace with weights
  `wenzlWeight r Q = schurPrincipal r Q / [r]_Q^{|μ|}`; `SchurWeyl.JimboGL.jimboTrace_eq_wenzl`
  realises it on `(K^r)^{⊗n}`; and `SchurWeyl.JimboGL.markov_tr_blockE` / `normaliser_eq` show that
  every Markov trace at Wenzl's level-`r` parameter has exactly these weights, with the
  normaliser `[r]_Q^n` forced.

The vanishing criterion for the actual weights is `SchurWeyl.wenzlWeight_eq_zero_iff` (any `r`)
and `SchurWeyl.ocneanuWeight_conventionD_eq_zero_iff` (convention D), both unconditional.
-/

/-! ### Recovering the level from the Markov parameter (unconditional) -/

/-- Wenzl's parameter relation, solved for `Q^r`: `Q^r(1 − Q + z) = z`.

Pure algebra — no hypothesis at all, not even `Q ≠ 0`. This is the inversion
`Q^r = z/(1 − Q + z)` quoted in the file header, in the form that avoids
dividing. -/
theorem pow_level_mul_eq_of_markovParameter {Q z : R} {r : ℕ}
    (h : z * (1 - Q ^ r) = Q ^ r * (1 - Q)) :
    Q ^ r * (1 - Q + z) = z := by linear_combination -h

/-- **`Q^r` is determined by the Markov parameter, and hence so is `r`.**

If two levels `r` and `s` sit at the same parameter `z` then `r = s`, for `Q`
not a root of unity. So "which Wenzl level is this trace at?" has at most one
answer — which is what lets `level_eq_two_of_conventionD` below turn convention
D's parameter into the *integer* 2 rather than merely into `Q^r = Q²`. -/
theorem level_unique_of_markovParameter {Q z : R} {r s : ℕ} (hQ0 : Q ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1)
    (hr : z * (1 - Q ^ r) = Q ^ r * (1 - Q))
    (hs : z * (1 - Q ^ s) = Q ^ s * (1 - Q)) : r = s := by
  have hQ1 : Q ≠ 1 := fun h => hQ 1 one_ne_zero (by rw [h]; simp)
  -- `1 − Q + z ≠ 0`: otherwise `z = Q − 1` and the relation collapses to `Q = 1`
  have hne : 1 - Q + z ≠ 0 := by
    intro hz0
    have hzv : z = Q - 1 := by linear_combination hz0
    subst hzv
    exact hQ1 (by linear_combination hr)
  have hpow : Q ^ r = Q ^ s :=
    mul_right_cancel₀ hne ((pow_level_mul_eq_of_markovParameter hr).trans
      (pow_level_mul_eq_of_markovParameter hs).symm)
  -- `Q^(r−s) = 1` in `ℤ`-exponents, so `r = s`
  have hz : Q ^ ((r : ℤ) - (s : ℤ)) = 1 := by
    rw [zpow_sub₀ hQ0, zpow_natCast, zpow_natCast, hpow]
    exact div_self (pow_ne_zero _ hQ0)
  by_contra hrs
  exact hQ _ (by omega) hz

/-- **Convention D pins the level to the integer `r = 2`.**

Given that a trace's Markov parameter is Wenzl's at level `r`, and that the
parameter is convention D's (`Q = q²`, `z = q·z_D`, the factor `q` being the
Hecke-normalisation shift of `wenzlLevel_conventionD`), the level *is* `2`.

Unconditional: this is `wenzlLevel_conventionD`'s algebra plus
`level_unique_of_markovParameter`. -/
theorem level_eq_two_of_conventionD {q z : R} {r : ℕ} (hq0 : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → (q ^ 2) ^ k ≠ 1)
    (hz : z = q * (q ^ 3 / (q ^ 2 + 1)))
    (h : z * (1 - (q ^ 2) ^ r) = (q ^ 2) ^ r * (1 - q ^ 2)) : r = 2 := by
  subst hz
  refine level_unique_of_markovParameter (pow_ne_zero 2 hq0) hQ h ?_
  field_simp
  ring

/-! ### Conjugate-pair survival at level 2: `n = 2` vs `n = 6` (`qou-8zjc`)

At `n = 2`, the two partitions `(2)` and `(1,1)` are conjugate to each other and
both have at most `2` rows, so both carry non-zero Wenzl level-2 weight.

At `n ≥ 5` (and specifically `n = 6` in the two-nucleon `H₆(q)` trace), any
two-row partition `r₀ + r₁ = n` with `r₁ ≤ r₀` satisfies `r₀ ≥ 3` by pigeonhole,
so its transpose has `colLen 0 = r₀ ≥ 3` rows and is annihilated at Wenzl level
`r = 2`. Thus **no conjugate pair survives at `n = 6`**: the four two-row
survivors `(6)`, `(5,1)`, `(4,2)`, `(3,3)` all have vanishing conjugate weights
`y_{(1⁶)} = y_{(2,1⁴)} = y_{(2,2,1,1)} = y_{(2,2,2)} = 0`. -/

/-- `(2)` — one row — has `colLen 0 = 1`. -/
theorem colLen_ofRowLens_two :
    (YoungDiagram.ofRowLens [2] (by decide)).colLen 0 = 1 := by
  rw [← YoungDiagram.length_rowLens,
    YoungDiagram.rowLens_ofRowLens_eq_self (by decide)]
  rfl

/-- `(1,1)` — two rows — has `colLen 0 = 2`. -/
theorem colLen_ofRowLens_one_one :
    (YoungDiagram.ofRowLens [1, 1] (by decide)).colLen 0 = 2 := by
  rw [← YoungDiagram.length_rowLens,
    YoungDiagram.rowLens_ofRowLens_eq_self (by decide)]
  rfl

/-- **At `n = 2`, both members of the conjugate pair `(2)` and `(1,1)` survive
Wenzl level 2 (`qou-8zjc`).** -/
theorem conjugate_pair_survives_at_n_two :
    schurPrincipal 2 (2 : ℚ) (YoungDiagram.ofRowLens [2] (by decide)) / 1 ≠ 0
      ∧ schurPrincipal 2 (2 : ℚ) (YoungDiagram.ofRowLens [1, 1] (by decide)) / 1 ≠ 0 := by
  have hQ : ∀ k : ℤ, k ≠ 0 → (2 : ℚ) ^ k ≠ 1 :=
    not_root_of_unity_of_pos_ne_one (by norm_num) (by norm_num)
  constructor
  · rw [Ne, conventionD_weight_eq_zero_iff (by norm_num) hQ one_ne_zero,
      colLen_ofRowLens_two]
    norm_num
  · rw [Ne, conventionD_weight_eq_zero_iff (by norm_num) hQ one_ne_zero,
      colLen_ofRowLens_one_one]
    norm_num

/-- **Pigeonhole on two-row partitions for `n ≥ 5` (`qou-8zjc`).**
Every two-row partition `r₀ + r₁ = n` (`r₁ ≤ r₀`) of `n ≥ 5` has first row
`r₀ ≥ 3`, so its conjugate has at least `3` rows. -/
theorem three_le_first_row_of_two_rows_of_five_le {r₀ r₁ n : ℕ}
    (hsum : r₀ + r₁ = n) (hord : r₁ ≤ r₀) (hn : 5 ≤ n) : 3 ≤ r₀ := by
  omega

/-- **General conjugate-annihilation lemma at level 2 (`qou-8zjc`).**
Whenever `μ.transpose` has at least `3` rows (`2 < μ.transpose.colLen 0`), its
convention-D weight vanishes, so `(μ, μ.transpose)` cannot survive as a live
conjugate pair. -/
theorem conjugate_weight_eq_zero_of_two_lt_colLen_transpose
    {Q Z : R} (hQ0 : Q ≠ 0) (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (hZ : Z ≠ 0)
    (μ : YoungDiagram) (ht : 2 < μ.transpose.colLen 0) :
    schurPrincipal 2 Q μ.transpose / Z = 0 :=
  (conventionD_weight_eq_zero_iff hQ0 hQ hZ μ.transpose).mpr ht

/-- `(3,3)` — the minimal-width two-row diagram at `n = 6` — has `colLen 0 = 2`. -/
theorem colLen_ofRowLens_three_three :
    (YoungDiagram.ofRowLens [3, 3] (by decide)).colLen 0 = 2 := by
  rw [← YoungDiagram.length_rowLens,
    YoungDiagram.rowLens_ofRowLens_eq_self (by decide)]
  rfl

/-- `(2,2,2)` — the conjugate of `(3,3)` at `n = 6` — has `colLen 0 = 3`. -/
theorem colLen_ofRowLens_two_two_two :
    (YoungDiagram.ofRowLens [2, 2, 2] (by decide)).colLen 0 = 3 := by
  rw [← YoungDiagram.length_rowLens,
    YoungDiagram.rowLens_ofRowLens_eq_self (by decide)]
  rfl

/-- **At `n = 6`, the rectangular two-row survivor `(3,3)` carries non-zero
weight while its conjugate `(2,2,2)` is annihilated (`qou-8zjc`).** -/
theorem n_six_three_three_survives_but_conjugate_dies :
    schurPrincipal 2 (2 : ℚ) (YoungDiagram.ofRowLens [3, 3] (by decide)) / 1 ≠ 0
      ∧ schurPrincipal 2 (2 : ℚ) (YoungDiagram.ofRowLens [2, 2, 2] (by decide)) / 1 = 0 := by
  have hQ : ∀ k : ℤ, k ≠ 0 → (2 : ℚ) ^ k ≠ 1 :=
    not_root_of_unity_of_pos_ne_one (by norm_num) (by norm_num)
  constructor
  · rw [Ne, conventionD_weight_eq_zero_iff (by norm_num) hQ one_ne_zero,
      colLen_ofRowLens_three_three]
    norm_num
  · rw [conventionD_weight_eq_zero_iff (by norm_num) hQ one_ne_zero,
      colLen_ofRowLens_two_two_two]
    norm_num

/-! ### The third live `z` spelling `1/[2]_q = q/(q²+1)` sits at no Wenzl level (`qou-niah`)

In Hecke-shifted Wenzl coordinates (`Q = q²`, `z_W = q · z`), the spelling
`z = q/(q²+1)` becomes `z_W = q²/(q²+1) = Q/(Q+1)`. Substituting `z_W(Q+1) = Q`
into Wenzl's parameter relation `z_W(1 − Q^r) = Q^r(1 − Q)` forces the golden
polynomial constraint `Q^r(1 + Q − Q²) = Q`. That relation fails at `r = 1` and
`r = 2` for every generic `Q`, and fails for **every** `r : ℕ` whenever
`1 + Q < Q²` (e.g. `Q = 2`), certifying that `q/(q²+1)` sits at no integer
Wenzl level in `ℚ(q)`. -/

/-- **Golden constraint forced by `z_W = Q/(Q+1)` (`qou-niah`).**
If `z * (Q + 1) = Q` and `z` satisfies Wenzl's level-`r` relation
`z * (1 - Q^r) = Q^r * (1 - Q)`, then `Q^r * (1 + Q - Q^2) = Q`. -/
theorem pow_level_mul_golden_of_inv_two_bracket {Q z : R} {r : ℕ}
    (hz : z * (Q + 1) = Q)
    (h : z * (1 - Q ^ r) = Q ^ r * (1 - Q)) :
    Q ^ r * (1 + Q - Q ^ 2) = Q := by
  have hstep : Q ^ r * (1 + Q - Q ^ 2) - Q =
      (Q + 1) * (Q ^ r * (1 - Q) - z * (1 - Q ^ r))
        + (1 - Q ^ r) * (z * (Q + 1) - Q) := by ring
  have h1 : Q ^ r * (1 - Q) - z * (1 - Q ^ r) = 0 := by linear_combination -h
  have h2 : z * (Q + 1) - Q = 0 := by linear_combination hz
  linear_combination hstep + (Q + 1) * h1 + (1 - Q ^ r) * h2

/-- **The `1/[2]_q` spelling is not at Wenzl level `r = 1` (`qou-niah`).** -/
theorem inv_two_bracket_not_wenzl_level_one {Q z : R}
    (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1) (hz : z * (Q + 1) = Q) :
    z * (1 - Q ^ 1) ≠ Q ^ 1 * (1 - Q) := by
  intro h
  have hgold := pow_level_mul_golden_of_inv_two_bracket hz h
  have hfac : Q * (Q - 1) * Q = 0 := by
    calc Q * (Q - 1) * Q = Q - Q ^ 1 * (1 + Q - Q ^ 2) := by ring
      _ = 0 := by linear_combination -hgold
  rcases mul_eq_zero.mp hfac with h12 | h3
  · rcases mul_eq_zero.mp h12 with h1 | h2
    · exact hQ0 h1
    · exact hQ1 (sub_eq_zero.mp h2)
  · exact hQ0 h3

/-- **The `1/[2]_q` spelling is not at Wenzl level `r = 2` (`qou-niah`).** -/
theorem inv_two_bracket_not_wenzl_level_two {Q z : R}
    (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1) (hQm1 : Q + 1 ≠ 0) (hz : z * (Q + 1) = Q) :
    z * (1 - Q ^ 2) ≠ Q ^ 2 * (1 - Q) := by
  intro h
  have hgold := pow_level_mul_golden_of_inv_two_bracket hz h
  have hfac : Q * (Q - 1) ^ 2 * (Q + 1) = 0 := by
    calc Q * (Q - 1) ^ 2 * (Q + 1) = Q - Q ^ 2 * (1 + Q - Q ^ 2) := by ring
      _ = 0 := by linear_combination -hgold
  rcases mul_eq_zero.mp hfac with h12 | h3
  · rcases mul_eq_zero.mp h12 with h1 | h2
    · exact hQ0 h1
    · exact hQ1 (sub_eq_zero.mp (pow_eq_zero h2))
  · exact hQm1 h3

/-- **All-`r` exclusion of `1/[2]_q` from the Wenzl level family (`qou-niah`).**
In any strict ordered field, whenever `0 < Q` and `1 + Q < Q²` (e.g. `Q = 2`),
`Q^r (1 + Q - Q²) ≤ 0 < Q` for every `r : ℕ`, so `z_W = Q/(Q+1)` satisfies
Wenzl's parameter relation at **no** integer level `r`. -/
theorem inv_two_bracket_no_wenzl_level_of_sq_gt_add_one
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {Q z : K} (hQpos : 0 < Q) (hgt : 1 + Q < Q ^ 2) (hz : z * (Q + 1) = Q)
    (r : ℕ) :
    z * (1 - Q ^ r) ≠ Q ^ r * (1 - Q) := by
  intro h
  have hgold := pow_level_mul_golden_of_inv_two_bracket hz h
  have hpow : 0 < Q ^ r := pow_pos hQpos r
  have hneg : 1 + Q - Q ^ 2 < 0 := sub_neg.mpr hgt
  have hlhs : Q ^ r * (1 + Q - Q ^ 2) < 0 := mul_neg_of_pos_of_neg hpow hneg
  linarith

end QOU.QBeta.WenzlWeight
