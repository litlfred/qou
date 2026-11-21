---
doc_id: arxiv-0801.3233v4
doc_title: "Twisted Deformation Quantization of Algebraic Varieties (Survey)"
section_id: sec-006-6-twisted-deformation-quantization
section_title: "Twisted Deformation Quantization"
section_number: 6
pages: 8-9
source_pdf: 0801.3233v4.pdf
source_sha256: d98f9d4a9ecb4c5e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 1.0
doc_brief: "Twisted Deformation Quantization of Algebraic Varieties (Survey) — Let X be a smooth algebraic variety over a ﬁeld of characteristic 0. We introduce the notion of twisted associative (resp."
---
Just as in the case of usual deformations, given a 
twisted (associative or Poisson) deformation $\bsym{\mcal{A}}$ 
of $\mcal{O}_X$, we can define the first order bracket 
$\{ -,- \}_{\bsym{\mcal{A}}}$ on $\mcal{O}_X$. The first order bracket is
invariant under twisted gauge equivalence.

Let $\bsym{\mcal{A}}$ be a twisted Poisson deformation, and 
let $\bsym{\mcal{B}}$ be a twisted associative deformation. We say 
that $\bsym{\mcal{B}}$ is a {\em twisted quantization} of
$\bsym{\mcal{A}}$ if 
\[ \{ -,- \}_{\bsym{\mcal{B}}} = \{ -,- \}_{\bsym{\mcal{A}}} . \]

The next theorem is influenced by ideas of Kontsevich (from 
\cite{Ko3} and private communications).

\begin{thm}[\cite{Ye5}]  \label{thm_new}
Let $\K$ be a field containing $\mbb{R}$, and let $X$ be a
smooth algebraic variety over $\K$.
There is a canonical bijection 
\[ \begin{aligned}
& \opn{tw{.}quant} : \frac{ \{ \tup{twisted Poisson deformations of 
$\mcal{O}_{X}$} \} }
{\tup{ twisted gauge equivalence}} \\
&   \hspace{3em} \iso \ 
\frac{ \{ \tup{twisted associative deformations of 
$\mcal{O}_X$} \} }{\tup{ twisted gauge equivalence}} ,
\end{aligned} \] 
called the {\em twisted quantization map}, which is a twisted quantization in
the sense above.
\end{thm} 

As before, by ``canonical'' we mean that the twisted quantization map
commutes with \'etale morphisms $X' \to X$.

The proof of Theorem \ref{thm_new} relies on a rather complicated
calculations involving Maurer-Cartan equations in cosimplicial DG Lie
algebras, and cosimplicial $2$-groupoids. See Appendices C and D. 

The results on pronilpotent gerbes from \cite{Ye6} tell us that 
when $\mrm{H}^1(X, \mcal{O}_{X}) = 0$ and 
$\mrm{H}^2(X, \mcal{O}_{X}) = 0$, there are no really twisted deformations. 
Thus Theorem \ref{thm_new} implies:

\begin{cor}  \label{cor_new}
Assume the cohomology groups 
$\mrm{H}^1(X, \mcal{O}_{X})$ and $\mrm{H}^2(X, \mcal{O}_{X})$ vanish.
Then the function $\opn{tw{.}quant}$ of the theorem gives a bijection
\[ \opn{quant} : \frac{ \{ \tup{Poisson deformations of 
$\mcal{O}_{X}$} \} }
{\tup{ gauge equivalence}} 
\iso
\frac{ \{ \tup{associative deformations of 
$\mcal{O}_X$} \} }{\tup{ gauge equivalence}} .
\] 








\end{cor} 

As we already mentioned, if $\mrm{H}^1(X, \mcal{T}_{X}) = 0$, then all
twisted Poisson deformations are sheaf theoretically trivial. 
Likewise, if $\mrm{H}^1(X, \mcal{D}_{X}) = 0$, then all
twisted associative deformations are sheaf theoretically trivial. 
Hence:

\begin{cor}  \label{cor_new3}
Assume the cohomology groups $\mrm{H}^1(X, \mcal{O}_{X})$,
$\mrm{H}^2(X, \mcal{O}_{X})$, \linebreak
$\mrm{H}^1(X, \mcal{T}_{X})$ and
$\mrm{H}^1(X, \mcal{D}_{X})$
vanish. Then the function $\opn{tw{.}quant}$ of the theorem gives a bijection
\[ \opn{quant} : \frac{ \{ \tup{formal Poisson brackets on 
$\mcal{O}_{X}[[\hbar]]$} \} }{\tup{ gauge equivalence}} 
\iso
\frac{ \{ \tup{star products on $\mcal{O}_X[[\hbar]]$} \} }
{\tup{ gauge equivalence}} .
 \] 









\end{cor} 

The conditions of Corollary \ref{cor_new3} are satisfied, for instance, when
$X = \mbf{P}^n_{\K}$ ($n$-dimensional projective space over $\K$). 

Let me finish this survey with a question. 
Given a variety $X$, with Poisson bracket $\{-,-\}_1$ on 
$\mcal{O}_X$, we can form the Poisson deformation 
$\mcal{A} := \mcal{O}_X[[\hbar]]$ with bracket $\hbar \{-,-\}_1$,
as in Example \ref{exa10}. 
By viewing $\mcal{A}$ as a twisted Poisson deformation
(cf.\ Example \ref{exa:20}), and applying
Theorem \ref{thm_new}, we get a twisted associative deformation 
$\bsym{\mcal{B}} := \opn{quant}(\mcal{A})$.

\begin{que}
Does there exist a variety $X$, with a symplectic
Poisson bracket $\{-,-\}_1$, such that the corresponding twisted
associative deformation $\bsym{\mcal{B}}$ is really twisted?
\end{que}

My feeling is that the answer is positive. 
And moreover, an example should be when $X$ is any Calabi-Yau surface,
and $\{-,-\}_1$ is any nonzero Poisson bracket on $X$.
It might be possible to settle this question with an explicit (yet very hard)
calculation, since there are explicit formulas for the twisted quantization
map.
