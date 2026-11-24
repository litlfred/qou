import Mathlib.Tactic

/-!
# Traced-Volume Product vs. Strand-Tracked Positive Half-Twist (`qou-jwl8`)

Bean `qou-jwl8` (`computations/probes/traced_volume_and_delta_models_audit_probe.py`,
`computations/probes/np_splitting/np_h3_genuine_word_probe.py`,
`computations/probes/np_splitting/np_product_vs_braid_blast_radius_probe.py`).

`HeckeRational.traced_volume` and `markov_trace(ordering) = ∏ᵢ V̂ᵢ` evaluate the
Ocneanu Markov trace of the generator-indexed product

    P_A = ∏_{i=0}^{A-2} ∏_{j=i+1}^{A-1} (σ_{i+1} + d_{ij}),

which places every pair `(i, j)` (`j > i`) on generator `σ_{i+1}`, rather than
the strand-tracked positive half-twist `Δ_A` in which each pair of strands
crosses once on the Artin generator where those two strands actually meet.

This module proves the exact universal algebraic obstructions separating `P_A`
and `Δ_A` (§7c generic over `[CommRing R]`, specialized to `[Field K]` and
`[LinearOrderedField K]`, with zero empirical constants):

1. **Three-strand exact trace difference (`trTracedVolumeA3_sub_trHalfTwistA3`):**
   For arbitrary pair shifts `(a, b, c) = (d_{01}, d_{02}, d_{12})` in any
   commutative ring `R`, Hecke parameter `h`, and Markov parameter `z`,
   - `P_3(a,b,c) = (σ_1 + a)(σ_1 + b)(σ_2 + c)` peels `σ_2` to give
     `tr_M(P_3) = ((a + b + h)z + 1 + ab)(z + c)`;
   - `Δ_3(a,b,c) = (σ_1 + a)(σ_2 + b)(σ_1 + c)` peels `σ_2` to give
     `tr_M(Δ_3) = (z + b)((a + c + h)z + 1 + ac)`;
   - Their difference factors universally (independently of `a = d_{01}`) as
     `tr_M(P_3(a,b,c)) - tr_M(Δ_3(a,b,c)) = (b - c) * (z^2 - h * z - 1)`.

2. **Root locus of the quadratic Markov factor (`heckeQuadFactor_eq_roots`):**
   Over any field `K` with `q ≠ 0` and `h = q - q⁻¹`,
     `z^2 - (q - q⁻¹)z - 1 = (z - q)(z + q⁻¹)`,
   vanishing iff `z = q` or `z = -q⁻¹`. At Convention D (`z_D = q^3 / (q^2 + 1)`),
     `z_D^2 - (q - q⁻¹)z_D - 1 = -(q^4 + q^2 + 1) / (q^2 + 1)^2 < 0`
   for every nonzero `q` in any linearly ordered field. Consequently,
     `tr_D(P_3(a,b,c)) = tr_D(Δ_3(a,b,c)) ↔ b = c`,
   explaining why `uud` (`d_{02} = d_{12}`) agrees identically (`4/8` binary
   orderings at `A = 3`) while `udd` (`d_{02} ≠ d_{12}`) strictly differs.

3. **Four-strand uniform (`d_{ij} = 0`) obstruction
   (`trTracedVolumeA4Uniform_sub_trHalfTwistA4Uniform`):**
   Even when all strands are identical (`d_{ij} = 0`, e.g. `pppp`),
   `P_4(0) = σ_1^3 σ_2^2 σ_3` and `Δ_4 = σ_1(σ_2 σ_1)(σ_3 σ_2 σ_1)` satisfy
     `tr_M(P_4(0)) - tr_M(Δ_4) = -h * z * (z^2 - h * z - 1)`,
   which at Convention D (`z = z_D(q)`) is strictly positive for every `q > 1`.

-- Ref: [leitner2026] bean qou-jwl8; computations/probes/traced_volume_and_delta_models_audit_probe.py
-/

namespace QOU.BraidsAndKnots.TracedVolumeVsHalfTwist

/-- Ocneanu Markov trace on `H_2` of the two-crossing product `(σ_1 + a)(σ_1 + c)`
under `σ_1^2 = h * σ_1 + 1`, `tr(1) = 1`, and `tr(σ_1) = z`:
`(σ_1 + a)(σ_1 + c) = (a + c + h) * σ_1 + (1 + a * c)`. -/
def trH2Pair {R : Type*} [CommRing R] (h z a c : R) : R :=
  (a + c + h) * z + (1 + a * c)

/-- Ocneanu Markov trace of the `A = 3` traced-volume product
`P_3(a, b, c) = (σ_1 + a)(σ_1 + b)(σ_2 + c)`, obtained by Markov-peeling the
single `σ_2 + c` factor (`tr(X * (σ_2 + c)) = tr(X) * (z + c)` for `X ∈ H_2`). -/
def trTracedVolumeA3 {R : Type*} [CommRing R] (h z a b c : R) : R :=
  trH2Pair h z a b * (z + c)

