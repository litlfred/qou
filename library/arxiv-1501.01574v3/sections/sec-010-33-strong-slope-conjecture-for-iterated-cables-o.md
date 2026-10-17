---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-010-33-strong-slope-conjecture-for-iterated-cables-o
section_title: "Strong Slope Conjecture for iterated cables of adequate knots"
section_number: 3.3
pages: 14-17
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.937
latex_coverage_ratio: 0.975
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polynomial and the boundary slopes of knots under the operation of cabling."
---
Let $D$ be a link diagram, and $x$ a crossing of $D$.  Associated to
$D$ and $x$ are two link diagrams, each with one fewer crossing than
$D$, called the \emph{$A$--resolution} and \emph{$B$--resolution} of
the crossing. See Figure \ref{resolutions}.

A Kauffman state $\sigma$ is a choice of $A$--resolution or
$B$--resolution at each crossing of $D$. Corresponding to every state
$\sigma$ is a crossing--free diagram $s_\sigma$: this is a collection
of circles in the projection plane. We can encode the choices that lead
to the state $\sigma$ in a graph $G_\sigma$, as follows. The vertices
of $G_\sigma$ are in $1-1$ correspondence with the state circles of
$s_\sigma$. Every crossing $x$ of $D$ corresponds to a pair of arcs
that belong to circles of $s_\sigma$; this crossing gives rise to an
edge in $G_\sigma$ whose endpoints are the state circles containing
those arcs.



Every Kauffman state $\sigma$ also gives rise to a surface $S_\sigma$,
as follows. Each state circle of $\sigma$ bounds a disk in $S^3$. This
collection of disks can be disjointly embedded in the ball below the
projection plane. At each crossing of $D$, we connect the pair of
neighboring disks by a half-twisted band to construct a surface
$S_\sigma \subset S^3$ whose boundary is $K$. See Figure
\ref{statesurface} for an example where $\sigma$ is the all--$B$
state.




\begin{figure}
  \includegraphics{splicing.eps}
  
  \caption{From left to right: A crossing, the $A$-resolution and  the
 the $B$-resolution.}
    
  \label{resolutions}
\end{figure}



\begin{figure}
  \includegraphics{Effie-example.eps} \hspace{.2in}
  \includegraphics{Effie-HA.eps} \hspace{.2in}
  \includegraphics{Effie-SA.eps}
  \caption{From left to right: An example link diagram, the graph
    $\G_{\sigma}$ corresponding to state surface
    $S_{\sigma}$. \thanks{Figure borrowed from \cite{fkp:qsf}.}}
  \label{statesurface}
\end{figure}


\begin{define}\label{defi:adequate}
A link diagram $D$ is called \emph{$A$--adequate} if the state graph
$\GA$ corresponding to the all--$A$ state contains no 1--edge loops.
Similarly, $D$ is called \emph{$B$--adequate} if the all--$B$ graph $\GB$
contains no 1--edge loops.  A link diagram 
is \emph{adequate} if it is
both $A$-- and $B$--adequate.  A link that admits an adequate diagram
is also called \emph{adequate}.
\end{define}

The number of negative crossings  $c_-$  of an $A$--adequate knot diagram is a knot invariant.
Similarly, the number of positive crossings $c_+$ of  a  $B$-adequate knot diagram is a knot invariant.
Let $v_A$ (resp. $v_B$) be the number of state circles in the all--$A$ (resp. all--$B$) state of the knot diagram $D$.

The following summarizes \cite[Lemma 5.4]{Li}, \cite[Proposition 2.1]{Le06} and \cite[Theorem 3.1]{KL}.

\begin{lemma} 
\label{degLe}
Let $D$ be a diagram of a knot $K$.

(1) We have
$$2 \, d_-[J_{K}(n)] \ge  -c_- n^2 + (c -v_A) n  + v_A - c_+.$$
Equality holds for all $n \ge 1$ if $D$ is $A$--adequate. Moreover, if equality holds for some $n \ge 3$ then $D$ is $A$--adequate.

(2) We have
$$
2 \, d_+[J_{K}(n)] \le c_+ n^2 + (v_B - c) n + c_- - v_B.
$$
Equality holds for all $n \ge 1$ if $D$ is $B$--adequate. Moreover, if equality holds for some $n \ge 3$ then $D$ is $B$--adequate.
\end{lemma}



The following theorem, which implies that the Slope Conjecture is true for adequate knots, summarizes results proved in   \cite{FKP, FKP-guts}.

