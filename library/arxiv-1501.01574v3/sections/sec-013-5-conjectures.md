---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-013-5-conjectures
section_title: "Conjectures"
section_number: 5
pages: 22-23
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
text_source: latex
latex_prose_ratio: 0.632
latex_coverage_ratio: 1.0
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polyn omial and the boundary slopes of knots under the operation of cabling."
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


\subsection{Non-alternating Montesinos knots up to nine crossings} Table 2 summarizes the relevant information 
about these knots.
The Jones slopes and  the sets of cluster points 
$\{2b_K(n)\}', \{2b_K^{*}(n)\}'$ were obtained from Garoufalidis' paper \cite{Ga-slope}.
The corresponding
boundary slopes together with the values $\chi(S)$ and $\abs{\partial S}$ were obtained using Dunfield's program for calculating boundary slopes of Montesinos knots \cite{ndunfield}.
In all cases,  Conjectures \ref{conj} and \ref{slopeaug} are easily verified for the knots and their mirror images.
Note that, for example, for $9_{44}$
we have $a/b=14/3 \in js_K$, $\{2b_K(n)\}'=\{-2, -8/3\}$, and $\frac{\chi(S)}{{\abs{\partial S} b}} =\frac{-6}{3}=-2$ as predicted
by  Conjecture \ref{slopeaug}. However, this assertion alone  doesn't guarantee that $b_K(n)\le 0$. Thus,
in general,   Conjecture \ref{slopeaug} does not imply Conjecture \ref{conj}.

\begin{table}[]
\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|c|c|}
\hline
$K$& $js_K$ & $jx_{K}$ & $\chi(S)$ & $|\partial{S}|$ & $js^*_K$ & $jx_K^*(n)$ & $\chi(S^*)$ & $|\partial{S^*}|$\\
\hline
$8_{19}$ & $\{12\}$ &   $\{0\}$ & $0$ & $2$ & $\{0\}$ & $\{5\}$ & $-5$ & $1$ \\
\hline
$8_{20}$ &$\{ 8/3\}$  &$\{-1, -5/3\}$  & $-3$ & $1$ & $\{-10\}$& $\{4\}$ &$-4$ &$1$\\
\hline
$8_{21}$ & $\{1\}$ &  $\{-2\}$ & $-4$ & $2$ & $\{-12\}$ & $\{3\}$ &$-3$ &$1$\\
\hline
$9_{42}$  & $\{6\}$ &  $\{-1\}$ & $-2$ & $2$ & $\{-8\}$ & $\{5\}$ &$-5$ &$1$\\
\hline
$9_{43}$  & $\{ 32/3\}$ &  $\{-1, -5/3\}$ & $-3$& $1$ & $\{-4\}$& $\{5\}$ &$-5$ &$1$\\
\hline
$9_{44}$ & $\{ 14/3\}$ & $\{-2, -8/3\}$  &$-6$ &$1$ & $\{-10\}$ & $\{4\}$ &$-4$ &$1$\\
\hline
$9_{45}$  & $\{ 1\}$ &  $\{-2\}$ &$-4$ &$2$ & $\{-14\}$& $\{4\}$ &$-4$&$1$\\
\hline
$9_{46}$  & $\{ 2\}$ &  $\{-1\}$ &$-2$ &$2$& $\{-12\}$ & $\{5\}$ &$-5$&$1$\\
\hline
$9_{48}$ & $\{11\}$ &  $\{-3\}$ &$-6$ & $2$ &$\{-4\}$& $\{3\}$ &$-3$&$1$\\
\hline
 \end{tabular}
\vskip 0.3in 
\caption{Non-alternating Montesinos knots up to nine crossings.}
\end{center}
\end{table}

\begin{corollary}\label{conjcables} Suppose that $K\in \{ 8_{19},  8_{21}, 9_{42}, 9_{45}, 9_{46},
9_{48}, 9_{49} \}$ and let $K'$ be an iterated cable of $K$. Then, Conjectures \ref{conj} and  \ref{slopeaug}
hold true for $K'$.
\end{corollary}
\begin{proof}
We first note that $
d_+[J_{K}(n)]=an^2+bn+d(n)
$
is a quadratic quasi-polynomial of period $\le 2$, with $4a \in \BZ, 2b \in \BZ$ and $b \le 0$. Suppose
${K_{p,q}}$ is cable of $K$.
Theorem \ref{thm-quasi} and the proof of Proposition \ref{quasi} then imply that 
$$
d_+[J_{K_{p,q}}(n)]=An^2+Bn+D(n)
$$
is a quadratic quasi-polynomial of period $\le 2$, with $4A \in \BZ, 2B \in \BZ$ and $B \le 0$.
Moreover, the proof of Proposition \ref{quasi} shows that one of the following is true:
\begin{enumerate}
\item We have $4A=pq$ and $B=0$.
\item We have $4A=4q^2a$ and $2B=2 \abs{q} b+ (1- \abs{q}) \abs{4aq-p}$.

