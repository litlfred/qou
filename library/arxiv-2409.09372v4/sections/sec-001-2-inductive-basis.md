---
doc_id: arxiv-2409.09372v4
doc_title: "Markov traces on degenerate cyclotomic Hecke algebras"
section_id: sec-001-2-inductive-basis
section_title: "Inductive basis"
section_number: 2
pages: 4-6
source_pdf: 2409.09372v4.pdf
source_sha256: b7eed67ec102ab3d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.842
doc_brief: "Markov traces on degenerate cyclotomic Hecke algebras — Let Hn(u) be the degenerate cyclotomic Hecke algebra with parameter u = {u1, . . . , um}."
---
[]{#Sec:Inductive-basis label="Sec:Inductive-basis"}

In this section we present some facts which are used later and construct the inductive basis for $H_n(\boldsymbol{u})$ from its standard basis.

The *Jucys--Murphy elements* of $\mathbb{C}(\boldsymbol{u})\mathfrak{S}_n$ are defined as the sum of transpositions: $$\begin{aligned}
  &&L_k=(1,k)+(2,k)+\cdots+(k\negmedspace-\negmedspace1,k),\quad k=2, \ldots, n,
\end{aligned}$$ with $L_1=0$ (and recall that $s_i=(i,i+1)$ for $i=1,\ldots,n-1$). These elements, studied by Jucys [@Jucys] and Murphy [@Murphy], admit an inductive characterization: $$\begin{aligned}
\label{Equ:JM-S}
&&L_1=0 \text{ and } L_{k+1}=s_kL_{k}s_k+s_k, \quad k=1, 2,\ldots, n-1,
\end{aligned}$$ or equivalently, $$\begin{aligned}
L_{k+1}&=&\sum_{j=1}^{k}s_k\cdots s_j\cdots s_k, \quad k=1, 2,\ldots, n-1.
\end{aligned}$$ They generate a maximal commutative subalgebra of $\mathbb{C}(\boldsymbol{u})\mathfrak{S}_n$ [@Murphy Eq. (2.6)].

For $1\leq i,j\leq n-1$, we write $s_{i,j}=s_i\cdots s_{j}$. Recall that $t_{i+1}=s_{i}t_{i}s_{i}$ with $t_1=t$ for $i\geq1$, that is, $t_{i+1}=s_{i,1}t_{1}s_{1,i}$. Eqs. [\[Equ:JM-H\]](#Equ:JM-H){reference-type="eqref" reference="Equ:JM-H"} and [\[Equ:JM-S\]](#Equ:JM-S){reference-type="eqref" reference="Equ:JM-S"} show $$\begin{aligned}
\label{Equ:J-JM}
  &&J_k=t_k+L_k, \qquad k=1,2, \ldots, n.
\end{aligned}$$

The following fact is well-known, see for example [@Z2 2.3].

::: lemma
[]{#Lem:si-Jj label="Lem:si-Jj"}Suppose that $1\le i<n$ and $1\le j, k\le n$. Then

1.  $s_jJ_j-J_{j+1}s_j=-1$ and $s_{j-1}J_j-J_{j-1}s_{j-1}=1$.

2.  $s_iJ_j=J_js_i$ if $i\neq j-1, j$.

3.  $J_jJ_k=J_kJ_j$ if $1\le j, k\le n$.

4.  $s_j(J_jJ_{j+1})=(J_jJ_{j+1})s_j$ and $s_j(J_j+J_{j+1})=(J_{j}+J_{j+1})s_j$.

5.  if $a\in \mathbb{C}(\boldsymbol{u})$ and $i\neq j$ then $s_i$ commutes with $(J_1-a)(J_2-a)\cdots(J_j-a)$.
:::

The following fact will be useful.

::: lemma
[]{#Lemm:s-t label="Lemm:s-t"}For $1\leq a,b\leq n$ and positive integers $k,\ell$, we have

1.  $s_at_b=t_bs_a$ if $a\neq b, b-1$.

2.  $s_at_a=t_{a+1}s_a$.

3.  $t_at_b-t_bt_a=[L_a,t_b]-[t_a,L_b]$, equivalently $$\begin{aligned}
    t_{a}t_b-t_bt_a=s_{b-1,1}s_{a-1,2}(s_1t-ts_1)s_{2,a-1}s_{1,b-1}.
    \end{aligned}$$

4.  Recursion identity: $$\begin{aligned}
    t^{\ell}s_1t^ks_1=s_1t^ks_1t^{\ell}+\displaystyle\sum_{i=1}^{\ell}
        (t^{\ell-i}s_1t^{k+i-1}-t^{k+i-1}s_1t^{\ell-i}).
    \end{aligned}$$

5.  Braiding relation: $$\begin{aligned}
    t_{n}^{\ell}t_{n+1}^k=(s_{n-1}s_n)(s_{n-2}s_{n-1})\cdots(s_1s_2)
    (t^{\ell}s_1t^ks_1)(s_2s_1)\cdots(s_{n-1}s_{n-2})(s_ns_{n-1}).
    \end{aligned}$$

6.  Conjugation relation: $$\begin{aligned}
    t_{n+1}^kt=tt_{n+1}^k+t^ks_{n,1}s_{2,n}-s_{n,1}s_{2,n}t^k.
    \end{aligned}$$
:::

::: proof
*Proof.* (i)--(ii) follow from direct computation. (iii) follows by using the commutativity of $L_a$ and $J_b$ with Eq. [\[Equ:J-JM\]](#Equ:J-JM){reference-type="eqref" reference="Equ:J-JM"}.

We prove (iv) by induction on $\ell$. For $\ell=1$, by apply the equality $$\begin{aligned}
s_1ts_1ts_1t+s_1t=ts_1ts_1+ts_1
\end{aligned}$$ iteratively, we obtain $$\begin{aligned}
ts_1t^{k}s_1&=s_1t^{k}s_1t+s_1t^{k}-t^{k}s_1
\end{aligned}$$ for any positive integer $k$. Assume it is true for $\ell\geq 1$. For $\ell+1$, by induction hypothesis, we have $$\begin{aligned}
t^{\ell+1}s_1t^{k}s_1&=ts_1t^{k}s_1t^{\ell}+\sum_{i=1}^{\ell}\left(t^{\ell+1-i}
s_1t^{k+i-1}-t^{k+i}s_1t^{\ell-i}\right)\\
&=s_1t^{k}s_1t^{\ell+1}+\sum_{i=1}^{\ell+1}\left(t^{\ell+1-i}
s_1t^{k+i-1}-t^{k+i-1}s_1t^{\ell+1-i}\right).
 
\end{aligned}$$ Thus (iv) holds for any positive integers $k,\ell$.

(v). Apply induction on $n$ and $n=1$ is trivial. Assume it holds for $n\geq 1$. For $n+1$, $$\begin{aligned}
 t_{n+1}^{\ell}t_{n+2}^{k}&=(s_ns_{n+1})t_{n}^{\ell}t_{n+1}^{k}(s_{n+1}s_{n})\\
  &=(s_ns_{n+1})(s_{n-1}s_n)\cdots(s_1s_2)(t^{\ell}s_1t^{k}s_1)
    (s_2s_1)\cdots(s_ns_{n-1})(s_{n+1}s_{n}).
 
\end{aligned}$$ (vi). It is easy to see that $$\begin{aligned}
   t_{n+1}^kt&=s_{n,2}(s_1t^ks_1t)s_{2,n}\\
   &=s_{n,2}(ts_1t^ks_1+t^ks_1-s_1t^k)s_{2,n}\\
   &=tt_{n+1}^k+t^ks_{n,1}s_{2,n}-s_{n,1}s_{2,n}t^k,
 
\end{aligned}$$ where the second equality follows by applying (iv). ◻
:::

The following fact will be useful.

::: corollary
[]{#Cor:t-n-n+1 label="Cor:t-n-n+1"}For positive integers $n,k,\ell,a$, we have $$\begin{aligned}
t_{n}^{\ell}t_{n+a}^k=t_{n+a}^kt_{n}^{\ell}+\sum_{i=1}^{\ell}
s_{n+a-1}\cdots s_{n}
\left(t_n^{\ell-i}s_nt_n^{k+i-1}-t_n^{k+i-1}s_nt_n^{\ell-i}\right)
s_{n}\cdots s_{n+a-1}.
\end{aligned}$$
:::

::: proof
*Proof.* We argue by induction. For $a=1$, Lemma [\[Lemm:s-t\]](#Lemm:s-t){reference-type="ref" reference="Lemm:s-t"}(v) gives $$\begin{aligned}
 t_n^{\ell}t_{n+1}^k=(s_{n-1}s_n)\cdots(s_1s_2)(s_1t^ks_1t^{\ell})(s_2s_1)\cdots(s_ns_{n-1}).
  
\end{aligned}$$ Then the equality follows by using Lemma [\[Lemm:s-t\]](#Lemm:s-t){reference-type="ref" reference="Lemm:s-t"}(iv, v).

Now assume it holds for $a\geq 1$. Since $$\begin{aligned}
  t_{n+a+1}^k=(s_{n+a}\cdots s_{n+1})t_{n+1}^k(s_{n+1}\cdots s_{n+a}),
 
\end{aligned}$$ Lemma [\[Lemm:s-t\]](#Lemm:s-t){reference-type="ref" reference="Lemm:s-t"}(i) shows $$\begin{aligned}
t_{n}^{\ell}t_{n+a+1}^k
&= (s_{n+a}\cdots s_{n+1})(t_{n}^{\ell}t_{n+1}^{k})(s_{n+1}\cdots s_{n+a}) \\
&= t_{n+a}^k t_{n}^{\ell} + \sum_{i=1}^{\ell} s_{n+a}\cdots s_{n+1}(t_n^{\ell-i}s_n t_n^{k+i-1} - t_n^{k+i-1}s_n t_n^{\ell-i})s_{n+1}\cdots s_{n+a}.
\end{aligned}$$ This completes the proof. ◻
:::

Now we are ready to describe the inductive basis for $H_{\infty}(\boldsymbol{u})$, which are derived from the standard basis Eq. ([\[Equ:Standard-basis\]](#Equ:Standard-basis){reference-type="ref" reference="Equ:Standard-basis"}). The following fact is an $H_{n+1}(\boldsymbol{u})$-analogue of [@Jones (4.4)] and [@L Theorem 2].

::: theorem
[]{#Them:Inductive-basis label="Them:Inductive-basis"} Every element of $H_{n+1}(\boldsymbol{u})$ can be uniquely expressed as a $\mathbb{C}(\boldsymbol{u})$--linear combination of the following four types of words:

1.  $h_{n}$;

2.  $h_{n}s_n \cdots s_i$, $i = 1, \ldots, n$;

3.  $h_{n}s_n \cdots s_i J_{i}^k$, $i = 1, \ldots, n$, $1 \leq k\leq m-1$;

4.  $h_{n}J_{n+1}^k$, $1 \leq k \leq m-1$;

where $h_{n} \in H_n(\boldsymbol{u})$.
:::

::: proof
*Proof.* We prove this by induction on $n$. Thanks to the standard basis theorem [@K Theorem 7.5.6] (see Eq. [\[Equ:Standard-basis\]](#Equ:Standard-basis){reference-type="eqref" reference="Equ:Standard-basis"}), it is enough to show that $$\begin{aligned}
x &= J_1^{k_1} \cdots J_{n+1}^{k_{n+1}} w \in \mathfrak{B}_{n+1}\setminus \mathfrak{B}_n
\end{aligned}$$ can be expressed uniquely in terms of the four-type words, that is, we only need to consider the following cases:

**Case (a):** $x$ contains no $J_{n+1}$, but $w = w'(s_n s_{n-1} \cdots s_i)$ with $w'\in \mathfrak{S}_{n}$, i.e., $$\begin{aligned}
  x = J_{i_1}^{k_1}J_{i_2}^{k_2} \cdots J_{i_r}^{k_r}w'(s_n s_{n-1} \cdots s_i),
\end{aligned}$$ where $1 \leq i_1 < \cdots < i_r \leq n$ and $w'\in \mathfrak{S}_{n}$. Then $$\begin{aligned}
x = (J_{i_1}^{k_1} \cdots J_{i_r}^{k_r}w')(s_n s_{n-1} \cdots s_i),
\end{aligned}$$ which is of type (II).

**Case (b):** $x$ contains $J_{n+1}$ and $x = J_{i_1}^{k_1}J_{i_2}^{k_2} \cdots J_{i_r}^{k_r}J_{n+1}^{k}w$ with $1 \leq i_1 < \cdots < i_r \leq n$, $k\geq 1$ and $w \in  \mathfrak{S}_{n}$. Using the commutation relation $J_{n+1}w=wJ_{n+1}$ (Lemma [\[Lem:si-Jj\]](#Lem:si-Jj){reference-type="ref" reference="Lem:si-Jj"}(ii)), we rewrite $$\begin{aligned}
x = \left(J_{i_1}^{k_1} \cdots J_{i_r}^{k_r}w\right) J_{n+1}^{k},
\end{aligned}$$ which is of type (IV).

**Case (c):** $x = x'J_{n+1}^k w'(s_n s_{n-1} \cdots s_i)$ with $x' \in H_n(\boldsymbol{u})$ and $w' \in \mathfrak{S}_n$. Then $$\begin{aligned}
x &= (x'w')(J_{n+1}^{k}s_n s_{n-1} \cdots s_i) \qquad \text{(Lemma~\ref{Lem:si-Jj}(ii))}\\
&= (x'w')J_{n+1}^{k-1}(s_n J_n + 1)s_{n-1} \cdots s_i\qquad  \text{(Eq~\eqref{Equ:JM-H})}\\
&= (x'w's_{n-1} \cdots s_i)J_{n+1}^{k-1} + (x'w')(J_{n+1}^{k-1}s_n)J_n s_{n-1} \cdots s_i.
\end{aligned}$$ By induction, $y = J_n s_{n-1} \cdots s_i$ is a $\mathbb{C}(\boldsymbol{u})$--linear combination of words of four types, that is, there exists $h_{n-1} \in H_{n-1}(\boldsymbol{u})$ such that $$\begin{aligned}
 y&= h_{n-1}(1 + s_{n-1} \cdots s_i + s_{n-1} \cdots s_i J_i^a + J_n^b)
\end{aligned}$$ for some $1\leq a,b<m-1$. Thus $$\begin{aligned}
(J_{n+1}^{k-1} s_n)y &=  h_{n-1}(J_{n+1}^{k-1} s_n)(1 + s_{n-1} \cdots s_i + s_{n-1} \cdots s_i J_i^a + J_n^b)
\end{aligned}$$ is a $\mathbb{C}(\boldsymbol{u})$--linear combination of words of four types, showing $x$ is also such a combination. The standard basis is unique, so any two expressions of $x$ in terms of the four types would imply a non-trivial linear relation in the standard basis, which is impossible. Thus the decomposition is unique. ◻
:::

::: theorem
[]{#Them:Basis-for-Markov label="Them:Basis-for-Markov"} Every element of $H_{n+1}(\boldsymbol{u})$ can be written uniquely as a $\mathbb{C}(\boldsymbol{u})$--linear combination of words of one of the following types:

1.  $h_{n}$;

2.  $h_{n}s_n \cdots s_i$, $i = 1, \ldots, n$;

3.  $h_{n}s_n \cdots s_i t_{i}^k$, $i = 1, \ldots, n$, $1 \leq k\leq m-1$;

4.  $h_{n}t_{n+1}^k$, $1 \leq k \leq m-1$;

where $h_{n} \in H_n(\boldsymbol{u})$.
:::

::: proof
*Proof.* By Theorem [\[Them:Inductive-basis\]](#Them:Inductive-basis){reference-type="ref" reference="Them:Inductive-basis"}, we need to express words of types (III) and (IV) in terms of words of type (a)--(d). Let $h = h_{n}s_n \cdots s_i J_i^k$ ($1 \leq k\leq m-1$) be a word of type (III). We prove the assertion holds by induction on $k$.

For $k = 1$, $J_i=t_i+L_i$ shows $$\begin{aligned}
 h &= h_{n}s_n \cdots s_i(t_i + L_i) = h_{n}s_n \cdots s_i t_i + h_{n}s_n \cdots s_i L_i,
\end{aligned}$$ which is a combination of types (a), (b), (c). Assume the claim holds for $k = p$. For $k = p+1$, we have $$\begin{aligned}
  h_{n}s_n \cdots s_i J_i^{p+1}& = h_{n}s_n \cdots s_i J_i^p (t_i + L_i),
\end{aligned}$$ which decomposes into terms handled by induction. Similar argument shows the assertion holds for words of type (IV). ◻
:::

::: theorem
[]{#Them:t-basis label="Them:t-basis"}Keeping notations as above, then the set $$\begin{aligned}
\mathscr{T}_n := \left\{ t_{i_1}^{k_1} \cdots t_{i_r}^{k_r} w \;\middle|\; 1 \leq i_1 < \cdots < i_r \leq n,\; 0 \leq k_1, \ldots, k_r\leq m-1,\; w \in \mathfrak{S}_n \right\}
\end{aligned}$$ forms a $\mathbb{C}(\boldsymbol{u})$-basis of $H_n(\boldsymbol{u})$.
:::

::: proof
*Proof.* By Theorem [\[Them:Basis-for-Markov\]](#Them:Basis-for-Markov){reference-type="ref" reference="Them:Basis-for-Markov"}, it suffices to show that the inductive basis (a)--(d) lies in $\mathscr{T}_n$. Firstly an induction argument shows $h_{n-1} \in \mathscr{T}_{n-1} \subset \mathscr{T}_n$ when $h_{n-1} \in H_{n-1}(\boldsymbol{u})$. For any $h_{n-1}\in H_{n-1}(\boldsymbol{u})$, we assume that $h_{n-1} = t_{i_1}^{k_1} \cdots t_{i_r}^{k_r} \sigma$ with $\sigma\in \mathfrak{S}_{n-1}$. Then $$\begin{aligned}
 && h_{n-1}s_{n-1} \cdots s_i= t_{i_1}^{k_1} \cdots t_{i_r}^{k_r} \sigma s_{n-1} \cdots s_i \in \mathscr{T}_n,\\
 &&h_{n-1}s_{n-1} \cdots s_i t_i^k=t_{i_1}^{k_1} \cdots t_{i_r}^{k_r} \sigma t_{n}^k s_{n-1} \cdots s_i \in \mathscr{T}_n,\\
&&h_{n-1}t_{n+1}^k=t_{i_1}^{k_1} \cdots t_{i_r}^{k_r} \sigma t_{n}^k s_{n-1} \cdots s_i \in \mathscr{T}_n.
\end{aligned}$$ This proof is completed. ◻
:::
