import QOU.StandardModel.BringGenerationSplitAndCKMTexture
import QOU.StandardModel.CompositeT29ThresholdInstability
import QOU.StandardModel.S3CirculantKoideTraceIdentity
import QOU.StandardModel.KoideSingletDoubletEquipartition
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith

/-!
# Bring $N_{\mathrm{gen}} = 3$ Complete-Intersection Fission Weld & Satellite $T(2,n)\text{–}4_1$ Tau Mass Adjudication (`qou-gen3` + `qou-htk4`)

Formalizes over generic rings and ordered fields (`AGENTS.md §7c`: zero `ℝ`, zero empirical
decimal literals, zero `sorry`, zero custom `axiom`s) the structural unification of:

1. **§1 — Bring's Genus-$4$ Complete Intersection $\Sigma_4 \subset \mathbb{P}^4$, $\mathbb{Z}_3 \subset \mathfrak{S}_3 \subset \mathfrak{S}_5$ `3 + 1` Split, and Composite $T(2,9) \to 3\,T(2,3)$ Fission (`qou-gen3`):**
   - Complete-intersection degree $d = 1 \cdot 2 \cdot 3 = 6$, canonical adjunction degree
     $\deg K_{\Sigma_4} = 6(1 + 2 + 3 - 5) = 6$, Euler characteristic $\chi(\Sigma_4) = -6$, and
     genus $g(\Sigma_4) = 4 = \dim H^{1,0}(\Sigma_4)$.
   - Exact cyclic $\mathbb{Z}_3 = A_3 \subset \mathfrak{S}_3 \subset \mathfrak{S}_5$ character
     branching $\mathrm{Res}^{\mathfrak{S}_5}_{\mathbb{Z}_3} V_{(4,1)} = V_{\omega \oplus \bar\omega} \oplus 2\,V_{\mathrm{triv}}$
     refining the $\mathfrak{S}_4$ split $4 = 3 + 1$, welded directly to the topological partition
     of `admissibleOddTorusSet = {3, 5, 7, 9}` (`card = 4`) into the `3` three-body-indecomposable
     generation windings `{3, 5, 7}` (`card = 3`) and the `1` composite fissioning winding `{9}`
     (`threeOddKnotChannels 9 = {((3, 3), 3)}`).

2. **§2 — Soma JSJ Simplicial-Volume Dichotomy & Agol Two-Cusped Forbidden-Gap Exclusion (`qou-htk4`):**
   - Proves that Seifert-fibred cable satellites $C_{2,2m+1}(4_1)$ have winding-independent JSJ
     volume `vol41` and unit three-point `bend = 1`.
   - Proves via Agol's two-cusped hyperbolic minimum volume bound (`4 * G_Catalan ≤ volPattern`)
     that `[33/10, 35/10]` lies strictly inside the topological forbidden gap `(vol41, vol41 + 4G)`
     between all Seifert cables and all hyperbolic satellites (Whitehead, Mazur, twisted Whitehead,
     Berge, or iterated patterns) at third-generation pole order `k = 3`.

3. **§3 — Figure-Eight $A$-Polynomial Cone-Holonomy Hyperbolicity Window ($M_n(4_1)$, $n \ge 4$):**
   - Proves the exact algebraic factorization `figEightLongTrace c - 1 = (1 - c)(1 + 2c)` and
     completed square `17/8 - figEightLongTrace c = 2(c - 1/4)²` governing the Schläfli integral
     of $n$-fold cyclic branched covers $M_n(4_1)$ across the hyperbolic orbifold window
     `-1/2 < c < 1` (`0 < 2π/n < 2π/3`, i.e. `n ≥ 4`, collapsing at Euclidean `n = 3`, `c = -1/2`).

4. **§4 — Bring $\mathbf{4} \otimes \overline{\mathbf{4}} = \mathbf{1} \oplus \mathbf{15}$ Quantum-Dimension Identity & Rule-13a Koide Protection Class:**
   - Proves `[4]_q² = 1 + [3]_q [5]_q` over any `[Field F]` (`q ≠ 0`, `q - q⁻¹ ≠ 0`).
   - Isolates `KoideTopologicalProtectionHypothesis` (`0` global instances, `0` `True` fields),
     deriving the monic quadratic $\sqrt{m_\tau}$ resolvent from protected singlet–doublet
     equipartition welded to the figure-eight muon input.

