---
doc_id: arxiv-1711.08944v2
doc_title: "The second largest eigenvalues of some Cayley graphs on alternating groups ∗"
section_id: sec-001-2-the-second-largest-eigenvalue-of-agn
section_title: "The second largest eigenvalue of AGn"
section_number: 2
pages: 3-7
source_pdf: 1711.08944v2.pdf
source_sha256: ad7a020e7e92b788
toc_source: outline
text_source: latex
latex_prose_ratio: 0.622
latex_coverage_ratio: 0.595
doc_brief: "The second largest eigenvalues of some Cayley graphs on alternating groups ∗ — Let An denote the alternating group of degree n with n ≥3."
---
[]{#s-3 label="s-3"} Recall that the complete alternating group graph is defined as $CAG_n=\mathrm{Cay}(A_n,T_3)$, where $T_3=\{(i,j,k),(i,k,j)\mid 1\leq i<j<k\leq n\}$ is the set of all $3$-cycles in $S_n$. In this section, we mainly focus on determining the second largest eigenvalue of $CAG_n$. The main idea is to find some suitable equitable partition so that we can decompose the edge set of $CAG_n$ into that of $n$ copies of $CAG_{n-1}$ and that of the extended alternating group graph $EAG_{n}=\mathrm{Cay}(A_n,T_2)$, where $T_2=\{(1,i,j),(1,j,i)\mid 2\leq i<j\leq n\}$ is the set of $3$-cycles in $S_n$ moving $1$, which ensures that the way of induction could be used to find the second largest eigenvalue of $CAG_n$. For this reason, we first need to consider the same problem for the graph $EAG_n$, and again, the main method depends on finding some suitable equitable partition to decompose the edge set of $EAG_n$.

For $1\leq i,j\leq n$, we define $$\label{equ-3}
X_i(j)=\{\tau\in A_n\mid \tau_j=i\}.$$ For any fixed $i$ (resp. $j$), we see that $X_i(1), X_i(2),\ldots,X_i(n)$ (resp. $X_1(j), X_2(j),\ldots,$ $X_n(j)$) partition $A_n$. Now we shall verify that $\Pi: A_n=X_i(1)\cup X_i(2)\cup \cdots\cup X_i(n)$ is an equitable partition of $EAG_n$ for each $i$. For $\tau\in X_i(1)$, we have $N(\tau)\cap X_i(1)=\emptyset$ since $(\sigma\tau)_1\neq \tau_1=i$ for any $\sigma\in T_2$, and $N(\tau)\cap X_i(j)=\{(1,k,j)\tau\mid 2\leq k\leq n,k\neq j\}$ for $2\leq j\leq n$. Thus each $\tau\in X_i(1)$ has no neighbors in $X_i(1)$ and $n-2$ neighbors in $X_i(j)$ for each $j$ ($2\leq j\leq n$). For each fixed $j$ ($2\leq j\leq n$), let $\tau\in X_i(j)$, we have $N(\tau)\cap X_i(1)=\{(1,j,k)\tau\mid 2\leq k\leq n,k\neq j\}$, $N(\tau)\cap X_i(j)=\{(1,k,l)\tau,(1,l,k)\tau\mid 2\leq k<l\leq n,k,l\neq j\}$, and $N(\tau)\cap X_i(\ell)=\{(1,\ell,j)\tau\}$ for any $\ell\not\in\{1,j\}$. This implies that $\tau$ has $n-2$ neighbors in $X_i(1)$, $(n-2)(n-3)$ neighbors in $X_i(j)$, and one neighbor in $X_i(\ell)$ for each $\ell\not\in\{1,j\}$. Thus the partition $\Pi$ is an equitable partition of $EAG_n$ with divisor matrix $$B_\Pi=
\left[
\begin{matrix}
0&n-2&n-2&\cdots&n-2\\
n-2&(n-2)(n-3)&1&\cdots&1\\
n-2&1&(n-2)(n-3)&\cdots&1\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
n-2&1&1&\cdots&(n-2)(n-3)
\end{matrix}
\right]
\begin{matrix}
X_i(1)\\
X_i(2)\\
X_i(3)\\
\vdots\\
X_i(n)
\end{matrix}$$ Then the characteristic polynomial of $B_\Pi$ is equal to $$\begin{aligned}
|\lambda I_n-B_\Pi|
&=&
\left|
\begin{smallmatrix}
\lambda &-(n-2)&-(n-2)&\cdots&-(n-2)\\
-(n-2)&\lambda-(n-2)(n-3)&-1&\cdots&-1\\
-(n-2)&-1&\lambda-(n-2)(n-3)&\cdots&-1\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
-(n-2)&-1&-1&\cdots&\lambda-(n-2)(n-3)
\end{smallmatrix}
\right|\\
&=&
(\lambda-(n-1)(n-2))\left|
\begin{smallmatrix}
1 &-(n-2)&-(n-2)&\cdots&-(n-2)\\
1&\lambda-(n-2)(n-3)&-1&\cdots&-1\\
1&-1&\lambda-(n-2)(n-3)&\cdots&-1\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
1&-1&-1&\cdots&\lambda-(n-2)(n-3)
\end{smallmatrix}
\right|\\
&=&
(\lambda-(n-1)(n-2))\left|
\begin{smallmatrix}
1 &0&0&\cdots&0\\
1&\lambda-(n-2)(n-4)&n-3&\cdots&n-3\\
1&n-3&\lambda-(n-2)(n-4)&\cdots&n-3\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
1&n-3&n-3&\cdots&\lambda-(n-2)(n-4)
\end{smallmatrix}
\right|\\
&=&
(\lambda-(n-1)(n-2))\left|
\begin{smallmatrix}
\lambda-(n-2)(n-4)&n-3&\cdots&n-3\\
n-3&\lambda-(n-2)(n-4)&\cdots&n-3\\
\vdots&\vdots&\ddots&\vdots\\
n-3&n-3&\cdots&\lambda-(n-2)(n-4)
\end{smallmatrix}
\right|\\
&=&
(\lambda\!-\!(n-1)(n-2))\left|
(\lambda\!-\!(n-2)(n-4))I_{n-1}\!+\!(n-3)(J_{n-1}\!-\!I_{n-1})
\right|\\
&=&
(\lambda-(n-1)(n-2))(\lambda-(n^2-5n+5))^{n-2}(\lambda+(n-2)),
\end{aligned}$$ where $I_{n-1}$ and $J_{n-1}$ denote the identity matrix and all ones matrix of order $n-1$, respectively. By Lemma [\[lem-2-1\]](#lem-2-1){reference-type="ref" reference="lem-2-1"}, we have

::: lem
[]{#lem-3-1 label="lem-3-1"} Let $EAG_n$ be the extended alternating group graph with $n\geq 3$. Then $EAG_n$ has eigenvalues $(n-1)(n-2)$, $n^2-5n+5$ (with multiplicity at least $n-2$) and $2-n$. Moreover, if $f$ is an eigenvector of $EAG_n$ corresponding to any other eigenvalue, then for all $i,j\in\{1,2,\ldots,n\}$, we have $$\sum_{x\in X_i(j)}f(x)=0,$$ where $X_i(j)$ is defined in ([\[equ-3\]](#equ-3){reference-type="ref" reference="equ-3"}).
:::

Now we give the second largest eigenvalue of $EAG_n$.

::: thm
[]{#thm-2 label="thm-2"} Let $EAG_n$ be the extended alternating group graph with $n\geq 3$. Then the two largest eigenvalues of $EAG_n$ are $\lambda_1(EAG_n)=(n-1)(n-2)$ and $\lambda_2(EAG_n)=n^2-5n+5$.
:::

::: proof
*Proof.* Obviously, $\lambda_1(EAG_n)=(n-1)(n-2)$ because $EAG_n$ is $(n-1)(n-2)$-regular. Now we prove $\lambda_2(EAG_n)=n^2-5n+5$ by induction on $n$. For $n=3$, we have $EAG_3=K_3$, which gives that $\lambda_2(EAG_3)=-1$, and the result follows. Now suppose $n\geq 4$ and assume that the result holds for $EAG_{n-1}$, i.e., $\lambda_2(EAG_{n-1})=(n-1)^2-5(n-1)+5$. Let $\lambda$ be an eigenvalue of $EAG_n$ that is not equal to $(n-1)(n-2)$, $n^2-5n+5$ or $2-n$, and let $f$ be any fixed eigenvector corresponding to $\lambda$. Then $f$ must sum to zero on $X_i(j)$ for all $1\leq i,j\leq n$. Now we partition the vertex set of $EAG_n$ as $A_n=X_1(2)\cup X_2(2)\cup \cdots\cup X_n(2)$. As in the proof of Theorem [\[thm-1\]](#thm-1){reference-type="ref" reference="thm-1"}, one can easily verify that the induce subgraph of $EAG_n$ on $X_i(2)$ is isomorphic to $EAG_{n-1}$ for each $i$ ($1\leq i\leq n$). Let $E_1=\cup_{i=1}^n E(EAG_n[X_i(2)])$ and $E_2=E(EAG_n)\setminus E_1$. We claim that $E_2$ is exactly the set of edges of the alternating group graph $AG_n=\mathrm{Cay}(A_n,T_1)$, where $T_1=\{(1,2,k),(1,k,2)\mid 3\leq k\leq n\}$. In fact, for any $\gamma\in X_i(2)$ and $\gamma'\in X_j(2)$ ($i\neq j$), we have $\{\gamma,\gamma'\}\in E(EAG_n)$ if and only if $\gamma'\gamma^{-1}\in T_2$ (i.e., $\gamma'\gamma^{-1}$ is a $3$-cycle moving $1$), which is the case if and only $\gamma'\gamma^{-1}\in T_1(\subseteq T_2)$ because $\gamma'\gamma^{-1}$ must move $2$ due to $i\neq j$. This implies that the edges in $E_2$ come from $T_1$. On the other hand, we see that $T_1$ can only be used to produce the edges in $E_2$ because each edge in $E_1$ comes from $T_2\setminus T_1$, i.e., the set of $3$-cycles in $T_2$ fixing $2$. Then $$\begin{aligned}
\lambda&=&\frac{f^TA(EAG_n)f}{f^Tf}\\
&=&\frac{2\sum_{\{x,y\}\in E(EAG_n)}f(x)f(y)}{\sum_{x\in A_n}f(x)^2}\\
&=&\frac{2\sum_{\{x,y\}\in E_1}f(x)f(y)}{\sum_{x\in A_n}f(x)^2}+\frac{2\sum_{\{x,y\}\in E_2}f(x)f(y)}{\sum_{x\in A_n}f(x)^2}.
\end{aligned}$$ For the first term, we have $$\begin{aligned}
\frac{2\sum_{\{x,y\}\in E_1}f(x)f(y)}{\sum_{x\in A_n}f(x)^2}&=&\frac{\sum_{i=1}^n2\sum_{\{x,y\}\in E(EAG_n[X_i(2)])}f(x)f(y)}{\sum_{i=1}^n\sum_{x\in X_i(2)}f(x)^2}\\
&\leq &\max_{1\leq i\leq n}\frac{2\sum_{\{x,y\}\in E(EAG_n[X_i(2)])}f(x)f(y)}{\sum_{x\in X_i(2)}f(x)^2}\\
&\leq &\lambda_2(EAG_{n-1}),
\end{aligned}$$ where the last inequality follows from the fact $\sum_{x\in X_i(2)}f(x)=0$ for each $i$ according to Lemma [\[lem-3-1\]](#lem-3-1){reference-type="ref" reference="lem-3-1"}. For the second term, since $f$ is orthogonal to the all ones vector $\mathbf{1}$, we have $$\frac{2\sum_{\{x,y\}\in E_2}f(x)f(y)}{\sum_{x\in A_n}f(x)^2}\leq\max_{g\perp\mathbf{1}}\frac{g^TA(AG_n)g}{g^Tg}=\lambda_2(AG_n).$$ Combining above two bounds, we conclude that $$\lambda\leq \lambda_2(EAG_{n-1})+\lambda_2(AG_n)=(n-1)^2-5(n-1)+5+2n-6=n^2-5n+5$$ by Theorem [\[thm-1\]](#thm-1){reference-type="ref" reference="thm-1"}. Hence $\lambda_2(EAG_n)=n^2-5n+5$, and our result follows. ◻
:::

Now we focus on the complete alternating group graph $CAG_n=\mathrm{Cay}(A_n,T_3)$ where $T_3=\{(i,j,k),(i,k,j)\mid 1\leq i<j<k\leq n\}$. Obviously, $CAG_n$ is a $2\binom{n}{3}$-regular graph. As above, we shall verify that $\Pi: A_n=X_i(1)\cup X_i(2)\cup \cdots\cup X_i(n)$ is also an equitable partition of $CAG_n$ for each fixed $i$, where $X_i(j)$ is defined in ([\[equ-3\]](#equ-3){reference-type="ref" reference="equ-3"}). For each fixed $j$ ($1\leq j\leq n$), let $\tau\in X_i(j)$. We have $N(\tau)\cap X_i(j)=\{(k,l,m)\tau,(k,m,l)\tau\mid1\leq k<l<m\leq n, k,l,m\neq j\}$, and $N(\tau)\cap X_i(\ell)=\{(\ell,j,k)\tau\mid 1\leq k\leq n, k\neq\ell, j\}$ for each $\ell\neq j$. This implies that $\tau$ has $2\binom{n-1}{3}$ neighbors in $X_i(j)$, and $n-2$ neighbors in $X_i(\ell)$ for each $\ell\neq j$. Thus $\Pi$ is an equitable partition of $CAG_n$ with divisor matrix $$B_\Pi=
\left[
\begin{matrix}
2\binom{n-1}{3}&n-2&n-2&\cdots&n-2\\
n-2&2\binom{n-1}{3}&n-2&\cdots&n-2\\
n-2&n-2&2\binom{n-1}{3}&\cdots&n-2\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
n-2&n-2&n-2&\cdots&2\binom{n-1}{3}
\end{matrix}
\right]
\begin{matrix}
X_i(1)\\
X_i(2)\\
X_i(3)\\
\vdots\\
X_i(n)
\end{matrix}.$$ It is easy to see that $B_\Pi$ has eigenvalues $2\binom{n}{3}$ and $\frac{1}{3}n(n-2)(n-4)$, where the first one is of multiplicity $1$ having the all ones vector $\mathbf{1}$ as its eigenvector, and the second one is of multiplicity $n-1$ having each vector orthogonal to $\mathbf{1}$ as an eigenvector. Again by Lemma [\[lem-2-1\]](#lem-2-1){reference-type="ref" reference="lem-2-1"}, we have

::: lem
[]{#lem-4-1 label="lem-4-1"} Let $CAG_n$ be the complete alternating group graph with $n\geq 3$. Then $CAG_n$ has eigenvalues $2\binom{n}{3}$ and $\frac{1}{3}n(n-2)(n-4)$ (with multiplicity at least $n-1$). Moreover, if $f$ is an eigenvector of $CAG_n$ corresponding to any other eigenvalue, then for all $i,j\in\{1,2,\ldots,n\}$, we have $$\sum_{x\in X_i(j)}f(x)=0,$$ where $X_i(j)$ is defined in ([\[equ-3\]](#equ-3){reference-type="ref" reference="equ-3"}).
:::

Now we prove the main result of this section.

::: thm
[]{#thm-3 label="thm-3"} Let $CAG_n$ be the complete alternating group graph with $n\geq 3$. Then the two largest eigenvalues of $CAG_n$ are $\lambda_1(CAG_n)=2\binom{n}{3}$ and $\lambda_2(CAG_n)=\frac{1}{3}n(n-2)(n-4)$.
:::

::: proof
*Proof.* Clearly, we have $\lambda_1(CAG_n)=2\binom{n}{3}$ because $CAG_n$ is $2\binom{n}{3}$-regular. We shall prove $\lambda_2(CAG_n)=\frac{1}{3}n(n-2)(n-4)$ by induction on $n$. For $n=3$, we have $\lambda_2(CAG_3)=\lambda_2(K_3)=-1$, as required. Now suppose $n\geq 4$. Assume that the result holds for $n-1$, i.e., $\lambda_2(CAG_{n-1})=\frac{1}{3}(n-1)(n-3)(n-5)$. Let $\lambda$ be any eigenvalue of $CAG_n$ that is not equal to $2\binom{n}{3}$ or $\frac{1}{3}n(n-2)(n-4)$, and pick any eigenvector $f$ of $CAG_n$ corresponding to $\lambda$. Again, the vector $f$ must sum to zero on $X_i(j)$ for all $i,j$ according to Lemma [\[lem-4-1\]](#lem-4-1){reference-type="ref" reference="lem-4-1"}. We partition the vertex set of $CAG_n$ as $A_n=X_1(1)\cup X_2(1)\cup \cdots\cup X_n(1)$. Let $E_1=\{\{\tau,\sigma\}\in E(CAG_n)\mid \tau_1\neq \sigma_1\}$ and $E_2^i=\{\{\tau,\sigma\}\in E(CAG_n)\mid \tau_1=\sigma_1=i\}$ for $1\leq i\leq n$. Then $E_1\cup E_2^1\cup E_2^2\cup \cdots\cup E_2^n$ is a partition of $E(CAG_n)$. As in the proof of Theorem [\[thm-2\]](#thm-2){reference-type="ref" reference="thm-2"}, we see that $E_1$ is exactly the set of edges of the extended alternating group graph $EAG_n=\mathrm{Cay}(A_n,T_2)$ with $T_2=\{(1,k,l),(1,l,k)\mid 2\leq k<l\leq n\}$, and for each $i$, $E_2^i$ is exactly the set of edges of the induced subgraph of $CAG_n$ on $X_i(1)$ which is also isomorphic to $CAG_{n-1}$. Then we have $$\begin{aligned}
\lambda&=&\frac{f^TA(CAG_n)f}{f^Tf}\\
&=&\frac{2\sum_{\{x,y\}\in E(CAG_n)}f(x)f(y)}{\sum_{x\in A_n}f(x)^2}\\
&=&\frac{2\sum_{\{x,y\}\in E_1}f(x)f(y)}{\sum_{x\in A_n}f(x)^2}+\frac{\sum_{i=1}^n2\sum_{\{x,y\}\in E_2^i}f(x)f(y)}{\sum_{x\in A_n}f(x)^2}.
\end{aligned}$$ For the first term, since $f$ is orthogonal to the all ones vector $\mathbf{1}$, we have $$\frac{2\sum_{\{x,y\}\in E_1}f(x)f(y)}{\sum_{x\in A_n}f(x)^2}\leq\max_{g\perp\mathbf{1}}\frac{g^TA(EAG_n)g}{g^Tg}=\lambda_2(EAG_n).$$ For the second term, we have $$\begin{aligned}
\frac{\sum_{i=1}^n2\sum_{\{x,y\}\in E_2^i}f(x)f(y)}{\sum_{x\in A_n}f(x)^2}&=&\frac{\sum_{i=1}^n2\sum_{\{x,y\}\in E(CAG_n[X_i(1)])}f(x)f(y)}{\sum_{i=1}^n\sum_{x\in X_i(1)}f(x)^2}\\
&\leq &\max_{1\leq i\leq n}\frac{2\sum_{\{x,y\}\in E(CAG_n[X_i(1)])}f(x)f(y)}{\sum_{x\in X_i(1)}f(x)^2}\\
&\leq &\lambda_2(CAG_{n-1}),
\end{aligned}$$ where the last inequality follows from the fact $\sum_{x\in X_i(1)}f(x)=0$ for each $i$ according to Lemma [\[lem-3-1\]](#lem-3-1){reference-type="ref" reference="lem-3-1"}. Combining above two bounds, we conclude that $$\lambda\leq \lambda_2(EAG_{n})+\lambda_2(CAG_{n-1})=n^2-5n+5+\frac{1}{3}(n-1)(n-3)(n-5)=\frac{1}{3}n(n-2)(n-4)$$ by Theorem [\[thm-2\]](#thm-2){reference-type="ref" reference="thm-2"}. Hence $\lambda_2(EAG_n)=\frac{1}{3}n(n-2)(n-4)$, as required. ◻
:::

At the end of this paper, we pose the following problem.

::: prob
[]{#prob-1 label="prob-1"} How to determine all distinct eigenvalues (with multiplicities) of $AG_n$, $EAG_n$ and $CAG_n$?
:::

# Acknowledgments

The authors are grateful to the anonymous referees for their useful and constructive comments, which have considerably improved the presentation of this paper.
