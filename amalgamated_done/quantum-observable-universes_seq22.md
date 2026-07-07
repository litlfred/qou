<!-- FILE_START: q-harmonic-analysis-intro.md -->
We build heat-flow, Laplace, Fourier, and resolvent calculus on top of the $q$-deformed operators. The framework organises around the $q$-shuffle Hopf algebra $\mathcal{H}_q$ and its grouplikes $\exp_q, \log_q, \mathrm{Li}_2^q$.
<!-- FILE_END: q-harmonic-analysis-intro.md -->

<!-- FILE_START: q-heat-equation.md -->
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a quantum observable universe with $q$-Laplacian $\Delta_q$. The **$q$-heat equation** is the evolution equation

$$
  \partial_t u \;=\; -\Delta_q u
$$

for a time-dependent section $u \colon \mathbb{R}_{\ge 0} \times \mathcal{S} \to \mathbf{1}_{\mathbf{C}}$, where $t$ is the Reeb-flow parameter evaluated in units of the Planck step $t_P(q) = q/(q - 1)$.
<!-- FILE_END: q-heat-equation.md -->

<!-- FILE_START: q-heat-equation-elaboration.md -->
The Reeb time $t$ evolves at fixed cosmological time $q$. The left-hand side $\partial_t$ acts as the infinitesimal generator of the Reeb translation. The equation decomposes as

$$
  \partial_t u  =  -q^{-2}\Delta u - q^{-1}(1 - q^{-1})[\text{Coriolis}]u - (1 - q^{-1})^2\Delta_\xi u,
$$

balancing classical diffusion across the base manifold, Reeb-spin diffusion along the internal Reeb fibre, and Coriolis cross-coupling. Because $\Delta_q$ is a polynomial operator in $q, q^{-1}$, the $q$-heat equation holds over any commutative ring in which $q - 1$ is invertible.
<!-- FILE_END: q-heat-equation-elaboration.md -->

<!-- FILE_START: q-heat-equation-exists.md -->
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a quantum observable universe with initial data $u_0 \colon \mathcal{S} \to \mathbf{1}_{\mathbf{C}}$. There exists a formal solution $u(t)$ of the $q$-heat equation $\partial_t u = -\Delta_q u$ with $u(0) = u_0$.
<!-- FILE_END: q-heat-equation-exists.md -->

<!-- FILE_START: q-heat-equation-unique.md -->
Given initial data $u_0$, the solution $u(t)$ of the $q$-heat equation is uniquely determined as the $\exp(-t \Delta_q) u_0$ semigroup orbit.
<!-- FILE_END: q-heat-equation-unique.md -->

<!-- FILE_START: categorical-laplace-transform.md -->
The **categorical Laplace transform** is the monoidal functor

$$
  \mathcal{L}\colon \bigl(\mathrm{End}_{\mathbf{C}}(A), \ast_q\bigr) \;\longrightarrow\; \bigl(\mathrm{End}_{\mathbf{C}}(A), \cdot\bigr)
$$

defined by the Hopf pairing against the real exponential grouplike $\exp_q(-s\cdot) \in G(\mathcal{H}_q)$:

$$
  \mathcal{L}[f](s) \;=\; \mathrm{tr}_M\bigl(\exp_q(-s\cdot)  \cdot  f\bigr).
$$

$\mathcal{L}$ intertwines $q$-convolution with pointwise product, uniquely characterising it as the mate of the comultiplication $\Delta_q$ on $\mathcal{H}_q$.
<!-- FILE_END: categorical-laplace-transform.md -->

<!-- FILE_START: categorical-laplace-transform-properties.md -->
The transform $\mathcal{L}$ applies over any base ring $R$ where $\mathcal{H}_q$ supports the grouplike. Evaluating the pairing against the archimedean realisation recovers the integral $\int_0^\infty e^{-st} f(t) dt$.
<!-- FILE_END: categorical-laplace-transform-properties.md -->

