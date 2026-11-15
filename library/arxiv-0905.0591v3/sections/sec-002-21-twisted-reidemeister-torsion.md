---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-002-21-twisted-reidemeister-torsion
section_title: "Twisted Reidemeister torsion"
section_number: 2.1
pages: 3-4
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.968
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexander polynomials of a 3–manifold associated to a representation of its fundamental group."
---
\label{section:twitorsion}\label{section:twitau}


Let $N$ be a 3--manifold with empty or toroidal boundary, $F$ a torsion--free abelian group
and $\alpha:\pi_1(N)\to \mbox{GL}(k,R[F])$  a representation. Recall that we denote by $Q(R[F])$ the quotient field of $R[F]$.

We endow $N$ with a finite CW--structure.
We denote the universal cover of $N$ by $\tilde{N}$.
Recall that there exists a canonical left $\pi_1(N)$--action on the universal cover $\tilde{N}$ given by deck transformations. We
consider the cellular chain complex $C_*(\tilde{N})$ as a right $\mathbb{Z}[\pi_1(N)]$-module by defining $\sigma \cdot
g\mathrel{\mathop:}= g^{-1}\sigma$ for a chain $\sigma$. The representation $\alpha$ induces a representation $\alpha:\pi_1(N)\to \mbox{GL}(k,R[F])\to \mbox{GL}(k,Q(R[F]))$
which gives rise to  a left action of $\pi_1(N)$ on $Q(R[F])^k$. We can therefore consider
the  $Q(R[F])$--complex
\[ C_*(\tilde{N})\otimes_{\mathbb{Z}[\pi_1(N)]}Q(R[F])^k.\]
We now endow the free $\mathbb{Z}[\pi_1(N)]$--modules $C_*(\tilde{N})$
with a basis by picking lifts of the cells of $N$ to $\tilde{N}$.
Together with the canonical basis for $Q(R[F])^k$ we can now view  the $Q(R[F])$--complex $C_*(\tilde{N})\otimes_{\mathbb{Z}[\pi_1(N)]}Q(R[F])^k$
as a complex of based $Q(R[F])$--modules.

If this complex is not acyclic, then we define $\tau(N,\alpha)=0$.
Otherwise we denote by $\tau(N,\alpha)\in Q(R[F])\setminus \{0\}$ the  Reidemeister torsion of this based $Q(R[F])$--complex.
We will not recall the definition of Reidemeister torsion, referring instead to the many excellent expositions,
 e.g. \cite{Mi66}, \cite{Tu01} and \cite{Nic03}. However, in the next section we will
present a method for computing explicitly the twisted Reidemeister torsion of a 3--manifold.

It follows from Chapman's theorem \cite{Chp74} and from standard arguments (cf. the above literature) that
up to multiplication by an element in
\[     \{ \pm\det(\alpha(g)) \, |\, g\in \pi_1(N)\}\]
the Reidemeister torsion $\tau(N,\alpha)$ is well--defined, i.e. up to that indeterminacy $\tau(N,\alpha)$ is independent of the choice of underlying CW--structure
and the choice of the lifts of the cells. In the following, given $w\in Q(R[F])$ we write
\[ \tau(N,\alpha) \doteq w \]
if there exists a representative of $\tau(N,\alpha)$ which equals $w$.


Note that if $\gamma:\pi_1(N)\to \mbox{GL}(k,R)$ is a representation and $\psi:\pi_1(N)\to F$ a  homomorphism to a free abelian group, then we get a tensor representation
\[ \begin{array}{rcl} \gamma\otimes \psi: \pi_1(N) &\to & \mbox{GL}(k,R[F]) \\
g&\mapsto & \gamma(g)\cdot \psi(g)\end{array} \]
and the corresponding Reidemeister torsion $\tau(N,\gamma \otimes \psi)$. Except for parts of Section \ref{section:slice}
we will always consider the twisted Reidemeister torsion corresponding to such a tensor representation.
In that case, specializing the previous formula, $\tau(N,\gamma \otimes \psi)$  is well--defined up to multiplication by an element  in
\[     \{\pm \det(\gamma(g)) f\, |\, g\in \pi_1(N), f\in F\}.\]
In particular, if $\gamma:\pi_1(N)\to \mbox{SL}(k,R)$ is a  representation to a special linear groups,
then $\tau(N,\gamma \otimes \psi)\in Q(R[F])$ is well--defined up to multiplication
by an element in $\pm F$.
Furthermore, if $k$ is even, then $\tau(N,\gamma\otimes \psi)\in Q(R[F])$ is in fact well--defined up to multiplication
by an element in $F$ (cf. e.g. \cite{GKM05}).

\noindent Finally we adopt the following notation:
\begin{enumerate}
\item Given a homomorphism $\gamma:\pi\to G$ to a finite group $G$
we get an induced representation $\pi\to \mbox{Aut}(\mathbb{Z}[G])\cong \mbox{GL}(|G|,\mathbb{Z})$
given by left multiplication. In our notation we will not distinguish between a homomorphism to a finite group and the corresponding representation over $\mathbb{Z}$.


\item If $N$ is the exterior of a link $L\subset S^3$, $\psi:\pi_1(S^3\setminus \nu L)\to F$ the abelianization
and $\gamma:\pi\to \mbox{GL}(k,R)$ a representation, then we  write
$\tau(L,\gamma)$ for $\tau(S^3\setminus \nu L,\gamma\otimes \psi)$.


\end{enumerate}
