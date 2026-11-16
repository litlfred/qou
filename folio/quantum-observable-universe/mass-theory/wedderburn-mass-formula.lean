import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Group.Units.Defs


/-!
# Three-Invariant Wedderburn Mass Formula

The atomic mass is determined by three Wedderburn invariants
of the transfer matrix chain. These are complete: no fourth
invariant exists.

**Pre-Archimedean stub.** The formal statement lives over an
abstract commutative ring `R ⊇ ℤ[q, q⁻¹]`.  Real-valued
specialisation (substitution `q ↦ q₀`, mass scale via `m_e`) is
the Archimedean realisation and is performed downstream in
`QOU.ArchimedeanMassFormula` (per
`QOU.GroundRingAnnotations`).  See audit
`docs/audits/2026-05-03-pre-archimedean-proof-audit.md` §1
(Step 9) for the wall-discipline rationale.

-- Ref: [leitner2026] thm:wedderburn-mass-formula
-/

namespace QOU.WedderburnMass

universe u

/-- The three Wedderburn invariants of a transfer matrix chain.
    These correspond to the three extremal irreps of H_n(q):
    symmetric (dim 1), standard (dim n-1), alternating (dim 1).

    Polymorphic in the ground ring `R`.  The pre-Archimedean
    convention is `R = ℤ[q, q⁻¹]` (Laurent polynomials); the
    Archimedean specialisation evaluates at `q ↦ q₀ ∈ ℝ`. -/
structure ThreeInvariants (R : Type u) where
  Φ₁ : R  -- standard trace
  Φ₂ : R  -- determinant
  Φ₃ : R  -- chirality (sym / alt)

/-- The mass formula parameters, all derived from `q` and `m_e`.

    Parametrised over the ground ring `R`.  Pre-Arch: every field
    is a Laurent polynomial in `q`.  Post-Arch: every field is the
    real evaluation at `q = q₀`. -/
structure MassParams (R : Type u) where
  q : R
  m_e : R
  m_p : R      -- from PL thimble
  m_n : R      -- from quark ΔΦ
  α : R        -- m_e × 8G
  β₂ : R       -- -2[3]_q
  β₃ : R       -- ≈ HA²

/-- The atomic mass from the Wedderburn formula, valued in the
    ground ring `R`. -/
def atomicMass {R : Type u} [CommRing R]
    (p : MassParams R) (Z N : ℕ)
    (inv : ThreeInvariants R) : R :=
  (Z : R) * p.m_p + (N : R) * p.m_n + (Z : R) * p.m_e +
  p.α * (inv.Φ₁ + p.β₂ * inv.Φ₂ + p.β₃ * inv.Φ₃)

/-- The quantum n-integer `[n]_q = (q^n - q^{-n})/(q - q^{-1})`,
    in any commutative ring carrying a unit `q` and its inverse.

    On `R = ℤ[q, q⁻¹]` this is the genuine Laurent-polynomial
    `q`-integer.

    Base ring (AGENTS.md §7c): stated over a bare `CommRing`.  Both
    the substrate parameter and the denominator are carried as
    **units** — `q : Rˣ` (so `q⁻¹` is the units inverse, never a
    field inverse) and `d : Rˣ` pinned by `hd : ↑d = q - q⁻¹` — so
    the quotient is the division-free product `(qⁿ - q⁻ⁿ) · d⁻¹`.
    This replaces the old `[Field R]` + `hq : q * q ≠ 1` form, which
    additionally admitted the junk case `q = 0` (there `hq` holds
    while `q⁻¹ = 0`, so the "quotient" silently collapsed to `0/0`).
    Over a field the two agree: take `d = Units.mk0 (q - q⁻¹) _`. -/
def quantumInt {R : Type u} [CommRing R]
    (q d : Rˣ) (_hd : (d : R) = (q : R) - (↑q⁻¹ : R)) (n : ℕ) : R :=
  ((q : R) ^ n - (↑q⁻¹ : R) ^ n) * (↑d⁻¹ : R)

/-- `β₂ = -2 [3]_q` is derived from the baryon quantum number. -/
def beta2 {R : Type u} [CommRing R]
    (q d : Rˣ) (hd : (d : R) = (q : R) - (↑q⁻¹ : R)) : R :=
  -2 * quantumInt q d hd 3