/-- Ocneanu Markov trace of the `A = 3` strand-tracked positive half-twist
`Δ_3(a, b, c) = (σ_1 + a)(σ_2 + b)(σ_1 + c)`, obtained by Markov-peeling the
middle `σ_2 + b` factor (`tr((σ_1 + a)(σ_2 + b)(σ_1 + c)) = (z + b) * tr((σ_1 + a)(σ_1 + c))`). -/
def trHalfTwistA3 {R : Type*} [CommRing R] (h z a b c : R) : R :=
  (z + b) * trH2Pair h z a c

/-- The quadratic Hecke-Markov factor `z^2 - h * z - 1` governing the discrepancy
between `traced_volume` products and strand-tracked half-twists. -/
def heckeQuadFactor {R : Type*} [CommRing R] (h z : R) : R :=
  z ^ 2 - h * z - 1

/-- **Universal `A = 3` trace discrepancy (`§7c`, arbitrary `CommRing`).**
The difference between the traced-volume product `P_3(a,b,c)` and the
strand-tracked half-twist `Δ_3(a,b,c)` is independent of `a = d_{01}` and factors
as `(b - c) * (z^2 - h * z - 1)`. -/
theorem trTracedVolumeA3_sub_trHalfTwistA3 {R : Type*} [CommRing R] (h z a b c : R) :
    trTracedVolumeA3 h z a b c - trHalfTwistA3 h z a b c =
      (b - c) * heckeQuadFactor h z := by
  unfold trTracedVolumeA3 trHalfTwistA3 trH2Pair heckeQuadFactor
  ring

/-- When `b = c` (`d_{02} = d_{12}`, as for `uud`), `P_3` and `Δ_3` have identical
Markov trace over any commutative ring and for every `(h, z, a)`. -/
theorem trTracedVolumeA3_eq_of_eq {R : Type*} [CommRing R] (h z a b : R) :
    trTracedVolumeA3 h z a b b = trHalfTwistA3 h z a b b := by
  have hsub := trTracedVolumeA3_sub_trHalfTwistA3 h z a b b
  rw [sub_self, zero_mul] at hsub
  exact sub_eq_zero.mp hsub

/-- Over any field with `q ≠ 0`, the quadratic factor `z^2 - (q - q⁻¹)z - 1`
splits into `(z - q)(z + q⁻¹)`. -/
theorem heckeQuadFactor_eq_roots {K : Type*} [Field K] (q z : K) (hq : q ≠ 0) :
    heckeQuadFactor (q - q⁻¹) z = (z - q) * (z + q⁻¹) := by
  unfold heckeQuadFactor
  field_simp
  ring

/-- Over any field with `q ≠ 0`, `heckeQuadFactor (q - q⁻¹) z = 0` iff
`z = q` (the one-row augmentation root) or `z = -q⁻¹` (the one-column sign root). -/
theorem heckeQuadFactor_eq_zero_iff {K : Type*} [Field K] (q z : K) (hq : q ≠ 0) :
    heckeQuadFactor (q - q⁻¹) z = 0 ↔ z = q ∨ z = -q⁻¹ := by
  rw [heckeQuadFactor_eq_roots q z hq, mul_eq_zero, sub_eq_zero, add_eq_zero_iff_eq_neg]

/-- Convention-D Markov parameter `z_D(q) = q^3 / (q^2 + 1)`. -/
noncomputable def zD {K : Type*} [Field K] (q : K) : K :=
  q ^ 3 / (q ^ 2 + 1)

