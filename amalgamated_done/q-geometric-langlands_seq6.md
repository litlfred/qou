<!-- FILE_START: spectral-trace-intro.md -->
Having identified the unit particle as a cohomological defect, we count these defects across the spectral fiber. The maximal ideals of $\mathcal{O}_q(\mathcal{B})$ act as the primes of the quantum geometry. Counting them with appropriate weights yields $q$-analogs of classical arithmetic functions. Defect-counting on the geometric side is dual to spectral decomposition on the algebraic side.

Tannaka--Krein duality bridges these two perspectives. The category of localized representations at defects is equivalent to the category of comodules over the Hopf algebra reconstructed from the Reeb spectrum. This equivalence converts the geometric sum over defects into a spectral trace over Reeb eigenvalues, providing the non-commutative analog of the classical explicit formula from prime number theory.
<!-- FILE_END: spectral-trace-intro.md -->

<!-- FILE_START: q-von-mangoldt-function.md -->
To measure the arithmetic weight of fundamental defects in a quantum observable universe, we deform the classical von Mangoldt function. 

We define the **$q$-von Mangoldt function** over the maximal ideals $\mathfrak{m}$ of the coordinate ring $\mathcal{O}_q(\mathcal{B})$. Let $N(\mathfrak{m})$ denote the norm of $\mathfrak{m}$, given by the cardinality of its residue field. We set:

$$
\Lambda_q(\mathfrak{m}) = \begin{cases}
\dfrac{N(\mathfrak{m})^{\hbar_q} - 1}{\hbar_q} & \text{if } \mathfrak{m} \text{ corresponds to a fundamental defect}, \\[6pt]
0 & \text{otherwise}.
\end{cases}
$$

A maximal ideal constitutes a fundamental defect if it lies over a prime ideal of the center of $A$. The fraction $\frac{N(\mathfrak{m})^{\hbar_q} - 1}{\hbar_q}$ deforms the classical logarithm. As $q \to 1$, we have $\hbar_q \to 0$. L'Hôpital's rule recovers $\Lambda_q(\mathfrak{m}) \to \log N(\mathfrak{m}) = \Lambda(\mathfrak{m})$, restoring the classical von Mangoldt function.
<!-- FILE_END: q-von-mangoldt-function.md -->

<!-- FILE_START: q-chebyshev-function.md -->
We define the **$q$-Chebyshev function** as the partial sum of the $q$-von Mangoldt function over the geometry:

$$
\psi_q(X) = \sum_{\substack{\mathfrak{m} \in \mathrm{MaxSpec}(\mathcal{O}_q(\mathcal{B})) \\ N(\mathfrak{m}) \le X}} \Lambda_q(\mathfrak{m}).
$$

This $q$-deformed prime counting function accumulates the weights of fundamental defects ordered by norm. The function $\psi_q(X)$ encodes the distribution of matter across the spectral fiber, weighted by the quantum Planck constant. In the classical limit $q \to 1$, we recover the classical Chebyshev function $\psi(X)$.
<!-- FILE_END: q-chebyshev-function.md -->

<!-- FILE_START: tannaka-krein-isomorphism.md -->
Tannaka--Krein duality establishes a self-duality between two perspectives on the substrate:

$$
\mathbf{Rep}_{\mathrm{loc}}(A) \simeq \mathbf{Comod}(\mathcal{H}_\xi).
$$

Here, $\mathbf{Rep}_{\mathrm{loc}}(A)$ is the category of localized $A$-module representations, supported at maximal ideals. The category $\mathbf{Comod}(\mathcal{H}_\xi)$ consists of comodules over the Hopf algebra $\mathcal{H}_\xi$ reconstructed from the Reeb spectrum. The geometric side of localized representations at defects matches the spectral side of global quantum group symmetries of the Reeb flow. The fibre functor $\tau$ underlying this equivalence sends each localized module to its fiber at the unit defect. The reconstruction theorem guarantees that $\mathcal{H}_\xi$ is uniquely determined by the monoidal structure of $\mathbf{Rep}_{\mathrm{loc}}(A)$.
<!-- FILE_END: tannaka-krein-isomorphism.md -->

<!-- FILE_START: tannaka-krein-su2.md -->
We execute the Tannaka--Krein reconstruction algorithm concretely for $\mathrm{SU}(2)$.

**Step 1: The monoidal category.** We start with $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ and the forgetful fibre functor $\tau \colon \mathbf{C} \to \mathrm{Vect}_\mathbb{C}$. The simple objects are $V_0, V_{1/2}, V_1, V_{3/2}, \ldots$ with dimension $\dim V_j = 2j + 1$.

**Step 2: Compute the coend.** The reconstructed Hopf algebra is $H = \mathrm{coend}(\tau^\vee \otimes \tau)$:

$$
  H = \bigoplus_{j \in \frac{1}{2}\mathbb{Z}_{\geq 0}}
      V_j^* \otimes V_j
  \bigg/ \sim.
$$

