import QOU.BraidKnot.wedderburn_trace_identity
import QOU.BraidKnot.KeystoneVerlindeSMatrixBridge
import QOU.QBeta.QBesselContiguityRecurrence

/-!
# Keystone s013 — the q-Bessel radial-part target (machine-checked obligation)

The keystone residual-(i) reduced to the single open field `bwS0 λ = d_q(λ)/D`
(`KeystoneVerlindeSMatrixBridge.BWVacuumRowIsHecke`).  The modular-category identification
(audit `2026-06-22-keystone-modular-category-identification.md`) settled the arena as the
NON-compact `SU_q(2) → E_q(2)` contraction (Hahn–Exton q-Bessel at real `q₀ > 1`), and the
q-Bessel precheck (audit `2026-06-20-keystone-qbessel-heat-kernel-lead.md`) located the open
object as the **radial-part identity**: is the second-kind q-Bessel radial weight, at the
partition points, the vacuum row `d_q/D`?  The value-map screen
(`computations/probes/keystone_valuemap_screen_s013.py`, merged #3197) sharpened *what* the
weight must return at the four `n = 5` conjugation classes.  This file makes both machine-checked:

1. **The four shape identities** (sorry-free, generic field — §7c): the n = 5 q-hook-length
   dimensions are `d_q(5) = [1]`, `d_q(4,1) = [4]`, `d_q(3,2) = [5]`, and — the sole genuine
   product, the discriminating self-conjugate block — `d_q(3,1,1) = [4][3]/[2]`.  Stated
   multiplicatively (`shape_*`), so no nonzero hypotheses are needed; the division form is the
   corollary `dq_311_div`.
2. **The obligation class** `QBesselRadialPartRealization` — the OPEN conjecture carrier
   (bean `s013`; NO instance is provided, per the §3b-tax honest-open-state convention): a
   partition → q-Bessel-lattice assignment plus a radial weight family constrained to the
   corpus-formalized **Jackson second-kind q-Bessel contiguity**
   (`QOU.QBeta.qbessel_second_kind_coeff_closed_form`'s hypothesis), transpose-equivariant,
   whose values at the partition points ARE the vacuum row `S0`.  The recurrence constraint is
   what makes the carrier content-bearing: a solution family is a SINGLE coefficient orbit
   (`realization_on_orbit`), so all `S0` values must lie on one q-Bessel orbit — a strong,
   falsifiable demand, not an arbitrary table.
3. **The discriminating test** (`realization_discriminating_block`): any realization forces the
   weight at the self-conjugate block's lattice point to satisfy
   `w · D · [2]_q = [4]_q · [3]_q` — the machine-checked form of the scope note's kill-test
   (`docs/scope/2026-07-01-s013-qbessel-radial-part-target.md`): a candidate lattice map that
   fits the three single-q-integer blocks but misses `[4][3]/[2]` at `(3,1,1)` is wrong.

The open construction — the actual `latticePt` map — is the owner-gated DG object (#2503).
Nothing here asserts it exists; this file pins exactly what it must satisfy.  Base ring: generic
`[Field R]` throughout (no archimedean construct).  No fit.

-- Ref: [koelink1994] https://doi.org/10.1215/S0012-7094-94-07617-0 — Hahn–Exton q-Bessel =
--      E_q(2) matrix coefficients, the second-order q-difference equation.
-- Ref: [koelink-swarttouw-1994] https://doi.org/10.1006/jmaa.1994.1330 — q-Hankel
--      orthogonality (the radial-part measure this obligation targets).
-/

namespace QOU.BraidKnot.Keystone

open scoped BigOperators
open QOU.BraidKnot (qIntGeo qFactorial)
open QOU.QBeta (qbesselSecondKindRatio qbessel_second_kind_coeff_closed_form)

variable {R : Type*} [Field R]

/-! ## The n = 5 shape identities (sorry-free) -/

/-- `[1]_q = 1`. -/
theorem qIntGeo_one (q : R) : qIntGeo q 1 = 1 := by
  simp [qIntGeo]

/-- `[5]_q! = [1][2][3][4][5]` — the q-factorial expanded. -/
theorem qFactorial_five (q : R) :
    qFactorial q 5
      = qIntGeo q 1 * qIntGeo q 2 * qIntGeo q 3 * qIntGeo q 4 * qIntGeo q 5 := by
  simp [qFactorial, Finset.prod_range_succ]

/-- Hook-length product of `λ = (5)`: hooks `{5,4,3,2,1}`. -/
def hookProdRow5 (q : R) : R :=
  qIntGeo q 5 * qIntGeo q 4 * qIntGeo q 3 * qIntGeo q 2 * qIntGeo q 1

/-- Hook-length product of `λ = (4,1)`: hooks `{5,3,2,1,1}`. -/
def hookProd41 (q : R) : R :=
  qIntGeo q 5 * qIntGeo q 3 * qIntGeo q 2 * qIntGeo q 1 * qIntGeo q 1

/-- Hook-length product of `λ = (3,2)`: hooks `{4,3,2,1,1}`. -/
def hookProd32 (q : R) : R :=
  qIntGeo q 4 * qIntGeo q 3 * qIntGeo q 2 * qIntGeo q 1 * qIntGeo q 1

/-- Hook-length product of the self-conjugate `λ = (3,1,1)`: hooks `{5,2,2,1,1}`. -/
def hookProd311 (q : R) : R :=
  qIntGeo q 5 * qIntGeo q 2 * qIntGeo q 2 * qIntGeo q 1 * qIntGeo q 1

/-- **`d_q(5) = [1]_q = 1`** (multiplicative form): `[5]_q! = ∏ hooks(5)`. -/
theorem shape_row5 (q : R) : qFactorial q 5 = hookProdRow5 q := by
  rw [qFactorial_five]
  rw [hookProdRow5]
  ring_nf

/-- **`d_q(4,1) = [4]_q`** (multiplicative form): `[5]_q! = [4]_q · ∏ hooks(4,1)`.
The standard-representation family `d_q(n−1,1) = [n−1]_q` at `n = 5`. -/
theorem shape_41 (q : R) : qFactorial q 5 = qIntGeo q 4 * hookProd41 q := by
  rw [qFactorial_five]
  rw [hookProd41, qIntGeo_one]
  ring

/-- **`d_q(3,2) = [5]_q`** (multiplicative form): `[5]_q! = [5]_q · ∏ hooks(3,2)`.
The muon block. -/
theorem shape_32 (q : R) : qFactorial q 5 = qIntGeo q 5 * hookProd32 q := by
  rw [qFactorial_five]
  rw [hookProd32, qIntGeo_one]
  ring

/-- **`d_q(3,1,1) = [4]_q[3]_q/[2]_q`** (multiplicative form):
`[5]_q! · [2]_q = [4]_q · [3]_q · ∏ hooks(3,1,1)`.  The electron block — the sole
self-conjugate class at `n = 5` and the only `d_q` that is NOT a single balanced
q-integer.  The realization difficulty is concentrated here (value-map screen #3197). -/
theorem shape_311 (q : R) :
    qFactorial q 5 * qIntGeo q 2 = qIntGeo q 4 * qIntGeo q 3 * hookProd311 q := by
  rw [qFactorial_five]
  rw [hookProd311, qIntGeo_one]
  ring

/-- The division form of the trivial row partition `λ = (5)`:
`d_q(5) = [5]_q! / ∏ hooks(5) = 1`. -/
theorem dq_row5_div (q : R) (hrow5 : hookProdRow5 q ≠ 0) :
    qFactorial q 5 / hookProdRow5 q = 1 := by
  rw [shape_row5 q]
  exact div_self hrow5

/-- The division form of the standard representation `λ = (4,1)`:
`d_q(4,1) = [5]_q! / ∏ hooks(4,1) = [4]_q`. -/
theorem dq_41_div (q : R) (h41 : hookProd41 q ≠ 0) :
    qFactorial q 5 / hookProd41 q = qIntGeo q 4 := by
  rw [shape_41 q]
  exact mul_div_cancel_right₀ (qIntGeo q 4) h41

/-- The division form of the two-row block `λ = (3,2)`:
`d_q(3,2) = [5]_q! / ∏ hooks(3,2) = [5]_q`. -/
theorem dq_32_div (q : R) (h32 : hookProd32 q ≠ 0) :
    qFactorial q 5 / hookProd32 q = qIntGeo q 5 := by
  rw [shape_32 q]
  exact mul_div_cancel_right₀ (qIntGeo q 5) h32

/-- The division form of the discriminating block:
`d_q(3,1,1) = [5]_q!/∏hooks = [4]_q[3]_q/[2]_q`. -/
theorem dq_311_div (q : R) (h2 : qIntGeo q 2 ≠ 0) (h311 : hookProd311 q ≠ 0) :
    qFactorial q 5 / hookProd311 q = qIntGeo q 4 * qIntGeo q 3 / qIntGeo q 2 := by
  rw [div_eq_div_iff h311 h2]
  exact shape_311 q

/-! ## The obligation class (OPEN — bean s013; no instance) -/

/-- **Conjecture carrier (OPEN — the s013 / precheck step-(a) obligation): the q-Bessel
radial-part realization of the keystone vacuum row.**  A realization supplies:

* `latticePt` — the partition → q-Bessel-lattice assignment.  **This map is the open
  geometric construction** (the owner-gated DG object, #2503); it is NOT established
  anywhere in the corpus, and this class does not assert it exists.
* `weight` — the radial weight family, **constrained** to the corpus-formalized Jackson
  second-kind q-Bessel contiguity (the hypothesis of
  `QOU.QBeta.qbessel_second_kind_coeff_closed_form`).  This constraint is the content:
  a solution family is a single coefficient orbit, so all vacuum-row values must lie on
  ONE q-Bessel orbit (`realization_on_orbit`) — falsifiable, not an arbitrary table.
* `latticePt_conj` — transpose-equivariance, the `W_λ = W_{λ′}` hallmark the measure must
  respect (precheck P2).
* `realizes` — the weight at each partition's lattice point IS the vacuum row `S0`.

No instance is provided: the open state is the honest state (§3b-tax).  The discriminating
numerical test a candidate must pass is `realization_discriminating_block` below. -/
class QBesselRadialPartRealization (q a : R) (h : VerlindeModularData R) where
  /-- Partition → q-Bessel-lattice point (the open DG construction). -/
  latticePt : h.Part → ℕ
  /-- The radial weight family (second-kind radial part). -/
  weight : ℕ → R
  /-- `weight` solves the Jackson second-kind q-Bessel contiguity — the corpus-formalized
  constraint (`QBesselContiguityRecurrence`) making this carrier content-bearing. -/
  weight_qbessel : ∀ k,
    weight (k + 1) * ((1 - q ^ (k + 1)) * (1 - a * q ^ (k + 1)))
      = -(a * q ^ (2 * k + 1)) * weight k
  /-- Transpose-equivariance: `λ` and `λ′` share a lattice point (precheck P2). -/
  latticePt_conj : ∀ p ∈ h.parts, latticePt (h.conj p) = latticePt p
  /-- **The realization**: the radial weight at the partition point is the vacuum row. -/
  realizes : ∀ p ∈ h.parts, weight (latticePt p) = h.S0 p

/-- **Any realization puts the whole vacuum row on a single q-Bessel coefficient orbit**:
`S0 p = weight 0 · ∏_{j < latticePt p} r_j` with `r_j` the second-kind contiguity ratio.
This is the falsifiable content of the obligation — the `S0` values are not free, they are
one orbit of the corpus's q-Bessel recurrence. -/
theorem realization_on_orbit (q a : R) (h : VerlindeModularData R)
    [r : QBesselRadialPartRealization q a h]
    (hD : ∀ k, (1 - q ^ (k + 1)) * (1 - a * q ^ (k + 1)) ≠ 0)
    (p : h.Part) (hp : p ∈ h.parts) :
    h.S0 p
      = r.weight 0
        * ∏ j ∈ Finset.range (r.latticePt p), qbesselSecondKindRatio q a j := by
  rw [← r.realizes p hp]
  exact qbessel_second_kind_coeff_closed_form q a r.weight hD r.weight_qbessel _

/-- **The discriminating test (machine-checked form of the s013 scope-note kill-test).**
For any block whose q-dimension has the self-conjugate `(3,1,1)` shape
`d_q · [2]_q = [4]_q · [3]_q` (proved for the actual hook data in `shape_311`), a
realization forces the radial weight at its lattice point to satisfy
`w · D · [2]_q = [4]_q · [3]_q`.  A candidate `latticePt` that fits the three
single-q-integer blocks but misses this product at the self-conjugate block is wrong. -/
theorem realization_discriminating_block (q a : R) (h : VerlindeModularData R)
    [r : QBesselRadialPartRealization q a h]
    (p : h.Part) (hp : p ∈ h.parts)
    (hdim : h.qDim p * qIntGeo q 2 = qIntGeo q 4 * qIntGeo q 3) :
    r.weight (r.latticePt p) * h.D * qIntGeo q 2 = qIntGeo q 4 * qIntGeo q 3 := by
  rw [r.realizes p hp, h.S0_eq p hp, div_mul_cancel₀ _ h.D_ne, hdim]

/-- Transpose-invariance of the radial weight under any `QBesselRadialPartRealization`:
    since `λ` and `λ′` share a lattice point, their radial weights coincide. -/
theorem realization_weight_conj (q a : R) (h : VerlindeModularData R)
    [r : QBesselRadialPartRealization q a h]
    (p : h.Part) (hp : p ∈ h.parts) :
    r.weight (r.latticePt (h.conj p)) = r.weight (r.latticePt p) := by
  rw [r.latticePt_conj p hp]

/-- Any `QBesselRadialPartRealization` forces the vacuum row `S0` to be invariant
    under partition conjugation `p ↦ h.conj p`. -/
theorem realization_S0_conj (q a : R) (h : VerlindeModularData R)
    [r : QBesselRadialPartRealization q a h]
    (p : h.Part) (hp : p ∈ h.parts) (hcp : h.conj p ∈ h.parts) :
    h.S0 (h.conj p) = h.S0 p := by
  rw [← r.realizes (h.conj p) hcp, ← r.realizes p hp, r.latticePt_conj p hp]

end QOU.BraidKnot.Keystone
