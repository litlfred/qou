---
doc_id: arxiv-1710.04865v2
doc_title: "THE COLORED JONES POL YNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS"
section_id: sec-001-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 6-12
source_pdf: 1710.04865v2.pdf
source_sha256: ac8f436173d550e8
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.872
doc_brief: "THE COLORED JONES POLYNOMIAL AND KONTSEVICH-ZAGIER SERIES FOR DOUBLE TWIST KNOTS — Using a result of Takata, we prove a formula for the colored Jones polynomial of the double twist knots K(−m,−p) and"
duplicate_of: "cjdoubletwistfinal"
---
We begin by recalling the setup from [@takata]. Let $l$ and $t$ be coprime odd integers with $l > t \geq 1$ and $p^{\prime} := \frac{l-1}{2}$. For $1 \leq j \leq p^{\prime}$, define integers $r(j)$ such that $r(j) \equiv (2j-1)t \pmod{2l}$ and $-l < r(j) < l$. We put $\sigma_j := (-1)^{\lfloor \frac{(2j-1)t}{l}\rfloor}$, $r^{\prime}(j) := \frac{\mid r(j) \mid + 1}{2}$ and $i_{r^{\prime}(j)}=j$ (and thus $i_k = j$ if and only if $r^{\prime}(j)=k$). For an integer $i$, sgn($i$) denotes the sign of $i$. Let $\underline{n} = (n_1, \dotsc, n_{p^{\prime}})$ and $n_s=0$ for $s \leq 0$. Finally, define

$$\begin{equation}
 \label{kappa}
