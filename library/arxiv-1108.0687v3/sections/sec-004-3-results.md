---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures"
section_id: sec-004-3-results
section_title: "Results"
section_number: 3
pages: 6-9
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 1.0
doc_brief: "Concentration of Lipschitz functionals of determinantal and other strong Rayleigh measures — Let {X1, . . ."
---
[]{#sec:results label="sec:results"}

The chief consequence of the strong Rayleigh property that we use to prove concentration inequalities is the stochastic covering property. Although all of our examples so far of measures with the SCP are in fact strong Rayleigh, we note that this may not be the case in the future, and with this in mind, we state a result that uses only the SCP.

::: thm
[]{#th:main label="th:main"} Let ${\mathbb P}$ be a $k$-homogeneous probability measure on ${\mathcal B}_n$ satisfying the SCP. Let $f$ be a Lipschitz-1 function on ${\mathcal B}_n$. Then $${\mathbb P}(f - {\mathbb E}f \geq a) \leq \exp \left ( - \frac{a^2}{8k} \right
   ) \, .$$
:::

::: unremarks
$(i)$ Replacing $f$ with $-f$ gives immediate two-sided bounds: $$\label{eq:two sided}
{\mathbb P}(|f - {\mathbb E}f| > a) \leq 2 \exp \left ( \frac{-a^2}{8 k} \right )  \, .$$ $(ii)$ Replacing every $X_i$ by $1 - X_i$ if necessary, we may assume without loss of generality that $k \leq n/2$, whence $$\label{eq:k to n}
{\mathbb P}(f - {\mathbb E}f > a) \leq \exp \left ( \frac{-a^2}{4 n} \right ) \, .$$
:::

For strong Rayleigh measures that are not necessarily homogeneous, we have the following result.

::: thm
[]{#th:general label="th:general"} Let ${\mathbb P}$ be strong Rayleigh with mean $\mu= {\mathbb E}N$. Let $f : {\mathcal B}_n \to \mathbb{R}$ be Lipschitz-1. Then $$\begin{aligned}
{\mathbb P}(f - {\mathbb E}f > a) & \leq &
   3 \exp \left ( - \frac{a^2}{16 (a + 2 \mu)} \right ) \, ;  \\[1ex]
{\mathbb P}(|f - {\mathbb E}f| > a) & \leq &
   5 \exp \left ( - \frac{a^2}{16 (a + 2 \mu)} \right ) \, .
\end{aligned}$$
:::

::: unremark
Because $a, \mu\leq n$, the denominator in these inequalities may be replaced by $48 n$.
:::

## Continuous versions

Continuous versions of these results may be stated in terms of point processes, which we now briefly review. Formally, a point process on a space $S$ is a random counting measure on $S$. In other words, a point process is a map ${\cal Z}$ defined on a probability space $(\Omega , {\mathcal F}, {\mathbb P})$ taking values in the space of counting measures on $S$, a counting measure being one that takes only integer values or $+\infty$. Intuitively, one envisions the sample counting measure ${\cal Z}(\omega)$ as a set of points such that the sum of delta functions at these points is the sample counting measure.

If the number $k$ of points in the support of ${\cal Z}$ is deterministic, we may dispense with much of the formalism by ordering the points in the support of ${\cal Z}$ uniformly at random and identifying the process ${\cal Z}$ with the resulting exchangeable probability law on sequences of length $k$ in $S$. Notationally, if ${\cal Z}$ is a $k$-homogeneous point process on $\mathbb{R}^d$ with law ${\mathbb P}$, we denote by ${\mathbb P}_{\uparrow}$ the corresponding exchangeable law on $(\mathbb{R}^d)^k$. For $1 \leq j \leq k$, we use $X_j$ to denote the "$j^{th}$ random point", that is, the $j^{th}$ coordinate function on $(\mathbb{R}^d)^k$. The following sampling algorithm for any $k$-homogeneous point process is almost trivial once one identifies ${\cal Z}$ with ${\mathbb P}_{\uparrow}$, and yet it is a generalization of an algorithm previously proved only in the case of determinantal point process in [@HKPV Proposition 4.4.3].

::: lem
[]{#lem:k step label="lem:k step"} Let ${\cal Z}$ be a $k$-homogeneous point process on a standard Borel space $S$ and let ${\mathbb P}_{\uparrow}$ be the corresponding exchangeable measure on $S^k$. Then for $0 \leq j < k$ there are regular conditional distributions $Q_{x_1 , \ldots , x_j}$ for the law of $X_{j+1}$ given $X_1 = x_1 , \ldots , X_j = x_j$ such that the following procedure samples from ${\mathbb P}_{\uparrow}$.

> Sample $X_1$ from $Q_\emptyset$.
>
> Recursively, conditional on $X_1 = x_1 , \ldots , X_j = x_j$, sample $X_{j+1}$ from $Q_{x_1 , \ldots , x_j}$.

In the case where $S$ is finite, let $R$ denote the random set $\{ X_1 , \ldots , X_n \}$. Then the law $Q_{x_1 ,
\ldots , x_j}$ is equal to $1 / (k-j)$ times the conditional intensity measure of $R \setminus \{ x_1 , \ldots , x_j \}$ given $x_1 , \ldots , x_j \in R$.
:::

Any standard Borel space admits regular conditional distributions [@durrett Theorem 4.1.6]. The sampling algorithm essentially restates the definition of regular conditional probabilities for sequential sampling. Because ${\mathbb P}_{\uparrow}$ is exchangeable, conditioning on $X_{i_1} = x_1 ,
\ldots , X_{i_j} = x_j$ gives the same exchangeable measure on the sequence of remaining elements of $R$ for any $i_1 , \ldots , i_j$. Thus for any $x$ other than $x_1 , \ldots , x_j$, we have $${\mathbb P}(x \in R {\, | \, } x_1 \in R , \ldots , x_j \in R) =
   (k-j) {\mathbb P}(X_{j+1} = x {\, | \, } X_1 = x_1 , \ldots , X_j = x_j)$$ which is the final conclusion. $\hfill \Box$

::: unremark
In the case of a measures on a finite set of size $n$, the main point of this sampling scheme is to sample in $k$ steps rather than $n$ steps, so as better to control the Azuma martingale. But also, sequential conditioning on $x \in R$ can be easy to compute. For example, conditioning on an edge being in a spanning tree replaces the original graph by a contraction along that edge.
:::

Intuitively, there is a stochastic covering property for point processes defined to hold when conditioning on the presence of a point depresses the process everywhere else but by at most one point. To make this definition precise begin by extending the notion of one measure stochastically covering another to point processes. We say the point process ${\cal Z}$ stochastically covers the point process ${\cal W}$ if there is a coupling of these two laws on counting measures supported on pairs $(\mu , \nu)$ such that $\mu = \nu$ or $\mu = \nu + \delta_x$ for some $x$. Metrizing the space of finite counting measures on $S$ by the total variation distance, we see as before that if ${\cal Z}\triangleright{\cal W}$ then $d_\infty ({\cal L}({\cal Z}) , {\cal L}({\cal W})) \leq 1$.

Next, given a $k$-homogeneous point process ${\cal Z}$ on a space $S$, we let ${\cal Z}_{x_1 , \ldots , x_j}$ denote the $(k-j)$-homogeneous point process whose law is the law of $\{ X_{j+1} , \ldots , X_k \}$ when sampling according to the procedure in Lemma [\[lem:k step\]](#lem:k step){reference-type="ref" reference="lem:k step"} conditional on $X_1 = x_1 , \ldots , X_j = x_j$. The $k$-homogeneous point process ${\cal Z}$ is said to have the **stochastic covering property** if $${\cal Z}_{x_1 , \ldots , x_j} \triangleright{\cal Z}_{x_1 , \ldots , x_{j+1}}$$ for all choices of $x_1 , \ldots , x_{j+1}$. Note that the left-hand side is $(k-j)$-homogeneous while the right-hand side is $(k-j-1)$-homogeneous.

::: thm
[]{#th:cont homog label="th:cont homog"} Let ${\cal Z}$ be a $k$-homogeneous point process on a standard Borel space $S$ and let $f$ be a Lipschitz-1 function (with respect to the total variation distance) on counting measures with total mass $k$ on $\mathbb{R}^d$. If ${\cal Z}$ has the SCP, then $${\mathbb P}(f - {\mathbb E}f \geq a)
   \leq \exp \left ( - \frac{a^2}{8k} \right ) \, .$$
:::

For point processes that are not homogeneous, as in the discrete case, we require more than the SCP. Rather than defining a notion of strong Rayleigh here, we will stick to the case of determinantal point processes, this being where all of our examples arise; see Section [\[s:continuous\]](#s:continuous){reference-type="ref" reference="s:continuous"} for definitions.

::: thm
[]{#th:continuous label="th:continuous"} Let ${\cal Z}$ be a determinantal point process with ${\mathbb E}N = \mu< \infty$. Let $f$ be a Lipschitz-1 function on finite counting measures. Then $$\begin{aligned}
{\mathbb P}(f - {\mathbb E}f \geq a )
   & \leq & 3 \exp \left ( - \frac{a^2}{16 (a + 2\mu)} \right )
   \, ; \\[1ex]
{\mathbb P}(|f - {\mathbb E}f \geq a )
   & \leq & 5 \exp \left ( - \frac{a^2}{16 (a + 2\mu)} \right ) \, .
\end{aligned}$$
:::
