import MathlibExt.YekutieliIntegration
import QOU.FluidDynamics.DECNavierStokes
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Group.TypeTags.Basic

/-!
# The abelian DEC vorticity is the abelian specialisation of Yekutieli's plaquette holonomy

Bean `qou-4k93`. Owner question 2026-11-25: *"is the discrete Stokes, discrete
na-Stokes per yektieli? do we need to use that?"*

Ref: [yekutieli2015] https://doi.org/10.1142/9537 (non-abelian multiplicative
integration and Stokes on surfaces); [leitner2026]
`MathlibExt/YekutieliIntegration.lean` (the discrete path-ordered product
`holonomy`); [mohamed2016dec] arXiv:1508.01166 §3.2 (abelian DEC `d₁`).

**Setup.** A face `f` of a 2-complex carries an ordered boundary word: a list of
oriented edges `(e, s)`, where `s = true` means the edge is traversed along its
orientation. A connection assigns a transport `U e` in a group `G` to each
edge. The **Yekutieli face holonomy** is the path-ordered product
`holonomy [U e₀^{±1}, U e₁^{±1}, …]` of `MathlibExt.YekutieliIntegration`.
This is the discrete multiplicative integral; in a non-abelian `G` its value
depends on the order and on the basepoint (up to conjugation).

**What is proved (sorry-free).**

* `faceHolonomy_abelian` (general → paper). For an *additive* velocity
  1-cochain `v : E → R`, take the abelian connection `U e = ofAdd (v e)` in
  `Multiplicative R`. Then the Yekutieli face holonomy equals
  `ofAdd ((d₁ v)_f)`, where `d₁` is the signed incidence matrix read off the
  same boundary words (`incid`). So the DEC vorticity of
  `DECNavierStokes.lean` is exactly the abelian specialisation of Yekutieli's
  plaquette holonomy. The DEC identity is a special case; nothing in #9434's
  energy/vorticity lemmas needs the non-abelian form.
* `faceHolonomy_perm_abelian`. In the abelian case the boundary word may be
  reordered or rebased freely (`holonomy_perm`). In a non-abelian `G` it may
  not, which is the content Yekutieli's surface ordering (kites) exists to
  handle.

**Not done here.** The global non-abelian Stokes theorem on a closed surface
(the ordered kite product over all 24 Bring faces, conjugated to a basepoint,
equals the product of commutators of the 2g = 8 generators) is not stated.
It needs a spanning tree and a face ordering of the Bring map, which the corpus
does not yet have in Lean.

**Where q-NS would need the non-abelian form.** Only for a
connection-valued vorticity: the gauge-covariant diffusion of
`q-ns-properties.md` item 2 (an `SU_q(2)` connection `A` transported along
filaments), or edge transports taken in the braid group / Hecke algebra
(crossings `σ_i` on edges). The velocity 1-form of `def:q-navier-stokes` is
additive and needs only the abelian specialisation.

Base ring (§7c): generic `CommRing R`, generic `Group G`; no `ℝ`.
-/

namespace QOU.FluidDynamics.DECYekutieli

open QOU.MathlibExt.YekutieliIntegration

variable {E : Type*} [DecidableEq E]

/-- Transport of one oriented edge. -/
def edgeTransport {G : Type*} [Group G] (U : E → G) (es : E × Bool) : G :=
  if es.2 then U es.1 else (U es.1)⁻¹

/-- **Yekutieli face holonomy**: the path-ordered product along the boundary word. -/
def faceHolonomy {G : Type*} [Group G] (U : E → G) (w : List (E × Bool)) : G :=
  holonomy (w.map (edgeTransport U))

/-- Signed incidence of edge `e` in a boundary word: the DEC `d₁` entry. -/
def incid {R : Type*} [CommRing R] (w : List (E × Bool)) (e : E) : R :=
  (w.map (fun es => if es.1 = e then (if es.2 then (1 : R) else -1) else 0)).sum

variable {R : Type*} [CommRing R]

/-- Signed edge value of an additive 1-cochain. -/
def signedVal (v : E → R) (es : E × Bool) : R := if es.2 then v es.1 else -v es.1

theorem sum_signedVal_eq [Fintype E] (v : E → R) (w : List (E × Bool)) :
    (w.map (signedVal v)).sum = ∑ e, incid w e * v e := by
  induction w with
  | nil => simp [incid]
  | cons es w ih =>
    simp only [List.map_cons, List.sum_cons, ih, incid, add_mul, Finset.sum_add_distrib]
    congr 1
    obtain ⟨a, s⟩ := es
    cases s <;> simp [signedVal, ite_mul]

/-- **General → paper.** The Yekutieli face holonomy of the abelian connection
`U = ofAdd ∘ v` is `ofAdd` of the DEC vorticity `Σ_e incid_f(e) · v e = (d₁ v)_f`. -/
theorem faceHolonomy_abelian [Fintype E] (v : E → R) (w : List (E × Bool)) :
    faceHolonomy (fun e => Multiplicative.ofAdd (v e)) w
      = Multiplicative.ofAdd (∑ e, incid w e * v e) := by
  rw [← sum_signedVal_eq]
  unfold faceHolonomy holonomy
  induction w with
  | nil => simp
  | cons es w ih =>
    simp only [List.map_cons, List.prod_cons, List.sum_cons, ih, ofAdd_add]
    obtain ⟨a, s⟩ := es
    cases s <;> simp [edgeTransport, signedVal]

omit [DecidableEq E] in
/-- In the abelian case the boundary word can be reordered or rebased freely. -/
theorem faceHolonomy_perm_abelian {G : Type*} [CommGroup G] (U : E → G)
    {w w' : List (E × Bool)} (h : w.Perm w') :
    faceHolonomy U w = faceHolonomy U w' :=
  holonomy_perm (h.map _)

/-- **Provenance edge, formal.** For a DEC complex whose `d₁` is the signed
incidence of the face boundary words `bd`, the Yekutieli face holonomy of the
abelian connection `ofAdd ∘ v` is `ofAdd` of the DEC vorticity
`DEC.Complex2.vort` of `DECNavierStokes.lean`. -/
theorem faceHolonomy_eq_vort {V F : Type*} [Fintype V] [Fintype E] [Fintype F]
    (C : QOU.FluidDynamics.DEC.Complex2 R V E F) (bd : F → List (E × Bool))
    (hd1 : ∀ f e, C.d1 f e = incid (bd f) e) (v : E → R) (f : F) :
    faceHolonomy (fun e => Multiplicative.ofAdd (v e)) (bd f)
      = Multiplicative.ofAdd (C.vort v f) := by
  rw [faceHolonomy_abelian]
  simp [QOU.FluidDynamics.DEC.Complex2.vort, Matrix.mulVec, dotProduct, hd1]

end QOU.FluidDynamics.DECYekutieli
