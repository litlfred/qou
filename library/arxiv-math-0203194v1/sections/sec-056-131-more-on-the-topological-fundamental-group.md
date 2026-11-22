---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-056-131-more-on-the-topological-fundamental-group
section_title: "More on the topological fundamental group."
section_number: 13.1
pages: 116-118
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.977
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::1.1} 

\begin{para}\label{para::1.1.1}
 We shall work throughout in the context of Berkovich analytic geometry,
 over a fixed complete ultrametric field $(K,|\;|)$.

 What has been said about Berkovich spaces in I.\ref{sec-1} remains true
 in this broader context (\ie without any further restriction on
 $K$). 

 More precisely, we shall work with {\it paracompact strictly
 $K$-analytic spaces} in the sense of \cite{ecfnas}. We recall that these
 form a category equivalent to the category of quasi-separated rigid
 spaces over $K$ having an admissible covering of finite type.

 The main
 advantage of these spaces over rigid spaces lies in their topology: this
 is a topology in the usual sense (not a Grothendieck topology);
 moreover, each point has a fundamental system of open neighborhoods
 which are locally compact, countable at infinity and arcwise connected.

 We shall deal mostly with what we have called, for convenience,
 (analytic) {\it K-manifolds}, \ie 
 paracompact strictly $K$-analytic spaces which satisfy the following
 condition (I.\ref{para:p-adic-manifold}):
 
\begin{quote}
 {\it any $s\in S$ has a neighborhood $U(s)$ which is isomorphic 
 to an affinoid subdomain of some smooth space (in the sense of \cite{ecfnas}
 \ie a space which admits locally an \'etale morphism to the affine space 
  $\A^{\dim S}$).}
\end{quote}

\begin{rems}\label{rems:1.1.1.5}

 a) Any affinoid domain of a $K$-manifold is
 rigid-analytically smooth, \ie satisfies the jacobian criterion (\cf
 \cite[2.2]{ecfnas}; note also that ``smooth'' in the sense of Berkovich
 amounts to ``rigid-analytically smooth and having no boundary''); a
 fortiori, an affinoid $K$-manifold is rigid-analytically
 smooth.  Conversely, a rigid-analytically smooth (strictly) $K$-affinoid
 space $S$ is a $K$-manifold, \cf \cite[rem. 9.7]{spasalc}.

 b) This notion is slightly stronger than the notion of spaces
 locally embeddable in a smooth space considered in \cite{spasalc}. The
 main difference is that we impose that $S$ is a {\it good space} in the
 sense of \cite{ecfnas}, \ie that any point has an affinoid
 neighborhood, which is not automatic for non-classical points (this
 will be useful in \secref{sec::3}).

 c) It follows immediately from remark a) that {\it a
 $K$-manifold is nothing but a good and rigid-analytically smooth
 (paracompact strictly $K$-analytic) space.}

 d) Let $\phi:S'\to S$ be an \'etale morphism of paracompact
 strictly $K$-analytic spaces.  If $S$ is a $K$-manifold, so is $S'$.

 e) For an algebraic $K$-variety $X$, one has $X$ smooth
 $\iff$ $X^{\mathrm{an}}$ smooth $\iff$  $X^{\mathrm{an}}$ is a
 $K$-manifold.  A morphism $f$ is \'etale $\iff$ $f^{an}$ is \'etale.
\end{rems}

 \medskip 
 It follows from \cite[cor. 9.5]{spasalc} that $K$-manifolds are locally
 arcwise-connected and {\it locally simply-connected},
 hence subject to the familiar theory of topological coverings (the
 difficulty is to show that non-classical points admit contractible 
 neighborhoods).   
  In particular, any pointed $K$-manifold $(S,s)$ admits a {\it universal
 (pointed) topological covering} $(\tilde S,\tilde s)$, such that

 $S \cong \tilde S/\pi_1^{\mathrm{top}}(S,s)$; 

 $\tilde S$ is a (pointed) $K$-manifold, and  $\pi_1^{\mathrm{top}}(S,s)$
 is a discrete group of automorphisms of $\tilde S$.

 Let us also recall that in dimension one, $\pi_1^{\mathrm{top}}(S,s)$
 is a free group isomorphic to the fundamental group of the dual graph
 of the semistable reduction of $S$ (\cf \cite[5.3]{efgonas}). In higher
 dimension, there is no such restriction on the discrete groups
 $\pi_1^{\mathrm{top}}(S,s)$: actually, any differentiable manifold is
 homotopy equivalent to some $K$-manifold \cite[6.1.8]{staagonf}.
