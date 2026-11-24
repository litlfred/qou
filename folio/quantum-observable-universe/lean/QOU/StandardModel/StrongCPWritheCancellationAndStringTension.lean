import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.GroupTheory.Perm.Sign
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic
import QOU.StandardModel.ThetaQcdFramingCp
import QOU.MathlibInfra.ConfinementLayerTower
import QOU.MathlibExt.QIntegerCanonical

set_option autoImplicit false

/-!
# Strong-CP $\bar{\theta}_{\mathrm{QCD}} = 0$ Writhe/Determinant Cancellation & $\mathrm{SU}(3)_c$ Wilson String Tension

Pure-mathematics Lean 4 formalization for Standard Model Package 5 (`qou-tcpx` / `Q-Gap-11`,
aggregating `tqcp`, `qou-1jqd`, `qou-db6w`), authored with `0 sorry`, standard axioms only,
zero empirical constants inside `.lean`, and following `AGENTS.md §7c` base-ring generality
(generic `[CommRing R]`, `[Field K]`, and `[CommRing K] [LinearOrder K] [IsStrictOrderedRing K]`
throughout §§1–3, with paired `_real` specialisation solely where `Real.log` / `Real.exp` cross
the archimedean wall in §3.3):

1. **§1 — Topological Writhe Cancellation, Mirror-Paired $T(2,9) \oplus \overline{T(2,9)}$ Loops,
   and $\mathrm{SU}(3)_c$ $[1^3]$ Colour-Singlet Framing (`\theta_{\mathrm{top}} = 0`):**
   - Formalizes signed Artin braid words `BraidWord`, homomorphic writhe `writheWord`, bar/mirror
     involution `mirrorWord` ($\sigma_i^{\pm 1} \mapsto \sigma_i^{\mp 1}$), and the underlying
     strand permutation `wordPerm`, proving:
     * exact mirror-pair writhe cancellation `writheWord (w ++ mirrorWord w) = 0`,
     * amphicheiral substrate zero writhe on $\beta_{4_1} = \sigma_1 \sigma_2^{-1} \sigma_1 \sigma_2^{-1}$
       and $\beta_{\mathrm{Bor}} = (\sigma_1 \sigma_2^{-1})^3$,
     * non-zero chirality $w(T_{2,9}) = +9 \neq 0$ vs closed mirror-pair cancellation
       $w(T_{2,9} \oplus \overline{T_{2,9}}) = 0$,
     * exact sign–writhe parity identity `Equiv.Perm.sign (wordPerm n w) = (-1 : ℤˣ) ^ writheWord w`.
   - Constructs the explicit $3 \times 3 \times 3$ Levi-Civita colour-singlet tensor `leviCivita3`
     and rank-1 singlet projector `singletProj3` ($P_{(1^3)}^2 = P_{(1^3)}$, $\mathrm{Tr}\,P_{(1^3)} = 1$),
     proving over any `CommRing R`:
     * exact $\mathfrak{sl}_3(R)$ Lie derivation annihilation ($\mathrm{Tr}\,A = 0 \implies d\rho_{\mathbf{3}^{\otimes 3}}(A)|\varepsilon\rangle = 0$),
     * exact $\mathrm{SL}_3(R)$ invariance ($(g \otimes g \otimes g)|\varepsilon\rangle = (\det g)|\varepsilon\rangle = |\varepsilon\rangle$ for $\det g = 1$),
     * balanced-framing $[1^3]$ parity cancellation $(q \cdot (-q^{-1}))^{w(\beta)}\,\mathrm{sgn}(\pi(\beta)) = 1$.
   - Discharges `QOU.StandardModel.ThetaQCDFraming.ColorSectorCPEven` constructively on mirror-paired
     colour-singlet vacuum configurations (`colorSectorCPEvenOfMirrorPair`), and proves over any
     ordered field with $q > 0, q \neq 1$ that CP-evenness of $q^m$ ($m \in \mathbb{Z}$) forces
     $m = 0$ and $\Theta = +1 \neq -1$ (strictly selecting $\theta_{\mathrm{top}} = 0$ and excluding $\pi$).

2. **§2 — Nelson–Barr / Hermitian Quark-Mass Determinant Reality ($\arg\det(M_u M_d) = 0$) Coexisting
   with Non-Zero Jarlskog $J_{\mathrm{CP}} \neq 0$ over `QuadI R = R[i]`:**
   - Defines the generic Gaussian ring extension `QuadI R` ($R[i]$ over any `[CommRing R]`),
     conjugation homomorphism `conjHom`, and conjugate-transpose `dagger`, proving
     `conj (Matrix.det M) = Matrix.det (dagger M)` in arbitrary dimension.
   - Proves over **any** `[CommRing R]` (division-free, characteristic-independent) that $3 \times 3$
     Hermitian matrices $M_u, M_d$ with real diagonals satisfy `(Matrix.det (M_u * M_d)).im = 0`,
     and over any strict ordered ring that positive-spectrum congruence $M = A^\dagger \mathrm{diag}(d) A$
     ($d_i > 0$, $\det A \neq 0$) forces `(Matrix.det M).re > 0` (excluding $\arg\det = \pi$).
   - Proves Jarlskog's exact $3 \times 3$ commutator-cube identity
     $\mathrm{Im}\,\mathrm{Tr}([D, H]^3) = 6(u_0 - u_1)(u_1 - u_2)(u_2 - u_0)\,\mathrm{Im}(H_{01} H_{12} H_{20})$
     and constructs an explicit Hermitian positive-determinant pair `(witnessMu, witnessMd)` over
     `QuadI ℤ` with $\det(M_u M_d) = 312 > 0$ (`im = 0`) and $\mathrm{Im}\,\mathrm{Tr}([M_u^2, M_d^2]^3) = -351360 \neq 0$.
   - Proves Ellis–Gaillard 1-loop / factorized chiral dressing determinant reality
     `(Matrix.det ((H_L * M_u * H_R) * (K_L * M_d * K_R))).im = 0` even when $[H_L, M_u] \neq 0$ makes
     the dressed mass operator non-Hermitian, bounds $\bar{\theta}_{\mathrm{eff}}$ when tree contributions
     vanish, and isolates higher-loop UV counterterm finiteness as a zero-instance conditional class
     `HigherLoopStrongCPFiniteHypothesis` (Rule 13a / §3b-cond).

3. **§3 — Algebraic $\mathfrak{su}(3)_c$ Quadratic Casimir Scaling ($4/3$, $3$, Ratio $9/4$) and
   $q$-Deformed Markov-Trace / `ConfinementLayer` Wilson Area-Law String Tension:**
   - Proves from explicit matrix commutators and Fierz contractions (without $\sqrt{3}$) that the
     fundamental $\mathfrak{su}(3)_c$ Casimir operator equals $\frac{4}{3} I_3$ and the adjoint
     Casimir operator on traceless $3 \times 3$ matrices equals $3\,\mathrm{id}$ ($C_2(\mathbf{8}) / C_2(\mathbf{3}) = 9/4$),
     together with the Dynkin table ($\mathbf{1}, \mathbf{3}, \mathbf{6}, \mathbf{8}, \mathbf{10}$)
     and the $\frac{1}{2}$ baryon-to-meson pairwise colour-exchange factor ($-2/3$ vs $-4/3$).
   - Connects the rank-3 colour Markov step $z_3(q) = q^3 / [3]_q$ directly to `QOU.QInteger.qIntBal q 3`,
     proves $0 < z_3(q) < 1$ on $q \in (0, 3/2]$ (and $0 < 1/[3]_q \le 1/3$ for all $q > 0$),
     proves exact perimeter cancellation in the Creutz ratio, bridges worldsheet plaquette area to
     `QOU.MathlibInfra.ConfinementLayerTower.configCost`, and proves the paired `_real` archimedean
     exponential area law $z_3^A = \exp(-\sigma_{\mathrm{step}} A)$ with $\sigma_{\mathrm{model}} = (-\ln z_3)/a_{\mathrm{cal}}^2 > 0$.

-- Ref: [wilson1971] https://doi.org/10.1103/PhysRevB.4.3174
-- Ref: [fulton-harris1991] Representation Theory: A First Course
-- Ref: [leitner2026] appendix-standard-model/sm-params-theta-qcd.md
-/

namespace QOU.StandardModel.StrongCPWritheCancellationAndStringTension

open scoped BigOperators
open Matrix
open QOU.StandardModel.ThetaQCDFraming (BarInvolution IsCPEven IsPurePhase ColorSectorCPEven)
open QOU.MathlibInfra.ConfinementLayerTower (ConfinementLayer natConfigToInt configCost)
open QOU.QInteger (qIntBal qIntBal_def)

-- ============================================================================
-- §1. Topological Writhe Cancellation, [1^3] Singlet Projector & ColorSectorCPEven
-- ============================================================================

section TopologicalWritheAndSinglet

/-- A signed elementary Artin crossing `(idx, pos)` representing $\sigma_{\mathrm{idx}}^{+1}$
    when `pos = true` and $\sigma_{\mathrm{idx}}^{-1}$ when `pos = false`. -/
structure BraidCrossing where
  idx : ℕ
  pos : Bool
  deriving DecidableEq, Repr

/-- Signed crossing exponent $+1$ or $-1$ of a single Artin generator. -/
def crossingSign (c : BraidCrossing) : ℤ :=
  if c.pos then 1 else -1

/-- Mirror / bar-involution on a single crossing ($\sigma_i^{\pm 1} \mapsto \sigma_i^{\mp 1}$). -/
def mirrorCrossing (c : BraidCrossing) : BraidCrossing :=
  ⟨c.idx, !c.pos⟩

@[simp]
theorem crossingSign_mirror (c : BraidCrossing) :
    crossingSign (mirrorCrossing c) = -crossingSign c := by
  rcases c with ⟨idx, pos⟩
  cases pos <;> simp [mirrorCrossing, crossingSign]

/-- Total algebraic writhe $w(\beta) = \sum_k \epsilon_k \in \mathbb{Z}$ of a braid word. -/
def writheWord (w : List BraidCrossing) : ℤ :=
  (w.map crossingSign).sum

/-- Termwise crossing-sign flip $\overline{\beta}$ (mirror image braid word). -/
def mirrorWord (w : List BraidCrossing) : List BraidCrossing :=
  w.map mirrorCrossing

@[simp]
theorem writheWord_nil : writheWord [] = 0 := rfl

@[simp]
theorem writheWord_cons (c : BraidCrossing) (w : List BraidCrossing) :
    writheWord (c :: w) = crossingSign c + writheWord w := by
  simp [writheWord]

theorem writheWord_append (w₁ w₂ : List BraidCrossing) :
    writheWord (w₁ ++ w₂) = writheWord w₁ + writheWord w₂ := by
  simp [writheWord, List.map_append, List.sum_append]

theorem writheWord_reverse (w : List BraidCrossing) :
    writheWord w.reverse = writheWord w := by
  simp [writheWord, List.map_reverse, List.sum_reverse]

/-- Mirroring flips algebraic writhe identically: $w(\overline{\beta}) = -w(\beta)$. -/
theorem writheWord_mirror (w : List BraidCrossing) :
    writheWord (mirrorWord w) = -writheWord w := by
  induction w with
  | nil => rfl
  | cons c rest ih =>
    have hcons : mirrorWord (c :: rest) = mirrorCrossing c :: mirrorWord rest := rfl
    rw [hcons, writheWord_cons, crossingSign_mirror, ih, writheWord_cons]
    ring

/-- **Mirror-Pair Writhe Cancellation**: concatenating any braid word with its mirror
    (either `w ++ mirrorWord w` or `w ++ (mirrorWord w).reverse`) yields identically zero writhe. -/
theorem writheWord_mirror_pair_eq_zero (w : List BraidCrossing) :
    writheWord (w ++ mirrorWord w) = 0 ∧
    writheWord (w ++ (mirrorWord w).reverse) = 0 := by
  constructor
  · rw [writheWord_append, writheWord_mirror, add_neg_cancel]
  · rw [writheWord_append, writheWord_reverse, writheWord_mirror, add_neg_cancel]

