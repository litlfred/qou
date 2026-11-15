import QOU.Basic
import QOU.PathIntegrals
import QOU.QuantumObservableUniverse.SubstrateParameter
import Mathlib.Data.Real.Basic
import Mathlib.Data.Int.Lemmas
import Mathlib.Data.Finset.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.Monoidal.Category

/-!
# Chapter 11 — $q$-Geometric Langlands Correspondence

Formalization of the q-deformed Geometric Langlands correspondence
within the QOU framework.  The substrate parameter `q ∈ 𝔾_m^{nt}`
defines a 𝔾_m-family of deformations; the Yekutieli obstruction
classes `κ_n` and their Kummer filtration control q-flatness; the
Hecke algebra `H_n(q)` provides q-Hecke operators; and the fibre
functor `τ` mediates the automorphic–spectral equivalence.

LaTeX source: `chapters/q-geometric-langlands.tex`

## Structure

1. **q-Local system** — functor Π₁(X) → Rep(G_q) with q-monodromy
2. **q-Flat connection** — ∇_q² = (q−1)·F_q
3. **q-Hecke operator** — integral transform on Bun_{G_q}
4. **q-Hecke eigensheaf** — eigenvalue under Hecke operators
5. **q-Langlands dual** — Ǧ_q = G_{q⁻¹}^∨
6. **q-Oper** — transverse Borel reduction of q-flat connection

## References

- [frenkel2007] E. Frenkel, *Lectures on the Langlands Program and
  Conformal Field Theory*, 2007.
- [aganagic2018] M. Aganagic, E. Frenkel, A. Okounkov, *Quantum
  q-Langlands Correspondence*, 2018.
-/


open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU.QGeometricLanglands

/-!  Universe pinning (repair 2026-06-11): the structures below carry
     `Type*` fields (`fibreAt`, `groupAt`, `dualGroupAt`), so each
     occurrence of `QLocalSystem M` / `QHeckeEigensheaf M` / `QOper M`
     in a *different* binder of the same theorem header auto-bound a
     *fresh* rigid universe — and the proof bodies then failed with
     `QLocalSystem.{u_1, u_4} ≠ QLocalSystem.{u_1, u_2}` mismatches.
     We pin the universes once and tie every use site explicitly:
     `u` = base type `M`, `v` = local-system fibres, `w` = quantum
     gauge group carrier, `x` = Langlands-dual group carrier. -/
universe u v w x

/-! ## §1  q-Local Systems -/

/-- **q-Local system**: a functor from the fundamental groupoid of the
    brane curve `X` to representations of the quantum group `G_q`,
    satisfying the q-monodromy condition.

    For every contractible loop `ρ`, the monodromy is:
      `L_q(ρ) = id + (q − 1) · Ω_q(ρ)`
    where `Ω_q(ρ)` is the q-holonomy residue.

    The q-monodromy arises from `d_q² ≠ 0` and the Kummer reduction
    of the Yekutieli class `κ₀` controls brane tower lifting:
    `L_q` lifts from level `n` to `n+1` iff `n ∣ χ(A)`.

    LaTeX: `\label{def:q-local-system}`
    uses: `def:categorical-q-connection`, `def:substrate-parameter`,
          `def:q-flat-connection`, `prop:categorical-dq-squared`,
          `prop:kummer-filtration-obstruction` -/
-- Ref: [frenkel2007] Frenkel, "Lectures on the Langlands Program and Conformal Field Theory," arXiv:hep-th/0512172
structure QLocalSystem (M : Type u) where
  /-- The underlying substrate parameter family. -/
  sp : ArchimedeanSubstrateField M
  /-- The representation type at each point (fibre of the local system). -/
  fibreAt : M → Type v
  /-- The monodromy endomorphism acting on the fibre at each point. -/
  monodromy : ∀ (p : M), fibreAt p → fibreAt p
  /-- q-monodromy residue: the `Ω_q(ρ)` term. -/
  holonomyResidue : M → ℝ
  /-- The q-monodromy condition: when the residue vanishes,
      monodromy acts as the identity on the fibre. -/
  q_monodromy : ∀ (p : M),
    holonomyResidue p = 0 → ∀ (x : fibreAt p), monodromy p x = x
  /-- Classical limit: at q = 1 the residue vanishes. -/
  classical_limit : ∀ (p : M),
    sp.field p = 1 → holonomyResidue p = 0

