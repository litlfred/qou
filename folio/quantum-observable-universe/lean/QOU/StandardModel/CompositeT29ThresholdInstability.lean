/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.RingTheory.Coprime.Basic
import Mathlib.Tactic
import QOU.Observations.InhomogeneousLeptonLoopResolvent

set_option autoImplicit false

/-!
# Dynamical 3-Body Threshold & Resolvent-Cut Audit of Composite `T(2,9) → 3 × T(2,3)` in `H₂(q)` / `H₃(q)`

Option 3B backup formalization for Open Gap 3 (bean `qou-618l`, companion to `qou-x4qm` / `qou-xtcl`
and `QOU.Observations.InhomogeneousLeptonLoopResolvent`).

Every declaration in this module is stated over generic commutative rings (`[CommRing R]`),
arbitrary associative `R`-algebras (`[Ring A] [Algebra R A]`), generic fields (`[Field K]`), or
generic ordered fields (`[Field K] [LinearOrder K] [IsStrictOrderedRing K]`) per `AGENTS.md §7c`
(zero `ℝ`, zero empirical literals, zero `sorry`, zero custom axioms).

## Main Results

1. **Arithmetic & Topological 3-Body Selection Rules on Bring's Genus-`≤ 4` Window (`{3, 5, 7, 9}`):**
   - `admissibleOddTorusSet_eq`: Seifert's genus bound `g(T_{2,n}) = (n - 1)/2 ≤ 4` on non-trivial
     odd windings `n ≥ 3` selects `{3, 5, 7, 9}`.
   - `torusLink_component_dichotomy` & `no_two_odd_winding_split`: even `n` gives 2-component torus
     links (`gcd(2, n) = 2`, e.g. the Hopf link `T(2,2)`), odd `n` gives single-component torus
     knots (`gcd(2, n) = 1`), and **no** odd `n` splits as `n = n₁ + n₂` into two odd windings.
   - `three_odd_knot_threshold_nine` & `threeOddKnotChannels_bring_window`: any 3-body split
     `n = n₁ + n₂ + n₃` into non-trivial odd torus knots (`nᵢ ≥ 3` odd) satisfies `9 ≤ n`; hence
     `n ∈ {3, 5, 7}` have **empty** 3-knot decay channels, while `n = 9` uniquely reaches the
     threshold via the **unique** channel `(3, 3, 3)` (`seifertGenus_t29_exceeds_three_t23` shows
     Seifert genus is strictly super-additive: `g(T_{2,9}) = 4 > 3 = 3 g(T_{2,3})`).

2. **Universal Hecke Power Reduction, Renormalized Cubic Generator, & Pairwise Bézout Coprimality:**
   - `hecke_pow_succ_eq_continuant`: in *any* associative `R`-algebra (`[CommRing R] [Ring A]
     [Algebra R A]`), any `s ∈ A` obeying `s² = h s + 1` satisfies `s^{n+1} = f_{n+1}(h) s + f_n(h)`
     for all `n : ℕ`.
   - `hecke_pow3_quadratic_and_pow9_fission`: the trefoil generator `Σ := s³` itself obeys the
     renormalized quadratic Hecke law `Σ² = h₃ Σ + 1` with `h₃ = h(h² + 3)`, yielding the **exact
     operator fission split**
     `s⁹ = P₆(h) s³ + h(h² + 3) · 1`, where `P₆(h) = h⁶ + 6h⁴ + 9h² + 1 = h₃² + 1`.
   - `heckeCont_harmonic_and_pairwise_bezout` & `heckeCont_generation_coprime_and_t29_dvd`: over
     every `[CommRing R]`, `{f₃(h), f₅(h), f₇(h)}` are **pairwise Bézout coprime**, while
     `f₃(h) ∣ f₉(h)` and `f₂(h) ∣ f₈(h)`.
   - `r21b_odd_trace_eq_diff` & `tauD3_sigma1_odd_eq_tauTorusOdd`: instantiates the universal
     reduction on `H₃(q)`'s `2 × 2` `(2,1)` hook representation (`χ_{(2,1)}(σ₁^{2m+1}) = q^{2m+1} - q^{-(2m+1)}`)
     and proves exact agreement between `H₃(q)` and `H₂(q)` Convention-D Markov traces, connecting
     directly to `InhomogeneousLoopResolvent.eval_eq_wAlg_of_vol_zero` on zero-volume torus knots.

3. **Exact Two-Arm Sign Dichotomy for `Q₃(q) = E(T_{2,9}; q) - 3 E(T_{2,3}; q)` (`q > 1`):**
   - **Arm A — Unsubtracted Total Trace / Continuant / Toroidal Resolvent Crossover:**
     * `continuant_and_chebyshev_threshold_iff`: `3 f₃(h) < f₉(h) ↔ 2 < h⁶ + 6h⁴ + 9h²` and
       `3(q³ + q⁻³) < q⁹ + q⁻⁹ ↔ 6 < (q³ + q⁻³)²`.
     * `continuant_subadditive_on_low_q` & `tauTorusOdd_subadditive_on_low_q`: for `1 < q ≤ 6/5`
       (continuant/Chebyshev) and `1 < q ≤ 8/7` (Convention-D Markov trace and toroidal
       `InhomogeneousLoopResolvent`, both strictly containing the `q ≈ 1.11` substrate regime),
       unsubtracted traces satisfy `E(T_{2,9}; q) < 3 E(T_{2,3}; q)` (**kinematically closed**),
       crossing into `E(T_{2,9}; q) > 3 E(T_{2,3}; q)` for `4/3 ≤ q`.
   - **Arm B — Universal Super-Additivity of Subtracted / Hook / Quantum-Integer Functionals:**
     For **every** `q > 1` in any ordered field:
     * `hook21_t29_strict_superadditive`: `χ_{(2,1)}(σ₁⁹) - 3 χ_{(2,1)}(σ₁³) = (q³ - q⁻³)³ > 0`.
     * `qIntBal_t29_strict_superadditive`: `[9]_q - 3 [3]_q = (q - q⁻¹)² [3]_q³ > 0`.
     * `deltaContinuant_t29_strict_superadditive`: `(f₉(h) - 1) - 3(f₃(h) - 1) = h²(h⁶ + 7h⁴ + 15h² + 7) > 0`.
     * `deltaTauTorus_t29_strict_superadditive`: `(τ_D(σ₁⁹) - 1/2) - 3(τ_D(σ₁³) - 1/2) > 0` via an
       exact `(q - 1)²` Taylor-positivity factorization over `q⁷(q² + 1)²`.

4. **Self-Energy Resolvent Second-Sheet Pole Shift & Rule-13a Conditional Exclusion Carrier:**
   - `resolvent_stable_below_three_knot_threshold` vs `resolvent_second_sheet_above_threshold`:
     vanishing 3-knot absorptive width keeps `n ∈ {3, 5, 7}` on the real energy axis, whereas any
     open channel `Q₃ > 0` with nonzero coupling `g₃ ≠ 0` eliminates all real-axis poles and shifts
     the `n = 9` pole strictly into the lower half-plane (`z_im = -Γ₉ / 2 < 0`).
   - `CompositeT29DecayExclusionHypothesis` (Rule 13a, **zero instances**): isolates the open
     physical mass-map / Fock-space compositeness bridge required to upgrade 3-body instability into
     exclusion of a 4th fundamental chiral generation.

-- Ref: [leitner2026] beans qou-618l, qou-x4qm, qou-xtcl, qou-91w7
-- Ref: [murasugi1958] K. Murasugi, Osaka Math. J. 10 (1958) 181–189 (alternating crossing number)
-- Ref: [geckpfeiffer2000] M. Geck, G. Pfeiffer, Characters of Finite Coxeter Groups and Iwahori–Hecke Algebras
-/

namespace QOU.StandardModel.CompositeT29ThresholdInstability

open Matrix
open QOU.QBeta.WeightSpaceMarkov
open QOU.QBeta.E0WeightCandidates
open QOU.Observations.ElectronUnitSplit
open QOU.Observations.InhomogeneousLeptonLoopResolvent

/-! ## Section 1: Arithmetic & Topological Selection Rules on Bring's Genus-`≤ 4` Window -/

section ArithmeticSelectionRules

/-- Seifert genus `g(T_{2,n}) = (n - 1) / 2` of an odd two-strand torus knot `T(2,n)`. -/
def seifertGenusT2 (n : ℕ) : ℕ := (n - 1) / 2

/-- Link component count `gcd(2, n)` of the two-strand torus closure `T(2, n) = σ₀ⁿ̂`. -/
def torusLinkComponentsT2 (n : ℕ) : ℕ := Nat.gcd 2 n

/-- Non-trivial odd torus-knot windings `n ≥ 3` embedding in Bring's genus-`4` curve `Σ₄`. -/
def admissibleOddTorusSet : Finset ℕ :=
  (Finset.Icc 3 11).filter (fun n => n % 2 = 1 ∧ seifertGenusT2 n ≤ 4)