/-- Amphicheiral figure-eight knot braid word $\beta_{4_1} = \sigma_0 \sigma_1^{-1} \sigma_0 \sigma_1^{-1}$. -/
def figEightBraidWord : List BraidCrossing :=
  [⟨0, true⟩, ⟨1, false⟩, ⟨0, true⟩, ⟨1, false⟩]

/-- Borromean 3-component baryon link word $\beta_{\mathrm{Bor}} = (\sigma_0 \sigma_1^{-1})^3$. -/
def borromeanBraidWord : List BraidCrossing :=
  [⟨0, true⟩, ⟨1, false⟩, ⟨0, true⟩, ⟨1, false⟩, ⟨0, true⟩, ⟨1, false⟩]

/-- Positive 2-strand gluon torus knot braid word $\beta_{T(2,9)} = \sigma_0^9$. -/
def t29GluonBraidWord : List BraidCrossing :=
  List.replicate 9 ⟨0, true⟩

/-- Exact writhe audit on the substrate vacuum $4_1$, Borromean link, chiral single $T(2,9)$,
    and closed mirror-paired $T(2,9) \oplus \overline{T(2,9)}$ vacuum loop. -/
theorem substrate_and_gluon_writhe_identities :
    writheWord figEightBraidWord = 0 ∧
    writheWord borromeanBraidWord = 0 ∧
    writheWord t29GluonBraidWord = 9 ∧
    writheWord (mirrorWord t29GluonBraidWord) = -9 ∧
    writheWord (t29GluonBraidWord ++ mirrorWord t29GluonBraidWord) = 0 := by
  decide

/-- Adjacent transposition $(i, i+1) \in S_n$ induced by a valid crossing (`c.idx + 1 < n`). -/
def crossingPerm (n : ℕ) (c : BraidCrossing) : Equiv.Perm (Fin n) :=
  if h : c.idx + 1 < n then
    Equiv.swap ⟨c.idx, Nat.lt_of_succ_lt h⟩ ⟨c.idx + 1, h⟩
  else
    1

/-- Underlying strand permutation $\pi(\beta) \in S_n$ of a braid word. -/
def wordPerm (n : ℕ) : List BraidCrossing → Equiv.Perm (Fin n)
  | [] => 1
  | c :: rest => crossingPerm n c * wordPerm n rest

/-- Every in-range elementary crossing induces an odd permutation ($\mathrm{sgn} = -1 \in \mathbb{Z}^\times$),
    matching $(-1)^{\epsilon_k} = -1$ in $\mathbb{Z}^\times$ for both $\epsilon_k = \pm 1$. -/
theorem crossingPerm_sign_eq_neg_one {n : ℕ} {c : BraidCrossing} (hc : c.idx + 1 < n) :
    Equiv.Perm.sign (crossingPerm n c) = (-1 : ℤˣ) ^ (crossingSign c) := by
  unfold crossingPerm
  rw [dif_pos hc]
  have hne : (⟨c.idx, Nat.lt_of_succ_lt hc⟩ : Fin n) ≠ ⟨c.idx + 1, hc⟩ := by
    intro heq
    have hval : c.idx = c.idx + 1 := congrArg Fin.val heq
    omega
  rw [Equiv.Perm.sign_swap hne]
  rcases c with ⟨idx, pos⟩
  cases pos <;> simp [crossingSign]

/-- **Strand-Exchange Sign–Writhe Parity Theorem**: for any braid word `w` whose crossings lie in
    `Fin n`, the permutation sign $\mathrm{sgn}(\pi(w)) \in \mathbb{Z}^\times$ equals $(-1)^{w(\beta)}$
    (equivalently $\mathrm{sgn}(\pi(w)) \cdot (-1)^{w(\beta)} = 1$). -/
theorem wordPerm_sign_eq_neg_one_zpow_writhe {n : ℕ} (w : List BraidCrossing)
    (hw : ∀ c ∈ w, c.idx + 1 < n) :
    Equiv.Perm.sign (wordPerm n w) = (-1 : ℤˣ) ^ (writheWord w) ∧
    Equiv.Perm.sign (wordPerm n w) * (-1 : ℤˣ) ^ (writheWord w) = 1 := by
  induction w with
  | nil =>
    simp [wordPerm]
  | cons c rest ih =>
    have hc : c.idx + 1 < n := hw c List.mem_cons_self
    have hrest : ∀ c' ∈ rest, c'.idx + 1 < n := fun c' hm => hw c' (List.mem_cons_of_mem c hm)
    obtain ⟨ih_eq, _⟩ := ih hrest
    have hsign_mul :
        Equiv.Perm.sign (wordPerm n (c :: rest)) =
          (-1 : ℤˣ) ^ (writheWord (c :: rest)) := by
      simp only [wordPerm, map_mul, writheWord_cons]
      rw [crossingPerm_sign_eq_neg_one hc, ih_eq, ← zpow_add]
    refine ⟨hsign_mul, ?_⟩
    rw [hsign_mul, ← zpow_add, ← two_mul, zpow_mul]
    have hsq : (-1 : ℤˣ) ^ (2 : ℤ) = 1 := by decide
    rw [hsq, one_zpow]

/-- Explicit $3 \times 3 \times 3$ completely antisymmetric Levi-Civita colour-singlet tensor
    $\varepsilon_{ijk} \in \{-1, 0, +1\}$ spanning $\mathbf{1} \subset \mathbf{3}^{\otimes 3}$. -/
def leviCivita3 (i j k : Fin 3) : ℤ :=
  match i.val, j.val, k.val with
  | 0, 1, 2 => 1
  | 1, 2, 0 => 1
  | 2, 0, 1 => 1
  | 0, 2, 1 => -1
  | 2, 1, 0 => -1
  | 1, 0, 2 => -1
  | _, _, _ => 0

/-- Complete $S_3$ antisymmetry and norm-squared $\sum_{i,j,k} \varepsilon_{ijk}^2 = 6 = 3!$. -/
theorem leviCivita3_antisymm_and_norm :
    (∀ i j k : Fin 3, leviCivita3 j i k = -leviCivita3 i j k) ∧
    (∀ i j k : Fin 3, leviCivita3 i k j = -leviCivita3 i j k) ∧
    (∀ i j k : Fin 3, leviCivita3 k j i = -leviCivita3 i j k) ∧
    (∀ i j k : Fin 3, leviCivita3 j k i = leviCivita3 i j k) ∧
    (∑ i : Fin 3, ∑ j : Fin 3, ∑ k : Fin 3, (leviCivita3 i j k) ^ 2) = 6 := by
  decide

/-- Rank-1 colour-singlet $[1^3]$ projector $P_{(1^3)} = \frac{1}{6}|\varepsilon\rangle\langle\varepsilon|$
    on $V_3^{\otimes 3} \cong K^{27}$ over any `[Field K]`. -/
def singletProj3 (K : Type*) [Field K] :
    Matrix (Fin 3 × Fin 3 × Fin 3) (Fin 3 × Fin 3 × Fin 3) K :=
  Matrix.of fun ⟨i₁, j₁, k₁⟩ ⟨i₂, j₂, k₂⟩ =>
    ((leviCivita3 i₁ j₁ k₁ : K) * (leviCivita3 i₂ j₂ k₂ : K)) / 6

/-- Exact idempotency $P_{(1^3)}^2 = P_{(1^3)}$ and rank-1 trace $\mathrm{Tr}(P_{(1^3)}) = 1$
    over any `[Field K]` with `(6 : K) ≠ 0`. -/
theorem singletProj3_idempotent_and_trace_one {K : Type*} [Field K] (h6 : (6 : K) ≠ 0) :
    singletProj3 K * singletProj3 K = singletProj3 K ∧
    Matrix.trace (singletProj3 K) = 1 := by
  have h36 : (36 : K) ≠ 0 := by
    have h66 : (36 : K) = 6 * 6 := by ring
    rw [h66]
    exact mul_ne_zero h6 h6
  have hsum : (∑ x : Fin 3 × Fin 3 × Fin 3, (leviCivita3 x.1 x.2.1 x.2.2 : K) ^ 2) = 6 := by
    have hZ : (∑ x : Fin 3 × Fin 3 × Fin 3, (leviCivita3 x.1 x.2.1 x.2.2) ^ 2) = 6 := by decide
    have hK := congrArg (Int.cast : ℤ → K) hZ
    push_cast at hK
    exact hK
  constructor
  · ext x y
    simp only [Matrix.mul_apply, singletProj3, Matrix.of_apply]
    have hfactor :
        (∑ z : Fin 3 × Fin 3 × Fin 3,
          (leviCivita3 x.1 x.2.1 x.2.2 : K) * (leviCivita3 z.1 z.2.1 z.2.2 : K) / 6 *
            ((leviCivita3 z.1 z.2.1 z.2.2 : K) * (leviCivita3 y.1 y.2.1 y.2.2 : K) / 6)) =
          ((leviCivita3 x.1 x.2.1 x.2.2 : K) * (leviCivita3 y.1 y.2.1 y.2.2 : K) / 36) *
            (∑ z : Fin 3 × Fin 3 × Fin 3, (leviCivita3 z.1 z.2.1 z.2.2 : K) ^ 2) := by
      rw [Finset.mul_sum]
      refine Finset.sum_congr rfl ?_
      intro z _
      field_simp [h6, h36]
      ring
    rw [hfactor, hsum]
    field_simp [h6, h36]
    ring
  · simp only [Matrix.trace, Matrix.diag, singletProj3, Matrix.of_apply]
    have htr :
        (∑ x : Fin 3 × Fin 3 × Fin 3,
          (leviCivita3 x.1 x.2.1 x.2.2 : K) * (leviCivita3 x.1 x.2.1 x.2.2 : K) / 6) =
          (∑ x : Fin 3 × Fin 3 × Fin 3, (leviCivita3 x.1 x.2.1 x.2.2 : K) ^ 2) / 6 := by
      rw [Finset.sum_div]
      refine Finset.sum_congr rfl ?_
      intro x _
      ring
    rw [htr, hsum, div_self h6]

/-- **$\mathfrak{sl}_3(R)$ Lie-Derivation Annihilation of the $[1^3]$ Colour Singlet**:
    Over ANY commutative ring `R`, the 3-strand Lie action
    $(A \otimes I \otimes I + I \otimes A \otimes I + I \otimes I \otimes A)|\varepsilon\rangle$
    equals $(\mathrm{Tr}\,A)|\varepsilon\rangle$, and therefore vanishes identically for every
    traceless $\mathfrak{su}(3)_c$ generator ($\mathrm{Tr}\,A = 0$). -/
theorem su3_lie_deriv_leviCivita3 {R : Type*} [CommRing R]
    (A : Matrix (Fin 3) (Fin 3) R) (i j k : Fin 3) :
    (∑ a : Fin 3,
      (A i a * (leviCivita3 a j k : R) +
       A j a * (leviCivita3 i a k : R) +
       A k a * (leviCivita3 i j a : R))) =
      Matrix.trace A * (leviCivita3 i j k : R) := by
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [leviCivita3, Matrix.trace, Matrix.diag, Fin.sum_univ_three] <;>
    ring

theorem su3_lie_deriv_leviCivita3_eq_zero_of_trace_zero {R : Type*} [CommRing R]
    {A : Matrix (Fin 3) (Fin 3) R} (htr : Matrix.trace A = 0) (i j k : Fin 3) :
    (∑ a : Fin 3,
      (A i a * (leviCivita3 a j k : R) +
       A j a * (leviCivita3 i a k : R) +
       A k a * (leviCivita3 i j a : R))) = 0 := by
  rw [su3_lie_deriv_leviCivita3, htr, zero_mul]

/-- **$\mathrm{SL}_3(R)$ Group Invariance of the $[1^3]$ Colour Singlet**:
    Over ANY commutative ring `R`, $(g \otimes g \otimes g)|\varepsilon\rangle = (\det g)|\varepsilon\rangle$,
    so every special linear colour transformation ($\det g = 1$) leaves $|\varepsilon\rangle$ strictly invariant. -/
