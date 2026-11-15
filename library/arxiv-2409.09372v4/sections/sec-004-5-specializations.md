---
doc_id: arxiv-2409.09372v4
doc_title: "Markov traces on degenerate cyclotomic Hecke algebras"
section_id: sec-004-5-specializations
section_title: "Specializations"
section_number: 5
pages: 13-16
source_pdf: 2409.09372v4.pdf
source_sha256: b7eed67ec102ab3d
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.95
doc_brief: "Markov traces on degenerate cyclotomic Hecke algebras — Let Hn(u) be the degenerate cyclotomic Hecke algebra with parameter u = {u1, . . . , um}."
---
This section is devoted to investigating the specializations of (non-)normalized Markov traces. In particular, we obtain the Broué--Malle--Michel symmetrizing trace on $H_n(\boldsymbol{u})$ and show that the Brundan--Kleshchev trace on $H_n(\boldsymbol{u})$ is a specialization of the non-normalized Markov trace.

We begin with the following fact.

::: lemma
[]{#Lemm:t-trace label="Lemm:t-trace"}Let $\mathrm{tr}$ be the normalized Markov trace on $H_n(\boldsymbol{u})$ with parameters $z=0$, $y_1, \ldots, y_{m-1}\in \mathbb{C}(\boldsymbol{u})$. For any $w\in \mathfrak{S}_n-\{1\}$ and $0\leq a_1, \ldots, a_n\leq m-1$, we have $$\begin{aligned}
\mathrm{tr}(t_1^{a_1}t_2^{a_2}\cdots t_n^{a_n}w)=0.
 
\end{aligned}$$
:::

::: proof
*Proof.* Any reduced word $w\in\mathfrak{S}_n-\{1\}$ can be expressed in Jones' normal form: $$w=(s_{i_r}s_{i_r-1}\cdots s_{k_r})\cdots(s_{i_1}s_{i_1-1}\cdots s_{k_1}),$$ where $1\leq i_1<\cdots<i_r\leq n-1$, $1\leq k_1<\cdots<k_r\leq n-1$ and $i_j\geq k_j$ for all $j$.

If $i_r<{n-1}$ then Theorem [\[Them:Markov\]](#Them:Markov){reference-type="ref" reference="Them:Markov"}(m4) shows $$\begin{aligned}
\mathrm{tr}(t_1^{a_1}t_2^{a_2}\cdots t_n^{a_n}w)=y_{a_n}\mathrm{tr}(t_1^{a_1}t_2^{a_2}\cdots t_{n-1}^{a_{n-1}}w).
\end{aligned}$$ So we may assume that $i_r=n-2$ and let $w'=s_{i_r}w$. Then $w'\in\mathfrak{S}_{n-2}$ and $$\begin{aligned}
 \mathrm{tr}(t_1^{a_1}t_2^{a_2}\cdots t_{n-1}^{a_{n-1}}w)&=\mathrm{tr}\left(t_1^{a_1}t_2^{a_2}\cdots t_{n-2}^{a_{n-2}}s_{n-2}t_{n-2}^{a_{n-1}}w'\right)\\
 &=z\,\mathrm{tr}\left(t_1^{a_1}t_2^{a_2}\cdots t_{n-2}^{a_{n-2}+a_{n-1}}w'\right)\\
 &=0.
 
\end{aligned}$$ If $i_r=n-1$ then $w'\in\mathfrak{S}_{n-1}$ and $$\begin{aligned}
 \operatorname{tr}(t_1^{a_1}t_2^{a_2}\dotsm t_{n-1}^{a_{n-1}}w)
 &=\operatorname{tr}(t_1^{a_1}t_2^{a_2}\dotsm t_{n-1}^{a_{n-1}}s_{n-1}t_{n-1}^{a_n}w')\\
 &=z\operatorname{tr}(t_1^{a_1}t_2^{a_2}\dotsm t_{n-1}^{a_{n-1}+a_n}w')\\
 &=0.
 
\end{aligned}$$ In both cases, the trace vanishes under $z=0$. Thus, $\mathrm{tr}(t_1^{a_1}t_2^{a_2}\cdots t_n^{a_n}w)=0$ for all non-trivial $w$. This completes the proof. ◻
:::

The following result is an immediate consequence of Lemma [\[Lemm:t-trace\]](#Lemm:t-trace){reference-type="ref" reference="Lemm:t-trace"}:

::: corollary
[]{#Cor:t-trace label="Cor:t-trace"} Let $\mathrm{tr}_{\boldsymbol{0}}$ be the normalized Markov trace on $H_n(\boldsymbol{u})$ with parameters $z = y_1 = \cdots = y_{m-1} = 0$. Then $\mathrm{tr}_{\boldsymbol{0}}$ is a trace on $H_n(\boldsymbol{u})$ satisfying: $$\mathrm{tr}_{\boldsymbol{0}}(t_1^{a_1} \cdots t_n^{a_n}w) =\begin{cases}
1, & \text{if } a_1 = \cdots = a_n = 0 \text{ and } w = 1; \\
0, & \text{otherwise}.
\end{cases}$$
:::

::: proof
*Proof.* Since $\mathrm{tr}_{\boldsymbol{0}}(1) = 1$ by definition, it remains to show: $$\mathrm{tr}_{\boldsymbol{0}}(t_1^{a_1} \cdots t_n^{a_n}w) = 0 \quad \text{for all } w \in \mathfrak{S}_n-\{1\} \text{ or } a_i \neq 0 \text{ (some } i\text{)}.$$

*Case 1:* When $w \in \mathfrak{S}_n-\{1\}$, Lemma [\[Lemm:t-trace\]](#Lemm:t-trace){reference-type="ref" reference="Lemm:t-trace"} directly gives $\mathrm{tr}_{\boldsymbol{0}}(t_1^{a_1} \cdots t_n^{a_n}w) = 0$.

*Case 2:* If $a_i \neq 0$ for some $i$, let $i$ be maximal with $a_i \neq 0$. By Theorem [\[Them:Markov\]](#Them:Markov){reference-type="ref" reference="Them:Markov"} (m4), we have $$\mathrm{tr}_{\boldsymbol{0}}(t_1^{a_1} \cdots t_n^{a_n}) = y_{a_i} \mathrm{tr}_{\boldsymbol{0}}(t_1^{a_1} \cdots t_{i-1}^{a_{i-1}}) = 0.$$ This completes the proof. ◻
:::

::: remark
This specialization $\mathrm{tr}_{\boldsymbol{0}}$, which is referred to as the Broué--Malle--Michel symmetrizing trace on $H_n(\boldsymbol{u})$, closely resembles the canonical symmetric trace on cyclotomic Hecke algebras of type $G(m,1,n)$ defined by Bremke and Malle [@BM]. Their trace emerges as a specialization of the Markov trace for cyclotomic Hecke algebras, as detailed in [@GIM Lemma 4.3]. It is a natural question to determine the Schur elements of the degenerate cyclotomic Hecke algebras with respect to the Broué--Malle--Michel symmetrizing trace.
:::

Let $\mathrm{tr}$ be the normalized Markov trace on $H_{\infty}(\boldsymbol{u})$ with parameters $z, y_1,\ldots, y_{m-1}$. It would be interesting to determine $\mathrm{tr}(J_1^{a_1}J_2^{a_2}\cdots J_i^{a_i}w)$ for all $1\leq a_i\leq m-1$, for all $w\in _i$, and for all $i\geq 1$. For example, it is easy to verify that $$\mathrm{tr}(J_1J_2\cdots J_i)=\prod_{j=1}^i\mathrm{tr}(J_i)=\prod_{j=1}^{i-1}(y_1+(j-1)z)$$ for $i=1,2\ldots$. Furthermore, for positive integers $n,k$, and for all $h\in H_{n}(\boldsymbol{u})$, we have $$\begin{aligned}
    \mathrm{tr}(hJ_{n+1}\cdots J_{n+k})&=\mathrm{tr}(h)\prod_{i=1}^k(y_1+(n+i-1)z).
\end{aligned}$$ Now assume that $z=0$, for positive integers $n,k$, and for all $h\in H_{n}(\boldsymbol{u})$, we have $$\mathrm{tr}(hJ_{n+1}^2\cdots J_{n+k}^2)=\mathrm{tr}(h)\prod_{i=1}^{k}(y_2+n+i-1).$$

The following specialization of the non-normalized Markov traces will be helpful.

::: lemma
[]{#Lemm:Specialization label="Lemm:Specialization"}Let $\mathrm{Tr}_0$ be the non-normalized Markov trace on $H_n(\boldsymbol{u})$ with parameters $z=0$ and $y_1, \ldots, y_{m-1}\in\mathbb{C}(\boldsymbol{u})$. For $1\leq k\leq m-1$ and $1\leq i\leq n$, $$\begin{aligned}
\mathrm{Tr}_0(J_i^{k})&=&\mathrm{Tr}_0(J_{i-1}^{k})
+k\sum_{\ell=0}^{k-1}\mathrm{Tr}_0(J_{i}^{k-2-\ell}J_{i-1}^{\ell})-
\sum_{j=0}^{k-1}\sum_{\ell=0}^{j-1}\mathrm{Tr}_0(J_{i}^{k-2-\ell}J_{i-1}^{\ell}).
  
\end{aligned}$$
:::

::: proof
*Proof.* Clearly it is trivial when $i=1$. For $i>1$, using Eq. ([\[Equ:JM-H\]](#Equ:JM-H){reference-type="ref" reference="Equ:JM-H"}) and Lemma [\[Lemm:J-s_n\]](#Lemm:J-s_n){reference-type="ref" reference="Lemm:J-s_n"}, we derive $$\begin{aligned}
J_{i}^{k}&=s_{i-1}J_{i-1}^{k}s_{i-1}+\sum_{j=0}^{k-1}J_{i}^{k-1-j}J_{i-1}^js_{i-1}\\
&=s_{i-1}J_{i-1}^{k}s_{i-1}+\sum_{j=0}^{k-1}J_{i}^{k-1-j}
\biggl(s_{i-1}J_i^j-\sum_{\ell=0}^{j-1}J_i^{j-1-\ell}J_{i-1}^{\ell}\biggr)\\
&=s_{i-1}J_{i-1}^{k}s_{i-1}+\sum_{j=0}^{k-1}J_{i}^{k-1-j}
s_{i-1}J_i^j-\sum_{j=0}^{k-1}\sum_{\ell=0}^{j-1}J_{i}^{k-2-\ell}J_{i-1}^{\ell}.
\end{aligned}$$ Thus Theorem [\[Them:Markov-BK\]](#Them:Markov-BK){reference-type="ref" reference="Them:Markov-BK"} shows $$\begin{aligned}
\mathrm{Tr}(J_{i}^{k})&=\mathrm{Tr}(J_{i-1}^{k})+k\,\mathrm{Tr}(J_{i}^{k-1}s_{i-1})-
\sum_{j=0}^{k-1}\sum_{\ell=0}^{j-1}\mathrm{Tr}(J_{i}^{k-2-\ell}J_{i-1}^{\ell}).
\end{aligned}$$ Again using Lemma [\[Lemm:J-s_n\]](#Lemm:J-s_n){reference-type="ref" reference="Lemm:J-s_n"} and Theorem [\[Them:Markov-BK\]](#Them:Markov-BK){reference-type="ref" reference="Them:Markov-BK"}, we have $$\begin{aligned}
\mathrm{Tr}(J_{i}^{k-1}s_{i-1})&=z\,\mathrm{Tr}(J_{i-1}^{k})+
\sum_{\ell=0}^{k-1}\mathrm{Tr}(J_{i}^{k-2-\ell}J_{i-1}^{\ell}).
\end{aligned}$$ Therefore, we yield $$\begin{aligned}
\mathrm{Tr}_0(J_{i}^{k})&=\mathrm{Tr}_0(J_{i-1}^{k})
+k\sum_{\ell=0}^{k-1}\mathrm{Tr}_0(J_{i}^{k-2-\ell}J_{i-1}^{\ell})-
\sum_{j=0}^{k-1}\sum_{\ell=0}^{j-1}\mathrm{Tr}_0(J_{i}^{k-2-\ell}J_{i-1}^{\ell}).
\end{aligned}$$ It completes the proof. ◻
:::

The following fact states the Brundan--Kleshchev trace $\tau_{\mathrm{BK}}$ is a specialization of the non-normalized Markov trace $\mathrm{Tr}$, which may viewed as a first step to the problem posed in [@Z2 Remark 5.7(ii)].

::: corollary
[]{#Cor:BK-specialization label="Cor:BK-specialization"}Let $\mathrm{Tr}_{\boldsymbol{0},1}$ be the non-normalized Markov trace on $H_n(\boldsymbol{u})$ with parameter $z=y_1=\cdots=y_{m-2}=0$ and $y_{m-1}=1$. Then $\mathrm{Tr}_{\boldsymbol{0},1}=\tau_{\mathrm{BK}}$.
:::

::: proof
*Proof.* For $i=1, \ldots, n$, Lemma [\[Lemm:Specialization\]](#Lemm:Specialization){reference-type="ref" reference="Lemm:Specialization"} shows $$\begin{aligned}
\mathrm{tr}_{\boldsymbol{0},1}(J_{i}^{a_i})&=\left\{\begin{array}
  {ll}1,&\text{ if }a_i=m-1;\\
  0,&\text{ otherwise.}
\end{array}\right.
\end{aligned}$$ Therefore $$\begin{aligned}
 \mathrm{Tr}_{\boldsymbol{0},1}(J_1^{a_1}\cdots J_n^{a_n})=\left\{\begin{array}
  {ll}1,&\text{ if }a_1=\cdots=a_n=m-1;\\
  0,&\text{ otherwise.}
\end{array}\right.
\end{aligned}$$ Note that any reduced word $w\in\mathfrak{S}_n-\{1\}$ can be expressed in Jones' normal form: $$w=(s_{i_r}s_{i_r-1}\cdots s_{i_r-k_r})\cdots(s_{i_1}s_{i_1-1}\cdots s_{i_1-k_1}),$$ where $1\leq i_1<\cdots<i_r\leq n-1$. Then Lemma [\[Lem:si-Jj\]](#Lem:si-Jj){reference-type="ref" reference="Lem:si-Jj"} shows $$\begin{aligned}
  J_1^{a_1}\cdots J_n^{a_n}w&=J_1^{a_1}\cdots J_{i_r}^{a_{i_r}}J_{i_r+1}^{a_{i_r+1}}s_{i_r}w'J_{i_r+2}^{a_{i_r+2}}\cdots J_n^{a_n},
\end{aligned}$$ where $w'=s_{i_r}w$. Then Lemma [\[Lemm:J-s_n\]](#Lemm:J-s_n){reference-type="ref" reference="Lemm:J-s_n"} shows $$\begin{aligned}
J_{i_r+1}^{a_{i_r+1}}s_{i_r}&= s_{i_r}J_{i_r}^{a_{i_r+1}}+\sum_{j=0}^{a_{i_r+1}-1}J_{i_r+1}^{a_{i_r+1}-1-j}J_{i_r}^j.
 
\end{aligned}$$ Now Theorem [\[Them:Markov-BK\]](#Them:Markov-BK){reference-type="ref" reference="Them:Markov-BK"} and $z=0$ show $$\begin{aligned}
  \mathrm{Tr}_{\boldsymbol{0},1}(J_1^{a_1}\cdots J_n^{a_n}w)&=\sum_{j=0}^{a_{i_r+1}-1}\mathrm{Tr}_{\boldsymbol{0},1}(J_1^{a_1}\cdots J_{i_r}^{a_{i_r}+j}w'J_{i_r+1}^{a_{i_r+1}-1-j}J_{i_r+2}^{a_{i_r+2}}\cdots J_n^{a_n})\\
  &=\sum_{j=0}^{a_{i_r+1}-1}\mathrm{Tr}_{\boldsymbol{0},1}(J_1^{a_1}\cdots J_{i_r}^{a_{i_r}+j}w')\mathrm{Tr}_{\boldsymbol{0},1}(J_{i_r+1}^{a_{i_r+1}-1-j}J_{i_r+2}^{a_{i_r+2}}\cdots J_n^{a_n}).
\end{aligned}$$ Thus apply the induction argument and trace properties iteratively show each term vanishes due to $z=0$ and Lemma [\[Lemm:Specialization\]](#Lemm:Specialization){reference-type="ref" reference="Lemm:Specialization"}. It completes the proof. ◻
:::
