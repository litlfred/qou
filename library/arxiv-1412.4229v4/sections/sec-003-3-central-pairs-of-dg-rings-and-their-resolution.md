---
doc_id: arxiv-1412.4229v4
doc_title: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS"
section_id: sec-003-3-central-pairs-of-dg-rings-and-their-resolution
section_title: "Central Pairs of DG Rings and their Resolutions"
section_number: 3
pages: 16-23
source_pdf: 1412.4229v4.pdf
source_sha256: 248d6a1e28a76a94
toc_source: outline
text_source: latex
latex_prose_ratio: 0.993
latex_coverage_ratio: 0.971
doc_brief: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS — Let A →B be a homomorphism of commutative rings."
---
\label{sec:resolutions-rings}

In this section we introduce several special kinds of DG rings and 
homomorphisms. Recall that $\cat{DGR}$ is the category of DG rings. 

\begin{dfn}
A DG ring $A = \bigoplus_{i \in \Z} A^i$ is called {\em nonpositive} if 
$A^i = 0$ for all $i > 0$. 
The full subcategory of $\cat{DGR}$ consisting of nonpositive DG rings is 
denoted by $\cat{DGR}^{\leq 0}$.
\end{dfn}

\begin{dfn} \label{dfn:330}
A DG ring $A = \bigoplus_{i \in \Z} A^i$ is called {\em strongly commutative} 
if it satisfies these two conditions:
\begin{enumerate}
\rmitem{i} $A$ is weakly commutative (Definition \ref{dfn:750}(2)), namely 
$b \cd a = (-1)^{i j} \cd a \cd b$ for all $a \in A^{i}$ and $b \in A^{j}$. 

\rmitem{ii} $a \cd a = 0$ for all $a \in A^i$ and $i$ odd. 
\end{enumerate}
We denote by $\cat{DGR}_{\mrm{sc}}$ the full subcategory of 
$\cat{DGR}$ on the strongly commutative DG rings.
\end{dfn}

\begin{dfn} \label{dfn:876}
A DG ring $A$ is called a {\em commutative DG ring} if it is both nonpositive 
and strongly commutative. The full subcategory of $\cat{DGR}$ consisting of 
commutative DG rings is denoted by $\cat{DGR}_{\mrm{sc}}^{\leq 0}$. 
\end{dfn}

In other words, 
\[ \cat{DGR}_{\mrm{sc}}^{\leq 0} = \cat{DGR}^{\leq 0} \cap
\cat{DGR}_{\mrm{sc}} . \]

\begin{exa}
A commutative DG ring $A$ concentrated in degree $0$ (i.e.\ $A = A^0$) is just 
a commutative ring. 
\end{exa}

\begin{rem}
The name ``strongly commutative DG ring'' was suggested to us by J. 
Palmieri. In an earlier version of this paper we used the name 
``strictly commutative DG ring'', following \cite{ML}; and in \cite{YZ2}
it was ``super-commutative DG algebra''. 

The name ``weakly commutative DG ring'' is ``commutative DG algebra'' in 
\cite{ML}, and ``graded-commutative DG algebra'' in \cite{AILN}. 

Of course when the number $2$ is invertible in $A^0$ (e.g.\ if $A^0$  contains 
$\Q$), then condition (i) of Definition \ref{dfn:330} implies condition (ii), 
so that the distinction between weak and strong commutativity disappears. See 
also Remark \ref{rem:750}.
\end{rem}

Central homomorphisms were introduced in Definition \ref{dfn:750}(3). 

\begin{dfn} \label{dfn:910}
A {\em central pair of DG rings} is a central homomorphism 
$u : A \to B$ in $\cat{DGR}$, where the DG ring $A$ is commutative. 
We usually denote this pair by $B / A$, keeping $u$ implicit. 

Suppose $A \xar{u} B$ and $A' \xar{u'} B'$
are central pairs of DG rings. A {\em morphism of central pairs} 
$w / v : B' / A' \to B / A$
consists of homomorphisms 
$v : A' \to A$ and $w : B' \to B$
in $\cat{DGR}$, such that 
$u \circ v = w \circ u'$. 
The resulting category is called the {\em category of central 
pairs of DG rings}, and is denoted by $\cat{PDGR}$. 
\end{dfn}

A morphism $w / v$ in $\cat{PDGR}$ is shown in diagram (\ref{eqn:985}). 
We do not require the homomorphism $w : B' \to B$ to be 
central. The homomorphism $v : A' \to A$ is automatically central, because $A$ 
is commutative. 

\begin{dfn} \label{dfn:911}
\mbox{}
\begin{enumerate}
\item A {\em nonpositive central pair} is a central pair $B / A$ such that both 
$A$ and $B$ are nonpositive DG rings. The full subcategory of nonpositive 
central pairs is denoted by $\cat{PDGR}^{\leq 0}$.

