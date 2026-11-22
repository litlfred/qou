---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-057-132-etale-versus-topological-coverings-again
section_title: "'Etale versus topological coverings (again)."
section_number: 13.2
pages: 118-121
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.961
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::1.2}  

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
