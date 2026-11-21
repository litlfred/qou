---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-012-23-discrete-orthogonal-polynomial-ensembles-and
section_title: "Discrete orthogonal polynomial ensembles and determinantal point processes"
section_number: 2.3
pages: 8-10
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.985
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
---
Let $E$ be an infinite countable discrete subset of $\mathbb{R}$. We first recall the definition of an orthogonal polynomial ensemble in our setting. Let $\omega$ be a discrete weight as in the previous subsection. We assume that its support lies inside $E$, and in all the sequel, we may identify a measure on $E$ with its density with respect to the counting measure on $E$. Let $N$ be a positive integer.

::: defi
An $N$-orthogonal polynomial ensemble is a probability measure $\mathbb{P}_N$ on $E^N$ given by the following formula: $$\label{orthpolenseq}
d\mathbb{P}_N(x_1,...x_N)= C_N \prod_{1 \leq i < j \leq N} (x_i-x_j)^2 \prod_{i=1}^Nd\omega(x_i)$$ where $C_N$ is the normalization constant: $$\begin{aligned}
C_N^{-1} = \sum_{x_1, ..., x_N \in E} \prod_{1 \leq i < j \leq N} (x_i-x_j)^2 \prod_{i=1}^N\omega(x_i) 
\end{aligned}$$
:::

We now recall the definition of a determinantal point process on $E$. We denote by $\text{Conf}(E)$ the space of configuration in $E$ which is in this context simply the set of all subsets of $E$, $$\begin{aligned}
\text{Conf}(E) := 2^E.
\end{aligned}$$

::: defi
[]{#defdpp label="defdpp"}A *point process* is a probability measure $\mathbb{P}$ on $\text{Conf}(E)$. It is said to be *determinantal* if there exists a function $$\begin{aligned}
K : E \times E \rightarrow \mathbb{R}
\end{aligned}$$such that for any $n \in \mathbb{N}$ and any $\{a_1,...,a_n \} \subset E$, one has $$\begin{aligned}
\mathbb{P}( X \in \text{Conf}(E), \hspace{0.1cm}  \{a_1,...,a_n \} \subset X) = \det \left(K(a_i,a_j)\right)_{i,j=1}^n.
\end{aligned}$$ The function $K$ is called the *correlation kernel* of the determinantal point process.
:::

::: rem
The correlation kernel of a given determinantal point process is not unique. Indeed, if one has a determinantal point process with kernel $K$, for any non-vanishing function $f:E \rightarrow \mathbb{R}$ the function $$\begin{aligned}
\tilde{K}(x,y)=\frac{f(x)}{f(y)}K(x,y)
\end{aligned}$$ can also serve as a kernel for the same determinantal point process.
:::

As a matter of fact, any orthogonal polynomial ensemble gives rise to a determinantal point process, what we resume in the following Proposition (see e.g. [@konig] and references therein). Note that since the measure ([\[orthpolenseq\]](#orthpolenseq){reference-type="ref" reference="orthpolenseq"}) is symmetric and does not charge $N$-tuples which contain two equal coordinates, it can and it will be identified with a measure on the space of configurations.

::: prop
[]{#proporthpolens label="proporthpolens"} An orthogonal polynomial ensemble given by ([\[orthpolenseq\]](#orthpolenseq){reference-type="ref" reference="orthpolenseq"}) is a determinantal point process on $E$. Its correlation kernel is given by the formula $$\begin{aligned}
K_N(x,y)&=\sqrt{\omega(x)\omega(y)}\sum_{n=0}^{N-1}\frac{p_n(x)p_n(y)}{h_n}\\
&= \begin{cases}\sqrt{\omega(x)\omega(y)}\frac{c_{N-1}}{h_{N-1} c_{N}}\frac{p_N(x)p_{N-1}(y)-p_N(y)p_{N-1}(x)}{x-y}, \quad \text{for $x \neq y$}, \\
\omega(x)\frac{c_{N-1}}{h_{N-1} c_{N}}\left(p_{N}'(x)p_{N-1}(x)-p_N(x)p_{N-1}'(x)\right), \quad \text{for $x=y$}. \end{cases}
\end{aligned}$$
:::

The second equality is just the Christoffel-Darboux formula, while the last one follows from L'Hospital rule.

::: rem
Observe that $K_N$ is the kernel of the orthogonal projection from $l^2(E)$ (where $E$ is equipped with the counting measure) onto $$\begin{aligned}
\sqrt{\omega}\mathbb{R}_{N-1}[x] = \{x \mapsto\sqrt{\omega(x)}p(x),\hspace{0.1cm} p \text{ is a polynomial of degree at most $N-1$}\}.
\end{aligned}$$
:::

The main object of our study is given by the following definition.

::: defi
[]{#maindef label="maindef"} Let $k \in \mathbb{N}$ be a non-negative integer. Given an orthogonal polynomial ensemble $\mathbb{P}_N$ with weight $\omega$, its *Christoffel deformation* of order $k$, denoted by $\mathbb{P}_N^{k}$, is the orthogonal polynomial ensemble with weight $\omega^k$.
:::

The next Proposition gives a compact formula for the kernel of the Christoffel deformation which will be suitable for asymptotic analysis.

::: prop
[]{#propkernelcharlier label="propkernelcharlier"}The Christoffel deformation of order $k$, $\mathbb{P}_N^k$, is a determinantal point process with kernel $K_N^k$ given by: $$\begin{aligned}
K^{k}_N(x,y) =\frac{\sqrt{\omega(x)\omega(y)}}{\prod_{i=1}^k|(x-u_i)(y-u_i)|} \frac{c_{N-1}}{h_{N-1}c_{N+2k}}\frac{D_N^k(x)D_{N-1}^k(y)-D_N^k(y)D_{N-1}^k(x)}{(\delta_N^k)^2(x-y)}.
\end{aligned}$$
:::

::: proof
*Proof.* This is a straightforward computation, using Propositions [\[proporthpolens\]](#proporthpolens){reference-type="ref" reference="proporthpolens"} and [\[propchristoffel\]](#propchristoffel){reference-type="ref" reference="propchristoffel"}. Indeed, Proposition [\[proporthpolens\]](#proporthpolens){reference-type="ref" reference="proporthpolens"} states that $\mathbb{P}_N^k$ is a determinantal point process with kernel $$\begin{aligned}
K_N^k(x,y)=\sqrt{\omega^k(x)\omega^k(y)}\frac{p_N^k(x)p_{N-1}^k(y)-p_N^k(y)p_{N-1}^k(x)}{h_{N-1}^k(x-y)}.
\end{aligned}$$ By the definition of the measure $\omega^k$ and using Proposition [\[propchristoffel\]](#propchristoffel){reference-type="ref" reference="propchristoffel"} and the explicit expression of the polynomials $p_n^k$, this kernel can be written as $$\begin{gathered}
K_N^k(x,y)\\
=\frac{\sqrt{\omega(x)\omega(y)}}{\prod_{i=1}^k|(x-u_i)(y-u_i)|}\frac{1}{\delta_N^k\delta_{N-1}^k c_{N+2k}c_{N+2k-1}h_{N-1}^k}\frac{D_N^k(x)D_{N-1}^k(y)-D_N^k(y)D_{N-1}^k(x)}{x-y}.
\end{gathered}$$ The expression for the squared norm $h_{N-1}^k$ given in Proposition [\[propchristoffel\]](#propchristoffel){reference-type="ref" reference="propchristoffel"} leads to the desired result. ◻
:::
