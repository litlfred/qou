-- Ref: [tate1974] Tate, *The arithmetic of elliptic curves*,
--      Invent. Math. 23 (1974) 179–206.
--      https://doi.org/10.1007/BF01389745
--
-- Sibling of `def:categorical-mordell-weil`.
--
-- Carries the three constructions the `.md` defines:
--   * the categorical Mordell–Weil group `𝓔_q(𝟙) = Hom_𝐂(𝟙, E_q)`,
--   * the q-deformed L-function `L(𝓔_q, s)` as an Euler product over
--     the places of Bring's curve, and
--   * the q-Tate–Shafarevich group `Ш_q(𝓔_q)` as the kernel of the
--     local–global map on monoidal `H¹`.
--
-- History (bean `qou-08zf`, 2026-09-03; audit
-- `docs/audits/2026-08-26-t3g-carrier3-has-no-formal-content.md`): this
-- sibling was `def CategoricalMordellWeil := trivial` — the
-- `def-disguised-true` shape (AGENTS.md §1a) — while claiming that "the
-- compiled formalisation lives under QOU/AppendixSurreals/", where no such
-- declaration exists.  The real declaration is
-- `QOU.CategoricalMordellWeil` in `QOU/QBirchSwinnertonDyer.lean`
-- (namespace `QOU`, so the `lean.ref` `qou:QOU.AppendixSurreals.…` could
-- never reach it, and the `trivial` stub shadowed it).  The sibling now
-- re-exports that declaration under the manifest's name, so the ref
-- resolves to the genuine object, and adds the two constructions the
-- library file does not carry.

import QOU.QBirchSwinnertonDyer
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Group.Subgroup.Ker

namespace QOU.AppendixSurreals

universe u v

section MordellWeil

variable {C : Type u} [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]

/-- **Categorical Mordell–Weil group** of an object `E` of the monoidal
    category `𝐂`: the abelian group of `𝟙`-rational points
    `𝓔_q(𝟙) := Hom_𝐂(𝟙, E)` (`.md` §1).  The same type as
    `QOU.CategoricalMordellWeil`; re-exported here so the content block's
    `lean.ref` resolves to the genuine construction.  The group law is
    induced by chord–tangent addition on `𝓔_q` transported through the
    fibre functor; only the underlying type is defined. -/
-- Ref: [tate1974] https://doi.org/10.1007/BF01389745
abbrev CategoricalMordellWeil (E : C) : Type v := QOU.CategoricalMordellWeil E

/-- In the Descartes QOU the categorical Mordell–Weil group of the adjoint
    object is trivial (`r_q = 0`): `Hom(𝟙, Ad(A))` is a subsingleton by the
    observability axiom.  Restated from `QOU.descartes_rank_zero` on the
    re-exported name. -/
theorem descartes_rank_zero {k : Type*} [CommRing k]
    (Q : QuantumObservableUniverse.{u, v} k) :
    Subsingleton (@CategoricalMordellWeil Q.C Q.catInst Q.monInst Q.adjointObj) :=
  QOU.descartes_rank_zero Q

end MordellWeil

section LFunction

variable {K : Type*} [Field K]

/-- **Local Euler factor** of the q-deformed L-function at a place with
    Frobenius eigenvalue `α` and norm `N`, in the variable `t = N^{−s}`:
    `1 / (1 − α t + N t²)` (`.md` §2, the factor
    `(1 − α_𝓔(𝔪) N(𝔪)^{−s} + N(𝔪)^{1−2s})^{−1}`).  Generic over any
    field: no `s`-exponentiation is needed once `t` is the variable. -/
def localEulerFactor (α N t : K) : K := 1 / (1 - α * t + N * t ^ 2)

/-- **The q-deformed L-function** `L(𝓔_q, s) = ∏_𝔪 localEulerFactor` over a
    finite set `S` of places `𝔪` of the coordinate ring of Bring's curve,
    with Frobenius eigenvalue `α 𝔪`, norm `N 𝔪 = q^{f(𝔪)}` and
    `t 𝔪 = N(𝔪)^{−s}`.  The `.md` writes the product over `Spec(R_q)`;
    the finite truncation is what a computation evaluates. -/
def qDeformedLFunction {ι : Type*} (S : Finset ι) (α N t : ι → K) : K :=
  ∏ m ∈ S, localEulerFactor (α m) (N m) (t m)

/-- The Euler factor at a place with vanishing Frobenius eigenvalue and
    trivial norm reduces to `1/(1 + t²)` — a sanity evaluation of the
    definition, nothing more. -/
theorem localEulerFactor_zero_one (t : K) : localEulerFactor 0 1 t = 1 / (1 + t ^ 2) := by
  unfold localEulerFactor
  ring

end LFunction

section Sha

/-- **The q-Tate–Shafarevich group** `Ш_q(𝓔_q)`: the kernel of the
    local–global map on the first monoidal cohomology,

      Ш_q(𝓔_q) := ker ( H¹_⊗(𝐂, E_q) → ∏_{ρ ∈ Spec(ξ_q)} H¹_⊗(𝐂_ρ, E_q) ),

    stated for an abelian group `H` (the global `H¹_⊗`), a family of local
    groups `Hloc ρ` indexed by the Reeb spectrum, and the localisation
    homomorphisms `loc ρ`.  The kernel of the product map is the
    intersection of the kernels. -/
def categoricalSha {H : Type*} [AddCommGroup H] {ρ : Type*} {Hloc : ρ → Type*}
    [∀ r, AddCommGroup (Hloc r)] (loc : ∀ r, H →+ Hloc r) : AddSubgroup H :=
  ⨅ r, (loc r).ker

/-- Membership in `Ш_q`: a global class is in `Ш_q` iff it dies at every
    Reeb eigenvalue. -/
theorem mem_categoricalSha {H : Type*} [AddCommGroup H] {ρ : Type*} {Hloc : ρ → Type*}
    [∀ r, AddCommGroup (Hloc r)] (loc : ∀ r, H →+ Hloc r) (x : H) :
    x ∈ categoricalSha loc ↔ ∀ r, loc r x = 0 := by
  unfold categoricalSha
  simp [AddSubgroup.mem_iInf, AddMonoidHom.mem_ker]

end Sha

end QOU.AppendixSurreals
