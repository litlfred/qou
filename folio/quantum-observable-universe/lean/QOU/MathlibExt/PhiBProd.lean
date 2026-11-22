import Mathlib.Topology.Algebra.InfiniteSum.NatInt
import Mathlib.Topology.Algebra.InfiniteSum.Constructions
import Mathlib.Analysis.SpecialFunctions.Log.Summable
import QOU.MathlibExt.FaddeevQuantumDilogarithm

/-!
# The modular-double product `phiBProd` — a `FaddeevPhi` inhabitant (Im b² > 0)

Discharges the `FaddeevPhi` conjecture-class on the **product-supported
substrate branch**: for `Im b² > 0` (in particular the substrate b-map
`b = √(ln q₀ / 2π)·e^{iπ/4}`, PR #3540) the Faddeev `Φ_b` equals the
modular-double product

$$\Phi_b(z) \;=\; \frac{\prod_{k\ge 0}\bigl(1 + e^{i\pi b^2(2k+1)}e^{2\pi bz}\bigr)}
                       {\prod_{k\ge 0}\bigl(1 + e^{-i\pi b^{-2}(2k+1)}e^{2\pi z/b}\bigr)},$$

verified against the contour integral to `1e-39` at both anchors
(`computations/qbeta/phi-b-substrate-regime.witness.json`, battery S5).  Here
the product is formalized as a `tprod` and **both modular-double shift
equations are proved by index re-shifting** — the infinite-product limit of the
`qPochProd_add` cocycle argument of the finite backbone (PR #3500) — yielding
`FaddeevPhi b (phiBProd b)` under explicit `Multipliable` hypotheses.

**Hypothesis discipline (§3b-cond style).** The two `Multipliable` inputs are
the *analytic* convergence facts (geometric bounds `|q|^k`, `|q̃|^k` for
`Im b² > 0`).  Their Mathlib discharge needs the norm→`Multipliable` bridge
(`Mathlib.Analysis.SpecialFunctions.Complex.LogBounds` cone), which is outside
the current sandbox olean cone — they are therefore carried as **explicit named
hypotheses** on `faddeevPhi_phiBProd`, not axiomatized and not `sorry`'d.  The
algebraic content (factor shift identities + telescoping + the guarded dual
shift) is proved unconditionally.  Route decision + follow-up:
`docs/audits/2026-07-11-phib-lean-route-memo.md`.

-- Ref: [faddeev1995] Faddeev, Lett. Math. Phys. 34 (1995) 249.
--        https://doi.org/10.1007/BF01872779
-- Ref: [leitner2026] docs/audits/2026-07-11-phib-lean-route-memo.md
-/

namespace QOU.MathlibExt.PhiBProd

open Complex
open QOU.MathlibExt.FaddeevQuantumDilogarithm

noncomputable section

/-- Numerator (compact-half) factor `1 + q^{2k+1}·e^{2πbz}`, `q = e^{iπb²}`,
written additively in the exponent. -/
def numFactor (b z : ℂ) (k : ℕ) : ℂ :=
  1 + Complex.exp ((Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1)
        + 2 * (Real.pi : ℂ) * b * z)

/-- Even-exponent variant `1 + q^{2k}·e^{2πbz}` — the numerator family after a
`−ib/2` shift of `z`; its `k = 0` term is the shift prefactor `1 + e^{2πbz}`. -/
def numEven (b z : ℂ) (k : ℕ) : ℂ :=
  1 + Complex.exp ((Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ))
        + 2 * (Real.pi : ℂ) * b * z)

/-- Denominator (modular-dual-half) factor `1 + q̃^{2k+1}·e^{2πz/b}`,
`q̃ = e^{-iπ/b²}`. -/
def denFactor (b z : ℂ) (k : ℕ) : ℂ :=
  1 + Complex.exp (-((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1)
        + 2 * (Real.pi : ℂ) * z / b)

/-- Even-exponent dual variant `1 + q̃^{2k}·e^{2πz/b}`; its `k = 0` term is the
dual shift prefactor `1 + e^{2πz/b}`. -/
def denEven (b z : ℂ) (k : ℕ) : ℂ :=
  1 + Complex.exp (-((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ))
        + 2 * (Real.pi : ℂ) * z / b)

/-- **The modular-double product.**  On `Im b² > 0` both halves converge
geometrically and this equals the Faddeev contour integral (battery S5). -/
def phiBProd (b z : ℂ) : ℂ :=
  (∏' k, numFactor b z k) / (∏' k, denFactor b z k)

end

/-! ## Index shift: `∏' f = f 0 · ∏' f ∘ succ` at monoid level

Mathlib's `Multipliable.tprod_eq_zero_mul` needs `CommGroup`; `ℂ` under `·` is
only a monoid (zero).  The split-off-one-factor identity is rebuilt here from
the `CommMonoid`-level pieces (`tprod_mul_tprod_compl`, `tprod_singleton`,
`Equiv.tprod_eq`). -/

/-- `ℕ ≃ ({0}ᶜ : Set ℕ)` by `k ↦ k + 1`. -/
def succEquivCompl : ℕ ≃ ({0}ᶜ : Set ℕ) where
  toFun k := ⟨k + 1, by simp⟩
  invFun x := x.1 - 1
  left_inv k := by simp
  right_inv x := by
    obtain ⟨n, hn⟩ := x
    have hn0 : n ≠ 0 := by simpa using hn
    exact Subtype.ext (Nat.succ_pred_eq_of_ne_zero hn0)

/-- Split off the `k = 0` factor of a `tprod` over `ℕ`, assuming the shifted
tail is multipliable (monoid-level replacement for `tprod_eq_zero_mul`). -/
theorem tprod_eq_zero_mul_succ {f : ℕ → ℂ} (hf : Multipliable fun k => f (k + 1)) :
    ∏' k, f k = f 0 * ∏' k, f (k + 1) := by
  classical
  have hshift : (fun k : ℕ => f ((succEquivCompl k : ℕ))) = fun k => f (k + 1) := rfl
  have hg : Multipliable fun x : ({0}ᶜ : Set ℕ) => f x := by
    rw [← succEquivCompl.multipliable_iff]
    exact hf
  have hs : Multipliable fun x : ({0} : Set ℕ) => f x :=
    (hasProd_unique _).multipliable
  have key := hs.tprod_mul_tprod_compl hg
  have hsingle : (∏' x : ({0} : Set ℕ), f x) = f 0 := tprod_singleton 0 f
  have hcompl : (∏' x : ({0}ᶜ : Set ℕ), f x) = ∏' k, f (k + 1) := by
    rw [← succEquivCompl.tprod_eq (fun x : ({0}ᶜ : Set ℕ) => f x), hshift]
  rw [hsingle, hcompl] at key
  exact key.symm

/-! ## Factor shift identities (pure exponent algebra) -/

variable {b z : ℂ}

lemma numFactor_shift_down (b z : ℂ) (k : ℕ) :
    numFactor b (z - I * (b / 2)) k = numEven b z k := by
  unfold numFactor numEven
  exact congrArg (fun E => 1 + Complex.exp E) (by ring)

lemma numFactor_shift_up (b z : ℂ) (k : ℕ) :
    numFactor b (z + I * (b / 2)) k = numEven b z (k + 1) := by
  unfold numFactor numEven
  refine congrArg (fun E => 1 + Complex.exp E) ?_
  push_cast
  ring

lemma numEven_zero (b z : ℂ) :
    numEven b z 0 = 1 + Complex.exp (2 * (Real.pi : ℂ) * b * z) := by
  unfold numEven
  refine congrArg (fun E => 1 + Complex.exp E) ?_
  push_cast
  ring

lemma denFactor_shift_b_invariant (hb0 : b ≠ 0) (z : ℂ) (k : ℕ) :
    denFactor b (z - I * (b / 2)) k = denFactor b (z + I * (b / 2)) k := by
  unfold denFactor
  have hminus : -((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * (z - I * (b / 2)) / b
      = (-((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1)
          + 2 * (Real.pi : ℂ) * z / b) + -((Real.pi : ℂ) * I) := by
    field_simp
    ring
  have hplus : -((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * (z + I * (b / 2)) / b
      = (-((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1)
          + 2 * (Real.pi : ℂ) * z / b) + (Real.pi : ℂ) * I := by
    field_simp
    ring
  rw [hminus, hplus]
  simp [Complex.exp_add, Complex.exp_neg, Complex.exp_pi_mul_I]

lemma numFactor_shift_binv_invariant (hb0 : b ≠ 0) (z : ℂ) (k : ℕ) :
    numFactor b (z - I / (2 * b)) k = numFactor b (z + I / (2 * b)) k := by
  unfold numFactor
  have hminus : (Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * b * (z - I / (2 * b))
      = ((Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1)
          + 2 * (Real.pi : ℂ) * b * z) + -((Real.pi : ℂ) * I) := by
    field_simp
    ring
  have hplus : (Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * b * (z + I / (2 * b))
      = ((Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1)
          + 2 * (Real.pi : ℂ) * b * z) + (Real.pi : ℂ) * I := by
    field_simp
    ring
  rw [hminus, hplus]
  simp [Complex.exp_add, Complex.exp_neg, Complex.exp_pi_mul_I]

lemma denFactor_shift_down (hb0 : b ≠ 0) (z : ℂ) (k : ℕ) :
    denFactor b (z - I / (2 * b)) k = denEven b z (k + 1) := by
  unfold denFactor denEven
  refine congrArg (fun E => 1 + Complex.exp E) ?_
  push_cast
  field_simp
  ring

lemma denFactor_shift_up (hb0 : b ≠ 0) (z : ℂ) (k : ℕ) :
    denFactor b (z + I / (2 * b)) k = denEven b z k := by
  unfold denFactor denEven
  refine congrArg (fun E => 1 + Complex.exp E) ?_
  field_simp
  ring

lemma denEven_zero (b z : ℂ) :
    denEven b z 0 = 1 + Complex.exp (2 * (Real.pi : ℂ) * z / b) := by
  unfold denEven
  refine congrArg (fun E => 1 + Complex.exp E) ?_
  push_cast
  ring

/-! ## Telescoped product identities -/

/-- Numerator telescoping under the `b`-shift: the `−ib/2` product carries one
extra factor — exactly the shift prefactor. -/
theorem tprod_num_shift (b z : ℂ)
    (hmul : Multipliable (numFactor b (z + I * (b / 2)))) :
    (∏' k, numFactor b (z - I * (b / 2)) k)
      = (1 + Complex.exp (2 * (Real.pi : ℂ) * b * z))
        * ∏' k, numFactor b (z + I * (b / 2)) k := by
  have hdown : (fun k => numFactor b (z - I * (b / 2)) k) = numEven b z :=
    funext (numFactor_shift_down b z)
  have hup : (fun k => numFactor b (z + I * (b / 2)) k)
      = fun k => numEven b z (k + 1) := funext (numFactor_shift_up b z)
  have hmul' : Multipliable fun k => numEven b z (k + 1) := hup ▸ hmul
  calc (∏' k, numFactor b (z - I * (b / 2)) k)
      = ∏' k, numEven b z k := by rw [hdown]
    _ = numEven b z 0 * ∏' k, numEven b z (k + 1) := tprod_eq_zero_mul_succ hmul'
    _ = (1 + Complex.exp (2 * (Real.pi : ℂ) * b * z))
        * ∏' k, numFactor b (z + I * (b / 2)) k := by rw [numEven_zero, hup]

/-- Denominator telescoping under the `1/b`-shift: the `+i/(2b)` product
carries the extra dual prefactor. -/
theorem tprod_den_shift (hb0 : b ≠ 0) (z : ℂ)
    (hmul : Multipliable (denFactor b (z - I / (2 * b)))) :
    (∏' k, denFactor b (z + I / (2 * b)) k)
      = (1 + Complex.exp (2 * (Real.pi : ℂ) * z / b))
        * ∏' k, denFactor b (z - I / (2 * b)) k := by
  have hdown : (fun k => denFactor b (z - I / (2 * b)) k)
      = fun k => denEven b z (k + 1) := funext (denFactor_shift_down hb0 z)
  have hup : (fun k => denFactor b (z + I / (2 * b)) k) = denEven b z :=
    funext (denFactor_shift_up hb0 z)
  have hmul' : Multipliable fun k => denEven b z (k + 1) := hdown ▸ hmul
  calc (∏' k, denFactor b (z + I / (2 * b)) k)
      = ∏' k, denEven b z k := by rw [hup]
    _ = denEven b z 0 * ∏' k, denEven b z (k + 1) := tprod_eq_zero_mul_succ hmul'
    _ = (1 + Complex.exp (2 * (Real.pi : ℂ) * z / b))
        * ∏' k, denFactor b (z - I / (2 * b)) k := by rw [denEven_zero, hdown]

/-! ## The class instance -/

/-- **`phiBProd` inhabits `FaddeevPhi`** (given the two analytic convergence
facts as explicit hypotheses — see the module docstring).  This turns the
conjecture-class into a theorem-class on the product-supported branch: the
open content that remains is (a) the `Multipliable` discharge (geometric
bounds, `Im b² > 0`) and (b) the `|q| = 1` fibre regime, where the product
diverges and only the contour integral defines `Φ_b`. -/
theorem faddeevPhi_phiBProd (b : ℂ) (hb : 0 < b.re)
    (hnum : ∀ w : ℂ, Multipliable (numFactor b w))
    (hden : ∀ w : ℂ, Multipliable (denFactor b w)) :
    FaddeevPhi b (phiBProd b) := by
  have hb0 : b ≠ 0 := by
    intro h
    rw [h] at hb
    simp at hb
  refine ⟨hb, ?_, ?_⟩
  · -- b-shift: numerator telescopes, denominator invariant.
    intro z
    have hden_eq : (fun k => denFactor b (z - I * (b / 2)) k)
        = fun k => denFactor b (z + I * (b / 2)) k :=
      funext (denFactor_shift_b_invariant hb0 z)
    unfold phiBProd
    rw [hden_eq, tprod_num_shift b z (hnum _), mul_div_assoc]
  · -- 1/b-shift (guarded): numerator invariant, denominator telescopes.
    intro z hpre
    have hnum_eq : (fun k => numFactor b (z - I / (2 * b)) k)
        = fun k => numFactor b (z + I / (2 * b)) k :=
      funext (numFactor_shift_binv_invariant hb0 z)
    unfold phiBProd
    rw [hnum_eq, tprod_den_shift hb0 z (hden _)]
    rw [eq_comm, mul_div_assoc']
    exact (mul_div_mul_left _ _ hpre).symm ▸ rfl

/-! ## The substrate b-map lands in the product-supported branch

The physical b-map pinned by the numerical battery (PR #3540,
`computations/qbeta/phi-b-substrate-regime.witness.json`) is
`b(t) = √(t/2π)·e^{iπ/4}` with `t = ln q₀ > 0`.  Here we prove the two facts
that place it in scope: `Re b > 0` (the `FaddeevPhi.hb` precondition) and
`Im b² > 0` (the branch on which the modular-double product converges — the
regime of `faddeevPhi_phiBProd`).  With the pending `Multipliable` discharge,
`faddeevPhi_phiBProd (substrateB t) …` becomes the physical instance. -/

/-- The substrate b-map `b(t) = √(t/2π)·e^{iπ/4}` (`t = ln q₀`). -/
noncomputable def substrateB (t : ℝ) : ℂ :=
  (Real.sqrt (t / (2 * Real.pi)) : ℂ) * Complex.exp ((Real.pi / 4 : ℝ) * I)

/-- `Re (substrateB t) > 0` for `t > 0` — the `FaddeevPhi.hb` precondition
holds at the physical map. -/
theorem substrateB_re_pos {t : ℝ} (ht : 0 < t) : 0 < (substrateB t).re := by
  unfold substrateB
  rw [Complex.re_ofReal_mul, Complex.exp_ofReal_mul_I_re, Real.cos_pi_div_four]
  have hr : 0 < Real.sqrt (t / (2 * Real.pi)) :=
    Real.sqrt_pos.mpr (div_pos ht (by positivity))
  positivity

/-- `(substrateB t)² = (t/2π)·i` — the square is purely imaginary with
positive imaginary part (for `t > 0`), i.e. `q = e^{2πib²} = e^{-t} = 1/q₀`
and the product-branch condition `Im b² > 0` holds. -/
theorem substrateB_sq {t : ℝ} (ht : 0 ≤ t) :
    (substrateB t) ^ 2 = ((t / (2 * Real.pi) : ℝ) : ℂ) * I := by
  unfold substrateB
  rw [mul_pow, ← Complex.exp_nat_mul]
  have h1 : ((Real.sqrt (t / (2 * Real.pi)) : ℂ)) ^ 2
      = ((t / (2 * Real.pi) : ℝ) : ℂ) := by
    rw [← Complex.ofReal_pow]
    norm_cast
    exact Real.sq_sqrt (div_nonneg ht (by positivity))
  have h2 : ((2 : ℕ) : ℂ) * (((Real.pi / 4 : ℝ) : ℂ) * I)
      = ((Real.pi / 2 : ℝ) : ℂ) * I := by
    push_cast
    ring
  rw [h1, h2, Complex.exp_mul_I]
  have hc : Complex.cos ((Real.pi / 2 : ℝ) : ℂ) = 0 := by
    rw [← Complex.ofReal_cos, Real.cos_pi_div_two, Complex.ofReal_zero]
  have hs : Complex.sin ((Real.pi / 2 : ℝ) : ℂ) = 1 := by
    rw [← Complex.ofReal_sin, Real.sin_pi_div_two, Complex.ofReal_one]
  rw [hc, hs]
  ring

/-- `Im (substrateB t)² > 0` for `t > 0` — the physical b-map sits on the
product-supported (`Im b² > 0`) branch, where `phiBProd` realizes `Φ_b`. -/
theorem substrateB_sq_im_pos {t : ℝ} (ht : 0 < t) :
    0 < ((substrateB t) ^ 2).im := by
  rw [substrateB_sq ht.le]
  simp only [Complex.mul_im, Complex.ofReal_re, Complex.I_im, Complex.ofReal_im,
    Complex.I_re, mul_zero, mul_one, add_zero]
  positivity

/-! ## Discharging the `Multipliable` hypotheses (`Im b² > 0`)

Both factor families are `1 + (geometric)`: the exponents step by `2πi·b²`
(numerator) and `−2πi/b²` (denominator), whose real parts decrease strictly
when `Im b² > 0`.  `multipliable_one_add_of_summable` (complete normed ring)
then discharges both hypotheses of `faddeevPhi_phiBProd` — making the
instance unconditional on the product-supported branch, in particular at the
substrate b-map. -/

private lemma summable_norm_exp_arith (E₀ c : ℂ) (hc : c.re < 0) :
    Summable fun k : ℕ => ‖Complex.exp (E₀ + (k : ℂ) * c)‖ := by
  have hnorm : (fun k : ℕ => ‖Complex.exp (E₀ + (k : ℂ) * c)‖)
      = fun k => Real.exp E₀.re * Real.exp c.re ^ k := by
    funext k
    rw [Complex.norm_exp]
    have hre : (E₀ + (k : ℂ) * c).re = E₀.re + k * c.re := by
      simp [Complex.add_re, Complex.mul_re]
    rw [hre, Real.exp_add, ← Real.exp_nat_mul, mul_comm (k : ℝ) c.re]
  rw [hnorm]
  exact (summable_geometric_of_lt_one (Real.exp_pos _).le
    (Real.exp_lt_one_iff.mpr hc)).mul_left _

/-- The numerator family is multipliable whenever `Im b² > 0`. -/
theorem multipliable_numFactor (b z : ℂ) (hβ : 0 < (b ^ 2).im) :
    Multipliable (numFactor b z) := by
  have hE : ∀ k : ℕ, (Real.pi : ℂ) * I * b ^ 2 * (2 * (k : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * b * z
      = ((Real.pi : ℂ) * I * b ^ 2 + 2 * (Real.pi : ℂ) * b * z)
        + (k : ℂ) * (2 * (Real.pi : ℂ) * I * b ^ 2) := by
    intro k; ring
  have hc : (2 * (Real.pi : ℂ) * I * b ^ 2).re < 0 := by
    have : (2 * (Real.pi : ℂ) * I * b ^ 2).re
        = -(2 * Real.pi * (b ^ 2).im) := by
      simp [Complex.mul_re, Complex.mul_im]
    rw [this]
    have hπ : (0 : ℝ) < 2 * Real.pi * (b ^ 2).im := by positivity
    linarith
  have hsum := summable_norm_exp_arith
    ((Real.pi : ℂ) * I * b ^ 2 + 2 * (Real.pi : ℂ) * b * z)
    (2 * (Real.pi : ℂ) * I * b ^ 2) hc
  have : Multipliable fun k : ℕ => 1 + Complex.exp
      (((Real.pi : ℂ) * I * b ^ 2 + 2 * (Real.pi : ℂ) * b * z)
        + (k : ℂ) * (2 * (Real.pi : ℂ) * I * b ^ 2)) :=
    multipliable_one_add_of_summable hsum
  refine this.congr fun k => ?_
  unfold numFactor
  rw [hE k]

/-- The denominator (modular-dual) family is multipliable whenever
`Im b² > 0` (there `Re(−2πi/b²) < 0` as well — the `q̃` suppression). -/
theorem multipliable_denFactor (b z : ℂ) (hβ : 0 < (b ^ 2).im) :
    Multipliable (denFactor b z) := by
  have hE : ∀ k : ℕ, -((Real.pi : ℂ) * I) / b ^ 2 * (2 * (k : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * z / b
      = (-((Real.pi : ℂ) * I) / b ^ 2 + 2 * (Real.pi : ℂ) * z / b)
        + (k : ℂ) * (-(2 * (Real.pi : ℂ) * I) / b ^ 2) := by
    intro k; ring
  have hc : (-(2 * (Real.pi : ℂ) * I) / b ^ 2).re < 0 := by
    have h1 : (-(2 * (Real.pi : ℂ) * I) / b ^ 2).re
        = -(2 * Real.pi * (b ^ 2).im) / Complex.normSq (b ^ 2) := by
      simp [Complex.div_re, Complex.mul_re, Complex.mul_im, neg_div]
    have hns : 0 < Complex.normSq (b ^ 2) :=
      Complex.normSq_pos.mpr (fun h => by simp [h] at hβ)
    rw [h1]
    have hnum : (0 : ℝ) < 2 * Real.pi * (b ^ 2).im := by positivity
    exact div_neg_of_neg_of_pos (by linarith) hns
  have hsum := summable_norm_exp_arith
    (-((Real.pi : ℂ) * I) / b ^ 2 + 2 * (Real.pi : ℂ) * z / b)
    (-(2 * (Real.pi : ℂ) * I) / b ^ 2) hc
  have : Multipliable fun k : ℕ => 1 + Complex.exp
      ((-((Real.pi : ℂ) * I) / b ^ 2 + 2 * (Real.pi : ℂ) * z / b)
        + (k : ℂ) * (-(2 * (Real.pi : ℂ) * I) / b ^ 2)) :=
    multipliable_one_add_of_summable hsum
  refine this.congr fun k => ?_
  unfold denFactor
  rw [hE k]

/-- **The unconditional physical instance.**  At the substrate b-map
`substrateB t` (`t = ln q₀ > 0`), `phiBProd` satisfies every `FaddeevPhi`
axiom with no remaining hypotheses — the conjecture-class is a theorem-class
on the physical branch.  What stays open is only the `|q| = 1` fibre regime
(real `b`), where the product diverges and the contour integral is the sole
definition. -/
theorem faddeevPhi_phiBProd_substrate {t : ℝ} (ht : 0 < t) :
    FaddeevPhi (substrateB t) (phiBProd (substrateB t)) :=
  faddeevPhi_phiBProd _ (substrateB_re_pos ht)
    (fun w => multipliable_numFactor _ w (substrateB_sq_im_pos ht))
    (fun w => multipliable_denFactor _ w (substrateB_sq_im_pos ht))

end QOU.MathlibExt.PhiBProd