\item A {\em commutative central pair} is a central pair $B / A$ such that the 
DG ring $B$ is also commutative. The full subcategory of commutative 
central pairs is denoted by $\cat{PDGR}_{\mrm{sc}}^{\leq 0}$.

\item A morphism $w / v : B' / A' \to B / A$ in $\cat{PDGR}$
is called {\em central} if the homomorphism $w : B' \to B$ is central.
The subcategory of $\cat{PDGR}$ on all objects, but only with central 
homomorphisms, is denoted by $\cat{PDGR}_{\vec{\mrm{ce}}}$.

\item A morphism $w / v : B' / A' \to B / A$ in $\cat{PDGR}$
is called a {\em quasi-iso\-morphism} if the homomorphisms 
$v : A' \to A$ and $w : B' \to B$ are both quasi-isomorphisms.
\end{enumerate}
\end{dfn}

\begin{dfn} \label{dfn:912}
Let $B / A$ be a central pair of DG rings. 
A {\em resolution} of $B / A$ is a morphism 
$s / r : \til{B} / \til{A} \to B / A$ in $\cat{PDGR}$,
such that:
\begin{itemize}
\item $r : \til{A} \to A$ is a quasi-isomorphism.
\item $s : \til{B} \to B$ is a surjective quasi-isomorphism.
\end{itemize}

The resolution is called {\em strict} if $\til{A} = A$ and $r = \opn{id}_A$, 
the identity automorphism of $A$.
\end{dfn}

See diagram (\ref{eqn:482}) for an illustration. 

\begin{dfn} \label{dfn:913}
Let $w / v : B' / A' \to B / A$ be a morphism in $\cat{PDGR}$,
let 
$s / r : \til{B} / \til{A} \to B / A$
be a resolution of $B / A$, and let 
$s' / r' : \til{B}' / \til{A}' \to B' / A'$
be a resolution of $B' / A'$. A morphism 
$\til{w} / \til{v} : \til{B}' / \til{A}' \to \til{B} / \til{A}$
in $\cat{PDGR}$ is said to be {\em morphism of resolutions above $w / v$}
if 
\[ (w / v) \circ (s' / r') = (s / r) \circ (\til{w} / \til{v}) \]
in $\cat{PDGR}$.
In this case, we also say that $\til{w} / \til{v}$ is a {\em resolution of 
$w / v$}.

If $B' / A' = B / A$ and $w / v$ is the identity automorphism, then 
we say that $\til{w} / \til{v}$ is a morphism of resolutions of $B / A$. 
\end{dfn}

A morphism $\til{w} / \til{v}$ is shown in diagram (\ref{eqn:986}).

By {\em graded set} we mean a set $X$ 
with a partition $X = \coprod_{i \in \Z} X^i$; the elements of $X^i$ are 
said to have degree $i$. We say that $X$ is a {\em nonpositive graded set} if 
$X^i = \varnothing$ for all $i > 0$. 
A {\em filtered graded set} is a graded set $X$, with 
an ascending filtration 
$F = \{ F_j(X) \}_{j \in \Z}$
by graded subsets, such that $X = \bigcup_j F_j(X)$ and 
$F_{-1}(X) = \varnothing$. 

Let $A$ be a DG ring. We denote by $A^{\natural}$ the graded ring gotten from 
$A$ by forgetting the differential. The same for DG modules. 
When talking about free modules, we assume the DG ring $A$ is nonzero (to avoid 
nonsense).

For a variable $x$ of degree $i$, we let 
$A \ot x := A[-i]$, the shift by $-i$ of the DG $A$-module $A$.
For any element $a \in A^j$ we denote by $a \ot x$ or $a \cd x$ 
the element $\opn{t}^{-i}(a) \in A[-i]^{j + i}$; cf.\ (\ref{eqn:1025}).
Note that $\d(x) = 0$, and $\d(a \cd x) = \d(a) \cd x$ for any $a \in A$.  
Now consider a graded set of variables $X$. The {\em free DG $A$-module on $X$} 
is 
\[ A \ot X := \bigoplus_{x \in X} \ A \ot x . \]
A {\em free DG $A$-module} is a DG $A$-module $P$ that is isomorphic to 
$A \ot X$ for some graded set of variables $X$. The image of $X$ in $P$ is 
called a {\em basis} of $P$. 

Let $P$ be a DG $A$-module. A {\em semi-free filtration} on $P$ 
is an ascending filtration 
$F = \{ F_j(P) \}_{j \in \Z}$
of $P$ by DG submodules, such that $P = \bigcup_j F_j(P)$, 
$F_{-1}(P) = 0$, and each 
$\opn{gr}^F_j(P) := F_{j}(P) / F_{j - 1}(P)$ 
is a free DG $A$-module. 

