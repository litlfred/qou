---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-014-52-linear-transformations-preserving-stability-p
section_title: "Linear transformations preserving stability – polynomial case."
section_number: 5.2
pages: 15-19
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.938
---
\begin{theorem}[Theorem 1.1 of \cite{BB5}]
Let $\kappa\in\NN^m$, and let $T:\CC[\x]^{\leq\kappa}\goesto\CC[\x]$
be a linear transformation.
Then $T$ maps $\Stab[\x]^{\leq\kappa}$ into $\Stab[\x]$ if and only if 
either\\
\textup{(a)}\ $T(f) = \eta(f)\cdot p$ for some linear functional
$\eta:\CC[\x]^{\leq\kappa}\goesto\CC$ and $p\in\Stab[\x]$, or\\
\textup{(b)}\ the polynomial $T((\x+\y)^\kappa)$ is stable in $\Stab[\x,\y]$.
\end{theorem}
\begin{proof}
Let $\u=\{u_{ij}:\ (i,j)\in I(\kappa)\}$, and define a linear 
transformation $\widetilde{T}:\CC[\u]^{\ma}\goesto\CC[\x]$ as follows.
For every $A\subseteq I(\kappa)$, define $\alpha(A):[m]\goesto\NN$ by 
putting $\alpha(A,i) = |\{j\in[\kappa(i)]:\ (i,j)\in A\}|$ for each 
$i\in[m]$.  Then for each $A\subseteq I(\kappa)$ define
$\widetilde{T}(\u^{A}) = T(\x^{\alpha(A)})$, and extend this linearly to
all of $\CC[\u]^{\ma}$.  Let $\Delta:\CC[\u]^{\ma}\goesto\CC[\x]$ be
the diagonalization operator defined by $\Delta(u_{ij})=x_{i}$ for all
$(i,j)\in I(\kappa)$, extended algebraically.

Notice that $T = \widetilde{T}\circ\Pol_{\kappa}$,
and that $\widetilde{T} = T\circ\Delta$.  By Proposition 5.1 (and 
Lemma 2.4), it follows that $T$ preserves stability if and 
only if $\widetilde{T}$ preserves stability.  This is
equivalent to one of two cases in Theorem 3.4.

In case (a), if $\widetilde{T}= p\cdot\widetilde{\eta}$ for some 
$p\in\Stab[\x]$ and linear functional $\widetilde{\eta}:\CC[\y]^{\ma}\goesto\CC$
then $T=p\cdot (\eta\circ \Pol_{\kappa})$ is also in case (a).
Conversely, if $T$ is in case (a) then the same is true of 
$\widetilde{T}$, by construction.

In case (b), let 
$\Pol_{\kappa}^{(\y)}:\CC[\y]^{\leq\kappa}\goesto\CC[\v]^{\ma}$
denote the $\kappa$-th polarization of the $\y$ variables.
The symbols of $T$ and $\widetilde{T}$ are related by
$$
\widetilde{T}((\u+\v)^{I(\kappa)}) =
(T\circ \Delta)((\u+\v)^{I(\kappa)}) =
\Pol_{\kappa}^{(\y)}T((\x+\y)^{\kappa}),
$$
and Proposition 5.1 shows that $T$ is in case (b) if and only if
$\widetilde{T}$ is in case (b).
\end{proof}



\subsection{Linear transformations preserving stability -- 
transcendental case.}

\begin{exercise}
Let $T:\CC[\x]\goesto\CC[\x]$ be a linear transformation.\\
\textup{(a)}\ Then $T:\Stab[\x]\goesto\Stab[\x]$ if and only if
$T:\Stab[\x]^{\leq\kappa}\goesto\Stab[\x]$ for all 
$\kappa\in\NN^{m}$.\\ 
\textup{(b)}\ Define $S:\CC[\x,\y]\goesto\CC[\x,\y]$ by $S(\x^{\alpha}\y^{\beta})=
T(\x^{\alpha})\y^{\beta}$ and linear extension.  If $T((\x+\u)^{\kappa})$
is stable for all $\kappa\in\NN^{m}$ then
$S((\x+\u)^{\kappa}(\y+\v)^{\beta})$ is stable for all $\kappa,\beta\in\NN^{m}$.
\end{exercise}

Let $\overline{\Stab[\x]}$ denote the set of all power series in
$\CC[[\x]]$ that are obtained as the limit of a sequence of stable polynomials
in $\Stab[\x]$ which converges uniformly on compact sets.
Theorem 5.4 is an astounding generalization of the P\'olya-Schur Theorem.
For $\alpha\in\NN^{m}$, let $\alpha!=\prod_{i=1}^{m}\alpha(i)!$.

\begin{theorem}[Theorem 1.3 of \cite{BB5}]
Let $T:\CC[\x]\goesto\CC[\x]$ be a linear transformation.
Then $T$ maps $\Stab[\x]$ into $\Stab[\x]$ if and only if 
either\\
\textup{(a)}\ $T(f) = \eta(f)\cdot p$ for some linear functional
$\eta:\CC[\x]\goesto\CC$ and $p\in\Stab[\x]$, or\\
\textup{(b)}\ the power series
$$T(\e^{-\x\y}) = \sum_{\alpha:[m]\goesto\NN}(-1)^{\alpha}
T(\x^\alpha)\frac{\y^\alpha}{\alpha!}
$$
is in $\overline{\Stab[\x,\y]}$ 
\end{theorem}
(Theorem 3.5 has a similar extension -- see Theorems 1.2 and 1.4 of
\cite{BB5}.)

