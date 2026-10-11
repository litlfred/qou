---
doc_id: arxiv-math-9810105v2
doc_title: "arXiv:math/9810105v2 [math.CO] 26 Mar 1999"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-8
source_pdf: 9810105v2.pdf
source_sha256: 0a432946234949c1
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.944
---
\label{s-intro}

Let $S_N$ be the group of permutations of $1,2,\dots,N$.
If $\pi\in S_N$, we say that $\pi(i_1),\cdots,\pi(i_k)$
is an increasing subsequence in $\pi$ if $i_1<i_2< \cdots <i_k$ and
$\pi(i_1) < \pi(i_2) < \cdots < \pi(i_k)$.
Let $l_N(\pi)$ be the length of the longest increasing subsequence.
For example, if $N=5$ and $\pi$ is the permutation 
$5\ \ 1\ \ 3\ \  2\ \ 4$ (in one-line notation 
: thus $\pi(1)=5$, $\pi(2)=1$, $\dots$), then the longest
increasing subsequences are $1\ \ 2\ \ 4$ and $1\ \ 3\ \ 4$, and $l_N(\pi)=3$.
Equip $S_N$ with uniform distribution, 
\begin{equation*}
   q_{n,N}=Prob(l_N\le n)=\frac{f_{N,n}}{N!}, 
\end{equation*}
where $f_{N,n}=\# \text{(permutations $\pi$ in $S_N$ with $l_N\le n$)}$.
The goal of this paper is to determine the asymptotics of 
$q_{n,N}$ as $N\to\infty$.
This problem was raised by Ulam in the early 60's \cite{Ul}, 
and on the basis of Monte Carlo simulations, he 
conjectured that the limit
\begin{equation}
   c\equiv \lim_{N\to\infty} \frac1{\sqrt{N}} \E_N(l_N)
\end{equation}
exists.   
(Here $\E_N(\cdot)$ denotes the expectation value with respect
to the distribution function $q_{n,N}$.)
The problem of proving the existence of this limit and the computation 
of $c$ has became known as ``Ulam's problem''.
An argument of Erd\"os and Szekeres \cite{ES} shows that 
$\E_N(l_N)\geq \frac12\sqrt{N-1}$, so that if the limit 
exists, then $c\geq\frac12$.
Subsequent numerical work by Baer and Brock \cite{BB} 
in late 60's suggested that value of $c$ is 2.
The existence of the limit was rigorously 
established by Hammersley \cite{Ha} in 1972.
In \cite{LS}, Logan and Shepp proved that $c\geq 2$ and simultaneously 
Vershik and Kerov \cite{VK} (see also \cite{VK2}) showed that $c=2$, 
thus settling Ulam's problem.
Alternative proofs of Ulam's problem are due to Aldous and Diaconis 
\cite{AD}, Sepp\"al\"ainen \cite{Se} and Johansson \cite{Johan}.
Over the years, various conjectures have been made concerning 
the variance $Var(l_N)$ of $l_N$, and Monte Carlo simulations of 
Odlyzko and Rains beginning in 1993, indicated that 
\begin{equation}\label{e-c0}
   \lim_{N\to\infty} \frac1{N^{1/3}} Var(l_N) = c_0
\end{equation}
for some numerical constant $c_0 \sim 0.819$. 
Also Odlyzko and Rains computed $\E(l_N)$ to higher order 
and found 
\begin{equation}\label{e-c1}
   \lim_{N\to\infty} \frac{\E(l_N)-2\sqrt{N}}{N^{1/6}} =c_1
\end{equation}
where $c_1 \sim -1.758$.
Further historical information on Ulam's problem, together with some 
discussions of the methods used by various authors, can be found 
in \cite{AD} and \cite{OR}

\bigskip
Before stating our results, we need to define the Tracy-Widom 
distribution \cite{TW} (see below).
Let $u(x)$ be the solution of the Painlev\'e II (PII) equation,
\begin{equation}\label{e-int1}
  u_{xx}=2u^3+xu, \quad\text{and}\quad 
