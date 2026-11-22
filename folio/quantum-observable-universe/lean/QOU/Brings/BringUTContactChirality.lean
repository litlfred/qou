/-
# UT(Σ₄) is canonically oriented and chiral; conjugation is a strict contactomorphism

Owner, 2026-10-12: option 1 ("bar involution = conjugation") only if it can be derived (bean
`qou-jfx8`). `BringConjugationChirality.lean` showed that on `UT(Σ₄)` (where the corpus puts the
Reeb flow) the natural lift of complex conjugation `ι` preserves orientation, so it cannot be
the `σ ↔ σ⁻¹` swap there. This file states what DOES fix the chirality on `UT(Σ₄)`.

## 1. The geodesic flow fixes the orientation

On the upper half-plane with unit tangent vectors `(x, y, θ)`, the Liouville (contact) form
of the geodesic flow is `α = (cos θ dx + sin θ dy)/y`, whose Reeb field is the geodesic
spray. Then

    α ∧ dα = −(1/y²) dx ∧ dy ∧ dθ,

nowhere zero (`contact_volume_coeff`). So `α ∧ dα` is a canonical volume form on `UT(Σ₄)`
(it descends, being `PSL₂ℝ`-invariant), and it orients `UT(Σ₄)` with **no choice made**. Note the
sign: it is the *opposite* of the orientation `dx ∧ dy ∧ dθ` built from the complex
orientation of the base and the counter-clockwise fibre. This matches
`BringConeLinkEulerNumber.lean`, which identifies the cone's link with `UT(Σ₄)`
"orientation reversed". (Matching signs of two conventions is recorded, not proved here.)

## 2. Conjugation preserves the contact form itself

In the upper half-plane, conjugation is `z ↦ −z̄`, i.e. `(x, y) ↦ (−x, y)`, and its differential
sends `θ ↦ π − θ`. The pullback of `α` is `α` (`iota_pullback_alpha`), so `ι` lifts to a
**strict contactomorphism**, commuting with the Reeb (geodesic) flow, with Jacobian
determinant `+1` (`iota_lift_det`). More generally `α` is built from the metric alone
(`α_v(ξ) = ⟨v, dπ ξ⟩`), so the lift of EVERY isometry, orientation-reversing ones included,
preserves it; the lemma checks the reflection `z ↦ −z̄` as the instance. Conjugation is a symmetry of the whole Reeb structure; it
cannot carry chirality.

## 3. UT(Σ₄) has no fibre-preserving orientation reversal

Reversing orientation negates the Seifert Euler number. The link has Euler number `−6 ≠ 0`
(`bring_link_euler`), so `e ≠ −e` (`bring_link_chiral`). Hence no orientation-reversing,
fibre-preserving self-map exists. (For Seifert spaces with `SL̃₂` geometry every
self-homeomorphism is isotopic to a fibre-preserving one; that is a citation, not proved here.)
**UT(Σ₄) is a chiral 3-manifold.**

## What this derives, and the one bit left

On an oriented 3-manifold, the skein/Hecke relation at `q` with orientation `o` is the relation
at `q⁻¹` with orientation `−o`, and links go to mirrors: the only symmetry is the JOINT one
(orientation reversal, `q ↦ q⁻¹`). On `UT(Σ₄)` the orientation is canonical (§1) and cannot be
reversed (§3), and conjugation does not touch it (§2). So once `q₀ > 1` is fixed (CAL-2), the
preference between `σ` and `σ⁻¹` is determined. What remains is a single **global** sign
convention, "a positive crossing is positive for `α ∧ dα`", not a per-collision choice. That bit
is equivalent to `q₀ > 1` versus `q₀ < 1`, which the framework has already spent. It is a
convention to record, not a parameter to fit. **§4 below removes even that bit** for strands that
follow the Reeb flow: `α` fixes their direction and the ambient orientation together.

The per-collision `ChiralityMatching` class (`letterSign_conj`) has the wrong shape for
`UT(Σ₄)`: chirality there is global, not a property of where on `Σ₄` a collision sits.

§7c: over `ℝ` (trigonometry, orientation signs) and `ℤ` (Euler numbers).

-- Ref: [manuscript] lem:bring-cone-reeb-quaternionic-twist; bean qou-rydq; bean qou-jfx8.
   Geodesic flow as Reeb flow of the Liouville form: standard (Geiges, *An Introduction to
   Contact Topology*, §1.5). Skein modules under orientation reversal: arXiv:1610.04728.
   Seifert manifolds, Euler number and orientation: Scott, *The geometries of 3-manifolds*
   (1983), §3.
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import QOU.Brings.BringConeLinkEulerNumber