For $\alpha\leq \beta$ in $\NN^{m}$, let $(\beta)_{\alpha} = 
\beta!/(\beta-\alpha)!$, and for $\alpha\not\leq\beta$ let
$(\beta)_{\alpha} = 0$.

\begin{theorem}[Theorem 5.1 of \cite{BB5}]
Let $F(\x,\y)= \sum_{\alpha\in\NN^{m}} P_{\alpha}(\x)\y^{\alpha}$ be a
power series in $\CC[\x][[\y]]$ (so that each $P_{\alpha}\in\CC[\x]$).
Then $F(\x,\y)$ is in $\overline{\Stab[\x,\y]}$ if and only if
for all $\beta\in\NN^{m},$
$$
\sum_{\alpha\leq\beta}(\beta)_{\alpha}P_{\alpha}(\x)\y^{\alpha}
$$
is stable in $\Stab[\x,\y]$.
\end{theorem}
(This implies the analogous result for real stability, since
$\StabR[\x]=\Stab[\x]\cap\RR[\x]$.)

\begin{exercise}
Derive Theorem 5.4 from Theorems 5.2 and 5.5.  (Hint:\ 
$T((\x+\y)^\kappa)$ is stable if and only if $T((\one-\x\y)^\kappa)$
is stable.)
\end{exercise}

One direction of Theorem 5.5 is relatively straightforward.

\begin{lemma}[Lemma 5.2 of \cite{BB5}]
Fix $\beta\in\NN^{m}$.  The linear transformation $T:\y^{\alpha}\mapsto
(\beta)_{\alpha}\y^{\alpha}$ on $\CC[\y]$ preserves stability.
\end{lemma}
\begin{proof}
By Theorem 5.2 and Exercise 5.3(a), it suffices to show that for
all $\kappa\in\NN^{m}$, the polynomial $T((\y+\u)^{\kappa})$
is stable.  Now
$$
T((\y+\u)^{\kappa}) = \prod_{i=1}^{m}
\left[
\sum_{j=0}^{\kappa(i)} j! \binom{\kappa(i)}{j}\binom{\beta(i)}{j} 
y_{i}^{j}u_{i}^{\kappa(i)-j}
\right],
$$
so it suffices to show that for all $k,b\in\NN$, the polynomial
$f(t) = \sum_{j=0}^{k} j! \binom{k}{j}\binom{b}{j} t^{j}$
is real stable.  Let $g(t) = (1+d/dt)^{k} t^{b}$. 
One can check that $f(t) = t^{b} g(1/t)$.  It thus suffices to show
that $1+d/dt$ preserves stability.  For any $a\in\NN$,
$(1+d/dt)(t+u)^{a} = (t+u+a)(t+u)^{a-1}$ is stable, and so Theorem 5.2
implies the result.
\end{proof}

Now, let $F=F(\x,\y)$ be as in the statement of Theorem 5.5, and let
$(F_{n}:\ n\in\NN)$ be a sequence of stable polynomials
$F_{n}(\x,\y)= \sum_{\alpha\in\NN^{m}} P_{n,\alpha}(\x)\y^{\alpha}$ 
in $\Stab[\x,\y]$ converging to $F$ uniformly on compact sets.
Fix $\beta\in\NN$ and define a linear transformation
$T:\CC[\x,\y] \goesto\CC[\x,\y]$ by $T(\x^{\gamma}\y^{\alpha})
= (\beta)_{\alpha}  \x^{\gamma}\y^{\alpha}$ and linear extension.
By Lemma 5.7 and Exercise 5.3, $T$ preserves stability in 
$\Stab[\x,\y]$.  Thus, $(T(F_{n}):\ n\in\NN)$ is a sequence of stable
polynomials converging to $T(F)$.  Since $T(F)$ is a 
polynomial the convergence is uniform on compact sets, and so
Hurwitz's Theorem implies that $T(F)$ is stable.

The converse direction of Theorem 5.5 is considerably more technical,
although the idea is simple.  With $F$ as in the theorem, for each 
$n\geq 1$ let
$$
F_{n}(\x,\y) = \sum_{\alpha \leq n\one}
(n\one)_{\alpha}P_{\alpha}(\x)\frac{\y^{\alpha}}{n^{\alpha}}.
$$
The sequence $(F_{n}:\ n\geq 1)$ converges to $F$,
since for each $\alpha\in\NN^m$,
$n^{-\alpha}(n\one)_\alpha \goesto 1$ as $n\goesto\infty$.
Each $F_{n}$ is stable, by hypothesis (and scaling).  The hard
work is involved with showing that the convergence is uniform on
compact sets.  To do this, Borcea and Br\"and\'en develop a very
flexible multivariate generalization of the Szasz Principle
\cite[Theorem 5.6]{BB5} -- in itself an impressive accomplishment.
Unfortunately, we have no space here to develop this result -- see
Section 5.2 of \cite{BB5}.


\section{Johnson's Conjectures.}

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
