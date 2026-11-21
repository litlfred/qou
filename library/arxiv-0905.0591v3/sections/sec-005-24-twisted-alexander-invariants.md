---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-005-24-twisted-alexander-invariants
section_title: "Twisted Alexander invariants"
section_number: 2.4
pages: 6-7
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.989
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:twialex}
Let $N$ be a 3-manifold and let $\alpha:\pi_1(N)\to \mbox{GL}(k,R[F])$ be a representation with $R$ a Noetherian UFD.
Similarly to Section \ref{section:twitau} we
define the $R[F]$--chain complex $C_*(\tilde{N})\otimes_{\mathbb{Z}[\pi_1(N)]}R[F]^k$.
 For $i\ge 0$, we define \emph{the $i$-th twisted Alexander module of $(N,\alpha)$} to be the $R[F]$--module
$$
H_i(N;R[F]^k) \mathrel{\mathop:}= H_i(C_*(\tilde{N})\otimes_{\mathbb{Z}[\pi_1(N)]}R[F]^k).
$$
where $\pi_1(N)$ acts on $R[F]^k$ by $\alpha$.
 Since $N$ is compact and $R[F]$
is Noetherian these modules are finitely presented over $R[F]$.



\begin{definition} \label{def:polynomial}
The \emph{$i$-th twisted Alexander polynomial of $(N,\alpha)$}
is defined to be $\mbox{ord} (H_i(N;R[F]^k))\in R[F]$ and denoted by
$\Delta^{\alpha}_{N,i}$.
\end{definition}

Recall that by the discussion of Section \ref{section:torsioninvariants} twisted Alexander polynomials are well-defined up to
multiplication by a unit in $R[F]$.
Note that the units of $R[F]$ are of the form $rf$ with $r$ a unit in $R$ and $f\in F$.
 In the following, given $p\in R[F]$ we write
\[ \Delta^{\alpha}_{N,i} \doteq p \]
if there exists a representative of $\Delta^{\alpha}_{N,i}$ which equals $p$.


\noindent
We often write
 $\Delta^\alpha_{N}$ instead of  $\Delta^{\alpha}_{N,1}$,
and we refer to it as the \emph{twisted Alexander polynomial of
$(N,\alpha)$}. We recall that given a representation $\gamma:\pi_1(N)\to \mbox{GL}(k,R)$ and a non--trivial homomorphism $\psi:\pi_1(N)\to F$ to a free abelian group $F$ we get a tensor
representation $\gamma\otimes \psi$ and in particular  twisted Alexander polynomials
 $\Delta^{\gamma\otimes \psi}_{N,i}$. In almost all cases we will consider twisted Alexander polynomials corresponding to such a tensor representation.

 \noindent
When we consider twisted Alexander polynomials of links we  adopt the following notational conventions:
\begin{enumerate}
\item We identify $R[\mathbb{Z}]$ with $R[t^{\pm
1}]$ and $R[\mathbb{Z}^m]$ with $R[t_1^{\pm 1},\dots,t_m^{\pm 1}]$.
\item Given a link $L\subset S^3$ together with the abelianization  $\psi:\pi_1(S^3\setminus \nu L)\to F$
and a representation $\gamma:\pi_1(S^3\setminus \nu L)\to \mbox{GL}(k,R)$  with $R$ a Noetherian UFD, we  write
$\Delta^{\gamma}_{L,i}$ instead of $\Delta^{\gamma\otimes \psi}_{S^3\setminus \nu L,i}$.
\item If $L$ is an ordered oriented link, then we have a canonical isomorphism $F\cong \mathbb{Z}^m$
and we can identify $R[F]$ with $R[t_1^{\pm 1},\dots,t_m^{\pm 1}]$.
\item We sometimes record the fact that the twisted Alexander polynomial of a link $L$ is a (multivariable) Laurent polynomial in the notation, i.e. given
an oriented knot $K\subset S^3$ we sometimes write $\Delta^\gamma_{K,i}(t)=\Delta^\gamma_{K,i}\in R[t^{\pm
1}]$
and given an ordered oriented $m$--component link $L\subset S^3$
we sometimes write $\Delta^\gamma_{L,i}(t_1,\dots,t_m)=\Delta^\gamma_{L,i}\in R[t_1^{\pm 1},\dots,t_m^{\pm 1}]$.
\item Finally given a link $L$ we also drop the representation from the notation when the representation
 is the trivial representation to $\mbox{GL}(1,\mathbb{Z})$.
\end{enumerate}

With all these conventions, given a knot $K\subset S^3$, the polynomial $\Delta_K(t)=\Delta_K \in \mathbb{Z}[t^{\pm 1}]$
is just the ordinary Alexander polynomial.
