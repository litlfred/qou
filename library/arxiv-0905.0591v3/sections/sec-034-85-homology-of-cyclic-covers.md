---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-034-85-homology-of-cyclic-covers
section_title: "Homology of cyclic covers"
section_number: 8.5
pages: 28-29
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.972
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:cycliccovers}

Let $K\subset S^3$ be a knot. We denote by $H\mathrel{\mathop:}=H_1(S^3\setminus \nu K;\mathbb{Z}[t^{\pm 1}])$ its Alexander module. Given $n\in \mathbb{N}$ we denote by $L_n$ the  $n$--fold cyclic branched cover of $K$.
Recall that we have a canonical isomorphism $H/(t^n-1)\cong H_1(L_n)$.
Put differently, the Alexander module determines the homology of the branched covers. In the same vein,  the following formula due to Fox (\cite{Fo56} and see also \cite{Go78})
shows  that the Alexander polynomial determines the size of the homology of a branched cover:
\begin{equation}

| H_1(L_n )|=\left| \prod_{j=1}^{n-1} \Delta_K(e^{2\pi ij/n})\right|.
\end{equation}
Here we write $|H_1(L_n)|=0$ if $H_1(L_n)$ has positive rank. Gordon \cite{Go72} used this formula to study extensively the homology of the branched covers of a knot.
Gordon \cite[p.~366]{Go72} asked whether the non--zero values of the sequence $|H_1(L_n)|$ converge to infinity
if there exists a zero of the Alexander polynomial which is not a root of unity.

Given a multivariable polynomial $p\mathrel{\mathop:}=p(t_1,\dots,t_n)\in \mathbb{C}[t_1^{\pm 1},\dots,t_n^{\pm 1}]$ the Mahler measure is defined as
\[ m(p)=\exp \, \int_{\theta_1=0}^{1} \dots  \int_{\theta_n=0}^{1}\mbox{log} \left|p\big(e^{2\pi i \theta_1},\dots,e^{2\pi i \theta_1}\big) \right| \,d \theta_1 \dots d \theta_n.\]
Note that the integral  can be singular, but one can show that the integral always
converges. It is known (cf. e.g. \cite{SW02}) that an integral one variable polynomial $p$ always satisfies $m(p)\geq 1$, and it satisfies
$m(p)=1$ if and only if all zeroes of $p$ are roots of unity.


\begin{theorem}
Let $K$ be any knot, then
\[ \lim_{n\to \infty} \frac{1}{n}\mbox{log} |\mbox{Tor} \,H_1(L_n)|  = \log(m(\Delta_K(t))).\]
\end{theorem}

This theorem was proved for most cases by Gonz\'alez-Acu\~na and Short \cite{GS91}, the most general statement was proved by Silver and Williams \cite[Theorem~2.1]{SW02}. We also refer to \cite{Ri90} for a related result.
Note that by the above discussion this theorem in particular implies the affirmative answer to Gordon's question.

Silver and Williams also generalized this theorem to links (\cite[Theorem~2.1]{SW02}), relating the Mahler measure multivariable Alexander polynomial to the
homology growth of finite abelian covers of the link.
Finally in \cite[Section~3]{SW09c} these results are extended to the twisted case for certain representations
(e.g. integral representations). We refer to \cite[Section~3]{SW09c} for the precise formulations and to \cite[Section~5]{SW09c} for an interesting example.