## References

- [braden-disney-hogg-2022] Braden & Disney-Hogg, Eur. J. Math. 10 (2024) 3, arXiv:2208.13692
- [rolfsen1976] Rolfsen, Knots and Links (1976)
- [koide1983prd] Koide, Phys. Rev. D 28 (1983) 252–254
-/

set_option autoImplicit false

namespace QOU.StandardModel.BringThreeGenerationsAndTauSatellite

open QOU.Brings
open QOU.StandardModel.BringGenerationSplitAndCKMTexture
open QOU.StandardModel.CompositeT29ThresholdInstability
open QOU.StandardModel.S3CirculantKoideTraceIdentity

/-! ## §1. Complete-Intersection Adjunction of $\Sigma_4 \subset \mathbb{P}^4$ & `3 + 1` Fission Weld -/

section BringAdjunctionAndFissionWeld

/-- Bézout complete-intersection degree $1 \cdot 2 \cdot 3 = 6$ of
    $\Sigma_4 = \{p_1 = p_2 = p_3 = 0\} \subset \mathbb{P}^4$. -/
def bringIntersectionDegree : ℕ :=
  1 * 2 * 3

/-- Canonical bundle degree $\deg K_{\Sigma_4} = d \cdot ((1 + 2 + 3) - 5) = 6$ by adjunction on $\mathbb{P}^4$. -/
def bringCanonicalDegree : ℤ :=
  (bringIntersectionDegree : ℤ) * ((1 + 2 + 3 : ℤ) - 5)

/-- Topological Euler characteristic $\chi(\Sigma_4) = -\deg K_{\Sigma_4} = -6$. -/
def bringEulerChar : ℤ :=
  -bringCanonicalDegree

/-- Arithmetic/topological genus $g(\Sigma_4) = 4$ satisfying $2g - 2 = \deg K_{\Sigma_4}$. -/
def bringGenus : ℕ :=
  4

/-- **Complete-intersection adjunction & $H^{1,0}(\Sigma_4)$ dimension identity**:
    $\deg \Sigma_4 = 6$, $\deg K_{\Sigma_4} = 6$, $\chi(\Sigma_4) = -6$, $2g - 2 = \deg K_{\Sigma_4}$,
    and $\dim V_{(4,1)} = \chi_{\mathrm{std}}(1) = g = 4$. -/
theorem bring_adjunction_euler_and_h10_dim :
    bringIntersectionDegree = 6 ∧
    bringCanonicalDegree = 6 ∧
    bringEulerChar = -6 ∧
    2 * (bringGenus : ℤ) - 2 = bringCanonicalDegree ∧
    S5Char.chiStd 0 = (bringGenus : ℤ) := by
  decide

/-- Conjugacy class sizes of the cyclic colour/generation subgroup $\mathbb{Z}_3 = A_3 = \langle(0\,1\,2)\rangle$. -/
def z3ClassSize : Fin 3 → ℤ :=
  ![1, 1, 1]

/-- Inclusion of $\mathbb{Z}_3 = \{1, (0\,1\,2), (0\,2\,1)\}$ into the 7 conjugacy classes of $\mathfrak{S}_5$. -/
def z3ToS5Class : Fin 3 → Fin 7 :=
  ![0, 3, 3]

/-- Restriction of an $\mathfrak{S}_5$ class function to $\mathbb{Z}_3 \subset \mathfrak{S}_5$. -/
def resS5ToZ3 (χ : Fin 7 → ℤ) : Fin 3 → ℤ :=
  fun c => χ (z3ToS5Class c)

/-- Unscaled character inner product $3\langle \chi, \psi \rangle_{\mathbb{Z}_3}$. -/
def z3Inner (χ ψ : Fin 3 → ℤ) : ℤ :=
  z3ClassSize 0 * χ 0 * ψ 0 + z3ClassSize 1 * χ 1 * ψ 1 + z3ClassSize 2 * χ 2 * ψ 2

