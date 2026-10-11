---
doc_id: arxiv-math-9910019v1
doc_title: "arXiv:math/9910019v1 [math.CO] 5 Oct 1999"
section_id: sec-005-43-random-turn-vicious-walker-model
section_title: "Random turn vicious walker model"
section_number: 4.3
pages: 11-17
source_pdf: 9910019v1.pdf
source_sha256: 07dd7ab7068b1482
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.567
---
Random permutations and random involutions arise also in certain random 
walk process in a one dimensional integer lattice.
We call a particle left-movable (resp. right-movable) 
if its left (resp. right) site is vacant.
Initially, $p$ particles are located at the points $1,2,3,\cdots,p$.
At each time step $t$ ($t=1,2,\cdots$), 
one particle 
among the left-movable particles 
is selected at random,  
and is moved to its left site
(so at $t=1$, the leftmost particle is moved.)
Suppose this process is repeated for $n$ time steps. 
It is found that \cite{forrester99}
there is a bijection between all the possible configurations 
and the set of Young tableaux with at most $p$ rows of size $n$ : 
simply, in the $k^{\text{th}}$ row, write the times 
when the particle is originally at the point $k$ (see Figure \ref{fig-walk}).
\begin{figure}[ht]
 \centerline{\epsfig{file=walk.eps, width=13cm}}
 \caption{random turn vicious walkers and Young tableaux}
\label{fig-walk}
\end{figure}
In this correspondence the number of moves made by the $k^{\text{th}}$ 
particle (counted from the left) is the number of boxes 
in the $k^{\text{th}}$ row of the corresponding Young tableau.
If we take the limit $p\to\infty$, we remove the constraint 
on the number of rows. 
In other words, we start with countably many particles located at 
$1,2,3,\cdots$ and at each 
time step, we move a randomly selected left-movable particle 
to its left site.
Then the statistics of the number of moves made by the leftmost particle 
in $n$ time steps 
is identical to that of the number of boxes 
in the first row of a random Young 
diagram under the probability $M^1_n$ (or the length of the longest 
increasing subsequence of a random involution).
Hence in the large $n$ limit, we obtain GOE fluctuation.

Now suppose after $n$ steps of left moves, 
by taking $n$ steps of right moves, 
we want the particles brought back to their original positions.
The first $n$ steps gives a Young tableaux and the next $n$ step gives another 
Young tableaux.
So we are in the situation of pairs of Young tableaux, i.e. $\beta=2$ case.
Especially if the number of particles are infinite, 
the statistics of the moves made by the leftmost 
particle is identical to the length of the longest increasing 
subsequence of a random permutation : GUE fluctuation
\cite{forrester99}.







