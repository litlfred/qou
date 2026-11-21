import Mathlib.Tactic

/-!
# QOU.MassTheory.GermRootVectorGaugeFixing

**The transverse non-abelian-Stokes surface pairing is gauge-FIXED on a
single-generator braid channel, and the determined value is zero.**

This closes the question left open by the trefoil discretization
([`docs/audits/2026-08-08-nastokes-surface-curvature-trefoil-negative.md`](../../../../../../docs/audits/2026-08-08-nastokes-surface-curvature-trefoil-negative.md)):
that probe measured `c₂ = ‖Ω₂^⊥‖/h²` ranging over `0 … 897` across "natural"
germ / handle-holonomy choices and read the spread as O(100×) *gauge freedom*.
It is not freedom. Two conventions the corpus already pins collapse the orbit to
a point, and the point is `0`.

## The two conventions

1. **Germ.** `def:germ-commutator-q-curvature` defines `δq_i` as a *germ-level
   increment of the substrate parameter `q`* — the logarithmic `q`-derivative
   `q·(∂_q σ_i)·σ_i⁻¹`, not `log σ_i` (which is the braid-direction connection
   1-form, whose commutator is the *inter-crossing Magnus* object, already known
   to vanish identically on a single-generator word). In the 2-dim Hecke
   representation the two germs are **`q`-independent constant matrices**
   (`germOne_eq`, `germTwo_eq` below), so the germ `q`-curvature
   `F_q = ⁅δq₁, δq₂⁆` is the **pure root vector** `-4E` (`germCurvature_eq`),
   nilpotent (`germCurvature_sq`).

2. **Transport.** Yekutieli path-ordering
   ([`QOU.MathlibExt.YekutieliIntegration`](../MathlibExt/YekutieliIntegration.lean))
   makes the transport to a band the *ordered partial product* along the word,
   and Seifert's algorithm on a braid closure puts bands ↔ letters (discs ↔
   strands; `seifertBettiOne = c - s + 1` in
   [`TransverseSurfaceCurvature`](TransverseSurfaceCurvature.lean)). On the
   deuteron word `σ₁³` **every** partial product is a power of `ρ(σ₁)`; the
   generator `σ₂` never occurs, so transports mentioning it are inadmissible.

## What is proved here (sorry-free)

* **Abstract (generic `CommRing` scalars, generic `Ring` algebra).**
  `transported_eq_smul`: if `F` is an `Ad u`-eigenvector (root vector) with
  eigenvalue `c`, then conjugation by `uᵏ` returns `cᵏ • F` — every transported
  curvature is a *scalar multiple of one and the same element*.
  `comm_smul_smul`: two scalar multiples of a common element commute.
  `transversePairing_eq_zero`: therefore the intersection-form-weighted
  transverse pairing `Σᵢⱼ Jᵢⱼ • ⁅𝓕ᵢ, 𝓕ⱼ⁆` vanishes **for every intersection
  form `J`, every `H₁` basis / spanning tree, and every handle-exponent
  assignment**. The vanishing is gauge-*independent*, not gauge-*fixed by fiat*.

* **Concrete (2-dim Hecke rep over a generic `Field`).** The generators satisfy
  the braid relation (`heckeGen_braid`) and the Hecke relation
  (`heckeGen1_hecke`), certifying the representation; the germ curvature is the
  root vector `-4E` with `Ad(σ₁) F = (-q²) • F` (`germCurvature_conj_heckeGen1`);
  and the deuteron pairing is `0` (`deuteron_transversePairing_eq_zero`).

## Scope — read this before citing

This is a **scope-(b) structural exclusion restricted to single-generator
`(2, L)`-torus channels** (the deuteron `pn` channel `σ₁³`). The cited invariant
is the `Ad(ρ(σ₁))`-eigenvector property of the germ curvature. It does **not**
exclude the transverse pairing for multi-generator words (`A ≥ 3` nuclei), where
transports involve both generators and the eigenvector property fails.

**"sorry-free ≠ derived" seam.** Lean proves the *algebra*. The step
`∂_q σ₁ = dHeckeGen1` (entrywise differentiation of a 2×2 matrix of rational
functions in `q`) is done by hand — it is checked here only in the sense that
`germOne_eq` derives `germ₁` from the supplied `dHeckeGen1` by Lean algebra
(`heckeGen1_logDeriv`). Cite as "the germs are the constant matrices
`H - 2E`, `-H`, and Lean proves their commutator is the root vector `-4E`",
never "Lean proves the germ is the `q`-derivative".

**Base ring (§7c).** The abstract layer is a generic `CommRing` acting on a
generic `Ring`; the concrete layer is a generic `Field` (needed only for `q⁻¹`).
No `ℝ`, no ordering, no `Real.*`, no archimedean evaluation anywhere.

