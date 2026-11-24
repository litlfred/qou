import Mathlib.Tactic

/-!
# Convention D is the `U_q(𝔰𝔩₂)` fundamental quantum trace — and `𝔰𝔩₃` is not it

Bean `qou-d0qq`, prune P2 of
`docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md` §B.

On the fundamental representation `V` of `U_q(𝔰𝔩_N)`, the braiding `Ř` on `V ⊗ V` has
eigenvalue `q` on `Sym² V` and `−q⁻¹` on `Λ² V` (the paper's §7a normalisation
`(σ − q)(σ + q⁻¹) = 0`), so its quantum trace, normalised by the quantum dimension
`[N]_q²` of `V ⊗ V`, is the Markov parameter

    z_N = (q · dim_q Sym² V − q⁻¹ · dim_q Λ² V) / [N]_q².

With `dim_q Sym² V = [N]_q [N+1]_q / [2]_q` and `dim_q Λ² V = [N]_q [N−1]_q / [2]_q`
this collapses to `z_N = q^N / [N]_q`; the file states the two cases the plan needs
explicitly, from the quantum dimensions, so nothing about the general formula is
assumed:

* `zSL2_eq_zD` — `N = 2`: `(q[3]_q − q⁻¹) / [2]_q² = q³/(q²+1)`, i.e. exactly the
  framework's convention-D parameter `z_D` (`QOU.Mass.RouteCPivotalVsCount.zD`).
  This is the algebraic form of the `5 × 10⁻³¹` agreement the planning agent measured.
* `zSL3_eq` — `N = 3`: `(q[3]_q[4]_q/[2]_q − q⁻¹[3]_q) / [3]_q² = q⁵/(q⁴+q²+1)`.
* `zSL3_ne_zD` — the two are never equal: `z_3 = z_2` would force `q²(q²+1) =
  q⁴+q²+1`, i.e. `0 = 1`. No ordering, no `ℝ`: the plan expected an archimedean
  inequality here and it is not needed.

Consequence for the KZ front: the target algebra that reproduces the framework's
trace convention is `𝔰𝔩₂`, and the identification question is `q₀`-free.

Base ring: a generic `Field K`; the hypotheses are exactly the denominators.
-/

namespace QOU.Mass.SL2QuantumTraceIsZD

variable {K : Type*} [Field K]

/-- Symmetric quantum integer `[n]_q = q^{n-1} + q^{n-3} + ⋯ + q^{-(n-1)}`, the cases used. -/
def qint2 (q : K) : K := q + q⁻¹
def qint3 (q : K) : K := q ^ 2 + 1 + q⁻¹ ^ 2
def qint4 (q : K) : K := q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3

/-- `U_q(𝔰𝔩₂)`: `dim_q Sym² V = [3]_q`, `dim_q Λ² V = 1`. -/
def zSL2 (q : K) : K := (q * qint3 q - q⁻¹ * 1) / (qint2 q) ^ 2

/-- `U_q(𝔰𝔩₃)`: `dim_q Sym² V = [3]_q[4]_q/[2]_q`, `dim_q Λ² V = [3]_q`. -/
def zSL3 (q : K) : K :=
  (q * (qint3 q * qint4 q / qint2 q) - q⁻¹ * qint3 q) / (qint3 q) ^ 2

/-- Convention D, as in `RouteCPivotalVsCount`. -/
def zD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

theorem zSL2_eq_zD (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) : zSL2 q = zD q := by
  unfold zSL2 zD qint2 qint3
  have h2' : q + q⁻¹ ≠ 0 := by
    intro h
    apply h2
    have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [← this, h, mul_zero]
  field_simp
  ring

theorem zSL3_eq (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    zSL3 q = q ^ 5 / (q ^ 4 + q ^ 2 + 1) := by
  unfold zSL3 qint2 qint3 qint4
  have h2' : q + q⁻¹ ≠ 0 := by
    intro h
    apply h2
    have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [← this, h, mul_zero]
  have h3' : q ^ 2 + 1 + q⁻¹ ^ 2 ≠ 0 := by
    intro h
    apply h3
    have : q ^ 2 * (q ^ 2 + 1 + q⁻¹ ^ 2) = q ^ 4 + q ^ 2 + 1 := by field_simp
    rw [← this, h, mul_zero]
  field_simp
  ring

/-- `z_3 ≠ z_2` over every field: cross-multiplying `q⁵(q²+1) = q³(q⁴+q²+1)` leaves `q³ = 0`. -/
theorem zSL3_ne_zD (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    zSL3 q ≠ zD q := by
  rw [zSL3_eq q hq h2 h3]
  unfold zD
  intro h
  rw [div_eq_div_iff h3 h2] at h
  have hq3 : q ^ 3 = 0 := by linear_combination -h
  exact pow_ne_zero 3 hq hq3


/-- **Non-equality of `zSL3` and `zSL2` (`qou-8du0`).**
For `q ≠ 0`, `q ^ 2 + 1 ≠ 0`, and `q ^ 4 + q ^ 2 + 1 ≠ 0`, `zSL3 q ≠ zSL2 q`. -/
theorem zSL3_ne_zSL2 (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    zSL3 q ≠ zSL2 q := by
  rw [zSL2_eq_zD q hq h2]
  exact zSL3_ne_zD q hq h2 h3

end QOU.Mass.SL2QuantumTraceIsZD