/-- Trivial character of $\mathbb{Z}_3$. -/
def z3ChiTriv : Fin 3 → ℤ :=
  ![1, 1, 1]

/-- Real 2-dimensional chiral character $\omega \oplus \bar\omega$ of $\mathbb{Z}_3$ over $\mathbb{Z}$. -/
def z3ChiChiralPair : Fin 3 → ℤ :=
  ![2, -1, -1]

/-- Subset of Bring's genus-`≤ 4` odd torus knots `{3, 5, 7, 9}` that have **zero** 3-body odd-knot
    fission channels. -/
def indecomposableGenerationWindings : Finset ℕ :=
  admissibleOddTorusSet.filter (fun n => (threeOddKnotChannels n).card = 0)

/-- Subset of Bring's genus-`≤ 4` odd torus knots `{3, 5, 7, 9}` that possess an open 3-body
    odd-knot fission channel (`T(2,9) -> 3 T(2,3)`). -/
def compositeFissionWindings : Finset ℕ :=
  admissibleOddTorusSet.filter (fun n => 0 < (threeOddKnotChannels n).card)

theorem indecomposableGenerationWindings_eq :
    indecomposableGenerationWindings = {3, 5, 7} := by
  have hch := threeOddKnotChannels_bring_window
  ext n
  simp only [indecomposableGenerationWindings, admissibleOddTorusSet_eq.1,
    Finset.mem_filter, Finset.mem_insert, Finset.mem_singleton]
  constructor
  · rintro ⟨hn | hn | hn | hn, h0⟩
    · exact Or.inl hn
    · exact Or.inr (Or.inl hn)
    · exact Or.inr (Or.inr hn)
    · subst hn; rw [hch.2.2.2.2] at h0; omega
  · rintro (rfl | rfl | rfl)
    · exact ⟨Or.inl rfl, by simp [hch.1]⟩
    · exact ⟨Or.inr (Or.inl rfl), by simp [hch.2.1]⟩
    · exact ⟨Or.inr (Or.inr (Or.inl rfl)), by simp [hch.2.2.1]⟩

theorem compositeFissionWindings_eq :
    compositeFissionWindings = {9} := by
  have hch := threeOddKnotChannels_bring_window
  ext n
  simp only [compositeFissionWindings, admissibleOddTorusSet_eq.1,
    Finset.mem_filter, Finset.mem_insert, Finset.mem_singleton]
  constructor
  · rintro ⟨hn | hn | hn | hn, hpos⟩
    · subst hn; simp [hch.1] at hpos
    · subst hn; simp [hch.2.1] at hpos
    · subst hn; simp [hch.2.2.1] at hpos
    · exact hn
  · rintro rfl
    exact ⟨Or.inr (Or.inr (Or.inr rfl)), by rw [hch.2.2.2.2]; omega⟩

/-- **Unified `4 = 3 + 1` Representation & Topological Fission Bridge (`qou-gen3`)**:
    1. Under $\mathbb{Z}_3 \subset \mathfrak{S}_3 \subset \mathfrak{S}_4 \subset \mathfrak{S}_5$,
       $H^{1,0}(\Sigma_4) \cong V_{(4,1)}$ (`dim = 4`) branches as `s4ChiStd + s4ChiTriv` (`3 + 1`)
       and on $\mathbb{Z}_3$ as `z3ChiChiralPair + 2 * z3ChiTriv` (`(2 + 1) + 1 = 3 + 1`), with
       orthogonality `z3Inner z3ChiChiralPair z3ChiTriv = 0`.
    2. Topologically, `admissibleOddTorusSet = {3, 5, 7, 9}` (`card = 4 = bringGenus`) partitions
       disjointly into `indecomposableGenerationWindings = {3, 5, 7}` (`card = 3 = s4ChiStd 0`)
       and `compositeFissionWindings = {9}` (`card = 1 = s4ChiTriv 0`). -/
