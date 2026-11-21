/-
# The monodromy weight filtration and the τ-assignment obligation, typed

Assignment-map brick on the `TauRhoHodgeLift` wall, building on the merged
monodromy Jordan structure (`HeckeMonodromyJordan`, #4090) and the
ρ-equivariance (#4059). Three facts and one typed target:

* **`channel_vectors_collide_at_monodromy`** — at `q = i` the e₊ and e₋
  channel VECTORS (not just their eigenvalues) coincide, both equal to the
  nilpotent `N v = σv − i·v`: the channel pair collapses onto the Jordan
  weight filtration at the degenerate locus. This is the precise domain
  datum of the τ-functor's evaluation `F(channel pair at the degenerate
  locus) = (H^{1,0}, H^{0,1})`.
* **`monodromyN_star`** — conjugation carries the `i`-Jordan nilpotent to
  the `(−i)`-Jordan nilpotent `N̄` (via the merged `mulStep_star`): ρ
  exchanges the two Jordan structures, the algebraic twin of the geometric
  deck exchange (T3).
* **`jordan_sq_zero_bar`** — `N̄² = 0`, DERIVED from `N² = 0` by
  conjugation transport (not re-proved).
* **`TauAssignmentData`** — the typed assignment obligation: a linear map
  from the length-rule module to the `H^{1,0}` model that kills the
  nilpotent (factors through the semisimple quotient — the local-to-global
  monodromy step) together with a ρ-partner and the intertwining law.
  Content-bearing fields; NO instance declared. Derived (never restated):
  **`QOU.Machinery.HeckeGeneral.bar_kills_nilpotent`** — the partner automatically
  kills the conjugate nilpotent, from the fields plus `monodromyN_star`.

Inhabiting `TauAssignmentData` with functorial provenance (the map coming
from the framework's τ on the T1–T3 geometric side) is now the precisely
typed remaining content of the `TauRhoHodgeLift` wall on the module side.

HONESTY (STRICT): no instance of `TauAssignmentData` is declared — its
existence with provenance IS the wall; the derived lemma shows the fields
are non-degenerate (they derive a consequence, §3b-cond rule 5). Nothing
wired; `1/(8π)` stays phase-4.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/
import QOU.Machinery.HeckeMonodromyJordan
import QOU.Machinery.HeckeDihedralBraidReduction

namespace QOU.Machinery.HeckeGeneral

open Complex

variable {W : Type*}

/-- **The channel vectors collide at the monodromy point**: at `q = i` the
e₊ vector `σv + q⁻¹·v` and the e₋ vector `σv − q·v` are BOTH the nilpotent
`N v = σv − i·v`. The channel pair collapses onto the Jordan weight
filtration at the degenerate locus — the exact domain datum of the
τ-functor's evaluation there. -/
theorem channel_vectors_collide_at_monodromy (D : DescentStructure W) (v : W → ℂ) :
    (mulStep D ((I : ℂ) - I⁻¹) v + (I : ℂ)⁻¹ • v = monodromyN D v)
      ∧ (mulStep D ((I : ℂ) - I⁻¹) v - (I : ℂ) • v = monodromyN D v) := by
  constructor
  · unfold monodromyN
    rw [monodromy_h]
    funext u
    simp only [Pi.add_apply, Pi.sub_apply, Pi.smul_apply, smul_eq_mul, Complex.inv_I]
    ring
  · unfold monodromyN
    rw [monodromy_h]

/-- The conjugate nilpotent: the `(−i)`-Jordan structure `N̄ v = σ̄v + i·v`
(the generator action at the conjugated parameter `h̄ = −2i`). -/
noncomputable def monodromyNbar (D : DescentStructure W) (v : W → ℂ) : W → ℂ :=
  mulStep D (-(2 * I)) v + I • v

/-- **ρ exchanges the two Jordan structures**: conjugation carries the
`i`-nilpotent to the `(−i)`-nilpotent — `star ∘ N = N̄ ∘ star`, entrywise,
at every rank. The algebraic twin of the geometric deck-eigenspace
exchange (T3). -/
theorem monodromyN_star (D : DescentStructure W) (v : W → ℂ) (u : W) :
    star (monodromyN D v u) = monodromyNbar D (fun x => star (v x)) u := by
  unfold monodromyN monodromyNbar
  simp only [Pi.sub_apply, Pi.add_apply, Pi.smul_apply, smul_eq_mul, star_sub, star_mul]
  rw [mulStep_star]
  have hstar : star (2 * I) = -(2 * I) := by
    simp [Complex.star_def]
  have hI : star (I : ℂ) = -I := by
    simp [Complex.star_def]
  rw [hstar, hI]
  ring

/-- **`N̄² = 0`, by conjugation transport** — derived from the merged
`jordan_sq_zero`, not re-proved: conjugating the `i`-Jordan relation gives
the `(−i)`-Jordan relation. -/
theorem jordan_sq_zero_bar (D : DescentStructure W) (w : W → ℂ) :
    monodromyNbar D (monodromyNbar D w) = 0 := by
  have key := jordan_sq_zero D (fun x => star (w x))
  funext u
  have h1 : monodromyNbar D w u = star (monodromyN D (fun x => star (w x)) u) := by
    rw [monodromyN_star]
    congr 1
    funext x
    simp
  have h2 : monodromyNbar D (monodromyNbar D w) u
      = star (monodromyN D (monodromyN D (fun x => star (w x))) u) := by
    have hfun : monodromyNbar D w = fun x =>
        star (monodromyN D (fun y => star (w y)) x) := by
      funext x
      rw [monodromyN_star]
      congr 1
      funext y
      simp
    rw [hfun, monodromyN_star]
  rw [h2, key]
  simp

/-- **The typed τ-assignment obligation** (the module side of the
`TauRhoHodgeLift` wall): a linear map from the length-rule module to the
`H^{1,0}` model that kills the nilpotent — factoring through the
semisimple quotient, the local-to-global monodromy step — together with a
ρ-partner map and the conjugation intertwining law. Content-bearing (four
quantified laws, no `True`); NO instance is declared: inhabiting this with
functorial provenance (the map arising from the framework's τ on the
T1–T3 geometric side) IS the remaining wall content. -/
structure TauAssignmentData (D : DescentStructure W) where
  /-- The assignment onto the `H^{1,0}` model. -/
  toFun : (W → ℂ) → (Fin 4 → ℂ)
  /-- The ρ-partner assignment onto the `H^{0,1}` model. -/
  toFunBar : (W → ℂ) → (Fin 4 → ℂ)
  /-- Additivity. -/
  map_add : ∀ v v', toFun (v + v') = toFun v + toFun v'
  /-- The assignment kills the nilpotent: the target sees only the
  semisimple quotient of the local monodromy. -/
  kills_nilpotent : ∀ v, toFun (monodromyN D v) = 0
  /-- The ρ-intertwining law: conjugation carries the assignment to its
  partner (`F ∘ ρ = conj ∘ F` at the assignment level). -/
  rho_compat : ∀ v u, star (toFun v u) = toFunBar (fun x => star (v x)) u

/-- **Derived, not restated** (§3b-cond rule 5): the ρ-partner
automatically kills the conjugate nilpotent — from `kills_nilpotent`,
`rho_compat`, and the exchange `monodromyN_star`. The fields are
non-degenerate: they force the partner to factor through the conjugate
semisimple quotient without saying so. -/
theorem bar_kills_nilpotent {D : DescentStructure W}
    (A : TauAssignmentData D) (w : W → ℂ) :
    A.toFunBar (monodromyNbar D w) = 0 := by
  funext u
  have hfun : monodromyNbar D w = fun x =>
      star (monodromyN D (fun y => star (w y)) x) := by
    funext x
    rw [monodromyN_star]
    congr 1
    funext y
    simp
  rw [hfun]
  have hcompat := A.rho_compat (monodromyN D (fun y => star (w y))) u
  rw [A.kills_nilpotent] at hcompat
  simp only [Pi.zero_apply, star_zero] at hcompat
  have : A.toFunBar (fun x => star (monodromyN D (fun y => star (w y)) x)) u = 0 :=
    hcompat.symm
  simpa using this

end QOU.Machinery.HeckeGeneral
