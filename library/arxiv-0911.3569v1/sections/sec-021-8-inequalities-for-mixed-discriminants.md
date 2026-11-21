---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-021-8-inequalities-for-mixed-discriminants
section_title: "Inequalities for mixed discriminants."
section_number: 8
pages: 23-27
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.94
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
This section summarizes a powerful application of stable polynomials from
a 2008 paper of Gurvits \cite{Gu}.

We will use without mention the facts that $\log$ and $\exp$ are strictly
increasing functions on $(0,\infty)$.
A function $\rho:I\goesto\RR$ defined on an interval $I\subseteq\RR$ is
\emph{convex} provided that for all $a_1,a_2\in I$,
$\rho((a_1+a_2)/2)\leq (\rho(a_1)+\rho(a_2))/2$.  It is \emph{strictly
convex} if it is convex and equality holds here only when $a_1=a_2$.
A function $\rho:I\goesto\RR$ is \emph{(strictly) concave} if $-\rho$
is (strictly) convex.
For example, for positive reals $a_1,a_2>0$ one has
$(\sqrt{a_1}-\sqrt{a_2})^2\geq0$, with equality only if $a_1=a_2$.
It follows that $\log((a_1+a_2)/2)\geq (\log(a_1) + \log(a_2))/2$, with
equality only if $a_1=a_2$.  That is, $\log$ is strictly concave.\\

\noindent\textbf{Jensen's Inequality} (Theorem 90 of \cite{HLP})\textbf{.}\
\emph{
Let $\rho:I\goesto\RR$ be defined on an interval $I\subseteq\RR$,
let $a_i\in I$ for $i\in[n]$, and let $b_i>0$ for $i\in[n]$ be such
that $\sum_{i=1}^n b_i = 1$.  If $\rho$ is convex then
$$
\rho\left(\sum_{i=1}^n b_i a_i\right) \leq
\sum_{i=1}^n b_i\, \rho(a_i).
$$
If $\rho$ is strictly convex and equality holds, then $a_1=a_2=\cdots=a_n$.}\\

For integer $d\geq 1$, let $\G(d) = (1-1/d)^{d-1}$, and let $\G(0)=1$.
Note that $\G(1)=0^0=1$, and that $\G(d)$ is a strictly decreasing function
for $d\geq 1$.  For homogeneous $f\in\RR[\x]$ with nonnegative coefficients,
define the \emph{capacity} of $f$ to be
$$
\CAP(f) = \inf_{\c>\zero} \frac{f(\c)}{c_1\cdots c_m},
$$
with the infimum over the set of all $\c\in\RR^m$ with $c_i>0$ for all $i\in[m]$.

\begin{lemma}[Lemma 3.2 of \cite{Gu}]
Let $f=\sum_{i=0}^d b_i x\in\RR[x]$ be a nonzero
univariate polynomial of degree $d$ with nonnegative coefficients.
If $f$ is real stable then
$b_1=f'(0)\geq \G(d)\CAP(f)$, and if $\CAP(f)>0$ then
equality holds if and only if $d\leq 1$ or $f(x) = b_d(x+\xi)^d$ for some $\xi>0$.
\end{lemma}
\begin{proof}
If $\CAP(f)=0$ then there is nothing to prove,
so assume that $\CAP(f)>0$.
If $d=0$ then $f'(0)= b_{1} = 0 = \G(0)\CAP(f)$, and
if $d=1$ then $f'(0)= b_1 = \G(1)\CAP(f)$, so assume that $d\geq 2$.
If $f(0)=0$ then $f'(0)=\lim_{c\goesto 0}f(c)/c\geq \CAP(f) > 
\G(d)\CAP(f)$.
Thus, assume that $d\geq 2$ and $f(0)=b_0>0$.  We may rescale the polynomial
so that $b_0=1$.  Now there are $a_i>0$ for $i\in[d]$ such that
$$
f(x) = \prod_{i=1}^d (1+a_i x),
$$
and $b_1=a_1+\cdots+a_d$.  For any $c>0$ we have
$$
\frac{\log(\CAP(f)c)}{d}
\leq
\frac{\log(f(c))}{d} = \frac{1}{d}\sum_{i=1}^d \log(1+a_i c)
\leq
\log\left(1+\frac{b_1 c}{d}\right),
$$
by Jensen's Inequality.  It follows that $\CAP(f)c\leq (1+b_1c/d)^d$
for all $c>0$.  Let $g(x)=(1+b_1x/d)^d$.  Elementary calculus shows that
$$
\CAP(g)= \inf_{c>0} \frac{g(c)}{c} = \frac{g(c_*)}{c_*} = \frac{b_1}{\G(d)},
\ \ \mathrm{in\ which}\ \ c_*=\frac{d}{b_1(d-1)}.
$$
Since $\CAP(f)\leq \CAP(g)$, this yields the stated inequality.
If equality holds, then equality holds in the application
of Jensen's Inequality, and so $f$ has the stated form.
\end{proof}

