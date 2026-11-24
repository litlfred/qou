import QOU.StandardModel.ComponentFraming
import QOU.StandardModel.SignCoherentTwist
import QOU.Eightfold.USpinColemanGlashowLambdaSigma
import Mathlib.Data.Int.ModEq
import Mathlib.Tactic

set_option autoImplicit false

/-!
# Post-`2026-11-21` Hopf-Link Framing Constraints, Complete Coherence Window, Asselmeyer–Maluga Hirzebruch Defect, and Charge-Free Coleman–Glashow (`qou-kebu`, `qou-qvpl`, `qou-pwz4`, `qou-krgl`)

Non-conjectural algebraic formalization (`0 sorry`, `0 axiom`) advancing the untouched `Q-Drain-7`
items under the `2026-11-20..22` owner rulings (`docs/coordination/owner-rulings.md` rows 36, 37,
59, 113):

1. **Section 1 — Post-`2026-11-21` Hopf-Link Electron (`σ₀σ₁σ₀ ∈ B₃`) Component Framing (`qou-kebu`):**
   - `QOU.StandardModel.ComponentFraming` proved `e_framing_is_neg_one` under the pre-`2026-11-21`
     premise that the electron closes to a 1-component knot (`π` transitive, true only for the
     trefoil backup `σ₀³ ∈ B₂` / `(σ₀σ₁)² ∈ B₃`).
   - Under the `2026-11-21` ruling, the primary electron word is `σ₀σ₁σ₀ ∈ B₃`, whose closure is
     the 2-component Hopf link with underlying permutation `piHopf = swap 0 2` (cycle type `(2,1)`).
   - We prove `piHopf_not_transitive`, `isComponentFraming_piHopf_iff` (`t 0 = t 2`),
     `hopf_electron_forced_with_range` (`t ∈ {-1, 0, 1}³` and `∑ t = -3` still force `t = (-1,-1,-1)`),
     and `hopf_electron_unconstrained_without_range` (without the `{-1, 0, 1}` single-twist cap,
     `![a, -3 - 2a, a]` is a valid `piHopf` component framing for every `a ∈ ℤ`, making the
     `{-1, 0, 1}` range cap load-bearing for `e⁻` on the Hopf link).

2. **Section 2 — Complete Coherence Load-Bearing Window (`qou-kebu`):**
   - Discharges the corollary left unproved in `SignCoherentTwist.lean:302–320`
     (`signCoherent_of_total_two` and `signCoherent_of_abs_total_ge_two`), and proves the exact
     equivalence `exists_incoherent_in_range_iff`: a mixed-sign assignment in `{-1, 0, 1}³` with
     total `T` exists **if and only if** `T ∈ {-1, 0, +1}`.

3. **Section 3 — Asselmeyer–Maluga `arXiv:1910.09966` §5.2–5.3 Hirzebruch Defect `h = 3σ - p₁` & Baez–Huerta `ℤ₆` Check (`qou-qvpl` Open Checks B & C + Rule-13a Guard for Check A):**
   - Formalizes `1910.09966` §5.2–5.3's actual Hirzebruch framing defect
     `hirzebruchDefect sig p1 = 3 * sig - p1` (fixing the Seifert-signature misreading of closed PR `#8149`
     noted by W12):
     * `hirzebruchDefect_mod_three`: `3 * sig - T ≡ -T [ZMOD 3]`, so the fractional `ℤ/3ℤ` charge
       class comes entirely from `-p₁ = -T(t)` while `sig ↦ sig + Δσ` shifts `h` by `3 Δσ`
       (and `1910.09966` §5.3 imports the `/3` normalization and defines no `I₃` or `Y`).
     * `zeroLinking_unitFraming_hirzebruchDefect_eq_two_mul_sum`: on any zero-linking `n`-component
       link (such as the QOU Borromean carrier `V³` where `lk_{ij} = 0`, so the surgery linking
       matrix is `Λ = diag(t₁, …, tₙ)`), unit-range framings `tᵢ ∈ {-1, 0, 1}` satisfy
       `σ(Λ) = ∑ sgn(tᵢ) = T(t)`, forcing `3σ(Λ) - T(t) = 2 T(t) ∈ 2ℤ` (even numerator, unable to
       hit `3Q_d = -1` or `3Q_e = -3` without multi-twist `|tᵢ| ≥ 2`, non-zero linking, or extra
       closed 4-manifold summands `# ±ℂP²`).
     * `baez_huerta_z6_congruence_iff`: resolves Check C as an exact `ℤ` divisibility equivalence.
     * `CategoricalRibbonHyperchargeDerivationHypothesis`: zero-instance Rule-13a carrier keeping
       Check A (`Y_t = 2(T(t)/3 - I₃)` derivation from QOU axioms) explicitly open.

