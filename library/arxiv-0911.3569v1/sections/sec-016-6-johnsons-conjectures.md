---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-016-6-johnsons-conjectures
section_title: "Johnson's Conjectures."
section_number: 6
pages: 17-19
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.964
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
Let $\A = (A_{1},\ldots,A_{k})$ be a $k$-tuple of $n$-by-$n$ matrices.
Define the \emph{mixed determinant} of $\A$ to be
$$
\Det(\A) = \Det(A_{1},\ldots,A_{k}) = 
\sum_{(S_{1},\ldots,S_{k})} \prod_{i=1}^{k} \det A_{i}[S_{i}],
$$
in which the sum is over all ordered sequences of $k$ pairwise disjoint
subsets of $[n]$ such that $[n]=S_{1}\cup\cdots\cup S_{k}$,  and
$A_{i}[S_{i}]$ is the principal submatrix of $A_{i}$ supported on rows 
and columns in $S_{i}$.  Let $A_i(S_i)$ be the complementary
principal submatrix supported on rows and columns not in $S_i$,
and for $j\in[n]$ let $A_i(j)=A_i(\{j\})$.

For example, when $k=2$ and $A_{1}=xI$ and $A_{2}=-B$, this specializes 
to $\Det(xI,-B)=\det(xI-B)$, the characteristic polynomial of $B$.
In the late 1980s, Johnson made three conjectures about
the $k=2$ case more generally.\\

\noindent
\textbf{Johnson's Conjectures.}\  \emph{
Let $A$ and $B$ be $n$-by-$n$ matrices, with $A$ positive definite
and $B$ Hermitian.\\
\textup{(a)}\  Then $\Det(xA,-B)$ has only real roots.\\
\textup{(b)}\  For $j\in[n]$, the roots of 
$\Det(xA(j),-B(j))$ interlace those of $\Det(xA,-B)$.\\
\textup{(c)}\  The inertia of $\Det(xA,-B)$ is the same as that of
$\det(xI-B)$.}\\

In part (c), the \emph{inertia} of a univariate real stable polynomial $p$
is the triple $\iota(p)=(\iota_{-}(p),\iota_{0}(p),\iota_{+}(p))$
with entries the number of negative, zero, or positive roots of $p$, respectively.

In 2008, Borcea and Br\"and\'en \cite{BB1} proved all three of these
statements in much greater generality.

\begin{theorem}[Theorem 2.6 of \cite{BB1}]
Fix integers $\ell,m,n\geq 1$.  For $h\in[\ell]$ and $i\in[m]$
let $B_{h}$ and $A_{hi}$ be $n$-by-$n$ matrices, and let
$$
L_{h} = \sum_{i=1}^{m} x_{i} A_{hi} + B_{h}.
$$
\textup{(a)}\
If all the $A_{hi}$ are positive semidefinite and all the $B_{h}$
are Hermitian, then $\Det(\L)=\Det(L_{1},\ldots,L_\ell)
\in\StabR[\x]$ is real stable.\\
\textup{(b)}\
For each $j\in[n]$, let $\L(j)=(L_{1}(j),\ldots,L_\ell(j))$.
With the hypotheses of part (a),
the polynomial $\Det(\L)+y\Det(\L(j))\in\StabR[\x,y]$ is real stable.
\end{theorem}
\begin{proof}
Let $Y=\diag(y_1,...,y_n)$ be a diagonal matrix of indeterminates.
By Proposition 2.1, for each $h\in[\ell]$ the polynomial
$$
\det(Y+L_h) = \sum_{S\subseteq[n]}\y^S \det L_h(S)
$$
is real stable in $\StabR[\x,\y]$.
By inversion of all the $\y$ indeterminates, each
$$
\det(I-YL_h)=  \sum_{S\subseteq[n]}(-1)^{|S|} \y^S \det L_h[S]
$$
is real stable.  Since $\prod_{h=1}^\ell \det(I-YL_h)$ is real 
stable, contraction and specialization imply that
$$
\Det(\L) =
(-1)^n 
\left.\frac{\partial^n}{\partial y_1\cdots \partial y_n}
\prod_{h=1}^\ell \det(I-YL_h)\right|_{\y=\zero}
$$
is real stable, proving part (a).

For part (b), let $V$ be the $n$-by-$n$ matrix with all entries
zero except for $V_{jj}=y$.  By part (a),
$$
\Det(V,L_1,...,L_h)=\Det(\L) + y \Det(\L(j))
$$
is real stable.
\end{proof}

Theorem 6.1 (with Corollary 2.10) clearly settles Conjectures (a) and (b).

\begin{proof}[Proof of Conjecture (c).]
Let $A$ and $B$ be $n$-by-$n$ matrices with 
$A$ positive definite and $B$ Hermitian.  Let $(\iota_-,\iota_0,\iota_+)$
be the inertia of $\det(xI-B)$.  Let $f(x) = \Det(xA,-B)$, and let
$(\nu_-,\nu_0,\nu_+)$ be the inertia of $f$.

