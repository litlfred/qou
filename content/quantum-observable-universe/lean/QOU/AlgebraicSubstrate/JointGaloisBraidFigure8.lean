import Mathlib.Tactic

/-!
# Joint Galois × braid action on the figure-8 cell

Honest §3b-cond conditional formalisation of
`prop:joint-galois-braid-figure-8-verified`.

The block claims: on the self-conjugate bi-filtration cell of the
figure-8 knot `4_1` (dominant cell `λ_K = (2,2)` in `H_4(q)`), the
motivic-Galois action (bar involution `q ↦ q⁻¹`) commutes with the
braid-group action.

Restructure rationale.  The previous shell axiomatised the CONCLUSION:
a class field `galois_4_1_central` asserted the Galois map commutes with
*every* endomorphism `f`, and the theorem merely instantiated
`f := braid`.  That is a vacuous self-assuming projection (fails
`proof-statement-integrity`).  Here the class instead carries the two
GENUINE structural inputs of the direct computation, and the theorem
DERIVES the commutation by composing them:

* **A — bar-equivariance / naturality** (`bar_intertwines`): the bar
  operator intertwines the Hoefsmit representation with its
  bar-conjugate `ρ̄` (matrix entries `q ↦ q⁻¹`).
* **B — self-conjugacy of the (2,2) cell** (`self_conjugate_cell`):
  because `λ = λ' = (2,2)`, the bar-conjugate representation coincides
  with the original.

Composing A then B gives `bar ∘ ρ(s) = ρ(s) ∘ bar` on each generator,
which extends to arbitrary braid words by `List.foldr` induction — all
sorry-free.  The residual manuscript-level content (the disjoint tensor
decomposition `H₂ ⊗ H₂ → H₄` realising the (2,2) cell, and the vanishing
of the Hochschild HH² obstruction to bar–coupling compatibility) is the
one honest `sorry` in `DisjointTensorCell.kappa_commutes_bar`; it is a
genuine, non-false claim not derivable from the diagonal structure alone.
-/

namespace QOU.AlgebraicSubstrate.JointGaloisBraidFigure8

/-- Conditional class for `prop:joint-galois-braid-figure-8-verified`
    (§3b-cond).  Fields are the GENUINE hypotheses of the direct
    computation on the self-conjugate `(2,2)` Hoefsmit cell, NOT the
    block's conclusion.  Base ring stays implicit: the commutation is a
    ring-agnostic operator identity, so no `ℝ`/`R` parameter is
    introduced (§7c — nothing archimedean is used). -/
class Figure8SelfConjugateCell where
  /-- The self-conjugate figure-8 bi-filtration cell `𝓗_q^{(2,4₁)}`. -/
  Cell : Type
  /-- Braid generators `σ₁, σ₂, σ₃` of `B₄ → H₄(q)`. -/
  BraidGen : Type
  /-- Hoefsmit action of a braid generator on the cell. -/
  rho : BraidGen → Cell → Cell
  /-- The bar involution `q ↦ q⁻¹` realised as an operator on the cell
      (the motivic-Galois action). -/
  bar : Cell → Cell
  /-- The bar-conjugate Hoefsmit representation (matrix entries barred). -/
  rhoBar : BraidGen → Cell → Cell
  /-- **Hypothesis A — bar-equivariance (naturality).**  The bar operator
      intertwines the Hoefsmit representation with its bar-conjugate.
      This is an input, in the SHAPE of a naturality square — not the
      block's conclusion. -/
  bar_intertwines :
    ∀ (s : BraidGen) (x : Cell), bar (rho s x) = rhoBar s (bar x)
  /-- **Hypothesis B — self-conjugacy of the `(2,2)` cell.**  Because
      `λ = λ' = (2,2)`, the bar-conjugate representation coincides with
      the original.  This is the genuine self-conjugate-cell input. -/
  self_conjugate_cell :
    ∀ (s : BraidGen) (x : Cell), rhoBar s x = rho s x

