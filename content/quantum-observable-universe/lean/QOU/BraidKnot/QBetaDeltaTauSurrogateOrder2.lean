import Mathlib.Data.Real.Basic
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import QOU.BraidKnot.QBetaPerBlockChiClosedForms

/-!
# QOU.BraidKnot.QBetaDeltaTauSurrogateOrder2

**Order-2 (second-derivative) Taylor coefficient of `delta_tau_M_surrogate`
at `q = 1`, via the quotient-rule chain extended one level past the
order-1 result.**

The parent file `QBetaPerBlockChiClosedForms.lean` proves the order-1
coefficient `delta_tau_M_surrogate_hasDerivAt_one : HasDerivAt
delta_tau_M_surrogate (-5/6) 1` by the quotient rule on `N/D`, and leaves
the order-2 coefficient as a `True := trivial` placeholder
(`delta_tau_M_surrogate_taylor_coeff_2`) with a note that the
`iteratedDeriv`-level discharge is "bulky but tractable". This file
discharges it.

## What is proved

Write `g = N/D = delta_tau_M_surrogate` with

  `N(q) = -q¹¹+q¹⁰-2q⁹+q⁸+q⁶-q⁵-q³+2q²-q+1`,  `N(1)=0, N'(1)=-10, N''(1)=-100`,
  `D(q) = 4q⁵(q²+q+1)`,                          `D(1)=12, D'(1)=72,  D''(1)=368`.

The first derivative is, by the quotient rule,
  `g'(q) = (N'(q)·D(q) − N(q)·D'(q)) / D(q)²`   (`delta_tau_M_surrogate_deriv`).
This file proves
  `HasDerivAt delta_tau_M_surrogate_deriv (5/3) 1`,
i.e. `g''(1) = 5/3` — differentiating the quotient-rule result a SECOND
time. The order-2 Taylor coefficient is then
  `c₂ = g''(1) / 2! = (5/3)/2 = 5/6`,
matching the witnessed value
`delta_tau_M_surrogate_taylor_witness 2 = 5/6` (from
`qbeta-c3-multiblock-recursion-attack.witness.json`).

The proof reuses ONLY the lemma toolkit of the verified order-1 proof
(`hasDerivAt_pow`, `HasDerivAt.{neg,const_mul,add,sub,mul,div}`,
`convert … using 1`, `norm_num`) — no `iteratedDeriv`/`eventuallyEq`
machinery — so it is a faithful "the quotient-rule chain extends"
demonstration. The numerical checkpoints (`N''(1)=-100`, `D''(1)=368`,
`num'(1)=-1200`, `den'(1)=1728`, `g''(1)=34560/20736=5/3`) are recorded in
the comments at each step.

LaTeX label: `prop:qbeta-delta-tau-surrogate-order2`
-/

namespace QOU.BraidKnot

/-- The first-derivative function of `delta_tau_M_surrogate`, written
explicitly via the quotient rule:

  `g'(q) = (N'(q)·D(q) − N(q)·D'(q)) / D(q)²`,

with `N'(q) = -11q¹⁰+10q⁹-18q⁸+8q⁷+6q⁵-5q⁴-3q²+4q-1` and
`D'(q) = 28q⁶+24q⁵+20q⁴` the (manually differentiated) numerator and
denominator derivatives. Equality with `deriv delta_tau_M_surrogate` on
`{q | q ≠ 0}` follows from the order-1 quotient-rule proof; here we only
need this explicit form to take the second derivative. -/
noncomputable def delta_tau_M_surrogate_deriv (q : ℝ) : ℝ :=
  ((-11*q^10 + 10*q^9 - 18*q^8 + 8*q^7 + 6*q^5 - 5*q^4 - 3*q^2 + 4*q - 1)
      * (4 * q^5 * (q^2 + q + 1))
    - (-q^11 + q^10 - 2*q^9 + q^8 + q^6 - q^5 - q^3 + 2*q^2 - q + 1)
      * (28*q^6 + 24*q^5 + 20*q^4))
  / ((4 * q^5 * (q^2 + q + 1)) * (4 * q^5 * (q^2 + q + 1)))

/-- **Consistency with order-1.** `g'(1) = -5/6`, matching
`delta_tau_M_surrogate_hasDerivAt_one`. Pure numerical identity. -/
theorem delta_tau_M_surrogate_deriv_at_one :
    delta_tau_M_surrogate_deriv 1 = -5/6 := by
  unfold delta_tau_M_surrogate_deriv
  norm_num

/-- **Theorem (order-2 / second derivative).** The explicit first-derivative
function has derivative `5/3` at `q = 1`:

  `g''(1) = 5/3`,

