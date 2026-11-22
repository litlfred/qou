/-
# QOU.QBeta.YekutieliTrefoilDiscretization — a canonical discretization of the Yekutieli surface 2-form on the trefoil Seifert surface

Bean `qou-prjo`: the deuteron Δ_λ binding magnitude's surviving object is the transverse
non-abelian-Stokes surface-curvature pairing `½P∮∮[F_q,F_q]` on the pn braid `σ₁³ = trefoil`,
integrated over the trefoil's genus-1 Seifert surface. Because `σ₁³` is a **single-generator
(abelian)** word, all path/Magnus corrections vanish beyond order 1, so the entire order-2
binding datum is this surface term. The wall (per the bean) is *"a canonical discretization of
the Yekutieli surface 2-form on the trefoil Seifert surface — data the corpus lacks."*

This file supplies that discretization and proves its defining structural property.

**The discretization.** A genus-`g` Seifert surface has `H₁` of rank `2g` with a basis of
handles `A : Fin (2g) → L` (their `q`-connection holonomies, valued in a Lie/associative
algebra `L`) and a Seifert form `V : Fin (2g) → Fin (2g) → ℤ`. The surface-ordered second-order
term `½∮∮[F_q,F_q]` discretizes to the **Seifert-weighted bracket sum**

  `surface2Form V A = ∑_{i,j} V_{ij} · ⁅A_i, A_j⁆`

(the doubled form, to stay integral; the physical `½` is applied downstream). For the trefoil,
`V = [[-1, 1], [0, -1]]` (`g = 1`, two handles `a, b`, intersection `a·b = 1`).

**The structural theorem (proved).** Because Lie self-brackets vanish (`⁅A_i, A_i⁆ = 0`) and the
bracket is antisymmetric, the **symmetric (self-linking) part of `V` drops out** — only the
**skew (intersection) part** `V_{ij} − V_{ji}` survives:

  `surface2Form V A = (V_{01} − V_{10}) • ⁅A_0, A_1⁆`   (genus 1),

so for the trefoil (`V_{01} − V_{10} = 1`) the discretized surface term is **exactly
`⁅A_a, A_b⁆`** — the commutator of the two handle holonomies, weighted by the unit intersection.
This is the canonical, framing-independent (self-linking `V_{ii}` cancels) discretization: the
transverse datum is the non-abelian **intersection** of the two Seifert handles, nothing else.

**Honesty (STRICT).** Generic algebra over `[Ring R]`, sorry-free, no `native_decide`, no
trivial-true, no axiom. This DEFINES the discretization and proves its skew-only structure; it
does NOT by itself produce the deuteron number — the handle holonomies `A_a, A_b` (the corpus
`F_q` q-connection on the Seifert surface) are the remaining input (bean `qou-jqof`/`qou-yczy`).
No fit; nothing wired.

## References
- [leitner2026] bean `qou-prjo` (transverse surface-curvature surviving object); `qou-yczy`
  (Yekutieli 2-form discretization); `QOU.MathlibExt.YekutieliIntegration`;
  `docs/audits/2026-07-24-eunit-magnus-order2.md` §2 (single-generator ⇒ transverse).
- [yekutieli2015] A. Yekutieli, *Nonabelian multiplicative integration on surfaces* (the
  surface-ordered `[F,F]` term this discretizes).
-/
import Mathlib.Tactic

namespace QOU.QBeta.YekutieliTrefoilDiscretization

variable {R : Type*} [Ring R]

/-- Ring commutator (the Lie bracket on `R`). -/
def bracket (a b : R) : R := a * b - b * a

@[simp] theorem bracket_self (a : R) : bracket a a = 0 := by simp [bracket]

theorem bracket_skew (a b : R) : bracket a b = - bracket b a := by
  simp only [bracket]; noncomm_ring

/-- **Central (color-dressing) invariance (sorry-free).** Adding central elements `s, t` (they
commute with everything — e.g. the `bring_color_weighted` scalar dressing `−h(½−δ/4)·1`) to the
two arguments leaves the bracket unchanged: `⁅a+s, b+t⁆ = ⁅a,b⁆`. -/
theorem bracket_add_central {a b s t : R}
    (hs : ∀ x, s * x = x * s) (ht : ∀ x, t * x = x * t) :
    bracket (a + s) (b + t) = bracket a b := by
  simp only [bracket, mul_add, add_mul]
  rw [ht a, hs b, hs t]; abel

/-- The right-handed trefoil Seifert matrix `[[-1, 1], [0, -1]]` (genus 1). -/
def seifertTrefoil : Fin 2 → Fin 2 → ℤ
  | 0, 0 => -1
  | 0, 1 => 1
  | 1, 0 => 0
  | 1, 1 => -1

