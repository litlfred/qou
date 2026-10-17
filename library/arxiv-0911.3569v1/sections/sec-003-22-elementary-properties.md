---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-003-22-elementary-properties
section_title: "Elementary properties."
section_number: 2.2
pages: 3-4
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 0.944
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
The following simple observation often allows multivariate problems to
be reduced to univariate ones, as will be seen. 
\begin{lemma}
A polynomial $f\in\CC[\x]$ is stable if and only if for all
$\a,\b\in\RR^m$ with $\b>\zero$, $f(\a + \b t)$ is stable in $\Stab[t]$.
\end{lemma}
\begin{proof}
Since $\HH^{m} = \{\a+\b t:\ \a,\b\in\RR^{m},\ \b>\zero,\
\mathrm{and}\ t\in\HH\}$, the result follows.
\end{proof}

For $f\in\CC[\x]$ and $i\in[m]$, let $\deg_i(f)$ denote the degree of $x_i$
in $f$.
\begin{lemma}
These operations preserve stability of polynomials in $\CC[\x]$.\\
\textup{(a)}\ \textbf{Permutation:}\ for any permutation $\sigma:[m]\goesto[m]$,
$f \mapsto f(x_{\sigma(1)},...,x_{\sigma(m)})$.\\
\textup{(b)}\ \textbf{Scaling:}\ for $c\in\CC$ and $\a\in\RR^{m}$ with
$\a>\zero$, $f \mapsto cf(a_{1}x_{1},\ldots,a_{m}x_{m})$.\\
\textup{(c)}\ \textbf{Diagonalization:}\ for $\{i,j\}\subseteq[m]$,
$f \mapsto f(\x)|_{x_i=x_j}$.\\
\textup{(d)}\ \textbf{Specialization:}\ for $a\in\Hbar$,
$f \mapsto f(a, x_{2},\ldots,x_{m})$.\\
\textup{(e)}\ \textbf{Inversion:}\ if $\deg_1(f)=d$,
$f \mapsto x_{1}^{d}f(-x_{1}^{-1},x_{2},\ldots,x_{m})$.\\
\textup{(f)}\ \textbf{Differentiation (or ``Contraction''):}\
$f \mapsto \partial_1 f(\x)$.
\end{lemma}
\begin{proof}
Parts (a,b,c) are clear.  Part (d) is also clear in the case that
$\Im(a)>0$.  For $a\in\RR$ apply part (d) with values in the sequence
$(a + \i 2^{-n}:\ n\in\NN)$, and then apply Hurwitz's Theorem to the
limit as $n\goesto\infty$.  Part (e) follows from the fact that
$\HH$ is invariant under the operation $z\mapsto -z^{-1}$.  For part (f),
let $d = \deg_{1}(f)$, and consider the sequence $f_{n} = n^{-d} 
f(nx_{1},x_{2},\ldots,x_{m})$ for all $n\geq 1$.  Each $f_{n}$
is stable and the sequence converges to a polynomial, so the limit is stable.
Since $\deg_1(f)=d$, this limit is not identically zero.  This implies that
for all $z_2,...,z_m\in\HH$, the polynomial $g(x)=f(x,z_2,...,z_m)\in\CC[x]$
has degree $d$.  Clearly $g'(x)=\partial_1 f(x,z_2,...,z_m)$.  Let
$\xi_1,...,\xi_d$ be the roots of $g(x)$, so that
$g(x)=c\prod_{h=1}^d (x-\xi_h)$ for some $c\in\CC$.
Since $f$ is stable, $\Im(\xi_h)\leq 0$ for all $h\in[d]$.  Now
$$
\frac{g'(x)}{g(x)}=\frac{d}{dx}\log g(x)=\sum_{h=1}^d\frac{1}{x-\xi_h}.
$$
If $\Im(z)>0$ then $\Im(1/(z-\xi_h))<0$ for all $h\in[d]$, so that
$g'(z)\neq 0$.  Thus, if $\z\in\HH^m$ then $\partial_1 f(\z)\neq 0$.
That is, $\partial_1 f$ is stable.
\end{proof}
\noindent
Of course, by permutation, parts (d,e,f) of Lemma 2.4 apply for any index
$i\in[m]$ as well (not just $i=1$).  Part (f) is essentially the Gauss-Lucas
Theorem:\ the roots of $g'(x)$ lie in the convex hull of the roots of $g(x)$.
