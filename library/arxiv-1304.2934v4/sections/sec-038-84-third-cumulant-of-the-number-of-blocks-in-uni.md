---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-038-84-third-cumulant-of-the-number-of-blocks-in-uni
section_title: "Third cumulant of the number of blocks in uniform set-partitions"
section_number: 8.4
pages: 68-69
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.989
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
Fix $n \ge 0$. Let $B_n$ be the number of set-partitions of $[n]$, known as the $n$-th Bell number. Dobinski's formula states that $B_n=\E^{-1} \sum_{k =0}^\infty k^n/k!$, which allows us to consider a random variable $M$ with the following distribution:
\[\proba[M=k] = \frac{1}{\E B_n} \frac{k^n}{k!}.\]
An easy observation, useful below, is that $\esper[M^r]=B_{n+r}/B_n$. As above, we denote $X_n$ the number of blocks in a uniform set-partition of size $[n]$. We also consider a Poisson variable $P$ of parameter $1$, independent from $X_n$.
Stam \cite{StamRandomPartition} proved the following relation (with a very nice probabilistic explanation).

\begin{lemma}
    \cite[Theorem 2]{StamRandomPartition}
    We have the following equality of random variables in law:
    \[M \stackrel{\text{law}}{=} X_n + P.\] 
\end{lemma}

\noindent Therefore, $\kappa^{(3)}(M) = \kappa^{(3)}(X_n) + \kappa^{(3)}(P)$. But $\kappa^{(3)}(P)=1$ is a constant (independent of $n$), whose value will not be relevant for the asymptotic of $\kappa^{(3)}(X_n)$. Let us consider $\kappa^{(3)}(M)$. It is given by:
\[\kappa^{(3)}(M) = \esper[M^3] -3 \,\esper[M^2] \esper[M] +2 (\esper[M])^3=\frac{B_{n+3}}{B_n} -3 \frac{B_{n+2}\, B_{n+1}}{(B_n)^2}
+2 \frac{(B_{n+1})^3}{(B_n)^3}.\]
In order to find the asymptotic of the above formula, we use the following estimate for Bell numbers. This is a variant of the Moser-Wyman formula \cite{MoserWymanFormula}, that can be found in an unpublished note of Mohr \cite{NoteMohr}.

\begin{lemma}
Let $\alpha_n$ be the positive real number defined by the equation $\alpha_n\, \E^{\alpha_n}=n$; in particular $\alpha_n=(\log n)\,(1-o(1))$. Then, one has, for any integer $r$,
    \begin{multline*}
        B_{n+r}=\frac{(n+r)!}{(\alpha_n)^{n+r}}\, \frac{\exp(\E^{\alpha_n}-1)}{\sqrt{2\pi \beta_n}} \\
        \times \left( 1+\frac{P_0+rP_1+r^2P_2}{\E^{\alpha_n}}+\frac{Q_0+rQ_1+r^2Q_2+r^3Q_3+r^4Q_4}{\E^{2\alpha_n}} +O(\E^{-3\alpha_n}) \right),
    \end{multline*}
where $\beta_n=((\alpha_n)^2+\alpha_n)\,\E^{\alpha_n}$, and the $P_i$'s and $Q_i$'s are explicit rational functions of $\alpha_n$, with $P_i=O((\alpha_n)^{-i})$ and $Q_i=O((\alpha_n)^{-i})$.
\end{lemma}

This lemma yields an estimate for quotients of Bell numbers (we substitute $\E^{\alpha_n}$ by $n/\alpha_n$):
\begin{multline*}
    (\alpha_n)^r \, \frac{B_{n+r}}{B_n}=(n+1) \cdots (n+r) \left( 
1+\alpha_n \, \frac{rP_1+r^2P_2}{n} \right.\\
\left.+(\alpha_n)^2 \, \frac{-P_0 (rP_1+r^2P_2)+rQ_1+r^2Q_2+r^3Q_3+r^4Q_4}{n^2} +O(\alpha_n^3/n^3)\right)
\end{multline*}
Consider the expression 
\[k^3:=\alpha_n^3 \left(\frac{B_{n+3}}{B_n} -3 \frac{B_{n+2}\, B_{n+1}}{B_n^2} +2 \frac{(B_{n+1})^3}{(B_n)^3} \right).\]
With the help of a computer algebra program, we find
\[k^3 = n \left( (-6 \, P_2\, (P_1+P_2) + 6 \, Q_3 + 36 \, Q_4 ) (\alpha_n)^2 + 12 P_2\, \alpha_n + 2\right) +O((\alpha_n)^3).\]

From the estimate $P_i=O((\alpha_n)^{-i})$ and $Q_i=O((\alpha_n)^{-i})$, we see that the dominant term in $k^3$ comes 
from the constant $2$ in the above equation. Namely,
\[k^3= 2 n + O\!\left(\frac{n}{\alpha_n}\right), \quad\text{ that is }\kappa^{(3)}(X_n)= \frac{2n}{(\alpha_n)^3} + O\!\left(\frac{n}{(\alpha_n)^4}\right),\]
as claimed in the previous subsection.
\bigskip
\bigskip
