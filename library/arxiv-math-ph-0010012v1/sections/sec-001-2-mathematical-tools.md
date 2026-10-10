---
doc_id: arxiv-math-ph-0010012v1
doc_title: "From random polynomials to symplectic geometry Steve Zelditch"
section_id: sec-001-2-mathematical-tools
section_title: "Mathematical Tools"
section_number: 2
pages: 2-3
source_pdf: 0010012v1.pdf
source_sha256: cd6eca5ccb81ff90
text_source: latex
latex_prose_ratio: 0.906
latex_coverage_ratio: 0.97
doc_brief: "From random polynomials to symplectic geometry Steve Zelditch — We review some recent results on random polynomials and their generalizations in complex and symplectic geometry."
---
We give a quick summary of some basic tools and methods that are used below. We will concentrate on general ideas and refer to [@SZ1; @SZ2; @BSZ3] for detailed expositions.

## Vector spaces of large dimension

In defining our ensembles of polynomials, we will be dealing with a sequence $( {\mathcal H}_N, \langle, \rangle_N)$ of Hilbert spaces of increasing dimension $d_N = dim {\mathcal H}_N$, where $N$ is the 'degree of the polynomial', a large integral (semiclassical) parameter. The dimension is given by a (Hilbert) polynomial of the form $d_N \sim a_0 N^m$ in the complex case (with $m = dim_{{\mathbb C}} M$) and by a function of polynomial growth $d_N \sim  a_0 N^{m - 1}$ in the real case (with $m = \mbox{dim}_{{\mathbb R}} M$).

In our applications, the spaces ${\mathcal H}_N$ will be one of the following.

###  Spherical harmonics and real eigenfunctions

We denote by $\Delta$ the standard Laplacian on $S^m$ and by ${\mathcal H}_N (S^m)$ the space of spherical harmonics of degree $N$ on $S^m.$ They are the eigenfunctions of $\Delta$ of eigenvalue $\lambda_{m,N} = N ( N + m - 1)$ and form a real vector space of dimension $d_{m, N} = \frac{2N + m -1}{N + m -1}
\left( \begin{array}{l} N + m -1 \\ \\ m -1 \end{array} \right)$.

More generally, we may consider the Laplacian $\Delta$ of any compact Riemannian manifold $(M, g)$. In place of spherical harmonics of degree $N$, we partition the spectrum of $\sqrt{\Delta}$ into intervals $[N  \log N, (N+ 1) \log (N + 1)]$ (the reason for the longer length is given in [@Ze2]), and let ${\mathcal H}_N$ denote the span of the eigenfunctions with eigenvalues in the $N$th interval. Linear combinations of such eigenfunctions are of course not eigenfunctions of $\Delta$, but they behave like polynomials of degree $N$ and their random linear combinations give a replacement for random spherical harmonics. Their use for modelling quantum ergodic and quantum mixing eigenfunctions is discussed [@Ze2; @HKZ].

### Holomorphic sections of positive line bundles

For any Kähler manifold $(M,\omega)$ of complex dimension $m$ there exists a holomorphic hermitian line bundle $(L, h) \to (M, \omega)$ whose Ricci curvature $Ric(h) = \omega$. $L$ is called *positive* since it posseses a metric of positive curvature, i.e. $\omega(X, JY)$ defines a Riemannian metric. We denote by $L^N$ the $N$th power of $L$ and by $H^0(M, L^N)$ the space of holomorphic sections. Its dimension $d_N = dim H^0(M, L^N)$ is given by the Hilbert polynomial $d_N = \frac{c_1(L)^m}{m!}
N^m + \cdots$ for sufficiently large $N$, where $\cdots$ represent the lower order terms. We equip $M$ with the volume form $dV_{\omega} = \frac{\omega^m}{m!}$ and $H^0(M, L^N)$ with the inner product $||s||^2 = \int_M h(s(z), s(z)) dV.$ For background we refer to [@GH].

In the simplest case of Riemann surfaces, examples include:

- $M = {\mathbb C}{\mathbb P}^1, L = {\mathcal O}(1), L^2 = T {\mathbb C}{\mathbb P}^1, h = h_{FS}, \omega = \omega_{FS}$ (Fubini study hermitian metric and curvature (1,1)-form). That $({\mathbb C}{\mathbb P}^1, \omega_{FS})$ is positively curved in the usual Riemannian sense is equivalent to positivity of $T{\mathbb C}{\mathbb P}^1$. $H^0({\mathbb C}{\mathbb P}^1, {\mathcal O}(2 N))$ may be interpreted as the space of holomorphic vector fields of type $(\frac{\partial}{\partial z})^N$. More simply put, sections are homogeneous holomorphic polynomials $s = \sum_{j = 0}^N c_k z_0^k z_1^{N - k}$ of degree $N$ in two complex variables. Such polynomials are known as the $SU(2)$-ensemble.

- $M = {\bf H}^2/\Gamma, L = T^*M, h_{FS} =$ hyperbolic metric. Hyperbolic surfaces are negatively curved in the Riemannian sense, so their tangent bundles are negatively curved, and their co-tangent bundles are positively curved. Holomorphic sections are holomorphic differentials of type $(dz)^N$.

- $M = {\mathbb C}/ {\mathbb Z}^2, \omega_0 = dz \wedge d\bar{z}$. The complex torus is flat in the Riemannian sense, so neither its tangent nor cotangent bundles are positively curved. The 'quantizing line bundle' with curvature $\omega_0$ is rather the bundle $\Theta$ whose sections are the classical theta-functions. The sections of $\Theta^N$ are known as theta-functions of level $N$.

