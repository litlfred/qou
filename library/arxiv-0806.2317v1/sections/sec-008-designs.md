---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces"
section_id: sec-008-designs
section_title: "Designs"
section_number: null
pages: 23-27
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.897
latex_coverage_ratio: 0.984
doc_brief: "Bounds for codes and designs in complex subspaces — We introduce the concepts of complex Grassmannian codes and designs."
---
\label{sec:designs}

In this section, we introduce the concept of a \defn{complex Grassmannian $2$-design}. We give lower bounds for the size of a $t$-design and indicate the relationship between designs and codes.

Recall that $H_t(m,n)$ is the direct sum of the irreducible representations $H_\mu$ of $U(n)$ containing the zonal polynomials $Z_{\mu,a}$, where $\mu$ is an integer partition of size at most $t$ and length at most $m$. $H_t(m,n)$ may also be thought of as the symmetric polynomials of degree at most $t$ in the principle angles of pairs of subspaces in $\gras{m}{n}$. Since the zonal orthogonal polynomials $Z_{\mu,a}$ (with $\abs{\mu} \leq t$ and $\len(\mu) \leq m$) span $H_t(m,n)$ and are contained in $\Hom_t(n)$, it follows that $H_t(m,n)$ is a subspace of $\Hom_t(n)$. 

We call a finite subset $S \sbs \gras{m}{n}$ a \defn{$t$-design} if, for every polynomial $f$ in $H_t(m,n)$, 
\[
\frac{1}{|S|}\sum_{a \in S} f(a) = \int_{\gras{m}{n}} f(c) \; dc.
\]
In other words, the average of $f$ over $S$ is the same as the average of $f$ over the entire Grassmannian space. Recall that the average of $f$ over $\gras{m}{n}$ can be written as $\ip{1}{f}$: with this in mind we define an inner product for functions on $S$ as follows:
\[
\ip{f}{g}_S := \frac{1}{|S|} \sum_{a \in S} \conj{f(a)}g(a).
\]
Then $S$ is a $t$-design if $\ip{1}{f} = \ip{1}{f}_S$ for every $f \in H_t(m,n)$.
Equivalently, the zonal orthogonal polynomials $Z_{\mu,a}$ span $H_\mu$, so $S$ is a $t$-design if every $Z_{\mu,a}$ has the same averages over $S$ and $\gras{m}{n}$, where $\mu$ is a partition of at most $t$ into at most $m$ parts.

By way of example, consider Theorem \ref{thm:relcodebnd}. If $f = \sum_{\mu}c_{\mu} g_{\mu}$ and $c_{\mu} > 0$ for every $\abs{\mu} \leq t$, then equality in Theorem \ref{thm:relcodebnd} implies that $S$ is a $t$-design. 

For the purposes of quantum tomography applications, $1$- and $2$-designs play a special role (see \cite{grr}, as well as \cite{sco}). In those cases, there is a more explicit description of a $t$-design. 

\begin{lemma}
\label{lem:equivdes}
Let $S$ be a finite subset of $\gras{m}{n}$. Then $S$ is a $1$-design if and only if
\[
\frac{1}{|S|} \sum_{a\in S} P_a = \int_{\gras{m}{n}} P_a \; da = \frac{m}{n}I.
\]
Moreover, $S$ is a $2$-design if and only if 
\begin{equation}
\label{eqn:tswap}
\frac{1}{|S|} \sum_{a\in S} P_a \otimes P_a = \int_{\gras{m}{n}} P_a \otimes P_a \; da.
\end{equation}
\end{lemma}

Before proving Lemma \ref{lem:equivdes}, we note the integral on the RHS of equation \eqref{eqn:tswap} can be evaluated explicitly. Writing $P_a = \sum_{i=1}^m a_ia_i^*$ for some orthonormal basis $\{a_i\}$ of $a$, and letting $T$ denote the ``swap" operator $T: e_i \otimes e_j \mapsto e_j \otimes e_i$, the integral is obtained from Lemma 5.3 of \cite{rs1}:
\[
\int_{\gras{m}{n}} P_a \otimes P_a \; da = \frac{m}{n(n^2-1)}\left[(nm-1)I + (n-m)T\right]. 
\]