\subsection{Symmetrized versions of Johansson's model}\label{subsec-Jo}

In \cite{kurtj:shape}, Johansson introduced a certain model 
which has several probabilistic interpretations, 
as a randomly growing Young diagram, a totally asymmetric one dimensional 
exclusion process, a certain zero-temperature directed polymer in a random 
environment or as a kind of first-passage site percolation model.
Here we consider the symmetrized versions.
The limiting distributions are parallel to the results of Section 
\ref{sec-result} depending on the symmetry type.

Each model is defined on $\M$, a subset of $\Z^2$, and at each site 
$(i,j)\in\M$, we define a random variable $w(i,j)$ of geometric
distribution. 
We are interested in ``the length of the longest up/right path''.
Let $g(q)$ denote the geometric distribution with parameter $q$.
Let $0<q<1$, and let $\alpha,\beta\ge 0$ such that 
$\alpha \sqrt{q}, \beta \sqrt{q}<1$.
Otherwise stated, the random variables $w(i,j)$ are independent each other.
We denote by $(j,k)\nearrow (j',k')$ the set of up/right paths $\pi$ from 
$(j,k)$ to $(j',k')$.

\begin{enumerate}
\item Let $\M=\Z_+^2$. 
Let 
\begin{equation}
   w(i,j)\sim g(q).
\end{equation}
Define 
\begin{equation}
  G^\symmU(N)=\max \{\sum_{(i,j)\in\pi} w(i,j) : \pi\in (1,1)\nearrow(N,N) \}.
\end{equation}
\item Let $\M=\Z^2$. 
Let $w(i,j)=0$ if $i=0$ or $j=0$, and for $i,j\neq 0$, let 
\begin{equation}
   w(i,j)=w(-i,-j)\sim g(q).
\end{equation}
Define 
\begin{equation}
   G^\symmUU(N)=\max \{ \sum_{(i,j)\in\pi} w(i,j) : 
\pi\in (-N,-N)\nearrow(N,N) \}.
\end{equation}
\item Let $\M=\Z_+^2$. 
Let 
\begin{eqnarray}
   w(i,j)=w(j,i) &\sim& g(q),\quad   i\neq j, \\
   w(i,i)&\sim& g(\alpha\sqrt{q}).
\end{eqnarray}
Define 
\begin{equation}
  G^\symmO(N)=\max \{ \sum_{(i,j)\in\pi} w(i,j) : \pi\in (1,1)\nearrow(N,N) \}.
\end{equation}
\item Let $\M=\Z_+\times \Z_-$.
Let 
\begin{eqnarray}
  w(i,-j)=w(j,-i) &\sim& g(q), \quad i\neq -j, \\
  w(i,-i) &\sim& g(\beta\sqrt{q}).
\end{eqnarray}
Define 
\begin{equation}
   G^\symmS(N)=\max \{ \sum_{(i,j)\in\pi} w(i,j) : 
\pi\in (1,-N)\nearrow (N,-1) \}.
\end{equation}
\item Let $\M=\Z^2$.
Let $w(i,j)=0$ if $i=0$ or $j=0$. Otherwise 
\begin{eqnarray}
   w(i,j)=w(-i,-j) &\sim& g(q),\quad |i|\neq|j|, \\
   w(i,i)=w(-i,-i) &\sim& g(\alpha\sqrt{q}), \\
   w(i,-i)=w(-i,i) &\sim& g(\beta\sqrt{q}).
\end{eqnarray}
Define 
\begin{equation}
   G^\symmu(N)=\max \{ \sum_{(i,j)\in\pi} w(i,j) : 
\pi\in(-N,-N)\nearrow (N,N) \}.
\end{equation}
\end{enumerate}

We are interested in the limiting distributions of $G^\symmg(N)$.
\begin{thm}\label{thm-4.2}
Set 
\begin{equation}
  \eta(q)=\frac{2\sqrt{q}}{1-\sqrt{q}}, 
\qquad \rho(q)=\frac{q^{1/6}(1+\sqrt{q})^{1/3}}{1-\sqrt{q}}.
\end{equation}
We have 
\begin{enumerate}
\item 
\begin{equation}\label{e-appl-2}
  \lim_{N\to\infty}
\Prob\biggl(\frac{G^\symmU(N;q)-\eta(q)N}
{\rho(q)N^{1/3}}\le x\biggr)
= F_2(x).
\end{equation}
\item 
\begin{equation}
  \lim_{N\to\infty}
\Prob\biggl(\frac{G^\symmUU(N;q)-\eta(q)(2N)}
{2^{2/3}\rho(q)(2N)^{1/3}}\le x\biggr)
= F_2(x)^2.
\end{equation}
\item 
\begin{eqnarray}
  \lim_{N\to\infty}
\Prob\biggl(\frac{G^\symmO(N;q,\alpha)-\eta(q)N}
{\rho(q)N^{1/3}}\le x\biggr)
&=& F_4(x), \qquad 0\le\alpha<1, \\
\label{e-appl-3}
  \lim_{N\to\infty}
\Prob\biggl(\frac{G^\symmO(N;q,\alpha)-\eta(q)N}
{\rho(q)N^{1/3}}\le x\biggr)
&=& F^\symmO(x;w), \quad \alpha=1-\frac{2w}{\rho(q)N^{1/3}}, \\
  \lim_{N\to\infty}
\Prob\biggl(\frac{G^\symmO(N;q,\alpha)-\eta(q)N}
{\rho(q)N^{1/3}}\le x\biggr)
&=& 0, \qquad\qquad \alpha>1.
\end{eqnarray}
\item
\begin{equation}
  \lim_{N\to\infty}
\Prob\biggl(\frac{G^\symmS(N;q,\beta)-\eta(q)N}
{\rho(q)N^{1/3}}\le x\biggr)
= F_1(x), \qquad 0\le\beta.
\end{equation}
\item 
\begin{eqnarray}
  \lim_{N\to\infty}
\Prob\biggl(\frac{G^\symmu(N;q,\alpha,\beta)-\eta(q)(2N)}
{2^{2/3}\rho(q)(2N)^{1/3}}\le x\biggr)
&=& F_2(x), \qquad 0\le\alpha<1, \beta\ge 0, \\
  \lim_{N\to\infty}
\Prob\biggl(\frac{G^\symmu(N;q,\alpha,\beta)-\eta(q)(2N)}
{2^{2/3}\rho(q)(2N)^{1/3}}\le x\biggr)
&=& F^\symmu(x;w), \quad \alpha=1-\frac{2w}{\rho(q)(2N)^{1/3}}, \beta\ge 0 \\
  \lim_{N\to\infty}
\Prob\biggl(\frac{G^\symmu(N;q,\alpha,\beta)-\eta(q)(2N)}
{2^{2/3}\rho(q)(2N)^{1/3}}\le x\biggr)
&=& 0, \qquad\qquad \alpha>1, \beta\ge 0.
\end{eqnarray}
\end{enumerate}
\end{thm}

\begin{rem}
  The results \eqref{e-appl-2} and \eqref{e-appl-3} with $w=0$ 
are obtained in \cite{kurtj:recent}. 
For $\tsymmU$, 
the longest up/right path in $(1,1)\nearrow (M,N)$, $M\neq N$, 
is also considered.
\end{rem}

The proof of the above theorem is analogous to that of 
the result in Section \ref{sec-result}.
There again is a Toeplitz/Hankel determinantal formula for each 
case. 
In fact, the only change with the symmetrized permutation case is 
that we have $(1+q+2\sqrt{q}\cos\theta)^N d\theta/(2\pi)$ instead of 
$e^{2t\cos\theta} d\theta/(2\pi)$ for the weight. 
In analyzing the asymptotics of orthogonal polynomials, we need
different scaling, but once we scale, the analysis is parallel.
One important common property of the above two weights is 
that both of the supports of their equilibrium measures change 
from the full circle to a part of the circle with one gap 
depending on $2t/k<1$ and $2t/k>1$, and $N/k<\eta(q)^{-1}$ 
and $N/k>\eta(q)^{-1}$. 
And also in the one gap case, 
the equilibrium measures decay like a square root at the ends 
of the supports.



\bibliographystyle{plain}