The relation $\sim$ identifies $(\tau(f)^* \otimes \mathrm{id})$ with $(\mathrm{id} \otimes \tau(f))$ for all morphisms $f$. The matrix coefficients $t^j_{m,m'} \in V_j^* \otimes V_j$ form a basis.

**Step 3: Reconstruct the algebra structure.** Multiplication on $H$ arises from the tensor product in $\mathbf{C}$. For the fundamental representation $V = V_{1/2}$, the four matrix coefficients $\alpha, \beta, \bar\alpha, \bar\beta$ generate $H$. The relations derive from the $R$-matrix:

$$
  \alpha\beta = q\,\beta\alpha, \quad
  \alpha\bar\alpha = q\,\bar\alpha\alpha, \quad
  \beta\bar\beta = \bar\beta\beta, \quad
  \alpha\bar\beta - \bar\beta\alpha = (q - q^{-1})\,\beta\bar\alpha,
$$

along with the quantum determinant $\alpha\bar\beta - q\,\beta\bar\alpha = 1$.

**Step 4: Reconstruct the coalgebra.** The comultiplication follows from the monoidal structure via $\Delta(t^j_{m,m'}) = \sum_{k} t^j_{m,k} \otimes t^j_{k,m'}$. On the generators:

$$
  \Delta\begin{pmatrix} \alpha & \beta \\ \bar\alpha & \bar\beta \end{pmatrix}
  = \begin{pmatrix} \alpha & \beta \\ \bar\alpha & \bar\beta \end{pmatrix}
    \otimes
    \begin{pmatrix} \alpha & \beta \\ \bar\alpha & \bar\beta \end{pmatrix}.
$$

The counit is $\varepsilon(t^j_{m,m'}) = \delta_{mm'}$. The antipode is $S(\alpha) = \bar\beta$, $S(\beta) = -q^{-1}\beta$, $S(\bar\alpha) = -q\bar\alpha$, and $S(\bar\beta) = \alpha$. Equivalently, $S(u) = u^{-1}$ where $u = \bigl(\begin{smallmatrix} \alpha & \beta \\ \bar\alpha & \bar\beta \end{smallmatrix}\bigr)$.

**Result.** The algorithm outputs $H \cong \mathcal{O}_q(\mathrm{SU}(2))$. We recover the quantum coordinate ring entirely from the monoidal structure of its representation category. 

On Bring's quantum observable universe, $q$ assumes the value dictated by the Descartes condition. The reconstruction then yields $\mathcal{O}_{q_{\mathrm{Bring}}}(\mathrm{SU}(2))$ equipped with its $S_5$-equivariant structure. The weight spaces of $H$ automatically encode the Reeb spectrum.
<!-- FILE_END: tannaka-krein-su2.md -->

<!-- FILE_START: explicit-formula.md -->
Tannaka--Krein self-duality induces a discrete Fourier transform over the spectral-geometric space. The explicit formula equates the geometric sum over defects to the spectral trace over Reeb eigenvalues:

$$
\psi_q(X) = X - \sum_{\rho \in \mathrm{Spec}(\xi_q)} \frac{X^\rho}{[\rho]_q} - \ln_q(2\pi\Omega_q) - \frac{1}{2}\ln_q(1 - X^{-2})
$$

where $[\rho]_q = \frac{q^\rho - q^{-\rho}}{q - q^{-1}}$ is the $q$-integer, $\Omega_q$ is the Reeb period, and $\ln_q$ is the $q$-logarithm.

The leading term $X$ measures the smooth background growth of defect density. The sum over $\mathrm{Spec}(\xi_q)$ captures fluctuations driven by Reeb eigenvalues, where each $\rho$ contributes a wave of amplitude $X^\rho / [\rho]_q$. The constant and tail terms arise from trivial eigenvalues and functional equation symmetry. This formula provides the non-commutative analog of the explicit formula of prime number theory.
<!-- FILE_END: explicit-formula.md -->

<!-- FILE_START: yekutieli-quantum-li.md -->
The spectral trace over Reeb eigenvalues acts as a matrix-valued promotion of the classical logarithmic integral $\mathrm{Li}(x) = \int_2^x \frac{dt}{\ln t}$.

In classical analytic number theory, $\mathrm{Li}(x)$ integrates the scalar probability $1/\ln t$ of finding a prime near $t$. The logarithm converts multiplication to addition, and the integral sums independent contributions into a single real number. This structure is purely abelian. 

The quantum substrate counts defects via the nonabelian multiplicative integral. Instead of summing scalar weights $1/\ln t$, one computes a path-ordered product of matrices along the Reeb flow. Each factor encodes the parallel transport of the adjoint representation $\mathrm{Ad}(A)$ along one orbit of $\xi_q$. The ordering reflects the non-commutativity of the gauge connection.

The multiplicative integral formally replaces $\mathrm{Li}(x)$:

| Classical | Quantum substrate |
|-----------|-------------------|
| Scalar weight $1/\ln t$ | Matrix weight $X^\rho / [\rho]_q$ (trace of holonomy) |
| Ordinary integral $\int dt$ | Path-ordered product $\prod^{\to}$ |
| Additive (abelian) | Multiplicative (nonabelian) |
| Result: real number $\mathrm{Li}(x)$ | Result: holonomy matrix in $\mathrm{GL}(V)$ |

This construction relies on the nonabelian Stokes theorem. Just as the classical Stokes theorem reduces a 2-dimensional integral to its 1-dimensional boundary, the nonabelian analog reduces the path-ordered product over a bounding surface to the holonomy around its boundary curve.

Applied to a prime orbit $\varrho_\mathfrak{m}$ of the Reeb flow, the 2-dimensional integral over any bounding surface collapses to the 1-dimensional holonomy around the prime knot itself. The counting weight for the prime $\mathfrak{m}$ is the holonomy of $\mathrm{Ad}(A)$ around the closed vortex filament corresponding to $\mathfrak{m}$.

The explicit formula requires $q$-integers $[\rho]_q$ rather than ordinary logarithms. The $q$-integer is the trace of the holonomy matrix in the fundamental representation. It captures the full nonabelian transport around the prime orbit. This multiplicative integral provides the precise formulation of the quantum $\mathrm{Li}(x)$.
<!-- FILE_END: yekutieli-quantum-li.md -->
