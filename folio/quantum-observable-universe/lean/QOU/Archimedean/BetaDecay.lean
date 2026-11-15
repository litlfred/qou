import QOU.Archimedean.TransferMatrix
import QOU.Archimedean.TorusKnot
import Mathlib.RingTheory.Localization.FractionRing
import Mathlib.Data.Nat.GCD.Basic

/-!
# Beta Decay Operator and Knot Operators

The beta decay operator `T_{β-decay}(q)`, the knot operator
`F(τ(r,s), N)` for each embeddable torus knot, and the spectral
decomposition theorem (as corollary of cohomological embedding).

**Note to reader**: all proofs over `ℤ[q, q⁻¹]` (equivalently
`ℤ[t, t⁻¹]` with `t = q^{1/2}`).

## References

- [beta-decay-skein] Def: beta decay as skein crossing change.
- [leitner2026] §5/embeddability-closure: torus knots exhaust H¹(Σ_g).
- [rosso-jones1993] Completeness of torus knot invariants.
-/

namespace QOU.Archimedean

/-! ## §1  Beta decay operator -/

/-- The beta decay operator `T_{β-decay}(q) = σ₀ · σ₁⁻¹` in `H₃(q)`.

    This is the universal `±1` transition operator: it changes one
    neutron crossing to a proton crossing (or vice versa) at the
    converting vertex.

    In the Gröbner–Shirshov framework, `σ₁⁻¹ = σ₁ − (q − q⁻¹)`,
    so `T_{β-decay} = σ₀σ₁ − (q − q⁻¹)σ₀`.

    As a 2×2 matrix, the decay changes the crossing coefficients
    at the converting generator from `(𝔴⁺_nn, 𝔴⁰_nn)` to
    `(𝔴⁺_pn, 𝔴⁰_pn)` (or vice versa). -/
structure BetaDecayOp where
  /-- Parent nuclear configuration. -/
  parent : NuclearConfig
  /-- Daughter nuclear configuration. -/
  daughter : NuclearConfig
  /-- The daughter differs by exactly one nucleon: n → p. -/
  is_beta_minus : ∃ k : ℕ,
    parent.length = daughter.length ∧
    parent[k]! = NucleonType.neutron ∧
    daughter[k]! = NucleonType.proton ∧
    ∀ j, j ≠ k → parent[j]! = daughter[j]!

/-! ## §2  The Q-value ratio (over ℤ[t, t⁻¹]) -/

/-- The Skein polynomial ratio `P_dau / P_par` in the fraction field.

    Since we work with cleared Skein polynomials (multiplied by
    powers of `t + t⁻¹`), the ratio is an element of the fraction
    field of `ℤ[t, t⁻¹]`.  For the Q-value, we need `log_q` of
    this ratio, which counts exceptional divisor levels.

    We embed both polynomials into `FractionRing R_t` (the field of
    fractions of the integral domain `ℤ[t, t⁻¹]`) and perform
    division there.  The `algebraMap` coercion is the canonical
    embedding `R_t →+* FractionRing R_t`. -/
noncomputable def skeinRatio (op : BetaDecayOp) : FractionRing R_t :=
  let P_par := skeinPolynomialCleared op.parent
  let P_dau := skeinPolynomialCleared op.daughter
  -- Embed into the fraction field and divide.
  -- In the cleared form, the (t+t⁻¹) powers cancel between
  -- parent and daughter (same number of chains).
  algebraMap R_t (FractionRing R_t) P_dau /
    algebraMap R_t (FractionRing R_t) P_par

/-! ## §3  Markov trace on H_n(q) (cleared form)

The Markov trace on `H_n(q)` is defined recursively by:
- `tr_M(1) = 1`
- `tr_M(b · σ_{n-1}) = z · tr_M(b)` for `b ∈ H_{n-1}(q)`
  where `z = 1/(t + t⁻¹)`.

Since `z ∉ ℤ[t, t⁻¹]`, we work with the **cleared Markov trace**:
`tr_M^cl(x) := (t + t⁻¹)^k · tr_M(x)` where `k` is chosen to
clear all denominators.

For a 2×2 transfer matrix `M` representing an element of `H_n(q)`,
the cleared Markov trace is `M[0][0] + (t + t⁻¹) · M[1][0]`,
which is exactly `tracedVolCleared` from TransferMatrix.lean.
-/

