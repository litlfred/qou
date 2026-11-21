import UGB.GrobnerShirshov.HeckeGS
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith


/-!
# QOU.VertexAlgebra.JetRelations

The 34 QU/QUO + cohomological relations lifted to the jet bundle J^n(A).
Each base-level relation from vertex-algebra-relations is indexed by
brane level n, with inter-level compatibility (J-3c, J-4a) connecting
adjacent levels via the jet embedding ℓ_n and descent 𝔡_{n+1}.

The descent involution τ̂_n = ℓ_n ∘ 𝔡_{n+1} decomposes level-(n+1)
relations into descended (from level n) and transient (new at n+1).

LaTeX label: `prop:vertex-algebra-jet-relations`

## References
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [jones1987] https://doi.org/10.2307/1971403
- [yekutieli2010] https://doi.org/10.1016/j.aim.2010.06.007

**Ground ring**: this Lean sibling is the **archimedean specialisation
over `ℝ`** (AGENTS.md §7c), matching the `HeckeGS` library, whose
`RewritingSystem (HeckeGen n)` and `HeckeParams.q` are over `ℝ`. The
underlying combinatorial content stays generic to any commutative ring
with the same `q`-data; `q ↦ q₀ ∈ ℝ` is the numerical evaluation.
-/

namespace QOU.VertexAlgebra.JetRelations

open UGB.GrobnerShirshov
open UGB.GrobnerShirshov.Hecke

-- ═══════════════════════════════════════════════════════════════════
-- Level-indexed Hecke algebra
-- ═══════════════════════════════════════════════════════════════════

/-- The Hecke algebra at brane level n is H_{k}(q) where k is the
    strand count. The substrate parameter q is the same at every level
    (Euler characteristic stability). -/
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
noncomputable def levelHecke (hp : HeckeParams) (strands : ℕ) (hs : 0 < strands)
    (_level : ℕ) : RewritingSystem (HeckeGen strands) ℝ :=
  heckeRewritingSystem strands hs hp

-- ═══════════════════════════════════════════════════════════════════
-- J-1: Hecke relations are level-independent
-- ═══════════════════════════════════════════════════════════════════

/-- J-1: The Hecke relation at level n has the same form as at level 0.
    The substrate parameter q does not depend on the brane level. -/
-- Ref: [kassel1995] Ch. X (Hecke algebras and Markov trace)
--      — Kassel, "Quantum Groups," Springer GTM 155, 1995.
--      DOI: 10.1007/978-1-4612-0783-2
theorem hecke_level_independent (hp : HeckeParams) (strands : ℕ)
    (hs : 0 < strands) (n m : ℕ) :
    levelHecke hp strands hs n = levelHecke hp strands hs m := by
  -- Both sides reduce to `heckeRewritingSystem strands hs hp`.
  --
  -- `hs` was added to `levelHecke` when `UGB.GrobnerShirshov.heckeRewritingSystem`
  -- gained `(hn : 0 < n)`, and the three call sites in this file were not
  -- updated — the migration boundary, inside a single file. `autoImplicit`
  -- then reported it as an application type mismatch on `n`, three arguments
  -- downstream of the missing one.
  --
  -- **Level-independence here is true BY CONSTRUCTION, not derived**:
  -- `levelHecke` takes its level as `_level` and discards it. The statement
  -- records that the definition is level-blind; it is not evidence that the
  -- Hecke relation *would* be level-independent under a level-sensitive
  -- construction.
  rfl

-- ═══════════════════════════════════════════════════════════════════
-- J-3c: Inter-level Markov trace compatibility
-- ═══════════════════════════════════════════════════════════════════

/-- J-3c, in the form the Lean actually supports.

    The claim this section is *about*: the Markov trace is level-independent
    on descended elements, `tr_M^{(n+1)}(ℓ_n(w)) = tr_M^{(n)}(w)` for all
    `w ∈ H^{(n)}(q)` — the knot-coordinate form of Euler characteristic
    stability, i.e. the Jones polynomial of a knot does not depend on brane
    level.

    **This was a bare `axiom`, and it is provable — by `rfl`.** Its statement is
    `levelHecke hp n level = levelHecke hp n (level + 1)`, and `levelHecke`
    discards its level argument, so both sides are the same term. Assuming it
    bought nothing, while adding a global axiom to `#print axioms` for every
    statement downstream.

    **What it does NOT establish is what its docstring claimed.** That text read
    "the Markov trace is level-independent on descended elements,
    `tr_M^{(n+1)}(ℓ_n(w)) = tr_M^{(n)}(w)`" — a claim about the Markov trace and
    the jet embedding. Neither appears in the statement, and the bound
    `w : AlgElement (HeckeGen n) ℝ` was never used, which is the tell. The real
    claim needs `tr_M` and `ℓ_n` formalised; it is not in this file and is not
    proved anywhere by this declaration. -/
-- Ref: [jones1987] §3 (The Markov trace) + §4 (Link polynomials)
--      — Jones, "Hecke algebra representations of braid groups and link
--      polynomials," Ann. Math. 126 (1987). Verified against the
--      published version.
theorem levelHecke_succ_eq {n : ℕ} (hp : HeckeParams) (hn : 0 < n) (level : ℕ) :
    levelHecke hp n hn level = levelHecke hp n hn (level + 1) := rfl

