---
doc_id: arxiv-0801.3233v4
doc_title: "Twisted Deformation Quantization of Algebraic Varieties (Survey)"
section_id: sec-001-1-some-background-on-deformation-quantization
section_title: "Some background on Deformation Quantization"
section_number: 1
pages: 2-3
source_pdf: 0801.3233v4.pdf
source_sha256: d98f9d4a9ecb4c5e
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.979
doc_brief: "Twisted Deformation Quantization of Algebraic Varieties (Survey) — Let X be a smooth algebraic variety over a ﬁeld of characteristic 0. We introduce the notion of twisted associative (resp."
---
Throughout $\K$ is a field of characteristic $0$.

Let $C$ be a commutative $\K$-algebra. 
Recall that a {\em Poisson bracket} on $C$ is a 
$\K$-bilinear function
\[ \{-,-\} : C \times C \to C \]
which makes $C$ into a Lie algebra, and is a biderivation (i.e.\ 
a derivation in each argument). 
The pair $\bigl( C, \{-,-\} \bigr)$ is called a Poisson algebra. 

Poisson algebras arise in several ways, e.g.\ classical Hamiltonian
mechanics, or Lie theory.

Let $\K[[\hbar]]$ be the ring of formal power series in the
variable $\hbar$. And let $C[[\hbar]]$ be the set of formal power series with
coefficients in $C$, which we view only as a 
$\K[[\hbar]]$-module. 
A {\em star product} on $C[[\hbar]]$ is a $\K[[\hbar]]$-bilinear function
\[ \star : C[[\hbar]] \times C[[\hbar]] \to C[[\hbar]]  \]
which makes $C[[\hbar]]$ into an associative 
$\K[[\hbar]]$-algebra, with unit $1 \in C$, and  such that 
\[ f \star g \equiv f g \ \opn{mod}\ \hbar \]
for any $g, f \in C$.

Note that the star product $\star$ can be expanded into a power series as
follows: there is a sequence $\{ \omega_j \}_{j \geq 1}$ of $\K$-bilinear
functions $\omega_j : C \times C \to C$, such that 
\begin{equation} \label{eqn:omega2}
f \star g := f g + 
\sum_{j = 1}^{\infty} \omega_j(f, g) \hbar^j
\end{equation}
for $f, g \in C$. The conditions that $\star$ is associative and unital place
certain constraints on the sequence $\{ \omega_j \}_{j \geq 1}$.

\begin{exa} \label{exa3}
Suppose $\star$ is a star product on  $C[[\hbar]]$. Given $f, g \in C$, we know
that 
\[ f \star g - g \star f \equiv 0 \ \opn{mod}\ \hbar . \]
Hence there is a unique element 
$\{ f, g \}_{\star} \in C$
such that 
\[ \smfrac{1}{2 \hbar} \bigl( f \star g - g \star f \bigr)
\equiv \{ f, g \}_{\star}  \ \opn{mod}\ \hbar . \]
It is quite easy to show that $\{ -,- \}_{\star}$ is a Poisson
bracket on $C$. We call it the {\em first order bracket}
of $\star$. 
\end{exa}

Deformation quantization seeks to reverse Example \ref{exa3}.

\begin{dfn}
Given a Poisson bracket $\{ -,- \}$ on the algebra $C$, a 
{\em deformation quantization} of $\{ -,- \}$ is a star product $\star$ on
$C[[\hbar]]$ whose first order bracket is $\{ -,- \}$.
\end{dfn}

In physics $\hbar$ is the {\em Planck constant}. For a
quantum
phenomenon depending on $\hbar$, the limit as $\hbar \to 0$ is thought
of the as the classical limit of this phenomenon.

The original idea by the physicists Flato et.\ al.\ (\cite{BFFLS},
1978) was that deformation quantization should model the transition
from classical Hamiltonian mechanics to quantum mechanics.
Special cases (like the Moyal product) were known. The problem 
arose: {\em does any Poisson bracket admit a 
deformation quantization}?

For a symplectic manifold $X$ and $C = \mrm{C}^{\infty}(X)$ 
the problem was solved by De Wilde and Lecomte  (\cite{DL}, 1983). 
A more geometric solution was discovered by Fedosov (\cite{Fe},
1994). The general case, i.e.\ $C = \mrm{C}^{\infty}(X)$ for a 
Poisson manifold $X$, was solved by Kontsevich  (\cite{Ko1}, 1997).
See surveys in the book \cite{CKTB}.

\begin{rem} \label{rem:parameter}
The deformations considered in this paper are parameterized by the algebra 
$\K[[\hbar]]$. It is possible to replace $\K[[\hbar]]$ with any other noetherian
complete local commutative $\K$-algebra $R$, with maximal ideal $\m$, such that
$R / \m = \K$. Instead of $C[[\hbar]]$ we take the complete tensor product 
$R \hatotimes{\K} C$, with its obvious augmentation to $C$.
All results will remain valid. 
\end{rem}
