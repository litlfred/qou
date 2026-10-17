---
doc_id: arxiv-1501.04614v1
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1501.04614v1.pdf
source_sha256: ebebcae0c1823217
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.966
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES — We continue our study of the degree of the colored Jones polynomial under knot cabling started in [8]."
---
For a knot $K \subset S^3$, let $n(K)$ denote a tubular neighborhood of
$K$ and let $M_K:=\overline{ S^3\setminus n(K)}$ denote the exterior of
$K$. Let $\langle \mu, \lambda \rangle$ be the canonical
meridian--longitude basis of $H_1 (\bdy n(K))$.  An element $a/b \in
{\QQ}\cup \{ 1/0\}$ is called a \emph{boundary slope} of $K$ if there
is a properly embedded essential surface $(S, \bdy S) \subset (M_K,
\bdy n(K))$, such that  $\bdy S$ represents $a \mu + b \lambda \in
H_1 (\bdy n(K))$.  Hatcher showed that every knot $K \subset S^3$
has finitely many boundary slopes \cite{hatcher}.
We will use $bs_K$ to denote the set of boundary slopes of $K$.

For a Laurent polynomial $f(v) \in \BC[v^{\pm 1/4}]$, let $d_+[f]$  be the highest degree of $f$ in $v$. For a knot $K \subset S^3$, Garoufalidis \cite{Ga-quasi} proved that the highest degree of its colored Jones polynomial is a quadratic quasi-polynomial. This means that there exist an integer $N_K>0$ and periodic functions $a_{K}(n), b_{K}(n), c_{K}(n)$ such that 
$$d_+[J_K(n)] = a_{K}(n) \, n^2 + b_{K}(n) n + c_{K}(n)$$
for $n \ge N_K$.  The common period of $a_{K}(n), b_{K}(n) ,  c_{K}(n)$ is called the period of $K$.
Let $d_-[J_K(n)]$ denote the lowest degree of $J_K(n)$ in $v$.
For a sequence $\{x_n\}$, let $\{x_n\}'$ denote the set of its cluster points. Elements of the set
$$js_K:= \left\{ 4n^{-2}d_+[J_K(n)]  \right\}' \quad
 \mbox{and} \quad js^*_K:= \left\{ 4n^{-2}d_-[J_K(n)] \right\}' $$
 are called {\em Jones slopes} of $K$. 
It is known that
 $J_K(n, v) = J_{K^*}(n, v^{-1})$, where $K^*$ is the mirror image of $K$. Thus statements about the lowest degree 
$d_-[J_K(n)]$, which is equal to $- d_+[J_{K^*}(n)]$,  can be equivalently made. With this in mind we will mostly discuss the highest degree in this paper.

In \cite {Effie-Anh-slope}  we studied the behavior of $d_+[J_K(n)]$ under knot cabling for knots of period at most two.
In this paper we study knots with period greater than two.

To state our results, let $K$ be a knot with framing 0, and $p,q$ are co-prime integers.
The $(p,q)$-cable $K_{p,q}$ of $K$ is the $0$-framed satellite of $K$ with
pattern $(p,q)$ torus knot. It is known that $K_{-p,-q}=\text{r}K_{p,q}$, where $\text{r}K_{p,q}$ denotes $\K$ with the opposite orientation, and that the colored Jones polynomial of a \textit{knot} is independent of the orientation of the knot. Hence in the statements of results below, and throughout the paper,  we will assume that our cables are non-trivial in the  sense  that $q>1$.


 \begin{theorem}
 \label{thm-quasi-constant}
 Let $K$ be a knot such that for $n \gg 0$ we have
$$
d_+[J_K(n)]=an^2+b(n)n+d(n)
$$
where $a$ is a constant, $b(n)$ and $d(n)$ are periodic functions with $b(n) \le 0$. Let \begin{eqnarray*}
M_1 &=&  \max\{|b(i)-b(j)| \, : \,  i \equiv j \pmod{2}\},\\
M_2 &=& \max\{2b(i) + |b(i)-b(j)| + |d(i)-d(j)| \, : \, i \equiv j \pmod{2}\}.
\end{eqnarray*}

