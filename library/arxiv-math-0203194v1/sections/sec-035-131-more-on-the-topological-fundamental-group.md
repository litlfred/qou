---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp Tôhoku-Hokkaidô lectures in Arithmetic Geometry"
section_id: sec-035-131-more-on-the-topological-fundamental-group
section_title: "More on the topological fundamental group."
section_number: 13.1
pages: 116-123
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.979
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



\subsection{\'Etale versus topological coverings (again).}\label{sub::1.2}  

\begin{para}\label{para::1.2.1}
 Let $S$ be a connected $K$-manifold. Let $S' \xrightarrow{f} S$ be a
 finite \'etale morphism ($S'$ is then a $K$-manifold).  Its degree $n$ may be
 defined as the rank of the locally free $\mathcal{O}_S$-module
 $f_\ast\mathcal{O}_{S'}$. Assume that $K$ is algebraically closed. Then
 one has the formula 

 \begin{equation*}
  n=\sum_{y\in f^{-1}(x)}[\mathscr{H}(y):\mathscr{H}(x)]
 \end{equation*}
 where $\mathscr{H}(x)$ stands for the residue field of
 the point $x$ (if $S=\matheur{M}(\mathcal{A})$ is affinoid and
 $x$ corresponds to the bounded multiplicative seminorm $|\;|_x$, this is
 just $\mathscr{H}(x)= 
 \widehat{Q(\mathcal{A}/\Ker|\;|_x)}$).

 Then $f$ is a {\it topological covering if and only if all fibers have
 the same cardinality}, which 
 amounts to the algebraic notion of being ``completely decomposed'': $
 \mathscr{H}(y)=\mathscr{H}(f(y))$ for any $y\in S'$, 
 \cf \cite[3.2.7]{staagonf}, \cite[6.3.1]{ecfnas}.

 This criterion shows at once that the Kummer \'etale covering
 $z\mapsto z^n$ (with $\mathrm{char}(K) \nmid n$) of the 
 punctured disk is {\it not} a topological covering. 
\end{para}

\begin{para}\label{para::1.2.2}   A {\it geometric point} $\ovl{s}$ of $S$ is a
 point with value in some complete algebraically closed extension 
 $(\Omega,|\;|)$ of
 $(K,|\;|)$,  \ie a morphism ${\ovl{s}} : \matheur{M}(\Omega) \to S$ in
 the category of analytic spaces over 
 $K$ \cite[p.48]{staagonf}.  For any finite \'etale covering there are
 exactly $n$ liftings ${\ovl{s}'}:\matheur{M}(\Omega)\to S'$ of $\ovl{s}$,
 \ie $n$ geometric points of $S'$ above $S$. We usually denote by $s$ the
 point of $S$ which is the image of $\ovl{s}$.  
\end{para}

\begin{dfn} [Berkovich, De Jong] \label{def::1.2.3}
 A morphism $f:S'\to S$ is a {\it covering} (\resp {\it \'etale 
 covering}, \resp {\it topological covering}) if $S$ is covered by open
 subsets $U$ such that $\coprod V_j = f^{-1}U \to U$ and the restriction 
 of $f$ to every $V_j$ is finite (\resp \'etale finite, \resp an
 isomorphism).
\end{dfn}

\noindent There is an obvious notion of morphism
 between coverings of $S$.  The category of \'etale coverings, \resp
 finite \'etale coverings, \resp topological coverings, will be denoted
 by $\Cov^{\mathrm{et}}_S$, \resp $\Cov^{\mathrm{alg}}_S$, \resp
 $\Cov^{\mathrm{top}}_S$.
 
 \medskip There are inclusions (fully faithful embeddings) 
 \begin{equation*}
  \Cov^{\mathrm{alg}}_S \hookrightarrow  \Cov^{\mathrm{et}}_S,
   \quad \Cov^{\mathrm{top}}_S \hookrightarrow  \Cov^{\mathrm{et}}_S.
 \end{equation*}

