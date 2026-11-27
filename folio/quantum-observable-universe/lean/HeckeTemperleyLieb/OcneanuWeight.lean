import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Algebra.BigOperators.Field
import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Algebra.Polynomial.BigOperators
import Mathlib.LinearAlgebra.Span.Basic
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.Algebra.Polynomial.Eval.SMul
import Mathlib.LinearAlgebra.LinearIndependent.Lemmas

/-!
# QOU.SchurWeyl.OcneanuWeight — the Ocneanu/Markov weight at general `n`

`HeckeWedderburnData` realises the Markov trace on `H_n(q)` as a weighted character sum
`tr_M = Σ_λ w_λ χ_λ`.  `HeckeMarkov3` proves the three weights at `n = 3`
(`markovWeight0/1/2`, derive-then-check against the normalisation and the two Markov relations);
`HeckeWedderburnDataGeneral` supplies the block decomposition at every `n` but leaves the weight
family an explicit **parameter**, because what makes a family *the* Ocneanu one is the Markov
condition, and that is proved only at `n = 3`.

This file supplies the missing ingredient's *definition*: a single closed form
`ocneanuWeight q z μ`, one formula for every Young diagram.  That it **reproduces
`markovWeight0/1/2` exactly** at `n = 3` is proved in `OcneanuWeightMarkov3`, which is a separate
file because those comparisons are `ℝ`-valued (§7c below) while everything here is generic.

## The formula

For a Young diagram `μ`,

```
ocneanuWeight q z μ  =  ∏_{(i,j) ∈ μ} ( q^{2i}·(q² − 1 − q·z) + q^{2j+1}·z )
                      / ∏_{(i,j) ∈ μ} ( q^{2·h(i,j)} − 1 )
```

with `h` the hook length.  Numerator: one factor per cell, affine in the Markov parameter `z`, with
a framing monomial in the row index.  Denominator: the `q²`-hook product.  Pulling the row index
out of the numerator gives the equivalent form `q^{2n(λ)}·∏_x ((q²−1) + zq(q^{2c(x)}−1)) /
∏_x (q^{2h(x)}−1)`, with `c` the cell content and `n(λ) = Σ_i i·λ_i`.

## Provenance — derived, not recalled

The corpus already carried a candidate general-`n` weight
(`computations/mass_at_3A_proper.py::jones_wenzl_weight`).  It is **wrong**: it fails to reproduce
the proved `n = 3` weights under any of 160 convention combinations, and never sums to `1`
(`computations/schurweyl/ocneanu_weight_validation.py`).  The formula above was therefore derived
rather than recalled, in exact `ℚ(q,z)`
(`computations/schurweyl/ocneanu_weight_general_n.py`): solve `n = 2` from `tr(1) = 1` and
`tr(σ₁) = z`; read `n ≤ 3` as a per-cell content product over the hook denominator; then solve
`n = 4, 5` from scratch to pin the framing monomial, which `n ≤ 3` **cannot** see — every partition
of `n ≤ 3` has distinct cell contents, and the first repeat is the two content-`0` cells of `(2,2)`.

Numerically validated in exact arithmetic: `Σ_λ d_λ w_λ = 1` and `Σ_λ w_λ χ^λ(σ₁) = z` through
`n = 6`, and the branching identity `w_μ^{(n)} = Σ_{λ = μ + □} w_λ^{(n+1)}` through `n = 5 → 6`.

## What is NOT claimed here

`OcneanuWeightMarkov3`'s `n = 3` specialisations are the only Lean-proved content about this
formula.  **The Markov property at general `n` is open.**  Nothing in either file instantiates
`HeckeWedderburnData` with `ocneanuWeight` — doing so would let a downstream consumer read the
resulting functional as a Markov trace on the strength of a numerical check, which is exactly the
laundering `HeckeWedderburnDataGeneral`'s docstring warns against.  The general-`n` Markov property
has to be *proved* before that instantiation is honest.

**Update 2026-11-20 — it is now proved, at every `z` and every `n`**, in
`OcneanuMarkovTraceEveryZ` (`SeminormalRep.ocneanuMarkovTraceEveryZ`): normalisation, branching and
the Markov condition for `ocneanuWeight q z` follow by polynomial interpolation in `z` from the
proved Wenzl-level theorems, because `ocneanuWeight q z_r = wenzlWeight r (q²)` on the infinite
lattice `z_r = Q^r/(q·[r]_Q)`. The sentences above describe this file, which still proves only the
definition and the `n = 3` checks.

