---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-012-43-convergence-to-the-polarization
section_title: "Convergence to the polarization."
section_number: 4.3
pages: 13-14
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.912
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
Let $0\not\equiv f(x)\in\Stab[x]$ be a univariate stable polynomial of degree
at most $m$:\ say $f(x) = c(x-\xi_1)\cdots(x-\xi_n)$ in which $c\neq 0$,
$n\leq m$, and $\xi_i\not\in\HH$ for all $i\in[n]$.  Then the polynomial
$F_0\in\CC[\x]$ defined by
$$
F_0(x_1,...,x_m)=c(x_1-\xi_1)\cdots(x_n-\xi_n)
$$
is multiaffine and stable, and $F_0(x,...,x)=f(x)$.
Let $\Sigma=(\{i_k,j_k\}:\ k\in\NN)$ be a sequence of two-element subsets of
$[m]$, and for each $k\in\NN$ let $T_k = T_{i_k j_k}^{(1/2)}$ and define
$F_{k+1} = T_k(F_k)$.  By induction using Lemma 4.3, each
$F_k\in\Stab[\x]^\ma$ is multiaffine and stable, and
$F_k(x,...,x)=f(x)$ for all $k\in\NN$.  We will construct such
a sequence $\Sigma$ for which $(F_k:\ k\in\NN)$ converges to $\Pol_m f$.

Let $P\in\CC[\x]^\ma$ be multiaffine, say $P(\x)=\sum_{S\subseteq[m]} c(S)\x^S$.
For $\{i,j\}\subseteq [m]$ let
$$
\omega_{ij}(P) = \sum_{S\subseteq[m]} |c(S)-c(\tau_{ij}(S))|
$$
be the \emph{$ij$-th imbalance} of $P$, and let
$||P||=\sum_{\{i,j\}\subseteq[m]} \omega_{ij}(P)$
be the \emph{total imbalance} of $P$.

\begin{exercise}
\textup{(a)}\
Let $(P_k:\ k\in\NN)$ be polynomials in $\CC[\x]^\ma$  for which
there is a $p\in\CC[x]$ such that $P_k(x,...,x)=p(x)$ for all $k\in\NN$.
If $||P_k||\goesto 0$ as $k\goesto 0$, then $(P_k:\ k\in\NN)$ converges to
a limit $P\in\CC[\x]^\ma$, and $||P||=0$.\\
\textup{(b)}\
For $P\in\CC[\x]^\ma$, $||P||=0$ if and only if $P$ is invariant under
all permutations of $[m]$.  Thus, in part (a) the limit is $P=\Pol_m p$.
\end{exercise}

\begin{exercise}
Let $P\in\CC[\x]^\ma$, let $\{i,j\}\subseteq [m]$, and let $Q=T_{ij}^{(1/2)}
P$.\\
\textup{(a)}\ Then $\omega_{ij}(Q)=0$.\\
\textup{(b)}\ If $h\in[m]\drop\{i,j\}$ then
$\omega_{hi}(Q)\leq (\omega_{hi}(P)+\omega_{hj}(P))/2$,
and similarly for $\omega_{hj}(Q)$.\\
\textup{(c)}\ If $\{h,k\}\subseteq[m]\drop\{i,j\}$ then
$\omega_{hk}(Q)=\omega_{hk}(P)$.\\
\textup{(d)}\ Consequently, $||Q|| \leq ||P|| - \omega_{ij}(P).$
\end{exercise}

Now we choose the sequence $\Sigma=(\{i_k,j_k\}:\ k\in\NN)$ as follows:\
for each $k\in\NN$, $\{i_k,j_k\}\subseteq[m]$ is any pair of indices
$\{i,j\}$ for which $\omega_{ij}(F_k)$ attains its maximum value.  Then
$\omega_{i_k j_k}(F_k)\geq\binom{m}{2}^{-1}||F_{k}||$, so that by
Exercise 4.6(d) and induction on $k\in\NN$,
$$
||F_{k+1}||\leq \left(1-\binom{m}{2}^{-1}\right)||F_k||
\leq \left(1-\binom{m}{2}^{-1}\right)^{k+1} ||F_0||.
$$
Thus, by Exercise 4.5, $F_k$ converges to $\Pol_m f$,
the $m$-th polarization of $f$.  Finally, since each $F_k$ is stable 
(and the limit is a polynomial),  Hurwitz's Theorem implies that $\Pol_m f$
is stable.  This completes the proof of Lemma 4.2, and hence of 
Theorem 4.1.