\begin{proof}
We prove the lemma by showing that $H_t = \Hom_t$ for $t \in \{1,2\}$; the result then follows by considering the polynomials of the form $a \mapsto (P_a)_{ij}$ in $\Hom_1$ and $a \mapsto (P_a)_{ij}(P_a)_{kl}$ in $\Hom_2$.

Recall that $H_t$ is contained in $\Hom_t$, so it suffices to show that the dimensions of the spaces are equal. When $t = 1$, we have $\dim(H_1) = \dim(\Hom_1) = n^2$, so $H_1 = \Hom_1$. When $t = 2$, recall that $\dim(H_2) = \binom{n^2}{2}$ (assuming $m > 1$), and the space of homogeneous degree-$2$ polynomials on the coordinates of $n \times n$ matrices has dimension $\binom{n^2+1}{2}$. However, $\Hom_2$ is the space of degree-$2$ polynomials on projection matrices, not general matrices. If $P_a$ is a projection matrix, then the degree-$2$ polynomial
\[
P_a \mapsto m\tr(AP_a^2) - \tr(P_a)\tr(AP_a)
\]
is identically zero for every $A$. There are $n^2$ linearly independent polynomials of that form for general $n \times n$ matrices; therefore,
\[
\dim(\Hom_2) = \binom{n^2+1}{2} - n^2 = \binom{n^2}{2}.
\]
Thus $H_2 = \Hom_2$. \qed
\end{proof}

We now consider bounds for $t$-designs. The following is the \defn{absolute bound}.

\begin{lemma}
If $S$ is a $t$-design, then
\[
|S| \geq \dim(H_{\floor{t/2}}(m,n)).
\]
\end{lemma}

\begin{proof}
Let $\{e_1,\ldots,e_N\}$ be an orthonormal basis for $H_{\floor{t/2}}$. Since $e_i$ is a symmetric polynomial in the eigenvalues, so is $\conj{e_i}e_j$. It follows from the unique decomposition of $L^2(\gras{m}{n})$ that $\conj{e_i}e_j$ is in $H_{2\floor{t/2}}$ and therefore in $H_t$. If $S$ is a $t$-design, and $\conj{e_i}e_j$ is in $H_t$, then
\[
\ip{e_i}{e_j} = \ip{1}{\conj{e_i}e_j} = \ip{1}{\conj{e_i}e_j}_S = \ip{e_i}{e_j}_S,
\]
whence it follows that $\{e_1,\ldots,e_l\}$ are orthogonal as functions of $S$ (a space of dimension $|S|$). \qed
\end{proof}

If equality holds, then the basis for $H_{t/2}(m,n)$ is also a basis for the functions on $S$. There is also a \defn{relative bound}.

\begin{theorem}
\label{thm:reldesbnd}
Let $f(x_1,\ldots,x_m) \in \re[x]$ be a symmetric polynomial such that $f = \sum_{\mu}c_{\mu} Z_{\mu}$, where $Z_{\mu}$ is a zonal polynomial for the Grassmanian space, and $c_0 > 0$. Furthermore, suppose $S$ is a $t$-design such that $f_a(b) = f(y_1(a,b),\ldots,y_m(a,b)) \geq 0$ for every $a \neq b$ in $S$, and $c_\mu \leq 0$ for every $\abs{\mu} > t$. Then
\[
|S| \geq \frac{f(1,\ldots,1)}{c_0}.
\]
\end{theorem}

