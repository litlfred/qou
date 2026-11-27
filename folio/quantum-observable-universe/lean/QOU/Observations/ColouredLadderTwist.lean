/-
# The coloured lepton ladder `Δ^{2k+1}` is lighter at every level

Thread "Derive the electron's categorical weight" (2026-11-27, owner card: "Coloured ring mass of
Δⁿ (all levels)"). Audit: `docs/audits/2026-11-27-electron-categorical-weight.md` §12. Probe:
`computations/probes/coloured_ladder/coloured_delta_ladder_probe.py` (26/26).

Words (owner ruling 22:37Z): `e = Δ = σ₁σ₂σ₁`, `μ = Δ³`, `τ = Δ⁵` (`LeptonUniversalityLadder`).
At level `N = 2j + 1` (the spin-`j` module `V_j`), the framing-corrected ring mass is
`m_N(β) = f^{−w} tr(K^{⊗3} ρ_N(β))`, with `f` fixed by stabilisation. The ribbon structure gives
the following (standard; checked numerically for `N ≤ 6` by the probe, and carried here as the
hypothesis `TwistDecomposition`, not as an axiom):

* `f = q^{2j(j+1)}`, and the full twist `Δ²` acts on the spin-`J` part of `V_j^{⊗3}` by
  `q^{2J(J+1) − 6j(j+1)}`;
* hence `m_N(Δ^{2k+1}) = Σ_J a_J r_J^k` with `r_J = q^{e_J}`, `e_J = 2J(J+1) − 18j(j+1)`.

In doubled spins `n = 2j = N − 1`, `M = 2J ≤ 3n`, this file proves:

* `twistExp_le`: `2 e_J = M(M+2) − 9n(n+2) ≤ −12n`, with equality at the top `M = 3n`
  (`twistExp_top`). So every ratio has `e_J ≤ −6(N−1)`.
* `ladder_envelope`: if `0 < r_J ≤ ρ` for every `J`, then `|Σ a_J r_J^k| ≤ (Σ |a_J|)·ρ^k`.
* `coloured_ladder_decays`: with `r_J = q^{e_J}`, `q ≥ 1` and `e_J ≤ −6n`,
  `|m_N(Δ^{2k+1})| ≤ C·(q^{−6n})^k`.

So for `q > 1` no level `N ≥ 2` makes the ladder heavier. The masses fall at least as fast as
`q^{−6(N−1)k}`. The mirror ladder `Δ^{−(2k+1)}` is the heavier direction. Nothing here is compared
with a measured value, and no level is chosen.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic

namespace QOU.Observations.ColouredLadderTwist

/-- Twice the ratio exponent, in doubled spins: `2 e_J = M(M+2) − 9 n(n+2)`. -/
def twistExp2 (n M : ℤ) : ℤ := M * (M + 2) - 9 * (n * (n + 2))

/-- **Every ratio exponent is at most `−6(N−1)`**: `2 e_J ≤ −12 n` for `0 ≤ M ≤ 3n`. -/
theorem twistExp_le (n M : ℤ) (hM0 : 0 ≤ M) (hM : M ≤ 3 * n) : twistExp2 n M ≤ -12 * n := by
  unfold twistExp2
  nlinarith

/-- The top component `M = 3n` attains it. -/
theorem twistExp_top (n : ℤ) : twistExp2 n (3 * n) = -12 * n := by
  unfold twistExp2; ring

/-- The rep-theoretic input, as data: the ladder masses are a finite sum of geometric terms. -/
structure TwistDecomposition (K : Type*) [Field K] (ι : Type*) [Fintype ι] where
  /-- coefficients `a_J` -/
  a : ι → K
  /-- ratios `r_J` -/
  r : ι → K
  /-- the ladder masses `m_k = m_N(Δ^{2k+1})` -/
  m : ℕ → K
  decomp : ∀ k, m k = ∑ J, a J * r J ^ k

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **Envelope.** `|Σ a_J r_J^k| ≤ (Σ |a_J|) ρ^k` when `0 < r_J ≤ ρ`. -/
theorem ladder_envelope {ι : Type*} [Fintype ι] (a r : ι → K) (ρ : K)
    (hr0 : ∀ J, 0 < r J) (hr : ∀ J, r J ≤ ρ) (k : ℕ) :
    |∑ J, a J * r J ^ k| ≤ (∑ J, |a J|) * ρ ^ k := by
  calc |∑ J, a J * r J ^ k| ≤ ∑ J, |a J * r J ^ k| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ J, |a J| * ρ ^ k := by
        refine Finset.sum_le_sum fun J _ => ?_
        rw [abs_mul, abs_of_pos (pow_pos (hr0 J) k)]
        exact mul_le_mul_of_nonneg_left (pow_le_pow_left₀ (hr0 J).le (hr J) k) (abs_nonneg _)
    _ = (∑ J, |a J|) * ρ ^ k := by rw [Finset.sum_mul]

/-- **The coloured ladder decays at every level.** With `r_J = q^{e_J}`, `q ≥ 1`, and every
`e_J ≤ −6n` (`twistExp_le`), `|m_k| ≤ (Σ |a_J|)·(q^{−6n})^k`. -/
theorem coloured_ladder_decays {ι : Type*} [Fintype ι] (D : TwistDecomposition K ι)
    (q : K) (hq : 1 ≤ q) (n : ℤ) (e : ι → ℤ) (he : ∀ J, e J ≤ -6 * n)
    (hr : ∀ J, D.r J = q ^ e J) (k : ℕ) :
    |D.m k| ≤ (∑ J, |D.a J|) * (q ^ (-6 * n)) ^ k := by
  have hq0 : 0 < q := lt_of_lt_of_le one_pos hq
  rw [D.decomp]
  refine ladder_envelope D.a D.r _ (fun J => by rw [hr]; exact zpow_pos hq0 _) (fun J => ?_) k
  rw [hr]
  exact zpow_le_zpow_right₀ hq (he J)

/-- For `q > 1` and `n ≥ 1` the envelope ratio `q^{−6n}` is `< 1`. -/
theorem envelope_ratio_lt_one (q : K) (hq : 1 < q) (n : ℤ) (hn : 1 ≤ n) : q ^ (-6 * n) < 1 :=
  zpow_lt_one_of_neg₀ hq (by omega)

end QOU.Observations.ColouredLadderTwist
