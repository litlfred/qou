---
doc_id: arxiv-math-9910019v1
doc_title: "Symmetrized random permutations"
section_id: sec-004-41-random-involutions-and-random-signed-involuti
section_title: "Random involutions and random signed involutions"
section_number: 4.1
pages: 9-11
source_pdf: 9910019v1.pdf
source_sha256: 07dd7ab7068b1482
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.994
doc_brief: "Symmetrized random permutations — 8 sections: Front matter; Introduction; Tracy-Widom distribution functions"
---
The ensemble $S^\symmO_{n,m}$ is the set of involutions with 
$n$ 2-cycles and $m$ 1-cycles.
In the previous section, we considered the limiting statistics when 
$n$ and $m$ are related by $m=[\sqrt{2n}\alpha]$ with $\alpha$ 
being finite ; either fixed or $\alpha\to 1$ with certain rate.
It is of interest to consider the whole set of involutions 
without constraints on the number of fixed points.
Similarly, the signed involutions without constraint 
on the number of fixed points and negated points is also of interest.
We define the ensembles of involutions and signed involutions 
\begin{align}
  \tilde{S}_n &=\{\pi\in S_n : \pi=\pi^{-1} \}, \\
  \tilde{S}_n^\symmu &= \{\pi\in S_{2n} : 
\pi=\pi^{-1},\ \pi=\iota\pi\iota \}, 
\end{align}
and denote by $\tilde{L}_n(\pi)$ and $\tilde{L}^\symmu_n(\pi)$ the length
of the longest increasing subsequence of $\pi\in\tilde{S}_n$ 
and that of $\pi\in\tilde{S}_n^\symmu$, 
respectively.

Noting $\tilde{S}_n=\bigcup_{2k+m=n} S^\symmO_{k,m}$, 
we have 
\begin{equation}\label{e-appl-1}
  \Prob\bigl(\tilde{L}_n\le l\bigr)= \frac{1}{|\tilde{S}_{k,m}|} 
\sum_{2k+m=n} \Prob\bigl(L^\symmO_{k,m}\le l\bigr) |S_{k,m}|. 

\end{equation}
It is not difficult to check that (see pp.66-67 of \cite{Kn}) 
as $n\to\infty$, the main contribution to the sum 
$|\tilde{S}_{k,m}|=\sum_{2k+m=n} |S_{k,m}|$ comes from 
$\sqrt{2k}-(2k)^{\epsilon+1/4}\le m\le\sqrt{2k}+(2k)^{\epsilon+1/4}$.
Comparing with the scaling $m=[\sqrt{2k}-2w(2k)^{1/3}]$ 
in Theorem \ref{thm3}, the main contribution to the sum 
\eqref{e-appl-1} comes from when $w=0$, or $\alpha=1$.
Thus we obtain GOE Tracy-Widom distribution function in the limit.











Similarly, we can obtain the convergence of moments.
The signed involution case is analogous.

\begin{thm}
For fixed $x\in\R$, 
\begin{align}
  \lim_{n\to\infty} 
\Prob\biggl( \frac{\tilde{L}_n-2\sqrt{n}}{n^{1/6}} \le x\biggr)
&= F_1(x), \\
\lim_{n\to\infty} 
\Prob\biggl( \frac{\tilde{L}_n^\symmu-2\sqrt{n}}{2^{2/3}n^{1/6}}\le x\biggr)
&= F_1(x)^2.
\end{align}
We also have convergence of all the moments.
\end{thm}

This result should be compared with the results on random permutation 
and random signed permutation where the limiting distribution 
was $F_2(x)$ and $F_2(x)^2$ under the same scaling of the above 
(see \cite{BDJ}, \cite{TW3}, \cite{Bo} and Theorem \ref{thm1} above).

\begin{rem}
  As in the permutation case, the length of the longest \emph{increasing} 
subsequence and the length of the longest \emph{decreasing} subsequence 
of random involutions have the same statistics. 
This can be seen by noting that there is a bijection 
(called Robinson-Schensted correspondence, see e.g. \cite{Kn}) 
between 
the set $\tilde{S}_n$ of involutions of $n$ letters 
and the set of standard Young tableaux 
of size $n$, and the rows and the columns of standard Young tableaux 
have the same statistics under the push forward of the uniform probability 
distribution on $\tilde{S}_n$ under this bijection.
\end{rem}



