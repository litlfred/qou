---
doc_id: arxiv-2111.12409v4
doc_title: "On the generalisation of Roth’s theorem"
section_id: sec-004-2-the-interpolating-polynomial
section_title: "The interpolating polynomial"
section_number: 2
pages: 7-8
source_pdf: 2111.12409v4.pdf
source_sha256: 3f0b94ee06fe79bf
toc_source: outline
text_source: latex
latex_prose_ratio: 0.951
latex_coverage_ratio: 0.96
doc_brief: "On the generalisation of Roth’s theorem — We present two generalisations of Roth’s approximation theorem on proper adelic curves, assuming some technical conditions on the behavior of the logarithmic"
---
\label{aux}

We fix a proper adelic curve $\mathbb X=(\mathbb K,\Omega, \phi)$  and an algebraic closure of $\mathbb K$. In this section we recall the existence of an interpolating polynomial $\delta\in\mathbb K[X_1,\ldots,X_N]$ associated to  some elements $\bm{\alpha}_1,\ldots,\bm{\alpha}_n\in\mathbb K^N$ having some explicit bounds on: the degree, the $\bm{d}$-index at all the $\bm{\alpha}_j$'s and the height. The complete construction of $\delta$ can be found in \cite{C}, and we will recall it in appendix \ref{ap}.

We fix for the whole section the following data: two natural numbers $n,N\ge 2$, and  a vector $\bm{d}=(d_1,\ldots ,d_N)\in(\mathbb R_{>0})^N$.  We say that two vectors  $\bm{\alpha}=(\alpha^{(1)},\ldots,\alpha^{(N)})$, $\bm{\beta}=(\beta^{(1)},\ldots,\beta^{(N)})$  are \emph{componentwise different} if $\alpha^{(j)}\neq\beta^{(j)}$ for  $j=1,\ldots, N$.
\begin{defn}  The \emph{$\bm{d}$-index of $P(X_1,\dots ,X_N)\neq 0$ at $\bm{\alpha}\in\mathbb K^N$} is the real number:
$$
\Ind_{\bm{\alpha},\bm{d}}(P):=\min_{\bm i\in \mathbb N^N}\left\{\sum_{j=1}^{N}\frac{i_j}{d_j}\in\mathbb R\colon \Delta^{\bm i}P(\bm{\alpha})\neq 0\right \}
$$
\end{defn}
Let's fix  $t\in\mathbb R$ such that $0<t<N$, the following two sets will play a central role in the theory:
$$
\sG_t:=\left \{\bm i\in \mathbb N^N\colon i_j\leq d_j\; \forall j=1,\dots ,N,\, {\rm{and}}\sum_{j=1}^{N}\frac{i_j}{d_j}\leq t\right \},
$$
$$
\sC_t:=\left\{(x_1,\dots ,x_N)\in [0,1]^N \colon \sum_{j=1}^{N}x_j \leq t \right \}
$$
The Lebesgue measure of $\sC_t$ will be denoted as $V(t)$, and for simplicity of terminology we will refer to it simply as ``volume''.

\begin{lem}\label{Lemmepagina156}  The cardinality of  $\sG_t$  is asymptotic to $d_1 d_2\ldots d_N V(t)$.
\end{lem}
\begin{proof}See \cite[p. 157]{bogu}.
\end{proof}


Now fix some vectors $\bm{\alpha}_1,\ldots,\bm{\alpha}_n\in\mathbb K^N$ where $\bm{\alpha}_h=(\alpha^{(1)}_h,\ldots,\alpha^{(N)}_h)$ for every $h=1,\ldots, n$ and let  $\bm{X}=(X_1,\ldots,X_N)$ be a vector of variables. For any two multi-indices  $\bm {a}=(a_1,a_2,\dots ,a_N)$ and $\bm {i}=(i_{1},i_{2},\dots ,i_{N})$ of $\mathbb N^{N}$ we use the following notations:
$$
{\bm a\choose \bm i}:={{{a_1}}\choose {i_1}}  {{{a_2}} \choose {i_2}} \ldots {{{a_N}}\choose {i_N}}
$$
$$
\bm{\alpha}_h^{\bm i}:=(\alpha_{h}^{(1)}){^{{i_1}}}  ({\alpha}_{h}^{(2)}){^{{i_2}}}\ldots (\alpha_{h}^{(N)}){^{{i_N}}}
$$
$$
\bm{X}^{\bm i}:=X^{i_1}_1X^{i_2}_2\ldots X^{i_N}_N
$$
with the convention ${{{p}}\choose {q}}=0$ if $0\leq p<q$ for the binomial coefficient. Now, consider $\gamma\in\mathbb R$ such that $0<\gamma<\frac{1}{2nN^2}$; we always assume that $\frac{d_{j+1}}{d_j}\le\gamma$ for any $j=1,\ldots, N-1$ , which means in particular that  $d_j=O(d_1)$ for any $j$. We also put $\eta:=2\gamma n < \frac{1}{N^2}$ and $d:=d_1d_2\ldots d_N$.

We have the following result about the existence of a polynomial $\delta(X_1,\ldots,X_N)\in\mathbb K[X_1,\ldots X_N]$ with some prescribed properties. In the appendix A we will sketch Corvaja's construction of $\delta(X_1,\ldots,X_N)$ adapting it to the case of adelic curves:
\begin{prop}\label{interpolationpoly} Assume that in the adelic curve $\mathbb X$ the condition $h_{\mathbb X}(2)\le \log 2$ is satisfied and assume that the number $\eta\in\mathbb R$ is chosen as explained above.   Let's fix some vectors $\bm{\alpha}_1,\ldots,\bm{\alpha}_n,\bm{\beta}\in\mathbb K^N$ that are pairwise componentwise different.  Moreover let's choose some parameters $s, t_1,\dots, t_n\in\mathbb R$, with $0<s<1$ and $0< t_h<\frac{N}{2}$ for $h=1,\dots ,n$ such that the following condition on volumes is verified:
\begin{equation}\label{basicinequality}
(1+\eta)^N<V(s)+\sum_{h=1}^{n}V(t_h)<1+2N\eta
\end{equation}
Then there exists a polynomial $\delta(X_1,\ldots X_N)\in\mathbb K[X_1,\ldots, X_N]$ satisfying the following properties:
\begin{enumerate}
\item[$(1)$] $\delta(\bm\beta)\neq 0$;
\item[$(2)$] ${\deg}_{X_{j}}\delta\leq dd_jV(s)+O(d)$,  for $1\leq j\leq N$;
\item[$(3)$] ${\rm{Ind}}_{\bm{\alpha}_h,\bm{d}}(\delta)\geq dV(s)\left ( t_h-s-\frac{2N^2\eta}{V(s)} \right)+ O(d^{N-1}_1) $,  for $1\leq h\leq n$;
\item[$(4)$] $\displaystyle h_{\mathbb X}(\delta)\leq d\sum_{j=1}^{N}d_j\left( \log 2+   \sum_{h=1}^{n}V(t_h)h(\alpha^{(j)}_{h})\right)+O(d\log d)$;
\end{enumerate}
\end{prop}
\proof
See \cite[Proposition 2.6]{C}.
\endproof
