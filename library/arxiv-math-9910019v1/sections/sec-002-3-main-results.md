---
doc_id: arxiv-math-9910019v1
doc_title: "Symmetrized random permutations"
section_id: sec-002-3-main-results
section_title: "Main Results"
section_number: 3
pages: 7-9
source_pdf: 9910019v1.pdf
source_sha256: 07dd7ab7068b1482
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.994
doc_brief: "Symmetrized random permutations — 8 sections: Front matter; Introduction; Tracy-Widom distribution functions"
---
\label{sec-result}

As in the Introduction, let $N$ denote 
$n, 2n+m, 2n+m,2n,4n+2m_++2m_-$ for
each of $\tsymmU, \tsymmO, \tsymmS, \tsymmUU, \tsymmu$ case respectively.
We scale the random variables : for permutations and involutions, 
\begin{equation}
\chi^\symmU_n = \frac{L^\symmU_n-2\sqrt{N}}{N^{1/6}}, \qquad 
\chi^\symmO_{n,m} = \frac{L^{\symmO}_{n,m}-2\sqrt{N}}{N^{1/6}}, \qquad 
\chi^\symmS_{n,m} = \frac{L^{\symmS}_{n,m}-2\sqrt{N}}{N^{1/6}}, 
\end{equation}
and for signed permutations and signed involutions, 
\begin{equation}
\chi^\symmUU_{n} = \frac{L^\symmUU_n-2\sqrt{N}}{2^{2/3}N^{1/6}}, \qquad 
\chi^\symmu_{n,m_+,m_-} =
\frac{L^{\symmu}_{n,m_+,m_-}-2\sqrt{N}}{2^{2/3}N^{1/6}}.
\end{equation}
All the results in this section are taken from \cite{BR2} which utilizes 
the algebraic work of \cite{BR1}.

First, we state the results for random permutations and 
random signed permutations.
Random permutations show GUE fluctuation in the limit, 
while random signed permutations have $\text{GUE}^2$ fluctuation.
\begin{thm}\label{thm1}
  For fixed $x\in\R$, 
\begin{align}
  \lim_{n\to\infty} \Prob\bigl( \chi^\symmU_n \le x\bigr) 
&= F_2(x), \\
  \lim_{n\to\infty} \Prob\bigl( \chi^\symmUU_n \le x\bigr) 
&= F_2(x)^2.
\end{align}
\end{thm}

For the involution cases, we have the following limits.
\begin{thm}\label{thm2}
 For each fixed $\alpha$ and $\beta$, and for fixed $x\in\R$, 
we have : for $\tsymmO$, 
\begin{align}
  \lim_{n\to\infty} \Prob\bigl( \chi^\symmO_{n,[\sqrt{2n}\alpha]}
\le x \bigr) &= F_4(x), 
\qquad 0\le \alpha<1, \\
  \lim_{n\to\infty} \Prob\bigl( \chi^\symmO_{n,[\sqrt{2n}]}
\le x \bigr) &= F_1(x), \\
  \lim_{n\to\infty} \Prob\bigl( \chi^\symmO_{n,[\sqrt{2n}\alpha]}
\le x \bigr) &= 0, 
\qquad\qquad \alpha>1, 
\end{align}
for $\tsymmS$, 
\begin{align}
  \lim_{n\to\infty} \Prob\bigl( \chi^\symmS_{n,[\sqrt{2n}\beta]}
\le x \bigr) &= F_1(x), 
\qquad \beta\ge 0, 
\end{align}
and for $\tsymmu$, 
\begin{align}
  \lim_{n\to\infty} 
\Prob\bigl( \chi^\symmu_{n,[\sqrt{n}\alpha],[\sqrt{n}\beta]}
\le x \bigr) &= F_2(x), 
\qquad 0\le\alpha<1, \beta\ge 0, \\
  \lim_{n\to\infty} 
\Prob\bigl( \chi^\symmu_{n,[\sqrt{n}],[\sqrt{n}\beta]}
\le x \bigr) &= F_1(x)^2, 
\qquad \beta\ge 0, \\
  \lim_{n\to\infty} 
\Prob\bigl( \chi^\symmu_{n,[\sqrt{n}\alpha],[\sqrt{n}\beta]}
\le x \bigr) &= 0, 
\qquad\qquad \alpha>1, \beta\ge 0.
\end{align}
\end{thm}

This theorem shows that for $\tsymmO$ and $\tsymmu$, 
the limiting distributions differ depending on the value of $\alpha$.
As indicated earlier in the Introduction, as $\alpha\to 1$ at a certain rate, 
we obtain smooth transitions. 
From Corollary \ref{cor16},
the following results are consistent with Theorem \ref{thm2}.
\begin{thm}\label{thm3}
For fixed $w\in\R$, $\beta\ge 0$ and $x\in\R$, 
\begin{align}
  \lim_{n\to\infty} \Prob\bigl( \chi^\symmO_{n,m}
\le x \bigr) &= F^\symmO(x;w),
\qquad m=[\sqrt{2n} - 2w(2n)^{1/3}],\\
     \lim_{n\to\infty}