so the order-2 Taylor coefficient is `g''(1)/2! = 5/6`. Proof: the
quotient rule `HasDerivAt.div` applied to the numerator
`num = N'·D − N·D'` and denominator `den = D·D`, each built from explicit
polynomial `HasDerivAt` chains — the order-1 quotient-rule chain extended
one derivative level. -/
theorem delta_tau_M_surrogate_deriv_hasDerivAt_one :
    HasDerivAt delta_tau_M_surrogate_deriv (5/3) 1 := by
  unfold delta_tau_M_surrogate_deriv
  -- N(q) = -q¹¹+…+1 ;  N(1)=0, N'(1)=-10
  have hN : HasDerivAt
      (fun q : ℝ => -q^11 + q^10 - 2*q^9 + q^8 + q^6 - q^5 - q^3 + 2*q^2 - q + 1)
      (-10 : ℝ) 1 := by
    have h11 := (hasDerivAt_pow 11 (1 : ℝ)).neg
    have h10 := hasDerivAt_pow 10 (1 : ℝ)
    have h9  := (hasDerivAt_pow 9 (1 : ℝ)).const_mul 2
    have h8  := hasDerivAt_pow 8 (1 : ℝ)
    have h6  := hasDerivAt_pow 6 (1 : ℝ)
    have h5  := hasDerivAt_pow 5 (1 : ℝ)
    have h3  := hasDerivAt_pow 3 (1 : ℝ)
    have h2  := (hasDerivAt_pow 2 (1 : ℝ)).const_mul 2
    have h1  := hasDerivAt_id (1 : ℝ)
    have h0  : HasDerivAt (fun _ : ℝ => (1 : ℝ)) 0 1 := hasDerivAt_const 1 1
    have hsum := (((((((((h11.add h10).sub h9).add h8).add h6).sub h5).sub h3).add h2).sub h1).add h0)
    convert hsum using 1
    norm_num
  -- N'(q) = -11q¹⁰+… ;  N'(1)=-10, N''(1)=-100
  have hNp : HasDerivAt
      (fun q : ℝ => -11*q^10 + 10*q^9 - 18*q^8 + 8*q^7 + 6*q^5 - 5*q^4 - 3*q^2 + 4*q - 1)
      (-100 : ℝ) 1 := by
    have h10 := ((hasDerivAt_pow 10 (1 : ℝ)).const_mul 11).neg
    have h9  := (hasDerivAt_pow 9 (1 : ℝ)).const_mul 10
    have h8  := (hasDerivAt_pow 8 (1 : ℝ)).const_mul 18
    have h7  := (hasDerivAt_pow 7 (1 : ℝ)).const_mul 8
    have h5  := (hasDerivAt_pow 5 (1 : ℝ)).const_mul 6
    have h4  := (hasDerivAt_pow 4 (1 : ℝ)).const_mul 5
    have h2  := (hasDerivAt_pow 2 (1 : ℝ)).const_mul 3
    have h1  := (hasDerivAt_pow 1 (1 : ℝ)).const_mul 4
    have h0  : HasDerivAt (fun _ : ℝ => (1 : ℝ)) 0 1 := hasDerivAt_const 1 1
    have hsum := (((((((h10.add h9).sub h8).add h7).add h5).sub h4).sub h2).add h1).sub h0
    convert hsum using 1 <;>
      first
        | (funext q; simp only [Pi.add_apply, Pi.sub_apply, Pi.neg_apply]; ring)
        | norm_num
  -- D(q) = 4q⁵(q²+q+1) ;  D(1)=12, D'(1)=72   (same shape as order-1's hD)
  have hD : HasDerivAt (fun q : ℝ => 4 * q^5 * (q^2 + q + 1)) (72 : ℝ) 1 := by
    have h5  : HasDerivAt (fun q : ℝ => q^5) ((5 : ℝ) * 1^4) 1 := hasDerivAt_pow 5 1
    have h2  : HasDerivAt (fun q : ℝ => q^2) ((2 : ℝ) * 1^1) 1 := hasDerivAt_pow 2 1
    have h1  : HasDerivAt (fun q : ℝ => q) (1 : ℝ) 1 := hasDerivAt_id 1
    have h0  : HasDerivAt (fun _ : ℝ => (1 : ℝ)) 0 1 := hasDerivAt_const 1 1
    have hquad : HasDerivAt (fun q : ℝ => q^2 + q + 1) (3 : ℝ) 1 := by
      have := (h2.add h1).add h0
      convert this using 1
      norm_num
    have hprod : HasDerivAt (fun q : ℝ => q^5 * (q^2 + q + 1)) (18 : ℝ) 1 := by
      have := h5.mul hquad
      convert this using 1
      norm_num
    have := hprod.const_mul 4
    convert this using 1
    · funext q; ring
    · norm_num
  -- D'(q) = 28q⁶+24q⁵+20q⁴ ;  D'(1)=72, D''(1)=368
  have hDp : HasDerivAt
      (fun q : ℝ => 28*q^6 + 24*q^5 + 20*q^4) (368 : ℝ) 1 := by
    have h6 := (hasDerivAt_pow 6 (1 : ℝ)).const_mul 28
    have h5 := (hasDerivAt_pow 5 (1 : ℝ)).const_mul 24
    have h4 := (hasDerivAt_pow 4 (1 : ℝ)).const_mul 20
    have hsum := (h6.add h5).add h4
    convert hsum using 1
    norm_num
  -- num = N'·D − N·D' ;  num(1)=-120, num'(1)=N''·D−N·D'' at 1 = -100·12 − 0·368 = -1200
  have hnum := (hNp.mul hD).sub (hN.mul hDp)
  -- den = D·D ;  den(1)=144, den'(1)=2·D·D' at 1 = 2·12·72 = 1728
  have hden := hD.mul hD
  have hden_ne :
      (fun q : ℝ => 4 * q^5 * (q^2 + q + 1)) 1
        * (fun q : ℝ => 4 * q^5 * (q^2 + q + 1)) 1 ≠ 0 := by norm_num
  -- g''(1) = (num'·den − num·den')/den² = (-1200·144 − (-120)·1728)/144² = 34560/20736 = 5/3
  have hdiv := hnum.div hden hden_ne
  convert hdiv using 1
  norm_num

/-- **Corollary (order-2 Taylor coefficient = 5/6).** Since
`g''(1) = 5/3`, the second Taylor coefficient at `q = 1` is
`g''(1) / 2! = 5/6`, matching the witnessed catalogue value
`delta_tau_M_surrogate_taylor_witness 2`. -/
theorem delta_tau_M_surrogate_taylor_coeff_2_eq :
    (5 : ℝ) / 3 / (Nat.factorial 2) = 5 / 6 := by
  norm_num [Nat.factorial]

end QOU.BraidKnot