\kappa(p^{\prime})= \left\{
\begin{array}{ll}
-Nn_{p^{\prime}} & \text{if $\sigma_{p^{\prime}}=-1$,} \\
0 & \text{if $\sigma_{p^{\prime}}=1$} \\
\end{array} \right. \\
\end{equation}$$

and

$$\begin{equation}
 \label{tau}
\tau(j) = \left\{
\begin{array}{ll}
(-1)^{n_j - n_{j-1}} & \text{if $\sigma_j=-1$,} \\
q^{\binom{n_j - n_{j-1} + 1}{2}} & \text{if $\sigma_{j}=1$.} \\
\end{array} \right. \\
\end{equation}$$

Consider the family of 2-bridge knots $\frak{b}(l,t)$ [@bz]. The main result in [@takata] is an explicit formula for the colored Jones polynomial of $\frak{b}(l,t)^{*}$.

::: theorem
[]{#takata label="takata"} We have $$\begin{equation}
 \label{spt}
J_N(\frak{b}(l,t)^{*}; q) = \sum_{N-1 \geq n_{p^{\prime}} \geq \dotsc \geq n_1 \geq 0} q^{a({\underline{n}})N + b_1(\underline{n}) + b_2(\underline{n})} X(\underline{n})
\end{equation}$$ where[^1] $$\begin{equation*}
\begin{aligned}
a({\underline{n}}) & = -\frac{1}{2} \sum_{j=1}^{p^{\prime}} \Biggl( \sum_{k=r^{\prime}(j)}^{p^{\prime}} (\sigma_{i_k} + \sigma_{i_{p^{\prime} + 1 -k}})\Biggr) (n_j - n_{j-1}) - \frac{1}{2} \sum_{j=1}^{p^{\prime} - 1} (\sigma_{j+1} + \sigma_{p^{\prime} + 1 - j}) n_j \\
& - \frac{1}{2} (\sigma_{p^{\prime}} + 1) n_{p^{\prime}} - \sum_{j=1}^{p^{\prime}} \sigma_j, \\
b_1(\underline{n}) & = - a({\underline{n}}) + \sum_{k=1}^{\frac{l-t}{2}} \frac{1-\sigma_{i_k}}{2} n_{i_k - 1} - \sum_{k=\frac{l-t}{2}+1}^{p^{\prime}} n_{i_k - 1} + \sum_{k=\frac{l-t}{2}+1}^{p^{\prime}} \frac{1+\sigma_{i_k}}{2} n_{i_k} - (1+\sigma_{p^{\prime}}) n_{p^{\prime}} \\
& + \frac{1}{2} \sum_{j=1}^{p^{\prime} - 1} (\sigma_{j+1} - \sigma_j) n_j \\
& - \frac{1}{2} \sum_{k=1}^{p^{\prime} - 1} \sum_{k^{\prime} = k+1}^{p^{\prime}} \frac{1 + \operatorname{sgn}(i_k - i_{k^{\prime}})}{2}(\sigma_{i_k} - \sigma_{i_{k^{\prime}}})(n_{i_k} - n_{i_k - 1})(n_{i_{k^{\prime}}} - n_{i_{k^{\prime}} - 1}) \\
& + \sum_{j=1}^{p^{\prime}} \sigma_j \Bigl( \sum_{k=1}^{r^{\prime}(j)} (n_{i_k} - n_{i_k - 1}) \Bigr) n_{j-1}, \\
b_2(\underline{n}) & = \left\{
\begin{array}{ll}
\displaystyle \sum_{k=\frac{l-t}{2} + 1}^{\frac{t-1}{2}} \frac{1+ \sigma_{i_k}}{2} n_{i_k - 1} & \text{if $l < 2t$} \\
\displaystyle - \sum_{k=\frac{t+1}{2} + 1}^{\frac{l-t}{2}} \frac{1+ \sigma_{i_k}}{2} n_{i_k - 1} & \text{if $l > 2t,$} \\
\end{array} \right. \\
X(\underline{n}) & = (-1)^{n_{p^{\prime}}} q^{\kappa(p^{\prime})} \frac{(q)_{N-1} (q)_{n_{p^{\prime}}}}{(q)_{N-n_{p^{\prime}} - 1}} \prod_{j=1}^{p^{\prime}} \frac{\tau(j)}{(q)_{n_j - n_{j-1}}}.
\end{aligned}
\end{equation*}$$
:::

As the mirror image of the torus knots $T_{(2, 2t+1)}$ is $\frak{b}(2t+1, 1)$ (cf. [@bz; @petersen; @Tran]), one can check that Theorem [\[takata\]](#takata){reference-type="ref" reference="takata"} recovers the $q$-hypergeometric expression for $J_N(T_{(2, 2t+1)}; q)$ given in [@hikami1; @hikami2]. Our interest will be to apply Theorem [\[takata\]](#takata){reference-type="ref" reference="takata"} to the case of the double twist knots $K_{(m, p)} = \frak{b}(4mp-1, 4mp-2p-1)$ and $K_{(m,-p)}=\frak{b}(4mp+1, 4mp-2p+1)$ (cf. [@Tran]). In order to facilitate these computations, we need the following results concerning $\sigma_j$, $i_k$ and $\sigma_{i_k}$. We omit the proofs as they are straightforward generalizations of Lemmas 6--9 in [@takata].

::: lemma
[]{#l8 label="l8"} For $l=4mp-1$ and $t=4mp-2p-1$, we have\

1.  $\sigma_{j} = \left\{
    \begin{array}{ll}
    1 & \text{if $j \equiv 1, 2, \dotsc, m \pmod{2m}$} \\
    -1 & \text{if $j \equiv 0, m+1, \dotsc, 2m-1 \pmod{2m}.$} \\
    \end{array} \right.$\

2.  To compute $i_k$, apply the following algorithm. Divide the integers from $1$ to $p'$ into $2m-1$ intervals, each of length $p$, and a final interval of length $p -1$. The value of $i_k$ is $2m(p-k) + m$ in the first interval and $1- (2m(p-k) + m)$ in the second. If $j>1$ is odd, then to obtain the value of $i_k$ in the $j$th interval, add $4mp- 1$ to the formula for $i_k$ in the $(j-2)$th interval. If $j > 2$ is even, then to obtain the value of $i_k$ in the $j$th interval, subtract $4mp - 1$ from the formula for $i_k$ in the $(j-2)$th interval.\

3.  To compute $\sigma_{i_k}$, apply the following algorithm. Divide the integers from $1$ to $p'$ into $2m-1$ intervals, each of length $p$, and a final interval of length $p - 1$. The value of $\sigma_{i_k}$ alternates between $1$ and $-1$ starting with $1$ in the first interval.
:::

::: lemma
[]{#l9 label="l9"} Let $l=4mp-1$ and $t=4mp-2p-1$. Then for $1\leq k \leq p'$ and $1\leq j \leq p'-1$ we have\

1.  $\sigma_{i_k} + \sigma_{i_{p^{\prime} + 1 - k}} = \left\{
    \begin{array}{ll}
    2 & \text{if $k = p, 3p, \dotsc, (2m-1)p$} \\
    -2 & \text{if $k = 2p, \dotsc, (2m-2)p$} \\
    0 & \text{otherwise.} \\
    \end{array} \right.$\

2.  $\sigma_{j+1} + \sigma_{p^{\prime} + 1 - j} = 0$.
:::

::: lemma
[]{#l6 label="l6"} For $l=4mp + 1$ and $t=4mp - 2p + 1$, we have\

1.  $\sigma_{j} = \left\{
    \begin{array}{ll}
    1 & \text{if $j \equiv 1, 2, \dotsc, m \pmod{2m}$} \\
    -1 & \text{if $j \equiv 0, m+1, \dotsc, 2m-1 \pmod{2m}.$} \\
    \end{array} \right.$\

2.  To compute $i_k$, apply the following algorithm. Divide the integers from $1$ to $p'$ into $2m$ intervals of length $p$. The value of $i_k$ is $2m(p-k) + m + 1$ in the first interval and $1- (2m(p-k) + m + 1)$ in the second. If $j>1$ is odd, then to obtain the value of $i_k$ in the $j$th interval, add $4mp+1$ to the formula for $i_k$ in the $(j-2)$th interval. If $j > 2$ is even, then to obtain the value of $i_k$ in the $j$th interval, subtract $4mp+1$ from the formula for $i_k$ in the $(j-2)$th interval.\

3.  To compute $\sigma_{i_k}$, apply the following algorithm. Divide the integers from 1 to $p'$ into $2m$ intervals of length $p$. The value of $\sigma_{i_k}$ alternates between $-1$ and $1$ starting with $-1$ in the first interval.
:::

::: lemma
[]{#l7 label="l7"} Let $l=4mp + 1$ and $t=4mp - 2p + 1$. Then for $1\leq k \leq p'$ and $1\leq j \leq p'-1$ we have\

1.  $\sigma_{i_k} + \sigma_{i_{p^{\prime} + 1 - k}} = 0$\

2.  $\sigma_{j+1} + \sigma_{p^{\prime} + 1 - j} =  \left\{
    \begin{array}{ll}
    2 & \text{if $j \equiv 0 \pmod{2m}$} \\
    -2 & \text{if $j \equiv m \pmod{2m}$} \\
    0 & \text{otherwise.} \\
    \end{array} \right.$\
:::

We now illustrate the computation of $a({\underline{n}})$ and $b_1({\underline{n}}) + b_2({\underline{n}})$ for $l=8p-1$ and $t=6p-1$. The routine evaluation of $X(\underline{n})$ is left to the reader. First, we take $m=2$ in Lemmas [\[l8\]](#l8){reference-type="ref" reference="l8"} and [\[l9\]](#l9){reference-type="ref" reference="l9"} to obtain

$$\begin{equation}
 \label{step0}
\sigma_{j} = \left\{
\begin{array}{ll}
1 & \text{if $j \equiv 1, 2 \pmod{4}$} \\
-1 & \text{if $j \equiv 0, 3 \pmod{4},$} \\
\end{array} \right. \\
\end{equation}$$

$$\begin{equation}
 \label{step1}
i_k = \left\{
\begin{array}{ll}
4(p-k) + 2 & \text{if $1 \leq k \leq p$,} \\
4(k-p) - 1 & \text{if $p+1 \leq k \leq 2p$,} \\
12p - 4k + 1 & \text{if $2p+1 \leq k \leq 3p$,} \\
 4k - 12p & \text{if $3p+1 \leq k \leq 4p-1$,} \\
\end{array} \right. \\
\end{equation}$$

$$\begin{equation}
 \label{step2}
\sigma_{i_k} = \left\{
\begin{array}{ll}
1 & \text{if $1 \leq k \leq p$,} \\
-1 & \text{if $p+1 \leq k \leq 2p$,} \\
1 & \text{if $2p+1 \leq k \leq 3p$,} \\
 -1 & \text{if $3p+1 \leq k \leq 4p-1,$} \\
\end{array} \right. \\
\end{equation}$$

$$\begin{equation}
 \label{step3}
\sigma_{i_k} + \sigma_{i_{4p-k}} = \left\{
\begin{array}{ll}
2 & \text{if $k = p, 3p$} \\
-2 & \text{if $k = 2p$} \\
0 & \text{otherwise} \\
\end{array} \right. \\
\end{equation}$$ and $$\begin{equation}
 \label{step4}
\sigma_{j+1} + \sigma_{4p - j} = 0.
\end{equation}$$

Applying ([\[step0\]](#step0){reference-type="ref" reference="step0"}), ([\[step1\]](#step1){reference-type="ref" reference="step1"}), ([\[step3\]](#step3){reference-type="ref" reference="step3"}), ([\[step4\]](#step4){reference-type="ref" reference="step4"}) and reindexing yields

$$\begin{equation}
 \label{a}
\begin{aligned}
a({\underline{n}}) & = -\frac{1}{2} \sum_{j=1}^{4p-1} \Biggl( \sum_{k=r^{\prime}(j)}^{4p-1} (\sigma_{i_k} + \sigma_{i_{4p - k}})\Biggr) (n_j - n_{j-1}) - 1 \\
& = -\frac{1}{2} \Biggl[ \sum_{j=1}^{p}  \Biggl( \sum_{k=3p-j+1}^{4p-1} (\sigma_{i_k} + \sigma_{i_{4p -k}})\Biggr) (n_{4j-3} - n_{4j-4}) \\
&  + \sum_{j=1}^{p} \Biggl( \sum_{k=p-j+1}^{4p-1} (\sigma_{i_k} + \sigma_{i_{4p -k}})\Biggr) (n_{4j-2} - n_{4j-3}) + \sum_{j=1}^{p-1} \Biggl( \sum_{k=3p+j}^{4p-1} (\sigma_{i_k} + \sigma_{i_{4p -k}})\Biggr) (n_{4j} - n_{4j-1}) \\
& + \sum_{j=1}^{p} \Biggl( \sum_{k=p+j}^{4p-1} (\sigma_{i_k} + \sigma_{i_{4p -k}})\Biggr) (n_{4j-1} - n_{4j-2}) \Biggr] - 1 \\
& = \sum_{j=1}^{2p-1} (-1)^j n_{2j} - 1.
\end{aligned}
\end{equation}$$

By ([\[step0\]](#step0){reference-type="ref" reference="step0"}) and ([\[step2\]](#step2){reference-type="ref" reference="step2"}), the second and fifth sums in $b_1({\underline{n}})$ are zero. We then use ([\[step0\]](#step0){reference-type="ref" reference="step0"})--([\[step2\]](#step2){reference-type="ref" reference="step2"}) and reindex to obtain

$$\begin{equation}
 \label{thirdpart}
\begin{aligned}
-\sum_{k=p+1}^{4p-1} n_{i_{k} - 1} & = - \Biggl( \sum_{k=p+1}^{2p} n_{i_{k} - 1} + \sum_{k=2p+1}^{3p} n_{i_{k} - 1} + \sum_{k=3p+1}^{4p-1} n_{i_{k} - 1} \Biggr) \\
& = - \Biggl( \sum_{j=1}^{p} (n_{4j-2} + n_{4j-4}) + \sum_{j-1}^{p-1} n_{4j-1} \Biggr),
\end{aligned}
\end{equation}$$

$$\begin{equation}
 \label{fourthpart}
\sum_{k=p+1}^{4p-1} \frac{1+\sigma_{i_k}}{2} n_{i_k} = \sum_{k=2p+1}^{3p} n_{i_k} = \sum_{j=1}^{p} {n_{4j-3}},
\end{equation}$$

$$\begin{equation}
 \label{sixthpart}
\frac{1}{2} \sum_{j=1}^{4p-2} (\sigma_{j+1} - \sigma_j) n_j = \sum_{j=1}^{2p-1} (-1)^j n_{2j}
\end{equation}$$ and $$\begin{equation}
 \label{b2}
b_2({\underline{n}}) = \sum_{k=p+1}^{3p-1} \frac{1+\sigma_{i_k}}{2} n_{{i_k} - 1} = \sum_{k=2p+1}^{3p-1} n_{{i_k} - 1} = \sum_{j=2}^{p} n_{4j-4}.
\end{equation}$$ By ([\[a\]](#a){reference-type="ref" reference="a"})--([\[b2\]](#b2){reference-type="ref" reference="b2"}), the sum of $b_2({\underline{n}})$ and the first six terms in $b_1({\underline{n}})$ equals

$$\begin{equation}
 \label{sixb1b2}
1 + n_{4p-1}  + \sum_{j=1}^{p} (n_{4j-3} - n_{4j-2} - n_{4j-1}).
\end{equation}$$

To compute the seventh term in $b_1({\underline{n}})$, we use ([\[step1\]](#step1){reference-type="ref" reference="step1"}) and ([\[step2\]](#step2){reference-type="ref" reference="step2"}) to observe that $k < k^{\prime}$ and $\sigma_{i_k} \neq \sigma_{i_{k^{\prime}}}$ if and only if either $1 \leq k \leq p$ and $p+1 \leq k^{\prime} \leq 2p$ or $1 \leq k \leq p$ and $3p+1 \leq k^{\prime} \leq 4p-1$ or $p+1 \leq k \leq 2p$ and $2p+1 \leq k^{\prime} \leq 3p$ or $2p+1 \leq k \leq 3p$ and $3p+1 \leq k^{\prime} \leq 4p-1$. Also, $\operatorname{sgn}(i_k - i_{k^{\prime}}) = 1$ if and only if $i_k > i_{k^{\prime}}$ and either $i_k = 4p-4k+2$ for $1 \leq k \leq p$ and $i_{k^{\prime}} = 4k^{\prime} - 4p - 1$ for $p+1 \leq k^{\prime} \leq 2p$ or $i_k = 4p-4k+2$ for $1 \leq k \leq p$ and $i_{k^{\prime}} = 4k^{\prime} -12p$ for $3p+1 \leq k^{\prime} \leq 4p-1$ or $i_k = 4k-4p-1$ for $p+1 \leq k \leq 2p$ and $i_{k^{\prime}} = 12p - 4k^{\prime} + 1$ for $2p+1 \leq k^{\prime} \leq 3p$ or $i_k = 12p - 4k + 1$ for $2p+1 \leq k \leq 3p$ and $i_{k^{\prime}} = 4k^{\prime} - 12p$ for $3p+1 \leq k^{\prime} \leq 4p-1$. Taking these cases into account and reindexing, we have

$$\begin{equation*}
\begin{aligned}
& - \frac{1}{2} \sum_{k=1}^{4p-2} \sum_{k^{\prime} = k+1}^{4p-1} \frac{1 + \operatorname{sgn}(i_k - i_{k^{\prime}})}{2}(\sigma_{i_k} - \sigma_{i_{k^{\prime}}})(n_{i_k} - n_{i_k - 1})(n_{i_{k^{\prime}}} - n_{i_{k^{\prime}} - 1}) \\
& = - \sum_{k=1}^{p} \sum_{k^{\prime} = p+1}^{2p-k} (n_{i_k} - n_{i_k - 1})(n_{i_{k^{\prime}}} - n_{i_{k^{\prime}} - 1}) - \sum_{k=1}^{p} \sum_{k^{\prime}=3p+1}^{4p-k} (n_{i_k} - n_{i_k - 1})(n_{i_{k^{\prime}}} - n_{i_{k^{\prime}} - 1}) \\
& + \sum_{k=p+1}^{2p} \sum_{k^{\prime} = 4p-k+1}^{3p} (n_{i_k} - n_{i_k - 1})(n_{i_{k^{\prime}}} - n_{i_{k^{\prime}} - 1}) - \sum_{k=2p+1}^{3p} \sum_{k^{\prime} = 3p+1}^{6p-k} (n_{i_k} - n_{i_k - 1})(n_{i_{k^{\prime}}} - n_{i_{k^{\prime}} - 1}) \\
& = - \sum_{j=1}^{p} \sum_{j^{\prime}=2}^{j} (n_{4j-2} - n_{4j-3})(n_{4j^{\prime} - 5} - n_{4j^{\prime} - 6}) - \sum_{j=1}^{p} \sum_{j^{\prime}=2}^{j} (n_{4j-2} - n_{4j-3})(n_{4j^{\prime} -4} - n_{4j^{\prime} - 5}) \\
\end{aligned}
\end{equation*}$$

$$\begin{equation}
  \label{sevenb1}
\begin{aligned}
& + \sum_{j=1}^{p} \sum_{j^{\prime} = 1}^{j} (n_{4j-1} - n_{4j-2})(n_{4j^{\prime} - 3} - n_{4j^{\prime} - 4}) - \sum_{j=1}^{p} \sum_{j^{\prime}=2}^{j} (n_{4j-3} - n_{4j-4})(n_{4j^{\prime}-4} - n_{4j^{\prime} - 5}).
\end{aligned}
\end{equation}$$

Finally, using ([\[step0\]](#step0){reference-type="ref" reference="step0"}) and ([\[step1\]](#step1){reference-type="ref" reference="step1"}), then reindexing and simplifying gives the eighth term in $b_1(\underline{n})$,

$$\begin{equation}
 \label{lastb1}
\begin{aligned}
& \sum_{j=1}^{4p-1} \sigma_j \Bigl( \sum_{k=1}^{r^{\prime}(j)} (n_{i_k} - n_{i_k - 1}) \Bigr) n_{j-1} \\
& = \sum_{j=1}^{p} \sigma_{4j-3} \Bigl( \sum_{k=1}^{3p-j+1} (n_{i_k} - n_{i_k - 1}) \Bigr) n_{4j-4} +  \sum_{j=1}^{p} \sigma_{4j-2} \Bigl( \sum_{k=1}^{p-j+1} (n_{i_k} - n_{i_k - 1}) \Bigr) n_{4j-3} \\
& +  \sum_{j=1}^{p-1} \sigma_{4j} \Bigl( \sum_{k=1}^{3p+j} (n_{i_k} - n_{i_k - 1}) \Bigr) n_{4j-1} +  \sum_{j=1}^{p} \sigma_{4j-1} \Bigl( \sum_{k=1}^{p+j} (n_{i_k} - n_{i_k - 1}) \Bigr) n_{4j-2} \\
& = \sum_{j=1}^{p} \Biggl( \sum_{k=1}^{p} (n_{4p-4k+2} - n_{4p-4k+1}) + \sum_{k=p+1}^{2p} (n_{4k-4p-1} - n_{4k-4p-2}) \\
& + \sum_{k=2p+1}^{3p-j+1} (n_{12p - 4k + 1} - n_{12p - 4k}) \Biggr) n_{4j-4} + \sum_{j=1}^{p} \Biggl( \sum_{k=1}^{p-j+1} (n_{4p-4k+2} - n_{4p-4k+1}) \Biggr) n_{4j-3} \\
& - \sum_{j=1}^{p-1} \Biggl( \sum_{k=1}^{p} (n_{4p-4k+2} - n_{4p-4k+1}) + \sum_{k=p+1}^{2p} (n_{4k-4p-1} - n_{4k-4p-2}) \\
& + \sum_{k=2p+1}^{3p} (n_{12p - 4k + 1} - n_{12p - 4k}) + \sum_{k=3p+1}^{3p+j} (n_{4k-12p} - n_{4k-12p-1}) \Biggr) n_{4j-1} \\
& - \sum_{j=1}^{p} \Biggl( \sum_{k=1}^{p} (n_{4p-4k+2} - n_{4p-4k+1}) + \sum_{k=p+1}^{p+j} (n_{4k-4p-1} - n_{4k-4p-2}) \Biggr) n_{4j-2} \\
& = \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=1}^{j-1} (n_{4j^{\prime} - 1} - n_{4j^{\prime} - 3}) + \sum_{j=j^{\prime}}^{p} (n_{4j^{\prime} - 1} - n_{4j^{\prime} - 4}) \Biggr) n_{4j-4} + \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime} = j}^{p} (n_{4j^{\prime} - 2} - n_{4j^{\prime} - 3} ) \Biggr) n_{4j-3} \\
& - \sum_{j=1}^{p-1} \Biggl( \sum_{j^{\prime} = j+1}^{p} (n_{4j^{\prime} - 1} - n_{4j^{\prime} - 4}) + n_{4j}\Biggr) n_{4j-1} \\
& - \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=1}^{j} (n_{4j^{\prime} - 1} - n_{4j^{\prime} - 3}) + \sum_{j^{\prime}=j+1}^{p} (n_{4j^{\prime} - 2} - n_{4j^{\prime} - 3}) \Biggr) n_{4j-2}.
\end{aligned}
\end{equation}$$

Thus, combining ([\[a\]](#a){reference-type="ref" reference="a"})--([\[lastb1\]](#lastb1){reference-type="ref" reference="lastb1"}) implies that $b_1({\underline{n}}) + b_2({\underline{n}})$ equals

$$\begin{equation*}
\begin{aligned}
& 1 + n_{4p-1}  + \sum_{j=1}^{p} (n_{4j-3} - n_{4j-2} - n_{4j-1}) \\
& - \sum_{j=1}^{p} \sum_{j^{\prime}=2}^{j} (n_{4j-2} - n_{4j-3})(n_{4j^{\prime} - 5} - n_{4j^{\prime} - 6}) - \sum_{j=1}^{p} \sum_{j^{\prime}=2}^{j} (n_{4j-2} - n_{4j-3})(n_{4j^{\prime} -4} - n_{4j^{\prime} - 5}) \\
& + \sum_{j=1}^{p} \sum_{j^{\prime} = 1}^{j} (n_{4j-1} - n_{4j-2})(n_{4j^{\prime} - 3} - n_{4j^{\prime} - 4}) - \sum_{j=1}^{p} \sum_{j^{\prime}=2}^{j} (n_{4j-3} - n_{4j-4})(n_{4j^{\prime}-4} - n_{4j^{\prime} - 5}) \\
& + \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=1}^{j-1} (n_{4j^{\prime} - 1} - n_{4j^{\prime} - 3}) + \sum_{j=j^{\prime}}^{p} (n_{4j^{\prime} - 1} - n_{4j^{\prime} - 4}) \Biggr) n_{4j-4} + \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime} = j}^{p} (n_{4j^{\prime} - 2} - n_{4j^{\prime} - 3} ) \Biggr) n_{4j-3} \\
& - \sum_{j=1}^{p-1} \Biggl( \sum_{j^{\prime} = j+1}^{p} (n_{4j^{\prime} - 1} - n_{4j^{\prime} - 4}) + n_{4j}\Biggr) n_{4j-1} \\
& - \sum_{j=1}^{p} \Biggl( \sum_{j^{\prime}=1}^{j} (n_{4j^{\prime} - 1} - n_{4j^{\prime} - 3}) + \sum_{j^{\prime}=j+1}^{p} (n_{4j^{\prime} - 2} - n_{4j^{\prime} - 3}) \Biggr) n_{4j-2}.
\end{aligned}
\end{equation*}$$

[^1]: Note that there is a misprint in the definition of $X(\underline{n})$ in [@takata]. Each $\overline{q}$ in the prefactor should be $q$.
