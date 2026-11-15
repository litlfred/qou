---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-070-155-examples-and-applications
section_title: "Examples and applications."
section_number: 15.5
pages: 156-162
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.961
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::3.5} 

\begin{para}\label{para::3.5.1} For any full subcategory $\Cov^\bullet_S$ of
 $\Cov^{\mathrm{et}}_S$ which is stable under 
 taking connected components, fiber products  and quotients, we have seen
 that there is a natural continuous homomorphism 
 \begin{equation*}
  \pi_1^{\mathrm{et}}(S, \ovl{s})\to \pi_1^\bullet(S, \ovl{s}) 
 \end{equation*}
 with dense image (\ref{cor::1.4.8}). Any discrete representation
 of $ \pi_1^\bullet(S, \ovl{s})$ gives rise to a 
 discrete representation of $ \pi_1^{\mathrm{et}}(S, \ovl{s})$ with the
 same coimage. It follows that the \'etale Riemann-Hilbert 
 functor induces a fully faithful functor 
 \begin{equation*}
  \left\{
   \begin{matrix}
    \text{discrete fin. dim.}\\
    \text{$\pi_1^\bullet(S,\ovl{s})$-representations}
   \end{matrix}
   \right\}
   \xrightarrow{RH^\bullet}
   \left\{
    \begin{matrix}
     \text{vector bundles with integrable}\\
     \text{connection $(M,\nabla)$ on $S$}
    \end{matrix}
   \right\}.
 \end{equation*}
 Note that the monodromy group defined in \ref{para::3.4.7} coincides
 with the image 
 of $\pi_1^\bullet(S, \ovl{s})$.  We shall discuss the avatars
 $RH^\bullet$ in the cases of $\Cov^{\mathrm{top}}_S$,
 $\Cov^{\mathrm{alg}}_S$, $\Cov^{\mathrm{loc.alg}}_S$,
 $\Cov^{\mathrm{temp}}_S$.
\end{para}

