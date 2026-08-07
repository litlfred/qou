import Mathlib.Tactic
import Mathlib.Topology.Algebra.InfiniteSum.Ring
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle

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
* `summable_qThetaTerm` — the series converges for `P > 1`, `w ≠ 0`.
* `qTheta_functional_equation` — `θ_P(P²w) = w·θ_P(w)`, i.e. `θ_p(pw) = w θ_p(w)`.
* `qThetaC_conj` / `norm_qThetaC_conj_pair` — `θ_P` commutes with conjugation,
  so the two **conjugate** `0`-side exponents give **exactly equal** magnitudes
  on the real axis. This is the formal core of the refutation the whole C1 arc
  restarted from: a basis putting them "~17 orders of magnitude apart" is
  impossible, not merely unobserved.

`summable_qThetaTerm` and `qTheta_functional_equation` are the **analytic
foundation for the converse**. The vanishing
theorem itself needs neither (see below), but every route to "these are the
*only* zeros" needs `θ_p` to be a genuine analytic object, and the functional
equation is what forces the zero set to be a union of `p`-orbits.

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
  `HasProd`/`Multipliable`/`tprod` (full infinite-product infrastructure) and
  `Analysis/Meromorphic/{Divisor, IsolatedZeros, Order}`. It does **not** have
  the argument principle, which rules out the cheap zero-counting route
  ("`θ_p` is holomorphic on `ℂ*` and `θ_p(pw) = wθ_p(w)` forces exactly one
  zero per fundamental annulus; `−1` is one; done"). So the two viable routes
  are (a) prove the argument principle, or (b) prove JTP via the product side
  — define `∏(1−xᵐ)(1+xᵐw)(1+xᵐ⁻¹w⁻¹)`, show it satisfies the same functional
  equation, and conclude the ratio is elliptic and bounded hence constant. Both
  are substantial; (b) additionally needs Liouville on `ℂ*/p^ℤ`. Neither is a
  small job, and this file's two analytic lemmas above are the shared prefix of
  both. Recorded so this is not re-scoped as cheap.
* **That these zeros are poles of `P`.** That needs the analytic construction
  — convergent `0`-side series, entire `∞`-side series, the matrix inverse and
  its meromorphy — none of which is formalised.
* **Divisor completeness.** The residue-theorem argument (each entry has
  exactly two simple poles per fundamental domain, so residues cancel) lives on
  the multiplicative torus `ℂ*/p^ℤ` and needs elliptic-function theory that
  Mathlib does not have.

Numerically all of the above is checked in the witness
`computations/qbeta/c3-w2-c1-connection-matrix.witness.json` (7/7).

-- Ref: [manuscript] computations/qbeta/c3_w2_c1_connection_matrix.py
-- Ref: [rsz2013] Astérisque 355 §3.3 (Ramis–Sauloy–Zhang)
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

end QOU.QBeta.C1Poles
