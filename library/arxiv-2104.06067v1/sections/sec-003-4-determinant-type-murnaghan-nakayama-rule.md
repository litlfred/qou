---
doc_id: arxiv-2104.06067v1
doc_title: "On irreducible characters of the Iwahori-Hecke algebra in type A"
section_id: sec-003-4-determinant-type-murnaghan-nakayama-rule
section_title: "Determinant type Murnaghan-Nakayama rule"
section_number: 4
pages: 12-17
source_pdf: 2104.06067v1.pdf
source_sha256: 750303181ca019ba
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.994
doc_brief: "On irreducible characters of the Iwahori-Hecke algebra in type A — We use vertex operators to compute irreducible characters of the Iwahori-Hecke algebra of type A."
---
The Murnaghan-Nakayama rule is an iterative formula to compute the Hecke algebra characters. The combinatorial rule was proved by Ram [@Ram] using the Frobenius formula and the Hall-Littlewood symmetric functions. In this section, we formulate a determinant type Murnaghan-Nakayama rule and use it to compute the characters and also give a new proof of the Murnaghan-Nakayama rule.

For two partitions $\mu\subset\lambda,$ the set-theoretic difference $\theta=\lambda-\mu$ is called a *skew diagram* denoted by $\lambda/\mu$. A subset $\xi$ of $\theta$ is connected if any two squares in $\theta$ are connected by a path in $\xi$. The connected components, themselves skew diagrams, are by definition the maximal connected subsets of $\theta$. A skew diagram $\lambda/\mu$ is a vertical (resp. horizontal) strip if each row (resp. column) contains at most one box. A skew diagram $\theta$ is a *border strip* if it contains no $2\times 2$ blocks of squares and is connected (see [@Mac]). If the border strip $\theta=\lambda-\mu$ has $m$ connected components $(\xi_1,\xi_2,\ldots,\xi_m)$, we define the weight of $\theta$ by $$wt(\theta;t)= (t-1)^{m-1}\prod\limits_{i=1}^{m}(-1)^{r(\xi_{i})-1}t^{c(\xi_i)-1}.$$ where the $r(\xi_i)$ (resp. $c(\xi_i)$) means the number of rows (resp. columns) in the border strip $\xi_i$. Usually we refer $\theta$ as a broken border strip to emphasize the non-connectedness of $\theta$.

Let $\lambda\vdash n$. A Young tableau of shape $\lambda$ is an assignment of numbers $1,2,\ldots,n$ into the dots of the Young diagram.

A tableau is *standard* if its rows and columns are increasing sequences. Let $f^{\lambda}$ be the number of standard tableau of shape $\lambda$ and let $\lambda^{-}$ be a partition obtained by removing an inner corner of $\lambda,$ then [@Sag] $$\begin{aligned}
\label{e:branch}
f^{\lambda}=\sum\limits_{\lambda^{-}}f^{\lambda^{-}}.
\end{aligned}$$

