---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-018-39-volume-of-unitary-group
section_title: "Volume of unitary group"
section_number: 3.9
pages: 68-70
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 0.967
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
Formalism of orthogonal polinomials provides also a simple derivation of
eq.(\ref{volun}) for the volume of unitary group. Consider
eq.(\ref{1mamoev}) with $U(H) = H^2$. Then Gaussian matrix integral can be
easily evaluated:
\be
c_N\int_{N\times N} dH e^{-\frac{1}{2}{\rm Tr}H^2} =
c_N\prod_{i=1}^N \int dH_{ii}e^{-\frac{1}{2}H_{ii}^2}
\prod_{i<j}^N \int d^2H_{ij} e^{-\mid H_{ij}\mid^2} =
(2\pi)^{N^2/2}, \nn
\ee
while according to eqs.(\ref{orthopol}) and (\ref{ZNprod})
the same integral is equal to
\be
\frac{1}{N!}\prod_{i=1}^N\int_{-\infty}^{+\infty}e^{-\frac{1}{2}h_i^2}
\prod_{i>j}^N (h_i-h_j)^2 =
\prod_{j=1}^N \mid\mid {\rm He}_{j-1} \mid\mid^2. \nn
\ee
Here $\mid\mid {\rm He}_{j-1} \mid\mid$
stand for the norms of orthogonal Hermite
polinomials (\ref{hepo}), $\mid\mid {\rm He}_k \mid\mid^2  =  \sqrt{2\pi} k!$.
Comparing the two expressions for the same integral we get:
\be
c_N^{-1} = (2\pi)^{\frac{N^2}{2}}\prod_{k=0}^{N-1} \frac{1}{\sqrt{2\pi}k!} =
\frac{(2\pi)^{\frac{N(N-1)}{2}}}{\prod_{k=0}^{N-1} k!}.
\label{cnform}
\ee
According to (\ref{cN})
\be
c_N^{-1} = N!\frac{{\rm Vol}_{U(N)}}{({\rm Vol}_{U(1)})^N}
\nn
\ee
and ${\rm Vol}_{U(1)} = 2\pi$. Thus we obtain eq.(\ref{volun}):
\be
{\rm Vol}_{U(N)} = \frac{(2\pi)^{\frac{N(N+1)}{2}}}{\prod_{k=0}^N k!}.
\nn
\ee

An example of somewhat more sophisticated (quantum) group-theoretical
quantity, arising from Gaussian matrix models, is provided by the following
formula for the $q$-factorial \cite{CAD} (see also \cite{KMSW2}):
\be
\frac{1}{(q,q)_N} \equiv  \prod_{n=1}^N \frac{1}{1-q^n} =
\frac{\int\int_{N\times N} dH[dU] e^{-m^2{\rm Tr}H^2 + {\rm
Tr}HUHU^{\dagger}}}{{\rm Vol}_{U(N)} \int_{N\times N} dH e^{-m^2{\rm Tr}H^2}}.
\ee
Integral in the numerator is over Hermitean ($H$) and unitary ($U$) $N\times
N$ matrices, and $q \equiv m^2 - \sqrt{m^4-1}$.

Explicit expression (\ref{cnform}) can be used to prove that
$c_N = 0$ for all {\it negative} integer $N$ \cite{Toda}.
Eq.(\ref{cnform}) defines $c_N$ only for positive integer $N$ as a finite
product. There is an obvious prescription for analytical continuation of such
products, provided continuation of the items is known (it can be considered as
implied by the similar formula for integrals with the varying upper limit):
Let
\be
F(N) = \sum_{k = -\infty}^N f(k).
\ee
Then
\be
S(N) \equiv \sum_{k=1}^N f(k) = F(N) - F(0)
\ee
and, obviously, $F(0) - F(-N) = \sum_{k = 1-N}^0 f(k)$,  so that
\be
S(-N) \equiv F(-N) - F(0) = -\sum_{k=0}^{N-1} f(-k).
\ee
Exponentiation of this
formula gives the rule for the products. In the case of $c_N$ one can
treat factorials in (\ref{cnform}) as Gamma-functions,
\be
(2\pi)^{\frac{N(N-1)}{2}} c_N = \prod_{k=1}^N \Gamma(k),
\ee
and obtain:
\be
(2\pi)^{-\frac{N(N+1)}{2}} c_{-N} = \left( \prod_{k=0}^{N-1}
\Gamma(-k)\right)^{-1} = 0,
\label{cnneg}
\ee
because of the poles of $\Gamma$-functions.


\












\bigskip
