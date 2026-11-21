---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-072-161-review-of-complex-orbifolds
section_title: "Review of complex orbifolds."
section_number: 16.1
pages: 162-165
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.993
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::4.1}

\begin{para}\label{para::4.1.1} There are several variants of the notion 
 of complex orbifold. We follow \cite{calip} and see orbifolds 
 as being locally quotients of a complex manifold by a finite group 
 acting faithfully. More precisely, a {\it complex orbifold} 
 $\mathcal{S}=(\ovl{S}, (Z_i,e_i))$ consists in 
 \begin{itemize}
  \renewcommand{\labelitemi}{\normalfont\bfseries\textendash}
  \item a normal analytic space $\ovl{S}$,
  \item a locally finite collection of irreducible (Weil) divisors
	$(Z_i)$,
  \item a positive integer\footnote{in other variants, one also allows
	$e_i=\infty$. This leads to `parabolic structures' which have
	indeed non-archimedean counterparts in positive characteristic
	(cusps of Drinfeld modular curves...). But we shall be mostly
	interested in non-archimedean orbifolds in characteristic zero,
	where such `parabolic structures' cannot occur. } $e_i$
	attached to each $Z_i$.
 \end{itemize}


\medskip\noindent It is assumed that $\ovl{S}$ is covered by so-called
 {\it orbifold charts}, \ie morphisms  $W 
\xrightarrow{\phi} V \subset \ovl{S} $ where 
 \begin{itemize}
  \renewcommand{\labelitemi}{\normalfont\bfseries\textendash}
  \item $W$ is a complex manifold,
  \item $\phi$ is a (ramified) covering in the sense of \ref{def::1.2.3}
	(\ie $V$ is covered by open subsets $U$ such that $\coprod V_j =
	\phi^{-1}U \to U$ and the restriction of $\phi$ to every $V_j$
	is finite),
  \item except for a closed subset $\Sigma$ of codimension $2$ in $V$,
	$\phi$ is \'etale above $V\setminus (V\cap\bigcup Z_i)$ (hence
	induces a topological covering of $V\setminus (V\cap\bigcup
	Z_i)$), and is {\it ramified with index $e_i$ above
	$Z_i$}.\footnote{it is easily seen that this definition is equivalent
	to that of \cite{calip}, using {\it loc.~cit.} 14.2.}
 \end{itemize}

\medskip Note that if $s$ is a non-singular point of $\ovl{S}$ not
 contained in $\bigcup Z_i$, then any smooth open neighborhood of $s$ in
 $\ovl{S}$ disjoint from $\bigcup Z_i$ provides an orbifold chart around
 $s$. Hence we may and shall assume that $\Sigma $ is contained in
 $\bigcup Z_i\cup \ovl{S}^{\mathrm{sing}}$ (where $\ovl{S}^{\mathrm{sing}}$ denotes the
 set of singular points of $\ovl{S}$).
 
 \noindent We shall often write
 $Z=\bigcup Z_i\cup
 \ovl{S}^{\mathrm{sing}}$, and
 $S=\ovl{S}\setminus Z$ (which is a manifold).  

\medskip\noindent {\it Remark.} By shrinking the $W$'s, one can assume
 that they are open subsets of $\C^n$; this matches with the conventional
 use of the word `chart'. However, we do not impose here this condition
 which would have no non-archimedean counterpart.


\end{para}

\begin{para}\label{para::4.1.2} A {\it morphism of orbifolds}
 $f:\mathcal{S}'\to \mathcal{S}$ is a morphism $\ovl{S}'\to \ovl{S}$, such
 that $\ovl{S}'$ is covered by orbifold charts  $\phi': W'\to V'$ with
 the property that $f\circ \phi'$ factors through some orbifold 
 chart $\phi:W\to V$ of $\mathcal{S}$: $f\circ \phi'=\phi\circ f'$ 
(for some morphism $f'\colon W'\to W$).

 \medskip\noindent {\it Example.}  Let $(\ovl{S}, (Z_i,e_i)_{i\in I})$ be
 an orbifold, and let $J\subset I$ be the subset of indices for which
 $e_i>1$. Then the identity of $\ovl{S}$ induces an isomorphism
 $(\ovl{S}, (Z_i,e_i)_{i\in I})\cong (\ovl{S}, (Z_i,e_i)_{i\in J})$. In
 other words, one can `forget' the divisors with index $e_i=1$.
 
 \noindent Considering complex manifolds as orbifolds with an empty
 collection of divisors ($S=\ovl{S}$), one can embed the 
 category of complex manifolds as a full subcategory of the category of
 complex orbifolds.

 \noindent It will be convenient to attach to any irreducible divisor
 $D\subset \ovl{S}$ an index $e_D\in \Z_{>0}$ which is $e_i$ if
 $D=Z_i$ and $1$ if $D$ is none of the $Z_i$'s.