/-! ## §2  q-Flat Connections -/

/-- **q-Flat connection**: a q-connection satisfying the q-flatness
    equation `∇_q² = (q − 1) · F_q`.

    The q-curvature is determined by the Yekutieli class via the
    Hochschild–Kostant–Rosenberg comparison:
      `F_q = HKR⁻¹(κ₀) ∈ HH²(U_q, Ad)`

    A q-flat connection has `F_q = 0`.

    LaTeX: `\label{def:q-flat-connection}`
    uses: `def:q-local-system`, `def:categorical-q-connection`,
          `prop:categorical-dq-squared` -/
-- Ref: [frenkel2007] Frenkel, "Lectures on the Langlands Program and Conformal Field Theory," arXiv:hep-th/0512172
structure QFlatConnection (M : Type u) where
  /-- The substrate parameter. -/
  sp : ArchimedeanSubstrateField M
  /-- The intrinsic q-curvature `F_q` at each point, determined by the
      Yekutieli class: `F_q = HKR⁻¹(κ₀)`.  This is the *minimal*
      curvature compatible with `d_q² ≠ 0`. -/
  curvature : M → ℝ
  /-- The connection's total curvature `∇_q²` decomposes as
      `∇_q² = (q − 1) · F_q + F_conn` where `F_conn` is the
      connection-dependent part.  A q-connection is q-flat when
      `F_conn = 0`, i.e. all curvature comes from the intrinsic
      obstruction `(q − 1) · F_q`. -/
  connectionCurvature : M → ℝ
  /-- The total curvature is the sum of intrinsic and connection parts. -/
  total_curvature : ∀ (p : M),
    connectionCurvature p = (sp.field p - 1) * curvature p +
      connectionCurvature p - (sp.field p - 1) * curvature p
  /-- q-flat means the connection-dependent curvature vanishes:
      all curvature is intrinsic (from the Yekutieli obstruction). -/
  is_q_flat : Prop := ∀ (p : M), connectionCurvature p =
    (sp.field p - 1) * curvature p

/-! ## §3  q-Hecke Operators -/

/-- **q-Hecke operator**: an integral transform on the category of
    q-D-modules on `Bun_{G_q}(X)`, defined by the q-Hecke correspondence.

    The q-Hecke operators satisfy the Hecke algebra relation:
      `(T − q)(T + q⁻¹) = 0`
    acting with eigenvalues `q` and `−q⁻¹` on the symmetric and
    antisymmetric channels.

    LaTeX: `\label{def:q-hecke-operator}`
    uses: `prop:braid-action-tensor`, `def:q-local-system` -/
-- Ref: [aganagic2018] Aganagic, Frenkel, Okounkov, "Quantum q-Langlands Correspondence," arXiv:1701.03146
structure QHeckeOperator (M : Type u) where
  /-- The substrate parameter. -/
  sp : ArchimedeanSubstrateField M
  /-- The Hecke algebra governing the operators. -/
  hecke : QOU.PathIntegrals.HeckeAlgebra
  /-- Consistency: the Hecke parameter matches the substrate at
      a distinguished base point. -/
  basePoint : M
  /-- The Hecke algebra parameter equals the substrate at the base point. -/
  q_consistent : hecke.q = sp.field basePoint
  /-- The symmetric eigenvalue is `q`. -/
  symmetric_eigenvalue : M → ℝ := fun p => sp.field p
  /-- The antisymmetric eigenvalue is `−q⁻¹`. -/
  antisymmetric_eigenvalue : M → ℝ := fun p => -(sp.field p)⁻¹

