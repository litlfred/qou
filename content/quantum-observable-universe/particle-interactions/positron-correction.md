The $+1$ additive term in the Q-value formula is a parity-dependent offset $\delta_A$, required to match the evaluated character sum to the observed kinematics.

## Statement

**Proposition.**
*The evaluated Q-value functional includes a formal parity-dependent trace offset:*

$$
  Q = (\Sigma_{\mathrm{char}} + \delta_A) \times m_e
$$

*where the offset $\delta_A$ depends on the parity regime.*

## Applicability of the correction

We apply the offset $\delta_A$ differently across two regimes ([parity regime selection](#thm:parity-regime-selection)):

1. **$A = 1$** (neutron decay) and **Even $A$**:
   We add the correction explicitly, setting $\delta_A = 1$.
   $Q = (S\Delta + 1) \times m_e$ (for $A=1$).
   $Q = (\Sigma_{\mathrm{FP}} + 1) \times m_e$ (for even $A$).

2. **Odd $A \geq 3$**:
   We apply no explicit correction, setting $\delta_A = 0$.
   $Q = |S\Delta| \times m_e$.

> **Open Issue:** We currently rely on this parity-dependent $\delta_A$ to align the categorical evaluation with the kinematic Q-value. We lack a formal justification for why $\delta_A$ is absorbed for odd $A$ but required for even $A$.