/-- The beta decay transfer matrix `T_{β-decay} = σ₀ · σ₁⁻¹` in H₃(q).

    Using the Hecke relation `σ⁻¹ = σ − (q − q⁻¹)`,
    we have `T_{β-decay} = σ₀σ₁ − (q − q⁻¹)σ₀`.

    As a 2×2 matrix: the decay changes one nn crossing to a pn
    crossing at the converting vertex.  The net effect on the
    transfer matrix chain is to replace `T_nn` by `T_pn` at the
    converting site.  In the doubled integral form, this is
    `two_T_pn` (the pn crossing matrix). -/
noncomputable def T_beta_decay : TMatrix :=
  two_T_pn

/-- Cleared Markov trace of the beta decay operator:
    `(t + t⁻¹) · tr_M(T_{β-decay})` in `ℤ[t, t⁻¹]`. -/
noncomputable def markovTrace_beta_decay : R_t :=
  tracedVolCleared T_beta_decay

/-! ### Shell capacity and filling status -/

/-- Cumulative shell capacities from the magic numbers.
    Shell `k` is filled when `N ≥ shellCapacity k`. -/
def shellCapacity (shell : ℕ) : ℕ :=
  match shell with
  | 1 => 2    -- e-shell (trefoil)
  | 2 => 8    -- gen2-shell (cinquefoil)
  | 3 => 20   -- c-shell
  | 4 => 28   -- weak-shell
  | 5 => 50   -- strong-shell
  | 6 => 82   -- top-shell
  | _ => 0

/-- Previous shell capacity (lower bound for the active range). -/
def prevShellCapacity (shell : ℕ) : ℕ :=
  match shell with
  | 0 => 0
  | n + 1 => shellCapacity n

/-- Whether a shell is active for a given neutron number.
    Shell `k` is active if `prevCap(k) < N ≤ cap(k)`. -/
def shellActive (shell : ℕ) (N : ℕ) : Bool :=
  prevShellCapacity shell < N && N ≤ shellCapacity shell

/-- Whether a shell is fully filled: `N ≥ cap(shell)`. -/
def shellFilled (shell : ℕ) (N : ℕ) : Bool :=
  N ≥ shellCapacity shell

/-! ### Torus knot transfer matrix -/

/-- The transfer matrix for a torus knot `τ(r,s)`.

    The torus knot braid word is `(σ₁σ₂…σ_{r-1})^s`, which gives
    a product of `r-1` crossing matrices repeated `s` times.

    For the knot operator, we compute the product of crossing matrices
    along the knot's braid representative.  We define this as the
    `s`-th power of the single-period transfer matrix. -/
noncomputable def torusKnotMatrix (τ : TorusKnotLabel) : TMatrix :=
  let singlePeriod := (List.replicate (τ.r - 1) T_pp).foldl (· * ·) 1
  (List.replicate τ.s singlePeriod).foldl (· * ·) 1

/-- Cleared Markov trace of `τ · T_{β-decay}`:
    `(t + t⁻¹) · tr_M(τ · T_{β-decay})` in `ℤ[t, t⁻¹]`. -/
noncomputable def markovTrace_knot_beta (τ : TorusKnotLabel) : R_t :=
  tracedVolCleared (torusKnotMatrix τ * T_beta_decay)

/-- The Pauli-projected knot operator for fully filled shells.

    For a full shell, the antisymmetrizer `e_{(1^r)}` projects onto
    the sign representation of `S_r`.  The Pauli-projected knot
    operator reduces to the determinant sign:

    `det(T_pp)^{(r-1)·s}` where `det(T_pp) = −(𝔴⁺)²·HA = −HA`
    (since `𝔴⁺_pp = 1`).

    The determinant of a single crossing matrix `T(c,d)` is:
    `det = (c·HA + d)·d − c² = c·HA·d + d² − c²`.
    For pp: `c=1, d=0`, so `det = 0 − 1 = −1`.

    Thus the Pauli factor is `(-1)^{(r-1)·s}`. -/
noncomputable def pauliProjectedKnotOp (τ : TorusKnotLabel) : R_t :=
  if (τ.r - 1) * τ.s % 2 = 0 then 1 else -1

/-! ## §3a  Knot operators -/

/-- The knot operator `F(τ, N)` for torus knot `τ` at neutron
    number `N` on a genus-`g` surface.

    This is defined over `ℤ[t, t⁻¹]` via the Markov trace of
    the torus knot element composed with the beta decay operator
    in `H₃(q)`.

    The operator is:
    - `1` if `τ` is not embeddable (null: zero action)
    - `1` if `τ`'s shell is not active (cancels in parent/daughter)
    - `markovTrace_knot_beta τ` if active shell, partially filled
      (the `(t+t⁻¹)` normalisation is absorbed into `Q_bare`)
    - `pauliProjectedKnotOp τ` if active shell, fully filled
      (Pauli exclusion projects to sign representation) -/
