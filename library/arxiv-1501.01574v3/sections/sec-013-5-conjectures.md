---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-013-5-conjectures
section_title: "Conjectures"
section_number: 5
pages: 22-23
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 1.0
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polynomial and the boundary slopes of knots under the operation of cabling."
---
Recall that for every knot $K \subset S^3$, there is an integer $N_K>0$ and periodic functions $a_{K}(n), b_{K}(n), c_{K}(n)$ such that 
$$d_+[J_K(n)] = a_{K}(n) \, n^2 + b_{K}(n) n + c_{K}(n)$$
for $n \ge N_K$.   In Propositions \ref{quasi}  and \ref{quasi-constant} we made the assumption that  $b(n) \le 0$. Then we concluded that, under the appropriate hypotheses, this property
is preserved under cabling. As we will discuss below, the property that $b(n)\leq 0$ is known to hold  
for all non-trivial knots, of any period,  for which $b_K(n)$ has been calculated.

We propose the following conjecture. 

\begin{conjecture}
\label{conj}
For every non-trivial knot $K \subset S^3$, we have $$b_K(n) \le 0.$$
Moreover, if $b_K(n)=0$ then   $K$ is a composite knot or  a cable knot or a torus knot. 
\end{conjecture}
Note that $b_U(n)=1/2$ for the trivial knot $U$. 

\begin{remark} It is known that a knot $K$ is composite or cable or a torus knot if and only if its complement $M_K$ contains  embedded essential annuli \cite[Lemma V.1.3.4]{jacoshalen}. Thus the last part of Conjecture \ref{conj} can alternatively be stated as
follows: If $b_K(n)=0$, then $M_K$ contains an embedded essential  annulus.
\end{remark}

By Theorem \ref{slopeadequate}, for $B$-adequate knots and their  iterated cables we have $b_K(n) \le 0$.
Moreover, if $K$ is a $B$-adequate knot and $2b=v_B-c=0$, then  by Lemma \ref{v_B-c}
$K$ is a torus knot.
Thus Conjecture \ref{conj} holds for $B$-adequate knots and their cables.
 Notice that,
as shown in the proof of Theorem \ref{slopeadequate}, the case $b_K(n)=0$ occurs quite often for cables of $B$-adequate knots.
Conjecture \ref{conj} holds for the knots of  Table 1. In the next section we will check that Conjecture \ref{conj} holds true for 
 2-fusion knots.
 Thus the conjecture holds for all
 the classes of knots for which
$ d_+[J_{K}(n)] $ and $ d_-[J_{K}(n)]$ have been calculated to date.
\medskip

We now turn our attention to the Strong Slope Conjecture (Conjecture \ref{slopeaug})  stated in the Introduction.
By Theorem \ref{slopeadequate}, Conjecture \ref{slopeaug} is true for iterated cables of $B$-adequate knots (and in particular iterated torus knots).
Furthermore,  the arguments in the proofs of Corollary \ref{integers} and  Theorem \ref{slopeadequate} generalize easily to show that, under the hypothesis of Proposition \ref{quasi} or Proposition \ref{quasi-constant}, the Strong Slope Conjecture is closed under knot cabling. For instance we have the following:

\begin{corollary}
Let $K$ be a knot such that for $n \gg 0$ we have
$d_+[J_K(n)]$
is a quadratic quasi-polynomial of period $\le 2$. Suppose $p/q$ is not a Jones slope of $K$. Then if $K$ satisfies Conjecture \ref{slopeaug} so does $K_{p/q}$.
\end{corollary}


\begin{remark}Similar ones to Conjectures \ref{conj} and \ref{slopeaug}  can also be formulated  for the lowest degree of the colored Jones polynomial by noting that $J_K(n, v) = J_{K^*}(n, v^{-1})$, where $K^*$ is the mirror image of $K$. To illustrate this
point  we discuss the example of the knot $9_{49}$. This knot has genus two and is not $B$-adequate since the leading coefficient of its colored Jones polynomial 
is 2 \cite{Ga-slope}
and not $\pm 1$.  By Table 1, $ js^*_K=\{0\} $ and $2b_K^*(n)=3$.
A genus two Seifert surface $S$,  has boundary  slope $0=a_K^*(n)$ and $\chi(S)=-3=-2b_K^*(n)$. Thus   
Conjectures  \ref{conj} and \ref{slopeaug} 
hold for
the mirror image $9^{*}_{49}$. We also mention that  the same is true for $9_{49}$ since it is known to be $A$--adequate.
\end{remark}

 Next we 
discuss more families of knots, not covered by Theorem  \ref{slopeadequate},
for which the above conjectures are true.
