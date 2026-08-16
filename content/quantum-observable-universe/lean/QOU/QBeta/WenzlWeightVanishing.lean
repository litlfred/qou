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

* **Cited, and since #5230 also axiomatised** — Wenzl's theorem that the
  Ocneanu/Markov trace weights on `H_n(Q)` at Markov parameter
  `z_W = Q^r(1−Q)/(1−Q^r)` are the principal specialisations
  `s_λ(1, Q, …, Q^{r−1})` of the Schur function, normalised so that
  `Σ_λ f^λ y_λ = tr(1) = 1`. See `-- Ref:` on `schurPrincipal`, and the class
  `IsOcneanuWeightSystem` in the *Wenzl's theorem as a hypothesis* section
  below, which carries it as an explicit `[Instance]` hypothesis on every
  statement that talks about the *actual* weight rather than the formula.
  This is the "Ocneanu-trace weight formula" of #5207's phrasing: the *given*,
  not the thing to be shown.

  **Axiomatising it upgrades nothing** (AGENTS.md §"Axiomatization is NOT a
  Proof"). Statements carrying `[IsOcneanuWeightSystem …]` are *proved
  conditional on Wenzl 1988*, which is what they already were. The change is
  that the compiler now tracks the dependency instead of a reader having to
  notice a comment.

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
hook-content product. The bridge to the actual weight is Wenzl 1988, carried by
`IsOcneanuWeightSystem`; the corresponding statement about the weight itself is
`conventionD_ocneanuWeight_eq_zero_iff_of_wenzl`, which is conditional.

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

/-! ## Wenzl's theorem as a hypothesis

Everything above is about `schurPrincipal`, a function this file *defines*. To
say anything about the **actual Ocneanu/Markov-trace weights** one needs the
external input — Wenzl (1988) — that those weights *are* this function. Below,
that input stops being a comment and becomes a class threaded through the
signature of every statement that depends on it (AGENTS.md §3b-cond).

**This proves nothing new.** Per AGENTS.md §"Axiomatization is NOT a Proof",
axiomatising an input does not discharge it: a `class` is an assumption wearing
infrastructure. The statements below are *proved conditional on Wenzl 1988* and
must be cited that way. What the change buys is that the dependency is
machine-tracked — a downstream declaration cannot use the weight-vanishing fact
without `IsOcneanuWeightSystem` appearing in its type, where `#check` and code
review will both see it.

**Why a `class` and not an `axiom`.** An `axiom` would assert Wenzl's theorem
globally and irrevocably; it could never be discharged, and it would have to be
stated at some fixed `(Q, z, r)` or else quantified over a Hecke-algebra
formalisation this repo does not have. The class form is parameterised, is
*satisfiable* and *falsifiable* (both proved below), and — the deciding
property — can one day be **discharged**: whoever formalises `H_n(Q)` and its
Markov trace supplies the instance, and every conditional statement below
becomes unconditional with no edit to this file. The cost is that the
dependency does not appear in `#print axioms`; it appears in the *type*
instead, which is why the conditional lemmas wear `_of_wenzl` in their names.

**No instance is provided, and none should be** except by proving Wenzl's
theorem. The satisfiability witness below is deliberately *not* registered as
an `instance`, so typeclass search can never silently discharge the hypothesis.
-/

/-- **Wenzl (1988), as an explicit hypothesis: `y` is the Ocneanu weight system
at level `r`.**

The class carries Wenzl's *hypothesis*, not the vanishing conclusion. Its two
fields say:

1. `markovParameter_eq` — the trace's Markov parameter `z` is Wenzl's at level
   `r`, i.e. `z = Q^r(1−Q)/(1−Q^r)`, cleared of denominators.
2. `weight_eq_schurPrincipal` — **the external input.** At that parameter the
   weights are the level-`r` principal specialisations, up to the normaliser
   `Z` fixed by `Σ_λ f^λ y_λ = tr(1) = 1`. Only `Z ≠ 0` is used, so the
   statement does not depend on which normalisation convention is in force.

Nothing about *vanishing* appears here. The conclusion `y μ = 0 ↔ ℓ(λ) > r` is
**derived** — from this class plus the unconditional
`schurPrincipal_eq_zero_iff` — rather than projected out of a field. That is
the §3b-cond non-degeneracy requirement, and it is the whole point: the
mathematical content of the vanishing lemma stays where it was proved, and the
class supplies only the bridge.

`y` is opaque. Lean cannot yet see the Hecke algebra or its trace, so the class
cannot *quantify over* the actual Ocneanu weight — it can only name the
property a candidate `y` would have to have. Producing an instance for the real
trace weights is exactly Wenzl's theorem, and is exactly what remains
unformalised.
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01404457
   Wenzl, "Hecke algebras of type $A_n$ and subfactors", Invent. Math. 92
   (1988) 349–383. -/
class IsOcneanuWeightSystem (Q z : R) (r : ℕ) (y : YoungDiagram → R) : Prop where
  /-- The trace's Markov parameter is Wenzl's at level `r`, denominators
  cleared: `z(1 − Q^r) = Q^r(1 − Q)`. -/
  markovParameter_eq : z * (1 - Q ^ r) = Q ^ r * (1 - Q)
  /-- **Wenzl 1988.** The weights are the level-`r` principal specialisations,
  up to a nonzero normaliser. -/
  weight_eq_schurPrincipal :
    ∃ Z : R, Z ≠ 0 ∧ ∀ μ : YoungDiagram, y μ = schurPrincipal r Q μ / Z

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
`level_unique_of_markovParameter`. It is what
`conventionD_ocneanuWeight_eq_zero_iff_of_wenzl` uses to consume the class's
`markovParameter_eq` field — so that field does real work rather than
decorating the class. -/
theorem level_eq_two_of_conventionD {q z : R} {r : ℕ} (hq0 : q ≠ 0)
    (hq2 : q ^ 2 + 1 ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → (q ^ 2) ^ k ≠ 1)
    (hz : z = q * (q ^ 3 / (q ^ 2 + 1)))
    (h : z * (1 - (q ^ 2) ^ r) = (q ^ 2) ^ r * (1 - q ^ 2)) : r = 2 := by
  subst hz
  refine level_unique_of_markovParameter (pow_ne_zero 2 hq0) hQ h ?_
  field_simp
  ring

/-! ### The vanishing criterion for the actual Ocneanu weight (conditional) -/

/-- **The weight-vanishing criterion, conditional on Wenzl 1988.**

`y μ = 0 ↔ ℓ(μ) > r`, for the *actual* Ocneanu weight system `y` — as opposed
to `schurPrincipal_eq_zero_iff`, which says the same of the formula and is
unconditional.

Derived, not projected: the class supplies `y = schurPrincipal / Z`, and all
the mathematical content comes from `schurPrincipal_eq_zero_iff`.

`z` is an explicit argument: it appears in the hypothesis but not in the
conclusion, so typeclass resolution cannot recover it. -/
theorem ocneanuWeight_eq_zero_iff_of_wenzl {Q : R} (z : R) {r : ℕ}
    {y : YoungDiagram → R} [hw : IsOcneanuWeightSystem Q z r y] (hQ0 : Q ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) (μ : YoungDiagram) :
    y μ = 0 ↔ r < μ.colLen 0 := by
  obtain ⟨Z, hZ, hy⟩ := hw.weight_eq_schurPrincipal
  rw [hy, div_eq_zero_iff]
  simp only [hZ, or_false]
  exact schurPrincipal_eq_zero_iff hQ0 hQ r μ

/-- **The all-`n` Temperley–Lieb weight-vanishing lemma for the actual Ocneanu
weight — conditional on Wenzl 1988.**

At convention D, `y_λ = 0 ⟺ λ has at least three rows`. This is the statement
#5207 named, stated about the object #5207 meant (the trace's Wedderburn
weights) rather than about the hook-content formula, and it is **conditional**:
the `[IsOcneanuWeightSystem]` hypothesis is Wenzl's theorem.

