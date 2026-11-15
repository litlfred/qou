---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-009-21-a-lemma-from-complex-analysis
section_title: "A lemma from complex analysis"
section_number: 2.1
pages: 8-8
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.915
latex_coverage_ratio: 0.974
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sub.complex}


To prove Theorem \ref{thm.11}, we need to improve the weak
convergence of Theorem \ref{thm.MMR} to the strong convergence.
This uses the next lemma on normal
families that is sometimes referred to by the name of {\em Vitali} or
{\em Montel's} theorem. For a reference, see \cite{Hi,Sch}. The lemma exhibits
the power of holomorphy, coupled with uniform boundedness.




\begin{lemma}
\lbl{lem.complex}
If
$$
f_n: \{z \in \BC \, : \, |z| < r \} \to \{z \in \BC \, : \, |z| \leq M \}
$$
is a uniformly bounded sequence of holomorphic functions such
that for every $m \geq 0$, we have:
$$
\lim_{n \to \infty} f^{(m)}_n(0) =a_m.
$$
Then,
\begin{itemize}
\item
The limit $f(z)=\lim_n f_n(z)$ exists pointwise for all $z$ with $|z| < r$ .
\item
$f$ is holomorphic,
\item
The convergence is uniform on compact subsets, and
\item
For every $m$, $f^{(m)}(0)=a_m$.
\end{itemize}
In other words, weak convergence and uniform boundedness imply
strong convergence.
\end{lemma}


\begin{proof}
$\{f_n\}_n$ is uniformly bounded, so it is a normal family, and contains
a convergent subsequence $f_j\to f$. Convergence is uniform on compact sets,
and $f$ is holomorphic, and for every $m \geq 0$,
$\lim_j f_j^{(m)}(0)=f^{(m)}(0)=a_m$.

If $\{f_n\}_n$ is not convergent (uniformly on compact sets),
since it is a normal family, then
there exist two subsequences that converge to $f$ and $g$
respectively, with $f \neq g$. Applying the above discussion, it
follows that $f$ and $g$ are holomorphic functions with equal
derivatives of all orders at $0$. Thus, $f=g$, giving a
contradiction.
\end{proof}


 Theorem \ref{thm.11} follows from Lemma \ref{lem.complex} and
the following result, whose proof will be given in Section
\ref{sec.estimates}.

\begin{theorem}
\lbl{thm.boundC3} {\rm (Proof in Section \ref{sub.thm.boundC2})}

For every knot $K$ there exists an open neighborhood $U_K$ of $0 \in
\BC$ and a positive number $M$ such that for $\a \in U_K$, and all
$n \geq 1$, we have:
$$
|f_{K,n}(\a)| < M.
$$






\end{theorem}
