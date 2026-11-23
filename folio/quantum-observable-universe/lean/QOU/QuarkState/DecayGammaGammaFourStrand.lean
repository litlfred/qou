/-
# The β-decay as a γγ process on four strands, and what energy conservation forces

Bean `qou-99qc`. Owner (Carl), 2026-11-20: *"Q_β must be DERIVED, not chosen"* and *"We should be
able to algebraically derive the formula for Q_β from the γγ production."* Pre-registered in
`computations/probes/qbeta_derivation_r4_r1/PREREGISTRATION.md` before anything here was computed.

Photon throughout: `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` (ruled; `QOU/Photon.lean`).

## Setting

The explicit `(3,1)` representation of `H₄(q)` of `FlavourDoubletFourStrands.lean`. The `H₃` letters
`σ₀, σ₁` of the photon are the `H₄` letters `σ₁, σ₂` there (`s1`, `s2`), so the chiral vertex is
`V = s1·s2⁻¹`. The flavour doublet sits on the left line of `s1`, with two labels: **A**, the `σ₃`
lines `Lu, Ld`; **B**, the `J₄` lines `Ja, Jb`.

## R1 — the transition amplitude d → u of the γγ pair (proved)

* `flip_word_*`: on label A, the d → u sandwich `Lu·w·Ld` of the six normal-form words of `H₃` is
  `0, 0, eS, q·eS, q·eS, q²·eS` for `1, σ₀, σ₁, L₋ = σ₁σ₀, L₊ = σ₀σ₁, e⁻ = σ₀σ₁σ₀`.
  So the flip functional is `λ_A(w) = q^{(number of σ₀)}` on words containing `σ₁`, and `0` otherwise.