\end{enumerate}
 In case (1), a surface $S$ with boundary slope $pq$ is the cabling annulus; thus $\chi(S)=0=2B$
and Conjectures \ref{conj} and  \ref{slopeaug} are satisfied.
In case (2),  let $S$ be a surface that satisfies Conjecture \ref{slopeaug}
for $K$. We view $\M$ as the union of $M_K$ and a cable space $\C$.
An essential  surface $S'$ realizing the boundary slope $4A=4q^2a$ for $\K$ 
is obtained by Theorem \ref{main:bs}. This surface is constructed as in the proof of Lemma \ref{glue}.
By  Corollary \ref{integers} we see that $\abs{\partial S'}=\abs{\partial S}$,
$\abs {S'\cap T_{+}}=\abs{q} \, \abs{\partial S}$ and
$$\chi(S')=\chi(M_K\cap S')+\chi(\C \cap S')=\abs{q}  \chi(S)+\abs{\partial S} \, \abs{4aq-p} (1- \abs{q} ).$$
By assumption, $\chi(S)=\abs{\partial S} (2b)$.
Combining the last  two equations with the formula in (2) above, we have
$$\chi(S')=\abs{\partial S} \left( 2 \abs{q} b+ (1-\abs{q}) \abs{4aq-p}\right)=\abs{\partial S'}(2B),$$
which shows that $S'$ satisfies Conjecture \ref{slopeaug}.

Applying the above argument repeatedly we obtain the result for iterated cables.
\end{proof}






\subsection{A family of pretzel knots}
 Consider the pretzel knot $K_p=(-2,3,p)$, where $p$ is an odd integer. It is known that $K_p$ is $A$-adequate if $p>0$, and $B$-adequate if $p<0$. Moreover, $K_p$ is a torus knot if $p \in \{1,3,5\}$. 

 
Suppose now that  $p \ge 5$. Then $K_p$ is $A$-adequate and  by above discussion Conjecture  \ref{slopeaug} 
holds  for
the mirror image $K_p^{*}$.


By \cite[Section 4.7]{Ga-slope} and Example 6.3 below we have $$4a_{K_p}(n) = 2(p^2-p-5)/(p-3) \quad \text{and} \quad 2b_{K_p}(n) = 
-(p-5)/(p-3).$$

Since $4a_{K_p}(n)$ is not an integer, in fact it is easily checked that $ \gcd ( 2(p^2-p-5), p-3)=1$, $K_p$ is not $B$-adequate.
Thus we can't apply Theorem  \ref{slopeadequate}. Note moreover that $\gcd(p-5, p-3)=2$.
By  \cite[Theorem 3.3]{callahan}, $K_p$ has an essential surface with boundary slope $2(p^2-p-5)/(p-3)$, with two boundary components, and Euler characteristic $-(p-5)$, which is equal to $(p-3)(2b_{K_p}(n))$.   
Note that for $p=5$ we get $b_{K_p}(n)=0$. The knot $K=(2,-3,5)$ is known to be a torus knot, which is in agreement with Conjecture \ref{conj}.


Suppose now that $p \le -1$. Then $K$ is $B$-adequate. By \cite[Section 4.7]{Ga-slope} and Example 6.3
we have $4a^*_{K_p}(n) = 2(p+1)^2/p$ and $$2b^*_{K_p}(n) = 
\begin{cases}
1 &\mbox{if } n \not\equiv 0 \pmod{p} \\ 
1 - 2/p & \mbox{if } n \equiv 0 \pmod{p}.
\end{cases}$$

Again since $4a^*_{K_p}(n)$ is not an integer, $K_p$ is not $A$-adequate and Theorem  \ref{slopeadequate} doesn't apply to $K_p^*$.
According to \cite[Theorem 3.3]{callahan}, 
 $K_p$ has an essential surface with boundary slope $2(p+1)^2/p$ and Euler characteristic $p$, which is equal to $p(2b_{K_p}(n))$ when $n \not\equiv 0 \pmod{p}$. Thus we have:
 
\begin{corollary} For an odd integer $p$,  the pretzel knots  $K_p=(-2,3,p)$ and $K^{*}_p$
satisfy Conjectures \ref{conj} and \ref{slopeaug}. 
\end{corollary}
