---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-004-23-univariate-stable-polynomials
section_title: "Univariate stable polynomials."
section_number: 2.3
pages: 4-6
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.96
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
A nonzero univariate polynomial is real stable if and only if
it has only real roots.  Let $f$ and $g$ be two such polynomials,
let $\xi_{1}\leq\xi_{2}\leq\cdots\leq\xi_{k}$ be the roots of $f$,
and let $\theta_{1}\leq\theta_{2}\leq\cdots\leq\theta_{\ell}$ be the 
roots of $g$.  These roots are \emph{interlaced} if they are ordered so that 
$\xi_{1}\leq\theta_{1}\leq\xi_{2}\leq\theta_{2}\leq\cdots$ or
$\theta_{1}\leq\xi_{1}\leq\theta_{2}\leq\xi_{2}\leq\cdots$.
For each $i\in[\ell]$, let $\ghat_{i} = g/(x-\theta_{i})$.  If $\deg f 
\leq \deg g$ and the roots of $g$ are simple,
then there is a unique $(a,b_{1},\ldots,b_{\ell})\in\RR^{\ell+1}$
such that
$$
f = ag + b_{1} \ghat_{1} + \cdots + b_{\ell} \ghat_{\ell}.
$$
\begin{exercise}
Let $f,g\in\StabR[x]$ be nonzero and such that $fg$ has only simple roots,
let $\deg f \leq \deg g$,  and let $\theta_{1}<\cdots<\theta_{\ell}$ be
the roots of $g$.  The following are equivalent:\\
\textup{(a)}\  The roots of $f$ and $g$ are interlaced.\\
\textup{(b)}\ The sequence  $f(\theta_{1}),f(\theta_{2}),\ldots,f(\theta_{\ell})$
alternates in sign (strictly).\\ 
\textup{(c)}\ In $f = ag + \sum_{i=1}^{\ell} b_{i} \ghat_{i}$, all of
$b_{1},\ldots,b_{\ell}$ have the same sign (and are nonzero).
\end{exercise}

The\emph{Wronskian} of $f,g\in \CC[x]$ is $\Wr[f,g]=f'\cdot g-f\cdot g'$.
If $f = ag + \sum_{i=1}^{\ell} b_{i} \ghat_{i}$ as in Exercise 2.5 then
$$
\frac{\Wr[f,g]}{g^{2}} = \frac{d}{dx}\left(\frac{f}{g}\right) =
\sum_{i=1}^{\ell} \frac{-b_{i}}{(x-\theta_{i})^{2}}.
$$
It follows that if $f$ and $g$ are as in Exercise 2.5(a) then
$\Wr[f,g]$ is either positive for all real $x$, or negative for
all real $x$.   Since $\Wr[g,f]=-\Wr[f,g]$ the condition that
$\deg f\leq \deg g$ is immaterial.  Any pair $f,g$ with interlacing 
roots can be approximated arbitrarily closely by such a pair with all
roots of $fg$ simple.  It follows that for any pair $f,g$ with interlacing 
roots, the Wronskian $\Wr[f,g]$ is either nonnegative on all of $\RR$ 
or nonpositive on all of $\RR$.

Nonzero univariate polynomials $f,g\in\StabR[x]$ are in \emph{proper position}, 
denoted by $f\ll g$, if $\Wr[f,g]\leq 0$ on all of $\RR$.
For convenience we also let $0\ll f$ and $f\ll 0$ for any 
$f\in\StabR[x]$;\ in particular $0\ll 0$.

\begin{exercise}
Let $f,g\in\StabR[x]$ be real stable.  Then $f \ll g$ and $g\ll f$
if and only if $cf=dg$ for some $c,d\in\RR$ not both zero.
\end{exercise}

\noindent
\textbf{Hermite-Kakeya-Obreschkoff (HKO) Theorem}
(Theorem 6.3.8 of \cite{RS})\textbf{.}\ \emph{
Let $f,g\in\RR[x]$.  Then $af+bg\in\StabR[x]$ for all $a,b\in\RR$
if and only if $f,g\in\StabR[x]$  and either $f\ll g$ or $g\ll f$.
}\\

\noindent
\textbf{Hermite-Biehler (HB) Theorem}
(Theorem 6.3.4 of \cite{RS})\textbf{.}\ \emph{
Let $f,g\in\RR[x]$.  Then $g+\i f\in\Stab[x]$ if and only if 
$f,g\in\StabR[x]$ and $f\ll g$.
}\\

\begin{proof}[Proofs of HKO and HB]
It suffices to prove these when $fg$ has only simple roots.