\end{para}

\begin{para}\label{para::4.1.3} A morphism $f$ is called an {\it
 orbifold-covering} if it is a covering in the sense of \ref{def::1.2.3}
 and for any 
 orbifold chart $\phi': W'\to V'$ of $\mathcal{S}'$, $f\circ\phi': W'\to
 V=f(V')$ is an orbifold chart of $\mathcal{S}\;$ (in
 loose words: any lifting $f'$ as in \ref{para::4.1.2} is 
 \'etale).  
 
 \medskip\noindent The restriction of $f$ above $S$ is then an \'etale
 covering: indeed, this is clear except above
 a closed subset of codimension $\geq 2$ in $S$, thus above the whole of
 $S$ by purity since $S$ is smooth.
 
 \medskip\noindent {\it Example.} $(\A^1, (0,e'))
 \xrightarrow{z\mapsto z^n} (\A^1, (0,e)) $ is
 a morphism if and only if $e| ne'$, and is an orbifold-covering if
 and only if 
 $e=ne'$.   
  
\medskip \noindent {\it Remark.} Let $f:\mathcal{S}'\to \mathcal{S}$ be
 an orbifold-covering. As we just saw, we may assume 
 that all the indices $e'_i,e_j$ are $>1$. Then $f(Z')\subset Z$ and
 $f^{-1}(S)\subset S'$.
\end{para}

\begin{para}\label{para::4.1.4} Following Thurston, an orbifold is said to be
 good or {\it uniformizable} if it admits a {\it global} orbifold chart
 (\ie with $V=\ovl{S}$).  In that case, there exists a {\it universal} 
 global orbifold chart, called the {\it universal orbifold-covering} (it
 is indeed an orbifold-covering in the above sense); its underlying space
 is a simply-connected complex manifold if $\ovl{S}$ is connected.
 
 \medskip\noindent {\it Example.} By a classical result due to Fox,
 $(\P^1, (\zeta_i,e_i)_{i=0,\ldots, n})$ is uniformizable if and only if
 $n\geq 2$ or ($n=1$ and $e_0=e_1$). Under these conditions, 
 there exist algebraic global charts which are finite coverings of $\P^1$. 
\end{para}

\begin{para}\label{para::4.1.5} It is proved in {\it loc.~cit.} that orbifold
 charts are locally unique. Apart from a subset of codimension $2$,
 they are given in local coordinates around $\phi^{-1}(Z_i)$ by:
 $(z_1,z_2,\ldots, z_n)\mapsto (z_1^{e_i},z_2,\ldots, z_n)$.
 
 \noindent It follows that there exist orbifold charts of the form
 $W\to V=W/G$ ({\it loc.~cit.} 14.6), where $W$ is an
 open subset of $\C^n$ stable under a finite group $G$ of linear
 transformations.
\end{para}

\begin{para}\label{para::4.1.6} Let $\mathcal{S}=(\ovl{S}, (Z_i,e_i))$ be a
 connected orbifold, and let $\Gamma$ be a discrete group acting
 faithfully and properly by automorphisms on $\mathcal{S}$. The {\it orbifold
 quotient} $\mathcal{S}/\Gamma$ is defined as follows: the underlying
 analytic space is $\ovl{S}/\Gamma$. The ramifications divisors are the
 images of the $Z_i$'s, and the irreducible divisors $D$ with
 non-trivial fixer $\Gamma_D$; the
 latter are endowed with the multiplicity $e_D.| \Gamma_D|$.

 Note that the projection $\mathcal{S}\to \mathcal{S}/\Gamma$ is an
 orbifold-covering.
\end{para}

\begin{para}\label{para::4.1.7} One of the main applications of complex
 orbifolds is to represent moduli problems for isomorphism classes of
 objects with finite automorphism group. We have already alluded to this
 in II.\ref{sub:1.1}.  Here we shall content ourselves with examining
 the case of complex elliptic curves.

 \noindent Let $H$ be the subgroup of $SL_3(\R)$ consisting
 of matrices of the form
 $\begin{pmatrix}
 1&x_1&x_2\\ 0&a&b\\ 0&c&d
  \end{pmatrix}$ (this is a
 semi-direct product $SL_2(\R)\ltimes\R^2$).  It acts on the product
 $\mathfrak{h}$ 
 $\times\C$ of the Poincar\'e upper half plane $\mathfrak{h}$ and $\C$ by
 the rule 
 \begin{equation*}
  \begin{pmatrix}
   1&x_1&x_2\\0&a&b\\0&c&d
  \end{pmatrix}.
  (\tau, v)=\Bigl(\frac{a\tau+b}{c\tau +d},\frac{v+x_1\tau+x_2}{c\tau+d}\Bigr).
 \end{equation*}
 As is well-known, elliptic curves $E$ together with a symplectic isomorphism
 $\mathrm{H}_1(E,\Z)\cong \Z^2$ are classified by points of the
 Poincar\'e upper half plane $\mathfrak{h}$, the universal object being
 the quotient of $\mathfrak{h}\times\C$ by the action of the subgroup 
 $1.\Z^2\subset H$ (mapping to $\mathfrak{h}$ through the first projection). 

 Let $\Ker(SL_2(\Z)\to SL_2(\Z/N\Z))$ be the full congruence group of
 level $N$, $\Gamma(N)$ its image in $PGL(2)$, and $\tilde\Gamma(N)$ be
 the subgroup 
 \begin{equation*}
  \Ker(SL_2(\Z)\to SL_2(\Z/N\Z)).\Z^2\subset H.
 \end{equation*}
 For $N\geq 3$, the group $\tilde \Gamma(N)$ is
 torsion-free and acts freely on $\mathfrak{h}\times\C$; elliptic curves 
 together with a level $N$ structure (\cf II.\ref{para:1.1.2}) are
 classified by $\mathfrak{h}/\Gamma(N)$, the universal object being
 $(\mathfrak{h}\times\C)/\tilde \Gamma(N)\to \mathfrak{h}/\Gamma(N)$. 
 
 This still holds for $N=1$ or $2$, provided one interprets these
 quotients as orbifold quotients. For $N=2$, the element 
  $\begin{pmatrix}1&&0\\ &-1&\\ 0&&-1 \end{pmatrix} \in
 \tilde \Gamma(N)$ of order $2$ has fixed divisors in
 $\mathfrak{h}\times\C$: the quotient of
 $\{(\tau,x_1\tau+x_2) \mid x_1,x_2\in (\frac{1}{2}\Z)^2\}$ by $\tilde
 \Gamma(N)$, which is a disjoint union $\coprod_1^4 Z_i$ of four
 `horizontal' curves (horizontal with respect to the projection to 
 $\mathfrak{h}/\Gamma(2)=\P^1\setminus\{0,1,\infty\}$); they have the
 index $e_i=2$ (the order of the fixer).
 
This orbifold is uniformizable: the Legendre elliptic pencil provides a
global orbifold chart. Note however that, as an analytic variety,
$\mathfrak{h}\times\C/\tilde \Gamma(2)$ is a not an elliptic surface but
a $\P^1$-bundle.

The case $N=1$ is similar: $\mathfrak{h}/\Gamma(1)=\A^1$ is the $j$-line. It should be considered as an orbifold, with
divisor $\{j=0 \,{\rm(index \;3)} ,\;j=1728\,{\rm(index \;2)} \}$. In addition to the image of the horizontal divisors
$Z_i$ on $\mathfrak{h}\times\C/\tilde \Gamma(1)$, there are three vertical divisors with index $2$, and two vertical
divisors with index $3$.  


\end{para}

\begin{para}\label{para::4.1.8} More generally, let us consider a Shimura
 variety of PEL type as in II.\ref{para:1.2.4}.  Recall from {\it
 loc.~cit.} the commutative diagram
\begin{equation*}
\begin{CD}
 \tilde S @>\mathcal{P}>> \mathcal{D}\\
 @V\mathcal{Q}VV @VV\mathcal{Q}V\\
 S @>\mathcal{P}>> \mathcal{D}/\Gamma
\end{CD}
\end{equation*}
where $S$ is a component of the Shimura variety, the horizontal maps are
 {\it isomorphisms}, and $\Gamma$ is a congruence subgroup. If $\Gamma$
 has torsion, it is appropriate to consider $S$ as an orbifold quotient 
 (defined by $\mathcal{Q}$ as in \ref{para::4.1.6}). 
\end{para}