We say that $P$ is a {\em semi-free DG $A$-module} if it admits some semi-free 
filtration. See \cite{AFH} and \cite{Hi}.
A semi-free DG module is K-projective, and hence also K-flat. 

Let $P$ be a semi-free DG $A$-module, with semi-free filtration $F$. 
For each $j \geq 0$ choose a graded subset $Y_j \subseteq F_j(P)$
whose image $\bar{Y}_j$
in $\opn{gr}^F_j(P)$ is a basis of this free DG $A$-module.
The  graded set  
$X := \coprod_{i \in \Z} \, Y_j$
is filtered by 
$F_j(X) := \bigcup_{j' \leq j} Y_{j'}$. 
Such a filtered graded set is called a {\em semi-basis of $P$}.
Note that for every $j$ there is an isomorphism of graded 
$A^{\natural}$-modules 
$A^{\natural} \ot F_j(X) \cong F_j(P)^{\natural}$;
and so $A^{\natural} \ot X \cong P^{\natural}$. 
For any element $y \in Y_j$, its image
$\bar{y} \in \bar{Y}_j \subseteq \opn{gr}^F_j(P)$
satisfies $\d(\bar{y}) = 0$; and hence 
$\d(y) \in F_{j - 1}(X)$. 
We see that 
$\d(F_{j}(X)) \subseteq F_{j - 1}(X)$. 

Given a graded set of variables $X$, we can form the 
noncommutative polynomial ring $\Z \bra{X}$ over $\Z$, which is the free 
$\Z$-module on the set of monomials $x_1 \cdots x_m$ in the elements of $X$,
and with the obvious multiplication and grading. 

The next definition is not standard. Its first occurrence seems to have  been 
in \cite{YZ2}. 

\begin{dfn}  \label{dfn:751}
Let $X = \coprod_{i \in \Z} X^i$ be a graded set of variables.
The {\em strongly commutative polynomial ring} $\Z[X]$ is the quotient of 
$\Z \bra{X}$ by the two-sided ideal generated by the elements 
$y \cd x - (-1)^{i j} \cd x \cd y$ and $z^2$, for all $x \in X^{i}$, 
$y \in X^{j}$ and $z \in X^k$, with $i, j, k \in \Z$ and $k$ odd. 
\end{dfn}

\begin{dfn} \label{dfn:60}
Consider a nonpositive central pair of DG rings $A \xar{u} B$. 
\begin{enumerate}
\item We say that $B$ is a {\em commutative semi-free DG ring over $A$},  
that $u$ is a {\em commutative semi-free DG ring homomorphism}, and that 
$B / A$ is a {\em commutative semi-free pair of DG rings}, if there is 
an isomorphism of graded $A^{\natural}$-rings
$B^{\natural} \cong A^{\natural} \ot_{\Z} \Z[X]$,
where $X$ is a nonpositive graded set, and $\Z[X]$ is the strongly commutative 
polynomial ring. Such a graded set $X$ is called a {\em set of commutative 
semi-free ring generators} of $B$ over $A$. 

\item We say that $B$ is a {\em noncommutative semi-free DG ring over $A$}, 
that $u$ is a {\em noncommutative semi-free DG ring homomorphism}, and that 
$B / A$ is a {\em noncommutative semi-free pair of DG rings}, if there 
is an isomorphism of graded $A^{\natural}$-rings
$B^{\natural} \cong A^{\natural} \ot_{\Z} \Z \bra{X}$,
where $X$ is a nonpositive graded set, and $\Z\bra{X}$ is the noncommutative 
polynomial ring. Such a graded set $X$ is called a {\em set of noncommutative 
semi-free ring generators} of $B$ over $A$. 

\item  We say that  $B$ is a {\em K-flat DG ring over $A$}, that 
$u$ is a {\em K-flat DG ring homomorphism}, and that 
$B / A$ is a {\em K-flat pair of DG rings}, if $B$ is K-flat
as a DG $A$-module (left or right -- it does not matter). 
\end{enumerate}
\end{dfn}

\begin{prop} \label{prop:750}
Let $u : A \to B$ a nonpositive central pair of DG rings, which is either 
commutative semi-free or a noncommutative semi-free. Then $u : A \to B$ is 
K-flat. \end{prop}

\begin{proof}
In the noncommutative case, let $X$ be a set of noncommutative semi-free ring 
generators of $B$ over $A$. Then the monomials $x_1 \cdots x_m$, 
with  $x_1, \ldots, x_m \in X$, are a semi-basis for the DG $A$-module $B$.
We are using the fact that the graded set $X$ is nonpositive. 
 
In the commutative case, let $X$ be a set of commutative semi-free ring 
generators of $B$ over $A$. Choose some ordering of the set $X$. 
Then the monomials $x_1 \cdots x_m$, with  $x_1 \leq \cdots \leq x_m$
in $X$, and $x_i < x_{i + 1}$ if $x_i$ is odd, are a semi-basis for the DG 
$A$-module $B$. Again, we are using the fact that the graded set $X$ is 
nonpositive. 