For HKO we can assume that $\deg(f)\leq\deg(g)$.  Exercise 2.5
shows that if the roots of $f$ and $g$ are interlaced then for all $a,b\in\RR$,
the roots of $g$ and $af+bg$ are interlaced, so that $af+bg$ is real stable.
The converse is trivial if $cf=dg$ for some $c,d\in\RR$ not both zero, so
assume otherwise.  From the hypothesis, both $f$ and $g$ are real stable.
If there are $z_0,z_1\in\HH$ for which $\Im(f(z_0)/g(z_0))<0$ and
$\Im(f(z_1)/g(z_1))>0$, then for some $\lambda\in[0,1]$ the number
$z_\lambda=(1-\lambda)z_0+\lambda z_1$ is such that
$\Im(f(z_\lambda)/g(z_\lambda))=0$.  Thus $f(z_\lambda)-a g(z_\lambda)=0$
for some real number $a\in\RR$.  Since $f-ag$ is stable (by hypothesis)
and $z_\lambda\in\HH$, this implies that $f-ag\equiv 0$, a contradiction.
Thus $\Im(f(z)/g(z))$ does not change sign for $z\in\HH$.  This implies
Exercise 2.5(c):\  all the $b_i$ have the same sign
(consider $f/g$ at the points $\theta_i+\i \epsilon$ for $\epsilon>0$
approaching $0$).  Thus, the roots of $f$ and $g$ are interlaced.

For HB, let $p=g+\i f$.  Considering $\i p=-f+\i g$ if necessary, we can
assume that $\deg f\leq \deg g$.  If $f\ll g$ then Exercise 2.5(c)
implies that $\Im(f(z)/g(z))\leq 0$ for all $z\in\HH$, so that
$g+\i f$ is stable.  For the converse, let $p(x)=c\prod_{i=1}^d(x-\xi_i)$,
so that $\Im(\xi_i)\leq 0$ for all $i\in[d]$.
Now $|z-\xi_i|\geq |\overline{z}-\xi_i|$ for all $z\in\HH$ and $i\in[d]$,
so that $|p(z)|\geq|p(\overline{z})|$ for all $z\in\HH$.
For any $z\in\HH$ with $f(z)\neq 0$ we have
$$
\left|\frac{g(z)}{f(z)}+\i\right| \geq
\left|\frac{g(\overline{z})}{f(\overline{z})}+\i\right| =
\left|\frac{g(z)}{f(z)}-\i\right|,
$$
and it follows that $\Im(g(z)/f(z))\geq 0$ for all $z\in\HH$ with $f(z)\neq 0$.
Since $fg$ has simple roots it follows that $g(x)+y f(x)$ is stable in
$\Stab[x,y]$.  By contraction and specialization, both $f$ and $g$ are real
stable.  By scaling and specialization, $af+bg$ is stable for all $a,b\in\RR$.
By HKO, the roots of $f$ and $g$ are interlaced.  Since $\Im(f(z)/g(z))\leq 0$
for all $z\in\HH$, all the $b_i$ in Exercise 2.5(c) are positive, so
that $\Wr[f,g]$ is negative on all of $\RR$:\ that is $f\ll g$.
\end{proof}

For $\lambda:\NN\goesto\RR$, let $T_{\lambda}:\RR[x]\goesto\RR[x]$ 
be the linear transformation defined by $T_{\lambda}(x^{n}) = 
\lambda(n) x^{n}$ and linear extension.  A \emph{multiplier sequence
(of the first kind)} is such a $\lambda$ for which $T_{\lambda}(f)$
is real stable whenever $f$ is real stable.  P\'olya and Schur 
characterized multiplier sequences as follows.\\

\noindent
\textbf{P\'olya-Schur Theorem} (Theorem 1.7 of \cite{BB4})\textbf{.}\ \emph{
Let $\lambda:\NN\goesto\RR$.  The following are equivalent:\\
\textup{(a)}\ $\lambda$ is a multiplier sequence.\\
\textup{(b)}\ $F_{\lambda}(x)=\sum_{n=0}^{\infty} \lambda(n) x^{n}/n!$ is an entire 
function which is the limit, uniformly on compact sets, of real
stable polynomials with all roots of the same sign.\\
\textup{(c)}\ Either $F_{\lambda}(x)$ or $F_{\lambda}(-x)$ has the form
$$
Cx^{n}\e^{ax}\prod_{j=1}^{\infty}(1+\alpha_{j}x),
$$
in which $C\in\RR$, $n\in\NN$, $a\geq 0$, all $\alpha_{j}\geq 0$,
and $\sum_{j=1}^{\infty}\alpha_{j}$ is finite.\\
\textup{(d)}\ For all $n\in\NN$, the polynomial 
$T_{\lambda}((1+x)^{n})$ is real stable with all roots of the same 
sign.
}\\

One of the main results of Borcea and Br\"and\'en's theory is a
great generalization of the P\'olya-Schur Theorem -- a 
characterization of \underline{all} \emph{stability preservers}: linear
transformations $T:\CC[\x]\goesto\CC[\x]$ such that $T(f)$ is stable
whenever $f$ is stable.  (Also the analogous characterization of real
stability preservers.)  This is discussed in some detail in Section 5.3.