We begin by showing that $\nu_0=\iota_0$.
Since $\iota_0=\min\{|S|:\ S\subseteq[n]\ \mathrm{and}\ \det(B(S))\neq 0\}$,
it follows that $\nu_0\geq \iota_0$.  The constant term of $f(x)$ is
$(-1)^n\det(B)$, so that if $\iota_0=0$ then $\nu_0=0$.  If $\iota_0=k>0$
then let $S=\{s_1,...,s_k\}\subseteq[n]$ be such that $\det(B(S))\neq 0$.
For $0\leq i\leq k$ let 
$f_i(x)=\Det(A(\{s_1,..,s_i\}),-B(\{s_1,..,s_i\}))$,
so that $f_0(x)=f(x)$.  By Theorem 6.1, the roots of $f_{i-1}$ and of
$f_i$ are interlaced, for each $i\in[k]$.  Thus,
$$
\nu_0 = \iota_0(f_0) \leq \iota_0(f_1)+1 \leq \iota_0(f_2)+2 \leq
\cdots \leq \iota_0(f_k)+k = k = \iota_0,
$$
since $\iota_0(f_k)=0$ because $\det(B(S))\neq 0$.  Therefore $\nu_0=\iota_0$.

For any positive definite matrix $A$, $\Det(xA,-B)$ is a polynomial of degree
$n$.  Suppose that $A$ is such a matrix for which $\nu_+\neq\iota_+$.
Consider the matrices $A_\lambda = (1-\lambda)I+\lambda A$ for
$\lambda\in[0,1]$.  Each of these matrices is positive definite.
From the paragraph above, each of the polynomials
$g_\lambda(x)=\Det(xA_\lambda,-B)$ has $\iota_0(g_\lambda)=\iota_0$.
Since $\iota_+(g_0)=\iota_+\neq\nu_+=\iota_+(g_1)$ and the roots of $g_\lambda$
vary continuously with $\lambda$, there is some value $\mu\in(0,1)$ for which
$\iota_0(g_\mu)>\iota_0$.  This contradiction shows that $\nu_+=\iota_+$,
and hence $\nu_-=\iota_-$ as well.
\end{proof}

Borcea and Br\"and\'en \cite{BB1} proceed to derive many inequalities for
the principal minors of positive semidefinite matrices, and some for merely
Hermitian matrices.  These are applications of inequalities valid more
generally for real stable polynomials.  The simplest of these inequalities are
as follows.

For an $n$-by-$n$ matrix $A$, the \emph{$j$-th symmetrized Fisher product}
is
$$
\sigma_j(A) = \sum_{S\subseteq[n]:\ |S|=j} \det(A[S])\det(A(S)).
$$
and the \emph{$j$-th averaged Fisher product} is
$\widehat{\sigma}_j(A) = \binom{n}{j}^{-1} \sigma_j(A)$.
Notice that $\sigma_j(A)=\sigma_{n-j}(A)$ for all $0\leq j\leq n$.

\begin{coro}
Let $A$ be an $n$-by-$n$ positive semidefinite matrix.\\
\textup{(a)}\ Then $\widehat{\sigma}_j(A)^2 \geq 
\widehat{\sigma}_{j-1}(A) \widehat{\sigma}_{j+1}(A)$
for all $1\leq j\leq n-1$.\\
\textup{(b)}\ Also, $\widehat{\sigma}_0(A)\leq \widehat{\sigma}_1(A)
\leq \cdots \leq \widehat{\sigma}_{\lfloor n/2\rfloor}$.\\
\textup{(c)}\  If $A$ is positive definite and $\det(A)=d$ then
$$
\frac{\widehat{\sigma}_1(A)}{d} \geq
\left(\frac{\widehat{\sigma}_2(A)}{d}\right)^{1/2} \geq
\left(\frac{\widehat{\sigma}_3(A)}{d}\right)^{1/3} \geq \cdots \geq
\left(\frac{\widehat{\sigma}_n(A)}{d}\right)^{1/n} =1.
$$
\end{coro}
\begin{proof}
It suffices to consider positive definite $A$.
By Theorem 6.1, the polynomial $\Det(xA,-A)=\sum_{j=0}^n (-1)^j
\sigma_j(A) x^j$ has only real roots, and these roots are all positive.
Part (a) follows from Newton's Inequalities \cite[Theorem 51]{HLP}.
Part (a) and the symmetry $\sigma_j(A)=\sigma_{n-j}(A)$ for all $0\leq j\leq n$
imply part (b).  Part (c) follows from Maclaurin's Inequalities
\cite[Theorem 52]{HLP}.
\end{proof}