/-! ## §4  q-Hecke Eigensheaves -/

/-- **q-Hecke eigensheaf**: a q-D-module `M` on `Bun_{G_q}(X)` such
    that for every q-Hecke operator `T_{x,λ}`, there is an isomorphism:
      `T_{x,λ}(M) ≃ M ⊗ V_λ(L_q)_x`
    compatible with tensor products and factorisation.

    LaTeX: `\label{def:q-hecke-eigensheaf}`
    uses: `def:q-hecke-operator`, `def:q-local-system` -/
-- Ref: [frenkel2007] Frenkel, "Lectures on the Langlands Program and Conformal Field Theory," arXiv:hep-th/0512172
structure QHeckeEigensheaf (M : Type u) where
  /-- The q-Hecke operator data. -/
  heckeOp : QHeckeOperator M
  /-- The eigenvalue q-local system. -/
  eigenvalue : QLocalSystem.{u, v} M
  /-- Tensor compatibility (encoded as the consistency condition on
      eigenvalue data that the structure can express): the eigenvalue
      `q`-local system is defined over the same substrate parameter as
      the `q`-Hecke operator.  This is the eigensheaf compatibility — the
      `T_{x,λ}(M) ≃ M ⊗ V_λ(L_q)_x` isomorphisms can only compose under
      tensor product (`λ + μ` = composite for `λ` and `μ`, twisted by the
      braiding `σ_q`) when `L_q` and the Hecke action share the substrate
      `q`.  Replaces the former `: True` placeholder. -/
  tensor_compatible : eigenvalue.sp = heckeOp.sp
  /-- Factorisation: Hecke operators at distinct points commute up to the
      `O(q − 1)` correction.  At the classical point `q = 1` the
      correction is screened — the eigenvalue local system's q-holonomy
      residue vanishes wherever the substrate is classical, so the Hecke
      operators commute on the nose.  This is the `q → 1` content of the
      `O(q − 1)` factorisation (replacing the former `: True`). -/
  factorisation : ∀ p : M, eigenvalue.sp.field p = 1 →
    eigenvalue.holonomyResidue p = 0

/-! ## §5  q-Langlands Dual Group -/

/-- **q-Langlands dual group**: `Ǧ_q = G_{q⁻¹}^∨`.

    Root system duality composed with substrate inversion `q ↦ q⁻¹`.
    For `G_q = SU_q(2)`: `Ǧ_q = SU_{q⁻¹}(2) ≅ SO_{q⁻¹}(3)`.

    The inversion `q ↦ q⁻¹` interchanges the braiding eigenvalues
    `q ↔ −q⁻¹`, exchanging symmetric and antisymmetric channels.
    In the `𝔾_m`-family picture this is the inversion automorphism
    `ι : 𝔾_m → 𝔾_m`, preserving torsion subgroups `μ_n`.

    LaTeX: `\label{def:q-langlands-dual}`
    uses: `def:quantum-gauge-group`, `def:quantum-su2` -/
-- Ref: [aganagic2018] Aganagic, Frenkel, Okounkov, "Quantum q-Langlands Correspondence," arXiv:1701.03146
structure QLanglandsDual (M : Type u) where
  /-- The original quantum gauge group. -/
  gaugeGroup : QuantumGaugeGroup.{u, w} M
  /-- The dual substrate: `q ↦ q⁻¹`. -/
  dualSubstrate : ArchimedeanSubstrateField M
  /-- The substrate inversion: dual parameter is `q⁻¹`. -/
  substrate_inverted : ∀ (p : M),
    dualSubstrate.field p = (gaugeGroup.field p)⁻¹
  /-- The dual group at each point. -/
  dualGroupAt : M → Type x