theorem sl3_action_leviCivita3 {R : Type*} [CommRing R]
    (g : Matrix (Fin 3) (Fin 3) R) (i j k : Fin 3) :
    (∑ a : Fin 3, ∑ b : Fin 3, ∑ c : Fin 3,
      g i a * g j b * g k c * (leviCivita3 a b c : R)) =
      Matrix.det g * (leviCivita3 i j k : R) := by
  have hsum6 :
      (∑ a : Fin 3, ∑ b : Fin 3, ∑ c : Fin 3,
        g i a * g j b * g k c * (leviCivita3 a b c : R)) =
        g i 0 * g j 1 * g k 2 - g i 0 * g j 2 * g k 1 +
        g i 1 * g j 2 * g k 0 - g i 1 * g j 0 * g k 2 +
        g i 2 * g j 0 * g k 1 - g i 2 * g j 1 * g k 0 := by
    simp [Fin.sum_univ_three, leviCivita3]
    ring
  rw [hsum6]
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [leviCivita3, Matrix.det_fin_three] <;>
    ring

theorem sl3_action_leviCivita3_of_det_one {R : Type*} [CommRing R]
    {g : Matrix (Fin 3) (Fin 3) R} (hdet : Matrix.det g = 1) (i j k : Fin 3) :
    (∑ a : Fin 3, ∑ b : Fin 3, ∑ c : Fin 3,
      g i a * g j b * g k c * (leviCivita3 a b c : R)) = (leviCivita3 i j k : R) := by
  rw [sl3_action_leviCivita3, hdet, one_mul]

/-- **Balanced $[1^3]$ Hecke Eigenvalue & Colour-Strand Exchange Cancellation**:
    In $H_3(q)$ ($\sigma_i^2 = (q - q^{-1})\sigma_i + 1$), the antisymmetric $[1^3]$ representation
    sends $\sigma_i \mapsto -q^{-1}$, so the $\mathrm{SL}_3$-balanced generator $\tilde{\sigma}_i = q \sigma_i$
    acts as $q \cdot (-q^{-1}) = -1$, and for every 3-strand word $w$ its eigenvalue $(-1)^{w(\beta)}$
    cancels the Levi-Civita strand-permutation sign $\mathrm{sgn}(\pi(w))$ identically (`= +1`). -/
theorem balanced_singlet_hecke_phase_eq_one {K : Type*} [Field K] {q : K} (hq : q ≠ 0)
    (w : List BraidCrossing) (hw : ∀ c ∈ w, c.idx + 1 < 3) :
    (q * (-q⁻¹)) ^ (writheWord w) * ((Equiv.Perm.sign (wordPerm 3 w) : ℤ) : K) = 1 := by
  have hqm : q * (-q⁻¹) = -1 := by
    rw [mul_neg, mul_inv_cancel₀ hq]
  rw [hqm]
  induction w with
  | nil =>
    simp [wordPerm, writheWord]
  | cons c rest ih =>
    have hc : c.idx + 1 < 3 := hw c List.mem_cons_self
    have hrest : ∀ c' ∈ rest, c'.idx + 1 < 3 := fun c' hm => hw c' (List.mem_cons_of_mem c hm)
    have hcsign : ((Equiv.Perm.sign (crossingPerm 3 c) : ℤ) : K) = -1 := by
      have h1 := crossingPerm_sign_eq_neg_one hc
      rcases c with ⟨idx, pos⟩
      cases pos <;> (simp [crossingSign] at h1; rw [h1]; norm_num)
    have hpowc : (-1 : K) ^ (crossingSign c) = -1 := by
      rcases c with ⟨idx, pos⟩
      cases pos <;> simp [crossingSign]
    simp only [wordPerm, map_mul, Units.val_mul, Int.cast_mul, writheWord_cons]
    rw [zpow_add₀ (by norm_num : (-1 : K) ≠ 0), hpowc, hcsign]
    calc (-1 : K) * (-1 : K) ^ writheWord rest * (-1 * ((Equiv.Perm.sign (wordPerm 3 rest) : ℤ) : K))
        = (-1 : K) ^ writheWord rest * ((Equiv.Perm.sign (wordPerm 3 rest) : ℤ) : K) := by ring
      _ = 1 := ih hrest

/-- Integer-exponent framing phase $q^m$ ($m \in \mathbb{Z}$) is a pure phase whenever `bar q = q⁻¹`. -/
theorem purePhase_zpow {K : Type*} [Field K] [BarInvolution K]
    {q : K} (hq : q ≠ 0) (hbarq : BarInvolution.bar q = q⁻¹) (m : ℤ) :
    IsPurePhase (q ^ m) := by
  unfold IsPurePhase
  cases m with
  | ofNat n =>
    simp only [Int.ofNat_eq_coe, zpow_natCast]
    exact QOU.StandardModel.ThetaQCDFraming.bar_qpow hbarq n
  | negSucc n =>
    simp only [zpow_negSucc, inv_inv]
    have hbar_inv : ∀ x : K, x ≠ 0 → BarInvolution.bar x⁻¹ = (BarInvolution.bar x)⁻¹ := by
      intro x hx
      have hmul : BarInvolution.bar x * BarInvolution.bar x⁻¹ = 1 := by
        rw [← BarInvolution.bar_mul, mul_inv_cancel₀ hx, BarInvolution.bar_one]
      exact (inv_eq_of_mul_eq_one_right hmul).symm
    rw [hbar_inv (q ^ (n + 1)) (pow_ne_zero _ hq),
      QOU.StandardModel.ThetaQCDFraming.bar_qpow hbarq (n + 1), inv_inv]

/-- CP-evenness criterion for signed writhe framing phases $q^m$ ($m \in \mathbb{Z}$):
    `IsCPEven (q ^ m) ↔ q ^ (2 * m) = 1`. -/
theorem cpEven_zpow_iff {K : Type*} [Field K] [BarInvolution K]
    {q : K} (hq : q ≠ 0) (hbarq : BarInvolution.bar q = q⁻¹) (m : ℤ) :
    IsCPEven (q ^ m) ↔ q ^ (2 * m) = 1 := by
  have hpure : BarInvolution.bar (q ^ m) = (q ^ m)⁻¹ := purePhase_zpow hq hbarq m
  unfold IsCPEven
  rw [hpure]
  have hqm : q ^ m ≠ 0 := zpow_ne_zero m hq
  constructor
  · intro h
    calc q ^ (2 * m) = q ^ (m + m) := by rw [two_mul]
      _ = q ^ m * q ^ m := zpow_add₀ hq m m
      _ = q ^ m * (q ^ m)⁻¹ := by rw [h]
      _ = 1 := mul_inv_cancel₀ hqm
  · intro h
    have hmul : q ^ m * q ^ m = 1 := by
      rw [← zpow_add₀ hq m m, ← two_mul]
      exact h
    exact inv_eq_of_mul_eq_one_left hmul

/-- **Constructive Discharge of `ColorSectorCPEven` on Mirror-Paired Vacuum Configurations**:
    For ANY braid word `w` (in particular `t29GluonBraidWord`, realizing $T(2,9) \oplus \overline{T(2,9)}$),
    the closed mirror-paired framing phase $q^{w(\beta \oplus \overline{\beta})} = q^0 = 1$ satisfies all
    axioms of `ColorSectorCPEven K` with `framingPhase = 1` ($\theta_{\mathrm{top}} = 0$). -/
def colorSectorCPEvenOfMirrorPair (K : Type*) [Field K] [BarInvolution K]
    (q : K) (hq : q ≠ 0) (hbarq : BarInvolution.bar q = q⁻¹)
    (w : List BraidCrossing) : ColorSectorCPEven K where
  framingPhase := q ^ (writheWord (w ++ mirrorWord w))
  framing_nonzero := zpow_ne_zero _ hq
  framing_pure := purePhase_zpow hq hbarq _
  framing_cp_even := by
    rw [(writheWord_mirror_pair_eq_zero w).1, zpow_zero]
    exact BarInvolution.bar_one

theorem colorSectorCPEvenOfMirrorPair_eq_one {K : Type*} [Field K] [BarInvolution K]
    (q : K) (hq : q ≠ 0) (hbarq : BarInvolution.bar q = q⁻¹)
    (w : List BraidCrossing) :
    (colorSectorCPEvenOfMirrorPair K q hq hbarq w).framingPhase = 1 := by
  change q ^ (writheWord (w ++ mirrorWord w)) = 1
  rw [(writheWord_mirror_pair_eq_zero w).1, zpow_zero]

/-- **Strict Exclusion of $\theta_{\mathrm{top}} = \pi$ (`Θ = -1`) at Any Ordered Real Substrate $q > 0, q \neq 1$**:
    Over any ordered field, if $q > 0$ and $q \neq 1$, then `IsCPEven (q ^ m)` holds **if and only if**
    $m = 0$, forcing $q^m = +1$ ($\theta_{\mathrm{top}} = 0$) and strictly ruling out $q^m = -1$ ($\theta = \pi$),
    while simultaneously proving that a single unpaired $T(2,9)$ tube ($m = 9$) is NOT CP-even. -/
theorem cpEven_zpow_iff_zero_and_ne_neg_one
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] [BarInvolution K]
    {q : K} (hq_pos : 0 < q) (hq_ne_one : q ≠ 1) (hbarq : BarInvolution.bar q = q⁻¹) (m : ℤ) :
    (IsCPEven (q ^ m) ↔ m = 0) ∧
    (IsCPEven (q ^ m) → q ^ m = 1 ∧ q ^ m ≠ -1) ∧
    ¬ IsCPEven (q ^ (writheWord t29GluonBraidWord)) := by
  have hq_nz : q ≠ 0 := ne_of_gt hq_pos
  have hzpow_eq_one_iff : ∀ k : ℤ, q ^ k = 1 ↔ k = 0 := by
    intro k
    constructor
    · intro hk
      cases k with
      | ofNat n =>
        rcases Nat.eq_zero_or_pos n with rfl | hn_pos
        · rfl
        · rw [Int.ofNat_eq_coe, zpow_natCast] at hk
          rcases lt_or_gt_of_ne hq_ne_one with hlt | hgt
          · exact absurd hk (ne_of_lt (pow_lt_one₀ (le_of_lt hq_pos) hlt (Nat.ne_of_gt hn_pos)))
          · exact absurd hk (ne_of_gt (one_lt_pow₀ hgt (Nat.ne_of_gt hn_pos)))
      | negSucc n =>
        rw [zpow_negSucc, inv_eq_one] at hk
        rcases lt_or_gt_of_ne hq_ne_one with hlt | hgt
        · exact absurd hk (ne_of_lt (pow_lt_one₀ (le_of_lt hq_pos) hlt (Nat.succ_ne_zero n)))
        · exact absurd hk (ne_of_gt (one_lt_pow₀ hgt (Nat.succ_ne_zero n)))
    · rintro rfl
      exact zpow_zero q
  have hiff : IsCPEven (q ^ m) ↔ m = 0 := by
    rw [cpEven_zpow_iff hq_nz hbarq m, hzpow_eq_one_iff (2 * m)]
    omega
  refine ⟨hiff, ?_, ?_⟩
  · intro hcp
    have hm0 : m = 0 := hiff.mp hcp
    subst hm0
    rw [zpow_zero]
    exact ⟨rfl, by linarith⟩
  · rw [substrate_and_gluon_writhe_identities.2.2.1, cpEven_zpow_iff hq_nz hbarq 9,
      hzpow_eq_one_iff (2 * 9)]
    omega

end TopologicalWritheAndSinglet

-- ============================================================================
-- §2. QuadI R = R[i] Nelson–Barr / Hermitian Determinant Reality & Jarlskog CP
-- ============================================================================