\begin{theorem}\label{thm:essential} 
Let $D$ be an $A$--adequate diagram of a knot $K$. Then the state
surface $S_A$ is essential  in the knot
complement $M_K$, and it  has boundary slope $-2c_-$. Furthermore, we have
$$-2c_- = \lim_{n \to \infty} 4\, n^{-2}d_-[J_K(n)].$$

Similarly, if $D$ is a $B$--adequate diagram of a
knot $K$, then $S_B$ is essential in the knot 
complement $M_K$, and it  has boundary slope $-2c_+$.
 Furthermore, we have
$$2c_+ =  \lim_{n \to \infty} 4\, n^{-2}d_+[J_K(n)].$$
\end{theorem}

By Lemma 
\ref{degLe}, the highest degree of the colored Jones polynomial of a $B$-adequate knot is 
an actual quadratic polynomial in $n$. That is the period is one.  The following lemma shows that
the term $b\leq 0$ and thus non-trivial $B$-adequate knots satisfy the hypothesis of Proposition \ref{quasi}.


\begin{lemma}
\label{v_B-c}
Suppose $D$ is a diagram of a non-trivial knot $K$. Then $v_B \le c$. Furthermore, 
if  $v_B = c$ then $K$ is a torus knot.
\end{lemma}

\begin{proof} Let $D$ be a diagram of a non-trivial knot and let $S_B$ be the all-$B$ state surface obtained from $D$.
Recall that $S_B$ is a surface with a single boundary component obtained by starting with $v_B$ disks 
and attaching 
a half-twisted band for each crossing of $D$. Thus the Euler characteristic of $S_B$ is
$\chi(S_B)=v_B-c$. Since $D$ represents a non-trivial knot, we have
$\chi(S_B)\le 0$ and thus $v_B \le c$.

If $\chi(S_B)= v_B-c=0$, then  (since $\partial S_B$ has one component) $S_B$ must be a Mobius band. This implies
that $D$ is the standard closed 2-braid diagram of   a $(2, q)$-torus  knot.
\end{proof}

The above discussion shows that the first part of Theorem \ref{thm-quasi} applies to non-trivial $B$--adequate knots. Similarly the second part of the theorem applies to non-trivial $A$--adequate knots.
We are now ready to  prove  the following theorem that implies Theorem \ref{main:js} stated in the introduction. 