theorem bring_three_plus_one_generation_fission_weld :
    (∀ c : Fin 3, resS5ToZ3 S5Char.chiStd c = z3ChiChiralPair c + 2 * z3ChiTriv c) ∧
    z3Inner z3ChiChiralPair z3ChiTriv = 0 ∧
    z3Inner (resS5ToZ3 S5Char.chiStd) z3ChiTriv = 6 ∧
    indecomposableGenerationWindings = {3, 5, 7} ∧
    compositeFissionWindings = {9} ∧
    (indecomposableGenerationWindings.card : ℤ) = s4ChiStd 0 ∧
    (compositeFissionWindings.card : ℤ) = s4ChiTriv 0 ∧
    (admissibleOddTorusSet.card : ℤ) = S5Char.chiStd 0 ∧
    Disjoint indecomposableGenerationWindings compositeFissionWindings ∧
    indecomposableGenerationWindings ∪ compositeFissionWindings = admissibleOddTorusSet := by
  rw [indecomposableGenerationWindings_eq, compositeFissionWindings_eq, admissibleOddTorusSet_eq.1]
  decide

end BringAdjunctionAndFissionWeld

/-! ## §2. Soma JSJ Volume Dichotomy & Agol Two-Cusped Forbidden-Gap Theorem (`qou-htk4`) -/

section SatelliteJSJAndAgolGap

/-- JSJ simplicial volume `Vol(P(K)) = Vol(K) + Vol((S¹ × D²) \ P)` across an incompressible
    companion torus (Gromov–Thurston–Soma additivity). -/
def satelliteJSJVolume {R : Type*} [AddMonoid R] (volCompanion volPattern : R) : R :=
  volCompanion + volPattern

/-- **Seifert cable JSJ volume rigidity & unit three-point bend**:
    For every Seifert-fibred cable pattern (`volPattern = 0`, covering $C_{2,3}(4_1)$,
    $C_{2,5}(4_1)$, $C_{2,7}(4_1)$), `satelliteJSJVolume vol41 0 = vol41`, so the three-point
    lepton bend ratio `x(5)² / (x(3) * x(7))` equals `1` identically. -/
theorem pure_cable_jsj_volume_and_unit_bend {F : Type*} [Field F]
    (vol41 : F) (hvol : vol41 ≠ 0) :
    satelliteJSJVolume vol41 0 = vol41 ∧
    (satelliteJSJVolume vol41 0) ^ 2 /
      (satelliteJSJVolume vol41 0 * satelliteJSJVolume vol41 0) = 1 := by
  unfold satelliteJSJVolume
  rw [add_zero]
  refine ⟨rfl, ?_⟩
  field_simp

