---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-011-32-1-matrix-model
section_title: "1-matrix model"
section_number: 3.2
pages: 47-49
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.681
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
Hermitean matrix integrals are usually transformed to the eigenvalue form by
separation of angular and eigenvalue variables. As usually, the simplest is
the case of the 1-matrix model

\be
Z_N\{t\} \equiv c_N\int_{N\times N} dH e^{\sum_{k=0}^{\infty} t_k {\rm Tr}
H^k},
\label{1mamo"}
\ee
where this separations does not involve any information about unitary-matrix
integrals. Take
\be
H = U^{\dagger}DU,
\label{diag}
\ee
where $U$ is a unitary matrix and
diagonal matrix $D = {\rm diag}(h_1...h_N)$ has eigenvalues of $H$ as its
entries. Then integration measure
\be
dH = \prod_{i,j=1}^N dH_{ij} = \frac{[dU]}{[dU_{Cartan}]} \prod_{i-1}^N dh_i
\Delta^2(h),
\label{Dyson}
\ee
where "Van-der-Monde determinant" $\Delta (h) \equiv det_{(ij)} h_i^{j-1} =
\prod_{i>j}^N (h_i - h_j)$
and $[dU]$ is Haar measure of integration over unitary matrices.

The way to derive eq.(\ref{Dyson}) is to consider the norm of infinitesimal
variation
\be
\mid\mid \delta H\mid\mid^2 &\equiv \sum_{i,j=1}^N \mid \delta H_{ij}\mid^2 =
 \sum_{i,j=1}^N \delta H_{ij}\delta H_{ji} = {\rm Tr} (\delta H)^2 = \nn \\
&= {\rm Tr}\left(-U^{\dagger}\delta UU^{\dagger}DU + U^{\dagger}D\delta U
+ U^{\dagger}\delta DU \right)^2 = \nn \\
&= {\rm Tr} (\delta D)^2 + 2i{\rm Tr}{\delta u}[\delta D,D] +
2{\rm Tr}\left(-{\delta u} D {\delta u} D + (\delta u)^2D^2 \right), \nn
\ee
where $\delta u \equiv \frac{1}{i}{\delta U}U^{\dagger} = \delta u^{\dagger}$
and $\delta D = {\rm diag}(\delta h_1\ldots \delta h_N)$.
The second term at the r.h.s. vanishes because both $D$ and $\delta D$ are
diagonal and commute. Therefore
\be
\mid\mid \delta H\mid\mid^2 = \sum_{i=1}^N (\delta h_i)^2 +
\sum_{i,j=1}^N (\delta u)_{ij}(\delta u)_{ji}(h_i-h_j)^2. \nn
\ee
Now it remains to recall the basic relation between the infinitesimal norm and
the measure:
${\rm if}\ \ \mid\mid \delta l \mid\mid^2 = G_{ab}\delta l^a\delta l^b \ \
{\rm then}\ \ [dl] = \sqrt{{\rm det}_{ab}G_{ab}} \prod_a dl^a, $
to obtain eq.(\ref{Dyson}) with Haar measure
$[dU] = \prod_{ij}^N du_{ij}$ being associated with the infinitesimal norm
\be
\mid\mid \delta u\mid\mid^2 = {\rm Tr}(\delta u)^2 = \sum_{i,j=1}^N \delta
u_{ij}\delta u_{ji} = \sum_{i,j=1}^N \mid \delta u_{ij}\mid^2 \nn
\ee
and $[dU_{Cartan}] \equiv \prod_{i=1}^N du_{ii}$.

Coming back to the 1-matrix model it remains  to note that the "action"
${\rm Tr} U(H) \equiv \sum_{k=0}^{\infty} t_k {\rm Tr}H^k$ with $H$ substituted
in the form (\ref{diag}) is independent of $U$:
\be
{\rm Tr} U(H) = \sum_{i=1}^N U(h_i). \nn
\ee
Thus
\be
Z_N\{t\} = \frac{1}{N!} \prod_{i=1}^N \int dh_i e^{U(h_i)} \prod_{i>j}^N
(h_i-h_j)^2 = \nn \\
= \frac{1}{N!} \prod_{i=1}^N \int dh_i e^{U(h_i)} \Delta^2(h),
\label{1mamoev}
\ee
provided $c_N$ is chosen to be
\be
c_N^{-1} = N!\frac{{\rm Vol}_{U(N)}}{({\rm Vol}_{U(1)})^N},
\label{cN}
\ee
where the volume of unitary group in Haar measure is equal to
\be
{\rm Vol}_{U(N)} = \frac{(2\pi)^{N(N+1)/2}}{\prod_{k=1}^N k!}.
\label{volun}
\ee
A simple way to derive eq.(\ref{volun}) will be described at the end of this
section, as an example of application of orthogonal polinomials technique.
