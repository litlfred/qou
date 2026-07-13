<!-- FILE_START: intro-q-resolvent-wick.md -->
We define the $q$-resolvent $R_q(s) = (s + \widehat{\Delta_q})^{-1}$ as a categorical Laplace transform of the $q$-heat semigroup. The categorical Wick rotation collapses the Laplace and Fourier transforms into a single grouplike pairing against $\exp_q \in G(\mathcal{H}_q)$ evaluated at $s$ or $i\xi$.
<!-- FILE_END: intro-q-resolvent-wick.md -->

<!-- FILE_START: q-resolvent.md -->
Let $\widehat{\Delta_q}$ be the $q$-Laplacian acting on $\mathrm{End}_{\mathbf{C}}(A)$, and let $s \in \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, A)$ be a categorical spectral parameter. The **$q$-resolvent** is the morphism

$$
  R_q(s) \;=\; \bigl(s + \widehat{\Delta_q}\bigr)^{-1} \;\in\; \mathrm{End}_{\mathbf{C}}(A),
$$

defined wherever $s + \widehat{\Delta_q}$ is invertible in the convolution algebra $\mathcal{H}_q$.
<!-- FILE_END: q-resolvent.md -->

<!-- FILE_START: q-resolvent-properties.md -->
$R_q(s)$ is the categorical Laplace transform of the $q$-heat semigroup $\exp(-t \widehat{\Delta_q})$:

$$
  R_q(s) \;=\; \mathrm{tr}_M\bigl(\exp_q(-s \cdot)  \cdot  \exp(-t \widehat{\Delta_q})\bigr).
$$

The first resolvent identity $R_q(s_1) - R_q(s_2) = (s_2 - s_1) R_q(s_1) R_q(s_2)$ is the Hopf-algebraic mate of the comultiplication axiom on $\mathcal{H}_q$. Under the categorical Fourier transform with $G = \mathrm{SU}_q(2)$, the resolvent diagonalises over irreducibles:

$$
  R_q(s) \;=\; \bigoplus_{j \in \widehat{G}} \frac{\pi_j}{s + \lambda_j(q)},
$$

where $\lambda_j(q) = [j]_q[j+1]_q (1 - q^{-1})^2$. 

The resolvent acts as the $s$-domain Green's function of the $q$-heat flow. Contour integration around a pole at $-\lambda_j(q)$ extracts the projector $\pi_j$ onto the $j$-isotypic subspace.
<!-- FILE_END: q-resolvent-properties.md -->

<!-- FILE_START: q-resolvent-exists.md -->
For $s \in \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, A)$ outside the categorical spectrum of $\widehat{\Delta_q}$, the $q$-resolvent $R_q(s) = (s + \widehat{\Delta_q})^{-1}$ exists as an endomorphism of $\mathrm{End}_{\mathbf{C}}(A)$.
<!-- FILE_END: q-resolvent-exists.md -->

<!-- FILE_START: q-resolvent-unique.md -->
The $q$-resolvent $R_q(s)$ is the unique morphism satisfying $(s + \widehat{\Delta_q}) \circ R_q(s) = \mathrm{id}$.
<!-- FILE_END: q-resolvent-unique.md -->

<!-- FILE_START: laplace-fourier-wick-rotation.md -->
The categorical Laplace and categorical Fourier transforms are two real forms of a single complex spectral pairing against the $q$-exponential grouplike $\exp_q \in G(\mathcal{H}_q)$:

$$
  \mathcal{F}[f](\xi) \;=\; \mathcal{L}[f](i\xi).
$$

This is the *categorical Wick rotation*. The $q$-heat equation $\partial_t u = -\Delta_q u$ and the Schrödinger-type equation $i\partial_t u = -\Delta_q u$ are sibling dynamics, evolving under $\tau = t + i\varTheta$. The Wick rotation acts only on the spectral parameter, securing base-ring independence where a primitive fourth root of unity exists.
<!-- FILE_END: laplace-fourier-wick-rotation.md -->