Both class fields are consumed, neither trivially:

* `markovParameter_eq` → `level_eq_two_of_conventionD` turns convention D's
  parameter into the integer `r = 2`;
* `weight_eq_schurPrincipal` → transports the unconditional vanishing criterion
  to `y`.

Cite as *"proved conditional on Wenzl 1988"*, never as *"proved"*.

`z` and `r` are explicit: neither appears in the conclusion, so typeclass
resolution cannot recover them. -/
theorem conventionD_ocneanuWeight_eq_zero_iff_of_wenzl {q : R} (z : R) (r : ℕ)
    {y : YoungDiagram → R} [hw : IsOcneanuWeightSystem (q ^ 2) z r y]
    (hq0 : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → (q ^ 2) ^ k ≠ 1)
    (hz : z = q * (q ^ 3 / (q ^ 2 + 1))) (μ : YoungDiagram) :
    y μ = 0 ↔ 3 ≤ μ.rowLens.length := by
  have hr : r = 2 :=
    level_eq_two_of_conventionD hq0 hq2 hQ hz hw.markovParameter_eq
  subst hr
  rw [ocneanuWeight_eq_zero_iff_of_wenzl (r := 2) z (pow_ne_zero 2 hq0) hQ μ,
    YoungDiagram.length_rowLens]
  omega