/-- Finite 3-body odd-knot decay channel set `{(n₁, n₂, n₃) | nᵢ ≥ 3 odd, n₁ + n₂ + n₃ = n}`. -/
def threeOddKnotChannels (n : ℕ) : Finset ((ℕ × ℕ) × ℕ) :=
  ((Finset.Icc 3 9 ×ˢ Finset.Icc 3 9) ×ˢ Finset.Icc 3 9).filter
    (fun t => t.1.1 % 2 = 1 ∧ t.1.2 % 2 = 1 ∧ t.2 % 2 = 1 ∧ t.1.1 + t.1.2 + t.2 = n)

/-- Bring's genus-`≤ 4` bound admits exactly the four non-trivial odd windings `{3, 5, 7, 9}`. -/
theorem admissibleOddTorusSet_eq :
    admissibleOddTorusSet = {3, 5, 7, 9} ∧ admissibleOddTorusSet.card = 4 := by
  decide

/-- **Link-component parity dichotomy:** odd `n` closes to a 1-component knot (`gcd(2, n) = 1`),
whereas even `n` closes to a 2-component link (`gcd(2, n) = 2`, e.g. Hopf link `T(2,2)`). -/
theorem torusLink_component_dichotomy (n : ℕ) :
    (n % 2 = 1 → torusLinkComponentsT2 n = 1) ∧
    (n % 2 = 0 → torusLinkComponentsT2 n = 2) := by
  refine ⟨?_, ?_⟩ <;> intro h <;> rw [torusLinkComponentsT2, Nat.gcd_rec 2 n, h] <;> decide

/-- **Parity exclusion of 2-body odd-knot splits:** no odd winding `n` can split additively into
two odd windings `n₁ + n₂ = n`. -/
theorem no_two_odd_winding_split {n n₁ n₂ : ℕ}
    (hn : n % 2 = 1) (h1 : n₁ % 2 = 1) (h2 : n₂ % 2 = 1) :
    n₁ + n₂ ≠ n := by
  omega

/-- **Universal 3-odd-knot threshold (`3 + 3 + 3 = 9`):** for *any* non-trivial constituents
`n₁, n₂, n₃ ≥ 3` with `n₁ + n₂ + n₃ = n`, we have `9 ≤ n` (forbidding `n ∈ {3, 5, 7}`), and
equality `n = 9` holds if and only if `(n₁, n₂, n₃) = (3, 3, 3)`. -/
theorem three_odd_knot_threshold_nine {n n₁ n₂ n₃ : ℕ}
    (h1 : 3 ≤ n₁) (h2 : 3 ≤ n₂) (h3 : 3 ≤ n₃) (hsum : n₁ + n₂ + n₃ = n) :
    9 ≤ n ∧ n ≠ 3 ∧ n ≠ 5 ∧ n ≠ 7 ∧ (n = 9 ↔ (n₁ = 3 ∧ n₂ = 3 ∧ n₃ = 3)) := by
  omega

/-- **Signed fermion–antifermion crossing-budget barrier:** even under signed writhe conservation
`n₁ - n₂ + n₃ = n` (with an antifermion carrying negative writhe `-n₂`, `nᵢ ≥ 3`), total minimal
crossing number satisfies both `9 ≤ n₁ + n₂ + n₃` (exceeding `n` for `n < 9`) and `n + 6 ≤ n₁ + n₂ + n₃`. -/
theorem signed_three_knot_crossing_budget {n n₁ n₂ n₃ : ℕ}
    (h1 : 3 ≤ n₁) (h2 : 3 ≤ n₂) (h3 : 3 ≤ n₃)
    (hsigned : (n₁ : ℤ) - (n₂ : ℤ) + (n₃ : ℤ) = (n : ℤ)) (hn : n < 9) :
    9 ≤ n₁ + n₂ + n₃ ∧ n < n₁ + n₂ + n₃ ∧ n + 6 ≤ n₁ + n₂ + n₃ := by
  refine ⟨by omega, by omega, by omega⟩

/-- **Exact 3-knot channel census across `{3, 5, 7, 9}`:** `n = 3, 5, 7` have zero channels,
while `n = 9` has the unique channel `((3, 3), 3)`. -/
theorem threeOddKnotChannels_bring_window :
    threeOddKnotChannels 3 = ∅ ∧
    threeOddKnotChannels 5 = ∅ ∧
    threeOddKnotChannels 7 = ∅ ∧
    threeOddKnotChannels 9 = {((3, 3), 3)} ∧
    (threeOddKnotChannels 9).card = 1 := by
  decide

/-- **Topological Seifert-genus super-additivity:** `g(T_{2,9}) = 4 > 3 = 3 g(T_{2,3})`. -/
theorem seifertGenus_t29_exceeds_three_t23 :
    seifertGenusT2 3 = 1 ∧
    seifertGenusT2 9 = 4 ∧
    3 * seifertGenusT2 3 < seifertGenusT2 9 := by
  decide

end ArithmeticSelectionRules

/-! ## Section 2: Universal Hecke Power Reduction, Cubic Fission Split, & `H₃(q)` Bridge -/

section GenericHeckeReduction

/-- Morgan–Voyce / Fibonacci-polynomial continuant `f_n(h)` governing `s^{n+1} = f_{n+1}(h) s + f_n(h)`
for any quadratic Hecke generator `s² = h s + 1`. -/
def heckeCont {R : Type*} [CommRing R] (h : R) : ℕ → R
  | 0 => 0
  | 1 => 1
  | n + 2 => h * heckeCont h (n + 1) + heckeCont h n

/-- Degree-6 harmonic cofactor `P₆(h) = h⁶ + 6h⁴ + 9h² + 1` in `f₉(h) = f₃(h) P₆(h)`. -/
def harmonicCofactorP6 {R : Type*} [CommRing R] (h : R) : R :=
  h ^ 6 + 6 * h ^ 4 + 9 * h ^ 2 + 1

/-- Renormalized cubic Hecke parameter `h₃(h) = h(h² + 3)` governing `(s³)² = h₃(h) s³ + 1`. -/
def cubicHeckeParam {R : Type*} [CommRing R] (h : R) : R :=
  h * (h ^ 2 + 3)

/-- **Exact harmonic factorization `f₉ = f₃ P₆` and pairwise Bézout identities on `{f₃, f₅, f₇}`**
over any `[CommRing R]`. -/
theorem heckeCont_harmonic_and_pairwise_bezout {R : Type*} [CommRing R] (h : R) :
    heckeCont h 2 = h ∧
    heckeCont h 3 = h ^ 2 + 1 ∧
    heckeCont h 5 = h ^ 4 + 3 * h ^ 2 + 1 ∧
    heckeCont h 7 = h ^ 6 + 5 * h ^ 4 + 6 * h ^ 2 + 1 ∧
    heckeCont h 9 = heckeCont h 3 * harmonicCofactorP6 h ∧
    heckeCont h 8 = heckeCont h 2 * (h ^ 6 + 6 * h ^ 4 + 10 * h ^ 2 + 4) ∧
    harmonicCofactorP6 h = cubicHeckeParam h ^ 2 + 1 ∧
    heckeCont h 3 * (h ^ 2 + 2) - heckeCont h 5 = 1 ∧
    heckeCont h 3 * (h ^ 4 + 4 * h ^ 2 + 2) - heckeCont h 7 = 1 ∧
    heckeCont h 5 * (h ^ 4 + 4 * h ^ 2 + 3) - heckeCont h 7 * (h ^ 2 + 2) = 1 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    simp only [heckeCont, harmonicCofactorP6, cubicHeckeParam] <;> ring

/-- **Pairwise `IsCoprime` for `{f₃, f₅, f₇}` vs divisibility `f₃ ∣ f₉` over any `[CommRing R]`.** -/
theorem heckeCont_generation_coprime_and_t29_dvd {R : Type*} [CommRing R] (h : R) :
    IsCoprime (heckeCont h 3) (heckeCont h 5) ∧
    IsCoprime (heckeCont h 3) (heckeCont h 7) ∧
    IsCoprime (heckeCont h 5) (heckeCont h 7) ∧
    heckeCont h 3 ∣ heckeCont h 9 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · exact ⟨h ^ 2 + 2, -1, by simp only [heckeCont]; ring⟩
  · exact ⟨h ^ 4 + 4 * h ^ 2 + 2, -1, by simp only [heckeCont]; ring⟩
  · exact ⟨h ^ 4 + 4 * h ^ 2 + 3, -(h ^ 2 + 2), by simp only [heckeCont]; ring⟩
  · exact ⟨harmonicCofactorP6 h, (heckeCont_harmonic_and_pairwise_bezout h).2.2.2.2.1⟩

