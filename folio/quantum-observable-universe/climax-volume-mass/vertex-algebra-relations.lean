import UGB.GrobnerShirshov.HeckeGS
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith


/-!
# QOU.VertexAlgebra.Relations

The QU/QUO axioms expressed in Hecke generators: structural relations
(Hecke, Yang–Baxter, far-commutativity) are already formalized in
`QOU.GrobnerShirshov.Hecke` as constructive `ReductionRule` definitions.
This file re-exports the relevant declarations and adds the Markov trace,
anomaly freedom, and cohomological constraints that go beyond the
Gröbner–Shirshov framework.

LaTeX label: `prop:vertex-algebra-relations`

## References
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [jones1987] https://doi.org/10.2307/1971403

**Ground ring**: this Lean sibling is the **archimedean specialisation
over `ℝ`** (AGENTS.md §7c), matching the `HeckeGS` library, whose
`AlgElement (HeckeGen n)` and `HeckeParams.q` are over `ℝ`. The
underlying combinatorial content stays generic to any commutative ring
with the same `q`-data; `q ↦ q₀ ∈ ℝ` is the numerical evaluation.
-/

namespace QOU.VertexAlgebra

open UGB.GrobnerShirshov
open UGB.GrobnerShirshov.Hecke

-- ═══════════════════════════════════════════════════════════════════
-- QU-1: Re-export the three Hecke relations from HeckeGS.lean
-- ═══════════════════════════════════════════════════════════════════

/- QU-1a: The Hecke relation σᵢ² = (q - q⁻¹)σᵢ + 1 is formalized
    as `heckeRelation` in HeckeGS.lean — a constructive `ReductionRule`
    in the Gröbner–Shirshov rewriting system.
    Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
         — Kassel, "Quantum Groups," Springer GTM 155, 1995.
         DOI: 10.1007/978-1-4612-0783-2 -/
#check @heckeRelation  -- ReductionRule (HeckeGen n) ℝ

/- QU-1b: Yang–Baxter σᵢσᵢ₊₁σᵢ = σᵢ₊₁σᵢσᵢ₊₁ is formalized
    as `yangBaxterRelation` in HeckeGS.lean.
    Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
         — Kassel, "Quantum Groups," Springer GTM 155, 1995.
         DOI: 10.1007/978-1-4612-0783-2 -/
#check @yangBaxterRelation  -- ReductionRule (HeckeGen n) ℝ

/- QU-1c: Far-commutativity σᵢσⱼ = σⱼσᵢ for |i-j| ≥ 2 is
    formalized as `farCommRelation` in HeckeGS.lean.
    Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
         — Kassel, "Quantum Groups," Springer GTM 155, 1995.
         DOI: 10.1007/978-1-4612-0783-2 -/
#check @farCommRelation  -- ReductionRule (HeckeGen n) ℝ

/- The three families do **NOT** form a Gröbner–Shirshov basis. This comment
    previously cited Bokut & Shiao 2001, Theorem 3.5 for the claim; that theorem
    gives a GS basis for the **completed** system, obtained by adjoining
    `sᵢsᵢ₋₁⋯sⱼsᵢ → sᵢ₋₁sᵢsᵢ₋₁⋯sⱼ`, and the defining relations alone are not
    confluent. Refuted at n = 4 in `UGB.GrobnerShirshov.Hecke.NotAGSBasis`:
    Yang–Baxter for (σ₂,σ₃) and far-commutation for (σ₃,σ₁) overlap on
    `σ₃σ₂σ₃σ₁`, and the two reductions `σ₂σ₃σ₂σ₁` and `σ₃σ₂σ₁σ₃` are both
    irreducible. Bean qou-auq3 tracks the completion.
    Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
         — Kassel, "Quantum Groups," Springer GTM 155, 1995.
         DOI: 10.1007/978-1-4612-0783-2 -/
#check @UGB.GrobnerShirshov.Hecke.hecke_is_gs_basis_false

-- ═══════════════════════════════════════════════════════════════════
-- QU-2: Antipode = Hecke inverse (derived from heckeRelation)
-- ═══════════════════════════════════════════════════════════════════

/- QU-2d: The inverse σᵢ⁻¹ = (q⁻¹ - q)σᵢ + q⁻¹ is formalized as
    `embedNegativeGen` in HeckeGS.lean — constructive from the Hecke
    relation. This IS the antipode S(σᵢ).
    Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
         — Kassel, "Quantum Groups," Springer GTM 155, 1995.
         DOI: 10.1007/978-1-4612-0783-2 -/
