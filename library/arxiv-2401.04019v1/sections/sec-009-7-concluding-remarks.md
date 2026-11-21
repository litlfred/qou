---
doc_id: arxiv-2401.04019v1
doc_title: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY"
section_id: sec-009-7-concluding-remarks
section_title: "Concluding remarks"
section_number: 7
pages: 18-20
source_pdf: 2401.04019v1.pdf
source_sha256: 1a29e52a81639640
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.955
doc_brief: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY — The work of Andrews and Merca on the truncated Euler’s pen- tagonal number theorem led to a resurgence in research on truncated"
---
[]{#concluding label="concluding"}

In this article we considered several conjectures and identities that first appeared in [@M1]. Identities (6.7), (6.10), (6.12) and (6.13) from [@M1] are proved using the Jacobi Triple Product identity in [@KMR]. We generalized these identities and gave both analytic and combinatorial proofs. Considerations of similar identities from [@M1], and their proofs in [@KMR] led us to discover an interesting result about the number of distinct $5$-regular partitions of $n$. Theorem [\[main\]](#main){reference-type="ref" reference="main"} proves the cases $k=1,2,3$ of Conjecture 4.3 in [@M1] which concerns the non-negativity of the coefficients of a certain truncated theta function. The theorem gives inequalities involving the number of partitions of $n$ with parts congruent to $\pm S \mod R$ and it also leads to results involving the generalizations of the minimal excludant statistic for partitions.

At the end of [@M1], Merca made another conjecture about the non-negativity of the coefficients of a truncated series. Suppose $R\geq 2$ and $1\leq S<R$ and define $$T_{\pm}(q,k,S,R):=\frac{1}{(q^S, q^{R-S};q^R)_\infty }\sum_{n=k}^\infty q^{n(3n\mp 1)R/2\pm 3nS}(1-q^{S\pm nR}).$$ Conjecture 6.15 on [@M1] states that, for all $k\geq 1$, each of $T_{+}(q,k,S,R)$, $-T_{-}(q,k,S,R)$, and $T_{-}(q,k,S,R)+T_{+}(q,k,S,R)$ has non-negative coefficients. We establish the first two parts of the conjecture.

::: theorem
For $1\leq S<R$ and $k\geq 1$,

-   $T_{+}(q,k,S,R)$ has non-negative coefficients;

-   $T_{-}(q,k,S,R)$ has non-positive coefficients.
:::

::: proof
*Proof.* Let $1\leq S <R$ and $k\geq 1$.

To show that for the $q$-series $T_+(q,k,S,R)$ has non-negative coefficients, we rewrite it as $$\begin{aligned}
&T_+(q,k,S,R)
\\& =\frac{1}{(q^S, q^{R-S};q^R)_\infty} \sum_{n=k}^\infty q^{n(3n-1)R/2+3nS}(1-q^{n(R-S)}+q^{n(R-S)}-q^{S+nR})\\ & = \frac{1}{(q^S, q^{2R-S};q^R)_\infty} \sum_{n=k}^\infty q^{n(3n-1)R/2+3nS}\, \frac{1-q^{n(R-S)}}{1-q^{R-S}}\\ & \ \ \ + \frac{1}{(q^{S+R}, q^{R-S};q^R)_\infty} \sum_{n=k}^\infty q^{n(3n-1)R/2+3nS+nR-nS}\, \frac{1-q^{(n+1)S}}{1-q^S}\\ & = \frac{1}{(q^S, q^{2R-S};q^R)_\infty} \sum_{n=k}^\infty q^{n(3n-1)R/2+3nS} (1+q^{R-S}+q^{2(R-S)}+\cdots +q^{(n-1)(R-S)})\\ & \ \ \ + \frac{1}{(q^{S+R}, q^{R-S};q^R)_\infty} \sum_{n=k}^\infty q^{n(3n+1)R/2+2nS}(1+q^{S}+q^{2S}+\cdots+ q^{nS})
.
\end{aligned}$$ Clearly, this $q$-series has non-negative coefficients.

If $k\geq 2$, we rewrite $$\begin{aligned}
&-T_-(q,k,S,R)\\ & = - \frac{1}{(q^S, q^{R-S};q^R)_\infty} \sum_{n=k}^\infty q^{n(3n+ 1)R/2- 3nS}(1-q^{S- nR})\\& =\frac{1}{(q^S, q^{R-S};q^R)_\infty} \sum_{n=k}^\infty q^{n(3n+1)R/2-3nS+S-nR}(1-q^{n(R-S)}+q^{n(R-S)}-q^{nR-S})\\ & = \frac{1}{(q^S, q^{2R-S};q^R)_\infty} \sum_{n=k}^\infty q^{n(3n+1)R/2-3nS+S-nR}\, \frac{1-q^{n(R-S)}}{1-q^{R-S}}\\ & \ \ \ + \frac{1}{(q^{S+R}, q^{R-S};q^R)_\infty} \sum_{n=k}^\infty q^{n(3n+1)R/2-3nS+S-nR+nR-nS}\, \frac{1-q^{(n-1)S}}{1-q^S}\\ & = \frac{1}{(q^S, q^{2R-S};q^R)_\infty} \sum_{n=k}^\infty q^{n(3n-1)R/2-3nS+S} (1+q^{R-S}+q^{2(R-S)}+\cdots +q^{(n-1)(R-S)})\\ & \ \ \ + \frac{1}{(q^{S+R}, q^{R-S};q^R)_\infty} \sum_{n=k}^\infty q^{n(3n+1)R/2-4nS+S}(1+q^{S}+q^{2S}+\cdots+ q^{(n-2)S})
.
\end{aligned}$$ If $k=1$, we have $$\begin{aligned}
&-T_-(q,1,S,R) =\frac{q^{R-2S}}{(q^S, q^{2R-S};q^R)_\infty}  - T_-(q,2,S,R). 
\end{aligned}$$ Clearly, in each case $-T_-(q,1,S,R)$ has non-negative coefficients. ◻
:::

Finally, we note that results of a similar flavor appear in [@M2]. Let $g(n)=|\mathcal P_{\pm 1,5}(n)|$ (respectively $h(n)=|\mathcal P_{\pm 2,5}(n)|$) be the number of partitions of $n$ into parts congruent to $\pm 1 \mod 5$ (respectively $\pm 2\mod 5$). If $\xi(n)$ is either of $g(n)$ or $h(n)$, Merca [@M2 Corollary 3.3] proves the following families of linear homogeneous inequalities. For $k\geq 1$, $S\in\{1,2\}$, and $n\geq 0$ $$\label{eq:M2}
        u_{\xi,S}^{\pm}(n):= \pm \sum_{j=k}^\infty\left(\xi\left(n-5j(3j\pm 1)/2\pm 3jS\right)-\xi\left(n-5j(3j\pm 1)/2\mp (3j\pm 1)S\right) \right)\geq 0$$ and asks for combinatorial interpretations of these sums. The requested interpretations can be read off the generating functions obtained in the proofs in [@M2].

In the proof of [@M2 Theorem 2.1] (with $R=5, S=1$) it is shown that $$\sum_{n=0}^\infty u_{g,1}^{+}(n)q^n=\frac{1}{(q^{6},q^{4};q^5)_\infty}\sum_{j=k}^\infty q^{5j(3j+1)/2-3j}\big(1+q+q^{2}+\cdots +q^{6j}\big).$$

Now, $\displaystyle \frac{1}{(q^{6},q^{4};q^5)_\infty}$ is the generating function for the number of partitions $\lambda\in \mathcal P_{\pm 1,5}(n)$ of $n$ with no part equal to $1$. We can interpret $\displaystyle q^{5j(3j+1)/2-3j}$ as generating a single partition $(5j+1)^j\cup \delta_{1,5,j}$.

Then $$u_{g,1}^+(n)=|\{(\lambda,(5j+1)^j\cup \delta_{1,5,j})\vdash n  \mid   \lambda\in \mathcal P_{\pm 1, 5}, m_\lambda(1)\leq 6j, j\geq k\}|.$$

In a similar way we can show that $$\begin{aligned}
u_{h,2}^+(n)&=|\{ (\lambda, (5(j-1)+2)^j\cup \delta_{2,5,j})\vdash n \mid \lambda \in \mathcal P_{\pm2,5}, m_{\lambda}(2)\leq 6j, j\geq k \}|\\
u_{g,1}^-(n)&=|\{ (\lambda, (5j+1)^{j-1}\cup\delta_{1,5,j}\cup (4)) \vdash n \mid \lambda \in \mathcal P_{\pm1,5}, m_{\lambda}(1)\leq 6j-2, j\geq k\}|\\ 
u_{h,2}^-(n)&=|\{(\lambda, (5(j-1)+2)^{j-1}\cup \delta_{2,5,j}\cup (3)) \vdash n\mid \lambda \in \mathcal P_{\pm 2, 5}, m_\lambda(2)\leq 6j-2, j\geq k \}|. 
\end{aligned}$$

Using the generating functions in [@M2 Corollary 3.2], we have $$\begin{aligned}
u_{g,2}^+(n)&=|\{ (\lambda, (\delta_{4,5,2j-1}\setminus \delta_{4,5,j-1}))\vdash n \mid \lambda \in \mathcal P_{\pm1,5}, m_{\lambda}(1)\leq 12j+1, j\geq k \}|\\ u_{g,2}^-(n)&=|\{ (\lambda, (\delta_{4,5,2j-2}\setminus \delta_{4,5,j-1})\cup(5(j-1)+1))\vdash n \mid \lambda \in \mathcal P_{\pm1,5}, m_{\lambda}(1)\leq 12j-3, j\geq k \}|\\
u_{h,1}^+(n)&=|\{ (\lambda, (\delta_{2,5,2j}\setminus \delta_{2,5,j}))\vdash n \mid \lambda \in \mathcal P_{\pm2,5}, m_{\lambda}(2)\leq 3j-2, j\geq k \}|\\ & \ \ \ +|\{ (\lambda, (\delta_{3,5,2j+1}\setminus \delta_{3,5,j+2})\cup(5j+3))\vdash n \mid \lambda \in \mathcal P_{\pm2,5}, m_{\lambda}(3)= 1, j\geq k \}|
\\ u_{h,1}^-(n)&=|\{ (\lambda, (\delta_{2,5,2j-1}\setminus \delta_{2,5,j}) \cup(5(j-1)+3))\vdash n \mid \lambda \in \mathcal P_{\pm2,5}, m_{\lambda}(2)\leq 3j-3, j\geq k \}|\\ & \ \ \ 
+|\{ (\lambda, (\delta_{3,5,2j}\setminus \delta_{3,5,j+1})\cup(5(j-1)+2))\vdash n \mid \lambda \in \mathcal P_{\pm2,5}, m_{\lambda}(3)= 1, j\geq k \}|.
\end{aligned}$$
