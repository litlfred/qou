import Mathlib.Combinatorics.Young.YoungDiagram
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum
import QOU.MathlibExt.YoungDiagramCells

/-!
# QOU.BraidKnot.TwoFiltrationBridge — conjectural class (§3b)

**§3b class axiomatisation** for content block
[`conj:two-filtration-bridge`](../../../quantum-observable-universe/mass-theory/two-filtration-bridge.md):
*Two-filtration bridge: iterated-integral depth $\leftrightarrow$
partition-cellular GB-depth via the central idempotents $e_\lambda$.*

This is a **conjecture**: the class carries the conjecture's actual
content as the `bridge` field (the depth-lift dichotomy); the
`noncomputable instance`'s `sorry` represents the open conjecture itself
(per AGENTS.md §3b), NOT a missing proof.

**Mathlib-infra pass (2026-06-25, Tier 1).** Both partition-side objects
are now *real*: the partition index is Mathlib `YoungDiagram` with the
genuine conjugate involution `YoungDiagram.transpose` (self-conjugacy =
`μ.transpose = μ`), and the **partition-cellular GB-depth is the concrete
definition** `gbDepth` = max hook length over cells (built here from the
real `rowLen`/`colLen`/`cells` API) — no longer an abstract `dGB` class
field. Only the QOU-specific iterated-integral depth-lift `dII` and the
chiral-pair predicate remain abstract (the open conjectural content). The
faithful conditional form is
`QOU.AlgebraicSubstrate.TwoFiltrationBridgeGeneral`.
-/

namespace QOU.BraidKnot

open YoungDiagram

/-- **Hook length** of cell `c = (i, j)` in a Young diagram `μ`:
    arm `(rowLen i - j)` + leg `(colLen j - i)` − 1. For a cell of `μ`
    this is `≥ 1` (truncated ℕ subtraction is exact there). -/
def TwoFiltrationBridge.hookLength (μ : YoungDiagram) (c : ℕ × ℕ) : ℕ :=
  (μ.rowLen c.1 - c.2) + (μ.colLen c.2 - c.1) - 1

/-- **Partition-cellular GB-depth** $\mathrm{depth}_{\mathrm{GB}}(\lambda)
    = \max_\square h(\square)$: the maximum hook length over all cells
    (the centre $Z(H_n(q))$ side of the bridge). The empty diagram has
    depth `0`. -/
def gbDepth (μ : YoungDiagram) : ℕ :=
  μ.cells.sup fun c => TwoFiltrationBridge.hookLength μ c

/-- **Two-filtration bridge** (iterated-integral depth $\leftrightarrow$
    partition-cellular GB-depth via $e_\lambda$).

    Conjectural class — see
    [`conj:two-filtration-bridge`](../../../quantum-observable-universe/mass-theory/two-filtration-bridge.md). -/
class TwoFiltrationBridge where
  /-- Iterated-integral depth-lift $d_{\mathrm{II}}(\lambda)$ of the
      central idempotent $e_\lambda$ (the grouplike side). -/
  dII : YoungDiagram → ℕ
  /-- Predicate selecting the depth-3 chiral-pair period family. -/
  isChiralPair : YoungDiagram → Prop
  /-- **The conjecture** (depth-lift dichotomy, from the manuscript):
      a self-conjugate cell ($\mu^\top = \mu$) lifts to depth $2$ (real /
      Bloch–Wigner period), a chiral pair to depth $3$ (Tate-twisted
      period), and every other cell's lift is bounded by its concrete
      GB-depth `gbDepth μ` (max hook length). -/
  bridge : ∀ μ : YoungDiagram,
    (μ.transpose = μ → dII μ = 2) ∧
    (isChiralPair μ → dII μ = 3) ∧
    (μ.transpose ≠ μ → ¬ isChiralPair μ → dII μ ≤ gbDepth μ)

-- The conjecture itself.  The `sorry` represents the **open
-- conjecture** per §3b — not a missing proof.
-- Ref: [manuscript] quantum-observable-universe/mass-theory/two-filtration-bridge.ts

