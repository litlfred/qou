import Mathlib.Algebra.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# The archimedean twins are instantiations of their generic siblings — step 1

Companion to
`docs/audits/2026-09-05-the-archimedean-suffix-convention-is-the-wrong-instrument.md`,
which proved this for `speedOfLight` only and said plainly that the other pairs were
**analogous but not proved**. This file proves the rest, so the claim stops resting on
shape.

For each pair the generic (content-block sibling) and archimedean (library) forms are
restated here verbatim in structure, and the theorem is that the archimedean one is the
generic one evaluated at `ℝ`. Restating rather than importing is deliberate: these are
`QOU.Information.*` names that currently collide across the two surfaces, so importing
both is exactly what cannot be done.

**What each theorem licenses.** Not a rename. It licenses replacing the archimedean
body with the instantiation, leaving ONE definition and an `ℝ` form that is a theorem
over it — the `QOU/Archimedean/GroundRingEval.lean` pattern ("produced from ... rather
than posited beside it").

**Two of them are not merely redundant but WEAKER**, and that is the part worth having:
a hypothesis the generic form carries in its type is dropped by the archimedean one,
which then returns junk instead of being unformable. Recorded as `_junk_at_` theorems.

-- Ref: [manuscript] §9/information-speed-of-light, §9/operational-entropy,
--      §9/gravitational-constant, §9/information-bandwidth
-/

namespace ArchimedeanTwinProbe

/-! ## 1. Operational entropy — `η_q = (2q − 1)/q³` -/

/-- Sibling: over any commutative ring, `q` a **unit**, division-free. -/
def operationalEntropyGeneric {k : Type*} [CommRing k] (q : kˣ) : k :=
  (2 * (q : k) - 1) * ((↑q⁻¹ : k) * (↑q⁻¹ : k) * (↑q⁻¹ : k))

/-- Library twin: `ℝ`-valued, division by a possibly-zero `q ^ 3`. -/
noncomputable def operationalEntropyArch (q : ℝ) : ℝ := (2 * q - 1) / q ^ 3

theorem operationalEntropy_arch_is_generic (q : ℝ) (u : ℝˣ) (hu : (u : ℝ) = q) :
    operationalEntropyArch q = operationalEntropyGeneric u := by
  unfold operationalEntropyArch operationalEntropyGeneric
  have hq : q ≠ 0 := by rw [← hu]; exact u.ne_zero
  rw [Units.val_inv_eq_inv_val, hu]
  field_simp

/-- **Weaker, not merely redundant.** At `q = 0` the archimedean form returns `0`;
the generic form cannot be formed there, since `0` is not a unit. -/
theorem operationalEntropy_junk_at_zero : operationalEntropyArch 0 = 0 := by
  unfold operationalEntropyArch
  norm_num

/-! ## 2. Information bandwidth — `𝓑 = q · η / (q − 1)²` -/

/-- Sibling: `u` is the **unit** `q − 1`, carried as a hypothesis in the type. -/
def informationBandwidthGeneric {R : Type*} [CommRing R]
    (q η : R) (u : Rˣ) (_hu : (u : R) = q - 1) : R :=
  q * η * (↑u⁻¹ : R) ^ 2

/-- Library twin: divides by `(q − 1) ^ 2` with no invertibility hypothesis. -/
noncomputable def informationBandwidthArch (q η : ℝ) : ℝ := q * η / (q - 1) ^ 2

theorem informationBandwidth_arch_is_generic
    (q η : ℝ) (u : ℝˣ) (hu : (u : ℝ) = q - 1) :
    informationBandwidthArch q η = informationBandwidthGeneric q η u hu := by
  unfold informationBandwidthArch informationBandwidthGeneric
  have h1 : (q - 1) ≠ 0 := by rw [← hu]; exact u.ne_zero
  rw [Units.val_inv_eq_inv_val, hu]
  field_simp

/-- **Weaker.** At `q = 1` — classicality, where the bandwidth is meant to diverge —
the archimedean form returns `0`. -/
theorem informationBandwidth_junk_at_one (η : ℝ) : informationBandwidthArch 1 η = 0 := by
  unfold informationBandwidthArch
  norm_num

/-! ## 3. Gravitational constant — and its `S_cell` route

The two forms of the cell entropy LOOK different:

* sibling `cellEntropy q u = u² / q³`, i.e. `(q−1)²/q³`;
* library `s_cell = η · ℏ² / (1 − ℏ²)` with `η = (2q−1)/q³`, `ℏ = (q−1)/q`.

They agree — but the library route additionally divides by `1 − ℏ² = (2q−1)/q²`, which
vanishes at `q = 1/2`. That is a singularity the algebraically-equal sibling form does
not have, so this pair is a redundancy AND an extra junk point. -/

noncomputable def cellEntropyArch (q : ℝ) : ℝ :=
  ((2 * q - 1) / q ^ 3) * ((q - 1) / q) ^ 2 / (1 - ((q - 1) / q) ^ 2)

/-- The library's compound `S_cell` is the sibling's `u²/q³`. -/
theorem cellEntropy_arch_eq_simple (q : ℝ) (hq : q ≠ 0) (h2 : 2 * q - 1 ≠ 0) :
    cellEntropyArch q = (q - 1) ^ 2 / q ^ 3 := by
  unfold cellEntropyArch
  have hone : 1 - ((q - 1) / q) ^ 2 = (2 * q - 1) / q ^ 2 := by
    field_simp; ring
  rw [hone]
  field_simp

/-- **The extra junk point the sibling form does not have.** At `q = 1/2` the library
route divides by `1 − ℏ² = 0` and returns `0`, while `(q−1)²/q³ = 2` there. -/
theorem cellEntropy_arch_junk_at_half :
    cellEntropyArch (1 / 2) = 0 ∧ ((1 : ℝ) / 2 - 1) ^ 2 / ((1 : ℝ) / 2) ^ 3 = 2 := by
  constructor
  · unfold cellEntropyArch
    norm_num
  · norm_num

/-! ## 4. q-deformed Reeb vector field

Here the sibling is over `R_q = ℤ[q,q⁻¹]` rather than an arbitrary ring, so the bridge
is `QOU.Archimedean.evalAt` rather than plain instantiation. What is provable without
importing either surface is the shape claim: the archimedean body is the generic body
with `q_inv := fun p => (sp.field p)⁻¹`. Stated over a general field so it is not a
statement about `ℝ` in particular. -/

def qReebGeneric {M K : Type*} [Field K]
    (q_inv xi_f bracket : M → K) (p : M) : K :=
  q_inv p * xi_f p + (1 - q_inv p) * bracket p

noncomputable def qReebArch {M : Type*}
    (field xi_f bracket : M → ℝ) (p : M) : ℝ :=
  (field p)⁻¹ * xi_f p + (1 - (field p)⁻¹) * bracket p

theorem qReeb_arch_is_generic {M : Type*}
    (field xi_f bracket : M → ℝ) (p : M) :
    qReebArch field xi_f bracket p
      = qReebGeneric (fun x => (field x)⁻¹) xi_f bracket p := rfl

/-! ## 5. Algebraic primality — `Prop`-valued, a different shape

The sibling abstracts the span predicate; the library fixes it. So the library form is
the sibling at one particular `inSpan`. The two also differ on `n ≠ 0` versus `n ≥ 1`,
which over `ℕ` is the same condition — stated here so the difference is not mistaken
for content. -/

def IsAlgPrimeGeneric (inSpan : ℕ → List ℕ → Prop) (nonTrivial : ℕ → List ℕ → Prop)
    (n : ℕ) : Prop :=
  n ≠ 0 ∧ ∀ parts, nonTrivial n parts → ¬ inSpan n parts

def IsAlgPrimeArch (inSpan : ℕ → List ℕ → Prop) (nonTrivial : ℕ → List ℕ → Prop)
    (n : ℕ) : Prop :=
  n ≥ 1 ∧ ∀ parts, nonTrivial n parts → ¬ inSpan n parts

theorem algPrime_arch_iff_generic (inSpan nonTrivial : ℕ → List ℕ → Prop) (n : ℕ) :
    IsAlgPrimeArch inSpan nonTrivial n ↔ IsAlgPrimeGeneric inSpan nonTrivial n := by
  unfold IsAlgPrimeArch IsAlgPrimeGeneric
  constructor
  · rintro ⟨h1, h2⟩; exact ⟨Nat.one_le_iff_ne_zero.mp h1, h2⟩
  · rintro ⟨h1, h2⟩; exact ⟨Nat.one_le_iff_ne_zero.mpr h1, h2⟩

end ArchimedeanTwinProbe
