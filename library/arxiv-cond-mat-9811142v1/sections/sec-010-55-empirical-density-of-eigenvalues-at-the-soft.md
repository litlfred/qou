---
doc_id: arxiv-cond-mat-9811142v1
doc_title: "arXiv:cond-mat/9811142v1 [cond-mat.mes-hall] 10 Nov 1998"
section_id: sec-010-55-empirical-density-of-eigenvalues-at-the-soft
section_title: "Empirical density of eigenvalues at the soft edge"
section_number: 5.5
pages: 32-33
source_pdf: 9811142v1.pdf
source_sha256: 8666ebc040336b14
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.971
---
The dynamical distribution functions at the soft edge calculated in Section 4 can be realized by parameter dependent random matrices of the type ([\[1.3\]](#1.3){reference-type="ref" reference="1.3"}). Thus we can numerically construct random matrices and empirically compute eigenvalue distributions for comparison against the theoretical prediction. The simplest distribution to compute empirically is the density (one-point function). Here we will undertake such a calculation for the orthogonal to unitary transition at the soft edge.

As deduced from ([\[2.s\]](#2.s){reference-type="ref" reference="2.s"}), ([\[2.1b\]](#2.1b){reference-type="ref" reference="2.1b"}) and ([\[3.20\'\]](#3.20'){reference-type="ref" reference="3.20'"}) the theoretical prediction for the scaled density at the soft edge of the orthogonal to unitary transition is $$\begin{aligned}
\label{6.1}
\rho_{(1)}^{\rm soft}(X;t) & = & S_1^{\rm soft}(X,X;t,t) \nonumber \\
& = & \int_0^\infty \Big ( {\rm Ai} (X + v) \Big )^2 \, dv +
{1 \over 2} \int_0^\infty e^{-st_X} {\rm Ai} (X - s) \, ds.
\end{aligned}$$ The theory of Section 1 tells us that the parameter dependent random matrices ([\[1.3\]](#1.3){reference-type="ref" reference="1.3"}), for an appropriate $X^{(0)}$ have, in the infinite dimension limit, a scaled density at the soft edge given by ([\[6.1\]](#6.1){reference-type="ref" reference="6.1"}). Since we are considering the orthogonal to unitary transition, $X^{(0)}$ must be chosen as a real symmetric matrix with joint p.d.f. for the elements $$P(X^{(0)}) = \prod_{j=1}^N \Big ( {1 \over 2 \pi} \Big )^{1/2}
e^{ - X_{jj}^{(0)\, 2}/2} \prod_{j < k} {1 \over \pi^{1/2}}
e^{ - X_{jk}^{(0) \, 2}}.$$ The joint distribution of the elements of $X$, $P(X;\tau)$ say, is obtained by integrating over $X_{jj}^{(0)}$ and $X_{jk}^{(0)}$. Thus $$\begin{aligned}
\label{6.7}
P(X;\tau) & = & \prod_{j=1}^N \int_{-\infty}^\infty dX_{jj}^{(0)} \,
\prod_{j < k}  \int_{-\infty}^\infty dX_{jk}^{(0)} \,
P(X^{(0)}) P(X^{(0)};X;\tau) \nonumber \\
& = &  \prod_{j=1}^N {e^{-X_{jj}^2}/(1 + e^{-2\tau}) \over
\sqrt{\pi (1 + e^{-2 \tau})}}
\prod_{j < k} {2 \over \pi \sqrt{1 - e^{- 4 \tau}}}
e^{- 2 ({\rm Re} X_{jk})^2/(1 + e^{-2\tau})}
e^{- 2 ({\rm Im} X_{jk})^2/(1 - e^{-2\tau})}, \nonumber \\
\end{aligned}$$ which tells us that the diagonal and the real and imaginary parts of the upper triangular elements are all independent, having Gaussian distributions with mean zero and variances $2/(1 + e^{-2 \tau})$, $4/(1 + e^{-2 \tau})$ and $4/(1 - e^{-2 \tau})$ respectively. Hence, for a given value of $N$ and $\tau$ such matrices are simple to generate numerically. For each such random matrix the eigenvalues $\lambda_j$ are computed and scaled according to $\lambda \mapsto (\lambda_j - (2N)^{1/2})
2^{1/2} N^{1/6}$. For $N$ large enough and with $\tau$ related to $t$ by ([\[4.6\]](#4.6){reference-type="ref" reference="4.6"}) the corresponding empirical density should approach ([\[6.1\]](#6.1){reference-type="ref" reference="6.1"}). The situation for a relative small value of $N$ (recall the occurence of $N^{1/6}$) is illustrated in Figure 1, where good agreement with the infinite dimension limit is observed.

Also of interest is the possibility of providing a realization of the hard edge results. Unfortunately here it seems that the initial conditions used do not precisely correspond to a situation in which $X$ in ([\[1.6\]](#1.6){reference-type="ref" reference="1.6"}) can be generated from a formula analogous to ([\[6.7\]](#6.7){reference-type="ref" reference="6.7"}). The problem is that if $X^{(0)}$ is a real $n \times m$ matrix with independent Gaussian entries, then the square of the eigenvalues of $X^{(0)\dagger} X^{(0)}$ has p.d.f. ([\[1.2\]](#1.2){reference-type="ref" reference="1.2"}) with $a = n - m - 1$. However in deducing ([\[1.4\]](#1.4){reference-type="ref" reference="1.4"}) from ([\[1.6\]](#1.6){reference-type="ref" reference="1.6"}) in the case of transitions to unitary symmetry ($\beta = 2$) we must take $a = n - m$, which is thus incompatible with the sought initial condition.

<figure id="1.f1">

<figcaption><span id="1.f1" label="1.f1"></span> Empirical histogram of the scaled soft edge density for 500 parameter dependent random matrices of the form (<a href="#6.7" data-reference-type="ref" data-reference="6.7">[6.7]</a>) with <span class="math inline"><em>τ</em> = .05</span> and <span class="math inline"><em>N</em> = 100</span>, compared against the infinite dimension form (<a href="#6.1" data-reference-type="ref" data-reference="6.1">[6.1]</a>). </figcaption>
</figure>
