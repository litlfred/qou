---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces"
section_id: sec-004-zonal-polynomials
section_title: "Zonal polynomials"
section_number: null
pages: 10-14
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.929
doc_brief: "Bounds for codes and designs in complex subspaces — We introduce the concepts of complex Grassmannian codes and designs."
---
\label{sec:zonal}

A \defn{zonal polynomial} at a point $a \in \gras{m}{n}$ is a function on points $b \in \gras{m}{n}$ which depends only on the the principle angles between $a$ and $b$. Given any univariate polynomial $f(x)$ of degree $k$, we define the \defn{zonal polynomial of $f$ at $b$} as follows: if $f(x) = \sum_{i=0}^k f_i x^i$, then
\[
f_a(b) = \sum_{i=0}^k f_i \tr(P_aP_b)^i.
\]
Here $P_a$ and $P_b$ are the projection matrices for $a$ and $b$. As written, the zonal polynomial is not homogeneous, but by embedding the constant $1$ into $\Hom_1(n)$ in the form $\tr(P_b)/m$, the exponents in $f_a(b)$ may be ``pushed up'' and we may assume $f_a$ is in $\Hom_k(n)$. To see that $f_a(b)$ only depends on the principal angles between $a$ and $b$, note that $\tr(P_aP_b)$ is simply the sum of the principal angles. 

There is another set of zonal polynomials that play a particular role in the theory of Delsarte bounds. Let $H_\mu$ be an irreducible representation in $L^2(\gras{m}{n})$. Then for each $a \in \gras{m}{n}$, define the \defn{zonal orthogonal polynomial} $Z_{\mu,a}$ to be the unique element of $H_\mu$ such that for every $p \in H_\mu$,
\[
\ip{Z_{\mu,a}}{p} = p(a).
\]
Then zonal polynomials are invariant under the unitary group, in the following sense:
\[
Z_{\mu,b}(a) = \ip{U^*Z_{\mu,a}}{U^*Z_{\mu,b}} = \ip{Z_{\mu,Ua}}{Z_{\mu,Ub}} = Z_{\mu,Ub}(Ua).
\]
The value of $Z_{\mu,b}(a)$ depends on the $U(n)$-orbit of $(a,b)$ and therefore depends on the principle angles of $a$ and $b$. With this in mind we sometimes write $Z_{\mu,a}(b) = Z_\mu(a,b)$ or $Z_{\mu,a}(b) = Z_\mu(y_1,\ldots,y_m)$, where $(y_1,\ldots,y_m)$ are the principal angles of $a$ and $b$.

Schur orthogonality \cite[Theorem 3.3]{sep} for irreducible representations implies that $Z_{\mu,a}$ and $Z_{\nu,b}$ are orthogonal for $\mu \neq \nu$. So, we have
\[
\ip{Z_{\mu,a}}{Z_{\nu,b}} = \de_{\mu,\nu} Z_{\mu}(a,b). 
\]
Moreover, $Z_{\mu,a}(b) = Z_{\mu,b}(a)$ is in fact real and symmetric in $a$ and $b$. The zonal polynomials satisfy some other important properties, including the following positivity condition:

\begin{lemma}
\label{lem:possum}
For any subset $S \sbs \gras{m}{n}$,
\[
\sum_{a,b \in S} Z_\mu(a,b) \geq 0.
\]
Equality holds only when $\sum_{a \in S} Z_{\mu,a} = 0$.
\end{lemma}

\begin{proof}
We have
\begin{align*}
\sum_{a,b \in S} Z_\mu(a,b) & = \sum_{a,b \in S} \ip{Z_{\mu,a}}{Z_{\mu,b}} \\
& = \ip{\sum_{a \in S} Z_{\mu,a}}{\sum_{b \in S} Z_{\mu,b}} \\
& \geq 0.
\end{align*} 
Equality holds if and only if $\sum_{a \in S} Z_{\mu,a} = 0$. \qed
\end{proof}

The second important condition the zonal polynomials satisfy is called the \defn{addition formula}:

\begin{lemma}
\label{lem:addform}
Let $e_1,\ldots,e_N$ be an orthonormal basis for the irreducible subspace $H_\mu$. Then
\[
\sum_{i=1}^N \conj{e_i(a)}e_i(b) = Z_{\mu}(a,b).
\]
\end{lemma}

\begin{proof}
Since $Z_{\mu,a}$ is in $H_\mu$, we may write it as a linear combination of $e_1,\ldots,e_N$:
\begin{align*}
Z_{\mu,a} & = \sum_{i=1}^N \ip{e_i}{Z_{\mu,a}}e_i \\
& = \sum_i \conj{e_i(a)} e_i.
\end{align*}
So, it follows that $Z_{\mu,a}(b) = \sum_i \conj{e_i(a)} e_i(b)$. \qed
\end{proof}

