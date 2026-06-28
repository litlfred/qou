The $+1$ additive term in the Q-value formula is **not** a
fitting constant — it is the positron mass $m_{e^+}/m_e = 1$,
recovered from the $\gamma\gamma \to e^- e^+$ pair production
vertex ([Breit–Wheeler](#def:breit-wheeler-pair-production)).

## Statement

**Proposition.**
*The character sum $\Sigma_\lambda \chi_\lambda(\Delta)$
subtracts the categorical action of* both *fermions produced
in pair creation (2 units of $m_e$), but the Q-value subtracts
only the emitted electron (1 unit).  The difference is the
positron action:*

$$
  Q = \Sigma_{\mathrm{char}} \times m_e + 1 \times m_e
$$

*where the $+1$ is $m_{e^+}/m_e$.*

## Applicability of the correction

The positron correction is needed in two regimes
([parity regime selection](#thm:parity-regime-selection)):

1. **$A = 1$** (neutron decay): no spectators absorb the
   positron action.  The correction is added explicitly:
   $Q = (S\Delta + 1) \times m_e$.

2. **Even $A$**: the spectator factorization gives a negative
   raw sum.  After Frobenius filtering, the positron correction
   restores the physical Q-value:
   $Q = (\Sigma_{\mathrm{FP}} + 1) \times m_e$.

For **odd $A \geq 3$**: the spectator product absorbs the
positron action automatically through the sign structure,
and no explicit correction is needed:
$Q = |S\Delta| \times m_e$.

## Physical interpretation

In the pair production vertex $\gamma\gamma \to e^- e^+$,
the photon energy creates both an electron and a positron.
The character sum counts the total fermionic action change
(both particles), while the Q-value is defined as the kinetic
energy available to the emitted electron alone.
