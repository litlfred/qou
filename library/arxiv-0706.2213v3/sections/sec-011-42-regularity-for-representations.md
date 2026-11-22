---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-011-42-regularity-for-representations
section_title: "Regularity for representations"
section_number: 4.2
pages: 14-14
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
toc_source: outline
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 1.0
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
In this subsection, we briefly review two notions of regularity {(see~\cite{Heu:2003},~\cite{Porti:1997} and~\cite{JDFibre})}. In the sequel $K \subset S^3$ denotes an oriented knot. 

 



Observe that for any representation $\rho$, $\dim H_1^\rho(E_K)$ is always greater or equal to $1$. We say that $\rho \in R^\mathrm{irr}(\Pi(K); \SL)$ is \emph{regular} if $\dim H_1^\rho(E_K) = 1$. This notion is invariant by conjugation and thus it is well defined for irreducible characters.

\begin{example}
For the trefoil knot and for the figure eight knot, one can prove that each irreducible representation of its group in $\SL$ is regular (see~\cite{JDFourier} and~\cite{Porti:1997}). 
\end{example}

Note that for a regular representation $\rho\colon \Pi(K) \to \SL$, we have $$\dim H_1^\rho(E_K) = 1, \; \dim H_2^\rho(E_K) = 1 \text{ and } H_j^\rho(E_K) = 0 \text{ for all } j \ne 1, 2.$$ 

Let $\gamma$ be a simple closed unoriented curve in $\bord E_K$. Among irreducible representations we focus on the $\gamma$-regular ones. We say that an irreducible representation $\rho : \Pi(K) \to \SL$ is \emph{$\gamma$-regular}, if (see~\cite[Definition 3.21]{Porti:1997}):
\begin{enumerate}
  \item the inclusion $\iota \colon \gamma \hookrightarrow E_K$ induces a \emph{surjective} map $$\iota_* \colon H^\rho_1(\gamma) \to H^\rho_1(E_K),$$
  \item if $\tr(\rho(\pi_1(\bord E_K))) \subset \{\pm 2\}$, then $\rho(\gamma) \ne \pm \I$.
\end{enumerate} 
It is easy to see that this notion is invariant by conjugation, thus the notion of $\gamma$-regularity is well-defined for irreducible characters. Also observe that a $\gamma$-regular representation is necessarily regular (the converse is false in general for an arbitrary curve). 


\begin{example}\label{ExReg}
For the trefoil knot, all irreducible representations of its group in $\SL$ are $\lambda$-regular (see~\cite{JDFourier}).

For the figure eight knot, one can prove that each irreducible representation of its group in $\SL$ is $\lambda$-regular \emph{except} two.


\end{example}

We close this section with an important fact concerning hyperbolic knots.
\begin{fact}[\cite{Porti:1997}]\label{holonomy}
Let $K$ be a hyperbolic knot and 
consider the holonomy representation $\rho_0$ associated to the complete hyperbolic structure. 
Let $\gamma$ be any simple closed curve in the boundary of $E_K$ such that $\rho_0(\gamma) \ne \pm \I$, then $\rho_0$ is $\gamma$-regular.
\end{fact}

In particular, for a hyperbolic knot the holonomy representation $\rho_0$ is always $\mu$-regular and $\lambda$-regular.

Applying  \cite[Proposition 3.26]{Porti:1997} to a hyperbolic knot exterior $E_K$,  
we obtain that for any simple closed curve $\gamma$, irreducible and non-$\gamma$-regular characters are contained in the set of zeros of the differential of the trace--function $I_{\gamma}$. 

\begin{remark}
Since the trace--function $I_{\gamma}$ is a regular function 
on the character variety,
the set of irreducible and non-$\gamma$-regular characters is discrete 
on the components where $I_{\gamma}$ is nonconstant.
\end{remark}

If $K$ is a hyperbolic knot, then the character of a complete holonomy representation is contained in a $1$-dimensional irreducible component $X_0(\Pi(K))$ of $X(\Pi(K))$, which satisfies the following condition: if a simple closed curve $\gamma$ in $\partial E_K$ represents any nontrivial element of $\Pi(K)$ then the trace--function $I_{\gamma}$ is nonconstant on $X_0(\Pi(K))$ (see \cite[Corollary 4.5.2]{HandBookGT}).
In particular, irreducible characters near the character of a complete holonomy representation
are $\mu$-regular and $\lambda$-regular.
