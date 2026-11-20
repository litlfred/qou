The $+1$ additive term in the Q-value formula is a parity-dependent offset $\delta_A$, required to match the evaluated character sum to the observed kinematics.

## Statement

**Proposition.**
*The evaluated Q-value functional includes a formal parity-dependent trace offset:*

$$
  Q = (\Sigma_{\mathrm{char}} + \delta_A) \times m_e
$$

*where the offset $\delta_A$ depends on the parity regime.*

## Applicability of the correction

The offset $\delta_A$ is applied differently across two regimes:

1. **$A = 1$** and **Even $A$**: The correction is added explicitly, setting $\delta_A = 1$.
2. **Odd $A \geq 3$**: No explicit correction is applied, setting $\delta_A = 0$.

> **Open Issue:** The alignment of the categorical evaluation with the kinematic Q-value currently relies on this parity-dependent $\delta_A$. There is no formal justification yet for why $\delta_A$ is absorbed for odd $A$ but required for even $A$.