namespace QOU.Brings.UTContactChirality

open Real

/-- **`α ∧ dα` is nowhere zero.** With `α = (cos θ dx + sin θ dy)/y`, the coefficient of
`dx ∧ dy ∧ dθ` in `α ∧ dα` is `a_x·(∂_y a_θ − ∂_θ a_y) − a_y·(∂_x a_θ − ∂_θ a_x)`, with
`∂_θ a_y = cos θ / y`, `∂_θ a_x = −sin θ / y` and `a_θ = 0`; it equals `−1/y²`. (The partial
derivatives are entered by hand; `ut_contact_orientation_probe.py` checks them symbolically.) -/
theorem contact_volume_coeff (y θ : ℝ) (hy : y ≠ 0) :
    (cos θ / y) * (0 - cos θ / y) - (sin θ / y) * (0 - -(sin θ / y)) = -1 / y ^ 2 := by
  have h := sin_sq_add_cos_sq θ
  field_simp
  linear_combination -h

theorem contact_volume_ne_zero (y θ : ℝ) (hy : y ≠ 0) :
    (cos θ / y) * (0 - cos θ / y) - (sin θ / y) * (0 - -(sin θ / y)) ≠ 0 := by
  rw [contact_volume_coeff y θ hy]
  exact div_ne_zero (by norm_num) (pow_ne_zero 2 hy)

/-- **Conjugation preserves `α`.** Under `(x, y, θ) ↦ (−x, y, π − θ)`, the `dx` coefficient
`cos θ / y` pulls back to `cos (π − θ)·(−1)/y` and the `dy` coefficient `sin θ / y` to
`sin (π − θ)/y`; both are unchanged. -/
theorem iota_pullback_alpha (y θ : ℝ) :
    cos (π - θ) * (-1) / y = cos θ / y ∧ sin (π - θ) / y = sin θ / y := by
  refine ⟨?_, by rw [sin_pi_sub]⟩
  rw [cos_pi_sub]; ring

/-- The lift `(x, y, θ) ↦ (−x, y, π − θ)` has Jacobian `diag(−1, 1, −1)`, determinant `+1`. -/
theorem iota_lift_det : ((-1 : ℤ) * 1 * (-1)) = 1 := by norm_num

/-- **Orientation reversal negates the Euler number; a nonzero Euler number forbids a
fibre-preserving orientation reversal.** -/
theorem euler_chiral (e : ℤ) (he : e ≠ 0) : e ≠ -e := by
  intro h; omega

/-- **`UT(Σ₄)` is chiral**: Euler number `−6`, so `e ≠ −e`. -/
theorem bring_link_chiral :
    linkEulerNumber (canonicalDegree 4) ≠ -linkEulerNumber (canonicalDegree 4) := by
  rw [bring_link_euler]; norm_num

/-! ## 4. The geodesic spray is the Reeb field, and Reeb strands are positively transverse

The unit-speed geodesic spray on the upper half-plane (metric `(dx² + dy²)/y²`) is
`R = y cos θ ∂ₓ + y sin θ ∂_y − cos θ ∂_θ`. It is the Reeb field of `α`: `α(R) = 1`
(`reeb_alpha_eq_one`) and `ι_R dα = 0` (`reeb_contraction_zero`, with the components of `dα`
entered by hand: `dα_{xy} = cos θ / y²`, `dα_{xθ} = sin θ / y`, `dα_{yθ} = −cos θ / y`; checked
symbolically in `ut_contact_orientation_probe.py`).

**Consequence (the one bit, removed).** A strand that follows the Reeb flow has `α > 0` on its
tangent, i.e. it is *positively transverse* to `ξ = ker α`. So `α` alone fixes both the
direction of every strand and the orientation `α ∧ dα` of the ambient manifold, and with them
the sign of every crossing between two such strands (Bennequin: closed braids transverse to a
contact structure have crossing signs measured in the contact orientation). Together with the
corpus's Hecke ↔ skein dictionary (`σ = L₊`, AGENTS.md §7a) and `q₀ > 1`, the preference between
`σ` and `σ⁻¹` at a collision of Reeb strands is **derived**: no convention is left to choose —
**for strands following the GEODESIC Reeb flow.** §5 shows the fibre rotation is a second Reeb
flow with the opposite orientation, so which flow the strands follow is itself the decision.

What this rests on, stated rather than hidden: the owner's picture that particle strands follow
the Reeb (geodesic) flow of `UT(Σ₄)`. That is the framework's modelling input, not a theorem here.

