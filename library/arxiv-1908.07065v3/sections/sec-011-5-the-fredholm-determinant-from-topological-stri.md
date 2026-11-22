---
doc_id: arxiv-1908.07065v3
doc_title: "Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-011-5-the-fredholm-determinant-from-topological-stri
section_title: "The Fredholm determinant from topological string theory"
section_number: 5
pages: 29-30
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 1.0
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve of N = 2, SU(2) super Yang–Mills"
---
\label{tssst}


Let $\mO$ be an operator on $L^2(\IR)$ such that $\mO^{-1}$ is of trace class. Then, $\mO$ has a discrete spectrum $\{E_n\}_{n\geq 0}$, and its Fredholm determinant 

\be
\label{fdm} \Xi(E)={\rm det}\left(1-E \mO^{-1} \right) =\prod_{n\geq0}\left({1-{E \over E_n}}\right)
 \ee

is an entire function of $E$ whose zeros give the spectrum of $\mO$: $\Xi(E_n)=0$ (see e.g. \cite{simon-paper} for these and other properties of Fredholm determinants). 

The Fredholm determinant contains very rich information about the spectral properties of $\mO$. For example, the spectral traces, defined as

 \be\label{trdef} Z_\ell=\sum_{n \geq 0}{1\over E_n^\ell}, 
 \ee
 
can be computed by expanding the spectral determinant around $E=0$. Indeed, we have
 
  \be 
  \Xi(E)=\sum_{N\geq 0} (-E)^N Z(N,\hbar) 
  \ee
  
where

\be
\label{conjclasses}
Z(N, \hbar) =\sum_{\{ m_\ell \}} {}^{'}\prod_\ell   {(-1)^{(\ell-1)m_\ell } Z_\ell^{m_\ell} \over m_\ell! \ell^{m_\ell}},
\ee

and the $ {}^{'}$ means that the sum is over the integers $m_\ell$ satisfying the constraint

\be
\label{Ncons}
\sum_\ell \ell m_\ell=N.
\ee

From the quantities $Z(N, \hbar)$ (which were called {\it fermionic
  spectral traces} in \cite{ghm}) one can extract the conventional
spectral traces (\ref{trdef}).

Although Fredholm determinants are central objects in spectral theory,
it is difficult to obtain explicit expressions for them. It is easy to
show (see for instance \cite{lst}) that the inverse of the modified
Mathieu operator \eqref{eq:schrodinger} is of trace class. Therefore,
the Fredholm determinant is well-defined, and it is an interesting
question to find an explicit, closed form expression for this
quantity.

In recent years it was discovered \cite{km, hw, cgm8, ghm, cgm} that, by
using topological string tools, it is possible to obtain explicitly
expression for Fredholm determinants of operators arising in the
context to quantum mirror curves.  We will refer to this relationship
as the TS/ST correspondence. As explained in section~\ref{deri}, the
modified Mathieu operator \eqref{eq:schrodinger} can be related, upon
a suitable limiting procedure, to the quantum mirror curve of local
$\IF_0$. Therefore we can study \eqref{fdm} within the context of
topological string theory and in particular, by using \cite{ghm, gm3},
we can deduce an explicit, closed form expression for the Fredholm
determinant of the modified Mathieu operator.  We will first state the
main result and then explain how to derive it within topological
string theory. We also present several independent tests of our
result, including an interesting connection to the TBA system of
\cite{post-zamo}.