## Base ring (§7c)

`ocneanuWeight` is stated over a generic `[Field R]`: it is a rational function of `q` and `z` with
no ordering, no `Real.sqrt`, no archimedean content — this file mentions `ℝ` nowhere.  The
specialisation to `ℝ` is confined to `OcneanuWeightMarkov3`, and is forced only because
`markovWeight0/1/2` are `ℝ`-valued.

References: Jones (1987) `[jones1987]`, Wenzl (1988) `[wenzl1988]`, Ram (1997) `[ram1997]`.

LaTeX label: `def:ocneanu-weight`
-/

namespace QOU.SchurWeyl

open YoungDiagram

/-- Hook length of the cell `c` in the Young diagram `μ`: arm (cells weakly to the right of `c` in
its row, `c` included) plus leg (cells strictly below `c` in its column). -/
def hookLength (mu : YoungDiagram) (c : ℕ × ℕ) : ℕ :=
  (mu.cells.filter (fun d => d.1 = c.1 ∧ c.2 ≤ d.2)).card
    + (mu.cells.filter (fun d => d.2 = c.2 ∧ c.1 < d.1)).card

/-- **The Ocneanu/Markov weight of a Young diagram**, one closed form for every `n`.

`w_μ(q,z) = ∏_{(i,j) ∈ μ} (q^{2i}(q² − 1 − qz) + q^{2j+1} z) / ∏_{(i,j) ∈ μ} (q^{2h(i,j)} − 1)`.

See the module docstring for how this was derived and for what is *not* proved about it. -/
noncomputable def ocneanuWeight {R : Type*} [Field R] (q z : R) (mu : YoungDiagram) : R :=
  (∏ c ∈ mu.cells, (q ^ (2 * c.1) * (q ^ 2 - 1 - q * z) + q ^ (2 * c.2 + 1) * z))
    / (∏ c ∈ mu.cells, (q ^ (2 * hookLength mu c) - 1))

/-! ### The convention-D Markov parameter truncates the support

Setting the per-cell numerator factor of a cell of content `c` to zero and solving for `z` gives
`z = q^{2k+1} / (1 + q² + ⋯ + q^{2k})` for `c = −k` (and no solution at `c = 0`, where the factor is
the constant `q² − 1`).  The **`k = 2`** member of that family is `z = q³/(q²+1)` — which is exactly
the Markov parameter of **convention D**, made canonical by the owner ruling of 2026-08-15.

So at convention D every Young diagram with three or more rows carries weight **zero**: such a
diagram contains the cell `(2,0)`, of content `−2`.  The `k = 1` member `z = q` likewise kills every
diagram with two or more rows.  Convention C's `z = √q/(q+1)` is not a member of the family at any
integer content, and truncates nothing.

Vanishing on the partitions of three or more rows is the condition for a trace on `H_n(q)` to
factor through its Temperley–Lieb quotient; that reading is standard (Jones (1983), Wenzl (1988))
and is *not* proved here.  What is proved here is the vanishing itself.

**This DUPLICATES existing corpus content, and is kept for one specific reason.**
`QOU.QBeta.WenzlWeight.schurPrincipal_eq_zero_iff` (sorry-free, general `n`, general level `r`)
already proves the vanishing criterion, and `wenzlLevel_conventionD` already proves that convention D
is level `r = 2`.  I derived the statement below independently and only then grepped the corpus —
the wrong order, and the corpus-grep discipline exists precisely to catch it.  The theorem is
retained because its hypotheses are strictly weaker: it needs no root-of-unity condition on `q`,
where the `iff` does.  The sharper `iff`, and the identification of the two weight formulas that
makes the duplication visible, are in `OcneanuWeightWenzl`:
`ocneanuWeight q (q³/(q²+1)) μ = schurPrincipal 2 (q²) μ / (q²+1)^{|μ|}`.

Cross-checked against `computations/ocneanu_weights.py::omega_lambda_via_inversion`, an independent
`p(n) × p(n)` linear solve at the live `q₀` and this `z`: at `n = 2 … 5` exactly the diagrams with
three or more rows come back zero, and every other weight agrees with the closed form to the limit
of the float64 arithmetic that path uses (worst `1.5e-16`, which cannot distinguish agreement from a
discrepancy below that scale). -/

