Continuing [Example](#ex:higher-forms-su2), the Hodge star on
$A = \mathcal{O}(\mathrm{SU}(2))$ acts on the $3D$-calculus
$\Omega^{\bullet}(A)$ as follows. The volume form is
$\mathrm{vol} = \omega_1 \wedge \omega_2 \wedge \omega_3$
(normalised by $\lambda(\mathrm{vol}) = 1$). Then:

- $\star 1 = \mathrm{vol}$,
  $\star\mathrm{vol} = 1$.
- On $1$-forms: $\star\omega_i = \tfrac{1}{2}\epsilon_{ijk}\,
  \omega_j \wedge \omega_k$ (each basis form maps to its
  complementary $2$-form).
- On $2$-forms: $\star(\omega_i \wedge \omega_j) =
  \epsilon_{ijk}\,\omega_k$ (each basis $2$-form maps to its
  complementary $1$-form).

The Hodge star is the categorical version of "rotating a form into
its complement": it identifies $\Omega^k(A)$ with $\Omega^{n-k}(A)$
using the Frobenius form as the inner product. The self-dual
$2$-forms $\Omega^+(A)$ are the $+1$-eigenspace of $\star$; in
$3$ dimensions, $\star$ on $\Omega^2(A)$ maps to $\Omega^1(A)$, so
the self-dual/anti-self-dual decomposition is trivial. The
non-trivial decomposition arises when $\dim H = 4$ (the archimedean
case, [Example](#prop:self-dual-curvature)).
