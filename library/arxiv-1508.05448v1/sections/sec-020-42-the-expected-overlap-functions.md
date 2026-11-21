---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-020-42-the-expected-overlap-functions
section_title: "The Expected Overlap Functions"
section_number: 4.2
pages: 65-67
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.972
doc_brief: "Concentration of Measure Techniques and Applications — 36 sections: Front matter; Biographical Sketch; Acknowledgments"
---
[]{#sec:Expected label="sec:Expected"}

Since the moments $M_n(\mathbf{p},\mathbf{q})$ satisfy concentration of measure, one is primarily only interested in their expectations. The next quantity we introduce is also defined just for the expectation. (Studying its distribution may be interesting, but we will not comment on this, here.) It is the expected overlap function of Chalker and Mehlig, introduced in [@CM] and further studied by them in [@MC].

Given $A_n \in \operatorname{Mat}_n(\mathbb{C})$, randomly distributed according to Ginibre's ensemble, almost surely it may be diagonalized. This means that we can find eigenvalues $\lambda_1,\dots,\lambda_n \in \mathbb{C}$ as well as pairs of vectors $\psi_1,\phi_1,\dots,\psi_n,\phi_n \in \mathbb{C}^n$ such that $$A_n \psi_k\,=\, \lambda_k \psi_k\, ,\quad
\phi_k^* A_n\, =\, \lambda_k \phi_k^*\, ,\quad
\phi_k^* \psi_j\, =\, \delta_{jk}\, .$$ Using this, for any other vector $\Psi \in \mathbb{C}^n$, there is the formula $$A_n \Psi\, =\, \sum_{k=1}^{n} \lambda_k \langle \phi_k, \Psi \rangle \psi_k\, .$$ These are random because they depend on $A_n$, but we may take the expectation over the randomness.

Given any continuous function, $f$, with compact support on $\mathbb{C}$, one may define $$\omega^{(1)}_n[f]\, =\, \frac{1}{n}\, \mathbb{E}\left[\sum_{k=1}^{n} f(\lambda_k) \|\phi_k\|^2 \|\psi_k\|^2\right]\, .$$ Similarly, given any continuous function, $F$, with compact support on $\mathbb{C}\times \mathbb{C}$, we may define $$\omega^{(2)}_n[F]\, =\, \frac{1}{n}\, \mathbb{E}\left[\sum_{j=1}^{n} \sum_{k\neq j} F(\lambda_j,\lambda_k) \langle \psi_k,\psi_j \rangle \langle \phi_j, \phi_k\rangle\right]\, .$$ Regularity of the eigenvalues and eigenvectors with respect to the matrix entries guarantees existence of functions $\mathcal{O}_n^{(1)} : \mathbb{C}\to \mathbb{C}$ and $\mathcal{O}_n^{(2)} : \mathbb{C}\times \mathbb{C}\to \mathbb{C}$ such that $$\omega^{(1)}_n[f]\, =\, \int_{\mathbb{C}} f(z) \mathcal{O}_n^{(1)}(z)\, d^2z\quad \text{and}\quad
\omega^{(2)}_n[F]\, =\, \int_{\mathbb{C}}\int_{\mathbb{C}} F(z,w) \mathcal{O}_n^{(2)}(z,w)\, d^2z\, d^2w\, .$$ Using these definitions, one may determine a relation between these expected overlap functions and the correlation functions for the eigenvalues. Define $\rho^{(1)}_n$ and $\rho^{(2)}_n$, analogously to $\omega^{(1)}_n$ and $\omega^{(2)}_n$ as $$\rho^{(1)}_n[f]\, =\, \frac{1}{n}\, \mathbb{E}\left[\sum_{k=1}^{n} f(\lambda_k)\right]\, ,\
\text{ and }\
\rho^{(2)}_n[F]\, =\, \frac{1}{n}\, \mathbb{E}\left[\sum_{j=1}^{n} \sum_{k\neq j} F(\lambda_j,\lambda_k)\right]\, .$$ Then there are functions $\mathcal{R}_n^{(1)} : \mathbb{C}\to \mathbb{C}$ and $\mathcal{R}_n^{(2)} : \mathbb{C}\times \mathbb{C}\to \mathbb{C}$ such that $$\rho^{(1)}_n[f]\, =\, \int_{\mathbb{C}} f(z) \mathcal{R}_n^{(1)}(z)\, d^2z\quad \text{and}\quad
\rho^{(2)}_n[F]\, =\, \int_{\mathbb{C}}\int_{\mathbb{C}} F(z,w) \mathcal{R}_n^{(2)}(z,w)\, d^2z\, d^2w\, .$$ Then $$\mathcal{O}_n^{(1)}(z) + \int_{\mathbb{C}} \mathcal{O}_n^{(2)}(z,w)\, d^2w\, =\, \mathcal{R}_n^{(1)}(z)\, .$$ In terms of these functions, for any nonnegative integers $p$ and $q$, $$\label{eq:mnpq}
m_n((p);(q))\, =\, \int_{\mathbb{C}} z^p \overline{z}^q \mathcal{O}_n^{(1)}(z)\, d^2z 
+ \int_{\mathbb{C}} \int_{\mathbb{C}} z^p \overline{w}^q \mathcal{O}_n^{(2)}(z,w)\, d^2z\, d^2w\, .$$ Therefore, the mixed matrix moments are calculable from the overlap functions. Moreover, the limiting values of the moments give some constraints for the limiting behavior of the overlap functions. It is easy to see that $\mathcal{O}_n^{(1)}(e^{i\theta} z) = \mathcal{O}_n^{(1)}(z)$ and $\mathcal{O}_n^{(2)}(e^{i\theta}z,e^{i\theta}w) = \mathcal{O}_n^{(2)}(z,w)$, consistent with the fact that $m_n((p);(q))$ equals $0$ unless $p=q$.