/-- The numerator factor of a cell of content `−2` vanishes at `z = q³/(q²+1)`. -/
theorem ocneanuNumFactor_eq_zero_of_content_neg_two {R : Type*} [Field R] (q : R)
    (hq : q ^ 2 + 1 ≠ 0) (j : ℕ) :
    q ^ (2 * (j + 2)) * (q ^ 2 - 1 - q * (q ^ 3 / (q ^ 2 + 1)))
        + q ^ (2 * j + 1) * (q ^ 3 / (q ^ 2 + 1)) = 0 := by
  have hpow : q ^ (2 * (j + 2)) = q ^ (2 * j + 1) * q ^ 3 := by ring
  rw [hpow]
  field_simp
  ring

/-- **At the convention-D Markov parameter `z = q³/(q²+1)`, every partition with three or more rows
has weight zero.**

The hypothesis `0 < μ.rowLen 2` says the third row is nonempty, i.e. `μ` has at least three rows;
equivalently `(2,0) ∈ μ`, a cell of content `−2`, whose numerator factor vanishes at this `z`. -/
theorem ocneanuWeight_conventionD_eq_zero_of_three_rows {R : Type*} [Field R] (q : R)
    (hq : q ^ 2 + 1 ≠ 0) (mu : YoungDiagram) (h : 0 < mu.rowLen 2) :
    ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) mu = 0 := by
  have hmem : (2, 0) ∈ mu.cells := by
    rw [YoungDiagram.mem_cells, YoungDiagram.mem_iff_lt_rowLen]
    exact h
  have hzero : ∏ c ∈ mu.cells,
      (q ^ (2 * c.1) * (q ^ 2 - 1 - q * (q ^ 3 / (q ^ 2 + 1)))
        + q ^ (2 * c.2 + 1) * (q ^ 3 / (q ^ 2 + 1))) = 0 :=
    Finset.prod_eq_zero hmem (by
      simpa using ocneanuNumFactor_eq_zero_of_content_neg_two (R := R) q hq 0)
  rw [ocneanuWeight, hzero, zero_div]

/-! ### The `z`-dependence lives only off the diagonal

The numerator factor of a cell is affine in `z`; its `z`-coefficient is
`q^{2j+1} − q^{2i+1}`, which vanishes **identically on the diagonal `i = j`** — with no hypothesis
on `q` whatever, since the two `z` terms cancel term-for-term. So a diagonal cell contributes a
constant, and the whole `z`-dependence of `ocneanuWeight` is carried by the off-diagonal cells.

Counting them gives the degree: a Young diagram has `d(μ)` diagonal cells (its Durfee square size),
so the numerator has `z`-degree at most `|μ| − d(μ)`. Since **every** non-empty diagram contains
`(0,0)`, `d ≥ 1` always, and the naive bound `|μ|` from `|μ|` affine factors is never attained.

**Why this matters, and where it is used.** The span of the Markov traces over the whole Ocneanu
family `{z_N}` is bounded by that degree plus one: writing `W(z) = Σ_k z^k c_k`, the family lies in
the span of the coefficient vectors `c_k`. Measured against `p(n)` — the number of Wedderburn
blocks, i.e. the dimension of the full space of trace functionals — this is a strong restriction,
and it is what forbids recovering an individual block's character by any *subtraction* over the
family.

`computations/probes/markov_trace_family_rank_probe.py` measures the consequences: `deg_z = |μ| −
d(μ)` for every partition at `n = 2..6` (exact, sympy over `ℚ(q)`), a resulting family rank of
exactly `n` against `p(n)` blocks, and — at `n = 6` — only the two one-dimensional blocks
individually recoverable, `(4,2)` **not** among them despite being visible to convention D.

**What is proved here is the mechanism, not the degree count.** The statement below confines the
`z`-dependence to the off-diagonal cells, which is the content; turning that into `deg_z ≤ |μ| −
d(μ)` needs the polynomial-degree argument over the product and is **not** done here. Nor is
`rank = n` proved — it is measured at `n = 2..7`, so the exclusion it supports is scope-(a). -/

/-- **The cell numerator factor is affine in `z`**, with `z`-coefficient `q^{2j+1} − q^{2i+1}`. -/
theorem ocneanuNumFactor_affine {R : Type*} [Field R] (q z : R) (i j : ℕ) :
    q ^ (2 * i) * (q ^ 2 - 1 - q * z) + q ^ (2 * j + 1) * z
      = q ^ (2 * i) * (q ^ 2 - 1) + (q ^ (2 * j + 1) - q ^ (2 * i + 1)) * z := by
  ring