-- **No instance is provided — the honest open state** (AGENTS.md §3b-tax).
-- Previously: `axiom twoFiltrationBridge_conjecture` plus a global instance discharging `TwoFiltrationBridge` with it.
-- Consumers already declare `[TwoFiltrationBridge]`, so the global instance was silently
-- satisfying a hypothesis they had correctly written down.  Removed.

/-! ### What `gbDepth` actually grades — bean `wpdb`

`prf:phi-q-categorical-truncation` Step 3 and two sibling blocks use
`Z^(k)(A) = span{eλ : gbDepth λ = k}` as the centre's depth grading, citing
`prop:curvature-rank-gb-stratification` — which stratifies by the curvature
rank of **words** and mentions no partition. That bridge is stated nowhere
(audit: `docs/audits/2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated.md`).

This section does not close it. It measures the **partition side**, and what
it finds bears directly on the downstream use: the grading is far coarser than
its notation suggests, and at the strand count where the framework actually
consumes it, it is trivial.
-/

/-- **The GB-depth is the corner hook**, `λ₁ + λ'₁ - 1`.

The maximum over all cells is attained at `(0,0)`: rows and columns are
antitone, so every cell's arm and leg are dominated by the corner's. -/
theorem gbDepth_eq_corner (μ : YoungDiagram) (h : μ.cells.Nonempty) :
    gbDepth μ = μ.rowLen 0 + μ.colLen 0 - 1 := by
  apply le_antisymm
  · refine Finset.sup_le fun c _ => ?_
    unfold TwoFiltrationBridge.hookLength
    have h1 : μ.rowLen c.1 - c.2 ≤ μ.rowLen 0 :=
      (Nat.sub_le _ _).trans (rowLen_anti μ 0 c.1 (Nat.zero_le _))
    have h2 : μ.colLen c.2 - c.1 ≤ μ.colLen 0 :=
      (Nat.sub_le _ _).trans (colLen_anti μ 0 c.2 (Nat.zero_le _))
    omega
  · obtain ⟨c, hc⟩ := h
    have hmem : ((0 : ℕ), (0 : ℕ)) ∈ μ.cells :=
      μ.up_left_mem (Nat.zero_le _) (Nat.zero_le _) hc
    simpa [TwoFiltrationBridge.hookLength] using
      Finset.le_sup (f := fun c => TwoFiltrationBridge.hookLength μ c) hmem

/-- **The grading is blind to the interior.** Two diagrams sharing a first row
and a first column have the same GB-depth however differently they are shaped
below and to the right of the corner — an immediate consequence of
`gbDepth_eq_corner`, and the reason the stratification is coarse. -/
theorem gbDepth_eq_of_border_eq (μ ν : YoungDiagram)
    (hμ : μ.cells.Nonempty) (hν : ν.cells.Nonempty)
    (hrow : μ.rowLen 0 = ν.rowLen 0) (hcol : μ.colLen 0 = ν.colLen 0) :
    gbDepth μ = gbDepth ν := by
  rw [gbDepth_eq_corner μ hμ, gbDepth_eq_corner ν hν, hrow, hcol]

/-- A diagram that is not a hook — one containing `(1,1)` — has at least four
cells. So every partition of `n ≤ 3` is a hook, which is what makes the
`H₃` computation below come out constant. -/
theorem four_le_card_of_mem_one_one (μ : YoungDiagram) (h : (1, 1) ∈ μ) :
    4 ≤ μ.cells.card := by
  have h00 : ((0 : ℕ), (0 : ℕ)) ∈ μ.cells := μ.up_left_mem (by omega) (by omega) h
  have h01 : ((0 : ℕ), (1 : ℕ)) ∈ μ.cells := μ.up_left_mem (by omega) (by omega) h
  have h10 : ((1 : ℕ), (0 : ℕ)) ∈ μ.cells := μ.up_left_mem (by omega) (by omega) h
  have hsub : ({(0,0), (0,1), (1,0), (1,1)} : Finset (ℕ × ℕ)) ⊆ μ.cells := by
    intro x hx
    fin_cases hx <;> assumption
  calc (4 : ℕ) = ({(0,0), (0,1), (1,0), (1,1)} : Finset (ℕ × ℕ)).card := by decide
    _ ≤ μ.cells.card := Finset.card_le_card hsub

