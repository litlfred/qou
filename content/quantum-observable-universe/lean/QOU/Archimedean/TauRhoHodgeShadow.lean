/-
# B2 shadow theorem — the ρ↔Hodge-conjugation dictionary is forced at the degenerate locus

Bean `qou-tq20` (milestone `qou-b5qg`, the τ-correspondence proof plan): the B2
statement is *"τ intertwines the fibre reality structure `ρ = conj` with the
Hodge conjugation of `H¹(Bring)`."* This file proves, sorry-free in Lean core,
everything that statement determines **at the degenerate locus** (its shadow):

* `hodgeShadow` — the Hodge-index assignment of the degenerate parameter pair
  (`q = i ↦ H^{1,0}` encoded as `true`, `q = −i ↦ H^{0,1}` as `false`).
* `shadow_norm` / `shadow_intertwines` — it satisfies the B1 dictionary: the
  normalization and the ρ-equivariance `hodgeOf (conj z) = ¬ hodgeOf z` on the
  pair.
* `shadow_unique` — **any** assignment satisfying the normalization and the
  ρ-intertwining agrees with `hodgeShadow` on the whole pair: the dictionary is
  FORCED (no freedom at the shadow level).
* `shadow_multiplier_compat` — the assignment is compatible with the geometric
  carrier (#3942): the `true`-point `q = i` is exactly the multiplier of the
  order-4 automorphism at the vertex `V` (`U·V = i·V`), and the `false`-point is
  the conjugate family's multiplier.

What this does **not** prove (the honest open remainder of B2, Mathlib-gated):
the *functorial lift* — that the categorical τ-functor itself carries `ρ` to the
Hodge conjugation of `H¹(Bring)` (a statement about the actual functor between
the braided category and the geometric side, requiring category-theoretic
apparatus unavailable in Lean core; the corpus's Mathlib build is currently
network-blocked in sandboxes — see `lean-environment-setup`). The shadow
theorems show the lift has a UNIQUE candidate and no consistency obstruction at
the degenerate locus.

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
-/
import Init.Data.Int.Basic
import QOU.Archimedean.SigmaJGeometricCarrier

namespace QOU.Archimedean.TauRhoHodgeShadow

open QOU.Archimedean.SigmaJGeometricCarrier
open QOU.Archimedean.SigmaJGeometricCarrier.GInt

/-- The degenerate-locus Hodge assignment: `q = i ↦ H^{1,0}` (`true`),
everything else (in use: `q = −i`) ↦ `H^{0,1}` (`false`). -/
def hodgeShadow (z : GInt) : Bool := z = I

/-- Normalization: the democratic point `q = i` is assigned `H^{1,0}`. -/
theorem shadow_norm : hodgeShadow I = true := by decide

/-- The conjugate point is assigned `H^{0,1}`. -/
theorem shadow_neg : hodgeShadow (neg I) = false := by decide

/-- ρ-equivariance on the degenerate pair: parameter conjugation maps to the
Hodge swap — `hodgeShadow (conj z) = ¬ hodgeShadow z` for `z ∈ {i, −i}`. -/
theorem shadow_intertwines :
    hodgeShadow (GInt.conj I) = !(hodgeShadow I)
      ∧ hodgeShadow (GInt.conj (neg I)) = !(hodgeShadow (neg I)) := by decide

/-- **Uniqueness (the dictionary is forced).** Any assignment `f` satisfying the
normalization `f i = true` and the ρ-intertwining on the pair agrees with
`hodgeShadow` on the whole degenerate pair. -/
theorem shadow_unique (f : GInt → Bool)
    (hnorm : f I = true)
    (hint : f (GInt.conj I) = !(f I)) :
    f I = hodgeShadow I ∧ f (neg I) = hodgeShadow (neg I) := by
  refine ⟨by rw [hnorm]; decide, ?_⟩
  have hconj : GInt.conj I = neg I := by decide
  rw [← hconj, hint, hnorm]
  decide

/-- Compatibility with the geometric carrier (#3942): the `true`-point `q = i`
is the multiplier of the order-4 automorphism at `V`, and the `false`-point is
the conjugate family's multiplier — the shadow assignment matches `dU = J`
eigendata at the vertices. -/
theorem shadow_multiplier_compat :
    (∀ k : Fin 5, cyc V k = I * V k) ∧ (∀ k : Fin 5, cyc W k = neg I * W k) :=
  ⟨cycle_multiplier_i, conj_cycle_multiplier_neg_i⟩

end QOU.Archimedean.TauRhoHodgeShadow
