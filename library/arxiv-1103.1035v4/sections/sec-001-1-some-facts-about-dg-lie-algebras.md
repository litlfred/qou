---
doc_id: arxiv-1103.1035v4
doc_title: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS"
section_id: sec-001-1-some-facts-about-dg-lie-algebras
section_title: "Some Facts about DG Lie Algebras"
section_number: 1
pages: 4-7
source_pdf: 1103.1035v4.pdf
source_sha256: dd5c4660e1d08ea1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.972
doc_brief: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS — Consider a pronilpotent DG (differential graded) Lie algebra over a ﬁeld of characteristic 0."
---
\label{sec:facts}

Let $\K$ be a field of characteristic $0$.
Given $\K$-modules $V, W$ we write $V \otimes W$ and 
$\opn{Hom}(V, W)$ instead of $V \otimes_{\K} W$ and $\opn{Hom}_{\K}(V, W)$,
respectively.

\begin{dfn}
By {\em parameter algebra} over $\K$ we mean a complete noetherian local
commutative $\K$-algebra $R$, with maximal ideal $\m$, such that $R / \m = \K$.
We call $\m$ a {\em parameter ideal}.
\end{dfn}

The most important example is of course
$R = \K[[\hbar]]$, where $\hbar$ is a variable, called the deformation
parameter.

Note that $R = \K \oplus \m$, so the ring $R$ can be recovered from the
nonunital algebra $\m$. For any $j \in \N$ let $R_j := R / \m^{j+1}$ and 
$\m_j := \m / \m^{j+1}$. So $R_0 = \K$, each $R_j$ is an artinian local ring
with maximal ideal $\m_j$, 
$R \cong \lim_{\leftarrow j} R_j$,
and
$\m \cong  \lim_{\leftarrow j} \m_j$.

Let us fix a parameter algebra $(R, \m)$.
Given an $R$-module $M$, its {\em $\m$-adic completion} is
\[ \what{M} := \lim_{\leftarrow j}\, (R_j \ot_R M) . \]
The module $M$ is called {\em $\m$-adically complete} if the canonical
homomorphism $M \to \what{M}$ is bijective. (Some texts would say that $M$ is
complete and separated.) Since $R$ is noetherian, the $\m$-adic completion
$\what{M}$ of any $R$-module $M$ is $\m$-adically complete; 
see \cite[Corollary 3.5]{Ye5}.

Given an $R$-module $M$ and a $\K$-module $V$ let us write 
\begin{equation} \label{eqn:52}
M \hot V := \lim_{\leftarrow j}\, (R_j \ot_R (M \ot V)) , 
\end{equation}
namely $M \hot V$ is the $\m$-adic completion of the $R$-module $M \ot V$. 
If $W$ is another $\K$-module, then there is a unique $R$-module isomorphism
\[ M \hot (V \ot W) \cong (M \hot V) \hot W \]
that commutes with the canonical homomorphisms from 
$M \ot V \ot W$; hence we shall simply denote this complete $R$-module by 
$M \hot V \hot W$.

Let $\g = \boplus_{i \in \Z} \g^i$ be a DG Lie algebra over $\K$.
(There is no finiteness assumption on $\g$.)
For any $i$ let $\m \hatotimes \g^i$ be the complete tensor product
as in (\ref{eqn:52}).
We get a pronilpotent $R$-linear DG Lie algebra 
\begin{equation} \label{eqn:64}
\m \hatotimes \g := \bigoplus_{i \in \Z}\, \m \hatotimes \g^i , 
\end{equation}
with differential $\d$ and graded Lie bracket  $[-,-]$ induced from $\g$. 

Recall that the Maurer-Cartan equation in $\m \hatotimes \g$ is
\begin{equation}
\d(\omega) + \smfrac{1}{2} [\omega, \omega] = 0
\end{equation}
for $\omega \in \m \hatotimes \g^1$.
A solution of this equation is called an {\em MC element}
of $\m \hatotimes \g$. The set of MC elements is denoted by 
$\opn{MC}(\m \hatotimes \g)$. 
In degree $0$ we have a pronilpotent Lie algebra $\m \hatotimes \g^0$,
so there is an associated pronilpotent group 
$\exp(\m \hatotimes \g^0)$, called the {\em gauge group}, and 
a bijective function 
\[ \exp : \m \hot \g^0 \to \exp(\m \hot \g^0) \]
called the exponential map.

