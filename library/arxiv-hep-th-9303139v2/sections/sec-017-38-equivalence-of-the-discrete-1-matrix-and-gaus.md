---
doc_id: arxiv-hep-th-9303139v2
doc_title: "arXiv:hep-th/9303139v2 5 Apr 1993"
section_id: sec-017-38-equivalence-of-the-discrete-1-matrix-and-gaus
section_title: "Equivalence of the discrete 1-matrix and Gaussian Kontsevich models"
section_number: 3.8
pages: 66-68
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.939
doc_brief: "arXiv:hep-th/9303139v2 5 Apr 1993 — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
Let us take the ordinary 1-matrix model with the $local$ measure $d\mu_h =
e^{U(h)}dh $ to be the scalar-product model, considered in
the previous subsection and take Miwa parametrization with upper signs and
with $r_k =
-\frac{1}{2}\delta_{k,2}$ (as we did in the section 2.6). Then $\hat V(h) =
\sum_k r_kh^k = -\frac{h^2}{2} = \frac{(ih)^2}{2}$.
The relevant orthogonal polinomials $\hat Q$ are just Hermite
polinomials of $imaginary$ argument:\footnote{
Note that this system of functions $\varphi_k = i^{-k}{\rm He}_k(ih)$
looks like $\varphi_0 = 1,\
\varphi_1 = h,\ \varphi_2 = h^2+1, \ldots$, and does not resemble any set of
orthogonal polinomials with a local measure (for example the product
$\varphi_0\cdot\varphi_2 = h^2+1$ may seem positive definite, this being
inconsistent with orthogonality requirement $\langle
\varphi_0\mid\varphi_2\rangle = 0$). The thing is that integration
at the l.h.s. of eq.(\ref{1mamoidgako}) is well defined only along the
imaginary axis, while integrals along the real axis are understood as
analytical continuation.
} $Q_k^{\{-\frac{h^2}{2}dh\}} = i^{-k}{\rm He}_k(ih) = h^k + \ldots$. These
polinomials possess an integral representation (\ref{hepo}):
\be
i^{1-k}{\rm He}_{k-1}(ih) =
\frac{1}{\sqrt{2\pi}} e^{-\frac{h^2}{2}}\int x^{k-1}
e^{-\frac{x^2}{2} + xh} dx  \stackrel{(\ref{varphiko})}{=}
\varphi_k^{\{\frac{x^2}{2}\}}(h).
\ee
Using (\ref{reduhv}) and (\ref{KIev"N}) we obtain a remarkable relation
between the two matrix models:
\be
\frac{Z_N\{t_0 = 0; t_k = -\frac{1}{k}{\rm tr}\Lambda ^{-k} +
\frac{1}{2}\delta_{k,2}\}}
{Z_N\{t_k = \frac{1}{2}\delta_{k,2}\}} =
\frac{\int_{N\times N} dH e^{\sum_{k=0}^{\infty} t_k {\rm Tr}
H^k}}{\int_{N\times N} dH e^{\frac{1}{2}H^2}} = \nn \\
= \frac{e^{-{\rm tr}\frac{\Lambda ^2}{2}}}
{(2\pi)^{\frac{n^2}{2}}({\rm det}\Lambda )^N}
\int_{n\times n}  dX ({\rm det}X)^N e^{-{\rm tr}\frac{X^2}{2} + \Lambda X}
= {\cal Z}_{\frac{X^2}{2}}\{N,t\},
\label{1mamoidgako}
\ee
where ${Z_N\{t_k = \frac{1}{2}\delta_{k,2}\}} = (-2\pi)^{\frac{N^2}{2}}c_N$.
This relation can be also regarded as an identity
\be
\frac{\int_{N\times N}dH e^{\frac{1}{2}{\rm Tr}H^2} Det(\Lambda \otimes I-
I\otimes
H)}{ \int_{N\times N}dH e^{\frac{1}{2}{\rm Tr}H^2}} =   \nn \\
= \frac{\int_{n\times n}dX e^{-\frac{1}{2}{\rm tr}X^2} {\rm
det}^N(X+\Lambda )}{\int_{n\times n}dX e^{-\frac{1}{2}{\rm tr}X^2}},
\ee
valid for any $\Lambda$.
Note that integrals are of differents sizes: $N\times N$ at the l.h.s. and
$n\times n$ at the r.h.s. While $N$-dependence is explicit at both sides of
the equation, the $n$-dependence at the l.h.s. enters only implicitly: through
the allowed domain of variation of variables
$t_k = -\frac{1}{k}{\rm tr}\Lambda ^{-k} + \frac{1}{2}\delta_{k,2}$.
(This can serve as an illustration to the general statement that the shape of
Kontsevich partition function ${\cal Z}_V$, considered as a function of $T$'s
rather than $ L$ or $\Lambda $, is independent of the matrix size $n$.)
Identity (\ref{1mamoidgako}) was anticipated
from the study of Ward identites for the
Gaussian Kontsevich model in \cite{ChMa} (see eq.
(2.53)

in the section 2.6 above),
and it was derived in the present form in ref.\cite{Toda}.

Eq.(\ref{1mamoidgako}) can be used to perfrom analytical continuation in $N$
and define what is $Z_N$ for $N$, which are not positive integers. Since $c_N
= 0$ for all {\it negative} integers (see eq.(\ref{cnneg}) below), the same is
true for $Z_N$. In the next section 4 we shall see that it is characteristic
property of $\tau$-functions of {\it forced} hierarchies.
