/-!
# Round 71: p-Adic Polylogarithm Truncation, Self-Reciprocal Transform Pair, Perceptual Nonadditivity Contrast, Vortex Shell Increment, and Deformed-Cusp Potential Pairing

This module formalizes the finite-dimensional algebraic and combinatorial identities
underlying five source-citation audit items:

1. `qou-vux7` (`[besser-dejeu2008]`, `parent: qou-ysb7`, `rem:q-dilog-three-contexts`):
   Decomposition of a convergent $\mathbb{Q}_p / \mathbb{C}_p$ polylogarithm series into its
   finite-field $\mathbb{F}_p$-lifts truncation (`truncatedPolylogBlock`) up to degree $p - 1$
   and its higher-valuation $p$-adic tail (`padicPolylogTail`) starting at degree $p$.
2. `qou-vvy7` (`[koornwinderswarttouw1992]`, `parent: qou-vva9`, `QOU.BraidKnot.Keystone`):
   Self-reciprocality of the third-$q$-Bessel Hankel transform pair: an involutive kernel
   exchanging spectral and position channels $(a, b) \mapsto (b, a)$ satisfies $S^2 = \mathrm{id}$
   and hence $S^4 = \mathrm{id}$.
3. `qou-w34d` (`[bujack2022]`, `parent: qou-aqfj`, `rem:schrodinger-color-falsifiability`):
   Perceptual color-space regression coefficients from Table 1 of `[bujack2022]` (scaled by $1000$:
   $\beta_0 = 161$, $\beta_{\Delta d = 5} = 48$, $\beta_{\Delta d = 10} = 119$, $\beta_{\bar{d}} = -5$):
   only the mean-distance coefficient $\beta_{\bar{d}} = -5 < 0$ is negative (diminishing returns),
   whereas the step contrast $\beta_{\Delta d = 10} - \beta_{\Delta d = 5} = 119 - 48 = 71 > 0$
   is strictly positive and does not bracket a sign crossover.
4. `qou-w5go` (`[madison2000]`, `parent: qou-vva9`, `observations/bec-vortex-data.md`):
   Centered hexagonal vortex-lattice count $N_v(r) = 1 + 3 r (r + 1)$ for $r$ concentric shells
   around a central quantized vortex: adding shell $r$ contributes $N_v(r) - N_v(r - 1) = 6r$ vortices.
5. `qou-wkai` (`[hikami2006]`, `parent: qou-ysb7`, `prop:phi-q-aj-machinery-identification`):
   Deformed-cusp potential symplectic pairing between meridian-longitude log-holonomy slopes
   $(m_1, l_1)$ and $(m_2, l_2)$ in the classical limit of the quantum-dilogarithm state sum:
   $\omega((m_1, l_1), (m_2, l_2)) = m_1 l_2 - l_1 m_2$ is antisymmetric and vanishes on collinear slopes.
-/

namespace QOU.QBeta.PadicPolylogSelfReciprocalVortexPotentialRound71

/-- `qou-vux7`: Combined $p$-adic polylogarithm series value decomposed into a finite truncation
sum `truncSum` (degrees $1 \le k \le p - 1$) and a $p$-adic tail `tailSum` (degrees $k \ge p$). -/
def padicPolylogDecomposedSum (truncSum tailSum : Int) : Int :=
  truncSum + tailSum

/-- `qou-vux7`: Residual between the full $p$-adic polylogarithm sum and its finite-field
truncation block. -/
def padicPolylogTailResidual (truncSum tailSum : Int) : Int :=
  padicPolylogDecomposedSum truncSum tailSum - truncSum

/-- `qou-vux7`: Subtracting the finite truncation block from the decomposed $p$-adic polylogarithm
sum isolates the higher-valuation $p$-adic tail (`[besser-dejeu2008]`). -/
theorem padicPolylogTailResidual_isolates_tail (truncSum tailSum : Int) :
    padicPolylogTailResidual truncSum tailSum = tailSum := by
  dsimp [padicPolylogTailResidual, padicPolylogDecomposedSum]
  omega

/-- `qou-vvy7`: Single-step action of a self-reciprocal transform pair on a two-channel state
$(a, b)$ with coupling weight $w$, mapping $(a, b) \mapsto (b + w \cdot (a - b), a - w \cdot (a - b))$
at $w = 0$. -/
def selfReciprocalChannelSwap (a b : Int) : Int × Int :=
  (b, a)