We see that in both cases $B$ is a semi-free DG $A$-module, and thus it is 
K-flat. 
\end{proof}

\begin{exa} \label{exa:690}
Let $A$ be a commutative ring, and let $\bsym{a} = (a_1, \ldots, a_n)$ be a 
sequence of elements in $A$. The Koszul complex 
$B := \opn{K}(A; \bsym{a})$ associated to this sequence is a commutative
semi-free DG ring over $A$. It has a set of commutative 
semi-free ring generators $X = \{ x_1, \ldots, x_n \}$ of degree $-1$,
such that $\d_B(x_i) = a_i$.   
\end{exa}

\begin{rem} \label{rem:750}
The strongly commutative polynomial ring $\Z[X]$ is a free graded $\Z$-module. 
This is what makes Proposition \ref{prop:750} work. 

The ``weakly commutative polynomial ring'', which is the quotient of 
$\Z \bra{X}$ by the two-sided ideal generated by the elements 
$y \cd x - (-1)^{i j} \cd x \cd y$ for all $x \in X^{i}$ and $y \in X^{j}$,
{\em is not flat over $\Z$}. Indeed, for any odd element $z \in X$ we have 
$z^2 \neq 0$ but $2 \cd z^2 = 0$. 
\end{rem}

\begin{dfn} \label{dfn:52}
Let $B / A$ be a central pair of DG rings, and let 
$s / r : \til{B} / \til{A} \to B / A$ be a resolution of $B / A$
(Definition \ref{dfn:912}). 
\begin{enumerate}
\item Assume $B / A$ is a commutative pair. We say that $\til{B} / \til{A}$
is a {\em commutative semi-free resolution} of $B / A$ if the pair 
$\til{B} / \til{A}$ is commutative semi-free (Definition \ref{dfn:60}(1)). 

\item We say that $\til{B} / \til{A}$ is a {\em noncommutative semi-free 
resolution} of $B / A$ if the pair 
$\til{B} / \til{A}$ is noncommutative semi-free (Definition \ref{dfn:60}(2)).

\item We say that $\til{B} / \til{A}$ is a {\em K-flat resolution} of $B / A$ 
if the pair $\til{B} / \til{A}$ is K-flat (Definition \ref{dfn:60}(3)).
\end{enumerate}
\end{dfn}

\begin{exa}
If $B$ is K-flat over $A$, then $B / A$ is a K-flat ring resolution of itself. 
It is terminal among all K-flat ring resolutions of $B / A$.
\end{exa}

\begin{exa}
Let $u : A \to B$ be a surjective homomorphism of commutative rings, and let 
$\bsym{a} = (a_1, \ldots, a_n)$ be a sequence of elements of $A$ that generates 
the ideal $\opn{Ker}(u)$. Assume that the sequence $\bsym{a}$ is regular. 
Define $\til{B} := \opn{K}(A; \bsym{a})$, the Koszul complex. 
Then $\til{B} / A$ is a strict commutative semi-free DG ring 
resolution of $B / A$. 
\end{exa}

\begin{rem}
In \cite{YZ2} we did not require the quasi-isomorphism $w$ to be surjective. 
That omission was not significant there, because we were mostly concerned with 
the case when $B$ is a ring (cf.\ \cite[Proposition 1.8]{YZ2}). When $B$ has 
nonzero negative components, the surjectivity is needed (cf.\ proof of Theorem 
\ref{thm:305} below).
\end{rem}

The next results in this section are enhanced versions of 
\cite[Propositions 1.7 and 1.8]{YZ2}.
The category $\cat{DGR}^{\leq 0} \centover A$ was introduced in Definition 
\ref{dfn:750}(4). 

\begin{lem} \label{lem:305}
Let $A$ be a commutative DG ring, and let 
$B, B' \in  \cat{DGR}^{\leq 0} \centover A$. 
Assume either of these two conditions holds\tup{:}
\begin{enumerate}
\rmitem{i} $B$ is commutative, and $B'$ is commutative semi-free over $A$, 
with commutative semi-free ring generating set $X$. 

\rmitem{ii} $B'$ is noncommutative semi-free over $A$, with noncommutative 
semi-free ring generating set $X$. 
\end{enumerate}
Let $w : X \to B$ be a degree $0$ function. Then\tup{:}
\begin{enumerate}
\item The function $w$ extends uniquely to a graded $A^{\natural}$-ring 
homomorphism $w : B'^{\, \natural} \to B^{\natural}$.

\item The graded ring homomorphism $w : B'^{\, \natural} \to B^{\natural}$
extends to a DG ring homomorphism $w : B' \to B$ iff 
$\d(w(x)) = w(\d(x))$ for all $x \in X$. 
\end{enumerate}
\end{lem}