An element $\ga \in \m \hatotimes \g^0$ acts on $\m \hatotimes \g$ by the
derivation 
\begin{equation}
\opn{ad}(\ga)(\al) := [\ga, \al] .
\end{equation}
We view $\opn{ad}(\ga)$ as an element of $R \hot \opn{End}(\g)^0$.
Let $g := \exp(\gamma) \in \exp(\m \hatotimes \g^0)$, and define 
\begin{equation} \label{eqn:11}
\opn{Ad}(g) := \exp (\opn{ad}(\gamma)) 
 = \sum_{i \geq 0} \, \smfrac{1}{i!} \opn{ad}(\ga)^i
\in R \hot \opn{End}(\g)^0 
\end{equation}
(this series converges in the $\m$-adic topology).
The element $\opn{Ad}(g)$ is an $R$-linear automorphism of the graded Lie
algebra $\m \hatotimes \g$. There is an induced group automorphism
$\opn{Ad}(g)$ of the group $\exp(\m \hatotimes \g^0)$, and this automorphism
satisfies the equation 
\begin{equation} \label{eqn:10}
\opn{Ad}(g)(h) = g \circ h \circ g^{-1} 
\end{equation}
for all $h \in \exp(\m \hatotimes \g^0)$.

There is another action of $\ga \in \m \hatotimes \g^0$ on 
$\om \in \m \hatotimes \g^{1}$:
\begin{equation}
\opn{af}(\ga)(\om) := [\ga, \om] - \d(\ga) = 
\opn{ad}(\ga)(\om) - \d(\ga) .
\end{equation}
This is an affine action, namely 
\[ \opn{af}(\ga) \in R \hot \bigl( \opn{End}(\g^1) \ltimes \g^1 \bigr) . \]
Consider the elements
$g := \exp(\ga) \in \exp(\m \hatotimes \g^0)$
and
\begin{equation}
\opn{Af}(g) := \exp(\opn{af}(\ga)) = 
\sum_{i \geq 0} \, \smfrac{1}{i!} \opn{af}(\ga)^i
\in R \hot \bigl( \opn{End}(\g^1) \ltimes \g^1 \bigr)  .
\end{equation}
(The series above converges in the $\m$-adic topology.) 
We get an affine action $\opn{Af}$ of the group $\exp(\m \hatotimes \g^0)$
on the $R$-module $\m \hatotimes \g^{1}$.
For $\om \in \m \hatotimes \g^1$ this becomes
\[ \opn{Af}(g)(\om) = 
\exp(\opn{ad}(\gamma))(\om) + 
\frac{ 1 - \exp(\opn{ad}(\gamma)) }{ \opn{ad}(\gamma) } (\d(\gamma)) . \]
The arguments in \cite[Section 1.3]{GM} (which refer to the case when
$\g^i$ are all finite dimensional over $\K$, $\g^i = 0$ for $i < 0$, and $R$ is
artinian) are valid also in our infinite case (cf.\ \cite[Section 2.2]{Ge}),
and they show that $\opn{Af}(g)$ preserves  the set 
$\opn{MC}(\m \hatotimes \g)$.
(This can be proved also using the method of Lemma \ref{lem:3}.)
We write
\begin{equation}
\ol{\opn{MC}}(\m \hatotimes \g) := 
\frac{ \opn{MC}(\m \hatotimes \g) }{ 
\opn{exp}(\m \hatotimes \g^0) } \ ,
\end{equation}
the quotient set by this action.
Given a homomorphism of DG Lie algebras 
 $\phi : \g \to \h$, and homomorphism of parameter algebras
$f : (R, \m) \to (S, \n)$, there is an induced function 
\begin{equation}
\ol{\opn{MC}}(\phi \ot f) :
\ol{\opn{MC}}(\m \hatotimes \g) \to
\ol{\opn{MC}}(\n \hatotimes \h) .
\end{equation} 

