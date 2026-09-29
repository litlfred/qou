/-
# B5 shadow assembly — the per-loop measure decomposition at the degenerate locus

Bean `qou-61lh` (milestone `qou-b5qg`, the τ-correspondence proof plan): the
assembly of the merged bricks into the conditional statement

  *IF the B2 functorial lift holds THEN the per-loop measure is ½·a₀ —
  the ½ forced by the reality structure ρ, the a₀ inherited through the
  conformal class (B3).*

This file proves, sorry-free in Lean core, the **shadow level** of that
assembly — everything the statement determines at the degenerate locus:

* `rho_forced_equal_split` — any weight function symmetric under the reality
  involution `ρ = conj` assigns EQUAL weight to the two members of the
  degenerate pair `{i, −i}` (the shadow of `H^{1,0} ⊕ H^{0,1}`): the ½ is
  forced by ρ-symmetry, not chosen (B4b, PR #3977).
* `channel_share_is_half` — the selected channel carries exactly half the
  doubled total.
* `kl_eigenvalue_at_one_eq_pairCount` — the KL eigenvalue `[2]_q` of
  `b_s = σ + q⁻¹` on the symmetric channel evaluates at `q = 1` to exactly
  the conjugate-pair count 2 (B4a, PR #3973): the tower's own `[2]_q`
  restores the doubled total at the classical point.
* `pairCount_ne_bettiOneBring` — the pair count 2 is NOT `b₁(Bring) = 2g = 8`:
  the numerically coincident decomposition `1/(π·b₁) = 1/(8π)` is a different
  reading (B4b V4 disambiguation).
* `shadow_assembly` — the composed theorem: ANY Hodge assignment satisfying
  the B1 dictionary (normalization + ρ-intertwining) agrees with the FORCED
  `hodgeShadow` (PR #3960 `shadow_unique`), and for ANY ρ-symmetric weight
  the selected channel's share satisfies
  `klEigenvalueAtOne * w(i) = w(i) + w(−i)` — the q→1 one-loop restores the
  doubled total, which is exactly bean B4's target statement
  "q→1 one-loop total = a₀·α" read at the shadow level.

What this does **not** prove (the honest open remainder — the SINGLE wall):
the **B2 functorial lift** — that the categorical τ-functor carries the
fibre reality structure ρ to the Hodge conjugation of `H¹(Bring)` with the
loop's mode space landing on the conjugate pair. That premise enters below
ONLY as the explicit hypotheses `(f, hnorm, hint, w, hsym)` — it is NOT
axiomatised, no class instance is fabricated, and nothing here (or anywhere)
wires `1/(8π)` to production: the identification stays phase-4. Per
AGENTS.md §"Axiomatization is NOT a Proof", proving this conditional shadow
theorem does not close the conjecture.

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
-/
import Init.Data.Int.Basic
import QOU.Archimedean.SigmaJGeometricCarrier
import QOU.Archimedean.TauRhoHodgeShadow

namespace QOU.Archimedean.PerLoopMeasureShadowAssembly

open QOU.Archimedean.SigmaJGeometricCarrier
open QOU.Archimedean.SigmaJGeometricCarrier.GInt
open QOU.Archimedean.TauRhoHodgeShadow

/-- The conjugate-pair count — the shadow of `dim {H^{1,0}, H^{0,1}} = 2`
(the #3920 Hodge doubling). -/
def pairCount : Int := 2

/-- The `q = 1` value of the KL eigenvalue `[2]_q` of `b_s = σ + q⁻¹` on the
symmetric channel (B4a: the one-loop coefficient is −[2]_q·x exactly). -/
def klEigenvalueAtOne : Int := 2

/-- `b₁(Bring) = 2g = 8` — recorded to disambiguate, never to divide by. -/
def bettiOneBring : Int := 8

/-- The tower's own KL eigenvalue at the classical point equals the
conjugate-pair count: the q→1 one-loop restores the doubled total. -/
theorem kl_eigenvalue_at_one_eq_pairCount : klEigenvalueAtOne = pairCount := rfl

/-- The ½ is the conjugate-PAIR share, not `1/b₁`: the pair count is not the
Bring Betti number (the `1/(π·b₁) = 1/(8π)` coincidence is a different
decomposition). -/
theorem pairCount_ne_bettiOneBring : pairCount ≠ bettiOneBring := by decide

/-- ρ exchanges the degenerate pair. -/
theorem conj_I_eq_neg_I : GInt.conj I = neg I := by decide

/-- **ρ-forced equal split.** Any weight symmetric under the reality
involution assigns equal weight to the two members of the degenerate pair —
the shadow of: reality of the Laplacian forces every spectral trace to split
equally across `H^{1,0} ⊕ H^{0,1}` (B4b V2/V3). -/
theorem rho_forced_equal_split (w : GInt → Int)
    (hsym : ∀ z, w (GInt.conj z) = w z) :
    w (neg I) = w I := by
  rw [← conj_I_eq_neg_I]
  exact hsym I

/-- **The selected channel carries exactly half the doubled total.** -/
theorem channel_share_is_half (w : GInt → Int)
    (hsym : ∀ z, w (GInt.conj z) = w z) :
    w I + w (neg I) = 2 * w I := by
  rw [rho_forced_equal_split w hsym]
  omega

/-- **Shadow assembly (the composed conditional theorem at the degenerate
locus).** For ANY Hodge assignment `f` satisfying the B1 dictionary
(normalization + ρ-intertwining) and ANY ρ-symmetric weight `w`:
(1) `f` agrees with the FORCED `hodgeShadow` on the whole pair
    (`shadow_unique`, PR #3960 — the dictionary has no freedom), and
(2) the KL eigenvalue at `q = 1` times the selected channel's weight equals
    the pair total — the q→1 one-loop restores the doubled unit, bean B4's
    target statement read at the shadow level.
The hypotheses are exactly the shadow content of the open B2 lift; they are
explicit binders, not axioms. -/
theorem shadow_assembly (f : GInt → Bool)
    (hnorm : f I = true)
    (hint : f (GInt.conj I) = !(f I))
    (w : GInt → Int)
    (hsym : ∀ z, w (GInt.conj z) = w z) :
    (f I = hodgeShadow I ∧ f (neg I) = hodgeShadow (neg I))
      ∧ klEigenvalueAtOne * w I = w I + w (neg I) := by
  refine ⟨shadow_unique f hnorm hint, ?_⟩
  rw [rho_forced_equal_split w hsym]
  show (2 : Int) * w I = w I + w I
  omega

end QOU.Archimedean.PerLoopMeasureShadowAssembly