4. **Section 4 — Charge-Value-Free U-Spin Coleman–Glashow Theorem (`qou-pwz4`, `qou-krgl`):**
   - Under the `2026-11-22` owner ruling (`owner-rulings.md` row 59: quark charges `qᵢ` must be
     derived rather than adopted as `+2/3, -1/3`), upgrades `USpinColemanGlashowLambdaSigma` by
     proving `coleman_glashow_borromeanV3_any_charges`: over any `[Field K]`, for **arbitrary**
     quark charges `qu, qd, qs : K` satisfying U-spin equality `qd = qs`, the connected Borromean
     `V³` Coleman–Glashow combination vanishes identically for all `q : K`.

-- Ref: [arxiv-1910.09966v1] Asselmeyer-Maluga, arXiv:1910.09966v1 §5.2–5.3, pp. 25–26.
-- Ref: [baez-huerta2010] Baez & Huerta, Bull. Amer. Math. Soc. 47 (2010) 483–552.
-- Ref: [colemanglashow1961] Coleman & Glashow, Phys. Rev. Lett. 6 (1961) 423.
-/

namespace QOU.StandardModel.HopfFramingAndHirzebruchDefect

open Matrix
open QOU.StandardModel.ComponentFraming
open QOU.StandardModel.SignCoherentTwist
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm

/-! ## Section 1: Post-`2026-11-21` Hopf-Link Electron (`σ₀σ₁σ₀ ∈ B₃`) Component Framing -/

/-- Underlying strand permutation `(0 2) ∈ Perm (Fin 3)` of the ruled `2026-11-21` electron braid
word `σ₀σ₁σ₀ ∈ B₃` (whose closure is the 2-component Hopf link: strands `{0, 2}` form one component
and strand `{1}` forms the second component). -/
def piHopf : Equiv.Perm (Fin 3) := Equiv.swap 0 2

/-- Artin generator product `s₀ s₁ s₀ = (0 1)(1 2)(0 1)` in `Perm (Fin 3)` equals `piHopf = (0 2)`. -/
theorem piHopf_eq_s0_s1_s0 :
    Equiv.swap (0 : Fin 3) 1 * Equiv.swap 1 2 * Equiv.swap 0 1 = piHopf := by
  decide

