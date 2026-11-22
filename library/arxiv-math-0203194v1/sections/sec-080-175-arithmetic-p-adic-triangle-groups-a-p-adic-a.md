---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-080-175-arithmetic-p-adic-triangle-groups-a-p-adic-a
section_title: "Arithmetic $p$-adic triangle groups. A $p$-adic analogue of Takeuchi's list."
section_number: 17.5
pages: 188-192
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.986
doc_brief: "Period mappings and differential equations. From C to Cp — 101 sections: Front matter; Purpose of this book.; Contents of this book."
---
\label{sub::5.5} 

\begin{para}\label{para::5.5.1} Arithmetic $p$-adic triangle groups are
 hyperbolic $p$-adic triangle groups which are {\it commensurable with
 the $p$-unit groups of quaternion algebras $\ovl{B}$ over number
 fields}.\footnote{In fact, these were the first $p$-adic triangle groups
 to be constructed \cite{poaptg}, and the existence of non-arithmetic
 hyperbolic $p$-adic triangle groups remained unclear for a while, before
 Kato's construction.}
 
 \medskip Let now $V$ be the set of $p$-adic and infinite places of
 $E$. It follows from the discussion of \ref{para::5.4.1} that
 arithmetic subgroups of 
 $G_{(V)}= PGL_2(E_v)$ are subgroups which are commensurable with the
 $p$-unit groups $PSL_1(\ovl{\mathcal{B}}[\frac{1}{p}])$ of quaternion
 algebras over {\it totally real} number fields $E$, which are {\it
 totally definite at infinity and split at exactly one place $v$ above
 $p$ }.
\end{para}

\begin{para}\label{para::5.5.2} Let $\Delta_p(e_0,e_1,e_\infty)\subset
 PGL_2(\C_p)$ be an arithmetic $p$-adic triangle group. Thus, there is a
 totally real number field $E \subset \C_p$, and a totally definite
 quaternion algebra $\ovl{B}$ over $E$, split at one place $v$ above $p$,
 and a maximal order $\ovl{\mathcal{B}}$, such that
 $\Delta_p(e_0,e_1,e_\infty)\subset PGL_2(E_v)$ is commensurable, up to
 conjugation, to
 $PSL_1\bigl(\ovl{\mathcal{B}}[\frac{1}{p}]\bigr)$. Instead of the 
 latter, it is equivalent and more convenient to work with the image
 $\Gamma_p^\ast$ in $PGL_2(E_v)$ of the normalizer $\bigl\{g\in
 \ovl{B}^\times\mid 
 \;g\ovl{\mathcal{B}}[\frac{1}{p}]=\ovl{\mathcal{B}}[\frac{1}{p}]g\bigr\}$.

 Let us show that the corresponding complex triangle group
 $\Delta_p(e_0,e_1,e_\infty)$ $\subset$ $PGL_2(\C)$ is arithmetic, attached
 to the same totally real number field $E$ (embedded into $\C$ via some
 real place $\infty_0$), and to the quaternion algebra $B$ over $E$
 obtained from $\ovl{B}$ by interchanging the local invariants at
 $\infty_0$ and $v$ (in particular $B$ is definite at every place at
 infinity except $\infty_0$, and {\it ramified at $v$} --- which turns out
 to be the unique place $v_p$ of $E$ above $p$ according to Takeuchi's
 classification).
 
 In the case $\Delta_p(e_0,e_1,e_\infty)=\Gamma_p^\ast$, this follows
 from \v{C}erednik's uniformization explained in  II.\ref{sub:7.4},
 II.\ref{sub:7.5}: in this 
 case, the Schwarz orbifold is a Shimura orbifold $\mathcal{X}^\ast$ and
 $\Delta(e_0,e_1,e_\infty)=\Gamma^\ast$.

 In general, the Schwarz
 orbifold $\mathcal{S}(e_0,e_1,e_\infty)$ is close to be a Shimura
 orbifold.  If fact, according to \ref{thm::5.3.7}, the $p$-adic Schwarz
 orbifold 
 $\mathcal{S}(e_0,e_1,e_\infty)$ is a finite orbifold-covering of a
 Mumford-Schwarz orbifold $\mathcal{S}(e'_0,e'_1,e'_\infty)$ with
 $\Delta_p(e_0,e_1,e_\infty)=\Delta_p(e'_0,e'_1,e'_\infty)$. Let $\Gamma$
 be a torsion-free subgroup of finite index of
 $\Delta_p(e'_0,e'_1,e'_\infty)\cap \Gamma_p^\ast$. Let $\Omega \subset
 \P^1_{\C_p}$ be the set of ordinary points for $\Gamma$. Then the
 Mumford curve $S=\Omega/\Gamma$ is simultaneously a finite orbifold
 covering of $\mathcal{S}(e'_0,e'_1,e'_\infty)$ and of $\mathcal{X}^\ast$
 (via the embeddings $\Gamma \subset \Delta_p(e'_0,e'_1,e'_\infty)$ and
 $\Gamma \subset \Gamma_p^\ast$ respectively).

 All these finite orbifold-coverings are defined over number
 fields $\subset \C$. Looking at the corresponding complex orbifolds, it
 is now clear that $\pi_1^{\mathrm{orb}}(\mathcal{S}(e_0,e_1,e_\infty))$
 $=\Delta(e_0,e_1,e_\infty)$ is commensurable with
 $\pi_1^{\mathrm{orb}}(\mathcal{X}^\ast)= \Gamma ^\ast$, whence the claim.
\end{para}

\begin{para}\label{para::5.5.3} Let us show, conversely, that if
 $\Delta(e_0,e_1,e_\infty)$ appears in Takeuchi's list, and if $B/E$ is
ramified at the place $v\mid p$, then $\Delta_p(e_0,e_1,e_\infty)$
exists and is an arithmetic $p$-adic triangle group; more precisely, it
is commensurable with the $p$-unit group of the quaternion algebras
$\ovl{B}/E$ obtained from $B$ by interchanging the local invariants at
$\infty_0$ (the indefinite place at infinity) and $v_p$ (in particular
$\ovl{B}$ is totally definite, and split at $v_p$).
 
 In the case $\Delta(e_0,e_1,e_\infty)=\Gamma^\ast$, \ie if
 $(e_0,e_1,e_\infty)$ is the first triple occurring on a row of 
 Takeuchi's table, this follows from \ref{thm::4.7.4}.     

 In general, $\Delta(e_0,e_1,e_\infty)$ is commensurable to an arithmetic
 triangle group $\Delta(e'_0,e'_1,e'_\infty)$ of the form $\Gamma^\ast$,
 and it is not difficult to deduce that $\Delta_p(e_0,e_1,e_\infty)$
 exists and is commensurable to
 $\Delta_p(e'_0,e'_1,e'_\infty)=\Gamma_p^\ast$. The point is that the
 corresponding respective projective connections $HGPC(a,b,c)$ and
 $HGPC(a',b',c')$ become isomorphic after suitable finite pull-backs.
\end{para}

\begin{para}\label{para::5.5.4} Putting \ref{para::5.5.2} and
 \ref{para::5.5.3} together, we conclude 
 that the arithmetic $p$-adic triangle groups
 $\Delta_p(e_0,e_1,e_\infty)$ are exactly those corresponding to the
 triples $(e_0,e_1,e_\infty)$ in Takeuchi's list when $v_p$ divides
 $\mathrm{disc}(B)$.  From that list, one gets:
\end{para}

\begin{thm}\label{thm::5.5.5} \cite{poaptg}. Up to permutation of the
 indices, there are $45$ arithmetic $2$-adic triangle groups, 
 $16$ arithmetic
 $3$-adic triangle groups, $9$ arithmetic $5$-adic triangle groups (and
 no arithmetic $p$-adic triangle group for $p>5$).

 More precisely, they are given by the following tables:

\begin{center}
 \renewcommand{\arraystretch}{1.5}
 \begin{longtable}{lcp{0.66\textwidth}}
 \multicolumn{3}{l}{\it Arithmetic $2$-adic triangle groups:}\\ \hline
 $E$ &$\mathrm{disc}(\ovl{B})$& $(e_0,e_1,e_\infty)
 \text{ \rm up to permutation}$ \\ \hline
 $\Q$ & $3$ & $(2,4,6)\,(2,6,6)\,(3,4,4)\,(3,6,6)$ \\
 $\Q(\sqrt 2)$ & $1$ &
 $(2,3,8)\, (2,4,8)\, (2,6,8)\, (2,8,8)\, (3,3,4)$\, $(3,8,8)\, 
 (4,4,4)\, (4,6,6)\, (4,8,8)$ \\
 $\Q(\sqrt 3)$ & $1$ &
 $(2,3,12)\, (2,6,12)\, (3,3,6)\, (3,4,12)\, (3,12,12)$\, $(6,6,6)$ \\
 $\Q(\sqrt 5)$ & $1$ &
 $(2,4,5)\, (2,4,10)\, (2,5,5)\, (2,10,10)\, (4,4,5)$\, $(5,10,10)$ \\
 $\Q(\sqrt 6)$ & $1$ & $(3,4,6)$ \\
 $\Q(\cos \pi/9)$ & $v_3$ & $(2,4,18)\, (2,18,18)\, (4,4,9)\, (9,18,18)$ \\
 $\Q(\cos \pi/8)$ & $1$ & $(2,3,16)\, (2,8,16)\, (3,3,8)\, (4,16,16)\,
 (8,8,8)$ \\ 
 $\Q(\cos \pi/10)$ & $1$ & $(2,5,20)\, (5,5,10)$  \\
 $\Q(\cos \pi/12)$ & $1$ &
 $(2,3,24)\, (2,12,24)\, (3,3,12)\, (3,8,24)\, (6,24,24)$\, $(12,12,12)$ \\
 $\Q(\sqrt 2, \sqrt 5)$ & $1$ & $(2,5,8)\, (4,5,5)$  \\ &&\\
 \multicolumn{3}{l}{\it Arithmetic $3$-adic triangle groups:} \\ \hline
 $\Q$ & $2$ & $(2,4,6)\, (2,6,6)\, (3,4,4)\, (3,6,6)$  \\
 $\Q(\sqrt 3)$ & $1$ & $(2,4,12)\, (2,12,12)\, (4,4,6)\, (6,12,12)$ \\
 $\Q(\sqrt 5)$ & $1$ & $(2,5,6)\, (3,5,5)$\\
 $\Q(\cos \pi/9)$ & $v_2$ & $(2,4,18)\, (2,18,18)\, (4,4,9)\, (9,18,18)$ \\
 $\Q(\cos \pi/15)$ & $1$ & $(2,5,30)\, (5,5,15)$ \\ && \\
 \multicolumn{3}{l}{\it Arithmetic $5$-adic triangle groups:}\\ \hline
 $\Q(\sqrt 5)$ & $1$ & $(2,3,10)\, (2,5,10)\, (3,3,5)\, (5,5,5)$ \\
 $\Q(\cos \pi/15)$ & $1$ &
 $(2,3,30)\, (2,15,30)\, (3,3,15)\, (3,10,30)\, (15,15,15)$ \\
 \end{longtable} 
\end{center}
\end{thm}

\begin{rems}
 (a) In these lists, one notice that $p$ divides
 at least one of the numbers $e_0,e_1,e_\infty$. This means that the
 parameters $a,b,c$ of the corresponding hypergeometric differential
 equation are not $p$-adic integers. In the literature on $p$-adic
 hypergeometric functions, on the contrary, $a,b,c$ are always assumed to
 be $p$-adic integers, for obvious convergence reasons.

 It is well-known that a fuchsian $p$-adic differential equations with
 Frobenius structure has exponents in $\Q\cap \Z_p$. Since this is not
 the case here, there is no Frobenius structure in the standard
 sense. However, there is some hidden Frobenius structure due to the
 ``geometric origin'' of the differential equation. We leave to the
 reader the intriguing question of finding out the right formulation of
 this hidden Frobenius structure (hint: the Frobenius structure is
 explicit at the level of the period mapping, \cf \cite{tpuosc}).

 \medskip
 (b) Takeuchi has also given a table with the various
 inclusions of triangle groups in each commensurability class. When
 $\Delta(e_0,e_1,e_\infty)$ is maximal (and $p$ ramified in the
 corresponding quaternion algebra), the corresponding $p$-adic triangle
 group $\Delta_p(e_0,e_1,e_\infty)$ is ``of Mumford type'', according to
 \ref{cor::5.3.7}.~(b).

 Arithmetic $p$-adic triangle groups not ``of Mumford type'' do exist,
 and are related to Shimura curves with {\it level divisible by $p$}.
 One can construct such $p$-adic triangle groups using Drinfeld's finite
 \'etale coverings $\Upsilon^n$ of the Drinfeld ``half space'' $\Omega$,
 which uniformize $p$-adically Shimura curves with level $p^n.M\,$ ($p$
 prime to $M$), \cf II.\ref{para:7.4.7}.  One has
 $\Gamma_p^+(p^nM)=\Gamma_p^+( M)$, 
 and the orbifold-quotient of a suitable intermediate covering $\Sigma$
 between $\Omega$ and $\Upsilon^n$ by $\Gamma_p^+( M)$ may be a Schwarz
 orbifold but not a Mumford-Schwarz orbifold. It seems that
 $\Delta_2(4,4,4)$ is of this type, for $p=2, \,n=M=1$ (we have not
 checked the details); the corresponding $\Gamma_2^+(1)$ is
 $\Delta_2(3,3,4)$.

 \medskip
 (c) Let $\ovl{S}$ be a smooth projective curve defined
 over $\ovl{\Q}$, and $\zeta_i$ be $\ovl{\Q}$-points on $\ovl{S}$
 endowed with indices $e_i$. We then say that the orbifold
 ${\mathcal{S}}=(\ovl{S}, (\zeta_i,e_i))$ is defined over $\ovl{\Q}$. In
 general, there is no reason for the uniformizing differential equation
 to be defined over $\ovl{\Q}$.

 However, this occurs if either ${\mathcal{S}}$ is a Schwarz orbifold
 (the uniformizing differential equation being essentially of
 hypergeometric type with rational parameters), or a Shimura orbifold
 (the uniformizing differential equation being essentially of Gauss-Manin
 type, \cf \ref{thm::4.7.4}). On the other hand, it is not difficult to
 see that the 
 property for the uniformizing differential equation to be defined over
 $\ovl{\Q}$ depends only on the commensurability class of the orbifold
 fundamental group $\pi_1^{\mathrm{orb}}(\mathcal{S})$.

 A transcendence conjecture of Chudnovsky, modified by Krammer 
 \cite[12]{aeoaafg}, predicts that the Schwarz and the Shimura 
 cases are the only exceptions, up to commensurability. Namely: 
 
 \begin{coj}\label{coj::5.5.6} (Chudnovsky-Krammer). Let ${\mathcal{S} }$
  be a one-dimensional hyperbolic orbifold defined over
  $\ovl{\Q}$. Assume that the uniformizing differential equation is
  defined over $\ovl{\Q}$. Then $\pi_1^{\mathrm{orb}}(\mathcal{S})$ is either
  commensurable to a triangle group, or is arithmetic.
 \end{coj}

 We {\it conjecture} the (straightforward) $p$-adic analogue of
 \ref{coj::5.5.6}.
 
 \medskip
 (d) By the theory of $p$-adic Betti lattices, there is
 a canonical $\ovl{\Q}$-structure in the $\C_p$-space of solutions at
 any point of $\P^1(\ovl{\Q})$ of the hypergeometric differential
 equation $HDGE(a,b,c)$ attached to an arithmetic $p$-adic triangle group
 (\cf \ref{thm::4.7.4}. If the base point is chosen to be one of the
 singularities $0,1,\infty$, one applies \ref{thm::4.7.4}
 to a finite orbifold-covering of the Schwarz orbifold which is a
 Shimura curve attached to a torsion-free congruence subgroup). 
 
 This raises the following (open) questions:

 {\it Is there a $\ovl{\Q}$-structure in the $\C_p$-space
 of solutions of the hypergeometric differential equation $HDGE(a,b,c)$
 attached to a non-arithmetic $p$-adic triangle group? Are
 non-arithmetic $p$-adic triangle groups related to some $p$-adic period
 mappings and suitable higher-dimensional Shimura orbifolds?}
\end{rems}