\begin{lemma}[Theorem 4.10 of \cite{Gu}]
Let $f\in\StabR[x_1,...,x_m]$ be real stable, with nonnegative 
coefficients, and homogeneous of degree $m$.
Let $g = \partial_m f|_{x_m=0}$.  Then
$$
\CAP(g) \geq \G(\deg_m(d))\CAP(f).
$$
\end{lemma}
\begin{proof}
We may assume that $d=\deg_m(f)\geq 1$.
Let $c_i>0$ for $i\in[m-1]$, and let $p_\c(x)=f(c_1,...,c_{m-1},x)$.
Since $f$ has nonnegative coefficients, $p_{\c}\not\equiv 0$.
As in the proof of Lemma 2.4(f), $p_\c$ has degree $d$.
By specialization, $p_\c$ is real stable.  Lemma 8.1 implies that
$$
g(\c)=p_\c'(0)\geq \G(d)\CAP(p_\c)\geq\G(d)\CAP(f)
$$
for all $\c\in\RR^{m-1}$ with $\c>\zero$.  If $m=1$ then $g=\CAP(g)$
is a constant.  If $m\geq 2$ then for any such $\c$ let
$b=(c_1\cdots c_{m-1})^{-1/(m-1)}$.  Since $g$ is homogeneous of
degree $m-1$,
$$
\frac{g(\c)}{c_1\cdots c_{m-1}}=g(bc_1,...,bc_{m-1})
\geq 
\G(d)\CAP(f).
$$
It follows that $\CAP(g)\geq \G(d)\CAP(f)$.
\end{proof}

\begin{theorem}[Theorem 2.4 of \cite{Gu}]
Let $f\in\StabR[x_1,...,x_m]$ be real stable, with nonnegative 
coefficients, and homogeneous of degree $m$.  Let $\deg_{i}(f)=d_i$
and $e_i=\min\{i,d_i\}$ for each $i\in[m]$.  Then
$$
\del^{\one} f(\zero) \geq \CAP(f)\prod_{i=2}^m \G(e_i).
$$
\end{theorem}
\begin{proof}
Let $g_m=f$ and let $g_{i-1}=\partial_i g_i|_{x_i=0}$ for all
$i\in[m]$.  By contraction and specialization, $g_{i}$ is real stable
for each $i\in[m]$.  Notice that $g_0=\del^{\one} f(\zero)=\CAP(g_0)$.
By Lemma 8.2.
$\CAP(g_{i-1})\geq\CAP(g_i)\cdot \G(\deg_i g_i)$ for each $i\in[m]$.
But $\deg_i g_i \leq \deg_i f = d_i$, and $\deg_i g_i$ is at most the
total degree of $g_i$, which is $i$.  Hence $\deg_i g_i \leq e_i$,
and thus $\G(\deg_i g_i) \geq \G(e_i)$.  Thus
$\CAP(g_{i-1})\geq\CAP(g_i)\cdot \G(e_{i})$ for each $i\in[m]$.
Combining these inequalities (and $\G(e_1)=1$) gives the result.
\end{proof}

With the notation of Theorem 8.3, since $e_i\leq i$ for all $i\in[m]$
and $G(d)$ is a decreasing function of $d$, one has the inequality
$$
\prod_{i=2}^m \G(e_i) \geq \prod_{i=2}^m \G(i)
= \prod_{i=2}^m \left(\frac{i-1}{i}\right)^{i-1} = \frac{m!}{m^m}.
$$
Thus, the following corollary is immediate.
\begin{coro}
Let $f\in\StabR[x_1,...,x_m]$ be real stable, with nonnegative 
coefficients, and homogeneous of degree $m$.  Then
$$
\del^{\one} f(\zero) \geq \frac{m!}{m^m}\cdot\CAP(f).
$$
\end{coro}

\begin{theorem}[Theorem 5.7 of \cite{Gu}]
Let $f\in\StabR[x_1,...,x_m]$ be real stable, with nonnegative 
coefficients, and homogeneous of degree $m$.  Equality holds in the bound of
Corollary 8.4 if and only if there are nonnegative reals $a_i\geq 0$ for
$i\in[m]$ such that
$$
f(\x) = (a_1 x_1 + \cdots + a_m x_m)^m.
$$
\end{theorem}
(We omit the proof.)

