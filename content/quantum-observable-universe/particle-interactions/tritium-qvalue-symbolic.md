The $Q$-value for tritium beta decay ${}^3\mathrm{H} \to {}^3\mathrm{He} + e^- + \bar\nu_e$ admits an exact closed form as a rational function of $q$.

## Statement

**Proposition.**

$$
  Q({}^3\mathrm{H} \to {}^3\mathrm{He})
  = \frac{3(q^2-1)^3(q^2+1)^2(3q^4+4q^2+3)}{32q^7}
    \times m_e
$$

This is the simplest non-trivial application of the [branching factorization](#prop:branching-qvalue-factorization). We have $(Z, N) = (1, 2)$ and $A = 3$ (the odd regime).

## Derivation

From the branching factorization with $Z = 1$ and $N = 2$:

$$
  \sum_{4^3 \text{ configs}} \Delta m_e
  = a^1 \cdot b^{1} \cdot (a - b)
  = ab(a - b)
$$

Substitute the channel sums $a = -h/2$ and $b = -3(q^2-1)(q^2+1)^2/(4q^3)$:

$$
  Q = |ab(a-b)| \times m_e.
$$

This simplifies to the stated closed form.

## Numerical evaluation

At the substrate parameter $q_0 = 1.109978595554181\ldots$ (50 decimal places):

$$
  Q({}^3\mathrm{H} \to {}^3\mathrm{He})
  \approx 0.0179 \;\text{MeV}.
$$

The experimental value is $Q_{\mathrm{exp}} = 0.0186$ MeV. The error is $-3.64\%$. The entire computation uses exactly three CODATA inputs ($\mathrm{Vol}(4_1)$, $m_\mu/m_e$, $m_e$) to fix $q_0$, with zero additional fitting.
