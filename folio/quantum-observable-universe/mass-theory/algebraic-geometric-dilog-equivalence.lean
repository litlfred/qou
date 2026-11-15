import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.Complex.UpperHalfPlane.Basic
import Mathlib.Tactic
import QOU.Archimedean.BlochWignerLobachevsky

open scoped UpperHalfPlane


/-!
# Algebraic-geometric dilogarithm equivalence (conjecture class)

The conjecture: under the Archimedean realization, the algebraic
partial product Φ_n(x; q) maps bijectively (via its denominator
zeros) to the ideal-tetrahedron cusps of the hyperbolic Φ_q-piece,
and its asymptotic recovers the Bloch-Wigner volume.

Per AGENTS.md §3b, downstream-of-conjecture statements are
themselves conjectures.  We package the assertion as a typeclass
that consumes `ArchimedeanLimit` and a `Kashaev`-style instance and
exposes the bijective + volumetric content.

## The shape parameter lives on the upper half plane, not on ℝ

An ideal tetrahedron in `ℍ³` is determined by a shape parameter
`z ∈ ℂ \ {0, 1}`, and it is **non-degenerate** exactly when
`Im z ≠ 0`; a real `z` is a *flat* tetrahedron, of volume zero.
Bloch-Wigner `D` is the volume of that tetrahedron, so `D` is a
function of a genuinely complex shape.  A previous revision of this
file typed it `BlochWignerD : ℝ → ℝ` and passed it the q-Pochhammer
state variable `x : ℝ` directly, on the grounds that the narrative's
matching map `z(x)` had been "composed away".  That typing is not
merely imprecise, it is **inconsistent with the corpus**: `D` is
conjugation-antisymmetric (`D(z̄) = −D(z)`), so on the real axis it
vanishes identically — proved sorry-free below as
`eq_zero_of_conjAntisymm_ofReal`, and separately in
`QOU.MassTheory.BlochVolumeLegFlatVanishing`.  Any honest
instantiation of the old class was therefore forced to
`volume = 0`, which is not a conjecture about hyperbolic volume but
its negation.  (The inconsistency was latent only because
`BlochWignerD` is `opaque` and no instance was ever constructed.)