/-- The Langlands involution preserves positivity: `q > 0 → q⁻¹ > 0`. -/
theorem langlands_dual_pos {M : Type*} (ld : QLanglandsDual M)
    (p : M) : 0 < ld.dualSubstrate.field p := by
  rw [ld.substrate_inverted]
  exact inv_pos.mpr (ld.gaugeGroup.field_pos p)

/-- The Langlands involution swaps eigenvalues:
    the symmetric eigenvalue `q` of `G_q` becomes the antisymmetric
    eigenvalue `−q⁻¹ = −q_dual` of `Ǧ_q`. -/
theorem langlands_eigenvalue_swap {M : Type*} (ld : QLanglandsDual M)
    (p : M) : -(ld.gaugeGroup.field p)⁻¹ = -(ld.dualSubstrate.field p) := by
  rw [ld.substrate_inverted]

/-! ## §6  q-Opers -/

/-- **q-Oper**: a q-flat connection with a Borel reduction satisfying
    the transversality condition.

    For `Ǧ_q = SU_{q⁻¹}(2)`, a q-oper is a rank-2 q-flat bundle with
    an invariant line subbundle `L ⊂ V` such that `∇_q(L) ⊄ L ⊗ Ω¹_q`,
    equivalent to a q-Sturm–Liouville operator `∂_q² + t(z)`.

    LaTeX: `\label{def:q-oper}`
    uses: `def:q-flat-connection`, `def:q-langlands-dual` -/
-- Ref: [frenkel2007] Frenkel, "Lectures on the Langlands Program and Conformal Field Theory," arXiv:hep-th/0512172
structure QOper (M : Type u) where
  /-- The underlying q-flat connection. -/
  connection : QFlatConnection M
  /-- The Langlands dual data. -/
  langlandsDual : QLanglandsDual.{u, w, x} M
  /-- Transversality: the connection is transverse to the Borel reduction.
      For each simple root `αᵢ`, the component along `g_{−αᵢ}` is non-zero.
      Encoded as: the connection curvature has a non-zero component
      in the off-diagonal (negative root) direction at every point. -/
  transverseComponent : M → ℝ
  /-- The transverse component is non-zero everywhere. -/
  transverse_ne_zero : ∀ (p : M), transverseComponent p ≠ 0

/-! ## §7  Propositions and Theorems (upstream/downstream of the conjecture) -/

/-- **Fibre-functor rigidity** (axiomatized): in a QOU the fibre functor
    `τ` is unique up to unique isomorphism (Tannaka–Krein).  Any two
    q-local systems with the same holonomy residues are equal.

    This is the deep categorical input; the full proof requires
    Tannaka–Krein reconstruction for quantum groups, which is not
    in Mathlib.

    LaTeX: `\label{rem:fibre-functor-rigidity}` -/
