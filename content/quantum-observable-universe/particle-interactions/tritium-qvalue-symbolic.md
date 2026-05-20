The Q-value for tritium beta decay
${}^3\mathrm{H} \to {}^3\mathrm{He} + e^- + \bar\nu_e$
has an exact closed form as a rational function of $q$.

## Statement

**Proposition.**

$$
  Q({}^3\mathrm{H} \to {}^3\mathrm{He})
  = \frac{3(q^2-1)^3(q^2+1)^2(3q^4+4q^2+3)}{32q^7}
    \times m_e
$$

This is the simplest non-trivial application of the
[branching factorization](#prop:branching-qvalue-factorization)
with $(Z, N) = (1, 2)$, so $A = 3$ (odd regime).

## Derivation

From the branching factorization with $Z = 1$, $N = 2$:

$$
  \sum_{4^3 \text{ configs}} \Delta m_e
  = a^1 \cdot b^{1} \cdot (a - b)
  = ab(a - b)
$$

Substituting the channel sums $a = -h/2$ and
$b = -3(q^2-1)(q^2+1)^2/(4q^3)$:

$$
  Q = |ab(a-b)| \times m_e
$$

which simplifies to the stated closed form.

## Numerical evaluation

At $q_0 = 1.109978595554181\ldots$ (50 dps):

$$
  Q({}^3\mathrm{H} \to {}^3\mathrm{He})
  \approx 0.0179 \;\text{MeV}
$$

The experimental value is $Q_{\mathrm{exp}} = 0.0186$ MeV,
giving an error of $-3.64\%$.  The entire computation uses
three CODATA inputs ($\mathrm{Vol}(4_1)$, $m_\mu/m_e$, $m_e$)
to fix $q_0$, with zero additional fitting.
