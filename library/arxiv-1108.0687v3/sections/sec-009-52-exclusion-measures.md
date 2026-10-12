---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures"
section_id: sec-009-52-exclusion-measures
section_title: "Exclusion measures"
section_number: 5.2
pages: 16-18
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
doc_brief: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures — Let {X1,...,X n} be a collection of binary valued random variables and let f : {0, 1}n → R be a Lipschitz"
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.987
---
[]{#ss:exclusion label="ss:exclusion"}

The symmetric group ${\cal S}_n$ acts on ${\mathcal B}_n$ by permuting the coordinates. Suppose a nonnegative rate $r(\tau)$ is given for each transposition $\tau \in {\cal S}_n$. Define a random evolution on ${\mathcal B}_n$ by letting each pair of coordinates $(i,j)$ transpose independently at rate $r(\tau_{ij})$. In other words, we have a continuous time chain on ${\mathcal B}_n$ which jumps from $x$ to $\tau (x)$ at rate $r(\tau)$ for each transposition $\tau$. This process is known as the symmetric exclusion process.

Borcea, Branden and Liggett [@borcea-branden-liggett Proposition 5.1] prove that the strong Rayleigh property is preserved under this evolution. In particular, because the point mass at a single state is always strong Rayleigh, it follows that the time $t$ distribution of a symmetric exclusion process started from a deterministic state is strong Rayleigh. The stochastic covering property follows, as do PHR and negative association. Interestingly, before the publication of [@borcea-branden-liggett], all that was known about this model was negative cylinder dependence [@liggett77 Lemma 2.3.4]).

Recently, it was shown by [@wagner-BAMS] that one can add birth and death to the exclusion dynamics and still preserve the strong Rayleigh property. More specifically, let $\{ \alpha_i ,
\beta_i : 1 \leq i \leq n \}$ be positive real numbers and let $\omega_i$ change to one at rate $\alpha_i$ and to zero at rate $\beta_i$, along with the exclusion dynamics. Then the evolution preserves the strong Rayleigh property and in particular, if the starting state is deterministic, all time $t$ marginals are strong Rayleigh.

::: cor
[]{#cor:exclusion label="cor:exclusion"} Let ${\mathbb P}$ be the law on ${\mathcal B}_n$ resulting from running an exclusion process for a fixed time, starting from a deterministic state with $k$ sites occupied. Then $${\mathbb P}(f - {\mathbb E}f \geq a) \leq e^{- a^2 / (8 k)} \, .$$
:::

::: example
[]{#eg:exclusion label="eg:exclusion"} Let $n > 0$ be even and populate a $n \times n$ square of the integer lattice in $\mathbb{Z}^2$ (with torus boundary conditions) by filling all sites in the left half and leaving empty all sites in the right half. Run the symmetric exclusion process for time $t$ with rate 1 on each edge. Let $f_t (\omega)$ denote the number of edges at time $t$ with exactly one endpoint occupied. The mean of $f_t$ starts at $n$ at time 0 and approaches its limiting value of $n^2 - O(1)$ as $t \to \infty$. Once $t = \Theta (n^2)$, the variance of $f_t$ becomes $\Theta (n^2)$ and the concentration inequality $${\mathbb P}(f - {\mathbb E}f \geq a) \leq e^{- a^2 / (4 n^2 )} \, ,$$ which holds for all $t$, becomes a meaningful Gaussian tail bound (here $k = n^2 / 2$).
:::

## Determinantal measures on a finite Boolean lattice {#ss:finite}

We say that a probability measure ${\mathbb P}$ on ${\mathcal B}_n$ is **determinantal** (in the general sense) if there is an $n \times n$ real or complex matrix $K$ such that that for every $S \subseteq \{ 1 , \ldots , n \}$, $$\label{eq:det}
{\mathbb E}\prod_{j \in S} X_j = \det K_S$$ where $K_S$ is the submatrix of $K$ obtained by choosing only those rows and columns whose index is in $S$. In this definition, the phrase "general sense" refers to the lack of further assumptions on $K$. An important subclass is the **Hermitian** determinantal measures, for which the matrix $K$ is Hermitian. In this paper we will be interested only in the Hermitian case and will use the term **determinantal** hereafter to refer only to the case where $K$ is Hermitian. Determinantal measures are known to be negatively associated [@lyons03 Theorem 6.5]. In fact they are strong Rayleigh [@borcea-branden-liggett proof of Theorem 3.4] and therefore satisfy the stochastic covering property.

::: example
[]{#eg:spanning tree 2 label="eg:spanning tree 2"} As previously remarked, the uniform or weighted random spanning tree is a determinantal measure.
:::

In the next section we will extend the notion of a determinantal measure to the continuous setting. The extension to a countably infinite set of variables is more straightforward: the kernel $K$ is now indexed by a countably infinite set, but [\[eq:det\]](#eq:det){reference-type="eqref" reference="eq:det"} may be interpreted as holding for all finite sets $S$. The following example of a determinantal process on $\mathbb{Z}$ appeared first in [@johansson03].

::: example
[]{#eg:nonintersecting RW label="eg:nonintersecting RW"} Let $\{ Y^{(k)} : 1 \leq k \leq n \}$ be $n$ independent time homogeneous nearest neighbor random walks on $\mathbb{Z}$. Begin the walks at locations $y_1 , \ldots , y_n$ and suppose the event that the walks are all at their starting positions at time $2n$ and have not intersected has positive probability. Conditional on this event, the positions at time $n$ form a determinantal measure. That is, the indicator functions $\{ X_j \}$ have a determinantal law, where $X_j = 1$ if some $Y^{(k)}$ is at position $j$ at time $n$, and zero otherwise.
:::

::: unremark
The positions of non-colliding random walks are given by a determinant under more general conditions (see [@karlin-mcgregor]). The present situation is arranged so as to make the kernel Hermitian.
:::