-- Ref: Bennequin, *Entrelacements et équations de Pfaff* (1983); Geiges, *An Introduction to
   Contact Topology*, §1.5 (geodesic flow as Reeb flow). -/

/-- **`α(R) = 1`** for the geodesic spray `R = (y cos θ, y sin θ, −cos θ)`. -/
theorem reeb_alpha_eq_one (y θ : ℝ) (hy : y ≠ 0) :
    (cos θ / y) * (y * cos θ) + (sin θ / y) * (y * sin θ) + 0 * (-cos θ) = 1 := by
  have h := sin_sq_add_cos_sq θ
  field_simp
  linear_combination h

/-- **`ι_R dα = 0`**: the three components `Σᵢ Rⁱ dα_{ij}` vanish. -/
theorem reeb_contraction_zero (y θ : ℝ) (hy : y ≠ 0) :
    (y * sin θ) * (-(cos θ / y ^ 2)) + (-cos θ) * (-(sin θ / y)) = 0 ∧
    (y * cos θ) * (cos θ / y ^ 2) + (-cos θ) * (cos θ / y) = 0 ∧
    (y * cos θ) * (sin θ / y) + (y * sin θ) * (-(cos θ / y)) = 0 := by
  refine ⟨?_, ?_, ?_⟩ <;> field_simp <;> ring

/-- **Reeb strands are positively transverse**: `α(R) > 0`. -/
theorem reeb_positively_transverse (y θ : ℝ) (hy : y ≠ 0) :
    0 < (cos θ / y) * (y * cos θ) + (sin θ / y) * (y * sin θ) + 0 * (-cos θ) := by
  rw [reeb_alpha_eq_one y θ hy]; norm_num

/-! ## 5. The OTHER Reeb flow: the fibre rotation orients UT(Σ₄) the opposite way

`UT(Σ)` carries a second canonical contact form, the Levi-Civita connection form
`η = dθ + dx/y` (the geodesic spray is `η`-horizontal). Its Reeb field is the fibre rotation
`∂_θ`, the Seifert circle action and the Sasakian Reeb field of the cone's link: the "vertical"
direction the corpus's `fermion-boson-knot-link-proof` has strands wind around. Then:

* `η ∧ dη = +(1/y²) dx ∧ dy ∧ dθ` (`fibre_contact_volume_coeff`), the **opposite** sign to
  `α ∧ dα = −(1/y²) dx ∧ dy ∧ dθ` (`contact_orientations_opposite`);
* `η(R) = 0` and `α(∂_θ) = 0` (`legendrian_duality`): each flow is Legendrian for the
  other's contact structure.

**So "strands follow the Reeb flow" names two different flows with OPPOSITE chirality.** Which
one the particle strands follow is a modelling decision; §4's derivation holds for geodesic
strands, and the same argument with `η` gives the mirror answer for fibre strands. -/

/-- **`η ∧ dη = +1/y²`.** With `η = (1/y, 0, 1)`, `dη_{xy} = ∂ₓη_y − ∂_yη_x = 1/y²` and
`dη_{xθ} = dη_{yθ} = 0`, the coefficient `η_x dη_{yθ} − η_y dη_{xθ} + η_θ dη_{xy}` is `1/y²`. -/
theorem fibre_contact_volume_coeff (y : ℝ) :
    (1 / y) * 0 - 0 * 0 + 1 * (0 - (-(1 / y ^ 2))) = 1 / y ^ 2 := by
  ring

/-- **The two canonical contact forms orient `UT(Σ)` oppositely.** -/
theorem contact_orientations_opposite (y θ : ℝ) (hy : y ≠ 0) :
    (cos θ / y) * (0 - cos θ / y) - (sin θ / y) * (0 - -(sin θ / y))
      = -((1 / y) * 0 - 0 * 0 + 1 * (0 - (-(1 / y ^ 2)))) := by
  rw [contact_volume_coeff y θ hy, fibre_contact_volume_coeff y]; ring

/-- **Legendrian duality**: the geodesic spray is `η`-horizontal and the fibre is `α`-horizontal. -/
theorem legendrian_duality (y θ : ℝ) (hy : y ≠ 0) :
    (1 / y) * (y * cos θ) + 0 * (y * sin θ) + 1 * (-cos θ) = 0 ∧
    (cos θ / y) * 0 + (sin θ / y) * 0 + 0 * 1 = 0 := by
  refine ⟨?_, by ring⟩
  field_simp
  ring

/-! ## 6. Owner ruling 2026-10-12 (SUPERSEDED in its orientation by §9): particle strands follow the FIBRE Reeb flow

