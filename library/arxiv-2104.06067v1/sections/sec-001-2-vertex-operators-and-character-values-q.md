---
doc_id: arxiv-2104.06067v1
doc_title: "On irreducible characters of the Iwahori-Hecke algebra in type A"
section_id: sec-001-2-vertex-operators-and-character-values-q
section_title: "Vertex operators and character values (q)"
section_number: 2
pages: 3-11
source_pdf: 2104.06067v1.pdf
source_sha256: 750303181ca019ba
toc_source: outline
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.976
doc_brief: "On irreducible characters of the Iwahori-Hecke algebra in type A — We use vertex operators to compute irreducible characters of the Iwahori-Hecke algebra of type A."
---
Let $\Lambda$ be the ring of symmetric functions in the $x_n$ ($n\in\mathbb N$) over the integers. In this paper we mostly work with the ring $\Lambda_F$ over the field $F=\mathbb Q(t)$ and view it as a graded ring under the natural degree.

The ring $\Lambda$ has several linear bases indexed by partitions. A *partition* $\lambda=(\lambda_1,\lambda_2,\ldots)$ is a weakly decreasing sequence of non-negative integers. The sum $|\lambda|=\sum_i\lambda_i$ is called the weight and the number of nonzero parts is called the length $l(\lambda)$. A partition $\lambda$ of weight $n$ is denoted by $\lambda \vdash n$, and the set of partitions is denoted by $\mathcal P$. When the parts of $\lambda$ are arranged in increasing order, so $\lambda=(1^{m_{1}}2^{m_{2}}\ldots)$ where $m_{i}=Card\{\lambda_{j}=i\mid 1\leq j\leq l(\lambda)\}$ is the multiplicity of $i$ in $\lambda$. $\lambda$ is called a *strict partition* if $m_i\leq 1$. When the finite sequence $\lambda=(\lambda_1,\lambda_2,\ldots)$ of nonnegative integers is an ordered or not necessarily weakly decreasing one such that $\sum_i\lambda_i=n$, $\lambda$ is called a *composition* of $n=\sum_i\lambda_i$, denoted as $\lambda\models n$. The length $l(\lambda)$ is the number of nonzero parts.

A partition $\lambda$ is visualized by its Young diagram: the set of nodes (or boxes situated at) $(i,j)\in \mathbb{Z}_+^{2}$ such that $1\leq j\leq \lambda_{i}$. If $\lambda$ is a diagram, then an inner corner of $\lambda$ is a node $(i,j)\in \lambda$ whose removal still leaves the diagram as that of a partition. The conjugate partition $\lambda'=(\lambda_1', \ldots, \lambda_{\lambda_1}')$ corresponds to the reflection of the Young diagram along the diagonal.

For each $r>1$, let $p_{r}=\sum x_{i}^{r}$ be the $r$th power-sum. Then $p_{\lambda}=p_{\lambda_{1}}p_{\lambda_{2}}\cdots p_{\lambda_{l}} (\lambda\in\mathcal P)$ form a $\mathbb Q$-basis of $\Lambda_{\mathbb Q}$. Let $s_{\lambda}$ be the Schur function associated with the partition $\lambda$, then $s_{\lambda}$'s form an orthonormal basis $\Lambda$ under the inner product $$\begin{aligned}
\label{e:inner}
\langle p_{\lambda}, p_{\mu}\rangle=\delta_{\lambda\mu}z_{\lambda}
\end{aligned}$$ where $z_{\lambda}=\prod_{i\geq 1}\lambda_im_i(\lambda)!$. The function $p_n$ acts on $\Lambda$ as a multiplication operator, and its

the dual operator is the differential operator $p_n^* =n\frac{\partial}{\partial p_n}$. Note that \* is $\mathbb Q(t)$-linear and anti-involutive satisfying $$\langle p_nu, v\rangle=\langle u, p_n^*v\rangle$$ for $u, v\in \Lambda$.

We now recall the vertex operator realization of the Schur symmetric functions [@Jing3]. Let

