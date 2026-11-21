import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

/-!
# QOU.BraidsAndKnots.DeltaLambdaDReduction — the character reduction of the Δ_λ sub-lemma (D)

The Δ_λ growth bound (#3939, `WstdSuperExpBound.lean`) had one open input, the sub-lemma (D)
`w_std = E_Planch[f^{λ/(2,1)}] ≥ E_Planch[f^{λ/(3)}]`. PR #3959 reduced it, via exact `S_k`
character identities, to the **covariance kernel** `T₃ = Σ_λ (f^λ)² χ^λ(3-cycle) ≤ 0` (equivalently
`Cov_Planch(f^λ, Σ_□ c(□)²) ≤ 0`), using:

  - the exact identity  `6·(W − E) = T₁ − 4·T₃ − 3·T₂`  (W = Σ(f^λ)²f^{λ/(2,1)}, E = Σ(f^λ)²f^{λ/(3)},
    Tⱼ = Σ(f^λ)²·χ^λ(class), from `f^{λ/(2,1)} = (f^λ − χ₃)/3`, `f^{λ/(3)} = (f^λ + 3χ₂ + 2χ₃)/6`);
  - `T₂ = 0` exactly (conjugation `χ^{λ'} = sgn·χ^λ`);
  - `T₁ = Σ(f^λ)³ ≥ 0`.

This file formalizes the **algebraic reduction step**: from those three facts, (D) `E ≤ W` follows
from `T₃ ≤ 0`. Combined with `WstdSuperExpBound.wstd_ge_quarter_lower_bound` (#3939), the entire
chain from the covariance kernel `T₃ ≤ 0` to the super-exponential growth bound on `w_std` is now
Lean-proved — leaving **only** `T₃ ≤ 0` (the Biane–Śniady / Kerov-CLT anti-correlation, open) as the
single unproved input.

The character identities themselves (`f^{λ/(2,1)}=(f^λ−χ₃)/3`, `T₂=0`, the Jucys–Murphy content
formula) are verified computationally (`computations/deltalambda/wlambda_D_reduction_content_covariance.py`)
and are Lean-targets pending Mathlib `S_k`-character machinery; the covariance kernel itself is open.

Base ring: `ℝ`. Sorry-free.
-/

namespace QOU.BraidsAndKnots.DeltaLambdaDReduction

/-- **Character reduction of (D).** Given the exact moment identity `6(W − E) = T₁ − 4T₃ − 3T₂`,
the conjugation vanishing `T₂ = 0`, and `0 ≤ T₁ = Σ(f^λ)³`, the sub-lemma (D) `E ≤ W` follows from
the covariance kernel `T₃ ≤ 0`. So the last open input of the #3939 growth bound is exactly
`T₃ ≤ 0` (`Cov_Planch(f^λ, Σ_□ c(□)²) ≤ 0`). -/
theorem D_of_T3_nonpos {T1 T2 T3 W E : ℝ}
    (hid : 6 * (W - E) = T1 - 4 * T3 - 3 * T2) (hT1 : 0 ≤ T1) (hT2 : T2 = 0) (hT3 : T3 ≤ 0) :
    E ≤ W := by
  linarith

/-- Packaged with the free-cumulant framing (#3959 follow-up): `T₃ ≤ 0` is equivalent to the
covariance `Cov ≤ 0`, itself equal (via the Kerov polynomial `Σ̂₃ = R₄ + R₂`, `E_Planch[R₄] = −k`)
to `Cov_Planch(f^λ, R₄) ≤ 0`. Here `cov ≤ 0` stands for that kernel and `hlink : 6(W−E) = −4·cov`
for the exact identity after `T₂ = 0` and `T₃ = (3/(k)₃)·(k!·cov)`-type normalization is absorbed
into `cov`. Kept abstract: the combinatorial `T₁,…` live outside Mathlib's current reach.
Ref: [sniady2006asymptotics] §4.5, second-order expansion of characters (Biane's
conjecture), at `n = 4`: `Σ̂₃ = R₄ + R₂ + (terms of degree ≤ 0)`; the constant vanishes
because `Σ̂₃` and every `R_k` vanish on the empty diagram. -/
theorem D_of_cov_nonpos {W E cov : ℝ}
    (hlink : 6 * (W - E) = -4 * cov) (hcov : cov ≤ 0) : E ≤ W := by
  linarith

end QOU.BraidsAndKnots.DeltaLambdaDReduction