/-- Every iterate of `piHopf` fixes strand `1`. -/
theorem piHopf_pow_apply_one (k : ℕ) : (piHopf ^ k) 1 = 1 := by
  induction k with
  | zero => rfl
  | succ m ih =>
    rw [pow_succ', Equiv.Perm.mul_apply, ih]
    decide

/-- **Non-Transitivity of the Hopf-Link Electron Permutation:**
Unlike the 1-component trefoil backup, `piHopf` is **not** transitive on `Fin 3`, so
`ComponentFraming.e_framing_is_neg_one`'s knot-transitivity hypothesis does not apply to `σ₀σ₁σ₀`. -/
theorem piHopf_not_transitive :
    ¬ (∀ i j : Fin 3, ∃ k : ℕ, (piHopf ^ k) i = j) := by
  intro htrans
  obtain ⟨k, hk⟩ := htrans 1 0
  rw [piHopf_pow_apply_one k] at hk
  exact absurd hk (by decide)

/-- Exact characterization of component framings on `piHopf = swap 0 2`: `t` is constant along
link components if and only if strands `0` and `2` carry equal twist (`t 0 = t 2`), leaving `t 1`
independent. -/
theorem isComponentFraming_piHopf_iff {t : Fin 3 → ℤ} :
    IsComponentFraming piHopf t ↔ t 0 = t 2 := by
  constructor
  · intro h
    have h2 := h 2
    have hp : piHopf 2 = 0 := by decide
    rw [hp] at h2
    exact h2
  · intro h02 i
    fin_cases i
    · change t (piHopf 0) = t 0
      have hp : piHopf 0 = 2 := by decide
      rw [hp, h02]
    · change t (piHopf 1) = t 1
      have hp : piHopf 1 = 1 := by decide
      rw [hp]
    · change t (piHopf 2) = t 2
      have hp : piHopf 2 = 0 := by decide
      rw [hp, h02]

/-- **With the `{-1, 0, 1}` single-twist range cap**, total twist `-3` still uniquely forces
`t = (-1, -1, -1)` on `Fin 3` by lower-bound saturation, without needing transitivity of `π`. -/
theorem hopf_electron_forced_with_range {t : Fin 3 → ℤ}
    (hrange : ∀ i, -1 ≤ t i ∧ t i ≤ 1)
    (htot : t 0 + t 1 + t 2 = -3) :
    ∀ i, t i = -1 := by
  have r0 := hrange 0
  have r1 := hrange 1
  have r2 := hrange 2
  have h0 : t 0 = -1 := by omega
  have h1 : t 1 = -1 := by omega
  have h2 : t 2 = -1 := by omega
  intro i
  fin_cases i <;> assumption

/-- **Without the `{-1, 0, 1}` single-twist range cap**, the 2-component Hopf link admits an
infinite `ℤ`-family `![a, -3 - 2a, a]` of valid component framings summing to `-3` (non-constant
whenever `a ≠ -1`, e.g. `![0, -3, 0]`). Thus moving `e⁻` from a 1-component knot to the 2-component
Hopf link makes the `{-1, 0, 1}` range cap load-bearing even for `e⁻`. -/
theorem hopf_electron_unconstrained_without_range (a : ℤ) :
    IsComponentFraming piHopf ![a, -3 - 2 * a, a] ∧
    (![a, -3 - 2 * a, a] 0 + ![a, -3 - 2 * a, a] 1 + ![a, -3 - 2 * a, a] 2 = -3) := by
  refine ⟨isComponentFraming_piHopf_iff.mpr rfl, ?_⟩
  simp
  ring

/-! ## Section 2: Complete Coherence Load-Bearing Window (`SignCoherentTwist` Corollary + Iff) -/

/-- **Corollary noted in `SignCoherentTwist.lean:302–320`:**
Every `t : Fin 3 → ℤ` in `{-1, 0, 1}³` with total `2` is automatically `SignCoherent`. -/
theorem signCoherent_of_total_two {t : Fin 3 → ℤ}
    (hrange : ∀ i, -1 ≤ t i ∧ t i ≤ 1)
    (hsum : t 0 + t 1 + t 2 = 2) :
    SignCoherent t := by
  obtain ⟨h0, h1, h2⟩ := no_mixed_sign_at_total_two hrange hsum
  have hall : ∀ i : Fin 3, 0 ≤ t i := by
    intro i
    fin_cases i <;> assumption
  exact coherent_iff_all_same_sign.mpr (Or.inl hall)

/-- General boundary saturation: for `t : Fin 3 → ℤ` in `{-1, 0, 1}³`, whenever `2 ≤ |t 0 + t 1 + t 2|`
(`T ∈ {-3, -2, +2, +3}`), `SignCoherent t` holds unconditionally. -/
theorem signCoherent_of_abs_total_ge_two {t : Fin 3 → ℤ}
    (hrange : ∀ i, -1 ≤ t i ∧ t i ≤ 1)
    (habs : 2 ≤ |t 0 + t 1 + t 2|) :
    SignCoherent t := by
  have r0 := hrange 0
  have r1 := hrange 1
  have r2 := hrange 2
  rcases le_or_gt 0 (t 0 + t 1 + t 2) with hnn | hneg
  · have hge2 : 2 ≤ t 0 + t 1 + t 2 := by
      rw [abs_of_nonneg hnn] at habs
      exact habs
    have p0 : 0 ≤ t 0 := by omega
    have p1 : 0 ≤ t 1 := by omega
    have p2 : 0 ≤ t 2 := by omega
    have hall : ∀ i : Fin 3, 0 ≤ t i := by intro i; fin_cases i <;> assumption
    exact coherent_iff_all_same_sign.mpr (Or.inl hall)
  · have hle2 : t 0 + t 1 + t 2 ≤ -2 := by
      rw [abs_of_neg hneg] at habs
      omega
    have n0 : t 0 ≤ 0 := by omega
    have n1 : t 1 ≤ 0 := by omega
    have n2 : t 2 ≤ 0 := by omega
    have hall : ∀ i : Fin 3, t i ≤ 0 := by intro i; fin_cases i <;> assumption
    exact coherent_iff_all_same_sign.mpr (Or.inr hall)

/-- **Exact Coherence Load-Bearing Window (`T ∈ {-1, 0, +1}`):**
In the single-twist cube `{-1, 0, 1}³`, a non-sign-coherent assignment of total twist `T` exists
**if and only if** `T = -1 ∨ T = 0 ∨ T = 1`. -/
theorem exists_incoherent_in_range_iff (T : ℤ) :
    (∃ t : Fin 3 → ℤ, (∀ i, -1 ≤ t i ∧ t i ≤ 1) ∧
      t 0 + t 1 + t 2 = T ∧ ¬ SignCoherent t) ↔
      (T = -1 ∨ T = 0 ∨ T = 1) := by
  constructor
  · rintro ⟨t, hrange, rfl, hinc⟩
    have r0 := hrange 0
    have r1 := hrange 1
    have r2 := hrange 2
    by_contra hnot
    have habs : 2 ≤ |t 0 + t 1 + t 2| := by
      rcases le_or_gt 0 (t 0 + t 1 + t 2) with hnn | hneg
      · rw [abs_of_nonneg hnn]; omega
      · rw [abs_of_neg hneg]; omega
    exact hinc (signCoherent_of_abs_total_ge_two hrange habs)
  · rintro (rfl | rfl | rfl)
    · refine ⟨![(-1 : ℤ), -1, 1], ?_, by decide, d_mixed_sign_not_coherent⟩
      intro i; fin_cases i <;> decide
    · refine ⟨![(-1 : ℤ), 0, 1], ?_, by decide, nu_mixed_sign_not_coherent⟩
      intro i; fin_cases i <;> decide
    · refine ⟨![(1 : ℤ), 1, -1], ?_, by decide, ?_⟩
      · intro i; fin_cases i <;> decide
      · intro h
        exact h ⟨0, 2, by decide, by decide⟩

/-! ## Section 3: Asselmeyer–Maluga `1910.09966` §5.2–5.3 Hirzebruch Defect & Baez–Huerta `ℤ₆` -/

/-- Asselmeyer–Maluga's 4-manifold Hirzebruch framing defect (`arXiv:1910.09966v1` §5.2 eq. (22),
§5.3): `h = 3 σ(M) - p₁(M, Σ)`, where `sig = σ(M)` is the 4-manifold / linking-matrix signature and
`p1 = ∑ᵢ tᵢ` is the sum of component framings. -/
def hirzebruchDefect (sig p1 : ℤ) : ℤ := 3 * sig - p1