\Prob\bigl( \chi^\symmu_{n,m_+,m_-}
\le x \bigr) &= F^\symmu(x;w),
\quad\qquad m_+=[\sqrt{n} - 2wn^{1/3}],\ m_-=[\sqrt{n}\beta].
\end{align}
\end{thm} 

When $\alpha>1$, Theorem \ref{thm2} shows that we have used 
inappropriate scaling. 
In a proper scaling, we obtain normal distribution $N(0,1)$.
\begin{thm}\label{thm4}
  For fixed $\alpha>1$ and $\beta\ge 0$, as $n\to\infty$, 
\begin{align}
  \frac{L^\symmO_{n,[\sqrt{2n}\alpha]}-(\alpha+1/\alpha)\sqrt{N}}
{\sqrt{(1/\alpha-1/\alpha^3)}N^{1/4}} 
&\to N(0,1) \qquad \text{in distribution},\\
  \frac{L^\symmu_{n,[\sqrt{n}\alpha],[\sqrt{n}\beta]}
-(\alpha+1/\alpha)\sqrt{N}}
{\sqrt{(1/\alpha-1/\alpha^{3})}N^{1/4}} 
&\to N(0,1) \qquad \text{in distribution}.
\end{align}
\end{thm}

All the above results are on the convergence in distribution.
We also have convergence of moments for all the cases.

\begin{thm}\label{thm5}
  For each case of the above theorems, all the moments of 
the random variable converge to the moments of the corresponding 
limiting distribution.
\end{thm}

From this result, we can obtain the asymptotics of variances.
Especially for $\tsymmU$, the variance is 
\begin{equation}
  \lim_{N\to\infty} \frac{\Var(l^\symmU_n)}{N^{1/3}}
=\int_{-\infty}^\infty x^2 dF_2(x) -
\biggl( \int_{-\infty}^\infty xdF_2(x)\biggr)^2.
\end{equation}
Evaluating the integrals, we obtain the value $0.8132\cdots$ 
(see \cite{TW1}).

The outline of the proofs is as follows.
First we consider the Poisson generating function. 
It is to let the number of points be Poisson.
For example, we define 
\begin{equation}
   P^\symmU_l(t)=e^{-t^2} \sum_{n=0}^{\infty} \frac{t^{2n}}{n!}
\Prob\bigl( L^\symmU_n\le l \bigr).
\end{equation}
The de-Poissonization lemma \cite{Jo2} tells us that 
in the limit $n\to\infty$, $\Prob\bigl( L^\symmU_n\le l \bigr) 
\sim P^\symmU_l(n^2)$, hence it is enough to obtain the asymptotics of 
the Poisson generating function.
The crucial point is that there is a determinantal formula for 
each Poisson generating function.
For the cases $\tsymmU$ and $\tsymmUU$, the determinant is 
of Toeplitz type \cite{Gessel, Rains}, while for the rest, 
it is of Hankel type \cite{BR1}.
In fact, as in \cite{Gessel}, there are general identities between 
sum of Schur functions and determinantal formulae (see \cite{BR1} 
for details), which can be used to consider other type of 
Young tableaux problems (see Subsection \ref{subsec-Jo} below).
Now general theory connects 
Toeplitz/Hankel determinants and orthogonal polynomials.
It turns out that to analyze all the above cases, only one set of 
orthogonal polynomials are needed, namely 
the orthogonal polynomials on the unit circle with respect to the 
weight $e^{2t\cos\theta} d\theta/(2\pi)$.

Now following Fokas, Its and Kitaev \cite{FIK}, there is a Riemann-Hilbert
representation for orthogonal polynomials.
Let $\Sigma$ be the unit circle in the complex plane oriented
counterclockwise. 
Let $Y(z)$ be a $2\times 2$ matrix-valued function satisfying 
\begin{equation}
\begin{cases}
   Y(z) \quad\text{is analytic in $\C\setminus\Sigma$},\\
   Y_+(z)=Y_-(z) \begin{pmatrix} 1&\frac{1}{z^k}e^{t(z+z^{-1})}\\
0&1 \end{pmatrix}, \quad z\in\Sigma, \\
   Y(z) \bigl(\begin{smallmatrix} z^{-k}&0\\0&z^k
\end{smallmatrix} \bigr) = I+O(z^{-1})  
\qquad \text{as $z\to\infty$}, 
\end{cases}
\end{equation}
where $Y_+(z)$ (resp. $Y_-(z)$) denotes the limit of $Y(z')$ 
as $z'\to z$ satisfying $|z'|<1$ (resp. $|z'|>1$).
Then one finds that for example, the 11 entry of $Y(z)$ is the 
$k^{\text{th}}$ monic orthogonal polynomial with respect to the weight 
$e^{2t\cos\theta} d\theta/(2\pi)$.
Once we have a Riemann-Hilbert representation, we can employ the
steepest-descent method (Deift-Zhou method) developed by Deift and Zhou
\cite{DZ1} to find asymptotics as parameters become large (or small).
For our case, the parameters are $t$ and $k$, and taking proper scaling,
we obtain precise asymptotics which eventually yield the convergence in 
distribution and convergence of moments.
We also mention that in our analysis, equilibrium measures play a
crucial role as in the papers \cite{DKMVZ, DKMVZ2, DKMVZ3}.