/-- **A diagonal cell contributes no `z`.** At `i = j` the two `z` terms cancel identically, so the
factor is the constant `q^{2i}(q² − 1)`. Unconditional: no hypothesis on `q`. -/
theorem ocneanuNumFactor_diagonal_z_free {R : Type*} [Field R] (q z : R) (i : ℕ) :
    q ^ (2 * i) * (q ^ 2 - 1 - q * z) + q ^ (2 * i + 1) * z = q ^ (2 * i) * (q ^ 2 - 1) := by
  ring

/-- **The `z`-dependence of the numerator is confined to the off-diagonal cells.**

The product splits into a `z`-free part over the diagonal cells and a part over the off-diagonal
cells, each factor there affine in `z` with a nonzero-in-general coefficient. The number of factors
that can carry `z` is therefore `|μ| − d(μ)`, `d(μ)` the count of diagonal cells. -/
theorem ocneanuNum_diagonal_split {R : Type*} [Field R] (q z : R) (mu : YoungDiagram) :
    (∏ c ∈ mu.cells, (q ^ (2 * c.1) * (q ^ 2 - 1 - q * z) + q ^ (2 * c.2 + 1) * z))
      = (∏ c ∈ mu.cells.filter (fun c => c.1 = c.2), q ^ (2 * c.1) * (q ^ 2 - 1))
        * (∏ c ∈ mu.cells.filter (fun c => ¬ (c.1 = c.2)),
            (q ^ (2 * c.1) * (q ^ 2 - 1) + (q ^ (2 * c.2 + 1) - q ^ (2 * c.1 + 1)) * z)) := by
  rw [← Finset.prod_filter_mul_prod_filter_not mu.cells (fun c => c.1 = c.2)]
  congr 1
  · refine Finset.prod_congr rfl ?_
    intro c hc
    have hij : c.1 = c.2 := (Finset.mem_filter.mp hc).2
    rw [← hij]
    exact ocneanuNumFactor_diagonal_z_free q z c.1
  · exact Finset.prod_congr rfl fun c _ => ocneanuNumFactor_affine q z c.1 c.2

/-- **Every non-empty diagram has a diagonal cell**, namely `(0,0)`. So `d(μ) ≥ 1` and the top
`z`-power `z^{|μ|}` always dies — the naive degree bound from `|μ|` affine factors is never
attained. -/
theorem mem_cells_diag_zero (mu : YoungDiagram) (h : 0 < mu.rowLen 0) : (0, 0) ∈ mu.cells := by
  rw [YoungDiagram.mem_cells, YoungDiagram.mem_iff_lt_rowLen]
  exact h

/-! ### The degree bound, as a polynomial in `z`

Packaging the numerator as an element of `R[X]` turns the split above into an actual **degree**
statement: the product's degree is at most the sum of its factors' degrees, each diagonal factor is
a constant, and each off-diagonal factor is linear. So

    deg_z (numerator)  ≤  #{cells off the diagonal}  =  |μ| − d(μ)

with `d(μ)` the Durfee square size. This is the `≤` direction, which is the one the span argument
needs: `W(z) = Σ_{k ≤ deg} z^k c_k` lies in the span of `deg + 1` fixed coefficient vectors, so the
whole Ocneanu family spans at most that many dimensions of the `p(n)`-dimensional space of trace
functionals.

Equality (`deg_z = |μ| − d(μ)` exactly) is **not** proved here — it is measured, exactly and
symbolically over `ℚ(q)`, at `n = 2..6` in
`computations/probes/markov_trace_family_rank_probe.py`, along with the resulting family rank of
exactly `n`. Neither equality nor `rank = n` is a theorem for all `n`. -/

open Polynomial in
/-- The Ocneanu numerator as a polynomial in the Markov parameter `z`, with the affine form of
`ocneanuNumFactor_affine` as its per-cell factor. -/
noncomputable def ocneanuNumPoly {R : Type*} [Field R] (q : R) (mu : YoungDiagram) : R[X] :=
  ∏ c ∈ mu.cells,
    (C (q ^ (2 * c.1) * (q ^ 2 - 1)) + C (q ^ (2 * c.2 + 1) - q ^ (2 * c.1 + 1)) * X)

