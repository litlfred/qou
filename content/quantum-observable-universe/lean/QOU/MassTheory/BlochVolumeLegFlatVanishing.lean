/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Data.Complex.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Linarith

/-!
# The volume leg of the extended-Bloch regulator vanishes on a flat triangulation

The Δ_λ binding **magnitude** needs an additive, extensive, super-pairwise term.
Neumann's extended Bloch group is the corpus's named candidate: its regulator
`R̂` descends to `Vol + i·CS`, a sum over ideal tetrahedra — additive by
construction, extensive in the triangulation, and super-pairwise because a
tetrahedron couples four vertices rather than two.

This file prunes **half** of that candidate before any construction is
attempted, per the formalize-first discipline (AGENTS.md §"Formalize-first
probe discipline"): the structural claim is stated and proved, and the result
narrows the search rather than a scan doing it.

## The claim

The Bloch–Wigner function `D` is **odd under complex conjugation**,
`D(z̄) = −D(z)`. A real number is its own conjugate. Therefore `D` vanishes at
every real argument, and so does any finite sum of `D` over real shapes —
**for every tetrahedron count**.

## Why this prunes, and exactly what it prunes

The deuteron's canonical closure is committed data, not a modelling choice:
`computations/deltalambda/deuteron-octahedral-gluing.witness.json` records the
`σ₁³` closure as the trefoil `T(2,3)` with

  `num_tetrahedra = 2`,  `shapes = [0.5 + 0i, 2.0 + 0i]`,
  `solution_type = "contains flat tetrahedra"`,  `volume = 0.0`,

and the edge gluing equation forces `z₀·z₁ = 1` identically along the whole
deformation. Both shapes are **real**, so `deuteron_volume_leg_eq_zero` below
gives `Vol = 0` — reproducing SnapPy's `0.0` from the symmetry alone, with no
numerics.

The sharp part is `sum_eq_zero_of_real_shapes`: the vanishing is **independent
of the tetrahedron count**. That is what closes the extensivity hope for this
leg. One cannot rescue the volume term by finding a finer triangulation, a
larger nucleus, or a different spanning choice: on real shapes the sum is `0`
for every `n`, so the very quantity that was supposed to grow like `A` is
identically zero at `A = 2`.

Note also that flattening does not enter. A flattening `[z; p, q]` records
branch data for `log z` and `−log(1−z)`; it shifts the **imaginary** part of
the regulator. `D` is the real part and is flattening-independent, so
"derive the flattening from the gluing equations" — the right instinct, and
the thing that distinguishes this route from a fit — cannot make this leg
nonzero.

## Scope of the exclusion (AGENTS.md §"Before declaring refuted")

This is a **scope-(b) structural exclusion**, and the invariant justifying it
is named: conjugation antisymmetry of `D`. It excludes *the volume leg on a
real-shape triangulation*, at any count.

It is **not** an exclusion of the extended-Bloch route. The `i·CS` leg is
untouched — and `CS` is precisely where flattening is load-bearing, since the
ordinary Bloch group only determines it mod `π²/6`. Whether `CS` can supply an
extensive magnitude is open and is not addressed here.

Neither does it say the corpus's deuteron volume "should" be zero: the corpus
carries **three inconsistent** deuteron knot assignments (trefoil, `Vol = 0`;
the census knot `6₂`, `Vol ≈ 4.40083`; the Hopf link, `Vol = 0`). This file
proves what follows *from the committed trefoil triangulation*. Which
assignment is canonical is an upstream question, and it is load-bearing: the
candidate term differs by the whole of `Vol(6₂)` between frames.

## Base ring

`D` is real-valued on complex shapes, so `ℝ` and `ℂ` here are genuine
archimedean content, not a gratuitous specialisation (AGENTS.md §7c).

## The hypothesis is the definition, not an assumption

`D(z̄) = −D(z)` is stated as a hypothesis on an abstract `D` rather than proved
of a concrete one, because Mathlib has no complex dilogarithm
(`QOU.MathlibExt.IdealTriangulation` records the same gap; bean `qou-idvt`).
Taking it as a hypothesis makes the theorem *stronger*, not weaker: it applies
to any function with that symmetry, and the symmetry is the standard defining
property of Bloch–Wigner, not a convenient extra.

-- Ref: [neumann2004] https://doi.org/10.2140/gt.2004.8.413
   Neumann, "Extended Bloch group and the Cheeger–Chern–Simons class",
   Geom. Topol. 8 (2004) 413–474. Local copy: `library/0307092v2/0307092v2.pdf`.
-- Ref: [zagier2007] https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/978-3-540-30308-4_1/chapter.pdf
   Zagier, "The dilogarithm function", §I.2: `D(z̄) = −D(z)`, hence `D` vanishes
   on `ℝ ∪ {∞}`. Local copy: `library/zagier-the-dilogarithm-function/zagier-the-dilogarithm-function.pdf`.
-/

namespace QOU.MassTheory.BlochVolumeLeg

open Finset

/-- **A conjugation-odd real-valued function vanishes on the reals.**

`D(x̄) = −D(x)` and `x̄ = x` for real `x`, so `D(x) = −D(x)`.

This is the whole mechanism. Bloch–Wigner's vanishing on the real line is
usually quoted as a computation with `Li₂`; it is not one, it is this
two-line symmetry argument, and stating it that way is what makes it
applicable without a dilogarithm in the library. -/
theorem eq_zero_of_conjAntisymm_ofReal (D : ℂ → ℝ)
    (hD : ∀ z : ℂ, D ((starRingEnd ℂ) z) = - D z) (x : ℝ) :
    D (x : ℂ) = 0 := by
  have h := hD (x : ℂ)
  rw [Complex.conj_ofReal] at h
  linarith

/-- **The volume leg vanishes on any flat triangulation, at any tetrahedron
count.**

If every shape parameter is real then `∑ D(zᵢ) = 0`, whatever the index set.

The count-independence is the point. An extensive term is one that grows with
the number of constituents; this sum does not grow, because every summand is
individually zero. So the volume leg cannot be made extensive by refining the
triangulation or by moving to a heavier nucleus whose closure is still
flat. -/
theorem sum_eq_zero_of_real_shapes {ι : Type*} (D : ℂ → ℝ)
    (hD : ∀ z : ℂ, D ((starRingEnd ℂ) z) = - D z)
    (s : Finset ι) (z : ι → ℝ) :
    ∑ i ∈ s, D ((z i : ℂ)) = 0 :=
  Finset.sum_eq_zero fun i _ => eq_zero_of_conjAntisymm_ofReal D hD (z i)

/-- The count-independence, stated so it cannot be missed: for **every** `n`,
a triangulation by `n` real-shaped ideal tetrahedra has volume leg `0`. -/
theorem sum_eq_zero_of_real_shapes_forall_card (D : ℂ → ℝ)
    (hD : ∀ z : ℂ, D ((starRingEnd ℂ) z) = - D z) (n : ℕ) (z : Fin n → ℝ) :
    ∑ i : Fin n, D ((z i : ℂ)) = 0 :=
  sum_eq_zero_of_real_shapes D hD Finset.univ z

/-! ## The deuteron instance

The committed triangulation, evaluated. -/

/-- The two shapes SnapPy reports for the `σ₁³` closure, as reals. -/
noncomputable def deuteronShapes : Fin 2 → ℝ
  | 0 => 1 / 2
  | 1 => 2

/-- **The deuteron's volume leg is exactly zero.**

`Vol = D(1/2) + D(2) = 0`, from conjugation antisymmetry alone — no `Li₂`
evaluation, no numerics. This reproduces the `volume = 0.0` recorded in
`deuteron-octahedral-gluing.witness.json`, and shows that figure is forced by
the shapes being real rather than being a numerical artefact of a degenerate
solve.

Consequently an extended-Bloch **volume** term contributes nothing at `A = 2`,
while the deuteron's binding is not zero. Any Bloch-group closure of the
binding magnitude must therefore come from the `CS` leg, or from a different
knot assignment — not from `Vol` on this triangulation. -/
theorem deuteron_volume_leg_eq_zero (D : ℂ → ℝ)
    (hD : ∀ z : ℂ, D ((starRingEnd ℂ) z) = - D z) :
    ∑ i : Fin 2, D ((deuteronShapes i : ℂ)) = 0 :=
  sum_eq_zero_of_real_shapes_forall_card D hD 2 deuteronShapes

/-! ## Non-vacuity

The hypothesis is satisfiable and the theorem is not about the empty
function. -/

/-- The zero function is conjugation-odd, so the hypothesis is consistent. -/
theorem conjAntisymm_zero : ∀ z : ℂ, (fun _ : ℂ => (0 : ℝ)) ((starRingEnd ℂ) z)
    = - (fun _ : ℂ => (0 : ℝ)) z := by
  intro z; simp

/-- A conjugation-odd function that is **not** identically zero: `Im`. It is
nonzero at `i`, so the theorems above are not silently quantifying over only
the trivial function — they genuinely say that such a function, however large
off the real axis, is pinned to `0` on it.

This is the honest form of the prune: `D` is not small on real shapes, it is
zero, while being unconstrained elsewhere. -/
theorem conjAntisymm_im : ∀ z : ℂ, Complex.im ((starRingEnd ℂ) z) = - Complex.im z := by
  intro z; simp

/-- …and `Im` is nonzero somewhere, so the previous lemma is not vacuous. -/
theorem im_i_ne_zero : Complex.im Complex.I ≠ 0 := by simp

/-- …yet `Im` still vanishes on every real shape, by the general theorem. This
is the prune in miniature: an unconstrained conjugation-odd function,
annihilated on exactly the locus the deuteron's triangulation lives on. -/
theorem im_vanishes_on_deuteron_shapes :
    ∑ i : Fin 2, Complex.im ((deuteronShapes i : ℂ)) = 0 :=
  deuteron_volume_leg_eq_zero Complex.im conjAntisymm_im

end QOU.MassTheory.BlochVolumeLeg
