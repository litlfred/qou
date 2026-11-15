---
doc_id: arxiv-math-9910019v1
doc_title: "Symmetrized random permutations"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: 9910019v1.pdf
source_sha256: 07dd7ab7068b1482
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.96
doc_brief: "Symmetrized random permutations — 8 sections: Front matter; Introduction; Tracy-Widom distribution functions"
---
\label{sec-intro}

Suppose that we are selecting $n$ points, $p_1,p_2,\cdots,p_n$, 
at random in a rectangle, 
say $R=[0,1]\times[0,1]$ (see Figure \ref{fig-randompoints}). 
We denote by $\pi$ the configuration of $n$ random points.
With probability 1, no two points have same $x$-coordinates nor $y$-coordinates.
An up/right path of $\pi$ 
is a collection of points $p_{i_1},p_{i_2},\cdots,p_{i_k}$ 
such that $x(p_{i_1})<x(p_{i_2})<\cdots<x(p_{i_k})$ 
and $y(p_{i_1})<y(p_{i_2})<\cdots<y(p_{i_k})$.
The length of such a path is defined by the number of the points in the path.
Now we denote by $l_n(\pi)$ the length of the longest up/right path 
of a random points configuration $\pi$.

\begin{figure}[ht]
 \centerline{\epsfig{file=randompoints.eps, width=5cm}}
 \caption{random points in a rectangle}
\label{fig-randompoints}
\end{figure}

As one can see from Figure \ref{fig-randompoints}, a configuration of $n$ 
points gives rise a permutation. 
For the example at hand, the corresponding permutation is 
$\bigl( \begin{smallmatrix}1&2&3&4&5\\5&1&3&2&4\end{smallmatrix}\bigr)$.

Therefore we can identity random points in $R$ and random permutations, 
and we use the same notation $\pi$. 
In this identification, $l_n(\pi)$ is the length of the longest increasing 
subsequence of a random permutation.

The longest increasing subsequence has been of great interest 
for a long time (see e.g. \cite{AD}, \cite{OR}, \cite{BDJ}).
Especially as $n\to\infty$, it is known that 
$\Exp(l_n)\sim 2\sqrt{n}$ \cite{LS}, \cite{VK1, VK2} (also \cite{AD95,
Se95, Jo2})
and $\Var(l_n)\sim c_0n^{1/3}$ \cite{BDJ} 
with some numerical constant $c_0=0.8132\cdots$.
Moreover, the limiting distribution 
of $l_n$ after proper scaling 
is obtained in \cite{BDJ} in terms of the solution to the 
Painlev\'e II equation 
(see Section \ref{sec-result} for precise statement).
An interesting feature is that the above limiting distribution function
is also the limiting 
distribution of the (scaled) largest eigenvalue of a random GUE matrix 
\cite{TW1}, the so-called ``GUE Tracy-Widom distribution'' $F_2$. 
In other words, properly centered and scaled, the length of the longest 
increasing subsequence of a random permutation behaves statistically 
for large $n$ like the largest eigenvalue of a random GUE matrix.
There have been many papers concerning the relations on 
combinatorics and random matrix theory : 
we refer the reader to \cite{Re, Gessel, Kerov, Rains, Jo2, 
BDJ, BDJ2, TW3, Bo, 
kurtj:shape, kurtj:trans, Ok, BOO, TW:randomwords, kurtj:recent, 
BR1, BR2}. 
The purpose of this paper is to survey the analytic results of 
the recent papers \cite{BR1, BR2} 
and discuss related topics.


In random matrix theory, three ensembles play important roles,  GUE, GOE 
and GSE (see e.g. \cite{Mehta}). 
Since random permutation is related to GUE, 
it would be interesting to ask which object in combinatorics is related to 
GOE and GSE. 
For this purpose, we consider symmetrized permutations.
In terms of random points, 5 symmetry types of the rectangle $R$ 
are considered, denoted by the symbols $\tsymmU$, $\tsymmO$,
$\tsymmS$, $\tsymmUU$, and $\tsymmu$. 
Throughout this paper (and also in \cite{BR1, BR2}), the symbol 
$\tsymmg$ is used to denote an arbitrary choice of the above five possibilities.
Let $\delta=\{(t,t):0\le t\le 1\}$, the diagonal line, 
and $\delta^t=\{(t,1-t):0\le t\le 1\}$, the anti-diagonal line.
Consider the following random points selections : 
\begin{enumerate}
\item $\tsymmU$ : select $n$ points in $R$ at random.
\item $\tsymmO$ : select $n$ points in $R\setminus\delta$ 
and $m$ points in $\delta$ at random, and add 
their reflection images about $\delta$.
\item $\tsymmS$ : select $n$ points in $R\setminus\delta^t$ 
and $m$ points in $\delta^t$ at random, and add
their reflection images about $\delta^t$.
\item $\tsymmUU$ : select $n$ points at random in $R$, and add 
their rotational images about the center $(1/2,1/2)$.
\item $\tsymmu$ : select $n$ points in $R\setminus\delta$, 
$m_+$ points in $\delta$ and $m_-$ points in $\delta^t$ at random, 
and add their reflection images about both $\delta$ and $\delta^t$.
\end{enumerate}

