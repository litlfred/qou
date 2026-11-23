*Proof.*
Invariance of the defining equation:

$$
  y^2  =  (\zeta_5 x)^5 - 1
      =  \zeta_5^{\,5}\, x^5 - 1
      =  x^5 - 1,
$$

using $\zeta_5^{\,5} = 1$.  So $\phi_5$ sends points of $\mathcal{X}_5$
to points of $\mathcal{X}_5$.  Iteration gives
$\phi_5^{\,k}(x, y) = (\zeta_5^{\,k} x, y)$, and $\phi_5^{\,5} = \mathrm{id}$
because $\zeta_5^{\,5} = 1$.  Order $5$: if $\phi_5^{\,k} = \mathrm{id}$
then $\zeta_5^{\,k} x = x$ at the point $(2, \sqrt{31})$, forcing $\zeta_5^{\,k} = 1$,
and hence $5 \mid k$ because $\zeta_5 = e^{2\pi i/5}$ is a primitive fifth root
of unity.  The map is bijective with inverse $\phi_5^{\,4}$, and both are
polynomial, so $\phi_5$ is an automorphism of the affine curve; it extends
to the smooth projective model, fixing the single point at infinity.  $\square$