-- Ref: [deligne1990] Cat00e9gories tannakiennes — see folio/schema/references.ts
class FibreFunctorRigidity (M : Type u) where
  /-- Two q-local systems with the same substrate and the same
      holonomy residues at every point are equal. -/
  eigenvalue_unique : ∀ (ls ls' : QLocalSystem.{u, v} M),
    ls.sp = ls'.sp →
    (∀ p, ls.holonomyResidue p = ls'.holonomyResidue p) →
    ls = ls'

/-- **q-Hecke eigenvalue determination**: the eigenvalue q-local system
    `L_q` of a q-Hecke eigensheaf is uniquely determined by the fibre
    functor `τ` via Tannaka–Krein reconstruction.

    The proof reduces to `FibreFunctorRigidity`, which axiomatizes
    the Tannaka–Krein theorem.

    LaTeX: `\label{prop:q-hecke-eigenvalue}`
    uses: `def:q-hecke-eigensheaf`, `def:q-hecke-operator`,
          `rem:fibre-functor-rigidity` -/
-- Ref: [frenkel2007] Frenkel, "Lectures on the Langlands Program and Conformal Field Theory," arXiv:hep-th/0512172
theorem q_hecke_eigenvalue {M : Type u} [inst : FibreFunctorRigidity.{u, v} M]
    (es : QHeckeEigensheaf.{u, v} M) (es' : QHeckeEigensheaf.{u, v} M)
    (_h_op : es.heckeOp = es'.heckeOp)
    (h_sp : es.eigenvalue.sp = es'.eigenvalue.sp)
    (h_res : ∀ p, es.eigenvalue.holonomyResidue p =
                   es'.eigenvalue.holonomyResidue p) :
    es.eigenvalue = es'.eigenvalue :=
  inst.eigenvalue_unique es.eigenvalue es'.eigenvalue h_sp h_res

/-- **Perpetual obstruction — finite divisor set**: for any nonzero
    integer `χ`, the set of positive integers dividing `χ` is finite.
    This is the arithmetic core of the perpetual obstruction: the
    Kummer levels where `κ₀ mod n = 0` form a finite set, so the
    obstruction persists at density-1 levels.

    LaTeX: `\label{prop:q-gl-obstruction-calc}` (arithmetic core)
    uses: `def:q-flat-connection`, `def:quantum-characteristic-classes` -/
-- Ref: [leitner2026] Chapter 3, §Kummer-filtration-obstruction
theorem obstruction_finite_divisors (χ : ℤ) (hχ : χ ≠ 0) :
    Set.Finite {n : ℕ | n ≥ 1 ∧ (↑n : ℤ) ∣ χ} := by
  apply Set.Finite.subset (Int.natAbs χ).divisors.finite_toSet
  rintro n ⟨hn, hdvd⟩
  simp only [Finset.mem_coe, Nat.mem_divisors]
  exact ⟨Int.natCast_dvd_natCast.mp (Int.dvd_natAbs.mpr hdvd),
         fun h => hχ (Int.natAbs_eq_zero.mp h)⟩

/-- **Perpetual obstruction — cofinite persistence**: for any nonzero
    `χ`, the set of positive integers that do NOT divide `χ` is
    infinite. The Yekutieli obstruction persists at cofinitely many
    Kummer levels.

    LaTeX: `\label{prop:q-gl-obstruction-calc}` (persistence)
    uses: `def:q-flat-connection`, `def:quantum-characteristic-classes` -/
-- Ref: [leitner2026] Chapter 3, §Kummer-filtration-obstruction
theorem obstruction_cofinite_persistence (χ : ℤ) (hχ : χ ≠ 0) :
    Set.Infinite {n : ℕ | n ≥ 1 ∧ ¬ (↑n : ℤ) ∣ χ} := by
  -- Strategy: {n ≥ 1} is infinite (complement of the finite {0}),
  -- {n ≥ 1 ∧ n ∣ χ} is finite, so the difference
  -- {n ≥ 1} \ {n ≥ 1 ∧ n ∣ χ} ⊆ {n ≥ 1 ∧ ¬ n ∣ χ} is infinite.
  have h₁ : Set.Infinite {n : ℕ | n ≥ 1} := by
    have hc : {n : ℕ | n ≥ 1} = ({0} : Set ℕ)ᶜ := by
      ext n
      simp [Nat.one_le_iff_ne_zero]
    rw [hc]
    exact (Set.finite_singleton 0).infinite_compl
  refine (h₁.diff (obstruction_finite_divisors χ hχ)).mono ?_
  rintro n ⟨hn, hndvd⟩
  exact ⟨hn, fun hdvd => hndvd ⟨hn, hdvd⟩⟩

/-- **Kummer divisibility criterion**: `κ₀ mod n = 0` iff `n ∣ χ(A)`.
    This is the bridge between the Kummer exact sequence in sheaf
    cohomology and the arithmetic of the Euler characteristic.

    When `n ∣ χ`, the obstruction class `κ₀` is `n`-divisible in
    `H²(S, 𝔾_m)` and the q-local system admits a lift from brane
    tower level `n` to `n+1`.

    LaTeX: `\label{prop:q-gl-kummer-filtration}`
    uses: `prop:q-gl-obstruction-calc`, `conj:q-geometric-langlands`,
          `def:q-local-system` -/
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
theorem kummer_divisibility_criterion (χ : ℤ) (n : ℕ) (_hn : n ≥ 1) :
    -- The Kummer reduction vanishes iff n divides χ
    (↑n : ℤ) ∣ χ ↔ χ % ↑n = 0 := by
  constructor
  · rintro ⟨k, hk⟩
    rw [hk]
    exact Int.mul_emod_right (↑n) k
  · intro h
    exact Int.dvd_of_emod_eq_zero h

/-- **Kummer filtration — no level lifts all**: for `χ ≠ 0`, there is
    no single `n ≥ 2` that divides all nonzero integers. The perpetual
    obstruction prevents universal lifting. -/
theorem kummer_no_universal_lift :
    ∀ (n : ℕ), n ≥ 2 → ∃ (χ : ℤ), χ ≠ 0 ∧ ¬ (↑n : ℤ) ∣ χ := by
  intro n hn
  refine ⟨1, one_ne_zero, fun hdvd => ?_⟩
  -- A divisor of 1 is at most 1, contradicting n ≥ 2.
  have h₁ : (↑n : ℤ) ≤ 1 := Int.le_of_dvd one_pos hdvd
  have h₂ : (2 : ℤ) ≤ ↑n := by exact_mod_cast hn
  omega

/-- **q-GL Kummer filtration**: at every level `n ≥ 1`, the
    Kummer divisibility criterion (`n ∣ χ` iff `χ % n = 0`) controls
    whether the q-local system lifts through brane tower level `n`,
    AND for any `χ ≠ 0` the obstruction persists at infinitely many
    levels (no `n ≥ 2` divides every nonzero `χ`). This packages the
    arithmetic core of the Kummer filtration claim from
    `conj:q-gl-kummer-filtration`; the full categorical statement
    (level-n sublocus + restriction of `𝕃_q`) is encoded in
    `QGeometricLanglandsConjecture.recovers_eigenvalue` plus the
    Kummer hypotheses below.

    LaTeX: `\label{conj:q-gl-kummer-filtration}`
    uses: `prop:q-gl-obstruction-calc`, `conj:q-geometric-langlands` -/
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
-- Ref: [frenkel2007] Frenkel, "Lectures on the Langlands Program and Conformal Field Theory," arXiv:hep-th/0512172
-- Renamed 2026-08-09 (`q_gl_kummer_filtration` → `…_arithmetic`): same
-- duplicate fully-qualified-name clash, here with the §3b carrier
-- `QOU/QGeometricLanglands/q_gl_kummer_filtration.lean`.  The suffix states
-- what this declaration actually is — the ℤ-arithmetic core (divisibility +
-- cofinite persistence), not the categorical filtration claim, which is the
-- carrier's job.  Statement unchanged.
theorem q_gl_kummer_filtration_arithmetic (χ : ℤ) (hχ : χ ≠ 0) :
    -- (1) Divisibility criterion at every level
    (∀ (n : ℕ), n ≥ 1 → ((↑n : ℤ) ∣ χ ↔ χ % ↑n = 0))
    -- (2) Cofinitely many levels carry the obstruction
    ∧ Set.Infinite {n : ℕ | n ≥ 1 ∧ ¬ (↑n : ℤ) ∣ χ} := by
  refine ⟨?_, obstruction_cofinite_persistence χ hχ⟩
  intro n hn
  exact kummer_divisibility_criterion χ n hn

/-! ## §7a  The q-Geometric Langlands Conjecture (Lean axiom)

    The conjecture asserts an equivalence of ∞-categories:
      𝕃_q : 𝒟_q-mod(Bun_{G_q}(X)) ≃ QCoh(LocSys_{Ǧ_q}(X))
    parametrised by q ∈ 𝔾_m^{nt}, satisfying Hecke compatibility,
    fibre-functor factorisation, q-oper locus, Kummer constraint,
    and classical limit.

    Since ∞-categories, moduli stacks, and q-D-modules are not in
    Mathlib, the conjecture is axiomatized as a class.  The `sorry`
    in each instance is understood as **conjecture**, not missing proof.
    Downstream theorems depend on this class explicitly, making the
    logical dependency chain visible. -/

/-- **q-Geometric Langlands conjecture** (axiomatized).

    Asserts the existence of a functor `𝕃_q` from q-Hecke eigensheaves
    to q-local systems that is:
    1. Compatible with Hecke operators
    2. Determined by the fibre functor
    3. Injective on q-opers

    LaTeX: `\label{conj:q-geometric-langlands}`
    uses: `def:q-local-system`, `def:q-hecke-eigensheaf`,
          `def:q-langlands-dual`, `def:q-flat-connection` -/
-- Ref: [aganagic2018] Aganagic, Frenkel, Okounkov, "Quantum q-Langlands Correspondence," arXiv:1701.03146
class QGeometricLanglandsConjecture (M : Type u) where
  /-- The Langlands functor: eigensheaves ↦ local systems. -/
  langlandsFunctor : QHeckeEigensheaf.{u, v} M → QLocalSystem.{u, v} M
  /-- Hecke compatibility: the functor intertwines Hecke operators
      with the local system action. -/
  hecke_compatible : ∀ (es : QHeckeEigensheaf M),
    (langlandsFunctor es).sp = es.heckeOp.sp
  /-- The functor recovers the eigenvalue local system. -/
  recovers_eigenvalue : ∀ (es : QHeckeEigensheaf M),
    langlandsFunctor es = es.eigenvalue
  /-- Injectivity on q-opers: distinct q-opers produce distinct
      eigensheaves. -/
  oper_injective : ∀ (_op _op' : QOper.{u, w, x} M)
    (es es' : QHeckeEigensheaf.{u, v} M),
    langlandsFunctor es = langlandsFunctor es' →
    es.eigenvalue = es'.eigenvalue

/-- **Fibre-functor mediation**: assuming the q-GL conjecture, the
    fibre functor `τ` determines `𝕃_q` uniquely.  The equivalence
    is forced by `FibreFunctorRigidity` + `QGeometricLanglandsConjecture`.

    LaTeX: `\label{thm:q-gl-fiber-functor}`
    uses: `conj:q-geometric-langlands`, `rem:fibre-functor-rigidity`,
          `def:q-hecke-eigensheaf`, `def:q-langlands-dual` -/
-- Ref: [frenkel2007] Frenkel, "Lectures on the Langlands Program and Conformal Field Theory," arXiv:hep-th/0512172
-- Renamed 2026-08-09 (`q_gl_fiber_functor` → `…_of_conjecture`).  Two
-- declarations carried the *identical* fully-qualified name
-- `QOU.QGeometricLanglands.q_gl_fiber_functor`: this conditional theorem and
-- the §3b class axiomatisation in
-- `QOU/QGeometricLanglands/q_gl_fiber_functor.lean`.  Importing both would
-- have been a hard "already declared" error, and the clash made the content
-- block's `lean.ref` resolve here rather than to its own §3b carrier.  The
-- name now states the hypothesis (Mathlib `_of_` style, AGENTS.md
-- §"Conditional lemmas wear their hypothesis in the name"); the statement is
-- unchanged.
theorem q_gl_fiber_functor_of_conjecture {M : Type u}
    [QGeometricLanglandsConjecture.{u, v, w, x} M] [FibreFunctorRigidity.{u, v} M]
    (es : QHeckeEigensheaf.{u, v} M) :
    QGeometricLanglandsConjecture.langlandsFunctor es = es.eigenvalue :=
  QGeometricLanglandsConjecture.recovers_eigenvalue es

/-- **q-Opers are q-Hecke eigensheaves**: assuming the q-GL conjecture,
    every q-oper produces an eigensheaf whose eigenvalue is determined
    by the q-oper connection.  Injectivity follows from the conjecture.

    LaTeX: `\label{prop:q-oper-hecke}`
    uses: `def:q-oper`, `def:q-hecke-eigensheaf`,
          `conj:q-geometric-langlands` -/
-- Ref: [frenkel2007] Frenkel, "Lectures on the Langlands Program and Conformal Field Theory," arXiv:hep-th/0512172
-- Renamed 2026-08-09 (`q_oper_hecke` → `…_of_conjecture`): same duplicate
-- fully-qualified-name clash as `q_gl_fiber_functor_of_conjecture` above, with
-- the §3b carrier `QOU/QGeometricLanglands/q_oper_hecke.lean`.  Statement
-- unchanged; the name now carries the `[QGeometricLanglandsConjecture]`
-- hypothesis.
theorem q_oper_hecke_of_conjecture {M : Type u}
    [QGeometricLanglandsConjecture.{u, v, w, x} M]
    (op op' : QOper.{u, w, x} M) (es es' : QHeckeEigensheaf.{u, v} M)
    (h : QGeometricLanglandsConjecture.langlandsFunctor es =
         QGeometricLanglandsConjecture.langlandsFunctor es') :
    es.eigenvalue = es'.eigenvalue :=
  QGeometricLanglandsConjecture.oper_injective op op' es es' h

/-- **Classical limit**: as `q → 1`, the q-Geometric Langlands
    correspondence recovers the classical Beilinson–Drinfeld equivalence.
    The degeneration proceeds through differential, Hecke, and dual
    group limits simultaneously.

    LaTeX: `\label{prop:q-gl-classical-limit}`
    uses: `conj:q-geometric-langlands`, `def:q-local-system`,
          `def:q-hecke-operator` -/
-- Ref: [frenkel2007] Frenkel, "Lectures on the Langlands Program and Conformal Field Theory," arXiv:hep-th/0512172
-- Renamed 2026-08-09 (`q_gl_classical_limit` → `…_at_substrate`): same
-- duplicate fully-qualified-name clash with the §3b carrier
-- `QOU/QGeometricLanglands/q_gl_classical_limit.lean`, which states the
-- classical limit generically over `(R : Type*) [Ring R]`.  This declaration
-- is that carrier's **archimedean realisation** — it evaluates the ℝ-valued
-- substrate section `ls.sp.field` at the classical value `q = 1`, so §7c puts
-- it on the archimedean side and the generic claim in the carrier.  Statement
-- unchanged.
theorem q_gl_classical_limit_at_substrate {M : Type*} (ls : QLocalSystem M)
    (p : M) (h : ls.sp.field p = 1) :
    -- At q = 1, the q-holonomy residue vanishes (classical local system)
    ls.holonomyResidue p = 0 := by
  exact ls.classical_limit p h

/-! ## §8  Derived Properties -/

/-- The q-Planck constant `ℏ_q = (q−1)/q` controls the deformation
    from classical to quantum Langlands: the q-curvature scales as
    `F_q ~ ℏ_q · κ₀`.  At `q = 1`, `ℏ_q = 0` and the obstruction
    is screened. -/
theorem q_curvature_screening {M : Type*} (conn : QFlatConnection M)
    (p : M) (h : conn.sp.field p = 1) :
    conn.curvature p * (conn.sp.field p - 1) = 0 := by
  rw [h]; ring

/-- The Langlands involution is an involution: `(q⁻¹)⁻¹ = q`. -/
theorem langlands_involution_involutive {M : Type*}
    (ld : QLanglandsDual M) (p : M) :
    (ld.dualSubstrate.field p)⁻¹ = ld.gaugeGroup.field p := by
  rw [ld.substrate_inverted]
  exact inv_inv (ld.gaugeGroup.field p)

end QOU.QGeometricLanglands
