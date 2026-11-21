---
doc_id: arxiv-0706.2213v3
doc_title: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS"
section_id: sec-012-43-review-on-the-nonabelian-reidemeister-torsion
section_title: "Review on the non–abelian Reidemeister torsion for knot exteriors"
section_number: 4.3
pages: 14-16
source_pdf: 0706.2213v3.pdf
source_sha256: 75dd29acc9e34bda
toc_source: outline
text_source: latex
latex_prose_ratio: 0.916
latex_coverage_ratio: 0.991
doc_brief: "NON–ABELIAN REIDEMEISTER TORSION FOR TWIST KNOTS — This paper gives an explicit formula for the SL 2(C)−non–abelian Reidemeister torsion as deﬁned in [Dub06] in the case of twist knots."
---
\label{Torsion}
This subsection gives a detailed review of the constructions made in~\cite[Section~6]{JDFourier}. In particular, we shall explain how to construct distinguished bases for the twisted homology groups of knot exteriors. 


\subsubsection{Canonical homology orientation of knot exteriors}
We equip the exterior of $K$ with its \emph{canonical homology orientation} defined as follows (see~\cite[Section V.3]{Turaev:2002}). We have 
$$H_*(E_K; \IR) = H_0(E_K; \IR) \oplus H_1(E_K; \IR)$$ 
and we base this $\IR$-vector space with $\{ \lbrack \! \lbrack pt \rbrack \! \rbrack, \lbrack \! \lbrack \mu \rbrack \! \rbrack\}$. Here $\lbrack \! \lbrack pt \rbrack \! \rbrack$ is the homology class of a point, and $\lbrack \! \lbrack \mu \rbrack \! \rbrack$ is the homology class of the meridian $\mu$ of $K$. This reference basis of $H_*(E_K; \IR)$ induces the so--called canonical homology orientation of $E_K$. In the sequel, we let $\mathfrak{o}$ denote the canonical homology orientation of $E_K$.


\subsubsection{How to construct natural bases of the twisted homology}

Let $\rho$ be a regular $\SL$-representation of $\Pi(K)$ and {\emph{fix}} a generator $P^\rho$ of $H_0^\rho(\bord E_K)$ (i.e. $P^\rho$ is an element in $\sll$ such that $Ad_{\rho(g)}(P^\rho) = P^\rho$ for all $g \in \pi_1(\bord E_K)$).  

The canonical inclusion $i\colon \bord E_K \to E_K$ induces {(see~\cite[Corollary 3.23]{Porti:1997})} an isomorphism $i_*\colon H_2^\rho(\bord E_K) \to H_2^\rho(E_K)$. Moreover, one can prove that {(see~\cite[Proposition 3.18]{Porti:1997})}
$$H_2^\rho(\bord E_K) \cong H_2(\bord E_K; \ZZ) \otimes \CC.$$
 More precisely, let $\lbrack \! \lbrack \bord E_K \rbrack \! \rbrack \in H_2(\bord E_K; \ZZ)$ be the fundamental class induced by the orientation of $\bord E_K$, one has $H_2^\rho(\bord E_K) = \CC\left[\lbrack \! \lbrack \bord E_K \rbrack \! \rbrack \otimes P^\rho\right]$.

 The \emph{reference generator} of $H_2^\rho(E_K)$ is defined by 
\begin{equation}\label{EQ:Defh2}
h_{(2)}^\rho 
= i_*([\lbrack \! \lbrack \bord E_K \rbrack \! \rbrack \otimes P^\rho]).
\end{equation}

Let $\rho$ be a $\lambda$-regular representation of $\Pi(K)$. The \emph{reference generator} of the first twisted homology group $H_1^\rho(E_K)$ is defined by
\begin{equation}\label{EQ:Defh1}
h_{(1)}^\rho(\lambda) 
= \iota_*\left(\left[\lbrack \! \lbrack \lambda \rbrack \! \rbrack  \otimes P^\rho\right]\right).
\end{equation}

\begin{remark}
The generator $h_{(1)}^\rho(\lambda)$ of  $H_1^\rho(E_K)$ depends on the orientation of $\lambda$. If we change the orientation of  the longitude $\lambda$ in Eq.~(\ref{EQ:Defh1}),  then the generator is change into its reverse.
\end{remark}

\begin{remark}
Note that $H_i^\rho(E_K)$ is isomorphic to the dual space of the $\sll_\rho$-twisted cohomology $H^i_\rho(E_K) = H^i(E_K; Ad \circ \rho)$. Reference elements defined in Eqs.~(\ref{EQ:Defh2}) and (\ref{EQ:Defh1}) are dual from the ones defined in~\cite[Section~3.4]{JDFibre}.
\end{remark}


\subsubsection{The Reidemeister torsion for knot exteriors}

Let $\rho \colon \Pi(K) \to \SL$ be a $\lambda$-regular representation. The \emph{Reidemeister torsion $\mathbb{T}^K_\lambda$} at $\rho$ is  
defined to be 
\begin{equation}\label{Tordef}
\mathbb{T}^K_\lambda(\rho)  = \mathrm{TOR}\left( {E_K; \sll_\rho, \{h_{(1)}^\rho(\lambda), h_{(2)}^\rho\}, \mathfrak{o}} \right) \in \CC^*.
\end{equation}
It is an invariant of knots. Moreover, if $\rho_1$ and $\rho_2$ are two $\lambda$-regular representations which have the same character then $\mathbb{T}^K_\lambda(\rho_1) = \mathbb{T}^K_\lambda(\rho_2)$. Thus, $\mathbb{T}^K_\lambda$ defines a map on the set $X^{\mathrm{irr}}_\lambda(\Pi(K)) = \{\chi \in X^{\mathrm{irr}}(\Pi(K)) \; |\; \chi \text{ is } \lambda\text{-regular}\}$ {of $\lambda$-regular characters}.

\begin{remark}\label{rmkinv}
The Reidemeister torsion $\mathbb{T}^K_\lambda(\rho)$ defined in Eq.~(\ref{Tordef}) is exactly the inverse of the one considered in~\cite{JDFibre}.
\end{remark}

{In the following remark we discuss sign properties of the torsion $\mathbb{T}^K_\lambda$.}
\begin{remark}\label{rmsgn}
\begin{enumerate}
  \item {The torsion $\mathbb{T}^{K}_{\lambda}$ does not depend on the orientation of $K$ (see~\cite[Proposition 3.4]{JDFibre}).}
  \item {Let $K^*$ denote the mirror image of $K$, and $\lambda^*$ be its preferred longitude as defined in Section~\ref{section:twist_knots}. The character varieties of $E_K$ and $E_{K^*}$ are same and
$\mathbb{T}^{K^*}_{\lambda^*} =  \mathbb{T}^K_\lambda.$}

{Indeed, if we take the mirror image of $K$, then the orientation of the ambient $3$-sphere is reversed, so the orientation of $E_{K^*}$ is the opposite of the one of $E_K$. As a consequence the generator of $H^\rho_2(E_{K^*})$ defined in Eq.~(\ref{EQ:Defh2}) is the opposite of the one of $H^\rho_2(E_{K})$. On the other hand, the meridian $\mu^*$ of $K^*$ is  the inverse of the one of $K$ whereas longitudes are same. So, the homology orientation of $K^*$ is the opposite of the one of $K$ whereas generators of the twisted $H_1$ are same. As a consequence $\mathbb{T}^{K^*}_{\lambda^*} =  \mathbb{T}^K_\lambda$.}
\end{enumerate}

\end{remark}
