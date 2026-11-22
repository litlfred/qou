---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-075-164-non-archimedean-orbifolds
section_title: "Non-archimedean orbifolds."
section_number: 16.4
pages: 167-170
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.924
latex_coverage_ratio: 0.798
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::4.4}

\begin{para}\label{para::4.4.1} We now work over a complete non-archimedean
 field $K$. The definition of orbifolds is parallel to the one 
 which we have selected in the complex situation. Being mainly interested
 in orbifolds which are quotients of 
 manifolds by finite groups, it is natural to replace everywhere \'etale
 (= topological) coverings in the complex case by {\it temperate}
 \'etale coverings in the non-archimedean context.

 \medskip\noindent A {\it $K$-orbifold} $\;\mathcal{S}=(\ovl{S},
 (Z_i,e_i))$ consists in 
 \begin{itemize}
  \renewcommand{\labelitemi}{\normalfont\bfseries\textendash}
  \item a normal $K$-analytic space $\ovl{S}$ (in the sense of
	Berkovich),
  \item a locally finite collection of irreducible divisors $(Z_i)$,
  \item a positive integer $e_i$ attached to each $Z_i$.
 \end{itemize}

 \noindent It is assumed that $\ovl{S}$ is covered by so-called
 {\it orbifold charts}, \ie morphisms
 $W \xrightarrow{\phi} V \subset \ovl{S} $ where 

\begin{itemize}
 \renewcommand{\labelitemi}{\normalfont\bfseries\textendash}
 \item $W$ is a $K$-manifold,
 \item $\phi$ is a (ramified) covering in the sense of \ref{def::1.2.3}
       (\ie $V$ is covered by open subsets $U$ such that 
       $\coprod V_j = \phi^{-1}U \to U$ and the restriction of $\phi$ to
       every $V_j$ is finite),
 \item except for a closed subset $\Sigma$ of codimension $2$ in $V$,
       $\phi$ restricts to a {\it temperate} \'etale covering 
       above $V\setminus (V\cap\bigcup Z_i)$, and is {\it ramified with index
       $e_i$ above $Z_i$}.
\end{itemize}  

 \medskip Here again, we may and shall assume that that $\Sigma $ is
 contained in $\bigcup Z_i\cup \ovl{S}^{\mathrm{sing}}$ and set
 $Z=\bigcup Z_i\cup \ovl{S}^{\mathrm{sing}},\;S=\ovl{S}\setminus Z$
 (which is a $K$-manifold).
\end{para}

\begin{rems}
  (i) At this point, because the notion of orbifold is local, it would
 not change if we had modified the definition of orbifold charts by
 replacing `temperate \'etale' by `finite \'etale' or by `\'etale'.  In
 contrast, we insist that orbifold charts are defined in terms of
 temperate coverings.
 
 (ii) Since we only prescribe the ramification indices and not
 the ramification groups, this notion of orbifold is 
 only reasonable in the tame case, \ie when $\ch(K) \nmid e_i$.  We 
 shall be mostly interested in the characteristic $0$ case.

 (iii) If $\dim \ovl{S} = 1$, then $S=\ovl{S}\setminus \bigcup Z_i$.
\end{rems}

\begin{para}\label{para::4.4.2} A {\it morphism of orbifolds}
 $f:\mathcal{S}'\to \mathcal{S}$ is a morphism $\ovl{S}'\to \ovl{S}$, such
 that $\ovl{S}'$ is covered by orbifold charts  $\phi': W'\to V'$ with
 the property that $f\circ \phi'$ factors through some orbifold chart
 $\phi:W\to V$ of $\mathcal{S}$: $f\circ \phi'=\phi\circ f'$.

 \medskip\noindent {\it Example.} Let $(\ovl{S}, (Z_i,e_i)_{i\in I})$ be
 an orbifold, and let $J\subset I$ be the subset of indices for which
 $e_i>1$. Then the identity of $\ovl{S}$ induces an isomorphism
 $(\ovl{S}, (Z_i,e_i)_{i\in I})\cong (\ovl{S}, (Z_i,e_i)_{i\in J})$. In
 other words, one can `forget' the divisors with index $e_i=1$.

 \noindent Considering $K$-manifolds as orbifolds with an empty
 collection of divisors ($S=\ovl{S}$), one can embed {\it the category of 
 $K$-manifolds as a full subcategory of the category of $K$-orbifolds}.

\noindent It will be convenient to attach to any irreducible divisor
 $D\subset \ovl{S}$ an index $e_D\in \Z_{>0}$ which is $e_i$ if
 $D=Z_i$ and $1$ if $D$ is none of the $Z_i$'s.
\end{para}

\begin{para}\label{para::4.4.3} A morphism $f$ is called an
{\it orbifold-covering} if it is a covering in the sense of
 \ref{def::1.2.3} and 
 for any orbifold chart $\phi': W'\to V'$ of $\mathcal{S}'$, $f\circ
 \phi': W'\to V=f(V')$ is an orbifold chart of $\mathcal{S}\;$ (note that if
 $\mathcal{S}'$ and $\mathcal{S}$ are just $K$-manifolds, an orbifold-covering
 amounts to a temperate \'etale covering, by our definition of orbifold
 charts).
 
 \noindent Orbifold-coverings of $\mathcal{S}$ form a category in an obvious
 way, denoted by $\Cov_\mathcal{S}$.
 