\end{para}

\begin{para}\label{para::1.1.2}
 Berkovich's analysis of the homotopy of analytic spaces of higher
 dimension makes use of De Jong's alteration theorem. This allows him to
 reduce the problem to the case of the generic fiber of so-called
 polystable fibrations of formal schemes over $K^0$ (the ring of
 integers in $K$). He associates to such fibrations a simplicial set
 which encodes the combinatorics of incidence of the intersection strata
 in the special fiber, and shows that the geometric realization of this
 simplicial set is homotopy equivalent to the generic fiber (viewed as
 an analytic $K$-manifold) \cite[5.4]{spasalc}.

 In particular, in the case of (the generic fiber of) an algebraic
 polystable fibration, the 
 simplicial set is finite, hence the topological fundamental group is
 finitely generated. Using De Jong's theorem and the following result,
 one can deduce that 
 {\it the topological fundamental group of an algebraic $K$-manifold is
 finitely generated}.
\end{para}

\begin{pro}\label{pro::1.1.3}
 Let $\ovl{S}$ be a $K$-manifold, and let $Z$ be a Zariski-closed,
 nowhere dense, reduced analytic subset. Then any topological covering
 of $S:=\ovl{S}\setminus Z$ extends uniquely to a topological covering of
 $\ovl{S}$. Equivalently (since $S$ and $\ovl{S}$ are locally
 simply-connected), the natural homomorphism $\pi_1^{\mathrm{top}}(S,s)\to
 \pi_1^{\mathrm{top}}(\ovl{S},s)$ is an isomorphism.
\end{pro}
\begin{proof}
 Extensions of topological coverings from $S$ to $\ovl{S}$ are unique if
 they exist, since $\ovl{S}$ is normal (note that $S$ is connected, 
 like $\ovl{S}$, by normality of $\ovl{S}$ \cite[3.3.16]{staagonf}).
 For the existence, we argue by induction on the dimension of $Z$
 (starting from the trivial case where $Z$ is empty).  This reduces the
 question to extending topological coverings from $S$ to $\ovl{S}\setminus
 Z^{\mathrm{sing}}$ (where $Z^{\mathrm{sing}}$ denotes the non-smooth
 locus of $Z$, which 
 is closed and of dimension less than the dimension of $Z$, \cf 
 \cite[2.2]{ecfnas}); equivalently, this reduces the question to the case
 where $Z$ is (rigid-analytically) smooth.

 By unicity, the question of existence of extensions is local, \ie is a
 question at the neighborhood in $S$ of each point $z$ of $Z$; we may
 assume that $\ovl{S}$ and $Z$ are (strictly) affinoid,
 rigid-analytically smooth and equidimensional ($Z$ of codimension $r>0$
 in $\ovl{S}$). The statement is clear if $z$ has a neighborhood $U(z)$
 which is a finite union of affinoid domains $U_i$'s such that
 $U_i\setminus (U_i\cap Z)$ is simply-connected. This is indeed the
 case, by Kiehl's theorem on the existence of tubular neighborhoods
 \cite{defeaidnf}: translated into Berkovich geometry, it asserts that (for
 $S$ affinoid and $Z$ a Zariski-closed subset, both rigid-analytically
 smooth and equidimensional) $Z$ has a neighborhood which is a finite
 union of affinoid domains $U_i$'s isomorphic to $(U_i \cap Z)\times
 \matheur{D}^r$, where $\matheur{D}^r$ is an $r$-dimensional polydisk,
 and $ (U_i\cap Z)$ corresponds to $(U_i \cap Z)\times \{0\}.$ Since
 $U_i\cap Z$ is a rigid-analytically smooth affinoid domain, it is
 locally simply connected according to Berkovich; on the other hand, in the
 non-archimedean situation, $\matheur{D}^r\setminus \{0\}$ is
 simply-connected. Whence the result.
\end{proof}