/-- **Exact Convention-D evaluation of `heckeQuadFactor` (`§7c`, generic `Field`).**
At `z = z_D(q) = q^3 / (q^2 + 1)` and `h = q - q⁻¹`,
`z_D^2 - h * z_D - 1 = -(q^4 + q^2 + 1) / (q^2 + 1)^2`. -/
theorem heckeQuadFactor_at_zD {K : Type*} [Field K] (q : K) (hq2 : q ^ 2 + 1 ≠ 0) :
    heckeQuadFactor (q - q⁻¹) (zD q) = -(q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 := by
  unfold heckeQuadFactor zD
  field_simp [hq2]
  ring

/-- Over any linearly ordered field, `heckeQuadFactor (q - q⁻¹) (zD q) < 0` for
every `q`. -/
theorem heckeQuadFactor_at_zD_neg {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (q : K) :
    heckeQuadFactor (q - q⁻¹) (zD q) < 0 := by
  have hq2_pos : (0 : K) < q ^ 2 + 1 := by positivity
  rw [heckeQuadFactor_at_zD q (ne_of_gt hq2_pos)]
  have hnum_pos : (0 : K) < q ^ 4 + q ^ 2 + 1 := by positivity
  have hden_pos : (0 : K) < (q ^ 2 + 1) ^ 2 := by positivity
  exact div_neg_of_neg_of_pos (neg_lt_zero.mpr hnum_pos) hden_pos

/-- **`A = 3` Convention-D characterization (`qou-jwl8`).**
Over any linearly ordered field, `trTracedVolumeA3` and `trHalfTwistA3` agree
at `z_D(q)` if and only if `b = c` (`d_{02} = d_{12}`). -/
theorem trTracedVolumeA3_eq_trHalfTwistA3_at_zD_iff
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (q a b c : K) :
    trTracedVolumeA3 (q - q⁻¹) (zD q) a b c =
      trHalfTwistA3 (q - q⁻¹) (zD q) a b c ↔ b = c := by
  have hfac_ne : heckeQuadFactor (q - q⁻¹) (zD q) ≠ 0 :=
    ne_of_lt (heckeQuadFactor_at_zD_neg q)
  rw [← sub_eq_zero, trTracedVolumeA3_sub_trHalfTwistA3, mul_eq_zero,
    or_iff_left hfac_ne, sub_eq_zero]

/-- Specialization to `udd` under the standard typed-crossing shifts
`d(u,d) = -h/2`, `d(d,d) = -h`: for every `q > 1` over a linearly ordered field,
the Convention-D traced-volume product and half-twist strictly disagree on `udd`. -/
theorem udd_tracedVolume_ne_halfTwist_at_zD
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (q : K) (hq1 : 1 < q) :
    let h := q - q⁻¹
    trTracedVolumeA3 h (zD q) (-h / 2) (-h / 2) (-h) ≠
      trHalfTwistA3 h (zD q) (-h / 2) (-h / 2) (-h) := by
  intro h
  rw [ne_eq, trTracedVolumeA3_eq_trHalfTwistA3_at_zD_iff q (-h / 2) (-h / 2) (-h)]
  have hh_pos : (0 : K) < h := by
    dsimp [h]
    have hinv_lt : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq1
    linarith
  linarith

/-! ### Four-strand uniform (`d_{ij} = 0`) obstruction -/

/-- Ocneanu Markov trace of the `A = 4` uniform traced-volume product
`P_4(0) = σ_1^3 σ_2^2 σ_3`:
`tr(σ_1^3) = (h^2 + 1)z + h`, `tr(σ_1^2) = h*z + 1`, `tr(σ_1) = z`. -/
def trTracedVolumeA4Uniform {R : Type*} [CommRing R] (h z : R) : R :=
  ((h ^ 2 + 1) * z + h) * (h * z + 1) * z

/-- Ocneanu Markov trace of the `A = 4` uniform positive half-twist
`Δ_4 = σ_1 (σ_2 σ_1) (σ_3 σ_2 σ_1)`, reduced via Markov peeling and the braid
relation (`tr_M(Δ_4) = z^2 * tr_2(σ_1^4) = z^2 * ((h^3 + 2h)z + h^2 + 1)`). -/
def trHalfTwistA4Uniform {R : Type*} [CommRing R] (h z : R) : R :=
  z ^ 2 * ((h ^ 3 + 2 * h) * z + h ^ 2 + 1)

/-- **Universal `A = 4` uniform trace discrepancy (`§7c`, arbitrary `CommRing`).**
Even when all pair shifts vanish (`d_{ij} = 0`), `P_4(0)` and `Δ_4` differ by
`-h * z * (z^2 - h * z - 1)`. -/
theorem trTracedVolumeA4Uniform_sub_trHalfTwistA4Uniform {R : Type*} [CommRing R] (h z : R) :
    trTracedVolumeA4Uniform h z - trHalfTwistA4Uniform h z =
      -h * z * heckeQuadFactor h z := by
  unfold trTracedVolumeA4Uniform trHalfTwistA4Uniform heckeQuadFactor
  ring

/-- At Convention D (`z = z_D(q)`), for every `q > 1` over a linearly ordered
field, the uniform `A = 4` traced-volume product strictly exceeds the half-twist
trace (`tr_D(P_4(0)) > tr_D(Δ_4)`). -/
theorem trTracedVolumeA4Uniform_gt_trHalfTwistA4Uniform_at_zD
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] (q : K) (hq1 : 1 < q) :
    trHalfTwistA4Uniform (q - q⁻¹) (zD q) < trTracedVolumeA4Uniform (q - q⁻¹) (zD q) := by
  have hq0 : (0 : K) < q := lt_trans zero_lt_one hq1
  have hh_pos : (0 : K) < q - q⁻¹ := by
    have hinv_lt : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq1
    linarith
  have hzD_pos : (0 : K) < zD q := by
    unfold zD
    positivity
  have hfac_neg : heckeQuadFactor (q - q⁻¹) (zD q) < 0 :=
    heckeQuadFactor_at_zD_neg q
  have hsub := trTracedVolumeA4Uniform_sub_trHalfTwistA4Uniform (q - q⁻¹) (zD q)
  have hprod_pos : (0 : K) < -(q - q⁻¹) * zD q * heckeQuadFactor (q - q⁻¹) (zD q) := by
    have h1 : -(q - q⁻¹) * zD q < 0 := by nlinarith
    exact mul_pos_of_neg_of_neg h1 hfac_neg
  linarith

end QOU.BraidsAndKnots.TracedVolumeVsHalfTwist
