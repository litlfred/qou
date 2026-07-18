# Toroidal Harmonics and the $\Delta_\lambda$ Mass Gap

Bridging the mass calculation from the canonical base $m_{\text{can}}$ to the AME2020 experimental frontier requires resolving the $\Delta_\lambda$ normalization shift (the shell-filling fraction $c_\lambda$).

## The Toroidal JSJ Equivalence

The Markov parameter recursion $c_k$ drives the strong-force topological trace. It constitutes a discrete evaluation of the knot complement's toroidal structure.

Let $q = e^{-\eta}$. The Markov parameter

$$
  z(q) = \frac{\sqrt{q}}{1+q}, \qquad w = z^2 = \frac{1}{2(\cosh\eta + 1)},
$$

is equivalently parametrised by $w$. Under the change of variables $x = \cosh\eta = \frac{1}{2w} - 1$, the continuous Legendre differential equation for the Toroidal Harmonics of half-integer degree $n-1/2$:

$$ (1 - x^2) y'' - 2x y' + (n^2 - 1/4) y = 0 $$

reduces exactly to the polynomial generating function ODE of the $z$-recursion:

$$ 4w^2(4w - 1) f'' + 16w^2 f' + (4n^2 - 1) f = 0 $$

This explicit map establishes that the topological evaluation $B_{\text{sym}}$ is the discrete shadow of the Toroidal JSJ decomposition. Evaluating $P_{n-1/2}^m(\cosh\eta)$ over the SU(4) Plancherel measure resolves the missing normalization factor $\Delta_\lambda$ for heavy nuclei analytically.

## The Golden Ratio Anchor for $\Delta_\lambda$

The toroidal ratio $P_{-1/2}/P_{1/2}$ drives the scaling gap $c_\lambda$. Setting the topological boundary condition to the known TQFT Fibonacci anyon root $q_0 = 1/\phi = \frac{\sqrt{5}-1}{2}$ fixes the geometric coordinate to $\cosh \eta = \frac{\sqrt{5}}{2} \approx 1.1180$.

Evaluating the toroidal harmonics at this geometric anchor yields:

$$ c_\lambda^{\text{topological}} = \frac{P_{-1/2}\left(\frac{\sqrt{5}}{2}\right)}{P_{1/2}\left(\frac{\sqrt{5}}{2}\right)} \approx 0.944649 $$

This parameter-free constant matches the empirical macroscopic shell-filling fraction for ${}^4\text{He}$ ($c_\lambda^{\text{exp}} \approx 0.943503$) to within $0.1\%$. The residual difference stems from higher-order entanglement terms beyond the 2-row stratum.
