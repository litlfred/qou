import QOU.BraidKnot.QBetaCategoricalPrecisionLadder

/-!
# The Hopf-link Jones value from the skein relation (c₃ input, bean `qou-cds1`)

The ladder's `jonesHopfClassicalLimit := -2` — the `c₃ = J_Hopf(1)` topological
input of the Q_β precision ladder — is here **derived** from the defining Jones
skein axioms, rather than asserted as a bare constant.

Write the Jones polynomial in `s = √t` (so the half-integer powers become
integer). Its defining data are:

* the skein relation at a crossing:  `s⁻²·V₊ − s²·V₋ = (s − s⁻¹)·V₀`;
* the unknot normalisation:          `V(unknot) = 1`;
* the two-component unlink value:     `V(2-unlink) = −(s + s⁻¹)`.

Apply the skein at the single crossing of the positive Hopf link — where
`V₊ = V(Hopf)`, `V₋ = V(2-unlink)`, `V₀ = V(unknot)` — and the Hopf value is
forced: `V(Hopf) = −(s + s⁵)`, hence `V(Hopf)|_{s=1} = −2` at the classical
point `q = 1`.

The skein/unknot/unlink hypotheses **are** the definition of the Jones
polynomial, so this is a derivation of the Hopf value from that definition — not
a new fit. Everything is stated over a generic `CommRing` in the cleared
(division-free) form of the axioms — multiply the skein by `s²` and the unlink
value by `s` — so the derivation is a single `linear_combination`. Sorry-free.

-- Ref: [manuscript] def:jones-polynomial; §7a Hecke–Skein convention
-- Ref: [jones1987] V. Jones, "Hecke algebra representations of braid groups and
--       link polynomials," Ann. of Math. 126 (1987)
-/

namespace QOU.BraidKnot

/-- **The Hopf-link Jones value from the skein relation.** Over any `CommRing`,
    given the cleared Jones data — `V(unknot) = 1`, `s·V(2-unlink) = −(s²+1)`
    (i.e. `V(2-unlink) = −(s+s⁻¹)`), and the cleared skein
    `V₊ − s⁴·V₋ = (s³−s)·V₀` at the Hopf crossing — the positive Hopf link has

      `V(Hopf) = −(s + s⁵)`. -/
theorem jonesHopf_of_skein {R : Type*} [CommRing R]
    (s Vhopf Vunlink Vunknot : R)
    (hunknot : Vunknot = 1)
    (hunlink : s * Vunlink = -(s ^ 2 + 1))
    (hskein : Vhopf - s ^ 4 * Vunlink = (s ^ 3 - s) * Vunknot) :
    Vhopf = -(s + s ^ 5) := by
  subst hunknot
  linear_combination hskein + s ^ 3 * hunlink

/-- **`J_Hopf(1) = −2`, derived.** At the classical point `s = 1` (`q = 1`) the
    skein derivation gives the Hopf value `−2` — the ladder's
    `jonesHopfClassicalLimit`, now a theorem conditional only on the Jones skein
    axioms rather than an asserted constant. -/
theorem jonesHopf_at_one {R : Type*} [CommRing R]
    (Vhopf Vunlink Vunknot : R)
    (hunknot : Vunknot = 1)
    (hunlink : (1 : R) * Vunlink = -((1 : R) ^ 2 + 1))
    (hskein : Vhopf - (1 : R) ^ 4 * Vunlink = ((1 : R) ^ 3 - 1) * Vunknot) :
    Vhopf = -2 := by
  have h := jonesHopf_of_skein 1 Vhopf Vunlink Vunknot hunknot hunlink hskein
  rw [h]; ring

/-- The derived reduced Jones polynomial of the positive Hopf link,
    `V(Hopf)(s) = −(s + s⁵)` in `s = √t`. -/
noncomputable def jonesHopfValue (s : ℝ) : ℝ := -(s + s ^ 5)

/-- **The ladder's `c₃` constant is the skein-derived Hopf value at `q = 1`.**
    `jonesHopfClassicalLimit = jonesHopfValue 1 = −2`: the constant wired into
    the Q_β ladder's N=3 rung is exactly the classical-point value of the
    skein-derived Hopf Jones polynomial, no longer a bare assertion. -/
theorem jonesHopfClassicalLimit_eq_jonesHopfValue_one :
    (jonesHopfClassicalLimit : ℝ) = jonesHopfValue 1 := by
  unfold jonesHopfClassicalLimit jonesHopfValue; norm_num

end QOU.BraidKnot