/-- Formal Gaussian extension $R[i] = R \oplus i R$ over any `[CommRing R]` (§7c: avoids `ℂ`/`ℝ`). -/
@[ext]
structure QuadI (R : Type*) where
  re : R
  im : R
  deriving DecidableEq

namespace QuadI

section RingDefs

variable {R : Type*} [CommRing R]

/-- Canonical real-axis embedding $R \hookrightarrow R[i]$. -/
def ofReal (x : R) : QuadI R := ⟨x, 0⟩

/-- Imaginary unit $i = (0, 1) \in R[i]$. -/
def I : QuadI R := ⟨0, 1⟩

/-- Complex conjugation $(a + b i)^* = a - b i$. -/
def conj (z : QuadI R) : QuadI R := ⟨z.re, -z.im⟩

/-- Squared modulus $|a + b i|^2 = a^2 + b^2 \in R$. -/
def normSq (z : QuadI R) : R := z.re ^ 2 + z.im ^ 2

instance : Zero (QuadI R) := ⟨⟨0, 0⟩⟩
instance : One (QuadI R) := ⟨⟨1, 0⟩⟩
instance : Add (QuadI R) := ⟨fun z w => ⟨z.re + w.re, z.im + w.im⟩⟩
instance : Neg (QuadI R) := ⟨fun z => ⟨-z.re, -z.im⟩⟩
instance : Sub (QuadI R) := ⟨fun z w => ⟨z.re - w.re, z.im - w.im⟩⟩
instance : Mul (QuadI R) := ⟨fun z w => ⟨z.re * w.re - z.im * w.im, z.re * w.im + z.im * w.re⟩⟩
instance : NatCast (QuadI R) := ⟨fun n => ⟨n, 0⟩⟩
instance : IntCast (QuadI R) := ⟨fun n => ⟨n, 0⟩⟩

@[simp] theorem zero_re : (0 : QuadI R).re = 0 := rfl
@[simp] theorem zero_im : (0 : QuadI R).im = 0 := rfl
@[simp] theorem one_re : (1 : QuadI R).re = 1 := rfl
@[simp] theorem one_im : (1 : QuadI R).im = 0 := rfl
@[simp] theorem ofReal_re (x : R) : (ofReal x).re = x := rfl
@[simp] theorem ofReal_im (x : R) : (ofReal x).im = 0 := rfl
@[simp] theorem I_re : (I : QuadI R).re = 0 := rfl
@[simp] theorem I_im : (I : QuadI R).im = 1 := rfl
@[simp] theorem add_re (z w : QuadI R) : (z + w).re = z.re + w.re := rfl
@[simp] theorem add_im (z w : QuadI R) : (z + w).im = z.im + w.im := rfl
@[simp] theorem neg_re (z : QuadI R) : (-z).re = -z.re := rfl
@[simp] theorem neg_im (z : QuadI R) : (-z).im = -z.im := rfl
@[simp] theorem sub_re (z w : QuadI R) : (z - w).re = z.re - w.re := rfl
@[simp] theorem sub_im (z w : QuadI R) : (z - w).im = z.im - w.im := rfl
@[simp] theorem mul_re (z w : QuadI R) : (z * w).re = z.re * w.re - z.im * w.im := rfl
@[simp] theorem mul_im (z w : QuadI R) : (z * w).im = z.re * w.im + z.im * w.re := rfl
@[simp] theorem natCast_re (n : ℕ) : (n : QuadI R).re = n := rfl
@[simp] theorem natCast_im (n : ℕ) : (n : QuadI R).im = 0 := rfl
@[simp] theorem intCast_re (n : ℤ) : (n : QuadI R).re = n := rfl
@[simp] theorem intCast_im (n : ℤ) : (n : QuadI R).im = 0 := rfl
@[simp] theorem conj_re (z : QuadI R) : (conj z).re = z.re := rfl
@[simp] theorem conj_im (z : QuadI R) : (conj z).im = -z.im := rfl

instance : CommRing (QuadI R) where
  add := (· + ·)
  add_assoc a b c := by ext <;> simp <;> ring
  zero := 0
  zero_add a := by ext <;> simp
  add_zero a := by ext <;> simp
  nsmul := nsmulRec
  neg := Neg.neg
  zsmul := zsmulRec
  neg_add_cancel a := by ext <;> simp
  add_comm a b := by ext <;> simp <;> ring
  sub_eq_add_neg a b := by ext <;> simp [sub_eq_add_neg]
  mul := (· * ·)
  left_distrib a b c := by ext <;> simp <;> ring
  right_distrib a b c := by ext <;> simp <;> ring
  zero_mul a := by ext <;> simp
  mul_zero a := by ext <;> simp
  mul_assoc a b c := by ext <;> simp <;> ring
  one := 1
  one_mul a := by ext <;> simp
  mul_one a := by ext <;> simp
  natCast := Nat.cast
  natCast_zero := by ext <;> simp
  natCast_succ n := by ext <;> simp
  intCast := Int.cast
  intCast_ofNat n := by ext <;> simp
  intCast_negSucc n := by
    apply QuadI.ext
    · simp [Int.negSucc_eq]
    · simp
  mul_comm a b := by ext <;> simp <;> ring

/-- Complex conjugation packaged as an involutive ring homomorphism `QuadI R →+* QuadI R`. -/
def conjHom : QuadI R →+* QuadI R where
  toFun := conj
  map_one' := by apply QuadI.ext <;> simp
  map_mul' a b := by
    apply QuadI.ext
    · simp
    · simp; ring
  map_zero' := by apply QuadI.ext <;> simp
  map_add' a b := by
    apply QuadI.ext
    · simp
    · simp [add_comm]

@[simp]
theorem conjHom_apply (z : QuadI R) : conjHom z = conj z := rfl

@[simp]
theorem conj_conj (z : QuadI R) : conj (conj z) = z := by
  apply QuadI.ext <;> simp

theorem conj_mul_self (z : QuadI R) : conj z * z = ofReal (normSq z) := by
  ext <;> simp [normSq, ofReal] <;> ring

theorem mul_conj_self (z : QuadI R) : z * conj z = ofReal (normSq z) := by
  rw [mul_comm, conj_mul_self]

theorem ofReal_mul (x y : R) : ofReal (x * y) = ofReal x * ofReal y := by
  ext <;> simp [ofReal]

end RingDefs

end QuadI

section HermitianDeterminantAndJarlskog

/-- Conjugate-transpose (Hermitian adjoint) $M^\dagger = (\overline{M})^T$ over `QuadI R`. -/
def dagger {m n R : Type*} [CommRing R] (M : Matrix m n (QuadI R)) : Matrix n m (QuadI R) :=
  (M.map QuadI.conjHom)ᵀ

@[simp]
theorem dagger_apply {m n R : Type*} [CommRing R]
    (M : Matrix m n (QuadI R)) (i : n) (j : m) :
    dagger M i j = QuadI.conj (M j i) := rfl

@[simp]
theorem dagger_dagger {m n R : Type*} [CommRing R] (M : Matrix m n (QuadI R)) :
    dagger (dagger M) = M := by
  refine Matrix.ext fun i j => ?_
  simp

theorem dagger_add {m n R : Type*} [CommRing R]
    (A B : Matrix m n (QuadI R)) :
    dagger (A + B) = dagger A + dagger B := by
  refine Matrix.ext fun i j => ?_
  simp only [dagger_apply, Matrix.add_apply, ← QuadI.conjHom_apply, map_add]

theorem dagger_sub {m n R : Type*} [CommRing R]
    (A B : Matrix m n (QuadI R)) :
    dagger (A - B) = dagger A - dagger B := by
  refine Matrix.ext fun i j => ?_
  simp only [dagger_apply, Matrix.sub_apply, ← QuadI.conjHom_apply, map_sub]

theorem dagger_neg {m n R : Type*} [CommRing R]
    (A : Matrix m n (QuadI R)) :
    dagger (-A) = -dagger A := by
  refine Matrix.ext fun i j => ?_
  simp only [dagger_apply, Matrix.neg_apply, ← QuadI.conjHom_apply, map_neg]

theorem dagger_mul {l m n R : Type*} [Fintype m] [CommRing R]
    (A : Matrix l m (QuadI R)) (B : Matrix m n (QuadI R)) :
    dagger (A * B) = dagger B * dagger A := by
  refine Matrix.ext fun i j => ?_
  have hmap : QuadI.conj (∑ k : m, A j k * B k i) =
      ∑ k : m, QuadI.conj (A j k) * QuadI.conj (B k i) := by
    simpa only [QuadI.conjHom_apply, map_mul] using
      (map_sum (QuadI.conjHom : QuadI R →+* QuadI R) (fun k : m => A j k * B k i) Finset.univ)
  simp only [dagger_apply, Matrix.mul_apply]
  rw [hmap]
  refine Finset.sum_congr rfl ?_
  intro k _
  ring

/-- Hermiticity predicate $M^\dagger = M$ over `QuadI R`. -/
def IsHermitianQuad {n R : Type*} [CommRing R] (M : Matrix n n (QuadI R)) : Prop :=
  dagger M = M

/-- Explicit real-diagonal condition `(M i i).im = 0` (automatic from `IsHermitianQuad` whenever
    `2` is regular in `R`, and stated directly so $3 \times 3$ theorems hold in **every** `CommRing R`). -/
def HasRealDiag {n R : Type*} [CommRing R] (M : Matrix n n (QuadI R)) : Prop :=
  ∀ i : n, (M i i).im = 0

theorem hasRealDiag_of_isHermitianQuad {n R : Type*} [CommRing R] [NoZeroDivisors R]
    (h2 : (2 : R) ≠ 0) {M : Matrix n n (QuadI R)} (hH : IsHermitianQuad M) :
    HasRealDiag M := by
  intro i
  have hdiag : QuadI.conj (M i i) = M i i := by
    have := congr_fun (congr_fun hH i) i
    simpa [dagger_apply] using this
  have him : -(M i i).im = (M i i).im := congrArg QuadI.im hdiag
  have htwo : (2 : R) * (M i i).im = 0 := by linear_combination -him
  exact (mul_eq_zero.mp htwo).resolve_left h2

/-- **Arbitrary-Dimension Adjoint Determinant Law**: $(\det M)^* = \det(M^\dagger)$ over any `CommRing R`. -/
theorem conj_det_eq_det_dagger {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]
    (M : Matrix n n (QuadI R)) :
    QuadI.conj (Matrix.det M) = Matrix.det (dagger M) := by
  unfold dagger
  rw [Matrix.det_transpose, ← QuadI.conjHom_apply, RingHom.map_det]
  rfl

/-- For ANY $n \times n$ Hermitian matrix $M^\dagger = M$, $\det M$ is conjugation-invariant:
    $(\det M)^* = \det M$. -/
theorem conj_det_of_isHermitianQuad {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]
    {M : Matrix n n (QuadI R)} (hH : IsHermitianQuad M) :
    QuadI.conj (Matrix.det M) = Matrix.det M := by
  rw [conj_det_eq_det_dagger, hH]

/-- **Exact $3 \times 3$ Hermitian Determinant Reality Theorem (Characteristic-Free)**:
    Over ANY commutative ring `R` (with zero division by $2$), every $3 \times 3$ Hermitian matrix
    with real diagonal has `(Matrix.det M).im = 0` identically (`Matrix.det M = ofReal (Matrix.det M).re`). -/
