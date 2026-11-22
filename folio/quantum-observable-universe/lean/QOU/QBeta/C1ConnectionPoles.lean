import Mathlib.Tactic
import Mathlib.Topology.Algebra.InfiniteSum.Ring
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Analysis.Complex.LocallyUniformLimit
import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.MeasureTheory.Integral.CircleIntegral
import QOU.Mathlib.CircleIntegralFinsetSum

/-!
# The q-theta zero locus — where the C1 connection matrix has its poles

The connection matrix `P = Y₀⁻¹ Y_∞` of the ramified C1 operator

    L = (p⁴z² − 1)τ² − (p²−1)τ − (p²−1),   τF(z) = F(pz),  q = p²

is `p`-elliptic, and every one of its poles sits where some `θ_p` in the
construction vanishes (`computations/qbeta/c3_w2_c1_connection_matrix.py`):

| pole on `ℂ*/p^ℤ` | locus | source | intrinsic? |
|---|---|---|---|
| `[−1]` | `z ∈ −p^ℤ` | `θ_p(z)`, the common numerator of the `0`-side character `e_t(z) = θ_p(z)/θ_p(z/t)` | **no** — normalisation artifact |
| `[−T]` | `z ∈ −T·p^ℤ` | `θ_p(z/T₊)` | yes |
| `[+T]` | `z ∈ +T·p^ℤ` | `θ_p(−z/T)` | yes |

with `T = √((p²−1)/p³) = √(q−1)/q^{3/4}` the theta-normalised canonical
parameter. So *all three* loci are single `p`-orbits of the zero set of `θ_p`,
and the whole question reduces to: **where does `θ_p` vanish?**

## What this file proves

* `qTheta_neg_zpow_eq_zero` — `θ_p(w) = 0` for every `w ∈ −p^ℤ`, the `⊇`
  direction of the zero locus, which is exactly what places the poles above.
  The converse — that these are the *only* zeros, each simple — is
  `QOU/QBeta/C1ThetaZeroLocus.lean`, built on the contour identity below.
* `summable_qThetaTerm` — the series converges for `P > 1`, `w ≠ 0`.
* `qTheta_functional_equation` — `θ_P(P²w) = w·θ_P(w)`, i.e. `θ_p(pw) = w θ_p(w)`.
* `qThetaC_conj` / `norm_qThetaC_conj_pair` — `θ_P` commutes with conjugation,
  so the two **conjugate** `0`-side exponents give **exactly equal** magnitudes
  on the real axis. This is the formal core of the refutation the whole C1 arc
  restarted from: a basis putting them "~17 orders of magnitude apart" is
  impossible, not merely unobserved.
* `differentiableOn_qThetaC` — **`θ_P` is holomorphic on `ℂ*`** (bean
  `qou-c1ln` step 1): Weierstrass M-test on annuli plus
  `TendstoLocallyUniformlyOn.differentiableOn`. Makes `θ_P` a genuine analytic
  object, the prerequisite for it having a divisor at all.
* `qThetaC_functional_equation` / `deriv_qThetaC_functional_equation` /
  `logDeriv_qThetaC_functional_equation` — the functional equation over `ℂ`,
  differentiated, and in logarithmic-derivative form
  `p·θ'(pw)/θ(pw) = 1/w + θ'(w)/θ(w)`. That last one is the **`+1` per
  period**: it is the entire zero-counting mechanism the converse zero locus
  runs on.
* `circleIntegral_scale` / `winding_step` / `qTheta_winding_step` — the same
  `+1`, carried up to the **contour** level:

      ∮_{|z| = pρ} θ'/θ dz  =  2πi  +  ∮_{|z| = ρ} θ'/θ dz

  for any `ρ > 0` on whose circle `θ_P` does not vanish. This is the form the
  argument principle consumes. `circleIntegral_scale` (change of variables for
  `circleIntegral`, absent from Mathlib) and `winding_step` (`1/w` in the
  integrand ⇒ `2πi` in the integral) are stated `θ`-free and are reusable.
* `qTheta_inversion` — `θ_P(1/w) = w·θ_P(w)`, Morita's inversion formula
  (arXiv:1105.1998 §2.1) in our normalisation.
* `thetaRatio_multiplier` — `θ_P(cz)/θ_P(z)` is a q-character with multiplier
  `c`: the building block of every connection coefficient in the literature
  (the *pseudo-constants* of Ramis–Sauloy–Zhang).
* `connRatio_reflect` — numerator and denominator of the closed form swap under
  conjugation, which is why `|χ| = 1` on `ℝ*` and zeros pair with conjugate poles.