\subsection{$\beta$-Plancherel measure on the set of Young diagrams}

Let $Y_n$ be the set of Young diagrams, or equivalently partitions, 
of size $n$.
Given a partition $\lambda=(\lambda_1,\lambda_2,\cdots) \vdash n$, 
let $d_\lambda$ denote the number of standard Young tableaux of shape
$\lambda$. 
We introduce the $\beta$-Plancherel measure $M^\beta_n$ on $Y_n$ 
defined by 
\begin{equation}
   M^\beta_n(\lambda)=\frac{d_\lambda^\beta}
{\sum_{\mu\vdash n}d_\mu^\beta}, \qquad \lambda\in Y_n.
\end{equation}
When $\beta=2$, this is the Plancherel measure which arises in the
representation theory.
We are interest in the typical shape and the fluctuation of $\lambda$ 
where $\lambda$ is taken randomly from the probability space $Y_n$  
with $M^\beta_n$.

A motivation introducing the above measure is the result of 
Regev \cite{Re}. 
In \cite{Re}, it is proved that for fixed $\beta >0$ and fixed $l$,
as $n\to\infty$,
\begin{equation}\label{int-as-1}
   \sum_{\substack{\lambda\vdash n \\ \lambda_1\le l}}
\bigl(d_\lambda\bigr)^\beta
\sim \biggl[ \frac{l^{l^2/2}l^n}{(\sqrt{2\pi})^{(l-1)/2}n^{(l-1)(l+2)/4}}
\biggr]^\beta \frac{n^{(l-1)/2}}{l!}
\int_{\R^l} e^{-\frac12\beta l\sum_{j}x_j^2}
\prod_{j<k} |x_j-x_k|^\beta d^l x.
\end{equation}
The multiple integral on the right hand side is 
the Selberg integral which can be computed exactly for each $\beta$.
When $\beta=1,2,4$, this integral is 
the normalization constant of the probability 
density of eigenvalues in 
GOE, GUE and GSE, respectively (see e.g. \cite{Mehta}).
So the basic question is if the $\beta$ in the definition 
of the $\beta$-Plancherel measure corresponds to 
the $\beta$ in the random matrix theory.



The well-known Robinson-Schensted correspondence \cite{Sc} 
establishes a bijection between 
$S_n$ and the pairs of standard Young tableaux with the same
shape of size $n$, $\RS : \pi \mapsto (P(\pi),Q(\pi))$.
Especially, we obtain $\sum_{\mu\vdash n} d_\mu^2= |S_n|=n!$.
Moreover, under $\RS$, the length of the longest increasing subsequence 
of $\pi\in S_n$ is equal to the number of boxes in the first 
row of $P(\pi)$ (or equally of $Q(\pi)$).
Therefore under $\RS$, the Plancherel measure $M^2_n$ is 
simply the push forward of 
the uniform probability measure on $S_n$ to $Y_n$, 
and the number of boxes in the first row of a random Young diagram 
and the length of the longest increasing subsequence of a random 
permutation have the same statistics : GUE ($\beta=2$) 
fluctuation in the limit.

If $\RS(\pi)=(P,Q)$, then $\RS(\pi^{-1})=(Q,P)$ (see e.g. \cite{Kn}).
Therefore the set of involutions $\tilde{S}_n$ is bijective to 
the set of (single) standard Young tableaux, and 
the number of boxes in the first row of a random Young diagram 
taken under the probability $M^1_n$ has the same statistics 
with the length of the longest increasing subsequence of a random
involution : GOE ($\beta=1$) fluctuation in the limit.

In fact, it is shown in \cite{Ok, BOO, kurtj:recent} that, 
for the case of $\beta=2$, in the large $n$ limit, 
the number of boxes in the $k^{\text{th}}$ of a random Young diagram 
corresponds to the $k^{\text{th}}$ largest eigenvalue 
of a random GUE matrix.
Also the typical shape of $\lambda$ is obtained in \cite{LS} and 
\cite{VK1} which is related to Wigner's semicircle law \cite{Kerov}.
On the other hand, the second row of a random Young diagram 
for $\beta=1$ is 
discussed in \cite{BR2} implying that it corresponds to 
the second eigenvalue of a random GOE matrix.
It would be interesting to obtain similar results for general row 
for $\beta=1$ and also for general $\beta$.