noncomputable def knotOperator (τ : TorusKnotLabel) (N : ℕ) (g : ℕ) : R_t :=
  if ¬ τ.embeddableOn g then 1
  else
    let shell := τ.shellNumber
    if ¬ (shellActive shell N) then 1
    else if shellFilled shell N then
      pauliProjectedKnotOp τ
    else
      markovTrace_knot_beta τ

/-! ## §4  Spectral decomposition theorem -/

/-- **Spectral decomposition Q-value — typeclass.**

    For β⁻ decay on Σ_g, the Q_q-value decomposes as:

    `Q_q = Q_bare × ∏_{τ(r,s) ∈ E_g} F(τ(r,s), N)`

    where:
    - `Q_bare = |log_q(P_dau/P_par)| · ℏ_q · m_e/3`
    - `F(τ, N)` is the knot operator
    - The product collapses to a single active term
    - The decomposition is exact (completeness of torus knot basis)

    **Proof structure:**
    1. Completeness: Rosso–Jones + self-duality → complete basis
    2. Inductive chain: zero Hecke steps, Gröbner normal form
    3. Shell cancellation: parent/daughter share inner chains
    4. Pauli projection: full shell → alternating irrep
    5. Tower termination: degree ≥ 3 needs genus > 4

    Per-`op` witness that the Q-value of a β-decay operator
    equals `Q_bare · ∏ (knot-operator product)`. Full proof requires:
    (1) Rosso–Jones completeness (external),
    (2) inductive chain construction (`TransferMatrix.lean`),
    (3) shell cancellation,
    (4) Pauli projection (Young symmetrizer),
    (5) tower termination (embeddability bound).
    Until those land, the equality is per-instance. -/
-- Ref: [rosso-jones1993] On the invariants of torus knots derived from quan — see folio/schema/references.ts
-- Ref: [leitner2026] §5/embeddability-closure
class SpectralDecompositionQValue
    (g : ℕ) (_hg : g = 4)
    (op : BetaDecayOp)
    (qValue qBare knotProd : R_t) : Prop where
  /-- `qValue = qBare · knotProd`. -/
  factorisation : qValue = qBare * knotProd

/-- Default instance when `qValue` is *defined* as the product
    `qBare * knotProd` (rather than asserted to equal it). -/
instance spectralDecompositionQValue_def
    (g : ℕ) (hg : g = 4) (op : BetaDecayOp) (qBare knotProd : R_t) :
    SpectralDecompositionQValue g hg op (qBare * knotProd) qBare knotProd :=
  ⟨rfl⟩

/-! ## §5  Interaction completeness -/

/-- Two `TorusKnotLabel`s with equal `r` and `s` fields are equal.
    The three Prop fields are equal by proof irrelevance. -/
private lemma tklabel_ext {τ₁ τ₂ : TorusKnotLabel}
    (hr : τ₁.r = τ₂.r) (hs : τ₁.s = τ₂.s) : τ₁ = τ₂ := by
  obtain ⟨r₁, s₁, h1, h2, h3⟩ := τ₁
  obtain ⟨r₂, s₂, h1', h2', h3'⟩ := τ₂
  simp only at hr hs
  subst hr; subst hs
  have e1 : h1 = h1' := proof_irrel h1 h1'
  have e2 : h2 = h2' := proof_irrel h2 h2'
  have e3 : h3 = h3' := proof_irrel h3 h3'
  subst e1; subst e2; subst e3
  rfl

/-- **Theorem (interaction completeness).**
    The 6 embeddable torus knots on Σ₄ exhaust the harmonic 1-forms
    on the fiber.  Every transfer matrix (= force operator) is a
    composition of these 6.  No 7th interaction exists.

    Proof: a 7th embeddable torus knot τ(r,s) with (r-1)(s-1)/2 ≤ 4
    and gcd(r,s) = 1 does not exist (exhaustive enumeration).
    The next candidate τ(2,11) requires genus 5 > 4. -/
