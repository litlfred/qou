---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-008-32-linear-transformations-preserving-stability-m
section_title: "Linear transformations preserving stability – multiaffine case."
section_number: 3.2
pages: 10-11
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.974
doc_brief: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS — Univariate polynomials with only real roots – while special – do occur often enough that their properties can lead to interesting"
---
\begin{lemma}[Lieb-Sokal Lemma, Lemma 2.1 of \cite{BB5}]
Let $g(\x)+yf(\x)\in\Stab[\x,y]$ be stable and such that
$\deg_i(f)\leq 1$.  Then $g-\partial_{i}f \in\Stab[\x]$ is stable.
\end{lemma}
\begin{proof}
Since $g$ is stable (by specialization to $y=0$), there is nothing to
prove if $\partial_i f\equiv 0$ identically, so assume otherwise
(and hence that $f\not\equiv 0$).
By permutation we can assume that $i=1$.  Since $f$ is stable and
$z_1,z\in\HH$ imply that $z_1-z^{-1}\in\HH$, it follows that
$$
yf(x_1-y^{-1},x_2,...,x_m)= - \partial_1 f(\x) + yf(\x)
$$
is stable.  Proposition 2.7(b) implies that for all $\z\in\HH^m$,
$$
\Im\left(\frac{g(\z)-\partial_1 f(\z)}{f(\z)}\right) =
\Im\left(\frac{g(\z)}{f(\z)}\right) +
\Im\left(\frac{-\partial_1 f(\z)}{f(\z)}\right) \geq 0.
$$
Thus, by Proposition 2.7(b) again, $g-\partial_1 f + yf$ is stable.
Specializing to $y=0$ shows that $g-\partial_1 f$ is stable.
\end{proof}

\begin{exercise}[Lemma 3.1 of \cite{BB5}]
Let $f\in\CC[\x]^\ma$ and $\w\in\HH^m$.  Then for all $\epsilon>0$
sufficiently small, $(\x+\w)^{[m]}+\epsilon f(\x)$ is stable.
(Here $(\x+\w)^{[m]}=\prod_{i=1}^m(x_i+w_i)$.)
\end{exercise}

For a linear transformation $T:\CC[\x]^{\ma}\goesto\CC[\x]$ of
multiaffine polynomials, define the \emph{algebraic symbol} of $T$ to
be the polynomial
$$
T((\x+\y)^{[m]})
= T\left(\prod_{i=1}^m (x_i+y_i)\right)
= \sum_{S\subseteq[m]} T(\x^{S})\y^{[m]\drop S}
$$
in $\CC[x_{1},\ldots,x_{m},y_{1},\ldots,y_{m}]=\CC[\x,\y]$.

\begin{theorem}[Theorem 1.1 of \cite{BB5}]
Let $T:\CC[\x]^{\ma}\goesto\CC[\x]$ be a linear transformation.
Then $T$ maps $\Stab[\x]^{\ma}$ into $\Stab[\x]$ if and only if 
either\\
\textup{(a)}\ $T(f) = \eta(f)\cdot p$ for some linear functional
$\eta:\CC[\x]^{\ma}\goesto\CC$ and $p\in\Stab[\x]$, or\\
\textup{(b)}\ the polynomial $T((\x+\y)^{[m]})$ is stable in $\Stab[\x,\y]$.
\end{theorem}
\begin{proof}
First, assume (b) that $T((\x+\y)^{[m]})\in\Stab[\x,\y]$ is stable.
By inversion, it follows that $\y^{[m]}T((\x-\y^{-\one})^{[m]})$ is also
stable. Thus, if $f\in\Stab[w_1,...,w_m]$ is stable then
$$
\y^{[m]}T((\x-\y^{-\one})^{[m]})f(\w)
=
\sum_{S\subseteq[m]} T(\x^{S})(-\y)^S f(\w)
$$
is stable.  If $f$ is also multiaffine then repeated application of
the Lieb-Sokal Lemma 3.2 (replacing $y_i$ by $-\partial/\partial w_i$ for
$i\in[m]$) shows that
$$
\sum_{S\subseteq[m]} T(\x^{S})\frac{\del^S}{\del \w^S} f(\w)
$$
is stable.  Finally, specializing to $\w=\zero$ shows that $T(f(\x))$
is stable.  Thus, the linear transformation $T$ maps $\Stab[\x]^\ma$
into $\Stab[\x]$.  This is clearly also the case if (a) holds.

Conversely, assume that $T$ maps $\Stab[\x]^\ma$ into $\Stab[\x]$.
Then for any $\w\in\HH^m$, $(\x+\w)^{[m]}\in\Stab[\x]^\ma$, so that
$T((\x+\w)^{[m]})\in\Stab[\x]$.

First, assume that there is a $\w\in\HH^m$ for which
$T((\x+\w)^{[m]})\equiv 0$ identically.  For any $f\in\CC[\x]^\ma$ let $\epsilon>0$
be as in Exercise 3.3.  Then $\epsilon T(f) = T((\x+\w)^{[m]}+\epsilon f)$
is stable, so that $T(f)$ is stable.  Thus, the image of $\CC[\x]^\ma$ under
$T$ is a $\CC$-subspace of $\Stab[\x]$.  By Proposition 2.12(b), $T$ has the
form of case (a).

Secondly, if $T((\x+\w)^{[m]})\not\equiv 0$ for all $\w\in\HH^m$ then,
since each of these polynomials is in $\Stab[\x]$, we have
$T((\x+\w)^{[m]})|_{\x=\z}\neq 0$ for all $\z\in\HH^m$ and $\w\in\HH^m$.
This shows that $T((\x+\y)^{[m]}))$ is stable in $\Stab[\x,\y]$, which is
the form of case (b).
\end{proof}

Theorem 3.4 has a corresponding real form -- the proof is completely 
analogous.
\begin{theorem}[Theorem 1.2 of \cite{BB5}]
Let $T:\RR[\x]^{\ma}\goesto\RR[\x]$ be a linear transformation.
Then $T$ maps $\StabR[\x]^{\ma}$ into $\StabR[\x]$ if and only if 
either\\
\textup{(a)}\ $T(f) = \eta(f)\cdot p + \xi(f)\cdot q$ for some linear functionals
$\eta,\xi:\RR[\x]^{\ma}\goesto\RR$ and $p,q\in\StabR[\x]$ such that
$p\ll q$, or\\
\textup{(b)}\ the polynomial $T((\x+\y)^{[m]})$ is real stable
in $\StabR[\x,\y]$, or\\
\textup{(c)}\ the polynomial $T((\x-\y)^{[m]})$ is real stable
in $\StabR[\x,\y]$.
\end{theorem}
\begin{proof}
\textbf{Exercise 3.6.}
\end{proof}