open Polynomial in
/-- `ocneanuNumPoly` really is the numerator: evaluating at `z` returns it. Without this the degree
bound below would be a statement about a free-standing polynomial rather than about the weight. -/
theorem ocneanuNumPoly_eval {R : Type*} [Field R] (q z : R) (mu : YoungDiagram) :
    (ocneanuNumPoly q mu).eval z
      = ∏ c ∈ mu.cells, (q ^ (2 * c.1) * (q ^ 2 - 1 - q * z) + q ^ (2 * c.2 + 1) * z) := by
  rw [ocneanuNumPoly, eval_prod]
  refine Finset.prod_congr rfl fun c _ => ?_
  simp only [eval_add, eval_mul, eval_C, eval_X]
  exact (ocneanuNumFactor_affine q z c.1 c.2).symm

open Polynomial in
/-- A cell factor is linear in `z`, hence of degree at most one. -/
theorem ocneanuNumFactor_natDegree_le_one {R : Type*} [Field R] (a b : R) :
    (C a + C b * X).natDegree ≤ 1 := by
  refine natDegree_add_le_of_degree_le ?_ ?_
  · simp
  · exact le_trans natDegree_mul_le (by simp)

open Polynomial in
/-- **The degree bound.** The numerator's degree in `z` is at most the number of cells **off** the
diagonal — equivalently `|μ| − d(μ)`, since the diagonal cells contribute constants. -/
theorem ocneanuNumPoly_natDegree_le {R : Type*} [Field R] (q : R) (mu : YoungDiagram) :
    (ocneanuNumPoly q mu).natDegree
      ≤ (mu.cells.filter (fun c => ¬ (c.1 = c.2))).card := by
  refine le_trans (natDegree_prod_le _ _) ?_
  rw [← Finset.sum_filter_add_sum_filter_not mu.cells (fun c => c.1 = c.2)]
  have hdiag : ∑ c ∈ mu.cells.filter (fun c => c.1 = c.2),
      (C (q ^ (2 * c.1) * (q ^ 2 - 1))
        + C (q ^ (2 * c.2 + 1) - q ^ (2 * c.1 + 1)) * X).natDegree = 0 := by
    refine Finset.sum_eq_zero fun c hc => ?_
    have h : c.1 = c.2 := (Finset.mem_filter.mp hc).2
    rw [← h, sub_self, map_zero, zero_mul, add_zero, natDegree_C]
  rw [hdiag, zero_add]
  refine le_trans (Finset.sum_le_sum (g := fun _ => 1)
    (fun c _ => ocneanuNumFactor_natDegree_le_one _ _)) ?_
  simp

/-! ### The span bound — why the degree bound restricts the whole family

The degree bound is what limits the *family*. A trace functional in the Ocneanu family is the
weight vector `W(z)` read at one `z`; if each component is a polynomial of degree `≤ d`, then
`W(z) = Σ_{k ≤ d} z^k c_k` for `d+1` fixed coefficient vectors, so **every** member of the family —
at every `z`, not merely the sampled ones — lies in the span of those `d+1` vectors.

Combined with `deg_z ≤ |μ| − d(μ) ≤ |μ| − 1`, the family at level `n` spans **at most `n`
dimensions**, against the `p(n)` dimensions of the full space of trace functionals. That gap is
what forbids isolating an individual block's character by subtraction over the family.

The first two lemmas are stated for an arbitrary finite family of polynomials, since nothing about
the Ocneanu weight is used. `ocneanuFamily_finrank_le` is the application. -/

