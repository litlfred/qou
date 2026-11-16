import QOU.Mass.HeckeMonodromy
import Mathlib.Tactic

/-!
# `KZPullbackGenerators` — the named hypothesis of Step-2 option C

Bean `qou-d0qq`, plan step 5 of
`docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md` §B. The Step-2 conjecture
`QOU.Mass.HeckeMonodromy` says the substrate connection's monodromy generators satisfy the
Hecke quadratic; option C names *which* connection. This file carries that name as a
**dependent** conjecture class (§3b-tax): its content is the hypothesis, and the quadratic
is **derived** from it (`quad_of_kz`), so the class does not restate the conclusion.

**The hypothesis.** The substrate connection is the `𝔰𝔩₂` Knizhnik–Zamolodchikov connection on
`Conf₃(ℂ)`, pulled back along the root map `z ↦ {X₁(z), X₂(z), X₃(z)}` of the colour cubic, at the
level fixed by the substrate parameter: `k + 2 = iπ / ln q` in Kohno's convention `q = e^{iπ/(k+2)}`
(`q₀` is an *input* here; nothing derives it). Concretely, for every lasso `i` around a branch
point the substrate generator `T.g i` is **conjugate** in the tower to a KZ monodromy generator
`k` that satisfies the Hecke quadratic with the level's `q`:

* the conjugacy is what `computations/probes/colour_cubic_braid_monodromy_probe.py` measured
  (13/13): every lasso lifts to a positive half-twist `σ_j^{+1}` up to an explicit conjugator;
* the quadratic on `k` is Kohno–Drinfeld — the monodromy of the `𝔰𝔩₂` KZ connection on `V^{⊗n}`
  is the R-matrix with eigenvalues `q, −q⁻¹` — cited, not formalised.