theorem det_hermitian3_im_eq_zero {R : Type*} [CommRing R]
    {M : Matrix (Fin 3) (Fin 3) (QuadI R)}
    (hH : IsHermitianQuad M) (hD : HasRealDiag M) :
    (Matrix.det M).im = 0 ∧ Matrix.det M = QuadI.ofReal (Matrix.det M).re := by
  have h10 : M 1 0 = QuadI.conj (M 0 1) := by
    have := congr_fun (congr_fun hH 1) 0; simpa [dagger_apply] using this.symm
  have h20 : M 2 0 = QuadI.conj (M 0 2) := by
    have := congr_fun (congr_fun hH 2) 0; simpa [dagger_apply] using this.symm
  have h21 : M 2 1 = QuadI.conj (M 1 2) := by
    have := congr_fun (congr_fun hH 2) 1; simpa [dagger_apply] using this.symm
  have hd0 : (M 0 0).im = 0 := hD 0
  have hd1 : (M 1 1).im = 0 := hD 1
  have hd2 : (M 2 2).im = 0 := hD 2
  have him : (Matrix.det M).im = 0 := by
    rw [Matrix.det_fin_three, h10, h20, h21]
    simp only [QuadI.sub_im, QuadI.add_im, QuadI.mul_re, QuadI.mul_im,
      QuadI.conj_re, QuadI.conj_im, hd0, hd1, hd2]
    ring
  refine ⟨him, ?_⟩
  ext
  · rfl
  · exact him

/-- **Tree-Level Strong-CP Mass-Determinant Cancellation (`\mathrm{Im}\det(M_u M_d) = 0`)**:
    For any $3 \times 3$ Hermitian up- and down-sector mass matrices $M_u, M_d$ over `QuadI R`
    with real diagonals, $\det(M_u M_d)$ has identically zero imaginary part — even when
    $[M_u, M_d] \neq 0$ makes the product $M_u M_d$ non-Hermitian and generates CKM CP violation. -/
theorem det_mul_hermitian3_im_eq_zero {R : Type*} [CommRing R]
    {Mu Md : Matrix (Fin 3) (Fin 3) (QuadI R)}
    (hHu : IsHermitianQuad Mu) (hDu : HasRealDiag Mu)
    (hHd : IsHermitianQuad Md) (hDd : HasRealDiag Md) :
    (Matrix.det (Mu * Md)).im = 0 ∧
    Matrix.det (Mu * Md) = QuadI.ofReal ((Matrix.det Mu).re * (Matrix.det Md).re) := by
  obtain ⟨_, hMu_eq⟩ := det_hermitian3_im_eq_zero hHu hDu
  obtain ⟨_, hMd_eq⟩ := det_hermitian3_im_eq_zero hHd hDd
  rw [Matrix.det_mul, hMu_eq, hMd_eq, ← QuadI.ofReal_mul]
  exact ⟨rfl, rfl⟩

/-- Congruence $A^\dagger \mathrm{diag}(d) A$ is automatically Hermitian and has real diagonal. -/
def gramDiag3 {R : Type*} [CommRing R]
    (A : Matrix (Fin 3) (Fin 3) (QuadI R)) (d : Fin 3 → R) :
    Matrix (Fin 3) (Fin 3) (QuadI R) :=
  dagger A * Matrix.diagonal (fun i => QuadI.ofReal (d i)) * A

theorem gramDiag3_hermitian_and_realDiag {R : Type*} [CommRing R]
    (A : Matrix (Fin 3) (Fin 3) (QuadI R)) (d : Fin 3 → R) :
    IsHermitianQuad (gramDiag3 A d) ∧ HasRealDiag (gramDiag3 A d) := by
  have hdiagH : dagger (Matrix.diagonal (fun i : Fin 3 => QuadI.ofReal (d i))) =
      Matrix.diagonal (fun i : Fin 3 => QuadI.ofReal (d i)) := by
    refine Matrix.ext fun i j => ?_
    by_cases hij : i = j
    · subst hij
      apply QuadI.ext <;> simp [QuadI.ofReal, QuadI.conj]
    · apply QuadI.ext <;>
        simp [Matrix.diagonal_apply_ne _ hij, Matrix.diagonal_apply_ne _ (Ne.symm hij), QuadI.conj]
  constructor
  · unfold IsHermitianQuad gramDiag3
    rw [dagger_mul, dagger_mul, dagger_dagger, hdiagH, Matrix.mul_assoc]
  · intro i
    fin_cases i <;>
      (simp [gramDiag3, Matrix.mul_apply, Matrix.diagonal_apply, dagger_apply,
        Fin.sum_univ_three, QuadI.ofReal, QuadI.conj]; ring)

/-- **Sylvester Positivity of $\det(M_u M_d) > 0$ (Strict Exclusion of $\arg\det(M_u M_d) = \pi$)**:
    Over ANY strict ordered commutative ring `K`, if $M_u = A_u^\dagger \mathrm{diag}(u) A_u$ and
    $M_d = A_d^\dagger \mathrm{diag}(d) A_d$ have strictly positive eigenvalues ($u_i > 0, d_i > 0$)
    and invertible mixing frames ($\det A_u \neq 0, \det A_d \neq 0$), then
    `(Matrix.det (M_u * M_d)).im = 0` AND `0 < (Matrix.det (M_u * M_d)).re` strictly! -/
