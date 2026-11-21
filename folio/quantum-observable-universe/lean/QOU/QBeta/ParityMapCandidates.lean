/-
# Which map is parity? The candidate involutions on `H_n(q)`, the trace and the γγ words

Bean `qou-99qc`. Owner (Carl), 2026-11-21: *"Settle which map is parity"* — the premise on which
decision (d) of `docs/audits/2026-11-21-pair-word-derivation-vs-physics-brief.md` turns (are the
mirror vertices `V̄ᵢ = σᵢ⁻¹σᵢ₊₁` γγ vertices?).

The photon is `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` (`QOU.Photon.photon`, owner ruling).

Maps compared (`h = q − q⁻¹`, `s` a Hecke letter):

* **braid mirror** `σ ↦ σ⁻¹` with `q` fixed — the corpus's `conj:p-from-braid-mirror` (P);
* **bar** `σ ↦ σ⁻¹`, `q ↦ q⁻¹` — semilinear; `Helicity.flip` with the parameter inverted;
* **eigenline swap** `ι : σ ↦ h − σ = −σ⁻¹`, `q` fixed — `Helicity.swap`;
* **word reversal** (the corpus's `conj:t-from-trace-cyclicity`, T) and the **group inverse**
  (= braid mirror ∘ reversal, the corpus's P·T);
* **`u ↔ d` flip** — not a map on `H_n`; on the Jimbo representation it is bar
  (`flip_diag`, PR #8706, and the exact probe below).

## What this file proves (generic field `K`, generic `K`-algebra `A`; no `ℝ`, no `sorry`)

§1 **The braid mirror at fixed `q` is not a map of `H_n(q)`.** If `σ⁻¹` satisfied the Hecke
relation at the same `q` then `2h = 0` (`flip_letter_same_q`). So the corpus's P is an
automorphism of the braid group `B_n` only; on the Hecke algebra a crossing mirror must either
invert `q` (bar) or carry the sign twist (`ι`). Neither preserves the convention-D trace at a
fixed `q` (`trace_flip`, `trace_swap`, `zD_sub_h`, `h_sub_zD`, `zD_sub_h_ne`, `h_sub_zD_ne`):
the braid mirror sends the Markov parameter `z_D` to `z_D − h = z_D(q⁻¹)` (Jones mirror), and
`ι` sends it to `h − z_D = −z_D(q⁻¹)`. In particular the trace-preservation component of the
corpus's `conj:cpt-d6-d7-d8-closure` fails for the named P at `n = 2`, `β = σ`, whenever
`h ≠ 0` (scope (b); the invariant is the Hecke relation).

§2 **Both crossing-mirror lifts exchange the left and right lines.** For `|q| > 1`, the left line
of the image letter is the right line of the original letter, for `ι` (`iota_leftLine`) and for
bar (`bar_leftLine`); the weak-vertex insertion `−h·P_L` goes to `−h·P_R` under `ι`
(`iota_insertion`) and to `+h·P_R` under bar (`bar_insertion`).

§3 **`ι` is an algebra automorphism of the `H₃` relations** (`swap_swap`, `iota_heckeH3Rel`),
sends `V ↦ V̄` (`Helicity.iota_vertex`, already in the corpus), and maps the photon family into
itself up to the scalar `1 + h(φ₀ + φ₁)` (`iota_photon`); bar does the same with `1 − h(φ₀+φ₁)`
(`bar_photon`). **But `ι` does not descend to the Jimbo image** (`iota_not_descend`): if a
nonzero vector is a common `q`-eigenvector of `σ₀, σ₁` and the Temperley–Lieb relation
`E₀E₁E₀ = E₀` (`E = q − σ`) holds, no `K`-algebra map extends `ι`. Both hypotheses hold on the
Jimbo representation `V^{⊗3}` at `|000⟩` (exact check,
`computations/probes/pair_word_brief/parity_map_probe.py`, 33/33).

§4 **`V̄ = (σ₁σ₀)·V·(σ₁σ₀)⁻¹` in any group with the braid relation** (`mirror_conj`), hence
`V̄³` is conjugate to `V³` (`mirror_pow_conj`) and every trace agrees on them
(`trace_mirror_pow`). The group inverse of `V` is conjugate to `V` by the half twist
(`inverse_conj`).

§5 **Words.** The γγ grammar is not closed under the corpus's P (`not_gg_mirror`), its T
(`not_gg_rev`) or its P·T (`not_gg_inv`), and **is** closed under P·T followed by the inner
half-twist rotation on `B₃` (`cpt_rotation_vpow`): P·T maps `V₀ᵏ` to a conjugate of itself.

## Not established here

That any of these maps IS physical parity. That reading needs an owner definition (the corpus's
P is a conjecture, and §1 shows it is not a symmetry of the Hecke algebra at fixed `q`). The
Jimbo hypotheses of `iota_not_descend` are checked by exact computation, not proved in Lean.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-- Ref: [kassel2008] https://doi.org/10.1007/978-0-387-68548-9
-/
import QOU.QuarkState.WeakVertexLeftProjector
import QOU.QuarkState.ChiralityPairBit
import QOU.Mass.BorromeanPhotonFactorisation
import QOU.Mass.GammaGammaWordSelection

namespace QOU.QBeta.ParityMapCandidates

/-! ## §1 The braid mirror at fixed `q`, and the trace -/

section Letter

open QOU.QuarkState.Helicity

variable {K A : Type*} [Field K] [Ring A] [Algebra K A] {q : K} {s : A}

/-- **The braid mirror at fixed `q` is not a letter.** If `σ⁻¹ = σ − h` satisfied the Hecke
relation at the same `q`, then `2h = 0`. -/
theorem flip_letter_same_q [Nontrivial A] (hs : IsLetter q s) (hf : IsLetter q (flip q s)) :
    (2 : K) * (q - q⁻¹) = 0 := by
  set c : K := q - q⁻¹ with hc
  have hinv : s * flip q s = 1 := (inv_letter hs).1
  have e1 : flip q s * flip q s = s * s - (2 * c) • s + (c * c) • (1 : A) := by
    simp only [QOU.QuarkState.Helicity.flip, ← hc, sub_mul, mul_sub, smul_mul_assoc,
      mul_smul_comm, one_mul, mul_one]
    module
  unfold IsLetter at hs hf
  rw [← hc] at hs hf
  rw [e1, hs] at hf
  have key : ((2 : K) * c) • flip q s = 0 := by
    have h2 : ((2 : K) * c) • flip q s =
        (c • flip q s + 1) - (c • s + 1 - (2 * c) • s + (c * c) • (1 : A)) := by
      simp only [QOU.QuarkState.Helicity.flip, ← hc]; module
    rw [h2, ← hf, sub_self]
  have h1 : ((2 : K) * c) • (1 : A) = 0 := by
    have := congrArg (fun x => s * x) key
    simpa [mul_smul_comm, hinv] using this
  have h3 : algebraMap K A ((2 : K) * c) = 0 := by
    rw [Algebra.algebraMap_eq_smul_one]; exact h1
  exact (map_eq_zero_iff _ (algebraMap K A).injective).mp h3

/-- A trace with `τ 1 = 1`, `τ σ = z` gives `τ(σ⁻¹) = z − h` (the braid mirror). -/
theorem trace_flip (τ : A →ₗ[K] K) {z : K} (h1 : τ 1 = 1) (hz : τ s = z) :
    τ (flip q s) = z - (q - q⁻¹) := by
  simp [QOU.QuarkState.Helicity.flip, map_sub, map_smul, h1, hz]

/-- ... and `τ(ι σ) = h − z` (the eigenline swap). -/
theorem trace_swap (τ : A →ₗ[K] K) {z : K} (h1 : τ 1 = 1) (hz : τ s = z) :
    τ (swap q s) = (q - q⁻¹) - z := by
  simp [swap, map_sub, map_smul, h1, hz]

end Letter

section Scalars

variable {K : Type*} [Field K] {q : K}

/-- The convention-D Markov parameter `z_D = q³/(q² + 1)`. -/
def zD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- **Jones mirror:** `z_D(q) − h = z_D(q⁻¹)`. The braid mirror at `q` equals the unmirrored
letter at `q⁻¹`, at the level of the Markov parameter. -/
theorem zD_sub_h (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) : zD q - (q - q⁻¹) = zD q⁻¹ := by
  have hq2' : (q⁻¹) ^ 2 + 1 ≠ 0 := by
    rw [inv_pow]; intro h
    apply hq2
    have : q ^ 2 * ((q ^ 2)⁻¹ + 1) = 0 := by rw [h, mul_zero]
    rw [mul_add, mul_inv_cancel₀ (pow_ne_zero 2 hq), mul_one] at this
    linear_combination this
  have h' : 1 + q ^ 2 ≠ 0 := by rwa [add_comm]
  unfold zD
  field_simp
  ring

/-- `h − z_D = −z_D(q⁻¹)`: the eigenline swap moves the Markov parameter off `z_D`. -/
theorem h_sub_zD (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) : (q - q⁻¹) - zD q = -zD q⁻¹ := by
  rw [← zD_sub_h hq hq2]; ring

/-- The braid mirror moves the trace of a letter whenever `h ≠ 0`. -/
theorem zD_sub_h_ne (hh : q - q⁻¹ ≠ 0) : zD q - (q - q⁻¹) ≠ zD q := by
  intro e; exact hh (sub_eq_self.mp e)

/-- The eigenline swap moves the trace of a letter whenever `q⁴ + 1 ≠ 0`. -/
theorem h_sub_zD_ne (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    (q - q⁻¹) - zD q ≠ zD q := by
  intro e
  have hk : (q - q⁻¹) - 2 * zD q = -(q ^ 4 + 1) / (q * (q ^ 2 + 1)) := by
    unfold zD; field_simp; ring
  have h0 : (q - q⁻¹) - 2 * zD q = 0 := by linear_combination e
  rw [hk, div_eq_zero_iff, neg_eq_zero] at h0
  rcases h0 with h0 | h0
  · exact h4 h0
  · exact mul_ne_zero hq hq2 h0

end Scalars

/-! ## §2 Left and right lines -/

section Lines

open QOU.QuarkState.Helicity

open QOU.QuarkState.LeftLine QOU.QuarkState.WeakVertexLeftProjector

variable {K A : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] [Ring A] [Algebra K A]
variable {q : K} {s : A}

/-- **`ι` exchanges the lines:** the left line of `ι σ` is the right line of `σ`. -/
theorem iota_leftLine (h1 : 1 < |q|) : leftLine q (swap q s) = rightLine q s := by
  rw [leftLine_of_one_lt h1, rightLine_of_one_lt h1, swap_Pp]

/-- **Bar exchanges the lines:** the left line of `σ⁻¹` at `q⁻¹` is the right line of `σ`. -/
theorem bar_leftLine (h1 : 1 < |q|) : leftLine q⁻¹ (flip q s) = rightLine q s := by
  have hn : ¬ 1 < |q⁻¹| := by
    rw [abs_inv]
    exact not_lt.mpr (inv_le_one_of_one_le₀ h1.le)
  rw [leftLine_of_not_one_lt hn, rightLine_of_one_lt h1, flip_Pm]

/-- The weak-vertex insertion of the `ι`-image letter is `−h·P_R` of the original letter. -/
theorem iota_insertion (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) (h1 : 1 < |q|) :
    weakVertex q (swap q s) - swap q s = -((q - q⁻¹) • rightLine q s) := by
  rw [weakVertex_sub_letter hq hq2 (swap_hecke hs), iota_leftLine h1]

/-- The weak-vertex insertion of the bar-image letter is `+h·P_R` of the original letter. -/
theorem bar_insertion (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q s) (h1 : 1 < |q|) :
    weakVertex q⁻¹ (flip q s) - flip q s = (q - q⁻¹) • rightLine q s := by
  have hq2' : q⁻¹ + q⁻¹⁻¹ ≠ 0 := by rwa [inv_inv, add_comm]
  rw [weakVertex_sub_letter (inv_ne_zero hq) hq2' (flip_hecke hs), bar_leftLine h1, inv_inv,
    ← neg_smul, neg_sub]

end Lines

/-! ## §3 `ι` on the `H₃` relations, the photon, and the Jimbo image -/

section Iota

open QOU.QuarkState.Helicity

open QOU.Photon (photon Colour)
open QOU.Mass.BorromeanPhotonFactorisation (HeckeH3Rel)

variable {K A : Type*} [Field K] [Ring A] [Algebra K A] {q : K} {a b : A}

theorem swap_swap (s : A) : swap q (swap q s) = s := by unfold swap; abel

/-- The inverse letters satisfy the braid relation. -/
theorem flip_braid (ha : IsLetter q a) (hb : IsLetter q b) (hab : a * b * a = b * a * b) :
    flip q a * flip q b * flip q a = flip q b * flip q a * flip q b := by
  let ua : Aˣ := ⟨a, flip q a, (inv_letter ha).1, (inv_letter ha).2⟩
  let ub : Aˣ := ⟨b, flip q b, (inv_letter hb).1, (inv_letter hb).2⟩
  have e : ua * ub * ua = ub * ua * ub := Units.ext (by simpa [ua, ub] using hab)
  have e' : (ua * ub * ua)⁻¹ = (ub * ua * ub)⁻¹ := by rw [e]
  have e'' := congrArg Units.val e'
  simpa [ua, ub, mul_inv_rev, mul_assoc] using e''

/-- **`ι` preserves the `H₃` relations** (an algebra automorphism of `H₃(q)`, `q` fixed). -/
theorem iota_heckeH3Rel (H : HeckeH3Rel (q - q⁻¹) a b) :
    HeckeH3Rel (q - q⁻¹) (swap q a) (swap q b) where
  quad_a := swap_hecke (s := a) H.quad_a
  quad_b := swap_hecke (s := b) H.quad_b
  braid := by
    have := flip_braid (q := q) H.quad_a H.quad_b H.braid
    simp only [swap_eq_neg_flip, neg_mul, mul_neg, neg_neg]
    rw [this]

/-- **`ι` maps the photon family into itself, up to the scalar `1 + h(φ₀ + φ₁)`:**
`ι(γ(φ₀, φ₁, φ₀₁)) − (1 + h(φ₀+φ₁))·1 = γ(hφ₀₁ − φ₀, −φ₁ − hφ₀₁, φ₀₁) − 1`. -/
theorem iota_photon (H : HeckeH3Rel (q - q⁻¹) a b) (φ : Colour K) :
    photon (swap q a) (iota_heckeH3Rel H).unitB φ =
      (1 + (q - q⁻¹) * (φ.phi0 + φ.phi1)) • (1 : A) +
        (photon a H.unitB (⟨(q - q⁻¹) * φ.phi01 - φ.phi0, -φ.phi1 - (q - q⁻¹) * φ.phi01,
          φ.phi01⟩ : Colour K) - 1) := by
  simp only [photon, QOU.Photon.vertex, HeckeH3Rel.unitB_val, HeckeH3Rel.unitB_inv, swap,
    sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one, smul_sub, smul_smul]
  module

/-- **Bar maps the photon family into itself, up to the scalar `1 − h(φ₀ + φ₁)`** (the letters
`σ⁻¹` at `q⁻¹`; the colour weights are free). -/
theorem bar_photon (H : HeckeH3Rel (q - q⁻¹) a b) (φ : Colour K) :
    photon (flip q a) (⟨flip q b, b, (inv_letter H.quad_b).2, (inv_letter H.quad_b).1⟩ : Aˣ) φ =
      (1 - (q - q⁻¹) * (φ.phi0 + φ.phi1)) • (1 : A) +
        (photon a H.unitB (⟨φ.phi0 + (q - q⁻¹) * φ.phi01, φ.phi1 - (q - q⁻¹) * φ.phi01,
          φ.phi01⟩ : Colour K) - 1) := by
  simp only [photon, QOU.Photon.vertex, HeckeH3Rel.unitB_val, HeckeH3Rel.unitB_inv,
    QOU.QuarkState.Helicity.flip, sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul,
    mul_one, smul_sub, smul_smul]
  module

/-- **`ι` does not descend to the Jimbo image.** Let `ρ : A → End(M)` be a representation in
which a nonzero `v` is a common `q`-eigenvector of `ρ σ₀`, `ρ σ₁` and the Temperley–Lieb relation
`E₀E₁E₀ = E₀` (`E = q − σ`) holds in `A` (e.g. `A` = the Jimbo image). Then no `K`-algebra
endomorphism of `A` sends `σᵢ ↦ ι σᵢ`: it would send the TL relation to `F₀F₁F₀ = F₀`
(`F = σ + q⁻¹`), which is false on `v` unless `[2]² = 1`. -/
theorem iota_not_descend {M : Type*} [AddCommGroup M] [Module K M]
    (ρ : A →ₐ[K] Module.End K M) {v : M} (hv : v ≠ 0) (hq2 : q + q⁻¹ ≠ 0)
    (h3 : (q + q⁻¹) ^ 2 ≠ 1) (hav : ρ a v = q • v) (hbv : ρ b v = q • v)
    (hTL : (q • (1 : A) - a) * (q • (1 : A) - b) * (q • (1 : A) - a) = q • (1 : A) - a) :
    ¬ ∃ φ : A →ₐ[K] A, φ a = swap q a ∧ φ b = swap q b := by
  rintro ⟨φ, ha, hb⟩
  have hE : ∀ x : A, φ x = swap q x → φ (q • (1 : A) - x) = x + q⁻¹ • (1 : A) := by
    intro x hx
    rw [map_sub, map_smul, map_one, hx]; unfold swap; module
  have hF := congrArg φ hTL
  rw [map_mul, map_mul, hE a ha, hE b hb] at hF
  have hFv : ∀ x : A, ρ x v = q • v → ρ (x + q⁻¹ • (1 : A)) v = (q + q⁻¹) • v := by
    intro x hx
    rw [map_add, map_smul, map_one, LinearMap.add_apply, LinearMap.smul_apply, hx,
      Module.End.one_apply, add_smul]
  have h1 : ρ ((a + q⁻¹ • (1 : A)) * (b + q⁻¹ • (1 : A)) * (a + q⁻¹ • (1 : A))) v =
      ρ (a + q⁻¹ • (1 : A)) v := by rw [hF]
  rw [map_mul, map_mul, Module.End.mul_apply, Module.End.mul_apply] at h1
  simp only [hFv a hav, hFv b hbv, LinearMap.map_smul, smul_smul] at h1
  have h2 : ((q + q⁻¹) * (q + q⁻¹) * (q + q⁻¹) - (q + q⁻¹)) • v = 0 := by
    rw [sub_smul, h1, sub_self]
  rcases smul_eq_zero.mp h2 with h | h
  · apply h3
    have : (q + q⁻¹) * ((q + q⁻¹) ^ 2 - 1) = 0 := by linear_combination h
    rcases mul_eq_zero.mp this with h' | h'
    · exact absurd h' hq2
    · exact sub_eq_zero.mp h'
  · exact hv h

end Iota

/-! ## §4 `V̄` is conjugate to `V` -/

section Conj

variable {G : Type*} [Group G] {a b : G}

/-- **`V̄ = (ba)·V·(ba)⁻¹`** with `V = ab⁻¹`, `V̄ = a⁻¹b`, in any group with `aba = bab`. -/
theorem mirror_conj (hab : a * b * a = b * a * b) :
    (b * a) * (a * b⁻¹) * (b * a)⁻¹ = a⁻¹ * b := by
  rw [mul_inv_eq_iff_eq_mul]
  calc b * a * (a * b⁻¹) = a⁻¹ * (a * b * a) * a * b⁻¹ := by group
    _ = a⁻¹ * (b * a * b) * a * b⁻¹ := by rw [hab]
    _ = a⁻¹ * b * (a * b * a) * b⁻¹ := by group
    _ = a⁻¹ * b * (b * a * b) * b⁻¹ := by rw [hab]
    _ = a⁻¹ * b * (b * a) := by group

/-- `V̄ᵏ = (ba)·Vᵏ·(ba)⁻¹`; in particular `V̄³` and `V³` are conjugate. -/
theorem mirror_pow_conj (hab : a * b * a = b * a * b) (k : ℕ) :
    (b * a) * (a * b⁻¹) ^ k * (b * a)⁻¹ = (a⁻¹ * b) ^ k := by
  rw [← mirror_conj hab, conj_pow]

/-- **The group inverse of `V` is conjugate to `V` by the half twist `Δ = aba`.** -/
theorem inverse_conj (hab : a * b * a = b * a * b) :
    (a * b * a) * (b * a⁻¹) * (a * b * a)⁻¹ = a * b⁻¹ := by
  rw [mul_inv_eq_iff_eq_mul]
  calc a * b * a * (b * a⁻¹) = a * (b * a * b) * a⁻¹ := by group
    _ = a * (a * b * a) * a⁻¹ := by rw [hab]
    _ = a * b⁻¹ * (b * a * b) := by group
    _ = a * b⁻¹ * (a * b * a) := by rw [hab]

/-- Every trace (`τ(xy) = τ(yx)`) takes the same value on `V̄ᵏ` and `Vᵏ`. -/
theorem trace_mirror_pow {A K : Type*} [Ring A] (τ : A → K) (hτ : ∀ x y, τ (x * y) = τ (y * x))
    {a b : Aˣ} (hab : a * b * a = b * a * b) (k : ℕ) :
    τ (((a⁻¹ * b) ^ k : Aˣ) : A) = τ (((a * b⁻¹) ^ k : Aˣ) : A) := by
  rw [← mirror_pow_conj hab k]
  set g := b * a
  rw [Units.val_mul, Units.val_mul, hτ, ← mul_assoc, Units.inv_mul, one_mul]

end Conj

/-! ## §5 The γγ words under the corpus's P, T and P·T -/

section Words

open QOU.Mass.GammaGammaWordSelection

/-- The corpus's P on words (`conj:p-from-braid-mirror`): every crossing changes sign. -/
def wMirror (w : Word) : Word := w.map fun c => ⟨c.gen, !c.pos⟩

/-- The corpus's T on words (`conj:t-from-trace-cyclicity`): reverse, signs kept. -/
def wRev (w : Word) : Word := w.reverse

/-- P·T: the group inverse. -/
def wInv (w : Word) : Word := (wMirror w).reverse

/-- The half-twist rotation on `B₃`: `σ₀ ↔ σ₁` (inner, conjugation by `Δ`). -/
def wFlip3 (w : Word) : Word := w.map fun c => ⟨1 - c.gen, c.pos⟩

theorem writhe_wMirror (w : Word) : writhe (wMirror w) = -writhe w := by
  induction w with
  | nil => simp [writhe, wMirror]
  | cons c t ih =>
    simp only [writhe, wMirror, List.map_cons, List.sum_cons] at ih ⊢
    rw [ih]; cases c with | mk g p => cases p <;> simp [sign] <;> ring

theorem writhe_wRev (w : Word) : writhe (wRev w) = writhe w := by
  simp [writhe, wRev, List.map_reverse, List.sum_reverse]

theorem gg_length_two {w : Word} (hw : GammaGammaWord w) (hl : w.length = 2) :
    ∃ i, w = vertex i := by
  cases hw with
  | nil => simp at hl
  | cons i hw' =>
    refine ⟨i, ?_⟩
    have : _ := hl
    simp [vertex] at this
    simp [this]

theorem not_gg_mirror : ¬ GammaGammaWord (wMirror (vertex 0)) := by
  intro h
  obtain ⟨i, hi⟩ := gg_length_two h (by simp [wMirror, vertex])
  simp [wMirror, vertex] at hi

theorem not_gg_rev : ¬ GammaGammaWord (wRev (vertex 0)) := by
  intro h
  obtain ⟨i, hi⟩ := gg_length_two h (by simp [wRev, vertex])
  simp [wRev, vertex] at hi

theorem not_gg_inv : ¬ GammaGammaWord (wInv (vertex 0)) := by
  intro h
  obtain ⟨i, hi⟩ := gg_length_two h (by simp [wInv, wMirror, vertex])
  simp [wInv, wMirror, vertex] at hi

/-- `V₀ᵏ` as a word. -/
def vpow : ℕ → Word
  | 0 => []
  | k + 1 => vertex 0 ++ vpow k

theorem vpow_gg (k : ℕ) : GammaGammaWord (vpow k) := by
  induction k with
  | zero => exact GammaGammaWord.nil
  | succ k ih => exact GammaGammaWord.cons 0 ih

theorem vpow_succ' (k : ℕ) : vpow (k + 1) = vpow k ++ vertex 0 := by
  induction k with
  | zero => simp [vpow]
  | succ k ih =>
    show vertex 0 ++ vpow (k + 1) = (vertex 0 ++ vpow k) ++ vertex 0
    rw [ih, List.append_assoc]

/-- **P·T followed by the half-twist rotation fixes `V₀ᵏ`.** So the corpus's P·T maps the γγ word
`V₀ᵏ` to a `Δ`-conjugate of itself (same closure, same trace). -/
theorem cpt_rotation_vpow (k : ℕ) : wFlip3 (wInv (vpow k)) = vpow k := by
  induction k with
  | zero => simp [vpow, wFlip3, wInv, wMirror]
  | succ k ih =>
    have hsplit : wFlip3 (wInv (vpow (k + 1))) =
        wFlip3 (wInv (vpow k)) ++ wFlip3 (wInv (vertex 0)) := by
      simp [vpow, wFlip3, wInv, wMirror, List.map_append, List.reverse_append]
    rw [hsplit, ih, vpow_succ']
    simp [wFlip3, wInv, wMirror, vertex]

end Words

end QOU.QBeta.ParityMapCandidates