/-- Modulo `3`, `hirzebruchDefect sig T ≡ -T [ZMOD 3]` for **every** integer signature `sig`:
the fractional `ℤ/3ℤ` charge residue comes exclusively from the framing sum `T`, while `sig`
contributes only an integer shift to `h / 3 = sig - T / 3`. -/
theorem hirzebruchDefect_mod_three (sig T : ℤ) :
    hirzebruchDefect sig T ≡ -T [ZMOD 3] := by
  rw [Int.modEq_iff_dvd]
  refine ⟨-sig, ?_⟩
  unfold hirzebruchDefect
  ring

/-- Shifting the 4-manifold signature `sig ↦ sig + dsig` (e.g. connected sum with `±ℂP²`) shifts
`hirzebruchDefect` by `3 * dsig` (`ΔQ = dsig` after dividing by `3`). -/
theorem hirzebruchDefect_sig_shift (sig dsig T : ℤ) :
    hirzebruchDefect (sig + dsig) T = hirzebruchDefect sig T + 3 * dsig := by
  unfold hirzebruchDefect
  ring

/-- Integer sign function `sgn : ℤ → ℤ` (`+1` for `x > 0`, `-1` for `x < 0`, `0` for `x = 0`),
giving the eigenvalue sign of a `1 × 1` diagonal linking-matrix block. -/
def intSign (x : ℤ) : ℤ :=
  if 0 < x then 1 else if x < 0 then -1 else 0