* `flip_pair`: for the γγ pair `Γ = γ(φ)γ(ψ)`,
  `Lu·Γ·Ld = (c_{σ₁} + q(c_{L₋} + c_{L₊}) + q²·c_{e⁻})·eS`, where `c_w` are the normal-form
  coordinates of `Γ` (`nf2 … nf5`, equal to `pairNFChiral`'s, `nf_eq_pairNFChiral`).
* `pair_eq_V3`, `flip_V3`, `flip_V3_back`: at the only derived colour weights
  `φ = (0, 0, qh)`, `ψ = (0, 0, −q⁻¹h)` the pair is `V³`, and its flip amplitude is
  `q²h³·eS` (and `q²h³·fS` back). **The Borromean γγ base flips flavour only at order `h³`.**
* `nf5_derived`: at those weights the `e⁻` coordinate `φ₀₁ψ₀ + φ₁ψ₀₁` is `0`. An `e⁻`-channel
  amplitude needs `φ₀` or `φ₁ ≠ 0`, and those weights are not derived in the corpus.
* `roundTrip_V3`: `tr(Lu·V³·Ld·V³) = (q²h³)²·(q⁴+1)/(q²+1)²`, i.e. `(q²h³)²` times the ruled
  convention-D weight `y₃` (`FlavourRoundTrip.roundTrip_A`).
* Label B: `Ja_photon`: `Ja·γ(φ) = t(φ)·Ja` with `t(φ) = 1 + qφ₀ + qφ₁ + φ₀₁`, the trivial
  character. Hence `pair_no_flip_B` (an `H₃` pair alone never flips the `J₄` label) and
  `pair_flip_B`: through the strand-4 vertex `V₄ = σ₂σ₃⁻¹`,
  `Ja·Γ·V₄·Jb = t(φ)t(ψ)q·eJ`. With the derived weights `t = 1` (`t_derived`).
* `weak_left`: the weak vertex of `σ₀` (`weakVertex − σ = −h·P_L`, `WeakVertexLeftProjector`) acts
  on either flavour line by `q⁻¹` instead of `q`: `Lu·(s1 − h·PL) = q⁻¹·Lu`.

## R4 — energy conservation in the mass channel (proved, ordered field)

`m_N = 2(m_μ·F_N − 6m_e)`, `F_N = |τ_N(β)|·[3]!/q³`, so `m_n − m_p = S·(|τ_n| − |τ_p|)` with
`S = 2m_μ[3]!/q³`. The plain traces of every element of `H₃(q)` on the two `T³ = ±½` weight spaces are
equal (positive words: `NucleonWeightSpaceTraces.trace_word_eq`; every element:
`HeckeWeightSpaceSymmetry.trace_ρn_eq_trace_ρp`, PR #8616, conjugation by the half-twist), so the `K`-weighted sectors are `q·t/[2]³` and
`q⁻¹·t/[2]³` with one `t`. Then:

* `sector_ratio`: `τ_n = q⁻²·τ_p` for every element: a relative difference `q⁻² − 1`, independent
  of the element.
* `qbeta_sector_neg`: for `q > 1`, `S > 0`, `m_e > 0`, `Q_β = S(|τ_n| − |τ_p|) − m_e < 0`. The
  neutron is lighter. Scope (b) for this normalisation; the invariant is the equal plain traces.
* `sector_dimnorm_eq`: normalised by each sector's own quantum dimension (`3q`, `3q⁻¹`) the two
  are equal, so `Q_β = −m_e`.
* `full_flip_eq`: the full trace is unchanged by `u ↔ d` (it swaps `q·t ↔ q⁻¹·t` and
  `q³ ↔ q⁻³`), so with the pinned proton `m_n = m_p` and `Q_β = −m_e`.

## What is NOT proved

That the decay's energy IS any of these round trips, which label is `n ↔ p`, or the MeV scale.
Base ring (§7c): generic `[Field K]`; an ordered field only for `qbeta_sector_neg`. No `ℝ`,
no `sorry`, no axiom, no class.

-- Ref: [humphreys1990] §7.4 (Hecke algebra, generic q)
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.QuarkState.FlavourDoubletFourStrands
import QOU.QuarkState.PhotonPairNormalForm
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Algebra.Order.Field.Basic

namespace QOU.QuarkState.DecayGammaGammaFourStrand

open Matrix

namespace F
export QOU.QuarkState.FlavourDoubletFour (s1 s2 s3 s1i s2i s3i Lu Ld PL eS fS Ja Jb eJ eS_eq fS_eq D_ne' D_ne'' J4_gg_vertex)
end F

/-- Entrywise check of a `3 × 3` matrix identity over a field. -/
local macro "mat3" : tactic =>
  `(tactic| ((try simp only [Matrix.mul_fin_three, Matrix.one_fin_three, Matrix.smul_of,
      Matrix.smul_vec3, Matrix.of_sub_of, Matrix.of_add_of]) <;> ext i j <;>
    fin_cases i <;> fin_cases j <;> (try simp) <;> (try field_simp) <;> (try ring) <;> (try simp)))

section Generic

variable {K : Type*} [Field K]

/-- `h = q − q⁻¹`. -/
def hh (q : K) : K := q - q⁻¹

/-- The photon `γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹` in the `(3,1)` of `H₄`
(`σ₀ ↦ F.s1`, `σ₁ ↦ F.s2`). -/
def photonM (q a0 a1 a2 : K) : Matrix (Fin 3) (Fin 3) K :=
  1 + a0 • F.s1 q + a1 • F.s2 q + a2 • (F.s1 q * F.s2i q)

/-- The chiral vertex `V = σ₀σ₁⁻¹`. -/
def V (q : K) : Matrix (Fin 3) (Fin 3) K := F.s1 q * F.s2i q

/-- Normal-form coordinates of `γ(a)γ(b)` on `σ₁, L₋, L₊, e⁻` (the canonical-chart
pair product, `pairNFChiral_eq`, at `h = q − q⁻¹`). -/
def nf2 (q a0 a1 a2 b0 b1 b2 : K) : K := a1 + b1 + hh q * a1 * b1 + a0 * b2 - hh q * (a2 * b2)
def nf3 (q a0 a1 a2 b0 b1 b2 : K) : K := a1 * b0 + a2 * b2 - hh q * (a1 * b2)
def nf4 (q a0 a1 a2 b0 b1 b2 : K) : K :=
  a2 + b2 + a0 * b1 + hh q * (a0 * b2) - hh q ^ 2 * (a2 * b2)
def nf5 (q a0 a1 a2 b0 b1 b2 : K) : K := a2 * b0 + a1 * b2

/-- The coordinates are those of the canonical γγ normal form. -/
theorem nf_eq_pairNFChiral (q a0 a1 a2 b0 b1 b2 : K) :
    pairNFChiral (q - q⁻¹) a0 a1 a2 b0 b1 b2 2 = nf2 q a0 a1 a2 b0 b1 b2 ∧
    pairNFChiral (q - q⁻¹) a0 a1 a2 b0 b1 b2 3 = nf3 q a0 a1 a2 b0 b1 b2 ∧
    pairNFChiral (q - q⁻¹) a0 a1 a2 b0 b1 b2 4 = nf4 q a0 a1 a2 b0 b1 b2 ∧
    pairNFChiral (q - q⁻¹) a0 a1 a2 b0 b1 b2 5 = nf5 q a0 a1 a2 b0 b1 b2 := by
  rw [pairNFChiral_eq]
  refine ⟨?_, ?_, ?_, ?_⟩ <;> simp [nf2, nf3, nf4, nf5, hh]

/-- The label-A flip coefficient of the γγ pair. -/
def flipCoeff (q a0 a1 a2 b0 b1 b2 : K) : K :=
  nf2 q a0 a1 a2 b0 b1 b2 + q * (nf3 q a0 a1 a2 b0 b1 b2 + nf4 q a0 a1 a2 b0 b1 b2)
    + q ^ 2 * nf5 q a0 a1 a2 b0 b1 b2

/-- The trivial character of the photon: `σ₀, σ₁ ↦ q`, `σ₀σ₁⁻¹ ↦ 1`. -/
def triv (q a0 a1 a2 : K) : K := 1 + q * a0 + q * a1 + a2

/-- At the derived colour weights both trivial characters multiply to `1`. -/
theorem t_derived {q : K} (hq : q ≠ 0) :
    triv q 0 0 (q * hh q) * triv q 0 0 (-(q⁻¹ * hh q)) = 1 := by
  unfold triv hh; field_simp; ring

variable {q : K} (hq : q ≠ 0) (hn : q ^ 2 + 1 ≠ 0)
include hq hn

/-! ### Label A: the six normal-form words -/

theorem flip_word_one : F.Lu * (1 : Matrix (Fin 3) (Fin 3) K) * F.Ld = 0 := by
  unfold F.Lu F.Ld; mat3

theorem flip_word_s0 : F.Lu * F.s1 q * F.Ld = 0 := by unfold F.Lu F.Ld F.s1; mat3

theorem flip_word_s1 : F.Lu * F.s2 q * F.Ld = F.eS q := rfl

theorem flip_word_Lm : F.Lu * (F.s2 q * F.s1 q) * F.Ld = q • F.eS q := by
  rw [F.eS_eq hq hn]; unfold F.Lu F.Ld F.s1 F.s2; mat3

theorem flip_word_Lp : F.Lu * (F.s1 q * F.s2 q) * F.Ld = q • F.eS q := by
  rw [F.eS_eq hq hn]; unfold F.Lu F.Ld F.s1 F.s2; mat3

theorem flip_word_em : F.Lu * (F.s1 q * F.s2 q * F.s1 q) * F.Ld = q ^ 2 • F.eS q := by
  rw [F.eS_eq hq hn]; unfold F.Lu F.Ld F.s1 F.s2; mat3

/-- **The γγ pair's d → u amplitude, label A.** -/
theorem flip_pair (a0 a1 a2 b0 b1 b2 : K) :
    F.Lu * (photonM q a0 a1 a2 * photonM q b0 b1 b2) * F.Ld =
      flipCoeff q a0 a1 a2 b0 b1 b2 • F.eS q := by
  rw [F.eS_eq hq hn]; unfold F.Lu F.Ld photonM F.s1 F.s2 F.s2i flipCoeff nf2 nf3 nf4 nf5 hh; mat3

set_option maxHeartbeats 2000000 in
/-- At the derived colour weights the pair is `V³` (`borromeanV3A_eq_switched_photon_product`,
here in the `(3,1)` of `H₄`). -/
theorem pair_eq_V3 :
    photonM q 0 0 (q * hh q) * photonM q 0 0 (-(q⁻¹ * hh q)) = V q * V q * V q := by
  unfold photonM V F.s1 F.s2i hh; mat3

omit hq hn in
/-- At the derived colour weights the `e⁻` coordinate vanishes. -/
theorem nf5_derived : nf5 q 0 0 (q * hh q) 0 0 (-(q⁻¹ * hh q)) = 0 := by
  simp [nf5]

/-- At the derived colour weights the flip coefficient is `q²h³`. -/
theorem flipCoeff_derived :
    flipCoeff q 0 0 (q * hh q) 0 0 (-(q⁻¹ * hh q)) = q ^ 2 * hh q ^ 3 := by
  unfold flipCoeff nf2 nf3 nf4 nf5 hh; field_simp; ring

/-- **The Borromean base flips flavour at order `h³`.** -/
theorem flip_V3 : F.Lu * (V q * V q * V q) * F.Ld = (q ^ 2 * hh q ^ 3) • F.eS q := by
  rw [← pair_eq_V3 hq hn, flip_pair hq hn, flipCoeff_derived hq hn]

/-- … and back. -/
theorem flip_V3_back : F.Ld * (V q * V q * V q) * F.Lu = (q ^ 2 * hh q ^ 3) • F.fS q := by
  rw [F.fS_eq hq hn]; unfold F.Lu F.Ld V F.s1 F.s2i hh; mat3

/-- **The round trip through the γγ base**: `(q²h³)²` times the convention-D weight. -/
theorem roundTrip_V3 :
    Matrix.trace (F.Lu * (V q * V q * V q) * F.Ld * (V q * V q * V q)) =
      (q ^ 2 * hh q ^ 3) ^ 2 * ((q ^ 4 + 1) / (q ^ 2 + 1) ^ 2) := by
  have hLu : (F.Lu : Matrix (Fin 3) (Fin 3) K) * F.Lu = F.Lu := by unfold F.Lu; mat3
  have hLd : (F.Ld : Matrix (Fin 3) (Fin 3) K) * F.Ld = F.Ld := by unfold F.Ld; mat3
  set W := V q * V q * V q
  have hc : Matrix.trace (F.Lu * W * F.Ld * W) =
      Matrix.trace ((F.Lu * W * F.Ld) * (F.Ld * W * F.Lu)) := by
    calc Matrix.trace (F.Lu * W * F.Ld * W)
        = Matrix.trace ((F.Lu * F.Lu) * W * (F.Ld * F.Ld) * W) := by rw [hLu, hLd]
      _ = Matrix.trace (F.Lu * (F.Lu * W * F.Ld * F.Ld * W)) := by simp only [mul_assoc]
      _ = Matrix.trace ((F.Lu * W * F.Ld * F.Ld * W) * F.Lu) := Matrix.trace_mul_comm _ _
      _ = Matrix.trace ((F.Lu * W * F.Ld) * (F.Ld * W * F.Lu)) := by simp only [mul_assoc]
  rw [hc, flip_V3 hq hn, flip_V3_back hq hn, smul_mul_smul_comm, Matrix.trace_smul,
    F.eS_eq hq hn, F.fS_eq hq hn]
  simp [Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three, hh]
  field_simp
  ring

/-! ### The weak vertex on the left line -/

/-- The weak vertex of `σ₀` acts on each flavour line by `q⁻¹`. -/
theorem weak_left : F.Lu * (F.s1 q - (q - q⁻¹) • F.PL) = q⁻¹ • F.Lu := by
  unfold F.Lu F.s1 F.PL; mat3

end Generic

/-! ### Label B -/

section LabelB

variable {K : Type*} [Field K] {q : K} (hq : q ≠ 0) (hn : q ^ 2 + 1 ≠ 0)
  (hD : q ^ 4 + q ^ 2 + 1 ≠ 0)
include hq hn hD

/-- On the `J₄`-line `Ja` (the `H₃` trivial sector) a photon acts by its trivial character. -/
theorem Ja_photon (a0 a1 a2 : K) : F.Ja q * photonM q a0 a1 a2 = triv q a0 a1 a2 • F.Ja q := by
  have := F.D_ne' hD; have := F.D_ne'' hD
  unfold F.Ja photonM triv F.s1 F.s2 F.s2i; mat3

/-- An `H₃` γγ pair alone never flips the `J₄` label. -/
theorem pair_no_flip_B (a0 a1 a2 b0 b1 b2 : K) :
    F.Ja q * (photonM q a0 a1 a2 * photonM q b0 b1 b2) * F.Jb q = 0 := by
  have := F.D_ne' hD; have := F.D_ne'' hD
  unfold F.Ja F.Jb photonM F.s1 F.s2 F.s2i; mat3

/-- **The γγ pair through the strand-4 vertex `V₄ = σ₂σ₃⁻¹`, label B.** -/
theorem pair_flip_B (a0 a1 a2 b0 b1 b2 : K) :
    F.Ja q * (photonM q a0 a1 a2 * photonM q b0 b1 b2 * (F.s2 q * F.s3i q)) * F.Jb q =
      (triv q a0 a1 a2 * triv q b0 b1 b2 * q) • F.eJ q := by
  have h1 : F.Ja q * photonM q a0 a1 a2 * photonM q b0 b1 b2 =
      (triv q a0 a1 a2 * triv q b0 b1 b2) • F.Ja q := by
    rw [Ja_photon hq hn hD, smul_mul_assoc, Ja_photon hq hn hD, smul_smul]
  calc F.Ja q * (photonM q a0 a1 a2 * photonM q b0 b1 b2 * (F.s2 q * F.s3i q)) * F.Jb q
      = (F.Ja q * photonM q a0 a1 a2 * photonM q b0 b1 b2) * (F.s2 q * F.s3i q) * F.Jb q := by
        simp only [mul_assoc]
    _ = (triv q a0 a1 a2 * triv q b0 b1 b2) • (F.Ja q * (F.s2 q * F.s3i q) * F.Jb q) := by
        rw [h1]; simp only [smul_mul_assoc]
    _ = _ := by rw [F.J4_gg_vertex hq hn hD, smul_smul]

end LabelB

/-! ### R4: energy conservation in the mass channel -/

section R4

variable {K : Type*} [Field K]

/-- The `T³ = −½` sector is `q⁻²` times the `T³ = +½` sector, for every element. -/
theorem sector_ratio (q t D : K) (hq : q ≠ 0) :
    q⁻¹ * t / D = (q ^ 2)⁻¹ * (q * t / D) := by
  field_simp

/-- Normalised by their own quantum dimensions (`3q`, `3q⁻¹`) the sectors agree. -/
theorem sector_dimnorm_eq (q t : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    q * t / (3 * q) = q⁻¹ * t / (3 * q⁻¹) := by
  field_simp

/-- The full `K`-weighted trace is unchanged by `u ↔ d`. -/
theorem full_flip_eq (q t D : K) :
    (q ^ 3 + q * t + q⁻¹ * t + q⁻¹ ^ 3) / D = (q⁻¹ ^ 3 + q⁻¹ * t + q * t + q ^ 3) / D := by
  ring

variable [LinearOrder K] [IsStrictOrderedRing K]

/-- **Energy conservation with the `T³` sectors as the two nucleons gives `Q_β < 0`.** -/
theorem qbeta_sector_neg (q t D S me : K) (hq : 1 < q) (hD : 0 < D) (hS : 0 < S)
    (hme : 0 < me) :
    S * (|q⁻¹ * t / D| - |q * t / D|) - me < 0 := by
  have hq0 : 0 < q := by linarith
  have hinv : q⁻¹ < q := by
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
    linarith
  rw [abs_div, abs_div, abs_mul, abs_mul, abs_of_pos hq0, abs_of_pos (inv_pos.mpr hq0),
    abs_of_pos hD]
  have hle : q⁻¹ * |t| / D ≤ q * |t| / D :=
    div_le_div_of_nonneg_right (mul_le_mul_of_nonneg_right hinv.le (abs_nonneg t)) hD.le
  nlinarith [mul_le_mul_of_nonneg_left (sub_nonpos.2 hle) hS.le]


end R4

section ClosedForm

variable {K : Type*} [Field K]

/-! ### The closed form these readings share

With `Q_β = |τ(Δ_S)|·E₀`, `τ(Δ_S) = −(h[2]/2)·y₃` (`QBetaChiralityReduction.tau_deltaS_eq_tau_J`) and the
order-zero `E₀ = m_e/(q(q−1))` (posited), every reading is `Q_β/m_e = (q+1)(q²+1)/(2q³)·y₃`.
All of the open content is in `y₃`. Form A is `y₃ = |q²−2q−1|/(q²+1)`. -/

/-- The common prefactor: `(h[2]/2)/(q(q−1)) = (q+1)(q²+1)/(2q³)`. -/
theorem prefactor_eq (q : K) (hq : q ≠ 0) (h1 : q - 1 ≠ 0) :
    (q - q⁻¹) * (q + q⁻¹) / 2 / (q * (q - 1)) = (q + 1) * (q ^ 2 + 1) / (2 * q ^ 3) := by
  field_simp; ring

/-- Label B through the strand-4 vertex (`y₃ = cJ/2`): the closed form. -/
theorem closedForm_B (q : K) (hq : q ≠ 0) (h1 : q - 1 ≠ 0) (hD : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    (q - q⁻¹) * (q + q⁻¹) / 2 / (q * (q - 1)) *
        ((q ^ 2 + 1) ^ 2 * (q ^ 4 + 1) / (q ^ 4 + q ^ 2 + 1) ^ 2) =
      (q + 1) * (q ^ 2 + 1) ^ 3 * (q ^ 4 + 1) / (2 * q ^ 3 * (q ^ 4 + q ^ 2 + 1) ^ 2) := by
  field_simp; ring

/-- Label A through the γγ base `V³` (`y₃ = (q²h³)²·y_D`): the closed form. -/
theorem closedForm_A_V3 (q : K) (hq : q ≠ 0) (h1 : q - 1 ≠ 0) (hn : q ^ 2 + 1 ≠ 0) :
    (q - q⁻¹) * (q + q⁻¹) / 2 / (q * (q - 1)) *
        ((q ^ 2 * (q - q⁻¹) ^ 3) ^ 2 * ((q ^ 4 + 1) / (q ^ 2 + 1) ^ 2)) =
      (q + 1) * (q ^ 2 - 1) ^ 6 * (q ^ 4 + 1) / (2 * q ^ 5 * (q ^ 2 + 1)) := by
  field_simp; ring


end ClosedForm

end QOU.QuarkState.DecayGammaGammaFourStrand