\medskip\noindent The restriction of $f$ above $S$ is then an \'etale
 covering: indeed, this is clear except above a closed subset of
 codimension $\geq 2$ in $S$, thus above the whole of $S$ by purity since
 $S$ is smooth.
 However, we do not know in general whether it
 is temperate (due to the non-local nature of the definition of
 temperate coverings).
 
\medskip\noindent {\it Example.} Assume that $\ch(K) \nmid n$. Then
 $(\A^1, (0, e')) \xrightarrow{z\mapsto z^n} (\A^1,
 (0, e)) $ is a morphism of orbifolds if and only if $e| ne'$, and is
 an orbifold-covering if and only if $e=ne'$.   

 \medskip \noindent {\it Remark.} Let $f:\mathcal{S}'\to \mathcal{S}$ be an
 orbifold-covering. As we just saw, we may assume that all the indices
 $e'_i,e_j$ are $>1$. Under this assumption, $f(Z')\subset Z$ and
$f^{-1}(S)\subset S'$.
\end{para}

\begin{para}\label{para::4.4.4} An orbifold is said to be {\it
 uniformizable}\footnote{we avoid the terminology `good' in 
 order to prevent confusion with good spaces in the sense of Berkovich,
 \cf last section.} if it admits a {\it global} orbifold chart.
 
 However, {\it universal global orbifold charts do not exist}; this is
 no surprise: there is no universal temperate covering of a
 $K$-manifold, except in trivial cases. For the same reason, {\it
 orbifold charts are not locally unique}.
 
 \medskip Let $f:\mathcal{S}'\to \mathcal{S}$ be an orbifold-covering of a
 uniformizable orbifold $\mathcal{S}$. Then the {\it restriction of $f$ to
 $f^{-1}(S)$ is a temperate \'etale covering} of $S$.

 Indeed, let $W\to \ovl{S}$ be a global orbifold chart. Then
 $W_{|S}\times_S f^{-1}(S)\to f'(W'_{|S}\times_S f^{-1}(S))= f^{-1}(S)$
 is an orbifold chart for $\mathcal{S}'$, hence $W_{| S}\times_S
 f^{-1}(S)\to S$ is an orbifold chart for $\mathcal{S}$. Since its image is
 $S$ itself, it is a temperate covering of $S$, of which $f^{-1}(S)\to S$ is 
 a quotient.

\medskip\noindent {\it Example.} Assume that $K$ is algebraically closed
of characteristic zero. Then $(\P^1, (\zeta_i, e_i)_{i=0,\ldots, n})$
is uniformizable if and only if $n\geq 2$ or ($n=1$ and $e_0=e_1$),
just as in the complex case. This actually follows from the complex
 case: one may assume that $K$ has the same cardinality as $\C$, choose
 an abstract isomorphism $K\cong \C$, and use the fact that in the
 complex case, one can find a global algebraic orbifold chart which is a
 finite ramified covering of $\ovl{S}$.
\end{para}

\begin{para}\label{para::4.4.5} Let us again assume that $K$ is of
 characteristic zero. Let $\mathcal{S}=(\ovl{S}, (Z_i,e_i))$ be a
 connected $K$-orbifold, and let $\Gamma$ be a virtually free discrete group acting
 faithfully and properly by automorphisms on $\mathcal{S}$.  The {\it
 orbifold quotient} $\mathcal{S}/\Gamma$ is defined as in the complex
 situation: the underlying analytic space is $\ovl{S}/\Gamma$. The
 ramification divisors are the images of the $Z_i$'s, and the
 irreducible divisors $D$ with non-trivial fixer $\Gamma_D$; the latter
 are endowed with the multiplicity $e_D.| \Gamma_D|$.
 Note that the projection $\mathcal{S}\to \mathcal{S}/\Gamma$ is an
 orbifold-covering.

 Interesting examples with $\ovl{S}$ open in $\P^1$ are discussed in
 \cite{van92:_discr_mumfor}. 
\end{para}

\begin{para}\label{para::4.4.6} One of the applications of $K$-orbifolds would
 be to represent moduli problems for isomorphism classes of objects with
 finite automorphism groups.

 Typical instances occur in the context of $p$-adic uniformization of
 Shimura varieties. Let us briefly mention how.  Recall from
 II.\ref{sub:7.2}, \ref{sub:7.3}
 the following basic commutative diagram

 \begin{equation*}
  \begin{CD}
   \mathcal{M}^0 @>\mathcal{P}>> \mathcal{D}\\
   @V\mathcal{Q}VV @VV\mathcal{Q}V\\
   S @>\mathcal{P}>> \mathcal{D}/\Gamma
  \end{CD}
 \end{equation*}
$S$ is a tube-like domain in the $p$-adic
 analytification of a Shimura variety, the horizontal maps are \'etale,
and $\Gamma$ is an arithmetic subgroup in the semi-simple group
$\ovl{G}^{\mathrm{ad}}$. Under the assumption that $\Gamma$ is small
enough, the maps $\mathcal{Q}$ are topological covering maps.

If one drops that assumption, one has to consider $S$ as an orbifold
quotient (defined by $\mathcal{Q}$ as in \ref{para::4.4.5}). This is
 especially relevant 
in the case of global uniformization, \ie when $S$ is a connected
component of the Shimura variety.

The fake projective planes of Mumford, Ishida, Kato, provide interesting
examples of this situation, \cf II.\ref{sub:7.5} and \cite{opuofpp}.
We shall see several other instances in the sequel.
\end{para}
