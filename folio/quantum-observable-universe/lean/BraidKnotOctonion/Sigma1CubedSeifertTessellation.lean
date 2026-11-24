/-!
# QOU.BraidKnot.Sigma1CubedSeifertTessellation

Pure **structural / combinatorial** facts about the σ₁³ (trefoil) Seifert
surface and the abelian shadow of its non-abelian Stokes surface term.

**Mathlib-free** (only `Init`; verified with `lean` directly, no olean
wall). Everything here is `decide`/`omega`/`rfl` on `Int`/`Nat`.

**Scope discipline (owner ruling 2026-08-02).** This file carries ONLY
derived structural facts — the Seifert CW cell count from Seifert's
algorithm and the abelianisation of the genus-1 surface relator. It does
**NOT** formalise, derive, or assert any numerical surface-term → binding
(C_knot = 5.853) connection: that connection is *empirical* and lives in
[`sigma1cubed_seifert_surface_term_probe.py`](../../../../../computations/deltalambda/sigma1cubed_seifert_surface_term_probe.py)
+ its witness, never a Lean proof.

Ref: [leitner2026] docs/audits/2026-08-02-sigma1cubed-seifert-surface-term-trace-cyclicity-prune.md;
Seifert's algorithm (standard). The observable-sector vanishing of the
surface-ordering defect is the corpus-proved `holonomy_perm`
(QOU.MathlibExt.YekutieliIntegration, CommMonoid permutation-invariance);
this file supplies its *abelianised combinatorial* shadow.
-/

namespace QOU.BraidKnot.Sigma1CubedSeifertTessellation

/-! ## 1. Seifert's algorithm on σ₁³ — the derived CW cell count

Seifert's algorithm on the standard σ₁³ diagram (2-strand braid, 3
positive crossings) yields **2** Seifert circles (⇒ 2 Seifert disks =
2-cells) joined by **3** twisted bands (one per crossing = 1-cells). These
counts are canonical (Seifert's algorithm has no free choice), so the
surface's Euler characteristic, genus and first-homology rank are derived,
not fitted. -/

/-- Number of Seifert disks (2-cells) from σ₁³: the 2 Seifert circles of a
2-strand braid. -/
def seifertDisks : Int := 2

/-- Number of twisted bands (1-cells): one per crossing of σ₁³. -/
def seifertBands : Int := 3

/-- Euler characteristic of the σ₁³ Seifert surface: `χ = #disks − #bands`
    (a 2-complex with `#disks` 2-cells glued along `#bands` 1-cells that
    connect the two disks; the standard band-surface CW count). -/
def seifertEuler : Int := seifertDisks - seifertBands

/-- **`χ = −1`** for the σ₁³ Seifert surface. -/
theorem seifertEuler_eq_neg_one : seifertEuler = -1 := by decide

/-- The surface has **one** boundary component (the knot σ₁³ closure is a
    knot, not a link). -/
def boundaryComponents : Int := 1

/-- Genus `g` of a connected surface with `b` boundary components satisfies
    `χ = 2 − 2g − b`. For the σ₁³ surface (`χ = −1`, `b = 1`) this pins
    `2g = 2 − b − χ = 2 − 1 − (−1) = 2`, i.e. `g = 1`. We record the genus
    and *verify the Euler relation closes* (the falsifiable content). -/
def seifertGenus : Int := 1

/-- **The Euler relation `χ = 2 − 2g − b` holds** for the derived counts —
    i.e. `g = 1` is forced by `χ = −1`, `b = 1`. This is the genuine check
    (had the cell count been wrong, this would fail). -/
theorem seifert_euler_relation :
    seifertEuler = 2 - 2 * seifertGenus - boundaryComponents := by decide

/-- First-homology rank of a genus-`g` surface with one boundary component
    is `2g`. -/
def rankH1 : Int := 2 * seifertGenus

/-- **`rank H₁ = 2`**: two handle generators `a₁, b₁`. -/
theorem rankH1_eq_two : rankH1 = 2 := by decide

/-! ## 2. The genus-1 surface relator is a single commutator, and its
    abelian shadow vanishes

For a genus-1 surface with one boundary component the fundamental-group
relation is `∂ = [a₁, b₁] = a₁ b₁ a₁⁻¹ b₁⁻¹` — a **single commutator** of
the two handle holonomies. The non-abelian Stokes theorem assigns exactly
this object (the surface-ordered curvature integral) to the surface.

Its **abelianisation** — the exponent-sum in each generator — is `(0, 0)`:
the abelian (unordered) holonomy of the surface term is trivial. This is
the combinatorial shadow of `holonomy_perm` / trace-cyclicity `tr[A,B]=0`:
the surface-ordering correction contributes nothing to any abelian /
character functional. -/

/-- Exponent-sum of the commutator word `[a,b] = a b a⁻¹ b⁻¹` in the `a`
    generator: `(+1) + (−1) = 0`. -/
def relatorExponentA : Int := 1 + (-1)

/-- Exponent-sum in the `b` generator: `(+1) + (−1) = 0`. -/
def relatorExponentB : Int := 1 + (-1)

/-- **The genus-1 surface relator abelianises to `(0,0)`.** Hence the
    abelian shadow of the NA-Stokes surface term is the identity: it adds
    nothing to any abelian/character-level functional (the combinatorial
    face of the trace-cyclicity prune). -/
theorem relator_abelianises_to_zero :
    relatorExponentA = 0 ∧ relatorExponentB = 0 := by decide

/-! ## 3. Symmetrized Seifert form — the canonical linking data (`det = 3`)

The Seifert matrix of σ₁³ (genus-1) is `V = [[-1, 1], [0, -1]]`; the
symmetrized form `V + Vᵀ = [[-2, 1], [1, -2]]` is the canonical intersection
/ linking form on H₁. Its determinant is the **trefoil determinant**
`|Δ_K(-1)| = 3` — a derived invariant, no free parameters. -/

/-- `det(V + Vᵀ)` for `V + Vᵀ = [[-2,1],[1,-2]]`: `(-2)(-2) − (1)(1) = 3`. -/
def symmetrizedSeifertDet : Int := (-2) * (-2) - 1 * 1

/-- **`det(V + Vᵀ) = 3 = trefoil determinant`.** -/
theorem symmetrizedSeifertDet_eq_three : symmetrizedSeifertDet = 3 := by decide

end QOU.BraidKnot.Sigma1CubedSeifertTessellation
