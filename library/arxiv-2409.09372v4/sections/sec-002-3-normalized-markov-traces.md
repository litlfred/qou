---
doc_id: arxiv-2409.09372v4
doc_title: "Markov traces on degenerate cyclotomic Hecke algebras"
section_id: sec-002-3-normalized-markov-traces
section_title: "Normalized Markov traces"
section_number: 3
pages: 6-10
source_pdf: 2409.09372v4.pdf
source_sha256: b7eed67ec102ab3d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.78
doc_brief: "Markov traces on degenerate cyclotomic Hecke algebras — Let Hn(u) be the degenerate cyclotomic Hecke algebra with parameter u = {u1, . . . , um}."
---
[]{#Sec:Markov-traces label="Sec:Markov-traces"} In this section, we construct a $\mathbb{C}(\boldsymbol{u})$--linear function on $H_n(\boldsymbol{u})$ and demonstrate it constitutes a normalized Markov trace through Lambropoulou's approach from [@L], thereby proving Theorem [\[Them:Markov\]](#Them:Markov){reference-type="ref" reference="Them:Markov"} from the introduction.

The following lemma is a degeneration version of [@L Lemma 6], which can be proved through analogous reasoning:

::: lemma
[]{#Lemm:Bimodules-iso label="Lemm:Bimodules-iso"}Define the map $$\begin{aligned}
&&\phi_n:H_n(\boldsymbol{u})\otimes_{H_{n-1}(\boldsymbol{u})}H_{n}(\boldsymbol{u})\bigoplus (\oplus_{i=0}^{m-1}H_{n}(\boldsymbol{u}))\longrightarrow H_{n+1}(\boldsymbol{u}),
\end{aligned}$$ by $$\begin{aligned}
&&\qquad\qquad a\otimes b\bigoplus (\oplus_{i=0}^{m-1}a_i)\mapsto as_nb+\sum_{i=0}^{m-1}a_kt_{n+1}^i.
\end{aligned}$$ Then $\phi_n$ is an $H_n(\boldsymbol{u})$-bimodule isomorphism.
:::

::: proof
*Proof.* Theorem [\[Them:Basis-for-Markov\]](#Them:Basis-for-Markov){reference-type="ref" reference="Them:Basis-for-Markov"} establishes that $$\begin{aligned}
  &&\mathscr{B}_n=\{s_{n-1}\cdots s_i\,|\,1\leq i\leq n-1\}\cup\{t_n^k\,|\,0\leq k\leq m-1\}\\
  &&\qquad\qquad\cup\{s_{n-1}\cdots s_{i}t_i^k\,|\,2\leq i\leq n-2,1\leq k\leq m-1\}
  
\end{aligned}$$ forms basis for $H_n(\boldsymbol{u})$ as a free $H_{n-1}(\boldsymbol{u})$-module. The universal property of tensor products yields: $$\begin{aligned}
  H_n(\boldsymbol{u})\otimes_{H_{n-1}(\boldsymbol{u})}H_{n}(\boldsymbol{u})&=&H_n(\boldsymbol{u})\otimes_{H_{n-1}(\boldsymbol{u})}
  (\oplus_{\alpha\in\mathscr{B}_n}H_{n-1}(\boldsymbol{u})\cdot\alpha)\\
  &=&\oplus_{\alpha\in\mathscr{B}_n} (H_n(\boldsymbol{u})\otimes_{H_{n-1}(\boldsymbol{u})}H_{n-1}(\boldsymbol{u})\cdot\alpha)\\
  &=&\oplus_{\alpha\in\mathscr{B}_n}H_n(\boldsymbol{u})\cdot\alpha.
                  
\end{aligned}$$ Thus $$\begin{aligned}
  H_n(\boldsymbol{u})\otimes_{H_{n-1}(\boldsymbol{u})}H_{n}(\boldsymbol{u})\bigoplus(\oplus_{i=0}^{m-1}H_n(\boldsymbol{u}))
  &=&\oplus_{\alpha\in\mathscr{B}_n}H_n(\boldsymbol{u})\cdot\alpha\bigoplus(\oplus_{i=0}^{m-1}H_n(\boldsymbol{u})).
                  
\end{aligned}$$ Similarly, the set $$\begin{aligned}
  &&\mathscr{B}_{n+1}=\{s_ns_{n-1}\cdots s_i\,|\,1\leq i\leq n\}
  \cup\{t_{n+1}^k\,|\,0\leq k\leq m-1\}\\
  &&\qquad\qquad\qquad\cup\{s_{n}\cdots s_{i}t_i^k\,|\,1\leq i\leq n-1,1\leq k\leq m-1\}
  
\end{aligned}$$ forms a basis of $H_{n+1}(\boldsymbol{u})$ as a free $H_{n}(\boldsymbol{u})$-module. Observing that $$\begin{aligned}
  &&\mathscr{B}_{n+1}=\{s_n\alpha\,|\,\alpha\in\mathscr{B}_{n}\}\cup\{t_{n+1}^k\,|\,0\leq k\leq m-1\},
  
\end{aligned}$$ we conclude $\phi_n$ bijectively maps basis elements to $\mathscr{B}_{n+1}$, establishing the bimodule isomorphism. ◻
:::

Given $z, y_1, \ldots, y_{m-1}\in \mathbb{C}(\boldsymbol{u})$, we inductively define a $\mathbb{C}(\boldsymbol{u})$-linear function $\mathrm{tr}$ on $H_{\infty}(\boldsymbol{u})$ as follows: Given an element $x\in H_{n+1}(\boldsymbol{u})$ expressed via Lemma [\[Lemm:Bimodules-iso\]](#Lemm:Bimodules-iso){reference-type="ref" reference="Lemm:Bimodules-iso"} as $$x:=\phi_n\left(a\otimes b\oplus\left(\oplus_{k=0}^{m-1}\alpha_kt_{n+1}^k\right)\right),$$ we define $$\begin{aligned}
\label{Equ:tr-def}
&& \mathrm{tr}(x):=z\mathrm{\,tr}(ab)+\mathrm{tr}(\alpha_0)+\sum_{k=1}^{m-1}
y_k\mathrm{tr}(\alpha_k),
\end{aligned}$$ where $y_k=\mathrm{tr}(t_{n+1}^k)$ (independent of $n$) and $\mathrm{tr}(1)=1$. This construction satisfies properties (m1), (m3), and (m4) of Theorem [\[Them:Markov\]](#Them:Markov){reference-type="ref" reference="Them:Markov"} in Introduction.

To show that the $\mathbb{C}(\boldsymbol{u})$-linear function $\mathrm{tr}$ defined by Eq. ([\[Equ:tr-def\]](#Equ:tr-def){reference-type="ref" reference="Equ:tr-def"}) satisfies $\mathrm{tr}(\alpha\beta)=\mathrm{tr}(\beta\alpha)$ for all $\alpha,\beta\in H_{\infty}(\boldsymbol{u})$, we need the following lemmas.

::: lemma
[]{#Lemm:xs_nys_n label="Lemm:xs_nys_n"}For $x,y\in H_{n}(\boldsymbol{u})$, $$\begin{aligned}
\mathrm{tr}(xs_nys_n)=\mathrm{tr}(s_nxs_ny).
  
\end{aligned}$$ In particular, $$\begin{aligned}
 \mathrm{tr}(t_n^ks_ns_{n-1}s_n)=\mathrm{tr}(s_nt_n^{k}s_ns_{n-1}).
  
\end{aligned}$$
:::

::: proof
*Proof.* Clearly the second equality follows directly from the first one by letting $x=t_n^k$ and $y=s_{n-1}$. We use the case analysis to establish the first equality:

**Case 1:** $x,y\in H_{n-1}(\boldsymbol{u})$. Then $s_nx=xs_n$ and $s_ny=ys_n$, which implies $$\begin{aligned}
\mathrm{tr}(xs_nys_n)=\mathrm{tr}(xy)=\mathrm{tr}(s_nxs_ny).
  
\end{aligned}$$

**Case 2:** $x\in H_{n-1}(\boldsymbol{u})$ and $y=\alpha s_{n-1}\beta$ with $\alpha,\beta\in H_{n-1}(\boldsymbol{u})$, or vice versa. Then $s_nx=xs_n$, $s_n\alpha=\alpha s_n$, and $s_n\beta=\beta s_n$, which show $$\begin{aligned}
   \mathrm{tr}(xs_nys_n)&=\mathrm{tr}(xs_n\alpha s_{n-1}\beta s_n)=\mathrm{tr}(x \alpha s_{n-1}s_{n}s_{n-1}\beta)=z\mathrm{tr}(x\alpha\beta),\\
   \mathrm{tr}(s_nxs_ny)&=\mathrm{tr}(xy)=\mathrm{tr}(x\alpha s_{n-1}\beta)=z\mathrm{tr}(x\alpha\beta).
  
\end{aligned}$$

**Case 3:** $x=\alpha s_{n-1}\beta$ and $y=\delta s_{n-1}\gamma$ with $\alpha,\beta, \delta,\gamma\in H_{n-1}(\boldsymbol{u})$. Then $$\begin{aligned}
   \mathrm{tr}(\alpha s_{n-1}\beta s_n \delta s_{n-1}\gamma s_n)&=\mathrm{tr}(\alpha s_{n-1}\beta  \delta (s_ns_{n-1}s_n)\gamma )\\&=z\mathrm{tr}(\alpha s_{n-1}\beta \delta\gamma)\\&=z^2\mathrm{tr}(\alpha\beta\delta\gamma),\\
   \mathrm{tr}(s_n\alpha s_{n-1}\beta s_n \delta s_{n-1}\gamma)&=\mathrm{tr}(\alpha (s_ns_{n-1}s_n\beta\delta s_{n-1}\gamma)\\&=z\mathrm{tr}(\alpha\beta\delta s_{n-1}\gamma)\\&=z^2\mathrm{tr}(\alpha\beta\delta \gamma).
  
\end{aligned}$$

**Case 4:** $x=\alpha t_{n}^{\ell}$ and $y=\beta t_n^{k}$ with $\alpha, \beta\in H_{n-1}(\boldsymbol{u})$, $0\leq \ell,k<m$. Then $$\begin{aligned}
   \mathrm{tr}(\alpha t_{n}^{\ell}s_n\beta t_n^ks_n)&=\mathrm{tr}(\alpha t_{n}^{\ell}\beta (s_nt_n^ks_n))=y_k\mathrm{tr}(\alpha t_{n}^{\ell}\beta)=y_ky_{\ell}\mathrm{tr}(\alpha\beta),\\
   \mathrm{tr}(s_n\alpha t_{n}^{\ell}s_n\beta t_{n}^k)&=\mathrm{tr}(\alpha (s_nt_n^{\ell}s_n)\beta t_n^{k})=y_{\ell}\mathrm{tr}(\alpha\beta t_n^{k})=y_ky_{\ell}\mathrm{tr}(\alpha\beta).
  
\end{aligned}$$

**Case 5:** $x=\alpha s_{n-1}\beta$ and $y=\gamma t_n^{\ell}$ with $\alpha,\beta, \gamma\in H_{n-1}(\boldsymbol{u})$ and $1\leq \ell<m$, or vice versa. Then $$\begin{aligned}
   \mathrm{tr}(\alpha s_{n-1}\beta s_n\gamma t_{n}^{\ell}s_n)&=\mathrm{tr}(\alpha s_{n-1}\beta \gamma (s_nt_{n}^{\ell}s_n))\\&=y_{\ell}\mathrm{tr}(\alpha s_{n-1}\beta \gamma)\\&=zy_{\ell}\mathrm{tr}(\alpha\beta\gamma),\\
   \mathrm{tr}(s_n\alpha s_{n-1}\beta s_n\gamma t_{n}^{\ell})&=\mathrm{tr}(\alpha (s_n s_{n-1}s_n)\beta\gamma t_n^{\ell})\\&=z\mathrm{tr}(\alpha\beta\gamma t_n^{\ell})\\&=zy_{\ell}\mathrm{tr}(\alpha\beta\gamma).
  
\end{aligned}$$ We complete the proof. ◻
:::

::: lemma
[]{#Lemm:Type-II label="Lemm:Type-II"}For $h_{n}\in H_n(\boldsymbol{u})$ and $1\leq i\leq n-1$, we have $$\begin{aligned}
 &&\mathrm{tr}(h_{n}s_ns_{n-1}\cdots s_it)=\mathrm{tr}(th_{n}s_ns_{n-1}\cdots s_i)\\
 &&\mathrm{tr}(h_{n}s_ns_{n-1}\cdots s_is_j)=\mathrm{tr}(s_jh_{n}s_ns_{n-1}\cdots s_i) \text{ for }j=1, \ldots, n. 
\end{aligned}$$
:::

::: proof
*Proof.* By an induction argument, we obtain $$\begin{aligned}
\mathrm{tr}(h_{n-1}s_ns_{n-1}\cdots s_it)&=z\mathrm{\,tr}(h_{n}s_{n-1}\cdots s_it)\\
 &=z\mathrm{\,tr}(th_{n}s_{n-1}\cdots s_i)\\
 &=\mathrm{tr}(th_{n}s_n\cdots s_i). 
\end{aligned}$$ For $j=1, \ldots, n-1$, we have $$\begin{aligned}
 \mathrm{tr}(h_{n}s_n\cdots s_is_j)&=z\mathrm{\,tr}(h_{n}s_{n-1}\cdots s_is_j)\\
 &=z\mathrm{\,tr}(s_jh_{n}s_{n-1}\cdots s_i)\\
 &=\mathrm{tr}(s_jh_{n}s_n\cdots s_i), 
\end{aligned}$$ where the first equality and last one follow by using Theorem [\[Them:Markov\]](#Them:Markov){reference-type="ref" reference="Them:Markov"} (m3). For $j=n$, the second equality follows directly by applying Lemma [\[Lemm:xs_nys_n\]](#Lemm:xs_nys_n){reference-type="ref" reference="Lemm:xs_nys_n"}. ◻
:::

::: lemma
[]{#Lemm:Typer-III label="Lemm:Typer-III"}For $h_{n}\in H_{n}(\boldsymbol{u})$ and $1\leq i\leq n-1$, $$\begin{aligned}
\mathrm{tr}(h_{n}s_ns_{n-1}\cdots s_{i}t_{i}^ks_n)&=
\mathrm{tr}(s_nh_{n}s_ns_{n-1}\cdots s_{i}t_{i}^k),\\
\mathrm{tr}(h_{n}s_ns_{n-1}\cdots s_{i}t_{i}^kt)&=
\mathrm{tr}(th_{n}s_ns_{n-1}\cdots s_{i}t_{i}^k).
\end{aligned}$$
:::

::: proof
*Proof.* Clearly Lemma [\[Lemm:xs_nys_n\]](#Lemm:xs_nys_n){reference-type="ref" reference="Lemm:xs_nys_n"} implies the first equality and the second equality holds for $n=1$. Assume that the second equality holds for $n\geq 1$. We show it holds for $n+1$. By applying rule (m3), we obtain $$\begin{aligned}
\mathrm{tr}(h_{n}s_ns_{n-1}\cdots s_{i}t_{i}^kt)&=z\,
\mathrm{tr}(h_{n}s_{n-1}\cdots s_{i}t_{i}^kt)\\
&=z\,\mathrm{tr}(th_{n}s_{n-1}\cdots s_{i}t_{i}^k)\\
&=\mathrm{tr}(th_{n}s_ns_{n-1}\cdots s_{i}t_{i}^k).
\end{aligned}$$ Thus the proof is completed. ◻
:::

::: lemma
[]{#Lemm:Type-IV label="Lemm:Type-IV"}For $h_{n}\in H_{n}(\boldsymbol{u})$ and $1\leq k\leq m-1$, $$\begin{aligned}
\mathrm{tr}(h_{n}t_{n+1}^kt)&=\mathrm{tr}(th_{n}t_{n+1}^k),\\
\mathrm{tr}(h_{n}t_{n+1}^ks_i)&=\mathrm{tr}(s_ih_{n}t_{n+1}^k) \text{ for }i=1, \ldots, n.
\end{aligned}$$
:::

::: proof
*Proof.* Note that $s_{n,1}s_{2,n}=s_{1,n-1}s_ns_{n-1,1}$. Thanks to Lemma [\[Lemm:s-t\]](#Lemm:s-t){reference-type="ref" reference="Lemm:s-t"}(vi) and Eq. [\[Equ:tr-def\]](#Equ:tr-def){reference-type="eqref" reference="Equ:tr-def"}, we get $$\begin{aligned}
\mathrm{tr}(h_{n}t_{n+1}^kt)&=\mathrm{tr}(h_{n}tt_{n+1}^k)+\mathrm{tr}(h_{n}t^ks_{n,1}s_{2,n})
-\mathrm{tr}(h_{n}s_{n,2}s_{1,n}t^k)\\
&=y_k\mathrm{tr}(h_{n}t).
\end{aligned}$$ On the other hand, Eq. [\[Equ:tr-def\]](#Equ:tr-def){reference-type="eqref" reference="Equ:tr-def"} shows $$\begin{aligned}
\mathrm{tr}(th_{n}t_{n+1}^k)&=y_k\mathrm{tr}(th_{n}).
\end{aligned}$$ Finally the induction argument shows $\mathrm{tr}(th_{n})=\mathrm{tr}(h_{n}t)$. Thus the first equality holds.

For $i=1, \ldots, n-1$, we have $$\begin{aligned}
 t_{n+1}^ks_i&=s_n\cdots s_1t^ks_1\cdots s_{i-1}(s_is_{i+1}s_i)s_{i+2}\cdots s_n \\
 &=s_n\cdots s_1t^ks_1\cdots s_{i-1}s_{i+1}s_is_{i+1}s_{i+2}\cdots s_n\\
 &=s_n\cdots s_{i+2} (s_{i+1}s_is_{i+1})s_{i-1}\cdots s_1t^ks_1\cdots  s_n\\
 &=s_it_{n+1}^k.
\end{aligned}$$ Then Eq. [\[Equ:tr-def\]](#Equ:tr-def){reference-type="eqref" reference="Equ:tr-def"} implies $$\begin{aligned}
\mathrm{tr}(h_{n}t_{n+1}^ks_i)&=\mathrm{tr}(h_{n}s_it_{n+1}^k)=y_k\mathrm{tr}(h_{n}s_i).
\end{aligned}$$ While $\mathrm{tr}(s_ih_{n}t_{n+1}^k)=y_k\mathrm{tr}(s_ih_{n})$. Thus the second equality holds for $i=1, \ldots,n-1$ by the induction argument.

For $i=n$, clearly $$\begin{aligned}
 \mathrm{tr}(h_{n}t_{n+1}^ks_n)=\mathrm{tr}(h_{n}s_{n}t_n^{k})=z\,\mathrm{tr}(h_{n}t_n^{k}).
\end{aligned}$$ Case by case calculation shows: for $h_{n}\in H_{n-1}(\boldsymbol{u})$, $$\begin{aligned}
  \mathrm{tr}(s_nh_{n}t_{n+1}^k)=\mathrm{tr}(h_{n}t_{n}^ks_n)=z\,\mathrm{tr}(h_{n}t_{n}^k);
 
\end{aligned}$$ For $h_{n}=\alpha s_{n-1}\beta\in H_{n}(\boldsymbol{u})$ where $\alpha,\beta\in H_{n-1}(\boldsymbol{u})$, $$\begin{aligned}
\mathrm{tr}(s_nh_{n}t_{n+1}^k)&=
\mathrm{tr}((\alpha  s_{n-1})s_n(s_{n-1}\beta t_{n}^k)s_n)\\
&=\mathrm{tr}(s_n(\alpha  s_{n-1})s_n(s_{n-1}\beta t_{n}^k)) \quad \text{(Lemma~\ref{Lemm:xs_nys_n})}\\
&=\mathrm{tr}(\alpha s_{n-1}s_n\beta t_{n}^k)\\
&=z\,\mathrm{tr}(h_{n}t_{n}^k),
\end{aligned}$$ where the last equality follows by applying Eq. [\[Equ:tr-def\]](#Equ:tr-def){reference-type="eqref" reference="Equ:tr-def"};

For $h_{n}=\alpha t_{n}^{\ell}\in H_{n}(\boldsymbol{u})$ where $\alpha\in H_{n-1}(\boldsymbol{u})$ and $1\leq \ell\leq m-1$, $$\begin{aligned}
\mathrm{tr}(s_n\alpha t_n^{\ell} t_{n+1}^k)
&=\mathrm{tr}(\alpha s_n t_n^{\ell}t_{n+1}^k)\\
&=\mathrm{tr}(\alpha t_n^{k}s_nt_n^{\ell})+\sum_{i=1}^{\ell}\mathrm{tr}(\alpha t_{n+1}^{\ell-i}t_{n}^{k-i-2})-\sum_{i=1}^{\ell}\mathrm{tr}(\alpha t_{n+1}^{k-i-2}t_{n}^{\ell-i})\\
&=z\,\mathrm{tr}(h_{n}t_{n}^k),
\end{aligned}$$ where the second equality follows by applying Corollary [\[Cor:t-n-n+1\]](#Cor:t-n-n+1){reference-type="ref" reference="Cor:t-n-n+1"} and the last equality follows by applying Eq. [\[Equ:tr-def\]](#Equ:tr-def){reference-type="eqref" reference="Equ:tr-def"}. ◻
:::

Now we can show that the linear function $\mathrm{tr}$ defined by Eq. ([\[Equ:tr-def\]](#Equ:tr-def){reference-type="ref" reference="Equ:tr-def"}) is a trace on $H_{\infty}(\boldsymbol{u})$.

::: theorem
[]{#Them:alpha-beta=beta-alpha label="Them:alpha-beta=beta-alpha"}For all $\alpha,\beta\in H_{\infty}(\boldsymbol{u})$, $$\begin{aligned}
\mathrm{tr}(\alpha\beta)=\mathrm{tr}(\beta\alpha).
\end{aligned}$$
:::

::: proof
*Proof.* By induction argument, it suffices to show that $$\begin{aligned}
  \mathrm{tr}(\alpha s_i)=\mathrm{tr}(s_i\alpha)&\text{ and }
  \mathrm{tr}(\alpha t)=\mathrm{tr}(t\alpha)
\end{aligned}$$ for all $\alpha\in H_{n+1}(\boldsymbol{u})$ and $i=1,\ldots,n$. Thanks to Theorem [\[Them:Basis-for-Markov\]](#Them:Basis-for-Markov){reference-type="ref" reference="Them:Basis-for-Markov"}, if $\alpha$ is of type (a), the induction step implies $\mathrm{tr}(\alpha t)=\mathrm{tr}(t\alpha)$ and $\mathrm{tr}(\alpha s_i)=\mathrm{tr}(s_i\alpha)$ for $i=1, \ldots, n-1$. Further Eq. [\[Equ:tr-def\]](#Equ:tr-def){reference-type="eqref" reference="Equ:tr-def"} shows $$\mathrm{tr}(\alpha s_n)=z\mathrm{\,tr}(\alpha)=\mathrm{tr}(s_n\alpha).$$ For $\alpha$ being of type (b), (c) and (d), the assertion follows by applying Lemmas [\[Lemm:Type-II\]](#Lemm:Type-II){reference-type="ref" reference="Lemm:Type-II"}, [\[Lemm:Typer-III\]](#Lemm:Typer-III){reference-type="ref" reference="Lemm:Typer-III"} and [\[Lemm:Type-IV\]](#Lemm:Type-IV){reference-type="ref" reference="Lemm:Type-IV"} respectively. ◻
:::

Now we are ready to prove Theorem [\[Them:Markov\]](#Them:Markov){reference-type="ref" reference="Them:Markov"} in the introduction.

::: proof
*Proof of Theorem [\[Them:Markov\]](#Them:Markov){reference-type="ref" reference="Them:Markov"}.* (m1), (m3), (m4) follow from its construction (see Eq. [\[Equ:tr-def\]](#Equ:tr-def){reference-type="eqref" reference="Equ:tr-def"}, while (m2) derives from Theorem [\[Them:alpha-beta=beta-alpha\]](#Them:alpha-beta=beta-alpha){reference-type="ref" reference="Them:alpha-beta=beta-alpha"}. Uniqueness follows from Theorem [\[Them:Basis-for-Markov\]](#Them:Basis-for-Markov){reference-type="ref" reference="Them:Basis-for-Markov"}. ◻
:::

Let us remark that the uniqueness of the normalized Markov trace $\mathrm{tr}$ can be also proved by applying Geck and Lambropoulou's argument in [@GL Lemma 4.2]. More precisely, we have the following fact.

::: lemma
Let $\tau: H_n(\boldsymbol{u})\rightarrow\mathbb{C}(\boldsymbol{u},z)$ be a normalized Markov trace. If $n\geq 1$, $k\geq 1$, $h\in H_{n}$, and $1 \leq i_2,\ldots, i_{k}\leq m-1$, then $$\begin{aligned}
     \tau(hs_{n}t_{n+2}^{i_2}\cdots t_{n+k}^{i_k})&=z\tau(ht_{n+1}^{i_2}t_{n+2}^{i_3}\cdots t_{n+k-1}^{i_k})
   
\end{aligned}$$ and $$\begin{aligned}
     \tau(ht_{n+2}^{i_2}\cdots t_{n+k}^{i_k})&=\tau(ht_{n+1}^{i_2}t_{n+2}^{i_3}\cdots t_{n+k-1}^{i_k}).
   
\end{aligned}$$
:::

::: proof
*Proof.* We prove the first equality by an induction argument on $k$. For $k=1$, it follows directly by applying Definition [\[Def:Markov-traces\]](#Def:Markov-traces){reference-type="ref" reference="Def:Markov-traces"}. Now we assume that $k>1$. Then we have $$\begin{aligned}
     \tau(hs_{n}t_{n+2}^{i_2}\cdots t_{n+k}^{i_k})&=\tau(hs_{n}s_{n+1}t_{n+1}^{i_2}s_{n+1}t_{n+3}^{i_3}\cdots t_{n+k}^{i_k})&\mathrm{(}t_{n+2}=s_{n+1}t_{n+1}s_{n+1}\mathrm{)}\\
     &=\tau(hs_{n}s_{n+1}t_{n+1}^{i_2}t_{n+3}^{i_3}\cdots t_{n+k}^{i_k}s_{n+1})
     &(\text{The proof of Lemma}~\ref{Lemm:Type-IV})\\
     &=\tau(s_{n+1}hs_{n}s_{n+1}t_{n+1}^{i_2}t_{n+3}^{i_3}\cdots t_{n+k}^{i_k})&(\tau \text{ is a trace})\\
     &=\tau(hs_{n+1}s_{n}s_{n+1}t_{n+1}^{i_2}t_{n+3}^{i_3}\cdots t_{n+k}^{i_k})&(hs_{n+1}=s_{n+1}h)\\
     &=\tau(hs_ns_{n+1}s_{n}t_{n+1}^{i_2}t_{n+3}^{i_3}\cdots t_{n+k}^{i_k})&(\text{Braid relations})\\
     &=\tau(hs_nt_{n}^{i_2}s_{n+1}s_nt_{n+3}^{i_3}\cdots t_{n+k}^{i_k})&(s_{n+1}t_n=t_ns_{n+1})\\
     &=\tau(hs_nt_{n}^{i_2}s_{n+1}t_{n+3}^{i_3}\cdots t_{n+k}^{i_k}s_n)&(\text{The proof of Lemma}~\ref{Lemm:Type-IV})\\
     &=\tau((s_nhs_nt_{n}^{i_2})s_{n+1}t_{n+3}^{i_3}\cdots t_{n+k}^{i_k})&(\tau \text{ is a trace})\\
     &=z\tau(s_nhs_nt_{n}^{i_2}t_{n+2}^{i_3}\cdots t_{n+k-1}^{i_k})&(\text{Induction})\\
     &=z\tau(hs_nt_{n}^{i_2}t_{n+2}^{i_3}\cdots t_{n+k-1}^{i_k}s_n)&(\tau \text{ is a trace})\\
     &=z\tau(hs_nt_{n}^{i_2}s_nt_{n+2}^{i_3}\cdots t_{n+k-1}^{i_k})&(\text{The proof of Lemma}~\ref{Lemm:Type-IV})\\
     &=z\tau(ht_{n+1}^{i_2}t_{n+2}^{i_3}\cdots t_{n+k-1}^{i_k}).
   
\end{aligned}$$ The second can be proved by an analogue computation. ◻
:::