/-- On the single-twist range `{-1, 0, 1}`, `intSign x = x` identically. -/
theorem intSign_eq_self_of_unit_range {x : ℤ} (hx : -1 ≤ x ∧ x ≤ 1) :
    intSign x = x := by
  unfold intSign
  split_ifs <;> omega

/-- Signature `σ(diag(t₁, …, tₙ)) = n₊(t) - n₋(t) = ∑ᵢ sgn(tᵢ)` of the diagonal surgery linking
matrix of a zero-linking `n`-component framed link (such as the QOU Borromean link `V³` where all
pairwise linking numbers `lk(Lᵢ, Lⱼ) = 0`). -/
def diagLinkingSignature {n : ℕ} (t : Fin n → ℤ) : ℤ :=
  ∑ i : Fin n, intSign (t i)

/-- **Zero-Linking Single-Twist Evenness Obstruction (`qou-qvpl` Open Check B):**
On any zero-linking `n`-component link (`Λ = diag(t₁, …, tₙ)`), if every strand framing lies in
`{-1, 0, 1}`, then `σ(Λ) = ∑ᵢ tᵢ = T(t)` and `hirzebruchDefect (σ(Λ)) (T(t)) = 2 * T(t)` (always
even!). Consequently `(3σ(Λ) - T(t)) / 3 = (2 / 3) T(t)` cannot reach odd numerators `-1` (`d`)
or `-3` (`e⁻`, since `T = -3` gives `h = -6`, `h / 3 = -2 ≠ -1`) without multi-twist `|tᵢ| ≥ 2`,
non-zero pairwise linking `lk_{ij} ≠ 0`, or free `# ±ℂP²` signature summands. -/
theorem zeroLinking_unitFraming_hirzebruchDefect_eq_two_mul_sum {n : ℕ}
    (t : Fin n → ℤ) (hrange : ∀ i, -1 ≤ t i ∧ t i ≤ 1) :
    hirzebruchDefect (diagLinkingSignature t) (∑ i : Fin n, t i) =
      2 * (∑ i : Fin n, t i) := by
  have hsig : diagLinkingSignature t = ∑ i : Fin n, t i := by
    unfold diagLinkingSignature
    refine Finset.sum_congr rfl fun i _ => intSign_eq_self_of_unit_range (hrange i)
  unfold hirzebruchDefect
  rw [hsig]
  ring

