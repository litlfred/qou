---
doc_id: arxiv-2409.09372v4
doc_title: "Markov traces on degenerate cyclotomic Hecke algebras"
section_id: sec-003-4-non-normalized-markov-traces
section_title: "Non-normalized Markov traces"
section_number: 4
pages: 10-13
source_pdf: 2409.09372v4.pdf
source_sha256: b7eed67ec102ab3d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.839
doc_brief: "Markov traces on degenerate cyclotomic Hecke algebras — Let Hn(u) be the degenerate cyclotomic Hecke algebra with parameter u = {u1, . . . , um}."
---
[]{#Sec:BK-trace label="Sec:BK-trace"} In this section we construct a $\mathbb{C}(\boldsymbol{u})$--linear function on $H_n(\boldsymbol{u})$ by using the standard bases and show it constitutes a non-normalized Markov trace, thereby proving Theorem [\[Them:Markov-BK\]](#Them:Markov-BK){reference-type="ref" reference="Them:Markov-BK"} from the introduction.

The following easy verified fact will be useful.

::: lemma
[]{#Lemm:J-s_n label="Lemm:J-s_n"} For integers $1 \leq k\leq m-1$ and $n \geq 1$, we have $$\begin{aligned}
J_{n+1}^k s_n &= s_n J_n^k + \sum_{i=0}^{k-1} J_{n+1}^{k-1-i} J_n^i.
\end{aligned}$$
:::

::: proof
*Proof.* Apply induction on $k$ and $k=1$ follows by applying Eq. [\[Equ:JM-H\]](#Equ:JM-H){reference-type="eqref" reference="Equ:JM-H"}. Assume that it holds for $k-1\geq 1$. For $k$, $$\begin{aligned}
J_{n+1}^{k} s_n &= J_{n+1}^{k-1}(s_nJ_n+1)\\
&= \biggl(s_n J_n^{k-1} + \sum_{i=0}^{k-2} J_{n+1}^{k-2-i} J_n^i\biggr)J_n+J_{n+1}^{k-1}\\
&=s_nJ_n^{k}+\sum_{i=0}^{k-2} J_{n+1}^{k-2-i} J_n^{i+1}+J_{n+1}^{k-1}\\
&= s_n J_n^k + \sum_{i=0}^{k-1} J_{n+1}^{k-1-i} J_n^i.
\end{aligned}$$ The proof is completed. ◻
:::

::: lemma
[]{#Lemm:Bimodules-iso-JM label="Lemm:Bimodules-iso-JM"} Define the bimodule map $$\psi_n: H_n(\boldsymbol{u}) \otimes_{H_{n-1}(\boldsymbol{u})} H_n(\boldsymbol{u}) \oplus \biggl(\bigoplus_{i=0}^{m-1} H_n(\boldsymbol{u})\biggr) \to H_{n+1}(\boldsymbol{u})$$ by $$a \otimes b \oplus \biggl(\bigoplus_{i=0}^{m-1} a_i\biggr) \mapsto a s_n b + \sum_{i=0}^{m-1} a_i J_{n+1}^i.$$ Then $\psi_n$ is an $H_n(\boldsymbol{u})$-bimodule isomorphism.
:::

::: proof
*Proof.* Analogous to Lemma [\[Lemm:Bimodules-iso\]](#Lemm:Bimodules-iso){reference-type="ref" reference="Lemm:Bimodules-iso"}'s proof using standard basis arguments. ◻
:::

Given $z, y_1, \ldots, y_{m-1}\in \mathbb{C}(\boldsymbol{u})$, we inductively define a $\mathbb{C}(\boldsymbol{u})$-linear function $\mathrm{Tr}$ on $H_\infty(\boldsymbol{u})$ as follows. Assume $\mathrm{Tr}$ is defined on $H_n(\boldsymbol{u})$. For $x \in H_{n+1}(\boldsymbol{u})$ decomposed via Lemma [\[Lemm:Bimodules-iso-JM\]](#Lemm:Bimodules-iso-JM){reference-type="ref" reference="Lemm:Bimodules-iso-JM"} as $$x = \psi_n\biggl(a \otimes b \oplus \biggl(\bigoplus_{k=0}^{m-1} \alpha_k J_{n+1}^k\biggr)\biggr),$$ we define $$\label{Equ:tr-def-JM}
\mathrm{Tr}(x) :=z\cdot\mathrm{Tr}(ab) + \mathrm{Tr}(\alpha_0) + \sum_{k=1}^{m-1} \mathrm{Tr}(J_{n+1}^k) \mathrm{Tr}(\alpha_k),$$ where $\mathrm{Tr}(1) = 0$ and $\mathrm{Tr}(J_{n+1}^k)$ determined by:

-   $\mathrm{Tr}(h s_n J_{n}^k s_n) = \mathrm{Tr}(J_{n}^k) \mathrm{Tr}(h)$ for all $h \in H_n(\boldsymbol{u})$ and for all $1 \leq k \leq m-1$;

-   $\mathrm{Tr}(J_1^k) =y_k$ for all $k=1,\ldots,m-1$.

Let us remark that (M4) and Lemma [\[Lemm:J-s_n\]](#Lemm:J-s_n){reference-type="ref" reference="Lemm:J-s_n"} show that $$\mathrm{Tr}(J_{n+1}^k)=\mathrm{Tr}(J_{n}^k)+\sum_{i=0}^{k-1} \mathrm{Tr}(J_n^iJ_{n+1}^{k-1-i}s_n)$$ for $1\leq k\leq m-1$, $n=1,2,\ldots$.

::: proposition
[]{#Prop:Tr-M label="Prop:Tr-M"} The $\mathbb{C}(\boldsymbol{u})$--linear function $\mathrm{Tr}$ satisfies

1.  $\mathrm{Tr}(s_n) = z$ for all $n \geq 1$;

2.  $\mathrm{Tr}(x s_n y) = z\cdot\mathrm{Tr}(xy)$ for all $x,y \in H_n(\boldsymbol{u})$;

3.  $\mathrm{Tr}(s_n J_n^k s_n) = \mathrm{Tr}(J_n^k)$ for $1 \leq k \leq m-1$ and for all $n\geq 1$.
:::

::: proof
*Proof.* (M1, M3) follows directly from Eq. [\[Equ:tr-def-JM\]](#Equ:tr-def-JM){reference-type="eqref" reference="Equ:tr-def-JM"} via bimodule structure, while (M4') is immediate from (M4). ◻
:::

::: remark
This trace construction specializes to the Brundan--Kleshchev trace $\tau_{\mathrm{BK}}$ through parameter specialization, analogous to [@GIM Lemma 4.3]. The non-normalized condition $\mathrm{Tr}(1)=0$ distinguishes it from the normalized Markov traces while preserving essential conjugation properties.
:::

We now show that the $\mathbb{C}(\boldsymbol{u})$--linear function $\mathrm{Tr}$ defined by Eq. [\[Equ:tr-def-JM\]](#Equ:tr-def-JM){reference-type="eqref" reference="Equ:tr-def-JM"} is a trace on $H_{\infty}(\boldsymbol{u})$, i.e., $$\mathrm{Tr}(\alpha\beta) = \mathrm{Tr}(\beta\alpha) \quad \text{ for all } \alpha,\beta \in H_{\infty}(\boldsymbol{u}).$$ Our approach follows arguments parallel to those in Section [\[Sec:Markov-traces\]](#Sec:Markov-traces){reference-type="ref" reference="Sec:Markov-traces"}.

::: lemma
[]{#Lemm:tr(xJy)=tr(xy) label="Lemm:tr(xJy)=tr(xy)"} For any $x,y \in H_n(\boldsymbol{u})$ and $1 \leq k\leq m-1$, $$\mathrm{Tr}(xJ_{n+1}^k y) = \mathrm{Tr}(J_{n+1}^k) \mathrm{Tr}(xy).$$
:::

::: proof
*Proof.* Let $w \in \mathfrak{S}_n$ be expressed in Jones normal form: $$\begin{aligned}
    w = (s_{i_1}s_{i_1-1}\cdots s_{k_1})(s_{i_2}s_{i_2-1}\cdots s_{k_2}) \cdots (s_{i_r}s_{i_r-1}\cdots s_{k_r}),
\end{aligned}$$ where $0 < i_1 < \cdots < i_r < n$, $0 < k_1 < \cdots < k_r \leq n-1$, and $i_j \geq k_j$ for all $j$. By Eq. [\[Equ:Standard-basis\]](#Equ:Standard-basis){reference-type="eqref" reference="Equ:Standard-basis"}, we may assume that $y = J_1^{a_1}\cdots J_n^{a_n}w' s_{n-1}$, where $0 \leq a_i\leq m-1$ and $w' \in \mathfrak{S}_{n-1}$.

Applying Lemma [\[Lem:si-Jj\]](#Lem:si-Jj){reference-type="ref" reference="Lem:si-Jj"}(ii, iii) for commutation relations: $$\begin{aligned}
    \mathrm{Tr}(xJ_{n+1}^k y) &= \mathrm{Tr}(xJ_{n+1}^k J_1^{a_1}\cdots J_n^{a_n}w's_{n-1}) \\
    &= \mathrm{Tr}(xJ_1^{a_1}\cdots J_n^{a_n} w's_{n-1} J_{n+1}^{k}) \quad \text{(Lemma~\ref{Lem:si-Jj})} \\
    &= \mathrm{Tr}(xy) \mathrm{Tr}(J_{n+1}^k). 
\end{aligned}$$ It completes the proof. ◻
:::

::: lemma
[]{#Lemm:JM-xs_nys_n label="Lemm:JM-xs_nys_n"} For sll $x,y\in H_{n}(\boldsymbol{u})$, $$\mathrm{Tr}(xs_nys_n) = \mathrm{Tr}(s_nxs_ny).$$ In particular, for all $1\leq k\leq m-1$, $$\mathrm{Tr}(J_n^ks_ns_{n-1}s_n) = \mathrm{Tr}(s_nJ_n^{k}s_ns_{n-1}).$$
:::

::: proof
*Proof.* The second equality follows from the first by taking $x = J_n^k$ and $y = s_{n-1}$. We establish the first equality through case by case analysis:

**Case 1.** $x,y \in H_{n-1}(\boldsymbol{u})$: $$\begin{aligned}
    \mathrm{Tr}(xs_nys_n) &= \mathrm{Tr}(xy) = \mathrm{Tr}(s_nxs_ny).
\end{aligned}$$ **Case 2.** $x \in H_{n-1}(\boldsymbol{u})$, $y = \alpha s_{n-1}\beta$ where $\alpha,\beta\in H_{n-1}(\boldsymbol{u})$, or vice versa: $$\begin{aligned}
    \mathrm{Tr}(xs_nys_n) &=\mathrm{Tr}(x\alpha(s_ns_{n-1}s_n)\beta)=\mathrm{Tr}(s_nxs_ny).
\end{aligned}$$ **Case 3.** $x = \alpha s_{n-1}\beta$, $y = \delta s_{n-1}\gamma$ where $\alpha,\beta,\delta,\gamma\in H_{n-1}(\boldsymbol{u})$: $$\begin{aligned}
    \mathrm{Tr}(xs_nys_n) &=\mathrm{Tr}(\alpha s_{n-1}\beta\delta(s_ns_{n-1}s_n)\gamma)= z^2\,\mathrm{Tr}(\alpha\beta\delta\gamma), \\
    \mathrm{Tr}(s_nxs_ny) &=\mathrm{Tr}(\alpha (s_ns_{n-1}s_n)\beta\delta s_{n-1}\gamma)= z^2\,\mathrm{Tr}(\alpha\beta\delta\gamma).
\end{aligned}$$ **Case 4.** $x \in H_{n-1}(\boldsymbol{u})$, $y = \alpha J_n^{\ell}$ where $\alpha\in H_{n-1}(\boldsymbol{u})$ and $1\leq\ell\leq m-1$, or vice versa: $$\begin{aligned}
    \mathrm{Tr}(xs_nys_n)&=\mathrm{Tr}(x\alpha s_nJ_n^{\ell}s_n)=
    \mathrm{Tr}(J_n^{\ell})\mathrm{Tr}(x\alpha), \\
    \mathrm{Tr}(s_nxs_ny) &=\mathrm{Tr}(x\alpha J_n^{\ell})= \mathrm{Tr}(J_n^{\ell})\mathrm{Tr}(x\alpha).
\end{aligned}$$ **Case 5.** $x = \alpha J_n^{\ell}$, $y = \beta J_n^k$ where $\alpha,\beta\in H_{n-1}(\boldsymbol{u})$ and $1\leq k, \ell\leq m-1$: $$\begin{aligned}
 \mathrm{Tr}(xs_nys_n)&= \mathrm{Tr}(\alpha\beta J_n^{\ell}s_nJ_n^ks_n)=\mathrm{tr}(J_n^{k})\mathrm{tr}(J_n^{\ell})\mathrm{Tr}(\alpha\beta), \\
\mathrm{Tr}(s_nxs_ny)&= \mathrm{Tr}(\alpha s_nJ_n^{\ell}s_nJ_n^k\beta)=\mathrm{tr}(J_n^{\ell})\mathrm{Tr}(J_n^k)\mathrm{Tr}(\alpha\beta).
\end{aligned}$$

**Case 6.** $x = \alpha s_{n-1}\beta$, $y = \gamma J_n^{\ell}$ where $\alpha,\beta,\gamma\in H_{n-1}(\boldsymbol{u})$, or vice versa: $$\begin{aligned}
    \mathrm{Tr}(xs_nys_n) &=\mathrm{Tr}(\alpha s_{n-1}\beta\gamma s_n J_n^{\ell}s_n)= z\,\mathrm{Tr}(J_n^{\ell})\mathrm{Tr}(\alpha\beta\gamma), \\
    \mathrm{Tr}(s_nxs_ny) &=\mathrm{Tr}(\alpha s_ns_{n-1}s_n\beta\gamma J_n^{\ell})= z\,\mathrm{Tr}(J_n^{\ell})\mathrm{Tr}(\alpha\beta\gamma).
\end{aligned}$$ All cases demonstrate the required equality, thus completing the proof. ◻
:::

::: lemma
[]{#Lemm:JM-Typer-III label="Lemm:JM-Typer-III"} For any $h_n \in H_n(\boldsymbol{u})$, $1 \leq i\leq n-1$, and $1 \leq k\leq m-1$, $$\begin{aligned}
    \mathrm{Tr}(h_n s_n s_{n-1} \cdots s_i J_i^k s_n) &=
    \mathrm{Tr}(s_n h_n s_n s_{n-1} \cdots s_i J_i^k), \\
    \mathrm{Tr}(h_n s_n s_{n-1} \cdots s_i J_i^k t) &=
     \mathrm{Tr}(t h_n s_n s_{n-1} \cdots s_i J_i^k).
\end{aligned}$$
:::

::: proof
*Proof.* For the **first equality**, we have $$\begin{aligned}
    \mathrm{Tr}(h_n s_n s_{n-1} \cdots s_i J_i^k s_n)
    &= \mathrm{Tr}(h_n s_n s_{n-1} s_n s_{n-2} \cdots s_i J_i^k) \\
    &= z\,\mathrm{Tr}(h_n s_{n-2} \cdots s_i J_i^k).
\end{aligned}$$ For $\mathrm{Tr}(s_n h_n s_n s_{n-1} \cdots s_i J_i^k)$, we apply the case by case analysis:

[Case 1.]{.underline} $h_n \in H_{n-1}(\boldsymbol{u})$: $$\begin{aligned}
    \mathrm{Tr}(s_n h_n s_n s_{n-1} \cdots s_i J_i^k)
    &= \mathrm{Tr}(h_n s_{n-1} \cdots s_i J_i^k) \\
    &= z\,\mathrm{Tr}(h_n s_{n-2} \cdots s_i J_i^k).
\end{aligned}$$

[Case 2.]{.underline} $h_n = \alpha s_{n-1} \beta$ where $\alpha, \beta \in H_{n-1}(\boldsymbol{u})$: $$\begin{aligned}
    \mathrm{Tr}(s_n h_n s_n \cdots s_i J_i^k)
    &= \mathrm{Tr}(\alpha s_n s_{n-1} s_n \beta s_{n-1} \cdots s_i J_i^k) \\
    &= z^2\,\mathrm{Tr}(\alpha \beta s_{n-2} \cdots s_i J_i^k) \\
    &= z\,\mathrm{Tr}(h_n s_{n-2} \cdots s_i J_i^k).
\end{aligned}$$

[Case 3.]{.underline} $h_n = \alpha J_n^\ell$ where $\alpha \in H_{n-1}(\boldsymbol{u}), 1 \leq \ell\leq m -1$: $$\begin{aligned}
    \mathrm{Tr}(s_n h_n s_n \cdots s_i J_i^k)
    &= \mathrm{Tr}(\alpha (s_n J_n^\ell s_n) s_{n-1} \cdots s_i J_i^k) \\
    &= z\,\mathrm{Tr}(J_n^\ell) \mathrm{Tr}(\alpha s_{n-2} \cdots s_i J_i^k) \\
    &= z\,\mathrm{Tr}(h_n s_{n-2} \cdots s_i J_i^k).
\end{aligned}$$ Thus, the first equality holds.

**Second Equality:** By induction on $n$. It is trivial for $n = 1$. Assume it is true for $n \geq 1$. For $n+1$, we have $$\begin{aligned}
    \mathrm{Tr}(h_{n+1} s_{n+1} \cdots s_i J_i^k t)
    &= z\,\mathrm{Tr}(h_{n+1} s_{n} \cdots s_i J_i^k t) \quad \text{(by (M3))} \\
    &= z\,\mathrm{Tr}(t h_{n+1} s_{n} \cdots s_i J_i^k) \quad \text{(inductive hypothesis)} \\
    &= \mathrm{Tr}(t h_{n+1} s_{n+1} \cdots s_i J_i^k).
\end{aligned}$$ This completes the proof. ◻
:::

::: lemma
[]{#Lemm:JM-Type-IV label="Lemm:JM-Type-IV"}For any $h_{n}\in H_{n}(\boldsymbol{u})$, $i=1, \ldots, n$, and $1\leq k\leq m-1$, we have $$\begin{aligned}
\mathrm{Tr}(h_{n}J_{n+1}^kt)&=&\mathrm{Tr}(th_{n}J_{n+1}^k),\\
\mathrm{Tr}(h_{n}J_{n+1}^ks_i)&=&\mathrm{Tr}(s_ih_{n}J_{n+1}^k).
\end{aligned}$$
:::

::: proof
*Proof.* Thanks to Lemma [\[Lemm:s-t\]](#Lemm:s-t){reference-type="ref" reference="Lemm:s-t"}(vi), $$\begin{aligned}
\mathrm{Tr}(h_{n}J_{n+1}^kt)&=\mathrm{Tr}(J_{n+1}^k)\mathrm{Tr}(h_{n}t)=\mathrm{Tr}(J_{n+1}^k)
\mathrm{Tr}(th_{n})=\mathrm{Tr}(th_{n}J_{n+1}^k),
\end{aligned}$$ where the second equality follows by the induction argument on $n$. Thus the first equality holds.

Now we show the second equality holds. For $i=1, \ldots, n-1$, $$\begin{aligned}
\mathrm{Tr}(h_{n}J_{n+1}^ks_i)=\mathrm{Tr}(J_{n+1}^k)\mathrm{Tr}(h_{n}s_i)
=\mathrm{Tr}(J_{n+1}^k)\mathrm{Tr}(s_ih_{n})
=\mathrm{Tr}(s_ih_{n}J_{n+1}^k),
\end{aligned}$$ where the middle equality uses the induction hypothesis $\mathrm{Tr}(h_{n}s_i)=\mathrm{Tr}(s_ih_{n})$.

Now Lemma [\[Lemm:J-s_n\]](#Lemm:J-s_n){reference-type="ref" reference="Lemm:J-s_n"} and Eq. [\[Equ:tr-def-JM\]](#Equ:tr-def-JM){reference-type="eqref" reference="Equ:tr-def-JM"} show $$\begin{aligned}
\mathrm{Tr}(h_{n}J_{n+1}^ks_n)&=z\,\mathrm{Tr}(h_{n}J_n^{k})+
\sum_{i=0}^{k-1}\mathrm{Tr}(h_nJ_{n}^iJ_{n+1}^{k-1-i}).
\end{aligned}$$

On the other hand, if $h_{n}\in H_{n-1}(\boldsymbol{u})$ then $s_nh_n=h_ns_n$ and Lemma [\[Lemm:J-s_n\]](#Lemm:J-s_n){reference-type="ref" reference="Lemm:J-s_n"} shows $$\begin{aligned}
\mathrm{Tr}(s_nh_{n}J_{n+1}^k)&=&z\,\mathrm{Tr}(h_{n}J_n^{k})+
\sum_{i=0}^{k-1}\mathrm{tr}(h_nJ_{n}^iJ_{n+1}^{k-1-i}).
\end{aligned}$$

If $h_{n}=\alpha s_{n-1}\beta\in H_{n}(\boldsymbol{u})$ where $\alpha,\beta\in H_{n-1}(\boldsymbol{u})$, then $$\begin{aligned}
\mathrm{Tr}(s_n\alpha s_{n-1}\beta J_{n+1}^k)
&=\mathrm{Tr}(\alpha (s_n J_{n+1}^k)s_{n-1}\beta)\\
&=z\,\mathrm{Tr}(\alpha J_n^{k}s_{n-1}\beta)+
\sum_{i=0}^{k-1}\mathrm{Tr}(\alpha J_{n}^iJ_{n+1}^{k-1-i}s_{n-1}\beta)\\
&=z\,\mathrm{Tr}(h_{n}J_n^{k})+
\sum_{i=0}^{k-1}\mathrm{Tr}(h_nJ_{n}^iJ_{n+1}^{k-1-i}),
\end{aligned}$$ where the last equality follows by an induction argument.

If $h_{n}=\alpha J_{n}^{\ell}\in H_{n}(\boldsymbol{u})$ where $\alpha\in H_{n-1}(\boldsymbol{u})$ and $1\leq \ell\leq m-1$, then $$\begin{aligned}
\mathrm{Tr}(s_n\alpha J_n^{\ell} J_{n+1}^k)&=\mathrm{Tr}(\alpha (s_n J_{n+1}^k)J_n^{\ell})\\
&=z\,\mathrm{Tr}(\alpha J_n^{k+\ell})+\sum_{i=0}^{k-1}\mathrm{Tr}(\alpha J_{n}^iJ_{n+1}^{k-1-i}J_n^{\ell})\\
&=z\,\mathrm{Tr}(h_{n}J_n^{k})+
\sum_{i=0}^{k-1}\mathrm{Tr}(h_nJ_{n}^iJ_{n+1}^{k-1-i}).
\end{aligned}$$ Thus $\mathrm{Tr}(h_{n}J_{n+1}^ks_n)=\mathrm{Tr}(s_nh_{n}J_{n+1}^k)$ holds in all cases. It completes the proof. ◻
:::

We are ready to show $\mathrm{Tr}$ is a trace function on $H_{\infty}(\boldsymbol{u})$.

::: theorem
[]{#Them:ab=ba label="Them:ab=ba"}For all $a,b\in H_{\infty}(\boldsymbol{u})$, $$\begin{aligned}
\mathrm{Tr}(ab)=\mathrm{Tr}(ba).
\end{aligned}$$
:::

::: proof
*Proof.* We verify $\mathrm{Tr}(ax)=\mathrm{Tr}(xa)$ inductively. Assume it holds for all $a, b\in H_{n}(\boldsymbol{u})$. For $a, b\in H_{n+1}(\boldsymbol{u})$, it suffices to check when $b$ is a generator $s_i$ ($1\leq i\leq n$) or $t$, that is, $$\begin{aligned}
(*)\qquad\quad\mathrm{Tr}(at)=\mathrm{Tr}(ta) \text{ and } \mathrm{Tr}(as_i)=\mathrm{Tr}(s_ia)\text{ for }1\leq i\leq n.
\end{aligned}$$ Thanks to Theorem [\[Them:Inductive-basis\]](#Them:Inductive-basis){reference-type="ref" reference="Them:Inductive-basis"}, we only need to check that Eq. $(*)$ holds when $a$ is an element of the four forms (I)---(IV): If $a$ is an element of form (I), i.e., $a=h_n\in H_n(\boldsymbol{u})$, then the induction hypothesis gives $$\mathrm{Tr}(h_nt)=\mathrm{Tr}(th_n)\text{ and }\mathrm{Tr}(h_ns_i)=\mathrm{Tr}(s_ih_n)\text{ for }i=1, \ldots, n-1.$$ Further Proposition [\[Prop:Tr-M\]](#Prop:Tr-M){reference-type="ref" reference="Prop:Tr-M"}(M3) shows $$\mathrm{Tr}(as_n)=z\,\mathrm{Tr}(a)=\mathrm{Tr}(s_na).$$ If $a$ is an element of forms (II)---(IV), the assertion follows directly form Lemmas [\[Lemm:JM-xs_nys_n\]](#Lemm:JM-xs_nys_n){reference-type="ref" reference="Lemm:JM-xs_nys_n"}, [\[Lemm:JM-Typer-III\]](#Lemm:JM-Typer-III){reference-type="ref" reference="Lemm:JM-Typer-III"}, and [\[Lemm:JM-Type-IV\]](#Lemm:JM-Type-IV){reference-type="ref" reference="Lemm:JM-Type-IV"}. ◻
:::

Now we can prove Theorem [\[Them:Markov-BK\]](#Them:Markov-BK){reference-type="ref" reference="Them:Markov-BK"} in Introduction.

::: proof
*Proof of Theorem [\[Them:Markov-BK\]](#Them:Markov-BK){reference-type="ref" reference="Them:Markov-BK"}.* (M1), (M3)--(M5) follow directly by Eq. [\[Equ:tr-def-JM\]](#Equ:tr-def-JM){reference-type="eqref" reference="Equ:tr-def-JM"} and (M2) follows by applying Theorem [\[Them:ab=ba\]](#Them:ab=ba){reference-type="ref" reference="Them:ab=ba"}. Note that having proved the existence, the uniqueness of $\mathrm{Tr}$ follows immediately. Indeed Theorem [\[Them:Inductive-basis\]](#Them:Inductive-basis){reference-type="ref" reference="Them:Inductive-basis"} shows that $\mathrm{Tr}(x)$ can be clearly computed inductively using rules (M1)--(M4) for any $x\in H_{n+1}(\boldsymbol{u})$. ◻
:::