\begin{proof}
This is an easy exercise. 
\end{proof}

\begin{lem} \label{lem:306}
Let $X$ be a nonpositive graded set, and let $A$ be a commutative DG 
ring. Consider the graded ring $B := A^{\natural} \ot_{\Z} \Z[X]$ or 
$B := A^{\natural} \ot_{\Z} \Z\bra{X}$. 
\begin{enumerate}
\item Let $\d_X : X \to B$ be a degree $1$ function. The function $\d_X$ 
extends uniquely to a degree $1$ derivation $\d_B : B \to B$, such 
that $\d_B|_A = \d_A$, the differential of $A$. 

\item The derivation $\d_B$ is a differential on $B$, i.e.\ 
$\d_B \circ \d_B = 0$, iff  
$(\d_B \circ \d_B)(x) = 0$ for all $x \in X$. 
\end{enumerate}
\end{lem}

\begin{proof}
(1) Take elements $x_j \in X^{n_j}$ for $j = 1, \ldots, m$, and consider the 
monomial $x_1 \cdots x_m \in \Z[X]$ (resp.\ in $\Z \bra{X}$). 
We let 
\[ \d_B(x_1 \cdots x_m) := 
\sum_{j = 1}^m (-1)^{n_1 + \cdots n_{j-1}} \cd x_1 \cdots x_{j-1} \cd 
\d_X(x_{j}) \cd x_{j+1} \cdots x_m \in B .  \]
This is well-defined in the commutative case (and there is nothing to check in 
the noncommutative case). Extending it additively we obtain a degree $1$ 
$\Z$-linear homomorphism 
$\Z[X] \to B$ (resp.\ $ \Z \bra{X} \to B$). This extends to 
a degree $1$ $A$-linear homomorphism $\d_B : B \to B$
that satisfies the graded Leibniz rule. 

\medskip \noindent
(2) This is an easy exercise. 
\end{proof}

For a DG ring $A$ we denote by $\opn{Z}(A) = \bigoplus_i \opn{Z}^i(A)$ 
the set of cocycles, and by 
$\opn{B}(A) = \bigoplus_i \opn{B}^i(A)$ 
the set of coboundaries (i.e.\ the kernel and image of $\d_A$, 
respectively).
So $\opn{Z}(A)$ a DG subring of $A$ (with zero differential of course),
and $\opn{B}(A)$ is a two-sided graded ideal of $\opn{Z}(A)$.

\begin{thm} \label{thm:305}
Let $A \xar{u} B$ be a nonpositive central pair of DG rings.
\begin{enumerate}
\item If $B$ is commutative, then there exists a strict commutative semi-free 
DG ring resolution 
$A \xar{\til{u}} \til{B}$ of $A \xar{u}  B$.

\item There exists a strict noncommutative semi-free DG ring resolution 
$A \xar{\til{u}} \til{B}$ of $A \xar{u}  B$.
\end{enumerate} 
\end{thm}

\begin{proof}
(1) We are looking for a commutative semi-free DG $A$-ring $\til{B}$,
with a quasi-isomorphism $v : \til{B} \to B$ in 
$\cat{DGR}_{\mrm{sc}}^{\leq 0} / A$. 
We shall construct an increasing sequence of 
commutative DG $A$-rings 
$F_0(\til{B}) \subseteq F_1(\til{B}) \subseteq \cdots$. 
The differential of $F_i(\til{B})$ will be denoted by $\d_i$. At the same time 
we shall construct an increasing sequence of graded sets 
$F_0(X) \subseteq F_1(X) \subseteq \cdots$,
with a compatible sequence of isomorphisms 
$F_i(\til{B})^{\natural} \cong A^{\natural} \ot_{\Z} \Z[F_i(X)]$.
We shall also construct a compatible sequence of DG ring homomorphisms 
$v_i : F_i(\til{B}) \to B$.
The DG $A$-ring $\til{B} := \bigcup_{i} F_i(\til{B})$ and the 
homomorphism $v := \lim_{i \to} v_i$ will have the desired properties. 

The construction is by recursion on $i \in \N$. Moreover, for every $i$ the 
following conditions will hold:
\begin{enumerate}
\rmitem{i} The homomorphisms $v_i : F_i(\til{B}) \to B$,
$\opn{B}(v_i) : \opn{B}(F_i(\til{B})) \to \opn{B}(B)$ and 
$\opn{H}(v_i) : \opn{H}(F_i(\til{B})) \to \opn{H}(B)$ are surjective
in degrees $\geq -i$. 

\rmitem{ii} The homomorphism 
$\opn{H}(v_i) : \opn{H}(F_i(\til{B})) \to \opn{H}(B)$ is 
bijective in degrees $\geq -i + 1$.
\end{enumerate}