\begin{proof}
Let $f_a$ be the zonal polynomial of $f$ at $a$, so that 
$f_a(b) \geq 0$ for $b \neq a$. Summing over all $b \in S$,
\[
|S|\ip{1}{f_a}_S \geq f_a(a) = f(1,\ldots,1).
\]
Again averaging over all $a \in S$,
\begin{align*}
f(1,\ldots,1) & \leq \sum_{a \in S} \ip{1}{f_a}_S \\
& = \sum_{a \in S} \sum_\mu c_\mu \ip{1}{Z_{\mu,a}}_S \\
& = \sum_\mu c_\mu \sum_{a \in S} \ip{1}{Z_{\mu,a}}_S.
\end{align*}
Since $S$ is a $t$-design, the inner sum is zero for $\abs{\mu} \leq t$ ($\mu \neq 0$). For $\abs{\mu} > t$, the inner sum is nonnegative (by Lemma \ref{lem:possum}) and $c_\mu \leq 0$. Therefore,
\begin{align*}
f(1) & \leq c_0 \sum_{a \in S} \ip{1}{Z_{0,a}}_S \\
& = c_0 |S|. \eqed
\end{align*} 
\end{proof}

If equality holds, then we have $f(a,b) = 0$ for every $a \neq b$ in $S$. That is, $S$ is an $f$-code. Furthermore, for every $\abs{\mu} > t$, we have either $c_\mu = 0$ or $\sum_{a \in S} Z_{\mu,a} = 0$.

As with classical codes and designs, the case where $S$ is both a $f$-code and a $t$-design is of particular interest, as the size of the set can be determined exactly. Combining Theorems \ref{thm:relcodebnd} and \ref{thm:reldesbnd} gives the following.

\begin{theorem}
\label{thm:absdescode}
Suppose $S$ is an $f$-code for $f = \sum_\mu c_\mu Z_\mu$, where $c_\mu \geq 0$, and $S$ is also a $t$-design for $t \geq \deg(f)$. Then
\[
|S| = \frac{f(1,1,\ldots,1)}{c_0}.
\]
\end{theorem}

Consider the following polynomial in $H_t(m,n)$: 
\[
Z_t := \sum_{\substack{\abs{\mu} \leq t \\ \len(\mu) \leq m}} Z_\mu.
\]
This polynomial satisfies $\ip{Z_{t,a}}{f} = f(a)$ for every $f \in H_t(m,n)$. Taking $f = Z_t$ in Theorem \ref{thm:absdescode}, we get:

\begin{corollary}
If $S$ is a $Z_t$-code and a $2t$-design, then 
\[
|S| = \dim(H_t(m,n)).
\] 
\end{corollary}

\begin{theorem}
\label{thm:twothree}
Any two of the following imply the third:
\begin{itemize}
\item $S$ is an $f$-code, where $\deg(f) = t$;

\item $S$ is a $2t$-design;
\item $|S| = \dim(H_t(m,n))$.
\end{itemize}
\end{theorem}

\begin{proof}
Suppose $S$ is a $f$-code with $|S| = \dim(H_t)$. Since equality holds in Corollary \ref{cor:abscodebnd}, the polynomials $f_a$ are a basis for $H_t$. However, we have
\[
\ip{Z_{t,a}}{f_b} = f_b(a) = \begin{cases}
0, & b \neq a; \\
f(1,1,\ldots,1), & b = a. \\
                             \end{cases}
\]
Thus $\{Z_{t,a}\}$ is a dual basis for $H_t$ and each $Z_{t,a}$ is a multiple of $f_{t,a}$. Now consider the averages $\ip{Z_{t,a}}{f_b}_S$: since $f_a(b) = Z_{t,a}(b) = 0$ for $b \neq a$, we get
\[
\ip{Z_{t,a}}{f_b}_S = \begin{cases}
0, & b \neq a; \\
f(1,1,\ldots,1), & b = a. \\
                             \end{cases}
\]
Thus we have
\[
\ip{1}{Z_{t,a}f_b}_S = \ip{\conj{Z_{t,a}}}{f_b}_S = \ip{\conj{Z_{t,a}}}{f_b} = \ip{1}{Z_{t,a}f_b}
\]
for the bases $\{Z_{t,a}\}$ and $\{f_b\}$. But the set $\{Z_{t,a}f_b\}$ spans $H_{2t}(n)$, so $S$ is a $2t$-design. 