/-- **Universal Soma–Agol Satellite Forbidden-Gap Exclusion at Pole Order `k = 3`**:
    Over any ordered field `K`, if `202 / 100 < vol41 < 204 / 100`, `91 / 100 < catalanG`,
    and `33 / 10 < volTarget < 35 / 10` (rational enclosures of $\mathrm{Vol}(4_1)$,
    Catalan's constant $G$, and $\mathrm{Vol}_{\mathrm{req}}^{(k=3)} = \hbar_{q_0}^3 m_\tau / m_e$),
    then for **every** satellite pattern obeying the Thurston–Agol dichotomy
    `volPattern = 0 ∨ 4 * catalanG ≤ volPattern`:
    1. Every Seifert cable undershoots `volTarget` by at least `63 / 50`;
    2. Every hyperbolic satellite (Whitehead, Mazur, twisted Whitehead, Berge, or iterated)
       overshoots `volTarget` by at least `54 / 25`;
    3. No satellite JSJ volume lies in `[33 / 10, 35 / 10]`. -/
theorem soma_agol_satellite_forbidden_gap_k3
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (vol41 catalanG volPattern volTarget : K)
    (h41_lo : (202 : K) / 100 < vol41)
    (h41_hi : vol41 < (204 : K) / 100)
    (hG_lo : (91 : K) / 100 < catalanG)
    (ht_lo : (33 : K) / 10 < volTarget)
    (ht_hi : volTarget < (35 : K) / 10) :
    (volPattern = 0 → (63 : K) / 50 < volTarget - satelliteJSJVolume vol41 volPattern) ∧
    (4 * catalanG ≤ volPattern → (54 : K) / 25 < satelliteJSJVolume vol41 volPattern - volTarget) ∧
    ((volPattern = 0 ∨ 4 * catalanG ≤ volPattern) →
      ¬ ((33 : K) / 10 ≤ satelliteJSJVolume vol41 volPattern ∧
         satelliteJSJVolume vol41 volPattern ≤ (35 : K) / 10)) := by
  unfold satelliteJSJVolume
  refine ⟨?_, ?_, ?_⟩
  · intro hp
    rw [hp]
    linarith
  · intro hp
    linarith
  · intro hdich hmem
    rcases hdich with hp | hp
    · rw [hp] at hmem
      linarith [hmem.1]
    · linarith [hmem.2]

end SatelliteJSJAndAgolGap

/-! ## §3. Figure-Eight $A$-Polynomial Cone-Holonomy Hyperbolicity Window ($M_n(4_1)$) -/

section BranchedCoverConeHolonomy

/-- Longitudinal half-trace `cosh(ℓ(α)/2) = 2 + c - 2c²` (`c = cos α`, `α = 2π/n`) determined by
    the figure-eight $A$-polynomial $L + L^{-1} = 2 + (M^2 + M^{-2}) - (M^4 + M^{-4})$ along
    $M^2 = e^{i\alpha}$, entering Mednykh's Schläfli integral for $\mathrm{Vol}(M_n(4_1))$. -/
def figEightLongTrace {R : Type*} [CommRing R] (c : R) : R :=
  2 + c - 2 * c ^ 2

/-- **Exact factorization at the parabolic cusp (`c = 1`) and Euclidean `n = 3` orbifold (`c = -1/2`)**:
    `figEightLongTrace c - 1 = (1 - c) * (1 + 2 * c)`. -/
theorem figEightLongTrace_sub_one_factor {R : Type*} [CommRing R] (c : R) :
    figEightLongTrace c - 1 = (1 - c) * (1 + 2 * c) := by
  unfold figEightLongTrace
  ring

/-- **Division-free completed-square peak identity (`8 * figEightLongTrace(1/4) = 17`)**
    over any `[CommRing R]`. -/
theorem figEightLongTrace_completed_square {R : Type*} [CommRing R] (c : R) :
    17 - 8 * figEightLongTrace c = (4 * c - 1) ^ 2 := by
  unfold figEightLongTrace
  ring

/-- **Hyperbolicity window of $4_1(n)$ (`n ≥ 4` vs Euclidean `n = 3`)**:
    Over any ordered field `K`, `1 < figEightLongTrace c` holds strictly across `-1 / 2 < c < 1`
    (all cone angles `0 < 2π/n < 2π/3`, i.e. `n ≥ 4`), vanishes to `1` at `c = -1 / 2` (`n = 3`)
    and `c = 1` (`α = 0`), and never exceeds `17 / 8`. -/
theorem figEightLongTrace_hyperbolic_window
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (c : K) (hlo : -(1 / 2 : K) < c) (hhi : c < 1) :
    1 < figEightLongTrace c ∧ figEightLongTrace c ≤ (17 : K) / 8 := by
  have hfac : figEightLongTrace c - 1 = (1 - c) * (1 + 2 * c) :=
    figEightLongTrace_sub_one_factor c
  have hpos1 : 0 < 1 - c := by linarith
  have hpos2 : 0 < 1 + 2 * c := by linarith
  have hprod : 0 < (1 - c) * (1 + 2 * c) := mul_pos hpos1 hpos2
  have hsq : 17 - 8 * figEightLongTrace c = (4 * c - 1) ^ 2 :=
    figEightLongTrace_completed_square c
  have hnonneg : 0 ≤ (4 * c - 1) ^ 2 := sq_nonneg (4 * c - 1)
  exact ⟨by linarith, by linarith⟩

end BranchedCoverConeHolonomy

/-! ## §4. Bring $\mathbf{4} \otimes \overline{\mathbf{4}} = \mathbf{1} \oplus \mathbf{15}$ Quantum-Dimension Identity & Rule-13a Koide Protection -/

section QuantumDimensionAndKoideProtection

/-- Balanced quantum integer `[k]_q = (q^k - q^{-k}) / (q - q⁻¹)` for `k : ℕ`. -/
def qBal {F : Type*} [Field F] (k : ℕ) (q : F) : F :=
  (q ^ k - (q⁻¹) ^ k) / (q - q⁻¹)

/-- **Exact $\mathfrak{su}_q(4)$ / Bring-$H^{1,0}(\Sigma_4)$ Tensor-Square Identity**:
    `[4]_q² = 1 + [3]_q * [5]_q` (`16 = 1 + 3 * 5` at `q = 1`), decomposing the squared quantum
    dimension of Bring's 4D canonical space into the singlet `1` plus the `15`-dimensional
    adjoint `[3]_q [5]_q`. -/
theorem qBal_four_sq_eq_one_add_three_mul_five {F : Type*} [Field F]
    (q : F) (hq : q ≠ 0) (hqh : q - q⁻¹ ≠ 0) :
    qBal 4 q ^ 2 = 1 + qBal 3 q * qBal 5 q := by
  unfold qBal
  have hqh2 : (q - q⁻¹) ^ 2 ≠ 0 := pow_ne_zero 2 hqh
  have hunit : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  have hnum :
      (q ^ 4 - (q⁻¹) ^ 4) ^ 2 =
        (q - q⁻¹) ^ 2 + (q ^ 3 - (q⁻¹) ^ 3) * (q ^ 5 - (q⁻¹) ^ 5) := by
    linear_combination (q - q⁻¹) ^ 2 * ((q * q⁻¹) ^ 2 + q * q⁻¹ + 1) * hunit
  rw [div_pow, div_mul_div_comm, ← sq, one_add_div hqh2, hnum]

/-- **Rule-13a Zero-Instance Hypothesis Class (`KoideTopologicalProtectionHypothesis`)**:
    Encapsulates the surviving zero-parameter mechanism for the third-to-first generation
    mass ratio:
    1. Topological protection of the classical $q \to 1$ Temperley–Lieb singlet–doublet
       equipartition `3 * (u² + v² + x²) = 2 * (u + v + x)²` on Bring's three-generation module
       `projGen3` against the finite-$q$ Wedderburn drift;
    2. Figure-eight hyperbolic saddle pinning `(v / u)² * (1 - q⁻¹)² = vol41` for the
       second-generation square-root ratio `v / u = √(m_μ / m_e)`. -/
class KoideTopologicalProtectionHypothesis (F : Type*) [Field F] (q vol41 : F) where
  /-- Electron square-root mass amplitude `u > 0`. -/
  uAmp : F
  /-- Muon square-root mass amplitude `v`. -/
  vAmp : F
  /-- Tau square-root mass amplitude `x`. -/
  xAmp : F
  /-- Non-vanishing electron amplitude (`u ≠ 0`). -/
  h_u_ne_zero : uAmp ≠ 0
  /-- Protected $q \to 1$ Koide trace-to-norm identity `3(u² + v² + x²) = 2(u + v + x)²`. -/
  h_protected_koide :
    3 * (uAmp ^ 2 + vAmp ^ 2 + xAmp ^ 2) = 2 * (uAmp + vAmp + xAmp) ^ 2
  /-- Second-generation figure-eight saddle identity `v² * (1 - q⁻¹)² = vol41 * u²`. -/
  h_muon_vol41 :
    vAmp ^ 2 * (1 - q⁻¹) ^ 2 = vol41 * uAmp ^ 2

/-- **Derived Monic $\sqrt{m_\tau / m_e}$ Quadratic Resolvent Welded to $\mathrm{Vol}(4_1)/\hbar_q^2$**:
    Under `[h : KoideTopologicalProtectionHypothesis F q vol41]`, the normalized root ratios
    `r_μ = h.vAmp / h.uAmp` and `r_τ = h.xAmp / h.uAmp` satisfy BOTH `r_μ² = vol41 / (1 - q⁻¹)²`
    AND the parameter-free monic Koide quadratic `r_τ² - 4(1 + r_μ) r_τ + (1 + r_μ² - 4 r_μ) = 0`. -/
theorem tau_sqrt_ratio_resolvent_from_vol41
    {F : Type*} [Field F] (q vol41 : F) (hq1 : 1 - q⁻¹ ≠ 0)
    [h : KoideTopologicalProtectionHypothesis F q vol41] :
    let rMu := h.vAmp / h.uAmp
    let rTau := h.xAmp / h.uAmp
    rMu ^ 2 = vol41 / (1 - q⁻¹) ^ 2 ∧
    rTau ^ 2 - 4 * (1 + rMu) * rTau + (1 + rMu ^ 2 - 4 * rMu) = 0 := by
  have hu := h.h_u_ne_zero
  have hu2 : h.uAmp ^ 2 ≠ 0 := pow_ne_zero 2 hu
  have hq12 : (1 - q⁻¹) ^ 2 ≠ 0 := pow_ne_zero 2 hq1
  have hk := h.h_protected_koide
  have hm := h.h_muon_vol41
  dsimp only
  refine ⟨?_, ?_⟩
  · rw [div_pow, div_eq_div_iff hu2 hq12]
    linear_combination hm
  · have hpoly :
      h.xAmp ^ 2 - 4 * (h.uAmp + h.vAmp) * h.xAmp +
        (h.uAmp ^ 2 + h.vAmp ^ 2 - 4 * h.uAmp * h.vAmp) = 0 := by
      have hid := S3CirculantKoideTraceIdentity.koide_quadratic_resolvent_ring_identity
        h.uAmp h.vAmp h.xAmp
      unfold S3CirculantKoideTraceIdentity.koideResolventPoly at hid
      rw [hk, sub_self] at hid
      exact hid.symm
    have hrv : (h.vAmp / h.uAmp) * h.uAmp = h.vAmp := div_mul_cancel₀ h.vAmp hu
    have hrx : (h.xAmp / h.uAmp) * h.uAmp = h.xAmp := div_mul_cancel₀ h.xAmp hu
    rw [← hrv, ← hrx] at hpoly
    apply mul_right_cancel₀ hu2
    rw [zero_mul]
    linear_combination hpoly

/-- **Algebraic Core Discharge Bridge (`qou-cw8i`):**
    100% of the $S_3 / \mathbb{Z}_3$ projector algebra, Fourier moments, classical $V^{\otimes 3}$
    $4 = 4$ equipartition, quadratic resolvent, and radical-free quartic mass polynomial are proved
    unconditionally over `[CommRing R]` in `QOU.StandardModel.KoideSingletDoubletEquipartition`.
    Consequently, `KoideTopologicalProtectionHypothesis` reduces to the single irreducible
    1-equation physical bridge `KoideSingletDoubletEquipartitionBridge` welded to the figure-eight
    muon relation `v² (1 - q⁻¹)² = vol41 u²` (provided as a `def`, never `instance`). -/
def koideTopologicalProtection_of_singletDoubletBridge
    {R : Type*} [CommRing R] (h3 : ∀ z : R, 3 * z = 0 → z = 0)
    [B : KoideSingletDoubletEquipartition.KoideSingletDoubletEquipartitionBridge R] :
    3 * (B.leptonRootMass 0 ^ 2 + B.leptonRootMass 1 ^ 2 + B.leptonRootMass 2 ^ 2) =
        2 * (B.leptonRootMass 0 + B.leptonRootMass 1 + B.leptonRootMass 2) ^ 2 ∧
      KoideSingletDoubletEquipartition.homogKoideResolvent
          (B.leptonRootMass 0) (B.leptonRootMass 1) (B.leptonRootMass 2) = 0 ∧
      KoideSingletDoubletEquipartition.koideMassQuarticPoly
          (B.leptonRootMass 0 ^ 2) (B.leptonRootMass 1 ^ 2) (B.leptonRootMass 2 ^ 2) = 0 :=
  KoideSingletDoubletEquipartition.bridge_implies_resolvent_and_quartic h3

end QuantumDimensionAndKoideProtection

end QOU.StandardModel.BringThreeGenerationsAndTauSatellite