$S(z)$ and the dual vertex operator $S^*(z)$ be the linear maps: $\Lambda\longrightarrow \Lambda[[z, z^{-1}]]$ defined by $$\begin{aligned}
\label{e:Schurop}
S(z)&=\mbox{exp} \left( \sum\limits_{n\geq 1} \dfrac{1}{n}p_nz^{n} \right) \mbox{exp} \left( -\sum \limits_{n\geq 1} \frac{\partial}{\partial p_n}z^{-n} \right)=\sum_{n\in\mathbb Z}S_nz^{n},\\ \label{e:Schurop*}
S^*(z)&=\mbox{exp} \left(-\sum\limits_{n\geq 1} \dfrac{1}{n}p_nz^{n} \right) \mbox{exp} \left(\sum \limits_{n\geq 1} \frac{\partial}{\partial p_n}z^{-n} \right)=\sum_{n\in\mathbb Z}S^*_nz^{-n}.
\end{aligned}$$ We use the convention to index the components by their degrees. The operators $S_n \in \mathrm{End}(\Lambda)$ are the Bernstein vertex operators realizing the Schur functions. The dual operators $S_n^*\in \mathrm{End}(\Lambda)$, introduced in [@Jing1], also realize the Schur functions.

The following relations will be useful in our discussion.

::: prop
[@Jing1] (1) The components of $S(z)$ and $S^{*}(z)$ obey the following commutation relations: $$\begin{aligned}
\label{e:relation}
S_{m}S_{n}+S_{n-1}S_{m+1}&=0,\\
S^{*}_{m}S^{*}_{n}+S^{*}_{n+1}S^{*}_{m-1}&=0,\\
S_{m}S^{*}_{n}+S^{*}_{n-1}S_{m-1}&=\delta_{m,n}.
\end{aligned}$$ (2) For any composition $\mu=(\mu_{1},\ldots,\mu_{k})$, the product $S_{\mu_{1}}\cdots S_{\mu_{k}}.1=s_{\mu}$ is the

Schur function labeled by $\mu$. In general, $s_{\mu}=0$ or $\pm s_{\lambda}$ for a partition $\lambda$ such that $\lambda\in \mathfrak{S}_{l}(\mu+\delta)-\delta.$ Here $\delta=(l-1,l-2,\ldots,1,0),$ where $l = l(\mu)$. Moreover, $S_{-n}.1=\delta_{n,0}, S^{*}_{n}.1=\delta_{n,0}, (n\geq0)$.
:::