/-- **The discretized Yekutieli surface 2-form** (doubled, integral) on a genus-1 Seifert
surface with Seifert form `V` and handle holonomies `A`: `∑_{i,j} V_{ij} · ⁅A_i, A_j⁆`. -/
def surface2Form (V : Fin 2 → Fin 2 → ℤ) (A : Fin 2 → R) : R :=
  ∑ i : Fin 2, ∑ j : Fin 2, (V i j) • bracket (A i) (A j)

/-- **Skew-only structure (sorry-free).** On a genus-1 surface, only the skew (intersection)
part of the Seifert form survives — the symmetric self-linking part cancels because Lie
self-brackets vanish and the bracket is antisymmetric. -/
theorem surface2Form_eq_skew (V : Fin 2 → Fin 2 → ℤ) (A : Fin 2 → R) :
    surface2Form V A = (V 0 1 - V 1 0) • bracket (A 0) (A 1) := by
  simp only [surface2Form, Fin.sum_univ_two, bracket_self, smul_zero, add_zero, zero_add]
  rw [bracket_skew (A 1) (A 0), smul_neg, sub_smul, sub_eq_add_neg]

/-- **Trefoil specialization (sorry-free).** For the trefoil Seifert form the discretized
surface 2-form is exactly the commutator of the two handle holonomies (`V_{01} − V_{10} = 1`):
`surface2Form seifertTrefoil A = ⁅A_a, A_b⁆`. The transverse datum is the non-abelian
intersection of the two Seifert handles. -/
theorem surface2Form_trefoil (A : Fin 2 → R) :
    surface2Form seifertTrefoil A = bracket (A 0) (A 1) := by
  rw [surface2Form_eq_skew]
  norm_num [seifertTrefoil]

/-- **Grounding in the corpus `F_q` (sorry-free).** The discretized trefoil surface 2-form
equals the germ q-curvature of the two handle increments, in the exact form of
`germ-commutator-q-curvature.lean`'s `Fq = (1+δq₁)(1+δq₂) − (1+δq₂)(1+δq₁)` (whose
`commutator_eq_curvature` proves it `= ⁅δq₁,δq₂⁆`). So the canonical discretization of
`½P∮∮[F_q,F_q]` over the genus-1 trefoil Seifert surface **is a single corpus germ q-curvature**
`F_q(A_a, A_b)` — the "data the corpus lacks" (bean `qou-prjo`) grounded in the corpus's own
`F_q`. -/
theorem surface2Form_trefoil_eq_germ_curvature (A : Fin 2 → R) :
    surface2Form seifertTrefoil A =
      (1 + A 0) * (1 + A 1) - (1 + A 1) * (1 + A 0) := by
  rw [surface2Form_trefoil, bracket]; noncomm_ring

/-- **Vanishing criterion / the transverse bridge (sorry-free).** The trefoil surface term
vanishes iff the two handle holonomies commute. This is the missing bridge of `qou-prjo`: in the
**abelian** `H₂(q)` strand algebra (single generator `σ₁`, `TrefoilSurfaceStateSum.commutator_zero`)
the handles commute and the term is forced to `0` — the `σ₁³` path gives nothing. A nonzero
transverse datum therefore requires the **non-commutative germ `Ring R`** level (where `F_q ≠ 0`,
`germ-commutator-q-curvature.curvature_antisymm`), exactly as the qou-tw5z τ-shadow lesson
demands: the surface is the ONLY source, and only off the abelian shadow. -/
theorem surface2Form_trefoil_eq_zero_iff (A : Fin 2 → R) :
    surface2Form seifertTrefoil A = 0 ↔ bracket (A 0) (A 1) = 0 := by
  rw [surface2Form_trefoil]

/-- **The dressing is irrelevant (sorry-free).** Shifting each handle holonomy by a central
element (the color/flavor scalar dressing) leaves the trefoil surface term unchanged. So the
whole `bring_color_weighted` `−h(½−δ/4)·1` interface dressing **does not contribute** to the
transverse curvature — only the BARE non-abelian crossing commutator `⁅A_a, A_b⁆` does. This
prunes the interface search: the missing deuteron datum is a genuinely non-commuting pair of
crossings, not a scalar color weight. -/
theorem surface2Form_trefoil_dressing_invariant (A s : Fin 2 → R)
    (h0 : ∀ x, s 0 * x = x * s 0) (h1 : ∀ x, s 1 * x = x * s 1) :
    surface2Form seifertTrefoil (fun i => A i + s i) = surface2Form seifertTrefoil A := by
  rw [surface2Form_trefoil, surface2Form_trefoil]
  exact bracket_add_central h0 h1

end QOU.QBeta.YekutieliTrefoilDiscretization
