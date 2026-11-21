---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05"
section_id: sec-010-44-example-graphs-on-perfect-matchings
section_title: "Example: Graphs on Perfect Matchings"
section_number: 4.4
pages: 25-27
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 1.0
doc_brief: "Stein’s Method and Random Character Ratios Running head: Stein’s Method and Random Character Ratios Version of 8/13/05 — Stein’s method is used to prove limit theorems for random character ratios."
---
\label{matching}

	In this example $G=S_{2n}$ and $K$ is the hyperoctahedral
	group of signed permutations on $n$ symbols, of size $2^n
	n!$. This Gelfand pair is discussed at length in Chapter 7 of
	\cite{Mac} and in Section 3 of \cite{HSS}, to which we refer
	the reader for proofs of facts in the next two
	paragraphs. Another useful reference is \cite{DHol}.

	The induced representation $1_K^G$ decomposes as
	$\oplus_{|\lambda|=n} V_{\lambda}$, where $\lambda$ ranges
	over all partitions of size $n$. An explicit formula for the
	numbers $d_{\lambda}$ appears in \cite{Mac} and is not needed
	in what follows. However it is worth remarking that the Plancherel measure of
	$(G,K)$, which chooses $\lambda$ with probability $\frac{2^n
	n!  d_{\lambda}}{(2n)!}$, is the $\alpha=2$ case of the so
	called Jack$_{\alpha}$ measure on partitions, which chooses
	$\lambda$ with probability \[ \frac{\alpha^n n!}{\prod_{s \in
	\lambda} (\alpha a(s) + l(s)+1) (\alpha a(s) + l(s) +
	\alpha)} \] where the product is over all boxes of the
	partition. Here $a(s)$ is the number of boxes in the same row
	of $s$ and to the right of $s$ (the ``arm'' of $s$), and
	$l(s)$ is the number of boxes in the same column of $s$ and
	below $s$ (the ``leg'' of $s$). For example the partition of 5
	below \[
\begin{array}{c c c} \framebox{}& \framebox{}& \framebox{} \\
\framebox{}& \framebox{}& \end{array} \] would have Jack$_{\alpha}$
measure \[ \frac{60 \alpha^2}{(2 \alpha+2)(3 \alpha+1) (\alpha+2)(2
\alpha+1)(\alpha+1)}.\] The Jack measure on partitions is of
interest to researchers in random matrix theory \cite{BO1},\cite{O2},
\cite{K2}.

	The double cosets $K_{\mu}$ of $K$ in $G$ are parameterized by
	partitions $\mu$ of size $n$ and have the following concrete
	description. A perfect matching of $\{1,\cdots,2n\}$ can be
	regarded as a 1-regular graph with vertex set
	$\{1,\cdots,2n\}$. Let $\epsilon$ be the ``identity matching''
	in which $i$ is adjacent to $n+i$ for $1 \leq i \leq n$. Given
	a permutation $w$ in $S_{2n}$, let $\delta(w)$ be the perfect
	matching of $\{1,\cdots,2n\}$ in which $i$ is adjacent to $j$
	if and only $|w(i)-w(j)|=n$. For example,
	$\delta(id)=\epsilon$. Note that the union $\delta_1 \cup
	\delta_2$ of two 1-regular graphs is a 2-regular graph, and
	thus a disjoint union of even length cycles. Let
	$\Lambda(\delta_1,\delta_2)$ be the partition whose parts are
	half the cycle lengths of $\delta_1 \cup \delta_2$. Then
	$Kw_1K = Kw_2 K$ if and only if $\Lambda(\epsilon,\delta(w_1))
	= \Lambda(\epsilon,\delta(w_2))$. Thus $Kw^{-1}K = KwK$ for
	all $w$, so that the machinery of Subsection \ref{gelfandCLT}
	is applicable. One also has that $Kw_1=Kw_2$ if and only if
	$\delta(w_1)=\delta(w_2)$. It follows that $G/K$ is in
	bijection with the perfect matchings of $\{1,\cdots,2n\}$ and
	that $\frac{|K_{\mu}|}{|K|}$ is equal to the number of perfect
	matchings $\delta$ with $\Lambda(\epsilon,\delta)=\mu$, which
	by elementary counting is $\frac{2^n n!}{2^{l(\mu)} \prod_j
	m_j(\mu)! j^{m_j(\mu)}}$ where $l(\mu)$ is the number of parts
	of $\mu$ and $m_j(\mu)$ is the number of parts of $\mu$ of size $j$.

	The main purpose of this subsection is to prove a central
	limit theorem for the random variable $W = \sqrt{2^{i-1} {n
	\choose i} (i-1)!}  \omega_{\lambda}(g_{(i,1^{n-i})})$, where
	$i$ is fixed and $\lambda$ is chosen from the Plancherel
	measure of $(G,K)$. Then Lemma \ref{specgelfand} gives a
	central limit theorem for the spectrum of random walk on the
	graph $H_{(i,1^{n-i})}$, whose vertices are the perfect
	matchings of $\{1,\cdots,2n\}$, with an edge between matchings
	$\delta_1$ and $\delta_2$ if and only if
	$\Lambda(\delta_1,\delta_2) = (i,1^{n-i})$. In the case $i=2$,
	the spectrum of this graph was determined in \cite{DHol}, and
	was shown to be asymptotically normal in \cite{F2} (with error
	term $O(n^{-1/4})$) and then in \cite{CF}, \cite{F3} (with
	error term $O(n^{-1/2})$). But the arguments in those papers
	used different information, and it was not clear that
	they could be pushed through to larger $i$. Theorem \ref{main2}
	will be used to deduce a central limit theorem for any fixed
	$i$ with error term $O(n^{-1/4})$.

	To apply Theorem \ref{main2}, $\omega_t$ will be taken to be
	the spherical function $\omega_{(n-1,1)}$. An explicit formula
	for $\omega_{(n-1,1)}$ is available.

	\begin{lemma} \label{valspher} (\cite{Mac}, p. 411) Let
	$m_1(\mu)$ denote the number of parts of size 1 of $\mu$. Then
	\[ \omega_{(n-1,1)}(g_{\mu}) =
	\frac{(2n-1)m_1(\mu)-n}{2n(n-1)} \] for all $\mu$ of size
	$n$. \end{lemma}

	Lemma \ref{con} is helpful.

	\begin{lemma} \label{con} (\cite{HSS}, Lemma 3.2) The
	coefficient of $K_{\mu}$ in $K_{\tau} K_{(i,1^{n-i})}$ is
	equal to $\frac{|K|^2}{|K_{\mu}|}$ multiplied by the number of
	pairs of perfect matchings $(\delta,\gamma)$ such that
	$\Lambda(\epsilon,\delta) = (i,1^{n-i})$,
	$\Lambda(\delta,\gamma)=\tau$, and
	$\Lambda(\epsilon,\gamma) = \mu$.  \end{lemma}

	The final combinatorial ingredient is an analog of Lemma \ref{term1}.

	\begin{lemma} \label{term1GP} Consider the random walk on $G$
	generated by $K_{(i,1^{n-i})}$. Then for $i$ fixed and $n \geq
	2i$, $\frac{p_2(K_{\mu})^2 |K|}{|K_{\mu}|}$ is equal to
	\begin{enumerate}