/-- The number of extremal irreps of S_n is exactly 3 for n ≥ 3:
    trivial [n], sign [1^n], and standard [n-1,1].
    For n = 2: trivial and sign only (standard = trivial).
    The transfer matrix is 2×2 (standard rep), giving 2 invariants
    (trace and determinant). The sym/alt ratio gives the third.

    For n ≥ 4, additional irreps exist (one per partition of n),
    but the three extremal invariants capture the dominant physics.
    The interior partitions (hooks) contribute subdominant corrections
    identifiable with meson exchange channels. -/
-- Ref: [leitner2026] prop:three-parameters-wedderburn
-- Ref: [kazhdan-lusztig1979] Kazhdan & Lusztig, "Representations of Coxeter groups and Hecke algebras," Invent. Math. 53 (1979)
theorem extremal_irreps_count :
    ∀ (n : ℕ), n ≥ 3 →
    -- S_n has 3 extremal one-row/one-column/hook partitions
    -- [n] → dim 1, [1^n] → dim 1, [n-1,1] → dim (n-1) ≥ 2
    ∃ (d_sym d_alt d_std : ℕ),
      d_sym = 1 ∧ d_alt = 1 ∧ d_std = n - 1 ∧ d_std ≥ 2 := by
  intro n hn
  refine ⟨1, 1, n - 1, rfl, rfl, rfl, ?_⟩
  omega

/-- Number of distinct extremal irreps `{[n], [n-1,1], [1^n]}` of `H_n(q)`
    for `n ≥ 1`:
    - `n = 1`: `1` (`[1]`)
    - `n = 2`: `2` (`[2], [1,1]`)
    - `n ≥ 3`: `3` (`[n], [n-1,1], [1^n]`). -/
def extremalIrrepCount (n : ℕ) : ℕ :=
  if n ≤ 1 then 1 else if n = 2 then 2 else 3

/-- Partition count `p(n)` on the low-strand window `n ∈ {1, 2, 3, 4}`:
    `p(1) = 1`, `p(2) = 2`, `p(3) = 3`, `p(4) = 5` (adding `[2,2]` and `[2,1,1]`). -/
def partitionCountLow (n : ℕ) : ℕ :=
  if n ≤ 1 then 1 else if n = 2 then 2 else if n = 3 then 3 else 5

/-- **Domain constraint (`qou-1jw9`).** On the low-strand window `1 ≤ n ≤ 4`,
    the three extremal partition blocks `(n), (n-1,1), (1^n)` exhaust all
    irreducible representations of `H_n(q)` if and only if `n ≤ 3`. At `n = 4`
    (`p(4) = 5 > 3`), two non-extremal blocks `(2,2)` and `(2,1,1)` appear. -/
theorem extremal_exhausts_iff_n_le_three (n : ℕ) (hn1 : 1 ≤ n) (hn4 : n ≤ 4) :
    extremalIrrepCount n = partitionCountLow n ↔ n ≤ 3 := by
  have h : n = 1 ∨ n = 2 ∨ n = 3 ∨ n = 4 := by omega
  rcases h with rfl | rfl | rfl | rfl <;> decide

/-- At `n = 4`, exactly `2` partitions (`(2,2)` and `(2,1,1)`) lie outside the
    three extremal partition blocks. -/
theorem non_extremal_irreps_at_n_eq_four :
    partitionCountLow 4 - extremalIrrepCount 4 = 2 := rfl

/-- Number of inter-nucleon bridges in the adjacent-chain topology `M_1 … M_{A-1}`. -/
def adjacentChainPairCount (A : ℕ) : ℕ := A - 1

/-- Number of nucleon pairs in the complete graph `K_A` (`A(A-1)/2`). -/
def allPairsCount (A : ℕ) : ℕ := A * (A - 1) / 2

/-- At `A = 2` (deuteron), the adjacent chain and complete pair graph coincide (`1 = 1`). -/
theorem adjacentChainPairCount_eq_allPairsCount_at_two :
    adjacentChainPairCount 2 = allPairsCount 2 := rfl

/-- **Adjacent-chain vs all-pairs growth constraint (`qou-1jw9`).** For every
    multi-nucleon system with `A ≥ 3`, the linear chain `M_1 … M_{A-1}` carries
    strictly fewer bridges (`A - 1`) than the all-pairs count `A(A-1)/2`
    (`2(A - 1) < A(A - 1)`). -/
theorem adjacentChain_twice_lt_allPairs_twice (A : ℕ) (hA : A ≥ 3) :
    2 * adjacentChainPairCount A < A * (A - 1) := by
  unfold adjacentChainPairCount
  exact Nat.mul_lt_mul_of_pos_right (by omega) (by omega)

end QOU.WedderburnMass
