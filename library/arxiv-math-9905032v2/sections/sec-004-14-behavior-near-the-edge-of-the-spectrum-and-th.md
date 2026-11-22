---
doc_id: arxiv-math-9905032v2
doc_title: "Asymptotics of Plancherel measures for symmetric groups"
section_id: sec-004-14-behavior-near-the-edge-of-the-spectrum-and-th
section_title: "Behavior near the edge of the spectrum and the Airy ensemble"
section_number: 1.4
pages: 8-10
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.962
doc_brief: "Asymptotics of Plancherel measures for symmetric groups — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
[]{#s14 label="s14"}

The discrete sine kernel $\mathsf{S}(k,a)$ vanishes if $a\ge 2$. Therefore, it follows from Theorem [\[t2\]](#t2){reference-type="ref" reference="t2"} that the limit correlations $\lim\boldsymbol{\varrho}(n,X(n))$ vanish if $a_i\ge 2$ for some $i$. However, as will be shown below in Proposition [\[p41\]](#p41){reference-type="ref" reference="p41"}, after a suitable scaling near the edge $u=2$, the correlation functions $\boldsymbol{\varrho}^\theta$ converge to the correlation functions given by the Airy kernel [@F; @TW]

$$\mathsf{A}(x,y)=\frac{A(x)A'(y)-A'(x)A(y)}{x-y}\,.$$

Here $A(x)$ is the Airy function:

$$\label{e17}
A(x)=\frac1\pi\,\int_0^\infty \cos\left(\frac{u^3}3+xu\right)\,du.$$

In fact, the following more precise statement is true about the behavior of the Plancherel measure near the edge $u=2$. By symmetry, everything we say about the edge $u=2$ applies to the opposite edge $u=-2$.

Consider the random point process on $\mathbb{R}$ whose correlation functions are given by the determinants

$$\rho^{\textup{Airy}}_k(x_1,\dots,x_k)= \det \Big[\,\mathsf{A}(x_i,x_j)
\Big]_{1\le i,j \le k}$$

and let

$$\zeta=(\zeta_1 > \zeta_2 > \zeta_3 > \dots ) \in\mathbb{R}^\infty$$

be its random configuration. We call the random variables $\zeta_i$'s the *Airy ensemble*. It is known [@F; @TW] that the Airy ensemble describes the behavior of the (properly scaled) 1st, 2nd, and so on largest eigenvalues of a Gaussian random Hermitian matrix. The distribution of individual eigenvalues was obtained by Tracy and Widom in [@TW] in terms of certain Painlevé transcendents.

It has been conjectured by Baik, Deift, and Johansson that the random variables

$$\widetilde{\lambda}=
\left(\widetilde{\lambda}_1 \ge \widetilde{\lambda}_2 \ge \dots
\right)\,,
\quad 
\widetilde{\lambda}_i =
n^{1/3} \, \left(
\frac{\lambda_i}{n^{1/2}}-2 \right)$$

converge, in distribution and together with all moments, to the Airy ensemble. They verified this conjecture for individual distribution of $\lambda_1$ and $\lambda_2$ in [@BDJ1] and [@BDJ2], respectively. In particular, in the case of $\lambda_1$, this generalizes the result of [@VK1; @VK2] that $\frac{\lambda_1}{\sqrt n} \to 2$ in probability as $n\to\infty$. The computation of $\lim \frac{\lambda_1}{\sqrt n}$ was known as the Ulam problem; different solutions to this problem were given in [@AD; @J; @S].

Convergence of all expectations of the form

$$\label{e18a}
\left\langle
\prod_{k=1}^r 
\sum_{i=1}^\infty e^{t_k \widetilde{\lambda}_i}
\right\rangle\,,
\quad t_1,\dots,t_r>0\,, 
\quad r=1,2,\dots\,,$$

to the corresponding quantities for the Airy ensembles was established in [@O]. The proof in [@O] was based on a combinatorial interpretation of [\[e18a\]](#e18a){reference-type="eqref" reference="e18a"} as the asymptotics in a certain enumeration problem for random surfaces.

In the present paper we use different ideas to prove the following

::: theorem
[]{#t3 label="t3"} As $n\to\infty$, the random variables $\widetilde{\lambda}$ converge, in joint distribution, to the Airy ensemble.
:::

This is done in Section [\[s4\]](#s4){reference-type="ref" reference="s4"} using methods described in the next subsection. The result stated in Theorem [\[t3\]](#t3){reference-type="ref" reference="t3"} was independently obtained by K. Johansson in [@J2].