<!-- FILE_START: categorical-laplace-three-contexts.md -->
Over $\mathbb{F}_p$, $\mathcal{L}$ becomes a finite sum over the grouplike spectrum. Over $\mathbb{Q}_p$, $\mathcal{L}$ is a continuous functional on locally constant functions. Over $\mathbb{C}_p$, $\mathcal{L}$ extends to rigid-analytic functions on the open disc.
<!-- FILE_END: categorical-laplace-three-contexts.md -->

<!-- FILE_START: categorical-laplace-q-heat-resolvent.md -->
The Laplace transform converts the $q$-heat equation into the spectral equation $s \hat{u}(s) - u_0 = -\widehat{\Delta_q} \hat{u}(s)$. This yields the resolvent of the $q$-Laplacian, $\hat{u}(s) = (s + \widehat{\Delta_q})^{-1} u_0$.
<!-- FILE_END: categorical-laplace-q-heat-resolvent.md -->

<!-- FILE_START: categorical-laplace-transform-exists.md -->
The categorical Laplace transform exists as a monoidal functor $(\mathrm{End}_{\mathbf{C}}(A), \ast_q) \to (\mathrm{End}_{\mathbf{C}}(A), \cdot)$.
<!-- FILE_END: categorical-laplace-transform-exists.md -->

<!-- FILE_START: categorical-laplace-transform-unique.md -->
The categorical Laplace transform is uniquely characterised as the mate of the coproduct $\Delta_q$ on $\mathcal{H}_q$ under the Frobenius pairing.
<!-- FILE_END: categorical-laplace-transform-unique.md -->

<!-- FILE_START: categorical-fourier-transform.md -->
The **categorical Fourier transform** pairs against the unitary grouplike $\exp_q(i\xi\cdot)$:

$$
  \mathcal{F}\colon \bigl(\mathrm{End}_{\mathbf{C}}(A), \ast_q\bigr) \;\longrightarrow\; \bigl(\mathrm{End}_{\mathbf{C}}(A), \cdot\bigr), \qquad \mathcal{F}[f](\xi) \;=\; \mathrm{tr}_M\bigl(\exp_q(i\xi\cdot) \cdot f\bigr),
$$

where $\xi$ ranges over the categorical spectrum $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, A^\vee)$.
<!-- FILE_END: categorical-fourier-transform.md -->

<!-- FILE_START: categorical-fourier-transform-properties.md -->
When $G = \mathrm{SU}_q(2)$, the Tannaka--Krein reconstruction identifies $\mathcal{F}$ with the Peter--Weyl decomposition. Applying $\mathcal{F}$ to the $q$-heat equation diagonalises the $q$-Laplacian on each Peter--Weyl summand, producing the Peter--Weyl heat kernel. The algebraic Fourier transform via Peter--Weyl projection functions identically over $\mathbb{F}_p$, $\mathbb{Q}_p$, and $\mathbb{Z}[q, q^{-1}]$.
<!-- FILE_END: categorical-fourier-transform-properties.md -->

<!-- FILE_START: categorical-fourier-brings-dft.md -->
When $G = C_5$ and $q = 1$, the transform degenerates to the classical discrete Fourier transform on $\mathbb{Z}/5$. Fourier decomposition separates spectral components, rendering collision invisible and securing the smoothness of the Briggs--Klein chart on Bring's surface.
<!-- FILE_END: categorical-fourier-brings-dft.md -->

<!-- FILE_START: categorical-fourier-transform-exists.md -->
The categorical Fourier transform exists as a monoidal functor.
<!-- FILE_END: categorical-fourier-transform-exists.md -->

<!-- FILE_START: categorical-fourier-transform-unique.md -->
The categorical Fourier transform is uniquely determined as the Wick rotation of the Laplace transform, coinciding with the Peter--Weyl decomposition in the Tannakian setting.
<!-- FILE_END: categorical-fourier-transform-unique.md -->
