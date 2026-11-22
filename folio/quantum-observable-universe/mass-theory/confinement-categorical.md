*The collapse of the GB-filtration spectral sequence operates as the categorical analog of color confinement. Only central elements survive to the $E_\infty$-page. Colored non-central elements vanish cohomologically.*

The Frobenius integral factors through the center via the Wedderburn projection $\pi_Z$ and Plancherel weight $\mu$. Consequently, every physical observable partitions into a sum of discrete Wedderburn residues.

Precisely, let $A = H_{n+1}(q)$ over a field $K$ with $q \neq 0$ not a root of unity, let $\Phi : A \xrightarrow{\sim} \prod_{\lambda \vdash n+1} \mathrm{Mat}_{f^\lambda}(K)$ be the Wedderburn isomorphism, and assume every $f^\lambda$ is nonzero in $K$. Define $\pi_Z(x) = \Phi^{-1}\bigl(\bigl(\mathrm{tr}(\rho_\lambda x)/f^\lambda\bigr)\cdot 1\bigr)_\lambda$. For every trace $\tau : A \to K$:

1. $\pi_Z(x)$ lies in the center $Z(A) = \bigoplus_\lambda K\, e_\lambda$, where $e_\lambda = \Phi^{-1}(1_\lambda)$;
2. $\tau = \tau \circ \pi_Z$, and $\tau(x) = \sum_\lambda \tau(e_\lambda)\,\mathrm{tr}(\rho_\lambda x)/f^\lambda$, so the weights $\mu_\lambda = \tau(e_\lambda)$ are the Plancherel weights of $\tau$;
3. every central $x$ satisfies $\pi_Z(x) = x$.

The identification of $Z(A)$ with the $E_\infty^{0,0}$ page uses the vanishing of $\mathrm{HH}^k(A)$ for $k \geq 1$, which is not part of the formal statement.
