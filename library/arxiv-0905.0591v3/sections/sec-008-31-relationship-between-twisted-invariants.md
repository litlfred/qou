---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-008-31-relationship-between-twisted-invariants
section_title: "Relationship between twisted invariants"
section_number: 3.1
pages: 7-8
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.97
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
The following proposition is \cite[Theorem~4.7]{Tu01}.

\begin{proposition}\label{prop:deltataualpha}
Let $N$ be a 3--manifold with empty or toroidal boundary and let
$\alpha:\pi_1(N)\to \mbox{GL}(k,R[F])$  a  representation where $R$ is a Noetherian UFD and $F$ a free abelian group. If $\Delta_{N,i}^{\alpha} \ne 0$
for $i=0,1,2$, then
\[ \tau(N,{\alpha} )\doteq  \prod_{i=0}^2 \big(\Delta^{{\alpha}}_{N,i}\big)^{(-1)^{i+1}}.\]
\end{proposition}

The following is a mild extension of \cite[Proposition~2.5]{FK06}, \cite[Lemmas~6.2~and~6.3]{FK08a} and \cite[Theorem~6.7]{FK08a}.
Most of the ideas go back to work of Turaev (cf. e.g. \cite{Tu86} and \cite{Tu01}). The third statement is proved in \cite{DFJ10}.

\begin{proposition}\label{prop:deltatau}\label{prop:taudelta}
Let $N$ be a 3--manifold with empty or toroidal boundary,  $\psi:\pi_1(N)\to F$ a non--trivial homomorphism to a free abelian group $F$
and $\gamma:\pi_1(N)\to \mbox{GL}(k,R)$  a  representation where $R$ is a Noetherian UFD. Then the following hold:
\begin{enumerate}
\item $\Delta_{N,0}^{\gamma \otimes \psi} \ne 0$ and $\Delta_{N,i}^{\gamma \otimes \psi}=1$ for $i\geq 3$.
\item If $\mbox{rank}(\mbox{Im}\{\pi_1(N)\to F\})>1$, then $\Delta^{{\gamma \otimes \psi}}_{N,0} \doteq 1$.
\item If $\g$ is irreducible and if $\g$ restricted to $\ker(\psi)$ is non-trivial, then $\Delta^{{\gamma \otimes \psi}}_{N,0} \doteq 1$.
\item If $\Delta_{N,1}^{\gamma \otimes \psi} \ne 0$, then $\Delta_{N,2}^{\gamma \otimes \psi} \ne 0$.
\item If $N$ has non--empty boundary and if $\Delta_{N,1}^{\gamma \otimes \psi} \ne 0$, then $\Delta^{{\gamma \otimes \psi}}_{N,2} \doteq 1$.
\item If  $\mbox{rank}(\mbox{Im}\{\pi_1(N)\to F\})>1$ and if $\Delta_{N,1}^{\gamma \otimes \psi} \ne 0$, then $\Delta^{{\gamma \otimes \psi}}_{N,2}\doteq 1$.
\item We have $\Delta_{N,1}^{\gamma \otimes \psi}= 0$ if and only if
$ \tau(N,{\gamma \otimes \psi} )=0$.
\item If $\Delta_{N,1}^{\gamma \otimes \psi} \ne 0$, then
\[ \tau(N,{\gamma \otimes \psi} )\doteq  \prod_{i=0}^2 \big(\Delta^{{\gamma \otimes \psi}}_{N,i}\big)^{(-1)^{i+1}}.\]
\end{enumerate}
\end{proposition}

A few remarks regarding the equalities of Proposition \ref{prop:deltataualpha} and Proposition \ref{prop:deltatau} (8)  are in order:
\begin{enumerate}
\item Note that twisted Reidemeister torsion has in general a smaller indeterminacy than twisted Alexander polynomials.
In particular the equality
holds up to the indeterminacy of the twisted Alexander polynomials.
\item As pointed out in Section \ref{section:compdelta}, the twisted Alexander polynomials $\Delta^{\gamma\otimes \psi}_{N,i}$ can be computed from a presentation
of the fundamental group, whereas the computation of $\tau(N,\gamma \otimes \psi)$
requires in general an understanding of the CW--structure of $N$ (cf. Section \ref{section:comptau}). In particular
the equality of  Proposition \ref{prop:deltatau} (8) is often a faster method for computing $\tau(N,\gamma \otimes \psi)$ (at the price of a higher indeterminacy).
\item The twisted Alexander polynomial is only defined for representations over a Noetherian UFD, whereas the twisted Reidemeister torsion is defined for a finite dimensional representation over any commutative ring.
\item It is an immediate consequence of Proposition \ref{prop:deltatau} that $\tau(N,{\gamma \otimes \psi} )$ lies in $R[F]$, i.e. is a polynomial,
if $\mbox{rank}(\mbox{Im}\{\pi_1(N)\to F\})>1$.
\end{enumerate}

\begin{remark}
\begin{enumerate}
\item
Given a link $L\subset S^3$ and a representation $\gamma:\pi_1(S^3\setminus L)\to \mbox{GL}(k,R)$
Wada \cite{Wa94} introduced an invariant, which in this paragraph we refer to as $W(L,\gamma)$.
Wada's invariant is in many papers referred to as the twisted Alexander polynomial of a link.
Kitano \cite{Ki96} showed that $W(L,\gamma)$
agrees with the Reidemeister torsion $\tau(L,\gamma)$ (with the same indeterminacy). This can also be shown using the arguments of  Section \ref{section:comptau}.
In particular, in light of Proposition \ref{prop:deltatau} we see that $W({L,\gamma})\doteq \Delta_{L}^{\gamma}$ if $L$ has more than one component.
\item Lin's original definition \cite{Lin01} of the twisted Alexander polynomial of a knot uses `regular Seifert surfaces' and is rather different in character to the algebra--topological approach taken in the subsequent papers. The relation between the definitions of twisted Alexander polynomials given by Lin \cite{Lin01}, Jiang and Wang \cite{JW93} and Section \ref{section:twialex}
    is explained in \cite[Proposition~3.3]{JW93} and \cite[Section~4]{KL99a}.
\end{enumerate}
\end{remark}