\begin{lemma}[Fact 2.2 of \cite{Gu}]
Let $f\in\RR[x_1,...,x_m]$ be homogeneous of degree $m$, with nonnegative
coefficients.  Assume that $\partial_{i}f(\one)=1$ for all $i\in[m]$.  Then $\CAP(f)=1$.
\end{lemma}
\begin{proof}
Let $f=\sum_{\alpha} b(\alpha) \x^{\alpha}$, so that if 
$b(\alpha)\neq 0$ then $|\alpha|=\sum_{i=1}^{m}\alpha(i)=m$.
By hypothesis, for all $i\in[m]$, $\sum_{\alpha} b(\alpha)\alpha(i)=1$.
Averaging these over all $i\in[m]$ yields $f(\one)=\sum_{\alpha} b(\alpha)=1$,
so that $\CAP(f)\leq 1$.  Conversely, let $\c\in\RR^{m}$ with $\c>\zero$.
Jensen's Inequality implies that
\showon
\log(f(\c))
&=&
\log\left(\sum_{\alpha} b(\alpha) \c^{\alpha}\right)\\
&\geq&
\sum_{\alpha} b(\alpha) \log(\c^{\alpha})
=
\sum_{i=1}^{m}\log(c_{i})\sum_{\alpha} b(\alpha)\alpha(i)
=
\log( c_{1}\cdots c_{m}).
\showoff
It follows that $\CAP(f)\geq 1$.
\end{proof}

\begin{example}[van der Waerden Conjecture]
An $m$-by-$m$ matrix $A=(a_{ij})$ is \emph{doubly stochastic} if 
all entries are nonnegative reals and every row and column sums to one.
In 1926, van der Waerden conjectured that if $A$ is an $m$-by-$m$ doubly
stochastic matrix then $\per(A) \geq m!/m^m$, with equality if and only if
$A=(1/m)J$, the $m$-by-$m$ matrix in which every entry is $1/m$.
In 1981 this lower bound was proved by Falikman, and the characterization of
equality was proved by Egorychev.  These results follow immediately from
Corollary 8.4 and Theorem 8.5, as follows.  It suffices to prove the
result for an $m$-by-$m$ doubly stochastic matrix $A=(a_{ij})$ with
no zero entries, by a routine limit argument.  The polynomial
$$
f_A(\x) = \prod_{j=1}^m\left(a_{1j} x_1 + \cdots + a_{mj} x_m\right)
$$
is clearly homogeneous and real stable, with nonnegative coefficients and
of degree $m$, and such that $\deg_{i}(f_{A})=m$ for all $i\in[m]$.   Since $A$
is doubly stochastic, Lemma 8.6 implies that $\CAP(f_{A})=1$.
Since
$$
\per(A) = \del^{\one} f_A(\zero),
$$
Corollary 8.4 and Theorem 8.5 imply the results of Falikman and Egorychev,
respectively.  Gurvits \cite{Gu} also uses a similar argument to prove a refinement
of the van der Waerden conjecture due to Schrijver and Valiant -- see 
also \cite{LS}.
\end{example}

Given $n$-by-$n$ matrices $A_1$,...,$A_m$, the \emph{mixed discriminant} of
$\AA = (A_1,...,A_m)$ is
$$
\Disc(\AA) =
\left. \del^{\one} \det(x_1 A_1 + \cdots + x_m A_m)\right|_{\x=\zero}.
$$
This generalizes the permanent of an $m$-by-$m$ matrix $B=(b_{ij})$
by considering the collection of matrices $\AA(B) = (A_1,...,A_m)$
defined by $A_h = \diag(a_{h1},...,a_{hm})$ for each $h\in[m]$.
In this case one sees that 
$$
\det(x_1 A_1 + \cdots + x_m A_m) = f_B(\x)
$$
with the notation of Example 8.7, and it follows that
$\Disc(\AA(B)) = \per(B)$.

\begin{example}[Bapat's Conjecture]
Generalizing the van der Waerden conjecture, in 1989 Bapat considered
the set $\Omega(m)$ of $m$-tuples of $m$-by-$m$ matrices
$\AA = (A_1,...,A_m)$ such that each $A_i$ is positive semidefinite
with trace $\tr(A_i)=1$, and $\sum_{i=1}^m A_i = I$.  For any doubly stochastic
matrix $B$, $\AA(B)$ is in this set.  The natural conjecture is that for
all $\AA\in\Omega(m)$, $\Disc(\AA)\geq m!/m^m$, and equality is
attained if and only if $\AA=\AA((1/m)J)$.  This was proved by Gurvits in 2006 --
again, it follows directly from Corollary 8.4 and Theorem 8.5.
It suffices to prove the result for $\AA\in\Omega(m)$ such that
each $A_{i}$ is positive definite, by a routine limit argument. 
By Proposition 2.1, for $\AA\in\Omega(m)$, the polynomial
$$
f_\AA(\x) = \det(x_1 A_1 + \cdots + x_m A_m)
$$
is real stable.  Since each $A_i$ is positive definite, all coefficients
of $f_\AA$ are nonnegative, $f_\AA$ is homogeneous of degree 
$m$,  and $\deg_{i}(f_{A})=m$ for all $i\in[m]$.
Since $\AA\in \Omega(m)$, Lemma 8.6 implies that 
$\CAP(f_{\AA})=1$.  Thus, $f_\AA$ satisfies the hypothesis of Theorems 
8.3 and 8.5, and since $\Disc(\AA) = \del^{\one} f_\AA(\zero)$,
the result follows.
\end{example}
