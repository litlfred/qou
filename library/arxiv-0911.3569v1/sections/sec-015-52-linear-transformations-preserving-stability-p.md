---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-015-52-linear-transformations-preserving-stability-p
section_title: "Linear transformations preserving stability – polynomial case."
section_number: 5.2
pages: 15-17
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.984
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
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