section H3

private theorem colLen_ofRowLens {w : List ℕ} (hw : List.Sorted (· ≥ ·) w)
    (hpos : ∀ x ∈ w, 0 < x) : (ofRowLens w hw).colLen 0 = w.length := by
  rw [← length_rowLens, rowLens_ofRowLens_eq_self hpos]

private theorem rowLen_ofRowLens {w : List ℕ} (hw : List.Sorted (· ≥ ·) w)
    (hpos : ∀ x ∈ w, 0 < x) (h : 0 < w.length) :
    (ofRowLens w hw).rowLen 0 = w[0]'h := by
  have hl : (0 : ℕ) < (ofRowLens w hw).rowLens.length := by
    rw [rowLens_ofRowLens_eq_self hpos]; exact h
  have := @get_rowLens (ofRowLens w hw) 0 hl
  rw [← this]
  simp [rowLens_ofRowLens_eq_self hpos]

private theorem cells_ne {w : List ℕ} (hw : List.Sorted (· ≥ ·) w)
    (hpos : ∀ x ∈ w, 0 < x) (h : 0 < w.length) :
    (ofRowLens w hw).cells.Nonempty := by
  refine ⟨(0, 0), ?_⟩
  have : (ofRowLens w hw).colLen 0 = w.length := colLen_ofRowLens hw hpos
  have hcol : 0 < (ofRowLens w hw).colLen 0 := by omega
  simpa using (mem_iff_lt_colLen).mpr hcol

/-- The three partitions of `3` — the `H₃` Wedderburn blocks of a single
nucleon (`schur-weyl-mass-decomposition`: symmetric, standard, antisymmetric). -/
def p3 : YoungDiagram := ofRowLens [3] (by decide)
def p21 : YoungDiagram := ofRowLens [2, 1] (by decide)
def p111 : YoungDiagram := ofRowLens [1, 1, 1] (by decide)

theorem gbDepth_p3 : gbDepth p3 = 3 := by
  rw [p3, gbDepth_eq_corner _ (cells_ne _ (by decide) (by decide)),
      rowLen_ofRowLens _ (by decide) (by decide), colLen_ofRowLens _ (by decide)]
  decide

theorem gbDepth_p21 : gbDepth p21 = 3 := by
  rw [p21, gbDepth_eq_corner _ (cells_ne _ (by decide) (by decide)),
      rowLen_ofRowLens _ (by decide) (by decide), colLen_ofRowLens _ (by decide)]
  decide

theorem gbDepth_p111 : gbDepth p111 = 3 := by
  rw [p111, gbDepth_eq_corner _ (cells_ne _ (by decide) (by decide)),
      rowLen_ofRowLens _ (by decide) (by decide), colLen_ofRowLens _ (by decide)]
  decide

/-- **At `n = 3` the partition grading has exactly one stratum.**

All three `H₃` blocks have GB-depth `3`, so `Z(H₃) = Z^(3)` and every other
stratum is zero.

The downstream consequence is the point. `prop:phi-q-categorical-truncation`
sets `k⋆(T_w) := max {gbDepth λ : λ ∈ supp(T_w)}` and states that the
truncation depth is *"structurally locked to the NF support of `T_w`"*. At
`n = 3` that maximum is `3` for **every** `T_w` with nonempty support — it is
constant, so it locks onto nothing. Whatever the truncation claim is worth at
the single-nucleon level, it is not carried by the support.

Scope-(a): this says the grading is degenerate here, not that the truncation
is false. It becomes non-trivial from `n = 4`, where `(2,2)` has depth `3`
against `4` for the four hooks. -/
theorem gbDepth_const_on_H3 :
    gbDepth p3 = gbDepth p21 ∧ gbDepth p21 = gbDepth p111 :=
  ⟨by rw [gbDepth_p3, gbDepth_p21], by rw [gbDepth_p21, gbDepth_p111]⟩