theorem det_mul_gramDiag3_real_and_pos
    {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (Au Ad : Matrix (Fin 3) (Fin 3) (QuadI K)) (u d : Fin 3 → K)
    (hu : ∀ i, 0 < u i) (hd : ∀ i, 0 < d i)
    (hAu : Matrix.det Au ≠ 0) (hAd : Matrix.det Ad ≠ 0) :
    (Matrix.det (gramDiag3 Au u * gramDiag3 Ad d)).im = 0 ∧
    0 < (Matrix.det (gramDiag3 Au u * gramDiag3 Ad d)).re := by
  have hnorm_pos : ∀ z : QuadI K, z ≠ 0 → 0 < QuadI.normSq z := by
    intro z hz
    unfold QuadI.normSq
    by_cases hre : z.re = 0
    · have him : z.im ≠ 0 := by
        intro him0
        apply hz
        ext <;> simp [hre, him0]
      rw [hre]
      simp [sq_pos_of_ne_zero him]
    · exact add_pos_of_pos_of_nonneg (sq_pos_of_ne_zero hre) (sq_nonneg z.im)
  have hdet_one : ∀ (A : Matrix (Fin 3) (Fin 3) (QuadI K)) (m : Fin 3 → K),
      Matrix.det (gramDiag3 A m) =
        QuadI.ofReal (QuadI.normSq (Matrix.det A) * (m 0 * m 1 * m 2)) := by
    intro A m
    unfold gramDiag3
    rw [Matrix.det_mul, Matrix.det_mul, ← conj_det_eq_det_dagger, Matrix.det_diagonal]
    simp only [Fin.prod_univ_three]
    calc QuadI.conj (Matrix.det A) *
          (QuadI.ofReal (m 0) * QuadI.ofReal (m 1) * QuadI.ofReal (m 2)) * Matrix.det A
        = (QuadI.conj (Matrix.det A) * Matrix.det A) *
            (QuadI.ofReal (m 0) * QuadI.ofReal (m 1) * QuadI.ofReal (m 2)) := by ring
      _ = QuadI.ofReal (QuadI.normSq (Matrix.det A) * (m 0 * m 1 * m 2)) := by
          rw [QuadI.conj_mul_self, ← QuadI.ofReal_mul, ← QuadI.ofReal_mul, ← QuadI.ofReal_mul]
  rw [Matrix.det_mul, hdet_one Au u, hdet_one Ad d, ← QuadI.ofReal_mul]
  refine ⟨rfl, ?_⟩
  simp only [QuadI.ofReal_re]
  exact mul_pos
    (mul_pos (hnorm_pos _ hAu) (mul_pos (mul_pos (hu 0) (hu 1)) (hu 2)))
    (mul_pos (hnorm_pos _ hAd) (mul_pos (mul_pos (hd 0) (hd 1)) (hd 2)))

/-- Associative ring commutator $[A, B] = A B - B A$. -/
def matComm {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]
    (A B : Matrix n n R) : Matrix n n R :=
  A * B - B * A

/-- If $A, B$ are Hermitian over `QuadI R`, then $A^2$ is Hermitian, $[A, B]$ is skew-Hermitian
    ($[A, B]^\dagger = -[A, B]$), and $[A, B]^3$ is also skew-Hermitian. -/
theorem commutator_cube_skewHermitian {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]
    {A B : Matrix n n (QuadI R)} (hA : IsHermitianQuad A) (hB : IsHermitianQuad B) :
    IsHermitianQuad (A ^ 2) ∧
    dagger (matComm A B) = -matComm A B ∧
    dagger ((matComm A B) ^ 3) = -((matComm A B) ^ 3) := by
  have hAsq : IsHermitianQuad (A ^ 2) := by
    unfold IsHermitianQuad
    rw [sq, dagger_mul, hA]
  have hK : dagger (matComm A B) = -matComm A B := by
    unfold matComm
    rw [dagger_sub, dagger_mul, dagger_mul, hA, hB, neg_sub]
  refine ⟨hAsq, hK, ?_⟩
  rw [pow_three, dagger_mul, dagger_mul, hK]
  simp [Matrix.mul_assoc]

/-- Entrywise formula for the commutator of a real diagonal matrix $D = \mathrm{diag}(u)$ with $H$:
    $([D, H])_{ij} = \mathrm{ofReal}(u_i - u_j) \cdot H_{ij}$. -/
theorem matComm_diagonal_apply {n R : Type*} [Fintype n] [DecidableEq n] [CommRing R]
    (u : n → R) (H : Matrix n n (QuadI R)) (i j : n) :
    matComm (Matrix.diagonal (fun k => QuadI.ofReal (u k))) H i j =
      QuadI.ofReal (u i - u j) * H i j := by
  unfold matComm
  simp only [Matrix.sub_apply, Matrix.mul_diagonal, Matrix.diagonal_mul]
  apply QuadI.ext <;> simp [QuadI.ofReal] <;> ring

/-- **Jarlskog's Exact $3 \times 3$ Commutator–Plaquette Identity over Generic `CommRing R`**:
    For real diagonal $D = \mathrm{diag}(u_0, u_1, u_2)$ and ANY $3 \times 3$ Hermitian matrix $H$
    with real diagonal over `QuadI R`, the trace of $[D, H]^3$ has identically zero real part and
    imaginary part equal to $6 (u_0 - u_1)(u_1 - u_2)(u_2 - u_0)\,\mathrm{Im}(H_{01} H_{12} H_{20})$. -/
theorem jarlskog_commutator_cube_trace {R : Type*} [CommRing R]
    (u : Fin 3 → R) {H : Matrix (Fin 3) (Fin 3) (QuadI R)}
    (hH : IsHermitianQuad H) (_hDH : HasRealDiag H) :
    (Matrix.trace ((matComm (Matrix.diagonal (fun i => QuadI.ofReal (u i))) H) ^ 3)).re = 0 ∧
    (Matrix.trace ((matComm (Matrix.diagonal (fun i => QuadI.ofReal (u i))) H) ^ 3)).im =
      6 * (u 0 - u 1) * (u 1 - u 2) * (u 2 - u 0) * (H 0 1 * H 1 2 * H 2 0).im := by
  have h10 : H 1 0 = QuadI.conj (H 0 1) := by
    have := congr_fun (congr_fun hH 1) 0; simpa [dagger_apply] using this.symm
  have h20 : H 2 0 = QuadI.conj (H 0 2) := by
    have := congr_fun (congr_fun hH 2) 0; simpa [dagger_apply] using this.symm
  have h21 : H 2 1 = QuadI.conj (H 1 2) := by
    have := congr_fun (congr_fun hH 2) 1; simpa [dagger_apply] using this.symm
  set D : Matrix (Fin 3) (Fin 3) (QuadI R) := Matrix.diagonal (fun i => QuadI.ofReal (u i))
  have htr :
      Matrix.trace ((matComm D H) ^ 3) =
        ∑ i : Fin 3, ∑ j : Fin 3, ∑ k : Fin 3,
          (QuadI.ofReal (u i - u j) * H i j) *
          (QuadI.ofReal (u j - u k) * H j k) *
          (QuadI.ofReal (u k - u i) * H k i) := by
    rw [pow_three]
    simp only [Matrix.trace, Matrix.diag, Matrix.mul_apply, Fin.sum_univ_three]
    dsimp only [D]
    simp only [matComm_diagonal_apply]
    ring
  have h6 :
      (∑ i : Fin 3, ∑ j : Fin 3, ∑ k : Fin 3,
          (QuadI.ofReal (u i - u j) * H i j) *
          (QuadI.ofReal (u j - u k) * H j k) *
          (QuadI.ofReal (u k - u i) * H k i)) =
        QuadI.ofReal ((u 0 - u 1) * (u 1 - u 2) * (u 2 - u 0)) *
          ((H 0 1 * H 1 2 * H 2 0 - QuadI.conj (H 0 1 * H 1 2 * H 2 0)) +
           (H 0 1 * H 1 2 * H 2 0 - QuadI.conj (H 0 1 * H 1 2 * H 2 0)) +
           (H 0 1 * H 1 2 * H 2 0 - QuadI.conj (H 0 1 * H 1 2 * H 2 0))) := by
    simp only [Fin.sum_univ_three, sub_self, h10, h20, h21]
    apply QuadI.ext <;> simp [QuadI.ofReal, QuadI.conj] <;> ring
  rw [htr, h6]
  constructor
  · simp [QuadI.ofReal, QuadI.conj]
  · simp [QuadI.ofReal, QuadI.conj, h20]
    ring

/-- Explicit Hermitian $3 \times 3$ up-quark witness matrix $\mathrm{diag}(1, 2, 3)$ over `QuadI ℤ`. -/
def witnessMu : Matrix (Fin 3) (Fin 3) (QuadI ℤ) :=
  !![QuadI.ofReal 1, 0, 0;
     0, QuadI.ofReal 2, 0;
     0, 0, QuadI.ofReal 3]

/-- Explicit Hermitian positive-definite $3 \times 3$ down-quark witness matrix over `QuadI ℤ`
    carrying an irreducible off-diagonal complex braiding phase $i$ on entry $(0, 2)$. -/
def witnessMd : Matrix (Fin 3) (Fin 3) (QuadI ℤ) :=
  !![QuadI.ofReal 4, QuadI.ofReal 1, QuadI.I;
     QuadI.ofReal 1, QuadI.ofReal 4, QuadI.ofReal 1;
     -QuadI.I, QuadI.ofReal 1, QuadI.ofReal 4]

/-- **Coexistence Theorem (`\bar{\theta}_{\mathrm{tree}} = 0` WITH Non-Zero Jarlskog CP Violation)**:
    `witnessMu` and `witnessMd` are both strictly Hermitian with positive determinants
    ($\det M_u = 6 > 0$, $\det M_d = 52 > 0$, $\det(M_u M_d) = 312 > 0$, $\mathrm{Im}\det(M_u M_d) = 0$),
    YET their squared-mass Jarlskog commutator $\mathrm{Im}\,\mathrm{Tr}([M_u^2, M_d^2]^3) = -351360 \neq 0$! -/
theorem strong_cp_zero_coexists_with_jarlskog_cp :
    IsHermitianQuad witnessMu ∧
    IsHermitianQuad witnessMd ∧
    Matrix.det witnessMu = QuadI.ofReal 6 ∧
    Matrix.det witnessMd = QuadI.ofReal 52 ∧
    (Matrix.det (witnessMu * witnessMd)).im = 0 ∧
    (Matrix.det (witnessMu * witnessMd)).re = 312 ∧
    (Matrix.trace ((matComm (witnessMu ^ 2) (witnessMd ^ 2)) ^ 3)).re = 0 ∧
    (Matrix.trace ((matComm (witnessMu ^ 2) (witnessMd ^ 2)) ^ 3)).im = -351360 ∧
    (Matrix.trace ((matComm (witnessMu ^ 2) (witnessMd ^ 2)) ^ 3)).im ≠ 0 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · refine Matrix.ext fun i j => ?_
    fin_cases i <;> fin_cases j <;> decide
  · refine Matrix.ext fun i j => ?_
    fin_cases i <;> fin_cases j <;> decide
  · decide
  · decide
  · decide
  · decide
  · decide
  · decide
  · decide

/-- Any 1-loop flavour-changing self-energy $V D V^\dagger$ built from a Hermitian kernel $D$
    is automatically Hermitian (and has real diagonal when $D$ has real diagonal). -/
theorem flavorSelfEnergy_hermitian_and_realDiag {R : Type*} [CommRing R]
    (V : Matrix (Fin 3) (Fin 3) (QuadI R))
    {D : Matrix (Fin 3) (Fin 3) (QuadI R)}
    (hHD : IsHermitianQuad D) (hDD : HasRealDiag D) :
    IsHermitianQuad (V * D * dagger V) ∧ HasRealDiag (V * D * dagger V) := by
  constructor
  · unfold IsHermitianQuad
    rw [dagger_mul, dagger_mul, dagger_dagger, hHD, Matrix.mul_assoc]
  · intro i
    have h10 : D 1 0 = QuadI.conj (D 0 1) := by
      have := congr_fun (congr_fun hHD 1) 0; simpa [dagger_apply] using this.symm
    have h20 : D 2 0 = QuadI.conj (D 0 2) := by
      have := congr_fun (congr_fun hHD 2) 0; simpa [dagger_apply] using this.symm
    have h21 : D 2 1 = QuadI.conj (D 1 2) := by
      have := congr_fun (congr_fun hHD 2) 1; simpa [dagger_apply] using this.symm
    have hd0 : (D 0 0).im = 0 := hDD 0
    have hd1 : (D 1 1).im = 0 := hDD 1
    have hd2 : (D 2 2).im = 0 := hDD 2
    simp only [Matrix.mul_apply, dagger_apply, Fin.sum_univ_three, h10, h20, h21,
      QuadI.add_re, QuadI.add_im, QuadI.mul_re, QuadI.mul_im,
      QuadI.conj_re, QuadI.conj_im, hd0, hd1, hd2]
    ring

/-- **Ellis–Gaillard 1-Loop / Factorized Chiral Dressing No-Regeneration Theorem**:
    For Hermitian wave-function / self-energy factors $H_L, H_R, K_L, K_R$ and Hermitian tree mass
    matrices $M_u, M_d$ (with real diagonals), even when $[H_L, M_u] \neq 0$ makes the chiral-dressed
    mass operator $M_u^{\mathrm{eff}} = H_L M_u H_R$ **non-Hermitian**, the product determinant
    $\det(M_u^{\mathrm{eff}} M_d^{\mathrm{eff}})$ STILL has identically zero imaginary part! -/
theorem det_chiralDressed_im_eq_zero {R : Type*} [CommRing R]
    {HL Mu HR KL Md KR : Matrix (Fin 3) (Fin 3) (QuadI R)}
    (hHL : IsHermitianQuad HL) (hDHL : HasRealDiag HL)
    (hMu : IsHermitianQuad Mu) (hDMu : HasRealDiag Mu)
    (hHR : IsHermitianQuad HR) (hDHR : HasRealDiag HR)
    (hKL : IsHermitianQuad KL) (hDKL : HasRealDiag KL)
    (hMd : IsHermitianQuad Md) (hDMd : HasRealDiag Md)
    (hKR : IsHermitianQuad KR) (hDKR : HasRealDiag KR) :
    (Matrix.det ((HL * Mu * HR) * (KL * Md * KR))).im = 0 := by
  obtain ⟨_, eHL⟩ := det_hermitian3_im_eq_zero hHL hDHL
  obtain ⟨_, eMu⟩ := det_hermitian3_im_eq_zero hMu hDMu
  obtain ⟨_, eHR⟩ := det_hermitian3_im_eq_zero hHR hDHR
  obtain ⟨_, eKL⟩ := det_hermitian3_im_eq_zero hKL hDKL
  obtain ⟨_, eMd⟩ := det_hermitian3_im_eq_zero hMd hDMd
  obtain ⟨_, eKR⟩ := det_hermitian3_im_eq_zero hKR hDKR
  rw [Matrix.det_mul, Matrix.det_mul, Matrix.det_mul, Matrix.det_mul, Matrix.det_mul,
    eHL, eMu, eHR, eKL, eMd, eKR]
  simp [QuadI.ofReal]

/-- Additive decomposition of the physical strong-CP angle
    $\bar{\theta}_{\mathrm{eff}} = \theta_{\mathrm{top}} + \arg\det(M_u M_d)_{\mathrm{tree}} + \delta\bar{\theta}_{\mathrm{EW}}$. -/
def thetaBarEffective {K : Type*} [CommRing K] (thetaTop argDetTree deltaThetaEW : K) : K :=
  thetaTop + argDetTree + deltaThetaEW

/-- When tree-level topological writhe (`thetaTop = 0`) and Hermitian mass-determinant phase
    (`argDetTree = 0`) both vanish, $|\bar{\theta}_{\mathrm{eff}}|$ equals $|\delta\bar{\theta}_{\mathrm{EW}}|$
    and is bounded by any multi-loop electroweak radiative envelope $\varepsilon_{\mathrm{EW}}$. -/
theorem abs_thetaBarEffective_le_of_tree_zero
    {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    {thetaTop argDetTree deltaThetaEW epsEW : K}
    (htop : thetaTop = 0) (hdet : argDetTree = 0)
    (hew : |deltaThetaEW| ≤ epsEW) :
    |thetaBarEffective thetaTop argDetTree deltaThetaEW| ≤ epsEW := by
  unfold thetaBarEffective
  rw [htop, hdet, zero_add, zero_add]
  exact hew

/-- **HONEST OPEN HIGHER-LOOP BOUNDARY (`§3b-cond`, zero instances)**:
    While tree-level writhe cancellation ($\theta_{\mathrm{top}} = 0$), tree-level Hermitian
    determinant reality ($\arg\det(M_u M_d) = 0$), and factorized 1-loop chiral dressings
    (`det_chiralDressed_im_eq_zero`) are unconditionally proved above, non-factorizable 3-loop+
    electroweak-QCD vertex corrections and UV counterterm finiteness remain open in QOU and are
    isolated here as an explicit hypothesis class with **no global instance**. -/
class HigherLoopStrongCPFiniteHypothesis (K : Type*) [CommRing K] [LinearOrder K] [IsStrictOrderedRing K] where
  /-- Non-factorizable multi-loop electroweak radiative shift $\delta\bar{\theta}_{\mathrm{EW}}$. -/
  deltaThetaEW : K
  /-- Theoretical multi-loop radiative envelope $\varepsilon_{\mathrm{EW}} \ge 0$. -/
  epsEW : K
  epsEW_nonneg : 0 ≤ epsEW
  /-- Open UV-finiteness / Ellis–Gaillard counterterm hypothesis $|\delta\bar{\theta}_{\mathrm{EW}}| \le \varepsilon_{\mathrm{EW}}$. -/
  radiative_shift_bounded : |deltaThetaEW| ≤ epsEW

theorem thetaBarEffective_bounded_of_higherLoopHypothesis
    {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    [h : HigherLoopStrongCPFiniteHypothesis K] :
    |thetaBarEffective (0 : K) 0 h.deltaThetaEW| ≤ h.epsEW ∧ 0 ≤ h.epsEW :=
  ⟨abs_thetaBarEffective_le_of_tree_zero rfl rfl h.radiative_shift_bounded, h.epsEW_nonneg⟩

end HermitianDeterminantAndJarlskog

-- ============================================================================
-- §3. SU(3)_c Quadratic Casimir Scaling & Markov-Trace / ConfinementLayer String Tension
-- ============================================================================

section CasimirAndStringTension

/-- Elementary $3 \times 3$ matrix unit $E_{ab}$ over any commutative ring `R`. -/
def matUnit3 {R : Type*} [CommRing R] (a b : Fin 3) : Matrix (Fin 3) (Fin 3) R :=
  Matrix.of fun i j => if i = a ∧ j = b then 1 else 0

/-- **Division-Free $\mathfrak{su}(3)_c$ Fundamental Casimir Operator Identity ($6 C_2(\mathbf{3}) = 8 I_3$)**:
    Over ANY commutative ring `R`, the traceless Fierz-projected Casimir contraction
    $3 \sum_{a,b} E_{ab} E_{ba} - I_3$ equals $8 I_3$ on $R^3$ (hence $C_2(\mathbf{3}) = \frac{1}{2}(3 - \frac{1}{3}) = \frac{8}{6} = \frac{4}{3}$). -/
theorem su3_fundamental_casimir_scaled {R : Type*} [CommRing R] :
    ((3 : R) • (∑ a : Fin 3, ∑ b : Fin 3, matUnit3 a b * matUnit3 b a) -
      (1 : Matrix (Fin 3) (Fin 3) R)) =
      (8 : R) • (1 : Matrix (Fin 3) (Fin 3) R) := by
  ext i j
  simp only [Matrix.sub_apply, Matrix.smul_apply, Matrix.sum_apply, Matrix.one_apply,
    matUnit3, Matrix.mul_apply, Matrix.of_apply, smul_eq_mul]
  fin_cases i <;> fin_cases j <;> (simp [Fin.sum_univ_three]; try ring)

/-- **Exact $\mathfrak{su}(3)_c$ Fundamental Casimir Operator $C_2(\mathbf{3}) = \frac{4}{3} I_3$**
    over any `[Field K]` with `(2 : K) ≠ 0` and `(3 : K) ≠ 0`. -/
theorem su3_fundamental_casimir_matrix {K : Type*} [Field K]
    (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    ((2 : K)⁻¹ • ((∑ a : Fin 3, ∑ b : Fin 3, matUnit3 a b * matUnit3 b a) -
      (3 : K)⁻¹ • (1 : Matrix (Fin 3) (Fin 3) K))) =
      (4 / 3 : K) • (1 : Matrix (Fin 3) (Fin 3) K) := by
  ext i j
  simp only [Matrix.smul_apply, Matrix.sub_apply, Matrix.sum_apply, Matrix.one_apply,
    matUnit3, Matrix.mul_apply, Matrix.of_apply, smul_eq_mul]
  fin_cases i <;> fin_cases j <;>
    (simp [Fin.sum_univ_three]; try (field_simp [h2, h3]; ring))

/-- **Division-Free $\mathfrak{su}(3)_c$ Adjoint Casimir Operator Identity ($2 C_2(\mathbf{8}) X = 6 X - 2(\mathrm{Tr}\,X) I_3$)**:
    Over ANY commutative ring `R` and any $3 \times 3$ matrix $X$,
    $\sum_{a,b} [E_{ab}, [E_{ba}, X]] = 6 X - 2(\mathrm{Tr}\,X) I_3$. -/
theorem su3_adjoint_casimir_scaled {R : Type*} [CommRing R]
    (X : Matrix (Fin 3) (Fin 3) R) :
    (∑ a : Fin 3, ∑ b : Fin 3,
      matComm (matUnit3 a b) (matComm (matUnit3 b a) X)) =
      (6 : R) • X - (2 * Matrix.trace X) • (1 : Matrix (Fin 3) (Fin 3) R) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    (simp [matComm, matUnit3, Matrix.trace, Matrix.diag, Matrix.mul_apply,
      Fin.sum_univ_three]; ring)

/-- **Exact $\mathfrak{su}(3)_c$ Adjoint Casimir Eigenvalue $C_2(\mathbf{8}) = 3$ on Traceless Matrices**:
    Over any `[Field K]` with `(2 : K) ≠ 0`, every traceless $X \in \mathfrak{sl}_3(K)$ satisfies
    $\frac{1}{2}\sum_{a,b} [E_{ab}, [E_{ba}, X]] = 3 X$. -/
theorem su3_adjoint_casimir_matrix {K : Type*} [Field K] (h2 : (2 : K) ≠ 0)
    {X : Matrix (Fin 3) (Fin 3) K} (htr : Matrix.trace X = 0) :
    ((2 : K)⁻¹ • (∑ a : Fin 3, ∑ b : Fin 3,
      matComm (matUnit3 a b) (matComm (matUnit3 b a) X))) =
      (3 : K) • X := by
  rw [su3_adjoint_casimir_scaled, htr, mul_zero, zero_smul, sub_zero, smul_smul]
  have h62 : (2 : K)⁻¹ * 6 = 3 := by field_simp [h2]; ring
  rw [h62]

/-- General $\mathfrak{su}(3)_c$ quadratic Casimir eigenvalue $C_2(p, q) = \frac{1}{3}(p^2 + pq + q^2 + 3p + 3q)$
    for highest-weight Dynkin labels $(p, q)$. -/
def su3CasimirDynkin (K : Type*) [Field K] (p q : ℕ) : K :=
  ((p ^ 2 + p * q + q ^ 2 + 3 * p + 3 * q : ℕ) : K) / 3

/-- Exact $\mathfrak{su}(3)_c$ Casimir table, Casimir scaling ratio $C_2(\mathbf{8})/C_2(\mathbf{3}) = 9/4$,
    meson singlet-vs-octet one-gluon exchange, and the $\frac{1}{2}$ baryon Y-junction pairwise law. -/
theorem su3_casimir_scaling_and_baryon_half_law {K : Type*} [Field K]
    (h2 : (2 : K) ≠ 0) (h3 : (3 : K) ≠ 0) :
    su3CasimirDynkin K 0 0 = 0 ∧
    su3CasimirDynkin K 1 0 = 4 / 3 ∧
    su3CasimirDynkin K 0 1 = 4 / 3 ∧
    su3CasimirDynkin K 2 0 = 10 / 3 ∧
    su3CasimirDynkin K 1 1 = 3 ∧
    su3CasimirDynkin K 3 0 = 6 ∧
    su3CasimirDynkin K 1 1 / su3CasimirDynkin K 1 0 = 9 / 4 ∧
    (su3CasimirDynkin K 0 0 - su3CasimirDynkin K 1 0 - su3CasimirDynkin K 0 1) / 2 = -(4 / 3) ∧
    (su3CasimirDynkin K 1 1 - su3CasimirDynkin K 1 0 - su3CasimirDynkin K 0 1) / 2 = 1 / 6 ∧
    (su3CasimirDynkin K 0 0 - 3 * su3CasimirDynkin K 1 0) / 6 =
      (1 / 2 : K) * ((su3CasimirDynkin K 0 0 - su3CasimirDynkin K 1 0 - su3CasimirDynkin K 0 1) / 2) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by ring
    rw [this]; exact mul_ne_zero h2 h2
  have h6 : (6 : K) ≠ 0 := by
    have : (6 : K) = 2 * 3 := by ring
    rw [this]; exact mul_ne_zero h2 h3
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
    (unfold su3CasimirDynkin; push_cast; field_simp [h2, h3, h4, h6]; try ring)

/-- Rank-3 positive-crossing Markov trace step $z_3(q) = q^3 / (q^2 + 1 + q^{-2})$. -/
def markovZ3 {K : Type*} [Field K] (q : K) : K :=
  q ^ 3 / (q ^ 2 + 1 + (q ^ 2)⁻¹)

/-- Bar-symmetric rank-3 quantum-dimension reciprocal $z_3^{\mathrm{sym}}(q) = 1 / (q^2 + 1 + q^{-2})$. -/
def markovZ3Sym {K : Type*} [Field K] (q : K) : K :=
  1 / (q ^ 2 + 1 + (q ^ 2)⁻¹)

/-- Negative-crossing / bar-conjugate rank-3 Markov step $z_3^{(-)}(q) = q^{-3} / (q^2 + 1 + q^{-2})$. -/
def markovZ3Neg {K : Type*} [Field K] (q : K) : K :=
  (q ^ 3)⁻¹ / (q ^ 2 + 1 + (q ^ 2)⁻¹)

/-- Exact bridge to `QOU.QInteger.qIntBal q 3` (`[3]_q = (q^3 - q^{-3})/(q - q^{-1}) = q^2 + 1 + q^{-2}`)
    and bar-duality $z_3(q^{-1}) = z_3^{(-)}(q)$, $z_3(q) \cdot z_3^{(-)}(q) = z_3^{\mathrm{sym}}(q)^2$. -/
theorem markovZ3_eq_div_qIntBal_and_bar_duality {K : Type*} [Field K]
    {q : K} (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    qIntBal q 3 = q ^ 2 + 1 + (q ^ 2)⁻¹ ∧
    markovZ3 q = q ^ 3 / qIntBal q 3 ∧
    markovZ3 q⁻¹ = markovZ3Neg q ∧
    markovZ3 q * markovZ3Neg q = (markovZ3Sym q) ^ 2 := by
  have hsub : q - q⁻¹ ≠ 0 := by
    intro h0
    apply hq2
    have hqq : q = q⁻¹ := sub_eq_zero.mp h0
    calc q ^ 2 = q * q := sq q
      _ = q * q⁻¹ := by nth_rw 2 [hqq]
      _ = 1 := mul_inv_cancel₀ hq
  have hq3 : qIntBal q 3 = q ^ 2 + 1 + (q ^ 2)⁻¹ := by
    rw [qIntBal_def]
    rw [div_eq_iff hsub]
    field_simp [hq]
    ring
  refine ⟨hq3, by rw [markovZ3, hq3], ?_, ?_⟩
  · unfold markovZ3 markovZ3Neg
    field_simp [hq]
    try ring
  · unfold markovZ3 markovZ3Neg markovZ3Sym
    field_simp [hq]
    try ring

/-- **Strict Confinement Window $0 < z_3(q) < 1$ on $q \in (0, 3/2]$ and $0 < z_3^{\mathrm{sym}}(q) \le 1/3$**:
    Over any strict ordered field, $z_3^{\mathrm{sym}}(q) \in (0, 1/3]$ for all $q > 0$, while
    $z_3(q) = q^3/[3]_q$ satisfies $0 < z_3(q) < 1$ for every $0 < q \le 3/2$ (enclosing the
    physical QOU substrate $q_0 \approx 1.110 \in (1, 3/2)$), whereas at $q = 2$, $z_3(2) = 32/21 > 1$. -/
theorem markovZ3_confinement_bounds
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {q : K} (hq : 0 < q) :
    0 < markovZ3Sym q ∧
    markovZ3Sym q ≤ 1 / 3 ∧
    (q ≤ 3 / 2 → 0 < markovZ3 q ∧ markovZ3 q < 1) ∧
    markovZ3 (2 : K) = 32 / 21 := by
  have hq_nz : q ≠ 0 := ne_of_gt hq
  have hq2_pos : 0 < q ^ 2 := sq_pos_of_pos hq
  have hden_ge_three : 3 ≤ q ^ 2 + 1 + (q ^ 2)⁻¹ := by
    have hsq : 0 ≤ (q - q⁻¹) ^ 2 := sq_nonneg (q - q⁻¹)
    have hid : q ^ 2 + 1 + (q ^ 2)⁻¹ - 3 = (q - q⁻¹) ^ 2 := by
      field_simp [hq_nz]; ring
    linarith
  have hden_pos : 0 < q ^ 2 + 1 + (q ^ 2)⁻¹ := by linarith
  refine ⟨div_pos one_pos hden_pos, ?_, ?_, ?_⟩
  · unfold markovZ3Sym
    rw [div_le_div_iff₀ hden_pos (by norm_num : (0 : K) < 3)]
    linarith
  · intro hq_le
    have hq3_pos : 0 < q ^ 3 := pow_pos hq 3
    refine ⟨div_pos hq3_pos hden_pos, ?_⟩
    unfold markovZ3
    rw [div_lt_one hden_pos]
    suffices hpoly : q ^ 5 < q ^ 4 + q ^ 2 + 1 by
      have hmul : q ^ 3 < (q ^ 2 + 1 + (q ^ 2)⁻¹) * 1 := by
        rw [mul_one]
        have hlt_div : q ^ 5 / q ^ 2 < (q ^ 4 + q ^ 2 + 1) / q ^ 2 :=
          div_lt_div_of_pos_right hpoly hq2_pos
        have hlhs : q ^ 5 / q ^ 2 = q ^ 3 := by field_simp [hq_nz]
        have hrhs : (q ^ 4 + q ^ 2 + 1) / q ^ 2 = q ^ 2 + 1 + (q ^ 2)⁻¹ := by
          field_simp [hq_nz]
        rwa [hlhs, hrhs] at hlt_div
      linarith
    have hq2_le : q ^ 2 ≤ 9 / 4 := by nlinarith
    by_cases hq1 : q ≤ 1
    · have h54 : q ^ 5 ≤ q ^ 4 := by
        calc q ^ 5 = q ^ 4 * q := by ring
          _ ≤ q ^ 4 * 1 := mul_le_mul_of_nonneg_left hq1 (pow_nonneg (le_of_lt hq) 4)
          _ = q ^ 4 := mul_one _
      linarith
    · push_neg at hq1
      have hqm1_pos : 0 < q - 1 := sub_pos.mpr hq1
      have hqm1_le : q - 1 ≤ 1 / 2 := by linarith
      have hprod1 : q ^ 2 * (q - 1) ≤ 9 / 8 := by nlinarith
      have hinner : q ^ 2 * (q - 1) - 1 ≤ 1 / 8 := by linarith
      have hkey : q ^ 2 * (q ^ 2 * (q - 1) - 1) ≤ 9 / 32 := by
        by_cases hsign : q ^ 2 * (q - 1) - 1 ≤ 0
        · have hnonpos : q ^ 2 * (q ^ 2 * (q - 1) - 1) ≤ 0 :=
            mul_nonpos_of_nonneg_of_nonpos (le_of_lt hq2_pos) hsign
          linarith
        · push_neg at hsign
          nlinarith
      linarith [show q ^ 5 - q ^ 4 - q ^ 2 = q ^ 2 * (q ^ 2 * (q - 1) - 1) by ring]
  · unfold markovZ3
    norm_num

/-- Generic multiplicative area-law factorization and strict plaquette-by-plaquette decay:
    $z^{A_1 + A_2} = z^{A_1} z^{A_2}$ and $z^{A + 1} < z^A$ for $0 < z < 1$. -/
theorem markovAreaDecay
    {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    {z : K} (hz0 : 0 < z) (hz1 : z < 1) (A₁ A₂ : ℕ) :
    z ^ (A₁ + A₂) = z ^ A₁ * z ^ A₂ ∧ z ^ (A₁ + 1) < z ^ A₁ := by
  refine ⟨pow_add z A₁ A₂, ?_⟩
  rw [pow_succ]
  calc z ^ A₁ * z < z ^ A₁ * 1 := mul_lt_mul_of_pos_left hz1 (pow_pos hz0 A₁)
    _ = z ^ A₁ := mul_one _

/-- **Creutz Ratio Exact Perimeter-Cancellation Theorem**:
    Over ANY `[Field K]`, for a Wilson loop $W(R, T) = c_0 \cdot p_{\mathrm{perim}}^{2(R + T)} \cdot z_{\mathrm{area}}^{R \cdot T}$
    with non-zero normalization $c_0$, perimeter factor $p_{\mathrm{perim}}$, and area factor $z_{\mathrm{area}}$,
    the multiplicative Creutz ratio cancels both $c_0$ and $p_{\mathrm{perim}}$ identically, isolating $z_{\mathrm{area}}$. -/
theorem creutz_ratio_cancels_perimeter {K : Type*} [Field K]
    {c₀ pPerim zArea : K} (hc₀ : c₀ ≠ 0) (hp : pPerim ≠ 0) (hz : zArea ≠ 0) (R T : ℕ) :
    let W := fun r t : ℕ => c₀ * pPerim ^ (2 * (r + t)) * zArea ^ (r * t)
    (W (R + 1) (T + 1) * W R T) / (W (R + 1) T * W R (T + 1)) = zArea := by
  intro W
  dsimp only [W]
  have hp1 : pPerim ^ (2 * (R + 1 + T)) ≠ 0 := pow_ne_zero _ hp
  have hp2 : pPerim ^ (2 * (R + (T + 1))) ≠ 0 := pow_ne_zero _ hp
  have hz1 : zArea ^ ((R + 1) * T) ≠ 0 := pow_ne_zero _ hz
  have hz2 : zArea ^ (R * (T + 1)) ≠ 0 := pow_ne_zero _ hz
  have hnum_p :
      pPerim ^ (2 * (R + 1 + (T + 1))) * pPerim ^ (2 * (R + T)) =
        pPerim ^ (2 * (R + 1 + T)) * pPerim ^ (2 * (R + (T + 1))) := by
    rw [← pow_add, ← pow_add]
    congr 1
    omega
  have hnum_z :
      zArea ^ ((R + 1) * (T + 1)) * zArea ^ (R * T) =
        zArea ^ ((R + 1) * T) * zArea ^ (R * (T + 1)) * zArea := by
    rw [← pow_add, ← pow_add, ← pow_succ]
    congr 1
    ring
  calc (c₀ * pPerim ^ (2 * (R + 1 + (T + 1))) * zArea ^ ((R + 1) * (T + 1)) *
          (c₀ * pPerim ^ (2 * (R + T)) * zArea ^ (R * T))) /
        (c₀ * pPerim ^ (2 * (R + 1 + T)) * zArea ^ ((R + 1) * T) *
          (c₀ * pPerim ^ (2 * (R + (T + 1))) * zArea ^ (R * (T + 1))))
      = ((c₀ * c₀) * (pPerim ^ (2 * (R + 1 + (T + 1))) * pPerim ^ (2 * (R + T))) *
          (zArea ^ ((R + 1) * (T + 1)) * zArea ^ (R * T))) /
        ((c₀ * c₀) * (pPerim ^ (2 * (R + 1 + T)) * pPerim ^ (2 * (R + (T + 1)))) *
          (zArea ^ ((R + 1) * T) * zArea ^ (R * (T + 1)))) := by ring
    _ = ((c₀ * c₀) * (pPerim ^ (2 * (R + 1 + T)) * pPerim ^ (2 * (R + (T + 1)))) *
          (zArea ^ ((R + 1) * T) * zArea ^ (R * (T + 1))) * zArea) /
        ((c₀ * c₀) * (pPerim ^ (2 * (R + 1 + T)) * pPerim ^ (2 * (R + (T + 1)))) *
          (zArea ^ ((R + 1) * T) * zArea ^ (R * (T + 1)))) := by
          rw [hnum_p, hnum_z]; ring
    _ = zArea := by
          refine mul_div_cancel_left₀ zArea ?_
          exact mul_ne_zero (mul_ne_zero (mul_ne_zero hc₀ hc₀) (mul_ne_zero hp1 hp2))
            (mul_ne_zero hz1 hz2)

/-- **Bridge to `ConfinementLayerTower` (`qou-5lct`)**:
    For any Layer-0 colour-plaquette worldsheet multiplicity vector `u : Fin m → ℕ` whose column
    costs satisfy $c_j \ge \Delta_q > 0$, the `ConfinementLayerTower.configCost` is bounded below by
    $\Delta_q \cdot \mathrm{Area}(u) = \Delta_q \sum_j u_j$, strictly confining every non-empty worldsheet. -/
theorem confinementLayer_worldsheet_area_lower_bound
    {m : ℕ} {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (c : Fin m → K) {deltaQ : K} (hdelta : 0 < deltaQ) (hc : ∀ j, deltaQ ≤ c j)
    (u : Fin m → ℕ) :
    ((∑ j : Fin m, u j : ℕ) : K) * deltaQ ≤ configCost c (natConfigToInt u) ∧
    (1 ≤ ∑ j : Fin m, u j → 0 < configCost c (natConfigToInt u)) := by
  have hle : ((∑ j : Fin m, u j : ℕ) : K) * deltaQ ≤ configCost c (natConfigToInt u) := by
    unfold configCost natConfigToInt
    simp only [Int.cast_natCast]
    rw [Nat.cast_sum, Finset.sum_mul]
    refine Finset.sum_le_sum ?_
    intro j _
    exact mul_le_mul_of_nonneg_left (hc j) (Nat.cast_nonneg (u j))
  refine ⟨hle, ?_⟩
  intro hpos
  have hcast : (1 : K) ≤ ((∑ j : Fin m, u j : ℕ) : K) := by exact_mod_cast hpos
  have hprod : deltaQ ≤ ((∑ j : Fin m, u j : ℕ) : K) * deltaQ := by
    calc deltaQ = 1 * deltaQ := (one_mul deltaQ).symm
      _ ≤ ((∑ j : Fin m, u j : ℕ) : K) * deltaQ :=
          mul_le_mul_of_nonneg_right hcast (le_of_lt hdelta)
  linarith

/-- Osterwalder–Schrader / Nakayama reflection-positivity inequality on Hermitian transfer channels:
    for non-negative transfer eigenvalues $w_r \ge 0$ and real reflection-paired overlap amplitudes $c_r$,
    the Euclidean correlation $\sum_r c_r^2 w_r^T$ is non-negative for every Euclidean time extent $T \in \mathbb{N}$. -/
theorem osterwalder_schrader_transfer_positivity
    {r : ℕ} {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (c w : Fin r → K) (hw : ∀ i, 0 ≤ w i) (T : ℕ) :
    0 ≤ ∑ i : Fin r, (c i) ^ 2 * (w i) ^ T := by
  refine Finset.sum_nonneg ?_
  intro i _
  exact mul_nonneg (sq_nonneg (c i)) (pow_nonneg (hw i) T)

/-! ### §3.3 Paired Archimedean Specialisation (`_real`, `AGENTS.md §7c`) -/

/-- Generic algebraic string-tension scaling $\sigma_{\mathrm{generic}}(\hat{\sigma}, a_{\mathrm{cal}}) = \hat{\sigma} / a_{\mathrm{cal}}^2$. -/
def wilsonStringTension {K : Type*} [Field K] (sigmaHat aCal : K) : K :=
  sigmaHat / (aCal ^ 2)

/-- Archimedean Wilson string tension $\sigma_{\mathrm{model}}(z, a_{\mathrm{cal}}) = (-\ln z) / a_{\mathrm{cal}}^2$ over `ℝ`. -/
noncomputable def wilsonStringTension_real (z aCal : ℝ) : ℝ :=
  wilsonStringTension (-Real.log z) aCal

/-- **Archimedean Exponential Area-Law & Strict String-Tension Positivity (`_real` pair of `markovAreaDecay`)**:
    For any Markov step $0 < z < 1$ (in particular $z = z_3(q)$ on $q \in (0, 3/2]$) and lattice spacing
    $a_{\mathrm{cal}} \neq 0$, $z^A = \exp(-(-\ln z) \cdot A)$, $\sigma_{\mathrm{model}}(z, a_{\mathrm{cal}}) > 0$,
    and Casimir scaling relates the adjoint and fundamental tensions by $\sigma_{\mathbf{8}} = \frac{9}{4}\sigma_{\mathbf{3}}$. -/
theorem markovAreaDecay_real {z aCal : ℝ} (hz0 : 0 < z) (hz1 : z < 1) (ha : aCal ≠ 0) (A : ℕ) :
    z ^ A = Real.exp (-((-Real.log z) * (A : ℝ))) ∧
    0 < wilsonStringTension_real z aCal ∧
    wilsonStringTension ((9 / 4 : ℝ) * (-Real.log z)) aCal =
      (9 / 4 : ℝ) * wilsonStringTension_real z aCal := by
  refine ⟨?_, ?_, ?_⟩
  · have hexp : z = Real.exp (Real.log z) := (Real.exp_log hz0).symm
    conv_lhs => rw [hexp]
    rw [← Real.exp_nat_mul]
    congr 1
    ring
  · unfold wilsonStringTension_real wilsonStringTension
    have hlog_neg : Real.log z < 0 := Real.log_neg hz0 hz1
    exact div_pos (neg_pos.mpr hlog_neg) (sq_pos_of_ne_zero ha)
  · unfold wilsonStringTension_real wilsonStringTension
    ring

end CasimirAndStringTension

end QOU.StandardModel.StrongCPWritheCancellationAndStringTension