/-- **Universal Hecke power reduction** in any associative `R`-algebra (`A` not assumed commutative):
if `s² = h · s + 1`, then `s^{n+1} = f_{n+1}(h) · s + f_n(h) · 1` for every `n : ℕ`. -/
theorem hecke_pow_succ_eq_continuant {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
    (h : R) (s : A) (hs : s ^ 2 = algebraMap R A h * s + 1) (n : ℕ) :
    s ^ (n + 1) =
      algebraMap R A (heckeCont h (n + 1)) * s + algebraMap R A (heckeCont h n) := by
  induction n with
  | zero =>
      simp [heckeCont]
  | succ k ih =>
      have hrec : algebraMap R A (heckeCont h (k + 2)) =
          algebraMap R A (heckeCont h (k + 1)) * algebraMap R A h +
            algebraMap R A (heckeCont h k) := by
        simp only [heckeCont]
        rw [mul_comm h (heckeCont h (k + 1))]
        simp only [map_add, map_mul]
      calc
        s ^ (k + 2) = s ^ (k + 1) * s := pow_succ s (k + 1)
        _ = (algebraMap R A (heckeCont h (k + 1)) * s + algebraMap R A (heckeCont h k)) * s := by
            rw [ih]
        _ = algebraMap R A (heckeCont h (k + 1)) * s ^ 2 +
              algebraMap R A (heckeCont h k) * s := by
            rw [add_mul, mul_assoc, ← sq]
        _ = algebraMap R A (heckeCont h (k + 1)) * (algebraMap R A h * s + 1) +
              algebraMap R A (heckeCont h k) * s := by
            rw [hs]
        _ = (algebraMap R A (heckeCont h (k + 1)) * algebraMap R A h +
              algebraMap R A (heckeCont h k)) * s +
              algebraMap R A (heckeCont h (k + 1)) := by
            rw [mul_add, mul_one, ← mul_assoc, add_right_comm, ← add_mul]
        _ = algebraMap R A (heckeCont h (k + 2)) * s + algebraMap R A (heckeCont h (k + 1)) := by
            rw [hrec]

/-- **Renormalized cubic Hecke law & exact `T(2,9)` operator fission split:** in any associative
`R`-algebra where `s² = h s + 1`:
1. `(s³)² = h₃(h) s³ + 1` (`s³` obeys its own quadratic Hecke relation with `h₃ = h(h² + 3)`), and
2. `s⁹ = P₆(h) s³ + h₃(h) · 1` (exact decomposition into descended `s³` harmonic + scalar transient). -/
theorem hecke_pow3_quadratic_and_pow9_fission {R : Type*} [CommRing R] {A : Type*} [Ring A]
    [Algebra R A] (h : R) (s : A) (hs : s ^ 2 = algebraMap R A h * s + 1) :
    (s ^ 3) ^ 2 = algebraMap R A (cubicHeckeParam h) * (s ^ 3) + 1 ∧
    s ^ 9 = algebraMap R A (harmonicCofactorP6 h) * (s ^ 3) + algebraMap R A (cubicHeckeParam h) := by
  have hp3 := hecke_pow_succ_eq_continuant h s hs 2
  have hp6 := hecke_pow_succ_eq_continuant h s hs 5
  have hp9 := hecke_pow_succ_eq_continuant h s hs 8
  have hc61 : heckeCont h 6 = cubicHeckeParam h * heckeCont h 3 := by
    simp only [heckeCont, cubicHeckeParam]; ring
  have hc60 : heckeCont h 5 = cubicHeckeParam h * heckeCont h 2 + 1 := by
    simp only [heckeCont, cubicHeckeParam]; ring
  have hc91 : heckeCont h 9 = harmonicCofactorP6 h * heckeCont h 3 := by
    simp only [heckeCont, harmonicCofactorP6]; ring
  have hc90 : heckeCont h 8 = harmonicCofactorP6 h * heckeCont h 2 + cubicHeckeParam h := by
    simp only [heckeCont, harmonicCofactorP6, cubicHeckeParam]; ring
  refine ⟨?_, ?_⟩
  · calc
      (s ^ 3) ^ 2 = s ^ 6 := by rw [← pow_mul]
      _ = algebraMap R A (heckeCont h 6) * s + algebraMap R A (heckeCont h 5) := hp6
      _ = algebraMap R A (cubicHeckeParam h * heckeCont h 3) * s +
            algebraMap R A (cubicHeckeParam h * heckeCont h 2 + 1) := by rw [hc61, hc60]
      _ = algebraMap R A (cubicHeckeParam h) *
            (algebraMap R A (heckeCont h 3) * s + algebraMap R A (heckeCont h 2)) + 1 := by
          simp only [map_add, map_mul, map_one]
          rw [mul_add, mul_assoc, add_assoc]
      _ = algebraMap R A (cubicHeckeParam h) * (s ^ 3) + 1 := by rw [← hp3]
  · calc
      s ^ 9 = algebraMap R A (heckeCont h 9) * s + algebraMap R A (heckeCont h 8) := hp9
      _ = algebraMap R A (harmonicCofactorP6 h * heckeCont h 3) * s +
            algebraMap R A (harmonicCofactorP6 h * heckeCont h 2 + cubicHeckeParam h) := by
          rw [hc91, hc90]
      _ = algebraMap R A (harmonicCofactorP6 h) *
            (algebraMap R A (heckeCont h 3) * s + algebraMap R A (heckeCont h 2)) +
            algebraMap R A (cubicHeckeParam h) := by
          simp only [map_add, map_mul]
          rw [mul_add, mul_assoc, add_assoc]
      _ = algebraMap R A (harmonicCofactorP6 h) * (s ^ 3) + algebraMap R A (cubicHeckeParam h) := by
          rw [← hp3]

end GenericHeckeReduction

/-! ## Section 3: Exact `H₃(q)` / `H₂(q)` Trace Identities & Binet Formulas Over `[Field K]` -/

section FieldTraceIdentities

variable {K : Type*} [Field K]

/-- Closed-form Convention-D Markov trace of odd torus powers `σ₁^{2m+1}` (shared by `H₂(q)` and `H₃(q)`). -/
def tauTorusOdd (q : K) (m : ℕ) : K :=
  q ^ (2 * m + 1) - (q ^ (2 * m + 1) + (q⁻¹) ^ (2 * m + 1)) / (q + q⁻¹) ^ 2

/-- Balanced quantum integer `[n]_q = (q^n - q^{-n}) / (q - q⁻¹)`. -/
def qIntBal (q : K) (n : ℕ) : K :=
  (q ^ n - (q⁻¹) ^ n) / (q - q⁻¹)

/-- **Exact Binet formula for all `n`:**
`f_{n+1}(q - q⁻¹) · (q + q⁻¹) = q^{n+1} - (-q⁻¹)^{n+1}` and
`f_{2m+1}(q - q⁻¹) · (q + q⁻¹) = q^{2m+1} + (q⁻¹)^{2m+1}`, `f_{2m}(q - q⁻¹) · (q + q⁻¹) = q^{2m} - (q⁻¹)^{2m}`. -/
theorem heckeCont_binet_odd_even (q : K) (hq : q ≠ 0) (m : ℕ) :
    heckeCont (q - q⁻¹) (2 * m + 1) * (q + q⁻¹) = q ^ (2 * m + 1) + (q⁻¹) ^ (2 * m + 1) ∧
    heckeCont (q - q⁻¹) (2 * m) * (q + q⁻¹) = q ^ (2 * m) - (q⁻¹) ^ (2 * m) := by
  induction m with
  | zero =>
      simp [heckeCont]
  | succ k ih =>
      have h2k2 : 2 * (k + 1) = 2 * k + 2 := by omega
      have h2k3 : 2 * (k + 1) + 1 = 2 * k + 3 := by omega
      have heven : heckeCont (q - q⁻¹) (2 * k + 2) * (q + q⁻¹) =
          q ^ (2 * k + 2) - (q⁻¹) ^ (2 * k + 2) := by
        calc
          heckeCont (q - q⁻¹) (2 * k + 2) * (q + q⁻¹)
              = (q - q⁻¹) * (heckeCont (q - q⁻¹) (2 * k + 1) * (q + q⁻¹)) +
                  heckeCont (q - q⁻¹) (2 * k) * (q + q⁻¹) := by
                simp only [heckeCont]; ring
          _ = (q - q⁻¹) * (q ^ (2 * k + 1) + (q⁻¹) ^ (2 * k + 1)) +
                (q ^ (2 * k) - (q⁻¹) ^ (2 * k)) := by
                rw [ih.1, ih.2]
          _ = q ^ (2 * k + 2) - (q⁻¹) ^ (2 * k + 2) := by
                have hqk : q ^ (2 * k) ≠ 0 := pow_ne_zero _ hq
                simp only [pow_add, pow_one, inv_pow]
                field_simp
                ring
      refine ⟨?_, ?_⟩
      · rw [h2k3]
        calc
          heckeCont (q - q⁻¹) (2 * k + 3) * (q + q⁻¹)
              = (q - q⁻¹) * (heckeCont (q - q⁻¹) (2 * k + 2) * (q + q⁻¹)) +
                  heckeCont (q - q⁻¹) (2 * k + 1) * (q + q⁻¹) := by
                simp only [heckeCont]; ring
          _ = (q - q⁻¹) * (q ^ (2 * k + 2) - (q⁻¹) ^ (2 * k + 2)) +
                (q ^ (2 * k + 1) + (q⁻¹) ^ (2 * k + 1)) := by
                rw [heven, ih.1]
          _ = q ^ (2 * k + 3) + (q⁻¹) ^ (2 * k + 3) := by
                have hqk : q ^ (2 * k) ≠ 0 := pow_ne_zero _ hq
                simp only [pow_add, pow_one, inv_pow]
                field_simp
                ring
      · rwa [h2k2]

/-- **Instantiation on `H₃(q)`'s `2 × 2` `(2,1)` hook matrix `r21b q`:**
`(r21b q)^{n+1} = f_{n+1}(q - q⁻¹) • r21b q + f_n(q - q⁻¹) • 1`. -/
theorem r21b_pow_succ_eq_continuant (q : K) (hq : q ≠ 0) (n : ℕ) :
    (r21b q) ^ (n + 1) =
      heckeCont (q - q⁻¹) (n + 1) • r21b q +
        heckeCont (q - q⁻¹) n • (1 : Matrix (Fin 2) (Fin 2) K) := by
  have hs : (r21b q) ^ 2 = algebraMap K (Matrix (Fin 2) (Fin 2) K) (q - q⁻¹) * r21b q + 1 := by
    rw [sq, Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]
    exact hecke_r21b q hq
  simpa [Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul] using
    hecke_pow_succ_eq_continuant (q - q⁻¹) (r21b q) hs n

/-- **Exact `(2,1)` hook trace of odd powers `σ₁^{2m+1}` in `H₃(q)`:**
`tr((r21b q)^{2m+1}) = q^{2m+1} - (q⁻¹)^{2m+1}`. -/
theorem r21b_odd_trace_eq_diff (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (m : ℕ) :
    ((r21b q) ^ (2 * m + 1)).trace = q ^ (2 * m + 1) - (q⁻¹) ^ (2 * m + 1) := by
  have hs : q + q⁻¹ ≠ 0 := by
    intro h; apply hq2; field_simp at h; linear_combination h
  rw [r21b_pow_succ_eq_continuant q hq (2 * m)]
  have htr : (heckeCont (q - q⁻¹) (2 * m + 1) • r21b q +
      heckeCont (q - q⁻¹) (2 * m) • (1 : Matrix (Fin 2) (Fin 2) K)).trace =
      heckeCont (q - q⁻¹) (2 * m + 1) * (q - q⁻¹) + 2 * heckeCont (q - q⁻¹) (2 * m) := by
    simp [r21b, Matrix.trace_fin_two]
    ring
  rw [htr]
  have hb := heckeCont_binet_odd_even q hq m
  apply mul_right_cancel₀ hs
  calc
    (heckeCont (q - q⁻¹) (2 * m + 1) * (q - q⁻¹) + 2 * heckeCont (q - q⁻¹) (2 * m)) * (q + q⁻¹)
        = (heckeCont (q - q⁻¹) (2 * m + 1) * (q + q⁻¹)) * (q - q⁻¹) +
            2 * (heckeCont (q - q⁻¹) (2 * m) * (q + q⁻¹)) := by ring
    _ = (q ^ (2 * m + 1) + (q⁻¹) ^ (2 * m + 1)) * (q - q⁻¹) +
          2 * (q ^ (2 * m) - (q⁻¹) ^ (2 * m)) := by rw [hb.1, hb.2]
    _ = (q ^ (2 * m + 1) - (q⁻¹) ^ (2 * m + 1)) * (q + q⁻¹) := by
          have hqm : q ^ (2 * m) ≠ 0 := pow_ne_zero _ hq
          simp only [pow_add, pow_one, inv_pow]
          field_simp
          ring

/-- **Exact `H₃(q) ↔ H₂(q)` Convention-D Markov trace agreement for all odd powers `2m + 1`:**
1. `τ_D^{(3)}(σ₁^{2m+1}) = tauTorusOdd q m`,
2. `y₂(q) q^{2m+1} + y₁₁(q) (-(q⁻¹)^{2m+1}) = tauTorusOdd q m`, and
3. `f_{2m+1}(q - q⁻¹) · (q³ / (q² + 1)) + f_{2m}(q - q⁻¹) = tauTorusOdd q m`. -/
theorem tauD3_sigma1_odd_eq_tauTorusOdd (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (m : ℕ) :
    tauD3 q (q ^ (2 * m + 1)) ((r21b q) ^ (2 * m + 1)) = tauTorusOdd q m ∧
    y2 q * q ^ (2 * m + 1) + y11 q * (-(q⁻¹) ^ (2 * m + 1)) = tauTorusOdd q m ∧
    heckeCont (q - q⁻¹) (2 * m + 1) * (q ^ 3 / (q ^ 2 + 1)) + heckeCont (q - q⁻¹) (2 * m) =
      tauTorusOdd q m := by
  have hs : q + q⁻¹ ≠ 0 := by
    intro h; apply hq2; field_simp at h; linear_combination h
  refine ⟨?_, ?_, ?_⟩
  · unfold tauD3 y3 y21 tauTorusOdd
    rw [r21b_odd_trace_eq_diff q hq hq2 m]
    field_simp
    ring
  · unfold y2 y11 tauTorusOdd
    have he : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
    rw [he]
    field_simp
    ring
  · have hb := heckeCont_binet_odd_even q hq m
    unfold tauTorusOdd
    apply mul_right_cancel₀ hs
    have hz : q ^ 3 / (q ^ 2 + 1) = q ^ 2 / (q + q⁻¹) := by
      have he : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
      rw [he]; field_simp
    rw [hz]
    calc
      (heckeCont (q - q⁻¹) (2 * m + 1) * (q ^ 2 / (q + q⁻¹)) +
          heckeCont (q - q⁻¹) (2 * m)) * (q + q⁻¹)
          = (heckeCont (q - q⁻¹) (2 * m + 1) * (q + q⁻¹)) * (q ^ 2 / (q + q⁻¹)) +
              heckeCont (q - q⁻¹) (2 * m) * (q + q⁻¹) := by ring
      _ = (q ^ (2 * m + 1) + (q⁻¹) ^ (2 * m + 1)) * (q ^ 2 / (q + q⁻¹)) +
            (q ^ (2 * m) - (q⁻¹) ^ (2 * m)) := by rw [hb.1, hb.2]
      _ = (q ^ (2 * m + 1) - (q ^ (2 * m + 1) + (q⁻¹) ^ (2 * m + 1)) / (q + q⁻¹) ^ 2) *
            (q + q⁻¹) := by
            have hqm : q ^ (2 * m) ≠ 0 := pow_ne_zero _ hq
            simp only [pow_add, pow_one, inv_pow]
            field_simp
            ring

/-- Classical `q = 1` value of `tauTorusOdd`: `tauTorusOdd 1 m = 1 / 2` for **every** `m : ℕ`. -/
theorem tauTorusOdd_at_one (h2 : (2 : K) ≠ 0) (m : ℕ) :
    tauTorusOdd (1 : K) m = 1 / 2 := by
  unfold tauTorusOdd
  simp only [one_pow, inv_one]
  rw [show (1 : K) + 1 = 2 by ring, show (2 : K) ^ 2 = 2 * 2 by ring]
  field_simp [h2]
  ring

/-- **Toroidal Inhomogeneous Resolvent Bridge (`#9213`):** because every torus knot `T(2, 2m+1)`
has `Vol = 0`, `InhomogeneousLoopResolvent.eval` reduces identically to `wAlg` (`τ_D / τ_e`), so
its 3-body excess equals `(tauTorusOdd q 4 - 3 * tauTorusOdd q 1) / tauElectron q`. -/
theorem toroidal_resolvent_t29_excess {ι : Type*} (R : InhomogeneousLoopResolvent ι K)
    {x3 x9 : ι} (hv3 : R.vol x3 = 0) (hv9 : R.vol x9 = 0) (q : K)
    (hw3 : R.wAlg x3 q = tauTorusOdd q 1 / tauElectron q)
    (hw9 : R.wAlg x9 q = tauTorusOdd q 4 / tauElectron q) :
    R.eval x9 q - 3 * R.eval x3 q =
      (tauTorusOdd q 4 - 3 * tauTorusOdd q 1) / tauElectron q := by
  rw [R.eval_eq_wAlg_of_vol_zero hv9 q, R.eval_eq_wAlg_of_vol_zero hv3 q, hw9, hw3]
  ring

end FieldTraceIdentities

/-! ## Section 4: Two-Arm Sign Audit of `E(T_{2,9}) - 3 E(T_{2,3})` Over Ordered Fields -/

section OrderedSignAudit

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-! ### Arm A: Unsubtracted Trace / Continuant / Toroidal Resolvent Crossover -/

/-- **Exact polynomial threshold equivalence for `f₉(h) - 3 f₃(h)` and `(q⁹ + q⁻⁹) - 3(q³ + q⁻³)`:**
both change sign at the *same* critical locus `(q³ + q⁻³)² = 6 ↔ h⁶ + 6h⁴ + 9h² = 2`. -/
theorem continuant_and_chebyshev_threshold_iff {q : K} (hq : 1 < q) :
    let h := q - q⁻¹
    heckeCont h 9 - 3 * heckeCont h 3 = (h ^ 2 + 1) * (h ^ 6 + 6 * h ^ 4 + 9 * h ^ 2 - 2) ∧
    (q ^ 9 + (q⁻¹) ^ 9) - 3 * (q ^ 3 + (q⁻¹) ^ 3) =
      (q ^ 3 + (q⁻¹) ^ 3) * ((q ^ 3 + (q⁻¹) ^ 3) ^ 2 - 6) ∧
    (q ^ 3 + (q⁻¹) ^ 3) ^ 2 - 6 = h ^ 6 + 6 * h ^ 4 + 9 * h ^ 2 - 2 ∧
    (3 * heckeCont h 3 < heckeCont h 9 ↔ 2 < h ^ 6 + 6 * h ^ 4 + 9 * h ^ 2) ∧
    (3 * (q ^ 3 + (q⁻¹) ^ 3) < q ^ 9 + (q⁻¹) ^ 9 ↔ 6 < (q ^ 3 + (q⁻¹) ^ 3) ^ 2) := by
  have hq0 : 0 < q := by linarith
  have hfac1 :
      heckeCont (q - q⁻¹) 9 - 3 * heckeCont (q - q⁻¹) 3 =
        ((q - q⁻¹) ^ 2 + 1) *
          ((q - q⁻¹) ^ 6 + 6 * (q - q⁻¹) ^ 4 + 9 * (q - q⁻¹) ^ 2 - 2) := by
    simp only [heckeCont]; ring
  have hfac2 :
      (q ^ 9 + (q⁻¹) ^ 9) - 3 * (q ^ 3 + (q⁻¹) ^ 3) =
        (q ^ 3 + (q⁻¹) ^ 3) * ((q ^ 3 + (q⁻¹) ^ 3) ^ 2 - 6) := by
    field_simp; ring
  have hfac3 :
      (q ^ 3 + (q⁻¹) ^ 3) ^ 2 - 6 =
        (q - q⁻¹) ^ 6 + 6 * (q - q⁻¹) ^ 4 + 9 * (q - q⁻¹) ^ 2 - 2 := by
    field_simp; ring
  have hb3_pos : 0 < (q - q⁻¹) ^ 2 + 1 := by positivity
  have hc3_pos : 0 < q ^ 3 + (q⁻¹) ^ 3 := by positivity
  refine ⟨hfac1, hfac2, hfac3, ?_, ?_⟩
  · constructor
    · intro hlt
      have hpos : 0 < heckeCont (q - q⁻¹) 9 - 3 * heckeCont (q - q⁻¹) 3 := sub_pos.mpr hlt
      rw [hfac1] at hpos
      have hmul := (mul_pos_iff_of_pos_left hb3_pos).mp hpos
      linarith
    · intro hgt
      have hpos : 0 < heckeCont (q - q⁻¹) 9 - 3 * heckeCont (q - q⁻¹) 3 := by
        rw [hfac1]
        exact mul_pos hb3_pos (by linarith)
      linarith
  · constructor
    · intro hlt
      have hpos : 0 < (q ^ 9 + (q⁻¹) ^ 9) - 3 * (q ^ 3 + (q⁻¹) ^ 3) := sub_pos.mpr hlt
      rw [hfac2] at hpos
      have hmul := (mul_pos_iff_of_pos_left hc3_pos).mp hpos
      linarith
    · intro hgt
      have hpos : 0 < (q ^ 9 + (q⁻¹) ^ 9) - 3 * (q ^ 3 + (q⁻¹) ^ 3) := by
        rw [hfac2]
        exact mul_pos hc3_pos (by linarith)
      linarith

/-- **Arm A Sub-Additivity (`1 < q ≤ 6/5`) vs Super-Additivity (`4/3 ≤ q`) for `f_n` and `q^n + q⁻ⁿ`:**
in the low-`q` window `1 < q ≤ 6/5` (which contains the `q ≈ 1.11` substrate regime), unsubtracted
continuants and Chebyshev sums are **strictly sub-additive** (`E(9) < 3 E(3)`), whereas for `q ≥ 4/3`
they are **strictly super-additive** (`3 E(3) < E(9)`). -/
theorem continuant_sub_vs_super_crossover :
    (∀ q : K, 1 < q → q ≤ 6 / 5 →
      heckeCont (q - q⁻¹) 9 < 3 * heckeCont (q - q⁻¹) 3 ∧
      q ^ 9 + (q⁻¹) ^ 9 < 3 * (q ^ 3 + (q⁻¹) ^ 3)) ∧
    (∀ q : K, 4 / 3 ≤ q →
      3 * heckeCont (q - q⁻¹) 3 < heckeCont (q - q⁻¹) 9 ∧
      3 * (q ^ 3 + (q⁻¹) ^ 3) < q ^ 9 + (q⁻¹) ^ 9) := by
  refine ⟨?_, ?_⟩
  · intro q hq1 hqle
    have hq0 : 0 < q := by linarith
    have hh_pos : 0 < q - q⁻¹ := by
      have : q - q⁻¹ = (q - 1) * (q + 1) / q := by field_simp; ring
      rw [this]
      have : 0 < q - 1 := sub_pos.mpr hq1
      positivity
    have hh_le : q - q⁻¹ ≤ 11 / 30 := by
      have hdiff : 11 / 30 - (q - q⁻¹) = (6 - 5 * q) * (6 * q + 5) / (30 * q) := by
        field_simp; ring
      have h65 : 0 ≤ 6 - 5 * q := by linarith
      have hnn : 0 ≤ 11 / 30 - (q - q⁻¹) := by rw [hdiff]; positivity
      linarith
    have hh2 : (q - q⁻¹) ^ 2 ≤ 1 / 6 := by nlinarith
    have hh4 : (q - q⁻¹) ^ 4 ≤ 1 / 36 := by nlinarith [sq_nonneg (q - q⁻¹)]
    have hh6 : (q - q⁻¹) ^ 6 ≤ 1 / 216 := by nlinarith [sq_nonneg (q - q⁻¹)]
    have hpoly_lt : (q - q⁻¹) ^ 6 + 6 * (q - q⁻¹) ^ 4 + 9 * (q - q⁻¹) ^ 2 < 2 := by linarith
    have hiff := continuant_and_chebyshev_threshold_iff hq1
    have hb3_pos : 0 < (q - q⁻¹) ^ 2 + 1 := by positivity
    have hc3_pos : 0 < q ^ 3 + (q⁻¹) ^ 3 := by positivity
    have hneg1 : heckeCont (q - q⁻¹) 9 - 3 * heckeCont (q - q⁻¹) 3 < 0 := by
      rw [hiff.1]
      exact mul_neg_of_pos_of_neg hb3_pos (by linarith)
    have hneg2 : (q ^ 9 + (q⁻¹) ^ 9) - 3 * (q ^ 3 + (q⁻¹) ^ 3) < 0 := by
      rw [hiff.2.1, hiff.2.2.1]
      exact mul_neg_of_pos_of_neg hc3_pos (by linarith)
    exact ⟨by linarith, by linarith⟩
  · intro q hqge
    have hq1 : 1 < q := by linarith
    have hq0 : 0 < q := by linarith
    have hh_ge : 7 / 12 ≤ q - q⁻¹ := by
      have hdiff : (q - q⁻¹) - 7 / 12 = (3 * q - 4) * (4 * q + 3) / (12 * q) := by
        field_simp; ring
      have h34 : 0 ≤ 3 * q - 4 := by linarith
      have hnn : 0 ≤ (q - q⁻¹) - 7 / 12 := by rw [hdiff]; positivity
      linarith
    have hh2_gt : 1 / 3 < (q - q⁻¹) ^ 2 := by nlinarith
    have hpoly_gt : 2 < (q - q⁻¹) ^ 6 + 6 * (q - q⁻¹) ^ 4 + 9 * (q - q⁻¹) ^ 2 := by
      have : 0 ≤ (q - q⁻¹) ^ 6 := by positivity
      have : 0 ≤ (q - q⁻¹) ^ 4 := by positivity
      linarith
    have hiff := continuant_and_chebyshev_threshold_iff hq1
    have h2 : 6 < (q ^ 3 + (q⁻¹) ^ 3) ^ 2 := by linarith [hiff.2.2.1]
    exact ⟨hiff.2.2.2.1.mpr hpoly_gt, hiff.2.2.2.2.mpr h2⟩

/-- **Arm A Sub-Additivity (`1 < q ≤ 8/7`) for Convention-D Markov Trace `tauTorusOdd`:**
in the low-`q` substrate window `1 < q ≤ 8/7` (`8/7 ≈ 1.1428 > q₀`), unsubtracted
`τ_D(σ₁⁹) < 3 τ_D(σ₁³)` (3-body channel kinematically closed). -/
theorem tauTorusOdd_subadditive_low_q (q : K) (hq1 : 1 < q) (hqle : q ≤ 8 / 7) :
    tauTorusOdd q 4 < 3 * tauTorusOdd q 1 := by
  have hq0 : 0 < q := by linarith
  have hs2_gt4 : 4 < (q + q⁻¹) ^ 2 := by
    have hid : (q + q⁻¹) ^ 2 - 4 = (q - 1) ^ 2 * (q + 1) ^ 2 / q ^ 2 := by field_simp; ring
    have hq1_pos : 0 < q - 1 := sub_pos.mpr hq1
    have hpos : 0 < (q + q⁻¹) ^ 2 - 4 := by rw [hid]; positivity
    linarith
  set S : K := q ^ 3 + (q⁻¹) ^ 3
  have hS_gt2 : 2 < S := by
    show 2 < q ^ 3 + (q⁻¹) ^ 3
    have hid : q ^ 3 + (q⁻¹) ^ 3 - 2 = (q - 1) ^ 2 * (q ^ 2 + q + 1) ^ 2 / q ^ 3 := by
      field_simp; ring
    have hq1_pos : 0 < q - 1 := sub_pos.mpr hq1
    have hpos : 0 < q ^ 3 + (q⁻¹) ^ 3 - 2 := by rw [hid]; positivity
    linarith
  have hnum_lt4 : 3 * (q ^ 3 + (q⁻¹) ^ 3) - (q ^ 9 + (q⁻¹) ^ 9) < 4 := by
    have hid : 4 - (3 * (q ^ 3 + (q⁻¹) ^ 3) - (q ^ 9 + (q⁻¹) ^ 9)) =
        (S - 2) * (S ^ 2 + 2 * S - 2) := by
      dsimp [S]; field_simp; ring
    have hS2 : 0 < S ^ 2 + 2 * S - 2 := by nlinarith
    have hpos : 0 < 4 - (3 * (q ^ 3 + (q⁻¹) ^ 3) - (q ^ 9 + (q⁻¹) ^ 9)) := by
      rw [hid]; exact mul_pos (by linarith) hS2
    linarith
  have hfrac_lt1 :
      (3 * (q ^ 3 + (q⁻¹) ^ 3) - (q ^ 9 + (q⁻¹) ^ 9)) / (q + q⁻¹) ^ 2 < 1 := by
    rw [div_lt_one (by linarith)]
    linarith
  have hx_gt1 : 1 < q ^ 3 := by
    have hid : q ^ 3 - 1 = (q - 1) * (q ^ 2 + q + 1) := by ring
    have hq1_pos : 0 < q - 1 := sub_pos.mpr hq1
    have hpos : 0 < q ^ 3 - 1 := by rw [hid]; positivity
    linarith
  have hx_lt : q ^ 3 < 3 / 2 := by
    have hq3_le : q ^ 3 ≤ (8 / 7 : K) ^ 3 := by
      have hid : (8 / 7 : K) ^ 3 - q ^ 3 =
          (8 / 7 - q) * ((8 / 7) ^ 2 + (8 / 7) * q + q ^ 2) := by ring
      have hnn : 0 ≤ (8 / 7 : K) ^ 3 - q ^ 3 := by
        rw [hid]; exact mul_nonneg (by linarith) (by positivity)
      linarith
    linarith [show ((8 / 7 : K) ^ 3) < 3 / 2 by norm_num]
  have hpoly_neg : q ^ 9 - 3 * q ^ 3 + 1 < 0 := by
    have hid : q ^ 9 - 3 * q ^ 3 + 1 =
        (q ^ 3 - 3 / 2) * ((q ^ 3) ^ 2 + (3 / 2) * q ^ 3 - 3 / 4) - 1 / 8 := by ring
    have hquad : 0 < (q ^ 3) ^ 2 + (3 / 2) * q ^ 3 - 3 / 4 := by nlinarith
    have hmul : (q ^ 3 - 3 / 2) * ((q ^ 3) ^ 2 + (3 / 2) * q ^ 3 - 3 / 4) < 0 :=
      mul_neg_of_neg_of_pos (by linarith) hquad
    linarith
  have hdecomp :
      tauTorusOdd q 4 - 3 * tauTorusOdd q 1 =
        (q ^ 9 - 3 * q ^ 3) +
          (3 * (q ^ 3 + (q⁻¹) ^ 3) - (q ^ 9 + (q⁻¹) ^ 9)) / (q + q⁻¹) ^ 2 := by
    unfold tauTorusOdd
    rw [show 2 * 4 + 1 = 9 by omega, show 2 * 1 + 1 = 3 by omega]
    ring
  linarith

/-- **Arm A Super-Additivity (`4/3 ≤ q`) for Convention-D Markov Trace `tauTorusOdd`:**
above the critical window (`q ≥ 4/3`), unsubtracted `3 τ_D(σ₁³) < τ_D(σ₁⁹)`. -/
theorem tauTorusOdd_superadditive_high_q (q : K) (hqge : 4 / 3 ≤ q) :
    3 * tauTorusOdd q 1 < tauTorusOdd q 4 := by
  have hq1 : 1 < q := by linarith
  have hq0 : 0 < q := by linarith
  have hs2_gt4 : 4 < (q + q⁻¹) ^ 2 := by
    have hid : (q + q⁻¹) ^ 2 - 4 = (q - 1) ^ 2 * (q + 1) ^ 2 / q ^ 2 := by field_simp; ring
    have hq1_pos : 0 < q - 1 := sub_pos.mpr hq1
    have hpos : 0 < (q + q⁻¹) ^ 2 - 4 := by rw [hid]; positivity
    linarith
  have hq9_inv_lt1 : (q⁻¹) ^ 9 < 1 := by
    have hqi_pos : 0 < q⁻¹ := inv_pos.mpr hq0
    have hqi_lt1 : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq1
    exact pow_lt_one₀ hqi_pos.le hqi_lt1 (by omega)
  have htau9_lb : (3 / 4 : K) * q ^ 9 - 1 / 4 < tauTorusOdd q 4 := by
    unfold tauTorusOdd
    rw [show 2 * 4 + 1 = 9 by omega]
    have hnum_pos : 0 < q ^ 9 + (q⁻¹) ^ 9 := by positivity
    have hdiv_lt : (q ^ 9 + (q⁻¹) ^ 9) / (q + q⁻¹) ^ 2 < (q ^ 9 + (q⁻¹) ^ 9) / 4 :=
      div_lt_div_of_pos_left hnum_pos (by norm_num) hs2_gt4
    linarith
  have htau3_ub : tauTorusOdd q 1 < q ^ 3 := by
    unfold tauTorusOdd
    rw [show 2 * 1 + 1 = 3 by omega]
    have hpos : 0 < (q ^ 3 + (q⁻¹) ^ 3) / (q + q⁻¹) ^ 2 := by positivity
    linarith
  set d : K := q - 4 / 3
  have hd : 0 ≤ d := sub_nonneg.mpr hqge
  have hq_eq : q = d + 4 / 3 := by dsimp [d]; ring
  have hexp : (3 / 4 : K) * q ^ 9 - 1 / 4 - (3 : K) * q ^ 3 =
      (3 / 4) * d ^ 9 + 9 * d ^ 8 + 48 * d ^ 7 + (448 / 3) * d ^ 6 +
        (896 / 3) * d ^ 5 + (3584 / 9) * d ^ 4 +
        (28429 / 81) * d ^ 3 + (15412 / 81) * d ^ 2 +
        (12496 / 243) * d + 68959 / 26244 := by
    rw [hq_eq]; ring
  have hpos : (0 : K) < (3 / 4) * d ^ 9 + 9 * d ^ 8 + 48 * d ^ 7 + (448 / 3) * d ^ 6 +
      (896 / 3) * d ^ 5 + (3584 / 9) * d ^ 4 +
      (28429 / 81) * d ^ 3 + (15412 / 81) * d ^ 2 +
      (12496 / 243) * d + 68959 / 26244 := by positivity
  linarith

/-- **Arm A Sub-Additivity (`1 < q ≤ 8/7`) vs Super-Additivity (`4/3 ≤ q`) Summary for `tauTorusOdd`.** -/
theorem tauTorusOdd_sub_vs_super_crossover :
    (∀ q : K, 1 < q → q ≤ 8 / 7 → tauTorusOdd q 4 < 3 * tauTorusOdd q 1) ∧
    (∀ q : K, 4 / 3 ≤ q → 3 * tauTorusOdd q 1 < tauTorusOdd q 4) :=
  ⟨tauTorusOdd_subadditive_low_q, tauTorusOdd_superadditive_high_q⟩

/-! ### Arm B: Universal Strict Super-Additivity (`3 E(3) < E(9)` for ALL `q > 1`) -/

/-- **Arm B1 — Universal `(2,1)` hook trace super-additivity (`∀ q > 1`):**
`tr((r21b q)⁹) - 3 tr((r21b q)³) = (q³ - (q⁻¹)³)³ > 0`. -/
theorem hook21_t29_strict_superadditive {q : K} (hq : 1 < q) :
    ((r21b q) ^ 9).trace - 3 * ((r21b q) ^ 3).trace = (q ^ 3 - (q⁻¹) ^ 3) ^ 3 ∧
    3 * ((r21b q) ^ 3).trace < ((r21b q) ^ 9).trace := by
  have hq0 : 0 < q := by linarith
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have ht3 := r21b_odd_trace_eq_diff q hq0.ne' hq2 1
  have ht9 := r21b_odd_trace_eq_diff q hq0.ne' hq2 4
  rw [show 2 * 1 + 1 = 3 by omega] at ht3
  rw [show 2 * 4 + 1 = 9 by omega] at ht9
  have hid : ((r21b q) ^ 9).trace - 3 * ((r21b q) ^ 3).trace = (q ^ 3 - (q⁻¹) ^ 3) ^ 3 := by
    rw [ht9, ht3]
    field_simp
    ring
  have hdiff_pos : 0 < q ^ 3 - (q⁻¹) ^ 3 := by
    have he : q ^ 3 - (q⁻¹) ^ 3 = (q - 1) * (q + 1) * (q ^ 4 + q ^ 2 + 1) / q ^ 3 := by
      field_simp; ring
    have hq1_pos : 0 < q - 1 := sub_pos.mpr hq
    rw [he]; positivity
  have hcube_pos : 0 < (q ^ 3 - (q⁻¹) ^ 3) ^ 3 := pow_pos hdiff_pos 3
  exact ⟨hid, by linarith⟩

/-- **Arm B2 — Universal balanced quantum-integer super-additivity (`∀ q > 1`):**
`[9]_q - 3 [3]_q = (q - q⁻¹)² [3]_q³ = (q - q⁻¹)² ((q - q⁻¹)² + 3)³ > 0`. -/
theorem qIntBal_t29_strict_superadditive {q : K} (hq : 1 < q) :
    qIntBal q 9 - 3 * qIntBal q 3 = (q - q⁻¹) ^ 2 * (qIntBal q 3) ^ 3 ∧
    qIntBal q 3 = (q - q⁻¹) ^ 2 + 3 ∧
    3 * qIntBal q 3 < qIntBal q 9 := by
  have hq0 : 0 < q := by linarith
  have hh_pos : 0 < q - q⁻¹ := by
    have he : q - q⁻¹ = (q - 1) * (q + 1) / q := by field_simp; ring
    have hq1_pos : 0 < q - 1 := sub_pos.mpr hq
    rw [he]; positivity
  have hq3_eq : qIntBal q 3 = (q - q⁻¹) ^ 2 + 3 := by
    unfold qIntBal
    rw [div_eq_iff hh_pos.ne']
    field_simp
    ring
  have hid : qIntBal q 9 - 3 * qIntBal q 3 = (q - q⁻¹) ^ 2 * (qIntBal q 3) ^ 3 := by
    rw [hq3_eq]
    unfold qIntBal
    apply mul_right_cancel₀ hh_pos.ne'
    rw [sub_mul, div_mul_cancel₀ _ hh_pos.ne']
    field_simp
    ring
  have hpos : 0 < (q - q⁻¹) ^ 2 * (qIntBal q 3) ^ 3 := by
    rw [hq3_eq]; positivity
  exact ⟨hid, hq3_eq, by linarith⟩

/-- **Arm B3 — Universal subtracted continuant super-additivity (`∀ q > 1`):**
`(f₉(h) - 1) - 3(f₃(h) - 1) = h²(h⁶ + 7h⁴ + 15h² + 7) > 0`. -/
theorem deltaContinuant_t29_strict_superadditive {q : K} (hq : 1 < q) :
    let h := q - q⁻¹
    (heckeCont h 9 - 1) - 3 * (heckeCont h 3 - 1) =
      h ^ 2 * (h ^ 6 + 7 * h ^ 4 + 15 * h ^ 2 + 7) ∧
    3 * (heckeCont h 3 - 1) < heckeCont h 9 - 1 := by
  have hq0 : 0 < q := by linarith
  have hh_pos : 0 < q - q⁻¹ := by
    have he : q - q⁻¹ = (q - 1) * (q + 1) / q := by field_simp; ring
    have hq1_pos : 0 < q - 1 := sub_pos.mpr hq
    rw [he]; positivity
  have hid :
      (heckeCont (q - q⁻¹) 9 - 1) - 3 * (heckeCont (q - q⁻¹) 3 - 1) =
        (q - q⁻¹) ^ 2 *
          ((q - q⁻¹) ^ 6 + 7 * (q - q⁻¹) ^ 4 + 15 * (q - q⁻¹) ^ 2 + 7) := by
    simp only [heckeCont]; ring
  have hpos :
      0 < (q - q⁻¹) ^ 2 *
        ((q - q⁻¹) ^ 6 + 7 * (q - q⁻¹) ^ 4 + 15 * (q - q⁻¹) ^ 2 + 7) := by
    positivity
  exact ⟨hid, by linarith⟩

/-- Positive degree-18 Taylor quotient `Q₁₈(q)` in `(Δτ_D(9) - 3 Δτ_D(3)) = (q - 1)² Q₁₈(q) / (q⁷(q²+1)²)`. -/
def deltaTauQuotientPoly {R : Type*} [CommRing R] (q : R) : R :=
  let t := q - 1
  t ^ 18 + 20 * t ^ 17 + 191 * t ^ 16 + 1158 * t ^ 15 + 4999 * t ^ 14 +
    16336 * t ^ 13 + 41937 * t ^ 12 + 86606 * t ^ 11 + 146078 * t ^ 10 +
    203025 * t ^ 9 + 233329 * t ^ 8 + 221381 * t ^ 7 + 172152 * t ^ 6 +
    108155 * t ^ 5 + 53561 * t ^ 4 + 20055 * t ^ 3 + 5269 * t ^ 2 + 832 * t + 50

/-- **Arm B4 — Universal subtracted Convention-D Markov trace super-additivity (`∀ q > 1`):**
subtracting the classical `q = 1` transposition baseline `τ_D(σ₁^{2m+1}; 1) = 1/2` gives
`(τ_D(σ₁⁹) - 1/2) - 3(τ_D(σ₁³) - 1/2) = (q - 1)² Q₁₈(q) / (q⁷ (q² + 1)²) > 0` for **all** `q > 1`. -/
theorem deltaTauTorus_t29_strict_superadditive {q : K} (hq : 1 < q) :
    (tauTorusOdd q 4 - 1 / 2) - 3 * (tauTorusOdd q 1 - 1 / 2) =
      (q - 1) ^ 2 * deltaTauQuotientPoly q / (q ^ 7 * (q ^ 2 + 1) ^ 2) ∧
    3 * (tauTorusOdd q 1 - 1 / 2) < tauTorusOdd q 4 - 1 / 2 := by
  have hq0 : 0 < q := by linarith
  have ht : 0 < q - 1 := sub_pos.mpr hq
  have hs : q + q⁻¹ ≠ 0 := by positivity
  have hid :
      (tauTorusOdd q 4 - 1 / 2) - 3 * (tauTorusOdd q 1 - 1 / 2) =
        (q - 1) ^ 2 * deltaTauQuotientPoly q / (q ^ 7 * (q ^ 2 + 1) ^ 2) := by
    unfold tauTorusOdd deltaTauQuotientPoly
    rw [show 2 * 4 + 1 = 9 by omega, show 2 * 1 + 1 = 3 by omega]
    have he : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
    rw [he]
    field_simp
    ring
  have hQ_pos : 0 < deltaTauQuotientPoly q := by
    unfold deltaTauQuotientPoly
    dsimp only
    positivity
  have hpos : 0 < (q - 1) ^ 2 * deltaTauQuotientPoly q / (q ^ 7 * (q ^ 2 + 1) ^ 2) := by
    positivity
  exact ⟨hid, by linarith⟩

end OrderedSignAudit

/-! ## Section 5: Self-Energy Resolvent Second-Sheet Pole Shift & Rule-13a Conditional Carrier -/

section ResolventThresholdInstability

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Squared modulus `|z - E - Δ + i Γ / 2|² = (zRe - E - Δ)² + (zIm + Γ / 2)²` of the inverse
dressed propagator `G_n(z)⁻¹` at complex energy `z = zRe + i zIm`. -/
def resolventInvDenomSq (E Δ Γ zRe zIm : K) : K :=
  (zRe - E - Δ) ^ 2 + (zIm + Γ / 2) ^ 2

/-- Threshold 3-body decay width `Γ₉ = g₃² φ₃ (E₉ - 3 E₃)²` when the `(3,3,3)` channel is open. -/
def threeBodyThresholdWidth (g3 φ3 E3 E9 : K) : K :=
  g3 ^ 2 * φ3 * (E9 - 3 * E3) ^ 2

/-- **Below-threshold real-axis stability (`n ∈ {3, 5, 7}`, `Γ_n = 0`):** when the 3-knot
absorptive width vanishes, `G_n(z)⁻¹` has a unique zero on the real energy axis at
`(zRe, zIm) = (E + Δ, 0)`. -/
theorem resolvent_stable_below_three_knot_threshold (E Δ zRe zIm : K) :
    resolventInvDenomSq E Δ 0 zRe zIm = 0 ↔ (zRe = E + Δ ∧ zIm = 0) := by
  unfold resolventInvDenomSq
  rw [zero_div, add_zero]
  constructor
  · intro hz
    have h1 : (zRe - E - Δ) ^ 2 = 0 := by nlinarith [sq_nonneg (zRe - E - Δ), sq_nonneg zIm]
    have h2 : zIm ^ 2 = 0 := by nlinarith [sq_nonneg (zRe - E - Δ), sq_nonneg zIm]
    have hr : zRe - E - Δ = 0 := sq_eq_zero_iff.mp h1
    have hi : zIm = 0 := sq_eq_zero_iff.mp h2
    exact ⟨by linarith, hi⟩
  · rintro ⟨rfl, rfl⟩
    ring

/-- **Above-threshold second-sheet instability (`n = 9`, `3 E₃ < E₉`, `g₃ ≠ 0`):**
1. `0 < Γ₉`,
2. For **every** real energy `zRe : K`, `0 < (Γ₉ / 2)² ≤ |G₉(zRe + i 0)⁻¹|²` (hence **no** real pole),
3. The dressed pole moves strictly into the lower half-plane at `(E₉ + Δ₉, -Γ₉ / 2)` (`zIm < 0`). -/
theorem resolvent_second_sheet_above_threshold {g3 φ3 E3 E9 Δ9 : K}
    (hg : g3 ≠ 0) (hφ : 0 < φ3) (hopen : 3 * E3 < E9) :
    let Γ9 := threeBodyThresholdWidth g3 φ3 E3 E9
    0 < Γ9 ∧
    (∀ zRe : K, (Γ9 / 2) ^ 2 ≤ resolventInvDenomSq E9 Δ9 Γ9 zRe 0 ∧
      resolventInvDenomSq E9 Δ9 Γ9 zRe 0 ≠ 0) ∧
    -Γ9 / 2 < 0 ∧
    resolventInvDenomSq E9 Δ9 Γ9 (E9 + Δ9) (-Γ9 / 2) = 0 := by
  have hg2 : 0 < g3 ^ 2 := sq_pos_of_ne_zero hg
  have hQ : 0 < E9 - 3 * E3 := sub_pos.mpr hopen
  have hΓ : 0 < threeBodyThresholdWidth g3 φ3 E3 E9 := by
    unfold threeBodyThresholdWidth
    positivity
  refine ⟨hΓ, ?_, ?_, ?_⟩
  · intro zRe
    unfold resolventInvDenomSq
    rw [zero_add]
    have hsq : 0 ≤ (zRe - E9 - Δ9) ^ 2 := sq_nonneg _
    have hhalf_pos : 0 < (threeBodyThresholdWidth g3 φ3 E3 E9 / 2) ^ 2 := by positivity
    exact ⟨by linarith, by linarith⟩
  · linarith
  · unfold resolventInvDenomSq
    ring

/-- **Rule-13a Conditional Conjecture Carrier (Zero Instances):**
Isolates the open physical bridge needed for Option 3B (`qou-618l`) to exclude `T(2,9)` as a 4th
fundamental chiral generation:
1. `energyMap : ℕ → K` assigns single-fermion rest energy to odd windings `n ∈ admissibleOddTorusSet`
   with `3 * energyMap 3 < energyMap 9` (satisfied unconditionally by Arm B functionals for all
   `q > 1`, but open because the physical `T(2,n) ↦ m_phys(n)` mass map is still open),
2. `fissionCoupling_ne_zero`: nonzero 3-body transition vertex `g₃ ≠ 0` on `(3, 3, 3)`, and
3. `fundamentalGen_iff_zero_threeKnotWidth`: a genus-`≤ 4` odd torus winding defines an independent
   asymptotic chiral generation if and only if its 3-body odd-knot fission width vanishes
   (encoding Fock-space compositeness / continuum dissolution of `σ₁⁹ ∈ ℤ[h][σ₁³]`). -/
class CompositeT29DecayExclusionHypothesis (K : Type*) [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] where
  energyMap : ℕ → K
  fissionCoupling : K
  phaseSpaceFactor : K
  fundamentalGenPred : ℕ → Prop
  energy_t29_superadditive : 3 * energyMap 3 < energyMap 9
  fissionCoupling_ne_zero : fissionCoupling ≠ 0
  phaseSpaceFactor_pos : 0 < phaseSpaceFactor
  threeKnotWidth : ℕ → K := fun n =>
    if (threeOddKnotChannels n).Nonempty then
      threeBodyThresholdWidth fissionCoupling phaseSpaceFactor (energyMap 3) (energyMap n)
    else 0
  threeKnotWidth_def : ∀ n, threeKnotWidth n =
    if (threeOddKnotChannels n).Nonempty then
      threeBodyThresholdWidth fissionCoupling phaseSpaceFactor (energyMap 3) (energyMap n)
    else 0
  fundamentalGen_iff_zero_threeKnotWidth :
    ∀ n ∈ admissibleOddTorusSet, fundamentalGenPred n ↔ threeKnotWidth n = 0

/-- **Conditional 3-Generation Stability Theorem (`qou-618l`):** under
`CompositeT29DecayExclusionHypothesis`, `n ∈ {3, 5, 7}` have `threeKnotWidth n = 0` (surviving as
stable generations), while `n = 9` has `0 < threeKnotWidth 9` (excluded), leaving exactly `{3, 5, 7}`. -/
theorem surviving_generations_eq_three_five_seven_of_hypothesis
    [ctx : CompositeT29DecayExclusionHypothesis K] :
    ctx.threeKnotWidth 3 = 0 ∧
    ctx.threeKnotWidth 5 = 0 ∧
    ctx.threeKnotWidth 7 = 0 ∧
    0 < ctx.threeKnotWidth 9 ∧
    (ctx.fundamentalGenPred 3 ∧ ctx.fundamentalGenPred 5 ∧
      ctx.fundamentalGenPred 7 ∧ ¬ ctx.fundamentalGenPred 9) := by
  have hch := threeOddKnotChannels_bring_window
  have hw3 : ctx.threeKnotWidth 3 = 0 := by rw [ctx.threeKnotWidth_def, hch.1]; simp
  have hw5 : ctx.threeKnotWidth 5 = 0 := by rw [ctx.threeKnotWidth_def, hch.2.1]; simp
  have hw7 : ctx.threeKnotWidth 7 = 0 := by rw [ctx.threeKnotWidth_def, hch.2.2.1]; simp
  have hne9 : (threeOddKnotChannels 9).Nonempty := by
    rw [hch.2.2.2.1]; exact Finset.singleton_nonempty _
  have hw9_pos : 0 < ctx.threeKnotWidth 9 := by
    rw [ctx.threeKnotWidth_def, if_pos hne9]
    exact (resolvent_second_sheet_above_threshold ctx.fissionCoupling_ne_zero
      ctx.phaseSpaceFactor_pos ctx.energy_t29_superadditive (Δ9 := 0)).1
  have hadm : (3 : ℕ) ∈ admissibleOddTorusSet ∧ (5 : ℕ) ∈ admissibleOddTorusSet ∧
      (7 : ℕ) ∈ admissibleOddTorusSet ∧ (9 : ℕ) ∈ admissibleOddTorusSet := by
    rw [admissibleOddTorusSet_eq.1]; decide
  refine ⟨hw3, hw5, hw7, hw9_pos, ?_, ?_, ?_, ?_⟩
  · exact (ctx.fundamentalGen_iff_zero_threeKnotWidth 3 hadm.1).mpr hw3
  · exact (ctx.fundamentalGen_iff_zero_threeKnotWidth 5 hadm.2.1).mpr hw5
  · exact (ctx.fundamentalGen_iff_zero_threeKnotWidth 7 hadm.2.2.1).mpr hw7
  · intro h9
    have hz := (ctx.fundamentalGen_iff_zero_threeKnotWidth 9 hadm.2.2.2).mp h9
    linarith

end ResolventThresholdInstability

end QOU.StandardModel.CompositeT29ThresholdInstability