/-- **Baez–Huerta `ℤ₆` Congruence Equivalence (`qou-qvpl` Open Check C):**
With integer cleared hypercharge `Y₃ = 2 * T - 3 * w'` (`3Y = 2T - 6I₃`, `w' = 2I₃`), whenever
weak-isospin parity `2 ∣ (w - w')` holds, the Baez–Huerta `ℤ₆` condition `6 ∣ (2τ + 3w + Y₃)` holds
**if and only if** colour triality satisfies `3 ∣ (τ + T)`. -/
theorem baez_huerta_z6_congruence_iff (tau w w' T : ℤ) (hw : (2 : ℤ) ∣ (w - w')) :
    (6 : ℤ) ∣ (2 * tau + 3 * w + (2 * T - 3 * w')) ↔ (3 : ℤ) ∣ (tau + T) := by
  obtain ⟨k, hk⟩ := hw
  have hid : 2 * tau + 3 * w + (2 * T - 3 * w') = 2 * (tau + T) + 6 * k := by
    have hw_eq : w - w' = 2 * k := hk
    linarith
  rw [hid]
  constructor
  · rintro ⟨m, hm⟩
    refine ⟨m - k, ?_⟩
    omega
  · rintro ⟨r, hr⟩
    refine ⟨r + k, ?_⟩
    omega

/-- **Rule-13a Open Conjecture Carrier (`qou-qvpl` Open Check A):**
Records that deriving `Y_t = 2 (T(t) / 3 - I₃)` from QOU categorical axioms (rather than selecting
it by Gell-Mann–Nishijima consistency `Q_twist = Q`) remains an open conjecture (`AGENTS.md`
Rule 13a; **zero instances**). -/
class CategoricalRibbonHyperchargeDerivationHypothesis : Prop where
  hypercharge_from_ribbon_axioms :
    ∀ (T twoI3 : ℤ), ∃ Y3 : ℤ, Y3 = 2 * T - 3 * twoI3

/-! ## Section 4: Charge-Value-Free U-Spin Coleman–Glashow Theorem (`qou-pwz4`, `qou-krgl`) -/

section ChargeFreeColemanGlashow

variable {K : Type*} [Field K]

/-- Adjacent pairwise charge sum `Q₁₂ + Q₂₃` on an `(a, a, b)` 3-strand weight space
(basis `|aab⟩, |aba⟩, |baa⟩`, covering `p = uud`, `Σ⁺ = uus`, `Σ⁻ = dds`), parameterized by
arbitrary strand charges `qa, qb : K`:
- on `|aab⟩`: `qa·qa + qa·qb`,
- on `|aba⟩`: `qa·qb + qb·qa = 2·qa·qb`,
- on `|baa⟩`: `qb·qa + qa·qa`. -/
def QAdjAAB (qa qb : K) : Matrix (Fin 3) (Fin 3) K :=
  !![qa * qa + qa * qb, 0, 0;
     0, 2 * qa * qb, 0;
     0, 0, qb * qa + qa * qa]

/-- Adjacent pairwise charge sum `Q₁₂ + Q₂₃` on an `(a, b, b)` 3-strand weight space
(basis `|abb⟩, |bab⟩, |bba⟩`, covering `n = udd`, `Ξ⁰ = uss`, `Ξ⁻ = dss`), parameterized by
arbitrary strand charges `qa, qb : K`:
- on `|abb⟩`: `qa·qb + qb·qb`,
- on `|bab⟩`: `qb·qa + qa·qb = 2·qa·qb`,
- on `|bba⟩`: `qb·qb + qb·qa`. -/
def QAdjABB (qa qb : K) : Matrix (Fin 3) (Fin 3) K :=
  !![qa * qb + qb * qb, 0, 0;
     0, 2 * qa * qb, 0;
     0, 0, qb * qb + qb * qa]

/-- At `(qa, qb) = (2/3, -1/3)`, `QAdjAAB` and `QAdjABB` reproduce `QAdjp` and `QAdjn` of
`USpinColemanGlashowLambdaSigma`. -/
theorem QAdjAAB_at_ud_eq_QAdjp :
    QAdjAAB ((2 : K) / 3) (-(1 : K) / 3) = QOU.Eightfold.USpinColemanGlashowLambdaSigma.QAdjp := by
  have h9 : (9 : K)⁻¹ = (3 : K)⁻¹ * (3 : K)⁻¹ := by
    rw [show (9 : K) = 3 * 3 by ring, _root_.mul_inv_rev]
  ext i j
  fin_cases i <;> fin_cases j <;>
    (simp [QAdjAAB, QOU.Eightfold.USpinColemanGlashowLambdaSigma.QAdjp, Q12p, Q23p,
      div_eq_mul_inv, h9]; try ring)

theorem QAdjABB_at_ud_eq_QAdjn :
    QAdjABB ((2 : K) / 3) (-(1 : K) / 3) = QOU.Eightfold.USpinColemanGlashowLambdaSigma.QAdjn := by
  have h9 : (9 : K)⁻¹ = (3 : K)⁻¹ * (3 : K)⁻¹ := by
    rw [show (9 : K) = 3 * 3 by ring, _root_.mul_inv_rev]
  ext i j
  fin_cases i <;> fin_cases j <;>
    (simp [QAdjABB, QOU.Eightfold.USpinColemanGlashowLambdaSigma.QAdjn, Q12n, Q23n,
      div_eq_mul_inv, h9]; try ring)

/-- When `qa = qb` (as on `Σ⁻ = dds` and `Ξ⁻ = dss` whenever `qd = qs`), both `QAdjAAB` and
`QAdjABB` collapse to the scalar matrix `(2 * qd²) • I₃`. -/
theorem QAdjAAB_same_eq_scalar (qd : K) :
    QAdjAAB qd qd = (2 * qd ^ 2) • (1 : Matrix (Fin 3) (Fin 3) K) := by
  ext i j; fin_cases i <;> fin_cases j <;> (simp [QAdjAAB]; try ring)

theorem QAdjABB_same_eq_scalar (qd : K) :
    QAdjABB qd qd = (2 * qd ^ 2) • (1 : Matrix (Fin 3) (Fin 3) K) := by
  ext i j; fin_cases i <;> fin_cases j <;> (simp [QAdjABB]; try ring)

/-- Connected Borromean `V³` trace functional on an `(a, a, b)` baryon with arbitrary quark charges
`(qa, qb)` (subtracting the static average `(1/3) tr(QAdjAAB qa qb) = (1/3)(2 qa² + 4 qa qb)`). -/
def trConnBorAAB (qa qb q : K) : K :=
  (1 / 3 : K) * (trace (QAdjAAB qa qb * borromeanV3A q) -
    ((2 * qa * qa + 4 * qa * qb) / 3) * trace (borromeanV3A q))

/-- Connected Borromean `V³` trace functional on an `(a, b, b)` baryon with arbitrary quark charges
`(qa, qb)` (subtracting the static average `(1/3) tr(QAdjABB qa qb) = (1/3)(4 qa qb + 2 qb²)`). -/
def trConnBorABB (qa qb q : K) : K :=
  (1 / 3 : K) * (trace (QAdjABB qa qb * borromeanV3B q) -
    ((4 * qa * qb + 2 * qb * qb) / 3) * trace (borromeanV3B q))

/-- On `Σ⁻ = (d, d, s)` (`AAB`) and `Ξ⁻ = (d, s, s)` (`ABB`), when `qd = qs`, both connected
traces vanish identically for **any** `qd, q : K`. -/
theorem trConnBor_equal_charge_eq_zero (qd q : K) (h3 : (3 : K) ≠ 0) :
    trConnBorAAB qd qd q = 0 ∧ trConnBorABB qd qd q = 0 := by
  have hscalar : (2 * qd * qd + 4 * qd * qd) / 3 = 2 * qd ^ 2 := by
    field_simp [h3]; ring
  have hscalarB : (4 * qd * qd + 2 * qd * qd) / 3 = 2 * qd ^ 2 := by
    field_simp [h3]; ring
  refine ⟨?_, ?_⟩
  · unfold trConnBorAAB
    rw [QAdjAAB_same_eq_scalar, hscalar, Matrix.smul_mul, Matrix.one_mul,
      Matrix.trace_smul, smul_eq_mul, sub_self, mul_zero]
  · unfold trConnBorABB
    rw [QAdjABB_same_eq_scalar, hscalarB, Matrix.smul_mul, Matrix.one_mul,
      Matrix.trace_smul, smul_eq_mul, sub_self, mul_zero]

/-- **Charge-Value-Free U-Spin Coleman–Glashow Theorem (`owner-rulings.md` row 59 Compliant):**
For **any** `[Field K]` (`3 ≠ 0`), **any** substrate parameter `q : K`, and **any** quark charges
`qu, qd, qs : K` satisfying U-spin charge equality `qd = qs` (without adopting `qu = +2/3` or
`qd = -1/3`), the alternating connected Borromean `V³` Coleman–Glashow combination
`(Δ_EM(p) - Δ_EM(n)) - (Δ_EM(Σ⁺) - Δ_EM(Σ⁻)) + (Δ_EM(Ξ⁰) - Δ_EM(Ξ⁻))` vanishes identically. -/
theorem coleman_glashow_borromeanV3_any_charges (qu qd qs q : K) (h3 : (3 : K) ≠ 0)
    (huSpin : qd = qs) :
    (trConnBorAAB qu qd q - trConnBorABB qu qd q) -
      (trConnBorAAB qu qs q - trConnBorAAB qd qs q) +
      (trConnBorABB qu qs q - trConnBorABB qd qs q) = 0 := by
  subst huSpin
  obtain ⟨hSM, hXM⟩ := trConnBor_equal_charge_eq_zero qd q h3
  rw [hSM, hXM]
  ring

end ChargeFreeColemanGlashow

end QOU.StandardModel.HopfFramingAndHirzebruchDefect