* `connRatio_elliptic` — the closed form found for the connection invariant
  (a ratio of four `θ_p`'s) is `p`-elliptic, straight from the functional
  equation. Proves the *shape* is right; not that χ equals it.

`summable_qThetaTerm`, `differentiableOn_qThetaC` and
`qTheta_functional_equation` are the **analytic foundation for the converse**.
The vanishing theorem itself needs none of them (see below), but every route to
"these are the *only* zeros" needs `θ_p` to be a genuine analytic object, and
the functional equation is what forces the zero set to be a union of
`p`-orbits.

The proof is an **involution**, and needs no analysis at all. For each `k`, the
map `n ↦ 2k−1−n` on `ℤ`

* leaves the exponent `−n(n+1) + 2kn` **invariant** (pure `ring`), and
* **flips** `(−1)ⁿ`, since `n + (2k−1−n) = 2k−1` is odd,

so the series is its own negative and therefore vanishes. Crucially
`Equiv.tsum_eq` and `tsum_neg` are both **unconditional** in Mathlib, so **no
summability hypothesis is required** — which is what makes this cheap.

### Reparametrisation

Everything is stated in `P` with `p = P²`, so that the exponent is `−n(n+1)`
with **no integer division**. `θ_P(P²w) = w·θ_P(w)` is then the usual
`θ_p(pw) = w·θ_p(w)`. This is purely to keep the arithmetic division-free;
nothing mathematical turns on it.

## What this file does NOT prove — stated so it is not read for more

* **The converse.** That `−p^ℤ` are the *only* zeros of `θ_p` is the **Jacobi
  triple product**, which is not proved here. Without it one gets "these points
  *are* zeros", not "there are no others".

  **Mathlib cannot supply it** (source inspected at HEAD, 2026-08-07):
  `Mathlib/NumberTheory/ModularForms/JacobiTheta/` has `OneVariable`,
  `TwoVariable`, `Bounds`, `Manifold`, defining the *additive* two-variable
  theta `jacobiTheta₂ z τ = ∑' n : ℤ, …` — but there is **no Jacobi triple
  product** anywhere (the "triple product" matches are Jordan algebras, the
  Hermitian functional calculus, and the vector cross product) and **no
  zero-locus or vanishing results for theta at all**.

  What Mathlib *does* have, and what a future attempt should build on:
  `HasProd`/`Multipliable`/`tprod` (full infinite-product infrastructure),
  `Analysis/Meromorphic/{Divisor, IsolatedZeros, Order}`, and the full
  `circleIntegral` API including
  `Complex.circleIntegral_eq_of_differentiable_on_annulus_off_countable`. It
  does **not** have the argument principle, a winding number, or a complex
  residue (name scan at HEAD, 2026-08-07: zero hits for `argumentPrinciple`,
  `windingNumber`, `countZeros`; every `residue` hit is `IsLocalRing`).

  **But JTP is not on the critical path**, and that is worth stating plainly
  because this file previously implied it was. The two routes are not equally
  costly:

  (a) *zero-counting.* `θ_p` holomorphic on `ℂ*` + `θ_p(pw) = wθ_p(w)` forces
      the winding number on `|w| = pρ` to exceed the one on `|w| = ρ` by
      **exactly one**. That is no longer a sketch: it is
      `qTheta_winding_step` below, proved. The argument principle then reads
      the difference off as *exactly one zero, with multiplicity, in
      `ρ < |z| < pρ`*, which combined with `qTheta_neg_zpow_eq_zero` pins it at
      `−p^k`, makes it simple, and excludes any other. **Every input to (a)
      other than the argument principle itself is now proved in this file**,
      up to and including the contour identity it would be applied to.
  (b) *JTP via the product side* — define `∏(1−xᵐ)(1+xᵐw)(1+xᵐ⁻¹w⁻¹)`, show it
      satisfies the same functional equation, conclude the ratio is elliptic
      and bounded hence constant. This additionally needs Liouville on
      `ℂ*/p^ℤ`, i.e. strictly more than (a).

  So the honest remaining gap is **one named Mathlib-scale lemma**, the
  argument principle on an annulus, not a theory build-out. That is still not a
  small job — but it is a different size of job than "formalise JTP", and the
  distinction was being lost. Recorded so this is neither re-scoped as cheap
  nor written off as hopeless.

  Independently: the statement itself is checked to hold at our substrate in
  `computations/qbeta/c3_w2_c1_theta_zero_count.py`, so what is missing is a
  formalisation gap and not a mathematical doubt.
* **That these zeros are poles of `P`.** That needs the analytic construction
  — convergent `0`-side series, entire `∞`-side series, the matrix inverse and
  its meromorphy — none of which is formalised.
* **Divisor completeness.** The residue-theorem argument (each entry has
  exactly two simple poles per fundamental domain, so residues cancel) lives on
  the multiplicative torus `ℂ*/p^ℤ` and needs elliptic-function theory that
  Mathlib does not have.

Numerically all of the above is checked in the witness
`computations/qbeta/c3-w2-c1-connection-matrix.witness.json` (7/7).

-- Ref: [leitner2026] computations/qbeta/c3_w2_c1_connection_matrix.py
-- Ref: [ramis-sauloy-zhang2013] Astérisque 355 §3.3 (Ramis–Sauloy–Zhang)
-- Ref: [lin2024] explicit connection formula and q-Stokes matrix for the
--      confluent basic hypergeometric nφn−1 (a zero parameter; §2–§3, q → 1 in §4). A
--      worked explicit q-Stokes computation; whether its equation class
--      covers the C1 module is not checked here.
-/

namespace QOU.QBeta.C1Poles

/-- One term of the q-theta series, `P^{-n(n+1)} wⁿ`. -/
noncomputable def qThetaTerm (P w : ℝ) (n : ℤ) : ℝ := P ^ (-(n * (n + 1))) * w ^ n

/-- `θ_P(w) = ∑_{n ∈ ℤ} P^{-n(n+1)} wⁿ`, the q-theta with `p = P²`. -/
noncomputable def qTheta (P w : ℝ) : ℝ := ∑' n : ℤ, qThetaTerm P w n

/-- The pairing `n ↦ 2k−1−n`, an involution of `ℤ`. -/
def pairing (k : ℤ) : ℤ ≃ ℤ where
  toFun n := 2 * k - 1 - n
  invFun n := 2 * k - 1 - n
  left_inv n := by simp
  right_inv n := by simp

/-- `(-(P^{2k}))^j = (-1)^j · P^{2kj}` — splitting the sign off the base. -/
private lemma neg_zpow_split (P : ℝ) (k j : ℤ) :
    (-(P ^ (2 * k))) ^ j = (-1 : ℝ) ^ j * P ^ (2 * k * j) := by
  have h : -(P ^ (2 * k)) = (-1 : ℝ) * P ^ (2 * k) := by ring
  rw [h, mul_zpow, ← zpow_mul]

/-- `n` and `2k−1−n` have opposite parity, so `(-1)^·` flips. -/
private lemma sign_flip (n k : ℤ) :
    ((-1 : ℝ)) ^ (2 * k - 1 - n) = -((-1 : ℝ)) ^ n := by
  rcases Int.even_or_odd n with he | ho
  · have hodd : Odd (2 * k - 1 - n) := by
      obtain ⟨t, ht⟩ := he; exact ⟨k - t - 1, by omega⟩
    rw [hodd.neg_one_zpow, he.neg_one_zpow]
  · have heven : Even (2 * k - 1 - n) := by
      obtain ⟨t, ht⟩ := ho; exact ⟨k - t - 1, by omega⟩
    rw [heven.neg_one_zpow, ho.neg_one_zpow]; ring

/-- **The heart.** At `w = -P^{2k}` the term at `2k−1−n` is the negative of the
term at `n`: the exponent is invariant and the sign flips. -/
theorem qThetaTerm_pairing (P : ℝ) (hP : 0 < P) (k n : ℤ) :
    qThetaTerm P (-(P ^ (2 * k))) (2 * k - 1 - n)
      = - qThetaTerm P (-(P ^ (2 * k))) n := by
  have hP0 : P ≠ 0 := ne_of_gt hP
  simp only [qThetaTerm, neg_zpow_split P]
  rw [sign_flip n k]
  rw [show -((2 * k - 1 - n) * (2 * k - 1 - n + 1)) = -((2*k-1-n) * (2*k-n)) by ring_nf]
  rw [mul_comm ((-1 : ℝ) ^ n) _, mul_comm (-((-1 : ℝ) ^ n)) _]
  rw [← mul_assoc, ← mul_assoc, ← zpow_add₀ hP0, ← zpow_add₀ hP0]
  rw [show -((2*k-1-n) * (2*k-n)) + 2 * k * (2 * k - 1 - n)
        = -(n * (n + 1)) + 2 * k * n by ring]
  ring

/-! ### Analytic infrastructure

The vanishing theorem below needs none of this — `Equiv.tsum_eq` and `tsum_neg`
are unconditional, so it goes through even if `qTheta` were junk. But *any*
route to the converse (Jacobi triple product, or zero-counting via the argument
principle) needs `qTheta` to be a genuine analytic object first. These two are
that foundation. -/

/-- `P ^ (m : ℤ) = exp (log P * m)` for `P > 0`. -/
private lemma zpow_eq_exp (P : ℝ) (hP : 0 < P) (m : ℤ) :
    P ^ m = Real.exp (Real.log P * m) := by
  rw [← Real.rpow_intCast P m, Real.rpow_def_of_pos hP]

private lemma abs_zpow' (w : ℝ) (n : ℤ) : |w ^ n| = |w| ^ n := by
  have h := norm_zpow w n
  rwa [Real.norm_eq_abs, Real.norm_eq_abs] at h

/-- The modulus of a term, in exponential form: `exp(−L n² + (M−L) n)` with
`L = log P` and `M = log |w|`. -/
private lemma abs_qThetaTerm (P w : ℝ) (hP : 0 < P) (hw : w ≠ 0) (n : ℤ) :
    |qThetaTerm P w n|
      = Real.exp (Real.log P * (-(n * (n + 1))) + Real.log |w| * n) := by
  have hw0 : (0:ℝ) < |w| := abs_pos.mpr hw
  rw [qThetaTerm, abs_mul, abs_zpow' w n, abs_of_pos (zpow_pos hP _),
      zpow_eq_exp P hP, zpow_eq_exp |w| hw0, ← Real.exp_add]
  push_cast
  ring_nf

/-- **The q-theta series is summable** for `P > 1`, `w ≠ 0`.

`|term n| = exp(−L n² + (M−L) n)` with `L = log P > 0`. Since
`−L t² + B t ≤ B²/(4L)` for every real `t` (one completed square), the series is
dominated by `C·e^{−|n|}` with `C = exp(B²/(4L))`, `B = |M−L| + 1`. -/
theorem summable_qThetaTerm (P w : ℝ) (hP : 1 < P) (hw : w ≠ 0) :
    Summable (fun n : ℤ => qThetaTerm P w n) := by
  have hP0 : (0:ℝ) < P := lt_trans zero_lt_one hP
  have hL : 0 < Real.log P := Real.log_pos hP
  set L := Real.log P with hLdef
  set M := Real.log |w| with hMdef
  set B := |M - L| + 1 with hBdef
  have hB : 0 ≤ B := by positivity
  set C := Real.exp (B ^ 2 / (4 * L)) with hCdef
  refine Summable.of_norm_bounded
    (g := fun n : ℤ => C * Real.exp (-1) ^ (n.natAbs)) ?_ ?_
  · have hr : Real.exp (-1) < 1 := by
      rw [show (1:ℝ) = Real.exp 0 by simp]
      exact Real.exp_lt_exp.mpr (by norm_num)
    have hr0 : (0:ℝ) ≤ Real.exp (-1) := (Real.exp_pos _).le
    have hnat : Summable (fun k : ℕ => C * Real.exp (-1) ^ k) :=
      (summable_geometric_of_lt_one hr0 hr).mul_left C
    refine Summable.of_nat_of_neg ?_ ?_
    · simpa using hnat
    · simpa using hnat
  · intro n
    have hgoal : ‖qThetaTerm P w n‖
        = Real.exp (L * (-((n:ℝ) * ((n:ℝ) + 1))) + M * (n:ℝ)) := by
      rw [Real.norm_eq_abs, abs_qThetaTerm P w hP0 hw n]
    rw [hgoal]
    show _ ≤ C * Real.exp (-1) ^ (n.natAbs)
    have hexp : Real.exp (-1) ^ (n.natAbs) = Real.exp (-((n.natAbs : ℝ))) := by
      rw [← Real.exp_nat_mul]; ring_nf
    rw [hexp, hCdef, ← Real.exp_add]
    apply Real.exp_le_exp.mpr
    have habs : ((n.natAbs : ℝ)) = |(n : ℝ)| := by
      rw [Int.cast_natAbs]; simp
    rw [habs]
    have h1 : M * (n : ℝ) - L * (n : ℝ) ≤ |M - L| * |(n : ℝ)| := by
      calc M * (n : ℝ) - L * (n : ℝ) = (M - L) * (n : ℝ) := by ring
        _ ≤ |(M - L) * (n : ℝ)| := le_abs_self _
        _ = |M - L| * |(n : ℝ)| := abs_mul _ _
    have h2 : (0:ℝ) ≤ |(n : ℝ)| := abs_nonneg _
    have hn2 : |(n : ℝ)| ^ 2 = (n : ℝ) ^ 2 := sq_abs _
    -- `B - 1 = |M - L|`: the linear term is `|M-L|·|n|`, not `B·|n|`
    have key : L * (-((n : ℝ) * ((n : ℝ) + 1))) + M * (n : ℝ)
        ≤ -L * |(n : ℝ)| ^ 2 + |M - L| * |(n : ℝ)| := by
      rw [hn2]; nlinarith [h1, h2]
    have para : -L * |(n : ℝ)| ^ 2 + |M - L| * |(n : ℝ)|
        ≤ B ^ 2 / (4 * L) - |(n : ℝ)| := by
      have h4L : (0:ℝ) < 4 * L := by linarith
      rw [le_sub_iff_add_le, ← sub_nonneg]
      have expand : B ^ 2 / (4 * L)
            - (-L * |(n : ℝ)| ^ 2 + |M - L| * |(n : ℝ)| + |(n : ℝ)|)
          = (2 * L * |(n : ℝ)| - B) ^ 2 / (4 * L) := by
        rw [hBdef]; field_simp; ring
      rw [expand]
      positivity
    linarith [key, para]

/-- **The functional equation** `θ_P(P²w) = w · θ_P(w)`.

With `p = P²` this is the usual `θ_p(pw) = w·θ_p(w)` — what makes `θ_p(z/T)⁻¹`
realise the multiplier a slope-1 irregular singularity demands. Both sides equal
`∑ P^{−n(n−1)} wⁿ`. Unconditional, like the vanishing theorem. -/
theorem qTheta_functional_equation (P w : ℝ) (hP : 0 < P) (hw : w ≠ 0) :
    qTheta P (P ^ (2:ℤ) * w) = w * qTheta P w := by
  have hP0 : P ≠ 0 := ne_of_gt hP
  have hleft : ∀ n : ℤ,
      qThetaTerm P (P ^ (2:ℤ) * w) n = P ^ (-(n * (n - 1))) * w ^ n := by
    intro n
    rw [qThetaTerm, mul_zpow, ← zpow_mul, ← mul_assoc, ← zpow_add₀ hP0]
    congr 2
    ring
  have hright : ∀ n : ℤ,
      w * qThetaTerm P w (n - 1) = P ^ (-(n * (n - 1))) * w ^ n := by
    intro n
    have hww : w * w ^ (n - 1) = w ^ n := by
      have h := zpow_add₀ hw 1 (n - 1)
      rw [zpow_one, show (1:ℤ) + (n - 1) = n by ring] at h
      exact h.symm
    rw [qThetaTerm, show -((n - 1) * ((n - 1) + 1)) = -(n * (n - 1)) by ring,
        ← mul_assoc, mul_comm w _, mul_assoc, hww]
  calc qTheta P (P ^ (2:ℤ) * w)
      = ∑' n : ℤ, P ^ (-(n * (n - 1))) * w ^ n := by
        rw [qTheta]; exact tsum_congr hleft
    _ = ∑' n : ℤ, w * qThetaTerm P w (n - 1) := (tsum_congr hright).symm
    _ = w * ∑' n : ℤ, qThetaTerm P w (n - 1) := by rw [tsum_mul_left]
    _ = w * qTheta P w := by
        rw [qTheta]
        congr 1
        exact (Equiv.subRight (1:ℤ)).tsum_eq (fun n => qThetaTerm P w n)

/-- **The q-theta vanishes on the whole orbit `-P^{2k}`, `k ∈ ℤ`.**

With `p = P²` this says `θ_p(w) = 0` for every `w ∈ −p^ℤ`. No summability
hypothesis: `Equiv.tsum_eq` and `tsum_neg` hold unconditionally, so the
involution closes the goal outright. -/
theorem qTheta_neg_zpow_eq_zero (P : ℝ) (hP : 0 < P) (k : ℤ) :
    qTheta P (-(P ^ (2 * k))) = 0 := by
  set f : ℤ → ℝ := fun n => qThetaTerm P (-(P ^ (2 * k))) n with hf
  have hpt : ∀ n : ℤ, f ((pairing k) n) = - f n := fun n => qThetaTerm_pairing P hP k n
  have hS : ∑' n : ℤ, f n = - ∑' n : ℤ, f n := by
    calc ∑' n : ℤ, f n
        = ∑' n : ℤ, f ((pairing k) n) := ((pairing k).tsum_eq f).symm
      _ = ∑' n : ℤ, (- f n) := by simp only [hpt]
      _ = - ∑' n : ℤ, f n := tsum_neg
  have hzero : ∑' n : ℤ, f n = 0 := by linarith
  simpa [qTheta, hf] using hzero

/-- Specialisation `k = 0`: `θ_P(-1) = 0`. This is the `[−1]` pole — the one
coming from the `0`-side character's common numerator, hence a normalisation
artifact rather than intrinsic connection data. -/
theorem qTheta_neg_one_eq_zero (P : ℝ) (hP : 0 < P) : qTheta P (-1) = 0 := by
  simpa using qTheta_neg_zpow_eq_zero P hP 0

/-- **The `∞`-side pole loci `z ∈ ∓T·p^ℤ`.**

The `∞`-side solutions carry `θ_p(z/T₊)` and `θ_p(−z/T)` in their denominators,
so they blow up exactly where those vanish. For any `T ≠ 0` and any `k`, the
point `z = −T·P^{2k}` is such a zero. Instantiating `T := T₊` gives the `[−T]`
locus and `T := −T₊` the `[+T]` locus. -/
theorem qTheta_div_eq_zero_on_orbit (P T : ℝ) (hP : 0 < P) (hT : T ≠ 0) (k : ℤ) :
    qTheta P ((-(T * P ^ (2 * k))) / T) = 0 := by
  have h : (-(T * P ^ (2 * k))) / T = -(P ^ (2 * k)) := by
    field_simp
  rw [h]
  exact qTheta_neg_zpow_eq_zero P hP k

/-! ### Conjugation — the formal core of the refutation

The whole C1 arc restarted from refuting a "the `0`-side basis is degenerate,
the two conjugate exponents sit ~17 orders of magnitude apart" negative. The
reason that is *impossible* is one line of algebra, and it formalises cheaply. -/

/-- The q-theta with a COMPLEX argument (the base `P` stays real). -/
noncomputable def qThetaC (P : ℝ) (w : ℂ) : ℂ :=
  ∑' n : ℤ, (P : ℂ) ^ (-(n * (n + 1))) * w ^ n

/-- **`θ_P` has real coefficients, so it commutes with conjugation.** -/
theorem qThetaC_conj (P : ℝ) (w : ℂ) :
    qThetaC P ((starRingEnd ℂ) w) = (starRingEnd ℂ) (qThetaC P w) := by
  rw [qThetaC, qThetaC, Complex.conj_tsum]
  refine tsum_congr fun n => ?_
  rw [map_mul, map_zpow₀, map_zpow₀, Complex.conj_ofReal]

/-- **The magnitudes at a conjugate pair of exponents agree EXACTLY.**

The `0`-side exponents are a conjugate pair `t`, `conj t`
(`C1ZeroSideExponents.conjugate_pair_iff`). For **real** `z`,
`z / conj t = conj (z / t)`, so by `qThetaC_conj` the two theta values are
conjugates and their magnitudes are equal — hence so are `|e_t(z)|` for the two
exponents, since they share the numerator `θ_p(z)`.

A construction placing the two conjugate exponents "~17 orders of magnitude
apart" is therefore **impossible**, which is exactly what the numerics found
(measured ratio `1.0`, deviation `0.0`) and what
`computations/qbeta/c3_w2_c1_connection_matrix.py` records. No hypothesis on `t`
is needed: at `t = 0` both sides are `θ_P(0)`. -/
theorem norm_qThetaC_conj_pair (P : ℝ) (z : ℝ) (t : ℂ) :
    ‖qThetaC P ((z : ℂ) / (starRingEnd ℂ) t)‖ = ‖qThetaC P ((z : ℂ) / t)‖ := by
  have hz : ((z : ℂ)) / (starRingEnd ℂ) t = (starRingEnd ℂ) ((z : ℂ) / t) := by
    rw [map_div₀, Complex.conj_ofReal]
  rw [hz, qThetaC_conj, RCLike.norm_conj]

/-! ### The connection invariant's closed form

Numerically, the basis-invariant connection datum
`χ = P₀₀P₁₁/(P₀₁P₁₀)` equals

    χ(z) = θ_p(z/α)·θ_p(−z/ᾱ) / [ θ_p(−z/α)·θ_p(z/ᾱ) ],   α = t₂/T

with constant **exactly 1** and `|α| = q^{3/4}` — worst relative deviation
`5.3e-63` over twelve independent points
(`computations/qbeta/c3_w2_c1_connection_invariant.py` and successors). The
theorem below proves that this *shape* has the required invariance, straight
from the functional equation. It does not prove that χ equals it — that needs
the analytic construction, which is not formalised. -/

/-- **The closed form is `p`-elliptic.**

Stated division-free as a cross-multiplied identity, so no hypothesis that the
theta values are nonzero is needed. The four functional-equation factors are
`z/a`, `−z/b` upstairs and `−z/a`, `z/b` downstairs; their products are both
`−z²/(ab)` and cancel. -/
theorem connRatio_elliptic (P a b z : ℝ) (hP : 0 < P)
    (ha : a ≠ 0) (hb : b ≠ 0) (hz : z ≠ 0) :
    qTheta P (P ^ (2:ℤ) * z / a) * qTheta P (-(P ^ (2:ℤ) * z) / b)
        * (qTheta P (-z / a) * qTheta P (z / b))
      = qTheta P (-(P ^ (2:ℤ) * z) / a) * qTheta P (P ^ (2:ℤ) * z / b)
        * (qTheta P (z / a) * qTheta P (-z / b)) := by
  have e : ∀ w : ℝ, w ≠ 0 → qTheta P (P ^ (2:ℤ) * w) = w * qTheta P w :=
    fun w hw => qTheta_functional_equation P w hP hw
  have d1 : P ^ (2:ℤ) * z / a = P ^ (2:ℤ) * (z / a) := by ring
  have d2 : -(P ^ (2:ℤ) * z) / b = P ^ (2:ℤ) * (-z / b) := by ring
  have d3 : -(P ^ (2:ℤ) * z) / a = P ^ (2:ℤ) * (-z / a) := by ring
  have d4 : P ^ (2:ℤ) * z / b = P ^ (2:ℤ) * (z / b) := by ring
  rw [d1, d2, d3, d4, e _ (div_ne_zero hz ha), e _ (div_ne_zero (neg_ne_zero.mpr hz) hb),
      e _ (div_ne_zero (neg_ne_zero.mpr hz) ha), e _ (div_ne_zero hz hb)]
  ring

/-- **The theta quotient `E_c(z) = θ_P(cz)/θ_P(z)` is a q-character with
multiplier `c`.**

Division-free form of `E_c(P²z) = c · E_c(z)`. This is the building block every
connection coefficient in the literature is made of: Lin–Ma–Xu
(arXiv:2412.02281, Thm 1.2) writes them as
`(constant) · θ_q(−aᵢz)/θ_q(−z) · z^{log_q aᵢ}`, and `θ_q(cz)/θ_q(z)` is the
q-analogue of the power `z^{log_q c}`. Such coefficients are the
*pseudo-constants* of Ramis–Sauloy–Zhang. It is also why the cross-ratio χ has
constant exactly `1`: the constants and the `θ(z)` denominators cancel. -/
theorem thetaRatio_multiplier (P c z : ℝ) (hP : 0 < P) (hc : c ≠ 0) (hz : z ≠ 0) :
    qTheta P (P ^ (2:ℤ) * (c * z)) * qTheta P z
      = c * (qTheta P (c * z) * qTheta P (P ^ (2:ℤ) * z)) := by
  rw [qTheta_functional_equation P (c * z) hP (mul_ne_zero hc hz),
      qTheta_functional_equation P z hP hz]
  ring

/-- **The reflection law behind `|χ| = 1` on the real axis.**

With `ᾱ = conj α`, the numerator and denominator of the closed form swap under
conjugation: `N(z̄) = conj (D z)`. Hence `χ(z̄) = 1/conj χ(z)`, which forces
`|χ| = 1` on `ℝ*` and pairs every zero with a conjugate pole — exactly the
structure measured (reflection law verified numerically to `1e-268`). -/
theorem connRatio_reflect (P : ℝ) (a z : ℂ) :
    qThetaC P ((starRingEnd ℂ) z / a) * qThetaC P (-((starRingEnd ℂ) z) / (starRingEnd ℂ) a)
      = (starRingEnd ℂ) (qThetaC P (-z / a) * qThetaC P (z / (starRingEnd ℂ) a)) := by
  rw [map_mul, ← qThetaC_conj, ← qThetaC_conj, map_div₀, map_div₀, map_neg,
      RingHomCompTriple.comp_apply, RingHom.id_apply]
  ring

/-- **Inversion formula** `θ_P(1/w) = w · θ_P(w)`.

Morita (arXiv:1105.1998 §2.1) records it as `x·θ(1/x) = θ(x)` in his
normalisation; this is the same identity in ours. Reindex `n ↦ −n` on the left
and `n ↦ n−1` on the right: both sides are `∑ P^{−n(n−1)} wⁿ`. Unconditional. -/
theorem qTheta_inversion (P w : ℝ) (hw : w ≠ 0) :
    qTheta P (1 / w) = w * qTheta P w := by
  have hL : ∀ n : ℤ, qThetaTerm P (1 / w) (-n) = P ^ (-(n * (n - 1))) * w ^ n := by
    intro n
    have h1 : ((1:ℝ) / w) ^ (-n) = w ^ n := by
      rw [one_div, inv_zpow, ← zpow_neg, neg_neg]
    rw [qThetaTerm, h1, show -(-n * (-n + 1)) = -(n * (n - 1)) by ring]
  have hR : ∀ n : ℤ, w * qThetaTerm P w (n - 1) = P ^ (-(n * (n - 1))) * w ^ n := by
    intro n
    have hww : w * w ^ (n - 1) = w ^ n := by
      have h := zpow_add₀ hw 1 (n - 1)
      rw [zpow_one, show (1:ℤ) + (n - 1) = n by ring] at h
      exact h.symm
    rw [qThetaTerm, show -((n - 1) * ((n - 1) + 1)) = -(n * (n - 1)) by ring,
        ← mul_assoc, mul_comm w _, mul_assoc, hww]
  calc qTheta P (1 / w)
      = ∑' n : ℤ, qThetaTerm P (1 / w) ((Equiv.neg ℤ) n) :=
        ((Equiv.neg ℤ).tsum_eq (fun n => qThetaTerm P (1 / w) n)).symm
    _ = ∑' n : ℤ, P ^ (-(n * (n - 1))) * w ^ n := tsum_congr hL
    _ = ∑' n : ℤ, w * qThetaTerm P w (n - 1) := (tsum_congr hR).symm
    _ = w * ∑' n : ℤ, qThetaTerm P w (n - 1) := by rw [tsum_mul_left]
    _ = w * qTheta P w := by
        rw [qTheta]; congr 1
        exact (Equiv.subRight (1:ℤ)).tsum_eq (fun n => qThetaTerm P w n)

/-! ### Holomorphy on `ℂ*` — the first analytic infrastructure step

Bean `qou-c1ln` step 1. Needed by every route to the converse of the zero
locus, and by any statement that `θ_p` has a *divisor* at all. -/

/-- One term of the complex-argument series. -/
noncomputable def qThetaCTerm (P : ℝ) (w : ℂ) (n : ℤ) : ℂ :=
  (P : ℂ) ^ (-(n * (n + 1))) * w ^ n

lemma qThetaC_eq_tsum (P : ℝ) (w : ℂ) : qThetaC P w = ∑' n : ℤ, qThetaCTerm P w n := rfl

/-- **The complex `θ_P` restricted to real arguments is the real one.**

The bridge every real fact about `θ_P` — the vanishing theorem
`qTheta_neg_zpow_eq_zero` above all — crosses to reach the complex-analytic
statements. Unconditional: `Complex.ofReal_tsum` needs no summability, since
both sides are `0` when the family is not summable. -/
lemma qThetaC_ofReal (P w : ℝ) : qThetaC P (w : ℂ) = ((qTheta P w : ℝ) : ℂ) := by
  rw [qThetaC_eq_tsum, qTheta, Complex.ofReal_tsum]
  refine tsum_congr fun n => ?_
  rw [qThetaCTerm, qThetaTerm]
  push_cast
  ring

lemma norm_qThetaCTerm (P : ℝ) (hP : 0 < P) (w : ℂ) (n : ℤ) :
    ‖qThetaCTerm P w n‖ = qThetaTerm P ‖w‖ n := by
  rw [qThetaCTerm, qThetaTerm, norm_mul, norm_zpow, norm_zpow, Complex.norm_real,
      Real.norm_eq_abs, abs_of_pos hP]

/-- On `r ≤ ‖w‖ ≤ R` the terms are dominated by `qThetaTerm P R n + qThetaTerm P r n`,
which is summable — the Weierstrass majorant. -/
lemma norm_le_annulus (P r R : ℝ) (hP : 0 < P) (hr : 0 < r) (w : ℂ)
    (hw1 : r ≤ ‖w‖) (hw2 : ‖w‖ ≤ R) (n : ℤ) :
    ‖qThetaCTerm P w n‖ ≤ qThetaTerm P R n + qThetaTerm P r n := by
  have hw0 : (0:ℝ) < ‖w‖ := lt_of_lt_of_le hr hw1
  have hR : (0:ℝ) < R := lt_of_lt_of_le hw0 hw2
  have key : ‖w‖ ^ n ≤ R ^ n + r ^ n := by
    rw [zpow_eq_exp _ hw0, zpow_eq_exp _ hR, zpow_eq_exp _ hr]
    have hlr : Real.log r ≤ Real.log ‖w‖ := Real.log_le_log hr hw1
    have hlR : Real.log ‖w‖ ≤ Real.log R := Real.log_le_log hw0 hw2
    rcases le_or_gt 0 n with hn | hn
    · have hcast : (0:ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
      have h1 : Real.log ‖w‖ * (n:ℝ) ≤ Real.log R * (n:ℝ) := by nlinarith
      have h2 := Real.exp_le_exp.mpr h1
      nlinarith [Real.exp_pos (Real.log r * (n:ℝ))]
    · have hcast : ((n : ℝ)) ≤ 0 := by exact_mod_cast hn.le
      have h1 : Real.log ‖w‖ * (n:ℝ) ≤ Real.log r * (n:ℝ) := by nlinarith
      have h2 := Real.exp_le_exp.mpr h1
      nlinarith [Real.exp_pos (Real.log R * (n:ℝ))]
  rw [norm_qThetaCTerm P hP w n, qThetaTerm, qThetaTerm, qThetaTerm]
  have hPpos : (0:ℝ) < P ^ (-(n * (n + 1))) := zpow_pos hP _
  nlinarith [key, hPpos]

/-- **`θ_P` is holomorphic on `ℂ*`.**

Partial sums are finite sums of `c·wⁿ`, differentiable off `0`; on any annulus
`r < ‖w‖ < R` the Weierstrass M-test gives locally uniform convergence, and
`TendstoLocallyUniformlyOn.differentiableOn` transfers differentiability to the
limit. This is what makes `θ_P` a genuine analytic object rather than a formal
`tsum`, and it is the prerequisite for talking about its divisor at all. -/
theorem differentiableOn_qThetaC (P : ℝ) (hP : 1 < P) :
    DifferentiableOn ℂ (qThetaC P) {(0:ℂ)}ᶜ := by
  have hP0 : (0:ℝ) < P := lt_trans zero_lt_one hP
  intro w₀ hw₀
  have hw₀0 : w₀ ≠ 0 := hw₀
  have hn0 : (0:ℝ) < ‖w₀‖ := norm_pos_iff.mpr hw₀0
  set r := ‖w₀‖ / 2 with hrdef
  set R := 2 * ‖w₀‖ with hRdef
  have hr : (0:ℝ) < r := by positivity
  set U : Set ℂ := {w : ℂ | r < ‖w‖ ∧ ‖w‖ < R} with hUdef
  have hUopen : IsOpen U := by
    have : U = (fun w : ℂ => ‖w‖) ⁻¹' (Set.Ioo r R) := by
      ext w; simp [hUdef, Set.mem_Ioo]
    rw [this]; exact isOpen_Ioo.preimage continuous_norm
  have hw₀U : w₀ ∈ U := by
    constructor
    · simp only [hrdef]; linarith
    · simp only [hRdef]; linarith
  have hsum : Summable (fun n : ℤ => qThetaTerm P R n + qThetaTerm P r n) :=
    (summable_qThetaTerm P R hP (by positivity)).add
      (summable_qThetaTerm P r hP (by positivity))
  have hbound : ∀ (n : ℤ), ∀ w ∈ U, ‖qThetaCTerm P w n‖
      ≤ qThetaTerm P R n + qThetaTerm P r n := by
    intro n w hw
    exact norm_le_annulus P r R hP0 hr w hw.1.le hw.2.le n
  have htu := tendstoUniformlyOn_tsum hsum hbound
  have hdiff : ∀ (t : Finset ℤ),
      DifferentiableOn ℂ (fun w : ℂ => ∑ n ∈ t, qThetaCTerm P w n) U := by
    intro t
    have : (fun w : ℂ => ∑ n ∈ t, qThetaCTerm P w n)
        = ∑ n ∈ t, (fun w : ℂ => qThetaCTerm P w n) := by funext w; simp
    rw [this]
    refine DifferentiableOn.sum ?_
    intro n _ w hw
    have hwne : w ≠ 0 := by
      intro h; rw [h] at hw; simp [hUdef] at hw; linarith [hw.1]
    exact DifferentiableAt.differentiableWithinAt
      ((differentiableAt_zpow.mpr (Or.inl hwne)).const_mul _)
  have hres : DifferentiableOn ℂ (qThetaC P) U :=
    htu.tendstoLocallyUniformlyOn.differentiableOn
      (Filter.Eventually.of_forall hdiff) hUopen
  exact ((hres.differentiableAt (hUopen.mem_nhds hw₀U))).differentiableWithinAt

/-! ### The `+1` per period — the mechanism that counts the zeros

The three results below are the **entire** input to "exactly one zero per
fundamental annulus" other than the argument principle itself. See the
`## What this file does NOT prove` note above for why that matters: it is what
takes the Jacobi triple product off the critical path. -/

/-- **The functional equation over `ℂ`**, `θ_P(P²w) = w·θ_P(w)`.

Same proof as the real `qTheta_functional_equation`, re-run over `ℂ` because
everything analytic downstream (`deriv`, contour integrals) needs the complex
argument. -/
theorem qThetaC_functional_equation (P : ℝ) (hP : 0 < P) (w : ℂ) (hw : w ≠ 0) :
    qThetaC P ((P : ℂ) ^ (2:ℤ) * w) = w * qThetaC P w := by
  have hP0 : ((P : ℂ)) ≠ 0 := by exact_mod_cast hP.ne'
  have hleft : ∀ n : ℤ,
      qThetaCTerm P ((P : ℂ) ^ (2:ℤ) * w) n = (P : ℂ) ^ (-(n * (n - 1))) * w ^ n := by
    intro n
    rw [qThetaCTerm, mul_zpow, ← zpow_mul, ← mul_assoc, ← zpow_add₀ hP0]
    congr 2
    ring
  have hright : ∀ n : ℤ,
      w * qThetaCTerm P w (n - 1) = (P : ℂ) ^ (-(n * (n - 1))) * w ^ n := by
    intro n
    have hww : w * w ^ (n - 1) = w ^ n := by
      have h := zpow_add₀ hw 1 (n - 1)
      rw [zpow_one, show (1:ℤ) + (n - 1) = n by ring] at h
      exact h.symm
    rw [qThetaCTerm, show -((n - 1) * ((n - 1) + 1)) = -(n * (n - 1)) by ring,
        ← mul_assoc, mul_comm w _, mul_assoc, hww]
  calc qThetaC P ((P : ℂ) ^ (2:ℤ) * w)
      = ∑' n : ℤ, (P : ℂ) ^ (-(n * (n - 1))) * w ^ n := by
        rw [qThetaC_eq_tsum]; exact tsum_congr hleft
    _ = ∑' n : ℤ, w * qThetaCTerm P w (n - 1) := (tsum_congr hright).symm
    _ = w * ∑' n : ℤ, qThetaCTerm P w (n - 1) := by rw [tsum_mul_left]
    _ = w * qThetaC P w := by
        rw [qThetaC_eq_tsum]
        congr 1
        exact (Equiv.subRight (1:ℤ)).tsum_eq (fun n => qThetaCTerm P w n)

/-- **The functional equation, differentiated**: `p·θ'(pw) = θ(w) + w·θ'(w)`
(with `p = P²`).

Legitimate only because `differentiableOn_qThetaC` is available: the identity
`θ_P(P²w) = w·θ_P(w)` holds on `ℂ*`, which is open, so the two sides agree on a
neighbourhood of every `w ≠ 0` and their derivatives agree there. Without
holomorphy there is nothing to differentiate. -/
theorem deriv_qThetaC_functional_equation (P : ℝ) (hP : 1 < P) (w : ℂ) (hw : w ≠ 0) :
    (P : ℂ) ^ (2:ℤ) * deriv (qThetaC P) ((P : ℂ) ^ (2:ℤ) * w)
      = qThetaC P w + w * deriv (qThetaC P) w := by
  have hP0 : (0:ℝ) < P := lt_trans zero_lt_one hP
  have hPc : ((P : ℂ)) ≠ 0 := by exact_mod_cast hP0.ne'
  set c : ℂ := (P : ℂ) ^ (2:ℤ) with hcdef
  have hc : c ≠ 0 := zpow_ne_zero _ hPc
  have hcw : c * w ≠ 0 := mul_ne_zero hc hw
  have hdiff : ∀ z : ℂ, z ≠ 0 → DifferentiableAt ℂ (qThetaC P) z := fun z hz =>
    (differentiableOn_qThetaC P hP).differentiableAt
      (isOpen_compl_singleton.mem_nhds (by simpa using hz))
  have hlin : HasDerivAt (fun z : ℂ => c * z) c w := by
    simpa using (hasDerivAt_id w).const_mul c
  have h1 : HasDerivAt (fun z : ℂ => qThetaC P (c * z))
      (c * deriv (qThetaC P) (c * w)) w := by
    have h := ((hdiff (c * w) hcw).hasDerivAt).comp w hlin
    simp only [Function.comp_def] at h
    rwa [mul_comm (deriv (qThetaC P) (c * w)) c] at h
  have h2 : HasDerivAt (fun z : ℂ => z * qThetaC P z)
      (qThetaC P w + w * deriv (qThetaC P) w) w := by
    simpa using (hasDerivAt_id w).mul ((hdiff w hw).hasDerivAt)
  have hEq : (fun z : ℂ => z * qThetaC P z) =ᶠ[nhds w] (fun z : ℂ => qThetaC P (c * z)) := by
    filter_upwards [isOpen_compl_singleton.mem_nhds (show w ∈ ({(0:ℂ)}ᶜ) by simpa using hw)]
      with z hz
    exact (qThetaC_functional_equation P hP0 z (by simpa using hz)).symm
  exact (h1.congr_of_eventuallyEq hEq).unique h2

/-- **The `+1`.** The logarithmic derivative gains exactly `1/w` per period:

    p·θ'(pw)/θ(pw)  =  1/w + θ'(w)/θ(w),   p = P².

This is the whole zero-counting mechanism in one line. Integrating over
`|w| = ρ` and substituting `w ↦ pw` turns the `1/w` into `2πi`, so the winding
number of `θ_p` on `|w| = pρ` is exactly **one more** than on `|w| = ρ`.
The argument principle reads that off as *exactly one zero, counted with
multiplicity, in every fundamental annulus*, which with
`qTheta_neg_zpow_eq_zero` pins that zero at `−p^k` and makes it simple. That
inference is taken in `QOU/QBeta/C1ThetaZeroLocus.lean`
(`qThetaC_eq_zero_iff`). -/
theorem logDeriv_qThetaC_functional_equation (P : ℝ) (hP : 1 < P) (w : ℂ)
    (hw : w ≠ 0) (hθ : qThetaC P w ≠ 0) :
    (P : ℂ) ^ (2:ℤ) * deriv (qThetaC P) ((P : ℂ) ^ (2:ℤ) * w)
        / qThetaC P ((P : ℂ) ^ (2:ℤ) * w)
      = 1 / w + deriv (qThetaC P) w / qThetaC P w := by
  have hP0 : (0:ℝ) < P := lt_trans zero_lt_one hP
  rw [qThetaC_functional_equation P hP0 w hw,
      deriv_qThetaC_functional_equation P hP w hw]
  field_simp

/-! ### The `+1`, at the level of contours

`logDeriv_qThetaC_functional_equation` says the *integrand* gains `1/w` per
period. These three turn that into a statement about the *integral*, which is
the form the argument principle consumes. -/

/-- **Scaling a circle contour.** `∮_{|z| = aR} f = ∮_{|z| = R} a·f(a·z)`.

Immediate from the definition — `circleMap 0 (aR) θ = a · circleMap 0 R θ` —
but Mathlib has no change-of-variables for `circleIntegral`, so it is proved
here. Stated for its own sake: nothing about `θ_P` enters. -/
theorem circleIntegral_scale (f : ℂ → ℂ) (a R : ℝ) :
    (∮ z in C((0:ℂ), a * R), f z)
      = ∮ z in C((0:ℂ), R), (a : ℂ) * f ((a : ℂ) * z) := by
  simp only [circleIntegral, deriv_circleMap, circleMap, zero_add, smul_eq_mul,
             Complex.ofReal_mul]
  refine intervalIntegral.integral_congr fun θ _ => ?_
  ring_nf

/-- **A `1/w` in the integrand is a `2πi` in the integral.**

Abstracted away from `θ_P`: any `g` that is circle-integrable on `|z| = R` and
satisfies `a·g(a z) = 1/z + g(z)` on that circle has
`∮_{|z| = aR} g = 2πi + ∮_{|z| = R} g`. The `2πi` is
`circleIntegral.integral_sub_center_inv`; the hypothesis `hstep` is exactly
what the logarithmic-derivative functional equation supplies. -/
theorem winding_step (g : ℂ → ℂ) (a R : ℝ) (hR : 0 < R)
    (hint : CircleIntegrable g 0 R)
    (hstep : ∀ z : ℂ, ‖z‖ = R → (a : ℂ) * g ((a : ℂ) * z) = z⁻¹ + g z) :
    (∮ z in C((0:ℂ), a * R), g z)
      = 2 * Real.pi * Complex.I + ∮ z in C((0:ℂ), R), g z := by
  rw [circleIntegral_scale]
  have hRne : R ≠ 0 := ne_of_gt hR
  have hcongr : (∮ z in C((0:ℂ), R), (a : ℂ) * g ((a : ℂ) * z))
      = ∮ z in C((0:ℂ), R), (z⁻¹ + g z) := by
    refine circleIntegral.integral_congr hR.le fun z hz => ?_
    exact hstep z (by simpa [Complex.dist_eq] using hz)
  rw [hcongr]
  have h0 : (0:ℂ) ∉ Metric.sphere (0:ℂ) |R| := by
    simp only [Metric.mem_sphere, dist_self]
    exact fun h => hRne (abs_eq_zero.mp h.symm)
  have hinv : CircleIntegrable (fun z : ℂ => z⁻¹) 0 R := by
    simpa using
      (circleIntegrable_sub_zpow_iff (c := (0:ℂ)) (w := (0:ℂ)) (R := R) (n := -1)).2
        (Or.inr (Or.inr h0))
  rw [circleIntegral.integral_add hinv hint]
  congr 1
  simpa using circleIntegral.integral_sub_center_inv (0:ℂ) hRne

/-- **The winding number of `θ_P` rises by exactly one per period.**

    ∮_{|z| = pρ} θ'/θ dz  =  2πi  +  ∮_{|z| = ρ} θ'/θ dz,     p = P².

The only hypothesis beyond `ρ > 0` is that `θ_P` has no zero on `|z| = ρ` —
unavoidable, since otherwise the integrand is not defined there, and harmless,
since the radius is ours to choose.

The argument principle reads the left-hand side minus the right as *the number
of zeros, with multiplicity, in the annulus `ρ < |z| < pρ`*, hence exactly one;
`qTheta_neg_zpow_eq_zero` supplies that zero at `−p^k`, making it simple and the
only one, so the zero set is exactly `−p^ℤ` and the C1 pole divisor is exact
rather than `⊇`. That is `QOU/QBeta/C1ThetaZeroLocus.lean`, which consumes this
theorem: `qThetaC_eq_zero_iff` and `qThetaC_analyticOrderAt_neg_zpow`.

Checked numerically at our substrate in
`computations/qbeta/c3_w2_c1_theta_zero_count.py`. -/
theorem qTheta_winding_step (P : ℝ) (hP : 1 < P) (ρ : ℝ) (hρ : 0 < ρ)
    (hne : ∀ z : ℂ, ‖z‖ = ρ → qThetaC P z ≠ 0) :
    (∮ z in C((0:ℂ), P ^ 2 * ρ), deriv (qThetaC P) z / qThetaC P z)
      = 2 * Real.pi * Complex.I
        + ∮ z in C((0:ℂ), ρ), deriv (qThetaC P) z / qThetaC P z := by
  have hop : IsOpen ({(0:ℂ)}ᶜ) := isOpen_compl_singleton
  have hA : AnalyticOnNhd ℂ (qThetaC P) {(0:ℂ)}ᶜ :=
    (differentiableOn_qThetaC P hP).analyticOnNhd hop
  have hdD : DifferentiableOn ℂ (deriv (qThetaC P)) {(0:ℂ)}ᶜ :=
    (hA.deriv).differentiableOn
  have hsub : Metric.sphere (0:ℂ) ρ ⊆ {(0:ℂ)}ᶜ := by
    intro z hz
    simp only [Metric.mem_sphere, dist_zero_right] at hz
    simp only [Set.mem_compl_iff, Set.mem_singleton_iff]
    intro h
    rw [h] at hz
    simp only [norm_zero] at hz
    exact (ne_of_gt hρ) hz.symm
  have hnesph : ∀ z ∈ Metric.sphere (0:ℂ) ρ, qThetaC P z ≠ 0 := fun z hz =>
    hne z (by simpa [dist_zero_right] using hz)
  have hcont : ContinuousOn (fun z : ℂ => deriv (qThetaC P) z / qThetaC P z)
      (Metric.sphere (0:ℂ) ρ) :=
    ((hdD.continuousOn).mono hsub).div
      ((hA.differentiableOn.continuousOn).mono hsub) hnesph
  have hint : CircleIntegrable (fun z : ℂ => deriv (qThetaC P) z / qThetaC P z) 0 ρ :=
    hcont.circleIntegrable hρ.le
  have hcast : ((P ^ 2 : ℝ) : ℂ) = (P : ℂ) ^ (2:ℤ) := by
    rw [zpow_two]; push_cast; ring
  refine winding_step _ (P ^ 2) ρ hρ hint ?_
  intro z hz
  have hz0 : z ≠ 0 := by
    intro h; rw [h] at hz; simp at hz; exact (ne_of_gt hρ) hz.symm
  have h := logDeriv_qThetaC_functional_equation P hP z hz0 (hne z hz)
  rw [hcast]
  rw [← mul_div_assoc, h, one_div]

/-! ### The argument principle on an annulus

`qTheta_winding_step` above produces the contour identity; this section proves
the inference that consumes it, in the form Mathlib does not have — for a
function presented as `(∏ (·−a)^{m a})·u`. The *existence* of that presentation
for an analytic function is `QOU.Mathlib.exists_finset_factorisation`.

Everything below is `θ`-free and upstreamable. -/

section ArgumentPrinciple

open Metric

/-- `∮_{|z|=R} (z−a)⁻¹ dz = 2πi` when `a` is inside the circle. -/
theorem integral_inv_sub_inside (a : ℂ) (R : ℝ) (ha : ‖a‖ < R) :
    (∮ z in C((0:ℂ), R), (z - a)⁻¹) = 2 * Real.pi * Complex.I := by
  refine circleIntegral.integral_sub_inv_of_mem_ball ?_
  simpa [Complex.dist_eq] using ha

/-- `∮_{|z|=R} (z−a)⁻¹ dz = 0` when `a` is outside the circle. -/
theorem integral_inv_sub_outside (a : ℂ) (R : ℝ) (hR : 0 ≤ R) (ha : R < ‖a‖) :
    (∮ z in C((0:ℂ), R), (z - a)⁻¹) = 0 := by
  have hne : ∀ z ∈ closedBall (0:ℂ) R, z - a ≠ 0 := by
    intro z hz h
    rw [sub_eq_zero] at h
    subst h
    simp only [mem_closedBall, Complex.dist_eq, sub_zero] at hz
    linarith
  refine Complex.circleIntegral_eq_zero_of_differentiable_on_off_countable
    hR Set.countable_empty ?_ ?_
  · exact ContinuousOn.inv₀ (by fun_prop) hne
  · intro z hz
    refine DifferentiableAt.inv (by fun_prop) (hne z ?_)
    exact ball_subset_closedBall hz.1

/-- `logDeriv` of `(· − a)^m · u` splits as `m/(z−a) + logDeriv u`. -/
theorem logDeriv_pow_sub_mul (u : ℂ → ℂ) (a : ℂ) (m : ℕ) (z : ℂ)
    (hz : z ≠ a) (hu : DifferentiableAt ℂ u z) (hun : u z ≠ 0) :
    logDeriv (fun w => (w - a) ^ m * u w) z = m * (z - a)⁻¹ + logDeriv u z := by
  have hsub : DifferentiableAt ℂ (fun w : ℂ => w - a) z := by fun_prop
  have hsubne : (z - a) ≠ 0 := sub_ne_zero.mpr hz
  have hpow : DifferentiableAt ℂ (fun w : ℂ => (w - a) ^ m) z := hsub.pow m
  have hpowne : ((z - a) ^ m) ≠ 0 := pow_ne_zero _ hsubne
  rw [logDeriv_mul z hpowne hun hpow hu, logDeriv_fun_pow hsub m]
  congr 1
  rw [logDeriv_apply]
  have : deriv (fun w : ℂ => w - a) z = 1 := by
    simpa using (hasDerivAt_id z).sub_const a |>.deriv
  rw [this, one_div]

/-- **Argument principle on an annulus, for a single zero of known order.**

If `f = (· − a)^m · u` with `u` analytic and non-vanishing on an open `A`
containing the closed annulus `r ≤ ‖z‖ ≤ R`, and the zero `a` lies strictly
inside the annulus, then the winding difference is exactly `m`:

    ∮_{|z|=R} f'/f  −  ∮_{|z|=r} f'/f  =  m · 2πi.

The `u'/u` part cancels by the annulus Cauchy theorem; the `m/(z−a)` part
contributes `2πi` on the outer circle (Cauchy) and `0` on the inner (holomorphic
in the disc). -/
theorem argumentPrinciple_annulus_single (u : ℂ → ℂ) (a : ℂ) (m : ℕ) {A : Set ℂ}
    (r R : ℝ) (hr : 0 < r) (hrR : r < R)
    (hAopen : IsOpen A) (hAsub : closedBall (0:ℂ) R \ ball (0:ℂ) r ⊆ A)
    (hu : AnalyticOnNhd ℂ u A) (hune : ∀ z ∈ A, u z ≠ 0)
    (har : r < ‖a‖) (haR : ‖a‖ < R) :
    (∮ z in C((0:ℂ), R), deriv (fun w => (w - a) ^ m * u w) z
        / ((fun w => (w - a) ^ m * u w) z))
      - (∮ z in C((0:ℂ), r), deriv (fun w => (w - a) ^ m * u w) z
        / ((fun w => (w - a) ^ m * u w) z))
      = (m : ℂ) * (2 * Real.pi * Complex.I) := by
  set f : ℂ → ℂ := fun w => (w - a) ^ m * u w with hf
  set L : ℂ → ℂ := fun z => deriv u z / u z with hL
  have hR0 : (0:ℝ) < R := lt_trans hr hrR
  -- `u'/u` is continuous on `A`
  have hdu : DifferentiableOn ℂ (deriv u) A := (hu.deriv).differentiableOn
  have hLcont : ContinuousOn L A :=
    (hdu.continuousOn).div (hu.differentiableOn.continuousOn) hune
  -- the two spheres sit in `A`
  have hsphR : sphere (0:ℂ) R ⊆ A := by
    refine subset_trans ?_ hAsub
    intro z hz
    simp only [mem_sphere, Complex.dist_eq, sub_zero] at hz
    exact ⟨by simp [Complex.dist_eq, hz], by simp [Complex.dist_eq, hz]; linarith⟩
  have hsphr : sphere (0:ℂ) r ⊆ A := by
    refine subset_trans ?_ hAsub
    intro z hz
    simp only [mem_sphere, Complex.dist_eq, sub_zero] at hz
    exact ⟨by simp [Complex.dist_eq, hz]; linarith, by simp [Complex.dist_eq, hz]⟩
  -- pointwise: `f'/f = m/(z−a) + u'/u` on each sphere
  have hsplit : ∀ ρ : ℝ, sphere (0:ℂ) ρ ⊆ A → ρ ≠ ‖a‖ →
      ∀ z ∈ sphere (0:ℂ) ρ, deriv f z / f z = (m : ℂ) * (z - a)⁻¹ + L z := by
    intro ρ hρA hρa z hz
    have hzA : z ∈ A := hρA hz
    have hza : z ≠ a := by
      intro h; subst h
      simp only [mem_sphere, Complex.dist_eq, sub_zero] at hz
      exact hρa hz.symm
    have hud : DifferentiableAt ℂ u z := (hu z hzA).differentiableAt
    have := logDeriv_pow_sub_mul u a m z hza hud (hune z hzA)
    rwa [logDeriv_apply, logDeriv_apply] at this
  -- integrability
  have hLint : ∀ ρ : ℝ, 0 ≤ ρ → sphere (0:ℂ) ρ ⊆ A → CircleIntegrable L 0 ρ :=
    fun ρ hρ hρA => (hLcont.mono hρA).circleIntegrable hρ
  have hIint : ∀ ρ : ℝ, 0 ≤ ρ → ρ ≠ ‖a‖ →
      CircleIntegrable (fun z : ℂ => (m : ℂ) * (z - a)⁻¹) 0 ρ := by
    intro ρ hρ0 hρa
    have h0 : a ∉ sphere (0:ℂ) |ρ| := by
      simp only [mem_sphere, Complex.dist_eq, sub_zero]
      intro h
      rw [abs_of_nonneg hρ0] at h
      exact hρa h.symm
    have := (circleIntegrable_sub_zpow_iff (c := (0:ℂ)) (w := a) (R := ρ) (n := -1)).2
      (Or.inr (Or.inr h0))
    simpa using this.const_mul (m : ℂ)
  -- assemble
  have hRne : R ≠ ‖a‖ := by linarith
  have hrne : r ≠ ‖a‖ := by linarith
  have hbig : ∀ ρ : ℝ, 0 ≤ ρ → sphere (0:ℂ) ρ ⊆ A → ρ ≠ ‖a‖ →
      (∮ z in C((0:ℂ), ρ), deriv f z / f z)
        = (m : ℂ) * (∮ z in C((0:ℂ), ρ), (z - a)⁻¹) + ∮ z in C((0:ℂ), ρ), L z := by
    intro ρ hρ0 hρA hρa
    rw [circleIntegral.integral_congr hρ0 (hsplit ρ hρA hρa),
        circleIntegral.integral_add (hIint ρ hρ0 hρa) (hLint ρ hρ0 hρA),
        circleIntegral.integral_const_mul]
  rw [hbig R hR0.le hsphR hRne, hbig r hr.le hsphr hrne,
      integral_inv_sub_inside a R haR, integral_inv_sub_outside a r hr.le har]
  -- the `u'/u` circle integrals agree, by the annulus Cauchy theorem
  have hcancel : (∮ z in C((0:ℂ), R), L z) = ∮ z in C((0:ℂ), r), L z := by
    refine Complex.circleIntegral_eq_of_differentiable_on_annulus_off_countable
      hr hrR.le Set.countable_empty (hLcont.mono hAsub) ?_
    intro z hz
    have hzA : z ∈ A := hAsub ⟨ball_subset_closedBall hz.1.1,
      fun h => hz.1.2 (ball_subset_closedBall h)⟩
    exact ((hdu z hzA).differentiableAt (hAopen.mem_nhds hzA)).div
      ((hu z hzA).differentiableAt) (hune z hzA)
  rw [hcancel]
  ring

/-- **The C1 payoff: any factorised zero in a fundamental annulus is SIMPLE.**

Compose `qTheta_winding_step` (winding difference `= 2πi`) with
`argumentPrinciple_annulus_single` (winding difference `= m·2πi`): the
multiplicity is forced to `1`.

So *conditional only on `θ_P` admitting a factorisation `(·−a)^m·u` on the
annulus with `u` analytic and non-vanishing* — the classical finiteness fact,
not an extra assumption about `θ_P` — the zero in each fundamental annulus is
simple. Together with `qTheta_neg_zpow_eq_zero`, which puts a zero at `−p^k`,
that zero **is** `−p^k` and there is no other: the converse zero locus.

The remaining gap is therefore exactly the existence of the factorisation, and
nothing else. -/
theorem multiplicity_eq_one_of_winding_step (u : ℂ → ℂ) (a : ℂ) (m : ℕ) {A : Set ℂ}
    (r R : ℝ) (hr : 0 < r) (hrR : r < R)
    (hAopen : IsOpen A) (hAsub : Metric.closedBall (0:ℂ) R \ Metric.ball (0:ℂ) r ⊆ A)
    (hu : AnalyticOnNhd ℂ u A) (hune : ∀ z ∈ A, u z ≠ 0)
    (har : r < ‖a‖) (haR : ‖a‖ < R)
    (hwind : (∮ z in C((0:ℂ), R), deriv (fun w => (w - a) ^ m * u w) z
                / ((fun w => (w - a) ^ m * u w) z))
              - (∮ z in C((0:ℂ), r), deriv (fun w => (w - a) ^ m * u w) z
                / ((fun w => (w - a) ^ m * u w) z))
            = 2 * Real.pi * Complex.I) :
    m = 1 := by
  have hap := argumentPrinciple_annulus_single u a m r R hr hrR hAopen hAsub hu hune har haR
  rw [hwind] at hap
  have hne : (2 * (Real.pi : ℂ) * Complex.I) ≠ 0 := by
    have : (Real.pi : ℂ) ≠ 0 := by
      exact_mod_cast Real.pi_ne_zero
    simp [this, Complex.I_ne_zero]
  have : ((m : ℂ) - 1) * (2 * Real.pi * Complex.I) = 0 := by
    rw [sub_mul, one_mul, ← hap]; ring
  have hm : (m : ℂ) = 1 := by
    rcases mul_eq_zero.mp this with h | h
    · exact sub_eq_zero.mp h
    · exact absurd h hne
  exact_mod_cast hm

/-- Pointwise split of the logarithmic derivative of a finite product of powers
times a non-vanishing factor. -/
theorem logDeriv_prod_pow_sub_mul (u : ℂ → ℂ) (S : Finset ℂ) (m : ℂ → ℕ) (z : ℂ)
    (hz : ∀ a ∈ S, z ≠ a) (hu : DifferentiableAt ℂ u z) (hun : u z ≠ 0) :
    logDeriv (fun w => (∏ a ∈ S, (w - a) ^ (m a)) * u w) z
      = (∑ a ∈ S, (m a : ℂ) * (z - a)⁻¹) + logDeriv u z := by
  have hne : ∀ a ∈ S, ((z - a) ^ (m a)) ≠ 0 :=
    fun a ha => pow_ne_zero _ (sub_ne_zero.mpr (hz a ha))
  have hd : ∀ a ∈ S, DifferentiableAt ℂ (fun w : ℂ => (w - a) ^ (m a)) z :=
    fun a _ => (by fun_prop : DifferentiableAt ℂ (fun w : ℂ => w - a) z).pow _
  have hprodne : (∏ a ∈ S, (z - a) ^ (m a)) ≠ 0 := Finset.prod_ne_zero_iff.mpr hne
  have hprodd : DifferentiableAt ℂ (fun w : ℂ => ∏ a ∈ S, (w - a) ^ (m a)) z :=
    DifferentiableAt.fun_finset_prod (fun a ha => hd a ha)
  rw [logDeriv_mul z hprodne hun hprodd hu, logDeriv_prod S _ z hne hd]
  congr 1
  refine Finset.sum_congr rfl fun a ha => ?_
  rw [logDeriv_fun_pow (by fun_prop : DifferentiableAt ℂ (fun w : ℂ => w - a) z)]
  have : logDeriv (fun w : ℂ => w - a) z = (z - a)⁻¹ := by
    rw [logDeriv_apply]
    simp
  rw [this]


/-- **The argument principle on an annulus, `Finset`-indexed**, with the factors
allowed to sit anywhere off the two contours.

For `F = (∏ a ∈ S, (·−a)^{m a})·u` with `u` analytic and non-vanishing on a
neighbourhood of the closed annulus, the winding difference counts *exactly the
factors between the two circles*, with multiplicity. A factor inside the inner
circle contributes `2πi` to both integrals and cancels; one outside the outer
circle contributes to neither.

The weaker hypothesis is what the θ instantiation needs. A factorisation
obtained from `MeromorphicOn.extract_zeros_poles` is analytic on an *open* set,
which must therefore be strictly larger than the closed contour annulus — so its
zero set can spill into the two collars, and demanding `r < ‖a‖ < R` for every
`a ∈ S` would be a hypothesis one cannot discharge without first proving the
collars zero-free. Counting with a filter removes the need entirely. -/
theorem argumentPrinciple_annulus_filter (u : ℂ → ℂ) (S : Finset ℂ) (m : ℂ → ℕ)
    {A : Set ℂ} (r R : ℝ) (hr : 0 < r) (hrR : r < R)
    (hAopen : IsOpen A) (hAsub : Metric.closedBall (0:ℂ) R \ Metric.ball (0:ℂ) r ⊆ A)
    (hu : AnalyticOnNhd ℂ u A) (hune : ∀ z ∈ A, u z ≠ 0)
    (hS : ∀ a ∈ S, ‖a‖ ≠ r ∧ ‖a‖ ≠ R) :
    (∮ z in C((0:ℂ), R), deriv (fun w => (∏ a ∈ S, (w - a) ^ (m a)) * u w) z
        / ((∏ a ∈ S, (z - a) ^ (m a)) * u z))
      - (∮ z in C((0:ℂ), r), deriv (fun w => (∏ a ∈ S, (w - a) ^ (m a)) * u w) z
        / ((∏ a ∈ S, (z - a) ^ (m a)) * u z))
      = (∑ a ∈ S.filter (fun a => r < ‖a‖ ∧ ‖a‖ < R), (m a : ℂ))
          * (2 * Real.pi * Complex.I) := by
  classical
  set F : ℂ → ℂ := fun w => (∏ a ∈ S, (w - a) ^ (m a)) * u w with hF
  set L : ℂ → ℂ := fun z => deriv u z / u z with hL
  have hR0 : (0:ℝ) < R := lt_trans hr hrR
  have hdu : DifferentiableOn ℂ (deriv u) A := (hu.deriv).differentiableOn
  have hLcont : ContinuousOn L A :=
    (hdu.continuousOn).div (hu.differentiableOn.continuousOn) hune
  have hsphR : Metric.sphere (0:ℂ) R ⊆ A := by
    refine subset_trans ?_ hAsub
    intro z hz
    simp only [Metric.mem_sphere, Complex.dist_eq, sub_zero] at hz
    exact ⟨by simp [Complex.dist_eq, hz], by simp [Complex.dist_eq, hz]; linarith⟩
  have hsphr : Metric.sphere (0:ℂ) r ⊆ A := by
    refine subset_trans ?_ hAsub
    intro z hz
    simp only [Metric.mem_sphere, Complex.dist_eq, sub_zero] at hz
    exact ⟨by simp [Complex.dist_eq, hz]; linarith, by simp [Complex.dist_eq, hz]⟩
  -- pointwise split on each sphere
  have hsplit : ∀ ρ : ℝ, Metric.sphere (0:ℂ) ρ ⊆ A → (∀ a ∈ S, ρ ≠ ‖a‖) →
      ∀ z ∈ Metric.sphere (0:ℂ) ρ,
        deriv F z / F z = (∑ a ∈ S, (m a : ℂ) * (z - a)⁻¹) + L z := by
    intro ρ hρA hρa z hz
    have hzA : z ∈ A := hρA hz
    have hza : ∀ a ∈ S, z ≠ a := by
      intro a ha h
      simp only [Metric.mem_sphere, Complex.dist_eq, sub_zero] at hz
      exact hρa a ha (h ▸ hz).symm
    have hud : DifferentiableAt ℂ u z := (hu z hzA).differentiableAt
    have := logDeriv_prod_pow_sub_mul u S m z hza hud (hune z hzA)
    rwa [logDeriv_apply, logDeriv_apply] at this
  -- integrability of each piece
  have hLint : ∀ ρ : ℝ, 0 ≤ ρ → Metric.sphere (0:ℂ) ρ ⊆ A → CircleIntegrable L 0 ρ :=
    fun ρ hρ hρA => (hLcont.mono hρA).circleIntegrable hρ
  have hIint : ∀ ρ : ℝ, 0 ≤ ρ → ∀ a ∈ S, ρ ≠ ‖a‖ →
      CircleIntegrable (fun z : ℂ => (m a : ℂ) * (z - a)⁻¹) 0 ρ := by
    intro ρ hρ0 a _ hρa
    have h0 : a ∉ Metric.sphere (0:ℂ) |ρ| := by
      simp only [Metric.mem_sphere, Complex.dist_eq, sub_zero]
      intro h
      rw [abs_of_nonneg hρ0] at h
      exact hρa h.symm
    have := (circleIntegrable_sub_zpow_iff (c := (0:ℂ)) (w := a) (R := ρ) (n := -1)).2
      (Or.inr (Or.inr h0))
    simpa using this.const_mul (m a : ℂ)
  have hRne : ∀ a ∈ S, R ≠ ‖a‖ := fun a ha => ((hS a ha).2).symm
  have hrne : ∀ a ∈ S, r ≠ ‖a‖ := fun a ha => ((hS a ha).1).symm
  have hbig : ∀ ρ : ℝ, 0 ≤ ρ → Metric.sphere (0:ℂ) ρ ⊆ A → (∀ a ∈ S, ρ ≠ ‖a‖) →
      (∮ z in C((0:ℂ), ρ), deriv F z / F z)
        = (∑ a ∈ S, (m a : ℂ) * (∮ z in C((0:ℂ), ρ), (z - a)⁻¹))
          + ∮ z in C((0:ℂ), ρ), L z := by
    intro ρ hρ0 hρA hρa
    have hfun : (∑ a ∈ S, fun z : ℂ => (m a : ℂ) * (z - a)⁻¹)
        = fun z : ℂ => ∑ a ∈ S, (m a : ℂ) * (z - a)⁻¹ := by
      funext z; simp [Finset.sum_apply]
    have hint1 : CircleIntegrable (fun z : ℂ => ∑ a ∈ S, (m a : ℂ) * (z - a)⁻¹) 0 ρ :=
      hfun ▸ CircleIntegrable.sum S (fun a ha => hIint ρ hρ0 a ha (hρa a ha))
    rw [circleIntegral.integral_congr hρ0 (hsplit ρ hρA hρa),
        circleIntegral.integral_add hint1 (hLint ρ hρ0 hρA),
        QOU.Mathlib.integral_fun_sum (fun a ha => hIint ρ hρ0 a ha (hρa a ha))]
    congr 1
    exact Finset.sum_congr rfl fun a _ => circleIntegral.integral_const_mul _ _ _ _
  rw [hbig R hR0.le hsphR hRne, hbig r hr.le hsphr hrne]
  -- the `u'/u` integrals cancel by the annulus Cauchy theorem
  have hcancel : (∮ z in C((0:ℂ), R), L z) = ∮ z in C((0:ℂ), r), L z := by
    refine Complex.circleIntegral_eq_of_differentiable_on_annulus_off_countable
      hr hrR.le Set.countable_empty (hLcont.mono hAsub) ?_
    intro z hz
    have hzA : z ∈ A := hAsub ⟨Metric.ball_subset_closedBall hz.1.1,
      fun h => hz.1.2 (Metric.ball_subset_closedBall h)⟩
    exact ((hdu z hzA).differentiableAt (hAopen.mem_nhds hzA)).div
      ((hu z hzA).differentiableAt) (hune z hzA)
  rw [hcancel, add_sub_add_right_eq_sub, ← Finset.sum_sub_distrib,
      Finset.sum_filter, Finset.sum_mul]
  -- term by term: `2πi − 2πi` inside, `2πi − 0` between, `0 − 0` outside
  refine Finset.sum_congr rfl fun a ha => ?_
  rcases lt_trichotomy ‖a‖ r with h | h | h
  · rw [QOU.QBeta.C1Poles.integral_inv_sub_inside a R (by linarith),
        QOU.QBeta.C1Poles.integral_inv_sub_inside a r h,
        if_neg (by rintro ⟨h', -⟩; linarith)]
    ring
  · exact absurd h (hS a ha).1
  · rcases lt_trichotomy ‖a‖ R with h2 | h2 | h2
    · rw [QOU.QBeta.C1Poles.integral_inv_sub_inside a R h2,
          QOU.QBeta.C1Poles.integral_inv_sub_outside a r hr.le h, if_pos ⟨h, h2⟩]
      ring
    · exact absurd h2 (hS a ha).2
    · rw [QOU.QBeta.C1Poles.integral_inv_sub_outside a R (by linarith) h2,
          QOU.QBeta.C1Poles.integral_inv_sub_outside a r hr.le h,
          if_neg (by rintro ⟨-, h'⟩; linarith)]
      ring

/-- **The argument principle on an annulus, `Finset`-indexed** — the special case
of `argumentPrinciple_annulus_filter` where every factor already lies strictly
between the two contours, so the filter is the whole index set. -/
theorem argumentPrinciple_annulus_finset (u : ℂ → ℂ) (S : Finset ℂ) (m : ℂ → ℕ)
    {A : Set ℂ} (r R : ℝ) (hr : 0 < r) (hrR : r < R)
    (hAopen : IsOpen A) (hAsub : Metric.closedBall (0:ℂ) R \ Metric.ball (0:ℂ) r ⊆ A)
    (hu : AnalyticOnNhd ℂ u A) (hune : ∀ z ∈ A, u z ≠ 0)
    (hS : ∀ a ∈ S, r < ‖a‖ ∧ ‖a‖ < R) :
    (∮ z in C((0:ℂ), R), deriv (fun w => (∏ a ∈ S, (w - a) ^ (m a)) * u w) z
        / ((∏ a ∈ S, (z - a) ^ (m a)) * u z))
      - (∮ z in C((0:ℂ), r), deriv (fun w => (∏ a ∈ S, (w - a) ^ (m a)) * u w) z
        / ((∏ a ∈ S, (z - a) ^ (m a)) * u z))
      = (∑ a ∈ S, (m a : ℂ)) * (2 * Real.pi * Complex.I) := by
  classical
  rw [argumentPrinciple_annulus_filter u S m r R hr hrR hAopen hAsub hu hune
        (fun a ha => ⟨(hS a ha).1.ne', (hS a ha).2.ne⟩),
      Finset.filter_true_of_mem hS]

end ArgumentPrinciple

end QOU.QBeta.C1Poles