Verbatim: *"2 fibre"* (choice between the geodesic flow, Reeb of `α`, and the fibre rotation,
Reeb of `η`; bean `qou-jfx8`). Consequences, all stated for the fibre reading:

* **The orientation is fixed by the fibre line field alone.** Reversing the fibre direction
  (`η ↦ −η`) leaves `η ∧ dη` unchanged (`eta_volume_neg_invariant`), so no choice of fibre
  direction enters. The orientation is `+dx ∧ dy ∧ dθ`: complex orientation of the base,
  counter-clockwise fibre. In that orientation `e(UT(Σ₄)) = χ(Σ₄) = −6`, which is
  `bring_link_euler`.
* **Fibre strands are positively transverse to `ker η`** (`fibre_positively_transverse`).
* **The chiral invariant of fibre strands is the torsion linking residue of the fibre class.**
  `H₁(UT(Σ₄)) ≅ ℤ⁸ ⊕ ℤ/6`, with the fibre generating `ℤ/6`, so two fibres have a linking number
  defined in `ℚ/ℤ`, namely `lk(f, f) = −1/e = 1/6 mod 1`. The sign convention is the one making the
  Hopf fibration (`e = −1`) link `+1`. Reversing the orientation sends `1/6 ↦ −1/6 ≡ 5/6`, and
  `1/6 ≢ −1/6 (mod 1)` (`fibre_linking_residue_chiral`). So the residue detects the orientation,
  i.e. the chirality, of every fibre strand pair.

What the residue does NOT give: a sign for an individual crossing. It lives in `ℚ/ℤ`, not `ℚ`,
because the base has genus 4; "positive" is not defined mod 1. It distinguishes the two
chiralities. It does not by itself say which of `σ` or `σ⁻¹` an energy prefers; that needs an
energy that depends on the residue (`SegmentCollisionDatum` Part G).

-- Ref: Seifert-fibred spaces, `H₁` and the torsion linking form: Scott (1983) §3; Hopf link
   sign convention as in `BringConeLinkEulerNumber.hopf_link_euler`. -/

/-- **The orientation does not depend on the fibre direction**: `(−η) ∧ d(−η) = η ∧ dη`
(each factor changes sign). -/
theorem eta_volume_neg_invariant (c : ℝ) : (-1 : ℝ) * (-1) * c = c := by ring

/-- **Fibre strands are positively transverse**: `η(∂_θ) = 1 > 0`. -/
theorem fibre_positively_transverse : (0 : ℝ) < (1 / 1) * 0 + 0 * 0 + 1 * 1 := by norm_num

/-- The torsion linking residue of the fibre class: `−1/e`. -/
def fibreLinkingResidue (e : ℚ) : ℚ := -1 / e

theorem bring_fibre_linking_residue : fibreLinkingResidue (-6) = 1 / 6 := by
  unfold fibreLinkingResidue; norm_num

/-- **The residue is chiral**: `1/6` and its orientation-reverse `−1/6` differ by a
non-integer, so they are different elements of `ℚ/ℤ`. -/
theorem fibre_linking_residue_chiral :
    ¬ ∃ n : ℤ, fibreLinkingResidue (-6) - (-fibreLinkingResidue (-6)) = n := by
  rintro ⟨n, hn⟩
  rw [bring_fibre_linking_residue] at hn
  have h3 : (3 : ℚ) * n = 1 := by linarith
  have : (3 : ℤ) * n = 1 := by exact_mod_cast h3
  omega

/-! ## 7. Both flows checked side by side (owner, 2026-10-12: "check both flows")

| | fibre flow (Reeb of `η`) — RULED | geodesic flow (Reeb of `α`) |
|---|---|---|
| orientation fixed | `+dx ∧ dy ∧ dθ` | `−dx ∧ dy ∧ dθ` (`contact_orientations_opposite`) |
| Euler number in that orientation | `−6` | `+6` (orientation reversal negates `e`) |
| fibre linking residue `−1/e` | `1/6` | `−1/6 ≡ 5/6` (`geodesic_residue_eq_neg`) |
| chiral (`ℓ ≢ −ℓ` mod 1) | yes | yes (`geodesic_residue_chiral`) |

So BOTH readings make `UT(Σ₄)` chiral, with mirror-image residues: the choice of flow fixes the
SIGN of the chirality, never whether it exists. Part G of `SegmentCollisionDatum` applies to
either, with `ℓ = 1/6` (fibre) or `ℓ = 5/6` (geodesic).