Let $q_{n}=q_{n}(x;t)$ be the generalized homogeneous symmetric function defined by $$\begin{aligned}
\label{e:qop}
Q(z)=\mbox{exp} \left( \sum\limits_{n=1}^{\infty}\frac{1-t^{n}}{n}p_{n}z^{n} \right)=\sum\limits_{n\geq0}q_{n}z^{n},
\end{aligned}$$ and $q_{n}=0$ if $n<0$. Denote $q_{\lambda}=q_{\lambda_{1}}q_{\lambda_{2}}\cdots q_{\lambda_{l}}$ for any partition $\lambda$, then the set $\{q_{\lambda}\}$ forms a basis of $\Lambda_{\mathbb{Q}(t)}$. Their dual operators with respect to the inner product [\[e:inner\]](#e:inner){reference-type="eqref" reference="e:inner"} are defined by $$\begin{aligned}
\label{e:qop*}
Q^{*}(z)=\mbox{exp} \left( \sum\limits_{n=1}^{\infty}(1-t^{n})\frac{\partial}{\partial p_{n}}z^{-n} \right)=\sum\limits_{n\geq0}q_{n}^{*}z^{-n},
\end{aligned}$$ and $q_n^*=0$ if $n<0$. In particular, $q^*_n.1=\delta_{n, 0}$ for $n\geq 0$.

For $n\geq0,$ by [\[e:qop\]](#e:qop){reference-type="eqref" reference="e:qop"} and [\[e:Schurop\*\]](#e:Schurop*){reference-type="eqref" reference="e:Schurop*"}, we have $$\begin{aligned}
q_{n}&=\sum\limits_{\lambda\vdash n}\frac{1}{z_{\lambda}(t)}p_{\lambda},\\
S^*_{-n}.1&=\sum\limits_{\lambda\vdash n}\frac{(-1)^{l(\lambda)}}{z_{\lambda}}p_{\lambda},
\end{aligned}$$ where $z_{\lambda}(t)=\prod\limits_{i\geq1}\frac{i^{m_{i}(\lambda)}m_{i}(\lambda)!}{1-t^{\lambda_{i}}},$ and $z_{\lambda}=z_{\lambda}(0).$

Let $H_n(q)$ be the Iwahori-Hecke algebra of type $A$ (see [\[e:Hecke1\]](#e:Hecke1){reference-type="eqref" reference="e:Hecke1"}-[\[e:Hecke3\]](#e:Hecke3){reference-type="eqref" reference="e:Hecke3"}).

Let $w=s_{i_1}\cdots s_{i_k}$ be a reduced expression of $w\in \mathfrak S_n$, where $s_i=(i,i+1)$. We define $T_w=T_{i_1}\cdots T_{i_k}$, which is well-defined and independent from the choice of reduced expressions. Then $H_n(q)$ has a linear basis consisting of $T_w$, $w\in \mathfrak S_n$.

For $\sigma_r=(12\cdots r)\in \mathfrak S_n$ in cycle notation, let $T_{\sigma_r}$ be the corresponding element in $H_n(q)$. For any composition $\mu=(\mu_1, \ldots, \mu_l)$ of $n$, let $\sigma_{\mu}=\sigma_{\mu_1}\times \cdots \times \sigma_{\mu_l}\in \mathfrak S_{\mu_1}\times \cdots\times \mathfrak S_{\mu_l}\hookrightarrow \mathfrak S_n$, we define $T_{\sigma_{\mu}}=T_{\sigma_{\mu_1}}\cdots T_{\sigma_{\mu_l}}$. Let $\phi: H_n(q)\longrightarrow \mathrm{End}(V)$ be an irreducible representation associated with partition $\lambda$. In general the character $\chi^{\lambda}(T)=\mathrm{Tr}(\phi(T))$ is no longer a function of conjugacy classes of $S_n$. However, it is known that all irreducible character values at elements $T_w$ are determined by their values at the element $T_{\sigma_{\mu}}$ [@GP]. For this reason, we will denote $\chi^{\lambda}(T_{\sigma_{\mu}})=\chi^{\lambda}_{\mu}(q)$.

Denote $\tilde{q}_{r}(t)=\frac{t^{r}}{t-1}q_{r}(t^{-1})$ and let $\tilde{q}_{\mu}(t)=\tilde{q}_{\mu_{1}}(t)\tilde{q}_{\mu_{2}}(t)\cdots\tilde{q}_{\mu_{l}}(t)=\frac{t^{|\mu|}}{(t-1)^{l(\mu)}}q_{\mu}(t^{-1}).$ We have the following Frobenius type formula for the characters of $H_{n}(q)$ from [@Ram].

::: prop
[@Ram] The irreducible character $\chi^{\lambda}$ of $H_{n}$ corresponding to $\lambda$ is determined by $$\begin{aligned}
\label{e:characters}
\tilde{q}_{\mu}(q)=\sum\limits_{\lambda\vdash n}\chi^{\lambda}_{\mu}(q)s_{\lambda}.
\end{aligned}$$ where $\mu\vdash n$ and $s_{\lambda}$ is the Schur function associated with partition $\lambda$.
:::

Therefore, $$\begin{aligned}
\label{e:chi}
\chi^{\lambda}_{\mu}(q)&=\langle \tilde{q}_{\mu}(q), s_{\lambda}\rangle
=\frac{q^{|\mu|}}{(q-1)^{l(\mu)}}\langle q_{\mu}(q^{-1}), S_{\lambda}.1\rangle,
\end{aligned}$$ and we are going to compute $g^{\lambda}_{\mu}(t):=\langle q_{\mu}(t), S_{\lambda}.1\rangle$ in the following.

::: prop
[]{#Up Down label="Up Down"} For any $m\in\mathbb Z_+, n\in\mathbb{Z}$ $$\begin{aligned}
\label{e:com1}
S^{*}_{n}q_{m}=q_{m}S^{*}_{n}+(1-t)\sum\limits_{k=1}^{m}q_{m-k}S^*_{n-k},\\ \label{e:com2}
q^{*}_{m}S_{n}=S_{n}q^{*}_{m}+(1-t)\sum\limits_{k=1}^{m}S_{n-k}q^*_{m-k}.
\end{aligned}$$
:::

::: proof
*Proof.* The usual vertex operator calculus gives that $$\begin{aligned}
\label{e:relations1}
S^*(z)Q(w)&=Q(w)S^*(z)\frac{z-tw}{z-w},
\\ \label{e:relations2}
Q^{*}(w)S(z)&=S(z)Q^{*}(w)\frac{w-tz}{w-z},
\end{aligned}$$ where the rational functions are expanded at $w=0$ and $z=0$ respectively. The relations then follow by comparing coefficients of $z^{-n}w^{m}$ in [\[e:relations1\]](#e:relations1){reference-type="eqref" reference="e:relations1"} and $z^{n}w^{-m}$ in [\[e:relations2\]](#e:relations2){reference-type="eqref" reference="e:relations2"} respectively. ◻
:::

For two compositions $\lambda,\mu,$ we say $\lambda\subset \mu$ if $\lambda_{i}\leq \mu_{i}$ for all $i\geq1$. In this case, we write $\lambda-\mu=(\lambda_{1}-\mu_{1},\lambda_{2}-\mu_{2},\ldots)\vDash |\lambda|-|\mu|$. For each partition $\lambda=(\lambda_1, \ldots, \lambda_l)$, we define that $$\begin{aligned}
\lambda^{[i]}=(\lambda_{i+1}, \cdots, \lambda_l), \qquad i=0, 1, \ldots, l
\end{aligned}$$ So $\lambda^{[0]}=\lambda$ and $\lambda^{[l]}=\emptyset$. Next, we give the main results.

::: thm
[]{#t:iterative label="t:iterative"} For partitions $\lambda,\mu\vdash n$ and integer number $k$, $$\begin{aligned}
\label{e:qS}
q_{k}^{*}S_{\lambda}.1&=\sum\limits_{\tau\models k}(1-t)^{l(\tau)}S_{\lambda-\tau}.1\\ \label{e:Sq}
S^{*}_{k}q_{\mu}&=\sum_{\mbox{\tiny$\begin{array}{c}
\tau\subset \mu\\ |\tau|\geq k 
\end{array}$}}(1-t)^{l(\tau)}q_{\mu-\tau}S^{*}_{k-\mid \tau \mid}.1
=\sum\limits_{i=k}^{n}\sum\limits_{\tau\in \mathcal{C}^{\mu}_{i}}(1-t)^{l(\tau)}q_{\mu-\tau}S^{*}_{k-i}.1,
\end{aligned}$$ where $\mathcal{C}^{\mu}_{k}\triangleq\{\tau\models k\mid \tau\subset\mu\}.$
:::

::: proof
*Proof.* We argue by induction on $l(\lambda)$ for the first relation. The initial step is clear. Assume that [\[e:qS\]](#e:qS){reference-type="eqref" reference="e:qS"} holds for any partition with length $<l(\lambda)$, it follows from Proposition [\[Up Down\]](#Up Down){reference-type="ref" reference="Up Down"} that $$\begin{aligned}
q_{k}^{*}S_{\lambda}&=S_{\lambda_{1}}q^{*}_{k}S_{\lambda_{2}}\cdots S_{\lambda_{l}}.1+(1-t)\sum\limits_{i=1}^{k}S_{\lambda_{1}-i}q^*_{k-i}S_{\lambda_{2}}\cdots S_{\lambda_{l}}.1\\
&=\sum\limits_{\tau\models k}(1-t)^{l(\tau)}S_{\lambda_{1}}S_{\lambda^{[1]}-\tau}.1+\sum\limits_{i=1}^{k}\sum\limits_{\tau\models k-i}(1-t)^{l(\tau)+1}S_{\lambda_{1}-i}S_{\lambda^{[1]}-\tau}.1\\
&=\sum\limits_{\tau\models k}(1-t)^{l(\tau)}S_{\lambda-\tau}.1.
\end{aligned}$$ The other relation [\[e:Sq\]](#e:Sq){reference-type="eqref" reference="e:Sq"} is shown similarly. ◻
:::

::: exmp
Let $\lambda=(321), \mu=(2^21^2)$ be two partitions. $$\begin{aligned}
g^{\lambda}_{\mu}(t)&=\langle q_{2}q_{2}q_{1}q_{1}, S_{3}S_{2}S_{1}.1 \rangle\\
&=(1-t)^{2}\langle q_{2}q_{1}q_{1}, S_{3}S_{1}.1+S_{2}S_{2}.1+S_{2}S_{1}S_{1}.1 \rangle\\
&=2(1-t)^4\langle q_{1}q_{1}, S_{1}S_{1}.1+S_{2}.1 \rangle\\
&=4(1-t)^5\langle q_{1}, S_{1}.1 \rangle\\
&=4(1-t)^6.
\end{aligned}$$
:::

To compute the characters of the Hecke algebra, we collect some simple facts (see [@JL]).

::: lem
[]{#l:z label="l:z"} For partitions $\lambda,\mu \vdash n,$ $$\begin{aligned}
\label{e:q.1}
\sum\limits_{\lambda \vdash n}\frac{(-1)^{l(\lambda)}}{z_{\lambda}(t)}&=
\begin{cases}
t^n-t^{n-1}&\text{if $n\geq 1$}\\
1&\text{if $n=0$}
\end{cases}
\\ \label{e:S.1}
\sum\limits_{\lambda \vdash n}\frac{1}{z_{\lambda}(t)}&=
\begin{cases}
1-t&\text{if $n\geq 1$}\\
1&\text{if $n=0$}
\end{cases}
\\ \label{e:X(1^n)}
{\chi}^{(1^n)}_{\mu}(1)&=\langle p_{\mu}, S_{(1^n)}.1 \rangle=(-1)^{n-l(\mu)}
\\ \label{e:X(n)}
{\chi}^{(n)}_{\mu}(1)&=\langle p_{\mu}, S_n.1 \rangle=1.
\end{aligned}$$
:::

The following formulas are well-known [@Ram]. They are also obtained as special cases in our formulas for the hook and two-row cases.

::: prop
For $\mu\vdash n$, one has that $$\begin{aligned}
\label{e:onerow}
\chi^{(n)}_{\mu}(q)&=q^{n-l(\mu)},\\ \label{e:onecolumn}
\chi^{(1^n)}_{\mu}(q)&=(-1)^{n-l(\mu)}.
\end{aligned}$$
:::

For $\mu\vdash n$ and $1\leq i\leq n$, we introduce two sequences of polynomials respectively in $t$ and $t^{-1}$: $$\begin{aligned}
\label{e:ai}
a_i(\mu;t)&=(1-t)^{-l(\mu)}\sum\limits_{\tau\in \mathcal{C}^{\mu}_{i}}(1-t)^{l(\mu-\tau)}(1-t^{-1})^{l(\tau)},\\ \label{e:bi}
b_i(\mu;t)&=(1-t^{-1})^{-l(\mu)}\sum\limits_{\tau\in \mathcal{C}^{\mu}_{i}}(1-t^{-1})^{l(\mu-\tau)+l(\tau)}.
\end{aligned}$$

They are fixed by the generating functions shown below.

::: lem
[]{#l:ab label="l:ab"} For a partition $\mu=(\mu_1, \ldots, \mu_r)$, we have that $$\begin{aligned}
\label{e:av}
(1-t^{-1}v)^r\prod_{i=1}^r(1+v+\cdots+v^{\mu_i-1})&=\sum_{i=0}^{|\mu|}a_i(\mu, t)v^i\\ \label{e:bv}
\prod_{i=1}^r(t^{-1}+v^{\mu_i}+(1-t^{-1})(1+v+\cdots+v^{\mu_i-1}))&=\sum_{i=0}^{|\mu|}b_i(\mu, t)v^i
\end{aligned}$$
:::

::: proof
*Proof.* Let $c_i(\mu; t')=(1-t')^{-r}\sum\limits_{\tau\in \mathcal{C}^{\mu}_{i}}(1-t')^{l(\mu-\tau)}(1-t^{-1})^{l(\tau)}$. Then $$\begin{aligned}
(1-t')^r\sum_{i=0}^{|\mu|}c_i(\mu;t')v^i&=\sum_{k=0}^{|\mu|}\sum_{\tau\subset\mu, \tau\vDash k}(1-t')^{l(\mu-\tau)}(1-t^{-1})^{l(\tau)}v^k\\
&=\sum_{k=0}^{|\mu|}\sum_{\tau_1+\cdots+\tau_r=k}(1-t')^{r-\delta_{\tau_1,\mu_1}-\cdots -\delta_{\tau_r,\mu_r}}(1-t^{-1})^{r-\delta_{\tau_1,0}-\cdots-\delta_{\tau_r,0}}v^k\\
&=(1-t')^r\prod_{i=1}^r\left(\sum_{\tau_i=0}^{\mu_i}(1-t')^{-\delta_{\tau_i,\mu_i}}(1-t^{-1})^{1-\delta_{\tau_i,0}}v^{\tau_i}\right),
\end{aligned}$$ which implies the lemma by noting that $$\begin{gathered}
1+\sum_{i=1}^{n-1}(1-t^{-1})v^i+\frac{1-t^{-1}}{1-t'}v^n=\begin{cases}
(1-t^{-1}v)[n]_v, & t'=t\\
t^{-1}+v^k+(1-t^{-1})[n]_v, & t'=t^{-1}\end{cases}.
\end{gathered}$$ ◻
:::

We remark that $a_0(\mu; t)=b_0(\mu; t)=1$ and for any $0\leq j\leq n=|\mu|$ $$\begin{aligned}
a_j(\mu; t)&=(-1)^{l(\mu)}a_{n-j}(\mu;t^{-1}),\\
b_j(\mu;t)&=b_{n-j}(\mu;t).
\end{aligned}$$

Now we give the irreducible character formulas labeled by hook and two-row partitions.

::: thm
[]{#t:hook label="t:hook"} For partition $\mu\vdash n$ and $k\geq 0$, we have $$\begin{aligned}
\label{e:hook}
\chi^{(k,1^{n-k})}_{\mu}(q)=(-1)^{n-k+l(\mu)}\sum\limits_{i=k}^{n}a_i(\mu;q)q^i
\end{aligned}$$
:::

::: proof
*Proof.* Let $l=l(\mu)$. By Theorem [\[t:iterative\]](#t:iterative){reference-type="ref" reference="t:iterative"} it follows that $$\begin{aligned}
&g^{(k,1^{n-k})}_{\mu}(t)=\langle q_{\mu}, S_{(k,1^{n-k})}.1 \rangle=\langle S_{k}^{*}q_{\mu}, S_{(1^{n-k})}.1 \rangle\\
=&\sum\limits_{i=k}^{n}\sum_{\mbox{\tiny$\begin{array}{c}
\mid \tau \mid=i\\
\tau\subset \mu\end{array}$}}(1-t)^{l(\tau)}\langle q_{\mu-\tau}S^*_{k-i}.1, S_{(1^{n-k})}.1 \rangle\\
=&\sum\limits_{i=k}^{n}\sum_{\mbox{\tiny$\begin{array}{c}
\mid \tau \mid=i\\
\tau\subset \mu\end{array}$}}(1-t)^{l(\tau)}\sum\limits_{\mu^{(1)}\vdash \mu_{1}-\tau_{1}, \cdots, \mu^{(l)}\vdash \mu_{l}-\tau_{l}}\sum\limits_{\lambda\vdash i-k}\frac{(-1)^{l(\lambda)}}{z_{\mu^{(1)}}(t)\cdots z_{\mu^{(l)}}(t)z_{\lambda}}
\langle p_{\mu^{(1)}\cup\cdots\cup\mu^{(l)}\cup\lambda}, S_{(1^{n-k})}.1 \rangle\\
=&\sum\limits_{i=k}^{n}\sum_{\mbox{\tiny$\begin{array}{c}
\mid \tau \mid=i\\
\tau\subset \mu\end{array}$}}(1-t)^{l(\tau)}\sum\limits_{\mu^{(1)}\vdash \mu_{1}-\tau_{1}}\cdots\sum\limits_{\mu^{(l)}\vdash \mu_{l}-\tau_{l}}\sum\limits_{\lambda\vdash i-k}\frac{(-1)^{n-k}(-1)^{l(\mu^{(1)})}\cdots(-1)^{l(\mu^{(l)})}}{z_{\mu^{(1)}}(t)\cdots z_{\mu^{(l)}}(t)z_{\lambda}}\\
=&(-1)^{n-k}\sum\limits_{i=k}^{n}\sum\limits_{\tau\in \mathcal{C}^{\mu}_{i}}t^{n-i}(1-t^{-1})^{l(\mu-\tau)}(1-t)^{l(\tau)},
\end{aligned}$$ where we have used [\[e:q.1\]](#e:q.1){reference-type="eqref" reference="e:q.1"} and [\[e:S.1\]](#e:S.1){reference-type="eqref" reference="e:S.1"} in the last equation. The theorem follows by recalling [\[e:ai\]](#e:ai){reference-type="eqref" reference="e:ai"} and $\chi_{\mu}^{\lambda}(q)=(-1)^{l(\mu)}q^{n}(1-q)^{-l(\mu)}g_{\mu}^{\lambda}(q^{-1})$. ◻
:::

Lemma [\[l:ab\]](#l:ab){reference-type="ref" reference="l:ab"} offers practical way to compute [\[e:hook\]](#e:hook){reference-type="eqref" reference="e:hook"} by expanding the generating function up to certain power of $v$ and then setting $v=q$.

::: exmp
Let $\lambda=(6,1^2),\mu=(2^4)$. Taking terms of $v$ with degree $\geq 6$ and then setting $v=q$, $$\begin{aligned}
(1-t^{-1}v)^4(1+v)^4&\equiv(1-t^{-1}v)^4(6v^2+4v^3+v^4)\\
&\equiv t^{-4}v^4\cdot 6v^2+(t^{-4}v^4-4t^{-3}v^3)4v^3+(t^{-4}v^4-4t^{-3}v^3+6t^{-2}v^2)v^4\\
&\equiv 6t^2-12t^3+3t^4.
\end{aligned}$$ Therefore $\chi^{(6, 1^2)}_{(2^4)}(q)=6q^2-12q^3+3q^4$.
:::

::: thm
[]{#t:two label="t:two"} For partition $\mu\vdash n$ and $k\geq n-k\geq 0$ we have $$\begin{aligned}
\label{e:two}
\chi^{(k,n-k)}_{\mu}(q)&=q^{n-l(\mu)}(b_k(\mu;q)-b_{k+1}(\mu;q)),\\
\sum_{i=0}^{[n/2]}\chi^{(n-i, i)}_{\mu}(q)&=q^{n-l(\mu)}b_{[n/2]}(\mu;q).
\end{aligned}$$
:::

::: proof
*Proof.* By the same argument in the proof of Theorem [\[t:hook\]](#t:hook){reference-type="ref" reference="t:hook"} we see that $g^{(k,n-k)}_{\mu}(t)=\langle S_k^*q_{\mu}, S_{n-k}.1\rangle$ is equal to $$\begin{aligned}
&\sum\limits_{i=k}^{n}\sum\limits_{\tau\in\mathcal{C}^{\mu}_{i}}(1-t)^{l(\tau)}\sum\limits_{\mu^{(1)}\vdash \mu_{1}-\tau_{1}, \cdots, \mu^{(l)}\vdash \mu_{l}-\tau_{l}}\sum\limits_{\lambda\vdash i-k}\frac{(-1)^{l(\lambda)}}{z_{\mu^{(1)}}(t)\cdots z_{\mu^{(l)}}(t)z_{\lambda}}\\
=&\sum\limits_{\tau\in\mathcal{C}^{\mu}_{k}}(1-t)^{l(\mu-\tau)+l(\tau)}-\sum\limits_{\tau\in\mathcal{C}^{\mu}_{k+1}}(1-t)^{l(\mu-\tau)+l(\tau)},
\end{aligned}$$ which implies the first result by [\[e:bi\]](#e:bi){reference-type="eqref" reference="e:bi"}. The second one is clear. ◻
:::

::: exmp
Let $\lambda=(4,2),\mu=(3,2,1)$. By Theorem [\[t:two\]](#t:two){reference-type="ref" reference="t:two"}

$$\begin{aligned}
&\prod_{i=1}^3(t^{-1}+v^i+(1-t^{-1})[i]_v)-v^{-1}\prod_{i=1}^3(t^{-1}+v^i+(1-t^{-1})[i]_v)\\
&=(v-v^{-1})(t^{-1}+v^2+(1-t^{-1})(1+v))(t^{-1}+v^3+(1-t^{-1})(1+v+v^2)).
\end{aligned}$$ The coefficient of $v^4$ is $(1-t^{-1})(2-t^{-1})$. Therefore $$\chi_{(321)}^{(42)}(q)=q^3(b_4(q)-b_5(q))=q^3(2-3q^{-1}+q^{-2})=2q^3-3q^2+q.$$
:::

Using the similar argument, we can compute the general character values.

For a partition-valued function $\underline{\mu}=(\mu^{(1)}, \ldots, \mu^{(r)})$, we define $$z_{\underline{\mu}}(t)=z_{\mu^{(1)}}(t)\cdots z_{\mu^{(r)}}(t),$$ and call $|\underline{\mu}|=\sum_i|\mu^{(i)}|$ the weight of $\underline{\mu}$ and $l(\underline{\mu})=\sum_il(\mu^{(i)})$ the length of $\underline{\mu}$. Given a composition $\tau=(\tau_1, \ldots, \tau_r)$, we denote by $\underline{\mu}\vdash \tau$ the partition-valued function $\underline{\mu}=(\mu^{(1)}, \ldots, \mu^{(r)})$ such that $\mu^{(i)}\vdash \tau_i$. Clearly $|\underline{\mu}|=|\tau|$.

The following general formula expresses the Hecke algebra character in terms of irreducible characters of the symmetric groups of lower degrees.

::: thm
[]{#t:gen label="t:gen"} For $\lambda, \mu\vdash n$, the irreducible character $\chi_{\mu}^{\lambda}(q)$ is given by $$\begin{aligned}
\chi^{\lambda}_{\mu}(q)=\frac1{(q-1)^{l(\mu)}}\sum_{i=\lambda_1}^nq^i\sum_{\mbox{\tiny$\begin{matrix}|\tau|=i\\
\tau\subset\mu\end{matrix}$}}(1-q^{-1})^{l(\tau)}
\sum_{{\underline\nu}\vdash \mu-\tau}\sum_{\rho\vdash i-\lambda_1}\frac{(-1)^{l(\underline{\nu})+l(\rho)}}
{z_{\underline{\nu}}(q)z_{\rho}}\chi^{\lambda^{[1]}}_{\underline{\nu}\cup\rho}.
\end{aligned}$$
:::

::: proof
*Proof.* Let $l(\mu)=l$. As in the proof Theorem [\[t:hook\]](#t:hook){reference-type="ref" reference="t:hook"} we have that $$\begin{aligned}
&\chi^{\lambda}_{\mu}(q)=\frac{q^n}{(q-1)^l}\langle S_{\lambda_1}^{*}q_{\mu}, S_{\lambda^{[1]}}.1 \rangle\\
=&\frac{q^n}{(q-1)^l}\sum\limits_{i=\lambda_1}^{n}\sum_{\mbox{\tiny$\begin{array}{c}
\mid \tau \mid=i\\
\tau\subset \mu\end{array}$}}(1-q^{-1})^{l(\tau)}\sum_{\underline{\nu}\vdash \mu-\tau}\sum\limits_{\rho\vdash i-\lambda_1}\frac{(-1)^{l(\rho)}}{z_{\underline{\nu}}(q^{-1})z_{\rho}}\chi^{\lambda^{[1]}}_{\underline{\nu}\cup\rho}\\
=&\frac1{(q-1)^l}\sum\limits_{i=\lambda_1}^{n}\sum_{\mbox{\tiny$\begin{array}{c}
\mid \tau \mid=i\\
\tau\subset \mu\end{array}$}}q^i(1-q^{-1})^{l(\tau)}\sum_{\underline{\nu}\vdash \mu-\tau}\sum\limits_{\rho\vdash i-\lambda_1}\frac{(-1)^{l(\rho)+l(\underline{\nu})}}{z_{\underline{\nu}}(q)z_{\rho}}\chi^{\lambda^{[1]}}_{\underline{\nu}\cup\rho}.
\end{aligned}$$ ◻
:::

We remark that one obtains another general formula for $\chi_{\mu}^{\lambda}(q)$ based on the transition matrix from the elementary symmetric function $S_{-m}^*.1$ to the generalized symmetric functions $q_{\rho}$. Using the definition of $Q(z)$, it is easy to see that $$S^*(tz).1=Q(z)S^*(z).1$$ Then we have the generalized Newton's formula: $$S^*_{-m}.1=\frac1{t^m-1}(q_1S^*_{-m+1}.1+q_2S^*_{-m+2}.1+\cdots q_{m-1}S^*_{-1}.1+q_m),$$ which leads to the decomposition: $S_{-m}^*.1=\sum_{\rho\vdash m}C_{m,\rho}(t)q_{\rho}$. The first few terms are given by $$\begin{aligned}
S^*_{-1}.1&=\frac{q_1}{t-1},\\
S^*_{-2}.1&=\frac{q_1^2}{(t^2-1)(t-1)}+\frac{q_2}{t^2-1},\\
S^*_{-3}.1&=\frac{q_1^3}{(t^3-1)(t^2-1)(t-1)}+\frac{(t+2)q_2q_1}{(t^3-1)(t^2-1)}+\frac{q_3}{t^3-1},\\
S^*_{-4}.1&=\frac{q_1^4}{(t^4-1)(t^3-1)(t^2-1)(t-1)}+\frac{(t^2+t+2)q_3q_1}{(t^4-1)(t^3-1)}\\
&+\frac{(t^2+2t+3)q_2q_1^2}{(t^4-1)(t^3-1)(t^2-1)}+\frac{q_2^2}{(t^4-1)(t^2-1)}+\frac{q_4}{t^4-1}.
\end{aligned}$$

The following result can be shown similarly as Theorem [\[t:gen\]](#t:gen){reference-type="ref" reference="t:gen"}.

::: thm
For $\lambda, \mu\vdash n$. Then the irreducible character $\chi^{\lambda}_{\mu}(q)$ is given by $$\begin{aligned}
\chi^{\lambda}_{\mu}(q)=\frac{q^{\lambda_1}}{(q-1)^{l(\mu)}}\sum_{i=\lambda_1}^n\sum_{\mbox{\tiny$\begin{matrix}|\tau|=i\\
\tau\subset\mu\end{matrix}$}}(1-q^{-1})^{l(\tau)}
\sum_{\rho\vdash i-\lambda_1}(q-1)^{l(\mu-\tau)+l(\rho)}C_{i-\lambda_1, \rho}(q^{-1})\chi^{\lambda^{[1]}}_{(\mu-\tau)^*\cup \rho}(q),
\end{aligned}$$ where $C_{m,\rho}(t)$ is the transition coefficient from $S^*_{-m}.1$ to $q_{\rho}$ and $(\mu-\tau)^*$ is the rearranged partition obtained from $\mu-\tau$.
:::