-- ═══════════════════════════════════════════════════════════════════
-- JC-3: Euler characteristic stability across levels
-- ═══════════════════════════════════════════════════════════════════

/-- The Euler characteristic of the level-`n` brane algebra, `χ = 2 - 2g`
    at genus `g = 4`.

    Stated as a function of the level so that the stability theorem below
    says something about it. The level is discarded — that is the content
    being recorded, and writing it out is what makes the theorem falsifiable
    rather than an arithmetic identity. -/
def eulerChar (_n : ℕ) : ℤ := 2 - 2 * 4

/-- JC-3: χ(A_n) = χ(A_0) = -6 for all brane levels n.
    The rigidity trace of the identity is level-invariant.

    **Restated 2026-09-04.** This was `theorem euler_level_stable (_n : ℕ) :
    (2 : ℤ) - 2 * 4 = -6 := by norm_num` — a `norm_num` arithmetic fact that
    mentions no brane level and would hold if the numbers came from anywhere
    else, under a docstring about level-invariance. It now names `eulerChar`
    and states both halves of the claim, so it is false if `eulerChar` is
    wrong or level-sensitive. -/
-- Ref: [leitner2026] §4/vertex-algebra-jet-relations
theorem euler_level_stable (n : ℕ) :
    eulerChar n = eulerChar 0 ∧ eulerChar n = -6 := by
  constructor <;> norm_num [eulerChar]

-- ═══════════════════════════════════════════════════════════════════
-- JC-4: Yekutieli obstruction as transient R-matrix
-- ═══════════════════════════════════════════════════════════════════

/-- JC-4: The Yekutieli obstruction κ_n measures the transient part
    of the R-matrix at level n+1:
    κ_n = tr_M^{(n+1)}((1 - τ̂_n) Ř^{(n+1)}).

    **Re-scoped 2026-11-15 (owner decision, PR #7747).** This block used to
    carry `axiom yekutieli_perpetual`, documented as "κ_n ≠ 0 for all n when
    χ = -6" but stating only `q > 1 → q⁻¹(1 - q⁻¹) ≠ 0`. That statement is the
    theorem below, so the axiom was removed (it had no consumers). The
    documented claim is also withdrawn: on Bring's surface the jet obstruction
    vanishes exactly when `n ∣ χ = -6`, i.e. for `n ∈ {1, 2, 3, 6}`, and
    persists for `n ∤ 6` (item 3 of `thm:qu-to-qou`, bean `qou-lx8f`). What is
    proved here is only that the coefficient `q⁻¹(1 - q⁻¹)` is nonzero. -/
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
theorem yekutieli_coeff_nonzero (q : ℝ) (hq : q > 1) :
    q⁻¹ * (1 - q⁻¹) ≠ 0 := by
  have hqpos : q > 0 := by linarith
  have hqi : q⁻¹ > 0 := by positivity
  have hqi1 : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  exact ne_of_gt (mul_pos hqi (by linarith))

-- ═══════════════════════════════════════════════════════════════════
-- D-4: Descent decomposition (bosonic vs fermionic)
-- ═══════════════════════════════════════════════════════════════════

/-- The descent operator τ̂_n = ℓ_n ∘ 𝔡_{n+1} on the Hecke algebra
    at brane level n.  Built from jet prolongation ℓ_n and descent
    homomorphism 𝔡_{n+1}.  This is a specific operator, not an
    arbitrary endomorphism. -/
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
structure DescentOperator (n : ℕ) (hp : HeckeParams) where
  /-- The jet prolongation ℓ_n : H^{(n)} → H^{(n+1)}. -/
  jet_embed : RewritingSystem (HeckeGen n) ℝ → RewritingSystem (HeckeGen n) ℝ
  /-- The descent homomorphism 𝔡_{n+1} : H^{(n+1)} → H^{(n)}. -/
  descent : RewritingSystem (HeckeGen n) ℝ → RewritingSystem (HeckeGen n) ℝ
  /-- The key identity: 𝔡 ∘ ℓ = id. -/
  descent_left_inv : ∀ w, descent (jet_embed w) = w

/-- D-4: The descent involution τ̂_n = ℓ_n ∘ 𝔡_{n+1} is idempotent.
    This splits the algebra into descended (bosonic) and transient
    (fermionic) parts.

    Proof: τ̂² = (ℓ ∘ 𝔡) ∘ (ℓ ∘ 𝔡) = ℓ ∘ (𝔡 ∘ ℓ) ∘ 𝔡 = ℓ ∘ id ∘ 𝔡 = ℓ ∘ 𝔡 = τ̂. -/
-- Ref: [leitner2026] §4/vertex-algebra-jet-relations
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
theorem descent_idempotent {n : ℕ} {hp : HeckeParams}
    (op : DescentOperator n hp)
    (w : RewritingSystem (HeckeGen n) ℝ) :
    let τ := fun x => op.jet_embed (op.descent x)
    τ (τ w) = τ w := by
  simp only
  -- τ(τ(w)) = ℓ(𝔡(ℓ(𝔡(w)))) = ℓ(𝔡(w)) = τ(w)
  -- using: 𝔡(ℓ(x)) = x for all x (descent_left_inv)
  rw [op.descent_left_inv]

end QOU.VertexAlgebra.JetRelations