**What is derived.** `quad_of_kz`: conjugation preserves the quadratic, so every `T.g i` satisfies
it. `heckeMonodromy_of_kz` then assembles a `HeckeMonodromy` instance from this class plus the
braid and far-commutation hypotheses — which are *not* consequences of per-generator conjugacy (the
measured conjugators differ from lasso to lasso), so they stay explicit — and a shadow map lying
over `q ↦ 1`. The tower is over a commutative ring `R` with `q : Rˣ`, matching the restated
`HeckeMonodromy` (issue #7992).

**What is not claimed.** That the substrate connection *is* the pulled-back KZ connection is the
open hypothesis this class names; no instance is provided, and none should be until the
connection is constructed (option C's remaining work). Kohno 1987 and Drinfeld 1985 are cited but
not held in `library/`.

-- Ref: [kohno1987] Kohno, Ann. Inst. Fourier 37 (1987) — KZ monodromy factors through `H_n(q)`.
-- Ref: [drinfeld1985] Drinfeld — quasi-Hopf / R-matrix side of the Kohno–Drinfeld theorem.
-- Ref: [leitner2026] computations/probes/colour_cubic_braid_monodromy_probe.py
-/

namespace QOU.Mass

open QOU.MathlibExt.OcneanuTrace

/-- **Dependent conjecture (Step-2 option C).** Each substrate generator is conjugate, in the
tower, to a Knizhnik–Zamolodchikov monodromy generator satisfying the Hecke quadratic with the
level's `q`. The class carries the hypothesis; the quadratic on `T.g i` is derived below. -/
class KZPullbackGenerators {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
    (T : MarkovTrace R A) (q : Rˣ) : Prop where
  /-- For every lasso there is a KZ generator `k` with the Hecke quadratic (Kohno–Drinfeld) and a
  unit `u` conjugating it to the substrate generator (the measured half-twist lift). -/
  conj_kz : ∀ i, ∃ k : A, (k * k = ((q : R) - ↑q⁻¹) • k + 1) ∧ ∃ u : Aˣ, T.g i = ↑u * k * ↑u⁻¹

namespace KZPullbackGenerators

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable (T : MarkovTrace R A) (q : Rˣ)

/-- Conjugation preserves the Hecke quadratic: `(u k u⁻¹)² = u k² u⁻¹ = h • (u k u⁻¹) + 1`. -/
theorem quad_of_conj {k : A} {h : R} (hk : k * k = h • k + 1) (u : Aˣ) :
    (↑u * k * ↑u⁻¹) * (↑u * k * ↑u⁻¹) = h • (↑u * k * ↑u⁻¹) + 1 := by
  have hu : (↑u⁻¹ : A) * ↑u = 1 := Units.inv_mul u
  have hu' : (↑u : A) * ↑u⁻¹ = 1 := Units.mul_inv u
  calc (↑u * k * ↑u⁻¹) * (↑u * k * ↑u⁻¹)
      = ↑u * (k * ((↑u⁻¹ * ↑u) * k)) * ↑u⁻¹ := by noncomm_ring
    _ = ↑u * (k * k) * ↑u⁻¹ := by rw [hu, one_mul]
    _ = ↑u * (h • k + 1) * ↑u⁻¹ := by rw [hk]
    _ = h • (↑u * k * ↑u⁻¹) + ↑u * ↑u⁻¹ := by
        rw [mul_add, add_mul, mul_one, mul_smul_comm, smul_mul_assoc]
    _ = h • (↑u * k * ↑u⁻¹) + 1 := by rw [hu']

/-- **Derived:** every substrate generator satisfies the Hecke quadratic. -/
theorem quad_of_kz [KZPullbackGenerators T q] (i : ℕ) :
    T.g i * T.g i = ((q : R) - ↑q⁻¹) • T.g i + 1 := by
  obtain ⟨k, hk, u, hu⟩ := KZPullbackGenerators.conj_kz (T := T) (q := q) i
  rw [hu]
  exact quad_of_conj hk u

/-- The Step-2 class assembled from the KZ hypothesis plus the relations that per-generator
conjugacy does **not** supply (braid, far commutation), and a shadow `ε` lying over `q ↦ 1`. -/
theorem heckeMonodromy_of_kz [KZPullbackGenerators T q] {B : Type*} [Ring B] (ε : A →+* B)
    (braid : ∀ i, T.g i * T.g (i + 1) * T.g i = T.g (i + 1) * T.g i * T.g (i + 1))
    (far_comm : ∀ i j, i + 2 ≤ j → T.g i * T.g j = T.g j * T.g i)
    (shadow_at_one : ε (algebraMap R A q) = 1) :
    HeckeMonodromy T q ε :=
  { quad := quad_of_kz T q
    braid := braid
    far_comm := far_comm
    shadow_at_one := shadow_at_one }

/-! ## Polynomial inverse and common-conjugator relation transport (`bean qou-d0qq`)

From the derived quadratic `T.g i * T.g i = ((q : R) - ↑q⁻¹) • T.g i + 1`, every
substrate generator `T.g i` has the explicit polynomial inverse
`T.g i - ((q : R) - ↑q⁻¹) • 1` (`pullback_gen_mul_shifted_eq_one`). Furthermore,
when two generators `k₁, k₂ : A` are conjugated by the *same* unit `u : Aˣ`, both
the three-strand braid relation and far commutation transport across conjugation
(`common_unit_conj_braid` and `common_unit_conj_comm`), isolating why distinct
per-lasso conjugators `u_i ≠ u_{i+1}` are the sole obstruction to automatic braid
transport. -/

/-- **Explicit polynomial inverse of every pulled-back generator (`bean qou-d0qq`).**
Under `[KZPullbackGenerators T q]`, `T.g i * (T.g i - ((q : R) - ↑q⁻¹) • 1) = 1`. -/
theorem pullback_gen_mul_shifted_eq_one [KZPullbackGenerators T q] (i : ℕ) :
    T.g i * (T.g i - ((q : R) - ↑q⁻¹) • (1 : A)) = 1 := by
  have hq := quad_of_kz T q i
  calc T.g i * (T.g i - ((q : R) - ↑q⁻¹) • (1 : A))
      = T.g i * T.g i - ((q : R) - ↑q⁻¹) • T.g i := by
        rw [mul_sub, mul_smul_comm, mul_one]
    _ = (((q : R) - ↑q⁻¹) • T.g i + 1) - ((q : R) - ↑q⁻¹) • T.g i := by
        rw [hq]
    _ = 1 := by abel

/-- **Common-conjugator transport of the braid relation (`bean qou-d0qq`).**
If `k₁ * k₂ * k₁ = k₂ * k₁ * k₂`, then conjugating both `k₁` and `k₂` by the same
unit `u : Aˣ` preserves the braid relation. -/
theorem common_unit_conj_braid {k₁ k₂ : A}
    (hb : k₁ * k₂ * k₁ = k₂ * k₁ * k₂) (u : Aˣ) :
    (↑u * k₁ * ↑u⁻¹) * (↑u * k₂ * ↑u⁻¹) * (↑u * k₁ * ↑u⁻¹) =
      (↑u * k₂ * ↑u⁻¹) * (↑u * k₁ * ↑u⁻¹) * (↑u * k₂ * ↑u⁻¹) := by
  have hu : (↑u⁻¹ : A) * ↑u = 1 := Units.inv_mul u
  calc (↑u * k₁ * ↑u⁻¹) * (↑u * k₂ * ↑u⁻¹) * (↑u * k₁ * ↑u⁻¹)
      = ↑u * (k₁ * ((↑u⁻¹ * ↑u) * k₂) * ((↑u⁻¹ * ↑u) * k₁)) * ↑u⁻¹ := by noncomm_ring
    _ = ↑u * (k₁ * k₂ * k₁) * ↑u⁻¹ := by rw [hu, one_mul, one_mul]
    _ = ↑u * (k₂ * k₁ * k₂) * ↑u⁻¹ := by rw [hb]
    _ = ↑u * (k₂ * ((↑u⁻¹ * ↑u) * k₁) * ((↑u⁻¹ * ↑u) * k₂)) * ↑u⁻¹ := by
        rw [hu, one_mul, one_mul]
    _ = (↑u * k₂ * ↑u⁻¹) * (↑u * k₁ * ↑u⁻¹) * (↑u * k₂ * ↑u⁻¹) := by noncomm_ring

/-- **Common-conjugator transport of far commutation (`bean qou-d0qq`).**
If `k₁ * k₂ = k₂ * k₁`, then conjugating both by the same unit `u : Aˣ` preserves
commutation. -/
theorem common_unit_conj_comm {k₁ k₂ : A}
    (hc : k₁ * k₂ = k₂ * k₁) (u : Aˣ) :
    (↑u * k₁ * ↑u⁻¹) * (↑u * k₂ * ↑u⁻¹) = (↑u * k₂ * ↑u⁻¹) * (↑u * k₁ * ↑u⁻¹) := by
  have hu : (↑u⁻¹ : A) * ↑u = 1 := Units.inv_mul u
  calc (↑u * k₁ * ↑u⁻¹) * (↑u * k₂ * ↑u⁻¹)
      = ↑u * (k₁ * ((↑u⁻¹ * ↑u) * k₂)) * ↑u⁻¹ := by noncomm_ring
    _ = ↑u * (k₁ * k₂) * ↑u⁻¹ := by rw [hu, one_mul]
    _ = ↑u * (k₂ * k₁) * ↑u⁻¹ := by rw [hc]
    _ = ↑u * (k₂ * ((↑u⁻¹ * ↑u) * k₁)) * ↑u⁻¹ := by rw [hu, one_mul]
    _ = (↑u * k₂ * ↑u⁻¹) * (↑u * k₁ * ↑u⁻¹) := by noncomm_ring

end KZPullbackGenerators

end QOU.Mass