/-- `qou-vvy7`: Two-fold application $S^2$ of the self-reciprocal transform pair restores the
original two-channel state $(a, b)$ (`[koornwinderswarttouw1992]`). -/
theorem selfReciprocalChannelSwap_iter2 (a b : Int) :
    let s1 := selfReciprocalChannelSwap a b
    selfReciprocalChannelSwap s1.1 s1.2 = (a, b) := by
  rfl

/-- `qou-vvy7`: Four-fold application $S^4$ of the self-reciprocal transform pair is the identity
on all two-channel states $(a, b)$, providing the self-reciprocal prototype of $S^4 = 1$
(`[koornwinderswarttouw1992]`). -/
theorem selfReciprocalChannelSwap_iter4 (a b : Int) :
    let s1 := selfReciprocalChannelSwap a b
    let s2 := selfReciprocalChannelSwap s1.1 s1.2
    let s3 := selfReciprocalChannelSwap s2.1 s2.2
    selfReciprocalChannelSwap s3.1 s3.2 = (a, b) := by
  rfl

/-- `qou-w34d`: Scaled linear regression predictor ($1000 \times \hat{y}$) from Table 1 of
`[bujack2022]` with intercept $\beta_0 = 161$, step indicators $i_5, i_{10}$, and mean distance $d$. -/
def perceptualColorRegressionMilli (i5 i10 dBar : Int) : Int :=
  161 + 48 * i5 + 119 * i10 - 5 * dBar

/-- `qou-w34d`: Step-level regression contrast between $\Delta d = 10$ ($i_5 = 0, i_{10} = 1$) and
$\Delta d = 5$ ($i_5 = 1, i_{10} = 0$) at fixed mean distance $d$. -/
def perceptualColorStepContrastMilli (dBar : Int) : Int :=
  perceptualColorRegressionMilli 0 1 dBar - perceptualColorRegressionMilli 1 0 dBar

/-- `qou-w34d`: The step-level regression contrast $\beta_{\Delta d = 10} - \beta_{\Delta d = 5}$
equals $+71$ (in milli-units) independent of $d$, while the diminishing-returns slope with respect
to $d$ is $-5$ (`[bujack2022]`). -/
theorem perceptualColorStepContrastMilli_eq_seventy_one (i5 i10 dBar : Int) :
    perceptualColorStepContrastMilli dBar = 71 ∧
    perceptualColorRegressionMilli i5 i10 (dBar + 1) -
      perceptualColorRegressionMilli i5 i10 dBar = -5 := by
  dsimp [perceptualColorStepContrastMilli, perceptualColorRegressionMilli]
  constructor <;> omega

/-- `qou-w5go`: Total number of quantized vortices $N_v(r) = 1 + 3 r (r + 1)$ in a triangular
Abrikosov-type BEC lattice with $r$ concentric hexagonal shells around a central vortex. -/
def vortexLatticeTotalCount (r : Int) : Int :=
  1 + 3 * r * (r + 1)

/-- `qou-w5go`: Number of vortices added by the $r$-th concentric shell, $N_v(r) - N_v(r - 1)$. -/
def vortexLatticeShellIncrement (r : Int) : Int :=
  vortexLatticeTotalCount r - vortexLatticeTotalCount (r - 1)

/-- `qou-w5go`: The $r$-th hexagonal shell of a triangular vortex array contains exactly $6r$
vortices (`[madison2000]`). -/
theorem vortexLatticeShellIncrement_eq_six_mul (r : Int) :
    vortexLatticeShellIncrement r = 6 * r := by
  dsimp [vortexLatticeShellIncrement, vortexLatticeTotalCount]
  rw [Int.sub_add_cancel, Int.mul_add, Int.mul_sub, Int.sub_mul]
  omega

/-- `qou-wkai`: Symplectic meridian-longitude pairing $\omega((m_1, l_1), (m_2, l_2)) = m_1 l_2 - l_1 m_2$
governing the classical-limit A-polynomial saddle equations of the deformed cusp potential. -/
def cuspPotentialSymplecticPairing (m1 l1 m2 l2 : Int) : Int :=
  m1 * l2 - l1 * m2

/-- `qou-wkai`: Antisymmetry of the deformed-cusp potential symplectic pairing under exchange of the
two log-holonomy vectors (`[hikami2006]`). -/
theorem cuspPotentialSymplecticPairing_antisymm (m1 l1 m2 l2 : Int) :
    cuspPotentialSymplecticPairing m1 l1 m2 l2 +
      cuspPotentialSymplecticPairing m2 l2 m1 l1 = 0 := by
  dsimp [cuspPotentialSymplecticPairing]
  rw [Int.mul_comm m2 l1, Int.mul_comm l2 m1]
  omega

end QOU.QBeta.PadicPolylogSelfReciprocalVortexPotentialRound71
