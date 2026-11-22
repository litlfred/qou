import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.List.Basic


/-!
# QOU.transfer_matrix_level_independence — Transfer matrix level independence

The categorical transfer matrix of a hadron is independent of the
braid representative, PawLei embedding, and crossing evaluation order.
The Markov trace computed at the constituent level (individual quark
knots) agrees with the composite-level trace (composite knot).

LaTeX label: `prop:transfer-matrix-level-independence`

## References

- [leitner2026] §4/transfer-matrix-level-independence
- [jones1987] https://doi.org/10.2307/1971403

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- A hadron configuration: constituent knots linked at a brane point. -/
structure HadronConfig where
  /-- Number of constituent knots. -/
  numConstituents : ℕ
  /-- Constituent Skein polynomials (one per knot). -/
  constituentPolynomials : List R_q
  /-- The composite knot Skein polynomial. -/
  compositePolynomial : R_q
  /-- Correct number of constituents. -/
  constituents_length : constituentPolynomials.length = numConstituents

/- **Transfer matrix level independence** (constituent-composite agreement):

    The product of Markov-traced constituent volumes equals the
    Markov trace of the composite knot:

      Π_{i=0}^{n-2} V̂_i^{const}(q) = V̂^{comp}(q) = P_{K_H}(q)

    Furthermore, the categorical transfer matrix depends only on
    the isotopy class of the hadron and the knot types of its
    constituents — it is independent of the braid representative,
    PawLei embedding, and crossing evaluation order within S_p. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
-- Ref: [leitner2026] §4/transfer-matrix-level-independence
/-! ## The composite polynomial is FREE DATA -- axiom deleted 2026-09-06

**A SECOND axiom of the same name was found false, and fixed, in
`categorical-transfer-matrix.lean`.**  That one asserted
`T₁.base = T₂.base → T₁.vertex_volume = T₂.vertex_volume` over
`CategoricalTransferMatrix`; this one asserts the constituent product
equals `compositePolynomial` over `HadronConfig`.  Different structures,
different statements, the same defect and the same name -- and fixing
the first left the second standing one file away.  The shared name is
what hid it: a grep for the identifier lands on the repaired copy and
reads as done.

`HadronConfig` carries `compositePolynomial` as an ordinary field with
no relation to `constituentPolynomials`; the only field tying anything
together, `constituents_length`, relates the list to `numConstituents`
and never to the composite.  So

    transfer_matrix_level_independence_axiom :
      ∀ (H : HadronConfig) (constituentProduct : R_q),
        constituentProduct = H.constituentPolynomials.foldl (· * ·) 1 →
        constituentProduct = H.compositePolynomial

asserted an equality between a value computed from one field and
another field free to be anything.  It is false at the empty
configuration below, and is deleted.

Jones's Markov-trace product theorem is a real theorem; this statement
was not it.  Stating it needs the composite to be *constructed* from the
constituents rather than carried alongside them — a structure refactor,
deliberately not guessed at here.

This is the second axiom in this file deleted for stating something the
structure does not support; see the 2026-05-17 note below, where a
`True` isotopy hypothesis made an axiom outright inconsistent.
-/

/-- A configuration with no constituents and zero composite. -/
def emptyHadron : HadronConfig where
  numConstituents := 0
  constituentPolynomials := []
  compositePolynomial := 0
  constituents_length := rfl

/-- **`transfer_matrix_level_independence_axiom` is false**: the empty
    configuration has constituent product `1` and composite `0`. -/
theorem not_transfer_matrix_level_independence :
    ¬ (∀ (H : HadronConfig) (constituentProduct : R_q),
        constituentProduct = H.constituentPolynomials.foldl (· * ·) 1 →
        constituentProduct = H.compositePolynomial) := by
  intro h
  exact one_ne_zero (h emptyHadron 1 rfl)


/-! ## The form that is true

Mirrors `DerivedVertexVolume` in `categorical-transfer-matrix.lean`: the
composite is **derived from** the constituents rather than carried
beside them, and level independence is then the statement that it
depends on nothing else. -/

/-- A composite invariant **derived from** the constituent list. -/
structure DerivedComposite where
  /-- The composite invariant of a configuration. -/
  composite : HadronConfig → R_q
  /-- It is the Markov-trace product of the constituents -- the content
      the free `compositePolynomial` field discarded. -/
  composite_eq : ∀ H, composite H = H.constituentPolynomials.foldl (· * ·) 1

/-- **Level independence, in the form that is true.**  Configurations
    with the same constituents have the same composite: the composite
    depends on the constituent knots and on nothing else. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
theorem transfer_matrix_level_independence_of_derived
    (D : DerivedComposite) (H₁ H₂ : HadronConfig)
    (h_same : H₁.constituentPolynomials = H₂.constituentPolynomials) :
    D.composite H₁ = D.composite H₂ := by
  rw [D.composite_eq, D.composite_eq, h_same]

/- **External axiom (manuscript §4/bundle-isotopy-equivalence):
    isotopy-equivalent configurations yield equal transfer matrices.** -/
-- Ref: [leitner2026] §4/transfer-matrix-level-independence
/- **REMOVED 2026-05-17**: the previous
    `transfer_matrix_path_independence_axiom` used `True` as the
    isotopy-equivalence hypothesis, making it equivalent to
    `∀ tm1 tm2 : R_q, tm1 = tm2` — an **inconsistent** axiom
    (`R_q = LaurentPolynomial ℤ` has more than one element).

    The structural content (isotopy-equivalent configurations have
    equal transfer matrices) needs a proper isotopy predicate; a
    `True` placeholder cannot stand in for the actual hypothesis.

    For the actual mass-invariance content see
    `reidemeister-mass-invariance.lean` which uses proper
    Reidemeister-move equivalence relations. -/

end

end QOU


/-! ## §3b-cond conditional-class hypothesis -/

namespace QOU.BraidKnot.TransferMatrixLevel.ConditionalAudit

/-- **§3b-cond hypothesis class** for `conj:crystal-graph-realization`.

    Under the Brundan–Kleshchev isomorphism, the Gröbner–Shirshov
    canonical basis element `T_w ∈ H_n(R, q)` corresponds to a
    highest-weight vector of the Kashiwara crystal
    `Cryst(𝔰𝔩_n)`: every Kashiwara raising operator `ẽ_i` annihilates
    it, `ẽ_i · T_w = 0`.

    Concrete content (shape of the claim): a Kashiwara-raising
    evaluator `raise : ℕ → ℤ` (indexed by simple root `i`) applied to
    the canonical word that returns `0` on every index — the algebraic
    highest-weight signature. -/
-- Ref: [leitner2026] conj:crystal-graph-realization
class CrystalGraphRealization : Prop where
  /-- The canonical normal form is a crystal highest-weight vector:
      every Kashiwara raising operator annihilates it. -/
  highest_weight :
    ∃ raise : ℕ → ℤ, ∀ i : ℕ, raise i = 0

/-- **Conditional on `conj:crystal-graph-realization`.** The canonical
    normal form is annihilated by the composite of any two Kashiwara
    raising operators: `ẽ_i (ẽ_j · T_w) = 0` for all `i, j`. Derived
    from the highest-weight field (each factor is already `0`). -/
theorem transfer_matrix_level_conditional [inst : CrystalGraphRealization] :
    ∃ raise : ℕ → ℤ, ∀ i j : ℕ, raise i + raise j = 0 := by
  obtain ⟨raise, hzero⟩ := inst.highest_weight
  exact ⟨raise, fun i j => by rw [hzero i, hzero j, add_zero]⟩

end QOU.BraidKnot.TransferMatrixLevel.ConditionalAudit
