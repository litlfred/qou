import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.Archimedean.lepton_continuant_binet — closed form of the continuant, and the bridge exclusion

Companion to `lepton_continuant_recurrence` (the Morgan–Voyce
recurrence itself) and `lepton_continuant_generation_exclusion` (the
divisibility / T(2,9)-harmonic result).  This file supplies the two
algebraic facts behind bean `qou-lsp9` — *the `net(T(2,n)) → lepton
mass` map* — whose numerical companion is
[`lepton_net_to_mass_bridge_exclusion.py`](../../../../../computations/lepton_net_to_mass_bridge_exclusion.py).

## 1. The Binet closed form

Because `h = q − q⁻¹`, the characteristic polynomial `x² − h x − 1` of
the Morgan–Voyce recurrence has roots `q` and `−q⁻¹` (their sum is `h`,
their product `−1`).  Hence the continuant is *exactly geometric up to
an alternating `q⁻ⁿ` remainder*:

```
  b_n · (q + q⁻¹) = qⁿ − (−1)ⁿ · (q⁻¹)ⁿ
```

This is the invariant that prunes the search: `net(n) = b_{n-1} + b_n`
is therefore log-linear in `n` up to a remainder decaying like `q⁻²ⁿ`,
while the observed lepton tower is log-concave (log-increments 5.332
then 2.822).

## 2. Ratio rigidity of the multiplicative bridge class

`mass_ratio_rigidity` records the consequence for the whole class
`m n = C · gⁿ · (net n)^p`: the step-to-step variation of the mass
ratio is carried *entirely* by the variation of the net ratio.  Since
that variation is the exponentially-small remainder above, fitting the
observed 12.3× drop between the two steps forces `p ≈ 667` and
`g² ≈ 5·10⁻⁶²` (measured in the Python twin).  The class is not
under-determined — it is exponentially fine-tuned, which is the
exclusion.

**Scope.** Scope-(b) for that multiplicative class only, resting on the
proved asymptotics.  Non-multiplicative bridges — an additive interface
term, or a Higgs-coupling route where `n` enters through linking with
`4₁` rather than through `net` — are **not** excluded here.

-- Ref: [manuscript] quantum-observable-universe/predicted-spectra/lepton-continuant-recurrence.md
-/

namespace QOU.Archimedean

variable {K : Type*} [Field K]

/-- The Morgan–Voyce continuant evaluated in a field at the Hecke
parameter `h = q − q⁻¹`: `b 0 = 0`, `b 1 = 1`,
`b (n+2) = h · b (n+1) + b n`.  This is the field-valued twin of
`morganVoyceB : ℕ → Polynomial ℤ`. -/
def morganVoyceBK (q : K) : ℕ → K
  | 0 => 0
  | 1 => 1
  | (n + 2) => (q - q⁻¹) * morganVoyceBK q (n + 1) + morganVoyceBK q n

@[simp] lemma morganVoyceBK_zero (q : K) : morganVoyceBK q 0 = 0 := rfl

@[simp] lemma morganVoyceBK_one (q : K) : morganVoyceBK q 1 = 1 := rfl

lemma morganVoyceBK_succ_succ (q : K) (n : ℕ) :
    morganVoyceBK q (n + 2)
      = (q - q⁻¹) * morganVoyceBK q (n + 1) + morganVoyceBK q n := rfl

/-- **Binet closed form for the Morgan–Voyce continuant.**

`b_n · (q + q⁻¹) = qⁿ − (−1)ⁿ (q⁻¹)ⁿ`, for any `q ≠ 0` in a field.

The two roots of `x² − (q − q⁻¹)x − 1` are `q` and `−q⁻¹`; this is the
resulting Binet formula.  Its content is that the continuant is
geometric with ratio `q` up to an alternating remainder of size
`q⁻ⁿ` — the fact that makes `net` log-linear in the winding number. -/
theorem morganVoyceBK_binet (q : K) (hq : q ≠ 0) (n : ℕ) :
    morganVoyceBK q n * (q + q⁻¹) = q ^ n - (-1 : K) ^ n * (q⁻¹) ^ n := by
  induction n using Nat.twoStepInduction with
  | zero => simp
  | one => simp
  | more n ih ih' =>
      rw [morganVoyceBK_succ_succ]
      have expand :
          ((q - q⁻¹) * morganVoyceBK q (n + 1) + morganVoyceBK q n) * (q + q⁻¹)
            = (q - q⁻¹) * (morganVoyceBK q (n + 1) * (q + q⁻¹))
              + morganVoyceBK q n * (q + q⁻¹) := by ring
      rw [expand, ih', ih]
      simp only [pow_succ]
      field_simp
      ring

/-- The net normal-form coefficient `net(T(2,n)) = a_n + b_n = b_{n-1} + b_n`,
field-valued twin of `netCoeff`. -/
def netK (q : K) (n : ℕ) : K := morganVoyceBK q n + morganVoyceBK q (n + 1)

/-- **Ratio rigidity of the multiplicative bridge class.**

If a candidate mass map has the multiplicative shape
`m n = C · gⁿ · (net n)^p` — which covers every power law, every
exponential-times-power, and in particular the "missing scale factor"
(`p = 1`, `g = 1`) that bean `qou-lsp9` posits — then each two-step
mass ratio is `g²` times the corresponding net ratio raised to `p`.

Consequence (the exclusion): the *only* thing that can make consecutive
mass ratios differ is the variation of the net ratio.  By
`morganVoyceBK_binet` that variation is the `O(q⁻²ⁿ)` remainder — 0.38%
at the substrate `q₀` — so reproducing the observed 12.3× drop demands
`p ≈ 667`, and `p` grows like `q²ⁿ` for any further generation. -/
theorem mass_ratio_rigidity (C g : K) (p n : ℕ) (net m : ℕ → K)
    (hm : ∀ k, m k = C * g ^ k * (net k) ^ p)
    (hC : C ≠ 0) (hg : g ≠ 0) (hnet : net n ≠ 0) :
    m (n + 2) / m n = g ^ 2 * (net (n + 2) / net n) ^ p := by
  rw [hm, hm, div_pow]
  have hCg : C * g ^ n ≠ 0 := mul_ne_zero hC (pow_ne_zero _ hg)
  have hnp : (net n) ^ p ≠ 0 := pow_ne_zero _ hnet
  field_simp
  ring

end QOU.Archimedean
