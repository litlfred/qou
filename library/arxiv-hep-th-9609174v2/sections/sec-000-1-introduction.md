---
doc_id: arxiv-hep-th-9609174v2
doc_title: "arXiv:hep-th/9609174v2 23 Sep 1996"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-4
source_pdf: 9609174v2.pdf
source_sha256: 87885f4d03661f26
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.997
doc_brief: "arXiv:hep-th/9609174v2 23 Sep 1996 — We prove the universality of correlation functions of chiral unitary and unitary ensembles of ran- dom matrices in the microscopic limit."
---
Consider a four-dimensional gauge theory coupled to fermions
in given representations of the gauge group, and with given global
(and possibly spontaneously broken) flavor symmetries. 
In the chiral limit, the associated Dirac operator 
${\rm i} D\!\llap{/}$ anticommutes with $\gamma_5$,
\begin{equation}
\{{\rm i} D\!\llap{/},\gamma_5\} ~=~ 0 ~.
\end{equation}
This means that the associated eigenvalues of ${\rm i} D\!\llap{/}$,
defined by
${\rm i} D\!\llap{/}\,\phi_n = \lambda_n\phi_n$ 
appear symmetrically around zero:
$\pm\lambda_n$. The corresponding eigenfunctions are, for $\lambda_n
\neq 0$, $\phi_n$ and $\gamma_5\phi_n$. The accumulation of eigenvalues
near $\lambda = 0$ determines whether or not chiral symmetry is
spontaneously broken through the formation of a chiral condensate 
\cite{BC}. The study of the Dirac operator spectrum near $\lambda = 0$
is thus of fundamental importance for our understanding of chiral
symmetry breaking in gauge theories. For example, for QCD with $N_f$
flavors it is expected to lead to the conventional
${\rm SU}(N_f)_{\rm L}\times 
{\rm SU}(N_f)_{\rm R}\rightarrow{\rm SU}(N_f)_{\rm V}
$ scenario, with all its
implications in terms of low-energy effective Lagrangians.

\vspace{12pt}\noindent
In a series of papers \cite{V93,V94,V96}, 
Verbaarschot and collaborators
have added substantial new insight to this issue. Their central
assertion is that the spectral density of the Dirac operator very close
to the origin $\lambda = 0$ should be {\em universal},
depending only on the symmetries in question. One startling consequence
of this conjecture is that the spectral density of the Dirac operator
near the origin need not be computed in the gauge theory at all, but
can be extracted from much simpler random matrix theories.
The pertinent
random matrix ensemble is determined by symmetry arguments alone.
To find universal features of the Dirac spectrum near the origin,
it is essential to first consider the problem in a finite volume $V_4$,
corresponding in matrix-model terms to finite-size matrices, and then
magnify the spectrum near the origin at a scale of order $1/V_4$. 
The usual spectral density $\rho(\lambda)$ 
is defined by the following average 
over gauge field configurations:
\begin{equation}
\rho(\lambda) = \sum_n \langle\delta(\lambda - \lambda_n)\rangle ~.
\end{equation}
By the Banks-Casher relation\footnote{
Applied na\"{\i}vely here, ignoring
the subtlety of regularization.} \cite{BC}
(taking here the limit $V_4 \rightarrow \infty$),
\begin{eqnarray}
\langle \bar{\psi}\psi\rangle =\frac{1}{V_4}
\lim_{m\rightarrow 0}2m \int_0^{\infty}
\d\lambda \frac{\rho(\lambda)}{\lambda^2 + m^2} 
= \frac{\pi\rho(0)}{V_4} ~, 
\label{BC}
\end{eqnarray}
this spectral density, evaluated at the origin, is directly related to
the appearance of a chiral condensate. 
It follows that the average spacing
between eigenvalues becomes roughly constant near 
$\lambda = 0$ \cite{LS},
\begin{equation}
\Delta \lambda \sim \frac{\pi}{V_{4}\langle\bar{\psi}\psi\rangle} ~.
\end{equation}
Magnifying $\rho(\lambda)$ near
$\lambda = 0$ according to the prescription given above
thus entails the introduction of an associated 
{\em microscopic} spectral
density $\rho_{\rm S}(\lambda)$, which is defined by \cite{V93}
\begin{equation}
\rho_{\rm S}(\lambda) ~=~ \lim_{V_{4}\rightarrow\infty} \frac{1}{V_4}
\rho\left(\frac{\lambda}
{V_4}\right) ~.
\end{equation}
The precise statement is that this microscopic spectral
density should be a universal function.
The most compelling
evidence comes from the fact that the microscopic spectral
density defined as above, and evaluated in a particular random matrix
theory, exactly reproduces the Leutwyler-Smilga spectral sum rules
\cite{LS} and appropriate generalizations \cite{SV}.