/-- Two partitions of `4`, chosen because this is where the grading first
separates: `[4]` has corner hook `4`. -/
def p4 : YoungDiagram := ofRowLens [4] (by decide)

/-- The self-conjugate `(2,2)` cell — the one the compute script flags as where
the two filtrations were observed to disagree. Corner hook `3`. -/
def p22 : YoungDiagram := ofRowLens [2, 2] (by decide)

theorem gbDepth_p4 : gbDepth p4 = 4 := by
  rw [p4, gbDepth_eq_corner _ (cells_ne _ (by decide) (by decide)),
      rowLen_ofRowLens _ (by decide) (by decide),
      colLen_ofRowLens _ (by decide)]
  decide

theorem gbDepth_p22 : gbDepth p22 = 3 := by
  rw [p22, gbDepth_eq_corner _ (cells_ne _ (by decide) (by decide)),
      rowLen_ofRowLens _ (by decide) (by decide),
      colLen_ofRowLens _ (by decide)]
  decide

/-- **At `n = 4` the partition grading has at least two strata.**

The counterpart to `gbDepth_const_on_H3`: the grading is degenerate at `n = 3`
and non-degenerate at `n = 4`. That is what makes `n = 4` the first place any
candidate word-side filtration can be tested against it — and, via
`WordFiltrationObstruction`, the first place the naive ideal-power reading is
provably not it. -/
theorem gbDepth_ne_on_H4 : gbDepth p4 ≠ gbDepth p22 := by
  rw [gbDepth_p4, gbDepth_p22]; decide

end H3

/-! ### `gbDepth` is the content spread — the form the algebra side can meet

`gbDepth_eq_corner` says the depth is `λ₁ + λ'₁ - 1`. That is a statement about
the *shape*'s bounding arms, and nothing in it speaks the language of
`H_n(R, q)`. This section rewrites it in a form that does.

The **content** of a cell `(i, j)` is `j - i`, its diagonal. Contents are what
the Jucys–Murphy elements measure: `L_k` acts on the `λ`-isotypic component by
the content of the cell added at step `k`, and the centre of `H_n(R, q)` is
generated by symmetric functions in the `L_k`. So a statement about contents is
a statement the centre can hear; one about hook maxima is not.

`gbDepth_eq_content_spread` below says the two coincide: **the GB-depth is the
number of distinct diagonals `λ` meets.** That does not close the word-depth ↔
partition-depth bridge (bean `wpdb`) — it relocates the partition side onto the
axis the algebra side is indexed by, which is what a proof would have to match.
-/

/-! The content, its extremes, and the corner-positivity lemmas were originally
defined **locally here** — a sixth copy of a one-line definition already present
five times in the tree. Worse, the spelling chosen to dodge a shadowing problem
(`cellContent`, so as not to occupy the bare `QOU.BraidKnot.content` slot that
`open QOU.BraidKnot` would shadow) collided head-on with
`QOU.BraidKnot.cellContent` in the standalone sibling
`mass-theory/jucys-murphy-central-elements-qou.lean`: the *same* fully-qualified
name at an incompatible signature. Shadowing is a readability hazard; a
duplicate declaration is a hard error the moment anything imports both. The
rename traded down.

Both are now gone: this file imports
[`QOU.MathlibExt.YoungDiagramCells`](../MathlibExt/YoungDiagramCells.lean) and
uses its `content` / `sup_content` / `inf_content` / `rowLen0_pos` /
`colLen0_pos`. That module is the single home for the nine copies (bean
`qou-cdup`); this is the first migration onto it. -/

open QOU.MathlibExt.YoungDiagramCells (content sup_content inf_content
  rowLen0_pos colLen0_pos)

/-- **The GB-depth counts the diagonals `λ` meets.**

