---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-009-31-technical-assumptions
section_title: "Technical assumptions"
section_number: 3.1
pages: 7-9
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.989
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
\label{section:hyp}

In this subsection, we give some sufficient conditions on the compact
hyperbolic three--manifold $M$ whose boundary consists of
a disjoint union of tori and on the representations $\varphi$ and
$\rho$ which assure the acyclicity of the twisted chain complex
$C_*(M;\sllmt_\rho)$. 

We require assumptions on the topology of $M$,
on the surjective homomorphism $\varphi$ of $\pi_1(M)$ onto $\ZZ^n$ and
on the $\SL$-representation $\rho$. The assumption on $\varphi$ is also
related to the topology of $M$, we will show this in the second half
of this subsection.

We also prove that if $M$ is a hyperbolic knot exterior,
$\varphi\colon \pi_1(M) \to \ZZ$ the abelianization and $\rho\colon
\pi_1(M) \to \SL$ the holonomy (\ie~the discrete and faithful
representation), then all our assumptions are satisfied.


\subsubsection{Topological assumption for $M$}

Let $b$ be the number of components of $\bord
M$.  We let $T^2_\ell$ denotes the $\ell$--component of $\bord M$.  The usual inclusion $i:\bord M \to M$
  induces an homomorphism $i_* \colon H_1(\bord M;\ZZ) \to
  H_1(M;\ZZ)$. First we assume
the following condition on the homology group $H_1(M;\ZZ)$:
\begin{itemize}
\item[$(A_M)$] the homomorphism  $i_* \colon H_1(\bord M;\ZZ) \to
  H_1(M;\ZZ)$ is onto and its restriction  $(i|_{T^2_\ell})_*$ to the $\ell$-th component of $\partial M$ 
  has rank one for all $\ell$.
\end{itemize}
Thus we can choose two closed loops $\mu_\ell$ and $\lambda_\ell$ on $T^2_\ell$ 
such that the homology classes $\bbrack{\mu_\ell}$ and $\bbrack{\lambda_\ell}$ form a basis of 
$H_1(T^2_\ell;\ZZ)$ and the image $i_*(\bbrack{\mu_\ell})$ generates the subgroup $\im (i|_{T^2_\ell})_*$
and $\bbrack{\lambda_\ell}$ generates the kernel of $(i|_{T^2_\ell})_*$. We call $\mu_\ell$ a meridian and $\lambda_\ell$ a longitude.

We let $\bm{\lambda}$ denote the set 
$(\lambda_1, \ldots, \lambda_b) \subset \partial M$ of 
such generators of $\ker \varphi_{|\pi_1(T^2_\ell)}$
and call $\bm{\lambda}$ the multi--longitude curve.

\begin{remark}
  From the homology long exact sequence of $(M, \bord M)$, it follows
  that $b_1(M) = b$ and $H_1(M;\ZZ)$ has no--torsion.
\end{remark}

\begin{example}[Knot exteriors]\label{ex:knot}
Suppose that $M$ is the exterior $E_K$ of a
hyperbolic knot $K$ in $S^3$. Here $E_K = S^3 \setminus N(K)$ where $N(K)$ is an
open tubular neighbourhood of $K$.  Then $M = E_K$ satisfies the
condition~$(A_M)$. This is due to the existence of a Seifert
surface of the knot.
\end{example}

\begin{remark}[Link exteriors]

 Let $L$ be a hyperbolic link such that each
components of the link bounds a Seifert surface missing the other
components.  This condition for a link $L = K_1 \cup \ldots \cup K_b$
is equivalent to that the linking numbers $\lk(K_i, K_j)$ are zero for
all $i, j$. It is the reason that we can obtain the required Seifert
surface by first choosing an arbitrary Seifert surface for $K_{i_k}$
and then getting rid of the intersections by adding tubes as in
Fig~\ref{fig:whitehead_link}.  The intersections of such Seifert surfaces
and the boundary $\bord E_L$ form a set of longitudes.

Note that it is not necessarily the case that Seifert surfaces are
disjoint if each component of a link $L = K_1 \cup \ldots \cup K_b$
bounds a Seifert surface missing the other components.  Links whose
components do bound disjoint Seifert surfaces are called 
{\it boundary links}. 
For example, the Whitehead link $L = K_1 \cup K_2$ has the
linking number $\lk(K_1, K_2) = 0$.  Hence there exist two Seifert
surfaces $F_i$ ($i=1, 2$) such that $\bord F_i = K_i$ and $F_i \cap
K_j = \emptyset$\, ($i \not = j$).  But in fact the Whitehead link
does not bound disjoint Seifert surfaces since the Whitehead link is
not a boundary link, for more details see~\cite[Chapter 5 E]{Rolfsen}.

In this paper, three--manifold under considerations has the same properties about the homology group like as 
those of a boundary link exterior.
\end{remark}

