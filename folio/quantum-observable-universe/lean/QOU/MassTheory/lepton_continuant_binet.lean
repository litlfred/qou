import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# QOU.Archimedean.lepton_continuant_binet — closed form of the continuant, and the bridge exclusion

Companion to `lepton_continuant_recurrence` (the Morgan–Voyce
recurrence itself) and `lepton_continuant_generation_exclusion` (the
divisibility / T(2,9)-harmonic result).  This file supplies the
algebraic facts behind bean `qou-lsp9` — *the `net(T(2,n)) → lepton
mass` map* — whose numerical companions are
[`lepton_net_to_mass_bridge_exclusion.py`](../../../../../computations/lepton_net_to_mass_bridge_exclusion.py)
(§§1–2) and
[`lepton_linear_readout_rigidity.py`](../../../../../computations/lepton_linear_readout_rigidity.py)
(§3).

Sections 1–2 treat the `net` readout; §3 generalises to *every* linear
readout of `H₂(q)`, which is what answers the natural objection "use the
Markov trace instead".  The positivity invariant that closes the one
remaining escape lives in the companion
`QOU.Archimedean.lepton_continuant_positivity`, split out per the §7c
base-ring wall: this file is pure `[Field K]` algebra, that one needs an
*order*.

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

-- Ref: [leitner2026] quantum-observable-universe/predicted-spectra/lepton-continuant-recurrence.md
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

/-! ## 3. The exclusion is not about `net` — it is about `H₂(q)` being two-dimensional

`net` is one choice of readout, and singling it out understates the
result.  `H₂(q)` has dimension `2! = 2` with basis `{1, σ₀}`, and the
normal form is `NF(σ₀^w) = a_w · 1 + b_w · σ₀` with `a_w = b_{w-1}`.  So
*every* linear functional `φ` on `H₂(q)` — every possible way of reading
a number off the lepton's own braid — evaluates to

```
  φ(σ₀^w) = α · b_{w-1} + β · b_w,        α = φ(1),  β = φ(σ₀).
```

`netK` is `(α, β) = (1, 1)`; the **Markov trace** `tr_M`, which is the
readout the canonical mass route actually uses (`F_Bor` in the nucleon
formula is a `tr_M`), is `(α, β) = (tr_M 1, tr_M σ₀)`.  Both are single
points in this two-parameter family.

The theorems below show the family is *rigid*: the `(α, β)` dependence
collapses into one constant `B = α − β q⁻¹`, and every member obeys the
same two-step recursion with ratio `q²` up to a `q⁻ⁿ` remainder.  There
is no choice of readout — not `net`, not `tr_M`, not any other — that
bends the tower.  That is what upgrades the exclusion from "the net does
not work" to "no `H₂(q)`-linear readout can work".
-/

/-- A linear functional on `H₂(q)` evaluated along the generation braids.

With `α = φ(1)` and `β = φ(σ₀)`, this is `φ(σ₀^(n+1))`, since
`NF(σ₀^(n+1)) = b_n · 1 + b_{n+1} · σ₀`.  The index is the *lower*
continuant index, so winding `w` corresponds to `n = w - 1`. -/
def linFunctionalK (α β q : K) (n : ℕ) : K :=
  α * morganVoyceBK q n + β * morganVoyceBK q (n + 1)

/-- `net` is the linear functional with both coefficients `1`. -/
lemma netK_eq_linFunctionalK (q : K) (n : ℕ) :
    netK q n = linFunctionalK 1 1 q n := by
  simp [netK, linFunctionalK]

/-- **Binet closed form for an arbitrary linear readout.**

`(α b_n + β b_{n+1})(q + q⁻¹) = A qⁿ − (−1)ⁿ B q⁻ⁿ`, with

```
  A = α + β q        (the growing amplitude)
  B = α − β q⁻¹      (the decaying amplitude)
```