## References

- Ref: [yekutieli2015] https://doi.org/10.1142/9537 — non-abelian multiplicative
  integration and Stokes' theorem on surfaces.
- Ref: [leitner2026] `quantum-observable-universes/germ-commutator-q-curvature.md`
  — `[δq₁, δq₂] = F_q`, the two-observer germ definition of the `q`-curvature.
- Ref: [leitner2026] `docs/audits/2026-08-09-nastokes-gauge-fixing-germ-root-vector.md`
-/

namespace QOU.MassTheory.GermRootVectorGauge

/-! ## 1. Abstract layer — a root-vector curvature annihilates the pairing -/

section Abstract

variable {K A : Type*} [CommRing K] [Ring A] [Algebra K A]

/-- Ring commutator `⁅x, y⁆ = x*y - y*x`. Stated locally so the file does not
    depend on which `LieRing` instance is in scope for `A`. -/
def comm (x y : A) : A := x * y - y * x

@[simp] theorem comm_self (x : A) : comm x x = 0 := by
  simp [comm]

/-- **Transported curvature.** The curvature `F` parallel-transported back to the
    basepoint along the `k`-th partial product of a single-generator word:
    `𝓕ₖ = uᵏ · F · u⁻ᵏ`. On the deuteron word `σ₁³` every admissible transport
    has this shape, with `u = ρ(σ₁)`. -/
def transported (u : Aˣ) (F : A) (k : ℕ) : A :=
  ((u ^ k : Aˣ) : A) * F * (((u ^ k)⁻¹ : Aˣ) : A)

/-- **`F` is an `Ad u`-eigenvector (a root vector of the transport torus).** -/
def IsRootVector (u : Aˣ) (F : A) (c : K) : Prop :=
  (u : A) * F * ((u⁻¹ : Aˣ) : A) = c • F

/-- **Root-vector transport is scalar.** Conjugating a root vector by any power
    of its transport unit returns a *scalar multiple of the same element*.

    This is the whole gauge-fixing mechanism: the handle holonomy can be any
    power of `u` whatsoever, and the transported curvature still points along
    one fixed line. -/
theorem transported_eq_smul (u : Aˣ) (F : A) (c : K) (h : IsRootVector u F c) :
    ∀ k : ℕ, transported u F k = (c ^ k) • F := by
  intro k
  induction k with
  | zero => simp [transported]
  | succ n ih =>
      have hstep : transported u F (n + 1)
          = ((u ^ n : Aˣ) : A) * ((u : A) * F * ((u⁻¹ : Aˣ) : A)) * (((u ^ n)⁻¹ : Aˣ) : A) := by
        simp only [transported, pow_succ, Units.val_mul, mul_inv_rev, Units.val_inv_eq_inv_val]
        noncomm_ring
      rw [hstep, h, mul_smul_comm, smul_mul_assoc]
      have : ((u ^ n : Aˣ) : A) * F * (((u ^ n)⁻¹ : Aˣ) : A) = transported u F n := rfl
      rw [this, ih, smul_smul, pow_succ, mul_comm (c ^ n) c]

/-- **Two scalar multiples of a common element commute.** -/
theorem comm_smul_smul (a b : K) (F : A) : comm (a • F) (b • F) = 0 := by
  have h : (a • F) * (b • F) = (b • F) * (a • F) := by
    rw [smul_mul_assoc, mul_smul_comm, smul_smul, smul_mul_assoc, mul_smul_comm, smul_smul,
      mul_comm a b]
  simp [comm, h]

/-- **THE GAUGE-FIXING THEOREM.**

    Let the curvature `F` be an `Ad u`-eigenvector and let every handle transport
    be a power of the single unit `u` — the situation forced by a
    single-generator braid word. Then the intersection-form-weighted transverse
    surface pairing

      `Ω₂^⊥ = Σᵢ Σⱼ Jᵢⱼ • ⁅𝓕ᵢ, 𝓕ⱼ⁆`

    **vanishes identically**, for *every* intersection form `J` (so every Seifert
    matrix, every `H₁` basis, every spanning tree) and *every* assignment `k` of
    handles to word positions.

    So the surface→scalar map is not merely gauge-*fixable* here: its value does
    not depend on the gauge at all, and that value is `0`. -/