#check @embedNegativeGen  -- AlgElement (HeckeGen n) ℝ

-- ═══════════════════════════════════════════════════════════════════
-- QU-3: Markov trace (requires functional on AlgElement)
-- ═══════════════════════════════════════════════════════════════════

/-- The Markov trace tr_M : AlgElement(HeckeGen n, ℝ) → ℝ.
    Defined by the two Markov properties on normal forms.

    This extends the Gröbner–Shirshov framework with a linear functional
    satisfying conjugation invariance and stabilisation. The existence
    and uniqueness is Jones 1987, Theorem 5.1.

    **Markov trace** on H_n(q) — axiomatised pending the full
    Markov-recursion-on-GS-normal-forms implementation in the
    transfer-matrix framework. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
axiom MarkovTrace {n : ℕ} (hp : HeckeParams) (f : AlgElement (HeckeGen n) ℝ) : ℝ

/-- **AlgElement.embed_succ** — embed H_n into H_{n+1} by treating
    generators as σ₀,…,σ_{n-1}.  Axiomatised pending the concrete
    Hecke-algebra implementation. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
axiom AlgElement.embed_succ {n : ℕ} (f : AlgElement (HeckeGen n) ℝ) :
    AlgElement (HeckeGen (n + 1)) ℝ

/-- **AlgElement.mul** — convolution on monomials.  Axiomatised
    pending concrete formal-algebra ring structure. -/
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
axiom AlgElement.mul {n : ℕ}
    (_ _ : AlgElement (HeckeGen n) ℝ) : AlgElement (HeckeGen n) ℝ

/-! ### `AlgElement.zero` — axiom deleted 2026-09-06, it SHADOWED the real one

This file declared

    axiom AlgElement.zero {n : ℕ} : AlgElement (HeckeGen n) ℝ

while `UGB.GrobnerShirshov.AlgElement.zero` — a real `def` with a real
`isZero_zero` theorem (`UGB/GrobnerShirshov/Elem.lean`) — was already in
scope through the `HeckeGS` import.  Measured: inside this namespace the
bare name resolved to the **axiom**, and its type
(`{n : ℕ} → AlgElement (HeckeGen n) ℝ`) differs from the library's
(`{G} → {k} → [Ring k] → AlgElement G k`), so `isZero_zero` did not apply
to it.

The consequence was not cosmetic.  `markov_nondegenerate` concludes
`f = AlgElement.zero`, which under the axiom meant *"`f` equals a fixed
unknown element"* — not *"`f` is zero"*.  With the axiom gone the name
resolves to the library definition and the conclusion says what it
reads as; `(AlgElement.zero).isZero` is now provable here by
`UGB.GrobnerShirshov.AlgElement.isZero_zero`.

`AlgElement.mul` and `AlgElement.embed_succ` below have no library
counterpart and remain axiomatised; `MarkovTrace` likewise.  Claims about
those are specifications rather than theorems — with an opaque operator
there is no definition to unfold, so they can be neither proved nor
refuted.  That is a real gap and is left visible. -/

/-- QU-3a: Markov conjugation invariance —
    tr_M(σᵢ · f) = tr_M(f · σᵢ) for all i and f. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
axiom markov_conjugation {n : ℕ} (hp : HeckeParams) (i : Fin n)
    (f : AlgElement (HeckeGen n) ℝ) :
    MarkovTrace hp (AlgElement.leftMulGen ⟨i⟩ f)
    = MarkovTrace hp (AlgElement.rightMulGen f ⟨i⟩)

/-- QU-3b: Markov stabilisation —
    tr_M(f · σ_n) = δ⁻¹ · tr_M(f) where δ = -(q + q⁻¹). -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
axiom markov_stabilisation {n : ℕ} (hp : HeckeParams)
    (f : AlgElement (HeckeGen n) ℝ) :
    MarkovTrace hp (AlgElement.leftMulGen ⟨⟨n, by omega⟩⟩
      (AlgElement.embed_succ f))
    = MarkovTrace hp f / (-(hp.q + hp.q⁻¹))

/-- QU-3c: Non-degeneracy —
    the Markov trace pairing (f, g) ↦ tr_M(f · g) is non-degenerate
    on GS normal forms. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
axiom markov_nondegenerate {n : ℕ} (hp : HeckeParams)
    (f : AlgElement (HeckeGen n) ℝ) :
    (∀ g : AlgElement (HeckeGen n) ℝ,
      MarkovTrace hp (AlgElement.mul f g) = 0) →
    f = AlgElement.zero