\vspace{12pt}\noindent
To understand the significance of this universality conjecture, let us
for convenience first
focus on one example, that of QCD with $N_f$ massless fermions in the
fundamental representation. As
explained in refs.~\cite{V93},
the relevant matrix model partition function
is given by a chiral unitary ensemble of the form
\begin{equation}
Z_{\chi {\rm UE}} = \int 
\d W\, {\rm det}^{N_f}\left(
\begin{array}{cc}
0&W^\dagger\\
W&0
\end{array}\right)\, \e^{-N{\rm tr}\, V(W^{\dagger}W)} ~.
\end{equation}
Here only symmetry arguments alone
have selected the integration to be over complex $N\times N$
matrices, and the Dirac
operator structure is encoded in the determinant.
But such symmetry arguments
alone place no restrictions on the form of $V(\lambda)$,
which appears in the exponent. 
If indeed symmetry arguments alone should determine the 
microscopic spectral density of QCD from this matrix ensemble, then any
reasonable choice of $V(\lambda)$ should give the same result for 
$\rho_{\rm S}(\lambda)$.
This universality argument, if correct, 
allows us to evaluate the integral
with a function $V(\lambda)$ of our own choice. 
Some hints supporting this universality 
had been found in refs.~\cite{BHZ}.
Clearly, the most 
convenient choice in to make the matrix integral Gaussian except
for the determinant factor in front. This is the choice made in 
refs.~\cite{V93}.

\vspace{12pt}\noindent
It is important to separate the question of universality
of the spectral density of the Dirac operator close to 
the origin into two parts. 
The first concerns the crucial jump from the $d$-dimensional
gauge field integrations to the framework of zero-dimensional matrix 
models with similar symmetries. 
The second step concerns the conjecture about
the universality of the microscopic spectral density
{\em within the framework of matrix models}.
The purpose of this paper is to prove the latter of these
universality conjectures.
The question of whether the universality
extends all the way from zero-dimensional large-$N$ matrix models to
full-fledged quantum field theories such as QCD will of course remain
unproven. But we shall show, within the context of large-$N$ matrix
models, under what conditions the microscopic spectral density and 
higher correlation functions are universal. 
This is a major step towards
understanding the original issue, 
which concerns the possible universality
of also the Dirac operator spectrum near $\lambda = 0$.

\vspace{12pt}\noindent
This paper is organized as follows.
In section 2 we prove a theorem for the asymptotic behavior
of generic orthogonal polynomials over a semi-infinite range.
By making use of this theorem, we compute the associated
universal form of the microscopic spectral density as well as
all higher order correlation functions in the same limit.
This universality class is of relevance for four-dimensional
${\rm SU}(N_c \! \geq \! 3)$ gauge
theories with fermions in the fundamental representation.
In section 3 we repeat the analysis for a class of orthogonal
polynomials over an infinite range. This case 
is considered to be relevant
for three-dimensional ${\rm SU}(N_c \! \geq \! 3)$ 
gauge theories with an even number
of fermions in the fundamental representation. 
We conclude in section 4 with a discussion 
about the possible relation between the
chiral-flavor (or parity-flavor) symmetry breaking in gauge theories
and the now established universality of random matrices
in the microscopic limit.

\setcounter{equation}{0}