Recall from [\[e:qS\]](#e:qS){reference-type="eqref" reference="e:qS"}, for a fixed partition $\lambda$ with $l=l(\lambda)$ we have that $$\begin{aligned}
\label{e:qS2}
q^*_{k}S_{\lambda}.1=\sum_{\mbox{\tiny$\begin{array}{c}
\tau_1,\ldots, \tau_l\geq0\\
|\tau|=k\end{array}$}}(1-t)^{l-\sum\delta_{\tau_i,0}}S_{\lambda-\tau}.1.
\end{aligned}$$

For any composition $\tau\vDash k$, $S_{\lambda-\tau}.1=sg(\sigma)S_{\mu}.1$ if $\lambda-\tau+\delta$ is strict and $\mu=\sigma(\lambda-\tau+\delta)-\delta$ for some permutation $\sigma\in \mathfrak S_l$, otherwise $S_{\lambda-\tau}.1=0$. Note that $\mu$ must be a partition $\subset\lambda$ with weight $|\lambda|-k$ if $S_{\lambda-\tau}.1\neq 0$.

In fact, note that $\mu_i=\lambda_{\sigma(i)}-\tau_{\sigma(i)}+i-\sigma(i)$ for some permutation $\sigma$ that sends $\lambda-\tau+\delta$ into partition $\mu$. If $j=\sigma(i)\geq i$, then $\lambda_i-\mu_i=\lambda_i-\lambda_j+\tau_j-i+j\geq 0$. If $j=\sigma(i)<i$, we claim that $\lambda_i-\mu_i\geq 0$ otherwise $\lambda_i-\mu_i=\lambda_i-\lambda_j+\tau_j-i+j<0$, then $$(\lambda_j-\tau_j, \lambda_{j+1}-\tau_{j+1}, \ldots, \lambda_i-\tau_i)+(i-j, \ldots, 1, 0)=(\lambda_j-\tau_j+i-j, \ldots, \lambda_i-\tau_i).$$ Observe that $(\lambda_i-\tau_i)-(\lambda_j-\tau_j+i-j)<0$ so $\sigma$ cannot send $i$ to $j$, which is a contradiction!

Conversely, for any $\mu\vdash |\lambda|-k$ and any $\sigma\in \mathfrak S_l$, the $l$-tuple $$(\lambda_1-\mu_{\sigma(1)}-1+\sigma(1), \lambda_2-\mu_{\sigma(2)}-2+\sigma(2), \cdots, \lambda_l-\mu_{\sigma(l)}-l+\sigma(l))$$ is a composition of $k$ provided that $\lambda_i-\mu_{\sigma(i)}+i-\sigma(i)\geq 0$. Then $sg(\sigma)S_{\mu}.1=S_{\lambda-\tau}.1$ for $\tau_i=\lambda_i-\mu_{\sigma(i)}-i+\sigma(i)$. Therefore [\[e:qS2\]](#e:qS2){reference-type="eqref" reference="e:qS2"} can be rewritten as: $$\begin{aligned}
q^*_{k}S_{\lambda}.1&=\sum\limits_{\mu}\sum_{\mbox{\tiny$\begin{array}{c}
\sigma\in  S_l\\
\lambda_i-i-\mu_{\sigma(i)}+\sigma(i)\geq 0\end{array}$}}sgn(\sigma)(1-t)^{l-\sum\delta_{\lambda_i-i-\mu_{\sigma(i)}+\sigma(i),0}}S_{\mu}.1\\
&=(1-t)^{l}\sum\limits_{\mu}\det(\delta_{\lambda_i-i\geq \mu_j-j}(1-t)^{-\delta_{\lambda_i-i, \mu_j-j}})S_{\mu}.1
\end{aligned}$$ where the sum is over all partitions $\mu\subset \lambda$ such that $\mid\lambda/\mu\mid=k$.

For partitions $\mu\subset\lambda$ and $|\lambda/\mu|=k$, consider the $l(\lambda)\times l(\lambda)$-matrix $$M(\lambda/\mu; t)=(\delta_{\lambda_i-i\geq\mu_j-j}(1-t)^{-\delta_{\lambda_i-i, \mu_j-j}})$$ where $\delta_{a\geq b}=1$ if $a\geq b$ and $\delta_{a\geq b}=0$ otherwise. Then we have proven the following theorem.

::: thm
Let $\lambda=(\lambda_{1},\ldots, \lambda_{l})$ be a partition and $k$ be a positive integer. Then one has $$\begin{aligned}
\label{e:de}
q^*_{k}S_{\lambda}.1=\sum\limits_{\mu}(1-t)^{l}\det M(\lambda/\mu; t)S_{\mu}.1
\end{aligned}$$ where the sum is over all partitions $\mu\subset \lambda$ such that $\mid\lambda/\mu\mid=k$.
:::

The matrix $M(\lambda/\mu; t)$ has the following properties: (i) if $M(\lambda/\mu; t)_{ij}=\frac1{1-t}$, then all entries in the southwest region to the $(i, j)$-entry are zero; (ii) if $M(\lambda/\mu; t)_{ij}=0$, then all entries down the $j$th column are also zero;

and (iii) if $M(\lambda/\mu; t)_{ij}=1$, then all entries in the northeast region to the $(i, j)$-entry are also $1$. et's divide $\lambda/\mu$ into several cases:

**Case $1:$** If $\lambda/\mu$ is a $k$-border strip with the initial box at the $r$th row, then $M(\lambda/\mu; t)$ has the following form: $$\begin{gathered}
\begin{pmatrix}
\frac1{1-t}  & \cdots & 1 & 1& 1 & \cdots & 1 & 1 \\
\vdots           & \ddots & \vdots  & \vdots & \vdots & \cdots & \vdots & \vdots \\
0 & \cdots & \frac1{1-t}  & 1 & 1 & \cdots & 1 & 1\\
0 & \cdots & 0 &  1  & 1 & \cdots & 1 & 1 \\
0 &\cdots & 0 & \frac{1}{1-t}  & 1 &\cdots & 1 &1\\
0 &\cdots & 0 &0 & \frac{1}{1-t} & \cdots & 1 &1\\
\vdots &\vdots & \vdots &\vdots &\vdots &\ddots &\vdots &\vdots\\
0 &\cdots & 0 & 0 &0 &\cdots &\frac{1}{1-t} &1
\end{pmatrix}_{l\times l}
=\begin{pmatrix}M_0 & * \\
 0 & M_1
\end{pmatrix}, \\
\det(\lambda/\mu;k)=(1-t)^{-r+1}(\frac{-t}{1-t})^{l-r}
\end{gathered}$$ where $M_0$ is an $(r-1)\times (r-1)$ upper-triangular matrix with $\frac1{1-t}$ on the diagonal and $M_1$ is a $(l-r+1)\times (l-r+1)$ quasi upper-triangular matrix with $1$ on the diagonal and $\frac1{1-t}$ on the (lower) secondary diagonal. For simplicity we denote $M_1$ by $M(\xi; t)$, where $\xi$ is the border strip obtained from $\lambda/\mu$ by removing the initial empty boxes.

**Case $2:$** If $\lambda/\mu$ is connected and contains a $2 \times 2$ block of boxes, then $\det(\lambda/\mu; t)=0$. This can be seen as follows. Without loss of generality, suppose $ht(\lambda/\mu)=l(\lambda)-1$ and the $2 \times 2$ block appear at the $r$-th and $(r+1)$-th rows $(1\leq r\leq l-1)$, then $M(\lambda/\mu; t)$ has the following form: $$\begin{gathered}
M(\lambda/\mu;t)=
\bordermatrix{
& & & &r-1 &r & & & \cr
&1  &1 &\cdots &1 &1 &\cdots &1 &1\cr
&\frac{1}{1-t}  &1 &\cdots &1 &1 &\cdots &1 &1\cr
&0 &\frac{1}{1-t} &\cdots &1 &1 &\cdots &1 &1\cr
&\vdots &\vdots &\ddots &\vdots &\vdots &\ddots &\vdots &\vdots\cr
r &0 &0 &\cdots &\frac{1}{1-t} &1 &\cdots &1 &1\cr
r+1 &0 &0 &\cdots &0 &1 &\cdots &1 &1\cr
&\vdots &\vdots &\ddots &\vdots &\vdots &\ddots &\vdots &\vdots\cr
&0 &0 &0 &0 &0 &\cdots &\frac{1}{1-t} &1
}, \quad \det(\lambda/\mu;t)=0.
\end{gathered}$$

**Case $3:$** If $\lambda/\mu$ has two connected components $\xi_1, \xi_2$, then $M(\lambda/\mu; t)$ is a $2\times 2$ upper-triangular block matrix with the diagonal blocks corresponding to $\xi_1, \xi_2$. If one of the components contains a $2\times 2$-block of boxes, then $\det(\lambda/\mu; t)=0$. Suppose each $\xi_i$ is a border strip and there are $r_i$ unoccupied rows immediately above $\xi_i$ on the border of $\lambda$, then $M(\lambda/\mu; t)$ has the following form: $$\begin{gathered}
M(\lambda/\mu; t)=\begin{pmatrix}M_1 & * \\
 0 & M_2
\end{pmatrix}, \qquad \det M_i=(1-t)^{-r_i+1}(\frac{-t}{1-t})^{ht(\xi_i)-1},
\end{gathered}$$ where each $M_i$ is a $2\times 2$ block diagonal matrices specified in case one.

In general, if $\lambda/\mu$ has $m$ connected components $\xi_1, \xi_2,\cdots,\xi_m$, then $\det M(\lambda/\mu; t)=0$ unless each $\xi_i$ is a border strip. Then $$\begin{gathered}
M(\lambda/\mu;t)=
\begin{pmatrix}
M_1  &* &\cdots &*\\
0  &M_2 &\cdots &*\\
0 &\vdots &\cdots &\vdots\\
0 &0 &\vdots &M_s
\end{pmatrix}
\end{gathered}$$ where the diagonal blocks are either $\frac{1}{1-t}$ or the quasi upper-triangular matrix $M(\xi_j;t)$, $i=1,2,\ldots,s; j=1,2\ldots,m$. It is clear that the number of $\frac1{1-t}$ on the diagonal is equal to $Card\{\lambda_i=\mu_i\mid i=1,\ldots,l\}=l-\sum\limits_{j} r(\xi_j)$ and the order of $M(\xi_j;k)$ is equal to $r(\xi_j), j=1,2, \ldots, m$. Therefore,

$$\begin{aligned}
\det(\lambda/\mu;t)&=(\frac{1}{1-t})^{l-\sum r(\xi_i)}\prod\limits_{i=1}^{m}\det(\xi_{i};t)\\
&=(\frac{1}{1-t})^{l-\sum r(\xi_i)}\prod\limits_{i=1}^{m}(\frac{-t}{1-t})^{r(\xi_i)-1}\\
&=(1-t)^{m-l}\prod\limits_{i=1}^{m}(-t)^{r(\xi_i)-1}.
\end{aligned}$$ Thus we have proved the following result.

::: cor
[]{#t:det label="t:det"} Let $\lambda$ be a partition and $k$ a positive integer. Then one has that $$\begin{aligned}
q^*_{k}S_{\lambda}.1=\sum\limits_{\mu}(1-t)^{C(\lambda/\mu)}\prod\limits_{i=1}^{C(\lambda/\mu)}(-t)^{r(\xi_i)-1}S_{\mu}.1
\end{aligned}$$ where the sum runs through all partitions $\mu\subset \lambda$ such that $\lambda/\mu$ is a $k$-broken border strip. Here $\xi_1,\ldots,\xi_{C(\lambda/\mu)}$ are the connected components of $\lambda/\mu$.
:::

::: rem
If $k=|\lambda|=n$ in Corollary [\[t:det\]](#t:det){reference-type="ref" reference="t:det"}, then $q^*_{k}S_{\lambda}.1=0$ unless $\lambda$ is a hook. In this case, $q^*_{n}S_{(m,1^{n-m})}.1=(1-t)(-t)^{n-m}$. So for all $\lambda\vdash n\geq1$, $$\begin{aligned}
g^{\lambda}_{(n)}(t)=
\begin{cases}
0,&\text{if $\lambda$ is not a hook}\\
(1-t)(-t)^{n-m},&\text{if $\lambda=(m,1^{n-m})$}.
\end{cases}
\end{aligned}$$ Similarly, when $k=1$, then $q^*_1S_{\lambda}.1=(1-t)\sum\limits_{\lambda^{-}}S_{\lambda^{-}}.1$, where

$\lambda^{-}$ runs through all partitions obtained from $\lambda$ by removing an inner corner. Therefore, $$\begin{aligned}
g^{\lambda}_{(1^n)}(t)=(1-t)\sum\limits_{\lambda^{-}}g^{\lambda^{-}}_{(1^{n-1})}(t).
\end{aligned}$$ By [\[e:branch\]](#e:branch){reference-type="eqref" reference="e:branch"} it follows that, $$\begin{aligned}
g^{\lambda}_{(1^n)}(t)=(1-t)^nf^{\lambda}
\end{aligned}$$ where $f^{\lambda}$ is the number of standard tableau of shape $\lambda$.
:::

We now present a new proof of the Murnaghan-Nakayama rule for $H_n(q)$ [@Ram] (cf. [@HR; @Ha]).

::: thm
**(The Murnaghan-Nakayama rule for $H_n(q)$)**[]{#t:M-N rule label="t:M-N rule"} Let $\mu$ be a partition and $k$ a positive integer. Then one has that $$\begin{aligned}
\tilde{q}_{k}S_{\mu}.1=\sum\limits_{\lambda}wt(\lambda/\mu;q)S_{\lambda}.1,
\end{aligned}$$ where the sum is over all partitions $\lambda\supset\mu$ such that $\lambda/\mu$ is a $k$-broken border strip.
:::

::: proof
*Proof.* By Corollary [\[t:det\]](#t:det){reference-type="ref" reference="t:det"} and duality, it is enough to check that $$\begin{aligned}
(1-t)^{m}\prod\limits_{i=1}^{m}(-t)^{r(\xi_i)-1}=t^{k-1}(1-t)wt(\lambda/\mu;t)
\end{aligned}$$ where $\lambda/\mu$ is a $k$-broken border strip with $m$ connected components $\xi_1,\ldots,\xi_m$. Suppose $\mid\xi_i\mid=k_i,$ then $\sum_i k_i=k.$ Since $\xi_i$ is a border strip, $r(\xi_i)+c(\xi_i)=k_i+1$, $i=1,2,\ldots, m$. Therefore, $$\begin{aligned}
t^{k-1}(1-t)wt(\lambda/\mu;t)&=(1-t)^mt^{k-m}\prod\limits_{i=1}^{m}(-1)^{r(\xi_i)-1}t^{1-c(\xi_i)}\\
&=(1-t)^m\prod\limits_{i=1}^{m}(-1)^{r(\xi_i)-1}t^{k_i-c(\xi_i)}\\
&=(1-t)^{m}\prod\limits_{i=1}^{m}(-t)^{r(\xi_i)-1}.
\end{aligned}$$ ◻
:::