We start by choosing a set $Z_0''$ of degree $-1$ elements, and a function 
$v_0 : Z''_0 \to B^{-1}$, such that the set 
$\d_B(v_0(Z''_0))$ generates  $\opn{B}^{0}(B)$ as an $A^0$-module. 
Let $Y''_0$ be a set of degree $0$ elements, with a bijection 
$\d_0 : Z''_0 \to Y''_0$. 
Let $v_0 : Y''_0 \to B^{0}$ 
be the unique function such that 
$v_0(\d_0(z)) = \d_B(v_0(z))$ for all $z \in Z''_0$.

Choose a set $Y'_0$ of degree $0$ elements, and a function 
$v_0 : Y'_0 \to B^0$, such that the set $v_0(Y'_0 \sqcup Y''_0)$
generates $B^0$ as an $A^0$-ring. 

Define the graded set 
$F_0(X) := Y'_0 \sqcup Y''_0 \sqcup Z''_0$,
and the graded ring 
$F_0(\til{B})^{\natural} := A^{\natural} \ot_{\Z} \Z[F_0(X)]$.
Setting $\d_0(y) := 0$ for $y \in Y'_0 \sqcup Y''_0$
gives a degree $1$ function 
$\d_0 : F_0(X) \to F_0(\til{B})^{\natural}$.
According to Lemma \ref{lem:306} we get a differential $\d_0$ on 
the graded ring $F_0(\til{B})^{\natural}$, and it becomes the DG $A$-ring 
$F_0(\til{B})$. 
Lemma \ref{lem:305} says that the function $v_0 : F_0(X) \to B$ 
extends uniquely to a DG $A$-ring homomorphism
$v_0 : F_0(\til{B}) \to B$. Condition (i) holds, and condition (ii) holds 
trivially, for $i = 0$. 