James and Constantine give an explicit formula for the zonal orthogonal polynomials of $\gras{m}{n}$ in terms of Schur polynomials, the irreducible characters of $SL(m,\cx)$. If $y = (y_1,\ldots,y_m)$ are variables and $\sg = (s_1,\ldots,s_m)$ is a partition into at most $m$ parts, then the (unnormalized) \defn{Schur polynomial} is defined as
\[
X_\sg(y) := \frac{\det(y_i^{s_j+m-j})_{i,j}}{\det(y_i^{k-j})_{i,j}}.
\]
Each Schur polynomial is a symmetric polynomial in $(y_1,\ldots,y_m)$. For more information about Schur polynomials, see Stanley \cite[Chapter 7]{stan}. The \defn{normalized Schur polynomial} $X^*_\sg$ is the multiple of $X_\sg$ such that $X^*_\sg(1,\ldots,1) = 1$.

To define the zonal orthogonal polynomials for $\gras{m}{n}$, first define the \defn{ascending product}
\[
(a)_s := a(a+1)\ldots(a+s-1),
\]
and given a partition $\sg = (s_1,\ldots,s_m)$, define \defn{complex hypergeometric coefficients}
\[
[a]_{\sg} := \prod_{i=1}^m (a-i+1)_{s_i}.
\]
Further assume we have a partial order $\leq$ on partitions defined such that $\nobreak{(s_1,\ldots,s_m) \leq (k_1,\ldots,k_l)}$ if and only if $s_i \leq k_i$ for all $i$. Letting $y+1 := (y_1+1,\ldots,y_m+1)$, the \defn{complex hypergeometric binomial coefficients} $\smallsbinom{\ka}{\sg}$ are given by the formula
\[
X^*_\ka(y+1) = \sum_{\sg \leq \ka} \sbinom{\ka}{\sg}X^*_{\sg}(y).
\]
We can now define the zonal orthogonal polynomials for $\gras{m}{n}$. The following result is due to James and Constantine \cite{jc1}.

\begin{theorem}
Let 
\[
\rho_\sg := \sum_{i=1}^m s_i(s_i-2i+1)
\]
and let $\sg$ and $\ka$ partition $s$ and $k$ respectively. Also let
\[
[c]_{(\ka,\sg)} := \sum_i\frac{\sbinom{\ka}{\sg_i}\sbinom{\sg_i}{\sg}}{(k-s)\sbinom{\ka}{\sg}}\frac{[c]_{(\ka,\sg_i)}}{\left(c + \frac{\rho_\ka - \rho_\sg}{k-s}\right)},
\]
where the summation is over partitions $\sg_i = (s_1,\ldots,s_{i-1},s_i+1,s_{i+1},\ldots)$ that are nonincreasing. Then up to normalization, the zonal orthogonal polynomial for $H_\ka$ is
\[
Z_{\ka}(y) := \sum_{\sg \leq \ka} \frac{(-1)^s \sbinom{\ka}{\sg}[c]_{(\ka,\sg)}}{[a]_\sg}X^*_\sg(y),
\]
where $y = (y_1,\ldots,y_m)$ is the set of principal angles.
\end{theorem}

The first few normalized Schur polynomials are:
\begin{align*}
X^*_0(y) & = 1 \\
X^*_1(y) & = \frac{1}{m}\sum_{i=1}^m y_i \\
X^*_{1,1}(y) & = \frac{1}{\binom{m}{2}} \sum_{i<j} y_iy_j \\
X^*_2(y) & = \frac{1}{\binom{m+1}{2}}\Big(\sum_{i=1}^m y_i^2 + \sum_{i<j}y_iy_j \Big).
\end{align*}
Up to normalization by a constant, the first few zonal orthogonal polynomials are:
\begin{align*}
Z_0(y) & = 1 \\
Z_1(y) & = nX^*_1(y) - m \\
Z_{1,1}(y) & = m(m-1) - 2(n-1)(m-1)X^*_1(y) + (n-1)(n-2)X^*_{1,1}(y) \\
Z_2(y) & = m(m+1) - 2(n+1)(m+1)X^*_1(y) + (n+1)(n+2)X^*_{2}(y).
\end{align*}
The correct normalizations satisfy 
\[
\ip{Z_{\mu,a}}{Z_{\mu,a}} = Z_\mu(1,1,\ldots,1) = \dim H_\mu.
\]
With the exception of the case $\mu = 0$ (which is normalized correctly in the formula above), normalizations for $Z_\mu$ will not play a role in the results which follow.
