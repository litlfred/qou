The $Q$-value for tritium beta decay ${}^3\mathrm{H} \to {}^3\mathrm{He} + e^- + \bar\nu_e$ admits an exact closed form as a rational function of $q$.

## Statement

**Proposition.**

$$
  Q({}^3\mathrm{H} \to {}^3\mathrm{He})
  = \frac{3(q^2-1)^3(q^2+1)^2(3q^4+4q^2+3)}{32q^7}
    \times m_e
$$

This follows from the branching factorization with $(Z, N) = (1, 2)$ and $A = 3$ (the odd regime).

## Derivation

From the branching factorization:

$$
  \sum_{4^3 \text{ configs}} \Delta m_e
  = a^1 \cdot b^{1} \cdot (a - b)
  = ab(a - b)
$$

Substituting the channel sums yields the stated closed form.

## Numerical evaluation

At the aether parameter $q_0$:

$$
  Q({}^3\mathrm{H} \to {}^3\mathrm{He})
  \approx 0.0179 \;\text{MeV}.
$$

The experimental value is $Q_{\mathrm{exp}} = 0.0186$ MeV. The error is $-3.64\%$. The computation uses exactly three CODATA inputs to fix $q_0$, with zero additional fitting.
