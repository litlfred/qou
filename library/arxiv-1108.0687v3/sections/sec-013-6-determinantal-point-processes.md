---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures"
section_id: sec-013-6-determinantal-point-processes
section_title: "Determinantal point processes"
section_number: 6
pages: 18-23
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.685
doc_brief: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures — Let {X1, . . ."
---
[]{#s:continuous label="s:continuous"}

We consider here only simple point processes and often assume ${\mathbb E}N < \infty$ as well. If $\rho_k : (\mathbb{R}^d)^k \to \mathbb{R}^+$ are measurable functions, then the simple point process ${\cal Z}$ is said to have joint intensities $\{ \rho_k \}$ if for any $k$ and any family $D_1 , \ldots , D_k$ of disjoint Borel subsets of $\mathbb{R}^d$, $${\mathbb E}\left [ \prod_{j=1}^k {\cal Z}(D_j) \right ] = \int_{\prod_j D_j}
   \rho_k (x_1 , \ldots , x_k) \, dx_1 \cdots dx_k \, .$$ In particular, $${\mathbb E}N = \int_{\mathbb{R}^d} \rho_1 (x) \, dx$$ so under the assumption ${\mathbb E}N < \infty$, we see that $\rho_1 (x) \, dx$ is a finite measure on $\mathbb{R}^d$. If $\rho_1$ is not finite, we will assume it is $\sigma$-finite. In any case, $\rho_1$ is called the **first intensity measure**; see [@HKPV Sections 1.2 and 4.2] for further discussion of joint intensities and determinantal measures.

::: defn
A point process ${\cal Z}$ is said to be determinantal if it has joint intensities $\{ \rho_k \}$ and there is a measurable kernel $K : (\mathbb{R}^d)^2 \to {\cal C}$ such that $$\label{eq:kernel}
\rho_k (x_1 , \ldots , x_k)
   = \det \left ( K(x_i , x_j) \right )_{1 \leq i,j \leq k} \, .$$ If $K(y,x) = \overline{K(x,y)}$ for every $x,y$, then the process is said to be Hermitian. When discussing determinantal processes below, we will always assume they are Hermitian.
:::

Stochastic covering carries over to the continuous case. To state the relevant results we invoke the notion of the **Palm process**. This is a version of the process conditioned on the (measure zero) event of a point at a specified location, $x$. It may be obtained by conditioning on there being a point within distance $\epsilon$ of a given location $x$, then taking a weak limit. A more complete treatment may be found in [@kallenberg]. The following proposition is proved in [@goldman10].

::: pr
[]{#pr:cover cont label="pr:cover cont"} Suppose ${\cal Z}$ is a determinantal point process with continuous kernel $K$ and finite trace. Fix $x$ and let ${\cal Z}_x$ denote the Palm process that conditions on a point at $x$. Let ${\cal Z}_x'$ denote the result of removing the point at $x$ from ${\cal Z}_x$. Then

1.  Whenever $K-L$ is positive semi-definite, the process with kernel $K$ stochastically dominates the process with kernel $L$ (this is [@goldman10 Theorem 3]).

2.  ${\cal Z}_x'$ is determinantal with kernel $L$ such that $K-L$ is positive semi-definite.

3.  Consequently, ${\cal Z}\succeq {\cal Z}_x'$.

  \
:::

The continuous analogue of Proposition [\[pr:k cover\]](#pr:k cover){reference-type="ref" reference="pr:k cover"} is

::: pr
[]{#eq:pr k cont label="eq:pr k cont"} Let ${\cal Z}$ be a determinantal point process with finite mean ${\mathbb E}N = \mu< \infty$. Then for any $k$ for which ${\mathbb P}(N = k+1)$ and ${\mathbb P}(N = k)$ are both nonzero, the conditional distributions of ${\cal Z}$ given $N$ satisfy $$( {\cal Z}{\, | \, } N = k+1) \triangleright({\cal Z}{\, | \, } N = k) \, .$$
:::

The following facts may be found in [@HKPV-PS Theorem 7]. A determinantal point process ${\cal Z}$ with mean $\mu< \infty$ has a kernel $K$ whose spectrum is countable, contained in $[0,1]$, and sums to $\mu$. Furthermore, ${\cal Z}$ may be represented as a mixture of homogeneous determinantal processes as follows. Let $\{ \lambda_i : i \geq 1 \}$ enumerate the eigenvalues with multiplicities and let $\{ \phi_i \}$ be a corresponding eigenbasis. For each $i$, flip an independent coin with success probability $\lambda_i$. Let $I$ denote the set of $i$ for which the coin-flip was successful. Let $K_I$ be the (random) projection operator onto the subspace spanned by the eigenvectors $\phi_i$ for which the coin-flip was successful. Then $K_I$ is almost surely a projection of finite dimension $|I|$ and is the kernel of a $|I|$-homogeneous determinantal point process. Choosing $K_I$ at random and then sampling from the corresponding process recovers the law of ${\cal Z}$.

Several consequences are apparent. First, conditioning on $N = k$ is the same as conditioning on exactly $k$ successes among the Bernoulli trials. Secondly, the conditional law of $I$ given $|I| = k+1$ stochastically dominates the conditional law of $I$ given $|I| = k$. When the number of Bernoullis is finite, this follows from the strong Rayleigh property for independent Bernoullis; an easy limit argument extends the conclusion to the infinite case. This fact about stochastic domination is equivalent to saying that the conditional law of the random subspace $K_I$ given $|I| = k+1$ stochastically dominates the conditional law of the random subspace $K_I$ given $|I| = k$, in the sense that the two laws can be coupled as $(K , K')$ so that $K' \subseteq K$. When $K' \subseteq K$, the operator $\pi_{K} - \pi_{K'}$ is positive semi-definite. By $(ii)$ of Proposition [\[pr:cover cont\]](#pr:cover cont){reference-type="ref" reference="pr:cover cont"}, we conclude that $({\cal Z}{\, | \, } N = k+1) \succeq ({\cal Z}{\, | \, } N = k)$ which is equivalent to stochastic covering in this case. $\hfill \Box$

With $f$ as in the statement of the theorem, and $I$ the collection of indices described in the previous proposition, define $\psi(I)$ to be the expectation of $f$ applied to a configuration chosen from the determinantal process with kernel $K_I$. Recall the notation $N=|I|$.

The event $\{ f - {\mathbb E}f > a \}$ is contained in the union of three events: $$\left \{ N > \mu+ \frac{a}{2} \right \} \cup
   \left \{ \psi(I) - {\mathbb E}f > \frac{a}{2} \right \} \cup
   \left \{ f - \psi(I) > \frac{a}{2} \, , \, N \leq \mu+
      \frac{a}{2} \right \}  \, .$$ Thus ${\mathbb P}(f - {\mathbb E}f > a)$ is bounded above by the sum of the corresponding probabilities. Each of the first two pieces is bounded above by $\exp [- a^2 / (4(a + 2\mu))]$: the first follows from Lemma [\[lem:N concentration\]](#lem:N concentration){reference-type="ref" reference="lem:N concentration"} and the second follows from the proof of Lemma [\[lem:phi concentration\]](#lem:phi concentration){reference-type="ref" reference="lem:phi concentration"} because $\psi$ is Lipschitz in the Bernoulli variables $Y_i:={\bf 1}_{i\in I}$. The last piece is bounded above by $\exp [- a^2 / (16 (a + 2\mu))]$. To see this, apply Theorem [\[th:cont homog\]](#th:cont homog){reference-type="ref" reference="th:cont homog"} to the homogenous determinantal processes ${\mathbb P}_I$ with kernels $K_I$, obtaining, when $|I|=k$, that $${\mathbb P}_I \left ( f - \psi(I) > \frac{a}{2} \right )
   \leq \exp \left ( - \frac{(a/2)^2}{8 k} \right )
   \leq \exp \left ( - \frac{a^2}{16 (a + 2 \mu)} \right ) \, .$$ Reassembling these gives the upper bound $${\mathbb P}\left ( f - \psi(I) > \frac{a}{2} \, , \, N \leq \mu+
   \frac{a}{2} \right )
   \leq \exp \left ( -\frac{a^2}{16 (a + 2 \mu)} \right ) \, .$$ The rest of the argument is identical to the conclusion of the proof of Theorem [\[th:general\]](#th:general){reference-type="ref" reference="th:general"}. $\hfill \Box$

::: example
[]{#eg:ginibre label="eg:ginibre"} Ginibre [@ginibre65] considers the distribution of eigenvalues of an $k \times k$ matrix with independent complex Gaussian entries. In the limit as $k \to \infty$, the density becomes constant over the whole plane. The limiting process ${\cal Z}$ turns out to be a (Hermitian) determinantal point process with kernel $$K(z_1 , z_2) := \frac{1}{\pi} e^{z_1 \overline{z_2}}
   \, \exp \left ( - \frac{|z_1|^2 + |z_2|^2}{2} \right ) \, ;$$ see, e.g. [@soshnikov00 (2.16)]. The process ${\cal Z}$ is ergodic and invariant under all rigid transformations of the plane. It was suggested [@lecaer-ho90] to use this process as the set of centers for a random Voronoi tesselation because the mutual repulsion of the points makes the resulting tesselation more realistic than the standard Poisson-Voronoi tesselation for many purposes. Some rigorous results along these lines were obtained in [@goldman10].

The mean number of points in any region $D$ is $1/\pi$ times the area $|D|$, so the restriction of ${\cal Z}_D$ to such a region of finite area is a determinantal process with finite mean number of points. Fix a finite region, $D$, and let $f$ count the number of "lonely" points in $D$, these being such that no other point of ${\cal Z}$ in $D$ is within distance 1. We claim that $f$ is Lipschitz with constant equal to 6. Clearly if a point $z$ is added to the configuration $\eta$ then $f$ can increase by at most 1. It is well known that the maximum number of points in a unit disk that can be at mutual distance of at least 1 from one another is 6, which implies that the addition of $z$ can result in the loss of at most 6 lonely points. Applying Theorem [\[th:continuous\]](#th:continuous){reference-type="ref" reference="th:continuous"} to $f/6$ yields the concentration inequality $${\mathbb P}(|f - {\mathbb E}f| \geq a) \leq 5 \exp \left (
   - \frac{a^2}{96 (a + 12 |D| / \pi )} \right ) \, .$$
:::

::: example
[]{#eg:zeros label="eg:zeros"} Let $\{ X_n \}$ be IID standard complex Gaussian random variables and define the random power series $$h(z) := \sum_{n=0}^\infty X_n z^n \, .$$ It is easy to see that $h$ is almost surely analytic on the open unit disk and the number of zeros on any disk of radius $\rho < 1$ has finite mean. The remarkable properties of the point process ${\cal Z}$ on the unit disk that is the zero set of $h$ are detailed in [@peres-virag]. It is a determinantal process whose kernel is the Bergman kernel $\pi^{-1} (1 - z \overline{w})^{-2}$. It is invariant under Möbius transformations of the unit disk and has intensity measure $\pi^{-1} / (1 - |z|^2)^2$. Endowing the unit disk with the hyperbolic metric, the Möbius transformations become isometries, whence ${\cal Z}$ is hyperbolic isometry invariant.

Fix $\rho < 1$ and $r > 0$ and let $f$ count the number of zeros of the restriction ${\cal Z}_\rho$ of ${\cal Z}$ to the disk of radius $1-\rho$ that are "hyperbolically lonely", meaning that no other point of ${\cal Z}_\rho$ is within a hyperbolic distance $r$. Let $c_r$ denote the maximum number of points at mutual hyperbolic distance $r$ that may be be placed in a disk of hyperbolic radius $r$. Arguing as in Example [\[eg:ginibre\]](#eg:ginibre){reference-type="ref" reference="eg:ginibre"} we see that $f$ is Lipschitz with constant $c_r$. The mean number of points in ${\cal Z}_\rho$ is $\rho^2 / (1 - \rho^2)$ which for simplicity we can bound from above by $1/(1-\rho^2)$. An application of Theorem [\[th:continuous\]](#th:continuous){reference-type="ref" reference="th:continuous"} to $f / c_r$ now yields $${\mathbb P}(|f - {\mathbb E}f| \geq a) \leq 5 \exp \left (
   - \frac{a^2}{16 c_r a + 32 c_r^2 (1 - \rho^2)^{-1} } \right ) \, .$$
:::

# Acknowledgments

We thank Subhroshekhar Ghosh and an anonymous referee for detailed comments leading to the correction and improvement of the exposition and results.