And the corpus does not merely have the *mechanism*; it has the
**concrete function and an unconditional vanishing theorem**.
`QOU.Archimedean.BlochWigner_lob : ℂ → ℝ` is a real definition
(Milnor's `Λ(α)+Λ(β)+Λ(γ)`, not an `opaque`), and
`QOU.Knot.FlatTet.BlochWigner_lob_ofReal` proves
`BlochWigner_lob (x : ℂ) = 0` for **every** real `x`, with no
hypothesis at all.  So under the old typing the two could not be
wired without collapsing the conjecture outright — the defect was
latent only because no file imported the other.  That also makes the
old docstring's justification ("stands in ... until Mathlib provides
a complete formalisation of the classical dilogarithm") stale on the
Lobachevsky route: the corpus supplied one itself, of type `ℂ → ℝ`.

Under the present typing that wiring becomes both possible and
non-vacuous — `fun z : ℍ => BlochWigner_lob (z : ℂ)` is not
identically zero (`3·D(y₊) = Vol(5₂)`, matched to 20 digits, bean
`qou-ma3u`).  It is **not** done here: discharging the `opaque` is a
change to what this conjecture asserts, not a retyping, and is left
to the author.

The repair is to **un-compose** the map: the shape is a field the
instance must supply, typed `UpperHalfPlane` so that a flat shape is
not expressible.  The state variable `x : ℝ` keeps its own role in
the q-Pochhammer asymptotic; it is not the shape.

-- Ref: [leitner2026] conj:algebraic-geometric-dilog-equivalence
-- Ref: [kashaev1997] Kashaev, "The hyperbolic volume of knots from the quantum dilogarithm," Lett. Math. Phys. 39 (1997)
-- Ref: [murakami-murakami2001] Murakami & Murakami, "The colored Jones polynomials and the simplicial volume of a knot," Acta Math. 186 (2001), arXiv:math/9905075
-/

namespace QOU.QPochhammer

/-- Local restatement of the q-Pochhammer denominator (mirrors the
    sibling `q-pochhammer-partial-product.lean`; kept self-contained
    so this file does not depend on cross-file elaboration). -/
-- Ref: [leitner2026] def:q-pochhammer-partial-product
def denomPolyLocal (q x : ℝ) : ℕ → ℝ
  | 0 => 1
  | n + 1 => (1 - x * q ^ n) * denomPolyLocal q x n

/-- Local restatement of the partial product `Φ_n(x; q) = 1 / (x; q)_n`. -/
-- Ref: [leitner2026] def:q-pochhammer-partial-product
noncomputable def partialProductLocal (q x : ℝ) (n : ℕ) : ℝ :=
  (denomPolyLocal q x n)⁻¹

/-- Bloch-Wigner placeholder.  Like `LiTwo`, this stands in for the
    real-valued `Real.dilog`-derived Bloch-Wigner function `D(z)`
    until Mathlib provides a complete formalisation of the classical
    dilogarithm.

    **Domain.** `D` is the volume of the ideal tetrahedron of shape
    `z`, so its argument is a shape parameter on the open upper half
    plane, not a real number.  See the module docstring: on `ℝ` the
    function vanishes identically, so typing it `ℝ → ℝ` silently
    forces every volume it names to zero. -/
-- Ref: [leitner2026] rem:kashaev-volume-density
-- Ref: [zagier1986] https://doi.org/10.1007/BF01388528 (Bloch-Wigner D)
noncomputable def BlochWignerD (z : ℍ) : ℝ :=
  QOU.Archimedean.BlochWigner_lob (z : ℂ)

/-- **The discharge is definitional.**  `BlochWignerD` unfolds to the
    corpus's concrete Bloch-Wigner on the underlying complex point;
    nothing about the conjecture is hidden behind an `opaque` any
    more. -/
theorem blochWignerD_eq (z : ℍ) :
    BlochWignerD z = QOU.Archimedean.BlochWigner_lob (z : ℂ) := rfl

/-! ## Why the shape may not be real (the retyping, justified)

Two sorry-free facts.  The first is the property that makes a real
shape fatal; the second is what the `UpperHalfPlane` type buys. -/

/-- **A conjugation-antisymmetric real-valued function vanishes on ℝ.**
    Bloch-Wigner satisfies `D(z̄) = −D(z)`; hence `D` is identically
    zero on the real axis.  (Stated for a general `D` so the file
    stays self-contained; the same statement is proved for the
    corpus's Bloch volume leg in
    `QOU.MassTheory.BlochVolumeLegFlatVanishing`.) -/
-- Ref: [leitner2026] rem:kashaev-volume-density
theorem eq_zero_of_conjAntisymm_ofReal (D : ℂ → ℝ)
    (hD : ∀ z : ℂ, D ((starRingEnd ℂ) z) = - D z) (r : ℝ) :
    D (r : ℂ) = 0 := by
  have h := hD (r : ℂ)
  rw [Complex.conj_ofReal] at h
  linarith

/-- **A real shape carries no volume.**  If the volume `V` is named by
    a conjugation-antisymmetric `D` at a *real* argument, then `V = 0`
    — the flat tetrahedron.  This is the defect the old
    `BlochWignerD : ℝ → ℝ` typing produced, recorded as a theorem so
    that reverting the retyping reinstates a visible contradiction
    rather than a silent one.  The corpus's concrete counterpart is
    `QOU.Knot.FlatTet.BlochWigner_lob_ofReal`, which needs no
    antisymmetry hypothesis because `BlochWigner_lob` is defined
    rather than opaque. -/
-- Ref: [leitner2026] conj:algebraic-geometric-dilog-equivalence §2
theorem flat_shape_has_no_volume (D : ℂ → ℝ)
    (hD : ∀ z : ℂ, D ((starRingEnd ℂ) z) = - D z) (V r : ℝ)
    (hV : V = D (r : ℂ)) : V = 0 := by
  rw [hV, eq_zero_of_conjAntisymm_ofReal D hD]

/-- **The upper half plane excludes flat shapes.**  No point of `ℍ` is
    a real number, so the retyped `BlochWignerD` cannot be applied to
    a flat shape at all: the degeneracy is now a *type* error rather
    than a derivable `volume = 0`. -/
theorem shape_ne_real (z : ℍ) (r : ℝ) : (z : ℂ) ≠ (r : ℂ) := by
  intro h
  have hz := z.im_pos
  rw [← UpperHalfPlane.coe_im, h, Complex.ofReal_im] at hz
  exact lt_irrefl 0 hz

/-- **`UpperHalfPlane` already carries the sibling's shape nondegeneracy.**
    The sibling conjecture `conj:shared-denominator-cusp-holonomy` encodes a
    cusp shape as a three-field `GeometricShape z` (`z ≠ 0`, `z ≠ 1`,
    `0 < Im z`).  The last field implies the other two — both `0` and `1` are
    real — so `ℍ` is exactly that predicate and no bespoke structure is needed
    here.  (The two nondegeneracy fields in the sibling are therefore
    redundant; recorded, not changed, since that file is a separate conjecture
    block.) -/
theorem shape_ne_zero_ne_one (z : ℍ) : (z : ℂ) ≠ 0 ∧ (z : ℂ) ≠ 1 :=
  ⟨by simpa using shape_ne_real z 0, by simpa using shape_ne_real z 1⟩

/-- The algebraic-geometric equivalence, as a §3b-cond
    hypothesis-carrying class over the substrate parameter `q` and the
    state variable `x` (both real; each instance pins one `(q, x)` pair).  Per
    AGENTS.md §3b-cond rule 5, the fields axiomatise the conjecture's
    *inputs* — NOT its conclusion:

    * (`shape`) the matched ideal-tetrahedron **shape parameter**, on
      the open upper half plane.  This is the narrative's `z(x)`, no
      longer "composed away": an instance must exhibit the matching
      map's value, and cannot exhibit a flat (real) one.

    * (`vc_asymptotic`) the volume-conjecture **saddle asymptotic**:
      the rescaled log partial product converges to some limit
      `volume` under Faddeev's scaling.  This is the analytic core of
      Kashaev-Murakami-Murakami; for the figure-eight `4₁` it is the
      theorem of Ohtsuki (2016) / Andersen-Hansen.

    * (`pole_cusp_matched`) the matched-cusp volume identification
      `volume = D(shape)`, whose geometric content is supplied by
      `conj:shared-denominator-cusp-holonomy` (the pole side of the
      matching is the unconditional theorem
      `denomPolyLocal_roots_explicit` below).

    The §2 Bloch-Wigner asymptotic is then **derived**
    (`AlgebraicGeometricEquivalence.asymptotic_volume`), not assumed.
    A previous revision carried the conclusion itself as a field plus
    a vacuous `∃ z, z k = q^{-k}` pole field; both are gone — the
    class now asserts exactly the open hypotheses and nothing
    provable-outright. -/
-- Ref: [leitner2026] conj:algebraic-geometric-dilog-equivalence
class AlgebraicGeometricEquivalence (q x : ℝ) where
  /-- The matched ideal-tetrahedron shape parameter (upper half plane;
      a real shape would be a flat tetrahedron — see
      `flat_shape_has_no_volume`). -/
  shape : ℍ
  /-- The limit of the rescaled log partial product (the saddle
      volume). -/
  volume : ℝ
  /-- Hypothesis (i): the volume-conjecture saddle asymptotic. -/
  -- Ref: [murakami-murakami2001] volume conjecture; Ohtsuki asymptotic for 4₁
  vc_asymptotic :
    ∀ ε > (0 : ℝ),
      ∃ N : ℕ, ∀ m, N ≤ m →
        ‖(1 - q) * Real.log (partialProductLocal q x m) - volume‖ < ε
  /-- Hypothesis (ii): the saddle volume is the Bloch-Wigner volume at
      the matched shape parameter. -/
  -- Ref: [leitner2026] conj:shared-denominator-cusp-holonomy
  pole_cusp_matched : volume = BlochWignerD shape

/-! ## The pole side is a THEOREM (unconditional)

The genuine §1 algebraic content — that each `x = q^{-k}` is an actual
**root** of `(x;q)_n` — is unconditional algebra and is proved here
sorry-free (mirroring the generic `QOU.QBeta.qPochDenom_eq_zero_at_pole`,
merged separately). A previous class revision carried a vacuous
`∃ z, z k = q^{-k}` pole field alongside this theorem; the field is gone
(see the class docstring). Only the *cusp correspondence* (that these
poles match the ideal-tetrahedron cusps — the class's `shape` and
`pole_cusp_matched` hypotheses, i.e. `conj:shared-denominator-cusp-holonomy`)
and the VC saddle asymptotic remain the open volume conjecture. -/

/-- Structural unfold of the `n+1` step (definitional). -/
theorem denomPolyLocal_succ (q x : ℝ) (n : ℕ) :
    denomPolyLocal q x (n + 1) = (1 - x * q ^ n) * denomPolyLocal q x n := rfl

/-- **Pole vanishing (theorem).** `(x; q)_n` vanishes at each pole `x = q^{-j}`,
    `j < n` (`q ≠ 0`) — the unconditional algebraic half of
    `conj:algebraic-geometric-dilog-equivalence §1`. -/
-- Ref: [leitner2026] conj:algebraic-geometric-dilog-equivalence §1
theorem denomPolyLocal_eq_zero_at_pole (q : ℝ) (hq : q ≠ 0)
    (n j : ℕ) (hj : j < n) : denomPolyLocal q (q ^ (-(j : ℤ))) n = 0 := by
  induction n with
  | zero => exact absurd hj (Nat.not_lt_zero j)
  | succ m ih =>
    rw [denomPolyLocal_succ]
    rcases (Nat.lt_succ_iff.mp hj).lt_or_eq with h | h
    · rw [ih h, mul_zero]
    · have key : q ^ (-(j : ℤ)) * q ^ (m : ℕ) = 1 := by
        rw [h, ← zpow_natCast q m, ← zpow_add₀ hq, neg_add_cancel, zpow_zero]
      rw [key, sub_self, zero_mul]

/-- **Theorem-backed pole side.** The strengthened §1 statement the class field
    omits: the explicit root function `k ↦ q^{-k}` together with the proof that
    each value is a genuine zero of `(x; q)_n`. Unconditional for `q ≠ 0`.

    **Renamed 2026-09-14 from `pole_cusp_bijection_proved`** (bean `qou-mfdq`,
    executing the recommendation of
    `docs/audits/2026-09-04-how-the-hyperbolic-volume-could-arise-from-qou.md`
    §"Two moves"). The old name asserted three things this statement does not
    contain: there is **no cusp** in the type, **no bijection** (no `Equiv`, no
    injectivity, no cardinality), and `_proved` claimed a compound the file's own
    prose calls open. What it proves is that `n` explicit values are roots of a
    polynomial. The old name was the sort of thing a downstream reader greps and
    cites as evidence for the geometric side; the corpus-grep discipline is
    exactly what it would have defeated. -/
-- Ref: [leitner2026] conj:algebraic-geometric-dilog-equivalence §1
theorem denomPolyLocal_roots_explicit (q : ℝ) (hq : q ≠ 0) (n : ℕ) :
    ∃ z : Fin n → ℝ, (∀ k : Fin n, z k = q ^ (-(k : ℤ)))
      ∧ (∀ k : Fin n, denomPolyLocal q (z k) n = 0) :=
  ⟨fun k => q ^ (-(k : ℤ)), fun _ => rfl,
    fun k => denomPolyLocal_eq_zero_at_pole q hq n k k.isLt⟩

/-! ## The `[Volume Conjecture] ⟹ §2 asymptotic` conditional (§3b-cond)

The §2 asymptotic (`(1−q)·log Φ_n(x;q) → D(z)`, the Bloch–Wigner volume) follows
from the **volume conjecture** together with the **pole-to-cusp matched volume**.
The theorem below makes that conditional structure explicit and honest: the two
mathematical hypotheses carry ALL the content and are cited — **not** laundered:

* `h_vc_asymptotic` — the q-Pochhammer/Kashaev **saddle asymptotic** converges to
  the hyperbolic volume `V`. This is the volume conjecture's analytic core; for
  the figure-eight `4₁` it is the **theorem** of Ohtsuki (2016) / Andersen–Hansen,
  and `⟨4₁⟩_N` is literally this q-Pochhammer sum
  (`computations/qbeta/qbeta_c3_kashaev_invariant_grounding.py`).
* `h_pole_cusp_matched` — the matched cusp volume equals `D(z)` at a shape `z`
  on the upper half plane; the algebraic pole side is proved above
  (`denomPolyLocal_roots_explicit`); the geometric cusp match is
  `conj:shared-denominator-cusp-holonomy`.

The composition (below) is the trivial limit-point substitution — precisely
because the two hypotheses hold the mathematics. This is the **rigorous-
conditional** wiring of the bar-EVEN mass part (`Re 𝔙 = Vol`); the bar-ODD
`S = Im 𝔙` needs the *deformed complex* volume conjecture + the open `u(q₀)` map
(`conj:binding-qbeta-complex-volume`), and is NOT touched here (anti-laundering). -/

/-- **Conditional (VC + pole-cusp match ⟹ §2 asymptotic).** If the q-Pochhammer
    rescaled log converges to a volume `V` (the volume-conjecture saddle
    asymptotic; a theorem for `4₁`) and `V = D(z)` at the matched shape `z ∈ ℍ`
    (the pole-cusp matched cusp volume), then the §2 Bloch–Wigner asymptotic
    holds. The content is the two hypotheses; the composition is a limit-point
    substitution. -/
-- Ref: [murakami-murakami2001] volume conjecture; Ohtsuki asymptotic expansion for 4₁
theorem asymptotic_volume_of_vc (q x V : ℝ) (z : ℍ)
    (h_vc_asymptotic : ∀ ε > (0 : ℝ), ∃ N : ℕ, ∀ m, N ≤ m →
      ‖(1 - q) * Real.log (partialProductLocal q x m) - V‖ < ε)
    (h_pole_cusp_matched : V = BlochWignerD z) :
    ∀ ε > (0 : ℝ), ∃ N : ℕ, ∀ m, N ≤ m →
      ‖(1 - q) * Real.log (partialProductLocal q x m) - BlochWignerD z‖ < ε := by
  rw [← h_pole_cusp_matched]; exact h_vc_asymptotic

/-- **§2 asymptotic, DERIVED from the class hypotheses.**  Given the
    axiomatised inputs (`shape`, `vc_asymptotic`, `pole_cusp_matched`), the
    rescaled log partial product converges to the Bloch-Wigner volume at the
    instance's matched shape — the conclusion the previous class revision
    carried as a field, now a theorem via `asymptotic_volume_of_vc`. -/
-- Ref: [leitner2026] conj:algebraic-geometric-dilog-equivalence §2
theorem AlgebraicGeometricEquivalence.asymptotic_volume (q x : ℝ)
    [h : AlgebraicGeometricEquivalence q x] :
    ∀ ε > (0 : ℝ), ∃ N : ℕ, ∀ m, N ≤ m →
      ‖(1 - q) * Real.log (partialProductLocal q x m)
        - BlochWignerD h.shape‖ < ε :=
  asymptotic_volume_of_vc q x h.volume h.shape h.vc_asymptotic h.pole_cusp_matched

/-- **Stated equivalence (conjecture bundle, both halves).**  §1 is the
    unconditional strengthened pole side (`denomPolyLocal_roots_explicit`,
    needing only `q ≠ 0`); §2 is derived from the class hypotheses.  The
    only conjectural inputs are the class fields — the composition
    contains no `sorry` and assumes nothing provable-outright. -/
-- Ref: [leitner2026] conj:algebraic-geometric-dilog-equivalence
theorem algebraic_geometric_equivalence
    (q x : ℝ) (hq : q ≠ 0) (n : ℕ) [h : AlgebraicGeometricEquivalence q x] :
    (∃ z : Fin n → ℝ, (∀ k : Fin n, z k = q ^ (-(k : ℤ)))
      ∧ (∀ k : Fin n, denomPolyLocal q (z k) n = 0)) ∧
    (∀ ε > (0 : ℝ), ∃ N : ℕ, ∀ m, N ≤ m →
      ‖(1 - q) * Real.log (partialProductLocal q x m)
        - BlochWignerD h.shape‖ < ε) :=
  ⟨denomPolyLocal_roots_explicit q hq n,
    AlgebraicGeometricEquivalence.asymptotic_volume q x⟩

end QOU.QPochhammer