We shall need the following sort of algebraic differential calculus
(which is used a lot implicitly in deformation theory).
Let $\K[t]$ be the polynomial algebra in a variable $t$, and let $M$ be a
$\K$-module. A polynomial 
$f(t) \in \K[t] \otimes M$ defines a 
function $f : \K \to M$, namely for any $\la \in \K$ the element
$f(\la) \in M$ is gotten by substitution $t \mapsto \la$.
We refer to $f : \K \to M$ as a polynomial function, or as 
a polynomial path in $M$. 

Let $\K[\ep] := \K[t] / (t^2)$, where $\ep$ is the class of $t$. 
Given $f(t) \in \K[t] \otimes M$ and $\la \in \K$ we denote by 
$f(\la + \ep) \in \K[\ep] \otimes M$ the result of the substitution 
$t \mapsto \la + \ep$.

\begin{lem} \label{lem:7}
Let $f(t) \in \K[t] \otimes M$. If 
\[ f(\la + \ep)  = f(\la) \]
in $\K[\ep] \otimes M$ for all $\la \in \K$, then $f(\la) = f(0)$
for all $\la \in \K$.
\end{lem}

\begin{proof}
This is an elementary calculation; note that $\K$ has characteristic $0$.
\end{proof}

Given an element $\om \in \opn{MC}(\m \hatotimes \g)$, consider the 
$R$-linear operator (of degree $1$)
\begin{equation} \label{eqn:17}
 \d_{\om} := \d + \opn{ad}(\om) 
\end{equation}
on $\m \hatotimes \g$.