\item $\frac{i^2}{4^{i-1}} n^{-2i} + O(n^{-2i-1})$ if $K_{\mu}=K_{(1^n)}=K$.
\item $\frac{2i^2}{4^{i-1}} n^{-2i} + O(n^{-2i-1})$ if $K_{\mu}=K_{(i,i,1^{n-2i})}$.
\item $O(n^{-2i-1})$ otherwise.
\end{enumerate} 
\end{lemma}

\begin{proof} Lemma \ref{con} implies that $\frac{p_2(K_{\mu}) |K_{(i,1^{n-i})}|^2}{|K|^2}$
is equal to the number of pairs of matchings $(\delta,\gamma)$ such
that $\Lambda(\epsilon,\delta) = (i,1^{n-i})$,
$\Lambda(\delta,\gamma)=(i,1^{n-i})$, and $\Lambda(\epsilon,\gamma) = \mu$.

For the first assertion, it follows either from the previous paragraph
or from Lemmas \ref{fourier} and \ref{orthog2} that $p_2(K) =
\frac{1}{2^{i-1} {n \choose i} (i-1)!}$. For the second assertion, it
is straightforward from the previous paragraph that
$p_2(K_{(i,i,1^{n-2i})}) = 1 + O(n^{-1})$. Then use the formula for
$\frac{|K_{\mu}|}{|K|}$ given earlier in this subsection.