\begin{rems}
 (i) If $S'\to S$ is an \'etale covering, then $S'$ is a $K$-manifold.

 (ii) It is worth noticing that the notions of \'etale and of 
 topological coverings are local on the base $S$, but not the
 notion of algebraic coverings (except if $S$ is compact).

 (iii) Even if $S$ is covered by finitely many $U$'s as in the
 definition, it does not follow that $S'$ is a disjoint union of
 finite algebraic coverings of $S$. For instance, a Tate elliptic
 curve (with universal covering $\tilde S\cong \G_m$) has a
 covering by two open subsets $U_1,U_2$ such that $\tilde S_{|
 U_i}$ is a disjoint union of copies of $S$.

  (iv) It is an immediate but important fact that these
 categories are stable under taking fiber product (over $S$). 
 It is also stable under taking finite disjoint unions.

  (v) One should pay attention to the fact that unlike
 $\Cov^{\mathrm{top}}_S$, $\Cov^{\mathrm{et}}_S$ is not stable 
 under arbitrary disjoint unions, nor under composition (in the sense
 that the composition of an \'etale covering $S'/S$ and an \'etale
 covering $S''/S'$ may not be an \'etale covering
 $S''/S$). However, we have:
\end{rems}

\begin{lem}\label{lem::1.2.4}
 Any morphism which is the composition of a covering (\resp \'etale
 covering) followed or preceded by a finite (\resp finite \'etale)
 morphism is a covering (\resp \'etale covering).
\end{lem}
\begin{proof}
 Let us consider the case of a covering $g:S''\to S'$
 followed by a finite covering $f:S'\to S$ (the reverse situation is
 immediate from the definition). Let $s$ be a point of $S$. Then for any
 $s'$ in the finite set $f^{-1}(s)$, there exists an open neighborhood
 $U_{s'}\subset S'$ of $s'$ such that $g^{-1}(U_{s'})$ is a disjoint
 union of spaces $U_{s',i}$, each being finite over $U_{s'}$ via $g$. We
 may assume that the $U_{s'}$ are pairwise disjoint. Since $f$ is finite,
 it is in particular a closed continuous map, hence 
 $S'$ admits a basis of open neighborhoods of $f^{-1}(\bar{s})$ of
 the form $f^{-1}(V)$. 

 In particular,
 there is an open neighborhood $V_s$ of $s$ such that $\displaystyle
 \coprod_{s'\in f^{-1}(s)} U_{s'}$ contains $f^{-1}(V_s)$. We may
 replace each $U_{s'}$ by its intersection with $f^{-1}(V_s)$ (which is a
 union of connected components of $f^{-1}(V_s)$). It is then clear that
 $g\circ f$ induces a finite morphism from $U_{s',i}$ to $V_s$. Hence
 $g\circ f$ is a covering.  The \'etale variant is similar.
\end{proof}

\begin{exs}\label{exs::1.2.5}
  (i) The prototype of an \'etale covering is given by the logarithm map
	\begin{equation*}
	 \log:\; \matheur{D}_{\C_p}(1,1^-)\longrightarrow
	 (\A^1_{\C_p})^{\mathrm{an}}.
	\end{equation*}
	For any $m\in \N$, the inverse image of the open disk
	\begin{equation*}
	 \matheur{D}_m=\matheur{D}\left(0,
	 \bigl(|p|^{-m+\frac{1}{p-1}}\bigr)^-\right)
	 \subset (\A^1_{\C_p})^{\mathrm{an}}
	\end{equation*}
	is a disjoint union
	\begin{equation*}
	 \coprod_{\zeta \in \mu_{p^\infty}}\;\Bigl\{q\in
	  \matheur{D}(1,1^-) \Bigm| \zeta q^{p^m}\in 
	  \matheur{D}\left(1, \bigl(|p|^{\frac{1}{p-1}}\bigr)^-\right)\Bigr\}
	\end{equation*}
	and each of these components is isomorphic to $\matheur{D}_m$ if $m=0$,
	and finite \'etale onto $\matheur{D}_m$ in general (we are using
	here the 
	factorization $q\mapsto \zeta q^{p^m}=t\mapsto \log t \mapsto
	p^{-m}\log t =\log q$ of the logarithm).

  (ii) This example may be interpreted as a Dwork period
	mapping (II.\ref{para:6.3.1}). In fact, all examples of period
	mappings considered in II.\ref{sub:6.3} are \'etale coverings
	of the period domain 
	$\mathcal{D}$. For instance, the Gross-Hopkins period mapping  
	(II.\ref{para:6.3.2}) is an \'etale covering of $
	(\P^1_{\C_p})^{\mathrm{an}}$, \cf \cite[7.2]{efgonas}. 

	\noindent Any period mapping is \'etale, but it may happen in
	some cases that it is surjective without being an \'etale
	covering, \cf \cite[5.41]{psfpg} (this somewhat mysterious
	phenomenon is due to the existence of bijective
	non-quasi-compact \'etale morphisms).

  (iii) Any (possibly infinite) topological covering of a
	finite \'etale covering is an \'etale covering after \ref{lem::1.2.4}.
\end{exs}

The following two lemmas are due to V. Berkovich and J. De Jong (and not
stated in the most general form).
 
\begin{lem}\label{lem::1.2.6}
 \begin{enumerate}
  \item An \'etale presheaf $\mathcal{F}$ on $S$ which is representable
	by an \'etale covering $S'$ is a sheaf.  For any subdomain $U
	\subset S$, $\mathcal{F}_{|U}$ is representable by $S'\times_S
	U$.
  \item Let $\mathcal{F}$ be an \'etale sheaf. Let $U_i$ an
	open covering of $S$. If for every $i$, $\mathcal{F}_{|U_i}$ is
	representable by an \'etale covering, so is $\mathcal{F}$.
 \end{enumerate}
\end{lem}
 
 For (i), \cf \cite[4.1.3, 4.1.4, 4.1.5]{ecfnas}.  Here we take advantage
 of working with {\it strict} analytic spaces.  Gluing --- using 
 \cite[1.3.3]{ecfnas} --- gives (ii) (\cf also \cite[2.3]{efgonas}).

\begin{lem}\label{lem::1.2.7} Let $S'\to S$ be an \'etale covering, and
 let $R\subset S'\times_S S'$ be a union of connected components which
 is an equivalence relation on $S'$ over $S$. Then $S'/R$ (viewed as an
 \'etale sheaf on $S$) is representable by an \'etale covering $S''\to S$. 
\end{lem}


\cf \cite[2.4]{efgonas}: by the previous lemma, the question is local on
 $S$; the proof is by reduction to the case of a finite \'etale covering
 of affinoid spaces. 

\medskip In the situation of \ref{lem::1.2.7}, we say that the $S''\to
 S$ is a {\it quotient \'etale covering of} $S'\to S$.



\subsection{Existence of \'etale paths.}\label{sub::1.3}  
 
\begin{para}\label{para::1.3.1} Let us fix a geometric point $\ovl{s}$ of
 $S$. We consider the fiber functor 
 \begin{equation*}
  F^{\mathrm{et}}_{S,\ovl{s}}=F^{\mathrm{et}}_{\ovl{s}} :
   \Cov^{\mathrm{et}}_S \longrightarrow \Sets,\;\; S' \mapsto
   \{\text{geometric points $\ovl{s}'$ of $S'$ above $\ovl{s}$}\}
 \end{equation*}
and its restrictions

\begin{equation*}
 F^{\mathrm{alg}}_{S,\ovl{s}}=F^{\mathrm{alg}}_{\ovl{s}}:
 \Cov^{\mathrm{alg}}_S\longrightarrow \Sets,
\end{equation*}
(considered in \cite{sga1}) and
\begin{equation*}
 F^{\mathrm{top}}_{S,\ovl{s}}=F^{\mathrm{top}}_{\ovl{s}}:
  \Cov^{\mathrm{top}}_S\longrightarrow \Sets.
\end{equation*} 

 An {\it \'etale path} (\resp {\it algebraic path}) from
 $\ovl{s}$ to another geometric point $\ovl{t}$ of $S$ is an isomorphism
 of functors $F^{\mathrm{et}}_{\ovl{s}} \xrightarrow{\sim}
 F^{\mathrm{et}}_{\ovl{t}}$ (\resp $F^{\mathrm{alg}}_{\ovl{s}}
 \xrightarrow{\sim} F^{\mathrm{alg}}_{\ovl{t}}$). 

 The set of \'etale paths is topologized by taking as fundamental open
 neighborhoods of an \'etale path $\alpha$ the set 
 $\Stab_{S',\ovl{s}'}\circ \alpha$, where $\Stab_{S',\ovl{s}'}$ runs among
 the stabilizers in $\Aut(F_{\bar{s}}^{\mathrm{et}})$ of arbitrary geometric
 points $\ovl{s}'$ above 
 $\ovl{s}$ in arbitrary \'etale coverings $S'/S$.

 If we do the same for algebraic paths, we get the profinite topology
 considered in \cite{sga1}. 

 On the other hand, an isomorphism of functors
 $F^{\mathrm{top}}_{\ovl{s}} \xrightarrow{\sim}
 F^{\mathrm{top}}_{\ovl{t}}$ amounts to a path up to homotopy in the
 usual sense between $s$ and $t$ in the arcwise connected space $S$
 (this is compatible with composition of paths, which is juxtaposition
 in the reverse order according to our convention); they form a
 discrete set --- in fact, a principal homogeneous space under 
 $\pi^{\mathrm{top}}(S,s)$ acting on the left. 

 \medskip The inclusions $ \Cov^{\mathrm{alg}}_S \hookrightarrow
 \Cov^{\mathrm{et}}_S ,\;\Cov^{\mathrm{top}}_S \hookrightarrow
 \Cov^{\mathrm{et}}_S$ induce continuous maps from the space of \'etale
 paths between $\ovl{s}$ and $\ovl{t}$ to the space of algebraic paths
 between $\ovl{s}$ and $\ovl{t}$ (\resp to the discrete set of paths up
 to homotopy between $s$ and $t$).

 \medskip\noindent If $f: S\to X$ is any morphism of $K$-manifolds, and
 if $\alpha$ is an \'etale path from $\ovl{s}$ to $\ovl{t}$, there is an 
 obvious notion of push-forward $f_\ast\alpha$, which is an \'etale path
 from $f\circ \ovl{s}$ to $f\circ \ovl{t}$ ; it is compatible with
 composition of \'etale paths (as composition of isomorphisms of functors).
\end{para}

\begin{para}\label{para::1.3.2} It follows from \cite[exp. V]{sga1} that
 algebraic paths exist. Using the nice topology of Berkovich spaces,
 A.J. De Jong was able to prove \cite[2.9]{efgonas}: 
\end{para}

\begin{klem}\label{lem::1.3.3}  Etale paths exist. More precisely,
 any Berkovich path $\gamma$ (up to homotopy) between $s$ and 
 $t$ lifts to an \'etale path $\ovl{\gamma}$ between $\ovl{s}$ and $\ovl{t}$.
\end{klem}

\begin{proof}
 Up to introducing intermediate geometric points, we may assume
 that $S$ is affinoid (hence compact). For any {\it finite} open cover
 $\mathcal{U}=(U_i)$ of $S$, let us denote by
 $\Cov^{\mathrm{et}}_{S,\mathcal{U}}$ the full subcategory of
 $\Cov^{\mathrm{et}}_{S}$ of \'etale coverings $f:S'\to S$ such that
 $f^{-1}(U_i)= \coprod V_{ij}$ and $V_{ij}$ is \'etale finite over $U_i$
 via $f$.  We thus have
 \begin{equation*}
 \Cov^{\mathrm{et}}_{S}=\underset{\mathcal{U}}{\liminj}\;
  \Cov^{\mathrm{et}}_{S,\mathcal{U}}, \text{ and }
  \Isom(F^{\mathrm{et}}_{\ovl{s}}, F^{\mathrm{et}}_{\ovl{t}})
  =\underset{\mathcal{U}}{\limproj}\;
  \Isom(F^{\mathrm{et}}_{\ovl{s},\mathcal{U}},
  F^{\mathrm{et}}_{\ovl{t},\mathcal{U}})
 \end{equation*}

 \medskip\noindent where $F^{\mathrm{et}}_{\ovl{s},\mathcal{U}},
 F^{\mathrm{et}}_{\ovl{t},\mathcal{U}}$ denote the restrictions of
 $F^{\mathrm{et}}_{\ovl{s} }, F^{\mathrm{et}}_{\ovl{t} }$ to
 $\Cov^{\mathrm{et}}_{S,\mathcal{U}}$.

 We have to show that $\Isom(F^{\mathrm{et}}_{\ovl{s}},
 F^{\mathrm{et}}_{\ovl{t}}) \neq \emptyset$. The idea is to construct 
 non-empty compact subsets $K_\mathcal{U}$ of
 $\Isom(F^{\mathrm{et}}_{\ovl{s},\mathcal{U}},
 F^{\mathrm{et}}_{\ovl{t},\mathcal{U}})$ (topologized as above) such that
 if $\mathcal{U}'$ refines $\mathcal{U}$, $K_{\mathcal{U}'}$ maps to
 $K_\mathcal{U} $ under the natural map
 $\Isom(F^{\mathrm{et}}_{\ovl{s},\mathcal{U}'},
 F^{\mathrm{et}}_{\ovl{t},\mathcal{U}'})\to
 \Isom(F^{\mathrm{et}}_{\ovl{s},\mathcal{U}},
 F^{\mathrm{et}}_{\ovl{t},\mathcal{U}})$; it will follow that
 $\Isom(F^{\mathrm{et}}_{\ovl{s}}, F^{\mathrm{et}}_{\ovl{t}}) \supset
 \underset{\mathcal{U}}{\limproj} K_\mathcal{U}\neq \emptyset$.

 In fact, it suffices to do so for a cofinal system of $\mathcal{U}$'s,
 which are chosen as follows. Since $S$ is {\it arcwise connected}, there
 is a continuous embedding $I=[0,1]\hookrightarrow S$ with $0\mapsto
 s,\;1\mapsto t$.
 One considers finite open coverings $\mathcal{U} =(U_1,\ldots, U_n)$
 such that
 \begin{equation*}
 U_1\cap I = [0,r_1[,\;\ldots, U_i\cap I=]r_i,t_i[,\;\ldots, U_m\cap
  I=]r_m,1],\;U_{m+1}\cap 
  I=\emptyset,\ldots
 \end{equation*}
 \noindent for some points $r_i<t_{i-1}<r_{i+1}<t_i$ in $I \;(i=2,\ldots,
 m-1)$ and some $ m\leq n$.

 Given $\mathcal{U}$, one chooses $s_i$ in $U_i\cap U_{i+1}\cap I$ (which
 amounts to a real number between $r_{i+1}$ and $t_i$), and a geometric
 point $\ovl{s}_i$ above $s_i\; (i=1,\ldots, m-1)$; one completes this
 collection of geometric points by setting $\ovl{s}_0=\ovl{s},\;
 \ovl{s}_m=\ovl{t}$.  Let us look at the diagram

 \begin{equation*}
 \Cov^{\mathrm{et}}_{S,\mathcal{U}}
 \xrightarrow{\sigma_i}
 \Ind \Cov^{\mathrm{alg}}_{\mathcal{U}_{i+1}}
 \begin{array}{c}
  \xrightarrow{F^{\mathrm{alg}}_{\ovl{s}_i, U_{i+1}}}\\
  \xrightarrow{F^{\mathrm{alg}}_{\ovl{s}_{i+1}, U_{i+1}}}\\
 \end{array}
 \Sets.
 \end{equation*}               
 One has $F^{\mathrm{alg}}_{\ovl{s}_j, U_{i+1}}\circ \sigma_i =
 F^{\mathrm{et}}_{\ovl{s}_i, \mathcal{U} },\;\;j=i,i+1$, whence
 continuous maps 
 \begin{equation*}
 \Isom(F^{\mathrm{alg}}_{\ovl{s}_i,
 U_{i+1}},F^{\mathrm{alg}}_{\ovl{s}_{i+1}, U_{i+1}})\to
 \Isom(F^{\mathrm{et}}_{\ovl{s}_i, \mathcal{U}
 },F^{\mathrm{et}}_{\ovl{s}_{i+1}, \mathcal{U}}).
 \end{equation*} 
 Since algebraic paths exist, $\Isom(F^{\mathrm{alg}}_{\ovl{s}_i,
 U_{i+1}},F^{\mathrm{alg}}_{\ovl{s}_{i+1}, U_{i+1}})$ is a non-empty
 compact set for any $i=0,\ldots, m$.  On composing such isomorphisms for
 $i=0,\ldots, m$, one gets a continuous map
 \begin{equation*}
 \sigma_{\mathcal{U},(\ovl{s}_i)}: \prod_{i=0}^m
  \Isom(F^{\mathrm{alg}}_{\ovl{s}_{i},
  U_{i+1}},F^{\mathrm{alg}}_{\ovl{s}_{i+1}, U_{i+1}})\to
  \Isom(F^{\mathrm{et}}_{\ovl{s},\mathcal{U}},
  F^{\mathrm{et}}_{\ovl{t},\mathcal{U}})
 \end{equation*} 
 whose image is a non-empty compact set $K_\mathcal{U}$.

 In fact, while the map $\sigma_{\mathcal{U},(\ovl{s}_i)}$ depends on the
 choice of the geometric points $\ovl{s}_i$, its image $K_\mathcal{U}$
 does not. Indeed, for any other choice $\ovl{s}'_i$, there is an
 algebraic path
 \begin{equation*}
  \gamma_i:\;F^{\mathrm{alg}}_{\ovl{s}_i, U_{i+1}\cap U_i} \xrightarrow{\sim}
   F^{\mathrm{alg}}_{\ovl{s}'_i, U_{i+1}\cap
   U_i},\;\;\gamma_0=\id,\;\gamma_m=\id.
 \end{equation*} 
 We denote by the same letter the induced algebraic
 paths on $U_i$ and on $U_{i+1}$. Then 
 $\sigma_{\mathcal{U},(\ovl{s}_i)}(\alpha_0,\ldots,\alpha_m) 
 =
 \sigma_{\mathcal{U},(\ovl{s}'_i)}(\gamma_1\alpha_0\gamma_0^{-1},\ldots,
 \gamma_{m}\alpha_m\gamma_{m-1}^{-1})$, whence the independence.

 From this observation, it is straightforward to conclude that if
 $\mathcal{U}'$ refines $\mathcal{U}$, $K_{\mathcal{U}'}$ maps to 
 $K_\mathcal{U} $ under the natural map
 $\Isom(F^{\mathrm{et}}_{\ovl{s},\mathcal{U}'},
 F^{\mathrm{et}}_{\ovl{t},\mathcal{U}'})\to
 \Isom(F^{\mathrm{et}}_{\ovl{s},\mathcal{U}},
 F^{\mathrm{et}}_{\ovl{t},\mathcal{U}})$. This establishes the first
 assertion.

 For the second one (the surjectivity of
 $\Isom(F_{\ovl{s}}^{\mathrm{et}}), F_{\ovl{t}}^{\mathrm{et}}) \to
 \Isom (F_{\ovl{s}}^{\mathrm{top}}, F_{\ovl{t}}^{\mathrm{top}})$), 
 one may argue as follows: let $\ovl{\tilde s}$ be a
 lifting of $\ovl{s}$ to the universal topological covering $\pi:\tilde
 S \to S$. Then $\gamma.\bar{\tilde s}$ is a lifting of $\ovl{t}$
 to the universal topological covering.  Let $\alpha$ be an \'etale path
 between $\bar{\tilde s}$ and $\gamma.\bar{\tilde s}$. Then
 $\ovl{\gamma}:=\pi_\ast(\alpha)$ is an \'etale path between $\ovl{s}$
 and $\ovl{t}$ which maps to the ordinary path $\gamma$ up to homotopy,
 viewed as an isomorphism $F_{\ovl{s}}^{\mathrm{top}}\to
 F_{\ovl{t}}^{\mathrm{top}}$.
\end{proof}