Conversely, suppose $S$ is a $2t$-design with $|S| = \dim(H_t)$, and let $f$ annihilate of the angle set of $A$. Since $H_t$ spans the functions on $|S|$, each $f_a$ is in $H_t$ and is therefore a polynomial of degree $t$. Thus $f$ has degree $t$. \qed
\end{proof}

The simplest case of Theorem \ref{thm:twothree} is when $t = 1$: in this case, $S$ is a $1$-distance set and a $2$-design of size $n^2$. Moreover, $S$ is a $Z_1$-code, and $Z_1$ is the annihilator of $\tfrac{m(mn-1)}{n^2-1}$. Thus the inner product between every two distinct subspaces is $\al = \tfrac{m(mn-1)}{n^2-1}$.

\begin{comment}
If Theorem \ref{thm:twothree} holds, then the annihilator of $S$ is simply $Z_k$, and so $Z_k$ has the form of an annihilator
\[
Z_{k,a}(b) = \prod_{i=1}^k (\tr(P_aP_b) - \al_i).
\]
In the case for $k=1$, where we have
\[
Z_{1,a}(b) = \frac{n(n^2-1}{m(n-m)}\Big[\tr(P_aP_b)- \frac{m(mn-1)}{n^2-1}\Big],
\]
so $Z_1$ is the annihilator of $\al = \tfrac{m(mn-1)}{n^2-1}$. For $k = 2$, we have
\begin{align*}
Z_k(y) & = Z_0(y) + Z_1(y) + Z_2(y) + Z_{1,1}(y) \\
& =  \frac{n^2(n^2-1)(n+2)(n+3)}{4(n-m+1)(n-m)}X^*_2 + \frac{n^2(n^2-1)(n-2)(n-3)}{4(n-m)(n-m-1)}X^*_{1,1} \\ 
& \qquad + \frac{n(n^2-1)(m^2n^2-mn^3+4mn-n^2+m^2-1)}{(n-m)(n-m+1)(n-m-1)}X^*_1 \\
& \qquad + \frac{n(n^2-1)(m^3n-m^2n^2+mn+2m^2-2)}{2(n-m)(n-m+1)(n-m-1)}.
\end{align*}
{\bf Here we are assuming the correct normalizations.} If $Z_2$ is an annihilator, say of $\al$ and $\be$, then
\begin{align*}
Z_2(y) & = c(\sum_i y_i - \al)(\sum_i y_i - \be) \\
& = c\big[(\sum_i y_i^2 + \sum_{i<j}y_iy_j) + \sum_{i<j}y_iy_j - (\al+\be)\sum_i y_i + \al\be\big] \\
& = c\big[{m+1 \choose 2}X_2^* + {m \choose 2}X_{1,1}^* - m(\al+\be)X_1^* + \al\be\big].
\end{align*}
Two equations for $Z_2$ can be equal only if ratios of the coefficients of $X_2^*$ and $X_{1,1}^*$ are the same:
\[
\frac{{m+1 \choose 2}}{ {m \choose 2}} = \frac{\frac{n^2(n^2-1)(n+2)(n+3)}{4(n-m)(n-m+1)}}{\frac{n^2(n^2-1)(n-2)(n-3)}{4(n-m)(n-m-1)}},
\]
which simplifies to 
\[
n^2 - 5mn + 5m^2+1 = 0.
\]
for $n \neq 0$. The last equation is satisfied only for certain particular integer values such as $(n,m) = (7,2),(18,5),(47,13)$. 
\end{comment}
