---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-019-41-mixed-matrix-moments
section_title: "Mixed Matrix Moments"
section_number: 4.1
pages: 60-65
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.994
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
Given any $n\times n$ matrix $A$, any positive integer $k$, and any nonnegative integers $p(1),q(1),\dots,p(k),q(k)$, we may define $$M_n(\mathbf{p};\mathbf{q})\, 
=\, \frac{1}{n}\, \operatorname{tr}[A_n^{p(1)} (A_n^*)^{q(1)} \cdots A_n^{p(k)} (A_n^*)^{q(k)}]\, ,$$ for $\mathbf{p}=(p(1),\dots,p(k))$, $\mathbf{q}=(q(1),\dots,q(k))$. Notice that $M_0=1$. As an example, consider $$\begin{gathered}
M_n((2,2);(2,2))\, = \\ \, \frac{1}{n}\, \sum_{j_1,\dots,j_8=1}^n a_n(j_1,j_2) a_n(j_2,j_3) \overline{a}_n(j_4,j_3) \overline{a}_n(j_5,j_4) a_n(j_5,j_6) a_n(j_6,j_7)
\overline{a}_n(j_8,j_7) \overline{a}_n(j_1,j_8)\, .
\end{gathered}$$ If we consider the Ginibre ensemble and let $a_n(j,k) = (X(j,k)+iY(j,k))/\sqrt{2n}$ as before, then we have $$\mathbb{E}[a_n(j,k) a_n(j',k')]\, =\, \mathbb{E}[\overline{a}_n(j,k) \overline{a}_n(j',k')], =\, 0\ \text{ and } \
\mathbb{E}[a_n(j,k) \overline{a}_n(j',k')]\, =\, n^{-1} \delta_{j,j'} \delta_{k,k'}\, .$$ Recall that Wick's rule says that for mean $0$ Gaussian random variables $X_1,\dots,X_n$, $$\mathbb{E}(X_1X_2\dots X_n)=\sum \prod_{i,j}(X_iX_j)$$ where the sum is over all distinct ways of dividing $1,\dots,n$ into pairs. Using this, and defining $m_n(\mathbf{p},\mathbf{q}) = \mathbb{E}[M_n(\mathbf{p},\mathbf{q})]$, gives us: $$\label{eq:recurrence}
m_n(\mathbf{p},\mathbf{q})\, =\, \sum_{(\mathbf{p}',\mathbf{q}',\mathbf{p}'',\mathbf{q}'') \in \mathcal{S}(\mathbf{p},\mathbf{q})} 

