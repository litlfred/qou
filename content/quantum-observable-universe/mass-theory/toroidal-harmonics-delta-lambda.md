# Toroidal Harmonics and the $\Delta_\lambda$ Mass Gap

To bridge the mass calculation from the canonical base $m_{\text{can}}$ to the precision experimental frontier (AME2020), we must resolve the $\Delta_\lambda$ normalization shift (the shell-filling fraction $c_\lambda$).

## The Toroidal JSJ Equivalence

The Markov parameter recursion $c_k$ driving the strong-force topological trace is fundamentally a discrete evaluation of the knot complement's toroidal structure.

Let $q = e^{-\eta}$. The Markov parameter $z(q) = \frac{\sqrt{q}}{1+q}$ is equivalently parametrized by $w = z^2 = \frac{1}{2(\cosh\eta + 1)}$.
Under the change of variables $x = \cosh\eta = \frac{1}{2w} - 1$, the continuous Legendre differential equation for the Toroidal Harmonics (half-integer degree $n-1/2$):

$$ (1 - x^2) y'' - 2x y' + (n^2 - 1/4) y = 0 $$

Reduces *exactly* to the polynomial generating function ODE of the $z$-recursion:

$$ 4w^2(4w - 1) f'' + 16w^2 f' + (4n^2 - 1) f = 0 $$

This explicit map proves that the topological evaluation $B_{\text{sym}}$ is the discrete shadow of the Toroidal JSJ decomposition. The missing normalization factor for heavy nuclei ($\Delta_\lambda$) is therefore analytically resolvable as the evaluation of $P_{n-1/2}^m(\cosh\eta)$ over the SU(4) Plancherel measure.