`gbDepth μ = (max content − min content) + 1`. Since the contents of a Young
diagram fill the whole range between their extremes — the first row supplies
`0 … λ₁-1` and the first column `-(λ'₁-1) … 0` — this is exactly the number of
distinct contents.

This is the same number as the corner hook, said in the algebra's coordinates
rather than the diagram's. -/
theorem gbDepth_eq_content_spread (μ : YoungDiagram) (h : μ.cells.Nonempty) :
    (gbDepth μ : ℤ) = μ.cells.sup' h content - μ.cells.inf' h content + 1 := by
  rw [sup_content h, inf_content h, gbDepth_eq_corner μ h]
  have hr := rowLen0_pos h
  have hc := colLen0_pos h
  omega

/-- The contents of `λ` are exactly the integers `j - (λ'₁ - 1)` for
`0 ≤ j < gbDepth λ` — an unbroken interval, no gaps.

Both inclusions are cheap and neither is vacuous. Forward: every cell's content
lies between `-(λ'₁-1)` and `λ₁-1` because its row and column lengths are
dominated by the corner's. Backward: a non-negative target is hit by a cell of
the *first row* and a negative one by a cell of the *first column*, and the
bound `j < λ₁+λ'₁-1` is exactly what puts the witness inside the diagram. -/
theorem content_image_eq_range (μ : YoungDiagram) (h : μ.cells.Nonempty) :
    μ.cells.image content
      = (Finset.range (gbDepth μ)).image (fun j : ℕ => (j : ℤ) - ((μ.colLen 0 : ℤ) - 1)) := by
  have hr := rowLen0_pos (μ := μ) h
  have hc := colLen0_pos (μ := μ) h
  have hgb : gbDepth μ = μ.rowLen 0 + μ.colLen 0 - 1 := gbDepth_eq_corner μ h
  ext x
  simp only [Finset.mem_image, Finset.mem_range]
  constructor
  · rintro ⟨c, hcm, rfl⟩
    have hj : c.2 < μ.rowLen 0 :=
      lt_of_lt_of_le ((YoungDiagram.mem_iff_lt_rowLen).mp hcm)
        (YoungDiagram.rowLen_anti μ 0 c.1 (Nat.zero_le _))
    have hi : c.1 < μ.colLen 0 :=
      lt_of_lt_of_le ((YoungDiagram.mem_iff_lt_colLen).mp hcm)
        (YoungDiagram.colLen_anti μ 0 c.2 (Nat.zero_le _))
    refine ⟨c.2 + μ.colLen 0 - 1 - c.1, by omega, ?_⟩
    unfold content; omega
  · rintro ⟨j, hj, rfl⟩
    rcases le_or_gt (μ.colLen 0 - 1) j with hcase | hcase
    · -- non-negative content: witness on the first row
      refine ⟨((0 : ℕ), j - (μ.colLen 0 - 1)), (YoungDiagram.mem_iff_lt_rowLen).mpr (by omega), ?_⟩
      unfold content; omega
    · -- negative content: witness on the first column
      refine ⟨((μ.colLen 0 - 1) - j, (0 : ℕ)), (YoungDiagram.mem_iff_lt_colLen).mpr (by omega), ?_⟩
      unfold content; omega

/-- **The GB-depth counts the *distinct contents* `λ` carries.**

Stated on the image rather than on the extremes, because that is the form the
algebra side has to match: the JM eigenvalues are a *set*, one per content, and
what a bridge would have to reproduce is its cardinality. See
`card_eigen_image` below. -/
theorem card_content_image (μ : YoungDiagram) (h : μ.cells.Nonempty) :
    (μ.cells.image content).card = gbDepth μ := by
  rw [content_image_eq_range μ h,
    Finset.card_image_of_injective _ (fun a b hab => by omega), Finset.card_range]

/-! ### The algebraic restatement, conditional on the seminormal eigenvalue GAP -/

/-- **The seminormal eigenvalue theorem, carried as a §3b-cond hypothesis.**