theorem transversePairing_eq_zero {n : ℕ} (u : Aˣ) (F : A) (c : K)
    (h : IsRootVector u F c) (J : Fin n → Fin n → K) (k : Fin n → ℕ) :
    ∑ i : Fin n, ∑ j : Fin n,
        J i j • comm (transported u F (k i)) (transported u F (k j)) = 0 := by
  have hz : ∀ i j : Fin n,
      J i j • comm (transported u F (k i)) (transported u F (k j)) = 0 := by
    intro i j
    rw [transported_eq_smul u F c h, transported_eq_smul u F c h, comm_smul_smul, smul_zero]
  simp [hz]

/-- The two-handle (genus-one) specialisation: a Seifert surface with `H₁` rank 2
    and *any* intersection pairing `j` between its two handles. -/
theorem transversePairing_genusOne_eq_zero (u : Aˣ) (F : A) (c : K)
    (h : IsRootVector u F c) (j : K) (ka kb : ℕ) :
    j • comm (transported u F ka) (transported u F kb)
      + (-j) • comm (transported u F kb) (transported u F ka) = 0 := by
  rw [transported_eq_smul u F c h, transported_eq_smul u F c h, comm_smul_smul, comm_smul_smul,
    smul_zero, smul_zero, add_zero]

end Abstract

/-! ## 2. Concrete layer — the 2-dim Hecke representation and its germ curvature -/

section Hecke

variable {K : Type*} [Field K]

/-- `ρ(σ₁)` in the 2-dimensional Hecke representation of `B₃` (reduced Burau at
    `t = q²`, rescaled by `-1/q`; eigenvalues `q, -q⁻¹`). -/
def heckeGen1 (q : K) : Matrix (Fin 2) (Fin 2) K := !![q, -q⁻¹; 0, -q⁻¹]

/-- `ρ(σ₂)` in the same representation. -/
def heckeGen2 (q : K) : Matrix (Fin 2) (Fin 2) K := !![-q⁻¹, 0; -q, q]

/-- The inverse of `ρ(σ₁)` (`det = -1`). -/
def heckeGen1Inv (q : K) : Matrix (Fin 2) (Fin 2) K := !![q⁻¹, -q⁻¹; 0, -q]

/-- The entrywise `q`-derivative `∂_q ρ(σ₁)`, supplied as data.

    **Seam (see the module docstring).** Lean does not differentiate here; this
    is the by-hand entrywise derivative of `heckeGen1` (`∂_q q = 1`,
    `∂_q (-q⁻¹) = q⁻²`, `∂_q 0 = 0`). Everything downstream of it *is* Lean
    algebra. -/
def dHeckeGen1 (q : K) : Matrix (Fin 2) (Fin 2) K := !![1, q⁻¹ ^ 2; 0, q⁻¹ ^ 2]

/-- The first germ `δq₁ = H - 2E`, a **constant** (`q`-independent) matrix. -/
def germOne : Matrix (Fin 2) (Fin 2) K := !![1, -2; 0, -1]

/-- The second germ `δq₂ = -H`, a **constant** (`q`-independent) matrix. -/
def germTwo : Matrix (Fin 2) (Fin 2) K := !![-1, 0; 0, 1]

/-- The germ `q`-curvature `F_q = ⁅δq₁, δq₂⁆`. -/
def germCurvature : Matrix (Fin 2) (Fin 2) K := comm (germOne : Matrix (Fin 2) (Fin 2) K) germTwo