Define the map $\iota$ on $S_n$ by $\iota(x)=n+1-x$.
Let $\fp(\pi)$ denote the number of  points satisfying $\pi(x)=x$, 
and $\ifp(\pi)$ denote the number of points satisfying $\pi(x)=\iota(x)$ 
($\ifp$ represents negated points : see Remark \ref{rem-3} below).
Each of the above process corresponds to 
picking a random permutation from each of the following ensembles :
{
\allowdisplaybreaks
\begin{align}
S^\symmU_n &= S_n\\
S^\symmO_{n,m} &= \{\pi\in S_{2n+m}:\pi=\pi^{-1},\ 
\fp(\pi)=m \}\\
S^\symmS_{n,m} &= \{\pi\in S_{2n+m}:\pi=\iota \pi^{-1}\iota ,\ 
\ifp(\pi)=m \}\\
S^\symmUU_n &= \{\pi\in S_{2n}:\pi=\iota\pi\iota\}\\
S^\symmu_{n,m_+,m_-} &= \{\pi\in S_{4n+2m_++2m_-}:
\pi=\pi^{-1},\ \pi=\iota\pi^{-1}\iota,\
\fp(\pi)=2m_+,\ \ifp(\pi)=2m_- \}.
\end{align}
}
We denote the length of the longest increasing subsequence (equivalently, 
the longest up/right path) of $\pi$ in each of the ensemble respectively by 
\begin{equation}
  L^\symmU_n,\quad L^\symmO_{n,m},\quad L^\symmS_{n,m},\quad L^\symmUU_n,\quad 
L^\symmu_{n,m_+,m_-}.
\end{equation}

\begin{rems}
  The map $\pi\mapsto \iota^{-1}\pi$ gives a bijection 
between $S^\symmO_{n,m}$ and $S^\symmS_{n,m}$. 
Thus $L^\symmS_{n,m}$ has the same statistics with the length 
of the longest \emph{decreasing} subsequence of a random 
involution with $m$ fixed points taken from $S^\symmO_{n,m}$.
From the definition, $L^\symmO_{n,m}$ is the random variable describing 
the length of the longest \emph{increasing} subsequence of a random 
involution taken from the same ensemble.
\end{rems}

\begin{rems}\label{rem-2}
  We may identify $S_{2n}$ with the set of bijections from
$\{-n,\cdots,-2,-1,1,2,\cdots,n\}$ onto itself.
In this identification, $S_n^\symmUU$ becomes the set of
signed permutations ; $\pi(x)=-\pi(-x)$.
The longest increasing subsequence problem of a random signed permutation
is considered in \cite{TW3} and \cite{Bo}.
\end{rems}

\begin{rems}\label{rem-3}
  Under the identification in Remark \ref{rem-2}, $S^\symmu_{n,m_+,m_-}$ 
becomes the set of signed involutions with $m_+$ fixed points 
and $m_-$ negated points (we call $x$ a negated point if $\pi(x)=-x$.)
\end{rems}

\bigskip
In this paper, we are interested in the statistics of $L^\symmg$ 
as $n\to\infty$.
Especially for $\tsymmO$, $\tsymmS$ and $\tsymmu$, we 
are interested in the cases when 
$m=[\sqrt{2n}\alpha]$ for $\tsymmO$, $m=[\sqrt{2n}\beta]$ for $\tsymmS$, 
and $m_+=[\sqrt{n}\alpha]$ and $m_-=[\sqrt{n}\beta]$ for $\tsymmu$ 
with fixed $\alpha, \beta \ge 0$ where $[k]$ denotes the largest 
integer less than or equal to $k$.
Then for most cases, the expected values have the same asymptotics.
Namely, if we set $N=n, 2n+m, 2n+m,2n,4n+2m_++2m_-$ for 
each of $\tsymmU, \tsymmO, \tsymmS, \tsymmUU, \tsymmu$ case respectively, 
we have 
\begin{equation}
   \lim_{N\to\infty} \frac{\Exp(L^\symmg)}{\sqrt{N}} =2, 
\end{equation}
when $0\le\alpha\le 1$ and $\beta\ge 0$ are fixed for $\tsymmO$,
$\tsymmS$ and $\tsymmu$.
When $\alpha>1$, we have different expected value in the limit 
(see Section \ref{sec-result}.)

On the other hand, the variance behaves asymptotically 
like $c_0N^{1/3}$ but now with 
different constant $c_0$ depending on the symmetry type.
It is because each symmetry type has different limiting distribution : 
$L^\symmU_n$ has GUE fluctuation, $L^\symmS_{n,m}$ GOE fluctuation 
and $L^\symmUU_n$ $\text{GUE}^2$
fluctuation 
(see Section \ref{sec-result} below for precise statements).
Here $\text{GUE}^2$ denotes the statistics of 
a superimposition of eigenvalues of two random GUE matrices.
Similarly for $\text{GOE}^2$.
The cases of $\tsymmO$ and $\tsymmu$ show more interesting features.
For $\tsymmO$, the limiting distribution function changes depending on 
the value of $\alpha=m/\sqrt{2n}$. 
The fluctuation is GSE when $\alpha<1$, GOE when $\alpha=1$ 
and Gaussian when $\alpha>1$.
By taking suitable scaling limit $\alpha\to 1$, we can find a certain smooth 
transition between GSE and GOE.
For $\tsymmu$, the value $\alpha=m_+/\sqrt{n}$ determines the limiting 
distribution ; the value $m_-$ plays no role in the transition.
The fluctuation is 
GUE when $\alpha<1$, $\text{GOE}^2$ when $\alpha=1$,
and Gaussian when $\alpha>1$.

In Section \ref{sec-dist}, we define 
the Tracy-Widom distributions for GUE, GOE and GSE as well as new classes of 
distribution functions describing the transition around $\alpha=1$.
Main results are stated in Section \ref{sec-result}, and 
Section 4 includes some applications and the related problems.
Most of the results in this article are taken from 
\cite{BR1, BR2}. 
The only new result is Theorem \ref{thm-4.2}.

\medskip
\noindent {\bf Acknowledgments.}
The authors would like to thank organizers of the workshop 
\emph{Random Matrix Models and their Applications} for their invitations.