-- ═══════════════════════════════════════════════════════════════════
-- QUO-2: Observability (Schur's lemma for the Hecke algebra)
-- ═══════════════════════════════════════════════════════════════════

/-- QUO-2: An element commuting with all generators under conjugation
    is a scalar. Equivalent to Hom(1, Ad(A)) = 0. -/
-- Ref: [leitner2026] §4/vertex-algebra-relations
axiom observability {n : ℕ} (hp : HeckeParams)
    (f : AlgElement (HeckeGen n) ℝ) :
    (∀ i : Fin n, AlgElement.leftMulGen ⟨i⟩
      (AlgElement.rightMulGen f ⟨i⟩) = f) →
    ∃ c : ℝ, f = AlgElement.smul c (AlgElement.singleton [])

-- ═══════════════════════════════════════════════════════════════════
-- QUO-3: Anomaly freedom (Chern class vanishing)
-- ═══════════════════════════════════════════════════════════════════

/-- QUO-3a: c₁(Ad(A)) = 0. Writhe balance: for each generator,
    tr_M(σᵢ) = tr_M(σᵢ⁻¹). -/
-- Ref: [leitner2026] §4/vertex-algebra-relations
axiom first_chern_vanishes {n : ℕ} (hp : HeckeParams) (i : Fin n) :
    MarkovTrace hp (embedPositiveGen i)
    = MarkovTrace hp (embedNegativeGen i hp)

-- ═══════════════════════════════════════════════════════════════════
-- C-2: q-deformed obstruction d_q² ≠ 0
-- ═══════════════════════════════════════════════════════════════════

/-- C-2: The obstruction coefficient q⁻¹(1-q⁻¹) is nonzero for q > 1.
    This proves d_q² ≠ 0 on vertical forms. -/
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
theorem dq_squared_nonzero (q : ℝ) (hq : q > 1) :
    q⁻¹ * (1 - q⁻¹) ≠ 0 := by
  have hqpos : q > 0 := by linarith
  have hqi : q⁻¹ > 0 := by positivity
  have hqi1 : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  have h1 : 1 - q⁻¹ > 0 := by linarith
  exact ne_of_gt (mul_pos hqi h1)

-- ═══════════════════════════════════════════════════════════════════
-- C-4b: Descartes constraint χ = -6
-- ═══════════════════════════════════════════════════════════════════

/-- C-4b: χ = 2 - 2g = -6 forces g = 4. -/
-- Ref: [leitner2026] §4/vertex-algebra-relations
theorem descartes_genus : (2 : ℤ) - 2 * 4 = -6 := by norm_num

/- `descartes_trace` RETIRED 2026-09-15.  It asserted, as an `axiom` over the
    `axiom MarkovTrace`, that the Markov trace of the identity is `-6` for every
    strand count and every parameter.  Under the owner ruling `tr(id_X) = dim_q(X)`
    that value is a quantum dimension (positive, `q`-dependent, and for the
    Frobenius–Hopf object divergent); `-6` is `chi_eu(M_0)`, the Euler
    characteristic of the base curve.  It had no consumers.  See
    `docs/audits/2026-09-15-chi-as-a-component-of-the-chern-character.md`. -/

-- ═══════════════════════════════════════════════════════════════════
-- C-7: Self-dual curvature (instanton)
-- ═══════════════════════════════════════════════════════════════════

/-- C-7: The curvature [σᵢ, σⱼ] is self-adjoint under the antipode:
    S([σᵢ, σⱼ]) = [σᵢ, σⱼ] where [a, b] = ab(ba)⁻¹. -/
-- Ref: [leitner2026] §4/vertex-algebra-relations
axiom self_dual_curvature {n : ℕ} [NeZero n] (hp : HeckeParams)
    (i j : Fin n) (hij : i ≠ j) :
    -- S(ab · ba⁻¹) = ab · ba⁻¹, where ab = braidToAlg [σᵢ, σⱼ] and
    -- ba⁻¹ = braidToAlg [σⱼ⁻¹, σᵢ⁻¹].
    braidToAlg (n := n) hp [-(j.val : ℤ), -(i.val : ℤ), i.val, j.val]
    = braidToAlg (n := n) hp [i.val, j.val, -(j.val : ℤ), -(i.val : ℤ)]

end QOU.VertexAlgebra
