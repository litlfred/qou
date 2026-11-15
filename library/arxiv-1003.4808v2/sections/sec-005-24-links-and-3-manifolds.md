---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-005-24-links-and-3-manifolds
section_title: "Links and 3-manifolds"
section_number: 2.4
pages: 13-14
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 1.0
doc_brief: "Quantum Field Theory and the Volume Conjecture — 15 sections: Front matter; Preliminaries; The many dimensions of the volume"
---
[]{#sec:links label="sec:links"}

The final generalization of the volume conjecture that we consider is to arbitrary links in arbitrary three-manifolds. Here we really begin to require a true TQFT description of the "quantum $G$-invariants" of knots and links. This was supplied by quantum Chern-Simons theory with compact gauge group $G$ in [@Wit-Jones], and reinterpreted via quantum groups and R-matrices in [@Resh-Tur]. Using either of these approaches, one may define a quantum partition function

$$Z^G(M,L;\{R_a\};\hbar) \label{ZM}$$

for a link $L$ in any three-manifold $M$, where each component of the link is colored with a different representation $R_a$. The "polynomial" $P^G_R$ is obtained from this after normalizing by the partition function of an empty manifold,

$$P^G_{\{R_a\}}(M,L;q) = \frac{Z^G(M,L;\{R_a\};\hbar)}{Z^G(M;\hbar)}\,,\qquad (q=e^{2\hbar})\,.$$

Thus, in the case of the colored Jones polynomial,

$$J_N(K;q) = \frac{Z^{SU(2)}(S^3,K;R_N;\hbar)}{Z^{SU(2)}(S^3;\hbar)}\,.$$

The integer $k$ (appearing in $q=e^{2\hbar}=e^{\frac{2\pi i}{k}}$) is identified with the "level" or coupling constant of the compact Chern-Simons theory.[^1]

The partition function [\[ZM\]](#ZM){reference-type="eqref" reference="ZM"} supplies the left-hand-side of the volume conjecture. We then want to understand the asymptotics of $Z^G(M,L;\{R_a\};\hbar)$ in the limit $\hbar\to 0$, with a parameter $u_a = \hbar(\lambda_a^* + \rho^*)$ held fixed for each separate link component. The answer should be given by perturbative, quantum Chern-Simons theory with *complex* gauge group $G_{\mathbb{C}}$, evaluated on the link complement $M\backslash L$, in the background of a flat connection with fixed holonomy

$$m_a = \exp(u_a)$$

around the meridian of each excised link component. Denoting this perturbative Chern-Simons partition function by

$$Z^{G_{\mathbb{C}}}_{\rm pert}(M\backslash L;\{u_a\};\hbar) = \exp\left(-\frac1{4\hbar}I_{CS}(\{u_a\})-\frac\delta2\log\hbar+\ldots\right)\,,$$

we expect that

$$\boxed{Z^G(M,L;\{R_a\};\hbar) \;\overset{\hbar\to 0}{\sim}\; Z^{G_{\mathbb{C}}}_{\rm pert}(M\backslash L;\{u_a\};\hbar)}\,. \label{fullVC}$$

This discussion can also be rephrased in a somewhat more symmetric manner, using link complements on both sides of the volume conjecture. It turns out that in compact Chern-Simons theory the partition function of a knot (or link) $K\subset M$ colored by representation $R_\lambda$ is equivalent to the partition function of the knot complement $M\backslash K$ with fixed meridian holonomy

$$m = \exp\left(i\pi\frac{\lambda^*+\rho^*}{k}\right) = \exp\left(\hbar(\lambda^*+\rho^*)\right) = \exp(u)\,.$$

For the compact $G$ theory to make sense, the eigenvalues of the matrix $u/i\pi$ must clearly be rational. However, interesting asymptotics --- potentially with exponential growth as in [\[fullVC\]](#fullVC){reference-type="eqref" reference="fullVC"} --- occur when $u$ is *analytically continued* away from such rational values. This process of analytic continuation naturally lands one in the regime of Chern-Simons theory with complex gauge group $G_{\mathbb{C}}$ [@DGLZ].\
After so many generalizations, it may be unclear that the volume conjecture has anything to do with volumes anymore. Indeed, for higher-rank gauge groups $G$, "volume" should not be a hyperbolic volume but rather the "volume" of a holonomy representation

$$\varrho : \pi_1 (M\backslash K) \to G_{{\mathbb{C}}}\,. \label{rhofirst}$$

Even in the case of $G=SU(2)$ and knots in the three-sphere, one may run across cases of non-hyperbolic knot complements. It was clear from the initial days of the volume conjecture [@Mur-Mur] that even in these cases the asymptotics of $J_N(K;q)$ could still be given by an appropriate flat (but non-hyperbolic/non-metric) $SL(2,{\mathbb{C}})$ structure.

[^1]: To be completely precise, the integer $k$ used throughout these lectures is the sum of the Chern-Simons level and the dual Coxeter number of $G$. []{#foot:k label="foot:k"}