open Polynomial in
/-- A family of polynomials of degree `≤ d`, evaluated at `z`, lies in the span of the `d+1`
coefficient vectors — for **every** `z`. -/
theorem eval_mem_span_coeff {R ι : Type*} [Field R] [Fintype ι]
    (p : ι → R[X]) (d : ℕ) (hd : ∀ i, (p i).natDegree ≤ d) (z : R) :
    (fun i => (p i).eval z)
      ∈ Submodule.span R (Set.range fun k : Fin (d + 1) => fun i => (p i).coeff (k : ℕ)) := by
  have key : (fun i => (p i).eval z)
      = ∑ k : Fin (d + 1), z ^ (k : ℕ) • (fun i => (p i).coeff (k : ℕ)) := by
    funext i
    simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul]
    rw [eval_eq_sum_range' (n := d + 1) (Nat.lt_succ_of_le (hd i))]
    rw [Fin.sum_univ_eq_sum_range (fun k => z ^ k * (p i).coeff k)]
    exact Finset.sum_congr rfl fun k _ => mul_comm _ _
  rw [key]
  exact Submodule.sum_mem _ fun k _ =>
    Submodule.smul_mem _ _ (Submodule.subset_span ⟨k, rfl⟩)

open Polynomial in
/-- **The family spans at most `d+1` dimensions.** -/
theorem finrank_span_eval_le {R ι : Type*} [Field R] [Fintype ι]
    (p : ι → R[X]) (d : ℕ) (hd : ∀ i, (p i).natDegree ≤ d) :
    Module.finrank R
        (Submodule.span R (Set.range fun z : R => fun i => (p i).eval z)) ≤ d + 1 := by
  classical
  have hle : Submodule.span R (Set.range fun z : R => fun i => (p i).eval z)
      ≤ Submodule.span R (Set.range fun k : Fin (d + 1) => fun i => (p i).coeff (k : ℕ)) := by
    rw [Submodule.span_le]
    rintro _ ⟨z, rfl⟩
    exact eval_mem_span_coeff p d hd z
  haveI : Fintype ↑(Set.range fun k : Fin (d + 1) => fun i => (p i).coeff (k : ℕ)) :=
    (Set.finite_range _).fintype
  haveI : Module.Finite R
      ↥(Submodule.span R (Set.range fun k : Fin (d + 1) => fun i => (p i).coeff (k : ℕ))) :=
    Module.Finite.span_of_finite R (Set.finite_range _)
  refine (Submodule.finrank_mono hle).trans ?_
  refine (finrank_span_le_card _).trans ?_
  rw [Set.toFinset_range]
  exact Finset.card_image_le.trans (by simp)

/-- Off-diagonal cells are strictly fewer than all cells, because `(0,0)` is diagonal. -/
theorem ocneanuOffDiag_card_lt {mu : YoungDiagram} (h : 0 < mu.rowLen 0) :
    (mu.cells.filter (fun c => ¬ (c.1 = c.2))).card < mu.card := by
  classical
  refine Finset.card_lt_card ?_
  refine (Finset.ssubset_iff_of_subset (Finset.filter_subset _ _)).mpr ?_
  exact ⟨(0, 0), mem_cells_diag_zero mu h, by simp⟩

open Polynomial in
/-- **The Ocneanu family at level `n` spans at most `n` dimensions**, against the `p(n)` dimensions
of the full space of trace functionals on `H_n(q)`.

This is the `≤` half of the measured `rank = n`; equality is **not** proved (see
`markov_trace_family_rank_probe.py`, exact at `n = 2..6`). -/
theorem ocneanuFamily_finrank_le {R : Type*} [Field R] (q : R) (n : ℕ) (hn : 0 < n)
    (S : Finset YoungDiagram) (hcard : ∀ mu ∈ S, mu.card = n)
    (hne : ∀ mu ∈ S, 0 < mu.rowLen 0) :
    Module.finrank R (Submodule.span R
        (Set.range fun z : R => fun mu : {x // x ∈ S} =>
          (ocneanuNumPoly q (mu : YoungDiagram)).eval z)) ≤ n := by
  have hd : ∀ mu : {x // x ∈ S},
      (ocneanuNumPoly q (mu : YoungDiagram)).natDegree ≤ n - 1 := by
    intro mu
    refine (ocneanuNumPoly_natDegree_le q _).trans ?_
    have hlt := ocneanuOffDiag_card_lt (hne _ mu.2)
    rw [hcard _ mu.2] at hlt
    omega
  exact (finrank_span_eval_le
    (fun mu : {x // x ∈ S} => ocneanuNumPoly q (mu : YoungDiagram)) (n - 1) hd).trans_eq
    (Nat.sub_add_cancel hn)

/-! ### The lower bound: the `n` hooks are linearly independent, so `rank = n`

`ocneanuFamily_finrank_le` gives `rank ≤ n`. This section supplies `≥ n` by exhibiting `n`
members of the family that are linearly independent — the **hook** diagrams `(n−k, 1^k)`,
`k = 0..n−1`. Each hook has one diagonal cell, `n−k−1` arm cells and `k` leg cells, so its
numerator is `(q²−1)·∏ arm_j·∏ leg_i`, a product of `n−1` linear factors with **known roots**.

The mechanism is that **the leg roots are the Ocneanu family itself**: the `i`-th leg factor
vanishes at `z_i = q^{2i}(q²−1)/(q(q^{2i}−1)) = q^i/[i]_q`. So hook `k` vanishes at `z_m` exactly
when `m ≤ k` — which is the row cap, read as *"a diagram with `k+1` rows is invisible at every
level `≤ k`"* — and evaluating hooks `0..n−1` at `z_1..z_n` gives a triangular system with nonzero
diagonal. The row cap and the rank are one phenomenon.

The genericity conditions on `q` (leg roots distinct; arm roots off the leg roots; `q² ≠ 1`)
are **stated as hypotheses**, not proved: they hold when `q` is not a root of unity of small
order, and `hooks_linearIndependent` is exactly as conditional as they are. Measured exactly
over `ℚ(q)` at `n = 2..6` in `markov_trace_family_rank_probe.py`; the leg-root/Ocneanu
identification was verified there symbolically before this was written.

`hookNum` is the hook numerator written out directly. Its identification with
`ocneanuNumPoly q μ` for the hook diagram `μ` is **not** proved here — it requires computing
`YoungDiagram.cells` of a specific shape and is a separate plumbing step. -/

open Polynomial in
/-- **Triangular independence** (generic). If functionals `φ m` satisfy `φ m (f k) = 0` for
`m < k` and `φ m (f m) ≠ 0`, then `f` is linearly independent: apply `φ 0` to a vanishing
combination to isolate `c 0`, then `φ 1`, and so on. -/
theorem linearIndependent_of_triangular {R V : Type*} [Field R] [AddCommGroup V] [Module R V]
    {n : ℕ} (f : Fin n → V) (φ : Fin n → (V →ₗ[R] R))
    (hlt : ∀ m k : Fin n, m < k → φ m (f k) = 0)
    (hdiag : ∀ m : Fin n, φ m (f m) ≠ 0) :
    LinearIndependent R f := by
  rw [Fintype.linearIndependent_iff]
  intro g hg
  suffices H : ∀ N : ℕ, ∀ i : Fin n, (i : ℕ) = N → g i = 0 from fun i => H i i rfl
  intro N
  induction N using Nat.strong_induction_on with
  | _ N ih =>
    intro i hi
    have h1 : φ i (∑ k, g k • f k) = 0 := by rw [hg, map_zero]
    rw [map_sum] at h1
    simp only [map_smul, smul_eq_mul] at h1
    have hsplit : ∀ k : Fin n, k ≠ i → g k * φ i (f k) = 0 := by
      intro k hk
      rcases lt_or_gt_of_ne hk with hki | hik
      · have : g k = 0 := ih k (by rw [← hi]; exact hki) k rfl
        rw [this, zero_mul]
      · rw [hlt i k hik, mul_zero]
    rw [Finset.sum_eq_single i (fun k _ hk => hsplit k hk)
      (fun h => absurd (Finset.mem_univ i) h)] at h1
    exact (mul_eq_zero.mp h1).resolve_right (hdiag i)

open Polynomial in
/-- Arm cell `(0,j)`, `j ≥ 1`: numerator factor `(q²−1) + q(q^{2j}−1)·z`. -/
noncomputable def armFactor {R : Type*} [Field R] (q : R) (j : ℕ) : R[X] :=
  C (q ^ 2 - 1) + C (q * (q ^ (2 * j) - 1)) * X

open Polynomial in
/-- Leg cell `(i,0)`, `i ≥ 1`: numerator factor `q^{2i}(q²−1) − q(q^{2i}−1)·z`. -/
noncomputable def legFactor {R : Type*} [Field R] (q : R) (i : ℕ) : R[X] :=
  C (q ^ (2 * i) * (q ^ 2 - 1)) - C (q * (q ^ (2 * i) - 1)) * X

/-- The root of the `i`-th leg factor, `z_i = q^{2i}(q²−1)/(q(q^{2i}−1))` — which is the Ocneanu
family parameter `q^i/[i]_q`. -/
noncomputable def legRoot {R : Type*} [Field R] (q : R) (i : ℕ) : R :=
  q ^ (2 * i) * (q ^ 2 - 1) / (q * (q ^ (2 * i) - 1))

open Polynomial in
theorem legFactor_eval_legRoot {R : Type*} [Field R] (q : R) (i : ℕ)
    (hden : q * (q ^ (2 * i) - 1) ≠ 0) :
    (legFactor q i).eval (legRoot q i) = 0 := by
  have hq : q ≠ 0 := left_ne_zero_of_mul hden
  have hq2 : q ^ (2 * i) - 1 ≠ 0 := right_ne_zero_of_mul hden
  simp only [legFactor, legRoot, eval_sub, eval_mul, eval_C, eval_X]
  field_simp
  ring

open Polynomial in
/-- Numerator of the hook `(n−k, 1^k)`: one diagonal cell (constant), `n−k−1` arm cells, `k`
leg cells. -/
noncomputable def hookNum {R : Type*} [Field R] (q : R) (n k : ℕ) : R[X] :=
  C (q ^ 2 - 1) * (∏ j ∈ Finset.Icc 1 (n - k - 1), armFactor q j)
    * (∏ i ∈ Finset.Icc 1 k, legFactor q i)

open Polynomial in
/-- Hook `(n−k,1^k)` vanishes at leg root `z_m` for `1 ≤ m ≤ k`: the `m`-th leg factor is in the
product. This is the row cap in polynomial form. -/
theorem hookNum_eval_legRoot_eq_zero {R : Type*} [Field R] (q : R) (n k m : ℕ)
    (hm1 : 1 ≤ m) (hmk : m ≤ k) (hden : q * (q ^ (2 * m) - 1) ≠ 0) :
    (hookNum q n k).eval (legRoot q m) = 0 := by
  simp only [hookNum, eval_mul, eval_prod]
  have hmem : m ∈ Finset.Icc 1 k := Finset.mem_Icc.mpr ⟨hm1, hmk⟩
  rw [Finset.prod_eq_zero hmem (legFactor_eval_legRoot q m hden)]
  simp

open Polynomial in
/-- Hook `(n−k,1^k)` is NONZERO at leg root `z_m` when `k < m`: no leg factor `i ≤ k` is the
`m`-th, and no arm factor vanishes there. The `≠ 0` hypotheses are the genericity conditions on
`q`. -/
theorem hookNum_eval_legRoot_ne_zero {R : Type*} [Field R] (q : R) (n k m : ℕ) (hkm : k < m)
    (hq21 : q ^ 2 - 1 ≠ 0)
    (harm : ∀ j, (armFactor q j).eval (legRoot q m) ≠ 0)
    (hleg : ∀ i, i ≠ m → (legFactor q i).eval (legRoot q m) ≠ 0) :
    (hookNum q n k).eval (legRoot q m) ≠ 0 := by
  simp only [hookNum, eval_mul, eval_prod, eval_C]
  refine mul_ne_zero (mul_ne_zero hq21 ?_) ?_
  · exact Finset.prod_ne_zero_iff.mpr fun j _ => harm j
  · refine Finset.prod_ne_zero_iff.mpr fun i hi => hleg i ?_
    exact ne_of_lt (lt_of_le_of_lt (Finset.mem_Icc.mp hi).2 hkm)

open Polynomial in
/-- **The `n` hooks are linearly independent** — the `≥ n` half of `rank = n`.

Functional `m` is evaluation at `z_{m+1}`; hook `k` vanishes there iff `m+1 ≤ k` iff `m < k`,
and hook `m` is nonzero there. Uniform in `m` — the last hook needs no special case. -/
theorem hooks_linearIndependent {R : Type*} [Field R] (q : R) (n : ℕ)
    (hq21 : q ^ 2 - 1 ≠ 0)
    (hden : ∀ m, 1 ≤ m → m ≤ n → q * (q ^ (2 * m) - 1) ≠ 0)
    (harm : ∀ j m, 1 ≤ m → m ≤ n → (armFactor q j).eval (legRoot q m) ≠ 0)
    (hleg : ∀ i m, 1 ≤ m → m ≤ n → i ≠ m → (legFactor q i).eval (legRoot q m) ≠ 0) :
    LinearIndependent R (fun k : Fin n => hookNum q n (k : ℕ)) := by
  refine linearIndependent_of_triangular _ (fun m : Fin n => Polynomial.leval (legRoot q (m + 1)))
    ?_ ?_
  · intro m k hmk
    simp only [Polynomial.leval_apply]
    exact hookNum_eval_legRoot_eq_zero q n k (m + 1) (Nat.succ_pos _)
      (Nat.succ_le_of_lt hmk) (hden _ (Nat.succ_pos _) (Nat.succ_le_of_lt m.isLt))
  · intro m
    simp only [Polynomial.leval_apply]
    exact hookNum_eval_legRoot_ne_zero q n m (m + 1) (Nat.lt_succ_self _) hq21
      (fun j => harm j _ (Nat.succ_pos _) (Nat.succ_le_of_lt m.isLt))
      (fun i hi => hleg i _ (Nat.succ_pos _) (Nat.succ_le_of_lt m.isLt) hi)

end QOU.SchurWeyl
