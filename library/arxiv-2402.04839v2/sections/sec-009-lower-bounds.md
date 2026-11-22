---
doc_id: arxiv-2402.04839v2
doc_title: "On a volume invariant of 3-manifolds"
section_id: sec-009-lower-bounds
section_title: "Lower bounds"
section_number: null
pages: 11-11
source_pdf: 2402.04839v2.pdf
source_sha256: daf09811c350a2ad
toc_source: outline
text_source: latex
latex_prose_ratio: 0.969
latex_coverage_ratio: 0.97
doc_brief: "On a volume invariant of 3-manifolds (Kegel, Ray, Spreer, Thompson, Tillmann) — defines topological volume vol_t(M), the smallest volume of a hyperbolic-link complement in M; bounds and a…"
---
In \Cref{cor:topinv} (2) we have shown that a sequence of manifolds with unbounded rank of first homology has unbounded topological volume. In the next theorem, we develop a lower bound which quantifies this.

\begin{reptheorem}{thm:lower_bounds}
    Let $M$ be a closed, orientable 3--manifold and $p$ be a prime. Then
    \begin{equation*}
        \frac{\operatorname{rk}(H_1(M;\Z_p))}{168.602}< \volt(M).
    \end{equation*}
    Moreover, we have $\volt(M)>3.08,$ $3.69$, $3.77$ for $\operatorname{rk}(H_1(M;\Z_2))>5$, $7$, $10$, respectively.
\end{reptheorem}

\begin{proof}
   A result by Guzman--Shalen~\cite{Guzman_Shalen} states that for every finite-volume, orientable, hyperbolic 3-manifold $N$, and every prime $p$, we have $\operatorname{rk}(H_1(N;\Z_p)) < 168.602 \cdot  \volh(N)$. Now let $L \subset M$ be a volume minimiser of $M$, and set $N=M\setminus L$. Since the rank of the first homology cannot increase under filling, the first inequality follows, i.e.
   \begin{equation*}
       \frac{\operatorname{rk}(H_1(M;\Z_p))}{168.602}\leq\frac{\operatorname{rk}(H_1(M\setminus L;\Z_p))}{168.602}< \volh(M\setminus L)= \volt(M).
   \end{equation*}
   For the other inequalities we use the main results of~\cite{Culler_Shalen2011,Culler_Shalen2012,Guzman_Shalen2020} stating that for every \textit{closed}, finite-volume, orientable, hyperbolic $3$--manifold $N$ with $\operatorname{rk}(H_1(N;\Z_2))>5$, $7$ or $10$ we have $\volh(N)>3.08$, $3.69$ or $3.77$ respectively. Let $L$ be a volume minimiser for $M$. For every cusp $c_i$ of $M\setminus L$ we choose a sequence of slopes $p^{c_i}_n/q^{c_i}_n$ whose lengths converge to $\infty$ and such that filling $M\setminus L$ with these slopes yield manifolds $N_n$ with $\operatorname{rk}(H_1(N_n;\Z_2))=\operatorname{rk}(H_1(M;\Z_2))$. Note that the latter is satisfied if all $p^{c_i}_n$ are even. Since the lengths of the slopes converge to infinity it follows that {\em (a)} the manifolds $N_n$ are hyperbolic for $n$ sufficiently large, and {\em (b)} the volumes of $N_n$ converge to the volume of $M\setminus L$. Thus, applying the results of~\cite{Culler_Shalen2011,Culler_Shalen2012,Guzman_Shalen2020} to the $N_n$ yields the claimed inequalities for $\volt(M)$.
\end{proof}

\begin{example}\label{ex:SFS}
Although our general upper and lower bounds are far from sharp, we claim that their asymptotic behaviour is the same. Let $M$ be the Seifert fibered space of genus $g$ and $n$ singular fibres $SFS(g;p,\ldots, p)$ for a prime $p$. From the standard surgery description (see \cref{fig:SFS}) of $M$ we compute $\operatorname{rk}(H_1(M;\Z_p))=2g+n$ and thus \cref{thm:lower_bounds} and \cref{cor:SFS_bound} yield
    \begin{equation*}
        \frac{2g+n}{168.602} <\volt(M) < 37g+22n-28.
    \end{equation*}
    We observe that the quotient of the upper bound divided by the lower bound is bounded.
\end{example}