\mathbb{E}[M_n(\mathbf{p}',\mathbf{q}') M_n(\mathbf{p}'',\mathbf{q}'')]\, ,$$ where $\mathcal{S}(\mathbf{p},\mathbf{q})$ is the set of all admissible pairs, which we describe now. Let $R = p(1)+\dots+p(k)+q(1)+\dots+q(k)$, and define $\sigma = (\sigma(1),\dots,\sigma(R)) \in \{+1,-1\}^R$ as $\sigma\, =\, ((+1)^{p(1)},(-1)^{q(1)},\dots,(+1)^{p(k)},(-1)^{q(k)})$ viewed as spins on vertices arranged on a circle. We will sometimes denote this as $\sigma_{\mathbf{p},\mathbf{q}}$. Let $\Sigma(\mathbf{p},\mathbf{q})$ denote pairs $(\sigma',\sigma'')$ as follows. We match up the first $+1$ and any $-1$. Where these two are removed, we pinch the circle into two smaller circles. Then the remaining spins on the two smaller circles comprise $\sigma'$ and $\sigma''$. E.g., for a particular example $$\sigma = (\underline{+1},+1,\underline{-1},-1,+1,+1,-1,-1) \mapsto (\sigma',\sigma'') = ((+1),(-1,+1,+1,-1,-1))\, .$$ The set $\Sigma(\mathbf{p},\mathbf{q})$ is the set of all possible pairs $(\sigma',\sigma'')$ obtainable in this way. We then define $\mathcal{S}(\mathbf{p},\mathbf{q})$ to be the set of all pairs $(\mathbf{p}',\mathbf{q}')$ and $(\mathbf{p}'',\mathbf{q}'')$ by mapping backwards $\Sigma(\mathbf{p},\mathbf{q})$ from $\sigma'$ and $\sigma''$, this way.

Using this, we wish to give the main ideas of the proof of the following theorem.

::: theorem
[]{#thm:MMM label="thm:MMM"} For any $k$ and any $\mathbf{p},\mathbf{q}$, we have $$\lim_{n \to \infty} m_n(\mathbf{p},\mathbf{q})\, =\, m(\mathbf{p},\mathbf{q})\, ,$$ where $m(\mathbf{p},\mathbf{q})$ is as follows. Let $C_R$ denote the number of all non-crossing matchings of $R$ vertices on a circle (Catalan's number). Let $m(\mathbf{p},\mathbf{q})$ denote the cardinality of all such matchings satisfying the following constraint: assigning spins to the $R$ vertices by $\sigma_{\mathbf{p},\mathbf{q}}$, each edge has two endpoints with one $+1$ spin and one $-1$ spin.
:::

As an example, $m((2,2);(2,2)) = 3$ where the matchings are indicated diagrammatically as $$\begin{tikzpicture}
\draw (0,0) circle (1.5cm);
\draw[very thick] (67.5:1.5cm) .. controls (75:0.75cm) and (105:0.75cm)  .. (112.5:1.5cm);
\draw[very thick] (22.5:1.5cm) .. controls (15:0.75cm) and (-15:0.75cm)  .. (-22.5:1.5cm);
\draw[very thick] (-67.5:1.5cm) .. controls (-75:0.75cm) and (-105:0.75cm)  .. (-112.5:1.5cm);
\draw[very thick] (157.5:1.5cm) .. controls (165:0.75cm) and (195:0.75cm)  .. (202.5:1.5cm);
\fill (157.5:1.5cm) circle (1mm);
\fill (112.5:1.5cm) circle (1mm);
\filldraw[fill=white, very thick] (67.5:1.5cm) circle (1mm);
\filldraw[fill=white, very thick] (22.5:1.5cm) circle (1mm);
\fill (-22.5:1.5cm) circle (1mm);
\fill (-67.5:1.5cm) circle (1mm);
\filldraw[fill=white, very thick] (-112.5:1.5cm) circle (1mm);
\filldraw[fill=white, very thick] (-157.5:1.5cm) circle (1mm);
\end{tikzpicture}
\hspace{1cm}
\begin{tikzpicture}
\draw (0,0) circle (1.5cm);
\draw[very thick] (67.5:1.5cm) .. controls (75:0.75cm) and (105:0.75cm)  .. (112.5:1.5cm);
\draw[very thick] (22.5:1.5cm) .. controls (90:0.25cm) ..  (157.5:1.5cm);
\draw[very thick] (-22.5:1.5cm) .. controls (-90:0.25cm) ..  (-157.5:1.5cm);
\draw[very thick] (-67.5:1.5cm) .. controls (-75:0.75cm) and (-105:0.75cm)  .. (-112.5:1.5cm);
\fill (157.5:1.5cm) circle (1mm);
\fill (112.5:1.5cm) circle (1mm);
\filldraw[fill=white, very thick] (67.5:1.5cm) circle (1mm);
\filldraw[fill=white, very thick] (22.5:1.5cm) circle (1mm);
\fill (-22.5:1.5cm) circle (1mm);
\fill (-67.5:1.5cm) circle (1mm);
\filldraw[fill=white, very thick] (-112.5:1.5cm) circle (1mm);
\filldraw[fill=white, very thick] (-157.5:1.5cm) circle (1mm);
\end{tikzpicture}
\hspace{1cm}
\begin{tikzpicture}
\draw (0,0) circle (1.5cm);
\draw[very thick] (67.5:1.5cm) .. controls (0:0.25cm) .. (-67.5:1.5cm);
\draw[very thick] (22.5:1.5cm) .. controls (15:0.75cm) and (-15:0.75cm)  .. (-22.5:1.5cm);
\draw[very thick] (112.5:1.5cm) .. controls (180:0.25cm)  .. (-112.5:1.5cm);
\draw[very thick] (157.5:1.5cm) .. controls (165:0.75cm) and (195:0.75cm)  .. (202.5:1.5cm);
\fill (157.5:1.5cm) circle (1mm);
\fill (112.5:1.5cm) circle (1mm);
\filldraw[fill=white, very thick] (67.5:1.5cm) circle (1mm);
\filldraw[fill=white, very thick] (22.5:1.5cm) circle (1mm);
\fill (-22.5:1.5cm) circle (1mm);
\fill (-67.5:1.5cm) circle (1mm);
\filldraw[fill=white, very thick] (-112.5:1.5cm) circle (1mm);
\filldraw[fill=white, very thick] (-157.5:1.5cm) circle (1mm);
\end{tikzpicture}$$ Theorem [\[thm:MMM\]](#thm:MMM){reference-type="ref" reference="thm:MMM"} is a well-known result. We refer to [@Kemp] for a discussion. We will motivate a proof of this result, without including all details, here. Our reason is that we actually want to use this result to motivate the discussion of random matrices and spin glasses further, which we indicated earlier.

## Argument for the Proof of the Mixed Matrix Moments {#subsec:Argument}

The first step in the argument for the proof of Theorem [\[thm:MMM\]](#thm:MMM){reference-type="ref" reference="thm:MMM"} is to use concentration of measure (COM) to replace ([\[eq:recurrence\]](#eq:recurrence){reference-type="ref" reference="eq:recurrence"}) with a nonlinear recurrence relation. Here what we mean is non-linearity in the probability measure for the random entries of the matrix. Since the expectation is linear, what we really mean is to obtain a product of two expectations. If $M_n(\mathbf{p}',\mathbf{q}')$ and $M_n(\mathbf{p}'',\mathbf{q}'')$ were independent, then we could replace the expectation by a product, but they are not exactly independent. Instead, they satisfy COM, which means that they are approximately non-random. And, of course, non-random variables are exactly independent of every other random variable (as well as themselves).

The easiest version of COM is just $L^2$-concentration. For example, the following lemma is very easy to prove:

::: lemma
[]{#lem:unifGrad label="lem:unifGrad"} Suppose $f : \mathbb{R}^n \to \mathbb{R}$ is a function such that\
$\|\nabla f\|^2_{\infty} = \sup_{\mathbf{x} \in \mathbb{R}^n} \sum_{k=1}^n \left(\frac{\partial f}{\partial x_k}(\mathbf{x})\right)^2$ is finite. Then if $U_1,\dots,U_n,V_1,\dots,V_n$ are IID $\mathcal{N}(0,1)$ random variables then $$\label{eq:lemG}
\mathbb{E}\left[\left(f(\mathbf{U})-f(\mathbf{V})\right)^2\right]\, \leq\, 2 \|\nabla f\|_{\infty}^2\, .$$
:::

This can be proved using the basic, but important method of "quadratic interpolation," which is sometimes called the "smart path method" by some mathematicians working on spin glasses.

::: proof
*Proof.* Let $\boldsymbol{Z} = (Z_1,\dots,Z_n)$ be an IID $\mathcal{N}(0,1)$ vector, independent of $\mathbf{U}$ and $\mathbf{V}$. Then define $\widetilde{\mathbf{U}}(\theta) = \sin(\theta)\, \mathbf{U} 
+ \cos(\theta)\, \mathbf{Z}$ and $\widetilde{\mathbf{V}}(\theta) = \sin(\theta)\, \mathbf{V} 
+ \cos(\theta)\, \mathbf{Z}$. Then $\frac{d}{d\theta} \widetilde{\mathbf{U}}(\theta) = \widetilde{\mathbf{U}}(\theta+\frac{\pi}{2})$, and $\mathbb{E}[\widetilde{\mathbf{U}}(\theta) \widetilde{\mathbf{U}}(\theta+\frac{\pi}{2})] = 0$. This means that $\widetilde{\mathbf{U}}(\theta)$ is statistically independent of its $\theta$-derivative. Similar results hold for $\widetilde{\mathbf{V}}(\theta)$. On the other hand $\mathbb{E}[\widetilde{\mathbf{V}}(\theta) \widetilde{\mathbf{U}}(\theta+\frac{\pi}{2})] = 
-\sin(\theta)\cos(\theta)$.

Next, using the fundamental theorem of calculus, $$\mathbb{E}\left[\left(f(\mathbf{U})-f(\mathbf{V})\right)^2\right]\,
=\, \int_0^{\pi/2} \frac{d}{d\theta}
\mathbb{E}\left[\left(f(\widetilde{\mathbf{U}}(\theta))-f(\widetilde{\mathbf{V}}(\theta))\right)^2\right]\,
d\theta\, ,$$ and an easy calculation using Gaussian integration by parts (and the covariance formulas mentioned above) shows that $$\frac{d}{d\theta}
\mathbb{E}\left[\left(f(\widetilde{\mathbf{U}}(\theta))-f(\widetilde{\mathbf{V}}(\theta))\right)^2\right]\,
=\, 2\sin(2\theta) \mathbb{E}\left[\nabla f(\widetilde{\mathbf{U}}(\theta)) \cdot 
\nabla f(\widetilde{\mathbf{V}}(\theta))\right]\, .$$ Then (4.7) follows by using the Cauchy-Schwarz inequality. ◻
:::

This is only the simplest Gaussian COM result. Notice that the method of proof is similar to the method used to proved Talagrand's Gaussian concentration of measure inequality for Lipschitz functions as stated in chapter 2 Theorem [\[GCOM\]](#GCOM){reference-type="ref" reference="GCOM"}

This lemma is a tool which can be applied to show that the various mixed matrix moments $M_n(\mathbf{p},\mathbf{q})$ do satisfy COM. We present this lemma here, because it is easier to obtain concentration of measure for the matrix moments using this lemma than with Theorem [\[GCOM\]](#GCOM){reference-type="ref" reference="GCOM"}. It should be noted, that [\[GCOM\]](#GCOM){reference-type="ref" reference="GCOM"} will also work in this case and will give a sharper concentration bound. Either way, it is an interesting calculation, and much of the combinatorics, especially involving matchings related to Catalan's number, are first visible in the grad-squared calculation.

Since the goal of this section is to give a general outline of the proof of the formula for the mixed matrix moments and relate it to spin glass techniques, we will just state that the desired concentration of measure result is true.

Then we are able to boost ([\[eq:recurrence\]](#eq:recurrence){reference-type="ref" reference="eq:recurrence"}) to $$\label{eq:recur2}
\lim_{n \to \infty} m_n(\mathbf{p},\mathbf{q}) - 
\sum_{(\mathbf{p}',\mathbf{q}',\mathbf{p}'',\mathbf{q}'') \in \mathcal{S}(\mathbf{p},\mathbf{q})} 
m_n(\mathbf{p}',\mathbf{q}') m_n(\mathbf{p}'',\mathbf{q}'')\, =\, 0\, .$$ Another easy fact is that, due to symmetry, $m_n(\mathbf{p},\mathbf{q})=0$ unless $p(1)+\dots+p(k)=q(1)+\dots+q(k)$. And, of course, $m_0=1$.

Using this, and the method of induction, one can then prove Theorem [\[thm:MMM\]](#thm:MMM){reference-type="ref" reference="thm:MMM"}.

## Commentary on Proof Technique

The quadratic interpolation technique is important in spin glasses. The first major use was by Guerra and Toninelli [@GT] and Guerra [@G]. It is called the "smart path method" by Talagrand [@Talagrand2]. This is the method which we used to prove Talagrand's Gaussian concentration of measure inequality in chapter 2.

Using Wick's rule to obtain a recurrence relation is important in many subjects. It is a standard approach to determining moments of random matrices. See, for instance, [@AndersonGuionnetZeitouni], chapter 1. In the context of Gaussian spin glasses, this technique combined with stochastic stability leads to the Aizenman-Contucci identities [@AC]. When combined with concentration of measure it leads to the Ghirlanda-Guerra identities [@GG]. See, for instance, the review [@ContucciGiardina].

For random matrices, the problem of recombining the moments into useful information about the limiting empirical spectral measure is also important. For Hermitian random matrices, this is related to the classical moment method. The standard approach is to put the moments together into the Stieltjes transform, and then to proceed from there [@Pastur]. Again, a good general reference is [@AndersonGuionnetZeitouni], chapter 1.

For spin glasses, the problem of integrating the Ghirlanda-Guerra identities into a useful result for mean-field models was solved only relatively recently. Panchenko showed that the "extended Ghirlanda-Guerra identities" imply Parisi's ultrametric ansatz [@Panchenko]. This is an important work. One element of his proof is putting various terms together into a a new exponential type generating function. This might be somewhat analogous to the Stieltjes transform step. But after that, the proofs are very different.

For non-Hermitian random matrices, getting useful information from the moments is the topic we focus on next.