\begin{figure}[!h]
  \begin{center}
    \includegraphics[scale=.5]{Whitehead_link}
  \end{center}
  \caption{The Whitehead link}
  \label{fig:whitehead_link}
\end{figure}


\subsubsection{Assumption on $\varphi$}

We suppose that 
$$\varphi \colon \pi_1(M) \to \ZZ^n = 
\left\langle t_1, \ldots, t_n \;|\; t_i t_j = t_j t_i, \; \forall i, j \; \right\rangle$$
 is a
surjective homomorphism which satisfies the following assumption (in
the case of manifolds with boundary)
\begin{itemize}
\item[$(A_\varphi)$] the restriction $\varphi_{|\pi_1(T^2_\ell)}$ of
  $\varphi$ to the $\ell$--th boundary component of $\partial M$ is non--trivial and
  has rank 1, \ie
  $$\varphi(\pi_1(T^2_\ell)) = 
  \langle t_1^{a_1^{(\ell)}} \cdots t_n^{a_n^{(\ell)}} \rangle$$ 
  for some $(a_1^{(\ell)}, \cdots, a_n^{(\ell)}) \in \NN^n\setminus \{0\}$.
\end{itemize} 

\begin{remark}
  Every homomorphism from $\pi_1(M)$ to an abelian group factors
  through the abelianization $H_1(M;\ZZ)$ of $\pi_1(M)$, \ie, the
  following diagram is commutative:
  $$
  \xymatrix@R=20pt{
    \pi_1(M) \ar[rd]_{\varphi} \ar[r] & 
    H_1(M;\ZZ) \ar[d]^{\varphi_h}\\
     & 
    \ZZ^n 
  }
  $$
  When we consider a surjective homomorphism $\varphi$ onto $\ZZ^n$,
  the induced homomorphism $\varphi_h$ is also surjective. Together
  with the condition $(A_M)$, this means that \emph{$n$ must be not greater than  $b_1(M) = b$}.  Moreover we have the null--homologous closed
  curve $\lambda_\ell$ on each $T^2_\ell$, every homomorphism $\varphi$ has
  the multi--longitude consisting of these $\lambda_\ell$.
\end{remark}

\begin{example}[Abelianization representation]\label{ex:ab}
 Suppose that $M$ is the exterior $E_K$ of a knot $K \subset S^3$ or a link exterior $E_L$ of a link $L \subset S^3$ whose linking number between arbitrary two components is zero. The
abelianization $\varphi\colon \pi_1(M) \to H_1(M; \ZZ) \simeq \ZZ^b$ satisfies Assumption $(A_\varphi)$.  From Assumption~$(A_M)$, it follows that $H_1(M;\ZZ)
= \langle \mu_1, \ldots, \mu_b\rangle$.  Assumption ~$(A_\varphi)$
means that each entry of any representative matrix of $\varphi_h$ is
non-zero.
\end{example}


\subsubsection{Assumption on $\SL$-representations}

It is required for an $\SL$-representation $\rho$ of $\pi_1(M)$ to be
a {\it ``generic''} representation, which essentially means that
$\rho$ lies in {\it the geometric components} of {\it the character
  variety}.
  
The character variety of $\pi_1(M)$ is the set of characters of
$\SL$-representations. Here the character of an $\SL$-representation
$\rho$ is a map $\pi_1(M) \to \CC$ given by the assignment $\gamma
\mapsto \trace \rho(\gamma)$ for all $\gamma \in \pi_1(M)$, where $\trace$ denotes the usual trace of square matrices.  This set
has a structure of an affine algebraic variety (refer to
\cite{CS:1983}) denoted by $X(M)$. For a complete hyperbolic manifold,
the character variety $X(M)$ contains the distinguished components
related to the complete hyperbolic structure.  These components are
defined by containing a lift of the holonomy representation $\pi_1(M)
\to \PSL$ (\ie, the discrete and faithful representation)  determined by the complete hyperbolic structure.
We call these components the geometric components.

Here $\bm{\lambda}$ is the multi--longitude corresponding to $\varphi$.
The precise definition is given as follows.

\begin{notation*}
  For each boundary component $T^2_\ell$ of $M$, we fix a generator
  $P_\ell^\rho$ of the homology group $H_0(T^2_\ell; \sllrho)$, \ie~a
  non--trivial vector $P_\ell^\rho \in \sll$ which satisfies
  $Ad_{\rho(g)}(P_\ell^\rho) = P_\ell^\rho$ for all $g \in \pi_1(T^2_\ell)$
  (for more details, see~\cite[Section 3.3.1]{Porti:1997}).
\end{notation*}

