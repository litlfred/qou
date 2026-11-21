---
doc_id: arxiv-1408.3518v3
doc_title: "On Augmentation Algorithms for Linear and Integer-Linear Programming: From Edmonds-Karp to Bland and Beyond"
section_id: sec-002-2-proofs
section_title: "Proofs"
section_number: 2
pages: 8-9
source_pdf: 1408.3518v3.pdf
source_sha256: cf18585b886587c7
toc_source: outline
text_source: latex
latex_prose_ratio: 0.92
latex_coverage_ratio: 0.959
doc_brief: "On Augmentation Algorithms for Linear and Integer-Linear Programming: From Edmonds-Karp to Bland and Beyond — 13 sections: Front matter; Introduction.; Our Contributions"
---
We present the proofs to the above results in separate subsections. We will use the following  lemma (a slight variation from Theorem 3.1 in \cite{Ahuja+Magnanti+Orlin}) which  establishes the bounds we claim once we can guarantee sufficient improvement at each iteration:
\begin{lemma}
\label{Lemma: Sufficient improvement leads to polynomial algorithm}

Let $\epsilon>0$ be given. Moreover, let $H$ denote the difference between maximum and minimum objective-function values of the LP/ILP problem in $n$ variables.
Suppose that $f^k=\vecc^\T \vex_k$ is the objective-function value of the solution $\vex_k$ at the $k$-th iteration of an algorithm and that $f^*=\vecc^\T \vex_{\min}$ is the minimum objective-function value. Furthermore, suppose that the algorithm guarantees that for every augmentation $k$,
\[
(f^k-f^{k+1})\geq\beta(f^k-f^*)
\]
(i.e., the improvement at augmentation $k+1$ is at least $\beta$ times the maximum possible improvement). Then the algorithm reaches a solution with $f^k-f^*<\epsilon$ in no more than $2 \log{(H/\epsilon)}/\beta$ augmentations.
\end{lemma}

\proof{Proof:} Without loss of generality, we assume that $\vecc$ is an integer vector. (Thus for the ILP version the values $f^k$ are decreasing successive integer values.) The biggest necessary change of value of the objective function occurs when we start the augmentation at an maximum point $\vex_{\max}$ and end with some minimum optimal point $\vex_{\min}$. Thus, we have $H=f^{\max}-f^{\min}$.

If we had at every augmentation an improvement of at least $\beta (f^{\max}-f^{\min})/2$, then
in no more than $2/\beta$ augmentations we would have reached the optimum. But if this improvement is not achieved at each augmentation, say at the $q$-th augmentation we have $f^q-f^{q+1} \leq \beta (f^{\max}-f^{\min})/2$ then, together with the hypothesis $(f^q-f^{q+1})\geq\beta(f^q-f^{\min})$, we get that
\[
  f^q-f^{\min} \leq (f^{\max}-f^{\min})/2=H/2.
\]
In other words, the overall improvement reached so far is at least half of the maximum possible improvement $H$.
In conclusion, after $2/\beta$ augmentations, we have either reached the optimum or have at least divided the possible gap by $2$. Therefore in no more than $2/\beta \log_2{(H/\epsilon)}$ augmentations we reach a solution with $f^k-f^*<\epsilon$. \Halmos
\endproof

It is important to note that in the ILP case $f^k$ is integer, and we can apply Lemma \ref{Lemma: Sufficient improvement leads to polynomial algorithm} with $\epsilon=1$ and conclude that we can reach the optimum in $O(\log{(H)}/\beta)$ augmentations. In the LP case, let $\delta$ denote the least common multiple of all subdeterminants of $A$. Observe that once we find a feasible solution $\vex_k$ with objective value $f^k$ satisfying $f^k-f^*<\epsilon=1/\delta$, then any vertex with an objective value of at most $f^k$ must be optimal. As explained above (right before the statement of Theorem \ref{theorem:main, ILP case}), such a vertex can be found from $\vex_k$ in at most $n$ additional augmentations. This leads to extra factors of $n$ and of $\log(\delta)$ in the bounds for the LP cases compared to the ILP cases.



\subsection{Proof of Lemma \ref{ILP-greedy} and Theorem \ref{theorem:main, ILP case}}

Let us assume that $\vex_k$ is a non-optimal feasible solution, and let $\vex_{\min}$ be an optimal solution to the ILP. Then there exists a (sign-compatible) representation
\[
  \vex_{\min} -  \vex_k =\sum\alpha_i\veg_i,
\]
with $\alpha_i>0$, $\alpha_i\in\Z$ and with $\alpha_i\veg_i\red \vex_{\min} - \vex_k$. Moreover, due to Seb\"o's result \cite{Sebo90}, at most $2n-2$ summands are needed.

Note that sign-compatibility of the representation $\vex_{\min}-\vex_k =\sum\alpha_i\veg_i$ implies that for all $i$ the vectors $\vex_{k}+\alpha_i\veg_i$ and $\vex_{\min}-\alpha_i\veg_i$ are all feasible solutions, since their components lie between the components of $\vex_k$ and of $\vex_{\min}$. Moreover, we can observe that for all such sign-compatible representations $\vex_{\min}-\vex_k =\sum\alpha_i\veg_i$ we must have $\vecc^\T\veg_i\leq 0$ for all $i$, as otherwise $\vex_{\min}-\alpha_i\veg_i$ would be a feasible solution with $\vecc^\T (\vex_{\min}-\alpha_i\veg_i)=\vecc^\T\vex_{\min}-\alpha_i\vecc^\T\veg_i<\vecc^\T\vex_{\min}$, contradicting the minimality of $\vex_{\min}$.

Next, we analyze what happens for each choice of augmentation rule:
