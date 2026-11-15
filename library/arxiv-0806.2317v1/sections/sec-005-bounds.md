---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces"
section_id: sec-005-bounds
section_title: "Bounds"
section_number: null
pages: 14-18
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 0.909
doc_brief: "Bounds for codes and designs in complex subspaces — We introduce the concepts of complex Grassmannian codes and designs."
---
\label{sec:bounds}

Recall that an $\scr{A}$-code is a collection $S$ of subspaces in $\gras{m}{n}$ such that $\tr(P_aP_b) \in \scr{A}$ for every $a \neq b$ in $S$. In this section, we find upper bounds on the size of an $\scr{A}$-code in terms of either the cardinality of $\scr{A}$ or its elements. A summary of the results for $\abs{\scr{A}} \leq 2$ is given in Table \ref{tab:codebounds}.

\begin{table}
\renewcommand{\arraystretch}{2.2}
\setlength{\tabcolsep}{10pt}
\begin{center}
\begin{tabular}{|c||c|c|}
\hline
$\scr{A}$ & $\{\al\}$ & $\{\al,\be\}$ \\
\hline
\rule{0pt}{37pt} \parbox{0.7in}{Absolute bound\\} & \raisebox{8pt}{$n^2$} & \raisebox{7pt}{$\qquad \qquad  \quad \; \dbinom{n^2}{2} \qquad (m > 1)$} \\
\hline 
\rule{0pt}{30pt} \parbox{0.7in}{Relative bound} & \raisebox{-2pt}{$\dfrac{n(m-\al)}{m^2-n\al}$} &  \raisebox{1pt}{$\dfrac{n(m-\al)(m-\be)}{m^2\left[\frac{(m+1)^2}{2(n+1)}+\frac{(m-1)^2}{2(n-1)}-(\al+\be) + \frac{n\al\be}{m^2}\right]}$} \\
\rule{0pt}{40pt} \parbox{0.7in}{Relative bound\\conditions} & $\al < \dfrac{m^2}{n}$ & $\al+\be \leq \dfrac{2(m^2n-4m+n)}{n^2-4}$, \\
\rule{0pt}{30pt} & & \raisebox{10pt}{$\al + \be - \dfrac{n\al\be}{m^2} < \dfrac{m^2n-2m+n}{n^2-1}$} \\
\hline
\end{tabular}
\caption{Upper bounds on $|S|$, when $S \sbs \gras{m}{n}$ is an $\scr{A}$-code.}
\label{tab:codebounds}
\end{center}
\end{table}

If $\scr{A} = \{\al_1,\ldots,\al_k\}$, then the \defn{annihilator} of $\scr{A}$ is the function 
\[
\ann_{\scr{A}}(x) := \prod_{i=1}^k (x-\al_i),
\]
The significance of the annihilator is that $\ann_{\scr{A}}(\tr(P_aP_b)) = 0$ for any $a \neq b$ in $S$. More generally, for any polynomial $f$, an \defn{$f$-code} is a collection $S$ of subspaces such that $f(\tr(P_a)) \neq 0$ and $f(\tr(P_aP_b)) = 0$ for every $a \neq b$ in $S$. If $\scr{A}$ is any set of angles and $f$ is the annihilator of $\scr{A}$, then an $\scr{A}$-code is also an $f$-code.

\begin{theorem}
\label{thm:abscodebnd}
If $S \sbs \gras{m}{n}$ is an $\scr{A}$-code, with $|\scr{A}| = k$, then
\[
|S| \leq \dim(\Hom_k(n)) \leq \binom{n^2+k-1}{k}.
\]
\end{theorem}

\begin{proof}
We prove more generally that if $S$ is an $f$-code, with $\deg(f) = k$, then $|S| \leq \dim(\Hom_k(n))$. The result then follows by taking $f$ to be the annihilator of $\scr{A}$. 

Consider the zonal polynomials $f_a(b) := f(\tr(P_aP_b))$, for $a \in S$. Note that $f_a$ is in $\Hom_k(n)$, since $f_a(b)$ is a degree-$k$ polynomial in the entries of $P_b$. Since $f_a(b) = 0$ for every $b \in S$ except $a$, and $f_a(a) \neq 0$, the set $\{f_a: a \in S\}$ is linearly independent. Thus the number of functions $|S|$ is at most the dimension of the space $\Hom_k(n)$. \qed
\end{proof}

\begin{corollary}
\label{cor:abscodebnd1}
Let $S$ be a collection of subspaces in $\gras{m}{n}$ such that $\tr(P_aP_b) = \al$ for all $a \neq b$ in $S$. Then
\[
|S| \leq n^2.
\]
\end{corollary}

\begin{proof}
Use Theorem \ref{thm:abscodebnd} with the degree-$1$ annihilator of $\al$, which induces zonal polynomials in $\Hom_1(n)$. \qed
\end{proof}

Since $f_a(b)$ is also a degree-$k$ symmetric polynomial in the principal angles of $a$ and $b$, it follows that $f_a$ is also in $H_k(m,n)$. Then by the same argument as in Theorem \ref{thm:abscodebnd}, we have 
\begin{corollary}
\label{cor:abscodebnd}
If $S \sbs \gras{m}{n}$ is an $\scr{A}$-code, with $|\scr{A}| = k$, then
\[
|S| \leq \dim(H_k(m,n)).
\]
\end{corollary}

If equality holds, then the functions $f_a$ form a basis for the space. Moreover, the space $H_k(m,n)$ is exactly the space of functions on $S$. 

Theorem \ref{thm:abscodebnd} and Corollary \ref{cor:abscodebnd} are called \defn{absolute bounds} for Grassmannian codes, because the bounds depend only on the number of different inner product values that occur in $S$. When $m = 1$ these bounds reduce to the absolute bounds of Delsarte, Goethals and Seidel \cite[Theorem 6.1]{dgs}. There is also a \defn{relative bound}, which depends on the actual values of the inner products and is sometimes tighter.

\begin{theorem}
\label{thm:relcodebnd}
Let $f(y_1,\ldots,y_m) \in \re[y_1,\ldots,y_m]$ be a symmetric polynomial such that $f = \sum_{\mu}c_{\mu} Z_{\mu}$, where $Z_{\mu}$ is a zonal orthogonal polynomial, and each $c_{\mu} \geq 0$. Further assume that $c_0$ is strictly positive. If $S$ is a set of subspaces in $\gras{m}{n}$ such that $f_a(b) := f(y_1(a,b),\ldots,y_m(a,b))$ is nonpositive for every $a \neq b$ in $S$, then 
\[
|S| \leq \frac{f(1,\ldots,1)}{c_0}.
\]
\end{theorem}

\begin{proof}
Since $f_a(b) \leq 0$ for $b \neq a$, summing over all $b \in S$, we have
\[
\sum_{b \in S} f_a(b) \leq f_a(a) = f(1,\ldots,1).
\]
Then averaging over all $a \in S$,
\begin{align*}
f(1,\ldots,1) & \geq \frac{1}{|S|}\sum_{a,b \in S} f_a(b) \\
& = \frac{1}{|S|} \sum_\mu c_\mu \sum_{a,b \in S} Z_\mu(a,b). 
\end{align*}
By Lemma \ref{lem:possum}, the inner sum is non-negative for $\mu \neq 0$. If $\mu = 0$, then $Z_0(a,b) = 1$ for all $a$ and $b$, and hence,
\begin{align*}
f(1) & \geq \frac{1}{|S|} c_0 \sum_{a,b \in S} 1 \\
& = c_0 |S|. \eqed
\end{align*} 
\end{proof}

Equality holds if and only if $f_a(b) = 0$ for every $a \neq b \in S$ and for each $\mu \neq 0$, we have either $c_\mu = 0$ or $\sum_{a \in S} Z_{\mu,a} = 0$. (We will see in Section \ref{sec:designs} that when $c_\mu > 0$ for all $\abs{\mu} \leq \deg(f)$, this implies that we have a Grassmannian $t$-design.)

By way of example, we consider the case of an $\{\al\}$-code in detail.

\begin{corollary}
\label{cor:onebound}
Let $S$ be a subset of $\gras{m}{n}$ such that $\tr(P_aP_b) = \al$ for all $a \neq b$ in $S$, and $\al < m^2/n$. Then
\[
|S| \leq \frac{n(m-\al)}{m^2-n\al}.
\]
\end{corollary}

\begin{proof}
The first two zonal orthogonal polynomials are $Z_0(y) = 1$ and (up to normalization) $Z_1(y) = \sum_{i=1}^my_i - m^2/n$. The annihilator for $\al$ is the polynomial $f(x) = x - \al$, which induces the zonal polynomial at subspace $a$ given by 
\[
f_{a}(b) = \tr(P_aP_b) - \frac{\al\tr(P_b)}{m} = \sum_{i=1}^m y_i - \al,
\]
for principle angles $y_1,\ldots,y_m$ of $a$ and $b$. Thus we may write
\begin{align*}
f(y_1,\ldots,y_m) & = \sum_{i=1}^m y_i - \al \\
& = c_1Z_{1}(y) + \left(\frac{m^2}{n}-\al\right)Z_{0}(y).
\end{align*}
Applying Theorem \ref{thm:relcodebnd}, we find that
\[
|S| \leq \frac{f(1,\ldots,1)}{c_0} = \frac{m-\al}{m^2/n-\al}. \eqed
\]
\end{proof}
When $m = 1$, we recover Delsarte, Goethals and Seidel's bound for complex equiangular lines: 
\[
|S| \leq \frac{n(1-\al)}{1-n\al}.
\]

Similarly, using the zonal orthogonal polynomials $Z_0,Z_1,Z_{1,1}$ and $Z_2$, we get a bound on the size of a subset containing two inner products, say $\al$ and $\be$.

\begin{corollary}
\label{cor:twobound}
Let $S$ be a subset of $\gras{m}{n}$ such that $\tr(P_aP_b) \in {\al,\be}$ for all $a \neq b$ in $S$. Further assume that
\begin{align*}
\al+\be & \leq \frac{2(m^2n-4m+n)}{n^2-4}, \\
\al + \be - \frac{n\al\be}{m^2} & < \frac{m^2n-2m+n}{n^2-1}.
\end{align*}
Then
\[
|S| \leq \frac{n(m-\al)(m-\be)}{m^2\left[\frac{(m+1)^2}{2(n+1)}+\frac{(m-1)^2}{2(n-1)}-(\al+\be) + \frac{n\al\be}{m^2}\right]}.
\]
\end{corollary}

When $m = 1$ this reduces to the Delsarte, Goethals and Seidel bound of 
\[
|S| \leq \frac{n(n+1)(1-\al)(1-\be)}{2-(n+1)(\al+\be) + n(n+1)\al\be}
\]
for lines in complex projective space $\cx P^{n-1}$.