### Almost holomorphic sections

Symplectic almost-complex manifolds $(M, J, \omega)$ possess a similar but analytically more complicated geometric quantization as spaces $H^0_J(M, L^N)$ of 'almost-holomorphic' sections. They are defined by a $\bar{D}$ complex over the $S^1$-bundle $X$ due to Boutet de Monvel -Guillemin [@BG]. What we need to know about these spaces is that their orthogonal projectors $\Pi_N$ have the same scaling asymptotics as in the complex case, if one works in suitable (Heisenberg) coordinates [@SZ2].

## Gaussian measures and spherical measures

We will restrict attention to two related ensembles:

- *Gaussian ensembles*: We fix an orthonormal basis $\{f_j\}$ of ${\mathcal H}_N$ and write functions as orthonormal sums $f = \sum_{j = 1}^{d_N} c_j f_j$. We then define the (complex) Gaussian measure by $$\gamma = e^{- ||f||^2} {\mathcal D}f,\;\; \mbox{i.e.} \;\; \gamma = e^{- |c|^2} dc.$$ More generally we fix a symmetric matrix $\Delta$ on ${\mathbb C}^{d_N}$ with positive (semi-)definite imaginary part and define: $$\begin{equation}
  \gamma_\Delta= \frac{e^{- \langle\Delta^{-1}
  c,c\rangle}}{(2\pi)^{p/2}\det\Delta}
  dc\,,\label{gaussian}
  \end{equation}$$ Gaussian ensembles come in both real and complex flavors. In the real case, the exponents acquire factors of $1/2$ and the denominator acquires a square root.

- *Spherical ensembles*: We denote by $S{\mathcal H}_N = \{f \in {\mathcal H}_N: ||f|| = 1\}.$ We then equip $S{\mathcal H}_N$ with the uniform (Haar) probability measure $\nu_N.$

We will denote the expected value of a random variable $X$ with respect to the Gaussian ensemble by ${\bf E}_{\gamma}(X)$ (resp. ${\bf E}_{\nu}(X)$ for the spherical ensemble).

These two ensembles are *equivalent* in the sense that the two large dimension limits give equivalent results when scaled properly. A more precise formulation goes as follows:

*[]{#spherical-vs-gaussian label="spherical-vs-gaussian"} Let $T_N: {\mathbb R}^{d_N} \to R^k$, $N=1,2,\dots$, be a sequence of linear maps, where $d_N
\to \infty$. Suppose that $\frac{1}{d_N}T_N T_N^*
\to
\Delta$. Then $T_{N*} \nu_{d_N} \to \gamma_{\Delta}$.*

## Sequences of random polynomials

We are often interested in sequences of polynomials $\{s_N\}$ chosen independently and at random from ${\mathcal H}_N$ from either a Gaussian or spherical ensemble. We thereform form the product probability space $({\mathcal H}_{\infty}, \mu_{\infty})$, defined by $${\mathcal H}_{\infty} = {\mathcal H}_1 \times {\mathcal H}_2 \times \cdots \times {\mathcal H}_N \times \cdots,\;\;\; \mu_{\infty} = \times_{N = 1}^{\infty} \mu_N, \;\; (\mu_N = \gamma_N\;
\mbox{or}\; \nu_N).$$ When we say that a sequence of polynomials $\{s_N\}$ of increasing degerees does something almost surely, we mean that the set of such sequences has measure one in this product ensemble.

## Szegö kernels

Our results depend on the fact that certain statistical properties of polynomials can be expressed in terms of the reproducing kernels $\Pi_N(x,y)$ (orthogonal projections) of the Hilbert spaces ${\mathcal H}_N$. They are known as Szego kernels, and are essentially the same as the 'coherent states' of the physics literature. The local structure of the Szegö kernel is given by the following scaling asymptotics:

::: theo
As $N \to \infty$, we have:

- [@BSZ2; @SZ2] Complex case: $$\Pi_N(z_0 + \frac{u}{\sqrt{N}}, \frac{\theta}{N}, z_0 + 
  \frac{v}{\sqrt{N}}, \frac{\varphi}{N})
  \sim \frac{1}{\pi^m} e^{i (\theta - \varphi)}
  e^{u \cdot \bar{v} -{\frac{1}{2}}(|u|^2 + |v|^2)} \{1 + \frac{1}{\sqrt{N}}
  p_{1}(u,v; z_0)
  + \cdots \}\,.$$ The leading order term is the Szegö kernel for the reduced Heisenberg group, whence the name 'Heisenberg class.'

- Real case: $$N^{-m + 1} \Pi_N(x_0 + \frac{u}{N},  x_0 + 
  \frac{v}{N})
  \sim \Gamma(\frac{m - 1}{2}) (\frac{|u - v|}{2})^{\frac{m - 2}{2}} J_{\frac{m - 2}{2}}(|u - v|) + \cdots \,,$$ where $J_{\nu}$ is the Bessel function of the first kind of order $\nu$ (whence the name 'Euclidean class'.)
:::

The proof of the scaling asymptotics in the complex holomorphic case [@BSZ2] is based on the Boutet-de-Monvel- Sjostrand parametrix for the Szegö kernel, which is valid for positive line bundles. A similar parametrix was constructed in the symplectic almost-complex case [@SZ2], and the scaling asymptotics were derived from it. In the real case of $S^m$, the scaling asymptotics are closely related to the 'Mehler-Heine formula'. The terms 'Heisenberg class' and 'Euclidean class' suggest infinite dimensional Gaussian ensembles related to representations of the Heisenberg and Euclidean motion groups.
