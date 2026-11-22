---
doc_id: arxiv-0801.3233v4
doc_title: "Twisted Deformation Quantization of Algebraic Varieties (Survey)"
section_id: sec-004-4-deformation-quantization
section_title: "Deformation Quantization"
section_number: 4
pages: 5-6
source_pdf: 0801.3233v4.pdf
source_sha256: d98f9d4a9ecb4c5e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.987
latex_coverage_ratio: 0.97
doc_brief: "Twisted Deformation Quantization of Algebraic Varieties (Survey) — Let X be a smooth algebraic variety over a ﬁeld of characteristic 0. We introduce the notion of twisted associative (resp."
---
Kontsevich \cite{Ko1} proved that any Poisson deformation of a real 
$\mrm{C}^{\infty}$ manifold $X$ can be canonically quantized. 
In this section we present an algebraic version of this result. But first a
definition. 

\begin{dfn}
Let $\mcal{A}$ be a Poisson deformation of $\mcal{O}_X$. 
A {\em quantization} of $\mcal{A}$ is an 
associative deformation $\mcal{B}$, such that the first order
brackets satisfy
\[ \{ -,- \}_{\mcal{B}} = \{ -,- \}_{\mcal{A}} . \]
\end{dfn} 

Recalling Example 2.2,
we see that this definition captures the essence
of deformation quantization, namely quantizing a Poisson bracket on 
$\mcal{O}_X$.

\begin{thm}[\cite{Ye1}] \label{thm1} 
Let $\K$ be a field containing $\mbb{R}$, and let $X$ be a smooth
affine algebraic variety over $\K$.
There is a canonical bijection
\[ \opn{quant} : \frac{ \{ \tup{formal Poisson brackets on 
$\mcal{O}_{X}[[\hbar]]$} \} }{\tup{ gauge equivalence}} 
\iso
\frac{ \{ \tup{star products on $\mcal{O}_X[[\hbar]]$} \} }
{\tup{ gauge equivalence}} .
 \] 








which is a quantization as defined above. 
\end{thm} 

By ``canonical'' we mean that this quantization map 
commutes with \'etale morphisms $X' \to X$ (and in particular with
automorphisms of $X$).

Actually our result in \cite{Ye1} is stronger -- it holds for a wider
class of varieties, not just affine varieties. 
However all these cases are subsumed in Corollary \ref{cor_new3} below. 

On the other hand, it might be good to remark that when writing \cite{Ye1} we
did not know Theorem \ref{thm:diff}, and hence we only considered differential
star products in that paper. Now we know that there is no difference (up to
gauge equivalence), so Theorem \ref{thm1} is correct as stated. In the context
of complex manifolds  this issue is still open: it is not known if every star
product is gauge equivalent to a differential one! See \cite{KS2}.

It is important to note that even the affine case of Theorem \ref{thm1} is a
``global result''. In this context ``local'' means a sufficiently small affine
open set $U \subset X$ that admits an \'etale coordinate system, namely an 
\'etale morphism $U \to \mbf{A}^n_{\K}$. This is totally analogous to the case
of $\mrm{C}^{\infty}$ manifolds studied by Kontsevich, where ``local'' meant an
open set in the manifold $\mbf{A}^n_{\R} = \R^n$.

Theorem \ref{thm1} is a consequence of the following more general
result.

\begin{thm}[\cite{Ye1}] \label{thm2} 
Let $\K$ be a field containing $\mbb{R}$, and let $X$ be a
smooth algebraic variety over $\K$. There is a diagram 
\[ \UseTips \xymatrix @C=5ex @R=3.5ex {
\mcal{T}^{}_{\mrm{poly}, X} 
\ar[d]
& \mcal{D}^{}_{\mrm{poly}, X}
\ar[d] \\
\opn{Mix}_{\bsym{U}}(\mcal{T}^{}_{\mrm{poly}, X} ) 
\ar[r]^{\Psi_{\bsym{\sigma}}}
&
\opn{Mix}_{\bsym{U}}(\mcal{D}^{}_{\mrm{poly}, X} )
} \] 
where:
\begin{itemize}
\item $\opn{Mix}_{\bsym{U}}(\mcal{T}^{}_{\mrm{poly}, X})$
and
$\opn{Mix}_{\bsym{U}}(\mcal{D}^{}_{\mrm{poly}, X})$
are sheaves of DG Lie algebras on $X$, called {\em mixed
resolutions};
\item the vertical arrows are DG Lie algebra quasi-isomorphisms;
\item and the horizontal arrow $\Psi_{\bsym{\sigma}}$
is an $\mrm{L}_{\infty}$ quasi-isomorphism. 
\end{itemize}
\end{thm}

The mixed resolutions combine the {\em commutative \v{C}ech 
resolution} associated to a sufficiently refined affine open covering $\bsym{U}$
of $X$, and the {\em Grothendieck sheaf of jets}. 
An {\em $\mrm{L}_{\infty}$ quasi-isomorphism} is a
generalization of a DG Lie algebra quasi-iso\-mor\-phism. 
The $\mrm{L}_{\infty}$ quasi-isomorphism $\Psi_{\bsym{\sigma}}$ depends on some
choices; but the dependence on these choices and on the covering 
$\bsym{U}$ disappears in homotopy. 
Theorem \ref{thm2} is proved using the {\em Formality Theorem}
of Kontsevich \cite{Ko1} and {\em formal geometry}.
More on the proof of Theorem \ref{thm2} in Appendices B and C.
A somewhat different approach to Theorem \ref{thm2} can be found in Van den
Bergh's paper \cite{VdB}.