For the third assertion, there are two cases. The first case is that
$\mu$ has $n-2i$ parts of size 1, but is not equal to
$(i,i,1^{n-2i})$. Then $p_2(K_{\mu})=O(n^{-1})$ and the formula for
$\frac{|K|}{|K_{\mu}|}$ shows it to be at most $c_i n^{-2i}$ where
$c_i$ is a constant depending on $i$. So in the first case, the result
is proved. The second case is that $\mu$ has $n-2i+r$ parts of size 1,
where $1 \leq r < 2i$. From the first paragraph of the proof, it is
straightforward to see that $p_2(K_{\mu})=O(n^{-r})$. Also the formula
for $\frac{|K|}{|K_{\mu}|}$ shows it to be $O(n^{r-2i})$, proving the
result. \end{proof}

	Combining the ingredients, one deduces the following result.

\begin{theorem} \label{CLTgel} Choose $\lambda$ from the Plancherel
 measure of the Gelfand pair $(G,K)$, and define a random variable $W=
 \sqrt{2^{i-1} {n \choose i} (i-1)!}
 \omega_{\lambda}(g_{(i,1^{n-i})})$. Then there is a constant $A_i$
 such that for all real $x_0$, \[ \left| \pp(W \leq x_0) -
 \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{x_0} e^{-\frac{x^2}{2}} dx
 \right| \leq A_i n^{-1/4} .\] \end{theorem}

\begin{proof} One applies Theorem \ref{main2}, choosing $u=(i,1^{n-i})$ and $\omega_t$ to be the spherical
 function $\omega_{(n-1,1)}$. By Lemma \ref{valspher}, $\omega_t$ is
 real valued and $a=\frac{i(2n-1)}{2n(n-1)}$. Observe that
 $\omega_t(g_{\mu})+2a-1$ vanishes if $\mu=(i,i,1^{n-2i})$ and by
 Lemma \ref{valspher} is $O(n^{-1})$ for any other $\mu$ such that
 $p_2(K_{\mu}) \neq 0$, since any such $\mu$ has at least $n-2i$ parts
 of size 1. Thus by Lemma \ref{term1GP}, \[ \sum_{\mu \neq (1^n)} \frac{|K|
 p_2(K_{\mu})^2}{|K_{\mu}|} (\omega_t(g_{\mu}) + 2a -1)^2 =
 O(n^{-2i-3}).\] Since $\frac{|K_u|}{|K|} = 2^{i-1} {n \choose i}
 (i-1)!$, the first error term in Theorem \ref{main2} is at most $A_i'
 n^{-1/2}$, where $A_i'$ is a constant depending on $i$.

	 To bound the second error term in Theorem \ref{main2}, one
 applies Lemma \ref{term1GP} to see that \[ \sum_{\mu}
 \left(8 - \frac{6(1-\omega_t(g_{\mu}))}{a} \right) \frac{|K|
 p_2(K_{\mu})^2}{|K_{\mu}|} = O(n^{-2i-1}).\] Note that cancellation
 occurred for the coefficient of $n^{-2i}$ coming from the terms
 $\mu=(1^n)$ and $\mu=(i,i,1^{n-2i})$. It follows that the second
 error term is at most $A_i'' n^{-1/4}$, where $A_i''$ is another
 constant depending only on $i$. \end{proof}
