/-
# The single `Φ_q` (μ₀) is one of four first-order terms of the octahedral 4-dilogarithm product

`2509.02354` (McPhail-Snyder–Reshetikhin): the holonomy R-matrix of quantum `sl₂` at a root of
unity factorizes into a product of **four** quantum dilogarithms — the four ideal tetrahedra of the
crossing's ideal octahedron. The QOU currently uses a **single** Faddeev `Φ_q` per crossing; the
counit scale `μ₀ = m_e/(3(q−q⁻¹)/2)` is that single-tetrahedron *first-order* phase, and the
deuteron −9% is (hypothesis) the other three tetrahedra.

This file formalises the exact algebraic backbone of that statement, purely as a ring identity
(§7c: generic `CommRing R`, no `ℝ` — the archimedean evaluation of the `Φᵢ` happens downstream). It
does **not** derive the −9% (that needs the actual octahedral holonomy compute); it makes precise
that **the single dilogarithm is the first-order truncation of the four-factor product**, so the
"missing" contribution is the other three factors *plus* the Magnus/cross (commutator-order) terms.

Model each dilogarithm as a leading perturbation `1 + aᵢ` of the identity (`aᵢ = log Φᵢ` to leading
order). The holonomy is the product `∏ᵢ₌₁⁴ (1 + aᵢ)`.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

namespace QOU.MassTheory

variable {R : Type*} [CommRing R]

/-- The **octahedral holonomy** to leading order in each factor: the product of the four
dilogarithm perturbations `(1 + aᵢ)`, one per ideal tetrahedron of the crossing's octahedron. -/
def fourDilog (a b c d : R) : R := (1 + a) * (1 + b) * (1 + c) * (1 + d)

/-- The **single-dilogarithm (μ₀) truncation**: the QOU keeps one tetrahedron, `1 + a`. -/
def singleDilog (a : R) : R := 1 + a

/-- **Exact expansion of the four-factor product** into elementary-symmetric orders. The
**first-order (linear) part is `a + b + c + d`** — the four tetrahedra enter symmetrically; the
quadratic `e₂`, cubic `e₃`, quartic `e₄` parts are the Magnus/cross (commutator-order) corrections. -/
theorem fourDilog_expand (a b c d : R) :
    fourDilog a b c d
      = 1 + (a + b + c + d)
          + (a*b + a*c + a*d + b*c + b*d + c*d)
          + (a*b*c + a*b*d + a*c*d + b*c*d)
          + a*b*c*d := by
  unfold fourDilog; ring

/-- **μ₀ is one of the four first-order terms.** The four-factor holonomy minus the single-dilog
truncation `(1 + a)` is exactly the *other three* first-order tetrahedron terms `(b + c + d)` plus
all the higher-order (cross / Magnus) corrections. So `singleDilog a` captures `a` — one of four —
at first order, and the remainder is the octahedral completion. -/
theorem fourDilog_sub_single (a b c d : R) :
    fourDilog a b c d - singleDilog a
      = (b + c + d)
          + (a*b + a*c + a*d + b*c + b*d + c*d)
          + (a*b*c + a*b*d + a*c*d + b*c*d)
          + a*b*c*d := by
  unfold fourDilog singleDilog; ring

/-- **First-order agreement, quantified.** If the three missing tetrahedra vanish (`b = c = d = 0`)
the four-factor holonomy collapses to the single dilog `1 + a` exactly — the single-`Φ_q` model is
the `b = c = d = 0` restriction of the octahedron, confirming `μ₀` is precisely the one-tetrahedron
truncation. -/
@[simp] theorem fourDilog_single_restrict (a : R) :
    fourDilog a 0 0 0 = singleDilog a := by
  unfold fourDilog singleDilog; ring

/-- **The missing part is second-order-and-up in the missing tetrahedra together with their
first order.** Symmetric companion: dropping the whole octahedral completion (`a` alone kept) and
comparing to the identity isolates `a` as the sole surviving first-order term. -/
theorem fourDilog_linear_part (a b c d : R) :
    fourDilog a b c d
      = 1 + (a + b + c + d)
          + ((a*b + a*c + a*d + b*c + b*d + c*d)
             + (a*b*c + a*b*d + a*c*d + b*c*d) + a*b*c*d) := by
  unfold fourDilog; ring

/-! ## Bar-parity of the octahedral orders (the #4158 discriminating-test structure)

The bar involution `q ↦ q⁻¹` acts on the single-tetrahedron amplitudes as `aᵢ ↦ −aᵢ` (they are
bar-**odd**, being linear in `v − v⁻¹`, `v = √q`). Under this the elementary-symmetric orders split
by parity: the linear part `e₁` is bar-**odd** and the quadratic part `e₂` is bar-**even**. This is
the exact structure the #4158 Magnus route found for the deuteron `−9.21%`: a bar-odd linear
impurity `t = (v−v⁻¹)/[2]_v` ⊕ a bar-even quadratic gap `h² = (v−v⁻¹)²[2]_v²`. The two routes
converge on this parity split (`octahedral_barsplit_convergence_probe.py`); the bar-even `e₂`
coefficient (`≈ 1.0·h²`) is the shared remaining open. -/

/-- The **linear order** `e₁` of the octahedral expansion (the first-order tetrahedron sum). -/
def e1 (a b c d : R) : R := a + b + c + d

/-- The **quadratic order** `e₂` (the pairwise tetrahedron products — the Magnus / cross terms). -/
def e2 (a b c d : R) : R := a*b + a*c + a*d + b*c + b*d + c*d

/-- **`e₁` is bar-ODD.** Under `aᵢ ↦ −aᵢ` the linear part flips sign — matching the bar-odd
impurity `−t` of the #4158 decomposition. -/
theorem e1_bar_odd (a b c d : R) : e1 (-a) (-b) (-c) (-d) = - e1 a b c d := by
  unfold e1; ring

/-- **`e₂` is bar-EVEN.** Under `aᵢ ↦ −aᵢ` the quadratic (pairwise) part is invariant — matching
the bar-even gap `h²` of the #4158 decomposition. So the octahedral 4-`Φ_q` holonomy splits the
`−9.21%` as bar-odd linear ⊕ bar-even quadratic, the same parities as the Magnus route. -/
theorem e2_bar_even (a b c d : R) : e2 (-a) (-b) (-c) (-d) = e2 a b c d := by
  unfold e2; ring

end QOU.MassTheory
