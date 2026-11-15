---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3-manifolds"
section_id: sec-005-covers-and-branched-covers
section_title: "Covers and branched covers"
section_number: null
pages: 6-7
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.986
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
\label{sec:covers}

It is straightforward to see that hyperbolic volume is multiplicative under finite-sheeted covers. The following example shows that the analogous fact is not true for topological volume in general. 

\begin{example}
We show in \cref{sec:computations} that $m009$ (Snappy notation) is the unique minimiser of $\R P^3,$ and hence 
$\volt(\R P^3)=\volh(m009)\approx 2.66674$. One sees this by noting that $\R P^3$ is obtained as a Dehn filling of $m009$ in a unique way, but it is not obtained by filling a cusped hyperbolic 3--manifold of smaller volume. As we saw in \cref{ex:volume-S3}, we have $\volt(S^3)\approx 2.02988$, so 
$$\volt(S^3) < 2\volt(\R P^3).$$
This shows that the topological volume is not multiplicative under finite covers in general. A surgery description of $m009$ is given by performing a $2$-surgery on one component of the Whitehead link $L5a1$ (using notation from the Thistlethwaite link table). The complement of the other link component in this surgery yields $m009$. From this surgery description one can see that the lift to $S^3$ of the minimiser in $\R P^3$  is the complement of $L6a1$ with volume $2 \cdot \volt (\mathbb{R}P^3) \approx 5.33$.
\end{example}

Nonetheless we have the following behaviour of topological volume under finite-sheeted covers. 

\begin{lemma}\label{lem:covers}
Let $X$ and $Y$ be closed, orientable 3--manifolds. If there is a $d$--fold cover $X\to  Y$, then 
\begin{equation}
\label{eq:covering}
\volt(X) \leq  d\cdot \volt(Y).
\end{equation}
\end{lemma}

\begin{proof}
Suppose $X$ and $Y$ are closed, orientable 3--manifolds with $p\co X \to Y$ a $d$--fold cover.
Suppose $L $ in $Y$ is a hyperbolic link. Then $X \setminus p^{-1}(L) \to Y \setminus L$ is a $d$--fold cover and in particular $p^{-1}(L) \subset X$ is a hyperbolic link, with $\volh (X \setminus p^{-1}(L)) =d \cdot  \volh(Y \setminus L)$. A minimiser $L \subset Y$  hence gives 
$\volt(X) \le \volh (X \setminus p^{-1}(L)) =d \cdot  \volh(Y \setminus L) = d \cdot  \volt(Y).$
\end{proof}

\begin{example}
For each $d>0,$ choose $p$ and $q$ such that $d \cdot p$ and $q$ are coprime. Then we have a $d$--fold covering of lens spaces 
$L(p, q) \to L(d\cdot p,q).$
 We show in \cref{prop:lens-space-limit} that for $p$ sufficiently large, $\volt(L(d\cdot p, q))$ and $\volt(L(p, q))$ are arbitrarily close to the volume of the Whitehead link complement. Hence the gap in \Cref{eq:covering} can be arbitrarily large, as $d$ varies.
\end{example}

\begin{question}
If $X\to  Y$ is a $d$--fold cover of non-hyperbolic closed, orientable 3--manifolds, is $\volt(X) <  d\cdot \volt(Y)$, that is, is Inequality~(\ref{eq:covering}) always strict?
\end{question}

As an application of \cref{lem:covers} we observe that knowledge about the topological volume can be leveraged to give bounds on degrees of covers. Recall that a link $L\subset S^3$ is called \emph{universal} if every closed, orientable 3--manifold arises as a cover of $S^3$ branched along $L$. The existence of universal links was first shown by Thurston in unpublished work. By work of Hilden, Lozano, and Montesinos~\cite{HLM2,HLM4,HLM3}, we know that there are numerous universal links, including the figure eight knot, the Whitehead link, and the Borromean rings.

\begin{corollary}
Let $L$ be a hyperbolic universal link in $S^3$ and let $d_L(M)$ denote the minimal degree of a cover $M\rightarrow S^3$ branched along $L$. Then
\begin{align*}
    \volt(M)\leq d_L(M) \volh(L).
\end{align*}
For example, we have
\[
\pushQED{\qed} 
 \volt(M)\leq d_{K4a1}(M) \volh(K4a1)=d_{K4a1}(M)\volt(S^3).\qedhere
\popQED
\]  
\end{corollary}

In particular, we obtain general lower bounds on $d_L(M)$ from the the topological volumes of $S^3$ and $M$. On the other hand, we remark that $d_L(M)$ is algorithmically computable, since the homeomorphism problem for $3$-manifolds is decidable: there exists a deterministic algorithm to decide if two given $3$-manifolds are homeomorphic or not~\cite{Kuperberg}. Thus we can enumerate all branched covers of $L$ ordered by the degree of the covering and check when the first such manifold is homeomorphic to $M$.