/-- The surviving side for the actual weight — conditional on Wenzl 1988.
A diagram with at most two rows has nonzero Ocneanu weight. -/
theorem conventionD_ocneanuWeight_ne_zero_of_two_rows_of_wenzl {q : R} (z : R)
    (r : ℕ) {y : YoungDiagram → R} [IsOcneanuWeightSystem (q ^ 2) z r y]
    (hq0 : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hQ : ∀ k : ℤ, k ≠ 0 → (q ^ 2) ^ k ≠ 1)
    (hz : z = q * (q ^ 3 / (q ^ 2 + 1))) (μ : YoungDiagram)
    (h : μ.rowLens.length ≤ 2) : y μ ≠ 0 := by
  rw [Ne, conventionD_ocneanuWeight_eq_zero_iff_of_wenzl z r hq0 hq2 hQ hz μ]
  omega

/-! ### The class is satisfiable, and it is not vacuous

A conditional theorem behind an *unsatisfiable* hypothesis proves nothing, and
one behind a hypothesis satisfied by *everything* constrains nothing. Both are
ruled out below: some `y` meet the class, and some `y` demonstrably do not.
-/

/-- **The class is satisfiable** — the hypothesis is not empty, so the
conditional theorems above are not vacuous.

**This does not discharge Wenzl's theorem, and must not be read as doing so.**
It says only that the *defined function* `schurPrincipal` satisfies, by
`rfl`, the property of being its own principal specialisation. Wenzl's content
is that the **Markov trace's** weights have this form — a statement about an
object this file cannot name. Deliberately **not** an `instance`, so typeclass
resolution can never use it to silently discharge an
`[IsOcneanuWeightSystem …]` hypothesis. -/
theorem isOcneanuWeightSystem_schurPrincipal (r : ℕ) {Q : R}
    (hQr : (1 : R) - Q ^ r ≠ 0) :
    IsOcneanuWeightSystem Q (Q ^ r * (1 - Q) / (1 - Q ^ r)) r
      (fun μ => schurPrincipal r Q μ / 1) where
  markovParameter_eq := by field_simp
  weight_eq_schurPrincipal := ⟨1, one_ne_zero, fun _ => rfl⟩

/-- **The class is not vacuous: it rules things out.**

The constant function `1` is *not* an Ocneanu weight system at `Q = 2` in `ℚ`,
at any level `2` and any parameter — because it fails to vanish on the
three-row diagram `(1³)`, which `ocneanuWeight_eq_zero_iff_of_wenzl` forces it
to. So the class genuinely constrains `y`; it is not a label that any function
can wear. Together with `isOcneanuWeightSystem_schurPrincipal` this brackets
the hypothesis from both sides. -/
theorem not_isOcneanuWeightSystem_const_one (z : ℚ) :
    ¬ IsOcneanuWeightSystem (2 : ℚ) z 2 (fun _ => 1) := by
  intro hw
  have hQ : ∀ k : ℤ, k ≠ 0 → (2 : ℚ) ^ k ≠ 1 :=
    not_root_of_unity_of_pos_ne_one (by norm_num) (by norm_num)
  have := (ocneanuWeight_eq_zero_iff_of_wenzl (hw := hw) z (by norm_num) hQ
    (YoungDiagram.ofRowLens [1, 1, 1] (by decide))).mpr
    (by rw [colLen_ofRowLens_one_one_one]; norm_num)
  norm_num at this

end QOU.QBeta.WenzlWeight
