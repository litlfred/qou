---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-060-142-powers-of-the-ribbon-element-and-the-twist-e
section_title: "Powers of the ribbon element and the twist element"
section_number: 14.2
pages: 54-56
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
toc_source: inferred
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.836
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — We construct an invariant JM of integral homology spheres M with values in a completion d Z[q] of the polynomial ring"
---
[]{#sec:powers-ribb-elem label="sec:powers-ribb-elem"} Here we give formulas for the powers of the ribbon element $\modr$ and the twist element $\omega$.

For $p,n\ge 0$, set $$S(n,p) = \{(i_1,\ldots,i_p)\zzzvert i_1,\ldots,i_p\ge 0,\quad i_1+\cdots+i_p=n\}.$$ For $\modi =(i_1,\ldots,i_p)\in S(n,p)$, set $\bbq{n}{\modi }=\frac{[n]_q!}{[n_1]_q!\cdots[n_p]_q!}$, $f(\modi )=\sum_{j=1}^{p-1}(s_j^2+s_j)$ with $s_j=\sum_{k=1}^ji_k$, and $g(\modi )=\sum_{j=1}^p(p-j)i_j$.

::: proposition
[]{#r8 label="r8"} For $p\ge 0$, we have $$\begin{gathered}
    \modr ^{-p}
    = v^{\frac p2 H(H+2)}\sum_{n\ge 0}v^{\hf n(n+3)}
    \Bigl(\sum_{\modi \in S(n,p)}\bbq{n}{\modi }q^{f(\modi )}K^{2g(\modi )}\Bigr)
    K^nF^{(n)}e^n,\\
    \modr ^p
    = v^{-\frac p2 H(H+2)}
    \sum_{n\ge 0}(-1)^nv^{-\hf n(n+3)}
    \Bigl(\sum_{\modi \in S(n,p)}\bb{n}{\modi }_{q^{-1}}q^{-f(\modi )}K^{-2g(\modi )}\Bigr)
    K^{-n}F^{(n)}e^n,
  
\end{gathered}$$ where $\bb{n}{\modi }_{q^{-1}}\Bigl(=q^{-\sum_{1\le j<k\le p}i_ji_k}\bbq{n}\modi \Bigr)$ is the conjugate of $\bbq{n}{\modi }$.
:::

::: proof
*Proof.* We only prove the first formula. The other can be similarly proved.

Define $a_{p,n}\in U_h^0$ by $$\label{e14}
    \modr ^{-p}
    = v^{\frac p2 H(H+2)}\sum_{n\ge 0}v^{\hf n(n+3)}a_{p,n}
    K^nF^{(n)}e^n.$$ We have $a_{0,n}=\delta _{n,0}$ and $a_{1,n}=1$.

Since $\modr$ is central, we have $$\begin{split}
      \modr ^{-p-1}
      &=v^{\frac p2 H(H+2)}\sum_{i\ge 0}v^{\hf i(i+3)}a_{p,i}
      K^iF^{(i)}
      \Bigl(v^{\hf H(H+2)}\sum_{j\ge 0}v^{\hf j(j+3)}
      K^jF^{(j)}e^j\Bigr) e^i\\
      &=v^{\frac {p+1}2 H(H+2)}
      \sum_{k\ge 0}v^{\hf k(k+3)}
      \Bigl(
      \sum_{i=0}^k a_{p,i} \bbq{k}{i} q^{i^2+i} K^{2i}
      \Bigr)
      K^kF^{(k)}e^{k}.
    \end{split}$$ Hence, we have $$a_{p+1,k}=\sum_{i=0}^k a_{p,i} \bbq{k}{i} q^{i^2+i} K^{2i}.$$ By induction using this formula, we can verify for $p\ge 0$ $$\label{e16}
    a_{p,n}=\sum_{\modi \in S(n,p)}\bbq{n}{\modi }q^{f(\modi )}K^{2g(\modi )}.$$ ◻
:::

We can derive formulas for the powers of $\omega$ from Proposition [\[r8\]](#r8){reference-type="ref" reference="r8"} as follows.

::: proposition
[]{#r5 label="r5"} For $p\in \modZ$, we have $$\label{e13}
    \omega ^p = \sum_{n\ge 0} \omega _{p,n}P'_n,$$ where $$\begin{gathered}
    \omega _{p,n} =
    \begin{cases}
      v^{\hf n(n+3)}
      \sum_{\;\modi \in S(n,p)}\bbq{n}{\modi }q^{f(\modi )}&{\text{for $p\ge 0$}},\\
      (-1)^nv^{-\hf n(n+3)}
      \sum_{\;\modi \in S(n,-p)}\bb{n}{\modi }_{q^{-1}}q^{-f(\modi )}&{\text{for $p\le 0$.}}
    \end{cases}
  
\end{gathered}$$
:::

::: proof
*Proof.* Since the proof is similar to that of Proposition [\[thm:38\]](#thm:38){reference-type="ref" reference="thm:38"}, we give only a sketch proof. We consider only the case $p\ge 0$; the other case follows by symmetry.

We can express $\omega ^p$ as in [\[e13\]](#e13){reference-type="eqref" reference="e13"}, where the $\omega _{p,n}$ are in $\Zvv$. For each $k\ge 0$, we have $$\begin{split}
      \langle \omega ^p,\V'_{2k}\rangle 
      =\sum_{n\ge 0}\omega _{p,n}\langle P'_n,\V'_{2k}\rangle 
      =\sum_{n=0}^k \omega _{p,n}\{k+n\}_{2n}/\{n\}!.
    \end{split}$$ By computing the action of $\modr ^{-p}$ on the weight $0$ vector $\modv ^{2k}_k\in \V_{2k}$ using Proposition [\[r8\]](#r8){reference-type="ref" reference="r8"}, we obtain $$\trq^{\V'_{2k}}(\modr ^{-p})
    =\sum_{n=0}^k v^{\hf n(n+3)}\epsilon (a_{p,n})\BB{k+n}{2n}/\{n\}!,$$ where $a_{p,n}$ is given by [\[e14\]](#e14){reference-type="eqref" reference="e14"} and [\[e16\]](#e16){reference-type="eqref" reference="e16"}. Since $\langle \omega ^p,\V'_{2k}\rangle =\trq^{\V'_{2k}}(\modr ^{-p})$, we have $$\sum_{n=0}^k \omega _{p,n}\{k+n\}_{2n}/\{n\}!
    =\sum_{n=0}^k v^{\hf n(n+3)}\epsilon (a_{p,n})\BB{k+n}{2n}/\{n\}!$$ for all $k\ge 0$. Since $\BB{k+n}{2n}/\{n\}!\neq0$ whenever $0\le n\le k$, it follows that $\omega _{p,n}=v^{\hf n(n+3)}\epsilon (a_{p,n})$ for all $n\ge 0$, hence the assertion. ◻
:::

A skein-theoretic version of Proposition [\[r5\]](#r5){reference-type="ref" reference="r5"} has been given by Masbaum [@Masbaum].