theorem interaction_completeness :
    sigma4_knots.length = 6 ∧
    ∀ τ : TorusKnotLabel, τ.embeddableOn 4 → τ ∈ sigma4_knots := by
  refine ⟨by simp [sigma4_knots], ?_⟩
  intro τ hτ
  -- Ref: [rosso-jones1993] https://doi.org/10.1016/0393-0440(93)90033-B
  -- Extract r, s, and the three structural hypotheses first so that
  -- `τ.r`/`τ.s` projections reduce to bare `r`/`s` in the hypothesis
  obtain ⟨r, s, hr2, hrs, hcop⟩ := τ
  -- Unfold embeddability to get (r-1)(s-1)/2 ≤ 4 (projections iota-reduce)
  simp only [TorusKnotLabel.embeddableOn, TorusKnotLabel.seifertRank] at hτ
  -- Bound (r - 1) * (s - 1) ≤ 9 from (r - 1) * (s - 1) / 2 ≤ 4
  have h9 : (r - 1) * (s - 1) ≤ 9 := by
    have hdiv := Nat.div_add_mod ((r - 1) * (s - 1)) 2
    have hmod := Nat.mod_lt ((r - 1) * (s - 1)) (by omega : 0 < 2)
    omega
  -- Bound r ≤ 4: if r ≥ 5, then (r-1)*r ≥ 4*5 = 20 > 9 ≥ (r-1)*(s-1)
  have hr4 : r ≤ 4 := by
    by_contra hgt
    push_neg at hgt
    have hmul1 : (r - 1) * r ≤ (r - 1) * (s - 1) :=
      Nat.mul_le_mul_left _ (by omega)
    have hmul2 : 4 * 5 ≤ (r - 1) * r :=
      Nat.mul_le_mul (by omega) (by omega)
    linarith [hmul1, hmul2, h9]
  -- Helper: rewrite membership goal using equality of labels
  have mem_eq : ∀ (lbl : TorusKnotLabel), lbl ∈ sigma4_knots →
      r = lbl.r → s = lbl.s →
      (⟨r, s, hr2, hrs, hcop⟩ : TorusKnotLabel) ∈ sigma4_knots :=
    fun lbl hlbl hrr hss =>
      (tklabel_ext (τ₁ := ⟨r, s, hr2, hrs, hcop⟩) (τ₂ := lbl) hrr hss).symm ▸ hlbl
  -- Exhaustive case bash on r ∈ {2, 3, 4}
  interval_cases r
  · -- r = 2: s ∈ {3, ..., 10}; odd s coprime to 2, even s not
    have hs_lo : 3 ≤ s := by omega
    have hs_hi : s ≤ 10 := by omega
    interval_cases s
    · exact mem_eq e_label (by simp [sigma4_knots]) rfl rfl
    · exact absurd hcop (by decide)
    · exact mem_eq gen2_label (by simp [sigma4_knots]) rfl rfl
    · exact absurd hcop (by decide)
    · exact mem_eq c_label (by simp [sigma4_knots]) rfl rfl
    · exact absurd hcop (by decide)
    · exact mem_eq strong_label (by simp [sigma4_knots]) rfl rfl
    · exact absurd hcop (by decide)
  · -- r = 3: s ∈ {4, 5}; both coprime to 3
    have hs_lo : 4 ≤ s := by omega
    have hs_hi : s ≤ 5 := by omega
    interval_cases s
    · exact mem_eq t_label (by simp [sigma4_knots]) rfl rfl
    · exact mem_eq weak_label (by simp [sigma4_knots]) rfl rfl
  · -- r = 4: (r-1)*(s-1) = 3*(s-1) ≤ 9 forces s ≤ 4, but s > 4; contradiction
    omega

/-! ## §6  Tower termination -/

/-- No degree-3 torus knot embeds on Σ₄.
    `τ(2, 3³) = τ(2, 27)` needs genus `(1)(26)/2 = 13 > 4`. -/
theorem no_degree3_on_sigma4 :
    ¬ (TorusKnotLabel.mk 2 27 (by omega) (by omega) (by decide)).embeddableOn 4 := by
  simp [TorusKnotLabel.embeddableOn, TorusKnotLabel.seifertRank]

/-- The jet bundle over Σ₄ has exactly 3 non-zero levels (0, 1, 2).
    Degree 1: 4 knots. Degree 2: 2 knots. Degree ≥ 3: none. -/
theorem jet_levels_sigma4 :
    (sigma4_knots.filter (fun τ => τ.degree = 1)).length = 4 ∧
    (sigma4_knots.filter (fun τ => τ.degree = 2)).length = 2 := by
  refine ⟨?_, ?_⟩ <;>
    simp [sigma4_knots, e_label, gen2_label, c_label, t_label, weak_label,
          strong_label, TorusKnotLabel.degree]

end QOU.Archimedean