Fit with the corpus (`fermion-boson-knot-link-proof`): there, a 2-component link `T(2, 2k)` has
components with OPPOSITE winding `±1` around the vertical (fibre) direction. Under the fibre
reading this is a strand following the flow and a strand against it, i.e. particle and
antiparticle as oppositely oriented fibre strands, which is consistent. Under the geodesic reading
the vertical winding is not the flow direction at all, and the `±1` has no flow interpretation.
That supports the ruling; it does not prove it. -/

/-- **Geodesic reading**: the orientation is reversed, so `e = +6` and the residue is `−1/6`. -/
theorem geodesic_residue_eq_neg :
    fibreLinkingResidue (-(-6)) = -fibreLinkingResidue (-6) := by
  unfold fibreLinkingResidue; norm_num

/-- **The geodesic residue is chiral too**: `−1/6 ≢ 1/6 (mod 1)`. -/
theorem geodesic_residue_chiral :
    ¬ ∃ n : ℤ, fibreLinkingResidue 6 - (-fibreLinkingResidue 6) = n := by
  rintro ⟨n, hn⟩
  unfold fibreLinkingResidue at hn
  have h3 : (3 : ℚ) * n = -1 := by linarith
  have : (3 : ℤ) * n = -1 := by exact_mod_cast h3
  omega

/-! ## 8. Owner refinement 2026-10-12: free strands follow geodesics; the convolution adds fibre rotation

Verbatim: *"geodesic is for a single braid. two braids coming in want to adhere to their geodesic,
however the knot-convolution operator #, changes this."* So a free strand moves along the geodesic
spray `X`, and during a convolution its velocity is `X + κ V` with `V = ∂_θ` the fibre rotation.

* `geodesic_curvature_eq_eta`: `η(X + κV) = κ`, i.e. the connection form measures the departure
  from the geodesic, which is the geodesic curvature of the projected curve. Free strands
  (`κ = 0`) are `η`-horizontal.
* `unit_speed_alpha`: `α(X + κV) = 1` for every `κ`. Free or interacting, every strand stays
  POSITIVELY transverse to `ker α`. By contrast `η(X + κV) = κ` changes sign with the turning
  direction, so `η` cannot orient crossings consistently.

**Consequence, flagged for the owner.** Under this refinement the ambient orientation fixed by the
strands' transversality is `α ∧ dα` (§1, the geodesic one). Its fibre linking residue is `−1/6`
(§7), the mirror of the `+1/6` recorded under the 2026-10-12 "fibre" ruling (§6). The fibre flow
enters as the convolution's TURNING (`κ`; one half twist turns the relative direction by `π`,
`ConvolutionFlowFibre.lean`), not as the strands' own direction. Which orientation is canonical is
the owner's call; this file records both. -/

/-- **The connection form is the geodesic curvature**: `η(X + κV) = κ`. -/
theorem geodesic_curvature_eq_eta (y θ κ : ℝ) (hy : y ≠ 0) :
    (1 / y) * (y * cos θ) + 0 * (y * sin θ) + 1 * (-cos θ + κ) = κ := by
  field_simp; ring

/-- **Unit speed is preserved**: `α(X + κV) = 1`, so every strand stays positively transverse. -/
theorem unit_speed_alpha (y θ κ : ℝ) (hy : y ≠ 0) :
    (cos θ / y) * (y * cos θ) + (sin θ / y) * (y * sin θ) + 0 * (-cos θ + κ) = 1 := by
  have h := sin_sq_add_cos_sq θ
  field_simp
  linear_combination h

/-! ## 9. 🟧 Owner ruling 2026-10-12 (final): the GEODESIC orientation is canonical, `ℓ = −1/6`

Owner pick, after §8: "Geodesic α, ℓ = −1/6". Free strands follow geodesics; the
knot-convolution operator adds fibre turning (`κ = η(velocity)`); crossings are oriented by
`α ∧ dα`, the orientation in which every strand is positively transverse. The canonical fibre
linking residue is therefore `−1/6 ∈ ℚ/ℤ` (`canonicalResidue`). It is chiral
(`canonicalResidue_chiral`, i.e. `geodesic_residue_chiral`). §6's `+1/6` is its mirror, kept as the
record of the superseded orientation. -/

/-- The canonical fibre linking residue under the 2026-10-12 geodesic ruling: `−1/6`. -/
def canonicalResidue : ℚ := fibreLinkingResidue 6

theorem canonicalResidue_eq : canonicalResidue = -1 / 6 := by
  unfold canonicalResidue fibreLinkingResidue; norm_num

theorem canonicalResidue_chiral :
    ¬ ∃ n : ℤ, canonicalResidue - (-canonicalResidue) = n := geodesic_residue_chiral

end QOU.Brings.UTContactChirality
