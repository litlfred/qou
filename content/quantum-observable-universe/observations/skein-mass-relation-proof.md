
The electron is identified with the trefoil $3_1$, a torus knot with
$\mathrm{Vol}(3_1) = 0$. Its mass therefore sits at the base of the
topological tower: it is the unit against which all other masses are measured.
The muon is identified with the figure-eight knot $4_1$, whose complement
carries a complete hyperbolic structure of volume
$\mathrm{Vol}(4_1) \approx 2.02988$.

Applying the [topological mass theorem](#thm:topological-mass) to the muon--electron mass
*ratio* eliminates the overall mass scale and gives

$$
  \frac{m_\mu}{m_e}
  \;=\;
  \frac{\mathrm{Vol}(4_1) / \hbar_q^{\,2}}{m_e / m_e}
  \;=\;
  \frac{\mathrm{Vol}(4_1)}{\hbar_q^{\,2}}.
$$

Substituting $\hbar_q = 1 - q^{-1}$ and the CODATA value
$m_\mu / m_e = 206.768\,2827(46)$, one solves for $\hbar_q$:

$$
  \hbar_q^{\,2}
  = \frac{\mathrm{Vol}(4_1)}{m_\mu / m_e}
  = \frac{2.02988}{206.7683}
  \approx 0.009\,817,
  \qquad
  \hbar_q \approx 0.09908.
$$

Inverting $\hbar_q = 1 - 1/q$ yields
$1/q = 1 - 0.09908 = 0.90092$, so

$$
  q \;\approx\; 1.10997.
$$

The Skein relation itself is the mass-functional analogue of the Kauffman
bracket recursion. At each crossing in the color-exchange diagram of a
hadron, the three resolutions $L_+$, $L_-$, $L_0$ satisfy
$q\,\mathcal{M}(L_+) - q^{-1}\mathcal{M}(L_-) = (q^{1/2}-q^{-1/2})\,\mathcal{M}(L_0)$. This relation is inherited from the
$q$-deformed $\mathrm{SU}(2)$ Chern--Simons functional on the
$1$-jet bundle prolongation of the CR manifold
(see [Chapter](#chap:path-integrals-braiding)).