\begin{theorem}\label{slopeadequate}
Let $K$ be a $B$-adequate knot and $K':=K_{(p_1,q_1),(p_2,q_2), \cdots, (p_r,q_r)}$ an iterated cable knot of $K$. 
Then we have $js_{K'} \subset bs_{K'}$.
Furthermore, for $n \gg 0$, 
$$
d_+[J_{K'}(n)]=An^2+Bn+D(n),
$$
is a quadratic quasi-polynomial of period $\le 2$, with $4A \in \BZ$,  $2B \in \BZ$ and $B \le 0$, and there is an essential surface $S'$ in the complement of $K'$  
with boundary slope $4A$ and such that $\chi(S')=2B$. In particular $K'$ satisfies the Strong Slope Conjecture.
\end{theorem}

\begin{proof}
Suppose $K$ is a $B$--adequate knot. First, we prove that the conclusion of Theorem \ref{slopeadequate} holds true for the cable knot $K_{p_1,q_1}$. We will distinguish two cases according to whether $K$ is a non-trivial knot or not.

\smallskip

\underline{\textit{Case 1.}}\ Suppose that $K$ is non-trivial. 
Then, by Lemmas \ref{degLe} and \ref{v_B-c} we have
$$
d_+[J_K(n)]=an^2+bn+d
$$
for $n>0$, where $a=c_+/2$, $b = (v_B - c)/2 \le 0$ and $d = (c_- - v_B)/2$. 
By Theorem \ref{thm:essential}, $4a=2c_+$ is a boundary slope of $K$. 
Furthermore, an essential surface that realizes this boundary slope
is the state surface $S_B$. Since $S_B$ is constructed by joining $v_B$ disks with $c$ bands we have $\abs{\bdy S_B}=1$ and $\chi(S_B)=v_B-c=2b$. Thus the conclusion is true in this case.

Now we consider a  cable  $K_{p_1,q_1}$ of $K$.
Since $\abs{q_1}>1$, and the Jones slopes of $K$ are integers,
we have  $\frac{p_1}{q_1} \notin js_K$. 
Theorem \ref{thm-quasi} and the proof of Proposition \ref{quasi} then imply that
$$
d_+[J_{K_{p_1,q_1}}(n)]=A_1 n^2+B_1n+D_1(n)
$$
is a quadratic quasi-polynomial of period $\le 2$, with $4A_1 \in \BZ, 2B_1 \in \BZ$ and $B_1 \le 0$.
Moreover, since $js_K \subset bs_K$ we have $js_{K_{p_1,q_1}} \subset bs_{K_{p_1,q_1}}$.
Furthermore, the proof of Proposition \ref{quasi} show that one of the following is true:
\begin{enumerate}
\item We have $4A_1=pq$ and $B_1=0$.
\item We have $4A_1=4q^2a$ and $2B_1=2 \abs{q} b+ (1- \abs{q}) \abs{4aq-p}$.

\end{enumerate}
 In case (1), the surface $S$ with boundary slope $pq$ is the cabling annulus; thus $\chi(S)=0=2B_1$.
In case (2), an essential  surface $S$ realizing the boundary slope $4A_1=4q^2a=2q^2c_{+}$
is obtained by Theorem \ref{main:bs}.  By Corollary \ref{integers} we have $\abs{\bdy S} = \abs{\bdy S_B} = 1$ and 
$\chi(S)= \abs{q} \chi(S_B)+ (1- \abs{q}) \abs{4aq-p}=2B_1$. Thus the conclusion follows for  $K_{p_1,q_1}$.

\smallskip

\underline{\textit{Case 2.}}\
Suppose that $K$ is the trivial knot.  Then $K_{p_1,q_1}$ is the $(p_1,q_1)$-torus knot. Note that $0$ and $p_1q_1$ are boundary slopes of $K_{p_1,q_1}$; realized by a Seifert surface and an annulus respectively.

 For $n>0$, by \cite{Mo} (or by equation \eqref{cables}) we have
$$J_{K_{p_1,q_1}}(n)= v^{p_1q_1(n^2-1)/4} \sum_{k \in \CS_n} v^{-p_1k(q_1k+1)} \frac{v^{(2qk+1)/2}-v^{-(2qk+1)/2}}{v^{1/2}-v^{-1/2}}.$$
By \cite[Section 4.8]{Ga-slope}, \cite[Lemma 1.4]{Tr-strongAJ} and \cite[Lemma 2.1]{RZ}, we have the following. If $p_1>0$ and $q_1>0$ then
$$d_+[J_{K_{p_1,q_1}}(n)]= \big( p_1q_1n^2+d(n) \big)/4$$
where $d(n)=-p_1q_1-\frac{1}{2} \big( 1+(-1)^{n}\big)(p_1-2)(q_1-2)$ is a periodic sequence of period $\le 2$. In this case we have $A_1(n) = p_1q_1/4$ and $B_1(n) = 0$.

If $p_1<0<q_1$ then 
$$d_+[J_{K_{p_1,q_1}}(n)]= \big( (p_1q_1-p_1+q_1)n-(p_1q_1-p_1+q_1) \big)/2.$$
In this case we have $A_1(n) = 0$ and $B_1(n) = (p_1q_1-p_1+q_1)/2$. Note that $p_1q_1-p_1+q_1=1+(p_1+1)(q_1-1) \le 0$. 


In both cases we have that $$
d_+[J_{K_{p_1,q_1}}(n)]=A_1n^2+B_1n+D_1(n)
$$
is a quadratic quasi-polynomial of period $\le 2$, with $4A_1 \in \BZ, 2B_1 \in \BZ$ and $B_1 \le 0$. Moreover, we have $$js_{K_{p_1,q_1}} \subset bs_{K_{p_1,q_1}}.$$

For $p_1>0$ and $q_1 >0$, an essential surface with slope $p_1q_1$ for $K_{p_1,q_1}$ is the cabling annulus $A$; thus $\chi(A_1)=0=2B_1$.
For $p_1<0<q_1$, the genus of $K_{p_1,q_1}$ is $g= -(q_1-1)(p_1+1)/2$.
A Seifert surface $S$ of minimal genus for $K_{p_1,q_1}$ has boundary slope $0$ and 
$\chi(S)=1-2g=p_1q_1-p_1+q_1=2B_1$. This proves the desired conclusion for the torus knot $K_{p_1,q_1}$.

We have proved that the conclusion of Theorem \ref{slopeadequate} holds true for the cable knot $K_{p_1,q_1}$. Now, applying the arguments in Case 1 repeatedly will finish the proof of the theorem for iterated cables.
\end{proof}



 
\subsection{ Proof of Theorem \ref{main:js}}   Part (1) is immediate from Theorem \ref{slopeadequate}.
Suppose now that $K$ is $A$-adequate. Then the mirror image $K^{*}$ is $B$-adequate.
Furthermore, $J_{K^{*}}(n)$ is obtained from $J_{K}(n)$ by replacing $v$ with $v^{-1}$. Thus in this case the result will follow
by applying  Theorem \ref{slopeadequate} to $K^{*}$.
\smallskip
