---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-037-91-definitions-and-basic-properties
section_title: "Definitions and basic properties"
section_number: 9.1
pages: 29-30
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.89
latex_coverage_ratio: 0.95
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:generalprop}

Let $X$ be a  CW--complex  with finitely many cells in each dimension.
Assume we are given a  non--trivial homomorphism $\psi:\pi_1(X)\to F$ to a torsion--free abelian group and a  representation
$\gamma:\pi_1(X)\to \mbox{GL}(k,R)$ where $R$ is a Noetherian UFD.
As in Section \ref{section:twialex} we can define the twisted Alexander modules
\[ H_i(X;R[F]^k)=H_i(C_*(\tilde{X};\mathbb{Z})\otimes_{\mathbb{Z}[\pi_1(X)]} R[F]^k)\]
where $\pi_1(X)$ acts on $C_*(\tilde{X};\mathbb{Z})$ by deck transformations and on $R[F]^k$ by $\gamma\otimes \psi$.
These modules are finitely presented and we can therefore define the twisted Alexander polynomial $\Delta^{\gamma\otimes \psi}_{X,i}\in R[F]$
to be the order of the $R[F]$--module $H_i(X;R[F]^k)$.
Note that twisted Alexander polynomials are homotopy invariants, in  particular given any manifold homotopy equivalent to a finite CW--complex we can define the twisted Alexander polynomials $\Delta^{\gamma\otimes \psi}_{X,i}\in R[F]$.

Let $G$ be a finitely presented group and $X=K(G,1)$ its  Eilenberg--Maclane space.
Given  a  non--trivial homomorphism $\psi:G\to F$ to a torsion--free abelian group and a  representation
$\gamma:G\to \mbox{GL}(k,R)$ where $R$ is a Noetherian UFD we define
\[ \Delta^{\gamma\otimes \psi}_{G,i}=\Delta^{\gamma\otimes \psi}_{K(G,1),i}.\]


\begin{remark}
\begin{enumerate}
\item For $i=0,1$ the Alexander polynomials $\Delta^{\gamma\otimes \psi}_{X,i}\in R[F]$ can be computed using Fox calculus
as in Section \ref{section:compdelta}.
\item Note that unless the Euler characteristic of $X$ vanishes we can not define the Reidemeister torsion corresponding to $(X,\psi,\gamma)$.
\item Most of the results of Section \ref{section:basics} do not hold in the general context.
The only results which do generalize are Proposition \ref{prop:taudelta} (2), Lemma \ref{lem:equ:rep} and Theorem \ref{thm:shapiro}.
\item
Note that given a finitely presented group $G$ and $\psi$, $\gamma$ as above Wada \cite{Wa94}
introduced an invariant which we refer to as $W(G,\gamma\otimes \psi)\in Q(R[F])$.
Using \cite[Lemma~4.11]{Tu01} one can  show that
\[ W(G,\gamma \otimes \psi) \doteq \frac{\Delta^{\gamma\otimes \psi}_{G,1} }{\Delta^{\gamma\otimes \psi}_{G,0}}.\]



In the literature Wada's invariant is often referred to as the  twisted Alexander polynomial of a group.
\end{enumerate}
\end{remark}