Now take any $i \geq 0$, and assume that 
$v_i : F_i(\til{B}) \to B$ is already defined, and it satisfies conditions 
(i)-(ii). 
Choose a graded set $Y'_{i+1}$ of degree $-i-1$ elements, and a 
function $v_{i+1} : Y'_{i+1} \to \opn{Z}^{-i-1}(B)$, such that  
the cohomology classes of the elements of $v_{i+1}(Y'_{i+1})$
generate $\opn{H}^{-i-1}(B)$ as $\opn{H}^{0}(A)$-module. 
For $y \in Y'_{i+1}$ let $\d_{i+1}(y) := 0 \in F_i(\til{B})$.

Consider the $A^0$-module
\[ J_{i+1} := \bigl\{ b \in \opn{Z}^{-i} (F_i(\til{B})) \mid 
\mrm{H}^{-i}(v_i)(b) = 0 \bigr\} . \]
Choose a graded set $Y'''_{i+1}$ of degree $-i-1$ elements, and a 
function $\d_{i+1} : Y'''_{i+1} \to J_{i+1}$, such that the cohomology 
classes of the elements of $\d_{i+1}(Y'''_{i+1})$ generate the 
$\mrm{H}^{0}(A)$-module 
\[ \opn{Ker} \bigl( \mrm{H}^{-i}(v_i) : 
\mrm{H}^{-i}(F_i(\til{B})) \to \mrm{H}^{-i}(B) \bigr) . \]
For any $y \in Y'''_{i+1}$  there exists some $b \in B^{-i-1}$ such that 
$v_i(\d_{i+1}(y)) = \d(b)$, and we let $v_{i+1}(y) := b$. 

Choose a graded set $Z''_{i+1}$ of degree $-i-2$ elements, and a
function $v_{i+1} :  Z''_{i+1} \to B^{-i-2}$, such that the set 
$\d_B(v_{i+1}(Z''_{i+1}))$ generates $\opn{B}^{-i-1}(B)$ as 
$A^0$-module. 
Let $Y''_{i+1}$ be a set of degree $-i-1$ elements, with a bijection 
$\d_{i+1} : Z''_{i+1} \to Y''_{i+1}$. 
Let 
$v_{i+1} : Y''_{i+1} \to B^{-i-1}$ 
be the unique function such that 
$v_{i+1}(\d_{i+1}(z)) = \d_B(v_{i+1}(z))$
for all $z \in Z''_{i+1}$.
For $y \in Y''_{i+1}$ we define $\d_{i+1}(y) := 0$. 

Lastly choose a graded set $Y'_{i+1}$ of degree $-i-1$ elements, and a 
function $v_{i+1} : Y'_{i+1} \to B^{-i-1}$, such that, 
letting 
\[ Y_{i+1} := Y'_{i+1} \sqcup Y''_{i+1} \sqcup Y'''_{i+1}  , \] 
the set $v_{i+1}(Y_{i+1})$ generates $B^{-i-1}$ as an $A^0$-module. 
Since 
$v_i : \opn{B}^{-i}(F_i(\til{B})) \to \opn{B}^{-i}(B)$ 
is surjective, for any $y \in Y'_{i+1}$ there exists 
$b \in F_i(\til{B})^{-i}$ such that 
$v_i(b) = \d_B(v_{i+1}(y))$, and we define $\d_{i+1}(y) := b$.

Define the graded set 
\[ F_{i+1}(X) := F_{i}(X) \sqcup Y_{i+1} \sqcup Z''_{i+1} \]
and the commutative graded ring 
\[ F_{i+1}(\til{B})^{\natural} := A^{\natural} \ot_{\Z} \Z[F_{i+1}(X)] . \]
There is a degree $1$ function 
$\d_{i+1} : F_{i+1}(X) \to F_{i+1}(\til{B})^{\natural}$
such that $\d_{i+1}|_{F_i(X)} = d_i$. 
According to Lemma \ref{lem:306} the function $\d_{i+1}$ induces 
a differential $\d_{i+1}$ on $F_{i+1}(\til{B})^{\natural}$;
so we get a DG ring $F_{i+1}(\til{B})$. 
Likewise we have a degree $0$ function 
$v_{i+1} : F_{i+1}(X) \to B$ such that 
$v_{i+1}|_{F_{i}(X)} = v_i|_{F_{i}(X)}$.
By Lemma \ref{lem:305} there is an induced DG 
$A$-ring homomorphism $v_{i+1} : F_{i+1}(\til{B}) \to B$, 
and it satisfies 
$v_{i+1}|_{F_{i}(\til{B})} = v_i$.

\medskip \noindent 
(2) Here we are looking for a noncommutative semi-free DG $A$-ring $\til{B}$,
with a quasi-isomorphism $v : \til{B} \to B$ in 
$\cat{DGR}^{\leq 0} \centover A$. 
The proof here is the same as in part (1), except that we now replace 
$\Z[F_i(X)]$ with $\Z \bra{F_{i}(X)}$ everywhere.
\end{proof}

\begin{thm} \label{thm:306}
Let $A \xar{u} B$ be a central pair of nonpositive DG rings. 
Suppose we are given two factorizations 
$A \xar{\til{u}} \til{B} \xar{v} B$ and 
$A \xar{\til{u}'} \til{B}' \xar{v'} B$
of $u$ in $\cat{DGR}^{\leq 0} \centover A$, such that
$v$ is a surjective quasi-isomorphism, and either of these two conditions 
holds\tup{:}
\begin{enumerate}
\rmitem{i} The DG ring $\til{B}$ is commutative, and the DG ring 
$\til{B}'$ is commutative semi-free over $A$.
\rmitem{ii} The DG ring $\til{B}'$ is noncommutative semi-free over $A$.
\end{enumerate}
Then there exists a homomorphism 
$w : \til{B}' \to \til{B}$ in $\cat{DGR}^{\leq 0} \centover A$ such that 
$w \circ \til{u}' = \til{u}$ and $v \circ w = v'$.
\end{thm}

The situation is shown in this commutative diagram in 
$\cat{DGR} \centover A$ below. 

\begin{equation} \label{eqn:23}
\UseTips \xymatrix @C=5ex @R=5ex {
& 
\til{B}'
\ar[dr]^{v'}
\\
A
\ar[rr]^{u}
\ar[ur]^{\til{u}'} ="utilp"
\ar[dr]_{\til{u}}

{} \save 
[]+<-6ex,6ex> *+[F-:<3pt>]{\scriptstyle \text{semi-free}} 
\ar@{..} "utilp" 
\restore
& 
&
B
\\
&
\til{B}
\ar[ur]_{v} ="v"

{} \save 
[]+<10ex,-2ex> *+[F-:<3pt>]{\scriptstyle \text{surj qu-isom}} 
\ar@{..} "v" 
\restore
}
\qquad  
\xymatrix @C=5ex @R=5ex {
& 
\til{B}'
\ar[dr]^{v'}
\ar[dd]_{w}
\\
A
\ar[ur]^{\til{u}'}
\ar[dr]_{\til{u}}
& 
&
B
\\
&
\til{B}
\ar[ur]_{v}
}
\end{equation}

\begin{proof}
The proof is similar to that of \cite[Proposition 1.8]{YZ2}.
Let $X = \coprod_{i \leq 0} X^i$ be a set of commutative (resp.\ 
noncommutative) 
semi-free DG $A$-ring generators of $\til{B}'$ over $A$. Define 
$F_i(X) := \bigcup_{-i \leq j \leq 0} X^i$, 
and let $F_i(\til{B}')$ be the $A$-subring of $\til{B}'$ generated by the set 
$F_i(X)$. So $F_i(\til{B}')$ is a DG $A$-ring, 
$F_i(\til{B}')^{\natural} \cong A^{\natural} \ot_{\Z} \Z[F_i(X)]$
(resp.\ $F_i(\til{B}')^{\natural} \cong A^{\natural} \ot_{\Z} \Z \bra{F_i(X)}$),
and $\til{B}' = \bigcup_i F_i(\til{B}')$. 
We will construct a consistent sequence of homomorphisms 
$w_i : F_i(\til{B}') \to \til{B}$ in 
$\cat{DGR}^{\leq 0} \centover A$, 
satisfying 
$w_i \circ \til{u}' = \til{u}$ and $v \circ w_i = v'$.
The construction is by recursion on $i \in \N$.
Then $w := \lim_{i \to} w_i$ will have the required properties. 

We start with $i = 0$. Take any $x \in X^0$. Since $v$ is surjective, 
there exists $b \in \til{B}^{0}$ such that 
$v(b) = v'(x)$ in $B^{0}$. We let 
$w_0(x) := b$. The resulting function $w_0 : X^0 \to \til{B}$
extends uniquely to a DG $A$-ring homomorphism 
$w_0 : F_i(\til{B}') \to \til{B}$, by Lemma \ref{lem:305}. 

Next consider any $i \in \N$, and 
assume a DG $A$-ring homomorphism $w_{i} : F_i(\til{B}') \to \til{B}$ is 
defined, satisfying the required conditions. 
Take any element $x \in X^{-i-1}$. 
Since $v$ is surjective, there exists $b \in \til{B}^{-i-1}$ such 
that 
$v(b) = v'(x)$ in $B^{-i-1}$. 
Now $\d(x) \in F_i(\til{B}')^{-i}$ is a cocycle in $F_i(\til{B}')$, so 
$w_i(\d(x)) \in \til{B}^{-i}$ is a cocycle. 
Let $c := w_i(\d(x)) - \d(b) \in \til{B}^{-i}$, which is also a cocycle. 
We have 
\[ v(c) = v(w_i(\d(x)) - v(\d(b)) = 
v'(\d(x)) - v(\d(b)) = 
\d(v'(x) - v(b)) = 0 . \]
Thus the cohomology class $[c]$ satisfies 
$\opn{H}(v)([c]) = [v(c)] = 0$.
Because $ \opn{H}(v)$ is bijective we conclude that $[c] = 0$ in 
$\opn{H}^{-i}(\til{B})$. Hence there is some $b' \in \til{B}^{-i-1}$ such that 
$\d(b') = c$. We define $w_{i+1}(x) := b + b'$. Then 
\begin{equation} \label{eqn:305}
 \d(w_{i+1}(x)) = \d(b + b') = \d(b) + c = w_{i}(\d(x)) . 
\end{equation}

In this way we obtain a function 
$w_{i+1} : F_{i+1}(X) \to \til{B}$ that extends $w_i$.
According to Lemma \ref{lem:305}(1), the function $w_{i+1}$ extends uniquely 
to a homomorphism of graded $A^{\natural}$-rings
$F_{i+1}(w) : F_{i+1}(\til{B}')^{\natural} \to \til{B}^{\natural}$. 
Equation (\ref{eqn:305}) and Lemma \ref{lem:305}(2) imply that 
$w_{i+1} : F_{i+1}(\til{B}')^{} \to \til{B}^{}$
is in fact a homomorphism of DG rings. 
\end{proof}

\begin{cor} \label{cor:980} \mbox{}
\begin{enumerate}
\item Any object $B / A$ of $\cat{PDGR}^{\leq 0}$ admits a nonpositive 
K-flat resolution $\til{B} / \til{A}$.

\item Any morphism 
$w / v : B' / A' \to B / A$ in $\cat{PDGR}^{\leq 0}$ admits a nonpositive 
K-flat resolution $\til{w} / \til{v}$.
\end{enumerate}
\end{cor}

\begin{proof}
(1) Let $\til{B}$ be a noncommutative semi-free DG ring resolution of $B$ over 
$A$. See Theorem \ref{thm:305}.
Then $\til{B} / A$ is strict nonpositive K-flat resolution of $B / A$. 

\medskip \noindent
(2) Let $\til{B}'$ be a noncommutative semi-free DG ring resolution of $B'$ 
over 
$A'$, and let $\til{A}$ be a commutative semi-free DG ring resolution of $A$ 
over $A'$. Next, let $\til{B}$ be a noncommutative semi-free DG ring resolution 
of $B$ over $\til{A}$. So $\til{B}' / A'$ is a K-flat resolution of $B' / A'$, 
and $\til{B} / \til{A}$ is a K-flat resolution of $B / A$. Also, we have a 
homomorphism $\til{v} : A' \to \til{A}$ above $v : A' \to A$. Finally, 
according to Theorem \ref{thm:306}, we can find a 
homomorphism $\til{w} : \til{B}' \to \til{B}$
that respects all other homomorphisms. 
\end{proof}