Suppose $p- (4a-M_1)q < 0$ or $p- (4a + M_1)q > \max\{0,M_2\}$. Then for $n \gg 0$ we have
$$d_+[J_{\K}(n)]=An^2+B(n)n+D(n)$$
where $A$ is a constant, and $B(n), D(n)$ are periodic functions with $B(n) \le 0$. Moreover, if $js_K \subset bs_K$ then $js_{\K} \subset bs_{\K}$.
 \end{theorem}


Theorem \ref{thm-quasi-constant} has applications to two open conjectures about the degree of  $J_K(n)$.
The first conjecture, formulated by the authors in  \cite{Effie-Anh-slope},  asserts  that the linear part
$b_K(n)$ is not positive and it detects the existence of essential annuli in the knot complement.



\begin{conjecture} \cite{Effie-Anh-slope}
\label{conj}
For every non-trivial knot $K \subset S^3$, we have $$b_K(n) \le 0.$$
Moreover, if $b_K(n)=0$ then   $K$ is a composite knot or  a cable knot or a torus knot. 
\end{conjecture}

Note that $b_U(n)=1/2$ for the trivial knot $U$. 
 It is known that a knot $K$ is composite or cable or a torus knot if and only if its complement $M_K$ contains  embedded essential annuli \cite[Lemma V.1.3.4]{jacoshalen}. Thus the last part of Conjecture \ref{conj} can alternatively be stated as
follows: If $b_K(n)=0$, then $M_K$ contains an embedded essential  annulus.

The second conjecture is the Slope Conjecture formulated by Garoufalidis in  \cite{Ga-slope}.


\begin{conjecture} [Slope Conjecture] \cite{Ga-slope}
\label{slope}
For every knot $K \subset S^3$ we have 
$$js_K : = \{4a_K(n)\} \subset bs_K.$$
\end{conjecture}

Conjecture  \ref{slope} is known for the following classes of knots:
\begin{enumerate}

\item alternating knots, non-alternating knots with up to nine crossings, torus knots, the family ($-2, 3, 2m+3)$ of 3-string pretzel  knots (by Garoufalidis \cite{Ga-slope}).

\item adequate knots (by Futer, Kalfagianni and Purcell \cite{FKP}).



\item iterated cable knots of $B$-adequate knots,  iterated torus knots, and iterated of all non-alternating knots with up to nine crossings that have period two  (by Kalfagianni and Tran \cite{Effie-Anh-slope}).

\item a certain 2-parameter family of closed 3-braids, called 2-fusion knots (by Garoufalidis and Dunfield \cite{DG} and Garoufalidis and van der Veen \cite{GV}).



\item some families of 3-string pretzel knots (by Lee and van der Veen \cite{leV}).
\end{enumerate}


In this paper we will verify Conjecture \ref{conj} for 2-fusion knots and ``most" of their cables. For cases (1)-(3) 
the conjecture was verified in  \cite{Effie-Anh-slope}.
Theorem \ref{thm-quasi-constant} implies the following.

\begin{corollary} \label{cables}
 Let $K$ be a knot such that for $n \gg 0$ we have
$$
d_+[J_K(n)]=an^2+b(n)n+d(n)
$$
where $a$ is a constant, $b(n)$ and $d(n)$ are periodic functions. Let $M_1, M_2$
be as in the statement of Theorem \ref{thm-quasi-constant}.
If $K$ satisfies Conjectures \ref{conj}  and  \ref{slope}, then
$\K$ satisfies the conjectures  provided that  $p- (4a-M_1)q < 0$ or $p- (4a + M_1)q > \max\{0,M_2\}$. 
 \end{corollary}

As an application of  Corollary \ref{cables} we will prove Conjectures \ref{conj}  and  \ref{slope}
for cables of 2-fusion knots.

We would like to thank Stavros Garoufalidis for helpful correspondence.