u\sim -Ai(x)\quad\text{as}\quad x\to\infty,
\end{equation}
where $Ai$ is the Airy function.
The (global) existence and uniqueness of this solution was first 
established in \cite{HM} : 
the asymptotics as $x\to\pm\infty$ are,  
\begin{equation}\label{e-asyPII}
  \begin{split}
   &u(x)=-Ai(x)+O\biggl(\frac{e^{-(4/3)x^{3/2}}}{x^{1/4}}\biggr) 
\quad \text{as}\quad x\to\infty,\\
   &u(x)= -\sqrt{\frac{-x}2} \biggl(1+O\bigl(\frac1{x^2}\bigr)\biggr) 
\qquad \text{as}
\quad x\to -\infty,
  \end{split}
\end{equation}
(see, for example, \cite{HM}, \cite{IN}, \cite{DZ}).
Recall \cite{AS} that $Ai(x)\sim 
\frac{e^{-(2/3)x^{3/2}}}{2\sqrt{\pi}x^{1/4}}$ as $x\to\infty$.
Define the Tracy-Widom distribution 
\begin{equation}\label{e-F}
  F(t) = \exp \biggl(-\int_t^\infty (x-t)u^2(x) dx\biggr).
\end{equation}
From~\eqref{e-asyPII} and~\eqref{e-F}, $F'(t)>0$, 
$F(t)\to 1$ as $t\to +\infty$ and $F(t)\to 0$ 
as $t\to -\infty$, so that $F$ is indeed a distribution function.
Our first result concerns the convergence of $l_N$ in distribution 
after appropriate centering and scaling. 
\begin{thm}\label{thm1}
  Let $S_N$ be the group of all permutations of $N$ numbers
with uniform distribution and let $l_N(\pi)$ be the length of
the longest increasing subsequence of $\pi\in S_N$.
   Let $\chi$ be a random variable whose distribution function is $F$.
   Then, as $N\to\infty$, 
\begin{equation*}
   \chi_N\equiv\frac{l_N-2\sqrt{N}}{N^{1/6}}\to\chi 