\begin{para}\label{para::3.5.2} The functor $RH^{\mathrm{top}}$ was studied in
 I.\ref{sub-connection} (in the case $K=\C_p$). Its essential image consists 
 of connections which satisfy `Cauchy's theorem' at every (possibly
 non-classical) point of $S$, or equivalently, which have a full set of
 multivalued analytic solutions, or else, such that 
 $M^\nabla$ is a locally constant sheaf on the topological space $S$.
\end{para}

\begin{para}\label{para::3.5.3} The essential image of the functor
 $RH^{\mathrm{alg}}$ consists of objects $(M,\nabla)$ such that
 $M_{\mathrm{et}}^\nabla$ becomes constant on some finite \'etale
 covering of $S$.

 Let us assume for instance that $S$ is affinoid with good reduction
 $S^0$, and that $K$ is a finite extension of
 $\widehat{\Q_p^{\mathrm{ur}}}$ as in 
 I.\ref{sub-r-and-unit-root}. Then among the finite representations of $
 \pi_1^{\mathrm{alg}}(S, \ovl{s}) $, one can distinguish those which
 factor through $ \pi_1^{\mathrm{alg}}(S_0, \ovl{s}_0) $. The
 corresponding connections underlie overconvergent unit-root isocrystals
 with finite global monodromy. We have seen a standard example in
 I.\ref{exa-dwork-exp}, given by the differential equation
 $\frac{d}{dz} y = -\pi y$ 
 on $S=\matheur{D}(0,1^+)$, which is trivialized over an Artin-Schreier covering.
 
 Let us now consider a case of bad reduction, namely the case of an
 annulus $S_r=\mathcal{C}(]1,r[),\;r\in | K|, 
 r>1$ over any discretely valued $p$-adic field $K$. Let $\mathcal{R}$ be
 the Robba ring at infinity. Then $RH^{\mathrm{alg}}$ induces a 
 functor
 \begin{equation*}
  \{\text{finite representations of $\pi_1^{\mathrm{alg}}(S_r,
   \ovl{s})$}\}
   \to \{\text{$\mathcal{R}$-differential modules}\}.
 \end{equation*}
 In relation to the local monodromy theorem \ref{coj::3.3.5}, it would be very
 interesting to understand the essential image of this functor as $r\to
1^+$. Note however that there is a difficulty with base-points in
passing to the limit $r\to 1^+$ (the problem disappears if one considers
only abelian representations).

Nevertheless, any $\mathcal{R}$-differential module $M$ extends to a
vector bundle $(M_r,\nabla_r)$ with connection on some $S_r$. Let us
assume that $M$ is semisimple and has a Frobenius structure.

If $M$ is tame, then \ref{thm::3.2.8} ensures that $M$ is in the image
of the above functor
\begin{equation*}
 \{\text{finite $\pi_1^{\mathrm{alg}}(S_r, \ovl{s})$-representations}
  \}\to \{\text{$\mathcal{R}$-differential modules}\}
\end{equation*}
for $r$ close enough to
$1$. The local monodromy theorem \ref{coj::3.3.5} implies the same if
$M$ is wild, 
although the monodromy representation might be non-abelian in this case,
as \ref{thm::3.3.6} shows.
\end{para}

\begin{para}\label{para::3.5.4} The essential image of the functor
 $RH^{\mathrm{loc.alg}}$ consists of objects $(M,\nabla)$ such that for every
 compact subdomain $W\subset S$, $(M_{\mathrm{et}}^\nabla)_{| W}$ becomes
 constant on some finite \'etale covering of $W$.
 Although not explicitly introduced in \cite{ramero98}, it is clear that
 these connections played an important heuristic role in that paper,
 especially those coming from abelian representations of the locally
 algebraic fundamental group (1.5).

 The basic example is $(\mathcal{O}_{\A^1}, d-1)$ over $\C_p$ (with
 solution $e^z$). It is trivialized by the logarithmic \'etale covering
 of ${\A^1}$.
 
 Similarly, for any ramified polynomial $P(z^{1/m})$, the differential
 equation with basic solution $e^{P(z^{1/m})}$ is trivialized over a
 locally algebraic \'etale covering of a sufficiently small punctured
 disk $\matheur{D}_{\C_p}(\infty,\epsilon)^\ast$ around $\infty$ (the
 logarithmic 
 covering of a Kummer covering). By \ref{para::3.1.5}, we see that any
 differential 
 equation with polynomial coefficients --- or more generally meromorphic
 singularity at $\infty\;$ --- with {\it rational} formal exponents at
 $\infty$, and with no logarithm in the formal solutions $\hat y$ (\cf
 \ref{para::3.1.2}), corresponds to an object in the image of the
 locally algebraic Riemann-Hilbert functor
 \begin{equation*}
  \left\{
   \begin{matrix}
    \text{finite dimensional}\\
    \text{$\pi_1^{\mathrm{loc.alg}}(\matheur{D}(\infty,\epsilon)^\ast,
    \ovl{s})$-representations}
   \end{matrix}
  \right\}
  \to
  \{\text{$\mathcal{O}(\matheur{D}(\infty,\epsilon)^\ast)$-differential
  modules}\}
 \end{equation*}
 for $\epsilon$ small enough.

 There is a certain analogy between the logarithmic \'etale
 covering of $\matheur{D}_{\C_p}(\infty,\epsilon)^\ast$ and the {\it
 real blow-up} of $\matheur{D}_{\C}(\infty,\epsilon)^\ast$ which plays
 such an important role in 
 the study of irregular singularities of complex differential
 equations. In both cases, the point at infinity becomes a limiting
 circle\footnote{L. Ramero points out that the change from analytic to
 \'etale topology is essential in the $p$-adic case, while in the
 complex case, the real blow-up corresponds to completion for a
 different uniform structure of the punctured disk with no change of the
 topology.}.

\medskip Let us return to a general vector bundle $(M,\nabla)$ with
 connection on $\matheur{D}(\infty,1^-)^\ast$ which extends to a vector bundle
 with meromorphic connection at $\infty$. We assume that it is has a
 Frobenius structure near the unit circle, and that the formal exponents
 at infinity are rational. Regarding problem \ref{para::3.2.9}, a
 natural question is:
\end{para}

\begin{que}\label{que::3.5.5} Under which further conditions, if any,
 does there exist a locally algebraic covering of
 $\matheur{D}(\infty,1^-)^\ast$ 
 over which the connection becomes an iterated extension of trivial
 connections?
\end{que}
At any rate, in the cases where this holds, this would let Ramero's
locally algebraic fundamental group play the same role, 
over $\C_p$, as Ramis' wild fundamental group (over $\C$) in the local
study of meromorphic irregular singularities.

\begin{para}\label{para::3.5.6} The essential image of the functor
 $RH^{\mathrm{temp}}$ consists of objects $(M,\nabla)$ such that 
 $M_{\mathrm{et}}^\nabla$ becomes constant on some temperate \'etale
 covering of $S$.  This implies that there is a finite \'etale Galois
covering $f:\;T\to S$ such that the pull-back
$(M',\nabla')=f^\ast(M,\nabla)$ has a full set of multivalued analytic
solutions, \ie $M^{\prime \nabla'}$ is locally constant. Let $G$ be the group
$\Aut_S\,T$, and set $n=| G| $.
 
Assume that there are $n$ distinct $K$-rational points $t_i$ in $T$
 lying above $s$. Then the monodromy group admits the following {\it
 concrete interpretation}: 

\noindent let $\alpha_{ij}$ be a Berkovich path (up to homotopy)
connecting $t_i$ to $t_j$. Then $f_\ast(\alpha_{ij})\in
\pi_1^{\mathrm{temp}}(S,\ovl{s})$. When $i,j$ and $\alpha_{ij}$ vary,
they generate the image $\Aut_S\,\tilde T$ of
$\pi_1^{\mathrm{temp}}(S,\ovl{s})$ (note that, varying $j$, they
generate the finite quotient $G$). It follows that the monodromy group
consists of the images of the $f_\ast(\alpha_{ij})$'s in $GL(M_{(s)})$
by the monodromy representation.

Therefore, except for the occurrence of the finite \'etale covering, the 
picture is quite similar to the complex situation.
 

\end{para}

\begin{pro}\label{pro::3.5.7} Let $S=\A^1\setminus\{\zeta_1,\ldots,
 \zeta_m\}$. Assume\footnote{this very strong assumption is rarely met
 in practice.} that the residue characteristic $p$ of $K$ does not
 divide $n$. Then:
 \begin{enumerate}
  \renewcommand{\theenumi}{\alph{enumi}}
  \item for any open or closed disk $\matheur{D}\subset S$, the restriction of
	$\nabla$ to $\matheur{D}$ is trivial (\ie has a full set of solutions); in
	particular, $\nabla$ satisfies the Robba condition;
  \item for any open or closed annulus
	$\mathcal{C}\subset S$, the pull-back of $\nabla$ to the Kummer
	covering of $\mathcal{C}$ of degree $n$ is trivial.
 \end{enumerate}

 In particular,
 $p$-adic exponents in the sense of Christol-Mebkhout exist (in any
 annulus which does not contain any $\zeta_i$), and they are rational
 numbers with denominator $n$ (or a divisor of $n$).
\end{pro}

\begin{proof}
 One is immediately reduced to considering closed disks and
 annuli. We know the pull-back of $\nabla$ to $\tilde T$ is trivial. Let
 $\matheur{D}'$ (\resp $\mathcal{C}'$) be a connected component of $\matheur{D}\times_S
 \tilde T$ (\resp $\mathcal{C}\times_S \tilde T$). Because $n$ is assumed
 to be prime to $p$, the covering $\matheur{D}'\to \matheur{D}$ is trivial (\resp is a Kummer
 covering of degree dividing $n$), \cf \cite[6.3.3, 6.3.5]{ecfnas} (taking
 into account the fact that disks and annuli are simply-connected). The
 assertions follow.
\end{proof}

\medskip\noindent {\it Example.} (see also the example at the end of
\ref{lem::2.1.2}). Let $K$ be a $p$-adic field for any odd $p$. 
Let $T=E\setminus E[2]$ be a Tate curve deprived from its four
$2$-torsion points (assumed to be $K$-rational), written in 
Legendre form: 
\begin{equation*}
 y^2=x(x-1)(x-\lambda),\quad |\lambda(\lambda -1)|\neq 1.
\end{equation*}
Let $f$ be the projection from $T$ to $S=\A^1\setminus
\{0,1,\lambda \}$.
Here $\tilde T$ is of the form $\G_m\setminus \pm(\sqrt q)^\Z$, and
$T\cong \tilde T/ q^\Z $.

The sum of the canonical one-dimensional $K$-linear representation of
$q^\Z$ ($q$ acting by multiplication by a factor $q$) and its dual
extends to a representation of the semi-direct product of $q^\Z$ and
$\Z/2\Z$ (which is the Galois group of the covering $\tilde T\to S$). On
can choose the local monodromies at $0,\lambda, 1,\infty$ respectively
in such a way that they correspond to the matrices
\begin{equation*}
 \begin{pmatrix}0&1\\1&0\end{pmatrix},
 \begin{pmatrix}0&1\\1&0\end{pmatrix},
  \begin{pmatrix}0&q\\q^{-1}&0\end{pmatrix},
  \begin{pmatrix}0& q^{-1}\\q&0\end{pmatrix}
\end{equation*}
respectively. It is
then easy to check that the monodromy around an annulus surrounding $0$
and $\lambda$ alone ($|\lambda|$ being assumed $<1$ for convenience) is
trivial: the $p$-adic exponents are zero.
 
\begin{para}\label{para::3.5.8} Much more interesting examples arise in the
 context of $p$-adic period mappings. We place ourselves in the 
 setting of  II.\ref{sub:7.2}. Assuming the congruence subgroup sufficiently
 small, the picture was the following: 

\begin{center}
 \begin{picture}(150,90)(0,-5)
  \put(10,60){\makebox(0,0)[c]{$\til{S}$}}
  \put(25,60){\vector(1,0){20}}
  \put(25,45){\vector(1,-1){20}}
  \put(60,60){\makebox(0,0)[c]{$\mathcal{M}$}}
  \put(60,45){\vector(0,-1){20}}
  \put(60,10){\makebox(0,0)[c]{$S$}}
  \put(115,60){\makebox(0,0)[c]{$\mathcal{D}$}}
  \put(75,60){\vector(1,0){25}}
  \put(88,65){\makebox(0,0)[c]{${}^\mathcal{P}$}}
  \put(115,45){\vector(0,-1){20}}
  \put(75,10){\vector(1,0){20}}
  \put(115,10){\makebox(0,0)[c]{$\mathcal{D}/\Gamma$}}
 \end{picture}
\end{center}
where $S$ was a suitable connected `tube-like' domain
 in the Shimura variety $\Sh_{\C_p}$ ($\mathcal{M}^0$ was a deformation
 space for $p$-divisible groups quasi-isogenous to a fixed one, and
 $\mathcal{D}$ was the period domain).

 The period mapping turned out to be expressable in terms of quotients of
 solutions of the Gauss-Manin connection (on $S$), 
 and the Gauss-Manin connection was trivializable on $\mathcal{M}^0 $,
 hence on $\tilde S$ (II.\ref{cor:7.2.6}).

 \medskip Let us now abandon the assumption that the congruence subgroup
 is sufficiently small. Then a similar picture holds 
 true: $\Gamma$ is now only virtually torsion-free, and the covering
 $\mathcal{M}^0\to S $ is now ramified. By removing the 
 singularities, one obtains a {\it temperate \'etale covering}, which
 trivializes the Gauss-Manin 
 connection (using II.\ref{cor:7.2.6} after passing to a suitable
 finite \'etale covering). It follows that the 
 {\it Gauss-Manin connection (restricted to $S$ deprived from the
 singularities) is in the image of the temperate 
 Riemann-Hilbert functor}. 

 The situation is therefore similar the the complex one, except that $S$
 is only a small domain in the Shimura variety in 
 general. The most favorable situation occurs in the case of global
 uniformization (II.\ref{sub:7.3}), \ie when $S$ is a component of $\Sh$.
\end{para}

\begin{para}\label{para::3.5.9} Let us now give a criterion for a connection
 in the image of $RH^{\mathrm{et}}$ to be in the image of $RH^{\mathrm{temp}}$.
\end{para}

\begin{pro}\label{pro::3.5.10} Let $\rho:
\pi_1^{\mathrm{et}}(S,\ovl{s}) \to GL(V)$ be a finite-dimensional
 discrete representation (corresponding to an \'etale local system 
 $\mathcal{V}$). Let us consider the following conditions:
 \begin{enumerate}
  \renewcommand{\theenumi}{\alph{enumi}}
  \item $\rho$ factors through a discrete representation of
	$\pi_1^{\mathrm{temp}}(S,\ovl{s})$,
  \item $\Im \rho$ is virtually torsion-free,
  \item $\Im \rho$ is finitely generated.
 \end{enumerate}
 Then {\rm (c)} $\Rightarrow$ {\rm (b)} $\Rightarrow$ {\rm (a)}. If moreover
 $S$ is the 
 analytification of a smooth algebraic $K$-variety, 
 then {\rm (a)} $\Rightarrow$ {\rm (c)}.
\end{pro}

\begin{proof}
 (c) $\Rightarrow$ (b): this is Selberg's lemma: any finitely
 generated subgroup of $GL(V)$ is virtually torsion-free.

 (b) $\Rightarrow$ (a) follows from \ref{thm::2.1.8}.~(b). 

 (a) $\Rightarrow$ (c): under (a), $\Coim\,\rho$ is the Galois group of a
 Galois temperate covering of $S$. If $S$ is 
 algebraic, $\Coim\,\rho$ must be finitely generated by \ref{pro::2.1.6}. 
\end{proof}

\begin{para}\label{para::3.5.11} We finish the section by showing that the
 connections which lie in the image of the temperate 
Riemann-Hilbert functor are algebrizable (this is not automatic in the
 non-archimedean situation), and even fuchsian: 
\end{para}

\begin{thm}\label{thm::3.5.12} Assume that $S$ is the analytification of
 a smooth algebraic $K$-variety $S^{\mathrm{alg}}$. Let 
 $(M,\nabla)$ be a vector bundle with integrable connection on $S$ which
 comes from a discrete representation of 
 $\pi_1^{\mathrm{temp}}(S,\ovl{s})$. Then $(M,\nabla)$ is the
 analytification of a (unique) algebraic vector 
 bundle with integrable connection on $S^{\mathrm{alg}}$, which has
 regular singularities and exponents in $\Q/\Z$ at any 
divisorial valuation of $K(S)$.  
\end{thm}

\begin{proof}
 By assumption, there is a finite Galois \'etale covering $S'\to
 S$ (with group $G$) such that $(M,\nabla)$ becomes 
 trivial on the topological universal covering of $S'$. The pull-back
 $(M,\nabla)_{S'}$ corresponds to a (unique) 
 representation of 
 $\pi_1^{\mathrm{top}}(S', s')$ (for any point $s'$ above $s$). Let
 $\ovl{S}'$ be a smooth algebraic compactification of $S'$ 
 (Hironaka). We may replace $K$ by the completion of its algebraic
 closure. By \ref{pro::1.1.3}, the homomorphism 
 $\pi_1^{\mathrm{top}}(S', s')\to\pi_1^{\mathrm{top}}(\ovl{S}', s')$ is
 an isomorphism, and it follows that $(M,\nabla)_{S'}$ extends 
 (uniquely) to a vector bundle with integrable connection on 
 $\ovl{S}'$. By GAGA (K\"opf), the latter is the analytification of a
 (unique) algebraic vector 
 bundle with integrable connection on $\ovl{S}^{\prime \mathrm{alg}}$. It is
 now easy to conclude by Galois descent from $S^{\prime \mathrm{alg}}$ to 
 $S^{\mathrm{alg}}$ (we refer to 
 \cite{andre01:_de_rham} for the details on regular singularities,
 exponents, and GAGA functor for connections).
\end{proof}

\begin{para}\label{para::3.5.13} Besides discrete representations of
 $\pi_1^{\mathrm{temp}}(S,\ovl{s})$, it is also useful to 
 consider {\it projective discrete representations}, \ie discrete
 representations with value in $PGL(V)$.  They give rise to {\it
 projective connections} over $S^{\mathrm{alg}}$, at least when
 $S^{\mathrm{alg}}$ is an {\it affine curve}. 

 Indeed, replacing $S^{\mathrm{alg}}$ by a finite Galois \'etale
 covering $S^{\prime \mathrm{alg}}$ with Galois group $G$, we may
 replace $\pi_1^{\mathrm{temp}}(S')$ by $\pi_1^{\mathrm{top}}(S')$, 
 which is a free group, for which the lifting property is immediate. This
 provides a connection $\nabla'$ over $S^{\prime \mathrm{alg}}$,
 and the associated projective connection is endowed with a $G$-action
 compatible with the $G$-action on $S^{\prime \mathrm{alg}}$, hence
 descends to a projective connection on $S^{\mathrm{alg}}$.
\end{para}

One has more: 
\begin{pro}\label{pro::3.5.14} Then any projective discrete representation
 $\ovl{\rho}:$ $\pi_1^{\mathrm{temp}}(S,\ovl{s})$ $\to$ $PSL(V)$ lifts to
 a genuine discrete representation
 $\rho:\,\pi_1^{\mathrm{temp}}(S,\ovl{s})\to SL(V)$, after replacing $K$
 by a finite extension.
\end{pro}

\begin{proof}
 We have seen that $\ovl{\rho}$ corresponds to a projective connection on
 $S^{\mathrm{alg}}$. Now it is well known that any projective connection
 lifts to a genuine connection after replacing $K$ by a finite extension
 (because $\mathrm{H}^2(S^{\mathrm{alg}}_{\ovl{K}, et},
 \Z/2\Z)=0$, \cf \cite[2.2.2.1]{katz90:_expon}). It suffices to check that the
 pull-back $\nabla''$ of this connection on $S^{\prime \mathrm{alg}}$
 comes from a discrete representation
 $\rho:\,\pi_1^{\mathrm{temp}}(S',\ovl{s}')\to SL(V)$. But we have on the
 other hand our connection $\nabla'$ which is projectively equivalent to
 $\nabla''$, 
 and which we may assume to come from a discrete representation 
 $\pi_1^{\mathrm{temp}}(S',\ovl{s}')\to SL(V)$. Let $S''$ be a finite
 \'etale covering of $S'$ such that the pull-back of any class in
 $\mathrm{H}^1(S^{\mathrm{alg}}_{\ovl{K}, 
 et}, \Z/2\Z)$ vanishes in $\mathrm{H}^1(S^{\prime \prime\,
 \mathrm{alg}}_{\ovl{K}, et}, 
 \Z/2\Z)$. Since $\nabla'$ and $\nabla''$ are projectively equivalent,
 their pull-backs on $S''$ are isomorphic 
 ({\it loc.~cit.}). It follows that $\nabla''$ comes from a discrete
 representation $\pi_1^{\mathrm{temp}}(S',\ovl{s}')\to SL(V)$.        
\end{proof}

\medskip We leave it as an exercise to translate \ref{pro::3.5.10} in
the context of projective connections.

 
\newpage