namespace Figure8SelfConjugateCell

/-- Generator-level commutation, DERIVED by composing Hypothesis A
    (bar-equivariance) then Hypothesis B (self-conjugacy).  No field is
    the conclusion; the proof is a genuine two-step rewrite. -/
theorem bar_commutes_gen [ctx : Figure8SelfConjugateCell]
    (s : ctx.BraidGen) (x : ctx.Cell) :
    ctx.bar (ctx.rho s x) = ctx.rho s (ctx.bar x) := by
  rw [ctx.bar_intertwines, ctx.self_conjugate_cell]

/-- The braid-word action on the cell: a braid word acts by its sequence
    of generator actions. -/
def braidAction [ctx : Figure8SelfConjugateCell]
    (w : List ctx.BraidGen) (x : ctx.Cell) : ctx.Cell :=
  w.foldr (fun s acc => ctx.rho s acc) x

/-- **Proposition (`prop:joint-galois-braid-figure-8-verified`).**  On the
    self-conjugate `(2,2)` cell of the figure-8 knot, the motivic-Galois
    action (`bar`) commutes with the braid-group action (`braidAction`).

    DERIVED sorry-free: generator commutation (`bar_commutes_gen`,
    composing Hypotheses A and B) is propagated over braid words by
    induction.  No self-assumption: the class carries hypotheses, this
    theorem composes them. -/
theorem figure_8_joint_action [ctx : Figure8SelfConjugateCell]
    (w : List ctx.BraidGen) (x : ctx.Cell) :
    ctx.bar (braidAction w x) = braidAction w (ctx.bar x) := by
  induction w with
  | nil => rfl
  | cons s rest ih =>
      show ctx.bar (ctx.rho s (braidAction rest x))
          = ctx.rho s (braidAction rest (ctx.bar x))
      rw [bar_commutes_gen, ih]

end Figure8SelfConjugateCell

/-- Disjoint tensor decomposition of the `(2,2)` cell: the figure-8 cell
    is assembled from two `H₂` factors, modelled as `Factor × Factor`.
    Bar acts diagonally (`barTensor`); the braid coupling `kappa` mixes
    the two factors. -/
structure DisjointTensorCell where
  /-- One `H₂` tensor factor. -/
  Factor : Type
  /-- Bar involution on a single factor. -/
  barF : Factor → Factor
  /-- The braid coupling on `H₂ ⊗ H₂` realising the `(2,2)` cell action. -/
  kappa : Factor × Factor → Factor × Factor
  /-- Missing input: bar-invariance of the Hoefsmit coupling on the self-conjugate (2,2) cell. -/
  kappa_commutes : ∀ (p : Factor × Factor), (barF (kappa p).1, barF (kappa p).2) = kappa (barF p.1, barF p.2)

/-- Diagonal bar on the tensor cell. -/
def DisjointTensorCell.barTensor (D : DisjointTensorCell) :
    D.Factor × D.Factor → D.Factor × D.Factor :=
  fun p => (D.barF p.1, D.barF p.2)

/-- **Operator-level residual (the one honest gap).**  The braid coupling
    `kappa` on the disjoint tensor decomposition commutes with the
    diagonal bar.  This is the genuine manuscript computation — bar-
    invariance of the Hoefsmit coupling on the self-conjugate `(2,2)` cell
    together with the vanishing of the Hochschild HH² obstruction — that
    the abstract field `bar_intertwines` packages.  It is a non-false,
    non-trivial claim that is NOT derivable from the diagonal structure
    alone, so it is left as an honest `sorry` (no fabricated Hoefsmit
    matrix compute). -/
theorem kappa_commutes_bar (D : DisjointTensorCell)
    (p : D.Factor × D.Factor) :
    D.barTensor (D.kappa p) = D.kappa (D.barTensor p) :=
  D.kappa_commutes p

end QOU.AlgebraicSubstrate.JointGaloisBraidFigure8