The content is: the Jucys–Murphy element `L_k` acts on the seminormal basis of
the `λ`-block by a scalar depending only on the content of the cell added at
step `k` — `q^{2c}` in the QOU convention — and that assignment is injective at
generic `q`. This is **not proved in the corpus**: `QJucysMurphy.lean` records it
as an open GAP (Ref: [ram1997] Thm 4.1, [murphy1992], [hoefsmit1974]).

Per §3b-cond the class carries the *hypotheses*, never the conclusion. The two
fields are the eigenvalue assignment and its injectivity; `card_eigen_image`
below **derives** the count from them rather than asserting it. Discharging this
class is option A of bean `wpdb` and would make the results downstream of it
unconditional; it is deliberately left without an instance, which is the honest
representation of an open statement. -/
class SeminormalEigenvalue (K : Type*) where
  /-- The eigenvalue `L_k` acts by, as a function of the added cell's content. -/
  eigenOfContent : ℤ → K
  /-- At generic `q` the assignment `c ↦ q^{2c}` separates contents. -/
  eigenOfContent_injective : Function.Injective eigenOfContent

variable {K : Type*} [SeminormalEigenvalue K] [DecidableEq K]

/-- The Jucys–Murphy eigenvalue attached to a cell. -/
def eigen (c : ℕ × ℕ) : K := SeminormalEigenvalue.eigenOfContent (content c)

/-- The `λ`-block carries as many distinct JM eigenvalues as `λ` has contents.

Pure consequence of injectivity — the eigenvalue map does not collapse any two
diagonals — so nothing about `H_n(q)` is smuggled in beyond the class fields. -/
theorem card_eigen_image (μ : YoungDiagram) :
    (μ.cells.image (eigen (K := K))).card = (μ.cells.image content).card := by
  have himg : μ.cells.image (eigen (K := K))
      = (μ.cells.image content).image SeminormalEigenvalue.eigenOfContent := by
    rw [Finset.image_image]; rfl
  rw [himg,
    Finset.card_image_of_injective _ SeminormalEigenvalue.eigenOfContent_injective]

/-- **`gbDepth λ` is the number of distinct JM eigenvalues on the `λ`-block** —
conditional on `SeminormalEigenvalue`.

This is the partition side of bean `wpdb` said entirely inside the algebra: no
diagram, no hook, no cell. It is *not* the bridge — the word side is still
unrelated to it — but it is the shape the word side would have to match, and it
localises the whole remaining partition-side debt in one named open class. -/
theorem gbDepth_eq_card_eigen (μ : YoungDiagram) (h : μ.cells.Nonempty) :
    (μ.cells.image (eigen (K := K))).card = gbDepth μ := by
  rw [card_eigen_image, card_content_image μ h]

/-! ### Where this stops, and why

The natural next step is to read the content spread back inside the algebra.
The Jucys–Murphy element `L_k` acts on the seminormal basis with eigenvalue
`q^{2c(k)}` (QOU convention, `QOU/SchurWeyl/QJucysMurphy.lean`), and `c ↦ q^{2c}`
is injective at generic `q`, so

  gbDepth λ  =  #{ distinct JM eigenvalues on the λ-block }

would be an *intrinsically algebraic* restatement — no diagram, no hook — and
that is the shape the word side would have to match.

**It is not provable here, and the obstruction is not this file's.** The
seminormal eigenvalue statement is itself an open GAP in the corpus:
`QJucysMurphy.lean` records *"Seminormal eigenvalue — GAP: `L_k` acts with
eigenvalue `q^{2c(k)}` on the seminormal basis"* (Ref: [ram1997] Thm 4.1,
[murphy1992], [hoefsmit1974]), and the block-eigenvalue statement is a further
GAP downstream of it.

So the bridge bottoms out in an already-known gap rather than in a new one.
Closing it needs the seminormal eigenvalue theorem first — after which the
identity above should follow from `gbDepth_eq_content_spread` plus injectivity
of `c ↦ q^{2c}`, and the remaining question becomes the well-definedness of the
word filtration (bean `wpdb`).
-/

end QOU.BraidKnot