\qquad\text{in distribution,}
\end{equation*}
i.e.
\begin{equation*}
   \lim_{N\to\infty} Prob\biggl(\chi_N\equiv
\frac{l_N-2\sqrt{N}}{N^{1/6}}\le t\biggr)
=F(t) \quad\text{for all $t\in\R$.}
\end{equation*}
\end{thm}
In order to show that the moments of $\chi_N$ converge to the
corresponding moments of $\chi$ we need estimates for the distribution
function $F_N(t)$ of $\chi_N$ for large $|t|$. From the large
deviation formulas for $l_N$ (see below), we expect that $F_N(t)$
(resp., $1-F_N(t)$) 
should go to zero rapidly as $t\to-\infty$ (resp., $t\to+\infty$). 
In fact, we will prove that, for
$M>0$ sufficiently large, there are positive constants $c$ and $C(M)$
such that
\begin{equation}\label{e-J1.6a'}
F_N(t)\le C(M)e^{ct^3}     
\end{equation}
if $-2N^{1/3}\le t\le -M$, and
\begin{equation}\label{e-J1.6b'}
1-F_N(t)\le C(M)e^{-ct^{3/5}}   
\end{equation}
if $M\le t\le N^{5/6}-2N^{1/3}$.
Together with Theorem~\ref{thm1}  these estimates yield 
\begin{thm}\label{thm2}
   For any $m=1,2,3,\cdots$, we have
\begin{equation*}
   \lim_{N\to\infty} \E_N(\chi_N^m)= \E(\chi^m),
\end{equation*}
where $\E(\cdot)$ denotes expectation with respect to the distribution
function $F$. In particular,
 \begin{equation}\label{e-Jcor1}
      \lim_{N\to\infty} \frac{Var(l_N)}{N^{1/3}} =
\int_{-\infty}^{\infty} t^2dF(t) -
\biggl( \int_{-\infty}^{\infty} tdF(t) \biggr)^2.
  \end{equation}
and
\begin{equation}\label{e-Jcor2}
  \lim_{N\to\infty} \frac{\E_N(l_N)-2\sqrt{N}}{N^{1/6}} =
\int_{-\infty}^{\infty} tdF(t).
\end{equation}
\end{thm}
If one solves the Painlev\'e II equation~\eqref{e-int1} numerically 
(see, \cite{TW}), and then 
computes the integrals on the RHS of the formulae of ~\eqref{e-Jcor1} 
and~\eqref{e-Jcor2}, one obtains the values 0.8132 and -1.7711 
which agree with 
$c_0$ and $c_1$ in~\eqref{e-c0} and~\eqref{e-c1} respectively, 
up to two decimal places.


\bigskip
The distribution function $F(t)$ in Theorems \ref{thm1} and \ref{thm2} 
first arose in the work of Tracy and Widom on 
the Gaussian Unitary Ensemble (GUE) of random matrix theory.
In this theory (see, e.g., \cite{Me}), one considers $N\times N$ 
hermitian matrix $M=(M_{ij})$ with probability density
\begin{equation*}
   Z_N^{-1}e^{-tr(M^2)}dM
=Z_N^{-1}e^{-tr(M^2)} \biggl(\prod_{i=1}^{N} dM_{ii}\biggr) 
\prod_{i=1}^{N} d(ReM_{ij}) d(ImM_{ij}),
\end{equation*}
where $Z_N$ is the normalization constant.
In \cite{TW}, Tracy and Widom showed that 
as the size of the hermitian matrices increases, 
the distribution of the (properly centered and scaled) largest 
eigenvalue of a random GUE matrix 
converges precisely to $F(t)$ !
In other words, properly centered and scaled, the length of the longest 
increasing subsequence for a permutation $\pi\in S_N$, behaves statistically 
for large $N$ like the largest eigenvalue of a random GUE matrix 
(see the Appendix for an intuitive argument).
In \cite{TW}, the authors also computed the distribution functions of 
the second, third, $\cdots$ largest eigenvalues of such random matrices, 
and the question arises whether such distribution functions describe 
the statistics of quantities identifiable in the random permutation 
context.

Recall the Robinson-Schensted correspondence 
(see, e.g., \cite{Sa}, and also Section 5.1.4 in \cite{Kn}) 
which establishes a bijection $\pi\mapsto (P(\pi),Q(\pi))$ from $S_N$ 
to pairs of Young tableaux with shape$(P(\pi))$  $=$shape$(Q(\pi))$. 
Under this correspondence, the number of boxes in the first row 
of $P(\pi)$ (equivalently $Q(\pi)$) is precisely $l_N(\pi)$, 
(see, \cite{Sa}, \cite{Kn}).
In other words, the results on $l_N$ can be rephrased as results on  
the statistics of the number of boxes in the first row of Young tableaux.
Monte Carlo simulations of Odlyzko and Rains \cite{OR} indicate that $\wt{l}_N$, 
the number of boxes in the second row of $P(\pi)$ 
(equivalently $Q(\pi)$) behaves 
statistically for large $N$, like the second largest eigenvalue of a 
random GUE matrix.
More precisely, their simulations indicate that 
\begin{equation*}
   \lim_{N\to\infty} \frac{\E_N(\wt{l}_N)-2\sqrt{N}}{N^{1/6}}
=-3.618, 
\end{equation*}
and 
\begin{equation*}
   \lim_{N\to\infty} \frac{Var(\wt{l}_N)}{N^{1/3}} = 0.545.
\end{equation*}
These values agree, once again, to two decimal places with 
the mean and variance of the suitably centered 
and scaled second largest eigenvalue of a GUE matrix, 
as computed in \cite{TW}.
Presumably, the number of boxes in the third row of $P(\pi)$ should 
behave statistically like the third largest eigenvalue of a GUE matrix 
as $N\to\infty$, etc. 
In recent work \cite{BDJ}, the authors have shown that this 
conjecture is indeed true for the second row.
Also, beautiful results of Okounkov \cite{Ok}, 
using arguments from combinatorial topology, have now provided an elegant 
basis for understanding the relationship between the statistics 
of Young tableaux and the eigenvalues of random matrices.
Over the last year, many other intriguing results have been obtained 
on a variety of problems arising in mathematics and mathematical 
physics, which are closely related to, or motivated by, 
the longest increasing subsequence problem. 
We refer the reader to 
\cite{TW2}, \cite{Bo}, \cite{Jo2, Jo3} and \cite{BR}.



\bigskip
As in \cite{Johan}, we consider the Poissonization $\phi_n(\lambda)$ 
of $q_{n,N}$, 
\begin{equation}\label{e-int4}
  \phi_n(\lambda) \equiv \sum_{N=0}^{\infty} 
\frac{e^{-\lambda}\lambda^N}{N!} q_{n,N}.
\end{equation}
The function $\phi_n(\lambda)$ is a distribution function (in $n$) of
a random variable $L(\lambda)$ coming from a superadditive process
introduced by Hammersley in \cite{Ha}, and used by him to show that the
limit (1.1) exists. The random variable $L(\lambda)$ is defined as
follows.
Consider a homogeneous rate one Poisson process in
the plane and let $L(\lambda)$ denote the maximum number of points in
an up-right (increasing) path through the points starting at $(0,0)$
and ending at $(\sqrt{\lambda},\sqrt{\lambda})$. For more details see
\cite{AD} and \cite{Se2}, and for a generalization to the non-homogeneous case
see \cite{DeZe}. Theorem~\ref{thm1}  and~\ref{thm2} 
hold for the random variable
$L(\lambda)$ as $\lambda\to\infty$.
Referring to the ``de-Poissonization'' 
Lemmas~\ref{lem-dep2} and ~\ref{lem-dep3} 
below, we see that it is easy to recover the asymptotics of $q_{n,N}$ 
as $N\to\infty$ from the knowledge of $\phi_n(\lambda)$ for 
$\lambda\sim N$. 
In other words, in order to compute the asymptotics of $l_N$, 
we must investigate 
the double scaling limit of $\phi_n(\lambda)$ when 
$\lambda\to\infty$ and $1\le n\le N\sim\lambda$, and this is 
the technical thrust of the paper.

To this end we use the following representation for $\phi_n(\lambda)$, 
\begin{equation}\label{e-phi}
    \phi_n(\lambda) 
    = e^{-\lambda} D_{n-1}(\exp(2\sqrt{\lambda}\cos{\theta})), 
\end{equation}
where $D_{n-1}$ denotes the $n\times n$ Toeplitz determinant
with weight function $f(e^{i\theta})=\exp(2\sqrt{\lambda}\cos{\theta})$
on the unit circle, (see, e.g.,\cite{Sz}).
The above formula follows from work of Gessel in \cite{Ge} using well known 
results about Toeplitz determinants.
As noted in \cite{Johan}, the formula can also be proved using 
the following representation for $q_{n,N}$, $1\le n\le N$, 
discovered by \cite{OPWW}, 
\begin{equation}\label{e-rains}
   q_{n,N}=\frac{2^{2N}N!}{(2N)!}
\int_{[-\pi,\pi]^n} \bigl( \sum_{j=1}^{n} \cos\theta_j \bigr)^{2N}
\prod_{1\le j<k\le n} |e^{i\theta_j}-e^{i\theta_k}|^2
\frac{d^n\theta}{(2\pi)^nn!}.
\end{equation}
In addition, an earlier result of Diaconis and Shahshahani (\cite{DS}) shows 
that the above formula~\eqref{e-rains} is true also in the case 
$n>N$ when $q_{n,N}\equiv 1$. 
Inserting~\eqref{e-rains} into ~\eqref{e-int4}, we obtain 
\begin{equation}\label{e-DiS}
    \phi_n(\lambda) = e^{-\lambda} \frac{1}{(2\pi)^nn!} 
\int_{[-\pi,\pi]^n}\exp(2\sqrt{\lambda}\sum_{j=1}^{n} \cos{\theta_j}) 
\prod_{1\leq j<k \leq n} |e^{i\theta_j}-e^{i\theta_k}|^2 d^n\!\theta, 
\end{equation}
which is precisely~\eqref{e-phi} by standard methods in the theory of 
Toeplitz determinants (see, \cite{Sz}).
An additional proof of~\eqref{e-phi} can be found in \cite{GWW}, and 
also an alternative derivation of formula~\eqref{e-rains} is given 
in \cite{Rains}.
For the convenience of the reader we provide (yet another) 
proof of~\eqref{e-phi} 
in the Appendix to this paper.

Using the integral representation~\eqref{e-phi}, 
Johansson (\cite{Johan}) proved 
the following bound for $\phi(\lambda)$ :     
for any given $\epsilon >0$, there exist $C$ and $\delta>0$ such that 
\begin{equation}\label{e-J1.11}
  \begin{split}
    &0\le\phi_n(\lambda)\le Ce^{-\delta\lambda}
\quad\text{if}\quad (1+\epsilon)n< 2\sqrt{\lambda},\\
    &0\le 1- \phi_n(\lambda) \le \frac{C}{n}
\quad\text{if}\quad (1-\epsilon)n> 2\sqrt{\lambda}.
  \end{split}
\end{equation}
This information and the de-Poissonization Lemma~\ref{lem-dep2}  
are enough to give a new proof (\cite{Johan}) that
\begin{equation}\label{e-J1.11'}
  \lim_{N\to\infty} L_N/2\sqrt{N} =1.
\end{equation}
The first estimate in~\eqref{e-J1.11} is a consequence of the following lower
tail large deviation formula for $\phi_n(\lambda)$,
\begin{equation}\label{e-J1.12'}
\lim_{\lambda\to\infty}\frac
1{\lambda}\phi_{[x\sqrt{\lambda}]}(\lambda)=              
-1+2x-\frac 34x^2-\frac{x^2}2\log\frac 2x\equiv -U(x),
\end{equation}
if $x<2$.
For the upper tail Sepp\"al\"ainen in \cite{Se2} used
the interacting particle system implicitly
introduced by Hammersley in \cite{Ha} to show that
\begin{equation}\label{e-J1.13}
  \lim_{\lambda\to\infty} \frac1{\sqrt{\lambda}}
\log\bigl(1-\phi_{[x\sqrt{\lambda}]}(\lambda)\bigr) = -2x\cosh^{-1}(x/2)
+2\sqrt{x^2-4}\equiv -I(x)
\end{equation}
if $x>2$. We note that Hammersley's interacting particle system was also used
earlier by Aldous and Diaconis in \cite{AD}.
The super-additivity of the process described above implies that we
actually have, see \cite{Se2} and also \cite{Ki},
\begin{equation}\label{e-J1.13'}
1-\phi_{[xM]}(M^2)\le e^{-MI(x)},    
\end{equation}
if $M$ is a positive integer and $x\ge 2$. This estimate can be used
to show~\eqref{e-J1.6b'}, but in this paper we will give an independent proof
of~\eqref{e-J1.6b'}.
The large deviation formula~\eqref{e-J1.13} implies, via a de-Poissonization
argument, that for $x>2$,
\begin{equation}\label{e-J1.14}
  \lim_{N\to\infty} \frac1{\sqrt{N}} \log Prob\bigl( l_N>x\sqrt{N}\bigr)
=-I(x).
\end{equation}
For the lower tail the large deviation formula for $l_N$ is not the
same as for $L(\lambda)$, the Poissonized case. Deuschel and Zeitouni
in \cite{DeZe2} use combinatorial and variational
ideas from Logan and Shepp \cite{LS} to prove that
\begin{equation}\label{e-z50}
  \lim_{N\to\infty} \frac1{N} \log Prob\bigl( l_N<x\sqrt{N}\bigr)
=-H(x),
\end{equation}
if $0<x<2$, where
\begin{equation}\label{e-J15}
  H(x)=-\frac12 +\frac{x^2}8+\log\frac{x}2
-\bigl(1+\frac{x^2}4\bigr)\log\bigl(\frac{2x^2}{4+x^2}\bigr).
\end{equation}
For the lower tail we have no analogue of~\eqref{e-J1.13'}. The rate functions
$U$ and $H$ are related via a Legendre transform, see \cite{Se2}.
The above results show clearly that the distribution function for
$l_N$ is sharply concentrated in the region
$\{ (2-\epsilon)\sqrt{N} < l_N < (2+\epsilon)\sqrt{N} \}$ for
any $\epsilon >0$, and they can be used to see heuristically that the
variance for $l_N$ should be of order $N^{1/3}$, see \cite{Ki}.

\bigskip
As is well known (see, \cite{Sz}) the Toeplitz determinant $D_{n-1}$ 
in~\eqref{e-phi} 
is intimately connected with the polynomials  
$p_n(z;\lambda)=\kappa_n(\lambda)z^n+\cdots$, 
which are orthonormal with respect to 
the weight $f(e^{i\theta})\frac{d\theta}{2\pi}=
\exp(\sqrt{\lambda}(z+z^{-1})) \frac{dz}{2\pi iz}$
on the unit circle, 
\begin{equation}
   \int_{-\pi}^{\pi} p_n(e^{i\theta})\overline{p_m(e^{i\theta})} 
f(e^{i\theta})\frac{d\theta}{2\pi}
=\delta_{n,m} \quad\text{for $n,m\geq 0$}.
\end{equation}
The leading coefficient $\kappa^2_n(\lambda)$ can be expressed
in terms of Toeplitz determinants,
\begin{equation}
   \kappa_n^2(\lambda)=\frac{D_{n-1}(\lambda)}{D_n(\lambda)}
\end{equation}
where $D_n(\lambda)=D_n(\exp(2\sqrt{\lambda}\cos\theta))$.
But by Szeg\"o's strong limit theorem (\cite{Sz2})
for Toeplitz determinants, 
$\lim_{n\to\infty}D_{n}(\lambda)=e^{\lambda}$, and hence 
\begin{equation}
  \log\phi_n(\lambda) =  \sum_{k=n}^{\infty} \log{\kappa^2_{k}(\lambda)}.
\end{equation}
Therefore, if one can control the large $k,\lambda$
behavior of $\kappa^2_{k}(\lambda)$
for all $k\geq n$, one will control the large 
$n,\lambda$ behavior of $\phi_n(\lambda)$.

The key point in our analysis is that
$\kappa^2_{k}(\lambda)$ can be expressed in terms of 
the following Riemann-Hilbert Problem (RHP) :
Let $\Sigma$ be the unit circle oriented counterclockwise.
Let $Y(z;k+1,\lambda)$ be the $2\times 2$ matrix-valued function satisfying
\begin{equation}\label{e-Y}
  \begin{cases}
     Y(z;k+1,\lambda) \quad\text{is analytic in}\quad \C-\Sigma,\\
     Y_+(z;k+1,\lambda)=Y_-(z;k+1,\lambda) \begin{pmatrix}
1&\frac{1}{z^{k+1}}e^{\sqrt{\lambda}(z+z^{-1})}\\0&1 \end{pmatrix}
\quad\text{on}\quad \Sigma,\\
     Y(z;k+1,\lambda) z^{-(k+1)\sigma_3}
=I+O(\frac1{z}) \quad\text{as}\quad z\to\infty,
  \end{cases}
\end{equation}
where $Y_+$ and $Y_-$ denote the limit from inside and outside of
the circle respectively, and $\sigma_3=
\bigl( \begin{smallmatrix} 1&0\\0&-1 \end{smallmatrix} \bigr)$, 
so that $z^{-(k+1)\sigma_3}=
\bigl( \begin{smallmatrix} z^{-(k+1)}&0\\
0&z^{k+1} \end{smallmatrix} \bigr)$.
Here $I$ is the $2\times 2$ identity matrix.
This RHP has a unique solution  
(see~\eqref{e-beg1} below), and the fact of the matter is that
\begin{equation}\label{e-Y21}
   \kappa^2_{k}(\lambda)=-Y_{21}(0;k+1,\lambda)
\end{equation}
where $Y_{21}(0;k,\lambda)$ is the $(21)$-entry of the solution
$Y$ at $z=0$.
In \cite{DZ1} and \cite{DZ}, Deift and Zhou introduced a steepest descent 
type method to compute the asymptotic behavior of RHP's containing 
large oscillatory and/or exponentially growing/decaying factors as in~\eqref{e-Y}.
This method was further extended in \cite{DVZ2} and eventually placed 
in a very general form by Deift, Zhou and Venakides in \cite{DVZ}, 
making possible the analysis of the limiting behavior 
of a large variety of asymptotic problems in pure and applied mathematics 
(see, e.g., \cite{DIZ}).
As we will see, the application of this method to~\eqref{e-Y} makes it possible 
to control the large $k,\lambda$ behavior of $\kappa_k^2(\lambda)$. 
The calculation in this paper have many similarities to the computations 
in [DKMVZ], where the authors use the steepest descent method to obtain 
Plancherel-Rotach type asymptotics for polynomials orthogonal with respect of 
varying weights, $e^{-NV(x)}dx$ on the real line, and hence to prove  
universality for a class of random matrix models.
The Riemann-Hilbert formulation of the theory of orthogonal 
polynomials on the line is due to Fokas, Its and Kitaev (\cite{FIK}) : 
the RHP~\eqref{e-Y} is an adaptation of the construction in \cite{FIK} 
to the case of orthogonal polynomial with respect to a weight 
on the unit circle.

\bigskip
This paper is arranged as follows. 
In Section~\ref{s-PII}, we discuss of some of the basic theory of RHP's 
and also provide some information on the RHP associated with the PII equation.
This information will be used in the construction of an approximate solution,  
i.e. a \emph{parametrix},  
for the RHP~\eqref{e-Y} in  
subsequent sections. The appearance of the 
PII equation in the limiting distribution 
$F(t)$ for $\chi_N$  
originates in this construction of the parametrix.
A connection of $\phi_n(\lambda)$ to Toda lattice and the Painlev\'e III equation 
is presented in Section~\ref{s-TL}.
Section~\ref{s- Begin} is the starting point for the 
analysis of the RHP~\eqref{e-Y}.
In this section, ~\eqref{e-Y} is transformed into an equivalent 
RHP via  
a so-called $g$-function.
The role of $g$-function, first introduced in \cite{DZ}, and then 
analyzed in full generality in \cite{DVZ}, 
is to replace exponentially growing terms in a RHP by oscillatory or 
exponentially decreasing terms.
It turns out that in the case of~\eqref{e-Y}, as in \cite{DKMVZ}, the 
$g$-function can be constructed in terms of an associated equilibrium 
measure $d\mu(s)$ as follows, 
\begin{equation}
   g(z)\equiv\int_{\Sigma} \log(z-s) d\mu(s).
\end{equation}
The measure $d\mu$ is the unique minimizer of the following variational problem : 
\begin{equation}\label{e-variational}
   E^{V}=\inf \{I^{V}(\wt{\mu}) : \text{$\wt{\mu}$ is a probability measure on the 
unit circle $\Sigma$}\}
\end{equation}
where 
\begin{equation}
   I^{V}(\wt{\mu})= \iint_{\Sigma\times\Sigma} \log|s-w|^{-1} 
d\wt{\mu}(s) d\wt{\mu}(w) +\int_{\Sigma} V(s) d\wt{\mu}(s)
\end{equation}
and $V(s)=-\sqrt{\lambda}(s+s^{-1})$. 
The variational problem~\eqref{e-variational} describes the equilibrium configuration 
of electrons, say, confined to the unit circle with Coulomb interactions, 
and acted on by an external field $V$.
It turns out that the support of the equilibrium measure depends  
critically on the quantity 
\begin{equation}
   \gamma=\frac{2\sqrt{\lambda}}{k+1}.
\end{equation}
We need to distinguish these two cases, $\gamma\le 1$ and $\gamma>1$.
As noted by Gross and Witten (\cite{GW}), and also by Johansson 
(\cite{Johan}), the point $\frac{2\sqrt{\lambda}}{k+1}=1$ corresponds 
to a (third order) phase transition for a statistical system 
with partition function~\eqref{e-DiS}.
The first case, when $\gamma=\frac{2\sqrt{\lambda}}{k+1}\le 1$, 
is discussed in 
Section~\ref{s-K1}, and the second case,  
when $\gamma=\frac{2\sqrt{\lambda}}{k+1}>1$, is discussed 
in Section~\ref{s-K2}.
The principal results of the above two sections are summarized in 
Lemmas~\ref{lem-K1} and ~\ref{lem-K2}. 
We obtain full asymptotics of $\kappa^2_{n}(\lambda)$ 
for $n, \lambda >0$ when $n, \lambda \to\infty$.
In Section~\ref{s-phi}, by summing up $\kappa^2_{k}(\lambda)$
for all $k\geq n$, we obtain the asymptotics of $\phi_n(\lambda)$ 
in Lemma~\ref{lem-phi}.
The relation between $\phi_n(N)$ and $q_{n,N}$ 
(de-Poissonization) is discussed in 
Section~\ref{s- dep}.
Finally, the proofs of Theorem~\ref{thm1} and~\ref{thm2} are given in 
Section~\ref{s-pf}.

\bigskip
\textbf{Notational remarks} : The primary variables in this paper are $n,N$, 
and $\lambda$. 
The letters $C$, $c$ denote general positive constants.
Rather than introducing many such constants $C_1,C_2,\cdots,c_1,c_2,\cdots,$ 
we always interpret $C,c$ in a general way. 
For example, we write $|f(x)|\le 2C|g(x)|+e^c|h(x)|\le C(|g(x)|+|h(x)|)$, etc. 
We will also use certain auxiliary positive parameters 
$M,M_1 ,M_2 ,\cdots,M_7$. 
If a constant depends on some of these parameters, we indicate 
this explicitly, for example, $C(M_2 ,M_4)$. 
In addition to the standard big $O$ notation, we also use a notation 
$O_M$. 
Thus $f=O(\frac1{n^{1/3}})$ means $|f|\le \frac{C}{n^{1/3}}$, where 
$C$ is independent of $M,M_1,\cdots$.
On the other hand, $f=O_M(\frac1{n^{1/3}})$ means 
$|f|\le \frac{C(M,M_1,\cdots)}{n^{1/3}}$, 
where $C(M,M_1,\cdots)$ depends on at least one of the parameters 
$M,M_1,\cdots$.

In the estimates that follow we will often claim that an inequality 
is true ``as $n\to\infty$''. 
For example, in~\eqref{e-z35} below, we say that 
\begin{equation*}
   |\log{\phi_n(\lambda)}| \le C\exp\biggl(-c(n+1)
\bigl(1-\frac{2\sqrt{\lambda}}{n+1}\bigr)^{3/2}\biggr),
\end{equation*}
as $n\to\infty$.
This mean that there exists a number $n_0$, say, which may 
depend on \emph{all} the other relevant constants in the problem, 
such that the inequality is true for $n\geq n_0$, etc.
(For this particular inequality the only other parameter is 
$M_5$, but it turns out that the constants $C$, $c$ can be 
chosen independent of $M_5$ (see below).)
