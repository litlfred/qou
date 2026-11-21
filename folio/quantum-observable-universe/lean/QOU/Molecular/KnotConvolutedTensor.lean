/-
# The knot-convoluted tensor product `A ⊗_K B`

Owner, 2026-10-13 (bean `qou-a1hh`): the bond is "a knot-convoluted tensor product that acts on braids,
part of dual space". The corpus carrier is `prop:ilp-covalent-bond`: the bond is a knot operator `K` acting
by right multiplication, `x ↦ NF(x · K)`, selected in the LP's dual space (knot operators).

Here the product is stated over any monoid `M` (the Hecke algebra's multiplicative monoid in use), with three
monoid homomorphisms: `ι₁`, `ι₂` place the two atoms on their strands and `ι` places the knot operator on a
site. Definition: `A ⊗_K B := ι₁ A * ι₂ B * ι K`.

Proved (no hypothesis beyond the monoid laws):

* `kct_one` — with the trivial operator the product is the plain (index-shift) tensor product;
* `kct_mul` — operators at the SAME site compose: `(A ⊗_K B) · ι K' = A ⊗_{K K'} B`. A second bond
  operator multiplies onto existing strands; it never adds strands. This is why the bond-order obstruction of
  PR #7773 (U5: extra trefoil BLOCKS that must each be adjacent to both nuclei) does not arise in this reading;
* `kct_pow` — order-`k` at one site is `K ^ k`;

Operators at two different sites `ι, ι'` are simply applied in sequence (`kct … k * ι' k'`); that is the
definition, not a theorem, so it is not stated as one.

**Not fixed here (and not by the corpus):** which site `ι` is, and whether order `k` means `K ^ k` at one
site or `K` at `k` sites (`embeddable-knot-operator` reads it as `k` channels). The selection of `K` and of
the site is the corpus LP, run in `computations/probes/knot_convoluted_tensor_h2_probe.py`.

§7c: generic monoid; no archimedean content.

-- Ref: [manuscript] prop:ilp-covalent-bond; def:molecular-braid; def:embeddable-knot-operator; bean qou-a1hh
-/
import Mathlib.Algebra.Group.Hom.Defs
import Mathlib.Algebra.Group.Basic

namespace QOU.Molecular.KnotConvolutedTensor

variable {M A B Kn : Type*} [Monoid M] [Monoid A] [Monoid B] [Monoid Kn]

/-- The knot-convoluted tensor product `A ⊗_K B := ι₁ A * ι₂ B * ι K`. -/
def kct (ι₁ : A →* M) (ι₂ : B →* M) (ι : Kn →* M) (a : A) (b : B) (k : Kn) : M :=
  ι₁ a * ι₂ b * ι k

/-- **Trivial operator**: the plain tensor product. -/
theorem kct_one (ι₁ : A →* M) (ι₂ : B →* M) (ι : Kn →* M) (a : A) (b : B) :
    kct ι₁ ι₂ ι a b 1 = ι₁ a * ι₂ b := by
  simp [kct]

/-- **Operators at the same site compose**: no new strands. -/
theorem kct_mul (ι₁ : A →* M) (ι₂ : B →* M) (ι : Kn →* M) (a : A) (b : B) (k k' : Kn) :
    kct ι₁ ι₂ ι a b k * ι k' = kct ι₁ ι₂ ι a b (k * k') := by
  simp [kct, mul_assoc]

/-- **Order `k` at one site is `K ^ k`.** -/
theorem kct_pow (ι₁ : A →* M) (ι₂ : B →* M) (ι : Kn →* M) (a : A) (b : B) (k : Kn) (n : ℕ) :
    ι₁ a * ι₂ b * (ι k) ^ n = kct ι₁ ι₂ ι a b (k ^ n) := by
  simp [kct, map_pow]

end QOU.Molecular.KnotConvolutedTensor