\begin{lem} \label{lem:3}
Let $\om, \om' \in \opn{MC}(\m \hatotimes \g)$,
and let $g \in \opn{exp}(\m \otimes \g^0)$ be such that
$\om' = \opn{Af}(g)(\om)$. 
Then for any $i \in \Z$ the diagram of $R$-modules
\[ \UseTips \xymatrix @C=10ex @R=6ex {
\m \hatotimes \g^{i}
\ar[r]^{\opn{Ad}(g)}
\ar[d]_{\d_{\om}}
&
\m \hatotimes \g^{i}
\ar[d]^{\d_{\om'}}
\\
\m \hatotimes \g^{i+1}
\ar[r]^{\opn{Ad}(g)}
&
\m \hatotimes \g^{i+1}
} \]
is commutative.
\end{lem}

\begin{proof}
Since $\m \hatotimes \g^{i}$ and $\m \hatotimes \g^{i+1}$ are
$\m$-adically complete $R$-modules, it suffices to verify this after replacing
$R$ with $R_j$. Therefore we can assume that $R$ is artinian.

Consider the DG Lie algebra 
$\K[t] \otimes \m \otimes \g$. 
Let $\ga := \log(g) \in \m \otimes \g^0$, and define 
\[ g(t) := \exp(t \ga) \in \exp(\K[t] \otimes \m \otimes \g^0)
\subset \K[t] \otimes R \otimes \opn{End}(\g^0) . \]
So $g(0) = 1$ and $g(1) = g$. Next let 
\[ \om(t) := \opn{Af}(g(t))(\om) \in \K[t] \otimes \m \otimes \g^1 , \]
which is an MC element of $\K[t] \otimes \m \otimes \g$, and it 
satisfies $\om(0) = \om$ and $\om(1) = \om'$. Consider the polynomial 
\[ f(t) := \opn{Ad}(g(1-t)) \circ \d_{\om(t)} \circ \opn{Ad}(g(t)) \in 
\K[t] \otimes R \otimes \opn{Hom}(\g^{i}, \g^{i+1}) . \]
It satisfies  
\[ f(0) = \opn{Ad}(g) \circ \d_{\om} \]
and 
\[ f(1) =  \d_{\om'} \circ \opn{Ad}(g)  . \]
We will prove that $f$ is constant.
See diagram below depicting $f(\la)$, $\la \in \K$.

\[ \UseTips \xymatrix @C=10ex @R=7ex {
\m \otimes \g^{i}
\ar[r]^{\opn{Ad}(g(\la))}
\ar@{-->}[d]
&
\m \otimes \g^{i}
\ar[d]^{\d_{\om(\la)}}
\ar@{-->}[r]
&
\m \otimes \g^{i}
\ar@{-->}[d]
\\
\m \otimes \g^{i+1}
\ar@{-->}[r]
&
\m \otimes \g^{i+1}
\ar[r]^{\opn{Ad}(g(1 - \la))}
&
\m \otimes \g^{i+1}
} \]

\medskip
Take any $\la \in \K$. Then 
\[ \begin{aligned}
& f(\la +\ep) - f(\la) = \\
& \qquad \opn{Ad}(g(1 - \ep - \la)) \circ
\bigl( \d_{\om(\la + \ep)} \circ \opn{Ad}(g(\ep)) -  
\opn{Ad}(g(\ep)) \circ \d_{\om(\la)} \bigr) \circ \opn{Ad}(g(\la)) 
\end{aligned} \]
in $\K[\ep] \otimes R \otimes \opn{Hom}(\g^{i}, \g^{i+1})$.
A calculation shows that 
\[ \opn{Ad}(g(\ep)) = 1 + \ep \cdot \opn{ad}(\ga) \in 
\K[\ep] \otimes R \otimes \opn{End}(\g) \]
and
\[ \om(\la + \ep) = \om(\la) + \ep \cdot [\ga, \om(\la)] - 
\ep \cdot \d(\ga) \in \K[\ep] \otimes \m \otimes \g^1 . \]
Hence for any 
$\al \in R \otimes \g^{-1}$ we have
\[ 
\begin{aligned}
& \bigl( \d_{\om(\la + \ep)} \circ \opn{Ad}(g(\ep)) \bigr)(\al) = \\
& \qquad \d(\al) + \ep \cdot \d([\ga, \al]) 
+ [\om(\la + \ep), \al] + \ep [ \om(\la + \ep), [\ga, \al]]
\end{aligned} \]
and 
\[ \begin{aligned}
& \bigl( \opn{Ad}(g(\ep)) \circ \d_{\om(\la} \bigr)(\al) = \\
& \qquad \d(\al) + [\om(\la), \al] + \ep [\ga, \d(\al)] +
\ep [\ga, [\om(\la), \al ]] \ .
\end{aligned} \]
After expanding terms and using the graded Jacobi identity we see that 
\[ \bigl( \d_{\om(\la + \ep)} \circ \opn{Ad}(g(\ep)) \bigr)(\al) =
\bigl( \opn{Ad}(g(\ep)) \circ \d_{\om(\la} \bigr)(\al) \]
in $\K[\ep] \otimes R \otimes \g^0$.
Therefore $f(\la +\ep) = f(\la)$. By Lemma \ref{lem:7} we conclude that 
$f$ is constant.
\end{proof}

\begin{prop} \label{prop:100}
\begin{enumerate}
\item Let $\om \in \opn{MC}(\m \hot \g)$. Then 
$\d_{\om}$ is a degree $1$ derivation of the graded Lie algebra $\m \hot \g$,
and $\d_{\om} \circ \d_{\om} = 0$. We obtain a new DG Lie algebra 
$(\m \hot \g)_{\om}$, with the same Lie bracket $[-,-]$, and a new differential
$\d_{\om}$.

\item Let $g \in \opn{exp}(\m \hot \g^0)$, and let 
$\om' := \opn{Af}(g)(\om) \in \opn{MC}(\m \hot \g)$. Then 
\[ \opn{Ad}(g) : (\m \hot \g)_{\om} \to (\m \hot \g)_{\om'} \]
is an isomorphism of DG Lie algebras.
\end{enumerate}
\end{prop}

\begin{proof}
(1) This is well known (and very easy to check). 

\medskip \noindent
(2) Let $\ga := \log(g) \in \m \hot \g^0$.
Since $\opn{ad}(\ga)$ is a derivation of the graded Lie algebra 
$\m \hot \g$, it follows that 
$\opn{Ad}(g) = \exp(\opn{ad}(\ga))$ is an automorphism of 
$\m \hot \g$. By Lemma \ref{lem:3} this automorphism exchanges $\d_{\om}$
\and $\d_{\om'}$.
\end{proof}
