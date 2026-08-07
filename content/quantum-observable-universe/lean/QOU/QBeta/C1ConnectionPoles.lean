import Mathlib.Tactic
import Mathlib.Topology.Algebra.InfiniteSum.Ring
import Mathlib.Analysis.SpecialFunctions.Pow.Real

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

`θ_p(w) = 0` for every `w ∈ −p^ℤ` — the `⊇` direction of the zero locus, which
is exactly what is needed to place the poles above.

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
  triple product**, which is not proved here. (Whether Mathlib carries JTP was
  not established — the environment available when this was written had only a
  partial olean cache and no Mathlib source, so its absence there is not
  evidence.) Without the converse one gets "these points *are* zeros", not
  "there are no others".
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

end QOU.QBeta.C1Poles
