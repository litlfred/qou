---
doc_id: arxiv-2404.03933v2
doc_title: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2)"
section_id: sec-009-10-the-asymptotic-of-probability-measures-for-uq
section_title: "The asymptotic of probability measures for uq(sl2)"
section_number: 10
pages: 28-30
source_pdf: 2404.03933v2.pdf
source_sha256: 48aff6e97e1f1267
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.926
doc_brief: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) — We study the decomposition of tensor powers of two dimensional irreducible rep- resentations of quantum sl2 at even roots of unity into direct sums"
---
[]{#as10 label="as10"}

## Corresponding Markov processes

### Probabilistic measures induced by Markov processes

Let $X$ be a countable set. A *local Markov process* on $X$ is a collection of transition probabilities $\{\mathrm{Prob}(x\to y)\}_{x,y\in X}$, i.e. $0\leq \mathrm{Prob}(x\to y)\leq 1$, such that

-   for each $x$ there are only finitely many $y$ such that $\mathrm{Prob}(x\to y)\neq 0$,

-   $\sum\limits_y \mathrm{Prob}(x\to y)=1$, i.e. $x$ with probability $1$ will transition to some $y$.

Let $\{p(x)\}$ be a probability measure on $X$, i.e. for each $x\in X$, $0\leq p(x) \leq 1$ and $\sum\limits_x p(x)=1$. We will say it is *local*, if $p(x)\neq 0$ only for finitely many $x\in X$.

One of the fundamental properties of Markov processes is that function $$p_N(x)=(\mathrm{Prob}^Np)(x)=\sum_{x_1,x_2,\dots, x_N}p(x_1)\mathrm{Prob}(x_1\to x_2)\dots \mathrm{Prob}(x_N\to x)$$ is a probability measure on $X$ for each $N\in\mathbb{Z}_{>0}$, $N\geq 2$. For each such $N$ it is local if $p(x)$ is local and the Markov process is local. In particular, if $p(x)=\delta_{x,x_0}$ by applying repeatedly a local Markov process to such distribution we have a sequence of probability distributions on $X$: $$p_{x_0}(x)=\sum_{x_1,x_2,\dots, x_{N-1}}\mathrm{Prob}(x_0\to x_1)\dots \mathrm{Prob}(x_{N-1}\to x)$$ It turned out that character and Plancherel measures introduced earlier are exactly of this nature.

### Character and Plancherel measures for $U_q(\mathfrak{sl}_2)$

Consider the Markov process on $\mathbb{Z}_{\geq 0}$ with transition probabilities determined by tensor product decomposition ([\[A\]](#A){reference-type="ref" reference="A"}): $$\mathrm{Prob}(n\to m)=\frac{\mathrm{ch}_{T(m)}(x)\dim\mathrm{Hom}(T(n)\otimes T(1),T(m))}{\mathrm{ch}_{T(n)}(x)\mathrm{ch}_{T(1)}(x)}$$ Here $x=e^t>0$ which ensures positivity of transition probabilities. The Markov property $\sum_m \mathrm{Prob}(n\to m)=1$ is guaranteed by the decomposition rule of the tensor product. The character measure on the set of tilting components of $T(1)^{\otimes N}$ can be regarded as a probability distribution on $\mathbb{Z}_{\geq 0}$ induced by this Markov process.

The probability $p^{(l)}_N(k;t)$ is the result of iteration of this random process starting from the distribution supported at $k=0$, i.e. from $p^{(l)}_0(k;t)=\delta_{k,0}$: $$p^{(l)}_N(k;t)=\sum_{\gamma} \mathrm{Prob}(0\to 1)\mathrm{Prob}(1\to k_2)\dots \mathrm{Prob}(k_{N-1}\to k)$$ Here the sum is taken over all lattice paths described in Section [\[lpm\]](#lpm){reference-type="ref" reference="lpm"}. A path $\gamma$ starts at the origin, follows the rules of elementary steps and ends at $k$ after $N+1$ steps $(k_i,k_{i+1})$.

Specializing the character measure to $t=0$ we obtain the Markov process interpretation of the Plancherel measure for $U_q(\mathfrak{sl}_2)$. The results on the asymptotic of probability measures for $U_q(sl_2)$ can also be obtained by analyzing this Markov process. It will be done in a separate publication.

### Plancherel and quantum Plancherel measures for $u_q(\mathfrak{sl}_2)$

The decomposition rules [\[B\]](#B){reference-type="ref" reference="B"} define two natural Markov processes on $\{0,1,\ldots,3l-2\}$: $$\label{probmatrix}
\mathrm{Prob}(n\to m)=\frac{d_m \dim\mathrm{Hom}(T(n)\otimes T(1),T(m))}{d_n d_1}.$$ Here $T(n)$ are representations $T(n)$ of $u_q(\mathfrak{sl}_2)$ as described in Section [\[secplanch\]](#secplanch){reference-type="ref" reference="secplanch"}. For Plancherel and quantum Plancherel $d_n$ are dimensions $\dim T(n)$ and quantum dimensions $\mathrm{dim}_q T(n)$ of representation $T(n)$ correspondingly, see Sections [\[secplanch\]](#secplanch){reference-type="ref" reference="secplanch"} and [\[qdims\]](#qdims){reference-type="ref" reference="qdims"}.

## The asymptotic of Plancherel and quantum Plancherel measures on $u_q(\mathfrak{sl}_2)$-modules {#markovuq}

The asymptotic of these measures can be computed directly from the analysis of multiplicities. But it is much easier to use Markov processes in this case.

### Plancherel measure

For the small quantum group the Markov matrix ([\[probmatrix\]](#probmatrix){reference-type="ref" reference="probmatrix"}) is a real $3l-1\times 3l-1$ matrix with non-negative matrix elements: $$\mathrm{Prob}(k\to k+1)=\begin{cases}
\frac{k+2}{2(k+1)},&\textit{if $0\leq k \leq l-2$}\\
1,&\textit{if $k=l-1$, $2l-1$}\\
0,&\textit{if $k=3l-2$}\\
\frac{1}{2},&\textit{if else}
\end{cases}$$ $$\mathrm{Prob}(k\to k-1)=\begin{cases}
\frac{k}{2(k+1)},&\textit{if $0\leq k \leq l-2$}\\
0,&\textit{if $k=l-1, 2l-1$}\\
\frac{1}{2},&\textit{if else}
\end{cases}$$ $$\mathrm{Prob}(3l-2\to l-1)=\frac{1}{2}.$$

It is not difficult to check explicitly that its largest eigenvalue $\lambda_{\text{max}}=1$ and that it has multiplicity $1$. Thus the stationary distribution in this case is given by components of the eigenvector corresponding to the largest eigenvalue of the Markov matrix. Straightforward computation shows that it is given by $$(p_0,\ldots, p_{3l-2}),$$ where $$p_j=\begin{cases}
0,&\textit{if $k\leq l-2$}\\
\frac{2l-1-k}{l^2},&\textit{if $l\leq k\leq 2l-2$,}\\
\frac{3l-1-k}{l^2},&\textit{if $2l\leq k\leq 3l-2$,}\\
\frac{1}{2l},&\textit{if $k=l-1$ or $k=2l-1$.}
\end{cases}$$ It is normalized to the total probability condition $$\sum\limits_{j=0}^{3l-2}p_j=1.$$

### Quantum Plancherel measure

The Markov matrix for the quantum Plancherel measure is given by transition probabilities $$\mathrm{Prob}(k\to k+1)=\begin{cases}
\frac{q^{k+2}-q^{-(k+2)}}{(q^{k+1}-q^{-(k+1)})(q+q^{-1})},&\textit{if $0\leq k \leq l-3$}\\
0,&\textit{if $k=l-2$}
\end{cases}$$ $$\mathrm{Prob}(k\to k-1)=\begin{cases}
\frac{q^{k}-q^{-k}}{(q^{k+1}-q^{-(k+1)})(q+q^{-1})},&\textit{if $0\leq k \leq l-3$}\\
1,&\textit{if $k=l-2$}
\end{cases}$$ It is a $l-1 \times l-1$ matrix supported on irreducible representations because quantum dimensions of other indecomposable summands in $T(1)^{\otimes N}$ vanish. The largest eigenvalue $\lambda_{\text{max}}=1$ of this matrix has multiplicity $1$. It is not difficult to compute components of the corresponding eigenvector $(p_0,\ldots, p_{l-2})$: $$p_j=-\frac{(q^{j+1}-q^{-(j+1)})^2}{2l}=\frac{2\mathrm{sin}^2\left(\frac{\pi (j+1)}{l} \right)}{l}.$$ It is normalized to the total probability condition $$\sum\limits_{j=0}^{l-2}p_j=1.$$