The whole two-parameter family therefore has the *same* two-term shape
as `net`: one component growing like `qⁿ`, one decaying like `q⁻ⁿ`.
Changing the readout only re-weights the two amplitudes; it cannot
introduce a third scale, because there is no third basis element. -/
theorem linFunctionalK_binet (α β q : K) (hq : q ≠ 0) (n : ℕ) :
    linFunctionalK α β q n * (q + q⁻¹)
      = (α + β * q) * q ^ n
        - (-1 : K) ^ n * ((α - β * q⁻¹) * (q⁻¹) ^ n) := by
  have expand :
      (α * morganVoyceBK q n + β * morganVoyceBK q (n + 1)) * (q + q⁻¹)
        = α * (morganVoyceBK q n * (q + q⁻¹))
          + β * (morganVoyceBK q (n + 1) * (q + q⁻¹)) := by ring
  rw [linFunctionalK, expand, morganVoyceBK_binet q hq n,
      morganVoyceBK_binet q hq (n + 1)]
  simp only [pow_succ]
  ring

/-- **Two-step rigidity of every `H₂(q)`-linear readout.**

```
  φ(n+2) = q² · φ(n) + (−1)ⁿ (q − q⁻¹) B q⁻ⁿ,      B = α − β q⁻¹.
```

Every linear readout of the lepton braid advances by the *same* factor
`q²` per generation step, corrected only by a term decaying like `q⁻ⁿ`.
The readout choice `(α, β)` survives solely inside `B`, i.e. it can
rescale the vanishing correction but not the `q²`.

This is the invariant that prunes the search (AGENTS.md formalize-first
probe discipline).  Composed with `mass_ratio_rigidity`, it excludes
`m_w = C g^w φ(σ₀^w)^p` for *every* linear functional `φ`, not just for
`net`: the observed lepton tower is log-concave (log-increments 5.332
then 2.822), while every member of this family is log-linear up to
`O(q⁻²ⁿ)`. -/
theorem linFunctionalK_two_step (α β q : K) (hq : q ≠ 0)
    (hqq : q + q⁻¹ ≠ 0) (n : ℕ) :
    linFunctionalK α β q (n + 2)
      = q ^ 2 * linFunctionalK α β q n
        + (-1 : K) ^ n * ((q - q⁻¹) * ((α - β * q⁻¹) * (q⁻¹) ^ n)) := by
  have h0 := linFunctionalK_binet α β q hq n
  have h2 := linFunctionalK_binet α β q hq (n + 2)
  refine mul_right_cancel₀ hqq ?_
  rw [h2]
  have expand :
      (q ^ 2 * linFunctionalK α β q n
          + (-1 : K) ^ n * ((q - q⁻¹) * ((α - β * q⁻¹) * (q⁻¹) ^ n)))
        * (q + q⁻¹)
        = q ^ 2 * (linFunctionalK α β q n * (q + q⁻¹))
          + (-1 : K) ^ n
            * ((q - q⁻¹) * (q + q⁻¹) * ((α - β * q⁻¹) * (q⁻¹) ^ n)) := by
    ring
  rw [expand, h0]
  simp only [pow_add]
  ring

/-- **The fine-tuned direction does not escape either.**

One might hope to cancel the growing `qⁿ` component and get a different
law from the survivor.  The readout `α = β q⁻¹` kills `B`, and the
recursion then becomes *exactly* geometric with ratio `q²` — no
remainder at all, hence still log-linear.  So the one direction in the
family that could have behaved differently is the most rigid of all:
there is no member with a bent tower. -/
theorem linFunctionalK_exactly_geometric (β q : K) (hq : q ≠ 0)
    (hqq : q + q⁻¹ ≠ 0) (n : ℕ) :
    linFunctionalK (β * q⁻¹) β q (n + 2)
      = q ^ 2 * linFunctionalK (β * q⁻¹) β q n := by
  rw [linFunctionalK_two_step _ _ q hq hqq n, sub_self, zero_mul, mul_zero,
    mul_zero, add_zero]

end QOU.Archimedean