\begin{definition}
  For the multi--longitude $\bm{\lambda} = \{\lambda_1, \ldots,
  \lambda_b\}$, an irreducible representation $\rho$ is called
  $\bm{\lambda}$-regular if $\rho$ satisfies the following conditions:
  \begin{enumerate}
  \item for each boundary component $T^2_\ell$ of $\bord M$, the restriction of
    $\rho$ to $\pi_1(T^2_\ell)$ is non--trivial;
  \item the following homomorphism, induced from all inclusions $\lambda_\ell \hookrightarrow M$ $(1 \myleq \ell \myleq b)$,
    $$\mathop{\bigoplus}_{\ell = 1}^b H_1(\lambda_{\ell};\sllrho) \to H_1(M;\sllrho)$$
    is surjective and;
  \item if $\trace \rho(\pi_1(T^2_\ell)) \subset \{\pm 2\}$, 
     then
    $\rho(\lambda_{\ell}) \not = \pm \I$.
  \end{enumerate}
\end{definition}

\begin{remark}
  The chain $P^\rho_\ell \otimes \lambda_{\ell}$ becomes a cycle \ie,
  it defines a homology class in $H_1(\lambda;\sllrho)$.
  By~\cite[Proposition 3.22 and Corollaire 3.21]{Porti:1997}, for a
  $\bm{\lambda}$-regular representation $\rho$, we have the following
  bases of the twisted homology groups:
  \begin{itemize}
  \item the homology group $H_1(M;\sllrho)$ has a basis $\left\{
    \bbrack{P^\rho_1 \otimes \lambda_1}, \ldots, \bbrack{P^\rho_b \otimes \lambda_b} \right\}$,
  \item the homology group $H_2(M;\sllrho)$ has a basis  $\left\{
    \bbrack{P^\rho_1\otimes T^2_1}, \ldots, \bbrack{P^\rho_b \otimes T^2_b} \right\}$.
  \end{itemize}
In \cite[Definition 3.21]{Porti:1997}, irreducibility is not required and the second condition is written by using 
twisted cohomology groups.
Since we consider representations near the holonomy representation of $\pi_1(M)$,
 we focus on $\bm{\lambda}$-regularity of irreducible representations in the present article.
\end{remark}

Here we use the same symbol $\lambda_\ell$ and $T^2_\ell$ for lifts of $\lambda_\ell$ and $T^2_\ell$ to the universal cover.

\begin{remark}
  For generic points on the geometric component of $X(M)$, the
  corresponding $\SL$-representations satisfy
  $\bm{\lambda}$-regularity.
\end{remark}
  
We assume the following assumption for $\SL$-representation of
$\pi_1(M)$
\begin{itemize}
\item[$(A_\rho)$] the representation $\rho\colon \pi_1(M) \to \SL$ is
  $\bm{\lambda}$-regular for the multi--longitude $\bm{\lambda}$ determined by $\varphi \colon \pi_1(M) \to \ZZ^n$.
\end{itemize}

\begin{example}[Holonomy representation]\label{ex:holonomy}
  Suppose that $M$ is a hyperbolic three--di\-men\-sio\-nal manifold. Let
  $\rho_0\colon \pi_1(M) \to \SL$ be a lift of the
  discrete and faithful representation of $\pi_1(M)$ to
  $\mathrm{PSL}_2(\CC)$ given by the hyperbolic structure. Porti
  proves~\cite{Porti:1997} that $\rho_0$ satisfies Assumption
  $(A_\rho)$ for any system of homotopically non--trivial curves $(\gamma_1, \ldots,
  \gamma_b)$.
 \end{example}

We mention a relation between the character variety $X(M)$ and the
twisted homology group $H_1(M;\sllrho)$ for $\bm \lambda$-regular representation.  
\begin{remark}
  The twisted cohomology group $H^1(M;\sllrho)$ is the dual space of
  the twisted homology group $H_1(M;\sllrho)$ by the Universal
  Coefficient Theorem.  Following~\cite{TN} and~\cite[Proposition
  3.2.1]{CS:1983} together with $\chi(M)=0$, it is known that, near
  the discrete and faithful representation, the character variety
  $X(M)$ is a complex affine variety with dimension $b$ where $b$ is
  the number of torus boundary components.  In affine varieties, the
  dimension of Zariski tangent space is not less that the one of
  of the variety.  The Zariski tangent space of the character variety
  can be injectively mapped into $H^1(M;\sllrho)$.  We also have 
  $\dim_{\CC} H^1(M;\sllrho) = b$ near the discrete and faithful
  representation, thus the spaces $X(M)$, $T^{Zar}_{\chi_\rho}X(M)$
  and $H^1(M;\sllrho)$ have the same dimension $b$.  This means that
  characters near the discrete and faithful representation are
  smooth points and $H^1(M;\sllrho)$ is identified with the tangent
  space $T_{\chi_\rho}X(M)$ (see also \cite[Chapter 3]{Porti:1997} for
  such identifications).
\end{remark}