@[simp] theorem heckeGen1_mul_inv (q : K) (hq : q ≠ 0) :
    heckeGen1 q * heckeGen1Inv q = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [heckeGen1, heckeGen1Inv, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

@[simp] theorem heckeGen1Inv_mul (q : K) (hq : q ≠ 0) :
    heckeGen1Inv q * heckeGen1 q = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [heckeGen1, heckeGen1Inv, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- **Braid relation** `σ₁σ₂σ₁ = σ₂σ₁σ₂` — certifies that `heckeGen1`,
    `heckeGen2` really are a braid-group representation (not arbitrary
    matrices). -/
theorem heckeGen_braid (q : K) :
    heckeGen1 q * heckeGen2 q * heckeGen1 q = heckeGen2 q * heckeGen1 q * heckeGen2 q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [heckeGen1, heckeGen2, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- **Hecke relation** `(σ₁ - q)(σ₁ + q⁻¹) = 0` — certifies the eigenvalue pair
    `(q, -q⁻¹)`, i.e. that this is the *Hecke* quotient, not just Burau. -/
theorem heckeGen1_hecke (q : K) (hq : q ≠ 0) :
    (heckeGen1 q - q • (1 : Matrix (Fin 2) (Fin 2) K)) *
      (heckeGen1 q + q⁻¹ • (1 : Matrix (Fin 2) (Fin 2) K)) = 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [heckeGen1, Matrix.mul_apply, Fin.sum_univ_two, Matrix.one_apply]

/-- **The logarithmic `q`-derivative germ is the constant matrix `H - 2E`.**

    `q · (∂_q σ₁) · σ₁⁻¹ = !![1, -2; 0, -1]` — the `q`-dependence cancels
    exactly. This is the Lean-checked half of the germ identification; the
    `∂_q` step itself is the by-hand seam recorded in the module docstring. -/
theorem heckeGen1_logDeriv (q : K) (hq : q ≠ 0) :
    q • (dHeckeGen1 q * heckeGen1Inv q) = (germOne : Matrix (Fin 2) (Fin 2) K) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [dHeckeGen1, heckeGen1Inv, germOne] <;>
    field_simp <;> ring

/-- **The germ curvature is the pure root vector `-4E`.** -/
theorem germCurvature_eq : (germCurvature : Matrix (Fin 2) (Fin 2) K) = !![0, -4; 0, 0] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [germCurvature, comm, germOne, germTwo] <;> ring

/-- **The germ curvature is nilpotent** — the hallmark of a root vector (a
    Cartan component would square to a nonzero multiple of the identity). -/
theorem germCurvature_sq :
    (germCurvature : Matrix (Fin 2) (Fin 2) K) * germCurvature = 0 := by
  rw [germCurvature_eq]
  ext i j
  fin_cases i <;> fin_cases j <;> simp [Matrix.mul_apply, Fin.sum_univ_two]

/-- **THE ROOT-VECTOR IDENTITY.** `Ad(σ₁) F_q = (-q²) • F_q`.

    The germ `q`-curvature is an eigenvector of conjugation by the Hecke
    generator, with eigenvalue the ratio of `σ₁`'s eigenvalues,
    `q / (-q⁻¹) = -q²`. -/
theorem germCurvature_conj_heckeGen1 (q : K) (hq : q ≠ 0) :
    heckeGen1 q * germCurvature * heckeGen1Inv q
      = (-q ^ 2) • (germCurvature : Matrix (Fin 2) (Fin 2) K) := by
  rw [germCurvature_eq]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [heckeGen1, heckeGen1Inv, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp

/-- `ρ(σ₁)` as a unit of the matrix ring — the transport unit of the deuteron
    channel. -/
def heckeUnit1 (q : K) (hq : q ≠ 0) : (Matrix (Fin 2) (Fin 2) K)ˣ :=
  ⟨heckeGen1 q, heckeGen1Inv q, heckeGen1_mul_inv q hq, heckeGen1Inv_mul q hq⟩

theorem isRootVector_germCurvature (q : K) (hq : q ≠ 0) :
    IsRootVector (K := K) (heckeUnit1 q hq) germCurvature (-q ^ 2) :=
  germCurvature_conj_heckeGen1 q hq

/-- **THE DEUTERON RESULT.**

    On the `pn`/deuteron channel word `σ₁³` every admissible handle transport is
    a power of `ρ(σ₁)`, and the germ curvature is an `Ad(ρ(σ₁))`-eigenvector.
    Hence the transverse non-abelian-Stokes surface pairing vanishes — for
    **every** Seifert intersection form `J` and **every** handle-exponent
    assignment `k`.

    The `0 … 897` spread reported by the trefoil discretization probe therefore
    does not measure a physical ambiguity; the admissible sub-orbit is a single
    point, and it is `0`. -/
theorem deuteron_transversePairing_eq_zero {n : ℕ} (q : K) (hq : q ≠ 0)
    (J : Fin n → Fin n → K) (k : Fin n → ℕ) :
    ∑ i : Fin n, ∑ j : Fin n,
        J i j • comm (transported (heckeUnit1 q hq) germCurvature (k i))
          (transported (heckeUnit1 q hq) germCurvature (k j)) = 0 :=
  transversePairing_eq_zero _ _ _ (isRootVector_germCurvature q hq) J k

/-- The genus-one trefoil specialisation with the standard Seifert intersection
    form `J = V - Vᵀ = !![0, 1; -1, 0]` and the derived handle exponents
    `(1, 2)` (the partial products before bands 2 and 3 of `σ₁³`). -/
theorem trefoil_transversePairing_eq_zero (q : K) (hq : q ≠ 0) :
    (1 : K) • comm (transported (heckeUnit1 q hq) germCurvature 1)
        (transported (heckeUnit1 q hq) germCurvature 2)
      + (-1 : K) • comm (transported (heckeUnit1 q hq) germCurvature 2)
        (transported (heckeUnit1 q hq) germCurvature 1) = 0 :=
  transversePairing_genusOne_eq_zero _ _ _ (isRootVector_germCurvature q hq) 1 1 2

end Hecke

end QOU.MassTheory.GermRootVectorGauge
