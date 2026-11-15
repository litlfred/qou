---
doc_id: arxiv-2201.05665v1
doc_title: "HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY"
section_id: sec-001-2-the-sine-kernel-determinant
section_title: "The sine-kernel determinant"
section_number: 2
pages: 2-3
source_pdf: 2201.05665v1.pdf
source_sha256: bad7bde03d199a73
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.99
doc_brief: "HAROLD WIDOM’S WORK IN RANDOM MATRIX THEORY — This is a survey of Harold Widom’s work in random matrices."
---
Let $J = \cup_{k=0}^{n}J_k = \cup_{k=0}^{n}(a_k, b_k)$ be a union of $n+1$ disjoint intervals in $\mathbb{R}$. Consider the Fredholm determinant $$P_x= \det \left( 1 - K_{\textrm{sine}}\right),$$ where $K_{\textrm{sine}}$ is the trace class operator in $L_2\Bigl(J; dz\Bigr)$ with kernel $$K_{\textrm{sine}}(z,z') = \frac{\sin x(z-z')}{\pi (z-z')}.$$ The determinant $P_x$ plays a central role in random matrix theory. Indeed, it is the probability of finding no eigenvalues in the union of intervals $\frac{xJ}{\pi} := \cup_{k=0}^{n}\left(\frac{xa_k}{\pi}, \frac{xb_k}{\pi}\right)$ for a random Hermitian matrix chosen from the Gaussian Unitary Ensemble (GUE), in the bulk scaling limit with mean spacing 1 (see [@M] and Figure [1](#fig:sine){reference-type="ref" reference="fig:sine"}). Moreover, in the one interval case, the second derivative of $P_x$ describes the distribution of normalized spacings of eigenvalues of large random GUE matrices (see, e.g. [@Deift0]). The determinant $P_x$ also appears in quantum and statistical mechanics. For instance, it describes the emptiness formation probability in the one-dimensional impenetrable Bose gas [@L] and the gap probability in the one dimensional Coulomb gas, at inverse temperature $\beta = 2$ (see, e.g. [@D1]).

The key analytical issue related to $P_x$ is its large $x$ behavior, i.e., the "large gap asymptotics". Harold Widom made major contributions to the resolution of this question.

<figure id="fig:sine">

<figcaption>The eigenvalues of a large (<span class="math inline">2000 × 2000</span>) GUE matrix. The full point process sits on the bottom of the figure, and the histogram records the density of points (approximating the Wigner semi-circle). Inlaid is a zoom-in of the point process. As the size of the GUE matrix goes to infinity, this converges to <span class="math inline"><em>β</em> = 2</span> sine process whose gap probabilities are discussed here.</figcaption>
</figure>

In the one interval case, $n =0$, after rescaling and translation, we may assume $J = (-1, 1)$. For this case, in 1973, des Cloizeaux and Mehta [@dCM] showed that as $x\to\infty$, $$\ln P_x=-{x^2\over 2} -{1\over 4}\ln x+ c_0 +o(1),\label{as1}$$ for some constant $c_0$. In 1976, Dyson [@D2] showed that $P_x$ in fact has a full asymptotic expansion of the form $$\label{dyson_as}
\ln P_x=-{x^2\over 2} -{1\over 4}\ln x+ c_0 +{a_1\over x}+ {a_2\over
x^2}+\cdots.$$ Dyson identified all the constants $c_0$, $a_1$, $a_2$, $\dots$. Of particular interest is the constant $c_0$, which he found to be $$c_0={1\over 12}\ln 2+ 3\zeta'(-1),\label{c0}$$ where $\zeta(z)$ is the Riemann zeta-function. It should be noted that Dyson obtained this result using one of the early results of Widom [@33] on the asymptotics of Toeplitz determinants with symbols supported on circular arcs.

The results in [@dCM] and [@D2] were not fully rigorous. In [@72], using an adaptation of Szegő's classical method to the continuous analogues of orthogonal polynomials (the so-called Krein functions), Widom gave the first rigorous proof of the leading asymptotics in ([\[as1\]](#as1){reference-type="ref" reference="as1"}) in the form $$\ln P_x=-{x^2\over 2}(1+o(1))$$ as $x \to \infty$. Actually, Widom proved a slightly stronger result, $$\frac{d}{dx}\ln P_x = -x + O(1)$$ as $x \to \infty$. In addition, Widom computed the leading asymptotics of $\textrm{tr}\left( (1- K_{\textrm{sine}})^{-1}K_{\textrm{sine}}\right)$, which is the ratio of the probability that there is at most one eigenvalue in the interval $\left(\frac{-x}{\pi}, \frac{x}{\pi}\right)$ to $P_x$. In the subsequent paper [@83], Widom considered the multi-interval case, $n > 0$, and showed that as $x \to \infty$, $$\frac{d}{dx}\ln P_x = c_1 x + c_2(x) + o(1)$$ where $c_1$ is a negative constant and $c_2(x)$ is a certain bounded oscillatory function of $x$, which was described up to the solution of a Jacobi inversion problem[^1]. The method of [@83] is a further development of the approach in [@72]. As in [@72], Widom also computes the leading asymptotics of $\textrm{tr}\left( (1- K_{\textrm{sine}})^{-1}K_{\textrm{sine}}\right)$.

The formula ([\[c0\]](#c0){reference-type="ref" reference="c0"}) for $c_0$ in [@D2] was in the form of conjecture: A rigorous proof of ([\[c0\]](#c0){reference-type="ref" reference="c0"}) was only given in 2004. In fact, two proofs of this formula were given independently in [@K] and [@E]. It is remarkable that the proof of ([\[c0\]](#c0){reference-type="ref" reference="c0"}) in [@K] again uses (in conjunction with the nonlinear steepest descent method) Widom's computation in [@33].

[^1]: An explicit formula for $c_2(x)$, in terms of the Riemann theta-function, was obtained later in [@DIZ].
